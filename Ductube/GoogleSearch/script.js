// ignore all keywords
console.log("Google Filter: RUNNING");

keywords = ['analyticsvidhya.com','machinelearningmastery.com','medium.com','geeksforgeeks.org']

function filterPage() {
    blocked = []
    console.log(`Filtering Pages...`)
    try{
    search_results = document.querySelector("#search").querySelectorAll("div")[1];
    search_divs = search_results.querySelectorAll("div")
    Array.from(search_divs).forEach((result)=>{
        contains_citation = result.querySelector("cite")
        if(contains_citation){
            top_div = contains_citation.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode
            top_div_url = top_div.querySelector("h3").textContent
            if(!blocked.includes(top_div_url)){
                    citation_url = contains_citation.textContent
                    for(i=0;i<keywords.length;i++){
                        candidate = keywords[i]
                        if(citation_url.includes(candidate)){
                            //hide content
                            try{
                                    console.log(`Hiding: ${candidate} at ${top_div_url}`)
                                    blocked.push(top_div_url)
                                    top_div.hidden=true
                                    continue
                            }
                            catch{
                                console.log(`Unable to hide: ${citation_url}`)
                            }
                        }
                    }
            }
        }

        
    })}
    catch{
        console.log("failure...")
    }
    
}

setInterval(filterPage,2000)



