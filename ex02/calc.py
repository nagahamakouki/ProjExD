import tkinter as tk
import tkinter.messagebox as tkm
root = tk.Tk()
root.geometry

def button_click(event):
    btn = event.widget
    num = btn["text"]
    tkm.showinfo("",f"{num}ボタンがクリックされました")

r,c=0,0
for i in range(10):
   button =tk.Button(root,text=f"{i}",width=4,height=2,font=("",30))
   button.grid(row =r,column = c)
   button.bind("<1>",button_click)
   c+=1
   if c%3 ==0:
    r+=1
    c=0

root.mainloop()