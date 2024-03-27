import math
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib as mpl
import numpy as np
import matplotlib.lines
from matplotlib.path import Path
import random
import io
import sys
import math

#plt.rcParams['text.usetex'] = True
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf8')
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf8')

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

# 직선
def drawLine(ax,pts,dash=False,color='black'):
    if dash: linestype = 'dashed'
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

# 문자
def drawText(ax,text='',xy=(0,0),position='top'):
    if len(xy) > 2: raise Exception("too many inputs for xy")
    l = len(str(text))
    fontsize = 16
    if 'mathrm' in text: 
        l -= 10
    cp = xy
    if position == 'top':
        plt.text(cp[0]-2*l, cp[1]+5, text, fontsize=fontsize, zorder=3)
    elif position == 'bottom':
        plt.text(cp[0]-2*l, cp[1]-8, text, fontsize=fontsize, zorder=3)
    elif position == 'left':
        plt.text(cp[0]-2-l*4.5, cp[1]-2, text, fontsize=fontsize, zorder=3)
    elif position == 'right':
        plt.text(cp[0]+l, cp[1]-2, text, fontsize=fontsize, zorder=3)
    elif position == 'top_r':
        plt.text(cp[0]+1+l*0.3, cp[1]+5, text, fontsize=fontsize, zorder=3)
    elif position == 'top_l':
        plt.text(cp[0]+1-l*5, cp[1]+2, text, fontsize=fontsize, zorder=3)
    elif position == 'bottom_r':
        plt.text(cp[0]+1+l*0.3, cp[1]-11, text, fontsize=fontsize, zorder=3)
    elif position == 'bottom_l':
        plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5, text, fontsize=fontsize, zorder=3)
    else: raise Exception('no matching position')


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
def drawCircle_(ax,center, radius, fill=False, alpha=1, dash=False, position=None, color='',ec='black'):
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
            print(a1, a2)
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
    # 지나는 점 (p1, p2의 중점)
    mp = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

    if (p2[0]-p1[0]) == 0: #y-axis
        if type == 'left' or type == 'top':
            cp = (mp[0]-0.2*d,mp[1])
        else:
            cp = (mp[0]+0.2*d,mp[1])
    elif (p2[1]-p1[1]) == 0: #x_axis
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

# 선분의 길이를 표시하는 bezier 곡선을 그리는 함수
def drawArc(ax, p_list, position, text, boxed=False,color='black',distance=5):
    if len(p_list) != 2: raise Exception('p_list has more or less than 2 elements')
    p1 = p_list[0]
    p2 = p_list[1]
    if 'top' in position: cp = find_controlPoint_arc(p1,p2,'top',distance)
    elif 'bottom' in position: cp = find_controlPoint_arc(p1,p2,'bottom',distance)
    elif 'r' in position: cp = find_controlPoint_arc(p1,p2,'right',distance)
    elif 'l' in position: cp = find_controlPoint_arc(p1,p2,'left',distance)
    p1 = (round(p1[0],5),round(p1[1],5))
    p2 = (round(p2[0],5),round(p2[1],5))
    l = len(text)
    fontsize = 16
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

    pp = mpatches.PathPatch(path, fc="none", transform=ax.transData, linestyle="--", zorder=3, color=color)
    ax.add_patch(pp)

    if boxed:
        if position == 'top':
            plt.text(cp[0]-2*l, cp[1]+3.5, text, fontsize=fontsize, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom':
            plt.text(cp[0]-2*l, cp[1]-7.5, text, fontsize=fontsize, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'left':
            plt.text(cp[0]-2-l*4.5, cp[1]-2, text, fontsize=fontsize, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'right':
            plt.text(cp[0]+l, cp[1]-2, text, fontsize=fontsize, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'top_r':
            plt.text(cp[0]+l*0.3, cp[1]+2, text, fontsize=fontsize, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'top_l':
            plt.text(cp[0]+1-l*5, cp[1]+2, text, fontsize=fontsize, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_r':
            plt.text(cp[0]+l*0.3, cp[1]-8+l*0.5, text, fontsize=fontsize, zorder=3, bbox=dict(ec='black', fc='white'))
        elif position == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-8+l*0.5, text, fontsize=fontsize, zorder=3, bbox=dict(ec='black', fc='white'))
    else:
        if position == 'top':
            plt.text(cp[0]-l*5, cp[1]+1, text, fontsize=fontsize, zorder=3)
        elif position == 'bottom':
            plt.text(cp[0]-l*5, cp[1], text, fontsize=fontsize, zorder=3)
        elif position == 'left':
            plt.text(cp[0]-2-l*4.5, cp[1]-2, text, fontsize=fontsize, zorder=3)
        elif position == 'right':
            plt.text(cp[0]+l*0.1, cp[1]-2, text, fontsize=fontsize, zorder=3)
        elif position == 'top_r':
            plt.text(cp[0]+l*0.3, cp[1]+2, text, fontsize=fontsize, zorder=3)
        elif position == 'top_l':
            plt.text(cp[0]+1-l*4, cp[1]+2, text, fontsize=fontsize, zorder=3)
        elif position == 'bottom_r':
            plt.text(cp[0]+l, cp[1]-8+l*0.5, text, fontsize=fontsize, zorder=3)
        elif position == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-3+l*0.5, text, fontsize=fontsize, zorder=3)
        else: raise Exception('no matching position')


#점만 찍는 함수
def drawDot(ax,points=list,colors=False):
    if colors: format = 'r.'
    else: format = 'k.'
    for i in range(0,len(points)):
        ax.plot(points[i][0], points[i][1],format, zorder=3)

#직선 화살표 그리는 함수
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

#직선 양면 화살표 그리는 함수
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
    fontsize = 16
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
        middle_p2 = (((start_p[0]+end_p[0])/2+l),((start_p[1]+end_p[1])/2))
    else: raise Exception('not a stright line')
    if l == 0:
        drawArrow(ax,middle_p,end_p)
        drawArrow(ax,middle_p,start_p)
    else:
        drawArrow(ax,middle_p2,end_p)
        cp = controlPoint(middle_p1,middle_p2,'left')
        plt.text(cp[0]-l*0.6, middle_p[1]-2, text, fontsize=fontsize, zorder=3)
        drawArrow(ax,middle_p1,start_p)

# 점을 찍는 함수
def setPoint(ax,points=list,text=[],position=[],fill=False,color='black'):
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
        fontsize = 16
        if position[i] == 'top':
            plt.text(cp[0]-2*l, cp[1]+3.5, text[i], fontsize=fontsize, zorder=3)
        elif position[i] == 'bottom':
            plt.text(cp[0]-2*l, cp[1]-10, text[i], fontsize=fontsize, zorder=3)
        elif position[i] == 'left':
            plt.text(cp[0]-3-l*4.5, cp[1]-2, text[i], fontsize=fontsize, zorder=3)
        elif position[i] == 'right':
            plt.text(cp[0]+l, cp[1]-2, text[i], fontsize=fontsize, zorder=3)
        elif position[i] == 'top_r':
            plt.text(cp[0]+l*0.3, cp[1]+2, text[i], fontsize=fontsize, zorder=3)
        elif position[i] == 'top_l':
            plt.text(cp[0]+1-l*5, cp[1]+2, text[i], fontsize=fontsize, zorder=3)
        elif position[i] == 'bottom_r':
            plt.text(cp[0]+l*0.3, cp[1]-10, text[i], fontsize=fontsize, zorder=3)
        elif position[i] == 'bottom_l':
            plt.text(cp[0]+1-l*5, cp[1]-10, text[i], fontsize=fontsize, zorder=3)
        else: raise Exception('no matching position')
        #plt.text(points[i][0]-0.5, points[i][1]+0.1, text[i], fontsize=14, zorder=3)

        if fill:
            ax.plot(points[i][0], points[i][1],"k.", zorder=3,color=color)

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
    


def move_p2p(p_list=list,before_p=0,after_p=0):
    #center point
    x_move = after_p[0] - before_p[0]
    y_move = after_p[1] - before_p[1]
    new_p_list = []
    for index in range(len(p_list)):
        p = p_list[index]
        new_p_list.append((p[0]+x_move,p[1]+y_move))
    return new_p_list
def move_p_single(p,x_move=0,y_move=0):
        new_p = (p[0]+x_move,p[1]+y_move)
        return new_p
def calculate_distance(p1=tuple, p2=tuple):
    import math
    d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    return d
def c_과와(var):
    var = str(var)
    if 'frac' in var or 'sqrt' in var:
        if int(var[len(var)-2]) in (0,1,3,6,7,8):
            n = '과'
        else:
            n = '와'

    else:
        if int(var[len(var)-1]) in (0,1,3,6,7,8):
            n = '과'
        else:
            n = '와'
    return n
def find_p_in_circle323(r,p_list=[],O=(0,0)):
    import math
    import random
    def calculate_distance(p1=tuple, p2=tuple):
        import math
        d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
        return d
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
    sign = random.choice([1,-1])
    x = random.randint(r*-1,r)
    y = math.sqrt(r*r-x*x) * sign
    temp_p = (x,y)
    d_list = []
    while too_close(temp_p,p_list):
        x = random.randint(r*-1,r)
        y = math.sqrt(r*r-x*x) * sign
        temp_p = (x,y)
    return move_p_single((x,y),O[0],O[1])
def find_text_position_circle323(p,r=50):
    x = p[0]
    y = p[1]
    output = ""
    if y > 0:
        output += 'top'
    else:
        output += 'bottom'
    if x > 0:
        output += '_r'
    else:
        output += '_l'
    #exception_case
    if x >= 0 and x < (r/6):
        if y > 0:
            return 'top'
        else:
            return 'bottom'
    if y >= 0 and y < (r/6):
        if x > 0:
            return 'right'
        else:
            return 'left'
    return output
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
def get_diameter(r):
    return r*2


# 3-2-3-02
def circle323_Stem_001():
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
    radius = int(scale)
    ratio = random.randint(10,20)
    stem_radius = int(radius/ratio)
    #line-radius
    p_right = (radius,0)
    p_left = (-radius,0)
    if random.randint(0,1):
        l_radius = [p_right,O]
    else:
        l_radius = [O,p_left]
    #line above x-asix
    p_top1 = find_p_in_circle323(radius)
    p_top2 = find_p_in_circle323(radius,[p_top1])
    len_top = int(calculate_distance(p_top1,p_top2)/ratio)
    while p_top1[1] <= 0 or p_top2[1] <= 0 or calculate_distance(p_top1,p_top2) < 60 or len_top == stem_radius or len_top >= stem_radius*2:
        p_top1 = find_p_in_circle323(radius)
        p_top2 = find_p_in_circle323(radius,[p_top1])
        len_top = int(calculate_distance(p_top1,p_top2)/ratio)
    l_top = [p_top1,p_top2]
    #line below x_axis
    p_bottom1 = find_p_in_circle323(radius)
    p_bottom2 = find_p_in_circle323(radius,[p_bottom1])
    len_bottom = int(calculate_distance(p_bottom1,p_bottom2)/ratio)
    while p_bottom1[1] >= 0 or p_bottom2[1] >= 0 or calculate_distance(p_bottom1,p_bottom2) < 60 or len_bottom in [len_top,stem_radius] or len_bottom >= stem_radius*2:
        p_bottom1 = find_p_in_circle323(radius)
        p_bottom2 = find_p_in_circle323(radius,[p_bottom1])
        len_bottom = int(calculate_distance(p_bottom1,p_bottom2)/ratio)
    l_bottom = [p_bottom1,p_bottom2]
    #draw
    drawCircle(ax,O,radius)
    drawDot(ax,[O])
    drawLine(ax,l_top)
    drawLine(ax,l_bottom)
    drawLine(ax,l_radius)
    drawArc(ax,l_radius,'top','$%s \mathrm{cm}$'%(stem_radius))
    drawArc(ax,l_top,'bottom','$%s \mathrm{cm}$'%(len_top))
    drawArc(ax,l_bottom,'top','$%s \mathrm{cm}$'%(len_bottom))
    plt.axis('scaled')
    #stem/answer/comment
    stem = "원의 반지름은 몇 $$수식$$rm cm$$/수식$$인가요?"
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(stem_radius)
    comment = "(해설)\n원의 반지름은 원의 중심과 원 위의 한점을 이은\n"\
                "선이므로 $$수식$$%srm cm$$/수식$$ 입니다." %(stem_radius)
    svg= saveSvg()
    #plt.show()
    return stem, answer, comment, svg

# 3-2-3-05
def circle323_Stem_002():
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
    radius = int(scale/2)
    p_left = (radius*-1,0)
    p_right = (radius,0)
    circle323_Stem_num_list = ['①','②','③','④','⑤']
    #p_top: x > 0 & y > 0
    p_top = find_p_in_circle323(radius,[p_left,p_right])
    top_x = p_top[0]
    top_y = p_top[1]
    while top_x > -10 or top_y < 0:
        p_top = find_p_in_circle323(radius,[p_left,p_right])
        top_x = p_top[0]
        top_y = p_top[1]
    #p_top_opposite: opposite of p_top
    p_top_opposite = (top_x*-1,top_y*-1)
    #p_bottom: y < 0
    p_bottom = find_p_in_circle323(radius,[p_top,p_top_opposite,p_left,p_right])
    bottom_y = p_bottom[1]
    while bottom_y > 0:
        p_bottom = find_p_in_circle323(radius,[p_top_opposite,p_left,p_right])
        bottom_y = p_bottom[1]
    #point name
    p_name_list = ['A','B','C','D','E']
    random.shuffle(p_name_list)
    p_name_top, p_name_left, p_name_right, p_name_top_opposite, p_name_bottom = p_name_list
    p_name_O = 'O'
    #lines
    set_lines = True
    if set_lines:
        l_diameter = [p_left,p_right]
        l_answer = [p_top,p_top_opposite]
        l_center_2_bottom = [O,p_bottom]
        l_name_diameter = p_name_left+p_name_right
        l_name_radius_left = p_name_left + p_name_O
        l_name_radius_right = p_name_O + p_name_right
        l_name_answer = p_name_top + p_name_top_opposite
        l_name_center_2_bottom = p_name_O + p_name_bottom
        l_name_center_2_top_opposite = p_name_O + p_name_top_opposite
        l_name_top_2_center = p_name_top + p_name_O
        l_name_list = [l_name_diameter,l_name_radius_left,l_name_radius_right]
        l_name_list += [l_name_center_2_bottom,l_name_center_2_top_opposite,l_name_top_2_center]
        l_name_list_stem = random.sample(l_name_list,4) + [l_name_answer]
    random.shuffle(l_name_list_stem)
    draw = True
    if draw:
        #draw_circle323
        drawCircle(ax,O,radius)
        #draw_points
        setPoint(ax,[O],["O"],['top_r'],True,'red')
        setPoint(ax,l_diameter,text=[p_name_left,p_name_right],position=['left','right'])
        text_position_list = [find_text_position_circle323(p_top),find_text_position_circle323(p_top_opposite),find_text_position_circle323(p_bottom)]
        setPoint(ax,[p_top,p_top_opposite,p_bottom],text=[p_name_top,p_name_top_opposite,p_name_bottom],position=text_position_list)
        #draw_lines
        drawLine(ax,l_diameter)
        drawLine(ax,l_answer)
        drawLine(ax,l_center_2_bottom)
        problem_option = random.randint(0,1)
        if problem_option == 0:
            drawLine(ax,[p_top,p_right])
        elif problem_option == 1:
            drawLine(ax,[p_left,p_top])
        plt.axis('scaled')
    #stem/find_answer
    l_name_list_stem.sort()
    stem = "선분 %s와 길이가 같은 선분은 어느 것인가요?\n" %(l_name_diameter)
    for i in range(len(l_name_list_stem)):
        l_name = l_name_list_stem[i]
        stem += '%s 선분 %s    ' %(circle323_Stem_num_list[i],l_name)
        if i == 2:
            stem += "\n"
        if l_name == l_name_answer:
            answer_index = i
    #comment
    comment = "(해설)\n한 원에서 원의 지름은 모두 같으므로\n"
    comment += "선분 %s와 길이가 같은 선분은 선분 %s입니다." %(l_name_diameter,l_name_answer)
    answer = '(답):%s'%circle323_Stem_num_list[answer_index]
    #plt.show()
    svg= saveSvg()
    return stem, answer, comment, svg

# 3-2-3-06
def circle323_Stem_003():
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
    #generate shapes
    while True:
        radius_small = random.randint(4,8)
        radius_big = radius_small + random.randint(1,4)
        ratio = 9
        p_center_big = (-radius_big*ratio-10,0)
        p_center_small = (radius_small*ratio+10,0)
        p_text_big = (p_center_big[0],p_center_big[1]+radius_big*ratio+10)
        p_text_small = (p_center_small[0],p_text_big[1])
        p_random_big2 = find_p_in_circle323(radius_big*ratio,O=p_center_big)
        p_random_big3 = find_p_in_circle323(radius_big*ratio,[p_random_big2],O=p_center_big)
        p_random_small2 = find_p_in_circle323(radius_small*ratio,O=p_center_small)
        p_random_small3 = find_p_in_circle323(radius_small*ratio,[p_random_small2],O=p_center_small)
        distance_big = int(calculate_distance(p_random_big2,p_random_big3)/ratio)
        distance_small = int(calculate_distance(p_random_small2,p_random_small3)/ratio)
        min = 6
        if (min < distance_big and distance_big < get_diameter(radius_big)-3) and (min < distance_small and distance_small < get_diameter(radius_small)-3):
            break
    p_random_big1 = find_p_in_circle323(radius_big*ratio,O=p_center_big)
    p_random_small1 = find_p_in_circle323(radius_small*ratio,O=p_center_small)
    l_diameter_big = [
        p_random_big1,
        move_p2p([p_center_big],p_random_big1,p_center_big)[0]
    ]
    l_diameter_small = [
        p_random_small1,
        move_p2p([p_center_small],p_random_small1,p_center_small)[0]
    ]
    l_random_big = [p_random_big2,p_random_big3]
    l_random_small = [p_random_small2,p_random_small3]
    #draw
    drawCircle_(ax,p_center_big,radius_big*ratio)
    drawCircle_(ax,p_center_small,radius_small*ratio)
    drawDot(ax,[p_center_big,p_center_small],True)
    drawLine_multiple(ax,[l_diameter_big,l_diameter_small])
    drawLine_multiple(ax,[l_random_small,l_random_big])
    drawArc(ax,l_diameter_small,'top','$%s \mathrm{cm}$'%(get_diameter(radius_small)),distance=10)
    drawArc(ax,l_diameter_big,'top','$%s \mathrm{cm}$'%(get_diameter(radius_big)),distance=10)
    drawArc(ax,l_random_big,'top','$%s \mathrm{cm}$'%(distance_big),distance=10)
    drawArc(ax,l_random_small,'top','$%s \mathrm{cm}$'%(distance_small),distance=10)
    drawText(ax,'A',p_text_big)
    drawText(ax,'B',p_text_small)
    plt.axis('scaled')
    #stem/answer/comment
    stem = "두 원의 지름의 차는 몇 $$수식$$rm cm$$/수식$$인가요?"
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(get_diameter(radius_big)-get_diameter(radius_small))
    comment = "(해설)\nA원의 지름은 $$수식$$%srm cm$$/수식$$이고 B원의 지름은 $$수식$$%srm cm$$/수식$$\n"\
                "입니다. 따라서 두 원의 지름의 차는\n"\
                "$$수식$$%s - %s = %s(rm cm)$$/수식$$입니다."%(
                    get_diameter(radius_big), 
                    get_diameter(radius_small),
                    get_diameter(radius_big),get_diameter(radius_small),
                    (get_diameter(radius_big)-get_diameter(radius_small))
                )
    #plt.show()
    svg = saveSvg()
    return stem, answer, comment, svg

# 3-2-3-11
def circle323_Stem_004():
    stem = "크기가 가장 큰 원은 어느 것인가요?\n"
    #generate variable
    number_circle323_Stem_list = ['①','②','③','④','⑤']
    diameter_list = []
    radius_list = []
    index_switch_diameter_2_radius = 0
    while len(diameter_list) < 5: #지름_list 생성
        random_diameter = random.randint(2,20)
        if random_diameter not in diameter_list: #중복체크
            diameter_list.append(random_diameter)
    random.shuffle(diameter_list)
    for diameter in diameter_list: #반지름_list 생성 from 지름_list
        if diameter % 2 == 0: #반지름 가능
            radius = int(diameter/2)
            radius_list.append(radius)
            diameter_list.remove(diameter)
            index_switch_diameter_2_radius += 1
    length_list = diameter_list + radius_list #종합_list 생성
    #stem
    for i in range(len(length_list)):
        stem += number_circle323_Stem_list[i] + ' '
        length = length_list[i]
        if i+1 <= len(length_list)-index_switch_diameter_2_radius: #지름
            stem += '지름이 $$수식$$%srm cm$$/수식$$인 원\n'%(length)
        else: #반지름
            stem += '반지름이 $$수식$$%srm cm$$/수식$$인 원\n'%(length)
    stem = stem[:len(stem)-1]
    #comment/find_answer
    max_length = length_list[0]
    max_index = 0
    comment = "(해설)\n지름을 비교해 본다.\n"
    for i in range(len(length_list)):
        comment += number_circle323_Stem_list[i] + ' '
        if i+1 <= len(length_list)-index_switch_diameter_2_radius: #지름
            diameter = length_list[i]
            comment += '$$수식$$%srm cm$$/수식$$, '%(diameter)
            if max_length < diameter:
                max_length = diameter
                max_index = i
        else: #반지름
            radius = length_list[i]
            diameter = radius*2
            comment += '$$수식$$%s \\times 2 = %s(rm cm)$$/수식$$, '%(radius,diameter)
            if max_length < diameter:
                max_length = diameter
                max_index = i
        if i == 2 or i == 4:
            comment += '\n'
    answer = '(답):%s'%number_circle323_Stem_list[max_index]
    comment += "따라서 크기가 가장 큰 원은 %s입니다." %(number_circle323_Stem_list[max_index])
    
    return stem,answer,comment
    
# 3-2-3-12
def circle323_Stem_005():
    #generate variable
    radius = random.randint(2,8)
    diameter = radius * 2
    problem_optoin1 = random.randint(0,1)
    if problem_optoin1 == 0: #지름 -> 반지름
        stem = "지름이 $$수식$$$$수식$$%srm cm$$/수식$$$$/수식$$인 원의 반지름은 몇 $$수식$$rm cm$$/수식$$인가요?" %(diameter)
        answer = '(답):$$수식$$%srm cm$$/수식$$'%(radius)
        comment = "(해설)\n(원의 반지름) $$수식$$=$$/수식$$ (원의 지름)$$수식$$ div 2$$/수식$$\n"
        comment += "$$수식$$=%s div 2 = %s(rm cm)$$/수식$$"%(diameter,radius)
    elif problem_optoin1 == 1: #반지름 -> 지름
        stem = "반지름이 $$수식$$$$수식$$%srm cm$$/수식$$$$/수식$$인 원의 지름은 몇 $$수식$$rm cm$$/수식$$인가요?" %(radius)
        answer = '(답):$$수식$$%srm cm$$/수식$$'%(diameter)
        comment = "(해설)\n(원의 지름) $$수식$$=$$/수식$$ (원의 반지름)$$수식$$ \\times 2$$/수식$$\n"
        comment += "$$수식$$=%s \\times 2 = %s(rm cm)$$/수식$$"%(radius,diameter)

    return stem,answer,comment

# 3-2-3-14
def circle323_Stem_006():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #generate circle323s
    radius_big = int(scale/2) #first_circle323
    p_big_center = (radius_big*-1,0)
    radius_small = random.randint(radius_big*0.4,radius_big*0.8) #second circle323
    p_small_center = (radius_small,0)
    p_big_center,p_small_center = move_p_to_center([p_big_center,p_small_center])
    #point
    p_big_left = (p_big_center[0]-radius_big,0)
    p_small_left = (p_small_center[0]-radius_small,0)
    p_small_right = (p_small_center[0]+radius_small,0)
    #line
    l_left_2_right = [p_big_left,p_small_right]
    l_big_radius_left = [p_big_left,p_big_center]
    l_small_radius_left = [p_small_left,p_small_center]
    #ratio
    ratio = random.randint(5,15)
    while int(radius_big/ratio) <= int(radius_small/ratio):
        ratio = random.randint(5,15)
    radius_big_scale_down = int(radius_big / ratio)
    radius_small_scale_down = int(radius_small/ratio)
    diameter_big_scale_down = radius_big_scale_down*2
    diameter_small_scale_down = radius_small_scale_down*2
    #draw
    drawCircle(ax,p_big_center,radius_big)
    drawCircle(ax,p_small_center,radius_small)
    setPoint(ax,[p_big_left,p_small_right],['A','B'],['left','right']) #draw_A,B
    drawDot(ax,[p_big_center,p_small_center]) #dot in centers
    drawLine(ax,l_left_2_right) #draw line
    drawArc(ax,l_big_radius_left,'top','$%s \mathrm{cm}$'%(radius_big_scale_down))
    drawArc(ax,l_small_radius_left,'top','$%s \mathrm{cm}$'%(radius_small_scale_down))
    plt.axis('scaled')
    #stem/answer/comment
    stem = "선분 AB의 길이는 몇 $$수식$$rm cm$$/수식$$인가요? \n"
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(diameter_big_scale_down+diameter_small_scale_down)
    comment = "(해설)\n(큰 원의 지름) $$수식$$=%s \\times 2 = %s(rm cm)$$/수식$$ \n"\
                "(작은 원의 지름) $$수식$$=%s \\times 2 = %s(rm cm)$$/수식$$ \n"\
                "(선분 AB의 길이) \n"\
                " $$수식$$=$$/수식$$ (큰 원의 지름)$$수식$$+$$/수식$$(작은 원의 지름)\n"\
                " $$수식$$=%s+%s=%s(rm cm)$$/수식$$" %(
                    radius_big_scale_down,diameter_big_scale_down,
                    radius_small_scale_down,diameter_small_scale_down,
                    diameter_big_scale_down,diameter_small_scale_down,diameter_big_scale_down+diameter_small_scale_down
                )
    #plt.show()
    svg= saveSvg()
    return stem, answer, comment, svg

# 3-2-3-15
def circle323_Stem_007():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #generate circle323s
    radius_big = int(scale)
    p_big_center = (0,0)
    radius_small = int(scale/2)
    p_small_center = (radius_small*-1,0)
    #ratio
    ratio = random.randint(7,20)
    while int(radius_big/ratio) <= int(radius_small/ratio):
        ratio = random.randint(7,20)
    radius_small_scale_down = int(radius_small/ratio)
    diameter_small_scale_down = radius_small_scale_down*2
    radius_big_scale_down = diameter_small_scale_down
    diameter_big_scale_down = radius_big_scale_down*2
    #point
    p_big_left = (p_big_center[0]-radius_big,0)
    p_big_right = (p_big_center[0]+radius_big,0)
    p_small_left = (p_small_center[0]-radius_small,0)
    p_small_right = (p_small_center[0]+radius_small,0)
    #line
    l_big_diameter = [p_big_left,p_big_right]
    l_small_radius_left = [p_small_left,p_small_center]
    #draw
    drawCircle(ax,p_big_center,radius_big)
    drawCircle(ax,p_small_center,radius_small)
    setPoint(ax,[p_small_center,p_big_center],['A','B'],['bottom','bottom_r'],True,color='red')
    drawLine(ax,l_big_diameter)
    drawArc(ax,l_small_radius_left,'top','$%s \mathrm{cm}$'%(radius_small_scale_down))
    plt.axis('scaled')
    #stem/answer/comment
    stem = "점 $$수식$$A$$/수식$$, 점 $$수식$$B$$/수식$$는 원의 중심입니다. 큰 원의 지름은 몇 $$수식$$rm cm$$/수식$$인가요?"
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(radius_big_scale_down*2)
    comment = "(해설)\n(작은 원의 지름) $$수식$$=%s \\times 2=%s(rm cm)$$/수식$$ \n"\
                "(큰 원의 지름) $$수식$$=%s \\times 2=%s(rm cm)$$/수식$$ \n" %(
                    radius_small_scale_down,diameter_small_scale_down,
                    radius_big_scale_down,diameter_big_scale_down
                    )
    #plt.show()
    svg= saveSvg()
    return stem, answer, comment, svg

# 3-2-3-16
def circle323_Stem_008():
    #setting
    scale = 100
    O = (0,0)
    x_p = (scale,0)
    y_p = (0,scale)
    x_n = (scale*-1,0)
    y_n = (0,scale*-1)
    dim_2 = [x_p, y_p, x_n, y_n]
    ax = setChart(dim_2)
    #generate circle323
    radius_big = int(scale)
    p_big_center = (0,0)
    radius_small = int(scale/random.randint(2,3))
    p_small_center = (0,0)
    #ratio
    ratio = random.randint(5,10)
    while int(radius_big/ratio) <= int(radius_small/ratio):
        ratio = random.randint(5,10)
    radius_big_scale_down = int(radius_big/ratio)
    radius_small_scale_down = int(radius_small/ratio)
    len_stem = radius_big_scale_down - radius_small_scale_down
    #point
    p_big_left = (radius_big*-1,0)
    p_big_right = (radius_big,0)
    p_big_top = (0,radius_big)
    p_big_bottom = (0,radius_big*-1)
    p_small_left = (radius_small*-1,0)
    p_small_right = (radius_small,0)
    p_small_top = (0,radius_small)
    p_small_bottom = (0,radius_small*-1)
    #line
    l_small_radius_left = [p_small_left,p_small_center]
    l_random_side = random.choice([[p_small_right,p_big_right,'top'],[p_small_bottom,p_big_bottom,'right'],[p_small_top,p_big_top,'right']])
    l_big_radius_random_side = [p_big_center,l_random_side[1]]
    l_small_radius_2_big_radius = [l_random_side[0],l_random_side[1]]
    position = l_random_side[2]
    #draw
    drawCircle(ax,p_big_center,radius_big)
    drawCircle(ax,p_small_center,radius_small)
    drawDot(ax,[O])
    drawLine(ax,l_small_radius_left)
    drawArc(ax,l_small_radius_left,'top','$%s \mathrm{cm}$'%(radius_small_scale_down))
    #lines & arc for outter
    drawLine(ax,l_big_radius_random_side)
    drawArc(ax,l_small_radius_2_big_radius,position,'$%s \mathrm{cm}$'%(len_stem))
    plt.axis('scaled')
    #stem/answer/comment
    stem = "큰 원의 반지름은 몇 $$수식$$rm cm$$/수식$$인가요?"
    answer = '(답):$$수식$$%srm cm$$/수식$$'%(radius_big_scale_down)
    comment = "(해설)\n큰 원의 반지름은 (작은 원의 반지름)$$수식$$+%s$$/수식$$이므로 \n" %(len_stem)
    comment += "(큰 원의 반지름) $$수식$$=%s+%s=%s(rm cm)$$/수식$$입니다."%(radius_small_scale_down,len_stem,radius_big_scale_down)
    
    #plt.show()
    svg= saveSvg()
    return stem, answer, comment, svg

# 3-2-3-18
def circle323_Stem_009():
    def drawInnerCircle323s(ax,numOfCiecles):
        diameter_small = 140/numOfCiecles
        radius_small = diameter_small/2
        p_tempCenter = (-70+radius_small,0)
        for i in range(numOfCiecles):
            drawCircle_(ax,p_tempCenter,radius_small)
            drawDot(ax,[p_tempCenter],True)
            p_tempCenter = (p_tempCenter[0]+diameter_small,p_tempCenter[1])

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
    numOfCircle323s = random.randint(2,4)
    radius_small = random.randint(3,8)
    diameter_big = get_diameter(radius_small)*numOfCircle323s
    #generate shapes
    p_center = (0,0)
    l_diameter = [(-70,0),(70,0)]
    #draw
    drawCircle_(ax,p_center,70)
    drawLine(ax,l_diameter)
    drawInnerCircle323s(ax,numOfCircle323s)
    plt.axis('scaled')
    #stem/answer/comment
    stem = "큰 원 안에 크기가 같은 작은 원 $$수식$$%s$$/수식$$개를 맞닿게 "\
            "그린 것입니다. 큰 원의 지름이 $$수식$$%srm cm$$/수식$$라면 작은 "\
            "원의 반지름은 몇 $$수식$$rm cm$$/수식$$인가요?"%(numOfCircle323s,diameter_big)
    answer = "(답):$$수식$$%srm cm$$/수식$$"%(radius_small)
    comment = "(해설)\n큰 원의 지름은 작은 원의 반지름의 $$수식$$%s$$/수식$$배 이므로\n"\
                "(작은 원의 반지름) $$수식$$=$$/수식$$ (큰 원의 지름)$$수식$$ div %s$$/수식$$\n"\
                "$$수식$$= %s div %s = %s(rm cm)$$/수식$$입니다."%(
                    numOfCircle323s*2,
                    numOfCircle323s*2,
                    diameter_big,numOfCircle323s*2,radius_small
                )
    #plt.show()
    svg = saveSvg()
    return stem, answer, comment, svg

# 3-2-3-21/22
def circle323_Stem_010():
    def circle323_Stem_006_22_drawCircle323s(ax,r=50,O=(0,0),n=2):
        answer_r = int(r/random.randint(4,20))
        temp_c = O
        setPoint(ax,[(temp_c[0]-r-3,temp_c[1])],['A'],['left'])
        for i in range(n):
            drawCircle(ax,temp_c,r)
            drawDot(ax,[temp_c],True)
            temp_c = (temp_c[0]+r,temp_c[1])
        setPoint(ax,[(temp_c[0],temp_c[1])],['B'],['right'])
        drawLine(ax,[(O[0]-r,O[1]),temp_c])
        drawDoubleArrow(ax,(O[0]-r,O[1]-r*1.5),(temp_c[0],temp_c[1]-r*1.5),'$%s\mathrm{cm}$'%(answer_r*(n+1)))
        drawLine(ax,[(O[0]-r,O[1]-r*1.7),(O[0]-r,O[1])],True)
        drawLine(ax,[(temp_c[0],temp_c[1]-r*1.7),temp_c],True)
        return answer_r,n
    def circle323_Stem_006_21_drawCircle323s(ax,r=50,O=(0,0),n=2):
        answer_r = int(r/random.randint(4,20))
        temp_c = O
        l_radius = [(temp_c[0]-r,temp_c[1]),O]
        setPoint(ax,[(temp_c[0]-r-3,temp_c[1])],['A'],['left'])
        drawArc(ax,l_radius,'top','$%s \mathrm{cm}$'%(answer_r))
        for i in range(n):
            drawCircle(ax,temp_c,r)
            drawDot(ax,[temp_c],True)
            temp_c = (temp_c[0]+r,temp_c[1])
        setPoint(ax,[(temp_c[0],temp_c[1])],['B'],['right'])
        drawLine(ax,[(O[0]-r,O[1]),temp_c])
        return answer_r,n
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
    numOfCircle323 = random.randint(3,5)
    #generate circle323
    radius = int(200/numOfCircle323)
    p_center = (radius + scale*-1,0)

    problem_option = random.randint(21,22) #type of problem
    if problem_option == 21:
        answer_r,numOfCircle323 = circle323_Stem_006_21_drawCircle323s(ax,radius,p_center,numOfCircle323)
        plt.axis('scaled')
        radius = answer_r
        total_length = radius*(numOfCircle323+1)
        stem = "반지름이 $$수식$$%srm cm$$/수식$$인 원 $$수식$$%s$$/수식$$개를 그림과 같이 서로 원의 "\
                "중심을 지나도록 겹쳐서 그렸습니다. "\
                "선분 AB의 길이는 몇 $$수식$$rm cm$$/수식$$인가요?" %(radius,numOfCircle323)
        answer = '(답):$$수식$$%srm cm$$/수식$$'%(total_length)
        comment = "(해설)\n원이 $$수식$$%s$$/수식$$개이므로 선분 AB의 길이는 반지름 $$수식$$%s$$/수식$$개의\n"\
                    "길이와 같습니다. \n"\
                    "따라서 선분 AB의 길이는 $$수식$$%s \\times %s = %s (rm cm)$$/수식$$입니다." %(
                        numOfCircle323,numOfCircle323+1,
                        radius,numOfCircle323+1,total_length
                    )
    elif problem_option == 22:
        radius,numOfCircle323 = circle323_Stem_006_22_drawCircle323s(ax,radius,p_center,numOfCircle323)
        plt.axis('scaled')
        numOfRadius = numOfCircle323 + 1
        total_length = radius*(numOfRadius)
        stem = "크기가 같은 원 $$수식$$%s$$/수식$$개를 그림과 같이 서로 원의 "\
                "중심을 지나도록 겹쳐서 그렸습니다. "\
                "원의 반지름은 몇 $$수식$$rm cm$$/수식$$인가요?"%(numOfCircle323)
        answer = '(답):$$수식$$%srm cm$$/수식$$'%(radius)
        comment = "(해설)\n선분 AB의 길이는 원의 반지름의 $$수식$$%s$$/수식$$배입니다. \n"%(numOfRadius)
        comment += "따라서 원의 반지름은 $$수식$$%s div %s = %s (rm cm)$$/수식$$입니다." %(total_length,numOfRadius,radius)

    #plt.show()
    svg= saveSvg()
    return stem, answer, comment, svg
