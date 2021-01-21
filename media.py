import os

extensions = ['psd','pdf','ai','indd','blend','tif','tiff','bmp','jpg','jpeg','gif','png','eps','raw','cr2','nef','orf','sr2','webm','mpg','mp2','mpeg','mpe','mpv','ogg','mp4','m4p','m4v','avi','wmv','mov','qt','flv','swf','avchd']
compressions = ['7z','s7z','ace','afa','alz','apk','arc','ark','arc','cdx','arj','b1','b6z','ba','bh','cab','car','cfs','cpt','dar','dd','dgc','dmg','ear','gca','ha','hki','ice','jar','kgb','lzh','lha','lzx','pak','partimg','paq6','paq7','paq8','pea','pim','pit','qda','rar','rk','sda','sea','sen','sfx','shk','sit','sitx','sqx','gz','tgz','bz2','tbz2','lz','tlz','xz','txz','uc','uc0','uc2','ucn','ur2','ue2','uca','uha','war','wim','xar','xp3','yz1','zip','zipx','zoo','zpaq','zz']

exts = {a:set() for a in extensions}
comps = {a:set() for a in compressions}

with open('everyFile.txt','r',encoding='utf-8') as infile:
    for line in infile.readlines():
        ext = line.split(".")[-1].strip()
        if ext in extensions:
            exts[ext].add(line)
        if ext in compressions:
            comps[ext].add(line)

print("FILES")
for fileType, links in exts.items():
    size = len(links)
    if size>0:
        print(fileType,len(links) )

print("FILES")
dimensions = {"small":set(),"medium":set(),"large":set(),"huge":set()}
for fileType, links in comps.items():
    if len(links) > 0:
        for link in links:
            link = link.strip()
            try:
                stats = os.stat(link)
                size = stats.st_size / (1024*1024)
                if 0 < size < 10:
                    dimensions["small"].add(link)
                if 10 < size < 100:
                    dimensions["medium"].add(link)
                if 100 < size < 1000:
                    dimensions["large"].add(link)
                if 1000 < size < 10000000:
                    dimensions["huge"].add(link)
            except Exception as ee:
                print(ee)


with open('compressedFiles.txt','w',encoding='utf-8') as outfile:
    for dim, links in dimensions:
        for link in links:
            outfile.write(f"{dim}\t{link}\n")