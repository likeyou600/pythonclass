from bokeh.plotting import figure, output_file, show
# 增加一個表格title
p = figure(width=800, height=400, title="零用金統計")
# title 的樣式設定
p.title.text_color = "green"
p.title.text_font_size = "18pt"

# x軸的名稱及樣式
p.xaxis.axis_label = "年齡"
p.xaxis.axis_label_text_color = "violet"
# y軸的名稱及樣式
p.yaxis.axis_label = "零用金"
p.yaxis.axis_label_text_color = "violet"

listx1 = [14, 16, 18, 20, 24, 26]
listy1 = [15, 50, 80, 40, 70, 50]
# line_width 粗度 ,line_alpha顏色透明度0~1 ,line_dash 指定線的樣式 ,legend 圖示(圖例)
p.line(listx1, listy1, line_width=6, line_color="red",
       line_alpha=0.3, line_dash='dashed', legend_label="女性")

listx2 = [14, 16, 18, 20, 24, 26]
listy2 = [10, 40, 30, 50, 80, 60]
p.line(listx2, listy2, line_width=2,
       line_dash='dotted', legend_label="男性")


output_file("line3.html")
show(p)
