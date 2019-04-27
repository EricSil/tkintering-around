#print("hello world")

import tkinter









##############  FUNCTIONS

def find_screen_width():

        t = tkinter.Tk() # new window
        t.update()
        t.state('zoomed')
        width = t.winfo_width()
        t.destroy()

        return width


def find_screen_height():
        t = tkinter.Tk() # new window
        t.update()
        t.state('zoomed')
        height = t.winfo_height()
        t.destroy()

        return height


def plan_b():
        label_field = tkinter.Label(enemies_window, text="No, Foo you, but in English")
        label_field.pack()

        
################# END FUNCTIONS



##############################        Window Positioning
# Create 2 windows
allies_window, enemies_window = tkinter.Tk(), tkinter.Tk();


# find screen size
screen_width = find_screen_width()
screen_height = find_screen_height()

# Set allied window to center-left
allies_window.geometry("+0+"+str(int(screen_height/2)))

#set enemies window to center-right
window_width = enemies_window.winfo_reqwidth()
usable_width = str(screen_width - window_width)
enemies_window.geometry("+" + str(int(usable_width))+ "+" + str(int(screen_height/2)))

#################################################################################



label_field = tkinter.Label(allies_window, text="Hello World")
label_field.pack()
entry_field = tkinter.Entry(allies_window)
entry_field.pack()
button = tkinter.Button(allies_window, text="Foo - but in latin", command=plan_b)
button.pack()








#These keep the windows open when outside of python IDLE
allies_window.mainloop()#,enemies_window.mainloop();



