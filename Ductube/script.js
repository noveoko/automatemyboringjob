// ignore all keywords
console.log("YT Filter: RUNNING");

keywords = ['nft','stonk','where to','should you','what happens', 'secret','could ','mansion','most ','mind-blowing','why ','in the life','how ','remix','top 1','top 2','behind the scene','hype','review','perfect','what i learned','introducing','session','music for','debunk','myth','3x','10x','100x','2x','how-to','how to','detox','clip','all time','making of','trailer','funn','loses it','react','free','hired','portlandia','better','faster','reaction','off grid','disturbing','renovating','silicon valley','epoxy','resin','most searched','adhd','motivated','procrastinate','audience','wants to','dumb','live','your friend','money','power','murder','bill burr','jeffries','comedian','trailer']
channels = ['hardware','laugh','motivat','comedy','power','nbc']

function filterYTPage() {
    console.log('Filtering YT Page...')
    let vids = document.getElementsByTagName('ytd-rich-item-renderer')
    let hidden = []
    for(i=0;i<vids.length;i++){
        video = vids[i]
        video_title = video.querySelector("#video-title").innerText
        channel_title = video.querySelector("#channel-name").innerText
        channel_title = channel_title.toLowerCase()
        for(j=0;j<channels.length;j++){
            if(channel_title.includes(channels[j])){
                video.style.display = "none"
                hidden.push(video)
                continue
            }
        }
        video_title = video_title.toLowerCase()
        for(j=0;j<keywords.length;j++){
            if(video_title.includes(keywords[j])){
                video.style.display = "none"
                hidden.push(video)
                continue
            }
        }
    }
//print results
    //console.log("YT Filter: HIDDEN " + hidden.length + " VIDEOS")
}

function filterRedditPage(){
    already_blocked = []
    console.log('Filtering Reddit Page...')
    headings = document.getElementsByTagName('h3')
    for(i=0;i<headings.length;i++){
        heading = headings[i]
        //heading contains any of the keywords
        heading_text = heading.innerText
        heading_text = heading_text.toLowerCase()
        if (!already_blocked.includes(heading_text)){
        for(j=0;j<keywords.length;j++){
            if(heading_text.includes(keywords[j])){
                console.log(`Hiding Element with name ${heading_text}`)
                headings[i].parentNode.parentNode.parentNode.parentNode.parentNode.textContent='💀'
                already_blocked.push(heading_text)
                continue
            }
    }}
}}


if (document.URL.startsWith("https://www.youtube.com")){
    setInterval(filterYTPage, 800)
}
else if (document.URL.startsWith("https://www.reddit.com")){
    setInterval(filterRedditPage,2000)
}


