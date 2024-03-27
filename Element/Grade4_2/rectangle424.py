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
def setPolygonPoint(ax,verts,points=list,text=[]):
    def find_text_position_polygonAngle(p_list,p):
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
        position = find_text_position_polygonAngle(verts,cp)
        drawText(ax,text[i],cp,position)
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
        drawText(ax,text[i],cp,position[i])
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
            elif angle != 90:
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
            #plt.text(points[i][0]-0.5, points[i][1]+0.1, text[i], fontsize=14, zorder=3)

            if fill:
                ax.plot(points[i][0], points[i][1],"k.", zorder=3)
    def drawText(ax,text='',xy=(0,0),position='top'):
        if len(xy) > 2: raise Exception("too many inputs for xy")
        l = len(str(text))
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
            plt.text(cp[0]+1+l*0.3, cp[1]+5, text, fontsize=16, zorder=3)
        elif position == 'top_l':
            plt.text(cp[0]+1-l*5, cp[1]+2, text, fontsize=16, zorder=3)
        elif position == 'bottom_r':
            plt.text(cp[0]+1+l*0.3, cp[1]-11, text, fontsize=16, zorder=3)
        elif position == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5, text, fontsize=16, zorder=3)
        else: raise Exception('no matching position')

    if len(verts) != len(show_angle) and show_angle != []: raise Exception("size of verts and size of show_angle don't match")
    if len(verts) != len(show_angle_num) and show_angle_num != []: raise Exception("size of verts and size of show_angle_num don't match")
    if len(verts) != len(show_point) and show_point != []: raise Exception("size of verts and size of show_point don't match")
    #draw angle/angle_num
    angle_sum = 0
    for i in range(len(verts)):
        first_index = (i-1) % (len(verts))
        second_index = (i) % (len(verts))
        third_index = (i+1) % (len(verts))
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
def drawAngle_(ax, p_list=[]):
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
            width = 0.3*d
            height = 0.3*d
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
        elif angle > 0 and angle < 180:
            if diff:
                if (i%2 == 1):
                    pp = mpatches.Arc(p2, angle=0, width=width*1.3, height=height*1.3, theta1=a1, theta2=a2, ec=color[i], zorder=3)
                else:
                    pp = mpatches.Arc(p2, angle=0, width=width*0.8, height=height*0.8, theta1=a1, theta2=a2, ec=color[i], zorder=3)
                ax.add_patch(pp)
            else:
                pp = mpatches.Arc(p2, angle=0, width=width, height=height, theta1=a1, theta2=a2, ec=color[i], zorder=3)
        else: raise Exception('wrong angle')

        ax.add_patch(pp)
        i += 1

# 직선
def drawLine(ax,pts,dash=False,color='black'):
    if dash: linestype = '--'
    else: linestype = '-'
    line_1 = matplotlib.lines.Line2D((pts[0][0],pts[1][0]), (pts[0][1],pts[1][1]), linewidth=1, linestyle = linestype,color=color)
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
            colors = yellow
        else:
            colors = [color]
            for i in range(len(polygon)-1):
                colors += [color]
    else:
        colors = random.choice([blue,orange,purple,green,yellow])
    for i in range(len(polygon)):
        verts = polygon[i]
        if len(verts) == 2:
            drawLine(ax,verts,dash=dash,color='gray',alpha=alpha)
            continue

        
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


# 다각형 + 각 + Text
def drawPolygonAngle(ax, verts=list, show_angle=[], show_angle_num=[], show_point=[]):
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
    def find_text_position_polygonAngle(p_list,p):
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
            position = find_text_position_polygonAngle(verts,angle_p)
            if show_angle_num[second_index] == True: drawText(ax,'$%s\mathrm{°}$'%(angle_num),angle_p,position)
            elif show_angle_num[second_index] == False: pass
            else: raise Exception("Invalid input")
        #point_text
        if show_point != []:
            text_p = verts[second_index]
            text = show_point[second_index]
            position = find_text_position_polygonAngle(verts,text_p)
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
def drawText(ax,text='',cp=(0,0),position='top'):
    if len(cp) > 2: raise Exception("too many inputs for cp")
    l = len(str(text))
    if 'mathrm' in text:
        l -= 10
    if position == 'top':
        plt.text(cp[0]-l*3, cp[1]+1, text, fontsize=16, zorder=3)
    elif position == 'bottom':
        plt.text(cp[0]-2*l, cp[1]-10, text, fontsize=16, zorder=3)
    elif position == 'left':
        plt.text(cp[0]-2-l*7, cp[1]-2, text, fontsize=16, zorder=3)
    elif position == 'right':
        plt.text(cp[0]+l, cp[1]-2, text, fontsize=16, zorder=3)
    elif position == 'top_r':
        plt.text(cp[0]+l*0.3, cp[1]+1, text, fontsize=16, zorder=3)
    elif position == 'top_l':
        plt.text(cp[0]-l*7, cp[1]+1, text, fontsize=16, zorder=3)
    elif position == 'bottom_r':
        plt.text(cp[0]+l*0.3, cp[1]-10, text, fontsize=16, zorder=3)
    elif position == 'bottom_l':
        plt.text(cp[0]-l*7, cp[1]-10, text, fontsize=16, zorder=3)
    else: raise Exception('no matching position')

# 선분의 길이를 표시하는 bezier 곡선을 그리는 함수
def drawArc(ax, p1, p2, position, text, boxed=False):
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
        Path.CURVE3
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
            plt.text(cp[0]-5*l, cp[1]+1, text, fontsize=16, zorder=3)
        elif position == 'bottom':
            plt.text(cp[0]-5*l, cp[1]-5, text, fontsize=16, zorder=3)
        elif position == 'left':
            plt.text(cp[0]-l*8, cp[1]-2, text, fontsize=16, zorder=3)
        elif position == 'right':
            plt.text(cp[0]+l, cp[1]-2, text, fontsize=16, zorder=3)
        elif position in ['top_r','right_t']:
            plt.text(cp[0]+l, cp[1]+2, text, fontsize=16, zorder=3)
        elif position in ['top_l','left_t']:
            plt.text(cp[0]-l*8, cp[1]+2, text, fontsize=16, zorder=3)
        elif position in ['bottom_r','right_b']:
            plt.text(cp[0]+l, cp[1]-8+l*0.5, text, fontsize=16, zorder=3)
        elif position in ['bottom_l','left_b']:
            plt.text(cp[0]-l*8, cp[1]-8+l*0.5, text, fontsize=16, zorder=3)
        else: raise Exception('no matching position')
def drawPolygonArc(ax,verts=list,show_length=[],show_text=[],length_ratio=10,unit='cm'):
    def drawArc(ax, p1, p2, position, text, boxed=False):
        if 'top' in position: cp = find_controlPoint_arc(p1,p2,'top')
        elif 'bottom' in position: cp = find_controlPoint_arc(p1,p2,'bottom')
        elif 'right' in position: cp = find_controlPoint_arc(p1,p2,'right')
        elif 'left' in position: cp = find_controlPoint_arc(p1,p2,'left')


        p1 = (round(p1[0],5),round(p1[1],5))
        p2 = (round(p2[0],5),round(p2[1],5))
        l = len(text)
        if 'mathrm' in text: 
            l -= 11
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

        pp = mpatches.PathPatch(path, fc="none", transform=ax.transData, linestyle="--", zorder=3)
        ax.add_patch(pp)
        if position == 'top':
            plt.text(cp[0]-5*l, cp[1]+1, text, fontsize=16, zorder=3)
        elif position == 'bottom':
            plt.text(cp[0]-5*l, cp[1]-7, text, fontsize=16, zorder=3)
        elif position == 'left':
            plt.text(cp[0]-l*8, cp[1]-2, text, fontsize=16, zorder=3)
        elif position == 'right':
            plt.text(cp[0]+l, cp[1]-2, text, fontsize=16, zorder=3)
        elif position in ['top_r','right_t']:
            plt.text(cp[0]+l, cp[1]+2, text, fontsize=16, zorder=3)
        elif position in ['top_l','left_t']:
            plt.text(cp[0]-l*8, cp[1]+2, text, fontsize=16, zorder=3)
        elif position in ['bottom_r','right_b']:
            plt.text(cp[0]+l, cp[1]-8+l*0.5, text, fontsize=16, zorder=3)
        elif position in ['bottom_l','left_b']:
            plt.text(cp[0]-l*8, cp[1]-8+l*0.5, text, fontsize=16, zorder=3)
        else: raise Exception('no matching position')
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
        elif x >= x_center: #right
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
            
        return position
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
        position = find_text_position_polygonArc(verts,[p1,p2])
        length = int(c_distance(p1,p2)/length_ratio)
        if show_length != []:
            if show_length[i] == True:
                drawArc(ax,p1,p2,position,'$%s\mathrm{%s}$'%(length,unit))
        if show_text != []: 
            if show_text[i] != '':
                drawArc(ax,p1,p2,position,show_text[i])


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


def resize(p_list=list,scale=100):
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

    angle = a2 -a1
    if angle < 0:
        angle = 360 + angle
    angle = int(angle)
    if (angle%5) == 4:
        angle += 1
    else:
        angle = angle - (angle%5)
    return angle
def calculate_distance(p1=tuple, p2=tuple):
    import math
    d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    return d

def create_p_angle(angle,length,p=[0,0]):
    import math
    angle_radiant = math.radians(angle)
    x = round((math.cos(angle_radiant)*length),5) + p[0]
    y = round((math.sin(angle_radiant)*length),5) + p[1]
    return (x,y)
def find_p_in_2lines(l1,l2):
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
    def find_y_linear_equation(eq,x=None):
        if eq[0] in ['y']:
            return eq[1]
        elif eq[0] in ['x']:
            raise Exception("Invalid")
        slope,y_intersect = eq
        return slope*x + y_intersect
    def find_x_linear_equation(eq,y=None):
        if eq[0] in ['x']:
            pass
        elif eq[0] in ['y']:
            raise Exception("Invalid")
        slope, y_intersect = eq
        return (y-y_intersect)/slope
    eq1 = find_linear_equation(l1[0],l1[1])
    eq2 = find_linear_equation(l2[0],l2[1])
    slope1,y_intersect1 = eq1
    slope2,y_intersect2 = eq2
    if slope1 in ['x','y'] and slope2 in ['x','y']:
        if slope1 == slope2:
            raise Exception("Two lines are parallel")
        else:
            if slope1 == 'x':
                return (y_intersect1,y_intersect2)
            elif slope1 == 'y':
                return (y_intersect2,y_intersect1)
    elif slope1 in ['x','y']: #x=a,y=a
        if slope1 == 'x':
            x = y_intersect1
            y = find_y_linear_equation(eq2,x)
        elif slope1 == 'y':
            y = y_intersect1
            x = find_x_linear_equation(eq2,y)
    elif slope2 in ['x','y']: #x=a,y=a
        if slope2 == 'x':
            x = y_intersect2
            y = find_y_linear_equation(eq1,x)
        elif slope2 == 'y':
            y = y_intersect2
            x = find_x_linear_equation(eq1,y)
    else: #normal case
        x = (y_intersect2 - y_intersect1)/(slope1-slope2)
        y = find_y_linear_equation(eq1,x)
    return (x,y)

def new_p_rectangle_right_angle(scale=100,position='bottom_l',move_x=0,move_y=0):
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
    top_left_p = (random.randint(10,scale)*-1,random.randint(10,scale))
    top_right_p = (random.randint(10,scale),random.randint(10,scale))
    bottom_right_p = (random.randint(10,scale),random.randint(10,scale)*-1)
    bottom_left_p = (random.randint(10,scale)*-1,random.randint(10,scale)*-1)
    #right angle on one side
    if position == 'top_l':
        top_left_p = (random.randint(10,scale)*-1,random.randint(10,scale))
        top_right_p = (random.randint(10,scale),top_left_p[1])
        bottom_left_p = (top_left_p[0],random.randint(10,scale)*-1)
        bottom_right_p = (random.randint(1,scale),random.randint(1,scale)*-1)
    elif position == 'top_r':
        top_right_p = (random.randint(10,scale),random.randint(10,scale))
        top_left_p = (random.randint(10,scale)*-1,top_right_p[1])
        bottom_right_p = (top_right_p[0],random.randint(10,scale)*-1)
        bottom_left_p = (random.randint(10,scale)*-1,random.randint(10,scale)*-1)
    elif position == 'bottom_r':
        bottom_right_p = (random.randint(10,scale),random.randint(10,scale)*-1)
        bottom_left_p = (random.randint(10,scale)*-1,bottom_right_p[1])
        top_right_p = (bottom_right_p[0],random.randint(10,scale))
        top_left_p = (random.randint(10,scale)*-1,random.randint(10,scale))
    elif position == 'bottom_l':
        bottom_left_p = (random.randint(10,scale)*-1,random.randint(10,scale)*-1)
        bottom_right_p = (random.randint(10,scale),bottom_left_p[1])
        top_left_p = (bottom_left_p[0],random.randint(1,scale))
        top_right_p = (random.randint(10,scale),random.randint(10,scale))
    else: raise Exception('Invalid position')
    rectangle = [top_left_p,top_right_p,bottom_right_p,bottom_left_p]
    rectangle = move_to_center(rectangle)
    rectangle = move_p(rectangle,move_x,move_y)
    return rectangle
def new_p_trapezoid_(scale=100,position='left',move_x=0,move_y=0):
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
    top_left_p = (random.randint(10,scale)*-1,random.randint(10,scale))
    top_right_p = (random.randint(10,scale),random.randint(10,scale))
    bottom_right_p = (random.randint(10,scale),random.randint(10,scale)*-1)
    bottom_left_p = (random.randint(10,scale)*-1,random.randint(10,scale)*-1)
    #right angle on one side
    if position == 'top':
        top_left_p = (random.randint(10,scale)*-1,random.randint(10,scale))
        top_right_p = (random.randint(10,scale),top_left_p[1])
        bottom_left_p = (top_left_p[0],random.randint(10,scale)*-1)
        bottom_right_p = (top_right_p[0],random.randint(1,scale)*-1)
        while abs(bottom_right_p[1] - bottom_left_p[1]) < 20:
            bottom_right_p = (top_right_p[0],random.randint(1,scale)*-1)
    elif position == 'right':
        top_right_p = (random.randint(10,scale),random.randint(10,scale))
        top_left_p = (random.randint(10,scale)*-1,top_right_p[1])
        bottom_right_p = (top_right_p[0],random.randint(10,scale)*-1)
        bottom_left_p = (random.randint(10,scale)*-1,bottom_right_p[1])
        while abs(bottom_left_p[0] - top_left_p[0]) < 20:
            bottom_left_p = (random.randint(10,scale)*-1,bottom_right_p[1])
    elif position == 'bottom':
        bottom_right_p = (random.randint(10,scale),random.randint(10,scale)*-1)
        bottom_left_p = (random.randint(10,scale)*-1,bottom_right_p[1])
        top_right_p = (bottom_right_p[0],random.randint(10,scale))
        top_left_p = (bottom_left_p[0],random.randint(10,scale))
        while abs(top_right_p[1] - top_left_p[1]) < 20:
            top_left_p = (bottom_left_p[0],random.randint(10,scale))
    elif position == 'left':
        bottom_left_p = (random.randint(10,scale)*-1,random.randint(10,scale)*-1)
        bottom_right_p = (random.randint(10,scale),bottom_left_p[1])
        top_left_p = (bottom_left_p[0],random.randint(10,scale))
        top_right_p = (random.randint(10,scale),top_left_p[1])
        while abs(top_right_p[0] - bottom_right_p[0]) < 20:
            top_right_p = (random.randint(10,scale),top_left_p[1])
    else: raise Exception('Invalid position')
    rectangle = [top_left_p,top_right_p,bottom_right_p,bottom_left_p]
    rectangle = move_to_center(rectangle)
    rectangle = move_p(rectangle,move_x,move_y)
    return rectangle
def new_p_trapezoid(scale=100,position='top',move_x=0,move_y=0):
    import random
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
    top_left_p = (random.randint(10,scale)*-1,random.randint(10,scale))
    top_right_p = (random.randint(10,scale),random.randint(10,scale))
    bottom_right_p = (random.randint(10,scale),random.randint(10,scale)*-1)
    bottom_left_p = (random.randint(10,scale)*-1,random.randint(10,scale)*-1)
    top_left_num_angle = int(c_angle([bottom_left_p,top_left_p,top_right_p]))
    top_left_num_angle = top_left_num_angle - (top_left_num_angle%5)
    bottom_left_num_angle = 180 - top_left_num_angle
    top_right_num_angle = int(c_angle([top_left_p,top_right_p,bottom_right_p]))
    top_right_num_angle = top_right_num_angle - (top_right_num_angle%5)
    bottom_right_num_angle = 180 - top_right_num_angle
    while 90 in [top_left_num_angle, top_right_num_angle,bottom_right_num_angle,bottom_left_num_angle]:
        top_left_p = (random.randint(10,scale)*-1,random.randint(10,scale))
        top_right_p = (random.randint(10,scale),random.randint(10,scale))
        bottom_right_p = (random.randint(10,scale),random.randint(10,scale)*-1)
        bottom_left_p = (random.randint(10,scale)*-1,random.randint(10,scale)*-1)
        top_left_num_angle = int(c_angle([bottom_left_p,top_left_p,top_right_p]))
        top_left_num_angle = top_left_num_angle - (top_left_num_angle%5)
        bottom_left_num_angle = 180 - top_left_num_angle
        top_right_num_angle = int(c_angle([top_left_p,top_right_p,bottom_right_p]))
        top_right_num_angle = top_right_num_angle - (top_right_num_angle%5)
        bottom_right_num_angle = 180 - top_right_num_angle
    #parallel on which side
    if position == 'top' or position == 'bottom': #up/down
        top_left_p = (random.randint(10,scale)*-1,random.randint(10,scale))
        top_right_p = (random.randint(10,scale),top_left_p[1])
        bottom_left_p = (random.randint(10,scale)*-1,random.randint(10,scale)*-1)
        bottom_right_p = (random.randint(10,scale),bottom_left_p[1])
        while abs((top_right_p[0]-top_left_p[0]) - (bottom_right_p[0]-bottom_left_p[0])) < 20:
            top_left_p = (random.randint(10,scale)*-1,random.randint(10,scale))
            top_right_p = (random.randint(10,scale),top_left_p[1])
            bottom_left_p = (random.randint(10,scale)*-1,random.randint(10,scale)*-1)
            bottom_right_p = (random.randint(10,scale),bottom_left_p[1])
    elif position == 'right' or position == 'left': #left/right
        top_right_p = (random.randint(10,scale),random.randint(10,scale))
        bottom_right_p = (top_right_p[0],random.randint(10,scale)*-1)
        top_left_p = (random.randint(10,scale)*-1,random.randint(10,scale))
        bottom_left_p = (top_left_p[0],random.randint(10,scale)*-1)
        while abs((top_right_p[1]-bottom_right_p[1]) - (top_left_p[1]-bottom_left_p[1])) < 20:
            top_right_p = (random.randint(10,scale),random.randint(10,scale))
            bottom_right_p = (top_right_p[0],random.randint(10,scale)*-1)
            top_left_p = (random.randint(10,scale)*-1,random.randint(10,scale))
            bottom_left_p = (top_left_p[0],random.randint(10,scale)*-1)
    else: raise Exception('Invalid position')
    rectangle = [top_left_p,top_right_p,bottom_right_p,bottom_left_p]
    rectangle = move_to_center(rectangle)
    rectangle = move_p(rectangle,move_x,move_y)
    return rectangle
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
    while True:
        angle1_5 = random.randint(6,30)
        angle1 = angle1_5*5
        if not(80 < angle1 and angle1 < 100):
            break
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
def new_p_rhombus(scale=100,move_x=0,move_y=0):
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
    #angle1,angle2
    angle1_5 = random.randint(6,30)
    while angle1_5 <= 18:
        angle1_5 = random.randint(6,30)
    angle2_5 = 36 - angle1_5
    angle1 = angle1_5*5
    angle2 = angle2_5*5
    #lengh1,length2
    length1 = random.randint(3,9)
    length2 = length1
    #points
    bottom_left_p = (0,0)
    bottom_right_p = (length2,0)
    top_left_p = new_p_angle(angle1,length1)
    top_right_p = new_p_angle(angle1,length1,bottom_right_p)

    rectangle = [top_left_p,top_right_p,bottom_right_p,bottom_left_p]
    rectangle = move_to_center(rectangle)
    rectangle = move_p(rectangle,move_x,move_y)
    if angle1 > angle2:
        rectangle = rotate_p(rectangle,min(angle1,angle2)/2)
    else:
        rectangle = rotate_p(rectangle,min(angle1,angle2)/-2)
    return rectangle
def create_p_parallelogram(left_angle=0,side=0,width=0,scale=100,move_x=0,move_y=0):
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
    #lengh
    if side == 0 or width == 0:
        side = random.randint(5,9)
        width = random.randint(5,9)
    #points
    p_bottom_l = (0,0)
    p_bottom_r = (width,0)
    p_top_l = new_p_angle(left_angle,side)
    p_top_r = new_p_angle(left_angle,side,p_bottom_r)

    parallelogram = [p_top_l,p_top_r,p_bottom_r,p_bottom_l]
    parallelogram = move_p(parallelogram,move_x,move_y)
    return parallelogram
def create_p_trapezoid_right_angle(position='left',scale=100,move_x=0,move_y=0):
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
    top_left_p = (random.randint(10,scale)*-1,random.randint(10,scale))
    top_right_p = (random.randint(10,scale),random.randint(10,scale))
    bottom_right_p = (random.randint(10,scale),random.randint(10,scale)*-1)
    bottom_left_p = (random.randint(10,scale)*-1,random.randint(10,scale)*-1)
    #right angle on one side
    if position == 'top':
        top_left_p = (random.randint(10,scale)*-1,random.randint(10,scale))
        top_right_p = (random.randint(10,scale),top_left_p[1])
        bottom_left_p = (top_left_p[0],random.randint(10,scale)*-1)
        bottom_right_p = (top_right_p[0],random.randint(1,scale)*-1)
        while abs(bottom_right_p[1] - bottom_left_p[1]) < 20:
            bottom_right_p = (top_right_p[0],random.randint(1,scale)*-1)
    elif position == 'right':
        top_right_p = (random.randint(10,scale),random.randint(10,scale))
        top_left_p = (random.randint(10,scale)*-1,top_right_p[1])
        bottom_right_p = (top_right_p[0],random.randint(10,scale)*-1)
        bottom_left_p = (random.randint(10,scale)*-1,bottom_right_p[1])
        while abs(bottom_left_p[0] - top_left_p[0]) < 20:
            bottom_left_p = (random.randint(10,scale)*-1,bottom_right_p[1])
    elif position == 'bottom':
        bottom_right_p = (random.randint(10,scale),random.randint(10,scale)*-1)
        bottom_left_p = (random.randint(10,scale)*-1,bottom_right_p[1])
        top_right_p = (bottom_right_p[0],random.randint(10,scale))
        top_left_p = (bottom_left_p[0],random.randint(10,scale))
        while abs(top_right_p[1] - top_left_p[1]) < 20:
            top_left_p = (bottom_left_p[0],random.randint(10,scale))
    elif position == 'left':
        bottom_left_p = (random.randint(10,scale)*-1,random.randint(10,scale)*-1)
        bottom_right_p = (random.randint(10,scale),bottom_left_p[1])
        top_left_p = (bottom_left_p[0],random.randint(10,scale))
        top_right_p = (random.randint(10,scale),top_left_p[1])
        while abs(top_right_p[0] - bottom_right_p[0]) < 20:
            top_right_p = (random.randint(10,scale),top_left_p[1])
    else: raise Exception('Invalid position')
    rectangle = [top_left_p,top_right_p,bottom_right_p,bottom_left_p]
    rectangle = move_to_center(rectangle)
    rectangle = move_p(rectangle,move_x,move_y)
    return rectangle


#4-2-4-05
def rectangle424_Stem_001():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #create rectangle, answer/stem lines
    random_side = random.randint(0,3)
    if random_side == 0: #top_l
        position = 'top_l'
        if random.randint(0,1):
            stem_line = 'AB'
            answer_line = 'AD'
        else:
            stem_line = 'AD'
            answer_line = 'AB'
    elif random_side == 1: #top_r
        position = 'top_r'
        if random.randint(0,1):
            stem_line = 'AB'
            answer_line = 'BC'
        else:
            stem_line = 'BC'
            answer_line = 'AB'
    elif random_side == 2: #bottom_r
        position = 'bottom_r'
        if random.randint(0,1):
            stem_line = 'BC'
            answer_line = 'CD'
        else:
            stem_line = 'CD'
            answer_line = 'BC'
    elif random_side == 3: #bottom_l
        position = 'bottom_l'
        if random.randint(0,1):
            stem_line = 'AD'
            answer_line = 'CD'
        else:
            stem_line = 'CD'
            answer_line = 'AD'
    rectangle = new_p_rectangle_right_angle(position=position)
    rectangle = resize(rectangle,80)
    drawPolygon(ax,rectangle)
    #draw point
    setPoint(ax,rectangle,['A','B','C','D'],['left','right','right','left'])
    #point
    top_l_p = rectangle[0]
    top_r_p = rectangle[1]
    bottom_r_p = rectangle[2]
    bottom_l_p = rectangle[3]
    #form stem/answer
    stem = "변$$수식$$%s$$/수식$$와 서로 수직인 변은 어느 것인가요?\n" %(stem_line)
    line_list = ['AB','BC','CD','AD']
    char_list = ['①','②','③','④']
    for i in range(len(line_list)):
        line = line_list[i]
        if line == stem_line:
            line_list.remove(line)
            break
    line_list.sort()
    for i in range(len(line_list)):
        line = line_list[i]
        stem += char_list[i] + ' 변$$수식$$%s$$/수식$$  ' %(line)
        if line == answer_line:
            answer_num = char_list[i]
    
    comment = "(해설)\n변$$수식$$%s$$/수식$$와 만나서 이루는 각이 직각인 변은\n"\
                "변$$수식$$%s$$/수식$$입니다."%(
                    stem_line,
                    answer_line
                )
    answer = '(답):%s'%(answer_num)
    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg

#4-2-4-11
def rectangle424_Stem_002():
    stem = "도형에서 서로 평행한 변은 어느 것인가요?\n"
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #create rectangle, answer/stem lines
    stem_list = [['AD','BC'],['AB','CD'],['AB','BC'],['BC','CD'],['CD',"AD"]]
    random.shuffle(stem_list)
    random_side = random.randint(0,3)
    if random_side == 0: #top
        position = 'top'
        answer_list = ['AD','BC']
        stem_line = 'AB'
    elif random_side == 1: #right
        position = 'right'
        answer_list = ['AB','CD']
        stem_line = 'BC'
    elif random_side == 2: #bottom
        position = 'bottom'
        answer_list = ['AD','BC']
        stem_line = 'CD'
    elif random_side == 3: #left
        position = 'left'
        answer_list = ['AB','CD']
        stem_line = 'AD'
    rectangle = new_p_trapezoid_(position=position)
    rectangle = resize(rectangle,90)
    drawPolygon(ax,rectangle)
    #draw point
    setPoint(ax,rectangle,['A','B','C','D'],['left','right','right','left'])
    
    #form stem/answer
    char_list = ['①','②','③','④','⑤']
    for i in range(len(stem_list)):
        lines = stem_list[i]
        stem += '%s 변$$수식$$%s$$/수식$$,변$$수식$$%s$$/수식$$   '%(char_list[i],lines[0],lines[1])
        if lines == answer_list:
            answer = char_list[i]
        if i in [1,3]:
            stem += '\n'
    comment = "(해설)\n변$$수식$$%s$$/수식$$와 변$$수식$$%s$$/수식$$는 변$$수식$$%s$$/수식$$에 수직이므로\n"\
                "변$$수식$$%s$$/수식$$와 변$$수식$$%s$$/수식$$는 서로 평행합니다." %(
                    answer_list[0],answer_list[1],stem_line,
                    answer_list[0],answer_list[1]
                    )
    answer = '(답):%s'%(answer)
    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg

#4_2_4_23
def rectangle424_Stem_003():
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
    right_angle_position = random.choice(['top','bottom','right','left'])
    #generate polygon
    while True:
        trapezoid = create_p_trapezoid_right_angle(right_angle_position)
        trapezoid = resize(trapezoid)
        #point
        p_top_l = trapezoid[0]
        p_top_r = trapezoid[1]
        p_bottom_r = trapezoid[2]
        p_bottom_l = trapezoid[3]
        if right_angle_position == 'top':
            l_answer = [p_top_l,p_top_r]
            l_answer_opposite = [p_bottom_l,p_bottom_r]
        elif right_angle_position == 'right':
            l_answer = [p_top_r,p_bottom_r]
            l_answer_opposite = [p_top_l,p_bottom_l]
        elif right_angle_position == 'bottom':
            l_answer = [p_bottom_l,p_bottom_r]
            l_answer_opposite = [p_top_l,p_top_r]
        elif right_angle_position == 'left':
            l_answer = [p_top_l,p_bottom_l]
            l_answer_opposite = [p_top_r,p_bottom_r]
        len_answer = int(calculate_distance(l_answer[0],l_answer[1])/10)
        len_answer_opposite = int(calculate_distance(l_answer_opposite[0],l_answer_opposite[1])/10)
        tooDifferent = abs(calculate_distance(p_top_l,p_top_r) - calculate_distance(p_top_l,p_bottom_l)) > 70\
            or abs(calculate_distance(p_top_l,p_bottom_l) - calculate_distance(p_bottom_l,p_bottom_r)) > 70
        if len_answer < len_answer_opposite and not(tooDifferent):
            break
    #draw
    drawPolygon(ax,trapezoid)
    setPolygonPoint(ax,trapezoid,trapezoid,['A','B','C','D'])
    if right_angle_position == 'top':
        drawPolygonAngle_(ax,trapezoid,[1,1,0,0])
        drawPolygonArc(ax,trapezoid,[1,1,1,1])
        l_name_comment = ['AD','BC','AB']
    elif right_angle_position == 'bottom':
        drawPolygonAngle_(ax,trapezoid,[0,0,1,1])
        drawPolygonArc(ax,trapezoid,[1,1,1,1])
        l_name_comment = ['AD','BC','CD']
    elif right_angle_position == 'right':
        drawPolygonAngle_(ax,trapezoid,[0,1,1,0])
        drawPolygonArc(ax,trapezoid,[1,1,1,1])
        l_name_comment = ['AB','CD','BC']
    elif right_angle_position == 'left':
        drawPolygonAngle_(ax,trapezoid,[1,0,0,1])
        drawPolygonArc(ax,trapezoid,[1,1,1,1])
        l_name_comment = ['AB','CD','AD']
    
    stem = "도형에서 평행선 사이의 거리를 구해 보세요."
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(len_answer)
    comment = "(해설)\n평행선은 변$$수식$$%s$$/수식$$와 변$$수식$$%s$$/수식$$입니다.\n"\
                "평행선 사이의 거리는 두 변에 수직인 변$$수식$$%s$$/수식$$의\n"\
                "길이인 $$수식$$%srm cm$$/수식$$입니다." %(
                    l_name_comment[0],l_name_comment[1],
                    l_name_comment[2],
                    len_answer
                    )
    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg

#4_2_4_29
def rectangle424_Stem_004():
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
        angle_right = random.randint(7,14)*5
        angle_middle = random.randint(10,14)*5
        angle_left = 180 - (angle_right+angle_middle)
        if angle_right != 90 and angle_middle != 90 and angle_left < 90:
            break
    #generate shapes
    p_center = (0,0)
    l_top = [(-70,50),(70,50)]
    l_top_ = [(-70,60),(70,60)]
    l_bottom = [(-70,0),(70,0)]
    p_right = create_p_angle(angle_right,70,p_center)
    p_left = create_p_angle(angle_middle,70,p_center)
    p_left = rotate_p([p_left],angle_middle)[0]
    l_right = [p_center,p_right]
    l_left = [p_center,p_left]
    p_left = find_p_in_2lines(l_top_,l_left)
    p_right = find_p_in_2lines(l_top_,l_right)
    l_left = [p_center,p_left]
    l_right = [p_center,p_right]
    p_C = find_p_in_2lines(l_top,l_left)
    p_E = find_p_in_2lines(l_top,l_right)
    l_top = [(p_left[0]-30,l_top[0][1]),(p_right[0]+30,l_top[0][1])]
    l_bottom = [(l_top[0][0],0),(l_top[1][0],0)]
    p_comment = (p_C[0],l_bottom[0][1])
    l_comment = [p_comment,p_C]
    angle_left = calculate_angle([p_center,p_C,p_E])
    angle_middle = calculate_angle([p_E,p_center,p_C])
    angle_right = calculate_angle([(p_center[0]+10,p_center[1]),p_center,p_E])
    #draw shapes
    drawText(ax,'A',l_top[0],'left')
    drawText(ax,'B',l_bottom[0],'left')
    if angle_right > 55: move_x1 = 20
    elif angle_right < 40: move_x1 = 30
    else: move_x1 = 25
    if angle_left > 55: move_x2 = 15
    else: move_x2 = 20
    drawText(ax,'$%s \mathrm{°}$'%(angle_right),(p_center[0]+move_x1,p_center[1]+1),'top')
    drawText(ax,'$%s \mathrm{°}$'%(angle_left),(p_C[0]+move_x2,p_C[1]-1),'bottom')
    setPoint(ax,[p_C,p_E,p_center],['C','E','D'],['top_r','top_l','bottom'])
    drawAngle(ax,[[p_center,p_C,p_E],[p_E,p_center,p_C],[(p_center[0]+10,p_center[1]),p_center,p_E]],True)
    drawLine_multiple(ax,[l_top,l_bottom])
    drawLine_multiple(ax,[l_right,l_left])
    plt.axis('scaled')
    svg_stem = saveSvg()
    drawLine(ax,l_comment,color='blue')
    drawAngle(ax,[[p_center,p_comment,p_C]])
    drawText(ax,'F',p_comment,'bottom')
    plt.axis('scaled')
    svg_comment = saveSvg()

    stem = "직선$$수식$$A$$/수식$$와 직선$$수식$$B$$/수식$$는 서로 평행합니다. 각$$수식$$CDE$$/수식$$는 몇 도인가요?\n" \
        "$$수식$$ ANGLE CDE = $$/수식$$ {box} $$수식$$rm °$$/수식$$"
            
    answer = "(답):$$수식$$%s$$/수식$$"%(angle_middle)
    comment = "(해설)\n점$$수식$$C$$/수식$$에서 직선$$수식$$B$$/수식$$에 수선을 그었을 때 직선$$수식$$B$$/수식$$와\n"\
                "만나는 점을 점$$수식$$F$$/수식$$라 하면 평행선과 수선이\n"\
                "만나서 이루는 각의 크기는 $$수식$$90rm °$$/수식$$이므로\n"\
                "(각$$수식$$FCE$$/수식$$) $$수식$$= 90rm °$$/수식$$, (각$$수식$$FCD$$/수식$$) $$수식$$= 90rm ° - %srm ° = %srm °$$/수식$$\n"\
                "입니다.\n"\
                "$$수식$$삼각형CFD$$/수식$$에서\n"\
                "(각$$수식$$CDF$$/수식$$) $$수식$$= 180rm ° - %srm ° - 90rm ° = %srm °$$/수식$$입니다.\n"\
                "한 직선이 이루는 각의 크기는 $$수식$$180rm °$$/수식$$이므로\n"\
                "(각$$수식$$CDE$$/수식$$) $$수식$$= 180rm ° - %srm ° - %srm ° = %srm °$$/수식$$입니다."%(
                    angle_left, (90-angle_left),
                    (90-angle_left), angle_left,
                    angle_left, angle_right, angle_middle
                )
    #plt.show()
    box = "$$수식$$box{　　}$$/수식$$"
    stem = stem.format(box=box)
    return stem, answer, comment, [svg_stem,svg_comment]

#4-2-4-34
def rectangle424_Stem_005():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #draw trapezoid
    #point
    #angle/num_angle
    while True:
        trapezoid = new_p_trapezoid()
        trapezoid = resize(trapezoid,90)
        top_left_p = trapezoid[0]
        top_right_p = trapezoid[1]
        bottom_right_p = trapezoid[2]
        bottom_left_p = trapezoid[3]
        top_left_angle = [bottom_left_p,top_left_p,top_right_p]
        top_right_angle = [top_left_p,top_right_p,bottom_right_p]
        bottom_right_angle = [top_right_p,bottom_right_p,bottom_left_p]
        bottom_left_angle = [bottom_right_p,bottom_left_p,top_left_p]
        top_left_num_angle = int(calculate_angle(top_left_angle))
        top_left_num_angle = top_left_num_angle - (top_left_num_angle%5)
        bottom_left_num_angle = 180 - top_left_num_angle
        top_right_num_angle = int(calculate_angle(top_right_angle))
        top_right_num_angle = top_right_num_angle - (top_right_num_angle%5)
        bottom_right_num_angle = 180 - top_right_num_angle
        noRightAngle = top_right_num_angle != 90 and\
                        top_left_num_angle != 90 and\
                        bottom_right_num_angle != 90 and\
                        bottom_left_num_angle != 90
        if noRightAngle:
            break
    #draw
    drawPolygon(ax,trapezoid)
    position_leftRight = random.randint(0,1)
    position_topBottom = random.randint(0,1)
    if position_leftRight: #left_side
        drawAngle_(ax,bottom_left_angle)
        drawAngle_(ax,top_left_angle)
        if position_topBottom: #answer - top_left
            answer_num = top_left_num_angle
            stem_num = bottom_left_num_angle
            drawText(ax,'%s'%('A'),top_left_p,'top')
            drawText(ax,'$%s\mathrm{°}$'%(bottom_left_num_angle),bottom_left_p,'bottom')
        else: #answer - bottom_left'
            answer_num = bottom_left_num_angle
            stem_num = top_left_num_angle
            drawText(ax,'%s'%('A'),bottom_left_p,'bottom')
            drawText(ax,'$%s\mathrm{°}$'%(top_left_num_angle),top_left_p,'top')
    else: #right_sde
        drawAngle_(ax,top_right_angle)
        drawAngle_(ax,bottom_right_angle)
        if position_topBottom: #answer - top_right
            answer_num = top_right_num_angle
            stem_num = bottom_right_num_angle
            drawText(ax,'%s'%('A'),top_right_p,'top')
            drawText(ax,'$%s\mathrm{°}$'%(bottom_right_num_angle),bottom_right_p,'bottom')
        else: #answer - bottom_right
            answer_num = bottom_right_num_angle
            stem_num = top_right_num_angle
            drawText(ax,'%s'%('A'),bottom_right_p,'bottom')
            drawText(ax,'$%s\mathrm{°}$'%(top_right_num_angle),top_right_p,'top')
    plt.axis('scaled')
    svg = saveSvg()

    if position_leftRight: #left_side
        if top_right_p[0] < bottom_right_p[0]:
            comment_p= (top_right_p[0],bottom_right_p[1])
            drawLine(ax,[(top_right_p),comment_p])
            drawAngle_(ax,[top_left_p,top_right_p,comment_p])
            drawAngle_(ax,[top_right_p,comment_p,bottom_left_p])
        else:
            comment_p= (bottom_right_p[0],top_right_p[1])
            drawLine(ax,[(bottom_right_p),comment_p])
            drawAngle_(ax,[comment_p,bottom_right_p,bottom_left_p])
            drawAngle_(ax,[top_left_p,comment_p,bottom_right_p])
    else: #right_sde
        if top_left_p[0] > bottom_left_p[0]:
            comment_p = (top_left_p[0],bottom_left_p[1])
            drawLine(ax,[(top_left_p),comment_p])
            drawAngle_(ax,[comment_p,top_left_p,top_right_p])
            drawAngle_(ax,[bottom_right_p,comment_p,top_left_p])
        else:
            comment_p = (bottom_left_p[0],top_left_p[1])
            drawLine(ax,[bottom_left_p,comment_p])
            drawAngle_(ax,[bottom_left_p,comment_p,top_right_p])
            drawAngle_(ax,[bottom_right_p,bottom_left_p,comment_p])
    plt.axis('scaled')
    svg_comment = saveSvg()
    stem = "다음 사다리꼴에서 $$수식$$A$$/수식$$의 각도는 몇 도인가요?"
    comment = "(해설)\n서로 평행한 두 변에 수직인 선분$$수식$$AB$$/수식$$를\n"\
                "그었습니다. 따라서 만들어진 사각형에서\n"\
                "$$수식$$A = 360rm ° - %srm ° - 90rm ° - 90rm ° = %srm °$$/수식$$입니다." %(stem_num, answer_num) 
    answer = '(답):$$수식$$%srm °$$/수식$$'%answer_num
    plt.show()
    return stem, answer, comment, [svg,svg_comment]

#4-2-4-41
def rectangle424_Stem_006():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #draw parallelogram
    parallelogram = new_p_parallelogram(90)
    parallelogram = resize(parallelogram,90)
    drawPolygon(ax,parallelogram)
    #point
    p_top_l = parallelogram[0]
    p_top_r = parallelogram[1]
    p_bottom_r = parallelogram[2]
    p_bottom_l = parallelogram[3]
    ratio = random.randint(9,15)
    d_side = int(calculate_distance(p_top_l,p_bottom_l)/ratio)
    d_top = int(calculate_distance(p_top_l,p_top_r)/ratio)
    perimeter = d_top*2 + d_side*2
    #draw arc
    random_prob = random.randint(0,3)
    if random_prob == 0: #left,top
        drawArc(ax,p_bottom_l,p_top_l,'left','$%s\mathrm{cm}$'%(d_side))
        drawArc(ax,p_top_l,p_top_r,'top','$%s\mathrm{cm}$'%(d_top))
    elif random_prob == 1:#top,right
        drawArc(ax,p_top_l,p_top_r,'top','$%s\mathrm{cm}$'%(d_top))
        drawArc(ax,p_top_r,p_bottom_r,'right','$%s\mathrm{cm}$'%(d_side))
    elif random_prob == 2:#right,bottom
        drawArc(ax,p_top_r,p_bottom_r,'right','$%s\mathrm{cm}$'%(d_side))
        drawArc(ax,p_bottom_l,p_bottom_r,'bottom','$%s\mathrm{cm}$'%(d_top))
    elif random_prob == 3:#bottom,left
        drawArc(ax,p_bottom_l,p_top_l,'left','$%s\mathrm{cm}$'%(d_side))
        drawArc(ax,p_bottom_l,p_bottom_r,'bottom','$%s\mathrm{cm}$'%(d_top))

    stem = "평행사변형의 네 변의 길이의 합은 몇 $$수식$$rm cm$$/수식$$인가요?"
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(perimeter)
    comment = "(해설)\n평행사변형의 네 변의 길이의 합은\n"\
                "$$수식$$%s+%s+%s+%s=%s(rm cm)$$/수식$$입니다." %(
                    d_top,d_side,d_top,d_side,perimeter
                    )
    
    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg

#4-2-4-43
def rectangle424_Stem_007():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #generate shapes
    parallelogram = new_p_parallelogram(90)
    parallelogram = resize(parallelogram,90)
    #point
    p_top_l = parallelogram[0]
    p_top_r = parallelogram[1]
    p_bottom_r = parallelogram[2]
    p_bottom_l = parallelogram[3]
    #generate variable
    ratio = random.randint(9,15)
    side = int(calculate_distance(p_top_l,p_bottom_l)/ratio)
    top = int(calculate_distance(p_top_l,p_top_r)/ratio)
    perimeter = side*2 + top*2
    #draw
    drawPolygon(ax,parallelogram)
    setPoint(ax,parallelogram,['A','B','C','D'],['top_l','top_r','bottom_r','bottom_l'])
    random_prob = random.randint(0,3)
    if random_prob == 0: #left
        drawArc(ax,p_bottom_l,p_top_l,'left','$%s\mathrm{cm}$'%side)
        answer_len = top
        comment_len = side
        stem_l_name = 'AB'
        comment_l_name = 'AD'
    elif random_prob == 1:#right
        drawArc(ax,p_top_r,p_bottom_r,'right','$%s\mathrm{cm}$'%side)
        answer_len = top
        comment_len = side
        stem_l_name = 'AB'
        comment_l_name = 'BC'
    elif random_prob == 2:#top
        drawArc(ax,p_top_l,p_top_r,'top','$%s\mathrm{cm}$'%top)
        answer_len = side
        comment_len = top
        stem_l_name = 'BC'
        comment_l_name = 'AB'
    elif random_prob == 3:#bottom
        drawArc(ax,p_bottom_l,p_bottom_r,'bottom','$%s\mathrm{cm}$'%top)
        answer_len = side
        comment_len = top
        stem_l_name = 'BC'
        comment_l_name = 'AB'

    stem = "평행사변형의 네 변의 길이의 합은 $$수식$$%srm cm$$/수식$$입니다. "\
            "변$$수식$$%s$$/수식$$는 몇 $$수식$$rm cm$$/수식$$인가요?"%(
                perimeter, stem_l_name
                )
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(answer_len)
    comment = "(해설)\n평행사변형은 마주보는 두 변의 길이가 같습니다.\n"\
                "(변$$수식$$AB$$/수식$$) $$수식$$=$$/수식$$ (변$$수식$$CD$$/수식$$), (변$$수식$$AD$$/수식$$) $$수식$$=$$/수식$$ (변$$수식$$BC$$/수식$$)\n"\
                "따라서 (변$$수식$$%s$$/수식$$) $$수식$$+$$/수식$$ (변$$수식$$%s$$/수식$$) $$수식$$= %s div 2$$/수식$$\n"\
                "(변$$수식$$%s$$/수식$$) $$수식$$= %s -$$/수식$$ (변$$수식$$%s$$/수식$$) $$수식$$= %s - %s = %s(rm cm)$$/수식$$\n"\
                "입니다."%(
                    stem_l_name,comment_l_name,perimeter,
                    stem_l_name,int(perimeter/2),comment_l_name,int(perimeter/2),comment_len, answer_len
                )
    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg

#4-2-4-46
def rectangle424_Stem_008():
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
        a_num_left_5 = random.randint(16,20)
        if a_num_left_5 != 18:
            break
    a_num_left = a_num_left_5*5
    #generate parallelogram
    parallelogram = create_p_parallelogram(a_num_left)
    parallelogram = resize(parallelogram,90)
    #point
    p_top_l = parallelogram[0]
    p_top_r = parallelogram[1]
    p_bottom_r = parallelogram[2]
    p_bottom_l = parallelogram[3]
    #draw
    drawPolygon(ax,parallelogram)
    setPolygonPoint(ax,parallelogram,parallelogram,['A','B','C','D'])
    if a_num_left <= 90: #right_side parallelogram
        l_middle = [p_top_l,p_bottom_r]
        p_stem1 = p_bottom_l
        p_stem2 = p_bottom_r
        a_stem1 = [p_bottom_r,p_bottom_l,p_top_l]
        a_stem2 = [p_top_l,p_bottom_r,p_bottom_l]
        a_answer = [p_top_r,p_bottom_r,p_top_l]
        a_name_stem1 = 'ADC'
        a_name_stem2 = 'ACD'
        a_name_answer = 'ACB'
        a_name_comment = 'BCD'
        a_num_stem1 = a_num_left
        a_num_stem2 = int(calculate_angle(a_stem2))
        a_num_stem2 -= (a_num_stem2%5)
        a_num_answer = 180 - (a_num_stem1+a_num_stem2)
        a_num_comment = 180 - a_num_stem1
        drawLine(ax,l_middle)
        drawAngle_multiple(ax,[a_stem1])
        drawAngle_multiple(ax,[a_stem2,a_answer],True)
        drawText(ax,'$%s\mathrm{°}$'%(a_num_stem1),(p_stem1[0]+13,p_stem1[1]+7),'top')
        drawText(ax,'$%s\mathrm{°}$'%(a_num_stem2),(p_stem2[0]-22,p_stem2[1]+1),'top')
    else: #left_side parallelogram
        l_middle = [p_top_r,p_bottom_l]
        p_stem1 = p_top_l
        p_stem2 = p_top_r
        a_stem1 = [p_bottom_l,p_top_l,p_top_r]
        a_stem2 = [p_top_l,p_top_r,p_bottom_l]
        a_answer = [p_bottom_l,p_top_r,p_bottom_r]
        a_name_stem1 = 'BAD'
        a_name_stem2 = 'ABD'
        a_name_answer = 'CBD'
        a_name_comment = 'ABC'
        a_num_stem1 = 180 - a_num_left
        a_num_stem2 = int(calculate_angle(a_stem2))
        a_num_stem2 -= (a_num_stem2%5)
        a_num_answer = 180 - (a_num_stem1+a_num_stem2)
        a_num_comment = 180 - a_num_stem1
        drawLine(ax,l_middle)
        drawAngle_multiple(ax,[a_stem1])
        drawAngle_multiple(ax,[a_stem2,a_answer],True)
        drawText(ax,'$%s\mathrm{°}$'%(a_num_stem1),(p_stem1[0]+13,p_stem1[1]-3),'bottom')
        drawText(ax,'$%s\mathrm{°}$'%(a_num_stem2),(p_stem2[0]-22,p_stem2[1]-1),'bottom')

    stem = "사각형$$수식$$ABCD$$/수식$$는 평행사변형입니다. "\
            "각$$수식$$%s$$/수식$$의 크기는 몇 도인가요?" %(a_name_answer)
    answer = "(답):$$수식$$%srm °$$/수식$$" %(a_num_answer)
    comment = "(해설)\n평행사변형은 이웃한 두 각의 크기의 합이\n"\
                "$$수식$$180rm °$$/수식$$이므로 $$수식$$%srm °+ (각%s) = 180rm °$$/수식$$,\n"\
                "$$수식$$(각%s) = 180rm ° - %srm ° = %srm °$$/수식$$ 입니다.\n"\
                "따라서 $$수식$$(각%s)=(각%s)-(각%s)$$/수식$$\n"\
                "$$수식$$= %srm ° - %srm ° = %srm °$$/수식$$입니다." %(
                    a_num_stem1,a_name_comment,
                    a_name_comment,a_num_stem1,a_num_comment,
                    a_name_answer,a_name_comment,a_name_stem2,
                    a_num_comment,a_num_stem2,a_num_answer
                    )

    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg

#4-2-4-48, 49
def rectangle424_Stem_009():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    rhombus = new_p_rhombus()
    rhombus = resize(rhombus)
    #point
    p_top_l = rhombus[0]
    p_top_r = rhombus[1]
    p_bottom_r = rhombus[2]
    p_bottom_l = rhombus[3]
    #angle
    a_top_r = [p_top_l,p_top_r,p_bottom_r]
    a_bottom_r = [p_top_r,p_bottom_r,p_bottom_l]
    a_bottom_l = [p_bottom_r,p_bottom_l,p_top_l]
    a_top_l = [p_bottom_l,p_top_l,p_top_r]
    #draw
    random_prob = random.randint(0,3)
    if random_prob == 0: #left/top
        drawPolygonAngle(ax,rhombus,[1,1,1,1],[0,0,1,1],['A','B','',''])
        answer_A = calculate_angle(a_bottom_r)
        answer_B = calculate_angle(a_top_r)
    elif random_prob == 1: #left/bottom
        drawPolygonAngle(ax,rhombus,[1,1,1,1],[1,0,0,1],['','A','B',''])
        answer_A = calculate_angle(a_bottom_l)
        answer_B = calculate_angle(a_bottom_r)
    elif random_prob == 2: #right/top
        drawPolygonAngle(ax,rhombus,[1,1,1,1],[1,1,0,0],['','','A','B'])
        answer_A = calculate_angle(a_top_l)
        answer_B = calculate_angle(a_bottom_l)
    elif random_prob == 3: #right/bottom
        drawPolygonAngle(ax,rhombus,[1,1,1,1],[0,1,1,0],['A','','','B'])
        answer_A = calculate_angle(a_top_l)
        answer_B = calculate_angle(a_top_r)

    stem = "다음 도형은 마름모입니다. $$수식$$A$$/수식$$와 $$수식$$B$$/수식$$에 알맞은 각도를 차례대로 구해 보세요."
    answer = '(답):$$수식$$%srm °$$/수식$$, $$수식$$%srm °$$/수식$$'%(answer_A,answer_B)
    comment = "(해설)\n마름모는 마주 보는 두 각의 크기가 같으므로\n"\
                "$$수식$$A=%srm °$$/수식$$, $$수식$$B=%srm °$$/수식$$입니다." %(answer_A,answer_B)
    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg

#4-2-4-54
def rectangle424_Stem_010():
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
    length = random.randint(3,10)
    perimeter = length*4
    #generate shapes
    rhombus = new_p_rhombus()
    rhombus = resize(rhombus)
    l_random = random.choice([
        [rhombus[0], rhombus[1],'top_l'],
        [rhombus[1], rhombus[2],'top_r'],
        [rhombus[2], rhombus[3],'bottom_r'],
        [rhombus[3], rhombus[0],'bottom_l']
    ])
    #draw shapes
    drawPolygon(ax,rhombus)
    drawArc(ax,l_random[0],l_random[1],l_random[2],'A')

    stem = "다음 마름모는 네 변의 길이가 $$수식$$%srm cm$$/수식$$일때 $$수식$$A$$/수식$$는 몇 $$수식$$rm cm$$/수식$$인가요?"%(perimeter)
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(length)
    comment = "(해설)\n마름모는 네 변의 길이가 모두 같으므로\n"\
                "$$수식$$A = %s div 4 = %s(rm cm)$$/수식$$입니다."%(
                    perimeter, length
                )
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem,answer,comment,svg
