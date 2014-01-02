#!/usr/bin/python

#from PoemClass import Poem

#firstPoem = Poem()
#firstPoem.poem_choice()
from Tkinter import *
import pickle
import tkFileDialog
class gui(Frame):  
    def __init__(self, parent,anthology):
        Frame.__init__(self, parent)
        self.parent = parent
        self.anthology=anthology
        self.initUI()
    def display(self,*args):        
        choice= self.selected.get()
        self.display_text.set(self.anthology[choice])
        if choice=='Please select an option':
            self.button.configure(state="disabled")
        else: self.button.configure(state="normal")   
    
    def save(self):
        filename = tkFileDialog.asksaveasfilename(initialfile=self.selected.get()+'.txt')
        if filename:
            f=open(filename, 'w')
            f.write(self.display_text.get())
            f.close()
        
    def initUI(self):      
        self.parent.title("poems")
        self.pack(fill=BOTH, expand=1)
        
        titles=self.anthology.keys()      
        self.selected = StringVar(self)
        self.selected.set('Please select an option')        
        w = apply(OptionMenu, (self, self.selected) + tuple(titles))
        self.selected.trace("w",self.display)
        w.pack()
        text=Text(self)
        self.display_text=StringVar()
        self.display_text.set(self.anthology['Please select an option'])
        Label(self,textvariable=self.display_text ).pack()
        self.button = Button(self, text="Save", command=self.save,state=DISABLED)
        self.button.pack()

def main():
  
    root = Tk()
    anthology=pickle.load(open('poems.p'))
    anthology['Please select an option']='\n\n\nWELCOME!!!' #default message
    
    RWidth=root.winfo_screenwidth()/2.7
    RHeight=root.winfo_screenheight()/1.7
    root.geometry(("%dx%d")%(RWidth,RHeight))
    app = gui(root,anthology)
    root.mainloop()  


if __name__ == '__main__':
    main()  
