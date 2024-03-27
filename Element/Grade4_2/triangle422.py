import math
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
    def find_text_position_polygon(p_list,p):
        def c_center_p(p_list=[]):
            #calculate center point
            x_center = 0
            y_center = 0
            for p in p_list:
                x_center += p[0]
                y_center += p[1]
            x_center /= len(p_list)
            y_center /= len(p_list)
            return (x_center,y_center)
        center = c_center_p(p_list)
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
        l = len(text[i])
        position = find_text_position_polygon(verts,cp)
        if position == 'top':
            plt.text(cp[0]-l*1.5, cp[1]+2, text[i], fontsize=16, zorder=3)
        elif position == 'bottom':
            plt.text(cp[0]-2*l, cp[1]-9, text[i], fontsize=16, zorder=3)
        elif position == 'left':
            plt.text(cp[0]-3-l*4.5, cp[1]-2, text[i], fontsize=16, zorder=3)
        elif position == 'right':
            plt.text(cp[0]+l+3, cp[1]-2, text[i], fontsize=16, zorder=3)
        elif position == 'top_r':
            plt.text(cp[0]+l*0.3, cp[1]+2, text[i], fontsize=16, zorder=3)
        elif position == 'top_l':
            plt.text(cp[0]+1-l*5, cp[1]+2, text[i], fontsize=16, zorder=3)
        elif position == 'bottom_r':
            plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5, text[i], fontsize=16, zorder=3)
        elif position == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5, text[i], fontsize=16, zorder=3)
        else: raise Exception('no matching position')
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
def drawText(ax,text='',xy=(0,0),position='top'):
    if len(xy) > 2: raise Exception("too many inputs for xy")
    l = len(str(text))
    if text in 'mathrm':
        l -= 14
    cp = xy
    if position == 'top':
        plt.text(cp[0]-l*0.3, cp[1]+0.5, text, fontsize=16, zorder=3)
    elif position == 'bottom':
        plt.text(cp[0]-l*0.3, cp[1]-7, text, fontsize=16, zorder=3)
    elif position == 'left':
        plt.text(cp[0]-2-l*4.5, cp[1]-2, text, fontsize=16, zorder=3)
    elif position == 'right':
        plt.text(cp[0]+l, cp[1]-2, text, fontsize=16, zorder=3)
    elif position == 'top_r':
        plt.text(cp[0]+l*0.3, cp[1]+0.5, text, fontsize=16, zorder=3)
    elif position == 'top_l':
        plt.text(cp[0]-1-l*5, cp[1]+0.5, text, fontsize=16, zorder=3)
    elif position == 'bottom_r':
        plt.text(cp[0]-l*0.3, cp[1]-5, text, fontsize=16, zorder=3)
    elif position == 'bottom_l':
        plt.text(cp[0], cp[1]-5, text, fontsize=16, zorder=3)
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
        position = find_text_position_polygonArc(verts,[p1,p2])
        length = int(c_distance(p1,p2)/length_ratio)
        if show_length != []:
            if show_length[i] == True:
                drawArc(ax,p1,p2,position,str(length)+' '+unit)
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
            pp = mpatches.RegularPolygon(xy=center, fc=random.choice(colors), fill=True, lw=2, zorder=3, alpha=alpha)
    else:
        if dash:
            pp = mpatches.RegularPolygon(xy=center, ec='black', fill=False, lw=1, ls='--', zorder=3)
        else:
            pp = mpatches.RegularPolygon(xy=center, ec='black', fill=False, lw=2, zorder=3,numVertices=n)

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
        p_list.reverse()
    return p_list
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
def resize_polygon_multiple(p_list_multiple=list,scale=90):
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


def equal_list(elements,l):
    if l == []:
        return False
    for temp_l in l:
        temp_elements = elements.copy()
        for i in range(len(temp_l)):
            if temp_l[i] in temp_elements:
                temp_elements.remove(temp_l[i])
        if temp_elements == []:
            return True
        
    return False
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


#4-2-2-03
def triangle422_Stem_001():
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
    length = random.randint(3,8)
    perimeter = length*3
    #generate shapes
    triangle = create_p_triangle(right_bottom_left=[length,length,length])
    triangle = resize_polygon(triangle)
    l_side = [triangle[0],triangle[1]]
    #draw
    drawPolygon(ax,triangle)
    drawArc(ax,l_side[0],l_side[1],'right','    ',True)
    #stem/answer/comment
    stem = "다음 정삼각형의 세 변의 길이의 합은 $$수식$$%srm cm$$/수식$$입니다. □에 알맞은 수를 구해 보세요."%(perimeter)
    answer = "(답):$$수식$$%srm cm$$/수식$$"%(length)
    comment = "(해설)\n정삼각형은 세 변의 길이가 같으므로\n"\
                "(한 변의 길이) $$수식$$=$$/수식$$ (세 변의 길이의 합)$$수식$$div 3$$/수식$$\n"\
                "$$수식$$= %s div 3 = %s(rm cm)$$/수식$$입니다."%(
                    perimeter,length
                )
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem, answer, comment, svg

#4-2-2-04
def triangle422_Stem_002():
    stem = "삼각형의 세 변의 길이가 다음과 같을때, 이등변삼각형이 아닌 것을 찾아 기호를 써보세요.\n"
    char_list = ['㉠','㉡','㉢','㉣']
    #create num_list=[(num1,num2,num3)]
    num_list = []
    while len(num_list) < 3:
        random_num1 = random.randint(2,9)
        random_num2 = random.randint(2,9)
        if random_num1 != random_num2:
            if len(num_list) == 2:
                random_num3 = random.randint(2,9)
                while random_num3 == random_num1 or random_num3 == random_num2:
                    random_num3 = random.randint(2,9)
                num_list.append([random_num1,random_num2,random_num3])
                all_diff_len = [random_num1,random_num2,random_num3]
            else:
                num_list.append(random.sample([random_num1,random_num2,random_num1],3))
    random.shuffle(num_list)
    #form stem
    for i in range(len(num_list)):
        stem += char_list[i] + ' $$수식$$%srm cm$$/수식$$, $$수식$$%srm cm$$/수식$$, $$수식$$%srm cm$$/수식$$\n' %(num_list[i][0],num_list[i][1],num_list[i][2])
        if num_list[i] == all_diff_len:
            answer_index = i
            
    answer = '(답):%s'%char_list[answer_index]
    comment = "(해설)\n%s은 세 변의 길이가 모두 다르므로 이등변삼각형\n"\
                "이 아닙니다." %(char_list[answer_index])
    return stem,answer,comment

#4-2-2-05, 06
def triangle422_Stem_003():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    problem_option = random.choice([5,6])
    while True:
        width = random.randint(3,7)
        height = random.randint(5,10)
        side = int(math.sqrt(height**2+width**2/4))
        perimeter = side*2+width
        properSizeOfWidthHeight = height > width and height-width >= 2 and height-width <= 6
        if properSizeOfWidthHeight:
            if problem_option == 5:
                break
            elif problem_option == 6:
                if perimeter%3 == 0:
                    break
    triangle = create_p_triangle(right_bottom_left=[side,width,side])
    triangle = resize_polygon(triangle)
    triangle = move_to_center(triangle)
    top_p,right_p,left_p = triangle
    drawPolygon(ax,triangle)
    #text
    left_xy = (left_p[0]-7,left_p[1]-3)
    right_xy = (right_p[0]+4,right_p[1]-3)
    top_xy = (top_p[0]-2,top_p[1]+3)
    drawText(ax,'A',top_xy)
    drawText(ax,'B',left_xy)
    drawText(ax,'C',right_xy)
    
    if problem_option == 5:
        drawArc(ax,left_p,right_p,'bottom','$%s\mathrm{cm}$'%(width))
        show_side = random.randint(0,1)
        if show_side == 0: #left_side
            drawArc(ax,left_p,top_p,'left','$%s\mathrm{cm}$'%(side))
        elif show_side == 1: #right_side
            drawArc(ax,right_p,top_p,'right','$%s\mathrm{cm}$'%(side))
        stem = "삼각형$$수식$$ABC$$/수식$$는 이등변삼각형입니다. 삼각형$$수식$$ABC$$/수식$$의 세 변의 길이의 합은 몇 $$수식$$rm cm$$/수식$$인가요?"
        comment = "(해설)\n이등변삼각형은 두 변의 길이가 같으므로\n"\
                    "(변 AB) = (변 AC) $$수식$$= %srm cm$$/수식$$\n"\
                    "따라서 삼각형 ABC의 세 변의 길이의 합은\n"\
                    "$$수식$$%s+%s+%s=%s(rm cm)$$/수식$$입니다." %(
                        side,
                        side,side,width,perimeter
                    )
        answer = '(답):$$수식$$%srm cm$$/수식$$'%(perimeter)
    elif problem_option == 6:
        lengthOfNewTriangle = int(perimeter/3)
        drawArc(ax,left_p,right_p,'bottom','$%s\mathrm{cm}$'%(width))
        show_side = random.randint(0,1)
        if show_side: #left_side
            drawArc(ax,left_p,top_p,'left','$%s\mathrm{cm}$'%(side))
        else: #right_side
            drawArc(ax,right_p,top_p,'right','$%s\mathrm{cm}$'%(side))
        stem = "세 변의 길이의 합이 아래 이등변삼각형과 같은 정삼각형을 만들려고 합니다. 정삼각형의 한 변의 길이를 몇 $$수식$$rm cm$$/수식$$로 해야 하나요?"
        comment = "(해설)\n이등변삼각형은 두 변의 길이가 같으므로\n"\
                    "(이등변삼각형의 세 변의 길이의 합)\n"\
                    "$$수식$$= %s + %s + %s = %s(rm cm)$$/수식$$입니다.\n"\
                    "정삼각형은 세 변의 길이가 같으므로\n"\
                    "(정삼각형의 한 변의 길이)\n"\
                    "$$수식$$=%s div 3 = %s(rm cm)$$/수식$$입니다." %(
                        side,side,width,perimeter,
                        perimeter,lengthOfNewTriangle
                    )
        answer = '(답):$$수식$$%srm cm$$/수식$$'%(lengthOfNewTriangle)
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem, answer, comment, svg

#4-2-2-07
def triangle422_Stem_004():
    while True:
        random_num1 = random.randint(2,9)
        random_num2 = random.randint(2,9)
        if random_num1 != random_num2:
            break
    name = random.choice(['윤서','성욱이','찬호','경수','철수','영희','영서'])
    stem = name + "는 세 변의 길이가 다음과 같은 이등변삼각형을 그렸습니다. □안에 들어갈 수 있는 수를 모두 구해 보세요."
    stem += "$$표$$$$수식$$%srm cm$$/수식$$, $$수식$$%srm cm$$/수식$$, □$$수식$$rm cm$$/수식$$$$/표$$" %(random_num1, random_num2)
    answer_list = [random_num1, random_num2]
    answer_list.sort()
    answer = '(답):$$수식$$%s$$/수식$$, $$수식$$%s$$/수식$$'%(answer_list[0],answer_list[1])
    comment = "(해설)\n이등변삼각형은 두 변의 길이가 같습니다.\n"\
                "삼각형의 세 변 중 두 변이 각각 $$수식$$%srm cm$$/수식$$, $$수식$$%srm cm$$/수식$$이므로\n"\
                "이등변삼각형이 될 수 있는 세 변의 길이는\n"\
                "$$수식$$%srm cm$$/수식$$, $$수식$$%srm cm$$/수식$$, $$수식$$%srm cm$$/수식$$ 또는 $$수식$$%srm cm$$/수식$$, $$수식$$%srm cm$$/수식$$, $$수식$$%srm cm$$/수식$$입니다.\n"\
                "따라서 □안에 들어갈 수 있는 수는 $$수식$$%s$$/수식$$, $$수식$$%s$$/수식$$입니다." %(
        random_num1,random_num2,
        random_num1,random_num2,answer_list[0],random_num1,random_num2,answer_list[1],
        answer_list[0],answer_list[1]
    )
    return stem,answer,comment

#4-2-2-11, 12
def triangle422_Stem_005():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    left_p = (-50,0)
    right_p = (50,0)
    top_p = (0,random.randint(30,150))
    triangle = [top_p,right_p,left_p]
    triangle = move_to_center(triangle)
    top_p,right_p,left_p = triangle
    drawPolygon(ax,triangle)
    #angle
    drawAngle(ax,[[top_p,right_p,left_p]]) #right_angle
    drawAngle(ax,[[right_p,left_p,top_p]]) #left_angle
    num_angle = int(c_angle([top_p,right_p,left_p]))
    num_angle = num_angle - (num_angle%10)
    #text_position
    left_xy = (left_p[0]-7,left_p[1]-7)
    right_xy = (right_p[0],right_p[1]-7)
    top_xy = (top_p[0]-2,top_p[1]+3)
    #arc
    ratio = random.randint(13,18)
    len_side = int(math.sqrt(top_p[1]**2+100**2) / ratio)
    len_bottom = int(100/ratio)
    while len_side == len_bottom:
        ratio = random.randint(13,18)
        len_side = int(math.sqrt(top_p[1]**2+100**2) / ratio)
        len_bottom = int(100/ratio)
    flag = random.randint(0,1)
    if flag: #11
        stem = "$$수식$$A$$/수식$$에 알맞은 수를 구해 보세요."
        answer = len_side
        comment = "(해설)\n두 각의 크기가 같으므로 이등변삼각형입니다.\n"
        comment += "이등변삼각형은 두 변의 길이가 같으므로\n"
        comment += "$$수식$$A = %srm cm$$/수식$$입니다." %(answer)
        answer = '(답):$$수식$$%srm cm$$/수식$$'%(answer)
        flag_ = random.randint(0,1)
        #angle
        drawText(ax,'$%s\mathrm{°}$'%(num_angle),left_xy)
        drawText(ax,'$%s\mathrm{°}$'%(num_angle),right_xy)
        #arc
        if flag_: #left
            drawArc(ax,right_p,top_p,'right','$%s\mathrm{cm}$'%(len_side))
            drawArc(ax,left_p,top_p,'left','%s'%('A'))
        else: #right
            drawArc(ax,right_p,top_p,'right','%s'%('A'))
            drawArc(ax,left_p,top_p,'left','$%s\mathrm{cm}$'%(len_side))
    else: #12
        stem = "A에 알맞은 각도를 구해 보세요."
        answer = num_angle
        comment = "(해설)\n두 변의 길이가 같으므로 이등변삼각형입니다.\n"
        comment += "이등변삼각형은 두 각의 크기가 같으므로\n"
        comment += "$$수식$$A=%s°$$/수식$$입니다." %(answer)
        answer = '(답):$$수식$$%s°$$/수식$$'%(answer)
        #arc
        drawArc(ax,right_p,top_p,'right','$%s\mathrm{cm}$'%(len_side))
        drawArc(ax,left_p,top_p,'left','$%s\mathrm{cm}$'%(len_side))
        #angle
        flag_ = random.randint(0,1)
        if flag_: #left
            drawText(ax,'%s'%('A'),left_xy)
            drawText(ax,'$%s\mathrm{°}$'%(num_angle),right_xy)
        else: #right
            drawText(ax,'$%s\mathrm{°}$'%(num_angle),left_xy)
            drawText(ax,'%s'%('A'),right_xy)
    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg

#4-2-2-14
def triangle422_Stem_006():
    stem = "삼각형의 세 각 중에서 두 각의 크기를 잰 것입니다. 이등변삼각형이 될 수 있는 것을 모두 찾아 기호를 써보세요."
    char_list = ['㉠','㉡','㉢']
    #create num_list [(bool,num1,num2)]
    bool_list = [random.randint(0,1),random.randint(0,1),random.randint(0,1)]
    while bool_list == [1,1,1] or bool_list == [0,0,0]:
        bool_list = [random.randint(0,1),random.randint(0,1),random.randint(0,1)]
    num_list = []
    check_list = []
    for i in range(3):
        while True:
            random_side_num5 = random.randint(6,11)
            random_other_side_num5 = random.randint(6,16)
            random_last_num5 = 36 - (random_side_num5 + random_other_side_num5)
            smallerThan180 = random_side_num5*2*5+random_other_side_num5*5 < 180
            itNotEquilateralTriangle = random_side_num5 != random_other_side_num5 and\
                                        random_side_num5 != random_last_num5 and\
                                        random_other_side_num5 != random_last_num5
            isNotInList = (random_side_num5*5,random_other_side_num5*5)not in check_list and\
                            (random_side_num5*5,random_side_num5*5) not in check_list
            if smallerThan180 and itNotEquilateralTriangle and isNotInList:
                break

        if bool_list[i]: #이등변삼각형
            check_list.append((random_side_num5*5,random_side_num5*5))
            num_list.append((True,random_side_num5*5,random_side_num5*5))
        else: #그냥 삼각형
            check_list.append((random_side_num5*5,random_other_side_num5*5))
            num_list.append((False,random_side_num5*5,random_other_side_num5*5))
    random.shuffle(num_list)
    #form stem,answer,comment
    answer = "(답):"
    comment = "(해설)\n나머지 한 각의 크기를 각각 구해 봅니다.\n"
    stem += "$$표$$"
    for i in range(3):
        num_tuple = num_list[i]
        if num_tuple[0] == True: #이등변삼각형
            num1 = num_tuple[1]
            num3 = num_tuple[2]
            num2 = 180 - (num1+num3)
            answer += char_list[i] +', '
        else: #그냥 삼각형
            num1 = num_tuple[1]
            num2 = num_tuple[2]
            num3 = 180 - (num1+num2)
        stem += char_list[i] +' $$수식$$%s°$$/수식$$, $$수식$$%s°$$/수식$$ ' %(num1,num2)
        comment += char_list[i] + ' $$수식$$180° - %s° - %s° = %s°$$/수식$$\n'%(num1,num2,num3)
    stem += "$$/표$$" 
    answer = answer[:len(answer)-2]
    comment += "따라서 이등변삼각형이 될 수 있는 것은 세 각\n"
    comment += "중 두 각의 크기가 같은 %s입니다." %(answer.split("(답):")[1])
    return stem,answer,comment

#4-2-2-16
def triangle422_Stem_007():
    def drawTriangles(ax,numOfTriangles,len_side,len_bottom):
        len_height = math.sqrt(len_side*len_side-len_bottom*len_bottom/4)
        len_side *= 10
        len_bottom *= 10
        len_height *= 10
        #create triangles
        triangle = create_p_triangle(right_bottom_left=[len_side,len_bottom,len_side])
        triangle_list = []
        for i in range(numOfTriangles):
            triangle_list.append(triangle)
            triangle = flip_p(triangle,'y')
            triangle = flip_p(triangle,'x')
            triangle = move_p(triangle,len_bottom/2)
            if i%2 == 0:
                triangle = move_p(triangle,0,len_height/3)
            else:
                triangle = move_p(triangle,0,-len_height/3)
        triangle_list = resize_polygon_multiple(triangle_list)
        #set points/length
        first_triangle = triangle_list[0]
        last_triangle = triangle_list[len(triangle_list)-1]
        p_odd = []
        p_even = []
        p_position = []
        for i in range(len(triangle_list)):
            p = triangle_list[i][0]
            if i%2 == 0: #odd
                p_odd.append(p)
                p_position += ['top']
            else: #even
                p_even.append(p)
        p_even.reverse()
        if numOfTriangles % 2 == 0:
            p_triangle = p_odd + [last_triangle[2]] + p_even + [first_triangle[2]]
            show_len = ['','','$%s \mathrm{cm}$'%(int(len_side/10))]
            p_position += ['top']
        else:
            p_triangle = p_odd + [last_triangle[1]] + p_even + [first_triangle[2]]
            show_len=['$%s \mathrm{cm}$'%(int(len_side/10)),'','']
            p_position += ['bottom']
        for i in range(len(p_even)):
            p_position += ['bottom']
        p_position += ['bottom']
        p_name = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
        drawPolygon_multiple(ax,triangle_list)
        drawPolygonArc(ax,last_triangle,show_text=show_len)
        setPoint(ax,p_triangle,p_name[:len(p_triangle)],p_position)
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
    numOfTriangles = random.randint(2,6)
    len_side = random.randint(6,10)
    len_bottom = random.randint(4,6)
    perimeter = len_side*2 + len_bottom*numOfTriangles
    #generate shapes
    drawTriangles(ax,numOfTriangles,len_side,len_bottom)

    stem = "똑같은 이등변삼각형 $$수식$$%s$$/수식$$개를 변끼리 이어붙여서 다음 도형을 만들었습니다. 이 도형의 둘레가 "\
            "$$수식$$%srm cm$$/수식$$라면 선분 AB의 길이는 몇 $$수식$$rm cm$$/수식$$인가요?"%(
                numOfTriangles, perimeter
            )
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(len_bottom)
    comment = "(해설)\n선분 AB의 길이를 $$수식$$□rm cm$$/수식$$라 하면\n"\
                "(도형의 둘레)\n"\
                "$$수식$$=□ times %s + %s + %s$$/수식$$\n"\
                "$$수식$$= %s(rm cm)$$/수식$$입니다.\n"\
                "$$수식$$□ times %s = %s - %s$$/수식$$, $$수식$$□= %s div %s$$/수식$$,\n"\
                "$$수식$$□= %s(rm cm)$$/수식$$입니다."%(
                    numOfTriangles, len_side, len_side,
                    perimeter,
                    numOfTriangles, perimeter, len_side*2, len_bottom*numOfTriangles, numOfTriangles,
                    len_bottom
                )
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem, answer, comment, svg

#4-2-2-19, 20
def triangle422_Stem_008():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)

    triangle = [(-50,0),(0,100),(50,0)]
    triangle = move_to_center(triangle)
    drawPolygon(ax,triangle)
    #point
    p_left = triangle[0]
    p_top = triangle[1]
    p_right = triangle[2]
    #angle
    random_angle = random.randint(0,2)
    if random_angle == 0: #top,right
        drawAngle_(ax,[p_left,p_top,p_right])
        drawAngle_(ax,[p_top,p_right,p_left])
        drawText(ax,'$60\mathrm{°}$',p_top,'top')
        drawText(ax,'$60\mathrm{°}$',p_right,'bottom')
    elif random_angle == 1: #top,left
        drawAngle_(ax,[p_left,p_top,p_right])
        drawAngle_(ax,[p_right,p_left,p_top])
        drawText(ax,'$60\mathrm{°}$',p_top,'top')
        drawText(ax,'$60\mathrm{°}$',p_left,'bottom')
    elif random_angle == 2: #left,right
        drawAngle_(ax,[p_right,p_left,p_top])
        drawAngle_(ax,[p_top,p_right,p_left])
        drawText(ax,'$60\mathrm{°}$',p_left,'bottom')
        drawText(ax,'$60\mathrm{°}$',p_right,'bottom')
    #length
    len = random.randint(3,13)
    random_arc = random.randint(0,2)
    if random_arc == 0: #left
        drawArc(ax,p_left,p_top,'left','$%s\mathrm{cm}$'%(len))
    elif random_arc == 1: #right
        drawArc(ax,p_right,p_top,'right','$%s\mathrm{cm}$'%(len))
    elif random_arc == 2: #bottom
        drawArc(ax,p_left,p_right,'bottom','$%s\mathrm{cm}$'%(len))
    random_prob = random.randint(0,1)
    if random_prob: #19
        stem = "A에 알맞은 수를 구해 보세요."
        answer = '(답):$$수식$$%srm cm$$/수식$$'%(len)
        comment = "(해설)\n삼각형의 나머지 한 각의 크기는\n"\
                    "$$수식$$180° - 60° - 60° = 60°$$/수식$$ 입니다.\n"\
                    "삼각형의 세 각의 크기가 같으므로 정삼각형\n"\
                    "입니다. 따라서 정삼각형은 세 변의 길이가\n"\
                    "같으므로 $$수식$$A=%srm cm$$/수식$$입니다." %(len)
        while True: 
            random_arc_ = random.randint(0,2)
            if random_arc_ != random_arc:
                break
        if random_arc_ == 0: #left
            drawArc(ax,p_left,p_top,'left','A')
        elif random_arc_ == 1: #right
            drawArc(ax,p_right,p_top,'right','A')
        elif random_arc_ == 2: #bottom
            drawArc(ax,p_left,p_right,'bottom','A')
    else: #20
        stem = "다음 삼각형의 세 변의 길이의 합은 몇 $$수식$$rm cm$$/수식$$인가요?"
        answer = '(답):$$수식$$%srm cm$$/수식$$'%(len*3)
        comment = "(해설)\n삼각형의 세 각의 크기의 합은 $$수식$$180°$$/수식$$이므로\n"
        comment += "나머지 한 각의 크기는\n"
        comment += "$$수식$$180°-60°-60°=60°$$/수식$$입니다.\n"
        comment += "주어진 삼각형은 세 각의 크기가 모두 같으므로\n"
        comment += "정삼각형입니다.\n"
        comment += "정삼각형은 세 변의 길이가 같으므로\n"
        comment += "(세 변의 길이의 합) $$수식$$= %s+%s+%s=%s(rm cm)$$/수식$$\n" %(len,len,len,len*3)
        comment += "입니다."

    #plt.show()
    plt.axis('scaled')
    svg= saveSvg()
    return stem, answer, comment, svg

#4-2-2-23
def triangle422_Stem_009():
    stem = "삼각형의 세 각의 크기를 나타낸 것입니다. 예각삼각형은 어느 것인가요?\n"
    char_list = ['①','②','③','④','⑤']
    triangle_list = []
    #create triangle_list
    answer_index = random.randint(0,4)
    for i in range(5):
        if i == answer_index:
            while True:
                small_angle_num5_1 = random.randint(3,17)
                small_angle_num5_2 = random.randint(3,17)
                rest_angle_num5 = 36-(small_angle_num5_1+small_angle_num5_2)
                angle_list = [small_angle_num5_1*5,small_angle_num5_2*5,rest_angle_num5*5]
                if not equal_list(angle_list,triangle_list) and rest_angle_num5 > 0 and rest_angle_num5 < 17:
                    break
            angle_list.sort()
            triangle_list.append(angle_list)
        else:
            while True:
                big_angle_num5 = random.randint(18,24)
                small_angle_num5 = random.randint(3,11)
                rest_angle_num5 = 36-(small_angle_num5+big_angle_num5)
                angle_list = [big_angle_num5*5,small_angle_num5*5,rest_angle_num5*5]
                if not equal_list(angle_list,triangle_list) and rest_angle_num5 > 0:
                    break
            angle_list.sort()
            triangle_list.append(angle_list)
    #form stem
    for i in range(len(triangle_list)):
        triangle = triangle_list[i]
        stem += char_list[i] + ' $$수식$$%s°$$/수식$$, $$수식$$%s°$$/수식$$, $$수식$$%s°$$/수식$$       '%(triangle[0],triangle[1],triangle[2])
        if i == 1 or i == 3:
            stem += '\n'
    answer = char_list[answer_index]
    comment = "(해설)\n세 각이 모두 예각인 것을 찾으면 %s입니다." %(answer)
    answer = '(답):%s'%(answer)
    return stem,answer,comment

#4-2-2-28
def triangle422_Stem_010():
    #create triangle_list
    answer_num = random.randint(0,2)
    triangle_list = []
    if answer_num == 0: #예각
        answer = "예각삼각형"
        small_angle5_1 = random.randint(3,17)
        small_angle5_2 = random.randint(3,17)
        small_rest_angle5 = 36 - (small_angle5_1 + small_angle5_2)
        while small_rest_angle5 <= 0 or small_rest_angle5 >= 18:
            small_angle5_1 = random.randint(3,17)
            small_angle5_2 = random.randint(3,17)
            small_rest_angle5 = 36 - (small_angle5_1 + small_angle5_2)
        triangle_list = [small_angle5_1*5, small_angle5_2*5, small_rest_angle5*5]
        random.shuffle(triangle_list)
    elif answer_num == 1: #둔각
        answer = "둔각삼각형"
        big_angle5 = random.randint(20,30)
        small_angle5 = random.randint(3,17)
        rest_angle5 = 36 - (big_angle5 + small_angle5)
        while rest_angle5 <= 0:
            big_angle5 = random.randint(20,30)
            small_angle5 = random.randint(3,17)
            rest_angle5 = 36 -(big_angle5 + small_angle5)
        triangle_list = [small_angle5*5,rest_angle5*5,big_angle5*5]
    elif answer_num == 2: #직각
        answer = "직각삼각형"
        right_angle5 = 18
        small_angle5 = random.randint(3,17)
        small_rest_angle5 = 18 - small_angle5
        triangle_list = [small_rest_angle5*5,small_angle5*5,right_angle5*5]
    
    #stem
    stem = "두 각의 크기가 각각 $$수식$$%s°$$/수식$$, $$수식$$%s°$$/수식$$인 삼각형이 있습니다. 이 삼각형은 예각삼각형,직각삼각형, "\
            "둔각삼각형중에서 어떤 삼각형인가요?"%(
                triangle_list[0],triangle_list[1]
            )
    #comment
    comment = "(해설)\n삼각형의 세 각의 크기의 합은 $$수식$$180°$$/수식$$이므로\n"
    comment += "나머지 한 각의 크기는\n"
    comment += "$$수식$$180° - %s° - %s° = %s°$$/수식$$입니다.\n" %(triangle_list[0],triangle_list[1],triangle_list[2])
    if answer_num == 0: #예각
        comment += "따라서 세 각이 $$수식$$%s°$$/수식$$, $$수식$$%s°$$/수식$$, $$수식$$%s°$$/수식$$로 모두 예각인\n"%(triangle_list[0],triangle_list[1],triangle_list[2])
        comment += "삼각형이므로 예각삼각형입니다."
    elif answer_num == 1: #둔각
        comment +=  "따라서 세 각이 $$수식$$%s°$$/수식$$, $$수식$$%s°$$/수식$$, $$수식$$%s°$$/수식$$로 한 각이 둔각인\n"%(triangle_list[0],triangle_list[1],triangle_list[2])
        comment += "삼각형이므로 둔각삼각형입니다."
    elif answer_num == 2: #직각
        comment += "따라서 세 각이 $$수식$$%s°$$/수식$$, $$수식$$%s°$$/수식$$, $$수식$$%s°$$/수식$$로 한 각이 직각인\n"%(triangle_list[0],triangle_list[1],triangle_list[2])
        comment += "삼각형이므로 직각삼각형입니다."
    answer = '(답):%s'%(answer)
    return stem,answer,comment
