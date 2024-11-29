import { storageManager } from '../utils/storage';

chrome.runtime.onInstalled.addListener(async () => {
    // Initialize settings on install
    await storageManager.getSettings();
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type === 'GET_SETTINGS') {
        storageManager.getSettings().then(sendResponse);
        return true;
    }
});

// Ensure content scripts are injected into existing tabs on update/install
chrome.runtime.onInstalled.addListener(async () => {
    const tabs = await chrome.tabs.query({ url: ['http://*/*', 'https://*/*'] });
    for (const tab of tabs) {
        if (tab.id) {
            try {
                await chrome.scripting.executeScript({
                    target: { tabId: tab.id },
                    files: ['contentScript.js']
                });
            } catch (e) {
                console.error(`Failed to inject into tab ${tab.id}:`, e);
            }
        }
    }
});