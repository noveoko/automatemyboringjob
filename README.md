# automatemyboringjob
Programs to automate YOUR boring job

#Example 1 Web Scraping in a Hurry
##Purpose
Grab all the headings on a website without installing any plugins

* Press CTRL+Shift+i
* In the *Developer's Tool Bar/Window* click on **Console** to open the JavaScript console
* Copy the following script (between the ``` script content ``` tags):
```
var heads = document.querySelectorAll("h1,h2,h3,h4");
for (i = 0; i < heads.length; i++){
		console.log(heads[i].innerText)
	};
```
* Paste this script into your console, and hit `ENTER`
* Now just simply copy paste the headlines that have been printed in the console window

## Example result (from CNN.com):
```
White House preparing draft national emergency order
VM29150:3 Trump administration has identified $7B in funds to build a border wall
VM29150:3 ANALYSIS No one knows how Trump plans to end the shutdown
VM29150:3 ANALYSIS A big lesson for Trump in Senate shutdown votes
VM29150:3 Pelosi schools Trump in the art of power
VM29150:3 Senator slams Ted Cruz's 'crocodile tears
...
```
