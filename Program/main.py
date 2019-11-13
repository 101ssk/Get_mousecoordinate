# -*- coding: utf-8 -*-
import pyautogui
import time
from datetime import datetime 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk

TIME = 10

def get_now():
    now = datetime.now().strftime("%H:%M:%S.%f")
    return now

def get_cursor_loop(loop_second):
    """
    0.1秒ずつ、指定秒数分カーソル位置を取得

    args
    ----
    loop_second:int
    データを取得する秒数
    """
    times = []
    positions = []
    p_x = []
    p_y = []
    count = 0

    for _ in range(0, loop_second*10):
        # 時刻とカーソル位置の取得
        now = get_now()
        x, y = pyautogui.position()

        p_x.append(x)
        p_y.append(y)
        # リストに情報を追加
        times.append(now)
        positions.append([x, y])
        count += 0.1
        print(count)
        # sleep
        time.sleep(0.1)

    # print(times)
    # print(positions)
    return times, positions,p_x,p_y

def get_window_size():
    window_size = pyautogui.size()
    # print(window_size)
    return window_size

if __name__ == '__main__':
    times, positions, p_x, p_y = get_cursor_loop(TIME)
    window_size = get_window_size()

    with open('position.txt','wt') as f:
        for x in positions:
            f.write(str(x)+'\n')

    with open('time.txt','wt') as f:
        for y in times:
            f.write(str(y)+'\n')

    with open('p_x.txt','wt') as f:
        for i in p_x:
            f.write(str(i)+'\n')
    
    with open('p_y.txt','wt') as f:
        for j in p_y:
            f.write(str(j)+'\n')

    data = np.array(positions)
    df = pd.DataFrame(data, columns=['x', 'y'])
    # (0,0)座標が画面の左上なのでy軸のみ順番を反転
    sns.jointplot(data=df, x='x', y='y', xlim=(0, window_size[0]), ylim=(window_size[1], 0))

    plt.show()
