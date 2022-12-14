import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.geometry("300x600")

entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(row=0, column=0, columnspan=3)

def button_click(event):
    btn = event.widget
    num = btn["text"]
    siki= entry.get()
    if num == "=":
        res = eval(siki)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)

    elif num == "AC": #ALLCLEAR
        entry.delete(0,tk.END) #ACを押すと表示内容の全削除を行う

    elif num =="A":
        txt = entry.get()[:-1] #最後の一文字を抜いた文字式の取得
        entry.delete(0,tk.END) #全部消す
        entry.insert(0,txt) #最後の一文字を抜いた文字式の挿入

    elif num == "x^2":
        res = eval(siki) #評価
        ni = res*res #二乗の計算
        entry.delete(0,tk.END) 
        entry.insert(tk.END,ni) #結果の挿入

    elif num == "%":
        if siki == int: #整数か小数かの判別
            res = int(siki)/100 #パーセント計算
        else:
            res = float(siki)/100
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)

    else:
        entry.insert(tk.END,num)
    #tkm.showinfo("", f"{num}ボタンがクリックされました")
a,b=1,0
options = ["AC","A"]
for op in options:
   button = tk.Button(root, text=f"{op}", width=4, height=1, font=("",30))
   button.grid(row=a, column=b)
   button.bind("<1>", button_click)
   b+=1
   if b%3 == 0:
    a += 1
    b = 0



r,c=2,2
for i in range(9,-1,-1):
   button = tk.Button(root, text=f"{i}", width=4, height=1, font=("",30))
   button.grid(row=r, column=c)
   button.bind("<1>", button_click)
   c -= 1
   if c%3 == 2:
    r += 1
    c = 2

operators = ["","=","+","-","/","*","x^2","%"]
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=1, font=("",30))
    button.grid(row=r, column=c)
    button.bind("<1>",button_click)
    c -= 1
    if c%3 == 2:
        r+=1
        c = 2

root.mainloop()