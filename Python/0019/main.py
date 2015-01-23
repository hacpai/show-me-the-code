from Tkinter import *

def change_relf( event ):
    global relf_index
    lst = [ "flat", "groove", "raised", "ridge", "solid", "sunken" ]
    lbl.config( relief = lst[relf_index % len( lst )] )
    relf_index += 1

def change_color( event ):
    global color_index
    lst = [ "red", "yellow", "blue" ]
    lbl.config ( fg = lst[color_index % len( lst )] )
    color_index += 1

def increase_circle( event ):
    cav.delete( "circle" )
    global r
    r += 2
    if r < 100:
        cav.create_oval( 100 - r, 100 - r,
                100 + r, 100 + r, tags = "circle" )

def decrease_circle( event ):
    cav.delete( "circle" )
    global r
    r -= 2
    if r > 2:
        cav.create_oval( 100 - r, 100 - r,
                100 + r, 100 + r, tags = "circle" )

root = Tk()

lbl = Label( root, text = " Welcome to Python" )
cav = Canvas( root, width = 200, height = 200, bg = "white" )
btnl = Button( root, text = "relief" )
btnr = Button( root, text = "color" )

r = 50
cav.create_oval( 100 - r, 100 - r,
        100 + r, 100 + r, tags = "circle" )

lbl.pack()
cav.pack()
btnl.pack( side = LEFT, anchor = CENTER, expand = YES )
btnr.pack( side = LEFT, anchor = CENTER, expand = YES )

relf_index = 0
btnl.bind( "<Button-1>", change_relf )
color_index = 0
btnr.bind( "<Button-1>", change_color )

cav.bind( "<Up>", increase_circle )
cav.bind( "<Down>", decrease_circle )
cav.focus_set()

root.mainloop()
