from turtle import width
from bokeh.plotting import figure, show, output_file

listy = [10, 15, 7, 9, 13, 16]  # Y軸上顯現的點
listx = ['2021-05-10 01:00', '2021-05-10 02:00', '2021-05-10 03:00',
         '2021-05-10 04:00', '2021-05-10 05:00', '2021-05-10 06:00']
#X軸上顯現的點

p = figure(x_range=listx, width=800, height=400)
p.line(listx, listy)
p.text(x=listx, y=listy, text=listy)
output_file("line2.html")
show(p)
