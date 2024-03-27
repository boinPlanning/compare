import numpy as np
# from math import gcd
import math
import random




answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤"
}





answer_kodict = {
    0: "ㄱ",
    1: "ㄴ",
    2: "ㄷ",
    3: "ㄹ",
    4: "ㅁ"
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
















circle_one = "①"
circle_two = "②"
circle_three = "③"
circle_four = "④"












def josa(a, b):
    if b == "은" or b == "는":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "는"
        else:
            return "은"

    elif b == "가" or b == "이":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "가"
        else:
            return "이"

    elif b == "야" or b == "이야":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "야"
        else:
            return "이야"

    elif b == "을" or b == "를":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "를"
        else:
            return "을"

    elif b == "과" or b == "와":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "와"
        else:
            return "과"

    elif b == "로" or b == "으로":
        if (str(a))[-1] == "0" or (str(a))[-1] == "3" or (str(a))[-1] == "6":
            return "으로"
        else:
            return "로"

    elif b == "라고" or b == "이라고":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "라고"
        else:
            return "이라고"




























# 5-2-4-유형01-1
def decimalmul524_Stem_001():
    stem = "소수의 곱셈을 보기와 같이 분수의 곱셈으로 계산하려고 합니다. $$수식$$LEFT ( {su} RIGHT )$$/수식$$ 안에 알맞은 수의 합을 구하시오.\n$$표$$보기\n$$수식$$0.2 `Times` 6 `=` 2 over 10 `Times` 6 `=` {k1} over 10 `=` 12 over 10 `=` 1.2$$/수식$$$$/표$$\n$$수식$$0.{sa} `Times` {sb} `=` {sf} over 10 `Times` {sb} `=` {k2} over 10 `=` {sf} over 10 `=` {sf}$$/수식$$\n"
    answer = "(답): $$수식$${saa}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$0.{sa} `Times` {sb} `=` {qsa} over 10 Times {sb} `=` {k3} over 10 `=` {qsc} over 10 `=` {qsd}$$/수식$$이므로 " \
              "$$수식$$LEFT ( {su} RIGHT )$$/수식$$ 안에 알맞은 수의 합은\n" \
              "$$수식$${sa} `+` {sa} `+` {sc} `+` {sd} `=` {saa}$$/수식$$입니다.\n\n"



    sa = np.random.randint(2, 10)
    sb = np.random.randint(2, 10)

    sc = sa * sb
    sd = sa * sb / 10

    if sd - (sd // 1) == 0:
        sd = round(sd)

    saa = sa + sa + sc + sd

    if saa - (saa // 1) == 0:
        saa = round(saa)

    su = "````"
    sf = "{ LEFT ( ```` RIGHT ) }"

    qsa = "{ LEFT ( %s RIGHT ) }" % sa
    qsc = "{ LEFT ( %s RIGHT ) }" % sc
    qsd = "{ LEFT ( %s RIGHT ) }" % sd

    k1 = "{2 `Times` 6}"
    k2 = "{ LEFT ( %s RIGHT ) `Times` %s}" % (su, sb)
    k3 = "{ LEFT ( %s RIGHT ) `Times` %s}" % (sa, sb)

    stem = stem.format(sa=sa, sb=sb, su=su, sf=sf, k1=k1, k2=k2)
    answer = answer.format(saa=saa)
    comment = comment.format(sa=sa, sb=sb, qsa=qsa, k3=k3, qsc=qsc, qsd=qsd, sc=sc, sd=sd, saa=saa, su=su)

    return stem, answer, comment




































# 5-2-4-유형01-2
def decimalmul524_Stem_002():
    stem = "$$수식$${saa} `Times` {sbb}$$/수식$${rur1} $$수식$$0.1$$/수식$$의 개수로 계산하려고 합니다. {c1}, {c2}, {c3}, {c4}에 알맞은 수로 짝지어진 것을 고르시오.\n$$표$$$$수식$${saa} `Times` {sbb}$$/수식$${eun1} $$수식$$0.1$$/수식$$이 $$수식$$LEFT ($$/수식$${c1}$$수식$$RIGHT )$$/수식$$개씩 $$수식$$LEFT ($$/수식$${c2}$$수식$$RIGHT )$$/수식$$묶음이므로 $$수식$$0.1$$/수식$$이 모두 $$수식$$LEFT ($$/수식$${c3}$$수식$$RIGHT )$$/수식$$개입니다.\n→ $$수식$${saa} `Times` {sbb} `=` LEFT ($$/수식$${c4}$$수식$$RIGHT )$$/수식$$$$/표$$\n{circle_one} {x1}\n{circle_two} {x2}\n{circle_three} {x3}\n{circle_four} {x4}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${saa} `Times` {sbb} `=` 0.1 `Times` {scc} `Times` {sbb} `=` 0.1 `Times` {sdd} `=` {see}$$/수식$$\n" \
              "→ $$수식$$0.1$$/수식$$이 모두 $$수식$${sdd}$$/수식$$개이므로 $$수식$${saa} `Times` {sbb} `=` {see}$$/수식$$입니다.\n\n"

    c1 = "㉠"
    c2 = "㉡"
    c3 = "㉢"
    c4 = "㉣"

    while True:
        sa = np.random.randint(2, 10)
        saa = round(sa / 10, 1)
        sbb = np.random.randint(2, 10)
        if (1 < (saa * sbb)) and (10 > (saa * sbb)):
            break

    scc = round(saa * 10)
    sdd = scc * sbb
    see = round(0.1 * sdd, 1)

    if (see - see // 1) == 0:
        see = int(see)

    sa = saa * 10
    sb = sbb
    sc = saa * 10 * sbb
    sd = round(saa * sbb, 2)

    if (sd - sd // 1) == 0:
        sd = int(sd)

    se = round(saa * sbb / 10, 2)

    if (se - se // 1) == 0:
        se = int(se)

    y1 = "%s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$, %s $$수식$$%s$$/수식$$" % (c1, sa, c2, sb, c3, sc, c4, sd)
    y2 = "%s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$, %s $$수식$$%s$$/수식$$" % (c1, sb, c2, sa, c3, sc, c4, sd)
    y3 = "%s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$, %s $$수식$$%s$$/수식$$" % (c1, sa, c2, sb, c3, sc, c4, se)
    y4 = "%s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$, %s $$수식$$%s$$/수식$$" % (c1, sb, c2, sa, c3, sc, c4, se)

    candidates = [y1, y2, y3, y4]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4] = candidates

    correct_idx = 0

    for idx, sdx in enumerate(candidates):
        if sdx == y1:
            correct_idx = idx
            break

    rur1 = josa(sbb, "를")

    eun1 = josa(sbb, "은")

    stem = stem.format(saa=saa, sbb=sbb, x1=x1, x2=x2, x3=x3, x4=x4, c1=c1, c2=c2, c3=c3, c4=c4, circle_one=circle_one,
                       circle_two=circle_two, circle_three=circle_three, circle_four=circle_four, rur1=rur1, eun1=eun1)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see)

    return stem, answer, comment


































# 5-2-4-유형01-3
def decimalmul524_Stem_003():
    stem = "자연수의 곱셈을 이용하여 $$수식$${saa} `Times` {sbb}$$/수식$${rur1} 계산하시오.\n$$표$$ $$수식$${scc} `Times` {sbb} `=` {sdd}$$/수식$$ $$/표$$\n"
    answer = "(답): $$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa}$$/수식$${eun1} $$수식$${scc}$$/수식$$의 $$수식$$1 over 100$$/수식$$배이므로 " \
              "$$수식$${saa} `Times` {sbb}$$/수식$${eun2} $$수식$${sdd}$$/수식$$의 $$수식$$1 over 100$$/수식$$배인 $$수식$${see}$$/수식$${ga1} 됩니다.\n\n"


    while True:
        sa = np.random.randint(12, 100)
        saa = round(sa / 100, 2)
        sbb = np.random.randint(2, 10)

        if (saa * sbb > 1) and (sa % 10 != 0):
            break

    scc = round(saa * 100)
    sdd = scc * sbb
    see = round(sdd / 100, 2)

    rur1 = josa(sbb, "를")
    eun1 = josa(saa, "은")
    eun2 = josa(sbb, "은")
    ga1 = josa(see, "가")


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, rur1=rur1)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, eun1=eun1, eun2=eun2, ga1=ga1)

    return stem, answer, comment








































# 5-2-4-유형01-4
def decimalmul524_Stem_004():
    stem = "빈 칸에 알맞은 수를 구하시오.\n$$수식$$LEFT ( {saa} RIGHT )$$/수식$$→$$수식$$LEFT ( {sq} RIGHT )$$/수식$$→$$수식$$LEFT ( {su} RIGHT )$$/수식$$\n"
    answer = "(답): $$수식$${scc}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sdd} `Times` {sbb} `=` {see}$$/수식$$이고, $$수식$${saa}$$/수식$${eun1} $$수식$${sdd}$$/수식$$의 " \
              "$$수식$$1 over 100$$/수식$$배이므로 곱도 $$수식$$1 over 100$$/수식$$배인 $$수식$${scc}$$/수식$$입니다.\n\n"


    while True:
        sa = np.random.randint(12, 100)
        saa = round(sa / 100, 2)
        sbb = np.random.randint(2, 10)

        if (saa * sbb > 1) and (sa % 10 != 0):
            break

    scc = round(saa * sbb, 2)
    sdd = round(saa * 100)
    see = sdd * sbb

    sq = "{Times {%s}}" % (sbb)
    su = "```` ```` ````"

    eun1 = josa(saa, "은")


    stem = stem.format(saa=saa, sq=sq, su=su)
    answer = answer.format(scc=scc)
    comment = comment.format(sdd=sdd, sbb=sbb, see=see, saa=saa, scc=scc, eun1=eun1)

    return stem, answer, comment









































# 5-2-4-유형01-5
def decimalmul524_Stem_005():
    stem = "곱이 가장 작은 것을 찾아 기호를 쓰시오.\n$$표$$ㄱ. $$수식$$0.{sa} Times {sb}$$/수식$$\nㄴ. $$수식$$0.{sc} Times {sd}$$/수식$$\nㄷ. $$수식$$0.{se} Times {sf}$$/수식$$\nㄹ. $$수식$$0.{sg} Times {sh}$$/수식$$$$/표$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "ㄱ. $$수식$$0.{sa} Times {sb} `=` {saa}$$/수식$$, " \
              "ㄴ. $$수식$$0.{sc} Times {sd} `=` {sbb}$$/수식$$, " \
              "ㄷ. $$수식$$0.{se} Times {sf} `=` {scc}$$/수식$$, " \
              "ㄹ. $$수식$$0.{sg} Times {sh} `=` {sdd}$$/수식$$\n" \
              "따라서 곱이 가장 작은 것은 {a1}입니다.\n\n"


    while True:
        sa = [2, 4, 6, 8][np.random.randint(0, 4)]
        sb = [2, 4, 6, 8][np.random.randint(0, 4)]
        sc = [2, 4, 6, 8][np.random.randint(0, 4)]
        sf = [2, 4, 6, 8][np.random.randint(0, 4)]
        sd = [3, 5, 7, 9][np.random.randint(0, 4)]
        se = [3, 5, 7, 9][np.random.randint(0, 4)]
        sg = [3, 5, 7, 9][np.random.randint(0, 4)]
        sh = [3, 5, 7, 9][np.random.randint(0, 4)]

        t1 = sa * sb
        t2 = sc * sd
        t3 = se * sf
        t4 = sg * sh

        if (sa * sb > 20) and (sa * sb < 60) and (sc * sd > 20) and (sc * sd < 60) and (se * sf > 20) and (
                se * sf < 60) and (sg * sh > 20) and (sg * sh < 60) and (se != ((sc * sd) / sf)) and (t1 != t2) and (
                t1 != t3) and (t1 != t4) and (t2 != t4) and (t3 != t4):
            break

    saa = round(sa * sb / 10, 1)
    if saa - saa // 1 == 0:
        saa = round(saa)

    sbb = round(sc * sd / 10, 1)
    if sbb - sbb // 1 == 0:
        sbb = round(sbb)

    scc = round(se * sf / 10, 1)
    if scc - scc // 1 == 0:
        scc = round(scc)

    sdd = round(sg * sh / 10, 1)
    if sdd - sdd // 1 == 0:
        sdd = round(sdd)

    candidates = [saa, sbb, scc, sdd]

    correct_idx = 0

    for idx, sdx in enumerate(candidates):
        if sdx == min(candidates):
            correct_idx = idx
            break


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sh=sh)
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(sa=sa, sb=sb, saa=saa, sc=sc, sd=sd, sbb=sbb, se=se, sf=sf, scc=scc, sg=sg, sh=sh, sdd=sdd,
                             a1=answer_kodict[correct_idx])

    return stem, answer, comment
























































# 5-2-4-유형01-6
def decimalmul524_Stem_006():
    stem = "계산 결과를 잘못 말한 친구의 이름을 쓰시오.\n{p1}: $$수식$${saa} `Times` 5$$/수식$$는 $$수식$${sbb}$$/수식$${wa1} $$수식$$5$$/수식$$의 곱으로 어림할 수 있으니까 결과는 $$수식$${scc}$$/수식$$ 정도가 될 거야.\n{p2}: $$수식$${sdd} `Times` {see}$$/수식$$에서 $$수식$${sff}$$/수식$${wa2} $$수식$${see}$$/수식$$의 곱은 약 $$수식$${sgg}$$/수식$$이니까 $$수식$${sdd}$$/수식$${wa3} $$수식$${see}$$/수식$$의 곱은 $$수식$${shh}$$/수식$$ 정도가 돼.\n"
    answer = "(답): {p2}\n"
    comment = "(해설)\n" \
              "$$수식$${sff}$$/수식$${wa2} $$수식$${see}$$/수식$$의 곱은 약 $$수식$${sgg}$$/수식$$이므로 " \
              "$$수식$${sff}$$/수식$$의 $$수식$$0.01$$/수식$$배인 $$수식$${sdd}$$/수식$${wa3} $$수식$${see}$$/수식$$의 곱은 " \
              "$$수식$${sgg}$$/수식$$의 $$수식$$0.01$$/수식$$배인 $$수식$${sii}$$/수식$$ 정도가 됩니다.\n\n"


    while True:
        p1 = ["지호", "민준", "도윤", "준영", "미호", "빛나", "채영", "은채", "희준", "시언", "혁재", "가희"][np.random.randint(0, 12)]
        p2 = ["지호", "민준", "도윤", "준영", "미호", "빛나", "채영", "은채", "희준", "시언", "혁재", "가희"][np.random.randint(0, 12)]

        if p1 != p2:
            break

    while True:
        sa = np.random.randint(31, 100)
        saa = round(sa / 100, 2)

        if ((sa // 10) % 2 != 0) and (sa % 10 != 0) and ((sa % 10) >= 5) and ((sa % 10) <= 9):
            break
        elif ((sa // 10) % 2 == 0) and (sa % 10 != 0) and ((sa % 10) >= 1) and ((sa % 10) <= 4):
            break

    sbb = round(saa, 1)
    scc = sbb * 5

    if (scc - scc // 1) == 0:
        scc = round(scc)

    while True:
        sd = np.random.randint(21, 100)
        sdd = round(sd / 100, 2)

        if (sd // 10) % 2 != 0:
            if ((sd % 10) >= 5) and ((sd % 10) <= 9):
                break

        if (sd // 10) % 2 == 0:
            if ((sd % 10) >= 1) and ((sd % 10) <= 4):
                break

    while True:
        see = np.random.randint(2, 10)
        if sdd * see > 1:
            break

    sff = round(sdd * 100)
    sgg = round(sff * see)
    shh = round(sgg / 10)
    sii = round(sgg / 100)

    wa1 = josa(sbb, "과")
    wa2 = josa(sff, "과")
    wa3 = josa(sdd, "과")


    stem = stem.format(p1=p1, p2=p2, saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, wa1=wa1,
                       wa2=wa2, wa3=wa3)
    answer = answer.format(p2=p2)
    comment = comment.format(sff=sff, see=see, sgg=sgg, sdd=sdd, sii=sii, wa2=wa2, wa3=wa3)

    return stem, answer, comment













































# 5-2-4-유형01-7
def decimalmul524_Stem_007():
    stem = "계산 결과를 비교하여 ○ 안에 $$수식$$ &gt; $$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 써넣으려고 합니다. 알맞은 기호를 고르시오.\n$$수식$$0.{sa}{sb} `Times` {sc}$$/수식$$ ○ $$수식$$0.{sd}{se} `Times` {sf}$$/수식$$\n{circle_one} $$수식$$&gt;$$/수식$$\n{circle_two} $$수식$$=$$/수식$$\n{circle_three} $$수식$$&lt;$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$0.{sa}{sb} `Times` {sc} `=` {saa}$$/수식$$, " \
              "$$수식$$0.{sd}{se} `Times` {sf} `=` {sbb}$$/수식$$\n" \
              "→ $$수식$${saa}````{scc}````{sbb}$$/수식$$\n\n"


    while True:
        sa = np.random.randint(3, 10)
        sb = np.random.randint(3, 10)
        sc = np.random.randint(3, 10)
        se = np.random.randint(3, 10)
        sd = 11 - sa
        sf = np.random.randint(2, 10)

        if (((sa * sc - 10) / sd) <= sf) and (sf <= ((sa * sc + 10) / sd)) and (sc != sf):
            break

    saa = round(((10 * sa + sb) / 100) * sc, 2)
    sbb = round(((10 * sd + se) / 100) * sf, 2)

    if saa - sbb > 0:
        scc = '&gt;'
        a1 = '①'
    elif saa - sbb == 0:
        scc = '='
        a1 = '②'
    elif saa - sbb < 0:
        scc = '&lt;'
        a1 = '③'


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, circle_one=circle_one, circle_two=circle_two,
                       circle_three=circle_three)
    answer = answer.format(a1=a1)
    comment = comment.format(sa=sa, sb=sb, sc=sc, saa=saa, sd=sd, se=se, sf=sf, sbb=sbb, scc=scc)

    return stem, answer, comment



















































# 5-2-4-유형02-1
def decimalmul524_Stem_008():
    stem = "소수를 분수로 나타내어 계산한 것입니다. ㉠, ㉡에 알맞은 수로 짝지어진 것을 고르시오.\n$$표$$$$수식$${saa} `Times` {sbb} `=` {scc} over ㉠ `Times` {sbb} `=` {k1} over ㉠ `=` {sdd} over ㉠ `=`$$/수식$$㉡$$/표$$\n① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${saa}$$/수식$${eun1} 소수 두 자리 수이므로 분모가 $$수식$$100$$/수식$$인 분수로\n 나타냅니다.\n" \
              "$$수식$${saa} `Times` {sbb} `=` {scc} over 100 `Times` {sbb}$$/수식$$\n$$수식$$ `=` " \
              "{k1} over 100 `=` {sdd} over 100 `=` {see}$$/수식$$\n\n"


    while True:
        saa = np.random.randint(102, 1000)
        if saa % 10 != 0:
            saa = round(saa * 0.01, 2)
            break

    while True:
        sbb = np.random.randint(11, 50)
        if sbb % 10 != 0:
            break

    scc = round(saa * 100)
    sdd = scc * sbb
    see = round(sdd * 0.01, 2)
    sa = 10
    sb = round(sdd * 0.1, 1)
    sc = round(sdd * 0.01, 2)
    sd = 100
    k1 = "{%s `Times` %s}" % (scc, sbb)
    se = 1000

    y1 = "%s $$수식$$%d$$/수식$$, %s $$수식$$%.1f$$/수식$$" % ("㉠", sa, "㉡", sb)
    y2 = "%s $$수식$$%d$$/수식$$, %s $$수식$$%.2f$$/수식$$" % ("㉠", sa, "㉡", sc)
    y3 = "%s $$수식$$%d$$/수식$$, %s $$수식$$%.1f$$/수식$$" % ("㉠", sd, "㉡", sb)
    y4 = "%s $$수식$$%d$$/수식$$, %s $$수식$$%.2f$$/수식$$" % ("㉠", sd, "㉡", sc)
    y5 = "%s $$수식$$%d$$/수식$$, %s $$수식$$%.1f$$/수식$$" % ("㉠", se, "㉡", sb)

    candidates = [y1, y2, y3, y4, y5]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4, x5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):
        if sdx == y4:
            correct_idx = idx
            break

    eun1 = josa(saa, "은")


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, k1=k1)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, k1=k1, eun1=eun1)

    return stem, answer, comment
















































# 5-2-4-유형02-2
def decimalmul524_Stem_009():
    stem = "$$수식$${sa}.{sb} `Times` {sn}$$/수식$${wa1} 계산 결과가 같은 것을 찾아 선택하세요.\n{circle_one} $$수식$${x1}$$/수식$$\n{circle_two} $$수식$${x2}$$/수식$$\n{circle_three} $$수식$${x3}$$/수식$$\n{circle_four} $$수식$${x4}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${sa}.{sb} `Times` {sn} $$/수식$$\n $$수식$$`=` {f1} $$/수식$$\n $$수식$$`=` {sc} over 10 `Times` {sn}$$/수식$$입니다.\n\n"


    while True:
        sa = np.random.randint(1, 10)
        sb = np.random.randint(1, 10)
        sn = np.random.randint(2, 10)
        if sn != sb:
            break

    sc = sa * 10 + sb

    temp1 = str(round(sa + sb / 10, 1))
    temp2 = temp1

    for inde in range(sn - 1):
        temp2 += "+%s" % (temp1)

    f1 = temp2

    temp3 = temp1
    for indes in range(sn):
        if indes % 3 == 0:
            temp3 += "\\\\"
        temp3 += "+%s" % (temp1)

    y1 = temp3
    y2 = "%d over 100 `Times` %d" % (sc, sn)
    y3 = "%d.%d `Times` %d" % (sa, sn, sb)
    y4 = "%d over 10 `Times` %d" % (sc, sn)

    candidates = [y1, y2, y3, y4]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):
        if sdx == y4:
            correct_idx = idx
            break

    wa1 = josa(sn, "와")


    stem = stem.format(sa=sa, sb=sb, sn=sn, x1=x1, x2=x2, x3=x3, x4=x4, circle_one=circle_one, circle_two=circle_two,
                       circle_three=circle_three, circle_four=circle_four, wa1=wa1)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(sa=sa, sb=sb, sn=sn, f1=f1, sc=sc)

    return stem, answer, comment

















































# 5-2-4-유형02-3
def decimalmul524_Stem_010():
    stem = "자연수의 곱셈을 이용하여 소수의 곱셈을 계산하려고 합니다. $$수식$$□$$/수식$$ 안에 알맞은 수의 합을 구하시오.\n$$표$$곱해지는 수가 $$수식$$1 over 10$$/수식$$이 되면\n계산 결과도 $$수식$$1 over {sq}$$/수식$$배가 되므로\n$$수식$${saa} `Times` {sbb} `=` {sq}$$/수식$$ → $$수식$${scc} `Times` {sbb} `=` {sq}$$/수식$$입니다.$$/표$$\n"
    answer = "(답): $$수식$${sff}$$/수식$$\n"
    comment = "(해설)\n" \
              "곱해지는 수 $$수식$${scc}$$/수식$${eun1} $$수식$${saa}$$/수식$$의 $$수식$$1 over 10$$/수식$$배이므로 " \
              "곱도 $$수식$${sdd}$$/수식$$의 $$수식$$1 over 10$$/수식$$배인 $$수식$${see}$$/수식$${ga1} 됩니다.\n" \
              "따라서 $$수식$$□$$/수식$$ 안에 알맞은 수의 합은 $$수식$$10 `+` {sdd} `+` {see} `=` {sff}$$/수식$$입니다.\n\n"


    saa = np.random.randint(12, 100)
    sbb = np.random.randint(3, 10)

    scc = round(saa / 10, 1)
    if scc - (scc // 1) == 0:
        scc = round(scc)

    sdd = saa * sbb

    see = round(sdd / 10, 1)
    if see - (see // 1) == 0:
        see = round(see)

    sff = round(10 + sdd + see, 1)
    if sff - (sff // 1) == 0:
        sff = round(sff)

    #sq = "LEFT ($$/수식$$ $$수식$$RIGHT )"
    sq="□"

    eun1 = josa(scc, "은")
    ga1 = josa(see, "가")


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sq=sq)
    answer = answer.format(sff=sff)
    comment = comment.format(scc=scc, saa=saa, sdd=sdd, see=see, sff=sff, eun1=eun1, ga1=ga1)

    return stem, answer, comment





















































# 5-2-4-유형02-4
def decimalmul524_Stem_011():
    stem = "계산해 보시오.\n$$수식$${saa} `Times` {sbb}$$/수식$$\n"
    answer = "(답): $$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} `Times` {sbb} `=` {scc} over 10 `Times` {sbb} `=` {k1} over 10 `=` {sdd} over 10 `=` {see}$$/수식$$입니다.\n\n"


    while True:
        sade = np.random.randint(1, 10)
        sa1 = np.random.randint(3, 10)
        saa = round(sa1 + sade / 10, 1)
        sbb = np.random.randint(3, 10)

        if (saa >= 3.2) and (saa * sbb > 10) and (sbb != 5):
            break

    scc = round(saa * 10)
    sdd = scc * sbb
    see = round(sdd * 0.1, 1)

    k1 = "{%s `Times` %d}" % (scc, sbb)


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, k1=k1)

    return stem, answer, comment




















































# 5-2-4-유형02-5
def decimalmul524_Stem_012():
    stem = "계산 결과를 비교하여 곱이 더 큰 것을 찾아 기호를 쓰시오.\n$$표$$ㄱ. $$수식$${sa}.{sb} `Times` {sc}$$/수식$$      ㄴ. $$수식$${sd}.{se} `Times` {sf}$$/수식$$$$/표$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "ㄱ. $$수식$${sa}.{sb} `Times` {sc} `=` {saa}$$/수식$$, ㄴ. $$수식$${sd}.{se} `Times` {sf} `=` {sbb}$$/수식$$\n" \
              "따라서 곱이 가장 더 큰 것의 기호를 쓰면 {a1}입니다.\n\n"


    while True:
        sa = np.random.randint(3, 10)
        sb = np.random.randint(3, 10)
        sc = np.random.randint(3, 10)
        se = np.random.randint(3, 10)
        sd = 10 - sa

        while True:
            sf = np.random.randint(1, 100)
            if (((sa * sc - 10) / sd) <= sf) and (((sa * sc + 10) / sd) >= sf) and (2 <= sf):
                break

        saa = round((sa + sb / 10) * sc, 1)
        if saa - saa // 1 == 0:
            saa = round(saa)

        sbb = round((sd + se / 10) * sf, 1)
        if sbb - sbb // 1 == 0:
            sbb = round(sbb)

        a1 = ""

        if saa > sbb:
            a1 = "ㄱ"
        elif saa < sbb:
            a1 = "ㄴ"

        if a1 != "":
            break


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf)
    answer = answer.format(a1=a1)
    comment = comment.format(sa=sa, sb=sb, sc=sc, saa=saa, sd=sd, se=se, sf=sf, sbb=sbb, a1=a1)

    return stem, answer, comment






















































# 5-2-4-유형02-6
def decimalmul524_Stem_013():
    stem = "빈 칸에 알맞은 수를 구하시오.\n$$수식$$LEFT ( {aaa} RIGHT )$$/수식$$ → $$수식$$LEFT ( {bbb} RIGHT )$$/수식$$ → $$수식$$LEFT ( {ccc} RIGHT )$$/수식$$ → $$수식$$LEFT ( {sq} RIGHT )$$/수식$$\n"
    answer = "(답): $$수식$${sdd}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} `Times` {sbb} `=` {see}$$/수식$$ → $$수식$${see} `Times` {scc} `=` {sdd}$$/수식$$\n\n"


    while True:
        sa = np.random.randint(2, 10)
        saa = round(sa / 10, 1)
        sbb = np.random.randint(2, 10)
        if ((saa * sbb) > 1) and (sbb != 5):
            break

    scc = np.random.randint(2, 10)
    sdd = round(saa * sbb * scc, 1)
    if sdd - (sdd // 1) == 0:
        sdd = round(sdd)

    see = round(saa * sbb, 1)
    if see - (see // 1) == 0:
        see = round(see)

    aaa = "{%s}" % (saa)
    bbb = "{Times {%s}}" % (sbb)
    ccc = "{Times {%s}}" % (scc)
    sq = "```` ```` ````"


    stem = stem.format(aaa=aaa, bbb=bbb, ccc=ccc, sq=sq)
    answer = answer.format(sdd=sdd)
    comment = comment.format(saa=saa, sbb=sbb, see=see, scc=scc, sdd=sdd)

    return stem, answer, comment



















































# 5-2-4-유형02-7
def decimalmul524_Stem_014():
    stem = "{spp}이가 계산 결과를 비교하여 알게 된 점을 쓴 것입니다. ㉠, ㉡, ㉢, ㉣에 알맞게 짝을 지은 것을 고르시오.\n$$표$$$$수식$${saa} `Times` {sbb} `=`$$/수식$$㉠      $$수식$${scc} `Times` {sdd} `=`$$/수식$$㉡\n곱해지는 수가 $$수식$${saa}$$/수식$$에서 $$수식$${scc}$$/수식$${ro1} ㉢배가 되면 계산 결과도 ㉣배가 되는 구나!$$/표$$\n{circle_one} {x1}\n{circle_two} {x2}\n{circle_three} {x3}\n{circle_four} {x4}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${saa} `Times` {sbb} `=` {see}$$/수식$$, $$수식$${scc} `Times` {sdd} `=` {sff}$$/수식$$\n" \
              "따라서 계산 결과를 비교하여 알게 된 점은 곱해지는 수가 $$수식$${saa}$$/수식$$에서 $$수식$${scc}$$/수식$${ro1} " \
              "$$수식$${sa}$$/수식$$배가 되면 계산 결과 $$수식$${sff}$$/수식$$도 $$수식$${see}$$/수식$$의 $$수식$${sa}$$/수식$$배가 됩니다.\n\n"


    spp = ['수영', '민택', '도윤', '현욱', '지민', '연진', "상철", "진환", "나연", "서진", "태연", "주성"][np.random.randint(0, 12)]

    while True:
        sx = np.random.randint(11, 30)
        sxx = round(sx / 10, 1)
        if (sx % 10) != 0:
            break

    while True:
        sy = np.random.randint(101, 300)
        syy = round(sy / 100, 2)
        if (sy % 10) != 0:
            break

    scc = [sxx, syy][np.random.randint(0, 2)]
    sdd = np.random.randint(3, 10)

    if scc == sxx:
        saa = round(scc * 10)
        sgg = round((scc * sdd) / 10, 2)
        if sgg - (sgg // 1) == 0:
            sgg = round(sgg)

    elif scc == syy:
        saa = round(scc * 100)
        sgg = round((scc * sdd) * 10, 2)
        if sgg - (sgg // 1) == 0:
            sgg = round(sgg)

    sbb = sdd
    see = saa * sbb
    sff = round(scc * sdd, 2)

    if sff - (sff // 1) == 0:
        sff = round(sff)

    if scc == sxx:
        sa = '{1 over 10}'
        sb = '{1 over 100}'

    elif scc == syy:
        sa = '{1 over 100}'
        sb = '{1 over 10}'


    y1 = '%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$' % ("㉠", see, "㉡", sff, "㉢", sa, "㉣", sa)
    y2 = '%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$' % ("㉠", see, "㉡", sgg, "㉢", sb, "㉣", sb)
    y3 = '%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$' % ("㉠", see, "㉡", sff, "㉢", sa, "㉣", sb)
    y4 = '%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$' % ("㉠", see, "㉡", sgg, "㉢", sb, "㉣", sa)

    candidates = [y1, y2, y3, y4]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):
        if sdx == y1:
            correct_idx = idx
            break

    ro1 = josa(scc, "로")


    stem = stem.format(spp=spp, saa=saa, sbb=sbb, scc=scc, sdd=sdd, x1=x1, x2=x2, x3=x3, x4=x4, ro1=ro1,
                       circle_one=circle_one, circle_two=circle_two, circle_three=circle_three, circle_four=circle_four)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(saa=saa, sbb=sbb, see=see, scc=scc, sdd=sdd, sff=sff, sa=sa, ro1=ro1)

    return stem, answer, comment






















































# 5-2-4-유형03-1
def decimalmul524_Stem_015():
    stem = "{sss}을 한 개 만드는 데 밀가루 $$수식$${saa} rm kg$$/수식$$이 필요합니다.\n{sss}을 $$수식$${sbb}$$/수식$$개 만드는 데 필요한 밀가루는 모두 몇 $$수식$$rm kg$$/수식$$입니까?\n"
    answer = "(답): $$수식$${scc} rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${sss}을 $$수식$${sbb}$$/수식$$개 만드는 데 " \
              "필요한 밀가루의 양$$수식$$RIGHT )$$/수식$$\n$$수식$$ `=` {saa} `Times` {sbb} `=` {scc} LEFT ( rm kg RIGHT )$$/수식$$\n\n"


    sss = ["식빵", "모카빵", "밤빵", "맘모스빵"][np.random.randint(0, 4)]

    while True:
        sa = np.random.randint(2, 10)
        saa = round(sa / 10, 1)
        sbb = np.random.randint(3, 9)
        if (saa * sbb) > 1:
            break

    scc = round(saa * sbb, 1)

    if scc - scc // 1 == 0:
        scc = round(scc)


    stem = stem.format(sss=sss, saa=saa, sbb=sbb)
    answer = answer.format(scc=scc)
    comment = comment.format(sss=sss, sbb=sbb, saa=saa, scc=scc)
    return stem, answer, comment






















































# 5-2-4-유형03-2
def decimalmul524_Stem_016():
    stem = "{sss} 한 개의 길이는 $$수식$${saa} rm m$$/수식$$입니다. 똑같은 {sss} $$수식$${sbb}$$/수식$$개의 길이는 모두 몇 $$수식$$rm m$$/수식$$입니까?\n"
    answer = "(답): $$수식$${scc} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${sss} $$수식$${sbb}$$/수식$$개의 길이$$수식$$RIGHT ) `=` {saa} `Times` {sbb} `=` {scc} LEFT ( rm m RIGHT )$$/수식$$\n\n"


    sss = ["철사", "노끈", "색 테이프", "종이테이프", "포장 끈", "털실", "나무 막대"][np.random.randint(0, 7)]

    while True:
        sa = np.random.randint(21, 99)
        saa = round(sa / 100, 2)
        sbb = np.random.randint(3, 10)

        if (sa % 10 != 0) and ((saa * sbb) > 1):
            break

    scc = round(saa * sbb, 2)

    if (scc - (scc // 1)) == 0:
        scc = round(scc)


    stem = stem.format(sss=sss, saa=saa, sbb=sbb)
    answer = answer.format(scc=scc)
    comment = comment.format(sss=sss, sbb=sbb, saa=saa, scc=scc)

    return stem, answer, comment
























































# 5-2-4-유형03-3
def decimalmul524_Stem_017():
    stem = "한 자루의 무게가 $$수식$${saa} rm g$$/수식$$인 {sss} $$수식$${sbb}$$/수식$$자루의 무게는 몇 $$수식$$rm g$$/수식$$입니까?\n"
    answer = "(답): $$수식$${scc} rm g$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${sss} $$수식$${sbb}$$/수식$$자루의 무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$${sss} 한 자루의 무게$$수식$$RIGHT ) `Times` {sbb}$$/수식$$\n" \
              "$$수식$$= {saa} `Times` {sbb} `=` {scc} LEFT ( rm g RIGHT )$$/수식$$\n\n"


    sss = ["연필", "볼펜", "색연필", "사인펜", "네임펜"][np.random.randint(0, 5)]

    while True:
        sade = np.random.randint(1, 100)
        if (sade % 10) != 0:
            break

    sa1 = np.random.randint(7, 10)
    saa = round((sa1 + (sade / 100)), 2)

    sbb = np.random.randint(8, 19)
    scc = round(saa * sbb, 2)

    if (scc - (scc // 1)) == 0:
        scc = round(scc)


    stem = stem.format(saa=saa, sss=sss, sbb=sbb)
    answer = answer.format(scc=scc)
    comment = comment.format(sss=sss, sbb=sbb, saa=saa, scc=scc)

    return stem, answer, comment



















































# 5-2-4-유형03-4
def decimalmul524_Stem_018():
    stem = "{spp}이는 다음과 같이 운동 계획을 세웠습니다. {spp}이가 일주일 동안 운동할 거리는 몇 $$수식$$rm {{km}}$$/수식$$입니까?\n$$표$$운동 종류 : 산책로 $$수식$${saa} rm {{km}}$$/수식$$ 걷기\n운동 횟수 : 일주일에 $$수식$${sbb}$$/수식$$번$$/표$$\n"
    answer = "(답): $$수식$${scc} rm {{km}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${spp}이가 일주일 동안 운동할 거리$$수식$$RIGHT )$$/수식$$\n$$수식$$ `=` {saa} `Times` {sbb} `=` {scc} LEFT ( rm {{km}} RIGHT )$$/수식$$\n\n"


    spp = ["은진", "주영", "서준", "도윤", "희철", "서윤", "나연", "유정", "희연", "새봄", "우중", "한솔"][np.random.randint(0, 12)]

    sade = np.random.randint(1, 10)
    sa1 = np.random.randint(2, 5)
    saa = round(sa1 + (sade / 10), 1)

    sbb = np.random.randint(3, 8)
    scc = round(saa * sbb, 1)

    if scc - (scc // 1) == 0:
        scc = round(scc)


    stem = stem.format(spp=spp, saa=saa, sbb=sbb)
    answer = answer.format(scc=scc)
    comment = comment.format(spp=spp, saa=saa, sbb=sbb, scc=scc)

    return stem, answer, comment





















































# 5-2-4-유형03-5
def decimalmul524_Stem_019():
    stem = "{spp}이는 {sss}를 매일 $$수식$${saa} rm L$$/수식$$씩 마십니다. {spp}이가 $$수식$${sbb}$$/수식$$일 동안 마실 {sss}를 준비하려면 $$수식$$1 rm L$$/수식$$짜리 {sss}를 적어도 몇 개 사야 합니까?\n"
    answer = "(답): $$수식$${sdd}$$/수식$$ 개\n"
    comment = "(해설)\n" \
              "{sss}를 매일 $$수식$${saa} rm L$$/수식$$씩 $$수식$${sbb}$$/수식$$일 동안 마시려면 " \
              "{sss}가 $$수식$${saa} `Times` {sbb} `=` {scc} LEFT ( rm L RIGHT )$$/수식$$ 필요합니다.\n" \
              "따라서 $$수식$$1 rm L$$/수식$$짜리 {sss}를 적어도 $$수식$${sdd}$$/수식$$개 사야 합니다.\n\n"


    spp = ["혜영", "지영", "현준", "하윤", "은진", "주영", "서준", "도윤", "희철", "서윤", "나연", "유정", "희연", "새봄", "우중", "한솔"][
        np.random.randint(0, 16)]
    sss = ["우유", "사과주스", "딸기주스", "포도주스", "키위주스"][np.random.randint(0, 5)]

    while True:
        sade = np.random.randint(2, 10)
        saa = round(sade / 10, 1)
        sbb = np.random.randint(4, 10)
        if (sade != 5) and (sbb != 5) and ((saa * sbb) > 1.5):
            break

    scc = round(saa * sbb, 1)
    sdd = math.ceil(scc)


    stem = stem.format(spp=spp, sss=sss, saa=saa, sbb=sbb)
    answer = answer.format(sdd=sdd)
    comment = comment.format(sss=sss, saa=saa, sbb=sbb, scc=scc, sdd=sdd)

    return stem, answer, comment

















































# 5-2-4-유형03-6
def decimalmul524_Stem_020():
    stem = "{spp}이는 매일 $$수식$${saa}$$/수식$$시간 $$수식$${sbb}$$/수식$$분씩 {sss} 공부를 합니다. $$수식$${scc}$$/수식$$일 동안 {spp}이가 {sss} 공부를 한 시간은 모두 몇 시간입니까?\n"
    answer = "(답): $$수식$${see}$$/수식$$ 시간\n"
    comment = "(해설)\n" \
              "$$수식$${saa}$$/수식$$시간 $$수식$${sbb}$$/수식$$분 $$수식$$= {sdd}$$/수식$$시간이므로\n" \
              "$$수식$$LEFT ($$/수식$${spp}이가 {sss} 공부를 한 시간$$수식$$RIGHT )$$/수식$$\n$$수식$$ `=` {sdd} `Times` {scc} `=` {see} LEFT ($$/수식$$시간$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    spp = \
    ["주원", "은혁", "선정", "예준", "혜영", "지영", "현준", "하윤", "은진", "주영", "서준", "도윤", "희철", "서윤", "나연", "유정", "희연", "새봄", "우중",
     "한솔"][np.random.randint(0, 20)]

    sss = ["국어", "수학", "영어", "과학", "사회"][np.random.randint(0, 5)]

    saa = np.random.randint(1, 5)
    sbb = [15, 30, 45][np.random.randint(0, 3)]
    scc = np.random.randint(3, 8)
    sdd = round(saa + (sbb / 60), 2)
    see = round(sdd * scc, 2)

    if see - (see // 1) == 0:
        see = round(see)


    stem = stem.format(spp=spp, saa=saa, sbb=sbb, sss=sss, scc=scc)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, sdd=sdd, spp=spp, sss=sss, scc=scc, see=see)

    return stem, answer, comment




















































# 5-2-4-유형03-7
def decimalmul524_Stem_021():
    stem = "길이가 $$수식$${saa} rm {{cm}}$$/수식$$인 {sss} $$수식$${sbb}$$/수식$$장을 $$수식$${scc} rm {{cm}}$$/수식$$씩 겹치도록 한 줄로 길에 이어 붙였습니다. 이어 붙인 {sss} 전체 길이는 몇 $$수식$$rm {{cm}}$$/수식$$입니까?\n"
    answer = "(답): $$수식$${sgg} rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "{sss}가 $$수식$${sbb}$$/수식$$장이므로 겹친 부분은 $$수식$${sdd}$$/수식$$군데입니다.\n" \
              "$$수식$$LEFT ($$/수식$${sss} $$수식$${sbb}$$/수식$$장의 길이$$수식$$RIGHT ) `-` LEFT ($$/수식$$겹친 부분의 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$=` LEFT ( {saa} `Times` {sbb} RIGHT ) `-` LEFT ( {scc} `Times` {sdd} RIGHT )$$/수식$$\n$$수식$$ `=` {see} `-` {sff} `=` {sgg} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n\n"


    sss = ['색 테이프', '종이테이프', '종이띠'][np.random.randint(0, 3)]

    while True:
        sa = np.random.randint(51, 150)
        saa = round(sa / 10, 1)
        if (sa % 10) != 0:
            break

    sbb = np.random.randint(8, 20)

    while True:
        sc = np.random.randint(11, 30)
        scc = round(sc / 10, 1)
        if (sc % 10) != 0:
            break

    sdd = sbb - 1
    see = round(saa * sbb, 1)
    if see == (see // 1):
        see = int(see)

    sff = round(scc * sdd, 1)
    if sff == (sff // 1):
        sff = int(sff)

    sgg = round(see - sff, 1)
    if sgg == (sgg // 1):
        sgg = int(sgg)


    stem = stem.format(saa=saa, sss=sss, sbb=sbb, scc=scc)
    answer = answer.format(sgg=sgg)
    comment = comment.format(sss=sss, sbb=sbb, sdd=sdd, saa=saa, scc=scc, see=see, sff=sff, sgg=sgg)

    return stem, answer, comment














































# 5-2-4-유형04-1
def decimalmul524_Stem_022():
    stem = "한 변의 길이가 $$수식$${saa} rm m$$/수식$$인 마름모의 둘레는 몇 $$수식$$rm m$$/수식$$입니까?\n"
    answer = "(답): $$수식$${sbb} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "마름모는 네 변의 길이가 모두 같으므로\n" \
              "$$수식$$LEFT ($$/수식$$마름모의 둘레$$수식$$RIGHT )$$/수식$$\n$$수식$$ `=` LEFT ($$/수식$$한 변의 길이$$수식$$RIGHT ) `Times` 4$$/수식$$\n$$수식$$ `=` {saa} `Times` 4 `=` {sbb} LEFT ( rm m RIGHT )$$/수식$$입니다.\n\n"


    while True:
        sa = np.random.randint(3, 10)
        saa = round(sa / 10, 1)
        if sa != 5:
            break

    sbb = round(saa * 4, 1)
    if sbb - (sbb // 1) == 0:
        sbb = round(sbb)


    stem = stem.format(saa=saa)
    answer = answer.format(sbb=sbb)
    comment = comment.format(saa=saa, sbb=sbb)

    return stem, answer, comment

















































# 5-2-4-유형04-2
def decimalmul524_Stem_023():
    stem = "가로가 $$수식$${saa} rm {{cm}}$$/수식$$, 세로가 $$수식$${sbb} rm {{cm}}$$/수식$$인 직사각형의 둘레는 구하는 과정입니다. ㉠, ㉡에 알맞은 수로 짝지어진 것을 고르시오.\n$$표$$$$수식$$LEFT ($$/수식$$직사각형의 둘레$$수식$$RIGHT ) `=` LEFT ( LEFT ($$/수식$$가로$$수식$$RIGHT ) `+` LEFT ($$/수식$$세로$$수식$$RIGHT ) RIGHT ) `Times`$$/수식$$㉠$$수식$$= LEFT ( {saa} `+` {sbb} RIGHT ) `Times`$$/수식$$㉠$$수식$$`=`$$/수식$$㉡$$수식$$LEFT ( rm {{cm}} RIGHT )$$/수식$$$$/표$$\n{circle_one} {x1}\n{circle_two} {x2}\n{circle_three} {x3}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$직사각형의 둘레$$수식$$RIGHT ) `=` LEFT ($$/수식$$가로$$수식$$RIGHT ) `+` LEFT ($$/수식$$세로$$수식$$RIGHT ) `+` LEFT ($$/수식$$가로$$수식$$RIGHT ) `+` LEFT ($$/수식$$세로$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ( LEFT ($$/수식$$가로$$수식$$RIGHT ) `+` LEFT ($$/수식$$세로$$수식$$RIGHT ) RIGHT ) `Times` 2$$/수식$$\n" \
              "$$수식$$= LEFT ( {saa} `+` {sbb} RIGHT ) `Times` {sa}$$/수식$$\n" \
              "$$수식$$= {scc} `Times` {sa} `=` {sb} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n\n"


    while True:
        sade = np.random.randint(1, 10)
        sa1 = np.random.randint(5, 10)
        saa = round(sa1 + (sade / 10), 1)
        sbde = np.random.randint(1, 10)
        sb1 = np.random.randint(3, 8)
        sbb = round(sb1 + (sbde / 10), 1)
        scc = round(saa + sbb, 1)
        if scc - (scc // 1) != 0:
            break

    sa = 2
    sb = round(scc * sa, 1)

    if sb - (sb // 1) == 0:
        sb = round(sb)

    sc = 3
    sd = round(scc * sc, 1)
    se = 4
    sf = round(scc * se, 1)

    if sf - (sf // 1) == 0:
        sf = round(sf)

    y1 = "%s $$수식$$%d$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", sa, "㉡", sb)
    y2 = "%s $$수식$$%d$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", sc, "㉡", sd)
    y3 = "%s $$수식$$%d$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", se, "㉡", sf)

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [x1, x2, x3] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):
        if sdx == y1:
            correct_idx = idx
            break


    stem = stem.format(saa=saa, sbb=sbb, x1=x1, x2=x2, x3=x3, circle_one=circle_one, circle_two=circle_two,
                       circle_three=circle_three)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(saa=saa, sbb=sbb, sa=sa, scc=scc, sb=sb)

    return stem, answer, comment


















































# 5-2-4-유형04-3
def decimalmul524_Stem_024():
    stem = "다음 도형의 둘레는 몇 $$수식$$rm m$$/수식$$입니까?\n$$표$$● {sss}입니다.\n● 한 변의 길이가 $$수식$${saa} rm m$$/수식$$입니다.$$/표$$\n"
    answer = "(답): $$수식$${scc} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${sss}의 둘레$$수식$$RIGHT )$$/수식$$\n$$수식$$ `=` LEFT ($$/수식$$한 변의 길이$$수식$$RIGHT ) `Times` {sbb}$$/수식$$\n$$수식$$ `=` {saa} `Times` {sbb} `=` {scc} LEFT ( rm m RIGHT )$$/수식$$\n\n"


    sss = ["정삼각형", "정사각형", "정오각형", "정육각형", "정칠각형", "정팔각형", "정구각형"][np.random.randint(0, 7)]

    while True:
        sa = np.random.randint(31, 100)
        saa = round(sa / 100, 2)
        if sa % 10 != 0:
            break

    sbb = 3

    temp_list = ["정삼각형", "정사각형", "정오각형", "정육각형", "정칠각형", "정팔각형", "정구각형"]

    for idx, sdx in enumerate(temp_list):
        if sdx == sss:
            sbb += idx
            break

    scc = round(saa * sbb, 2)

    if scc - (scc // 1) == 0:
        scc = round(scc)


    stem = stem.format(sss=sss, saa=saa)
    answer = answer.format(scc=scc)
    comment = comment.format(sss=sss, sbb=sbb, saa=saa, scc=scc)

    return stem, answer, comment





















































# 5-2-4-유형04-4
def decimalmul524_Stem_025():
    stem = "두 변의 길이가 각각 $$수식$${saa} rm {{cm}}$$/수식$$, $$수식$${sbb} rm {{cm}}$$/수식$$인 평행사변형이 있습니다. 이 평행사변형의 둘레는 몇 $$수식$$rm {{cm}}$$/수식$$입니까?\n"
    answer = "(답): $$수식$${sdd} rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$평행사변형의 둘레$$수식$$RIGHT )$$/수식$$\n$$수식$$ `=` LEFT ( LEFT ($$/수식$$한 변의 길이" \
              "$$수식$$RIGHT ) `+` LEFT ($$/수식$$다른 한 변의 길이$$수식$$RIGHT ) RIGHT ) `Times` 2$$/수식$$\n" \
              "$$수식$$= LEFT ( {saa} `+` {sbb} RIGHT ) `Times` 2$$/수식$$\n" \
              "$$수식$$= {scc} `Times` 2 `=` {sdd} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n\n"


    while True:
        sade = np.random.randint(1, 100)
        sa1 = np.random.randint(2, 5)
        saa = round(sa1 + (sade / 100), 2)
        sbde = np.random.randint(1, 100)
        sb1 = np.random.randint(3, 6)
        sbb = round(sb1 + (sbde / 100), 2)
        scc = round(saa + sbb, 2)

        if ((sade % 10) != 0) and ((sbde % 10) != 0) and (scc - (scc // 1) != 0):
            break

    sdd = round(scc * 2, 2)

    if sdd - (sdd // 1) == 0:
        sdd = round(sdd)


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(sdd=sdd)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)

    return stem, answer, comment

















































# 5-2-4-유형04-5
def decimalmul524_Stem_026():
    stem = "한 변의 길이가 $$수식$${saa} rm m$$/수식$$인 {s1}의 둘레와 한 변의 길이가 $$수식$${sbb} rm m$$/수식$$인 {s2}의 둘레의 차는 몇 $$수식$$rm m$$/수식$$입니까?\n"
    answer = "(답): $$수식$${see} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${s1}의 둘레$$수식$$RIGHT )$$/수식$$\n$$수식$$ `=` LEFT ($$/수식$$한 변의 길이$$수식$$RIGHT ) `Times` {sa}$$/수식$$\n$$수식$$ `=` {saa} `Times` {sa} `=` {scc} LEFT ( rm m RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${s2}의 둘레$$수식$$RIGHT )$$/수식$$\n$$수식$$ `=` LEFT ($$/수식$$한 변의 길이$$수식$$RIGHT ) `Times` {sb}$$/수식$$\n$$수식$$ `=` {sbb} `Times` {sb} `=` {sdd} LEFT ( rm m RIGHT )$$/수식$$\n" \
              "→ $$수식$$LEFT ($$/수식$$두 정다각형의 둘레의 차$$수식$$RIGHT ) `=` {sc} `-` {sd} `=` {see} LEFT ( rm m RIGHT )$$/수식$$\n\n"


    while True:
        s1 = ["정삼각형", "정사각형", "정오각형", "정육각형", "정칠각형", "정팔각형", "정구각형"][np.random.randint(0, 7)]
        s2 = ["정삼각형", "정사각형", "정오각형", "정육각형", "정칠각형", "정팔각형", "정구각형"][np.random.randint(0, 7)]
        if s1 != s2:
            break

    saade = np.random.randint(5, 10)
    saa = round(saade / 10, 1)
    sbbde = np.random.randint(5, 10)
    sbb = round(sbbde / 10, 1)

    temp_list = ["정삼각형", "정사각형", "정오각형", "정육각형", "정칠각형", "정팔각형", "정구각형"]

    sa = 3
    for idx, sdx in enumerate(temp_list):
        if sdx == s1:
            sa += idx
            break

    sb = 3
    for tdx, udx in enumerate(temp_list):
        if udx == s2:
            sb += tdx
            break

    scc = round(saa * sa, 1)
    sdd = round(sbb * sb, 1)

    if (scc - sdd) >= 0:
        sc = scc
        sd = sdd
    elif (scc - sdd) < 0:
        sc = sdd
        sd = scc

    see = round(abs(scc - sdd), 1)

    if see - (see // 1) == 0:
        see = round(see)


    stem = stem.format(saa=saa, s1=s1, sbb=sbb, s2=s2)
    answer = answer.format(see=see)
    comment = comment.format(s1=s1, sa=sa, saa=saa, scc=scc, s2=s2, sb=sb, sbb=sbb, sdd=sdd, sc=sc, sd=sd, see=see)

    return stem, answer, comment




















































# 5-2-4-유형04-6
def decimalmul524_Stem_027():
    stem = "다음 두 정다각형의 둘레의 합은 몇 $$수식$$rm {{cm}}$$/수식$$입니까?\n$$표$$● 한 변의 길이가 $$수식$${saa} rm {{cm}}$$/수식$$인 {s1}\n● 한 변의 길이가 $$수식$${sbb} rm {{cm}}$$/수식$$인 {s2}$$/표$$\n"
    answer = "(답): $$수식$${see} rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${s1}의 둘레$$수식$$RIGHT )$$/수식$$\n$$수식$$ `=` LEFT ($$/수식$$한 변의 길이$$수식$$RIGHT ) `Times` {sa}$$/수식$$\n$$수식$$ `=` {saa} `Times` {sa} `=` {scc} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${s2}의 둘레$$수식$$RIGHT )$$/수식$$\n$$수식$$ `=` LEFT ($$/수식$$한 변의 길이$$수식$$RIGHT ) `Times` {sb}$$/수식$$\n$$수식$$ `=` {sbb} `Times` {sb} `=` {sdd} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n" \
              "→ $$수식$$LEFT ($$/수식$$두 정다각형의 둘레의 합$$수식$$RIGHT ) `=` {scc} `+` {sdd}$$/수식$$\n$$수식$$ `=` {see} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n\n"


    while True:
        s1 = ["정삼각형", "정사각형", "정오각형", "정육각형", "정칠각형", "정팔각형", "정구각형"][np.random.randint(0, 7)]
        s2 = ["정삼각형", "정사각형", "정오각형", "정육각형", "정칠각형", "정팔각형", "정구각형"][np.random.randint(0, 7)]
        if s1 != s2:
            break

    saade = np.random.randint(1, 10)
    saa1 = np.random.randint(4, 10)
    saa = round(saa1 + (saade / 10), 1)

    sbbde = np.random.randint(1, 10)
    sbb1 = np.random.randint(4, 10)
    sbb = round(sbb1 + (sbbde / 10), 1)

    temp_list = ["정삼각형", "정사각형", "정오각형", "정육각형", "정칠각형", "정팔각형", "정구각형"]
    sa = 3
    for idx, sdx in enumerate(temp_list):
        if sdx == s1:
            sa += idx
            break
    sb = 3
    for tdx, udx in enumerate(temp_list):
        if udx == s2:
            sb += tdx
            break

    scc = round(saa * sa, 1)
    if scc - (scc // 1) == 0:
        scc = round(scc)

    sdd = round(sbb * sb, 1)
    if sdd - (sdd // 1) == 0:
        sdd = round(sdd)

    see = round(scc + sdd, 1)
    if see - (see // 1) == 0:
        see = round(see)


    stem = stem.format(saa=saa, s1=s1, sbb=sbb, s2=s2)
    answer = answer.format(see=see)
    comment = comment.format(sa=sa, saa=saa, scc=scc, sb=sb, sbb=sbb, sdd=sdd, see=see, s1=s1, s2=s2)

    return stem, answer, comment






















































# 5-2-4-유형05-1
def decimalmul524_Stem_028():
    stem = "소수의 곱셈을 분수의 곱셈으로 계산하려고 합니다. ㉠, ㉡, ㉢, ㉣에 알맞은 수로 짝지어진 것을 고르시오.\n$$표$$$$수식$$ {s1} TIMES {s2} = {s1} TIMES {f1} = {sc} over {n1} = {f3} over {n1} = LEFT ( {c4} RIGHT ) $$/수식$$$$/표$$\n① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${s1} TIMES {s2} = {s1} TIMES {s3} over {n1} = {k2} over {n1} = {s4} over {n1} = {s5} $$/수식$$ 입니다.\n\n"


    while True:
        s1 = np.random.randint(2, 10)
        ss2 = np.random.randint(2, 10)
        s2 = round(ss2 * 0.1, 1)
        if 1 < (s1 * s2) and (s1 != ss2):
            break

    # s1 = A, s2 = B, s3 = C, s4=D, s5=E, t1 = a, t2 = b
    s3 = round(s2 * 10)
    s4 = round(s1 * s3)
    s5 = round(s4 * 0.1, 1)
    if s5 - (s5 // 1) == 0:
        s5 = round(s5)
    t1 = int(s2 * 10)
    t2 = int(s1 * t1)
    t3 = round(int(t2) * 0.1, 1)
    t4 = s1
    t5 = s1 * t4
    t6 = t5 * 0.1
    t7 = round(int(t2) * 0.01, 2)
    t8 = round(t5 * 0.01, 2)

    k2 = "{%s `TIMES` %s}" % (s1, s3)
    sc = "{ %d TIMES LEFT ( ㉡ RIGHT ) }" % s1

    c1 = "㉠"
    c2 = "㉡"
    c3 = "㉢"
    c4 = "㉣"
    n1 = 10

    f1 = "{{ LEFT ( %s RIGHT )} over %s}" % (c1, n1)
    f3 = "{ LEFT ( %s RIGHT ) }" % c3

    y1 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", t1, "㉡", t1, "㉢", t2, "㉣", t3)
    y2 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", t4, "㉡", t4, "㉢", t5, "㉣", t6)
    y3 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", t1, "㉡", t1, "㉢", t2, "㉣", t7)
    y4 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", t4, "㉡", t4, "㉢", t5, "㉣", t8)
    y5 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", t1, "㉡", t1, "㉢", t2, "㉣", t2)
    candidates = [y1, y2, y3, y4, y5]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4, x5] = candidates

    correct_idx = 0

    for idx, sdx in enumerate(candidates):
        if sdx == y1:
            correct_idx = idx
            break


    stem = stem.format(s1=s1, s2=s2, n1=n1, c1=c1, c3=c3, c4=c4, sc=sc, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, f1=f1, f3=f3)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, n1=n1, k2=k2)

    return stem, answer, comment




















































# 5-2-4-유형05-2
def decimalmul524_Stem_029():
    stem = "자연수의 곱셈을 이용하여 $$수식$${s1} TIMES {s2}$$/수식$${rur1} 계산하시오.\n$$표$$$$수식$${s6}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${s2}$$/수식$${eun1} $$수식$${s3}$$/수식$$의 $$수식$${n1} over {n2}$$/수식$$배이므로 " \
              "$$수식$${s1} TIMES {s2}$$/수식$${eun1} $$수식$${s4}$$/수식$$의 $$수식$${n1} over {n2}$$/수식$$배인 $$수식$${s5}$$/수식$${ga1} 됩니다.\n\n"


    while True:
        s1 = np.random.randint(21, 100)
        ss2 = np.random.randint(2, 10)
        s2 = round(ss2 * 0.01, 2)
        if 1 < s1 * s2:
            break

    s3 = int(s2 * 100)
    s4 = s1 * s3
    s5 = round(s4 / 100, 2)

    if s5 - (s5 // 1) == 0:
        s5 = round(s5)

    s6 = "%d TIMES %d = %d" % (s1, s3, s4)
    n1 = 1
    n2 = 100

    rur1 = josa(s2, "를")
    eun1 = josa(s2, "는")
    ga1 = josa(s5, "가")


    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, rur1=rur1)
    answer = answer.format(a1=s5)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, n1=n1, n2=n2, eun1=eun1, ga1=ga1)

    return stem, answer, comment



















































# 5-2-4-유형05-3
def decimalmul524_Stem_030():
    stem = "계산해 보시오.\n$$수식$${s1} TIMES {s2}$$/수식$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${s1} TIMES {s3} = {s4}$$/수식$$이고 $$수식$${s2}$$/수식$${eun1} " \
              "$$수식$${s3}$$/수식$$의 $$수식$${n1} over {n2}$$/수식$$배이므로 " \
              "곱도 $$수식$${n1} over {n2}$$/수식$$배인 $$수식$${s5}$$/수식$$입니다.\n\n"


    while True:
        s1 = np.random.randint(2, 10)
        s2 = np.random.randint(1, 100)
        s2 = s2 * 0.01
        s2 = round(s2, 2)
        if 1 < s1 * s2:
            break

    s3 = int(s2 * 100)
    s4 = s1 * s3
    s5 = s4 / 100

    n1 = 1
    n2 = 100

    eun1 = josa(s2, "는")


    stem = stem.format(s1=s1, s2=s2)
    answer = answer.format(a1=s5)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, n1=n1, n2=n2, eun1=eun1)

    return stem, answer, comment


















































# 5-2-4-유형05-4
def decimalmul524_Stem_031():
    stem = "㉠과 ㉡의 차를 구하시오.\n$$표$$㉠ $$수식$${s1} TIMES {s2}$$/수식$$      ㉡ $$수식$${s3} TIMES {s4}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${s1} TIMES {s2} = {s5}$$/수식$$, ㉡ $$수식$${s3} TIMES {s4} = {s6}$$/수식$$\n" \
              "따라서 ㉠과 ㉡의 차는 $$수식$${s7} - {s8} = {s9}$$/수식$$입니다.\n\n"


    # A, C, B, D
    while True:
        s1 = np.random.randint(13, 30)
        s3 = np.random.randint(13, 30)
        ss2 = np.random.randint(2, 10)
        s2 = round(0.1 * ss2, 1)
        ss4 = np.random.randint(12, 100)
        s4 = round(0.01 * ss4, 2)

        if (s1 != 20) and (s3 != 20) and (((s1 * s2) - (s3 * s4)) > -1) and (((s1 * s2) - (s3 * s4)) < 1) and (
                s4 != ((s1 * s2) / s3)):
            break

    s4 = round(s4, 2)
    s5 = s1 * s2
    s5 = round(s5, 2)
    s6 = s3 * s4
    s6 = round(s6, 2)

    if ((s1 * s2) - (s3 * s4)) >= 0:
        s7 = s5
        s8 = s6

    elif ((s1 * s2) - (s3 * s4)) < 0:
        s7 = s6
        s8 = s5

    s9 = s7 - s8
    s9 = round(s9, 2)


    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4)
    answer = answer.format(a1=s9)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, s8=s8, s9=s9)

    return stem, answer, comment
























































# 5-2-4-유형05-5
def decimalmul524_Stem_032():
    stem = "다음 중 곱이 가장 큰 것은 어느 것입니까?\n① $$수식$${sa} TIMES {sb}$$/수식$$\n② $$수식$${sc} TIMES {sd}$$/수식$$\n③ $$수식$${se} TIMES {sf}$$/수식$$\n④ $$수식$${sg} TIMES {sh}$$/수식$$\n⑤ $$수식$${si} TIMES {sj}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "① $$수식$${sa} TIMES {sb} = {ca}$$/수식$$\n" \
              "② $$수식$${sc} TIMES {sd} = {cb}$$/수식$$\n" \
              "③ $$수식$${se} TIMES {sf} = {cc}$$/수식$$\n" \
              "④ $$수식$${sg} TIMES {sh} = {cd}$$/수식$$\n" \
              "⑤ $$수식$${si} TIMES {sj} = {ce}$$/수식$$\n\n"


    while True:
        sa = np.random.randint(11, 36)
        sbb = np.random.randint(2, 10)
        sb = round(sbb * 0.1, 1)
        sc = np.random.randint(5, 10)
        sdd = np.random.randint(2, 10)
        sd = round(sdd * 0.1, 1)
        se = np.random.randint(11, 36)
        sff = np.random.randint(10, 100)
        sf = round(sff * 0.01, 2)
        sg = np.random.randint(11, 36)
        shh = np.random.randint(10, 100)
        sh = round(shh * 0.01, 2)
        si = np.random.randint(11, 36)
        sjj = np.random.randint(10, 100)
        sj = round(sjj * 0.01, 2)
        ca = round(sa * sb, 2)
        cb = round(sc * sd, 2)
        cc = round(se * sf, 2)
        cd = round(sg * sh, 2)
        ce = round(si * sj, 2)

        if (sa != 20) and (sa != 30) and (sb * sa > 4) and (sb * sa < 7) and (sd * sc > 4) and (sd * sc < 7) and (
                se != sa) and (se != 20) and (se != 30) and (sf * se > 4) and (sf * se < 7) and (sg != sa) and (
                sg != se) and (sg != 20) and (sg != 30) and (sg * sh > 4) and (sh * sh < 7) and (si != sa) and (
                si != se) and (si != sg) and (si != 20) and (si != 30) and (si * sj > 4) and (si * sj < 7) and (
                ca != cb) and (ca != cc) and (ca != cd) and (ca != ce) and (cb != cc) and (cb != cd) and (
                cb != ce) and (cc != cd) and (cc != ce) and (cd != ce):
            break

    if ca - (ca // 1) == 0:
        ca = round(ca)
    if cb - (cb // 1) == 0:
        cb = round(cb)
    if cc - (cc // 1) == 0:
        cc = round(cc)
    if cd - (cd // 1) == 0:
        cd = round(cd)
    if ce - (ce // 1) == 0:
        ce = round(ce)

    candidates = [ca, cb, cc, cd, ce]

    max = 0

    for i in candidates:
        if max < i:
            max = i

    correct_idx = 0

    for i, s in enumerate(candidates):
        if s == max:
            correct_idx = i
            break


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sh=sh, si=si, sj=sj)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sh=sh, si=si, sj=sj, ca=ca, cb=cb, cc=cc,
                             cd=cd, ce=ce)

    return stem, answer, comment




















































# 5-2-4-유형05-6
def decimalmul524_Stem_033():
    stem = "가로가 $$수식$${sa} rm m$$/수식$$, 세로가 $$수식$${sb} rm m$$/수식$$인 직사각형의 넓이는 몇 $$수식$$rm m^{n1}$$/수식$$인지 구하시오.\n"
    answer = "(답): $$수식$${a1} rm m^{n1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$직사각형의 넓이$$수식$$RIGHT ) = ($$/수식$$가로$$수식$$RIGHT ) TIMES LEFT ($$/수식$$" \
              "세로$$수식$$RIGHT ) = {sa} TIMES {sb} = {sc} LEFT ( rm m^{n1} RIGHT )$$/수식$$\n\n"


    sa = np.random.randint(2, 10)

    while True:
        sbb = np.random.randint(2, 10)
        sb = round(sbb * 0.1, 1)
        if sa * sb > 1:
            break

    sc = round(sa * sb, 1)
    if sc - (sc // 1) == 0:
        sc = round(sc)

    n1 = 2


    stem = stem.format(sa=sa, sb=sb, n1=n1)
    answer = answer.format(a1=sc, n1=n1)
    comment = comment.format(sa=sa, sb=sb, sc=sc, n1=n1)

    return stem, answer, comment




















































# 5-2-4-유형05-7
def decimalmul524_Stem_034():
    stem = "계산 결과를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 써넣으려고 합니다. 알맞은 기호를 고르시오.\n$$수식$${sa} `Times` 0.{sb}{sc}$$/수식$$ ○ $$수식$${sd} `Times` 0.{se}{sf}$$/수식$$\n{circle_one} $$수식$$&gt;$$/수식$$\n{circle_two} $$수식$$=$$/수식$$\n{circle_three} $$수식$$&lt;$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${sa} `Times` 0.{sb}{sc} `=` {saa}$$/수식$$, " \
              "$$수식$${sd} `Times` 0.{se}{sf} `=` {sbb}$$/수식$$\n" \
              "→ $$수식$${saa}````{scc}````{sbb}$$/수식$$\n\n"


    while True:
        sa = np.random.randint(3, 10)
        sb = np.random.randint(3, 10)
        sc = np.random.randint(3, 10)
        sf = np.random.randint(3, 10)
        se = 11 - sb
        sd = np.random.randint(2, 10)

        if (((sa * sb - 10) / se) <= sd) and (sd <= ((sa * sb + 10) / se)) and (sa != sd):
            break

    saa = round(sa * ((sb * 10 + sc) / 100), 2)
    if saa - (saa // 1) == 0:
        saa = int(saa)

    sbb = round(sd * ((se * 10 + sf) / 100), 2)
    if sbb - (sbb // 1) == 0:
        sbb = int(sbb)

    if saa - sbb > 0:
        scc = '&gt;'
        a1 = '①'

    elif saa - sbb == 0:
        scc = '='
        a1 = '②'

    elif saa - sbb < 0:
        scc = '&lt;'
        a1 = '③'


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, circle_one=circle_one, circle_two=circle_two,
                       circle_three=circle_three)
    answer = answer.format(a1=a1)
    comment = comment.format(sa=sa, sb=sb, sc=sc, saa=saa, sd=sd, se=se, sf=sf, sbb=sbb, scc=scc)

    return stem, comment, answer


















































# 5-2-4-유형06-1
def decimalmul524_Stem_035():
    stem = "소수의 곱셈을 보기와 같이 분수의 곱셈으로 계산하려고 합니다. $$수식$$LEFT ( ```` RIGHT )$$/수식$$ 안에 알맞은 수의 합을 구하시오.\n$$표$$보기\n$$수식$$ {n1} TIMES {n2} = {n1} TIMES {nk} = {k1} over {n4} = {n5} over {n4} = {n6} $$/수식$$$$/표$$\n$$수식$$ {sa} TIMES {sb} = {sa} TIMES {f1} = {k2} over {n4} = {f2} over {n4} = {f2}$$/수식$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa} TIMES {sb} = {sa} TIMES {g1} = {k3} over {n4} = {g2} over {n4} = LEFT ( {se} RIGHT )$$/수식$$ 이므로 " \
              "$$수식$$LEFT ( ```` RIGHT )$$/수식$$ 안에 알맞은 수의 합은 $$수식$${sc} + {sc} + {sd} + {se} = {sf}$$/수식$$입니다.\n\n"


    n1 = 7
    n2 = 1.4
    n3 = 14
    n4 = 10
    n5 = 98
    n6 = 9.8

    k1 = "{ %s `Times` %s}" % (n1, n3)
    nk = "{ %s over %s }" % (n3, n4)

    while True:
        sa = np.random.randint(2, 10)
        sbb = np.random.randint(12, 100)
        sb = round(sbb * 0.1, 1)

        if (sa == 7) and (sbb == 14):
            continue
        elif 10 < (sa * sb):
            break

    k2 = "{ %s `Times` LEFT ( ```` RIGHT )}" % (sa)

    sc = int(sb * 10)
    sd = sa * sc
    se = round(sd * 0.1, 1)
    if se - (se // 1) == 0:
        se = round(se)

    sf = 2 * sc + sd + se
    k3 = "{ %s `Times` LEFT ( %d RIGHT ) }" % (sa, sc)

    f1 = "{ LEFT ( ```` RIGHT ) } over 10"
    f2 = "{LEFT ( ```` RIGHT )}"

    g1 = "{ LEFT ( %s RIGHT ) } over %s" % (sc, n4)
    g2 = "{LEFT ( %s RIGHT )}" % sd


    stem = stem.format(sa=sa, sb=sb, n1=n1, n2=n2, n4=n4, n5=n5, n6=n6, k1=k1, k2=k2, f1=f1, f2=f2, nk=nk)
    answer = answer.format(a1=sf)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, n4=n4, k3=k3, g1=g1, g2=g2)

    return stem, answer, comment



















































# 5-2-4-유형06-2
def decimalmul524_Stem_036():
    stem = "자연수의 곱셈을 이용하여 $$수식$${s1} TIMES {s2}$$/수식$${rur1} 계산하시오.\n$$표$$$$수식$${s6}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${s2}$$/수식$${eun1} $$수식$${s3}$$/수식$$의 $$수식$${n1} over {n2}$$/수식$$배이므로 " \
              "$$수식$${s1} TIMES {s2}$$/수식$${eun1} $$수식$${s4}$$/수식$$의 $$수식$${n1} over {n2}$$/수식$$배인 $$수식$${s5}$$/수식$${ga1} 됩니다.\n\n"


    s1 = np.random.randint(3, 10)

    while True:
        ss2 = np.random.randint(31, 99)
        s2 = round(ss2 * 0.1, 1)
        if 20 < s1 * s2:
            break
    if s2 - (s2 // 1) == 0:
        s2 = round(s2)

    s3 = int(s2 * 10)
    s4 = int(s1 * s3)
    s5 = round(s4 / 10, 1)

    if s5 - (s5 // 1) == 0:
        s5 = round(s5)

    s6 = "%d TIMES %d = %d" % (s1, s3, s4)
    n1 = 1
    n2 = 10

    rur1 = josa(s2, "를")
    eun1 = josa(s2, "은")
    ga1 = josa(s5, "가")


    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, rur1=rur1)
    answer = answer.format(a1=s5)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, n1=n1, n2=n2, eun1=eun1, ga1=ga1)

    return stem, answer, comment
















































# 5-2-4-유형06-3
def decimalmul524_Stem_037():
    stem = "빈칸에 알맞은 수를 구하시오.\n$$수식$$LEFT ( {b1} RIGHT )$$/수식$$ → $$수식$$LEFT ( {b2} RIGHT )$$/수식$$ → $$수식$$LEFT ( {su} RIGHT )$$/수식$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${s1} TIMES {s3} = {s4}$$/수식$$이고, " \
              "$$수식$${s2}$$/수식$${eun1} $$수식$${s3}$$/수식$$의 $$수식$${n1} over {n2}$$/수식$$배이므로 " \
              "곱도 $$수식$${n1} over {n2}$$/수식$$배인 $$수식$${s5}$$/수식$$입니다.\n\n"


    while True:
        ss1 = np.random.randint(2, 10)
        s1 = ss1 * 10
        ss2 = np.random.randint(205, 600)
        s2 = round(ss2 / 100, 2)

        if (100 < (s1 * s2)) and (ss2 % 5 == 0) and (ss2 % 10 != 0):
            break

    s3 = round(s2 * 100)
    s4 = s1 * s3
    s5 = round(s4 / 100, 2)

    if s5 - (s5 // 1) == 0:
        s5 = round(s5)

    n1 = 1
    n2 = 100
    su = "```` ```` ````"
    b1 = s1
    b2 = " TIMES %s " % (s2)

    eun1 = josa(s2, "은")


    stem = stem.format(s1=s1, s2=s2, su=su, b1=b1, b2=b2)
    answer = answer.format(a1=s5)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, n1=n1, n2=n2, eun1=eun1)

    return stem, answer, comment



















































# 5-2-4-유형06-4
def decimalmul524_Stem_038():
    stem = "계산 결과를 비교하여 곱이 더 큰 것을 찾아 기호를 쓰시오.\n$$표$$ㄱ. $$수식$${sa} TIMES {sb}.{sc}$$/수식$$      ㄴ. $$수식$${sd} TIMES {se}.{sf}$$/수식$$$$/표$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "ㄱ. $$수식$${sa} TIMES {sb}.{sc} = {ca}$$/수식$$, ㄴ. $$수식$${sd} TIMES {se}.{sf} = {cb}$$/수식$$\n" \
              "따라서 곱이 가장 더 큰 것의 기호를 쓰면 {a1}입니다.\n\n"


    sa = np.random.randint(3, 10)
    sb = np.random.randint(3, 10)
    sc = np.random.randint(3, 10)
    sf = np.random.randint(3, 10)

    se = 10 - sb

    while True:
        sd = np.random.randint(2, 1000)

        if ((sa * sb - 10) / se <= sd) and ((sa * sb + 10) / se >= sd):
            break

    ca = round(sa * (sb + 0.1 * sc), 1)
    if ca - (ca // 1) == 0:
        ca = round(ca)

    cb = round(sd * (se + 0.1 * sf), 1)
    if cb - (cb // 1) == 0:
        cb = round(cb)

    maxnum = max(ca, cb)
    correct_idx = 0

    if maxnum == ca:
        correct_idx = 0
    elif maxnum == cb:
        correct_idx = 1


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf)
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, ca=ca, cb=cb, a1=answer_kodict[correct_idx])

    return stem, answer, comment




















































# 5-2-4-유형06-5
def decimalmul524_Stem_039():
    stem = "밑변의 길이가 $$수식$${sa} rm {{cm}}$$/수식$$, 높이가 $$수식$${sb} rm {{cm}}$$/수식$$인 평행사변형의 넓이는 몇 $$수식$$rm {{cm}}^{n1}$$/수식$$인지 구하시오.\n"
    answer = "(답): $$수식$${a1}``rm {{cm}}^{n1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$평행사변형의 넓이$$수식$$RIGHT )$$/수식$$\n$$수식$$ = LEFT ($$/수식$$밑변$$수식$$RIGHT ) TIMES LEFT ($$/수식$$" \
              "높이$$수식$$RIGHT ) = {sa} TIMES {sb} = {sc}``LEFT ( rm {{cm}}^{n1} RIGHT )$$/수식$$\n\n"


    sa = np.random.randint(2, 10)

    while True:
        sbb = np.random.randint(12, 99)
        sb = round(sbb * 0.1, 1)

        if (sa * sb > 10) and (sbb % 10 != 0):
            break
    if sb - (sb // 1) == 0:
        sb = round(sb)

    sc = round(sa * sb, 1)
    if sc - (sc // 1) == 0:
        sc = round(sc)

    n1 = 2


    stem = stem.format(sa=sa, sb=sb, n1=n1)
    answer = answer.format(a1=sc, n1=n1)
    comment = comment.format(sa=sa, sb=sb, sc=sc, n1=n1)

    return stem, answer, comment






















































# 5-2-4-유형06-6
def decimalmul524_Stem_040():
    stem = "계산 결과가 {s} 보다 큰 것을 모두 고르시오.\n{circle_one} {s}$$수식$$TIMES {sa}$$/수식$$\n{circle_two} {s}$$수식$$TIMES {sb}$$/수식$$\n{circle_three} {s}$$수식$$TIMES {sc}$$/수식$$\n{circle_four} {s}$$수식$$TIMES {sd}$$/수식$$\n"
    answer = "(답): {a1}, {a2}\n"
    comment = "(해설)\n" \
              "계산 결과가 곱해지는 수보다 큰 수가 되려면 곱해지는 수에 $$수식$$1$$/수식$$보다 큰 수를 곱해야 합니다.\n"


    s = ["가", "㉠", "□", "■", "♠", "♥", "♣"][np.random.randint(0, 7)]

    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = np.random.randint(1, 10)
    d = np.random.randint(1, 10)

    sa = round(0.9 + 0.01 * a, 2)
    sb = round(1 + 0.01 * b, 2)
    sc = round(10 + 0.1 * c, 1)
    sd = round(0.1 * d, 1)

    candidates = [sa, sb, sc, sd]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4] = candidates

    ans_list = []

    for idx, sdx in enumerate(candidates):
        if sdx > 1:
            ans_list.append(idx)


    stem = stem.format(s=s, sa=x1, sb=x2, sc=x3, sd=x4, circle_one=circle_one, circle_two=circle_two,
                       circle_three=circle_three, circle_four=circle_four)
    answer = answer.format(a1=answer_dict[(ans_list[0])], a2=answer_dict[(ans_list[1])])

    return stem, answer, comment















































# 5-2-4-유형06-7
def decimalmul524_Stem_041():
    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 자연수 중에서 □ 안에 들어갈 수 있는 수를 모두 구하시오.\n$$표$$$$수식$$`{sa}`times`{sb}.{sc}{sd}`&lt;`{se}{sf}.$$/수식$$□$$/표$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`times`{sb}.{sc}{sd}`=`{se}{sf}.{sg}`$$/수식$$\n" \
              "따라서 $$수식$$`{se}{sf}.{sg}`&lt;`{se}{sf}.□`$$/수식$$이므로 " \
              "□ 안에 들어갈 수 있는 자연수는 $$수식$${sn}$$/수식$$입니다.\n\n"


    sb = [3, 5, 7, 9][np.random.randint(0, 4)]

    while True:
        sa = [4, 6, 8][np.random.randint(0, 3)]
        sc = [0, 1, 3, 5][np.random.randint(0, 4)]
        if (sa * sc) != 6:
            break

    sd = 5
    nlist = []

    # a X b.cd
    num = round(sb + (0.1 * sc) + (0.01 * sd), 2)
    num = round(sa * num, 1)

    se = int(num / 10)
    sf = int(num % 10)
    ef = se * 10 + sf

    sg = round(round(num - ef, 1) * 10)

    for i in range(sg + 1, 10):
        nlist.append(str(i))

    sn = ', ````'.join(nlist)


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf)
    answer = answer.format(a1=sn)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sn=sn)

    return stem, answer, comment


















































# 5-2-4-유형07-1
def decimalmul524_Stem_042():
    stem = "{p}이는 {s1}에 길이가 $$수식$${sa} rm {{cm}}$$/수식$$인 {s2}{j1} 세우고 그림자의 길이를 재었더니 {s2}의 길이가 $$수식$${sb}$$/수식$$배였습니다. 그림자의 길이는 몇 $$수식$$rm {{cm}}$$/수식$$입니까?\n"
    answer = "(답): $$수식$${a1} rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$그림자의 길이$$수식$$RIGHT )$$/수식$$\n$$수식$$ = LEFT ($$/수식$${s2}의 길이$$수식$$RIGHT ) TIMES {sb} = {sa} TIMES {sb} = {sc} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n\n"


    p = \
    ["은진", "주영", "서준", "도윤", "주원", "은혁", "선정", "예준", "혜영", "지영", "현준", "하윤", "은진", "주영", "서준", "도윤", "희철", "서윤", "나연",
     "유정", "희연", "새봄", "우중", "한솔", "혜성"][np.random.randint(0, 25)]

    s1 = ["운동장", "마당", "모래밭", "주차장"][np.random.randint(0, 4)]
    s2 = ["나무 막대", "쇠막대", "우산", "지팡이", "야구 배트"][np.random.randint(0, 5)]

    j1 = proc_jo(s2, 1)

    while True:
        sa = np.random.randint(62, 95)
        if (sa != 70) and (sa != 80) and (sa != 90):
            break

    sbb = np.random.randint(13, 20)
    sb = round(sbb * 0.1, 1)
    sc = round(sa * sb, 1)

    if sc - (sc // 1) == 0:
        sc = round(sc)


    stem = stem.format(p=p, s1=s1, sa=sa, s2=s2, sb=sb, j1=j1)
    answer = answer.format(a1=sc)
    comment = comment.format(sa=sa, sb=sb, sc=sc, s2=s2)

    return stem, answer, comment




















































# 5-2-4-유형07-2
def decimalmul524_Stem_043():
    stem = "{p1}이의 몸무게는 $$수식$${sa} rm kg$$/수식$$이고, {p2}의 몸무게는 {p1}이의 몸무게의 $$수식$${sb}$$/수식$$배입니다. {p2}의 몸무게는 몇 $$수식$$rm kg$$/수식$$입니까?\n"
    answer = "(답): $$수식$${a1} rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${p2}의 몸무게$$수식$$RIGHT )$$/수식$$\n$$수식$$ = LEFT ($$/수식$${p1}이의 몸무게" \
              "$$수식$$RIGHT ) TIMES {sb}$$/수식$$\n$$수식$$ = {sa} TIMES {sb} = {sc} LEFT ( rm kg RIGHT )$$/수식$$\n\n"


    p1 = \
    ["하은", "진혁", "민준", "윤선", "은진", "주영", "서준", "도윤", "주원", "은혁", "선정", "예준", "혜영", "지영", "현준", "하윤", "은진", "주영", "서준",
     "도윤", "희철", "서윤", "나연", "유정", "희연", "새봄", "우중", "한솔", "혜성"][np.random.randint(0, 29)]

    p2 = ["아버지", "삼촌", "이모부", "고모부", "큰아버지", "작은아버지"][np.random.randint(0, 6)]

    sa = np.random.randint(31, 42)

    while True:
        sbb = np.random.randint(17, 27)
        sb = round(sbb * 0.1, 1)
        if sbb % 10 != 0:
            break

    sc = round(sa * sb, 1)

    if sc - (sc // 1) == 0:
        sc = round(sc)


    stem = stem.format(p1=p1, sa=sa, p2=p2, sb=sb)
    answer = answer.format(a1=sc)
    comment = comment.format(p1=p1, sa=sa, p2=p2, sb=sb, sc=sc)

    return stem, answer, comment




















































# 5-2-4-유형07-3
def decimalmul524_Stem_044():
    stem = "$$수식$${n1} rm L$$/수식$$의 페인트로 $$수식$${sa} rm m^{n2}$$/수식$$의 벽을 칠할 수 있다고 합니다. $$수식$${sb} rm L$$/수식$$의 페인트로 칠할 수 있는 벽의 넓이는 몇 $$수식$$rm m^{n2}$$/수식$$입니까?\n"
    answer = "(답): $$수식$${a1} rm m^{n2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( {sb} rm L$$/수식$$의 페인트로 칠할 수 있는 벽의 넓이" \
              "$$수식$$RIGHT )$$/수식$$\n$$수식$$ = {sa} TIMES {sb} = {sc} LEFT ( rm m^{n2}` RIGHT )$$/수식$$\n\n"


    while True:
        saa = np.random.randint(212, 499)
        sa = round(saa * 0.01, 2)

        if saa % 10 != 0:
            break

    sb = np.random.randint(4, 10)
    sc = round(sa * sb, 2)

    n1 = 1
    n2 = 2


    stem = stem.format(sa=sa, sb=sb, n1=n1, n2=n2)
    answer = answer.format(a1=sc, n2=n2)
    comment = comment.format(sa=sa, sb=sb, sc=sc, n2=n2)

    return stem, answer, comment





















































# 5-2-4-유형07-4
def decimalmul524_Stem_045():
    stem = "{p1}네 가족은 하루에 물을 $$수식$${sa} rm L$$/수식$$ 사용합니다. 수압 밸브를 약하게 조절하면 평소 사용량의 $$수식$${sb}$$/수식$$배만큼 아낄 수 있습니다. 수압 밸브를 약하게 조절했을 때 {p1}네 가족이 하루 동안 아끼는 물의 양은 몇 $$수식$$rm L$$/수식$$입니까?\n"
    answer = "(답): $$수식$${a1} rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$하루 동안 아낄 수 있는 물의 양$$수식$$ RIGHT )$$/수식$$\n$$수식$$ = {sa} TIMES {sb} = {sc} LEFT ( rm L RIGHT )$$/수식$$\n\n"


    p1 = ["은주", "주호", "영규", "보배", "준서", "지혜", "솔미", "홍기", "연우", "필교", "혜교", "빛나", "아라", "은수", "민우"][
        np.random.randint(0, 15)]

    sa = np.random.randint(14, 25)
    sa = sa * 10

    sb = np.random.randint(11, 20)
    sb = round(sb * 0.01, 2)

    sc = round(sa * sb, 2)

    if sc - (sc // 1) == 0:
        sc = round(sc)


    stem = stem.format(sa=sa, sb=sb, p1=p1)
    answer = answer.format(a1=sc)
    comment = comment.format(sa=sa, sb=sb, sc=sc, p1=p1)

    return stem, answer, comment



















































# 5-2-4-유형07-5
def decimalmul524_Stem_046():
    stem = "{s}{j1} {p1}이는 $$수식$${sa} rm L$$/수식$$의 $$수식$${sb}$$/수식$$만큼 마셨고, {p2}이는 $$수식$${sc} rm L$$/수식$$마셨습니다. {s}를 누가 몇 $$수식$$rm L$$/수식$$ 더 많이 마셨습니까?\n"
    answer = "(답): {a1}, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${p1}이가 마신 {s}의 양$$수식$$RIGHT ) = {sa} TIMES {sb} = {sd} LEFT ( rm L RIGHT )$$/수식$$\n" \
              "$$수식$${com}$$/수식$$이므로 {w1}이가 $$수식$${com2}$$/수식$$ 더 많이 마셨습니다.\n\n"


    while True:
        s = ["음료수", "물", "우유", "사과주스", "딸기주스", "포도주스", "키위주스"][np.random.randint(0, 7)]
        j1 = proc_jo(s, 1)

        while True:
            p1 = ["혜영", "지영", "현준", "하윤", "은진", "주영", "서준", "도윤", "희철", "서윤", "나연", "유정", "희연", "새봄", "우중", "한솔", "혜성"][
                np.random.randint(0, 17)]
            p2 = ["혜영", "지영", "현준", "하윤", "은진", "주영", "서준", "도윤", "희철", "서윤", "나연", "유정", "희연", "새봄", "우중", "한솔", "혜성"][
                np.random.randint(0, 17)]
            if p1 != p2:
                break

        while True:
            sa = np.random.randint(2, 6)
            sbb = np.random.randint(21, 50)
            sb = round(sbb * 0.01, 2)

            if (sa * sb > 1) and (sa * sb < 1.6):
                break

        while True:
            sc = np.random.randint(11, 16)
            sc = round(sc * 0.1, 1)
            if sc != sa * sb:
                break

        sd = round(sa * sb, 2)

        se = round(sd - sc, 2)  # p2
        sf = round(sc - sd, 2)  # p1

        a1 = ""
        a2 = ""
        com = ""
        w1 = ""
        com2 = ""

        if sf < 0:
            a1 = p1
            a2 = "%s rm L" % (se)
            com = "%s &gt; %s" % (sd, sc)
            w1 = p1
            com2 = "%s `-` %s `=` %s LEFT ( rm L RIGHT )" % (sd, sc, se)
            break

        elif sf > 0:
            a1 = p2
            a2 = "%s rm L" % (sf)
            com = "%s &gt; %s" % (sc, sd)
            w1 = p2
            com2 = "%s `-` %s `=` %s LEFT ( rm L RIGHT )" % (sc, sd, sf)
            break


    stem = stem.format(sa=sa, sb=sb, sc=sc, p1=p1, s=s, p2=p2, j1=j1)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(sa=sa, sb=sb, sd=sd, p1=p1, com=com, s=s, w1=w1, com2=com2)

    return stem, answer, comment





















































# 5-2-4-유형07-6
def decimalmul524_Stem_047():
    stem = "$$수식$$1$$/수식$$분에 $$수식$${sa} rm {{km}}$$/수식$$씩 일정하게 달리는 {s}가 있습니다. 이 {s}가 $$수식$${sb}$$/수식$$분 $$수식$${sc}$$/수식$$초 동안 달릴 수 있는 거리는 몇 $$수식$$rm {{km}}$$/수식$$입니까?\n"
    answer = "(답): $$수식$${a1} rm {{km}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sb}$$/수식$$분 $$수식$${sc}$$/수식$$초 $$수식$$= {sd}$$/수식$$분이므로\n" \
              "$$수식$$LEFT ($$/수식$${s}가 $$수식$${sb}$$/수식$$분 $$수식$${sc}$$/수식$$초 동안 " \
              "달릴 수 있는 거리$$수식$$RIGHT )$$/수식$$\n$$수식$$ = {sa} times {sd} = {se} LEFT ( rm {{km}} RIGHT )$$/수식$$입니다.\n\n"


    s = ["기차", "열차", "자동차"][np.random.randint(0, 3)]

    sa = np.random.randint(2, 5)
    sb = np.random.randint(5, 16)
    sc = [15, 30, 45][np.random.randint(0, 3)]
    sd = sb + sc / 60
    se = round(sa * sd, 2)

    if se - (se // 1) == 0:
        se = round(se)


    stem = stem.format(sa=sa, s=s, sb=sb, sc=sc, )
    answer = answer.format(a1=se)
    comment = comment.format(sb=sb, sc=sc, sd=sd, s=s, sa=sa, se=se)

    return stem, answer, comment





















































# 5-2-4-유형08-1
def decimalmul524_Stem_048():
    stem = "가 {s} 나$$수식$$=$$/수식$$가$$수식$$`times$$/수식$$나 라고 약속할 때, $$수식$$`{sa}`$$/수식$$ {s} $$수식$$`{sb}`$$/수식$${rur1} 계산하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "가 대신 $$수식$${sa}$$/수식$${rur2} 넣고 나 대신 $$수식$${sb}$$/수식$${rur1} 넣어 식을 세웁니다.\n" \
              "→ $$수식$$`{sa}`$$/수식$$ {s} $$수식$$`{sb}`=`{sa}`times`{sb}`=`{sc}`$$/수식$$\n\n"


    s = ["♦", "♠", "♥", "♣", "♢", "♡", "♤", "♧"][np.random.randint(0, 8)]

    while True:
        sa = np.random.randint(3, 10)
        sbb = np.random.randint(2, 10)
        sb = round(sbb * 0.1, 1)
        if sa * sb > 2:
            break

    sc = round(sa * sb, 1)

    if sc - (sc // 1) == 0:
        sc = round(sc)

    rur1 = josa(sb, "를")
    rur2 = josa(sa, "를")


    stem = stem.format(sa=sa, s=s, sb=sb, rur1=rur1)
    answer = answer.format(a1=sc)
    comment = comment.format(sa=sa, sb=sb, sc=sc, s=s, rur1=rur1, rur2=rur2)

    return stem, answer, comment

















































# 5-2-4-유형08-2
def decimalmul524_Stem_049():
    stem = "가 {s} 나 를 다음과 같이 약속할 때, $$수식$$`{sa}`$$/수식$$ {s} $$수식$$`{sb}`$$/수식$${rur1} 계산하시오.\n$$표$$ 가 {s} 나$$수식$$=$$/수식$$가$$수식$$`times`$$/수식$$나 $$/표$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "가 대신 $$수식$${sa}$$/수식$${rur2} 넣고 나 대신 $$수식$${sb}$$/수식$${rur1} 넣어 식을 세웁니다.\n" \
              "→ $$수식$$`{sa}`$$/수식$$ {s} $$수식$$`{sb}`=`{sa}`times`{sb}`=`{sc}`$$/수식$$\n\n"


    s = ["♦", "♠", "♥", "♣", "♢", "♡", "♤", "♧"][np.random.randint(0, 8)]

    while True:
        sa = np.random.randint(12, 50)
        sbb = np.random.randint(12, 50)
        sb = round(sbb * 0.01, 2)

        if (sa % 10 != 0) and (sa * sb < 12) and (sbb % 10 != 0):
            break

    sc = round(sa * sb, 2)

    rur1 = josa(sb, "를")
    rur2 = josa(sa, "를")


    stem = stem.format(sa=sa, s=s, sb=sb, rur1=rur1)
    answer = answer.format(a1=sc)
    comment = comment.format(sa=sa, sb=sb, sc=sc, s=s, rur1=rur1, rur2=rur2)

    return stem, answer, comment






















































# 5-2-4-유형08-3
def decimalmul524_Stem_050():
    stem = "가 {s} 나$$수식$$`=`$$/수식$$가$$수식$$`times`$$/수식$$나$$수식$$`+`{sa}`$$/수식$${rago1} 약속할 때, $$수식$$`{sb}`$$/수식$$ {s} $$수식$$`{sc}`$$/수식$${rur1} 계산하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "가 대신 $$수식$${sb}$$/수식$${rur2} 넣고 나 대신 $$수식$${sc}$$/수식$${rur1} 넣어 식을 세웁니다.\n" \
              "→ $$수식$$`{sb}`$$/수식$$ {s} $$수식$$`{sc}`=`{sb}`times`{sc}`+`{sa}`=`{sd}`+`{sa}`=`{se}`$$/수식$$\n\n"


    s = ["♦", "♠", "♥", "♣", "♢", "♡", "♤", "♧"][np.random.randint(0, 8)]

    sa = np.random.randint(2, 10)

    while True:
        sb = np.random.randint(2, 10)
        scc = np.random.randint(102, 290)
        sc = round(scc * 0.01, 2)

        if (sb * sc < 20) and (scc % 10 != 0):
            break

    sd = round(sb * sc, 2)
    se = round(sd + sa, 2)

    rur1 = josa(sc, "를")
    rur2 = josa(sb, "를")

    rago1 = josa(sa, "라고")


    stem = stem.format(sa=sa, s=s, sb=sb, sc=sc, rur1=rur1, rago1=rago1)
    answer = answer.format(a1=se)
    comment = comment.format(sa=sa, sb=sb, sc=sc, s=s, se=se, sd=sd, rur1=rur1, rur2=rur2)

    return stem, answer, comment





















































# 5-2-4-유형08-4
def decimalmul524_Stem_051():
    stem = "가 {s} 나 를 다음과 같이 약속할 때, $$수식$$`{sa}`$$/수식$$ {s} $$수식$$`{sb}`$$/수식$${rur1} 계산하시오.\n$$표$$ 가 {s} 나$$수식$$`=`{sc}`times`$$/수식$$가$$수식$$`+`{sd}`times`$$/수식$$나 $$/표$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "가 대신 $$수식$${sa}$$/수식$${rur2} 넣고 나 대신 $$수식$${sb}$$/수식$${rur1} 넣어 식을 세웁니다.\n" \
              "→ $$수식$$`{sa}`$$/수식$$ {s} $$수식$$`{sb}`=`{sc}`times`{sa}`+`{sd}`times`{sb}`=`{se}`+`{sf}`=`{sg}`$$/수식$$\n\n"


    s = ["♦", "♠", "♥", "♣", "♢", "♡", "♤", "♧"][np.random.randint(0, 8)]

    sa = np.random.randint(3, 10)
    sa = round(sa * 0.1, 1)

    while True:
        sbb = np.random.randint(51, 160)
        sb = round(sbb * 0.1, 1)
        if sbb % 10 != 0:
            break

    sc = np.random.randint(5, 10)
    sd = np.random.randint(2, 6)

    se = round(sc * sa, 1)
    if se - (se // 1) == 0:
        se = round(se)

    sf = round(sd * sb, 1)
    if sf - (sf // 1) == 0:
        sf = round(sf)

    sg = round(se + sf, 1)
    if sg - (sg // 1) == 0:
        sg = round(sg)

    rur1 = josa(sb, "를")
    rur2 = josa(sa, "를")


    stem = stem.format(sa=sa, s=s, sb=sb, sc=sc, sd=sd, rur1=rur1)
    answer = answer.format(a1=sg)
    comment = comment.format(sa=sa, sb=sb, sc=sc, s=s, sd=sd, se=se, sf=sf, sg=sg, rur1=rur1, rur2=rur2)

    return stem, answer, comment




















































# 5-2-4-유형08-5
def decimalmul524_Stem_052():
    stem = "가 {s} 나$$수식$$`=`$$/수식$$가$$수식$$`times`$$/수식$$나 라고 약속할 때, $$수식$$`{sa}`$$/수식$$ {s} $$수식$$`LEFT (`{sb}`$$/수식$$ {s} $$수식$$`{sc}`RIGHT )`$$/수식$${rur1} 계산하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "괄호 안을 먼저 계산합니다.\n" \
              "$$수식$$`{sb}`$$/수식$$ {s} $$수식$$`{sc}`=`{sb}`times`{sc}`=`{sd}$$/수식$$ " \
              "→ $$수식$$`{sa}`$$/수식$$ {s} $$수식$$`LEFT (`{sb}`$$/수식$$ {s} $$수식$$`{sc}`RIGHT )`=`{sa}`$$/수식$$ {s} $$수식$$`{sd}`=`{sa}`times`{sd}`=`{se}`$$/수식$$\n\n"


    s = ["♦", "♠", "♥", "♣", "♢", "♡", "♤", "♧"][np.random.randint(0, 8)]

    sa = np.random.randint(2, 10)
    sb = np.random.randint(2, 6)

    while True:
        sc = np.random.randint(2, 10)
        sc = round(sc * 0.1, 1)
        if sc * sb > 1:
            break

    sd = round(sc * sb, 1)
    if sd - (sd // 1) == 0:
        sd = round(sd)

    se = round(sa * sd, 1)
    if se - (se // 1) == 0:
        se = round(se)

    rur1 = josa(sc, "를")


    stem = stem.format(sa=sa, s=s, sb=sb, sc=sc, rur1=rur1)
    answer = answer.format(a1=se)
    comment = comment.format(sa=sa, sb=sb, sc=sc, s=s, sd=sd, se=se)

    return stem, answer, comment



















































# 5-2-4-유형08-6
def decimalmul524_Stem_053():
    stem = "가 {s} 나 를 다음과 같이 약속할 때, ㉠ {s} $$수식$$`{sa}`=`{sb}`$$/수식$${ga1} 되는 ㉠의 값을 구하시오.\n$$표$$ 가 {s} 나$$수식$$`=`$$/수식$$가$$수식$$`div`$$/수식$$나 $$/표$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "가 대신 ㉠을 넣고 나 대신 $$수식$${sa}$$/수식$${rur1} 넣어 식을 세웁니다.\n" \
              "㉠ {s} $$수식$$`{sa}`=`$$/수식$$㉠$$수식$$`div`{sa}`=`{sb}`$$/수식$$ → ㉠$$수식$$`=`{sb}`times`{sa}`=`{sc}`$$/수식$$\n\n"


    s = ["♦", "♠", "♥", "♣", "♢", "♡", "♤", "♧"][np.random.randint(0, 8)]

    while True:
        saa = np.random.randint(12, 36)
        sa = round(saa * 0.01, 2)
        if saa % 10 != 0:
            break

    sb = np.random.randint(6, 10)
    sc = round(sb * sa, 2)

    ga1 = josa(sb, "가")
    rur1 = josa(sa, "를")


    stem = stem.format(sa=sa, s=s, sb=sb, ga1=ga1)
    answer = answer.format(a1=sc)
    comment = comment.format(sa=sa, sb=sb, sc=sc, s=s, rur1=rur1)

    return stem, answer, comment



















































# 5-2-4-유형09-1
def decimalmul524_Stem_054():
    stem = "소수의 곱셈을 분수의 곱셈으로 계산하려고 합니다. ㉠, ㉡, ㉢, ㉣에 알맞은 수로 짝지어진 것을 고르시오.\n$$표$$$$수식$$`{sa}`TIMES`{sb}`=`{g1}`times`{g2}`=`{g3} over {n3}`=`LEFT ( {c4} RIGHT )`$$/수식$$$$/표$$\n① {a1}\n② {a2}\n③ {a3}\n④ {a4}\n⑤ {a5}\n"
    answer = "(답): {a}\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`TIMES`{sb}`=`{g4}`times`{g5}`=`{se}over{n3}`=`{sf}$$/수식$$입니다.\n\n"


    sa = 2 * (np.random.randint(1, 5))
    sa = round(sa * 0.1, 1)

    while True:
        sb = np.random.randint(11, 100)
        if sb % 5 == 0:
            if sb % 10 != 0:
                sb = round(sb * 0.01, 2)
                break

    sc = round(10 * sa)
    sd = round(100 * sb)
    se = round(sc * sd)
    sf = round(se / 1000, 3)

    aa = round(sa * 10)
    ab = round(sb * 100)
    ac = round(aa * ab)

    ad = round(ac / 1000, 3)
    ae = round(sa * 100)
    ah = round(sb * 1000, 1)

    if ah - (ah // 1) == 0:
        ah = round(ah)

    ai = round(ac / 10000, 5)
    af = round(ae * ab)
    ag = round(af / 1000, 3)

    if ag - (ag // 1) == 0:
        ag = round(ag)

    c1 = "㉠"
    c2 = "㉡"
    c3 = "㉢"
    c4 = "㉣"

    g1 = "{{LEFT ( %s RIGHT )} over 10}" % c1
    g2 = "{{LEFT ( %s RIGHT )} over 100}" % c2
    g3 = "{LEFT ( %s RIGHT )}" % c3

    g4 = "{%s over 10}" % sc
    g5 = "{%s over 100}" % sd

    y1 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % (c1, aa, c2, ab, c3, ac, c4, ad)
    y2 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % (c1, ae, c2, ab, c3, af, c4, ag)
    y3 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % (c1, aa, c2, ah, c3, af, c4, ag)
    y4 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % (c1, aa, c2, ab, c3, ac, c4, ag)
    y5 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % (c1, aa, c2, ab, c3, ac, c4, ai)

    candidates = [y1, y2, y3, y4, y5]
    ans = y1
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0

    for i, c in enumerate(candidates):
        if c == ans:
            correct_idx = i
            break

    n1 = 10
    n2 = 100
    n3 = 1000


    stem = stem.format(sa=sa, sb=sb, c1=c1, c2=c2, c3=c3, c4=c4, n1=n1, n2=n2, n3=n3, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5,
                       g1=g1, g2=g2, g3=g3)
    answer = answer.format(a=answer_dict[correct_idx])
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, n1=n1, n2=n2, n3=n3, g4=g4, g5=g5)

    return stem, answer, comment





















































# 5-2-4-유형09-2
def decimalmul524_Stem_055():
    stem = "자연수의 곱셈을 이용하여 $$수식$$`{sa}`TIMES`{sb}`$$/수식$${rur1} 계산하시오.\n$$표$$ $$수식$$`{sc}`times`{sd}`=`{se}`$$/수식$$ $$/표$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`$$/수식$${eun1} $$수식$$`{sc}`$$/수식$$의 $$수식$$`{n1}over{n2}`$$/수식$$배이고 $$수식$$`{sb}`$$/수식$${eun2} " \
              "$$수식$$`{sd}`$$/수식$$의 $$수식$$`{n1}over{n3}`$$/수식$$배이므로 $$수식$$`{sa}TIMES`{sb}`$$/수식$${eun2} $$수식$$`{se}`$$/수식$$의 " \
              "$$수식$$`{n1}over{n4}`$$/수식$$배인 $$수식$$`{sf}`$$/수식$${ga1} 됩니다.\n\n"


    while True:
        saa = np.random.randint(12, 96)
        sa = round(saa * 0.01, 2)
        sb = np.random.randint(2, 10)
        sb = round(sb * 0.1, 1)
        if (saa % 10 != 0) and (sa * sb > 0.06) and (sa * sb < 0.63):
            break

    sc = int(sa * 100)
    sd = int(sb * 10)
    se = sc * sd
    sf = round(se / 1000, 3)

    n1 = 1
    n2 = 100
    n3 = 10
    n4 = 1000

    rur1 = josa(sb, "를")
    eun1 = josa(sa, "은")
    eun2 = josa(sb, "은")
    ga1 = josa(sf, "가")


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, rur1=rur1)
    answer = answer.format(a1=sf)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, n1=n1, n2=n2, n3=n3, n4=n4, eun1=eun1, eun2=eun2,
                             ga1=ga1)

    return stem, answer, comment





















































# 5-2-4-유형09-3
def decimalmul524_Stem_056():
    stem = "빈칸에 알맞은 수를 구하시오.\n$$수식$$LEFT ( {sa} RIGHT )$$/수식$$ → $$수식$$LEFT ( {st} RIGHT )$$/수식$$ → $$수식$$LEFT ( {su} RIGHT )$$/수식$$\n"
    answer = "(답): $$수식$$`{a1}`$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sc}`TIMES`{sd}`=`{se}`$$/수식$$이고 $$수식$$`{sa}`$$/수식$${eun1} $$수식$$`{sc}`$$/수식$$의 " \
              "$$수식$$`{n1}over{n2}`$$/수식$$배, $$수식$$`{sb}`$$/수식$${eun2} $$수식$$`{sd}`$$/수식$$의 $$수식$$`{n1}over{n2}`$$/수식$$배이므로 " \
              "곱은 $$수식$$`{n1}over{n3}`$$/수식$$배인 $$수식$$`{sf}`$$/수식$$입니다.\n\n"


    while True:
        saa = np.random.randint(12, 96)
        sa = round(saa * 0.01, 2)
        sb = np.random.randint(2, 10)
        sb = round(sb * 0.01, 2)

        if (saa % 10 != 0) and ((sa * sb) > 0.006) and ((sa * sb) < 0.063):
            break

    sc = int(sa * 100)
    sd = int(sb * 100)
    se = sc * sd
    sf = round(se / 10000, 4)

    n1 = 1
    n2 = 100
    n3 = 10000

    st = "{Times %s}" % (sb)
    su = "```` ````"

    eun1 = josa(sa, "은")
    eun2 = josa(sb, "은")


    stem = stem.format(sa=sa, st=st, su=su)
    answer = answer.format(a1=sf)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, n1=n1, n2=n2, n3=n3, eun1=eun1, eun2=eun2)

    return stem, answer, comment



















































# 5-2-4-유형09-4
def decimalmul524_Stem_057():
    stem = "계산 결과를 비교하여 곱이 더 큰 것을 찾아 기호를 쓰시오.\n$$표$$ㄱ. $$수식$$`{sa}`TIMES`{sb}`$$/수식$$ ㄴ. $$수식$$`{sc}`TIMES`{sd}`$$/수식$$ $$/표$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "ㄱ. $$수식$$`{sa}`TIMES`{sb}`=`{se}`$$/수식$$, ㄴ. $$수식$$`{sc}`TIMES`{sd}`=`{sf}`$$/수식$$\n" \
              "따라서 곱이 가장 더 큰 것의 기호를 쓰면 {a1}입니다.\n\n"


    while True:
        saa = np.random.randint(31, 86)
        sa = round(saa * 0.01, 2)
        sb = np.random.randint(3, 9)
        sb = round(sb * 0.1, 1)
        sc = np.random.uniform(sa - 0.05, sa + 0.06)
        sc = float(format(sc, '.1f'))

        if (saa % 10 != 0) and (sa * sb > 0.1) and (sa * sb < 0.5) and (sc != sa) and (sc >= sa - 0.05) and (
                sc <= sa + 0.05):
            break

    while True:
        sd = np.random.uniform(sb - 0.1, sb + 0.1)
        sd = float(format(sd, '.2f'))

        if (sd != sb):
            break

    se = round(sa * sb, 3)
    sf = round(sc * sd, 3)

    maxnum = max(se, sf)
    correct_idx = 0

    if maxnum == se:
        correct_idx = 0

    elif maxnum == sf:
        correct_idx = 1


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, a1=answer_kodict[correct_idx])

    return stem, answer, comment
























































# 5-2-4-유형09-5
def decimalmul524_Stem_058():
    stem = "가장 큰 수와 가장 작은 수의 곱을 구하시오.\n$$수식$$`LEFT ( {sa} RIGHT )````````LEFT ( {sb} RIGHT )````````LEFT ( {sc} RIGHT )````````LEFT ( {sd} RIGHT )`$$/수식$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "가장 큰 수는 $$수식$$`{se}`$$/수식$$, 가장 작은 수는 $$수식$$`{sf}`$$/수식$$입니다.\n" \
              "→ $$수식$$`{se}`times`{sf}`=`{sg}`$$/수식$$\n\n"


    while True:
        saa = np.random.randint(2, 10)
        sa = round(saa / 10, 1)
        sbb = np.random.randint(2, 10)
        sb = round(sbb / 10, 1)
        scc = np.random.randint(2, 10)
        sc = round(scc / 10, 1)
        sdd = np.random.randint(2, 10)
        sd = round(sdd / 10, 1)

        if (sa != sb) and (sa != sc) and (sa != sd) and (sb != sc) and (sb != sd) and (sc != sd):
            break

    se = max(sa, sb, sc, sd)
    sf = min(sa, sb, sc, sd)
    sg = round(se * sf, 2)


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(a1=sg)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg)

    return stem, answer, comment























































# 5-2-4-유형09-6
def decimalmul524_Stem_059():
    stem = "㉠과 ㉡의 합을 구하시오.\n$$표$$ ㉠ $$수식$$`{sa}`times`{sb}`$$/수식$$ ㉡ $$수식$$`{sc}`times`{sd}`$$/수식$$ $$/표$$\n"
    answer = "(답): $$수식$$`{a1}`$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$$`{sa}`times`{sb}`=`{se}`$$/수식$$ ㉡ $$수식$$`{sc}`times`{sd}`=`{sf}`$$/수식$$\n" \
              "따라서 ㉠과 ㉡의 합은 $$수식$$`{se}`+`{sf}`=`{sg}`$$/수식$$입니다.\n\n"


    while True:
        saa = np.random.randint(2, 10)
        sa = round(saa * 0.1, 1)
        sbb = np.random.randint(12, 99)
        sb = round(sbb * 0.01, 2)
        scc = np.random.randint(12, 99)
        sc = round(scc * 0.01, 2)
        sdd = np.random.randint(2, 10)
        sd = round(sdd * 0.1, 1)

        if (sbb % 10 != 0) and (sa * sb > 0.1) and (sa * sb < 0.5) and (scc % 10 != 0) and (sb != sc) and (
                sa != sd) and (sd * sc > 0.1) and (sd * sc < 0.5):
            break

    se = round(sa * sb, 3)
    sf = round(sc * sd, 4)
    sg = round(se + sf, 3)

    if sg - (sg // 1) == 0:
        sg = round(sg)


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(a1=sg)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg)

    return stem, answer, comment


















































# 5-2-4-유형10-1
def decimalmul524_Stem_060():
    stem = "$$수식$${saa} `Times` {sbb}$$/수식$${rur1} 분수의 곱셈으로 계산하려고 합니다. 바르게 계산한 것을 고르시오.\n① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${saa}$$/수식$${gwa1} $$수식$${sbb}$$/수식$${eun1} 둘 다 소수 한 자리 수이므로 분모가 $$수식$$10$$/수식$$인 분수로 바꾸어야 합니다.\n" \
              "→ $$수식$${saa} `Times` {sbb} `=` {scc} over 10 `Times` {sdd} over 10 `=` {see} over 100 `=` {sff}$$/수식$$\n\n"


    while True:
        saade = np.random.randint(12, 99)
        saa = round(saade / 10, 1)
        sbbde = np.random.randint(12, 99)
        sbb = round(sbbde / 10, 1)

        if (saade % 10 != 0) and (sbbde % 10 != 0) and (saa * sbb > 5) and (saa * sbb < 20) and (saa != sbb):
            break

    scc = saade
    sdd = sbbde
    see = scc * sdd

    sff = round(see / 100, 2)
    if sff - (sff // 1) == 0:
        sff = round(sff)

    sgg = round(see / 1000, 3)
    if sgg - (sgg // 1) == 0:
        sgg = round(sgg)

    shh = round(see / 10000, 4)
    if shh - (shh // 1) == 0:
        shh = round(shh)

    sii = round(see / 100000, 5)
    if sii - (sii // 1) == 0:
        sii = round(sii)

    y1 = "%s `Times` %s `=` %s over 10 `Times` %s over 10 `=` %s over 100 `=` %s" % (saa, sbb, scc, sdd, see, sff)
    y2 = "%s `Times` %s `=` %s over 10 `Times` %s over 100 `=` %s over 1000 `=` %s" % (saa, sbb, scc, sdd, see, sgg)
    y3 = "%s `Times` %s `=` %s over 100 `Times` %s over 10 `=` %s over 1000 `=` %s" % (saa, sbb, scc, sdd, see, sgg)
    y4 = "%s `Times` %s `=` %s over 100 `Times` %s over 100 `=` %s over 10000 `=` %s" % (saa, sbb, scc, sdd, see, shh)
    y5 = "%s `Times` %s `=` %s over 100 `Times` %s over 100 `=` %s over 10000 `=` %s" % (saa, sbb, scc, sdd, see, sii)

    candidates = [y1, y2, y3, y4, y5]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4, x5] = candidates

    correct_idx = 0

    for idx, sdx in enumerate(candidates):
        if sdx == y1:
            correct_idx = idx
            break

    rur1 = josa(sbb, "를")
    gwa1 = josa(saa, "과")
    eun1 = josa(sbb, "은")


    stem = stem.format(saa=saa, sbb=sbb, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, rur1=rur1)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, gwa1=gwa1, eun1=eun1)

    return stem, answer, comment





















































# 5-2-4-유형10-2
def decimalmul524_Stem_061():
    stem = "계산해 보시오.\n$$수식$${saa} `Times` {sbb}$$/수식$$\n"
    answer = "(답): $$수식$${sff}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${scc} `Times` {sdd} `=` {see}$$/수식$$이고, $$수식$${saa}$$/수식$${eun1} $$수식$${scc}$$/수식$$의 " \
              "$$수식$$1 over 100$$/수식$$배, $$수식$${sbb}$$/수식$${eun2} $$수식$${sdd}$$/수식$$의 $$수식$$1 over 10$$/수식$$배이므로 " \
              "곱은 $$수식$${see}$$/수식$$의 $$수식$$1 over 1000$$/수식$$배인 $$수식$${sff}$$/수식$$입니다.\n\n"


    while True:
        saade = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95][np.random.randint(0, 10)]
        saa1 = np.random.randint(1, 10)
        saa = round(saa1 + saade / 100, 2)
        sbbde = [2, 4, 6, 8][np.random.randint(0, 4)]
        sbb1 = np.random.randint(1, 10)
        sbb = round(sbb1 + sbbde / 10, 1)

        if (saa >= 1.05) and (saa <= 9.15) and (5 < saa * sbb) and (saa * sbb < 20) and (1.2 <= sbb) and (sbb <= 9.8):
            break

    scc = round(saa * 100)
    sdd = round(sbb * 10)
    see = scc * sdd
    sff = round(see / 1000, 3)

    eun1 = josa(saa, "는")
    eun2 = josa(sbb, "는")


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(sff=sff)
    comment = comment.format(scc=scc, sdd=sdd, see=see, saa=saa, sbb=sbb, sff=sff, eun1=eun1, eun2=eun2)

    return stem, answer, comment


















































# 5-2-4-유형10-3
def decimalmul524_Stem_062():
    stem = "빈 칸에 알맞은 수를 구하시오.\n$$수식$$LEFT ( {b1} RIGHT )$$/수식$$ → $$수식$$LEFT ( {b2} RIGHT )$$/수식$$ → $$수식$$LEFT ( {b3} RIGHT )$$/수식$$ → $$수식$$LEFT ( {b4} RIGHT )$$/수식$$\n"
    answer = "(답): $$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} `Times` {sbb} `=` {sdd}$$/수식$$ → $$수식$${sdd} `Times` {scc} `=` {see}$$/수식$$\n\n"


    while True:
        saade = [2, 4, 6, 8][np.random.randint(0, 4)]
        saa1 = np.random.randint(1, 6)
        saa = round(saa1 + (saade / 10), 1)
        sbb = [1.5, 2.5, 3.5, 4.5, 5.5][np.random.randint(0, 5)]
        if (1.2 <= saa) and (saa <= 5.4) and ((saa * sbb) < 10):
            break

    while True:
        sccde = np.random.randint(1, 10)
        scc1 = np.random.randint(1, 5)
        scc = round(scc1 + (sccde / 100), 2)
        if (1.02 <= scc) and (scc <= 5.05):
            break

    sdd = round(saa * sbb, 3)
    if sdd - (sdd // 1) == 0:
        sdd = round(sdd)
    see = round(sdd * scc, 5)

    b1 = saa
    b2 = "{Times {%s}}" % (sbb)
    b3 = "{Times {%s}}" % (scc)
    b4 = "```` ````"


    stem = stem.format(b1=b1, b2=b2, b3=b3, b4=b4)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, sdd=sdd, scc=scc, see=see)

    return stem, answer, comment

















































# 5-2-4-유형10-4
def decimalmul524_Stem_063():
    stem = "$$수식$${sa}{sb}{sc} `Times` {sd}{se}$$/수식$${eun1} $$수식$${saa}$$/수식$$입니다. $$수식$${sa}.{sb}{sc} `Times` {sd}.{se}$$/수식$$의 값을 어림하여 결과 값에 소수점을 알맞게 찍은 것을 고르시오.\n① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${sa}.{sb}{sc} `Times` {sd}.{se}$$/수식$${rur1} $$수식$${sf}.{sg}$$/수식$$의 $$수식$${sh}$$/수식$$배 정도로 " \
              "어림하면 $$수식$${sff}$$/수식$$ 정도가 됩니다.\n" \
              "→ $$수식$${sa}.{sb}{se} `Times` {sd}.{se} `=` {scc}$$/수식$$\n\n"


    sa = np.random.randint(1, 6)
    sb = np.random.randint(0, 9)

    while True:
        sc = np.random.randint(1, 10)

        if sc != 5:
            break

    sd = np.random.randint(1, 6)
    se = np.random.randint(1, 10)
    sf = sa

    if (1 <= sc) and (sc <= 4):
        sg = sb

    elif (6 <= sc) and (sc <= 9):
        sg = sb + 1

    if (1 <= se) and (se <= 4):
        sh = sd

    elif (5 <= se) and (se <= 9):
        sh = sd + 1

    saa = (sa * 100 + sb * 10 + sc) * (sd * 10 + se)
    sbb = round(saa / 10000, 4)
    scc = round(saa / 1000, 3)
    sdd = round(saa / 100, 2)
    see = round(saa / 10, 1)
    sff = round((sf + (sg / 10)) * sh, 1)

    y1 = sbb
    y2 = scc
    y3 = sdd
    y4 = see
    y5 = round(saa * 1.0, 1)

    candidates = [y1, y2, y3, y4, y5]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4, x5] = candidates

    correct_idx = 0

    for idx, sdx in enumerate(candidates):
        if sdx == y2:
            correct_idx = idx
            break

    eun1 = josa(se, "은")
    rur1 = josa(se, "를")


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, saa=saa, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, eun1=eun1)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sh=sh, sff=sff, scc=scc, rur1=rur1)

    return stem, answer, comment





















































# 5-2-4-유형10-5
def decimalmul524_Stem_064():
    stem = "계산 결과를 비교하여 곱이 더 큰 것을 찾아 기호를 쓰시오.\n$$표$$ㄱ. $$수식$${saa} `Times` {sbb}$$/수식$$      ㄴ. $$수식$${scc} `Times` {sdd}$$/수식$$$$/표$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "ㄱ. $$수식$${saa} `Times` {sbb} `=` {see}$$/수식$$, ㄴ. $$수식$${scc} `Times` {sdd} `=` {sff}$$/수식$$\n" \
              "따라서 곱이 더 큰 것의 기호를 쓰면 {a1}입니다.\n\n"

    while True:
        while True:
            saade = np.random.randint(11, 44)
            saa = round(saade / 10, 1)

            sbbde = np.random.randint(11, 44)
            sbb = round(sbbde / 10, 1)

            sccde = np.random.randint(1, 60)
            scc = round(sccde / 10, 1)

            sddde = np.random.randint(1, 100)
            sdd = round(sddde / 10, 1)

            if (saade % 10 != 0) and (sbbde % 10 != 0) and (sccde % 10 != 0) and (sddde % 10 != 0) and (
                    2 < saa * sbb) and (
                    saa * sbb < 6) and (sbb != saa) and ((saa - 0.5) <= scc) and (scc <= (saa + 0.5)) and (
                    scc != saa) and (
                    scc != sbb) and (((saa * sbb - 0.5) / scc) < sdd) and (((saa * sbb + 0.5) / scc) > sdd) and (
                    sdd != saa) and (sdd != sbb) and (sdd != scc):
                break

        see = round(saa * sbb, 2)
        sff = round(scc * sdd, 2)

        if see > sff:
            a1 = "ㄱ"
            break

        elif see < sff:
            a1 = "ㄴ"
            break


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(a1=a1)
    comment = comment.format(saa=saa, sbb=sbb, see=see, scc=scc, sdd=sdd, sff=sff, a1=a1)

    return stem, answer, comment




















































# 5-2-4-유형10-6
def decimalmul524_Stem_065():
    stem = "㉠과 ㉡의 차를 구하시오.\n$$표$$㉠ $$수식$${saa} `Times` {sbb}$$/수식$$      ㉡ $$수식$${scc} `Times` {sdd}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${sii}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${saa} `Times` {sbb} `=` {see}$$/수식$$, ㉡ $$수식$${scc} `Times` {sdd} `=` {sff}$$/수식$$\n" \
              "따라서 ㉠과 ㉡의 차는 $$수식$${sgg} `-` {shh} `=` {sii}$$/수식$$입니다.\n\n"


    while True:
        saade = np.random.randint(51, 99)
        saa = round(saade / 10, 1)

        sbbde = np.random.randint(2, 10)
        sbb = round(sbbde / 10, 1)

        sccde = np.random.randint(12, 50)
        scc = round(sccde / 10, 1)

        sddde = np.random.randint(11, 100)
        sdd = round(sddde / 10, 1)

        if (saade % 10 != 0) and (3 < saa * sbb) and (sccde % 10 != 0) and (sddde % 10 != 0) and (
                ((saa * sbb - 0.3) / scc) < sdd) and (((saa * sbb + 0.3) / scc) > sdd) and (sdd != ((saa * sbb) / scc)):
            break

    see = round(saa * sbb, 2)
    sff = round(scc * sdd, 2)

    if ((saa * sbb) - (scc * sdd)) >= 0:
        sgg = round(saa * sbb, 2)
        shh = round(scc * sdd, 2)

    elif ((saa * sbb) - (scc * sdd)) < 0:
        shh = round(saa * sbb, 2)
        sgg = round(scc * sdd, 2)

    sii = round(sgg - shh, 2)


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(sii=sii)
    comment = comment.format(saa=saa, sbb=sbb, see=see, scc=scc, sdd=sdd, sff=sff, sgg=sgg, shh=shh, sii=sii)

    return stem, answer, comment



















































# 5-2-4-유형10-7
def decimalmul524_Stem_066():
    stem = "㉠에 알맞은 자연수는 모두 몇 개인가요?\n$$표$$ $$수식$$`{sa}.{sb}`times`{sc}.{sd}`&lt;`$$/수식$$㉠$$수식$$`&lt;`{se}{sf}.{sg}`times`0.{sh}`$$/수식$$ $$/표$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}.{sb}`times`{sc}.{sd}`=`{a}`$$/수식$$, $$수식$$`{se}{sf}.{sg}`times`0.{sh}`=`{b}`$$/수식$$\n" \
              "따라서 $$수식$$`{a}`&lt;`㉠`&lt;`{b}$$/수식$$이므로 ㉠에 알맞은 자연수는 $$수식$${c}$$/수식$${ro1} $$수식$${d}$$/수식$$개입니다.\n\n"


    while True:
        sa = np.random.randint(2, 10)
        sc = 11 - sa
        sb = np.random.randint(1, 8)
        sd = np.random.randint(1, 8)
        sg = np.random.randint(1, 8)
        sf = np.random.randint(0, 6)
        se = np.random.randint(1 + ((sa * sc) / 10), 4 + ((sa * sc) / 10))

        a = (sa + 0.1 * sb) * (sc + 0.1 * sd)
        e = math.ceil(a)

        sh = np.random.randint(7, 10)
        b = (10 * se + sf + 0.1 * sg) * (0.1 * sh)
        if e < b:
            break

    f = math.floor(b)
    a = round(a, 2)
    b = round(b, 2)

    clist = []

    for i in range(e, f + 1):
        clist.append(str(i))

    c = ',````'.join(clist)
    d = f - e + 1

    ro1 = josa(c, "로")


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sh=sh)
    answer = answer.format(a1=d)
    comment = comment.format(a=a, b=b, c=c, d=d, sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sh=sh, ro1=ro1)

    return stem, answer, comment





















































# 5-2-4-유형10-8
def decimalmul524_Stem_067():
    stem = "□ 안에 들어갈 수 있는 가장 작은 자연수를 구하시오.\n$$표$$ $$수식$$`{sa}.{sb}{sc}`times`{sd}.{se}{sf}`&lt;`$$/수식$$□ $$/표$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}.{sb}{sc}`times`{sd}.{se}{sf}`=`{a}`$$/수식$$\n" \
              "따라서 $$수식$$`{a}`&lt;`$$/수식$$□이므로 □ 안에 들어갈 수 가장 작은 자연수는 $$수식$${b}$$/수식$$입니다.\n\n"


    sa = np.random.randint(2, 7)
    sb = np.random.randint(0, 6)
    sd = np.random.randint(2, 7)
    se = np.random.randint(0, 6)

    sc = 5
    sf = np.random.randint(1, 5) * 2
    a = round((sa + 0.1 * sb + 0.01 * sc) * (sd + 0.1 * se + 0.01 * sf), 3)
    b = math.ceil(a)


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf)
    answer = answer.format(a1=b)
    comment = comment.format(a=a, b=b, sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf)

    return stem, answer, comment




















































# 5-2-4-유형11-1
def decimalmul524_Stem_068():
    stem = "{s1} $$수식$$1 rm L$$/수식$$에는 $$수식$${saa} rm g$$/수식$$의 {s2}이 녹아 있습니다. 이 {s1} $$수식$${sbb} rm L$$/수식$$에 녹아 있는 {s2}은 몇 $$수식$$rm g$$/수식$$입니까?\n"
    answer = "(답): $$수식$${scc} rm g$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${s1} $$수식$${sbb} rm L$$/수식$$에 녹아 있는 {s2}의 양$$수식$$RIGHT )$$/수식$$\n$$수식$$ `=` {saa} `Times` {sbb} `=` {scc} LEFT ( rm g RIGHT )$$/수식$$\n\n"


    [s1, s2] = [["소금물", "소금"], ["설탕물", "설탕"], ["꿀물", "꿀"]][np.random.randint(0, 3)]

    while True:
        sa = np.random.randint(31, 90)
        saa = round(sa / 100, 2)
        sb = np.random.randint(2, 10)
        sbb = round(sb / 10, 1)
        if (sa % 10 != 0) and (0.1 < (saa * sbb)):
            break

    scc = round(saa * sbb, 3)


    stem = stem.format(s1=s1, saa=saa, s2=s2, sbb=sbb)
    answer = answer.format(scc=scc)
    comment = comment.format(s1=s1, sbb=sbb, s2=s2, saa=saa, scc=scc)

    return stem, answer, comment



















































# 5-2-4-유형11-2
def decimalmul524_Stem_069():
    stem = "어떤 자동차는 $$수식$$1 rm {{km}}$$/수식$$를 달리는 데 $$수식$${saa} rm L$$/수식$$의 {sss}가 필요합니다. 이 자동차가 $$수식$${sbb} rm {{km}}$$/수식$$를 달리려면 {sss}가 몇 $$수식$$rm L$$/수식$$ 필요합니까?\n"
    answer = "(답): $$수식$${scc} rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( {sbb} rm {{km}}$$/수식$$를 달리는 데 필요한 {sss}$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ( 1 rm {{km}}$$/수식$$를 달리는 데 필요한 {sss}$$수식$$RIGHT ) `Times` LEFT ($$/수식$$달리는 거리$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {saa} `Times` {sbb} `=` {scc} LEFT ( rm L RIGHT )$$/수식$$\n\n"


    sss = ["휘발유", "경유", "연료"][np.random.randint(0, 3)]

    sa = np.random.randint(5, 10)
    saa = round(sa / 100, 2)
    sb = np.random.randint(3, 10)
    sbb = round(sb / 10, 1)
    scc = round(saa * sbb, 3)


    stem = stem.format(saa=saa, sss=sss, sbb=sbb)
    answer = answer.format(scc=scc)
    comment = comment.format(sbb=sbb, sss=sss, saa=saa, scc=scc)

    return stem, answer, comment








































# 5-2-4-유형11-3
def decimalmul524_Stem_070():
    stem = "{spp}가 키우는 {sss}는 $$수식$${saa}$$/수식$$월에 몸무게가 $$수식$${sbb} rm kg$$/수식$$이었습니다. $$수식$${scc}$$/수식$$월에는 $$수식$${saa}$$/수식$$월보다 몸무게가 $$수식$${sdd}$$/수식$$배만큼 늘어났습니다. {spp}가 키우는 {sss}의 $$수식$${scc}$$/수식$$월 몸무게는 몇 $$수식$$rm kg$$/수식$$입니까?\n"
    answer = "(답): $$수식$${sff} rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${scc}$$/수식$$월 몸무게는 $$수식$${saa}$$/수식$$월보다 $$수식$${sdd}$$/수식$$배만큼 " \
              "늘어났으므로 $$수식$${saa}$$/수식$$월의 몸무게에 $$수식$${see}$$/수식$${rur1} 곱합니다.\n" \
              "→ $$수식$$LEFT ( {scc}$$/수식$$월 몸무게$$수식$$RIGHT ) `=` {sbb} `Times` {see} `=` {sff} LEFT ( rm kg RIGHT )$$/수식$$\n\n"


    spp = \
    ["예나", "은수", "지호", "현규", "지우", "은주", "주호", "영규", "보배", "준서", "지혜", "솔미", "홍기", "연우", "필교", "혜교", "빛나", "아라", "은수",
     "민우"][np.random.randint(0, 20)]

    sss = ["강아지", "고양이"][np.random.randint(0, 2)]

    while True:
        saa = np.random.randint(1, 8)
        sb = np.random.randint(31, 60)
        sbb = round(sb / 10, 1)
        scc = np.random.randint(1, 13)

        if (sb % 10 != 0) and ((saa + 2) <= scc):
            break

    sdd = [0.1, 0.2, 0.3][np.random.randint(0, 3)]

    see = round(sdd + 1, 1)
    sff = round(sbb * see, 2)

    if sff - (sff // 1) == 0:
        sff = round(sff)

    rur1 = josa(see, "를")


    stem = stem.format(spp=spp, sss=sss, saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(sff=sff)
    comment = comment.format(scc=scc, saa=saa, sdd=sdd, see=see, sbb=sbb, sff=sff, rur1=rur1)

    return stem, answer, comment



















































# 5-2-4-유형11-4
def decimalmul524_Stem_071():
    stem = "{spp}네 {s1}의 {s2}{j1} 가로가 $$수식$${saa} rm m$$/수식$$, 세로가 $$수식$${sbb} rm m$$/수식$$인 직사각형 모양입니다. 이 {s2}의 가로와 세로를 각각 $$수식$${scc}$$/수식$$배로 늘려 새로운 {s2}{j2} 만들려고 합니다. 새로운 {s2}의 넓이는 몇 $$수식$$rm m^{qq}$$/수식$$입니까?\n"
    answer = "(답): $$수식$${sff} rm m^{qq}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$새로운 {s2}의 가로$$수식$$RIGHT ) `=` {saa} `Times` {scc} `=` {sdd} LEFT ( rm m RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$새로운 {s2}의 세로$$수식$$RIGHT ) `=` {sbb} `Times` {scc} `=` {see} LEFT ( rm m RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$새로운 {s2}의 넓이$$수식$$RIGHT ) `=` {sdd} `Times` {see} `=` {sff} LEFT ( rm m^{qq} RIGHT )$$/수식$$\n\n"


    spp = ["은주", "주호", "영규", "보배"][np.random.randint(0, 4)]
    s1 = ["학교", "아파트 단지", "마을"][np.random.randint(0, 3)]
    s2 = ["놀이터", "공원", "쉼터"][np.random.randint(0, 3)]

    j1 = proc_jo(s2, -1)
    j2 = proc_jo(s2, 1)


    while True:
        saade = [2, 4, 6, 8][np.random.randint(0, 4)]
        saa1 = np.random.randint(11, 15)
        saa = round(saa1 + (saade / 10), 1)
        sbbde = [2, 4, 6, 8][np.random.randint(0, 4)]
        sbb1 = np.random.randint(6, 10)
        sbb = round(sbb1 + (sbbde / 10), 1)
        if (11.2 <= saa) and (saa <= 14.8) and (6.6 <= sbb) and (sbb <= 9.8):
            break

    scc = [1.5, 2.5][np.random.randint(0, 2)]
    sdd = round(saa * scc, 2)
    if sdd - (sdd // 1) == 0:
        sdd = round(sdd)

    see = round(sbb * scc, 2)
    if see - (see // 1) == 0:
        see = round(see)

    sff = round(sdd * see, 4)
    if sff - (sff // 1) == 0:
        sff = round(sff)

    qq = 2


    stem = stem.format(spp=spp, s1=s1, s2=s2, j1=j1, saa=saa, sbb=sbb, scc=scc, j2=j2, qq=qq)
    answer = answer.format(sff=sff, qq=qq)
    comment = comment.format(s2=s2, saa=saa, scc=scc, sdd=sdd, sbb=sbb, see=see, sff=sff, qq=qq)

    return stem, answer, comment






















































# 5-2-4-유형11-5
def decimalmul524_Stem_072():
    stem = "한 변의 길이가 $$수식$${saa} rm m$$/수식$$인 정사각형과 {s1}가 $$수식$${sbb} rm m$$/수식$$, {s2}가 $$수식$${scc} rm m$$/수식$$인 {s3}이 있습니다. 두 도형 중 어느 도형의 넓이가 더 넓습니까?\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$정사각형의 넓이$$수식$$RIGHT ) `=` {saa} `Times` {saa} `=` {sdd} LEFT ( rm m^{qq} RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${s3}의 넓이$$수식$$RIGHT ) `=` {sbb} `Times` {scc} `=` {see} LEFT ( rm m^{qq} RIGHT )$$/수식$$\n" \
              "따라서 {a1}의 넓이가 더 넓습니다.\n\n"


    [s1, s2, s3] = [["밑변의 길이", "높이", "평행사변형"], ["가로", "세로", "직사각형"]][np.random.randint(0, 2)]


    while True:
        while True:
            sa = np.random.randint(4, 9)
            saa = round(sa / 10, 1)
            sb = np.random.randint(1, 100)
            sbb = round(sb / 100, 2)
            sc = np.random.randint(1, 100)
            scc = round(sc / 100, 2)

            if (sb % 10 != 0) and ((saa - 0.1) < sbb) and (sbb < (saa + 0.1)) and (sc % 10 != 0):
                if saa > sbb:
                    if (((saa * saa) / sbb) < scc) and (((saa * saa + 0.05) / sbb) > scc):
                        break
                elif saa < sbb:
                    if (((saa * saa - 0.05) / sbb) < scc) and (((saa * saa) / sbb) > scc):
                        break

        sdd = round(saa * saa, 2)
        see = round(sbb * scc, 4)
        qq = 2

        if sdd > see:
            a1 = "정사각형"
            break

        elif sdd < see:
            a1 = s3
            break

        else:
            continue


    stem = stem.format(saa=saa, s1=s1, sbb=sbb, s2=s2, scc=scc, s3=s3)
    answer = answer.format(a1=a1)
    comment = comment.format(saa=saa, sdd=sdd, qq=qq, sbb=sbb, scc=scc, see=see, a1=a1, s3=s3)

    return stem, answer, comment






















































# 5-2-4-유형11-6
def decimalmul524_Stem_073():
    stem = "길이가 $$수식$${saa} rm m$$/수식$$인 양초가 있습니다. 이 양초는 한 시간에 $$수식$${sbb} rm m$$/수식$$씩 일정한 빠르기로 탄다고 합니다. 양초에 $$수식$${scc}$$/수식$$분 동안 불을 붙여 태웠다면 타고 남은 양초의 길이는 몇 $$수식$$rm m$$/수식$$입니까?\n"
    answer = "(답): $$수식$${sgg} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${scc}$$/수식$$분$$수식$$= {scc} over 60$$/수식$$시간$$수식$$= {sdd} over 10 = {see}$$/수식$$시간이므로\n" \
              "$$수식$$LEFT ( {scc}$$/수식$$분 동안 탄 길이$$수식$$RIGHT )$$/수식$$\n$$수식$$ `=` LEFT ($$/수식$$한 시간 동안 타는 길이$$수식$$RIGHT ) `Times` LEFT ($$/수식$$" \
              "탄 시간$$수식$$RIGHT )$$/수식$$\n$$수식$$ `=` {sbb} `Times` {see} `=` {sff} LEFT ( rm m RIGHT )$$/수식$$\n" \
              "→ $$수식$$LEFT ($$/수식$$타고 남은 양초의 길이$$수식$$RIGHT )$$/수식$$\n$$수식$$ `=` {saa} `-` {sff} `=` {sgg} LEFT ( rm m RIGHT )$$/수식$$\n\n"


    while True:
        saade = np.random.randint(15, 26)
        saa = round(saade / 100, 2)
        if (saade % 10 != 0):
            break

    sbbde = np.random.randint(3, 10)
    sbb = round(sbbde / 100, 2)

    while True:
        scc = np.random.randint(2, 60)
        if scc % 6 == 0:
            break

    sdd = round(scc / 6)
    see = round(sdd / 10, 1)
    sff = round(sbb * see, 3)
    sgg = round(saa - sff, 3)


    stem = stem.format(saa=saa, sbb=sbb, scc=scc)
    answer = answer.format(sgg=sgg)
    comment = comment.format(scc=scc, sdd=sdd, see=see, sbb=sbb, sff=sff, saa=saa, sgg=sgg)

    return stem, answer, comment
























































# 5-2-4-유형12-1
def decimalmul524_Stem_074():
    stem = "수 카드 $$수식$$LEFT ( {sa} RIGHT )$$/수식$$, $$수식$$LEFT ( {sb} RIGHT )$$/수식$$, $$수식$$LEFT ( {sc} RIGHT )$$/수식$$, $$수식$$LEFT ( {sd} RIGHT )$$/수식$${rur1} □ 안에 한 번씩 모두 넣어 곱이 가장 큰 곱셈식을 만들었을 때의 곱을 구하시오.\n$$표$$□.□$$수식$$Times$$/수식$$□.□$$/표$$"
    answer = "(답): $$수식$${scc}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠.㉡$$수식$$Times$$/수식$$㉢.㉣에서 곱이 가장 큰 곱셈식을 만들려면 ㉠과 ㉢에 큰 수인 $$수식$${se}$$/수식$$, $$수식$${sf}$$/수식$${rur2} 넣습니다.\n" \
              "→ $$수식$${se}.{sg} `Times` {sf}.{sh} `=` {saa}$$/수식$$, $$수식$${se}.{sh} `Times` {sf}.{sg} `=` {sbb}$$/수식$$\n" \
              "따라서 곱이 가장 큰 곱셈식의 곱은 $$수식$${scc}$$/수식$$입니다.\n\n"


    sa, sb, sc, sd = random.sample(list(range(1, 10)), 4)

    # while True:
    #     sa = np.random.randint(1, 10)
    #     sb = np.random.randint(1, 10)
    #     sc = np.random.randint(1, 10)
    #     sd = np.random.randint(1, 10)
    #     if (sa != sb) and (sa != sc) and (sa != sd) and (sb != sc) and (sb != sd) and (sc != sd):
    #         break

    temp_list = [sa, sb, sc, sd]
    temp_list.sort(reverse=True)
    # temp_list.reverse()
    [se, sf, sg, sh] = temp_list

    saa = round((se + (sg / 10)) * (sf + (sh / 10)), 2)
    sbb = round((se + (sh / 10)) * (sf + (sg / 10)), 2)
    scc = max([saa, sbb])

    rur1 = josa(sd, "를")
    rur2 = josa(sf, "를")


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, rur1=rur1)
    answer = answer.format(scc=scc)
    comment = comment.format(se=se, sf=sf, sg=sg, sh=sh, saa=saa, sbb=sbb, scc=scc, rur2=rur2)

    return stem, answer, comment

























































# 5-2-4-유형12-2
def decimalmul524_Stem_075():
    stem = "수 카드 $$수식$$LEFT ( {sa} RIGHT )$$/수식$$, $$수식$$LEFT ( {sb} RIGHT )$$/수식$$, $$수식$$LEFT ( {sc} RIGHT )$$/수식$$, $$수식$$LEFT ( {sd} RIGHT )$$/수식$${rur1} □ 안에 한 번씩 모두 넣어 곱이 가장 작은 곱셈식을 만들었을 때의 곱을 구하시오.\n$$표$$□.□$$수식$$Times$$/수식$$□.□$$/표$$\n"
    answer = "(답): $$수식$${scc}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠.㉡$$수식$$Times$$/수식$$㉢.㉣에서 곱이 가장 작은 곱셈식을 만들려면 ㉠과 ㉢에 작은 수인 $$수식$${se}$$/수식$$, $$수식$${sf}$$/수식$${rur2} 넣습니다.\n" \
              "→ $$수식$${se}.{sg} `Times` {sf}.{sh} `=` {saa}$$/수식$$, $$수식$${se}.{sh} `Times` {sf}.{sg} `=` {sbb}$$/수식$$\n" \
              "따라서 곱이 가장 작은 곱셈식의 곱은 $$수식$${scc}$$/수식$$입니다.\n\n"


    sa, sb, sc, sd = random.sample(list(range(1, 10)), 4)

    # while True:
    #     sa = np.random.randint(1, 10)
    #     sb = np.random.randint(1, 10)
    #     sc = np.random.randint(1, 10)
    #     sd = np.random.randint(1, 10)
    #
    #     if (sa != sb) and (sa != sc) and (sa != sd) and (sb != sc) and (sb != sd) and (sc != sd):
    #         break

    temp_list = [sa, sb, sc, sd]
    temp_list.sort()
    [se, sf, sg, sh] = temp_list

    saa = round((se + (sg / 10)) * (sf + (sh / 10)), 2)
    sbb = round((se + (sh / 10)) * (sf + (sg / 10)), 2)
    scc = min([saa, sbb])

    rur1 = josa(sd, "를")
    rur2 = josa(sf, "를")

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, rur1=rur1)
    answer = answer.format(scc=scc)
    comment = comment.format(se=se, sf=sf, sg=sg, sh=sh, saa=saa, sbb=sbb, scc=scc, rur2=rur2)

    return stem, answer, comment

























































# 5-2-4-유형12-3
def decimalmul524_Stem_076():
    stem = "수 카드 $$수식$$LEFT ( {sa} RIGHT )$$/수식$$, $$수식$$LEFT ( {sb} RIGHT )$$/수식$$, $$수식$$LEFT ( {sc} RIGHT )$$/수식$$, $$수식$$LEFT ( {sd} RIGHT )$$/수식$${rur1} □ 안에 한 번씩 모두 넣어 $$수식$$LEFT ($$/수식$$소수$$수식$$RIGHT ) `Times` LEFT ($$/수식$$자연수$$수식$$RIGHT )$$/수식$$의 곱셈식을 만들려고 합니다. 곱이 가장 클 때의 값을 구하시오.\n$$표$$□.□□$$수식$$Times$$/수식$$□$$/표$$\n"
    answer = "(답): $$수식$${scc}$$/수식$$\n"
    comment = "(해설)\n" \
              "높은 자리 숫자가 클수록 곱도 커지므로 ㉠.㉡㉢$$수식$$Times$$/수식$$㉣에서 곱이 가장 큰 곱셈식을 만들려면 " \
              "㉠과 ㉣에 큰 수인 $$수식$${se}$$/수식$$, $$수식$${sf}$$/수식$${rur2} 넣습니다.\n" \
              "→ $$수식$${se}.{sg}{sh} `Times` {sf} `=` {saa}$$/수식$$, $$수식$${sf}.{sg}{sh} `Times` {se} `=` {sbb}$$/수식$$\n" \
              "따라서 곱이 가장 클 때의 값은 $$수식$${scc}$$/수식$$입니다.\n\n"


    sa, sb, sc, sd = random.sample(list(range(1, 10)), 4)

    # while True:
    #     sa = np.random.randint(1, 10)
    #     sb = np.random.randint(1, 10)
    #     sc = np.random.randint(1, 10)
    #     sd = np.random.randint(1, 10)
    #
    #     if (sa != sb) and (sa != sc) and (sa != sd) and (sb != sc) and (sb != sd) and (sc != sd):
    #         break

    temp_list = [sa, sb, sc, sd]
    temp_list.sort(reverse=True)
    # temp_list.reverse()
    [se, sf, sg, sh] = temp_list

    saa = round((se + (sg / 10) + (sh / 100)) * sf, 2)
    sbb = round((sf + (sg / 10) + (sh / 100)) * se, 2)
    scc = max([saa, sbb])

    rur1 = josa(sd, "를")
    rur2 = josa(sf, "를")

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, rur1=rur1)
    answer = answer.format(scc=scc)
    comment = comment.format(se=se, sf=sf, sg=sg, sh=sh, saa=saa, sbb=sbb, scc=scc, rur2=rur2)

    return stem, answer, comment




























































# 5-2-4-유형12-4
def decimalmul524_Stem_077():
    stem = "수 카드 $$수식$$LEFT ( {sa} RIGHT )$$/수식$$, $$수식$$LEFT ( {sb} RIGHT )$$/수식$$, $$수식$$LEFT ( {sc} RIGHT )$$/수식$$, $$수식$$LEFT ( {sd} RIGHT )$$/수식$${rur1} □ 안에 한 번씩 모두 넣어 $$수식$$LEFT ($$/수식$$소수$$수식$$RIGHT ) `Times` LEFT ($$/수식$$자연수$$수식$$RIGHT )$$/수식$$의 곱셈식을 만들려고 합니다. 곱이 가장 작을 때의 값을 구하시오.\n□.□□$$수식$$Times$$/수식$$□\n"
    answer = "(답): $$수식$${scc}$$/수식$$\n"
    comment = "(해설)\n" \
              "높은 자리 숫자가 작을수록 곱도 작아지므로 ㉠.㉡㉢$$수식$$Times$$/수식$$㉣에서 곱이 가장 작은 곱셈식을 만들려면 " \
              "㉠과 ㉣에 작은 수인 $$수식$${se}$$/수식$$, $$수식$${sf}$$/수식$${rur2} 넣습니다.\n" \
              "→ $$수식$${se}.{sg}{sh} `Times` {sf} `=` {saa}$$/수식$$, $$수식$${sf}.{sg}{sh} `Times` {se} `=` {sbb}$$/수식$$\n" \
              "따라서 곱이 가장 작을 때의 값은 $$수식$${scc}$$/수식$$입니다.\n\n"


    sa, sb, sc, sd = random.sample(list(range(1, 10)), 4)

    # while True:
    #     sa = np.random.randint(2, 10)
    #     sb = np.random.randint(2, 10)
    #     sc = np.random.randint(2, 10)
    #     sd = np.random.randint(2, 10)
    #     if (sa != sb) and (sa != sc) and (sa != sd) and (sb != sc) and (sb != sd) and (sc != sd):
    #         break

    temp_list = [sa, sb, sc, sd]
    temp_list.sort()
    [se, sf, sg, sh] = temp_list

    saa = round((se + (sg / 10) + (sh / 100)) * sf, 2)
    sbb = round((sf + (sg / 10) + (sh / 100)) * se, 2)
    scc = min([saa, sbb])

    rur1 = josa(sd, "를")
    rur2 = josa(sf, "를")


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, rur1=rur1)
    answer = answer.format(scc=scc)
    comment = comment.format(se=se, sf=sf, sg=sg, sh=sh, saa=saa, sbb=sbb, scc=scc, rur2=rur2)

    return stem, answer, comment


























































# 5-2-4-유형12-5
def decimalmul524_Stem_078():
    stem = "$$수식$$3$$/수식$$장의 수 카드 중 $$수식$$2$$/수식$$장을 골라 각각 한 번씩 사용하여 만들 수 있는 가장 큰 소수 한 자리 수와 가장 작은 소수 한 자리 수의 곱은 얼마입니까?\n$$수식$$LEFT ( {sa} RIGHT )$$/수식$$,$$수식$$LEFT ( {sb} RIGHT )$$/수식$$,$$수식$$LEFT ( {sc} RIGHT )$$/수식$$\n"
    answer = "(답): $$수식$${saa}$$/수식$$\n"
    comment = "(해설)\n" \
              "만들 수 있는 가장 큰 소수 한 자리 수는 $$수식$${sd}.{se}$$/수식$$이고,\n" \
              "만들 수 있는 가장 작은 소수 한 자리 수는 $$수식$${sf}.{se}$$/수식$$입니다.\n" \
              "→ $$수식$${sd}.{se} `Times` {sf}.{se} `=` {saa}$$/수식$$\n\n"


    sa, sb, sc = random.sample(list(range(1, 10)), 3)

    # while True:
    #     sa = np.random.randint(1, 10)
    #     sb = np.random.randint(1, 10)
    #     sc = np.random.randint(1, 10)
    #     if (sa != sb) and (sa != sc) and (sb != sc):
    #         break

    temp_list = [sa, sb, sc]
    temp_list.sort(reverse=True)
    # temp_list.reverse()
    [sd, se, sf] = temp_list

    saa = round((sd + (se / 10)) * (sf + (se / 10)), 2)


    stem = stem.format(sa=sa, sb=sb, sc=sc)
    answer = answer.format(saa=saa)
    comment = comment.format(sd=sd, se=se, sf=sf, saa=saa)

    return stem, answer, comment





















































# 5-2-4-유형12-6
def decimalmul524_Stem_079():
    stem = "$$수식$$3$$/수식$$장의 수 카드 중 $$수식$$2$$/수식$$장을 골라 각각 한 번씩 사용하여 만들 수 있는 가장 큰 소수 두 자리 수와 가장 작은 소수 두 자리 수의 곱은 얼마입니까? $$수식$$LEFT ($$/수식$$단, 소수점 아래 마지막 자리는 $$수식$$0$$/수식$$이 될 수 없습니다.$$수식$$RIGHT )$$/수식$$\n$$수식$$LEFT ( {ss} RIGHT )$$/수식$$, $$수식$$LEFT ( {sa} RIGHT )$$/수식$$, $$수식$$LEFT ( {sb} RIGHT )$$/수식$$\n"
    answer = "(답): $$수식$${saa}$$/수식$$\n"
    comment = "(해설)\n" \
              "만들 수 있는 가장 큰 소수 두 자리 수는 $$수식$${sc}.0{sd}$$/수식$$이고,\n" \
              "만들 수 있는 가장 작은 소수 두 자리 수는 $$수식$$0.{sd}{sc}$$/수식$$입니다.\n" \
              "→ $$수식$${sc}.0{sd} `Times` 0.{sd}{sc} `=` {saa}$$/수식$$\n\n"


    sa, sb = random.sample(list(range(1, 6)), 2)

    # while True:
    #     sa = np.random.randint(1, 6)
    #     sb = np.random.randint(1, 6)
    #     if sa != sb:
    #         break

    sc = max([sa, sb])
    sd = min([sa, sb])
    ss = 0
    saa = round((sc + (sd / 100)) * ((sd / 10) + (sc / 100)), 4)


    stem = stem.format(sa=sa, sb=sb, ss=ss)
    answer = answer.format(saa=saa)
    comment = comment.format(sc=sc, sd=sd, saa=saa)

    return stem, answer, comment






















































# 5-2-4-유형13-1
def decimalmul524_Stem_080():
    stem = "㉠, ㉡, ㉢에 알맞은 수로 짝 지어진 것을 고르시오.\n$$표$$$$수식$${saa} `Times` 10 `=`$$/수식$$㉠\n$$수식$${saa} `Times` 100 `=`$$/수식$$㉡\n$$수식$${saa} `Times` 1000 `=`$$/수식$$㉢$$/표$$\n① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${saa} `Times` 10 `=` {sa}$$/수식$$\n" \
              "$$수식$${saa} `Times` 100 `=` {sb}$$/수식$$\n" \
              "$$수식$${saa} `Times` 1000 `=` {sc}$$/수식$$\n\n"


    while True:
        saade = np.random.randint(1, 100)
        saa = round(saade / 100, 2)
        if saade % 10 != 0:
            break

    sa = round(saa * 10, 1)
    sb = round(saa * 100)
    sc = round(saa * 1000)
    sd = round(saa * 10000)

    y1 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", sa, "㉡", sb, "㉢", sc)
    y2 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", sb, "㉡", sa, "㉢", sd)
    y3 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", sd, "㉡", sa, "㉢", sc)
    y4 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", sa, "㉡", sb, "㉢", sd)
    y5 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", sb, "㉡", sc, "㉢", sa)

    candidates = [y1, y2, y3, y4, y5]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4, x5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):
        if sdx == y1:
            correct_idx = idx
            break


    stem = stem.format(saa=saa, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(saa=saa, sa=sa, sb=sb, sc=sc)

    return stem, answer, comment

























































# 5-2-4-유형13-2
def decimalmul524_Stem_081():
    stem = "다음 계산을 이용하여 $$수식$${saa} `Times` {sdd}$$/수식$$을 계산하시오.\n$$표$$$$수식$${saa} `Times` {sbb} `=` {scc}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} `Times` {sdd}$$/수식$$은 $$수식$${saa} `Times` {sbb}$$/수식$$보다 $$수식$${sbb}$$/수식$$에 $$수식$$0$$/수식$$이 " \
              "$$수식$$1$$/수식$$개 더 있으므로 $$수식$${scc}$$/수식$$에서 오른쪽으로 한 칸 옮기면 $$수식$${see}$$/수식$$입니다.\n\n"


    while True:
        saade = np.random.randint(11, 100)
        saa = round(saade / 10, 1)
        if saade % 10 != 0:
            break

    sbb = np.random.randint(11, 100)
    scc = round(saa * sbb, 1)
    if scc - (scc // 1) == 0:
        scc = round(scc)

    sdd = sbb * 10
    see = round(scc * 10)


    stem = stem.format(saa=saa, sdd=sdd, sbb=sbb, scc=scc)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sdd=sdd, sbb=sbb, scc=scc, see=see)

    return stem, answer, comment
























































# 5-2-4-유형13-3
def decimalmul524_Stem_082():
    stem = "다음 계산을 이용하여 $$수식$${saa} `Times` {sdd}$$/수식$$을 계산하시오.\n$$표$$$$수식$${saa} `Times` {sbb} `=` {scc}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} `Times` {sdd}$$/수식$$은 $$수식$${saa} `Times` {sbb}$$/수식$$보다 $$수식$${sbb}$$/수식$$에 " \
              "$$수식$$0$$/수식$$이 $$수식$$2$$/수식$$개 더 있으므로 $$수식$${scc}$$/수식$$에서 오른쪽으로 두 칸 옮기면 $$수식$${see}$$/수식$$입니다.\n\n"


    while True:
        saade = np.random.randint(11, 100)
        saa = round(saade / 10, 1)
        if saade % 10 != 0:
            break

    sbb = np.random.randint(11, 99)
    scc = round(saa * sbb, 1)
    if scc - (scc // 1) == 0:
        scc = round(scc)

    sdd = sbb * 100
    see = round(scc * 100)


    stem = stem.format(saa=saa, sdd=sdd, sbb=sbb, scc=scc)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sdd=sdd, sbb=sbb, scc=scc, see=see)

    return stem, answer, comment























































# 5-2-4-유형13-4
def decimalmul524_Stem_083():
    stem = "계산 결과가 다른 것을 고르시오.\n① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "① $$수식$${z1}$$/수식$$\n" \
              "② $$수식$${z2}$$/수식$$\n" \
              "③ $$수식$${z3}$$/수식$$\n" \
              "④ $$수식$${z4}$$/수식$$\n" \
              "⑤ $$수식$${z5}$$/수식$$\n\n"


    while True:
        saa = np.random.randint(11, 100)
        if saa % 10 != 0:
            break

    sbb = round(saa / 10, 1)
    scc = round(saa / 100, 2)
    sdd = round(sbb * 100)
    see = round(scc * 1000)

    sff = saa * 100
    sgg = saa * 10

    y1 = ["%s `Times` 100" % (sbb), "%s `Times` 100 `=` %s" % (sbb, sdd)]
    y2 = ["%s `Times` 1000" % (scc), "%s `Times` 1000 `=` %s" % (scc, see)]
    y3 = ["%s$$/수식$$의 $$수식$$100배" % (saa), "%s `Times` 100 `=` %s" % (saa, sff)]
    y4 = ["%s `Times` 10" % (saa), "%s `Times` 10 `=` %s" % (saa, sgg)]
    y5 = ["%s$$/수식$$의 $$수식$$100배" % (sbb), "%s `Times` 100 `=` %s" % (sbb, sgg)]

    candidates = [y1, y2, y3, y4, y5]
    np.random.shuffle(candidates)

    x1 = candidates[0][0]
    x2 = candidates[1][0]
    x3 = candidates[2][0]
    x4 = candidates[3][0]
    x5 = candidates[4][0]

    z1 = candidates[0][1]
    z2 = candidates[1][1]
    z3 = candidates[2][1]
    z4 = candidates[3][1]
    z5 = candidates[4][1]

    correct_idx = 0
    for idx, sdx in enumerate(candidates):
        if sdx == y3:
            correct_idx = idx
            break


    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(z1=z1, z2=z2, z3=z3, z4=z4, z5=z5)

    return stem, answer, comment






















































# 5-2-4-유형13-5
def decimalmul524_Stem_084():
    stem = "{p1}가 키우는 식물은 $$수식$${saa} rm m$$/수식$$까지 자랐고, {p2}가 키우는 식물은 $$수식$${sbb} rm {{cm}}$$/수식$$까지 자랐습니다. 누가 키우는 식물이 더 깁니까?\n"
    answer = "(답): {see}\n"
    comment = "(해설)\n" \
              "{p1}가 키우는 식물의 길이를 $$수식$$rm {{cm}}$$/수식$$ 단위로 나타내면 $$수식$$1 rm m `=` 100 rm {{cm}}$$/수식$$이므로\n" \
              "$$수식$${saa} `Times` 100 `=` {scc} LEFT ( rm {{cm}} RIGHT )$$/수식$$입니다.\n" \
              "따라서 $$수식$${sdd}$$/수식$$이므로 {see}가 키우는 식물이 더 깁니다.\n\n"


    p1 = ["은서", "지우", "지호"][np.random.randint(0, 3)]
    p2 = ["이수", "태호", "진서"][np.random.randint(0, 3)]

    while True:
        saade = np.random.randint(1, 1000)
        saa = round(saade / 1000, 3)
        sbbde = np.random.randint(1, 1000)
        sbb = round(sbbde / 10, 1)

        if (saade != sbbde):
            if (saade % 10 != 0) and (saade % 100 != 0) and (0.5 < saa) and (saa < 1) and (sbbde % 10 != 0) and (
                    (saa * 100 - 0.5) <= sbb) and (sbb <= (saa * 100 + 0.5)) and (sbb != saa * 100):
                break

    scc = round(saa * 100, 1)

    if scc - sbb > 0:
        sdd = "%s `&gt;` %s" % (scc, sbb)
        see = p1

    elif scc - sbb < 0:
        sdd = "%s `&gt;` %s" % (sbb, scc)
        see = p2


    stem = stem.format(p1=p1, saa=saa, p2=p2, sbb=sbb)
    answer = answer.format(see=see)
    comment = comment.format(p1=p1, saa=saa, scc=scc, sdd=sdd, see=see)

    return stem, answer, comment






















































# 5-2-4-유형13-6
def decimalmul524_Stem_085():
    stem = "굵기가 일정한 {s1} $$수식$$1 rm m$$/수식$$의 무게는 $$수식$${saa} rm kg$$/수식$$입니다. 이 {s1} $$수식$${sbb} rm m$$/수식$$의 무게는 몇 $$수식$$rm kg$$/수식$$입니까?\n"
    answer = "(답): $$수식$${scc} rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${s1} $$수식$${sbb} rm m$$/수식$$의 무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$${s1} $$수식$$1 rm m$$/수식$$의 무게$$수식$$RIGHT ) `Times` LEFT ($$/수식$$길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {saa} `Times` {sbb} `=` {scc} LEFT ( rm kg RIGHT )$$/수식$$입니다.\n\n"


    s1 = ["통나무", "철근"][np.random.randint(0, 2)]

    while True:
        saade = np.random.randint(401, 900)
        saa = round(saade / 100, 2)
        if saade % 10 != 0:
            break

    sbb = [1000, 100][np.random.randint(0, 2)]
    scc = round(saa * sbb)


    stem = stem.format(s1=s1, saa=saa, sbb=sbb)
    answer = answer.format(scc=scc)
    comment = comment.format(s1=s1, sbb=sbb, saa=saa, scc=scc)

    return stem, answer, comment

























































# 5-2-4-유형13-7
def decimalmul524_Stem_086():
    stem = "{s1} 가게는 여러 종류의 {s1}을 무게를 재어 팝니다. {p1}는 $$수식$${saa} rm g$$/수식$$짜리 {s1}을 $$수식$${scc}$$/수식$$개, {p2}는 $$수식$${sbb} rm g$$/수식$$짜리 {s1}을 $$수식$${sdd}$$/수식$$개 샀습니다. 두 사람이 산 {s1}의 무게의 합은 몇 $$수식$$rm g$$/수식$$입니까?\n"
    answer = "(답): $$수식$${sgg} rm g$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${p1}가 산 {s1}의 무게$$수식$$RIGHT ) `=` {saa} `Times` {scc} `=` {see} LEFT ( rm g RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${p2}가 산 {s1}의 무게$$수식$$RIGHT ) `=` {sbb} `Times` {sdd} `=` {sff} LEFT ( rm g RIGHT )$$/수식$$\n" \
              "따라서 두 사람이 산 {s1}의 무게의 합은 $$수식$${see} `+` {sff} `=` {sgg} LEFT ( rm g RIGHT )$$/수식$$입니다.\n\n"


    s1 = ["사탕", "초콜릿"][np.random.randint(0, 2)]
    p1 = ["은서", "지호", "희수"][np.random.randint(0, 3)]
    p2 = ["이수", "진서", "지혜"][np.random.randint(0, 3)]

    while True:
        saade = np.random.randint(31, 99)
        saa = round(saade / 10, 1)
        sbbde = np.random.randint(41, 90)
        sbb = round(sbbde / 10, 1)

        if (saade % 10 != 0) and (sbbde % 10 != 0):
            break

    [scc, sdd] = [[10, 100], [100, 10]][np.random.randint(0, 2)]

    see = round(saa * scc)
    sff = round(sbb * sdd)
    sgg = see + sff


    stem = stem.format(s1=s1, p1=p1, saa=saa, scc=scc, p2=p2, sbb=sbb, sdd=sdd)
    answer = answer.format(sgg=sgg)
    comment = comment.format(p1=p1, s1=s1, saa=saa, scc=scc, see=see, p2=p2, sbb=sbb, sdd=sdd, sff=sff, sgg=sgg)

    return stem, answer, comment




















































# 5-2-4-유형13-8
def decimalmul524_Stem_087():
    stem = "{p} 돈 $$수식$$`1`$$/수식$${s}{j} 우리나라 돈으로 바꾸면 $$수식$$`{sa}`$$/수식$$원입니다. $$수식$$`{sb}`$$/수식$${s}{j} 우리나라 돈으로 바꾸면 얼마가 됩니까?\n"
    answer = "(답): $$수식$$`{a1}`$$/수식$$원\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`Times`{sb}`=`{sc}` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$\n\n"


    p, s, sa = [['미국', '달러', 1165.69], ['중국', '위안', 174.63], ['일본', '엔', 10.73], ['영국', '파운드', 1550.73],
                ['인도', '루피', 16.22], ['베트남', '베트남동', 0.05], ['태국', '바트', 38.57], ['러시아', '러시아루블', 18.22],
                ['사우디', '사우디리얄', 310.73]][np.random.randint(0, 9)]

    j = proc_jo(s, 1)

    sb = [10, 100, 1000][np.random.randint(0, 3)]

    if sb == 10:
        sc = round(sa * sb, 3)

    else:
        sc = round(sa * sb)


    stem = stem.format(p=p, s=s, sa=sa, sb=sb, j=j)
    answer = answer.format(a1=sc)
    comment = comment.format(sa=sa, sb=sb, sc=sc)

    return stem, answer, comment





















































# 5-2-4-유형14-1
def decimalmul524_Stem_088():
    stem = "㉠, ㉡, ㉢에 알맞은 수로 짝 지어진 것을 고르시오.\n$$표$$$$수식$${saa} `Times` 0.1 `=`$$/수식$$㉠\n$$수식$${saa} `Times` 0.01 `=`$$/수식$$㉡\n$$수식$${saa} `Times` 0.001 `=`$$/수식$$㉢$$/표$$\n① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${saa} `Times` 0.1 `=` {sa}$$/수식$$\n" \
              "$$수식$${saa} `Times` 0.01 `=` {sb}$$/수식$$\n" \
              "$$수식$${saa} `Times` 0.001 `=` {sc}$$/수식$$\n\n"


    saa = np.random.randint(11, 100)
    sa = round(saa * 0.1, 1)
    if sa - (sa // 1) == 0:
        sa = round(sa)

    sb = round(saa * 0.01, 2)
    sc = round(saa * 0.001, 3)
    sd = round(saa * 0.0001, 4)

    y1 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", sa, "㉡", sb, "㉢", sc)
    y2 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", sb, "㉡", sa, "㉢", sd)
    y3 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", sd, "㉡", sa, "㉢", sc)
    y4 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", sa, "㉡", sb, "㉢", sd)
    y5 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", sb, "㉡", sc, "㉢", sa)

    candidates = [y1, y2, y3, y4, y5]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4, x5] = candidates

    correct_idx = 0

    for idx, sdx in enumerate(candidates):
        if sdx == y1:
            correct_idx = idx
            break


    stem = stem.format(saa=saa, sa=sa, sb=sb, sc=sc, sd=sd, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(saa=saa, sa=sa, sb=sb, sc=sc)

    return stem, answer, comment




























































# 5-2-4-유형14-2
def decimalmul524_Stem_089():
    stem = "다음 계산을 이용하여 $$수식$${saa} `Times` {sdd}$$/수식$${rur1} 계산하시오.\n$$표$$$$수식$${saa} `Times` {sbb} `=` {scc}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} `Times` {sdd}$$/수식$${eun1} $$수식$${saa} `Times` {sbb}$$/수식$$보다 $$수식$${sbb}$$/수식$$에 소수점 아래 자리 수가 $$수식$$1$$/수식$$개 더 늘어났으므로 " \
              "$$수식$${scc}$$/수식$$에서 소수점을 왼쪽으로 한 칸 옮기면 $$수식$${see}$$/수식$$입니다.\n\n"


    while True:
        saa = np.random.randint(11, 100)
        sbbde = np.random.randint(11, 100)
        sbb = round(sbbde / 10, 1)
        scc = round(saa * sbb, 1)
        if (sbbde % 10 != 0) and (scc - (scc // 1) != 0):
            break

    sdd = round(sbb * 0.1, 2)
    see = round(scc * 0.1, 2)

    rur1 = josa(sdd, "를")
    eun1 = josa(sdd, "는")


    stem = stem.format(saa=saa, sdd=sdd, sbb=sbb, scc=scc, rur1=rur1)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sdd=sdd, sbb=sbb, scc=scc, see=see, eun1=eun1)

    return stem, answer, comment




























































# 5-2-4-유형14-3
def decimalmul524_Stem_090():
    stem = "다음 계산을 이용하여 $$수식$${saa} `Times` {sdd}$$/수식$${rur1} 계산하시오.\n$$표$$$$수식$${saa} `Times` {sbb} `=` {scc}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} `Times` {sdd}$$/수식$${eun1} $$수식$${saa} `Times` {sbb}$$/수식$$보다 $$수식$${sbb}$$/수식$$에 소수점 아래 자리 수가 " \
              "$$수식$$2$$/수식$$개 더 늘어났으므로 $$수식$${scc}$$/수식$$에서 소수점을 왼쪽으로 두 칸 옮기면 $$수식$${see}$$/수식$$입니다.\n\n"


    while True:
        saa = np.random.randint(11, 100)
        sbbde = np.random.randint(11, 100)
        sbb = round(sbbde / 10, 1)
        scc = round(saa * sbb, 1)
        if (sbbde % 10 != 0) and (scc - (scc // 1) != 0):
            break

    sdd = round(sbb * 0.01, 3)
    see = round(scc * 0.01, 3)

    rur1 = josa(sdd, "를")
    eun1 = josa(sdd, "는")


    stem = stem.format(saa=saa, sdd=sdd, sbb=sbb, scc=scc, rur1=rur1)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sdd=sdd, sbb=sbb, scc=scc, see=see, eun1=eun1)

    return stem, answer, comment
























































# 5-2-4-유형14-4
def decimalmul524_Stem_091():
    stem = "곱의 소수점 아래 자리 수가 다른 것을 고르시오.\n① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${saa} `Times` {sgg} `=` {shh}$$/수식$$이므로\n" \
              "① $$수식$${z1}$$/수식$$\n" \
              "② $$수식$${z2}$$/수식$$\n" \
              "③ $$수식$${z3}$$/수식$$\n" \
              "④ $$수식$${z4}$$/수식$$\n" \
              "⑤ $$수식$${z5}$$/수식$$\n\n"


    saa = np.random.randint(11, 100)
    sbb = saa * 10
    scc = saa * 100

    sddde = np.random.randint(1, 10)
    sdd = round(sddde / 10, 1)

    see = round(sdd * 0.1, 2)
    sff = round(sdd * 0.01, 3)
    sgg = round(sdd * 10)
    shh = saa * sgg

    sii = round(saa * sdd, 1)
    if sii - (sii // 1) == 0:
        sii = round(sii)

    sjj = round(sbb * see, 1)
    if sjj - (sjj // 1) == 0:
        sjj = round(sjj)

    skk = round(scc * sff, 1)
    if skk - (skk // 1) == 0:
        skk = round(skk)

    sll = round(sbb * sff, 2)
    smm = round(saa / 10, 1)

    y1 = ["%s `Times` %s" % (saa, sdd), "%s `Times` %s `=` %s" % (saa, sdd, sii)]
    y2 = ["%s `Times` %s" % (sbb, see), "%s `Times` %s `=` %s" % (sbb, see, sjj)]
    y3 = ["%s `Times` %s" % (scc, sff), "%s `Times` %s `=` %s" % (scc, sff, skk)]
    y4 = ["%s `Times` %s" % (sbb, sff), "%s `Times` %s `=` %s" % (sbb, sff, sll)]
    y5 = ["%s `Times` %s" % (smm, sddde), "%s `Times` %s `=` %s" % (smm, sddde, sii)]

    candidates = [y1, y2, y3, y4, y5]
    np.random.shuffle(candidates)
    [[x1, z1], [x2, z2], [x3, z3], [x4, z4], [x5, z5]] = candidates

    correct_idx = 0

    for idx, sdx in enumerate(candidates):
        if sdx == y4:
            correct_idx = idx
            break


    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(saa=saa, sgg=sgg, shh=shh, z1=z1, z2=z2, z3=z3, z4=z4, z5=z5)

    return stem, answer, comment




















































# 5-2-4-유형14-5
def decimalmul524_Stem_092():
    stem = "선물을 포장하는 데 다음과 같이 끈을 사용하였습니다. 어느 색 끈을 몇 $$수식$$rm m$$/수식$$ 더 많이 사용하였습니까?\n$$표$${s1} 끈 : 전체 $$수식$${saa} rm m$$/수식$$의 $$수식$$0.1$$/수식$$만큼\n{s2} 끈 : 전체 $$수식$${sbb} rm m$$/수식$$의 $$수식$$0.01$$/수식$$만큼$$/표$$\n"
    answer = "(답): {s1} 끈, $$수식$${see} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$사용한 {s1} 끈의 길이$$수식$$RIGHT ) `=` {saa} `Times` 0.1 `=` {scc} LEFT ( rm m RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$사용한 {s2} 끈의 길이$$수식$$RIGHT ) `=` {sbb} `Times` 0.01 `=` {sdd} LEFT ( rm m RIGHT )$$/수식$$\n" \
              "$$수식$${scc} &gt; {sdd}$$/수식$$이므로 {s1} 끈을 $$수식$${scc} `-` {sdd} `=` {see} LEFT ( rm m RIGHT )$$/수식$$ 더 많이 사용하였습니다.\n\n"


    s1 = ["노란색", "연두색", "초록색", "주황색"][np.random.randint(0, 4)]
    s2 = ["파란색", "빨간색", "분홍색", "보라색"][np.random.randint(0, 4)]

    saa = np.random.randint(6, 15)
    sbb = np.random.randint(11, 25)
    scc = round(saa * 0.1, 1)
    sdd = round(sbb * 0.01, 2)
    see = round(scc - sdd, 2)

    if see - (see // 1) == 0:
        see = round(see)


    stem = stem.format(s1=s1, s2=s2, saa=saa, sbb=sbb)
    answer = answer.format(s1=s1, see=see)
    comment = comment.format(s1=s1, s2=s2, saa=saa, scc=scc, sbb=sbb, sdd=sdd, see=see)

    return stem, answer, comment





















































# 5-2-4-유형14-6
def decimalmul524_Stem_093():
    stem = "어느 날 휘발유 $$수식$$1 rm L$$/수식$$의 값은 $$수식$${saa}$$/수식$$원입니다. 휘발유 $$수식$${sbb} rm L$$/수식$$의 값은 얼마입니까?\n"
    answer = "(답): $$수식$${scc}$$/수식$$원\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$휘발유 $$수식$${sbb} rm L$$/수식$$의 값$$수식$$RIGHT ) `=` {saa} `Times` {sbb} `=` {scc} LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$\n\n"


    saa = np.random.randint(1101, 2000)
    sbb = [0.1, 0.01, 0.001][np.random.randint(0, 3)]
    scc = round(saa * sbb, 3)

    if scc - (scc // 1) == 0:
        scc = round(scc)


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(scc=scc)
    comment = comment.format(sbb=sbb, saa=saa, scc=scc)

    return stem, answer, comment

























































# 5-2-4-유형14-7
def decimalmul524_Stem_094():
    stem = "㉠, ㉡에 알맞은 수를 차례대로 구하시오.\n$$수식$$LEFT ( {saa} RIGHT )$$/수식$$ → $$수식$$LEFT ( {b1} RIGHT )$$/수식$$ → $$수식$$LEFT ($$/수식$${b2}$$수식$$RIGHT )$$/수식$$\n$$수식$$LEFT ($$/수식$${b3}$$수식$$RIGHT )$$/수식$$ → $$수식$$LEFT ( {b4} RIGHT )$$/수식$$ → $$수식$$LEFT ($$/수식$${b5}$$수식$$RIGHT )$$/수식$$\n"
    answer = "(답): $$수식$${sbb}$$/수식$$, $$수식$${scc}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} `Times` 0.1 `=` {sbb}$$/수식$$, $$수식$${sbb} `Times` 0.01 `=` {scc}$$/수식$$\n\n"


    saa = np.random.randint(11, 1000)

    sbb = round(saa * 0.1, 1)

    if sbb - (sbb // 1) == 0:
        sbb = round(sbb)

    scc = round(sbb * 0.01, 3)

    b1 = "{Times 0.1}"
    b2 = "㉠"
    b3 = "㉠"
    b4 = "{Times 0.01}"
    b5 = "㉡"


    stem = stem.format(saa=saa, b1=b1, b2=b2, b3=b3, b4=b4, b5=b5)
    answer = answer.format(sbb=sbb, scc=scc)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc)

    return stem, answer, comment


























































# 5-2-4-유형15-1
def decimalmul524_Stem_095():
    stem = "$$수식$$`{sa}`$$/수식$$의 $$수식$$`{sb}`$$/수식$$배는 얼마입니까?\n"
    answer = "(답): $$수식$$`{a1}`$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`$$/수식$$의 $$수식$$`{sb}`$$/수식$$배이므로 $$수식$$`{sa}`$$/수식$$에서 소수점을 왼쪽으로 $$수식$$`{sc}`$$/수식$$칸 옮깁니다.\n" \
              "→ $$수식$$`{sa}`times`{sb}`=`{sd}`$$/수식$$\n\n"


    while True:
        saa = np.random.uniform(101, 1000)
        sa = round(saa * 0.01, 2)
        if (saa % 10) != 0:
            break

    sb = [0.1, 0.01, 0.001][np.random.randint(0, 3)]

    sc = int((-1) * math.log10(sb))
    sd = round(sa * sb, 5)


    stem = stem.format(sa=sa, sb=sb)
    answer = answer.format(a1=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd)

    return stem, answer, comment


























































# 5-2-4-유형15-2
def decimalmul524_Stem_096():
    stem = "㉠, ㉡, ㉢에 알맞은 수로 짝 지어진 것을 고르시오.\n$$표$$$$수식$$`{sa}`TIMES`{sb}`=`{sg}`$$/수식$$\n$$수식$$`{sc}`TIMES`{sd}`=`{c1}`$$/수식$$\n$$수식$$`{sc}`TIMES`{se}`=`{c2}`$$/수식$$\n$$수식$$`{sc}`TIMES`{sf}`=`{c3}`$$/수식$$$$/표$$\n① {a1}\n② {a2}\n③ {a3}\n④ {a4}\n⑤ {a5}\n"
    answer = "(답): $$수식$$`{a}`$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`TIMES`{sb}`=`{ag}`$$/수식$$\n" \
              "$$수식$$`{sc}`TIMES`{sd}`=`{a}`$$/수식$$\n" \
              "$$수식$$`{sc}`TIMES`{se}`=`{b}`$$/수식$$\n" \
              "$$수식$$`{sc}`TIMES`{sf}`=`{c}`$$/수식$$\n\n"


    sa = np.random.randint(2, 10)  # 자연수
    sb = np.random.randint(2, 10)

    sc = round(sa * 0.1, 1)  # 소수점첫째
    sd = round(sb * 0.1, 1)  # 소수점첫째
    se = round(sb * 0.01, 2)
    sf = round(sb * 0.001, 3)
    sg = sa * sb

    a = round(sc * sd, 2)
    b = round(sc * se, 3)
    c = round(sc * sf, 4)
    d = round(c * 0.1, 5)

    c1 = "㉠"
    c2 = "㉡"
    c3 = "㉢"

    a1 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % (c1, a, c2, b, c3, c)
    a2 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % (c1, b, c2, a, c3, d)
    a3 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % (c1, d, c2, a, c3, c)
    a4 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % (c1, a, c2, b, c3, d)
    a5 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % (c1, b, c2, c, c3, a)

    if 10 > sg:
        a2 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%.5f$$/수식$$" % (c1, b, c2, a, c3, d)
        a3 = "%s $$수식$$%.5f$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % (c1, d, c2, a, c3, c)
        a4 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%.5f$$/수식$$" % (c1, a, c2, b, c3, d)

    candidates = [a1, a2, a3, a4, a5]
    ans = a1

    np.random.shuffle(candidates)

    a1, a2, a3, a4, a5 = candidates

    correct_idx = 0

    for i, ca in enumerate(candidates):
        if ca == ans:
            correct_idx = i
            break


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, c1=c1, c2=c2, c3=c3, a1=a1, a2=a2, a3=a3, a4=a4,
                       a5=a5)
    answer = answer.format(a=answer_dict[correct_idx])
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, a=a, b=b, c=c, ag=sg)

    return stem, answer, comment






















































# 5-2-4-유형15-3
def decimalmul524_Stem_097():
    stem = "다음 계산을 이용하여 $$수식$$`{sd}`times`{se}`$$/수식$${rur1} 계산하시오.\n$$표$$ $$수식$$`{sa}`times`{sb}`=`{sc}`$$/수식$$ $$/표$$\n"
    answer = "(답): $$수식$$`{a1}`$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sd}`times`{se}`$$/수식$${eun1} $$수식$$LEFT ($$/수식$$소수 한 자리 수$$수식$$RIGHT ) `times` LEFT ($$/수식$$소수 한 자리 수$$수식$$RIGHT )$$/수식$$이므로 " \
              "계산 결과는 소수 두 자리 수이므로 $$수식$$`{sd}`times`{se}`=`{sf}`$$/수식$$입니다.\n\n"


    while True:
        sa = np.random.randint(11, 100)
        sb = np.random.randint(11, 100)
        sc = sa * sb

        if (sc % 10 != 0) and (sb % 10 != 0) and (sc % 10 != 0):
            break

    sd = round(sa * 0.1, 1)
    se = round(sb * 0.1, 1)
    sf = round(sd * se, 2)

    rur1 = josa(se, "를")
    eun1 = josa(se, "은")


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, rur1=rur1)
    answer = answer.format(a1=sf)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, eun1=eun1)

    return stem, answer, comment
























































# 5-2-4-유형15-4
def decimalmul524_Stem_098():
    stem = "다음 계산을 이용하여 $$수식$$`{sd}`times`{se}`$$/수식$${rur1} 계산하시오.\n$$표$$ $$수식$$`{sa}`times`{sb}`=`{sc}`$$/수식$$ $$/표$$\n"
    answer = "(답): $$수식$$`{a1}`$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sd}`times`{se}`$$/수식$${eun1} $$수식$$LEFT ($$/수식$$소수 두 자리 수$$수식$$RIGHT ) `times` LEFT ($$/수식$$소수 두 자리 수$$수식$$RIGHT )$$/수식$$이므로 " \
              "계산 결과는 소수 네 자리 수이므로 $$수식$$`{sd}`times`{se}`=`{sf}`$$/수식$$입니다.\n\n"


    while True:
        sa = np.random.randint(11, 100)
        sb = np.random.randint(11, 100)
        sc = sa * sb
        if (sc % 10 != 0) and (sb % 10 != 0) and (sc % 10 != 0):
            break

    sd = round(sa * 0.01, 2)
    se = round(sb * 0.01, 2)
    sf = round(sd * se, 4)

    rur1 = josa(se, "를")
    eun1 = josa(se, "은")


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, rur1=rur1)
    answer = answer.format(a1=sf)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, eun1=eun1)

    return stem, answer, comment
























































# 5-2-4-유형15-5
def decimalmul524_Stem_099():
    stem = "$$수식$$`{sa}`times`{sb}`$$/수식$${eun1} 소수 몇 자리 수입니까?\n① {a1}\n② {a2}\n③ {a3}\n④ {a4}\n⑤ {a5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`times`{sb}`$$/수식$${eun1} $$수식$$LEFT ($$/수식$$소수 세 자리 수$$수식$$RIGHT ) `times` LEFT ($$/수식$$소수 두 자리 수$$수식$$RIGHT )$$/수식$$이므로 " \
              "계산 결과는 소수 다섯 자리 수가 됩니다.\n\n"


    a1 = "소수 한 자리 수"
    a2 = "소수 두 자리 수"
    a3 = "소수 세 자리 수"
    a4 = "소수 네 자리 수"
    a5 = "소수 다섯 자리 수"

    while True:
        sa = np.random.randint(1001, 10000)
        sb = np.random.randint(1, 100)

        if (sa % 2 != 0) and (sb % 2 != 0) and (sa % 10 != 0) and (sa % 10 != 0):
            sa = round(sa * 0.001, 3)
            sb = round(sb * 0.01, 2)
            break

    candidates = [a1, a2, a3, a4, a5]
    ans = a5

    np.random.shuffle(candidates)

    a1, a2, a3, a4, a5 = candidates

    correct_idx = 0

    for i, ca in enumerate(candidates):
        if ca == ans:
            correct_idx = i
            break

    eun1 = josa(sb, "는")


    stem = stem.format(sa=sa, sb=sb, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, eun1=eun1)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(sa=sa, sb=sb, eun1=eun1)

    return stem, answer, comment






















































# 5-2-4-유형15-6
def decimalmul524_Stem_100():
    stem = "$$수식$$`{sa}`times`{sb}`=`{sc}`$$/수식$$임을 이용하여 ㉠은 ㉡의 몇 배인지 구하시오.\n$$표$$ ㉠ $$수식$$`{sd}`times`{se}`$$/수식$$ ㉡ $$수식$$`{sf}`times`{sg}`$$/수식$$ $$/표$$\n"
    answer = "(답): $$수식$$`{a1}`$$/수식$$배\n"
    comment = "(해설)\n" \
              "㉠ $$수식$$`{sa}`times`{sb}`=`{sc}`$$/수식$$ → $$수식$$`{sd}`times`{se}`=`{sh}`$$/수식$$\n" \
              "㉡ $$수식$$`{sa}`times`{sb}`=`{sc}`$$/수식$$ → $$수식$$`{sf}`times`{sg}`=`{si}`$$/수식$$\n" \
              "따라서 ㉠과 ㉡의 $$수식$$`{sj}`$$/수식$$배입니다.\n\n"


    sa = np.random.randint(11, 100)
    sb = np.random.randint(2, 10)
    sc = sa * sb

    sd = round(sa * 0.1, 1)
    if sd - (sd // 1) == 0:
        sd = round(sd)

    se = round(sb * 0.1, 1)

    sh = round(sd * se, 2)
    if sh - (sh // 1) == 0:
        sh = round(sh)

    sj = [100, 1000][np.random.randint(0, 2)]

    if sj == 100:
        sf = round(sa * 0.01, 2)
        sg = round(sb * 0.01, 2)

    elif sj == 1000:
        sf = round(sa * 0.001, 3)
        sg = round(sb * 0.01, 3)

    si = "%s" % (round(sf * sg, 5))


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg)
    answer = answer.format(a1=sj)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sh=sh, si=si, sj=sj)

    return stem, answer, comment
























































# 5-2-4-유형15-7
def decimalmul524_Stem_101():
    stem = "$$수식$${saa} `Times` {sbb}$$/수식$${gwa1} 계산 결과가 같은 것은 어느 것입니까?\n{one_one} $$수식$${x1}$$/수식$$\n{one_two} $$수식$${x2}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${saa} `Times` {sbb} `=` {sgg}$$/수식$$이고\n" \
              "① $$수식$${x1} `=` {x3}$$/수식$$, ② $$수식$${x2} `=` {x4}$$/수식$$입니다.\n\n"


    while True:
        saade = np.random.randint(11, 1000)
        saa = round(saade / 10, 1)
        sbbde = np.random.randint(11, 1000)
        sbb = round(sbbde / 10, 1)
        if (saade % 10 != 0) and (sbbde % 10 != 0):
            break

    scc = round(saa * 0.1, 2)
    sdd = round(sbb * 0.1, 2)

    [see, sff] = [[round(saa * 100), round(sbb * 0.01, 3)], [round(saa * 1000), round(sbb * 0.001, 4)]][
        np.random.randint(0, 2)]

    if see - (see // 1) == 0:
        see = round(see)

    sgg = round(saa * sbb, 2)
    shh = round(scc * sdd, 4)
    sii = sgg

    y1 = ["%s `Times` %s" % (scc, sdd), shh]
    y2 = ["%s `Times` %s" % (see, sff), sii]

    candidates = [y1, y2]
    np.random.shuffle(candidates)

    x1 = candidates[0][0]
    x2 = candidates[1][0]
    x3 = candidates[0][1]
    x4 = candidates[1][1]

    correct_idx = 0
    for idx, sdx in enumerate(candidates):
        if sdx == y2:
            correct_idx = idx
            break

    one_one = "①"
    one_two = "②"

    gwa1 = josa(sbb, "과")


    stem = stem.format(saa=saa, sbb=sbb, x1=x1, x2=x2, one_one=one_one, one_two=one_two, gwa1=gwa1)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(saa=saa, sbb=sbb, sgg=sgg, scc=scc, sdd=sdd, shh=shh, see=see, sff=sff, sii=sii, x1=x1,
                             x2=x2, x3=x3, x4=x4)
    return stem, answer, comment


























































# 5-2-4-유형15-8
def decimalmul524_Stem_102():
    stem = "{p}가 계산기로 $$수식$$`{sa}`times`{a}`$$/수식$${rur1} 계산하려고 두 수를 눌렀는데 수 하나의 소수점을 잘못 눌러 계산 결과가 $$수식$$`{x}`$$/수식$${ga1} 나왔습니다. {p}가 계산기에 누른 두 수로 알맞은 것을 고르시오.\n① $$수식$${a1}$$/수식$$\n② $$수식$${a2}$$/수식$$\n③ $$수식$${a3}$$/수식$$\n④ $$수식$${a4}$$/수식$$\n⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): $$수식$$`{ans}`$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`times`{a}`=`{y}`$$/수식$$이어야 하는데 잘못 눌러서 $$수식$$`{x}`$$/수식$${ga1} 나왔으므로 " \
              "$$수식$$`{sd}`$$/수식$$와 $$수식$$`{a}`$$/수식$${rur1} 눌렀거나 " \
              "$$수식$$`{sa}`$$/수식$$와 $$수식$$`{b}`$$/수식$${rur2} 누른 것입니다.\n\n"


    p = ['민기', '지수', '주호', '현아'][np.random.randint(0, 4)]

    while True:
        sa = np.random.randint(5, 100)
        if sa % 5 == 0:
            if sa % 10 != 0:
                sa = round(sa * 0.01, 2)
                break
    while True:
        a = np.random.randint(1, 10)
        if a % 2 == 0:
            a = round(a * 0.1, 1)
            break

    y = round(sa * a, 2)
    x = round(y * 10, 2)
    if x - (x // 1) == 0:
        x = int(x)

    sb = round(sa * 0.1, 3)
    sc = round(sa * 100)
    sd = sa * 10
    b = round(a * 10)
    c = round(a * 100)
    d = round(a * 0.1, 2)

    a1 = "%.2f,``%d" % ((sa), (b))
    a2 = "%.2f,``%d" % ((sa), (c))
    a3 = "%.2f,``%s" % ((sa), (d))
    a4 = "%.3f,``%.1f" % ((sb), (a))
    a5 = "%d,``%.1f" % ((sc), (a))

    candidates = [a1, a2, a3, a4, a5]
    ans = a1

    np.random.shuffle(candidates)

    a1, a2, a3, a4, a5 = candidates

    correct_idx = 0

    for i, ca in enumerate(candidates):
        if ca == ans:
            correct_idx = i
            break

    rur1 = josa(a, "를")
    ga1 = josa(x, "가")
    rur2 = josa(b, "를")


    stem = stem.format(sa=sa, a=a, p=p, x=x, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, rur1=rur1, ga1=ga1)
    answer = answer.format(ans=answer_dict[correct_idx])
    comment = comment.format(sa=sa, a=a, y=y, x=x, sd=sd, b=b, ga1=ga1, rur1=rur1, rur2=rur2)

    return stem, answer, comment

























































# 5-2-4-유형16-1
def decimalmul524_Stem_103():
    stem = "□ 안에 알맞은 수를 구하시오.\n$$수식$$`{sa}`times`$$/수식$$□$$수식$$`=`{sb}`$$/수식$$\n"
    answer = "(답): $$수식$$`{a1}`$$/수식$$\n"
    comment = "(해설)\n" \
              "소수점이 왼쪽으로 $$수식$$`{sc}`$$/수식$$칸 옮겨진 것이므로 □$$수식$$`=`{sd}`$$/수식$$\n\n"


    while True:
        saa = np.random.randint(11, 100)
        sa = round(saa * 0.1, 1)
        if (saa % 10) != 0:
            break

    sb = [round(sa / 10, 2), round(sa / 100, 3), round(sa / 1000, 4)][np.random.randint(0, 3)]

    sc = int((-1) * math.log10(sb / sa))
    sd = round(sb / sa, 4)


    stem = stem.format(sa=sa, sb=sb)
    answer = answer.format(a1=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd)

    return stem, answer, comment



























































# 5-2-4-유형16-2
def decimalmul524_Stem_104():
    stem = "□ 안에 알맞은 수를 구하시오.\n$$수식$$`{sa}`times`$$/수식$$□$$수식$$`=`{sb}`$$/수식$$\n"
    answer = "(답): $$수식$$`{a1}`$$/수식$$\n"
    comment = "(해설)\n" \
              "소수점이 오른쪽으로 $$수식$$`{sc}`$$/수식$$칸 옮겨진 것이므로 □$$수식$$`=`{sd}`$$/수식$$\n\n"


    while True:
        saa = np.random.randint(101, 1000)
        sa = round(saa * 0.01, 2)
        if (saa % 10 != 0) and (saa % 100 != 0):
            break

    sb = int([sa * 100, sa * 1000, sa * 10000][np.random.randint(0, 3)])
    sc = int(math.log10(sb / sa))
    sd = round(sb / sa)


    stem = stem.format(sa=sa, sb=sb)
    answer = answer.format(a1=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd)

    return stem, answer, comment


























































# 5-2-4-유형16-3
def decimalmul524_Stem_105():
    stem = "어떤 수에 $$수식$$`{sa}`$$/수식$$을 곱했더니 $$수식$$`{sb}`$$/수식$${ga1} 되었습니다. 어떤 수는 얼마입니까?\n"
    answer = "(답): $$수식$$`{a1}`$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`$$/수식$$을 곱하면 소수점이 왼쪽으로 $$수식$$`{sc}`$$/수식$$칸 옮겨집니다. " \
              "어떤 수에서 소수점이 왼쪽으로 $$수식$$`{sc}`$$/수식$$칸 " \
              "옮겨진 수가 $$수식$$`{sb}`$$/수식$$이므로 어떤 수는 $$수식$$`{sd}`$$/수식$$입니다.\n\n"


    sa = ([0.01, 0.001, 0.0001][np.random.randint(0, 3)])
    sb = np.random.randint(2, 10)
    sb = round(sb * 0.1, 1)
    sc = int((-1) * math.log10(sa))
    sd = round(sb / sa)

    ga1 = josa(sb, "가")


    stem = stem.format(sa=sa, sb=sb, ga1=ga1)
    answer = answer.format(a1=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd)

    return stem, answer, comment
































































# 5-2-4-유형16-4
def decimalmul524_Stem_106():
    stem = "보기를 이용하여 □ 안에 알맞은 수를 구하시오.\n$$표$$ 보기\n$$수식$$`{sa}`times`{sb}`={sc}`$$/수식$$ $$/표$$\n$$수식$$`{sd}`times`$$/수식$$□$$수식$$`=`{se}`$$/수식$$\n"
    answer = "(답): $$수식$$`{a1}`$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sd}`$$/수식$${nun1} $$수식$$`{sa}`$$/수식$$의 $$수식$$`{a}`$$/수식$$배인데 " \
              "$$수식$$`{se}`$$/수식$${nun2} $$수식$$`{sc}`$$/수식$$의 $$수식$$`{c}`$$/수식$$배이므로\n" \
              "□ 안에 알맞은 수는 $$수식$$`{sb}`$$/수식$$의 $$수식$$`{b}`$$/수식$$배인 $$수식$$`{sf}`$$/수식$$입니다.\n\n"


    while True:
        sa = np.random.randint(101, 160)
        sb = np.random.randint(1000 / sa, 10000 / sa)
        if (sa % 10 != 0) and (sb % 10 != 0) and (sb > 9) and (sb < 100):
            break

    sc = sa * sb
    ran = np.random.randint(0, 5)

    aten = sa / 10
    ahun = sa / 100
    chun = sc / 100
    ctho = sc / 1000
    ctth = sc / 10000

    if ran == 0:
        sd = aten
        se = chun
    elif ran == 1:
        sd = aten
        se = ctho
    elif ran == 2:
        sd = aten
        se = ctth
    elif ran == 3:
        sd = ahun
        se = ctho
    elif ran == 4:
        sd = aten
        se = ctth

    a = round(sd / sa, 4)
    c = round(se / sc, 4)
    b = round(c / a, 4)
    sf = round(sb * b, 4)

    nun1 = josa(sd, "는")
    nun2 = josa(se, "는")


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)
    answer = answer.format(a1=sf)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, a=a, b=b, c=c, nun1=nun1, nun2=nun2)

    return stem, answer, comment































































# 5-2-4-유형16-5
def decimalmul524_Stem_107():
    stem = "보기를 이용하여 □ 안에 알맞은 수를 구하시오.\n$$표$$ 보기\n$$수식$$`{sa}`times`{sb}`={sc}`$$/수식$$ $$/표$$\n□$$수식$$`times`{sd}`=`{se}`$$/수식$$\n"
    answer = "(답): $$수식$$`{a1}`$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sd}`$$/수식$$은 $$수식$$`{sb}`$$/수식$$의 $$수식$$`{b}`$$/수식$$배인데 " \
              "$$수식$$`{se}`$$/수식$${eun1} $$수식$$`{sc}`$$/수식$$의 $$수식$$`{c}`$$/수식$$배이므로\n" \
              "□ 안에 알맞은 수는 $$수식$$`{sa}`$$/수식$$의 $$수식$$`{a}`$$/수식$$배인 $$수식$$`{sf}`$$/수식$$입니다.\n\n"


    while True:
        sa = np.random.randint(101, 160)
        sb = np.random.randint(1000 / sa, 10000 / sa)
        if (sa % 10 != 0) and (sb % 10 != 0) and (9 < sb) and (sb < 100):
            break

    sc = sa * sb
    ran = np.random.randint(0, 4)

    if ran == 0:
        sd = sb * 10
        se = sc / 10
    elif ran == 1:
        sd = sb * 10
        se = sc / 100
    elif ran == 2:
        sd = sb * 100
        se = sc / 10
    elif ran == 3:
        sd = sb * 100
        se = sc / 100

    b = round(sd / sb)
    c = round(se / sc, 2)
    a = round(c / b, 4)
    sf = round(sa * a, 4)

    eun1 = josa(se, "는")


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)
    answer = answer.format(a1=sf)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, a=a, b=b, c=c, eun1=eun1)

    return stem, answer, comment






























































# 5-2-4-유형16-6
def decimalmul524_Stem_108():
    stem = "□ 안에 알맞은 수가 다른 하나를 고르시오.\n{one_one} {a1}\n{one_two} {a2}\n{one_three} {a3}\n{one_four} {a4}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "① {c1}\n" \
              "② {c2}\n" \
              "③ {c3}\n" \
              "④ {c4}\n\n"


    while True:
        saa = np.random.randint(5001, 10000)
        sa = round(saa * 0.01, 2)
        if (saa % 10) != 0:
            break
    sb = round(sa * 100)

    while True:
        scc = np.random.randint(1001, 10000)
        sc = round(scc * 0.001, 3)
        if (scc % 10) != 0:
            break
    sd = round(sc * 100, 1)

    while True:
        see = np.random.randint(101, 1000)
        se = round(see * 0.001, 3)
        if (see % 10) != 0:
            break
    sf = round(se * 100, 1)

    while True:
        sgg = np.random.randint(101, 1000)
        sg = round(sgg * 0.01, 2)
        if (sgg % 10) != 0:
            break
    sh = round(sg * 1000)

    b = round(sb / sa)
    a = math.log10(b)
    d = round(sd / sc)
    c = math.log10(d)
    f = round(sf / se)
    e = math.log10(f)
    h = round(sh / sg)
    g = math.log10(h)

    a1 = "$$수식$${%.2f}`times`□`={%d}`$$/수식$$" % (sa, sb)
    a2 = "$$수식$${%.3f}`times`□`={%.1f}`$$/수식$$" % (sc, sd)
    a3 = "$$수식$$□`times`{%.3f}`={%.1f}`$$/수식$$" % (se, sf)
    a4 = "$$수식$${%.2f}`times`□`={%d}`$$/수식$$" % (sg, sh)

    c1 = "소수점이 오른쪽으로 $$수식$$`{%d}`$$/수식$$칸 옮겨진 것이므로 $$수식$$`□`={%d}`$$/수식$$" % (a, b)
    c2 = "소수점이 오른쪽으로 $$수식$$`{%d}`$$/수식$$칸 옮겨진 것이므로 $$수식$$`□`={%d}`$$/수식$$" % (c, d)
    c3 = "소수점이 오른쪽으로 $$수식$$`{%d}`$$/수식$$칸 옮겨진 것이므로 $$수식$$`□`={%d}`$$/수식$$" % (e, f)
    c4 = "소수점이 오른쪽으로 $$수식$$`{%d}`$$/수식$$칸 옮겨진 것이므로 $$수식$$`□`={%d}`$$/수식$$" % (g, h)

    alist = [a1, a2, a3, a4]
    clist = [a, c, e, g]

    dict = {a1: c1, a2: c2, a3: c3, a4: c4}

    for i, ca in enumerate(clist):
        if ca == 3:
            ans = alist[i]

    candidates = [a1, a2, a3, a4]
    com = [a1, a2, a3, a4]

    np.random.shuffle(candidates)

    x1, x2, x3, x4 = candidates
    correct_idx = 0

    for i, ca in enumerate(candidates):
        if ca == a1:
            com[i] = dict[a1]
        if ca == a2:
            com[i] = dict[a2]
        if ca == a3:
            com[i] = dict[a3]
        if ca == a4:
            com[i] = dict[a4]
        if ca == ans:
            correct_idx = i

    y1, y2, y3, y4 = com

    one_one = "①"
    one_two = "②"
    one_three = "③"
    one_four = "④"


    stem = stem.format(a1=x1, a2=x2, a3=x3, a4=x4, one_one=one_one, one_two=one_two, one_three=one_three, one_four=one_four)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(c1=y1, c2=y2, c3=y3, c4=y4)

    return stem, answer, comment




























































# 5-2-4-유형16-7
def decimalmul524_Stem_109():
    stem = "㉠과 ㉡에 알맞은 수의 곱을 구하시오.\n$$표$$$$수식$${saa} `Times` {sbb} `=`$$/수식$$㉠, $$수식$${scc} `Times`$$/수식$$㉡$$수식$$`=` {sdd}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${shh}$$/수식$$\n"
    comment = "(해설)\n" \
              "● $$수식$${saa} `Times` {sbb} `=` {see}$$/수식$$이므로 ㉠$$수식$$`=` {see}$$/수식$$입니다.\n" \
              "● $$수식$${scc} `Times`$$/수식$$㉡$$수식$$`=` {sdd}$$/수식$$에서 소수점이 왼쪽으로 $$수식$${sff}$$/수식$$칸 옮겨진 것이므로 " \
              "㉡$$수식$$`=` {sgg}$$/수식$$입니다.\n" \
              "→ $$수식$${see} `Times` {sgg} `=` {shh}$$/수식$$\n\n"


    while True:
        saade = np.random.randint(1001, 10000)
        saa = round(saade / 1000, 3)
        if saade % 10 != 0:
            break

    sbb = [10, 100][np.random.randint(0, 2)]

    while True:
        scc = np.random.randint(10001, 100000)
        if scc % 10 == 0:
            break

    sdd = [round(scc / 10), round(scc / 100, 2), round(scc / 1000, 3)][np.random.randint(0, 3)]
    see = round(saa * sbb, 2)
    sff = int((-1) * math.log10(sdd / scc))
    sgg = round(sdd / scc, 3)
    shh = round(see * sgg, 5)


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(shh=shh)
    comment = comment.format(saa=saa, sbb=sbb, see=see, scc=scc, sdd=sdd, sff=sff, sgg=sgg, shh=shh)

    return stem, answer, comment


























































# 5-2-4-유형17-1
def decimalmul524_Stem_110():
    stem = "어떤 수에 $$수식$${sa}$$/수식$${rur1} 곱해야 할 것을 잘못하여 더했더니 $$수식$${sb}$$/수식$${ga1} 되었습니다. 바르게 계산한 값을 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □라 하여 잘못 계산한 식을 세우면\n" \
              "□$$수식$$`+`{sa}`=`{sb}`$$/수식$$, □$$수식$$`=`{sb}`-`{sa}`$$/수식$$, □$$수식$$`=`{a}`$$/수식$$\n" \
              "따라서 바르게 계산한 값은 $$수식$$`{a}`times`{sa}`=`{sc}`$$/수식$$입니다.\n\n"


    sa = np.random.randint(4, 10)

    while True:
        a = np.random.randint(13, 42)
        if a % 10 != 0:
            a = round(a * 0.01, 2)
            break

    sb = sa + a

    sc = round(sa * a, 2)
    if sc - (sc // 1) == 0:
        sc = round(sc)

    rur1 = josa(sa, "를")
    ga1 = josa(sb, "가")


    stem = stem.format(sa=sa, sb=sb, rur1=rur1, ga1=ga1)
    answer = answer.format(a1=sc)
    comment = comment.format(sa=sa, sb=sb, sc=sc, a=a)

    return stem, answer, comment































































# 5-2-4-유형17-2
def decimalmul524_Stem_111():
    stem = "어떤 수에 $$수식$${sa}$$/수식$${rur1} 곱해야 할 것을 잘못하여 뺐더니 $$수식$${sb}$$/수식$${ga1} 되었습니다. 바르게 계산한 값을 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □라 하여 잘못 계산한 식을 세우면\n" \
              "□$$수식$$`-`{sa}`=`{sb}`$$/수식$$, □$$수식$$`=`{sb}`+`{sa}`$$/수식$$, □$$수식$$`=`{sc}`$$/수식$$\n" \
              "따라서 바르게 계산한 값은 $$수식$$`{sc}`times`{sa}`=`{sd}`$$/수식$$입니다.\n\n"


    while True:
        sa = np.random.randint(11, 89)
        sb = np.random.randint(11, 89)
        if (sa % 10 != 0) & (sb % 10 != 0):
            if sa != sb:
                sa = round(sa * 0.1, 1)
                sb = round(sb * 0.1, 1)
                if (sa + sb >= 2.3) & (sa + sb < 10):
                    test = int(10 * (sa + sb))
                    if test % 10 != 0:
                        break

    sc = round(sa + sb, 1)
    if sc - (sc // 1) == 0:
        sc = round(sc)

    sd = round(sc * sa, 2)
    if sd - (sd // 1) == 0:
        sd = round(sd)

    rur1= josa(sa, "를")
    ga1 = josa(sb, "가")


    stem = stem.format(sa=sa, sb=sb, rur1=rur1, ga1=ga1)
    answer = answer.format(a1=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd)

    return stem, answer, comment

































































# 5-2-4-유형17-3
def decimalmul524_Stem_112():
    stem = "어떤 수에 $$수식$${sa}$$/수식$$을 곱해야 할 것을 잘못하여 $$수식$${sb}$$/수식$$을 곱했더니 $$수식$${sc}$$/수식$${ga1} 되었습니다. 바르게 계산한 값을 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □라 하여 잘못 계산한 식을 세우면 □$$수식$$`times`{sb}`=`{sc}`$$/수식$$이므로\n" \
              "□는 $$수식$${sc}$$/수식$$의 소수점을 오른쪽으로 $$수식$${a}$$/수식$$칸 옮긴 $$수식$${sd}$$/수식$$입니다.\n" \
              "따라서 바르게 계산한 값은 $$수식$$`{sd}`times`{sa}`=`{se}`$$/수식$$입니다.\n\n"


    while True:
        sa = [0.1, 0.01, 0.001][np.random.randint(0, 3)]
        sb = [0.1, 0.01, 0.001][np.random.randint(0, 3)]
        sc = np.random.randint(1001, 10000)
        if sa != sb:
            if sc % 10 != 0:
                sc = round(sc * 0.001, 3)
                break

    a = round((-1) * math.log10(sb))
    sd = round(sc / sb, 3)
    if sd - (sd // 1) == 0:
        sd = round(sd)

    se = round(sd * sa, 5)

    ga1 = josa(sc, "가")


    stem = stem.format(sa=sa, sb=sb, sc=sc, ga1=ga1)
    answer = answer.format(a1=se)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, a=a)

    return stem, answer, comment






























































# 5-2-4-유형17-4
def decimalmul524_Stem_113():
    stem = "어떤 수에 $$수식$${sa}$$/수식$$을 곱해야 할 것을 잘못하여 $$수식$${sb}$$/수식$$을 곱했더니 $$수식$${sc}$$/수식$${ga1} 되었습니다. 바르게 계산한 값을 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □라 하여 잘못 계산한 식을 세우면 □$$수식$$`times`{sb}`=`{sc}`$$/수식$$이므로\n" \
              "□는 $$수식$${sc}$$/수식$$의 소수점을 {a}으로 $$수식$${b}$$/수식$$칸 옮긴 $$수식$${sd}$$/수식$$입니다.\n" \
              "따라서 바르게 계산한 값은 $$수식$$`{sd}`times`{sa}`=`{se}`$$/수식$$입니다.\n\n"


    sa = [0.1, 0.01, 0.001, 10, 100][np.random.randint(0, 5)]

    if sa > 1:
        sb = [0.1, 0.01, 0.001][np.random.randint(0, 3)]
        a = "오른쪽"
        while True:
            sc = np.random.randint(1001, 10000)
            if sc % 10 != 0:
                sc = round(sc * 0.001, 3)
                break

    elif sa < 1:
        sb = [10, 100][np.random.randint(0, 2)]
        a = "왼쪽"
        while True:
            sc = np.random.randint(1001, 10000)
            if sc % 10 != 0:
                sc = round(sc * 0.1, 1)
                break

    b = round(abs(math.log10(sb)))

    sd = round(sc / sb, 3)
    if sd - (sd // 1) == 0:
        sd = int(sd)

    se = round(sd * sa, 6)
    if se - (se // 1) == 0:
        se = round(se)

    ga1 = josa(sc, "가")


    stem = stem.format(sa=sa, sb=sb, sc=sc, ga1=ga1)
    answer = answer.format(a1=se)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, a=a, b=b)

    return stem, answer, comment












