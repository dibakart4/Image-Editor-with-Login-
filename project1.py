#********************************************************IMPORT THE LIBRARIES***********************************************************************************************
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
#import random
#import time
#import datetime
#import numpy as np
#import cv2
#import matplotlib.pyplot as plt
#from PIL import Image,ImageTk
import os

#***************************************************************DEFINE THE CLASS***********************************************************************************

class Window1:
	def __init__(self,master):
		self.master=master
		self.master.title("PHOTO EDITING")
		self.master.geometry('1350x750+0+0')
		self.master.config(bg='dark khaki')
		self.frame=Frame(self.master,bg='dark khaki')
		self.frame.pack()

		self.username=StringVar()
		self.password=StringVar()

		self.lbltitle=Label(self.frame,text="LOGIN HERE!",font=('arial',50,'bold'),fg='black',bg='dark khaki')
		self.lbltitle.grid(row=0,column=0,columnspan=2,pady=40)
	
		self.lgnframe1=LabelFrame(self.frame,width=1350,height=600,font=('arial',20,'bold'),bd=20,bg='olive drab',relief='ridge')
		self.lgnframe1.grid(row=1,column=0)

		self.lgnframe2=LabelFrame(self.frame,width=1000,height=600,font=('arial',20,'bold'),bd=20,bg='olive drab',relief='ridge')
		self.lgnframe2.grid(row=2,column=0)

		self.lblusername=Label(self.lgnframe1,text='UserName',font=('arial',20,'bold'),bd=22,bg='olive drab')
		self.lblusername.grid(row=0,column=0)
		
		self.txtusername=Entry(self.lgnframe1,font=('arial',20,'bold'),textvariable=self.username)
		self.txtusername.grid(row=0,column=1)

		self.lblpassword=Label(self.lgnframe1,text='Password',font=('arial',20,'bold'),bd=22,bg='olive drab')
		self.lblpassword.grid(row=1,column=0)
		
		self.txtpassword=Entry(self.lgnframe1,font=('arial',20,'bold'),textvariable=self.password,show="*")
		self.txtpassword.grid(row=1,column=1)
		
		self.lgnbtn=Button(self.lgnframe2,text='LOGIN',width=20,font=('arial',15,'bold'),command=self.login_system)
		self.lgnbtn.grid(row=4,column=0,pady=20,padx=8)
		
		self.resetbtn=Button(self.lgnframe2,text='RESET',width=20,font=('arial',15,'bold'),command=self.reset)
		self.resetbtn.grid(row=4,column=2,pady=20,padx=8)

		self.exitbtn=Button(self.lgnframe2,text='EXIT',width=20,font=('arial',15,'bold'),command=self.exit)
		self.exitbtn.grid(row=4,column=4,pady=20,padx=8)

#****************************************************DEFINE THE FUNCTIONS************************************************************************************************
		
	def login_system(self):
		u=(self.username.get())
		p=(self.password.get())
		if(u=='dibakar_trailblazer' and (p==str(122412121))):
			os.system('python project.py')
		else:
			tkinter.messagebox.askyesno("Login System","Invalid Login Details")
			self.username.set("")
			self.password.set("")
		
	def reset(self):
		self.username.set("")
		self.password.set("")

	def exit(self):
		self.exit=tkinter.messagebox.askyesno("Login System","Confirm if you want to exit")
		if self.exit>0:
			self.master.destroy()

#*********************************************************************************************************************************

	
if __name__=='__main__':
	root=Tk()
	app=Window1(root)
	root.mainloop()
