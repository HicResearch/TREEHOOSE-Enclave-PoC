import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from PIL import Image, ImageTk
import os

class App():
    #def __init__(self, root, *args, **kw):
        #Frame.__init__(self, parent, *args, **kw)
    def __init__(self, root): #self, root):
        #setting title

        #setting window size
        width=600
        height=500
        root.resizable(True, True)

        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        #root.resizable(width=False, height=False)

        GButton_145=tk.Button(root)
        GButton_145["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_145["font"] = ft
        GButton_145["fg"] = "#000000"
        GButton_145["justify"] = "center"
        GButton_145["text"] = "Browse"
        GButton_145.place(x=30,y=80,width=70,height=25)
        GButton_145["command"] = self.GButton_145_command

        GButton_621=tk.Button(root)
        GButton_621["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_621["font"] = ft
        GButton_621["fg"] = "#000000"
        GButton_621["justify"] = "center"
        GButton_621["text"] = "Search"
        GButton_621.place(x=120,y=80,width=70,height=25)
        GButton_621["command"] = self.GButton_621_command

        GButton_936=tk.Button(root)
        GButton_936["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_936["font"] = ft
        GButton_936["fg"] = "#000000"
        GButton_936["justify"] = "center"
        GButton_936["text"] = "Delete"
        GButton_936.place(x=220,y=80,width=70,height=25)
        GButton_936["command"] = self.GButton_936_command

        GButton_417=tk.Button(root)
        GButton_417["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_417["font"] = ft
        GButton_417["fg"] = "#000000"
        GButton_417["justify"] = "center"
        GButton_417["text"] = "Export"
        GButton_417.place(x=440,y=470,width=70,height=25)
        GButton_417["command"] = self.GButton_417_command

        GButton_642=tk.Button(root)
        GButton_642["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_642["font"] = ft
        GButton_642["fg"] = "#000000"
        GButton_642["justify"] = "center"
        GButton_642["text"] = "Quit"
        GButton_642.place(x=520,y=470,width=70,height=25)
        GButton_642["command"] = self.GButton_642_command

        GLineEdit_112=tk.Entry(root)
        GLineEdit_112["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_112["font"] = ft
        GLineEdit_112["fg"] = "#333333"
        GLineEdit_112["justify"] = "center"
        GLineEdit_112["text"] = "Text query"
        GLineEdit_112.place(x=30,y=20,width=338,height=30)

        GButton_363=tk.Button(root)
        GButton_363["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_363["font"] = ft
        GButton_363["fg"] = "#000000"
        GButton_363["justify"] = "center"
        GButton_363["text"] = "re-label"
        GButton_363.place(x=330,y=80,width=70,height=25)
        GButton_363["command"] = self.GButton_363_command

        #self.GLabel_378=tk.Label(root) #root.grid()
        '''ft = tkFont.Font(family='Times',size=10)
        self.GLabel_378["font"] = ft
        self.GLabel_378["fg"] = "#333333"
        self.GLabel_378["justify"] = "center"
        self.GLabel_378["text"] = "Images"

        self.GLabel_378.place(x=10,y=120,width=573,height=330)'''

        ####
        #self.GLabel_378 = root.grid()
        #root.grid_rowconfigure(0, weight=1)
        #root.grid_columnconfigure(0, weight=1)
        ## Canvas
        '''root.grid_rowconfigure(10, weight=1)
        root.grid_columnconfigure(120, weight=1)'''
        #self.cnv = Canvas(root)
        self.cnv = Frame(root,width=10, height=10) #, background="white")
        #self.cnv.place(x=0, y=0, anchor="se", width=375, height=115)



        #self.cnv.grid(row=0, column=0, sticky='nswe')
        #self.cnv.place(relx=.5, rely=.5, width=57, height=30,anchor=SE)
        self.cnv.pack(side='left') #side=TOP,fill=X) #(fill=None, expand=False)

        '''hScroll = Scrollbar(self.cnv, orient=HORIZONTAL) #, command=self.cnv.xview)
        hScroll.grid(row=1, column=0, sticky='we')
        vScroll = Scrollbar(self.cnv, orient=VERTICAL) #, command=self.cnv.yview)
        vScroll.grid(row=0, column=1, sticky='ns')'''
        vscrollbar = Scrollbar(self.cnv, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=False) #(row=1, column=0, sticky='we') #pack(fill=Y, side=RIGHT, expand=False)

        vscrollbar1 = Scrollbar(self.cnv, orient=HORIZONTAL)
        vscrollbar1.pack(fill=X, side=BOTTOM, expand=False) #grid(row=1, column=0, sticky='we') #pack(fill=X, side=BOTTOM, expand=False)

        self.canvas = Canvas(self.cnv, width=150, height=150, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set, xscrollcommand=vscrollbar1.set)
        #self.canvas.grid(row=1, column=0, sticky='we') #pack(side=LEFT, fill=BOTH, expand=True)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        vscrollbar.config(command=self.canvas.yview)
        vscrollbar1.config(command=self.canvas.xview)

        self.cnv.grid_rowconfigure(0, minsize=200, weight=0)
        self.cnv.grid_columnconfigure(0, minsize=200, weight=0)
        #self.cnv.grid_columnconfigure(1, weight=0)
        #self.cnv.grid(row=0, column=0, sticky='nswe')
        ## Scrollbars for canvas
        '''hScroll = Scrollbar(root, orient=HORIZONTAL, command=self.cnv.xview)
        hScroll.grid(row=1, column=0, sticky='we')
        vScroll = Scrollbar(root, orient=VERTICAL, command=self.cnv.yview)
        vScroll.grid(row=0, column=1, sticky='ns')
        self.cnv.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set)'''
        ## Frame in canvas

        '''self.frm = Frame(self.cnv)
        ## This puts the frame in the canvas's scrollable zone
        #self.cnv.create_window(x=10,y=120, window=self.frm, anchor='nw')
        self.cnv.create_window(10, 120, window=self.frm, anchor='nw')'''
        ## Frame contents

        ###

        self.GLabel_445=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_445["font"] = ft
        self.GLabel_445["fg"] = "#333333"
        self.GLabel_445["justify"] = "center"
        self.GLabel_445["text"] = "Query"
        self.GLabel_445.place(x=450,y=0,width=125,height=125)

    def GButton_145_command(self):
        print("command")


    def GButton_621_command(self):
        print("command")


    def GButton_936_command(self):
        print("command")


    def GButton_417_command(self):
        print("command")


    def GButton_642_command(self):
        print("command")


    def GButton_363_command(self):
        print("command")

    def QueryCallback(self,img):
        self.GLabel_445.configure(image = img)
        self.GLabel_445.image = img






    def ImagesCallback(self, root,img, r, c, imagepanels, tag):
        #self.GLabel_378.configure(image=img)
        #img[-1].GLabel_378(row=r, column=c)
        #self.cnv = Canvas(root)
        ###root.grid_rowconfigure(10, weight=1)
        ###root.grid_columnconfigure(120, weight=1)
        #self.cnv = img[-1]
        #img[-1].grid(row=r, column=c)
        #img[-1].pack()

        #self.cnv.grid(row=r, column=c)
        ###self.canvas.grid(row=r, column=c) #, sticky='nswe')

        '''hScroll = Scrollbar(self.cnv, orient=HORIZONTAL, command=self.cnv.xview)
        hScroll.grid(row=1, column=0, sticky='we')
        vScroll = Scrollbar(self.cnv, orient=VERTICAL, command=self.cnv.yview)
        vScroll.grid(row=0, column=1, sticky='ns')'''
        ##self.cnv.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set)
        ## Frame in canvas

        ###self.frm = Frame(self.cnv) #, bg="green")
        ## This puts the frame in the canvas's scrollable zone
        #self.cnv.create_window(x=10,y=120, window=self.frm, anchor='nw')

        ##self.cnv.create_window(50, 100, window=self.frm) #, anchor='nw')



        #myvar = Label(self.cnv, image=img).grid(row=r, column=c)
        myvar = Label(self.cnv, image=img)
        tagLabel = Label(self.cnv, text=tag)

        '''label = tk.Label(root, width=700, bg="white", text="test", borderwidth=0, font=("Calibri", height))
        label.place(x=10, y=10)'''
        myvar.bind("<Button-1>", clickFunction)

        myvar.pack(side=RIGHT)
        tagLabel.pack(side = RIGHT)


        #myvar.image = img
        #myvar.pack()
        #imagepanels.append(myvar)
        #imagepanels[-1].grid(row=r, column=c)



    def UpdateCanvasCallback(self,):
        self.cnv.update_idletasks()
        ## Configure size of canvas's scrollable zone
        #self.cnv.configure(scrollregion=(10, 120, self.frm.winfo_width(), self.frm.winfo_height()))
        #self.GLabel_378.image = img

def clickFunction(event):  # event is argument with info about event that triggered the function
    global selectedNumber  # make the number visible throughout the program, don't need this if you'll just pass it as argument to function
    event.widget.config(background="red")  # event.widget is reference to widget that was clicked on and triggered the function
    selectedNumber = 7 - event.widget.grid_info()[ "column"]  # grid info is dictionary with info about widget's grid relative to widget, more at http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/grid-methods.html
    if (selectedNumber > 5):
        selectedNumber = 5
        print(selectedNumber)
        ''' if someday you won't use grid, but will use list to store Labels, this is a way to get Label's position
        selectedNumber = myLabels.index(event.widget)
        '''


'''if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()'''

def show_images(top10, query): # root=None):
 root = Tk() #Tk()
 #root.title("Similar Images")
 root.title("MRI Sequence Identifier")

 root.imageframe = App(root)

 #root.imageframe.pack(fill=BOTH, expand=True)




 root.title("Image Search Engine")

 '''buttonImg = Button(root, text='Search', command=search, width=10, height=1, bg='#2B70F1', fg='black')
 buttonImg.pack(side=BOTTOM, pady=30)
 buttonImg.config(font=("Courier", 13))

 buttonChos = Button(root, text='Choose Image', command=imgChose, width=13, height=1, bg='#2B70F1', fg='black')
 buttonChos.pack(side=BOTTOM, pady=0)
 buttonChos.config(font=("Courier", 13))
'''



 images = []
 imagetks = []
 imagepanels = []
 r=0

 size = 80, 80
 c = 0

 # first show the query image
 imgQuery = query #Image.open(query)
 #imgQuery.thumbnail(size)
 #imagenameq = os.path.splitext(imgQuery[0])[0]
 imgq = Image.open(imgQuery)
 imgq.thumbnail(size)
 imgtkq = ImageTk.PhotoImage(imgq)


 #root.imageframe.GLabel_445.configure(imgtkq)

 root.bind("<Return>", root.imageframe.QueryCallback(imgtkq))


 #panelQuery = Label(root.GLabel_445.interior, image=imgtkq)

 #root = tk.Tk()




 for image in top10:
  imagename = os.path.splitext(image[0])[0]
  img = Image.open(image)
  img.thumbnail(size)


  #glb_img = ImageTk.PhotoImage(img)
  #tk.Checkbutton(root, text="Koala", image=glb_img, compound='top').pack()

  #root.mainloop()
  images.append(img)
  imgtk = ImageTk.PhotoImage(images[-1])
  # added TICK BOX

  imagetks.append(imgtk)

  #root.bind("<Return>", ImagesCallback(imgtk))

  #panel = Label(root.imageframe.interior, image=imagetks[-1])

  #panel = tk.Label(root, image=img)


  ####panel = Label(root, image=imagetks[-1])


  #label.bind("<Button-1>",lambda e,url=url:open_url(url)).bind("<Button-1>", lambda e, url=url: open_url(url))
  #Label.bind("<Button-1>", lambda x: click(label.bind())

  ##panel.bind("<Button-1>", clickFunction)

  #checkbox = tk.Checkbutton(root, text='test', image=imagetks[-1], compound='top').pack()


  ####imagepanels.append(panel)

  #imagepanels.append(checkbox)
  if r % 20 == 0:
      c += 1
      r = 0
  #imagepanels[-1].grid(row=r, column=c)

  r = r+1
######
  #im = Image.open(s)
  #tkimage = ImageTk.PhotoImage(im)


 ## Update display to get correct dimensions

  root.bind("<Return>", root.imageframe.ImagesCallback(root,imgtk, r,c, imagepanels, 'T1'))

 root.bind("<Return>", root.imageframe.UpdateCanvasCallback())
 root.mainloop()