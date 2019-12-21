from numpy import cos, sin, radians
from matplotlib.pylab import subplots, show

x, y = 300, 550
max_depth = 9
fig, axes = subplots(figsize=(12,12))
axes.margins(0.1)
axes.set_axis_off()
# axes.set_title("La SeMA les desea una ¡feliz Navidad fractal!", fontsize=23)

def draw_fractal_tree(x1, y1, angle, depth):
    if depth:
        x2 = x1 + int(cos(radians(angle)) * 12*depth)
        y2 = y1 + int(sin(radians(angle)) * 10*(y-1.7*abs(x2-x)) )
        color_depth = 1-depth/max_depth
        axes.plot( (x1, x2), (y1, y2), lw=2*depth,
                   color=(0.13*color_depth, 0.75*color_depth, 0.13*color_depth ))
        y_factor = 1-abs(x2-x)
        draw_fractal_tree(x2, y2, angle-15, depth-1)
        draw_fractal_tree(x2, y2, angle+15, depth-1)

def draw_star(x, y):
    axes.plot( x, y, marker='*', color='gold', markersize=60 )


draw_fractal_tree(x, y, angle=90, depth=max_depth)

x_star, y_star = x+50, y+5650*max_depth

text_box = axes.text(x_star-175, y_star-1850, 'SeMA', fontsize=48,
                     style='italic', color='gold')
draw_star(x_star, y_star)

show()
