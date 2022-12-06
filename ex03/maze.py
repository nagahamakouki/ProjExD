import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym
    if mx == 13 and my == 7: #ゴールマスについたとき
        tkm.showwarning("報告","ゴールおめでとう")

def key_up(event):
    global key
    key = ""

def main_proc():
    global key, cx, cy ,mx, my
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    if maze_lst[mx][my] == 1: #壁
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1
    cx, cy = mx*100+50, my*100+50
    canvas.coords("kokaton", cx, cy)
    root.after(100,main_proc)
    
    
if __name__ == "__main__":
    global mx, my
    root = tk.Tk()
    root.title("まよえるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canvas, maze_lst)

    image1 = tk.PhotoImage(file="fig/7.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=image1, tag="kokaton")
    #image2 = tk.PhotoImage(file="fig/3.png")
    #if mx == 13 and my == 7:
    #    canvas.create_image(1350,750,image=image2,tag="goal")
    canvas.pack()

    key = ""
    root.bind("<KeyPress>", key_down)  
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()

