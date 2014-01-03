import Tkinter
import tkFileDialog

class Gui(Tkinter.Frame):
    def __init__(self,poems):
        self.poems  = poems        
        root        = Tkinter.Tk()
        self.parent = root
        RWidth      = root.winfo_screenwidth()/2.7
        RHeight     = root.winfo_screenheight()/1.7
        root.geometry(("%dx%d")%(RWidth,RHeight))
        Tkinter.Frame.__init__(self,root)
        self._initUI()

    def _initUI(self):
        self.parent.title("poems")
        self.pack(fill=Tkinter.BOTH, expand=1)
        titles=self.poems.keys()      
        self.selected = Tkinter.StringVar(self)
        self.selected.set('Please select an option')        
        w = apply(Tkinter.OptionMenu, (self, self.selected) + tuple(titles))
        self.selected.trace("w",self.display)
        w.pack()
        # text=Tkinter.Text(self)
        self.display_text=Tkinter.StringVar()
        # self.display_text.set(self.anthology['Please select an option'])
        self.display_text.set("Bonjour")
        Tkinter.Label(self,textvariable=self.display_text).pack()
        self.button = Tkinter.Button(self, text="Save", command=self.save,state=Tkinter.DISABLED)
        self.button.pack()
        
    
    def display(self,*args):        
        choice= self.selected.get()
        self.display_text.set(self.poems[choice.lower()])
        state = ["normal","disabled"][choice=='Please select an option']
        self.button.configure(state=state)
        
    
    def save(self):
        filename = tkFileDialog.asksaveasfilename(initialfile=self.selected.get()+'.txt')
        if filename:
            f=open(filename, 'w')
            f.write(self.display_text.get())
            f.close()
