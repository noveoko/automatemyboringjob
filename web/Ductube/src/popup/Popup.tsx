import React, { useEffect, useState } from 'react';
import { v4 as uuidv4 } from 'uuid';
import { FilterRule, FilterSettings } from '../types/FilterTypes';
import { storageManager } from '../utils/storage';
import { FilterRuleForm } from './components/FilterRuleForm';
import { FilterRuleList } from './components/FilterRuleList';
import { ToggleSwitch } from './components/ToggleSwitch';

const Popup: React.FC = () => {
    const [settings, setSettings] = useState<FilterSettings | null>(null);
    const [currentSite, setCurrentSite] = useState<string>('');

    useEffect(() => {
        const loadData = async () => {
            const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
            if (tab.url) {
                const url = new URL(tab.url);
                setCurrentSite(url.hostname);
            }
            const settings = await storageManager.getSettings();
            setSettings(settings);
        };
        loadData();
    }, []);

    if (!settings) {
        return <div className="p-4">Loading...</div>;
    }

    const handleGlobalToggle = async (enabled: boolean) => {
        const newSettings = {
            ...settings,
            globalEnabled: enabled
        };
        await storageManager.saveSettings(newSettings);
        setSettings(newSettings);
    };

    const handleSiteToggle = async (enabled: boolean) => {
        const newSettings = {
            ...settings,
            siteSpecificSettings: {
                ...settings.siteSpecificSettings,
                [currentSite]: {
                    ...settings.siteSpecificSettings[currentSite],
                    enabled
                }
            }
        };
        await storageManager.saveSettings(newSettings);
        setSettings(newSettings);
    };

    const handleAddRule = async (rule: Omit<FilterRule, 'id' | 'createdAt' | 'lastModified'>) => {
        const newRule: FilterRule = {
            ...rule,
            id: uuidv4(),
            createdAt: Date.now(),
            lastModified: Date.now()
        };

        const newSettings = {
            ...settings,
            rules: [...settings.rules, newRule]
        };
        await storageManager.saveSettings(newSettings);
        setSettings(newSettings);
    };

    const handleToggleRule = async (ruleId: string) => {
        const newSettings = {
            ...settings,
            rules: settings.rules.map(rule =>
                rule.id === ruleId ? { ...rule, enabled: !rule.enabled } : rule
            )
        };
        await storageManager.saveSettings(newSettings);
        setSettings(newSettings);
    };

    const handleDeleteRule = async (ruleId: string) => {
        const newSettings = {
            ...settings,
            rules: settings.rules.filter(rule => rule.id !== ruleId)
        };
        await storageManager.saveSettings(newSettings);
        setSettings(newSettings);
    };

    return (
        <div className="w-96 p-4 space-y-6">
            <div className="space-y-4">
                <ToggleSwitch
                    enabled={settings.globalEnabled}
                    onChange={handleGlobalToggle}
                    label="Enable Content Filter"
                />

                {currentSite && (
                    <ToggleSwitch
                        enabled={settings.siteSpecificSettings[currentSite]?.enabled ?? true}
                        onChange={handleSiteToggle}
                        label={`Enable for ${currentSite}`}
                    />
                )}
            </div>

            <div className="border-t pt-4">
                <h2 className="text-lg font-medium mb-4">Filter Rules</h2>
                <FilterRuleForm onSubmit={handleAddRule} />
            </div>

            <div className="border-t pt-4">
                <FilterRuleList
                    rules={settings.rules}
                    onToggleRule={handleToggleRule}
                    onDeleteRule={handleDeleteRule}
                />
            </div>
        </div>
    );
};

export default Popup;