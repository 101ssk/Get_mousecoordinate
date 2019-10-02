import tkinter as tk
import time 
from datetime import datetime
import sys

times = []
count = 0

def get_now():
    now = datetime.now().strftime("%H:%M:%S.%f")
    return now

# ボタン内の数字管理クラス
class Counter():
    def __init__(self):
        self.num=0
    def count_up(self):
        now = get_now()
        print(now)
        # print(self.num)
        if data[self.num] == '\n':
            # print(self.num)          
            self.num += 1
        if self.num == 50:
            sys.exit()
        else:
            # print("number")
            # print(self.num)
            button["text"] = data[self.num]
            self.num += 1
    

# ファイルをオープン
test_data = open("num1.txt", "r")
# すべての内容を読み込む
data = test_data.read()
# 内容を表示
print(data)
# ファイルをクローズ
test_data.close()

root = tk.Tk()
root.title("Answer Number")
root.geometry("400x300")
root.configure(background='black')

# カウンター用のインスタンス作成
counter = Counter()
button = tk.Button(root,text=counter.num,fg='#ff0000')
button["command"] = counter.count_up
button.pack(anchor="center",expand=1)

root.mainloop()
