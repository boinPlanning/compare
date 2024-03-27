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
        drawText(ax,text[i],points[i],position[i])

        if fill:
            ax.plot(points[i][0], points[i][1],"k.", zorder=3)
def setPolygonPoint(ax,verts,points=list,text=[]):
    def find_text_position_polygon(p_list,p):
        def new_p_center(p_list=[]):
            #calculate center point
            x_center = 0
            y_center = 0
            for p in p_list:
                x_center += p[0]
                y_center += p[1]
            x_center /= len(p_list)
            y_center /= len(p_list)
            return (x_center,y_center)
        center = new_p_center(p_list)
        x_center = center[0]
        y_center = center[1]
        x = p[0]
        y = p[1]
        dx = abs(x-x_center)
        dy = abs(y-y_center)
        #exceptional case
        if x*x_center >= 0 and x_center == x:
            if y > y_center:
                position = 'top'
            elif y < y_center:
                position = 'bottom'
        elif y*y_center >= 0 and y_center == y:
            if x > x_center:
                position = 'right'
            elif x < x_center:
                position = 'left'
        #normal case
        elif dx >= dy: #right/left - x
            if x >= x_center: #right
                position = 'right'
            else: #left
                position = 'left'
        else: #top/bottom - y
            if y >= y_center: #top
                position = 'top'
            else: #bottom
                position = 'bottom'
        return position
    if len(points) != len(text): raise Exception("Number of text and number of point do not match")
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
        position = find_text_position_polygon(verts,cp)
        drawText(ax,text[i],cp,position)

    
# 점
def drawDot(ax,points=list,colors=False):
    if colors: format = 'r.'
    else: format = 'k.'
    for i in range(0,len(points)):
        ax.plot(points[i][0], points[i][1],format, zorder=3)

# 각
def drawPolygonAngle(ax, verts=list, show_angle=[], show_angle_num=[], show_point=[]):
    def drawAngle(ax, multiple_p_list=[],diff=False):
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
            angle = int(a2 -a1)
            if angle < 0:
                angle = 360 + angle
            #approximate
            if angle >= 89 and angle <= 91:
                angle = 90
                if abs(a2) <= 2:
                    a2 = 0.0
                if a2 >= 89 and a2 <= 91:
                    a2 = 90.0
            #width&height
            d = 50
            if angle <= 30:
                width = 0.4*d
                height = 0.4*d
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
    def text_position_top_bottom(p):
        x = p[0]
        y = p[1]
        output = ""
        if y > 0:
            output += 'top'
        else:
            output += 'bottom'
        #exception_case
        if x==0:
            if y > 0:
                return 'top'
            else:
                return 'bottom'
        if y==0:
            if x > 0:
                return 'right'
            else:
                return 'left'
        return output
    def text_position_right_left(p):
        x = p[0]
        y = p[1]
        output = ""
        if x > 0:
            output += 'right'
        else:
            output += 'left'
        #exception_case
        if x==0:
            if y > 0:
                return 'top'
            else:
                return 'bottom'
        if y==0:
            if x > 0:
                return 'right'
            else:
                return 'left'
        return output

    if len(verts) != len(show_angle) and show_angle != []: raise Exception("size of verts and size of show_angle don't match")
    if len(verts) != len(show_angle_num) and show_angle_num != []: raise Exception("size of verts and size of show_angle_num don't match")
    if len(verts) != len(show_point) and show_point != []: raise Exception("size of verts and size of show_point don't match")
    #draw angle/angle_num
    angle_sum = 0
    for i in range(len(verts)):
        first_index = i % (len(verts))
        second_index = (i+1) % (len(verts))
        third_index = (i+2) % (len(verts))
        angle = [verts[first_index],verts[second_index],verts[third_index]]
        #total angle_num should be n*180
        if i == (len(verts)-1): #last angle
            angle_num = 180*(i-1) - angle_sum
        else: #rest angle
            angle_num = round(c_angle(angle))
            if (angle_num%5) < 5:
                angle_num = angle_num - (angle_num%5)
            angle_sum += angle_num
        #angle_sign
        if show_angle != []:
            if show_angle[i] == True: drawAngle(ax,[angle])
            elif show_angle[i] == False: pass
            else: raise Exception("Invalid input")
        #angle_num
        if show_angle_num != []:
            angle_p = verts[second_index]
            position = text_position_top_bottom(angle_p)
            if show_angle_num[i] == True: drawText(ax,'%s°'%(angle_num),angle_p,position)
            elif show_angle_num[i] == False: pass
            else: raise Exception("Invalid input")
        #point_text
        if show_point != []:
            text_p = verts[second_index]
            text = show_point[second_index]
            position = text_position_right_left(text_p)
            if show_point[i] != '': setPoint(ax,[text_p],[text],[position])
def drawAngle_multiple(ax, multiple_p_list=[],diff=False):
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
        angle = a2 -a1
        if angle < 0:
            angle = 360 + angle
        #width&height
        d = 50
        if angle < 30:
            width = 0.4*d
            height = 0.4*d
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
            
            codes = [
                    Path.MOVETO,
                    Path.LINETO,
                    Path.LINETO
                ]
            path = Path(verts,codes)

            pp = mpatches.PathPatch(path, ec=color[i], fill=False, zorder=3)
        elif angle < 30:
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
def drawAngle(ax, p_list=[]):
    color = ['r','g','b','c','m','y']
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
    angle = a2 -a1
    if angle < 0:
        angle = 360 + angle

    #width&height
    d = 50
    if angle < 30:
        width = 0.4*d
        height = 0.4*d
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
def drawLine(ax,pts,dash=False,color='black'):
    if dash: linestype = '--'
    else: linestype = '-'

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
def drawPolygon(ax, verts, fill=False, alpha=1, dash=False,color=''):
    def drawLine(ax,pts,dash=False,color='gray',alpha=alpha):
        if dash: linestype = 'dashed'
        else: linestype = '-'
        line_1 = matplotlib.lines.Line2D((pts[0][0],pts[1][0]), (pts[0][1],pts[1][1]), linewidth=1, linestyle = linestype,color=color,alpha=alpha)
        ax.add_line(line_1)
    if len(verts) == 2:
        drawLine(ax,verts,dash,'gray',alpha)
    else:
        if color != '': colors = [color]
        else:
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
                pp = mpatches.PathPatch(path, fc=random.choice(colors), fill=True, lw=1, zorder=3, alpha=alpha)
        else:
            if dash:
                pp = mpatches.PathPatch(path, ec='black', fill=False, lw=1, ls='--', zorder=3, alpha=alpha)
            else:
                pp = mpatches.PathPatch(path, ec='black', fill=False, lw=1, zorder=3, alpha=alpha)
        ax.add_patch(pp)
        verts.pop()
def drawPolygon_multiple(ax, polygon, fill=False, alpha=1, dash=False,color=''):
    def drawLine(ax,pts,dash=False,color='gray',alpha=alpha):
        if dash: linestype = '--'
        else: linestype = '-'
        line_1 = matplotlib.lines.Line2D((pts[0][0],pts[1][0]), (pts[0][1],pts[1][1]), lw=1, ls = linestype,color=color,alpha=alpha,zorder=3)
        ax.add_line(line_1)
    blue = ['cornflowerblue','royalblue','lightsteelblue']
    orange = ['peachpuff','orange','moccasin']
    purple = ['violet','mediumorchid','plum']
    green = ['limegreen','forestgreen','palegreen']
    yellow = ['lightyellow','khaki','ivory']
    for i in range(len(polygon)):
        verts = polygon[i]
        if len(verts) == 2:
            drawLine(ax,verts,dash=dash,color='gray',alpha=alpha)
            continue
        if color != '':
            if color == 'Blue':
                colors = blue
            elif color == 'Oragne':
                colors = orange
            elif color == 'Purple':
                colors = purple
            elif color == 'Green':
                colors = green
            elif color == 'Yellow':
                colors == yellow
            else:
                colors = [color]
        else:
            colors = random.choice([blue,orange,purple,green,yellow])
        
        vert = verts
        vert.append(verts[0])
        codes = [Path.MOVETO]

        for j in range(0,len(vert)-2):
            codes.append(Path.LINETO)

        codes.append(Path.CLOSEPOLY)

        path = Path(vert,codes)
        
        if fill:
            if dash:
                pp = mpatches.PathPatch(path, fc='gray', fill=True, lw=1, ls='--', zorder=3, alpha=alpha)
            else:
                pp = mpatches.PathPatch(path, fc=colors[i], fill=True, lw=1, zorder=3, alpha=alpha)
        else:
            if dash:
                pp = mpatches.PathPatch(path, ec='gray', fill=False, lw=1, ls='--', zorder=3)
            else:
                pp = mpatches.PathPatch(path, ec='k', fill=False, lw=1, zorder=3)
        ax.add_patch(pp)
        verts.pop()

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
            pp = mpatches.Arc(center, width=radius*2, height=radius*2, angle=0, theta1=theta1, theta2=theta2, ec='black', lw=1, fill=False, zorder=3)
    else:
        if fill:
            if dash:
                pp = mpatches.Circle(center,radius=radius, fc=random.choice(colors), ec='black', lw=1, ls='--', fill=True, zorder=3, alpha=alpha)
            else:
                pp = mpatches.Circle(center,radius=radius, fc=random.choice(colors), ec='black', lw=1, fill=True, zorder=3, alpha=alpha)
        else:
            if dash:
                pp = mpatches.Circle(center,radius=radius, ec='black', lw=1, ls='--', fill=False, zorder=3)
            else:
                pp = mpatches.Circle(center,radius=radius, ec='black', lw=1, fill=False, zorder=3)
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
            pp = mpatches.Arc(center, width=width, height=height, angle=0, theta1=theta1, theta2=theta2, ec='black', lw=1, zorder=3)
    else:
        if fill:
            if dash:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, fc=random.choice(colors), ec='black', lw=1, ls='--', fill=True, zorder=3, alpha=alpha)
            else:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, fc=random.choice(colors), ec='black', lw=1, fill=True, zorder=3, alpha=alpha)
        else:
            if dash:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, ec='black', lw=1, ls='--', fill=False, zorder=3)
            else:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, ec='black', lw=1, fill=False, zorder=3)

    ax.add_patch(pp)

# 문자
def drawText(ax,text='',xy=(0,0),position='top'):
    if len(xy) > 2: raise Exception("too many inputs for xy")
    l = len(str(text))
    if 'mathrm' in text: 
        l -= 10
    cp = xy
    if position == 'top':
        plt.text(cp[0]-l*3, cp[1]+1, text, fontsize=16, zorder=3)
    elif position == 'bottom':
        plt.text(cp[0]-l*3, cp[1]-12, text, fontsize=16, zorder=3)
    elif position == 'left':
        plt.text(cp[0]-5-l*4, cp[1]-2, text, fontsize=16, zorder=3)
    elif position == 'right':
        plt.text(cp[0]+l, cp[1]-2, text, fontsize=16, zorder=3)
    elif position == 'top_r':
        plt.text(cp[0]+l*0.3, cp[1]+5, text, fontsize=16, zorder=3)
    elif position == 'top_l':
        plt.text(cp[0]-1-l*5, cp[1]+5, text, fontsize=16, zorder=3)
    elif position == 'bottom_r':
        plt.text(cp[0]-l, cp[1]-12, text, fontsize=16, zorder=3)
    elif position == 'bottom_l':
        plt.text(cp[0], cp[1]-12, text, fontsize=16, zorder=3)
    else: raise Exception('no matching position')

# 선분의 길이를 표시하는 bezier 곡선을 그리는 함수
def drawPolygonArc(ax,verts=list,show_length=[],show_text=[],length_ratio=10,unit='cm',alpha=1):
    def c_distance(p1=tuple, p2=tuple):
        import math
        d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
        return d
    def find_text_position_polygonArc(p_list,l):
        def new_p_middle(p1=tuple,p2=tuple):
            return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
        def new_p_center(p_list=[]):
            #calculate center point
            x_center = 0
            y_center = 0
            for p in p_list:
                x_center += p[0]
                y_center += p[1]
            x_center /= len(p_list)
            y_center /= len(p_list)
            return (x_center,y_center)
        if len(l) != 2: raise Exception("Length of line is more/less than 2")
        center = new_p_center(p_list)
        x_center = center[0]
        y_center = center[1]
        p = new_p_middle(l[0],l[1])
        x1,y1 = l[0]
        x2,y2 = l[1]
        x1,y1,x2,y2 = round(x1,5),round(y1,5),round(x2,5),round(y2,5)
        x = p[0]
        y = p[1]
        dx = abs(x-x_center)
        dy = abs(y-y_center)
        #exceptional case
        if x1 == x2:
            if x > x_center:
                position = 'right'
            elif x < x_center:
                position = 'left'
        elif y1 == y2:
            if y > y_center:
                position = 'top'
            elif y < y_center:
                position = 'bottom'
        #normal case
        elif dx >= dy: #right/left - x
            if x >= x_center: #right
                position = 'right'
                if y >= y_center: #top
                    position += '_t'
                else: #bottom
                    position += '_b'
            else: #left
                position = 'left'
                if y >= y_center: #top
                    position += '_t'
                else: #bottom
                    position += '_b'
        else: #top/bottom - y
            if y >= y_center: #top
                position = 'top'
                if x >= x_center: #right
                    position += '_r'
                else: #left
                    position += '_l'
            else: #bottom
                position = 'bottom'
                if x >= x_center: #right
                    position += '_r'
                else: #left
                    position += '_l'
        return position
    #handle exception
    if len(verts) != len(show_length) and show_length != []: raise Exception("size of verts and size of show_arc don't match")
    if len(verts) != len(show_text) and show_text != []: raise Exception("size of verts and size of show_text don't match")
    #draw arc
    for i in range(len(verts)):
        if i == len(verts)-1:
            p1 = verts[i]
            p2 = verts[0]
        else:
            p1 = verts[i]
            p2 = verts[i+1]
        if show_length != []:
            if show_length[i] == True:
                length = int(c_distance(p1,p2)/length_ratio)
                position = find_text_position_polygonArc(verts,[p1,p2])
                drawArc(ax,[p1,p2],position,'$%s \\mathrm{%s}$'%(length,unit))
        if show_text != []: 
            if show_text[i] != '':
                position = find_text_position_polygonArc(verts,[p1,p2])
                drawArc(ax,[p1,p2],position,show_text[i])
def drawArc(ax, p_list, position, text, boxed=False,color='black'):
    if len(p_list) != 2: raise Exception('p_list has more or less than 2 elements')
    p1 = p_list[0]
    p2 = p_list[1]
    if 'top' in position: cp = find_controlPoint_arc(p1,p2,'top')
    elif 'bottom' in position: cp = find_controlPoint_arc(p1,p2,'bottom')
    elif 'right' in position: cp = find_controlPoint_arc(p1,p2,'right')
    elif 'left' in position: cp = find_controlPoint_arc(p1,p2,'left')
    p1 = (round(p1[0],5),round(p1[1],5))
    p2 = (round(p2[0],5),round(p2[1],5))
    l = len(text)
    if 'mathrm' in text: 
        l -= 12
    vert = [
        p1,
        cp, # 제어점
        p2
    ]
    codes = [
        Path.MOVETO,
        Path.CURVE3,
        Path.CURVE3,
    ]

    path = Path(vert,codes)
    pp = mpatches.PathPatch(path, fc="none", transform=ax.transData, linestyle="--", zorder=3, color=color)
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
        elif position == 'top_r' or position == 'right_t':
            plt.text(cp[0]+l*0.3, cp[1]+2, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'top_l' or position == 'left_t':
            plt.text(cp[0]+1-l*5, cp[1]+2, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_r' or position == 'right_b':
            plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_l' or position == 'left_b':
            plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5, text, fontsize=16, zorder=3, bbox=dict(ec='black', fc='white'))
    else:
        if position == 'top':
            plt.text(cp[0]-3*l, cp[1]+1, text, fontsize=16, zorder=3)
        elif position == 'bottom':
            plt.text(cp[0]-3*l, cp[1]-5, text, fontsize=16, zorder=3)
        elif position == 'left':
            plt.text(cp[0]-l*8, cp[1]-2, text, fontsize=16, zorder=3)
        elif position == 'right':
            plt.text(cp[0], cp[1]-2, text, fontsize=16, zorder=3)
        elif position in ['top_r','right_t']:
            plt.text(cp[0]+l*0.6, cp[1]+2, text, fontsize=16, zorder=3)
        elif position in ['top_l','left_t']:
            plt.text(cp[0]-l*9, cp[1]+2, text, fontsize=16, zorder=3)
        elif position in ['bottom_r','right_b']:
            plt.text(cp[0]+l, cp[1]-8+l*0.5, text, fontsize=16, zorder=3)
        elif position in ['bottom_l','left_b']:
            plt.text(cp[0]-l*8, cp[1]-8+l*0.5, text, fontsize=16, zorder=3)
        else: raise Exception('no matching position')


# 직선 화살표 그리는 함수(dy==0)
def drawArrow(ax,start_p=tuple,end_p=tuple,colors=False):
    from math import sqrt
    h = 1
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
    if 'mathrm' in text: 
        l -= 10*7
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




# 모든 대각선을 그리는 함수
def draw_all_diagonal(ax,polygon=list,color='blue'):
    for i in range(len(polygon)):
        p1 = polygon[i]
        for j in range(len(polygon)):
            p2 = polygon[j]
            if j != i and j != i+1 and j != i-1:
                line_1 = matplotlib.lines.Line2D((p1[0],p2[0]), (p1[1],p2[1]), linewidth=1, linestyle = '-',color=color)
                ax.add_line(line_1)

# 정다각형 그리는 함수
def drawRegular(ax, center, n, radius, fill=False, alpha=1, dash=False):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    if fill:
        if dash:
            pp = mpatches.RegularPolygon(xy=center, fc=random.choice(colors), fill=True, lw=1, ls='--', zorder=3, alpha=alpha)
        else:
            pp = mpatches.RegularPolygon(xy=center, fc=random.choice(colors), fill=True, lw=1, zorder=3, alpha=alpha)
    else:
        if dash:
            pp = mpatches.RegularPolygon(xy=center, ec='black', fill=False, lw=1, ls='--', zorder=3)
        else:
            pp = mpatches.RegularPolygon(xy=center, ec='black', fill=False, lw=1, zorder=3,numVertices=n)

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

    if abs(p2[0]-p1[0]) < 1:
        if type == 'left' or type == 'top':
            cp = (mp[0]-0.2*d,mp[1])
        else:
            cp = (mp[0]+0.2*d,mp[1])

    elif abs(p2[1]-p1[1]) < 1:
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
def find_controlPoint_arc(p1,p2,position='top',distance=10):
    def round_p(p,roundNumber=5):
        p = (round(p[0],roundNumber),round(p[1],roundNumber))
        return p
    def find_linear_equation(p1,p2):
        x1,y1 = p1
        x2,y2 = p2
        if x1 == x2:
            return ('x',x1)
        if y1 == y2:
            return ('y',y1)
        slope = (y2-y1)/(x2-x1)
        y_intersect = y1 - slope*x1
        return (slope,y_intersect)
    def find_p_middle(p1=tuple,p2=tuple):
        return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
    def find_p_onLineInCertainDistance(equation,middle_point,distance):
        middle_x,middle_y = middle_point
        slope,y_intersect = equation
        new_x_positive = middle_x + math.sqrt(distance**2/((1/slope)**2+1))
        new_y_positive = -1/slope*new_x_positive + 1/slope*middle_x + middle_y
        new_x_negative = middle_x - math.sqrt(distance**2/((1/slope)**2+1))
        new_y_negative = -1/slope*new_x_negative + (1/slope)*middle_x + middle_y
        return (new_x_positive, new_y_positive),(new_x_negative, new_y_negative)
    def calculate_distance(p1=tuple, p2=tuple):
        import math
        d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

        return d
    p1,p2 = round_p(p1),round_p(p2)
    equation = find_linear_equation(p1,p2)
    slope, y_intersect = equation
    x1,y1 = p1
    x2,y2 = p2
    d = calculate_distance(p1,p2)
    if slope == 'x':
        cp_y = (y1+y2)/2
        if position == 'right':
            cp_x = y_intersect + distance
        elif position == 'left':
            cp_x = y_intersect - distance
        else: raise Exception('Invalid Position')
    elif slope == 'y':
        cp_x = (x1+x2)/2
        if position == 'top':
            cp_y = y_intersect + distance
        elif position == 'bottom':
            cp_y = y_intersect - distance
        else: raise Exception('Invalid Position')
    else:
        p_middle = find_p_middle(p1,p2)
        cp_positive, cp_negative = find_p_onLineInCertainDistance(equation,p_middle,distance)
        if slope > 0:
            if position in ['top','left']:#negative
                cp_x,cp_y = cp_negative
            elif position in ['bottom','right']:#positive
                cp_x,cp_y = cp_positive
            else: raise Exception('Invalid Position')
        elif slope < 0:
            if position in ['top','right']:#positive
                cp_x,cp_y = cp_positive
            elif position in ['bottom','left']:#negative
                cp_x,cp_y = cp_negative
            else: raise Exception('Invalid Position')
        else: raise Exception('Slope is 0')
    return (cp_x,cp_y)

def calculate_distance(p1, p2):
    d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    return d


def line_equation(p1, p2, x):
    y = ((p2[1]-p1[1])/(p2[0]-p1[0])) * (x-p1[0]) + p1[1]

    return y

#plt.rcParams['text.usetex'] = True
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf8')
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf8')


def resize_multiple(p_list_multiple=list,scale=90):
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
    #move all to center / find the ratio
    sum_criteria_val = 0
    criteria_list = []
    for i in range(len(p_list_multiple)):
        p_list = p_list_multiple[i]
        p_list = move_to_center(p_list)
        #find the criteria point
        criteria_val = abs(p_list[0][0])*2
        for p in p_list:
            x = p[0]
            y = p[1]
            #compare
            if max(abs(x),abs(y)) > criteria_val:
                criteria_val = max(abs(x),abs(y))
        criteria_val *= 2
        sum_criteria_val += criteria_val
        criteria_list.append(criteria_val)
    #find ratio
    ratio = (scale*2)/sum_criteria_val

    #scale up/down with calculated ratio
    new_p_list_multiple = []
    for i in range(len(p_list_multiple)):
        p_list = p_list_multiple[i]
        #create new_p_num
        new_p_num = []
        for p in p_list:
            x_new = p[0] * ratio
            y_new = p[1] * ratio
            new_p_num.append((x_new,y_new))
        new_p_num = move_to_center(new_p_num)
        x_move = -100 + (scale*2/len(p_list_multiple))/2 + (int(scale*2 / len(p_list_multiple))*i)
        new_p_num = move_p(new_p_num,x_move)

        new_p_list_multiple.append(new_p_num)
    
    return new_p_list_multiple
def resize_polygon_multiple(p_list_multiple=list):
    def resize_polygon(p_list=list,scale=90):
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
        #move to center
        p_list = move_to_center(p_list)
        #find the criteria point
        criteria_val = abs(p_list[0][0])

        for p in p_list:
            x = p[0]
            y = p[1]
            #compare
            if max(abs(x),abs(y)) > criteria_val:
                criteria_val = max(abs(x),abs(y))
        #find ratio
        ratio = scale/criteria_val
        #create new_p_num
        new_p_num = []

        for p in p_list:
            x_new = p[0] * ratio
            y_new = p[1] * ratio
            new_p_num.append((x_new,y_new))
        new_p_num = move_to_center(new_p_num)
        p_list = new_p_num
        return new_p_num
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
    p_all = []
    for i in range(len(p_list_multiple)):
        p_all += p_list_multiple[i]
    p_all = move_to_center(p_all)
    p_all = resize_polygon(p_all)
    for i in range(len(p_list_multiple)):
        p_list_multiple[i] = p_all[:len(p_list_multiple[i])]
        p_all = p_all[len(p_list_multiple[i]):]
    return p_list_multiple
def resize(p_list=list,scale=90):
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
    #move to center
    p_list = move_to_center(p_list)
    #find the criteria point
    criteria_val = abs(p_list[0][0])

    for p in p_list:
        x = p[0]
        y = p[1]
        #compare
        if max(abs(x),abs(y)) > criteria_val:
            criteria_val = max(abs(x),abs(y))
    #find ratio
    ratio = scale/criteria_val
    #create new_p_num
    new_p_num = []

    for p in p_list:
        x_new = p[0] * ratio
        y_new = p[1] * ratio
        new_p_num.append((x_new,y_new))
    new_p_num = move_to_center(new_p_num)
    return new_p_num
def flip_p(p_list=list,axis='x'):
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
    #handle exception
    if axis not in ['x','y','xy']: raise Exception("wrong input for axis parameter")
    p1_original = p_list[0]
    #move_to_center for affective flip
    p_list = move_to_center(p_list)
    dx = p_list[0][0] - p1_original[0]
    dy = p_list[0][1] - p1_original[1]
    #flip
    for i in range(len(p_list)):
        x = p_list[i][0]
        y = p_list[i][1]
        if axis == 'x': #X-axis
            x *= -1
        elif axis == 'y': # Y-axis
            y *= -1
        else: # X-axis and Y-axis
            x *= -1
            y *= -1
        p_list[i] = (x,y)
    #move_back
    for i in range(len(p_list)):
        x = p_list[i][0] + dx
        y = p_list[i][1] + dy
        p_list[i] = (x,y)
    #switch the location of point
    if axis in ['x','y']:
        p_list = [p_list[0],p_list[2],p_list[1]]
    return p_list
def move_p(p_list=list,x_move=0,y_move=0):
    #center point
    new_p_list = []
    for index in range(len(p_list)):
        p = p_list[index]
        new_p_list.append((p[0]+x_move,p[1]+y_move))
    return new_p_list
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

def new_p_triangle(width_height=[],right_bottom_left=[],bottom_left_angle=[],move_x=0,move_y=0):
    import math
    def move_p(p_list=list,x_move=0,y_move=0):
        #center point
        new_p_list = []
        for index in range(len(p_list)):
            p = p_list[index]
            new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
    def new_p_angle(angle,length,p=[0,0]):
        import math
        angle_radiant = math.radians(angle)
        x = round((math.cos(angle_radiant)*length),5) + p[0]
        y = round((math.sin(angle_radiant)*length),5) + p[1]
        return (x,y)
    scale = 100
    #points - p_top,p_right,p_center
    p_center = (0,0)
    if width_height != []:
        if len(width_height) != 2: raise Exception("Input is incomplete")
        len_width = width_height[0]
        len_height = width_height[1]
        angle = math.degrees(math.atan(len_height/len_width))
        len_left = abs(len_height/math.cos(math.radians(180-angle)))
        p_right = (len_width,0)
        p_top = new_p_angle(angle,len_left,p_center)
    elif right_bottom_left != []:
        if len(right_bottom_left) != 3: raise Exception("Input is incomplete")
        len_right = right_bottom_left[0]
        len_bottom = right_bottom_left[1]
        len_left = right_bottom_left[2]
        if len_right > len_bottom+len_left or len_bottom > len_right+len_left or len_left > len_right+len_bottom:
            raise Exception("Lengths of triangle are against the triangle inequality theorem, which means sum of two lengths is smaller than the other length")
        angle = math.degrees(math.acos((len_bottom**2+len_left**2-len_right**2)/(2*len_bottom*len_left)))
        p_right = (len_bottom,0)
        p_top = new_p_angle(angle,len_left,p_center)
    elif bottom_left_angle != []:
        if len(bottom_left_angle) != 3: raise Exception("Input is incomplete")
        len_bottom = bottom_left_angle[0]
        len_left = bottom_left_angle[1]
        angle = bottom_left_angle[2]
        p_right = (len_bottom,0)
        p_top = new_p_angle(angle,len_left,p_center)
    else: raise Exception("No input to make points for triangle")


    triangle = [p_top,p_right,p_center]
    triangle = move_p(triangle,move_x,move_y)
    return triangle
def create_p_regular(n=3,scale=100,move_x=0,move_y=0):
    import random
    def new_p_angle(angle,length,p=[0,0]):
        angle_radiant = math.radians(angle)
        x = (math.cos(angle_radiant)*length) + p[0]
        y = (math.sin(angle_radiant)*length) + p[1]
        return (x,y)
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
    temp_p = (0,0)
    angle = 180 * (n-2) / n
    length = int(scale/2)
    polygon = [(0,0)]
    for i in range(n-1):
        temp_p = new_p_angle(angle,length,temp_p)
        polygon.append(temp_p)
        polygon = rotate_p(polygon,180-angle)
        temp_p = (rotate_p([temp_p],180-angle))[0]

    polygon = move_to_center(polygon)
    polygon = move_p(polygon,move_x,move_y)
    return polygon
def create_p_triangle(width_height=[],right_bottom_left=[],bottom_left_angle=[],move_x=0,move_y=0):
    import random
    import math
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
    def new_p_angle(angle,length,p=[0,0]):
        import math
        angle_radiant = math.radians(angle)
        x = round((math.cos(angle_radiant)*length),5) + p[0]
        y = round((math.sin(angle_radiant)*length),5) + p[1]
        return (x,y)
    scale = 100
    #points - p_top,p_right,p_center
    p_center = (0,0)
    if width_height != []:
        if len(width_height) != 2: raise Exception("Input is incomplete")
        len_width = width_height[0]
        len_height = width_height[1]
        angle = math.degrees(math.atan(len_height/len_width))
        len_left = abs(len_height/math.cos(math.radians(180-angle)))
        p_right = (len_width,0)
        p_top = new_p_angle(angle,len_left,p_center)
    elif right_bottom_left != []:
        if len(right_bottom_left) != 3: raise Exception("Input is incomplete")
        len_right = right_bottom_left[0]
        len_bottom = right_bottom_left[1]
        len_left = right_bottom_left[2]
        if len_right > len_bottom+len_left or len_bottom > len_right+len_left or len_left > len_right+len_bottom:
            raise Exception("Lengths of triangle are against the triangle inequality theorem, which means sum of two lengths is smaller than the other length")
        angle = math.degrees(math.acos((len_bottom**2+len_left**2-len_right**2)/(2*len_bottom*len_left)))
        p_right = (len_bottom,0)
        p_top = new_p_angle(angle,len_left,p_center)
    elif bottom_left_angle != []:
        if len(bottom_left_angle) != 3: raise Exception("Input is incomplete")
        len_bottom = bottom_left_angle[0]
        len_left = bottom_left_angle[1]
        angle = bottom_left_angle[2]
        p_right = (len_bottom,0)
        p_top = new_p_angle(angle,len_left,p_center)
    else: raise Exception("No input to make points for triangle")


    triangle = [p_top,p_right,p_center]
    triangle = move_p(triangle,move_x,move_y)
    return triangle
def create_p_rectangle(width,height,move_x=0,move_y=0):
    import random
    def new_p_angle(angle,length,p=[0,0]):
        angle_radiant = math.radians(angle)
        x = (math.cos(angle_radiant)*length) + p[0]
        y = (math.sin(angle_radiant)*length) + p[1]
        return (x,y)
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
    temp_p = (0,0)
    angle = 90
    n = 4
    polygon = [(0,0)]
    for i in range(n-1):
        if (i%2) == 0: #width
            temp_p = new_p_angle(angle,width,temp_p)
        else: #height
            temp_p = new_p_angle(angle,height,temp_p)
        polygon.append(temp_p)
        polygon = rotate_p(polygon,180-angle)
        temp_p = (rotate_p([temp_p],180-angle))[0]
        
    #polygon.reverse()
    polygon = move_to_center(polygon)
    polygon = move_p(polygon,move_x,move_y)
    return polygon
def create_p_trapezoid(length_top,length_bottom,height,move_x=0,move_y=0):
    import random
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
    p_top_l = (length_top/2*-1,height)
    p_top_r = (length_top/2,height)
    p_bottom_r = (length_bottom/2,0)
    p_bottom_l = (length_bottom/2*-1,0)
    trapezoid = [p_top_l,p_top_r,p_bottom_r,p_bottom_l]
    trapezoid = move_p(trapezoid,move_x,move_y)
    return trapezoid
def create_p_rhombus(width,height,move_x=0,move_y=0):
    def move_p(p_list=list,x_move=0,y_move=0):
        #center point
        new_p_list = []
        for index in range(len(p_list)):
            p = p_list[index]
            new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
    #points
    p_left = (width/2*-1,0)
    p_right = (width/2,0)
    p_top = (0,height/2)
    p_bottom = (0,height/2*-1)
    rhombus = [p_top,p_right,p_bottom,p_left]
    rhombus = move_p(rhombus,move_x,move_y)
    return rhombus
def create_p_parallelogram(left_angle=0,width=0,length=0,move_x=0,move_y=0):
    import random
    import math
    def new_p_angle(angle,length,p=[0,0]):
        angle_radiant = math.radians(angle)
        x = (math.cos(angle_radiant)*length) + p[0]
        y = (math.sin(angle_radiant)*length) + p[1]
        return (x,y)
    def move_p(p_list=list,x_move=0,y_move=0):
        #center point
        new_p_list = []
        for index in range(len(p_list)):
            p = p_list[index]
            new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
    #left_angle,right_angle
    if left_angle == 0:
        a_num_left_5 = random.randint(10,28)
        while 16 <= a_num_left_5 and a_num_left_5 <= 20:
            a_num_left_5 = random.randint(10,28)
        left_angle = a_num_left_5*5
    #lengh1,length2
    if width == 0 or length == 0:
        width = random.randint(3,9)
        length = random.randint(5,9)
    #points
    p_bottom_l = (0,0)
    p_bottom_r = (length,0)
    p_top_l = new_p_angle(left_angle,width)
    p_top_r = new_p_angle(left_angle,width,p_bottom_r)

    parallelogram = [p_top_l,p_top_r,p_bottom_r,p_bottom_l]
    parallelogram = move_p(parallelogram,move_x,move_y)
    return parallelogram

def find_p_middle(p1=tuple,p2=tuple):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
def find_p_center(p_list=[]):
    #calculate center point
    x_center = 0
    y_center = 0
    for p in p_list:
        x_center += p[0]
        y_center += p[1]
    x_center /= len(p_list)
    y_center /= len(p_list)
    return (x_center,y_center)
def calculate_angle(p_list=[]):
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
    angle = int(angle)
    angle = angle - (angle%5)
    return angle

def is_triangle(l1,l2,l3):
    if l1 >= l2 and l1 >= l3:#l1
        if l1 < l2+l3:
            return True
    elif l2 >= l3 and l2 >= l1:#l2
        if l2 < l1+l3:
            return True
    elif l3 >= l1 and l3 >= l2:#l3
        if l3 < l1+l2:
            return True
    return False

#5-2-3-11,12
def conandsym523_Stem_001():
    def c_distance(p1=tuple, p2=tuple):
        import math
        d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
        return d
    def new_p_triangle(width=10,height=10,angle=0,move_x=0,move_y=0):
        import random
        import math
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
        def new_p_angle(angle,length,p=[0,0]):
            import math
            angle_radiant = math.radians(angle)
            x = round((math.cos(angle_radiant)*length),5) + p[0]
            y = round((math.sin(angle_radiant)*length),5) + p[1]
            return (x,y)
        scale = 100
        #points
        p_center = (0,0)
        if angle == 0:
            angle = math.degrees(math.atan(height/width))
        length = abs(height/math.cos(math.radians(180-angle)))
        if angle == 90:
            p_top = (0,height)
        else:
            p_top = new_p_angle(angle,length,p_center)
        p_right = (width,0)
        # num_angle = c_angle([angle_p1,angle_center,angle_p2])
        # while num_angle > 150 or num_angle < 10:
        #     angle_center = new_p()
        #     angle_p1 = new_p([angle_center],scale,scale)
        #     angle_p2 = new_p([angle_center],scale,scale+random.randint(-30,-1))
        #     num_angle = c_angle([angle_p1,angle_center,angle_p2])
        p_top = (p_top[0],p_top[1])
        triangle = [p_top,p_right,p_center]
        triangle = move_to_center(triangle)
        triangle = move_p(triangle,move_x,move_y)
        return triangle
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
    while True:
        len_bottom = random.randint(8,13)
        len_left = random.randint(5,15)
        len_right = random.randint(5,15)
        areDifferent = abs(len_left-len_right) > 2 and abs(len_bottom-len_left) > 2 and abs(len_bottom-len_right) > 2
        if is_triangle(len_bottom,len_right,len_left) and areDifferent:
            break
    #perimeter = len_bottom + len_left + len_right
    angle = math.degrees(math.atan2(len_left,len_bottom))
    #generate polygon
    triangle1 = new_p_triangle(len_bottom,len_left,angle=angle,move_x=-len_bottom*3/4)
    triangle2 = new_p_triangle(len_bottom,len_left,angle=angle,move_x=len_bottom*3/4)

    len_bottom = int(c_distance(triangle1[1], triangle1[2]))
    len_left = int(c_distance(triangle1[0], triangle1[2]))
    len_right = int(c_distance(triangle1[0], triangle1[1]))
    perimeter = len_bottom + len_left + len_right

    triangle1,triangle2 = resize_polygon_multiple([triangle1,triangle2])
    #draw
    drawPolygon(ax,triangle1)
    drawPolygon(ax,triangle2)
    setPoint(ax,triangle1,['A','B','C'],['top','bottom','bottom'])
    setPoint(ax,triangle2,['D','E','F'],['top','bottom','bottom'])
    random_prob = random.randint(0,2)
    show_text1 = ['','','']
    show_text2 = ['$%s\mathrm{cm}$'%len_right,'$%s\mathrm{cm}$'%len_bottom,'$%s\mathrm{cm}$'%len_left]
    show_text1[random_prob] = show_text2[random_prob]
    show_text2[random_prob] = ''
    drawPolygonArc(ax,triangle1,show_text=show_text1)
    drawPolygonArc(ax,triangle2,show_text=show_text2)
    #stem
    stem = "두 삼각형은 서로 합동입니다. 삼각형$$수식$$DEF$$/수식$$의 둘레는 몇 $$수식$$rm cm$$/수식$$인가요?"
    if random_prob == 0: #right
        comment = "(해설) (변$$수식$$AB$$/수식$$) $$수식$$=$$/수식$$ (변$$수식$$DE$$/수식$$) $$수식$$= %srm cm$$/수식$$\n" %len_right
    elif random_prob == 1: #bottom
        comment = "(해설) (변$$수식$$BC$$/수식$$) $$수식$$=$$/수식$$ (변$$수식$$EF$$/수식$$) $$수식$$= %srm cm$$/수식$$\n" %len_bottom
    elif random_prob == 2: #left
        comment = "(해설) (변$$수식$$AC$$/수식$$) $$수식$$=$$/수식$$ (변$$수식$$DF$$/수식$$) $$수식$$= %srm cm$$/수식$$\n" %len_left
    comment += " $$수식$$ \\Rightarrow$$/수식$$ (삼각형$$수식$$DEF$$/수식$$의 둘레)\n"
    comment += " $$수식$$= %s + %s + %s = %s(rm cm)$$/수식$$" %(len_left,len_right,len_bottom,perimeter)
    answer = '(답): $$수식$$%srm cm$$/수식$$'%perimeter
    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg

#5-2-3-13
def conandsym523_Stem_002():
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
    p_list = ['A','B','C','D','E','F']
    l_left_list = ['AB','BC','AC']
    l_right_list = ['DE','EF','DF']
    while True:
        len_left = random.randint(5,10)
        len_right = random.randint(5,10)
        len_bottom = random.randint(5,10)
        areNotSameLengths = len_left != len_right and len_left != len_bottom and len_right != len_bottom
        if is_triangle(len_left,len_right,len_bottom) and areNotSameLengths:
            break
    perimeter = len_left + len_right + len_bottom
    len_list = [len_right,len_bottom,len_left]
    #generate shapes
    triangle_left = new_p_triangle(right_bottom_left=[len_right,len_bottom,len_left],move_x=-30)
    triangle_left = resize(triangle_left,15)
    triangle_left = rotate_p(triangle_left,60)
    triangle_right = flip_p(triangle_left)
    triangle_right = [
        triangle_right[0],triangle_right[2],triangle_right[1]
    ]
    triangle_right = move_p(triangle_right,30)
    triangle_left,triangle_right = resize_polygon_multiple([triangle_left,triangle_right])
    while True:
        index_left = random.randint(0,2)
        index_right = random.randint(0,2)
        if index_left != index_right:
            break
    show_len = [
        '$%s\mathrm{cm}$'%(len_right),
        '$%s\mathrm{cm}$'%(len_bottom),
        '$%s\mathrm{cm}$'%(len_left)
    ]
    show_left = show_len.copy()
    show_right = show_len.copy()
    for i in range(len(show_len)):
        if i != index_left:
            show_left[i] = ''
        if i != index_right:
            show_right[i] = ''
        if i != index_left and i != index_right:
            index_answer = i
    #draw shapes
    drawPolygon(ax,triangle_left)
    drawPolygon(ax,triangle_right)
    drawPolygonArc(ax,triangle_right,show_text=show_right)
    drawPolygonArc(ax,triangle_left,show_text=show_left)
    setPoint(ax,triangle_left,p_list[:3],['top','top','bottom'])
    setPoint(ax,triangle_right,p_list[3:6],['top','top','bottom'])

    stem = "두 삼각형은 서로 합동입니다. 삼각형$$수식$$ABC$$/수식$$의 둘레가 $$수식$$%srm cm$$/수식$$일 때, 변$$수식$$%s$$/수식$$는 몇 $$수식$$rm cm$$/수식$$인가요?"%(
                perimeter,l_left_list[index_answer]
            )
    answer = "(답):$$수식$$%srm cm$$/수식$$"%(len_list[index_answer])
    comment = "(해설)\n(변$$수식$$%s$$/수식$$) $$수식$$=$$/수식$$ (변$$수식$$%s$$/수식$$) $$수식$$= %srm cm$$/수식$$\n"\
                " → (변$$수식$$%s$$/수식$$) $$수식$$= %s - (%s + %s) = %s(rm cm)$$/수식$$"%(
                    l_left_list[index_right],l_right_list[index_right],len_list[index_right],
                    l_left_list[index_answer],perimeter,len_list[index_left],len_list[index_right],len_list[index_answer]
            )
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem,answer,comment, svg

#5-2-3-14
def conandsym523_Stem_003():
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
    while True:
        width = random.randint(10,20)
        height = random.randint(10,20)
        if abs(width-height) > 5:
            break
    area = width*height
    p_list = ['A','B','C','D','E','F','G','H']
    l_left_list = ['AB','BC','CD','AD']
    l_right_list = ['EF','FG','GH','EH']
    len_list = [width,height,width,height]
    len_arc_list = [
        '$%s\mathrm{cm}$'%(len_list[0]),
        '$%s\mathrm{cm}$'%(len_list[1]),
        '$%s\mathrm{cm}$'%(len_list[2]),
        '$%s\mathrm{cm}$'%(len_list[3])
    ]
    invalid_index_list = [(1,0),(0,2),(1,3),(2,0),(3,1)]
    while True:
        index_right = random.randint(0,3)
        index_left = random.randint(0,3)
        if index_right != index_left and (index_left,index_right) not in invalid_index_list:
            break
    show_left = len_arc_list.copy()
    show_right = len_arc_list.copy()
    for i in range(len(len_arc_list)):
        if i != index_left:
            show_left[i] = ''
        if i != index_right:
            show_right[i] = ''
    #generate shapes
    rectangle = create_p_rectangle(width,height)
    rectangle_left = move_p(rectangle,-1)
    rectangle_right = rotate_p(rectangle,90)
    rectangle_right = move_p(rectangle_right,1)
    rectangle_left,rectangle_right = resize_multiple([rectangle_left,rectangle_right])
    #draw shapes
    drawPolygon_multiple(ax,[rectangle_left,rectangle_right])
    setPoint(ax,rectangle_left,p_list[:4],['top','top','bottom','bottom'])
    setPoint(ax,rectangle_right,p_list[4:],['bottom','top','top','bottom'])
    drawPolygonArc(ax,rectangle_left,show_text=show_left)
    drawPolygonArc(ax,rectangle_right,show_text=show_right)
    #stem/answer/comment
    stem = "두 직사각형은 서로 합동입니다. 직사각형$$수식$$ABCD$$/수식$$의 넓이는 몇 $$수식$$rm cm^{2}$$/수식$$인가요?"
    answer = '(답):$$수식$$%srm cm^{2}$$/수식$$'%(area)
    comment = "(해설)\n대응변의 길이가 서로 같으므로\n"\
                "(변$$수식$$%s$$/수식$$) $$수식$$=$$/수식$$ (변$$수식$$%s$$/수식$$) $$수식$$= %srm cm$$/수식$$\n"\
                "(직사각형$$수식$$ABCD$$/수식$$의 넓이) $$수식$$= %s times %s = %s(rm cm^{2})$$/수식$$\n"\
                ""%(
                    l_left_list[index_right], l_right_list[index_right], len_list[index_right],
                    width, height, area
                )
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem,answer,comment, svg

#5-2-3-17
def conandsym523_Stem_004():
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
    len_bottom = random.randint(5,8)
    len_left = random.randint(3,5)
    len_right = len_bottom + len_left - random.randint(1,2)
    len_perimeter = len_bottom + len_left + len_right
    angle = math.degrees(math.atan(len_left/len_bottom))
    #generate polygon
    triangle1 = new_p_triangle(right_bottom_left=[len_right,len_bottom,len_left])
    triangle1 = resize(triangle1)
    triangle2 = flip_p(triangle1)
    triangle = resize_multiple([triangle1+triangle2])
    triangle1 = triangle[0][0:3]
    triangle2 = triangle[0][3:6]
    #point
    p1_top = triangle1[0]
    p1_right = triangle1[1]
    p1_left = triangle1[2]
    p2_top = triangle2[0]
    p2_right = triangle2[1]
    p2_left = triangle2[2]
    #draw
    dx = abs(p1_right[0] - p2_right[0])
    triangle2 = move_p(triangle2,dx)
    #point reset after movement
    p2_top = triangle2[0]
    p2_right = triangle2[1]
    p2_left = triangle2[2]
    drawPolygon(ax,triangle1)
    drawPolygon(ax,triangle2)
    setPoint(ax,triangle1,['A','C','B'],['top','bottom','bottom'])
    setPoint(ax,triangle2,['D','',''],['top','bottom','bottom'])
    random_prob = random.randint(0,1)
    if random_prob == 0: # 1-> (1_left,len_left), 2->(2_left,len_right), answer->(bottom)
        line_stem1 = [p1_left,p1_top]
        line_stem2 = [p2_left,p2_top]
        len_line_stem1 = len_left
        len_line_stem2 = len_right
        line_name_stem2 = ['AC','BD']
        show_text = ['$%s\mathrm{cm}$'%(len_line_stem1),'$%s\mathrm{cm}$'%(len_line_stem2)]
        line_answer = [p1_top,p1_right]
        len_answer = len_bottom
        line_name_answer = 'BC'
        drawArc(ax,line_stem1,'left',show_text[0])
        drawArc(ax,line_stem2,'left',show_text[1])
    elif random_prob == 1: # 1-> (1_right,len_right), 2->(2_right,len_left), answer->(bottom)
        line_stem1 = [p1_top,p1_right]
        line_stem2 = [p2_top,p2_right]
        len_line_stem1 = len_right
        len_line_stem2 = len_left
        line_name_stem2 = ['AB','CD']
        show_text = ['$%s\mathrm{cm}$'%(len_line_stem1),'$%s\mathrm{cm}$'%(len_line_stem2)]
        line_answer = [p1_top,p1_right]
        len_answer = len_bottom
        line_name_answer = 'BC'
        drawArc(ax,line_stem1,'right',show_text[0])
        drawArc(ax,line_stem2,'right',show_text[1])

    stem = "삼각형$$수식$$ABC$$/수식$$와 $$수식$$DCB$$/수식$$는 서로 합동입니다. 삼각형$$수식$$ABC$$/수식$$의 둘레가 $$수식$$%srm cm$$/수식$$ 일 때, 변$$수식$$%s$$/수식$$의 "\
            "길이는 몇 $$수식$$rm cm$$/수식$$인가요?" %(len_perimeter,line_name_answer)
    comment = "(해설)\n각각의 대응변의 길이가 서로 같으므로\n"\
                "(변$$수식$$%s$$/수식$$) $$수식$$=$$/수식$$ (변$$수식$$%s$$/수식$$) $$수식$$= %srm cm$$/수식$$\n"\
                "(삼각형$$수식$$ABC$$/수식$$의 둘레)\n"\
                "$$수식$$=$$/수식$$ (변$$수식$$AB$$/수식$$) $$수식$$+$$/수식$$ (변$$수식$$BC$$/수식$$) $$수식$$+$$/수식$$ (변$$수식$$AC$$/수식$$)\n"\
                "$$수식$$= %s +$$/수식$$ (변$$수식$$%s$$/수식$$) $$수식$$+ %s  = %s(rm cm)$$/수식$$\n"\
                "(변$$수식$$%s$$/수식$$) $$수식$$= %s - (%s+%s) = %s(rm cm)$$/수식$$" %(
                    line_name_stem2[0],line_name_stem2[1],len_line_stem2,
                    len_line_stem1,line_name_answer,len_line_stem2,len_perimeter,
                    line_name_answer,len_perimeter,len_line_stem1,len_line_stem2,len_answer
                    )
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(len_bottom)
    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg

#5-2-3-23
def conandsym523_Stem_005():
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
    n = random.randint(3,5) * 2
    point_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
    #generate polygon/axis
    polygon = create_p_regular(n)
    polygon = resize(polygon)
    p_center = find_p_center(polygon)
    line_axis = [(p_center[0],105),(p_center[0],-99)]
    line_name_axis = point_list[n+1]+point_list[n+2]
    #angle for stem/answer
    first_index_stem = random.randint(0,n-1)
    second_index_stem = (first_index_stem+1)%(n)
    third_index_stem = (first_index_stem+2)%(n)
    angle_name_stem = point_list[first_index_stem]+point_list[second_index_stem]+point_list[third_index_stem]
    first_index_answer = (first_index_stem + round(n/2))%(n)
    second_index_answer = (second_index_stem + round(n/2))%(n)
    third_index_answer = (third_index_stem + round(n/2))%(n)
    angle_name_answer = point_list[first_index_answer]+point_list[second_index_answer]+point_list[third_index_answer]

    stem = "직선$$수식$$%s$$/수식$$을 대칭축으로 하는 선대칭도형입니다. 각$$수식$$%s$$/수식$$의 대응각을 써 보세요." %(
                line_name_axis,
                angle_name_stem
                )
    comment = "(해설)\n대칭축을 따라 접었을 때 각$$수식$$%s$$/수식$$과 각$$수식$$%s$$/수식$$이\n"\
                "겹칩니다. 따라서 각$$수식$$%s$$/수식$$의 대응각은 각$$수식$$%s$$/수식$$\n"\
                "입니다." %(
                    angle_name_stem,angle_name_answer,
                    angle_name_stem,angle_name_answer
                )
    answer = '(답):각$$수식$$%s$$/수식$$'%angle_name_answer
    #draw
    drawPolygon(ax,polygon)
    setPolygonPoint(ax,polygon,polygon,point_list[0:n])
    drawLine(ax,line_axis,color='red')
    setPoint(ax,line_axis,[point_list[n+1],point_list[n+2]],['top','bottom'])
    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg

#5-2-3-32,34
def conandsym523_Stem_006():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    problem_option1 = random.randint(0,1) #triangle/rectangle
    if problem_option1 == 0: #삼각형-32
        #generate variable
        len_side = random.randint(5,10)
        len_bottom = random.randint(3,6) *2
        while len_side*2 <= len_bottom:
            len_side = random.randint(5,10)
            len_bottom = random.randint(3,6) *2
        len_bottomHalf = int(len_bottom/2)
        angle_side = int(math.degrees(math.acos((len_bottom**2+len_side**2-len_side**2)/(2*len_bottom*len_side))))
        angle_side -= (angle_side%5)
        #generate polygon/line/angle
        triangle = create_p_triangle(right_bottom_left=[len_side,len_bottom,len_side])
        triangle = resize(triangle)
        #point
        p_top = triangle[0] 
        p_right = triangle[1]
        p_left = triangle[2]
        p_middle = [p_top[0],p_right[1]]
        #line
        l_axis = [p_top,p_middle]
        l_left = [p_left,p_top]
        l_right = [p_top,p_right]
        l_leftHalf = [p_left,p_middle]
        l_rightHalf = [p_middle,p_right]
        #angle
        a_middle_right = [p_right,p_middle,p_top]
        a_middle_left = [p_top,p_middle,p_left]
        a_left = [p_middle,p_left,p_top]
        a_right = [p_top,p_right,p_middle]
        #draw
        drawPolygon(ax,triangle)
        drawLine(ax,l_axis)
        setPolygonPoint(ax,triangle,[p_middle],['D'])
        drawAngle(ax,a_middle_right)
        stem = "직선$$수식$$AD$$/수식$$를 대칭축으로 하는 선대칭도형입니다. "
        problem_option2 = random.randint(0,1) # length/angle
        if problem_option2 == 0: #length
            stem += "변$$수식$$BC$$/수식$$는 몇 $$수식$$rm cm$$/수식$$인가요?"
            comment = "(해설)\n선대칭도형에서 대칭축은 대응점끼리 이은 선분을\n"\
                        "둘로 똑같이 나누므로\n"\
                        "(선분$$수식$$CD$$/수식$$) $$수식$$=$$/수식$$ (선분$$수식$$BD$$/수식$$) $$수식$$= %srm cm$$/수식$$입니다.\n"\
                        "따라서 (변$$수식$$BC$$/수식$$) $$수식$$= %s + %s = %s(rm cm)$$/수식$$입니다." %(
                            len_bottomHalf,
                            len_bottomHalf,len_bottomHalf,len_bottom
                        )
            answer = '(답):$$수식$$%srm cm$$/수식$$'%(len_bottom)
            setPoint(ax,triangle,['A','B','C',],['top','right','left'])
            problem_option3 = random.choice([l_rightHalf,l_leftHalf])
            drawArc(ax,problem_option3,'bottom','$%s\mathrm{cm}$'%(len_bottomHalf))
            drawArc(ax,l_left,'left','$%s\mathrm{cm}$'%(len_side))
        elif problem_option2 == 1: #angle
            stem += "$$수식$$B$$/수식$$에 알맞은 각도를 구해 보세요."
            comment = "(해설)\n선대칭도형에서는 각각의 대응각의 크기가 서로\n"\
                        "같고 삼각형의 세각의 크기의 합은 $$수식$$180rm °$$/수식$$ 이므로\n"\
                        "(각$$수식$$ACD$$/수식$$) $$수식$$=$$/수식$$ (각$$수식$$ABD$$/수식$$) $$수식$$= %srm °$$/수식$$\n"\
                        "따라서 $$수식$$B = %srm °$$/수식$$입니다." %(
                            angle_side,
                            angle_side
                            )
            answer = '(답):$$수식$$%srm °$$/수식$$'%(angle_side)
            drawPolygonAngle(ax,triangle,[1,1,0],[0,1,0],['A','B','C'])
        plt.axis('scaled')
        svg= saveSvg()
        svg_comment = ''
    elif problem_option1 == 1: #사다리꼴-34
        #generate variable
        len_top = random.randint(5,10)
        len_bottom = len_top + random.randint(3,7)
        len_height = len_top + random.randint(1,3)
        #generate polygon/line/angle
        trapezoid = create_p_trapezoid(len_top,len_bottom,len_height)
        trapezoid = resize(trapezoid)
        #point
        p_top_l = trapezoid[0]
        p_top_r = trapezoid[1]
        p_bottom_r = trapezoid[2]
        p_bottom_l = trapezoid[3]
        p_top_m = find_p_center([p_top_l,p_top_r])
        p_bottom_m = find_p_center([p_bottom_l,p_bottom_r])
        p_dash = (p_bottom_r[0]+20,p_bottom_r[1])
        #line
        l_dash = [p_bottom_r,p_dash]
        l_axis = [(p_top_m[0],100),(p_bottom_m[0],-100)]
        #angle
        a_stem = [p_dash,p_bottom_r,p_top_r]
        a_right_top = [p_bottom_m,p_top_m,p_top_r]
        a_right_bottom = [p_bottom_r,p_bottom_m,p_top_m]
        a_num_stem = calculate_angle(a_stem)
        #draw
        drawPolygon(ax,trapezoid)
        drawLine(ax,l_axis,color='red')
        drawAngle_multiple(ax,[a_right_top,a_right_bottom])
        setPolygonPoint(ax,trapezoid,l_axis,['A','B'])
        drawLine(ax,l_dash,True)
        drawAngle(ax,a_stem)
        drawText(ax,'$%s\mathrm{°}$'%(a_num_stem),p_bottom_r,'top_r')
        #comment
        comment = "(해설)\n한 직선이 이루는 각의 크기는 $$수식$$180rm °$$/수식$$ 이므로\n"
        comment += "(각$$수식$$DEH$$/수식$$) $$수식$$= 180rm ° - %srm ° = %srm °$$/수식$$입니다.\n"%(a_num_stem,180-a_num_stem)
        problem_optoin2 = random.randint(0,1)
        if problem_optoin2 == 0: #answer: top_left
            a_answer = [p_bottom_l,p_top_l,p_top_r]
            a_num_answer = a_num_stem
            a_name_stem = 'C'
            drawText(ax,'C',trapezoid[0],'top')
            drawAngle(ax,a_answer)
            comment += "각각의 대응각의 크기가 서로 같고 사각형의 네\n"
            comment += "각의 크기의 합은 $$수식$$360rm °$$/수식$$ 이므로\n"
            comment += "$$수식$$C =$$/수식$$ (각 $$수식$$GDE$$/수식$$) $$수식$$= 360rm ° - (90rm ° + 90rm ° + %srm °)$$/수식$$\n"%(180-a_num_stem)
            comment += "$$수식$$= %srm °$$/수식$$ 입니다." %(a_num_stem)
        elif problem_optoin2 == 1: #answer: bottom_left
            a_answer = [p_bottom_r,p_bottom_l,p_top_l]
            a_num_answer = 180 - a_num_stem
            a_name_stem = 'F'
            drawText(ax,'F',trapezoid[3],'bottom')
            drawAngle(ax,a_answer)
            comment += "$$수식$$F =$$/수식$$ (각 $$수식$$DEH$$/수식$$) $$수식$$= %srm °$$/수식$$입니다.\n"%(a_num_answer)
        #stem/answer
        stem = "선분$$수식$$AB$$/수식$$를 대칭축으로 하는 선대칭도형입니다. $$수식$$%s$$/수식$$에 알맞은 각도를 구해 보세요." %(a_name_stem)
        answer = '(답):$$수식$$%srm °$$/수식$$'%(a_num_answer)
        plt.axis('scaled')
        svg= saveSvg()
        #draw_comment
        if problem_optoin2 == 0:
            setPolygonPoint(ax,trapezoid,trapezoid,['','D','','F'])
        elif problem_optoin2 == 1:
            setPolygonPoint(ax,trapezoid,trapezoid,['C','D','',''])
        
        setPoint(ax,[p_bottom_r,p_top_m,p_bottom_m],['E','G','H'],['bottom_r','top_r','bottom_r'])
        plt.axis('scaled')
        svg_comment= saveSvg()
    #plt.show()
    return stem, answer, comment, [svg,svg_comment]

#5-2-3-37
def conandsym523_Stem_007():
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
    len_top = random.randint(5,15)*2
    len_bottom = len_top + random.randint(3,5)*2
    height = len_top + random.randint(0,5)
    side = round(math.sqrt(height*height+((len_bottom-len_top)**2)/4))
    perimeter = len_top + len_bottom + side*2
    l_name_left = ['AE','DF','AD']
    l_name_right = ['BE','CF','BC']
    len_list = [int(len_top/2),int(len_bottom/2),side]
    len_arc_list = [
        '$%s\mathrm{cm}$'%(len_list[0]),
        '$%s\mathrm{cm}$'%(len_list[1]),
        '$%s\mathrm{cm}$'%(len_list[2])
    ]
    while True:
        index_right = random.randint(0,2)
        index_left = random.randint(0,2)
        if index_right != index_left:
            break
    show_left = len_arc_list.copy()
    show_right = len_arc_list.copy()
    for i in range(3):
        if i != index_right:
            show_right[i] = ''
        if i != index_left:
            show_left[i] = ''
        if i != index_right and i != index_left:
            index_answer = i
    #generate shapes
    trapezoid = create_p_trapezoid(len_top,len_bottom,height)
    trapezoid = resize(trapezoid)
    p_middle_top = find_p_middle(trapezoid[0],trapezoid[1])
    p_middle_bottom = find_p_middle(trapezoid[2],trapezoid[3])
    l_middle = [p_middle_top,p_middle_bottom]
    ll_middle = [(p_middle_top[0],p_middle_top[1]+5),p_middle_bottom]
    l_left_list = [
        [trapezoid[0],p_middle_top],
        [p_middle_bottom,trapezoid[3]],
        [trapezoid[0],trapezoid[3]]
    ]
    l_right_list = [
        [p_middle_top,trapezoid[1]],
        [trapezoid[2],p_middle_bottom],
        [trapezoid[1],trapezoid[2]]
    ]
    position_left = ['top','bottom','left']
    position_right = ['top','bottom','right']
    #draw shapes
    drawPolygon(ax,trapezoid)
    drawLine(ax,l_middle,color='red')
    setPoint(ax,trapezoid,['A','B','C','D'],['top_l','top_r','bottom_r','bottom_l'])
    setPoint(ax,ll_middle,['E','F'],['top','bottom'])
    drawArc(ax,l_right_list[index_right],position_right[index_right],show_right[index_right])
    drawArc(ax,l_left_list[index_left],position_left[index_left],show_left[index_left])
    #stem/answer/comment
    stem = "직선$$수식$$EF$$/수식$$를 대칭축으로 하는 선대칭도형입니다. 사각형$$수식$$ABCD$$/수식$$의 둘레가 $$수식$$%srm cm$$/수식$$일 때 변$$수식$$%s$$/수식$$는 "\
            "몇 $$수식$$rm cm$$/수식$$인가요?"%(
                perimeter,l_name_left[index_answer]
            )
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(len_list[index_answer])
    comment = "(해설)\n선대칭도형에서 대응변의 길이가 같으므로\n"\
                "(변$$수식$$%s$$/수식$$) $$수식$$=$$/수식$$ (변$$수식$$%s$$/수식$$),\n"\
                "(변$$수식$$%s$$/수식$$) $$수식$$=$$/수식$$ (변$$수식$$%s$$/수식$$) $$수식$$= %srm cm$$/수식$$,\n"\
                "(변$$수식$$%s$$/수식$$) $$수식$$=$$/수식$$ (변$$수식$$%s$$/수식$$) $$수식$$= %srm cm$$/수식$$입니다.\n"\
                "변$$수식$$%s$$/수식$$의 길이를 $$수식$$□ rm cm$$/수식$$라고 하면\n"\
                "$$수식$$(%s + □ + %s) times 2 = %s$$/수식$$,\n"\
                "$$수식$$□ + %s = %s$$/수식$$, $$수식$$□ = %s - %s = %s$$/수식$$입니다.\n"\
                "따라서 변$$수식$$%s$$/수식$$는 $$수식$$%srm cm$$/수식$$입니다."%(
                    l_name_left[index_answer], l_name_right[index_answer],
                    l_name_left[index_right], l_name_right[index_right], len_list[index_right],
                    l_name_left[index_left], l_name_right[index_left], len_list[index_left],
                    l_name_left[index_answer],
                    len_list[index_left], len_list[index_right], perimeter,
                    len_list[index_left]+len_list[index_right], int(perimeter/2), int(perimeter/2), len_list[index_left]+len_list[index_right], len_list[index_answer],
                    l_name_left[index_answer], len_list[index_answer]
                )
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem,answer,comment, svg

#5-2-3-38
def conandsym523_Stem_008():
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
    while True:
        length = random.randint(4,10) * 2
        height = random.randint(4,10) * 2
        if length != height:
            break
    area = int(length*height/2)
    #generate shapes
    rhombus = create_p_rhombus(length,height)
    rhombus = resize(rhombus)
    l_length = [rhombus[1],rhombus[3]]
    l_height = [rhombus[0],rhombus[2]]
    p_middle = find_p_middle(rhombus[1],rhombus[3])
    #draw shapes
    drawPolygon(ax,rhombus,True,color='skyblue')
    drawLine(ax,l_length,True)
    drawArc(ax,l_length,'bottom_l','$%s\mathrm{cm}$'%(length))
    drawLine(ax,l_height,True)
    drawArc(ax,l_height,'right_t','$%s\mathrm{cm}$'%(height))
    setPoint(ax,rhombus+[p_middle],['A','B','C','D','E'],['top','right','bottom','left','top_l'])
    #stem/answer/comment
    random_axis = random.choice(['x','y'])
    area_firstTriangle = int(height*length/4)
    if random_axis == 'x':
        l_axis = 'BD'
        l_nonAxis = 'AC'
        l_halfNonAxis = 'AE'
        len_nonAxis = height
        len_axis = length
        first_triangle = 'ADB'
        second_triangle = 'CDB'
    elif random_axis == 'y':
        l_axis = 'AC'
        l_nonAxis = 'BD'
        l_halfNonAxis = 'DE'
        len_nonAxis = length
        len_axis = height
        first_triangle = 'ADC'
        second_triangle = 'ABC'
    stem = "선분$$수식$$%s$$/수식$$를 대칭축으로 하는 선대칭도형입니다. 사각형$$수식$$ABCD$$/수식$$의 넓이는 몇 $$수식$$rm cm^{2}$$/수식$$인가요?"%(l_axis)
    answer = '(답):$$수식$$%srm cm^{2}$$/수식$$'%(area)
    comment = "(해설)\n선분$$수식$$%s$$/수식$$는 선분$$수식$$%s$$/수식$$를 둘로 똑같이 나누므로\n"\
                "(선분$$수식$$%s$$/수식$$) $$수식$$= %s div 2 = %s(rm cm)$$/수식$$입니다. 대응점\n"\
                "끼리 이은 선분은 대칭축과 수직으로 만나므로\n"\
                "(삼각형$$수식$$%s$$/수식$$의 넓이)\n"\
                "$$수식$$= %s times %s div 2 = %s(rm cm^{2})$$/수식$$입니다.\n"\
                "삼각형$$수식$$%s$$/수식$$와 삼각형$$수식$$%s$$/수식$$의 넓이가 같으므로\n"\
                "(사각형$$수식$$ABCD$$/수식$$의 넓이) $$수식$$= %s times 2 = %s(rm cm^{2})$$/수식$$\n"\
                "입니다."%(
                    l_axis,l_nonAxis,
                    l_halfNonAxis, len_nonAxis, int(len_nonAxis/2),
                    first_triangle, len_axis, int(len_nonAxis/2), area_firstTriangle,
                    first_triangle, second_triangle,
                    area_firstTriangle, area
                )
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem,answer,comment, svg

#5-2-3-49
def conandsym523_Stem_009():
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
    while True:
        length = random.randint(5,15)
        width = random.randint(5,15)
        if abs(length-width) < 4:
            break
    left_angle = random.randint(40,70)
    perimeter = (length + width) * 2
    #generate shapes
    parallelogram = create_p_parallelogram(left_angle,width,length)
    parallelogram = resize(parallelogram)
    p_center = find_p_middle(parallelogram[0],parallelogram[2])
    p_list = ['A','B','C','D']
    p_position_list = ['top_l','top_r','bottom_r','bottom_l']
    l_show = random.choice([
        [parallelogram[0],parallelogram[1],'top'],
        [parallelogram[1],parallelogram[2],'right'],
        [parallelogram[2],parallelogram[3],'bottom'],
        [parallelogram[3],parallelogram[0],'left']
    ])
    #draw shapes
    drawPolygon(ax,parallelogram)
    setPoint(ax,parallelogram,p_list,p_position_list)
    drawDot(ax,[p_center],True)
    drawText(ax,'O',p_center,'bottom')
    if l_show[2] == 'top':
        matching_length_list = ['CD','AB','BC','DA']
        len_answer = width
        len_stem = length
    elif l_show[2] == 'right':
        matching_length_list = ['DA','BC','CD','AB']
        len_answer = length
        len_stem = width
    elif l_show[2] == 'bottom':
        matching_length_list = ['BA','DC','CB','AD']
        len_answer = width
        len_stem = length
    elif l_show[2] == 'left':
        matching_length_list = ['CB','AD','DC','BA']
        len_answer = length
        len_stem = width
    drawArc(ax,l_show[:2],l_show[2],'$%s\mathrm{cm}$'%(len_stem))
    #stem/answer/comment
    stem = "점$$수식$$O$$/수식$$를 대칭의 중심으로 하는 점대칭도형입니다. 도형의 둘레가 $$수식$$%srm cm$$/수식$$일 때 변$$수식$$%s$$/수식$$의 길이는 몇 $$수식$$rm cm$$/수식$$인가요?"%(
                perimeter, matching_length_list[2]
            )
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(len_answer)
    comment = "(해설)\n각각의 대응변의 길이가 서로 같으므로\n"\
                "(변$$수식$$%s$$/수식$$) $$수식$$=$$/수식$$ (변$$수식$$%s$$/수식$$) $$수식$$= %srm cm$$/수식$$,\n"\
                "(변$$수식$$%s$$/수식$$) $$수식$$=$$/수식$$ (변$$수식$$%s$$/수식$$)\n"\
                "$$수식$$= (%s - %s times 2) div 2 = %s(rm cm)$$/수식$$입니다."%(
                    matching_length_list[0],matching_length_list[1],len_stem,
                    matching_length_list[2],matching_length_list[3],
                    perimeter,len_stem,len_answer
                )
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem,answer,comment, svg

#5-2-3-54
def conandsym523_Stem_010():
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
    while True:
        length = random.randint(5,15)
        width = random.randint(5,15)
        if abs(length-width) < 5:
            break
    left_angle = random.randint(60,70)
    diagonal_left = int(math.sqrt(length**2+width**2-2*length*width*math.cos(math.radians(left_angle))))
    diagonal_right = int(math.sqrt(length**2+width**2-2*length*width*math.cos(math.radians(180-left_angle))))
    if diagonal_left%2 != 0:
        diagonal_left += 1
    if diagonal_right%2 != 0:
        diagonal_right += 1
    halfDiagonal_left = int(diagonal_left/2)
    halfDiagonal_right = int(diagonal_right/2)
    sumOfDiagonals = diagonal_left + diagonal_right
    #generate shapes
    parallelogram = create_p_parallelogram(left_angle,width,length)
    parallelogram = resize(parallelogram)
    p_center = find_p_middle(parallelogram[0],parallelogram[2])
    p_list = ['A','B','C','D']
    p_position_list = ['top_l','top_r','bottom_r','bottom_l']
    l_show = random.choice([
        [parallelogram[0],p_center,'top_r'],
        [parallelogram[1],p_center,'top_l'],
        [parallelogram[2],p_center,'top_r'],
        [parallelogram[3],p_center,'top_l']
    ])
    #draw shapes
    drawPolygon(ax,parallelogram)
    setPoint(ax,parallelogram,p_list,p_position_list)
    drawDot(ax,[p_center],True)
    drawText(ax,'O',p_center,'bottom')
    drawLine(ax,[parallelogram[0],parallelogram[2]],True)
    drawLine(ax,[parallelogram[1],parallelogram[3]],True)
    if l_show[0] == parallelogram[0]:
        matching_l_list = ['AO','CO','BD','BO','DO']
        len_stem = halfDiagonal_left
        len_answer = halfDiagonal_right
    elif l_show[0] == parallelogram[1]:
        matching_l_list = ['BO','DO','AC','AO','CO']
        len_stem = halfDiagonal_right
        len_answer = halfDiagonal_left
    elif l_show[0] == parallelogram[2]:
        matching_l_list = ['CO','AO','BD','DO','BO']
        len_stem = halfDiagonal_left
        len_answer = halfDiagonal_right
    elif l_show[0] == parallelogram[3]:
        matching_l_list = ['DO','BO','AC','CO','AO']
        len_stem = halfDiagonal_right
        len_answer = halfDiagonal_left
    drawArc(ax,l_show[:2],l_show[2],'$%s\mathrm{cm}$'%(len_stem))
    #stem/answer/comment
    stem = "사각형$$수식$$ABCD$$/수식$$는 점$$수식$$O$$/수식$$를 대칭의 중심으로 하는 점대칭도형입니다. 두 대각선의 길이의 합이 $$수식$$%srm cm$$/수식$$일 때 선분$$수식$$%s$$/수식$$는 몇 $$수식$$rm cm$$/수식$$인가요?"%(
                sumOfDiagonals, matching_l_list[3]
            )
    answer = "(답):$$수식$$%srm cm$$/수식$$"%(len_answer)
    comment = "(해설)\n각각의 대응점에서 대칭의 중심까지의 거리가\n"\
                "서로 같으므로\n"\
                "(선분$$수식$$%s$$/수식$$) $$수식$$=$$/수식$$ (선분$$수식$$%s$$/수식$$) $$수식$$= %srm cm$$/수식$$입니다.\n"\
                "두 대각선의 길이의 합이 $$수식$$%srm cm$$/수식$$이므로\n"\
                "(선분$$수식$$%s$$/수식$$) $$수식$$= %s - %s times 2 = %s(rm cm)$$/수식$$,\n"\
                "(선분$$수식$$%s$$/수식$$) $$수식$$=$$/수식$$ (선분$$수식$$%s$$/수식$$) $$수식$$= %s div 2 = %s(rm cm)$$/수식$$입니다."\
                ""%(
                    matching_l_list[0],matching_l_list[1],len_stem,
                    sumOfDiagonals,
                    matching_l_list[2],sumOfDiagonals,len_stem,sumOfDiagonals-len_stem*2,
                    matching_l_list[3],matching_l_list[4],sumOfDiagonals-len_stem*2,len_answer
                )
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem,answer,comment, svg
