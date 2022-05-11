#################################
file = open("gallery_MRI_Sequences_labls.html", 'w')

file.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"' + '\n')
file.write('    "http://www.w3.org/TR/html4/loose.dtd">' + '\n')
file.write('<html>' + '\n')
file.write('<title>' + title + '</title>' + '\n')
file.write('<head>' + '\n')
file.write('<style>' + '\n')
file.write('body {font-size:small;padding:10px;background-color:black;margin-left:15%;margin-right:15%;font-family:"Lucida Grande",Verdana,Arial,Sans-Serif;color: white;}' + '\n')
file.write('img {border-style:solid;border-width:5px;border-color:white;}' + '\n')
file.write('h1 {text-align:center;}' + '\n')
file.write('a:link {color: grey; text-decoration: none;}' + '\n')
file.write('a:visited {color: grey; text-decoration: none;}' + '\n')
file.write('a:active {color: grey; text-decoration: none;}' + '\n')
file.write('a:hover {color: grey;text-decoration: underline;}' + '\n')
file.write('</style>' + '\n')
file.write('</head>' + '\n')
file.write('<body>' + '\n')
file.write('<h1>' + title + '</h1>' + '\n')
file.write(listString + '\n')
file.write('</body>' + '\n')
file.write('</html>')

file.close()

next= filenames #os.listdir('./Images')
image= filenames #os.listdir('./Images')
page= filenames #os.listdir('./Images')

next.append('gallery_MRI_Sequences.html')

x=len(next)
y=len(page)
z=len(image)

for fname in page:
    while y>0:
        y=y-1
        x=x-1
        z=z-1
        page[y] = page[y].replace("jpg", "html")
        file = open(page[y], 'w')
        file.write('<html>' + '\n')
        file.write('<title>' + title + '</title>' + '\n')
        file.write('<head>' + '\n')
        file.write('<script type="text/javascript">function delayer(){window.location = "./' + next[x].replace("jpg", "html") +'"}</script>' + '\n')
        file.write('<style>' + '\n')
        file.write('body {font-size:small;text-align:center;background-color:black;font-family:"Lucida Grande",Verdana,Arial,Sans-Serif;color: white;}' + '\n')
        file.write('a:link {color: white; text-decoration: none;}' + '\n')
        file.write('a:visited {color: white; text-decoration: none;}' + '\n')
        file.write('a:active {color: white; text-decoration: none;}' + '\n')
        file.write('a:hover {color: white;text-decoration: underline;}' + '\n')
        file.write('</style>' + '\n')
        file.write('</head>' + '\n')
        file.write('<body onLoad="setTimeout(\'delayer()\', 3000)">' + '\n')
        file.write('<p><a href="gallery.html">' + title + '</a></p>' + '\n')
        file.write('<a href="' + next[x].replace("jpg", "html") + '">' + '<img height="10%" src="' + image[z] + '" />' + 'Test'+' </a>')
        file.write('</body>' + '\n')
        file.write('</html>')
        file.close()