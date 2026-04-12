import colorgram

colors = colorgram.extract('image.jpg', 10)

colors_list = []
for i in range(len(colors)):
    color_cell = {}
    color_cell['r']= colors[i].rgb[0]
    color_cell['g']= colors[i].rgb[1]
    color_cell['b']= colors[i].rgb[2]
    colors_list.append(color_cell)