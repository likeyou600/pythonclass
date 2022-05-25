from bokeh.plotting import figure, output_file, show
jsons = {
    '台北': [('01:00', 20), ('02:00', 41), ('03:00', 21), ('04:00', 22), ('05:00', 20)],
    '台中': [('01:00', 60), ('02:00', 78), ('03:00', 62), ('04:00', 60), ('05:00', 58)],
    '台南': [('01:00', 35), ('02:00', 44), ('03:00', 44), ('04:00', 48), ('05:00', 47)],
    '高雄': [('01:00', 80), ('02:00', 75), ('03:00', 82), ('04:00', 84), ('05:00', 82)]}
CityLineColors = {'台北': 'black', '台中': 'blue', '台南': 'green', '高雄': 'red'}

# 直方圖用
allcity_name = []
allcity_avg_pm = []
allcity_avg_pm_color = []
# 直方圖用

# 折線圖用
citycount = 0
city_pm = [list() for _ in range(4)]
# 折線圖用

for site in jsons.items():
    sitename = site[0]
    allcity_name.append(sitename)

    sumpm = 0
    for timepm in site[1]:
        time = timepm[0]
        pm = timepm[1]
        city_pm[citycount].append(pm)

        sumpm += pm
    avgpm = sumpm/5
    allcity_avg_pm.append(avgpm)

    if(avgpm >= 71):
        allcity_avg_pm_color.append('purple')
    elif(avgpm < 71 and avgpm >= 54):
        allcity_avg_pm_color.append('red')
    elif(avgpm < 54 and avgpm >= 36):
        allcity_avg_pm_color.append('yellow')
    else:
        allcity_avg_pm_color.append('green')

    citycount += 1


# 直方圖
q = figure(x_range=allcity_name, title="PM2.5-AVERAGE")

q.vbar(x=allcity_name, top=allcity_avg_pm,
       width=0.1, color=allcity_avg_pm_color)
q.text(x=allcity_name, y=allcity_avg_pm, text=allcity_avg_pm)
output_file("bar_PM25.html")
show(q)
# 直方圖


# 折線圖
listxsame = ['1h', '2h', '3h', '4h', '5h']
p = figure(x_range=listxsame, width=800, height=400, title="PM2.5")
# x軸的名稱及樣式
p.xaxis.axis_label = "Time"
p.xaxis.axis_label_text_color = "black"
# y軸的名稱及樣式
p.yaxis.axis_label = "PM2.5"
p.yaxis.axis_label_text_color = "black"

p.line(listxsame, city_pm[0], line_color=CityLineColors[allcity_name[0]],
       legend_label=allcity_name[0])
p.line(listxsame, city_pm[1], line_color=CityLineColors[allcity_name[1]],
       legend_label=allcity_name[1])
p.line(listxsame, city_pm[2], line_color=CityLineColors[allcity_name[2]],
       legend_label=allcity_name[2])
p.line(listxsame, city_pm[3], line_color=CityLineColors[allcity_name[3]],
       legend_label=allcity_name[3])

output_file("line_PM25.html")
show(p)
# 折線圖


# 最後輸出
print("============== CityPM25 ==============")
for i in range(4):
    avg_pm = str(allcity_avg_pm[i])
    ci_pm = str(city_pm[i])
    print("---"+allcity_name[i]+"("+avg_pm+"):"+ci_pm)
# 最後輸出
