import { FilterSettings } from '../types/FilterTypes';

class StorageManager {
    private static instance: StorageManager;
    private cache: { settings?: FilterSettings } = {};

    private constructor() { }

    static getInstance(): StorageManager {
        if (!StorageManager.instance) {
            StorageManager.instance = new StorageManager();
        }
        return StorageManager.instance;
    }

    async getSettings(): Promise<FilterSettings> {
        if (this.cache.settings) {
            return this.cache.settings;
        }

        const result = await chrome.storage.local.get('filterSettings');
        const settings = result.filterSettings || this.getDefaultSettings();
        this.cache.settings = settings;
        return settings;
    }

    async saveSettings(settings: FilterSettings): Promise<void> {
        this.cache.settings = settings;
        await chrome.storage.local.set({ filterSettings: settings });
        await this.notifySettingsChanged();
    }

    private async notifySettingsChanged(): Promise<void> {
        const tabs = await chrome.tabs.query({});
        tabs.forEach(tab => {
            if (tab.id) {
                chrome.tabs.sendMessage(tab.id, { type: 'SETTINGS_UPDATED' })
                    .catch(() => { }); // Ignore errors for inactive tabs
            }
        });
    }

    private getDefaultSettings(): FilterSettings {
        return {
            globalEnabled: true,
            rules: [],
            siteSpecificSettings: {}
        };
    }
}

export const storageManager = StorageManager.getInstance();