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
    #pt = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
    #pt = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if len(text) == 0:
        for t in range(len(points)):
            text.append('')

    for i in range(0,len(points)):
        cp = points[i]
        l = len(text[i])
        if position[i] == 'top':
            plt.text(cp[0]-2*l, cp[1]+7, text[i], fontsize=16, zorder=3)
        elif position[i] == 'bottom':
            plt.text(cp[0]-2*l, cp[1]-9, text[i], fontsize=16, zorder=3)
        elif position[i] == 'left':
            plt.text(cp[0]-3-l*4.5, cp[1]-2, text[i], fontsize=16, zorder=3)
        elif position[i] == 'right':
            plt.text(cp[0]+l+7, cp[1]-2, text[i], fontsize=16, zorder=3)
        elif position[i] == 'top_r':
            plt.text(cp[0]+l*0.3, cp[1]+2, text[i], fontsize=16, zorder=3)
        elif position[i] == 'top_l':
            plt.text(cp[0]+1-l*5, cp[1]+2, text[i], fontsize=16, zorder=3)
        elif position[i] == 'bottom_r':
            plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5, text[i], fontsize=16, zorder=3)
        elif position[i] == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5, text[i], fontsize=16, zorder=3)
        else: raise Exception('no matching position')

        if fill:
            ax.plot(points[i][0], points[i][1],"k.", zorder=3)
    
# 점
def drawDot(ax,points=list,colors=False):
    if colors: format = 'r.'
    else: format = 'k.'
    for i in range(0,len(points)):
        ax.plot(points[i][0], points[i][1],format, zorder=3)

# 각
def drawPolygonAngle_(ax, verts=list, show_angle=[], show_angle_num=[], show_point=[]):
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
            if (angle_num%5) < 3:
                angle_num = angle_num - (angle_num%5)
            angle_sum += angle_num
        #angle_sign
        if show_angle != []:
            if show_angle[i] == True: drawAngle(ax,[angle])
            elif show_angle[i] == False: continue
            else: raise Exception("Invalid input")
        #angle_num
        if show_angle_num != []:
            angle_p = verts[second_index]
            position = text_position_top_bottom(angle_p)
            if show_angle_num[i] == True: drawText(ax,'%s°'%(angle_num),angle_p,position)
            elif show_angle_num[i] == False: continue
            else: raise Exception("Invalid input")
        #point_text
        if show_point != []:
            text_p = verts[second_index]
            text = show_point[second_index]
            position = text_position_right_left(text_p)
            if show_point[i] != '': setPoint(ax,text_p,text,position)
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
    if dash: linestype = 'dashed'
    else: linestype = '-'
    line_1 = matplotlib.lines.Line2D((pts[0][0],pts[1][0]), (pts[0][1],pts[1][1]), linewidth=1, linestyle = linestype,color=color)
    ax.add_line(line_1)

# 다각형
def drawPolygon(ax, verts, fill=False, alpha=1, dash=False,color=''):
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
            pp = mpatches.PathPatch(path, ec='black', fill=False, lw=1, ls='--', zorder=3)
        else:
            pp = mpatches.PathPatch(path, ec='black', fill=False, lw=1, zorder=3)
    ax.add_patch(pp)
    verts.pop()

# 다각형 + 각 + Text
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
    def text_position_top_bottom(p):
        x = p[0]
        y = p[1]
        output = ""
        if y > 0:
            output += 'top'
        else:
            output += 'bottom'

        return output
    def text_position_right_left(p):
        x = p[0]
        y = p[1]
        output = ""
        if x > 0:
            output += 'right'
        else:
            output += 'left'
        return output

    if len(verts) != len(show_angle) and show_angle != []: raise Exception("size of verts and size of show_angle don't match")
    if len(verts) != len(show_angle_num) and show_angle_num != []: raise Exception("size of verts and size of show_angle_num don't match")
    if len(verts) != len(show_point) and show_point != []: raise Exception("size of verts and size of show_point don't match")
    #centeralize
    verts = move_to_center(verts)
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
            if (angle_num%5) < 3:
                angle_num = angle_num - (angle_num%5)
            angle_sum += angle_num
        #angle_sign
        if show_angle != []:
            if show_angle[i] == True: drawAngle(ax,[angle])
            elif show_angle[i] == False: continue
            else: raise Exception("Invalid input")
        #angle_num
        if show_angle_num != []:
            angle_p = verts[second_index]
            position = text_position_top_bottom(angle_p)
            if show_angle_num[second_index] == True: drawText(ax,'%s°'%(angle_num),angle_p,position)
            elif show_angle_num[second_index] == False: pass
            else: raise Exception("Invalid input")
        #point_text
        if show_point != []:
            text_p = verts[second_index]
            text = show_point[second_index]
            position = text_position_right_left(text_p)
            if show_point[second_index] != '': setPoint(ax,[text_p],[text],[position])

    vert = verts
    vert.append(verts[0])
    codes = [Path.MOVETO]
    for i in range(0,len(verts)-2):
        codes.append(Path.LINETO)
    codes.append(Path.CLOSEPOLY)
    path = Path(verts,codes)
    pp = mpatches.PathPatch(path, ec='black', fill=False, lw=1, zorder=3)
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
        plt.text(cp[0]-2*l, cp[1]+5, text, fontsize=16, zorder=3)
    elif position == 'bottom':
        plt.text(cp[0]-2*l, cp[1]-8, text, fontsize=16, zorder=3)
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

# 선분의 길이를 표시하는 bezier 곡선을 그리는 함수
def drawPolygonArc_(ax,verts=list,show_length=[],show_text=[],length_ratio=10,unit='cm'):
    def c_distance(p1=tuple, p2=tuple):
        import math
        d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
        return d
    def new_p_middle(p1=tuple,p2=tuple):
        return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
    def text_position_polygon(p_list,p):
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
        if dx >= dy: #right/left - x
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
        position = text_position_polygon(verts,new_p_middle(p1,p2))
        length = int(c_distance(p1,p2)/length_ratio)
        if show_length != []:
            if show_length[i] == True:
                drawArc(ax,[p1,p2],position,str(length)+' '+unit)
        if show_text != []: 
            if show_text[i] != '':
                drawArc(ax,[p1,p2],position,show_text[i])
def drawArc(ax, p_list, position, text, boxed=False,color='black'):
    if len(p_list) != 2: raise Exception('p_list has more or less than 2 elements')
    p1 = p_list[0]
    p2 = p_list[1]
    if 'top' in position: cp = find_controlPoint_arc(p1,p2,'top')
    elif 'bottom' in position: cp = find_controlPoint_arc(p1,p2,'bottom')
    elif 'right' in position: cp = find_controlPoint_arc(p1,p2,'right')
    elif 'left' in position: cp = find_controlPoint_arc(p1,p2,'left')
    l = len(text)
    if 'mathrm' in text: 
        l -= 10
    vert = [
        p1,
        cp, # 제어점
        p2
    ]
    codes = [
        Path.MOVETO,
        Path.CURVE3,
        Path.CURVE3
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
            plt.text(cp[0]-2-l*5, cp[1]-2, text, fontsize=16, zorder=3)
        elif position == 'right':
            plt.text(cp[0]+l*0.1, cp[1]-2, text, fontsize=16, zorder=3)
        elif position in ['top_r','right_t']:
            plt.text(cp[0]+l*0.1, cp[1]+2, text, fontsize=16, zorder=3)
        elif position in ['top_l','left_t']:
            plt.text(cp[0]-2-l*5, cp[1]+2, text, fontsize=16, zorder=3)
        elif position in ['bottom_r','right_b']:
            plt.text(cp[0]+l, cp[1]-8+l*0.5, text, fontsize=16, zorder=3)
        elif position in ['bottom_l','left_b']:
            plt.text(cp[0]-2-l*5, cp[1]-4, text, fontsize=16, zorder=3)
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

def line_equation(p1, p2, x):
    y = ((p2[1]-p1[1])/(p2[0]-p1[0])) * (x-p1[0]) + p1[1]

    return y

#plt.rcParams['text.usetex'] = True
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf8')
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf8')

#return pairs
def fact_num_pair(num):
    num = int(num)
    dict_num = dict()
    num_list = []
    max = int(num**0.5) + 1
    #fill the dict_num
    for i in range(2,num+1):
        dict_num[i] = 0
    i = 2
    while i < max:
        if num % i == 0:
            num_list.append((i,int(num/i)))
        i += 1

    return num_list
def is_exist(elements,l):
    if l == []:
        return False
    for temp_l in l:
        temp_elements = elements.copy()
        for i in range(len(temp_l)):
            if temp_l[i] in elements:
                temp_elements.remove(temp_l[i])
        if temp_elements == []:
            return True
        
    return False
def random_whole(min,max):
    import random
    while True:
        x = random.randint(min,max)
        if x != 0:
            return x


def new_p_middle(p1=tuple,p2=tuple):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def new_p_regular(n=3,scale=100,move_x=0,move_y=0):
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
        
    #polygon.reverse()
    polygon = move_to_center(polygon)
    polygon = move_p(polygon,move_x,move_y)
    return polygon
def create_p_parallelogram(left_angle=0,side=0,width=0,move_x=0,move_y=0):
    import random,math
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
    if side == 0 or width == 0:
        side = random.randint(3,9)
        width = random.randint(5,9)
    #points
    p_bottom_l = (0,0)
    p_bottom_r = (width,0)
    p_top_l = new_p_angle(left_angle,side)
    p_top_r = new_p_angle(left_angle,side,p_bottom_r)

    parallelogram = [p_top_l,p_top_r,p_bottom_r,p_bottom_l]
    parallelogram = move_p(parallelogram,move_x,move_y)
    return parallelogram
def new_p_parallelogram(scale=100,move_x=0,move_y=0):
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
    #angle1,angle2
    angle1_5 = random.randint(6,30)
    angle2_5 = 36 - angle1_5
    angle1 = angle1_5*5
    angle2 = angle2_5*5
    #lengh1,length2
    length1 = random.randint(3,9)
    length2 = random.randint(5,9)
    #points
    bottom_left_p = (0,0)
    bottom_right_p = (length2,0)
    top_left_p = new_p_angle(angle1,length1)
    top_right_p = new_p_angle(angle1,length1,bottom_right_p)

    rectangle = [top_left_p,top_right_p,bottom_right_p,bottom_left_p]
    rectangle = move_to_center(rectangle)
    rectangle = move_p(rectangle,move_x,move_y)
    return rectangle
def new_p_rectangle(width,height,move_x=0,move_y=0):
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
def new_p_triangle(width=10,height=10,angle=0,move_x=0,move_y=0):
    import random
    import math
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
def new_p_rhombus(width,height,move_x=0,move_y=0):
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
def new_p_trapezoid_(length_top,length_bottom_l,length_bottom_r,height,move_x=0,move_y=0):
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
    p_bottom_r = ((length_top/2)*-1+length_bottom_r,0)
    p_bottom_l = ((length_top/2+length_bottom_l)*-1,0)
    trapezoid = [p_top_l,p_top_r,p_bottom_r,p_bottom_l]
    trapezoid = move_p(trapezoid,move_x,move_y)
    return trapezoid


def resize_multiple(p_list_multiple=list,scale=90):
    def move_p(p_list=list,x_move=0,y_move=0):
        #center point
        new_p_list = []
        for index in range(len(p_list)):
            p = p_list[index]
            new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
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
    ratio = (scale*2)/sum_criteria_val * 1.5

    #scale up/down with calculated ratio
    new_p_list_multiple = []
    x_move = -100 + int(scale*2 / len(p_list_multiple))*(i+1)
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
def move_p(p_list=list,x_move=0,y_move=0):
    #center point
    new_p_list = []
    for index in range(len(p_list)):
        p = p_list[index]
        new_p_list.append((p[0]+x_move,p[1]+y_move))
    return new_p_list
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

def random_line(polygon=list):
    import random
    n = random.randint(0,len(polygon)-1)
    p1 = polygon[n]
    if n == (len(polygon)-1): p2 = polygon[0]
    else: p2 = polygon[n+1]
    return [p1,p2]
def text_position_circle(p):
    x = p[0]
    y = p[1]
    output = ""
    if y > 0:
        output += 'top'
    else:
        output += 'bottom'
    if x > 0:
        output += '_r'
    else:
        output += '_l'
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
        else: #left
            position = 'left'
    else: #top/bottom - y
        if y >= y_center: #top
            position = 'top'
        else: #bottom
            position = 'bottom'
    return position


#5-1-6-02
def roundandarea516_Stem_001():
    char_list = ['영','일','이','삼','사','오','육','칠','팔','구','십']
    n = random.randint(3,8)
    length = random.randint(2,10)
    perimeter = n*length

    stem = "한 변의 길이가 $$수식$$%srm m$$/수식$$인 정%s각형의 둘레는 몇 $$수식$$rm m$$/수식$$인가요?" %(length,char_list[n])
    answer = '(답):$$수식$$%srm m$$/수식$$'%(perimeter)
    comment = "(해설)\n(정%s각형의 둘레)\n"\
                "$$수식$$=$$/수식$$ (한 변의 길이) $$수식$$times$$/수식$$ (변의 수)\n"\
                "$$수식$$=%s times %s = %s (rm m)$$/수식$$" %(
                    char_list[n],
                    length,n,perimeter
                )
    return stem,answer,comment

#5-1-6-03
def roundandarea516_Stem_002():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #start
    char_list = ['영','일','이','삼','사','오','육','칠','팔','구','십']
    n = random.randint(3,8)
    length = random.randint(2,10)
    perimeter = n*length
    polygon = new_p_regular(n)
    polygon = resize(polygon)
    #draw
    line = random_line(polygon)
    p1 = line[0]
    p2 = line[1]
    position = find_text_position_polygonArc(polygon,line)
    drawArc(ax,[p1,p2],position,'$%s \mathrm{cm}$'%(length))
    drawPolygon(ax,polygon)

    stem = "다음 정다각형의 둘레를 구해 보세요."
    comment = "(해설)\n(정%s각형의 둘레)\n"\
                "$$수식$$=$$/수식$$ (한 변의 길이) $$수식$$times$$/수식$$ (변의 수)\n"\
                "$$수식$$= %s times %s = %s(rm cm)$$/수식$$" %(
                    char_list[n],
                    length,n,perimeter
                )
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(perimeter)
    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg

#5-1-6-14
def roundandarea516_Stem_003():
    width = random.randint(10,20)
    height = random.randint(10,20)
    while width == height:
        width = random.randint(10,20)
        height = random.randint(10,20)
    perimeter = (width+height)*2

    stem = "가로가 $$수식$$%srm cm$$/수식$$, 세로가 $$수식$$%srm cm$$/수식$$인 직사각형 모양의 액자의 둘레는 몇 $$수식$$rm cm$$/수식$$인가요?" %(width,height)
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(perimeter)
    comment = "(해설)\n(직사각형의 둘레) $$수식$$=$$/수식$$ {(가로)$$수식$$+$$/수식$$(세로)}$$수식$$times 2$$/수식$$ 이므로\n"\
                "(액자의 둘레) $$수식$$=(%s+%s) times 2 = %s(rm cm)$$/수식$$입니다." %(width,height,perimeter)
    return stem,answer,comment

#5-1-6-15
def roundandarea516_Stem_004():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #start
    height = random.randint(3,15)
    width = random.randint(3,15)
    while height == width:
        height = random.randint(3,15)
        width = random.randint(3,15)
    perimeter = (height + width)*2
    parallelogram = new_p_parallelogram()
    parallelogram = resize(parallelogram)
    #point
    p_top_l = parallelogram[0]
    p_top_r = parallelogram[1]
    p_bottom_r = parallelogram[2]
    p_bottom_l = parallelogram[3]
    #draw
    if random.randint(0,1):
        drawArc(ax,[p_bottom_l,p_top_l],'left','$%s \mathrm{cm}$'%(height))
        drawArc(ax,[p_top_l,p_top_r],'top','$%s \mathrm{cm}$'%('□'))
        answer_value = width
        stem_value = height
    else:
        drawArc(ax,[p_bottom_l,p_top_l],'left','$%s \mathrm{cm}$'%('□'))
        drawArc(ax,[p_top_l,p_top_r],'top','$%s \mathrm{cm}$'%(width))
        answer_value = height
        stem_value = width
    drawPolygon(ax,parallelogram)

    stem = "평행사변형의 둘레가 $$수식$$%srm cm$$/수식$$일 때 □ 안에 알맞은 수를 구해 보세요."%(perimeter)
    comment = "(해설)\n둘레가 $$수식$$%srm cm$$/수식$$인 평행사변형의 한 변의 길이와\n"\
                "다른 변의 길이의 합은 $$수식$$%s div 2 = %s(rm cm)$$/수식$$입니다.\n "\
                "$$수식$$□ + %s = %s$$/수식$$ 이므로 $$수식$$□ = %s - %s = %s(rm cm)$$/수식$$입니다." %(
                    perimeter,
                    perimeter,width+height,
                    stem_value,width+height,width+height,stem_value,answer_value
                    )
    answer = '(답):$$수식$$%s$$/수식$$'%str(answer_value)
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem,answer,comment,svg

#5-1-6-19
def roundandarea516_Stem_005():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #start
    n = random.randint(2,4)
    side_n = 2 + 2*n
    length = random.randint(2,9)
    perimeter = side_n*length
    width = length * n
    height = length
    rectangle = new_p_rectangle(width,height)
    rectangle = resize(rectangle)
    #point
    p_top_l = rectangle[0]
    p_top_r = rectangle[1]
    p_bottom_r = rectangle[2]
    p_bottom_l = rectangle[3]
    p_length =  round((p_top_r[0] - p_top_l[0])/n,5)
    p_top_l_temp = p_top_l
    p_bottom_l_temp = p_bottom_l
    colors = []
    color_index = random.randint(0,147)
    for i in mcolors.CSS4_COLORS:
        colors.append(i)
    for i in range(n):
        x = p_top_l[0] + p_length*(i+1)
        p_top_middle = (x,p_top_l_temp[1])
        p_bottom_middle = (x,p_bottom_l_temp[1])
        drawPolygon(ax,[p_top_l_temp,p_top_middle,p_bottom_middle,p_bottom_l_temp],True,color=colors[color_index])
        p_top_l_temp = p_top_middle
        p_bottom_l_temp = p_bottom_middle
    
    stem = "정사각형 모양의 블록 $$수식$$%s$$/수식$$개를 붙여 만든 직사각형의 둘레가 $$수식$$%srm cm$$/수식$$입니다. 블록의 한 변의 길이는 몇 $$수식$$rm cm$$/수식$$인가요?" %(n,perimeter)
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(length)
    comment = "(해설)\n블록의 한 변의 길이를 □ 라고 하면\n"\
                "직사각형의 둘레는 $$수식$$□ times %s$$/수식$$ 입니다.\n "\
                "$$수식$$□ times %s = %s$$/수식$$ → $$수식$$□ = %s div %s = %s(rm cm)$$/수식$$입니다.\n"\
                "따라서 블록의 한 변의 길이는 $$수식$$%srm cm$$/수식$$입니다." %(
                    side_n,
                    side_n,perimeter,perimeter,side_n,length,
                    length
                )
    
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem,answer,comment,svg
    
#5-1-6-21
def roundandarea516_Stem_006():
    width = random.randint(3,10)
    height = random.randint(3,10)
    while width == height:
        width = random.randint(3,10)
        height = random.randint(3,10)
    perimeter = (width+height) * 2
    random_prob = random.randint(0,1)
    if random_prob: 
        stem_variable = "가로"
        stem_value = width
        answer_variable = "세로"
        answer_value = height
    else:
        stem_variable = "세로"
        stem_value = height
        answer_variable = "가로"
        answer_value = width
    stem = "%s가 $$수식$$%srm cm$$/수식$$이고 둘레가 $$수식$$%srm cm$$/수식$$인 직사각형이 있었습니다. 이 직사각형의 %s는 몇 $$수식$$rm cm$$/수식$$인가요?" %(
                stem_variable,stem_value,perimeter,
                answer_variable
                )
    comment = "(해설)\n직사각형의 %s를 $$수식$$□ rm cm$$/수식$$라고 하면\n"\
                "$$수식$$(□ + %s) times 2 = %s$$/수식$$, $$수식$$□ + %s = %s$$/수식$$, $$수식$$□ = %s$$/수식$$입니다.\n"\
                "따라서 직사각형의 %s는 $$수식$$%srm cm$$/수식$$입니다." %(
                    answer_variable,
                    stem_value,perimeter,stem_value,width+height,answer_value,
                    answer_variable,answer_value
                )
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(answer_value)
    return stem,answer,comment

#5-1-6-37
def roundandarea516_Stem_007():
    width = random.randint(3,10)
    height = random.randint(3,10)
    while width == height:
        width = random.randint(3,10)
        height = random.randint(3,10)
    area = (width*height)
    random_prob = random.randint(0,1)
    if random_prob: 
        stem_variable = "가로"
        stem_value = width
        answer_variable = "세로"
        answer_value = height
    else:
        stem_variable = "세로"
        stem_value = height
        answer_variable = "가로"
        answer_value = width
    stem = "넓이가 $$수식$$%srm cm^{2}$$/수식$$이고 %s가 $$수식$$%srm cm$$/수식$$인 직사각형 모양의 수첩이 있습니다. 수첩의 %s는 몇 $$수식$$rm cm$$/수식$$인가요?" %(
                area,stem_variable,stem_value,
                answer_variable
                )

    comment = "(해설)\n(직사각형의 넓이) $$수식$$=$$/수식$$ (가로) $$수식$$times$$/수식$$ (세로)이므로\n"\
                "(%s) $$수식$$=$$/수식$$ (직사각형의 넓이) $$수식$$div $$/수식$$(%s)입니다.\n"\
                "→ (%s) $$수식$$= %s div %s = %s(rm cm)$$/수식$$" %(
                    answer_variable,stem_variable,
                    answer_variable,area,stem_value,answer_value
                    )
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(answer_value)
    return stem,answer,comment

#5-1-6-40
def roundandarea516_Stem_008():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #create variables
    a_width = random.randint(3,8)
    a_height = random.randint(3,8)
    while a_width == a_height:
        a_width = random.randint(3,8)
        a_height = random.randint(3,8)
    a_area = a_width*a_height
    n = random.randint(2,3)
    b_area = a_area*n
    if random.randint(0,1):
        b_width,b_height = random.sample([a_height*n,a_width],2)
    else:
        b_width,b_height = random.sample([a_height,a_width*n],2)
    
    #draw
    a_rectangle = new_p_rectangle(a_width*5,a_height*5)
    b_rectangle = new_p_rectangle(b_width*5,b_height*5)
    a_rectangle,b_rectangle = resize_multiple([a_rectangle,b_rectangle])
    a_text = (a_rectangle[0][0]-5,max(a_rectangle[0][1],b_rectangle[0][1])+10)
    b_text = (b_rectangle[0][0]-5,max(a_rectangle[0][1],b_rectangle[0][1])+10)
    drawText(ax,'A',a_text)
    drawText(ax,'B',b_text)
    drawPolygon(ax,a_rectangle)
    drawPolygonArc_(ax,a_rectangle,show_text=['$%s\mathrm{cm}$'%(a_width),'','','$%s\mathrm{cm}$'%(a_height)])
    drawPolygon(ax,b_rectangle)
    random_prob = random.randint(0,1)
    if random_prob: 
        stem_variable = "가로"
        stem_value = b_width
        answer_variable = "세로"
        answer_value = b_height
        drawPolygonArc_(ax,b_rectangle,show_text=['$%s \mathrm{cm}$'%(b_width),'','',''])
    else:
        stem_variable = "세로"
        stem_value = b_height
        answer_variable = "가로"
        answer_value = b_width
        drawPolygonArc_(ax,b_rectangle,show_text=['','$%s \mathrm{cm}$'%(b_height),'',''])
    stem = "직사각형$$수식$$B$$/수식$$의 넓이는 직사각형$$수식$$A$$/수식$$의 넓이의 $$수식$$%s$$/수식$$배 입니다. 직사각형$$수식$$B$$/수식$$의 %s는 몇 $$수식$$rm cm$$/수식$$인가요?" %(
                n,
                answer_variable
            )
    comment = "(해설)\n($$수식$$A$$/수식$$의 넓이) $$수식$$= %s times %s = %s(rm cm^{2})$$/수식$$\n"\
                "$$수식$$B$$/수식$$의 넓이는 $$수식$$A$$/수식$$의 넓이의 $$수식$$%s$$/수식$$배이므로\n"\
                "$$수식$$%s times %s = %s (rm cm^{2})$$/수식$$입니다.\n"\
                "($$수식$$B$$/수식$$의 넓이) $$수식$$=$$/수식$$ (%s)$$수식$$times %s = %s$$/수식$$,\n"\
                "(%s) $$수식$$= %s div %s = %s(rm cm)$$/수식$$" %(
                    a_width,a_height,a_area,
                    n,
                    a_area,n,b_area,
                    answer_variable,stem_value,b_area,
                    answer_variable,b_area,stem_value,answer_value
                )
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(answer_value)
    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg

#5-1-6-44
def roundandarea516_Stem_009():
    def km2_2_m2(num):
        return num*1000000
    def m2_2_cm2(num):
        return num*10000
    #unit
    unit_list = ['cm^{2}','{km}^{2}']
    random.shuffle(unit_list)
    num1_unit = unit_list[0]
    num2_unit = unit_list[1]
    #random number
    num1 = random.randint(1,15)
    num2 = random.randint(1,15)
    while num1 == num2:
        num1 = random.randint(1,15)
        num2 = random.randint(1,15)
    #create result number
    if num1_unit == 'cm^{2}': num1_ = m2_2_cm2(num1)
    else: 
        temp = km2_2_m2(num1)
        num1_ = num1
        num1 = temp
    if num2_unit == 'cm^{2}': num2_ = m2_2_cm2(num2)
    else: 
        temp = km2_2_m2(num2)
        num2_ = num2
        num2 = temp
    #creating stem list
    stem_1 = [(num1,'m^{2}'),(num1_,num1_unit)]
    stem_2 = [(num2,'m^{2}'),(num2_,num2_unit)]
    random.shuffle(stem_1)
    random.shuffle(stem_2)
    #form stem/comment
    stem = "□  안에 알맞은 단위를 써넣으세요.\n"
    comment = "(해설)\n$$수식$$1rm m^{2} = 10000rm cm^{2}$$/수식$$, $$수식$$1rm km^{2} = 1000000rm m^{2}$$/수식$$이므로\n"
    random_prob = random.randint(0,1)
    if random_prob: #stem_1,stem_2
        stem += "(1) $$수식$$%srm %s = %s □ $$/수식$$ \n" %(stem_1[0][0],stem_1[0][1],stem_1[1][0])
        stem += "(2) $$수식$$%srm %s = %s □ $$/수식$$" %(stem_2[0][0],stem_2[0][1],stem_2[1][0])
        answer = "(답):$$수식$$rm %s$$/수식$$, $$수식$$rm %s$$/수식$$"%(stem_1[1][1],stem_2[1][1])
        comment += "(1) $$수식$$%srm %s = %srm %s$$/수식$$ \n" %(stem_1[0][0],stem_1[0][1],stem_1[1][0],stem_1[1][1])
        comment += "(2) $$수식$$%srm %s = %srm %s$$/수식$$" %(stem_2[0][0],stem_2[0][1],stem_2[1][0],stem_2[1][1])
    else: #stem_2,stem_1
        stem += "(1) $$수식$$%srm %s = %s □ $$/수식$$ \n" %(stem_2[0][0],stem_2[0][1],stem_2[1][0])
        stem += "(2) $$수식$$%srm %s = %s □ $$/수식$$" %(stem_1[0][0],stem_1[0][1],stem_1[1][0])
        answer = "(답):$$수식$$rm %s$$/수식$$, $$수식$$rm %s$$/수식$$"%(stem_2[1][1],stem_1[1][1])
        comment += "(1) $$수식$$%srm %s = %srm %s$$/수식$$ \n" %(stem_2[0][0],stem_2[0][1],stem_2[1][0],stem_2[1][1])
        comment += "(2) $$수식$$%srm %s = %srm %s$$/수식$$" %(stem_1[0][0],stem_1[0][1],stem_1[1][0],stem_1[1][1])
    return stem,answer,comment

#5-1-6-46
def roundandarea516_Stem_010():
    def km2_2_m2(num):
        return num*1000000
    def m2_2_cm2(num):
        return num*10000
    squareUnit_list = ['m^{2}','km^{2}']
    square_length = random.randint(1,10)
    square_unit = random.choice(squareUnit_list)
    area = int(random.choice(['100','1000','10000']))
    if square_unit == squareUnit_list[0]: 
        area_unit = 'cm^{2}'
        answer_num =  int(m2_2_cm2(square_length**2) / area)
    else: 
        area_unit = 'm^{2}'
        answer_num =  int(km2_2_m2(square_length**2) / area)
    stem = "한 변의 길이가 $$수식$$%srm %s$$/수식$$인 정사각형 모양의 땅에는 $$수식$$%srm %s$$/수식$$가 몇 번 들어가나요?" %(
                str(square_length),square_unit.split('^')[0],
                str(area),area_unit
            )
    comment = "(해설)\n(땅의 넓이) $$수식$$= %s times %s = %s (rm %s)$$/수식$$\n"\
                "$$수식$$%srm %s = %srm %s$$/수식$$ 이므로 $$수식$$%srm %s$$/수식$$가\n"\
                "$$수식$$%s$$/수식$$번 들어갑니다." %(
                    square_length,square_length,square_length**2,square_unit,
                    str(square_length**2),square_unit,str(answer_num*area),area_unit,str(area),area_unit,
                    answer_num
                )
    answer = '(답):$$수식$$%s$$/수식$$번'%str(answer_num)
    return stem,answer,comment

#5-1-6-52
def roundandarea516_Stem_011():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #create variable
    while True:
        height = random.randint(3,10)
        width = random.randint(3,10)
        angle = random.randint(45,60)
        side = int(height/math.sin(math.radians(angle)))
        if width > side:
            break
    sumOfWidthHeight = width + height
    area = height*width
    random_prob = random.randint(0,1)
    #draw
    parallelogram = create_p_parallelogram(angle,side,width)
    parallelogram = resize(parallelogram)
    drawPolygon(ax,parallelogram)
    #point
    p_top_l = parallelogram[0]
    p_top_r = parallelogram[1]
    p_bottom_r = parallelogram[2]
    p_bottom_l = parallelogram[3]
    p_middle_x = (new_p_middle(p_top_l,p_top_r)[0] + new_p_middle(p_bottom_l,p_bottom_r)[0])/2
    p_top_middle = (p_middle_x,p_top_l[1])
    p_bottom_middle = (p_middle_x,p_bottom_l[1])
    
    if random_prob: #answer=높이
        stem_variable = "밑변의 길이"
        stem_value = width
        answer_variable = "높이"
        answer_value = height
        drawArc(ax,[p_bottom_l,p_bottom_r],'bottom','$%s\mathrm{cm}$'%(stem_value))
        drawAngle(ax,[p_top_middle,p_bottom_middle,p_bottom_l])
        drawLine(ax,[p_top_middle,p_bottom_middle],True)
    else: #answer=밑변의 길이
        stem_variable = "높이"
        stem_value = height
        answer_variable = "밑변의 길이"
        answer_value = width
        drawLine(ax,[p_top_middle,p_bottom_middle],True)
        drawArc(ax,[p_top_middle,p_bottom_middle],'right','$%s\mathrm{cm}$'%(stem_value))
        drawAngle(ax,[p_top_middle,p_bottom_middle,p_bottom_l])
    #stem/comment/answer
    stem = "다음 평행사변형의 넓이가 $$수식$$%srm cm^{2}$$/수식$$이고 %s가 $$수식$$%srm cm$$/수식$$일 때, 밑변의 길이와 높이의 합은 몇 $$수식$$rm cm$$/수식$$인가요?"%(
                area,stem_variable,stem_value
            )
    comment = "(해설)\n(평행사변형의 넓이) $$수식$$=$$/수식$$ (밑변의 길이) $$수식$$times$$/수식$$ (높이)\n"\
                "(%s) $$수식$$=$$/수식$$ (평행사변형의 넓이) $$수식$$div$$/수식$$ (%s)\n"\
                "$$수식$$= %s div %s = %s(rm cm)$$/수식$$\n"\
                "따라서 밑면의 길이와 높이의 합은\n"\
                "$$수식$$%s + %s = %s(rm cm)$$/수식$$입니다." %(
                    answer_variable,stem_variable,
                    area,stem_value,answer_value,
                    width,height,sumOfWidthHeight
                )
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(sumOfWidthHeight)
    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg

#5-1-6-54
def roundandarea516_Stem_012():
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
    width = random.randint(3,10)
    height = random.choice([4,6,8,10])
    area = int(width * height / 2)
    #draw
    triangle = new_p_triangle(width,height)
    triangle = resize(triangle)
    #points
    p_top = triangle[0]
    p_right = triangle[1]
    p_left = triangle[2]
    p_angle = (p_top[0],p_left[1])
    l_width = [p_left,p_right]
    l_height = [p_top,p_angle]
    #draw
    drawPolygon(ax,triangle)
    drawLine(ax,[p_left,p_angle],True)
    drawArc(ax,l_width,'bottom','$%s \mathrm{cm}$'%(width))
    drawLine(ax,l_height,True)
    drawArc(ax,l_height,'right','$%s \mathrm{cm}$'%(height))
    drawAngle(ax,[p_top,p_angle,p_left])
    #stem/comment/answer
    stem = "삼각형의 넓이는 몇 $$수식$$rm cm^{2}$$/수식$$ 인가요?"
    comment = "(해설)\n(삼각형의 넓이) $$수식$$=$$/수식$$ (밑변의 길이) $$수식$$times$$/수식$$ (높이) $$수식$$div 2$$/수식$$\n"\
                "$$수식$$= %s times %s div 2 = %s div 2 = %s (rm cm^{2})$$/수식$$입니다." %(
                    width,height,width*height,area
                )
    answer = '(답):$$수식$$%srm cm^{2}$$/수식$$'%(area)
    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg

#5-1-6-62,63
def roundandarea516_Stem_013():
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
        width = random.randint(3,15)
        height = random.randint(3,15)
        if (width*height)%2 == 0 and abs(width-height) < 6:
            break
    area = int(width * height / 2)
    #generate polygon
    rhombus = new_p_rhombus(width,height)
    rhombus = resize(rhombus)
    #points
    p_top = rhombus[0]
    p_right = rhombus[1]
    p_bottom = rhombus[2]
    p_left = rhombus[3]
    p_center = new_p_middle(p_top,p_bottom)
    #lines
    l_width = [p_left,p_right]
    l_height = [p_top,p_bottom]
    #draw
    drawLine(ax,l_width,True)
    drawArc(ax,[p_left,p_right],'bottom_l','$%s \mathrm{cm}$'%(width),color='cornflowerblue')
    drawLine(ax,l_height,True)
    drawArc(ax,[p_top,p_bottom],'right_t','$%s \mathrm{cm}$'%(height),color='cornflowerblue')
    drawAngle(ax,[p_top,p_center,p_left])
    drawPolygon(ax,rhombus)

    stem = "마름모의 넓이를 구해 보세요."
    comment = "(해설)\n(마름모의 넓이)\n"\
                "$$수식$$=$$/수식$$ (한 대각선의 길이)$$수식$$times$$/수식$$(다른 대각선의 길이)$$수식$$div 2$$/수식$$\n"\
                "$$수식$$= %s times %s div 2 = %s (rm cm^{2})$$/수식$$입니다." %(
                    width,height,area
                )
    answer = '(답):$$수식$$%srm cm^{2}$$/수식$$'%(area)
    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg

#5-1-6-65
def roundandarea516_Stem_014():
    stem_list = []
    char_list = ['①','②','③','④','⑤']
    while len(stem_list) < 4:
        random_num = random.randint(20,100)
        fact_num_list = fact_num_pair(random_num)
        if len(fact_num_list) >= 4:
            while len(stem_list) < 4:
                num1,num2 = random.choice(fact_num_list)
                if is_exist([num1,num2],stem_list): pass
                else: stem_list.append([num1,num2])
    answer_index = random.randint(0,4)
    random_temp_num = random.randint(2,5)
    answer_tuple = (abs(random_temp_num),int((random_num+random_whole(-5,5))/random_temp_num))
    stem_list.insert(answer_index,answer_tuple)
    random_num + random_temp_num
    #form stem
    stem = "마름모의 두 대각선의 길이입니다. 넓이가 다른 하나는 어느 것인가요?\n"
    for i in range(len(stem_list)):
        num1,num2 = stem_list[i]
        stem += '%s $$수식$$%srm cm$$/수식$$,$$수식$$%srm cm$$/수식$$  '%(char_list[i],num1,num2)
        if i == 1 or i == 3:
            stem += " \n"

    
    answer = '(답):%s'%char_list[answer_index]
    comment = "(해설)\n두 대각선의 곱이 다른 하나는 %s이므로 넓이가\n"\
                "다른 하나도 %s입니다." %(
                    char_list[answer_index],
                    char_list[answer_index]
                )
    return stem,answer,comment

#5-1-6-77
def roundandarea516_Stem_015():
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
    n = random.randint(2,5)
    length_bottom_l = random.randint(3,5)
    length_bottom_r = random.randint(7,10)
    length_top = length_bottom_l*(n-1)-length_bottom_r
    length_bottom = length_bottom_l + length_bottom_r
    while length_top >= length_bottom or length_top <= 3 or length_bottom_r <= length_top:
        n = random.randint(2,5)
        length_bottom_l = random.randint(3,5)
        length_bottom_r = random.randint(7,10)
        length_top = length_bottom_l*(n-1)-length_bottom_r
        length_bottom = length_bottom_l + length_bottom_r
    length_height = random.choice([4,6,8,10])
    area_triangle = int(length_height * length_bottom_l /2)
    area_trapezoid = int((length_top+length_bottom)*length_height/2)
    #generate polygon
    trapezoid = new_p_trapezoid_(length_top,length_bottom_l,length_bottom_r,length_height)
    trapezoid = resize(trapezoid)
    #point
    p_top_l = trapezoid[0]
    p_top_r = trapezoid[1]
    p_bottom_r = trapezoid[2]
    p_bottom_l = trapezoid[3]
    p_middle = (p_top_l[0],p_bottom_l[1])
    #line
    l_height = [p_top_l,p_middle]
    l_bottom_l = [p_bottom_l,p_middle]
    l_bottom_r = [p_middle,p_bottom_r]
    #angle
    a_middle = [p_top_l,p_middle,p_bottom_l]
    #draw
    drawPolygon(ax,trapezoid)
    setPoint(ax,trapezoid,['A','B','C','D'],['top','top','bottom','bottom'])
    setPoint(ax,[p_middle],['E'],['bottom'])
    drawLine(ax, l_height,True)
    drawArc(ax,l_height,'right','$%s \mathrm{cm}$'%(length_height),color='cornflowerblue')
    drawArc(ax,l_bottom_l,'bottom','$%s \mathrm{cm}$'%(length_bottom_l),color='cornflowerblue')
    drawArc(ax,l_bottom_r,'bottom','$%s \mathrm{cm}$'%(length_bottom_r),color='cornflowerblue')
    drawAngle(ax,a_middle)
    
    stem = "사다리꼴$$수식$$ABCD$$/수식$$의 넓이는 삼각형$$수식$$ADE$$/수식$$의 넓이의 $$수식$$%s$$/수식$$배입니다. 변$$수식$$AB$$/수식$$의 길이는 몇 $$수식$$rm cm$$/수식$$인가요?" %(n)
    comment = "(해설)\n(삼각형$$수식$$ADE$$/수식$$의 넓이) $$수식$$= %s times %s div 2 = %s (rm cm^{2})$$/수식$$\n"\
                "사다리꼴$$수식$$ABCD$$/수식$$의 넓이는 $$수식$$%s times %s = %s (rm cm^{2})$$/수식$$\n"\
                "입니다.\n"\
                "(사다리꼴$$수식$$ABCD$$/수식$$의 넓이)\n"\
                "$$수식$$={%s + %s +$$/수식$$ (변AB)$$수식$$} times %s div 2 = %s$$/수식$$에서\n"\
                "$$수식$${%s +$$/수식$$ (변AB)$$수식$$} times %s = %s$$/수식$$,\n"\
                "$$수식$$%s +$$/수식$$ (변AB) $$수식$$= %s$$/수식$$, (변 AB) $$수식$$= %s(rm cm)$$/수식$$입니다." %(
                    length_bottom_l,length_height,area_triangle,
                    area_triangle,n,area_trapezoid,
                    length_bottom_l,length_bottom_r,length_height,area_trapezoid,
                    length_bottom,length_height,area_trapezoid*2,
                    length_bottom,int(area_trapezoid*2/length_height),length_top
                )
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(length_top)
    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg
