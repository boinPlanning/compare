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





def get_josa(a, b):
    if b == "가" or b == "이":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "가"
        else:
            return "이"

    elif b == "라고" or b == "이라고":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "라고"
        else:
            return "이라고"

    elif b == "는" or b == "은":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "는"
        else:
            return "은"

    elif b == "로" or b == "으로":
        if (str(a))[-1] == "0" or (str(a))[-1] == "3" or (str(a))[-1] == "6":
            return "으로"
        else:
            return "로"







# 4-1-3-01
def mulanddiv413_Stem_001():
    stem = "빈 곳에 두 수의 곱을 써넣으세요.\n$$수식$${boxone}$$/수식$$  $$수식$${boxtwo}$$/수식$$  $$수식$${boxthree}$$/수식$$\n"
    answer = "(정답)\n$$수식$${scc}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} TIMES {sbb} = {scc}$$/수식$$ \n\n"


    smalla_1 = np.random.randint(1, 10)
    smalla_2 = np.random.randint(1, 10)
    smalla_3 = np.random.randint(1, 10)
    saa = (smalla_1 * 100) + (smalla_2 * 10) + smalla_3

    smallb = np.random.randint(2, 10)
    sbb = smallb * 10

    scc = saa * sbb

    boxone = "box{%d}" % saa
    boxtwo = "box{%d}" % sbb
    boxthree = "box{%s````````````````````}" % "㉠"


    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxthree=boxthree)
    answer = answer.format(scc=scc)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc)

    return stem, answer, comment



































# 4-1-3-05
def mulanddiv413_Stem_002():
    stem = "곱의 크기를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$표$$ $$수식$${saa} TIMES {sbb}$$/수식$$ ○ $$수식$${scc} TIMES {sdd}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설) \n" \
              "$$수식$${saa} TIMES {sbb} = {see}$$/수식$$, $$수식$${scc} TIMES {sdd} = {sff}$$/수식$$이므로 $$수식$${see} ```` {a1} ```` {sff}$$/수식$$이므로\n" \
              "$$수식$${saa} TIMES {sbb} ```` {a1} ```` {scc} TIMES {sdd}$$/수식$$입니다.\n\n"


    smalla_1 = np.random.randint(1, 10)
    smalla_2 = np.random.randint(1, 10)
    smalla_3 = np.random.randint(1, 10)
    saa = (smalla_1 * 100) + (smalla_2 * 10) + smalla_3

    smallc_1 = np.random.randint(1, 10)
    smallc_2 = np.random.randint(1, 10)
    smallc_3 = np.random.randint(1, 10)
    scc = (smallc_1 * 100) + (smallc_2 * 10) + smallc_3

    smm = np.random.randint(2, 10)
    snn = np.random.randint(2, 10)

    sbb = smm * 10
    sdd = snn * 10
    see = saa * sbb
    sff = scc * sdd

    if see > sff:
        a1 = "&gt;"
    elif see == sff:
        a1 = "="
    else:
        a1 = "&lt;"


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(a1=a1)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, smm=smm, snn=snn, a1=a1)

    return stem, answer, comment









































# 4-1-3-06
def mulanddiv413_Stem_003():
    stem = "{t1}의 저금통에 든 동전입니다. 모두 얼마인가요?\n{boxone}{boxtwo}\n{boxthree}{boxfour}\n"
    answer = "(정답)\n$$수식$${sgg}$$/수식$$원\n"
    comment = "(해설)\n" \
              "$$수식$${saa}$$/수식$$원짜리 동전은 $$수식$${saa} TIMES {scc} = {see} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$이고 " \
              "$$수식$${sbb}$$/수식$$원짜리 동전은 $$수식$${sbb} TIMES {sdd} = {sff} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$입니다.\n" \
              "{t1}의 저금통에 든 동전은 모두 $$수식$${see} + {sff} = {sgg} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    t1 = ["성진이", "동국이", "종석이", "사랑이", "행복이", "철준이", "찬민이"][np.random.randint(0, 7)]

    m_list = [10, 50, 100, 500]
    out = random.sample(m_list, 2)
    saa = out[0]
    sbb = out[1]

    if ((saa == 10) or (saa == 50)):
        smallc_1 = np.random.randint(1, 10)
        smallc_2 = np.random.randint(1, 10)
        smallc_3 = np.random.randint(1, 10)
        scc = (smallc_1 * 100) + (smallc_2 * 10) + smallc_3
    else:
        smallc = np.random.randint(2, 10)
        scc = smallc * 10

    if ((sbb == 10) or (sbb == 50)):
        smalld_1 = np.random.randint(1, 10)
        smalld_2 = np.random.randint(1, 10)
        smalld_3 = np.random.randint(1, 10)
        sdd = (smalld_1 * 100) + (smalld_2 * 10) + smalld_3
    else:
        smalld = np.random.randint(2, 10)
        sdd = smalld * 10

    see = saa * scc
    sff = sbb * sdd
    sgg = see + sff

    if ((saa == 10) or (saa == 50)):
        boxone = "$$수식$$%d$$/수식$$원짜리 동전" % saa
        boxtwo = " $$수식$$%d$$/수식$$개" % scc
    else:
        boxone = "$$수식$$%d$$/수식$$원짜리 동전" % saa
        boxtwo = " $$수식$$%d$$/수식$$개" % scc

    if ((sbb == 10) or (sbb == 50)):
        boxthree = "$$수식$$%d$$/수식$$원짜리 동전" % sbb
        boxfour = " $$수식$$%d$$/수식$$개" % sdd
    else:
        boxthree = "$$수식$$%d$$/수식$$원짜리 동전" % sbb
        boxfour = " $$수식$$%d$$/수식$$개" % sdd

    boxfive = "%s" % "①"


    stem = stem.format(t1=t1, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour)
    answer = answer.format(sgg=sgg)
    comment = comment.format(t1=t1, saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg)

    return stem, answer, comment




































# 4-1-3-07
def mulanddiv413_Stem_004():
    stem = "계산이 틀린 사람은 누구인가요?\n$$표$${t1} : $$수식$${saa} TIMES {sbb} = {scc}$$/수식$$\n{t2} : $$수식$${sdd} TIMES {see} = {sff}$$/수식$$\n{t3} : $$수식$${sgg} TIMES {shh} = {sii}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "{a1}의 계산식에서 $$수식$${sdd} TIMES {see}$$/수식$$에서 $$수식$${sdd} TIMES {skk} = {smm}$$/수식$$이므로 " \
              "$$수식$${sdd} TIMES {see}$$/수식$$은 $$수식$${smm}$$/수식$$에 $$수식$$0$$/수식$$을 $$수식$$1$$/수식$$개 붙인 $$수식$${snn}$$/수식$$입니다.\n\n"


    t_list = ["진호", "민서", "건희", "주희", "종수", "송선", "하루", "정윤", "상수", "현정", "권기"]

    out = random.sample(t_list, 3)

    tt1 = out[0]
    tt2 = out[1]
    tt3 = out[2]

    while True:
        smalla_1 = np.random.randint(1, 10)
        smalla_2 = np.random.randint(1, 10)
        smalla_3 = np.random.randint(1, 10)
        saa = (smalla_1 * 100) + (smalla_2 * 10) + smalla_3

        smalld_1 = np.random.randint(1, 10)
        smalld_2 = np.random.randint(1, 10)
        smalld_3 = np.random.randint(1, 10)
        sdd = (smalld_1 * 100) + (smalld_2 * 10) + smalld_3

        smallg_1 = np.random.randint(1, 10)
        smallg_2 = np.random.randint(1, 10)
        smallg_3 = np.random.randint(1, 10)
        sgg = (smallg_1 * 100) + (smallg_2 * 10) + smallg_3

        if (saa != sdd) and (saa != sgg) and (sdd != sgg):
            break

    smallb = np.random.randint(2, 10)
    sbb = smallb * 10
    smalle = np.random.randint(2, 10)
    see = smalle * 10
    smallh = np.random.randint(2, 10)
    shh = smallh * 10

    scc = saa * sbb
    sii = sgg * shh
    skk = int(see / 10)
    smm = sdd * skk
    snn = smm * 10

    num_f = len(str(snn))
    while True:
        chf = ""
        for i in range(num_f):
            if i == (num_f - 1):
                chf = chf + "0"
            else:
                smallf = np.random.randint(1, 10)
                chf = chf + str(smallf)
        if int(chf) != snn:
            sff = chf
            break

    p1 = []
    p2 = []
    p3 = []
    p1.append(tt1), p1.append(saa), p1.append(sbb), p1.append(scc)
    p2.append(tt2), p2.append(sdd), p2.append(see), p2.append(sff)
    p3.append(tt3), p3.append(sgg), p3.append(shh), p3.append(sii)
    pp = [p1, p2, p3]
    np.random.shuffle(pp)

    t1 = pp[0][0]
    sa = int(pp[0][1])
    sb = int(pp[0][2])
    sc = int(pp[0][3])
    t2 = pp[1][0]
    sd = int(pp[1][1])
    se = int(pp[1][2])
    sf = int(pp[1][3])
    t3 = pp[2][0]
    sg = int(pp[2][1])
    sh = int(pp[2][2])
    si = int(pp[2][3])


    stem = stem.format(t1=t1, t2=t2, t3=t3, saa=sa, sbb=sb, scc=sc, sdd=sd, see=se, sff=sf, sgg=sg, shh=sh, sii=si)
    answer = answer.format(a1=tt2)
    comment = comment.format(a1=tt2, sdd=sdd, see=see, sff=sff, skk=skk, smm=smm, snn=snn)

    return stem, answer, comment









































# 4-1-3-09
def mulanddiv413_Stem_005():
    stem = "두 곱의 차를 구해 보세요.\n$$표$$ $$수식$${saa} TIMES {sbb}$$/수식$$    $$수식$${scc} TIMES {sdd}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${sgg}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} TIMES {sbb} = {see}$$/수식$$, $$수식$${scc} TIMES {sdd} = {sff}$$/수식$$이므로 두 수의 차는 " \
              "$$수식$${see} - {sff} = {sgg}$$/수식$$입니다.\n\n"


    while True:
        smalla_1 = np.random.randint(1, 10)
        smalla_2 = np.random.randint(1, 10)
        smalla_3 = np.random.randint(1, 10)
        saa = (smalla_1 * 100) + (smalla_2 * 10) + smalla_3

        smallc_1 = np.random.randint(1, 10)
        smallc_2 = np.random.randint(1, 10)
        smallc_3 = np.random.randint(1, 10)
        scc = (smallc_1 * 100) + (smallc_2 * 10) + smallc_3

        smallb = np.random.randint(2, 10)
        sbb = smallb * 10

        smalld = np.random.randint(2, 10)
        sdd = smallb * 10

        see = saa * sbb
        sff = scc * sdd

        if (see > sff):
            break

    sgg = see - sff


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg)
    answer = answer.format(sgg=sgg)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg)

    ran_num = np.random.randint(0, 2)

    if ran_num == 1:  # 두 곱의 합
        stem = "두 곱의 합을 구해 보세요.\n$$표$$ $$수식$${saa} TIMES {sbb}$$/수식$$    $$수식$${scc} TIMES {sdd}$$/수식$$ $$/표$$\n"
        answer = "(정답)\n$$수식$${sgg}$$/수식$$\n"
        comment = "(해설)\n" \
                  "$$수식$${saa} TIMES {sbb} = {see}$$/수식$$, $$수식$${scc} TIMES {sdd} = {sff}$$/수식$$이므로 두 수의 합은 " \
                  "$$수식$${see} + {sff} = {sgg}$$/수식$$입니다.\n\n"

        while True:
            smalla_1 = np.random.randint(1, 10)
            smalla_2 = np.random.randint(1, 10)
            smalla_3 = np.random.randint(1, 10)
            saa = (smalla_1 * 100) + (smalla_2 * 10) + smalla_3

            smallc_1 = np.random.randint(1, 10)
            smallc_2 = np.random.randint(1, 10)
            smallc_3 = np.random.randint(1, 10)
            scc = (smallc_1 * 100) + (smallc_2 * 10) + smallc_3

            smallb = np.random.randint(2, 10)
            sbb = smallb * 10

            smalld = np.random.randint(2, 10)
            sdd = smallb * 10

            see = saa * sbb
            sff = scc * sdd

            if (see > sff):
                break

        sgg = see + sff


        stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg)
        answer = answer.format(sgg=sgg)
        comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg)

    return stem, answer, comment

    # ran_num = np.random.randint(0, 2)
    # if ran_num == 0: # 두 곱의 차
    #     stem = "두 곱의 차를 구해 보세요.\n\n$$표$$ $$수식$${saa} TIMES {sbb}$$/수식$$    $$수식$${scc} TIMES {sdd}$$/수식$$ $$/표$$\n"
    #     answer = "(정답)\n$$수식$${sgg}$$/수식$$\n"
    #     comment = "(해설)\n" \
    #               "$$수식$${saa} TIMES {sbb} = {see}$$/수식$$, $$수식$${scc} TIMES {sdd} = {sff}$$/수식$$이므로 두 수의 차는 " \
    #               "$$수식$${see} - {sff} = {sgg}$$/수식$$입니다.\n\n"
    #
    #     while True:
    #         smalla_1 = np.random.randint(1, 10)
    #         smalla_2 = np.random.randint(1, 10)
    #         smalla_3 = np.random.randint(1, 10)
    #         saa = (smalla_1 * 100) + (smalla_2 * 10) + smalla_3
    #
    #         smallc_1 = np.random.randint(1, 10)
    #         smallc_2 = np.random.randint(1, 10)
    #         smallc_3 = np.random.randint(1, 10)
    #         scc = (smallc_1 * 100) + (smallc_2 * 10) + smallc_3
    #
    #         smallb = np.random.randint(2, 10)
    #         sbb = smallb * 10
    #
    #         smalld = np.random.randint(2, 10)
    #         sdd = smallb * 10
    #
    #         see = saa * sbb
    #         sff = scc * sdd
    #
    #         if(see > sff):
    #             break
    #
    #     sgg = see - sff
    #
    #     stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg)
    #     answer = answer.format(sgg=sgg)
    #     comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg)
    #
    # else :  # 두 곱의 합
    #     stem = "두 곱의 합을 구해 보세요.\n\n$$표$$ $$수식$${saa} TIMES {sbb}$$/수식$$    $$수식$${scc} TIMES {sdd}$$/수식$$ $$/표$$\n"
    #     answer = "(정답)\n$$수식$${sgg}$$/수식$$\n"
    #     comment = "(해설)\n" \
    #               "$$수식$${saa} TIMES {sbb} = {see}$$/수식$$, $$수식$${scc} TIMES {sdd} = {sff}$$/수식$$이므로 두 수의 합은 " \
    #               "$$수식$${see} + {sff} = {sgg}$$/수식$$입니다.\n\n"
    #
    #     while True:
    #         smalla_1 = np.random.randint(1, 10)
    #         smalla_2 = np.random.randint(1, 10)
    #         smalla_3 = np.random.randint(1, 10)
    #         saa = (smalla_1 * 100) + (smalla_2 * 10) + smalla_3
    #
    #         smallc_1 = np.random.randint(1, 10)
    #         smallc_2 = np.random.randint(1, 10)
    #         smallc_3 = np.random.randint(1, 10)
    #         scc = (smallc_1 * 100) + (smallc_2 * 10) + smallc_3
    #
    #         smallb = np.random.randint(2, 10)
    #         sbb = smallb * 10
    #
    #         smalld = np.random.randint(2, 10)
    #         sdd = smallb * 10
    #
    #         see = saa * sbb
    #         sff = scc * sdd
    #
    #         if (see > sff):
    #             break
    #
    #     sgg = see + sff
    #
    #     stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg)
    #     answer = answer.format(sgg=sgg)
    #     comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg)
    #
    # return stem, answer, comment





































# 4-1-3-11
def mulanddiv413_Stem_006():
    stem = "{t1}네 반 학생 $$수식$${saa}$$/수식$$명에게 {s1}을 새긴 {s2}를 한 개씩 나누어 주려고 합니다. {s2}는 $$수식$${sbb}$$/수식$$원, {s1}을 새기는 데는 $$수식$${scc}$$/수식$$원이 든다면 이름을 새긴 이름표 $$수식$${saa}$$/수식$$개를 만드는 데 필요한 금액은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$원\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${s2} 한 개 구매하는 데 필요한 금액$$수식$$RIGHT )$$/수식$$ \n$$수식$$` = {sbb} + {scc} = {sdd} ` $$/수식$$ $$수식$$LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${s2} $$수식$${saa}$$/수식$$개를 만드는 데 필요한 금액$$수식$$RIGHT )$$/수식$$ \n$$수식$$ = {sdd} TIMES {saa} = {see} `$$/수식$$ $$수식$$ LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$\n\n"


    t1 = ["은현이", "종석이", "창민이", "수진이", "성연이", "시현이", "단하"][np.random.randint(0, 7)]
    s1 = ["이름", "이니셜", "닉네임", "별명"][np.random.randint(0, 4)]
    s2 = ["이름표", "노트", "다이어리"][np.random.randint(0, 3)]

    smalla = np.random.randint(2, 6)
    saa = smalla * 10

    smallb = np.random.randint(10, 100)
    sbb = smallb * 10

    smallc = np.random.randint(10, 100)
    scc = smallc * 10

    while True:
        sdd = sbb + scc
        if (sdd >= 1000):
            sbb = sbb - 10
        else:
            break

    see = sdd * saa

    boxone = "□"


    stem = stem.format(t1=t1, s1=s1, s2=s2, saa=saa, sbb=sbb, scc=scc, boxone=boxone)
    answer = answer.format(see=see)
    comment = comment.format(s2=s2, saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see)

    return stem, answer, comment






































# 4-1-3-12
def mulanddiv413_Stem_007():
    stem = "빈 곳에 알맞은 수를 써넣으세요.\n$$수식$${boxnum}$$/수식$$ → $$수식$${boxtimes}$$/수식$$ → $$수식$${boxone}$$/수식$$\n"
    answer = "(정답)\n$$수식$${shh}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$````````````````{c1}````{c2}````{c3}$$/수식$$ \n" \
              "$$수식$$````TIMES``````````````{a1}````{a2}$$/수식$$ \n" \
              "─────────\n" \
              "$$수식$${f}$$/수식$$ \n" \
              "$$수식$$`{g}$$/수식$$ \n" \
              "─────────\n" \
              "$$수식$$`{h}$$/수식$$\n" \
              "\n\n"


    while True:
        saa = np.random.randint(11, 100)
        if (saa % 10) != 0:
            break

    saa_list = [int(i) for i in str(saa)]
    a1 = int(saa_list[0])
    a2 = int(saa_list[1])

    scc = np.random.randint(100, 1000)
    scc_list = [int(i) for i in str(scc)]
    c1 = int(scc_list[0])
    c2 = int(scc_list[1])
    c3 = int(scc_list[2])

    sff = scc * a2
    if 10 < sff and sff < 100:  # 두 자리 수
        sff_list = [int(i) for i in str(sff)]
        f1 = int(sff_list[0])
        f2 = int(sff_list[1])
        f = "````````````````````````%d````%d" % (f1, f2)
    elif 99 < sff and sff < 1000:  # 세 자리 수
        sff_list = [int(i) for i in str(sff)]
        f1 = int(sff_list[0])
        f2 = int(sff_list[1])
        f3 = int(sff_list[2])
        f = "````````````````%d````%d````%d" % (f1, f2, f3)
    elif 999 < sff and sff < 10000:  # 네 자리 수
        sff_list = [int(i) for i in str(sff)]
        f1 = int(sff_list[0])
        f2 = int(sff_list[1])
        f3 = int(sff_list[2])
        f4 = int(sff_list[3])
        f = "````````%d````%d````%d````%d" % (f1, f2, f3, f4)

    sgg = scc * a1
    if 10 < sgg and sgg < 100:  # 두 자리 수
        sgg_list = [int(i) for i in str(sgg)]
        g1 = int(sgg_list[0])
        g2 = int(sgg_list[1])
        g = "````````````````%d````%d" % (g1, g2)
    elif 99 < sgg and sgg < 1000:  # 세 자리 수
        sgg_list = [int(i) for i in str(sgg)]
        g1 = int(sgg_list[0])
        g2 = int(sgg_list[1])
        g3 = int(sgg_list[2])
        g = "````````%d````%d````%d" % (g1, g2, g3)
    elif 999 < sgg and sgg < 10000:
        sgg_list = [int(i) for i in str(sgg)]
        g1 = int(sgg_list[0])
        g2 = int(sgg_list[1])
        g3 = int(sgg_list[2])
        g4 = int(sgg_list[3])
        g = "%d````%d````%d````%d" % (g1, g2, g3, g4)

    shh = sgg * 10 + sff
    if 999 < shh and shh < 10000:
        shh_list = [int(i) for i in str(shh)]
        h1 = int(shh_list[0])
        h2 = int(shh_list[1])
        h3 = int(shh_list[2])
        h4 = int(shh_list[3])
        h = "%d````%d````%d````%d" % (h1, h2, h3, h4)
    elif 9999 < shh and shh < 100000:
        shh_list = [int(i) for i in str(shh)]
        h1 = int(shh_list[0])
        h2 = int(shh_list[1])
        h3 = int(shh_list[2])
        h4 = int(shh_list[3])
        h5 = int(shh_list[4])
        h = "%d````%d````%d````%d````%d" % (h1, h2, h3, h4, h5)

    boxone = "box{　　　}"
    boxnum = "%d" % scc
    boxtimes = "TIMES %d" % saa


    stem = stem.format(boxone=boxone, boxnum=boxnum, boxtimes=boxtimes)
    answer = answer.format(shh=shh)
    comment = comment.format(saa=saa, a1=a1, a2=a2, scc=scc, c1=c1, c2=c2, h=h, c3=c3, f=f, g=g)

    return stem, answer, comment







































# 4-1-3-13
def mulanddiv413_Stem_008():
    stem = "계산해 보세요.\n$$표$$ $$수식$${saa} TIMES {sdd}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${sgg}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$````````````````{a1}````{a2}````{a3}$$/수식$$\n" \
              "$$수식$$````TIMES``````````````{d1}````{d2}$$/수식$$\n" \
              "─────────\n" \
              "$$수식$${m}$$/수식$$\n" \
              "$$수식$$`{n}$$/수식$$\n" \
              "─────────\n" \
              "$$수식$$`{g}$$/수식$$\n\n"


    saa = np.random.randint(100, 1000)
    saa_list = [int(i) for i in str(saa)]
    a1 = int(saa_list[0])
    a2 = int(saa_list[1])
    a3 = int(saa_list[2])

    while True:
        sdd = np.random.randint(11, 100)
        if (sdd % 10) != 0:
            break

    sdd_list = [int(i) for i in str(sdd)]
    d1 = int(sdd_list[0])
    d2 = int(sdd_list[1])

    smm = saa * d2
    if 10 < smm and smm < 100:  # 두 자리 수
        smm_list = [int(i) for i in str(smm)]
        m1 = int(smm_list[0])
        m2 = int(smm_list[1])
        m = "````````````````````````%d````%d" % (m1, m2)
    elif 99 < smm and smm < 1000:  # 세 자리 수
        smm_list = [int(i) for i in str(smm)]
        m1 = int(smm_list[0])
        m2 = int(smm_list[1])
        m3 = int(smm_list[2])
        m = "````````````````%d````%d````%d" % (m1, m2, m3)
    elif 999 < smm and smm < 10000:  # 네 자리 수
        smm_list = [int(i) for i in str(smm)]
        m1 = int(smm_list[0])
        m2 = int(smm_list[1])
        m3 = int(smm_list[2])
        m4 = int(smm_list[3])
        m = "````````%d````%d````%d````%d" % (m1, m2, m3, m4)

    snn = saa * d1
    if 10 < snn and snn < 100:  # 두 자리 수
        snn_list = [int(i) for i in str(snn)]
        n1 = int(snn_list[0])
        n2 = int(snn_list[1])
        n = "````````````````%d````%d" % (n1, n2)
    elif 99 < snn and snn < 1000:  # 세 자리 수
        snn_list = [int(i) for i in str(snn)]
        n1 = int(snn_list[0])
        n2 = int(snn_list[1])
        n3 = int(snn_list[2])
        n = "````````%d````%d````%d" % (n1, n2, n3)
    elif 999 < snn and snn < 10000:  # 네 자리 수
        snn_list = [int(i) for i in str(snn)]
        n1 = int(snn_list[0])
        n2 = int(snn_list[1])
        n3 = int(snn_list[2])
        n4 = int(snn_list[3])
        n = "%d````%d````%d````%d" % (n1, n2, n3, n4)

    sgg = snn * 10 + smm
    if 99 < sgg and sgg < 1000:  # 세 자리 수
        sgg_list = [int(i) for i in str(sgg)]
        g1 = int(sgg_list[0])
        g2 = int(sgg_list[1])
        g3 = int(sgg_list[2])
        g = "````````````````%d````%d````%d" % (g1, g2, g3)
    elif 999 < sgg and sgg < 10000:  # 네 자리 수
        sgg_list = [int(i) for i in str(sgg)]
        g1 = int(sgg_list[0])
        g2 = int(sgg_list[1])
        g3 = int(sgg_list[2])
        g4 = int(sgg_list[3])
        g = "````````%d````%d````%d````%d" % (g1, g2, g3, g4)
    else:  # 다섯 자리 수
        sgg_list = [int(i) for i in str(sgg)]
        g1 = int(sgg_list[0])
        g2 = int(sgg_list[1])
        g3 = int(sgg_list[2])
        g4 = int(sgg_list[3])
        g5 = int(sgg_list[4])
        g = "%d````%d````%d````%d````%d" % (g1, g2, g3, g4, g5)


    stem = stem.format(saa=saa, sdd=sdd)
    answer = answer.format(sgg=sgg)
    comment = comment.format(a1=a1, a2=a2, a3=a3, d1=d1, d2=d2, m=m, n=n, g=g)

    return stem, answer, comment




































# 4-1-3-14
def mulanddiv413_Stem_009():
    stem = "다음 중 계산 결과가 네 자리 수인 것은 어느 것인가요?\n① $$수식$${x1}$$/수식$$     ② $$수식$${x2}$$/수식$$     ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "① $$수식$${x1} ```` = ```` {xa1}$$/수식$$\n" \
              "② $$수식$${x2} ```` = ```` {xa2}$$/수식$$\n" \
              "③ $$수식$${x3} ```` = ```` {xa3}$$/수식$$\n" \
              "④ $$수식$${x4} ```` = ```` {xa4}$$/수식$$\n" \
              "⑤ $$수식$${x5} ```` = ```` {xa5}$$/수식$$\n" \
              "따라서 계산 결과가 네 자리 수인 것은 {a1}입니다.\n\n"


    while True:
        saa = np.random.randint(100, 1000)
        sbb = np.random.randint(11, 100)
        if (sbb % 10) != 0:
            a, b = divmod(10000, saa)
            if sbb > a:
                break

    while True:
        scc = np.random.randint(100, 1000)
        sdd = np.random.randint(11, 100)
        if (sdd % 10) != 0:
            a, b = divmod(10000, scc)
            if sdd > a:
                break

    while True:
        see = np.random.randint(100, 1000)
        sff = np.random.randint(11, 100)
        if (sff % 10) != 0:
            a, b = divmod(10000, see)
            if sff > a:
                break

    while True:
        sgg = np.random.randint(100, 1000)
        shh = np.random.randint(11, 100)
        if (shh % 10) != 0:
            a, b = divmod(10000, sgg)
            if shh > a:
                break

    while True:
        sii = np.random.randint(100, 1000)
        sjj = np.random.randint(11, 100)
        if (sjj % 10) != 0:
            a, b = divmod(10000, sii)
            if sjj < a:
                break

    skk = saa * sbb
    sll = scc * sdd
    smm = see * sff
    snn = sgg * shh
    soo = sii * sjj

    y1 = "%d TIMES %d" % (saa, sbb)
    y2 = "%d TIMES %d" % (scc, sdd)
    y3 = "%d TIMES %d" % (see, sff)
    y4 = "%d TIMES %d" % (sgg, shh)
    y5 = "%d TIMES %d" % (sii, sjj)
    y_list_idx = [0, 1, 2, 3, 4]
    y_list_sdx = [y1, y2, y3, y4, y5]

    x_list = []
    tmp = [[x, y] for x, y in zip(y_list_idx, y_list_sdx)]
    np.random.shuffle(tmp)

    for idx in range(len(tmp)):
        x_list.append(tmp[idx][1])

    x1 = x_list[0]
    x2 = x_list[1]
    x3 = x_list[2]
    x4 = x_list[3]
    x5 = x_list[4]

    answer_list = [1, 2, 3, 4, 5]
    correct_idx = 0
    for idx in range(len(tmp)):
        if tmp[idx][0] == 4:  # answer = y5
            correct_idx = idx
            answer_list[idx] = soo
        elif tmp[idx][0] == 0:
            answer_list[idx] = skk
        elif tmp[idx][0] == 1:
            answer_list[idx] = sll
        elif tmp[idx][0] == 2:
            answer_list[idx] = smm
        elif tmp[idx][0] == 3:
            answer_list[idx] = snn

    xa1 = answer_list[0]
    xa2 = answer_list[1]
    xa3 = answer_list[2]
    xa4 = answer_list[3]
    xa5 = answer_list[4]


    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, a1=answer_dict[correct_idx], xa1=xa1, xa2=xa2, xa3=xa3,
                             xa4=xa4, xa5=xa5)

    return stem, answer, comment







































# 4-1-3-16
def mulanddiv413_Stem_010():
    stem = "가장 큰 수와 가장 작은 수의 곱을 구해 보세요.\n$$표$$ $$수식$${x1}$$/수식$$  $$수식$${x2}$$/수식$$  $$수식$${x3}$$/수식$$  $$수식$${x4}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} &gt; {sbb} &gt; {scc} &gt; {sdd}$$/수식$$이므로 가장 큰 수는 $$수식$${saa}$$/수식$$이고 가장 작은 수는 $$수식$${sdd}$$/수식$$입니다.\n" \
              "따라서 두 수의 곱은 $$수식$${saa} TIMES {sdd} = {see}$$/수식$$입니다.\n\n"


    while True:
        saa = np.random.randint(100, 1000)
        sbb = np.random.randint(100, 1000)
        if (saa != sbb):
            if saa > sbb:
                break

    while True:
        scc = np.random.randint(11, 100)
        sdd = np.random.randint(11, 100)
        if ((scc % 10) != 0) and ((sdd % 10) != 0):
            if scc > sdd:
                break

    see = saa * sdd

    x_list = [saa, sbb, scc, sdd]
    np.random.shuffle(x_list)
    [x1, x2, x3, x4] = x_list


    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see)

    return stem, answer, comment





































# 4-1-3-17
def mulanddiv413_Stem_011():
    stem = "□ 안에 들어갈 수 있는 두 자리 수 중 가장 작은 수를 구해 보세요.\n$$표$$ $$수식$${saa} TIMES $$/수식$$ □ $$수식$$&gt; {sbb}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${spp}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} TIMES {s1} = {b1}$$/수식$$,  $$수식$${saa} TIMES {s2} = {b2}$$/수식$$\n" \
              "$$수식$${saa} TIMES {snn} = {b3}$$/수식$$,  $$수식$${saa} TIMES {s3} = {b4}$$/수식$$,  $$수식$${saa} TIMES {s4} = {b5}$$/수식$$, $$수식$$CDOTS$$/수식$$\n" \
              "따라서 □ 안에 들어갈 수 있는 두 자리 수는 $$수식$${snn}$$/수식$$보다\n큰 수 이므로 가장 작은 수는 $$수식$${spp}$$/수식$$입니다. \n\n"


    while True:
        while True:
            saa = np.random.randint(100, 1000)
            sbb = np.random.randint(1000, 100000)
            if sbb > (saa * 9):
                break

        snn = int(sbb / saa)
        spp = snn + 1
        if spp < 100:
            b1 = saa * (snn - 2)
            b2 = saa * (snn - 1)
            b3 = saa * snn
            b4 = saa * (snn + 1)
            b5 = saa * (snn + 2)

            s1 = snn - 2
            s2 = snn - 1
            s3 = snn + 1
            s4 = snn + 2
            break


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(spp=spp)
    comment = comment.format(saa=saa, sbb=sbb, snn=snn, spp=spp, b1=b1, b2=b2, b3=b3, b4=b4, b5=b5, s1=s1, s2=s2, s3=s3,
                             s4=s4)

    return stem, answer, comment









































# 4-1-3-18
def mulanddiv413_Stem_012():
    stem = "{t}는 매일 $$수식$${saa} rm mL$$/수식$$의 {r}를 마십니다. {t}가\n$$수식$${sbb}$$/수식$$월과 $$수식$${scc}$$/수식$$월에 마신 {r}의 양은 모두 몇 $$수식$$rm mL$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${sgg} rm mL$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sbb}$$/수식$$월과 $$수식$${scc}$$/수식$$월은 $$수식$${sdd} + {see} = {sff} ` LEFT ($$/수식$$일$$수식$$RIGHT )$$/수식$$이므로 " \
              "{t}가 두 달 동안 마신 {r}는 $$수식$${saa} TIMES {sff} = {sgg} LEFT ( rm mL RIGHT )$$/수식$$입니다.\n\n"


    t = ["미성이", "준성이", "시진이", "정국이", "민상이", "수정이"][np.random.randint(0, 6)]
    r = ["우유", "미숫가루", "두유", "사이다", "주스"][np.random.randint(0, 5)]

    smalla = np.random.randint(10, 100)
    saa = smalla * 10

    month = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    bc_list = random.sample(month, 2)
    sbb = bc_list[0]
    scc = bc_list[1]

    if sbb == 1 or sbb == 3 or sbb == 5 or sbb == 7 or sbb == 8 or sbb == 10 or sbb == 12:
        sdd = 31
    else:
        sdd = 30

    if scc == 1 or scc == 3 or scc == 5 or scc == 7 or scc == 8 or scc == 10 or scc == 12:
        see = 31
    else:
        see = 30

    sff = sdd + see
    sgg = saa * sff


    stem = stem.format(t=t, saa=saa, r=r, sbb=sbb, scc=scc)
    answer = answer.format(sgg=sgg)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, t=t, r=r)

    return stem, answer, comment








































# 4-1-3-19
def mulanddiv413_Stem_013():
    stem = "{t}네 농장에서 딴 {s}{j1} 한 상자에 $$수식$${saa}$$/수식$$개씩 $$수식$${sbb}$$/수식$$상자에 담아 포장을 하였습니다. 포장한 {s}{j2} 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${scc}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$포장한 {s}의 수$$수식$$RIGHT )$$/수식$$\n " \
              "$$수식$$= ` LEFT ($$/수식$$한 상자에 들어가는 {s}의 수$$수식$$RIGHT ) TIMES LEFT ($$/수식$$상자 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {saa} TIMES {sbb} = {scc} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"


    t = ["미성이", "준성이", "시진이", "정국이", "민상이", "수정이"][np.random.randint(0, 6)]
    s = ["귤", "사과", "포도", "복숭아", "감"][np.random.randint(0, 5)]

    if s == "사과" or s == "포도" or s == "복숭아":
        j1 = "를"
        j2 = "는"
    else:
        j1 = "을"
        j2 = "은"

    saa = np.random.randint(100, 1000)
    sbb = np.random.randint(26, 100)
    scc = saa * sbb


    stem = stem.format(t=t, s=s, j1=j1, j2=j2, saa=saa, sbb=sbb)
    answer = answer.format(scc=scc)
    comment = comment.format(s=s, saa=saa, sbb=sbb, scc=scc)

    return stem, answer, comment





































# 4-1-3-20
def mulanddiv413_Stem_014():
    stem = "설명하는 수와 $$수식$${saa}$$/수식$$의 곱은 얼마인가요?\n$$수식$$100$$/수식$$이 $$수식$${sbb}$$/수식$$개, $$수식$$10$$/수식$$이 $$수식$${scc}$$/수식$$개, $$수식$$1$$/수식$$이 $$수식$${sdd}$$/수식$$인 수\n"
    answer = "(정답)\n$$수식$${smm}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$100$$/수식$$이 $$수식$${sbb}$$/수식$$개, $$수식$$10$$/수식$$이 $$수식$${scc}$$/수식$$개, $$수식$$1$$/수식$$이 $$수식$${sdd}$$/수식$$인 수는\n" \
              "$$수식$${see} + {sff} + {sgg} = {shh}$$/수식$$입니다.\n" \
              "따라서 $$수식$${shh}$$/수식$$와 $$수식$${saa}$$/수식$$의 곱은 $$수식$${shh} TIMES {saa} = {smm}$$/수식$$입니다.\n\n"


    saa = np.random.randint(10, 100)
    sbb = np.random.randint(1, 10)
    sdd = np.random.randint(1, 10)
    scc = np.random.randint(1, 50)

    sff = scc * 10
    sgg = sdd

    while True:
        see = sbb * 100

        shh = see + sff + sgg
        if shh > 1000:
            sbb = sbb - 1
        else:
            break

    smm = shh * saa


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(smm=smm)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, smm=smm)

    return stem, answer, comment









































# 4-1-3-21
def mulanddiv413_Stem_015():
    stem = "어느 문구점에서는 {t} 한 개를 $$수식$${saa}$$/수식$$원에 사와서 $$수식$${sbb}$$/수식$$원에 판다고 합니다. 이 문구점에서는 {t} $$수식$${scc}$$/수식$$개를 팔았을 때 얻는 이익은 모두 얼마인가요?\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$원\n"
    comment = "(해설)\n" \
              "{t} 한 개를 팔았을 때의 이익은\n" \
              "$$수식$${sbb} - {saa} = {sdd} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$ 입니다.\n" \
              "따라서 {t} $$수식$${scc}$$/수식$$개를 팔았을 때 얻는 이익은 모두\n" \
              "$$수식$${sdd} TIMES {scc} = {see} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$ 입니다.\n\n"


    t = ["풀", "딱지", "자", "필통", "붓"][np.random.randint(0, 5)]

    while True:
        smalla = np.random.randint(10, 100)
        saa = smalla * 10
        smallb = np.random.randint(10, 100)
        sbb = smallb * 10
        if (sbb > (saa + 100)):
            break

    scc = np.random.randint(10, 100)
    sdd = sbb - saa
    see = sdd * scc


    stem = stem.format(t=t, saa=saa, sbb=sbb, scc=scc)
    answer = answer.format(see=see)
    comment = comment.format(t=t, saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see)

    return stem, answer, comment









































# 4-1-3-23
def mulanddiv413_Stem_016():
    stem = "{t}는 용돈 $$수식$${skk}$$/수식$$만 원으로 $$수식$${saa}$$/수식$$원짜리 {s}을 $$수식$${sbb}$$/수식$$개 샀습니다. {t}에게 남은 돈은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${sdd}$$/수식$$원\n"
    comment = "(해설)\n" \
              "산 {s}값은 $$수식$${saa} TIMES {sbb} = {scc} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$ 입니다.\n" \
              "{t}에게 {s}을 사고 남은 돈은\n" \
              "$$수식$${skk1} - {scc} = {sdd} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$ 입니다.\n\n"


    t = ["미성이", "준성이", "시진이", "정국이", "민상이", "수정이"][np.random.randint(0, 6)]
    s = ["사탕", "초콜렛", "연필", "카라멜", "풍선껌"][np.random.randint(0, 5)]

    smalla = np.random.randint(10, 100)
    saa = smalla * 10
    sbb = np.random.randint(10, 30)
    scc = saa * sbb
    skk = np.random.randint(1, 6)
    skk1 = skk * 10000

    while True:
        sdd = skk * 10000 - scc
        if (sdd < 0):
            skk = skk + 1
        else:
            break

    if (skk == 1):
        skk = ""


    stem = stem.format(t=t, s=s, saa=saa, sbb=sbb, skk=skk)
    answer = answer.format(sdd=sdd)
    comment = comment.format(s=s, t=t, saa=saa, sbb=sbb, scc=scc, sdd=sdd, skk1=skk1)

    return stem, answer, comment






































# 4-1-3-24
def mulanddiv413_Stem_017():
    stem = "$$수식$${saa}$$/수식$$권이 한 묶음인 {s1}은 $$수식$${sbb}$$/수식$$묶음, $$수식$${scc}$$/수식$$권이 한 묶음인 {s2}은 $$수식$${sdd}$$/수식$$묶음이 있습니다. {s1}과 {s2} 중 무엇이 몇 권 더 많은가요?\n$$수식$${boxone}$$/수식$$이 $$수식$${boxtwo}$$/수식$$권 더 많습니다.\n"
    answer = "(정답)\n{s3}, $$수식$${sgg}$$/수식$$\n"
    comment = "(해설)\n" \
              "{s1}은 $$수식$${sbb} TIMES {saa} = {see} LEFT ($$/수식$$권$$수식$$RIGHT )$$/수식$$ 이고, {s2}은 $$수식$${sdd} TIMES {scc} = {sff} LEFT ($$/수식$$권$$수식$$RIGHT )$$/수식$$ 입니다.\n" \
              "따라서 $$수식$${see} ```` {skk} ```` {sff}$$/수식$$이므로 {s3}이 {s4}보다 $$수식$${smm} - {snn} = {sgg} ` LEFT ($$/수식$$권$$수식$$RIGHT )$$/수식$$ 더 많습니다.\n\n"


    while True:
        s1 = ["동화책", "위인전", "영웅전", "만화책", "소설책"][np.random.randint(0, 5)]
        s2 = ["동화책", "위인전", "영웅전", "만화책", "소설책"][np.random.randint(0, 5)]
        if s1 != s2:
            break

    while True:
        saa = np.random.randint(10, 100)
        scc = np.random.randint(10, 100)
        sbb = np.random.randint(100, 1000)
        sdd = np.random.randint(100, 1000)
        see = sbb * saa
        sff = sdd * scc

        if see != sff:
            break

    if see > sff:
        skk = "&gt;"
        s3 = s1
        s4 = s2
    else:
        skk = "&lt;"
        s3 = s2
        s4 = s1

    smm = max(see, sff)
    snn = min(see, sff)
    sgg = smm - snn

    boxone = "box{%s````````````````````}" % "㉠"
    boxtwo = "box{%s````````````````````}" % "㉡"


    stem = stem.format(s1=s1, s2=s2, saa=saa, sbb=sbb, scc=scc, sdd=sdd, boxone=boxone, boxtwo=boxtwo)
    answer = answer.format(s3=s3, sgg=sgg)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg,
                             smm=smm, snn=snn, skk=skk)

    return stem, answer, comment




































# 4-1-3-25
def mulanddiv413_Stem_018():
    stem = "빈 곳에 알맞은 수를 써넣으세요.\n$$표$$ $$수식$$ {saa} DIV {sbb} $$/수식$$ = $$수식$${boxone}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${scc}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {scc}$$/수식$$\n\n"


    smallb = np.random.randint(2, 10)
    sbb = smallb * 10

    while True:
        smalla = np.random.randint(2, 50)
        saa = sbb * smalla
        if saa >= 1000 or saa < 100:
            continue
        else:
            break

    scc = int(saa / sbb)

    boxone = "box{　　　}"


    stem = stem.format(saa=saa, sbb=sbb, boxone=boxone)
    answer = answer.format(scc=scc)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc)

    return stem, answer, comment









































# 4-1-3-26
def mulanddiv413_Stem_019():
    stem = "다음 중 $$수식$${saa} DIV {sbb}$$/수식$${gwa1} 몫이 같은 것을 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${x1}$$/수식$$  ㉡ $$수식$${x2}$$/수식$$  ㉢ $$수식$${x3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "$$수식$${saa} ` div ` {sbb}$$/수식$${gwa1} $$수식$${y2}$$/수식$$은 몫이 같습니다.\n\n"


    while True:
        saa = np.random.randint(10, 100)
        sbb = np.random.randint(2, 10)

        if saa % sbb == 0:
            break

    smally1 = 10 * saa
    smally2_1 = 10 * saa
    smally2_2 = 10 * sbb
    smally3 = 10 * sbb

    y1 = "%d DIV %d" % (smally1, sbb)
    y2 = "%d DIV %d" % (smally2_1, smally2_2)
    y3 = "%d DIV %d" % (saa, smally3)

    y_list = [y1, y2, y3]
    np.random.shuffle(y_list)

    [x1, x2, x3] = y_list
    correct_answer = ["㉠", "㉡", "㉢"]

    correct_idx = 0

    for idx, sdx in enumerate(y_list):
        if sdx == y2:
            correct_idx = idx
            break

    if (str(sbb))[-1] == "2" or (str(sbb))[-1] == "4" or (str(sbb))[-1] == "5" or (str(sbb))[-1] == "9":
        gwa1 = "와"
    else:
        gwa1 = "과"


    stem = stem.format(saa=saa, sbb=sbb, x1=x1, x2=x2, x3=x3, gwa1=gwa1)
    answer = answer.format(a1=correct_answer[correct_idx])
    comment = comment.format(saa=saa, sbb=sbb, y2=y2, gwa1=gwa1)

    return stem, answer, comment







































# 4-1-3-27
def mulanddiv413_Stem_020():
    stem = "몫의 크기를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$표$$ $$수식$${saa} DIV {sbb}$$/수식$$  ○  $$수식$${scc} DIV {sdd}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${skk}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {see} CDOTS {sff}$$/수식$$, " \
              "$$수식$${scc} DIV {sdd} = {sgg} CDOTS {shh}$$/수식$$이므로 몫은 " \
              "$$수식$${see} ```` {skk} ```` {sgg}$$/수식$$이므로 " \
              "$$수식$${saa} DIV {sbb} ```` {skk} ```` {scc} DIV {sdd}$$/수식$$입니다.\n\n"


    saa = np.random.randint(100, 1000)
    scc = np.random.randint(100, 1000)

    while True:
        sbb = np.random.randint(11, 100)
        if (sbb % 10) != 0:
            break
    while True:
        sdd = np.random.randint(11, 100)
        if (sdd % 10) != 0:
            break

    see, sff = divmod(saa, sbb)
    sgg, shh = divmod(scc, sdd)

    if see > sgg:
        skk = "&gt;"
    elif see == sgg:
        skk = "="
    else:
        skk = "&lt;"


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(skk=skk)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, skk=skk)

    return stem, answer, comment










































# 4-1-3-28
def mulanddiv413_Stem_021():
    stem = "나머지가 다른 것은 어느 것인가요?\n① $$수식$${x1}$$/수식$$     ② $$수식$${x2}$$/수식$$     ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "① $$수식$${x1} = {xa1} CDOTS {xn1}$$/수식$$\n" \
              "② $$수식$${x2} = {xa2} CDOTS {xn2}$$/수식$$\n" \
              "③ $$수식$${x3} = {xa3} CDOTS {xn3}$$/수식$$\n" \
              "④ $$수식$${x4} = {xa4} CDOTS {xn4}$$/수식$$\n" \
              "⑤ $$수식$${x5} = {xa5} CDOTS {xn5}$$/수식$$\n" \
              "따라서 나머지가 다른 것은 {a1}입니다.\n\n"


    smallb = np.random.randint(2, 10)
    sbb = smallb * 10
    smalld = np.random.randint(2, 10)
    sdd = smalld * 10
    smallf = np.random.randint(2, 10)
    sff = smallf * 10
    smallh = np.random.randint(2, 10)
    shh = smallh * 10
    smallj = np.random.randint(2, 10)
    sjj = smallj * 10

    smm = np.random.randint(5, 50)
    soo = np.random.randint(5, 50)
    sqq = np.random.randint(5, 50)
    sss = np.random.randint(5, 50)
    suu = np.random.randint(5, 50)

    min_num = min(sbb, sdd, sff, shh, sjj)

    while True:
        snn = np.random.randint(1, min_num)
        spp = np.random.randint(1, min_num)
        if snn != spp:
            break

    saa = smm * sbb + snn
    scc = soo * sdd + snn
    see = sqq * sff + snn
    sgg = sss * shh + snn
    sii = suu * sjj + spp

    y1 = "%d DIV %d" % (saa, sbb)
    y2 = "%d DIV %d" % (scc, sdd)
    y3 = "%d DIV %d" % (see, sff)
    y4 = "%d DIV %d" % (sgg, shh)
    y5 = "%d DIV %d" % (sii, sjj)

    y_list_idx = [0, 1, 2, 3, 4]
    y_list_sdx = [y1, y2, y3, y4, y5]

    x_list = []
    tmp = [[x, y] for x, y in zip(y_list_idx, y_list_sdx)]
    np.random.shuffle(tmp)

    for idx in range(len(tmp)):
        x_list.append(tmp[idx][1])

    x1 = x_list[0]
    x2 = x_list[1]
    x3 = x_list[2]
    x4 = x_list[3]
    x5 = x_list[4]

    answer_list = [1, 2, 3, 4, 5]  # temporary
    xn_list = [1, 2, 3, 4, 5]  # temporary
    correct_idx = 0

    for idx in range(len(tmp)):
        if tmp[idx][0] == 4:  # answer = y5
            correct_idx = idx
            answer_list[idx] = suu
            xn_list[idx] = spp
        elif tmp[idx][0] == 0:
            answer_list[idx] = smm
            xn_list[idx] = snn
        elif tmp[idx][0] == 1:
            answer_list[idx] = soo
            xn_list[idx] = snn
        elif tmp[idx][0] == 2:
            answer_list[idx] = sqq
            xn_list[idx] = snn
        elif tmp[idx][0] == 3:
            answer_list[idx] = sss
            xn_list[idx] = snn

    xa1 = answer_list[0]
    xa2 = answer_list[1]
    xa3 = answer_list[2]
    xa4 = answer_list[3]
    xa5 = answer_list[4]

    xn1 = xn_list[0]
    xn2 = xn_list[1]
    xn3 = xn_list[2]
    xn4 = xn_list[3]
    xn5 = xn_list[4]


    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, a1=answer_dict[correct_idx], xa1=xa1, xa2=xa2, xa3=xa3,
                             xa4=xa4, xa5=xa5, xn1=xn1, xn2=xn2, xn3=xn3, xn4=xn4, xn5=xn5)

    return stem, answer, comment









































# 4-1-3-30
def mulanddiv413_Stem_022():
    stem = "다음 중 나누어떨어지는 나눗셈의 몫은 얼마인지 구해 보세요.\n$$수식$${box1}$$/수식$$  $$수식$${box2}$$/수식$$  $$수식$${box3}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${x1} = {ax1}$$/수식$$, $$수식$${x2} = {ax2}$$/수식$$, $$수식$${x3} = {ax3}$$/수식$$이므로 나누어떨어지는 나눗셈은 $$수식$${scc} DIV {sdd}$$/수식$$이고, 몫은 $$수식$${skk}$$/수식$$입니다.\n\n"


    smallb = np.random.randint(1, 10)
    sbb = smallb * 10
    smalld = np.random.randint(1, 10)
    sdd = smalld * 10
    smallf = np.random.randint(1, 10)
    sff = smallf * 10

    sgg = np.random.randint(5, 50)
    skk = np.random.randint(5, 50)
    smm = np.random.randint(5, 50)

    shh = np.random.randint(1, sbb)
    snn = np.random.randint(1, sff)

    saa = sgg * sbb + shh
    scc = sdd * skk
    see = smm * sff + snn

    y1 = "%d DIV %d" % (saa, sbb)
    y2 = "%d DIV %d" % (scc, sdd)
    y3 = "%d DIV %d" % (see, sff)

    smallax1 = "%d CDOTS %d" % (sgg, shh)
    smallax2 = "%d" % (skk)
    smallax3 = "%d CDOTS %d" % (smm, snn)

    y_list = [y1, y2, y3]
    np.random.shuffle(y_list)
    [x1, x2, x3] = y_list
    ax_list = ["", "", ""]

    correct_idx = 0

    for idx, sdx in enumerate(y_list):
        if sdx == y1:
            ax_list[idx] = smallax1
        elif sdx == y2:
            correct_idx = idx
            ax_list[idx] = smallax2
        elif sdx == y3:
            ax_list[idx] = smallax3

    ax1 = ax_list[0]
    ax2 = ax_list[1]
    ax3 = ax_list[2]

    box1 = "[``%s``]" % x1
    box2 = "[``%s``]" % x2
    box3 = "[``%s``]" % x3


    stem = stem.format(box1=box1, box2=box2, box3=box3)
    answer = answer.format(a1=skk)
    comment = comment.format(x1=x1, x2=x2, x3=x3, ax1=ax1, ax2=ax2, ax3=ax3, scc=scc, sdd=sdd, skk=skk)

    return stem, answer, comment







































# 4-1-3-31
def mulanddiv413_Stem_023():
    stem = "$$수식$$1$$/수식$$분 동안 사용하는 물의 양이 일정한 가습기에 물 $$수식$${saa} rm mL$$/수식$$를 넣으면 $$수식$${sbb}$$/수식$$분 동안 사용할 수 있다고 합니다. 이 가습기는 $$수식$$1$$/수식$$분 동안 몇 $$수식$$rm mL$$/수식$$의 물을 사용하는 것인가요?\n"
    answer = "(정답)\n$$수식$${scc} rm mL$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1$$/수식$$분 동안 사용하는 물의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$$가습기에 넣은 물의 양$$수식$$RIGHT ) div LEFT ($$/수식$$사용하는 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {saa} div {sbb} = {scc} LEFT ( rm mL RIGHT )$$/수식$$\n\n"


    smallb = np.random.randint(1, 10)
    sbb = smallb * 10

    while True:
        smalla = np.random.randint(2, 100)
        saa = sbb * smalla
        if saa > 100 and saa < 1000:
            break

    scc = int(saa / sbb)


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(scc=scc)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc)

    return stem, answer, comment





































# 4-1-3-32
def mulanddiv413_Stem_024():
    stem = "양계장에서 오늘 $$수식$${saa}$$/수식$$개의 달걀을 생산했습니다. 달걀을 한 판에 $$수식$${sbb}$$/수식$$개씩 담으면 몇 판까지 담을 수 있나요?\n"
    answer = "(정답)\n$$수식$${scc}$$/수식$$판\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {scc} CDOTS {sdd}$$/수식$$이므로 달걀을 한 판에 $$수식$${sbb}$$/수식$$개씩 담으면 " \
              "$$수식$${scc}$$/수식$$판까지 담을 수 있고 $$수식$${sdd}$$/수식$$개가 남습니다.\n\n"


    while True:
        saa = np.random.randint(100, 1000)
        smallb = np.random.randint(2, 10)
        sbb = smallb * 10
        if (saa % sbb) != 0:
            break

    scc, sdd = divmod(saa, sbb)


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(scc=scc)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)

    return stem, answer, comment







































# 4-1-3-33
def mulanddiv413_Stem_025():
    stem = "{t}는 $$수식$${saa}$$/수식$$쪽인 {book}을 모두 읽으려고 합니다. 하루에 $$수식$${sbb}$$/수식$$쪽씩 읽으면 다 읽는 데 모두 며칠이 걸리는지 구해 보세요.\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$일\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb}`={scc}`CDOTS{sdd}$$/수식$$\n" \
              "따라서 하루에 $$수식$${sbb}$$/수식$$쪽씩 $$수식$${scc}$$/수식$$일 읽으면 $$수식$${sdd}$$/수식$$쪽이 남으므로 " \
              "다 읽는 데 모두 $$수식$${see}$$/수식$$일이 걸립니다.\n\n"


    t = ["선주", "순수", "지소", "소이", "단하", "시훤이"][np.random.randint(0, 6)]
    book = ["동화책", "소설책", "위인전", "고전소설", "시집"][np.random.randint(0, 5)]

    while True:
        saa = np.random.randint(100, 1000)
        if (saa % 10) != 0:
            break

    smallb = np.random.randint(2, 10)
    sbb = smallb * 10
    scc, sdd = divmod(saa, sbb)
    see = scc + 1


    stem = stem.format(t=t, saa=saa, sbb=sbb, book=book)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see)

    return stem, answer, comment








































# 4-1-3-34
def mulanddiv413_Stem_026():
    stem = "다음 나눗셈의 나머지 ●가 될 수 있는 수 중 가장 큰 수가 $$수식$${saa}$$/수식$$일 때 ▲를 구해 보세요. $$수식$$LEFT ($$/수식$$단, ■ 는 자연수 입니다.$$수식$$RIGHT )$$/수식$$\n$$표$$$$수식$${sbb} DIV$$/수식$$■$$수식$$=$$/수식$$▲$$수식$$CDOTS$$/수식$$ ●$$/표$$\n"
    answer = "(정답)\n$$수식$${sdd}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sbb} DIV$$/수식$$■ $$수식$$=$$/수식$$ ▲ $$수식$$CDOTS$$/수식$$ ● 에서 " \
              "●는 ■보다 작습니다.\n" \
              "따라서 ●가 될 수 있는 수는 수 중 가장 큰 수가 $$수식$${saa}$$/수식$$이므로 ■는 $$수식$${saa}$$/수식$$보다 1큰 $$수식$${scc}$$/수식$$입니다.\n" \
              "따라서 $$수식$${sbb} DIV {scc} = $$/수식$$▲$$수식$$CDOTS{saa}$$/수식$$이므로\n" \
              "$$수식$${scc} TIMES$$/수식$$ ▲ $$수식$$+ {saa} = {sbb}$$/수식$$, $$수식$${scc} TIMES $$/수식$$ ▲ $$수식$$={skk}$$/수식$$. ▲$$수식$$= {sdd}$$/수식$$입니다.\n\n"


    saa = [19, 29, 39, 49, 59, 69, 79, 89][np.random.randint(0, 6)]
    scc = saa + 1
    sdd = np.random.randint(1, 20)
    sbb = sdd * scc + saa
    skk = sbb - saa


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(sdd=sdd)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, skk=skk)

    return stem, answer, comment








































# 4-1-3-36
def mulanddiv413_Stem_027():
    stem = "몫이 큰 것부터 차례대로 기호를 나열하세요.\n$$표$${boxone} $$수식$${saa} DIV {sbb}$$/수식$$\n{boxtwo} $$수식$${scc} DIV {sdd}$$/수식$$\n{boxthree} $$수식$${see} DIV {sff} $$/수식$$$$/표$$\n"
    answer = "(정답)\n{a1}, {a2}, {a3}\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {sgg}$$/수식$$, $$수식$${scc} DIV {sdd} = {shh}$$/수식$$, $$수식$${see} DIV {sff} = {sii}$$/수식$$\n\n"


    while True:
        sbb = np.random.randint(11, 100)
        if (sbb % 10) != 0:
            break

    while True:
        sdd = np.random.randint(11, 100)
        if (sdd % 10) != 0:
            break

    while True:
        sff = np.random.randint(11, 100)
        if (sff % 10) != 0:
            break

    s_list = random.sample(range(1, 10), 3)
    sgg = s_list[0]
    shh = s_list[1]
    sii = s_list[2]

    saa = sbb * sgg
    scc = sdd * shh
    see = sff * sii

    y_list = [sgg, shh, sii]
    y_list.sort(reverse=True)

    if (y_list[0] == sgg):
        a1 = "㉠"
    elif (y_list[0] == shh):
        a1 = "㉡"
    else:
        a1 = "㉢"

    if (y_list[1] == sgg):
        a2 = "㉠"
    elif (y_list[1] == shh):
        a2 = "㉡"
    else:
        a2 = "㉢"

    if (y_list[2] == sgg):
        a3 = "㉠"
    elif (y_list[2] == shh):
        a3 = "㉡"
    else:
        a3 = "㉢"

    boxone = "%s" % "㉠"
    boxtwo = "%s" % "㉡"
    boxthree = "%s" % "㉢"


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, boxone=boxone, boxtwo=boxtwo,
                       boxthree=boxthree)
    answer = answer.format(a1=a1, a2=a2, a3=a3)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, sii=sii)
    
    return stem, answer, comment








































# 4-1-3-37
def mulanddiv413_Stem_028():
    stem = "㉠과 ㉡에 알맞은 수의 합을 구해 보세요.\n$$표$$$$수식$${saa} DIV {sbb} = $$/수식$$ ㉠ $$수식$$CDOTS {scc}$$/수식$$\n$$수식$${sdd} DIV {see} = {sff} CDOTS$$/수식$$ ㉡$$/표$$\n"
    answer = "(정답)\n$$수식$${sii}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {sgg} CDOTS {scc}$$/수식$$ → ㉠ $$수식$$={sgg}$$/수식$$\n" \
              "$$수식$${sdd} DIV {see} = {sff} CDOTS {shh}$$/수식$$ → ㉡ $$수식$$={shh}$$/수식$$\n" \
              "따라서 ㉠$$수식$$+$$/수식$$㉡$$수식$$={sgg} + {shh} = {sii}$$/수식$$입니다.\n\n"


    while True:
        while True:
            sbb = np.random.randint(11, 100)
            if (sbb % 10) != 0:
                break

        while True:
            see = np.random.randint(11, 100)
            if (see % 10) != 0:
                break

        scc = np.random.randint(1, sbb)
        sgg = np.random.randint(1, 10)
        saa = sbb * sgg + scc

        if 100 <= saa and saa < 1000:
            break

    sdd = np.random.randint(100, 1000)
    sff, shh = divmod(sdd, see)
    sii = sgg + shh


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff)
    answer = answer.format(sii=sii)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, sii=sii)

    return stem, answer, comment











































# 4-1-3-38
def mulanddiv413_Stem_029():
    stem = "가장 큰 수를 가장 작은 수로 나눈 몫을 구해 보세요.\n$$표$$$$수식$${x1}$$/수식$$  $$수식$${x2}$$/수식$$  $$수식$${x3}$$/수식$$  $$수식$${x4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              " $$수식$${saa} &gt; {sbb} &gt; {scc} &gt; {sdd}$$/수식$$이므로 가장 큰 수는 $$수식$${saa}$$/수식$$이고 가장 작은 수는 $$수식$${sdd}$$/수식$$입니다.\n" \
              "따라서 가장 큰 수를 가장 작은 수로 나눈 몫을 구하면 $$수식$${saa} DIV {sdd} = {see}$$/수식$$입니다.\n\n"


    while True:
        randnumb = np.random.randint(10, 100)
        randnumc = np.random.randint(10, 100)
        randnumd = np.random.randint(10, 100)

        if randnumb != randnumc and randnumb != randnumd and randnumc != randnumd:
            r_list = [randnumb, randnumc, randnumd]
            r_list.sort(reverse=True)
            sbb = r_list[0]
            scc = r_list[1]
            sdd = r_list[2]
            see = np.random.randint(1, 10)
            saa = sdd * see

            if saa < 100 and saa > sbb and sdd % 10 != 0:
                break

    y_list = [saa, sbb, scc, sdd]

    np.random.shuffle(y_list)

    x1 = y_list[0]
    x2 = y_list[1]
    x3 = y_list[2]
    x4 = y_list[3]


    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see)

    return stem, answer, comment












































# 4-1-3-41
def mulanddiv413_Stem_030():
    stem = "□ 안에 들어갈 수 있는 수 중에서 가장 큰 수를 구해 보세요.\n$$표$$ □$$수식$$DIV {saa} = {scc} CDOTS$$/수식$$ ● $$/표$$\n"
    answer = "(정답)\n$$수식$${sff}$$/수식$$\n"
    comment = "(해설)\n" \
              "□$$수식$$DIV {saa} = {scc}$$/수식$$이라고 하면\n" \
              "□$$수식$$= {saa} TIMES {scc} = {sdd}$$/수식$$입니다. 나머지인 ●는 나누는 수인 $$수식$${saa}$$/수식$$보다 작아야 하므로" \
              " ● 안에 가장 큰 수는 $$수식$${see}$$/수식$${ga1} 되어야 합니다.\n" \
              "따라서 □ 안에 들어갈 수 있는 가장 큰 수는 $$수식$${sdd}+{see}={sff}$$/수식$$입니다.\n\n"


    while True:
        saa = np.random.randint(11, 100)
        if (saa % 10) != 0:
            break

    scc = np.random.randint(2, 10)
    sdd = saa * scc
    see = saa - 1
    sff = sdd + see

    ga1 = get_josa(see, "가")


    stem = stem.format(saa=saa, scc=scc)
    answer = answer.format(sff=sff)
    comment = comment.format(saa=saa, scc=scc, sdd=sdd, see=see, sff=sff, ga1=ga1)

    return stem, answer, comment










































# 4-1-3-42
def mulanddiv413_Stem_031():
    stem = "{t}는 다음 나눗셈의 몫을 $$수식$${saa}$$/수식$${rago1} 어림하였습니다. 실제로 계산했을 때의 몫과 {t}가 어림한 몫의 차는 얼마인지 구해 보세요.\n$$표$$ $$수식$${sbb} DIV {scc}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${skk}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sbb} DIV {scc} = {sdd} CDOTS {see}$$/수식$$이므로 실제로 계산했을 때의 몫은 $$수식$${sdd}$$/수식$$입니다.\n" \
              "따라서 계산한 몫과 어림한 몫의 차는 \n" \
              "$$수식$${sdd} - {saa} = {skk}$$/수식$$입니다.\n\n"


    t = ["서진이", "동진이", "동준이", "시훤이", "단하", "주철이", "수진이"][np.random.randint(0, 7)]

    while True:
        sbb = np.random.randint(100, 1000)
        scc = np.random.randint(11, 100)
        if ((scc % 10) != 0) and (sbb % scc) != 0:
            sdd, see = divmod(sbb, scc)
            if (sdd > 1):
                saa = np.random.randint(1, sdd)
                skk = sdd - saa
                break

    rago1 = get_josa(saa, "라고")


    stem = stem.format(t=t, saa=saa, sbb=sbb, scc=scc, rago1=rago1)
    answer = answer.format(skk=skk)
    comment = comment.format(t=t, saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, skk=skk)

    return stem, answer, comment








































# 4-1-3-43
def mulanddiv413_Stem_032():
    stem = "나눗셈식에서 ■가 될 수 있는 수 중 가장 작은 수를 구해 보세요. $$수식$$LEFT ($$/수식$$단, ■ 는 자연수입니다.$$수식$$RIGHT )$$/수식$$\n$$표$$■$$수식$$ DIV {saa} = {sbb} CDOTS $$/수식$$●$$/표$$\n"
    answer = "(정답)\n$$수식$${scc}$$/수식$$\n"
    comment = "(해설)\n" \
              " 나머지 ●가 될 수 있는 수는 $$수식$$0$$/수식$$, $$수식$$1$$/수식$$, $$수식$$2$$/수식$$, $$수식$$CDOTS$$/수식$$, $$수식$${sdd}$$/수식$$이므로 ● $$수식$$= 0$$/수식$$일 때 ■가 가장 작습니다. " \
              "따라서 가장 작은 ■$$수식$$= {saa} TIMES {sbb} = {scc}$$/수식$$입니다.\n\n"


    while True:
        saa = np.random.randint(11, 100)
        if (saa % 10) != 0:
            break

    sbb = np.random.randint(2, 20)
    scc = saa * sbb
    sdd = saa - 1


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(scc=scc)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)

    return stem, answer, comment











































# 4-1-3-47
def mulanddiv413_Stem_033():
    stem = "어림한 나눗셈의 몫으로 가장 적절한 것을 찾아 써 보세요.\n$$표$$$$수식$${saa} DIV {sbb}$$/수식$$$$/표$$\n$$수식$$LEFT ( ```` {scc}$$/수식$$,  $$수식$${sdd}$$/수식$$,  $$수식$${see}$$/수식$$,  $$수식$${sff} ```` RIGHT )$$/수식$$\n"
    answer = "(정답)\n$$수식$${shh}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sbb}$$/수식$${nun1} 약 $$수식$${sgg}$$/수식$$이므로 $$수식$${sgg} TIMES {shh} = {skk}$$/수식$$, $$수식$${sgg} TIMES {smm} = {snn}$$/수식$$입니다.\n" \
              "따라서 어림한 나눗셈의 몫으로 가장 적절한 것은 $$수식$${shh}$$/수식$$입니다.\n\n"



    while True:
        while True:
            saa = np.random.randint(100, 1000)
            if saa % 10 != 0:
                break

        while True:
            sbb = np.random.randint(11, 100)
            if sbb % 10 != 0:
                break

        sgg = int(sbb / 10) * 10
        skk = int(saa / 100) * 100
        shh = int(skk / sgg)
        smm = shh + 10
        snn = sgg * smm

        h = [shh - 10, shh - 5, shh + 20, shh + 30]
        r_num = random.sample(range(0, 4), 2)
        h_list = [shh, shh + 10, h[r_num[0]], h[r_num[1]]]
        h_list.sort()

        scc = h_list[0]
        sdd = h_list[1]
        see = h_list[2]
        sff = h_list[3]

        if scc > 0:
            break

    nun1 = get_josa(sbb, "는")


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff)
    answer = answer.format(shh=shh)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, skk=skk, smm=smm,
                             snn=snn, nun1=nun1)

    return stem, answer, comment










































# 4-1-3-48
def mulanddiv413_Stem_034():
    stem = "몫이 더 큰 것의 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${saa} DIV {sbb}$$/수식$$  ㉡ $$수식$${scc} DIV {sdd}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${smm}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${saa} DIV {sbb} = {see}$$/수식$$, ㉡ $$수식$${scc} DIV {sdd} = {sff}$$/수식$$에서 " \
              "$$수식$${see}``{skk}``{sff}$$/수식$$이므로 몫이 더 큰 것은 {smm}입니다.\n\n"


    while True:
        while True:
            sbb = np.random.randint(11, 100)
            sdd = np.random.randint(11, 100)

            if sbb % 10 != 0 and sdd % 10 != 0 and sbb != sdd:
                break

        see = np.random.randint(10, 100)
        sff = np.random.randint(10, 100)

        saa = sbb * see
        scc = sdd * sff

        if saa < 1000:
            if scc < 1000:
                break

    if see > sff:
        skk = "&gt;"
        smm = "㉠"

    else:
        skk = "&lt;"
        smm = "㉡"



    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(smm=smm)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, skk=skk, smm=smm)

    return stem, answer, comment








































# 4-1-3-49
def mulanddiv413_Stem_035():
    stem = "길이가 $$수식$${saa} rm m$$/수식$$인 색 테이프를 $$수식$${sbb} rm {{cm}}$$/수식$$씩 잘라 리본을 만들려고 합니다. 리본을 몇 개까지 만들 수 있는지 구해 보세요.\n"
    answer = "(정답)\n$$수식$${skk}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${saa}rm m = {scc}rm {{cm}}$$/수식$$이므로 $$수식$${scc} DIV {sbb} = {skk}$$/수식$$입니다.\n" \
              "따라서 $$수식$${sbb}rm {{cm}}$$/수식$$짜리 리본을 $$수식$${skk}$$/수식$$개까지 만들 수 있습니다.\n\n"


    while True:
        saa = np.random.randint(1, 100)
        scc = saa * 100
        sbb = [4, 5, 10, 20, 25, 50, 100][np.random.randint(0, 7)]
        skk = int(scc / sbb)

        if skk < 1000:
            if scc < 1000:
                break


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(skk=skk)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, skk=skk)

    return stem, answer, comment








































# 4-1-3-50
def mulanddiv413_Stem_036():
    stem = "길이가 $$수식$${saa} rm m$$/수식$$인 도로 한쪽에 처음부터 끝까지 나무를 심으려고 합니다. $$수식$${sbb}rm m$$/수식$$ 간격으로 나무를 심는다면 나무는 모두 몇 그루가 필요하나요? $$수식$$LEFT ($$/수식$$단, 나무의 두께는 생각하지 않습니다.$$수식$$RIGHT )$$/수식$$\n"
    answer = "(정답)\n$$수식$${sdd}$$/수식$$그루\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$간격 수$$수식$$RIGHT ) = {saa} div {sbb} = {scc} LEFT ($$/수식$$군데$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$도로의 한쪽에 처음부터 끝까지 심은 나무 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$$간격 수$$수식$$RIGHT ) + 1 = {scc} + 1 = {sdd} LEFT ($$/수식$$그루$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 나무는 모두 $$수식$${sdd}$$/수식$$그루 필요합니다.\n\n"


    while True:
        while True:
            sbb = np.random.randint(11, 100)
            if sbb % 10 != 0:
                break

        scc = np.random.randint(10, 100)
        saa = sbb * scc

        if saa < 1000:
            break

    sdd = scc + 1


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(sdd=sdd)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)

    return stem, answer, comment










































# 4-1-3-51
def mulanddiv413_Stem_037():
    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 자연수 중에서 □ 안에 들어갈 수 있는 수는 모두 몇 개인가요?\n$$표$$ $$수식$${saa} TIMES$$/수식$$□  $$수식$$&gt;$$/수식$$  $$수식$${sbb} div {scc}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${snn}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${sbb} div {scc} = {sdd}$$/수식$$, $$수식$${saa} TIMES$$/수식$$□$$수식$$= {sdd}$$/수식$$라고 하면" \
              "□$$수식$$= {sdd} div {saa} = {see}$$/수식$$\n" \
              "$$수식$${saa} TIMES$$/수식$$□$$수식$$ ```` &gt; ```` {sdd}$$/수식$$이므로 □ $$수식$$ &gt; ```` {see}$$/수식$$입니다.\n" \
              "따라서 $$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 자연수 중에서 □ 안에 들어갈 수 있는 수는 {e}{ro1} 모두 $$수식$${snn}$$/수식$$개입니다.\n\n"


    while True:
        while True:
            scc = np.random.randint(11, 100)
            if scc % 10 != 0:
                break

        while True:
            p_flag = False
            sdd = np.random.randint(10, 100)
            for f in range(2, sdd):
                if sdd % f == 0:
                    p_flag = True
            if p_flag:
                break

        sbb = scc * sdd

        if sbb < 1000:
            break


    # 약수 구하기
    divisors = []
    for i in range(1, 9):
        if (sdd % i) == 0:
            divisors.append(i)
    see_list = random.sample(divisors, 1)
    see = see_list[0]

    e_list = []
    saa = int(sdd / see)

    for j in range(1, 10):
        if j > see:
            e_list.append(j)

    e_list.sort()

    if len(e_list) == 1:
        e = "$$수식$$%d$$/수식$$" % e_list[0]
    elif len(e_list) == 2:
        e = "$$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$" % (e_list[0], e_list[1])
    elif len(e_list) == 3:
        e = "$$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$" % (e_list[0], e_list[1], e_list[2])
    elif len(e_list) > 3:
        e = "$$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$CDOTS$$/수식$$, $$수식$$%d$$/수식$$" % (e_list[0], e_list[1], e_list[len(e_list) - 1])

    ro1_material = e_list[-1]
    ro1 = get_josa(ro1_material, "로")

    snn = len(e_list)


    stem = stem.format(saa=saa, sbb=sbb, scc=scc)
    answer = answer.format(snn=snn)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, e=e, snn=snn, ro1=ro1)

    return stem, answer, comment









































# 4-1-3-52
def mulanddiv413_Stem_038():
    stem = "큰 수를 작은 수로 나누었을 때의 몫과 나머지를 순서대로 구해 보세요.\n$$표$$ $$수식$${sa}$$/수식$$   $$수식$${sb}$$/수식$$ $$/표$$\n" \
        "몫 : {box}, 나머지 : {box}"
    answer = "(정답)\n$$수식$${scc}$$/수식$$, $$수식$${sdd}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sff} DIV {sgg} = {scc} CDOTS {sdd}$$/수식$$\n\n"

    box = "$$수식$$box{　　}$$/수식$$"

    while True:
        saa = np.random.randint(11, 1000)
        if saa % 10 != 0:
            break

    while True:
        if saa < 100:
            sbb = np.random.randint(100, 1000)
            if sbb % 10 != 0:
                break

        elif saa > 99:
            sbb = np.random.randint(10, 100)
            if sbb % 10 != 0:
                break

    sff = max(saa, sbb)
    sgg = min(saa, sbb)
    scc, sdd = divmod(sff, sgg)

    show_choice = np.random.randint(0, 2)

    if show_choice == 0:
        sa = saa
        sb = sbb
    else:
        sa = sbb
        sb = saa


    stem = stem.format(sa=sa, sb=sb, box=box)
    answer = answer.format(scc=scc, sdd=sdd)
    comment = comment.format(scc=scc, sdd=sdd, sff=sff, sgg=sgg)

    return stem, answer, comment













































# 4-1-3-55
def mulanddiv413_Stem_039():
    stem = "계산 결과가 맞는지 확인하여 적절한 말을 찾아 기호를 써 보세요.\n$$표$$ $$수식$${saa} DIV {sbb} = {scc} CDOTS {sdd}$$/수식$$ $$/표$$\n$$수식$$LEFT ($$/수식$$ ㉠ 맞습니다.  ㉡ 틀립니다. $$수식$$RIGHT )$$/수식$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {scc} CDOTS {sdd}$$/수식$$\n" \
              "→ $$수식$${sbb} TIMES {scc} = {see}$$/수식$$, $$수식$${see} + {sdd} = {sff}$$/수식$$\n" \
              "따라서 검산 결과가 {skk} 계산이 {smm}\n\n"


    while True:
        while True:
            sbb = np.random.randint(11, 100)
            if sbb % 10 != 0:
                break

        scc = np.random.randint(10, 100)
        sdd = np.random.randint(1, sbb)
        see = sbb * scc
        sff = see + sdd
        temp = np.random.randint(sff - 100, sff + 100)
        saa = [sff, temp][np.random.randint(0, 2)]

        if saa < 1000:
            if see < 1000:
                break


    if saa == sff:
        skk = "맞으므로"
        smm = "맞았습니다."
        a1 = "㉠"

    else:
        skk = "다르므로"
        smm = "틀렸습니다."
        a1 = "㉡"


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(a1=a1)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, skk=skk, smm=smm)

    return stem, answer, comment










































# 4-1-3-56
def mulanddiv413_Stem_040():
    stem = "나머지가 가장 큰 것을 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${saa} DIV {sbb}$$/수식$$  ㉡ $$수식$${scc} DIV {sdd}$$/수식$$\n㉢ $$수식$${see} DIV {sff}$$/수식$$  ㉣ $$수식$${sgg} DIV {shh}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n㉠ $$수식$${saa} DIV {sbb} = {sll} CDOTS {smm}$$/수식$$\n" \
              "㉡ $$수식$${scc} DIV {sdd} = {snn} CDOTS {soo}$$/수식$$\n" \
              "㉢ $$수식$${see} DIV {sff} = {spp} CDOTS {sqq}$$/수식$$\n" \
              "㉣ $$수식$${sgg} DIV {shh} = {srr} CDOTS {sss}$$/수식$$\n" \
              "따라서 나머지의 크기를 비교하면\n" \
              "$$수식$${x1} &gt; {x2} &gt; {x3} &gt; {x4}$$/수식$$이므로 나머지가 가장 큰 것은 {a1} 입니다.\n\n"


    while True:
        sbb = np.random.randint(11, 100)
        if (sbb % 10) != 0:
            break
    while True:
        sdd = np.random.randint(11, 100)
        if (sdd % 10) != 0:
            break
    while True:
        sff = np.random.randint(11, 100)
        if (sff % 10) != 0:
            break
    while True:
        shh = np.random.randint(11, 100)
        if (shh % 10) != 0:
            break

    while True:
        saa = np.random.randint(100, 1000)
        if (saa % sbb) != 0:
            break
    while True:
        scc = np.random.randint(100, 1000)
        if (scc % sdd) != 0:
            break
    while True:
        see = np.random.randint(100, 1000)
        if (see % sff) != 0:
            break
    while True:
        sgg = np.random.randint(100, 1000)
        if (sgg % shh) != 0:
            break

    sll, smm = divmod(saa, sbb)
    snn, soo = divmod(scc, sdd)
    spp, sqq = divmod(see, sff)
    srr, sss = divmod(sgg, shh)

    d_list = [smm, soo, sqq, sss]
    max_value = max(d_list)

    if max_value == smm:
        a1 = "㉠"
    elif max_value == soo:
        a1 = "㉡"
    elif max_value == sqq:
        a1 = "㉢"
    elif max_value == sss:
        a1 = "㉣"

    d_list.sort(reverse=True)
    x1 = d_list[0]
    x2 = d_list[1]
    x3 = d_list[2]
    x4 = d_list[3]


    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh)
    answer = answer.format(a1=a1)
    comment = comment.format(a1=a1, saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, sgg=sgg, shh=shh, sll=sll,
                             smm=smm, snn=snn, soo=soo, spp=spp, sqq=sqq, srr=srr, sss=sss, x1=x1, x2=x2, x3=x3, x4=x4)

    return stem, answer, comment











































# 4-1-3-59
def mulanddiv413_Stem_041():
    stem = "어떤 자연수를 $$수식$${saa}$$/수식$${jo1} 나눌 때 나올 수 있는 나머지 중에서 가장 큰 수와 어떤 자연수를 $$수식$${sbb}$$/수식$${jo2} 나눌 때 나올 수 있는 나머지 중에서 가장 큰 수의 합을 구해 보세요.\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$\n"
    comment = "(해설)\n$$수식$${saa}$$/수식$${jo1} 나눌 때 나올 수 있는 나머지 중에서 가장 큰 수는 $$수식$${scc}$$/수식$$입니다.\n" \
              "$$수식$${sbb}$$/수식$${jo2} 나눌 때 나올 수 있는 나머지 중에서 가장 큰 수는 $$수식$${sdd}$$/수식$$입니다.\n" \
              "따라서 두 수의 합은 $$수식$${scc} + {sdd} = {see}$$/수식$$입니다.\n\n"


    while True:
        saa = np.random.randint(11, 100)
        if (saa % 10) != 0:
            break
    while True:
        sbb = np.random.randint(11, 100)
        if (sbb % 10) != 0:
            break

    # check_a = [int(i) for i in str(saa)]
    # if check_a == 1 or check_a == 2 or check_a == 4 or check_a == 5 or check_a == 7 or check_a == 8 or check_a == 9:
    #     jo1 = "로"
    # else:
    #     jo1 = "으로"
    #
    # check_b = [int(i) for i in str(sbb)]
    # if check_b == 1 or check_b == 2 or check_b == 4 or check_b == 5 or check_b == 7 or check_b == 8 or check_b == 9:
    #     jo2 = "로"
    # else:
    #     jo2 = "으로"

    jo1 = get_josa(saa, "로")
    jo2 = get_josa(sbb, "로")

    scc = saa - 1
    sdd = sbb - 1
    see = scc + sdd


    stem = stem.format(saa=saa, sbb=sbb, jo1=jo1, jo2=jo2)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, jo1=jo1, jo2=jo2)

    return stem, answer, comment
















































# 4-1-3-60
def mulanddiv413_Stem_042():
    stem = "{what} $$수식$${saa}$$/수식$$개를 한 {basket}에 $$수식$${sbb}$$/수식$$개씩 담으려고 합니다. {what}를 모두 담으려면 {basket}는 적어도 몇 개 필요한가요?\n"
    answer = "(정답)\n$$수식$${see}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${saa} DIV {sbb} = {scc} CDOTS {sdd}$$/수식$$\n" \
              "따라서 남는 {what} $$수식$${sdd}$$/수식$$개까지 모두 담으려면 {basket}는 적어도 $$수식$${scc} + 1 = {see} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$ 필요합니다.\n\n"


    saa = np.random.randint(100, 1000)

    while True:
        sbb = np.random.randint(11, 100)
        if sbb % 10 != 0:
            break

    scc, sdd = divmod(saa, sbb)
    see = scc + 1

    what = ["감자", "고구마", "양파", "양배추", "배추", "오이", "무", "가지", "사과", "복숭아", "자두", "참외", "토마토"][np.random.randint(0, 13)]
    basket = ["상자", "손수레", "바구니"][np.random.randint(0, 3)]


    stem = stem.format(saa=saa, sbb=sbb, what=what, basket=basket)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, what=what, basket=basket)

    return stem, answer, comment












































# 4-1-3-62
def mulanddiv413_Stem_043():
    stem = "어떤 수를 $$수식$${saa}$$/수식$${ro1} 나누어야 하는데 잘못하여 곱하였더니 $$수식$${sbb}$$/수식$$ {yo}. 바르게 계산하였을 때 몫과 나머지는 각각 얼마인가요?\n" \
        "몫 : {box}, 나머지 : {box}"
    answer = "(정답)\n$$수식$${sdd}$$수식$$, $$수식$${sff}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □ 라고 하면\n" \
              "$$수식$$LEFT [$$/수식$$잘못한 계산$$수식$$RIGHT ]$$/수식$$ □ $$수식$$TIMES {saa} = {sbb}$$/수식$$,\n" \
              "□$$수식$$={sbb} DIV {saa} = {scc}$$/수식$$\n" \
              "$$수식$$LEFT [$$/수식$$바른 계산$$수식$$RIGHT ] ```` {scc} DIV {saa} = {sdd} CDOTS {sff}$$/수식$$\n" \
              "따라서 바르게 계산했을 때 몫은 $$수식$${sdd}$$/수식$$이고, 나머지는 $$수식$${sff}$$/수식$$입니다.\n\n"

    box = "$$수식$$box{　　}$$/수식$$"

    while True:
        while True:
            saa = np.random.randint(11, 100)
            if (saa % 10) != 0:
                break

        while True:
            smallb = np.random.randint(8, 90)
            sbb = smallb * saa
            if (sbb < 1000) and (sbb > 100):
                break

        scc = int(sbb / saa)
        sdd, sff = divmod(scc, saa)
        if sdd > 0:
            break

    if (int((str(sbb))[-1]) == 2) or (int((str(sbb))[-1]) == 4) or (int((str(sbb))[-1]) == 5) or (
            int((str(sbb))[-1]) == 9):
        yo = "였습니다"
    else:
        yo = "이였습니다"

    ro1 = get_josa(saa, "로")


    stem = stem.format(saa=saa, sbb=sbb, yo=yo, ro1=ro1, box=box)
    answer = answer.format(sdd=sdd, sff=sff)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, sff=sff)

    return stem, answer, comment






