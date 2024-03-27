import numpy as np
import random

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
    elif bool_jo(num):
        # 을를
        return "을"
    return "를"


def name_jo(num):
    # 이
    if bool_jo(num):
        return "이"
    return ""




# 1-2-6-03
def addandsub126_Stem_001():
    stem = "{sth}{jo1} $$수식$${x1}$$/수식$$개 있습니다. 한 {where}에 {sth} $$수식$$10$$/수식$$개를 담으면 {where}에 담고 남는 {sth}{jo2} 몇 개일까요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${x1}$$/수식$$은 $$수식$$10$$/수식$$과 $$수식$${a1}$$/수식$$로 가를 수 있습니다.\n" \
              "따라서 {sth} $$수식$${x1}$$/수식$$개를 {where}에 $$수식$$10$$/수식$$개 담고 남은 " \
              "{sth}{jo2} $$수식$${a1}$$/수식$$개입니다.\n\n"

    sth = ['달걀', '사과', '귤', '공', '구슬', '초콜릿', '사탕'][np.random.randint(0, 7)]
    jo1 = proc_jo(sth, 0)
    jo2 = proc_jo(sth, -1)
    where = ['상자', '바구니', '봉투'][np.random.randint(0, 3)]

    x1 = np.random.randint(11, 20)
    a1 = x1 - 10

    stem = stem.format(sth=sth, jo1=jo1, jo2=jo2, x1=x1, where=where)
    answer = answer.format(a1=a1)
    comment = comment.format(sth=sth, jo2=jo2, where=where, x1=x1, a1=a1)

    return stem, answer, comment




# 1-2-6-04
def addandsub126_Stem_002():
    stem = "어떤 수를 두 번 더했더니 $$수식$${x1}$$/수식$$가 되었습니다. 어떤 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 $$수식$${box}$$/수식$$라 하여 덧셈식을 만들면 " \
              "$$수식$${box} + {box} = {x1}$$/수식$$입니다.\n" \
              "$$수식$${x1}$$/수식$$는 똑같은 수인 $$수식$${a1}$$/수식$$과 $$수식$${a1}$$/수식$$로 " \
              "가르기 할 수 있으므로 $$수식$${box} = {a1}$$/수식$$입니다.\n\n"

    box = "□"
    a1 = np.random.randint(5, 10)
    x1 = 2*a1

    stem = stem.format(x1=x1)
    answer = answer.format(a1=a1)
    comment = comment.format(box=box, x1=x1, a1=a1)

    return stem, answer, comment


def getTwoNumToMakeSum(sum):
    while True:
        a = np.random.randint(2, 10)
        b = sum - a
        if b < 10:
            break
    return a, b





# 1-2-6-08
def addandsub126_Stem_003():
    stem = "합이 $$수식$${s1}$$/수식$$가 되는 덧셈식을 모두 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${x1} + {x2}$$/수식$$    ㉡ $$수식$${x3} + {x4}$$/수식$$\n㉢ $$수식$${x5} + {x6}$$/수식$$    ㉣ $$수식$${x7} + {x8}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{a1}, {a2}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${x1} + {x2} = {x9}$$/수식$$, ㉡ $$수식$${x3} + {x4} = {x10}$$/수식$$,\n" \
              "㉢ $$수식$${x5} + {x6} = {x11}$$/수식$$, ㉣ $$수식$${x7} + {x8} = {x12}$$/수식$$\n" \
              "따라서 합이 $$수식$${s1}$$/수식$$가 되는 덧셈식은 {a1}, {a2}입니다.\n\n"

    while True:
        s1, s2, s3 = random.sample(list(range(11, 19)), 3)
        if s1 != 18:
            break
    while True:
        c1, c2 = getTwoNumToMakeSum(s1)
        c3, c4 = getTwoNumToMakeSum(s1)
        if c3 != c1:
            break
    c5, c6 = getTwoNumToMakeSum(s2)
    c7, c8 = getTwoNumToMakeSum(s3)

    x = [[c1, c2], [c3, c4], [c5, c6], [c7, c8]]
    np.random.shuffle(x)
    [[x1, x2], [x3, x4], [x5, x6], [x7, x8]] = x

    a = []
    x9 = x1 + x2
    if x9 == s1:
        a.append(0)
    x10 = x3 + x4
    if x10 == s1:
        a.append(1)
    x11 = x5 + x6
    if x11 == s1:
        a.append(2)
    x12 = x7 + x8
    if x12 == s1:
        a.append(3)

    [a1, a2] = [answer_kodict[a[0]], answer_kodict[a[1]]]

    stem = stem.format(s1=s1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(s1=s1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8,
                             a1=a1, a2=a2, x9=x9, x10=x10, x11=x11, x12=x12)

    return stem, answer, comment






# 1-2-6-09
def addandsub126_Stem_004():
    stem = "계산 결과의 크기를 비교하여 {box1} 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$ 를 알맞게 써넣으세요.\n$$표$$$$수식$${boxf1}``BIGCIRC``{boxf2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${x1} + {x2} = {s1}$$/수식$$, ㉡ $$수식$${x3} + {x4} = {s2}$$/수식$$\n" \
              "→ $$수식$${s1} {a1} {s2}$$/수식$$\n\n"

    box1 = "○"

    while True:
        s1 = np.random.randint(11, 19)
        s2 = np.random.randint(11, 19)
        if s1 != s2 or (s1 == s2 and s1 != 18):
            break
    if s1 > s2:
        a1 = '&gt;'
    elif s1 < s2:
        a1 = '&lt;'
    else:
        a1 = '='

    x1, x2 = getTwoNumToMakeSum(s1)
    x3, x4 = getTwoNumToMakeSum(s2)

    boxf1 = "%d + %d" % (x1, x2)
    boxf2 = "%d + %d" % (x3, x4)

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, box1=box1, boxf1=boxf1, boxf2=boxf2)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, s1=s1, s2=s2, a1=a1)

    return stem, answer, comment





# 1-2-6-10
def addandsub126_Stem_005():
    stem = "{where} 안에 {sth1} $$수식$${x1}$$/수식$$개와 {sth2} $$수식$${x2}$$/수식$$개가 들어 있습니다. {sth1}{j1} {sth2}{j2} 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${sth1}{j1} {sth2}의 수" \
              "$$수식$$RIGHT ) = {x1} + {x2} = {a1} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"

    where = ['바구니', '봉투', '박스'][np.random.randint(0, 3)]
    sth = [['고구마', '감자'], ['초콜릿', '사탕'], ['사과', '배'],
           ['아이스크림', '빵'], ['콜라', '사이다'], ['탁구공', '탁구채']][np.random.randint(0, 6)]

    np.random.shuffle(sth)
    sth1, sth2 = sth
    j1 = proc_jo(sth1, 2)
    j2 = proc_jo(sth2, -1)

    x1 = np.random.randint(1, 10)
    x2 = np.random.randint(1, 10)
    a1 = x1 + x2

    stem = stem.format(where=where, sth1=sth1, sth2=sth2, j1=j1, j2=j2, x1=x1, x2=x2)
    answer = answer.format(a1=a1)
    comment = comment.format(sth1=sth1, sth2=sth2, j1=j1, x1=x1, x2=x2, a1=a1)

    return stem, answer, comment





# 1-2-6-12
def addandsub126_Stem_006():
    stem = "{sa}과 {sb} 사이에 있는 수는 몇 개일까요?\n$$표$$$$수식$${x1} + {x2} =$$/수식$${sa}\n$$수식$${x3} +$$/수식$${sb}$$수식$$= {x4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${x1} + {x2} = {s1}$$/수식$$ → {sa}$$수식$$= {s1}$$/수식$$\n" \
              "$$수식$${x3} + {s2} = {x4}$$/수식$$ → {sb}$$수식$$= {s2}$$/수식$$\n" \
              "$$수식$${p1}$$/수식$$과 $$수식$${p2}$$/수식$$ 사이에 있는 수는 {p}로 " \
              "$$수식$${a1}$$/수식$$개입니다.\n\n"

    sa, sb = random.sample(['●', '★', '▲', '♥', '◆'], 2)

    x1 = np.random.randint(1, 10)
    x2 = np.random.randint(1, 10)
    s1 = x1 + x2
    while True:
        s2 = np.random.randint(1, 10)
        if s2 != s1:
            break

    x3 = np.random.randint(1, 10)
    x4 = x3 + s2

    ps = [s1, s2]
    ps.sort()
    p1, p2 = ps
    p = ""
    for i in range(p1 + 1, p2):
        p = p + "$$수식$$" + str(i) + "$$/수식$$"
        if i != p2 - 1:
            p = p + ", "

    a1 = p2 - p1 - 1

    stem = stem.format(sa=sa, sb=sb, x1=x1, x2=x2, x3=x3, x4=x4)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, s1=s1, s2=s2, sa=sa, sb=sb,
                             p1=p1, p2=p2, p=p, a1=a1)

    return stem, answer, comment





# 1-2-6-13
def addandsub126_Stem_007():
    stem = "{sa}$$수식$$+$$/수식$${sb}의 값을 구해 보세요.\n$$표$${sa}$$수식$$= {x1}$$/수식$$\n{sb}$$수식$$= {x2} + {x3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${x2} + {x3} = {s1}$$/수식$$ → {sb}$$수식$$= {s1}$$/수식$$\n" \
              "{sa}$$수식$$+$$/수식$${sb}$$수식$$= {x1} + {s1} = {a1}$$/수식$$\n\n"

    sa, sb = random.sample(['●', '★', '▲', '♥', '■'], 2)
    x1 = np.random.randint(1, 10)
    s1 = np.random.randint(2, 10)
    x2 = np.random.randint(1, s1)

    x3 = s1 - x2
    a1 = x1 + s1

    stem = stem.format(sa=sa, sb=sb, x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, s1=s1, a1=a1, sa=sa, sb=sb)

    return stem, answer, comment




# 1-2-6-14
def addandsub126_Stem_008():
    stem = "{sth}{jo1} {sa}{j1}는 $$수식$${x1}$$/수식$$개 먹었고, {sb}{j2}는 {sa}{j1}보다 $$수식$${x2}$$/수식$$개 더 {state} 먹었습니다. {sa}{j1}와 {sb}{j2}가 먹은 {sth}{jo2} 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${sb}{j2}가 먹은 {sth} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$${sa}{j1}가 먹은 {sth} 수$$수식$$RIGHT ) {op} {x2}$$/수식$$\n" \
              "$$수식$$= {x1} {op} {x2} = {s1} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n" \
              "→ $$수식$$LEFT ($$/수식$${sa}{j1}와 {sb}{j2}가 먹은 {sth} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$${sa}{j1}가 먹은 {sth} 수$$수식$$RIGHT ) {op2} LEFT ($$/수식$$" \
              "{sb}{j2}가 먹은 {sth} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {x1} {op2} {s1} = {a1} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"

    sth = ['감자', '초콜릿', '사탕', '빵', '고구마', '귤', '사과', '계란'][np.random.randint(0, 8)]
    jo1 = proc_jo(sth, 1)
    jo2 = proc_jo(sth, -1)

    sa, sb = random.sample(['영준', '용태', '호정', '승헌', '연주', '수진', '장현', '유리', '호민', '예지'], 2)
    j1 = name_jo(sa)
    j2 = name_jo(sb)

    state, op, op2 = [['많이', '+', '+'], ['적게', '-', '+']][np.random.randint(0, 2)]
    x1 = np.random.randint(2, 9)
    if state == '많이':
        s1 = np.random.randint(x1 + 1, 10)
        x2 = s1 - x1
    else:
        s1 = np.random.randint(1, x1)
        x2 = x1 - s1
    a1 = x1 + s1

    stem = stem.format(sth=sth, jo1=jo1, jo2=jo2, sa=sa, sb=sb, j1=j1, j2=j2, x1=x1, x2=x2, state=state)
    answer = answer.format(a1=a1)
    comment = comment.format(sth=sth, sa=sa, sb=sb, j1=j1, j2=j2, x1=x1, x2=x2, s1=s1, a1=a1, op=op, op2=op2)

    return stem, answer, comment





# 1-2-6-18
def addandsub126_Stem_009():
    stem = "계산 결과가 더 {state} 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${x1} - {x2}$$/수식$$    ㉡ $$수식$${x3} - {x4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${x1} - {x2} = {s1}$$/수식$$, ㉡ $$수식$${x3} - {x4} = {s2}$$/수식$$\n" \
              "$$수식$${s1} {op} {s2}$$/수식$$이므로 계산 결과가 더 {state} 것은 {a1}입니다.\n\n"

    while True:
        x1, x3 = random.sample(list(range(11, 20)), 2)
        x2, x4 = random.sample(list(range(1, 10)), 2)
        s1 = x1 - x2
        s2 = x3 - x4
        if s1 != s2:
            break

    state = ['작은', '큰'][np.random.randint(0, 2)]
    if state == '작은':
        if s1 < s2:
            a1 = '㉠'
            op = '&lt;'
        else:
            a1 = '㉡'
            op = '&gt;'
    else:
        if s1 > s2:
            a1 = '㉠'
            op = '&gt;'
        else:
            a1 = '㉡'
            op = '&lt;'

    stem = stem.format(state=state, x1=x1, x2=x2, x3=x3, x4=x4)
    answer = answer.format(a1=a1)
    comment = comment.format(state=state, x1=x1, x2=x2, x3=x3, x4=x4, s1=s1, s2=s2, op=op, a1=a1)

    return stem, answer, comment





# 1-2-6-19
def addandsub126_Stem_010():
    stem = "가장 큰 수와 가장 작은 수의 차를 구해 보세요.\n$$표$$$$수식$${x1}$$/수식$$   $$수식$${x2}$$/수식$$   $$수식$${x3}$$/수식$$   $$수식$${x4}$$/수식$$   $$수식$${x5}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$10$$/수식$$개씩 묶음의 수와 낱개의 수를 비교하면 " \
              "가장 큰 수는 $$수식$${s1}$$/수식$$이고, 가장 작은 수는 $$수식$${s2}$$/수식$$입니다.\n" \
              "따라서 가장 큰 수와 가장 작은 수의 차는 $$수식$${s1} - {s2} = {a1}$$/수식$$입니다.\n\n"

    p = random.sample(list(range(11, 20)), 2)
    q = random.sample(list(range(1, 10)), 3)
    x = p + q
    np.random.shuffle(x)
    [x1, x2, x3, x4, x5] = x
    x.sort()
    s1 = x[4]
    s2 = x[0]
    a1 = s1 - s2

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=a1)
    comment = comment.format(s1=s1, s2=s2, a1=a1)

    return stem, answer, comment




# 1-2-6-20
def addandsub126_Stem_011():
    stem = "{sa} $$수식$${x1}$$/수식$$명에게 {sth}{jo1} 한 개씩 나누어 주려고 합니다. {sth}{jo2} $$수식$${x2}$$/수식$$개 있다면 몇 개 더 필요할까요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n" \
              "{sa} 수에서 {sth} 수를 빼면 되므로 $$수식$${x1} - {x2}$$/수식$$를 계산합니다.\n" \
              "$$수식$${x1}$$/수식$$을 $$수식$$10$$/수식$$과 $$수식$${s1}$$/수식$$로 가르기 하여 " \
              "$$수식$$10$$/수식$$에서 $$수식$${x2}$$/수식$$을 한 번에 빼고 " \
              "남은 $$수식$${s2}$$/수식$$와 $$수식$${s1}$$/수식$$을 더하면 $$수식$${a1}$$/수식$$가 됩니다. " \
              "따라서 {sth}{jo3} $$수식$${a1}$$/수식$$개 더 필요합니다.\n\n"

    sa = ['어린이', '학생', '유치원생', '친구', '동생'][np.random.randint(0, 5)]
    sth = ['사탕', '구슬', '초콜릿', '빼빼로', '연필', '귤', '과자'][np.random.randint(0, 7)]
    jo1 = proc_jo(sth, 1)
    jo2 = proc_jo(sth, 0)
    jo3 = proc_jo(sth, -1)

    x1 = np.random.randint(11, 19)
    s1 = x1 - 10
    x2 = np.random.randint(s1 + 1, 10)
    s2 = 10 - x2
    a1 = s1 + s2

    stem = stem.format(sa=sa, sth=sth, jo1=jo1, jo2=jo2, x1=x1, x2=x2)
    answer = answer.format(a1=a1)
    comment = comment.format(sa=sa, sth=sth, jo3=jo3, x1=x1, x2=x2, s1=s1, s2=s2, a1=a1)

    return stem, answer, comment






# 1-2-6-21
def addandsub126_Stem_012():
    stem = "{sa}과 {sb}에 알맞은 수의 차를 구해 보세요.\n$$표$$$$수식$${x1} -$$/수식$${sa}$$수식$$= {x2}$$/수식$$\n{sb}$$수식$$- {x3} = {x4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${x1} -$$/수식$${sa}$$수식$$= {x2}$$/수식$$에서 $$수식$${x1} - {s1}= {x2}$$/수식$$이므로 " \
              "{sa}$$수식$$= {s1}$$/수식$$입니다.\n" \
              "{sb}$$수식$$- {x3} = {x4}$$/수식$$에서 $$수식$${s2} - {x3} = {x4}$$/수식$$이므로 " \
              "{sb}$$수식$$= {s2}$$/수식$$입니다.\n" \
              "따라서 $$수식$${s1} {op} {s2}$$/수식$$이므로 {sa}과 {sb}에 알맞은 수의 차는 " \
              "$$수식$${p1} - {p2} = {a1}$$/수식$$입니다.\n\n"

    sa, sb = random.sample(['■', '●', '★', '▲', '♥'], 2)

    while True:
        x2 = np.random.randint(1, 10)
        s1 = np.random.randint(1, 10)
        x1 = s1 + x2
        x3 = np.random.randint(1, 10)
        x4 = np.random.randint(1, 10)
        s2 = x3 + x4
        if s1 > s2:
            op = '&gt;'
            a1 = s1 - s2
            p1 = s1
            p2 = s2
        else:
            op = '&lt;'
            a1 = s2 - s1
            p1 = s2
            p2 = s1
        if (a1 < 10) and (s1 != s2):
            break

    stem = stem.format(sa=sa, sb=sb, x1=x1, x2=x2, x3=x3, x4=x4)
    answer = answer.format(a1=a1)
    comment = comment.format(sa=sa, sb=sb, x1=x1, x2=x2, x3=x3, x4=x4, s1=s1, s2=s2,
                             op=op, p1=p1, p2=p2, a1=a1)

    return stem, answer, comment




# 1-2-6-22
def addandsub126_Stem_013():
    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 중에서 $$수식$${box}$$/수식$$ 안에 들어갈 수 있는 수는 모두 몇 개인가요?\n$$표$$$$수식$${x1} - {x2} {op} {x3} - {box}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${x1} - {x2} = {s1}$$/수식$$이므로 $$수식$${s1} {op} {x3} - {box}$$/수식$$입니다.\n" \
              "{sols}따라서 $$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 중에서 " \
              "$$수식$${box}$$/수식$$ 안에 들어갈 수 있는 수는 {nums}로 모두 $$수식$${a1}$$/수식$$개입니다.\n\n"

    box = "□"

    while True:
        x1, x3 = random.sample(list(range(11, 18)), 2)
        x2 = np.random.randint(1, 10)
        s1 = x1 - x2
        std = x3 - s1
        if std > 0:
            break

    sol = "$$수식$${x3} - {box} = {tmp}$$/수식$$이면 " \
          "$$수식$${x3} - {atmp} = {tmp}$$/수식$$에서 $$수식$${box} = {atmp}$$/수식$$입니다.\n"
    sols = ""
    nums = ""
    a1 = 0

    if x1 > x3:
        op = '&gt;'
        for i in range(std + 1, 10):
            a1 = a1 + 1
            nums = nums + "$$수식$$ %s $$/수식$$" % str(i)
            if i != 9:
                nums = nums + ", "
            tmp = x3 - i
            sols = sols + sol.format(x3=x3, box=box, atmp=i, tmp=tmp)
    else:
        op = '&lt;'
        for i in range(1, std):
            if i > 9:
                break
            a1 = a1 + 1
            nums = nums + "$$수식$$ %s $$/수식$$" % str(i)
            if i != std - 1:
                nums = nums + ", "
            tmp = x3 - i
            sols = sols + sol.format(x3=x3, box=box, atmp=i, tmp=tmp)

    stem = stem.format(box=box, x1=x1, x2=x2, x3=x3, op=op)
    answer = answer.format(a1=a1)
    comment = comment.format(box=box, x1=x1, x2=x2, x3=x3, op=op, s1=s1, sols=sols, nums=nums, a1=a1)

    return stem, answer, comment






# 1-2-6-23
def addandsub126_Stem_014():
    stem = "같은 모양은 같은 수를 나타낼 때 {sa}, {sb}, {sc}은 각각 얼마인가요?\n$$표$${sa}$$수식$$+$$/수식$${sa}$$수식$$= {x1}$$/수식$$\n$$수식$${x2} -$$/수식$${sa}$$수식$$=$$/수식$${sb}\n{sc}$$수식$$- {x3} =$$/수식$${sb}$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$\n"
    comment = "(해설)\n" \
              "{sa}$$수식$$+$$/수식$${sa}$$수식$$= {x1}$$/수식$$에서 같은 수를 " \
              "$$수식$$2$$/수식$$번 더하여 $$수식$${x1}$$/수식$$이 되는 경우를 찾으면 " \
              "$$수식$${a1} + {a1} = {x1}$$/수식$$이므로 {sa}$$수식$$= {a1}$$/수식$$입니다.\n" \
              "$$수식$${x2} -$$/수식$${sa}$$수식$$=$$/수식$${sb}에서 " \
              "$$수식$${x2} - {a1} =$$/수식$${sb}이므로 {sb}$$수식$$= {a2}$$/수식$$입니다.\n" \
              "{sc}$$수식$$- {x3} =$$/수식$${sb}에서 {sc}$$수식$$- {x3} = {a2}$$/수식$$이고 " \
              "$$수식$${a3} - {x3} = {a2}$$/수식$$이므로 {sc}$$수식$$= {a3}$$/수식$$입니다.\n\n"

    sa, sb, sc = random.sample(['■', '●', '★', '▲', '♥'], 3)

    while True:
        a1 = np.random.randint(1, 10)
        x1 = 2 * a1
        x2 = np.random.randint(11, 19)
        a2 = x2 - a1
        if a2 < 10:
            break

    x3 = np.random.randint(1, 10)
    a3 = x3 + a2

    stem = stem.format(sa=sa, sb=sb, sc=sc, x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=a1, a2=a2, a3=a3)
    comment = comment.format(sa=sa, sb=sb, sc=sc, x1=x1, x2=x2, x3=x3, a1=a1, a2=a2, a3=a3)

    return stem, answer, comment




# 1-2-6-25
def addandsub126_Stem_015():
    stem = "$$수식$${x1}$$/수식$$에서 어떤 수를 {state1} 할 것을 잘못하여 {state2} $$수식$${x2}$$/수식$${j1} 되었습니다. 알맞게 계산한 값은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 $$수식$${box}$$/수식$$라 하여 식을 쓰면 " \
              "$$수식$${x1} {op1} {box} = {x2}$$/수식$$입니다.\n" \
              "$$수식$${x1}$$/수식$${state3} 하여 $$수식$${x2}$$/수식$${j1} 되는 수는 " \
              "$$수식$${s1}$$/수식$$이므로 $$수식$${box} = {s1}$$/수식$$입니다.\n" \
              "따라서 알맞게 계산하면 $$수식$${x1} {op2} {s1} = {a1}$$/수식$$입니다.\n\n"

    box = "□"

    state = np.random.randint(0, 2)
    state1 = ['빼야', '더해야'][state]
    state2 = ['더했더니', '뺐더니'][state]
    op1 = ['+', '-'][state]
    op2 = ['-', '+'][state]
    state3 = ['와 모으기', '에서 가르기'][state]

    s1 = np.random.randint(1, 9)
    x1 = np.random.randint(s1 + 1, 10)
    if state == 0:
        a1 = x1 - s1
        x2 = x1 + s1
    else:
        a1 = x1 + s1
        x2 = x1 - s1

    j1 = proc_jo(x2, 0)

    stem = stem.format(x1=x1, x2=x2, state1=state1, state2=state2, j1=j1)
    answer = answer.format(a1=a1)
    comment = comment.format(box=box, x1=x1, x2=x2, s1=s1, a1=a1, op1=op1, op2=op2, state3=state3, j1=j1)

    return stem, answer, comment






# 1-2-6-26
def addandsub126_Stem_016():
    stem = "{ss}에 승객이 $$수식$${sa}$$/수식$$명 있었습니다. 첫 번째 정류장에서 승객 $$수식$${sb}$$/수식$$명이 내리고, 두 번째 정류장에서 승객 $$수식$${sc}$$/수식$$명이 내렸습니다. {ss}에 남은 승객은 몇 명인가요?\n"
    answer = "(정답)\n$$수식$${se}$$/수식$$명\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$첫 번째 정류장에서 내리고 남은 승객 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$$처음 {ss}에 타고 있던 승객 수$$수식$$RIGHT ) - LEFT ($$/수식$$" \
              "첫 번째 정류장에서 내린 승객 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {sa} - {sb} = {sd} LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$\n" \
              "→ $$수식$$LEFT ($$/수식$${ss}에 남은 승객 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$$첫 번째 정류장에서 내리고 남은 승객 수$$수식$$RIGHT ) - LEFT ($$/수식$$" \
              "두 번째 정류장에서 내린 승객 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {sd} - {sc} = {se} LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$\n\n"

    ss = ['버스', '지하철', '기차'][np.random.randint(0, 3)]

    sa = np.random.randint(11, 20)
    sb = np.random.randint(3, 8)
    sc = np.random.randint(1, 4)
    sd = sa - sb
    se = sd - sc

    stem = stem.format(ss=ss, sa=sa, sb=sb, sc=sc)
    answer = answer.format(se=se)
    comment = comment.format(ss=ss, sa=sa, sb=sb, sc=sc, sd=sd, se=se)

    return stem, answer, comment
