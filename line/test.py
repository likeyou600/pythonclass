from bokeh.plotting import figure, output_file, show
json = {
    '台北': [('01:00', 20), ('02:00', 41), ('03:00', 21), ('04:00', 22), ('05:00', 20)],
    '台中': [('01:00', 60), ('02:00', 78), ('03:00', 62), ('04:00', 60), ('05:00', 58)],
    '台南': [('01:00', 35), ('02:00', 44), ('03:00', 44), ('04:00', 48), ('05:00', 47)],
    '高雄': [('01:00', 80), ('02:00', 75), ('03:00', 82), ('04:00', 84), ('05:00', 82)]
}
CityLineColors = {'台北': 'black', '台中': 'blue', '台南': 'green', '高雄': 'red'}
CityLine = list(CityLineColors)


loc = ['台北', '台中', '台南', '高雄']

q = figure(x_range=loc, title="PM2.5-AVERAGE")

colors = []
v1 = (20+41+21+22+20)/5
v2 = (60+78+62+60+58)/5
v3 = (35+44+44+48+47)/5
v4 = (80+75+82+84+82)/5
values = [v1, v2, v3, v4]

for i in range(0, 4):
    if((values[i]) >= 71):
        colors.append('purple')
    elif((values[i]) < 71 and (values[i]) >= 54):
        colors.append('red')
    elif((values[i]) < 54 and (values[i]) >= 36):
        colors.append('yellow')
    else:
        colors.append('green')

q.vbar(x=loc, top=values, width=0.1, color=colors)
# text指定各圖的名字 x y 指定在哪個位置出現
q.text(x=loc, y=values, text=values)
output_file("bar_PM25.html")
show(q)

listxsame = ['1h', '2h', '3h', '4h', '5h']
p = figure(x_range=listxsame, width=800, height=400, title="PM2.5")
# x軸的名稱及樣式
p.xaxis.axis_label = "Time"
p.xaxis.axis_label_text_color = "black"
# y軸的名稱及樣式
p.yaxis.axis_label = "PM2.5"
p.yaxis.axis_label_text_color = "black"

listypei = [20, 41, 21, 22, 20]
p.line(listxsame, listypei, line_color="black", legend_label="台北")
listychn = [60, 78, 62, 60, 58]
p.line(listxsame, listychn, line_color="blue", legend_label="台中")
listynan = [35, 44, 44, 48, 47]
p.line(listxsame, listynan, line_color="green", legend_label="台南")
listysho = [80, 75, 82, 84, 82]
p.line(listxsame, listysho, line_color="red", legend_label="高雄")

output_file("line_PM25.html")
show(p)
