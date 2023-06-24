// Flag to know whether a click event was triggered by the user or the script
let userClick = true;

// Function to collect and stringify styles
function collectAndStringifyStyles(el) {
  const styles = window.getComputedStyle(el);
  let styleStr = "";

  for(let prop of styles) {
    styleStr += `${prop}: ${styles.getPropertyValue(prop)}; `;
  }

  return styleStr;
}

document.body.addEventListener('click', function(e) {
  // Only proceed if the click was triggered by the user
  if (userClick) {
    e.preventDefault();
    userClick = false;  // Set the flag to false before triggering the click
    
    const el = e.target;
    const cloneEl = el.cloneNode(true);
    const styleNodes = Array.from(document.querySelectorAll('style, link[rel="stylesheet"]'));
    
    // Append the styles to the cloneEl
    styleNodes.forEach(styleNode => cloneEl.appendChild(styleNode.cloneNode(true)));
    
    let html = `<div style="${collectAndStringifyStyles(el)}">${cloneEl.outerHTML}</div>`;
    const blob = new Blob([html], {type: "text/html"});
    const url = URL.createObjectURL(blob);

    // Create an invisible link element, set its href attribute to the URL of the blob, 
    // and programmatically click it to trigger the download
    const link = document.createElement('a');
    link.href = url;
    link.download = 'element.html';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    
    userClick = true;  // Set the flag back to true after triggering the click
  }
});

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if(request.downloadUrl){
    chrome.action.onClicked.addListener((tab) => {
      chrome.scripting.executeScript({
        target: { tabId: tab.id },
        files: ['contentScript.js']
      });
    });
  }
});
