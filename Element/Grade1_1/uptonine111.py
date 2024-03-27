#-*- coding: utf-8 -*- 

import numpy as np
import io
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import cv2
import random
import os


PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../img/')

answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤"
}

answer_kodict = {
    0: "㉠",
    1: "㉡",
    2: "㉢",
    3: "㉣",
    4: "㉤"
}

def bool_jo(num):
    if type(num) == int:
        num = int(str(num)[-1])

        lee_nums = [0, 1, 3, 6, 7, 8]
        if num in lee_nums:
            return True
        else:
            return False
    else:
        num = str(num)[-1]
        num = ord(num)
        check = (num - 44032) % 28
        if check:
            return True
        return False


def proc_jo(num, check=0):
    if check < 0:
        # 은는
        if bool_jo(num):
            return "은"
        return "는"
    elif check == 0:
        # 이가
        if bool_jo(num):
            return "이"
        return "가"
    elif check == 2:
        # 와과
        if bool_jo(num):
            return "과"
        return "와"
    elif check == 3:
        # 이(라고)
        if bool_jo(num):
            return "이"
        return ""
    elif bool_jo(num):
        # 을를
        return "을"
    return "를"


def uptonine111_Stem_001():  # 1-1-1-04
    stem = "$$수식$${s1}$$/수식$$만큼 ○를 그린 것은 어느 것인가요?\n{one_one}$$표$${x1}$$/표$$\n{one_two}$$표$${x2}$$/표$$\n{one_three}$$표$${x3}$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "$$수식$${s1}$$/수식$${j1} {s2}이므로 ○를 $$수식$${s2}$$수식$$까지 세면서 그립니다.\n\n"

    s1 = np.random.randint(1, 5)
    slist = ["○", "○ ○", "○ ○ ○", "○ ○ ○ ○", "○ ○ ○ ○ ○"]

    y1 = slist[s1 - 1]
    slist.pop(s1 - 1)

    tmp = np.random.randint(1, 4)
    y2 = slist[tmp - 1]
    slist.pop(tmp - 1)
    tmp = np.random.randint(1, 3)
    y3 = slist[tmp - 1]

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [x1, x2, x3] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y1:
            correct_idx = idx
            break

    if s1 == 1:
        s2 = "하나"
    elif s1 == 2:
        s2 = "둘"
    elif s1 == 3:
        s2 = "셋"
    elif s1 == 4:
        s2 = "넷"
    elif s1 == 5:
        s2 = "다섯"

    j1 = proc_jo(s1, -1)

    one_one = "①"
    one_two = "②"
    one_three = "③"

    stem = stem.format(s1=s1, x1=x1, x2=x2, x3=x3, one_one=one_one,
                       one_two=one_two, one_three=one_three)  # 매핑시키기
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2, j1=j1)

    return stem, answer, comment


def uptonine111_Stem_002():  # 1-1-1-7
    stem = "틀린 것을 찾아 기호를 찾아 쓰세요.\n$$표$$ ㉠ {x1} \n㉡ {x2} \n㉢ {x3}$$/표$$"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "번호는 {sd}번입니다.\n\n"

    sa = ["일", "이", "삼", "사", "오"][np.random.randint(0, 5)]
    sb = ["한", "두", "세"][np.random.randint(0, 3)]
    sc = ["하나", "둘", "셋", "넷", "다섯"][np.random.randint(0, 5)]

    sd = ["배", "사과", "참외", "딸기"][np.random.randint(0, 4)]

    y1 = "우리 반은 %s반입니다." % (sa)
    y2 = "%s는 %s 개입니다." % (sd, sb)
    y3 = "번호는 %s 번입니다." % (sc)

    if sc == "하나":
        sd = "일"
    elif sc == "둘":
        sd = "이"
    elif sc == "셋":
        sd = "삼"
    elif sc == "넷":
        sd = "사"
    elif sc == "다섯":
        sd = "오"

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [x1, x2, x3] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y3:
            correct_idx = idx
            break

    stem = stem.format(x1=x1, x2=x2, x3=x3)  # 매핑시키기
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(sd=sd)

    return stem, answer, comment


def uptonine111_Stem_003():  # 1-1-1-11
    stem = "나타내는 수가 다른 하나를 찾아 써 보세요.\n$$표$${x1} {x2} {x3} {x4}$$/표$$"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "{x1}, {x2}, {x4} → {s1}\n" \
              "{x3} → {s2}\n\n"

    sa = ["하나", "둘", "셋", "넷", "다섯", "여섯", "일곱", "여덟", "아홉"]
    sb = ["일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    sc = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    r1 = np.random.randint(0, 5)
    r2 = r1

    while r1 == r2:
        r2 = np.random.randint(0, 5)

    y1 = sa[r1]
    y2 = sb[r1]
    y3 = sa[r2]
    y4 = sc[r1]
    y4 = "$$수식$$ %d $$/수식$$" % (y4)

    candidates = [y1, y2, y3, y4]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4] = candidates

    s1 = ""
    for i in range(0, r1 + 1):
        s1 = s1 + "●"

    s2 = ""
    for i in range(0, r2 + 1):
        s2 = s2 + "●"

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4)  # 매핑시키기
    answer = answer.format(a1=y3)
    comment = comment.format(x1=y1, x2=y2, x3=y3, x4=y4, s1=s1, s2=s2)

    return stem, answer, comment


def uptonine111_Stem_004():  # 1-1-1-14
    stem = "보기와 같이 어떤 수를 보고 만든 이야기입니다. 네모 안에 어떤 수를 써 보세요.\n$$표$$보기\n$$수식$${x1}$$/수식$$ → 우리 집은 $$수식$${x1}$$/수식$$층입니다.$$/표$$\n$$표$$$$수식$${boxblank}$$/수식$$ → {x2}{j1} {x3} 가지 {x4}{j2} 있습니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a1}$$/수식$${j3} 사용하여 실생활에서 사용되는 문장을 만든 것입니다.\n\n"

    sa = ["핸드폰", "옷", "책", "양말", "연필", "가방"][np.random.randint(0, 6)]
    sb = ["종류", "무늬", "모양"][np.random.randint(0, 3)]
    sc = ["한", "두", "세", "네", "다섯", "여섯", "일곱", "여덟", "아홉"]

    j1 = proc_jo(sa, 0)
    j2 = proc_jo(sb, 0)

    #boxblank = "$$수식$$BOX{````````}$$/수식$$"
    boxblank = "□"

    y1 = np.random.randint(1, 6)
    y2 = sa
    y3 = sc[np.random.randint(0, 5)]
    y4 = sb

    correct_idx = 0

    for idx, sdx in enumerate(sc):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y3:
            correct_idx = idx + 1
            break

    j3 = proc_jo(correct_idx, 1)

    stem = stem.format(x1=y1, x2=y2, x3=y3, x4=y4, j1=j1,
                       j2=j2, boxblank=boxblank)  # 매핑시키기
    answer = answer.format(a1=correct_idx)
    comment = comment.format(a1=correct_idx, j3=j3)

    return stem, answer, comment


def uptonine111_Stem_005():  # 1-1-1-18
    stem = "{sa}에 $$수식$${x1}$$/수식$$명의 학생이 한 줄로 서 있는데 그중에서 {wh}{j1} 앞에서 {sb}째에 서 있습니다. {wh}{j1} 뒤에서 몇째에 서 있을까요?\n"
    answer = "(정답)\n{a1}째\n"
    comment = "(해설)\n○를 $$수식$${x1}$$/수식$$개 그리고 앞으로 {sb}째에 색칠합니다.\n" \
              "$$수식$$LEFT ($$/수식$$앞$$수식$$ RIGHT )$$/수식$$ {sc} $$수식$$LEFT ($$/수식$$뒤$$수식$$RIGHT )$$/수식$$\n" \
              "뒤에서부터 순서를 세면 색칠한 것은 뒤에서 {a1}째에 서 있습니다.\n\n"

    sa = ["운동장", "교실", "놀이공원", "정류장", "복도"][np.random.randint(0, 5)]
    x1 = np.random.randint(2, 10)
    wh = ["현정이", "지수", "지환이", "은성이", "현수", "민경이"][np.random.randint(0, 6)]
    j1 = proc_jo(wh, -1)
    r1 = np.random.randint(0, x1 - 1)
    s_list = ["첫", "둘", "셋", "넷", "다섯", "여섯", "일곱", "여덟", "아홉"]
    sb = s_list[r1]
    a = x1 - r1 - 1
    a1 = s_list[a]

    sc = ""
    for i in range(0, x1):
        if i == r1:
            sc = sc + " ● "
        else:
            sc = sc + " ○ "

    stem = stem.format(sa=sa, x1=x1, wh=wh, j1=j1, sb=sb)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, sb=sb, sc=sc, a1=a1)

    return stem, answer, comment


def uptonine111_Stem_006():  # 1-1-1-19
    stem = "{wh1}네 모둠 학생 $$수식$$9$$/수식$$명이 한 줄로 서 있습니다. {wh1}{j1} {sa}째, {wh2}{j2} {sb}째에 서 있다면 {wh1}{j3} {wh2} 사이에는 몇 명이 서 있을까요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n차례 순서에는 {sa}째와 {sb}째 사이에는 {sc}가 있으므로 {sc}인 사람이 서 있습니다.\n" \
              "따라서 {wh1}{j3} {wh2} 사이에는 $$수식$${a1}$$/수식$$명이 서 있습니다.\n\n"

    wh1 = ["수진", "우중이", "종식이", "지훈이"][np.random.randint(0, 4)]
    wh2 = ["민영이", "수호", "유라", "민지"][np.random.randint(0, 4)]
    slist = ["첫", "둘", "셋", "넷", "다섯", "여섯", "일곱", "여덟", "아홉"]

    r1 = np.random.randint(0, 7)
    r2 = np.random.randint(r1 + 2, 9)
    sa = slist[r1]
    sb = slist[r2]
    j1 = proc_jo(wh1, -1)
    j2 = proc_jo(wh2, -1)
    j3 = proc_jo(wh1, 2)
    sc = ""

    for i in range(r1 + 1, r2):
        sc = sc + slist[i] + "째"
        if (i != r2 - 1):
            sc = sc + ", "

    a1 = r2 - r1 - 1

    stem = stem.format(wh1=wh1, wh2=wh2, j1=j1, j2=j2,
                       j3=j3, sa=sa, sb=sb)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(
        sa=sa, sb=sb, sc=sc, wh1=wh1, j3=j3, wh2=wh2, a1=a1)

    return stem, answer, comment


def uptonine111_Stem_007():  # 1-1-1-24
    stem = "수를 순서대로 바르게 쓴 사람은 누구인지 써 보세요.\n$$표$${x1}\n{x2}$$/표$$\n"
    answer = "(정답)\n{wh1}\n"
    comment = "(해설)\n$$수식$$1$$/수식$$부터 수를 순서대로 써 보면 \n" \
              "$$수식$$1$$/수식$$ - $$수식$$2$$/수식$$ - $$수식$$3$$/수식$$ - $$수식$$4$$/수식$$ - $$수식$$5$$/수식$$ - $$수식$$6$$/수식$$ - $$수식$$7$$/수식$$ - $$수식$$8$$/수식$$ - $$수식$$9$$/수식$$이므로 " \
              "수를 순서대로 바르게 쓴 학생은 {wh1}입니다.\n\n"

    wh1 = ["영수", "민아", "철수", "경아"][np.random.randint(0, 4)]
    wh2 = ["민주", "현주", "경수", "정은"][np.random.randint(0, 4)]

    r1 = np.random.randint(1, 6)
    r2 = np.random.randint(1, 6)

    s1 = " "
    for i in range(r1, r1 + 5):
        s1 = s1 + "$$수식$$" + str(i) + "$$/수식$$ "

    tmp = 0
    s2 = " "

    for i in range(r2, r2 + 5):
        if (tmp == 2):
            s2 = s2 + "$$수식$$" + str(i + 1) + "$$/수식$$ "
        elif (tmp == 3):
            s2 = s2 + "$$수식$$" + str(i - 1) + "$$/수식$$ "
        else:
            s2 = s2 + "$$수식$$" + str(i) + "$$/수식$$ "
        tmp = tmp + 1
        
    y1 = "{wh1} : {s1}".format(wh1=wh1, s1=s1)
    y2 = "{wh2} : {s2}".format(wh2=wh2, s2=s2)

    candidates = [y1, y2]
    np.random.shuffle(candidates)
    [x1, x2] = candidates

    stem = stem.format(x1=x1, x2=x2)  # 매핑시키기
    answer = answer.format(wh1=wh1)
    comment = comment.format(wh1=wh1)

    return stem, answer, comment


# 1-1-1-25
def uptonine111_Stem_008():
    stem = "{wh1}{j1} 수를 말하면 {wh2}{j2} 다음과 같이 거꾸로 세는 놀이를 하고 있습니다. {wh1}{j1} $$수식$${x1}$$/수식$${j3}라고 말했다면 {wh2}{j2} 대답해야 하는 수를 써 보세요.\n{wh1} : $$수식$${x2}$$/수식$$!\n{wh2} : {s1}\n{wh1} : $$수식$${x3}$$/수식$$!\n{wh2} : {s2}\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "{wh1}{j1} 말한 수를 거꾸로 세면 {s3}, {s4}이므로 {wh2}{j2} 말한 수는 {wh1}{j1} 말한 수를 거꾸로 센 수에서 말한 수를 제외한 모든 수를 쓰면 됩니다.\n" \
              "따라서 {wh1}{j1} $$수식$${x1}$$/수식$${j3}라고 말했으므로 $$수식$${x1}$$/수식$$부터 " \
              "순서를 거꾸로 하여 수를 세어 보면 {s5}이므로 {wh2}{j2} 대답해야 하는 수는 {a1}입니다.\n\n"

    wh1 = ["상현", "제희", "은지", "예원"][np.random.randint(0, 4)]
    wh2 = ["주희", "정환", "승협", "유리"][np.random.randint(0, 4)]

    j1 = proc_jo(wh1, 0)
    j2 = proc_jo(wh2, 0)

    x1 = np.random.randint(2, 10)
    x2 = np.random.randint(2, 10)
    x3 = np.random.randint(2, 10)

    j3 = proc_jo(x1, 3)

    while x1 == x2 or x1 == x3 or x2 == x3:
        x2 = np.random.randint(2, 10)
        x3 = np.random.randint(2, 10)

    s1 = ""
    s3 = "$$수식$$" + str(x2) + "$$/수식$$ - "

    for i in range(1, x2):
        s1 = s1 + "$$수식$$" + str(x2 - i) + "$$/수식$$, "
        s3 = s3 + "$$수식$$" + str(x2 - i) + "$$/수식$$ - "

    s1 = s1[0:-2]
    s3 = s3[0:-2]

    s2 = ""
    s4 = "$$수식$$" + str(x3) + "$$/수식$$ - "

    for i in range(1, x3):
        s2 = s2 + "$$수식$$" + str(x3 - i) + "$$/수식$$, "
        s4 = s4 + "$$수식$$" + str(x3 - i) + "$$/수식$$ - "

    s2 = s2[0:-2]
    s4 = s4[0:-2]

    s5 = "$$수식$$" + str(x1) + "$$/수식$$ - "
    a1 = ""

    for i in range(1, x1):
        a1 = a1 + "$$수식$$" + str(x1 - i) + "$$/수식$$, "
        s5 = s5 + "$$수식$$" + str(x1 - i) + "$$/수식$$ - "

    a1 = a1[0:-2]
    s5 = s5[0:-2]

    stem = stem.format(wh1=wh1, j1=j1, wh2=wh2, j2=j2, x1=x1,
                       x2=x2, x3=x3, s1=s1, s2=s2, j3=j3)
    answer = answer.format(a1=a1)
    comment = comment.format(wh1=wh1, j1=j1, wh2=wh2,
                             j2=j2, s3=s3, s4=s4, x1=x1, s5=s5, a1=a1, j3=j3)

    return stem, answer, comment


def uptonine111_Stem_009():  # 1-1-1-31
    stem = "{wh1}{j1} {wh2}{j2} 같은 건물에 살고 있습니다. {wh1}{j3} $$수식$${x1}$$/수식$$층보다 $$수식$${x2}$$/수식$$층 위에 살고, {wh2}{j2} {wh1}보다 $$수식$${x3}$$/수식$$층 위에 살고 있습니다. {wh2}{j2} 건물의 몇 층에 살고 있을까요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$층\n"
    comment = "(해설)\n" \
              "{wh1} : $$수식$${x1}$$/수식$$보다 $$수식$${x2}$$/수식$$ 큰 수 → $$수식$${x4}$$/수식$$ ⇒ $$수식$${x4}$$/수식$$층\n" \
              "{wh2} : $$수식$${x4}$$/수식$$보다 $$수식$${x3}$$/수식$$ 큰 수 → $$수식$${a1}$$/수식$$ ⇒ $$수식$${a1}$$/수식$$층\n\n"

    wh1 = ["지성이", "윤건이", "채원이", "승희"][np.random.randint(0, 4)]
    wh2 = ["성희", "도희", "한결이", "연주"][np.random.randint(0, 4)]

    j1 = proc_jo(wh1, 2)
    j2 = proc_jo(wh2, -1)
    j3 = proc_jo(wh1, -1)

    x1 = x2 = x3 = x4 = a1 = 10

    while a1 > 9:
        x1 = np.random.randint(1, 9)
        x2 = np.random.randint(1, 9)
        x3 = np.random.randint(1, 9)

        x4 = x1 + x2
        a1 = x4 + x3

    stem = stem.format(wh1=wh1, wh2=wh2, j1=j1, j2=j2,
                       j3=j3, x1=x1, x2=x2, x3=x3)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(wh1=wh1, wh2=wh2, x1=x1,
                             x2=x2, x3=x3, x4=x4, a1=a1)

    return stem, answer, comment


def uptonine111_Stem_010():  # 1-1-1-32
    stem = "{wh1}{j1} {s1}{j2} $$수식$${x1}$$/수식$$개 가지고 있었습니다. {wh2}{j3} 가지고 있던 {s1} 중에서 $$수식$${x2}$$/수식$$개를 {wh1}에게 주었더니 {wh1}{j4} {wh2}{j3} 가진 {s1}의 수가 같아졌습니다. 처음에 {wh2}{j3} 가지고 있던 {s1}{j6} 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n" \
              "{wh2}에게 {s1}{j2} $$수식$${x2}$$/수식$$개 받은 다음 {wh1}{j5} 가지고 있는 {s1}의 수는 $$수식$${x1}$$/수식$$보다 $$수식$${x2}$$/수식$$ 큰 수인 $$수식$${x3}$$/수식$$입니다. " \
              "이때 두 사람의 {s1}의 수가 같아졌으므로 {wh2}{j3} 가지고 있는 {s1}도 $$수식$${x3}$$/수식$$개 입니다. " \
              "따라서 처음에 {wh2}{j3} 가지고 있던 {s1}의 수는 $$수식$${x3}$$/수식$$보다 $$수식$${x2}$$/수식$$ 큰 수인 $$수식$${a1}$$/수식$$이므로 $$수식$${a1}$$/수식$$개입니다.\n\n"

    wh1 = ["은영이", "현경이", "성준이", "강훈이"][np.random.randint(0, 4)]
    wh2 = ["영훈이", "선화", "윤주", "민지"][np.random.randint(0, 4)]
    s1 = ["사탕", "초콜릿", "구슬", "사과", "머리끈"][np.random.randint(0, 5)]

    j1 = proc_jo(wh1, -1)
    j2 = proc_jo(s1, 1)
    j3 = proc_jo(wh2, 0)
    j4 = proc_jo(wh1, 2)
    j5 = proc_jo(wh1, 0)
    j6 = proc_jo(s1, -1)

    a1 = x1 = x2 = 9

    while a1 != x1 + x2 + x2 or a1 > 9:
        x1 = np.random.randint(1, 10)
        x2 = np.random.randint(1, 10)

        x3 = x1 + x2
        a1 = x3 + x2

    stem = stem.format(wh1=wh1, wh2=wh2, j1=j1, j2=j2, j3=j3,
                       j4=j4, j6=j6, x1=x1, x2=x2, s1=s1)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(wh1=wh1, wh2=wh2, j2=j2,
                             j3=j3, j5=j5, x1=x1, x2=x2, x3=x3, s1=s1, a1=a1)

    return stem, answer, comment


def uptonine111_Stem_011():  # 1-1-1-35
    stem = "{s1}{j1} $$수식$${x1}$$/수식$$개 있었습니다. {wh1}{j2} {s1}{j3} {s2} 먹었습니다. 남은 {s1}{j4} 몇 개일까요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n" \
              "{s1}{j3} {s2} 먹었으므로 남은 {s1}{j4} $$수식$${a1}$$/수식$$개입니다.\n\n"

    s1 = ["사과", "배", "사탕", "과자"][np.random.randint(0, 4)]
    x1 = np.random.randint(1, 10)
    wh1 = ["진영이", "현주", "여름이", "정원이"][np.random.randint(0, 4)]
    s_list = ["모두", "한 개", "두 개", "세 개", "네 개",
              "다섯 개", "여섯 개", "일곱 개", "여덟 개", "아홉 개"]

    j1 = proc_jo(s1, 0)
    j2 = proc_jo(wh1, 0)
    j3 = proc_jo(s1, 1)
    j4 = proc_jo(s1, -1)

    r1 = np.random.randint(0, x1)
    s2 = s_list[r1]

    if r1 == 0:
        a1 = 0
    else:
        a1 = x1 - r1

    stem = stem.format(s1=s1, s2=s2, wh1=wh1, x1=x1,
                       j1=j1, j2=j2, j3=j3, j4=j4)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(s1=s1, s2=s2, j3=j3, j4=j4, a1=a1)

    return stem, answer, comment


def uptonine111_Stem_012():  # 1-1-1-38
    stem = "{s1}{j1} {wh1}{j2} $$수식$${x1}$$/수식$$권 읽었고, {wh2}{j3} $$수식$${x2}$$/수식$$권 읽었습니다. {s1}{j1} 더 많이 읽은 사람은 누구일까요?\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n{s1}의 수를 ○로 나타냅니다.\n" \
              "{wh1}{j4} 읽은 {s1}의 수 : {s2}\n" \
              "{wh2}{j5} 읽은 {s1}의 수 : {s3}\n" \
              "○의 수는 {a1}{j5} 더 많으므로 더 많이 읽은 사람은 {a1}입니다.\n\n"

    s1 = ["동화책", "소설책", "그림책", "백과사전", "만화책"][np.random.randint(0, 5)]
    wh1 = ["지수", "지환이", "선빈이", "찬규"][np.random.randint(0, 4)]
    wh2 = ["민호", "동현이", "희수", "연희"][np.random.randint(0, 4)]

    j1 = proc_jo(s1, 1)
    j2 = proc_jo(wh1, -1)
    j3 = proc_jo(wh2, -1)
    j4 = proc_jo(wh1, 0)

    x1 = np.random.randint(1, 10)
    x2 = np.random.randint(1, 10)

    while x1 == x2:
        x2 = np.random.randint(1, 10)

    s2 = s3 = ""

    for i in range(0, x1):
        s2 = s2 + "○"
    for i in range(0, x2):
        s3 = s3 + "○"

    if x1 > x2:
        a1 = wh1
    else:
        a1 = wh2

    j5 = proc_jo(a1, 0)
    
    a1 = a1.replace('이', '')

    stem = stem.format(s1=s1, wh1=wh1, wh2=wh2, j1=j1,
                       j2=j2, j3=j3, x1=x1, x2=x2)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(wh1=wh1, wh2=wh2, s1=s1,
                             s2=s2, s3=s3, j4=j4, j5=j5, a1=a1)

    return stem, answer, comment


def uptonine111_Stem_013():  # 1-1-1-39
    stem = "수로 나타내었을 때 가장 작은 수는 어느 것인지 숫자로 써 보세요.\n$$표$$ {x1}, {x2}, {x3} $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n{x1} → $$수식$${x4}$$/수식$$, {x2} → $$수식$${x5}$$/수식$$, {x3} → $$수식$${x6}$$/수식$$\n" \
              "수를 순서대로 썼을 때 가장 앞에 있는 수가 가장 작은 수입니다.\n" \
              "수를 순서대로 쓰면 $$수식$${y4}$$/수식$$, $$수식$${y5}$$/수식$$, $$수식$${y6}$$/수식$$이므로 가장 작은 수는 {a1}입니다.\n\n"

    s_list = ["하나", "둘", "셋", "넷", "다섯", "여섯", "일곱", "여덟", "아홉"]
    r1 = np.random.randint(0, 7)

    y4 = r1 + 1
    y5 = r1 + 2
    y6 = r1 + 3

    candidates = [y4, y5, y6]
    np.random.shuffle(candidates)
    [x4, x5, x6] = candidates

    y1 = s_list[x4 - 1]
    y2 = s_list[x5 - 1]
    y3 = s_list[x6 - 1]

    a1 = s_list[y4 - 1]

    stem = stem.format(x1=y1, x2=y2, x3=y3)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1=y1, x2=y2, x3=y3, x4=x4,
                             x5=x5, x6=x6, y4=y4, y5=y5, y6=y6, a1=a1)

    return stem, answer, comment


def uptonine111_Stem_014():  # 1-1-1-41
    stem = "$$수식$$0$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 중에서 □ 안에 공통으로 들어갈 수 있는 수는 모두 몇 개일까요?\n$$표$$・ □는 $$수식$${x1}$$/수식$$보다 큽니다.\n・ □는 $$수식$${x2}$$/수식$$보다 $$수식$${x3}$$/수식$$ 큰 수보다 작습니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "・ □는 $$수식$${x1}$$/수식$$보다 크므로 □ 안에 들어갈 수 있는 수는 {s1}입니다.\n" \
              "・ $$수식$${x2}$$/수식$$보다 $$수식$${x3}$$/수식$$ 큰 수는 $$수식$${x4}$$/수식$$이고 □는 $$수식$${x4}$$/수식$$보다 작으므로 □ 안에 들어갈 수 있는 수는 {s2}입니다.\n" \
              "따라서 □ 안에 공통으로 들어갈 수 있는 수는 {s3}로 모두 $$수식$${a1}$$/수식$$개입니다.\n\n"

    x1 = np.random.randint(0, 10)
    x2 = np.random.randint(0, 10)
    x3 = np.random.randint(1, 10)
    x4 = x2 + x3

    while x1 > x2 + x3 or x4 > 9:
        x1 = np.random.randint(0, 10)
        x2 = np.random.randint(0, 10)
        x3 = np.random.randint(1, 10)
        x4 = x2 + x3

    s1 = ""

    for i in range(x1 + 1, 10):
        s1 = s1 + "$$수식$$" + str(i) + "$$/수식$$, "
    s1 = s1[0:-2]

    s2 = ""

    for i in range(0, x4):
        s2 = s2 + "$$수식$$" + str(i) + "$$/수식$$, "

    s2 = s2[0:-2]

    s3 = ""

    a1 = 0

    for i in range(x1 + 1, x4):
        s3 = s3 + "$$수식$$" + str(i) + "$$/수식$$, "
        a1 = a1 + 1

    s3 = s3[0:-2]

    if a1 == 0:
        s3 = "없으므"

    stem = stem.format(x1=x1, x2=x2, x3=x3)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4,
                             s1=s1, s2=s2, s3=s3, a1=a1)

    return stem, answer, comment


def uptonine111_Stem_015():  # 1-1-1-42
    stem = "다음 두 조건을 만족하는 수를 모두 구하세요.\n$$표$$(가) $$수식$${x1}$$/수식$${j1} $$수식$${x2}$$/수식$$ 사이에 있는 수입니다.\n(나) $$수식$${x3}$$/수식$$보다 작은 수입니다.$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "$$수식$${x1}$$/수식$$부터 $$수식$${x2}$$/수식$$까지의 수를 순서대로 쓰면 {s1}이므로 $$수식$${x1}$$/수식$${j1} $$수식$${x2}$$/수식$$ 사이에 있는 수는 {s2}입니다. " \
              "이 중에서 $$수식$${x3}$$/수식$$보다 작은 수는 {a1}입니다.\n" \
              "따라서 두 조건을 만족하는 수는 {a1}입니다.\n\n"

    x1 = np.random.randint(0, 5)
    x2 = np.random.randint(x1 + 5, 10)
    x3 = x1 + 4

    s1 = "$$수식$$" + str(x1) + "$$/수식$$, "
    s2 = ""

    for i in range(x1 + 1, x2 + 1):
        s1 = s1 + "$$수식$$" + str(i) + "$$/수식$$, "
        s2 = s2 + "$$수식$$" + str(i) + "$$/수식$$, "

    s1 = s1[0:-2]
    s2 = s2[0:-18]

    a1 = ""

    for i in range(x1 + 1, x3):
        a1 = a1 + "$$수식$$" + str(i) + "$$/수식$$, "

    a1 = a1[0:-2]
    j1 = proc_jo(x1, 2)

    stem = stem.format(x1=x1, x2=x2, x3=x3, j1=j1)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, s1=s1, j1=j1, s2=s2, x3=x3, a1=a1)

    return stem, answer, comment


#font_name = font_manager.FontProperties(fname="C:/WINDOWS/FONTS/MALGUN.TTF").get_name()
#rc("font", family=font_name)  # For Windows

answer_num_read = ["하나", "둘", "셋", "넷", "다섯", "여섯", "일곱", "여덟", "아홉"]

# svg파일을 문자열로 반환하는 함수


def saveSvg():
    file = io.StringIO()
    plt.savefig(file, format="svg", dpi=300)
    file.seek(0)
    svg_data = file.getvalue()

    return svg_data


def saveImg(image, image_wpath="image.jpg"):
    cv2.imwrite(image_wpath, image)


def load_img(image_path):
    path = np.fromfile(image_path, np.uint8)
    #img = cv2.imread(image_path)
    img = cv2.imdecode(path, cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = cv2.resize(img, (0, 0), None, .5, .5)

    return img


def num2hangul(num, version="일"):
    if version == "일":
        return {1: "일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}[num]
    elif version == "하나":
        return {1: "하나", 2: "둘", 3: "셋", 4: "넷", 5: "다섯", 6: "여섯", 7: "일곱", 8: "여덟", 9: "아홉"}[num]
    elif version == "첫째":
        return {1: "첫째", 2: "둘째", 3: "셋째", 4: "넷째", 5: "다섯째", 6: "여섯째", 7: "일곱째", 8: "여덟째", 9: "아홉째"}[num]



def check_jongsung(word):
    return (ord(word[-1]) - ord("가")) % 28 > 0


def num2circledConsonant(num):
    return {0: "㉠", 1: "㉡", 2: "㉢"}[num]

# 완료


def uptonine111_Stem_016():
    plt.rc('font', family='NanumGothic')
    
    # concat을 위해 정사각형으로 padding 넣어주는 함수
    def uptoine111_Stem_016_padding(set_size, img):
        h, w, c = img.shape

        delta_w = set_size - w
        delta_h = set_size - h
        top, bottom = delta_h//2, delta_h-(delta_h//2)
        left, right = delta_w//2, delta_w-(delta_w//2)

        new_img = cv2.copyMakeBorder(
            img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[255, 255, 255])

        return new_img

    # 공 이미지 3개의 크기를 같게 만들어주는 함수
    def uptonine111_Stem_016_resize(baseball, soccer, volley):
        baseball_h, baseball_w, baseball_c = baseball.shape
        soccer_h, soccer_w, soccer_c = soccer.shape
        volley_h, volley_w, volley_c = volley.shape

        max_h = max(baseball_h, soccer_h, volley_h)
        max_w = max(baseball_w, soccer_w, volley_w)

        if max_h < max_w:
            set_size = max_w
        else:
            set_size = max_h

        baseball = uptoine111_Stem_016_padding(set_size, baseball)
        soccer = uptoine111_Stem_016_padding(set_size, soccer)
        volley = uptoine111_Stem_016_padding(set_size, volley)

        return baseball, soccer, volley

    # 숫자 선택
    answer_num_read = ["하나", "둘", "셋", "넷", "다섯"]

    num_baseball, num_soccer = np.random.choice(
        np.arange(1, 5), size=2, replace=False)
    num_volleyball = 10 - num_baseball - num_soccer

    # 공 이미지 만들 준비
    img_list = ["baseball" for x in range(num_baseball)]
    img_list += ["soccer" for x in range(num_soccer)]
    img_list += ["volley" for x in range(num_volleyball)]
    np.random.shuffle(img_list)

    # 숫자에 맞게 이미지 가공 및 저장
    baseball = load_img(
        PATH + "uptonine111_Stem_003_img_baseball.jpg")
    soccer = load_img(
        PATH + "uptonine111_Stem_003_img_soccer.jpg")
    volleyball = load_img(
        PATH + "uptonine111_Stem_003_img_volleyball.jpg")

    # 정사각형으로 이미지 사이즈 통일
    baseball, soccer, volleyball = uptonine111_Stem_016_resize(
        baseball, soccer, volleyball)

    # image concat
    img1, img = None, None
    for i, img_name in enumerate(img_list):
        if i == 0:
            if img_name == "baseball":
                img = baseball
            elif img_name == "soccer":
                img = soccer
            else:
                img = volleyball
        elif i == 5:
            img1 = img
            if img_name == "baseball":
                img = baseball
            elif img_name == "soccer":
                img = soccer
            else:
                img = volleyball
        else:
            if img_name == "baseball":
                img = np.concatenate((img, baseball), axis=1)
            elif img_name == "soccer":
                img = np.concatenate((img, soccer), axis=1)
            else:
                img = np.concatenate((img, volleyball), axis=1)

    img = np.concatenate((img, img1), axis=0)

    plt.imshow(img)
    plt.axis("off")

    svg = saveSvg()
    plt.clf()
    
    # 정답으로 쓸 공 선택
    answer_dict = {"야구공": num_baseball,
                   "축구공": num_soccer, "배구공": num_volleyball}
    answer_dict.pop(np.random.choice(list(answer_dict.keys())))

    answer_list = []
    comment_list = []
    for name in answer_dict:
        answer_list.append(answer_dict[name])
        comment_list.append("%s을 세어 보면 %s이므로 $$수식$$%s$$/수식$$ 입니다." % (name, ", ".join(
            answer_num_read[:answer_dict[name]]), answer_dict[name]))

    stem = "수를 세어 □안에 알맞은 수를 써넣으세요.\n" \
        "{b1} : {boxblank}, {b2} : {boxblank}"
        
    boxblank = "$$수식$$BOX{　　}$$/수식$$"
    stem = stem.format(b1=list(answer_dict.keys())[0], b2=list(answer_dict.keys())[1], boxblank=boxblank)
    answer = "(정답) $$수식$$%s$$/수식$$, $$수식$$%s$$/수식$$" % (answer_list[0], answer_list[1])
    comment = "(해설)" + " \n".join(comment_list)

    return stem, answer, comment, svg

# 완료


def uptonine111_Stem_017():
    plt.rc('font', family='NanumGothic')
    def uptonine111_Stem_017_setting():
        # 숫자 선택
        stem_figure_num = np.random.randint(2, 5+1)

        # 숫자에 맞게 이미지 가공 및 저장
        img = load_img(
            PATH + "uptonine111_Stem_009_img_scissor.jpg")
        img_concat = img
        for i in range(stem_figure_num-1):
            img_concat = np.concatenate((img_concat, img), axis=1)

        # 문제, 정답, 해설에 필요한 변수 세팅
        stem_list = [stem_figure_num]
        answer_list = [num2hangul(stem_figure_num, "하나"),
                       num2hangul(stem_figure_num, "일")]
        comment_list = [", ".join(answer_num_read[:stem_figure_num])]

        return stem_list, answer_list, comment_list, img_concat

    # 문제, 정답, 해설에 필요한 변수 가져오기
    stem_list, answer_list, comment_list, img = uptonine111_Stem_017_setting()

    josa_ans01 = "은" if check_jongsung(answer_list[-1]) else "는"
    josa_ans02 = "이라고" if check_jongsung(answer_list[0]) else "라고"

    stem = "가위의 수를 세어 보고 두 가지 방법으로 읽어 보세요."
    answer = "(정답)" + ", ".join(answer_list)
    comment = "(해설)가위를 세어 보면 %s이므로 $$수식$$%s$$/수식$$입니다.\n" % (answer_list[0], stem_list[0])
    comment += "$$수식$$%s$$/수식$$%s %s 또는 %s%s 읽습니다." % (
        stem_list[0], josa_ans01, answer_list[0], answer_list[1], josa_ans02)

    plt.imshow(img)
    plt.axis("off")
    
    svg = saveSvg()
    plt.clf()
    
    return stem, answer, comment, svg

# 완료


def uptonine111_Stem_018():
    plt.rc('font', family='NanumGothic')
    answer_str = ["㉠", "㉡", "㉢"]
    def uptonine111_Stem_018_svg(stem_nums, stem_figures):
        # 표를 만들어 보기 입력
        fig, axs = plt.subplots(3, figsize=(3, 1.5), gridspec_kw={"hspace": 0})
        data = [["㉠", num2hangul(stem_nums[0], "첫째"), "→", stem_figures[0]],
                ["㉡", num2hangul(stem_nums[1], "첫째"), "→", stem_figures[1]],
                ["㉢", num2hangul(stem_nums[2], "첫째"), "→", stem_figures[2]]]

        for i, ax in enumerate(axs):
            ax.text(0.05, 0.5, " ".join(
                data[i]), horizontalalignment="left", verticalalignment="center")
            ax.set(xticks=[], yticks=[])

        svg_data = saveSvg()

        return svg_data

    stem_nums = np.random.choice(np.arange(2, 10), size=4, replace=False)
    false_num = stem_nums[-1]
    stem_nums = stem_nums[:-1]
    answer_index = np.random.randint(3)

    # ㄱ, ㄴ, ㄷ에 들어갈 보기 생성
    stem_figure = np.random.choice(["☆★", "♡♥", "◇◆"])
    stem_figures = []
    for i, sn in enumerate(stem_nums):
        stem_figure_str = [stem_figure[0]] * 9
        if i == answer_index:
            stem_figure_str[false_num-1] = stem_figure[1]
            stem_figures.append("".join(stem_figure_str))
        else:
            stem_figure_str[sn-1] = stem_figure[1]
            stem_figures.append("".join(stem_figure_str))

    svg = uptonine111_Stem_018_svg(stem_nums, stem_figures)

    stem = "순서에 맞게 색칠한 것입니다. 잘못 색칠한 것을 찾아 기호를 써 보세요."
    answer = "(정답) " + num2circledConsonant(answer_index) + "\n"
    print(answer)
    comment = "(해설) %s은 %s 번에 색칠이 되어 있어야 하는데 %s 번에 색칠되어 있습니다." % (
        answer_str[answer_index], num2hangul(stem_nums[answer_index], "첫째"), num2hangul(false_num, "첫째"))
    
    plt.clf()

    return stem, answer, comment, svg

# 완료


def uptonine111_Stem_019():
    plt.rc('font', family='NanumGothic')
    # 문제, 정답, 해설에 필요한 변수 세팅
    index = np.random.randint(0, 7)
    answer_result = sorted(list(np.arange(2, 10)), reverse=True)[index]
    answer_hangul = num2hangul(index+1, "첫째")
    hangul_list = [num2hangul(num, "첫째") for num in range(1, 10)]

    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 카드를 $$수식$$9$$/수식$$부터 거꾸로 놓으려고 합니다." \
           " 카드를 거꾸로 놓았을 때 %s로 놓일 수 카드의 수를 써 보세요." % answer_hangul
    answer = "(정답)$$수식$$%s$$/수식$$" % answer_result
    comment = "(해설)$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 카드를 $$수식$$9$$/수식$$부터 거꾸로 놓으면 \n"
    comment += "%s이므로\n%s로 놓인 수 카드의 수는 $$수식$$%s$$/수식$$입니다." % (
        ", ".join(hangul_list), answer_hangul, answer_result)

    return stem, answer, comment

# 완료


def uptonine111_Stem_020():
    plt.rc('font', family='NanumGothic')
    car_num = np.random.randint(1, 8)
    answer_result = car_num + 1

    car = load_img(
        PATH + "uptonine111_Stem_028_img_car.jpg")

    img = car
    
    for i in range(car_num-1):
        #if i == 0:
        #    img = car
        img = np.concatenate((img, car), axis=1)

    # 문제, 정답, 해설에 필요한 변수 세팅
    stem = "자동차의 수보다 $$수식$$1$$/수식$$큰 수는 얼마인가요?"
    answer = "(정답)$$수식$$%s$$/수식$$" % answer_result
    comment = "(해설)자동차의 수를 세어 보면 %s이므로 자동차의 수는 $$수식$$%s$$/수식$$입니다.\n" % (
        num2hangul(car_num, "하나"), car_num)
    comment += "따라서 자동차의 수보다 $$수식$$1$$/수식$$큰 수는 $$수식$$%s$$/수식$$보다 $$수식$$1$$/수식$$ 큰 수인 $$수식$$%s$$/수식$$입니다." % (
        car_num, answer_result)
    
    plt.imshow(img)
    plt.axis("off")
    
    svg = saveSvg()
    plt.clf()
    
    return stem, answer, comment, svg

# 완료


def uptonine111_Stem_021():
    plt.rc('font', family='NanumGothic')
    img = load_img(
        PATH + "uptonine111_Stem_029_img_input.jpg")

    num1, num2 = sorted(np.random.choice(np.arange(2, 9+1), 2, False))
    ans_num1, ans_num2 = num1-1, num2-1

    stem = "□ 안에 알맞은 수를 써넣으세요.\n"
    stem += "$$표$$$$수식$$%s$$/수식$$보다 $$수식$$1$$/수식$$ 작은 수는 $$수식$$BOX{`①`}$$/수식$$이고,\n$$수식$$BOX{`②`}$$/수식$$보다 " \
            "$$수식$$1$$/수식$$ 작은 수는 $$수식$$%s$$/수식$$입니다.$$/표$$" % (num1, ans_num2)

    answer = "(정답)$$수식$$%s$$/수식$$, $$수식$$%s$$/수식$$" % (ans_num1, num2)

    comment = "(해설)수의 순서에서 $$수식$$%s$$/수식$$ 바로 앞에 있는 수는 $$수식$$%s$$/수식$$이고, $$수식$$%s$$/수식$$ 바로 뒤에 수는 $$수식$$%s$$/수식$$입니다.\n" % (
        ans_num1, num1, num2, ans_num2)
    comment += "따라서 $$수식$$%s$$/수식$$보다 $$수식$$1$$/수식$$ 작은 수는 $$수식$$%s$$/수식$$이고, " \
               "$$수식$$%s$$/수식$$보다 $$수식$$1$$/수식$$ 작은 수는 $$수식$$%s$$/수식$$입니다." % (
                   num1, ans_num1, num2, ans_num2)
               
    plt.imshow(img)
    plt.axis("off")
    
    svg = saveSvg()
    plt.clf()
    
    return stem, answer, comment, svg
print(uptonine111_Stem_021())
# 완료


def uptonine111_Stem_022():
    fruit = np.random.choice(["사과", "딸기", "토마토"], 1)[0]
    num = np.random.randint(2, 9+1)
    person = np.random.choice(["진영", "민수", "지훈"], 1)[0]

    josa1 = "이" if check_jongsung(fruit) else "가"
    josa2 = "이가" if check_jongsung(person) else "가"
    josa3 = "을" if check_jongsung(fruit) else "를"
    josa4 = "은" if check_jongsung(fruit) else "는"

    stem = "%s%s $$수식$$%s$$/수식$$개 있었습니다. %s%s %s%s 모두 먹었습니다. 남은 %s%s 몇 개일까요?" % (
        fruit, josa1, num, person, josa2, fruit, josa3, fruit, josa4
    )
    answer = "(정답)$$수식$$0$$/수식$$개"
    comment = "(해설)%s%s 모두 먹었으므로 남은 %s%s 없습니다." % (fruit, josa3, fruit, josa4)

    return stem, answer, comment


def uptonine111_Stem_023():  # 1-1-1-04
    stem = "$$수식$${s1}$$/수식$$만큼 ○를 그린 것은 어느 것인가요?\n{one_one}$$표$${x1}$$/표$$\n{one_two}$$표$${x2}$$/표$$\n{one_three}$$표$${x3}$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "$$수식$${s1}$$/수식$${j1} {s2}이므로 ○를 $$수식$${s2}$$수식$$까지 세면서 그립니다.\n\n"

    s1 = np.random.randint(1, 9)
    slist = ["○", "○ ○", "○ ○ ○", "○ ○ ○ ○", "○ ○ ○ ○ ○", "○ ○ ○ ○ ○ ○", "○ ○ ○ ○ ○ ○ ○", "○ ○ ○ ○ ○ ○ ○ ○", "○ ○ ○ ○ ○ ○ ○ ○ ○"]

    y1 = slist[s1 - 1]
    slist.pop(s1 - 1)

    tmp = np.random.randint(1, 8)
    y2 = slist[tmp - 1]
    slist.pop(tmp - 1)
    tmp = np.random.randint(1, 7)
    y3 = slist[tmp - 1]

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [x1, x2, x3] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y1:
            correct_idx = idx
            break

    if s1 == 1:
        s2 = "하나"
    elif s1 == 2:
        s2 = "둘"
    elif s1 == 3:
        s2 = "셋"
    elif s1 == 4:
        s2 = "넷"
    elif s1 == 5:
        s2 = "다섯"
    elif s1 == 6:
        s2 = "여섯"
    elif s1 == 7:
        s2 = "일곱"
    elif s1 == 8:
        s2 = "여덞"
    elif s1 == 9:
        s2 = "아홉"

    j1 = proc_jo(s1, -1)

    one_one = "①"
    one_two = "②"
    one_three = "③"

    stem = stem.format(s1=s1, x1=x1, x2=x2, x3=x3, one_one=one_one,
                       one_two=one_two, one_three=one_three)  # 매핑시키기
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2, j1=j1)

    return stem, answer, comment


def uptonine111_Stem_024():  # 1-1-1-11
    stem = "나타내는 수가 다른 하나를 찾아 써 보세요.\n$$표$${x1} {x2} {x3} {x4}$$/표$$"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "{x1}, {x2}, {x4} → {s1}\n" \
              "{x3} → {s2}\n\n"

    sa = ["하나", "둘", "셋", "넷", "다섯", "여섯", "일곱", "여덟", "아홉"]
    sb = ["일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    sc = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    r1 = np.random.randint(0, 9)
    r2 = r1

    while r1 == r2:
        r2 = np.random.randint(0, 9)

    y1 = sa[r1]
    y2 = sb[r1]
    y3 = sa[r2]
    y4 = sc[r1]
    y4 = "$$수식$$ %d $$/수식$$" % (y4)

    candidates = [y1, y2, y3, y4]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4] = candidates

    s1 = ""
    for i in range(0, r1 + 1):
        s1 = s1 + "●"

    s2 = ""
    for i in range(0, r2 + 1):
        s2 = s2 + "●"

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4)  # 매핑시키기
    answer = answer.format(a1=y3)
    comment = comment.format(x1=y1, x2=y2, x3=y3, x4=y4, s1=s1, s2=s2)

    return stem, answer, comment


def uptonine111_Stem_025():  # 1-1-1-14
    stem = "보기와 같이 어떤 수를 보고 만든 이야기입니다. 네모 안에 어떤 수를 써 보세요.\n$$표$$보기\n$$수식$${x1}$$/수식$$ → 우리 집은 $$수식$${x1}$$/수식$$층입니다.$$/표$$\n$$표$$$$수식$${boxblank}$$/수식$$ → {x2}{j1} {x3} 가지 {x4}{j2} 있습니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a1}$$/수식$${j3} 사용하여 실생활에서 사용되는 문장을 만든 것입니다.\n\n"

    sa = ["핸드폰", "옷", "책", "양말", "연필", "가방"][np.random.randint(0, 6)]
    sb = ["종류", "무늬", "모양"][np.random.randint(0, 3)]
    sc = ["한", "두", "세", "네", "다섯", "여섯", "일곱", "여덟", "아홉"]

    j1 = proc_jo(sa, 0)
    j2 = proc_jo(sb, 0)

    #boxblank = "$$수식$$BOX{````````}$$/수식$$"
    boxblank = "□"

    y1 = np.random.randint(1, 10)
    y2 = sa
    y3 = sc[np.random.randint(0, 9)]
    y4 = sb

    correct_idx = 0

    for idx, sdx in enumerate(sc):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y3:
            correct_idx = idx + 1
            break

    j3 = proc_jo(correct_idx, 1)

    stem = stem.format(x1=y1, x2=y2, x3=y3, x4=y4, j1=j1,
                       j2=j2, boxblank=boxblank)  # 매핑시키기
    answer = answer.format(a1=correct_idx)
    comment = comment.format(a1=correct_idx, j3=j3)

    return stem, answer, comment




answer_num_read = ["하나", "둘", "셋", "넷", "다섯", "여섯", "일곱", "여덟", "아홉"]

# svg파일을 문자열로 반환하는 함수


def saveSvg():
    file = io.StringIO()
    plt.savefig(file, format="svg", dpi=300)
    file.seek(0)
    svg_data = file.getvalue()

    return svg_data


def saveImg(image, image_wpath="image.jpg"):
    cv2.imwrite(image_wpath, image)


def load_img(image_path):
    path = np.fromfile(image_path, np.uint8)
    #img = cv2.imread(image_path)
    img = cv2.imdecode(path, cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = cv2.resize(img, (0, 0), None, .5, .5)

    return img


def num2hangul(num, version="일"):
    if version == "일":
        return {1: "일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}[num]
    elif version == "하나":
        return {1: "하나", 2: "둘", 3: "셋", 4: "넷", 5: "다섯", 6: "여섯", 7: "일곱", 8: "여덟", 9: "아홉"}[num]
    elif version == "첫째":
        return {1: "첫째", 2: "둘째", 3: "셋째", 4: "넷째", 5: "다섯째", 6: "여섯째", 7: "일곱째", 8: "여덟째", 9: "아홉째"}[num]


def check_jongsung(word):
    return (ord(word[-1]) - ord("가")) % 28 > 0


def num2circledConsonant(num):
    return {0: "㉠", 1: "㉡", 2: "㉢"}[num]

# 완료


def uptonine111_Stem_026():
    plt.rc('font', family='NanumGothic')
    
    # concat을 위해 정사각형으로 padding 넣어주는 함수
    def uptoine111_Stem_016_padding(set_size, img):
        h, w, c = img.shape

        delta_w = set_size - w
        delta_h = set_size - h
        top, bottom = delta_h//2, delta_h-(delta_h//2)
        left, right = delta_w//2, delta_w-(delta_w//2)

        new_img = cv2.copyMakeBorder(
            img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[255, 255, 255])

        return new_img

    # 공 이미지 3개의 크기를 같게 만들어주는 함수
    def uptonine111_Stem_016_resize(baseball, soccer, volley):
        baseball_h, baseball_w, baseball_c = baseball.shape
        soccer_h, soccer_w, soccer_c = soccer.shape
        volley_h, volley_w, volley_c = volley.shape

        max_h = max(baseball_h, soccer_h, volley_h)
        max_w = max(baseball_w, soccer_w, volley_w)

        if max_h < max_w:
            set_size = max_w
        else:
            set_size = max_h

        baseball = uptoine111_Stem_016_padding(set_size, baseball)
        soccer = uptoine111_Stem_016_padding(set_size, soccer)
        volley = uptoine111_Stem_016_padding(set_size, volley)

        return baseball, soccer, volley

    # 숫자 선택
    answer_num_read = ["하나", "둘", "셋", "넷", "다섯", "여섯", "일곱", "여덟", "아홉"]

    num_baseball, num_soccer = np.random.choice(
        np.arange(1, 5), size=2, replace=False)
    num_volleyball = 10 - num_baseball - num_soccer

    # 공 이미지 만들 준비
    img_list = ["baseball" for x in range(num_baseball)]
    img_list += ["soccer" for x in range(num_soccer)]
    img_list += ["volley" for x in range(num_volleyball)]
    np.random.shuffle(img_list)

    # 숫자에 맞게 이미지 가공 및 저장
    baseball = load_img(
        "/home/boin-service/Visang/Element/img/uptonine111_Stem_003_img_baseball.jpg")
    soccer = load_img(
        "/home/boin-service/Visang/Element/img/uptonine111_Stem_003_img_soccer.jpg")
    volleyball = load_img(
        "/home/boin-service/Visang/Element/img/uptonine111_Stem_003_img_volleyball.jpg")

    # 정사각형으로 이미지 사이즈 통일
    baseball, soccer, volleyball = uptonine111_Stem_016_resize(
        baseball, soccer, volleyball)

    # image concat
    img1, img = None, None
    for i, img_name in enumerate(img_list):
        if i == 0:
            if img_name == "baseball":
                img = baseball
            elif img_name == "soccer":
                img = soccer
            else:
                img = volleyball
        elif i == 5:
            img1 = img
            if img_name == "baseball":
                img = baseball
            elif img_name == "soccer":
                img = soccer
            else:
                img = volleyball
        else:
            if img_name == "baseball":
                img = np.concatenate((img, baseball), axis=1)
            elif img_name == "soccer":
                img = np.concatenate((img, soccer), axis=1)
            else:
                img = np.concatenate((img, volleyball), axis=1)

    img = np.concatenate((img, img1), axis=0)

    plt.imshow(img)
    plt.axis("off")

    svg = saveSvg()
    plt.clf()
    
    # 정답으로 쓸 공 선택
    answer_dict = {"야구공": num_baseball,
                   "축구공": num_soccer, "배구공": num_volleyball}
    answer_dict.pop(np.random.choice(list(answer_dict.keys())))

    answer_list = []
    comment_list = []
    for name in answer_dict:
        answer_list.append(answer_dict[name])
        comment_list.append("%s을 세어 보면 %s이므로 $$수식$$%s$$/수식$$ 입니다." % (name, ", ".join(
            answer_num_read[:answer_dict[name]]), answer_dict[name]))

    stem = "수를 세어 □안에 알맞은 수를 써넣으세요.\n" \
        "{b1} : {boxblank}, {b2} : {boxblank}"
        
    boxblank = "$$수식$$BOX{　　}$$/수식$$"
    stem = stem.format(b1=list(answer_dict.keys())[0], b2=list(answer_dict.keys())[1], boxblank=boxblank)
    answer = "(정답) $$수식$$%s$$/수식$$, $$수식$$%s$$/수식$$" % (answer_list[0], answer_list[1])
    comment = "(해설)" + " \n".join(comment_list)

    return stem, answer, comment, svg

# 완료


def uptonine111_Stem_027():
    plt.rc('font', family='NanumGothic')
    def uptonine111_Stem_017_setting():
        # 숫자 선택
        stem_figure_num = np.random.randint(2, 9+1)

        # 숫자에 맞게 이미지 가공 및 저장
        img = load_img(
            "/home/boin-service/Visang/Element/img/uptonine111_Stem_009_img_scissor.jpg")
        img_concat = img
        for i in range(stem_figure_num-1):
            img_concat = np.concatenate((img_concat, img), axis=1)

        # 문제, 정답, 해설에 필요한 변수 세팅
        stem_list = [stem_figure_num]
        answer_list = [num2hangul(stem_figure_num, "하나"),
                       num2hangul(stem_figure_num, "일")]
        comment_list = [", ".join(answer_num_read[:stem_figure_num])]

        return stem_list, answer_list, comment_list, img_concat

    # 문제, 정답, 해설에 필요한 변수 가져오기
    stem_list, answer_list, comment_list, img = uptonine111_Stem_017_setting()

    josa_ans01 = "은" if check_jongsung(answer_list[-1]) else "는"
    josa_ans02 = "이라고" if check_jongsung(answer_list[0]) else "라고"

    stem = "가위의 수를 세어 보고 두 가지 방법으로 읽어 보세요."
    answer = "(정답)" + ", ".join(answer_list)
    comment = "(해설)가위를 세어 보면 %s이므로 $$수식$$%s$$/수식$$입니다.\n" % (answer_list[0], stem_list[0])
    comment += "$$수식$$%s$$/수식$$%s %s 또는 %s%s 읽습니다." % (
        stem_list[0], josa_ans01, answer_list[0], answer_list[1], josa_ans02)

    plt.imshow(img)
    plt.axis("off")
    
    svg = saveSvg()
    plt.clf()
    
    return stem, answer, comment, svg

# 완료
slist = ["첫", "둘", "셋", "넷", "다섯", "여섯", "일곱", "여덟", "아홉"]
def uptonine111_Stem_028():
    


    wants = np.random.randint(0, len(slist))   
    answer = "(정답)\n "+str(wants+1)+"\n"
    temp = slist[wants]
    stem = "1부터 9까지의 수 중에서 "+temp+"째 수를 구하세요. \n "
    comment = "(해설) 1부터 9까지의 수 중에서 "+temp+"째 수는 "+str(wants+1)+"입니다."
    return stem,answer, comment

def uptonine111_Stem_029():
    

    
    temp_choose = random.sample(range(0, len(slist))   ,2)   
    wants_0 = temp_choose[0]
    wants_1 = temp_choose[1]
    answer = "(정답)\n "+str(wants_0+1)+","+str(wants_1+1)+ " \n"
    temp_0 = slist[wants_0]
    temp_1 = slist[wants_1]
    
    stem = "1부터 9까지의 수 중에서 "+temp_0+"째 수와 "+temp_1+"째 수를 구하여 순서대로 써 보세요. \n "
    comment = "(해설) 1부터 9까지의 수 중에서 "+temp_0+"째 수는 "+str(wants_0+1)+"입니다.\n "
    comment += "1부터 9까지의 수 중에서 "+temp_1+"째 수는 "+str(wants_1+1)+"입니다.\n "
    return stem,answer, comment

def uptonine111_Stem_030():
    
    wants = np.random.randint(5, len(slist))   
    temp = 9 - (wants+1)
    
    answer = "(정답)\n "+str(slist[temp])+"째 \n"
    
    stem = "1부터 9까지의 수 중에서 "+slist[wants]+"째 수는 뒤에서부터 몇째에 놓이는 수인가요? \n "
    comment = "(해설) 1부터 9까지의 수 중 "+slist[wants]+" 째 수는 뒤에서 "+str(slist[temp])+" 째 수입니다.\n "
    
    return stem,answer, comment

def ImgPath(pathcheck,shape,ranNum): ## 응용 or 기본 / 모양 / 번호 
    if pathcheck==0:
        temps = "Element/Grade1_1/Normal"
    else:
        temps = "Element/Grade1_1/Applications"
    tempimg_list = ["/shape/","/box/","/cynlinder/"]
    want = tempimg_list[shape]
    want = temps+want+str(ranNum).zfill(2)
    return want


def uptonine111_Stem_031():
    
    wants = np.random.randint(5, len(slist)) 
    answer = "(정답)\n "+str(slist[wants-1])+"째 \n"    
    stem = "보기의 사물의 수를 세보세요. 사물의 수는 1부터 9까지의 수 중에서 몇째 수인가요?\n "
    stem +="$$표$$"        
    temp1 = np.random.randint(1, 20)
    right_shape= np.random.randint(0, 2)
    for i in range(0,wants ):
        stem += "$$이미지$$"+ImgPath(1,right_shape ,temp1 )+".jpg" +"$$/이미지$$   "
    stem +="$$/표$$"  
    comment = "(해설) 1부터 9까지의 수 중에서 "+slist[wants-1]+"째 수는 "+str(wants)+"입니다."
    return stem,answer, comment


def uptonine111_Stem_032():
    
    wants = np.random.randint(5, len(slist))   
    temp = 9 - (wants+1)
    answer = "(정답)\n "+str(slist[temp+1])+"째 \n"
    stem = "보기의 사물의 수를 세보세요. 사물의 수는 1부터 9까지의 수 중에서 뒤에서부터 몇째에 놓이는 수인가요? \n "
    stem +="$$표$$"        
    temp1 = np.random.randint(1, 20)
    right_shape= np.random.randint(0, 2)
    for i in range(0,wants ):
        stem += "$$이미지$$"+ImgPath(1,right_shape ,temp1 )+".jpg" +"$$/이미지$$   "
    stem +="$$/표$$"  
    comment = "(해설) 1부터 9까지의 수 중 "+str(wants)+"는 뒤에서 "+str(slist[temp+1])+"째 수입니다.\n "
    return stem,answer, comment    

print(uptonine111_Stem_028())