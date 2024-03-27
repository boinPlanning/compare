import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib as mpl
import numpy as np
from matplotlib.path import Path
import matplotlib.lines
import random
import io
import sys
import math

# 점 + 문자
def setPoint(ax,points=list,text=[],position=[],fill=False):
    temp = []
    for p in points:
        if p not in temp:
            temp.append(p)

    points = temp

    if len(text) == 0:
        for t in range(len(points)):
            text.append('')

    for i in range(0,len(points)):

        cp = points[i]
        l = len(text[i])
        if position[i] == 'top':
            plt.text(cp[0]-2*l, cp[1]+3.5, text[i], fontsize=16, zorder=3)
        elif position[i] == 'bottom':
            plt.text(cp[0]-2*l, cp[1]-7.5, text[i], fontsize=16, zorder=3)
        elif position[i] == 'left':
            plt.text(cp[0]-3-l*4.5, cp[1]-2, text[i], fontsize=16, zorder=3)
        elif position[i] == 'right':
            plt.text(cp[0]+l, cp[1]-2, text[i], fontsize=16, zorder=3)
        elif position[i] == 'top_r':
            plt.text(cp[0]+l*0.3, cp[1]+2, text[i], fontsize=16, zorder=3)
        elif position[i] == 'top_l':
            plt.text(cp[0]+1-l*5, cp[1]+2, text[i], fontsize=16, zorder=3)
        elif position[i] == 'bottom_r':
            plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5, text[i], fontsize=16, zorder=3)
        elif position[i] == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5, text[i], fontsize=16, zorder=3)
        else: raise Exception('no matching position')
        #plt.text(points[i][0]-0.5, points[i][1]+0.1, text[i], fontsize=14, zorder=3)

        if fill:
            ax.plot(points[i][0], points[i][1],"k.", zorder=3)
    

    #for i in range(0,len(points)):
    #    ax.plot([points[i][0]], [points[i][1]],"ko", zorder=3)

# 점
def drawDot(ax,points=list,colors=False):
    if colors: format = 'r.'
    else: format = 'k.'
    for i in range(0,len(points)):
        ax.plot(points[i][0], points[i][1],format, zorder=3)

# 각
def drawAngle(ax, p_lists=[],diff=False):
    d = 50
    if diff:
        color = ['r','g','b','c','m','y']
        #width_list = [0.4*d,0.6*d,0.4*d,0.6*d]
    else:
        color = ['r','r','r','r','r','r','r','r','r','r']
    i=0
    for p_list in p_lists:
        p1 = p_list[0]
        p2 = p_list[1]
        p3 = p_list[2]

        dx1 = p1[0] - p2[0]
        dy1 = p1[1] - p2[1]

        dx2 = p3[0] - p2[0]
        dy2 = p3[1] - p2[1]

        a1 = math.degrees(math.atan2(dy1,dx1))
        a2 = math.degrees(math.atan2(dy2,dx2))

        angle = a2 -a1
        if angle < 0:
            angle = 360 + angle

        #width&height
        if angle < 30:
            width = 0.4*d
            height = 0.4*d
        else:
            width = 0.2*d
            height = 0.2*d
        

        # if angle == 90:
        #     if a1 == 0.0 and a2 ==90.0:
        #         verts = [
        #             (p2[0]+0.1*d,p2[1]),
        #             (p2[0]+0.1*d,p2[1]+0.1*d),
        #             (p2[0],p2[1]+0.1*d)
        #         ]
        #     elif a1 == 90.0 and a2 == 180.0:
        #         verts = [
        #             (p2[0]-0.1*d,p2[1]),
        #             (p2[0]-0.1*d,p2[1]+0.1*d),
        #             (p2[0],p2[1]+0.1*d)
        #         ]
        #     elif a1 == 180.0 and a2 == -90.0:
        #         verts = [
        #             (p2[0]-0.1*d,p2[1]),
        #             (p2[0]-0.1*d,p2[1]-0.1*d),
        #             (p2[0],p2[1]-0.1*d)
        #         ]
        #     elif a1 == -90.0 and a2 == 0.0:
        #         verts = [
        #             (p2[0]+0.1*d,p2[1]),
        #             (p2[0]+0.1*d,p2[1]-0.1*d),
        #             (p2[0],p2[1]-0.1*d)
        #         ]
        #     elif a1 == 45.0 and a2 == 135.0:
        #         verts = [
        #             (p2[0]-math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d)),
        #             (p2[0],p2[1]+2*math.sqrt(0.01*d)),
        #             (p2[0]+math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d))
        #         ]
        #     elif a1 >= 135.0 and a2 <= -135.0:
        #         verts = [
        #             (p2[0]-math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d)),
        #             (p2[0]-2*math.sqrt(0.01*d),p2[1]),
        #             (p2[0]-math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d))
        #         ]
        #     elif a1 == -135.0 and a2 == -45.0:
        #         verts = [
        #             (p2[0]-math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d)),
        #             (p2[0],p2[1]-2*math.sqrt(0.01*d)),
        #             (p2[0]+math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d))
        #         ]
        #     else:
        #         verts = [
        #             (p2[0]+math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d)),
        #             (p2[0]+2*math.sqrt(0.01*d),p2[1]),
        #             (p2[0]+math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d))
        #         ]
            
        #     codes = [
        #             Path.MOVETO,
        #             Path.LINETO,
        #             Path.LINETO
        #         ]
        #     path = Path(verts,codes)

        #     pp = mpatches.PathPatch(path, ec='red', fill=False, zorder=3)
        if angle < 30:
            if diff and (i%2) == 1:
                pp = mpatches.Arc(p2, angle=0, width=width*3/4, height=height*3/4, theta1=a1, theta2=a2, ec=color[i], zorder=3)
                ax.add_patch(pp)
            pp = mpatches.Arc(p2, angle=0, width=width, height=height, theta1=a1, theta2=a2, ec=color[i], zorder=3)
        elif angle > 30:
            if diff and (i%2) == 1:
                pp = mpatches.Arc(p2, angle=0, width=width*2, height=height*2, theta1=a1, theta2=a2, ec=color[i], zorder=3)
                ax.add_patch(pp)
            pp = mpatches.Arc(p2, angle=0, width=width, height=height, theta1=a1, theta2=a2, ec=color[i], zorder=3)
        else: raise Exception('wrong angle')

        ax.add_patch(pp)
        i += 1
def drawAngle_multiple(ax, multiple_p_list=[],diff=False):
    def rotate_p(p_list=list,angle=0):
        def cart2pol(x, y):
            import math
            r = math.sqrt(x**2 + y**2)
            angle_radians = math.atan2(y, x)
            return(r, angle_radians)
        def pol2cart(r, angle_radians):
            import math
            x = r * math.cos(angle_radians)
            y = r * math.sin(angle_radians)
            return(x, y)
        import math
        for i in range(len(p_list)):
            cart_x = p_list[i][0]
            cart_y = p_list[i][1]
            pol_r, pol_angle_radians = cart2pol(cart_x,cart_y)
            pol_angle_radians += math.radians(angle)
            cart_x,cart_y = pol2cart(pol_r,pol_angle_radians)
            p_list[i] = (cart_x,cart_y)
        return p_list
    if diff:
        color = ['r','g','b','c','m','y']
        #width_list = [0.4*d,0.6*d,0.4*d,0.6*d]
    else:
        color = ['r','r','r','r','r','r','r','r','r','r']
    i=0
    for p_list in multiple_p_list:
        p1 = p_list[0]
        p2 = p_list[1]
        p3 = p_list[2]
        #calculate angle
        dx1 = p1[0] - p2[0]
        dy1 = p1[1] - p2[1]
        dx2 = p3[0] - p2[0]
        dy2 = p3[1] - p2[1]
        a1 = math.degrees(math.atan2(dy1,dx1))
        a2 = math.degrees(math.atan2(dy2,dx2))
        angle = round(a2 - a1)
        if angle < 0:
            angle = 360 + angle
        #width&height
        d = 50
        if angle < 30:
            width = 0.4*d
            height = 0.4*d
        elif angle == 90:
            d *= 15
        else:
            width = 0.2*d
            height = 0.2*d
        #draw angle
        if angle == 90:
            if a1 == 0.0 and a2 ==90.0:
                verts = [
                    (p2[0]+0.1*d,p2[1]),
                    (p2[0]+0.1*d,p2[1]+0.1*d),
                    (p2[0],p2[1]+0.1*d)
                ]
            elif a1 == 90.0 and a2 == 180.0:
                verts = [
                    (p2[0]-0.1*d,p2[1]),
                    (p2[0]-0.1*d,p2[1]+0.1*d),
                    (p2[0],p2[1]+0.1*d)
                ]
            elif a1 == 180.0 and a2 == -90.0:
                verts = [
                    (p2[0]-0.1*d,p2[1]),
                    (p2[0]-0.1*d,p2[1]-0.1*d),
                    (p2[0],p2[1]-0.1*d)
                ]
            elif a1 == -90.0 and a2 == 0.0:
                verts = [
                    (p2[0]+0.1*d,p2[1]),
                    (p2[0]+0.1*d,p2[1]-0.1*d),
                    (p2[0],p2[1]-0.1*d)
                ]
            elif a1 == 45.0 and a2 == 135.0:
                verts = [
                    (p2[0]-math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d)),
                    (p2[0],p2[1]+2*math.sqrt(0.01*d)),
                    (p2[0]+math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d))
                ]
            elif a1 >= 135.0 and a2 <= -135.0:
                verts = [
                    (p2[0]-math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d)),
                    (p2[0]-2*math.sqrt(0.01*d),p2[1]),
                    (p2[0]-math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d))
                ]
            elif a1 == -135.0 and a2 == -45.0:
                verts = [
                    (p2[0]-math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d)),
                    (p2[0],p2[1]-2*math.sqrt(0.01*d)),
                    (p2[0]+math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d))
                ]
            else:
                verts = [
                    (p2[0]+math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d)),
                    (p2[0]+2*math.sqrt(0.01*d),p2[1]),
                    (p2[0]+math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d))
                ]
                rotate_p(verts,(a1+a2)/2)
            codes = [
                    Path.MOVETO,
                    Path.LINETO,
                    Path.LINETO
                ]
            path = Path(verts,codes)

            pp = mpatches.PathPatch(path, ec=color[i], fill=False, zorder=3)
        elif angle <= 30:
            if diff and (i%2) == 1:
                pp = mpatches.Arc(p2, angle=0, width=width*3/4, height=height*3/4, theta1=a1, theta2=a2, ec=color[i], zorder=3)
                ax.add_patch(pp)
            pp = mpatches.Arc(p2, angle=0, width=width, height=height, theta1=a1, theta2=a2, ec=color[i], zorder=3)
        elif angle > 30:
            if diff and (i%2) == 1:
                pp = mpatches.Arc(p2, angle=0, width=width*2, height=height*2, theta1=a1, theta2=a2, ec=color[i], zorder=3)
                ax.add_patch(pp)
            pp = mpatches.Arc(p2, angle=0, width=width, height=height, theta1=a1, theta2=a2, ec=color[i], zorder=3)
        else: raise Exception('wrong angle')

        ax.add_patch(pp)
        i += 1
def drawAngle_(ax, p_list=[]):
    def rotate_p(p_list=list,angle=0):
        def cart2pol(x, y):
            import math
            r = math.sqrt(x**2 + y**2)
            angle_radians = math.atan2(y, x)
            return(r, angle_radians)
        def pol2cart(r, angle_radians):
            import math
            x = r * math.cos(angle_radians)
            y = r * math.sin(angle_radians)
            return(x, y)
        import math
        for i in range(len(p_list)):
            cart_x = p_list[i][0]
            cart_y = p_list[i][1]
            pol_r, pol_angle_radians = cart2pol(cart_x,cart_y)
            pol_angle_radians += math.radians(angle)
            cart_x,cart_y = pol2cart(pol_r,pol_angle_radians)
            p_list[i] = (cart_x,cart_y)
        return p_list

    color = ['r','g','b','c','m','y']
    p1 = p_list[0]
    p2 = p_list[1]
    p3 = p_list[2]
    #calculate angle
    dx1 = p1[0] - p2[0]
    dy1 = p1[1] - p2[1]
    dx2 = p3[0] - p2[0]
    dy2 = p3[1] - p2[1]
    a1 = round(math.degrees(math.atan2(dy1,dx1)))
    a2 = round(math.degrees(math.atan2(dy2,dx2)))
    angle = a2 -a1
    if angle < 0:
        angle = 360 + angle

    #width&height
    d = 50
    if angle < 30:
        width = 0.4*d
        height = 0.4*d
    elif angle == 90:
        d *= 15
    else:
        width = 0.2*d
        height = 0.2*d
    
    #draw angle
    if angle == 90:
        if a1 == 0.0 and a2 ==90.0:
            verts = [
                (p2[0]+0.1*d,p2[1]),
                (p2[0]+0.1*d,p2[1]+0.1*d),
                (p2[0],p2[1]+0.1*d)
            ]
        elif a1 == 90.0 and a2 == 180.0:
            verts = [
                (p2[0]-0.1*d,p2[1]),
                (p2[0]-0.1*d,p2[1]+0.1*d),
                (p2[0],p2[1]+0.1*d)
            ]
        elif a1 == 180.0 and a2 == -90.0:
            verts = [
                (p2[0]-0.1*d,p2[1]),
                (p2[0]-0.1*d,p2[1]-0.1*d),
                (p2[0],p2[1]-0.1*d)
            ]
        elif a1 == -90.0 and a2 == 0.0:
            verts = [
                (p2[0]+0.1*d,p2[1]),
                (p2[0]+0.1*d,p2[1]-0.1*d),
                (p2[0],p2[1]-0.1*d)
            ]
        elif a1 == 45.0 and a2 == 135.0:
            verts = [
                (p2[0]-math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d)),
                (p2[0],p2[1]+2*math.sqrt(0.01*d)),
                (p2[0]+math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d))
            ]
        elif a1 >= 135.0 and a2 <= -135.0:
            verts = [
                (p2[0]-math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d)),
                (p2[0]-2*math.sqrt(0.01*d),p2[1]),
                (p2[0]-math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d))
            ]
        elif a1 == -135.0 and a2 == -45.0:
            verts = [
                (p2[0]-math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d)),
                (p2[0],p2[1]-2*math.sqrt(0.01*d)),
                (p2[0]+math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d))
            ]
        else:
            verts = [
                (p2[0]+math.sqrt(d*0.01),p2[1]+math.sqrt(d*0.01)),
                (p2[0]+2*math.sqrt(d*0.01),p2[1]),
                (p2[0]+math.sqrt(d*0.01),p2[1]-math.sqrt(d*0.01))
            ]
            rotate_p(verts,(a1+a2)/2)
        
        codes = [
                Path.MOVETO,
                Path.LINETO,
                Path.LINETO
            ]
        path = Path(verts,codes)

        pp = mpatches.PathPatch(path, ec='red', fill=False, zorder=3)
    elif angle < 30:
        pp = mpatches.Arc(p2, angle=0, width=width, height=height, theta1=a1, theta2=a2, ec='red', zorder=3)
    elif angle > 30:
        pp = mpatches.Arc(p2, angle=0, width=width, height=height, theta1=a1, theta2=a2, ec='red', zorder=3)
    else: raise Exception('wrong angle')

    ax.add_patch(pp)

# 직선
def drawLine(ax,pts,dash=False):
    if dash: linestype = '--'
    else: linestype = '-'
    line_1 = matplotlib.lines.Line2D((pts[0][0],pts[1][0]), (pts[0][1],pts[1][1]), linewidth=1, linestyle = linestype,color='black')
    ax.add_line(line_1)
def drawLine_multiple(ax,l_list=list,dash=False,color='black'):
    if dash: linestype = '--'
    else: linestype = '-'
    for i in range(len(l_list)):
        pts = l_list[i]
        vert = [
            pts[0],
            pts[1]
        ]
        codes = [
            Path.MOVETO,
            Path.LINETO
        ]

        path = Path(vert,codes)

        pp = mpatches.PathPatch(path, fc="none", transform=ax.transData, linestyle=linestype, zorder=3, color=color)
        ax.add_patch(pp)

# 다각형
def drawPolygon(ax, verts, fill=False, alpha=1, dash=False):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    vert = verts
    vert.append(verts[0])
    codes = [Path.MOVETO]

    for i in range(0,len(vert)-2):
        codes.append(Path.LINETO)

    codes.append(Path.CLOSEPOLY)

    path = Path(vert,codes)
    
    if fill:
        if dash:
            pp = mpatches.PathPatch(path, fc=random.choice(colors), fill=True, lw=1, ls='--', zorder=3, alpha=alpha)
        else:
            pp = mpatches.PathPatch(path, fc=random.choice(colors), fill=True, lw=2, zorder=3, alpha=alpha)
    else:
        if dash:
            pp = mpatches.PathPatch(path, ec='black', fill=False, lw=1, ls='--', zorder=3)
        else:
            pp = mpatches.PathPatch(path, ec='black', fill=False, lw=2, zorder=3)
    ax.add_patch(pp)

# 다각형 + 각
def drawPolygonAngle(ax, verts=list, show_angle=False, show_angle_num=False):
    def drawAngle(ax, p_lists=[],diff=False):
        d = 50
        if diff:
            color = ['r','g','b','c','m','y']
            #width_list = [0.4*d,0.6*d,0.4*d,0.6*d]
        else:
            color = ['r','r','r','r','r','r','r','r','r','r']
        i=0
        for p_list in p_lists:
            p1 = p_list[0]
            p2 = p_list[1]
            p3 = p_list[2]

            dx1 = p1[0] - p2[0]
            dy1 = p1[1] - p2[1]

            dx2 = p3[0] - p2[0]
            dy2 = p3[1] - p2[1]

            a1 = math.degrees(math.atan2(dy1,dx1))
            a2 = math.degrees(math.atan2(dy2,dx2))

            angle = a2 -a1
            if angle < 0:
                angle = 360 + angle

            #width&height
            if angle < 30:
                width = 0.4*d
                height = 0.4*d
            else:
                width = 0.2*d
                height = 0.2*d
            
            if angle < 30:
                if diff and (i%2) == 1:
                    pp = mpatches.Arc(p2, angle=0, width=width*3/4, height=height*3/4, theta1=a1, theta2=a2, ec=color[i], zorder=3)
                    ax.add_patch(pp)
                pp = mpatches.Arc(p2, angle=0, width=width, height=height, theta1=a1, theta2=a2, ec=color[i], zorder=3)
            elif angle > 30:
                if diff and (i%2) == 1:
                    pp = mpatches.Arc(p2, angle=0, width=width*2, height=height*2, theta1=a1, theta2=a2, ec=color[i], zorder=3)
                    ax.add_patch(pp)
                pp = mpatches.Arc(p2, angle=0, width=width, height=height, theta1=a1, theta2=a2, ec=color[i], zorder=3)
            else: raise Exception('wrong angle')

            ax.add_patch(pp)
            i += 1

    #draw angle
    for i in range(len(verts)):
        first_index = i % (len(verts))
        second_index = (i+1) % (len(verts))
        third_index = (i+2) % (len(verts))
        angle = [verts[first_index],verts[second_index],verts[third_index]]
        drawAngle(ax,[angle])

    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    vert = verts
    vert.append(verts[0])
    codes = [Path.MOVETO]

    for i in range(0,len(verts)-2):
        codes.append(Path.LINETO)

    codes.append(Path.CLOSEPOLY)

    path = Path(verts,codes)
    
    
    pp = mpatches.PathPatch(path, ec='black', fill=False, lw=2, zorder=3)
    ax.add_patch(pp)

# 원
def drawCircle(ax,center, radius, fill=False, alpha=1, dash=False, position=None):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    x_min = ax.get_xlim()[0]
    x_max = ax.get_xlim()[1]

    y_min = ax.get_ylim()[0]
    y_max = ax.get_ylim()[1]

    if center[0]-radius-0.5 < x_min:
        x_min = center[0]-radius-0.5
    if center[0]+radius+0.5 > x_max:
        x_max = center[0]+radius+0.5
    if center[1]-radius-0.5 < y_min:
        y_min = center[1]-radius-0.5
    if center[1]+radius+0.5 > y_max:
        y_max = center[1]+radius+0.5

    maxlim = max(x_max, y_max)
    minlim = min(x_min, y_min)

    ax.set_xlim(minlim, maxlim)
    ax.set_ylim(minlim, maxlim)

    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    if position != None and fill == False:
        if position == 'left':
            theta1 = 90
            theta2 = 270
        elif position == 'right':
            theta1 = -90
            theta2 = 90
        elif position == 'top':
            theta1 = 0
            theta2 = 180
        elif position == 'bottom':
            theta1 = 180
            theta2 = 360

        if dash:
            pp = mpatches.Arc(center, width=radius*2, height=radius*2, angle=0, theta1=theta1, theta2=theta2, ec='black', lw=1, ls='--', fill=False, zorder=3)
        else:
            pp = mpatches.Arc(center, width=radius*2, height=radius*2, angle=0, theta1=theta1, theta2=theta2, ec='black', lw=2, fill=False, zorder=3)
    else:
        if fill:
            if dash:
                pp = mpatches.Circle(center,radius=radius, fc=random.choice(colors), ec='black', lw=1, ls='--', fill=True, zorder=3, alpha=alpha)
            else:
                pp = mpatches.Circle(center,radius=radius, fc=random.choice(colors), ec='black', lw=2, fill=True, zorder=3, alpha=alpha)
        else:
            if dash:
                pp = mpatches.Circle(center,radius=radius, ec='black', lw=1, ls='--', fill=False, zorder=3)
            else:
                pp = mpatches.Circle(center,radius=radius, ec='black', lw=2, fill=False, zorder=3)
    ax.add_patch(pp)

# 타원
def drawEllipse(ax,center, width, height, fill=False, alpha=1, dash=False, position=None):
    radius = max(width, height)/2

    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    x_min = ax.get_xlim()[0]
    x_max = ax.get_xlim()[1]

    y_min = ax.get_ylim()[0]
    y_max = ax.get_ylim()[1]

    if center[0]-radius-0.5 < x_min:
        x_min = center[0]-radius-0.5
    if center[0]+radius+0.5 > x_max:
        x_max = center[0]+radius+0.5
    if center[1]-radius-0.5 < y_min:
        y_min = center[1]-radius-0.5
    if center[1]+radius+0.5 > y_max:
        y_max = center[1]+radius+0.5

    maxlim = max(x_max, y_max)
    minlim = min(x_min, y_min)

    ax.set_xlim(minlim, maxlim)
    ax.set_ylim(minlim, maxlim)

    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    if position != None and fill == False:
        if position == 'left':
            theta1 = 90
            theta2 = 270
        elif position == 'right':
            theta1 = -90
            theta2 = 90
        elif position == 'top':
            theta1 = 0
            theta2 = 180
        elif position == 'bottom':
            theta1 = 180
            theta2 = 360

        if dash:
            pp = mpatches.Arc(center, width=width, height=height, angle=0, theta1=theta1, theta2=theta2, ec='black', lw=1, ls='--', zorder=3)
        else:
            pp = mpatches.Arc(center, width=width, height=height, angle=0, theta1=theta1, theta2=theta2, ec='black', lw=2, zorder=3)
    else:
        if fill:
            if dash:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, fc=random.choice(colors), ec='black', lw=1, ls='--', fill=True, zorder=3, alpha=alpha)
            else:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, fc=random.choice(colors), ec='black', lw=2, fill=True, zorder=3, alpha=alpha)
        else:
            if dash:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, ec='black', lw=1, ls='--', fill=False, zorder=3)
            else:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, ec='black', lw=2, fill=False, zorder=3)

    ax.add_patch(pp)

# 문자
def drawText(ax,text='',x=0,y=0):
    l = len(str(text))
    if 'mathrm' in text: 
        l -= 10
    plt.text(x-l, y, text, fontsize=16, zorder=3)

def drawText_(ax,text='',xy=(0,0)):
    if len(xy) > 2: raise Exception("too many inputs for xy")
    l = len(str(text))
    if 'mathrm' in text: 
        l -= 10
    x,y = xy
    plt.text(x-l, y, text, fontsize=16, zorder=3)


# 선분의 길이를 표시하는 bezier 곡선을 그리는 함수
def drawArc(ax, p1, p2, position, text, boxed=False):
    cp = controlPoint(p1,p2,position)
    d = math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
    l = len(text)
    if 'mathrm' in text: 
        l -= 10
    vert = [
        p1,
        cp, # 제어점
        p2,
        p1
    ]
    codes = [
        Path.MOVETO,
        Path.CURVE3,
        Path.CURVE3,
        Path.CLOSEPOLY,
    ]

    path = Path(vert,codes)

    pp = mpatches.PathPatch(path, fc="none", transform=ax.transData, linestyle="--", zorder=3)
    ax.add_patch(pp)


    if boxed:
        if position == 'top':
            plt.text(cp[0]-2*l, cp[1]+3.5, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom':
            plt.text(cp[0]-2*l, cp[1]-7.5, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'left':
            plt.text(cp[0]-2-l*4.5, cp[1]-2, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'right':
            plt.text(cp[0]+l, cp[1]-2, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'top_r':
            plt.text(cp[0]+l*0.3, cp[1]+2, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'top_l':
            plt.text(cp[0]+1-l*5, cp[1]+2, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_r':
            plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
    else:
        if position == 'top':
            plt.text(cp[0]-2*l, cp[1]+1, text, fontsize=16, zorder=3)
        elif position == 'bottom':
            plt.text(cp[0]-2*l, cp[1]-7.5, text, fontsize=16, zorder=3)
        elif position == 'left':
            plt.text(cp[0]-2-l*4.5, cp[1]-2, text, fontsize=16, zorder=3)
        elif position == 'right':
            plt.text(cp[0]+l, cp[1]-2, text, fontsize=16, zorder=3)
        elif position == 'top_r':
            plt.text(cp[0]+l*0.3, cp[1]+2, text, fontsize=16, zorder=3)
        elif position == 'top_l':
            plt.text(cp[0]+1-l*5, cp[1]+2, text, fontsize=16, zorder=3)
        elif position == 'bottom_r':
            plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5, text, fontsize=16, zorder=3)
        elif position == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5, text, fontsize=16, zorder=3)
        else: raise Exception('no matching position')

# 직선 화살표 그리는 함수(dy==0)
def drawArrow(ax,start_p=tuple,end_p=tuple,colors=False):
    from math import sqrt
    h = 0.003
    x1 = start_p[0]
    y1 = start_p[1]
    x2 = end_p[0]
    y2 = end_p[1]
    dx = end_p[0]-start_p[0]
    dy = end_p[1]-start_p[1]
    #new_dx = abs(x1) + sqrt((sqrt(dx**2+dy**2)-h)/2)
    #new_dy = abs(y1) + sqrt((sqrt(dx**2+dy**2)-h)/2)
    head_width = 3*h
    head_length = 1.5*head_width
    new_dx = 0
    new_dy = 0
    if dx == 0: 
        if dy < 0: new_dy = (abs(dy) - head_length)*-1
        else: new_dy = dy - head_length
    elif dy == 0: 
        if dx < 0: new_dx = (abs(dx) - head_length)*-1
        else: new_dx = dx - head_length
    else: raise Exception("not a stright line")
    
    ax.arrow(x1, y1, new_dx, new_dy, width=h)

# 직선 양면 화살표 그리는 함수(dy==0)
def drawDoubleArrow(ax,start_p=tuple,end_p=tuple,text='',colors=False):
    def controlPoint(p1, p2, type):
        d = math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
        #d = 2
        # 지나는 점 (p1, p2의 중점)
        mp = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

        if (p2[0]-p1[0]) == 0:
            if type == 'left' or type == 'top':
                cp = (mp[0]-0.2*d,mp[1])
            else:
                cp = (mp[0]+0.2*d,mp[1])

        elif (p2[1]-p1[1]) == 0:
            if type == 'bottom' or type == 'right':
                cp = (mp[0], mp[1]-0.2*d)
            else:
                cp = (mp[0], mp[1]+0.2*d)
        else:
            # 기울기
            m = - (p2[0]-p1[0])/(p2[1]-p1[1])
            #print(m)
            if m > 0:
                if m > 1:
                    if m > 50:
                        if type == 'left' or type == 'bottom':
                            x = mp[0] - 0.003*d
                        else:
                            x = mp[0] + 0.003*d
                    elif 50 >= m > 30:
                        if type == 'left' or type == 'bottom':
                            x = mp[0] - 0.005*d
                        else:
                            x = mp[0] + 0.005*d
                    elif 30 >= m > 10:
                        if type == 'left' or type == 'bottom':
                            x = mp[0] - 0.007*d
                        else:
                            x = mp[0] + 0.007*d
                    elif 10 >= m > 5:
                        if type == 'left' or type == 'bottom':
                            x = mp[0] - 0.02*d
                        else:
                            x = mp[0] + 0.02*d
                    else:
                        if type == 'left' or type == 'bottom':
                            x = mp[0] - 0.07*d
                        else:
                            x = mp[0] + 0.07*d
                else:
                    if type == 'left' or type == 'bottom':
                        x = mp[0] - 0.07*d
                    else:
                        x = mp[0] + 0.07*d
            else:
                if m < -1:
                    if m < -50:
                        if type == 'left' or type == 'top':
                            x = mp[0] - 0.003*d
                        else:
                            x = mp[0] + 0.003*d
                    elif -50 < m <= -30:
                        if type == 'left' or type == 'top':
                            x = mp[0] - 0.005*d
                        else:
                            x = mp[0] + 0.005*d
                    elif -30 < m <= -10:
                        if type == 'left' or type == 'top':
                            x = mp[0] - 0.007*d
                        else:
                            x = mp[0] + 0.007*d
                    elif -10 < m <= -5:
                        if type == 'left' or type == 'top':
                            x = mp[0] - 0.02*d
                        else:
                            x = mp[0] + 0.02*d
                    else:
                        if type == 'left' or type == 'top':
                            x = mp[0] - 0.07*d
                        else:
                            x = mp[0] + 0.07*d
                else:
                    if type == 'left' or type == 'top':
                        x = mp[0] - 0.07*d
                    else:
                        x = mp[0] + 0.07*d
            '''
            if 0 < abs(-1/m) < 1:
                if abs(-1/m) > 1/8:
                    if -1/m < 0:
                        if type == 'bottom' or type == 'left':
                            x = mp[0] - 0.07*d
                        else:
                            x = mp[0] + 0.07*d
                    else:
                        if type == 'bottom' or type == 'right':
                            x = mp[0] + 0.07*d
                        else:
                            x = mp[0] - 0.07*d
                else:
                    if -1/m < 0:
                        if type == 'bottom' or type == 'left':
                            x = mp[0] - 0.02*d
                        else:
                            x = mp[0] + 0.02*d
                    else:
                        if type == 'bottom' or type == 'right':
                            x = mp[0] + 0.02*d
                        else:
                            x = mp[0] - 0.02*d
            else:
                if -1/m < 0:
                    if type == 'left' or type == 'bottom':
                        x = mp[0] - 0.2*d
                    else:
                        x = mp[0] + 0.2*d
                else:
                    if type == 'left' or type == 'top':
                        x = mp[0] - 0.2*d
                    else:
                        x = mp[0] + 0.2*d
            '''

            y = m*(x-mp[0])+mp[1]
            # 제어점 (기울기가 m 이고 점 mp를 지나는 방정식 위의 점)
            cp = (x,y)

        return cp
    def drawArrow(ax,start_p=tuple,end_p=tuple,colors=False):
        from math import sqrt
        h = 2
        x1 = start_p[0]
        y1 = start_p[1]
        x2 = end_p[0]
        y2 = end_p[1]
        dx = end_p[0]-start_p[0]
        dy = end_p[1]-start_p[1]
        #new_dx = abs(x1) + sqrt((sqrt(dx**2+dy**2)-h)/2)
        #new_dy = abs(y1) + sqrt((sqrt(dx**2+dy**2)-h)/2)
        head_width = 3*h
        head_length = 1.5*head_width
        new_dx = 0
        new_dy = 0
        if dx == 0: 
            if dy < 0: new_dy = (abs(dy) - head_length)*-1
            else: new_dy = dy - head_length
        elif dy == 0: 
            if dx < 0: new_dx = (abs(dx) - head_length)*-1
            else: new_dx = dx - head_length
        else: raise Exception("not a stright line")
        
        ax.arrow(x1, y1, new_dx, new_dy, width=h)
    l = len(text)*7+2
    dx = end_p[0]-start_p[0]
    dy = end_p[1]-start_p[1]
    if dx == 0:
        middle_p = (((start_p[0]+end_p[0])/2),((start_p[1]+end_p[1])/2))
        middle_p1 = (((start_p[0]+end_p[0])/2),((start_p[1]+end_p[1])/2)+l/2)
        middle_p2 = (((start_p[0]+end_p[0])/2),((start_p[1]+end_p[1])/2)-l/2)
    elif dy == 0:
        middle_p = (((start_p[0]+end_p[0])/2),((start_p[1]+end_p[1])/2))
        middle_p1 = (((start_p[0]+end_p[0])/2-l/2),((start_p[1]+end_p[1])/2))
        middle_p2 = (((start_p[0]+end_p[0])/2+l/2),((start_p[1]+end_p[1])/2))
    else: raise Exception('not a stright line')
    if l == 0:
        drawArrow(ax,middle_p,end_p)
        drawArrow(ax,middle_p,start_p)
    else:
        drawArrow(ax,middle_p2,end_p)
        cp = controlPoint(middle_p1,middle_p2,'left')
        plt.text(cp[0]-l*0.425, middle_p[1]-2, text, fontsize=16, zorder=3)
        drawArrow(ax,middle_p1,start_p)





# 정다각형 그리는 함수
def drawRegular(ax, center, n, radius, fill=False, alpha=1, dash=False):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    if fill:
        if dash:
            pp = mpatches.RegularPolygon(xy=center, fc=random.choice(colors), fill=True, lw=1, ls='--', zorder=3, alpha=alpha)
        else:
            pp = mpatches.RegularPolygon(xy=center, fc=random.choice(colors), fill=True, lw=2, zorder=3, alpha=alpha)
    else:
        if dash:
            pp = mpatches.RegularPolygon(xy=center, ec='black', fill=False, lw=1, ls='--', zorder=3)
        else:
            pp = mpatches.RegularPolygon(xy=center, ec='black', fill=False, lw=2, zorder=3)

    ax.add_patch(pp)

# 막대 그래프
def drawBar(ax, xvalue, yvalue, xlabel='', ylabel=''):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    width = 0.35

    x = np.arange(len(xvalue))
    ax.bar(x=x-width/3, height=yvalue[0], width=width, color=random.choice(colors))
    ax.bar(x=width/3, height=yvalue[1], width=width, color=random.choice(colors))
    ax.bar(x=x+width/3, height=yvalue[2], width=width, color=random.choice(colors))
    '''
    for i in range(len(yvalue)):
        if i == 0:
            ax.bar(x=x-width/2, height=yvalue[i], width=width, color=random.choice(colors))
        else:
            ax.bar(x=x+width/2, height=yvalue[i], width=width, color=random.choice(colors))
    '''
    
    ax.set_ylabel(ylabel)
    ax.set_xticks(x)
    ax.set_xticklabels(xvalue)
    #ax.legend()

# svg파일을 문자열로 반환하는 함수
def saveSvg():
    file = io.StringIO()
    plt.savefig(file, format='svg', dpi=300)
    file.seek(0)
    svg_data = file.getvalue()

    return svg_data

# matplotlib 차트 세팅 함수
def setChart(points=[]):
    # 한글 폰트(나눔 고딕)
    #plt.rc('font', family='HYGothic') # For Windows
    if len(points) == 0:
        fig, ax = plt.subplots()
        plt.grid(True)

        return ax
    #mpl.font_manager._rebuild()
    plt.rc('font', family='NanumGothic')
    x = []
    y = []

    for i in points:
        x.append(i[0])
        y.append(i[1])

    maxlim = max(max(x), max(y))
    minlim = min(min(x), min(y))

    fig, ax = plt.subplots(figsize=(5,5))

    #fig, ax = plt.subplots()

    #plt.grid(True)
    plt.axis("off")
    #plt.axis('scaled') 

    ax.set_xlim(minlim-0.15*maxlim, maxlim+0.15*maxlim)
    ax.set_ylim(minlim-0.15*maxlim, maxlim+0.15*maxlim)

    #ax.set_xlim(0, 10)
    #ax.set_ylim(0, 10)

    return ax

# bezier 곡선의 제어점의 좌표를 구하는 함수
def controlPoint(p1, p2, type):
    d = math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
    #d = 2
    # 지나는 점 (p1, p2의 중점)
    mp = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

    if (p2[0]-p1[0]) == 0:
        if type == 'left' or type == 'top':
            cp = (mp[0]-0.2*d,mp[1])
        else:
            cp = (mp[0]+0.2*d,mp[1])

    elif (p2[1]-p1[1]) == 0:
        if type == 'bottom' or type == 'right':
            cp = (mp[0], mp[1]-0.2*d)
        else:
            cp = (mp[0], mp[1]+0.2*d)
    else:
        # 기울기
        m = - (p2[0]-p1[0])/(p2[1]-p1[1])
        #print(m)
        if m > 0:
            if m > 1:
                if m > 50:
                    if type == 'left' or type == 'bottom':
                        x = mp[0] - 0.003*d
                    else:
                        x = mp[0] + 0.003*d
                elif 50 >= m > 30:
                    if type == 'left' or type == 'bottom':
                        x = mp[0] - 0.005*d
                    else:
                        x = mp[0] + 0.005*d
                elif 30 >= m > 10:
                    if type == 'left' or type == 'bottom':
                        x = mp[0] - 0.007*d
                    else:
                        x = mp[0] + 0.007*d
                elif 10 >= m > 5:
                    if type == 'left' or type == 'bottom':
                        x = mp[0] - 0.02*d
                    else:
                        x = mp[0] + 0.02*d
                else:
                    if type == 'left' or type == 'bottom':
                        x = mp[0] - 0.07*d
                    else:
                        x = mp[0] + 0.07*d
            else:
                if type == 'left' or type == 'bottom':
                    x = mp[0] - 0.07*d
                else:
                    x = mp[0] + 0.07*d
        else:
            if m < -1:
                if m < -50:
                    if type == 'left' or type == 'top':
                        x = mp[0] - 0.003*d
                    else:
                        x = mp[0] + 0.003*d
                elif -50 < m <= -30:
                    if type == 'left' or type == 'top':
                        x = mp[0] - 0.005*d
                    else:
                        x = mp[0] + 0.005*d
                elif -30 < m <= -10:
                    if type == 'left' or type == 'top':
                        x = mp[0] - 0.007*d
                    else:
                        x = mp[0] + 0.007*d
                elif -10 < m <= -5:
                    if type == 'left' or type == 'top':
                        x = mp[0] - 0.02*d
                    else:
                        x = mp[0] + 0.02*d
                else:
                    if type == 'left' or type == 'top':
                        x = mp[0] - 0.07*d
                    else:
                        x = mp[0] + 0.07*d
            else:
                if type == 'left' or type == 'top':
                    x = mp[0] - 0.07*d
                else:
                    x = mp[0] + 0.07*d
        '''
        if 0 < abs(-1/m) < 1:
            if abs(-1/m) > 1/8:
                if -1/m < 0:
                    if type == 'bottom' or type == 'left':
                        x = mp[0] - 0.07*d
                    else:
                        x = mp[0] + 0.07*d
                else:
                    if type == 'bottom' or type == 'right':
                        x = mp[0] + 0.07*d
                    else:
                        x = mp[0] - 0.07*d
            else:
                if -1/m < 0:
                    if type == 'bottom' or type == 'left':
                        x = mp[0] - 0.02*d
                    else:
                        x = mp[0] + 0.02*d
                else:
                    if type == 'bottom' or type == 'right':
                        x = mp[0] + 0.02*d
                    else:
                        x = mp[0] - 0.02*d
        else:
            if -1/m < 0:
                if type == 'left' or type == 'bottom':
                    x = mp[0] - 0.2*d
                else:
                    x = mp[0] + 0.2*d
            else:
                if type == 'left' or type == 'top':
                    x = mp[0] - 0.2*d
                else:
                    x = mp[0] + 0.2*d
        '''

        y = m*(x-mp[0])+mp[1]
        # 제어점 (기울기가 m 이고 점 mp를 지나는 방정식 위의 점)
        cp = (x,y)

    return cp

def line_equation(p1, p2, x):
    y = ((p2[1]-p1[1])/(p2[0]-p1[0])) * (x-p1[0]) + p1[1]

    return y

#plt.rcParams['text.usetex'] = True
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf8')
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf8')

def c_distance(p1=tuple, p2=tuple):
    import math
    d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    return d
def c_angle(p_list=[]):
    import math
    if p_list:
        p1 = p_list[0]
        p2 = p_list[1]
        p3 = p_list[2]

    dx1 = p1[0] - p2[0]
    dy1 = p1[1] - p2[1]

    dx2 = p3[0] - p2[0]
    dy2 = p3[1] - p2[1]

    a1 = math.degrees(math.atan2(dy1,dx1))
    a2 = math.degrees(math.atan2(dy2,dx2))
    d = 50

    angle = a2 -a1
    if angle < 0:
        angle = 360 + angle

    return angle

def new_p(existing_p_list=[],scale=100,distance=0):
    def c_distance(p1=tuple, p2=tuple):
        import math
        d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

        return d
    def same_line(eq_list=list,p=tuple):
        x = p[0]
        y = p[1]
        for eq in eq_list:
            a = eq[0]
            b = eq[1]
            if str(a) == 'x':
                if b == y:
                    return True
            elif a*x + b == y:
                return True
        return False
    import random
    import math
    #prevent the point in the same line
    if len(existing_p_list) > 2:
        linear_eq_list = []
        iter_existing_p_list = iter(existing_p_list)
        first_p = next(iter_existing_p_list)
        x1 = first_p[0]
        y1 = first_p[1]
        for p in iter_existing_p_list: #create equations based on the existing points
            x2 = p[0]
            y2 = p[1]
            if x1 == x2: # x=a equation
                temp_linear_eq = ('x',x1)
            else: # y=ax+b equation
                temp_linear_eq = (int((y1-y2)/(x1-x2)),int((y1-x1*(y1-y2)/(x1-x2))))
            linear_eq_list.append(temp_linear_eq)
            x1 = x2
            y1 = y2
        if len(linear_eq_list) > 1: #handle the equation between first and last point
            x1 = first_p[0]
            y1 = first_p[1]
            if x1 == x2: # x=a equation
                temp_linear_eq = ('x',x1)
            else: # y=ax+b equation
                temp_linear_eq = (int((y1-y2)/(x1-x2)),int((y1-x1*(y1-y2)/(x1-x2))))
            linear_eq_list.append(temp_linear_eq)
    #generate the random point
    if len(existing_p_list) <= 2: #zero or one existing point
        if distance != 0: #find hte point in a certain distance
            if distance > scale: raise Exception("wrong distance/scale")
            #const variable
            existing_x = existing_p_list[0][0]
            existing_y = existing_p_list[0][1]
            #variable
            new_sign = random.choice([1,-1])
            new_x = random.randint(existing_x-distance,existing_x+distance)
            #using circle equation (x-x1)^2 + (y-y1)^2 = r^2
            new_y = existing_y + new_sign*math.sqrt(distance**2-(new_x-existing_x)**2)
            temp_p = (new_x,new_y)
            while temp_p in existing_p_list: # not the same point
                new_sign = random.choice([1,-1])
                new_x = random.randint(existing_x-distance,existing_x+distance)
                #using circle equation (x-x1)^2 + (y-y1)^2 = r^2
                new_y = existing_y + new_sign*math.sqrt(distance**2-(new_x-existing_x)**2)
                temp_p = (new_x,new_y)
        else:
            temp_p = (random.randint(0,scale),random.randint(0,scale))
            while temp_p in existing_p_list: # not the same point
                temp_p = (random.randint(0,scale),random.randint(0,scale))
    else: #more than one existing points
        #create point which ins't in the same line
        temp_p = (random.randint(0,scale),random.randint(0,scale))
        while same_line(linear_eq_list,temp_p):
            temp_p = (random.randint(0,scale),random.randint(0,scale))
    return temp_p
def rotate_p(p_list=list,angle=0):
    def cart2pol(x, y):
        import math
        r = math.sqrt(x**2 + y**2)
        angle_radians = math.atan2(y, x)
        return(r, angle_radians)
    def pol2cart(r, angle_radians):
        import math
        x = r * math.cos(angle_radians)
        y = r * math.sin(angle_radians)
        return(x, y)
    import math
    for i in range(len(p_list)):
        cart_x = p_list[i][0]
        cart_y = p_list[i][1]
        pol_r, pol_angle_radians = cart2pol(cart_x,cart_y)
        pol_angle_radians += math.radians(angle)
        cart_x,cart_y = pol2cart(pol_r,pol_angle_radians)
        p_list[i] = (cart_x,cart_y)
    return p_list


def move_to_center(p_list=list,center_index=-1):
    #calculate center point
    x_center = 0
    y_center = 0
    for p in p_list:
        x_center += p[0]
        y_center += p[1]
    x_center /= len(p_list)
    y_center /= len(p_list)
    new_p_list = []
    if center_index == -1: #center with calculated center point
        x_move = x_center * -1
        y_move = y_center * -1
    else: #center with center_index
        center_p = p_list[center_index]
        x_move = center_p[0] * -1
        y_move = center_p[1] * -1
    #make new list with new points
    for index in range(len(p_list)):
        if center_index == -1:
            p = p_list[index]
            new_p_list.append((p[0]+x_move,p[1]+y_move))
        else:
            if index == center_index:
                new_p_list.append((0,0))
            else:
                p = p_list[index]
                new_p_list.append((p[0]+x_move,p[1]+y_move))
    return new_p_list
def move_p(p_list=list,x_move=0,y_move=0):
    #center point
    new_p_list = []
    for index in range(len(p_list)):
        p = p_list[index]
        new_p_list.append((p[0]+x_move,p[1]+y_move))
    return new_p_list
def drawAngleLine(ax,move_x=0,move_y=0,scale=100,draw=True,show_num=False):
    def new_p(existing_p_list=[],scale=100,distance=0):
        def c_distance(p1=tuple, p2=tuple):
            import math
            d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

            return d
        def same_line(eq_list=list,p=tuple):
            x = p[0]
            y = p[1]
            for eq in eq_list:
                a = eq[0]
                b = eq[1]
                if str(a) == 'x':
                    if b == y:
                        return True
                elif a*x + b == y:
                    return True
            return False
        import random
        import math
        #prevent the point in the same line
        if len(existing_p_list) > 2:
            linear_eq_list = []
            iter_existing_p_list = iter(existing_p_list)
            first_p = next(iter_existing_p_list)
            x1 = first_p[0]
            y1 = first_p[1]
            for p in iter_existing_p_list: #create equations based on the existing points
                x2 = p[0]
                y2 = p[1]
                if x1 == x2: # x=a equation
                    temp_linear_eq = ('x',x1)
                else: # y=ax+b equation
                    temp_linear_eq = (int((y1-y2)/(x1-x2)),int((y1-x1*(y1-y2)/(x1-x2))))
                linear_eq_list.append(temp_linear_eq)
                x1 = x2
                y1 = y2
            if len(linear_eq_list) > 1: #handle the equation between first and last point
                x1 = first_p[0]
                y1 = first_p[1]
                if x1 == x2: # x=a equation
                    temp_linear_eq = ('x',x1)
                else: # y=ax+b equation
                    temp_linear_eq = (int((y1-y2)/(x1-x2)),int((y1-x1*(y1-y2)/(x1-x2))))
                linear_eq_list.append(temp_linear_eq)
        #generate the random point
        if len(existing_p_list) <= 2: #zero or one existing point
            if distance != 0: #find hte point in a certain distance
                if distance > scale: raise Exception("wrong distance/scale")
                #const variable
                existing_x = existing_p_list[0][0]
                existing_y = existing_p_list[0][1]
                #variable
                new_sign = random.choice([1,-1])
                new_x = random.randint(existing_x-distance,existing_x+distance)
                #using circle equation (x-x1)^2 + (y-y1)^2 = r^2
                new_y = existing_y + new_sign*math.sqrt(distance**2-(new_x-existing_x)**2)
                temp_p = (new_x,new_y)
                while temp_p in existing_p_list: # not the same point
                    new_sign = random.choice([1,-1])
                    new_x = random.randint(existing_x-distance,existing_x+distance)
                    #using circle equation (x-x1)^2 + (y-y1)^2 = r^2
                    new_y = existing_y + new_sign*math.sqrt(distance**2-(new_x-existing_x)**2)
                    temp_p = (new_x,new_y)
            else:
                temp_p = (random.randint(0,scale),random.randint(0,scale))
                while temp_p in existing_p_list: # not the same point
                    temp_p = (random.randint(0,scale),random.randint(0,scale))
        else: #more than one existing points
            #create point which ins't in the same line
            temp_p = (random.randint(0,scale),random.randint(0,scale))
            while same_line(linear_eq_list,temp_p):
                temp_p = (random.randint(0,scale),random.randint(0,scale))
        return temp_p
    def c_angle(p_list=[]):
        import math
        if p_list:
            p1 = p_list[0]
            p2 = p_list[1]
            p3 = p_list[2]

        dx1 = p1[0] - p2[0]
        dy1 = p1[1] - p2[1]

        dx2 = p3[0] - p2[0]
        dy2 = p3[1] - p2[1]

        a1 = math.degrees(math.atan2(dy1,dx1))
        a2 = math.degrees(math.atan2(dy2,dx2))
        d = 50

        angle = a2 -a1
        if angle < 0:
            angle = 360 + angle

        return angle
    def move_to_center(p_list=list,center_index=-1):
        #calculate center point
        x_center = 0
        y_center = 0
        for p in p_list:
            x_center += p[0]
            y_center += p[1]
        x_center /= len(p_list)
        y_center /= len(p_list)
        new_p_list = []
        if center_index == -1: #center with calculated center point
            x_move = x_center * -1
            y_move = y_center * -1
        else: #center with center_index
            center_p = p_list[center_index]
            x_move = center_p[0] * -1
            y_move = center_p[1] * -1
        #make new list with new points
        for index in range(len(p_list)):
            if center_index == -1:
                p = p_list[index]
                new_p_list.append((p[0]+x_move,p[1]+y_move))
            else:
                if index == center_index:
                    new_p_list.append((0,0))
                else:
                    p = p_list[index]
                    new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
    def move_p(p_list=list,x_move=0,y_move=0):
        #center point
        new_p_list = []
        for index in range(len(p_list)):
            p = p_list[index]
            new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
    def new_p_middle(p1=tuple,p2=tuple):
        return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
    #points
    angle_center = new_p()
    angle_p1 = new_p([angle_center],scale,scale)
    angle_p2 = new_p([angle_center],scale,scale)
    num_angle = c_angle([angle_p1,angle_center,angle_p2])
    while num_angle > 150 or num_angle < 10:
        angle_center = new_p()
        angle_p1 = new_p([angle_center],scale,scale)
        angle_p2 = new_p([angle_center],scale,scale)
        num_angle = c_angle([angle_p1,angle_center,angle_p2])
    angle = [angle_p1,angle_center,angle_p2]
    angle = move_to_center(angle)
    angle = move_p(angle,move_x,move_y)
    #draw
    if draw:
        drawLine(ax,[angle[0],angle[1]])
        drawLine(ax,[angle[2],angle[1]])
        drawAngle(ax,[angle])
    if show_num:
        #m_p = new_p_middle(angle[0],angle[2])
        c_p = angle[1]
        num_angle = int(c_angle(angle))
        drawText(ax,'$%s\mathrm{°}$'%(num_angle),c_p[0]+10,c_p[1])
    return angle
def new_p_triangle(scale=100,move_x=0,move_y=0):
    def new_p(existing_p_list=[],scale=100,distance=0):
        def c_distance(p1=tuple, p2=tuple):
            import math
            d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

            return d
        def same_line(eq_list=list,p=tuple):
            x = p[0]
            y = p[1]
            for eq in eq_list:
                a = eq[0]
                b = eq[1]
                if str(a) == 'x':
                    if b == y:
                        return True
                elif a*x + b == y:
                    return True
            return False
        import random
        import math
        #prevent the point in the same line
        if len(existing_p_list) > 2:
            linear_eq_list = []
            iter_existing_p_list = iter(existing_p_list)
            first_p = next(iter_existing_p_list)
            x1 = first_p[0]
            y1 = first_p[1]
            for p in iter_existing_p_list: #create equations based on the existing points
                x2 = p[0]
                y2 = p[1]
                if x1 == x2: # x=a equation
                    temp_linear_eq = ('x',x1)
                else: # y=ax+b equation
                    temp_linear_eq = (int((y1-y2)/(x1-x2)),int((y1-x1*(y1-y2)/(x1-x2))))
                linear_eq_list.append(temp_linear_eq)
                x1 = x2
                y1 = y2
            if len(linear_eq_list) > 1: #handle the equation between first and last point
                x1 = first_p[0]
                y1 = first_p[1]
                if x1 == x2: # x=a equation
                    temp_linear_eq = ('x',x1)
                else: # y=ax+b equation
                    temp_linear_eq = (int((y1-y2)/(x1-x2)),int((y1-x1*(y1-y2)/(x1-x2))))
                linear_eq_list.append(temp_linear_eq)
        #generate the random point
        if len(existing_p_list) <= 2: #zero or one existing point
            if distance != 0: #find hte point in a certain distance
                if distance > scale: raise Exception("wrong distance/scale")
                #const variable
                existing_x = existing_p_list[0][0]
                existing_y = existing_p_list[0][1]
                #variable
                new_sign = random.choice([1,-1])
                new_x = random.randint(existing_x-distance,existing_x+distance)
                #using circle equation (x-x1)^2 + (y-y1)^2 = r^2
                new_y = existing_y + new_sign*math.sqrt(distance**2-(new_x-existing_x)**2)
                temp_p = (new_x,new_y)
                while temp_p in existing_p_list: # not the same point
                    new_sign = random.choice([1,-1])
                    new_x = random.randint(existing_x-distance,existing_x+distance)
                    #using circle equation (x-x1)^2 + (y-y1)^2 = r^2
                    new_y = existing_y + new_sign*math.sqrt(distance**2-(new_x-existing_x)**2)
                    temp_p = (new_x,new_y)
            else:
                temp_p = (random.randint(0,scale),random.randint(0,scale))
                while temp_p in existing_p_list: # not the same point
                    temp_p = (random.randint(0,scale),random.randint(0,scale))
        else: #more than one existing points
            #create point which ins't in the same line
            temp_p = (random.randint(0,scale),random.randint(0,scale))
            while same_line(linear_eq_list,temp_p):
                temp_p = (random.randint(0,scale),random.randint(0,scale))
        return temp_p
    def move_to_center(p_list=list,center_index=-1):
        #calculate center point
        x_center = 0
        y_center = 0
        for p in p_list:
            x_center += p[0]
            y_center += p[1]
        x_center /= len(p_list)
        y_center /= len(p_list)
        new_p_list = []
        if center_index == -1: #center with calculated center point
            x_move = x_center * -1
            y_move = y_center * -1
        else: #center with center_index
            center_p = p_list[center_index]
            x_move = center_p[0] * -1
            y_move = center_p[1] * -1
        #make new list with new points
        for index in range(len(p_list)):
            if center_index == -1:
                p = p_list[index]
                new_p_list.append((p[0]+x_move,p[1]+y_move))
            else:
                if index == center_index:
                    new_p_list.append((0,0))
                else:
                    p = p_list[index]
                    new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
    def c_angle(p_list=[]):
        import math
        if p_list:
            p1 = p_list[0]
            p2 = p_list[1]
            p3 = p_list[2]

        dx1 = p1[0] - p2[0]
        dy1 = p1[1] - p2[1]

        dx2 = p3[0] - p2[0]
        dy2 = p3[1] - p2[1]

        a1 = math.degrees(math.atan2(dy1,dx1))
        a2 = math.degrees(math.atan2(dy2,dx2))
        d = 50

        angle = a2 -a1
        if angle < 0:
            angle = 360 + angle

        return angle
    def move_p(p_list=list,x_move=0,y_move=0):
        #center point
        new_p_list = []
        for index in range(len(p_list)):
            p = p_list[index]
            new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
    #points
    angle_center = new_p()
    angle_p1 = new_p([angle_center],scale,scale)
    angle_p2 = new_p([angle_center],scale,scale+random.randint(-30,-1))
    num_angle = c_angle([angle_p1,angle_center,angle_p2])
    while num_angle > 150 or num_angle < 10:
        angle_center = new_p()
        angle_p1 = new_p([angle_center],scale,scale)
        angle_p2 = new_p([angle_center],scale,scale+random.randint(-30,-1))
        num_angle = c_angle([angle_p1,angle_center,angle_p2])
    angle = [angle_p1,angle_center,angle_p2]
    angle = move_to_center(angle)
    angle = move_p(angle,move_x,move_y)
    return angle
def create_p_angle(angle,length,p=[0,0]):
    import math
    angle_radiant = math.radians(angle)
    x = round((math.cos(angle_radiant)*length),5) + p[0]
    y = round((math.sin(angle_radiant)*length),5) + p[1]
    return (x,y)


# 4-1-2-03
def angle412_Stem_001():
    def drawAngle(ax, p_list=[]):
        if p_list:
            p1 = p_list[0]
            p2 = p_list[1]
            p3 = p_list[2]

        dx1 = p1[0] - p2[0]
        dy1 = p1[1] - p2[1]

        dx2 = p3[0] - p2[0]
        dy2 = p3[1] - p2[1]

        a1 = math.degrees(math.atan2(dy1,dx1))
        a2 = math.degrees(math.atan2(dy2,dx2))

        d = 50

        angle = a2 -a1
        if angle < 0:
            angle = 360 + angle

        if angle < 30:
            pp = mpatches.Arc(p2, angle=0, width=0.25*d, height=0.25*d, theta1=a1, theta2=a2, ec='red', zorder=3)
        elif angle > 90:
            pp = mpatches.Arc(p2, angle=0, width=0.2*d, height=0.2*d, theta1=a1, theta2=a2, ec='red', zorder=3)
        else:
            if angle == 90:
                print(a1, a2)
                if a1 == 0.0 and a2 ==90.0:
                    verts = [
                        (p2[0]+0.1*d,p2[1]),
                        (p2[0]+0.1*d,p2[1]+0.1*d),
                        (p2[0],p2[1]+0.1*d)
                    ]
                elif a1 == 90.0 and a2 == 180.0:
                    verts = [
                        (p2[0]-0.1*d,p2[1]),
                        (p2[0]-0.1*d,p2[1]+0.1*d),
                        (p2[0],p2[1]+0.1*d)
                    ]
                elif a1 == 180.0 and a2 == -90.0:
                    verts = [
                        (p2[0]-0.1*d,p2[1]),
                        (p2[0]-0.1*d,p2[1]-0.1*d),
                        (p2[0],p2[1]-0.1*d)
                    ]
                elif a1 == -90.0 and a2 == 0.0:
                    verts = [
                        (p2[0]+0.1*d,p2[1]),
                        (p2[0]+0.1*d,p2[1]-0.1*d),
                        (p2[0],p2[1]-0.1*d)
                    ]
                elif a1 == 45.0 and a2 == 135.0:
                    verts = [
                        (p2[0]-math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d)),
                        (p2[0],p2[1]+2*math.sqrt(0.01*d)),
                        (p2[0]+math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d))
                    ]
                elif a1 >= 135.0 and a2 <= -135.0:
                    verts = [
                        (p2[0]-math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d)),
                        (p2[0]-2*math.sqrt(0.01*d),p2[1]),
                        (p2[0]-math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d))
                    ]
                elif a1 == -135.0 and a2 == -45.0:
                    verts = [
                        (p2[0]-math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d)),
                        (p2[0],p2[1]-2*math.sqrt(0.01*d)),
                        (p2[0]+math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d))
                    ]
                else:
                    verts = [
                        (p2[0]+math.sqrt(0.01*d),p2[1]+math.sqrt(0.01*d)),
                        (p2[0]+2*math.sqrt(0.01*d),p2[1]),
                        (p2[0]+math.sqrt(0.01*d),p2[1]-math.sqrt(0.01*d))
                    ]
                
                codes = [
                        Path.MOVETO,
                        Path.LINETO,
                        Path.LINETO
                    ]
                path = Path(verts,codes)

                pp = mpatches.PathPatch(path, ec='red', fill=False, zorder=3)
            else:
                pp = mpatches.Arc(p2, angle=0, width=0.2*d, height=0.2*d, theta1=a1, theta2=a2, ec='red', zorder=3)
            
        mid = ((p3[0]+p1[0])/2, (p3[1]+p1[1])/2)
        if mid[0]-p2[0] == 0:
            x = p2[0]
            if 0 <= a1 <= 90:
                y = p2[1]+0.2*d
            elif -180 <= a1 <= -90:
                y = p2[1]-0.2*d
        elif mid[1]-p2[1] == 0:
            y = p2[1]
            if 90 <= a1 <= 180:
                x = p2[0]-0.2*d
            elif -90 <= a1 <= 0:
                x = p2[0]+0.2*d
        else:
            n = (mid[1]-p2[1])/(mid[0]-p2[0])

            if 0 <= a1 < 90:
                if angle <= 90:
                    x = p2[0]+0.08*d
                else:
                    x = p2[0]-0.08*d
            elif 90 <= a1 < 180:
                x = p2[0]-0.08*d
            elif -180 <= a1 < -90:
                x = p2[0]-0.08*d
            else:
                x = p2[0]+0.08*d

            y = n*(x-p2[0])+p2[1]


        ax.add_patch(pp)
    def angle412_Stem_001_make_angle(ax,move_x=0,move_y=0):
        #points
        angle_center = new_p()
        angle_p1 = new_p([angle_center],50,40)
        angle_p2 = new_p([angle_center],50,40)
        num_angle = c_angle([angle_p1,angle_center,angle_p2])
        while num_angle > 150 or num_angle < 10:
            angle_center = new_p()
            angle_p1 = new_p([angle_center],50,40)
            angle_p2 = new_p([angle_center],50,40)
            num_angle = c_angle([angle_p1,angle_center,angle_p2])
        angle = [angle_p1,angle_center,angle_p2]
        angle = move_to_center(angle)
        angle = move_p(angle,move_x,move_y)
        return angle
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #generate angles
    angle1 = angle412_Stem_001_make_angle(ax,-66,0) #option1 (-100,-33)~(-33,33)
    angle2 = angle412_Stem_001_make_angle(ax,0,0) #option2 (-33,-33)~(33,33)
    angle3 = angle412_Stem_001_make_angle(ax,66,0) #option3 (33,-33)~(100,33)
    degree_angle1 = c_angle(angle1) 
    degree_angle2 = c_angle(angle2)
    degree_angle3 = c_angle(angle3)
    while abs(degree_angle1-degree_angle2) < 20 or abs(degree_angle2-degree_angle3) < 20 or abs(degree_angle1-degree_angle3) < 20:
        angle1 = angle412_Stem_001_make_angle(ax,-66,0)
        angle2 = angle412_Stem_001_make_angle(ax,0,0)
        angle3 = angle412_Stem_001_make_angle(ax,66,0)
        degree_angle1 = c_angle(angle1)
        degree_angle2 = c_angle(angle2)
        degree_angle3 = c_angle(angle3)
    #find_answer
    smallest_degree = min(degree_angle1,degree_angle2,degree_angle3)
    if degree_angle1 == smallest_degree:
        answer = '(답):A'
    elif degree_angle2 == smallest_degree:
        answer = '(답):B'
    elif degree_angle3 == smallest_degree:
        answer = '(답):C'
    #draw
    #angle1
    drawLine(ax,[angle1[0],angle1[1]])
    drawLine(ax,[angle1[2],angle1[1]])
    drawAngle(ax,angle1)
    #angle2
    drawLine(ax,[angle2[0],angle2[1]])
    drawLine(ax,[angle2[2],angle2[1]])
    drawAngle(ax,angle2)
    #angle3
    drawLine(ax,[angle3[0],angle3[1]])
    drawLine(ax,[angle3[2],angle3[1]])
    drawAngle(ax,angle3)
    #A,B,C
    drawText(ax,'A',-66,40)
    drawText(ax,'B',0,40)
    drawText(ax,'C',66,40)
    plt.axis('scaled')
    #comment
    stem = "세 각 중에서 가장 작은 각을 찾아 기호를 써 보세요."
    comment = "(해설)\n두 변이 벌어진 정도가 가장 작은 각을 찾으면\n"\
                "%s입니다."%(answer.split("(답):")[1])

    #plt.show()
    svg= saveSvg()
    return stem, answer, comment, svg

# 4-1-2-19
def angle412_Stem_002():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #begin
    #generate angles
    p_left = new_p([O],scale=100,distance=100)
    p_right = new_p([O],scale=100,distance=100)
    x_left = p_left[0]
    y_left = p_left[1]
    x_right = p_right[0]
    y_right = p_right[1]
    angle_middle = [p_right,O,p_left]
    degree_angle_middle = c_angle(angle_middle)
    while y_left <= 0 or y_right <= 0 or x_left >= x_right or degree_angle_middle < 30:
        p_left = new_p([O],scale=100,distance=100)
        p_right = new_p([O],scale=100,distance=100)
        x_left = p_left[0]
        y_left = p_left[1]
        x_right = p_right[0]
        y_right = p_right[1]
        angle_middle = [p_right,O,p_left]
        degree_angle_middle = c_angle(angle_middle)
    #angle1,2,3
    angle_left = [p_left,O,x_n]
    angle_middle = [p_right,O,p_left]
    angle_right = [x_p,O,p_right]
    p_middle_text = (int((p_left[0]/3.175+p_right[0]/3.175)/2),20)
    #draw_start
    drawAngle(ax,[angle_left,angle_middle,angle_right],True)
    #line
    drawLine(ax,[x_n,x_p])
    drawLine(ax,[O,p_left])
    drawLine(ax,[O,p_right])
    #point A,B,C
    drawText(ax,'A',-12,-10)
    drawText(ax,'B',p_middle_text[0],p_middle_text[1])
    drawText(ax,'C',10,-10)
    plt.axis('scaled')
    #answer
    degree_angle_left = c_angle(angle_left)
    degree_angle_middle = c_angle(angle_middle)
    degree_angle_right = c_angle(angle_right)
    bigDegree_list = []
    smallDegree_list = []
    if degree_angle_left > 90: 
        bigDegree_list.append('A')
        answer_A = "둔각"
    else: 
        smallDegree_list.append('A')
        answer_A = "예각"
    if degree_angle_middle > 90: 
        bigDegree_list.append('B')
        answer_B = "둔각"
    else: 
        smallDegree_list.append('B')
        answer_B = "예각"
    if degree_angle_right > 90: 
        bigDegree_list.append('C')
        answer_C = "둔각"
    else: 
        smallDegree_list.append('C')
        answer_C = "예각"
    answer = '(답):%s, %s, %s' %(answer_A,answer_B,answer_C)
    
    boxblank = "$$수식$$BOX{　　　}$$/수식$$"
    #stem/comment
    stem = "각을 보고 예각, 둔각 중 어느 것인지 각각 써보세요.\n"\
            "A : {boxblank}, B : {boxblank}, C : {boxblank}".format(boxblank=boxblank)
    comment = "(해설)\n"
    if smallDegree_list: #예각
        small_angle_names = ""
        for angle_name in smallDegree_list:
            small_angle_names += angle_name + '와 '
        small_angle_names = small_angle_names[:len(small_angle_names)-2]
        comment += "%s는 각도가 $$수식$$0 °$$/수식$$보다 크고 직각보다 작은\n"%(small_angle_names)
        comment += "각이므로 예각입니다.\n"
    if bigDegree_list: #둔각
        big_angle_names = ""
        for angle_name in bigDegree_list:
            big_angle_names += angle_name + '와 '
        big_angle_names = big_angle_names[:len(big_angle_names)-2]
        comment += "%s는 각도가 직각보다 크고 $$수식$$180 °$$/수식$$보다 작은\n" %(big_angle_names)
        comment += "각이므로 둔각입니다."
    #plt.show()
    svg= saveSvg()
    return stem, answer, comment, svg

# 4-1-2-21
def angle412_Stem_003():
    #generate list
    degree_list = []
    answer_list = []
    answer = 0
    while len(degree_list) < 5: #create list of random angles
        random_degree_10 = random.randint(1,17)
        random_degree = random_degree_10*10
        if random_degree not in degree_list:
            degree_list.append(random_degree)
            if random_degree < 90:
                answer += 1
                answer_list.append(random_degree)
    if answer_list == []: #예외 상황: 예각이 없음
        answer += 1
        answer_list.append(random.randint(1,8)*10)
        degree_list[random.randint(0,4)] = answer_list[0]
    #stem/comment
    stem = "다음에서 예각은 모두 몇 개인가요?\n"
    stem += '$$표$$$$수식$$'
    comment_answer_part = ''
    for degree in degree_list:
        stem += '%s°```'%(degree)
        if degree in answer_list:
            comment_answer_part += '$$수식$$%s°$$/수식$$, '%(degree)
    comment_answer_part = comment_answer_part[:len(comment_answer_part)-2]
    stem += "$$/수식$$$$/표$$"        
    comment = "(해설)\n예각은 각도가 $$수식$$0 °$$/수식$$보다 크고 직각보다 작은\n"
    comment += "각입니다.\n"
    comment += "따라서 예각은 %s의 $$수식$$%s$$/수식$$개입니다." %(comment_answer_part,answer)
    answer = '(답):$$수식$$%s$$/수식$$개'%(answer)
    return stem,answer,comment
        
# 4-1-2-27
def angle412_Stem_004():
    def drawAngleLine(ax,move_x,move_y,show_num=False):#points
        angle_center = new_p()
        angle_p1 = new_p([angle_center],50,40)
        angle_p2 = new_p([angle_center],50,40)
        num_angle = c_angle([angle_p1,angle_center,angle_p2])
        while num_angle > 150 or num_angle < 10:
            angle_center = new_p()
            angle_p1 = new_p([angle_center],50,40)
            angle_p2 = new_p([angle_center],50,40)
            num_angle = c_angle([angle_p1,angle_center,angle_p2])
        angle = [angle_p1,angle_center,angle_p2]
        angle = move_to_center(angle)
        angle = move_p(angle,move_x,move_y)
        #draw
        drawLine(ax,[angle[0],angle[1]])
        drawLine(ax,[angle[2],angle[1]])
        drawAngle(ax,[angle])
        if show_num:
            #m_p = new_p_middle(angle[0],angle[2])
            c_p = angle[1]
            num_angle = round(int(c_angle(angle)),1)
            num_angle = num_angle - (num_angle%10)
            drawText(ax,'$%s\mathrm{°}$'%(num_angle),c_p[0]+10,c_p[1])
        return angle
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #angle1,angle2
    angle1 = drawAngleLine(ax,-50,0,True)
    angle2 = drawAngleLine(ax,50,0,True)
    num_angle1 = int(c_angle(angle1))
    num_angle1 = num_angle1 - (num_angle1%10)
    num_angle2 = int(c_angle(angle2))
    num_angle2 = num_angle2 - (num_angle2%10)
    plt.axis('scaled')
    #stem/answer/comment
    stem = "두 각도의 합과 차를 구해 순서대로 쓰세요."
    answer = "(답):$$수식$$%s°$$/수식$$, $$수식$$%s°$$/수식$$" %(num_angle1+num_angle2,abs(num_angle1-num_angle2))
    comment = "(해설)\n합은 $$수식$$%s°+%s°=%s°$$/수식$$이고,\n" %(num_angle1,num_angle2,num_angle1+num_angle2)
    comment += "차는 $$수식$$%s°-%s°=%s°$$/수식$$입니다." %(max(num_angle1,num_angle2),min(num_angle1,num_angle2),abs(num_angle1-num_angle2))
    #plt.show()
    svg= saveSvg()
    return stem, answer, comment, svg

# 4-1-2-29, 30
def angle412_Stem_005():
    flag = random.randint(0,1)
    if flag: #29
        stem = "다음 중 각도의 합이 가장 큰 것을 찾아 기호를 써 보세요.\n"\
                "$$표$$"
        char_list = ['㉠', '㉡', '㉢', '㉣']
        num_list = []
        #create num_list
        while len(num_list) < 4:
            random_num10 = random.randint(1,10)
            random_num5 = random.randint(1,20)
            if (random_num10*10 + random_num5*5) not in num_list:
                if random.randint(0,1):
                    num_list.append((random_num10*10,random_num5*5,(random_num10*10 + random_num5*5)))
                else:
                    num_list.append((random_num5*5,random_num10*10,(random_num10*10 + random_num5*5)))
        #find answer & form stem/comment
        max_index = 0
        max_num = num_list[0][2]
        addedNum_list = []
        comment = "(해설)\n"
        for i in range(len(num_list)):
            num1 = num_list[i][0]
            num2 = num_list[i][1]
            addedNum = num_list[i][2]
            addedNum_list.append(addedNum)
            stem += char_list[i] +' $$수식$$%s° + %s°$$/수식$$  '%(num1,num2)
            comment += char_list[i] +' $$수식$$%s° + %s° = %s°$$/수식$$\n'%(num1,num2,addedNum)
            if addedNum > max_num:
                max_index = i
                max_num = addedNum
            if i == 1:
                stem += '\n'
        stem += '$$/표$$'
        addedNum_list.sort(reverse=True)

        answer = '(답):%s'%char_list[max_index]
        comment += "따라서 $$수식$$%s° &gt; %s° &gt; %s° &gt; %s°$$/수식$$ 이므로 각도의\n" %(addedNum_list[0],addedNum_list[1],addedNum_list[2],addedNum_list[3])
        comment += "합이 가장 큰 것은 %s입니다." %(char_list[max_index])
    else: #30
        stem = "각도가 가장 큰 것부터 차례대로 기호를 써 보세요.\n"\
                "$$표$$"
        char_list = ['㉠', '㉡', '㉢', '㉣']
        num_list = []
        c_num_list = []
        #create num_list [(num1,num2,sign_num,c_num)]
        while len(num_list) < 4:
            random_num1 = random.randint(1,20)
            random_num2 = random.randint(1,20)
            sign_num = random.choice([1,-1])
            if ((random_num1*5 + random_num2*5*sign_num) not in c_num_list) and ((random_num1*5 + random_num2*5*sign_num) > 0):
                num_list.append((random_num1*5,random_num2*5,sign_num,(random_num1*5 + random_num2*5*sign_num)))
                c_num_list.append(random_num1*5 + random_num2*5*sign_num)
        c_num_list.sort(reverse=True)
        #find answer & form stem/comment
        max_index = 0
        max_num = num_list[0][3]
        comment = "(해설)\n"
        answer = ""
        for i in range(len(num_list)):
            num1 = num_list[i][0]
            num2 = num_list[i][1]
            sign_num = num_list[i][2]
            c_num = num_list[i][3]
            for j in range(len(c_num_list)):
                if num_list[j][3] == c_num_list[i]:
                    answer += char_list[j] +', '
            if sign_num == 1: # add
                stem += '%s $$수식$$%s° + %s° $$/수식$$  '%(char_list[i],num1,num2)
                comment += '%s $$수식$$%s° + %s° = %s°$$/수식$$\n' %(char_list[i],num1,num2,c_num)
            else: # subtract
                stem += '%s $$수식$$%s° - %s° $$/수식$$  '%(char_list[i],num1,num2)
                comment += '%s $$수식$$%s° - %s° = %s°$$/수식$$\n'%(char_list[i],num1,num2,c_num)
            if c_num > max_num:
                max_index = i
                max_num = c_num
            if i == 1:
                stem += '\n'
        stem += '$$/표$$'
        temp = answer[:len(answer)-2]
        answer = "(답):" + temp
        comment += "따라서 $$수식$$%s° &gt; %s° &gt; %s° &gt; %s°$$/수식$$ 이므로 각도가\n" %(c_num_list[0],c_num_list[1],c_num_list[2],c_num_list[3])
        comment += "가장 큰 것부터 차례대로 기호를 써 보면\n%s입니다."%(temp)

    return stem,answer,comment

# 4-1-2-32
def angle412_Stem_006():
    stem = "가장 큰 각도와 가장 작은 각도의 차를 구해보세요.\n"
    num_list = []
    while len(num_list) < 3:
        random_num5 = random.randint(1,36)
        if (random_num5*5) not in num_list:
            num_list.append(random_num5*5)
    #find max/min index&value + form stem
    min_index = 0
    min_value = num_list[0]
    max_index = 0
    max_value = num_list[0]
    stem += '$$표$$$$수식$$'
    for i in range(len(num_list)):
        num = num_list[i]
        stem += '%s°```'%(num)
        if num > max_value:
            max_index = i
            max_value = num
        if num < min_value:
            min_index = i
            min_value = num
    stem += '$$/수식$$$$/표$$'
    num_list.sort(reverse=True)
    comment = "(해설)\n$$수식$$%s° > %s° > %s°$$/수식$$이므로 가장 큰 각도는\n" %(num_list[0],num_list[1],num_list[2])
    comment += "$$수식$$%s°$$/수식$$이고 가장 작은 각도는 $$수식$$%s°$$/수식$$입니다.\n" %(max_value,min_value)
    comment += "따라서 가장 큰 각도와 가장 작은 각도의 차는\n"
    comment += "$$수식$$%s° - %s° = %s°$$/수식$$입니다."  %(max_value,min_value,max_value-min_value)
    answer = '(답):$$수식$$%s°$$/수식$$'%(max_value-min_value)

    return stem,answer,comment

# 4-1-2-35
def angle412_Stem_007():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #generate variable
    random_angle = random.randint(3,14)*5
    angle1 = random_angle
    angle2 = 90 - random_angle
    #generate shapes
    l_bottom = [(-70,0),(70,0)]
    p = create_p_angle(angle1,70)
    p_middle = rotate_p([p],90)[0]
    l_right = [(0,0),p]
    l_middle = [(0,0),p_middle]
    #draw
    drawLine_multiple(ax,[l_bottom,l_right,l_middle])
    drawAngle_multiple(ax,[[(70,0),O,p],[p,O,p_middle],[p_middle,O,(-70,0)]])
    drawText(ax,'A',-10,-7)
    drawText(ax,'$%s \mathrm{°}$'%angle1,10,-7)
    plt.axis('scaled')
    #stem/answer/comment
    stem = "A에 알맞은 각도를 써 보세요"
    answer = '(답):$$수식$$%s°$$/수식$$'%(angle2)
    comment = "(해설)\n한 직선으로 이루어진 각도는 $$수식$$180 °$$/수식$$이므로\n"\
                "□ $$수식$$ = 180 ° - 90 ° - %s° = %s°$$/수식$$입니다."%(
                    angle1,angle2
                )
    #plt.show()
    svg = saveSvg()
    return stem, answer, comment, svg

# 4-1-2-37, 40
def angle412_Stem_008():
    stem = "A의 알맞은 각도를 써 보세요."
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    while True:
        p = new_p([O],distance=random.randint(40,70))
        triangle = [(-50,0),p,(50,0)]
        num_angle1 = int(c_angle([triangle[0],triangle[1],triangle[2]]))
        num_angle1 = num_angle1 - (num_angle1%5)
        num_angle2 = int(c_angle([triangle[1],triangle[2],triangle[0]]))
        num_angle2 = num_angle2 - (num_angle2%5)
        num_angle0 = 180 - (num_angle1 + num_angle2)
        noRightAngles = num_angle1 != 90 and num_angle2 != 90 and num_angle0 != 90
        notSameAngles = num_angle1 != num_angle2 and num_angle1 != num_angle0 and num_angle2 != num_angle0
        isProperPosition = p[1] > 20
        if isProperPosition and noRightAngles and notSameAngles:
            break
    triangle = move_to_center(triangle)
    left_p = triangle[0]
    top_p = triangle[1]
    right_p = triangle[2]
    drawLine(ax,[triangle[0],triangle[1]])
    drawLine(ax,[triangle[1],triangle[2]])
    drawLine(ax,[triangle[2],triangle[0]])
    problem_option = random.randint(0,1)
    problem_option = 1
    if problem_option: #37
        drawAngle(ax,[[triangle[0],triangle[1],triangle[2]]])
        drawAngle(ax,[[triangle[1],triangle[2],triangle[0]]])
        drawAngle(ax,[[triangle[2],triangle[0],triangle[1]]])
        indexPositionOfA = random.randint(0,2)
        if indexPositionOfA == 0:
            drawText(ax,'A',triangle[1][0]+2,triangle[1][1]+3)
            drawText(ax,'$%s \mathrm{°}$'%(num_angle2),triangle[2][0]-5,triangle[2][1]-7)
            drawText(ax,'$%s \mathrm{°}$'%(num_angle0),triangle[0][0]+5,triangle[0][1]-7)
            answer_1 = num_angle2
            answer_2 = num_angle0
            answer = 180 - num_angle2 - num_angle0
        elif indexPositionOfA == 1:
            drawText(ax,'$%s \mathrm{°}$'%(num_angle1),triangle[1][0]+2,triangle[1][1]+3)
            drawText(ax,'A',triangle[2][0]-5,triangle[2][1]-7)
            drawText(ax,'$%s \mathrm{°}$'%(num_angle0),triangle[0][0]+5,triangle[0][1]-7)
            answer_1 = num_angle1
            answer_2 = num_angle0
            answer = 180 - num_angle1 - num_angle0
        elif indexPositionOfA == 2:
            drawText(ax,'$%s \mathrm{°}$'%(num_angle1),triangle[1][0]+2,triangle[1][1]+3)
            drawText(ax,'$%s \mathrm{°}$'%(num_angle2),triangle[2][0]-5,triangle[2][1]-7)
            drawText(ax,'A',triangle[0][0]+5,triangle[0][1]-7)
            answer_1 = num_angle1
            answer_2 = num_angle2
            answer = 180 - num_angle1 - num_angle2
        temp = answer        
        answer = "(답):$$수식$$%s°$$/수식$$"%(answer)
        comment = "(해설)\n삼각형의 세 각의 크기의 합은 $$수식$$180 °$$/수식$$ 이므로\n "
        comment += "□ $$수식$$= 180 °-%s°-%s°=%s$$/수식$$입니다." %(answer_1,answer_2,temp)
    else: #40
        indexPositionOfA = random.randint(0,1)
        if indexPositionOfA == 0: # left:triangle[0]
            drawAngle(ax,[[left_p,top_p,right_p]])
            drawAngle(ax,[[top_p,right_p,left_p]])
            drawText(ax,'$%s \mathrm{°}$'%(num_angle1),top_p[0],top_p[1]+5)
            drawText(ax,'$%s \mathrm{°}$'%(num_angle2),right_p[0]-5,right_p[1]-5)
            #answer angle
            drawAngle(ax,[[top_p,left_p,(-100,right_p[1])]])
            drawLine(ax,[left_p,(left_p[0]-30,left_p[1])])
            drawText(ax,'A',left_p[0],left_p[1]-5)
            
            answer_1 = num_angle2
            answer_2 = num_angle1
            answer = num_angle2 + num_angle1
        elif indexPositionOfA == 1: #right:traingle[2]
            drawAngle(ax,[[left_p,top_p,right_p]])
            drawAngle(ax,[[right_p,left_p,top_p]])
            drawText(ax,'$%s \mathrm{°}$'%(num_angle1),top_p[0],top_p[1]+5)
            drawText(ax,'$%s \mathrm{°}$'%(num_angle0),left_p[0]+5,left_p[1]-5)
            #answer angle
            drawAngle(ax,[[(100,right_p[1]),right_p,top_p]])
            drawLine(ax,[left_p,(right_p[0]+30,right_p[1])])
            drawText(ax,'A',right_p[0],right_p[1]-5)

            answer_1 = num_angle1
            answer_2 = num_angle0
            answer = num_angle1 + num_angle0

        temp = answer 
        answer = '(답):$$수식$$%s°$$/수식$$'%(answer)
        comment = "(해설)\n삼각형에서 한 꼭짓점에서의 밖에 있는 각도는\n"
        comment += "다른 두 꼭짓점의 각도의 합과 같으므로\n "
        comment += "□ $$수식$$= %s°+%s°=%s$$/수식$$입니다." %(answer_1,answer_2,temp)
    plt.axis('scaled')
    #plt.show()
    svg= saveSvg()
    return stem, answer, comment, svg

# 4-1-2-44
def angle412_Stem_009():
    #create num_list
    num_list = []
    while len(num_list) < 3:
        random_num5 = random.randint(4,30)
        if random_num5 not in num_list:
            num_list.append(random_num5*5)
        if sum(num_list) > 180:
            num_list = []
            continue
        if len(num_list) == 3:
            num_list[2] = 180 - (num_list[0] + num_list[1])
    stem = "어떤 삼각형의 두 각의 크기는 각각 $$수식$$%s°$$/수식$$, $$수식$$%s°$$/수식$$"\
            "입니다. 이 삼각형의 나머지 한 각의 크기를 구해보세요."%(num_list[0], num_list[1])
    answer = '(답):$$수식$$%srm°$$/수식$$'%(num_list[2])
    comment = "(해설)\n삼각형의 세 각의 크기의 합은 $$수식$$180 °$$/수식$$이므로\n"
    comment += "삼각형의 나머지 한 각의 크기는\n"
    comment += "$$수식$$180 °-%s°-%s°=%s°$$/수식$$입니다." %(num_list[0], num_list[1], num_list[2])
    return stem,answer,comment

# 4-1-2-50, 51
def angle412_Stem_010():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    distance = random.randint(40,70)
    #p1:left, p2:right
    while True:
        p1 = new_p([O],distance=distance)
        p2 = new_p([O],distance=distance)
        angle1 = int(c_angle([(-50,0),p1,p2]))
        angle1 = angle1 - (angle1%10)
        angle2 = int(c_angle([p1,p2,(50,0)]))
        angle2 = angle2 - (angle2%10)
        angle3 = int(c_angle([p2,(50,0),(-50,0)]))
        angle3 = angle3 - (angle3%10)
        angle4 = 360 - (angle1+angle2+angle3)
        hasPositiveY = p1[1] > 0 and p2[1] > 0
        p1IsLeft_p2IsRight = p1[0] < 0 and p2[0] > 0
        noRightAngle = angle1 != 90 and angle2 != 90 and angle3 != 90 and angle4 != 90
        notTooClose = c_distance(p1,p2) > 20
        if hasPositiveY and p1IsLeft_p2IsRight and noRightAngle and notTooClose:
            break
    rectangle = [(-50,0),p1,p2,(50,0)]
    drawPolygonAngle(ax,rectangle,True)
    set_point_angle_position = True
    if set_point_angle_position:
        #point
        top_left_p = p1
        top_right_p = p2
        bottom_right_p = (50,0)
        bottom_left_p = (-50,0)
        #angle
        top_left_angle = int(c_angle([(-50,0),p1,p2]))
        top_left_angle = top_left_angle - (top_left_angle%10)
        top_right_angle = int(c_angle([p1,p2,(50,0)]))
        top_right_angle = top_right_angle - (top_right_angle%10)
        bottom_right_angle = int(c_angle([p2,(50,0),(-50,0)]))
        bottom_right_angle = bottom_right_angle - (bottom_right_angle%10)
        bottom_left_angle = int(c_angle([(50,0),(-50,0),p1]))
        bottom_left_angle = bottom_left_angle - (bottom_left_angle%10)
        bottom_left_angle = 360 - (top_left_angle+top_right_angle+bottom_right_angle)#accurate angle
        #address for angle text
        top_left_angle_xy = (top_left_p[0],top_left_p[1]+3)
        top_right_angle_xy = (top_right_p[0],top_right_p[1]+3)
        bottom_right_angle_xy = (bottom_right_p[0]-5,bottom_right_p[1]-7)
        bottom_left_angle_xy = (bottom_left_p[0]+5,bottom_left_p[1]-7)
        #answer_list
        answer_list = [top_left_angle,top_right_angle,bottom_right_angle,bottom_left_angle]
        answer_xy = [top_left_angle_xy,top_right_angle_xy,bottom_right_angle_xy,bottom_left_angle_xy]
    flag = random.randint(0,1)
    if flag == 0: #40:one answer
        stem = "사각형에서 A의 알맞은 각도를 써 보세요."
        answer_index = random.randint(0,3)
        answer = str(answer_list[answer_index])
        answer_list[answer_index] = 'A'
        comment = "(해설)\n사각형의 네 각의 크기의 합은 $$수식$$360 °$$/수식$$이므로\n"
        comment += "$$수식$$"
        for i in range(len(answer_list)):
            if str(answer_list[i]) != 'A':
                comment += str(answer_list[i]) +'°+'
        comment += "$$/수식$$ "
        comment += '□ $$수식$$=360 °$$/수식$$,\n '
        comment += '□ $$수식$$+%s°=360 °$$/수식$$, □ $$수식$$=360 °-%s°=%s°$$/수식$$\n' %(360-int(answer),360-int(answer),answer)
        comment += '입니다.'
    else: #41:two answer
        stem = "사각형에서 A와 B의 각도의 합을 구해 보세요."
        answer_list[random.randint(0,3)] = 'A'
        random_num = random.randint(0,3)
        while answer_list[random_num] == 'A':
            random_num = random.randint(0,3)
        answer_list[random_num] = 'B'
        comment = "(해설)\n사각형의 네 각의 크기의 합은 $$수식$$360 °$$/수식$$이므로\n"
        comment += '$$수식$$A+B'
        answer = 0
        for i in range(len(answer_list)):
            if str(answer_list[i]) not in ['A','B']:
                comment += '+' + str(answer_list[i]) +'°'
                answer += answer_list[i]
        answer = 360 - answer
        comment += "=360 °$$/수식$$,\n"
        comment += "$$수식$$A+B+%s°=360 °$$/수식$$,\n" %(360-answer)
        comment += "$$수식$$A+B=360 °-%s°=%s°$$/수식$$입니다." %(360-answer,answer)
        answer = str(answer)
    #text
    for i in range(len(answer_list)):
        output_text = str(answer_list[i])
        if str(answer_list[i]) not in ['A','B']:
            output_text += '\mathrm{°}'
        drawText_(ax,'$%s$'%output_text,answer_xy[i])
    answer = '(답):$$수식$$%s°$$/수식$$'%(answer)
    #plt.show()
    plt.axis('scaled')
    svg=saveSvg()
    return stem,answer,comment,svg
