from tkinter import *
import math
class calc:
 def getandreplace(self):
    self.expression = self.e.get()
    self.newtext=self.expression.replace(self.newdiv,'/')
    self.newtext=self.newtext.replace('x','*')
 def equals(self):
  """when the equal button is pressed"""
  self.getandreplace()
  try: 
    self.value= eval(self.newtext) #evaluate the expression using the eval function
  except SyntaxError or NameErrror:
    self.e.delete(0,END)
    self.e.insert(0,'Invalid Input!')
  else:
    self.e.delete(0,END)
    self.e.insert(0,self.value)
 
 def squareroot(self):
  """squareroot method"""
  self.getandreplace()
  try: 
   self.value= eval(self.newtext) #evaluate the expression using the eval function
  except SyntaxError or NameErrror:
   self.e.delete(0,END)
   self.e.insert(0,'Invalid Input!')
  else:
   self.sqrtval=math.sqrt(self.value)
   self.e.delete(0,END)
   self.e.insert(0,self.sqrtval)
 def square(self):
  """square method"""
  self.getandreplace()
  try: 
   self.value= eval(self.newtext) #evaluate the expression using the eval function
  except SyntaxError or NameErrror:
   self.e.delete(0,END)
   self.e.insert(0,'Invalid Input!')
  else:
   self.sqval=math.pow(self.value,2)
   self.e.delete(0,END)
   self.e.insert(0,self.sqval)
 
 def clearall(self): 
  """when clear button is pressed,clears the text input area"""
  self.e.delete(0,END)
 def trig_sin(self):
    self.getandreplace()
    try:
        self.value=eval(self.newtext)
    except SyntaxError or NameError:
        self.e.delete(0,END)
        self.e.insert(0,'Invalid input!')
    else:
        self.sinval=math.sin(self.value)
        self.e.delete(0,END)
        self.e.insert(0,self.sinval)
 def trig_cos(self):
    self.getandreplace()
    try:
        self.value=eval(self.newtext)
    except SyntaxError or NameError:
        self.e.delete(0,END)
        self.e.insert(0,'Invalid input!')
    else:
        self.cosval=math.cos(self.value)
        self.e.delete(0,END)
        self.e.insert(0,self.cosval)
 def trig_tan(self):
    self.getandreplace()
    try:
        self.value=eval(self.newtext)
    except SyntaxError or NameError:
        self.e.delete(0,END)
        self.e.insert(0,'Invalid input!')
    else:
        self.tanval=math.tan(self.value)
        self.e.delete(0,END)
        self.e.insert(0,self.tanval)
        
 def trig_cot(self):
    self.getandreplace()
    try:
        self.value=eval(self.newtext)
    except SyntaxError or NameError:
        self.e.delete(0,END)
        self.e.insert(0,'Invalid input!')
    else:
        self.cotval=1/math.tan(self.value)
        self.e.delete(0,END)
        self.e.insert(0,self.cotval)
 def trig_cosec(self):
    self.getandreplace()
    try:
        self.value=eval(self.newtext)
    except SyntaxError or NameError:
        self.e.delete(0,END)
        self.e.insert(0,'Invalid input!')
    else:
        self.cosecval=1/math.sin(self.value)
        self.e.delete(0,END)
        self.e.insert(0,self.cosecval)
 
 def trig_sec(self):
    self.getandreplace()
    try:
        self.value=eval(self.newtext)
    except SyntaxError or NameError:
        self.e.delete(0,END)
        self.e.insert(0,'Invalid input!')
    else:
        self.secval=1/math.cos(self.value)
        self.e.delete(0,END)
        self.e.insert(0,self.secval)

 def trig_arcsin(self):
    self.getandreplace()
    try:
        self.value=eval(self.newtext)
    except SyntaxError or NameError:
        self.e.delete(0,END)
        self.e.insert(0,'Invalid input!')
    else:
        self.arcsin=math.asin(self.value)
        self.e.delete(0,END)
        self.e.insert(0,self.arcsin)
 def trig_arccos(self):
    self.getandreplace()
    try:
        self.value=eval(self.newtext)
    except SyntaxError or NameError:
        self.e.delete(0,END)
        self.e.insert(0,'Invalid input!')
    else:
        self.arccos=math.acos(self.value)
        self.e.delete(0,END)
        self.e.insert(0,self.arccos)
 def trig_arctan(self):
    self.getandreplace()
    try:
        self.value=eval(self.newtext)
    except SyntaxError or NameError:
        self.e.delete(0,END)
        self.e.insert(0,'Invalid input!')
    else:
        self.arctan=math.atan(self.value)
        self.e.delete(0,END)
        self.e.insert(0,self.arctan)
 def trig_arccot(self):
    self.getandreplace()
    try:
        self.value=eval(self.newtext)
    except SyntaxError or NameError:
        self.e.delete(0,END)
        self.e.insert(0,'Invalid input!')
    else:
        self.arccot=math.atan(1/self.value)
        self.e.delete(0,END)
        self.e.insert(0,self.arccot)
 def trig_arccosec(self):
    self.getandreplace()
    try:
        self.value=eval(self.newtext)
    except SyntaxError or NameError:
        self.e.delete(0,END)
        self.e.insert(0,'Invalid input!')
    else:
        self.arccosec=math.asin(1/self.value)
        self.e.delete(0,END)
        self.e.insert(0,self.arccosec)
    
 def trig_arcsec(self):
    self.getandreplace()
    try:
        self.value=eval(self.newtext)
    except SyntaxError or NameError:
        self.e.delete(0,END)
        self.e.insert(0,'Invalid input!')
    else:
        self.arcsec=math.acos(1/self.value)
        self.e.delete(0,END)
        self.e.insert(0,self.arcsec)
        
 def clear1(self):
  self.txt=self.e.get()[:-1]
  self.e.delete(0,END)
  self.e.insert(0,self.txt)

 def action(self,argi): 
  """pressed button's value is inserted into the end of the text area"""
  self.e.insert(END,argi)
 
 def __init__(self,master):
  """Constructor method"""
  master.title('Calulator') 
  master.resizable(height=None,width=None)
  
  self.e = Entry(master)
  self.e.grid(row=0,column=0,columnspan=6,pady=5)
  self.e.focus_set() #Sets focus on the input text area
  self.div='÷'
  self.newdiv=self.div
  #Generating Buttons
  Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4,column=4,columnspan=2,sticky=N+S+E+W)
  Button(master,text='AC',width=3,command=lambda:self.clearall()).grid(row=1,column=4,sticky=N+S+E+W)
  Button(master,text='C',width=3,command=lambda:self.clear1()).grid(row=1,column=5,sticky=N+S+E+W)
  Button(master,text="+",width=3,command=lambda:self.action('+')).grid(row=4,column=3,sticky=N+S+E+W)
  Button(master,text="x",width=3,command=lambda:self.action('x')).grid(row=2,column=3,sticky=N+S+E+W)
  Button(master,text="-",width=3,command=lambda:self.action('-')).grid(row=3,column=3,sticky=N+S+E+W)
  Button(master,text="÷",width=3,command=lambda:self.action(self.newdiv)).grid(row=1,column=3,sticky=N+S+E+W) 
  Button(master,text="%",width=3,command=lambda:self.action('%')).grid(row=4,column=2,sticky=N+S+E+W)
  Button(master,text="7",width=3,command=lambda:self.action('7')).grid(row=1,column=0,sticky=N+S+E+W)
  Button(master,text="8",width=3,command=lambda:self.action(8)).grid(row=1,column=1,sticky=N+S+E+W)
  Button(master,text="9",width=3,command=lambda:self.action(9)).grid(row=1,column=2,sticky=N+S+E+W)
  Button(master,text="4",width=3,command=lambda:self.action(4)).grid(row=2,column=0,sticky=N+S+E+W)
  Button(master,text="5",width=3,command=lambda:self.action(5)).grid(row=2,column=1,sticky=N+S+E+W)
  Button(master,text="6",width=3,command=lambda:self.action(6)).grid(row=2,column=2,sticky=N+S+E+W)
  Button(master,text="1",width=3,command=lambda:self.action(1)).grid(row=3,column=0,sticky=N+S+E+W)
  Button(master,text="2",width=3,command=lambda:self.action(2)).grid(row=3,column=1,sticky=N+S+E+W)
  Button(master,text="3",width=3,command=lambda:self.action(3)).grid(row=3,column=2,sticky=N+S+E+W)
  Button(master,text="0",width=3,command=lambda:self.action(0)).grid(row=4,column=0,sticky=N+S+E+W)
  Button(master,text=".",width=3,command=lambda:self.action('.')).grid(row=4,column=1,sticky=N+S+E+W)
  Button(master,text="(",width=3,command=lambda:self.action('(')).grid(row=2,column=4,sticky=N+S+E+W)
  Button(master,text=")",width=3,command=lambda:self.action(')')).grid(row=2,column=5,sticky=N+S+E+W)
  Button(master,text="√",width=3,command=lambda:[self.squareroot()]).grid(row=3,column=4,sticky=N+S+E+W)
  Button(master,text="x²",width=3,command=lambda:self.square()).grid(row=3,column=5,sticky=N+S+E+W)
  Button(master,text="sin",width=3,command=lambda:[self.trig_sin()]).grid(row=5,column=0,sticky=N+S+E+W)
  Button(master,text="cos",width=3,command=lambda:[self.trig_cos()]).grid(row=5,column=1,sticky=N+S+E+W)
  Button(master,text="tan",width=3,command=lambda:[self.trig_tan()]).grid(row=5,column=2,sticky=N+S+E+W)
  Button(master,text="cot",width=3,command=lambda:[self.trig_cot()]).grid(row=5,column=3,sticky=N+S+E+W)  
  Button(master,text="cosec",width=3,command=lambda:[self.trig_cosec()]).grid(row=5,column=4,sticky=N+S+E+W)  
  Button(master,text="sec",width=3,command=lambda:[self.trig_sec()]).grid(row=5,column=5,sticky=N+S+E+W)
  Button(master,text="arcsin",width=3,command=lambda:[self.trig_arcsin()]).grid(row=6,column=0,sticky=N+S+E+W)
  Button(master,text="arccos",width=3,command=lambda:[self.trig_arccos()]).grid(row=6,column=1,sticky=N+S+E+W)
  Button(master,text="arctan",width=3,command=lambda:[self.trig_arctan()]).grid(row=6,column=2,sticky=N+S+E+W)
  Button(master,text="arccot",width=3,command=lambda:[self.trig_arccot()]).grid(row=6,column=3,sticky=N+S+E+W)  
  Button(master,text="arccosec",width=3,command=lambda:[self.trig_arccosec()]).grid(row=6,column=4,sticky=N+S+E+W)
  Button(master,text="arcsec",width=3,command=lambda:[self.trig_arcsec()]).grid(row=6,column=5,sticky=N+S+E+W)  
#Main
root = Tk()
root.resizable(height=None,width=None)
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)
root.grid_columnconfigure(3,weight=1)
root.grid_columnconfigure(4,weight=1)
root.grid_columnconfigure(5,weight=1)

obj=calc(root) #object instantiated
root.mainloop()