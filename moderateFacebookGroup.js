const rateContent = function(string){
    /*This module scores suspicious posts for removal
    Very little or no text (fewer than 5 words) = 0;
    Banned keywords in text = 0;
    */
    let tokens;
    let points = 1;
    let words = []
    let bannedKeywords = ['scam','bitcoin','totally free','last chance']
    try{string = string.toLowerCase();tokens = string.split(' ')}catch(error){
        //console.log(error);
        tokens=['null']
    }
    if(tokens.length>=10){
        bannedKeywords.forEach(word=>{
            if(string.includes(word)){
                points--;
                words.push(word)
            }
            })
    }else{return {score:0, words:words}}
    return {score:points, words:words}
    }
    
    const moderateContent = function(){
    window.scrollBy(3000, 0); // Scroll 100px to the right
    let stats = {declined:0,accepted:0}
    let targets = document.querySelectorAll("span");
    let matches = [];
    targets.forEach(target=>{
    if(target.textContent == 'Decline'){
    matches.push(target);
    }
    })
    count = 0;
    matches.forEach(match=>{
        count++;
        let post = match.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
        let spans = post.querySelectorAll("span");
        let approveButton;
        let declineButton;
        let body = post.querySelector("div[dir='auto']");
        let allText = post.textContent;
        spans.forEach(span=>{
            if(span.textContent=='Approve'){
                //approve found
                approveButton = span;
            }
            else if(span.textContent == 'Decline'){
                //decline found
                declineButton = span;
            }else{}
        })
        setTimeout(function(fullText){
            let score = rateContent(fullText);
            if(rateContent(allText).score<1){
                console.log("Declining!", rateContent(allText).words)
                declineButton.click();
                stats.declined++;
            }
            else{console.log("Will accept!")
                approveButton.click();
                stats.accepted++;
        }
         }, 3000);
    
    });
    
    if(count>=matches.length){
    console.log("Content Results:",stats)}
    }
    
    const removeAll= function(totalRuns=20){
        let runs = 0;
        const autoHelper = setInterval(function(){ 
            window.onscroll = function(ev) {
                if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
                    // you're at the bottom of the page
                }
            };
            moderateContent();
            runs++;
            console.log(`Run ${runs} of ${totalRuns}`)
         }, 6000);
         if(runs>=20){
            clearInterval(autoHelper)
         }
    }
    
    