window.addEventListener('DOMContentLoaded', (event) => {
  document.getElementById("grab").addEventListener('click', () => {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      if (chrome.scripting) {
        chrome.scripting.executeScript({
          target: {tabId: tabs[0].id},
          files: ['contentScript.js']
        });
      }
    });
  });
});
