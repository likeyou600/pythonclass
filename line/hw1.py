from turtle import width
from bokeh.plotting import figure, show

# 創建一個plot(統計圖)的大小，以pixel為單位
p = figure(width=800, height=400)

# 給座標 x y 配對描述點座標 (eg 1 15)
listx = [1, 5, 7, 9, 13, 16]  # X軸上顯現的點
listy = [15, 50, 80, 40, 70, 50]  # Y軸上顯現的點

# 按照座標畫直線
p.line(listx, listy)

# 會生成一個html的檔案，叫做main.html(內建的名稱)
show(p)
