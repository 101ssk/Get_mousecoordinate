# codeing=utf-8
import tkinter as tk

def click(event):
    # クリックされた場所に描画する
    canvas.create_oval(event.x-20, event.y-20, event.x+20, event.y+20, fill="red", width=0)

# ウィンドウを作る
root = tk.Tk()
root.geometry("600x400")

# Canvasを作る
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.place(x=0, y=0)

# イベントを設定する
canvas.bind("<Button-1>", click)


root.mainloop()
