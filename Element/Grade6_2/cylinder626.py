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
from matplotlib import pyplot
from matplotlib import cm

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
            plt.text(cp[0]-2*l, cp[1]+3, text[i], fontsize=10, zorder=3)
        elif position[i] == 'bottom':
            plt.text(cp[0]-2*l, cp[1]-9, text[i], fontsize=10, zorder=3)
        elif position[i] == 'left':
            plt.text(cp[0]-3-l*4.5, cp[1]-2, text[i], fontsize=10, zorder=3)
        elif position[i] == 'right':
            plt.text(cp[0]+l, cp[1]-2, text[i], fontsize=10, zorder=3)
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

                pp = mpatches.PathPatch(path, ec=color[i], fill=False, zorder=3, fc='none')
            elif angle <= 30:
                if diff and (i%2) == 1:
                    pp = mpatches.Arc(p2, angle=0, width=width*3/4, height=height*3/4, theta1=a1, theta2=a2, ec=color[i], zorder=3)
                    ax.add_patch(pp)
                pp = mpatches.Arc(p2, angle=0, width=width, height=height, theta1=a1, theta2=a2, ec=color[i], zorder=3)
            elif angle > 30:
                if diff and (i%2) == 1:
                    pp = mpatches.Arc(p2, angle=0, width=width*2, height=height*2, theta1=a1, theta2=a2, ec=color[i], zorder=3)
                    ax.add_patch(pp)
                pp = mpatches.Arc(p2, angle=0, width=width, height=height, theta1=a1, theta2=a2, ec=color[i], zorder=3, color=color[i])
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
            d *= 10
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
def drawAngle(ax, p_list=[]):
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
        pass
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
def drawPolygon(ax, verts, fill=False, alpha=1, dash=False,color='',ec='black'):
    def drawLine(ax,pts,dash=False,color='black',alpha=alpha):
        if dash: linestype = 'dashed'
        else: linestype = '-'
        line_1 = matplotlib.lines.Line2D((pts[0][0],pts[1][0]), (pts[0][1],pts[1][1]), linewidth=1, linestyle = linestype,color=color,alpha=alpha)
        ax.add_line(line_1)
    if len(verts) == 2:
        drawLine(ax,verts,dash,ec,alpha)
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
                pp = mpatches.PathPatch(path, fc=random.choice(colors), fill=True, lw=1, ls='--', zorder=3, alpha=alpha, ec=ec)
            else:
                pp = mpatches.PathPatch(path, fc=random.choice(colors), fill=True, lw=1, zorder=3, alpha=alpha, ec=ec)
        else:
            if dash:
                pp = mpatches.PathPatch(path, ec=ec, fill=False, lw=1, ls='--', zorder=3, alpha=alpha)
            else:
                pp = mpatches.PathPatch(path, ec=ec, fill=False, lw=1, zorder=3, alpha=alpha)
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
def drawCircle(ax,center, radius, fill=False, alpha=1, dash=False, position=None, color='',ec='black'):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)
    if color != '':
        colors = [color]
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

    if position != None and fill != True:
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
            pp = mpatches.Arc(center, width=radius*2, height=radius*2, angle=0, theta1=theta1, theta2=theta2, ec=ec, lw=1, ls='--', fill=False, zorder=3)
        else:
            pp = mpatches.Arc(center, width=radius*2, height=radius*2, angle=0, theta1=theta1, theta2=theta2, ec=ec, lw=1, fill=False, zorder=3)
    else:
        if fill:
            if dash:
                pp = mpatches.Circle(center,radius=radius, fc=random.choice(colors), ec=ec, lw=1, ls='--', fill=True, zorder=3, alpha=alpha)
            else:
                pp = mpatches.Circle(center,radius=radius, fc=random.choice(colors), ec=ec, lw=1, fill=True, zorder=3, alpha=alpha)
        else:
            if dash:
                pp = mpatches.Circle(center,radius=radius, ec='black', lw=1, ls='--', fill=False, zorder=3)
            else:
                pp = mpatches.Circle(center,radius=radius, ec='black', lw=1, fill=False, zorder=3)
    ax.add_patch(pp)
def drawSemiCircle(ax, center,radius,position,dash=False,ec='black'):
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
    if dash: ls = '--'
    else: ls = '-'
    pp = mpatches.Arc(center, width=radius*2, height=radius*2, angle=0, theta1=theta1, theta2=theta2, ec=ec, lw=1, ls=ls, fill=False, zorder=3)
    ax.add_patch(pp)

# 타원
def drawEllipse(ax,center, width, height, fill=False, alpha=1,set_color='',dash=False,position=None, ec='black'):
    radius = max(width, height)/2
    if set_color != '':
        color = set_color
    else:
        color_list = list(mcolors.CSS4_COLORS.keys())
        color = random.choice(color_list)

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
            pp = mpatches.Arc(center, width=width, height=height, angle=0, theta1=theta1, theta2=theta2, ec=ec, lw=1, ls='--', zorder=3)
        else:
            pp = mpatches.Arc(center, width=width, height=height, angle=0, theta1=theta1, theta2=theta2, ec=ec, lw=1, zorder=3)
    else:
        if fill:
            if dash:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, fc=color, ec=ec, lw=1, ls='--', fill=True, zorder=3, alpha=alpha)
            else:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, fc=color, ec=ec, lw=1, fill=True, zorder=3, alpha=alpha)
        else:
            if dash:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, ec=ec, lw=1, ls='--', fill=False, zorder=3)
            else:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, ec=ec, lw=1, fill=False, zorder=3)

    ax.add_patch(pp)

# 입체도형
def drawCylinder(ax,radius,height,p_center_bottom=(0,0),fill=False,set_color='',show_list=[],scale=11,x_move=0,y_move=0):
    def get_y_ellipse(x,p_center,length,height,position='top'):
        x = round(x,7)
        a = height
        b = round(length/2,7)
        h,k = p_center
        if position == 'top': sign = 1
        elif position == 'bottom': sign = -1
        y = k + sign*a*math.sqrt(1-((x-h)**2)/(b**2))
        return y
    def get_vertCodes_ellipse(p_center,length,height,position='top'):
        height = height/2
        temp_p = (p_center[0]-length/2,p_center[1])
        vert = [temp_p]
        codes = [Path.MOVETO]
        size = 60
        for i in range(size):
            temp_x = temp_p[0]+length/size
            temp_p = (temp_x,get_y_ellipse(temp_x,p_center,length,height,position))
            vert.append(temp_p)
            codes.append(Path.CURVE3)
        vert.append((p_center[0]+length/2,p_center[1]))
        codes.append(Path.CURVE3)
        return vert,codes
    def move_p(p,x_move=0,y_move=0):
            new_p = (p[0]+x_move,p[1]+y_move)
            return new_p
    len_radius,len_height = radius,height
    radius *= scale
    height *= scale
    p_center_bottom = move_p(p_center_bottom,x_move,y_move)
    p_center_top = (p_center_bottom[0],p_center_bottom[1]+height)
    p_top_r = (p_center_top[0]+radius,p_center_top[1])
    p_top_l = (p_center_top[0]-radius,p_center_top[1])
    p_bottom_r = (p_center_bottom[0]+radius,p_center_bottom[1])
    p_bottom_l = (p_center_bottom[0]-radius,p_center_bottom[1])
    l_left = [p_bottom_l,p_top_l]
    l_right = [p_bottom_r,p_top_r]
    l_radius = [p_center_top,p_top_r]
    l_diameter = [p_top_l,p_top_r]
    if fill:
        color_list = [('green','springgreen'),('purple','mediumpurple'),('blue','lightsteelblue'),('orange','moccasin')]
        if set_color != '':
            if set_color == 'green':
                color = color_list[0]
            elif set_color == 'purple':
                color = color_list[1]
            elif set_color == 'blue':
                color = color_list[2]
            elif set_color == 'orange':
                color = color_list[3]
            else: raise Exception("No Matching Color")
        elif set_color == '':
            color = random.choice(color_list)
        color_gradient(ax,p_top_l[0],p_top_r[0],p_bottom_r[1]-radius/2,p_top_r[1],color[0])
        vert_ellipse,codes_ellipse = get_vertCodes_ellipse(p_center_bottom,radius*2,radius/2,'bottom')
        vert = [
            (p_bottom_r[0]+5,p_bottom_r[1]),
            (p_bottom_r[0],p_bottom_r[1]-radius/2-5),
            (p_bottom_l[0],p_bottom_l[1]-radius/2-5),
            (p_bottom_l[0]-5,p_bottom_l[1]),
            p_bottom_l
        ]
        codes = [
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.CLOSEPOLY
        ]
        path = Path(vert_ellipse+vert,codes_ellipse+codes)
        pp = mpatches.PathPatch(path, fc='white', fill=True, lw=0, zorder=3)
        ax.add_patch(pp)
    drawEllipse(ax,p_center_top,radius*2,radius/2,fill=fill,set_color=color[1])
    drawEllipse(ax,p_center_bottom,radius*2,radius/2,position='bottom')
    drawEllipse(ax,p_center_bottom,radius*2,radius/2,dash=True,position='top')
    drawLine_multiple(ax,[l_left,l_right])
    if show_list != []:
        for i in show_list:
            if i in ['radius','r']:
                drawLine(ax,l_radius)
                drawDot(ax,[p_center_top],True)
                drawArc(ax,l_radius,'top','$%s \mathrm{cm}$'%(len_radius))
            elif i in ['diameter','d']:
                drawLine(ax,l_diameter)
                drawDot(ax,[p_center_top],True)
                drawArc(ax,l_diameter,'top','$%s \mathrm{cm}$'%(len_radius*2))
            elif i in ['height','h']:
                drawArc(ax,l_right,'right','$%s \mathrm{cm}$'%(len_height))
            else: raise Exception("Invalid value")
def drawCylinderNet(ax,radius,height,pi=3.14,fill=False,set_color='',show_list=[],scale=5,x_move=0,y_move=0):
    def move_p(p,x_move=0,y_move=0):
        new_p = (p[0]+x_move,p[1]+y_move)
        return new_p
    len_radius,len_height = radius,height
    len_perimeterOfCircle = 2*radius*pi
    radius *= scale
    height *= scale
    perimeterOfCircle = radius*2*3.14
    p_origin = move_p((0,0),x_move,y_move)
    p_top_l = move_p(p_origin,-perimeterOfCircle/2,height/2)
    p_top_r = move_p(p_origin,perimeterOfCircle/2,height/2)
    p_bottom_l = move_p(p_origin,-perimeterOfCircle/2,-height/2)
    p_bottom_r = move_p(p_origin,perimeterOfCircle/2,-height/2)
    p_center_top = (p_top_l[0]+radius*1.3,p_top_l[1]+radius)
    p_center_bottom = (p_bottom_r[0]-radius*1.3,p_bottom_r[1]-radius)
    l_right = [p_top_r,p_bottom_r]
    l_top = [p_top_l,p_top_r]
    l_bottom = [p_bottom_l,p_bottom_r]
    if fill:
        color_list = ['springgreen','mediumpurple','lightsteelblue','moccasin']
        if set_color != '':
            if set_color == 'green':
                color = color_list[0]
            elif set_color == 'purple':
                color = color_list[1]
            elif set_color == 'blue':
                color = color_list[2]
            elif set_color == 'orange':
                color = color_list[3]
            else: raise Exception("No Matching Color")
        elif set_color == '':
            color = random.choice(color_list)
        
    drawCircle(ax,p_center_top,radius,fill,color=color)
    drawPolygon(ax,[p_top_l,p_top_r,p_bottom_r,p_bottom_l],fill,color=color)
    drawCircle(ax,p_center_bottom,radius,fill,color=color)
    if show_list != []:
        for commend in show_list:
            if commend in ['radius','r']:
                pass
            elif commend in ['diameter','d']:
                pass
            elif commend in ['height','h']:
                drawArc(ax,l_right,'right','$%s \mathrm{cm}$'%(len_height))
            elif commend in ['perimeter']:
                drawArc(ax,l_bottom,'top_r','$%s \mathrm{cm}$'%(len_perimeterOfCircle))
            else: raise Exception('Invalid Commend')
def drawCone(ax,radius,height,p_center_bottom=(0,0),fill=False,set_color='',show_list=[],scale=11,x_move=0,y_move=0):
    def get_vertCodes_ellipse(p_center,length,height,position='top'):
        def get_y_ellipse(x,p_center,length,height,position='top'):
            x = round(x,7)
            a = height
            b = round(length/2,7)
            h,k = p_center
            if position == 'top': sign = 1
            elif position == 'bottom': sign = -1
            y = k + sign*a*math.sqrt(1-((x-h)**2)/(b**2))
            return y
        height = height/2
        temp_p = (p_center[0]-length/2,p_center[1])
        vert = [temp_p]
        codes = [Path.MOVETO]
        size = 100
        for i in range(size):
            temp_x = temp_p[0]+length/size
            temp_p = (temp_x,get_y_ellipse(temp_x,p_center,length,height,position))
            vert.append(temp_p)
            codes.append(Path.CURVE3)
        vert.append((p_center[0]+length/2,p_center[1]))
        codes.append(Path.CURVE3)
        return vert,codes
    def move_p(p,x_move=0,y_move=0):
            new_p = (p[0]+x_move,p[1]+y_move)
            return new_p
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
    def calculate_distance(p1=tuple, p2=tuple):
        import math
        d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

        return d
    def find_p_middle(p1=tuple,p2=tuple):
        return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
    len_radius,len_height = radius,height
    len_generatix = round(math.sqrt(len_radius**2+len_height**2))
    radius *= scale
    height *= scale
    
    p_center_bottom = move_p(p_center_bottom,x_move,y_move)
    p_top = (p_center_bottom[0],p_center_bottom[1]+height)
    p_bottom_r = (p_center_bottom[0]+radius,p_center_bottom[1])
    p_bottom_l = (p_center_bottom[0]-radius,p_center_bottom[1])
    polygon = [p_bottom_l,p_top,p_bottom_r]
    [p_bottom_l,p_top,p_bottom_r] = resize_polygon(polygon)
    p_center_bottom = find_p_middle(p_bottom_l,p_bottom_r)
    height = calculate_distance(p_center_bottom,p_top)
    radius = calculate_distance(p_bottom_l,p_center_bottom)
    
    l_left = [p_bottom_l,p_top]
    l_right = [p_bottom_r,p_top]
    l_radius = [p_center_bottom,p_bottom_r]
    l_height = [p_center_bottom,p_top]
    l_diameter = [p_bottom_l,p_bottom_r]
    if fill:
        color_list = [('green','springgreen'),('purple','mediumpurple'),('blue','lightsteelblue'),('orange','moccasin')]
        if set_color != '':
            if set_color == 'green':
                color = color_list[0]
            elif set_color == 'purple':
                color = color_list[1]
            elif set_color == 'blue':
                color = color_list[2]
            elif set_color == 'orange':
                color = color_list[3]
            else: raise Exception("No Matching Color")
        elif set_color == '':
            color = random.choice(color_list)
        color_gradient(ax,p_bottom_l[0],p_bottom_r[0],p_bottom_r[1]-radius/2,p_top[1],color[0])
        vert_ellipse,codes_ellipse = get_vertCodes_ellipse(p_center_bottom,radius*2,radius/2,'bottom')
        vert = [
            (p_bottom_r[0]+5,p_bottom_r[1]),
            (p_bottom_r[0],p_bottom_r[1]-radius/2-5),
            (p_bottom_l[0],p_bottom_l[1]-radius/2-5),
            (p_bottom_l[0]-5,p_bottom_l[1]),
            p_bottom_l
        ]
        codes = [
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.CLOSEPOLY
        ]
        path = Path(vert_ellipse+vert,codes_ellipse+codes)
        pp = mpatches.PathPatch(path, fc='white', fill=True, lw=0, zorder=3)
        ax.add_patch(pp)
    drawEllipse(ax,p_center_bottom,radius*2,radius/2,position='bottom')
    drawEllipse(ax,p_center_bottom,radius*2,radius/2,dash=True,position='top')
    vert = [
        p_bottom_l,
        p_top,
        p_bottom_r,
        (p_bottom_r[0]+5,p_bottom_r[1]),
        (p_bottom_r[0]+5,p_top[1]+5),
        (p_bottom_l[0]-5,p_top[1]+5),
        (p_bottom_l[0]-5,p_bottom_l[1]),
        p_bottom_l
    ]
    codes = [
        Path.MOVETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY
    ]
    path = Path(vert,codes)
    pp = mpatches.PathPatch(path, fc='white', fill=True, lw=0, zorder=3)
    ax.add_patch(pp)
    drawLine_multiple(ax,[l_left,l_right])
    if show_list != []:
        for commend in show_list:
            if commend in ['radius','r']:
                drawLine(ax,l_radius)
                drawArc(ax,l_radius,'bottom','$%s \mathrm{cm}$'%(len_radius))
            elif commend in ['diameter','d']:
                drawLine(ax,l_diameter)
                drawArc(ax,l_diameter,'bottom','$%s \mathrm{cm}$'%(len_radius*2))
            elif commend in ['height','h']:
                drawAngle(ax,[p_bottom_r,p_center_bottom,p_top])
                drawLine(ax,l_height,True)
                drawArc(ax,l_height,'left','$%s \mathrm{cm}$'%(len_height))
            elif commend in ['generatix']:
                drawArc(ax,l_right,'right','$%s \mathrm{cm}$'%(len_generatix))
            elif commend in ['setPoint','p']:
                setPoint(ax,[p_top,p_bottom_l,p_bottom_r],['A','B','C'],['top','left','right'])
            else: raise Exception("Invalid Commend")
def drawSphere(ax,radius,p_center=(0,0),set_color='',show_list=[],scale=80,x_move=0,y_move=0):
    def color_gradient_sphere(ax,x_min,x_max,y_min,y_max,set_color=''):
        from matplotlib import pyplot
        cmap_list = [pyplot.cm.Greens,pyplot.cm.Purples,pyplot.cm.Blues,pyplot.cm.Oranges]
        if set_color != '':
            if set_color == 'green':
                cmap = pyplot.cm.Greens
            elif set_color == 'purple':
                cmap = pyplot.cm.Purples
            elif set_color == 'blue':
                cmap = pyplot.cm.Blues
            elif set_color == 'orange':
                cmap = pyplot.cm.Oranges
            else: raise Exception('No matching cmap')
        elif set_color == '':
            cmap = random.choice(cmap_list)
        x_half = (x_min+x_max)/2
        y_half = (y_min+y_max)/2
        X1 = [[64,194], [64,174]]
        #section1
        ax.imshow(
        X1,
        interpolation='bicubic', 
        cmap=cmap,
        extent=(x_half, x_max, y_half, y_max),
        vmin = 0, vmax = 255
        )
        #section2
        ax.imshow(
        X1,
        interpolation='bicubic', 
        cmap=cmap,
        extent=(x_half, x_min, y_half, y_max),
        vmin = 0, vmax = 255
        )
        #section3
        ax.imshow(
        X1,
        interpolation='bicubic', 
        cmap=cmap,
        extent=(x_half, x_min, y_half, y_min),
        vmin = 0, vmax = 255
        )
        #section4
        ax.imshow(
        X1,
        interpolation='bicubic', 
        cmap=cmap,
        extent=(x_half, x_max, y_half, y_min),
        vmin = 0, vmax = 255
        )
    def get_vertCodes_circle(p_center,radius,position='top'):
        def get_y_circle(x,p_center,radius,position='top'):
            r = round(radius,1)
            x = round(x,1)
            h,k = p_center
            if position == 'top': sign = 1
            elif position == 'bottom': sign = -1
            y = k + sign*math.sqrt(round(r**2)-round((x-h)**2))
            return y
        temp_p = (p_center[0]-radius,p_center[1])
        diameter = radius*2
        vert = [temp_p]
        codes = [Path.MOVETO]
        size = 100
        for i in range(size):
            temp_x = temp_p[0]+diameter/size
            temp_p = (temp_x,get_y_circle(temp_x,p_center,radius,position))
            vert.append(temp_p)
            codes.append(Path.CURVE3)
        vert.append((p_center[0]+radius,p_center[1]))
        codes.append(Path.CURVE3)
        return vert,codes
    def move_p_multiple(p_list,x_move=0,y_move=0):
        for i in range(len(p_list)):
            p = p_list[i]
            new_p = (p[0]+x_move,p[1]+y_move)
            p_list[i] = new_p
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
    def calculate_distance(p1=tuple, p2=tuple):
        import math
        d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

        return d
    def find_p_middle(p1=tuple,p2=tuple):
        return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
    color_list = [('green','springgreen'),('purple','mediumpurple'),('blue','lightsteelblue'),('orange','moccasin')]
    if set_color != '':
        if set_color == 'green':
            color = color_list[0]
        elif set_color == 'purple':
            color = color_list[1]
        elif set_color == 'blue':
            color = color_list[2]
        elif set_color == 'orange':
            color = color_list[3]
        else: raise Exception("No Matching Color")
    elif set_color == '':
        color = random.choice(color_list)
    len_radius = radius
    radius *= 11
    p_top = (p_center[0],p_center[1]+radius)
    p_bottom = (p_center[0],p_center[1]-radius)
    p_left = (p_center[0]-radius,p_center[1])
    p_right = (p_center[0]+radius,p_center[1])
    polygon = [p_left,p_top,p_right,p_bottom]
    polygon = resize_polygon(polygon,scale)
    [p_left,p_top,p_right,p_bottom] = move_p_multiple(polygon,x_move,y_move)
    p_center = find_p_middle(p_left,p_right)
    radius = calculate_distance(p_left,p_center)
    p_top_l = (p_left[0],p_top[1])
    p_top_r = (p_right[0],p_top[1])
    p_bottom_l = (p_left[0],p_bottom[1])
    p_bottom_r = (p_right[0],p_bottom[1])
    l_left = [p_left,p_top]
    l_right = [p_right,p_top]
    l_radius = [p_center,p_top]
    l_diameter = [p_left,p_right]
    fill = True
    if fill:
        color_gradient_sphere(ax,p_bottom_l[0],p_bottom_r[0],p_bottom_l[1],p_top_l[1],color[0])
        vert_ellipse,codes_ellipse = get_vertCodes_circle(p_center,radius,'top')
        height_edge = 110
        side_edge = 5
        vert = [
            (p_right[0]+side_edge,p_right[1]),
            (p_right[0]+side_edge,p_top[0]+height_edge),
            (p_left[0]-side_edge,p_top[0]+height_edge),
            (p_left[0]-side_edge,p_left[1]),
            p_left
        ]
        codes = [
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.CLOSEPOLY
        ]
        path = Path(vert_ellipse+vert,codes_ellipse+codes)
        pp = mpatches.PathPatch(path, fc='white', fill=True, lw=0, zorder=3)
        ax.add_patch(pp)
        vert_ellipse,codes_ellipse = get_vertCodes_circle(p_center,radius,'bottom')
        vert = [
            (p_right[0]+side_edge,p_right[1]),
            (p_right[0]+side_edge,p_bottom[0]-height_edge),
            (p_left[0]-side_edge,p_bottom[0]-height_edge),
            (p_left[0]-side_edge,p_left[1]),
            p_left
        ]
        codes = [
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.CLOSEPOLY
        ]
        path = Path(vert_ellipse+vert,codes_ellipse+codes)
        pp = mpatches.PathPatch(path, fc='white', fill=True, lw=0, zorder=3)
        ax.add_patch(pp)
    drawCircle(ax,p_center,radius)
    drawEllipse(ax,p_center,radius*2,radius/2,position='bottom')
    drawEllipse(ax,p_center,radius*2,radius/2,dash=True,position='top')
    if show_list != []:
        for commend in show_list:
            if commend in ['radius','r']:
                drawLine(ax,l_radius)
                drawArc(ax,l_radius,'right','$%s \mathrm{cm}$'%(len_radius))
            elif commend in ['diameter','d']:
                drawLine(ax,l_diameter)
                drawArc(ax,l_diameter,'bottom','$%s \mathrm{cm}$'%(len_radius*2))
            elif commend in ['center']:
                drawDot(ax,[p_center],True)
            else: raise Exception("Invalid Commend")
    return p_center,radius


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
def color_gradient(ax,x_min,x_max,y_min,y_max,set_color=''):
    cmap_list = [pyplot.cm.Greens,pyplot.cm.Purples,pyplot.cm.Blues,pyplot.cm.Oranges]
    if set_color != '':
        if set_color == 'green':
            cmap = pyplot.cm.Greens
        elif set_color == 'purple':
            cmap = pyplot.cm.Purples
        elif set_color == 'blue':
            cmap = pyplot.cm.Blues
        elif set_color == 'orange':
            cmap = pyplot.cm.Oranges
        else: raise Exception('No matching cmap')
    elif set_color == '':
        cmap = random.choice(cmap_list)
    x_half = (x_min+x_max)/3
    X1 = [[194,64], [174,64]]
    X2 = [[64,194], [64,174]]
    ax.imshow(
    X1,
    interpolation='bicubic', 
    cmap=cmap,
    extent=(x_min, x_half, y_min, y_max),
    vmin = 0, vmax = 255
    )
    ax.imshow(
    X2,
    interpolation='bicubic', 
    cmap=cmap,
    extent=(x_half, x_max, y_min, y_max),
    vmin = 0, vmax = 255
    )

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
def drawArc(ax, p_list, position, text='', boxed=False,color='black',linestyle='--'):
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
        l -= 13
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

    pp = mpatches.PathPatch(path, fc="none", transform=ax.transData, linestyle=linestyle, zorder=3, color=color)
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
    elif text != '':
        if position == 'top':
            plt.text(cp[0]-2*l, cp[1]+1, text, fontsize=10, zorder=3)
        elif position == 'bottom':
            plt.text(cp[0]-2*l, cp[1]-3, text, fontsize=10, zorder=3)
        elif position == 'left':
            plt.text(cp[0]-2-l*6.5, cp[1]-2, text, fontsize=10, zorder=3)
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


def find_p_in_circle(r,p_list=[],O=(0,0)):
    def move_p_single(p,x_move=0,y_move=0):
            new_p = (p[0]+x_move,p[1]+y_move)
            return new_p
    def too_close(p,p_list):
        def calculate_distance(p1=tuple, p2=tuple):
            import math
            d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

            return d
        x = p[0]
        y = p[1]
        for temp_p in p_list:
            if calculate_distance((x,y),temp_p) < 20:
                return True
        return False
    import math, random
    sign = random.choice([1,-1])
    x = random.uniform(r*-1,r)
    y = math.sqrt(r*r-x*x) * sign
    temp_p = (x,y)
    while too_close(temp_p,p_list):
        x = random.uniform(r*-1,r)
        y = math.sqrt(r*r-x*x) * sign
        temp_p = (x,y)
    return move_p_single((x,y),O[0],O[1])
def calculate_distance(p1=tuple, p2=tuple):
    import math
    d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    return d

class Cylinder():
    def __init__(self,pi):
        self.pi = pi
        while True:
            self.radius = random.randint(3,7)
            self.height = random.randint(6,10)
            if self.radius*2 != self.height:
                break
        self.diameter = self.radius*2
        self.areaOfCircle = round(pi*self.radius**2,2)
        self.perimeterOfCircle = round(2*pi*self.radius,2)
        self.volume = round(self.areaOfCircle*self.height,2)
        self.surfaceArea = round(self.areaOfCircle*2 + self.perimeterOfCircle*self.height,3)
class Cone():
    def __init__(self,pi):
        self.pi = pi
        while True:
            self.radius = random.randint(3,10)
            self.height = random.randint(3,15)
            self.generatix = math.sqrt(self.height**2 + self.radius**2)
            if self.radius*2 != self.height and self.generatix % 1 == 0 and self.radius < self.height:
                break
        self.generatix = round(self.generatix)
        self.diameter = self.radius*2
class Sphere():
    def __init__(self,pi=3):
        self.pi = pi
        self.radius = random.randint(5,20)
        self.diameter = self.radius*2
        self.perimeter = 2*self.radius*pi
        self.area = self.radius**2*pi
        

#6-2-6-10
def cylinder626_Stem_001():
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
    pi = 3
    cylinder = Cylinder(pi)
    #generate shapes
    p_center_bottom = (0,0)
    show_list = ['d','h']
    #draw shapes
    drawCylinder(ax,cylinder.radius,cylinder.height,p_center_bottom,True,show_list=show_list)
    #stem/answer/comment
    stem = "다음 도형은 어떤 평면도형의 한 변을 기준으로\n"\
            "한 바퀴돌려 만든 입체도형입니다. 돌리기 전의\n"\
            "평면도형의 넓이는 몇 $$수식$$rm cm^{2}$$/수식$$인지\n"\
            "구해 보세요."
    answer = '(답): $$수식$$%srm cm^{2}$$/수식$$'%(cylinder.radius*cylinder.height)
    comment = "(해설) 돌리기 전의 평면도형은 가로가 $$수식$$%s$$/수식$$ $$수식$$\\\\div$$/수식$$ $$수식$$2 = %s(rm cm)$$/수식$$\n"\
                "이고 세로가 $$수식$$%srm cm$$/수식$$인 직사각형입니다.\n"\
                "따라서 돌리기 전의 평면도형의 넓이는 $$수식$$%s \\times %s = %s(rm cm^{2})$$/수식$$\n"\
                "입니다."%(
                    cylinder.diameter,cylinder.radius,
                    cylinder.height,
                    cylinder.radius,cylinder.height,(cylinder.radius*cylinder.height)
                )
    #plt.show()
    svg = saveSvg()
    return stem, answer, comment,svg
    
#6-2-6-11
def cylinder626_Stem_002():
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
    pi = 3
    cylinder = Cylinder(pi)
    #generate shapes
    p_center_bottom = (0,0)
    show_list = ['r','h']
    #draw shapes
    drawCylinder(ax,cylinder.radius,cylinder.height,p_center_bottom,True,show_list=show_list)
    #stem/answer/comment
    stem = "원기둥을 앞에서 본 모양의 넓이는 몇 $$수식$$rm cm^{2}$$/수식$$인지\n"\
            "구해보세요."
    answer = "(답): $$수식$$%srm cm^{2}$$/수식$$"%(cylinder.diameter*cylinder.height)
    comment = "(해설) 원기둥을 앞에서 본 모양은 가로가\n"\
                "$$수식$$%s \\times 2 = %s(rm cm)$$/수식$$이고 세로가 $$수식$$%srm cm$$/수식$$인 직사각형\n"\
                "입니다.\n"\
                "따라서 앞에서 본 모양의 넓이는 $$수식$$%s \\times %s = %s(rm cm^{2})$$/수식$$\n"\
                "입니다."%(
                    cylinder.radius, cylinder.diameter, cylinder.height,
                    cylinder.diameter, cylinder.height, (cylinder.diameter*cylinder.height)
                )
    #plt.show()
    svg = saveSvg()
    return stem,answer,comment,svg

#6-2-6-12
def cylinder626_Stem_003():
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
    pi = 3
    cylinder = Cylinder(pi)
    cylinderNet_sideLength = cylinder.perimeterOfCircle
    cylinderNet_sideWidth = cylinder.height
    #generate shapes
    p_center_bottom = (0,0)
    show_list = ['r','h']
    #draw shapes
    drawCylinder(ax,cylinder.radius,cylinder.height,p_center_bottom,True,show_list=show_list)
    #stem/answer/comment
    stem = "다음 원기둥을 펼쳐 전개도를 만들었을 때\n"\
            "옆면의 가로와 세로의 길이를 차례대로\n"\
            "구해 보세요.(원주율: $$수식$$3$$/수식$$)"
    answer = "(답): $$수식$$%srm cm$$/수식$$, $$수식$$%srm cm$$/수식$$"%(cylinderNet_sideLength,cylinderNet_sideWidth)
    comment = "(해설) (옆면의 가로) $$수식$$=$$/수식$$ (밑면의 둘레)\n"\
                " $$수식$$= %s \\times 2 \\times 3 = %s(rm cm)$$/수식$$\n"\
                "(옆면의 세로) $$수식$$=$$/수식$$ (원기둥의 높이) $$수식$$=  %s(rm cm)$$/수식$$"%(
                    cylinder.radius,cylinderNet_sideLength,
                    cylinderNet_sideWidth
                )
    #plt.show()
    svg = saveSvg()
    return stem,answer,comment,svg

#6-2-6-16
def cylinder626_Stem_004():
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
    pi = 3
    cylinder = Cylinder(pi)
    #generate shape
    show_list = ['perimeter','h']
    #draw shapes
    drawCylinderNet(ax,cylinder.radius,cylinder.height,pi,True,'green',show_list)
    #stem/answer/comment
    stem = "원기둥의 전개도에서 옆면의 가로가\n"\
            "$$수식$$%srm cm$$/수식$$, 세로가 $$수식$$%srm cm$$/수식$$일 때 원기둥의 밑면의\n"\
            "반지름은 몇 $$수식$$rm cm$$/수식$$인가요? (원주율: $$수식$$3$$/수식$$)"%(
                cylinder.perimeterOfCircle,cylinder.height
            )
    answer = '(답): $$수식$$%srm cm$$/수식$$'%(cylinder.radius)
    comment = "(해설) (밑면의 반지름) $$수식$$= %s$$/수식$$ $$수식$$\\\\div$$/수식$$ $$수식$$3$$/수식$$ $$수식$$\\\\div$$/수식$$ $$수식$$2 = %s(rm cm)$$/수식$$"%(
        cylinder.perimeterOfCircle,cylinder.radius
    )
    #plt.show()
    svg = saveSvg()
    return stem,answer,comment,svg

#6-2-6-17
def cylinder626_Stem_005():
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
    pi = 3.1
    cylinder = Cylinder(pi)
    perimeterOfSurfaceArea = (cylinder.perimeterOfCircle+cylinder.height+cylinder.perimeterOfCircle)*2
    #generate shape
    show_list = ['r','h']
    color = 'purple'
    #draw shapes
    if cylinder.radius >= 7:
        drawCylinderNet(ax,cylinder.radius,cylinder.height,pi,True,color,scale=2,x_move=-40)
        drawCylinder(ax,cylinder.radius,cylinder.height,fill=True,set_color=color,show_list=show_list,scale=5,x_move=50,y_move=-20)
    elif cylinder.radius >= 5:
        drawCylinderNet(ax,cylinder.radius,cylinder.height,pi,True,color,scale=3,x_move=-50)
        drawCylinder(ax,cylinder.radius,cylinder.height,fill=True,set_color=color,show_list=show_list,scale=6,x_move=50,y_move=-20)
    elif cylinder.radius == 4:
        drawCylinderNet(ax,cylinder.radius,cylinder.height,pi,True,color,scale=4,x_move=-45)
        drawCylinder(ax,cylinder.radius,cylinder.height,fill=True,set_color=color,show_list=show_list,scale=7,x_move=45,y_move=-20)
    elif cylinder.radius == 3:
        drawCylinderNet(ax,cylinder.radius,cylinder.height,pi,True,color,scale=5,x_move=-40)
        drawCylinder(ax,cylinder.radius,cylinder.height,fill=True,set_color=color,show_list=show_list,scale=6,x_move=40,y_move=-20)
    #stem/answer/comment
    stem = "원기둥과 원기둥의 전개도를 보고 전개도의\n"\
            "둘레는 몇 $$수식$$rm cm$$/수식$$인지 구해보세요. (원주율: $$수식$$3.1$$/수식$$)"
    answer = "(답): $$수식$$%srm cm$$/수식$$"%(perimeterOfSurfaceArea)
    comment = "(해설) (밑면의 둘레) $$수식$$= %s \\times 2 \\times 3.1 = %s(rm cm)$$/수식$$\n"\
                " (두 밑면의 둘레의 합) $$수식$$= %s \\times 2 = %s(rm cm)$$/수식$$\n"\
                " (옆면의 가로) $$수식$$=$$/수식$$ (밑면의 둘레) $$수식$$= %srm cm$$/수식$$\n"\
                " (옆면의 세로) $$수식$$=$$/수식$$ (원기둥의 높이) $$수식$$= %srm cm$$/수식$$\n"\
                " (옆면의 둘레) $$수식$$= (%s + %s) \\times 2 = %s(rm cm)$$/수식$$\n"\
                " (원기둥의 전개도의 둘레)\n"\
                " $$수식$$=$$/수식$$ (두 밑면의 둘레의 합) $$수식$$+$$/수식$$ (옆면의 둘레)\n"\
                " $$수식$$= %s + %s = %s(rm cm)$$/수식$$"%(
                    cylinder.radius, cylinder.perimeterOfCircle,
                    cylinder.perimeterOfCircle, (cylinder.perimeterOfCircle*2),
                    cylinder.perimeterOfCircle,
                    cylinder.height,
                    cylinder.perimeterOfCircle, cylinder.height, (cylinder.perimeterOfCircle+cylinder.height)*2,
                    (cylinder.perimeterOfCircle*2), (cylinder.perimeterOfCircle+cylinder.height)*2,
                    perimeterOfSurfaceArea
                )
    #plt.show()
    svg = saveSvg()
    return stem,answer,comment,svg

#6-2-6-21
def cylinder626_Stem_006():
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
    pi = 3
    cone = Cone(pi)
    #generate shapes
    show_list = ['r','h','generatix']
    #draw shapes
    drawCone(ax,cone.radius,cone.height,fill=True,show_list=show_list)
    #stem/answer/comment
    stem = "원뿔의 높이와 무선의 길이는 각각 몇\n"\
            "$$수식$$rm cm$$/수식$$인가요?"
    answer = '(답): $$수식$$%srm cm$$/수식$$, $$수식$$ %srm cm$$/수식$$'%(cone.height,cone.generatix)
    comment = "(해설)높이는 $$수식$$%srm cm$$/수식$$인고, 모선의 길이는 $$수식$$%srm cm$$/수식$$\n"\
                "입니다."%(cone.height,cone.generatix)
    #plt.show()
    svg = saveSvg()
    return stem,answer,comment,svg

#6-2-6-29
def cylinder626_Stem_007():
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
    pi = 3
    cone = Cone(pi)
    perimeterOfTriangle = cone.generatix*2 + cone.diameter
    #generate shapes
    show_list = ['r','h','generatix','p']
    #draw shapes
    drawCone(ax,cone.radius,cone.height,fill=True,show_list=show_list)
    #stem/answer/comment
    stem = "원뿔에서 삼각형$$수식$$ABC$$/수식$$의 둘레는 몇 $$수식$$rm cm$$/수식$$\n"\
            "인가요?"
    answer = "(답): $$수식$$%srm cm$$/수식$$"%(perimeterOfTriangle)
    comment = "(해설) 원뿔에서 모선의 길이는 모두 같으므로\n"\
                "($$수식$$선분AB$$/수식$$) $$수식$$=$$/수식$$ ($$수식$$선분AC$$/수식$$) $$수식$$= %srm cm$$/수식$$\n"\
                "($$수식$$선분BC$$/수식$$) $$수식$$= %s \\times 2 = %s(rm cm)$$/수식$$\n"\
                "($$수식$$삼각형ABC$$/수식$$의 둘레)\n"\
                " $$수식$$= %s + %s + %s = %s(rm cm)$$/수식$$"%(
                    cone.generatix,
                    cone.radius, cone.diameter,
                    cone.generatix, cone.diameter, cone.generatix, perimeterOfTriangle
                )
    #plt.show()
    svg = saveSvg()
    return stem,answer,comment,svg

#6-2-6-33
def cylinder626_Stem_008():
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
    pi = 3
    while True:
        sphere1 = Sphere(pi)
        sphere2 = Sphere(pi)
        if sphere1.radius != sphere2.radius and abs(sphere1.radius-sphere2.radius) < 5:
            break
    #generate shapes
    show_list1 = ['d','center']
    scale1 = 40
    scale2 = scale1 * (sphere1.radius/sphere2.radius)
    show_list2 = ['r','center']
    #draw shapes
    drawSphere(ax,sphere1.radius,set_color='blue',show_list=show_list1,scale=scale1,x_move=-50)
    drawSphere(ax,sphere2.radius,set_color='blue',show_list=show_list2,scale=scale2,x_move=50)
    #stem/answer/comment
    stem = '두 구의 반지름의 합은 몇 $$수식$$rm cm$$/수식$$인가요?'
    answer = '(답): $$수식$$%srm cm$$/수식$$'%(sphere1.radius+sphere2.radius)
    comment = "(해설) (왼쪽 구의 반지름) $$수식$$= %s$$/수식$$ $$수식$$\\\\div$$/수식$$ $$수식$$2 = %s(rm cm)$$/수식$$\n"\
                " (오른쪽 구의 반지름) $$수식$$= %srm cm$$/수식$$\n"\
                "$$수식$$\\rightarrow$$/수식$$ (두 구의 반지름의 합) $$수식$$= %s + %s = %s(rm cm)$$/수식$$"%(
                    sphere1.diameter, sphere1.radius,
                    sphere2.radius,
                    sphere1.radius, sphere2.radius, (sphere1.radius+sphere2.radius)
                )
    #plt.show()
    svg = saveSvg()
    return stem,answer,comment,svg

#6-2-6-34
def cylinder626_Stem_009():
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
    pi = 3
    sphere = Sphere(pi)
    show_list = ['r','center']
    p_center,radius = drawSphere(ax,sphere.radius,show_list=show_list)
    ratio = radius/sphere.radius
    stem_radius = sphere.radius
    #line-radius
    p_right = (radius,0)
    p_left = (-radius,0)
    #line above x-asix
    p_top1 = find_p_in_circle(radius)
    p_top2 = find_p_in_circle(radius,[p_top1])
    len_top = int(calculate_distance(p_top1,p_top2)/ratio)
    while True:
        p_top1 = find_p_in_circle(radius)
        p_top2 = find_p_in_circle(radius,[p_top1])
        len_top = int(calculate_distance(p_top1,p_top2)/ratio)
        isAboveX = p_top1[1] > 0 and p_top2[1] > 0
        isNotSameAsRadius = len_top != stem_radius
        if isAboveX and isNotSameAsRadius:
            isNotTooSmall = calculate_distance(p_top1,p_top2) >= 60
            isSmallerThanDiameter = len_top < stem_radius*2
            notHidingRadius = (p_top1[0] < 0 and p_top2[0] < 0) or (p_top1[0] > 0 and p_top2[0] > 0)
            if isNotTooSmall and isSmallerThanDiameter and notHidingRadius:
                break
    l_top = [p_top1,p_top2]
    #line below x_axis
    while True:
        p_bottom1 = find_p_in_circle(radius)
        p_bottom2 = find_p_in_circle(radius,[p_bottom1])
        len_bottom = int(calculate_distance(p_bottom1,p_bottom2)/ratio)
        if p_bottom1[1] < 0 and p_bottom2[1] < 0 and len_bottom not in [len_top,stem_radius]:
            if calculate_distance(p_bottom1,p_bottom2) >= 60 and len_bottom < sphere.diameter:
                break
    l_bottom = [p_bottom1,p_bottom2]
    #draw
    drawLine(ax,l_top)
    drawLine(ax,l_bottom)
    drawArc(ax,l_top,'bottom','$%s \mathrm{cm}$'%(len_top))
    drawArc(ax,l_bottom,'top','$%s \mathrm{cm}$'%(len_bottom))
    #stem/answer/comment
    stem = "구의 반지름은 몇 $$수식$$rm cm$$/수식$$인가요?"
    answer = '(답): $$수식$$%srm cm$$/수식$$'%(sphere.radius)
    comment = "(해설)구의 중심에서 구의 겉면의 한 점을 이은\n"\
                "선분의 길이는 $$수식$$%srm cm$$/수식$$입니다."%(
                    sphere.radius
                )
    svg= saveSvg()
    #plt.show()
    return stem, answer, comment, svg

#6-2-6-40
def cylinder626_Stem_010():
    #generate variable
    pi = 3
    while True:
        sphere = Sphere(pi)
        if sphere.radius < 10:
            break
    #stem/answer/comment
    stem = '지름이 $$수식$$%srm cm$$/수식$$인 구를 잘랐을 때 생기는\n'\
            "가장 큰 단면의 둘레와 넓이를 각각 구해 보세요.\n"\
            "(원주율: $$수식$$3$$/수식$$)"%(sphere.diameter)
    answer = '(답): $$수식$$%srm cm$$/수식$$, $$수식$$%srm cm^{2}$$/수식$$'%(
        sphere.perimeter, sphere.area
    )
    comment = "(해설)구를 잘랐을 때 생기는 단면 중에서 구의 중심을\n"\
                "지나는 단면이 가장 넓습니다.\n"\
                "$$수식$$\\rightarrow$$/수식$$ (가장 큰 단면의 둘레) $$수식$$= %s \\times 3 = %s(rm cm)$$/수식$$,\n"\
                "(가장 큰 단면의 넓이) $$수식$$= %s \\times %s \\times 3 = %s(rm cm^{2})$$/수식$$\n"%(
                    sphere.diameter, sphere.perimeter,
                    sphere.radius, sphere.radius, sphere.area
                )
    return stem, answer, comment

if __name__ == '__main__':
    stem,answer,comment = cylinder626_Stem_010()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')