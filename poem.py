import poems
import guibuilder

if __name__ == "__main__":
    gui = guibuilder.Gui(poems.poems_dict)
    gui.mainloop()
