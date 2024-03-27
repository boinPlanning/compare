"""
초등 3학년 1학기 4단원
"""

import numpy as np




answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤"
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






# 3-1-4-04
def multiplication314_Stem_001():
    stem = "㉠, ㉡에 알맞은 수를 차례로 구하세요.\n$$수식$${sa} ` times ` {sb} ` = `$$/수식$$ $$수식$${box1}$$/수식$$ → $$수식$${sc} ` times ` {sb} ` = `$$/수식$$ $$수식$${box2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${sd}$$/수식$$, $$수식$${se}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa} ` times ` {sb} ` = ` {sd}$$/수식$$이고 " \
              "계산한 $$수식$${sd}$$/수식$$에 $$수식$$0$$/수식$$을 붙이면  $$수식$${sc} ` times ` {sb} ` = ` {se}$$/수식$$입니다.\n\n"


    while True:
        sa = np.random.randint(2, 5)
        sb = np.random.randint(2, 10)
        if sa * sb <= 9:
            break

    sc = sa * 10
    sd = sa * sb
    se = sc * sb

    box1 = "box{㉠````````````````````}"
    box2 = "box{㉡````````````````````}"

    stem = stem.format(sa=sa, sb=sb, sc=sc, box1=box1, box2=box2)
    answer = answer.format(sd=sd, se=se)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)

    return stem, answer, comment






# 3-1-4-06
def multiplication314_Stem_002():
    stem = "계산 결과가 더 큰 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${sa} ` times ` {sb}$$/수식$$      ㉡ $$수식$${sc} ` times ` {sd}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{sy}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${sa} ` times ` {sb} ` = ` {se}$$/수식$$, ㉡ $$수식$${sc} ` times ` {sd} ` = ` {sf}$$/수식$$\n" \
              "따라서 $$수식$${se} ` {sx} ` {sf}$$/수식$$이므로 계산 결과가 더 큰 것은 {sy}입니다.\n\n"


    while True:
        ssa = np.random.randint(2, 5)
        sb = np.random.randint(2, 5)
        ssc = np.random.randint(1, 5)
        sd = np.random.randint(2, 10)

        sa = ssa * 10
        sc = ssc * 10
        se = sa * sb
        sf = sc * sd
        if ssa*sb <= 9 and ssc != ssa and sd!=sb and ssc*sd<=9 and sd!=(sa*sb)/sc and se!=sf:
            break

    if se > sf:
        sx = "&gt;"
        sy = "㉠"

    elif se < sf:
        sx = "&lt;"
        sy = "㉡"

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(sy=sy)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sx=sx, sy=sy)

    return stem, answer, comment







# 3-1-4-08
def multiplication314_Stem_003():
    stem = "{sp}이는 하루에 {ss}을 $$수식$${sa}$$/수식$$쪽씩 읽었습니다. {sp}이가 $$수식$${sb}$$/수식$$일 동안 읽은 {ss}은 모두 몇 쪽인가요?\n"
    answer = "(정답)\n$$수식$${sc}$$/수식$$쪽\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${sp}이가 $$수식$${sb}$$/수식$$일 동안 읽은 {ss} 쪽수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$$하루에 읽은 {ss} 쪽수$$수식$$RIGHT ) times LEFT ($$/수식$$날수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {sa} ` times {sb} ` = ` {sc} LEFT ($$/수식$$쪽$$수식$$RIGHT )$$/수식$$\n\n"


    splist = ["서준", "민영", "혁진", "혜란", "도윤", "주현", "자연", "재령", "민준", "상현", "영웅", "정윤", "수빈", "휘진"]
    sslist = ["동화책", "소설책", "위인전"]

    sp = np.random.choice(splist)
    ss = np.random.choice(sslist)

    ssa = np.random.randint(2, 6)
    sb = np.random.randint(6, 10)

    sa = ssa * 10
    sc = sa * sb

    stem = stem.format(sp=sp, ss=ss, sa=sa, sb=sb)
    answer = answer.format(sc=sc)
    comment = comment.format(sp=sp, ss=ss, sa=sa, sb=sb, sc=sc)

    return stem, answer, comment








# 3-1-4-14
def multiplication314_Stem_004():
    stem = "계산 결과를 비교하여 □ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${sa} ` times ` {sb}$$/수식$$     $$수식$${box}$$/수식$$     $$수식$${sc} ` times ` {sd}$$/수식$$\n"
    answer = "(정답)\n$$수식$${sx}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa} ` times ` {sb} ` = ` {se}$$/수식$$, $$수식$${sc} ` times ` {sd} ` = `{sf}$$/수식$$에서 " \
              "$$수식$${se} ` {sx} ` {sf}$$/수식$$이므로 " \
              "$$수식$${sa} ` times ` {sb} ` {sx} ` {sc} ` times ` {sd}$$/수식$$입니다.\n\n"


    while True:
        sa1 = np.random.randint(1, 5)
        sb = np.random.randint(2, 10)
        sa2 = np.random.randint(1, 5)
        sc1 = np.random.randint(1, 5)
        sd = np.random.randint(2, 10)
        sc2 = np.random.randint(1, 5)

        sa = sa1 * 10 + sa2
        sc = sc1 * 10 + sc2
        se = sa * sb
        sf = sc * sd

        if sa1*sb<=9 and sa2*sb<=9 and sa2!=sa1 and sc1 != sa1 and sd != sb and \
            sc1*sd <=9 and sc2 != sc1 and sc2*sd <=9 and se != sf:
            break

    if se > sf:
        sx = "&gt;"
    elif se < sf:
        sx = "&lt;"

    box = "□"

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, box=box)
    answer = answer.format(sx=sx)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sx=sx)

    return stem, answer, comment






# 3-1-4-15
def multiplication314_Stem_005():
    stem = "{ss} 한 타는 $$수식$$12$$/수식$$자루입니다. 선생님께서 {ss} $$수식$${sa}$$/수식$$타를 학생들에게 상품으로 주려고 합니다. 상품으로 줄 {ss}은 모두 몇 자루인가요?\n"
    answer = "(정답)\n$$수식$${sb}$$/수식$$자루\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$상품으로 줄 {ss} 수$$수식$$RIGHT )$$/수식$$\n$$수식$$ = ($$/수식$$한 타의 {ss} 수$$수식$$RIGHT ) times ` {sa} = 12 ` times ` {sa} ` = ` {sb} LEFT ($$/수식$$자루$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 상품으로 줄 {ss}은 모두 $$수식$${sb}$$/수식$$자루입니다.\n\n"


    sslist = ["연필", "볼펜", "사인펜", "형광펜", "색연필"]

    ss = np.random.choice(sslist)

    sa = np.random.randint(2, 5)
    sb = 12*sa

    stem = stem.format(ss=ss, sa=sa)
    answer = answer.format(sb=sb)
    comment = comment.format(ss=ss, sa=sa, sb=sb)

    return stem, answer, comment







# 3-1-4-16
def multiplication314_Stem_006():
    stem = "계산 결과가 가장 큰 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${sa} ` times ` {sb}$$/수식$$      ㉡ $$수식$${sc} ` times ` {sd}$$/수식$$     ㉢ $$수식$${se} ` times ` {sf}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{sx}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${sa} ` times ` {sb} ` = ` {sg}$$/수식$$, " \
              "㉡ $$수식$${sc} ` times ` {sd} ` = ` {sh}$$/수식$$, " \
              "㉢ $$수식$${se} ` times ` {sf} ` = ` {si}$$/수식$$\n" \
              "따라서 $$수식$${sj} ` &gt; ` {sk} ` &gt; ` {sl}$$/수식$$이므로 계산 결과가 가장 큰 것은 {sx}입니다.\n\n"


    while True:
        sa1 = np.random.randint(1, 5)
        sb = np.random.randint(2, 10)
        sa2 = np.random.randint(1, 5)
        sc1 = np.random.randint(1, 5)

        sd = np.random.randint(2, 10)
        sc2 = np.random.randint(1, 5)
        se1 = np.random.randint(1, 5)
        sf = np.random.randint(2, 10)
        se2 = np.random.randint(1, 5)

        sa = sa1 * 10 + sa2
        sc = sc1 * 10 + sc2
        se = se2 * 10 + se2

        sg = sa * sb
        sh = sc * sd
        si = se * sf

        if sa1 * sb <= 9 and sa2 * sb <= 9 and sc1 != sa1 and sd != sb and sc1 * sd <= 9 and \
            se1 != sa1 and se1 != sc1 and sf != sb and sf != sd and se1 * sf <= 9 and se2 * sf <= 9 and sg!=sh and sg!=si and sh!=si:
            break

    ghilist = [sg, sh, si]
    ghilist.sort(reverse=True)

    sj = ghilist[0]
    sk = ghilist[1]
    sl = ghilist[2]

    if sg == sj:
        sx = "㉠"
    elif sh == sj:
        sx = "㉡"
    elif si == sj:
        sx = "㉢"

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf)
    answer = answer.format(sx=sx)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sx=sx, sg=sg, sh=sh, si=si, sj=sj, sk=sk, sl=sl)

    return stem, answer, comment






# 3-1-4-17
def multiplication314_Stem_007():
    stem = "어떤 수를 $$수식$${sb}$$/수식$${ro} 나누었더니 $$수식$${sa}$$/수식$${pj} 되었습니다. 어떤 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${sc}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □라고 하면 $$수식$$□ ` div ` {sb} ` = ` {sa}$$/수식$$ → $$수식$${sa} ` times ` {sb} ` = `$$/수식$$□\n □$$수식$$` = ` {sc}$$/수식$$입니다.\n"\
              "따라서 어떤 수는 $$수식$${sc}$$/수식$$입니다.\n\n"


    while True:
        sa1 = np.random.randint(1, 5)
        sb = np.random.randint(2, 10)
        sa2 = np.random.randint(1, 5)
        if sa1*sb <= 9 and sa2*sb <= 9 and sa1 != sa2:
            break

    sa = sa1 * 10 + sa2
    sc = sa * sb
    pj = proc_jo(sa,0)

    if sb == 3 or sb == 6:
        ro = "으로"
    else:
        ro = "로"

    stem = stem.format(sb=sb, sa=sa, pj=pj, ro=ro)
    answer = answer.format(sc=sc)
    comment = comment.format(sc=sc, sa=sa, sb=sb)

    return stem, answer, comment







# 3-1-4-18
def multiplication314_Stem_008():
    stem = "{p1}와 {p2}의 대화를 읽고 {p1}와 {p2}가 가지고 있는 {ss}은 모두 몇 개인지 구해보세요.\n$$표$${p1}: 난 {ss}을 한 봉지에 $$수식$${sa}$$/수식$$개씩 $$수식$${sb}$$/수식$$봉지 가지고 있어.\n{p2}: 난 {ss}을 한 봉지에 $$수식$${sc}$$/수식$$개씩 $$수식$${sd}$$/수식$$봉지를 가지고 있지.$$/표$$\n"
    answer = "(정답)\n$$수식$${sg}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${p1}가 가지고 있는 {ss} 수$$수식$$RIGHT ) ` = ` {sa} ` times ` {sb} ` = ` {se} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${p2}가 가지고 있는 {ss} 수$$수식$$RIGHT ) ` = ` {sc} ` times ` {sd} ` = ` {sf} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 {p1}와 {p2}가 가지고 있는 {ss}은 모두 $$수식$${se} ` + ` {sf} ` = ` {sg} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    splist = ["수미", "현수", "채아", "민주", "지호", "연아", "은우", "시우", "혁재", "민아", "영서", "승태", "민지", "선규"]
    sslist = ["구슬", "밤", "강낭콩", "사탕", "초콜릿"]

    while True:
        p1 = np.random.choice(splist)
        p2 = np.random.choice(splist)
        if p1 != p2:
            break

    ss = np.random.choice(sslist)

    while True:
        ssa = np.random.randint(1, 5)
        sb = np.random.randint(2, 10)
        sc1 = np.random.randint(1, 5)
        sc2 = np.random.randint(1, 5)
        sd = np.random.randint(2, 10)

        if ssa*sb <= 9 and sc1*sd <= 9 and sc1 != ssa and sd != sb and sc2*sd <= 9:
            break

    sa = ssa*10
    sc = sc1*10 + sc2
    se = sa*sb
    sf = sc*sd
    sg = se+sf

    stem = stem.format(p1=p1, p2=p2, ss=ss, sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(sg=sg)
    comment = comment.format(p1=p1, p2=p2, ss=ss, sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg)

    return stem, answer, comment






# 3-1-4-21
def multiplication314_Stem_009():
    stem = "계산이 잘못된 것은 어느 것인가요?\n① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "{a1} $$수식$${sa} ` TIMES ` {sa3} = {sf}$$/수식$$입니다.\n\n"


    while True:
        sa3 = np.random.randint(2, 9)
        sa1 = np.random.randint(4, 10)
        sa2 = np.random.randint(1, 5)
        sb3 = np.random.randint(2, 9)
        sb1 = np.random.randint(4, 10)

        sb2 = np.random.randint(1, 5)
        sc3 = np.random.randint(2, 9)
        sc1 = np.random.randint(4, 10)
        sc2 = np.random.randint(1, 5)
        sd3 = np.random.randint(2, 9)

        sd1 = np.random.randint(4, 10)
        sd2 = np.random.randint(1, 5)
        se3 = np.random.randint(2, 9)
        se1 = np.random.randint(4, 10)
        se2 = np.random.randint(1, 5)

        if 10 <= (sa1 * sa3) and (sa2 * sa3) <= 9 and 10 <= (sb1 * sb3) and sb1 != sa1 and \
        (sb2 * sb3) <= 9 and 10 <= (sc1 * sc3) and sc1 != sa1 and sc1 != sb1 and \
        (sc2 * sc3) <= 9 and 10 <= (sd1 * sd3) and sd1 != sa1 and sd1 != sb1 and sd1 != sc1 and \
        (sd2 * sd3) <= 9 and 10 <= (se1 * se3) and se1 != sa1 and se1 != sb1 and se1 != sc1 and se1 != sd1 and \
        (se2 * se3) <= 9:
            break

    sa = sa1*10 + sa2
    sb = sb1*10 + sb2
    sc = sc1*10 + sc2
    sd = sd1*10 + sd2
    se = se1*10 + se2

    sf = sa*sa3
    sg = sb*sb3
    sh = sc*sc3
    si = sd*sd3
    sj = se*se3

    sk = (sa1 + sa2)*10*sa3

    y1 = "%d ` times ` %d ` = %d" % (sa, sa3, sk)
    y2 = "%d ` times ` %d ` = %d" % (sb, sb3, sg)
    y3 = "%d ` times ` %d ` = %d" % (sc, sc3, sh)
    y4 = "%d ` times ` %d ` = %d" % (sd, sd3, si)
    y5 = "%d ` times ` %d ` = %d" % (se, se3, sj)

    candidates = [y1, y2, y3, y4, y5]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4, x5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):
        if sdx == y1:
            correct_idx = idx
            break

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(a1=answer_dict[correct_idx], sa=sa, sa3=sa3, sf=sf)

    return stem, answer, comment







# 3-1-4-24
def multiplication314_Stem_010():
    stem = "가장 큰 수와 가장 작은 수의 곱은 얼마인가요?\n$$표$$$$수식$${sa1}$$/수식$$  $$수식$${sb2}$$/수식$$  $$수식$${sc3}$$/수식$$  $$수식$${sd4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${se}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa} ` &gt; ` {sb} ` &gt; `{sc} ` &gt; `{sd}$$/수식$$이므로 " \
              "가장 큰 수는 $$수식$${sa}$$/수식$$, 가장 작은 수는 $$수식$${sd}$$/수식$$입니다.\n" \
              "따라서 가장 큰 수와 가장 작은 수의 곱은 $$수식$${sa} ` times ` {sd} ` = ` {se}$$/수식$$입니다.\n\n"


    while True:
        sc = np.random.randint(5, 10)
        sd = np.random.randint(3, 7)
        sa1 = np.random.randint(4, 10)
        sb1 = np.random.randint(4, 10)
        sa2 = np.random.randint(1, 5)
        sb2 = np.random.randint(1, 5)

        sa = sa1*10 + sa2
        sb = sb1*10 + sb2

        if sd<sc and sb1<sa1 and sa2*sd <= 9 and sb2*sd <= 9 and sa!=sb:
            break

    se = sa*sd

    candidates = [sa, sb, sc, sd]
    np.random.shuffle(candidates)
    [sa1, sb2, sc3, sd4] = candidates

    stem = stem.format(sa1=sa1, sb2=sb2, sc3=sc3, sd4=sd4)
    answer = answer.format(se=se)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)

    return stem, answer, comment








# 3-1-4-26
def multiplication314_Stem_011():
    stem = "어떤 수를 $$수식$${sb}$$/수식$${ro} 나누었더니 $$수식$${sa}$$/수식$${pj} 되었습니다. 어떤 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${sc}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □라고 하면 □$$수식$$` div ` {sb} ` = ` {sa}$$/수식$$ → $$수식$${sa} ` times ` {sb} ` = `$$/수식$$□\n □$$수식$$` = ` {sc}$$/수식$$입니다.\n"\
              "따라서 어떤 수는 $$수식$${sc}$$/수식$$입니다.\n\n"


    while True:
        sb = np.random.randint(3,10)
        sa2 = np.random.randint(1,9)
        sa1 = np.random.randint(4,10)
        if sa2*sb <= 9 and 10 <= sa1*sb:
            break

    sa=sa1*10+sa2
    sc=sa*sb
    pj=proc_jo(sa,0)

    if sb == 3 or sb == 6:
        ro = "으로"
    else:
        ro = "로"

    stem = stem.format(sb=sb, sa=sa, pj=pj, ro=ro)
    answer = answer.format(sc=sc)
    comment = comment.format(sc=sc, sa=sa, sb=sb)

    return stem, answer, comment









# 3-1-4-27
def multiplication314_Stem_012():
    stem = "계산 결과가 가장 큰 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${sa} ` times ` {sb}$$/수식$$      ㉡ $$수식$${sc} ` times ` {sd}$$/수식$$     ㉢ $$수식$${se} ` times ` {sf}$$/수식$$     ㉣ $$수식$${sg} ` times ` {sh}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{sx}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${sa} ` times ` {sb} ` = ` {si}$$/수식$$, " \
              "㉡ $$수식$${sc} ` times ` {sd} ` = ` {sj}$$/수식$$\n " \
              "㉢ $$수식$${se} ` times ` {sf} ` = ` {sk}$$/수식$$, " \
              "㉣ $$수식$${sg} ` times ` {sh} ` = ` {sl}$$/수식$$\n" \
              "따라서 $$수식$${sm} ` &gt; ` {sn} ` &gt; ` {so} ` &gt; ` {sp}$$/수식$$이므로 계산 결과가 가장 큰 것은 {sx}입니다.\n\n"


    while True:
        sb = np.random.randint(2, 10)
        sd = np.random.randint(2, 10)
        sf = np.random.randint(2, 10)
        sh = np.random.randint(2, 10)

        sa1 = np.random.randint(5, 10)
        sc1 = np.random.randint(5, 10)
        se1 = np.random.randint(5, 10)
        sg1 = np.random.randint(5, 10)

        sa2 = np.random.randint(1, 5)
        sc2 = np.random.randint(1, 5)
        se2 = np.random.randint(1, 5)
        sg2 = np.random.randint(1, 5)

        sa = sa1 * 10 + sa2
        sc = sc1 * 10 + sc2
        se = se1 * 10 + se2
        sg = sg1 * 10 + sg2

        si = sa * sb
        sj = sc * sd
        sk = se * sf
        sl = sg * sh

        if sg1 < se1 and se1 < sc1 and sc1 < sa1 and sa2 * sb <= 9 and sc2 * sd <= 9 and se2 * sf <= 9 and sg2 * sh <= 9 and si != sj and sj != sk and sk != sl:
            break

    ijkllist = [si, sj, sk, sl]
    ijkllist.sort(reverse = True)

    sm = ijkllist[0]
    sn = ijkllist[1]
    so = ijkllist[2]
    sp = ijkllist[3]

    if si == sm:
        sx = "㉠"
    elif sj == sm:
        sx = "㉡"
    elif sk == sm:
        sx = "㉢"
    elif sl == sm:
        sx = "㉣"

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sh=sh)
    answer = answer.format(sx=sx)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sx=sx, sg=sg, sh=sh, si=si, sj=sj, sk=sk, sl=sl, sm=sm, sn=sn, so=so, sp=sp)

    return stem, answer, comment








# 3-1-4-33
def multiplication314_Stem_013():
    stem = "다음이 나타내는 수의 $$수식$${sb}$$/수식$$배인 수를 구해보세요.\n$$표$$$$수식$$10$$/수식$$이 $$수식$${sa1}$$/수식$$개,    $$수식$$1$$/수식$$이 $$수식$${sa2}$$/수식$$개$$/표$$\n"
    answer = "(정답)\n$$수식$${sc}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$10$$/수식$$이 $$수식$${sa1}$$/수식$$개, $$수식$$1$$/수식$$이 $$수식$${sa2}$$/수식$$개인 수는 $$수식$${sa}$$/수식$$입니다.\n" \
              "따라서 $$수식$${sa}$$/수식$$의 $$수식$${sb}$$/수식$$배인 수는 $$수식$${sa} ` times ` {sb} ` = ` {sc}$$/수식$$입니다.\n\n"


    while True:
        sb = np.random.randint(2, 10)
        sa2 = np.random.randint(5, 10)
        sa1 = np.random.randint(1, 5)
        if sa1*sb <= 9:
            break

    sa = sa1*10 + sa2
    sc = sa*sb

    stem = stem.format(sa1=sa1, sa2=sa2, sb=sb)
    answer = answer.format(sc=sc)
    comment = comment.format(sa1=sa1, sa2=sa2, sb=sb, sa=sa, sc=sc)

    return stem, answer, comment








# 3-1-4-34
def multiplication314_Stem_014():
    stem = "계산 결과가 가장 큰 것부터 차례대로 기호를 써 보세요.\n$$표$$㉠ $$수식$${sa} ` times ` {sb}$$/수식$$      ㉡ $$수식$${sc} ` times ` {sd}$$/수식$$     ㉢ $$수식$${se} ` times ` {sf}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{sx}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${sa} ` times ` {sb} ` = ` {sg}$$/수식$$, " \
              "㉡ $$수식$${sc} ` times ` {sd} ` = ` {sh}$$/수식$$, " \
              "㉢ $$수식$${se} ` times ` {sf} ` = ` {si}$$/수식$$\n" \
              "따라서 $$수식$${sj} ` &gt; ` {sk} ` &gt; ` {sl}$$/수식$$이므로 계산 결과가 큰 것부터 기호를 쓰면 {sx}입니다.\n\n"


    while True:
        sb = np.random.randint(2, 10)
        sd = np.random.randint(2, 10)
        sf = np.random.randint(2, 10)

        sa2 = np.random.randint(5, 10)
        sc2 = np.random.randint(5, 10)
        se2 = np.random.randint(5, 10)

        sa1 = np.random.randint(1, 5)
        sc1 = np.random.randint(1, 5)
        se1 = np.random.randint(1, 5)

        sa = sa1 * 10 + sa2
        sc = sc1 * 10 + sc2
        se = se1 * 10 + se2

        sg = sa * sb
        sh = sc * sd
        si = se * sf

        if sb < sd and sd < sf and se2 < sc2 and sc2 < sa2 and sa1 * sb <= 9 and sc1 * sd <= 9 and se1 * sf <= 9:
            if sa1 != se1 or sc1 != se1:
                break

    ghilist = [sg, sh, si]
    ghilist.sort(reverse = True)

    sj = ghilist[0]
    sk = ghilist[1]
    sl = ghilist[2]

    if sg == sj and sh==sk:
        sx = "㉠, ㉡, ㉢"
    elif sg == sj and si==sk:
        sx = "㉠, ㉢, ㉡"
    elif sh == sj and si==sk:
        sx = "㉡, ㉢, ㉠"
    elif sh == sj and sg == sk:
        sx = "㉡, ㉠, ㉢"
    elif si == sj and sg == sk:
        sx = "㉢, ㉠, ㉡"
    elif si == sj and sh == sk:
        sx = "㉢, ㉡, ㉠"

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf)
    answer = answer.format(sx=sx)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sx=sx, sg=sg, sh=sh, si=si, sj=sj, sk=sk, sl=sl)

    return stem, answer, comment








# 3-1-4-35
def multiplication314_Stem_015():
    stem = "원 모양인 {s1} 둘레에 {s2} $$수식$${sb}$$/수식$$그루를 $$수식$${sa} rm m$$/수식$$ 간격으로 심었습니다. {s1}의 둘레는 몇 $$수식$$rm m$$/수식$$인가요? $$수식$$LEFT ($$/수식$$단, {s2}의 두께는 생각하지 않는다.$$수식$$RIGHT )$$/수식$$\n"
    answer = "(정답)\n$$수식$${sc} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "{s2}를 $$수식$${sb}$$/수식$$그루 심었을 때 {s2} 사이의 간격은 $$수식$${sb}$$/수식$$군데입니다.\n" \
              "따라서 {s1} 둘레의 길이는 $$수식$${sa} ` times ` {sb} ` = ` {sc} ` LEFT ( ` rm m ` RIGHT )$$/수식$$입니다.\n\n"


    s1 = ["호수", "광장"][np.random.randint(0, 1)]
    s2 = ["나무", "소나무", "벚나무", "느티나무", "단풍나무", "플라타너스"][np.random.randint(0, 5)]

    while True:
        sb = np.random.randint(2, 10)
        a2 = np.random.randint(4, 10)
        a1 = np.random.randint(1, 5)
        if 10 <= a2*sb and a1*sb <= 9:
            break

    sa = a1*10 + a2
    sc = sa*sb

    stem = stem.format(s1=s1, s2=s2, sa=sa, sb=sb)
    answer = answer.format(sc=sc)
    comment = comment.format(s1=s1, s2=s2, sa=sa, sb=sb, sc=sc)

    return stem, answer, comment








# 3-1-4-36
def multiplication314_Stem_016():
    stem = "곧게 뻗은 길의 한쪽에 처음부터 끝까지 {ss} $$수식$${sb}$$/수식$$그루를 $$수식$${sa} rm m$$/수식$$ 간격으로 나란히 심었습니다. 이 길의 길이는 몇 $$수식$$rm m$$/수식$$인가요? $$수식$$LEFT ($$/수식$$단, {ss}의 두께는 생각하지 않는다.$$수식$$RIGHT )$$/수식$$\n"
    answer = "(정답)\n$$수식$${sd} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "{ss}를 $$수식$${sb}$$/수식$$그루 심었을 때 {ss} 사이의 간격은 $$수식$${sc}$$/수식$$군데입니다.\n" \
              "따라서 길의 길이는 $$수식$${sa} ` times ` {sc} ` = ` {sd} ` LEFT ( ` rm m ` RIGHT )$$/수식$$입니다.\n\n"


    ss = ["나무", "소나무", "벚나무", "느티나무", "단풍나무", "플라타너스"][np.random.randint(0, 5)]

    while True:
        sc = np.random.randint(2, 10)
        sb = sc + 1
        a2 = np.random.randint(4, 10)
        a1 = np.random.randint(1, 5)
        if 10 <= a2*sb and a1*sc <= 9:
            break

    sa = a1*10 + a2
    sd = sa*sc

    stem = stem.format(ss=ss, sa=sa, sb=sb)
    answer = answer.format(sd=sd)
    comment = comment.format(ss=ss, sa=sa, sb=sb, sc=sc, sd=sd)

    return stem, answer, comment








# 3-1-4-41
def multiplication314_Stem_017():
    stem = "가장 큰 수와 가장 작은 수의 곱은 얼마인가요?\n$$표$$$$수식$${sa1}$$/수식$$  $$수식$${sb2}$$/수식$$  $$수식$${sc3}$$/수식$$  $$수식$${sd4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${se}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa} ` &gt; ` {sb} ` &gt; `{sc} ` &gt; `{sd}$$/수식$$이므로 " \
              "가장 큰 수는 $$수식$${sa}$$/수식$$, 가장 작은 수는 $$수식$${sd}$$/수식$$입니다. \n" \
              "따라서 가장 큰 수와 가장 작은 수의 곱은 $$수식$${sa} ` times ` {sd} ` = ` {se}$$/수식$$입니다.\n\n"


    while True:
        sc = np.random.randint(5, 10)
        sd = np.random.randint(3, 7)

        sa1 = np.random.randint(4, 10)
        sb1 = np.random.randint(4, 10)
        sa2 = np.random.randint(3, 10)
        sb2 = np.random.randint(3, 10)

        sa = sa1*10 + sa2
        sb = sb1*10 + sb2

        if sd < sc and sb1 < sa1 and 10 <= sa2*sd and 10 <= sb2*sd and sa2 != sb2:
            break

    se = sa*sd

    candidates = [sa, sb, sc, sd]
    np.random.shuffle(candidates)
    [sa1, sb2, sc3, sd4] = candidates

    stem = stem.format(sa1=sa1, sb2=sb2, sc3=sc3, sd4=sd4)
    answer = answer.format(se=se)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)

    return stem, answer, comment








# 3-1-4-43
def multiplication314_Stem_018():
    stem = "바늘 한 쌈은 $$수식$$24$$/수식$$개입니다. 바늘 $$수식$${sa}$$/수식$$쌈은 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${sb}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$전체 바늘 수$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$= LEFT ($$/수식$$바늘 한 쌈의 바늘 수$$수식$$RIGHT ) times LEFT ($$/수식$$바늘 쌈 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= 24 times {sa} = {sb} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    sa = np.random.randint(3, 10)
    sb = 24*sa

    stem = stem.format(sa=sa)
    answer = answer.format(sb=sb)
    comment = comment.format(sa=sa, sb=sb)

    return stem, answer, comment







# 3-1-4-45
def multiplication314_Stem_019():
    stem = "어떤 수에 $$수식$${sb}$$/수식$${josa} 곱해야 할 것을 잘못하여 $$수식$${sb}$$/수식$${ro} 나누었더니 $$수식$${sa}$$/수식$${pj} 되었습니다. 바르게 계산하면 얼마인가요?\n"
    answer = "(정답)\n$$수식$${sd}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □라고 하면\n" \
              "□$$수식$$` div ` {sb} ` = ` {sa}$$/수식$$ → $$수식$${sa} ` times ` {sb} ` =$$/수식$$□, □$$수식$$= ` {sc}$$/수식$$입니다.\n" \
              "따라서 바르게 계산하면 $$수식$${sc} ` times ` {sb} ` = ` {sd} `$$/수식$$입니다.\n\n"


    sb = np.random.randint(2, 10)

    if sb == 2:
        sa = [33, 34, 43, 44][np.random.randint(0, 3)]
    elif sb == 3:
        sa = [22, 23, 32, 33][np.random.randint(0, 3)]
    elif sb == 4:
        sa = [11, 12, 21, 22][np.random.randint(0, 3)]
    elif sb == 5 or sb == 6 or sb == 7 or sb == 8 or sb == 9:
        sa = 11

    sc = sa*sb
    sd = sc*sb
    pj = proc_jo(sa, 0)

    if sb == 3 or sb == 6:
        ro = "으로"
    else:
        ro = "로"

    if sb in [1,3,6,7,8]:
        josa = "을"
    else:
        josa = "를"

    stem = stem.format(sb=sb, sa=sa, pj=pj, ro=ro, josa=josa)
    answer = answer.format(sd=sd)
    comment = comment.format(sc=sc, sa=sa, sb=sb, sd=sd)

    return stem, answer, comment




