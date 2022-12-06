import tkinter as tk
import maze_maker as mm
 
def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global key, cx, cy ,mx, my
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    cx, cy = mx*100+50, my*100+50
    canvas.coords("kokaton", cx, cy)
    root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("まよえるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=800, bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canvas, maze_lst)

    image1 = tk.PhotoImage(file="fig/7.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=image1, tag="kokaton")
    canvas.pack()



    key = ""
    root.bind("<KeyPress>", key_down)  
    root.bind("<KeyRelease>", key_up) 
    main_proc()
    root.mainloop()

