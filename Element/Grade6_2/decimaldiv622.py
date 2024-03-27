import numpy as np
import random




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








def josa(a, b):
    if b == "를" or b == "을":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "를"
        else:
            return "을"

    elif b == "과" or b == "와":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "와"
        else:
            return "과"

    elif b == "가" or b == "이":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "가"
        else:
            return "이"

    elif b == "로" or b == "으로":
        if (str(a))[-1] == "0" or (str(a))[-1] == "3" or (str(a))[-1] == "6":
            return "으로"
        else:
            return "로"









# 6-2-2-01
def decimaldiv622_Stem_001():
    stem = "$$수식$${saa} DIV {sbb}$$/수식$$와 몫이 같은 나눗셈은 어느 것인가요?\n① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "나누는 수와 나누어지는 수에 같은 수를 곱하면 몫은 변하지 않습니다.\n" \
              "$$수식$${saa} DIV {sbb} = {scc} DIV {sff} = {see} DIV {sdd}$$/수식$$\n\n"


    while True:
        sdd = np.random.randint(2, 10)
        see = np.random.randint(100, 1000)
        if ((see % 10) != 0) and (see % sdd) == 0:
            break

    scc = round(see / 10, 1)
    saa = round(see / 100, 2)
    sff = round(sdd / 10, 1)
    sbb = round(sdd / 100, 2)

    ans_choice = np.random.randint(0, 2)

    if ans_choice == 0:
        y1 = f"$$수식$${see} DIV {sdd}$$/수식$$"
    else:
        y1 = f"$$수식$${scc} DIV {sff}$$/수식$$"

    y2 = f"$$수식$${scc} DIV {sdd}$$/수식$$"
    y3 = f"$$수식$${see} DIV {sff}$$/수식$$"
    y4 = f"$$수식$${scc} DIV {sbb}$$/수식$$"
    y5 = f"$$수식$${see} DIV {sbb}$$/수식$$"

    candidates = [y1, y2, y3, y4, y5]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4, x5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):
        if sdx == y1:
            correct_idx = idx
            break


    stem = stem.format(saa=saa, sbb=sbb, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=answer_dict[correct_idx])
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff)

    return stem, answer, comment




























# 6-2-2-02
def decimaldiv622_Stem_002():
    stem = "자연수의 나눗셈을 이용하여 ㉠과 ㉡의 차를 구해 보세요.\n$$표$$ $$수식$${saa} DIV {sbb} = {scc} DIV {sdd} = $$/수식$$ ㉠\n$$수식$${see} DIV {sff} = {sgg} DIV {shh} = $$/수식$$ ㉡$$/표$$\n"
    answer = "(정답)\n$$수식$${spp}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {scc} DIV {sdd} = {sii}$$/수식$$\n" \
              "$$수식$${see} DIV {sff} = {sgg} DIV {shh} = {sjj}$$/수식$$\n" \
              "→ $$수식$${smm} - {snn} = {spp}$$/수식$$\n\n"


    while True:
        sdd = np.random.randint(2, 10)
        scc = np.random.randint(11, 100)
        if ((scc % sdd) == 0) and (scc % 10) != 0:
            break


    skk = [0.1, 0.01][np.random.randint(0, 2)]

    if skk == 0.1:
        sbb = round(sdd * skk, 1)
        saa = round(scc * skk, 1)

    else:
        sbb = round(sdd * skk, 2)
        saa = round(scc * skk, 2)


    while True:
        shh = np.random.randint(10, 100)
        sgg = np.random.randint(100, 1000)
        if (shh % 10) != 0:
            if ((sgg % 10) != 0) and ((sgg % shh) == 0):
                break

    see = round(sgg * skk, 2)
    sff = round(shh * skk, 2)

    sii = int(scc / sdd)
    sjj = int(sgg / shh)

    smm = max(sii, sjj)
    snn = min(sii, sjj)
    spp = smm - snn


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh)
    answer = answer.format(spp=spp)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, sii=sii, sjj=sjj,
                             smm=smm, snn=snn, spp=spp)

    return stem, answer, comment

























# 6-2-2-03
def decimaldiv622_Stem_003():
    stem = "$$수식$${saa} DIV {sbb} = {scc}$$/수식$${rur1} 이용하여 □ 안에 알맞은 수를 써넣으세요.\n$$수식$${sdd} DIV {see} = {boxone}$$/수식$$\n"
    answer = "(정답)\n$$수식$${sff}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sdd}$$/수식$${wa1} $$수식$${see}$$/수식$$에 각각 $$수식$${tmp}$$/수식$$을 곱하면 " \
              "$$수식$${saa}$$/수식$${wa2} $$수식$${sbb}$$/수식$$이므로\n" \
              "$$수식$${sdd} DIV {see} = {sff}$$/수식$$ 입니다.\n\n"


    while True:
        while True:
            sbb = np.random.randint(2, 10)
            saa = np.random.randint(100, 1000)
            if ((saa % 10) != 0) and (saa % sbb) == 0:
                break

        skk = [0.1, 0.01][np.random.randint(0, 2)]

        if skk == 0.1:
            sdd = round(saa * skk, 1)
            see = round(sbb * skk, 1)
            tmp = 10

        else:
            sdd = round(saa * skk, 2)
            see = round(sbb * skk, 2)
            tmp = 100

        scc = int(saa / sbb)
        sff = int(sdd / see)

        if ((sff == sdd / see) and (sff == saa / sbb) and (sff == scc)):
            break

    boxone = "□"

    rur1 = josa(scc, "를")
    wa1 = josa(sdd, "와")
    wa2 = josa(saa, "와")


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, boxone=boxone, rur1=rur1)
    answer = answer.format(sff=sff)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, skk=skk, tmp=tmp, wa1=wa1, wa2=wa2)

    return stem, answer, comment




























# 6-2-2-04
def decimaldiv622_Stem_004():
    stem = "종이 꽃가루를 만들기 위해 종이띠를 $$수식$${saa} rmcm$$/수식$$씩 자르려고 합니다. 종이띠 $$수식$${sbb} rmcm$$/수식$$로 종이 꽃가루를 몇 개 만들 수 있나요?\n"
    answer = "(정답)\n$$수식$${scc}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$만들 수 있는 종이 꽃가루 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {sbb} DIV {saa} = {see} DIV {sdd} = {scc} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"


    while True:
        sdd = np.random.randint(2, 10)
        see = np.random.randint(100, 1000)
        if ((see % sdd) == 0) and (see % 10) != 0:
            break

    skk = 0.1

    # saa = round(sdd * skk, 2)
    # sbb = round(see * skk, 2)
    # scc = int(sbb / saa)

    saa = round(sdd * skk, 5)
    sbb = round(see * skk, 5)
    scc = int(see / sdd)



    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(scc=scc)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, skk=skk)

    return stem, answer, comment





























# 6-2-2-05
def decimaldiv622_Stem_005():
    stem = "다음 $$수식$$&lt;$$/수식$$조건$$수식$$&gt;$$/수식$$을 만족하는 나눗셈식을 찾아 계산해 보세요.\n$$표$$ · $$수식$${saa} DIV {sbb}$$/수식$${rur1} 이용하여 풀 수 있습니다.\n· 나누어지는 수와 나누는 수를 각각 $$수식$$100$$/수식$$배 하면 $$수식$${saa} DIV {sbb}$$/수식$${ga1} 됩니다. $$/표$$\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa}$$/수식$${wa1} $$수식$${sbb}$$/수식$${rur2} 각각 $$수식$$1 over 100$$/수식$$배 하면 " \
              "$$수식$${scc}$$/수식$${wa2} $$수식$${sdd}$$/수식$${ga2} 됩니다.\n" \
              "→ $$수식$${scc} DIV {sdd} = {see}$$/수식$$\n\n"


    while True:
        while True:
            sbb = np.random.randint(11, 100)
            saa = np.random.randint(100, 1000)
            if ((saa % sbb) == 0) and ((saa % 10) != 0):
                break

        skk = 0.01
        scc = round(saa * skk, 2)
        sdd = round(sbb * skk, 2)
        see = scc / sdd

        if (see == saa / sbb):
            see = int(see)
            break

    rur1 = josa(sbb, "를")
    ga1 = josa(sbb, "가")
    wa1 = josa(saa, "와")

    rur2 = josa(sbb, "를")
    wa2 = josa(scc, "와")
    ga2 = josa(sdd, "가")


    stem = stem.format(saa=saa, sbb=sbb, rur1=rur1, ga1=ga1)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, skk=skk, wa1=wa1, rur2=rur2, wa2=wa2, ga2=ga2)

    return stem, answer, comment


































# 6-2-2-06
def decimaldiv622_Stem_006():
    stem = "리본 고리를 만들기 위해 리본을 $$수식$${saa} rm m$$/수식$$씩 자르려고 합니다. 리본 $$수식$${sbb} rm m$$/수식$$로 고리를 몇 개 만들 수 있는지 자연수의 나눗셈을 이용하여 구해 보세요.\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$개\n"
    comment = "(해설)\n" \
              "고리를 몇 개 만들 수 있는지 구하는 식을 쓰면 $$수식$${sbb} DIV {saa}$$/수식$$입니다.\n" \
              "$$수식$${sbb} DIV {saa}$$/수식$$에서 나누는 수와 나누어지는 수를 똑같이 $$수식$${tmp}$$/수식$$배 하면 " \
              "$$수식$${sdd} DIV {scc}$$/수식$${ga1} 됩니다. \n" \
              "$$수식$${sbb} DIV {saa} = {sdd} DIV {scc} = {scc}$$/수식$$이므로 고리를 $$수식$${see}$$/수식$$개 만들 수 있습니다.\n\n"


    while True:
        scc = np.random.randint(11, 100)
        sdd = np.random.randint(100, 1000)

        skk = 0.01
        sbb = round(sdd * skk, 2)
        saa = round(scc * skk, 2)
        tmp = 100

        see = int(sbb / saa)

        if ((sdd % scc) == 0) and ((sdd % 10) != 0) and see == sdd / scc:
            break


    ga1 = josa(scc, "가")


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, skk=skk, tmp=tmp, ga1=ga1)

    return stem, answer, comment


    # while True:
    #     scc = np.random.randint(11, 100)
    #     sdd = np.random.randint(100, 1000)
    #     if ((sdd % scc) == 0) and ((sdd % 10) != 0):
    #         break
    #
    # skk = 0.01
    # sbb = round(sdd * skk, 2)
    # saa = round(scc * skk, 2)
    # tmp = 100
    #
    # see = int(sbb / saa)

































# 6-2-2-07
def decimaldiv622_Stem_007():
    stem = "□ 안에 알맞은 수를 써넣으세요.\n$$수식$${saa}$$/수식$$ → $$수식$${box_q}$$/수식$$ → $$수식$${boxone}$$/수식$$\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {scc} DIV {sdd} = {see}$$/수식$$\n\n"


    while True:
        sdd = np.random.randint(11, 100)
        scc = np.random.randint(100, 1000)

        skk = 0.1

        saa = round(scc * skk, 1)
        sbb = round(sdd * skk, 1)

        see = int(saa / sbb)

        if ((scc % sdd) == 0) and ((scc % 10) != 0) and see == scc / sdd:
            break


    boxone = "box{　　　}"
    box_q = "`div`%s" % sbb


    stem = stem.format(saa=saa, boxone=boxone, box_q=box_q)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, skk=skk)

    return stem, answer, comment


    # while True:
    #     sdd = np.random.randint(11, 100)
    #     scc = np.random.randint(100, 1000)
    #
    #     if ((scc % sdd) == 0) and ((scc % 10) != 0):
    #         break
    #
    # skk = 0.1
    # saa = round(scc * skk, 1)
    # sbb = round(sdd * skk, 1)
    #
    # see = int(saa / sbb)






























# 6-2-2-09
def decimaldiv622_Stem_008():
    stem = "빈칸에 알맞은 수를 써넣으세요.\n$$수식$${boxone} ```` ```` DIV {sbb} $$/수식$$ → $$수식$${boxtwo}$$/수식$$\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {scc} DIV {sdd} = {see}$$/수식$$\n\n"


    while True:
        sdd = np.random.randint(11, 100)
        scc = np.random.randint(100, 1000)

        skk = 0.1

        saa = round(scc * skk, 1)
        sbb = round(sdd * skk, 1)

        boxone = "%0.1f" % saa
        see = int(saa / sbb)

        if ((scc % sdd) == 0) and ((scc % 10) != 0) and see == scc / sdd:
            break


    boxtwo = "□"


    stem = stem.format(saa=saa, sbb=sbb, boxone=boxone, boxtwo=boxtwo)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, skk=skk)

    return stem, answer, comment































# 6-2-2-10
def decimaldiv622_Stem_009():
    stem = "계산 결과를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${saa} DIV {sbb}$$/수식$$  ○  $$수식$${scc} DIV {sdd}$$/수식$$\n"
    answer = "(정답)\n$$수식$${sll}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {see} DIV {sff} = {sgg}$$/수식$$\n" \
              "$$수식$${scc} DIV {sdd} = {shh} DIV {sii} = {sjj}$$/수식$$\n" \
              "따라서 $$수식$${smm} &gt; {snn}$$/수식$$이므로 $$수식$${sll}$$/수식$$입니다.\n\n"


    while True:
        ans_choice = np.random.randint(0, 2)

        if ans_choice == 0:
            see = np.random.randint(10, 100)
            shh = np.random.randint(100, 1000)

        else:
            see = np.random.randint(100, 1000)
            shh = np.random.randint(10, 100)

        sff = np.random.randint(2, 10)

        sii = np.random.randint(2, 10)

        skk = 0.1
        saa = round(see * skk, 1)
        sbb = round(sff * skk, 1)
        scc = round(shh * skk, 1)
        sdd = round(sii * skk, 1)

        sgg = int(saa / sbb)
        sjj = int(scc / sdd)
        smm = max(sgg, sjj)
        snn = min(sgg, sjj)

        if ((see % 10) != 0) and ((see % sff) == 0) and ((shh % 10) != 0) and (
                (shh % sii) == 0) and sgg == see / sff and sjj == shh / sii and sff != sii:
            break


    if sgg > sjj:
        sll = "&gt;"

    elif sgg < sjj:
        sll = "&lt;"

    else:
        sll = "="


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(sll=sll)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, sii=sii, sjj=sjj,
                             skk=skk, sll=sll, smm=smm, snn=snn)

    return stem, answer, comment



    # while True:
    #     sff = np.random.randint(2, 10)
    #     see = np.random.randint(10, 100)
    #     if ((see % 10) != 0) and ((see % sff) == 0):
    #         break
    #
    # while True:
    #     sii = np.random.randint(2, 10)
    #     shh = np.random.randint(100, 1000)
    #     if ((see % 10) != 0) and ((see % sff) == 0):
    #         break
    #
    #
    # skk = 0.1
    # saa = round(see * skk, 1)
    # sbb = round(sff * skk, 1)
    # scc = round(shh * skk, 1)
    # sdd = round(sii * skk, 1)
    #
    # sgg = int(saa / sbb)
    # sjj = int(scc / sdd)
    # smm = max(sgg, sjj)
    # snn = min(sgg, sjj)


































# 6-2-2-11
def decimaldiv622_Stem_010():
    stem = "㉠, ㉡, ㉢, ㉣ 중에서 수가 다른 하나를 찾아 기호를 써 보세요.\n$$표$$ $$수식$${saa} DIV {sbb} = {{㉠}} over 10 DIV {{㉡}} over 10 = {scc} DIV {{㉢}} = {{㉣}}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n㉠\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {see} over 10 DIV {sff} over 10 = {scc} DIV {sdd} = {sgg}$$/수식$$\n" \
              "㉠ $$수식$$= {scc}$$/수식$$, ㉡ $$수식$$= {sdd}$$/수식$$, ㉢ $$수식$$= {sff}$$/수식$$, " \
              "㉣ $$수식$$= {sdd}$$/수식$$이므로 수가 다른 하나는 ㉠ 입니다.\n\n"


    sdd = np.random.randint(4, 10)
    scc = sdd ** 2

    saa = round(scc / 10, 1)
    sbb = round(sdd / 10, 1)

    see = scc
    sff = sdd
    sgg = sdd



    stem = stem.format(saa=saa, sbb=sbb, scc=scc)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg)

    return stem, answer, comment



    # while True:
    #     while True:
    #         sdd = np.random.randint(2, 10)
    #         scc = np.random.randint(10, 100)
    #         if ((scc % sdd) == 0):
    #             break
    #
    #     saa = scc / 10
    #     sbb = sdd / 10
    #     see = scc
    #     sff = sdd
    #
    #     if ((saa / sbb) == sdd) and ((saa / sbb) == sff) and (sdd == sff):
    #         sgg = sdd
    #         break


























# 6-2-2-12
def decimaldiv622_Stem_011():
    stem = "큰 수를 작은 수로 나눈 몫을 빈칸에 써넣으세요.\n$$수식$${boxone}````{boxtwo}````$$/수식$$ $$수식$${boxthree}$$/수식$$\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sbb} &gt; {saa}$$/수식$$이므로\n" \
              "$$수식$${sbb} DIV {saa} = {sdd} DIV {scc} = {see}$$/수식$$\n\n"


    while True:
        scc = np.random.randint(11, 100)
        sdd = np.random.randint(100, 1000)

        skk = 0.1
        sbb = round(sdd * skk, 1)
        saa = round(scc * skk, 1)

        see = int(sbb / saa)

        if (scc % 10) != 0 and ((sdd % 10) != 0) and ((sdd % scc) == 0) and see == sdd / scc:
            break


    r_num = np.random.randint(0, 2)

    if r_num == 0:
        if skk == 0.1:
            boxone = "%0.1f" % saa
            boxtwo = "%0.1f" % sbb
        else:
            boxone = "%0.2f" % saa
            boxtwo = "%0.2f" % sbb

    else:
        if skk == 0.1:
            boxone = "%0.1f" % sbb
            boxtwo = "%0.1f" % saa
        else:
            boxone = "%0.2f" % sbb
            boxtwo = "%0.2f" % saa

    boxthree = "box{　　　}"


    stem = stem.format(saa=saa, sbb=sbb, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, skk=skk)

    return stem, answer, comment
































# 6-2-2-13
def decimaldiv622_Stem_012():
    stem = "두 나눗셈의 몫의 차를 구해 보세요.\n$$표$$ $$수식$${saa} DIV {sbb}$$/수식$$    $$수식$${scc} DIV {sdd}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${sll}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {see} DIV {sff} = {sii}$$/수식$$\n" \
              "$$수식$${scc} DIV {sdd} = {sgg} DIV {shh} = {sjj}$$/수식$$\n" \
              "→ $$수식$${smm} - {snn} = {sll}$$/수식$$\n\n"


    while True:
        while True:
            sff = np.random.randint(10, 100)
            see = np.random.randint(100, 1000)
            if (sff % 10) != 0 and ((see % sff) == 0) and ((see % 10) != 0):
                break

        while True:
            shh = np.random.randint(10, 100)
            sgg = np.random.randint(100, 1000)
            if (shh % 10) != 0 and ((sgg % shh) == 0) and ((sgg % 10) != 0):
                break

        skk = 0.1

        saa = round(see * skk, 1)
        sbb = round(sff * skk, 1)
        scc = round(sgg * skk, 1)
        sdd = round(shh * skk, 1)

        if ((saa / sbb) == (see / sff)) and ((scc / sdd) == (sgg / shh)):
            sii = int(saa / sbb)
            sjj = int(scc / sdd)
            smm = max(sii, sjj)
            snn = min(sii, sjj)
            break

    sll = smm - snn


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(sll=sll)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, sii=sii, sjj=sjj,
                             skk=skk, sll=sll, smm=smm, snn=snn)

    return stem, answer, comment
































# 6-2-2-14
def decimaldiv622_Stem_013():
    stem = "빈칸에 알맞은 수를 써넣으세요.\n$$표$$ $$수식$${saa} DIV {sbb}$$/수식$$ → $$수식$${boxone}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {scc} DIV {sdd} = {see}$$/수식$$\n\n"


    while True:
        sdd = np.random.randint(10, 100)
        scc = np.random.randint(100, 1000)

        skk = [0.1, 0.01][np.random.randint(0, 2)]

        if skk == 0.1:
            saa = round(scc * skk, 1)
            sbb = round(sdd * skk, 1)

        else:
            saa = round(scc * skk, 2)
            sbb = round(sdd * skk, 2)

        see = int(saa / sbb)

        if (sdd % 10) != 0 and ((scc % 10) != 0) and ((scc % sdd) == 0) and see == scc / sdd:
            break


    boxone = "□"


    stem = stem.format(saa=saa, sbb=sbb, boxone=boxone)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, skk=skk)

    return stem, answer, comment



    # while True:
    #     sdd = np.random.randint(10, 100)
    #     scc = np.random.randint(100, 1000)
    #
    #     if (sdd % 10) != 0:
    #         if ((scc % 10) != 0) and ((scc % sdd) == 0):
    #             break
    #
    # skk = [0.1, 0.01][np.random.randint(0, 2)]
    #
    # if skk == 0.1:
    #     saa = round(scc * skk, 1)
    #     sbb = round(sdd * skk, 1)
    #
    # else:
    #     saa = round(scc * skk, 2)
    #     sbb = round(sdd * skk, 2)
    #
    # boxone = "□"
    #
    # see = int(saa / sbb)




























# 6-2-2-16
def decimaldiv622_Stem_014():
    stem = "{who}이네 집에서 가장 큰 방의 넓이는 $$수식$${saa} rmm^2$$/수식$$이고, {who}이의 방의 넓이는 $$수식$${sbb} rmm^2$$/수식$$입니다. 가장 큰 방의 넓이는 {who}이의 방 넓이의 몇 배인가요?\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$배\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$가장 큰 방의 넓이$$수식$$RIGHT ) DIV LEFT ($$/수식$${who}이의 방 넓이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${saa} DIV {sbb} = {scc} DIV {sdd} = {see} LEFT ($$/수식$$배$$수식$$RIGHT )$$/수식$$\n\n"


    who = ["영선", "기백", "나연", "민혁", "혁준", "희진", "유정", "병훈"][np.random.randint(0, 8)]


    while True:
        sdd = np.random.randint(100, 1000)
        scc = np.random.randint(1000, 10000)

        skk = [0.1, 0.01][np.random.randint(0, 2)]

        if skk == 0.1:
            saa = round(scc * skk, 1)
            sbb = round(sdd * skk, 1)

        else:
            saa = round(scc * skk, 2)
            sbb = round(sdd * skk, 2)

        see = int(saa / sbb)

        if (sdd % 10) != 0 and ((scc % 10) != 0) and ((scc % sdd) == 0) and see == scc / sdd:
            break



    stem = stem.format(saa=saa, sbb=sbb, who=who)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, skk=skk, who=who)

    return stem, answer, comment




    # while True:
    #     sdd = np.random.randint(100, 1000)
    #     scc = np.random.randint(1000, 10000)
    #     if (sdd % 10) != 0:
    #         if ((scc % 10) != 0) and ((scc % sdd) == 0):
    #             break
    #
    # skk = [0.1, 0.01][np.random.randint(0, 2)]
    #
    # if skk == 0.1:
    #     saa = round(scc * skk, 1)
    #     sbb = round(sdd * skk, 1)
    #
    # else:
    #     saa = round(scc * skk, 2)
    #     sbb = round(sdd * skk, 2)
    #
    # see = int(saa / sbb)


































# 6-2-2-17
def decimaldiv622_Stem_015():
    stem = "높이가 $$수식$${saa} rm {{cm}}$$/수식$$, 넓이가 $$수식$${sbb} rm {{cm}}^2$$/수식$$인 평행사변형이 있습니다. 이 평행사변형의 밑변의 길이는 몇 $$수식$$rm {{cm}}$$/수식$$입니까?\n"
    answer = "(정답)\n$$수식$${see} rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$밑변의 길이$$수식$$RIGHT ) = LEFT ($$/수식$$평행사변형의 넓이$$수식$$RIGHT ) DIV LEFT ($$/수식$$높이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {sbb} DIV {saa} = {sdd} DIV {scc} = {see} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n\n"


    while True:
        scc = np.random.randint(10, 100)
        sdd = np.random.randint(100, 1000)

        skk = 0.1

        saa = round(scc * skk, 1)
        sbb = round(sdd * skk, 1)

        see = int(sbb / saa)

        if (scc % 10) != 0 and ((sdd % 10) != 0) and ((sdd % scc) == 0) and see == sdd / scc:
            break


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, skk=skk)

    return stem, answer, comment



    # while True:
    #     scc = np.random.randint(10, 100)
    #     sdd = np.random.randint(100, 1000)
    #     if (scc % 10) != 0:
    #         if ((sdd % 10) != 0) and ((sdd % scc) == 0):
    #             break
    #
    # skk = 0.1
    # saa = round(scc * skk, 1)
    # sbb = round(sdd * skk, 1)
    # see = int(sbb / saa)




























# 6-2-2-18
def decimaldiv622_Stem_016():
    stem = "$$수식$${saa} DIV {sbb}$$/수식$${wa1} 몫이 같은 나눗셈을 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${scc} DIV {sdd}$$/수식$$    ㉡ $$수식$${see} DIV {sff}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${sqq}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {sgg} DIV {shh} = {snn}$$/수식$$\n" \
              "㉠ $$수식$${scc} DIV {sdd} = {sii} DIV {sjj} = {soo}$$/수식$$\n" \
              "㉡ $$수식$${see} DIV {sff} = {sll} DIV {smm} = {spp}$$/수식$$\n" \
              "따라서 $$수식$${saa} DIV {sbb}$$/수식$${wa1} 몫이 같은 나눗셈식은 $$수식$${sqq}$$/수식$$입니다.\n\n"


    # while True:
    #     while True:
    #         shh = np.random.randint(100, 1000)
    #         sgg = np.random.randint(1000, 10000)
    #
    #         if (shh % 10) != 0:
    #             if ((sgg % 10) != 0) and ((sgg % shh) == 0):
    #                 break
    #
    #     skk = 0.01
    #
    #     saa = round(sgg * skk, 2)
    #     sbb = round(shh * skk, 2)
    #     snn = int(saa / sbb)
    #     num = np.random.randint(0, 2)
    #
    #     while True:
    #         sjj = np.random.randint(1000, 10000)
    #         sii = np.random.randint(10000, 100000)
    #
    #         if (sjj % 10) != 0:
    #             if num == 0:
    #                 if ((sii % 10) != 0) and ((sii % sjj) == 0):
    #                     if sii == (snn * sjj):
    #                         break
    #
    #             else:
    #                 if ((sii % 10) != 0) and ((sii % sjj) == 0):
    #                     break
    #
    #     while True:
    #         smm = np.random.randint(1000, 10000)
    #         sll = np.random.randint(10000, 100000)
    #
    #         if (smm % 10) != 0:
    #             if num == 1:
    #                 if sll == (snn * smm):
    #                     if ((sll % 10) != 0) and ((sll % smm) == 0):
    #                         break
    #
    #             else:
    #                 if ((sll % 10) != 0) and ((sll % smm) == 0):
    #                     break
    #
    #     scc = round(sii * skk, 2)
    #     sdd = round(sjj * skk, 2)
    #     see = round(sll * skk, 2)
    #     sff = round(smm * skk, 2)
    #
    #     soo = int(scc / sdd)
    #     spp = int(see / sff)
    #
    #     if soo != spp:
    #         break

    # 위 코드는 계산이 너무 느림

    while True:
        snn = np.random.randint(2, 100)
        shh = np.random.randint(100, 1000)
        sgg = shh * snn

        ans_choice = np.random.randint(0, 2)

        if ans_choice == 0:
            soo = snn
            spp = np.random.randint(2, 100)
        else:
            soo = np.random.randint(2, 100)
            spp = snn

        sjj = np.random.randint(1000, 10000)
        sii = sjj * soo

        smm = np.random.randint(1000, 10000)
        sll = smm * spp

        skk = 0.01

        saa = round(sgg * skk, 2)
        sbb = round(shh * skk, 2)

        scc = round(sii * skk, 2)
        sdd = round(sjj * skk, 2)

        see = round(sll * skk, 2)
        sff = round(smm * skk, 2)


        if 1000 <= sgg and sgg < 10000 and shh % 10 != 0 and sgg % 10 != 0:
            if sjj % 10 != 0 and 10000 <= sii and sii < 100000 and sii % 10 != 0:
                if smm % 10 != 0 and 10000 <= sll and sll < 100000 and sll % 10 != 0:
                    break

    if soo == snn:
        sqq = "%s" % "㉠"
    else:
        sqq = "%s" % "㉡"


    wa1 = josa(sbb, "와")


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, wa1=wa1)
    answer = answer.format(sqq=sqq)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, sii=sii, sjj=sjj,
                             sll=sll, smm=smm, snn=snn, soo=soo, spp=spp, sqq=sqq, wa1=wa1)

    return stem, answer, comment
































# 6-2-2-19
def decimaldiv622_Stem_017():
    stem = "{who}이는 $$수식$$1$$/수식$$시간에 $$수식$${saa} rm {{km}}$$/수식$$를 걷습니다. 같은 빠르기로 {who}이네 집에서 $$수식$${sbb} rm {{km}}$$/수식$$떨어진 할머니네 집까지 걸어가려고 합니다. {who}이가 집에서 출발한 지 몇 시간 몇 분 후에 할머니네 집에 도착하나요?\n" \
        "{boxblank} 시간 {boxblank} 분 후"
    answer = "(정답)\n$$수식$${sdd}$$/수식$$, $$수식$${sff}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( {sbb} rm {{km}}$$/수식$$를 걷는 데 걸리는 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$$전체 거리$$수식$$RIGHT ) DIV LEFT ( 1$$/수식$$시간 동안 걷는 거리$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {sbb} DIV {saa}$$/수식$$\n" \
              "$$수식$${scc} LEFT ($$/수식$$시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${scc}$$/수식$$시간 $$수식$$= {sdd} {see} over 10$$/수식$$시간$$수식$$= {sdd} {sff}over 60$$/수식$$시간" \
              "$$수식$$= {sdd}$$/수식$$시간 $$수식$${sff}$$/수식$$분\n" \
              "따라서 {who}이는 집에서 출발한 지 $$수식$${sdd}$$/수식$$시간 $$수식$${sff}$$/수식$$분 후에 할머니네 집에 도착하게 됩니다.\n\n"

    boxblank = "$$수식$$BOX{　　}$$/수식$$"

    who = ["수진", "경진", "혁진", "민혁", "가영", "하율", "미란", "나은", "태연", "창훈"][np.random.randint(0, 10)]

    while True:
        see = np.random.randint(1, 10)
        sff = see * 6
        sdd = np.random.randint(1, 4)

        scc = round(sdd + (see / 10), 1)

        skk = 0.01
        saa_three = np.random.randint(100, 400)
        saa = round(skk * saa_three, 2)
        sbb = round(saa * scc, 3)

        if saa_three % 10 != 0 and (str(sbb))[-3] == ".":
            break




    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, who=who, boxblank=boxblank)
    answer = answer.format(sdd=sdd, sff=sff)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, who=who)

    return stem, answer, comment




    # while True:
    #     smallb = np.random.randint(100, 1000)
    #     smalla = np.random.randint(100, 1000)
    #
    #     if (smalla % 10) != 0:
    #         if (smallb > smalla) and ((smallb % smalla) == 0):
    #             break
    #
    # saa = round(smalla * 0.01, 2)
    # sbb = round(smallb * 0.01, 2)
    # scc = round(sbb / saa, 1)
    # sdd = round(scc)
    #
    # if sdd == 0:
    #     sd = ""
    # else:
    #     sd = sdd
    #
    # smalle = scc - sdd
    # see = int(smalle * 10)
    # sff = int(see * 6)





























# 6-2-2-20
def decimaldiv622_Stem_018():
    stem = "$$수식$${boxone}$$/수식$$, $$수식$${boxtwo}$$/수식$$, $$수식$${boxthree}$$/수식$$, $$수식$${boxfour}$$/수식$$, $$수식$${boxfive}$$/수식$$, $$수식$${boxsix}$$/수식$$, $$수식$$6$$/수식$$장의 수 카드를 모두 한 번씩 사용하여 다음 나눗셈식을 만들려고 합니다. 만들 수 있는 나눗셈식 중에서 몫이 가장 클 때의 몫을 구해 보세요.\n$$표$$ $$수식$${boxseven}.{boxseven}{boxseven} DIV {boxseven}.{boxseven}{boxseven}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${spp}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa}````&gt;````{sbb}````&gt;````{scc}````&gt;````{sdd}````&gt;````{see}````&gt;````{sff}$$/수식$$\n" \
              "몫이 가장 크려면 나누어지는 수를 가장 크게, 나누는 수를 가장 작게 해야 합니다.\n" \
              "→ $$수식$${sgg} DIV {shh} = {smm} DIV {snn} = {spp}$$/수식$$\n\n"


    while True:
        num_list = random.sample(range(1, 10), 6)
        num_list.sort(reverse=True)

        saa = int(num_list[0])
        sbb = int(num_list[1])
        scc = int(num_list[2])
        sdd = int(num_list[3])
        see = int(num_list[4])
        sff = int(num_list[5])

        smm = (saa * 100) + (sbb * 10) + scc
        snn = (sff * 100) + (see * 10) + sdd

        if (smm % snn) == 0 or (smm * 10) % snn == 0 or (smm * 100) % snn == 0:
            break

    spp = round(smm / snn, 2)
    if spp - (spp // 1) == 0:
        spp = int(spp)

    sgg = round(smm / 100, 2)
    shh = round(snn / 100, 2)

    np.random.shuffle(num_list)

    boxone = "%d" % num_list[0]
    boxtwo = "%d" % num_list[1]
    boxthree = "%d" % num_list[2]
    boxfour = "%d" % num_list[3]
    boxfive = "%d" % num_list[4]
    boxsix = "%d" % num_list[5]

    boxseven = "□"


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, boxone=boxone, boxtwo=boxtwo,
                       boxthree=boxthree, boxfour=boxfour, boxfive=boxfive, boxsix=boxsix, boxseven=boxseven)
    answer = answer.format(spp=spp)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, spp=spp, smm=smm,
                             snn=snn)

    return stem, answer, comment
































# 6-2-2-22
def decimaldiv622_Stem_019():
    stem = "도로 한쪽에 가로등이 처음부터 끝까지 $$수식$${saa} rmm$$/수식$$ 간격으로 세워져 있습니다. 도로의 길이가 $$수식$${sbb} rmm$$/수식$$일 때, 도로 한쪽에 세워진 가로등은 모두 몇 개인지 구해 보세요. $$수식$$LEFT ($$/수식$$단, 가로등의 두께는 생각하지 않습니다.$$수식$$RIGHT )$$/수식$$\n"
    answer = "(정답)\n$$수식$${sff}$$/수식$$개\n"
    comment = "(해설)\n" \
              "도로에 가로등이 처음부터 끝까지 세워져 있으므로\n" \
              "$$수식$$LEFT ($$/수식$$도로 한쪽에 세워진 가로등 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$$도로의 길이$$수식$$RIGHT ) DIV LEFT ($$/수식$$가로등 사이의 간격$$수식$$RIGHT ) + 1$$/수식$$\n" \
              "$$수식$$= {sbb} DIV {saa} + 1 = {sdd} DIV {scc} + 1$$/수식$$\n" \
              "$$수식$$= {see} + 1 = {sff} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"


    while True:
        scc = np.random.randint(100, 1000)
        sdd = np.random.randint(1000, 10000)

        if (scc % 10) != 0:
            if ((sdd % 10) != 0) and ((sdd % scc) == 0):
                break

    skk = 0.1
    saa = round(scc * skk, 1)
    sbb = round(sdd * skk, 1)

    see = int(sbb / saa)
    sff = see + 1


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff)
    answer = answer.format(sff=sff)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff)

    return stem, answer, comment
































# 6-2-2-23
def decimaldiv622_Stem_020():
    stem = "빈칸에 알맞은 수를 써넣으세요.\n$$수식$${boxone}````{boxtwo}$$/수식$$ → $$수식$${box1}$$/수식$$ $$수식$${boxthree}$$/수식$$ → $$수식$${box2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$, $$수식$${sii}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {scc} DIV {sdd} = {see}$$/수식$$\n" \
              "$$수식$${see} DIV {sff} = {sgg} DIV {shh} = {sii}$$/수식$$\n\n"


    while True:
        sdd = np.random.randint(10, 100)
        scc = np.random.randint(100, 1000)
        see = scc / sdd

        if ((scc % 10) != 0) and (((scc * 10) % sdd) == 0):
            sgg = int(see * 100)
            shh = np.random.randint(100, 1000)

            if ((shh % 10) != 0) and ((sgg % shh) == 0):
                check_e = [i for i in str(see)]

                if int(check_e[len(check_e) - 1]) != 0:
                    break

    saa = scc / 100
    sbb = sdd / 100
    sff = shh / 100
    sii = int(sgg / shh)

    boxone = "%0.2f" % saa
    boxtwo = "`div`%s" % sbb
    boxthree = "`div`%0.2f" % sff
    box1 = "box{㉠````````````````````}"
    box2 = "box{㉡````````````````````}"


    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, box1=box1, box2=box2)
    answer = answer.format(see=see, sii=sii)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, sii=sii)

    return stem, answer, comment






























# 6-2-2-24
def decimaldiv622_Stem_021():
    stem = "□ 안에 알맞은 수를 써넣으세요.\n$$수식$${boxone} DIV {boxtwo}$$/수식$$ → $$수식$${boxblank}$$/수식$$\n"
    answer = "(정답)\n$$수식$${sgg}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {scc} DIV {sdd} = {sgg}$$/수식$$\n\n"


    while True:
        see = np.random.randint(10000, 100000)
        sdd = np.random.randint(100, 1000)
        if ((see % 10) != 0):
            if ((see % 10) != 0) and ((see % sdd) == 0):
                break

    scc = see / 10
    saa = round(scc / 100, 3)
    sbb = sdd / 100
    sgg = round(saa / sbb, 1)

    boxone = "%0.3f" % saa
    boxtwo = "%0.2f" % sbb
    boxblank = "box{　　　}"


    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxblank=boxblank)
    answer = answer.format(sgg=sgg)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sgg=sgg)

    return stem, answer, comment



































# 6-2-2-25
def decimaldiv622_Stem_022():
    stem = "큰 수를 작은 수로 나눈 몫을 구하시오.\n$$수식$${saa}$$/수식$$      $$수식$${sbb}$$/수식$$\n"
    answer = "(정답)\n$$수식$${spp}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sbb} &gt; {saa}$$/수식$$\n" \
              "→$$수식$${sbb} DIV {saa} = {sdd} DIV {scc} = {spp}$$/수식$$\n" \
              "또는 $$수식$${sbb} DIV {saa} = {sff} DIV {see} = {spp}$$/수식$$\n\n"


    while True:
        sff = np.random.randint(1000, 10000)
        see = np.random.randint(100, 1000)
        scc = int(see / 10)

        if (see % 10) == 0:
            if ((sff % 10) != 0) and ((sff % scc) == 0):
                break

    sdd = sff / 10
    saa = scc / 10
    sbb = round(sdd / 10, 2)

    smm = max(saa, sbb)
    snn = min(saa, sbb)
    spp = round(smm / snn, 1)


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(spp=spp)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, smm=smm, snn=snn, spp=spp)

    return stem, answer, comment

































# 6-2-2-26
def decimaldiv622_Stem_023():
    stem = "㉠과 ㉡의 몫의 합은 얼마인가요?\n$$표$$ ㉠ $$수식$${saa} DIV {sbb}$$/수식$$   ㉡ $$수식$${scc} DIV {sdd}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${spp}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${saa} DIV {sbb} = {see} DIV {sff} = {smm}$$/수식$$\n" \
              "㉡ $$수식$${scc} DIV {sdd} = {sgg} DIV {shh} = {snn}$$/수식$$\n" \
              "→ $$수식$$LEFT ($$/수식$$㉠과 ㉡의 몫의 합$$수식$$RIGHT ) ```` = {smm} + {snn} = {spp}$$/수식$$\n\n"


    while True:
        sii = np.random.randint(100, 1000)
        sjj = np.random.randint(11, 100)
        sff = int(sjj / 10)

        if (sjj % 10) == 0:
            if ((sii % 10) != 0) and ((sii % sff) == 0):
                break

    see = sii / 10
    saa = round(see / 10, 2)
    sbb = sff / 10


    while True:
        skk = np.random.randint(100, 1000)
        sll = np.random.randint(100, 1000)
        shh = int(sll / 10)

        if (sll % 10) == 0:
            if ((skk % 10) != 0) and ((skk % shh) == 0):
                break

    sgg = skk / 10
    scc = round(sgg / 10, 2)
    sdd = shh / 10

    smm = round(saa / sbb, 1)
    snn = round(scc / sdd, 1)
    spp = round(smm + snn, 1)

    if spp - (spp // 1) == 0:
        spp = int(spp)


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(spp=spp)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, sii=sii, sjj=sjj,
                             skk=skk, sll=sll, smm=smm, snn=snn, spp=spp)

    return stem, answer, comment


































# 6-2-2-27
def decimaldiv622_Stem_024():
    stem = "계산 결과를 비교하여 ○ 안에 $$수식$$ &gt; $$/수식$$, $$수식$$ = $$/수식$$, $$수식$$ &lt; $$/수식$$를 알맞게 써넣으세요.\n$$수식$${saa} DIV {sbb} $$/수식$$  ○  $$수식$${scc} DIV {sdd}$$/수식$$\n"
    answer = "(정답)\n$$수식$${sll}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {see} DIV {sff} = {sqq}$$/수식$$\n" \
              "$$수식$${scc} DIV {sdd} = {sgg} DIV {shh} = {srr}$$/수식$$\n" \
              "따라서 $$수식$${sqq}````{sll}````{srr}$$/수식$$\n\n"


    while True:
        while True:
            sii = np.random.randint(1000, 10000)
            sjj = np.random.randint(100, 1000)
            sff = int(sjj / 10)

            if (sjj % 10) == 0 and ((sii % 10) != 0) and ((sii % sff) == 0):
                break

        see = sii / 10
        saa = round(see / 10, 2)
        sbb = sff / 10
        sqq = round(saa / sbb, 1)


        while True:
            skk = np.random.randint(1000, 10000)
            sll = np.random.randint(100, 1000)
            shh = int(sll / 10)
            if (sll % 10) == 0 and ((skk % 10) != 0) and ((skk % shh) == 0):
                break

        sgg = skk / 10
        scc = round(sgg / 10, 2)
        sdd = shh / 10
        srr = round(scc / sdd, 1)

        if sii == skk or sjj == sll:
            continue
        else:
            break


    if sqq > srr:
        sll = "%s" % "&gt;"
    elif sqq == srr:
        sll = "%s" % "="
    else:
        sll = "%s" % "&lt;"


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(sll=sll)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, sii=sii, sjj=sjj,
                             skk=skk, sll=sll, sqq=sqq, srr=srr)

    return stem, answer, comment




































# 6-2-2-28
def decimaldiv622_Stem_025():
    stem = "계산 결과가 가장 큰 것을 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${saa} DIV {sbb}$$/수식$$\n㉡ $$수식$${shh} DIV {sii}$$/수식$$\n㉢ $$수식$${soo} DIV {spp}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${szz}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${saa} DIV {sbb} = {scc} DIV {sdd} = {see} DIV {sff} = {sgg}$$/수식$$\n" \
              "㉡ $$수식$${shh} DIV {sii} = {sjj} DIV {skk} = {sll} DIV {smm} = {snn}$$/수식$$\n" \
              "㉢ $$수식$${soo} DIV {spp} = {sqq} DIV {srr} = {sss} DIV {stt} = {suu}$$/수식$$\n" \
              "$$수식$${svv}`&gt;`{sww}`&gt;`{sxx}$$/수식$$이므로 계산 결과가 가장 큰 것은 $$수식$${szz}$$/수식$$입니다.\n\n"



    while True:
        while True:
            see = np.random.randint(1000, 10000)
            sff = np.random.randint(100, 1000)
            sdd = int(sff / 10)

            if (sff % 10) == 0 and ((see % 10) != 0) and ((see % sdd) == 0):
                break

        scc = see / 10
        saa = round(scc / 10, 2)
        sbb = sdd / 10
        sgg = round(saa / sbb, 1)

        while True:
            sll = np.random.randint(100, 1000)
            smm = np.random.randint(100, 1000)
            skk = int(smm / 10)

            if (smm % 10) == 0 and ((sll % 10) != 0) and ((sll % skk) == 0):
                break

        sjj = sll / 10
        shh = round(sjj / 10, 2)
        sii = skk / 10
        snn = round(shh / sii, 1)


        while True:
            sss = np.random.randint(100, 1000)
            stt = np.random.randint(100, 1000)
            srr = int(stt / 10)

            if (stt % 10) == 0 and ((sss % 10) != 0) and ((sss % srr) == 0):
                break

        sqq = sss / 10
        soo = round(sqq / 10, 2)
        spp = srr / 10
        suu = round(soo / spp, 1)


        a_list = [sgg, snn, suu]
        a_list.sort(reverse=True)

        svv = a_list[0]
        sww = a_list[1]
        sxx = a_list[2]

        if sgg != snn and sgg != suu and snn != suu:
            break


    if sgg == svv:
        szz = "㉠"
    elif snn == svv:
        szz = "㉡"
    else:
        szz = "㉢"


    stem = stem.format(saa=saa, sbb=sbb, shh=shh, sii=sii, soo=soo, spp=spp)
    answer = answer.format(szz=szz)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, sii=sii, sjj=sjj,
                             skk=skk, sll=sll, smm=smm, snn=snn, soo=soo, spp=spp, sqq=sqq, srr=srr, sss=sss, stt=stt,
                             suu=suu, svv=svv, sww=sww, sxx=sxx, szz=szz)

    return stem, answer, comment



































# 6-2-2-29
def decimaldiv622_Stem_026():
    stem = "㉠ $$수식$$DIV$$/수식$$ ㉡의 값은 얼마인가요?\n$$표$$ ㉠ $$수식$${saa}$$/수식$${rur1} $$수식$$1 over 1000$$/수식$$배 한 수\n㉡ $$수식$${sbb}$$/수식$${rur2} $$수식$$10$$/수식$$배 한 수$$/표$$\n"
    answer = "(정답)\n$$수식$${skk}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${saa}$$/수식$${rur1} $$수식$$1 over 1000$$/수식$$배 한 수 → $$수식$${scc}$$/수식$$\n" \
              "㉡ $$수식$${sbb}$$/수식$${rur2} $$수식$$10$$/수식$$배 한 수 → $$수식$${sdd}$$/수식$$\n" \
              "→ $$수식$$㉠ DIV ㉡ = {scc} DIV {sdd} = {see} DIV {sff} = {skk}$$/수식$$\n\n"


    while True:
        while True:
            saa = np.random.randint(100, 1000)
            smm = np.random.randint(10, 100)
            if ((saa % 10) != 0) and ((smm % 10) != 0):
                break

        sbb = smm / 1000
        see = saa / 10
        sff = int(sbb * 1000)
        scc = round(see / 100, 3)
        sdd = sff / 100

        if ((saa * 10) % sff) == 0:
            skk = round(scc / sdd, 2)
            break

    rur1 = josa(saa, "를")
    rur2 = josa(sbb, "를")


    stem = stem.format(saa=saa, sbb=sbb, rur1=rur1, rur2=rur2)
    answer = answer.format(skk=skk)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, skk=skk, rur1=rur1, rur2=rur2)

    return stem, answer, comment






































# 6-2-2-31
def decimaldiv622_Stem_027():
    stem = "지석이는 자전거를 타고 $$수식$${saa}$$/수식$$시간 동안 $$수식$${sbb} rm {{km}}$$/수식$$를 갔습니다. 지석이가 일정한 빠르기로 갔다면 $$수식$$1$$/수식$$시간 동안 간 거리는 몇 $$수식$$rm m$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${sdd} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1$$/수식$$시간 동안 간 거리$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$$간 거리$$수식$$RIGHT ) DIV LEFT ($$/수식$$자전거를 탄 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {sbb} DIV {saa} = {scc} LEFT ( rm {{km}} RIGHT )$$/수식$$\n" \
              "$$수식$${scc} rm {{km}} = {sdd} rm m$$/수식$$이므로\n" \
              "지석이가 $$수식$$1$$/수식$$시간 동안 간 거리는 $$수식$${sdd} rm m$$/수식$$입니다.\n\n"


    while True:
        smm = np.random.randint(10000, 100000)
        snn = np.random.randint(10, 100)

        if (snn % 10) != 0:
            if ((smm % 10) != 0) and ((smm % snn) == 0):
                break

    sbb = round(smm / 1000, 3)
    saa = round(snn / 10, 1)
    scc = round(sbb / saa, 2)
    sdd = int(scc * 1000)


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(sdd=sdd)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)

    return stem, answer, comment




































# 6-2-2-32
def decimaldiv622_Stem_028():
    stem = "□ 안에 들어갈 수 있는 자연수는 모두 몇 개인가요?\n$$표$$ □ $$수식$$&lt;`{saa} DIV {sbb}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${snn}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {scc} DIV {sdd} = {see}$$/수식$$\n" \
              "→ □ $$수식$$&lt;`{see}$$/수식$$에서 □ 안에 들어갈 수 있는 자연수는 " \
              "$$수식$$1$$/수식$$부터 $$수식$${sff}$$/수식$$까지 모두 $$수식$${snn}$$/수식$$개입니다.\n\n"


    while True:
        scc = np.random.randint(100, 1000)
        sdd = np.random.randint(11, 100)

        if (sdd % 10) == 0:
            if ((scc % 10) != 0) and (scc % (sdd / 10) == 0):
                break

    saa = scc / 100
    sbb = sdd / 100
    see = round(saa / sbb, 1)

    f_list = []

    for i in range(1, int(see + 1)):
        if i < see:
            f_list.append(i)

    f_list.sort(reverse=True)
    sff = f_list[0]
    snn = len(f_list)


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(snn=snn)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, snn=snn)

    return stem, answer, comment
































# 6-2-2-33
def decimaldiv622_Stem_029():
    stem = "휘발유 $$수식$${saa} rm L$$/수식$$로 $$수식$${sbb} rm {{km}}$$/수식$$를 갈 수 있는 자동차가 있습니다. 휘발유 $$수식$$1 rm L$$/수식$$의 값이 $$수식$${scc}$$/수식$$원이라면 이 자동차가 $$수식$${sdd} rm {{km}}$$/수식$$를 가는 데 필요한 휘발유의 값은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${sgg}$$/수식$$원\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$휘발유 $$수식$$1 rm L$$/수식$$로 갈 수 있는 거리$$수식$$RIGHT )$$/수식$$\n$$수식$$= LEFT ($$/수식$$거리$$수식$$RIGHT ) DIV LEFT ($$/수식$$휘발유의 " \
              "양$$수식$$RIGHT )$$/수식$$\n$$수식$$= {sbb} DIV {saa} = {see} LEFT ( rm {{km}} RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ( {sdd} rm {{km}}$$/수식$$를 가는 데 필요한 휘발유의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$$전체 거리$$수식$$RIGHT ) DIV LEFT ($$/수식$$휘발유 $$수식$$1 rm L$$/수식$$로 갈 수 있는 " \
              "거리$$수식$$RIGHT )$$/수식$$\n$$수식$$= {sdd} DIV {see} = {sff} LEFT ( rm L RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ( {sdd} rm {{km}}$$/수식$$를 가는 데 필요한 휘발유의 값$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ( {sdd} rm {{km}}$$/수식$$를 가는 데 필요한 휘발유의 양$$수식$$RIGHT ) TIMES LEFT ($$/수식$$휘발유 $$수식$$1 rm L$$/수식$$의 " \
              "값$$수식$$RIGHT )$$/수식$$\n$$수식$$= {sff} TIMES {scc} = {sgg} LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$\n\n"



    while True:
        snn = np.random.randint(10, 100)
        smm = snn * (np.random.randint(10, 101))

        sbb = round(smm / 100, 2)
        saa = round(snn / 10, 1)

        see = round(sbb / saa, 2)

        shh = np.random.randint(1000, 10000)

        sdd = round(shh / 10, 5)

        sff = round(sdd / see, 5)

        scc = np.random.randint(1000, 2000)

        sgg = round(sff * scc, 2)
        if sgg - (sgg // 1) == 0:
            sgg = int(sgg)

        if snn % 10 != 0 and smm % 10 != 0 and 1000 <= smm and smm < 10000:
            if shh % 10 != 0 and (shh * 10) % see == 0:
                if scc % 10 == 0:
                    break


    # while True:
    #     smm = np.random.randint(1000, 10000)
    #     snn = np.random.randint(10, 100)
    #
    #     if (snn % 10) != 0:
    #         if ((smm % 10) != 0) and ((smm % snn) == 0):
    #             sbb = smm / 100
    #             saa = snn / 10
    #             see = sbb / saa
    #             shh = np.random.randint(1000, 10000)
    #             scc = np.random.randint(1000, 2000)
    #
    #             if ((shh % 10) != 0) and (((shh * 10) % see) == 0):
    #                 if (scc % 10) == 0:
    #                     break
    #
    # sdd = shh / 10
    # sff = round(sdd / see, 1)
    # sgg = int(sff * scc)


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(sgg=sgg)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, smm=smm, snn=snn)

    return stem, answer, comment





































# 6-2-2-34
def decimaldiv622_Stem_030():
    stem = "윗변의 길이가 $$수식$${saa} rm m$$/수식$$, 아랫변의 길이가 $$수식$${sbb} rm m$$/수식$$인 사다리꼴이 있습니다. 이 사다리꼴의 넓이가 $$수식$${scc} rm m^2$$/수식$$일 때, 높이는 몇 $$수식$$rm m$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${sff} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$사다리꼴의 넓이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ( LEFT ( $$/수식$$윗변의 길이$$수식$$RIGHT ) + LEFT ($$/수식$$아랫변의 " \
              "길이$$수식$$RIGHT ) RIGHT ) TIMES LEFT ($$/수식$$높이$$수식$$RIGHT ) DIV 2$$/수식$$\n" \
              "→ $$수식$$LEFT ($$/수식$$높이$$수식$$RIGHT ) = LEFT ($$/수식$$사다리꼴의 넓이$$수식$$RIGHT ) TIMES 2 $$/수식$$\n$$수식$$ DIV LEFT ( LEFT ($$/수식$$윗변의 " \
              "길이$$수식$$RIGHT ) + LEFT ($$/수식$$아랫변의 길이$$수식$$RIGHT ) RIGHT )$$/수식$$\n" \
              "$$수식$$= {scc} TIMES 2 DIV LEFT ( {saa} + {sbb} RIGHT )$$/수식$$\n" \
              "$$수식$$= {scc} TIMES 2 DIV {sdd}$$/수식$$\n" \
              "$$수식$$= {see} DIV {sdd} = {sff} LEFT ( rm m RIGHT )$$/수식$$\n\n"



    while True:
        while True:
            sgg = np.random.randint(10, 100)
            shh = np.random.randint(10, 100)
            if ((shh % 10) != 0) and ((sgg % 10) != 0):
                break

        saa = sgg / 10
        sbb = shh / 10
        sdd = round(saa + sbb, 1)

        sii = np.random.randint(100, 1000)

        if ((sii % 10) != 0) and (((sii * 10) % (sdd * 10)) == 0):
            scc = sii / 10
            see = 2 * scc
            break


    sff = round(see / sdd, 1)
    check_f = [i for i in str(sff)]

    if (len(check_f) == 3) and (check_f[2] == "0"):
        sff = int(sff)
    elif (len(check_f) == 4) and (check_f[3] == "0"):
        sff = int(sff)
    else:
        sff = sff


    stem = stem.format(saa=saa, sbb=sbb, scc=scc)
    answer = answer.format(sff=sff)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, sii=sii)

    return stem, answer, comment



































# 6-2-2-35
def decimaldiv622_Stem_031():
    stem = "빈칸에 알맞은 수를 써넣으세요.\n$$수식$${boxone} DIV {sbb}$$/수식$$ → $$수식$${boxblank}$$/수식$$\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {scc} DIV {sdd} = {see}$$/수식$$\n\n"


    while True:
        sdd = np.random.randint(10, 100)
        scc = np.random.randint(100, 1000)
        if (sdd % 10) != 0:
            if ((scc % 10) == 0) and ((scc % sdd) == 0):
                break

    saa = int(scc / 10)
    sbb = round(sdd / 10, 1)
    see = int(saa / sbb)

    boxone = "%d" % saa
    boxblank = "box{　　　}"


    stem = stem.format(sbb=sbb, boxone=boxone, boxblank=boxblank)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see)

    return stem, answer, comment



































# 6-2-2-36
def decimaldiv622_Stem_032():
    stem = "자연수를 소수로 나누어 빈칸에 알맞은 수를 써넣으세요.\n$$수식$${boxone}````{boxtwo}````$$/수식$$ $$수식$${boxblank}$$/수식$$\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "자연수는 $$수식$${saa}$$/수식$$, 소수는 $$수식$${sbb}$$/수식$$\n" \
              "→ $$수식$${saa} DIV {sbb} = {scc} DIV {sdd} = {see}$$/수식$$\n\n"


    # while True:
    #     sdd = np.random.randint(100, 1000)
    #     scc = np.random.randint(1000, 10000)
    #
    #     if (sdd % 10) != 0:
    #         if ((scc % 100) == 0) and ((scc % sdd) == 0):
    #             break

    while True:
        sdd = np.random.randint(1, 10) + (np.random.randint(10, 100)) * 10
        scc = 100 * (np.random.randint(10, 100))
        if scc % sdd == 0:
            break


    saa = int(scc / 100)
    sbb = round(sdd / 100, 2)
    see = int(saa / sbb)


    box_list = [saa, sbb]
    np.random.shuffle(box_list)

    if box_list[0] == saa:
        boxone = "%d" % box_list[0]
        boxtwo = "%0.2f" % box_list[1]

    else:
        boxone = "%0.2f" % box_list[0]
        boxtwo = "%d" % box_list[1]

    boxblank = "box{　　　}"


    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxblank=boxblank)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see)

    return stem, answer, comment






































# 6-2-2-37
def decimaldiv622_Stem_033():
    stem = "□ 안에 알맞은 수를 써넣으세요.\n$$수식$${saa}$$/수식$$ $$수식$$DIV {sbb}$$/수식$$ → $$수식$${boxblank}$$/수식$$\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {scc} DIV {sdd} = {see}$$/수식$$\n\n"


    while True:
        sdd = np.random.randint(10, 100)
        scc = np.random.randint(100, 1000)
        if (sdd % 10) != 0:
            if ((scc % 10) == 0) and ((scc % sdd) == 0):
                break

    saa = int(scc / 10)
    sbb = sdd / 10
    see = int(saa / sbb)

    boxblank = "box{　　　}"


    stem = stem.format(saa=saa, sbb=sbb, boxblank=boxblank)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see)

    return stem, answer, comment







































# 6-2-2-38
def decimaldiv622_Stem_034():
    stem = "계산 결과가 큰 것부터 차례대로 기호를 써 보세요.\n$$표$$㉠ $$수식$${sa1} DIV {sa2}$$/수식$$   ㉡ $$수식$${sb1} DIV {sb2}$$/수식$$\n㉢ $$수식$${sc1} DIV {sc2}$$/수식$$   ㉣ $$수식$${sd1} DIV {sd2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{a1}, {a2}, {a3}, {a4}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${sa1} DIV {sa2} = {sa3} DIV {sa4} = {sa5}$$/수식$$\n" \
              "㉡ $$수식$${sb1} DIV {sb2} = {sb3} DIV {sb4} = {sb5}$$/수식$$\n" \
              "㉢ $$수식$${sc1} DIV {sc2} = {sc3} DIV {sc4} = {sc5}$$/수식$$\n" \
              "㉣ $$수식$${sd1} DIV {sd2} = {sd3} DIV {sd4} = {sd5}$$/수식$$\n\n"

    while True:
        # while True:
        #     sdd = np.random.randint(10, 100)
        #     scc = np.random.randint(1000, 10000)
        #     if (sdd % 10) != 0:
        #         if ((scc % 10) == 0) and ((scc % sdd) == 0):
        #             break
        # while True:
        #     sii = np.random.randint(10, 100)
        #     shh = np.random.randint(1000, 10000)
        #     if (sii % 10) != 0:
        #         if ((shh % 10) == 0) and ((shh % sii) == 0):
        #             break
        # while True:
        #     snn = np.random.randint(100, 1000)
        #     smm = np.random.randint(1000, 10000)
        #     if (snn % 10) != 0:
        #         if ((smm % 100) == 0) and ((smm % snn) == 0):
        #             break
        # while True:
        #     sss = np.random.randint(100, 1000)
        #     srr = np.random.randint(1000, 10000)
        #     if (sss % 10) != 0:
        #         if ((srr % 100) == 0) and ((srr % sss) == 0):
        #             break

        while True:
            sdd = np.random.randint(1, 10) + (np.random.randint(1, 10)) * 10
            scc = 10 * (np.random.randint(100, 1000))

            if scc % sdd == 0:
                break

        while True:
            sii = np.random.randint(1, 10) + (np.random.randint(1, 10)) * 10
            shh = 10 * (np.random.randint(100, 1000))

            if shh % sii == 0:
                break

        while True:
            snn = np.random.randint(1, 10) + (np.random.randint(10, 100)) *10
            smm = 100 * (np.random.randint(10, 100))

            if smm % snn == 0:
                break

        while True:
            sss = np.random.randint(1, 10) + (np.random.randint(10, 100)) * 10
            srr = 100 * (np.random.randint(10, 100))

            if srr % sss == 0:
                break

        if scc == shh or sdd == sii or smm == srr or snn == sss:
            continue


        saa = int(scc / 10)
        sbb = round(sdd / 10, 1)
        sff = int(shh / 10)
        sgg = round(sii / 10, 1)
        skk = int(smm / 100)
        sll = round(snn / 100, 2)
        spp = int(srr / 100)
        sqq = round(sss / 100, 2)

        see = int(saa / sbb)
        sjj = int(sff / sgg)
        soo = int(skk / sll)
        stt = int(spp / sqq)

        pre_list = [saa, sff, skk, spp]
        post_list = [sbb, sgg, sll, sqq]
        midpre_list = [scc, shh, smm, srr]
        midpost_list = [sdd, sii, snn, sss]
        answer_list = [see, sjj, soo, stt]

        if see != sjj != soo != stt:
            num_list = [0, 1, 2, 3]
            np.random.shuffle(num_list)
            sa1 = pre_list[num_list[0]]
            sb1 = pre_list[num_list[1]]
            sc1 = pre_list[num_list[2]]
            sd1 = pre_list[num_list[3]]

            sa2 = post_list[num_list[0]]
            sb2 = post_list[num_list[1]]
            sc2 = post_list[num_list[2]]
            sd2 = post_list[num_list[3]]

            sa3 = midpre_list[num_list[0]]
            sb3 = midpre_list[num_list[1]]
            sc3 = midpre_list[num_list[2]]
            sd3 = midpre_list[num_list[3]]

            sa4 = midpost_list[num_list[0]]
            sb4 = midpost_list[num_list[1]]
            sc4 = midpost_list[num_list[2]]
            sd4 = midpost_list[num_list[3]]

            sa5 = answer_list[num_list[0]]
            sb5 = answer_list[num_list[1]]
            sc5 = answer_list[num_list[2]]
            sd5 = answer_list[num_list[3]]

            maxmin_list = [see, sjj, soo, stt]
            maxmin_list.sort(reverse=True)

            a1 = ""
            a2 = ""
            a3 = ""
            a4 = ""


            for i in range(0, len(answer_list)):
                if maxmin_list[0] == answer_list[num_list[i]]:
                    smalla1 = answer_list[num_list[i]]
                    if smalla1 == sa5:
                        a1 = "㉠"
                    elif smalla1 == sb5:
                        a1 = "㉡"
                    elif smalla1 == sc5:
                        a1 = "㉢"
                    else:
                        a1 = "㉣"
                elif maxmin_list[1] == answer_list[num_list[i]]:
                    smalla2 = answer_list[num_list[i]]
                    if smalla2 == sa5:
                        a2 = "㉠"
                    elif smalla2 == sb5:
                        a2 = "㉡"
                    elif smalla2 == sc5:
                        a2 = "㉢"
                    else:
                        a2 = "㉣"
                elif maxmin_list[2] == answer_list[num_list[i]]:
                    smalla3 = answer_list[num_list[i]]
                    if smalla3 == sa5:
                        a3 = "㉠"
                    elif smalla3 == sb5:
                        a3 = "㉡"
                    elif smalla3 == sc5:
                        a3 = "㉢"
                    else:
                        a3 = "㉣"
                elif maxmin_list[3] == answer_list[num_list[i]]:
                    smalla4 = answer_list[num_list[i]]
                    if smalla4 == sa5:
                        a4 = "㉠"
                    elif smalla4 == sb5:
                        a4 = "㉡"
                    elif smalla4 == sc5:
                        a4 = "㉢"
                    else:
                        a4 = "㉣"
            break



    stem = stem.format(sa1=sa1, sa2=sa2, sb1=sb1, sb2=sb2, sc1=sc1, sc2=sc2, sd1=sd1, sd2=sd2)
    answer = answer.format(a1=a1, a2=a2, a3=a3, a4=a4)
    comment = comment.format(sa1=sa1, sa2=sa2, sa3=sa3, sa4=sa4, sa5=sa5, sb1=sb1, sb2=sb2, sb3=sb3, sb4=sb4, sb5=sb5,
                             sc1=sc1, sc2=sc2, sc3=sc3, sc4=sc4, sc5=sc5, sd1=sd1, sd2=sd2, sd3=sd3, sd4=sd4, sd5=sd5)

    return stem, answer, comment

































# 6-2-2-39
def decimaldiv622_Stem_035():
    stem = "계산 결과를 비교하여 ○ 안에 $$수식$$ &gt; $$/수식$$, $$수식$$ = $$/수식$$, $$수식$$ &lt; $$/수식$$를 알맞게 써넣으세요.\n$$수식$${saa} DIV {sbb}$$/수식$$  ○  $$수식$${scc} DIV {sdd}$$/수식$$\n"
    answer = "(정답)\n$$수식$${sll}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {see} DIV {sff} = {sii}$$/수식$$\n" \
              "$$수식$${scc} DIV {sdd} = {sgg} DIV {shh} = {sjj}$$/수식$$\n" \
              "$$수식$${smm} {big_left} {snn}$$/수식$$이므로 $$수식$${saa} DIV {sbb} {sll} {scc} DIV {sdd}$$/수식$$입니다\n\n"


    # while True:
    #     sff = np.random.randint(10, 100)
    #     see = np.random.randint(1000, 10000)
    #     if (sff % 10) != 0:
    #         if ((see % 10) == 0) and ((see % sff) == 0):
    #             break
    #
    # saa = int(see / 10)
    # sbb = sff / 10
    # sii = int(saa / sbb)
    #
    # while True:
    #     shh = np.random.randint(10, 100)
    #     sgg = np.random.randint(1000, 10000)
    #
    #     if (shh % 10) != 0:
    #         if ((sgg % 10) == 0) and ((sgg % shh) == 0):
    #             break
    #
    # scc = int(sgg / 10)
    # sdd = shh / 10
    # sjj = int(scc / sdd)


    while True:
        while True:
            sff = np.random.randint(10, 100)
            see = np.random.randint(1000, 10000)
            if (sff % 10) != 0 and ((see % 10) == 0) and ((see % sff) == 0):
                break

        saa = int(see / 10)
        sbb = sff / 10
        sii = int(saa / sbb)

        while True:
            shh = np.random.randint(10, 100)
            sgg = np.random.randint(1000, 10000)

            if (shh % 10) != 0 and ((sgg % 10) == 0) and ((sgg % shh) == 0):
                break

        scc = int(sgg / 10)
        sdd = shh / 10
        sjj = int(scc / sdd)

        if see == sgg or sff == shh:
            continue
        else:
            break


    smm = max(sii, sjj)
    snn = min(sii, sjj)

    big_left = "&gt;"

    if sii > sjj:
        sll = "&gt;"
    elif sii < sjj:
        sll = "&lt;"
    else:
        sll = "="
        big_left = "="



    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(sll=sll)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, smm=smm, snn=snn,
                             sii=sii, sjj=sjj, sll=sll, big_left=big_left)

    return stem, answer, comment











































# 6-2-2-41
def decimaldiv622_Stem_036():
    stem = "길이가 $$수식$${saa} rm m$$/수식$$인 끈을 $$수식$${sbb} rm m$$/수식$$씩 모두 자르려고 합니다. 몇 번을 자르면 되는지 구해 보세요. $$수식$$LEFT ($$/수식$$단, 겹쳐서 자르는 것을 생각하지 않습니다.$$수식$$RIGHT )$$/수식$$\n"
    answer = "(정답)\n$$수식$${sff}$$/수식$$번\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$도막 수$$수식$$RIGHT ) = {saa} DIV {sbb} = {see} LEFT ($$/수식$$도막$$수식$$RIGHT )$$/수식$$\n" \
              "→ $$수식$$LEFT ($$/수식$$자르는 횟수$$수식$$RIGHT ) = {see} - 1 = {sff} LEFT ($$/수식$$번$$수식$$RIGHT )$$/수식$$\n\n"


    # while True:
    #     sdd = np.random.randint(100, 1000)
    #     scc = np.random.randint(1000, 10000)
    #     if (sdd % 10) != 0:
    #         if ((scc % 100) == 0) and ((scc % sdd) == 0):
    #             break

    while True:
        sdd = np.random.randint(1, 10) + (np.random.randint(10, 100)) * 10
        scc = 100 * (np.random.randint(10, 100))
        if scc % sdd == 0:
            break

    saa = int(scc / 100)
    sbb = round(sdd / 100, 2)
    see = int(saa / sbb)
    sff = see - 1


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(sff=sff)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff)

    return stem, answer, comment







































# 6-2-2-42
def decimaldiv622_Stem_037():
    stem = "길이가 $$수식$${saa} rm m$$/수식$$인 원 모양의 공원 둘레에 $$수식$${sbb} rm m$$/수식$$ 간격으로 가로등을 세우려고 합니다. 필요한 가로등은 몇 개인가요? $$수식$$LEFT ($$/수식$$단, 가로등의 두께는 생각하지 않습니다.$$수식$$RIGHT )$$/수식$$\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$가로등 사이의 간격 수$$수식$$RIGHT ) = {saa} DIV {sbb} = {see} LEFT ($$/수식$$군데$$수식$$RIGHT )$$/수식$$\n" \
              "→ 필요한 가로등 수는 가로등 사이의 간격 수와 같으므로 $$수식$${see}$$/수식$$개입니다.\n\n"


    # while True:
    #     sdd = np.random.randint(100, 1000)
    #     scc = np.random.randint(1000, 10000)
    #     if (sdd % 10) != 0:
    #         if ((scc % 100) == 0) and ((scc % sdd) == 0):
    #             break

    while True:
        sdd = np.random.randint(1, 10) + (np.random.randint(10, 100)) * 10
        scc = 10 * (np.random.randint(100, 1000))
        if scc % sdd == 0:
            break

    saa = int(scc / 10)
    sbb = round(sdd / 10, 2)
    see = int(saa / sbb)


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see)

    return stem, answer, comment




































# 6-2-2-43
def decimaldiv622_Stem_038():
    stem = "㉠은 ㉡의 몇 배인가요?\n$$표$$ ㉠ $$수식$$0.01$$/수식$$이 $$수식$${saa}$$/수식$$개인 수\n㉡ $$수식$$1$$/수식$$이 $$수식$${sbb}$$/수식$$개, $$수식$$0.1$$/수식$$이 $$수식$${scc}$$/수식$$개, $$수식$$0.01$$/수식$$이 $$수식$${sdd}$$/수식$$개인 수 $$/표$$\n"
    answer = "(정답)\n$$수식$${sgg}$$/수식$$배\n"
    comment = "(해설)\n" \
              "㉠ $$수식$$0.01$$/수식$$이 $$수식$${saa}$$/수식$$개인 수 : $$수식$${see}$$/수식$$\n" \
              "㉡ $$수식$$1$$/수식$$이 $$수식$${sbb}$$/수식$$개, $$수식$$0.1$$/수식$$이 $$수식$${scc}$$/수식$$개, " \
              "$$수식$$0.01$$/수식$$이 $$수식$${sdd}$$/수식$$개인 수 : $$수식$${sff}$$/수식$$\n" \
              "→ ㉠ $$수식$$DIV$$/수식$$ ㉡ $$수식$$= {see} DIV {sff} = {sgg} LEFT ($$/수식$$배$$수식$$RIGHT )$$/수식$$\n\n"


    while True:
        num_list = random.sample(range(1, 10), 3)
        sbb = num_list[0]
        scc = num_list[1]
        sdd = num_list[2]

        smm = (sbb * 100) + (scc * 10) + sdd

        # saa = np.random.randint(1000, 10000)
        # if ((saa % 100) == 0) and ((saa % smm) == 0):
        #     break

        saa = 100 * (np.random.randint(10, 100))
        if saa % smm == 0:
            break


    see = int(saa / 100)
    sff = round(smm / 100, 2)
    sgg = int(see / sff)


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(sgg=sgg)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, smm=smm)

    return stem, answer, comment



































# 6-2-2-44
def decimaldiv622_Stem_039():
    stem = "길이가 $$수식$${saa} rm m$$/수식$$인 자전거 도로의 한쪽에 $$수식$${sbb} rm m$$/수식$$ 간격으로 의자를 설치하려고 합니다. 길이가 $$수식$${scc} rm m$$/수식$$인 의자를 도로의 처음부터 끝까지 설치한다면 의자는 모두 몇 개가 필요한가요?\n"
    answer = "(정답)\n$$수식$${sgg}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$의자를 설치한 간격$$수식$$RIGHT ) + LEFT ($$/수식$$의자의 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {sbb} + {scc} = {sdd} LEFT ( rm m RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$도로의 전체 길이$$수식$$RIGHT ) - LEFT ($$/수식$$의자 한 개의 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {saa} - {scc} = {see} LEFT ( rm m RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$필요한 의자 수$$수식$$RIGHT ) = {see} DIV {sdd} + 1 = {sff} + 1 = {sgg} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"



    while True:
        sdd = round((np.random.randint(1, 10) + (np.random.randint(100, 1000)) * 10) / 100, 2)
        see = np.random.randint(100, 1000)

        sff = int(see / sdd)
        sgg = sff + 1

        scc = np.random.randint(2, 10)

        saa = see + scc

        sbb = sdd - scc

        if see % sdd == 0 and sbb < 100:
            break


    # while True:
    #     snn = np.random.randint(1000, 10000)
    #     smm = np.random.randint(10000, 100000)
    #
    #     if (snn % 10) == 0:
    #         if ((smm % 100) == 0) and ((smm % snn) == 0):
    #             break
    #
    # sdd = snn / 10
    # see = smm / 100
    # sff = see / sdd
    #
    # while True:
    #     saa = np.random.randint(100, 1000)
    #     if (saa % 10) != 0:
    #         break
    #
    # while True:
    #     sqq = np.random.randint(1000, 10000)
    #     if (sqq % 10) != 0:
    #         break
    #
    # scc = np.random.randint(2, 10)
    #
    # sbb = round(sqq / 100, 2)
    # sdd = sbb + scc
    # see = saa - scc
    # sgg = sff + 1


    stem = stem.format(saa=saa, sbb=sbb, scc=scc)
    answer = answer.format(sgg=sgg)
    # comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, smm=smm, snn=snn, sqq=sqq)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg)

    return stem, answer, comment





































# 6-2-2-45
def decimaldiv622_Stem_040():
    stem = "어떤 수를 $$수식$${saa}$$/수식$${ro1} 나누어야 할 것을 잘못하여 곱하였더니 $$수식$${sbb}$$/수식$${ga1} 되었습니다. 바르게 계산한 값과 잘못 계산한 값의 차를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □ 라고 하여 잘못 계산한 식을 세우면 \n" \
              "□$$수식$$ TIMES {saa} = {sbb}$$/수식$$ → □$$수식$$ = {sbb} DIV {saa} = {scc}$$/수식$$\n" \
              "어떤 수는 $$수식$${scc}$$/수식$$이므로\n" \
              "바르게 계산하면 $$수식$${scc} DIV {saa} = {sdd}$$/수식$$ 입니다.\n" \
              "또한 $$수식$${smm} &gt; {snn}$$/수식$$이므로\n" \
              "바르게 계산한 값과 잘못 계산한 값의 차는 $$수식$${smm} - {snn} = {see}$$/수식$$입니다.\n\n"


    # while True:
    #     smm = np.random.randint(10, 100)
    #     if (smm % 10) == 0:
    #         break
    #
    # sbb = np.random.randint(2, 10)
    # saa = smm / 100
    #
    # scc = int(sbb / saa)
    # sdd = int(scc / saa)


    while True:
        saa = round((np.random.randint(1, 10)) * 0.1, 1)
        sbb = np.random.randint(2, 10)

        scc = round(sbb / saa, 10)
        if scc - (scc // 1) == 0:
            scc = int(scc)

        sdd = round(scc / saa, 10)
        if sdd - (sdd // 1) == 0:
            sdd = int(sdd)


        if sdd == int(sdd):
            break


    smm = max(sdd, sbb)
    snn = min(sdd, sbb)
    see = int(smm - snn)

    ro1 = josa(saa, "로")
    ga1 = josa(sbb, "가")


    stem = stem.format(saa=saa, sbb=sbb, ro1=ro1, ga1=ga1)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, smm=smm, snn=snn)

    return stem, answer, comment








































# 6-2-2-47
def decimaldiv622_Stem_041():
    stem = "계산 결과를 비교하여 ○ 안에 $$수식$$ &gt; $$/수식$$, $$수식$$` = `$$/수식$$, $$수식$$ &lt; $$/수식$$를 알맞게 써넣으세요\n$$수식$${box1}$$/수식$$  ○  {box2}\n"
    answer = "(정답)\n$$수식$${sll}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {c}.{a} CDOTS CDOTS$$/수식$${ro1}\n" \
              "몫의 소수 첫째 자리 숫자가 $$수식$${a}$$/수식$$이므로 {snn}합니다.\n" \
              "따라서 $$수식$${saa} DIV {sbb}$$/수식$$의 몫을 반올림하여 자연수로 나타낸 수는 $$수식$${saa} DIV {sbb}$$/수식$$보다 {spp}\n\n"


    while True:
        sff = np.random.randint(31, 100)
        if (sff % 9) != 0:
            break

    saa = int(sff / np.gcd(sff, 9))
    sbb = int(9 / np.gcd(sff, 9))
    c = int(saa / sbb)
    smalla = (saa / sbb) - c
    check_a = [i for i in str(smalla)]
    a = int(check_a[2])


    if a >= 5:
        snn = "올림"
        spp = "큽니다."
        sll = "&lt;"

    else:
        snn = "내림"
        spp = "작습니다."
        sll = "&gt;"


    box1 = "%s`div`%s" % (saa, sbb)
    box2 = "$$수식$$%s`div`%s$$/수식$$ 의 몫을 반올림하여 자연수로 나타낸 수" % (saa, sbb)

    ro1 = josa(a, "로")


    stem = stem.format(box1=box1, box2=box2)
    answer = answer.format(sll=sll)
    comment = comment.format(saa=saa, sbb=sbb, a=a, c=c, snn=snn, spp=spp, ro1=ro1)

    return stem, answer, comment




































# 6-2-2-48
def decimaldiv622_Stem_042():
    stem = "몫을 반올림하여 소수 둘째 자리까지 나타내어 보세요.\n$$표$$ $$수식$${saa} DIV {sbb}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${c}.{a}{d}$$/수식$$\n"
    comment = "(해설)\n" \
              "몫을 소수 셋째 자리까지 구한 후 소수 셋째 자리에서 반올림하면\n" \
              "$$수식$${saa} DIV {sbb} = {c}.{a}{b}{b} CDOTS CDOTS$$/수식$$ → $$수식$${c}.{a}{d}$$/수식$$\n\n"



    while True:
        saa = round(np.random.randint(10, 100) + (np.random.randint(1, 10)) * 0.1, 1)
        sbb = np.random.randint(2, 10)

        div_ab = saa / sbb
        str_div_ab = str(round(div_ab, 10))

        if len(str_div_ab) < 8:
            continue

        if div_ab >= 10:
            if str_div_ab[3] == str_div_ab[4]:
                continue
            elif str_div_ab[4] != str_div_ab[5]:
                continue
            elif str_div_ab[5] != str_div_ab[6]:
                continue

        else:
            if str_div_ab[2] == str_div_ab[3]:
                continue
            elif str_div_ab[3] != str_div_ab[4]:
                continue
            elif str_div_ab[4] != str_div_ab[5]:
                continue

        if div_ab >= 10:
            c = int(str_div_ab[0]) * 10 + int(str_div_ab[1])
            a = int(str_div_ab[3])
            b = int(str_div_ab[4])
            if b == 9:
                continue
            break

        else:
            c = int(str_div_ab[0])
            a = int(str_div_ab[2])
            b = int(str_div_ab[3])
            if b == 9:
                continue
            break


    if b >= 5:
        d = b + 1
    else:
        d = b


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(c=c, a=a, d=d)
    comment = comment.format(saa=saa, sbb=sbb, a=a, b=b, c=c, d=d)

    return stem, answer, comment



    # while True:
    #     sff = np.random.randint(100, 1000)
    #     if (sff % 9) != 0:
    #         break
    #
    # smm = sff / np.gcd(sff, 9)
    # saa = smm / 10
    # sbb = sff / np.gcd(sff, 9)
    #
    # c = int(saa / sbb)
    # smallab = (saa / sbb) - c
    # check_ab = [i for i in str(smallab)]
    #
    # if len(check_ab) == 3:
    #     a = int(check_ab[2])
    #     b = 0
    #
    # elif len(check_ab) > 3:
    #     a = int(check_ab[2])
    #     b = int(check_ab[3])
    #
    #
    # if b >= 5:
    #     d = b + 1
    # else:
    #     d = b






































# 6-2-2-49
def decimaldiv622_Stem_043():
    stem = "몫을 반올림하여 소수 첫째 자리까지 구한 값과 소수 둘째 자리까지 구한 값의 차를 구해 보세요.\n$$표$$ $$수식$${saa} DIV {sbb}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${sqq}$$/수식$$\n"
    comment = "(해설)\n" \
              "· 몫을 소수 둘째 자리까지 구한 후 소수 둘째 자리에서 반올림하면\n" \
              "$$수식$${saa} DIV {sbb} = {c}.{a}{a} CDOTS CDOTS$$/수식$$ → $$수식$${smm}$$/수식$$\n" \
              "· 몫을 소수 셋째 자리까지 구한 후 소수 셋째 자리에서 반올림하면\n" \
              "$$수식$${saa} DIV {sbb} = {c}.{a}{a}{a} CDOTS CDOTS$$/수식$$ → $$수식$${snn}$$/수식$$\n" \
              "따라서 차는 $$수식$${soo} - {spp} = {sqq}$$/수식$$입니다.\n\n"



    while True:
        while True:
            sff = np.random.randint(31, 100)
            if (sff % 9) != 0:
                break

        skk = sff / np.gcd(sff, 9)
        sll = 9 / np.gcd(sff, 9)

        saa = skk / 10
        sbb = sll / 10

        c = int(saa / sbb)
        smalla = (saa / sbb) - c
        check_a = [i for i in str(smalla)]
        a = int(check_a[2])

        smm = round(saa / sbb, 1)
        snn = round(saa / sbb, 2)

        soo = max(smm, snn)
        spp = min(smm, snn)
        sqq = round(soo - spp, 2)

        if a != 9:
            break


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(sqq=sqq)
    comment = comment.format(saa=saa, sbb=sbb, a=a, c=c, sff=sff, skk=skk, sll=sll, smm=smm, snn=snn, soo=soo, spp=spp,
                             sqq=sqq)

    return stem, answer, comment






































# 6-2-2-50
def decimaldiv622_Stem_044():
    stem = "길이가 $$수식$${saa} rm m$$/수식$$인 나무도막의 무게는 $$수식$${sbb} rm kg$$/수식$$입니다. 이 나무도막의 굵기가 일정하다면 나무도막 $$수식$$1 rm m$$/수식$$의 무게는 몇 $$수식$$rm kg$$/수식$$인지 반올림하여 소수 둘째 자리까지 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${sdd} rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$나무도막의 무게$$수식$$RIGHT ) ` DIV ` LEFT ($$/수식$$나무도막의 길이$$수식$$RIGHT )$$/수식$$\n$$수식$$= {sbb} DIV {saa} = {scc}$$/수식$$\n" \
              "몫을 반올림하여 소수 둘째 자리까지 나타내면 $$수식$${sdd}$$/수식$$이므로\n" \
              "나무도막 $$수식$$1 rm m$$/수식$$의 무게는 $$수식$${sdd} rm kg$$/수식$$입니다.\n\n"


    while True:
        saa = np.random.randint(10, 100)
        if ((saa % 7) == 0) or ((saa % 11) == 0) or ((saa % 13) == 0) or ((saa % 17) == 0) or ((saa % 19) == 0) or (
                (saa % 23) == 0):
            smm = np.random.randint(1000, 10000)
            if ((smm % 10) != 0) and ((smm % saa) != 0):
                break

    sbb = smm / 100
    smallc = sbb / saa
    check_a = [i for i in str(smallc)]

    if int(sbb / saa) >= 10:
        a1 = int(check_a[0])
        a2 = int(check_a[1])
        a3 = "."
        a4 = int(check_a[3])
        a5 = int(check_a[4])
        a6 = int(check_a[5])
        a7 = "CDOTS"
        scc = "%d%d%s%d%d%d %s %s" % (a1, a2, a3, a4, a5, a6, a7, a7)

    else:
        a1 = int(check_a[0])
        a2 = "."
        a3 = int(check_a[2])
        a4 = int(check_a[3])
        a5 = int(check_a[4])
        a6 = "CDOTS"
        scc = "%d%s%d%d%d %s %s" % (a1, a2, a3, a4, a5, a6, a6)

    sdd = round(smallc, 2)


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(sdd=sdd)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)

    return stem, answer, comment











































# 6-2-2-51
def decimaldiv622_Stem_045():
    stem = "오렌지 주스 $$수식$${saa} rm L$$/수식$$를 $$수식$${sbb}$$/수식$$명이 똑같이 나누어 마시려고 합니다 한 사람이 몇 $$수식$$rmL$$/수식$$ 씩 마시게 되는지 반올림하여 소수 첫째 자리까지 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${sdd} rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$오렌지 주스의 양$$수식$$RIGHT ) DIV LEFT ($$/수식$$똑같이 나누어 마신 사람 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {saa} DIV {sbb} = {scc}$$/수식$$\n" \
              "몫을 반올림하여 소수 첫째 자리까지 나타내면\n" \
              "$$수식$${sdd}$$/수식$$이므로 한 사람이 $$수식$${sdd} rm L$$/수식$$씩 마시게 됩니다.\n\n"



    while True:
        while True:
            smm = np.random.randint(201, 900)
            if (smm % 10) != 0:
                saa = smm / 100
                sbb = np.random.randint(int(saa + 1), 10)
                if ((sbb % smm) != 0) and ((smm % sbb) != 0):
                    break

        smallc = saa / sbb
        check_a = [i for i in str(smallc)]

        if int(sbb / saa) >= 10:
            a1 = int(check_a[0])
            a2 = int(check_a[1])
            a3 = "."
            a4 = int(check_a[3])
            if a4 == 9:
                continue

            a5 = int(check_a[4])
            a6 = "CDOTS"
            scc = "%d%d%s%d%d %s %s" % (a1, a2, a3, a4, a5, a6, a6)

        else:
            a1 = int(check_a[0])
            a2 = "."
            a3 = int(check_a[2])
            if a3 == 9:
                continue

            a4 = int(check_a[3])
            a5 = "CDOTS"
            scc = "%d%s%d%d %s %s" % (a1, a2, a3, a4, a5, a5)

        sdd = round(smallc, 1)

        break


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(sdd=sdd)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)

    return stem, answer, comment



































# 6-2-2-52
def decimaldiv622_Stem_046():
    stem = "몫의 소수 $$수식$${scc}$$/수식$$째 자리 숫자를 구해 보세요.\n$$표$$$$수식$${saa} DIV {sbb}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${d}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {a}{b}.{c}{d}{d}{d} CDOTS CDOTS$$/수식$$이므로\n" \
              "몫의 소수 둘째 자리부터 숫자 $$수식$${d}$$/수식$${ga1} 반복되는 규칙이 있습니다.\n" \
              "따라서 몫의 소수 $$수식$${scc}$$/수식$$째 자리 숫자는 $$수식$${d}$$/수식$$입니다.\n\n"


    a = np.random.randint(1, 10)
    d = np.random.randint(1, 10)
    b = np.random.randint(0, 10)
    c = np.random.randint(0, 10)

    sff = ((a * 1000) + (b * 100) + (c * 10) + d) - ((a * 100) + (b * 10) + c)

    smalla = sff
    smallb = 9
    # frac = [smalla, smallb]

    while (smallb != 0):  # 최대공약수 계산
        temp = smalla % smallb
        smalla = smallb
        smallb = temp

    gcd_result = abs(smalla)
    sdd = sff / gcd_result
    sbb = int(9 / gcd_result)

    saa = sdd / 10
    scc = np.random.randint(5, 20)


    ga1 = josa(d, "가")

    stem = stem.format(saa=saa, sbb=sbb, scc=scc)
    answer = answer.format(d=d)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, a=a, b=b, c=c, d=d, sdd=sdd, sff=sff, ga1=ga1)

    return stem, answer, comment




































# 6-2-2-53
def decimaldiv622_Stem_047():
    stem = "기차가 $$수식$${saa}$$/수식$$시간 $$수식$${sbb}$$/수식$$분 동안 $$수식$${scc} rmkm$$/수식$$를 달렸습니다. 이 기차의 빠르기가 일정하다면 한 시간 동안 달린 거리는 몇 $$수식$$rmkm$$/수식$$인지 반올림하여 자연수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${see} rm {{km}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa}$$/수식$$시간 $$수식$${sbb}$$/수식$$분$$수식$$= {saa} {sbb} over 60$$/수식$$시간$$수식$$= {sdd}$$/수식$$시간\n" \
              "$$수식$$LEFT ($$/수식$$한 시간 동안 달린 거리$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$$전체 거리$$수식$$RIGHT ) DIV LEFT ($$/수식$$달린 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {scc} DIV {sdd} = {a}{b}.{b} CDOTS CDOTS$$/수식$$\n" \
              "몫을 반올림하여 자연수로 나타내면 $$수식$${see}$$/수식$$이므로 한 시간 동안 달린 거리는 $$수식$${see} rmkm$$/수식$$입니다. \n\n"


    while True:
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 9)
        sff = ((a * 10) + b) - a

        smalla = sff
        smallb = 9

        while (smallb != 0):  # 최대공약수 계산
            temp = smalla % smallb
            smalla = smallb
            smallb = temp

        gcd_result = abs(smalla)
        snn = sff / gcd_result
        smm = 9 / gcd_result

        while True:
            skk = np.random.randint(2, 100)
            if ((smm * skk) > 9) and ((smm * skk) < 100):
                scc = int(snn * skk)
                sgg = smm * skk
                break

        sdd = sgg / 10
        saa = int(sdd)
        shh = sdd - saa
        sbb = int(shh * 60)
        sii = scc / sdd

        if b < 5:
            see = (a * 10) + b
        else:
            see = (a * 10) + b + 1

        if sbb != 0:
            break


    stem = stem.format(saa=saa, sbb=sbb, scc=scc)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, sii=sii, a=a, b=b)

    return stem, answer, comment








































# 6-2-2-54
def decimaldiv622_Stem_048():
    stem = "소금 $$수식$${saa} rm kg$$/수식$$을 한 봉지에 $$수식$${sbb} rm kg$$/수식$$씩 나누어 담으려고 합니다. 나누어 담을 수 있는 봉지 수와 남는 소금은 몇 $$수식$$rm kg$$/수식$$인지 각각 구해 보세요.\n"
    answer = "(정답)\n$$수식$${scc}$$/수식$$봉지, $$수식$${f}.{g} rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$````````````````{scc}$$/수식$$\n" \
              "$$수식$$````````$$/수식$$─────\n" \
              "$$수식$${sbb}```` RIGHT )````{a}````{b}````.{c}$$/수식$$ \n" \
              "$$수식$$````````````{d}````{e}$$/수식$$\n" \
              "$$수식$$````````$$/수식$$─────\n" \
              "$$수식$$````````````````````````{f}.{g}$$/수식$$\n" \
              "$$수식$${scc}$$/수식$$봉지에 담을 수 있고, 남는 소금은 $$수식$${f}.{g} rm kg$$/수식$$입니다.\n\n"


    sbb = np.random.randint(3, 10)

    while True:
        smm = np.random.randint((sbb * 100), 1000)
        if (smm % 10) != 0:
            break

    saa = smm / 10
    check_m = [int(i) for i in str(smm)]

    a = check_m[0]
    b = check_m[1]
    c = check_m[2]


    scc, scc2 = divmod((smm - c) / 10, sbb)
    scc = int(scc)
    smallde = scc * sbb
    check_de = [i for i in str(smallde)]
    d = int(check_de[0])
    e = int(check_de[1])


    smallfg = ((a * 10) + b + (c * 0.1)) - ((d * 10) + e)
    smallfg = round(smallfg, 1)
    check_fg = [i for i in str(smallfg)]

    f = int(check_fg[0])
    g = int(check_fg[2])


    stem = stem.format(saa=saa, sbb=sbb, scc=scc)
    answer = answer.format(scc=scc, f=f, g=g)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, a=a, b=b, c=c, d=d, e=e, f=f, g=g)

    return stem, answer, comment





































# 6-2-2-55
def decimaldiv622_Stem_049():
    stem = "주스 $$수식$${saa} rm L$$/수식$$를 한 병에 $$수식$${sbb} rm L$$/수식$$씩 나누어 담으려고 합니다. 식을 완성하고, 나누어 담을 수 있는 병 수와 남는 주스의 양을 각각 구해 보세요.\n$$수식$${saa} $$/수식$$ {sb} $$수식$$ = $$/수식$$ $$수식$${box1}$$/수식$$\n $$수식$${box2}$$/수식$$ 병,  $$수식$${box3}$$/수식$$ $$수식$$ rm L$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${sdd}$$/수식$$, ㉡ $$수식$${scc}$$/수식$$, ㉢ $$수식$${sdd} rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa}$$/수식$$에서 $$수식$${sbb}$$/수식$${rur1} $$수식$${scc}$$/수식$$번 빼면 $$수식$${sdd}$$/수식$${ga1} 남습니다.\n" \
              "따라서 나누어 담을 수 있는 병 수는 $$수식$${scc}$$/수식$$병이고, 남는 주스는 $$수식$${sdd} rm L$$/수식$$입니다.\n\n"


    while True:
        smm = np.random.randint(100, 1000)
        if (smm % 10) != 0:
            break

    saa = smm / 10
    sbb = np.random.randint(3, 10)
    c_list = []

    for i in range(1, int(saa)):
        if (sbb * i) < saa:
            c_list.append(i)

    c_list.sort(reverse=True)
    scc = int(c_list[0])


    sb = ""
    for j in range(1, scc + 1):
        sb = sb + "$$수식$$ - %d $$/수식$$" % sbb
    sdd = round(saa - (sbb * scc), 1)

    box1 = "box{㉠````````````````````}"
    box2 = "box{㉡````````````````````}"
    box3 = "box{㉢````````````````````}"

    rur1 = josa(sbb, "를")
    ga1 = josa(sdd, "가")


    stem = stem.format(saa=saa, sbb=sbb, sb=sb, box1=box1, box2=box2, box3=box3)
    answer = answer.format(sdd=sdd, scc=scc)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, rur1=rur1, ga1=ga1)

    return stem, answer, comment

































# 6-2-2-56
def decimaldiv622_Stem_050():
    stem = "리본 $$수식$${sbb} rm m$$/수식$$로 상자 하나를 묶을 수 있습니다. 리본 $$수식$${saa} rm m$$/수식$$로 똑같은 모양의 상자를 리본으로 묶을 때 묶을 수 있는 상자 수와 남는 리본은 몇 $$수식$$rm m$$/수식$$인지 구해 보세요.\n"
    answer = "(정답)\n$$수식$${m}{n}$$/수식$$상자, $$수식$${i}.{c} rm m$$/수식$$\n"

    comment = "(해설)\n" \
              "$$수식$$````````````````{m}````{n}$$/수식$$\n" \
              "$$수식$$````````$$/수식$$─────\n" \
              "$$수식$${sbb}```` RIGHT )````{a}````{b}````.{c}$$/수식$$ \n" \
              "$$수식$$````````````{d}$$/수식$$\n" \
              "$$수식$$````````$$/수식$$─────\n" \
              "$$수식$$````````````{e}````{b}$$/수식$$\n" \
              "$$수식$$````````````{g}````{h}$$/수식$$\n" \
              "$$수식$$````````$$/수식$$─────\n" \
              "$$수식$$````````````````````````{i}````.{c}$$/수식$$\n" \
              "따라서 $$수식$${m}{n}$$/수식$$상자를 묶을 수 있고, 리본은 $$수식$${i}.{c} rm m$$/수식$$가 남습니다.\n\n"

   
    sbb = np.random.randint(2, 8)

    while True:
        smm = np.random.randint(100, 1000)
        if (smm % 10) != 0:
            check_m = [int(i) for i in str(smm)]
            if check_m[0] > sbb:
                a = check_m[0]
                b = check_m[1]
                c = check_m[2]
                break

    saa = smm / 10
    m, smallm = divmod(a, sbb)
    d = sbb * m
    e = a - d
    n, smalln = divmod((e * 10) + b, sbb)
    smallgh = sbb * n

    if smallgh >= 10:
        check_gh = [int(i) for i in str(smallgh)]
        g = check_gh[0]
        h = check_gh[1]
        i = (e * 10 + b) - (g * 10 + h)

    else:
        g = 0
        h = smallgh
        i = (e * 10 + b) - h


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(m=m, n=n, i=i, c=c)
    comment = comment.format(sbb=sbb, a=a, b=b, c=c, d=d, e=e, g=g, h=h, i=i, m=m, n=n)

    return stem, answer, comment

































# 6-2-2-57
def decimaldiv622_Stem_051():
    stem = "철사 $$수식$${sbb} rm {{cm}}$$/수식$$로 정사각형 한 개를 만들 수 있습니다. 철사 $$수식$${saa} rm {{cm}}$$/수식$$로 똑같은 크기의 정사각형을 몇 개 만들 수 있고, 남는 철사는 몇 $$수식$$rm {{cm}}$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${scc}$$/수식$$개, $$수식$${g}.{h} rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$````````````````````{scc}$$/수식$$\n" \
              "$$수식$$````$$/수식$$────\n" \
              "$$수식$${sbb}````RIGHT )````{a}{b}.{c}$$/수식$$\n" \
              "$$수식$$````````````````{e}{f}$$/수식$$\n" \
              "$$수식$$````$$/수식$$────\n" \
              "$$수식$$````````````````````{g}.{h}$$/수식$$\n" \
              "따라서 정사각형 $$수식$${scc}$$/수식$$개를 만들 수 있고, 철사는 $$수식$${g}.{h} rm {{cm}}$$/수식$$남습니다.\n\n"



    while True:
        while True:
            smm = np.random.randint(100, 899)
            if (smm % 10) != 0:
                break
        saa = smm / 10
        check_a = [i for i in str(saa)]
        a = int(check_a[0])
        b = int(check_a[1])
        c = int(check_a[3])

        scc = np.random.randint(2, 10)
        b_list = []
        for i in range(2, 10):
            if (i * scc) <= int(saa):
                b_list.append(i)
        b_list.sort(reverse=True)
        # print(saa)
        # print(b_list)

        if len(b_list) != 0:
            sbb = int(b_list[0])
            if sbb != 10:
                if saa - (scc * sbb) < sbb:
                    # print(sbb)
                    break

    check_b = [i for i in str(sbb * scc)]
    e = int(check_b[0])
    f = int(check_b[1])

    g = int(((a * 10) + b + (c * 0.1)) - ((e * 10) + f))
    smallh = round(((a * 10) + b + (c * 0.1)) - ((e * 10) + f) - g, 1)
    check_h = [i for i in str(smallh)]
    h = int(check_h[2])


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(scc=scc, g=g, h=h)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, a=a, b=b, c=c, e=e, f=f, g=g, h=h)

    return stem, answer, comment





































# 6-2-2-58
def decimaldiv622_Stem_052():
    stem = "어느 봉사단체에서 쌀 $$수식$${saa} rm kg$$/수식$$을 한 가구당 $$수식$${sbb} rm kg$$/수식$$씩 나누어 주려고 합니다. 이 쌀을 남김없이 모두 나누어 주려면 쌀은 적어도 몇 $$수식$$rm kg$$/수식$$이 더 필요한가요?\n"
    answer = "(정답)\n$$수식$${sff} rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$````````````````{scc}$$/수식$$\n" \
              "$$수식$$````$$/수식$$────\n" \
              "$$수식$${sbb}````RIGHT )````{saa}$$/수식$$\n" \
              "$$수식$$````````````````{sdd}$$/수식$$\n" \
              "$$수식$$````$$/수식$$────\n" \
              "$$수식$$````````````````````````{see}$$/수식$$\n" \
              "따라서 $$수식$${scc}$$/수식$$가구에게 나누어 줄 수 있고, 남는 쌀은 $$수식$${see} rm kg$$/수식$$입니다.\n" \
              "따라서 남김없이 모두 나누어 주려면 쌀은 적어도 $$수식$${sbb} - {see} = {sff} LEFT ( rm kg RIGHT )$$/수식$$이 더 필요합니다.\n\n"


    while True:
        smm = np.random.randint(1000, 10000)
        if (smm % 10) != 0:
            break

    saa = smm / 10
    sbb = np.random.randint(3, 10)
    scc, smalle = divmod(int(saa), sbb)
    sdd = sbb * scc
    smalla = saa - int(saa)

    see = round(smalle + smalla, 1)
    sff = round(sbb - see, 1)


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(sff=sff)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff)

    return stem, answer, comment






































# 6-2-2-59
def decimaldiv622_Stem_053():
    stem = "색 테이프를 한 명에게 $$수식$${saa} rmm$$/수식$$씩 나누어 주면 $$수식$${sbb}$$/수식$$명에게 나누어 주고 $$수식$${scc} rm m$$/수식$$가 남습니다. 이 색 테이프와 길이가 같은 리본을 한 명에게 $$수식$${sdd} rmm$$/수식$$씩 나누어 주려고 합니다. 리본은 몇 명에게 나누어 줄 수 있고, 남은 리본은 몇 $$수식$$rmm$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${sgg}$$/수식$$명, $$수식$${skk} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$나누어 주는 색 테이프의 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {saa} TIMES {sbb} = {see} LEFT ( rmm RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$전체 색 테이프의 길이$$수식$$RIGHT ) = {see} + {scc} = {sff} LEFT ( rmm RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$리본의 길이$$수식$$RIGHT ) = LEFT ($$/수식$$전체 색 테이프의 길이$$수식$$RIGHT ) = {sff} rmm$$/수식$$\n" \
              "$$수식$$````````````````````````{sgg}$$/수식$$\n" \
              "$$수식$$````````````$$/수식$$───\n" \
              "$$수식$${sdd}````RIGHT )````{sff}$$/수식$$\n" \
              "$$수식$$````````````````````{shh}$$/수식$$\n" \
              "$$수식$$````````````$$/수식$$───\n" \
              "$$수식$$````````````````````````{skk}$$/수식$$\n" \
              "따라서 $$수식$${sgg}$$/수식$$명에게 나누어 줄 수 있고, 남는 리본은 $$수식$${skk} rmm$$/수식$$입니다.\n\n"


    while True:
        saa = np.random.randint(2, 10)
        sbb = np.random.randint(2, 10)

        while True:
            shh = np.random.randint(10, 100)
            if (shh % 10) != 0:
                check_h = [int(i) for i in str(shh)]
                if check_h[0] < saa:
                    break

        scc = round(shh / 10, 1)
        see = saa * sbb
        sff = see + scc

        while True:
            szz = np.random.randint(10, 100)
            if (szz % 10) != 0:
                break

        sdd = szz / 10
        sgg, skk = divmod(sff, sdd)
        sgg = int(sgg)
        skk = round(skk, 1)
        shh = round(sdd * sgg, 1)
        if shh <= sgg * sdd:
            break


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(sgg=sgg, skk=skk)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, skk=skk, szz=szz)

    return stem, answer, comment




































# 6-2-2-60
def decimaldiv622_Stem_054():
    stem = "어느 올림픽 금메달의 무게는 $$수식$${saa} rm g$$/수식$$이었습니다. 이 금메달의 실제 금의 무게는 $$수식$${sbb} rm g$$/수식$$이고, 나머지 $$수식$${scc} rm g$$/수식$$은 은으로 되어 있습니다. 금 $$수식$${sdd} rm g$$/수식$$으로 이와 같은 금메달을 최대한 많이 만들 때 은은 적어도 몇 $$수식$$rm g$$/수식$$ 필요한가요?\n"
    answer = "(정답)\n$$수식$${sqq} rm g$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$````````````````````{m}{n}$$/수식$$\n" \
              "$$수식$$````````$$/수식$$─────\n" \
              "$$수식$${sbb}```` RIGHT )````{a}{b}{c}.{d}$$/수식$$ \n" \
              "$$수식$$````````````````{see}$$/수식$$\n" \
              "$$수식$$````````$$/수식$$─────\n" \
              "$$수식$$````````````````````{e}{c}$$/수식$$\n" \
              "$$수식$$````````````````````{g}{h}$$/수식$$\n" \
              "$$수식$$````````$$/수식$$─────\n" \
              "$$수식$$````````````````````````{i}.{d}$$/수식$$\n" \
              "금 $$수식$${sdd} rm g$$/수식$$으로 금메달을 $$수식$${skk}$$/수식$$개 까지 만들 수 있습니다.\n" \
              "$$수식$$LEFT ($$/수식$$금메달 $$수식$${skk}$$/수식$$개를 만드는 데 필요한 은의 무게$$수식$$RIGHT ) = {scc} TIMES {skk} = {sqq} LEFT ( rm g RIGHT )$$/수식$$\n" \
              "따라서 은은 적어도 $$수식$${sqq} rm g$$/수식$$ 필요합니다.\n\n"


    while True:
        saa = np.random.randint(100, 1000)
        if (saa % 10) != 0:
            break

    sbb = np.random.randint(5, 10)
    scc = saa - sbb

    while True:
        shh = np.random.randint(1000, 10000)
        if (shh % 10) != 0:
            check_h = [int(i) for i in str(shh)]
            a = check_h[0]
            b = check_h[1]
            c = check_h[2]
            d = check_h[3]
            if a < sbb:
                break

    sdd = shh / 10
    m, smallm = divmod((a * 10 + b), sbb)
    m = int(m)
    see = sbb * m
    e = (a * 10) + b - see
    n, smallb = divmod((e * 10) + c, sbb)
    n = int(n)
    smallgh = sbb * n

    if smallgh >= 10:
        check_gh = [i for i in str(smallgh)]
        g = int(check_gh[0])
        h = int(check_gh[1])
        i = ((e * 10) + c) - ((g * 10) + h)
        skk = m * 10 + n
        sqq = int(scc * skk)

    else:
        g = ""
        h = smallgh
        i = ((e * 10) + c) - h
        skk = m * 10 + n
        sqq = int(scc * skk)

    if e == 0:
        e = ""


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(sqq=sqq)
    comment = comment.format(sbb=sbb, scc=scc, sdd=sdd, see=see, skk=skk, sqq=sqq, a=a, b=b, c=c, d=d, e=e, g=g, h=h,
                             i=i, m=m, n=n)

    return stem, answer, comment





