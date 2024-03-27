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
            plt.text(cp[0]+1-l*5.5, cp[1]+2, text[i], fontsize=10, zorder=3)
        elif position[i] == 'bottom_r':
            plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5, text[i], fontsize=10, zorder=3)
        elif position[i] == 'bottom_l':
            plt.text(cp[0]-1-l*5, cp[1]-8+l*0.5, text[i], fontsize=10, zorder=3)
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
        plt.text(cp[0]-2*l-2, cp[1]-10, text, fontsize=10, zorder=3)
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

# 선분의 길이를 표시하는 bezier 곡선을 그리는 함수
def drawPolygonArc(ax,verts=list,show_length=[],show_text=[],length_ratio=10,unit='cm',alpha=1):
    def c_distance(p1=tuple, p2=tuple):
        import math
        d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
        return d
    def new_p_middle(p1=tuple,p2=tuple):
        return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
    def text_position_polygon(p_list,l):
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
        position = text_position_polygon(verts,[p1,p2])
        length = int(c_distance(p1,p2)/length_ratio)
        if show_length != []:
            if show_length[i] == True:
                drawArc(ax,p1,p2,position,'$%s \\mathrm{%s}$'%(length,unit))
        if show_text != []: 
            if show_text[i] != '':
                drawArc(ax,p1,p2,position,show_text[i])
def drawArc(ax, p_list, position, text, boxed=False,color='black'):
    if len(p_list) != 2: raise Exception('p_list has more or less than 2 elements')
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
        l -= 12
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
def drawArc_(ax, p_list, position, text, boxed=False,color='black'):
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
        l -= 13
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
        elif position == 'top_r' or position == 'right_t':
            plt.text(cp[0]+l*0.3, cp[1]+2, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'top_l' or position == 'left_t':
            plt.text(cp[0]+1-l*5, cp[1]+2, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_r' or position == 'right_b':
            plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_l' or position == 'left_b':
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
        elif position == 'top_r' or position == 'right_t':
            plt.text(cp[0]-9, cp[1]+2, text, fontsize=10, zorder=3)
        elif position == 'top_l' or position == 'left_t':
            plt.text(cp[0]+1-l*4, cp[1]+2, text, fontsize=10, zorder=3)
        elif position == 'bottom_r' or position == 'right_b':
            plt.text(cp[0]+l, cp[1]-8+l*0.5, text, fontsize=10, zorder=3)
        elif position == 'bottom_l' or position == 'left_b':
            plt.text(cp[0]-10-l*5, cp[1]+5, text, fontsize=10, zorder=3)
        else: raise Exception('no matching position')
def drawArc__(ax, p_list, position, text, boxed=False,color='black'):
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
            plt.text(cp[0]-2*l, cp[1]+3.5, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom':
            plt.text(cp[0]-2*l, cp[1]-7.5, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'left':
            plt.text(cp[0]-2-l*4.5, cp[1]-2, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'right':
            plt.text(cp[0]+l, cp[1]-2, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'top_r' or position == 'right_t':
            plt.text(cp[0]+l*0.3, cp[1]+2, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'top_l' or position == 'left_t':
            plt.text(cp[0]+1-l*5, cp[1]+2, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_r' or position == 'right_b':
            plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5, text, fontsize=10, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_l' or position == 'left_b':
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
        elif position == 'top_r' or position == 'right_t':
            plt.text(cp[0]-9, cp[1]+2, text, fontsize=10, zorder=3)
        elif position == 'top_l' or position == 'left_t':
            plt.text(cp[0]+1-l*4, cp[1]+2, text, fontsize=10, zorder=3)
        elif position == 'bottom_r' or position == 'right_b':
            plt.text(cp[0]+l, cp[1]-8+l*0.5, text, fontsize=10, zorder=3)
        elif position == 'bottom_l' or position == 'left_b':
            plt.text(cp[0]-10-l*5, cp[1]+5, text, fontsize=10, zorder=3)
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


def random_line(polygon=list):
    import random
    n = random.randint(0,len(polygon)-1)
    p1 = polygon[n]
    if n == (len(polygon)-1): p2 = polygon[0]
    else: p2 = polygon[n+1]
    return [p1,p2]

def find_p_middle(p1=tuple,p2=tuple):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def create_p_cuboid(length,width,height,move_x=0,move_y=0,scale=90):
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
    def move_p(p_list=list,x_move=0,y_move=0):
        #center point
        new_p_list = []
        for index in range(len(p_list)):
            p = p_list[index]
            new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
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
    def create_p_parallelogram_edge(left_angle=0,side=0,width=0,scale=100,move_x=0,move_y=0):
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
        parallelogram = rotate_p(parallelogram,90-left_angle)
        return parallelogram
    def create_p_parallelogram_middle(left_angle=0,side=0,width=0,scale=100,move_x=0,move_y=0):
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
        parallelogram = rotate_p(parallelogram,90-left_angle)
        return parallelogram
    def create_p_parallelogram_top(left_angle=0,side=0,width=0,scale=100,move_x=0,move_y=0):
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
        parallelogram = rotate_p(parallelogram,355)
        return parallelogram
    new_width = width*0.8
    widthHeight_part_left = create_p_parallelogram_edge(45,height,new_width)
    lengthHeight_part_front = create_p_parallelogram_middle(95,height,length)
    lengthWidth_part_bottom = create_p_parallelogram_top(50,new_width,length)
    p_widthHeightFBL = widthHeight_part_left[3]
    p_widthHeightFTR = lengthHeight_part_front[2]
    move_xy_widthHeight_L2R = (p_widthHeightFTR[0] - p_widthHeightFBL[0],p_widthHeightFTR[1]-p_widthHeightFBL[1])
    widthHeight_part_right = move_p(widthHeight_part_left,move_xy_widthHeight_L2R[0],move_xy_widthHeight_L2R[1])
    p_widthHeightFTR = widthHeight_part_right[2]
    p_widthHeightFBR = widthHeight_part_right[3]
    move_xy_lengthHeight_F2B = (p_widthHeightFTR[0]-p_widthHeightFBR[0],p_widthHeightFTR[1]-p_widthHeightFBR[1])
    lengthHeight_part_back = move_p(lengthHeight_part_front,move_xy_lengthHeight_F2B[0],move_xy_lengthHeight_F2B[1])
    p_lengthWidthBBL = lengthWidth_part_bottom[3]
    p_widthHeightFTL = widthHeight_part_left[0]
    move_xy_lengthWidth_B2T = (p_widthHeightFTL[0]-p_lengthWidthBBL[0],p_widthHeightFTL[1]-p_lengthWidthBBL[1])
    lengthWidth_part_top = move_p(lengthWidth_part_bottom,move_xy_lengthWidth_B2T[0],move_xy_lengthWidth_B2T[1])
    #move
    all_part = lengthHeight_part_front+widthHeight_part_right+lengthWidth_part_top+lengthHeight_part_back+widthHeight_part_left+lengthWidth_part_bottom
    all_after_resize = resize_polygon(all_part,scale)
    all_after_move = move_p_to_center(all_after_resize)
    all_after_move = move_p(all_after_move,move_x,move_y)
    lengthHeight_part_front,widthHeight_part_right,lengthWidth_part_top = all_after_move[:4],all_after_move[4:8],all_after_move[8:12]
    lengthHeight_part_back,widthHeight_part_left,lengthWidth_part_bottom = all_after_move[12:16],all_after_move[16:20],all_after_move[20:24]
    
    front_part = [lengthHeight_part_front] + [widthHeight_part_right] + [lengthWidth_part_top]
    back_part = [lengthHeight_part_back] + [widthHeight_part_left] + [lengthWidth_part_bottom]
    back_part = [
        [lengthHeight_part_back[2],lengthHeight_part_back[3]],
        [lengthHeight_part_back[3],lengthHeight_part_back[0]],
        [widthHeight_part_left[2],widthHeight_part_left[3]]
    ]
    return front_part,back_part
def create_p_cube_net(length,move_x=0,move_y=0):
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
    def move_p(p_list=list,x_move=0,y_move=0):
        #center point
        new_p_list = []
        for index in range(len(p_list)):
            p = p_list[index]
            new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
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
    p_outter_list = []
    temp_p = (0,0)
    p_outter_list.append(temp_p)
    temp_p = move_p([temp_p],10,0)
    p_outter_list.append(temp_p[0])
    temp_p = move_p(temp_p,0,10)
    p_outter_list.append(temp_p[0])
    temp_p = move_p(temp_p,10,0)
    p_outter_list.append(temp_p[0])
    temp_p = move_p(temp_p,0,-10)
    p_outter_list.append(temp_p[0])
    temp_p = move_p(temp_p,10,0)
    p_outter_list.append(temp_p[0])
    temp_p = move_p(temp_p,10,0)
    p_outter_list.append(temp_p[0])
    temp_p = move_p(temp_p,0,-10)
    p_outter_list.append(temp_p[0])
    temp_p = move_p(temp_p,-10,0)
    p_outter_list.append(temp_p[0])
    temp_p = move_p(temp_p,-10,0)
    p_outter_list.append(temp_p[0])
    temp_p = move_p(temp_p,0,-10)
    p_outter_list.append(temp_p[0])
    temp_p = move_p(temp_p,-10,0)
    p_outter_list.append(temp_p[0])
    temp_p = move_p(temp_p,0,10)
    p_outter_list.append(temp_p[0])
    temp_p = move_p(temp_p,-10,0)
    p_outter_list.append(temp_p[0])
    
    p_outter_list = resize_polygon(p_outter_list)
    p_inner_list = [
        [p_outter_list[1],p_outter_list[4],p_outter_list[9],p_outter_list[12]],
        [p_outter_list[5],p_outter_list[8]]
    ]
    return p_outter_list,p_inner_list
def create_p_cuboid_net(length,width,height,move_x=0,move_y=0,scale=90,typeNum=-1):
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
    def move_p(p_list=list,x_move=0,y_move=0):
        #center point
        new_p_list = []
        for index in range(len(p_list)):
            p = p_list[index]
            new_p_list.append((p[0]+x_move,p[1]+y_move))
        return new_p_list
    def move_p_single(p,x_move=0,y_move=0):
        new_p = (p[0]+x_move,p[1]+y_move)
        return new_p
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
    if typeNum == -1:
        typeNum = random.randint(0,2)
    p_outter_list = []
    temp_p = (0,0)
    p_outter_list.append(temp_p)
    if typeNum == 0: #regular type
        temp_p = move_p([temp_p],height,0)
        p_outter_list.append(temp_p[0])
        temp_p = move_p(temp_p,0,height)
        p_outter_list.append(temp_p[0])
        temp_p = move_p(temp_p,length,0)
        p_outter_list.append(temp_p[0])
        temp_p = move_p(temp_p,0,-height)
        p_outter_list.append(temp_p[0])
        temp_p = move_p(temp_p,height,0)
        p_outter_list.append(temp_p[0])
        temp_p = move_p(temp_p,length,0)
        p_outter_list.append(temp_p[0])
        temp_p = move_p(temp_p,0,-width)
        p_outter_list.append(temp_p[0])
        temp_p = move_p(temp_p,-length,0)
        p_outter_list.append(temp_p[0])
        temp_p = move_p(temp_p,-height,0)
        p_outter_list.append(temp_p[0])
        temp_p = move_p(temp_p,0,-height)
        p_outter_list.append(temp_p[0])
        temp_p = move_p(temp_p,-length,0)
        p_outter_list.append(temp_p[0])
        temp_p = move_p(temp_p,0,height)
        p_outter_list.append(temp_p[0])
        temp_p = move_p(temp_p,-height,0)
        p_outter_list.append(temp_p[0])
        p_outter_list = resize_polygon(p_outter_list,scale)
        p_outter_list = move_p(p_outter_list,move_x,move_y)
        p_inner_list = [
            [p_outter_list[1],p_outter_list[4],p_outter_list[9],p_outter_list[12]],
            [p_outter_list[5],p_outter_list[8]]
        ]
    elif typeNum == 1: #problem47 type
        temp_p = move_p_single(temp_p,height,0)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,0,height)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,length,0)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,0,-height)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,height,0)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,length,0)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,0,-width)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,0,-height)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,-length,0)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,0,height)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,-height,0)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,-length,0)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,-height,0)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,0,width)
        p_outter_list.append(temp_p)
        p_outter_list = resize_polygon(p_outter_list,scale)
        p_outter_list = move_p(p_outter_list,move_x,move_y)
        p_inner_list = [
            [p_outter_list[1],p_outter_list[4],p_outter_list[11],p_outter_list[12]],
            [p_outter_list[5],p_outter_list[6],p_outter_list[7],p_outter_list[10]]
        ]
    elif typeNum == 2: #problem48 rype
        temp_p = move_p_single(temp_p,width,0)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,length,0)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,0,-height)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,height,0)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,0,-width)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,-height,0)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,0,-height)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,0,-width)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,-length,0)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,0,width)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,0,height)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,0,width)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,-width,0)
        p_outter_list.append(temp_p)
        temp_p = move_p_single(temp_p,0,height)
        p_outter_list.append(temp_p)
        p_outter_list = resize_polygon(p_outter_list,scale)
        p_outter_list = move_p(p_outter_list,move_x,move_y)
        p_inner_list = [
            [p_outter_list[1],p_outter_list[2],p_outter_list[3],p_outter_list[12]],
            [p_outter_list[3],p_outter_list[6]],
            [p_outter_list[6],p_outter_list[7],p_outter_list[10],p_outter_list[11]]
        ]

    

    return p_outter_list,p_inner_list
def c_은는(var):
    var= str(var)
    if 'frac' in var or 'sqrt' in var:
        if int(var[len(var)-2]) in (0,1,3,6,7,8):
            n = '은'
        else:
            n = '는'
    else:
        last_char = var[len(var)-1]
        if last_char in ('L','M','N','R','l','m','n','r'):
            n = '은'
        elif last_char in ('0','1','3','6','7','8'):
            n = '은'
        else:
            n = '는'
    return n
def c_과와(var):
    var = str(var)
    if 'frac' in var or 'sqrt' in var:
        if int(var[len(var)-2]) in (0,1,3,6,7,8):
            n = '과'
        else:
            n = '와'
    else:
        last_char = var[len(var)-1]
        if last_char in ('L','M','N','R','l','m','n','r'):
            n = '과'
        elif last_char in ('0','1','3','6','7','8'):
            n = '과'
        else:
            n = '와'
    return n


#5-2-5-05
def cuboid525_Stem_001():
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
    length, width, height = random.randint(5,10),random.randint(5,10),random.randint(5,10)
    length_str,width_str,height_str = "$%s \\mathrm{cm}$"%(length), "$%s \\mathrm{cm}$"%(width), "$%s \\mathrm{cm}$"%(height)
    length_list = random.sample([length_str,'A'],2)
    width_list = random.sample([width_str,'B'],2)
    height_list = random.sample([height_str,'C'],2)
    #generate cuboid
    cuboid_front,cuboid_back = create_p_cuboid(length*10,width*10,height*10)
    cuboid_frontF,cuboid_frontR,cuboid_frontT = cuboid_front
    #draw
    drawPolygon_multiple(ax,cuboid_front,True)
    drawPolygon_multiple(ax,cuboid_back,dash=True)
    drawPolygonArc(ax,cuboid_frontF,show_text=['','',length_list[0],height_list[0]])
    drawPolygonArc(ax,cuboid_frontR,show_text=['',height_list[1],width_list[0],''])
    drawPolygonArc(ax,cuboid_frontT,show_text=[length_list[1],'','',width_list[1]])
    #comment
    stem = "직육면체의 $$수식$$A$$/수식$$, $$수식$$B$$/수식$$, $$수식$$C$$/수식$$에 알맞은 수를 써넣으세요."
    answer = '(답): $$수식$$A = %srm cm$$/수식$$, $$수식$$B = %srm cm$$/수식$$, $$수식$$C = %srm cm$$/수식$$' %(length,width,height)
    comment = "(해설) 직육면체에는 길이가 같은 모서리가 $$수식$$4$$/수식$$개씩 $$수식$$3$$/수식$$쌍이 있습니다.\n "
    comment += "따라서 $$수식$$A = %srm cm$$/수식$$, $$수식$$B = %srm cm$$/수식$$, $$C = %srm cm$$/수식$$입니다."%(
        length,width,height
    )
    #plt.show()
    svg= saveSvg()
    return stem,answer,comment,svg

#5-2-5-13
def cuboid525_Stem_002():
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
    length = random.randint(5,10)
    width = length
    height = length
    length_str,width_str,height_str = "$%s \\mathrm{cm}$"%(length), "$%s \\mathrm{cm}$"%(width), "$%s \\mathrm{cm}$"%(height)
    str_list = [[length_str,'$□ \\mathrm{cm}$'] , [width_str,'$□ \\mathrm{cm}$'] , [height_str,'$□ \\mathrm{cm}$']]

    random_showLength = random.randint(0,2)
    random_showBox = random.randint(0,2)
    for i in range(3):
        if i != random_showLength:
            str_list[i][0] = ''
        if i != random_showBox:
            str_list[i][1] = ''
        
    length_list = random.sample(str_list[0],2)
    width_list = random.sample(str_list[1],2)
    height_list = random.sample(str_list[2],2)

    #generate cuboid
    cuboid_front,cuboid_back = create_p_cuboid(length*10,width*10,height*10)
    cuboid_frontF,cuboid_frontR,cuboid_frontT = cuboid_front
    #draw
    drawPolygon_multiple(ax,cuboid_front,True)
    drawPolygon_multiple(ax,cuboid_back,dash=True)
    drawPolygonArc(ax,cuboid_frontF,show_text=['','',length_list[0],height_list[0]])
    drawPolygonArc(ax,cuboid_frontR,show_text=['',height_list[1],width_list[0],''])
    drawPolygonArc(ax,cuboid_frontT,show_text=[length_list[1],'','',width_list[1]])
    svg = saveSvg()
    #plt.show()
    #stem/answer/comment
    stem = "정육면체를 보고 □안에 알맞은 수를 구해 보세요.\n "
    answer = '(답): $$수식$$%srm cm$$/수식$$'%str(length)
    comment = "(해설) 정육면체이므로 모서리의 길이가 $$수식$$%srm cm$$/수식$$로 모두\n " %(length)
    comment += "같습니다."
    return stem,answer,comment,svg

#5-2-5-16
def cuboid525_Stem_003():
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
    length = random.randint(5,10)
    width = length
    height = length
    length_str,width_str,height_str = "$%s \\mathrm{cm}$"%(length), "$%s \\mathrm{cm}$"%(width), "$%s \\mathrm{cm}$"%(height)
    str_list = [
        [length_str,''] , [width_str,''] , [height_str,'']
    ]
    random_showLength = random.randint(0,2)
    for i in range(3):
        if i != random_showLength:
            str_list[i][0] = ''
        
    length_list = random.sample(str_list[0],2)
    width_list = random.sample(str_list[1],2)
    height_list = random.sample(str_list[2],2)

    #generate cuboid
    cuboid_front,cuboid_back = create_p_cuboid(length*10,width*10,height*10)
    cuboid_frontF,cuboid_frontR,cuboid_frontT = cuboid_front
    #draw
    drawPolygon_multiple(ax,cuboid_front,True)
    drawPolygon_multiple(ax,cuboid_back,dash=True)
    drawPolygonArc(ax,cuboid_frontF,show_text=['','',length_list[0],height_list[0]])
    drawPolygonArc(ax,cuboid_frontR,show_text=['',height_list[1],width_list[0],''])
    drawPolygonArc(ax,cuboid_frontT,show_text=[length_list[1],'','',width_list[1]])
    svg = saveSvg()
    #plt.show()
    #stem/answer/comment
    stem = "한 모서리의 길이가 $$수식$$%srm cm$$/수식$$인 정육면체 모양의\n " %(length)
    stem += "주사위가 있습니다. 이 주사위의 모서리의 길이의\n "
    stem += "합은 몇 $$수식$$rm cm$$/수식$$인가요?"
    answer = '(답): $$수식$$%srm cm$$/수식$$'%(length*12)
    comment = "(해설) 정육면체는 모서리가 $$수식$$12$$/수식$$개이고, 모서리의 길이가\n "
    comment += "모두 같습니다.\n"
    comment += "따라서 주사위의 모서리의 길이의 합은\n "
    comment += "$$수식$$%s \\times 12 = %s(rm cm)$$/수식$$입니다." %(length,length*12)
    return stem,answer,comment,svg

#5-2-5-23
def cuboid525_Stem_004():
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
    length,width,height = random.randint(5,10),random.randint(5,10),random.randint(5,10)

    length_str,width_str,height_str = "$%s \\mathrm{cm}$"%(length), "$%s \\mathrm{cm}$"%(width), "$%s \\mathrm{cm}$"%(height)
    str_list = [
        [length_str,''] , [width_str,''] , [height_str,'']
    ]
    random_ColoredSurfaceNumber = random.randint(0,2)
    
    length_list = random.sample(str_list[0],2)
    width_list = random.sample(str_list[1],2)
    height_list = random.sample(str_list[2],2)
    transparency = 0.5
    #generate cuboid
    cuboid_front,cuboid_back = create_p_cuboid(length*10,width*10,height*10)
    cuboid_frontF,cuboid_frontR,cuboid_frontT = cuboid_front
    all_surface = [cuboid_frontF,cuboid_frontR,cuboid_frontT]
    random_surface = all_surface[random_ColoredSurfaceNumber]
    #draw
    drawPolygon_multiple(ax,cuboid_front,alpha=transparency)
    drawPolygon_multiple(ax,cuboid_back,dash=True)
    drawPolygonArc(ax,cuboid_frontF,show_text=['','',length_list[0],height_list[0]],alpha=transparency)
    drawPolygonArc(ax,cuboid_frontR,show_text=['',height_list[1],width_list[0],''],alpha=transparency)
    drawPolygonArc(ax,cuboid_frontT,show_text=[length_list[1],'','',width_list[1]],alpha=transparency)
    drawPolygon(ax,random_surface,True,alpha=1)
    svg = saveSvg()
    #plt.show()
    #stem/answer/comment
    if random_ColoredSurfaceNumber == 0: #Front
        answer_len1 = length
        answer_len2 = height
    elif random_ColoredSurfaceNumber == 1: #Right
        answer_len1 = width
        answer_len2 = height
    elif random_ColoredSurfaceNumber == 2: #Top
        answer_len1 = length
        answer_len2 = width
    stem = "직육면체에서 색칠한 면과 평행한 면의 모서리의\n "
    stem += "길이의 합은 몇 $$수식$$rm cm$$/수식$$인가요?"
    answer = '(답): $$수식$$%srm cm$$/수식$$'%((answer_len1 + answer_len2)*2)
    comment = "(해설) 색칠한 면과 평행한 면은 모서리의 길이가 각각 같습니다.\n "
    comment += "따라서 색칠한 면과 평행한 면의 모서리의 길이의\n "
    comment += "합은 $$수식$$(%s+%s) \\times 2 = %s(rm cm)$$/수식$$입니다." %(
        answer_len1,answer_len2,(answer_len1 + answer_len2)*2
    )
    return stem,answer,comment,svg

#5-2-5-33,34
def cuboid525_Stem_005():
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
    problem_option = random.choice([33,34])
    while True:
        if problem_option == 33:
            length,width,height = random.randint(5,10),random.randint(5,10),random.randint(5,10)
        elif problem_option == 34:
            length,width,height = random.randint(10,30),random.randint(10,30),random.randint(10,30)
        if length != width or width != height or length != height:
            break
    length_str,width_str,height_str = "$%s \\mathrm{cm}$"%(length), "$%s \\mathrm{cm}$"%(width), "$%s \\mathrm{cm}$"%(height)
    str_list = [
        [length_str,''] , [width_str,''] , [height_str,'']
    ]
    
    length_list = random.sample(str_list[0],2)
    width_list = random.sample(str_list[1],2)
    height_list = random.sample(str_list[2],2)
    transparency = 0.5
    #generate cuboid
    cuboid_front,cuboid_back = create_p_cuboid(length*10,width*10,height*10)
    cuboid_frontF,cuboid_frontR,cuboid_frontT = cuboid_front
    all_surface = [cuboid_frontF,cuboid_frontR,cuboid_frontT]
    #draw
    drawPolygon_multiple(ax,cuboid_front,True,alpha=transparency)
    drawPolygon_multiple(ax,cuboid_back,dash=True)
    drawPolygonArc(ax,cuboid_frontF,show_text=['','',length_list[0],height_list[0]],alpha=transparency)
    drawPolygonArc(ax,cuboid_frontR,show_text=['',height_list[1],width_list[0],''],alpha=transparency)
    drawPolygonArc(ax,cuboid_frontT,show_text=[length_list[1],'','',width_list[1]],alpha=transparency)
    svg = saveSvg()
    #plt.show()
    #stem/answer/comment
    if problem_option == 33: #보이는 모서리
        stem = "다음 직육면체의 겨냥도에서 보이는 모서리의\n "
        stem += "길이의 합은 몇 $$수식$$rm cm$$/수식$$인가요?"
        answer = '(답): $$수식$$%srm cm$$/수식$$'%((length+width+height)*3)
        comment = "(해설) 길이가 $$수식$$%srm cm$$/수식$$, $$수식$$%srm cm$$/수식$$, $$수식$$%srm cm$$/수식$$인 모서리가 각각\n "%(length,width,height)
        comment += "$$수식$$3$$/수식$$개씩 보이므로\n "
        comment += "(보이는 모서리의 길이의 합)\n "
        comment += "$$수식$$=(%s+%s+%s) \\times 3 = %s(rm cm)$$/수식$$입니다." %(length,width,height,(length+width+height)*3)
    elif problem_option == 34: #보이지 않는 모서리
        stem = "직육면체의 겨냥도에서 보이지 않는 모서리의 길이의\n "
        stem += "합은 몇 $$수식$$rm cm$$/수식$$인가요?"
        answer = '(답): $$수식$$%srm cm$$/수식$$'%(length+width+height)
        comment = "(해설) 보이지 않는 모서리는 점선으로 나타낸 모서리입니다.\n "
        comment += "(보이지 않는 모서리의 길이의 합)\n "
        comment += "$$수식$$%s + %s + %s = %s (rm cm)$$/수식$$"%(
            length,width,height,length+width+height
        )
    return stem,answer,comment,svg

#5-2-5-39
def cuboid525_Stem_006():
    def find_answer(stem_answer_list,stem):
        for answer_list in stem_answer_list:
            if stem in answer_list:
                answer_list.remove(stem)
                return answer_list
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #generate polygon
    cube_net_outter,cube_net_inner = create_p_cube_net(90)
    pName_list = [
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N'
    ]
    available_stemP_list = ['A','C','D','F','G','H','I','K','L','N']
    stem_answer_list = [
        ['A','C','G'],
        ['D','F'],
        ['H','L','N'],
        ['I','K']
    ]
    p_stem = random.choice(available_stemP_list)
    p_answer = find_answer(stem_answer_list,p_stem)
    #draw
    drawPolygon(ax,cube_net_outter,True,alpha=0.5)
    drawPolygon(ax,cube_net_inner[0],alpha=0.5,dash=True)
    drawPolygon(ax,cube_net_inner[1],alpha=0.5,dash=True)
    setPolygonPoint(ax,cube_net_outter,cube_net_outter,pName_list)
    #plt.show()
    svg = saveSvg()
    #stem/answer/comment
    stem = "전개도를 접어서 정육면체를 만들었을 때, $$수식$$점%s$$/수식$$%s\n "\
            "만나는 점을 모두 찾아보세요."%(
                p_stem,c_과와(p_stem)
                )
    if len(p_answer) > 1:
        answer = '(답): $$수식$$점%s$$/수식$$,$$수식$$ 점%s$$/수식$$' %(p_answer[0],p_answer[1])
        comment_p = '$$수식$$점%s$$/수식$$%s $$수식$$점%s$$/수식$$' %(p_answer[0],c_과와(p_answer[0]),p_answer[1])
    else:
        answer = '(답): $$수식$$점%s$$/수식$$'%(p_answer[0])
        comment_p = '$$수식$$점%s$$/수식$$'%(p_answer[0])
    comment = "(해설) 정육면체의 전개도를 접으면 $$수식$$점%s$$/수식$$와 만나는 점은\n "%(p_stem)
    comment += "%s입니다." %(comment_p)
    return stem,answer,comment,svg

#5-2-5-41
def cuboid525_Stem_007():
    def find_answer(stem_answer_list,stem):
        for answer_list in stem_answer_list:
            if stem in answer_list:
                answer_list.remove(stem)
                return answer_list
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #generate polygon
    cube_net_outter,cube_net_inner = create_p_cube_net(90)
    pName_list = [
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N'
    ]
    available_lstem_list = [
        'AB','BC','CD','DE','EF','FG','GH','HI','IJ','JK','KL','LM','MN','AN'
    ]
    stem_answer_list = [
        ['AB','BC'],
        ['CD','FG'],
        ['DE','EF'],
        ['GH','AN'],
        ['HI','KL'],
        ['IJ','JK'],
        ['LM','MN']
    ]
    l_stem = random.choice(available_lstem_list)
    l_answer = find_answer(stem_answer_list,l_stem)[0]
    #draw
    drawPolygon(ax,cube_net_outter,True,alpha=0.5)
    drawPolygon(ax,cube_net_inner[0],alpha=0.5,dash=True)
    drawPolygon(ax,cube_net_inner[1],alpha=0.5,dash=True)
    setPolygonPoint(ax,cube_net_outter,cube_net_outter,pName_list)
    #plt.show()
    svg = saveSvg()
    #stem/answer/comment
    stem = "전개도를 접어서 정육면체를 만들었을 때,\n "\
            "$$수식$$선분%s$$/수식$$%s 겹치는 선분을 찾아 써 보세요."%(
                l_stem,c_과와(l_stem)
            )
    answer = '(답): $$수식$$선분%s$$/수식$$'%(l_answer)
    comment = "(해설) 전개도를 접었을 때 $$수식$$선분%s$$/수식$$%s $$수식$$선분%s$$/수식$$와\n "\
                "만나 한 모서리가 됩니다."%(
                    l_stem,c_은는(l_stem),l_answer
                    )
    return stem,answer,comment,svg

#5-2-5-48
def cuboid525_Stem_008():
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
        length,width,height = random.randint(5,10),random.randint(5,10),random.randint(5,10)
        if length != width or length != height or width != height:
            break
    length_str,width_str,height_str = "$%s \\mathrm{cm}$"%(length), "$%s \\mathrm{cm}$"%(width), "$%s \\mathrm{cm}$"%(height)
    str_list = [
        [length_str,''] , [width_str,''] , [height_str,'']
    ]
    length_list = str_list[0]
    width_list = str_list[1]
    height_list = str_list[2]
    transparency = 0.5
    typeNum = random.randint(0,2)
    #generate cuboid/cuboid_net
    cuboid_front,cuboid_back = create_p_cuboid(length*10,width*10,height*10,-50,scale=40)
    cuboid_frontF,cuboid_frontR,cuboid_frontT = cuboid_front
    cuboidNet_front,cuboidNet_back = create_p_cuboid_net(length*10,width*10,height*10,50,scale=60,typeNum=typeNum)
    p_arrowStart = find_p_middle(cuboid_frontT[0],cuboid_frontT[2])
    p_arrowEnd = (p_arrowStart[0],p_arrowStart[1]+30)
    netStr_list = [length_str,width_str,height_str]
    net_list = [length,width,height]
    char_list = ['B','C']
    stem_index = random.randint(0,2)
    answer_list = []
    for i in range(3):
        if i != stem_index:
            char = char_list.pop()
            answer_list.append(net_list[i])
            netStr_list[i] = char
    if typeNum == 0:
        p_text_x = find_p_middle(cuboidNet_front[5],cuboidNet_front[6])
        p_text_y = find_p_middle(cuboidNet_front[5],cuboidNet_front[8])
        p_text = (p_text_x[0]-1,p_text_y[1]-7)
        textOnNet = [
            '','',netStr_list[0],'','',
            '',netStr_list[1],'','',netStr_list[2],
            '','','',''
        ]
    elif typeNum == 1:
        p_text_x = find_p_middle(cuboidNet_front[5],cuboidNet_front[6])
        p_text_y = find_p_middle(cuboidNet_front[6],cuboidNet_front[7])
        p_text = (p_text_x[0]-1,p_text_y[1]-7)
        textOnNet = [
            '','',netStr_list[0],'','',
            '',netStr_list[1],netStr_list[2],'','',
            '','','','',''
        ]
    elif typeNum == 2:
        p_text_x = find_p_middle(cuboidNet_front[3],cuboidNet_front[12])
        p_text_y = find_p_middle(cuboidNet_front[3],cuboidNet_front[6])
        p_text = (p_text_x[0]-1,p_text_y[1]-7)
        textOnNet = [
            '',netStr_list[0],'','',netStr_list[1],
            '',netStr_list[2],'','','',
            '','','','',''
        ]
    #drawDot(ax,[p_text])
    #draw
    drawPolygon_multiple(ax,cuboid_front,True,alpha=transparency,color='Blue')
    drawPolygon_multiple(ax,cuboid_back,dash=True)
    drawPolygonArc(ax,cuboid_frontF,show_text=['','',length_list[0],height_list[0]],alpha=transparency)
    drawPolygonArc(ax,cuboid_frontR,show_text=['',height_list[1],width_list[0],''],alpha=transparency)
    drawPolygonArc(ax,cuboid_frontT,show_text=[length_list[1],'','',width_list[1]],alpha=transparency)
    drawArrow(ax,p_arrowEnd,p_arrowStart,True)
    drawText(ax,'A',p_arrowEnd)

    drawPolygon(ax,cuboidNet_front,True,0.5,color='royalblue')
    drawPolygon_multiple(ax,cuboidNet_back,dash=True)
    drawText(ax,'A',p_text)
    drawPolygonArc(ax,cuboidNet_front,show_text=textOnNet)
    #stem/answer/comment
    stem = "직육면체의 전개도를 그린 것입니다. $$수식$$B$$/수식$$,$$수식$$C$$/수식$$에\n "
    stem += "알맞은 수를 구해 보세요."
    answer = "(답): $$수식$$B:%srm cm$$/수식$$, $$수식$$C:%srm cm$$/수식$$" %(answer_list[0], answer_list[1])
    if typeNum == 0:
        comment = "(해설) $$수식$$면A$$/수식$$는 가로가 $$수식$$%srm cm$$/수식$$, 세로가 $$수식$$%srm cm$$/수식$$인 직사각형이고,\n" %(length,width)
        comment += "$$수식$$면A$$/수식$$의 옆에 있는 면은 가로가 $$수식$$%srm cm$$/수식$$, 세로가 $$수식$$%srm cm$$/수식$$인\n"%(height,width)
        comment += "직사각형입니다.\n "
        comment += "따라서 $$수식$$B$$/수식$$는 $$수식$$%srm cm$$/수식$$, $$수식$$C$$/수식$$는 $$수식$$%srm cm$$/수식$$입니다."%(answer_list[0],answer_list[1])
    elif typeNum == 1:
        comment = "(해설) $$수식$$면A$$/수식$$는 가로가 $$수식$$%srm cm$$/수식$$, 세로가 $$수식$$%srm cm$$/수식$$인 직사각형이고,\n" %(length,width)
        comment += "$$수식$$면A$$/수식$$의 아래에 있는 면은 가로가 $$수식$$%srm cm$$/수식$$, 세로가 $$수식$$%srm cm$$/수식$$인\n"%(width,height)
        comment += "직사각형입니다.\n "
        comment += "따라서 $$수식$$B$$/수식$$는 $$수식$$%srm cm$$/수식$$, $$수식$$C$$/수식$$는 $$수식$$%srm cm$$/수식$$입니다."%(answer_list[0],answer_list[1])
    elif typeNum == 2:
        comment = "(해설) $$수식$$면A$$/수식$$는 가로가 $$수식$$%srm cm$$/수식$$, 세로가 $$수식$$%srm cm$$/수식$$인 직사각형이고,\n" %(length,width)
        comment += "$$수식$$면A$$/수식$$의 옆에 있는 면은 가로가 $$수식$$%srm cm$$/수식$$, 세로가 $$수식$$%srm cm$$/수식$$인\n"%(height,width)
        comment += "직사각형입니다.\n "
        comment += "따라서 $$수식$$B$$/수식$$는 $$수식$$%srm cm$$/수식$$, $$수식$$C$$/수식$$는 $$수식$$%srm cm$$/수식$$입니다."%(answer_list[0],answer_list[1])

    #plt.show()
    svg = saveSvg()
    return stem,answer,comment,svg

#5-2-5-50
def cuboid525_Stem_009():
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
        length,width,height = random.randint(5,10),random.randint(5,10),random.randint(5,10)
        if length != width or length != height or width != height:
            break
    sumOfEdges = (length+width+height)*4
    length_str,width_str,height_str = "$%s \\mathrm{cm}$"%(length), "$%s \\mathrm{cm}$"%(width), "$%s \\mathrm{cm}$"%(height)

    typeNum = random.randint(0,2)
    #generate cuboid/cuboid_net
    cuboid_front,cuboid_back = create_p_cuboid(length*10,width*10,height*10,-50,scale=40)
    cuboid_frontF,cuboid_frontR,cuboid_frontT = cuboid_front
    cuboidNet_front,cuboidNet_back = create_p_cuboid_net(length*10,width*10,height*10,50,scale=60,typeNum=typeNum)
    #generate stem/comment/answer related stuffs
    edgeLenWithA_list = [length_str,width_str,height_str]
    edgeLenWithoutA_list = [length_str,width_str,height_str]
    comment_netStr_list = [length_str,width_str,height_str]
    lenCuboid_list = [length,width,height]
    stem_index = random.randint(0,2)
    for i in range(3):
        if i == stem_index:
            missing_len = lenCuboid_list.pop(i)
            edgeLenWithA_list[i] = 'A'
            edgeLenWithoutA_list[i] = ''
            comment_netStr_list[i] = 'A'
    if typeNum == 0:
        perimeter = length*4 + width*2 + height*8
        textOnNet = [
            '','',edgeLenWithoutA_list[0],'','',
            '',edgeLenWithoutA_list[1],'','',edgeLenWithoutA_list[2],
            '','','',''
        ]
    elif typeNum == 1:
        perimeter = length*4 + width*2 + height*8
        textOnNet = [
            '','',edgeLenWithoutA_list[0],'','',
            '',edgeLenWithoutA_list[1],edgeLenWithoutA_list[2],'','',
            '','','','',''
        ]
    elif typeNum == 2:
        perimeter = length*2 + width*6 + height*6
        textOnNet = [
            '',edgeLenWithoutA_list[0],'','',edgeLenWithoutA_list[1],
            '',edgeLenWithoutA_list[2],'','','',
            '','','','',''
        ]
    #draw
    transparency = 0.5
    drawPolygon_multiple(ax,cuboid_front,True,alpha=transparency,color='Blue')
    drawPolygon_multiple(ax,cuboid_back,dash=True)
    drawPolygonArc(ax,cuboid_frontF,show_text=['','',edgeLenWithoutA_list[0],edgeLenWithoutA_list[2]],alpha=transparency)
    drawPolygonArc(ax,cuboid_frontR,show_text=['','','',''],alpha=transparency)
    drawPolygonArc(ax,cuboid_frontT,show_text=['','','',edgeLenWithoutA_list[1]],alpha=transparency)

    drawPolygon(ax,cuboidNet_front,True,0.5,color='royalblue')
    drawPolygon_multiple(ax,cuboidNet_back,dash=True)
    drawPolygonArc(ax,cuboidNet_front,show_text=textOnNet)
    svg_stem = saveSvg()
    #draw_comment
    ax_comment = setChart(dim_2)
    cuboid_front,cuboid_back = create_p_cuboid(length*10,width*10,height*10,scale=40)
    cuboid_frontF,cuboid_frontR,cuboid_frontT = cuboid_front
    drawPolygon_multiple(ax_comment,cuboid_front,True,alpha=transparency,color='Blue')
    drawPolygon_multiple(ax_comment,cuboid_back,dash=True)
    drawPolygonArc(ax_comment,cuboid_frontF,show_text=['','',edgeLenWithA_list[0],edgeLenWithA_list[2]],alpha=transparency)
    drawPolygonArc(ax_comment,cuboid_frontR,show_text=['','','',''],alpha=transparency)
    drawPolygonArc(ax_comment,cuboid_frontT,show_text=['','','',edgeLenWithA_list[1]],alpha=transparency)

    #stem/answer/comment
    stem = "다음 직육면체의 모든 모서리의 길이의 합이\n "\
            "$$수식$$%srm cm$$/수식$$일 때 전개도의 둘레는 몇 $$수식$$rm cm$$/수식$$인가요?"%(
                sumOfEdges
                )
    answer = "(답): $$수식$$%srm cm$$/수식$$" %(perimeter)
    comment = "(해설) 직육면체의 모든 모서리의 길이의 합이 $$수식$$%srm cm$$/수식$$이므로\n"%(sumOfEdges)
    comment += "$$수식$$(%s + %s + A) \\times 4 = %s$$/수식$$입니다.\n"%(lenCuboid_list[0],lenCuboid_list[1],sumOfEdges)
    comment += "$$수식$$%s + %s + A = %s$$/수식$$, $$수식$$%s + A = %s$$/수식$$,\n"%(lenCuboid_list[0],lenCuboid_list[1],int(sumOfEdges/4),(lenCuboid_list[0]+lenCuboid_list[1]),int(sumOfEdges/4))
    comment += "$$수식$$A = %s - %s = %s$$/수식$$\n"%(int(sumOfEdges/4),(lenCuboid_list[0]+lenCuboid_list[1]),missing_len)
    comment += "따라서 전개도의 둘레는\n"
    if typeNum == 0:
        comment += "$$수식$$%s \\times 4 + %s \\times 2 + %s \\times 8 = %s$$/수식$$"%(length,width,height,perimeter)
    elif typeNum == 1:
        comment += "$$수식$$%s \\times 4 + %s \\times 2 + %s \\times 8 = %s$$/수식$$"%(length,width,height,perimeter)
    elif typeNum == 2:
        comment += "$$수식$$%s \\times 2 + %s \\times 6 + %s \\times 6 = %s$$/수식$$"%(length,width,height,perimeter)

    #plt.show()
    svg_comment = saveSvg()
    return stem,answer,comment,[svg_stem, svg_comment]


if __name__ == '__main__':
    stem, answer, comment,svg = cuboid525_Stem_008()
    print(stem + '\n')
    print(answer + '\n')
    print(comment + '\n')