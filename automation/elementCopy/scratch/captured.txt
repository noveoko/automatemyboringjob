// Flag to know whether a click event was triggered by the user or the script
let userClick = true;

document.body.addEventListener('click', function(e) {
  // Only proceed if the click was triggered by the user
  if (userClick) {
    e.preventDefault();
    var el = e.target;

    var html = el.outerHTML;
    var cloneEl = el.cloneNode(true);

    var styleNodes = Array.from(document.querySelectorAll('style, link[rel="stylesheet"]'));
    var scriptNodes = Array.from(document.querySelectorAll('script'));

    var styles = window.getComputedStyle(el);
    var styleStr = "";
    for(var prop of styles) {
      styleStr += `${prop}: ${styles.getPropertyValue(prop)}; `;
    }
    html = `<div style="${styleStr}">${html}</div>`;
    
    // Append the styles and scripts to the cloneEl
    styleNodes.forEach(styleNode => cloneEl.appendChild(styleNode.cloneNode(true)));
    scriptNodes.forEach(scriptNode => cloneEl.appendChild(scriptNode.cloneNode(true)));

    // Convert the cloneEl to a string
    html = cloneEl.outerHTML;

    var blob = new Blob([html], {type: "text/html"});
    var url = URL.createObjectURL(blob);

    // Create an invisible link element, set its href attribute to the URL of the blob, 
    // and programmatically click it to trigger the download
    var link = document.createElement('a');
    link.href = url;
    link.download = 'element.html';
    document.body.appendChild(link);
    userClick = false;  // Set the flag to false before triggering the click
    link.click();
    document.body.removeChild(link);
    userClick = true;  // Set the flag back to true after triggering the click
  }
});
