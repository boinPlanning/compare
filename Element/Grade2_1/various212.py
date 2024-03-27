from asyncio.log import logger
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
cube_dict_list = [
    {'file_name': "various_shapes212_cube_001.png", 'total': 4, 'first': 3, 'second': 1, 'third' : 0},
    {'file_name': "various_shapes212_cube_002.png", 'total': 5, 'first': 3, 'second': 2, 'third': 0},
    {'file_name': "various_shapes212_cube_003.png", 'total': 5, 'first': 4, 'second': 1, 'third': 0},
    {'file_name': "various_shapes212_cube_004.png", 'total': 4, 'first': 4, 'second': 0, 'third': 0},
    {'file_name': "various_shapes212_cube_005.png", 'total': 7, 'first': 6, 'second': 1, 'third': 0},
    {'file_name': "various_shapes212_cube_006.png", 'total': 7, 'first': 5, 'second': 2, 'third': 0},
    {'file_name': "various_shapes212_cube_007.png", 'total': 7, 'first': 5, 'second': 2, 'third': 0},
    {'file_name': "various_shapes212_cube_008.png", 'total': 7, 'first': 4, 'second': 3, 'third': 0},
    {'file_name': "various_shapes212_cube_009.png", 'total': 9, 'first': 5, 'second': 3, 'third': 1},
    {'file_name': "various_shapes212_cube_010.png", 'total': 8, 'first': 5, 'second': 3, 'third': 0},
    {'file_name': "various_shapes212_cube_011.png", 'total': 5, 'first': 3, 'second': 1, 'third': 1},
    {'file_name': "various_shapes212_cube_012.png", 'total': 6, 'first': 4, 'second': 2, 'third': 0},
    {'file_name': "various_shapes212_cube_013.png", 'total': 3, 'first': 2, 'second': 1, 'third': 0},
    {'file_name': "various_shapes212_cube_014.png", 'total': 7, 'first': 4, 'second': 2, 'third': 1},
]
name_list_base = ["이준", "서준", "하준", "도윤", "이안", "유준", "하윤", "지안", "아윤", "서윤", "아린"]
name_list_no_base = ["시우", "지호", "은우", "선우" , "서아", "이서", "지아", "시아", "지유"]

# 2-1-2-02 / 중 / 이해력
def various212_Stem_001():
    explanation1 = ["크기가 달라도 모양은 같습니다.", "크기가 다르면 모양도 다릅니다."]
    explanation2 = ["곧은 선이 없습니다. ", "곧은 선으로 둘러쌓여 있습니다."]
    explanation3 = ["뾰족한 부분이 없습니다.", "뾰족한 부분이 있습니다."]
    explanation4 = ["길쭉하거나 찌그러진 곳 없이 어느 쪽에서 보아도 모양이 항상 똑같습니다.", "길쭉하거나 찌그러진 곳 있어 보는 쪽에 따라서  모양이 다릅니다. "]

    while True:
        answer_count = 0
        answer_list = list()
        for i in range(4):
            r = random.randint(0, 1)
            if i == 0:
                if r == 1:
                    con1 = explanation1[0]
                else:
                    con1 = explanation1[1]
                    answer_count += 1
                answer_list.append(r)
            elif i == 1:
                if r == 1:
                    con2 = explanation2[0]
                else:
                    con2 = explanation2[1]
                    answer_count += 1
                answer_list.append(r)
            elif i == 2:
                if r == 1:
                    con3 = explanation3[0]
                else:
                    con3 = explanation3[1]
                    answer_count += 1
                answer_list.append(r)
            elif i == 3:
                if r == 1:
                    con4 = explanation4[0]
                else:
                    con4 = explanation4[1]
                    answer_count += 1
                answer_list.append(r)
        if answer_count != 0 and answer_list != 4:
            break

    stem = "원에 대한 설명으로 바르지 않은 것은 모두 몇 개 인가요? \n"
    stem += "$$표$$ ㉠{con1}\n㉡{con2}\n㉢{con3}\n㉣{con4}$$/표$$\n".format(con1=con1, con2=con2, con3=con3, con4=con4)

    answer = "(정답)\n$$수식$${answer}$$/수식$$개\n".format(answer=answer_count)

    wrong_explanation = ""
    wrong_flag  = ""
    for i in range(4):
        if i == 0 and answer_list[i] ==  0:
            wrong_explanation += "㉠" + explanation1[0] + "\n"
            wrong_flag += "㉠ "
        elif i == 1 and answer_list[i] ==  0:
            wrong_explanation += "㉡" + explanation2[0] + "\n"
            wrong_flag += "㉡ "
        elif i == 2 and answer_list[i] ==  0:
            wrong_explanation += "㉢" + explanation3[0] + "\n"
            wrong_flag += "㉢ "
        elif i == 3 and answer_list[i] ==  0:
            wrong_explanation += "㉣" + explanation4[0] + "\n"
            wrong_flag += "㉣ "

    comment = "(해설)\n" \
              "{wrong_explanation}\n" \
              "따라서 설명이 바르지 않은 것은 {wrong_flag}의 $$수식$${answer}$$/수식$$개 입니다.".format(wrong_explanation=wrong_explanation, wrong_flag = wrong_flag, answer = answer_count )

    return stem, answer, comment

# 2-1-2-04 / 중상 / 문제해결력
def various212_Stem_002():
    
    scale = 200
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]

    answer_count = random.randint(4, 8)
    ax = setChart(dim_2, (answer_count+1, 2))

    radius = 45 #first_circle

    c_x = int(answer_count/2)*50*(-1)
    c_y = 0
    c = (c_x, c_y)

    drawCircle(ax, c, radius)
    for i in range(answer_count-1):
        c_x += radius
        c = (c_x, c_y)
        drawCircle(ax, c, radius)
        
    ax.axis('tight')

    stem = "그림에서 원은 모두 몇개 인가요?"
    answer = "(정답)\n$$수식$${answer}$$/수식$$개\n".format(answer=answer_count)
    comment = "(해설)\n겹쳐져 있는 원을 하나씩 떼어 개수를 셉니다."
    # #plt.show()
    svg = saveSvg()

    return stem, answer, comment, svg

# 2-1-2-06 / 중상 / 문제해결력
def various212_Stem_003():
    
    scale = 80
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)

    p1 = (random.randint(-10, 10),random.randint(30, 50))
    p2 = (random.randint(-70, -50), random.randint(-80, -60))
    p3 = (random.randint(50, 70),random.randint(-75, -50))

    p1_p2 = int(p1[0]+p2[0])/2, int(p1[1]+p2[1])/2
    p2_p3 = int(p2[0]+p3[0])/2, int(p2[1]+p3[1])/2
    p3_p1 = int(p3[0]+p1[0])/2, int(p3[1]+p1[1])/2

    t1 = (p1[0]-10, p1[1])
    t2 = (p1_p2[0]-10, p1_p2[1])
    t3 = (p2[0]-10, p2[1])
    t4 = (p2_p3[0], p2_p3[1]-10)
    t5 = (p3[0], p3[1]-10)
    t6 = (p3_p1[0]+10, p3_p1[1])
    # def drawArrow(ax, start_p=tuple, end_p=tuple, colors=False):

    drawText(ax, "㉠", t1[0]+8, t1[1]+5)
    #drawArrow(ax, t1, p1)
    drawText(ax, "㉡", t2[0]-5, t2[1]-1)
    drawArrow(ax, t2, p1_p2)
    drawText(ax, "㉢", t3[0]-2, t3[1]-5)
    #drawArrow(ax, t3, p2)
    drawText(ax, "㉣", t4[0]-2, t4[1]-5)
    drawArrow(ax, t4, p2_p3)
    drawText(ax, "㉤", t5[0]+4, t5[1]+5)
    #drawArrow(ax, t5, p3)
    drawText(ax, "㉥", t6[0]+1, t6[1]-1)
    drawArrow(ax, t6, p3_p1)



    triangle = [p1, p2, p3]
    drawPolygon(ax, triangle)

    stem = "삼각형에서 변과 꼭짓점을 모두 찾아 각각 몇 개씩인지 써 보세요.\n변의 개수 : $$수식$${box}$$/수식$$개, 꼭짓점의 개수 : $$수식$${box}$$/수식$$개"
    box = "box{　　}"
    stem = stem.format(box=box)
    answer = "(정답)\n$$수식$$3$$/수식$$, $$수식$$3$$/수식$$\n"
    comment = "(해설)\n" \
              "변 : 삼각형의 곧은 선 → $$수식$$3$$/수식$$개 → ㉡, ㉣, ㉥\n" \
              "꼭짓점 : 삼각형의 두 곧은 선이 만나는 점 → $$수식$$3$$/수식$$개 → ㉠, ㉢, ㉤\n"
    svg = saveSvg()

    return stem, answer, comment, svg

# 2-1-2-07 / 중 / 이해력
def various212_Stem_004():
    explanation1 = ["곧은 선으로 둘러싸여 있습니다.", "굽은 선으로 둘러싸여 있습니다.", "곧은 선과 굽은 선이 섞여있습니다."]
    explanation2 = ["꼭짓점이 $$수식$$3$$/수식$$개 입니다. ", "꼭짓점이 $$수식$$4$$/수식$$개 입니다. ", "꼭짓점이 $$수식$$2$$/수식$$개 입니다."]
    explanation3 = ["변이 $$수식$$3$$/수식$$개 입니다. ", "변이 $$수식$$2$$/수식$$개 입니다", "변이 $$수식$$4$$/수식$$개 입니다"]
    explanation_list = [explanation1, explanation2, explanation3]
    random.shuffle(explanation_list)

    collect_flag = random.randint(1, 3)
    if collect_flag == 1:
        con1 = explanation_list[0][random.randint(1,2)]
        comment_1 = explanation_list[0][0]
        con2 = explanation_list[1][0]
        con3 = explanation_list[2][0]
    elif collect_flag == 2:
        con2 = explanation_list[1][random.randint(1,2)]
        comment_1 = explanation_list[1][0]
        con1 = explanation_list[0][0]
        con3 = explanation_list[2][0]
    elif collect_flag == 3:
        con3 = explanation_list[2][random.randint(1,2)]
        comment_1 = explanation_list[2][0]
        con1 = explanation_list[0][0]
        con2 = explanation_list[1][0]

    collect = {1:"㉠", 2:"㉡", 3:"㉢"}[collect_flag]

    stem = "삼각형의 설명으로 틀린 것을 찾아 기호를 써 보세요.\n"
    stem += "$$표$$ ㉠{con1}\n㉡{con2}\n㉢{con3}\n$$/표$$\n".format(con1=con1, con2=con2, con3=con3)
    answer = "(정답)\n{collect}".format(collect = collect)
    comment = "(해설)\n"
    comment += comment_1

    return stem, answer, comment

# 2-1-2-08 / 중상 / 문제해결력
def various212_Stem_005():
    
    #setting
    scale = 150
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax1 = setChart(dim_2)
    ax2 = setChart(dim_2)

    r1 = (-120,120)
    r2 = (-120, -120)
    r3 = (120, -120)
    r4 = (120, 120)

    # 사각형 그리기
    drawPolygon(ax1, [r1, r2, r3, r4])
    drawPolygon(ax2, [r1, r2, r3, r4])

    case = random.randint(1, 4)
    # 한 점이 사각형의 꼭짓점과 같을 때
    if case == 1:
        t1 = (random.randint(-100, 100), 120)
        t2 = (-120, random.randint(-100, 100))
        t3 = (120, -120)

        drawCircle(ax1, t1, 2)
        drawCircle(ax1, t2, 2)
        drawCircle(ax1, t3, 2)
        svg1 = saveSvg()

        drawCircle(ax2, t1, 2)
        drawCircle(ax2, t2, 2)
        drawCircle(ax2, t3, 2)

        drawLine(ax2, [t1, t2])
        drawLine(ax2, [t2, t3])
        drawLine(ax2, [t1, t3])
        svg2 = saveSvg()

        result = 4
    elif case == 2:
        t1 = (random.randint(-100, 100), 120)
        t2 = (120, random.randint(-100, 100))
        t3 = (-120, -120)

        drawCircle(ax1, t1, 2)
        drawCircle(ax1, t2, 2)
        drawCircle(ax1, t3, 2)
        svg1 = saveSvg()

        drawCircle(ax2, t1, 2)
        drawCircle(ax2, t2, 2)
        drawCircle(ax2, t3, 2)

        drawLine(ax2, [t1, t2])
        drawLine(ax2, [t2, t3])
        drawLine(ax2, [t1, t3])
        svg2 = saveSvg()

        result = 4

    # 세 점 모두 선 위에 있을 때
    elif case == 3:
        t1 = (random.randint(-100, 100), 120)
        t2 = (-120, random.randint(-100, 100))
        t3 = (120,  random.randint(-100, 100))

        drawCircle(ax1, t1, 2)
        drawCircle(ax1, t2, 2)
        drawCircle(ax1, t3, 2)
        svg1 = saveSvg()

        drawCircle(ax2, t1, 2)
        drawCircle(ax2, t2, 2)
        drawCircle(ax2, t3, 2)

        drawLine(ax2, [t1, t2])
        drawLine(ax2, [t2, t3])
        drawLine(ax2, [t1, t3])
        svg2 = saveSvg()

        result = 3
    elif case == 4:
        t1 = (random.randint(-100, 100), 120)
        t2 = (120,  random.randint(-100, 100))
        t3 = (-120, random.randint(-100, 100))

        drawCircle(ax1, t1, 2)
        drawCircle(ax1, t2, 2)
        drawCircle(ax1, t3, 2)
        svg1 = saveSvg()

        drawCircle(ax2, t1, 2)
        drawCircle(ax2, t2, 2)
        drawCircle(ax2, t3, 2)

        drawLine(ax2, [t1, t2])
        drawLine(ax2, [t2, t3])
        drawLine(ax2, [t1, t3])
        svg2 = saveSvg()

        result = 3


    stem = "색종이에 세 점을 꼭짓점으로 하는 삼각형을 그리려고 합니다. 그린 삼각형의 변을 따라 자르면 삼각형이 몇 개 만들어질까요?"
    answer = "(정답)\n$$수식$${0}$$/수식$$개".format(result)

    comment = "(해설)\n" \
              "세 점을 꼭짓점으로 하는 삼각형을 그리면 다음과 같습니다. \n" \
              "삼각형은 변과 꼭짓점이 각각 개인 도형이므로 삼각형의 변을 따라 자르면 삼각형이 $$수식$${0}$$/수식$$개 생깁니다.\n".format(result)

    svg = svg2 #[svg1, svg2]
    #plt.show()
    return stem, answer, comment, svg

# 2-1-2-11 / 중 / 이해력
def various212_Stem_006():
    
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
    polygon = new_p_polygon(4)
    polygon = resize(polygon,90)
    drawPolygon(ax,polygon)
    svg = saveSvg()

    stem = "사각형에서 변의 수와 꼭짓점의 수의 합은 모두 몇 개 인가요?"
    answer = "(정답)\n$$수식$$8$$/수식$$개"
    comment = "(해설)\n사각형은 $$수식$$4$$/수식$$개의 변과 $$수식$$4$$/수식$$개의 꼭짓점으로 이루어져 있습니다.\n"
    comment += "변은 곧은 선을 말하고, 꼭짓점은 두 곧은 선이 만나는 점입니다. "
    #plt.show()

    return stem, answer, comment, svg

# 2-1-2-12 / 중 / 이해력
def various212_Stem_007():
    
    explanation1 = ["변이 $$수식$$4$$/수식$$개 있습니다.", "변이 $$수식$$3$$/수식$$개 있습니다.", "변이 $$수식$$5$$/수식$$개 있습니다 "]
    explanation2 = ["꼭짓점이 $$수식$$2$$/수식$$개 있습니다.", "꼭짓점이 $$수식$$3$$/수식$$개 있습니다.", "꼭짓점이 $$수식$$4$$/수식$$개 있습니다."]
    explanation3 = ["변과 꼭짓점의 합이 $$수식$$7$$/수식$$개 입니다.", "변과 꼭짓점의 합이 $$수식$$8$$/수식$$개 입니다."]
    False_explanation_list = [explanation1, explanation2, explanation3]

    True_explanation = ["곧은 선들로 둘러싸여 있습니다.", "굽은 선이 없습니다. "]

    explanation_list = list()

    for e in random.sample(False_explanation_list, 2):
        explanation_list.append(random.choice(e))

    collect_flag = random.randint(1, 3)
    explanation_list.insert(collect_flag-1, random.choice(True_explanation))

    collect = {1:"㉠", 2:"㉡", 3:"㉢"}[collect_flag]

    stem = "삼각형과 사각형의 공통점을 찾아 기호를 써 보세요.\n"
    stem += "$$표$$ ㉠{con1}\n㉡{con2}\n㉢{con3}\n$$/표$$\n".format(con1=explanation_list[0], con2=explanation_list[1], con3=explanation_list[2])
    answer = "(정답)\n{collect}".format(collect = collect)
    comment = "(해설)\n"\
              "삼각형은 $$수식$$3$$/수식$$개의 곧은 선과 $$수식$$3$$/수식$$개의 꼭짓점으로 이루어져 있습니다. \n"\
              "사각형은 $$수식$$4$$/수식$$개의 곧은 선과 $$수식$$4$$/수식$$개의 꼭짓점으로 이루어져 있습니다. \n" \
              "삼각형과 사각형은 모두 곧은 선으로 둘러싸여 있습니다. "

    return stem, answer, comment

# 2-1-2-16 / 중 / 이해력
def various212_Stem_008():
    
    con_dict_list = [
        {'idx': 1, 'true_con' : "칠교판은 모두 $$수식$$7$$/수식$$개 입니다.", 'false_con' : "칠교판은 모두 $$수식$$6$$/수식$$개 입니다."},
        {'idx': 2, 'true_con': "칠교판 조각 중 사각형 모양은 $$수식$$2$$/수식$$개입니다.", 'false_con': "칠교판 조각 중 사각형 모양은 $$수식$$5$$/수식$$개입니다."},
        {'idx': 3, 'true_con': "칠교판 모양 중 삼각형 모양은 $$수식$$5$$/수식$$개입니다.", 'false_con': "칠교판 모양 중 삼각형 모양은 $$수식$$2$$/수식$$개입니다."},
        {'idx': 4, 'true_con': "칠교판 조각 중 가장 큰 조각은 삼각형 모양입니다.", 'false_con': "칠교판 조각 중 가장 큰 조각은 사각형 모양입니다."},
        {'idx': 5, 'true_con': "삼각형 모양 $$수식$$2$$/수식$$개를 붙여서 사각형 모양을 만들 수 있습니다.", 'false_con': "사각형 모양 $$수식$$2$$/수식$$개를 붙여서 삼각형 모양을 만들 수 있습니다."}
    ]
    random.shuffle(con_dict_list)

    answer_number = random.randint(0, 4)
    answer_con = ""

    con_list = list()
    for i in range(5):
        con_dict = con_dict_list[i]
        if i == answer_number:
            con_list.append(con_dict["false_con"])
            answer_con = con_dict["true_con"]
        else:
            con_list.append(con_dict["true_con"])

    scale = 200
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    dir = PATH
    img = mpimg.imread(dir + "various_shape212_stem008_img.png")
    img_width, img_height = img.shape[0], img.shape[1]
    max_size = max(img_width, img_height)
    if max_size <= 350:
        zoom_ratio = int(350/max_size)

    imageBox = OffsetImage(img, zoom=1*zoom_ratio)
    ab = AnnotationBbox(imageBox, (0, 0), frameon=False)
    ax.add_artist(ab)
    
    plt.imshow(img, origin='upper',
               extent=[-100*zoom_ratio, 100*zoom_ratio, -100*zoom_ratio, -100*zoom_ratio], aspect='auto')
    plt.axis("off")

    stem = "칠교판에 대한 설명으로 잘못된 것을 골라 보세요.\n\n"\
           "① {con1}\n" \
           "② {con2}\n" \
           "③ {con3}\n" \
           "④ {con4}\n" \
           "⑤ {con5}\n".format(con1 = con_list[0], con2 = con_list[1], con3 = con_list[2], con4 = con_list[3], con5 = con_list[4])

    answer = "(정답)\n{answer_number}".format(answer_number = answer_dict[answer_number])
    comment = "(해설)\n" \
              "{answer_number} {answer_con}".format(answer_number=answer_dict[answer_number], answer_con=answer_con)
    svg = saveSvg()
    plt.clf()
    
    return stem, answer, comment, svg

# 2-1-2-20 / 중 / 이해력
def various212_Stem_009():
    
    con_dict_list = [
        {'stem' : "오각형의 변의 수는 {idx}개입니다", 'answer' : 5, 'comment' : "오각형의 변의 수는 $$수식$$5$$/수식$$개"},
        {'stem': "오각형의 꼭짓점은 {idx}개입니다.", 'answer': 5, 'comment' : "오각형의 꼭짓점은 $$수식$$5$$/수식$$개"},
        {'stem': "육각형의 변의 수는 {idx}개입니다.", 'answer': 6, 'comment' : "육각형의 변의 수는 $$수식$$6$$/수식$$개"},
        {'stem': "육각형의 꼭짓점은 {idx}개입니다.", 'answer': 6, 'comment' : "육각형의 꼭짓점은 $$수식$$6$$/수식$$개"}]

    con1, con2 = random.sample(con_dict_list, 2)

    con1_stem = con1['stem'].format(idx = '㉠')
    con1_comment = con1['comment']

    con2_stem = con2['stem'].format(idx='㉡')
    con2_comment = con2['comment']

    result = con1['answer'] + con2['answer']

    stem = "㉠과 ㉡의 합을 구하세요\n\n"
    stem += "$$표$$ ㉠ {con1_stem}\n㉡ {con2_stem}\n$$/표$$\n".format(con1_stem=con1_stem, con2_stem=con2_stem)
    answer = "(정답)\n" \
             "$$수식$${result}$$/수식$$".format(result = result)
    comment = "(해설)\n" \
              "{con1_comment}이고, {con2_comment}입니다.\n" \
              "따라서 $$수식$${con1_answer}+{con2_answer}={result}$$/수식$$(개)입니다."\
                .format(con1_comment=con1_comment, con2_comment=con2_comment,
                        con1_answer = con1['answer'], con2_answer = con2['answer'], result = result)

    return stem, answer, comment

# 2-1-2-21 / 중 / 이해력
def various212_Stem_010():
    
    con_dict_list = [
        {'true_con' : "꼭짓점이 $$수식$$5$$/수식$$개입니다.", 'false_con' : "꼭짓점이 $$수식$$6$$/수식$$개입니다."},
        {'true_con': "크기는 다양합니다.", 'false_con': "크기가 항상 같습니다."},
        {'true_con': "곧은 선 $$수식$$5$$/수식$$개로 둘러싸여 있습니다.", 'false_con': "곧은 선 $$수식$$6$$/수식$$개로 둘러싸여 있습니다."},
        {'true_con': "변이 $$수식$$5$$/수식$$개입니다.", 'false_con': "변이 $$수식$$6$$/수식$$개입니다."},
        {'true_con': "사각형보다 변이 $$수식$$1$$/수식$$개 더 많습니다.",
            'false_con': "사각형보다 변이 2개 더 많습니다."}
    ]
    random.shuffle(con_dict_list)

    answer_number = random.randint(0, 4)
    answer_con = ""

    con_list = list()
    for i in range(5):
        con_dict = con_dict_list[i]
        if i == answer_number:
            con_list.append(con_dict["false_con"])
            answer_con = con_dict["true_con"]
        else:
            con_list.append(con_dict["true_con"])

    stem = "오각형에 대한 설명으로 옳지 않은 것은 어느 것일까요?\n\n"\
           "① {con1}\n" \
           "② {con2}\n" \
           "③ {con3}\n" \
           "④ {con4}\n" \
           "⑤ {con5}\n".format(con1 = con_list[0], con2 = con_list[1], con3 = con_list[2], con4 = con_list[3], con5 = con_list[4])

    answer = "(정답)\n{answer_number}".format(answer_number = answer_dict[answer_number])
    comment = "(해설)\n" \
              "{answer_number} {answer_con}".format(answer_number=answer_dict[answer_number], answer_con=answer_con)

    svg = ""

    return stem, answer, comment, svg

# 2-1-2-22 / 상 / 문제해결력
def various212_Stem_011():
    #setting
    scale = 200
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2, (5, 1))

    case = random.randint(0, 1)
    if case == 0:
        feature = "꼭짓점"
    else:
        feature = "변"

    poly_list = [0, 3, 4, 5, 6]
    poly_list = random.sample(poly_list, 4)
    result = 0
    for i in range(len(poly_list)):
        x = -100+70*i
        result += poly_list[i]
        if poly_list[i] == 0:
            drawCircle(ax, (x,0), 25)
        elif poly_list[i] == 3:
            polygon = new_p_regular(3, scale=100, move_x=x, move_y=-10)
            drawPolygon(ax, polygon)
        elif poly_list[i] == 4:
            polygon = new_p_regular(4, scale=80, move_x=x)
            drawPolygon(ax, polygon)
        elif poly_list[i] == 5:
            polygon = new_p_regular(5, scale=60, move_x=x)
            drawPolygon(ax, polygon)
        elif poly_list[i] == 6:
            polygon = new_p_regular(6, scale=50, move_x=x)
            drawPolygon(ax, polygon)
            
    ax.axis('tight')

    stem = "다음 네 도형의 {feature}의 수의 합은 모두 몇 개 일까요??\n".format(feature = feature)


    answer = "(정답)\n $$수식$${result}$$/수식$$개".format(result= result)
    comment = "(해설)\n" \
              "왼쪽에서부터 {feature}의 수를 구하면 $$수식$${poly1}$$/수식$$개, $$수식$${poly2}$$/수식$$개, $$수식$${poly3}$$/수식$$개, $$수식$${poly4}$$/수식$$개입니다.\n" \
              "→ {feature}의 수의 합 $$수식$$= {poly1}+{poly2}+{poly3}+{poly4} = {result}$$/수식$$(개)"\
                .format(feature = feature, poly1=poly_list[0], poly2=poly_list[1], poly3=poly_list[2], poly4=poly_list[3], result = result)

    svg = saveSvg()

    return stem, answer, comment, svg
def new_p_regular(n=3, scale=100, move_x=0, move_y=0):
        import random
        def new_p_angle(angle, length, p=[0, 0]):
            angle_radiant = math.radians(angle)
            x = (math.cos(angle_radiant) * length) + p[0]
            y = (math.sin(angle_radiant) * length) + p[1]
            return (x, y)

        def move_to_center(p_list=list, center_index=-1):
            # calculate center point
            x_center = 0
            y_center = 0
            for p in p_list:
                x_center += p[0]
                y_center += p[1]
            x_center /= len(p_list)
            y_center /= len(p_list)
            new_p_list = []
            if center_index == -1:  # center with calculated center point
                x_move = x_center * -1
                y_move = y_center * -1
            else:  # center with center_index
                center_p = p_list[center_index]
                x_move = center_p[0] * -1
                y_move = center_p[1] * -1
            # make new list with new points
            for index in range(len(p_list)):
                if center_index == -1:
                    p = p_list[index]
                    new_p_list.append((p[0] + x_move, p[1] + y_move))
                else:
                    if index == center_index:
                        new_p_list.append((0, 0))
                    else:
                        p = p_list[index]
                        new_p_list.append((p[0] + x_move, p[1] + y_move))
            return new_p_list

        def move_p(p_list=list, x_move=0, y_move=0):
            # center point
            new_p_list = []
            for index in range(len(p_list)):
                p = p_list[index]
                new_p_list.append((p[0] + x_move, p[1] + y_move))
            return new_p_list

        def rotate_p(p_list=list, angle=0):
            def cart2pol(x, y):
                import math
                r = math.sqrt(x ** 2 + y ** 2)
                angle_radians = math.atan2(y, x)
                return (r, angle_radians)

            def pol2cart(r, angle_radians):
                import math
                x = r * math.cos(angle_radians)
                y = r * math.sin(angle_radians)
                return (x, y)

            import math
            for i in range(len(p_list)):
                cart_x = p_list[i][0]
                cart_y = p_list[i][1]
                pol_r, pol_angle_radians = cart2pol(cart_x, cart_y)
                pol_angle_radians += math.radians(angle)
                cart_x, cart_y = pol2cart(pol_r, pol_angle_radians)
                p_list[i] = (cart_x, cart_y)
            return p_list

        temp_p = (0, 0)
        angle = 180 * (n - 2) / n
        length = int(scale / 2)
        polygon = [(0, 0)]
        for i in range(n - 1):
            temp_p = new_p_angle(angle, length, temp_p)
            polygon.append(temp_p)
            polygon = rotate_p(polygon, 180 - angle)
            temp_p = (rotate_p([temp_p], 180 - angle))[0]

        # polygon.reverse()
        polygon = move_to_center(polygon)
        polygon = move_p(polygon, move_x, move_y)
        return polygon

# 2-1-2-25 / 상 / 문제해결력
def various212_Stem_012():
    poly_list = [{'name': "원", 'answer' : 0},
                 {'name': "삼각형", 'answer': 3},
                 {'name': "사각형", 'answer': 4},
                 {'name': "오각형", 'answer': 5},
                 {'name': "육각형", 'answer': 6}]
    poly_list = random.sample(poly_list, 3)
    poly1 = poly_list[0]
    poly1['feature'] = random.choice(["변", "꼭짓점"])
    poly2 = poly_list[1]
    poly2['feature'] = random.choice(["변", "꼭짓점"])
    poly3 = poly_list[2]
    poly3['feature'] = random.choice(["변", "꼭짓점"])

    result = poly1['answer']+poly2['answer']+poly3['answer']
    stem = "{poly1}의 {poly1_feature}은 ■개, {poly2}의 {poly2_feature}은 ●개, {poly3}의 {poly1_feature}은 ★개입니다. ■ + ● + ★의 값을 구해 보세요.\n"\
        .format(poly1 = poly1['name'], poly1_feature = poly1['feature'],
                poly2 = poly2['name'], poly2_feature = poly2['feature'],
                poly3 = poly3['name'], poly3_feature = poly3['feature'])

    answer = "(정답)\n$$수식$${result}$$/수식$$".format(result = result)
    comment = "(해설)\n" \
              "{poly1}의 {poly1_feature}은 $$수식$${poly1_answer}$$/수식$$개, {poly2}의 {poly2_feature}은 $$수식$${poly2_answer}$$/수식$$개, {poly3}의 {poly3_feature}은 $$수식$${poly3_answer}$$/수식$$개입니다.\n" \
              "→ $$수식$$■ + ● + ★ = {poly1_answer} + {poly2_answer} + {poly3_answer} = {result}$$/수식$$\n"\
        .format(poly1 = poly1['name'], poly1_feature = poly1['feature'], poly1_answer = poly1['answer'],
                poly2 = poly2['name'], poly2_feature = poly2['feature'], poly2_answer = poly2['answer'],
                poly3 = poly3['name'], poly3_feature = poly3['feature'], poly3_answer = poly3['answer'],
                result = result)

    return stem, answer, comment

# 2-1-2-26 / 상 / 문제해결력
def various212_Stem_013():
    
    scale = 200
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    dir = PATH
    img = mpimg.imread(dir + "various_shape212_stem013_img.png")
    img_width, img_height = img.shape[0], img.shape[1]
    max_size = max(img_width, img_height)

    if max_size <= 380:
        zoom_ratio = int(380/max_size)
    elif max_size > 380:
        zoom_ratio = (380/max_size)*10
        zoom_ratio = math.floor(zoom_ratio)
        zoom_ratio = (zoom_ratio/10)
    else:
        zoom_ratio = 1

    imageBox = OffsetImage(img, zoom=1*zoom_ratio)
    ab = AnnotationBbox(imageBox, (0, 0), frameon=False)
    ax.add_artist(ab)

    poly_list = [{'name': "원", 'count': 3},
                 {'name': "삼각형", 'count': 4},
                 {'name': "사각형", 'count': 5},
                 {'name': "육각형", 'count': 2}]
    poly1, poly2 = random.sample(poly_list, 2)

    if poly1['count'] < poly2['count']:
        poly1, poly2 = poly2, poly1
    result = poly1['count'] - poly2['count']

    stem = "그림에서 {poly1}의 개수는 {poly2}의 개수보다 몇 개 더 많은가요?\n\n".format(poly1 = poly1['name'], poly2 = poly2['name'])
    answer = "(정답)\n$$수식$${result}$$/수식$$개".format(result = result)
    comment = "(해설)\n" \
              "원 $$수식$$3$$/수식$$개, 삼각형 $$수식$$4$$/수식$$개, 사각형 $$수식$$5$$/수식$$개, 오각형 $$수식$$2$$/수식$$개, 육각형 $$수식$$2$$/수식$$개 입니다. \n" \
              "따라서 {poly1}의 개수는 {poly2}의 개수보다 $$수식$${poly1_count}-{poly2_count} = {result}$$/수식$$(개) 더 많습니다."\
        .format(poly1 = poly1['name'], poly2 = poly2['name'], poly1_count = poly1['count'], poly2_count = poly2['count'], result = result)

    svg = saveSvg()

    return stem, answer, comment, svg

# 2-1-2-27 / 중하 / 이해력
def various212_Stem_014():
    
    scale = 200
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2, (5, 2))

    cube = random.choice(cube_dict_list)
    dir = PATH
    cube_img = mpimg.imread(dir+cube['file_name'])
    cube_img_width, cube_img_height = cube_img.shape[0], cube_img.shape[1]
    cube_img_max = max(cube_img_width, cube_img_height)

    if cube_img_max <= 360:
        zoom = int(360/cube_img_max)
    elif cube_img_max > 380:
        zoom = (380/cube_img_max)*10
        zoom = math.floor(zoom)/10
    else:
        zoom = 1
        
    #imageBox = OffsetImage(cube_img, zoom=1*zoom)
    #ab = AnnotationBbox(imageBox, (0, 0), frameon=False)
    #ax.add_artist(ab)
    
    plt.imshow(cube_img, origin='upper',
               extent=[-200*zoom, 200*zoom, -200*zoom, 200*zoom], aspect='auto')
    plt.axis("off")

    cube_total = cube["total"]
    cube_first, cube_second, cube_third = cube['first'], cube['second'], cube['third']
    comment1 = "$$수식$$1$$/수식$$층 : $$수식$${cube_first}$$/수식$$개".format(cube_first = cube_first)
    comment2 = ""
    comment3 = ""
    comment_4 = "→ (쌓기나무의 수)$$수식$$ = {cube_first}".format(
        cube_first=cube_first)
    if cube_second != 0:
        comment2 = ", $$수식$$2$$/수식$$층 : $$수식$${cube_second}$$/수식$$개".format(cube_second = cube_second)
        comment_4 += " + {cube_second}".format(cube_second = cube_second)
        if cube_third != 0:
            comment3 = ", $$수식$$3$$수식$$층 : $$수식$${cube_third}$$/수식$$개".format(cube_third = cube_third)
            comment_4 += " + {cube_third}".format(
                cube_third=cube_third)
    comment_4 += " = {cube_total}$$/수식$$개".format(cube_total=cube_total)


    stem = "다음과 똑같은 모양으로 쌓으려면 쌓기나무는 모두 몇 개 필요한가요?\n"
    answer = "(정답)\n$$수식$${cube_total}$$/수식$$개".format(cube_total=cube_total)
    comment = "(해설)\n"
    comment += comment1 + comment2 + comment3 + "\n" + comment_4
    svg = saveSvg()
    plt.clf()
    
    return stem, answer, comment, svg

# 2-1-2-29 / 중상 / 문제해결력
def various212_Stem_015():

    scale = 200
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2, (5, 2))

    cube1 = random.choice(cube_dict_list)
    cube_dict_list.remove(cube1)
    cube1_total = cube1["total"]
    cube2_total = cube1_total
    while cube1_total == cube2_total:
        cube2 = random.choice(cube_dict_list)
        cube2_total = cube2["total"]

    dir = PATH

    cube1_img = mpimg.imread(dir+cube1['file_name'])
    cube1_img_width, cube1_img_height = cube1_img.shape[0], cube1_img.shape[1]
    cube1_img_max = max(cube1_img_width, cube1_img_height)

    if cube1_img_max <= 160:
        zoom = int(160/cube1_img_max)
    elif cube1_img_max > 160:
        zoom = (160/cube1_img_max)*10
        zoom = math.floor(zoom)/10
    else:
        zoom = 1

    #imageBox = OffsetImage(cube1_img, zoom=1*zoom)
    #ab = AnnotationBbox(imageBox, (-100, 0), frameon=False)
    #ax.add_artist(ab)

    cube2_img = mpimg.imread(dir+cube2['file_name'])
    cube2_img_width, cube2_img_height = cube2_img.shape[0], cube2_img.shape[1]
    cube2_img_max = max(cube2_img_width, cube2_img_height)

    if cube2_img_max <= 160:
        zoom = int(160/cube2_img_max)
    elif cube2_img_max > 160:
        zoom = (160/cube2_img_max)*10
        zoom = math.floor(zoom)/10
    else:
        zoom = 1
        
    #imageBox = OffsetImage(cube2_img, zoom=1*zoom)
    #ab = AnnotationBbox(imageBox, (100, 0), frameon=False)
    #ax.add_artist(ab)
    
    plt.subplot(1,2,1)
    
    plt.imshow(cube1_img)
    plt.axis("off")
    
    plt.subplot(1,2,2)
    plt.imshow(cube2_img)
    plt.axis("off")

    r = random.randint(1, 4)
    if r == 1:
        student1 = random.choice(name_list_base)
        josa1 = "이와"
        name_list_base.remove(student1)
        student2 = random.choice(name_list_base)
        josa2 = "이는"
        josa3 = "이가"
    elif r == 2:
        student1 = random.choice(name_list_base)
        josa1 = "이와"
        student2 = random.choice(name_list_no_base)
        josa2 = "는"
    elif r == 3:
        student1 = random.choice(name_list_no_base)
        josa1 = "와"
        student2 = random.choice(name_list_base)
        josa2 = "이는"
    elif r == 4:
        student1 = random.choice(name_list_no_base)
        josa1 = "와"
        name_list_no_base.remove(student1)
        student2 = random.choice(name_list_no_base)
        josa2 = "는"
        josa3 = "가"

    if cube1["total"] < cube2["total"]:
        answer_student = student1
        answer_count = cube2["total"] - cube1["total"]
    else:
        answer_student = student2
        answer_count = cube1["total"] - cube2["total"]

    if answer_student in name_list_base:
        josa3 = "이가"
    else:
        josa3 = "가"

    drawText(ax, student1, -200, 0)
    drawText(ax, student2, 150, 0)

    comment1 = "[{student1}] $$수식$$1$$/수식$$층 : $$수식$${cube_first}$$/수식$$개".format(student1=student1, cube_first = cube1["first"])
    comment2 = ""
    comment3 = ""
    comment4 = "→ (쌓기나무의 수) $$수식$$= {cube_first}".format(
        cube_first=cube1["first"])
    if cube1["second"] != 0:
        comment2 = ", $$수식$$2$$/수식$$층 : $$수식$${cube_second}$$/수식$$개".format(cube_second = cube1["second"])
        comment4 += " + {cube_second}".format(cube_second = cube1["second"])
        if cube1["third"] != 0:
            comment3 = ", $$수식$$3$$/수식$$층 : $$수식$${cube_third}$$/수식$$개".format(cube_third = cube1["third"])
            comment4 += " + {cube_third}".format(cube_third=cube1["third"])
    comment4 += " = {cube_total}$$/수식$$개".format(cube_total=cube1["total"])

    comment5 = "[{student2}] $$수식$$1$$/수식$$층 : $$수식$${cube_first}$$/수식$$개".format(student2=student2, cube_first=cube2["first"])
    comment6 = ""
    comment7 = ""
    comment8 = "→ (쌓기나무의 수) $$수식$$= {cube_first}".format(
        cube_first=cube2["first"])
    if cube2["second"] != 0:
        comment6 = ", $$수식$$2$$/수식$$층 : $$수식$${cube_second}$$/수식$$개".format(cube_second=cube2["second"])
    comment8 += " + {cube_second}".format(cube_second=cube2["second"])
    if cube2["third"] != 0:
        comment7 = ", $$수식$$3$$/수식$$층 : $$수식$${cube_third}$$/수식$$개".format(cube_third=cube2["third"])
        comment8 += " + {cube_third}".format(cube_third=cube2["third"])
    comment8 += " = {cube_total}$$/수식$$개".format(cube_total=cube2["total"])

    if cube1["total"] > cube2["total"]:
        comment9 = "$$수식$${cube1_total} > {cube2_total}$$/수식$$이므로 {answer_student}{josa3} $$수식$${cube1_total}-{cube2_total}={answer_count}$$/수식$$개 더 필요합니다."\
            .format(cube1_total=cube1["total"], cube2_total=cube2["total"], answer_student=answer_student, josa3=josa3, answer_count=answer_count)
    else:
        comment9 = "$$수식$${cube1_total} &lt; {cube2_total}$$/수식$$이므로 {answer_student}{josa3} $$수식$${cube2_total} - {cube1_total} = {answer_count}$$/수식$$개 더 필요합니다."\
            .format(cube1_total=cube1["total"], cube2_total=cube2["total"], answer_student=answer_student, josa3=josa3, answer_count=answer_count)

    boxblank = "$$수식$$BOX{　　　}$$/수식$$"
    stem = "{student1}{josa1} {student2}{josa2} 각각 주어진 모양과 똑같은 모양으로 쌓으려고 합니다. 쌓기나무는 누가 몇 개 더 필요한가요?\n"\
        "$$표$${boxblank} (이)가 {boxblank} 개 더 필요합니다.$$/표$$".format(student1=student1, josa1=josa1, student2=student2, josa2=josa2, boxblank=boxblank)
    answer = "(정답)\n{answer_student}, $$수식$${answer_count}$$/수식$$"\
        .format(answer_student=answer_student, answer_count=answer_count, josa3=josa3)
    comment = "(해설)\n"
    comment += comment1 + comment2 + comment3 + "\n" + comment4 + "\n"
    comment += comment5 + comment6 + comment7 + "\n" + comment8 + "\n"
    comment += comment9

    svg = saveSvg()
    plt.clf()
    
    return stem, answer, comment, svg

# 2-1-2-31 / 중 / 이해력
def various212_Stem_016():
    
    scale = 200
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2, (5, 2))

    cube_3_list = list()
    cube_4_list = list()
    cube_5_list = list()
    cube_6_list = list()
    cube_7_list = list()
    cube_8_list = list()
    cube_9_list = list()

    for i in cube_dict_list:
        if i["total"] == 3:
            cube_3_list.append(i)
        elif i["total"] == 4:
            cube_4_list.append(i)
        elif i["total"] == 5:
            cube_5_list.append(i)
        elif i["total"] == 6:
            cube_6_list.append(i)
        elif i["total"] == 7:
            cube_7_list.append(i)
        elif i["total"] == 8:
            cube_8_list.append(i)
        elif i["total"] == 9:
            cube_9_list.append(i)
    r = random.randint(0, 1)
    if r == 0:
        cube1, cube2 = random.sample(cube_5_list,2)
        r1 = random.randint(0, 1)
        if r1 == 0:
            cube3 = random.choice(cube_4_list)
        else:
            cube3 = random.choice(cube_6_list)
    else:
        cube1, cube2 = random.sample(cube_7_list,2)
        r1 = random.randint(0, 1)
        if r1 == 0:
            cube3 = random.choice(cube_6_list)
        else:
            cube3 = random.choice(cube_8_list)

    result = random.randint(1, 3)
    if result == 1:
        cube3["position"] = (-150, 0)
        cube1["position"] = (0, 0)
        cube2["position"] = (150, 0)
        answer_sign = "㉠"

        cube1["sign"] = "㉡"
        cube2["sign"] = "㉢"
        cube3["sign"] = "㉠"

    elif result == 2:
        cube3["position"] = (0, 0)
        cube1["position"] = (-150, 0)
        cube2["position"] = (150, 0)
        answer_sign = "㉡"

        cube1["sign"] = "㉠"
        cube2["sign"] = "㉢"
        cube3["sign"] = "㉡"

    elif result == 3:
        cube3["position"] = (150, 0)
        cube1["position"] = (-150, 0)
        cube2["position"] = (0, 0)
        answer_sign = "㉢"

        cube1["sign"] = "㉠"
        cube2["sign"] = "㉡"
        cube3["sign"] = "㉢"

    dir = PATH

    cube_list = [cube1, cube2, cube3]
    for index, cube in enumerate(cube_list):
        img = mpimg.imread(dir+cube['file_name'])
        width, height = img.shape[0], img.shape[1]
        max_size = max(width, height)

        if max_size <= 120:
            zoom = int(120/max_size)
        elif max_size > 120:
            zoom = (120/max_size)*10
            zoom = math.floor(zoom)/10
        else:
            zoom = 1

        #imageBox = OffsetImage(img, zoom=1*zoom)
        #ab = AnnotationBbox(imageBox, cube["position"], frameon=False)
        #ax.add_artist(ab)

        plt.subplot(1, 3, index+1)
        
        plt.imshow(img)
        plt.axis("off")

    drawText(ax, "㉠", -520, 20)
    drawText(ax, "㉡", -200, 20)
    drawText(ax, "㉢", 120, 20)

    comment1_1 = "{cube_sign} $$수식$$1$$/수식$$층 : $$수식$${cube_first}$$/수식$$개".format(cube_sign=cube1["sign"], cube_first = cube1["first"])
    comment1_2 = ""
    comment1_3 = ""
    comment1_4 = " → $$수식$${cube_first}$$/수식$$".format(
        cube_first=cube1["first"])

    if cube1["second"] != 0:
        comment1_2 = ", $$수식$$2$$/수식$$층 : $$수식$${cube_second}$$/수식$$개".format(cube_second = cube1["second"])
        comment1_4 += " $$수식$$+ {cube_second}$$/수식$$".format(cube_second = cube1["second"])
        if cube1["third"] != 0:
            comment1_3 = ", $$수식$$3$$/수식$$층 : $$수식$${cube_third}$$/수식$$개".format(cube_third = cube1["third"])
            comment1_4 += " $$수식$$+ {cube_third}$$/수식$$".format(
                cube_third=cube1["third"])
    comment1_4 += " $$수식$$= {cube_total}$$/수식$$개".format(
        cube_total=cube1["total"])

    comment2_1 = "{cube_sign} $$수식$$1$$/수식$$층 : $$수식$${cube_first}$$/수식$$개".format(cube_sign=cube2["sign"], cube_first = cube2["first"])
    comment2_2 = ""
    comment2_3 = ""
    comment2_4 = " → $$수식$${cube_first}$$/수식$$".format(cube_first=cube2["first"])

    if cube2["second"] != 0:
        comment2_2 = ", $$수식$$2$$/수식$$층 : $$수식$${cube_second}$$/수식$$개".format(cube_second = cube2["second"])
        comment2_4 += " $$수식$$+ {cube_second}$$/수식$$".format(cube_second = cube2["second"])
        if cube2["third"] != 0:
            comment2_3 = ", $$수식$$3$$/수식$$층 : $$수식$${cube_third}$$/수식$$개".format(cube_third = cube2["third"])
            comment2_4 += " $$수식$$+ {cube_third}$$/수식$$".format(cube_third=cube2["third"])
    comment2_4 += " $$수식$$= {cube_total}$$/수식$$개".format(
        cube_total=cube2["total"])

    comment3_1 = "{cube_sign} $$수식$$1$$/수식$$층 : $$수식$${cube_first}$$/수식$$개".format(
        cube_sign=cube3["sign"], cube_first=cube3["first"])
    comment3_2 = ""
    comment3_3 = ""
    comment3_4 = " → $$수식$${cube_first}$$/수식$$".format(cube_first=cube3["first"])

    if cube3["second"] != 0:
        comment3_2 = ", $$수식$$2$$/수식$$층 : $$수식$${cube_second}$$/수식$$개".format(cube_second = cube3["second"])
        comment3_4 += " $$수식$$+ {cube_second}$$/수식$$".format(cube_second = cube3["second"])
        if cube3["third"] != 0:
            comment3_3 = ", $$수식$$3$$/수식$$층 : $$수식$${cube_third}$$/수식$$개".format(cube_third = cube3["third"])
            comment3_4 += " $$수식$$+ {cube_third}$$/수식$$".format(cube_third=cube3["third"])
    comment3_4 += " $$수식$$= {cube_total}$$/수식$$개".format(
        cube_total=cube3["total"])


    stem = "모양을 만드는 데 사용한 쌓기나무의 수가 다른 하나를 찾아 기호를 써 보세요.\n"
    answer = f"(정답)\n{answer_sign}"
    comment = "(해설)\n"
    if result == 1:
        comment += comment3_1 + comment3_2 + comment3_3 +comment3_4 + "\n"
        comment += comment1_1 + comment1_2 + comment1_3 +comment1_4 + "\n"
        comment += comment2_1 + comment2_2 + comment2_3 +comment2_4
    elif result == 2:
        comment += comment1_1 + comment1_2 + comment1_3 +comment1_4 + "\n"
        comment += comment3_1 + comment3_2 + comment3_3 +comment3_4 + "\n"
        comment += comment2_1 + comment2_2 + comment2_3 +comment2_4
    elif result == 3:
        comment += comment1_1 + comment1_2 + comment1_3 +comment1_4 + "\n"
        comment += comment2_1 + comment2_2 + comment2_3 +comment2_4 + "\n"
        comment += comment3_1 + comment3_2 + comment3_3 +comment3_4

    svg = saveSvg()
    plt.clf()
    
    return stem, answer, comment, svg

# 2-1-2-36 / 중상 / 문제해결력
def various212_Stem_017():
    
    scale = 200
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2, (5, 2))

    cube1, cube2 = random.sample(cube_dict_list, 2)
    cube1["position"] = (-100, 0)
    cube2["position"] = (100, 0)
    dir = PATH
    cube_list = [cube1, cube2]

    for cube in cube_list:
        img = mpimg.imread(dir+cube['file_name'])
        width, height = img.shape[0], img.shape[1]
        max_size = max(width, height)

        if max_size <= 160:
            zoom = int(160/max_size)
        elif max_size > 160:
            zoom = (160/max_size)*10
            zoom = math.floor(zoom)/10
        else:
            zoom = 1

        imageBox = OffsetImage(img, zoom=1*zoom)
        ab = AnnotationBbox(imageBox, cube["position"], frameon=False)
        ax.add_artist(ab)
    add_block = random.randint(1, 4)
    total_block = cube1["total"] + cube2["total"] + add_block

    r = random.randint(0, 1)
    if r == 0:
        student = random.choice(name_list_base)
        josa = "이는"
    else:
        student = random.choice(name_list_no_base)
        josa = "는"

    comment1_1 = "왼쪽 모양은 $$수식$$1$$/수식$$층 : $$수식$${cube_first}$$/수식$$".format(cube_first = cube1["first"])
    comment1_2 = ""
    comment1_3 = ""
    comment1_4 = " → $$수식$${cube_first}".format(cube_first=cube1["first"])
    if cube1["second"] != 0:
        comment1_2 = ", $$수식$$2$$/수식$$층 : $$수식$${cube_second}$$/수식$$개".format(cube_second = cube1["second"])
        comment1_4 += " + {cube_second}".format(cube_second = cube1["second"])
        if cube1["third"] != 0:
            comment1_3 = ", $$수식$$3$$/수식$$층 : $$수식$${cube_third}$$/수식$$개".format(cube_third = cube1["third"])
            comment1_4 += " + {cube_third}".format(cube_third=cube1["third"])
    comment1_4 += " = {cube_total}$$/수식$$개".format(cube_total=cube1["total"])

    comment2_1 = "오른쪽 모양은 $$수식$$1$$/수식$$층 : $$수식$${cube_first}$$/수식$$".format(cube_first = cube2["first"])
    comment2_2 = ""
    comment2_3 = ""
    comment2_4 = " → $$수식$${cube_first}".format(cube_first=cube2["first"])

    if cube2["second"] != 0:
        comment2_2 = ", $$수식$$2$$/수식$$층 : $$수식$${cube_second}$$/수식$$개".format(cube_second = cube2["second"])
        comment2_4 += " + {cube_second}".format(cube_second = cube2["second"])
        if cube2["third"] != 0:
            comment2_3 = ", $$수식$$3$$/수식$$층 : $$수식$${cube_third}$$/수식$$개".format(cube_third = cube2["third"])
            comment2_4 += " + {cube_third}".format(cube_third=cube2["third"])
    comment2_4 += " = {cube_total}$$/수식$$개".format(cube_total=cube2["total"])

    comment3 = f" → (남은 쌓기나무의 수) $$수식$$= {total_block} - {cube1['total']} - {cube2['total']} = {add_block}$$/수식$$개"

    stem = f"{student}{josa} 쌓기나무 $$수식$${total_block}$$/수식$$개를 가지고 있었습니다. 다음 두 모양을 만들고 남은 쌓기나무는 몇 개 인가요?"
    answer = f"(정답)\n$$수식$${add_block}$$/수식$$개"
    comment = "(해설)\n사용한 쌓기나무가 \n"
    comment += comment1_1 + comment1_2 + comment1_3 + comment1_4 + "\n"
    comment += comment2_1 + comment2_2 + comment2_3 + comment2_4 + " 입니다.\n"
    comment += comment3
    svg = saveSvg()
    return stem, answer, comment, svg
