import tkinter as tk
 

if __name__ == "__main__":
    root = tk.Tk()
    root.title("まよえるこうかとん")
    canvas = tk.Canvas(root,width=1500,height=800,bg="black")

    image1 = tk.PhotoImage(file="fig/7.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=image1,tag="kokaton")
    canvas.pack()
    key = ""
    root.mainloop()

