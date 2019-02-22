import tkinter as tk
from PIL import Image, ImageTk, ImageSequence


class App(object):
	"""docstring for App"""

	def __init__(self, parent):
		self.canvas = tk.Canvas(parent, width=700, hight=700)
		self.canvas.pack()
		self.sequence = [ImageTk.PhotoImage(img)
		for img in ImageSequence.Iterator(Image.open(r'/home/saumen/Python projects/Rotating gif/animated-woman-image-0058.gif))']:
			self.image=self.canvas.create_image(350, 350, image=self.sequence[0])
			self.animate(0)


	def animate(self, counter):
		self.canvas.itemconfig(self.image, image=self.sequence[counter])
		self.parent.after(33, lambda: self.animate(counter + 1) % len(self.sequence)))


root=tkinter.Tk()
app=App(root)
root.mainloop()
