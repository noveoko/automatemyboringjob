function get_google_results(){
let links = []
let results = document.querySelectorAll('h3');
results.forEach(result =>{
    link = result.parentElement.parentElement.querySelector("a").href
    links.push(link);
})
return links
}

function downloadArrayAsTextFile(array) {
    // Generate a random filename using Date and Math.random
    const filename = `list_${Date.now()}_${Math.floor(Math.random() * 10000)}.txt`;
    
    // Join the array items into a single string with each item on a new line
    const text = array.join('\n');
    
    // Create a Blob with the text content
    const blob = new Blob([text], { type: 'text/plain' });
    
    // Create a link element
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = filename;
    
    // Programmatically click the link to trigger the download
    document.body.appendChild(link);
    link.click();
    
    // Clean up by removing the link element
    document.body.removeChild(link);
}

function download_links(){
    results = get_google_results()
    downloadArrayAsTextFile(results);
}

function click_next(){
    let button = document.querySelector("span[style='display:block;margin-left:53px']");
    button.click();
}
download_links
click_next()
