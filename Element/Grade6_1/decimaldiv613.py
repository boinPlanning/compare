import numpy as np
import math
import fractions



answer_dict = {
    0 : "①",
    1 : "②",
    2 : "③",
    3 : "④",
    4 : "⑤"
}



answer_kodict={
    0 : "ㄱ",
    1 : "ㄴ",
    2 : "ㄷ",
    3 : "ㄹ",
    4 : "ㅁ"
}



answer_koonedict={
    0 : "㉠",
    1 : "㉡",
    2 : "㉢",
    3 : "㉣",
    4 : "㉤",
    5 : "㉥"
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






def josa(num, check):
    if check == "은" or check == "는":
        if num == 2 or num == 4 or num == 5 or num == 9 or num == "2" or num == "4" or num == "5" or num == "9":
            return "는"
        else:
            return "은"

    elif check == "이" or check == "가":
        if num == 2 or num == 4 or num == 5 or num == 9 or num == "2" or num == "4" or num == "5" or num == "9":
            return "가"
        else:
            return "이"

    elif check == "와" or check == "과":
        if num == 2 or num == 4 or num == 5 or num == 9 or num == "2" or num == "4" or num == "5" or num == "9":
            return "와"
        else:
            return "과"

    elif check == "를" or check == "을":
        if num == 2 or num == 4 or num == 5 or num == 9 or num == "2" or num == "4" or num == "5" or num == "9":
            return "를"
        else:
            return "을"

    elif check == "로" or check == "으로":
        if num == 0 or num == 3 or num == 6 or num == "0" or num == "3" or num == "6":
            return "으로"
        else:
            return "로"

    elif check == "이야" or check == "야":
        if num == 2 or num == 4 or num == 5 or num == 9 or num == "2" or num == "4" or num == "5" or num == "9":
            return "야"
        else:
            return "이야"









def show_int(a):
    if a == (a // 1):
        a = int(a)
    return a


















# 6-1-3-02
def decimaldiv613_Stem_001():
    stem = "자연수의 나눗셈을 이용하여 소수의 나눗셈을 해 보세요.\n$$표$$$$수식$${sa} ` div ` {sb} ` = ` {sc}$$/수식$$\n$$수식$${sd} ` div ` {sb} ` = ` {one}$$/수식$$\n$$수식$${se} ` div ` {sb} ` = ` {two}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${sf}$$/수식$$, $$수식$${sg}$$/수식$$\n"
    comment = "(해설)\n" \
              "나누는 수가 같을 때 나누어지는 수가 $$수식$$1 over 10$$/수식$$배, $$수식$$1 over 100$$/수식$$배가 되면 " \
              "몫도 $$수식$$1 over 10$$/수식$$배, $$수식$$1 over 100$$/수식$$배가 됩니다.\n\n"


    one = "㉠"
    two = "㉡"

# (1)
    sb = np.random.randint(2, 10)
    while True:
        sa = np.random.randint(sb * 100 + 1, 1000)
        if sa % sb == 0:
            sa_list = list(map(int, str(sa)))
            if (sa_list[0] % sb == 0 and sa_list[1] % sb == 0) or (sa_list[0] < sb and (sa_list[0]*10 + sa_list[1]) % sb == 0):
                if sa_list[2] % sb == 0:
                    sc = int(sa / sb)
                    sd = sa / 10
                    se = sa / 100
                    sf = sc / 10
                    sg = sc / 100
                    if sf > 1 and sg > 1:
                        break


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, one=one, two=two)
    answer = answer.format(sf=sf, sg=sg)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd)

    return stem, answer, comment



















# 6-1-3-03
def decimaldiv613_Stem_002():
    stem = "$$수식$${sa} ` div ` {sb} ` = ` {sc}$$/수식$${rur1} 이용하여 □ 안에 알맞은 수를 써넣으세요.\n$$표$$$$수식$${one} ` div ` {sb} ` = ` {sd}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${sf}$$/수식$$\n"
    comment = "(해설)\n" \
              "나누는 수가 $$수식$${sb}$$/수식$${ro1} 같고 몫이 $$수식$${se}$$/수식$$배가 되었으므로 나누어지는 수도 $$수식$${se}$$/수식$$배가 되어야 한다.\n" \
              "→ $$수식$${sf} ` div ` {sb} ` = ` {sd}$$/수식$$\n\n"


    one = "□"

# (1)
    sb = np.random.randint(2, 10)
    while True:
        sa = np.random.randint(sb * 100 + 1, 1000)
        if sa % sb == 0:
            sa_list = list(map(int, str(sa)))
            if (sa_list[0] % sb == 0 and sa_list[1] % sb == 0) or (sa_list[0] < sb and (sa_list[0]*10 + sa_list[1]) % sb == 0):
                if sa_list[2] % sb == 0:
                    e = [1/10, 1/100][np.random.randint(0, 2)]

                    if e == 1/10:
                        se = "1 over 10"
                    else:
                        se = "1 over 100"

                    sc = int(sa / sb)
                    sd = round(sc * e, 4)
                    sf = round(sa * e, 4)
                    if sf > 1:
                        break

    if (str(sc))[-1] == "2" or (str(sc))[-1] == "4" or (str(sc))[-1] == "5" or (str(sc))[-1] == "9":
        rur1 = "를"
    else:
        rur1 = "을"

    if (str(sb))[-1] == "0" or (str(sb))[-1] == "3" or (str(sb))[-1] == "6":
        ro1 = "으로"
    else:
        ro1 = "로"

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, one=one, rur1=rur1)
    answer = answer.format(sf=sf)
    comment = comment.format(sb=sb, sd=sd, se=se, sf=sf, ro1=ro1)

    return stem, answer, comment





















# 6-1-3-04
def decimaldiv613_Stem_003():
    stem = "$$수식$${sa} ` div ` {sb}$$/수식$${rur1} 이용하여 $$수식$${sc} ` div ` {sb}$$/수식$${gwa1} $$수식$${sd} ` div ` {sb}$$/수식$${rur1} 계산하는 방법을 이야기하고 있습니다. 잘못 이야기한 사람은 누구인가요?\n$$표$$$$수식$$LEFT [$$/수식$${t1}$$수식$$RIGHT ] ```` {sc} ` div ` {sb}$$/수식$$의 몫은 $$수식$${sa} ` div ` {sb}$$/수식$$의 $$수식$${k}$$/수식$$배야.\n$$수식$$LEFT [$$/수식$${t2}$$수식$$RIGHT ] ```` {sd} ` div ` {sb}$$/수식$$의 몫은 $$수식$${sa} ` div ` {sb}$$/수식$$의 몫의 $$수식$${sp}$$/수식$$배야.$$/표$$\n"
    answer = "(정답)\n{t}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT [$$/수식$${t1}$$수식$$RIGHT ] ```` {sc}`div`{sb}$$/수식$$의 몫은 $$수식$${sa}`div`{sb}$$/수식$$의 $$수식$${m}$$/수식$$배입니다.\n" \
              "$$수식$$LEFT [$$/수식$${t2}$$수식$$RIGHT ]$$/수식$$ 나누는 수가 같을 때 나누어지는 수가 $$수식$${q}$$/수식$$배가 되면 몫도 $$수식$${q}$$/수식$$배가 됩니다.\n\n"


    while True:
        t1 = ["미수", "기호", "수찬", "동영", "하루", "주찬", "성실"][np.random.randint(0, 7)]
        t2 = ["미수", "기호", "수찬", "동영", "하루", "주찬", "성실"][np.random.randint(0, 7)]
        if t1 != t2:
            break

    sb = np.random.randint(2, 10)
    while True:
        sa = np.random.randint(100, 1000)
        if sa % 10 != 0:
            sa_list = list(map(int, str(sa)))
            if (sa_list[0] % sb == 0 and sa_list[1] % sb == 0) or (sa_list[0] < sb and (sa_list[0]*10 + sa_list[1]) % sb == 0):
                if sa_list[2] % sb == 0:
                    sc = [sa/10, sa/100][np.random.randint(0, 2)]
                    if sc == sa/10:
                        sd = sa/100
                    elif sc == sa/100:
                        sd = sa/10
                    
                    if sc / sb > 1 and sa / sb > 1:
                        break

    sk = [1/10, 1/100][np.random.randint(0, 2)]
    sm = round(sc / sa, 2) # 옳음(c/a)
    sq = round(sd / sa, 2)
                    

    # if a * k == c (답이 t2일 때)

    if sk == sm:
        if sk == 1/100:
            k = "1 over 100"
            m = "1 over 100"
        elif sk == 1/10:
            k = "1 over 10"
            m = "1 over 10"
        t = t2
        if sq == 1/100:
            q = "1 over 100"
            sp = "1 over 100"
        elif sq == 1/10:
            q = "1 over 10"
            sp = "1 over 10"

    elif sk != sm:
        if sk == 1/100:
            k = "1 over 100"
            m = "1 over 10"
        elif sk == 1/10:
            k = "1 over 10"
            m = "1 over 100"
        t = t1
        if sq == 1/100:
            q = "1 over 100"
            sp = "1 over 100"
        elif sq == 1/10:
            q = "1 over 10"
            sp = "1 over 10"

    if (str(sb))[-1] == "2" or (str(sb))[-1] == "4" or (str(sb))[-1] == "5" or (str(sb))[-1] == "9":
        rur1 = "를"
        gwa1 = "와"
    else:
        rur1 = "을"
        gwa1 = "과"

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, sk=sk, sp=sp, t1=t1, t2=t2, k=k, rur1=rur1, gwa1=gwa1)
    answer = answer.format(t=t)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sp=sp, t1=t1, t2=t2, m=m, q=q)

    return stem, answer, comment









# 6-1-3-05
def decimaldiv613_Stem_004():
    stem = "빈 곳에 알맞은 수를 써넣으세요.\n$$수식$${box_a}$$/수식$$ → $$수식$${box_b}$$/수식$$ → $$수식$${box_one}$$/수식$$ → $$수식$${box_c}$$/수식$$ → $$수식$${box_two}$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${k}$$/수식$$, ㉡ $$수식$${h}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${e} ` div ` {b} ` = ` {d}$$/수식$$  →  $$수식$${a} ` div ` {b} ` = ` {k}$$/수식$$\n" \
              "$$수식$${f} ` div ` {c} ` = ` {g}$$/수식$$  →  $$수식$${k} ` div ` {c} ` = ` {h}$$/수식$$\n\n"


    one = "㉠"
    two = "㉡"

    while True:
        b = np.random.randint(2, 10)
        c = np.random.randint(2, 10)
        if b * c != 10:
            e = np.random.randint(100, 1000)
            if (e % 10 != 0) and (e % b == 0) and (e % c == 0):
                d = int(e / b)
                a = e / 10
                k = round(a / b, 2)
                f = int(k * 10)
                if (f % c == 0):
                    e_list = list(map(int, str(e)))
                    f_list = list(map(int, str(f)))
                    if (e_list[0] % b == 0 and e_list[1] % b == 0 and e_list[2] % b == 0) and (((f_list[0] % c == 0 and f_list[1] % c == 0) or (f_list[0] < c and (f_list[0]*10 + f_list[1]) % c == 0)) and f_list[2] % c == 0):
                        g = int(f / c)
                        h = round(k / c, 2)
                        if k > 1 and h > 1:
                            break

    box_a = "box{%s}" % a
    box_b = "`div`box{%s}" % b
    box_one = "box{%s````````````````````}" % one
    box_c = "`div`box{%s}" % c
    box_two = "box{%s````````````````````}" % two

    # stem = stem.format(one=one, two=two, a=a, b=b, c=c)
    stem = stem.format(box_a=box_a, box_b=box_b, box_one=box_one, box_c=box_c, box_two=box_two)
    answer = answer.format(k=k, h=h)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, k=k)

    return stem, answer, comment











# 6-1-3-06
def decimaldiv613_Stem_005():
    stem = "무게가 같은 {pen} $$수식$${a}$$/수식$$자루의 무게가 $$수식$${b} rm g$$/수식$$일 때 {pen} 한 자루의 무게는 몇 $$수식$$rm g$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${c} rm g$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${d} ` div ` {a} ` = ` {f}$$/수식$$ → $$수식$${b} ` div ` {a} `` = ` {c} LEFT ( rm g RIGHT )$$/수식$$\n\n"


    pen = ["연필", "색연필", "볼펜", "만년필", "형광펜"][np.random.randint(0, 5)]

    a = np.random.randint(2, 10)

    while True:
        d = np.random.randint(1000, 10000)
        if d % a == 0:
            d_list = list(map(int, str(d)))
            if (d_list[0] % a == 0 and d_list[1] % a == 0) or (d_list[0] < a and (d_list[0]*10 + d_list[1]) % a == 0):
                if d_list[2] % a == 0 and d_list[3] % a == 0:
                    b = d / 100
                    f = int(d / a)
                    c = round(b / a, 2)
                    if c > 1:
                        break

    stem = stem.format(a=a, b=b, pen=pen)
    answer = answer.format(c=c)
    comment = comment.format(a=a, b=b, c=c, d=d, f=f)

    return stem, answer, comment


















# 6-1-3-07
def decimaldiv613_Stem_006():
    stem = "색 테이프 $$수식$${a} rm {{mm}}$$/수식$$를 $$수식$${b}$$/수식$$도막으로 똑같이 나누면 한 도막이 $$수식$${c} rm {{mm}}$$/수식$$입니다. 색 테이프 $$수식$${d} rm {{cm}}$$/수식$$를 $$수식$${b}$$/수식$$도막으로 똑같이 나누면 한 도막은 몇 $$수식$$rm {{cm}}$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${e} rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` = ` {c}$$/수식$$이고 색 테이프 $$수식$${d} rm {{cm}}$$/수식$$를 $$수식$${b}$$/수식$$도막으로 " \
              "똑같이 나누는 식은 $$수식$${d} ` div ` {b}$$/수식$$입니다.\n" \
              "$$수식$${d}$$/수식$$는 $$수식$${a}$$/수식$$의 $$수식$${k}$$/수식$$배이므로 " \
              "색 테이프 $$수식$${d} rm {{cm}}$$/수식$$를 $$수식$${b}$$/수식$$도막으로 똑같이 나누면 한 도막은 $$수식$${c}$$/수식$$의 $$수식$${k}$$/수식$$배인 " \
              "$$수식$${e} rm {{cm}}$$/수식$$ 입니다.\n\n"


    b = np.random.randint(2, 10)

    while True:
        a = np.random.randint(100, 1000)
        if (a % b == 0) & (a % 10 != 0):
            a_list = list(map(int, str(a)))
            if (a_list[0] % b == 0 and a_list[1] % b == 0) or (a_list[0] < b and (a_list[0]*10 + a_list[1]) % b == 0):
                if a_list[2] % b == 0:
                    sk = [1/10, 1/100][np.random.randint(0, 2)]

                    if sk == 1/10:
                        k = "1 over 10"
                    else:
                        k = "1 over 100"

                    c = int(a / b)
                    d = round(a * sk, 2)
                    e = round(c * sk, 2)
                    if e > 1:
                        break

    stem = stem.format(a=a, b=b, c=c, d=d)
    answer = answer.format(e=e)
    comment = comment.format(a=a, b=b, c=c, d=d, k=k, e=e)

    return stem, answer, comment






















# 6-1-3-11
def decimaldiv613_Stem_007():
    stem = "{who1}네 모둠은 철사 $$수식$${a}rm {{mm}}$$/수식$$를 $$수식$${b}$$/수식$$명이 똑같이 나누어 가졌고, {who2}네 모둠은 $$수식$${c}rm {{cm}}$$/수식$$를 $$수식$${b}$$/수식$$명이 똑같이 나누어 가졌습니다. {who1}네 모둠은 한 명이 몇 $$수식$$rm {{mm}}$$/수식$$씩 가지고, {who2}네 모둠은 한 명이 몇 $$수식$$rm {{cm}}$$/수식$$씩 가졌나요?\n"
    answer = "(정답)\n{who1}네 모둠 $$수식$${d}rm {{mm}}$$/수식$$, {who2}네 모둠 $$수식$${e}rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` = ` {d} LEFT ( rm {{mm}} RIGHT )$$/수식$$이므로 {who1}네 모둠은 한 명이 $$수식$${d} rm {{mm}}$$/수식$$씩 가졌습니다.\n" \
              "{who2}네 모둠 한 명이 몇 $$수식$$rm {{cm}}$$/수식$$씩 가졌는지 구하는 식은 $$수식$${c} ` div ` {b}$$/수식$$이고 " \
              "$$수식$${c}$$/수식$$는 $$수식$${a}$$/수식$$의 $$수식$${k}$$/수식$$배이므로 철사 $$수식$${c} rm {{cm}}$$/수식$$를 $$수식$${b}$$/수식$$명이 " \
              "똑같이 나누어 가지면 그 길이는 $$수식$${d}$$/수식$$의 $$수식$${k}$$/수식$$배인 $$수식$${e} rm {{cm}}$$/수식$$입니다.\n" \
              "따라서 {who2}네 모둠은 한 명이 $$수식$${e} rm {{cm}}$$/수식$$씩 가졌습니다.\n\n"



    while True:
        who1 = ["민주", "경아", "준수", "아라", "석재", "철호", "은하", "선우", "원희", "혜교", "권기", "상후"][np.random.randint(0, 12)]
        who2 = ["민주", "경아", "준수", "아라", "석재", "철호", "은하", "선우", "원희", "혜교", "권기", "상후"][np.random.randint(0, 12)]
        if who1 != who2:
            break

    b = np.random.randint(2, 10)

    while True:
        a = np.random.randint(100, 1000)
        if (a % b == 0) & (a % 10 != 0):
            a_list = list(map(int, str(a)))
            if (a_list[0] % b == 0 and a_list[1] % b == 0) or (a_list[0] < b and (a_list[0]*10 + a_list[1]) % b == 0):
                if a_list[2] % b == 0:
                    sk = [1/10, 1/100][np.random.randint(0, 2)]
                
                    if sk == 1/10:
                        k = "1 over 10"
                    else:
                        k = "1 over 100"
                
                    d = int(a / b)
                    c = round(a * sk, 2)
                    e = round(d * sk, 2)
                    if e > 1:
                        break

    stem = stem.format(a=a, b=b, c=c, who1=who1, who2=who2)
    answer = answer.format(d=d, e=e, who1=who1, who2=who2)
    comment = comment.format(a=a, b=b, c=c, d=d, k=k, e=e, who1=who1, who2=who2)

    return stem, answer, comment





















# 6-1-3-12
def decimaldiv613_Stem_008():
    stem = "$$수식$${a}$$/수식$$분 동안 $$수식$${b} rm {{km}}$$/수식$$를 가는 자동차와 $$수식$${c}$$/수식$$분 동안 $$수식$${d} rm {{km}}$$/수식$$를 가는 기차가 있습니다. 자동차와 기차가 동시에 출발하여 같은 방향으로 출발한다면 $$수식$$1$$/수식$$분 후에는 어느 것이 몇 $$수식$$rm {{km}}$$/수식$$ 더 앞서 있는지 써 보세요.\n" \
        "{boxblank} 가 {boxblank} 더 앞서 있습니다."
    answer = "(정답)\n{e}, $$수식$${f} rm {{km}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$자동차가 $$수식$$1$$/수식$$분 동안 가는 거리$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {b} ` div ` {a} ` = ` {g} ` LEFT ( rm {{km}} RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$기차가 $$수식$$1$$/수식$$분 동안 가는 거리$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {d} ` div ` {c} ` = ` {h} ` LEFT ( rm {{km}} RIGHT )$$/수식$$\n" \
              "$$수식$${i} ` &lt; ` {j} ` $$/수식$$이므로 {e}가\n" \
              "$$수식$${j} ` - ` {i} ` = ` {f} ` LEFT ( rm {{km}} RIGHT )$$/수식$$ 더 앞서 있습니다.\n\n"

    boxblank = "$$수식$$box{　　}$$/수식$$"

    while True:
        while True:
            a = np.random.randint(2, 10)
            k = np.random.randint(100, 1000)
            if (k % a == 0) & (k % 10 != 0):
                k_list = list(map(int, str(k)))
                if (k_list[0] % a == 0 and k_list[1] % a == 0) or (k_list[0] < a and (k_list[0]*10 + k_list[1]) % a == 0):
                    if k_list[2] % a == 0:
                        b = round(k / 100, 2)
                        g = round(b / a, 2)
                        if g > 1:
                            break

        while True:
            c = np.random.randint(2, 10)
            l = np.random.randint(1000, 10000)
            if (l % c == 0) & (l % 10 != 0):
                l_list = list(map(int, str(l)))
                if (l_list[0] % c == 0 and l_list[1] % c == 0) or (l_list[0] < c and (l_list[0]*10 + l_list[1]) % c == 0):
                    if l_list[2] % c == 0:
                        d = round(l / 100, 2)
                        h = round(d / c, 2)
                        if h > 1:
                            break

        if g > h:
            i = h
            j = g
            f = round(g - h, 2)
            e = "자동차"
            break
        elif g < h:
            i = g
            j = h
            f = round(h - g, 2)
            e = "기차"
            break


    stem = stem.format(a=a, b=b, c=c, d=d, boxblank=boxblank)
    answer = answer.format(e=e, f=f)
    comment = comment.format(a=a, b=b, c=c, d=d, g=g, h=h, i=i, j=j, e=e, f=f)

    return stem, answer, comment











# 6-1-3-13
def decimaldiv613_Stem_009():
    stem = "빈 곳에 알맞은 수를 써넣으세요.\n$$수식$${box_a}$$/수식$$ → $$수식$${box_b}$$/수식$$ → $$수식$${box_one}$$/수식$$ → $$수식$${box_c}$$/수식$$ → $$수식$${box_two}$$/수식$$\n"
    answer = "(정답)\n㉡ $$수식$${d}$$/수식$$, ㉡ $$수식$${e}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` = ` {d}$$/수식$$, $$수식$${d} ` div ` {c} ` = ` {e}$$/수식$$\n\n"


    one = "㉠"
    two = "㉡"

    while True:
        b = np.random.randint(2, 10)
        c = np.random.randint(2, 10)
        if b * c != 10:
            j = np.random.randint(100, 1000)
            #hun = j // 100
            #ten = (j // 10) % 10
            #if (j % 10 != 0) and (j % b == 0) and (j % c == 0) and (ten % b != 0) and (hun % b != 0):
            #    break
            if j % 10 != 0 and j % b == 0 and (j/b) % c == 0:
                a = j / 10
                d = round(a / b, 2)
                e = round(d / c, 2)
                if d > 1 and e > 1 :
                    break

    box_a = "box{%s}" % a
    box_b = "`div`box{%s}" % b
    box_one = "box{%s````````````````````}" % one
    box_c = "`div`box{%s}" % c
    box_two = "box{%s````````````````````}" % two

    # stem = stem.format(one=one, two=two, a=a, b=b, c=c)
    stem = stem.format(box_a=box_a, box_b=box_b, box_one=box_one, box_c=box_c, box_two=box_two)
    answer = answer.format(d=d, e=e)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e)

    return stem, answer, comment

















# 6-1-3-14
def decimaldiv613_Stem_010():
    stem = "㉠과 ㉡에 알맞은 수의 합을 구해 보세요.\n$$표$$$$수식$${a} ` div ` {b} ` = ` {que} over 10 ` = ` ㉡$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${d}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` = ` {c} over 10 ` div ` {b} ` = ` {com} over 10 ` = ` {e} over 10 ` = ` {f} `$$/수식$$\n" \
              "㉠$$수식$$` = ` {b}$$/수식$$, ㉡$$수식$$` = ` {f}$$/수식$$이므로\n" \
              "㉠$$수식$$` + `$$/수식$$㉡$$수식$$` = ` {b} ` + ` {f} ` = ` {d}$$/수식$$입니다.\n\n"


    while True:
        b = np.random.randint(10, 100)
        c = np.random.randint(100, 1000)
        hun = c // 100
        ten = (c // 10) % 10
        if (c % b == 0) & (c % 10 != 0) & (hun % b != 0) & (ten % b != 0):
            break

    a = c / 10
    e = int(c / b)
    f = e / 10
    d = b + f
    que = "{%d ` div ` ㉠}" % c
    com = "{%d ` div ` %d}" % (c, b)


    stem = stem.format(a=a, b=b, que=que)
    answer = answer.format(d=d)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f, com=com)

    return stem, answer, comment















# 6-1-3-15
def decimaldiv613_Stem_011():
    stem = "빈 곳에 소수를 자연수로 나눈 몫을 써넣으세요.\n$$수식$${box_a}{box_one}{box_b}$$/수식$$\n"
    answer = "(정답)\n$$수식$${c}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` = ` {c}$$/수식$$\n\n"


    one = "(답)"

    while True:
        b = np.random.randint(2, 10)
        d = np.random.randint(100, 1000)
        hun = d // 100
        ten = (d // 10) % 10
        if (d % 10 != 0) & (d % b == 0) & (ten % b != 0) & (hun % b != 0):
            break

    a = d / 10
    c = round(a / b, 2)

    box_a = "$$수식$$box{%s}$$/수식$$" % a
    box_one = "$$수식$$box{　　　}$$/수식$$"
    box_b = "$$수식$$box{%s}$$/수식$$" % b

    # stem = stem.format(one=one, a=a, b=b)
    stem = stem.format(box_a=box_a, box_one=box_one, box_b=box_b)
    answer = answer.format(c=c)
    comment = comment.format(a=a, b=b, c=c)

    return stem, answer, comment












# 6-1-3-16
def decimaldiv613_Stem_012():
    stem = "빈 곳에 알맞은 수를 써넣으세요.\n{box_a}→$$수식$$LEFT ( `` div `` RIGHT )$$/수식$${box_b}→{box_one}\n{box_c}→$$수식$$LEFT ( `` div `` RIGHT )$$/수식$${box_d}→{box_two}\n"
    answer = "(정답)\n$$수식$${e}$$/수식$$, $$수식$${f}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` = ` {e}$$/수식$$, $$수식$${c} ` div ` {d} ` = ` {f}$$/수식$$\n\n"


    one = "㉠"
    two = "㉡"

    while True:
        b = np.random.randint(2, 10)
        g = np.random.randint(1000, 10000)
        tho = g // 1000
        hun = (g // 100) % 10
        ten = (g // 10) % 10
        if (g % 10 != 0) & (g % b == 0) & (ten % b != 0) & (hun % b != 0) & (tho % b != 0):
            a = g / 100
            e = round(a / b, 2)
            if e > 1:
                break

    while True:
        d = np.random.randint(10, 100)
        if d % 10 != 0:
            h = np.random.randint(1000, 10000)
            tho = h // 1000
            hun = (h // 100) % 10
            ten = (h // 10) % 10
            if (h % 10 != 0) & (h % d == 0) & (ten % d != 0) & (hun % d != 0) & (tho % d != 0):
                c = h / 100
                f = round(c / d, 2)
                if f > 1:
                    break

    box_a = "$$수식$$box{%s}$$/수식$$" % a
    box_b = "$$수식$$box{%s}$$/수식$$" % b
    box_one = "$$수식$$box{%s````````````````````}$$/수식$$" % one
    box_c = "$$수식$$box{%s}$$/수식$$" % c
    box_d = "$$수식$$box{%s}$$/수식$$" % d
    box_two = "$$수식$$box{%s````````````````````}$$/수식$$" % two

    # stem = stem.format(one=one, two=two, a=a, b=b, c=c, d=d)
    stem = stem.format(box_a=box_a, box_b=box_b, box_one=box_one, box_c=box_c, box_d=box_d, box_two=box_two)
    answer = answer.format(e=e, f=f)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f)

    return stem, answer, comment















# 6-1-3-17
def decimaldiv613_Stem_013():
    stem = "두 나눗셈의 몫의 합을 구해 보세요.\n$$표$$$$수식$${a} ` div ` {b}$$/수식$$        $$수식$${c} ` div ` {d}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${e}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` = ` {f}$$/수식$$, $$수식$${c} ` div ` {d} ` = ` {g} `$$/수식$$이므로 " \
              "두 나눗셈의 몫의 합은 $$수식$${f} ` + ` {g} ` = ` {e} `$$/수식$$입니다.\n\n"


    while True:
        b = np.random.randint(2, 10)
        j = np.random.randint(1000, 10000)
        tho = j // 1000
        hun = (j // 100) % 10
        ten = (j // 10) % 10
        if (j % b == 0) & (j % 10 != 0) & (tho % b != 0) & (hun % b != 0) & (ten % b != 0):
            break

    while True:
        d = np.random.randint(2, 10)
        k = np.random.randint(1000, 10000)
        tho = k // 1000
        hun = (k // 100) % 10
        ten = (k // 10) % 10
        if (k % d == 0) & (k % 10 != 0) & (tho % d != 0) & (hun % d != 0) & (ten % d != 0):
            break


    a = j / 100
    c = k / 100
    f = round(a / b, 2)
    g = round(c / d, 2)
    e = round(f + g, 2)

    stem = stem.format(a=a, b=b, c=c, d=d)
    answer = answer.format(e=e)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f, g=g)

    return stem, answer, comment





















# 6-1-3-18
def decimaldiv613_Stem_014():
    stem = "계산 결과를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${a} ` div ` {b}$$/수식$$  ○  $$수식$${c} ` div ` {d}$$/수식$$\n"
    answer = "(정답)\n$$수식$${l}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` = ` {e} `$$/수식$$, $$수식$${c} ` div ` {d} ` = ` {f} `$$/수식$$\n" \
              "$$수식$${g}{l}{h}$$/수식$$이므로 $$수식$${j}{l}{k}$$/수식$$입니다.\n\n"


    while True:
        b = np.random.randint(2, 10)
        m = np.random.randint(100, 1000)
        hun = m // 100
        ten = (m // 10) % 10
        if (m % b == 0) & (m % 10 != 0) & (hun % b != 0) & (ten % b != 0):
            break

    while True:
        d = np.random.randint(2, 10)
        n = np.random.randint(100, 1000)
        hun = n // 100
        ten = (n // 10) % 10
        if (n % d == 0) & (n % 10 != 0) & (hun % d != 0) & (ten % d != 0):
            break

    a = round(m / 10, 1)
    c = round(n / 10, 1)
    e = round(a/b, 3)
    f = round(c/d, 3)

    a = show_int(a)
    c = show_int(c)
    e = show_int(e)
    f = show_int(f)

    g = e
    h = f

    if e > f:
        j = "%s ` div ` %s" % (a, b)
        k = "%s ` div ` %s" % (c, d)
        l = "` &gt; `"

    elif e < f:
        k = "%s ` div ` %s" % (a, b)
        j = "%s ` div ` %s" % (c, d)
        l = "` &lt; `"

    elif e == f:
        j = "%s ` div ` %s" % (a, b)
        k = "%s ` div ` %s" % (c, d)
        l = "` = `"


    stem = stem.format(a=a, b=b, c=c, d=d)
    answer = answer.format(l=l)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, l=l, j=j, k=k)

    return stem, answer, comment
























# 6-1-3-19
def decimaldiv613_Stem_015():
    stem = "나눗셈의 몫이 $$수식$${t}$$/수식$$인 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${a} `` div `` {b}$$/수식$$      ㉡ $$수식$${c} `` div `` {d}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{k}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${a} `` div `` {b} `` = `` {e}$$/수식$$\n" \
              "㉡ $$수식$${c} `` div `` {d} `` = `` {f}$$/수식$$\n" \
              "따라서 나눗셈의 몫이 $$수식$${t}$$/수식$$인 것은 {k}입니다.\n\n"


    while True:
        b = np.random.randint(2, 10)
        g = np.random.randint(1000, 10000)
        tho = g // 1000
        hun = (g // 100) % 10
        ten = (g // 10) % 10

        if (g % b == 0) & (g % 10 != 0) & (tho % b != 0) & (hun % b != 0) & (ten % b != 0):
            d = np.random.randint(2, 10)
            h = np.random.randint(1000, 10000)
            tho = h // 1000
            hun = (h // 100) % 10
            ten = (h // 10) % 10
            if (h % b == 0) & (h % 10 != 0) & (tho % d != 0) & (hun % d != 0) & (ten % d != 0) & (b != d):
                break

    a = round(g / 100, 2)
    c = round(h / 100, 2)

    e = round(a / b, 2)
    f = round(c / d, 2)

    t = [e, f][np.random.randint(0, 2)]

    if e == t:
        k = "㉠"
    elif f == t:
        k = "㉡"


    stem = stem.format(a=a, b=b, c=c, d=d, t=t)
    answer = answer.format(k=k)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f, k=k, t=t)

    return stem, answer, comment























# 6-1-3-20
def decimaldiv613_Stem_016():
    stem = "일정한 빠르기로 $$수식$${a}$$/수식$$분 동안 $$수식$${b} rm {{km}}$$/수식$$를 가는 자동차가 있습니다. 이 자동차가 $$수식$$1$$/수식$$분 동안 가는 거리는 몇 $$수식$$rm {{km}}$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${c} rm {{km}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$자동차가 $$수식$$1$$/수식$$분 동안 가는 거리$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$자동차가 $$수식$${a}$$/수식$$분 동안 가는 거리$$수식$$RIGHT ) ` div ` {a}$$/수식$$\n" \
              "$$수식$$= ` {b} ` div ` {a} ` = ` {c} ` LEFT ( rm {{km}} RIGHT ) `$$/수식$$\n\n"


    while True:
        a = np.random.randint(2, 10)
        d = np.random.randint(100, 1000)
        hun = d // 100
        ten = (d // 10) % 10
        if (d % a == 0) & (d % 10 != 0) & (hun % a != 0) & (ten % a != 0):
            break

    b = round(d / 10, 1)
    c = round(b / a, 1)


    stem = stem.format(a=a, b=b)
    answer = answer.format(c=c)
    comment = comment.format(a=a, b=b, c=c)

    return stem, answer, comment























# 6-1-3-21
def decimaldiv613_Stem_017():
    stem = "{t}네 식구가 $$수식$${a}$$/수식$$주일 동안 마신 생수는 $$수식$${b} rm L$$/수식$$입니다. 매일 같은 양의 생수를 마셨다면 하루에 마신 생수는 몇 $$수식$$rm L$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${c} rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a}$$/수식$$주일$$수식$$` = ` {d}$$/수식$$일이므로\n" \
              "$$수식$$LEFT ($$/수식$$하루에 마신 생수의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ( {a}$$/수식$$주일 동안 마신 생수의 양$$수식$$RIGHT ) ` div ` LEFT ($$/수식$$날 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {b} ` div ` {d} ` = ` {c} ` LEFT ( rm L RIGHT ) `$$/수식$$\n\n"


    t = ["수미", "선우", "영미", "우찬이", "민지", "경배"][np.random.randint(0, 6)]

    # while True:
    #     a = np.random.randint(2, 10)
    #     f = np.random.randint(1000, 10000)
    #     tho = f // 1000
    #     hun = (f // 100) % 10
    #     ten = (f // 10) % 10
    #     if (f % a == 0) & (f % 10 != 0) & (tho % a != 0) & (hun % a != 0) & (ten % a != 0):
    #         break
    #
    # b = round(f / 100, 2)
    # d = a * 7
    # c = round(b / d, 2)


    while True:
        a = np.random.randint(1, 10)
        d = a * 7
        f1 = np.random.randint(143, 1429)
        f2 = d*f1
        f2_tho = int((str(f2))[-4]) * 100
        f2_hun = int((str(f2))[-3]) * 10
        f2_ten = int((str(f2))[-2])

        f2_check = f2_tho + f2_hun + f2_ten

        if 1000 <= f2 and f2 < 10000 and f2 % 10 != 0 and f2_check % d != 0:
            b = round(f2/100, 2)
            c = round(f1/100, 2)
            break

    stem = stem.format(a=a, b=b, t=t)
    answer = answer.format(c=c)
    comment = comment.format(a=a, b=b, c=c, d=d)

    return stem, answer, comment























# 6-1-3-22
def decimaldiv613_Stem_018():
    stem = "$$수식$${a} `` div `` {b} `` = `` {c}$$/수식$$임을 이용하여 □ 안에 알맞은 수를 구해 보세요.\n$$표$$□$$수식$$` div ` {b} ` = ` {d} `$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${e}$$/수식$$\n"
    comment = "(해설)\n" \
              "나누는 수가 $$수식$${b}$$/수식$${ro1} 같고 몫이 $$수식$${c}$$/수식$$에서 " \
              "$$수식$${d}$$/수식$${ro2} $$수식$${k}$$/수식$$배가 되었으므로 나누어지는 수도 $$수식$${k}$$/수식$$배가 되어야 합니다.\n" \
              "$$수식$${a}$$/수식$$의 $$수식$${k}$$/수식$$배는 $$수식$${e}$$/수식$$이므로 □ 안에 알맞은 수는 $$수식$${e}$$/수식$$입니다.\n\n"


    while True:
        b = np.random.randint(2, 10)
        a = np.random.randint(100, 1000)
        hun = a // 100
        ten = (a // 10) % 10
        if (a % b == 0) & (a % 10 != 0) & (hun % b != 0) & (ten % b != 0):
            break

    k = [1/10, 1/100][np.random.randint(0, 2)]
    c = int(a / b)

    if k == 1/10:
        d = round(c * 0.1, 1)
        e = round(a * 0.1, 1)
    elif k == 1/100:
        d = round(c * 0.01, 2)
        e = round(a * 0.01, 2)

    if b == 3 or b == 6:
        ro1 = "으로"
    else:
        ro1 = "로"

    if (str(d))[-1] == "3" or (str(d))[-1] == "6":
        ro2 = "으로"
    else:
        ro2 = "로"

    stem = stem.format(a=a, b=b, c=c, d=d)
    answer = answer.format(e=e)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, k=k, ro1=ro1, ro2=ro2)

    return stem, answer, comment

























# 6-1-3-23
def decimaldiv613_Stem_019():
    stem = "어떤 수에 $$수식$${a}$$/수식$${rur1} 곱했더니 $$수식$${b}$$/수식$${ga1} 되었습니다. 어떤 수를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${c}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$어떤 수$$수식$$RIGHT ) ` times ` {a} ` = ` {b}$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$어떤 수$$수식$$RIGHT ) ` = ` {b} ` div ` {a} ` = ` {c}$$/수식$$\n\n"


    while True:
        a = np.random.randint(2, 10)
        d = np.random.randint(1000, 10000)
        tho = d // 1000
        hun = (d // 100) % 10
        ten = (d // 10) % 10
        if (d % a == 0) & (d % 10 != 0) & (tho % a != 0) & (hun % a != 0) & (ten % a != 0):
            break

    b = round(d / 10, 1)
    c = round(b / a, 1)

    if a == 2 or a == 4 or a == 5 or a == 9:
        rur1 = "를"
    else:
        rur1 = "을"

    if (str(b))[-1] == "2" or (str(b))[-1] == "4" or (str(b))[-1] == "5" or (str(b))[-1] == "9":
        ga1 = "가"
    else:
        ga1 = "이"


    stem = stem.format(a=a, b=b, rur1=rur1, ga1=ga1)
    answer = answer.format(c=c)
    comment = comment.format(a=a, b=b, c=c)

    return stem, answer, comment


























# 6-1-3-24
def decimaldiv613_Stem_020():
    stem = "다음 수 중에서 가장 큰 수를 $$수식$${a}$$/수식$${ro1} 나눈 몫을 구해 보세요.\n$$표$$$$수식$${sb}$$/수식$$    $$수식$${sc}$$/수식$$    $$수식$${sd}$$/수식$$    $$수식$${se}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${f}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${b} ` &gt; ` {c} ` &gt; ` {d} ` &gt; ` {e}$$/수식$$이므로 가장 큰 수는 $$수식$${b}$$/수식$$입니다.\n" \
              "따라서 $$수식$${b} ` div ` {a} ` = ` {f}$$/수식$$입니다.\n\n"


    while True:
        a = np.random.randint(10, 100)
        k = np.random.randint(1000, 10000)
        l = np.random.randint(1000, 10000)
        m = np.random.randint(1000, 10000)
        n = np.random.randint(1000, 10000)
        tho = k // 100

        if (k % a == 0) & (k % 10 != 0) & (tho % a != 0):
            if (k > l) & (k > m) & (k > n) & (l > m) & (l > n) & (m > n):
                break

    b = k / 10
    c = l / 10
    d = m / 10
    e = n / 10

    f = round((b / a), 4)

    candidates = [b, c, d, e]
    np.random.shuffle(candidates)
    sb, sc, sd, se = candidates


    if (str(a))[-1] == "0" or (str(a))[-1] == "3" or (str(a))[-1] == "6":
        ro1 = "으로"
    else:
        ro1 = "로"

    stem = stem.format(a=a, sb=sb, sc=sc, sd=sd, se=se, ro1=ro1)
    answer = answer.format(f=f)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f)

    return stem, answer, comment






















# 6-1-3-25
def decimaldiv613_Stem_021():
    stem = "둘레가 $$수식$${a} rm {{cm}}$$/수식$$인 정사각형의 넓이는 몇 $$수식$$rm {{cm}}^2$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${b} rm {{cm}}^2$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$정사각형의 한 변의 길이$$수식$$RIGHT ) ` = `` LEFT ($$/수식$$둘레$$수식$$RIGHT ) ` div ` 4$$/수식$$\n" \
              "$$수식$$= ` {a} ` div ` 4 ` = ` {c} ` LEFT ( rm {{cm}} RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$정사각형의 넓이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$한 변의 길이$$수식$$RIGHT ) ` times ` LEFT ($$/수식$$한 변의 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {c} ` times ` {c} ` = ` {b} ` LEFT ( rm {{cm}}^2 RIGHT )$$/수식$$\n\n"


    while True:
        e = np.random.randint(100, 1000)
        hun = e // 100
        ten = (e // 10) % 10
        if (e % 4 == 0) & (e % 10 != 0) & (hun % 4 != 0) & (ten % 4 != 0):
            break

    a = e / 10
    c = (a / 4)
    b = round(c * c, 2)

    stem = stem.format(a=a)
    answer = answer.format(b=b)
    comment = comment.format(a=a, b=b, c=c)

    return stem, answer, comment
















# 6-1-3-29
def decimaldiv613_Stem_022():
    stem = "빈 곳에 알맞은 수를 써넣으세요.\n$$수식$${box_a}$$/수식$$ → $$수식$${box_b}$$/수식$$ → $$수식$${box_one}$$/수식$$\n"
    answer = "(정답)\n$$수식$${c}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` = ` {c}$$/수식$$\n\n"


    one = "㉠"

    while True:
        b = np.random.randint(2, 10)
        d = np.random.randint(100, 1000)
        a = d / 100
        if (d % 10 != 0) & (d % b == 0) & (a < b * 100):
            c = round(a / b, 2)
            if c < 1:
                break

    box_a = "box{%s}" % a
    box_b = "`div`box{%s}" % b
    box_one = "box{%s``````````}" % one

    # stem = stem.format(one=one, a=a, b=b)
    stem = stem.format(box_a=box_a, box_b=box_b, box_one=box_one)
    answer = answer.format(c=c)
    comment = comment.format(a=a, b=b, c=c)

    return stem, answer, comment
















# 6-1-3-30
def decimaldiv613_Stem_023():
    stem = "계산 결과를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${a} ` div ` {b}$$/수식$$  ○  $$수식$${c} ` div ` {d}$$/수식$$\n"
    answer = "(정답)\n$$수식$${t}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` = ` {e} `$$/수식$$, $$수식$${c} ` div ` {d} ` = ` {f}$$/수식$$\n" \
              "$$수식$${e} ` {t} ` {f}$$/수식$$이므로 $$수식$${a} ` div ` {b} ` {t} ` {c} ` div ` {d}$$/수식$$입니다.\n\n"


    while True:
        b = np.random.randint(2, 10)
        g = np.random.randint(100, 1000)
        d = np.random.randint(2, 10)
        h = np.random.randint(100, 1000)
        if (g % b == 0) & (h % d == 0) & (b != d):
            if (g < b * 100) & (h < d * 100):
                a = round(g / 100, 2)
                c = round(h / 100, 2)
                e = round(a / b, 3)
                f = round(c / d, 3)

                a = show_int(a)
                c = show_int(c)
                e = show_int(e)
                f = show_int(f)
                if e < 1 and f < 1:
                    break

    if e > f:
        t = "&gt;"
    elif e < f:
        t = "&lt;"
    elif e == f:
        t = "="

    stem = stem.format(a=a, b=b, c=c, d=d, e=e, f=f, t=t)
    answer = answer.format(t=t)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f, t=t)

    return stem, answer, comment



























# 6-1-3-31
def decimaldiv613_Stem_024():
    stem = "다음 중 계산 결과가 잘못된 것은 어느 것인가요?\n① {sa}\n② {sb}\n③ {sc}\n④ {sd}\n⑤ {se}\n"
    answer = "(정답)\n{k}\n"
    comment = "(해설)\n" \
              "{k} 나누어지는 수가 $$수식$$1 over 100$$/수식$$배가 되면 몫도 $$수식$$1 over 100$$/수식$$배가 됩니다.\n" \
              "{aa}\n\n"


    # while True:
    #     b = np.random.randint(2, 10)
    #     a = np.random.randint(10, 100)
    #     if (a % b == 0) & (a % 10 != 0):
    #         g = np.random.randint(2, 10)
    #         f = np.random.randint(100, 1000)
    #         if (f % g == 0) & (f < g * 100) & (f % 10 != 0):
    #             l = np.random.randint(2, 10)
    #             k = np.random.randint(10, 100)
    #             if (k % l == 0) & (k < l * 10) & (k % 10 != 0):
    #                 q = np.random.randint(2, 10)
    #                 p = np.random.randint(10, 100)
    #                 if (p % q == 0) & (p > q * 10) & (p % 10 != 0):
    #                     v = np.random.randint(2, 10)
    #                     u = np.random.randint(100, 1000)
    #                     if (u % v == 0) & (u < v * 100) & (u % 10 != 0):
    #                         break

    # 위의 코드는 계산이 너무 느림

    while True:
        b = np.random.randint(2, 10)
        a = np.random.randint(10, 100)
        if (a % b == 0) & (a % 10 != 0):
            break

    while True:
        g = np.random.randint(2, 10)
        f = np.random.randint(100, 1000)
        if (f % g == 0) & (f < g * 100) & (f % 10 != 0):
            break

    while True:
        l = np.random.randint(2, 10)
        k = np.random.randint(10, 100)
        if (k % l == 0) & (k < l * 10) & (k % 10 != 0):
            break

    while True:
        q = np.random.randint(2, 10)
        p = np.random.randint(10, 100)
        if (p % q == 0) & (p > q * 10) & (p % 10 != 0):
            break

    while True:
        v = np.random.randint(2, 10)
        u = np.random.randint(100, 1000)
        if (u % v == 0) & (u < v * 100) & (u % 10 != 0):
            break

    d = a / 100
    i = f / 100
    n = k / 10
    s = p / 100
    x = u / 100

    c = int(a / b)
    h = int(f / g)
    m = int(k / l)
    r = int(p / q)
    w = int(u / v)

    e = d / b
    j = i / g
    o = n / l
    t = r / 10
    z = s / q
    y = x / v

    sa = "$$수식$$%d ` div ` %d ` = ` %d `$$/수식$$ → $$수식$$` %.2f ` div ` %d ` = ` %.2f$$/수식$$" % (a, b, c, d, b, e)
    sb = "$$수식$$%d ` div ` %d ` = ` %d `$$/수식$$ → $$수식$$` %.2f ` div ` %d ` = ` %.2f$$/수식$$" % (f, g, h, i, g, j)
    sc = "$$수식$$%d ` div ` %d ` = ` %d `$$/수식$$ → $$수식$$` %.1f ` div ` %d ` = ` %.1f$$/수식$$" % (k, l, m, n, l, o)
    sd = "$$수식$$%d ` div ` %d ` = ` %d `$$/수식$$ → $$수식$$` %.2f ` div ` %d ` = ` %.1f$$/수식$$" % (p, q, r, s, q, t)
    se = "$$수식$$%d ` div ` %d ` = ` %d `$$/수식$$ → $$수식$$` %.2f ` div ` %d ` = ` %.2f$$/수식$$" % (u, v, w, x, v, y)

    ans = sd

    candidates = [sa, sb, sc, sd, se]
    np.random.shuffle(candidates)
    sa, sb, sc, sd, se = candidates

    for idx, sdx in enumerate(candidates):
        if sdx == ans:
             correct_idx = idx
             break

    k = answer_dict[correct_idx]

    aa = "$$수식$$%s ` div ` %s ` = ` %s `$$/수식$$ → $$수식$$` %s ` div ` %s ` = ` %s$$/수식$$" % (p, q, r, s, q, z)

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)
    answer = answer.format(k=k)
    comment = comment.format(k=k, aa=aa)

    return stem, answer, comment





















# 6-1-3-32
def decimaldiv613_Stem_025():
    stem = "빈 곳에 알맞은 수를 써넣으세요.\n{box_a}→$$수식$$LEFT ( `` div `` RIGHT )$$/수식$${box_b}→{box_one}\n"
    answer = "(정답)\n$$수식$${c}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` = ` {c}$$/수식$$\n\n"


    one = "㉠"

    while True:
        b = np.random.randint(2, 10)
        d = np.random.randint(100, 1000)
        a = d / 100
        if (d % 10 != 0) & (d % b == 0) & (a < b * 100):
            c = round(a / b, 2)
            if c < 1:
                break

    box_a = "$$수식$$box{%s}$$/수식$$" % a
    box_b = "$$수식$$box{%s}$$/수식$$" % b
    box_one = "$$수식$$box{%s````````````````````}$$/수식$$" % one

    # stem = stem.format(one=one, a=a, b=b)
    stem = stem.format(box_a=box_a, box_b=box_b, box_one=box_one)
    answer = answer.format(c=c)
    comment = comment.format(a=a, b=b, c=c)

    return stem, answer, comment


















# 6-1-3-33
def decimaldiv613_Stem_026():
    stem = "다음 중 나눗셈의 몫이 $$수식$$1$$/수식$$보다 작은 것은 어느 것인가요?\n① $$수식$${sa}$$/수식$$    ② $$수식$${sb}$$/수식$$    ③ $$수식$${sc}$$/수식$$\n④ $$수식$${sd}$$/수식$$    ⑤ $$수식$${se}$$/수식$$\n"
    answer = "(정답)\n{k}\n"
    comment = "(해설)\n" \
              "나누는 수가 나누어지는 수보다 크면 몫이 $$수식$$1$$/수식$$보다 작게 됩니다.\n" \
              "따라서 나눗셈의 몫이 $$수식$$1$$/수식$$보다 작은 것은 {k}입니다.\n" \
              "① $$수식$${aa}$$/수식$$\n" \
              "② $$수식$${ab}$$/수식$$\n" \
              "③ $$수식$${ac}$$/수식$$\n" \
              "④ $$수식$${ad}$$/수식$$\n" \
              "⑤ $$수식$${ae}$$/수식$$\n\n"


    # while True:
    #     b = np.random.randint(2, 15)
    #     q = np.random.randint(1000, 10000)
    #     if (q % b == 0) & (q % 10 != 0) & (q > b * 100):
    #         d = np.random.randint(2, 15)
    #         r = np.random.randint(100, 1000)
    #         if (r % d == 0) & (r < d * 100) & (r % 10 != 0):
    #             f = np.random.randint(2, 15)
    #             s = np.random.randint(100, 1000)
    #             if (s % f == 0) & (s > f * 10) & (s % 10 != 0):
    #                 h = np.random.randint(2, 15)
    #                 t = np.random.randint(100, 1000)
    #                 if (t % h == 0) & (t > h * 100) & (t % 10 != 0):
    #                     j = np.random.randint(2, 15)
    #                     u = np.random.randint(1000, 10000)
    #                     if (u % j == 0) & (u > j * 100) & (u % 10 != 0):
    #                         break

    # 위 코드의 경우, 계산 속도가 너무 느림

    while True:
        b = np.random.randint(2, 15)
        q = np.random.randint(1000, 10000)
        if (q % b == 0) & (q % 10 != 0) & (q > b * 100):
            break

    while True:
        d = np.random.randint(2, 15)
        r = np.random.randint(100, 1000)
        if (r % d == 0) & (r < d * 100) & (r % 10 != 0):
            break

    while True:
        f = np.random.randint(2, 15)
        s = np.random.randint(100, 1000)
        if (s % f == 0) & (s > f * 10) & (s % 10 != 0):
            break

    while True:
        h = np.random.randint(2, 15)
        t = np.random.randint(100, 1000)
        if (t % h == 0) & (t > h * 100) & (t % 10 != 0):
            break

    while True:
        j = np.random.randint(2, 15)
        u = np.random.randint(1000, 10000)
        if (u % j == 0) & (u > j * 100) & (u % 10 != 0):
            break


    a = q / 100
    c = r / 100
    e = s / 10
    g = t / 10
    i = u / 100

    l = a / b
    m = c / d
    n = e / f
    o = g / h
    p = i / j

    sa = "%.2f`div`%d" % (a, b)
    sb = "%.2f`div`%d" % (c, d)
    sc = "%.1f`div`%d" % (e, f)
    sd = "%.1f`div`%d" % (g, h)
    se = "%.2f`div`%d" % (i, j)

    aa = "%.2f`div`%d`=`%.2f" % (a, b, l)
    ab = "%.2f`div`%d`=`%.2f" % (c, d, m)
    ac = "%.1f`div`%d`=`%.1f" % (e, f, n)
    ad = "%.1f`div`%d`=`%.1f" % (g, h, o)
    ae = "%.2f`div`%d`=`%.2f" % (i, j, p)

    candidates = [[sa, aa], [sb, ab], [sc, ac], [sd, ad], [se, ae]]
    ans = candidates[1]
    np.random.shuffle(candidates)
    [sa, aa], [sb, ab], [sc, ac], [sd, ad], [se, ae] = candidates

    for i, s in enumerate(candidates):
        if s == ans:
             correct_idx = i
             break

    k = answer_dict[correct_idx]

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)
    answer = answer.format(k=k)
    comment = comment.format(aa=aa, ab=ab, ac=ac, ad=ad, ae=ae, k=k)

    return stem, answer, comment



























# 6-1-3-35
def decimaldiv613_Stem_027():
    stem = "무게가 같은 {t} $$수식$${a}$$/수식$$개의 무게는 $$수식$${b}rm kg$$/수식$$입니다. {t} 한 개의 무게는 몇 $$수식$$rm kg$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${c} rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${t} 한 개의 무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$${t} $$수식$${a}$$/수식$$개의 무게$$수식$$RIGHT ) ` div ` {a}$$/수식$$\n" \
              "$$수식$$= ` {b} ` div ` {a} ` = ` {c} ` LEFT ( rm kg RIGHT )$$/수식$$\n\n"


    t = ["통조림", "야구공", "연필", "필통", "지우개", "볼펜"][np.random.randint(0, 6)]

    while True:
        a = np.random.randint(2, 20)
        d = np.random.randint(100, 1000)
        if (d % a == 0) & (d % 10 != 0) & (d < a * 100):
            break

    b = d/100
    c = round(b/a, 2)

    stem = stem.format(t=t, a=a, b=b)
    answer = answer.format(c=c)
    comment = comment.format(a=a, b=b, c=c, t=t)

    return stem, answer, comment


































# 6-1-3-36
def decimaldiv613_Stem_028():
    stem = "$$수식$${a}$$/수식$${eun1} ㉠의 몇 배인가요?\n$$표$$$$수식$${a} ` div ` {b} ` = ` {c}$$/수식$$ → ㉠$$수식$$` div ` {b} ` = ` {d}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${e}$$/수식$$배\n"
    comment = "(해설)\n" \
              "나누는 수가 $$수식$${b}$$/수식$${ro1} 같고 몫인 $$수식$${c}$$/수식$${eun2} $$수식$${d}$$/수식$$의 $$수식$${e}$$/수식$$배이므로 나누어지는 수인 $$수식$${a}$$/수식$$도 ㉠의 $$수식$${e}$$/수식$$배입니다.\n\n"


    while True:
        b = np.random.randint(2, 10)
        a = np.random.randint(100, 1000)
        if (a % b == 0) & (a % 10 != 0) & (a < b * 100):
            break

    c = int(a / b)
    e = [10, 100][np.random.randint(0, 2)]
    l = a / e
    d = round(l / b, 4)

    eun1 = josa((str(a))[-1], "은")

    ro1 = josa((str(b))[-1], "로")

    eun2 = josa((str(c))[-1], "은")

    stem = stem.format(a=a, b=b, c=c, d=d, eun1=eun1)
    answer = answer.format(e=e)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, ro1=ro1, eun2=eun2)

    return stem, answer, comment

























# 6-1-3-37
def decimaldiv613_Stem_029():
    stem = "물이 일정하게 나오는 어떤 수도에서 $$수식$${a}$$/수식$$시간 $$수식$${b}$$/수식$$분 동안 물 $$수식$${c} rm L$$/수식$$가 나왔습니다. $$수식$$1$$/수식$$분 동안 나온 물은 몇 $$수식$$rm L$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${d} rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$1$$/수식$$시간$$수식$$` = ` 60$$/수식$$분이므로 $$수식$${a}$$/수식$$시간 $$수식$${b}$$/수식$$분$$수식$$` = ` {e}$$/수식$$분입니다.\n" \
              "$$수식$$LEFT ( 1$$/수식$$분 동안 나온 물의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$전체 물의 양$$수식$$RIGHT ) ` div ` LEFT ($$/수식$$물이 나온 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {c} ` div ` {e} ` = ` {d} ` LEFT ( rm L RIGHT )$$/수식$$\n\n"


    while True:
        a = np.random.randint(2, 10)
        b = np.random.randint(1, 60)
        e = a * 60 + b
        f = np.random.randint(100, 1000)

        if (f % e == 0) & (f % 10 != 0) & (f < e * 100):
            break

    c = f / 100
    d = round(c / e, 2)

    stem = stem.format(a=a, b=b, c=c)
    answer = answer.format(d=d)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e)

    return stem, answer, comment


























# 6-1-3-38
def decimaldiv613_Stem_030():
    stem = "한 변이 $$수식$${a} rm m$$/수식$$인 정사각형 모양의 벽을 흰색 페인트 $$수식$${b} rm L$$/수식$$를 사용하여 칠했습니다. $$수식$$1 rm m^2$$/수식$$의 벽을 칠하는 데 사용한 페인트는 몇 $$수식$$rm L$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${c} rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$벽의 넓이$$수식$$RIGHT ) ` = ` {a} ` times ` {a} ` = ` {d} ` LEFT ( ` rm m^2 RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ( 1 ` rm m^2$$/수식$$의 벽을 칠하는 데 사용한 페인트 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {b} ` div ` {d} ` = ` {c} ` LEFT ( rm L RIGHT )$$/수식$$\n\n"


    while True:
        a = np.random.randint(2, 10)
        d = a * a
        e = np.random.randint(100, 1000)
        if (e % d == 0) & (e % 10 != 0) & (e < d * 100):
            break

    b = e / 100
    c = round(b / d, 2)

    stem = stem.format(a=a, b=b)
    answer = answer.format(c=c)
    comment = comment.format(a=a, b=b, c=c, d=d)

    return stem, answer, comment
















# 6-1-3-41
def decimaldiv613_Stem_031():
    stem = "빈 곳에 알맞은 수를 써넣으세요.\n$$수식$${box_a}$$/수식$$ → $$수식$${box_b}$$/수식$$ → $$수식$${box_one}$$/수식$$\n$$수식$${box_c}$$/수식$$ → $$수식$${box_d}$$/수식$$ → $$수식$${box_two}$$/수식$$\n"
    answer = "(정답)\n$$수식$${e}$$/수식$$, $$수식$${f}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` = ` {e}$$/수식$$, $$수식$${c} ` div ` {d} ` = ` {f}$$/수식$$\n\n"


    one = "㉠"
    two = "㉡"


    # while True:
    #     b = np.random.randint(2, 10)
    #     g = np.random.randint(1000, 10000)
    #     tho = g // 100
    #     ten = (g // 10) % 10
    #     if (g % 10 != 0) & (g % b == 0) & (ten < b) & (tho % b != 0):
    #         break


    while True:
        b = np.random.randint(2, 10)
        g_front = np.random.randint(5, 50)
        g_back1 = np.random.randint(0, b)
        g_back2 = np.random.randint(1, 10)
        g = g_front * b * 100 + g_back1 * 10 + g_back2
        if g % b == 0 and g_front * b < 100:
            break


    # while True:
    #     d = np.random.randint(10, 100)
    #     if d % 10 != 0:
    #         h = np.random.randint(1000, 10000)
    #         tho = h // 100
    #         ten = h - ((h // 100) * 10)
    #         if (h % 10 == 0) & (h % d == 0) & (ten % d != 0) & (tho % d != 0):
    #             break


    while True:
        d = np.random.randint(10, 100)
        h_front = np.random.randint(1, 10)
        h_back = np.random.randint(1, 10)
        h = h_front * d * 100 + h_back * d
        if h % 10 == 0 and h_front * d < 100 and h_back * d < 100:
            break


    a = g / 100
    c = h / 100

    e = round(a / b, 2)
    f = round(c / d, 2)


    box_a = "box{%s}" % a
    box_b = "`div`$$/수식$$ $$수식$$box{%s}" % b
    box_one = "box{%s``````````}" % one
    box_c = "box{%s}" % c
    box_d = "`div`$$/수식$$ $$수식$$box{%s}" % d
    box_two = "box{%s``````````}" % two


    # stem = stem.format(one=one, two=two, a=a, b=b, c=c, d=d)
    stem = stem.format(box_a=box_a, box_b=box_b, box_one=box_one, box_c=box_c, box_d=box_d, box_two=box_two)
    answer = answer.format(e=e, f=f)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f)

    return stem, answer, comment


















# 6-1-3-42
def decimaldiv613_Stem_032():
    stem = "가장 큰 수를 가장 작은 수로 나눈 몫을 구해 보세요.\n$$표$$$$수식$${sa}$$/수식$$    $$수식$${sb}$$/수식$$    $$수식$${sc}$$/수식$$    $$수식$${sd}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${e}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${d} ` &gt; ` {a} ` &gt; ` {c} ` &gt; ` {b} `$$/수식$$이므로 가장 큰 수는 $$수식$${d}$$/수식$$이고, 가장 작은 수는 $$수식$${b}$$/수식$$입니다.\n" \
              "따라서 $$수식$${d} ` div ` {b} ` = ` {e} `$$/수식$$입니다.\n\n"


    while True:
        b = np.random.randint(2, 10)
        c = np.random.randint(2, 10)
        f = np.random.randint(100, 1000)
        hun = f // 10
        g = np.random.randint(10, 100)
        d = f / 100
        if (f % b == 0) & (hun % b != 0) & (f % 10 == 0):
            if (b < c):
                if (g % 10 != 0) & (c * 10 < g) & (g < d * 10):
                    break


    a = g / 10
    e = round(d / b, 2)

    candidates = [a, b, c, d]
    np.random.shuffle(candidates)
    sa, sb, sc, sd = candidates

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(e=e)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e)

    return stem, answer, comment

























# 6-1-3-43
def decimaldiv613_Stem_033():
    stem = "나눗셈의 몫이 더 큰 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${a} ` div ` {b}$$/수식$$    ㉡ $$수식$${c} ` div ` {d}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{k}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${a} ` div ` {b} ` = ` {e}$$/수식$$\n" \
              "㉡ $$수식$${c} ` div ` {d} ` = ` {f}$$/수식$$\n" \
              "따라서 $$수식$${g} ` &lt; ` {h}$$/수식$$이므로 나눗셈의 몫이 더 큰 것은 {k}입니다.\n\n"


    while True:
        b = np.random.randint(10, 100)
        m = np.random.randint(1000, 10000)
        mmul = m // 10
        if (m % b == 0) & (m % 10 == 0) & (mmul % b != 0):
            d = np.random.randint(10, 100)
            n = np.random.randint(1000, 10000)
            nmul = n // 10
            if (n % d == 0) & (n % 10 == 0) & (nmul % d != 0):
                a = m / 100
                c = n / 100
                e = round(a / b, 2)
                f = round(c / d, 2)
                if (e != f):
                    break

    if e > f:
        g = f
        h = e
        k = "㉠"

    elif e < f:
        g = e
        h = f
        k = "㉡"


    stem = stem.format(a=a, b=b, c=c, d=d)
    answer = answer.format(k=k)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, k=k)

    return stem, answer, comment


























# 6-1-3-44
def decimaldiv613_Stem_034():
    stem = "계산 결과를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${a} ` div ` {b}$$/수식$$  ○  $$수식$${c} ` div ` {d}$$/수식$$\n"
    answer = "(정답)\n$$수식$${k}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` = ` {e} `$$/수식$$, $$수식$${c} ` div ` {d} ` = ` {f} `$$/수식$$\n" \
              "따라서 $$수식$${e} ` {k} ` {f}$$/수식$$이므로 $$수식$${i} ` {k} ` {j}$$/수식$$입니다.\n\n"


    while True:
        b = np.random.randint(2, 10)
        m = np.random.randint(100, 1000)
        hun = m // 10
        if (m % b == 0) & (m % 10 == 0) & (hun % b != 0):
            break

    while True:
        d = np.random.randint(2, 10)
        n = np.random.randint(100, 1000)
        hun = n // 10
        if (n % d == 0) & (n % 10 == 0) & (hun % d != 0):
            break

    a = round(m / 100, 2)
    c = round(n / 100, 2)
    e = round(a/b, 3)
    f = round(c/d, 3)

    a = show_int(a)
    c = show_int(c)
    e = show_int(e)
    f = show_int(f)

    i = "%s ` div ` %s" % (a, b)
    j = "%s ` div ` %s" % (c, d)

    if e > f:
        k = "` &gt; `"
    elif e < f:
        k = "` &lt; `"
    elif e == f:
        k = "` = `"


    stem = stem.format(a=a, b=b, c=c, d=d)
    answer = answer.format(k=k)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f, i=i, j=j, k=k)

    return stem, answer, comment


























# 6-1-3-45
def decimaldiv613_Stem_035():
    stem = "큰 수를 작은 수로 나눈 몫을 구해 보세요.\n$$표$$$$수식$${sa}$$/수식$$           $$수식$${sb}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${c}$$/수식$$\n"
    comment = "(해설)\n" \
              "큰 수를 작은 수로 나누면\n" \
              "$$수식$${a} ` div ` {b} ` = ` {c}$$/수식$$\n\n"


    while True:
        b = np.random.randint(2, 10)
        m = np.random.randint(1000, 10000)
        mmul = m // 10
        if (m % b == 0) & (m % 10 == 0) & (mmul % b != 0):
            break

    a = m / 100
    c = round(a / b, 2)

    cand = [a, b]
    np.random.shuffle(cand)
    sa, sb = cand


    stem = stem.format(sa=sa, sb=sb)
    answer = answer.format(c=c)
    comment = comment.format(a=a, b=b, c=c)

    return stem, answer, comment


















# 6-1-3-46
def decimaldiv613_Stem_036():
    stem = "빈 곳에 알맞은 수를 써넣으세요.\n$$수식$${box_a}$$/수식$$ → $$수식$${box_b}$$/수식$$ → $$수식$${box_one}$$/수식$$\n"
    answer = "(정답)\n$$수식$${c}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` = ` {c}$$/수식$$\n\n"


    one = "㉠"

    while True:
        b = np.random.randint(2, 10)
        m = np.random.randint(1000, 10000)
        tho = m // 10
        if (m % 10 == 0) and (m % b == 0) and (tho % b != 0):
            break

    a = m / 100
    c = round(a / b, 2)

    box_a = "box{%s}" % a
    box_b = "`div`box{%s}" % b
    box_one = "box{%s``````````}" % one

    # stem = stem.format(a=a, b=b, one=one)
    stem = stem.format(box_a=box_a, box_b=box_b, box_one=box_one)
    answer = answer.format(c=c)
    comment = comment.format(a=a, b=b, c=c)

    return stem, answer, comment





















# 6-1-3-47
def decimaldiv613_Stem_037():
    stem = "다음 중 세로로 나누어떨어질 때까지 계산할 때 소수점 아래 $$수식$$0$$/수식$$을 내려 계산하지 않는 것은 어느 것인가요?\n① $$수식$${sa}$$/수식$$    ② $$수식$${sb}$$/수식$$    ③ $$수식$${sc}$$/수식$$\n④ $$수식$${sd}$$/수식$$    ⑤ $$수식$${se}$$/수식$$\n"
    answer = "(정답)\n{k}\n"
    comment = "(해설)\n" \
              "① $$수식$${aa}$$/수식$$    ② $$수식$${ab}$$/수식$$\n" \
              "③ $$수식$${ac}$$/수식$$    ④ $$수식$${ad}$$/수식$$\n" \
              "⑤ $$수식$${ae}$$/수식$$\n\n"



    while True:
        b = np.random.randint(2, 10)
        q = np.random.randint(100, 1000)
        qhun = q // 10
        if (q % b == 0) & (q % 10 == 0) & (qhun % b != 0):
            break

    while True:
        d = np.random.randint(2, 10)
        r = np.random.randint(1000, 10000)
        rhun = r // 10
        if (r % d == 0) & (rhun % d != 0) & (r % 10 == 0):
            break

    while True:
        f = np.random.randint(10, 100)
        s = np.random.randint(1000, 10000)
        shun = s // 10
        if (s % f == 0) & (shun % f != 0) & (s % 10 == 0):
            break

    while True:
        h = np.random.randint(2, 10)
        t = np.random.randint(100, 1000)
        if (t % h == 0) & (t % 10 != 0):
            break

    while True:
        j = np.random.randint(2, 10)
        u = np.random.randint(1000, 10000)
        uhun = u // 10
        if (u % j == 0) & (uhun % j != 0) & (u % 10 == 0):
            break


    a = q / 100
    c = r / 100
    e = s / 100
    g = t / 10
    i = u / 100

    # l = a / b
    # m = c / d
    # n = e / f
    # o = g / h
    # p = i / j
    #
    # sa = "%.1f`div`%d" % (a, b)
    # sb = "%.1f`div`%d" % (c, d)
    # sc = "%.1f`div`%d" % (e, f)
    # sd = "%.1f`div`%d" % (g, h)
    # se = "%.1f`div`%d" % (i, j)
    #
    # aa = "%.1f`div`%d`=`%.2f" % (a, b, l)
    # ab = "%.1f`div`%d`=`%.2f" % (c, d, m)
    # ac = "%.1f`div`%d`=`%.2f" % (e, f, n)
    # ad = "%.1f`div`%d`=`%.2f" % (g, h, o)
    # ae = "%.1f`div`%d`=`%.2f" % (i, j, p)

    l = round(a / b, 4)
    m = round(c / d, 4)
    n = round(e / f, 4)
    o = round(g / h, 4)
    p = round(i / j, 4)

    sa = "%.1f ` div ` %d" % (a, b)
    sb = "%.1f ` div ` %d" % (c, d)
    sc = "%.1f ` div ` %d" % (e, f)
    sd = "%.1f ` div ` %d" % (g, h)
    se = "%.1f ` div ` %d" % (i, j)

    aa = "%.1f ` div ` %d ` = ` %s" % (a, b, l)
    ab = "%.1f ` div ` %d ` = ` %s" % (c, d, m)
    ac = "%.1f ` div ` %d ` = ` %s" % (e, f, n)
    ad = "%.1f ` div ` %d ` = ` %s" % (g, h, o)
    ae = "%.1f ` div ` %d ` = ` %s" % (i, j, p)

    candidates = [[sa, aa], [sb, ab], [sc, ac], [sd, ad], [se, ae]]
    ans = candidates[3]

    np.random.shuffle(candidates)
    [sa, aa], [sb, ab], [sc, ac], [sd, ad], [se, ae] = candidates

    for i, s in enumerate(candidates):
        if s == ans:
             correct_idx = i
             break

    k = answer_dict[correct_idx]

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)
    answer = answer.format(k=k)
    comment = comment.format(aa=aa, ab=ab, ac=ac, ad=ad, ae=ae)

    return stem, answer, comment























# 6-1-3-48
def decimaldiv613_Stem_038():
    stem = "{t} $$수식$${a} rm L$$/수식$$를 컵 $$수식$${b}$$/수식$$개에 똑같이 나누어 담으려고 합니다. 컵 한 개에 담을 수 있는 {t}{nun1} 몇 $$수식$$rm L$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${c} rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$컵 한 개에 담을 수 있는 우유의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$전체 우유의 양$$수식$$RIGHT ) ` div ` LEFT ($$/수식$$컵의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {a} ` div ` {b} ` = ` {c} ` LEFT ( rm L RIGHT )$$/수식$$\n\n"


    t = ["우유", "음료수", "물"][np.random.randint(0, 3)]

    while True:
        b = np.random.randint(2, 10)
        d = np.random.randint(100, 1000)
        hun = d // 10
        if (d % b == 0) & (d % 10 == 0) & (hun % b != 0):
            break

    a = d / 100
    c = round(a / b, 2)

    nun1 = proc_jo(t, -1)

    stem = stem.format(a=a, b=b, t=t, nun1=nun1)
    answer = answer.format(c=c)
    comment = comment.format(a=a, b=b, c=c)

    return stem, answer, comment
























# 6-1-3-51
def decimaldiv613_Stem_039():
    stem = "어떤 수를 $$수식$${a}$$/수식$${ro1} 나누어야 할 것을 잘못하여 어떤 수에 $$수식$${b}$$/수식$${rur1} 곱하였더니 $$수식$${c}$$/수식$${ga1} 되었습니다. 바르게 계산하면 얼마인가요?\n"
    answer = "(정답)\n$$수식$${e}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □ 라고 하면\n" \
              "□$$수식$$` times ` {b} ` = ` {c}$$/수식$$  →  □$$수식$$` = ` {c} ` div ` {b} ` = ` {d}$$/수식$$입니다.\n" \
              "따라서 바르게 계산하면 $$수식$${d} ` div ` {a} ` = ` {e}$$/수식$$입니다.\n\n"


    # while True:
    #     a = np.random.randint(2, 10)
    #     b = np.random.randint(2, 10)
    #     f = np.random.randint(1000, 10000)
    #     hun = f // 10
    #     if (f % b == 0) & (f % a == 0) & (f % 10 == 0) & (hun % b != 0):
    #         break
    #
    # c = f / 100
    # d = round(c / b, 2)
    # e = round(d / a, 2)

    while True:
        a = np.random.randint(2, 10)
        b = np.random.randint(2, 10)
        f = np.random.randint(1000, 10000)
        hun = f // 10

        c = f / 100
        d = round(c / b, 2)
        e = round(d / a, 2)

        if (f % b == 0) and (f % a == 0) and (f % 10 == 0) and (hun % b != 0) and (d*100) % a == 0:
            break


    ro1 = josa(a, "로")

    rur1 = josa(b, "를")

    ga1 = josa((str(c))[-1], "가")

    stem = stem.format(a=a, b=b, c=c, ro1=ro1, rur1=rur1, ga1=ga1)
    answer = answer.format(e=e)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e)

    return stem, answer, comment























# 6-1-3-52
def decimaldiv613_Stem_040():
    stem = "{t}{j1} 한 상자에 $$수식$${a} rm kg$$/수식$$씩 들어 있는 사과를 $$수식$${b}$$/수식$$상자 샀습니다. 이 사과를 봉지 $$수식$${c}$$/수식$$개에 똑같이 나누어 담았을 때 한 봉지에 들어 있는 사과의 무게는 몇 $$수식$$rm kg$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${e} rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${t}{j2} 산 사과의 무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$한 상자에 들어 있는 사과의 무게$$수식$$RIGHT ) ` times ` LEFT ($$/수식$$상자 수$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` {a} ` times ` {b} ` = ` {d} LEFT ( rm kg RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$한 봉지에 들어 있는 사과의 무게$$수식$$RIGHT )$$/수식$$\n$$수식$$= ` LEFT ($$/수식$${t}{j2} 산 사과의 무게$$수식$$RIGHT ) ` div ` LEFT ($$/수식$$봉지 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {d} ` div ` {c} ` = ` {e} ` LEFT ( rm kg RIGHT )$$/수식$$\n\n"


    t = ["수지", "경미", "영수", "철민", "승보", "경민"][np.random.randint(0, 6)]

    j1 = proc_jo(t, -1)
    j2 = proc_jo(t, 0)

    while True:
        b = np.random.randint(10, 100)
        c = np.random.randint(10, 100)
        f = np.random.randint(1000, 10000)
        hun = f // 10
        if (f % b == 0) and (f % c == 0) and (f % 10 == 0) and (hun % c != 0):
            if b % 2 == 0 or b % 3 == 0 or b % 5 == 0:
                if c % 2 == 0 or c % 3 == 0 or c % 5 == 0:
                    break

    d = f / 100
    a = round(d / b, 2)
    e = round(d / c, 2)

    stem = stem.format(t=t, a=a, b=b, c=c, j1=j1)
    answer = answer.format(e=e)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, t=t, j2=j2)

    return stem, answer, comment
























# 6-1-3-54
def decimaldiv613_Stem_041():
    stem = "□ 안에 들어갈 수 있는 자연수를 모두 구해 보세요.\n$$표$$$$수식$${a} ` div ` {b} `` &lt; ``$$/수식$$□$$수식$$`` &lt; `` {c} ` div ` {d}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${g}$$/수식$$, $$수식$${h}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` = ` {e}$$/수식$$, $$수식$${c} ` div ` {d} ` = ` {f}$$/수식$$입니다.\n" \
              "$$수식$${e} `` &lt; ``$$/수식$$□$$수식$$`` &lt; `` {f}$$/수식$$이므로 □ 안에 들어갈 수 있는 자연수는 $$수식$${g}$$/수식$$, $$수식$${h}$$/수식$$입니다.\n\n"


    # while True:
    #     b = np.random.randint(2, 10)
    #     i = np.random.randint(1000, 10000)
    #     imul = i // 10
    #
    #     d = np.random.randint(2, 10)
    #     j = np.random.randint(1000, 10000)
    #     jmul = j // 10
    #
    #     a = i / 100
    #     c = j / 100
    #
    #     e = round(a / b, 2)
    #     f = round(c / d, 2)
    #
    #     if (i % b == 0) & (i % 10 == 0) & (imul % b != 0):
    #         if (j % d == 0) & (j % 10 == 0) & (jmul % d != 0):
    #             if (b != d) & (e < f):
    #                 break
    #
    # g = int(e) + 1
    # h = int(f)
    # ans = ""
    #
    # for i in range(g, h + 1):
    #     ans = ans + "$$수식$$%d$$/수식$$, " % i
    #
    # # ans = ans[:-5]
    # ans = ans[:-2]

    # 답이 2개 나오도록 조정


    while True:
        b = np.random.randint(2, 10)
        i_factor = np.random.randint(500, 5000)
        i = b * i_factor
        imul = i // 10

        d = np.random.randint(2, 10)
        j_factor = np.random.randint(500, 5000)
        j = d * j_factor
        jmul = j // 10

        a = i / 100
        c = j / 100

        e = round(a / b, 2)
        f = round(c / d, 2)

        g = int(e) + 1
        h = int(f)

        if (i % 10 == 0) and (imul % b != 0) and (j % 10 == 0) and (jmul % d != 0) and i < 10000 and j < 10000:
                if (b != d) and (e < f) and h-g == 1:
                    break


    stem = stem.format(a=a, b=b, c=c, d=d)
    answer = answer.format(g=g, h=h)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h)

    return stem, answer, comment






















# 6-1-3-56
def decimaldiv613_Stem_042():
    stem = "빈 곳에 큰 수를 작은 수로 나눈 몫을 소수로 써넣으세요.\n$$수식$${box_sa}$$/수식$$    $$수식$${box_sb}$$/수식$$ → $$수식$${box_one}$$/수식$$\n"
    answer = "(정답)\n$$수식$${c}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${b} ` div ` {a} ` = ` {c}$$/수식$$\n\n"


    one = "(답)"

    while True:
        a = np.random.randint(10, 100)
        f = np.random.randint(1000, 10000)
        tho = f // 100
        if (f % 100 == 0) & (f % a == 0) & (tho % a != 0) & (a % 10 != 0):
            break

    b = int(f / 100)
    c = b / a

    candidates = [a, b]
    np.random.shuffle(candidates)
    sa, sb = candidates

    box_sa = "box{%s}" % sa
    box_sb = "box{%s}" % sb
    box_one = "box{　　　}"


    # stem = stem.format(sa=sa, sb=sb, one=one)
    stem = stem.format(box_sa=box_sa, box_sb=box_sb, box_one=box_one)
    answer = answer.format(c=c)
    comment = comment.format(a=a, b=b, c=c)

    return stem, answer, comment


















# 6-1-3-57
def decimaldiv613_Stem_043():
    stem = "다음 중 자연수를 찾아 큰 수를 작은 수로 나눈 몫을 소수로 써 보세요.\n$$표$$$$수식$${sa}$$/수식$$    $$수식$${sb}$$/수식$$    $$수식$${sc}$$/수식$$    $$수식$${sd}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${e}$$/수식$$\n"
    comment = "(해설)\n" \
              "자연수는 $$수식$${b}$$/수식$$, $$수식$${c}$$/수식$$이고 $$수식$${c} ` &gt; ` {b}$$/수식$$이므로 큰 수는 $$수식$${c}$$/수식$$, 작은 수는 $$수식$${b}$$/수식$$입니다.\n" \
              "따라서 큰 수를 작은 수로 나누면 $$수식$${c} ` div ` {b} ` = ` {e}$$/수식$$입니다.\n\n"


    while True:
        j = np.random.randint(10, 100)
        k = np.random.randint(10, 100)
        b = np.random.randint(2, 10)
        q = np.random.randint(1000, 10000)
        tho = q // 100
        if (j % 10 != 0) & (k % 10 != 0) & (j != k):
            if (q % b == 0) & (q % 100 == 0) & (tho % b != 0):
                break

    a = j / 10
    d = k / 10
    c = int(q / 100)
    e = c / b

    candidates = [a, b, c, d]
    np.random.shuffle(candidates)
    sa, sb, sc, sd = candidates


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(e=e)
    comment = comment.format(b=b, c=c, d=d, e=e)

    return stem, answer, comment

























# 6-1-3-58
def decimaldiv613_Stem_044():
    stem = "몫이 큰 것부터 차례대로 기호를 써 보세요.\n$$표$$㉠ $$수식$${sa}$$/수식$$    ㉡ $$수식$${sb}$$/수식$$\n㉢ $$수식$${sc}$$/수식$$    ㉣ $$수식$${sd}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{k}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${sa} ` = ` {ai}$$/수식$$    ㉡ $$수식$${sb} ` = ` {aj}$$/수식$$\n" \
              "㉢ $$수식$${sc} ` = ` {al}$$/수식$$    ㉣ $$수식$${sd} ` = ` {am}$$/수식$$\n" \
              "$$수식$${max} ` &gt; ` {one} ` &gt; ` {two} ` &gt; ` {min} `$$/수식$$이므로 몫이 큰 것부터 차례대로 {k}입니다.\n\n"


    while True:
        while True:
            b = np.random.randint(2, 10)
            n = np.random.randint(1000, 10000)
            tho = n // 100
            if (n % b == 0) & (n % 100 == 0) & (tho % b != 0):
                break

        while True:
            d = np.random.randint(2, 10)
            o = np.random.randint(10, 100)
            tho = o // 10
            if (o % d == 0) & (o % 10 == 0) & (tho % d != 0):
                break

        while True:
            f = np.random.randint(2, 10)
            p = np.random.randint(1000, 10000)
            tho = p // 100
            if (p % f == 0) & (p % 100 == 0) & (tho % f != 0):
                break

        while True:
            h = np.random.randint(2, 10)
            q = np.random.randint(100, 1000)
            tho = q // 100
            if (q % h == 0) & (q % 100 == 0) & (tho % h != 0):
                break

        a = n / 100
        c = o / 10
        e = p / 100
        g = q / 100

        i = a / b
        j = c / d
        l = e / f
        m = g / h

        if a != c and a != e and a != g and c != e and c != g and e != g:
            if i != j and i != l and i != m and j != l and j != m and l != m:
                break

    sa = "%d ` div ` %d" % (a, b)
    sb = "%d ` div ` %d" % (c, d)
    sc = "%d ` div ` %d" % (e, f)
    sd = "%d ` div ` %d" % (g, h)


    candidates = [[sa, i], [sb, j], [sc, l], [sd, m]]
    np.random.shuffle(candidates)
    [sa, ai], [sb, aj], [sc, al], [sd, am] = candidates


    maxmin = [i, j, l, m]
    maxmin = sorted(maxmin, reverse=True)
    max, one, two, min = maxmin

    # k = ""
    #
    # for z, s in enumerate(maxmin):
    #     for v, x in enumerate(candidates):
    #         if x[1] == s:
    #             k = k + "%s, " % (answer_koonedict[v])
    #
    # k = k[:-2]

    # 위 코드의 경우, 원문자가 4개가 아니라 6개가 나오는 경우가 있음

    k = ""

    for idx in maxmin:
        if idx == ai:
            k += "㉠, "
        elif idx == aj:
            k += "㉡, "
        elif idx == al:
            k += "㉢, "
        elif idx == am:
            k += "㉣, "

    k = k[:-2]



    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(k=k)
    comment = comment.format(ai=ai, aj=aj, al=al, sa=sa, sb=sb, sc=sc, sd=sd, am=am, k=k, max=max, one=one, two=two, min=min)

    return stem, answer, comment

























# 6-1-3-59
def decimaldiv613_Stem_045():
    stem = "□ 안에 들어갈 수 있는 가장 큰 자연수를 구해 보세요.\n$$표$$$$수식$${a} ` div ` {b} ` &gt; `$$/수식$$□$$/표$$\n"
    answer = "(정답)\n$$수식$${e}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` = ` {c}`$$/수식$$이므로 □ 안에 들어갈 수 있는 자연수는 $$수식$${d}$$/수식$$부터 $$수식$${e}$$/수식$$까지입니다.\n" \
              "따라서 □ 안에 들어갈 수 있는 가장 큰 자연수는 $$수식$${e}$$/수식$$입니다.\n\n"


    while True:
        b = np.random.randint(2, 10)
        f = np.random.randint(100, 1000)
        tho = f // 10
        if (f % b == 0) & (f % 10 == 0) & (tho % b != 0):
            a = int(f / 10)
            if a > 2 * b:
                break

    c = a / b
    d = 1
    e = int(c)

    stem = stem.format(a=a, b=b)
    answer = answer.format(e=e)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e)

    return stem, answer, comment



























# 6-1-3-60
def decimaldiv613_Stem_046():
    stem = "무게가 같은 아령 $$수식$${a}$$/수식$$개의 무게를 재었더니 $$수식$${b}rm g$$/수식$$이었습니다. 아령 $$수식$$1$$/수식$$개의 무게는 몇 $$수식$$rm g$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${c}rm g$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$아령 $$수식$$1$$/수식$$개의 무게$$수식$$RIGHT ) ` = ` LEFT ($$/수식$$아령 $$수식$${a}$$/수식$$개의 무게$$수식$$RIGHT ) ` div ` {a}$$/수식$$\n" \
              "$$수식$$` = ` {b} ` div ` {a} ` = ` {c} ` LEFT ( rm g RIGHT ) `$$/수식$$\n\n"


    while True:
        a = np.random.randint(2, 10)
        d = np.random.randint(10000, 100000)
        tho = d // 10
        if (d % a == 0) & (d % 10 == 0) & (tho % a != 0):
            break

    b = int(d / 10)
    c = b / a

    stem = stem.format(a=a, b=b)
    answer = answer.format(c=c)
    comment = comment.format(a=a, b=b, c=c)

    return stem, answer, comment

























# 6-1-3-61
def decimaldiv613_Stem_047():
    stem = "$$수식$${a}$$/수식$$천 원으로 리본 $$수식$${b} rm m$$/수식$$를 살 수 있습니다. 천 원으로 살 수 있는 리본은 몇 $$수식$$rm m$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${c} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a}$$/수식$$천 원은 천 원의 $$수식$${a}$$/수식$$배이므로\n" \
              "$$수식$$LEFT ($$/수식$$천 원으로 살 수 있는 리본의 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {b} ` div ` {a} ` = ` {c} ` LEFT ( rm m RIGHT ) `$$/수식$$\n\n"


    while True:
        a = np.random.randint(2, 10)
        d = np.random.randint(10, 100)
        tho = d // 10
        if (d % a == 0) & (d % 10 == 0) & (tho % a != 0):
            break

    b = int(d / 10)
    c = b / a

    stem = stem.format(a=a, b=b)
    answer = answer.format(c=c)
    comment = comment.format(a=a, b=b, c=c)

    return stem, answer, comment




























# 6-1-3-62
def decimaldiv613_Stem_048():
    stem = "정육각형의 둘레는 $$수식$${a} rm {{cm}}$$/수식$$입니다. 이 정육각형의 한 변은 몇 $$수식$$rm {{cm}}$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${b} rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "정육각형은 $$수식$$6$$/수식$$개의 변의 길이가 모두 같으므로\n" \
              "$$수식$$LEFT ($$/수식$$한 변의 길이$$수식$$RIGHT ) ` = ` {a} ` div ` 6 ` = ` {b} ` LEFT ( rm {{cm}} RIGHT ) `$$/수식$$\n\n"


    while True:
        c = np.random.randint(100, 1000)
        tho = c // 10
        if (c % 6 == 0) & (c % 10 == 0) & (tho % 6 != 0):
            break

    a = int(c / 10)
    b = a / 6

    stem = stem.format(a=a)
    answer = answer.format(b=b)
    comment = comment.format(a=a, b=b)

    return stem, answer, comment


























# 6-1-3-66
def decimaldiv613_Stem_049():
    stem = "$$수식$${a} ` div ` {b} `$$/수식$$의 몫을 소수로 나타내었을 때 소수 $$수식$${c}$$/수식$$번째 자리 숫자를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${sd}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` = ` 0.{sa}{sb}{sc}{sb}{sc} ……$$/수식$$ {ro1} 소수 둘째 자리부터 숫자 {comment_sentence} 반복됩니다.\n" \
              "따라서 소수 $$수식$${c}$$/수식$$번째 자리 숫자는 $$수식$${sd}$$/수식$$입니다.\n\n"


    while True:
        sa = np.random.randint(0, 10)
        sb = np.random.randint(0, 10)
        sc = np.random.randint(0, 10)
        if (sa != sb) & (sa != sc):
            break

    f = ((100 * sa) + (10 * sb) + sc) - sa
    frac = fractions.Fraction(f, 990)
    a = frac.numerator
    b = frac.denominator

    c = np.random.randint(4, 20)

    if c % 2 == 0:
        sd = sb
    else:
        sd = sc

    ro1 = josa(sc, "로")

    gwa1 = josa(sb, "과")

    ga1 = josa(sc, "가")

    if sb == sc:
        comment_sentence = "%s%s" % (sc, ga1)
    else:
        comment_sentence = "$$수식$$%s$$/수식$$%s $$수식$$%s$$/수식$$%s" % (sb, gwa1, sc, ga1)

    stem = stem.format(a=a, b=b, c=c)
    answer = answer.format(sd=sd)
    comment = comment.format(a=a, b=b, c=c, sa=sa, sb=sb, sc=sc, sd=sd, ro1=ro1, gwa1=gwa1, ga1=ga1, comment_sentence=comment_sentence)

    return stem, answer, comment



























# 6-1-3-67
def decimaldiv613_Stem_050():
    stem = "몫을 어림하여 알맞은 식을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${a} ` div ` {b} ` = ` {c}$$/수식$$    ㉡ $$수식$${a} ` div ` {b} ` = ` {d}$$/수식$$\n㉢ $$수식$${a} ` div ` {b} ` = ` {e}$$/수식$$    ㉣ $$수식$${a} ` div ` {b} ` = ` {f}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{k}\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` div ` {b} ` $$/수식$${rur1} $$수식$${g} ` div ` {b}$$/수식$${ro1} 어림하면 $$수식$${g} ` div ` {b}$$/수식$$의 몫은 $$수식$${h}$$/수식$$보다 크고 $$수식$${i}$$/수식$$보다 작습니다.\n" \
              "따라서 알맞은 식은 {k}입니다.\n\n"


    while True:
        b = np.random.randint(2, 10)
        j = np.random.randint(1000, 10000)
        if (j % b == 0) & (j % 10 != 0):
            break


    a = j / 100
    l = a / b
    c = int(l * 100)

    d = round(l * 10, 1)
    e = round(l, 2)
    f = round(l / 10, 3)

    g = int(a)
    h = int(g / b)
    i = h + 1

    rur1 = josa(b, "를")

    ro1 = josa(b, "로")


    candidates = [c, d, e, f]
    ans = e
    np.random.shuffle(candidates)
    c, d, e, f = candidates


    for j, s in enumerate(candidates):
        if s == ans:
            k = answer_koonedict[j]

    stem = stem.format(a=a, b=b, c=c, d=d, e=e, f=f)
    answer = answer.format(k=k)
    comment = comment.format(a=a, b=b, g=g, h=h, i=i, k=k, rur1=rur1, ro1=ro1)

    return stem, answer, comment




























# 6-1-3-68
def decimaldiv613_Stem_051():
    stem = "$$수식$${a} ` div ` {b} ` $$/수식$${rur1} $$수식$${c} ` div ` {b}$$/수식$${ro1} 어림할 수 있습니다. 올바른 식의 기호를 써 보세요.\n$$표$$㉠ $$수식$${a} ` div ` {b} ` = ` {sd}$$/수식$$\n㉡ $$수식$${a} ` div ` {b} ` = ` {se}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{k}\n"
    comment = "(해설)\n" \
              "$$수식$${c} ` div ` {b} `$$/수식$$의 몫은 $$수식$${f}$$/수식$$보다 크고 $$수식$${g}$$/수식$$보다 작습니다.\n" \
              "따라서 $$수식$${a} ` div ` {b} ` = ` {d}$$/수식$$입니다.\n\n"


    while True:
        b = np.random.randint(2, 10)
        g = np.random.randint(1000, 10000)
        tho = g // 10

        if (g % b == 0) & (g % 10 == 0) & (tho % b != 0):
            a = g / 100
            d = round(a / b, 2)
            e = round(d * 10, 1)
            h = int(a)
            c = h + 1
            j = c / b

            if (c % b != 0):
                break

    f = int(j)
    g = f + 1

    candidates = [d, e]
    ans = d
    np.random.shuffle(candidates)
    sd, se = candidates


    for jdx, sdx in enumerate(candidates):
        if sdx == ans:
            k = answer_koonedict[jdx]

    rur1 = josa(b, "를")

    ro1 = josa(b, "로")

    stem = stem.format(a=a, b=b, c=c, sd=sd, se=se, rur1=rur1, ro1=ro1)
    answer = answer.format(k=k)
    comment = comment.format(a=a, b=b, c=c, d=d, f=f, g=g)

    return stem, answer, comment


























# 6-1-3-69
def decimaldiv613_Stem_052():
    stem = "몫을 어림하여 몫이 $$수식$$1$$/수식$$보다 큰 나눗셈을 모두 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${sa}$$/수식$$    ㉡ $$수식$${sb}$$/수식$$    ㉢ $$수식$${sc}$$/수식$$\n㉣ $$수식$${sd}$$/수식$$    ㉤ $$수식$${se}$$/수식$$    ㉥ $$수식$${sf}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{s}\n"
    comment = "(해설)\n" \
              "나누어지는 수가 나누는 수보다 크면 몫이 $$수식$$1$$/수식$$보다 크고, 나누어지는 수가 나누는 수보다 작으면 몫이 $$수식$$1$$/수식$$보다 작습니다.\n" \
              "따라서 나누어지는 수가 나누는 수보다 큰 나눗셈을 찾으면 {s}입니다.\n\n"


    while True:
        b = np.random.randint(2, 10)
        m = np.random.randint(10, 100)
        if (m % b == 0) & (m % 10 != 0):
            a = m / 10
            if a > b:
                break

    while True:
        d = np.random.randint(2, 10)
        n = np.random.randint(100, 1000)
        if (n % d == 0) & (n % 10 != 0):
            c = n / 100
            if c < d:
                break

    while True:
        f = np.random.randint(2, 10)
        o = np.random.randint(100, 1000)
        if (o % f == 0) & (o % 10 != 0):
            e = o / 100
            if e < f:
                break

    while True:
        h = np.random.randint(2, 10)
        p = np.random.randint(10, 100)
        if (p % h == 0) & (p % 10 != 0):
            g = p / 10
            if g < h:
                break

    while True:
        j = np.random.randint(2, 10)
        q = np.random.randint(100, 1000)
        if (q % j == 0) & (q % 10 != 0):
            i = q / 100
            if i > j:
                break

    while True:
        l = np.random.randint(2, 10)
        r = np.random.randint(100, 1000)
        if (r % l == 0) & (r % 10 != 0):
            k = r / 100
            if k > l:
                break

    sa = "%.1f ` div ` %d" % (a, b)
    sb = "%.2f ` div ` %d" % (c, d)
    sc = "%.2f ` div ` %d" % (e, f)
    sd = "%.1f ` div ` %d" % (g, h)
    se = "%.2f ` div ` %d" % (i, j)
    sf = "%.2f ` div ` %d" % (k, l)

    ans = [sa, se, sf]

    candidates = [sa, sb, sc, sd, se, sf]
    np.random.shuffle(candidates)
    sa, sb, sc, sd, se, sf = candidates

    s = ""

    for j, z in enumerate(candidates):
        if z in ans:
            print(answer_koonedict[j])
            s = s + "%s, " % (answer_koonedict[j])

    s = s[:-2]

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf)
    answer = answer.format(s=s)
    comment = comment.format(s=s)

    return stem, answer, comment


























# 6-1-3-70
def decimaldiv613_Stem_053():
    stem = "몫이 큰 것부터 차례대로 기호를 써 보세요.\n$$표$$㉠ $$수식$${a} ` div ` {e}$$/수식$$    ㉡ $$수식$${b} ` div ` {e}$$/수식$$\n㉢ $$수식$${c} ` div ` {e}$$/수식$$    ㉣ $$수식$${d} ` div ` {e}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{k}\n"
    comment = "(해설)\n" \
              "나눗셈 모두 나누는 수가 $$수식$${e}$$/수식$${ro1} 같으므로 나누어지는 수가 클수록 나눗셈의 몫이 큽니다.\n" \
              "$$수식$${max} ` &gt; ` {one} ` &gt; ` {two} ` &gt; ` {min} `$$/수식$$이므로 몫이 큰 것부터 차례대로 기호를 쓰면 {k}입니다.\n\n"


    while True:
        e = np.random.randint(2, 20)
        j = np.random.randint(100, 1000)
        n = np.random.randint(100, 1000)
        l = np.random.randint(1000, 10000)
        m = np.random.randint(1000, 10000)
        if (j % e == 0) & (n % e == 0) & (l % e == 0) & (m % e == 0):
            if (j % 10 != 0) & (n % 10 != 0) & (l % 10 != 0) & (m % 10 != 0):
                if (j != n) & (l != m):
                    break


    a = j / 10
    b = l / 100
    c = m / 100
    d = n / 10

    maxmin = [a, b, c, d]
    maxmin = sorted(maxmin, reverse=True)
    max, one, two, min = maxmin

    candidates = [a, b, c, d]
    np.random.shuffle(candidates)
    a, b, c, d = candidates

    k = ""

    for z, s in enumerate(maxmin):
        for v, x in enumerate(candidates):
            if x == s:
                k = k + "%s, " % (answer_koonedict[v])

    k = k[:-2]

    ro1 = josa((str(e))[-1], "로")

    stem = stem.format(a=a, b=b, c=c, d=d, e=e)
    answer = answer.format(k=k)
    comment = comment.format(max=max, one=one, two=two, min=min, k=k, e=e, ro1=ro1)

    return stem, answer, comment



























# 6-1-3-72
def decimaldiv613_Stem_054():
    stem = "작은 수를 큰 수로 나누었을 때의 몫을 소수 둘째 자리 미만을 버림하여 나타내어 보세요.\n$$표$$$$수식$${sa}$$/수식$$    $$수식$${sb}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${k}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${min_one} ` &lt; ` {max_one} `$$/수식$$이므로 $$수식$${min_one} ` div ` {max_one} `$$/수식$$를 계산합니다.\n" \
              "$$수식$${min_one} ` div ` {max_one} ` = ` {c}$$/수식$$ …… → $$수식$${k}$$/수식$$\n\n"



    while True:
        a = np.random.randint(2, 10)

        sa = [3, 7, 11, 13, 17][np.random.randint(0, 5)]
        k = np.random.randint(0, 3)
        m = np.random.randint(0, 3)
        n = np.random.randint(0, 3)
        b = pow(2, k) * pow(5, m) * pow(sa, n)

        max_one = max(a, b)
        min_one = min(a, b)

        maxa = max_one
        mina = min_one

        while True:
            rest_ab = maxa % mina
            mina = min(maxa, mina)
            maxa = rest_ab
            if rest_ab == 0 or rest_ab == 1:
                break

        c = min_one / max_one

        if (a % b != 0) and (b % a != 0) and rest_ab == 1 and len(str(c)) > 4 and (c*100) > 1:
            break


    # c = (a / b)
    # print(c)
    k = math.floor(c * 100) / 100
    # print(k)

    candidates = [a, b]
    np.random.shuffle(candidates)
    sa, sb = candidates

    stem = stem.format(sa=sa, sb=sb)
    answer = answer.format(k=k)
    comment = comment.format(c=c, k=k, max_one=max_one, min_one=min_one)

    return stem, answer, comment



























# 6-1-3-73
def decimaldiv613_Stem_055():
    stem = "나눗셈을 보고 바르게 말한 사람은 누구인가요?\n$$표$$$$수식$${sa} ` div ` {d}$$/수식$$    $$수식$${sb} ` div ` {d}$$/수식$$    $$수식$${sc} ` div ` {d}$$/수식$$$$/표$$\n$$표$${x1}\n{x2}\n{x3}$$/표$$\n"
    answer = "(정답)\n{t2}\n"
    comment = "(해설)\n" \
              "{y1}" \
              "{y2}" \
              "{y3}" \
              "따라서 바르게 말한 사람은 {t2}입니다.\n\n"



    while True:
        t1 = ["미주", "은수", "연아", "수찬", "경배", "태규", "승혁", "선우"][np.random.randint(0, 8)]
        t2 = ["미주", "은수", "연아", "수찬", "경배", "태규", "승혁", "선우"][np.random.randint(0, 8)]
        t3 = ["미주", "은수", "연아", "수찬", "경배", "태규", "승혁", "선우"][np.random.randint(0, 8)]
        if t1 != t2 and t1 != t3 and t2 != t3:
            break


    # while True:
    #     # d = np.random.randint(2, 20)
    #     d = [11, 13, 17, 19][np.random.randint(0, 4)]
    #     e = np.random.randint(100, 1000)
    #     if (e % d == 0) & (e % 10 != 0):
    #         a = e / 10
    #         if (a > d):
    #             f = np.random.randint(1000, 10000)
    #             if (f % d == 0) & (f % 10 != 0):
    #                 b = f / 100
    #                 if (b < d):
    #                     g = np.random.randint(1000, 10000)
    #                     if (g % d == 0) & (g % 10 != 0):
    #                         c = g / 100
    #                         if b < c and c < d:
    #                             break

    # 위 코드는 계산 속도가 너무 느림

    while True:
        d = [11, 13, 17, 19][np.random.randint(0, 4)]

        e_factor = np.random.randint(9, 91)
        e = e_factor * d

        f_factor = np.random.randint(90, 910)
        f = f_factor * d

        g_factor = np.random.randint(90, 910)
        g = g_factor * d

        a = e/10
        b = f/100
        c = g/100

        if 100 <= e and e < 1000 and 1000 <= f and f < 10000 and 1000 <= g and g < 10000 and e % 10 != 0 and f % 10 != 0 and g % 10 != 0 and f < g and a > d and b < c and c < d:
            break


    max_one = max(a, b, c)

    min_one = min(a, b, c)

    middle_list = [a, b, c]
    middle_list.sort()

    wrong_ch = [middle_list[1], max_one][np.random.randint(0, 2)]

    candidates = [a, b, c]
    np.random.shuffle(candidates)
    sa, sb, sc = candidates

    yiya1 = josa((str(d))[-1], "이야")

    ro1 = josa((str(d))[-1], "로")


    saying1 = f"$$수식$$LEFT [$$/수식$${t1}$$수식$$RIGHT ]$$/수식$$ 몫이 가장 작은 나눗셈은 $$수식$${wrong_ch} ` div ` {d}$$/수식$${yiya1}."
    saying2 = f"$$수식$$LEFT [$$/수식$${t2}$$수식$$RIGHT ]$$/수식$$ 몫이 $$수식$$1$$/수식$$보다 큰 나눗셈은 $$수식$${max_one} ` div ` {d}$$/수식$$뿐이야."
    saying3 = f"$$수식$$LEFT [$$/수식$${t3}$$수식$$RIGHT ]$$/수식$$ 어림으로는 나눗셈의 몫이 $$수식$$1$$/수식$$보다 큰지 작은지 알 수 없어."

    temp_list1 = [saying1, saying2, saying3]
    np.random.shuffle(temp_list1)
    x1, x2, x3 = temp_list1

    word1 = f"$$수식$$LEFT [$$/수식$${t1}$$수식$$RIGHT ]$$/수식$$ 세 나눗셈 모두 나누는 수가 $$수식$${d}$$/수식$${ro1} 모두 같으므로 나누어지는 수가 가장 작은 나눗셈의 몫이 가장 작습니다.\n→ 몫이 가장 작은 나눗셈은 $$수식$${min_one} ` div ` {d}$$/수식$$입니다.\n"
    word2 = f"$$수식$$LEFT [$$/수식$${t2}$$수식$$RIGHT ]$$/수식$$ 나누어지는 수가 나누는 수보다 크면 몫은 $$수식$$1$$/수식$$보다 큽니다.\n→ 몫이 $$수식$$1$$/수식$$보다 큰 나눗셈은 $$수식$${max_one} ` div ` {d}$$/수식$$입니다.\n"
    word3 = f"$$수식$$LEFT [$$/수식$${t3}$$수식$$RIGHT ]$$/수식$$ 나누어지는 수와 나누는 수의 크기를 비교하면 몫이 $$수식$$1$$/수식$$보다 큰지 작은지 알 수 있습니다.\n→ 어림으로 나눗셈의 몫이 $$수식$$1$$/수식$$보다 큰지 작은지 알 수 있습니다.\n"

    temp_list2 = []

    for idx in temp_list1:
        if idx == saying1:
            temp_list2.append(word1)
        elif idx == saying2:
            temp_list2.append(word2)
        elif idx == saying3:
            temp_list2.append(word3)

    y1, y2, y3 = temp_list2


    stem = stem.format(sa=sa, sb=sb, sc=sc, d=d, x1=x1, x2=x2, x3=x3)
    answer = answer.format(t2=t2)
    comment = comment.format(t2=t2, y1=y1, y2=y2, y3=y3)

    return stem, answer, comment







