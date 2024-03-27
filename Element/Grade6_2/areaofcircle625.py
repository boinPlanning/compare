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
            plt.text(cp[0]-l*1.5, top_y, text[i], fontsize=16, zorder=3)
        elif position == 'bottom':
            plt.text(cp[0]-l*1.5, bottom_y, text[i], fontsize=16, zorder=3)
        elif position == 'left':
            plt.text(left_x, cp[1]-2, text[i], fontsize=16, zorder=3)
        elif position == 'right':
            plt.text(right_x, cp[1]-2, text[i], fontsize=16, zorder=3)
        elif position == 'top_r':
            plt.text(right_x, top_y, text[i], fontsize=16, zorder=3)
        elif position == 'top_l':
            plt.text(left_x, top_y, text[i], fontsize=16, zorder=3)
        elif position == 'bottom_r':
            plt.text(right_x, bottom_y, text[i], fontsize=16, zorder=3)
        elif position == 'bottom_l':
            plt.text(left_x, bottom_y, text[i], fontsize=16, zorder=3)
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

# 원
def drawCircle(ax,center, radius, fill=False, alpha=1, dash=False, position=None, color='',ec='black'):
    colors = []
    for i in mcolors.CSS4_COLORS:
        if i != 'white' or i != 'snow':
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

# 선분의 길이를 표시하는 bezier 곡선을 그리는 함수
def drawPolygonArc(ax,verts=list,show_length=[],show_text=[],length_ratio=10,unit='cm',alpha=1):
    def c_distance(p1=tuple, p2=tuple):
        import math
        d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
        return d
    def new_p_middle(p1=tuple,p2=tuple):
        return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
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
                drawArc(ax,[p1,p2],position,'$%s \\mathrm{%s}$'%(length,unit))
        if show_text != []: 
            if show_text[i] != '':
                drawArc(ax,[p1,p2],position,show_text[i])
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
            plt.text(cp[0]-2-l*4.5, cp[1]-2, text, fontsize=16, zorder=3)
        elif position == 'right':
            plt.text(cp[0]+l*0.1, cp[1]-2, text, fontsize=16, zorder=3)
        elif position == 'top_r':
            plt.text(cp[0]+l*0.3, cp[1]+2, text, fontsize=16, zorder=3)
        elif position == 'top_l':
            plt.text(cp[0]+1-l*4, cp[1]+2, text, fontsize=16, zorder=3)
        elif position == 'bottom_r':
            plt.text(cp[0]+l, cp[1]-8+l*0.5, text, fontsize=16, zorder=3)
        elif position == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-3+l*0.5, text, fontsize=16, zorder=3)
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

def move_p_single(p,x_move=0,y_move=0):
        new_p = (p[0]+x_move,p[1]+y_move)
        return new_p
def get_circumferenceOfCircle(r,pi=3.14):
    return round(2*r*pi,2)
def get_diameter(r):
    return r*2
def get_areaOfCircle(r,pi=3.14):
    return round(r*r*pi,2)
def get_areaOfSquare(l):
    return l*l

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


#6-2-5-06
def areaofcircle625_Stem_001():
    #generate variable
    numberCircle_list = ['①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩', '⑪', '⑫', '⑬', '⑭', '⑮']
    diameter_list = []
    circumference_list = []
    while len(diameter_list) < 3:
        temp_diameter = random.randint(5,20)*5
        if temp_diameter not in diameter_list:
            diameter_list.append(temp_diameter)
            circumference_list.append(round(temp_diameter*3.14,1))
    #stem/answer/comment
    stem = "원주와 지름을 보고 원주율을 계산해 보세요.\n"\
            "$$표$$● 원주($$수식$$rm cm$$/수식$$):$$수식$$``%s``````$$/수식$$ 지름($$수식$$rm cm$$/수식$$):$$수식$$``%s``````$$/수식$$ 원주율: $$수식$$``$$/수식$$㉠\n● 원주($$수식$$rm cm$$/수식$$):$$수식$$``%s``````$$/수식$$ 지름($$수식$$rm cm$$/수식$$):$$수식$$``%s``````$$/수식$$ 원주율: $$수식$$``$$/수식$$㉡\n● 원주($$수식$$rm cm$$/수식$$):$$수식$$``%s``````$$/수식$$ 지름($$수식$$rm cm$$/수식$$):$$수식$$``%s``````$$/수식$$ 원주율: $$수식$$``$$/수식$$㉢$$/표$$"%(
                circumference_list[0],diameter_list[0],
                circumference_list[1],diameter_list[1],
                circumference_list[2],diameter_list[2]
            )
    answer = "(답):㉠ $$수식$$3.14$$/수식$$, ㉡ $$수식$$3.14$$/수식$$, ㉢ $$수식$$3.14$$/수식$$"
    comment = "(해설)\n㉠ $$수식$$%s div %s = 3.14$$/수식$$,\n"\
                "㉡ $$수식$$%s div %s = 3.14$$/수식$$,\n"\
                "㉢ $$수식$$%s div %s = 3.14$$/수식$$"%(
                circumference_list[0],diameter_list[0],
                circumference_list[1],diameter_list[1],
                circumference_list[2],diameter_list[2]
            )
    return stem,answer,comment

#6-2-5-09
def areaofcircle625_Stem_002():
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
    radius = random.randint(3,20)
    diameter = radius * 2
    circumference = diameter * 3
    #generate circle
    l_radius = [O,(70,0)]
    #draw
    drawCircle(ax,O,70)
    drawDot(ax,[O],True)
    drawArc(ax,l_radius,'top','    ',boxed=True)
    drawLine(ax,l_radius)
    #stem/answer/comment
    stem = "원주가 $$수식$$%srm cm$$/수식$$인 원입니다. □안에 알맞은 수를 써넣으세요. (원주율: $$수식$$3$$/수식$$)"%(circumference)
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(radius)
    comment = "(해설)\n(원의 지름) $$수식$$=$$/수식$$ (원주) $$수식$$div$$/수식$$ (원주율)\n"\
                "$$수식$$= %s div 3 = %s$$/수식$$"\
                "따라서 원의 반지름은 $$수식$$%s div 2 = %s(rm cm)$$/수식$$입니다."%(
                    circumference, diameter,
                    diameter, radius
                )
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem,answer,comment,svg

#6-2-5-11
def areaofcircle625_Stem_003():
    #generate variable
    radius = random.randint(3,20)
    diameter = radius * 2
    circumference = diameter * 3
    #stem/answer/comment
    stem = "길이가 $$수식$$%srm cm$$/수식$$인 종이 띠를 겹치지 않게 붙여서 원을 만들었습니다. 만들어진 원의 지름은 몇 $$수식$$rm cm$$/수식$$인가요? (원주율: $$수식$$3$$/수식$$)"%(
                circumference
            )
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(diameter)
    comment = "(해설)\n(원의 지름) $$수식$$= %s div 3 = %s(rm cm)$$/수식$$"%(
        circumference, diameter
    )
    return stem,answer,comment

#6-2-5-13
def areaofcircle625_Stem_004():
    #generate variable
    pi = 3.14
    radius = random.randint(3,20)
    diameter = radius * 2
    circumference = round(diameter * pi,2)
    #stem/answer/comment
    stem = "원주가 $$수식$$%srm cm$$/수식$$인 원의 반지름은 몇 $$수식$$rm cm$$/수식$$인가요? (원주율: $$수식$$3.14$$/수식$$)"%(circumference)
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(radius)
    comment = "(해설)\n(원의 반지름) $$수식$$=$$/수식$$ (원주) $$수식$$div$$/수식$$ (원주율) $$수식$$div$$/수식$$ $$수식$$2$$/수식$$ \n"\
                "$$수식$$= %s div %s div 2 = %s(rm cm)$$/수식$$"%(
                    circumference,pi,radius
                )
    return stem,answer,comment

#6-2-5-15
def areaofcircle625_Stem_005():
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
    radius = random.randint(3,20)
    diameter = radius * 2
    circumference = round(diameter * pi / 2,2)
    #generate circle
    l_radius = [O,(70,0)]
    l_diameter = [(-70,0),(70,0)]
    #draw
    drawCircle(ax,O,70,position='top')
    drawLine(ax,l_diameter)
    drawDot(ax,[O],True)
    drawArc(ax,l_radius,'top','$%s \mathrm{cm}$'%(radius))
    #stem/answer/comment
    stem = "반원의 둘레는 몇 $$수식$$rm cm$$/수식$$인가요? (원주율: $$수식$$3.1$$/수식$$)"
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(circumference+diameter)
    comment = "(해설)\n(반원의 둘레) $$수식$$=$$/수식$$ (원의 지름)$$수식$$times$$/수식$$(원주)$$수식$$div 2 + $$/수식$$(지름)\n"\
                "$$수식$$= %s times 2 times 3.1 div 2 + %s times 2$$/수식$$\n"\
                "$$수식$$= %s + %s = %s(rm cm)$$/수식$$"%(
                    radius, radius,
                    circumference, diameter, circumference + diameter
                )
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem,answer,comment,svg

#6-2-5-19
def areaofcircle625_Stem_006():
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
    radius_small = random.randint(3,10)
    radius_big = radius_small*2
    #generate circle
    l_diameter_big = [(-70,0),(70,0)]
    #draw
    drawCircle(ax,O,70)
    drawCircle(ax,(-35,0),35)
    drawLine(ax,l_diameter_big)
    drawDot(ax,[O,(-35,0)],True)
    #stem/answer/comment
    stem = "큰 원의 원주는 $$수식$$%srm cm$$/수식$$입니다. 두 원의 반지름의 합은 몇 $$수식$$rm cm$$/수식$$인가요? (원주율: $$수식$$3$$/수식$$)"%(get_circumferenceOfCircle(radius_big,pi))
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(radius_big+radius_small)
    comment = "(해설)\n(큰 원의 반지름) $$수식$$= %s div 3 div 2 = %s(rm cm)$$/수식$$\n"\
                "(작은 원의 반지름) $$수식$$= %s div 2 = %s(rm cm)$$/수식$$\n"\
                "따라서 두 원의 반지름의 합은 $$수식$$%s + %s = %s(rm cm)$$/수식$$\n"\
                "입니다."%(
                    get_circumferenceOfCircle(radius_big,pi),radius_big,
                    radius_big,radius_small,
                    radius_big,radius_small,radius_big+radius_small
                )
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem,answer,comment,svg

#6-2-5-30
def areaofcircle625_Stem_007():
    #generate variable
    radius = random.randint(5,15)
    pi = 3
    name_list = ['철수','영희','기철이','찬호','수호','경철이']
    name = random.choice(name_list)
    #stem/answer/comment
    stem = "%s는 컴퍼스의 침과 연필심 사이의 거리를 $$수식$$%srm cm$$/수식$$만큼 벌려서 원을 그렸습니다. %s가 그린 원의 넓이는 몇 $$수식$$rm cm^{2}$$/수식$$인가요? (원주율: $$수식$$3$$/수식$$)"%(
                name,
                radius,name
            )
    answer = "(답):$$수식$$%srm cm^{2}$$/수식$$"%(get_areaOfCircle(radius,pi))
    comment = "(해설)\n(원의 넓이) $$수식$$= %s times %s times %s = %s(rm cm^{2})$$/수식$$"%(
        radius,radius,pi,get_areaOfCircle(radius,pi)
    )
    return stem,answer,comment

#6-2-5-31
def areaofcircle625_Stem_008():
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
    radius_small = random.randint(3,5)
    radius_big = random.randint(7,10)
    #generate circle
    ratio = 8
    p_big = (-10-radius_big*ratio,0)
    p_small = (10+radius_small*ratio,0)
    l_radius_big = [p_big,move_p_single(p_big,radius_big*ratio)]
    l_radius_small = [p_small,move_p_single(p_small,radius_small*ratio)]
    p_text_big = (p_big[0],p_big[1]+10+radius_big*ratio)
    p_text_small = (p_small[0],p_big[1]+10+radius_big*ratio)
    #draw
    drawCircle(ax,p_big,radius_big*ratio)
    drawCircle(ax,p_small,radius_small*ratio)
    drawLine(ax,l_radius_big)
    drawLine(ax,l_radius_small)
    drawArc(ax,l_radius_big,'top','$%s \mathrm{cm}$'%(radius_big))
    drawArc(ax,l_radius_small,'top','$%s \mathrm{cm}$'%(radius_small))
    drawDot(ax,[p_big,p_small],True)
    drawText(ax,'A',p_text_big,'top')
    drawText(ax,'B',p_text_small,'top')
    #stem/answer/comment
    stem = "두 원 $$수식$$A$$/수식$$와 $$수식$$B$$/수식$$가 있습니다. $$수식$$A$$/수식$$의 넓이는 $$수식$$B$$/수식$$의 넓이보다 몇 $$수식$$rm cm^{2}$$/수식$$ 더 넓은지 구해 보세요. (원주율: $$수식$$3$$/수식$$)"
    answer = "(답):$$수식$$%s rm cm^{2}$$/수식$$"%(get_areaOfCircle(radius_big,pi)-get_areaOfCircle(radius_small,pi))
    comment = "(해설)\n($$수식$$원A$$/수식$$의 넓이)$$수식$$= %s times %s times %s = %s(rm cm^{2})$$/수식$$\n"\
                "($$수식$$원B$$/수식$$의 넓이) $$수식$$= %s times %s times %s = %s(rm cm^{2})$$/수식$$\n"\
                " → $$수식$$%s - %s = %s(rm cm^{2})$$/수식$$"%(
                    radius_big,radius_big,pi,get_areaOfCircle(radius_big,pi),
                    radius_small,radius_small,pi,get_areaOfCircle(radius_small,pi),
                    get_areaOfCircle(radius_big,pi),get_areaOfCircle(radius_small,pi),
                    (get_areaOfCircle(radius_big,pi)-get_areaOfCircle(radius_small,pi))
                )
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem,answer,comment,svg

#6-2-5-34,36
def areaofcircle625_Stem_009():
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
    radius = random.randint(3,10)
    #generate circle
    p_center = (0,0)
    l_radius = [p_center,(-70,0)]
    l_diameter = [(-70,0),(70,0)]
    l_random = random.choice([l_radius,l_diameter])
    #draw
    drawCircle(ax,p_center,70)
    drawDot(ax,[p_center],True)
    drawLine(ax,l_random)
    drawArc(ax,l_random,'top','    ',True)
    #stem/answer/comment
    stem = "원의 넓이가 $$수식$$%srm cm^{2}$$/수식$$일 때 □ 안에 들어갈 알맞은 수를 구해 보세요. (원주율: $$수식$$3.14$$/수식$$)"%(
                get_areaOfCircle(radius)
            )
    comment = "(해설)\n원의 반지름을 □ $$수식$$rm cm$$/수식$$라 하면\n"\
                "(원의 넓이) $$수식$$= □ times □ times 3.14 = %s$$/수식$$,\n"\
                "$$수식$$ □ times □ = %s div 3.14 = %s$$/수식$$,\n"\
                "$$수식$$%s times %s = %s$$/수식$$이므로 반지름은 $$수식$$%srm cm$$/수식$$입니다.\n"%(
                    get_areaOfCircle(radius),
                    get_areaOfCircle(radius),radius*radius,
                    radius,radius,radius*radius,radius
                )
    if l_random == l_radius:
        answer = '(답):$$수식$$%srm cm$$/수식$$'%(radius)
    elif l_random == l_diameter:
        answer = '(답):$$수식$$%srm cm$$/수식$$'%(get_diameter(radius))
        comment += "→ (지름) $$수식$$= %s times 2 = %s(rm cm)$$/수식$$"%(
            radius,get_diameter(radius)
        )
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem,answer,comment,svg

#6-2-5-40
def areaofcircle625_Stem_010():
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
    radius_small = random.randint(1,5)
    radius_big = radius_small * 2
    #generate circle
    p_center_big = (0,0)
    p_center_small = (35,0)
    l_diameter_big = [(-70,0),(70,0)]
    #draw
    drawCircle(ax,p_center_big,70,True)
    drawCircle(ax,p_center_small,35,True,color='white')
    drawLine(ax,l_diameter_big)
    drawArc(ax,l_diameter_big,'top_l','$%s \mathrm{cm}$'%(get_diameter(radius_big)))
    drawDot(ax,[p_center_big,p_center_small],True)
    #stem/answer/comment
    stem = "색칠한 부분의 넓이를 구해 보세요.(원주율: $$수식$$3$$/수식$$)"
    answer = '(답):$$수식$$%srm cm^{2}$$/수식$$'%(get_areaOfCircle(radius_big,pi)-get_areaOfCircle(radius_small,pi))
    comment = "(해설)\n(색칠한 부분의 넓이)\n"\
                "$$수식$$=$$/수식$$ (큰 원의 넓이) $$수식$$-$$/수식$$ (작은 원의 넓이)\n"\
                "$$수식$$= (%s times %s times %s) - (%s times %s times %s)$$/수식$$\n"\
                "$$수식$$= %s - %s = %s(rm cm^{2})$$/수식$$"%(
                    radius_big,radius_big,pi, radius_small,radius_small,pi,
                    get_areaOfCircle(radius_big,pi),get_areaOfCircle(radius_small,pi),
                    (get_areaOfCircle(radius_big,pi)-get_areaOfCircle(radius_small,pi))
                )
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem,answer,comment,svg

#6-2-5-42
def areaofcircle625_Stem_011():
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
    pi = 3.14
    radius = random.randint(4,9)
    length = radius*2 + random.randint(4,6)
    areaOfColored = round(radius*2*length - get_areaOfCircle(radius),5)
    #generate circle
    ratio = 9
    p_center_left = (-(length/2)*ratio,0)
    p_center_right = ((length/2)*ratio,0)
    rectangle = [
        (p_center_left[0],p_center_left[1]+radius*ratio),
        (p_center_right[0],p_center_right[1]+radius*ratio),
        (p_center_right[0],p_center_right[1]-radius*ratio),
        (p_center_left[0],p_center_left[1]-radius*ratio),
    ]
    l_rectangle_left = [rectangle[0],rectangle[3]]
    l_rectangle_top = [rectangle[0],rectangle[1]]
    l_rectangle_right = [rectangle[1],rectangle[2]]
    l_rectangle_bottom = [rectangle[2],rectangle[3]]
    #draw
    drawPolygon(ax,rectangle,True)
    drawCircle(ax,p_center_left,radius*ratio,True,color='white',ec='white')
    drawSemiCircle(ax,p_center_left,radius*ratio,'right')
    drawCircle(ax,p_center_right,radius*ratio,True,color='white',ec='white')
    drawSemiCircle(ax,p_center_right,radius*ratio,'left')
    drawDot(ax,[p_center_right,p_center_left],True)
    drawLine_multiple(ax,[l_rectangle_left,l_rectangle_right],True)
    drawLine_multiple(ax,[l_rectangle_top,l_rectangle_bottom])
    drawPolygonArc(ax,rectangle,show_text=['$□ \mathrm{cm}$','$%s \mathrm{cm}$'%(radius*2),'',''])
    drawPolygonAngle(ax,rectangle,[1,1,1,1])
    #stem/answer/comment
    stem = "색칠한 부분의 넓이가 $$수식$$%srm cm^{2}$$/수식$$일 때 □ 안에 들어갈 알맞은 수를 구해 보세요. (원주율 $$수식$$3.14$$/수식$$)"%areaOfColored
    answer = '(답):$$수식$$%s$$/수식$$'%(length)
    comment = "(해설)\n반원 $$수식$$2$$/수식$$개를 합하면 원이 됩니다.\n"\
                "→ (색칠한 부분의 넓이)\n"\
                "$$수식$$=$$/수식$$ (직사각형의 넓이) $$수식$$-$$/수식$$ (원의 넓이)\n"\
                "$$수식$$= %s(rm cm^{2})$$/수식$$\n"\
                "$$수식$$□ times %s - %s times %s times 3.14 = %s$$/수식$$,\n"\
                "$$수식$$□ times %s - %s = %s$$/수식$$,\n"\
                "$$수식$$□ times %s = %s$$/수식$$, $$수식$$□ = %s$$/수식$$"%(
                    areaOfColored,
                    radius*2,radius,radius,areaOfColored,
                    radius*2,get_areaOfCircle(radius),areaOfColored,
                    radius*2,round(areaOfColored+get_areaOfCircle(radius)),length
                )
    len = (length/2)*ratio
    plt.axis([-len*1.2,len*1.2,-len,len])
    #plt.show()
    svg = saveSvg()
    return stem,answer,comment,svg

#6-2-5-46
def areaofcircle625_Stem_012():
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
    radius_small = random.randint(9,13)
    radius_big = radius_small + random.randint(1,3)
    areaOfColored = round((get_areaOfCircle(radius_big) - get_areaOfCircle(radius_small))/2,2)
    #generate polygon
    ratio = 9
    p_center = (0,0)
    l_diameter_big = [(-radius_big*ratio,0),(radius_big*ratio,0)]
    l_radius_small = [p_center,(radius_small*ratio,0)]
    l_radius_big = [(-radius_big*ratio,0),p_center]
    l_edge_l = [(-radius_big*ratio,0),(-radius_small*ratio,0)]
    l_edge_r = [(radius_big*ratio,0),(radius_small*ratio,0)]
    rectangle = [
        (-radius_big*ratio-5,0),(radius_big*ratio+5,0),
        (radius_big*ratio+5,-radius_big*ratio),(-radius_big*ratio-5,-radius_big*ratio)
    ]
    #draw
    drawCircle(ax,p_center,radius_big*ratio,True)
    drawCircle(ax,p_center,radius_small*ratio,True,color='white')
    drawPolygon(ax,rectangle,True,color='white',ec='white')
    drawDot(ax,[p_center],True)
    drawLine(ax,l_diameter_big,True)
    drawLine_multiple(ax,[l_edge_r,l_edge_l])
    drawArc(ax,l_radius_small,'bottom','$%s \mathrm{cm}$'%(radius_small))
    drawArc(ax,l_radius_big,'bottom','$%s \mathrm{cm}$'%(radius_big))
    #stem/answer/comment
    stem = "색칠한 부분의 도형의 넓이는 몇 $$수식$$rm cm^{2}$$/수식$$인가요? (원주율: $$수식$$3.14$$/수식$$)"
    answer = "(답):$$수식$$%srm cm^{2}$$/수식$$"%(areaOfColored)
    comment = "(해설)\n(색칠한 부분의 도형의 넓이)\n"\
                "$$수식$$=$$/수식$$ (반지름이 $$수식$$%srm cm$$/수식$$인 반원의 넓이)\n"\
                "     $$수식$$-$$/수식$$ (반지름이 $$수식$$%srm cm$$/수식$$인 반원의 넓이)\n"\
                "$$수식$$= (3.14 times %s times %s) div 2 - (3.14 times %s times %s) div 2$$/수식$$\n"\
                "$$수식$$= %s - %s = %s(rm cm^{2})$$/수식$$"%(
                    radius_big,
                    radius_small,
                    radius_big,radius_big, radius_small,radius_small,
                    round(get_areaOfCircle(radius_big)/2,2), round(get_areaOfCircle(radius_small)/2,2), areaOfColored
                )
    #plt.show()
    len = radius_big*ratio
    plt.axis([-len*1.2,len*1.2,-len,len*1.1])
    svg = saveSvg()
    return stem,answer,comment,svg

#6-2-5-49
def areaofcircle625_Stem_013():
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
    radius = random.randint(3,8)
    length = radius*2
    areaOfColored = round(length*length - get_areaOfCircle(radius),2)
    #generate polygon
    rectangle = create_p_rectangle(140,140)
    p_center = (0,0)
    #draw
    drawPolygon(ax,rectangle,True)
    drawCircle(ax,p_center,70,True,color='white')
    #stem/answer/comment
    stem = "정사각형 안에 가장 큰 원을 그려 넣었습니다. 정사각형의 넓이가 $$수식$$%srm cm^{2}$$/수식$$일 때, 색칠한 부분의 넓이를 구해 보세요. (원주율: $$수식$$3.14$$/수식$$)"%(length*length)
    answer = '(답):$$수식$$%srm cm^{2}$$/수식$$'%(areaOfColored)
    comment = "(해설)\n(정사각형의 넓이) $$수식$$=$$/수식$$ (변의 길이) $$수식$$times$$/수식$$ (변의 길이)\n"\
                "$$수식$$=%s times %s = %s$$/수식$$이므로 정사각형 한변의 길이는\n"\
                "$$수식$$%srm cm$$/수식$$이며, 반지름은 $$수식$$%srm cm$$/수식$$이다.\n"\
                "(색칠한 부분의 넓이)\n"\
                "$$수식$$=$$/수식$$ (정사각형의 넓이) $$수식$$-$$/수식$$ (원의 넓이)\n"\
                "$$수식$$= %s -$$/수식$$ (반지름) $$수식$$times$$/수식$$ (반지름) $$수식$$times 3.14$$/수식$$\n"\
                "$$수식$$= %s - %s times %s times 3.14 = %s - %s$$/수식$$\n"\
                "$$수식$$= %s(rm cm^{2})$$/수식$$"%(
                    length, length, get_areaOfSquare(length), length,
                    radius,
                    get_areaOfSquare(length),
                    get_areaOfSquare(length), radius, radius, get_areaOfSquare(length), get_areaOfCircle(radius),
                    areaOfColored
                )
    #plt.show()
    plt.axis('scaled')
    svg = saveSvg()
    return stem,answer,comment,svg
