import tkinter as tk
 
def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""


if __name__ == "__main__":
    root = tk.Tk()
    root.title("まよえるこうかとん")
    canvas = tk.Canvas(root,width=1500,height=800,bg="black")

    image1 = tk.PhotoImage(file="fig/7.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=image1,tag="kokaton")
    canvas.pack()
    key = ""
    root.bind("<KeyPress",key_down)  
    root.bind("<KeyImpress>",key_up) 
    root.mainloop()

