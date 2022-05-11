from tkinter import *
from PIL import Image, ImageTk
import os

DATASETDIR = '/home/azureuser/PycharmProjects/WP3/'

class MainFrame(Frame):
    def __init__(self, parent, *args, **kw):
      Frame.__init__(self, parent, *args, **kw)

      # create a canvas object and a vertical scrollbar for scrolling it
      vscrollbar = Scrollbar(self, orient=VERTICAL)
      vscrollbar.pack(fill=Y, side=RIGHT, expand=False)

      vscrollbar1 = Scrollbar(self, orient=HORIZONTAL)
      vscrollbar1.pack(fill=X, side=BOTTOM, expand=False)

      canvas = Canvas(self, bd=0, highlightthickness=0,
                      yscrollcommand=vscrollbar.set, xscrollcommand=vscrollbar1.set)
      canvas.pack(side=LEFT, fill=BOTH, expand=True)
      vscrollbar.config(command=canvas.yview)
      vscrollbar1.config(command=canvas.xview)

      # reset the view
      canvas.yview_moveto(0)
      canvas.xview_moveto(0)

      # create a frame inside the canvas which will be scrolled with it
      self.interior = interior = Frame(canvas)
      interior_id = canvas.create_window(0, 0, window=interior,
                                         anchor=NW)

      # track changes to the canvas and frame width and sync them,
      # also updating the scrollbar
      def _configure_interior(event):
          # update the scrollbars to match the size of the inner frame
          size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
          canvas.config(scrollregion="0 0 %s %s" % size)
          if interior.winfo_reqwidth() != canvas.winfo_width():
              # update the canvas's width to fit the inner frame
              canvas.config(width=interior.winfo_reqwidth())
      interior.bind('<Configure>', _configure_interior)

      def _configure_canvas(event):
          if interior.winfo_reqwidth() != canvas.winfo_width():
              # update the inner frame's width to fill the canvas
              canvas.itemconfigure(interior_id, width=canvas.winfo_width())
      canvas.bind('<Configure>', _configure_canvas)


def show_images(top10, query): # root=None):
 root = Tk()
 root.title("Similar Images")
 root.imageframe = MainFrame(root)
 root.imageframe.pack(fill=BOTH, expand=True)



 root.title("Image Search Engine")

 '''buttonImg = Button(root, text='Search', command=search, width=10, height=1, bg='#2B70F1', fg='black')
 buttonImg.pack(side=BOTTOM, pady=30)
 buttonImg.config(font=("Courier", 13))

 buttonChos = Button(root, text='Choose Image', command=imgChose, width=13, height=1, bg='#2B70F1', fg='black')
 buttonChos.pack(side=BOTTOM, pady=0)
 buttonChos.config(font=("Courier", 13))
'''

 path = '/home/azureuser/PycharmProjects/WP3/'
 images = []
 imagetks = []
 imagepanels = []
 r=0

 size = 100, 100
 c = 0
 for image in top10:
  #imagename = os.path.splitext(image[0])[0]
  imagename = path + image  # os.path.splitext(image[0])[0]
  imagename = imagename[:-4] + '.jpeg'
  img = Image.open( imagename)
  img.thumbnail(size)
  images.append(img)
  imgtk = ImageTk.PhotoImage(images[-1])
  imagetks.append(imgtk)
  panel = Label(root.imageframe.interior, image=imagetks[-1])
  imagepanels.append(panel)

  if r % 20 == 0:
      c += 1
      r = 0
  imagepanels[-1].grid(row=r, column=c)

  r = r+1

 root.mainloop()
#if __name__ = '__main__':
#    show_images(top10, root=None)