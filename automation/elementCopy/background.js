chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
      if(request.downloadUrl){
        chrome.action.onClicked.addListener((tab) => {
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      files: ['contentScript.js']
    });
  });
      }
    }
  );
  

  