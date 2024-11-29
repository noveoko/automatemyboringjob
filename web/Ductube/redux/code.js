// manifest.json
{
  "manifest_version": 3,
  "name": "Smart Content Filter",
  "version": "1.0.0",
  "description": "Filter unwanted content across various websites",
  "permissions": [
    "storage",
    "activeTab",
    "scripting"
  ],
  "host_permissions": [
    "*://*/*"
  ],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  "background": {
    "service_worker": "background.ts",
    "type": "module"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["contentScript.ts"]
    }
  ]
}

// src/types/FilterTypes.ts
export interface FilterRule {
  id: string;
  type: 'keyword' | 'website' | 'element' | 'rating';
  value: string;
  enabled: boolean;
  site?: string;
}

export interface FilterState {
  rules: FilterRule[];
  enabled: boolean;
}

// src/popup/Popup.tsx
import React, { useState, useEffect } from 'react';
import { FilterRule, FilterState } from '../types/FilterTypes';

const Popup: React.FC = () => {
  const [filterState, setFilterState] = useState<FilterState>({
    rules: [],
    enabled: true
  });

  useEffect(() => {
    // Load saved filter state
    chrome.storage.sync.get(['filterState'], (result) => {
      if (result.filterState) {
        setFilterState(result.filterState);
      }
    });
  }, []);

  const toggleExtension = () => {
    const newState = { ...filterState, enabled: !filterState.enabled };
    setFilterState(newState);
    chrome.storage.sync.set({ filterState: newState });
    
    // Notify content script
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      if (tabs[0].id) {
        chrome.tabs.sendMessage(tabs[0].id, { 
          type: 'TOGGLE_FILTER',
          enabled: newState.enabled 
        });
      }
    });
  };

  const addRule = (rule: Omit<FilterRule, 'id'>) => {
    const newRule = { ...rule, id: Date.now().toString() };
    const newState = {
      ...filterState,
      rules: [...filterState.rules, newRule]
    };
    setFilterState(newState);
    chrome.storage.sync.set({ filterState: newState });
  };

  return (
    <div className="w-80 p-4">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-xl font-bold">Smart Content Filter</h1>
        <button
          onClick={toggleExtension}
          className={`px-4 py-2 rounded ${
            filterState.enabled ? 'bg-green-500' : 'bg-red-500'
          } text-white`}
        >
          {filterState.enabled ? 'Enabled' : 'Disabled'}
        </button>
      </div>
      <FilterRuleForm onSubmit={addRule} />
      <RuleList rules={filterState.rules} />
    </div>
  );
};

// src/contentScript.ts
import { FilterRule, FilterState } from './types/FilterTypes';

class ContentFilter {
  private filterState: FilterState = { rules: [], enabled: true };
  
  constructor() {
    this.initialize();
    this.setupMutationObserver();
  }

  private async initialize() {
    const result = await chrome.storage.sync.get(['filterState']);
    if (result.filterState) {
      this.filterState = result.filterState;
      this.applyFilters();
    }

    // Listen for messages from popup
    chrome.runtime.onMessage.addListener((message) => {
      if (message.type === 'TOGGLE_FILTER') {
        this.filterState.enabled = message.enabled;
        this.applyFilters();
      }
    });
  }

  private setupMutationObserver() {
    const observer = new MutationObserver((mutations) => {
      if (this.filterState.enabled) {
        this.applyFilters();
      }
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  }

  private applyFilters() {
    if (!this.filterState.enabled) {
      this.showAllContent();
      return;
    }

    this.filterState.rules.forEach((rule) => {
      if (!rule.enabled) return;

      switch (rule.type) {
        case 'keyword':
          this.filterByKeyword(rule.value);
          break;
        case 'website':
          this.filterByWebsite(rule.value);
          break;
        case 'element':
          this.filterByElement(rule.value);
          break;
        case 'rating':
          this.filterByRating(rule.value);
          break;
      }
    });
  }

  private filterByKeyword(keyword: string) {
    const elements = document.querySelectorAll('*');
    elements.forEach((element) => {
      if (element.textContent?.toLowerCase().includes(keyword.toLowerCase())) {
        this.hideElement(element as HTMLElement);
      }
    });
  }

  private filterByWebsite(website: string) {
    if (window.location.hostname.includes(website)) {
      // Apply website-specific filters
      this.applyWebsiteSpecificFilters(website);
    }
  }

  private filterByElement(selector: string) {
    const elements = document.querySelectorAll(selector);
    elements.forEach((element) => {
      this.hideElement(element as HTMLElement);
    });
  }

  private filterByRating(minRating: string) {
    // Example for Netflix
    if (window.location.hostname.includes('netflix.com')) {
      const ratingElements = document.querySelectorAll('[data-rating]');
      ratingElements.forEach((element) => {
        const rating = parseFloat(element.getAttribute('data-rating') || '0');
        if (rating < parseFloat(minRating)) {
          this.hideElement(element.closest('.title-card') as HTMLElement);
        }
      });
    }
  }

  private hideElement(element: HTMLElement) {
    if (!element.dataset.filteredContent) {
      element.dataset.filteredContent = 'true';
      element.style.display = 'none';
      this.showFilterFeedback(element);
    }
  }

  private showFilterFeedback(element: HTMLElement) {
    const feedback = document.createElement('div');
    feedback.className = 'filter-feedback';
    feedback.textContent = 'Content filtered';
    feedback.style.cssText = `
      background: rgba(0,0,0,0.1);
      padding: 8px;
      margin: 4px 0;
      border-radius: 4px;
      font-size: 12px;
      color: #666;
      text-align: center;
    `;
    element.parentNode?.insertBefore(feedback, element);
  }

  private showAllContent() {
    const filteredElements = document.querySelectorAll('[data-filtered-content]');
    filteredElements.forEach((element) => {
      (element as HTMLElement).style.display = '';
      delete (element as HTMLElement).dataset.filteredContent;
    });

    const feedbackElements = document.querySelectorAll('.filter-feedback');
    feedbackElements.forEach((element) => element.remove());
  }

  private applyWebsiteSpecificFilters(website: string) {
    const siteSpecificRules: Record<string, () => void> = {
      'youtube.com': () => {
        // YouTube specific filtering
        const videoCards = document.querySelectorAll('ytd-video-renderer');
        videoCards.forEach((card) => {
          const title = card.querySelector('#video-title')?.textContent?.toLowerCase();
          if (title && this.shouldFilterYouTubeVideo(title)) {
            this.hideElement(card as HTMLElement);
          }
        });
      },
      'linkedin.com': () => {
        // LinkedIn specific filtering
        const posts = document.querySelectorAll('.feed-shared-update-v2');
        posts.forEach((post) => {
          const content = post.textContent?.toLowerCase();
          if (content && this.shouldFilterLinkedInPost(content)) {
            this.hideElement(post as HTMLElement);
          }
        });
      }
      // Add more website-specific filters as needed
    };

    const filterFn = siteSpecificRules[website];
    if (filterFn) filterFn();
  }

  private shouldFilterYouTubeVideo(title: string): boolean {
    return this.filterState.rules
      .filter(rule => rule.enabled && rule.site === 'youtube.com')
      .some(rule => title.includes(rule.value.toLowerCase()));
  }

  private shouldFilterLinkedInPost(content: string): boolean {
    return this.filterState.rules
      .filter(rule => rule.enabled && rule.site === 'linkedin.com')
      .some(rule => content.includes(rule.value.toLowerCase()));
  }
}

// Initialize content filter
new ContentFilter();