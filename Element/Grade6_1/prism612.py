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
            plt.text(cp[0]-2*l, cp[1]+7, text[i], fontsize=10, zorder=3)
        elif position[i] == 'bottom':
            plt.text(cp[0]-2*l, cp[1]-9, text[i], fontsize=10, zorder=3)
        elif position[i] == 'left':
            plt.text(cp[0]-3-l*4.5, cp[1]-2, text[i], fontsize=10, zorder=3)
        elif position[i] == 'right':
            plt.text(cp[0]+l+7, cp[1]-2, text[i], fontsize=10, zorder=3)
        elif position[i] == 'top_r':
            plt.text(cp[0]+l*0.3, cp[1]+2, text[i], fontsize=10, zorder=3)
        elif position[i] == 'top_l':
            plt.text(cp[0]+1-l*5, cp[1]+2, text[i], fontsize=10, zorder=3)
        elif position[i] == 'bottom_r':
            plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5, text[i], fontsize=10, zorder=3)
        elif position[i] == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5, text[i], fontsize=10, zorder=3)
        else: raise Exception('no matching position')
        #plt.text(points[i][0]-0.5, points[i][1]+0.1, text[i], fontsize=14, zorder=3)

        if fill:
            ax.plot(points[i][0], points[i][1],"k.", zorder=3)
    

    #for i in range(0,len(points)):
    #    ax.plot([points[i][0]], [points[i][1]],"ko", zorder=3)
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
        if y > y_center:
            position = 'top'
        else:
            position = 'bottom'
        if x > x_center:
            position += '_r'
        else:
            position += '_l'
        # dx = abs(x-x_center)
        # dy = abs(y-y_center)
        # if dx >= dy: #right/left - x
        #     if x >= x_center: #right
        #         position = 'right'
        #     else: #left
        #         position = 'left'
        # else: #top/bottom - y
        #     if y >= y_center: #top
        #         position = 'top'
        #     else: #bottom
        #         position = 'bottom'
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
        top_y = cp[1]+1.5
        bottom_y = cp[1]-8
        left_x = cp[0]-3-l*5
        right_x = cp[0]+l+1
        if position == 'top':
            plt.text(cp[0]-l*1.5, top_y, text[i], fontsize=10, zorder=3)
        elif position == 'bottom':
            plt.text(cp[0]-l*1.5, bottom_y, text[i], fontsize=10, zorder=3)
        elif position == 'left':
            plt.text(left_x, cp[1]-2, text[i], fontsize=10, zorder=3)
        elif position == 'right':
            plt.text(right_x, cp[1]-2, text[i], fontsize=10, zorder=3)
        elif position == 'top_r':
            plt.text(right_x, top_y, text[i], fontsize=10, zorder=3)
        elif position == 'top_l':
            plt.text(left_x, top_y, text[i], fontsize=10, zorder=3)
        elif position == 'bottom_r':
            plt.text(right_x, bottom_y, text[i], fontsize=10, zorder=3)
        elif position == 'bottom_l':
            plt.text(left_x, bottom_y, text[i], fontsize=10, zorder=3)
        else: raise Exception('no matching position')

    
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
def drawLine(ax,pts,dash=False,color='black',alpha=1):
    if dash: linestype = 'dashed'
    else: linestype = '-'
    line_1 = matplotlib.lines.Line2D((pts[0][0],pts[1][0]), (pts[0][1],pts[1][1]), linewidth=1, linestyle = linestype,color=color,alpha=alpha)
    ax.add_line(line_1)

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
                pp = mpatches.PathPatch(path, fc=random.choice(colors), fill=True, lw=2, zorder=3, alpha=alpha)
        else:
            if dash:
                pp = mpatches.PathPatch(path, ec='black', fill=False, lw=1, ls='--', zorder=3, alpha=alpha)
            else:
                pp = mpatches.PathPatch(path, ec='black', fill=False, lw=2, zorder=3, alpha=alpha)
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
        elif color == 'Orange':
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
    if 'mathrm' in text: 
        l -= 10
    cp = xy
    if position == 'top':
        plt.text(cp[0]-2*l, cp[1]+5, text, fontsize=10, zorder=3)
    elif position == 'bottom':
        plt.text(cp[0]-2*l, cp[1]-8, text, fontsize=10, zorder=3)
    elif position == 'left':
        plt.text(cp[0]-2-l*4.5, cp[1]-2, text, fontsize=10, zorder=3)
    elif position == 'right':
        plt.text(cp[0]+l, cp[1]-2, text, fontsize=10, zorder=3)
    elif position == 'top_r':
        plt.text(cp[0]+1+l*0.3, cp[1]+5, text, fontsize=10, zorder=3)
    elif position == 'top_l':
        plt.text(cp[0]+1-l*5, cp[1]+2, text, fontsize=10, zorder=3)
    elif position == 'bottom_r':
        plt.text(cp[0]+1+l*0.3, cp[1]-11, text, fontsize=10, zorder=3)
    elif position == 'bottom_l':
        plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5, text, fontsize=10, zorder=3)
    else: raise Exception('no matching position')

#색칠
def colorPolygon(ax,vert=list,color='',alpha=1):
    if color != '': colors = [color]
    else:
        colors = []
        for i in mcolors.CSS4_COLORS:
            colors.append(i)

    vert.append(vert[0])
    codes = [Path.MOVETO]
    for i in range(0,len(vert)-2):
        codes.append(Path.LINETO)
    codes.append(Path.CLOSEPOLY)
    path = Path(vert,codes)
    pp = mpatches.PathPatch(path, fc=random.choice(colors), fill=True, lw=0, zorder=3, alpha=alpha)
    ax.add_patch(pp)
    vert.pop()
def colorPolygon_multiple(ax,vert_list=list,set_color='',alpha=1):
    if set_color != '': color = set_color
    else:
        color_list = list(mcolors.CSS4_COLORS.keys())
        color = random.choice(color_list)
    for i in range(len(vert_list)):
        vert = vert_list[i]
        vert.append(vert[0])
        codes = [Path.MOVETO]
        for i in range(0,len(vert)-2):
            codes.append(Path.LINETO)
        codes.append(Path.CLOSEPOLY)
        path = Path(vert,codes)
        pp = mpatches.PathPatch(path,fc=color,fill=True,lw=0,zorder=3,alpha=alpha)
        ax.add_patch(pp)
        vert.pop()


# 선분의 길이를 표시하는 bezier 곡선을 그리는 함수
def drawPolygonArc(ax,verts=list,show_length=[],show_text=[],length_ratio=10,unit='cm',alpha=1):
    def c_distance(p1=tuple, p2=tuple):
        import math
        d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
        return d
    def find_text_position_polygon(p_list,l):
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
    def drawArc(ax, p1, p2, position, text, boxed=False):
        if 'top' in position: cp = find_controlPoint_arc(p1,p2,'top')
        elif 'bottom' in position: cp = find_controlPoint_arc(p1,p2,'bottom')
        elif 'right' in position: cp = find_controlPoint_arc(p1,p2,'right')
        elif 'left' in position: cp = find_controlPoint_arc(p1,p2,'left')
        p1 = (round(p1[0],5),round(p1[1],5))
        p2 = (round(p2[0],5),round(p2[1],5))
        l = len(str(text))
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

        pp = mpatches.PathPatch(path, fc="none",transform=ax.transData,linestyle="--",zorder=3,alpha=alpha)
        ax.add_patch(pp)
        y_top = cp[1]+2
        y_bottom = cp[1]-8+l*0.5
        x_right = cp[0]+l*0.4
        x_left = cp[0]+1-l*5
        if boxed:
            if position == 'top':
                plt.text(cp[0]-2*l, cp[1]+3.5, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
            elif position == 'bottom':
                plt.text(cp[0]-2*l, cp[1]-7.5, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
            elif position == 'left':
                plt.text(cp[0]-2-l*4.5, cp[1]-2, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
            elif position == 'right':
                plt.text(cp[0]+l, cp[1]-2, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
            elif position == 'top_r':
                plt.text(cp[0]+l*0.3, cp[1]+2, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
            elif position == 'top_l':
                plt.text(cp[0]+1-l*5, cp[1]+2, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
            elif position == 'bottom_r':
                plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
            elif position == 'bottom_l':
                plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        else:
            if position == 'top':
                plt.text(cp[0]-2*l, y_top, text, fontsize=10, zorder=3)
            elif position == 'bottom':
                plt.text(cp[0]-2*l, y_bottom, text, fontsize=10, zorder=3)
            elif position == 'left':
                plt.text(x_left, cp[1]+2, text, fontsize=10, zorder=3)
            elif position == 'right':
                plt.text(x_right, cp[1]-4, text, fontsize=10, zorder=3)
            elif position == 'top_r':
                plt.text(x_right, y_top, text, fontsize=10, zorder=3)
            elif position == 'top_l':
                plt.text(x_left, y_top, text, fontsize=10, zorder=3)
            elif position == 'bottom_r':
                plt.text(x_right, y_bottom, text, fontsize=10, zorder=3)
            elif position == 'bottom_l':
                plt.text(x_left, y_bottom, text, fontsize=10, zorder=3)
            else: raise Exception('no matching position')
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
        position = find_text_position_polygon(verts,[p1,p2])
        length = int(c_distance(p1,p2)/length_ratio)
        if show_length != []:
            if show_length[i] == True:
                drawArc(ax,p1,p2,position,'$%s \\mathrm{%s}$'%(length,unit))
        if show_text != []: 
            if show_text[i] != '':
                drawArc(ax,p1,p2,position,show_text[i])
def drawArc(ax, p_list, position, text, boxed=False,color='black'):
    if len(p_list) != 2: raise Exception('p_list has more or less than 2 elements')
    if text == '': return
    p1 = p_list[0]
    p2 = p_list[1]
    if 'top' in position: cp = find_controlPoint_arc(p1,p2,'top')
    elif 'bottom' in position: cp = find_controlPoint_arc(p1,p2,'bottom')
    elif 'r' in position: cp = find_controlPoint_arc(p1,p2,'right')
    elif 'l' in position: cp = find_controlPoint_arc(p1,p2,'left')
    p1 = (round(p1[0],5),round(p1[1],5))
    p2 = (round(p2[0],5),round(p2[1],5))
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
            plt.text(cp[0]-2*l, cp[1]+3.5, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom':
            plt.text(cp[0]-2*l, cp[1]-7.5, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'left':
            plt.text(cp[0]-2-l*4.5, cp[1]-2, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'right':
            plt.text(cp[0]+l, cp[1]-2, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'top_r':
            plt.text(cp[0]+l*0.3, cp[1]+2, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'top_l':
            plt.text(cp[0]+1-l*5, cp[1]+2, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_r':
            plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
    else:
        if position == 'top':
            plt.text(cp[0]-2*l, cp[1]+1, text, fontsize=10, zorder=3)
        elif position == 'bottom':
            plt.text(cp[0]-2*l, cp[1]-7.5, text, fontsize=10, zorder=3)
        elif position == 'left':
            plt.text(cp[0]-2-l*4.5, cp[1]-2, text, fontsize=10, zorder=3)
        elif position == 'right':
            plt.text(cp[0]+l*0.1, cp[1]-2, text, fontsize=10, zorder=3)
        elif position == 'top_r':
            plt.text(cp[0]+l*0.3, cp[1]+2, text, fontsize=10, zorder=3)
        elif position == 'top_l':
            plt.text(cp[0]+1-l*4, cp[1]+2, text, fontsize=10, zorder=3)
        elif position == 'bottom_r':
            plt.text(cp[0]+l, cp[1]-8+l*0.5, text, fontsize=10, zorder=3)
        elif position == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-3+l*0.5, text, fontsize=10, zorder=3)
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
        plt.text(cp[0]-l*0.425, middle_p[1]-2, text, fontsize=10, zorder=3)
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
    equation = find_linear_equation(p1,p2)
    slope, y_intersect = equation
    x1,y1 = p1
    x2,y2 = p2
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
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf8')


def create_p_prism(numOfPoints,length,height):
    def find_p_middle(p1=tuple,p2=tuple):
        return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
    def move_p_to_center(p_list=list,center_index=-1):
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
    def move_p_single(p=tuple,x_move=0,y_move=0):
        return (p[0]+x_move,p[1]+y_move)
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
    def create_p_regular(n=3,length=50,move_x=0,move_y=0):
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
        polygon = [(0,0)]
        for i in range(n-1):
            temp_p = new_p_angle(angle,length,temp_p)
            polygon.append(temp_p)
            polygon = rotate_p(polygon,180-angle)
            temp_p = (rotate_p([temp_p],180-angle))[0]

        polygon = move_to_center(polygon)
        polygon = move_p(polygon,move_x,move_y)
        return polygon
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
    def squeeze_regular(p_list=list,squeeze_level=10,numOfPoints=5):
        #find p_left,p_right
        p_left = p_list[0]
        index_left = 0
        p_right = p_list[0]
        index_right = 0
        exceptionP_list = []
        for i in range(len(p_list)):
            p = p_list[i]
            if p[0] <= p_left[0]:
                p_left = p
                index_left = i
            if p[0] > p_right[0]:
                p_right = p
                index_right = i

        #cp_y
        cp_y = (p_left[1] + p_right[1]) / 2
        #cp_x
        cp_x = (p_right[0] + p_left[0]) / 2
        #moving pts
        for i in range(len(p_list)):
            p = p_list[i]
            x,y = p
            if y in [p_left[1],p_right[1]]:
                if numOfPoints == 8:
                    if i == 0:
                        p = move_p_single(p,0,squeeze_level)
                pass
            elif y > cp_y:
                if numOfPoints == 7:
                    if i == 2:
                        p = move_p_single(p,0, -(squeeze_level*2.3))
                    else:
                        p = move_p_single(p,0, -(squeeze_level*1.5))
                elif numOfPoints == 8:
                    if i in [2,3]:
                        p = move_p_single(p,0,-squeeze_level)
                elif numOfPoints == 9:
                    if i == 3:
                        p = move_p_single(p,0, -(squeeze_level+5))
                    else:
                        p = move_p_single(p,0, -(squeeze_level))
                elif numOfPoints == 10:
                    if i in [2,5]:
                        p = move_p_single(p,0, -(squeeze_level*0.8))
                    else:
                        p = move_p_single(p,0, -(squeeze_level*1.3))
                else:
                    p = move_p_single(p,0, -(squeeze_level))
            elif y < cp_y:
                if numOfPoints == 8:
                    p = move_p_single(p,0, squeeze_level)
                    if i in [6,7]:
                        p = move_p_single(p,0, squeeze_level)
                elif numOfPoints == 9:
                    if i in [0,6]:
                        p = move_p_single(p,0, squeeze_level*0.6)
                    else:
                        p = move_p_single(p,0, squeeze_level)
                elif numOfPoints == 10:
                    if i == 7:
                        p = move_p_single(p,0, squeeze_level*0.8)
                    elif i == 0:
                        p = move_p_single(p,0, squeeze_level*0.6)
                    else:
                        p = move_p_single(p,0, squeeze_level)
                else:
                    p = move_p_single(p,0, squeeze_level)
            if x > cp_x:
                if numOfPoints == 8:
                    p = move_p_single(p,-squeeze_level*0.4,0)
                else:
                    p = move_p_single(p,-squeeze_level*0.1,0)
            elif x < cp_x:
                if numOfPoints == 8:
                    p = move_p_single(p,squeeze_level*0.4,0)
                else:
                    p = move_p_single(p,squeeze_level*0.1,0)
            #redirect index
            if i == index_right:
                p_right_new = p
            if i == index_left:
                p_left_new = p
            p_list[i] = p
        return p_list,p_left_new,p_right_new
    def move_p2p(p_list=list,before_p=0,after_p=0):
        #center point
        x_move = after_p[0] - before_p[0]
        y_move = after_p[1] - before_p[1]
        new_p_list = []
        for index in range(len(p_list)):
            p = p_list[index]
            new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
    #generate variable
    length *= 11
    height *= 11
    #generate polygon - 3,4 are exeptional case
    polygon = create_p_regular(numOfPoints,length)
    polygon = resize_polygon(polygon,35)
    if numOfPoints not in [3,4]:
        noon,p_left,p_right = squeeze_regular(polygon,numOfPoints=numOfPoints)
    elif numOfPoints == 3:
        polygon[0] = (polygon[0][0], polygon[0][1]-20)
        polygon = flip_p(polygon,'y')
        p_left,p_right = polygon[0],polygon[1]
    elif numOfPoints == 4:
        polygon = create_p_rhombus(length*1.5,length*0.6*1.5)
        p_left,p_right = polygon[1],polygon[3]

    p_top = find_p_middle(p_left,p_right)
    p_top = (p_top[0],p_top[1]+height)
    polygon_t = move_p2p(polygon,find_p_middle(p_left,p_right),p_top)

    inner_list = []
    outter_list = []
    front_check = False
    if numOfPoints not in [3,4,8,9,10]:
        for i in range(len(polygon)):
            p = polygon[i]
            p_next = polygon[(i+1)%len(polygon)]
            p_next_next = polygon[(i+2)%len(polygon)]
            p_t = polygon_t[i]
            p_next_t = polygon_t[(i+1)%len(polygon_t)]
            p_next_next_t = polygon_t[(i+2)%len(polygon_t)]
            if p == p_right:
                front_check = True
                inner_list.pop()
            if front_check: #front
                outter_list.append([p,p_next,p_next_t,p_t])
            else: #back
                inner_list.append([p,p_next])
                inner_list.append([p_next,p_next_t])
        outter_list.append(polygon_t)
    elif numOfPoints == 3:
        inner_list = [
            [polygon[0],polygon[1]]
        ]
        outter_list = [
            [polygon[1],polygon[2],polygon_t[2],polygon_t[1]],
            [polygon[2],polygon[0],polygon_t[0],polygon_t[2]],
            polygon_t
        ]
    elif numOfPoints == 4:
        inner_list = [
            [polygon[3],polygon[0]],
            [polygon[0],polygon[1]]
        ]
        outter_list = [
            [polygon[1],polygon[2],polygon_t[2],polygon_t[1]],
            [polygon[2],polygon[3],polygon_t[3],polygon_t[2]],
            polygon_t
        ]
    elif numOfPoints >= 8:
        for i in range(len(polygon)):
            p = polygon[i]
            p_next = polygon[(i+1)%len(polygon)]
            p_next_next = polygon[(i+2)%len(polygon)]
            p_t = polygon_t[i]
            p_next_t = polygon_t[(i+1)%len(polygon_t)]
            p_next_next_t = polygon_t[(i+2)%len(polygon_t)]
            if p[1] == p_right[1]:
                front_check = True
                inner_list.pop()
            if front_check: #front
                outter_list.append([p,p_next,p_next_t,p_t])
                if i == len(polygon)-1:
                    outter_list.append([p_next,p_next_next,p_next_next_t,p_next_t])
            else: #back
                inner_list.append([p,p_next])
                inner_list.append([p_next,p_next_t])
        outter_list.append(polygon_t)
    #resize/move_to_center
    all_list = []
    for i in range(len(outter_list)):
        temp_list = outter_list[i]
        all_list += temp_list
    for i in range(len(inner_list)):
        temp_list = inner_list[i]
        all_list += temp_list
    all_list = move_p_to_center(all_list)
    for i in range(len(outter_list)):
        temp_list = all_list[:len(outter_list[i])]
        outter_list[i] = temp_list
        all_list = all_list[len(outter_list[i]):]
    for i in range(len(inner_list)):
        temp_list = all_list[:len(inner_list[i])]
        inner_list[i] = temp_list
        all_list = all_list[len(inner_list[i]):]
    return outter_list,inner_list
def create_p_prismNet(n=3,length=5,height=8,scale=100,move_x=0,move_y=0):
    def create_p_regular(n=3,scale=100,move_x=0,move_y=0):
        import random, math
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
    def move_p_to_center(p_list=list,center_index=-1):
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
    def move_p2p(p_list=list,before_p=0,after_p=0):
        #center point
        x_move = after_p[0] - before_p[0]
        y_move = after_p[1] - before_p[1]
        new_p_list = []
        for index in range(len(p_list)):
            p = p_list[index]
            new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
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
        return new_p_num

    #generate polygon
    polygon = create_p_regular(n,length*2)
    polygon = [polygon[len(polygon)-1]] + polygon[:len(polygon)-1]
    polygon_flip = flip_p(polygon,'y')
    p_cp = polygon[0]
    p_flip_cp = polygon_flip[len(polygon_flip)-1]

    p_inner_list = []
    p_outter_list = [(0,0)]
    first_p = (0,0)
    for i in range(1,n*2+1):
        if i == 1:#upper
            temp_p = (length,0)
            polygon = move_p2p(polygon,p_cp,temp_p)
            p_outter_list += polygon[:len(polygon)-1]
            p_inner_list.append([temp_p,(temp_p[0]+length,temp_p[1])])
            p_inner_list.append([temp_p,(temp_p[0],temp_p[1]-height)])
        elif i < n:
            temp_p = (temp_p[0]+length,temp_p[1])
            p_outter_list.append(temp_p)
            p_inner_list.append([temp_p,(temp_p[0],temp_p[1]-height)])
        elif i == n:
            temp_p = (temp_p[0]+length,temp_p[1])
            p_outter_list.append(temp_p)
            temp_p = (temp_p[0],temp_p[1]-height)
            p_outter_list.append(temp_p)
        elif i > n:
            if i-n == 2: #lower
                temp_p = (temp_p[0]-length,temp_p[1])
                polygon_flip = move_p2p(polygon_flip,p_flip_cp,temp_p)
                p_outter_list += polygon_flip
                p_inner_list.append([temp_p,(temp_p[0]+length,temp_p[1])])
            else:
                temp_p = (temp_p[0]-length,temp_p[1])
                p_outter_list.append(temp_p)
    p_all_list = p_outter_list.copy()
    for p_inner in p_inner_list:
        p_all_list += p_inner
    p_all_list = move_p_to_center(p_all_list)
    p_all_list = resize_polygon(p_all_list)
    p_outter_list = p_all_list[:len(p_outter_list)].copy()
    p_all_list = p_all_list[len(p_outter_list):]
    for i in range(len(p_inner_list)):
        p_inner_list[i] = [p_all_list[i*2],p_all_list[i*2+1]]
    return p_outter_list,p_inner_list
def create_p_pyramid(numOfPoints,length,height,move_x=0,move_y=0):
    def find_p_middle(p1=tuple,p2=tuple):
        return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
    def move_p_to_center(p_list=list,center_index=-1):
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
    def move_p_single(p=tuple,x_move=0,y_move=0):
        return (p[0]+x_move,p[1]+y_move)
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
            p_list.reverse()
        return p_list
    def create_p_regular(n=3,length=50,move_x=0,move_y=0):
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
        polygon = [(0,0)]
        for i in range(n-1):
            temp_p = new_p_angle(angle,length,temp_p)
            polygon.append(temp_p)
            polygon = rotate_p(polygon,180-angle)
            temp_p = (rotate_p([temp_p],180-angle))[0]

        polygon = move_to_center(polygon)
        polygon = move_p(polygon,move_x,move_y)
        return polygon
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
    def squeeze_regular(p_list=list,squeeze_level=20,numOfPoints=5):
        #find p_left,p_right
        p_left = p_list[0]
        index_left = 0
        p_right = p_list[0]
        index_right = 0
        exceptionP_list = []
        for i in range(len(p_list)):
            p = p_list[i]
            if p[0] <= p_left[0]:
                p_left = p
                index_left = i
            if p[0] > p_right[0]:
                p_right = p
                index_right = i

        #cp_y
        cp_y = (p_left[1] + p_right[1]) / 2
        #cp_x
        cp_x = (p_right[0] + p_left[0]) / 2
        #moving pts
        for i in range(len(p_list)):
            p = p_list[i]
            x,y = p
            if y in [p_left[1],p_right[1]]:
                pass
            elif y > cp_y:
                if numOfPoints in [7,10]:    
                    p = move_p_single(p,0, -(squeeze_level+13))
                else:
                    p = move_p_single(p,0, -(squeeze_level))
            elif y < cp_y:
                if numOfPoints == 8:
                    p = move_p_single(p,0, squeeze_level)
                    if x not in [p_left[0],p_right[0]]:
                        p = move_p_single(p,0, squeeze_level)
                    else:
                        p = move_p_single(p,0, squeeze_level*0.3)
                else:
                    p = move_p_single(p,0, squeeze_level)
            if x > cp_x:
                p = move_p_single(p,-squeeze_level*0.1,0)
            elif x < cp_x:
                p = move_p_single(p,squeeze_level*0.1,0)
            #redirect index
            if i == index_right:
                p_right_new = p
            if i == index_left:
                p_left_new = p
            p_list[i] = p
        return p_list,p_left_new,p_right_new
    length *= 50
    height *= 50
    #generate polygon - 3,4 are exeptional case
    polygon = create_p_regular(numOfPoints,length)
    if numOfPoints not in [3,4]:
        noon,p_left,p_right = squeeze_regular(polygon,numOfPoints=numOfPoints)
    elif numOfPoints == 3:
        polygon[0] = (polygon[0][0], polygon[0][1]-20)
        polygon = flip_p(polygon,'y')
        p_left,p_right = polygon[0],polygon[1]
    elif numOfPoints == 4:
        polygon = create_p_rhombus(length*1.5,length*0.6*1.5)
        p_left,p_right = polygon[1],polygon[3]
    p_top = find_p_middle(p_left,p_right)
    p_top = (p_top[0],p_top[1]+height)
    inner_list = []
    outter_list = []
    front_check = False
    if numOfPoints not in [3,4,8,9,10]:
        for i in range(len(polygon)):
            p = polygon[i]
            p_next = polygon[(i+1)%len(polygon)]
            p_next_next = polygon[(i+2)%len(polygon)]
            if p[1] == p_right[1]:
                front_check = True
            if front_check: #front
                outter_list.append([p,p_next,p_top])
            else: #back
                inner_list.append([p,p_next,p_top])
    elif numOfPoints == 3:
        p_top = (p_top[0],p_top[1]-height*0.3)
        inner_list = [
            [polygon[0],polygon[1]]
        ]
        outter_list = [
            [polygon[1],polygon[2],p_top],
            [polygon[2],polygon[0],p_top]
        ]
    elif numOfPoints == 4:
        inner_list = [
            [polygon[3],polygon[0],p_top],
            [polygon[0],polygon[1]]
        ]
        outter_list = [
            [polygon[1],polygon[2],p_top],
            [polygon[2],polygon[3],p_top],
        ]
    elif numOfPoints >= 8:
        for i in range(len(polygon)):
            p = polygon[i]
            p_next = polygon[(i+1)%len(polygon)]
            p_next_next = polygon[(i+2)%len(polygon)]
            if p[1] == p_right[1]:
                front_check = True
            if front_check: #front
                outter_list.append([p,p_next,p_top])
                if i == len(polygon)-1:
                    outter_list.append([p_next,p_next_next,p_top])
            else: #back
                inner_list.append([p,p_next,p_top])
    #resize/move_to_center
    all_list = []
    for i in range(len(outter_list)):
        temp_list = outter_list[i]
        all_list += temp_list
    for i in range(len(inner_list)):
        temp_list = inner_list[i]
        all_list += temp_list
    all_list = resize_polygon(all_list)
    all_list = move_p_to_center(all_list)
    for i in range(len(outter_list)):
        temp_list = all_list[:len(outter_list[i])]
        outter_list[i] = temp_list
        all_list = all_list[len(outter_list[i]):]
    for i in range(len(inner_list)):
        temp_list = all_list[:len(inner_list[i])]
        inner_list[i] = temp_list
        all_list = all_list[len(inner_list[i]):]
    return outter_list,inner_list
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
def move_p_to_center(p_list=list,center_index=-1):
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
    p_list = new_p_list
    return new_p_list
def move_p_single(p,x_move=0,y_move=0):
        new_p = (p[0]+x_move,p[1]+y_move)
        return new_p

#6-1-2-09
def prism612_Stem_001():
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
    char_list = ['영','일','이','삼','사','오','육','칠','팔','구','십']
    numOfBottomPts = random.randint(3,10)
    numOfBottomPts_str = char_list[numOfBottomPts]
    length = 2
    height = 6
    #generate polygon
    prism_outter,prism_inner = create_p_prism(numOfBottomPts,length,height)
    #draw
    drawPolygon_multiple(ax,prism_outter,True,0.5,color='lightsteelblue')
    drawPolygon_multiple(ax,prism_inner,dash=True)
    #stem/answer/comment
    stem = "각기둥의 이름을 써 보세요."
    answer = "(답): %s각기둥"%(numOfBottomPts_str)
    comment = "(해설) 밑면의 모양이 %s각형이므로 %s각기둥입니다."%(
        numOfBottomPts_str,numOfBottomPts_str
    )
    #plt.show()
    svg= saveSvg()
    return stem,answer,comment,svg

#6-1-2-12
def prism612_Stem_002():
    #generate variable
    char_list = ['삼','사','오','육','칠','팔','구','십']
    numOfAngles_str = random.choice(char_list)
    stem = "밑면의 모양이 %s각형인 각기둥의 이름은 무엇인가요?"%(numOfAngles_str)
    answer = "(답): %s각기둥"%(numOfAngles_str)
    comment = "(해설) 밑면의 모양이 %s각형이므로 %s각기둥입니다."%(numOfAngles_str,numOfAngles_str)
    return stem,answer,comment

#6-1-2-17
def prism612_Stem_003():
    #generate variable
    char_list = ['영','일','이','삼','사','오','육','칠','팔','구','십']
    numOfAngles = random.randint(3,10)
    numOfAngles_str = char_list[numOfAngles]
    sumOfEdges = numOfAngles * 3
    stem = "모서리가 $$수식$$%s$$/수식$$개인 각기둥이 있습니다. 이 각기둥의\n"%sumOfEdges
    stem += "이름은 무엇인가요?"
    answer = "(답): %s각기둥"%(numOfAngles_str)
    comment = "(해설) 각기둥에서 모서리의 수는 $$수식$$□ \\times 3$$/수식$$입니다.\n"
    comment += "$$수식$$□ \\times 3 = %s$$/수식$$에서 $$수식$$□ = %s$$/수식$$이므로 %s각기둥입니다."%(
        sumOfEdges, numOfAngles, numOfAngles_str
    )
    return stem,answer,comment

#6-1-2-18
def prism612_Stem_004():
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
    char_list = ['영','일','이','삼','사','오','육','칠','팔','구','십']
    numOfBottomPts = random.randint(3,6)
    numOfBottomPts_str = char_list[numOfBottomPts]
    polygon_name = '정%s각형'%(numOfBottomPts_str)
    if numOfBottomPts <= 5:
        length = random.randint(3,5)
        height = random.randint(3,8)
    elif numOfBottomPts > 5:
        length = random.randint(3,5)
        height = random.randint(8,12)
    sumOfEdges = numOfBottomPts * (length*2 + height)
    #generate polygon
    prism_outter,prism_inner = create_p_prism(numOfBottomPts,length,height)
    regular_t = prism_outter[len(prism_outter)-1]
    index = int((numOfBottomPts)/2)
    if numOfBottomPts >= 7: index += 1
    elif numOfBottomPts == 4: index -= 1
    p_top_before = regular_t[index-1]
    p_top = regular_t[index]
    p_bottom = prism_inner[len(prism_inner)-1][1]
    #draw
    drawPolygon_multiple(ax,prism_outter,True,0.5,color='lightsteelblue')
    drawPolygon_multiple(ax,prism_inner,dash=True)
    if numOfBottomPts == 3:
        drawArc(ax,[p_top_before,p_top],'top','$%s \mathrm{cm}$'%(length))
    else:
        drawArc(ax,[p_top_before,p_top],'right','$%s \mathrm{cm}$'%(length))
    drawArc(ax,[p_bottom,p_top],'right','$%s \mathrm{cm}$'%(height))
    #stem/answer/comment
    stem ="다음 각기둥의 밑면이 %s일 때 모든 모서리의\n"\
            "길이의 합은 몇 $$수식$$rm cm$$/수식$$인가요?"%(polygon_name)
    answer = '(답): $$수식$$%srm cm$$/수식$$'%(sumOfEdges)
    comment = "(해설) $$수식$$%srm cm$$/수식$$인 모서리가 $$수식$$%s$$/수식$$개, $$수식$$%srm cm$$/수식$$인 모서리가 $$수식$$%s$$/수식$$개\n"\
                "입니다.\n"\
                "\\rightarrow (모든 모서리의 길이의 합)\n"\
                "$$수식$$= %s \\times %s + %s \\times %s = %s + %s = %s(rm cm)$$/수식$$"%(
                    length, numOfBottomPts*2, height,numOfBottomPts,
                    length, numOfBottomPts*2, height, numOfBottomPts, length*numOfBottomPts*2,height*numOfBottomPts, sumOfEdges
                )
    #plt.show()
    svg= saveSvg()
    return stem,answer,comment,svg

#6-1-2-27
def prism612_Stem_005():
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
    char_list = ['영','일','이','삼','사','오','육','칠','팔','구','십']
    numOfPoints = random.randint(3,7)
    numOfEdges = numOfPoints * 3
    numOfPoints_str = char_list[numOfPoints]
    #generate polygon
    prismNet_outter, prismNet_inner = create_p_prismNet(numOfPoints)
    #draw
    drawPolygon(ax,prismNet_outter,True,0.5)
    drawPolygon_multiple(ax,prismNet_inner,dash=True)
    #stem/answer/comment
    stem = "전개도를 접었을 때 만들어지는 각기둥의 모서리는\n"\
            "몇 개인가요?"
    answer = '(답): $$수식$$%s$$/수식$$개'%(numOfEdges)
    comment = "(해설) 밑면의 모양이 %s각형이고 옆면의 모양이 직사각형\n"\
                "이므로 %s각기둥입니다.\n"\
                "따라서 %s각기둥의 모서리는 $$수식$$%s \\times 3 = %s$$/수식$$ (개)입니다."%(
                    numOfPoints_str,
                    numOfPoints_str,
                    numOfPoints_str, numOfPoints, numOfEdges
                )

    #plt.show()
    svg= saveSvg()
    return stem,answer,comment,svg

#6-1-2-29
def prism612_Stem_006():
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
    length = random.randint(4,8)
    height = random.randint(7,16)
    char_list = ['영','일','이','삼','사','오','육','칠','팔','구','십']
    numOfPoints = random.randint(3,7)
    numOfPoints_str = char_list[numOfPoints]
    sumOfEdges = length*numOfPoints*2 + height*numOfPoints

    #generate polygon
    prismNet_outter, prismNet_inner = create_p_prismNet(numOfPoints,length,height)
    show_length = []
    for i in range(len(prismNet_outter)):
        temp_str = ""
        if i == 2:
            temp_str = '$%s \mathrm{cm}$'%(length)
        elif i == numOfPoints*2-2:
            temp_str = '$%s \mathrm{cm}$'%(height)
        show_length.append(temp_str)
    #draw
    drawPolygon(ax,prismNet_outter,True,0.5)
    drawPolygon_multiple(ax,prismNet_inner,dash=True)
    drawPolygonArc(ax,prismNet_outter,show_text=show_length)
    #stem/answer/comment
    stem = "다음 전개도를 접어서 만든 각기둥에 대한 조건을\n"\
            "보고 밑면의 한 변의 길이는 몇 $$수식$$rm cm$$/수식$$인가요?\n"\
            "$$수식$$\\cdot$$/수식$$ 각기둥의 높이는 $$수식$$%srm cm$$/수식$$입니다.\n"\
            "$$수식$$\\cdot$$/수식$$ 각기둥의 옆면은 모두 합동이다.\n"\
            "$$수식$$\\cdot$$/수식$$ 각기둥의 모든 모서리의 길이의 합은 $$수식$$%srm cm$$/수식$$입니다."%(
                height,
                sumOfEdges
            )
    answer = "(답): $$수식$$%srm cm$$/수식$$"%(length)
    comment = "(해설) 옆면이 모두 합동이므로 밑면의 변의 길이는 모두\n"\
                "같습니다. 두 밑면의 모서리의 길이의 합은\n"\
                "$$수식$$%s - %s \\times %s = %s(rm cm)$$/수식$$입니다.\n"\
                "한 밑면의 모서리의 길이의 합은\n"\
                "$$수식$$%s$$/수식$$ $$수식$$\\\\div$$/수식$$ $$수식$$2 = %s(rm cm)$$/수식$$이므로 밑면의 한 변의 길이는\n"\
                "$$수식$$%s$$/수식$$ $$수식$$\\\\div$$/수식$$ $$수식$$%s = %s(rm cm)$$/수식$$입니다."%(
                    sumOfEdges,height,numOfPoints,length*numOfPoints*2,
                    length*numOfPoints*2,length*numOfPoints,
                    length*numOfPoints,numOfPoints,length
                )

    #plt.show()
    svg= saveSvg()
    return stem,answer,comment,svg

#6-1-2-32
def prism612_Stem_007():
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
    length = random.randint(4,8)
    height = random.randint(7,16)
    char_list = ['영','일','이','삼','사','오','육','칠','팔','구','십']
    numOfPoints = random.randint(3,7)
    numOfPoints_str = char_list[numOfPoints]
    areaOfSide = length*numOfPoints*height

    #generate polygon
    prismNet_outter, prismNet_inner = create_p_prismNet(numOfPoints,length,height)
    show_length = []
    for i in range(len(prismNet_outter)):
        temp_str = ""
        if i == 2:
            temp_str = '$%s \mathrm{cm}$'%(length)
        elif i == numOfPoints*2-2:
            temp_str = '$%s \mathrm{cm}$'%(height)
        show_length.append(temp_str)
    #draw
    drawPolygon(ax,prismNet_outter,True,0.5)
    drawPolygon_multiple(ax,prismNet_inner,dash=True)
    drawPolygonArc(ax,prismNet_outter,show_text=show_length)
    #stem/answer/comment
    stem = "다음은 밑면의 모양이 정%s각형인 각기둥의\n"\
            "전개도입니다. 모든 옆면의 넓이의 합은 몇 $$수식$$rm cm^{2}$$/수식$$\n"\
            "인가요?"%(numOfPoints_str)
    answer = '(답): $$수식$$%srm cm^{2}$$/수식$$'%(areaOfSide)
    comment = "(해설) 밑면의 모양이 정%s각형이므로\n"\
                "(옆면의 가로의 합) $$수식$$= %s \\times %s = %s(rm cm)$$/수식$$\n"\
                "(옆면의 세로) $$수식$$= %srm cm$$/수식$$\n"\
                "(모든 옆면의 넓이의 합)\n"\
                "$$수식$$= %s \\times %s = %s(rm cm^{2})$$/수식$$"%(
                    numOfPoints_str,
                    length,numOfPoints,(length*numOfPoints),
                    height,
                    (length*numOfPoints),height,areaOfSide
                )

    #plt.show()
    svg= saveSvg()
    return stem,answer,comment,svg

#6-1-2-35
def prism612_Stem_008():
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
    numOfPoints = random.randint(3,9)
    numOfBottom = 1
    numOfSides = numOfPoints
    #generate polygon
    pyramid_outter,pyramid_inner = create_p_pyramid(numOfPoints,1,2)
    #draw
    drawPolygon_multiple(ax,pyramid_outter,True,0.5,color='lightsteelblue')
    drawPolygon_multiple(ax,pyramid_inner,dash=True)
    #stem/answer/comment
    stem = "다음 각뿔의 밑면과 옆면은 각각 몇 개인가요?"
    answer = "(답): $$수식$$%s$$/수식$$개, $$수식$$%s$$/수식$$개"%(numOfBottom,numOfSides)
    comment = "(해설) 밑면: 밑에 놓인 면이므로 $$수식$$%s$$/수식$$개입니다.\n"\
                " 옆면: 밑면과 만나는 면이므로 $$수식$$%s$$/수식$$개입니다." %(
                    numOfBottom,
                    numOfSides
                )
    #plt.show()
    svg = saveSvg()
    return stem,answer,comment,svg

#6-1-2-48
def prism612_Stem_009():
    #generate variable
    length = random.randint(4,8)
    height = random.randint(7,16)
    char_list = ['영','일','이','삼','사','오','육','칠','팔','구','십']
    numOfPoints = random.randint(3,7)
    numOfPoints_str = char_list[numOfPoints]
    #stem/answer/comment
    stem = "밑면의 꼭짓점이 $$수식$$%s$$/수식$$개인 각뿔의 이름은 무엇인가요?"%(numOfPoints)
    answer = "(답): %s각뿔"%(numOfPoints_str)
    comment = "(해설) 밑면의 꼭짓점이 $$수식$$%s$$/수식$$개이므로 밑면의 모양은\n"\
                "%s각형입니다."%(
                    numOfPoints,
                    numOfPoints_str
                )
    return stem,answer,comment

#6-1-2-50
def prism612_Stem_010():
    #generate variable
    numOfBottomPts = random.randint(3,10)
    numOfEdges = numOfBottomPts * 2
    numOfSides = numOfBottomPts + 1
    #stem/answer/comment
    stem = "모서리가 $$수식$$%s$$/수식$$개인 각뿔의 면은 몇 개인가요?" %(numOfEdges)
    answer = "(답): $$수식$$%s$$/수식$$개"%(numOfSides)
    comment = "(해설)밑면의 변의 수를 □개라고 하면\n"\
                "(모서리의 수) $$수식$$= □ \\times 2 = %s$$/수식$$,\n"\
                "$$수식$$□ = %s$$/수식$$ $$수식$$\\\\div$$/수식$$ $$수식$$2 = %s$$/수식$$\n"\
                "밑면의 변의 수가 $$수식$$%s$$/수식$$이므로\n"\
                "(면의 수) $$수식$$=$$/수식$$ (밑면의 변의 수) $$수식$$+ 1$$/수식$$\n"\
                "$$수식$$= %s + 1 = %s$$/수식$$(개)\n"\
                "따라서 모서리가 $$수식$$%s$$/수식$$개인 각뿔의 면은 $$수식$$%s$$/수식$$개입니다."%(
                    numOfEdges,
                    numOfEdges, numOfBottomPts,
                    numOfBottomPts,
                    numOfBottomPts,numOfSides,
                    numOfEdges,numOfSides
                )
    return stem,answer,comment

#6-1-2-52
def prism612_Stem_011():
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
    len_side = random.randint(8,12)
    len_bottom = random.randint(6,7)
    numOfBottomPts = random.randint(3,10)
    sumOfEdgesLength = numOfBottomPts * (len_side+len_bottom)
    #generate polygon
    triangle = create_p_triangle(right_bottom_left=[len_side,len_bottom,len_side])
    triangle = resize_polygon(triangle)
    show_length = [
        '$%s \mathrm{cm}$'%(len_side)
        ,'$%s \mathrm{cm}$'%(len_bottom)
        ,'$%s \mathrm{cm}$'%(len_side)
    ]
    #draw
    drawPolygon(ax,triangle,True)
    drawPolygonArc(ax,triangle,show_text=show_length)
    #stem/answer/comment
    stem = "옆면이 다음과 같은 이등변삼각형으로 이루어진\n"\
            "각뿔의 모든 모서리의 길이의 합이 $$수식$$%srm cm$$/수식$$입니다.\n"\
            "이 각뿔의 밑면의 변은 몇 개인가요?"%(sumOfEdgesLength)
    answer = '(답): $$수식$$%s$$/수식$$개'%(numOfBottomPts)
    comment = "(해설) 각뿔에서 밑면을 이루는 모서리의 수와 밑면을\n"\
                "이루지 않는 모서리의 수는 서로 같습니다.\n"\
                "각뿔에서 $$수식$$%srm cm$$/수식$$인 모서리의 수와 $$수식$$%srm cm$$/수식$$인 모서리의\n"\
                "수가 같습니다.\n"\
                "밑면의 변의 수를 □ 개라고 하면\n"\
                "(모든 모서리의 길이의 합)\n"\
                "$$수식$$= %s \\times □ + %s \\times □ = %s$$/수식$$,\n"\
                "$$수식$$%s \\times □ = %s$$/수식$$, $$수식$$□ = %s$$/수식$$입니다.\n"\
                "따라서 이 각뿔의 밑면의 변은 $$수식$$%s$$/수식$$개입니다."%(
                    len_bottom,len_side,
                    len_bottom,len_side,sumOfEdgesLength,
                    len_bottom+len_side,sumOfEdgesLength,numOfBottomPts,
                    numOfBottomPts
                )
    #plt.show()
    svg = saveSvg()
    return stem,answer,comment,svg

if __name__ == '__main__':
    stem, answer, comment, svg = prism612_Stem_011()
    print(stem + '\n')
    print(answer + '\n')
    print(comment + '\n')