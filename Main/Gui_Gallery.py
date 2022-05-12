# original code from https://stackoverflow.com/questions/5787741/creating-a-photo-gallery-using-python

import os
from helper.load_custome_data import load_images_from_folder

path = '/home/ubuntu/studies/u-2i9S6_cORA1vaGucELFdF/AWS_WP3/'
#image_data = load_images_from_folder('dataset/', shuffle=False, width = width, height = height)
subfolders = [ f.path for f in os.scandir(path+'Gui_test_images/') if f.is_dir() ]
image_data = []
filenames = []
labels_names =[]
labels=[]
width = 20
height = 20
for folder in subfolders :


	image_data1, filenames1 = load_images_from_folder(folder, shuffle=False, width=width, height=height)

	image_data.append(image_data1)  # [*image_data, *image_data1] #image_data + image_data1
	filenames.append(filenames1)
	labels_names.append([folder[len(path + 'Gui_test_images/'):]] * len(image_data1))
	labels.append(folder[len(path + 'Gui_test_images/'):])

filenames = [item for sublist in filenames for item in sublist]
index = filenames[:20] #os.listdir('./Images')

x = len(index)

#for fname in index:
'''while x>0:
        x=x-1
        index[x] = '<a href="' + index[x].replace("jpg", "html") + '">' + '<img src="' + index[x] + '" />' + '</a>'''
index = ["".join(['<a href="', item.replace("jpg", "html"), '">', '<img src="', item, '" />', '</a>'])
             for item in filenames]

listString = '\n'.join(index)

title = os.getcwd()
title = title.split("/")
title = title.pop()

file = open("gallery_MRI_Sequences.html", 'w')

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

next= filenames[:20] #os.listdir('./Images')
image= filenames[:20] #os.listdir('./Images')
page= filenames[:20] #os.listdir('./Images')

next.append('gallery.html')

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