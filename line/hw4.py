from bokeh.plotting import figure, output_file, show
# bar 長條圖的繪製

# 設置各長條圖名稱
loc = ['春', '夏', '秋', '冬']
# 設置數據
values = [50, 30, 40, 30]
colors = ['red', 'blue', 'green', 'yellow']

p = figure(x_range=loc, title="蔬菜產量")
# vertival bar(垂直BAR),注意此y軸是用top,顏色可以指定分別顏色
p.vbar(x=loc, top=values, width=0.2, color=colors)
# text指定各圖的名字 x y 指定在哪個位置出現
p.text(x=loc, y=values, text=values)

output_file("bar.html")
show(p)
