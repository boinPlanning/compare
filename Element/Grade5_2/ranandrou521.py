"""
초등 5학년 2학기 1단원
"""


import numpy as np
import random
answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤"
}


answer_dict2 = {
        0: "㉠",
        1: "㉡",
        2: "㉢",
        3: "㉣"
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
    else:
        # 을를
        if bool_jo(num):
            return "을"
        return "를"








def get_josa(a, b):
    if b == "로" or b == "으로":
        if (str(a))[-1] == "0" or (str(a))[-1] == "3" or (str(a))[-1] == "6":
            return "으로"
        else:
            return "로"

    elif b == "와" or b == "과":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "와"
        else:
            return "과"













# 5-2-1-01
def ranandrou521_Stem_001():
    stem = "$$수식$${sa}$$/수식$$ 이상인 수는 모두 몇 개인가요?\n$$표$$$$수식$${t1}$$/수식$$     $$수식$${t2}$$/수식$$     $$수식$${t3}$$/수식$$     $$수식$${t4}$$/수식$$     $$수식$${t5}$$/수식$$     $$수식$${t6}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$과 같거나 큰 수는 " \
              "{saying1} " \
              "모두 $$수식$${ss}$$/수식$$개입니다.\n\n"



    ans_choice = np.random.randint(2, 5)

    if ans_choice == 2:
        while True:
            while 1:
                sa = [20, 30, 40, 50, 60, 70, 80, 90][np.random.randint(0, 8)]
                a1 = np.random.randint(1, 10)
                b1 = np.random.randint(1, 10)
                b2 = np.random.randint(1, 10)
                b3 = np.random.randint(1, 10)
                b4 = np.random.randint(1, 10)
                b5 = np.random.randint(1, 10)
                b6 = np.random.randint(1, 10)
                if b1 < b2 < b3 < b4 and sa - a1 + 1 < sa:
                    break

            ss1 = np.random.randint(sa - a1 + 1, sa)
            ss2 = np.random.randint(sa + a1 + 1, sa + a1 + 11)
            ss3 = np.random.randint(sa + 11, sa + 21)

            s1 = round(ss1 + b1 * 0.1, 1)
            s2 = round(ss1 + b2 * 0.1, 1)
            s3 = round(ss1 + b3 * 0.1, 1)
            s4 = round(ss1 + b4 * 0.1, 1)
            s5 = round(ss2 + b5 * 0.1, 1)
            s6 = round(ss3 + b6 * 0.1, 1)

            x1 = s5
            x2 = s6
            ss = 2

            ro1 = get_josa(x2, "로")
            saying1 = f"$$수식$${x1}$$/수식$$, $$수식$${x2}$$/수식$${ro1}"

            if sa > s1 and sa > s2 and sa > s3 and sa > s4 and sa <= s5 and sa <= s6:
                if s5 < s6:
                    break

    elif ans_choice == 3:
        while True:
            while 1:
                sa = [20, 30, 40, 50, 60, 70, 80, 90][np.random.randint(0, 8)]
                a1 = np.random.randint(1, 10)
                b1 = np.random.randint(1, 10)
                b2 = np.random.randint(1, 10)
                b3 = np.random.randint(1, 10)
                b4 = np.random.randint(1, 10)
                b5 = np.random.randint(1, 10)
                b6 = np.random.randint(1, 10)
                if b1 < b2 < b3 and b4 < b5 and sa - a1 + 1 < sa:
                    break

            ss1 = np.random.randint(sa - a1 + 1, sa)
            ss2 = np.random.randint(sa + a1 + 1, sa + a1 + 11)
            ss3 = np.random.randint(sa + 11, sa + 21)

            s1 = round(ss1 + b1 * 0.1, 1)
            s2 = round(ss1 + b2 * 0.1, 1)
            s3 = round(ss1 + b3 * 0.1, 1)
            s4 = round(ss2 + b4 * 0.1, 1)
            s5 = round(ss2 + b5 * 0.1, 1)
            s6 = round(ss3 + b6 * 0.1, 1)

            x1 = s4
            x2 = s5
            x3 = s6
            ss = 3

            ro1 = get_josa(x3, "로")
            saying1 = f"$$수식$${x1}$$/수식$$, $$수식$${x2}$$/수식$$, $$수식$${x3}$$/수식$${ro1}"

            if sa > s1 and sa > s2 and sa > s3 and sa <= s4 and sa <= s5 and sa <= s6:
                if s4 < s5 < s6:
                    break

    elif ans_choice == 4:
        while True:
            while 1:
                sa = [20, 30, 40, 50, 60, 70, 80, 90][np.random.randint(0, 8)]
                a1 = np.random.randint(1, 10)
                b1 = np.random.randint(1, 10)
                b2 = np.random.randint(1, 10)
                b3 = np.random.randint(1, 10)
                b4 = np.random.randint(1, 10)
                b5 = np.random.randint(1, 10)
                b6 = np.random.randint(1, 10)
                if b1 < b2 and b3 < b4 < b5 and sa - a1 + 1 < sa:
                    break

            ss1 = np.random.randint(sa - a1 + 1, sa)
            ss2 = np.random.randint(sa + a1 + 1, sa + a1 + 11)
            ss3 = np.random.randint(sa + 11, sa + 21)

            s1 = round(ss1 + b1 * 0.1, 1)
            s2 = round(ss1 + b2 * 0.1, 1)
            s3 = round(ss2 + b3 * 0.1, 1)
            s4 = round(ss2 + b4 * 0.1, 1)
            s5 = round(ss2 + b5 * 0.1, 1)
            s6 = round(ss3 + b6 * 0.1, 1)

            x1 = s3
            x2 = s4
            x3 = s5
            x4 = s6
            ss = 4

            ro1 = get_josa(x4, "로")
            saying1 = f"$$수식$${x1}$$/수식$$, $$수식$${x2}$$/수식$$, $$수식$${x3}$$/수식$$, $$수식$${x4}$$/수식$${ro1}"

            if sa > s1 and sa > s2 and sa <= s3 and sa <= s4 and sa <= s5 and sa <= s6:
                if s3 < s4 < s5 < s6:
                    break


    candidates = [s1, s2, s3, s4, s5, s6]
    np.random.shuffle(candidates)
    [t1, t2, t3, t4, t5, t6] = candidates


    stem = stem.format(sa=sa, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5, t6=t6)
    answer = answer.format(ss=ss)
    comment = comment.format(sa=sa, saying1=saying1, ss=ss)

    return stem, answer, comment



    # while 1:
    #     sa = [20, 30, 40, 50, 60, 70, 80, 90][np.random.randint(0, 8)]
    #     a1 = np.random.randint(1, 10)
    #     b1 = np.random.randint(1, 10)
    #     b2 = np.random.randint(1, 10)
    #     b3 = np.random.randint(1, 10)
    #     b4 = np.random.randint(1, 10)
    #     b5 = np.random.randint(1, 10)
    #     b6 = np.random.randint(1, 10)
    #     if b1 < b2 < b3 and b4 < b5 and sa - a1 + 1 < sa:
    #         break
    #
    # ss1 = np.random.randint(sa - a1 + 1, sa)
    # ss2 = np.random.randint(sa + a1 + 1, sa + a1 + 11)
    # ss3 = np.random.randint(sa + 11, sa + 21)
    #
    # s1 = ss1 + b1 * 0.1
    # s2 = ss1 + b2 * 0.1
    # s3 = ss1 + b3 * 0.1
    # s4 = ss2 + b4 * 0.1
    # s5 = ss2 + b5 * 0.1
    # s6 = ss3 + b6 * 0.1
    #
    # x1 = s4
    # x2 = s5
    # x3 = s6
    # ss = 3















































# 5-2-1-02
def ranandrou521_Stem_002():
    stem = "$$수식$${sa}$$/수식$$ 이하인 자연수들의 합을 구해 보세요\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$ 이하인 자연수는 $$수식$${sa}$$/수식$${gwa1} 같거나 작은 자연수이므로 {x1}입니다.\n" \
              "$$수식$$LEFT ({sa}$$/수식$$ 이하인 자연수의 합$$수식$$RIGHT )$$/수식$$\n$$수식$$ ` = ` {x2} ` = ` {ss}$$/수식$$\n\n"


    sa = np.random.randint(4, 10)
    ss = 0
    i = 1

    xlist = []

    while i <= sa:
        xlist.append(str(i))
        ss += i
        i += 1

    xlist.reverse()
    # x1 = ",~".join(xlist)
    x2 = " + ".join(xlist)

    x1 = ""
    for i_dx in xlist:
        if x1 == "":
            x1 = "$$수식$$%s$$/수식$$" % i_dx
        else:
            x1 = x1 + ", $$수식$$%s$$/수식$$" % i_dx

    gwa1 = get_josa(sa, "과")


    stem = stem.format(sa=sa)
    answer = answer.format(ss=ss)
    comment = comment.format(sa=sa, x1=x1, x2=x2, ss=ss, gwa1=gwa1)

    return stem, answer, comment



















































# 5-2-1-03
def ranandrou521_Stem_003():
    stem = "$$수식$${sa}$$/수식$$ 이하인 자연수들의 개수는 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$ 이하인 자연수는 $$수식$${sa}$$/수식$${gwa1} 같거나 작은 자연수이므로\n {x1}입니다.\n" \
              "따라서 $$수식$${sa}$$/수식$$ 이하인 자연수들의 개수는 $$수식$${ss}$$/수식$$개입니다.\n\n"


    sa = np.random.randint(4, 15)
    i = 1
    xlist = []

    while i <= sa:
        xlist.append(str(i))
        i += 1

    xlist.reverse()
    # x1 = ",~".join(xlist)
    ss = sa

    x1 = ""
    for i_dx in xlist:
        if x1 == "":
            x1 = "$$수식$$%s$$/수식$$" % i_dx
        else:
            x1 = x1 + ", $$수식$$%s$$/수식$$" % i_dx

    gwa1 = get_josa(sa, "과")


    stem = stem.format(sa=sa)
    answer = answer.format(ss=ss)
    comment = comment.format(sa=sa, x1=x1, ss=ss, gwa1=gwa1)

    return stem, answer, comment





















































# 5-2-1-05
def ranandrou521_Stem_004():
    stem = "□ 안에 들어갈 수 있는 수 중에서 가장 작은 자연수를 구해 보세요.\n$$표$$$$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$${p1} □ 이하인 수입니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${s3}$$/수식$$\n"
    comment = "(해설)\n" \
              "주어진 수는 $$수식$${s3}$$/수식$${p2} 같거나 작은 수입니다.\n" \
              "→ $$수식$${s3}$$/수식$$ 이하인 수\n\n"


    while 1:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(1, 10)

        if a1 != a2 != a3:
            break

    s3 = a1 * 100 + a2 * 10 + a3 * 1
    s2 = s3 - 1
    s1 = s2 - 1

    p1 = proc_jo(s3, -1)
    p2 = proc_jo(s3, 2)


    stem = stem.format(s1=s1, s2=s2, s3=s3, p1=p1)
    answer = answer.format(s3=s3)
    comment = comment.format(s3=s3, p2=p2)

    return stem, answer, comment




















































# 5-2-1-07
def ranandrou521_Stem_005():
    stem = "{n1}와 {n2} 중에서 잘못 말한 학생은 누구인가요?\n$$표$${t1}\n{t2}$$/표$$\n"
    answer = "(정답)\n{n2}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT [$$/수식$${n2}$$수식$$RIGHT ]$$/수식$$ $$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$$ 중에서 " \
              "$$수식$${s2}$$/수식$$ 이하인 수는 $$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$입니다.\n\n"


    n1 = ["현지", "순호", "성우", "운서", "상희"][np.random.randint(0, 5)]
    n2 = ["선기", "미우", "현서", "우호", "석우"][np.random.randint(0, 5)]

    while 1:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(1, 10)

        if a1 != a2:
            break

    sa = np.random.randint(21, 100)

    s3 = a1 * 10 + a2 * 1
    s2 = s3 - 1
    s1 = s2 - 1

    p1 = proc_jo(sa, 0)
    t1 = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ $$수식$$%d$$/수식$$ 이상인 수에는 $$수식$$%d$$/수식$$%s 포함됩니다." % (n1, sa, sa, p1)
    t2 = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$ 중에서 $$수식$$%d$$/수식$$ 이하인 수는 $$수식$$%d$$/수식$$뿐입니다." % (n2, s1, s2, s3, s2, s1)

    candidates = [t1, t2]
    np.random.shuffle(candidates)
    [t1, t2] = candidates


    stem = stem.format(n1=n1, n2=n2, t1=t1, t2=t2)
    answer = answer.format(n2=n2)
    comment = comment.format(n2=n2, s1=s1, s2=s2, s3=s3)

    return stem, answer, comment





















































# 5-2-1-09
def ranandrou521_Stem_006():
    stem = "다음은 {n1}가 $$수식$$□$$/수식$$ 이상인 자연수를 쓴 것입니다.  $$수식$$□$$/수식$$ 안에 들어갈 수 있는 자연수 중에서 가장 큰 수는 얼마인가요?\n$$표$$$$수식$${t1}$$/수식$$     $$수식$${t2}$$/수식$$     $$수식$${t3}$$/수식$$     $$수식$${t4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${s1}$$/수식$$\n"
    comment = "(해설)\n" \
              "주어진 수는 $$수식$${sa}$$/수식$${p1} 같거나 큰 수입니다.\n" \
              "□ 안에는 $$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$$, $$수식$$CDOTS  CDOTS$$/수식$${p2} 들어갈 수 있으므로 " \
              "이 중에서 가장 큰 수는 $$수식$${s1}$$/수식$$입니다.\n\n"


    n1 = ["성희", "현지", "순호", "성우", "운서", "상희", "선기", "미우", "현서", "우호", "석우"][np.random.randint(0, 11)]

    while 1:
        a1 = np.random.randint(5, 10)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(1, 10)
        if a3 > a2:
            break

    sa = a1 * 10 + a2
    sb = a1 * 10 + a3
    sc = (a1 + 1) * 10 + a2
    sd = (a1 + 1) * 10 + a3

    s1 = sa
    s2 = s1 - 1
    s3 = s1 - 2

    p1 = proc_jo(sa, 2)
    p2 = proc_jo(s3, 0)

    candidates = [sa, sb, sc, sd]
    np.random.shuffle(candidates)
    [t1, t2, t3, t4] = candidates


    stem = stem.format(n1=n1, t1=t1, t2=t2, t3=t3, t4=t4)
    answer = answer.format(s1=s1)
    comment = comment.format(sa=sa, s1=s1, s2=s2, s3=s3, p1=p1, p2=p2)

    return stem, answer, comment


















































# 5-2-1-15
def ranandrou521_Stem_007():
    stem = "$$수식$${sa}$$/수식$$ 초과인 자연수 중에서 가장 작은 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${s1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$ 초과인 자연수는 $$수식$${sa}$$/수식$$보다 큰 자연수이므로 " \
              "$$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$$, $$수식$${s4}$$/수식$$, $$수식$$CDOTS  CDOTS$$/수식$$입니다.\n" \
              "따라서 $$수식$${sa}$$/수식$$ 초과인 자연수 중에서 가장 작은 수는 $$수식$${s1}$$/수식$$입니다.\n\n"


    sa = np.random.randint(10, 20)

    s1 = sa + 1
    s2 = s1 + 1
    s3 = s2 + 1
    s4 = s3 + 1


    stem = stem.format(sa=sa)
    answer = answer.format(s1=s1)
    comment = comment.format(sa=sa, s1=s1, s2=s2, s3=s3, s4=s4)

    return stem, answer, comment




















































# 5-2-1-16
def ranandrou521_Stem_008():
    stem = "$$수식$${sa}$$/수식$$ 미만인 수를 잘못 쓴 사람은 누구인가요?\n$$표$${t1}\n{t2}\n{t3}$$/표$$\n"
    answer = "(정답)\n{n3}\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$ 미만인 수는 $$수식$${sa}$$/수식$$보다 작은 수이므로 " \
              "$$수식$${sa}$$/수식$${p1} 포함되지 않습니다.\n" \
              "따라서 잘못 쓴 사람은 $$수식$${sa}$$/수식$${p2} 쓴 {n3}입니다.\n\n"


    n1 = ["명호", "우주", "현희", "금호", "선주"][np.random.randint(0, 5)]
    n2 = ["지수", "영지", "선우", "석호", "명주"][np.random.randint(0, 5)]
    n3 = ["선희", "우호", "진희", "희수", "덕호"][np.random.randint(0, 5)]

    sa = np.random.randint(41, 60)

    a1 = sa - 13
    a2 = sa - 5
    a3 = sa - 2
    a4 = sa - 7
    a5 = sa - 11

    b1 = sa - 1
    b2 = sa - 14
    b3 = sa - 9
    b4 = sa - 6
    b5 = sa - 3

    c1 = sa - 4
    c2 = sa
    c3 = sa - 8
    c4 = sa - 17
    c5 = sa - 12

    p1 = proc_jo(sa, 0)
    p2 = proc_jo(sa, 3)

    candidates1 = [a1, a2, a3, a4, a5]
    candidates2 = [b1, b2, b3, b4, b5]
    candidates3 = [c1, c2, c3, c4, c5]

    np.random.shuffle(candidates1)
    np.random.shuffle(candidates2)
    np.random.shuffle(candidates3)

    [na1, na2, na3, na4, na5] = candidates1
    [nb1, nb2, nb3, nb4, nb5] = candidates2
    [nc1, nc2, nc3, nc4, nc5] = candidates3

    t1 = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$" % (n1, na1, na2, na3, na4, na5)
    t2 = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$" % (n2, nb1, nb2, nb3, nb4, nb5)
    t3 = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$" % (n3, nc1, nc2, nc3, nc4, nc5)

    candidates = [t1, t2, t3]
    np.random.shuffle(candidates)
    [t1, t2, t3] = candidates


    stem = stem.format(sa=sa, t1=t1, t2=t2, t3=t3)
    answer = answer.format(n3=n3)
    comment = comment.format(sa=sa, n3=n3, p1=p1, p2=p2)

    return stem, answer, comment



















































# 5-2-1-18
def ranandrou521_Stem_009():
    stem = "$$수식$${sa}$$/수식$$ 미만인 수는 모두 몇 개 인가요?\n$$표$$$$수식$${t1}$$/수식$$     $$수식$${t2}$$/수식$$     $$수식$${t3}$$/수식$$     $$수식$${t4}$$/수식$$     $$수식$${t5}$$/수식$$     $$수식$${t6}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$보다 작은 수는 {saying1} " \
              "모두 $$수식$${ss}$$/수식$$개입니다.\n\n"

    ans_choice = np.random.randint(2, 5)

    if ans_choice == 2:
        ss = 2

        sa = np.random.randint(11, 20)

        s1 = np.random.randint(6, 10)

        s2 = round(sa - 1 + 0.1 * (np.random.randint(1, 10)), 1)

        s3 = round(sa + 0.1 * (np.random.randint(1, 10)), 1)

        s4 = "%s ` 1 over %s" % (sa, np.random.randint(2, 10))

        s5 = sa

        s6 = "%s ` 1 over %s" % (sa + np.random.randint(1, 4), np.random.randint(2, 10))

        ro1 = get_josa(s2, "로")

        saying1 = f"$$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$${ro1}"


    elif ans_choice == 3:
        ss = 3

        sa = np.random.randint(11, 20)

        s1 = np.random.randint(6, 10)

        s2 = round(sa - 1 + 0.1 * (np.random.randint(1, 10)), 1)

        s3 = round(sa + 0.1 * (np.random.randint(1, 10)), 1)

        s4 = "%s ` 1 over %s" % (sa - 2, np.random.randint(2, 10))

        s5 = sa

        s6 = "%s ` 1 over %s" % (sa + np.random.randint(1, 4), np.random.randint(2, 10))

        ro1 = get_josa(s2, "로")

        saying1 = f"$$수식$${s1}$$/수식$$, $$수식$${s4}$$/수식$$, $$수식$${s2}$$/수식$${ro1}"


    elif ans_choice == 4:
        ss = 4

        sa = np.random.randint(11, 20)

        s1 = np.random.randint(6, 10)

        s2 = round(sa - 1 + 0.1 * (np.random.randint(1, 10)), 1)

        s3 = round(sa + 0.1 * (np.random.randint(1, 10)), 1)

        s4 = "%s ` 1 over %s" % (sa - 2, np.random.randint(2, 10))

        s5 = sa

        s6 = "%s ` 1 over %s" % (sa - 3, np.random.randint(2, 10))

        saying1 = f"$$수식$${s1}$$/수식$$, $$수식$${s6}$$/수식$$, $$수식$${s4}$$/수식$$, $$수식$${s2}$$/수식$$로"


    candidates = [s1, s2, s3, s4, s5, s6]
    np.random.shuffle(candidates)
    [t1, t2, t3, t4, t5, t6] = candidates


    stem = stem.format(sa=sa, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5, t6=t6)
    answer = answer.format(ss=ss)
    # comment = comment.format(sa=sa, s1=s1, s2=s2, s4=s4, s6=s6, ss=ss)
    comment = comment.format(sa=sa, saying1=saying1, ss=ss)

    return stem, answer, comment




    # sa = np.random.randint(11, 20)
    # s1 = np.random.randint(6, 10)
    #
    # a1 = sa - 1
    # a2 = np.random.randint(1, 10)
    # s2 = round(a1 + a2 * 0.1, 1)
    #
    # a3 = sa
    # a4 = np.random.randint(1, 10)
    # s3 = round(a3 + a4 * 0.1, 1)
    #
    # a5 = sa - 2
    # a6 = np.random.randint(1, 10)
    # s4 = "%d`1 over %d" % (a5, a6)
    # s5 = sa
    #
    # a7 = sa - 3
    # a8 = np.random.randint(1, 10)
    # s6 = "%d`1 over %d" % (a7, a8)
    #
    # ss = 4



















































# 5-2-1-21
def ranandrou521_Stem_010():
    stem = "$$수식$${sa}$$/수식$${p1} 포함되지 않는 수의 범위를 찾아 기호를 써 보세요.\n$$표$$㉠ {t1}\n㉡ {t2}\n㉢ {t3}$$/표$$\n"
    answer = "(정답)\n{st}\n"
    comment = "(해설)\n" \
              "㉠ {t1}: {c1}\n" \
              "㉡ {t2}: {c2}\n" \
              "㉢ {t3}: {c3}\n" \
              "따라서 $$수식$${sa}$$/수식$${p1} 포함되지 않는 수의 범위는 {st}입니다.\n\n"



    sa = np.random.randint(31, 50)

    x1 = "$$수식$$%d$$/수식$$ 초과인 자연수" % sa
    x2 = "$$수식$$%d$$/수식$$ 이하인 자연수" % sa
    x3 = "$$수식$$%d$$/수식$$ 이상인 자연수" % sa

    s1 = sa + 1
    s2 = sa + 2
    s3 = sa + 3

    u1 = sa
    u2 = sa - 1
    u3 = sa - 2

    z1 = sa
    z2 = sa + 1
    z3 = sa + 2

    c1 = "$$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$" % (s1, s2, s3)
    c2 = "$$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$" % (u1, u2, u3)
    c3 = "$$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$" % (z1, z2, z3)

    candidates1 = [x1, x2, x3]
    candidates2 = [c1, c2, c3]

    combine = list(zip(candidates1, candidates2))
    np.random.shuffle(combine)
    [t1, t2, t3], [c1, c2, c3] = zip(*combine)
    alist = [t1, t2, t3]

    correct_idx = 0
    for idx, sdx in enumerate(alist):
        if sdx == x1:
            correct_idx = idx
            break

    p1 = proc_jo(sa, 0)


    stem = stem.format(sa=sa, t1=t1, t2=t2, t3=t3, p1=p1)
    answer = answer.format(st=answer_dict2[correct_idx])
    comment = comment.format(t1=t1, t2=t2, t3=t3, c1=c1, c2=c2, c3=c3, sa=sa, st=answer_dict2[correct_idx], p1=p1)

    return stem, answer, comment


















































# 5-2-1-22
def ranandrou521_Stem_011():
    stem = " $$수식$$□$$/수식$$ 미만인 자연수는 $$수식$${sa}$$/수식$$개입니다.  $$수식$$□$$/수식$$ 안에 알맞은 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$\n"
    comment = "(해설)\n" \
              " $$수식$$□$$/수식$$ 미만인 자연수는 $$수식$${sa}$$/수식$$개이므로  $$수식$$□$$/수식$$보다 작은 자연수는 {x1}입니다.\n" \
              "따라서  $$수식$$□$$/수식$$ 안에 알맞은 자연수는 $$수식$${ss}$$/수식$$입니다.\n\n"


    sa = np.random.randint(10, 20)
    i = 1
    xlist = []

    while i <= sa:
        xlist.append(str(i))
        i += 1

    # x1 = ",~".join(xlist)
    ss = sa + 1

    x1 = ""
    for i_dx in xlist:
        if x1 == "":
            x1 = "$$수식$$%s$$/수식$$" % i_dx
        else:
            x1 = x1 + ", $$수식$$%s$$/수식$$" % i_dx


    stem = stem.format(sa=sa)
    answer = answer.format(ss=ss)
    comment = comment.format(sa=sa, x1=x1, ss=ss)

    return stem, answer, comment





















































# 5-2-1-24
def ranandrou521_Stem_012():
    stem = "자연수 부분이 $$수식$${ssa}$$/수식$$인 소수 한 자리 수 중에서 $$수식$${sa}$$/수식$$ 미만인 수는 모두 몇 개인가요? $$수식$$LEFT ($$/수식$$단, 소수 첫째 자리 숫자가 $$수식$$0$$/수식$$인 경우는 생각하지 않는다.$$수식$$RIGHT )$$/수식$$\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$개\n"
    comment = "(해설)\n" \
              "자연수 부분이 $$수식$${ssa}$$/수식$$인 소수 한 자리 수 → $$수식$${ssa}$$/수식$$.□\n" \
              "$$수식$${sa}$$/수식$$ 미만인 수는 $$수식$${sa}$$/수식$$보다 작은 수이므로 " \
              "{x1}{ro1}모두 $$수식$${ss}$$/수식$$개입니다.\n\n"


    ssa = np.random.randint(1, 10)
    ssb = np.random.randint(1, 10)
    sa = round(ssa + ssb * 0.1, 1)
    ss = ssb - 1

    i = 1
    xlist = []

    while i <= ssb - 1:
        xlist.append(str(round(ssa + i * 0.1, 1)))
        i += 1

    # x1 = ",~".join(xlist)

    x1 = ""
    for i_dx in xlist:
        if x1 == "":
            x1 = "$$수식$$%s$$/수식$$" % i_dx
        else:
            x1 = x1 + ", $$수식$$%s$$/수식$$" % i_dx

    if len(xlist) == 0:
        ro1 = ""
    else:
        ro1 = get_josa(xlist[-1], "로") + " "


    stem = stem.format(sa=sa, ssa=ssa)
    answer = answer.format(ss=ss)
    comment = comment.format(ssa=ssa, sa=sa, x1=x1, ss=ss, ro1=ro1)

    return stem, answer, comment






















































# 5-2-1-25
def ranandrou521_Stem_013():
    stem = "$$수식$${sa}$$/수식$$ 초과 $$수식$${sb}$$/수식$$ 미만인 수를 모두 찾아 써 보세요.\n$$표$$$$수식$${t1}$$/수식$$     $$수식$${t2}$$/수식$$     $$수식$${t3}$$/수식$$     $$수식$${t4}$$/수식$$     $$수식$${t5}$$/수식$$     $$수식$${t6}$$/수식$$     $$수식$${t7}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${s3}$$/수식$$, $$수식$${s7}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$보다 큰 수: $$수식$${big1}$$/수식$$, $$수식$${big2}$$/수식$$, $$수식$${big3}$$/수식$$, $$수식$${big4}$$/수식$$, $$수식$${big5}$$/수식$$\n" \
              "$$수식$${sb}$$/수식$$보다 작은 수: $$수식$${small1}$$/수식$$, $$수식$${small2}$$/수식$$, $$수식$${small3}$$/수식$$, $$수식$${small4}$$/수식$$\n" \
              "따라서 $$수식$${sa}$$/수식$$ 초과 $$수식$${sb}$$/수식$$ 미만인 수는 $$수식$${s3}$$/수식$$, $$수식$${s7}$$/수식$$입니다.\n\n"


    while True:
        sa = np.random.randint(21, 70)
        sb = np.random.randint(sa + 11, 90)

        s1 = np.random.randint(sb + 1, sb + 5)
        s2 = sb
        s3 = np.random.randint(sa + 1, sb - 5)
        s4 = np.random.randint(1, sa)
        s5 = sa
        s7 = np.random.randint(sa + 1, sb)

        if s3 < s7 and sb + 1 < s1:
            break

    s6 = np.random.randint(sb + 1, s1)

    sa_list = [s1, s2, s3, s6, s7]
    sa_list.sort()
    [big1, big2, big3, big4, big5] = sa_list

    sb_list = [s3, s4, s5, s7]
    sb_list.sort()
    [small1, small2, small3, small4] = sb_list



    candidates = [s1, s2, s3, s4, s5, s6, s7]
    np.random.shuffle(candidates)
    [t1, t2, t3, t4, t5, t6, t7] = candidates


    stem = stem.format(sa=sa, sb=sb, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5, t6=t6, t7=t7)
    answer = answer.format(s3=s3, s7=s7)
    comment = comment.format(sa=sa, big1=big1, big2=big2, big3=big3, big4=big4, big5=big5, sb=sb, small1=small1, small2=small2, small3=small3, small4=small4, s3=s3, s7=s7)

    return stem, answer, comment























































# 5-2-1-27
def ranandrou521_Stem_014():
    stem = "□ 안에 이상, 이하, 초과, 미만 중에서 알맞은 말을 써넣으세요.\n$$표$$$$수식$${sa}$$/수식$$     $$수식$${sb}$$/수식$$     $$수식$${sc}$$/수식$$     $$수식$${sd}$$/수식$$     $$수식$${se}$$/수식$$     $$수식$${sf}$$/수식$$     $$수식$${sg}$$/수식$$$$/표$$\n→ $$수식$${s1}$$/수식$$ {box1} $$수식$${s2}$$/수식$$ {box2}인 자연수\n"
    answer = "(정답)\n{t1}, {t2}\n"
    comment = "(해설)\n" \
              "{x1}\n" \
              "또 {x2}\n\n"


    sa = np.random.randint(21, 90)
    sb = sa + 1
    sc = sa + 2
    sd = sa + 3
    se = sa + 4
    sf = sa + 5
    sg = sa + 6

    s1 = [sa - 1, sa][np.random.randint(0, 2)]
    s2 = [sg, sg + 1][np.random.randint(0, 2)]

    p1 = proc_jo(s1, 3)
    p2 = proc_jo(s2, 3)

    if s1 == sa:
        t1 = "이상"
        x1 = "$$수식$$%d$$/수식$$%s 포함하고 $$수식$$%d$$/수식$$보다 큰 수이므로 $$수식$$%d$$/수식$$ 이상인 수입니다." % (s1, p1, s1, s1)

    elif s1 == sa - 1:
        t1 = "초과"
        x1 = "$$수식$$%d$$/수식$$%s 포함하지 않고 $$수식$$%d$$/수식$$보다 큰 수이므로 $$수식$$%d$$/수식$$ 초과인 수입니다." % (s1, p1, s1, s1)

    if s2 == sg:
        t2 = "이하"
        x2 = "$$수식$$%d$$/수식$$%s 포함하고 $$수식$$%d$$/수식$$보다 작은 수이므로 $$수식$$%d$$/수식$$ 이하인 수입니다." % (s2, p2, s2, s2)

    elif s2 == sg + 1:
        t2 = "미만"
        x2 = "$$수식$$%d$$/수식$$%s 포함하지 않고 $$수식$$%d$$/수식$$보다 작은 수이므로 $$수식$$%d$$/수식$$ 미만인 수입니다." % (s2, p2, s2, s2)

    box1 = "$$수식$$box{㉠````````````````````}$$/수식$$"
    box2 = "$$수식$$box{㉡````````````````````}$$/수식$$"


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, s1=s1, s2=s2, box1=box1, box2=box2)
    answer = answer.format(t1=t1, t2=t2)
    comment = comment.format(x1=x1, x2=x2)

    return stem, answer, comment























































# 5-2-1-34
def ranandrou521_Stem_015():
    stem = "자연수 부분이 $$수식$${sa}$$/수식$$, 소수 둘째 자리 숫자가 $$수식$${sb}$$/수식$$인 소수 두 자리 수 중에서 $$수식$${o1}$$/수식$$ 초과 $$수식$${o2}$$/수식$$ 이하인 수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$개\n"
    comment = "(해설)\n" \
              "자연수 부분이 $$수식$${sa}$$/수식$$, 소수 둘째 자리 숫자가 $$수식$${sb}$$/수식$$인 소수 두 자리 수 → $$수식$${sa}.□{sb}$$/수식$$\n" \
              "$$수식$${o1}$$/수식$$ 초과 $$수식$${o2}$$/수식$$ 이하인 수는 " \
              "{x1}이므로 모두 $$수식$${ss}$$/수식$$개입니다.\n\n"


    sa = np.random.randint(1, 10)
    sb = np.random.randint(1, 10)

    while True:
        sc = np.random.randint(1, 4)
        sd = np.random.randint(5, 10)
        if sc < sd:
            break

    o1 = round(sa + sc * 0.1, 1)
    o2 = round(sa + sd * 0.1, 1)
    ss = sd - sc

    i = 0
    # xlist = []
    # x1 = 0
    x1 = ""

    while sc + i + 1 <= sd:
        # xlist.append(str(round(sa + (sc + i) * 0.1 + sb * 0.01, 2)))
        # i += 1
        # x1 = ",~".join(xlist)
        if x1 == "":
            plus_material = str(round(sa + (sc + i) * 0.1 + sb * 0.01, 2))
            x1 += "$$수식$$%s$$/수식$$" % plus_material
            i += 1
        else:
            plus_material = str(round(sa + (sc + i) * 0.1 + sb * 0.01, 2))
            x1 += ", " + "$$수식$$%s$$/수식$$" % plus_material
            i += 1


    stem = stem.format(sa=sa, sb=sb, o1=o1, o2=o2)
    answer = answer.format(ss=ss)
    comment = comment.format(sa=sa, sb=sb, o1=o1, o2=o2, x1=x1, ss=ss)

    return stem, answer, comment

























































# 5-2-1-36
def ranandrou521_Stem_016():
    stem = "다음은 어느 {A}의 이용 요금을 나타낸 것입니다. 이 {A}을(를) $$수식$${sa}$$/수식$$분 동안 사용한다면 내야 하는 요금은 얼마인가요?\n$$표$$― 이용 요금 ―\n· 기본 $$수식$$1$$/수식$$시간 요금: $$수식$${sb}$$/수식$$원\n· $$수식$$1$$/수식$$시간 초과시 $$수식$$5$$/수식$$분마다 $$수식$${sc}$$/수식$$원$$/표$$\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$원\n"
    comment = "(해설)\n" \
              "$$수식$$60$$/수식$$분 $$수식$$=$$/수식$$ $$수식$$1$$/수식$$시간이므로 $$수식$${sa}$$/수식$$분 $$수식$$=$$/수식$$ $$수식$${s1}$$/수식$$시간 $$수식$${s2}$$/수식$$분입니다.\n" \
              "$$수식$${s1}$$/수식$$시간 $$수식$${s2}$$/수식$$분 $$수식$$=$$/수식$$ $$수식$$1$$/수식$$시간 $$수식$$+$$/수식$$ $$수식$${x1}$$/수식$$시간 $$수식$${s2}$$/수식$$분이므로\n" \
              "기본 $$수식$$1$$/수식$$시간 요금에, $$수식$${x1}$$/수식$$시간 $$수식$${s2}$$/수식$$분 $$수식$$=$$/수식$$ $$수식$${x2}$$/수식$$분의\n추가 요금을 내야 합니다.\n" \
              "$$수식$$LEFT ( 이용 요금 RIGHT ) ` = ` {sb} ` + ` {sc} ` TIMES ` LEFT ( {x2} ` DIV ` 5 RIGHT ) $$/수식$$\n $$수식$$` = {sb} ` + ` {x3} ` = ` {ss} ` LEFT ( 원 RIGHT )$$/수식$$\n\n"

    A = random.choice(["주차장","PC방","스터디 카페", "노래방"])

    ssa = [10, 20, 30][np.random.randint(0, 3)]
    sn = np.random.randint(1, 12)
    ssb = 5 * sn
    sa = ssa * 10 + ssb

    sb = [4000, 5000, 6000][np.random.randint(0, 3)]
    sc = [500, 600, 700, 800, 900][np.random.randint(0, 5)]
    s1 = int(sa // 60)
    s2 = sa - s1 * 60
    x1 = s1 - 1
    x2 = x1 * 60 + s2
    x3 = int(sc * x2 / 5)
    ss = int(sb + x3)


    stem = stem.format(A=A, sa=sa, sb=sb, sc=sc)
    answer = answer.format(ss=ss)
    comment = comment.format(sa=sa, sb=sb, sc=sc, ss=ss, s1=s1, s2=s2, x1=x1, x2=x2, x3=x3)

    return stem, answer, comment























































# 5-2-1-38
def ranandrou521_Stem_017():
    stem = "$$수식$${sa}$$/수식$${pj} 올림하여 소수 첫째 자리까지 나타내면 얼마인가요?\n"
    answer = "(정답)\n$$수식$${sb}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$${pj} 올림하여 소수 첫째 자리까지 나타내면 " \
              "$$수식$${sa}$$/수식$$ → $$수식$${sb}$$/수식$$\n\n"


    a1 = np.random.randint(1, 10)
    a2 = np.random.randint(1, 10)
    a3 = np.random.randint(1, 10)
    a4 = np.random.randint(1, 10)

    sa = round(a1 + a2 * 0.1 + a3 * 0.01 + a4 * 0.001, 3)
    sb = round(a1 + (a2 + 1) * 0.1, 2)

    pj = proc_jo(a4, 3)


    stem = stem.format(sa=sa, sb=sb, pj=pj)
    answer = answer.format(sb=sb)
    comment = comment.format(sa=sa, sb=sb, pj=pj)

    return stem, answer, comment

























































# 5-2-1-39
def ranandrou521_Stem_018():
    stem = "수의 크기를 비교하여 $$수식$$□$$/수식$$ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$표$$㉠$$수식$${box1}$$/수식$$\n㉡$$수식$${box2}$$/수식$$$$/표$$\n$$수식$$㉠````□````㉡$$/수식$$"
    answer = "(정답)\n$$수식$${st}$$/수식$$\n"
    comment = "(해설) \n" \
              "$$수식$${sa}$$/수식$${pj1} 올림하여 백의 자리까지 나타낸 수는 $$수식$${sa}$$/수식$$ → $$수식$${s1}$$/수식$$입니다.\n" \
              "$$수식$${sb}$$/수식$${pj2} 올림하여 천의 자리까지 나타낸 수는 $$수식$${sb}$$/수식$$ → $$수식$${s2}$$/수식$$입니다.\n" \
              "따라서 $$수식$${s1} ` {st} ` {s2}$$/수식$$입니다.\n\n"


    a1 = np.random.randint(1, 10)
    a2 = np.random.randint(1, 10)
    a3 = 0
    a4 = np.random.randint(1, 10)

    b1 = a1
    b2 = 0
    b3 = 0
    b4 = np.random.randint(1, 10)

    sa = a1 * 1000 + a2 * 100 + a3 * 10 + a4
    sb = b1 * 1000 + b2 * 100 + b3 * 10 + b4

    s1 = a1 * 1000 + (a2 + 1) * 100
    s2 = (b1 + 1) * 1000

    if s1 == s2:
        st = "="
    elif s1 > s2:
        st = "&gt;"
    elif s1 < s2:
        st = "&lt;"

    # pj1 = proc_jo(sa, 3)
    # pj2 = proc_jo(sb, 3)

    pj1 = proc_jo(a4, 3)
    pj2 = proc_jo(b4, 3)

    box = "□"
    box1 = "[``%d%s~올림하여~백의~자리까지~나타낸~수``]" % (sa, pj1)
    box2 = "[``%d%s~올림하여~천의~자리까지~나타낸~수``]" % (sb, pj2)


    stem = stem.format(sa=sa, sb=sb, box=box, box1=box1, box2=box2)
    answer = answer.format(st=st)
    comment = comment.format(sa=sa, sb=sb, pj1=pj1, pj2=pj2, s1=s1, s2=s2, st=st)

    return stem, answer, comment






















































# 5-2-1-40
def ranandrou521_Stem_019():
    stem = "올림하여 십의 자리까지 나타내면 $$수식$${sa}$$/수식$${pj} 되는 자연수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$개\n"
    comment = "(해설) \n" \
              "$$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$, $$수식$${s9}$$/수식$$, $$수식$${s10}$$/수식$$ " \
              "→ $$수식$${ss}$$/수식$$개\n\n"


    a1 = np.random.randint(1, 10)
    a2 = np.random.randint(1, 10)

    sa = a1 * 100 + a2 * 10

    s1 = a1 * 100 + (a2 - 1) * 10 + 1
    s2 = a1 * 100 + (a2 - 1) * 10 + 2
    s3 = a1 * 100 + (a2 - 1) * 10 + 3
    s9 = a1 * 100 + (a2 - 1) * 10 + 9
    s10 = a1 * 100 + (a2 - 1) * 10 + 10

    ss = 10

    pj = proc_jo(sa, 0)


    stem = stem.format(sa=sa, pj=pj)
    answer = answer.format(ss=ss)
    comment = comment.format(sa=sa, s1=s1, s2=s2, s3=s3, s9=s9, s10=s10, ss=ss)

    return stem, answer, comment





















































# 5-2-1-41
def ranandrou521_Stem_020():
    stem = "올림하여 십의 자리까지 나타낸 수가 가장 작은 수를 찾아 써 보세요.\n$$표$$$$수식$${t1}$$/수식$$    $$수식$${t2}$$/수식$$    $$수식$${t3}$$/수식$$    $$수식$${t4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${t1}$$/수식$$ → $$수식$${ts1}$$/수식$$, $$수식$${t2}$$/수식$$ → $$수식$${ts2}$$/수식$$, $$수식$${t3}$$/수식$$ → $$수식$${ts3}$$/수식$$, $$수식$${t4}$$/수식$$ → $$수식$${ts4}$$/수식$$\n" \
              "따라서 올림하여 십의 자리까지 나타낸 수가 가장 작은 수는 $$수식$${ss}$$/수식$$입니다.\n\n"


    a1 = np.random.randint(1, 10)
    a2 = np.random.randint(1, 9)
    a3 = 0
    a4 = np.random.randint(1, 10)
    sa = a1 * 1000 + a2 * 100 + a3 * 10 + a4

    b1 = a1
    b2 = a2 - 1
    b3 = np.random.randint(3, 5)
    b4 = 0
    sb = b1 * 1000 + b2 * 100 + b3 * 10 + b4

    c1 = a1
    c2 = a2 - 1
    c3 = b3 - 2
    c4 = np.random.randint(1, 10)
    sc = c1 * 1000 + c2 * 100 + c3 * 10 + c4

    d1 = a1
    d2 = a2 - 1
    d3 = b3 - 1
    d4 = np.random.randint(1, 10)
    sd = d1 * 1000 + d2 * 100 + d3 * 10 + d4

    s1 = a1 * 1000 + a2 * 100 + (a3 + 1) * 10
    s2 = b1 * 1000 + b2 * 100 + b3 * 10
    s3 = c1 * 1000 + c2 * 100 + (c3 + 1) * 10
    s4 = d1 * 1000 + d2 * 100 + (d3 + 1) * 10

    ss = sc

    candidates1 = [sa, sb, sc, sd]
    candidates2 = [s1, s2, s3, s4]

    combine = list(zip(candidates1, candidates2))
    np.random.shuffle(combine)
    [t1, t2, t3, t4], [ts1, ts2, ts3, ts4] = zip(*combine)


    stem = stem.format(t1=t1, t2=t2, t3=t3, t4=t4)
    answer = answer.format(ss=ss)
    comment = comment.format(t1=t1, t2=t2, t3=t3, t4=t4, ts1=ts1, ts2=ts2, ts3=ts3, ts4=ts4, ss=ss)

    return stem, answer, comment





















































# 5-2-1-42
def ranandrou521_Stem_021():
    stem = "{n1}의 자전거 자물쇠의 비밀번호를 올림하여 백의 자리까지 나타내면 $$수식$${sa}00$$/수식$$입니다. 자전거 자물쇠의 비밀번호를 구해 보세요.\n$$표$$$$수식$$LEFT [$$/수식$${n1}$$수식$$RIGHT ]$$/수식$$ 내 자전거 자물쇠의 비밀번호는  $$수식$$□$$/수식$$$$수식$$□$$/수식$$$$수식$${sb}$$/수식$$이야.$$/표$$\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$\n"
    comment = "(해설)\n" \
              "자전거 자물쇠의 비밀번호는 □□$$수식$${sb}$$/수식$$이고 올림하여 백의 자리까지 나타내면 $$수식$${sa}00$$/수식$$이 되므로 올림하기 전의 수는 $$수식$${s1}$$/수식$$■■입니다.\n" \
              "따라서 자전거 자물쇠의 비밀번호는 $$수식$${ss}$$/수식$$입니다.\n\n"


    n1 = ["선우", "희주", "현아", "수호", "정수", "숭태", "선규", "민지"][np.random.randint(0, 8)]

    a1 = np.random.randint(1, 10)
    a2 = np.random.randint(1, 10)
    a3 = np.random.randint(1, 10)
    a4 = np.random.randint(1, 9)
    sa = a1 * 10 + a2
    sb = a3 * 10 + a4

    s1 = sa - 1
    ss = s1 * 100 + sb


    stem = stem.format(sa=sa, sb=sb, n1=n1)
    answer = answer.format(ss=ss)
    comment = comment.format(sa=sa, sb=sb, s1=s1, ss=ss)

    return stem, answer, comment






















































# 5-2-1-43
def ranandrou521_Stem_022():
    stem = "어떤 수를 올림하여 십의 자리까지 나타냈더니 $$수식$${sa}$$/수식$${pj} 되었습니다. 어떤 수가 될 수 있는 자연수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$개\n"
    comment = "(해설)\n" \
              "올림하여 십의 자리까지 나타내면 $$수식$${sa}$$/수식$${pj} 되는 수는 자연수는 $$수식$${s1}$$/수식$$부터 $$수식$${s2}$$/수식$$까지의 자연수입니다.\n" \
              "따라서 어떤 수가 될 수 있는 수는 모두 $$수식$${ss}$$/수식$$개입니다.\n\n"


    a1 = np.random.randint(1, 10)

    sa = a1 * 10

    s1 = sa - 9
    s2 = sa

    ss = 10

    pj = proc_jo(sa, 0)


    stem = stem.format(sa=sa, pj=pj)
    answer = answer.format(ss=ss)
    comment = comment.format(sa=sa, s1=s1, s2=s2, ss=ss, pj=pj)

    return stem, answer, comment























































# 5-2-1-44
def ranandrou521_Stem_023():
    stem = "$$수식$${sa}$$/수식$${pj} 올림하여 백의 자리까지 나타낸 수와 올림하여 천의 자리까지 나타낸 수의 차는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$${pj} 올림하여 백의 자리까지 나타낸 수는 $$수식$${s1}$$/수식$$이고, " \
              "$$수식$${sa}$$/수식$${pj} 올림하여 천의 자리까지 나타낸 수는 $$수식$${s2}$$/수식$$입니다.\n" \
              "따라서 두 수의 차는 $$수식$${s2}`-`{s1}`=`{ss}$$/수식$$입니다.\n\n"


    a1 = np.random.randint(1, 9)
    a2 = np.random.randint(1, 10)
    a3 = np.random.randint(1, 10)
    a4 = np.random.randint(1, 10)

    sa = a1 * 1000 + a2 * 100 + a3 * 10 + a4

    s1 = a1 * 1000 + (a2 + 1) * 100
    s2 = (a1 + 1) * 1000
    ss = s2 - s1

    pj = proc_jo(a4, 3)


    stem = stem.format(sa=sa, pj=pj)
    answer = answer.format(ss=ss)
    comment = comment.format(sa=sa, s1=s1, s2=s2, ss=ss, pj=pj)

    return stem, answer, comment






















































# 5-2-1-45
def ranandrou521_Stem_024():
    stem = "다음 수를 올림하여 천의 자리까지 나타내면 $$수식$${sa}$$/수식$$입니다. □ 안에 들어갈 수 있는 수는 모두 몇 개인가요?\n$$표$$$$수식$${sb}□{sc}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$개\n"
    comment = "(해설) \n" \
              "올림하여 천의 자리까지 나타내면 $$수식$${sa}$$/수식$${pj} 되는 수는 자연수는 $$수식$${s1}$$/수식$$부터 $$수식$${s2}$$/수식$$까지의 자연수입니다.\n" \
              "따라서 □ 안에 들어갈 수 있는 수는 $$수식$${ss1}$$/수식$$, $$수식$${ss2}$$/수식$$, $$수식$${s3}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$, $$수식$${s9}$$/수식$$, $$수식$${s10}$$/수식$$로 " \
              "모두 $$수식$${ss}$$/수식$$개입니다.\n\n"


    a1 = np.random.randint(1, 10)
    a2 = np.random.randint(1, 10)
    a3 = np.random.randint(1, 10)
    a4 = np.random.randint(1, 10)

    sa = a1 * 10000 + a2 * 1000
    sb = a1 * 10 + (a2 - 1) * 1
    sc = a3 * 10 + a4 * 1

    s1 = a1 * 10000 + (a2 - 1) * 1000 + 1
    s2 = sa
    ss1 = 0
    ss2 = 1
    s3 = 2
    s9 = 8
    s10 = 9
    ss = 10

    pj = proc_jo(sa, 0)


    stem = stem.format(sa=sa, sb=sb, sc=sc)
    answer = answer.format(ss=ss)
    comment = comment.format(sa=sa, s1=s1, s2=s2, ss=ss, pj=pj, ss1=ss1, ss2=ss2, s3=s3, s9=s9, s10=s10)

    return stem, answer, comment





















































# 5-2-1-46
def ranandrou521_Stem_025():
    stem = "$$수식$${sa}$$/수식$${pj} 버림하여 소수 첫째 자리까지 나타내면 얼마인가요?\n"
    answer = "(정답)\n$$수식$${s2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$ → $$수식$${s1}0$$/수식$$ → $$수식$${s2}$$/수식$$\n\n"


    a1 = np.random.randint(1, 9)
    a2 = np.random.randint(1, 10)
    a3 = np.random.randint(1, 10)
    a4 = np.random.randint(1, 10)

    sa = round(a1 + a2 * 0.1 + a3 * 0.01 + a4 * 0.001, 3)
    s1 = round(a1 + a2 * 0.1, 2)
    s2 = round(a1 + a2 * 0.1, 2)

    pj = proc_jo(a4, 3)


    stem = stem.format(sa=sa, pj=pj)
    answer = answer.format(s2=s2)
    comment = comment.format(sa=sa, s1=s1, s2=s2, pj=pj)

    return stem, answer, comment





















































# 5-2-1-47
def ranandrou521_Stem_026():
    stem = "어림한 후 어림한 수의 크기를 비교하여 □ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n{saying1}\n{saying2}\n$$수식$$㉠```{box}```㉡$$/수식$$"
    answer = "(정답)\n$$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${st}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$${pj1} 버림하여 백의 자리까지 나타낸 수는 $$수식$${sa}$$/수식$$ → $$수식$${s1}$$/수식$$입니다.\n" \
              "$$수식$${sb}$$/수식$${pj2} 버림하여 천의 자리까지 나타낸 수는 $$수식$${sb}$$/수식$$ → $$수식$${s2}$$/수식$$입니다.\n" \
              "따라서 $$수식$${s1} ` {st} ` {s2}$$/수식$$입니다.\n\n"


    while True:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(1, 10)
        a4 = np.random.randint(1, 10)
        b1 = a1
        b2 = np.random.randint(1, 10)
        b3 = np.random.randint(1, 10)
        b4 = np.random.randint(1, 10)

        if a1 != a2 != a3 != a4 and a2 < b2 and a3 != b3:
            break

    sa = a1 * 1000 + a2 * 100 + a3 * 10 + a4
    sb = b1 * 1000 + b2 * 100 + b3 * 10 + b4

    s1 = a1 * 1000 + a2 * 100
    s2 = b1 * 1000

    if s1 > s2:
        st = "&gt;"
    elif s1 < s2:
        st = "&lt;"
    elif s1 == s2:
        st = "="

    pj1 = proc_jo(sa, 3)
    pj2 = proc_jo(sb, 3)

    # box = "box{~~}"
    # box1 = "box{~~~~~}"
    # box2 = "box{~~~~~}"

    box = "□"
    box1 = "$$수식$$box{㉠``````````````````````````````}$$/수식$$"
    box2 = "$$수식$$box{㉡``````````````````````````````}$$/수식$$"


    saying1 = "$$수식$$[%s%s 버림하여 백의 자리까지 나타낸 수]$$/수식$$ → %s" % (sa, pj1, box1)
    saying2 = "$$수식$$[%s%s 버림하여 천의 자리까지 나타낸 수]$$/수식$$ → %s" % (sb, pj2, box2)


    stem = stem.format(sa=sa, sb=sb, pj1=pj1, pj2=pj2, box=box, box1=box1, box2=box2, saying1=saying1, saying2=saying2)
    answer = answer.format(s1=s1, s2=s2, st=st)
    comment = comment.format(sa=sa, sb=sb, pj1=pj1, pj2=pj2, s1=s1, s2=s2, st=st)

    return stem, answer, comment





















































# 5-2-1-48
def ranandrou521_Stem_027():
    stem = "다음 중 버림하여 십의 자리까지 나타낸 수가 가장 큰 것은 어느 것인가요?\n① $$수식$${x1}$$/수식$$    ② $$수식$${x2}$$/수식$$    ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$    ⑤ $$수식$${x5}$$/수식$$\n"
    answer = "(정답)\n{st}\n"
    comment = "(해설)\n" \
              "버림하여 십의 자리까지 나타내면\n" \
              "① $$수식$${y1}$$/수식$$    ② $$수식$${y2}$$/수식$$    ③ $$수식$${y3}$$/수식$$\n" \
              "④ $$수식$${y4}$$/수식$$    ⑤ $$수식$${y5}$$/수식$$\n" \
              "입니다.\n" \
              "따라서 어림한 수가 가장 큰 것은 {st}입니다.\n\n"


    while True:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(0, 10)
        a3 = np.random.randint(0, 10)
        a4 = np.random.randint(0, 10)
        b2 = np.random.randint(0, 10)
        c2 = np.random.randint(0, 10)
        d2 = np.random.randint(0, 10)
        e2 = np.random.randint(0, 10)

        if a1 != a2 and a1 != a3 and a1 != a4 and a2 != a3 and a2 != a4 and a3 != a4:
            if a2 < b2 and b2 < c2 and c2 < d2 and d2 < e2:
                break

    b1 = a1
    b3 = np.random.randint(0, 10)
    b4 = np.random.randint(0, 10)

    c1 = b1
    c3 = np.random.randint(0, 10)
    c4 = np.random.randint(0, 10)

    d1 = c1
    d3 = np.random.randint(0, 10)
    d4 = np.random.randint(0, 10)

    e1 = d1
    e3 = np.random.randint(0, 10)
    e4 = np.random.randint(0, 10)

    sa = a1 * 1000 + a2 * 100 + a3 * 10 + a4
    sb = b1 * 1000 + b2 * 100 + b3 * 10 + b4
    sc = c1 * 1000 + c2 * 100 + c3 * 10 + c4
    sd = d1 * 1000 + d2 * 100 + d3 * 10 + d4
    se = e1 * 1000 + e2 * 100 + e3 * 10 + e4

    sa_borim = a1 * 1000 + a2 * 100 + a3 * 10
    sb_borim = b1 * 1000 + b2 * 100 + b3 * 10
    sc_borim = c1 * 1000 + c2 * 100 + c3 * 10
    sd_borim = d1 * 1000 + d2 * 100 + d3 * 10
    se_borim = e1 * 1000 + e2 * 100 + e3 * 10


    # candidates = [sa, sb, sc, sd, se]
    # np.random.shuffle(candidates)
    # [x1, x2, x3, x4, x5] = candidates

    # correct_idx = 0
    # for idx, sdx in enumerate(candidates):
    #     if sdx == se:
    #         correct_idx = idx
    #         break

    candidates = [[sa, sa_borim], [sb, sb_borim], [sc, sc_borim], [sd, sd_borim], [se, se_borim]]
    np.random.shuffle(candidates)
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4], [x5, y5]] = candidates

    correct_idx = 0
    for i_dx, s_dx in enumerate(candidates):
        if s_dx == [se, se_borim]:
            correct_idx = i_dx
            break

    st = answer_dict[correct_idx]


    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(st=st)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, st=st, y1=y1, y2=y2, y3=y3, y4=y4, y5=y5)

    return stem, answer, comment






















































# 5-2-1-49
def ranandrou521_Stem_028():
    stem = "버림하여 십의 자리까지 나타내면 $$수식$${sa}$$/수식$${pj} 되는 자연수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$개\n"
    comment = "(해설) \n" \
              "$$수식$${sb}$$/수식$$□ → □의 자리에 $$수식$$0$$/수식$$부터 $$수식$$9$$/수식$$까지 들어간 수를 버림하여 십의 자리까지 나타내면 $$수식$${sa}$$/수식$${pj} 됩니다.\n" \
              "구하는 수는 $$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$, $$수식$${s9}$$/수식$$, $$수식$${s10}$$/수식$$이므로 $$수식$${ss}$$/수식$$개입니다.\n\n"


    while True:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(1, 10)
        if a1 != a2:
            break

    a3 = 0

    sa = a1 * 100 + a2 * 10 + a3
    sb = a1 * 10 + a2

    s1 = sa
    s2 = sa + 1
    s3 = sa + 2
    s9 = sa + 8
    s10 = sa + 9

    ss = 10

    pj = proc_jo(sa, 0)


    stem = stem.format(sa=sa, pj=pj)
    answer = answer.format(ss=ss)
    comment = comment.format(sa=sa, sb=sb, s1=s1, s2=s2, s3=s3, s9=s9, s10=s10, ss=ss, pj=pj)

    return stem, answer, comment





















































# 5-2-1-50
def ranandrou521_Stem_029():
    stem = "버림하여 십의 자리까지 나타내면 $$수식$${sa}$$/수식$${pj} 되는 자연수 중에서 가장 큰 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$\n"
    comment = "(해설)\n" \
              "버림하여 십의 자리까지 나타내면 $$수식$${sa}$$/수식$${pj} 되는 자연수는 " \
              "$$수식$${s1}$$/수식$$부터 $$수식$${s2}$$/수식$$까지의 자연수입니다.\n" \
              "따라서 가장 큰 수는 $$수식$${ss}$$/수식$$입니다.\n\n"


    while True:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(1, 10)
        if a1 != a2:
            break

    a3 = 0

    sa = a1 * 100 + a2 * 10 + a3

    s1 = sa
    s2 = sa + 9

    ss = s2

    pj = proc_jo(sa, 0)


    stem = stem.format(sa=sa, pj=pj)
    answer = answer.format(ss=ss)
    comment = comment.format(sa=sa, s1=s1, s2=s2, ss=ss, pj=pj)

    return stem, answer, comment






















































# 5-2-1-51
def ranandrou521_Stem_030():
    stem = "어떤 자연수에 $$수식$${sa}$$/수식$${pj1} 곱해서 나온 수를 버림하여 십의 자리까지 나타내면 $$수식$${sb}$$/수식$$입니다. 어떤 자연수를 모두 구해 보세요.\n"
    answer = "(정답)\n$$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$$\n"
    comment = "(해설)\n" \
              "버림하여 십의 자리까지 나타내면 $$수식$${sb}$$/수식$${pj2} 되는 수는 자연수는 $$수식$${u1}$$/수식$$부터 $$수식$${u2}$$/수식$$까지입니다.\n" \
              "이 중에서 $$수식$${sa}$$/수식$$의 배수는 $$수식$${x1}$$/수식$$, $$수식$${x2}$$/수식$$, $$수식$${x3}$$/수식$$입니다.\n" \
              "따라서 어떤 자연수는 $$수식$${x1} ` DIV ` {sa} ` = ` {s1}$$/수식$$, $$수식$${x2} ` DIV ` {sa} ` = ` {s2}$$/수식$$, $$수식$${x3} ` DIV ` {sa} ` = ` {s3}$$/수식$$입니다.\n\n"


    sa = 3
    sb = [40, 50, 70, 80][np.random.randint(0, 4)]
    u1 = sb
    u2 = sb + 9
    s1 = int(sb // sa) + 1
    s2 = s1 + 1
    s3 = s1 + 2
    x1 = s1 * sa
    x2 = s2 * sa
    x3 = s3 * sa

    pj1 = proc_jo(sa, 3)
    pj2 = proc_jo(sb, 0)


    stem = stem.format(sa=sa, sb=sb, pj1=pj1)
    answer = answer.format(s1=s1, s2=s2, s3=s3)
    comment = comment.format(sa=sa, sb=sb, pj2=pj2, s1=s1, s2=s2, s3=s3, x1=x1, x2=x2, x3=x3, u1=u1, u2=u2)

    return stem, answer, comment




















































# 5-2-1-52
def ranandrou521_Stem_031():
    stem = "버림하여 백의 자리까지 나타내었을 때 서로 같은 수를 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${t1}$$/수식$$    ㉡ $$수식$${t2}$$/수식$$    ㉢ $$수식$${t3}$$/수식$$    ㉣ $$수식$${t4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{a1}, {a2}\n"
    comment = "(해설)\n" \
              "버림하여 백의 자리까지 나타내면\n" \
              "㉠ $$수식$${ts1}$$/수식$$    ㉡ $$수식$${ts2}$$/수식$$    ㉢ $$수식$${ts3}$$/수식$$    ㉣ $$수식$${ts4}$$/수식$$\n" \
              "입니다.\n" \
              "따라서 서로 같은 수를 찾아 기호를 쓰면 {a1}, {a2}입니다.\n\n"


    while True:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(0, 10)
        a3 = np.random.randint(0, 10)
        a4 = np.random.randint(0, 10)
        sa = a1 * 1000 + a2 * 100 + a3 * 10 + a4
        s1 = a1 * 1000 + a2 * 100
        b1 = a1
        b2 = np.random.randint(0, 10)
        b3 = np.random.randint(0, 10)
        b4 = np.random.randint(0, 10)
        sb = b1 * 1000 + b2 * 100 + b3 * 10 + b4
        s2 = b1 * 1000 + b2 * 100
        c1 = b1
        c2 = np.random.randint(0, 10)
        c3 = np.random.randint(0, 10)
        c4 = np.random.randint(0, 10)
        sc = c1 * 1000 + c2 * 100 + c3 * 10 + c4
        s3 = c1 * 1000 + c2 * 100
        d1 = c1
        d2 = np.random.randint(0, 10)
        d3 = np.random.randint(0, 10)
        d4 = np.random.randint(0, 10)
        sd = d1 * 1000 + d2 * 100 + d3 * 10 + d4
        s4 = d1 * 1000 + d2 * 100

        if a1 != a2 != a3 != a4 and a2 < b2 and b2 < c2 and a2 < d3 and a2 == d2 and a3 != d3 and a4 != d4:
            break

    candidates1 = [sa, sb, sc, sd]
    candidates2 = [s1, s2, s3, s4]

    combine = list(zip(candidates1, candidates2))
    np.random.shuffle(combine)
    [t1, t2, t3, t4], [ts1, ts2, ts3, ts4] = zip(*combine)
    alist = [t1, t2, t3, t4]

    correct_idx1 = 0
    correct_idx2 = 0

    for idx, sdx in enumerate(alist):
        if sdx == sa:
            correct_idx1 = idx
            break

    for idx, sdx in enumerate(alist):
        if sdx == sd:
            correct_idx2 = idx
            break

    if correct_idx1 > correct_idx2:
        correct_idx1, correct_idx2 = correct_idx2, correct_idx1

    a1 = answer_dict2[correct_idx1]
    a2 = answer_dict2[correct_idx2]

    # if correct_idx1 > correct_idx2:
    #     a1, a2 = a2, a1


    stem = stem.format(t1=t1, t2=t2, t3=t3, t4=t4)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(t1=t1, t2=t2, t3=t3, t4=t4, ts1=ts1, ts2=ts2, ts3=ts3, ts4=ts4,
                             a1=answer_dict2[correct_idx1], a2=answer_dict2[correct_idx2])

    return stem, answer, comment


























































# 5-2-1-53
def ranandrou521_Stem_032():
    stem = "다음을 만족하는 자연수의 범위를 이상과 이하를 이용하여 나타내어 보세요.\n$$표$$버림하여 천의 자리까지 나타내면 $$수식$${sa}$$/수식$$이 됩니다.$$/표$$\n$$수식$${box1}$$/수식$$ 이상 $$수식$${box2}$$/수식$$ 이하입니다.\n"
    answer = "(정답)\n$$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$\n"
    comment = "(해설)\n" \
              "버림하여 십의 자리까지 나타내면 $$수식$${sa}$$/수식$$이 되는 수는 자연수는 $$수식$${s1}$$/수식$$부터 $$수식$${s2}$$/수식$$까지의 자연수입니다.\n" \
              "따라서 $$수식$${s1}$$/수식$$ 이상 $$수식$${s2}$$/수식$$ 이하입니다.\n\n"


    a1 = np.random.randint(1, 10)

    sa = a1 * 1000

    s1 = sa
    s2 = sa + 999

    box1 = "box{㉠````````````````````}"
    box2 = "box{㉡````````````````````}"


    stem = stem.format(sa=sa, box1=box1, box2=box2)
    answer = answer.format(s1=s1, s2=s2)
    comment = comment.format(sa=sa, s1=s1, s2=s2)

    return stem, answer, comment





















































# 5-2-1-54
def ranandrou521_Stem_033():
    stem = "{n1}가 처음에 생각한 자연수는 무엇인가요?\n$$표$$$$수식$$LEFT [$$/수식$${n2}$$수식$$RIGHT ]$$/수식$$ 네가 생각한 자연수에 $$수식$${sa}$$/수식$${pj1} 곱해서 나온 수를 버림하여 십의 자리까지 나타내 봐. 얼마야?\n$$수식$$LEFT [$$/수식$${n1}$$수식$$RIGHT ]$$/수식$$ $$수식$${sb}$$/수식$$이야!$$/표$$\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$\n"
    comment = "(해설)\n" \
              "버림하여 십의 자리까지 나타내면 $$수식$${sb}$$/수식$${pj2} 되는 수는 자연수는 $$수식$${s1}$$/수식$$부터 $$수식$${s2}$$/수식$$까지의 자연수입니다.\n" \
              "{n1}가 생각하는 자연수에 $$수식$${sa}$$/수식$${pj1} 곱해 나온 수이므로 이 중에서 $$수식$${sa}$$/수식$$의 배수를 찾으면 $$수식$${x1}$$/수식$$입니다.\n" \
              "따라서 {n1}가 처음에 생각한 자연수는 $$수식$${x1} ` div ` {sa} ` = ` {ss}$$/수식$$입니다.\n\n"


    n1 = ["민호", "성희", "우수", "선호", "혁수"][np.random.randint(0, 5)]
    n2 = ["형수", "정희", "영수", "재희", "정우"][np.random.randint(0, 5)]

    sa = [6, 7, 8, 9][np.random.randint(0, 4)]

    if sa == 6:
        sb = [20, 50][np.random.randint(0, 2)]
    elif sa == 7:
        sb = [30, 50, 60][np.random.randint(0, 3)]
    elif sa == 8:
        sb = [30, 50, 60][np.random.randint(0, 3)]
    elif sa == 9:
        sb = [30, 40, 50, 60, 70, 80][np.random.randint(0, 6)]

    if sa == 6 and sb == 20:
        x1 = 24
    elif sa == 6 and sb == 50:
        x1 = 54
    elif sa == 7 and sb == 30:
        x1 = 35
    elif sa == 7 and sb == 50:
        x1 = 56
    elif sa == 7 and sb == 60:
        x1 = 63
    elif sa == 8 and sb == 30:
        x1 = 24
    elif sa == 8 and sb == 50:
        x1 = 56
    elif sa == 8 and sb == 60:
        x1 = 64
    elif sa == 9 and sb == 30:
        x1 = 36
    elif sa == 9 and sb == 40:
        x1 = 45
    elif sa == 9 and sb == 50:
        x1 = 54
    elif sa == 9 and sb == 60:
        x1 = 63
    elif sa == 9 and sb == 70:
        x1 = 72
    elif sa == 9 and sb == 80:
        x1 = 81

    s1 = sb
    s2 = sb + 9

    pj1 = proc_jo(sa, 3)
    pj2 = proc_jo(sb, 0)

    ss = int(x1 / sa)


    stem = stem.format(n1=n1, n2=n2, sa=sa, sb=sb, pj1=pj1)
    answer = answer.format(ss=ss)
    comment = comment.format(n1=n1, pj2=pj2, sa=sa, sb=sb, pj1=pj1, ss=ss, s1=s1, s2=s2, x1=x1)

    return stem, answer, comment



























































# 5-2-1-55
def ranandrou521_Stem_034():
    stem = "$$수식$${sa}$$/수식$${pj} 반올림하여 소수 첫째 자리까지 나타내면 얼마인가요?\n"
    answer = "(정답)\n$$수식$${s2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$ → $$수식$${s1} ` = ` {s2}$$/수식$$\n\n"


    while True:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(1, 10)
        a4 = np.random.randint(1, 10)

        if a1 != a2 != a3 != a4:
            break

    sa = round(a1 + a2 * 0.1 + a3 * 0.01 + a4 * 0.001, 3)

    if a3 < 5:
        s1 = round(a1 + a2 * 0.1, 3)
        s2 = round(a1 + a2 * 0.1, 1)
    else:
        s1 = round(a1 + (a2 + 1) * 0.1 + 0.000, 3)
        s2 = round(a1 + (a2 + 1) * 0.1, 1)

    s1 = '%.3f' % s1
    pj = proc_jo(a4, 3)


    stem = stem.format(sa=sa, pj=pj)
    answer = answer.format(s2=s2)
    comment = comment.format(sa=sa, s1=s1, s2=s2, pj=pj)

    return stem, answer, comment




















































# 5-2-1-57
def ranandrou521_Stem_035():
    stem = "반올림하여 백의 자리까지 나타내면 $$수식$${sa}$$/수식$$이 되는 자연수 중에서 가장 작은 수와 가장 큰 수를 각각 구해 보세요.\n" \
        "가장 작은 수 : {boxblank}, 가장 큰 수 : {boxblank}"
    
    answer = "(정답)\n$$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$\n"
    comment = "(해설)\n" \
              "반올림하여 백의 자리까지 나타내면 $$수식$${sa}$$/수식$$이 되는 자연수는 $$수식$${s1}$$/수식$$부터 $$수식$${s2}$$/수식$$까지의 자연수입니다.\n" \
              "이 중에서 가장 작은 수는 $$수식$${s1}$$/수식$$, 가장 큰 수는 $$수식$${s2}$$/수식$$입니다.\n\n"

    boxblank = "$$수식$$BOX{　　　}$$/수식$$"
    
    sa = [100, 200, 300, 400, 500, 600, 700, 800, 900][np.random.randint(0, 9)]
    s1 = sa - 50
    s2 = sa + 49


    stem = stem.format(sa=sa, boxblank=boxblank)
    answer = answer.format(s1=s1, s2=s2)
    comment = comment.format(sa=sa, s1=s1, s2=s2)

    return stem, answer, comment

























































# 5-2-1-58
def ranandrou521_Stem_036():
    stem = "반올림하여 천의 자리까지 나타낸 수가 다른 하나를 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${t1}$$/수식$$     ㉡ $$수식$${t2}$$/수식$$     ㉢ $$수식$${t3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{st}\n"
    comment = "(해설)\n" \
              "반올림하여 천의 자리까지 각각 나타내면\n" \
              "㉠ $$수식$${t1}$$/수식$$ → $$수식$${ts1}$$/수식$$, " \
              "㉡ $$수식$${t2}$$/수식$$ → $$수식$${ts2}$$/수식$$, " \
              "㉢ $$수식$${t3}$$/수식$$ → $$수식$${ts3}$$/수식$$입니다.\n" \
              "따라서 반올림하여 천의 자리까지 나타낸 수가 다른 하나는 {st}입니다.\n\n"



    while True:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(1, 9)
        a3 = np.random.randint(5, 10)
        a4 = np.random.randint(1, 10)
        a5 = np.random.randint(1, 10)
        b1 = a1
        b2 = a2 + 1
        b3 = np.random.randint(1, 5)
        b4 = np.random.randint(1, 10)
        b5 = np.random.randint(1, 10)
        c1 = a1
        c2 = a2
        c3 = np.random.randint(1, 5)
        c4 = np.random.randint(1, 10)
        c5 = 0
        if a1 != a2 != a3 != a4 != a5 and b1 != b2 != b3 != b4 != b5 and c1 != c2 != c3 != c4:
            break

    sa = a1 * 10000 + a2 * 1000 + a3 * 100 + a4 * 10 + a5

    if a3 < 5:
        s1 = a1 * 10000 + a2 * 1000
    else:
        s1 = a1 * 10000 + (a2 + 1) * 1000

    sb = b1 * 10000 + b2 * 1000 + b3 * 100 + b4 * 10 + b5

    if b3 < 5:
        s2 = b1 * 10000 + b2 * 1000
    else:
        s2 = b1 * 10000 + (b2 + 1) * 1000

    sc = c1 * 10000 + c2 * 1000 + c3 * 100 + c4 * 10 + c5

    if c3 < 5:
        s3 = c1 * 10000 + c2 * 1000
    else:
        s3 = c1 * 10000 + (c2 + 1) * 1000

    candidates1 = [sa, sb, sc]
    candidates2 = [s1, s2, s3]

    combine = list(zip(candidates1, candidates2))
    np.random.shuffle(combine)
    [t1, t2, t3], [ts1, ts2, ts3] = zip(*combine)
    alist = [t1, t2, t3]

    correct_idx = 0
    for idx, sdx in enumerate(alist):
        if sdx == sc:
            correct_idx = idx
            break


    stem = stem.format(sa=sa, t1=t1, t2=t2, t3=t3)
    answer = answer.format(st=answer_dict2[correct_idx])
    comment = comment.format(t1=t1, t2=t2, t3=t3, ts1=ts1, ts2=ts2, ts3=ts3, sa=sa, st=answer_dict2[correct_idx])

    return stem, answer, comment























































# 5-2-1-59
def ranandrou521_Stem_037():
    stem = "반올림하여 천의 자리까지 나타내면 $$수식$${ss}$$/수식$$이 되는 수가 아닌 것은 어느 것인가요??\n① $$수식$${t1}$$/수식$$    ② $$수식$${t2}$$/수식$$    ③ $$수식$${t3}$$/수식$$\n④ $$수식$${t4}$$/수식$$    ⑤ $$수식$${t5}$$/수식$$\n"
    answer = "(정답)\n{st}\n"
    comment = "(해설) \n" \
              "반올림하여 천의 자리까지 각각 나타내면\n" \
              "① $$수식$${t1}$$/수식$$ → $$수식$${ts1}$$/수식$$,   ② $$수식$${t2}$$/수식$$ → $$수식$${ts2}$$/수식$$,\n" \
              "③ $$수식$${t3}$$/수식$$ → $$수식$${ts3}$$/수식$$,   ④ $$수식$${t4}$$/수식$$ → $$수식$${ts4}$$/수식$$,\n" \
              "⑤ $$수식$${t5}$$/수식$$ → $$수식$${ts5}$$/수식$$입니다.\n" \
              "따라서 반올림하여 천의 자리까지 나타내면 $$수식$${ss}$$/수식$$이 되는 수가 아닌 것은 {st}입니다.\n\n"


    while True:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(5, 7)
        a3 = np.random.randint(1, 10)
        a4 = 0
        if a1 != a2 != a3:
            break

    sa = a1 * 1000 + a2 * 100 + a3 * 10 + a4

    b1 = a1
    b2 = a2 + 1
    b3 = np.random.randint(1, 10)
    b4 = 0
    sb = b1 * 1000 + b2 * 100 + b3 * 10 + b4

    c1 = a1
    c2 = b2 + 2
    c3 = np.random.randint(1, 10)
    c4 = 0
    sc = c1 * 1000 + c2 * 100 + c3 * 10 + c4

    d1 = a1 + 1
    # d2 = np.random.randint(1, 10)
    d2 = np.random.randint(1, 5)
    d3 = np.random.randint(1, 10)
    d4 = 0
    sd = d1 * 1000 + d2 * 100 + d3 * 10 + d4

    e1 = a1 + 1
    e2 = np.random.randint(5, 10)
    e3 = np.random.randint(1, 10)
    e4 = 0
    se = e1 * 1000 + e2 * 100 + e3 * 10 + e4

    s1 = (a1 + 1) * 1000
    s2 = (b1 + 1) * 1000
    s3 = (c1 + 1) * 1000
    s4 = d1 * 1000
    s5 = (e1 + 1) * 1000
    # ss = s5
    ss = s4

    candidates1 = [sa, sb, sc, sd, se]
    candidates2 = [s1, s2, s3, s4, s5]

    combine = list(zip(candidates1, candidates2))
    np.random.shuffle(combine)
    [t1, t2, t3, t4, t5], [ts1, ts2, ts3, ts4, ts5] = zip(*combine)
    alist = [t1, t2, t3, t4, t5]

    correct_idx = 0
    for idx, sdx in enumerate(alist):
        if sdx == se:
            correct_idx = idx
            break


    stem = stem.format(ss=ss, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5)
    answer = answer.format(st=answer_dict[correct_idx])
    comment = comment.format(t1=t1, t2=t2, t3=t3, t4=t4, t5=t5, ts1=ts1, ts2=ts2, ts3=ts3, ts4=ts4, ts5=ts5,
                             st=answer_dict[correct_idx], ss=ss)

    return stem, answer, comment






















































# 5-2-1-60
def ranandrou521_Stem_038():
    stem = "수의 크기를 비교하여 $$수식$$□$$/수식$$ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${box1}$$/수식$$\n$$수식$${box2}$$/수식$$\n$$수식$$㉠````□````㉡$$/수식$$"
    answer = "(정답)\n$$수식$${st}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$ → $$수식$${s1}$$/수식$$ → $$수식$${s1} ` {st} ` {sb}$$/수식$$입니다.\n\n"


    while True:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(1, 10)
        a4 = np.random.randint(1, 10)
        if a1 != a2 != a3 != a4:
            break

    sa = round(a1 * 1 + a2 * 0.1 + a3 * 0.01 + a4 * 0.001, 3)

    b1 = a1
    b2 = a2
    b3 = a3
    sb = round(b1 * 1 + b2 * 0.1 + b3 * 0.01, 2)

    if a4 < 5:
        s1 = round(a1 * 1 + a2 * 0.1 + a3 * 0.01, 2)
        st = "="
    else:
        s1 = round(a1 * 1 + a2 * 0.1 + (a3 + 1) * 0.01, 2)
        st = "&gt;"

    pj1 = proc_jo(sa, 3)

    box = "□"
    box1 = "㉠[``%s%s```반올림하여```소수```둘째```자리까지```나타낸```수``]" % (sa, pj1)
    box2 = "㉡[``%.2f``]" % (sb)


    stem = stem.format(sa=sa, sb=sb, box=box, box1=box1, box2=box2)
    answer = answer.format(st=st)
    comment = comment.format(sa=sa, sb=sb, s1=s1, st=st)

    return stem, answer, comment





















































# 5-2-1-62
def ranandrou521_Stem_039():
    stem = "반올림하여 소수 둘째 자리까지 나타내면 $$수식$${sa}$$/수식$${ga1} 되는 소수 세 자리 수 중에서 가장 큰 수와 가장 작은 수의 합은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$\n"
    comment = "(해설)\n" \
              "반올림하여 소수 둘째 자리까지 나타내면 $$수식$${sa}$$/수식$${ga1} 되는 소수 세 자리 수는 " \
              "$$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$, $$수식$${s4}$$/수식$$, $$수식$${s5}$$/수식$$입니다.\n" \
              "이 중에서 가장 큰 수는 $$수식$${s5}$$/수식$$, 가장 작은 수는 $$수식$${s1}$$/수식$$이므로 두 수의 합은 $$수식$${s5} ` + ` {s1} ` = ` {ss}$$/수식$$입니다.\n\n"


    while True:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(1, 10)
        if a1 != a2 != a3:
            break

    sa = round(a1 * 1 + a2 * 0.1 + a3 * 0.01, 2)

    s1 = round(a1 * 1 + a2 * 0.1 + (a3 - 1) * 0.01 + 0.005, 3)
    s2 = round(a1 * 1 + a2 * 0.1 + (a3 - 1) * 0.01 + 0.006, 3)
    s3 = round(a1 * 1 + a2 * 0.1 + (a3 - 1) * 0.01 + 0.007, 3)
    s4 = round(a1 * 1 + a2 * 0.1 + a3 * 0.01 + 0.003, 3)
    s5 = round(a1 * 1 + a2 * 0.1 + a3 * 0.01 + 0.004, 3)

    ss = round(s1 + s5, 3)

    ga1 = proc_jo(a3, 0)


    stem = stem.format(sa=sa, ga1=ga1)
    answer = answer.format(ss=ss)
    comment = comment.format(sa=sa, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, ss=ss, ga1=ga1)

    return stem, answer, comment






















































# 5-2-1-63
def ranandrou521_Stem_040():
    stem = "{sn} $$수식$${sa}$$/수식$$개를 한 상자에 $$수식$${sb}$$/수식$$개씩 담아 팔려고 할 때 팔 수 있는 상자 수를 알아보려고 합니다. {sn}{rur1} 한 상자에 $$수식$${sb}$$/수식$$개씩 담아 팔면 최대 몇 상자까지 팔 수 있나요?\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$상자\n"
    comment = "(해설)\n" \
              "$$수식$${sa} ` div ` {sb} ` = ` {s1} ` CDOTS ` {s2}$$/수식$$\n" \
              "남은 $$수식$${s2}$$/수식$$개를 팔 수 없으므로 버림하면 최대 $$수식$${ss}$$/수식$$상자까지 팔 수 있습니다.\n\n"


    sn = ["감", "귤", "포도", "달걀", "딸기"][np.random.randint(0, 5)]

    while True:
        a1 = np.random.randint(5, 10)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(1, 10)
        if a1 != a2 != a3:
            break

    sa = a1 * 100 + a2 * 10 + a3
    sb = 10

    s1 = a1 * 10 + a2
    s2 = a3

    ss = s1

    rur1 = proc_jo(sn, 1)


    stem = stem.format(sn=sn, sa=sa, sb=sb, rur1=rur1)
    answer = answer.format(ss=ss)
    comment = comment.format(sn=sn, sa=sa, sb=sb, s1=s1, s2=s2, ss=ss)

    return stem, answer, comment























































# 5-2-1-65
def ranandrou521_Stem_041():
    stem = "$$수식$${sa}$$/수식$${pj} 어림했더니 $$수식$${sb}$$/수식$$이 되었습니다. 어떻게 어림했는지 $$수식$$LEFT [$$/수식$$보기$$수식$$RIGHT ]$$/수식$$의 어림 방법을 활용하여 설명한 것입니다. 옳지 않은 것을 찾아 기호를 써 보세요.\n$$표$$$$수식$$LEFT [$$/수식$$보기$$수식$$RIGHT ]$$/수식$$\n올림     버림     반올림$$/표$$\n$$표$$㉠ {x1}\n㉡ {x2}\n㉢ {x3}$$/표$$\n"
    answer = "(정답)\n{st}\n"
    comment = "(해설)\n" \
              "{st} $$수식$${sa}$$/수식$${pj} 올림하여 백의 자리까지 나타내면 $$수식$${sc}$$/수식$$입니다.\n\n"


    while True:
        a1 = np.random.randint(2, 10)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(1, 5)
        a4 = np.random.randint(1, 10)
        if a1 != a2 != a3 != a4:
            break

    sa = a1 * 1000 + a2 * 100 + a3 * 10 + a4
    sb = a1 * 1000 + a2 * 100
    sc = a1 * 1000 + (a2 + 1) * 100

    pj = proc_jo(a4, 3)

    x1 = "$$수식$$%d$$/수식$$%s 올림하여 백의 자리까지 나타낸 것입니다." % (sa, pj)
    x2 = "$$수식$$%d$$/수식$$%s 버림하여 백의 자리까지 나타낸 것입니다." % (sa, pj)
    x3 = "$$수식$$%d$$/수식$$%s 반올림하여 백의 자리까지 나타낸 것입니다." % (sa, pj)

    candidates = [x1, x2, x3]
    np.random.shuffle(candidates)

    correct_idx = 0
    for idx, sdx in enumerate(candidates):
        if sdx == x1:
            correct_idx = idx
            break

    [x1, x2, x3] = candidates


    stem = stem.format(x1=x1, x2=x2, x3=x3, sa=sa, sb=sb, pj=pj)
    answer = answer.format(st=answer_dict2[correct_idx])
    comment = comment.format(st=answer_dict2[correct_idx], sa=sa, sb=sb, pj=pj, sc=sc)

    return stem, answer, comment

























































# 5-2-1-66
def ranandrou521_Stem_042():
    stem = "철물점에서 {sn}{pj} $$수식$$1 `` rm m$$/수식$$ 단위로 판매한다고 합니다. 화단의 울타리를 묶는 데 $$수식$${sa} `` rm {{cm}}$$/수식$$의 {sn}{pj2} 필요하다면 {sn}{pj} 최소 몇 $$수식$$rm m$$/수식$$ 사야 하나요?\n"
    answer = "(정답)\n$$수식$${s2} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa} `` rm {{cm}} ` = ` {s1} `` m $$/수식$$\n" \
              "{sn}{pj} $$수식$$1 `` rm m$$/수식$$ 단위로 사야 하므로 $$수식$${s1}$$/수식$${rur1} 올림하여 일의 자리까지 나타내면\n" \
              "$$수식$${s1}$$/수식$$ → $$수식$${s2}$$/수식$$입니다.\n" \
              "따라서 {sn}{pj} 최소 $$수식$${s2} `` rm m$$/수식$$ 사야 합니다.\n\n"


    sn = ["철사", "노끈"][np.random.randint(0, 2)]

    if sn == "철사":
        pj = "를"
        pj2 = "가"
    elif sn == "노끈":
        pj = "을"
        pj2 = "이"

    while True:
        a1 = np.random.randint(1, 5)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(1, 10)
        a4 = np.random.randint(1, 10)
        if a1 != a2 != a3 != a4:
            break

    sa = a1 * 1000 + a2 * 100 + a3 * 10 + a4
    s1 = round(a1 * 10 + a2 * 1 + a3 * 0.1 + a4 * 0.01, 2)
    s2 = a1 * 10 + (a2 + 1)

    rur1 = proc_jo(a4, 1)


    stem = stem.format(sn=sn, sa=sa, pj=pj, pj2=pj2)
    answer = answer.format(s2=s2)
    comment = comment.format(sn=sn, sa=sa, s1=s1, s2=s2, pj=pj, rur1=rur1)

    return stem, answer, comment






















































# 5-2-1-67
def ranandrou521_Stem_043():
    stem = "운동회 때 학생 $$수식$${sa}$$/수식$$명에게 {sn}을 $$수식$${sb}$$/수식$$개씩 나누어 주려고 합니다. 마트에서 {sn}을 $$수식$${sc}$$/수식$$개씩 묶음으로 팔고 한 묶음에 $$수식$${sd}$$/수식$$원이라면 최소 몇 개를 사야 하며 얼마가 필요한가요?\n필요한 {sn}은 $$수식$${box1}$$/수식$$개이고 $$수식$${box2}$$/수식$$원이 있어야 합니다.\n"
    answer = "(정답)\n$$수식$${s2}$$/수식$$, $$수식$${ss}$$/수식$$\n"
    comment = "(해설)\n" \
              "필요한 {sn}은 모두 $$수식$${sa} ` times ` {sb} ` = ` {s1} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$입니다.\n" \
              "{sn}을 $$수식$${sc}$$/수식$$개씩 묶음으로만 사야 하므로 최소 $$수식$${s2}$$/수식$$개를 사야 합니다.\n" \
              "{sn}을 $$수식$${sc}$$/수식$$개씩 묶음을 사야 하므로 $$수식$${sd} ` times ` {s3} ` = ` {ss} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$이 필요합니다.\n\n"


    sn = ["빵", "사탕", "초콜릿"][np.random.randint(0, 2)]

    while True:
        a1 = np.random.randint(1, 5)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(1, 10)
        if a1 != a2 != a3:
            break

    sa = a1 * 100 + a2 * 10 + a3

    sb = 2
    sc = 10

    sd = [4000, 5000, 6000, 7000, 8000][np.random.randint(0, 5)]

    s1 = sa * sb
    s2 = int((s1 / 10) + 1) * 10
    s3 = int(s2 / 10)
    ss = sd * s3

    box1 = "box{%s````````````````````}"%"㉠"
    box2 = "box{%s````````````````````}"%"㉡"


    stem = stem.format(sn=sn, sa=sa, sb=sb, sc=sc, sd=sd, box1=box1, box2=box2)
    answer = answer.format(s2=s2, ss=ss)
    comment = comment.format(sn=sn, sa=sa, sb=sb, sc=sc, sd=sd, s1=s1, s2=s2, s3=s3, ss=ss)

    return stem, answer, comment

























































# 5-2-1-68
def ranandrou521_Stem_044():
    stem = "{sn}네 반 학생 $$수식$${sa}$$/수식$$명에게 공책을 $$수식$${sb}$$/수식$$권씩 나누어 주려고 합니다. 도매점에서 공책을 $$수식$${sc}$$/수식$$권씩 묶음으로 팔고 한 묶음에 $$수식$${sd}$$/수식$$원일 때, 공책을 사는데 필요한 돈은 최소 얼마인가요?\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$원\n"
    comment = "(해설)\n" \
              "{sn}네 반 학생 $$수식$${sa}$$/수식$$명이므로 $$수식$${sa} ` times ` {sb} ` = ` {s1} ` LEFT ($$/수식$$권$$수식$$RIGHT )$$/수식$$입니다.\n" \
              "$$수식$${s1} ` div ` {sc} ` = ` {s2} ` CDOTS ` {s3}$$/수식$$이므로 공책을 $$수식$${s2}$$/수식$$묶음 사면 $$수식$${s3}$$/수식$$권이 모자랍니다.\n" \
              "따라서 공책을 최소 $$수식$${s2} ` + ` 1 ` = ` {s4} ` LEFT ($$/수식$$묶음$$수식$$RIGHT )$$/수식$$ 사야 합니다.\n" \
              "$$수식$$LEFT ($$/수식$$공책을 사는 데 필요한 돈$$수식$$RIGHT ) ` = ` {sd} ` times ` {s4} ` = ` {ss} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$\n\n"


    sn = ["진수", "우주", "영서", "정호", "진희"][np.random.randint(0, 5)]

    while True:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(1, 10)

        sa = a1 * 10 + a2

        sb = np.random.randint(2, 6)
        sc = [20, 30, 40][np.random.randint(0, 3)]
        sd = [4000, 5000, 6000, 7000, 8000][np.random.randint(0, 5)]

        s1 = sa * sb
        s2 = int(s1 / sc)
        s3 = s1 - s2 * sc
        s4 = s2 + 1
        if s3 != 0:
            break

    ss = sd * s4


    stem = stem.format(sn=sn, sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(ss=ss)
    comment = comment.format(sn=sn, sa=sa, sb=sb, sc=sc, sd=sd, s1=s1, s2=s2, s3=s3, s4=s4, ss=ss)

    return stem, answer, comment





















































# 5-2-1-69
def ranandrou521_Stem_045():
    stem = "다음 조건을 만족하는 자연수는 모두 몇 개인가요?\n$$표$$올림하여 백의 자리까지 나타내면 $$수식$${sa}$$/수식$$입니다.\n버림하여 백의 자리까지 나타내면 $$수식$${sb}$$/수식$$입니다.\n반올림하여 백의 자리까지 나타내면 $$수식$${sa}$$/수식$$입니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$개\n"
    comment = "(해설)\n" \
              "올림하여 백의 자리까지 나타내면 $$수식$${sa}$$/수식$$이 되는 자연수: $$수식$${s1}$$/수식$$부터 $$수식$${s2}$$/수식$$까지\n" \
              "버림하여 백의 자리까지 나타내면 $$수식$${sb}$$/수식$$이 되는 자연수: $$수식$${s3}$$/수식$$부터 $$수식$${s4}$$/수식$$까지\n" \
              "반올림하여 백의 자리까지 나타내면 $$수식$${sa}$$/수식$$이 되는 자연수: $$수식$${s5}$$/수식$$부터 $$수식$${s6}$$/수식$$까지\n" \
              "공통인 자연수는 $$수식$${s7}$$/수식$$부터 $$수식$${s8}$$/수식$$까지이므로 $$수식$${x1}$$/수식$$, $$수식$${x2}$$/수식$$, $$수식$${x3}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$, $$수식$${x4}$$/수식$$입니다.\n" \
              "→ $$수식$${x4} ` - ` {x1} ` + ` 1 ` = ` {ss} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"


    a1 = np.random.randint(3, 10)
    a2 = 0
    a3 = 0

    sa = a1 * 100 + a2 + a3
    sb = sa - 100

    s1 = sa - 99
    s2 = sa
    s3 = sb
    s4 = sb + 99
    s5 = sa - 50
    s6 = sa + 49
    s7 = s5
    s8 = s4

    x1 = s5
    x2 = s5 + 1
    x3 = s5 + 2
    x4 = s4

    ss = x4 - x1 + 1


    stem = stem.format(sa=sa, sb=sb)
    answer = answer.format(ss=ss)
    comment = comment.format(sa=sa, sb=sb, ss=ss, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, s8=s8, x1=x1, x2=x2, x3=x3, x4=x4)

    return stem, answer, comment

















































# 5-2-1-70
def ranandrou521_Stem_046():
    stem = "{n1}네 모둠에서 {n2} $$수식$${sa}$$/수식$$개를 만들었습니다. 이 {n2}을 한 봉지에 $$수식$${sb}$$/수식$$개씩 담아 $$수식$${sc}$$/수식$$원에 팔려고 합니다. 봉지에 담은 {n2}을 판 돈은 최대 얼마인가요?\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$원\n"
    comment = "(해설)\n" \
              "$$수식$${sa} ` div ` {sb} ` = ` {s1} ` CDOTS ` {s2}$$/수식$$이므로 {n2}을 $$수식$${s1}$$/수식$$봉지에 담으면 $$수식$${s2}$$/수식$$개가 남습니다.\n" \
              "따라서 봉지에 담은 {n2}을 판 돈은 최대 $$수식$${s1} ` times ` {sc} ` = ` {ss} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    n1 = ["영지", "은희", "세호", "진수", "태우"][np.random.randint(0, 5)]
    n2 = ["빵", "사탕", "초콜릿"][np.random.randint(0, 2)]

    while True:
        a1 = np.random.randint(4, 10)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(1, 10)
        if a1 != a2 != a3:
            break

    sa = a1 * 100 + a2 * 10 + a3
    sb = [10, 20, 30, 40][np.random.randint(0, 4)]
    sc = [3000, 4000, 5000, 6000][np.random.randint(0, 4)]

    s1 = int(sa // sb)
    s2 = sa - sb * s1
    ss = s1 * sc

    stem = stem.format(n1=n1, n2=n2, sa=sa, sb=sb, sc=sc)
    answer = answer.format(ss=ss)
    comment = comment.format(n1=n1, n2=n2, sa=sa, sb=sb, sc=sc, s1=s1, s2=s2, ss=ss)

    return stem, answer, comment
























































# 5-2-1-71
def ranandrou521_Stem_047():
    stem = "오늘 {n1}{pj1} 보러 온 사람 수를 반올림하여 십의 자리까지 나타내면 $$수식$${sa}$$/수식$$명입니다. 이 사람들에게 {n2}{pj2} 한 개씩 모두 나누어 주려면 {n2}{pj2} 적어도 몇 개 준비해야 하나요?\n"
    answer = "(정답)\n$$수식$${s2}$$/수식$$개\n"
    comment = "(해설)\n" \
              "반올림하여 십의 자리까지 나타내면 $$수식$${sa}$$/수식$$이므로 {n1}{pj1} 보러 온 사람 수의 범위는 $$수식$${s1}$$/수식$$명부터 $$수식$${s2}$$/수식$$명까지입니다.\n" \
              "{n2}{pj3} 가장 많이 필요한 경우는 사람 수가 가장 많을 때이므로 {n2}{pj2} 적어도 $$수식$${s2}$$/수식$$개 준비해야 합니다.\n\n"


    n1 = ["공연", "전시"][np.random.randint(0, 2)]
    n2 = ["부채", "풍선", "책받침"][np.random.randint(0, 3)]

    if n1 == "전시":
        pj1 = "를"
    elif n1 == "공연":
        pj1 = "을"

    if n2 == "부채":
        pj2 = "를"
        pj3 = "가"
    elif n2 == "풍선" or n2 == "책받침":
        pj2 = "을"
        pj3 = "이"

    while True:
        a1 = np.random.randint(5, 10)
        a2 = np.random.randint(1, 10)
        if a1 != a2:
            break

    sa = a1 * 100 + a2 * 10

    s1 = sa - 5
    s2 = sa + 4


    stem = stem.format(n1=n1, n2=n2, sa=sa, pj1=pj1, pj2=pj2)
    answer = answer.format(s2=s2)
    comment = comment.format(n1=n1, n2=n2, sa=sa, s1=s1, s2=s2, pj1=pj1, pj2=pj2, pj3=pj3)

    return stem, answer, comment






















































# 5-2-1-72
def ranandrou521_Stem_048():
    stem = "어느 날의 환율입니다. 우리나라 돈 $$수식$${sa}$$/수식$$원으로 최대 몇 {sn}까지 바꿀 수 있나요?\n$$표$$$$수식$${box1} ~ = ~ {box2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${s1}$$/수식$${sn}\n"
    comment = "(해설)\n" \
              "$$수식$${sa} ` div ` {sb} ` = ` {s1} ` CDOTS ` {s2}$$/수식$$\n" \
              "남은 $$수식$${s2}$$/수식$$원은 $$수식$$1$$/수식$${sn}로 바꿀 수 없으므로 버림하면 최대 $$수식$${s1}$$/수식$${sn}까지 바꿀 수 있습니다.\n\n"


    sn = ["엔화", "달러", "유로"][np.random.randint(0, 3)]

    if sn == "엔화":
        sb = 11
    elif sn == "달러":
        sb = 1200
    elif sn == "유로":
        sb = 1300

    while True:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(1, 10)
        sa = a1 * 100000 + a2 * 10000
        s1 = int(sa // sb)
        s2 = sa - sb * s1
        if a1 != a2 and s2 != 0:
            break

    box1 = "1`%s" % sn
    box2 = "%d`원" % sb


    stem = stem.format(sn=sn, sb=sb, sa=sa, box1=box1, box2=box2)
    answer = answer.format(s1=s1, sn=sn)
    comment = comment.format(sn=sn, sb=sb, sa=sa, s1=s1, s2=s2)

    return stem, answer, comment






