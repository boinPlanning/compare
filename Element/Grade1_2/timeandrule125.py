import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
#from draw2svg import *
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
def setPoint(ax, points=list, text=[], position=[], fill=False):
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

    for i in range(0, len(points)):
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
            plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5,
                     text[i], fontsize=10, zorder=3)
        elif position[i] == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5,
                     text[i], fontsize=10, zorder=3)
        else:
            raise Exception('no matching position')
        #plt.text(points[i][0]-0.5, points[i][1]+0.1, text[i], fontsize=14, zorder=3)

        if fill:
            ax.plot(points[i][0], points[i][1], "k.", zorder=3)

    #for i in range(0,len(points)):
    #    ax.plot([points[i][0]], [points[i][1]],"ko", zorder=3)

# 점


def drawDot(ax, points=list, colors=False):
    if colors:
        format = 'r.'
    else:
        format = 'k.'
    for i in range(0, len(points)):
        ax.plot(points[i][0], points[i][1], format, zorder=3)

# 각


def drawAngle(ax, p_lists=[], diff=False):
    d = 50
    if diff:
        color = ['r', 'g', 'b', 'c', 'm', 'y']
        #width_list = [0.4*d,0.6*d,0.4*d,0.6*d]
    else:
        color = ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r']
    i = 0
    for p_list in p_lists:
        p1 = p_list[0]
        p2 = p_list[1]
        p3 = p_list[2]

        dx1 = p1[0] - p2[0]
        dy1 = p1[1] - p2[1]

        dx2 = p3[0] - p2[0]
        dy2 = p3[1] - p2[1]

        a1 = math.degrees(math.atan2(dy1, dx1))
        a2 = math.degrees(math.atan2(dy2, dx2))

        angle = a2 - a1
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
            if diff and (i % 2) == 1:
                pp = mpatches.Arc(p2, angle=0, width=width*3/4, height=height *
                                  3/4, theta1=a1, theta2=a2, ec=color[i], zorder=3)
                ax.add_patch(pp)
            pp = mpatches.Arc(p2, angle=0, width=width, height=height,
                              theta1=a1, theta2=a2, ec=color[i], zorder=3)
        elif angle > 30:
            if diff and (i % 2) == 1:
                pp = mpatches.Arc(p2, angle=0, width=width*2, height=height*2,
                                  theta1=a1, theta2=a2, ec=color[i], zorder=3)
                ax.add_patch(pp)
            pp = mpatches.Arc(p2, angle=0, width=width, height=height,
                              theta1=a1, theta2=a2, ec=color[i], zorder=3)
        else:
            raise Exception('wrong angle')

        ax.add_patch(pp)
        i += 1

# 직선


def drawLine(ax, pts, dash=False):
    if dash:
        linestype = '--'
    else:
        linestype = '-'
    line_1 = matplotlib.lines.Line2D(
        (pts[0][0], pts[1][0]), (pts[0][1], pts[1][1]), linewidth=1, linestyle=linestype, color='black')
    ax.add_line(line_1)

# 다각형


def drawPolygon(ax, verts, fill=False, alpha=1, dash=False):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    vert = verts
    vert.append(verts[0])
    codes = [Path.MOVETO]

    for i in range(0, len(vert)-2):
        codes.append(Path.LINETO)

    codes.append(Path.CLOSEPOLY)

    path = Path(vert, codes)

    if fill:
        if dash:
            pp = mpatches.PathPatch(path, fc=random.choice(
                colors), fill=True, lw=1, ls='--', zorder=3, alpha=alpha)
        else:
            pp = mpatches.PathPatch(path, fc=random.choice(
                colors), fill=True, lw=2, zorder=3, alpha=alpha)
    else:
        if dash:
            pp = mpatches.PathPatch(
                path, ec='black', fill=False, lw=1, ls='--', zorder=3)
        else:
            pp = mpatches.PathPatch(
                path, ec='black', fill=False, lw=2, zorder=3)
    ax.add_patch(pp)

# 다각형 + 각


def drawPolygonAngle(ax, verts=list, show_angle=False, show_angle_num=False):
    def drawAngle(ax, p_lists=[], diff=False):
        d = 50
        if diff:
            color = ['r', 'g', 'b', 'c', 'm', 'y']
            #width_list = [0.4*d,0.6*d,0.4*d,0.6*d]
        else:
            color = ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r']
        i = 0
        for p_list in p_lists:
            p1 = p_list[0]
            p2 = p_list[1]
            p3 = p_list[2]

            dx1 = p1[0] - p2[0]
            dy1 = p1[1] - p2[1]

            dx2 = p3[0] - p2[0]
            dy2 = p3[1] - p2[1]

            a1 = math.degrees(math.atan2(dy1, dx1))
            a2 = math.degrees(math.atan2(dy2, dx2))

            angle = a2 - a1
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
                if diff and (i % 2) == 1:
                    pp = mpatches.Arc(p2, angle=0, width=width*3/4, height=height *
                                      3/4, theta1=a1, theta2=a2, ec=color[i], zorder=3)
                    ax.add_patch(pp)
                pp = mpatches.Arc(p2, angle=0, width=width, height=height,
                                  theta1=a1, theta2=a2, ec=color[i], zorder=3)
            elif angle > 30:
                if diff and (i % 2) == 1:
                    pp = mpatches.Arc(p2, angle=0, width=width*2, height=height*2,
                                      theta1=a1, theta2=a2, ec=color[i], zorder=3)
                    ax.add_patch(pp)
                pp = mpatches.Arc(p2, angle=0, width=width, height=height,
                                  theta1=a1, theta2=a2, ec=color[i], zorder=3)
            else:
                raise Exception('wrong angle')

            ax.add_patch(pp)
            i += 1

    #draw angle
    for i in range(len(verts)):
        first_index = i % (len(verts))
        second_index = (i+1) % (len(verts))
        third_index = (i+2) % (len(verts))
        angle = [verts[first_index], verts[second_index], verts[third_index]]
        drawAngle(ax, [angle])

    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    vert = verts
    vert.append(verts[0])
    codes = [Path.MOVETO]

    for i in range(0, len(verts)-2):
        codes.append(Path.LINETO)

    codes.append(Path.CLOSEPOLY)

    path = Path(verts, codes)

    pp = mpatches.PathPatch(path, ec='black', fill=False, lw=2, zorder=3)
    ax.add_patch(pp)

# 원


def drawCircle(ax, center, radius, fill=False, alpha=1, dash=False, position=None):
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
            pp = mpatches.Arc(center, width=radius*2, height=radius*2, angle=0, theta1=theta1,
                              theta2=theta2, ec='black', lw=1, ls='--', fill=False, zorder=3)
        else:
            pp = mpatches.Arc(center, width=radius*2, height=radius*2, angle=0,
                              theta1=theta1, theta2=theta2, ec='black', lw=2, fill=False, zorder=3)
    else:
        if fill:
            if dash:
                pp = mpatches.Circle(center, radius=radius, fc=random.choice(
                    colors), ec='black', lw=1, ls='--', fill=True, zorder=3, alpha=alpha)
            else:
                pp = mpatches.Circle(center, radius=radius, fc=random.choice(
                    colors), ec='black', lw=2, fill=True, zorder=3, alpha=alpha)
        else:
            if dash:
                pp = mpatches.Circle(
                    center, radius=radius, ec='black', lw=1, ls='--', fill=False, zorder=3)
            else:
                pp = mpatches.Circle(center, radius=radius,
                                     ec='black', lw=2, fill=False, zorder=3)
    ax.add_patch(pp)

# 타원


def drawEllipse(ax, center, width, height, fill=False, alpha=1, dash=False, position=None):
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
            pp = mpatches.Arc(center, width=width, height=height, angle=0,
                              theta1=theta1, theta2=theta2, ec='black', lw=1, ls='--', zorder=3)
        else:
            pp = mpatches.Arc(center, width=width, height=height, angle=0,
                              theta1=theta1, theta2=theta2, ec='black', lw=2, zorder=3)
    else:
        if fill:
            if dash:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, fc=random.choice(
                    colors), ec='black', lw=1, ls='--', fill=True, zorder=3, alpha=alpha)
            else:
                pp = mpatches.Ellipse(center, width=width, height=height, angle=0, fc=random.choice(
                    colors), ec='black', lw=2, fill=True, zorder=3, alpha=alpha)
        else:
            if dash:
                pp = mpatches.Ellipse(center, width=width, height=height,
                                      angle=0, ec='black', lw=1, ls='--', fill=False, zorder=3)
            else:
                pp = mpatches.Ellipse(
                    center, width=width, height=height, angle=0, ec='black', lw=2, fill=False, zorder=3)

    ax.add_patch(pp)

# 문자


def drawText(ax, text='', x=0, y=0):
    l = len(str(text))
    plt.text(x-l, y, text, fontsize=10, zorder=3)


def drawText_(ax, text='', xy=(0, 0)):
    if len(xy) > 2:
        raise Exception("too many inputs for xy")
    l = len(str(text))
    x, y = xy
    plt.text(x-l, y, text, fontsize=10, zorder=3)


# 선분의 길이를 표시하는 bezier 곡선을 그리는 함수
def drawArc(ax, p1, p2, position, text, boxed=False):
    cp = controlPoint(p1, p2, position)
    d = math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
    l = len(text)
    vert = [
        p1,
        cp,  # 제어점
        p2,
        p1
    ]
    codes = [
        Path.MOVETO,
        Path.CURVE3,
        Path.CURVE3,
        Path.CLOSEPOLY,
    ]

    path = Path(vert, codes)

    pp = mpatches.PathPatch(
        path, fc="none", transform=ax.transData, linestyle="--", zorder=3)
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
            plt.text(cp[0]-2*l, cp[1]+3.5, text, fontsize=10,
                     zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom':
            plt.text(cp[0]-2*l, cp[1]-7.5, text, fontsize=10,
                     zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'left':
            plt.text(cp[0]-2-l*4.5, cp[1]-2, text, fontsize=10,
                     zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'right':
            plt.text(cp[0]+l, cp[1]-2, text, fontsize=10,
                     zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'top_r':
            plt.text(cp[0]+l*0.3, cp[1]+2, text, fontsize=10,
                     zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'top_l':
            plt.text(cp[0]+1-l*5, cp[1]+2, text, fontsize=10,
                     zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_r':
            plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5, text, fontsize=10,
                     zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5, text, fontsize=10,
                     zorder=3, bbox=dict(ec='black', fc='white'))
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
        else:
            raise Exception('no matching position')

# 직선 화살표 그리는 함수(dy==0)


def drawArrow(ax, start_p=tuple, end_p=tuple, colors=False):
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
        if dy < 0:
            new_dy = (abs(dy) - head_length)*-1
        else:
            new_dy = dy - head_length
    elif dy == 0:
        if dx < 0:
            new_dx = (abs(dx) - head_length)*-1
        else:
            new_dx = dx - head_length
    else:
        raise Exception("not a stright line")

    ax.arrow(x1, y1, new_dx, new_dy, width=h)

# 직선 양면 화살표 그리는 함수(dy==0)


def drawDoubleArrow(ax, start_p=tuple, end_p=tuple, text='', colors=False):
    def controlPoint(p1, p2, type):
        d = math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
        #d = 2
        # 지나는 점 (p1, p2의 중점)
        mp = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

        if (p2[0]-p1[0]) == 0:
            if type == 'left' or type == 'top':
                cp = (mp[0]-0.2*d, mp[1])
            else:
                cp = (mp[0]+0.2*d, mp[1])

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
            cp = (x, y)

        return cp

    def drawArrow(ax, start_p=tuple, end_p=tuple, colors=False):
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
            if dy < 0:
                new_dy = (abs(dy) - head_length)*-1
            else:
                new_dy = dy - head_length
        elif dy == 0:
            if dx < 0:
                new_dx = (abs(dx) - head_length)*-1
            else:
                new_dx = dx - head_length
        else:
            raise Exception("not a stright line")

        ax.arrow(x1, y1, new_dx, new_dy, width=h)
    l = len(text)*7+2
    dx = end_p[0]-start_p[0]
    dy = end_p[1]-start_p[1]
    if dx == 0:
        middle_p = (((start_p[0]+end_p[0])/2), ((start_p[1]+end_p[1])/2))
        middle_p1 = (((start_p[0]+end_p[0])/2), ((start_p[1]+end_p[1])/2)+l/2)
        middle_p2 = (((start_p[0]+end_p[0])/2), ((start_p[1]+end_p[1])/2)-l/2)
    elif dy == 0:
        middle_p = (((start_p[0]+end_p[0])/2), ((start_p[1]+end_p[1])/2))
        middle_p1 = (((start_p[0]+end_p[0])/2-l/2), ((start_p[1]+end_p[1])/2))
        middle_p2 = (((start_p[0]+end_p[0])/2+l/2), ((start_p[1]+end_p[1])/2))
    else:
        raise Exception('not a stright line')
    if l == 0:
        drawArrow(ax, middle_p, end_p)
        drawArrow(ax, middle_p, start_p)
    else:
        drawArrow(ax, middle_p2, end_p)
        cp = controlPoint(middle_p1, middle_p2, 'left')
        plt.text(cp[0]-l*0.425, middle_p[1]-2, text, fontsize=10, zorder=3)
        drawArrow(ax, middle_p1, start_p)


# 정다각형 그리는 함수
def drawRegular(ax, center, n, radius, fill=False, alpha=1, dash=False):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    if fill:
        if dash:
            pp = mpatches.RegularPolygon(xy=center, fc=random.choice(
                colors), fill=True, lw=1, ls='--', zorder=3, alpha=alpha)
        else:
            pp = mpatches.RegularPolygon(xy=center, fc=random.choice(
                colors), fill=True, lw=2, zorder=3, alpha=alpha)
    else:
        if dash:
            pp = mpatches.RegularPolygon(
                xy=center, ec='black', fill=False, lw=1, ls='--', zorder=3)
        else:
            pp = mpatches.RegularPolygon(
                xy=center, ec='black', fill=False, lw=2, zorder=3)

    ax.add_patch(pp)

# 막대 그래프


def drawBar(ax, xvalue, yvalue, xlabel='', ylabel=''):
    colors = []
    for i in mcolors.CSS4_COLORS:
        colors.append(i)

    width = 0.35

    x = np.arange(len(xvalue))
    ax.bar(x=x-width/3, height=yvalue[0],
           width=width, color=random.choice(colors))
    ax.bar(x=width/3, height=yvalue[1],
           width=width, color=random.choice(colors))
    ax.bar(x=x+width/3, height=yvalue[2],
           width=width, color=random.choice(colors))
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
            cp = (mp[0]-0.2*d, mp[1])
        else:
            cp = (mp[0]+0.2*d, mp[1])

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
        cp = (x, y)

    return cp


def line_equation(p1, p2, x):
    y = ((p2[1]-p1[1])/(p2[0]-p1[0])) * (x-p1[0]) + p1[1]

    return y


#plt.rcParams['text.usetex'] = True
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf8')


#font_name = font_manager.FontProperties(fname='C:/WINDOWS/FONTS/MALGUN.TTF').get_name()
#rc('font', family=font_name)  # For Windows
#plt.rc('font', size = 20)  # For Windows

def new_p_polygon(n=3,scale=100,move_x=0,move_y=0):
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
    random_angle = random.randint(-30,30)
    length = int(scale/2)
    random_length = random.randint(round(scale/10)*-1,round(scale/10))
    polygon = [(0,0)]
    for i in range(n-1):
        if random.randint(0,1):
            temp_p = new_p_angle(angle,length,temp_p)
        else:
            random_angle = random.randint(-30,30)
            random_length = random.randint(round(scale/10)*-1,round(scale/10))
            temp_p = new_p_angle(angle+random_angle,length+random_length,temp_p)
        polygon.append(temp_p)
        polygon = rotate_p(polygon,180-angle)
        temp_p = (rotate_p([temp_p],180-angle))[0]
    polygon = move_to_center(polygon)
    polygon = move_p(polygon,move_x,move_y)
    return polygon
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
answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤",
    5: "⑥",
    6: "⑦",
    7: "⑧",
    8: "⑨",
    9: "⑩",
    10: "⑪",
    11: "⑫",
    12: "⑬",
    13: "⑭",
    14: "⑮"
}
clock_ori_img_dict_list = [
    {'file_name' : "tellingtimes_and_patterns125_0100.png", 'time' : '0100', 'hour' : 1, 'minute' : 0, 'str' : "$$수식$$1$$/수식$$시"},
    {'file_name' : "tellingtimes_and_patterns125_0200.png", 'time' : '0200', 'hour' : 2, 'minute' : 0, 'str' : "$$수식$$2$$/수식$$시"},
    {'file_name' : "tellingtimes_and_patterns125_0300.png", 'time' : '0300', 'hour' : 3, 'minute' : 0, 'str' : "$$수식$$3$$/수식$$시"},
    {'file_name' : "tellingtimes_and_patterns125_0400.png", 'time' : '0400', 'hour' : 4, 'minute' : 0, 'str' : "$$수식$$4$$/수식$$시"},
    {'file_name' : "tellingtimes_and_patterns125_0500.png", 'time' : '0500', 'hour' : 5, 'minute' : 0, 'str' : "$$수식$$5$$/수식$$시"},
    {'file_name' : "tellingtimes_and_patterns125_0600.png", 'time' : '0600', 'hour' : 6, 'minute' : 0, 'str' : "$$수식$$6$$/수식$$시"},
    {'file_name' : "tellingtimes_and_patterns125_0700.png", 'time' : '0700', 'hour' : 7, 'minute' : 0, 'str' : "$$수식$$7$$/수식$$시"},
    {'file_name' : "tellingtimes_and_patterns125_0800.png", 'time' : '0800', 'hour' : 8, 'minute' : 0, 'str' : "$$수식$$8$$/수식$$시"},
    {'file_name' : "tellingtimes_and_patterns125_0900.png", 'time' : '0900', 'hour' : 9, 'minute': 0, 'str' : "$$수식$$9$$/수식$$시"},
    {'file_name' : "tellingtimes_and_patterns125_1000.png", 'time' : '1000', 'hour' : 10, 'minute' : 0, 'str' : "$$수식$$10$$/수식$$시"},
    {'file_name' : "tellingtimes_and_patterns125_1100.png", 'time' : '1100', 'hour' : 11, 'minute' : 0, 'str' : "$$수식$$11$$/수식$$시"},
    {'file_name' : "tellingtimes_and_patterns125_1200.png", 'time' : '1200', 'hour' : 12, 'minute' : 0, 'str' : "$$수식$$12$$/수식$$시"},
    {'file_name': "tellingtimes_and_patterns125_0130.png", 'time' : '0130', 'hour': 1, 'minute': 30, 'next_hour': 2, 'str' : "$$수식$$1$$/수식$$시 $$수식$$30$$/수식$$분"},
    {'file_name': "tellingtimes_and_patterns125_0230.png", 'time' : '0230', 'hour': 2, 'minute': 30, 'next_hour': 3, 'str' : "$$수식$$2$$/수식$$시 $$수식$$30$$/수식$$분"},
    {'file_name': "tellingtimes_and_patterns125_0330.png", 'time' : '0330', 'hour': 3, 'minute': 30, 'next_hour': 4, 'str' : "$$수식$$3$$/수식$$시 $$수식$$30$$/수식$$분"},
    {'file_name': "tellingtimes_and_patterns125_0430.png", 'time' : '0430', 'hour': 4, 'minute': 30, 'next_hour': 5, 'str' : "$$수식$$4$$/수식$$시 $$수식$$30$$/수식$$분"},
    {'file_name': "tellingtimes_and_patterns125_0530.png", 'time' : '0530', 'hour': 5, 'minute': 30, 'next_hour': 6, 'str' : "$$수식$$5$$/수식$$시 $$수식$$30$$/수식$$분"},
    {'file_name': "tellingtimes_and_patterns125_0630.png", 'time' : '0630', 'hour': 6, 'minute': 30, 'next_hour': 7, 'str' : "$$수식$$6$$/수식$$시 $$수식$$30$$/수식$$분"},
    {'file_name': "tellingtimes_and_patterns125_0730.png", 'time' : '0730', 'hour': 7, 'minute': 30, 'next_hour': 8, 'str' : "$$수식$$7$$/수식$$시 $$수식$$30$$/수식$$분"},
    {'file_name': "tellingtimes_and_patterns125_0830.png", 'time' : '0830', 'hour': 8, 'minute': 30, 'next_hour': 9, 'str' : "$$수식$$8$$/수식$$시 $$수식$$30$$/수식$$분"},
    {'file_name': "tellingtimes_and_patterns125_0930.png", 'time' : '0930', 'hour': 9, 'minute': 30, 'next_hour': 10, 'str' : "$$수식$$9$$/수식$$시 $$수식$$30$$/수식$$분"},
    {'file_name': "tellingtimes_and_patterns125_1030.png", 'time' : '1030', 'hour': 10, 'minute': 30, 'next_hour': 11, 'str' : "$$수식$$10$$수식$$시 $$수식$$30$$/수식$$분"},
    {'file_name': "tellingtimes_and_patterns125_1130.png", 'time' : '1130', 'hour': 11, 'minute': 30, 'next_hour': 12, 'str' : "$$수식$$11$$수식$$시 $$수식$$30$$/수식$$분"},
    {'file_name': "tellingtimes_and_patterns125_1230.png", 'time' : '1230', 'hour': 12, 'minute': 30, 'next_hour': 1, 'str' : "$$수식$$12$$/수식$$시 $$수식$$30$$/수식$$분"},
]
clock_flip_img_dict_list = [
    {'file_name': "tellingtimes_and_patterns125_0100_flip.png", 'time' : '0100', 'hour' : 1, 'minute' : 0},
    {'file_name': "tellingtimes_and_patterns125_0200_flip.png", 'time' : '0200', 'hour' : 2, 'minute' : 0},
    {'file_name': "tellingtimes_and_patterns125_0300_flip.png", 'time': '0300', 'hour': 3, 'minute': 0},
    {'file_name': "tellingtimes_and_patterns125_0400_flip.png", 'time' : '0400', 'hour' : 4, 'minute' : 0},
    {'file_name': "tellingtimes_and_patterns125_0500_flip.png", 'time' : '0500', 'hour' : 5, 'minute' : 0},
    {'file_name': "tellingtimes_and_patterns125_0600_flip.png", 'time' : '0600', 'hour' : 6, 'minute' : 0},
    {'file_name': "tellingtimes_and_patterns125_0700_flip.png", 'time' : '0700', 'hour' : 7, 'minute' : 0},
    {'file_name': "tellingtimes_and_patterns125_0800_flip.png", 'time' : '0800', 'hour' : 8, 'minute' : 0},
    {'file_name': "tellingtimes_and_patterns125_0900_flip.png", 'time' : '0900', 'hour' : 9, 'minute': 0},
    {'file_name': "tellingtimes_and_patterns125_1000_flip.png", 'time' : '1000', 'hour' : 10, 'minute' : 0},
    {'file_name': "tellingtimes_and_patterns125_1100_flip.png", 'time' : '1100', 'hour' : 11, 'minute' : 0},
    {'file_name': "tellingtimes_and_patterns125_1200_flip.png", 'time' : '1200', 'hour' : 12, 'minute' : 0},
    {'file_name': "tellingtimes_and_patterns125_0130_flip.png", 'time' : '0130', 'hour': 1, 'minute': 30},
    {'file_name': "tellingtimes_and_patterns125_0230_flip.png", 'time' : '0230', 'hour': 2, 'minute': 30},
    {'file_name': "tellingtimes_and_patterns125_0330_flip.png", 'time' : '0330', 'hour': 3, 'minute': 30},
    {'file_name': "tellingtimes_and_patterns125_0430_flip.png", 'time' : '0430', 'hour': 4, 'minute': 30},
    {'file_name': "tellingtimes_and_patterns125_0530_flip.png", 'time' : '0530', 'hour': 5, 'minute': 30},
    {'file_name': "tellingtimes_and_patterns125_0630_flip.png", 'time' : '0630', 'hour': 6, 'minute': 30},
    {'file_name': "tellingtimes_and_patterns125_0730_flip.png", 'time' : '0730', 'hour': 7, 'minute': 30},
    {'file_name': "tellingtimes_and_patterns125_0830_flip.png", 'time' : '0830', 'hour': 8, 'minute': 30},
    {'file_name': "tellingtimes_and_patterns125_0930_flip.png", 'time' : '0930', 'hour': 9, 'minute': 30},
    {'file_name': "tellingtimes_and_patterns125_1030_flip.png", 'time' : '1030', 'hour': 10, 'minute': 30},
    {'file_name': "tellingtimes_and_patterns125_1130_flip.png", 'time' : '1130', 'hour': 11, 'minute': 30},
    {'file_name': "tellingtimes_and_patterns125_1230_flip.png", 'time' : '1230', 'hour': 12, 'minute': 30},
]
name_list_base = ["이준", "서준", "하준", "도윤", "이안", "유준", "하윤", "지안", "아윤", "서윤", "아린"]
name_list_no_base = ["시우", "지호", "은우", "선우" , "서아", "이서", "지아", "시아", "지유"]
action_list = ["공원에서 놀았습니다.", "밥을 먹었습니다.", "간식을 먹었습니다.", "영어 학원에 갔습니다.", "숙제를 했습니다.",
               "티비를 봤습니다.", "친구와 놀았습니다.", "게임을 했습니다.", "심부름을 했습니다.", "수학 학원에 갔습니다."]
pattern_list = [['a', 'b'], ['a', 'b', 'b'], ['a', 'a', 'b'], ['a', 'a', 'b', 'b'], ['a', 'b', 'c'], ['a','b', 'c'], ['a', 'b', 'a', 'c']]
fig_list = ['■', '▲', '●']

# 1-2-5-03 / 중 / 이해력
def timeandrule125_Stem_001():
    plt.rc('font', family='NanumGothic')
    hour_hand = random.randint(1, 12)
    minute_hand = 12

    scale = 200
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    dir = PATH
    img = mpimg.imread(dir + "tellingtimes_and_patterns125_empty.png")
    img_width, img_height = img.shape[0], img.shape[1]
    img_max = max(img_width, img_height)

    if img_max <= 340:
        img_zoom = round(340/img_max)
    elif img_max > 340:
        img_zoom = (340/img_max)*10
        img_zoom = math.floor(img_zoom)/10
    else:
        img_zoom = 1

    imageBox = OffsetImage(img, zoom=1*img_zoom)
    ab = AnnotationBbox(imageBox, (0, 0), frameon=False)
    ax.add_artist(ab)

    if hour_hand in [1, 3, 6, 7, 8, 10, 11]:
        josa = "을"
    elif hour_hand in [2, 4, 5, 9, 12]:
        josa = "를"

    stem = "시곗바늘을 그려 시각을 써 보시오. \n"
    stem += f"$$표$$ 짧은바늘 → $$수식$${hour_hand}$$/수식$$ \n 큰 바늘 → $$수식$${minute_hand}$$/수식$$ $$/표$$".format(hour_hand = hour_hand, minute_hand=minute_hand)
    answer = "(정답)\n$$수식$${hour_hand}$$/수식$$시\n".format(hour_hand=hour_hand)
    comment = f"(해설)\n짧은 바늘이 $$수식$${hour_hand}$$/수식$${josa} 가리키고, 긴 바늘이 $$수식$$12$$/수식$$를 가리키므로 $$수식$${hour_hand}$$/수식$$시 입니다.".format(
        minute_hand=minute_hand, josa=josa)
    svg = saveSvg()

    return stem, answer, comment, svg

# 1-2-5-04 / 중 / 문제해결력
def timeandrule125_Stem_002():
    plt.rc('font', family='NanumGothic')
    scale = 200
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)

    time_list = list(range(1, 5))
    time_list.extend(list(range(9, 11)))

    first_time = random.choice(time_list)
    second_time = first_time + 2

    event_list = ["동물원 도착", "사자 구경", "호랑이 구경", "코끼리 구경", "간식 시간", "놀이기구 탑승"]
    first_event, second_event = random.sample(event_list, 2)

    r = random.randint(0, 1)
    if r == 0:
        answer_event = first_event
        answer_time = first_time
    else:
        answer_event = second_event
        answer_time = second_time

    for clock in clock_ori_img_dict_list:
        if clock['hour'] == answer_time and clock['minute'] == 0:
            file_name = clock['file_name']

    dir = PATH

    file = dir + file_name
    img = mpimg.imread(file)
    img_width, img_height = img.shape[0], img.shape[1]
    img_max = max(img_width, img_height)

    if img_max <= 340:
        img_zoom = round(340/img_max)
    elif img_max > 340:
        img_zoom = (340/img_max)*10
        img_zoom = math.floor(img_zoom)/10
    else:
        img_zoom = 1

    imageBox = OffsetImage(img, zoom=1*img_zoom)
    ab = AnnotationBbox(imageBox, (0, 0), frameon=False)
    ax.add_artist(ab)


    stem = "시계는 지금 시각을 나타낸 것입니다. 계획대로 하였으면 지금 무엇을 하고 있는지 써 보세요.\n" \
           "$$표$$ {first_event} → $$수식$${first_time}$$/수식$$시 \n {second_event} → $$수식$${second_time}$$/수식$$시 $$/표$$"\
            .format(first_event = first_event, first_time = first_time, second_event = second_event, second_time = second_time)
    answer = "(정답)\n {answer_event} \n".format(answer_event = answer_event)
    comment = "(해설)\n짧은 바늘이 $$수식$${answer_time}$$/수식$$이고, 긴 바늘이 $$수식$$12$$/수식$$를 가리키므로 지금 시각은 $$수식$${answer_time}$$/수식$$시입니다. \n" \
              "따라서 $$수식$${answer_time}$$/수식$$시에는 {answer_event}을 하고 있습니다. "\
        .format(answer_time = answer_time, answer_event = answer_event)
    svg = saveSvg()

    return stem, answer, comment, svg

# 1-2-5-05 / 상 / 추론력
def timeandrule125_Stem_003():
    plt.rc('font', family='NanumGothic')
    scale = 200
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)

    clock_ontime = list()
    for clock in clock_flip_img_dict_list:
        if clock["minute"] == 0:
            clock_ontime.append(clock)

    clock = random.choice(clock_ontime)

    if clock["hour"] == 12:
        answer_hour = 1
    else:
        answer_hour = clock["hour"]+1
    dir = PATH
    file = dir + clock["file_name"]
    img = mpimg.imread(file)
    img_width, img_height = img.shape[0], img.shape[1]
    img_max = max(img_width, img_height)

    if img_max <= 340:
        img_zoom = round(340/img_max)
    elif img_max > 340:
        img_zoom = (340/img_max)*10
        img_zoom = math.floor(img_zoom)/10
    else:
        img_zoom = 1

    imageBox = OffsetImage(img, zoom=1*img_zoom)
    ab = AnnotationBbox(imageBox, (0, 0), frameon=False)
    ax.add_artist(ab)

    stem = "거울에 비춰 본 시계입니다. 시계가 나타내는 시각에서 긴바늘이 한 바퀴 움직일 때 시각을 써 보세요.\n"
    answer = "(정답)\n $$수식$${answer_hour}$$/수식$$시\n".format(answer_hour = answer_hour)
    comment = "(해설)\n" \
              "시계의 짧은바늘이 $$수식$${clock_hour}$$/수식$$을 가리키고, 긴바늘이 $$수식$$12$$/수식$$를 가리키므로 지금 시각은 $$수식$${clock_hour}$$/수식$$시입니다.\n" \
              "따라서 긴바늘이 한 바퀴 움직일 때 짧은바늘은 숫자 $$수식$$1$$/수식$$칸을 움직이므로 $$수식$${answer_hour}$$/수식$$시입니다."\
        .format(clock_hour = clock["hour"], answer_hour = answer_hour)
    svg = saveSvg()

    return stem, answer, comment, svg

# 1-2-5-07 / 상 / 추론력
def timeandrule125_Stem_004():
    plt.rc('font', family='NanumGothic')
    time1, time2 = random.sample(range(1, 12), 2)
    time3 = 12

    exam_list = [time1, time2, time3]
    random.shuffle(exam_list)

    exam1, exam2, exam3 = exam_list[0], exam_list[1], exam_list[2]
    for i, exam in enumerate(exam_list):
        if exam == 12:
            if i == 0:
                answer_sign = "㉠"
            elif i == 1:
                answer_sign = "㉡"
            elif i == 2:
                answer_sign = "㉢"

    stem = "시계의 짧은바늘과 긴바늘이 같은 숫자를 가리킬 때의 시각을 찾아 기호를 써 보세요.\n"
    stem += f"$$표$$ ㉠ $$수식$${exam1}$$/수식$$시  ㉡ $$수식$${exam2}$$/수식$$시  ㉢ $$수식$${exam3}$$/수식$$시$$/표$$"

    answer = f"(정답)\n {answer_sign}\n"
    comment = "(해설)\n" \
              "각각의 시각에 짧은바늘과 긴바늘이 가리키는 숫자를 알아보면\n" \
              "㉠ $$수식$${exam1}$$/수식$$시 → 짧은바늘 : $$수식$${exam1}$$/수식$$, 긴 바늘 : $$수식$$12$$/수식$$\n" \
              "㉡ $$수식$${exam2}$$/수식$$시 → 짧은바늘 : $$수식$${exam2}$$/수식$$, 긴 바늘 : $$수식$$12$$/수식$$\n" \
              "㉢ $$수식$${exam3}$$/수식$$시 → 짧은바늘 : $$수식$${exam3}$$/수식$$, 긴 바늘 : $$수식$$12$$/수식$$\n"\
        .format(exam1 = exam1, exam2 = exam2, exam3 = exam3)

    return stem, answer, comment

# 1-2-5-08 / 중 / 이해력
def timeandrule125_Stem_005():
    plt.rc('font', family='NanumGothic')
    scale = 200
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)

    clock_half_hour = list()
    for clock in clock_ori_img_dict_list:
        if clock["minute"] == 30:
            clock_half_hour.append(clock)

    clock = random.choice(clock_half_hour)
    dir = PATH
    file = dir + clock["file_name"]
    img = mpimg.imread(file)
    img_width, img_height = img.shape[0], img.shape[1]
    img_max = max(img_width, img_height)

    if img_max <= 340:
        img_zoom = round(340/img_max)
    elif img_max > 340:
        img_zoom = (340/img_max)*10
        img_zoom = math.floor(img_zoom)/10
    else:
        img_zoom = 1

    imageBox = OffsetImage(img, zoom=1*img_zoom)
    ab = AnnotationBbox(imageBox, (0, 0), frameon=False)
    ax.add_artist(ab)

    stem = "시각을 써 보세요.\n"
    answer = "(정답)\n $$수식$${answer_hour}$$/수식$$시 $$수식$${answer_minute}$$/수식$$분\n".format(answer_hour = clock["hour"], answer_minute = clock["minute"])
    comment = "(해설)\n" \
              "짧은 바늘이 $$수식$${answer_hour}$$/수식$$와 $$수식$${next_hour}$$수식$$사이에 있고, 긴 바늘이 $$수식$$6$$/수식$$을 가리키므로 $$수식$${answer_hour}$$/수식$$시 $$수식$${answer_minute}$$/수식$$분 입니다. "\
        .format(answer_hour = clock["hour"], next_hour = clock["next_hour"], answer_minute = clock["minute"])
    svg = saveSvg()

    return stem, answer, comment, svg

# 1-2-5-10 / 중 / 추론력
def timeandrule125_Stem_006():
    plt.rc('font', family='NanumGothic')
    exam1, exam2 = random.sample(range(1, 12), 2)
    exam3, exam4 = random.sample(range(1, 12), 2)

    exam_list = [exam1, exam2, exam3, exam4]
    random.shuffle(exam_list)
    exam1, exam2, exam3, exam4 = exam_list[0], exam_list[1], exam_list[2], exam_list[3]
    exam1 = f"$$수식$${exam1}$$/수식$$시"
    exam2 = f"$$수식$${exam2}$$/수식$$시"
    exam3 = f"$$수식$${exam3}$$/수식$$시"
    exam4 = f"$$수식$${exam4}$$/수식$$시"

    answer_sign = [1, 1, 0, 0]
    random.shuffle(answer_sign)
    sign1, sign2 = "", ""
    for i, sign in enumerate(answer_sign):
        if sign == 1:
            if i == 0:
                exam1 += " $$수식$$30$$/수식$$분"
                sign1 = "㉠"
                answer1 = exam1
            elif i == 1:
                exam2 += " $$수식$$30$$/수식$$분"
                if sign1 == "":
                    sign1 = "㉡"
                    answer1 = exam1
                else:
                    sign2 = "㉡"
                    answer2 = exam2
            elif i == 2:
                exam3 += " $$수식$$30$$/수식$$분"
                if sign1 == "":
                    sign1 = "㉢"
                    answer1 = exam3
                else:
                    sign2 = "㉢"
                    answer2 = exam3
            elif i == 3:
                exam4 += " $$수식$$30$$/수식$$분"
                if sign1 == "":
                    sign1 = "㉣"
                    answer1 = exam4
                else:
                    sign2 = "㉣"
                    answer2 = exam4

    stem = f"다음 중 시계의 긴 바늘이 $$수식$$6$$/수식$$을 가리키는 시각을 모두 찾아 기호를 써 보세요.\n$$표$$ ㉠ {exam1}       ㉡ {exam2}\n㉢ {exam3}      ㉣ {exam4}\n$$/표$$"

    answer = f"(정답)\n {sign1}, {sign2}\n"
    comment = "(해설)\n" \
              "시계의 긴 바늘이 $$수식$$6$$/수식$$을 가리킬 때 시각은 몇 시 $$수식$$30$$/수식$$분을 나타냅니다.\n" \
              "따라서 긴 바늘이 $$수식$$6$$/수식$$을 가리키는 시각은 {sign1} {answer1}, {sign2} {answer2} 입니다." \
        .format(sign1 = sign1, answer1 = answer1, sign2 = sign2, answer2 = answer2)

    return stem, answer, comment

# 1-2-5-11 / 중상 / 이해력
def timeandrule125_Stem_007():
    plt.rc('font', family='NanumGothic')
    scale = 200
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2, (5, 2.5))

    clock_half_hour = list()
    for clock in clock_ori_img_dict_list:
        if clock["minute"] == 30:
            clock_half_hour.append(clock)

    clock1, clock2 = random.sample(clock_half_hour, 2)
    if clock1["hour"] > clock2["hour"]:
        clock1, clock2 = clock2, clock1

    clock1["position"] = (-100, 0)
    clock2["position"] = (100, 0)
    dir = PATH

    for clock in [clock1, clock2]:
        img = mpimg.imread(dir+clock['file_name'])
        width, height = img.shape[0], img.shape[1]
        max_size = max(width, height)

        if max_size <= 110:
            zoom = int(110/max_size)
        elif max_size > 110:
            zoom = (110/max_size)*10
            zoom = math.floor(zoom)/10
        else:
            zoom = 1

        imageBox = OffsetImage(img, zoom=1*zoom)
        ab = AnnotationBbox(imageBox, clock["position"], frameon=False)
        ax.add_artist(ab)

    drawText(ax, "출발 시각", -130, 190)
    drawText(ax, "도착 시각", 70, 190)

    boxblank = "$$수식$$BOX{　　　　　}$$/수식$$"
    
    stem = "버스가 출발한 시각과 도착한 시각을 각각 써 보세요.\n출발 시각 : {boxblank}\n\n도착 시각 : {boxblank}".format(boxblank=boxblank)
    answer = "(정답)\n " \
             "$$수식$${clock1_hour}$$/수식$$시 $$수식$${clock1_minute}$$/수식$$분,\n" \
             "$$수식$${clock2_hour}$$/수식$$시 $$수식$${clock2_minute}$$/수식$$분"\
        .format(clock1_hour = clock1["hour"], clock1_minute=clock1["minute"], clock2_hour = clock2["hour"], clock2_minute=clock2["minute"])
    comment = "(해설)\n" \
              "출발 시각 : 짧은 바늘이 $$수식$${clock1_hour}$$/수식$$와 $$수식$${clock1_next}$$/수식$$사이에 있고, 긴 바늘이 $$수식$$6$$/수식$$을 가리키므로 $$수식$${clock1_hour}$$/수식$$시 $$수식$${clock1_minute}$$/수식$$분 입니다.\n" \
              "도착 시각 : 짧은 바늘이 $$수식$${clock2_hour}$$/수식$$와 $$수식$${clock2_next}$$/수식$$사이에 있고, 긴 바늘이 $$수식$$6$$/수식$$을 가리키므로 $$수식$${clock2_hour}$$/수식$$시 $$수식$${clock2_minute}$$/수식$$분 입니다.\n"\
        .format(clock1_hour = clock1["hour"], clock1_next = clock1["next_hour"], clock1_minute = clock1["minute"],
                clock2_hour = clock2["hour"], clock2_next = clock2["next_hour"], clock2_minute = clock2["minute"])
    svg = saveSvg()

    return stem, answer, comment, svg

# 1-2-5-14 / 중상 / 문제해결력
def timeandrule125_Stem_008():
    
    passed_hour = random.randint(1, 4)
    clock_list = list()
    for clock in clock_ori_img_dict_list:
        if clock["hour"] < 12 - passed_hour:
            clock_list.append(clock)
    clock = random.choice(clock_list)

    if clock["minute"] == 0:
        comment1 = "$$수식$${stem_hour}$$/수식$$시".format(stem_hour=clock["hour"] + passed_hour)
        for i in range(passed_hour):
            comment1 += " → $$수식$${stem_hour}$$/수식$$시".format(
                stem_hour=clock["hour"] + passed_hour - i - 1)

        stem = "시계의 긴 바늘이 $$수식$${passed_hour}$$/수식$$바퀴 움직였을 때의 시각이 $$수식$${stem_hour}$$/수식$$시 이었습니다. 처음 시각을 구해보세요. \n" \
            .format(passed_hour=passed_hour, stem_hour=clock["hour"] + passed_hour)
        answer = "(정답)\n$$수식$${clock_hour}$$/수식$$시".format(clock_hour=clock["hour"])
        comment = "(해설)\n" \
                  "처음 시각은 $$수식$${stem_hour}$$/수식$$시에서 긴 바늘이 $$수식$${passed_hour}$$/수식$$바퀴 움직이기 전의 시각입니다.\n" \
                  "{comment1}\n" \
                  "따라서 처음 시각은 $$수식$${clock_hour}$$/수식$$시 입니다. " \
            .format(stem_hour=clock["hour"] + passed_hour, passed_hour=passed_hour,
                    comment1 = comment1,
                    clock_hour=clock["hour"])
    else:
        comment1 = "$$수식$${stem_hour}$$/수식$$시 $$수식$${stem_minute}$$/수식$$분".format(stem_hour = clock["hour"]+passed_hour, stem_minute = clock["minute"])
        for i in range(passed_hour):
            comment1 += " → $$수식$${stem_hour}$$/수식$$시 $$수식$${stem_minute}$$/수식$$분".format(stem_hour = clock["hour"]+passed_hour-i-1, stem_minute = clock["minute"])

        stem = "시계의 긴 바늘이 $$수식$${passed_hour}$$/수식$$바퀴 움직였을 때의 시각이 $$수식$${stem_hour}$$/수식$$시 $$수식$${stem_minute}$$/수식$$분이었습니다. 처음 시각을 구해보세요. \n"\
            .format(passed_hour = passed_hour, stem_hour = clock["hour"]+passed_hour, stem_minute = clock["minute"])
        answer = "(정답)\n$$수식$${clock_hour}$$/수식$$시 $$수식$${clock_minute}$$/수식$$분".format(clock_hour=clock["hour"], clock_minute=clock["minute"])
        comment = "(해설)\n" \
                  "처음 시각은 $$수식$${stem_hour}$$/수식$$사 $$수식$${stem_minute}$$/수식$$에서 긴 바늘이 $$수식$${passed_hour}$$/수식$$바퀴 움직이기 전의 시각입니다.\n" \
                  "{comment1}\n" \
                  "따라서 처음 시각은 $$수식$${clock_hour}$$/수식$$시 $$수식$${clock_minute}$$/수식$$분 입니다. "\
            .format(stem_hour = clock["hour"]+passed_hour, stem_minute = clock["minute"], passed_hour = passed_hour,
                    comment1=comment1,
                    clock_hour = clock["hour"], clock_minute = clock["minute"])

    return stem, answer, comment 

# 1-2-5-15 / 상 / 추론력
def timeandrule125_Stem_009():

    clock1 = random.randint(5, 9)
    clock2 = clock1 + 2

    r = random.randint(0, 1)
    if r == 0:
        answer_long = 6
        answer_clock = "$$수식$${answer_hour}$$/수식$$시 $$수식$$30$$/수식$$분".format(answer_hour = clock1+1)
        comment1 = f"시계의 긴 바늘이 $$수식$$6$$/수식$$을 가리킬 때의 시각은 몇 시 $$수식$$30$$/수식$$분 입니다. 저녁 $$수식$${clock1}$$/수식$$시 $$수식$$30$$/수식$$분과 저녁 $$수식$${clock2}$$/수식$$시 사이의 시각이므로 {answer_clock}입니다."
    else:
        answer_long = 12
        answer_clock = "$$수식$${answer_hour}$$/수식$$시".format(answer_hour = clock1+1)
        comment1 = f"시계의 긴 바늘이 $$수식$$12$$/수식$$을 가리킬 때의 시각은 몇 시 입니다. 저녁 $$수식$${clock1}$$/수식$$시 $$수식$$30$$/수식$$분과 저녁 $$수식$${clock2}$$/수식$$시 사이의 시각이므로 {answer_clock}입니다."

    stem = "지금 설명하는 시각을 써 보세요.\n" \
           "$$표$$지금 시각은 저녁 $$수식$${clock1}$$/수식$$시 $$수식$$30$$/수식$$분과 저녁 $$수식$${clock2}$$/수식$$시 사이입니다. 시계의 긴 바늘이 $$수식$${answer_long}$$/수식$$를 가리키고 있습니다.$$/표$$"\
        .format(clock1 = clock1, clock2 = clock2, answer_long = answer_long)
    answer = "(정답)\n{answer_clock}".format(answer_clock=answer_clock)
    comment = "(해설)\n"
    comment += comment1

    return stem, answer, comment

# 1-2-5-16 / 상 / 문제해결력
def timeandrule125_Stem_010():
    plt.rc('font', family='NanumGothic')
    scale = 200
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)

    if random.randint(0, 1) == 0:
        student = random.choice(name_list_base)
        josa1 = "이네"
    else:
        student = random.choice(name_list_no_base)
        josa1 = "네"

    start_time_list = list()
    end_time_list = list()
    exam_time_list = list()
    answer_time_list = list()

    for clock in clock_ori_img_dict_list:
        if clock["hour"] in [2, 3, 4]:
            start_time_list.append(clock)
        if clock["hour"] in [7, 8, 9]:
            end_time_list.append(clock)

    start_time = random.choice(start_time_list)
    end_time = random.choice(end_time_list)


    for clock in clock_ori_img_dict_list:
        if clock["hour"] >= start_time["hour"]+1 and clock["hour"] < end_time["hour"]-1:
            exam_time_list.append(clock)
        elif clock["hour"] < start_time["hour"] or clock["hour"] > end_time["hour"]:
            answer_time_list.append(clock)

    exam1, exam2 = random.sample(exam_time_list, 2)
    answer_exam = random.choice(answer_time_list)

    exam_list = [exam1, exam2, answer_exam]
    random.shuffle(exam_list)
    clock1, clock2, clock3 = exam_list[0], exam_list[1], exam_list[2]
    answer_sign = ""

    for i, clock in enumerate(exam_list):
        if clock == answer_exam:
            if i == 0:
                answer_sign = "가"
            elif i == 1 :
                answer_sign = "나"
            elif i == 2 :
                answer_sign = "다"

    clock1["position"] = (-170, 0)
    clock2["position"] = (0, 0)
    clock3["position"] = (170, 0)
    dir = PATH

    for clock in exam_list:
        img = mpimg.imread(dir+clock['file_name'])
        width, height = img.shape[0], img.shape[1]
        max_size = max(width, height)

        if max_size <= 90:
            zoom = int(90/max_size)
        elif max_size > 90:
            zoom = (90/max_size)*10
            zoom = math.floor(zoom)/10
        else:
            zoom = 1

        imageBox = OffsetImage(img, zoom=1*zoom)
        ab = AnnotationBbox(imageBox, clock["position"], frameon=False)
        ax.add_artist(ab)

    drawText(ax, "가", -175, -100)
    drawText(ax, "나", -5, -100)
    drawText(ax, "다", 165, -100)

    stem = "{student}{josa1} 가족은 오후 {start_time_str}에 출발하여 저녁 {end_time_str}에 할머니 댁에 도착하였습니다. " \
           "{student}{josa1} 가족이 집에서 할머니 댁에 가는 동안의 시각이 될 수 없는 것을 찾아 기호를 써 보세요.\n" \
           .format(student = student, josa1 = josa1, start_time_str = start_time['str'], end_time_str = end_time['str'])
    answer = "(정답)\n{answer_sign}".format(answer_sign = answer_sign)
    comment = "(해설)\n" \
              "가 : {clock1_str}, 나 : {clock2_str}, 다 : {clock3_str}\n" \
              "{start_time_str} 부터 {end_time_str} 사이의 시간이 아닌 것은 {answer_sign}. {answer_str}입니다."\
        .format(clock1_str = clock1['str'], clock2_str = clock2['str'], clock3_str = clock3['str'], start_time_str = start_time['str'], end_time_str = end_time['str'], answer_sign = answer_sign, answer_str = answer_exam['str'])
    svg = saveSvg()

    return stem, answer, comment, svg

# 1-2-5-17 / 중 / 이해력
def timeandrule125_Stem_011():

    pattern = random.choice(pattern_list)
    pattern_len = len(pattern)
    pattern_str = ""

    c = list()
    for p in pattern:
        if p not in c:
            c.append(p)

    if len(c) == 2:
        fig1 = fig_list[0]
        fig2 = fig_list[1]
        stem_list = f"① {fig1}\n② {fig2}"
    elif len(c) == 3:
        fig1 = fig_list[0]
        fig2 = fig_list[1]
        fig3 = fig_list[2]
        stem_list = f"① {fig1}\n② {fig2}\n③ {fig3}"

    for i in pattern:
        if i == 'a':
            pattern_str += fig1 + "  "
        elif i == 'b':
            pattern_str += fig2 + "  "
        elif i == 'c':
            pattern_str += fig3 + "  "
    pattern_str = pattern_str[:-2]
    order = random.randint(8, 11)
    pattern_re = list()
    for i in range(order//pattern_len+1):
        pattern_re.extend(pattern)
    stem_str = ""

    for i in range(order):
        if pattern_re[i] == 'a':
            stem_str += fig1+ "  "
        elif pattern_re[i] == 'b':
            stem_str += fig2+ "  "
        elif pattern_re[i] == 'c':
            stem_str += fig3+ "  "
    stem_str = stem_str[:-2]
    result = order

    if pattern_re[result] == 'a':
        result_fig = fig1
        answer_num = '①'
    elif pattern_re[result] == 'b':
        result_fig = fig2
        answer_num = '②'
    elif pattern_re[result] == 'c':
        result_fig = fig3
        answer_num = '③'



    stem = "다음 도형을 규칙에 따라 늘어놓았을 때, 처음에서 $$수식$${order}$$/수식$$번째 놓을 도형은 무엇인가요?\n".format(order=order+1)
    stem += f"$$표$$ {stem_str} $$/표$$\n{stem_list}"
    answer = "(정답)\n{answer_num}".format(answer_num=answer_num)
    comment = "(해설)\n"
    comment += "{pattern_str} 도형이 반복되므로 $$수식$${order}$$/수식$$번째 도형은 {figure} 입니다."\
        .format(pattern_str= pattern_str, order = order+1, figure = result_fig)

    return stem, answer, comment

# 1-2-5-18 / 중 / 이해력
def timeandrule125_Stem_012():
    name_list = name_list_base
    name_list.extend(name_list_no_base)
    student1, student2, student3 = random.sample(name_list, 3)
    collect_list = ["봄이 가면 여름이 오지.", "여름이 가면 가을이 오지", "가을이 가면 겨울이 오지", "겨울이 가면 봄이 오지",
                    "봄 다음에는 여름이야.", "여름 다음에는 가을이야.", "가을 다음에는 겨울이야.", "겨울 다음에는 다시 봄이야."]
    wrong_list = ["여름이 지나면 봄이 와", "가을이 지나면 여름이 와", "겨울이 지나면 가을이 와"]
    con1, con2 = random.sample(collect_list, 2)
    wrong_con = random.choice(wrong_list)

    con_list = [con1, con2, wrong_con]
    random.shuffle(con_list)
    con1, con2, con3 = con_list[0], con_list[1], con_list[2]

    comment1, comment2, comment3 = con1, con2, con3
    comment1 += " (O)"
    comment2 += " (O)"
    comment3 += " (O)"

    for i, con in enumerate(con_list):
        if con == wrong_con:
            if i == 0:
                answer_student = student1
                comment1 = comment1.replace("(O)", "(X)")
            elif i == 1:
                answer_student = student2
                comment2 = comment2.replace("(O)", "(X)")
            elif i == 2:
                answer_student = student3
                comment3 = comment3.replace("(O)", "(X)")

    stem = "우리나라 계절의 규칙을 틀리게 말한 어린이는 누구인가요?\n"
    stem += f"$$표$$" \
            f"[{student1}] {con1}\n" \
            f"[{student2}] {con2}\n" \
            f"[{student3}] {con3}$$/표$$"
    answer = "(정답)\n{answer_student}".format(answer_student = answer_student)
    comment = "(해설)\n"
    comment += "우리나라 계절의 규칙 : 봄 - 여름 - 가을 - 겨울이 반복됩니다.\n"
    comment += student1 + " : " + comment1 + "\n"
    comment += student2 + " : " + comment2 + "\n"
    comment += student3 + " : " + comment3 + "\n"
    comment += "따라서 계절의 규칙을 다르게 말한 어린이는 {answer_student}입니다. ".format(answer_student = answer_student)

    return stem, answer, comment

# 1-2-5-23 / 중상 / 추론력
def timeandrule125_Stem_013():
    plt.rc('font', family='NanumGothic')
    scale = 200
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2, (5, 2))

    p = random.randint(1,6)
    if p == 1:
        pattern = "abcabcab"
        count1, count2, count3 = 5, 0, 2
    elif p == 2:
        pattern = "acbacbac"
        count1, count2, count3 = 5, 2, 0
    elif p == 3:
        pattern = "bacbacba"
        count1, count2, count3 = 0, 5, 2
    elif p == 4:
        pattern = "bcabcabc"
        count1, count2, count3 = 0, 2, 5
    elif p == 5:
        pattern = "cabcabca"
        count1, count2, count3 = 2, 5, 0
    elif p == 6:
        pattern = "cbacbacb"
        count1, count2, count3 = 2, 0, 5
    dir = PATH
    x = -180
    y = 0
    fig_dict_list = list()
    for i, fig in enumerate(pattern):
        fig_dict = dict()
        fig_dict["position"] = (x, y)
        x += 50

        if i == 5 or i == 6:
            fig_dict["fig"] = dir + \
                "tellingtimes_and_patterns212_stem013_blank.png"
        else:
            if pattern[i] == "a":
                fig_dict["fig"] = dir + "tellingtimes_and_patterns212_stem013_paper.png"
            elif pattern[i] == "b":
                fig_dict["fig"] = dir + \
                    "tellingtimes_and_patterns212_stem013_rock.png"
            elif pattern[i] == "c":
                fig_dict["fig"] = dir + \
                    "tellingtimes_and_patterns212_stem013_scissors.png"
        fig_dict_list.append(fig_dict)

    for p in fig_dict_list:
        img = mpimg.imread(p['fig'])
        width, height = img.shape[0], img.shape[1]
        max_size = max(width, height)

        if max_size <= 45:
            zoom = int(45 / max_size)
        elif max_size > 45:
            zoom = (45 / max_size) * 10
            zoom = math.floor(zoom) / 10
        else:
            zoom = 1

        imageBox = OffsetImage(img, zoom=1 * zoom)
        ab = AnnotationBbox(imageBox, p["position"], frameon=False)
        ax.add_artist(ab)

    stem = "규칙에 따라 빈칸에 들어갈 펼친 손가락은 모두 몇 개일까요?\n"
    answer = "(정답)\n$$수식$${answer_count}$$/수식$$개".format(answer_count = count3 + count1)
    comment = "(해설)\n" \
              "펼친 손가락이 $$수식$${count1}$$/수식$$개 - $$수식$${count2}$$/수식$$개 - $$수식$${count3}$$/수식$$개가 반복되는 규칙이므로 빈칸에는 차례대로 펼친 손가락 $$수식$${count3}$$/수식$$개, 펼친 손가락 $$수식$${count1}$$/수식$$개 그림이 들어갑니다.\n" \
              "따라서 빈칸에 들어갈 펼친 손가락은 모두 $$수식$${count3} + {count1} = {answer_count}$$/수식$$(개)입니다."\
        .format(count1 = count1, count2 = count2, count3 = count3, answer_count = count3 + count1)

    svg = saveSvg()

    return stem, answer, comment, svg

# 1-2-5-25 / 중상 / 추론력
def timeandrule125_Stem_014():

    num1, num2 = random.sample(list(range(1, 10)), 2)

    box1 = "Box{`````%s`````}" % num1
    box2 = "Box{`````%s`````}" % num2
    box3 = "Box{`````%s`````}" % num1
    box4 = "Box{`````%s`````}" % "①"
    box4_comment = "Box{`````%s`````}" % num2
    box5 = "Box{`````%s`````}" % "②"
    box5_comment = "Box{`````%s`````}" % num1
    box6 = "Box{`````%s`````}" % num2


    stem = "규칙에 따라 빈칸에 알맞은 수를 써넣으세요.\n"
    stem += f"$$수식$${box1}$$/수식$$$$수식$${box2}$$/수식$$$$수식$${box3}$$/수식$$$$수식$${box4}$$/수식$$$$수식$${box5}$$/수식$$$$수식$${box6}$$/수식$$"

    answer = "(정답)\n$$수식$${num2}$$/수식$$, $$수식$${num1}$$/수식$$".format(num1 = num1, num2 = num2)
    comment = "(해설)\n"
    comment += f"{num1}, {num2} 반복되는 규칙입니다. \n"
    comment += f"$$수식$${box1}$$/수식$$$$수식$${box2}$$/수식$$$$수식$${box3}$$/수식$$$$수식$${box4_comment}$$/수식$$$$수식$${box5_comment}$$/수식$$$$수식$${box6}$$/수식$$"

    return stem, answer, comment

# 1-2-5-28 / 상 / 추론력
def timeandrule125_Stem_015():

    start_num = random.randint(71, 89)
    common_difference = random.randint(2, 5)

    num1 = start_num
    num2 = num1 - common_difference
    num3 = num2 - common_difference
    num4 = num3 - common_difference
    num5 = num4 - common_difference
    num6 = num5 - common_difference

    box1 = "Box{`````%s`````}" % num1
    box2_blank = "Box{`````%s`````}" % "　　"
    box3 = "Box{`````%s`````}" % num3
    box4_blank = "Box{`````%s`````}" % "　　"
    box5 = "Box{`````%s`````}" % num5
    box6 = "Box{`````%s`````}" % "●"

    stem = "규칙에 따라 ●에 알맞은 수를 구해 보세요.\n"
    stem += f"$$수식$${box1}$$/수식$$$$수식$${box2_blank}$$/수식$$$$수식$${box3}$$/수식$$$$수식$${box4_blank}$$/수식$$$$수식$${box5}$$/수식$$$$수식$${box6}$$/수식$$"

    answer = "(정답)\n$$수식$${num6}$$/수식$$".format(num6 = num6)
    comment = "(해설)\n"
    comment += f"$$수식$${num1}$$/수식$$부터 시작하여 몇씩 $$수식$$2$$/수식$$번 작아지면 $$수식$${num3}$$/수식$$이 되므로 $$수식$${common_difference}$$/수식$$씩 작아지는 규칙입니다.\n"
    comment += f"따라서 $$수식$${num1}$$/수식$$부터 시작하여 $$수식$${common_difference}$$/수식$$씩 작아지는 수를 배열하면 $$수식$${num1} - {num2} - {num3} - {num4} - {num5} - {num6}$$/수식$$ 이므로\n●에 알맞은 수는 $$수식$${num6}$$/수식$$입니다."

    return stem, answer, comment

# 1-2-5-30 / 상 / 추론력
def timeandrule125_Stem_016():

    start_num = random.randint(45, 55)
    common_difference = random.randint(2, 4)
    n = random.randint(8, 10)

    num1 = start_num
    num2 = num1 - common_difference
    num3 = num2 - common_difference
    num4 = num3 - common_difference

    answer_num = num1 - common_difference*(n-1)

    ap = ""
    temp_num = start_num
    for i in range(n):
        ap += str(temp_num-common_difference) + " - "
        temp_num = temp_num - common_difference
    ap = ap[:-3]
    stem = f"규칙에 따라 늘어놓은 수 배열에서 $$수식$${answer_num}$$/수식$$은 몇 번째에 놓이는지 구해 보세요.\n"
    stem += f"$$표$$ $$수식$${num1} - {num2} - {num3} - {num4}$$/수식$$ ... $$/표$$"

    answer = "(정답)\n$$수식$${n}$$/수식$$번째".format(n = n)
    comment = "(해설)\n"
    comment += f"$$수식$${num1}$$/수식$$부터 시작하여 $$수식$${common_difference}$$/수식$$씩 작아집니다. \n"
    comment += f"따라서 $$수식$${ap}$$/수식$$ 이므로 $$수식$${answer_num}$$/수식$$은 $$수식$${n}$$/수식$$번째에 놓입니다."

    return stem, answer, comment
