# automatemyboringjob

![header](images/header.png)

Programs to automate YOUR boring job

# Example 1 Web Scraping in a Hurry

## Purpose
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
# Example 2: Remove Duplicate Files

from the remove_duplicate_files directory run:
`python delete_duplicates.py`
You will be prompted for a root path and then once you hit enter the following steps will take place:

1. All files will be found and opened and assigned a hash number using Python's built in `hash` module.
2. Next all superfluous files with more than one hash will be deleted.
3. At the end you will be promted to clean up the files created or leave them as they are.
 
# Example 3: Convert a Directory of PDF files into Audio books

Run
`python ebook_to_audiobook.py <path_to_your_PDF_directory>`


