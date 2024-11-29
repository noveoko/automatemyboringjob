import { FilterRule, FilterSettings } from '../types/FilterTypes';

class ContentFilter {
    private settings: FilterSettings | null = null;
    private observer: MutationObserver | null = null;
    private processTimer: number | null = null;

    constructor() {
        this.initialize();
    }

    private async initialize(): Promise<void> {
        await this.loadSettings();
        this.setupMessageListener();
        this.setupObserver();
        this.processPage();
    }

    private async loadSettings(): Promise<void> {
        try {
            const response = await chrome.runtime.sendMessage({ type: 'GET_SETTINGS' });
            this.settings = response;
        } catch (error) {
            console.error('Failed to load settings:', error);
        }
    }

    private setupMessageListener(): void {
        chrome.runtime.onMessage.addListener(async (message) => {
            if (message.type === 'SETTINGS_UPDATED') {
                await this.loadSettings();
                this.processPage();
            }
        });
    }

    private setupObserver(): void {
        this.observer = new MutationObserver((mutations) => {
            if (this.processTimer) {
                window.clearTimeout(this.processTimer);
            }

            this.processTimer = window.setTimeout(() => {
                const addedNodes = mutations.flatMap(m => Array.from(m.addedNodes));
                this.processNodes(addedNodes);
            }, 100);
        });

        this.observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    }

    private shouldFilter(): boolean {
        if (!this.settings?.globalEnabled) return false;

        const currentSite = window.location.hostname;
        const siteSettings = this.settings.siteSpecificSettings[currentSite];

        return siteSettings?.enabled ?? true;
    }

    private getActiveRules(): FilterRule[] {
        if (!this.settings) return [];

        const currentSite = window.location.hostname;
        const siteSettings = this.settings.siteSpecificSettings[currentSite];

        return this.settings.rules.filter(rule => {
            if (!rule.enabled) return false;
            if (!rule.targetSite) return true;
            return rule.targetSite === currentSite;
        });
    }

    private processPage(): void {
        if (!this.shouldFilter()) return;

        const rules = this.getActiveRules();
        this.processNodes([document.body], rules);
    }

    private processNodes(nodes: Node[], rules: FilterRule[] = this.getActiveRules()): void {
        if (!this.shouldFilter()) return;

        nodes.forEach(node => {
            if (node instanceof Element) {
                this.processElement(node, rules);
                node.querySelectorAll('*').forEach(el => this.processElement(el, rules));
            }
        });
    }

    private processElement(element: Element, rules: FilterRule[]): void {
        for (const rule of rules) {
            if (this.matchesRule(element, rule)) {
                this.hideElement(element);
                break;
            }
        }
    }

    private matchesRule(element: Element, rule: FilterRule): boolean {
        const text = element.textContent?.toLowerCase() || '';

        switch (rule.type) {
            case 'keyword':
                return text.includes(rule.value.toLowerCase());

            case 'website':
                if (element instanceof HTMLAnchorElement) {
                    return element.href.includes(rule.value.toLowerCase());
                }
                return false;

            case 'element':
                return element.matches(rule.value);

            case 'rating':
                return this.matchesRating(element, rule.value);

            default:
                return false;
        }
    }

    private matchesRating(element: Element, rating: string): boolean {
        if (window.location.hostname.includes('youtube.com')) {
            const ratingIndicator = element.querySelector('[aria-label*="rating"]');
            if (ratingIndicator) {
                const ratingText = ratingIndicator.getAttribute('aria-label') || '';
                return ratingText.toLowerCase().includes(rating.toLowerCase());
            }
        }
        return false;
    }

    private hideElement(element: Element): void {
        if (element.hasAttribute('data-filter-hidden')) return;

        element.setAttribute('data-filter-hidden', 'true');
        element.setAttribute('data-original-display', getComputedStyle(element).display);
        (element as HTMLElement).style.display = 'none';

        const indicator = document.createElement('div');
        indicator.className = 'filter-indicator';
        indicator.textContent = 'Content filtered';
        indicator.onclick = () => this.toggleElementVisibility(element, indicator);
        element.parentElement?.insertBefore(indicator, element);
    }

    private toggleElementVisibility(element: Element, indicator: HTMLElement): void {
        const isHidden = element.hasAttribute('data-filter-hidden');
        if (isHidden) {
            element.removeAttribute('data-filter-hidden');
            (element as HTMLElement).style.display =
                element.getAttribute('data-original-display') || 'block';
            indicator.textContent = 'Hide filtered content';
        } else {
            element.setAttribute('data-filter-hidden', 'true');
            (element as HTMLElement).style.display = 'none';
            indicator.textContent = 'Content filtered';
        }
    }
}

// Initialize the content filter
new ContentFilter();