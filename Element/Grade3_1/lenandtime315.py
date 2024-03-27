"""
초등 3학년 1학기 5단원
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





# 3-1-5-02
def lenandtime315_Stem_001():
    stem = "주어진 길이를 써 보세요.\n$$표$$     $$수식$${sa}$$/수식$$ 밀리미터    $$/표$$\n"
    answer = "(정답)\n$$수식$${sa} {sb}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$ 밀리미터는 $$수식$${sa} {sb}$$/수식$$라고 씁니다.\n\n"


    sa = np.random.randint(2, 10)
    sb = "rm {{mm}}"

    stem = stem.format(sa=sa)
    answer = answer.format(sa=sa, sb=sb)
    comment = comment.format(sa=sa, sb=sb)

    return stem, answer, comment





# 3-1-5-03
def lenandtime315_Stem_002():
    stem = "주어진 길이를 써 보세요.\n$$표$$  $$수식$${sa}$$/수식$$ 센티미터 $$수식$${sb}$$/수식$$ 밀리미터  $$/표$$\n"
    answer = "(정답)\n$$수식$${sa}{sc} {sb}{sd}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$ 센티미터 $$수식$${sb}$$/수식$$ 밀리미터는 $$수식$${sa}{sc} `` {sb}{sd}$$/수식$$라고 씁니다.\n\n"


    while True:
        sa = np.random.randint(2, 10)
        sb = np.random.randint(2, 10)
        if sa != sb:
            break

    sc="rm {{cm}}"
    sd="rm {{mm}}"

    stem = stem.format(sa=sa, sb=sb)
    answer = answer.format(sa=sa, sb=sb, sc=sc, sd=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd)

    return stem, answer, comment





# 3-1-5-05
def lenandtime315_Stem_003():
    stem = "$$수식$${sa} rm {{cm}}$$/수식$$보다 $$수식$${sb} rm {{mm}}$$/수식$$ 더 긴 길이는 몇 $$수식$$rm {{cm}}$$/수식$$ 몇 $$수식$$rm {{mm}}$$/수식$$인지 써 보세요.\n"
    answer = "(정답)\n$$수식$${sa} rm {{cm}} ``{sb} rm {{mm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa} rm {{cm}}$$/수식$$보다 $$수식$${sb} rm {{mm}}$$/수식$$ 더 긴 길이를\n" \
              "$$수식$${sa} rm {{cm}} ``{sb} rm {{mm}}$$/수식$$라 쓰고, $$수식$${sa}$$/수식$$ 센티미터 $$수식$${sb}$$/수식$$ 밀리미터라고 읽습니다.\n\n"


    while True:
        sa = np.random.randint(2, 10)
        sb = np.random.randint(2, 10)
        if sa != sb:
            break

    stem = stem.format(sa=sa, sb=sb)
    answer = answer.format(sa=sa, sb=sb)
    comment = comment.format(sa=sa, sb=sb)

    return stem, answer, comment






# 3-1-5-06
def lenandtime315_Stem_004():
    stem = "□ 안에 들어갈 알맞은 수를 구하세요.\n$$수식$$LEFT ( 1 RIGHT ) ```` {sa} rm {{cm}} `` {sb} rm {{mm}} ` = `$$/수식$$ $$수식$${box1}$$/수식$$ $$수식$$rm {{mm}}$$/수식$$\n$$수식$$LEFT ( 2 RIGHT ) ```` {se} rm {{mm}} ` = `$$/수식$$ $$수식$${box1}$$/수식$$ $$수식$$rm {{cm}} ``$$/수식$$ $$수식$${box1}$$/수식$$ $$수식$$rm {{mm}}$$/수식$$\n"
    answer = "(정답)\n$$수식$${sd}$$/수식$$, $$수식$${sh}$$/수식$$, $$수식$${sg}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1 RIGHT ) ```` {sa} rm {{cm}} `` {sb} rm {{mm}} ` = ` {sa} rm {{cm}} ` + ` {sb} rm {{mm}} $$/수식$$\n $$수식$$` = ` {sc} rm {{mm}} ` + ` {sb} rm {{mm}} ` = ` {sd} rm {{mm}}$$/수식$$\n" \
              "$$수식$$LEFT ( 2 RIGHT ) ```` {se} rm {{mm}} ` = ` {sf} rm {{mm}} ` + ` {sg} rm {{mm}} $$/수식$$\n $$수식$$` = ` {sh} rm {{cm}} ` + ` {sg} rm {{mm}} ` = ` {sh} rm {{cm}} `` {sg} rm {{mm}}$$/수식$$\n\n"



    while True:
        sa = np.random.randint(2, 10)
        sb = np.random.randint(2, 10)

        e1 = np.random.randint(1, 6)
        e2 = np.random.randint(2, 8)
        e3 = np.random.randint(2, 10)

        if sa != sb and sa != e1 and e1 != e2 and e2 != e3 and sb != e3:
            break

    sc = sa * 10
    sd = sb + sc

    se = e1 * 100 + e2 * 10 + e3
    sf = e1 * 100 + e2 * 10
    sg = e3
    sh = e1 * 10 + e2

    box1 = "box{　　　}"

    stem = stem.format(sa=sa, sb=sb, se=se, box1=box1)
    answer = answer.format(sd=sd, sh=sh, sg=sg)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sh=sh)

    return stem, answer, comment






# 3-1-5-08
def lenandtime315_Stem_005():
    stem = "틀린 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${s1}$$/수식$$\n㉡ $$수식$${s2}$$/수식$$\n㉢ $$수식$${s3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "{a1}. $$수식$${sc} rm {{cm}} `` {sd} rm {{mm}} ` = ` {sc} rm {{cm}} ` + ` {sd} rm {{mm}} ` = ` {sh} rm {{mm}} ` + ` {sd} rm {{mm}} ` = ` {si} rm {{mm}}$$/수식$$\n\n"


    answer_dict2 = {
        0 : "㉠",
        1 : "㉡",
        2 : "㉢"
    }

    sa = np.random.randint(2, 10)
    sb = sa * 10

    while True:
        sc = np.random.randint(2, 10)
        sd = np.random.randint(2, 10)
        if sc != sd:
            break

    se = sc * 100 + sd
    sh = sc * 10
    si = sh + sd
    sg = np.random.randint(21, 80)
    sf = sg * 10

    y1 = "%d rm {{cm}} ` = ` %d rm {{mm}}" % (sa, sb)
    y2 = "%d rm {{cm}} `` %d rm {{mm}} ` = ` %d rm {{mm}}" % (sc, sd, se)
    y3 = "%d rm {{mm}} ` = ` %d rm {{cm}}" % (sf, sg)

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [s1, s2, s3] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates) :
        if sdx == y2 :
            correct_idx = idx
            break

    stem = stem.format(s1=s1, s2=s2, s3=s3)
    answer = answer.format(a1=answer_dict2[correct_idx])
    comment = comment.format(a1=answer_dict2[correct_idx], sc=sc, sd=sd, sh=sh, si=si)

    return stem, answer, comment







# 3-1-5-09
def lenandtime315_Stem_006():
    stem = "□ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${sa} rm {{cm}} `` {sb} rm {{mm}} ``````$$/수식$$ $$수식$${box}$$/수식$$ $$수식$$`````` {se} rm {{mm}}$$/수식$$\n"
    answer = "(정답)\n$$수식$${sx}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa} rm {{cm}} `` {sb} rm {{mm}} ` = ` {sa} rm {{cm}} ` + ` {sb} rm {{mm}} ` = ` {sc} rm {{mm}} ` + ` {sb} rm {{mm}} ` = ` {sd} rm {{mm}}$$/수식$$\n" \
              "따라서 $$수식$${sd} ` {sx} ` {se}$$/수식$$이므로 $$수식$${sd} rm {{mm}} ` {sx} ` {se} rm {{mm}}$$/수식$$입니다.\n\n"


    while True:
        sa = np.random.randint(3, 10)
        sb = np.random.randint(3, 10)
        sc = sa * 10
        sd = sc + sb
        se = np.random.randint(sd - 15, sd + 16)
        if sa != sb:
            break

    if sd > se:
        sx = "&gt;"
    elif sd == se:
        sx = "="
    elif sd < se:
        sx = "&lt;"

    box = "box{　　　}"

    stem = stem.format(sa=sa, sb=sb, se=se, box=box)
    answer = answer.format(sx=sx)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sx=sx)

    return stem, answer, comment







# 3-1-5-10
def lenandtime315_Stem_007():
    stem = "옳은 문장을 찾아 기호를 써 보세요.\n$$표$$㉠ {s1}\n㉡ {s2}\n㉢ {s3} $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "{comment2}\n\n"


    answer_dict2 = {
        0 : "㉠",
        1 : "㉡",
        2 : "㉢"
    }

    ablist=["손톱의 길이는 약 $$수식$$10 rm {{cm}}$$/수식$$입니다.", "쌀 한 톨의 길이는 약 $$수식$$6 rm {{cm}}$$/수식$$입니다.", "지우개 한 개의 길이는 약 $$수식$$5 rm {{mm}}$$/수식$$입니다.",
            "$$수식$$10$$/수식$$원짜리 동전의 두께는 약 $$수식$$1 rm {{cm}}$$/수식$$입니다.", "내 발의 길이는 약 $$수식$$230 rm {{cm}}$$/수식$$입니다.", "자의 두께는 약 $$수식$$1 rm {{cm}}$$/수식$$입니다.",
            "$$수식$$800 rm {{mm}}$$/수식$$는 $$수식$$8 rm {{cm}}$$/수식$$입니다."]

    clist = ["손톱의 너비는 약 $$수식$$10 rm {{mm}}$$/수식$$입니다.", "수학책의 두께는 약 $$수식$$6 rm {{mm}}$$/수식$$입니다.", "샤프의 길이는 약 $$수식$$15 rm {{cm}}$$/수식$$입니다.",
              "$$수식$$300 rm {{mm}}$$/수식$$는 $$수식$$30 rm {{cm}}$$/수식$$입니다."]

    delist= ["손톱의 길이는 약 $$수식$$10 rm {{mm}}$$/수식$$입니다.", "쌀 한 톨의 길이는 약 $$수식$$6 rm {{mm}}$$/수식$$입니다.", "지우개 한 개의 길이는 약 $$수식$$5 rm {{cm}}$$/수식$$입니다.",
             "$$수식$$10$$/수식$$원짜리 동전의 두께는 약 $$수식$$1 rm {{mm}}$$/수식$$입니다.", "내 발의 길이는 약 $$수식$$230 rm {{mm}}$$/수식$$입니다.", "자의 두께는 약 $$수식$$1 rm {{mm}}$$/수식$$입니다.",
             "$$수식$$800 rm {{mm}}$$/수식$$는 $$수식$$80 rm {{cm}}$$/수식$$입니다."]

    while True:
        sa = np.random.choice(ablist)
        sb = np.random.choice(ablist)
        if sa != sb:
            break

    sc = np.random.choice(clist)

    for i in range(0, 7):
        if sa == ablist[i]:
            sd = delist[i]
        elif sb == ablist[i]:
            se = delist[i]

    y1 = sa
    y2 = sb
    y3 = sc

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [s1, s2, s3] = candidates

    correct_idx = 0
    aidx = 0
    bidx = 0

    for idx, sdx in enumerate(candidates) :
        if sdx == y3 :
            correct_idx = idx
        elif sdx == y1:
            aidx = idx
        elif sdx == y2:
            bidx = idx

    a2 = answer_dict2[aidx]
    a3 = answer_dict2[bidx]

    if aidx < bidx:
        comment2 = "%s. %s\n%s. %s"%(a2, sd, a3, se)
    elif aidx > bidx:
        comment2 = "%s. %s\n%s. %s"%(a3, se, a2, sd)


    stem = stem.format(s1=s1, s2=s2, s3=s3)
    answer = answer.format(a1=answer_dict2[correct_idx])
    comment = comment.format(a1=answer_dict2[correct_idx], comment2=comment2)

    return stem, answer, comment








# 3-1-5-11
def lenandtime315_Stem_008():
    stem = "다음 중 가장 긴 길이를 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${sa} rm {{cm}} `` {sb} rm {{mm}}$$/수식$$         ㉡ $$수식$${sc} rm {{mm}}$$/수식$$\n㉢ $$수식$${sd} rm {{cm}} `` {se} rm {{mm}}$$/수식$$         ㉣ $$수식$${sf} rm {{mm}}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{sx}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${sa} rm {{cm}} `` {sb} rm {{mm}} ` = ` {sa} rm {{cm}} ` + ` {sb} rm {{mm}} ` = ` {sg} rm {{mm}} ` + ` {sb} rm {{mm}} ` = ` {sh} rm {{mm}}$$/수식$$\n" \
              "㉢ $$수식$${sd} rm {{cm}} `` {se} rm {{mm}} ` = ` {sd} rm {{cm}} ` + ` {se} rm {{mm}} ` = ` {si} rm {{mm}} ` + ` {se} rm {{mm}} ` = ` {sj} rm {{mm}}$$/수식$$\n" \
              "$$수식$${sk} rm {{mm}} ` &gt; ` {sl} rm {{mm}} ` &gt; `{sm} rm {{mm}} ` &gt; `{sn} rm {{mm}}$$/수식$$이므로 길이가 가장 긴 것은 {sx}입니다.\n\n"


    # while True:
    #     sa = np.random.randint(4, 8)
    #     sb = np.random.randint(2, 10)
    #     if sa != sb:
    #         break
    #
    # sg = sa * 10
    # sh = sg + sb
    #
    # while True:
    #     sd = [sa - 1, sa + 1][np.random.randint(0, 2)]
    #     se = np.random.randint(2, 10)
    #     if se != sb and se != sd:
    #         break
    #
    # si = sd * 10
    # sj = si + se
    #
    # while True:
    #     sc = np.random.randint(sj - 9, sj + 10)
    #     sf = np.random.randint(sh - 9, sh + 10)
    #     if sc != sj and sc != sh and sf != sh and sf != sc and sf != sj:
    #         break


    while True:
        sa = np.random.randint(4, 8)
        sb = np.random.randint(2, 10)
        sg = sa * 10
        sh = sb + sg

        sd = [sa - 1, sa + 1][np.random.randint(0, 2)]
        se = np.random.randint(2, 10)
        si = sd * 10
        sj = se + si

        sc = np.random.randint(sj - 9, sj + 10)
        sf = np.random.randint(sh - 9, sh + 10)

        if sa != sb and sb != se and sd != se and sj != sc and sh != sc and sh != sf and sc != sf and sj != sf:
            break

    hcjflist = [sh, sc, sj, sf]
    hcjflist.sort(reverse=True)

    sk = hcjflist[0]
    sl = hcjflist[1]
    sm = hcjflist[2]
    sn = hcjflist[3]

    if sk == sh:
        sx = "㉠"
    elif sk == sc:
        sx = "㉡"
    elif sk == sj:
        sx = "㉢"
    elif sk == sf:
        sx = "㉣"

    stem = stem.format(sa=sa, sb=sb, sc=sc, se=se, sd=sd, sf=sf)
    answer = answer.format(sx=sx)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sh=sh, si=si, sj=sj, sk=sk,
                             sl=sl, sm=sm, sn=sn, sx=sx)

    return stem, answer, comment






# 3-1-5-12
def lenandtime315_Stem_009():
    stem = "주어진 길이를 써 보세요.\n$$표$$    $$수식$${sa}$$/수식$$ 킬로미터    $$/표$$\n"
    answer = "(정답)\n$$수식$${sa}{sb}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$ 킬로미터는 $$수식$${sa}{sb}$$/수식$$라고 씁니다.\n\n"


    sa = np.random.randint(2, 10)
    sb = "rm {{km}}"

    stem = stem.format(sa=sa)
    answer = answer.format(sa=sa, sb=sb)
    comment = comment.format(sa=sa, sb=sb)

    return stem, answer, comment









# 3-1-5-13
def lenandtime315_Stem_010():
    stem = "□ 안에 들어갈 알맞은 수를 구하세요.\n$$수식$$LEFT ( 1 RIGHT ) ```` {sa} rm {{km}} `` {sb} rm m ` = `$$/수식$$ $$수식$${box1}$$/수식$$ $$수식$$ rm m $$/수식$$\n $$수식$$LEFT ( 2 RIGHT ) ```` {se} rm m ` = `$$/수식$$ $$수식$${box1}$$/수식$$ $$수식$$rm {{km}} ``$$/수식$$ $$수식$${box1}$$/수식$$ $$수식$$rm m$$/수식$$\n"
    answer = "(정답)\n$$수식$${sd}$$/수식$$, $$수식$${sh}$$/수식$$, $$수식$${sg}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1 RIGHT ) ```` {sa} rm {{km}} `` {sb} rm m ` = ` {sa} rm {{km}} ` + ` {sb} rm m $$/수식$$\n $$수식$$ ` = ` " \
              "{sc} rm m ` + ` {sb} rm m ` = ` {sd} rm m$$/수식$$\n" \
              "$$수식$$LEFT ( 2 RIGHT ) ```` {se} rm m ` = ` {sf} rm m ` + ` {sg} rm m$$/수식$$\n $$수식$$ ` = ` {sh} rm {{km}} ` + ` {sg} rm m $$/수식$$ $$수식$$` = ` " \
              "{sh} rm {{km}} `` {sg} rm m$$/수식$$\n\n"


    while True:
        sa = np.random.randint(2, 10)
        sb = np.random.randint(2, 10)

        e1 = np.random.randint(1, 8)
        e2 = np.random.randint(2, 10)

        if sa != sb and sa != e1 and e1 != e2 and sb != e2:
            break

    sc = sa * 1000
    sd = sb + sc

    se = e1 * 1000 + e2 * 100
    sf = e1 * 1000
    sg = e2 * 100
    sh = e1

    box1 = "box{　　　}"

    stem = stem.format(sa=sa, sb=sb, se=se, box1=box1)
    answer = answer.format(sd=sd, sh=sh, sg=sg)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sh=sh)

    return stem, answer, comment







# 3-1-5-18
def lenandtime315_Stem_011():
    stem = "길이가 $$수식$$1 rm {{km}}$$/수식$$보다 긴 것은 어느 것인가요?\n① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "{a1} {se}\n\n"


    alist = ["백두산의 높이", "한라산의 높이", "인천대교의 길이", "거가대교의 길이", "양화대교의 길이", "지리산의 높이"]

    bcdlist = ["교실의 긴 쪽의 길이", "방문의 높이", "복도의 길이", "학교의 높이", "수학책 긴 쪽의 길이", "칠판의 길이", "아파트의 높이", "버스의 길이",
               "책상 긴 쪽의 길이", "학교 운동장의 둘레"]

    elist = ["백두산의 높이는 $$수식$$2750 rm m = 2 rm {{km}} 750 rm m$$/수식$$이므로 $$수식$$1 rm {{km}}$$/수식$$보다 깁니다.",
             "한라산의 높이는 $$수식$$1950 rm m = 1 rm {{km}} 950 rm m$$/수식$$이므로 $$수식$$1 rm {{km}}$$/수식$$보다 깁니다.",
             "인천대교의 길이는 $$수식$$21380 rm m = 21 rm {{km}} 380 rm m$$/수식$$이므로 $$수식$$1 rm {{km}}$$/수식$$보다 깁니다.",
             "거가대교의 길이는 $$수식$$8200 rm m = 8 rm {{km}} 200 rm m$$/수식$$이므로 $$수식$$1 rm {{km}}$$/수식$$보다 깁니다.",
             "양화대교의 길이는 $$수식$$1053 rm m = 1 rm {{km}} 53 rm m$$/수식$$이므로 $$수식$$1 rm {{km}}$$/수식$$보다 깁니다.",
             "지리산의 높이는 $$수식$$1917 rm m = 1 rm {{km}} 917 rm m$$/수식$$이므로 $$수식$$1 rm {{km}}$$/수식$$보다 깁니다."]


    sa = np.random.choice(alist)

    while True:
        sb = np.random.choice(bcdlist)
        sc = np.random.choice(bcdlist)
        sd = np.random.choice(bcdlist)
        sf = np.random.choice(bcdlist)
        if sb != sc and sb != sd and sb != sf and sc != sd and sc != sf and sd != sf:
            break


    for i in range(0, 6):
        if sa == alist[i]:
            se = elist[i]
        elif sb == alist[i]:
            se = elist[i]

    y1 = sa
    y2 = sb
    y3 = sc
    y4 = sd
    y5 = sf

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
    comment = comment.format(a1=answer_dict[correct_idx], se=se)

    return stem, answer, comment








# 3-1-5-20
def lenandtime315_Stem_012():
    stem = "주어진 길이를 선택하여 문장을 완성하려고 합니다. □ 안에 알맞은 길이를 찾아 써 보세요.\n$$표$$      {sa1}      {sb1}      {sc1}      $$/표$$\n→ {s1}에서 {s2}까지의 거리는 약 $$수식$${box}$$/수식$$입니다.\n"
    answer = "(정답)\n{sa}\n"
    comment = "(해설)\n" \
              "{s1}에서 {s2}까지의 거리로 알맞은 것은 {sa}입니다.\n\n"


    s1 = ["서울", "부산", "광주", "대전"][np.random.randint(0, 4)]

    if s1 == "서울":
        s2 = ["수원", "광주", "대구", "경주", "부산", "강릉"][np.random.randint(0, 6)]
        if s2 == "수원":
            sa = "$$수식$$45 rm {{km}}$$/수식$$"
        elif s2 == "광주":
            sa = "$$수식$$296 rm {{km}}$$/수식$$"
        elif s2 == "대구":
            sa = "$$수식$$232 rm {{km}}$$/수식$$"
        elif s2 == "경주":
            sa = "$$수식$$340 rm {{km}}$$/수식$$"
        elif s2 == "부산":
            sa = "$$수식$$417 rm {{km}}$$/수식$$"
        elif s2 == "강릉":
            sa = "$$수식$$240 rm {{km}}$$/수식$$"

    elif s1 == "부산":
        s2 = ["경주", "광주"][np.random.randint(0, 2)]
        if s2 == "경주":
            sa = "$$수식$$85 rm {{km}}$$/수식$$"
        elif s2 == "광주":
            sa = "$$수식$$263 rm {{km}}$$/수식$$"

    elif s1 == "광주":
        s2 = "목포"
        sa = "$$수식$$74 rm {{km}}$$/수식$$"

    elif s1 == "대전":
        s2 = ["광주", "부산"][np.random.randint(0, 2)]
        if s2 == "광주":
            sa = "$$수식$$168 rm {{km}}$$/수식$$"
        elif s2 == "부산":
            sa = "$$수식$$258 rm {{km}}$$/수식$$"

    bclist = ["$$수식$$5 rm {{cm}} ```` 3 rm {{mm}}$$/수식$$", "$$수식$$450 rm m$$/수식$$", "$$수식$$11 rm {{cm}} ```` 8 rm {{mm}}$$/수식$$",
              "$$수식$$208 rm m$$/수식$$", "$$수식$$16 rm {{cm}} ```` 5 rm {{mm}}$$/수식$$", "$$수식$$74 rm m$$/수식$$",
              "$$수식$$26 rm {{cm}} ```` 7 rm {{mm}}$$/수식$$", "$$수식$$258 rm m$$/수식$$",
              "$$수식$$9 rm {{cm}} ```` 4 rm {{mm}}$$/수식$$", "$$수식$$340 rm m$$/수식$$"]

    while True:
        sb = np.random.choice(bclist)
        sc = np.random.choice(bclist)
        if sc != sb:
            break

    candidates = [sa, sb, sc]
    np.random.shuffle(candidates)
    [sa1, sb1, sc1] = candidates

    box = "box{　　　}"

    stem = stem.format(sa1=sa1, sb1=sb1, sc1=sc1, box=box, s1=s1, s2=s2)
    answer = answer.format(sa=sa)
    comment = comment.format(s1=s1, s2=s2, sa=sa)

    return stem, answer, comment









# 3-1-5-24
def lenandtime315_Stem_013():
    stem = "□ 안에 들어갈 알맞은 수를 구하세요.\n$$수식$$LEFT ( 1 RIGHT ) ```` {sa}$$/수식$$분 $$수식$${sb}$$/수식$$초 $$수식$$ `=` $$/수식$$ $$수식$${box1}$$/수식$$초\n$$수식$$LEFT ( 2 RIGHT ) ```` {se}$$/수식$$초 $$수식$$ `=` $$/수식$$ $$수식$${box1}$$/수식$$분 $$수식$${box1}$$/수식$$초\n"
    answer = "(정답)\n$$수식$${sd}$$/수식$$, $$수식$${sh}$$/수식$$, $$수식$${sg}$$/수식$$\n"
    comment = "(해설)\n" \
             "$$수식$$LEFT ( 1 RIGHT ) ```` {sa}$$/수식$$분 $$수식$${sb}$$/수식$$초 $$수식$$= ` {sa}$$/수식$$분 " \
              "$$수식$$+ ` {sb}$$/수식$$초 $$수식$$= ` {sc}$$/수식$$초 $$수식$$+ ` {sb}$$/수식$$초 $$수식$$= ` {sd}$$/수식$$초\n" \
             "$$수식$$LEFT ( 2 RIGHT ) ```` {se}$$/수식$$초 $$수식$$= ` {sf}$$/수식$$초 $$수식$$+ ` {sg}$$/수식$$초 " \
              "$$수식$$= ` {sh}$$/수식$$분 $$수식$$+ ` {sg}$$/수식$$초 $$수식$$= ` {sh}$$/수식$$분 $$수식$${sg}$$/수식$$초\n\n"


    sa = np.random.randint(1, 10)

    while True:
        sb = np.random.randint(5, 56)
        if sb % 5 == 0:
            break

    sc = sa * 60
    sd = sc + sb

    sh = np.random.randint(1, 6)

    while True:
        sg = np.random.randint(5, 56)
        if sg % 5 == 0:
            break

    sf = sh * 60
    se = sf + sg

    box1 = "box{　　　}"

    stem = stem.format(sa=sa, sb=sb, se=se, box1=box1)
    answer = answer.format(sd=sd, sh=sh, sg=sg)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sh=sh)

    return stem, answer, comment









# 3-1-5-27
def lenandtime315_Stem_014():
    stem = "보기와 같이 □ 안에 알맞은 시간의 단위를 써 보세요.\n$$표$${bogi1}$$/표$$\n$$수식$$LEFT ( 1 RIGHT )$$/수식$$ $$수식$${sa1}$$/수식$$ $$수식$${box1}$$/수식$$\n$$수식$$LEFT ( 2 RIGHT )$$/수식$$ $$수식$${sb1}$$/수식$$ $$수식$${box1}$$/수식$$\n$$수식$$LEFT ( 3 RIGHT )$$/수식$$ $$수식$${sc1}$$/수식$$ $$수식$${box1}$$/수식$$\n"
    answer = "(정답)\n{se}, {sf}, {sg}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1 RIGHT )$$/수식$$ {sh}\n" \
              "$$수식$$LEFT ( 2 RIGHT )$$/수식$$ {si}\n" \
              "$$수식$$LEFT ( 3 RIGHT )$$/수식$$ {sj}\n\n"


    alist = ["손을 씻는 시간은 짧으므로: $$수식$$15", "신호등이 켜져 있는 시간: $$수식$$30", "물 한 잔을 마는 시간: $$수식$$10", "$$수식$$60 rm m$$/수식$$를 달리는 데 걸리는 시간: $$수식$$14"]

    blist = ["$$수식$$1$$/수식$$교시 수업 시간: $$수식$$40", "집에서 학교까지 가는 데 걸리는 시간: $$수식$$15", "양치질 하는 시간: $$수식$$3", "음악 한 곡을 듣는 시간: $$수식$$5"]

    clist = ["하루에 잠을 자는 시간: $$수식$$8", "영화 한 편을 보는 시간: $$수식$$2", "등산하는 데 걸리는 시간: $$수식$$4", "숙제하는 시간: $$수식$$1"]

    abclist = ["손을 씻는 시간은 짧으므로: $$수식$$15", "신호등이 켜져 있는 시간: $$수식$$30", "물 한 잔을 마는 시간: $$수식$$10", "$$수식$$60 rm m$$/수식$$를 달리는 데 걸리는 시간: $$수식$$14",
               "$$수식$$1$$/수식$$교시 수업 시간: $$수식$$40", "집에서 학교까지 가는 데 걸리는 시간: $$수식$$15", "양치질 하는 시간: $$수식$$3", "음악 한 곡을 듣는 시간: $$수식$$5",
               "하루에 잠을 자는 시간: $$수식$$8", "영화 한 편을 보는 시간: $$수식$$2", "등산하는 데 걸리는 시간: $$수식$$4", "숙제하는 시간: $$수식$$1"]

    sa = np.random.choice(alist)
    sb = np.random.choice(blist)
    sc = np.random.choice(clist)

    abc1list = ["손을 씻는 시간은 짧으므로 $$수식$$15$$/수식$$초입니다.", "신호등이 켜져 있는 시간은 짧으므로 $$수식$$30$$/수식$$초입니다.",
                "물 한 잔을 마는 시간은 짧으므로 $$수식$$10$$/수식$$초입니다.", "$$수식$$60 rm m$$/수식$$를 달리는 데 걸리는 시간은 짧으므로 $$수식$$14$$/수식$$초입니다.",
                "$$수식$$1$$/수식$$교시 수업 시간은 $$수식$$40$$/수식$$분이 알맞습니다.", "집에서 학교까지 가는 데 걸리는 시간은 $$수식$$15$$/수식$$분이 알맞습니다.",
                "양치질 하는 시간은 $$수식$$3$$/수식$$분이 알맞습니다.", "음악 한 곡을 듣는 시간은 $$수식$$5$$/수식$$분이 알맞습니다.",
                "하루에 잠을 자는 시간은 긴 시간이므로 $$수식$$8$$/수식$$시간이 알맞습니다.", "영화 한 편을 보는 시간은 긴 시간이므로 $$수식$$2$$/수식$$시간이 알맞습니다.",
                "등산하는 데 걸리는 시간은 긴 시간이므로 $$수식$$4$$/수식$$시간이 알맞습니다.", "숙제하는 시간은 긴 시간이므로 $$수식$$1$$/수식$$시간이 알맞습니다."]


    candidates = [sa, sb, sc]
    np.random.shuffle(candidates)
    [sa1, sb1, sc1] = candidates

    se = "초"
    sf = "분"
    sg = "시간"

    for i in range(0, 12):
        if sa1 == abclist[i]:
            sh = abc1list[i]
            break

    for i in range(0, 12):
        if sb1 == abclist[i]:
            si = abc1list[i]
            break

    for i in range(0, 12):
        if sc1 == abclist[i]:
            sj = abc1list[i]
            break

    if sa1 in alist and sb1 in blist and sc1 in clist:
        se = "초"
        sf = "분"
        sg = "시간"

    elif sa1 in alist and sb1 in clist and sc1 in blist:
        se = "초"
        sf = "시간"
        sg = "분"

    elif sa1 in blist and sb1 in alist and sc1 in clist:
        se = "분"
        sf = "초"
        sg = "시간"

    elif sa1 in blist and sb1 in clist and sc1 in alist:
        se = "분"
        sf = "시간"
        sg = "초"

    elif sa1 in clist and sb1 in alist and sc1 in blist:
        se = "시간"
        sf = "초"
        sg = "분"

    elif sa1 in clist and sb1 in blist and sc1 in alist:
        se = "시간"
        sf = "분"
        sg = "초"


    box1 = "box{　　　}"

    bogi = ["점심 식사를 하는 시간: $$수식$$20$$/수식$$분", "지하철을 타고 한 정거장을 가는데\n 걸리는 시간: $$수식$$4$$/수식$$분",
            "컴퓨터가 켜지는 시간: $$수식$$30$$/수식$$초", "기차를 타고 서울에서 부산까지 가는데\n 걸리는 시간: $$수식$$3$$/수식$$시간"]

    bogi1 = np.random.choice(bogi)

    stem = stem.format(sa1=sa1, sb1=sb1, sc1=sc1, box1=box1, bogi1=bogi1)
    answer = answer.format(se=se, sf=sf, sg=sg)
    comment = comment.format(sh=sh, si=si, sj=sj)

    return stem, answer, comment










# 3-1-5-28
def lenandtime315_Stem_015():
    stem = "{p1}와 {p2}는 $$수식$$500 rm m$$/수식$$ 달리기를 했습니다. {p1}의 기록은 $$수식$${sa}$$/수식$$초, {p2}의 기록은 $$수식$${sb}$$/수식$$분 $$수식$${sc}$$/수식$$초였습니다. 기록이 더 좋은 사람은 누구인가요?\n"
    answer = "(정답)\n{p3}\n"
    comment = "(해설)\n" \
              "$$수식$${sb}$$/수식$$분 $$수식$${sc}$$/수식$$초 $$수식$$= ` {sb}$$/수식$$분 $$수식$$+ ` {sc}$$/수식$$초 " \
              "$$수식$$= ` {sd}$$/수식$$초 $$수식$$+ ` {sc}$$/수식$$초 $$수식$$= ` {se}초$$/수식$$\n" \
              "따라서 $$수식$${sa} ` {sx} ` {se}$$/수식$$이므로 기록이 더 좋은 사람은 {p3}입니다.\n\n"


    splist = ["수미", "현수", "채아", "유주", "지호", "연아", "은우", "시우", "혁재", "진아", "영서", "승태", "민지", "선규"]

    while True:
        p1 = np.random.choice(splist)
        p2 = np.random.choice(splist)
        if p1 != p2:
            break

    sb = np.random.randint(2, 4)
    sc = np.random.randint(2, 60)
    sd = sb * 60
    se = sd + sc

    while True:
        sa = np.random.randint(se - 20, se + 21)
        if sa != se and sa % 10 != 0:
            break

    if sa > se:
        sx = "&gt;"
        p3 = p2
    elif sa < se:
        sx = "&lt;"
        p3 = p1

    stem = stem.format(p1=p1, p2=p2, sa=sa, sb=sb, sc=sc)
    answer = answer.format(p3=p3)
    comment = comment.format(p3=p3, sa=sa, sb=sb, sc=sc, sd=sd, se=se, sx=sx)

    return stem, answer, comment










# 3-1-5-29
def lenandtime315_Stem_016():
    stem = "㉠과 ㉡ 일을 하는 데 걸린 시간입니다. 시간이 더 오래 걸린 일은 무엇인지 기호를 쓰세요.\n$$표$$㉠ $$수식$${sa}$$/수식$$분 $$수식$${sb}$$/수식$$초      ㉡ $$수식$${se}$$/수식$$초$$/표$$\n"
    answer = "(정답)\n{sy}\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$분 $$수식$${sb}$$/수식$$초 $$수식$$= ` {sa}$$/수식$$분 $$수식$$+ ` {sb}$$/수식$$초 " \
              "$$수식$$= ` {sc}$$/수식$$초 $$수식$$+ ` {sb}$$/수식$$초 $$수식$$= ` {sd}$$/수식$$초\n" \
              "따라서 $$수식$${sd} ` {sx} ` {se}$$/수식$$이므로 시간이 더 오래 걸린 일은 {sy}입니다.\n\n"


    sa = np.random.randint(4, 9)
    sb = np.random.randint(2, 60)
    sc = sa * 60
    sd = sb + sc

    while True:
        se = np.random.randint(sd - 30, sd + 31)
        if se != sd and sa % 10 != 0:
            break

    if sd > se:
        sx = "&gt;"
        sy = "㉠"

    elif sd < se:
        sx = "&lt;"
        sy = "㉡"

    stem = stem.format(sa=sa, sb=sb, se=se)
    answer = answer.format(sy=sy)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sx=sx, sy=sy)

    return stem, answer, comment








# 3-1-5-32
def lenandtime315_Stem_017():
    stem = "$$수식$${sa}$$/수식$$시 $$수식$${sb}$$/수식$$분 $$수식$${sc}$$/수식$$초에서 $$수식$${sd}$$/수식$$초 후의 시각을 구해 보세요.\n{box1} 시 {box1} 분 {box1} 초\n"
    answer = "(정답)\n$$수식$${sa}$$/수식$$, $$수식$${sf}$$/수식$$, $$수식$${sg}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$시 $$수식$${sb}$$/수식$$분 $$수식$${sc}$$/수식$$초 $$수식$$+ ` {sd}$$/수식$$초 " \
              "$$수식$$= ` {sa}$$/수식$$시 $$수식$${sb}$$/수식$$분 $$수식$${se}$$/수식$$초\n" \
              "$$수식$$60$$/수식$$초 $$수식$$= ` 1$$/수식$$분이므로 분 단위로 받아올림하면 $$수식$${sa}$$/수식$$시 $$수식$${sf}$$/수식$$분 $$수식$${sg}$$/수식$$초입니다.\n\n"


    sa = np.random.randint(2, 10)
    sb = np.random.randint(11, 59)
    sc = np.random.randint(21, 60)

    while True:
        sd = np.random.randint(5, 46)
        if 61 <= sc + sd:
            break

    se = sc + sd
    sf = sb + 1
    sg = se - 60

    box1 = "$$수식$$box{　　　}$$/수식$$"

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, box1=box1)
    answer = answer.format(sa=sa, sf=sf, sg=sg)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg)

    return stem, answer, comment







# 3-1-5-34
def lenandtime315_Stem_018():
    stem = "시간의 길이가 더 긴 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${a1}$$/수식$$시간 $$수식$${a2}$$/수식$$분 $$수식$${a3}$$/수식$$초 $$수식$$+ {b1}$$/수식$$시간 $$수식$${b2}$$/수식$$분 $$수식$${b3}$$/수식$$초\n㉡ $$수식$${c1}$$/수식$$시간 $$수식$${c2}$$/수식$$분 $$수식$${c3}$$/수식$$초 $$수식$$+ {d1}$$/수식$$시간 $$수식$${d2}$$/수식$$분 $$수식$${d3}$$/수식$$초$$/표$$\n"
    answer = "(정답)\n{sy}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${a1}$$/수식$$시간 $$수식$${a2}$$/수식$$분 $$수식$${a3}$$/수식$$초 $$수식$$+ {b1}$$/수식$$시간 $$수식$${b2}$$/수식$$분 $$수식$${b3}$$/수식$$초\n" \
              "$$수식$$= ` {sa}$$/수식$$시간 $$수식$${sb}$$/수식$$분 $$수식$${sc}$$/수식$$초 $$수식$$= ` {sd}$$/수식$$시간 $$수식$${se}$$/수식$$분 $$수식$${sf}$$/수식$$초\n" \
              "㉡ $$수식$${c1}$$/수식$$시간 $$수식$${c2}$$/수식$$분 $$수식$${c3}$$/수식$$초 $$수식$$+ {d1}$$/수식$$시간 $$수식$${d2}$$/수식$$분 $$수식$${d3}$$/수식$$초\n" \
              "$$수식$$= ` {sg}$$/수식$$시간 $$수식$${sh}$$/수식$$분 $$수식$${si}$$/수식$$초 $$수식$$= ` {sj}$$/수식$$시간 $$수식$${sk}$$/수식$$분 $$수식$${sl}$$/수식$$초\n" \
              "따라서 $$수식$${sd}$$/수식$$시간 $$수식$${se}$$/수식$$분 $$수식$${sf}$$/수식$$초 $$수식$${sx} ` {sj}$$/수식$$시간 $$수식$${sk}$$/수식$$분 $$수식$${sl}$$/수식$$초이므로 " \
              "시간의 길이가 더 긴 것은 {sy}입니다.\n\n"


    while True:
        a1 = np.random.randint(2, 6)
        b1 = np.random.randint(1, 7)
        a2 = np.random.randint(11, 59)
        b2 = np.random.randint(5, 59)
        a3 = np.random.randint(11, 59)
        b3 = np.random.randint(5, 59)

        c1 = np.random.randint(2, 6)
        d1 = np.random.randint(1, 7)
        c2 = np.random.randint(11, 59)
        d2 = np.random.randint(5, 59)
        c3 = np.random.randint(11, 59)
        d3 = np.random.randint(5, 59)

        sa = a1 + b1
        sb = a2 + b2
        sc = a3 + b3
        sd = sa + 1
        se = sb - 60 + 1
        sf = sc - 60

        sg = c1 + d1
        sh = c2 + d2
        si = c3 + d3
        sj = sg + 1
        sk = sh - 60 + 1
        sl = si - 60

        if a1+b1 <= 8 and 61 <= a2+b2 and b2 != a2 and 61 <= a3+b3 and b3 != a3 and c1 != a1 and d1 != b1 and c1+d1 == a1+b1 and \
                61 <= c2+d2 and sb-2 <= c2+d2 and c2+d2 <= sb+2 and c2+d2 != sb and 61 <= c3+d3 and sc-2 <= c3+d3 and c3+d3 <= sc+2 and c3+d3 != sc and se != sk:
            break

    if se > sk:
        sx = "&gt;"
        sy="㉠"
    elif se < sk:
        sx = "&lt;"
        sy="㉡"

    stem = stem.format(a1=a1, b1=b1, c1=c1, a2=a2, b2=b2, c2=c2, a3=a3, b3=b3, c3=c3, d1=d1, d2=d2, d3=d3)
    answer = answer.format(sy=sy)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sh=sh, si=si, sj=sj, sk=sk, sl=sl, sx=sx, sy=sy, a1=a1, b1=b1, c1=c1, a2=a2, b2=b2, c2=c2, a3=a3, b3=b3, c3=c3, d1=d1, d2=d2, d3=d3)

    return stem, answer, comment






# 3-1-5-35
def lenandtime315_Stem_019():
    stem = "현재 시간은 $$수식$${a1}$$/수식$$시 $$수식$${a2}$$/수식$$분 $$수식$${a3}$$/수식$$초입니다. $$수식$${b1}$$/수식$$시간 $$수식$${b2}$$/수식$$분 $$수식$${b3}$$/수식$$초 후는 몇 시 몇 분 몇 초인가요?\n" \
        "{boxblank} 시 {boxblank} 분 {boxblank} 초"
    answer = "(정답)\n$$수식$${sa}$$/수식$$, $$수식$${sd}$$/수식$$, $$수식$${se}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a1}$$/수식$$시 $$수식$${a2}$$/수식$$분 $$수식$${a3}$$/수식$$초 $$수식$$+ ` {b1}$$/수식$$시간 $$수식$${b2}$$/수식$$분 $$수식$${b3}$$/수식$$초 " \
              "$$수식$$= ` {sa}$$/수식$$시 $$수식$${sd}$$/수식$$분 $$수식$${se}$$/수식$$초\n\n"

    boxblank = "$$수식$$BOX{　　}$$/수식$$"

    while True:
        a1 = np.random.randint(1, 8)
        b1 = np.random.randint(1, 8)
        if a1 + b1 <= 9:
            break

    while True:
        a2 = np.random.randint(2, 57)
        b2 = np.random.randint(2, 57)
        if a2 + b2 <= 58 and b2 != a2:
            break

    while True:
        a3 = np.random.randint(3, 60)
        b3 = np.random.randint(3, 60)
        if 61 <= a3 + b3 and b3 != a3:
            break

    sa = a1 + b1
    sb = a2 + b2
    sc = a3 + b3
    sd = sb + 1
    se = sc - 60

    stem = stem.format(a1=a1, b1=b1, a3=a3, a2=a2, b2=b2, b3=b3, boxblank=boxblank)
    answer = answer.format(sa=sa, sd=sd, se=se)
    comment = comment.format(a1=a1, b1=b1, a3=a3, a2=a2, b2=b2, b3=b3, sa=sa, sd=sd, se=se)

    return stem, answer, comment







# 3-1-5-36
def lenandtime315_Stem_020():
    stem = "{pp}이는 $$수식$${a1}$$/수식$$시 $$수식$${a2}$$/수식$$분 $$수식$${a3}$$/수식$$초에 {ss}를 시작했습니다. {ss}를 $$수식$${b2}$$/수식$$분 $$수식$${b3}$$/수식$$초 동안 했다면 {ss}를 끝낸 시각은 몇 시 몇 분 몇 초인가요?\n" \
        "{boxblank} 시 {boxblank} 분 {boxblank} 초"
    answer = "(정답)\n$$수식$${sa}$$/수식$$, $$수식$${sb}$$/수식$$, $$수식$${sc}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a1}$$/수식$$시 $$수식$${a2}$$/수식$$분 $$수식$${a3}$$/수식$$초 $$수식$$+ ` {b2}$$/수식$$분 $$수식$${b3}$$/수식$$초 " \
              "$$수식$$= ` {sa}$$/수식$$시 $$수식$${sb}$$/수식$$분 $$수식$${sc}$$/수식$$초\n\n"

    boxblank = "$$수식$$BOX{　　}$$/수식$$"

    pp = ["서준", "민영", "혁진", "혜란", "도윤", "주현", "자연", "재령", "민준", "상현", "영웅", "정윤", "수빈", "휘진"][np.random.randint(0, 14)]
    ss = ["샤워", "세수", "머리 감기"][np.random.randint(0, 3)]

    a1 = 7
    a2 = np.random.randint(57, 60)
    b2 = np.random.randint(2, 5)

    while True:
        a3 = np.random.randint(3, 60)
        b3 = np.random.randint(3, 60)
        if 61 <= a3 + b3 and b3 != a3:
            break

    sa = a1 + 1
    sb = a2 + b2 + 1 - 60
    sc = a3 + b3 - 60

    stem = stem.format(pp=pp, ss=ss, a1=a1, a3=a3, a2=a2, b2=b2, b3=b3, boxblank=boxblank)
    answer = answer.format(sa=sa, sb=sb, sc=sc)
    comment = comment.format(a1=a1, a3=a3, a2=a2, b2=b2, b3=b3, sa=sa, sb=sb, sc=sc)

    return stem, answer, comment








# 3-1-5-42
def lenandtime315_Stem_021():
    stem = "시간의 길이가 더 짧은 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${a2}$$/수식$$분 $$수식$${a3}$$/수식$$초 $$수식$$- ```` {b2}$$/수식$$분 $$수식$${b3}$$/수식$$초\n㉡ $$수식$${c2}$$/수식$$분 $$수식$${c3}$$/수식$$초 $$수식$$- ```` {d2}$$/수식$$분 $$수식$${d3}$$/수식$$초$$/표$$\n"
    answer = "(정답)\n{sy}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${a2}$$/수식$$분 $$수식$${a3}$$/수식$$초 $$수식$$- ```` {b2}$$/수식$$분 $$수식$${b3}$$/수식$$초 " \
              "$$수식$$= ` {sa}$$/수식$$분 $$수식$${sb}$$/수식$$초\n" \
              "㉡ $$수식$${c2}$$/수식$$분 $$수식$${c3}$$/수식$$초 $$수식$$- ```` {d2}$$/수식$$분 $$수식$${d3}$$/수식$$초 " \
              "$$수식$$= ` {sc}$$/수식$$분 $$수식$${sd}$$/수식$$초\n" \
              "따라서 $$수식$${sa}$$/수식$$분 $$수식$${sb}$$/수식$$초 $$수식$${sx} ```` {sc}$$/수식$$분 $$수식$${sd}$$/수식$$초이므로 " \
              "시간의 길이가 더 짧은 것은 {sy}입니다.\n\n"


    while True:
        a2 = np.random.randint(10, 26)
        b2 = np.random.randint(3, 10)
        a3 = np.random.randint(11, 40)
        b3 = np.random.randint(15, 60)

        c2 = np.random.randint(30, 59)
        d2 = np.random.randint(20, 41)
        c3 = np.random.randint(11, 59)
        d3 = np.random.randint(5, 56)

        sa = a2 - b2 - 1
        sb = 60 + a3 - b3
        sc = c2 - d2
        sd = c3 - d3

        if a3 + 1 <= b3 and d2 + 1 <= c2 and 1 <= c3 - d3 and c3 - d3 <= 19 and c3 != a3 and sb != sd:
            if (c2 - d2 == a2 - b2) or (c2 - d2 == a2 - b2 - 1):
                break

    sx = ""
    sy = ""

    if sa > sc:
        sx = "&gt;"
        sy = "㉡"
    elif sa == sc and sb > sd:
        sx = "&gt;"
        sy = "㉡"
    elif sa < sc:
        sx = "&lt;"
        sy = "㉠"
    elif sa == sc and sb < sd:
        sx = "&lt;"
        sy = "㉠"

    stem = stem.format(a2=a2, b2=b2, c2=c2, d2=d2, a3=a3, b3=b3, c3=c3, d3=d3)
    answer = answer.format(sy=sy)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, sx=sx, sy=sy, a2=a2, b2=b2, c2=c2, a3=a3, b3=b3, c3=c3, d2=d2, d3=d3)

    return stem, answer, comment









# 3-1-5-46
def lenandtime315_Stem_022():
    stem = "{pp}가 숙제를 끝낸 시각은 $$수식$${a1}$$/수식$$시 $$수식$${a2}$$/수식$$분입니다. {pp}가 $$수식$${b1}$$/수식$$시간 $$수식$${b2}$$/수식$$분 동안 숙제를 했다면 숙제를 시작한 시각은 몇 시 몇 분인가요?\n" \
        "{boxblank} 시 {boxblank} 분"
    answer = "(정답)\n$$수식$${sa}$$/수식$$, $$수식$${sb}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$숙제를 시작한 시각$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$숙제를 끝낸 시각$$수식$$RIGHT ) ```` - ```` LEFT ($$/수식$$숙제를 하는 데 걸린 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {a1}$$/수식$$시 $$수식$${a2}$$/수식$$분 $$수식$$- ```` {b1}$$/수식$$시간 $$수식$${b2}$$/수식$$분 $$수식$$= ` {sa}$$/수식$$시 $$수식$${sb}$$/수식$$분\n\n"

    boxblank = "$$수식$$BOX{　　}$$/수식$$"
    
    pp = ["수미", "현수", "채아", "민주", "지호", "연아", "은우", "시우", "혁재", "민아", "영서", "승태", "민지", "선규"][np.random.randint(0, 14)]

    while True:
        a1 = np.random.randint(3, 8)
        b1 = np.random.randint(1, 3)
        sa = a1 - b1 - 1
        if sa > 0:
            break

    while True:
        a2 = np.random.randint(11, 40)
        b2 = np.random.randint(15, 60)
        if a2 + 1 < b2:
            break

    sb = 60 + a2 - b2

    stem = stem.format(pp=pp, a1=a1, a2=a2, b1=b1, b2=b2, boxblank=boxblank)
    answer = answer.format(sa=sa, sb=sb)
    comment = comment.format(a1=a1, a2=a2, b1=b1, b2=b2, sa=sa, sb=sb)

    return stem, answer, comment








# 3-1-5-47
def lenandtime315_Stem_023():
    stem = "다음을 보고 {pp}가 {ss}를 시작한 시각은 몇 시 몇 분 몇 초인지 구해 보세요.\n$$표$$$$수식$$LEFT [$$/수식$${pp}$$수식$$RIGHT ]$$/수식$$ 지금 시각은 $$수식$${a1}$$/수식$$시 $$수식$${a2}$$/수식$$분 $$수식$${a3}$$/수식$$초이고\n $$수식$${b1}$$/수식$$시 $$수식$${b2}$$/수식$$분 $$수식$${b3}$$/수식$$초 전부터 {ss}를 했어.$$/표$$\n" \
        "{boxblank} 시 {boxblank} 분 {boxblank} 초"
    answer = "(정답)\n$$수식$${sd}$$/수식$$, $$수식$${se}$$/수식$$, $$수식$${sf}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${ss}를 시작한 시각$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {a1}$$/수식$$시 $$수식$${a2}$$/수식$$분 $$수식$${a3}$$/수식$$초 $$수식$$- ```` {b1}$$/수식$$시간 $$수식$${b2}$$/수식$$분 $$수식$${b3}$$/수식$$초\n" \
              "$$수식$$= ` {sa}$$/수식$$시 $$수식$${sb}$$/수식$$분 $$수식$${sc}$$/수식$$초 $$수식$$- ```` {b1}$$/수식$$시간 $$수식$${b2}$$/수식$$분 $$수식$${b3}$$/수식$$초\n" \
              "$$수식$$= ` {sd}$$/수식$$시 $$수식$${se}$$/수식$$분 $$수식$${sf}$$/수식$$초\n\n"

    boxblank = "$$수식$$BOX{　　}$$/수식$$"
     
    pp = ["찬호", "민호", "수미", "현수", "채아", "민주", "지호", "연아", "은우", "시우", "혁재", "민아", "영서", "승태", "민지", "선규"][np.random.randint(0, 16)]
    ss = ["야구", "농구", "배구", "축구"][np.random.randint(0, 4)]

    a1 = np.random.randint(5, 8)
    b1 = np.random.randint(1, 3)

    while True:
        a2 = np.random.randint(11, 30)
        b2 = np.random.randint(15, 46)
        a3 = np.random.randint(11, 30)
        b3 = np.random.randint(15, 46)

        if (a2 + 1 <= b2) and (a3 + 1 <= b3) and (a3 != a2):
            break

    sa = a1 - 1
    sb = 60 + a2 - 1
    sc = 60 + a3
    sd = sa - b1
    se = sb - b2
    sf = sc - b3

    stem = stem.format(pp=pp, ss=ss, a1=a1, a3=a3, a2=a2, b1=b1, b2=b2, b3=b3, boxblank=boxblank)
    answer = answer.format(sd=sd, se=se, sf=sf)
    comment = comment.format(ss=ss, a1=a1, a3=a3, a2=a2, b1=b1, b2=b2, b3=b3, sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf)

    return stem, answer, comment










# 3-1-5-48
def lenandtime315_Stem_024():
    stem = "어느 날 해가 뜬 시각은 오전 $$수식$${a1}$$/수식$$시 $$수식$${a2}$$/수식$$분 $$수식$${a3}$$/수식$$초이고 해가 진 시각은 오후 $$수식$${b1}$$/수식$$시 $$수식$${b2}$$/수식$$분 $$수식$${b3}$$/수식$$초입니다. 이날 낮의 길이는 몇 시간 몇 분 몇 초인가요?\n" \
        "{boxblank} 시 {boxblank} 분 {boxblank} 초"
    answer = "(정답)\n$$수식$${sa}$$/수식$$, $$수식$${sb}$$/수식$$, $$수식$${sc}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$해가 뜬 시각부터 정오까지의 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` 12$$/수식$$시 $$수식$$- ```` {a1}$$/수식$$시 $$수식$${a2}$$/수식$$분 $$수식$${a3}$$/수식$$초\n" \
              "$$수식$$= ` 11$$/수식$$시 $$수식$$59$$/수식$$분 $$수식$$60$$/수식$$초 $$수식$$- ```` {a1}$$/수식$$시 $$수식$${a2}$$/수식$$분 $$수식$${a3}$$/수식$$초\n" \
              "$$수식$$= ` {c1}$$/수식$$시간 $$수식$${c2}$$/수식$$분 $$수식$${c3}$$/수식$$초\n" \
              "$$수식$$LEFT ($$/수식$$낮의 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$해가 뜬 시각부터 정오까지의 시간$$수식$$RIGHT ) ```` + ```` LEFT ($$/수식$$정오부터 해가 진 시각까지의 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${c1}$$/수식$$시간 $$수식$${c2}$$/수식$$분 $$수식$${c3}$$/수식$$초 $$수식$$+ ```` {b1}$$/수식$$시 $$수식$${b2}$$/수식$$분 $$수식$${b3}$$/수식$$초\n" \
              "$$수식$$= ` {sa}$$/수식$$시간 $$수식$${sb}$$/수식$$분 $$수식$${sc}$$/수식$$초\n\n"

    boxblank = "$$수식$$BOX{　　}$$/수식$$"

    while True:
        a1 = np.random.randint(5, 8)
        a2 = np.random.randint(5, 26)
        a3 = np.random.randint(5, 26)

        if a2 != a3:
            break

    c1 = 11 - a1
    c2 = 59 - a2
    c3 = 60 - a3

    if a1 == 5:
        b1 = 8
    elif a1 == 6:
        b1 = 7
    elif a1 == 7:
        b1 = 6

    while True:
        b2 = np.random.randint(11, 59)
        b3 = np.random.randint(11, 59)
        if (61 - c2 <= b2) and (61 - c3 <= b3):
            break

    sa = c1 + b1 + 1
    sb = 1 + c2 + b2 - 60
    sc = c3 + b3 - 60

    stem = stem.format(a1=a1, a3=a3, a2=a2, b1=b1, b2=b2, b3=b3, boxblank=boxblank)
    answer = answer.format(sa=sa, sb=sb, sc=sc)
    comment = comment.format(a1=a1, a3=a3, a2=a2, b1=b1, b2=b2, b3=b3, sa=sa, sb=sb, sc=sc, c1=c1, c2=c2, c3=c3)

    return stem, answer, comment










# 3-1-5-49
def lenandtime315_Stem_025():
    stem = "어떤 시각에서 $$수식$${a1}$$/수식$$시각 $$수식$${a2}$$/수식$$분 후의 시간을 구해야 하는데 잘못하여 $$수식$${a1}$$/수식$$시각 $$수식$${a2}$$/수식$$분 전의 시간을 구했더니 $$수식$${b1}$$/수식$$시 $$수식$${b2}$$/수식$$분 $$수식$${b3}$$/수식$$초였습니다. 바르게 구한 시각은 몇 시 몇 분 몇 초인가요?\n" \
        "{boxblank} 시 {boxblank} 분 {boxblank} 초"
    answer = "(정답)\n$$수식$${sa}$$/수식$$, $$수식$${sb}$$/수식$$, $$수식$${sc}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 시각을 □라 하면\n" \
              "□$$수식$$- ` {a1}$$/수식$$시간 $$수식$${a2}$$/수식$$분$$수식$$= ` {b1}$$/수식$$시 $$수식$${b2}$$/수식$$분 $$수식$${b3}$$/수식$$초,\n" \
              "□$$수식$$= ` {b1}$$/수식$$시 $$수식$${b2}$$/수식$$분 $$수식$${b3}$$/수식$$초$$수식$$+ ` {a1}$$/수식$$시 $$수식$${a2}$$/수식$$분" \
              "$$수식$$= ` {c1}$$/수식$$시 $$수식$${c2}$$/수식$$분 $$수식$${c3}$$/수식$$초에서\n" \
              "어떤 시각은 $$수식$${c1}$$/수식$$시 $$수식$${c2}$$/수식$$분 $$수식$${c3}$$/수식$$초입니다.\n" \
              "따라서 바르게 구한 시각은\n" \
              "$$수식$${c1}$$/수식$$시간 $$수식$${c2}$$/수식$$분 $$수식$${c3}$$/수식$$초$$수식$$+ ` {a1}$$/수식$$시간 $$수식$${a2}$$/수식$$분" \
              "$$수식$$= ` {sa}$$/수식$$시간 $$수식$${sb}$$/수식$$분 $$수식$${sc}$$/수식$$초입니다.\n\n"

    boxblank = "$$수식$$BOX{　　}$$/수식$$"
    
    a1 = np.random.randint(1, 5)
    b1 = np.random.randint(1, 4)

    while True:
        a2 = np.random.randint(31, 60)
        b2 = np.random.randint(40, 59)
        b3 = np.random.randint(2, 59)

        if (121 <= b2 + a2 + a2) and (b3 != b2):
            break

    c1 = a1 + b1 + 1
    c2 = a2 + b2 - 60
    c3 = b3

    sa = c1 + a1 + 1
    sb = c2 + a2 - 60
    sc = c3

    stem = stem.format(a1=a1, a2=a2, b1=b1, b2=b2, b3=b3, boxblank=boxblank)
    answer = answer.format(sa=sa, sb=sb, sc=sc)
    comment = comment.format(a1=a1, a2=a2, b1=b1, b2=b2, b3=b3, sa=sa, sb=sb, sc=sc, c1=c1, c2=c2, c3=c3)

    return stem, answer, comment








# 3-1-5-50
def lenandtime315_Stem_026():
    stem = "어느 버스는 기점에서 $$수식$${a2}$$/수식$$분 $$수식$${a3}$$/수식$$초 간격으로 출발합니다. 기점에서 $$수식$${sn}$$/수식$$번째 버스가 출발한 시각이 오전 $$수식$${b1}$$/수식$$시 $$수식$${b2}$$/수식$$분 $$수식$${b3}$$/수식$$초라면 첫 번째 버스가 출발한 시각은 오전 몇 시 몇 분 몇 초인가요?\n" \
        "{boxblank} 시 {boxblank} 분 {boxblank} 초"
    answer = "(정답)\n오전 $$수식$${sa}$$/수식$$, $$수식$${sb}$$/수식$$, $$수식$${sc}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sn}$$/수식$$번째 버스는 첫 번째 버스가 출발하고 $$수식$${a2}$$/수식$$분 $$수식$${a3}$$/수식$$초가 $$수식$${sn1}$$/수식$$번 지나야 출발합니다.\n" \
              "{sx}$$수식$$= ` {c2}$$/수식$$분 $$수식$${c3}$$/수식$$초$$수식$$= ` {d1}$$/수식$$시간 $$수식$${d2}$$/수식$$분 $$수식$${d3}$$/수식$$초,\n" \
              "따라서 첫 번째 버스의 출발 시각은\n" \
              "$$수식$${b1}$$/수식$$시 $$수식$${b2}$$/수식$$분 $$수식$${b3}$$/수식$$초$$수식$$- ` {d1}$$/수식$$시간 $$수식$${d2}$$/수식$$분 $$수식$${d3}$$/수식$$초" \
              "$$수식$$= ` {e1}$$/수식$$시 $$수식$${e2}$$/수식$$분 $$수식$${e3}$$/수식$$초$$수식$$- ` {d1}$$/수식$$시간 $$수식$${d2}$$/수식$$분 $$수식$${d3}$$/수식$$초\n" \
              "$$수식$$= ` {sa}$$/수식$$시 $$수식$${sb}$$/수식$$분 $$수식$${sc}$$/수식$$초입니다.\n\n"

    boxblank = "$$수식$$BOX{　　}$$/수식$$"
    
    while True:
        while True:
            sn = np.random.randint(3, 6)
            sn1 = sn - 1
            a2 = np.random.randint(23, 57)
            a3 = np.random.randint(13, 57)
            if (91 <= (sn - 1) * a2) and ((sn - 1) * a2 <= 119) and (61 <= (sn - 1) * a3) and ((sn - 1) * a3 <= 75) and (a3 != a2):
                break

        if sn == 3:
            sx = "$$수식$$%d$$/수식$$분 $$수식$$%d$$/수식$$초$$수식$$+ ` %d$$/수식$$분 $$수식$$%d$$/수식$$초" % (a2, a3, a2, a3)
        elif sn == 4:
            sx = "$$수식$$%d$$/수식$$분 $$수식$$%d$$/수식$$초$$수식$$+ ` %d$$/수식$$분 $$수식$$%d$$/수식$$초$$수식$$+ ` %d$$/수식$$분 $$수식$$%d$$/수식$$초" % (a2, a3, a2, a3, a2, a3)
        elif sn == 5:
            sx = "$$수식$$%d$$/수식$$분 $$수식$$%d$$/수식$$초$$수식$$+ ` %d$$/수식$$분 $$수식$$%d$$/수식$$초$$수식$$+ ` %d$$/수식$$분 $$수식$$%d$$/수식$$초$$수식$$+ ` %d$$/수식$$분 $$수식$$%d$$/수식$$초" % (a2, a3, a2, a3, a2, a3, a2, a3)

        c2 = sn1 * a2
        c3 = sn1 * a3

        if c3 // 60 >= 1:
            d3 = c3 - ((c3 // 60) * 60)
            if (c2 + (c3 // 60)) // 60 >= 1:
                d2 = (c2 + (c3 // 60)) - (((c2 + (c3 // 60)) // 60) * 60)
                d1 = (c2 + (c3 // 60)) // 60
            else:
                d2 = c2 + (c3 // 60)
                d1 = 0
        else:
            d3 = c3
            if c2 // 60 >= 1:
                d2 = c2 - ((c2 // 60) * 60)
                d1 = c2 // 60
            else:
                d2 = c2
                d1 = 0

        b1 = np.random.randint(6, 8)

        while True:
            b2 = np.random.randint(1, 30)
            b3 = np.random.randint(22, 60)
            if b2 != b3:
                break

        if b3 >= d3:
            e3 = b3
            if b2 >= d2:
                e2 = b2
                if b1 >= d1:
                    e1 = b1
                else:
                    e1 = -1
            else:
                e2 = b2 + 60
                e1 = b1 - 1
        else:
            e3 = b3 + 60
            if b2 - 1 >= d2:
                e2 = b2 - 1
                if b1 >= d1:
                    e1 = b1
                else:
                    e1 = -1
            else:
                e2 = b2 - 1 + 60
                e1 = b1 - 1

        sa = e1 - d1
        sb = e2 - d2
        sc = e3 - d3

        if (sa >= 0) and (sb >= 0) and (sc >= 0):
            break

    stem = stem.format(sn=sn, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, boxblank=boxblank)
    answer = answer.format(sa=sa, sb=sb, sc=sc)
    comment = comment.format(sn=sn, sn1=sn1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, c2=c2, c3=c3, d1=d1, d2=d2, d3=d3, sx=sx,
                             sa=sa, sb=sb, sc=sc, e1=e1, e2=e2, e3=e3)

    return stem, answer, comment









# 3-1-5-51
def lenandtime315_Stem_027():
    stem = "어떤 시계는 $$수식$$1$$/수식$$시간에 $$수식$${second}$$/수식$$초씩 늦어집니다. 오후 $$수식$${sb}$$/수식$$시에 이 시계를 정확히 맞추었다면 $$수식$${sc}$$/수식$$일 후 오후 $$수식$${sb}$$/수식$$시에 이 시계가 가리키는 시각은 오후 몇 시 몇 분 몇 초인가요?\n" \
        "{boxblank} 시 {boxblank} 분 {boxblank} 초"
    answer = "(정답)\n오후 $$수식$${c1}$$/수식$$, $$수식$${c2}$$/수식$$, $$수식$${c3}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sc}$$/수식$$일$$수식$$= ` 24$$/수식$$시간$$수식$$times ` {sc} ` = ` {sd}$$/수식$$시간\n" \
              "$$수식$$LEFT ( {sc}$$/수식$$일 동안 늦어진 시간$$수식$$RIGHT ) ` = ` {sd} ` times ` {second} ` = ` {se} LEFT ($$/수식$$초$$수식$$RIGHT ) ` = ` {a2}$$/수식$$분 $$수식$${a3}$$/수식$$초\n" \
              "따라서 $$수식$${sc}$$/수식$$일 후 오후 $$수식$${sb}$$/수식$$시에 이 시계가 가리키는 시각은\n" \
              "$$수식$${sb}$$/수식$$시$$수식$$- ` {a2}$$/수식$$분 $$수식$${a3}$$/수식$$초" \
              "$$수식$$= ` {b1}$$/수식$$시 $$수식$${b2}$$/수식$$분 $$수식$${b3}$$/수식$$초$$수식$$- ` {a2}$$/수식$$분 $$수식$${a3}$$/수식$$초" \
              "$$수식$$= ` {c1}$$/수식$$시 $$수식$${c2}$$/수식$$분 $$수식$${c3}$$/수식$$초입니다.\n\n"

    boxblank = "$$수식$$BOX{　　}$$/수식$$"
    
    sb = np.random.randint(2, 12)

    while True:
        second = np.random.randint(3, 9)
        sc = np.random.randint(2, 5)

        sd = 24 * sc
        se = sd * second

        if se % 60 != 0:
            break

    a2 = (second * sd) // 60
    a3 = se - 60 * a2

    b1 = sb - 1
    b2 = 59
    b3 = 60

    c1 = b1
    c2 = 59 - a2
    c3 = 60 - a3

    stem = stem.format(second=second, sb=sb, sc=sc, boxblank=boxblank)
    answer = answer.format(c1=c1, c2=c2, c3=c3)
    comment = comment.format(a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, c1=c1, c2=c2, c3=c3, second=second, sb=sb, sc=sc, sd=sd, se=se)

    return stem, answer, comment












