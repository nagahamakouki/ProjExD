import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(row=0, column=0, columnspan=3)

def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        siki = entry.get()
        res = eval(siki)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)

    elif num == "AC":
        entry.delete(0,tk.END) #ACを押すと表示内容の全削除を行う

    elif num == "x^2":
        siki = entry.get() #文字列の取得
        res = eval(siki) #評価
        ni = res*res #二乗の計算
        entry.delete(0,tk.END)
        entry.insert(tk.END,ni)

    elif num == "%":
        siki = entry.get()
        if siki == int:
            res = int(siki)/100
        else:
            res = float(siki)/100
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)

    else:
        entry.insert(tk.END,num)
    #tkm.showinfo("", f"{num}ボタンがクリックされました")

r,c=1,2
for i in range(9,-1,-1):
   button = tk.Button(root, text=f"{i}", width=4, height=1, font=("",30))
   button.grid(row=r, column=c)
   button.bind("<1>", button_click)
   c -= 1
   if c%3 == 2:
    r += 1
    c = 2

operators = ["=","AC","+","-","/","*","x^2","%"]
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=1, font=("",30))
    button.grid(row=r, column=c)
    button.bind("<1>",button_click)
    c -= 1
    if c%3 == 2:
        r+=1
        c = 2

root.mainloop()