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







# 4-1-6-02
def findingrule416_Stem_001():
    stem = "규칙을 찾아 ㉠에 알맞은 수를 구해 보세요.\n$$수식$${box1}$$/수식$$$$수식$${box2}$$/수식$$$$수식$${box3}$$/수식$$$$수식$${box4}$$/수식$$$$수식$${box5}$$/수식$$$$수식$${box6}$$/수식$$$$수식$${box7}$$/수식$$\n"
    answer = "(정답)\n$$수식$${sd}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$부터 시작하여 $$수식$${sb}$$/수식$$씩 곱한 수가 오른쪽에 있으므로 빈 곳에 알맞은 수는 " \
              "$$수식$${sc} ` times ` {sb} ` = `{sd}$$/수식$$입니다.\n\n"


    sa = np.random.randint(2, 10)
    sb = np.random.randint(2, 10)

    s2 = sa*sb
    s3 = sa*sb**2
    s4 = sa*sb**3
    s5 = sa*sb**4
    s6 = sa*sb**5
    s7 = sa*sb**6

    list = [sa, s2, s3, s4, s5, s6, s7]

    rn= np.random.randint(2, 7)

    list[rn]="㉠"

    sc = list[rn-1]

    sa, s2, s3, s4, s5, s6, s7 = list

    sd=sc*sb

    box1 = "box{%s}" % sa
    box2 = "box{%s}" % s2
    box3 = "box{%s}" % s3
    box4 = "box{%s}" % s4
    box5 = "box{%s}" % s5
    box6 = "box{%s}" % s6
    box7 = "box{%s}" % s7

    stem = stem.format(box1=box1, box2=box2, box3=box3, box4=box4, box5=box5, box6=box6, box7=box7)
    answer = answer.format(sd=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd)

    return stem, answer, comment
















# 4-1-6-03
def findingrule416_Stem_002():
    stem = "규칙적인 수의 배열에서 ■, ●에 알맞은 수를 차례대로 각각 구해 보세요.\n$$수식$${box1}$$/수식$$$$수식$${box2}$$/수식$$$$수식$${box3}$$/수식$$$$수식$${box4}$$/수식$$\n                $$수식$${box5}$$/수식$$$$수식$${box6}$$/수식$$$$수식$${box7}$$/수식$$$$수식$${box8}$$/수식$$\n"
    answer = "(정답)\n$$수식$${sc}$$/수식$$, $$수식$${se}$$/수식$$\n"
    comment = "(해설)\n" \
              "오른쪽으로 $$수식$${sa}$$/수식$$씩 커지는 규칙입니다.\n" \
              "따라서 ■에 알맞은 수는 $$수식$${sb}$$/수식$$보다 $$수식$${sa}$$/수식$$ 큰 수인 $$수식$${sc}$$/수식$$이고, " \
              "●에 알맞은 수는 $$수식$${sd}$$/수식$$보다 $$수식$${sa}$$/수식$$ 큰 수인 $$수식$${se}$$/수식$$ 입니다.\n\n"


    sa = np.random.randint(100, 1000)

    while True:
        sb = np.random.randint(1001, 10000)
        if sb > 4*sa:
            break

    while True:
        sd = np.random.randint(100, 10000)
        if sd > 4*sa:
            break

    sc = sb + sa
    se = sd + sa

    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s6 = 0
    s7 = 0
    s8 = 0

    list = [s1, s2, s3, s4]

    rn = np.random.randint(1, 4)

    list[rn] = "■"

    if rn == 3:
        list[rn-1] = sb
        list[rn-2] = sb-sa
        list[rn-3] = sb-2*sa
    elif rn == 2:
        list[rn+1] = sb+2*sa
        list[rn-1] = sb
        list[rn-2] = sb-sa
    elif rn == 1:
        list[rn+2] = sb+3*sa
        list[rn+1] = sb+2*sa
        list[rn-1] = sb

    s1, s2, s3, s4 = list

    list2 = [s5, s6, s7, s8]

    rn2 = np.random.randint(1, 4)

    list2[rn2] = "●"

    if rn2 == 3:
        list2[rn2-1] = sd
        list2[rn2-2] = sd-sa
        list2[rn2-3] = sd-2*sa
    elif rn2 == 2:
        list2[rn2+1] = sd+2*sa
        list2[rn2-1] = sd
        list2[rn2-2] = sd-sa
    elif rn2 == 1:
        list2[rn2+2] = sd+3*sa
        list2[rn2+1] = sd+2*sa
        list2[rn2-1] = sd

    s5, s6, s7, s8 = list2

    box1 = "[```%s```]" % s1
    box2 = "[```%s```]" % s2
    box3 = "[```%s```]" % s3
    box4 = "[```%s```]" % s4
    box5 = "[```%s```]" % s5
    box6 = "[```%s```]" % s6
    box7 = "[```%s```]" % s7
    box8 = "[```%s```]" % s8

    stem = stem.format(box1=box1, box2=box2, box3=box3, box4=box4, box5=box5, box6=box6, box7=box7, box8=box8)
    answer = answer.format(sc=sc, se=se)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)

    return stem, answer, comment















def three_check(a):
    if 100 <= a and a < 1000:
        return True
    else:
        return False



# 4-1-6-09
def findingrule416_Stem_003():
    stem = "가 ~ 라 의 계산식을 보고 설명에 맞는 계산식을 찾아 기호를 써 보세요.\n$$표$$" \
        "가. $$수식$${ga_first_1} ` + ` {ga_second_1} ` = ` {ga_third_1}$$/수식$$    $$수식$${ga_first_2} ` + ` {ga_second_2} ` = ` {ga_third_2}$$/수식$$\n      $$수식$${ga_first_3} ` + ` {ga_second_3} ` = ` {ga_third_3}$$/수식$$    $$수식$${ga_first_4} ` + ` {ga_second_4} ` = ` {ga_third_4}$$/수식$$\n" \
        "나. $$수식$${na_first_1} ` + ` {na_second_1} ` = ` {na_third_1}$$/수식$$    $$수식$${na_first_2} ` + ` {na_second_2} ` = ` {na_third_2}$$/수식$$\n      $$수식$${na_first_3} ` + ` {na_second_3} ` = ` {na_third_3}$$/수식$$    $$수식$${na_first_4} ` + ` {na_second_4} ` = ` {na_third_4}$$/수식$$\n" \
        "다. $$수식$${da_first_1} ` - ` {da_second_1} ` = ` {da_third_1}$$/수식$$    $$수식$${da_first_2} ` - ` {da_second_2} ` = ` {da_third_2}$$/수식$$\n      $$수식$${da_first_3} ` - ` {da_second_3} ` = ` {da_third_3}$$/수식$$    $$수식$${da_first_4} ` - ` {da_second_4} ` = ` {da_third_4}$$/수식$$\n" \
        "라. $$수식$${ra_first_1} ` - ` {ra_second_1} ` = ` {ra_third_1}$$/수식$$    $$수식$${ra_first_2} ` - ` {ra_second_2} ` = ` {ra_third_2}$$/수식$$\n      $$수식$${ra_first_3} ` - ` {ra_second_3} ` = ` {ra_third_3}$$/수식$$    $$수식$${ra_first_4} ` - ` {ra_second_4} ` = ` {ra_third_4}$$/수식$$$$/표$$\n" \
        "$$표$${saa}는 {smm}의 자리가 $$수식$${skk}$$/수식$$씩 {sqq} {sbb}는 {smm}의 자리 수가 $$수식$${skk}$$/수식$$씩 {suu} 두 수의 {spp} $$수식$${srr}$$/수식$$씩 {sss}집니다.$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설) {stt} 중에서 {saa}의 {smm}의 자리 수가 $$수식$${skk}$$/수식$$씩 {sqq} {sbb}는 {smm}의 자리 수가 $$수식$${skk}$$/수식$$씩 {suu} 계산식은 {ans} 입니다.\n\n"
    
    answer_choice = np.random.randint(0, 4)

    # skk = [1, 2][np.random.randint(0, 2)]
    skk = 1

    if answer_choice == 0:
        ans = "가"

        saa = "더해지는 수"

        smm = ["백", "십"][np.random.randint(0, 2)]

        sqq = ["작아지고", "커지고"][np.random.randint(0, 2)]

        sbb = "더하는 수"

        if sqq == "작아지고":
            suu = "작아지는"
            sss = "작아"
        else:
            suu = "커지는"
            sss = "커"

        spp = "합은"

        if smm == "백":
            srr = skk * 200
            smm_num = 100
        else:
            srr = skk * 20
            smm_num = 10

        stt = "덧셈식"

        while True:
            if sqq == "작아지고":
                ga_first_1 = np.random.randint(100, 1000)
                ga_second_1 = np.random.randint(100, 1000)
                ga_third_1 = ga_first_1 + ga_second_1

                ga_first_2 = ga_first_1 - (skk * smm_num)
                ga_second_2 = ga_second_1 - (skk * smm_num)
                ga_third_2 = ga_first_2 + ga_second_2

                ga_first_3 = ga_first_2 - (skk * smm_num)
                ga_second_3 = ga_second_2 - (skk * smm_num)
                ga_third_3 = ga_first_3 + ga_second_3

                ga_first_4 = ga_first_3 - (skk * smm_num)
                ga_second_4 = ga_second_3 - (skk * smm_num)
                ga_third_4 = ga_first_4 + ga_second_4

                if smm == "백":
                    na_first_1 = np.random.randint(100, 1000)
                    na_second_1 = np.random.randint(100, 1000)
                    na_third_1 = na_first_1 + na_second_1

                    na_first_2 = na_first_1 - (skk * 10)
                    na_second_2 = na_second_1 - (skk * 10)
                    na_third_2 = na_first_2 + na_second_2

                    na_first_3 = na_first_2 - (skk * 10)
                    na_second_3 = na_second_2 - (skk * 10)
                    na_third_3 = na_first_3 + na_second_3

                    na_first_4 = na_first_3 - (skk * 10)
                    na_second_4 = na_second_3 - (skk * 10)
                    na_third_4 = na_first_4 + na_second_4

                else:
                    na_first_1 = np.random.randint(100, 1000)
                    na_second_1 = np.random.randint(100, 1000)
                    na_third_1 = na_first_1 + na_second_1

                    na_first_2 = na_first_1 - (skk * 100)
                    na_second_2 = na_second_1 - (skk * 100)
                    na_third_2 = na_first_2 + na_second_2

                    na_first_3 = na_first_2 - (skk * 100)
                    na_second_3 = na_second_2 - (skk * 100)
                    na_third_3 = na_first_3 + na_second_3

                    na_first_4 = na_first_3 - (skk * 100)
                    na_second_4 = na_second_3 - (skk * 100)
                    na_third_4 = na_first_4 + na_second_4

            else:
                ga_first_1 = np.random.randint(100, 400)
                ga_second_1 = np.random.randint(100, 400)
                ga_third_1 = ga_first_1 + ga_second_1

                ga_first_2 = ga_first_1 + (skk * smm_num)
                ga_second_2 = ga_second_1 + (skk * smm_num)
                ga_third_2 = ga_first_2 + ga_second_2

                ga_first_3 = ga_first_2 + (skk * smm_num)
                ga_second_3 = ga_second_2 + (skk * smm_num)
                ga_third_3 = ga_first_3 + ga_second_3

                ga_first_4 = ga_first_3 + (skk * smm_num)
                ga_second_4 = ga_second_3 + (skk * smm_num)
                ga_third_4 = ga_first_4 + ga_second_4

                if smm == "백":
                    na_first_1 = np.random.randint(100, 1000)
                    na_second_1 = np.random.randint(100, 1000)
                    na_third_1 = na_first_1 + na_second_1

                    na_first_2 = na_first_1 + (skk * 10)
                    na_second_2 = na_second_1 + (skk * 10)
                    na_third_2 = na_first_2 + na_second_2

                    na_first_3 = na_first_2 + (skk * 10)
                    na_second_3 = na_second_2 + (skk * 10)
                    na_third_3 = na_first_3 + na_second_3

                    na_first_4 = na_first_3 + (skk * 10)
                    na_second_4 = na_second_3 + (skk * 10)
                    na_third_4 = na_first_4 + na_second_4

                else:
                    na_first_1 = np.random.randint(100, 400)
                    na_second_1 = np.random.randint(100, 400)
                    na_third_1 = na_first_1 + na_second_1

                    na_first_2 = na_first_1 + (skk * 100)
                    na_second_2 = na_second_1 + (skk * 100)
                    na_third_2 = na_first_2 + na_second_2

                    na_first_3 = na_first_2 + (skk * 100)
                    na_second_3 = na_second_2 + (skk * 100)
                    na_third_3 = na_first_3 + na_second_3

                    na_first_4 = na_first_3 + (skk * 100)
                    na_second_4 = na_second_3 + (skk * 100)
                    na_third_4 = na_first_4 + na_second_4

            if ga_first_1 != ga_second_1 and na_first_1 != na_second_1 and ga_first_1 != na_first_1 and three_check(ga_third_1) and three_check(na_third_1):
                if three_check(ga_first_4) and three_check(ga_second_4) and three_check(ga_third_4):
                    if three_check(na_first_4) and three_check(na_second_4) and three_check(na_third_4):
                        break


    elif answer_choice == 1:
        ans = "나"

        saa = "더해지는 수"

        smm = ["백", "십"][np.random.randint(0, 2)]

        sqq = ["작아지고", "커지고"][np.random.randint(0, 2)]

        sbb = "더하는 수"

        if sqq == "작아지고":
            suu = "작아지는"
            sss = "작아"
        else:
            suu = "커지는"
            sss = "커"

        spp = "합은"

        if smm == "백":
            srr = skk * 200
            smm_num = 100
        else:
            srr = skk * 20
            smm_num = 10

        stt = "덧셈식"

        while True:
            if sqq == "작아지고":
                na_first_1 = np.random.randint(100, 1000)
                na_second_1 = np.random.randint(100, 1000)
                na_third_1 = na_first_1 + na_second_1

                na_first_2 = na_first_1 - (skk * smm_num)
                na_second_2 = na_second_1 - (skk * smm_num)
                na_third_2 = na_first_2 + na_second_2

                na_first_3 = na_first_2 - (skk * smm_num)
                na_second_3 = na_second_2 - (skk * smm_num)
                na_third_3 = na_first_3 + na_second_3

                na_first_4 = na_first_3 - (skk * smm_num)
                na_second_4 = na_second_3 - (skk * smm_num)
                na_third_4 = na_first_4 + na_second_4

                if smm == "백":
                    ga_first_1 = np.random.randint(100, 1000)
                    ga_second_1 = np.random.randint(100, 1000)
                    ga_third_1 = ga_first_1 + ga_second_1

                    ga_first_2 = ga_first_1 - (skk * 10)
                    ga_second_2 = ga_second_1 - (skk * 10)
                    ga_third_2 = ga_first_2 + ga_second_2

                    ga_first_3 = ga_first_2 - (skk * 10)
                    ga_second_3 = ga_second_2 - (skk * 10)
                    ga_third_3 = ga_first_3 + ga_second_3

                    ga_first_4 = ga_first_3 - (skk * 10)
                    ga_second_4 = ga_second_3 - (skk * 10)
                    ga_third_4 = ga_first_4 + ga_second_4

                else:
                    ga_first_1 = np.random.randint(100, 1000)
                    ga_second_1 = np.random.randint(100, 1000)
                    ga_third_1 = ga_first_1 + ga_second_1

                    ga_first_2 = ga_first_1 - (skk * 100)
                    ga_second_2 = ga_second_1 - (skk * 100)
                    ga_third_2 = ga_first_2 + ga_second_2

                    ga_first_3 = ga_first_2 - (skk * 100)
                    ga_second_3 = ga_second_2 - (skk * 100)
                    ga_third_3 = ga_first_3 + ga_second_3

                    ga_first_4 = ga_first_3 - (skk * 100)
                    ga_second_4 = ga_second_3 - (skk * 100)
                    ga_third_4 = ga_first_4 + ga_second_4

            else:
                na_first_1 = np.random.randint(100, 400)
                na_second_1 = np.random.randint(100, 400)
                na_third_1 = na_first_1 + na_second_1

                na_first_2 = na_first_1 + (skk * smm_num)
                na_second_2 = na_second_1 + (skk * smm_num)
                na_third_2 = na_first_2 + na_second_2

                na_first_3 = na_first_2 + (skk * smm_num)
                na_second_3 = na_second_2 + (skk * smm_num)
                na_third_3 = na_first_3 + na_second_3

                na_first_4 = na_first_3 + (skk * smm_num)
                na_second_4 = na_second_3 + (skk * smm_num)
                na_third_4 = na_first_4 + na_second_4

                if smm == "백":
                    ga_first_1 = np.random.randint(100, 1000)
                    ga_second_1 = np.random.randint(100, 1000)
                    ga_third_1 = ga_first_1 + ga_second_1

                    ga_first_2 = ga_first_1 + (skk * 10)
                    ga_second_2 = ga_second_1 + (skk * 10)
                    ga_third_2 = ga_first_2 + na_second_2

                    ga_first_3 = ga_first_2 + (skk * 10)
                    ga_second_3 = ga_second_2 + (skk * 10)
                    ga_third_3 = ga_first_3 + ga_second_3

                    ga_first_4 = ga_first_3 + (skk * 10)
                    ga_second_4 = ga_second_3 + (skk * 10)
                    ga_third_4 = ga_first_4 + ga_second_4

                else:
                    ga_first_1 = np.random.randint(100, 400)
                    ga_second_1 = np.random.randint(100, 400)
                    ga_third_1 = ga_first_1 + ga_second_1

                    ga_first_2 = ga_first_1 + (skk * 100)
                    ga_second_2 = ga_second_1 + (skk * 100)
                    ga_third_2 = ga_first_2 + ga_second_2

                    ga_first_3 = ga_first_2 + (skk * 100)
                    ga_second_3 = ga_second_2 + (skk * 100)
                    ga_third_3 = ga_first_3 + ga_second_3

                    ga_first_4 = ga_first_3 + (skk * 100)
                    ga_second_4 = ga_second_3 + (skk * 100)
                    ga_third_4 = ga_first_4 + ga_second_4

            if ga_first_1 != ga_second_1 and na_first_1 != na_second_1 and ga_first_1 != na_first_1 and three_check(
                    ga_third_1) and three_check(na_third_1):
                if three_check(ga_first_4) and three_check(ga_second_4) and three_check(ga_third_4):
                    if three_check(na_first_4) and three_check(na_second_4) and three_check(na_third_4):
                        break



    elif answer_choice == 2:
        ans = "다"

        saa = "빼어지는 수"

        smm = ["백", "십"][np.random.randint(0, 2)]

        sqq = ["작아지고", "커지고"][np.random.randint(0, 2)]

        sbb = "빼는 수"

        if sqq == "작아지고":
            suu = "커지는"
            sss = "작아"
        else:
            suu = "작아지는"
            sss = "커"

        spp = "차는"

        if smm == "백":
            srr = skk * 200
            smm_num = 100
        else:
            srr = skk * 20
            smm_num = 10

        stt = "뺄셈식"

        while True:
            if sqq == "작아지고":
                da_first_1 = np.random.randint(100, 1000)
                da_second_1 = np.random.randint(100, 1000)
                da_third_1 = da_first_1 - da_second_1

                da_first_2 = da_first_1 - (skk * smm_num)
                da_second_2 = da_second_1 + (skk * smm_num)
                da_third_2 = da_first_2 - da_second_2

                da_first_3 = da_first_2 - (skk * smm_num)
                da_second_3 = da_second_2 + (skk * smm_num)
                da_third_3 = da_first_3 - da_second_3

                da_first_4 = da_first_3 - (skk * smm_num)
                da_second_4 = da_second_3 + (skk * smm_num)
                da_third_4 = da_first_4 - da_second_4

                if smm == "백":
                    ra_first_1 = np.random.randint(100, 1000)
                    ra_second_1 = np.random.randint(100, 1000)
                    ra_third_1 = ra_first_1 - ra_second_1

                    ra_first_2 = ra_first_1 - (skk * 10)
                    ra_second_2 = ra_second_1 + (skk * 10)
                    ra_third_2 = ra_first_2 - ra_second_2

                    ra_first_3 = ra_first_2 - (skk * 10)
                    ra_second_3 = ra_second_2 + (skk * 10)
                    ra_third_3 = ra_first_3 - ra_second_3

                    ra_first_4 = ra_first_3 - (skk * 10)
                    ra_second_4 = ra_second_3 + (skk * 10)
                    ra_third_4 = ra_first_4 - ra_second_4

                else:
                    ra_first_1 = np.random.randint(100, 1000)
                    ra_second_1 = np.random.randint(100, 1000)
                    ra_third_1 = ra_first_1 - ra_second_1

                    ra_first_2 = ra_first_1 - (skk * 100)
                    ra_second_2 = ra_second_1 + (skk * 100)
                    ra_third_2 = ra_first_2 - ra_second_2

                    ra_first_3 = ra_first_2 - (skk * 100)
                    ra_second_3 = ra_second_2 + (skk * 100)
                    ra_third_3 = ra_first_3 - ra_second_3

                    ra_first_4 = ra_first_3 - (skk * 100)
                    ra_second_4 = ra_second_3 + (skk * 100)
                    ra_third_4 = ra_first_4 - ra_second_4

            else:
                da_first_1 = np.random.randint(100, 1000)
                da_second_1 = np.random.randint(100, 1000)
                da_third_1 = da_first_1 - da_second_1

                da_first_2 = da_first_1 + (skk * smm_num)
                da_second_2 = da_second_1 - (skk * smm_num)
                da_third_2 = da_first_2 - da_second_2

                da_first_3 = da_first_2 + (skk * smm_num)
                da_second_3 = da_second_2 - (skk * smm_num)
                da_third_3 = da_first_3 - da_second_3

                da_first_4 = da_first_3 + (skk * smm_num)
                da_second_4 = da_second_3 - (skk * smm_num)
                da_third_4 = da_first_4 - da_second_4

                if smm == "백":
                    ra_first_1 = np.random.randint(100, 1000)
                    ra_second_1 = np.random.randint(100, 1000)
                    ra_third_1 = ra_first_1 - ra_second_1

                    ra_first_2 = ra_first_1 + (skk * 10)
                    ra_second_2 = ra_second_1 - (skk * 10)
                    ra_third_2 = ra_first_2 - ra_second_2

                    ra_first_3 = ra_first_2 + (skk * 10)
                    ra_second_3 = ra_second_2 - (skk * 10)
                    ra_third_3 = ra_first_3 - ra_second_3

                    ra_first_4 = ra_first_3 + (skk * 10)
                    ra_second_4 = ra_second_3 - (skk * 10)
                    ra_third_4 = ra_first_4 - ra_second_4

                else:
                    ra_first_1 = np.random.randint(100, 1000)
                    ra_second_1 = np.random.randint(100, 1000)
                    ra_third_1 = ra_first_1 - ra_second_1

                    ra_first_2 = ra_first_1 + (skk * 100)
                    ra_second_2 = ra_second_1 - (skk * 100)
                    ra_third_2 = ra_first_2 - ra_second_2

                    ra_first_3 = ra_first_2 + (skk * 100)
                    ra_second_3 = ra_second_2 - (skk * 100)
                    ra_third_3 = ra_first_3 - ra_second_3

                    ra_first_4 = ra_first_3 + (skk * 100)
                    ra_second_4 = ra_second_3 - (skk * 100)
                    ra_third_4 = ra_first_4 - ra_second_4

            if da_first_1 != da_second_1 and ra_first_1 != ra_second_1 and da_first_1 != ra_first_1 and three_check(
                    da_third_1) and three_check(ra_third_1):
                if three_check(da_first_4) and three_check(da_second_4) and three_check(da_third_4):
                    if three_check(ra_first_4) and three_check(ra_second_4) and three_check(ra_third_4):
                        break

    else:
        ans = "라"

        saa = "빼어지는 수"

        smm = ["백", "십"][np.random.randint(0, 2)]

        sqq = ["작아지고", "커지고"][np.random.randint(0, 2)]

        sbb = "빼는 수"

        if sqq == "작아지고":
            suu = "커지는"
            sss = "작아"
        else:
            suu = "작아지는"
            sss = "커"

        spp = "차는"

        if smm == "백":
            srr = skk * 200
            smm_num = 100
        else:
            srr = skk * 20
            smm_num = 10

        stt = "뺄셈식"

        while True:
            if sqq == "작아지고":
                ra_first_1 = np.random.randint(100, 1000)
                ra_second_1 = np.random.randint(100, 1000)
                ra_third_1 = ra_first_1 - ra_second_1

                ra_first_2 = ra_first_1 - (skk * smm_num)
                ra_second_2 = ra_second_1 + (skk * smm_num)
                ra_third_2 = ra_first_2 - ra_second_2

                ra_first_3 = ra_first_2 - (skk * smm_num)
                ra_second_3 = ra_second_2 + (skk * smm_num)
                ra_third_3 = ra_first_3 - ra_second_3

                ra_first_4 = ra_first_3 - (skk * smm_num)
                ra_second_4 = ra_second_3 + (skk * smm_num)
                ra_third_4 = ra_first_4 - ra_second_4

                if smm == "백":
                    da_first_1 = np.random.randint(100, 1000)
                    da_second_1 = np.random.randint(100, 1000)
                    da_third_1 = da_first_1 - da_second_1

                    da_first_2 = da_first_1 - (skk * 10)
                    da_second_2 = da_second_1 + (skk * 10)
                    da_third_2 = da_first_2 - da_second_2

                    da_first_3 = da_first_2 - (skk * 10)
                    da_second_3 = da_second_2 + (skk * 10)
                    da_third_3 = da_first_3 - da_second_3

                    da_first_4 = da_first_3 - (skk * 10)
                    da_second_4 = da_second_3 + (skk * 10)
                    da_third_4 = da_first_4 - da_second_4

                else:
                    da_first_1 = np.random.randint(100, 1000)
                    da_second_1 = np.random.randint(100, 1000)
                    da_third_1 = da_first_1 - da_second_1

                    da_first_2 = da_first_1 - (skk * 100)
                    da_second_2 = da_second_1 + (skk * 100)
                    da_third_2 = da_first_2 - da_second_2

                    da_first_3 = da_first_2 - (skk * 100)
                    da_second_3 = da_second_2 + (skk * 100)
                    da_third_3 = da_first_3 - da_second_3

                    da_first_4 = da_first_3 - (skk * 100)
                    da_second_4 = da_second_3 + (skk * 100)
                    da_third_4 = da_first_4 - da_second_4

            else:
                ra_first_1 = np.random.randint(100, 1000)
                ra_second_1 = np.random.randint(100, 1000)
                ra_third_1 = ra_first_1 - ra_second_1

                ra_first_2 = ra_first_1 + (skk * smm_num)
                ra_second_2 = ra_second_1 - (skk * smm_num)
                ra_third_2 = ra_first_2 - ra_second_2

                ra_first_3 = ra_first_2 + (skk * smm_num)
                ra_second_3 = ra_second_2 - (skk * smm_num)
                ra_third_3 = ra_first_3 - ra_second_3

                ra_first_4 = ra_first_3 + (skk * smm_num)
                ra_second_4 = ra_second_3 - (skk * smm_num)
                ra_third_4 = ra_first_4 - ra_second_4

                if smm == "백":
                    da_first_1 = np.random.randint(100, 1000)
                    da_second_1 = np.random.randint(100, 1000)
                    da_third_1 = da_first_1 - da_second_1

                    da_first_2 = da_first_1 + (skk * 10)
                    da_second_2 = da_second_1 - (skk * 10)
                    da_third_2 = da_first_2 - da_second_2

                    da_first_3 = da_first_2 + (skk * 10)
                    da_second_3 = da_second_2 - (skk * 10)
                    da_third_3 = da_first_3 - da_second_3

                    da_first_4 = da_first_3 + (skk * 10)
                    da_second_4 = da_second_3 - (skk * 10)
                    da_third_4 = da_first_4 - da_second_4

                else:
                    da_first_1 = np.random.randint(100, 1000)
                    da_second_1 = np.random.randint(100, 1000)
                    da_third_1 = da_first_1 - da_second_1

                    da_first_2 = da_first_1 + (skk * 100)
                    da_second_2 = da_second_1 - (skk * 100)
                    da_third_2 = da_first_2 - da_second_2

                    da_first_3 = da_first_2 + (skk * 100)
                    da_second_3 = da_second_2 - (skk * 100)
                    da_third_3 = da_first_3 - da_second_3

                    da_first_4 = da_first_3 + (skk * 100)
                    da_second_4 = da_second_3 - (skk * 100)
                    da_third_4 = da_first_4 - da_second_4

            if da_first_1 != da_second_1 and ra_first_1 != ra_second_1 and da_first_1 != ra_first_1 and three_check(
                    da_third_1) and three_check(ra_third_1):
                if three_check(da_first_4) and three_check(da_second_4) and three_check(da_third_4):
                    if three_check(ra_first_4) and three_check(ra_second_4) and three_check(ra_third_4):
                        break

    if answer_choice == 0 or answer_choice == 1:
        while True:
            random_da_number = [10, 100][np.random.randint(0, 2)]
            random_da_calculate = np.random.randint(0, 2)

            if random_da_calculate == 0:
                da_first_1 = np.random.randint(100, 1000)
                da_second_1 = np.random.randint(100, 1000)
                da_third_1 = da_first_1 - da_second_1

                da_first_2 = da_first_1 - (skk * random_da_number)
                da_second_2 = da_second_1 + (skk * random_da_number)
                da_third_2 = da_first_2 - da_second_2

                da_first_3 = da_first_2 - (skk * random_da_number)
                da_second_3 = da_second_2 + (skk * random_da_number)
                da_third_3 = da_first_3 - da_second_3

                da_first_4 = da_first_3 - (skk * random_da_number)
                da_second_4 = da_second_3 + (skk * random_da_number)
                da_third_4 = da_first_4 - da_second_4

            else:
                da_first_1 = np.random.randint(100, 1000)
                da_second_1 = np.random.randint(100, 1000)
                da_third_1 = da_first_1 - da_second_1

                da_first_2 = da_first_1 + (skk * random_da_number)
                da_second_2 = da_second_1 - (skk * random_da_number)
                da_third_2 = da_first_2 - da_second_2

                da_first_3 = da_first_2 + (skk * random_da_number)
                da_second_3 = da_second_2 - (skk * random_da_number)
                da_third_3 = da_first_3 - da_second_3

                da_first_4 = da_first_3 + (skk * random_da_number)
                da_second_4 = da_second_3 - (skk * random_da_number)
                da_third_4 = da_first_4 - da_second_4

            if three_check(da_third_1) and three_check(da_first_4) and three_check(da_second_4) and three_check(da_third_4):
                break

        if random_da_number == 10:
            random_ra_number = 100
        else:
            random_ra_number = 10

        while True:
            random_ra_calculate = np.random.randint(0, 2)

            if random_ra_calculate == 0:
                ra_first_1 = np.random.randint(100, 1000)
                ra_second_1 = np.random.randint(100, 1000)
                ra_third_1 = ra_first_1 - ra_second_1

                ra_first_2 = ra_first_1 - (skk * random_ra_number)
                ra_second_2 = ra_second_1 + (skk * random_ra_number)
                ra_third_2 = ra_first_2 - ra_second_2

                ra_first_3 = ra_first_2 - (skk * random_ra_number)
                ra_second_3 = ra_second_2 + (skk * random_ra_number)
                ra_third_3 = ra_first_3 - ra_second_3

                ra_first_4 = ra_first_3 - (skk * random_ra_number)
                ra_second_4 = ra_second_3 + (skk * random_ra_number)
                ra_third_4 = ra_first_4 - ra_second_4

            else:
                ra_first_1 = np.random.randint(100, 1000)
                ra_second_1 = np.random.randint(100, 1000)
                ra_third_1 = ra_first_1 - ra_second_1

                ra_first_2 = ra_first_1 + (skk * random_ra_number)
                ra_second_2 = ra_second_1 - (skk * random_ra_number)
                ra_third_2 = ra_first_2 - ra_second_2

                ra_first_3 = ra_first_2 + (skk * random_ra_number)
                ra_second_3 = ra_second_2 - (skk * random_ra_number)
                ra_third_3 = ra_first_3 - ra_second_3

                ra_first_4 = ra_first_3 + (skk * random_ra_number)
                ra_second_4 = ra_second_3 - (skk * random_ra_number)
                ra_third_4 = ra_first_4 - ra_second_4

            if three_check(ra_third_1) and three_check(ra_first_4) and three_check(ra_second_4) and three_check(
                    ra_third_4):
                break

    elif answer_choice == 2 or answer_choice == 3:
        while True:
            random_ga_number = [10, 100][np.random.randint(0, 2)]
            random_ga_calculate = np.random.randint(0, 2)

            if random_ga_calculate == 0:
                ga_first_1 = np.random.randint(100, 1000)
                ga_second_1 = np.random.randint(100, 1000)
                ga_third_1 = ga_first_1 + ga_second_1

                ga_first_2 = ga_first_1 + (skk * random_ga_number)
                ga_second_2 = ga_second_1 + (skk * random_ga_number)
                ga_third_2 = ga_first_2 + ga_second_2

                ga_first_3 = ga_first_2 + (skk * random_ga_number)
                ga_second_3 = ga_second_2 + (skk * random_ga_number)
                ga_third_3 = ga_first_3 + ga_second_3

                ga_first_4 = ga_first_3 + (skk * random_ga_number)
                ga_second_4 = ga_second_3 + (skk * random_ga_number)
                ga_third_4 = ga_first_4 + ga_second_4

            else:
                ga_first_1 = np.random.randint(100, 1000)
                ga_second_1 = np.random.randint(100, 1000)
                ga_third_1 = ga_first_1 + ga_second_1

                ga_first_2 = ga_first_1 - (skk * random_ga_number)
                ga_second_2 = ga_second_1 - (skk * random_ga_number)
                ga_third_2 = ga_first_2 + ga_second_2

                ga_first_3 = ga_first_2 - (skk * random_ga_number)
                ga_second_3 = ga_second_2 - (skk * random_ga_number)
                ga_third_3 = ga_first_3 + ga_second_3

                ga_first_4 = ga_first_3 - (skk * random_ga_number)
                ga_second_4 = ga_second_3 - (skk * random_ga_number)
                ga_third_4 = ga_first_4 + ga_second_4

            if three_check(ga_third_1) and three_check(ga_first_4) and three_check(ga_second_4) and three_check(ga_third_4):
                break

        if random_ga_number == 10:
            random_na_number = 100
        else:
            random_na_number = 10

        while True:
            random_na_calculate = np.random.randint(0, 2)

            if random_na_calculate == 0:
                na_first_1 = np.random.randint(100, 1000)
                na_second_1 = np.random.randint(100, 1000)
                na_third_1 = na_first_1 + na_second_1

                na_first_2 = na_first_1 + (skk * random_na_number)
                na_second_2 = na_second_1 + (skk * random_na_number)
                na_third_2 = na_first_2 + na_second_2

                na_first_3 = na_first_2 + (skk * random_na_number)
                na_second_3 = na_second_2 + (skk * random_na_number)
                na_third_3 = na_first_3 + na_second_3

                na_first_4 = na_first_3 + (skk * random_na_number)
                na_second_4 = na_second_3 + (skk * random_na_number)
                na_third_4 = na_first_4 + na_second_4

            else:
                na_first_1 = np.random.randint(100, 1000)
                na_second_1 = np.random.randint(100, 1000)
                na_third_1 = na_first_1 + na_second_1

                na_first_2 = na_first_1 - (skk * random_na_number)
                na_second_2 = na_second_1 - (skk * random_na_number)
                na_third_2 = na_first_2 + na_second_2

                na_first_3 = na_first_2 - (skk * random_na_number)
                na_second_3 = na_second_2 - (skk * random_na_number)
                na_third_3 = na_first_3 + na_second_3

                na_first_4 = na_first_3 - (skk * random_na_number)
                na_second_4 = na_second_3 - (skk * random_na_number)
                na_third_4 = na_first_4 + na_second_4

            if three_check(na_third_1) and three_check(na_first_4) and three_check(na_second_4) and three_check(
                    na_third_4):
                break


    stem = stem.format(ga_first_1=ga_first_1, ga_second_1=ga_second_1, ga_third_1=ga_third_1, ga_first_2=ga_first_2, ga_second_2=ga_second_2, ga_third_2=ga_third_2,
                       ga_first_3=ga_first_3, ga_second_3=ga_second_3, ga_third_3=ga_third_3, ga_first_4=ga_first_4, ga_second_4=ga_second_4, ga_third_4=ga_third_4,
                       na_first_1=na_first_1, na_second_1=na_second_1, na_third_1=na_third_1, na_first_2=na_first_2, na_second_2=na_second_2, na_third_2=na_third_2,
                       na_first_3=na_first_3, na_second_3=na_second_3, na_third_3=na_third_3, na_first_4=na_first_4, na_second_4=na_second_4, na_third_4=na_third_4,
                       da_first_1=da_first_1, da_second_1=da_second_1, da_third_1=da_third_1, da_first_2=da_first_2,
                       da_second_2=da_second_2, da_third_2=da_third_2,
                       da_first_3=da_first_3, da_second_3=da_second_3, da_third_3=da_third_3, da_first_4=da_first_4,
                       da_second_4=da_second_4, da_third_4=da_third_4,
                       ra_first_1=ra_first_1, ra_second_1=ra_second_1, ra_third_1=ra_third_1, ra_first_2=ra_first_2,
                       ra_second_2=ra_second_2, ra_third_2=ra_third_2,
                       ra_first_3=ra_first_3, ra_second_3=ra_second_3, ra_third_3=ra_third_3, ra_first_4=ra_first_4,
                       ra_second_4=ra_second_4, ra_third_4=ra_third_4,
                       saa=saa, smm=smm, skk=skk, sqq=sqq, sbb=sbb, suu=suu, spp=spp, srr=srr, sss=sss)
    answer = answer.format(ans=ans)
    comment = comment.format(stt=stt, saa=saa, smm=smm, skk=skk, sqq=sqq, sbb=sbb, suu=suu, ans=ans)

    return stem, answer, comment


    # stem = "가~라의 계산식을 보고 설명에 맞는 계산식을 찾아 기호를 써 보세요.\n" \
    #        "                    가 $$수식$${rk1} ` + ` {rk2} ` = ` {rk12}$$/수식$$    나 $$수식$${sk1} ` + ` {sk2} ` = ` {sk12}$$/수식$$\n"\
    #        "                       $$수식$${nrk1} ` + ` {nrk2} ` = ` {nrk12}$$/수식$$     $$수식$${nsk1} ` + ` {nsk2} ` = ` {nsk12}$$/수식$$\n"\
    #        "                       $$수식$${nrk3} ` + ` {nrk4} ` = ` {nrk34}$$/수식$$     $$수식$${nsk3} ` + ` {nsk4} ` = ` {nsk34}$$/수식$$\n"\
    #        "                       $$수식$${nrk5} ` + ` {nrk6} ` = ` {nrk56}$$/수식$$     $$수식$${nsk5} ` + ` {nsk6} ` = ` {nsk56}$$/수식$$\n"\
    #        "                    다 $$수식$${ek1} ` - ` {ek2} ` = ` {ek12}$$/수식$$    라 $$수식$${fk1} ` - ` {fk2} ` = ` {fk12}$$/수식$$\n"\
    #        "                       $$수식$${nek1} ` - ` {nek2} ` = ` {nek12}$$/수식$$     $$수식$${nfk1} ` - ` {nfk2} ` = ` {nfk12}$$/수식$$\n"\
    #        "                       $$수식$${nek3} ` - ` {nek4} ` = ` {nek34}$$/수식$$     $$수식$${nfk3} ` - ` {nfk4} ` = ` {nfk34}$$/수식$$\n"\
    #        "                       $$수식$${nek5} ` - ` {nek6} ` = ` {nek56}$$/수식$$     $$수식$${nfk5} ` - ` {nfk6} ` = ` {nfk56}$$/수식$$\n"\
    #        "$$표$${sa}는 {sm}의 자리 수가 {sk}씩 {sq} {sb}는 {sm}의 자리 수가 {sk}씩 {su} 두 수의 {sp} {sr}씩 {ss}집니다.$$/표$$\n"
    #
    #
    #
    # lista = ["빼어지는 수", "더해지는 수"]
    #
    # sa = np.random.choice(lista)
    #
    # if sa == "빼어지는 수":
    #     sb = "빼는 수"
    #     st = "뺄셈식"
    # elif sa == "더해지는 수":
    #     sb = "더하는 수"
    #     st = "덧셈식"
    #
    # listm = ["백", "십"]
    # listk = ["1", "2"]
    # listq = ["작아지고", "커지고"]
    #
    # sm = np.random.choice(listm)
    # sk = np.random.choice(listk)
    # sq = np.random.choice(listq)
    #
    # if st == "뺄셈식":
    #     if sq == "작아지고":
    #         su = "커지는"
    #     elif sq == "커지고":
    #         su = "작아지는"
    # elif st == "덧셈식":
    #     if sq == "작아지고":
    #         su = "작아지는"
    #     elif sq == "커지고":
    #         su = "커지는"
    #
    # if st == "뺄셈식":
    #     sp = "차는"
    # elif st == "덧셈식":
    #     sp = "합은"
    #
    # if sm == "백":
    #     sy = int(sk) * 100
    # elif sm == "십":
    #     sy = int(sk) * 10
    #
    # sr = 2 * sy
    #
    # if sq == "작아지고":
    #     ss = "작아"
    # elif sq == "커지고":
    #     ss = "커"
    #
    # while True:
    #     while True:
    #         rk1 = np.random.randint(100, 1000)
    #         rk2 = np.random.randint(100, 1000)
    #         sk1 = np.random.randint(100, 1000)
    #         sk2 = np.random.randint(100, 1000)
    #         ek1 = np.random.randint(100, 1000)
    #         ek2 = np.random.randint(100, 1000)
    #         fk1 = np.random.randint(100, 1000)
    #         fk2 = np.random.randint(100, 1000)
    #         if rk1 != rk2 != sk1 != rk2 != ek1 != rk2 != fk1 != rk2:
    #             break
    #
    #     listrk1 = [int(rk1 + (int(sk) * 100)), int(rk1 - (int(sk) * 100))]
    #     listrk2 = [int(rk2 + (int(sk) * 100)), int(rk2 - (int(sk) * 100))]
    #
    #     listsk1 = [int(sk1 + (int(sk) * 10)), int(sk1 - (int(sk) * 10))]
    #     listsk2 = [int(sk2 + (int(sk) * 10)), int(sk2 - (int(sk) * 10))]
    #
    #     listek1 = [int(ek1 + (int(sk) * 100)), int(ek1 - (int(sk) * 100))]
    #     listek2 = [int(ek2 + (int(sk) * 100)), int(ek2 - (int(sk) * 100))]
    #
    #     listfk1 = [int(fk1 + (int(sk) * 10)), int(fk1 - (int(sk) * 10))]
    #     listfk2 = [int(fk2 + (int(sk) * 10)), int(fk2 - (int(sk) * 10))]
    #
    #     nrk1 = np.random.choice(listrk1)
    #     nrk2 = np.random.choice(listrk2)
    #
    #     nsk1 = np.random.choice(listsk1)
    #     nsk2 = np.random.choice(listsk2)
    #
    #     nek1 = np.random.choice(listek1)
    #     nek2 = np.random.choice(listek2)
    #
    #     nfk1 = np.random.choice(listfk1)
    #     nfk2 = np.random.choice(listfk2)
    #
    #     sz = ""
    #     if sa == "더해지는 수" and sm == "백" and sq == "커지고" and sb == "더하는 수" and su == "커지는":
    #         nrk1 = listrk1[0]
    #         nrk2 = listrk2[0]
    #         sz = "가"
    #     elif sa == "더해지는 수" and sm == "백" and sq == "커지고" and sb == "더하는 수" and su == "작아지는":
    #         nrk1 = listrk1[0]
    #         nrk2 = listrk2[1]
    #         sz = "가"
    #     elif sa == "더해지는 수" and sm == "백" and sq == "작아지고" and sb == "더하는 수" and su == "커지는":
    #         nrk1 = listrk1[1]
    #         nrk2 = listrk2[0]
    #         sz = "가"
    #     elif sb == "더해지는 수" and sm == "백" and sq == "작아지고" and "더하는 수" and su == "작아지는":
    #         nrk1 = listrk1[1]
    #         nrk2 = listrk2[1]
    #         sz = "가"
    #
    #     if sa == "더해지는 수" and sm == "십" and sq == "커지고" and sb == "더하는 수" and su == "커지는":
    #         nsk1 = listsk1[0]
    #         nsk2 = listsk2[0]
    #         sz = "나"
    #     elif sa == "더해지는 수" and sm == "십" and sq == "커지고" and sb == "더하는 수" and su == "작아지는":
    #         nsk1 = listsk1[0]
    #         nsk2 = listsk2[1]
    #         sz = "나"
    #     elif sa == "더해지는 수" and sm == "십" and sq == "작아지고" and sb == "더하는 수" and su == "커지는":
    #         nsk1 = listsk1[1]
    #         nsk2 = listsk2[0]
    #         sz = "나"
    #     elif sb == "더해지는 수" and sm == "십" and sq == "작아지고" and "더하는 수" and su == "작아지는":
    #         nsk1 = listsk1[1]
    #         nsk2 = listsk2[1]
    #         sz = "나"
    #
    #     if sa == "빼어지는 수" and sm == "백" and sq == "커지고" and sb == "빼는 수" and su == "커지는":
    #         nek1 = listek1[0]
    #         nek2 = listek2[0]
    #         sz = "다"
    #     elif sa == "빼어지는 수" and sm == "백" and sq == "커지고" and sb == "빼는 수" and su == "작아지는":
    #         nek1 = listek1[0]
    #         nek2 = listek2[1]
    #         sz = "다"
    #     elif sa == "빼어지는 수" and sm == "백" and sq == "작아지고" and sb == "빼는 수" and su == "커지는":
    #         nek1 = listek1[1]
    #         nek2 = listek2[0]
    #         sz = "다"
    #     elif sa == "빼어지는 수" and sm == "백" and sq == "작아지고" and sb == "빼는 수" and su == "작아지는":
    #         nek1 = listek1[1]
    #         nek2 = listek2[1]
    #         sz = "다"
    #
    #     if sa == "빼어지는 수" and sm == "십" and sq == "커지고" and sb == "빼는 수" and su == "커지는":
    #         nfk1 = listfk1[0]
    #         nfk2 = listfk2[0]
    #         sz = "라"
    #     elif sa == "빼어지는 수" and sm == "십" and sq == "커지고" and sb == "빼는 수" and su == "작아지는":
    #         nfk1 = listfk1[0]
    #         nfk2 = listfk2[1]
    #         sz = "라"
    #     elif sa == "빼어지는 수" and sm == "십" and sq == "작아지고" and sb == "빼는 수" and su == "커지는":
    #         nfk1 = listfk1[1]
    #         nfk2 = listfk2[0]
    #         sz = "라"
    #     elif sa == "빼어지는 수" and sm == "십" and sq == "작아지고" and sb == "빼는 수" and su == "작아지는":
    #         nfk1 = listfk1[1]
    #         nfk2 = listfk2[1]
    #         sz = "라"
    #
    #
    #     if nrk1 == listrk1[0]:
    #         nrk3 = int(nrk1 + (int(sk) * 100))
    #         nrk5 = int(nrk3 + (int(sk) * 100))
    #     elif nrk1 == listrk1[1]:
    #         nrk3 = int(nrk1 - (int(sk) * 100))
    #         nrk5 = int(nrk3 - (int(sk) * 100))
    #
    #     if nrk2 == listrk2[0]:
    #         nrk4 = int(nrk2 + (int(sk) * 100))
    #         nrk6 = int(nrk4 + (int(sk) * 100))
    #     elif nrk2 == listrk2[1]:
    #         nrk4 = int(nrk2 - (int(sk) * 100))
    #         nrk6 = int(nrk4 - (int(sk) * 100))
    #
    #     if nsk1 == listsk1[0]:
    #         nsk3 = int(nsk1 + (int(sk) * 10))
    #         nsk5 = int(nsk3 + (int(sk) * 10))
    #     elif nsk1 == listsk1[1]:
    #         nsk3 = int(nsk1 - (int(sk) * 10))
    #         nsk5 = int(nsk3 - (int(sk) * 10))
    #
    #     if nsk2 == listsk2[0]:
    #         nsk4 = int(nsk2 + (int(sk) * 10))
    #         nsk6 = int(nsk4 + (int(sk) * 10))
    #     elif nsk2 == listsk2[1]:
    #         nsk4 = int(nsk2 - (int(sk) * 10))
    #         nsk6 = int(nsk4 - (int(sk) * 10))
    #
    #     if nek1 == listek1[0]:
    #         nek3 = int(nek1 + (int(sk) * 100))
    #         nek5 = int(nek3 + (int(sk) * 100))
    #     elif nek1 == listek1[1]:
    #         nek3 = int(nek1 - (int(sk) * 100))
    #         nek5 = int(nek3 - (int(sk) * 100))
    #
    #     if nek2 == listek2[0]:
    #         nek4 = int(nek2 + (int(sk) * 100))
    #         nek6 = int(nek4 + (int(sk) * 100))
    #     elif nek2 == listek2[1]:
    #         nek4 = int(nek2 - (int(sk) * 100))
    #         nek6 = int(nek4 - (int(sk) * 100))
    #
    #     if nfk1 == listfk1[0]:
    #         nfk3 = int(nfk1 + (int(sk) * 10))
    #         nfk5 = int(nfk3 + (int(sk) * 10))
    #     elif nfk1 == listfk1[1]:
    #         nfk3 = int(nfk1 - (int(sk) * 10))
    #         nfk5 = int(nfk3 - (int(sk) * 10))
    #
    #     if nfk2 == listfk2[0]:
    #         nfk4 = int(nfk2 + (int(sk) * 10))
    #         nfk6 = int(nfk4 + (int(sk) * 10))
    #     elif nfk2 == listfk2[1]:
    #         nfk4 = int(nfk2 - (int(sk) * 10))
    #         nfk6 = int(nfk4 - (int(sk) * 10))
    #
    #     if rk1 + rk2 > 0 and nrk1 + nrk2 > 0 and nrk3 + nrk4 > 0 and nrk5 + nrk6 > 0 and sk1 + sk2 > 0 and nsk1 + nsk2 > 0 and nsk3 + nsk4 > 0 and nsk5 + nsk6 > 0 and \
    #             nrk1 > 0 and nrk2 > 0 and nrk3 > 0 and nrk4 > 0 and nrk5 > 0 and nrk6 > 0 and \
    #             nsk1 > 0 and nsk2 > 0 and nsk3 > 0 and nsk4 > 0 and nsk5 > 0 and nsk6 > 0 and \
    #             nek1 > 0 and nek2 > 0 and nek3 > 0 and nek4 > 0 and nek5 > 0 and nek6 > 0 and \
    #             nfk1 > 0 and nfk2 > 0 and nfk3 > 0 and nfk4 > 0 and nfk5 > 0 and nfk6 > 0 and \
    #             ek1 - ek2 > 0 and nek1 - nek2 > 0 and nek3 - nek4 > 0 and nek5 - nek6 > 0 and fk1 - fk2 > 0 and nfk1 - nfk2 > 0 and nfk3 - nfk4 > 0 and nfk5 - nfk6 > 0:
    #         break
    #
    # rk12 = rk1 + rk2
    # nrk12 = nrk1 + nrk2
    # nrk34 = nrk3 + nrk4
    # nrk56 = nrk5 + nrk6
    # sk12 = sk1 + sk2
    # nsk12 = nsk1 + nsk2
    # nsk34 = nsk3 + nsk4
    # nsk56 = nsk5 + nsk6
    # ek12 = ek1 - ek2
    # nek12 = nek1 - nek2
    # nek34 = nek3 - nek4
    # nek56 = nek5 - nek6
    # fk12 = fk1 - fk2
    # nfk12 = nfk1 - nfk2
    # nfk34 = nfk3 - nfk4
    # nfk56 = nfk5 - nfk6
    #
    # stem = stem.format(sa=sa, sm=sm, sk=sk, sq=sq, sb=sb, su=su, sp=sp, sr=sr, ss=ss, rk1=rk1, rk2=rk2, rk12=rk12, nrk12=nrk12, nrk1=nrk1, nrk2=nrk2, nrk3=nrk3, nrk4=nrk4, nrk5=nrk5, nrk6=nrk6, nrk34=nrk34, nrk56=nrk56, nsk34=nsk34, nsk56=nsk56,
    #                    sk1=sk1, sk2=sk2, sk12=sk12, nsk12=nsk12, nsk1=nsk1, nsk2=nsk2, nsk3=nsk3, nsk4=nsk4, nsk5=nsk5, nsk6=nsk6, ek1=ek1, ek2=ek2, ek12=ek12, nek12=nek12, nek1=nek1, nek2=nek2, nek3=nek3, nek4=nek4, nek5=nek5, nek6=nek6,
    #                    fk1=fk1, fk2=fk2, fk12=fk12, nfk12=nfk12, nfk1=nfk1, nfk2=nfk2, nfk3=nfk3, nfk4=nfk4, nfk5=nfk5, nfk6=nfk6, nek34=nek34, nek56=nek56, nfk34=nfk34, nfk56=nfk56)
    # answer = answer.format(sz=sz)
    # comment = comment.format(st=st, sa=sa, sm=sm, sk=sk, sb=sb, sz=sz)























# 4-1-6-10
def findingrule416_Stem_004():
    stem = "덧셈식의 규칙에 따라 {onecha}, {twocha} 안에 알맞은 수를 차례대로 써넣으세요.\n$$표$$$$수식$${sc} ` + ` {sb} ` = `{sd}$$/수식$$\n$$수식$${sc1} ` + ` {sb1} ` = `{sd1}$$/수식$$\n$$수식$${sc2} ` + ` {sb2} ` = `{sd2}$$/수식$$\n$$수식$${sc3} ` + ` {sb3} ` = `{sd3}$$/수식$$\n$$수식$${sc4} ` + ` {sb4} ` = `{sd4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$, $$수식$${ans1}$$/수식$$\n"
    comment = "(해설)\n" \
              "더해지는 수가 $$수식$${sa}$$/수식$$씩 커지고 더하는 수가 일정하면 합은 $$수식$${sa}$$/수식$$씩 커집니다.\n\n"


    sa = np.random.randint(100, 10000)
    sb = np.random.randint(100, 1000)
    sc = np.random.randint(100, 1000)

    ans = sb

    sd = sc + sb

    sb1 = sb
    sb2 = sb
    sb3 = sb
    sb4 = sb

    sc1 = sc + sa
    sc2 = sc + 2 * sa
    sc3 = sc + 3 * sa
    sc4 = sc + 4 * sa

    sd1 = sd + sa
    sd2 = sd + 2 * sa
    sd3 = sd + 3 * sa
    sd4 = sd + 4 * sa

    onecha = "①"
    twocha = "②"

    while True:
        rn = np.random.randint(0, 5)
        rn2 = np.random.randint(0, 5)
        if rn != rn2:
            break


    list1 = [sb, sb1, sb2, sb3, sb4]
    list1[rn] = "①"
    sb, sb1, sb2, sb3, sb4 = list1

    list2 = [sd, sd1, sd2, sd3, sd4]
    ans1 = list2[rn2]
    list2[rn2] = "②"
    sd, sd1, sd2, sd3, sd4 = list2

    stem = stem.format(sc=sc, sb=sb, sb1=sb1, sb2=sb2, sb3=sb3, sb4=sb4, sd=sd, sc1=sc1, sc2=sc2, sc3=sc3, sc4=sc4, sd1=sd1, sd2=sd2, sd3=sd3, sd4=sd4, onecha=onecha, twocha=twocha)
    answer = answer.format(ans=ans, ans1=ans1)
    comment = comment.format(sa=sa)

    return stem, answer, comment























# 4-1-6-11
def findingrule416_Stem_005():
    stem = "곱셈식의 규칙을 이용하여 규칙적인 나눗셈식을 만들어 보세요.\n$$표$$$$수식$${sa} ` times ` {sb} ` = ` {sc}$$/수식$$\n$$수식$${sd} ` times ` {sb} ` = ` {se}$$/수식$$\n$$수식$${sf} ` times ` {sb} ` = ` {sg}$$/수식$$$$/표$$\n$$수식$${box1}$$/수식$$ $$수식$$```` div ````$$/수식$$ $$수식$${box2}$$/수식$$ $$수식$$```` = ````{sb}$$/수식$$\n$$수식$${box3}$$/수식$$ $$수식$$```` div ````$$/수식$$ $$수식$${box4}$$/수식$$ $$수식$$```` = ```` {sb}$$/수식$$\n$$수식$${box5}$$/수식$$ $$수식$$```` div ````$$/수식$$ $$수식$${box6}$$/수식$$ $$수식$$```` = ```` {sb}$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${sc}$$/수식$$, ㉡ $$수식$${sa}$$/수식$$, ㉢ $$수식$${se}$$/수식$$, ㉣ $$수식$${sd}$$/수식$$, ㉤ $$수식$${sg}$$/수식$$, ㉥ $$수식$${sf}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa} ` times ` {sb} ` = ` {sc}$$/수식$$ → $$수식$${sc} ` div ` {sa} ` = ` {sb}$$/수식$$\n" \
              "$$수식$${sd} ` times ` {sb} ` = ` {se}$$/수식$$ → $$수식$${se} ` div ` {sd} ` = ` {sb}$$/수식$$\n" \
              "$$수식$${sf} ` times ` {sb} ` = ` {sg}$$/수식$$ → $$수식$${sg} ` div ` {sf} ` = ` {sb}$$/수식$$\n\n"


    saa = np.random.randint(1, 10)
    sbb = np.random.randint(1, 10)
    sa=(100*saa) + sbb

    sad = np.random.randint(1, 10)
    sbd = np.random.randint(1, 10)
    sd=(1000*sad) + sbd

    saf = np.random.randint(1, 10)
    sbf = np.random.randint(1, 10)
    sf=(10000*saf) + sbf

    sb = np.random.randint(2, 10)
    sc = sa*sb
    se = sd*sb
    sg = sf*sb

    box1 = "box{%s````````````````````}" % "㉠"
    box2 = "box{%s````````````````````}" % "㉡"
    box3 = "box{%s````````````````````}" % "㉢"
    box4 = "box{%s````````````````````}" % "㉣"
    box5 = "box{%s````````````````````}" % "㉤"
    box6 = "box{%s````````````````````}" % "㉥"

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, box1=box1, box2=box2, box3=box3, box4=box4, box5=box5, box6=box6)
    answer = answer.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg)

    return stem, answer, comment
























# 4-1-6-14
def findingrule416_Stem_006():
    stem = "규칙에 따라 $$수식$${sa} ` div ` {sb}$$/수식$$의 몫을 구해 보세요.\n$$표$$$$수식$${sg} ` div ` {sb} ` = ` {sc}$$/수식$$\n$$수식$${sh} ` div ` {sb} ` = ` {sd}$$/수식$$\n$$수식$${si} ` div ` {sb} ` = ` {se}$$/수식$$\n$$수식$${sj} ` div ` {sb} ` = ` {sf}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${sz}$$/수식$$\n"
    comment = "(해설)\n" \
              "나누어지는 수는 $$수식$${sg} ` = ` {sg} ` times ` 1 $$/수식$$, $$수식$${sh} ` = ` {sg} ` times `  2 $$/수식$$, " \
              "$$수식$${si} ` = ` {sg} ` times ` 3 $$/수식$$, $$수식$${sj} ` = ` {sg} ` times ` 4 $$/수식$$로\n" \
              "$$수식$${sg}$$/수식$$의 $$수식$$1$$/수식$$배, $$수식$$2$$/수식$$배, $$수식$$3$$/수식$$배, $$수식$$4$$/수식$$배가 되고,\n" \
              "나누는 수는 $$수식$${sb}$$/수식$${ro1} 일정할 때 몫은 " \
              "$$수식$${sc} ` times ` 1 ` = ` {sc}$$/수식$$, $$수식$${sc} ` times ` 2 ` = ` {sd}$$/수식$$, " \
              "$$수식$${sc} ` times ` 3 ` = ` {se}$$/수식$$, $$수식$${sc} ` times ` 4 ` = ` {sf}$$/수식$${ro2} " \
              "$$수식$${sc}$$/수식$$의 $$수식$$1$$/수식$$배, $$수식$$2$$/수식$$배, $$수식$$3$$/수식$$배, $$수식$$4$$/수식$$배가 됩니다.\n" \
              "따라서 $$수식$${sa}$$/수식$${eun1} $$수식$${sg}$$/수식$$의 $$수식$${sk}$$/수식$$배이므로 " \
              "$$수식$${sa} ` div ` {sb}$$/수식$$의 몫은 $$수식$${sc}$$/수식$$의 $$수식$${sk}$$/수식$$배인 $$수식$${sz}$$/수식$$입니다.\n\n"

    while True:
        sk = np.random.randint(4, 10)
        sb = np.random.randint(10, 100)

        if sk != sb: break

    while True:
        sg = np.random.randint(100, 1000)
        if sg % sb == 0:
            break


    sh = 2 * sg
    si = 3 * sg
    sj = 4 * sg

    sc = sg // sb

    sd = 2 * sc
    se = 3 * sc
    sf = 4 * sc

    sa = sg * sk
    sz = sc * sk

    if (str(sb))[-1] == "0" or (str(sb))[-1] == "3" or (str(sb))[-1] == "6":
        ro1 = "으로"
    else:
        ro1 = "로"

    if (str(sf))[-1] == "0" or (str(sf))[-1] == "3" or (str(sf))[-1] == "6":
        ro2 = "으로"
    else:
        ro2 = "로"

    if (str(sa))[-1] == "2" or (str(sa))[-1] == "4" or (str(sa))[-1] == "5" or (str(sa))[-1] == "9":
        eun1 = "는"
    else:
        eun1 = "은"

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sh=sh, si=si, sj=sj)
    answer = answer.format(sz=sz)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sh=sh, si=si, sj=sj, sk=sk, sz=sz, ro1=ro1, ro2=ro2, eun1=eun1)

    return stem, answer, comment



























# 4-1-6-15
def findingrule416_Stem_007():
    stem = "아래의 규칙을 이용하여 나누는 수가 $$수식$${sa}$$/수식$$일 때의 계산식 2개를 써 보세요.\n$$표$$$$수식$${sb} ` div ` {sb} ` = ` 1$$/수식$$\n$$수식$${sb2} ` div ` {sb} ` div ` {sb} ` = ` 1 $$/수식$$\n$$수식$${sb3} ` div ` {sb} ` div ` {sb} ` div ` {sb} ` = ` 1 $$/수식$$\n$$수식$${sb4} ` div ` {sb} ` div ` {sb} ` div ` {sb} ` div ` {sb} ` = ` 1 $$/수식$$$$/표$$\n$$표$$$$수식$${sa} ` div ` {sa} ` = ` 1$$/수식$$\n$$수식$${sa2} div ` {sa} ` div ` {sa} ` = ` 1 $$/수식$$\n$$수식$${box1}$$/수식$$\n$$수식$${box2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n㉠ $$수식$${sa3} ` div ` {sa} ` div ` {sa} ` div ` {sa} ` = ` 1 $$/수식$$, "\
             "㉡ $$수식$${sa4} ` div ` {sa} ` div ` {sa} ` div ` {sa} ` div ` {sa} ` = ` 1 $$/수식$$\n"
    comment = "(해설)\n" \
              "나누는 수가 $$수식$$1$$/수식$$개씩 늘어나고 계산 결과는 $$수식$$1$$/수식$$로 같습니다.\n" \
              "계산식을 $$수식$$2$$/수식$$개 더 써 보면 $$수식$${sa3} ` div ` {sa} ` div ` {sa} ` div ` {sa} ` = ` 1 $$/수식$$, "\
              "$$수식$${sa4} ` div ` {sa} ` div ` {sa} ` div ` {sa} ` div ` {sa} ` = ` 1 $$/수식$$입니다.\n\n"


    while True:
        sa = np.random.randint(2, 10)
        sb = np.random.randint(2, 10)
        if sa != sb:
            break


    sb2 = pow(sb, 2)
    sb3 = pow(sb, 3)
    sb4 = pow(sb, 4)
    sa2 = pow(sa, 2)
    sa3 = pow(sa, 3)
    sa4 = pow(sa, 4)

    box1 = "box{%s````````````````````````````````````````````````````````````````````````````````````````````````````}" % "㉠"
    box2 = "box{%s````````````````````````````````````````````````````````````````````````````````````````````````````}" % "㉡"

    stem = stem.format(sa=sa, sb=sb, sb2=sb2, sb3=sb3, sb4=sb4, sa2=sa2, box1=box1, box2=box2)
    answer = answer.format(sa=sa, sa3=sa3, sa4=sa4)
    comment = comment.format(sa=sa, sa3=sa3, sa4=sa4)

    return stem, answer, comment














