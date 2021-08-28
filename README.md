# automatemyboringjob

![header](images/header.png)

Programs to automate YOUR boring job

#Example 1 Web Scraping in a Hurry
##Purpose
Grab all the headings on a website without installing any plugins

- Press CTRL+Shift+i
- In the _Developer's Tool Bar/Window_ click on **Console** to open the JavaScript console
- Copy the following script (between the `script content` tags):

```
var getHeadings = function(){
    data = document.querySelectorAll("h1,h2,h3,h4");
    for(i=0;i<data.length;i++){
        console.log(data[i].innerText);
}

};
getHeadings();
```

- Paste this script into your console, and hit `ENTER`
- Now just simply copy paste the headlines that have been printed in the console window

## Example result (from CNN.com):

```
White House preparing draft national emergency order
Trump administration has identified $7B in funds to build a border wall
ANALYSIS No one knows how Trump plans to end the shutdown
ANALYSIS A big lesson for Trump in Senate shutdown votes
Pelosi schools Trump in the art of power
Senator slams Ted Cruz's 'crocodile tears
...
```
