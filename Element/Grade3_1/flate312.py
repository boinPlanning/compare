#from  draw2svg import *
import random
import math
import numpy as np
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib as mpl
import numpy as np
from matplotlib.path import Path
import random
import io
import sys
import math

#plt.rcParams['text.usetex'] = True
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf8')
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf8')

plt.rc('font', family='NanumGothic')

def line_equation(p1, p2, x):
    y = ((p2[1]-p1[1])/(p2[0]-p1[0])) * (x-p1[0]) + p1[1]

    return y
    
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

# 직선 또는 다각형 그리는 함수
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
            pp = mpatches.PathPatch(path, fc=random.choice(colors), fill=True, lw=1, zorder=3, alpha=alpha)
    else:
        if dash:
            pp = mpatches.PathPatch(path, ec='black', fill=False, lw=1, ls='--', zorder=3)
        else:
            pp = mpatches.PathPatch(path, ec='black', fill=False, lw=1, zorder=3)
    ax.add_patch(pp)

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
            pp = mpatches.RegularPolygon(xy=center, ec='black', fill=False, lw=1, zorder=3)

    ax.add_patch(pp)

# 원 그리는 함수
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

# 타원 그리는 함수
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

# 각을 그리는 함수
def drawAngle(ax, p3, p2, p1):
    
    dx1 = p1[0] - p2[0]
    dy1 = p1[1] - p2[1]

    dx2 = p3[0] - p2[0]
    dy2 = p3[1] - p2[1]

    a1 = math.degrees(math.atan2(dy1,dx1))
    a2 = math.degrees(math.atan2(dy2,dx2))

    #d = (math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)+math.sqrt((p3[0]-p2[0])**2+(p3[1]-p2[1])**2))/2
    d = 4

    #print(a1,a2)
    angle = a2 -a1
    if angle < 0:
        angle = 360 + angle

    if angle < 30:
        pp = mpatches.Arc(p2, angle=0, width=0.25*d, height=0.25*d, theta1=a1, theta2=a2, ec='red', zorder=3)
    elif angle > 90:
        pp = mpatches.Arc(p2, angle=0, width=0.2*d, height=0.2*d, theta1=a1, theta2=a2, ec='red', zorder=3)
    else:
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
        else:
            pp = mpatches.Arc(p2, angle=0, width=0.2*d, height=0.2*d, theta1=a1, theta2=a2, ec='red', zorder=3)
        
    mid = ((p3[0]+p1[0])/2, (p3[1]+p1[1])/2)
    if mid[0]-p2[0] == 0:
        x = p2[0]
        if 0 <= a1 <= 90:
            y = p2[1]+0.2*d
        elif -180 <= a1 <= -90:
            y = p2[1]-0.2*d
    elif mid[1]-p2[1] == 0:
        y = p2[1]
        if 90 <= a1 <= 180:
            x = p2[0]-0.2*d
        elif -90 <= a1 <= 0:
            x = p2[0]+0.2*d
    else:
        n = (mid[1]-p2[1])/(mid[0]-p2[0])

        if 0 <= a1 < 90:
            if angle <= 90:
                x = p2[0]+0.08*d
            else:
                x = p2[0]-0.08*d
        elif 90 <= a1 < 180:
            x = p2[0]-0.08*d
        elif -180 <= a1 < -90:
            x = p2[0]-0.08*d
        else:
            x = p2[0]+0.08*d

        y = n*(x-p2[0])+p2[1]

    ax.add_patch(pp)

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

# 선분의 길이를 표시하는 bezier 곡선을 그리는 함수
def drawArc(ax, p1, p2, position, text, boxed=False):
    cp = controlPoint(p1,p2,position)
    d = math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
    l = len(text)
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
            plt.text(cp[0]-0.09*l, cp[1], text, fontsize=16, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom':
            plt.text(cp[0]-0.05*l, cp[1], text, fontsize=16, bbox=dict(ec='black', fc='white'))
        elif position == 'left':
            plt.text(cp[0]-0.05*l, cp[1], text, fontsize=16, bbox=dict(ec='black', fc='white'))
        elif position == 'right':
            plt.text(cp[0]-0.05*l, cp[1], text, fontsize=16, bbox=dict(ec='black', fc='white'))
    else:
        if position == 'top':
            plt.text(cp[0]-0.05*l, cp[1], text, fontsize=16)
        elif position == 'bottom':
            plt.text(cp[0]-0.05*l, cp[1], text, fontsize=16)
        elif position == 'left':
            plt.text(cp[0]-0.05*l, cp[1], text, fontsize=16)
        elif position == 'right':
            plt.text(cp[0]-0.05*l, cp[1], text, fontsize=16)

# 점을 찍는 함수
def setPoint(ax,points,fill=False, text=[]):
    temp = []
    for p in points:
        if p not in temp:
            temp.append(p)
    points = temp
    if len(points) == 1:
        if len(text) == 0:
            text.append('')
        plt.text(points[0][0], points[0][1]+0.05, text[0], fontsize=16, zorder=3)
        if fill:
            ax.plot(points[0][0], points[0][1],"ko", zorder=3)
    else:
        if len(text) == 0:
            for t in range(len(points)):
                text.append('')

        for i in range(0,len(points)):

            plt.text(points[i][0]-0.5, points[i][1]+0.5, text[i], fontsize=16, zorder=3)

            if fill:
                ax.plot(points[i][0], points[i][1],"ko", zorder=3)

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

def distance(p1, p2):
    d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    return d

def line_equation(p1, p2, x):
    y = ((p2[1]-p1[1])/(p2[0]-p1[0])) * (x-p1[0]) + p1[1]

    return y


def create_p_polygon(n=3,scale=100,move_x=0,move_y=0):
    def calculate_distance(p1=tuple, p2=tuple):
        import math
        d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
        return d
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
    def find_p_start(p_list=[]):
        #calculate center point
        p_list = sorted(p_list,key=lambda p:(p[0]-p[1]),reverse=True)
        return p_list[0]
    def find_p_next(p,p_list):
        def find_p_topRight(p,p_list):
            x,y = p
            for p_temp in p_list:
                x_temp,y_temp = p_temp
                if x_temp >= x and y_temp >= y:
                    return p_temp
            return False
        def find_p_bottomRight(p,p_list):
            x,y = p
            for p_temp in p_list:
                x_temp,y_temp = p_temp
                if x_temp >= x and y_temp <= y:
                    return p_temp
            return False
        def find_p_topLeft(p,p_list):
            x,y = p
            for p_temp in p_list:
                x_temp,y_temp = p_temp
                if x_temp <= x and y_temp >= y:
                    return p_temp
            return False
        def find_p_bottomLeft(p,p_list):
            x,y = p
            for p_temp in p_list:
                x_temp,y_temp = p_temp
                if x_temp <= x and y_temp <= y:
                    return p_temp
            return False
        if len(p_list) == 1:
            return p_list[0]
        p_list = sorted(p_list, key=lambda temp_p:calculate_distance(p,temp_p))
        p_topRight = find_p_topRight(p,p_list)
        p_topLeft = find_p_topLeft(p,p_list)
        p_bottomLeft = find_p_bottomLeft(p,p_list)
        p_bottomRight = find_p_bottomRight(p,p_list)
        if p_topRight:
            return p_topRight
        elif p_topLeft:
            return p_topLeft
        elif p_bottomLeft:
            return p_bottomLeft
        elif p_bottomRight:
            return p_bottomRight
    def ccw_sort(p):
        p = np.array(p)
        mean = np.mean(p,axis=0)
        d = p-mean
        s = np.arctan2(d[:,0], d[:,1])
        return list(p[np.argsort(s),:])
    import random
    temp_p = (0,0)
    polygon = [(0,0)]
    #create polygon
    for i in range(n-1):
        while True:
            angle = 180 * (n-2) / n + random.randint(-30,30)
            length = scale/2 + random.randint(round(scale/10)*-1,round(scale/10))
            properAngle = 0 < abs(angle) and abs(angle) < 180
            properLength = 10 < length and length < 50
            if properAngle and properLength:
                break
        temp_p = new_p_angle(angle,length,temp_p)
        polygon.append(temp_p)
        polygon = rotate_p(polygon,180-angle)
        temp_p = (rotate_p([temp_p],180-angle))[0]
    #recreate polygon
    temp_p = find_p_start(polygon)
    new_polygon = [temp_p]
    polygon.remove(temp_p)
    for i in range(n-1):
        temp_p = find_p_next(temp_p,polygon)
        new_polygon.append(temp_p)
        polygon.remove(temp_p)

    polygon = ccw_sort(new_polygon)
    polygon = move_to_center(polygon)
    polygon = move_p(polygon,move_x,move_y)
    return polygon

# 3-1-2-06
def flate312_Stem_001():
    s_flag = random.randint(0,2)
    if s_flag == 0:
        line = "선분"
    elif s_flag == 1:
        line = "반직선"
    else:
        line = "직선"


    while True:
        p1 = (random.randint(-9,-1), random.randint(1,9))
        p2 = (random.randint(-9,-1), random.randint(1,9))

        p3 = (random.randint(1,9), random.randint(1,9))
        p4 = (random.randint(1,9), random.randint(1,9))

        p5 = (random.randint(-9,-1), random.randint(-9,-1))
        p6 = (random.randint(-9,-1), random.randint(-9,-1))

        p7 = (random.randint(1,9), random.randint(-9,-1))
        p8 = (random.randint(1,9), random.randint(-9,-1))

        if p1[0] < p2[0] and p3[0] < p4[0] and p5[0] < p6[0] and p7[0] < p8[0]:
            if distance(p1,p2) >= 5 and distance(p3,p4) >= 5 and distance(p5,p6) >= 5 and distance(p7,p8) >= 5:
                m1 = abs((p2[1]-p1[1])/(p2[0]-p1[0]))
                m2 = abs((p4[1]-p3[1])/(p4[0]-p3[0]))
                m3 = abs((p6[1]-p5[1])/(p6[0]-p5[0]))
                m4 = abs((p8[1]-p7[1])/(p8[0]-p7[0]))

                if m1 < 1.5 and m2 < 1.5 and m3 < 1.5 and m4 < 1.5:
                    break

    point_dict = {0:[p1,p2], 1:[p3,p4], 2:[p5,p6], 3:[p7,p8]}

    answer_dict = {0:"ㄱㄴ", 1:"ㄷㄹ", 2:"ㅁㅂ", 3:"ㅅㅇ"}
    answer_list = random.sample(range(4), 2)
    answer_list.sort()
    answer = "(답):{line} {answer1}, {line} {answer2}".format(line=line, answer1=answer_dict[answer_list[0]], answer2=answer_dict[answer_list[1]])

    ax = setChart(points=[p1,p2,p3,p4,p5,p6,p7,p8])
    
    for p in point_dict:
        drawPolygon(ax=ax, verts=point_dict[p])
        if p == 0:
            text = ["ㄱ","ㄴ"]
        elif p == 1:
            text = ["ㄷ", "ㄹ"]
        elif p == 2:
            text = ["ㅁ", "ㅂ"]
        else:
            text = ["ㅅ", "ㅇ"]

        if p in answer_list:
            if s_flag == 0:
                setPoint(ax=ax, points=point_dict[p], fill=True, text=text)
            elif s_flag == 1:
                x = point_dict[p][1][0] - 0.9
                y = line_equation(point_dict[p][0], point_dict[p][1], x)
                np = (x,y)

                setPoint(ax=ax, points=[point_dict[p][0], np], fill=True, text=text)
            else:
                x1 = point_dict[p][0][0] + 0.9
                y1 = line_equation(point_dict[p][0], point_dict[p][1], x1)
                np1 = (x1, y1)

                x2 = point_dict[p][1][0] - 0.9
                y2 = line_equation(point_dict[p][0], point_dict[p][1], x2)
                np2 = (x2, y2)

                setPoint(ax=ax, points=[np1, np2], fill=True, text=text)
        else:
            ss_flag = random.randint(0,1)
            if s_flag == 0:
                if ss_flag == 0:
                    x = point_dict[p][1][0] - 0.9
                    y = line_equation(point_dict[p][0], point_dict[p][1], x)
                    np = (x,y)

                    setPoint(ax=ax, points=[point_dict[p][0], np], fill=True, text=text)
                else:
                    x1 = point_dict[p][0][0] + 0.9
                    y1 = line_equation(point_dict[p][0], point_dict[p][1], x1)
                    np1 = (x1, y1)

                    x2 = point_dict[p][1][0] - 0.9
                    y2 = line_equation(point_dict[p][0], point_dict[p][1], x2)
                    np2 = (x2, y2)

                    setPoint(ax=ax, points=[np1, np2], fill=True, text=text)
            elif s_flag == 1:
                if ss_flag == 0:
                    setPoint(ax=ax, points=point_dict[p], fill=True, text=text)
                else:
                    x1 = point_dict[p][0][0] + 0.9
                    y1 = line_equation(point_dict[p][0], point_dict[p][1], x1)
                    np1 = (x1, y1)

                    x2 = point_dict[p][1][0] - 0.9
                    y2 = line_equation(point_dict[p][0], point_dict[p][1], x2)
                    np2 = (x2, y2)

                    setPoint(ax=ax, points=[np1, np2], fill=True, text=text)
            else:
                if ss_flag == 0:
                    setPoint(ax=ax, points=point_dict[p], fill=True, text=text)
                else:
                    x = point_dict[p][1][0] - 0.9
                    y = line_equation(point_dict[p][0], point_dict[p][1], x)
                    np = (x,y)

                    setPoint(ax=ax, points=[point_dict[p][0], np], fill=True, text=text)
    stem = "다음 도형을 보고 %s을 찾아 이름을 써보세요."%(line)
    comment = "(해설)\n%s을 모두 찾아서 읽어보면 %s %s 과\n"\
                "%s %s입니다."%(
        line,
        line, answer_dict[answer_list[0]], 
        line, answer_dict[answer_list[1]]
    )

    svg= saveSvg()

    #plt.show()
    return stem, answer, comment, svg
    
# 3-1-2-10
def flate312_Stem_002():
    stem = "도형에서 선분은 몇 개 있나요?"
    answer = "(답):$$수식$${n}$$/수식$$개"
    comment = "(해설)\n선분은 두 점을 곧게 이은 선으로 모두 $$수식$${n}$$/수식$$개입니다."

    numOfPoints = random.randint(3,9)
    polygon = create_p_polygon(numOfPoints)
    
    ax = setChart(points=polygon)
    drawPolygon(ax=ax, verts=polygon, fill=True)
    plt.axis('scaled')
    #plt.show()
    answer = answer.format(n=numOfPoints)
    comment = comment.format(n=numOfPoints)
    svg = saveSvg()
    return stem, answer, comment, svg

# 3-1-2-11
def flate312_Stem_003():
    scale = 10
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    numOfPoints = random.randint(3,9)
    polygon = create_p_polygon(numOfPoints)

    
    drawPolygon(ax=ax, verts=polygon, fill=True)
    plt.axis('scaled')
    #plt.show()
    stem = "도형에서 찾을 수 있는 각은 모두 몇 개인가요?"
    answer = "(답):$$수식$${n}$$/수식$$개".format(n=numOfPoints)
    comment = "(해설)\n변과 변이 만나서 이루는 도형이 각입니다.\n"\
                "따라서 도형에서 찾을 수 있는 각은 모두 $$수식$$%s$$/수식$$개\n"\
                "입니다."%(numOfPoints)
    svg = saveSvg()
    return stem, answer, comment, svg

# 3-1-2-18
def flate312_Stem_004():
    n = random.randint(4,9)
    while True:
        x = np.random.randint(0,9,n)
        y = np.random.randint(0,9,n)
        center_point = [np.sum(x)/n, np.sum(y)/n]
        angles = np.arctan2(x-center_point[0],y-center_point[1])
        sort_tups = sorted([(i,j,k) for i,j,k in zip(x,y,angles)], key = lambda t: t[2])

        if len(sort_tups) == len(set(sort_tups)):
            n_dgree = []
            for i in range(len(sort_tups)):
                if i == len(sort_tups) - 2:
                    p1 = sort_tups[i]
                    p2 = sort_tups[i+1]
                    p3 = sort_tups[0]
                elif i == len(sort_tups) - 1:
                    p1 = sort_tups[i]
                    p2 = sort_tups[0]
                    p3 = sort_tups[1]
                else:
                    p1 = sort_tups[i]
                    p2 = sort_tups[i+1]
                    p3 = sort_tups[i+2]

                dx1 = p1[0] - p2[0]
                dy1 = p1[1] - p2[1]

                dx2 = p3[0] - p2[0]
                dy2 = p3[1] - p2[1]

                a1 = math.degrees(math.atan2(dy1,dx1))
                a2 = math.degrees(math.atan2(dy2,dx2))
                angle = a2 -a1

                if angle < 0:
                    angle = 360 + angle

                if angle == 90 and a1 in [-180.0, -135.0, -90.0, -45.0, 0.0, 45.0, 90.0, 135.0, 180.0] and a2 in [-180.0, -135.0, -90.0, -45.0, 0.0, 45.0, 90.0, 135.0, 180.0]:
                    n_dgree.append([p1,p2,p3])

            if len(n_dgree) >= 2:
                break
    points = []
    for i in sort_tups:
        temp = (i[0], i[1])
        points.append(temp)

    ax = setChart(points=points)
    drawPolygon(ax=ax, verts=points, fill=True)
    plt.axis('scaled')
    svg1 = saveSvg()

    ex = setChart(points=points)
    drawPolygon(ax=ex, verts=points)
    for p in n_dgree:
        drawAngle(ax=ex, p1=p[0], p2=p[1], p3=p[2])
    plt.axis('scaled')
    svg2 = saveSvg()

    #plt.show()
    stem = "도형에서 직각은 모두 몇 개인가요?"
    answer = "(답):$$수식$${n}$$/수식$$개".format(n=len(n_dgree))
    comment = "(해설)\n직각삼각자로 직각을 모두 찾아 표시하면 위\n"\
                "그림과 같습니다. 따라서 직각을 세어보면 모두\n"\
                "$$수식$${n}$$/수식$$개 입니다.".format(n=len(n_dgree))
    svg = [svg1, svg2]

    return stem, answer, comment, svg

# 3-1-2-25
def flate312_Stem_005():
    index = random.randint(0,5)
    flag = random.randint(0,1)
    text=['가', '나', '다', '라', '마', '바']
    
    while True:
        t1 = [[random.randint(0,3), 5], [4,5], [random.randint(0,4), 8]]
        t2 = [[random.randint(5,8), 5], [9,5], [random.randint(5,9), 8]]
        t3 = [[random.randint(10,13), 5], [14,5], [random.randint(10,14), 8]]
        t4 = [[random.randint(0,3), 0], [4,0], [random.randint(0,4), 3]]
        t5 = [[random.randint(5,8), 0], [9,0], [random.randint(5,9), 3]]
        t6 = [[random.randint(10,13), 0], [14,0], [random.randint(10,14), 3]]

        if t1[2][0] != t1[0][0] and t1[2][0] != t1[1][0]:
            if t2[2][0] != t2[0][0] and t2[2][0] != t2[1][0]:
                if t3[2][0] != t3[0][0] and t3[2][0] != t3[1][0]:
                    if t4[2][0] != t4[0][0] and t4[2][0] != t4[1][0]:
                        if t5[2][0] != t5[0][0] and t5[2][0] != t5[1][0]:
                            if t6[2][0] != t6[0][0] and t6[2][0] != t6[1][0]:
                                break

    poly_list = [t1,t2,t3,t4,t5,t6]
    
    if flag == 0:
        poly_list[index][2][0] = poly_list[index][0][0]
    else:
        poly_list[index][2][0] = poly_list[index][1][0]
        

    ax = setChart(points=[(0,0), (11,11)])
    drawPolygon(ax=ax, verts=t1)
    drawPolygon(ax=ax, verts=t2)
    drawPolygon(ax=ax, verts=t3)
    drawPolygon(ax=ax, verts=t4)
    drawPolygon(ax=ax, verts=t5)
    drawPolygon(ax=ax, verts=t6)

    setPoint(ax=ax, points=[t1[2],t2[2],t3[2],t4[2],t5[2],t6[2]], text=text)

    plt.axis('scaled')
    #plt.show()

    stem = "직각삼각형을 찾아 기호를 써보세요."
    answer = "(답):{answer}".format(answer=text[index])
    comment = "(해설)\n한 각이 직각인 삼각형을 찾습니다."

    svg=saveSvg()
    return stem, answer, comment, svg

# 3-1-2-33
def flate312_Stem_006():
    stem = "도형은 직사각형입니다. ㉠, ㉡에 알맞은 수를 "\
            "각각 구해 보세요."
    answer = "(답):㉠ $$수식$${answer1}$$/수식$$, ㉡ $$수식$${answer2}$$/수식$$"
    comment = "(해설)\n직사각형은 마주 보는 변의 길이가 같습니다."

    while True:
        l = random.randint(5,20)
        w = random.randint(5,20)

        if l != w:
            break

    p1 = (0,0)
    p2 = (w,0)
    p3 = (w,l)
    p4 = (0,l)

    answer = answer.format(answer1=str(l), answer2=str(w))

    ax = setChart(points=[p1,p2,p3,p4])
    drawPolygon(ax=ax, verts=[p1,p2,p3,p4], fill=False)
    drawArc(ax=ax, p1=p1, p2=p2, position="bottom", text="㉡"+r"$\mathrm{cm}$", boxed=True)
    drawArc(ax=ax, p1=p2, p2=p3, position="right", text="㉠"+r"$\mathrm{cm}$", boxed=True)
    drawArc(ax=ax, p1=p3, p2=p4, position="top", text=r"$%d \mathrm{cm}$"%w, boxed=True)
    drawArc(ax=ax, p1=p4, p2=p1, position="left", text=r"$%d \mathrm{cm}$"%l, boxed=True)

    plt.axis('scaled')
    #plt.show()

    svg=saveSvg()
    return stem, answer, comment, svg

# 3-1-2-35
def flate312_Stem_007():
    while True:
        width = random.randint(5,20)
        height = random.randint(5,20)

        if width != height:
            break

    p1 = (0,0)
    p2 = (width,0)
    p3 = (width,height)
    p4 = (0,height)
    
    ax = setChart(points=[p1,p2,p3,p4])

    s_width = r'$%d\mathrm{cm}$'%width
    s_height = r'$%d\mathrm{cm}$'%height

    drawPolygon(ax=ax, verts=[p1,p2,p3,p4], fill=True)
    drawArc(ax=ax, p1=p1, p2=p4, position='left', text=s_height, boxed=True)
    drawArc(ax=ax, p1=p3, p2=p4, position='top', text=s_width, boxed=True)

    plt.axis('scaled')
    #plt.show()

    stem = "직사각형 네 변의 길이의 합은 몇 $$수식$$rm cm$$/수식$$인가요?"
    answer = "(답):$$수식$${answer} rm cm$$/수식$$".format(answer=str(2*(width+height)))
    comment = "(해설)\n(네 변의  길이의 합)$$수식$$=%s+%s+%s+%s=%s(rm cm)$$/수식$$"%(width, height, width, height,str(2*(width+height)))
    svg=saveSvg()
    return stem, answer, comment, svg

# 3-1-2-41
def flate312_Stem_008():
    stem = "한 변의 길이가 $$수식$${x} rm cm$$/수식$$인 정사각형의 네 변의 길이의 합은 몇 $$수식$$rm cm$$/수식$$인가요?"
    answer = "(답):$$수식$${a} rm cm$$/수식$$"
    comment = "(해설)\n정사각형은 네 변의 길이가 모두 같습니다.\n(정사각형 네 변의 길이의 합)$$수식$$={x}+{x}+{x}+{x}={a}(rm cm)$$/수식$$"

    x = random.randint(1,15)
    a = x*4

    stem = stem.format(x=x)
    answer = answer.format(a=a)
    comment = comment.format(x=x, a=a)
    return stem, answer, comment

# 3-1-2-44
def flate312_Stem_009():
    stem = "직사각형 모양의 종이를 잘라서 한 변의 길이가 "\
            "$$수식$${height} rm cm$$/수식$$인 정사각형이 가장 많이 나오게 만들려고 "\
            "합니다. 정사각형을 몇 개까지 만들 수 있나요?"
    answer = "(답):$$수식$${answer}$$/수식$$개"
    comment = "(해설)\n정사각형을 $$수식$${answer}$$/수식$$개까지 만들 수 있습니다."

    while True: 
        width = random.randint(8, 20)
        height = random.randint(2, 9)

        if width/height < 8 and width%height == 0 and width != height:
            break
        
    result = int(width/height)

    p1 = (0,0)
    p2 = (width,0)
    p3 = (width,height)
    p4 = (0,height)
    ax = setChart(points=[p1,p2,p3,p4])

    s_width = r'$%d\mathrm{cm}$'%width
    s_height = r'$%d\mathrm{cm}$'%height

    drawPolygon(ax=ax, verts=[p1,p2,p3,p4], fill=True)
    drawArc(ax=ax, p1=p1, p2=p2, position='bottom', text=s_width, boxed=True)
    drawArc(ax=ax, p1=p2, p2=p3, position='right', text=s_height, boxed=True)

    stem = stem.format(height=height)
    answer = answer.format(answer=str(result))
    comment = comment.format(answer=str(result))

    plt.axis('scaled')
    svg1 = saveSvg()

    for i in range(result):
        t1 = (height*i, 0)
        t2 = (height*i, height)
        t3 = (height*(i+1), height)

        drawPolygon(ax=ax, verts=[t1,t2])
        drawArc(ax=ax, p1=t2, p2=t3, position="top", text=s_height)

    svg2 = saveSvg()

    svg=[svg1, svg2]
    #plt.show()

    return stem, answer, comment, svg

# 3-1-2-45
def flate312_Stem_010():
    stem = "직사각형과 정사각형의 네 변의 길이의 합이 "\
            "같습니다. 정사각형 한 변의 길이는 몇 $$수식$$rm cm$$/수식$$ "\
            "인가요?"

    while True:
        width = random.randint(3,20)
        height = random.randint(5,20)

        if width != height and (width+height)%2 == 0:
            break

    # 직사각형
    p1 = (0,0)
    p2 = (width,0)
    p3 = (width,height)
    p4 = (0,height)

    s_width = r'$%d\mathrm{cm}$'%width
    s_height = r'$%d\mathrm{cm}$'%height

    # 정사각형 한 변의 길이
    l = int((width+height)/2)
    r1 = (width+3,0)
    r2 = (width+3+l, 0)
    r3 = (width+3+l, l)
    r4 = (width+3, l)

    ax = setChart(points=[p1,p2,p3,p4,r1,r2,r3,r4])

    drawPolygon(ax=ax, verts=[p1,p2,p3,p4], fill=True)
    drawArc(ax=ax, p1=p1, p2=p4, position='left', text=s_height, boxed=True)
    drawArc(ax=ax, p1=p3, p2=p4, position='top', text=s_width, boxed=True)

    drawPolygon(ax=ax, verts=[r1,r2,r3,r4], fill=True)

    plt.axis('scaled')
    #plt.show()

    answer = "(답):$$수식$$" + str(l) + " rm cm$$/수식$$"
    comment = "(해설)\n(직사각형의 네 변의 길이의 합)\n$$수식$$=%d+%d+%d+%d=%d(rm cm)$$/수식$$\n"%(width, height, width, height, 2*(width+height))
    comment = comment + "정사각형의 네 변의 길이의 합도 $$수식$$%d rm cm$$/수식$$이고\n"%(2*(width+height))
    comment = comment + "$$수식$$%d+%d+%d+%d=%d$$/수식$$이므로 정사각형의 한\n"\
                "변의 길이는 $$수식$$%drm cm$$/수식$$입니다."%(l,l,l,l,2*(width+height),l)
    svg = saveSvg()

    return stem, answer, comment, svg
