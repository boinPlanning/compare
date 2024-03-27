import numpy as np
import operator
import random
from math import gcd




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
    4: "㉤",
    5: "㉥"
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
        #이(라고)
        if bool_jo(num):
            return "이"
        return ""
    elif bool_jo(num):
        # 을를
        return "을"
    return "를"








#def gcd (a, b):
#    if b == 0:
#        return a
#    else :
#        if a < b:
#            a, b = b, a
#        return gcd(b, a % b)







def lcm(a, b):
    return a * b // gcd(a, b)










# 5-1-4-05
def reductionfra514_Stem_001():
    stem = "{wh1}{j1} {s1}{j2} 똑같이 $$수식$${x1}$$/수식$$조각으로 나누어 한 조각을 먹었습니다. {wh2}{j3} 같은 크기의 {s1}{j2} 똑같이 $$수식$${x2}$$/수식$$조각으로 나누었습니다. {wh1}{j4} 같은 양을 먹으려면 {wh2}{j3} 몇 조각을 먹어야 하나요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$조각\n"
    comment = "(해설)\n{wh1}{j1} 전체의 $$수식$$1 over {x1}$$/수식$$만큼을 먹었고 {wh2}{j3} {wh1}{j4} 똑같은 크기만큼 먹으려면 $$수식$${a1} over {x2}$$/수식$$" \
              "{j5} 먹어야 합니다. 따라서 {wh2}{j3} {wh1}{j4} 같은 양을 먹으려면 $$수식$${a1}$$/수식$$조각을 먹어야 합니다.\n\n"


    wh_list = ['윤서', '지우', '정호', '현기', '재수', '영서', '은지', '연주', '주호', '혁구', '영기', '상수', '은서', '동우', '재우', '진희', '준서',
               '유라', '수미', '현수', '채아', '민주', '지호', '연아', '은우', '시우', '혁재', '민하']

    wh1 = wh_list[np.random.randint(0, len(wh_list))]
    wh2 = wh_list[np.random.randint(0, len(wh_list))]

    while wh1 == wh2 :
        wh2 = wh_list[np.random.randint(0, len(wh_list))]

    s1 = ['피자', '호두파이', '사과파이', '케이크', '치즈케이크', '빈대떡'][np.random.randint(0, 6)]

    x1 = np.random.randint(3, 9)
    a1 = np.random.randint(2, 5)

    while x1 * a1 > 19 or x1 * a1 < 10 :
        a1 = np.random.randint(2, 5)

    x2 = x1 * a1

    j1 = proc_jo(wh1, -1)
    j2 = proc_jo(s1, 4)
    j3 = proc_jo(wh2, -1)
    j4 = proc_jo(wh1, 2)
    j5 = proc_jo(a1, 4)

    stem = stem.format(wh1 = wh1, wh2 = wh2, s1 = s1, x1 = x1, x2 = x2, j1 = j1, j2 = j2, j3 = j3, j4 = j4)
    answer = answer.format(a1 = a1)
    comment = comment.format(wh1 = wh1, wh2 = wh2, j1 = j1, j2 = j2, j3 = j3, j4 = j4, j5 = j5, x1 = x1, x2 = x2, a1 = a1)

    return stem, answer, comment


















# 5-1-4-08
def reductionfra514_Stem_002():
    stem = "주어진 분수와 크기가 같은 분수를 분모가 작은 것부터 차례로 $$수식$$3$$/수식$$개 써 보세요.\n$$수식$${boxl}{y} over {x}{boxr}$$/수식$$\n"
    answer = "(정답)\n$$수식$${y2} over {x2}$$/수식$$, $$수식$${y3} over {x3}$$/수식$$, $$수식$${y4} over {x4}$$/수식$$\n"
    comment = "(해설)\n분모와 분자에 $$수식$$0$$/수식$$이 아닌 같은 수, 즉 $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$, $$수식$${a4}$$/수식$${j1} 곱하여 " \
              "크기가 같은 분수를 만들어 봅니다.\n" \
              "$$수식$${y} over {x} ` = ` {l}{y} ` times ` {a2}{r} over {l}{x} ` times ` {a2}{r} ` = ` {y2} over {x2}$$/수식$$, " \
              "$$수식$${y} over {x} ` = ` {l}{y} ` times ` {a3}{r} over {l}{x} ` times ` {a3}{r} ` = ` {y3} over {x3}$$/수식$$, " \
              "$$수식$${y} over {x} ` = ` {l}{y} ` times ` {a4}{r} over {l}{x} ` times ` {a4}{r} ` = ` {y4} over {x4}$$/수식$$\n\n"


    x = np.random.randint(4, 10)
    y = np.random.randint(3, x)

    while gcd(x, y) != 1 :
        y = np.random.randint(3, x)

    a2 = 2
    a3 = 3
    a4 = 4

    x2 = x * a2
    x3 = x * a3
    x4 = x * a4

    y2 = y * a2
    y3 = y * a3
    y4 = y * a4

    boxl = "[``"
    boxr = "``]"

    l = "{"
    r = "}"

    j1 = proc_jo(a4, 4)

    stem = stem.format(x = x, y = y, boxl = boxl, boxr = boxr)
    answer = answer.format(x2 = x2, x3 = x3, x4 = x4, y2 = y2, y3 = y3, y4 = y4)
    comment = comment.format(j1 = j1, x = x, y = y, a2 = a2, a3 = a3, a4 = a4, l = l, r = r, x2 = x2, x3 = x3, x4 = x4, y2 = y2, y3 = y3, y4 = y4)
    return stem, answer, comment



















# 5-1-4-10
def reductionfra514_Stem_003():
    stem = "다음 중에서 크기가 같은 분수끼리 짝지어진 것을 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$$ {s1} $$/수식$$    ㉡ $$수식$$ {s2} $$/수식$$\n \n㉢ $$수식$$ {s3} $$/수식$$    ㉣ $$수식$$ {s4} $$/수식$$ $$/표$$\n"
    answer = "(정답)\n{aone}\n"
    comment = "(해설)\n{aone}. $$수식$$ {b_} over {a_} ` = ` {lg}{b_} ` times ` {a1}{rg} over {lg}{a_} ` times ` {a1}{rg} ` = ` {b_1} over {a_1} $$/수식$$\n\n"


    a_ = np.random.randint(4, 11)
    b_ = np.random.randint(3, a_)

    while gcd(a_, b_) != 1 :
        b_ = np.random.randint(3, a_)

    c_ = np.random.randint(4, 11)

    while c_ == a_ :
        c_ = np.random.randint(4, 11)

    d_ = np.random.randint(3, c_)

    while gcd(c_, d_) != 1 :
        d_ = np.random.randint(3, c_)

    e_ = np.random.randint(4, 11)

    while e_ == a_ or e_ == c_:
        e_ = np.random.randint(4, 11)

    f_ = np.random.randint(3, e_)

    while gcd(e_, f_) != 1:
        f_ = np.random.randint(3, e_)

    g_ = np.random.randint(4, 11)

    while g_ == a_ or g_ == c_ or g_ == e_ :
        g_ = np.random.randint(4, 11)

    h_ = np.random.randint(3, g_)

    while gcd(g_, h_) != 1:
        h_ = np.random.randint(3, g_)

    n_list = [2, 3, 4, 5, 6, 7]

    a1 = n_list.pop(np.random.randint(0, len(n_list)))
    c1 = n_list.pop(np.random.randint(0, len(n_list)))
    e1 = n_list.pop(np.random.randint(0, len(n_list)))
    g1 = n_list.pop(np.random.randint(0, len(n_list)))

    c2 = np.random.randint(2, 10)

    while c2 == c1 or d_*c2 >= c_*c1 :
        c2 = np.random.randint(2, 10)
        n_list.append(c1)
        c1 = n_list.pop(np.random.randint(0, len(n_list)))

    e2 = np.random.randint(2, 10)

    while e2 == e1 or f_*e2 >= e_*e1 :
        e2 = np.random.randint(2, 10)
        n_list.append(e1)
        e1 = n_list.pop(np.random.randint(0, len(n_list)))

    g2 = np.random.randint(2, 10)

    while g2 == g1 or h_*g2 >= g_*g1 :
        g2 = np.random.randint(2, 10)
        n_list.append(g1)
        g1 = n_list.pop(np.random.randint(0, len(n_list)))

    a_1 = a_ * a1
    b_1 = b_ * a1
    c_1 = c_ * c1
    d_1 = d_ * c2
    e_1 = e_ * e1
    f_1 = f_ * e2
    g_1 = g_ * g1
    h_1 = h_ * g2

    x1 = f"LEFT ( {b_} over {a_} ,~ {b_1} over {a_1} RIGHT )"
    x2 = f"LEFT ( {d_} over {c_} ,~ {d_1} over {c_1} RIGHT )"
    x3 = f"LEFT ( {f_} over {e_} ,~ {f_1} over {e_1} RIGHT )"
    x4 = f"LEFT ( {h_} over {g_} ,~ {h_1} over {g_1} RIGHT )"

    candidates = [x1, x2, x3, x4]
    np.random.shuffle(candidates)
    [s1, s2, s3, s4] = candidates

    correct_idx = 0

    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == x1:
            correct_idx = idx
            break

    lg = "{"
    rg = "}"

    stem = stem.format(s1 = s1, s2 = s2, s3 = s3, s4 = s4)
    answer = answer.format(aone = answer_kodict[correct_idx])
    comment = comment.format(lg = lg, rg = rg, aone = answer_kodict[correct_idx], a1 = a1, b_ = b_, a_ = a_, b_1 = b_1, a_1 = a_1)
    return stem, answer, comment
























# 5-1-4-11
def reductionfra514_Stem_004():
    stem = "$$수식$${b_} over {a_}$$/수식$${j1} 크기가 같은 분수를 모두 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$$ {s1} $$/수식$$    ㉡ $$수식$$ {s2} $$/수식$$    ㉢ $$수식$$ {s3} $$/수식$$\n㉣ $$수식$$ {s4} $$/수식$$    ㉤ $$수식$$ {s5} $$/수식$$    ㉥ $$수식$$ {s6} $$/수식$$ $$/표$$\n"
    answer = "(정답)\n{aone}, {atwo}\n"
    comment = "(해설)\n$$수식$${b_} over {a_} ` = ` {lg} {b_} ` div ` {a1} {rg} over {lg} {a_} ` div ` {a1} {rg} ` = ` {b_1} over {a_1}$$/수식$$, " \
              "$$수식$${b_} over {a_} ` = ` {lg} {b_} ` div ` {a2} {rg} over {lg} {a_} ` div ` {a2} {rg} ` = ` {b_2} over {a_2}$$/수식$$, " \
              "$$수식$${b_} over {a_} ` = ` {lg} {b_} ` div ` {a3} {rg} over {lg} {a_} ` div ` {a3} {rg} ` = ` {b_3} over {a_3}$$/수식$$.\n" \
              "$$수식$${b_} over {a_} ` = ` {lg} {b_} ` div ` {a4} {rg} over {lg} {a_} ` div ` {a4} {rg} ` = ` {b_4} over {a_4}$$/수식$$, " \
              "$$수식$${b_} over {a_} ` = ` {lg} {b_} ` div ` {a5} {rg} over {lg} {a_} ` div ` {a5} {rg} ` = ` {b_5} over {a_5}$$/수식$$\n\n"


    a = np.random.randint(2, 4)
    b = [3, 5, 7][np.random.randint(0, 3)]

    while b <= a :
        b = [3, 5, 7][np.random.randint(0, 3)]

    c = [1, 2, 3][np.random.randint(0, 3)]
    d = [1, 2, 3, 5][np.random.randint(0, 4)]

    while c >= d or d > 189/(a*a*b):
        c = [1, 2, 3][np.random.randint(0, 3)]
        d = [1, 2, 3, 5][np.random.randint(0, 4)]

    a1 = a
    a2 = min(a*a, b)
    a3 = max(a*a, b)

    a4 = a*b
    a5 = a*a*b

    b_list = [a1, a2, a3, a4, a5]

    b1 = b_list.pop(np.random.randint(0, len(b_list)))
    b2 = b_list.pop(np.random.randint(0, len(b_list)))
    b3 = b_list.pop(np.random.randint(0, len(b_list)))
    b4 = b_list.pop(np.random.randint(0, len(b_list)))
    b5 = b_list.pop(np.random.randint(0, len(b_list)))

    a_ = a5 * d
    b_ = a5 * c

    c_ = round(a_ / b1)
    d_ = round(b_ / b1)
    e_ = round(a_ / b2)
    f_ = round(b_ / b2)

    g_ = round(a_ / b2)
    h_ = round(b_ / b3)
    i_ = round(a_ / b3)
    j_ = round(b_ / b4)

    k_ = round(a_ / b4)
    l_ = round(b_ / b5)
    m_ = round(a_ / b1)
    n_ = round(b_ / b2)

    x1 = f"{d_} over {c_}"
    x2 = f"{f_} over {e_}"
    x3 = f"{h_} over {g_}"

    x4 = f"{j_} over {i_}"
    x5 = f"{l_} over {k_}"
    x6 = f"{n_} over {m_}"

    candidates = [x1, x2, x3, x4, x5, x6]
    np.random.shuffle(candidates)
    [s1, s2, s3, s4, s5, s6] = candidates

    correct_idx = 0
    correct_idx2 = 0

    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == x1:
            correct_idx = idx
        if sdx == x2 :
            correct_idx2 = idx

    if correct_idx > correct_idx2 :
        tmp = correct_idx
        correct_idx = correct_idx2
        correct_idx2 = tmp

    lg = "{"
    rg = "}"

    j1 = proc_jo(b_, 2)

    stem = stem.format(j1 = j1, s1 = s1, s2 = s2, s3 = s3, s4 = s4, s5 = s5, s6 = s6, a_ = a_, b_ = b_)
    answer = answer.format(aone = answer_kodict[correct_idx], atwo = answer_kodict[correct_idx2])
    comment = comment.format(lg = lg, rg = rg, a_ = a_, b_ = b_, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5, b_1 = round(b_/a1), a_1 = round(a_/a1), b_2 = round(b_/a2), a_2 = round(a_/a2), a_3 = round(a_/a3), b_3 = round(b_/a3), a_4 = round(a_/a4), b_4 = round(b_/a4), a_5 = round(a_/a5), b_5= round(b_/a5))

    return stem, answer, comment


























# 5-1-4-12
def reductionfra514_Stem_005():
    stem = "크기가 나머지와 다른 분수를 찾아 써 보세요.\n$$표$$ $$수식$$ {s1} $$/수식$$    $$수식$$ {s2} $$/수식$$    $$수식$$ {s3} $$/수식$$    $$수식$$ {s4} $$/수식$$    $$수식$$ {s5} $$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${j_} over {i_}$$/수식$$\n"
    comment = "(해설)\n크기가 같은 분수를 찾으려면 분모와 분자에 $$수식$$0$$/수식$$이 아닌 같은 수를 곱하거나 나누어 봅니다.\n" \
              "$$수식$${b_} over {a_} ` = ` {lg}{b_} ` div ` {b1}{rg} over {lg}{a_} ` div ` {b1}{rg} ` = ` {b_1} over {a_1}$$/수식$$, " \
              "$$수식$${b_} over {a_} ` = ` {lg}{b_} ` div ` {b2}{rg} over {lg}{a_} ` div ` {b2}{rg} ` = ` {b_2} over {a_2}$$/수식$$,\n" \
              "$$수식$${b_} over {a_} ` = ` {lg}{b_} ` div ` {b3}{rg} over {lg}{a_} ` div ` {b3}{rg} ` = ` {b_3} over {a_3}$$/수식$$, " \
              "$$수식$${b_} over {a_} ` = ` {lg}{b_} ` div ` {b4}{rg} over {lg}{a_} ` div ` {b4}{rg} ` = ` {b_4} over {a_4}$$/수식$$\n" \
              "따라서 크기가 나머지와 다른 분수는 $$수식$${j_} over {i_}$$/수식$$입니다.\n\n"


    a = np.random.randint(2, 4)
    b = [3, 5, 7][np.random.randint(0, 3)]

    while b <= a:
        b = [3, 5, 7][np.random.randint(0, 3)]

    c = [1, 2, 3][np.random.randint(0, 3)]
    d = [1, 2, 3, 5][np.random.randint(0, 4)]

    while c >= d or d > 189 / (a * a * b):
        c = [1, 2, 3][np.random.randint(0, 3)]
        d = [1, 2, 3, 5][np.random.randint(0, 4)]

    a1 = a
    a2 = min(a * a, b)
    a3 = max(a * a, b)

    a4 = a * b
    a5 = a * a * b

    b_list = [a1, a2, a3, a4, a5]

    b1 = b_list.pop(np.random.randint(0, len(b_list)))
    b2 = b_list.pop(np.random.randint(0, len(b_list)))
    b3 = b_list.pop(np.random.randint(0, len(b_list)))
    b4 = b_list.pop(np.random.randint(0, len(b_list)))
    b5 = b_list.pop(np.random.randint(0, len(b_list)))

    if b4 > b5 :
        tmp = b4
        b4 = b5
        b5 = tmp

    a_ = a5 * d
    b_ = a5 * c

    c_ = round(a_/b1)
    d_ = round(b_/b1)
    e_ = round(a_/b2)
    f_ = round(b_/b2)

    g_ = round(a_/b3)
    h_ = round(b_/b3)
    i_ = round(a_/b4)
    j_ = round(b_/b5)

    x1 = f"{b_} over {a_}"
    x2 = f"{d_} over {c_}"
    x3 = f"{f_} over {e_}"
    x4 = f"{h_} over {g_}"
    x5 = f"{j_} over {i_}"

    a_1 = round(a_/b1)
    a_2 = round(a_/b2)
    a_3 = round(a_/b3)
    a_4 = round(a_/b4)

    b_1 = round(b_/b1)
    b_2 = round(b_/b2)
    b_3 = round(b_/b3)
    b_4 = round(b_/b4)

    candidates = [x1, x2, x3, x4, x5]
    np.random.shuffle(candidates)
    [s1, s2, s3, s4, s5] = candidates

    lg = "{"
    rg = "}"

    stem = stem.format(s1 = s1, s2 = s2, s3 = s3, s4 = s4, s5 = s5)
    answer = answer.format(j_ = j_, i_ = i_)
    comment = comment.format(lg = lg, rg = rg, j_ = j_, i_ = i_, a_ = a_, b_ = b_, b1 = b1, b2 = b2, b3 = b3, b4 = b4, a_1 = a_1, b_1 = b_1, a_2 = a_2, b_2 = b_2, a_3 = a_3, b_3 = b_3, a_4 = a_4, b_4 = b_4)

    return stem, answer, comment













































# 5-1-4-14
def reductionfra514_Stem_006():
    stem = "㉠과 ㉡에 알맞은 수를 각각 구하여 차례로 써 보세요.\n$$표$$ $$수식$${lg}㉠{rg} over {a_} ` = ` {b_1} over {a_1} ` = ` {b_2} over {lg}㉡{rg}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${b_}$$/수식$$, $$수식$${a_2}$$/수식$$\n"
    comment = "(해설)\n$$수식$${lg}㉠{rg} over {a_} ` = ` {b_1} over {a_1}$$/수식$$에서 " \
              "$$수식$${lg}㉠ ` times ` {a1}{rg} over {lg}{a_} ` times ` {a1}{rg} ` = ` {b_1} over {a_1}$$/수식$$입니다.\n" \
              "→ $$수식$$㉠ ` times ` {a1} ` = ` {b_1}$$/수식$$, $$수식$$㉠ ` = ` {b_1} ` div ` {a1} ` = ` {b_}$$/수식$$\n" \
              "$$수식$${b_1} over {a_1} ` = ` {b_2} over {lg}㉡{rg}$$/수식$$에서 " \
              "$$수식$${lg}{b_1} ` times ` {a2}{rg} over {lg}{a_1} ` times ` {a2}{rg} ` = ` {b_2} over {lg}㉡{rg}$$/수식$$입니다.\n" \
              "→ $$수식$${a_1} ` times ` {a2} ` = ` ㉡$$/수식$$, $$수식$$㉡ ` = ` {a_2}$$/수식$$\n" \
              "따라서 ㉠$$수식$$` = ` {b_}$$/수식$$, ㉡$$수식$$` = ` {a_2}$$/수식$$입니다.\n\n"


    a_ = np.random.randint(3, 10)
    b_ = np.random.randint(2, a_)

    while gcd(a_, b_) != 1:
        a_ = np.random.randint(3, 10)
        b_ = np.random.randint(2, a_)

    a1 = np.random.randint(3, 6)
    a2 = np.random.randint(2, 5)

    a_1 = a_ * a1
    b_1 = b_ * a1
    a_2 = a_1 * a2
    b_2 = b_1 * a2

    lg = "{"
    rg = "}"

    ni_eun = "㉡"

    stem = stem.format(lg=lg, rg=rg, a_=a_, b_1=b_1, a_1=a_1, b_2=b_2)
    answer = answer.format(b_=b_, a_2=a_2)
    comment = comment.format(lg=lg, rg=rg, a_=a_, b_1=b_1, a_1=a_1, a1=a1, a2=a2, b_2=b_2, a_2=a_2, b_=b_)

    return stem, answer, comment






















# 5-1-4-15
def reductionfra514_Stem_007():
    stem = "$$수식$${b_} over {a_}$$/수식$${j1} 크기가 같은 분수 중에서 분모와 분자의 합이 $$수식$${c_}$$/수식$$인 분수를 써 보세요.\n"
    answer = "(정답)\n$$수식$${e_} over {d_}$$/수식$$\n"
    comment = "(해설)\n$$수식$${b_} over {a_}$$/수식$${j1} 크기가 같은 분수인 $$수식$${b_1} over {a_1}$$/수식$$, $$수식$${b_2} over {a_2}$$/수식$$, " \
              "$$수식$${b_3} over {a_3}$$/수식$$, $$수식$${b_4} over {a_4} CDOTS CDOTS $$/수식$$중에서 분모와 분자의 합이 $$수식$${c_}$$/수식$$인 " \
              "분수를 찾으면 $$수식$${e_} over {d_}$$/수식$$입니다.\n\n"


    a_ = np.random.randint(3, 10)
    b_ = np.random.randint(2, a_)

    while(gcd(a_, b_) != 1) :
        a_ = np.random.randint(3, 10)
        b_ = np.random.randint(2, a_)

    a1 = 2
    a2 = 3
    a3 = 4
    a4 = 5

    a_1 = a_ * a1
    b_1 = b_ * a1
    a_2 = a_ * a2
    b_2 = b_ * a2

    a_3 = a_ * a3
    b_3 = b_ * a3
    a_4 = a_ * a4
    b_4 = b_ * a4

    c_ = [a_2 + b_2, a_3 + b_3, a_4 + b_4][np.random.randint(0, 3)]

    if c_ == a_2 + b_2 :
        d_ = a_2
        e_ = b_2
    elif c_ == a_3 + b_3 :
        d_ = a_3
        e_ = b_3
    else :
        d_ = a_4
        e_ = b_4

    j1 = proc_jo(b_, 2)

    stem = stem.format(j1 = j1, a_ = a_, b_ = b_, c_ = c_)
    answer = answer.format(e_ = e_, d_ = d_)
    comment = comment.format(j1 = j1, a_ = a_, b_ = b_, c_ = c_, d_ = d_, e_ = e_, a_1 = a_1, b_1 = b_1, a_2 = a_2, b_2 = b_2, a_3 = a_3, b_3 = b_3, a_4 = a_4, b_4 = b_4)

    return stem, answer, comment
























# 5-1-4-16
def reductionfra514_Stem_008():
    stem = "어느 의회에서 어떤 결정을 할 때에는 전체 의원 $$수식$${c_}$$/수식$$명 중 적어도 $$수식$${d_}$$/수식$$명이 찬성해야 한다고 합니다. ㉠에 알맞은 수를 구해 보세요.\n$$표$$ 의회의 결정은 적어도 전체 의원 수의 $$수식$${lg}㉠{rg} over {a_}$$/수식$$이 찬성해야 합니다. $$/표$$\n"
    answer = "(정답)\n$$수식$${b_}$$/수식$$\n"
    comment = "(해설)\n전체 의원 $$수식$${c_}$$/수식$$명 중 적어도 $$수식$${d_}$$/수식$$명이 찬성해야 하므로 $$수식$${d_} over {c_}$$/수식$$입니다.\n"\
              "$$수식$${d_} over {c_} ` = ` {lg}㉠{rg} over {a_}$$/수식$$이고, $$수식$${c_} ` div ` {a} ` = `{a_}$$/수식$$이므로 $$수식$$㉠ ` = `{d_} ` div ` {a} ` = ` {b_}$$/수식$$입니다.\n\n"


    a_ = np.random.randint(3, 10)
    b_ = np.random.randint(2, a_)

    while (gcd(a_, b_) != 1) or 0.5 > a_/b_ :
        a_ = np.random.randint(3, 10)
        b_ = np.random.randint(2, a_)

    a = [50, 60, 70, 80, 90, 100][np.random.randint(0, 6)]

    c_ = a_ * a
    d_ = b_ * a

    lg = "{"
    rg = "}"

    stem = stem.format(lg = lg, rg = rg, a_ = a_, c_ = c_, d_ = d_)
    answer = answer.format(b_ = b_)
    comment = comment.format(lg = lg, rg = rg, a_ = a_, c_ = c_, d_ = d_, a = a, b_ = b_)

    return stem, answer, comment


























# 5-1-4-17
def reductionfra514_Stem_009():
    stem = "대화를 읽고 크기가 같은 분수를 같은 방법으로 구한 두 사람을 찾아 써 보세요.\n$$표$$ {s1}\n \n{s2}\n \n{s3}$$/표$$\n"
    answer = "(정답)\n{aone}, {atwo}\n"
    comment = "(해설)\n{aone}{j7} {atwo}{j8} {x} 크기가 같은 분수를 만들었습니다.\n" \
              "{na}{j9} {y} 크기가 같은 분수를 만들었습니다.\n" \
              "따라서 크기가 같은 분수를 같은 방법으로 구한 두 사람은 {aone}{j7} {atwo}입니다.\n\n"


    wh_list = ['수지', '은호', '선루', '윤서', '지우', '정호', '현기', '재수', '영서', '은지', '연주', '주호', '혁구', '영기', '상수', '은서', '동우',
               '재우', '진희', '준서', '유라', '수미', '현수', '채아', '민주', '지호', '연아', '은우', '시우', '혁재', '민하']

    wh1 = wh_list.pop(np.random.randint(0, len(wh_list)))
    wh2 = wh_list.pop(np.random.randint(0, len(wh_list)))
    wh3 = wh_list.pop(np.random.randint(0, len(wh_list)))

    n = np.random.randint(0, 2)

    a1 = np.random.randint(3, 10)
    b1 = np.random.randint(2, a1)

    while (gcd(a1, b1) != 1) :
        a1 = np.random.randint(3, 10)
        b1 = np.random.randint(2, a1)

    c1 = np.random.randint(3, 10)
    d1 = np.random.randint(2, c1)

    while (gcd(c1, d1) != 1) or c1 == a1:
        c1 = np.random.randint(3, 10)
        d1 = np.random.randint(2, c1)

    e1 = np.random.randint(3, 10)
    f1 = np.random.randint(2, e1)

    while (gcd(e1, f1) != 1) or e1 == a1 or e1 == c1:
        e1 = np.random.randint(3, 10)
        f1 = np.random.randint(2, e1)

    n_list = [2, 3, 4, 5, 6, 7, 8, 9]

    a = n_list.pop(np.random.randint(0, len(n_list)))
    c = n_list.pop(np.random.randint(0, len(n_list)))
    e = n_list.pop(np.random.randint(0, len(n_list)))

    a2 = a1 * a
    b2 = b1 * a
    c2 = c1 * c

    d2 = d1 * c
    e2 = e1 * e
    f2 = f1 * e

    g_ = "분모와 분자에 $$수식$$0$$/수식$$이 아닌 같은 수를 곱하여"
    h_ = "분모와 분자를 $$수식$$0$$/수식$$이 아닌 같은 수를 나누어"

    if n == 0 :
        a_ = a1
        b_ = b1
        a_1 = a2
        b_1 = b2
        c_ = c1
        d_ = d1
        c_1 = c2
        d_1 = d2
        e_ = e2
        f_ = f2
        e_1 = e1
        f_1 = f1
        x = g_
        y = h_
    else :
        a_ = a2
        b_ = b2
        a_1 = a1
        b_1 = b1
        c_ = c2
        d_ = d2
        c_1 = c1
        d_1 = d1
        e_ = e1
        f_ = f1
        e_1 = e2
        f_1 = f2
        x = h_
        y = g_

    j1 = proc_jo(b_, 2)
    j2 = proc_jo(d_, 2)
    j3 = proc_jo(f_, 2)

    j4 = proc_jo(b_1, 0)
    j5 = proc_jo(d_1, 0)
    j6 = proc_jo(f_1, 0)

    j7 = proc_jo(wh1, 2)
    j8 = proc_jo(wh2, -1)
    j9 = proc_jo(wh3, -1)

    x1 = f"$$수식$$LEFT [$$/수식$${wh1}$$수식$$RIGHT ] ```` {b_} over {a_}$$/수식$${j1} 크기가 같은 분수에는 $$수식$${b_1} over {a_1}$$/수식$${j4} 있어."
    x2 = f"$$수식$$LEFT [$$/수식$${wh2}$$수식$$RIGHT ] ```` {d_} over {c_}$$/수식$${j2} 크기가 같은 분수에는 $$수식$${d_1} over {c_1}$$/수식$${j5} 있어."
    x3 = f"$$수식$$LEFT [$$/수식$${wh3}$$수식$$RIGHT ] ```` {f_} over {e_}$$/수식$${j3} 크기가 같은 분수에는 $$수식$${f_1} over {e_1}$$/수식$${j6} 있어."

    candidates = [x1, x2, x3]
    np.random.shuffle(candidates)
    [s1, s2, s3] = candidates

    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == x1:
            aone = wh1
        elif sdx == x2 :
            atwo = wh2
        else :
            na = wh3

    stem = stem.format(s1 = s1, s2 = s2, s3 = s3)
    answer = answer.format(aone = aone, atwo = atwo)
    comment = comment.format(aone = aone, atwo = atwo, na = na, j7 = j7, j8 = j8, j9 = j9, x = x, y = y)

    return stem, answer, comment
























# 5-1-4-18
def reductionfra514_Stem_010():
    stem = "$$수식$${b_} over {a_}$$/수식$${j1} 크기가 같은 분수 중에서 분모와 분자의 합이 $$수식$${c_}$$/수식$$보다 크고 $$수식$${d_}$$/수식$$보다 작은 분수를 모두 써 보세요.\n"
    answer = "(정답)\n{s1}\n"
    comment = "(해설)\n$$수식$${b_} over {a_}$$/수식$${j1} 크기가 같은 분수를 구하면 $$수식$${b_} over {a_} ` = ` {b_1} over {a_1} ` = ` {b_2} over {a_2} " \
              "` = ` {b_3} over {a_3} ` = ` {b_4} over {a_4} ` = ` {b_5} over {a_5} CDOTS CDOTS $$/수식$$입니다.\n"\
              "따라서 분모와 분자의 합이 $$수식$${c_}$$/수식$$보다 크고 $$수식$${d_}$$/수식$$보다 작은 분수는 {s1}입니다.\n\n"


    a_ = np.random.randint(4, 10)
    b_ = np.random.randint(2, a_)

    while (gcd(a_, b_) != 1):
        a_ = np.random.randint(4, 10)
        b_ = np.random.randint(2, a_)

    a1 = 2
    a2 = 3
    a3 = 4
    a4 = 5
    a5 = 6

    a_1 = a_ * a1
    b_1 = b_ * a1
    a_2 = a_ * a2
    b_2 = b_ * a2

    a_3 = a_ * a3
    b_3 = b_ * a3
    a_4 = a_ * a4
    b_4 = b_ * a4

    a_5 = a_ * a5
    b_5 = b_ * a5

    c_1 = np.random.randint(a_1+b_1+1, a_2+b_2)

    while c_1 % 5 != 0 :
        c_1 = np.random.randint(a_1+b_1+1, a_2+b_2)

    c_2 = np.random.randint(a_2 + b_2 + 1, a_3 + b_3)

    while c_2 % 5 != 0:
        c_2 = np.random.randint(a_2 + b_2 + 1, a_3 + b_3)

    c_3 = np.random.randint(a_3 + b_3 + 1, a_4 + b_4)

    while c_3 % 5 != 0:
        c_3 = np.random.randint(a_3 + b_3 + 1, a_4 + b_4)

    c_4 = np.random.randint(a_4 + b_4 + 1, a_5 + b_5)

    while c_4 % 5 != 0:
        c_4 = np.random.randint(a_4 + b_4 + 1, a_5 + b_5)

    n = np.random.randint(0, 3)

    if n == 0 :
        c_ = c_1
        d_ = c_3
        s1 = f"$$수식$${b_2} over {a_2}$$/수식$$, $$수식$${b_3} over {a_3}$$/수식$$"
    elif n == 1 :
        c_ = c_1
        d_ = c_4
        s1 = f"$$수식$${b_2} over {a_2}$$/수식$$, $$수식$${b_3} over {a_3}$$/수식$$, $$수식$${b_4} over {a_4}$$/수식$$"
    else :
        c_ = c_2
        d_ = c_4
        s1 = f"$$수식$${b_3} over {a_3}$$/수식$$, $$수식$${b_4} over {a_4}$$/수식$$"

    j1 = proc_jo(b_, 2)

    stem = stem.format(j1 = j1, a_ = a_, b_ = b_, c_ = c_, d_ = d_)
    answer = answer.format(s1 = s1)
    comment = comment.format(j1 = j1, a_ = a_, b_ = b_, c_ = c_, d_ = d_, a_1 = a_1, b_1 = b_1, a_2 = a_2, b_2 = b_2, a_3 = a_3, b_3 = b_3, a_4 = a_4, b_4 = b_4, a_5 = a_5, b_5 = b_5, s1 = s1)

    return stem, answer, comment


























# 5-1-4-19
def reductionfra514_Stem_011():
    stem = "$$수식$${n_} over {m_}$$/수식$${j1} 크기가 같은 분수 중에서 분모와 분자의 합이 $$수식$${c_}$$/수식$$보다 크고 $$수식$${d_}$$/수식$$보다 작은 분수를 모두 써 보세요.\n"
    answer = "(정답)\n{s1}\n"
    comment = "(해설)\n$$수식$${n_} over {m_}$$/수식$${j1} 크기가 같은 분수 중 분모가 가장 작은 분수는 $$수식$${b_} over {a_}$$/수식$$입니다.\n" \
              "$$수식$${b_} over {a_}$$/수식$${j2} 크기가 같은 분수를 구하면 \n" \
              "$$수식$${b_} over {a_} `=` {b_1} over {a_1} `=` {b_2} over {a_2} " \
              "`=` {b_3} over {a_3} `=` {b_4} over {a_4} `=` {b_5} over {a_5} `=` {b_6} over {a_6} CDOTS CDOTS $$/수식$$입니다.\n"\
              "따라서 분모와 분자의 합이 $$수식$${c_}$$/수식$$보다 크고 $$수식$${d_}$$/수식$$보다 작은 분수는 {s1}입니다.\n\n"


    ab_list = [[5, 2], [4, 3], [5, 3], [5, 4]][np.random.randint(0, 4)]
    a_ = ab_list[0]
    b_ = ab_list[1]

    mn_list = [[a_*16, b_*16], [a_*9, b_*9]][np.random.randint(0, 2)]
    m_ = mn_list[0]
    n_ = mn_list[1]

    a1 = 2
    a2 = 3
    a3 = 4

    a4 = 5
    a5 = 6
    a6 = 7

    a_1 = a_ * a1
    b_1 = b_ * a1
    a_2 = a_ * a2
    b_2 = b_ * a2

    a_3 = a_ * a3
    b_3 = b_ * a3
    a_4 = a_ * a4
    b_4 = b_ * a4

    a_5 = a_ * a5
    b_5 = b_ * a5
    a_6 = a_ * a6
    b_6 = b_ * a6

    c_1 = np.random.randint(a_1+b_1+1, a_2+b_2)

    while c_1 % 5 != 0 :
        c_1 = np.random.randint(a_1+b_1+1, a_2+b_2)

    c_2 = np.random.randint(a_2 + b_2 + 1, a_3 + b_3)

    while c_2 % 5 != 0:
        c_2 = np.random.randint(a_2 + b_2 + 1, a_3 + b_3)

    c_3 = np.random.randint(a_3 + b_3 + 1, a_4 + b_4)

    while c_3 % 5 != 0:
        c_3 = np.random.randint(a_3 + b_3 + 1, a_4 + b_4)

    c_4 = np.random.randint(a_4 + b_4 + 1, a_5 + b_5)

    while c_4 % 5 != 0:
        c_4 = np.random.randint(a_4 + b_4 + 1, a_5 + b_5)

    c_5 = np.random.randint(a_5 + b_5 + 1, a_6 + b_6)

    while c_5 % 5 != 0:
        c_5 = np.random.randint(a_5 + b_5 + 1, a_6 + b_6)

    n = np.random.randint(0, 4)

    if n == 0 :
        c_ = c_1
        d_ = c_3
        s1 = f"$$수식$${b_2} over {a_2}$$/수식$$, $$수식$${b_3} over {a_3}$$/수식$$"
    elif n == 1 :
        c_ = c_2
        d_ = c_4
        s1 = f"$$수식$${b_3} over {a_3}$$/수식$$, $$수식$${b_4} over {a_4}$$/수식$$"
    elif n == 2 :
        c_ = c_2
        d_ = c_5
        s1 = f"$$수식$${b_3} over {a_3}$$/수식$$, $$수식$${b_4} over {a_4}$$/수식$$, $$수식$${b_5} over {a_5}$$/수식$$"
    else :
        c_ = c_3
        d_ = c_5
        s1 = f"$$수식$${b_4} over {a_4}$$/수식$$, $$수식$${b_5} over {a_5}$$/수식$$"

    j1 = proc_jo(n_, 2)
    j2 = proc_jo(b_, 2)

    stem = stem.format(j1 = j1, n_ = n_, m_ = m_, c_ = c_, d_ = d_)
    answer = answer.format(s1 = s1)
    comment = comment.format(j1 = j1, j2 = j2, m_ = m_, n_= n_, a_ = a_, b_ = b_, c_ = c_, d_ = d_, a_1 = a_1, b_1 = b_1, a_2 = a_2, b_2 = b_2, a_3 = a_3, b_3 = b_3, a_4 = a_4, b_4 = b_4, a_5 = a_5, b_5 = b_5, a_6 = a_6, b_6 = b_6, s1 = s1)

    return stem, answer, comment



























# 5-1-4-20
def reductionfra514_Stem_012():
    stem = "$$수식$${b_} over {a_}$$/수식$${j1} 크기가 같은 분수 중에서 분모와 분자의 차가 $$수식$${c_}$$/수식$$인 분수를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${aone}$$/수식$$\n"
    comment = "(해설)\n$$수식$${b_} over {a_}$$/수식$${j1} 크기가 같은 분수를 구하면 " \
              "$$수식$${b_} over {a_} ` = ` {b_1} over {a_1} ` = ` {b_2} over {a_2} " \
              "` = ` {b_3} over {a_3} ` = ` {b_4} over {a_4} CDOTS CDOTS $$/수식$$입니다.\n"\
              "따라서 분모와 분자의 차가 $$수식$${c_}$$/수식$$인 분수는 $$수식$${aone}$$/수식$$입니다.\n\n"


    a_ = np.random.randint(3, 10)
    b_ = np.random.randint(2, a_)

    while (gcd(a_, b_) != 1):
        a_ = np.random.randint(3, 10)
        b_ = np.random.randint(2, a_)

    a1 = 2
    a2 = 3
    a3 = 4
    a4 = 5

    a_1 = a_ * a1
    b_1 = b_ * a1
    a_2 = a_ * a2
    b_2 = b_ * a2

    a_3 = a_ * a3
    b_3 = b_ * a3
    a_4 = a_ * a4
    b_4 = b_ * a4

    answer_list = [[a_1 - b_1, f"{b_1} over {a_1}"], [a_2 - b_2, f"{b_2} over {a_2}"] , [a_3 - b_3, f"{b_3} over {a_3}"] , [a_4 - b_4, f"{b_4} over {a_4}"]][np.random.randint(0, 4)]

    c_ = answer_list[0]
    aone = answer_list[1]

    j1 = proc_jo(b_, 2)

    stem = stem.format(j1 = j1, a_ = a_, b_ = b_, c_ = c_)
    answer = answer.format(aone = aone)
    comment = comment.format(j1 = j1, a_ = a_, b_ = b_, c_ = c_, a_1 = a_1, b_1 = b_1, a_2 = a_2, b_2 = b_2, a_3 = a_3, b_3 = b_3, a_4 = a_4, b_4 = b_4, aone = aone)

    return stem, answer, comment

























# 5-1-4-21
def reductionfra514_Stem_013():
    stem = "$$수식$${b_} over {a_}$$/수식$${j1} 약분하려고 합니다. 분모와 분자를 나눌 수 없는 수는 어느 것인가요?\n① $$수식$${s1}$$/수식$$   ② $$수식$${s2}$$/수식$$    ③ $$수식$${s3}$$/수식$$    ④ $$수식$${s4}$$/수식$$   ⑤ $$수식$${s5}$$/수식$$\n"
    answer = "(정답)\n{aone}\n"
    comment = "(해설)\n$$수식$${b_} over {a_}$$/수식$${j1} 약분할 때 $$수식$${a_}$$/수식$${j2} $$수식$${b_}$$/수식$$의 공약수가 " \
              "$$수식$$1$$/수식$$, $$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$, $$수식$${a4}$$/수식$$, " \
              "$$수식$${a5}$$/수식$$이므로 분모와 분자를 나눌 수 있는 수는 " \
              "$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$, $$수식$${a4}$$/수식$$, $$수식$${a5}$$/수식$$입니다.\n\n"


    a = np.random.randint(2, 4)
    b = [3, 5, 7][np.random.randint(0, 3)]

    while b <= a :
        b = [3, 5, 7][np.random.randint(0, 3)]

    c = [1, 2, 3, 5][np.random.randint(0, 4)]
    d = [1, 2, 3, 5][np.random.randint(0, 4)]

    while c >= d or d > 189 / (a*a*b):
        c = [1, 2, 3, 5][np.random.randint(0, 4)]
        d = [1, 2, 3, 5][np.random.randint(0, 4)]

    a1 = a
    a2 = min(a*a, b)
    a3 = max(a*a, b)

    a4 = a*b
    a5 = a*a*b
    a6 = b*b

    b_list = [a1, a2, a3, a4, a5]

    b1 = b_list.pop(np.random.randint(0, len(b_list)))
    b2 = b_list.pop(np.random.randint(0, len(b_list)))
    b3 = b_list.pop(np.random.randint(0, len(b_list)))
    b4 = b_list.pop(np.random.randint(0, len(b_list)))
    b5 = b_list.pop(np.random.randint(0, len(b_list)))

    a_ = a5 * d
    b_ = a5 * c

    j1 = proc_jo(b_, 4)
    j2 = proc_jo(a_, 2)

    candidates = [b1, b2, b3, b4, a6]
    np.random.shuffle(candidates)
    [s1, s2, s3, s4, s5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == a6:
            correct_idx = idx
            break

    stem = stem.format(j1 = j1, a_ = a_, b_ = b_, s1 = s1, s2 = s2, s3 = s3, s4 = s4, s5 = s5)
    answer = answer.format(aone = answer_dict[correct_idx])
    comment = comment.format(j1 = j1, j2 = j2, a_ = a_, b_ = b_, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)

    return stem, answer, comment




























# 5-1-4-22
def reductionfra514_Stem_014():
    stem = "다음 중 약분할 수 있는 분수는 모두 몇 개인가요?\n$$표$$ $$수식$$ {s1} $$/수식$$    $$수식$$ {s2} $$/수식$$    $$수식$$ {s3} $$/수식$$    $$수식$$ {s4} $$/수식$$    $$수식$$ {s5} $$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${aone}$$/수식$$개\n"
    comment = "(해설)\n분모와 분자의 공약수가 $$수식$$1$$/수식$$ 외에도 더 있으면 약분할 수 있습니다.\n"\
              "{x_}이므로 {y_} 약분할 수 있습니다.\n"\
              "따라서 약분할 수 있는 분수는 $$수식$${aone}$$/수식$$개입니다.\n\n"


    abc_list = [2, 3, 5, 7, 11]

    a = abc_list.pop(np.random.randint(0, len(abc_list)))
    b = abc_list.pop(np.random.randint(0, len(abc_list)))
    c = abc_list.pop(np.random.randint(0, len(abc_list)))

    n_list = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

    a_1 = n_list.pop(np.random.randint(0, len(n_list)))
    b_1 = n_list.pop(np.random.randint(0, len(n_list)))

    while gcd(a_1, b_1) != 1 or b_1 >= a_1 or a_1*a<25 or a_1*a>121 :
        abc_list.append(a)
        abc_list.append(b)
        abc_list.append(c)
        a = abc_list.pop(np.random.randint(0, len(abc_list)))
        b = abc_list.pop(np.random.randint(0, len(abc_list)))
        c = abc_list.pop(np.random.randint(0, len(abc_list)))
        n_list.append(a_1)
        n_list.append(b_1)
        a_1 = n_list.pop(np.random.randint(0, len(n_list)))
        b_1 = n_list.pop(np.random.randint(0, len(n_list)))

    c_1 = n_list.pop(np.random.randint(0, len(n_list)))
    d_1 = n_list.pop(np.random.randint(0, len(n_list)))

    while gcd(c_1, d_1) != 1 or c_1 >= d_1 or c_1 * b < 25 or c_1 * b > 121:
        abc_list.append(b)
        abc_list.append(c)
        b = abc_list.pop(np.random.randint(0, len(abc_list)))
        c = abc_list.pop(np.random.randint(0, len(abc_list)))
        n_list.append(c_1)
        n_list.append(d_1)
        c_1 = n_list.pop(np.random.randint(0, len(n_list)))
        d_1 = n_list.pop(np.random.randint(0, len(n_list)))

    e_1 = n_list.pop(np.random.randint(0, len(n_list)))
    f_1 = n_list.pop(np.random.randint(0, len(n_list)))

    while gcd(e_1, f_1) != 1 or e_1 >= f_1 or e_1 * c < 25 or e_1 * c > 121:
        abc_list.append(c)
        c = abc_list.pop(np.random.randint(0, len(abc_list)))
        n_list.append(e_1)
        n_list.append(f_1)
        e_1 = n_list.pop(np.random.randint(0, len(n_list)))
        f_1 = n_list.pop(np.random.randint(0, len(n_list)))

    a_ = a_1 * a
    b_ = b_1 * a
    c_ = c_1 * b
    d_ = d_1 * b

    n = np.random.randint(2, 4)

    if n == 2 :
        e_ = np.random.randint(31, 90)
        f_ = np.random.randint(30, e_)

        while gcd(e_, f_) != 1 or e_ == a_ or e_ == c_ or f_ == b_ or f_ == d_ :
            e_ = np.random.randint(31, 90)
            f_ = np.random.randint(30, e_)

        j1 = proc_jo(d_, -1)
        j2 = proc_jo(b_, 2)
        j3 = proc_jo(d_, 2)

        x_ = f"$$수식$${b_}$$/수식$${j2} $$수식$${a_}$$/수식$$의 공약수는 $$수식$$1$$/수식$$, $$수식$${a}$$/수식$$이고, " \
            f"$$수식$${d_}$$/수식$${j3} $$수식$${c_}$$/수식$$의 공약수는 $$수식$$1$$/수식$$, $$수식$${b}$$/수식$$"
        y_ = f"$$수식$${b_} over {a_}$$/수식$$, $$수식$${d_} over {c_}$$/수식$${j1}"

    else :
        e_ = e_1 * c
        f_ = f_1 * c

        j1 = proc_jo(f_, -1)
        j2 = proc_jo(b_, 2)
        j3 = proc_jo(d_, 2)
        j4 = proc_jo(f_, 2)

        x_ = f"$$수식$${b_}$$/수식$${j2} $$수식$${a_}$$/수식$$의 공약수는 $$수식$$1$$/수식$$, $$수식$${a}$$/수식$$이고, " \
            f"$$수식$${d_}$$/수식$${j3} $$수식$${c_}$$/수식$$의 공약수는 $$수식$$1$$/수식$$, $$수식$${b}$$/수식$$이고, " \
            f"$$수식$${f_}$$/수식$${j4} $$수식$${e_}$$/수식$$의 공약수는 $$수식$$1$$/수식$$, $$수식$${c}$$/수식$$"
        y_ = f"$$수식$${b_} over {a_}$$/수식$$, $$수식$${d_} over {c_}$$/수식$$, $$수식$${f_} over {e_}$$/수식$${j1}"

    g_ = np.random.randint(30, 90)
    h_ = np.random.randint(30, 90)

    while gcd(g_, h_) != 1 or g_ == h_ or g_ == a_ or g_ == c_ or g_ == e_ or h_ == b_ or h_ == d_ or h_ == f_ :
        g_ = np.random.randint(30, 90)
        h_ = np.random.randint(30, 90)

    i_ = np.random.randint(30, 90)
    j_ = np.random.randint(30, 90)

    while gcd(i_, j_) != 1 or i_ == g_ or i_ == h_ or j_ == g_ or j_ == h_ or j_ == i_ or i_ == a_ or i_ == c_ or i_ == e_ or j_ == b_ or j_ == d_ or j_ == f_ :
        i_ = np.random.randint(30, 90)
        j_ = np.random.randint(30, 90)

    x1 = f"{b_} over {a_}"
    x2 = f"{d_} over {c_}"
    x3 = f"{f_} over {e_}"
    x4 = f"{h_} over {g_}"
    x5 = f"{j_} over {i_}"

    candidates = [x1, x2, x3, x4, x5]
    np.random.shuffle(candidates)
    [s1, s2, s3, s4, s5] = candidates

    stem = stem.format(s1 = s1, s2 = s2, s3 = s3, s4 = s4, s5 = s5)
    answer = answer.format(aone = n)
    comment = comment.format(x_ = x_, y_ = y_, aone = n)

    return stem, answer, comment



























# 5-1-4-24
def reductionfra514_Stem_015():
    stem = "$$수식$${b_} over {a_}$$/수식$${j1} 옳게 약분한 사람을 찾아 이름을 써 보세요.\n$$표$$ {s1}\n \n{s2}\n \n{s3} $$/표$$\n"
    answer = "(정답)\n{aone}\n"
    comment = "(해설)\n{z1}\n" \
              "{z2}\n\n"


    wh_list = ['수지', '은호', '선루', '윤서', '지우', '정호', '현기', '재수', '영서', '은지', '연주', '주호', '혁구', '영기', '상수', '은서', '동우',
               '재우', '진희', '준서', '유라', '수미', '현수', '채아', '민주', '지호', '연아', '은우', '시우', '혁재', '민하']

    wh1 = wh_list.pop(np.random.randint(0, len(wh_list)))
    wh2 = wh_list.pop(np.random.randint(0, len(wh_list)))
    wh3 = wh_list.pop(np.random.randint(0, len(wh_list)))

    ab_list = [[2, 2], [2, 3], [2, 5], [2, 7], [3, 3], [3, 5]][np.random.randint(0, 6)]
    a = ab_list[0]
    b = ab_list[1]

    c = np.random.randint(3, 6)
    d = np.random.randint(2, c)

    while ( gcd(c, d) != 1 or d == a ):
        c = np.random.randint(3, 6)
        d = np.random.randint(2, c)

    e = np.random.randint(2, 4)

    a_ = a * b * c
    b_ = a * b * d

    c_ = a * b
    d_ = b * d
    e_ = a_ * e
    f_ = b_ * e

    j1 = proc_jo(b_, 4)
    j2 = proc_jo(a_, 4)

    j3 = proc_jo(a, 0)
    j4 = proc_jo(d, 0)
    j5 = proc_jo(e, 4)

    j6 = proc_jo(f_, 0)
    j7 = proc_jo(a_, 2)

    if c_ == 3 or c_ == 6:
        ro1 = "으로"
    else:
        ro1 = "로"

    if d_ == 3 or d_ == 6:
        ro2 = "으로"
    else:
        ro2 = "로"

    x1 = f"$$수식$$LEFT [$$/수식$${wh1}$$수식$$RIGHT ]$$/수식$$ 분모와 분자를 $$수식$${a_}$$/수식$${j7} $$수식$${b_}$$/수식$$의 최대공약수인 $$수식$${c_}$$/수식$${ro1} 나누니 " \
         f"$$수식$${d} over {c}$$/수식$${j4} 되었어."
    x2 = f"$$수식$$LEFT [$$/수식$${wh2}$$수식$$RIGHT ]$$/수식$$ 분모 $$수식$${a_}$$/수식$${j2} $$수식$${c_}$$/수식$${ro1} 나누고, 분자 $$수식$${b_}$$/수식$${j1} $$수식$${d_}$$/수식$${ro2} 나누니 " \
         f"$$수식$${a} over {c}$$/수식$${j3} 되었어."
    x3 = f"$$수식$$LEFT [$$/수식$${wh3}$$수식$$RIGHT ]$$/수식$$ 분모 $$수식$${a_}$$/수식$${j7} 분자 $$수식$${b_}$$/수식$$에 각각 $$수식$${e}$$/수식$${j5} 곱하니 " \
         f"$$수식$${f_} over {e_}$$/수식$${j6} 되었어."



    candidates = [x1, x2, x3]
    np.random.shuffle(candidates)
    [s1, s2, s3] = candidates

    if s1 == x1 :
        z1 = f"$$수식$$LEFT [$$/수식$${wh2}$$수식$$RIGHT ]$$/수식$$ 분모와 분자를 각각 다른 수로 나누었으므로 옳은 방법이 아닙니다."
        z2 = f"$$수식$$LEFT [$$/수식$${wh3}$$수식$$RIGHT ]$$/수식$$ 약분한 것이 아니라 분모와 분자에 각각 같은 수를 곱하여 크기가 같은 분수를 만들었습니다."
    else :
        z2 = f"$$수식$$LEFT [$$/수식$${wh2}$$수식$$RIGHT ]$$/수식$$ 분모와 분자를 각각 다른 수로 나누었으므로 옳은 방법이 아닙니다."
        z1 = f"$$수식$$LEFT [$$/수식$${wh3}$$수식$$RIGHT ]$$/수식$$ 약분한 것이 아니라 분모와 분자에 각각 같은 수를 곱하여 크기가 같은 분수를 만들었습니다."

    stem = stem.format(b_ = b_, a_ = a_, j1 = j1, s1 = s1, s2 = s2, s3 = s3)
    answer = answer.format(aone = wh1)
    comment = comment.format(z1 = z1, z2 = z2)

    return stem, answer, comment


























# 5-1-4-25
def reductionfra514_Stem_016():
    stem = "분모가 $$수식$${a_}$$/수식$$인 진분수 중에서 약분하면 $$수식$${d} over {c}$$/수식$${j1} 되는 분수를 써 보세요.\n"
    answer = "(정답)\n$$수식$${b_} over {a_}$$/수식$$\n"
    comment = "(해설)\n$$수식$${lg}□{rg} over {a_} ` = ` {lg}□ ` div ` {c_}{rg} over {lg}{a_} ` div ` {c_}{rg} ` = ` {d} over {c}$$/수식$$"\
              "→ □$$수식$$` div ` {c_} ` = ` {d}$$/수식$$이므로 □$$수식$$` = ` {d} ` times ` {c_} ` = ` {b_}$$/수식$$입니다.\n" \
              "따라서 구하는 분수는 $$수식$${b_} over {a_}$$/수식$$입니다.\n\n"


    ab_list = [[1, 7], [2, 2], [2, 3], [2, 7], [3, 3], [3, 4], [3, 5]][np.random.randint(0, 7)]

    a = ab_list[0]
    b = ab_list[1]

    c = np.random.randint(3, 8)
    d = np.random.randint(2, c)

    while gcd(c, d) != 1 or a*b*c > 99 :
        c = np.random.randint(3, 8)
        d = np.random.randint(2, c)

    a_ = a * b * c
    b_ = a * b * d
    c_ = a * b

    j1 = proc_jo(d, 0)

    lg = "{"
    rg = "}"

    stem = stem.format(a_ = a_, d = d, c = c, j1 = j1)
    answer = answer.format(b_ = b_, a_ = a_)
    comment = comment.format(lg = lg, rg = rg, a_ = a_, c_ = c_,  d = d, c = c, b_ = b_)

    return stem, answer, comment
























# 5-1-4-26
def reductionfra514_Stem_017():
    stem = "$$수식$$ {b_} over {a_} $$/수식$${j1} 약분하였더니 $$수식$${d} over {c}$$/수식$${j2} 되었습니다. 분모와 분자를 어떤 수로 나누었나요?\n"
    answer = "(정답)\n$$수식$${c_}$$/수식$$\n"
    comment = "(해설)\n$$수식$${b_} over {a_} ` = ` {lg}{b_} ` div ` □{rg} over {lg}{a_} ` div ` □{rg} ` = ` {d} over {c}$$/수식$$에서 " \
              "$$수식$${b_} ` div `$$/수식$$□$$수식$$` = ` {d}$$/수식$$, □$$수식$$` = ` {b_} ` div ` {d} ` = ` {c_}$$/수식$$입니다.\n\n"


    ab_list = [[1, 7], [2, 2], [2, 3], [2, 7], [3, 3], [3, 4], [3, 5]][np.random.randint(0, 7)]

    a = ab_list[0]
    b = ab_list[1]

    c = np.random.randint(3, 8)
    d = np.random.randint(2, c)

    while gcd(c, d) != 1 or a*b*c > 99 :
        c = np.random.randint(3, 8)
        d = np.random.randint(2, c)

    a_ = a * b * c
    b_ = a * b * d
    c_ = a * b

    j1 = proc_jo(b_, 4)
    j2 = proc_jo(d, 0)

    lg = "{"
    rg = "}"

    stem = stem.format(a_ = a_, b_ = b_, c = c, d = d, j1 = j1, j2 = j2)
    answer = answer.format(c_ = c_)
    comment = comment.format(lg = lg, rg = rg,a_ = a_, b_ = b_, c = c, d= d, c_ = c_)

    return stem, answer, comment



























# 5-1-4-27
def reductionfra514_Stem_018():
    stem = "분모가 $$수식$${a_}$$/수식$$인 진분수 중에서 기약분수는 모두 몇 개인지 구해 보세요.\n"
    answer = "(정답)\n$$수식$${n}$$/수식$$개\n"
    comment = "(해설)\n$$수식$$1$$/수식$$부터 $$수식$${b_}$$/수식$$까지의 수 중에서 $$수식$${a_}$$/수식$${j1} " \
              "공약수가 $$수식$$1$$/수식$$뿐인 수는 {x}입니다.\n"\
              "따라서 분모가 $$수식$${a_}$$/수식$$인 진분수 중에서 기약분수는 {y}로 모두 $$수식$${n}$$/수식$$개입니다.\n\n"


    a_ = [6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20][np.random.randint(0, 11)]
    b_ = a_ - 1

    x = ""
    y = ""

    n = 0

    for i in range(1, b_+1) :
        if gcd(a_, i) == 1 :
            x = x + f"$$수식$${i}$$/수식$$, "
            y = y + f"$$수식$${i} over {a_}$$/수식$$, "
            n = n + 1

    x = x[0:-2]
    y = y[0:-2]

    j1 = proc_jo(a_, 2)

    stem = stem.format(a_ = a_)
    answer = answer.format(n = n)
    comment = comment.format(j1 = j1, b_ = b_, a_ = a_, x = x, y = y, n= n)

    return stem, answer, comment


























# 5-1-4-28
def reductionfra514_Stem_019():
    stem = "어떤 분수의 분모와 분자를 각각 $$수식$${c_}$$/수식$${ro} 약분하였더니 $$수식$${d} over {c}$$/수식$${j1} 되었습니다. 어떤 분수를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${b_} over {a_}$$/수식$$\n"
    comment = "(해설)\n약분하기 전의 분수는 $$수식$${lg}{d} ` times ` {c_}{rg} over {lg}{c} ` times ` {c_}{rg} ` = ` {b_} over {a_}$$/수식$$입니다.\n"\
              "따라서 어떤 분수는 $$수식$${b_} over {a_}$$/수식$$입니다.\n\n"


    ab_list = [[1, 7], [2, 2], [2, 3], [2, 7], [3, 3], [3, 4], [3, 5]][np.random.randint(0, 7)]

    a = ab_list[0]
    b = ab_list[1]

    c = np.random.randint(3, 10)
    d = np.random.randint(2, c)

    while gcd(c, d) != 1 or a*b*c > 99:
        c = np.random.randint(3, 10)
        d = np.random.randint(2, c)

    a_ = a* b* c
    b_ = a* b* d
    c_ = a* b

    lg = "{"
    rg = "}"

    j1 = proc_jo(d, 0)

    if int((str(c_))[-1]) == 0 or int((str(c_))[-1]) == 3 or int((str(c_))[-1]) == 6:
        ro = "으로"
    else:
        ro = "로"

    stem = stem.format(c_ = c_, c = c, d = d, j1 = j1, ro=ro)
    answer = answer.format(b_ = b_, a_ = a_)
    comment = comment.format(c = c, lg = lg, rg = rg, d = d, c_ = c_, b_ = b_, a_ = a_)

    return stem, answer, comment

























# 5-1-4-29
def reductionfra514_Stem_020():
    stem = "{wh1}네 학교 학생 $$수식$${a_}$$/수식$$명 중에서 $$수식$${b_}$$/수식$$명이 안경을 썼습니다. 안경을 쓴 학생은 전체의 몇 분의 몇인지 기약분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${e} over {d}$$/수식$$\n"
    comment = "(해설)\n안경을 쓴 학생은 전체의 $$수식$${b_} over {a_}$$/수식$$입니다.\n"\
              "$$수식$${a_}$$/수식$${j1} $$수식$${b_}$$/수식$$의 최대공약수는 $$수식$${c_}$$/수식$$이므로 기약분수로 나타내면 " \
              "$$수식$${lg}{b_} ` div ` {c_}{rg} over {lg}{a_} ` div ` {c_}{rg} ` = ` {e} over {d}$$/수식$$입니다.\n\n"


    wh_list = ['연수', '수지', '은호', '선루', '윤서', '지우', '정호', '현기', '재수', '영서', '은지', '연주', '주호', '혁구', '영기', '상수',
               '은서', '동우', '재우', '진희', '준서', '유라', '수미', '현수', '채아', '민주', '지호', '연아', '은우', '시우', '혁재', '민하']

    wh1 = wh_list[np.random.randint(0, len(wh_list))]

    a = [2, 3, 5][np.random.randint(0, 3)]
    b = [2, 3, 5][np.random.randint(0, 3)]
    c = [2, 3, 5, 7][np.random.randint(0, 4)]

    while a*b*c > 75 or 18 > a*b*c :
        a = [2, 3, 5][np.random.randint(0, 3)]
        b = [2, 3, 5][np.random.randint(0, 3)]
        c = [2, 3, 5, 7][np.random.randint(0, 4)]

    c_ = a*b*c

    d = np.random.randint(3, 10)
    e = np.random.randint(2, d)

    while gcd(e, d) != 1 or c_*d > 300 :
        d = np.random.randint(3, 10)
        e = np.random.randint(2, d)

    a_ = c_ * d
    b_ = c_ * e

    lg = "{"
    rg = "}"

    j1 = proc_jo(a_, 2)

    stem = stem.format(wh1 = wh1, a_ = a_, b_ = b_)
    answer = answer.format(d = d, e = e)
    comment = comment.format(j1 = j1, lg = lg, rg = rg, b_ = b_, a_  = a_, c_ = c_, e = e, d = d)

    return stem, answer, comment























# 5-1-4-30
def reductionfra514_Stem_021():
    stem = "{s1}에 참여한 학생 $$수식$${a_}$$/수식$$명 중 {s2}{j1} 쓰지 않은 학생은 $$수식$${d_}$$/수식$$명입니다. {s1}에 참여한 학생 중에서 {s2}{j1} 쓴 학생은 전체 학생의 몇 분의 몇인지 기약분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${d} over {c}$$/수식$$\n"
    comment = "(해설)\n$$수식$$LEFT ($$/수식$${s2}{j1} 쓴 학생 수$$수식$$RIGHT ) ` = ` {a_} ` - ` {d_} ` = ` {b_} ` LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$\n"\
              "따라서 {s1}에 참여한 학생 중에서 {s2}{j1} 쓴 학생은 전체 학생의 " \
              "$$수식$${lg}{b_} ` div ` {c_}{rg} over {lg}{a_} ` div ` {c_}{rg} ` = ` {d} over {c}$$/수식$$입니다.\n\n"


    s1 = ['현장체험 학습', '박물관 관람', '대형 수족관 관람', '기념관 관람'][np.random.randint(0, 4)]
    s2 = ['모자', '안경'][np.random.randint(0, 2)]

    ab_list = [[1, 7], [2, 3], [2, 4], [2, 7], [3, 3], [3, 4], [3, 5]][np.random.randint(0, 7)]

    a = ab_list[0]
    b = ab_list[1]

    c = np.random.randint(3, 10)
    d = np.random.randint(2, c)

    while gcd(c, d) != 1 or a*b*c>75 or 30 > a*b*c or c/3>d or d>(c*4)/5 :
        c = np.random.randint(3, 10)
        d = np.random.randint(2, c)

    a_ = a*b*c
    b_ = a*b*d
    c_ = a*b
    d_ = a_ - b_

    lg = "{"
    rg = "}"

    j1 = proc_jo(s2, 4)

    stem = stem.format(s1 = s1, s2 = s2, j1 =j1, a_ = a_, d_ = d_)
    answer = answer.format(d = d, c = c)
    comment = comment.format(lg = lg, rg = rg, s1 = s1, s2 = s2, j1 = j1, a_ = a_, b_ = b_, c_ = c_, d_ = d_, c = c, d = d)

    return stem, answer, comment
























# 5-1-4-31
def reductionfra514_Stem_022():
    stem = "기약분수로 나타내었을 때 $$수식$${b} over {a}$$/수식$${j1} 되는 분수 중에서 분모가 가장 큰 두 자리 수인 분수를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${c_} over {a_}$$/수식$$\n"
    comment = "(해설)\n$$수식$${a} ` times ` {c} ` = ` {a_}$$/수식$$, $$수식$${a} ` times ` {d} ` = ` {b_}$$/수식$$이므로 " \
              "분모가 될 수 있는 가장 큰 두 자리 수는 $$수식$${a_}$$/수식$$입니다.\n"\
              "따라서 구하는 분수는 $$수식$${b} over {a} ` = ` {lg}{b} ` times ` {c}{rg} over {lg}{a} ` times ` {c}{rg} ` = ` {c_} over {a_}$$/수식$$입니다.\n\n"


    a = np.random.randint(6, 20)

    while a == 10 :
        a = np.random.randint(6, 20)

    b = np.random.randint(2, a)

    while gcd(a, b) != 1 :
        b = np.random.randint(2, a)

    c = np.random.randint(100/a-1, int(100/a)) +1

    d = c + 1

    a_ = a*c
    b_ = a*d
    c_ = b*c

    lg = "{"
    rg = "}"

    j1 = proc_jo(b, 0)

    stem = stem.format(b = b, a = a, j1 = j1)
    answer = answer.format(a_ = a_, c_ = c_)
    comment = comment.format(lg = lg, rg = rg, a = a, c = c, d = d, b = b, a_ = a_, b_ = b_, c_ =c_)

    return stem, answer, comment





























# 5-1-4-33
def reductionfra514_Stem_023():
    stem = "어떤 분수의 분모와 분자에 각각 $$수식$${a}$$/수식$${j1} 더하고, $$수식$${b}$$/수식$$로 약분하였더니 $$수식$${b_} over {a_}$$/수식$${j2} 되었습니다. 어떤 분수를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${f_} over {e_}$$/수식$$\n"
    comment = "(해설)\n∙ $$수식$${b}$$/수식$$로 약분하기 전의 분수: $$수식$${lg}{b_} ` times ` {b}{rg} over {lg}{a_} ` times ` {b}{rg} ` = ` {d_} over {c_}$$/수식$$\n" \
              "∙ 분모와 분자에 각각 $$수식$${a}$$/수식$${j1} 더하기 전의 분수: " \
              "$$수식$${lg} {d_} ` - ` {a} {rg} over {lg} {c_} ` - ` {a} {rg} ` = ` {f_} over {e_} $$/수식$$\n"\
              "따라서 어떤 분수는 $$수식$${f_} over {e_}$$/수식$$입니다.\n\n"


    a_ = np.random.randint(4, 16)
    b_ = np.random.randint(2, a_)

    while gcd(a_, b_) != 1 :
        b_ = np.random.randint(2, a_)

    b = np.random.randint(4, 10)

    while a_*b > 99 :
        b = np.random.randint(4, 10)

    a = np.random.randint(3, 10)

    while a > b_*b-1 :
        a = np.random.randint(3, 10)

    c_ = a_*b
    d_ = b_*b

    e_ = c_ - a
    f_ = d_ - a

    lg = "{"
    rg = "}"

    j1 = proc_jo(a, 4)
    j2 = proc_jo(b_, 0)

    stem = stem.format(j1 = j1, j2 = j2, a = a, b = b, a_ = a_, b_ = b_)
    answer = answer.format(f_ = f_, e_ = e_)
    comment = comment.format(lg = lg, rg = rg, b_ = b_, a_ = a_, c_ = c_, d_ = d_, e_ = e_, f_ = f_, b = b, a = a, j1 = j1)

    return stem, answer, comment


























# 5-1-4-35
def reductionfra514_Stem_024():
    stem = "분모가 $$수식$${a}$$/수식$$보다 크고 $$수식$${b}$$/수식$$보다 작은 진분수 중에서 기약분수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${n}$$/수식$$개\n"
    comment = "(해설)\n분모가 $$수식$${a}$$/수식$$보다 크고 $$수식$${b}$$/수식$$보다 작은 진분수는 " \
              "{x_1}{x_2}{x_3}입니다.\n"\
              "이 중에서 기약분수는 {y_1}{y_2}{y_3}로 모두 $$수식$${n}$$/수식$$개입니다.\n\n"


    a = np.random.randint(2, 6)

    b = a + 4

    a_1 = a+1
    a_2 = a+2
    a_3 = a+3

    n = 0

    x_1 = ""
    y_1 = ""
    x_2 = ""
    y_2 = ""

    x_3 = ""
    y_3 = ""

    for i in range(1, a_1):
        x_1 = x_1 + f"$$수식$${i} over {a_1}$$/수식$$, "
        if gcd(a_1, i) == 1 :
            n = n + 1
            y_1 = y_1 + f"$$수식$${i} over {a_1}$$/수식$$, "

    for i in range(1, a_2):
        x_2 = x_2 + f"$$수식$${i} over {a_2}$$/수식$$, "
        if gcd(a_2, i) == 1 :
            n = n + 1
            y_2 = y_2 + f"$$수식$${i} over {a_2}$$/수식$$, "

    for i in range(1, a_3):
        x_3 = x_3 + f"$$수식$${i} over {a_3}$$/수식$$, "
        if gcd(a_3, i) == 1 :
            n = n + 1
            y_3 = y_3 + f"$$수식$${i} over {a_3}$$/수식$$, "

    x_3 = x_3[0:-2]
    y_3 = y_3[0:-2]

    stem = stem.format(a = a, b = b)
    answer = answer.format(n = n)
    comment = comment.format(a = a, b = b, x_1 = x_1, x_2 = x_2, x_3 = x_3, y_1 = y_1, y_2 = y_2, y_3 = y_3, n = n)

    return stem, answer, comment

























# 5-1-4-36
def reductionfra514_Stem_025():
    stem = "두 분수와 크기가 같은 분수를 각각 만들어 분모가 가장 작은 수로 통분하여 보세요.\n$$표$$ $$수식$${a} over {a_}$$/수식$$      $$수식$${b} over {b_}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${d_} over {c_}$$/수식$$, $$수식$${e_} over {c_}$$/수식$$\n"
    comment = "(해설)\n크기가 같은 분수를 구하면 \n"\
              "{x}\n"\
              "{y}\n"\
              "따라서 가장 작은 수를 분모로 하여 통분하면 $$수식$${d_} over {c_}$$/수식$$, $$수식$${e_} over {c_}$$/수식$$입니다.\n\n"


    cde_list = [[2, 2, 3], [2, 2, 5], [2, 3, 4], [2, 4, 5], [3, 2, 3], [3, 2, 5], [3, 3, 4], [3, 3, 5], [4, 2, 3], [4, 2, 5], [4, 3, 4], [4, 3, 5], [4, 4, 5]][np.random.randint(13)]

    c = cde_list[0]
    d = cde_list[1]
    e = cde_list[2]

    a_ = c * d
    b_ = c * e

    a = np.random.randint(1, a_)

    x = "$$수식$$"
    y = "$$수식$$"

    while gcd(a, a_) != 1 :
        a = np.random.randint(1, a_)

    b = np.random.randint(1, b_)

    while gcd(b, b_) != 1 :
        b = np.random.randint(1, b_)

    for i in range(1, e+1):
        a_m = a_ * i
        am = a * i
        x = x + f"{am} over {a_m} ` = `"

    for i in range(1, d+1) :
        b_n = b_ * i
        bn = b * i
        y = y + f"{bn} over {b_n} ` = `"

    x = x + "CDOTS CDOTS$$/수식$$"
    y = y + "CDOTS CDOTS$$/수식$$"

    c_ = c*d*e
    d_ = a*e
    e_ = b*d

    stem = stem.format(a = a, b = b, a_ = a_, b_ = b_)
    answer = answer.format(c_ = c_, d_ = d_, e_ = e_)
    comment = comment.format(x = x, y = y, c_ = c_, d_ = d_, e_ = e_)

    return stem, answer, comment

























# 5-1-4-37
def reductionfra514_Stem_026():
    stem = "$$수식$$ LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$을 잘못 통분한 것을 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${s1}$$/수식$$      ㉡ $$수식$${s2}$$/수식$$\n \n㉢ $$수식$${s3}$$/수식$$      ㉣ $$수식$${s4}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{aone}\n"
    comment = "(해설)\n{aone}. {y}\n\n"


    cde_list = [[2, 2, 3], [2, 2, 5], [2, 3, 4], [2, 4, 5], [3, 2, 3], [3, 2, 5], [3, 3, 4], [3, 3, 5], [4, 2, 3], [4, 2, 5], [4, 3, 4], [4, 3, 5], [4, 4, 5]][np.random.randint(13)]

    c = cde_list[0]
    d = cde_list[1]
    e = cde_list[2]

    a_ = c * d
    b_ = c * e

    a = np.random.randint(1, a_)

    while gcd(a, a_) != 1:
        a = np.random.randint(1, a_)

    b = np.random.randint(1, b_)

    while gcd(b, b_) != 1:
        b = np.random.randint(1, b_)

    a_1 = a_ * e
    a_2 = a_ * e * 2
    a_3 = a_ * e * 3
    a_4 = a_ * e * 4

    e2 = e * 2
    e3 = e * 3
    e4 = e * 4

    d2 = d * 2
    d3 = d * 3
    d4 = d * 4

    f1 = a * e
    f2 = a * e * 2
    f3 = a * e * 3
    f4 = a * e * 4

    g1 = b * d
    g2 = b * d * 2
    g3 = b * d * 3
    g4 = b * d * 4

    b_1 = b_ * d
    b_2 = b_ * d2
    b_3 = b_ * d3
    b_4 = b_ * d4

    n = np.random.randint(2, 5)

    lg = "{"
    rg = "}"

    if n == 1:
        a1 = a * d
        a2 = a * e2
        a3 = a * e3
        a4 = a * e4

        b1 = b * e
        b2 = b * d2
        b3 = b * d3
        b4 = b * d4

        j1 = proc_jo(a_1, 4)

        y = f"$$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$에서 $$수식$${a_1}$$/수식$${j1} 공통분모로 하여 통분하면, \n" \
            f"$$수식$${a} over {a_} = {lg}{a} ` TIMES ` {e}{rg} over {lg}{a_} ` TIMES ` {e}{rg} ` = ` {f1} over {a_1}$$/수식$$, " \
            f"$$수식$${b} over {b_} = {lg}{b} ` TIMES ` {d}{rg} over {lg}{b_} ` TIMES ` {d}{rg} = {g1} over {b_1}$$/수식$$이므로 " \
            f"$$수식$$LEFT ( {f1} over {a_1} ,~ {g1} over {b_1} RIGHT )$$/수식$$입니다."

    elif n == 2:
        a1 = a * e
        a2 = a * d2
        a3 = a * e3
        a4 = a * e4

        b1 = b * d
        b2 = b * e2
        b3 = b * d3
        b4 = b * d4

        j1 = proc_jo(a_2, 4)

        y = f"$$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$에서 $$수식$${a_2}$$/수식$${j1} 공통분모로 하여 통분하면, \n" \
            f"$$수식$${a} over {a_} = {lg}{a} ` TIMES ` {e2}{rg} over {lg}{a_} ` TIMES ` {e2}{rg} ` = ` {f2} over {a_2}$$/수식$$, " \
            f"$$수식$${b} over {b_} = {lg}{b} ` TIMES ` {d2}{rg} over {lg}{b_} ` TIMES ` {d2}{rg} = {g2} over {b_2}$$/수식$$이므로 " \
            f"$$수식$$LEFT ( {f2} over {a_2} ,~ {g2} over {b_2} RIGHT )$$/수식$$입니다."

    elif n == 3:
        a1 = a * e
        a2 = a * e2
        a3 = a * d3
        a4 = a * e4

        b1 = b * d
        b2 = b * d2
        b3 = b * e3
        b4 = b * d4

        j1 = proc_jo(a_3, 4)

        y = f"$$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$에서 $$수식$${a_3}$$/수식$${j1} 공통분모로 하여 통분하면, \n" \
            f"$$수식$${a} over {a_} = {lg}{a} ` TIMES ` {e3}{rg} over {lg}{a_} ` TIMES ` {e3}{rg} = {f3} over {a_3}$$/수식$$, " \
            f"$$수식$${b} over {a_} = {lg}{b} ` TIMES ` {d3}{rg} over {lg}{b_} ` TIMES ` {d3}{rg} = {g3} over {b_3}$$/수식$$이므로 " \
            f"$$수식$$LEFT ( {f3} over {a_3} ,~ {g3} over {b_3} RIGHT )$$/수식$$입니다."

    else:
        a1 = a * e
        a2 = a * e2
        a3 = a * e3
        a4 = a * d4

        b1 = b * d
        b2 = b * d2
        b3 = b * d3
        b4 = b * e4

        j1 = proc_jo(a_4, 4)

        y = f"$$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$에서 $$수식$${a_4}$$/수식$${j1} 공통분모로 하여 통분하면, \n" \
            f"$$수식$${a} over {a_} = {lg}{a} ` TIMES ` {e4}{rg} over {lg}{a_} ` TIMES ` {e4}{rg} ` = ` {f4} over {a_4}$$/수식$$, " \
            f"$$수식$${b} over {b_} = {lg}{b} ` TIMES ` {d4}{rg} over {lg}{b_} ` TIMES ` {d4}{rg} = {g4} over {b_4}$$/수식$$이므로 " \
            f"$$수식$$LEFT ( {f4} over {a_4} ,~ {g2} over {b_4} RIGHT )$$/수식$$입니다."

    x1 = f"LEFT ( {a1} over {a_1} ,~ {b1} over {a_1} RIGHT )"
    x2 = f"LEFT ( {a2} over {a_2} ,~ {b2} over {a_2} RIGHT )"
    x3 = f"LEFT ( {a3} over {a_3} ,~ {b3} over {a_3} RIGHT )"
    x4 = f"LEFT ( {a4} over {a_4} ,~ {b4} over {a_4} RIGHT )"

    candidates = [x1, x2, x3, x4]
    np.random.shuffle(candidates)
    [s1, s2, s3, s4] = candidates

    correct_idx = 0

    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if n == 1 and sdx == x1:
            correct_idx = idx
            break
        elif n == 2 and sdx == x2:
            correct_idx = idx
            break
        elif n == 3 and sdx == x3:
            correct_idx = idx
            break
        elif n == 4 and sdx == x4:
            correct_idx = idx
            break

    stem = stem.format(a = a, b = b, a_ = a_, b_ = b_, s1 = s1, s2 = s2, s3 = s3, s4 = s4)
    answer = answer.format(aone = answer_kodict[correct_idx])
    comment = comment.format(aone = answer_kodict[correct_idx], y = y)

    return stem, answer, comment



























# 5-1-4-38
def reductionfra514_Stem_027():
    stem = "두 분수를 $$수식$${a_1}$$/수식$${j1} 공통분모로 하여 통분했습니다. ㉠, ㉡에 알맞은 수를 차례로 구해 보세요.\n$$표$$ $$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$ → $$수식$$ LEFT ( {lg}㉠{rg} over {a_1} ,~ {lg}㉡{rg} over {a_1} RIGHT )$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${b1}$$/수식$$\n"
    comment = "(해설)\n$$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$ → " \
              "$$수식$$ LEFT ( {lg}{a} ` TIMES ` {c}{rg} over {lg}{a_} ` TIMES ` {c}{rg} ,~ {lg}{b} ` TIMES ` {d}{rg} over {lg}{b_} ` TIMES ` {d}{rg} RIGHT ) $$/수식$$ → " \
              "$$수식$$ LEFT ( {a1} over {a_1} ,~ {b1} over {a_1} RIGHT )$$/수식$$\n" \
              "따라서  ㉠$$수식$$` = ` {a1}$$/수식$$, ㉡$$수식$$` = ` {b1}$$/수식$$입니다.\n\n"


    a_ = np.random.randint(2, 10)
    b_ = np.random.randint(2, 10)

    while gcd(a_, b_) != 1 or a_*b_ > 33:
        a_ = np.random.randint(2, 10)
        b_ = np.random.randint(2, 10)

    a = np.random.randint(1, a_)

    while gcd(a, a_) != 1:
        a = np.random.randint(1, a_)

    b = np.random.randint(1, b_)

    while gcd(b, b_) != 1:
        b = np.random.randint(1, b_)

    n = np.random.randint(1, 4)

    c = b_ * n
    d = a_ * n

    a_1 = a_ * c
    a1 = a * c
    b1 = b * d

    j1 = proc_jo(a_1, 4)

    lg = "{"
    rg = "}"

    stem = stem.format(lg = lg, rg = rg, j1 = j1, a_ = a_, a = a, b = b, b_ = b_, a_1 = a_1)
    answer = answer.format(a1 = a1, b1 = b1)
    comment = comment.format(lg = lg, rg = rg, a = a, b = b, c = c, d = d, a_ = a_, b_ = b_, a_1 = a_1, a1 = a1, b1 = b1)

    return stem, answer, comment



























# 5-1-4-39
def reductionfra514_Stem_028():
    stem = "두 분수를 가장 작은 공통분모로 통분하여 보세요.\n$$표$$ $$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1} over {a_1}$$/수식$$, $$수식$${b1} over {a_1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${a_}$$/수식$${j1} $$수식$${b_}$$/수식$$의 최소공배수는 $$수식$${a_1}$$/수식$$이므로 " \
              "공통분모를 $$수식$${a_1}$$/수식$${ro} 하여 통분합니다.\n" \
              "$$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$ → " \
              "$$수식$$LEFT ( {lg}{a} `TIMES` {e}{rg} over {lg}{a_} `TIMES` {e}{rg} ,~ {lg}{b} `TIMES` {d}{rg} over {lg}{b_} `TIMES` {d}{rg} RIGHT )$$/수식$$ → " \
              "$$수식$$LEFT ( {a1} over {a_1} ,~ {b1} over {a_1} RIGHT )$$/수식$$\n\n"


    c = np.random.randint(2, 8)
    d = np.random.randint(2, 8)
    e = np.random.randint(2, 8)

    while gcd(e, d) != 1 or c*d*e>99 or 20 > c*d*e:
        c = np.random.randint(2, 8)
        d = np.random.randint(2, 8)
        e = np.random.randint(2, 8)

    a_ = c * d
    b_ = c * e

    a = np.random.randint(1, a_)

    while gcd(a, a_) != 1:
        a = np.random.randint(1, a_)

    b = np.random.randint(1, b_)

    while gcd(b, b_) != 1:
        b = np.random.randint(1, b_)

    a_1 = a_ * e
    a1 = a * e
    b1 = b * d

    lg = "{"
    rg = "}"

    j1 = proc_jo(a_, 2)

    if int((str(a_1))[-1]) == 0 or int((str(a_1))[-1]) == 3 or int((str(a_1))[-1]) == 6:
        ro = "으로"
    else:
        ro = "로"

    stem = stem.format(a = a, b = b, a_ = a_, b_ = b_)
    answer = answer.format(a1 = a1, b1 = b1, a_1 = a_1)
    comment = comment.format(j1 = j1, lg = lg, rg = rg, a= a, b = b, e = e, d = d, a1 = a1, b1 = b1, a_ = a_, b_ = b_, a_1 = a_1, ro=ro)

    return stem, answer, comment































# 5-1-4-40
def reductionfra514_Stem_029():
    stem = "분모의 곱을 공통분모로 하여 통분하여 보세요.\n$$표$$ $$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1} over {a_1}$$/수식$$, $$수식$${b1} over {a_1}$$/수식$$\n"
    comment = "(해설)\n두 분모 $$수식$${a_}$$/수식$${j1} $$수식$${b_}$$/수식$$의 곱은 $$수식$${a_1}$$/수식$$이므로 공통분모를 $$수식$${a_1}$$/수식$${ro} 하여 통분합니다.\n" \
              "$$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$ → " \
              "$$수식$$LEFT ( {lg}{a} ` TIMES ` {b_}{rg} over {lg}{a_} ` TIMES ` {b_}{rg} ,~ {lg}{b} ` TIMES ` {a_}{rg} over {lg}{b_} ` TIMES ` {a_}{rg} RIGHT )$$/수식$$ → " \
              "$$수식$$LEFT ( {a1} over {a_1} ,~ {b1} over {a_1} RIGHT )$$/수식$$\n\n"


    a_ = np.random.randint(2, 16)
    b_ = np.random.randint(2, 16)

    while a_ == b_ or a_*b_ > 99 or 20 > a_*b_ or a_%b_ == 0 or b_%a_ == 0:
        b_ = np.random.randint(2, 16)

    a = np.random.randint(1, a_)

    while gcd(a, a_) != 1 :
        a = np.random.randint(1, a_)

    b = np.random.randint(1, b_)

    while gcd(b, b_) != 1 :
        b = np.random.randint(1, b_)

    a_1 = a_ * b_
    a1 = a * b_
    b1 = b * a_

    lg = "{"
    rg = "}"

    j1 = proc_jo(a_, 2)

    if int((str(a_1))[-1]) == 0 or int((str(a_1))[-1]) == 3 or int((str(a_1))[-1]) == 6:
        ro = "으로"
    else:
        ro = "로"

    stem = stem.format(a = a, b = b, a_ = a_, b_ = b_)
    answer = answer.format(a1 = a1, b1 = b1, a_1 = a_1)
    comment = comment.format(j1 = j1, lg = lg, rg = rg, a= a, b = b, a1 = a1, b1 = b1, a_ = a_, b_ = b_, a_1 = a_1, ro=ro)

    return stem, answer, comment























# 5-1-4-41
def reductionfra514_Stem_030():
    stem = "$$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$을 잘못 통분한 것을 모두 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${s1}$$/수식$$      ㉡ $$수식$${s2}$$/수식$$\n \n㉢ $$수식$${s3}$$/수식$$      ㉣ $$수식$${s4}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{aone}, {atwo}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$ → " \
              "$$수식$$ LEFT ( {lg}{a} ` TIMES ` {e}{rg} over {lg}{a_} ` TIMES ` {e}{rg} ,~ {lg}{b} ` TIMES ` {d}{rg} over {lg}{b_} ` TIMES ` {d}{rg} RIGHT ) $$/수식$$  → " \
              "$$수식$$ LEFT ( {a1} over {a_1} ,~ {b1} over {a_1} RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$ → " \
              "$$수식$$ LEFT ( {lg}{a} ` TIMES ` {b_}{rg} over {lg}{a_} ` TIMES ` {b_}{rg} ,~ {lg}{b} ` TIMES ` {a_}{rg} over {lg}{b_} ` TIMES ` {a_}{rg} RIGHT ) $$/수식$$  → " \
              "$$수식$$ LEFT ( {a2} over {a_2} ,~ {b2} over {a_2} RIGHT )$$/수식$$\n\n"


    c = np.random.randint(2, 8)
    d = np.random.randint(2, 8)
    e = np.random.randint(2, 8)

    while gcd(e, d) != 1 or c*d*e > 70 or 20 > c*d*e :
        c = np.random.randint(2, 8)
        d = np.random.randint(2, 8)
        e = np.random.randint(2, 8)

    a_ = c*d
    b_ = c*e

    a = np.random.randint(1, a_)

    while gcd(a, a_) != 1 :
        a = np.random.randint(1, a_)

    b = np.random.randint(1, b_)

    while gcd(b, b_) != 1 :
        b = np.random.randint(1, b_)

    a_1 = a_ * e
    a1 = a * e
    b1 = b * d
    f1 = a * d
    g1 = b * e

    a_2 = a_ * b_
    a2 = a * b_
    b2 = b * a_
    f2 = a * a_
    g2 = b * b_

    x1 = f"LEFT ( {a1} over {a_1} ,~ {b1} over {a_1} RIGHT )"
    x2 = f"LEFT ( {f1} over {a_1} ,~ {g1} over {a_1} RIGHT )"
    x3 = f"LEFT ( {a2} over {a_2} ,~ {b2} over {a_2} RIGHT )"
    x4 = f"LEFT ( {f2} over {a_2} ,~ {g2} over {a_2} RIGHT )"

    candidates = [x1, x2, x3, x4]
    np.random.shuffle(candidates)
    [s1, s2, s3, s4] = candidates

    correct_idx = 0
    correct_idx2 = 0

    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == x2:
            correct_idx = idx
        elif sdx == x4:
            correct_idx2 = idx

    if correct_idx > correct_idx2 :
        tmp = correct_idx
        correct_idx = correct_idx2
        correct_idx2 = tmp

    lg = "{"
    rg = "}"

    stem = stem.format(a = a, b = b, a_ = a_, b_ = b_, s1 = s1, s2 = s2, s3 = s3, s4 = s4)
    answer = answer.format(aone = answer_kodict[correct_idx], atwo = answer_kodict[correct_idx2])
    comment = comment.format(lg = lg, rg = rg, a = a, b = b, a_ = a_, b_ = b_, e = e, d = d, a1 = a1, b1 = b1, a2 = a2, b2 = b2, a_1 = a_1, a_2 = a_2)

    return stem, answer, comment

























# 5-1-4-42
def reductionfra514_Stem_031():
    stem = "분모의 곱을 공통분모로 하여 통분한 것입니다. ㉠$$수식$$` + `$$/수식$$㉡의 값을 구해 보세요.\n$$표$$ $$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$ → $$수식$$ LEFT ( {lg}㉠{rg} over {a_1} ,~ {b1} over {lg}㉡{rg} RIGHT ) $$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${c_}$$/수식$$\n"
    comment = "(해설)\n분모 $$수식$${a_}$$/수식$${j1} $$수식$${b_}$$/수식$$의 곱 $$수식$${a_1}$$/수식$${j2} 공통분모로 하여 통분합니다.\n" \
              "$$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$ → " \
              "$$수식$$LEFT ( {lg}{a} ` TIMES ` {b_}{rg} over {lg}{a_} ` TIMES ` {b_}{rg} ,~ {lg}{b} ` TIMES ` {a_}{rg} over {lg}{b_} ` TIMES ` {a_}{rg} RIGHT )$$/수식$$ → " \
              "$$수식$$LEFT ( {a1} over {a_1} ,~ {b1} over {a_1} RIGHT )$$/수식$$\n" \
              "따라서 ㉠$$수식$$` = ` {a1}$$/수식$$, ㉡$$수식$$` = ` {a_1}$$/수식$$이므로 ㉠$$수식$$ ` + ` $$/수식$$㉡$$수식$$` = ` {c_}$$/수식$$입니다.\n\n"


    a_ = np.random.randint(2, 16)
    b_ = np.random.randint(2, 16)

    while a_ == b_ or a_*b_ > 60 or 20 > a_*b_ or a_%b_ == 0 or b_%a_ == 0:
        b_ = np.random.randint(2, 16)

    a = np.random.randint(1, a_)

    while gcd(a, a_) != 1:
        a = np.random.randint(1, a_)

    b = np.random.randint(1, b_)

    while gcd(b, b_) != 1:
        b = np.random.randint(1, b_)

    a_1 = a_ * b_
    a1 = a * b_
    b1 = b * a_

    lg = "{"
    rg = "}"

    c_ = a1 + a_1

    j1 = proc_jo(a_, 2)
    j2 = proc_jo(a_1, 4)

    stem = stem.format(lg = lg, rg = rg, a = a, b = b, a_ = a_, b_ = b_, a_1 = a_1, b1 = b1)
    answer = answer.format(c_ = c_)
    comment = comment.format(j1 = j1, j2 = j2, lg = lg, rg = rg, c_ = c_, a= a, b = b, a1 = a1, b1 = b1, a_ = a_, b_ = b_, a_1 = a_1)

    return stem, answer, comment

























# 5-1-4-46
def reductionfra514_Stem_032():
    stem = "두 분수를 통분하려고 합니다. 공통분모가 될 수 있는 수 중에서 $$수식$$100$$/수식$$보다 작은 수를 모두 찾으면 몇 개인가요?\n$$표$$ $$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${n}$$/수식$$개\n"
    comment = "(해설)\n두 분수 $$수식$${a} over {a_}$$/수식$${j1} $$수식$${b} over {b_}$$/수식$${j2} 통분할 때 공통분모가 될 수 있는 수는 " \
              "$$수식$${a_}$$/수식$${j3} $$수식$${b_}$$/수식$$의 공배수이므로 $$수식$${a_}$$/수식$${j3} $$수식$${b_}$$/수식$$의 최소공배수의 배수입니다.\n"\
              "따라서 공통분모가 될 수 있는 수는 $$수식$${a_1}$$/수식$$, $$수식$${a_2}$$/수식$$, $$수식$${a_3}$$/수식$$, $$수식$${a_4}$$/수식$$, " \
              "$$수식$${a_5} CDOTS CDOTS$$/수식$$이고, 이 중에서 $$수식$$100$$/수식$$보다 작은 수는 {x_}로 모두 $$수식$${n}$$/수식$$개입니다.\n\n"


    c = np.random.randint(2, 8)
    d = np.random.randint(2, 8)
    e = np.random.randint(2, 8)

    while gcd(e, d) != 1 or c * d * e > 45 or 20 > c * d * e:
        c = np.random.randint(2, 8)
        d = np.random.randint(2, 8)
        e = np.random.randint(2, 8)

    a_ = c * d
    b_ = c * e

    a = np.random.randint(1, a_)

    while gcd(a, a_) != 1:
        a = np.random.randint(1, a_)

    b = np.random.randint(1, b_)

    while gcd(b, b_) != 1:
        b = np.random.randint(1, b_)

    a_1 = a_ * e
    a_2 = a_ * e * 2
    a_3 = a_ * e * 3
    a_4 = a_ * e * 4
    a_5 = a_ * e * 5

    if a_2 <= 99 and a_3 >= 100 :
        n = 2
        x_ = f"$$수식$${a_1}$$/수식$$, $$수식$${a_2}$$/수식$$"
    elif a_3 <= 99 and a_4 >= 100 :
        n = 3
        x_ = f"$$수식$${a_1}$$/수식$$, $$수식$${a_2}$$/수식$$, $$수식$${a_3}$$/수식$$"
    else :
        n = 4
        x_ = f"$$수식$${a_1}$$/수식$$, $$수식$${a_2}$$/수식$$, $$수식$${a_3}$$/수식$$, $$수식$${a_4}$$/수식$$"

    j1 = proc_jo(a, 2)
    j2 = proc_jo(b, 4)
    j3 = proc_jo(a_, 2)

    stem = stem.format(a = a, b = b, a_ = a_, b_ = b_)
    answer = answer.format(n = n)
    comment = comment.format(j1 = j1, j2 = j2, j3 = j3, a = a, b = b, a_ = a_, b_ = b_, a_1 = a_1, a_2 = a_2, a_3 = a_3, a_4 = a_4, a_5 = a_5, x_ = x_, n = n)

    return stem, answer, comment

























# 5-1-4-47
def reductionfra514_Stem_033():
    stem = "어떤 두 기약분수를 분모의 곱을 공통분모로 하여 통분하였더니 다음과 같았습니다. 통분하기 전의 기약분수를 구해 보세요.\n$$표$$ $$수식$$LEFT ( {a1} over {a_1} ,~ {b1} over {a_1} RIGHT )$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a} over {a_}$$/수식$$, $$수식$${b} over {b_}$$/수식$$\n"
    comment = "(해설)\n두 분수를 약분하여 기약분수를 구하면\n" \
              "$$수식$${a1} over {a_1} ` = ` {a} over {a_}$$/수식$$, $$수식$${b1} over {a_1} ` = ` {b} over {b_}$$/수식$$이므로 " \
              "$$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$입니다.\n\n"


    a_ = np.random.randint(2, 16)
    b_ = np.random.randint(2, 16)

    while a_ == b_ or 20 > a_*b_ or a_*b_ > 80 or a_%b_ == 0 or b_%a_ == 0:
        a_ = np.random.randint(2, 16)
        b_ = np.random.randint(2, 16)

    a = np.random.randint(1, a_)

    while gcd(a, a_) != 1 :
        a = np.random.randint(1, a_)

    b = np.random.randint(1, b_)

    while gcd(b, b_) != 1 :
        b = np.random.randint(1, b_)

    a_1 = a_ * b_
    a1 = a * b_
    b1 = b * a_

    stem = stem.format(a1 = a1, b1 = b1, a_1 = a_1)
    answer = answer.format(a = a, b = b, a_ = a_, b_ = b_)
    comment = comment.format(a = a, b = b, a1 = a1, b1 = b1, a_ = a_, b_ = b_, a_1 = a_1)

    return stem, answer, comment




























# 5-1-4-48
def reductionfra514_Stem_034():
    stem = "다음 두 분수를 통분하려고 합니다. 공통분모가 될 수 있는 수 중에서 $$수식$$100$$/수식$$에 가장 가까운 수로 두 분수를 통분하여 보세요.\n$$표$$ $$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1} over {d_}$$/수식$$, $$수식$${b1} over {d_}$$/수식$$\n"
    comment = "(해설)\n두 분모 $$수식$${a_}$$/수식$$, $$수식$${b_}$$/수식$$의 공배수인 $$수식$${c_}$$/수식$$의 배수 중에서 $$수식$$100$$/수식$$에 " \
              "가장 가까운 수는 $$수식$${d_}$$/수식$$입니다.\n" \
              "$$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$ → " \
              "$$수식$$ LEFT ( {lg}{a} ` TIMES ` {f}{rg} over {lg}{a_} ` TIMES ` {f}{rg} ,~ {lg}{b} ` TIMES ` {g}{rg} over {lg}{b_} ` TIMES ` {g}{rg} RIGHT ) $$/수식$$ → " \
              "$$수식$$ LEFT ( {a1} over {d_} ,~ {b1} over {d_} RIGHT )$$/수식$$\n\n"


    cde_list = [[2, 2, 3], [2, 2, 7], [2, 3, 4], [2, 3, 7], [3, 2, 3], [3, 3, 4], [3, 3, 5], [4, 2, 3], [4, 3, 4], [6, 2, 3], [7, 2, 3]][np.random.randint(11)]

    c = cde_list[0]
    d = cde_list[1]
    e = cde_list[2]

    a_ = c * d
    b_ = c * e
    c_ = c * d * e

    a = np.random.randint(1, a_)

    while gcd(a, a_) != 1 :
        a = np.random.randint(1, a_)

    b = np.random.randint(1, b_)

    while gcd(b, b_ ) != 1 :
        b = np.random.randint(1, b_)

    n = 100 // (a_ * e )

    a_1 = a_ * e * n
    a_2 = a_ * e * (n+1)

    if (100-a_1) <= (a_2 - 100) :
        d_ = a_1
    elif (100 - a_1) > (a_2 - 100) :
        d_ = a_2

    f = round(d_ / a_)
    g = round(d_ / b_)

    a1 = a * f
    b1 = b * g

    lg = "{"
    rg = "}"

    stem = stem.format(a = a, b = b, a_ = a_, b_ = b_)
    answer = answer.format(a1 = a1, b1 = b1, d_ = d_)
    comment = comment.format(lg = lg, rg = rg, a_ = a_, b_ = b_, c_ = c_, d_ = d_, a = a, b = b, f = f, g = g, a1 = a1, b1 = b1)

    return stem, answer, comment
























# 5-1-4-50
def reductionfra514_Stem_035():
    stem = "어떤 두 기약분수를 통분하였더니 다음과 같았습니다. 통분하기 전의 두 분수를 구해 보세요.\n$$표$$ $$수식$$LEFT ( {a1} over {lg}□{rg} ,~ {b1} over {a_1} RIGHT )$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a} over {a_}$$/수식$$, $$수식$${b} over {b_}$$/수식$$\n"
    comment = "(해설)\n통분한 두 분수의 분모는 같으므로 □$$수식$$` = ` {a_1}$$/수식$$입니다.\n" \
              "$$수식$$LEFT ( {a1} over {a_1} ,~ {b1} over {a_1} RIGHT )$$/수식$$ → " \
              "$$수식$$ LEFT ( {lg}{a1} ` div ` {c_}{rg} over {lg}{a_1} ` div ` {c_}{rg} ,~ {lg}{b1} ` div ` {d_}{rg} over {lg}{a_1} ` div ` {d_}{rg} RIGHT ) $$/수식$$ → " \
              "$$수식$$ LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$\n\n\n"


    a_ = np.random.randint(2, 16)
    b_ = np.random.randint(2, 16)

    while gcd(a_, b_) != 1 or 20 > a_ * b_ or a_ * b_ > 80 :
        a_ = np.random.randint(2, 16)
        b_ = np.random.randint(2, 16)

    a = np.random.randint(1, a_)

    while gcd(a, a_) != 1:
        a = np.random.randint(1, a_)

    b = np.random.randint(1, b_)

    while gcd(b, b_) != 1:
        b = np.random.randint(1, b_)

    n = np.random.randint(1, 99/(a_*b_)+1)

    a_1 = a_ * b_ * n
    c_ = b_ * n
    d_ = a_ * n

    a1 = a * c_
    b1 = b * d_

    lg = "{"
    rg = "}"

    stem = stem.format(lg = lg, rg = rg, a1 = a1, b1 = b1, a_1 = a_1)
    answer = answer.format(a = a, b = b, a_ = a_, b_ = b_)
    comment = comment.format(lg = lg, rg = rg, a1 = a1, b1 = b1, a = a, b = b, a_ = a_, b_  = b_, c_ = c_, d_ = d_, a_1 = a_1)

    return stem, answer, comment
























# 5-1-4-52
def reductionfra514_Stem_036():
    stem = "두 분수의 크기를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${a} over {a_}$$/수식$$ ○ $$수식$${b} over {b_}$$/수식$$\n"
    answer = "(정답)\n$$수식$${aone}$$/수식$$\n"
    comment = "(해설)\n$$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$ → " \
              "$$수식$$ LEFT ( {lg}{a} ` TIMES ` {b_}{rg} over {lg}{a_} ` TIMES ` {b_}{rg} ,~ {lg}{b} ` TIMES ` {a_}{rg} over {lg}{b_} ` TIMES ` {a_}{rg} RIGHT ) $$/수식$$ → " \
              "$$수식$$ LEFT ( {a1} over {a_1} ,~ {b1} over {a_1} RIGHT )$$/수식$$이므로 $$수식$${a} over {a_} ` {aone} ` {b} over {b_}$$/수식$$입니다.\n\n\n"


    a_ = np.random.randint(2, 16)
    b_ = np.random.randint(2, 16)

    while gcd(a_, b_) != 1 or 20 > a_ * b_ or a_ * b_ > 75:
        a_ = np.random.randint(2, 16)
        b_ = np.random.randint(2, 16)

    a = np.random.randint(1, a_)

    while gcd(a, a_) != 1:
        a = np.random.randint(1, a_)

    b = np.random.randint(1, b_)

    while gcd(b, b_) != 1:
        b = np.random.randint(1, b_)

    a_1 = a_ * b_
    a1 = a * b_
    b1 = b * a_

    if a1 > b1:
        aone = "&gt;"
    elif a1 < b1:
        aone = "&lt;"

    lg = "{"
    rg = "}"

    stem = stem.format(a = a, b = b, a_ = a_, b_ = b_)
    answer = answer.format(aone = aone)
    comment = comment.format(aone = aone, lg = lg, rg = rg, a = a, b = b, a_ = a_, b_ = b_, a1 = a1, b1 = b1, a_1 = a_1)

    return stem, answer, comment


























# 5-1-4-54
def reductionfra514_Stem_037():
    stem = "두 분수 중 더 큰 분수의 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${s1}$$/수식$$      ㉡ $$수식$${s2}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{aone}\n"
    comment = "(해설)\n두 분수의 크기를 비교할 때 분모의 크기가 너무 크거나 최소공배수를 구하기 어려울 때는 분자를 같게 만들어 줍니다.\n"\
              "$$수식$${a} over {a_} ` = ` {b} over {c_}$$/수식$$ → $$수식$${b} over {c_} ` {x} ` {b} over {b_}$$/수식$$\n"\
              "따라서 더 큰 분수는 $$수식$${y}$$/수식$$입니다.\n\n"


    n = np.random.randint(2, 5)
    a = np.random.randint(3, 8)
    b = a * n

    a_ = np.random.randint(23, 32)

    while a_ * n > 99 or gcd(a_, a) != 1:
        a_ = np.random.randint(23, 32)

    b_ = np.random.randint(a_*n-10, a_*n+11)

    while gcd(b_, b) != 1 or gcd(a_, b_) != 1:
        b_ = np.random.randint(a_ * n - 10, a_ * n + 11)

    c_ = a_ * n

    x1 = f"{a} over {a_}"
    x2 = f"{b} over {b_}"

    candidates = [x1, x2]
    np.random.shuffle(candidates)
    [s1, s2] = candidates

    if c_ > b_ :
        x = "&lt;"
        y = x2
        correct_idx = 0
        for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
            if sdx == x2:
                correct_idx = idx
                break
    elif c_ < b_ :
        x = "&gt;"
        y = x1
        correct_idx = 0
        for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
            if sdx == x1:
                correct_idx = idx
                break

    stem = stem.format(s1 = s1, s2 = s2)
    answer = answer.format(aone = answer_kodict[correct_idx])
    comment = comment.format(a = a, b = b, a_ = a_, b_ = b_, c_ = c_, x = x, y = y)

    return stem, answer, comment

























# 5-1-4-55
def reductionfra514_Stem_038():
    stem = "세 분수 중 가장 큰 분수를 찾아 써 보세요.\n$$표$$ $$수식$${s1}$$/수식$$      $$수식$${s2}$$/수식$$      $$수식$${s3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${h_}$$/수식$$\n"
    comment = "(해설)\n$$수식$${a} over {a_} ` {x} ` {b} over {b_}$$/수식$$\n" \
              "$$수식$${a} over {a_}$$/수식$${j1} $$수식$${c} over {c_}$$/수식$$의 크기를 비교하면 $$수식$${c} over {d_} ` {y} ` {c} over {c_}$$/수식$$,\n" \
              "$$수식$${b} over {b_}$$/수식$${j2} $$수식$${c} over {c_}$$/수식$$의 크기를 비교하면 $$수식$${c} over {e_} ` {z} ` {c} over {c_}$$/수식$$입니다.\n"\
              "따라서 세 분수의 크기를 비교하면 $$수식$${f_} ` &lt; ` {g_} ` &lt; ` {h_}$$/수식$$입니다.\n\n"


    n = np.random.randint(2, 5)
    a = np.random.randint(1, 4)

    b = a
    c = a * n

    a_ = np.random.randint(4, 10)

    while gcd(a, a_) != 1 :
        a_ = np.random.randint(4, 10)

    b_ = np.random.randint(4, 10)

    while gcd(b, a_) != 1 or gcd(b, b_) != 1 or a_ == b_:
        b_ = np.random.randint(4, 10)

    c_ = np.random.randint(a_ * n - 5, a_ * n + 6)

    while c_ < c + 1 or gcd(c_, a_) != 1 or gcd(c_, b_) != 1 or gcd(c_, c) != 1 :
        c_ = np.random.randint(a_ * n - 5, a_ * n + 6)

    d_ = a_ * n
    e_ = b_ * n

    if a_ > b_ :
        x = "&lt;"
    elif a_ < b_ :
        x = "&gt;"
    else :
        x = "="

    if d_ > c_ :
        y = "&lt;"
    elif d_ < c_ :
        y = "&gt;"

    if e_ > c_ :
        z = "&lt;"
    elif e_ < c_ :
        z = "&gt;"

    if a_ > b_ and d_ > c_ and e_ > c_ :
        f_ = f"{a} over {a_}"
        g_ = f"{b} over {b_}"
        h_ = f"{c} over {c_}"
    elif a_ > b_ and d_ > c_ and e_ < c_ :
        f_ = f"{a} over {a_}"
        g_ = f"{c} over {c_}"
        h_ = f"{b} over {b_}"
    elif a_ > b_ and d_ < c_ and e_ < c_ :
        f_ = f"{c} over {c_}"
        g_ = f"{a} over {a_}"
        h_ = f"{b} over {b_}"
    elif a_ < b_ and d_ > c_ and e_ > c_ :
        f_ = f"{b} over {b_}"
        g_ = f"{a} over {a_}"
        h_ = f"{c} over {c_}"
    elif a_ < b_ and d_ < c_ and e_ > c_ :
        f_ = f"{b} over {b_}"
        g_ = f"{c} over {c_}"
        h_ = f"{a} over {a_}"
    elif a_ < b_ and d_ < c_ and e_ < c_ :
        f_ = f"{c} over {c_}"
        g_ = f"{b} over {b_}"
        h_ = f"{a} over {a_}"

    x1 = f"{a} over {a_}"
    x2 = f"{b} over {b_}"
    x3 = f"{c} over {c_}"

    candidates = [x1, x2, x3]
    np.random.shuffle(candidates)
    [s1, s2, s3] = candidates

    j1 = proc_jo(a, 2)
    j2 = proc_jo(b, 2)

    stem = stem.format(s1 = s1, s2 = s2, s3 = s3)
    answer = answer.format(h_ = h_)
    comment = comment.format(j1 = j1, j2 = j2, a = a, b = b, c = c, a_ = a_, b_ = b_, c_ = c_, d_ = d_, e_ = e_, x = x, y = y, z = z, f_ = f_, g_ = g_, h_ = h_)

    return stem, answer, comment























# 5-1-4-56
def reductionfra514_Stem_039():
    stem = "세 분수의 크기를 비교하여 작은 분수부터 차례대로 써 보세요.\n$$표$$ $$수식$${a} over {a_}$$/수식$$      $$수식$${b} over {b_}$$/수식$$      $$수식$${c} over {c_}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${d_}$$/수식$$, $$수식$${e_}$$/수식$$, $$수식$${f_}$$/수식$$\n"
    comment = "(해설)\n$$수식$${a} over {a_}$$/수식$${j1} $$수식$${b} over {b_}$$/수식$${j2} 통분하여 나타내면 " \
              "$$수식$${a1} over {a_1}$$/수식$$, $$수식$${b1} over {a_1}$$/수식$$이므로 $$수식$${a} over {a_} ` {x} ` {b} over {b_}$$/수식$$입니다.\n"\
              "$$수식$${b} over {b_}$$/수식$${j3} $$수식$${c} over {c_}$$/수식$${j4} 통분하여 나타내면 " \
              "$$수식$${b2} over {b_2}$$/수식$$, $$수식$${c2} over {b_2}$$/수식$$이므로 $$수식$${b} over {b_} ` {y} ` {c} over {c_}$$/수식$$입니다.\n"\
              "$$수식$${a} over {a_}$$/수식$${j1} $$수식$${c} over {c_}$$/수식$${j4} 통분하여 나타내면 " \
              "$$수식$${a3} over {a_3}$$/수식$$, $$수식$${c3} over {a_3}$$/수식$$이므로 $$수식$${a} over {a_} ` {z} ` {c} over {c_}$$/수식$$입니다.\n"\
              "따라서 작은 분수부터 차례대로 써 보면 $$수식$${d_}$$/수식$$, $$수식$${e_}$$/수식$$, $$수식$${f_}$$/수식$$입니다.\n\n"


    n = np.random.randint(2, 6)

    pqr_list = [2, 3, 5, 7]

    p = pqr_list.pop(np.random.randint(0, len(pqr_list)))
    q = pqr_list.pop(np.random.randint(0, len(pqr_list)))
    r = pqr_list.pop(np.random.randint(0, len(pqr_list)))

    a_ = n * p
    b_ = n * q
    c_ = n * r

    a = np.random.randint(3, a_)
    b = np.random.randint(3, b_)
    c = np.random.randint(3, c_)

    while gcd(a, a_) != 1 or gcd(b, b_) != 1 or gcd(c, c_) != 1 or a == b or a == c or b == c:
        a = np.random.randint(3, a_)
        b = np.random.randint(3, b_)
        c = np.random.randint(3, c_)

    a_1 = n*p*q
    a1 = a * q
    b1 = b * p

    b_2 = n * q * r
    b2 = b * r
    c2 = c * q

    a_3 = n * p * r
    a3 = a * r
    c3 = c * p

    if a1 > b1:
        x = "&gt;"
    elif a1 < b1:
        x = "&lt;"

    if b2 > c2:
        y = "&gt;"
    elif b2 < c2:
        y = "&lt;"

    if a3 > c3:
        z = "&gt;"
    elif a3 < c3:
        z = "&lt;"

    if a1 > b1 and b2 > c2 and a3 > c3:
        d_ = f"{c} over {c_}"
        e_ = f"{b} over {b_}"
        f_ = f"{a} over {a_}"
    elif a1 > b1 and b2 < c2 and a3 > c3:
        d_ = f"{b} over {b_}"
        e_ = f"{c} over {c_}"
        f_ = f"{a} over {a_}"
    elif a1 > b1 and b2 < c2 and a3 < c3:
        d_ = f"{b} over {b_}"
        e_ = f"{a} over {a_}"
        f_ = f"{c} over {c_}"
    elif a1 < b1 and b2 > c2 and a3 > c3:
        d_ = f"{c} over {c_}"
        e_ = f"{a} over {a_}"
        f_ = f"{b} over {b_}"
    elif a1 < b1 and b2 > c2 and a3 < c3:
        d_ = f"{a} over {a_}"
        e_ = f"{c} over {c_}"
        f_ = f"{b} over {b_}"
    elif a1 < b1 and b2 < c2 and a3 < c3:
        d_ = f"{a} over {a_}"
        e_ = f"{b} over {b_}"
        f_ = f"{c} over {c_}"

    j1 = proc_jo(a, 2)
    j2 = proc_jo(b, 4)
    j3 = proc_jo(b, 2)
    j4 = proc_jo(c, 4)

    stem = stem.format(a = a, b = b, c = c, a_ = a_, b_ = b_, c_ = c_)
    answer = answer.format(d_ = d_, e_ = e_, f_ = f_)
    comment = comment.format(a_ = a_, b_ = b_, c_ = c_, j1 = j1, j2 = j2, j3 = j3, j4 = j4, a = a, b = b, c = c, a1 = a1, b1 = b1, b2 = b2, c2 = c2, a3 = a3, c3 = c3, a_1 = a_1, b_2 = b_2, a_3 = a_3, x = x, y= y, z = z, d_ = d_, e_ = e_, f_ = f_)

    return stem, answer, comment


























# 5-1-4-57
def reductionfra514_Stem_040():
    stem = "다음 분수 중에서 가장 작은 분수를 찾아 써 보세요.\n$$표$$ $$수식$${s1}$$/수식$$      $$수식$${s2}$$/수식$$      $$수식$${s3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${d_}$$/수식$$\n"
    comment = "(해설)\n$$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$  →  " \
              "$$수식$$LEFT ( {a1} over {a_1} ,~ {b1} over {a_1} RIGHT )$$/수식$$  →  " \
              "$$수식$${a} over {a_} ` {x} ` {b} over {b_}$$/수식$$\n" \
              "$$수식$$LEFT ( {b} over {b_} ,~ {c} over {c_} RIGHT )$$/수식$$  →  " \
              "$$수식$$LEFT ( {b2} over {b_2} ,~ {c2} over {b_2} RIGHT )$$/수식$$  →  " \
              "$$수식$${b} over {b_} ` {y} ` {c} over {c_}$$/수식$$\n" \
              "$$수식$$LEFT ( {a} over {a_} ,~ {c} over {c_} RIGHT )$$/수식$$  →  " \
              "$$수식$$LEFT ( {a3} over {c_} ,~ {c} over {c_} RIGHT )$$/수식$$  →  " \
              "$$수식$${a} over {a_} ` {z} ` {c} over {c_}$$/수식$$\n" \
              "따라서 세 분수의 크기를 비교하면 $$수식$${d_} ` &lt; ` {e_} ` &lt; ` {f_}$$/수식$$입니다.\n\n"


    n = np.random.randint(2, 5)
    a_ = np.random.randint(3, 6)
    b_ = np.random.randint(3, 10)

    c_ = a_ * n

    while gcd(a_, b_) != 1 or gcd(c_, b_) != 1:
        b_ = np.random.randint(3, 10)

    a = np.random.randint(2, a_)
    b = np.random.randint(2, b_)
    c = np.random.randint(2, c_)

    while gcd(a, a_) != 1 or gcd(b, b_) != 1 or gcd(c, c_) != 1 or a == b or a == c or b == c :
        a = np.random.randint(2, a_)
        b = np.random.randint(2, b_)
        c = np.random.randint(2, c_)

    a_1 = a_ * b_
    a1 = a * b_
    b1 = b * a_

    b_2 = b_ * c_
    b2 = b * c_

    c2 = c * b_
    a3 = a * n

    if a1 > b1 :
        x = "&gt;"
    elif a1 < b1 :
        x = "&lt;"

    if b2 > c2 :
        y = "&gt;"
    elif b2 < c2 :
        y = "&lt;"

    if a3 > c :
        z = "&gt;"
    elif a3 < c :
        z = "&lt;"

    if a1 > b1 and b2 > c2 and a3 > c :
        d_ = f"{c} over {c_}"
        e_ = f"{b} over {b_}"
        f_ = f"{a} over {a_}"
    elif a1 > b1 and b2 < c2 and a3 > c :
        d_ = f"{b} over {b_}"
        e_ = f"{c} over {c_}"
        f_ = f"{a} over {a_}"
    elif a1 > b1 and b2 < c2 and a3 < c :
        d_ = f"{b} over {b_}"
        e_ = f"{a} over {a_}"
        f_ = f"{c} over {c_}"
    elif a1 < b1 and b2 > c2 and a3 > c :
        d_ = f"{c} over {c_}"
        e_ = f"{a} over {a_}"
        f_ = f"{b} over {b_}"
    elif a1 < b1 and b2 > c2 and a3 < c :
        d_ = f"{a} over {a_}"
        e_ = f"{c} over {c_}"
        f_ = f"{b} over {b_}"
    elif a1 < b1 and b2 < c2 and a3 < c :
        d_ = f"{a} over {a_}"
        e_ = f"{b} over {b_}"
        f_ = f"{c} over {c_}"

    x1 = f"{a} over {a_}"
    x2 = f"{b} over {b_}"
    x3 = f"{c} over {c_}"

    candidates = [x1, x2, x3]
    np.random.shuffle(candidates)
    [s1, s2, s3] = candidates


    stem = stem.format(s1 = s1, s2 = s2, s3 = s3)
    answer = answer.format(d_ = d_)
    comment = comment.format(a = a, b = b, c = c, a1 = a1, b1 = b1, b2 = b2, c2 = c2, a3 = a3, a_ = a_, b_ = b_, c_ = c_, a_1 = a_1, b_2 = b_2, x = x, y = y, z = z, d_ = d_, e_ = e_, f_ = f_)

    return stem, answer, comment
































# 5-1-4-58
def reductionfra514_Stem_041():
    stem = "다음 분수 중에서 가장 작은 분수를 찾아 써 보세요.\n$$표$$ $$수식$${s1}$$/수식$$      $$수식$${s2}$$/수식$$      $$수식$${s3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${d_}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( {d} {a} over {a_} ,~{d} {b} over {b_} RIGHT )$$/수식$$  →  " \
              "$$수식$$LEFT ( {d} {a1} over {a_1} ,~{d} {b1} over {a_1} RIGHT )$$/수식$$  →  " \
              "$$수식$${d} {a} over {a_} ` {x} ` {d} {b} over {b_}$$/수식$$\n" \
              "$$수식$$LEFT ( {d} {b} over {b_} ,~{d} {c} over {c_} RIGHT )$$/수식$$  →  " \
              "$$수식$$LEFT ( {d} {b2} over {b_2} ,~{d} {c2} over {b_2} RIGHT )$$/수식$$  →  " \
              "$$수식$${d} {b} over {b_} ` {y} ` {d} {c} over {c_}$$/수식$$\n" \
              "$$수식$$LEFT ( {d} {a} over {a_} ,~{d} {c} over {c_} RIGHT )$$/수식$$  →  " \
              "$$수식$$LEFT ( {d} {a3} over {c_} ,~{d} {c} over {c_} RIGHT )$$/수식$$  →  " \
              "$$수식$${d} {a} over {a_} ` {z} ` {d} {c} over {c_}$$/수식$$\n" \
              "따라서 세 분수의 크기를 비교하면 $$수식$${d_} ` &lt; ` {e_} ` &lt; ` {f_}$$/수식$$이므로 가장 큰 분수는 $$수식$${f_}$$/수식$$, " \
              "가장 작은 분수는 $$수식$${d_}$$/수식$$입니다.\n\n"


    d = np.random.randint(1, 6)
    n = np.random.randint(2, 5)
    a_ = np.random.randint(3, 6)
    b_ = np.random.randint(3, 10)

    c_ = a_ * n

    while gcd(a_, b_) != 1 or gcd(b_, c_) != 1:
        b_ = np.random.randint(3, 10)

    a = np.random.randint(2, a_)
    b = np.random.randint(2, b_)
    c = np.random.randint(2, c_)

    while gcd(a, a_) != 1 or gcd(b, b_) != 1 or gcd(c, c_) != 1 or a == b or a == c or b == c :
        a = np.random.randint(2, a_)
        b = np.random.randint(2, b_)
        c = np.random.randint(2, c_)

    a_1 = a_ * b_
    a1 = a * b_
    b1 = b * a_

    b_2 = b_ * c_
    b2 = b * c_
    c2 = c * b_

    a3 = a * n

    if a1 > b1 :
        x = "&gt;"
    elif a1 < b1 :
        x = "&lt;"

    if b2 > c2 :
        y = "&gt;"
    elif b2 < c2 :
        y = "&lt;"

    if a3 > c :
        z = "&gt;"
    elif a3 < c :
        z = "&lt;"

    if a1 > b1 and b2 > c2 and a3 > c:
        d_ = f"{d} {c} over {c_}"
        e_ = f"{d} {b} over {b_}"
        f_ = f"{d} {a} over {a_}"
    elif a1 > b1 and b2 < c2 and a3 > c:
        d_ = f"{d} {b} over {b_}"
        e_ = f"{d} {c} over {c_}"
        f_ = f"{d} {a} over {a_}"
    elif a1 > b1 and b2 < c2 and a3 < c:
        d_ = f"{d} {b} over {b_}"
        e_ = f"{d} {a} over {a_}"
        f_ = f"{d} {c} over {c_}"
    elif a1 < b1 and b2 > c2 and a3 > c:
        d_ = f"{d} {c} over {c_}"
        e_ = f"{d} {a} over {a_}"
        f_ = f"{d} {b} over {b_}"
    elif a1 < b1 and b2 > c2 and a3 < c:
        d_ = f"{d} {a} over {a_}"
        e_ = f"{d} {c} over {c_}"
        f_ = f"{d} {b} over {b_}"
    elif a1 < b1 and b2 < c2 and a3 < c:
        d_ = f"{d} {a} over {a_}"
        e_ = f"{d} {b} over {b_}"
        f_ = f"{d} {c} over {c_}"

    x1 = f"{d} {a} over {a_}"
    x2 = f"{d} {b} over {b_}"
    x3 = f"{d} {c} over {c_}"

    candidates = [x1, x2, x3]
    np.random.shuffle(candidates)
    [s1, s2, s3] = candidates

    stem = stem.format(s1 = s1, s2 = s2, s3 = s3)
    answer = answer.format(d_ = d_)
    comment = comment.format(d_ = d_, e_ = e_, f_ = f_, z = z, a = a, b = b, c = c, d = d, a1 = a1, b1 = b1, b2 = b2, c2 = c2, a3 = a3, a_ = a_, b_ = b_, c_ = c_, a_1 = a_1, b_2 = b_2, x = x, y = y)

    return stem, answer, comment


























# 5-1-4-59
def reductionfra514_Stem_042():
    stem = "세 접시에 {s}{j1} 같은 수만큼 놓여 있습니다.\n {s}{j2} 가장 많이 먹은 사람은 누구인가요?\n$$표$$ {s1}\n \n{s2}\n \n{s3} $$/표$$\n"
    answer = "(정답)\n{wh4}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( {a} over {a_} ,~ {b} over {b_} RIGHT )$$/수식$$  →  " \
              "$$수식$$LEFT ( {a1} over {b_} ,~ {b} over {b_} RIGHT )$$/수식$$  →  " \
              "$$수식$${a} over {a_} ` {x} ` {b} over {b_}$$/수식$$\n" \
              "$$수식$$LEFT ( {b} over {b_} ,~ {c} over {c_} RIGHT )$$/수식$$  →  " \
              "$$수식$$LEFT ( {b2} over {b_2} ,~ {c2} over {b_2} RIGHT )$$/수식$$  →  " \
              "$$수식$${b} over {b_} ` {y} ` {c} over {c_}$$/수식$$\n" \
              "$$수식$$LEFT ( {a} over {a_} ,~ {c} over {c_} RIGHT )$$/수식$$  →  " \
              "$$수식$$LEFT ( {a3} over {c_} ,~ {c} over {c_} RIGHT )$$/수식$$  →  " \
              "$$수식$${a} over {a_} ` {z} ` {c} over {c_}$$/수식$$\n" \
              "따라서 세 분수의 크기를 비교하면 $$수식$${d_} ` &lt; ` {e_} ` &lt; ` {f_}$$/수식$$이므로 {s}{j2} 가장 많이 먹은 사람은 {wh4}입니다.\n\n"


    wh_list = ['민우', '슬기', '준서', '수지', '은호', '선우', '윤서', '지우', '정호', '현기', '재수', '영서', '은지', '연주', '주호', '혁구', '영기', '상수', '은서', '동우', '재우', '진희', '준서', '유라', '수미', '현수', '채아', '민주', '지호', '연아', '은우', '시우', '혁재', '민하']

    wh1 = wh_list.pop(np.random.randint(0, len(wh_list)))
    wh2 = wh_list.pop(np.random.randint(0, len(wh_list)))
    wh3 = wh_list.pop(np.random.randint(0, len(wh_list)))

    s = ['딸기', '방울토마토', '체리', '앵두', '금귤'][np.random.randint(0, 5)]

    j1 = proc_jo(s, 0)
    j2 = proc_jo(s, 4)

    a_ = np.random.randint(3, 6)

    bc_list = [[a_*2, a_*3], [a_*4, a_*3]][np.random.randint(0, 2)]
    b_ = bc_list[0]
    c_ = bc_list[1]

    a = np.random.randint(2, a_)
    b = np.random.randint(2, b_)
    c = np.random.randint(2, c_)

    while gcd(a, a_) != 1 or gcd(b, b_) != 1 or gcd(c, c_) != 1 or a == b or a == c or b == c or (a*(b_/a_)-3)>b or b > (a*(b_/a_)+3) or (a*3-3)>c or c>(a*3 +3):
        a = np.random.randint(2, a_)
        b = np.random.randint(2, b_)
        c = np.random.randint(2, c_)

    a1 = round(a * (b_/a_))

    if b_ == a_ * 2 :
        b_2 = b_ * 3
        b2 = b * 3
        c2 = c * 2
    elif b_ == a_ * 4 :
        b_2 = b_ * 3
        b2 = b * 3
        c2 = c * 4

    a3 = a * 3

    if a1 > b :
        x = "&gt;"
    elif a1 < b :
        x = "&lt;"
    if b2 > c2 :
        y = "&gt;"
    elif b2 < c2 :
        y = "&lt;"
    if a3 > c :
        z = "&gt;"
    elif a3 < c :
        z = "&lt;"

    if a1 > b and b2 > c2 and a3 > c :
        d_ = f"{c} over {c_}"
        e_ = f"{b} over {b_}"
        f_ = f"{a} over {a_}"
        wh4 = wh1
    elif a1 > b and b2 < c2 and a3 > c :
        d_ = f"{b} over {b_}"
        e_ = f"{c} over {c_}"
        f_ = f"{a} over {a_}"
        wh4 = wh1
    elif a1 > b and b2 < c2 and a3 < c :
        d_ = f"{b} over {b_}"
        e_ = f"{a} over {a_}"
        f_ = f"{c} over {c_}"
        wh4 = wh3
    elif a1 < b and b2 > c2 and a3 > c :
        d_ = f"{c} over {c_}"
        e_ = f"{a} over {a_}"
        f_ = f"{b} over {b_}"
        wh4 = wh2
    elif a1 < b and b2 > c2 and a3 < c :
        d_ = f"{a} over {a_}"
        e_ = f"{c} over {c_}"
        f_ = f"{b} over {b_}"
        wh4 = wh2
    elif a1 < b and b2 < c2 and a3 < c :
        d_ = f"{a} over {a_}"
        e_ = f"{b} over {b_}"
        f_ = f"{c} over {c_}"
        wh4 = wh3

    j3 = proc_jo(a, 4)
    j4 = proc_jo(b, 4)
    j5 = proc_jo(c, 4)

    x1 = f"$$수식$$LEFT [$$/수식$${wh1}$$수식$$RIGHT ]$$/수식$$ 나는 한 접시의 $$수식$$ {a} over {a_} $$/수식$${j3} 먹었어."
    x2 = f"$$수식$$LEFT [$$/수식$${wh2}$$수식$$RIGHT ]$$/수식$$ 나는 한 접시의 $$수식$$ {b} over {b_} $$/수식$${j4} 먹었어."
    x3 = f"$$수식$$LEFT [$$/수식$${wh3}$$수식$$RIGHT ]$$/수식$$ 나는 한 접시의 $$수식$$ {c} over {c_} $$/수식$${j5} 먹었어."

    candidates = [x1, x2, x3]
    np.random.shuffle(candidates)
    [s1, s2, s3] = candidates

    stem = stem.format(s = s, s1 = s1, s2 = s2, s3 = s3, j1 = j1, j2 = j2)
    answer = answer.format(wh4 = wh4)
    comment = comment.format(a = a, b = b, c = c, a1 = a1, b2 = b2, c2 = c2, a3 = a3, a_ = a_, b_ = b_, c_ = c_, b_2 = b_2, x = x, y = y, z = z, s = s, j2 = j2, wh4 = wh4, d_ = d_, e_ = e_, f_ = f_)

    return stem, answer, comment




























# 5-1-4-60
def reductionfra514_Stem_043():
    stem = "㉠에 알맞은 자연수 중에서 가장 작은 수를 구해 보세요.\n$$표$$ $$수식$$ {a} over {a_} ` &lt; ` {lg}㉠{rg} over {b_}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${c2}$$/수식$$\n"
    comment = "(해설)\n$$수식$$LEFT ( {a} over {a_} ,~ {lg}㉠{rg} over {b_} RIGHT )$$/수식$$에서 분모의 곱으로 통분하면 " \
              "$$수식$$LEFT ( {lg}{a} ` TIMES ` {b_}{rg} over {lg}{a_} ` TIMES ` {b_}{rg} ,~ {lg}{lg}㉠{rg} ` TIMES ` {a_}{rg} over {lg}{b_} ` TIMES ` {a_}{rg} RIGHT )$$/수식$$입니다.\n" \
              "$$수식$${a} ` TIMES ` {b_} ` &lt; ` ㉠ ` TIMES ` {a_}$$/수식$$에서 $$수식$${a1} ` &lt; ` ㉠ ` TIMES ` {a_}$$/수식$$입니다.\n" \
              "$$수식$${c1} ` TIMES ` {a_} ` = ` {b1}$$/수식$$, $$수식$${c2} ` TIMES ` {a_} ` = ` {b2}$$/수식$$이므로 ㉠에 알맞은 수는 $$수식$${c2}$$/수식$$입니다.\n\n"


    a_ = np.random.randint(12, 26)
    b_ = np.random.randint(12, 26)

    while a_ == b_:
        b_ = np.random.randint(12, 26)

    a = np.random.randint(5, a_-4)

    while gcd(a, a_) != 1:
        a = np.random.randint(5, a_ - 4)

    a1 = a * b_
    c1 = a1 // a_
    c2 = c1 + 1
    b1 = c1 * a_
    b2 = c2 * a_

    lg = "{"
    rg = "}"

    stem = stem.format(lg = lg, rg = rg, a = a, a_ = a_, b_ = b_)
    answer = answer.format(c2 = c2)
    comment = comment.format(lg = lg, rg = rg, a = a, a_ = a_, b_ = b_, a1 = a1, c1 = c1, b1 = b1, b2 = b2, c2 = c2)

    return stem, answer, comment





























# 5-1-4-61
def reductionfra514_Stem_044():
    stem = "다음 중 $$수식$$1 over 2$$/수식$$보다 작은 분수는 모두 몇 개인가요?\n$$표$$ $$수식$$ {s1} $$/수식$$      $$수식$$ {s2} $$/수식$$      $$수식$$ {s3} $$/수식$$      $$수식$$ {s4} $$/수식$$      $$수식$$ {s5} $$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${n}$$/수식$$개\n"
    comment = "(해설)\n분자에 $$수식$$2$$/수식$$를 곱해서 분모보다 작으면 $$수식$$1 over 2$$/수식$$보다 작은 분수입니다.\n" \
              "{z1}\n" \
              "{z2}\n" \
              "{z3}\n" \
              "{z4}\n" \
              "{z5}\n" \
              "따라서 $$수식$$ 1 over 2 $$/수식$$보다 작은 분수는 $$수식$${x}$$/수식$$로 모두 $$수식$${n}$$/수식$$개입니다. \n\n"


    num_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    answer_list = []
    
    while True:
        sample = random.sample(num_list, 5)
        a_ = sample[0]
        b_ = sample[1]
        c_ = sample[2]
        d_ = sample[3]
        e_ = sample[4]
        
        a = random.randint(1, a_-1)
        b = random.randint(1, b_-1)
        c = random.randint(1, c_-1)
        d = random.randint(1, d_-1)
        e = random.randint(1, e_-1)
        
        if gcd(a, a_) == 1 and gcd(b, b_) == 1 and gcd(c, c_) == 1 and gcd(d, d_) == 1 and gcd(e, e_):
            x1 = f"{a} over {a_}"
            x2 = f"{b} over {b_}"
            x3 = f"{c} over {c_}"
            x4 = f"{d} over {d_}"
            x5 = f"{e} over {e_}"
            
            a1 = a * 2
            b1 = b * 2
            c1 = c * 2
            d1 = d * 2
            e1 = e * 2
    
            if a1 < a_:
                sa = "&lt;"
                answer_list.append(x1)
            else:
                sa = "&gt;"
            
            if b1 < b_:
                sb = "&lt;"
                answer_list.append(x2)
            else:
                sb = "&gt;"
                
            if c1 < c_:
                sc = "&lt;"
                answer_list.append(x3)
            else:
                sc = "&gt;"
                
            if d1 < d_:
                sd = "&lt;"
                answer_list.append(x4)
            else:
                sd = "&gt;"
                
            if e1 < e_:
                se = "&lt;"
                answer_list.append(x5)
            else:
                se = "&gt;"
                
            if len(answer_list) > 0:
                n = len(answer_list)
                break

    x = ",".join(answer_list)

    y1 = f"$$수식$${a} over {a_}$$/수식$$ → $$수식$${a} ` times ` 2 ` = ` {a1} ` {sa} ` {a_}$$/수식$$이므로 $$수식$${a} over {a_} ` {sa} ` 1 over 2$$/수식$$\n"
    y2 = f"$$수식$${b} over {b_}$$/수식$$ → $$수식$${b} ` times ` 2 ` = ` {b1} ` {sb} ` {b_}$$/수식$$이므로 $$수식$${b} over {b_} ` {sb} ` 1 over 2$$/수식$$\n"
    y3 = f"$$수식$${c} over {c_}$$/수식$$ → $$수식$${c} ` times ` 2 ` = ` {c1} ` {sc} ` {c_}$$/수식$$이므로 $$수식$${c} over {c_} ` {sc} ` 1 over 2$$/수식$$\n"
    y4 = f"$$수식$${d} over {d_}$$/수식$$ → $$수식$${d} ` times ` 2 ` = ` {d1} ` {sd} ` {d_}$$/수식$$이므로 $$수식$${d} over {d_} ` {sd} ` 1 over 2$$/수식$$\n"
    y5 = f"$$수식$${e} over {e_}$$/수식$$ → $$수식$${e} ` times ` 2 ` = ` {e1} ` {se} ` {e_}$$/수식$$이므로 $$수식$${e} over {e_} ` {se} ` 1 over 2$$/수식$$\n"

    xy_dict = {x1:y1, x2:y2, x3:y3, x4:y4, x5:y5}

    candidates = [x1, x2, x3, x4, x5]
    np.random.shuffle(candidates)
    [s1, s2, s3, s4, s5] = candidates

    z1 = xy_dict[s1]
    z2 = xy_dict[s2]
    z3 = xy_dict[s3]
    z4 = xy_dict[s4]
    z5 = xy_dict[s5]

    stem = stem.format(s1 = s1, s2 = s2, s3 = s3, s4 = s4, s5 = s5)
    answer = answer.format(n = n)
    comment = comment.format(z1 = z1, z2 = z2, z3 = z3, z4 = z4, z5 = z5, x = x, n = n)

    return stem, answer, comment





























# 5-1-4-63
def reductionfra514_Stem_045():
    stem = "{wh1}, {wh2}, {wh3}{j1} 각각 똑같은 {s}{j2} $$수식$$1$$/수식$$개씩 사서 먹었습니다. {wh1}{j3} 전체의 $$수식$$1 over {a_}$$/수식$$을, {wh2}{j4} 전체의 $$수식$$1 over {b_}$$/수식$$을, {wh3}{j1} 전체의 $$수식$$1 over {c_}$$/수식$$을 먹었습니다. {s}{j5} 가장 많이 남아 있는 사람은 누구인가요?\n"
    answer = "(정답)\n{wh4}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${wh1}에게 남아 있는 {s}의 양$$수식$$RIGHT ) ` = ` 1 ` - ` 1 over {a_} ` = ` {a} over {a_}$$/수식$$\n"\
              "$$수식$$LEFT ($$/수식$${wh2}에게 남아 있는 {s}의 양$$수식$$RIGHT ) ` = ` 1 ` - ` 1 over {b_} ` = ` {b} over {b_}$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${wh3}에게 남아 있는 {s}의 양$$수식$$RIGHT ) ` = ` 1 ` - ` 1 over {c_} ` = ` {c} over {c_}$$/수식$$\n" \
              "분자가 분모보다 $$수식$$1$$/수식$$ 작은 분수는 분모가 클수록 큽니다.\n"\
              "즉, $$수식$${d} ` &lt; ` {e} ` &lt; ` {f}$$/수식$$이므로 $$수식$${d_} ` &lt; ` {e_} ` &lt; ` {f_}$$/수식$$입니다.\n"\
              "따라서 {s}{j5} 가장 많이 남아 있는 사람은 {wh4}입니다.\n\n"


    wh_list = ['민우', '슬기', '수지', '은호', '선우', '윤서', '지우', '정호', '현기', '재수', '영서', '은지', '연주', '주호', '혁구', '영기', '상수', '은서', '동우', '재우', '진희', '준서', '유라', '수미', '현수', '채아', '민주', '지호', '연아', '은우', '시우', '혁재', '민하']

    wh1 = wh_list.pop(np.random.randint(0, len(wh_list)))
    wh2 = wh_list.pop(np.random.randint(0, len(wh_list)))
    wh3 = wh_list.pop(np.random.randint(0, len(wh_list)))

    s = ['빵', '케이크', '시루떡', '백설기'][np.random.randint(0, 4)]

    j1 = proc_jo(wh3, -1)
    j2 = proc_jo(s, 4)
    j3 = proc_jo(wh1, -1)
    j4 = proc_jo(wh2, -1)
    j5 = proc_jo(s, 0)

    a_ = np.random.randint(5, 16)
    b_ = np.random.randint(5, 16)

    while a_ == b_ :
        b_ = np.random.randint(5, 16)

    c_ = np.random.randint(5, 16)

    while c_ == a_ or c_ == b_ :
        c_ = np.random.randint(5, 16)

    a = a_ - 1
    b = b_ - 1
    c = c_ - 1

    if a < b and b < c :
        d = a
        e = b
        f = c
        d_ = f"{a} over {a_}"
        e_ = f"{b} over {b_}"
        f_ = f"{c} over {c_}"
        wh4 = wh3
    elif a < c and c < b :
        d = a
        e = c
        f = b
        d_ = f"{a} over {a_}"
        e_ = f"{c} over {c_}"
        f_ = f"{b} over {b_}"
        wh4 = wh2
    elif b < c and c < a :
        d = b
        e = c
        f = a
        d_ = f"{b} over {b_}"
        e_ = f"{c} over {c_}"
        f_ = f"{a} over {a_}"
        wh4 = wh1
    elif b < a and a < c :
        d = b
        e = a
        f = c
        d_ = f"{b} over {b_}"
        e_ = f"{a} over {a_}"
        f_ = f"{c} over {c_}"
        wh4 = wh3
    elif c < a and a < b :
        d = c
        e = a
        f = b
        d_ = f"{c} over {c_}"
        e_ = f"{a} over {a_}"
        f_ = f"{b} over {b_}"
        wh4 = wh2
    elif c < b and b < a :
        d = c
        e = b
        f = a
        d_ = f"{c} over {c_}"
        e_ = f"{b} over {b_}"
        f_ = f"{a} over {a_}"
        wh4 = wh1

    stem = stem.format(wh1 = wh1, wh2 = wh2, wh3 = wh3, s = s, j1 = j1, j2 = j2, j3 =j3, j4 =j4, j5 = j5, a_ = a_, b_ = b_, c_ = c_)
    answer = answer.format(wh4 = wh4)
    comment = comment.format(j5 = j5, a = a, b = b, c = c, a_ = a_, b_ = b_, c_ = c_, s = s, wh1 = wh1, wh2 = wh2, wh3 = wh3, wh4 = wh4, d = d, e = e, f = f, d_ = d_, e_ = e_, f_ = f_)

    return stem, answer, comment
























# 5-1-4-65
def reductionfra514_Stem_046():
    stem = "$$수식$${a} over {a_}$$/수식$$보다 크고 $$수식$${b} over {b_}$$/수식$$보다 작은 분수 중에서 분모가 $$수식$${c_}$$/수식$$인 분수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${n}$$/수식$$개\n"
    comment = "(해설)\n$$수식$${a} over {a_}$$/수식$${j1} $$수식$${b} over {b_}$$/수식$${j2} 분모를 $$수식$${c_}$$/수식$$으로 통분하면 " \
              "$$수식$${a1} over {c_} ` &lt; ` {lg}□{rg} over {c_} ` &lt; ` {b1} over {c_}$$/수식$$입니다.\n"\
              "따라서 구하는 분수의 분자는 $$수식$${a2}$$/수식$$부터 $$수식$${b2}$$/수식$$까지인 수이므로 모두 $$수식$${n}$$/수식$$개입니다.\n\n"


    cde_list = [[2, 2, 5], [2, 2, 7], [2, 3, 4], [2, 3, 5], [2, 3, 7], [2, 4, 5], [2, 4, 7], [2, 5, 7], [3, 2, 3], [3, 2, 5], [3, 2, 7], [3, 3, 4],
                [3, 3, 5], [3, 3, 7], [3, 4, 5], [4, 2, 3], [4, 2, 5], [4, 2, 7], [4, 3, 4], [4, 3, 5], [5, 2, 3], [5, 2, 5], [5, 3, 4], [5, 3, 5],
                [6, 2, 3], [6, 3, 4], [6, 3, 5], [7, 2, 3], [7, 2, 5], [7, 3, 4]][np.random.randint(0, 30)]

    c = cde_list[0]
    d = cde_list[1]
    e = cde_list[2]

    a_ = c * d
    b_ = c * e
    c_ = c * d * e

    a = np.random.randint(1, round(a_/2)+1)

    while gcd(a, a_) != 1:
        a = np.random.randint(1, round(a_ / 2)+1)

    b = np.random.randint(1, b_)

    while gcd(b, b_) != 1 or (a * e + 8)/d > b:
        b = np.random.randint(1, b_)

    a1 = a * e
    b1 = b * d

    a2 = a1 + 1
    b2 = b1 - 1

    n = b2 - a2 + 1

    j1 = proc_jo(a, 2)
    j2 = proc_jo(b, 4)

    lg = "{"
    rg = "}"

    stem = stem.format(a = a, b = b, a_ = a_, b_ = b_, c_ = c_)
    answer = answer.format(n = n)
    comment = comment.format(j1 = j1, j2 = j2, lg = lg, rg = rg, a = a, b = b, a1 = a1, b1 = b1, a2 = a2, b2 = b2, n = n , a_ = a_, b_ = b_, c_ = c_)

    return stem, answer, comment

























# 5-1-4-68
def reductionfra514_Stem_047():
    stem = "두 수의 크기를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${a} over {a_}$$/수식$$ ○ $$수식$${b_}$$/수식$$\n"
    answer = "(정답)\n$$수식$${x}$$/수식$$\n"
    comment = "(해설)\n$$수식$${a} over {a_} ` = ` {lg} {a} ` times ` {n} {rg} over {lg} {a_} ` times ` {n} {rg} ` = ` {c} over 10 ` = ` {c_}$$/수식$$이고 " \
              "$$수식$${c_} ` {x} ` {b_}$$/수식$$이므로 $$수식$${a} over {a_} ` {x} ` {b_}$$/수식$$입니다.\n\n"


    an_list = [[5, 2], [2, 5]][np.random.randint(0, 2)]

    a_ = an_list[0]
    n = an_list[1]

    a = np.random.randint(1, a_)
    b = np.random.randint(a*n - 2, a*n + 3)

    b_ = round(b / 10, 1)
    c = a * n
    c_ = round(c/10, 1)

    if c_ > b_:
        x = "&gt;"
    elif c_ == b_:
        x= "="
    else :
        x = "&lt;"

    lg = "{"
    rg = "}"

    stem = stem.format(a = a, a_ = a_, b_ = b_)
    answer = answer.format(x = x)
    comment = comment.format(x = x, lg = lg, rg = rg, a = a, c = c, n = n, a_ = a_, b_ = b_, c_ = c_)

    return stem, answer, comment





























# 5-1-4-70
def reductionfra514_Stem_048():
    stem = "소수를 기약분수로 나타낼 때 분모가 $$수식$${a_}$$/수식$${j1} 되는 것을 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${s1}$$/수식$$      ㉡ $$수식$${s2}$$/수식$$      ㉢ $$수식$${s3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{aone}\n"
    comment = "(해설)\n㉠ $$수식$${y1}$$/수식$$\n" \
              "㉡ $$수식$${y2}$$/수식$$\n" \
              "㉢ $$수식$${y3}$$/수식$$\n\n"


    # a_ = [20, 50][np.random.randint(0, 2)]
    #
    # a1 = np.random.randint(0, 10)
    # a2 = np.random.randint(1, 4) * 2
    #
    # while (a1 * 10 + a2) % 4 == 0 :
    #     a1 = np.random.randint(0, 10)
    #     a2 = np.random.randint(1, 4) * 2
    #
    # b1 = np.random.randint(0, 10)
    # b2 = 5
    #
    # x1 = f"0.{a1}{a2}"
    # x2 = f"0.{b1}{b2}"
    #
    # if a_ == 20 :
    #     c1 = np.random.randint(1, 10)
    #     c2 = 5
    # elif a_ == 50 :
    #     c1 = np.random.randint(1, 10)
    #     c2 = 2
    #
    # x3 = f"{c1}.{c2}"
    #
    # candidates = [x1, x2, x3]
    # np.random.shuffle(candidates)
    # [s1, s2, s3] = candidates
    #
    # correct_idx = 0
    # if a_ == 20 :
    #     for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
    #         if sdx == x2:
    #             correct_idx = idx
    #             break
    # elif a_ == 50 :
    #     for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
    #         if sdx == x1:
    #             correct_idx = idx
    #             break
    #
    # j1 = proc_jo(a_, 0)
    #
    # a = round((a1*10+a2)/2)
    # b = round((b1*10+b2)/5)
    #
    # c = 1
    # c3 = round(10 / c2)
    #
    # lg = "{"
    # rg = "}"
    #
    # if a1 != 0:
    #     z1 = f"$$수식$$0.{a1}{a2} ` = ` {lg}{a1}{a2}{rg} over 100 ` = ` {lg}{a1}{a2} ` div ` 2{rg} over {lg}100 ` div ` 2{rg} ` = ` {a} over 50$$/수식$$"
    # else:
    #     z1 = f"$$수식$$0.{a1}{a2} ` = ` {lg}{a2}{rg} over 100 ` = ` {lg}{a2} ` div ` 2{rg} over {lg}100 ` div ` 2{rg} ` = ` {a} over 50$$/수식$$"
    #
    # if b1 != 0:
    #     z2 = f"$$수식$$0.{b1}{b2} ` = ` {lg}{b1}{b2}{rg} over 100 ` = ` {lg}{b1}{b2} ` div ` 5{rg} over {lg}100 ` div ` 5{rg} ` = ` {b} over 20$$/수식$$"
    # else:
    #     z2 = f"$$수식$$0.{b1}{b2} ` = ` {lg}{b2}{rg} over 100 ` = ` {lg}{b2} ` div ` 5{rg} over {lg}100 ` div ` 5{rg} ` = ` {b} over 20$$/수식$$"
    #
    # z3 = f"$$수식$${c1}.{c2} ` = ` {c1} {c2} over 10 ` = ` {c1} {lg}{c2} ` div ` {c2}{rg} over {lg}10 ` div ` {c2}{rg} ` = ` {c1} {c} over {c3}$$/수식$$"
    #
    # xz_dict = {x1 : z1, x2 : z2, x3 : z3}
    #
    # y1 = xz_dict[s1]
    # y2 = xz_dict[s2]
    # y3 = xz_dict[s3]


    # 기약분수로 나타내기 위해 전체적으로 while 문으로 걸었음

    while True:
        a_ = [20, 50][np.random.randint(0, 2)]

        a1 = np.random.randint(0, 10)
        a2 = np.random.randint(1, 4) * 2

        while (a1 * 10 + a2) % 4 == 0 :
            a1 = np.random.randint(0, 10)
            a2 = np.random.randint(1, 4) * 2

        b1 = np.random.randint(0, 10)
        b2 = 5

        x1 = f"0.{a1}{a2}"
        x2 = f"0.{b1}{b2}"

        if a_ == 20 :
            c1 = np.random.randint(1, 10)
            c2 = 5
        elif a_ == 50 :
            c1 = np.random.randint(1, 10)
            c2 = 2

        x3 = f"{c1}.{c2}"

        candidates = [x1, x2, x3]
        np.random.shuffle(candidates)
        [s1, s2, s3] = candidates

        correct_idx = 0
        if a_ == 20 :
            for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
                if sdx == x2:
                    correct_idx = idx
                    break
        elif a_ == 50 :
            for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
                if sdx == x1:
                    correct_idx = idx
                    break

        j1 = proc_jo(a_, 0)

        a = round((a1*10+a2)/2)
        b = round((b1*10+b2)/5)

        c = 1
        c3 = round(10 / c2)

        lg = "{"
        rg = "}"

        if a1 != 0:
            z1 = f"$$수식$$0.{a1}{a2} ` = ` {lg}{a1}{a2}{rg} over 100 ` = ` {lg}{a1}{a2} ` div ` 2{rg} over {lg}100 ` div ` 2{rg} ` = ` {a} over 50$$/수식$$"
        else:
            z1 = f"$$수식$$0.{a1}{a2} ` = ` {lg}{a2}{rg} over 100 ` = ` {lg}{a2} ` div ` 2{rg} over {lg}100 ` div ` 2{rg} ` = ` {a} over 50$$/수식$$"

        if b1 != 0:
            z2 = f"$$수식$$0.{b1}{b2} ` = ` {lg}{b1}{b2}{rg} over 100 ` = ` {lg}{b1}{b2} ` div ` 5{rg} over {lg}100 ` div ` 5{rg} ` = ` {b} over 20$$/수식$$"
        else:
            z2 = f"$$수식$$0.{b1}{b2} ` = ` {lg}{b2}{rg} over 100 ` = ` {lg}{b2} ` div ` 5{rg} over {lg}100 ` div ` 5{rg} ` = ` {b} over 20$$/수식$$"

        z3 = f"$$수식$${c1}.{c2} ` = ` {c1} {c2} over 10 ` = ` {c1} {lg}{c2} ` div ` {c2}{rg} over {lg}10 ` div ` {c2}{rg} ` = ` {c1} {c} over {c3}$$/수식$$"

        xz_dict = {x1 : z1, x2 : z2, x3 : z3}

        y1 = xz_dict[s1]
        y2 = xz_dict[s2]
        y3 = xz_dict[s3]

        if a % 2 != 0 and a % 5 != 0 and a % 10 != 0 and a % 25 != 0 and a % 50 != 0:
            if b % 2 != 0 and b % 4 != 0 and b % 5 != 0 and b % 10 != 0 and b % 20 != 0:
                break


    stem = stem.format(j1 = j1, s1 = s1, s2 = s2, s3 = s3, a_ = a_)
    answer = answer.format(aone = answer_kodict[correct_idx])
    comment = comment.format(y1 = y1, y2 = y2, y3 = y3)

    return stem, answer, comment



























# 5-1-4-72
def reductionfra514_Stem_049():
    stem = "분수와 소수의 크기를 비교하여 가장 작은 수를 소수로 나타내어 보세요.\n$$표$$ $$수식$${s1}$$/수식$$     $$수식$${s2}$$/수식$$      $$수식$${s3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${d_}$$/수식$$\n"
    comment = "(해설)\n$$수식$${b2} over {b1} ` = ` {lg}{b2} ` times ` {n}{rg} over {lg}{b1} ` times ` {n}{rg} ` = ` {b3} over 100 ` = ` {b_}$$/수식$$\n"\
              "→ $$수식$${d_} ` &lt; ` {e_} ` &lt; ` {f_}$$/수식$$\n"\
              "따라서 크기를 비교하면 가장 작은 수는 $$수식$${d_}$$/수식$$입니다.\n\n"


    a_ = round(np.random.randint(2, 10)/10, 1)
    c_ = round(np.random.randint(2, 10)/10, 1)

    while a_ == c_:
        c_ = round(np.random.randint(2, 10) / 10, 1)

    b1 = [4, 20, 25, 50][np.random.randint(0, 4)]
    b2 = np.random.randint(2, b1)

    while gcd(b1, b2) != 1:
        b2 = np.random.randint(2, b1)

    n = round(100/b1)
    b3 = b2 * n

    b_ = round(b3/100, 2)

    abc_list = [a_, b_, c_]
    abc_list.sort()

    d_ = abc_list[0]
    e_ = abc_list[1]
    f_ = abc_list[2]

    x1 = f"{a_}"
    x2 = f"{b2} over {b1}"
    x3 = f"{c_}"

    candidates = [x1, x2, x3]
    np.random.shuffle(candidates)
    [s1, s2, s3] = candidates

    lg = "{"
    rg = "}"

    stem = stem.format(s1 = s1, s2 = s2, s3 = s3)
    answer = answer.format(d_ = d_)
    comment = comment.format(lg = lg, rg = rg, b1 = b1, b2 = b2, b3 = b3, n = n, b_ = b_, d_ = d_, e_ = e_, f_ = f_)

    return stem, answer, comment



























# 5-1-4-73
def reductionfra514_Stem_050():
    stem = "분수와 소수를 비교하여 작은 수부터 차례대로 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${a_}$$/수식$$     ㉡ $$수식$${b2} over {b1}$$/수식$$      ㉢ $$수식$${c_}$$/수식$$      ㉣ $$수식$${d1} {d3} over {d2}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{aone}\n"
    comment = "(해설)\n$$수식$${b2} over {b1} ` = ` {lg} {b2} ` TIMES ` {n} {rg} over {lg} {b1} ` TIMES ` {n} {rg} ` = ` {b3} over 100 ` = ` {b_}$$/수식$$\n"\
              "$$수식$${d1} {d3} over {d2} ` = ` {d1} {lg} {d3} ` TIMES ` {p} {rg} over {lg} {d2} ` TIMES ` {p} {rg} ` = ` {d1} {d4} over 100 ` = ` {d_}$$/수식$$\n"\
              "$$수식$${e_} ` &lt; ` {f_} ` &lt; ` {g_} ` &lt; ` {h_}$$/수식$$이므로 작은 수부터 차례대로 기호를 쓰면 {aone}입니다.\n\n"


    a_ = round(np.random.randint(11, 20)/10, 1)

    b1 = [4, 20, 25, 50][np.random.randint(0, 4)]
    b2 = np.random.randint(2, b1)

    while gcd(b1, b2) != 1:
        b2 = np.random.randint(2, b1)

    n = round(100 / b1)
    b3 = b2 * n

    b_ = round(b3/100, 2)
    c_ = round(np.random.randint(2, 10)/10, 1)

    d1 = 1
    d2 = [4, 20, 25, 50][np.random.randint(0, 4)]

    while d2 == b1 :
        d2 = [4, 20, 25, 50][np.random.randint(0, 4)]

    d3 = np.random.randint(2, d2)

    while gcd(d2, d3) != 1:
        d3 = np.random.randint(2, d2)

    p = round(100 / d2)
    d4 = d3 * p

    d_ = round(d4 / 100 + 1, 2)

    efgh_list = [a_, b_, c_, d_]
    efgh_list.sort()

    e_ = efgh_list[0]
    f_ = efgh_list[1]
    g_ = efgh_list[2]
    h_ = efgh_list[3]

    if b_ < c_ and c_ < d_ and d_ < a_ :
        aone = "㉡, ㉢, ㉣, ㉠"
    elif b_ < c_ and c_ < a_ and a_ < d_ :
        aone = "㉡, ㉢, ㉠, ㉣"
    elif b_ < d_ and d_ < c_ and c_ < a_ :
        aone = "㉡, ㉣, ㉢, ㉠"
    elif b_ < d_ and d_ < a_ and a_ < c_ :
        aone = "㉡, ㉣, ㉠, ㉢"
    elif c_ < d_ and d_ < a_ and a_ < b_ :
        aone = "㉢, ㉣, ㉠, ㉡"
    elif c_ < d_ and d_ < b_ and b_ < a_ :
        aone = "㉢, ㉣, ㉡, ㉠"
    elif c_ < b_ and b_ < d_ and d_ < a_ :
        aone = "㉢, ㉡, ㉣, ㉠"
    elif c_ < b_ and b_ < a_ and a_ < d_ :
        aone = "㉢, ㉡, ㉠, ㉣"

    lg = "{"
    rg = "}"

    stem = stem.format(a_ = a_, b1 = b1, b2 = b2, c_ = c_, d1 = d1, d2 = d2, d3 = d3)
    answer = answer.format(aone = aone)
    comment = comment.format(d4 = d4, lg = lg, rg = rg, b1 = b1, b2 = b2, b3 = b3, n = n, b_ = b_, d_ = d_, e_ = e_, f_ = f_, g_ = g_, h_ = h_, d1 = d1, d2 = d2, d3 = d3, p = p, aone = aone)

    return stem, answer, comment



























# 5-1-4-74
def reductionfra514_Stem_051():
    stem = "{wh}{j1} {c_1} {s}{j2} $$수식$${a2} over {a1} `` rm m `$$/수식$$, {c_2} {s}{j2} $$수식$${b_} `` rm m `$$/수식$$ 가지고 있습니다. {c_1}{j3} {c_2} {s} 중에서 어떤 색 {s}의 길이가 더 긴가요?\n"
    answer = "(정답)\n{c_3}\n"
    comment = "(해설)\n$$수식$${a2} over {a1} ` = ` {lg} {a2} ` TIMES ` {n} {rg} over {lg} {a1} ` TIMES ` {n} {rg} ` = ` {a3} over 100 " \
              "` = ` {a_} $$/수식$$ → $$수식$${a_} ` {x} ` {b_}$$/수식$$\n" \
              "따라서 {c_3} {s}의 길이가 더 깁니다.\n\n"



    wh_list = ['민우', '슬기', '수지', '은호', '선우', '윤서', '지우', '정호', '현기', '재수', '영서', '은지', '연주', '주호', '혁구', '영기', '상수',
               '은서', '동우', '재우', '진희', '준서', '유라', '수미', '현수', '채아', '민주', '지호', '연아', '은우', '시우', '혁재', '민하']

    wh = wh_list.pop(np.random.randint(0, len(wh_list)))

    s = ['테이프', '종이테이프', '노끈'][np.random.randint(0, 3)]

    c_list = ['빨간색', '파란색', '노란색', '초록색', '보라색', '남색', '연두색', '주황색', '분홍색']

    c_1 = c_list.pop(np.random.randint(0, len(c_list)))
    c_2 = c_list.pop(np.random.randint(0, len(c_list)))

    a1 = [4, 20, 25, 50][np.random.randint(0, 4)]
    a2 = np.random.randint(2, a1)

    while gcd(a1, a2) != 1 :
        a2 = np.random.randint(2, a1)

    n = round(100/a1)
    a3 = a2 * n

    a_ = round(a3/100, 2)
    b_ = round(np.random.randint(2, 10)/10, 1)

    if a_ > b_ :
        x = "&gt;"
        c_3 = c_1
    elif a_ < b_ :
        x = "&lt;"
        c_3 = c_2

    lg = "{"
    rg = "}"

    j1 = proc_jo(wh, -1)
    j2 = proc_jo(s, 4)
    j3 = proc_jo(c_1, 2)


    stem = stem.format(j1=j1, j2=j2, j3=j3, wh=wh, c_1=c_1, c_2=c_2, s=s, a1=a1, a2=a2, b_=b_)
    answer = answer.format(c_3=c_3)
    comment = comment.format(x=x, lg=lg, rg=rg, a1=a1, a2=a2, a3=a3, n=n, a_=a_, b_=b_, c_3=c_3, s=s)

    return stem, answer, comment





























# 5-1-4-75
def reductionfra514_Stem_052():
    stem = "시소에 {wh1}{j1} {wh2}{j2} 타고 있습니다. {wh1}의 몸무게는 $$수식$${a_} `` rm kg `$$/수식$$이고, {wh2}의 몸무게는 $$수식$${b1} {b3} over {b2} `` rm kg `$$/수식$$입니다. 두 사람 중에서 누가 탄 쪽으로 시소가 내려가나요?\n"
    answer = "(정답)\n{wh3}\n"
    comment = "(해설)\n$$수식$$ {b1} {b3} over {b2} ` = ` {b1} {b4} over 100 ` = ` {b_} $$/수식$$  →  $$수식$${a_} {x} {b_}$$/수식$$\n" \
              "따라서 {wh3}의 몸무게가 더 무거우므로 {wh3}{j3} 탄 쪽으로 시소가 내려갑니다.\n\n"



    wh_list = ['민우', '슬기', '수지', '은호', '선우', '윤서', '지우', '정호', '현기', '재수', '영서', '은지', '연주', '주호', '혁구', '영기', '상수',
               '은서', '동우', '재우', '진희', '준서', '유라', '수미', '현수', '채아', '민주', '지호', '연아', '은우', '시우', '혁재', '민하']

    wh1 = wh_list.pop(np.random.randint(0, len(wh_list)))
    wh2 = wh_list.pop(np.random.randint(0, len(wh_list)))

    b1 = np.random.randint(27, 38)
    b2 = [4, 20, 25, 50][np.random.randint(0, 4)]
    b3 = np.random.randint(2, b2)

    while gcd(b2, b3) != 1:
        b3 = np.random.randint(2, b2)

    b4 = round(b3*(100/b2))
    b_ = round(b4/100, 2) + b1

    a1 = b1
    a2 = round(np.random.randint(1, 10)/10, 1)

    a_ = a1 + a2

    if a_ > b_:
        x = "&gt;"
        wh3 = wh1

    elif a_ < b_:
        x = "&lt;"
        wh3 = wh2

    j1 = proc_jo(wh1, 2)
    j2 = proc_jo(wh2, 0)
    j3 = proc_jo(wh3, 0)


    stem = stem.format(wh1=wh1, wh2=wh2, j1=j1, j2=j2, a_=a_, b1=b1, b2=b2, b3=b3)
    answer = answer.format(wh3=wh3)
    comment = comment.format(b1=b1, b2=b2, b3=b3, b4=b4, a_=a_, b_=b_, x=x, wh3=wh3, j3=j3)

    return stem, answer, comment



























# 5-1-4-78
def reductionfra514_Stem_053():
    stem = "{p_}에서 {p1}까지의 거리는 $$수식$${a1} {a3} over {a2} `` rm {{km}} `$$/수식$$, {p2}까지의 거리는 $$수식$${b2} over {b1} `` rm {{km}} `$$/수식$$, {p3}까지의 거리는 $$수식$${c_} `` rm {{km}} `$$/수식$$입니다. {p_}에서 가장 가까운 곳을 써 보세요.\n"
    answer = "(정답)\n{p4}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${p_}에서 {p1}까지의 거리$$수식$$RIGHT )$$/수식$$\n$$수식$$ ` = ` {a1} {a3} over {a2} ` = ` {a1} {lg}{a3} ` TIMES ` {n} {rg} over {lg} {a2} ` TIMES ` {n} {rg} " \
              "` = ` {a1} {a4} over 1000 ` = ` {a_} `` LEFT ( rm {{km}} RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${p_}에서 {p2}까지의 거리$$수식$$RIGHT )$$/수식$$\n$$수식$$ ` = ` {b2} over {b1} ` = ` {b3} {b4} over {b1} " \
              "` = ` {b3} {lg} {b4} ` TIMES ` {p} {rg} over {lg} {b1} ` TIMES ` {p} {rg} ` = ` {b3} {b5} over 100 ` = ` {b_} `` LEFT ( rm {{km}} RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${p_}에서 {p3}까지의 거리$$수식$$RIGHT ) ` = ` {c_} `` rm {{km}} `$$/수식$$\n" \
              "따라서 $$수식$$ {d_} ` &lt; ` {e_} ` &lt; ` {f_}$$/수식$$이므로 {p_}에서 {p4}까지의 거리가 가장 가깝습니다.\n\n"


    # p_ = ['집', '학교'][np.random.randint(0, 2)]
    #
    # p_list = ['병원', '경찰서', '소방서', '공원', '도서관', '영화관', '대형 마트', '터미널']
    #
    # p1 = p_list.pop(np.random.randint(0, len(p_list)))
    # p2 = p_list.pop(np.random.randint(0, len(p_list)))
    # p3 = p_list.pop(np.random.randint(0, len(p_list)))
    #
    # a1 = np.random.randint(1, 3)
    # a2 = [8, 40, 200, 250, 500][np.random.randint(1, 5)]
    # a3 = np.random.randint(2, a2)
    #
    # while gcd(a2, a3) != 1 :
    #     a3 = np.random.randint(2, a2)
    #
    # n = round(1000/a2)
    # a4 = a3 * n
    #
    # # a_ = a1 + round(a4/1000, 3)
    # a_ = round(a1 + round(a4/1000, 3), 4)
    #
    # b1 = [4, 20, 25, 50][np.random.randint(0, 4)]
    # b3 = a1
    # b4 = np.random.randint(2, b1)
    #
    # while gcd(b1, b4) != 1:
    #     b4 = np.random.randint(2, b1)
    #
    # b2 = b3 * b1 + b4
    # p = round(100 / b1)
    #
    # b5 = b4 * p
    # # b_ = b3 + round(b5/100, 2)
    # b_ = round(b3 + round(b5/100, 2), 3)
    #
    # c1 = a1
    # c2 = round(np.random.randint(111, 900)/1000, 3)
    #
    # while c2 == round(a4/1000, 3) :
    #     c2 = round(np.random.randint(111, 900) / 1000, 3)
    #
    # c_ = round(c1 + c2, 3)
    #
    # def_list = [a_, b_, c_]
    #
    # def_list.sort()
    #
    # d_ = def_list[0]
    # e_ = def_list[1]
    # f_ = def_list[2]
    #
    # if a_ < b_ and a_ < c_ :
    #     p4 = p1
    # elif b_ < a_ and b_ < c_ :
    #     p4 = p2
    # elif c_ < a_ and c_ < b_ :
    #     p4 = p3
    # else :
    #     p4 = f"{a_}, {b_}, {c_}"
    #
    # lg = "{"
    # rg = "}"



    # 중복을 피하기 위해 전체 while 문으로 포함

    while True:
        p_ = ['집', '학교'][np.random.randint(0, 2)]

        p_list = ['병원', '경찰서', '소방서', '공원', '도서관', '영화관', '대형 마트', '터미널']

        p1 = p_list.pop(np.random.randint(0, len(p_list)))
        p2 = p_list.pop(np.random.randint(0, len(p_list)))
        p3 = p_list.pop(np.random.randint(0, len(p_list)))

        a1 = np.random.randint(1, 3)
        a2 = [8, 40, 200, 250, 500][np.random.randint(1, 5)]
        a3 = np.random.randint(2, a2)

        while gcd(a2, a3) != 1:
            a3 = np.random.randint(2, a2)

        n = round(1000 / a2)
        a4 = a3 * n

        # a_ = a1 + round(a4/1000, 3)
        a_ = round(a1 + round(a4 / 1000, 3), 4)

        b1 = [4, 20, 25, 50][np.random.randint(0, 4)]
        b3 = a1
        b4 = np.random.randint(2, b1)

        while gcd(b1, b4) != 1:
            b4 = np.random.randint(2, b1)

        b2 = b3 * b1 + b4
        p = round(100 / b1)

        b5 = b4 * p
        # b_ = b3 + round(b5/100, 2)
        b_ = round(b3 + round(b5 / 100, 2), 3)

        c1 = a1
        c2 = round(np.random.randint(111, 900) / 1000, 3)

        while c2 == round(a4 / 1000, 3):
            c2 = round(np.random.randint(111, 900) / 1000, 3)

        c_ = round(c1 + c2, 3)

        def_list = [a_, b_, c_]

        def_list.sort()

        d_ = def_list[0]
        e_ = def_list[1]
        f_ = def_list[2]

        if a_ < b_ and a_ < c_:
            p4 = p1
        elif b_ < a_ and b_ < c_:
            p4 = p2
        elif c_ < a_ and c_ < b_:
            p4 = p3
        else:
            p4 = f"{a_}, {b_}, {c_}"

        lg = "{"
        rg = "}"

        if a_ != b_ and a_ != c_ and b_ != c_:
            break



    stem = stem.format(p_=p_, p1=p1, p2=p2, p3=p3, a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, c_=c_)
    answer = answer.format(p4=p4)
    comment = comment.format(lg=lg, rg=rg, p_=p_, p1=p1, p2=p2, p3=p3, p4=p4, a1=a1, a2=a2, a3=a3, a4=a4, n=n, a_=a_,
                             b1=b1, b2=b2, b3=b3, b4=b4, b5=b5, p=p, d_=d_, c_=c_, b_=b_, e_=e_, f_=f_)

    return stem, answer, comment






























# 5-1-4-79
def reductionfra514_Stem_054():
    stem = "□ 안에 들어갈 수 있는 분모가 $$수식$$1000$$/수식$$인 분수는 모두 몇 개인가요?\n$$표$$ $$수식$${a1} {a3} over {a2} ` &lt; `$$/수식$$□$$수식$$` &lt; ` {b_} $$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${n_}$$/수식$$개\n"
    comment = "(해설)\n$$수식$${a1} {a3} over {a2} ` = ` {a1} {lg} {a3} ` TIMES ` {p} {rg} over {lg} {a2} ` TIMES ` {p} {rg} ` = ` {a1} {a4} over 1000 $$/수식$$, " \
              "$$수식$$ {b_} ` = ` {b1} {b3} over 1000 $$/수식$$이므로 $$수식$${a1} {a4} over 1000 ` &lt; `$$/수식$$□$$수식$$` &lt; ` {b1} {b3} over 1000$$/수식$$입니다.\n" \
              "□ 안에 알맞은 분수의 분자는 $$수식$${m}$$/수식$$부터 $$수식$${n}$$/수식$$까지의 수이므로 구하는 분수는 모두 $$수식$${n_}$$/수식$$개입니다.\n\n"



    a1 = np.random.randint(1, 4)
    a2 = [8, 40, 200, 250, 500][np.random.randint(0, 5)]
    a3 = np.random.randint(2, round(a2 / 2) + 1)

    while gcd(a2, a3) != 1:
        a3 = np.random.randint(2, round(a2 / 2) + 1)

    p = round(1000 / a2)
    a4 = a3 * p

    b1 = a1
    b2 = np.random.randint((a4 + 9) / 10, (a4 + 19) / 10 + 1)
    b3 = b2 * 10

    b_ = round(b1 + b2 / 100, 2)
    m = a4 + 1
    n = b3 - 1
    n_ = n - m + 1

    lg = "{"
    rg = "}"


    stem = stem.format(lg=lg, rg=rg, a1=a1, a2=a2, a3=a3, b_=b_)
    answer = answer.format(n_=n_)
    comment = comment.format(lg=lg, rg=rg, a1=a1, a2=a2, a3=a3, p=p, b1=b1, b3=b3, b_=b_, a4=a4, m=m, n=n, n_=n_)

    return stem, answer, comment































# 5-1-4-80
def reductionfra514_Stem_055():
    stem = "높이가 다음과 같은 {s}{j1} 한 개씩 있습니다. 이 중에서 $$수식$$2$$/수식$$개를 골라 쌓으려고 합니다. 가장 높게 쌓기 위해 필요한 {s}{j2} 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${a_} `` rm m `$$/수식$$      ㉡ $$수식$${b2} over {b1} `` rm m `$$/수식$$      ㉢ $$수식$${c2} over {c1} `` rm m `$$/수식$$      ㉣ $$수식$${d2} over {d1} `` rm m `$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{x}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${a_} `` LEFT ( rm m RIGHT ) `$$/수식$$\n" \
              "㉡ $$수식$${b2} over {b1} ` = ` {b3} over 100 ` = ` {b_} `` LEFT ( rm m RIGHT ) `$$/수식$$\n" \
              "㉢ $$수식$${c2} over {c1} ` = ` {c3} over 1000 ` = ` {c_} `` LEFT ( rm m RIGHT ) `$$/수식$$\n" \
              "㉣ $$수식$${d2} over {d1} ` = ` {d3} over 1000 ` = ` {d_} `` LEFT ( rm m RIGHT ) `$$/수식$$\n" \
              "$$수식$$ {e_} ` &lt; ` {f_} ` &lt; ` {g_} ` &lt; ` {h_}$$/수식$$이므로 가장 높게 쌓기 위해 필요한 {s}{j3} {x}입니다.\n\n"


    s = ['벽돌', '블록'][np.random.randint(0, 2)]

    b1 = [4, 20, 25, 50][np.random.randint(0, 4)]
    b2 = np.random.randint(2, b1)

    while gcd(b1, b2) != 1:
        b2 = np.random.randint(2, b1)

    b3 = round(b2 * (100 / b1))

    b_ = round(b3 / 100, 2)
    c1 = [8, 25, 40, 125][np.random.randint(0, 4)]

    while c1 == b1 * 10 or c1 == b1:
        c1 = [8, 25, 40, 125][np.random.randint(0, 4)]

    c2 = np.random.randint(3, c1)

    while gcd(c1, c2) != 1:
        c2 = np.random.randint(3, c1)

    c3 = c2 * round(1000 / c1)
    c_ = round(c3 / 1000, 3)

    a_ = np.random.randint(min(b_ * 100, c_ * 1000) - 10 + 1, max(b_ * 100, c_ * 1000) + 10 + 1)
    a_ = round(a_ / 100, 2)

    while a_ == b_:
        a_ = np.random.randint(min(b_ * 100, c_ * 1000) - 10 + 1, max(b_ * 100, c_ * 1000) + 10 + 1)
        a_ = round(a_ / 100, 2)

    d1 = [200, 250, 500][np.random.randint(0, 3)]

    while d1 == b1 * 10:
        d1 = [200, 250, 500][np.random.randint(0, 3)]

    d2 = np.random.randint(50, d1 - 49)

    while gcd(d1, d2) != 1:
        d2 = np.random.randint(50, d1 - 49)

    d3 = d2 * round(1000 / d1)
    d_ = round(d3 / 1000, 3)

    efgh_list = [a_, b_, c_, d_]
    efgh_list.sort()

    e_ = efgh_list[0]
    f_ = efgh_list[1]
    g_ = efgh_list[2]
    h_ = efgh_list[3]

    if (g_ == a_ and h_ == b_) or (g_ == b_ and h_ == a_):
        x = "㉠, ㉡"
    elif (g_ == a_ and h_ == c_) or (g_ == c_ and h_ == a_):
        x = "㉠, ㉢"
    elif (g_ == a_ and h_ == d_) or (g_ == d_ and h_ == a_):
        x = "㉠, ㉣"
    elif (g_ == b_ and h_ == c_) or (g_ == c_ and h_ == b_):
        x = "㉡, ㉢"
    elif (g_ == b_ and h_ == d_) or (g_ == d_ and h_ == b_):
        x = "㉡, ㉣"
    elif (g_ == c_ and h_ == d_) or (g_ == d_ and h_ == c_):
        x = "㉢, ㉣"

    j1 = proc_jo(s, 0)
    j2 = proc_jo(s, 4)
    j3 = proc_jo(s, -1)


    stem = stem.format(s=s, j1=j1, j2=j2, a_=a_, b1=b1, b2=b2, c1=c1, c2=c2, d1=d1, d2=d2)
    answer = answer.format(x=x)
    comment = comment.format(a_=a_, b1=b1, b2=b2, c1=c1, c2=c2, d1=d1, d2=d2, b3=b3, c3=c3, d3=d3, b_=b_, c_=c_, d_=d_,
                             e_=e_, f_=f_, g_=g_, h_=h_, s=s, j3=j3, x=x)

    return stem, answer, comment
