import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib import font_manager, rc
import random

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
import os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../img/')

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
        #if i == 0 or i == len(points)-1:
        #    plt.text(points[i][0]+0.5, points[i][1]+0.1, text[i], fontsize=14, zorder=3)
        #else:
        #top, bottom, right, left, top_r, top_l, bottom_r,bottom_l
        cp = points[i]
        l = len(text[i])
        if position[i] == 'top':
            plt.text(cp[0]-2*l, cp[1]+3.5, text[i], fontsize=10, zorder=3)
        elif position[i] == 'bottom':
            plt.text(cp[0]-2*l, cp[1]-7.5, text[i], fontsize=10, zorder=3)
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

# 직선
def drawLine(ax,pts,dash=False):
    if dash: linestype = '--'
    else: linestype = '-'
    line_1 = matplotlib.lines.Line2D((pts[0][0],pts[1][0]), (pts[0][1],pts[1][1]), linewidth=1, linestyle = linestype,color='black')
    ax.add_line(line_1)

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
    plt.text(x-l, y, text, fontsize=10, zorder=3)

def drawText_(ax,text='',xy=(0,0)):
    if len(xy) > 2: raise Exception("too many inputs for xy")
    l = len(str(text))
    x,y = xy
    plt.text(x-l, y, text, fontsize=10, zorder=3)


# 선분의 길이를 표시하는 bezier 곡선을 그리는 함수
def drawArc(ax, p1, p2, position, text, boxed=False):
    cp = controlPoint(p1,p2,position)
    d = math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
    l = len(text)
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

    '''
    if boxed:
        if position == 'top':
            plt.text(cp[0]-0.1*l, cp[1], text, fontsize=15, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom':
            plt.text(cp[0]-0.1*l, cp[1], text, fontsize=15, bbox=dict(ec='black', fc='white'))
        elif position == 'left':
            plt.text(cp[0]+0.03*l, cp[1], text, fontsize=15, bbox=dict(ec='black', fc='white'))
        elif position == 'right':
            plt.text(cp[0]-0.25*l, cp[1], text, fontsize=15, bbox=dict(ec='black', fc='white'))
    else:
        if position == 'top':
            plt.text(cp[0]-0.1*l, cp[1], text, fontsize=14)
        elif position == 'bottom':
            plt.text(cp[0]-0.1*l, cp[1], text, fontsize=14)
        elif position == 'left':
            plt.text(cp[0]+0.03*l, cp[1], text, fontsize=14)
        elif position == 'right':
            plt.text(cp[0]-0.25*l, cp[1], text, fontsize=14)
    '''

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
            plt.text(cp[0]+l, cp[1]-2, text, fontsize=10, zorder=3)
        elif position == 'top_r':
            plt.text(cp[0]+l*0.3, cp[1]+2, text, fontsize=10, zorder=3)
        elif position == 'top_l':
            plt.text(cp[0]+1-l*5, cp[1]+2, text, fontsize=10, zorder=3)
        elif position == 'bottom_r':
            plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5, text, fontsize=10, zorder=3)
        elif position == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5, text, fontsize=10, zorder=3)
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
        plt.text(cp[0]-l*0.425, middle_p[1]-2, text, fontsize=10, zorder=3)
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
def setChart(points=[], figsize=None):
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

    if figsize == None:
        fig, ax = plt.subplots(figsize=(5, 5))
    else:
        fig, ax = plt.subplots(figsize=figsize)

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
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf8')


#font_name = font_manager.FontProperties(fname='C:/WINDOWS/FONTS/MALGUN.TTF').get_name()
#rc('font', family=font_name)  # For Windows

DIR = PATH

def proc_img(file, figsize=None):
    scale = 200
    O = (0, 0)
    x_p = (scale, 0)
    y_p = (0, scale)
    x_n = (scale * -1, 0)
    y_n = (0, scale * -1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2, figsize)

    img = mpimg.imread(file)
    img_width, img_height = img.shape[0], img.shape[1]
    img_max = max(img_width, img_height)

    if img_max <= 340:
        img_zoom = round(340 / img_max)
    elif img_max > 340:
        img_zoom = (340 / img_max) * 10
        img_zoom = math.floor(img_zoom) / 10
    else:
        img_zoom = 1

    imageBox = OffsetImage(img, zoom=1 * img_zoom)
    ab = AnnotationBbox(imageBox, (0, 0), frameon=False)
    ax.add_artist(ab)

    svg = saveSvg()

    return svg


# 2-1-4-005 / 상 / 추론력
def measuringlen214_Stem_001():
    # 사람별 칠판 길이를 잰 결과를 리스트로 만들어서 정렬
    names = ['성우', '진수', '영희', '선우']
    numbers = np.random.choice(np.arange(4,10), 4, False)
    name_number_zip = list(zip(names, numbers))
    name_number_zip.sort(key=lambda x: (x[1], x[0]), reverse=True)

    # 질문에 나오는 사람은 앞에서 두번째이고
    q01 = name_number_zip[1][0]
    # 정답은 길이가 가장 작은(첫 번째) 사람이다.
    answer_result = name_number_zip[0][0]

    # [[사람이름, 길이], ...] 형식의 이중 리스트를 딕셔너리로 바꾼 뒤에 표를 만든다.
    name_number_dict = dict(name_number_zip)
    names = list(name_number_dict.keys())
    random.shuffle(names)

    # 2행 4열로 구성된 리스트 생성
    data = [names]
    cell = [name_number_dict[n] for n in names]
    data.append(cell)

    table = '\n$$표$${n1} : $$수식$${d1}$$/수식$$\n{n2} : $$수식$${d2}$$/수식$$\n{n3} : $$수식$${d3}$$/수식$$\n{n4} : $$수식$${d4}$$/수식$$\n$$/표$$'.format(
        n1=data[0][0], d1=data[1][0], n2=data[0][1], d2=data[1][1], n3=data[0][2], d3=data[1][2], n4=data[0][3], d4=data[1][3])

    stem = '%s와 친구들이 각자의 뼘으로 칠판의 긴 쪽의 길이를 재었습니다.\n' \
           '%s보다 한 뼘의 길이가 더 긴 사람은 누구인가요?\n' % (q01, q01)
    stem = stem + table
    answer = "(정답)\n" \
             "%s" % answer_result
    comment = '(해설)\n' \
              '같은 길이를 잴 때 한 뼘의 길이가 길수록 재어 나타낸 수가 작습니다.\n' \
              '따라서 %s보다 한 뼘의 길이가 더 작은 사람은 뼘으로 재어 나타낸 수가 $$수식$$%s$$/수식$$보다 큰 %s입니다.' % (q01, name_number_zip[1][1], answer_result)

    return stem, answer, comment


# 2-1-4-006 / 기본 / 이해력
def measuringlen214_Stem_002():
    plt.rc('font', family='NanumGothic')
    num01, num02 = np.random.choice(range(2, 9), 2, False)

    stem = '㉠, ㉡에 알맞은 수를 차례대로 써 보세요.\n' \
           '$$표$$$$수식$$1 rm {{cm}}$$/수식$$가 $$수식$$%s$$/수식$$번이면 ㉠이고, $$수식$$%s rm {{cm}}$$/수식$$는 $$수식$$1 rm {{cm}}$$/수식$$가 ㉡번입니다.$$/표$$\n' % (
        num01, num02
    )
    answer = '(정답)\n' \
             '$$수식$$%s$$/수식$$, $$수식$$%s$$/수식$$' % (num01, num02)
    comment = '(해설)\n' \
              '$$수식$$1 rm {{cm}}$$/수식$$가 $$수식$$%s$$/수식$$번 → $$수식$$%s rm {{cm}}$$/수식$$, $$수식$$%s rm {{cm}}$$/수식$$ → $$수식$$1 rm {{cm}}$$/수식$$가 $$수식$$%s$$/수식$$번' % (
        num01, num01, num02, num02
    )

    return stem, answer, comment


# 2-1-4-007 / 중 / 이해력
def measuringlen214_Stem_003():
    plt.rc('font', family='NanumGothic')
    img_list = [{'filename': 'measuringlen214_Stem_003_2cm.jpg', 'number':2},
               {'filename': 'measuringlen214_Stem_003_3cm.jpg', 'number':3},
               {'filename': 'measuringlen214_Stem_003_4cm.jpg', 'number':4}]

    img_dict = random.choice(img_list)
    img_path = DIR + img_dict['filename']
    number = img_dict['number']

    svg = proc_img(img_path, (5, 2))

    stem = '그림을 보고 □ 안에 알맞은 수를 써넣고, 그 길이를 써 보세요.\n' \
           '$$수식$$1 rm {{cm}}$$/수식$$가 $$수식$$BOX{`①`}$$/수식$$번\n' \
           '$$수식$$BOX{`②`}$$/수식$$ $$수식$$rm {{cm}}$$/수식$$\n'
    answer = '(정답)\n' \
             '$$수식$$%s$$/수식$$, $$수식$$%s$$/수식$$' % (number, number)
    comment = '(해설)\n' \
              '$$수식$$1 rm {{cm}}$$/수식$$가 $$수식$$%s$$/수식$$번이면 $$수식$$%s rm {{cm}}$$/수식$$입니다.' % (number, number)

    return stem, answer, comment, svg


# 2-1-4-008 / 중 / 이해력
def measuringlen214_Stem_004():
    plt.rc('font', family='NanumGothic')
    nums = random.sample(range(2, 9), 3)
    num01, num02, num03 = nums

    # 보기 3종 생성
    example_list = [{'exp': '$$수식$$%s rm {{cm}}$$/수식$$' % num01, 'num': num01},
               {'exp': '$$수식$$%s$$/수식$$ 센티미터' % num02, 'num': num02},
               {'exp': '$$수식$$1 rm {{cm}}$$/수식$$가 $$수식$$%s$$/수식$$번' % num03, 'num': num03}]

    # 랜덤 돌려서 ㄱ, ㄴ, ㄷ 지정
    random.shuffle(example_list)
    example_list[0]['idx'] = '㉠'
    example_list[1]['idx'] = '㉡'
    example_list[2]['idx'] = '㉢'

    exp01, exp02, exp03 = [d['exp'] for d in example_list]
    num01, num02, num03 = [d['num'] for d in example_list]

    # ㄱ, ㄴ, ㄷ 보기를 숫자 순서대로 내림차순 정렬
    sorted_dictionary_list = sorted(example_list, key=lambda d: (d['num']), reverse=True)
    sorted_idx, sorted_num = [], []
    for sd in sorted_dictionary_list:
        i = sd['idx']
        n = sd['num']
        sorted_idx.append(i)
        sorted_num.append(n)

    idx01, idx02, idx03 = sorted_idx

    stem = '길이가 긴 것부터 차례로 기호를 써 보세요.\n'
    stem += '$$표$$㉠ %s\n' \
            '㉡ %s\n' \
            '㉢ %s$$/표$$\n' % (exp01, exp02, exp03)
    answer = '(정답)\n' \
             '%s, %s, %s' % (idx01, idx02, idx03)
    comment = '(해설)\n' \
              '길이를 $$수식$$ rm {{cm}}$$/수식$$로 나타내면 ㉠ $$수식$$%s$$/수식$$, ㉡ $$수식$$%s$$/수식$$, ㉢ $$수식$$%s$$/수식$$입니다.\n' \
              '$$수식$$%s$$/수식$$이므로 길이가 긴 것부터 기호를 쓰면 %s, %s, %s입니다.' % (num01, num02, num03, ' `>` '.join(map(str, sorted_num)), idx01, idx02, idx03)

    svg = ''
    return stem, answer, comment, svg


# 2-1-4-009 / 상 / 문제해결력
def measuringlen214_Stem_005():
    plt.rc('font', family='NanumGothic')
    num01, num02 = np.random.randint(5, 8, 2)
    num03 = num01 * num02

    exp01 = ' `+` '.join(['6' for _ in range(num02)])
    exp01 += ' `=` %s' % num03

    stem = '정호와 성현이가 각자의 뼘으로 나무의 길이를 재었더니 정호의 뼘으로 $$수식$$%s$$/수식$$뼘이었습니다. \n' \
           '정호와 성현이의 한 뼘의 길이가 각각 $$수식$$%s rm {{cm}}$$/수식$$, $$수식$$%s rm {{cm}}$$/수식$$라면 나무의 길이는 성현이의 뼘으로 몇 뼘일까요?' % (num02, num01, num02)
    answer = '(정답)\n' \
             '$$수식$$%s$$/수식$$뼘' % num01
    comment = '(해설)\n' \
              '나무의 길이는 정호의 뺨으로 $$수식$$%s$$/수식$$뼘이므로 $$수식$$%s(rm cm)$$/수식$$입니다. \n' \
              '$$수식$$%s rm {{cm}}$$/수식$$는 성현이의 한 뼘 $$수식$$%s rm {{cm}}$$/수식$$를 $$수식$$%s$$/수식$$번 더한 것과 같으므로 ' \
              '나무의 길이는 성현이의 뼘으로 $$수식$$%s$$/수식$$뼘입니다.' % (num02, exp01, num03, num02, num01, num01)

    svg = ''
    return stem, answer, comment, svg


# 2-1-4-010 / 상 / 문제해결력
def measuringlen214_Stem_006():
    plt.rc('font', family='NanumGothic')
    img_list = [{'filename': 'measuringlen214_Stem_006_col3.jpg', 'number':10},
               {'filename': 'measuringlen214_Stem_006_col4.jpg', 'number':12},
                {'filename': 'measuringlen214_Stem_006_col5.jpg', 'number':14},
                {'filename': 'measuringlen214_Stem_006_col6.jpg', 'number':16}]

    img_dict = random.choice(img_list)
    img_path = DIR + img_dict['filename']
    svg = proc_img(img_path)
    number = img_dict['number']

    stem = '그림에서 가장 작은 사각형의 네 변의 길이는 모두 같고, 한 변은 $$수식$$1 rm {{cm}}$$/수식$$입니다.\n' \
           '가장 큰 사각형의 네 변의 길이의 합은 몇 $$수식$$ rm {{cm}}$$/수식$$인가요?\n'
    answer = '(정답)\n' \
             '$$수식$$%s rm {{cm}}$$/수식$$' % number
    comment = '(해설)\n' \
              '가장 큰 사각형의 네 변에는 $$수식$$1 rm {{cm}}$$/수식$$가 $$수식$$%s$$/수식$$번 들어갑니다.\n' \
              '따라서 가장 큰 사각형의 네 변의 길이의 합은 $$수식$$1 rm {{cm}}$$/수식$$로 $$수식$$%s$$/수식$$번이므로 $$수식$$%s rm {{cm}}$$/수식$$입니다.' % (number, number, number)

    return stem, answer, comment, svg


# 2-1-4-011 / 상 / 문제해결력
def measuringlen214_Stem_007():
    plt.rc('font', family='NanumGothic')
    img_path = DIR + 'measuringlen214_Stem_007_input.jpg'
    svg = proc_img(img_path)

    num = np.random.randint(2, 5, 1)[0]
    answer_result = (12 * num) - (3 * (num-1))
    exp01 = ' `+` '.join(['12' for _ in range(num)])
    exp01 += ' `=` %s rm cm' % (12*num)
    exp02 = ' `+` '.join(['3' for _ in range(num-1)])
    exp02 += ' `=` %s rm cm' % (3*(num-1))
    exp03 = '`=` %s `-` %s `=` %s rm cm' % (12*num, 3*(num-1), answer_result)


    stem = '그림과 같이 길이가 $$수식$$12 rm {{cm}}$$/수식$$인 색 테이프 $$수식$$%s$$/수식$$장을 $$수식$$3 rm {{cm}}$$/수식$$씩 겹치도록 이어 붙였습니다.\n' \
           '이어 붙인 색 테이프의 전체 길이는 몇 $$수식$$ rm {{cm}}$$/수식$$인가요?\n' % num
    answer = '(정답)\n' \
             '$$수식$$%s rm {{cm}}$$/수식$$' % answer_result
    comment = '(해설)\n' \
              '길이가 $$수식$$12 rm {{cm}}$$/수식$$인 색 테이프 $$수식$$%s$$/수식$$장의 길이의 합은 $$수식$$%s$$/수식$$입니다.\n' \
              '겹친 부분은 $$수식$$3 rm {{cm}}$$/수식$$씩 $$수식$$%s$$/수식$$군데이므로 겹친 부분의 길이의 합은 $$수식$$%s$$/수식$$입니다.\n' \
              '→ (이어 붙인 색 테이프의 전체 길이) $$수식$$%s$$/수식$$' % (num, exp01, num-1, exp02, exp03)

    return stem, answer, comment, svg


# 2-1-4-015 / 중 / 이해력
def measuringlen214_Stem_008():
    plt.rc('font', family='NanumGothic')
    img_list = [{'filename': 'measuringlen214_Stem_008_1to5.jpg', 'max': 5, 'min': 1},
                {'filename': 'measuringlen214_Stem_008_1to6.jpg', 'max': 6, 'min': 1},
                {'filename': 'measuringlen214_Stem_008_2to6.jpg', 'max': 6, 'min': 2},
                {'filename': 'measuringlen214_Stem_008_2to7.jpg', 'max': 7, 'min': 2},
                {'filename': 'measuringlen214_Stem_008_3to7.jpg', 'max': 7, 'min': 3},
                {'filename': 'measuringlen214_Stem_008_3to8.jpg', 'max': 8, 'min': 3},
                {'filename': 'measuringlen214_Stem_008_4to8.jpg', 'max': 8, 'min': 4},
                {'filename': 'measuringlen214_Stem_008_4to9.jpg', 'max': 9, 'min': 4},
                {'filename': 'measuringlen214_Stem_008_5to9.jpg', 'max': 9, 'min': 5}]

    img_dict = random.choice(img_list)
    img_path = DIR + img_dict['filename']
    svg = proc_img(img_path, (5, 2))

    max = img_dict['max']
    min = img_dict['min']
    answer_result = max - min

    stem = '색연필의 길이는 몇 $$수식$$ rm {{cm}}$$/수식$$인가요?\n'
    answer = '(정답)\n' \
             '$$수식$$%s rm {{cm}}$$/수식$$' % answer_result
    comment = '(해설)\n' \
              '색연필의 길이는 $$수식$$%s$$/수식$$부터 $$수식$$%s$$/수식$$까지 $$수식$$1 rm {{cm}}$$/수식$$가 $$수식$$%s$$/수식$$번 들어가므로 $$수식$$%s rm {{cm}}$$/수식$$입니다.' % (
                  min, max, answer_result, answer_result
    )

    return stem, answer, comment, svg


# 2-1-4-016 / 상 / 문제해결력
def measuringlen214_Stem_009():
    plt.rc('font', family='NanumGothic')
    num01, num02 = np.random.choice(np.arange(2, 9), 2, False)
    length = np.random.randint(2, 9)
    ans01 = num01 * length
    ans02 = num02 * length

    exp01 = ' `+` '.join([str(length) for _ in range(num01)])
    exp01 += '`=` %s' % ans01
    exp02 = ' `+` '.join([str(length) for _ in range(num02)])
    exp02 += '`=` %s' % ans02

    # 2행 2열로 구성된 리스트 생성
    fig, ax = plt.subplots(1, 1, figsize=(5, 2))
    data = [['정진', '우희'], [num01, num02]]
    t = ax.table(cellText=data, cellLoc='center', loc="center")
    t.set_fontsize(20)
    t.scale(1,4)
    ax.axis('tight')
    ax.set_axis_off()
    svg = saveSvg()

    stem = '길이가 약 $$수식$$%s rm {{cm}}$$/수식$$인 막대로 정진이와 우희가 가지고 있는 끈의 길이를 재었습니다.\n' \
           '정진이와 우희가 가지고 있는 끈의 길이는 각각 약 몇 $$수식$$ rm {{cm}}$$/수식$$인가요?\n' \
           '정진이는 약 $$수식$$BOX{`①`}$$/수식$$ $$수식$$rm{{cm}}$$/수식$$\n' \
           '우희는 약 $$수식$$BOX{`②`}$$/수식$$ $$수식$$rm {{cm}}$$/수식$$\n' % length
    answer = '(정답)\n' \
             '$$수식$$%s$$/수식$$, $$수식$$%s$$/수식$$' % (ans01, ans02)
    comment = '(해설)\n' \
              '정진: $$수식$$%s$$/수식$$이므로 약 $$수식$$%s rm {{cm}}$$/수식$$입니다.\n' \
              '우희: $$수식$$%s$$/수식$$이므로 약 $$수식$$%s rm {{cm}}$$/수식$$입니다.' % (exp01, ans01, exp02, ans02)

    return stem, answer, comment, svg


# 2-1-4-018 / 상 / 문제해결력
def measuringlen214_Stem_010():
    plt.rc('font', family='NanumGothic')
    table_h = random.randint(4, 9) * 10
    num01, num02 = np.random.choice(np.arange(2, 8), 2, False)

    num03 = table_h + num01
    num03_exp = '%s `+` %s `=` %s' % (table_h, num01, num03)
    num04 = num03 - num02
    num04_exp = '%s `-` %s `=` %s' % (num03, num02, num04)

    stem = '책상의 높이를 희정이는 약 $$수식$$%s rm {{cm}}$$/수식$$로 어림하였고, 은수는 희정이보다 $$수식$$%s rm {{cm}}$$/수식$$ 더 높게, ' \
           '효정이는 은수보다 $$수식$$%s rm {{cm}}$$/수식$$ 더 낮게 어림하였습니다. 효정이가 어림한 높이는 약 몇 $$수식$$ rm {{cm}}$$/수식$$인가요?' % (table_h, num01, num02)
    answer = '(정답)\n' \
             '약 $$수식$$%s rm {{cm}}$$/수식$$' % num04
    comment = '(해설)\n' \
              '은수가 어림한 책상의 높이는 약 $$수식$$%s(rm cm)$$/수식$$입니다.\n' \
              '따라서 효정이가 어림한 책상의 높이는 약 $$수식$$%s(rm cm)$$/수식$$입니다.' % (num03_exp, num04_exp)

    svg = ''
    return stem, answer, comment, svg


if __name__ == '__main__':
    # stem, answer, comment, svg = measuringlen214_Stem_001()
    # stem, answer, comment, svg = measuringlen214_Stem_002()
    # stem, answer, comment, svg = measuringlen214_Stem_003()
    # stem, answer, comment, svg = measuringlen214_Stem_004()
    # stem, answer, comment, svg = measuringlen214_Stem_005()
    # stem, answer, comment, svg = measuringlen214_Stem_006()
    # stem, answer, comment, svg = measuringlen214_Stem_007()
    # stem, answer, comment, svg = measuringlen214_Stem_008()
    # stem, answer, comment, svg = measuringlen214_Stem_009()
    stem, answer, comment, svg = measuringlen214_Stem_010()


    print(stem)
    print(answer)
    print(comment)

    plt.show()
