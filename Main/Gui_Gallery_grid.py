# original code from https://stackoverflow.com/questions/5787741/creating-a-photo-gallery-using-python
### Script to get result of classification from result file and display them in a gallery for relabellinh

import os
from helper.load_custome_data import load_images_from_folder

project_path = '/Users/esmamansouri/PycharmProjects/WP3_SMI/'

path = '/Users/esmamansouri/DUNDEE/Dundee/WP3/Autoencoder-image-search-master/MRISeq/IXItest/'

#image_data = load_images_from_folder('dataset/', shuffle=False, width = width, height = height)




# get file names and labels from classification results
file = open(project_path+'output/MRI_Sequence_Results.txt', 'r')

filen = project_path+'output/MRI_Sequence_Results.txt'

filen_cor = project_path+'output/MRI_Sequence_Results_corrected.txt'

labels = []
fnames = []
for line in file:
    fname = line.split(',')
    labels.append(fname[0])
    fnames.append(fname[1][:-1])








title = os.getcwd()
title = title.split("/")
title = title.pop()
file = open(project_path+"gallery_MRI_Sequences_labls.html", 'w')


file.write('<!DOCTYPE html>' + '\n')
file.write('<html>' + '\n')
file.write('<head>' + '\n')
file.write('<meta name="viewport" content="width=device-width, initial-scale-1">' + '\n')
file.write('<style>' + '\n')
file.write('*{' + '\n')
file.write('box-sizing: border-box;' + '\n')
file.write('}'+'\n')
file.write('* {' + '\n')
file.write('box-sizing: border-box;' + '\n')
file.write('}' + '\n')

file.write('body {' + '\n')
file.write( 'background-color: #f1f1f1;' + '\n')
file.write( 'padding: 20px;' + '\n')
file.write( 'font-family: Arial;' + '\n')
file.write('}')

file.write('/* Center website */' + '\n')
file.write('.main {' + '\n')
file.write(' max-width: 1000px;' + '\n')
file.write(' margin: auto;' + '\n')
file.write('}' + '\n')
file.write('h1 {' + '\n')
file.write('font-size: 50px;' + '\n')
file.write('word-break: break-all;' + '\n')
file.write('}' + '\n')

file.write('.row {' + '\n')
file.write('  margin: 8px -16px;' + '\n')
file.write('}' + '\n')

file.write('/* Add padding BETWEEN each column (if you want) */' + '\n')
file.write('.row,' + '\n')
file.write('.row > .column {' + '\n')
file.write('  padding: 8px;' + '\n')
file.write('}' + '\n')

file.write('/* Create three equal columns that floats next to each other */' + '\n')
file.write('.column {' + '\n')
file.write('  float: left;' + '\n')
file.write('  width: 33.33%;' + '\n')
file.write('  display: none; /* Hide columns by default */' + '\n')
file.write('}'+'\n')

file.write('/* Clear floats after rows */' + '\n')
file.write('.row:after {' + '\n')
file.write('  content: "";' + '\n')
file.write('  display: table;' + '\n')
file.write('  clear: both;' + '\n')
file.write('}' +'\n')

file.write('/* Content */' + '\n')
file.write('.content {' + '\n')
file.write('  background-color: white;' + '\n')
file.write('  padding: 10px;' + '\n')
file.write('}' + '\n')

file.write('/* The "show" class is added to the filtered elements */' + '\n')
file.write('.show {' + '\n')
file.write('  display: block;' + '\n')
file.write('}' + '\n')

file.write('/* Style the buttons */' + '\n')
file.write('.btn {' + '\n')
file.write('  border: none;' + '\n')
file.write('  outline: none;' + '\n')
file.write('  padding: 12px 16px;' + '\n')
file.write('  background-color: white;' + '\n')
file.write('  cursor: pointer;' + '\n')
file.write('}' + '\n')

file.write('/* Add a grey background color on mouse-over */' + '\n')
file.write('.btn:hover {' + '\n')
file.write('  background-color: #ddd;' + '\n')
file.write('}' +'\n')

file.write('/* Add a dark background color to the active button */' + '\n')
file.write('.btn.active {' + '\n')
file.write('  background-color: #666;' + '\n')
file.write('   color: white;' + '\n')
file.write('}'+'\n')
file.write('    </style>' + '\n')
file.write('</head>' + '\n')



file.write('<body>' + '\n')

file.write('<h2>MRI Sequence Classifier</h2>' + '\n')
file.write('<div id = "BtnContainer">' + '\n')
file.write('    <button class = "btn active" onclick="filterSelection(\'all\')"> Show all</button>' + '\n')
file.write('    <button class = "btn active" onclick="filterSelection(\'T1\')"> T1</button>' + '\n')
file.write('    <button class = "btn active" onclick="filterSelection(\'T2\')"> T2</button>' + '\n')
file.write('   <button class = "btn active" onclick="filterSelection(\'MRA\')"> MRA</button>' + '\n')
file.write('   <button class = "btn active" onclick="filterSelection(\'PD\')"> PD</button>' + '\n')
file.write('   <button class = "btn active" onclick="filterSelection(\'DTI\')"> DTI</button>' + '\n')
file.write('</div>' + '\n')
file.write('<!-- Gallery Grid -->' + '\n')



# get all labelled T1


file.write('<script language="JScript">' + '\n')
file.write('var textToSave = \' \';' + '\n')
file.write('</script>' + '\n')


classes = ['T1', 'T2', 'MRA', 'PD', 'DTI']
for cl in classes:
    #find indices of files having the same label
    rows = 0
    class_el_counter = 1
    class_indices = [i for i, s in enumerate(labels) if cl in s]
    l = len(class_indices)
    if l >10:
        grid_size = 5
    else:
        grid_size = l
    if len(class_indices) > 0:
        for f in class_indices: #range(0, len(fnames)):
            #if cl in labels[f]:


                if rows % grid_size == 0 :
                    file.write('<div class="row">' + '\n')
                    file.write('  <div class="column ' + cl + '">' + '\n')
                    file.write('    <div class="content">' + '\n')
                    rows = 0
                if rows < grid_size:
                    file.write(
                        '      <img src="file://'+ fnames[f]+'" alt="' +cl+'" style="width:50%">' + '\n')
                    '''file.write(
                        '      <img src="file:///home/ubuntu/studies/u-2i9S6_cORA1vaGucELFdF/AWS_WP3/Gui_test_images/IXI002-Guys-0828-PD.jpeg" alt="T1" style="width:100%">' + '\n')
                    file.write(
                        '      <img src="file:///home/ubuntu/studies/u-2i9S6_cORA1vaGucELFdF/AWS_WP3/Gui_test_images/IXI002-Guys-0828-PD.jpeg" alt="T1" style="width:100%">' + '\n')'''
                    #file.write('      <h4 id = '+ fnames[f]+' contentEditable="true">'+labels[f]+'</h4>' + '\n')

                    file.write('      <textarea id = "'+fnames[f]+'" >' + labels[f] + '</textarea>' + '\n')
                    #file.write('    <button id = "'+fnames[f]+'b" onclick="captureLabel()" >confirm</button> ' + '\n')
                    file.write('<button class = "btn active"  button id = "'+fnames[f]+'b" onclick="textToSave = captureLabel(\''+fnames[f]+'\', \''+labels[f]+'\', textToSave )"> ok</button>' + '\n')
                    ## get edited label
                    #file.write(' <script>' + '\n')
                    '''file.write(' function captureLabel(filename)' + '\n')
                    file.write(' {' + '\n')
                    file.write(' document.getElementById("'+ fnames[f] +'").value = "Fifth Avenue, New York City";' + '\n')
                    
                    file.write('}' + '\n')
                    file.write('</script >' + '\n')'''




                    #file.write('    <button id = ' + fnames[f] + ')" > confirm</button> ' + '\n')

                    ###### oldfile.write('      <h4 id = ' + fnames[f] + ' contentEditable="true">' + labels[f] + '</h4>' + '\n')

                    #file.write('     <p>Lorem ipsum dolor..</p>' + '\n')
                    rows += 1

                if rows % grid_size == 0:
                    file.write('    </div>' + '\n')
                    file.write('  </div>' + '\n')
                    #rows = 0
                if class_el_counter == len(class_indices):
                    file.write('    </div>' + '\n')
                    file.write('  </div>' + '\n')
                class_el_counter +=1

    file.write('</div>' + '\n')






#file.write('<script src="js/FileSaver.js"></script>' + '\n')
file.write('<script language="JScript">' + '\n')

file.write('function captureLabel(name, label, textToSave) {' + '\n')
file.write('var new_label = document.getElementById(name).value;' + '\n')
#file.write('document.getElementById(name).value ="TEST";' + '\n')
file.write('var old_label = label;'+'\n')
file.write('var new_line = new_label.concat(\',\' , name);' + '\n')
file.write('var old_line = old_label.concat(\',\' , name);' + '\n')

#file.write('var textToSave = new_line;' + '\n')

file.write('textToSave = textToSave.concat( \';\' , new_line);' + '\n') #new_line;' + '\n')

file.write('var hiddenElement = document.createElement(\'a\');' + '\n')

file.write('hiddenElement.href = \'data:attachment/text,\' + encodeURI(textToSave);' + '\n')
file.write('hiddenElement.target = \'_blank\';' + '\n')
file.write('hiddenElement.download = \'file//'+filen_cor+'\';' + '\n')
file.write('hiddenElement.click();' + '\n')
file.write('return textToSave;' + '\n')




'''file.write('var blob = new Blob([new_line],{ type: "text/plain;charset=utf-8" });' + '\n')
file.write('saveAs(blob, \'file//'+filen_cor+'\');'+ '\n')'''

'''file.write('const writeStream = fs.createWriteStream(\'file//'+filen_cor+'\');' + '\n')
file.write('const encoder = new TextEncoder;' + '\n')
file.write('let data = \'a\'.repeat(1024);' + '\n')
file.write('let uint8array = encoder.encode(data + "\n\n");' + '\n')

file.write('writeStream.write(uint8array);' + '\n')
file.write('writeStream.close();' + '\n')'''


'''file.write('var fso = new CreateObject("Scripting.FileSystemObject");' + '\n')
file.write('var s = fso.OpenTextFile(\'file'+filen_cor+'\', 8, true, -2);' + '\n')
file.write('s.WriteLine(new_label);' + '\n')
file.write('s.WriteLine(name);' + '\n')
file.write('s.WriteLine("-----------------------------");' + '\n')
file.write('s.Close();' + '\n')'''
# file.write('if (new_label !== "") {' + '\n')
# get modified label
'''file.write('var fs = require(\'fs\');'+ '\n')
file.write('fs.writeFile(\'file://'+filen_cor+'\',  \'utf8\', function(err, new_line) {' + '\n')
file.write('if (err) {' + '\n')
file.write(' return console.log(err)' + '\n')
file.write('})' + '\n')'''
'''file.write('let searchString = name;' + '\n')


file.write(' var old_label = label;'+'\n')
file.write(' var new_line = new_label.concat(\',\' , searchString);' + '\n')
file.write(' var old_line = old_label.concat(\',\' , searchString);' + '\n')
file.write('  let re = new RegExp(\'^.*\' + searchString + \'.*$\', \'gm\');' + '\n')
file.write('  var formatted = data.replace(old_line, new_line);' + '\n')
file.write('  fs.writeFile(\'file://'+filen_cor+'\', \'utf8\', function(err) {' + '\n')
file.write('    if (err) return console.log(err);' + '\n')
file.write('  });' + '\n')
file.write('});' + '\n')'''


### search for the lie in the result text file
# file.write('fs.readFile('+filen+', \'utf8\', function(err, data) {' + '\n')

##file.write('var fs = require(\'fs\')' + '\n')
##file.write('fs.readFile(\''+filen+'\', \'utf8\', function(err, data)' + '\n')
##file.write('{' + '\n')
##file.write(' let old_label = label;'+'\n')
##file.write(' let new_line = new_label.concat(\',\' , searchString);' + '\n')
##file.write(' let old_line = old_label.concat(\',\' , searchString);' + '\n')

'''file.write(' var formatted = data.replace( old_line, new_line);' + '\n')

file.write(' fs.writeFile(\''+filen+'\', formatted, \'utf8\', function(err)' + '\n')
file.write('    {' + '\n')
file.write('    if (err)' + '\n')
file.write('    return console.log(err);' + '\n')
file.write('    });' + '\n')
file.write('});' + '\n')'''
file.write('}' + '\n')
#file.write(' </script>' + '\n')
## capture edit label event


file.write('function filterSelection(c) {' + '\n')
file.write('  var x, i;' + '\n')
file.write('  x = document.getElementsByClassName("column");' + '\n')
file.write('  if (c == "all") c = "";' + '\n')
file.write(
    '// Add the "show" class (display:block) to the filtered elements, and remove the "show" class from the elements that are not selected' + '\n')
file.write(' for (i = 0; i < x.length; i++) {' + '\n')
file.write('   w3RemoveClass(x[i], "show");' + '\n')
file.write('   if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");' + '\n')
file.write(' }' + '\n')
file.write('}' + '\n')

file.write('// Show filtered elements' + '\n')
file.write('function w3AddClass(element, name) {' + '\n')
file.write(' var i, arr1, arr2;' + '\n')
file.write(' arr1 = element.className.split(" ");' + '\n')
file.write(' arr2 = name.split(" ");' + '\n')
file.write('  for (i = 0; i < arr2.length; i++) {' + '\n')
file.write('   if (arr1.indexOf(arr2[i]) == -1) {' + '\n')
file.write('     element.className += " " + arr2[i];' + '\n')
file.write('  }' + '\n')
file.write(' }' + '\n')
file.write('}' + '\n')

file.write('// Hide elements that are not selected' + '\n')
file.write('function w3RemoveClass(element, name) {' + '\n')
file.write(' var i, arr1, arr2;' + '\n')
file.write('  arr1 = element.className.split(" ");' + '\n')
file.write(' arr2 = name.split(" ");' + '\n')
file.write(' for (i = 0; i < arr2.length; i++) {' + '\n')
file.write('   while (arr1.indexOf(arr2[i]) > -1) {' + '\n')
file.write('     arr1.splice(arr1.indexOf(arr2[i]), 1);' + '\n')
file.write('   }' + '\n')
file.write(' }' + '\n')
file.write(' element.className = arr1.join(" ");' + '\n')
file.write('}' + '\n')

file.write('// Add active class to the current button (highlight it)' + '\n')
file.write('var btnContainer = document.getElementById("myBtnContainer");' + '\n')
file.write('var btns = btnContainer.getElementsByClassName("btn");' + '\n')
file.write('for (var i = 0; i < btns.length; i++) {' + '\n')
file.write(' btns[i].addEventListener("click", function(){' + '\n')
file.write('   var current = document.getElementsByClassName("active");' + '\n')
file.write('   current[0].className = current[0].className.replace(" active", "");' + '\n')
file.write('   this.className += " active";' + '\n')
file.write('  });' + '\n')
file.write('}' + '\n')
file.write('</script>' + '\n')
file.write('</div>' + '\n')
file.write('</body>' + '\n')
file.write('</html>' + '\n')


