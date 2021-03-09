from tkinter import *
import numpy as np
import cv2
from tkinter import filedialog
from tkinter import messagebox
import matplotlib.pyplot as plt
from PIL import Image,ImageTk
import time
file=None
file_save=None
file_crr=None
class Tar_Img:
		
	def display(self):
		global file
		global file_crr
		file=filedialog.askopenfilename(initialdir="/",title='select file to open',filetypes=(('all files','.*'),('text files','*.txt')))
		self.imgtk=ImageTk.PhotoImage(Image.open(file))
		file_crr=canvas.create_image(20,20,anchor=NW,image=self.imgtk)

	def resize(self):
		global file
		global file_save
		global file_crr
		canvas.delete(file_crr)
		self.temp=cv2.imread(file)
		self.re_size =cv2.resize(self.temp,(200,300),interpolation=cv2.INTER_LINEAR)
		self.imgtk_re=ImageTk.PhotoImage(Image.fromarray(self.re_size))
		file_crr=canvas.create_image(20,20,anchor=NW,image=self.imgtk_re)
		file_save=self.re_size

	def cnv_to_gray(self):
		global file
		global file_crr
		global file_save
		canvas.delete(file_crr)
		self.temp=cv2.imread(file)
		self.img_gray=cv2.cvtColor(self.temp, cv2.COLOR_RGB2GRAY)
		self.imgtk_gray=ImageTk.PhotoImage(Image.fromarray(self.img_gray))
		file_crr=canvas.create_image(20,20,anchor=NW,image=self.imgtk_gray)
		file_save=self.img_gray

	def cnv_to_hsv(self):
		global file
		global file_save
		global file_crr
		canvas.delete(file_crr)
		self.temp=cv2.imread(file)
		self.img_hsv=cv2.cvtColor(self.temp,cv2.COLOR_BGR2HSV)
		self.imgtk_hsv=ImageTk.PhotoImage(Image.fromarray(self.img_hsv))
		file_crr=canvas.create_image(20,20,anchor=NW,image=self.imgtk_hsv)
		file_save=self.img_hsv
		
	def img_translation(self,x,y):
		global file
		global file_save
		global file_crr
		canvas.delete(file_crr)
		self.temp=cv2.imread(file)
		self.rows,self.cols=self.temp.shape[:2]
		self.M = np.float32([[1,0,-x],[0,1,-y]]) 
		self.dst = cv2.warpAffine(self.temp,self.M,(self.cols,self.rows)) 
		self.imgtk_trans=ImageTk.PhotoImage(Image.fromarray(self.dst))
		file_crr=canvas.create_image(20,20,anchor=NW,image=self.imgtk_trans)
		file_save=self.dst

	def threshold(self):
		global file
		global file_save
		self.temp=cv2.imread(file)
		self.img_gray=cv2.cvtColor(self.temp,cv2.COLOR_BGR2GRAY)
		ret,thresh1=cv2.threshold(self.temp,127,255,cv2.THRESH_BINARY)
		ret,thresh2=cv2.threshold(self.temp,127,255,cv2.THRESH_BINARY_INV)
		ret,thresh3=cv2.threshold(self.temp,127,255,cv2.THRESH_TRUNC)
		ret,thresh4=cv2.threshold(self.temp,127,255,cv2.THRESH_TOZERO)
		ret,thresh5=cv2.threshold(self.temp,127,255,cv2.THRESH_TOZERO_INV)
		titles=['ORIGINAL IMAGE','Bianry Image','BINARY_INV IMAGE','TRUNC','TOZERO','TOZERO_INV']
		self.images=self.img_gray,thresh1,thresh2,thresh3,thresh4,thresh5
		for i in range(6):
    			plt.subplot(2,3,i+1),plt.imshow(self.images[i],cmap='gray')
    			plt.title(titles[i])
    			plt.xticks([]),plt.yticks([])
    
		plt.show()
	def edge_detection(self):
		global file
		global file_save
		global file_crr
		canvas.delete(file_crr)
		self.temp=cv2.imread(file)
		self.edges=cv2.Canny(self.temp,100,200)
		self.imgtk_edges=ImageTk.PhotoImage(Image.fromarray(self.edges))
		file_crr=canvas.create_image(20,20,anchor=NW,image=self.imgtk_edges)
		file_save=self.edges

	def blur_img(self):
		global file
		global file_save
		global file_crr
		canvas.delete(file_crr)
		self.temp=cv2.imread(file)
		self.blur=cv2.blur(self.temp,(10,10))
		self.imgtk_blur=ImageTk.PhotoImage(Image.fromarray(self.blur))
		file_crr=canvas.create_image(20,20,anchor=NW,image=self.imgtk_blur)
		file_save=self.edges

	def save_img(self):
		global file_save
		cv2.imwrite('img.jpg',file_save)
	
	

	def detect_face(self):
		self.face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
		global file
		global file_save
		self.img=cv2.imread(file)
		self.img=cv2.resize(self.img,(700,600))
		self.face_img=self.img.copy()
		self.gray=cv2.cvtColor(self.face_img,cv2.COLOR_BGR2RGB)
		self.faces=self.face_cascade.detectMultiScale(self.gray,1.05,4)
		for (x,y,w,h) in self.faces:
    			self.image=cv2.rectangle(self.face_img,(x,y),(x+w,y+h),(0,0,255),2)
		self.face_img=ImageTk.PhotoImage(Image.fromarray(self.face_img))
		canvas.create_image(20,20,anchor=NW,image=self.face_img)
    
	


tk=Tk()
tk.title('IMAGE EDITOR')
localtime=time.asctime(time.localtime(time.time()))
frame=Frame(tk,width=1080,height=150,relief=RIDGE,bg='cyan')
frame.pack()
lblinfo=Label(frame,font=('arial',20,'bold'),text='PHOTO EDITOR',fg='Steel Blue',bd=10,anchor='w')
lblinfo.pack()
lblinfo1=Label(frame,font=('arial',10,'bold'),text=localtime,fg='Steel Blue',bd=10,anchor='w')
lblinfo1.pack()
canvas=Canvas(tk,width=1080,height=500,bg='salmon2',relief=SUNKEN)
canvas.pack()
frame=Frame(tk,width=1080,height=70,bg='powder blue',relief=SUNKEN)
frame.pack()
#file=filedialog.askopenfilename(initialdir="/",title='select file to open',filetypes=(('text files','*.txt'),('all files','.*')))
	
butterfly=Tar_Img()

btn=Button(frame,text='Display',font=('arial',8,'bold'),padx=10,pady=10,bg='green',fg='white',justify='right',bd=5,command= butterfly.display)
btn.grid(row=0,column=0)
btn1=Button(frame,text='GRAY',font=('arial',8,'bold'),padx=10,pady=10,bg='green',fg='white',justify='right',bd=5,command=butterfly.cnv_to_gray)
btn1.grid(row=0,column=1)
btn2=Button(frame,text='HSV',font=('arial',8,'bold'),padx=10,pady=10,bg='green',fg='white',justify='right',bd=5,command=butterfly.cnv_to_hsv)
btn2.grid(row=0,column=2)
btn3=Button(frame,text='Translation',font=('arial',8,'bold'),padx=10,pady=10,bg='green',fg='white',justify='right',bd=5,command=lambda: butterfly.img_translation(-100,-100))
btn3.grid(row=0,column=3)
btn4=Button(frame,text='Threshold',font=('arial',8,'bold'),padx=10,pady=10,bg='green',fg='white',justify='right',bd=5,command=butterfly.threshold)
btn4.grid(row=0,column=4)
btn5=Button(frame,text='EdgeDetection',font=('arial',8,'bold'),padx=10,pady=10,bg='green',fg='white',justify='right',bd=5,command=butterfly.edge_detection)
btn5.grid(row=0,column=5)
btn6=Button(frame,text='Resize',font=('arial',8,'bold'),padx=10,pady=10,bg='green',fg='white',justify='right',bd=5,command=butterfly.resize)
btn6.grid(row=0,column=6)
btn7=Button(frame,text='Detect Face',font=('arial',8,'bold'),padx=10,pady=10,bg='green',fg='white',justify='right',bd=5,command=butterfly.detect_face)
btn7.grid(row=0,column=7)
btn8=Button(frame,text='save',font=('arial',8,'bold'),padx=10,pady=10,bg='green',fg='white',justify='right',bd=5,command=butterfly.save_img)
btn8.grid(row=0,column=8)
btn9=Button(frame,text='Blur',font=('arial',8,'bold'),padx=10,pady=10,bg='green',fg='white',justify='right',bd=5,command=butterfly.blur_img)
btn9.grid(row=0,column=9)


tk.update()
tk.mainloop()