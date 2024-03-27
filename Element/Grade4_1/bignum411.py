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



# 4-1-1-02
def bignum411_Stem_001():
    stem = "그림을 보고 □ 안에 알맞은 수를 써넣으세요\n$$수식$${boxone}$$/수식$$→$$수식$${boxpointer}$$/수식$$→$$수식$${boxtwo}$$/수식$$→$$수식$${boxpointer}$$/수식$$→$$수식$${boxthree}$$/수식$$→$$수식$${boxpointer}$$/수식$$→$$수식$${boxhun}$$/수식$$\n$$수식$$LEFT ( 1 RIGHT )  {e}$$/수식$$ 보다 $$수식$${boxfour}$$/수식$$ 큰 수는 $$수식$$10000$$/수식$$ 입니다.\n$$수식$$LEFT ( 2 RIGHT )  {f}$$/수식$$ 은 $$수식$$10000$$/수식$$ 보다 $$수식$${boxfive}$$/수식$$ 작은 수 입니다.\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n"\
              "$$수식$$LEFT ( 1 RIGHT )  {e}$$/수식$$ 에서 $$수식$${a}$$/수식$$씩 $$수식$${g}$$/수식$$번 커지면 $$수식$$10000$$/수식$$ 입니다.\n" \
              "$$수식$$LEFT ( 2 RIGHT )  10000$$/수식$$ 에서 $$수식$${h}$$/수식$$ 작아지면 $$수식$${f}$$/수식$$ 입니다.\n\n"


    aa = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    a = random.choice(aa)
    b = 10000 - (3*a)
    c = 10000 - (2*a)
    d = 10000 - a

    bcd = [b, c, d]
    ef = random.sample(bcd, 2)
    e = ef[0]
    f = ef[1]

    g = int((10000 - e)/a)
    h = 10000 - f
    a1 = 10000 - e
    a2 = 10000 - f




    boxone = "%d" % b
    boxtwo = "%d" % c
    boxthree = "%d" % d

    boxfour = "box{　　　}"
    boxfive = "box{　　　}"

    boxpointer= "(%d)" % a
    boxhun = "10000"

    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour, boxfive=boxfive,
                       boxpointer=boxpointer, e=e, f=f, boxhun=boxhun)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(e=e, a=a, g=g, h=h, f=f)

    return stem, answer, comment









# 4-1-1-04
def bignum411_Stem_002():
    stem = "$$수식$$10000$$/수식$$이 $$수식$${k}$$/수식$$개인 수를 쓰고 읽어 보세요.\n$$수식$${boxone}$$/수식$$\n$$수식$${boxtwo}$$/수식$$\n"
    answer = "(정답)\n$$수식$${kk}$$/수식$$ 또는 $$수식$${k}$$/수식$$만, {m}만\n"
    comment = "(해설)\n"\
              "$$수식$$10000$$/수식$$이 $$수식$${k}$$/수식$$개인 수는 $$수식$${kk}$$/수식$$ 또는 " \
              "$$수식$${k}$$/수식$$만이라 쓰고, {m}만이라고 읽습니다.\n\n"


    k = np.random.randint(2, 10)
    kk = 10000 * k

    mm = {2:"이", 3:"삼", 4:"사", 5:"오", 6:"육", 7:"칠", 8:"팔", 9:"구"}
    m = mm[k]

    boxone = "box{(쓰기)``````````````````````````````}"
    boxtwo = "box{(읽기)``````````````````````````````}"

    stem = stem.format(boxone=boxone, boxtwo=boxtwo, k=k)
    answer = answer.format(k=k, m=m, kk=kk)
    comment = comment.format(k=k, m=m, kk=kk)

    return stem, answer, comment









# 4-1-1-05
def bignum411_Stem_003():
    stem = "{a}는 $$수식$$10000$$/수식$$원짜리 {b}를 사려고 합니다. {a}의 지갑에 $$수식$$1000$$/수식$$원짜리 지폐가 $$수식$${c}$$/수식$$장 있다면 얼마가 더 있어야 {b}를 살 수 있나요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$원 또는 {a2}원 또는 {a3}원\n"
    comment = "(해설)\n"\
              "$$수식$$1000$$/수식$$원짜리 지폐 $$수식$${c}$$/수식$$장은 $$수식$${d}$$/수식$$원입니다.\n"\
              "$$수식$$10000$$/수식$$원은 $$수식$${d}$$/수식$$보다 $$수식$${e}$$/수식$$ 더 큰 수 이므로\n"\
              "$$수식$${e}$$/수식$$원이 더 있어야 $$수식$$10000$$/수식$$원짜리 {b}를 살 수 있습니다.\n\n"


    aa = ["희진이", "수경이", "미진이", "가영이", "하율이"]
    a = random.choice(aa)

    bb = ["모자", "목걸이", "귀걸이", "반지"]
    b = random.choice(bb)

    c = np.random.randint(1, 10)
    d = c*1000
    e = 10000-d
    ee = int(e/1000)

    ss = {1:"일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}
    s = ss[ee]

    if (ee==1):
        a3 = "일천 또는 천"
    else:
        a3 = "%s천" % s

    a1 = e
    a2 = "$$수식$$%d$$/수식$$천" %ee

    stem = stem.format(a=a, b=b, c=c)
    answer = answer.format(a1=a1, a2=a2, a3=a3)
    comment = comment.format(c=c, d=d, e=e, b=b)

    return stem, answer, comment









# 4-1-1-06
def bignum411_Stem_004():
    stem = "$$수식$$10000$$/수식$$원이 되려면 다음 돈이 얼마만큼 있어야 하나요?\n$$수식$${a}$$/수식$$원 $$수식$$LEFT ( RIGHT )$$/수식$$개 → $$수식$$10000$$/수식$$원\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$ 또는 {a2}\n"
    comment = "(해설)\n"\
              "$$수식$${a}$$/수식$$원이 $$수식$${b}$$/수식$$개이면 $$수식$$1000$$/수식$$원이고 "\
              "$$수식$$1000$$/수식$$원이 $$수식$$10$$/수식$$개이면 $$수식$$10000$$/수식$$원이므로 $$수식$${a}$$/수식$$원이 " \
              "$$수식$${c}$$/수식$$개 있어야 $$수식$$10000$$/수식$$원입니다.\n\n"


    aa = [10, 50, 100, 500]
    a = random.choice(aa)
    b = int(1000/a)

    cc = {1000:"천", 200: "이백", 100: "백", 20: "이십"}
    c = b*10
    a1 = c
    a2 = cc[c]

    stem = stem.format(a=a)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(a=a, b=b, c=c)

    return stem, answer, comment








# 4-1-1-07
def bignum411_Stem_005():
    stem = "{a}는 {b} 참가비로 $$수식$$10000$$/수식$$원짜리 지폐 $$수식$${c}$$/수식$$장과 $$수식$$1000$$/수식$$원짜리 지폐 $$수식$${d}$$/수식$$장을 냈습니다. {b} 참가비는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$원 또는 {a2}원 또는 {a3}원\n"
    comment = "(해설)\n"\
              "$$수식$$10000$$/수식$$원짜리 지폐 $$수식$${c}$$/수식$$장은 $$수식$${e}$$/수식$$원입니다.\n"\
              "$$수식$$1000$$/수식$$원짜리 지폐 $$수식$${d}$$/수식$$장은 $$수식$${f}$$/수식$$원입니다.\n"\
              "따라서 {b} 참가비는\n"\
              "$$수식$${e} `+ {f} ` = ` {g} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    aa = ["수지", "영미", "미나", "희주", "가희", "윤아", "혜미"]
    a = random.choice(aa)

    bb = ["수학 캠프", "영어 캠프", "수련회", "수학 여행"]
    b = random.choice(bb)

    while True:
        c = np.random.randint(1, 10)
        d = (np.random.randint(1, 10)) * 10
        if (c + (d/10) < 10):
            break

    e = c * 10000
    f = d * 1000

    g = e + f
    a1 = g
    a22 = int(a1 / 10000)

    a2 = "$$수식$$%d$$/수식$$만" % a22
    a33 = {1: "일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}
    a3 =  "%s만" % (a33[a22])

    stem = stem.format(a=a, b=b, c=c, d=d)
    answer = answer.format(a1=a1, a2=a2, a3=a3)
    comment = comment.format(b=b, c=c, d=d, e=e, f=f, g=g)

    return stem, answer, comment







# 4-1-1-08
def bignum411_Stem_006():
    stem = "{a}는 $$수식$$1000$$/수식$$원짜리 지폐 $$수식$${b}$$/수식$$장과 $$수식$$100$$/수식$$원 짜리 동전 $$수식$${c}$$/수식$$개를 모았습니다. {a}가 모은 돈은 모두 얼마인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$원 또는 {a2}원 또는 {a3}원\n"
    comment = "(해설)\n"\
              "$$수식$$1000$$/수식$$원짜리 지폐 $$수식$${b}$$/수식$$장은 $$수식$${d}$$/수식$$원이고, "\
              "$$수식$$100$$/수식$$원짜리 동전 $$수식$${c}$$/수식$$개는 $$수식$${e}$$/수식$$원입니다.\n"\
              "따라서 {a}가 모은 돈은 모두\n"\
              "$$수식$${d} ` + ` {e} ` = ` {f} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    aa = ["민수", "재희", "준하", "준수", "선우", "홍기", "수호"]
    a = random.choice(aa)

    while True:
        b = np.random.randint(1, 20)
        cc = np.random.randint(0, 90)

        c = cc * 10
        bc = 10*b + c

        if (bc % 100 == 0) and (bc >= 100) and (bc <= 900):
            break

    d = 1000 * b
    e = 100 * c
    f = d + e

    a1 = f
    ff = int(f/10000)
    a2 = "$$수식$$%d$$/수식$$만" % ff

    a33 = {2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}

    if (ff==1):
        a3 = "일만 또는 만"
    else:
        a3 = "%s만" % (a33[ff])

    stem = stem.format(a=a, b=b, c=c)
    answer = answer.format(a1=a1, a2=a2, a3=a3)
    comment = comment.format(b=b, d=d, c=c, e=e, a=a, f=f)

    return stem, answer, comment







# 4-1-1-09
def bignum411_Stem_007():
    stem = "㉠에 알맞은 수를 구해 보세요.\n$$수식$$10000$$/수식$$ 이 $$수식$${a}$$/수식$$개\n{y1}{y2}{y3}{y4}\n 이면 $$수식$${box}$$/수식$$\n"
    answer = "(정답)\n$$수식$${f}$$/수식$$\n"
    comment = "(해설)\n"\
              "$$수식$${full} = {f}$$/수식$$\n\n"

    
    box = "box{㉠``````````````````````````````}"
    a = np.random.randint(1, 10)
    aa = 10000 * a

    while True:
        b = np.random.randint(0, 10)
        c = np.random.randint(0, 10)
        d = np.random.randint(0, 10)
        e = np.random.randint(0, 10)

        temp_list = [b, c, d, e]
        if temp_list.count(0) <= 2:
            break

    f = aa + 1000 * b + 100 * c + 10 * d + e

    if (b==0):
        y1 = ""
        bb = ""
        bbb= ""
    else:
        y1 = "$$수식$$%d$$/수식$$ 이 $$수식$$%d$$/수식$$개\n" % (1000, b)
        bb = 1000 * b
        bbb= " ` + `%d" %(bb)

    if (c==0):
        y2 = ""
        cc = ""
        ccc = ""
    else:
        y2 = "$$수식$$%d$$/수식$$ 이 $$수식$$%d$$/수식$$개\n" % (100,c)
        cc = 100 * c
        ccc = " ` + ` %d" % (cc)

    if (d==0):
        y3 = ""
        dd = ""
        ddd = ""
    else:
        y3 = "$$수식$$%d$$/수식$$ 이 $$수식$$%d$$/수식$$개\n" % (10,d)
        dd = 10 * d
        ddd = " ` + ` %d" % (dd)

    if (e==0):
        y4 = ""
        e = " "
        eee = ""
    else:
        y4 = "$$수식$$%d$$/수식$$ 이 $$수식$$%d$$/수식$$개" % (1,e)
        eee = " ` + ` %d" % (e)

    full = ""
    result_list = [aa, bbb, ccc, ddd, eee]
    for idx in result_list :
        if idx :
            full += str(idx)

    stem = stem.format(y1=y1, y2=y2, y3=y3, y4=y4, a=a, box=box)
    answer = answer.format(f=f)
    comment = comment.format(full=full, f=f)

    return stem, answer, comment







# 4-1-1-10
def bignum411_Stem_008():
    stem = "수를 읽어 보세요\n$$수식$${boxone}$$/수식$$\n"
    answer = "(정답)\n{a}{b}{c}{d}{e}{a2}\n"
    comment = "(해설)\n"\
              "일의 자리는 수만 읽고 '일'은 읽지 않습니다. 그리고 자리 수의 값이 $$수식$$1$$/수식$$인 경우 "\
              "$$수식$$1$$/수식$$은 읽지 않습니다.\n"\
              "$$수식$${aa}{bb}{cc}{dd}{ee}$$/수식$$ → {a}{b}{c}{d}{e}{a2}\n\n"


    aa = np.random.randint(1, 10)
    bb = np.random.randint(0, 10)
    cc = np.random.randint(0, 10)

    dd = np.random.randint(0, 10)
    ee = np.random.randint(0, 10)

    number = {1:"일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}
    a = "%s만" % (number[aa])

    if(bb == 0):
        b=""
    elif(bb == 1):
        b = "천"
    else:
        b = "%s천" %(number[bb])

    if (cc == 0):
        c = ""
    elif(cc == 1):
        c = "백"
    else:
        c = "%s백" % (number[cc])

    if (dd == 0):
        d = ""
    elif(dd == 1):
        d = "십"
    else:
        d = "%s십" % (number[dd])

    if (ee == 0):
        e = ""
    else:
        e = "%s" % (number[ee])

    if(aa == 1):
        a2 = ", 만%s%s%s%s" %(b,c,d,e)
    else:
        a2 = ""

    boxone = "%d%d%d%d%d" % (aa,bb,cc,dd,ee)

    stem = stem.format(boxone=boxone)
    answer = answer.format(a=a, b=b, c=c, d=d, e=e, a2=a2)
    comment = comment.format(aa=aa, bb=bb, cc=cc, dd=dd, ee=ee, a=a, b=b, c=c, d=d, e=e, a2=a2)

    return stem, answer, comment








# 4-1-1-11
def bignum411_Stem_009():
    stem = "수로 써 보세요.\n$$수식$${boxone}$$/수식$$\n"
    answer = "(정답)\n$$수식$${ff}{gg}{hh}{ii}{jj} $$/수식$$\n"
    comment = "(해설)\n"\
              "{a}{b}{c}{d}{e} → "\
              "{aa}{bb}{cc}{dd}$$수식$${e1}$$/수식$$ → "\
              "$$수식$$```{ff}{gg}{hh}{ii}{jj}$$/수식$$\n\n"


    a1 = np.random.randint(1, 10)
    b1 = np.random.randint(0, 10)
    c1 = np.random.randint(0, 10)

    d1 = np.random.randint(0, 10)
    e1 = np.random.randint(0, 10)

    number = {1:"일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}

    a = "%s만" % (number[a1])

    if (b1==0):
        b=""
    elif (b1==1):
        b = "천"
    else:
        b = "%s천" %(number[b1])

    if (c1 == 0):
        c = ""
    elif(c1 == 1):
        c = "백"
    else:
        c = "%s백" % (number[c1])

    if (d1 == 0):
        d = ""
    elif(d1 ==1):
        d = "십"
    else:
        d = "%s십" % (number[d1])

    if (e1 == 0):
        e = ""
    else:
        e = "%s" % (number[e1])

    aa = "$$수식$$%d$$/수식$$만" % a1
    bb = "$$수식$$%d$$/수식$$천" % b1

    cc = "$$수식$$%d$$/수식$$백" % c1
    dd = "$$수식$$%d$$/수식$$십" % d1

    ff = a1
    gg = b1
    hh = c1

    ii = d1
    jj = e1

    boxone = "%s%s%s%s%s" % (a, b, c, d, e)

    stem = stem.format(boxone=boxone)
    answer = answer.format(ff=ff, gg=gg, hh=hh, ii=ii, jj=jj)
    comment = comment.format(aa=aa, bb=bb, cc=cc, dd=dd, e1=e1, a=a, b=b, c=c, d=d, e=e, ff=ff, gg=gg, hh=hh, ii=ii, jj=jj)

    return stem, answer, comment






# 4-1-1-13
def bignum411_Stem_010():
    stem = "다음을 수로 쓰고 읽어 보세요.\n$$표$$ $$수식$$10000$$/수식$$ 이 $$수식$${aa}$$/수식$$개, {y1}{y2}{y3}{y4}인 수$$/표$$\n$$수식$${boxtwo}$$/수식$$\n$$수식$${boxthree}$$/수식$$\n"
    answer = "(정답)\n$$수식$${aa}{bb}{cc}{dd}{ee}$$/수식$$, {a}{b}{c}{d}{e}{a2}\n"
    comment = "(해설)\n"\
              "$$수식$$10000$$/수식$$ 이 $$수식$${aa}$$/수식$$개,{y1}{y2}{y3}{y4}인 수를 "\
              "$$수식$${aa}{bb}{cc}{dd}{ee}$$/수식$${rago} 쓰고, " \
              "{a}{b}{c}{d}{e}{a2} {rago} 읽습니다.\n\n"


    aa = np.random.randint(1, 10)
    bb = np.random.randint(0, 10)
    cc = np.random.randint(0, 10)

    while True:
        dd = np.random.randint(0, 10)
        ee = np.random.randint(0, 10)
        if dd == 0 and ee == 0:
            continue
        else:
            break

    number = {1: "일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}

    if (bb == 0):
        y1 = ""
        b = ""
    elif(bb == 1):
        y1 = " $$수식$$%d$$/수식$$ 이 $$수식$$%d$$/수식$$개," % (1000, bb)
        b = "천"
    else:
        b = "%s천" % (number[bb])
        y1 = " $$수식$$%d$$/수식$$ 이 $$수식$$%d$$/수식$$개," % (1000, bb)

    if (cc == 0):
        y2 = ""
        c = ""
    elif(cc == 1):
        y2 = " $$수식$$%d$$/수식$$ 이 $$수식$$%d$$/수식$$개," % (100, cc)
        c = "백"
    else:
        y2 = " $$수식$$%d$$/수식$$ 이 $$수식$$%d$$/수식$$개," % (100, cc)
        c = "%s백" % (number[cc])

    if (dd == 0):
        y3 = ""
        d = ""
    elif (ee == 0):
        if (dd == 1):
            y3 = " $$수식$$%d$$/수식$$ 이 $$수식$$%d$$/수식$$개" % (10, dd)
            d = "십"
        else:
            y3 = " $$수식$$%d$$/수식$$ 이 $$수식$$%d$$/수식$$개" % (10, dd)
            d = "%s십" % (number[dd])
    else:
        if(dd == 1):
            y3 = " $$수식$$%d$$/수식$$ 이 $$수식$$%d$$/수식$$개," % (10, dd)
            d = "십"
        else:
            y3 = " $$수식$$%d$$/수식$$ 이 $$수식$$%d$$/수식$$개," % (10, dd)
            d = "%s십" % (number[dd])

    if (ee == 0):
        y4 = ""
        e = ""
    else:
        y4 = " $$수식$$%d$$/수식$$ 이 $$수식$$%d$$/수식$$개" % (1, ee)
        e = "%s" % (number[ee])

    number = {1:"일",2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}

    a = "%s만" % (number[aa])

    if (aa == 1):
        a2 = ", 또는 만%s%s%s%s"   % (b, c, d, e)
    else:
        a2 = ""

    if ee == 0 or ee == 1 or ee == 3 or ee == 6 or ee == 7 or ee == 8:
        rago = "이라고"
    else:
        rago = "라고"

    boxtwo = "box{(쓰기)``````````````````````````````}"
    boxthree = "box{(읽기)``````````````````````````````}"

    stem = stem.format(aa=aa, y1=y1, y2=y2, y3=y3, y4=y4, boxtwo=boxtwo, boxthree=boxthree)
    answer = answer.format(aa=aa, bb=bb, cc=cc, dd=dd, ee=ee, a=a, b=b, c=c, d=d, e=e, a2=a2)
    comment = comment.format(aa=aa, bb=bb, cc=cc, dd=dd, ee=ee, a=a, b=b, c=c, d=d, e=e, a2=a2, y1=y1, y2=y2, y3=y3, y4=y4, rago=rago)

    return stem, answer, comment









# 4-1-1-15
def bignum411_Stem_011():
    stem = "보기와 같이 각 자리의 숫자가 나타내는 값의 합으로 나타내어 보세요.\n$$표$$ $$수식$${boxone}$$/수식$$ $$/표$$\n$$수식$${aa}{bb}{cc}{dd}{ee} ` = `$$/수식$$$$수식$${boxtwo}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a}{b}{c}{d}{e}$$/수식$$\n"
    comment = "(해설)\n"\
              "각 자리의 숫자가 나타내는 값의 합으로 나타냅니다.\n\n"


    xaa = np.random.randint(1, 10)
    xbb = np.random.randint(1, 10)
    xcc = np.random.randint(1, 10)

    xdd = np.random.randint(1, 10)
    xee = np.random.randint(1, 10)

    xa = "%d0000" % (xaa)

    if (xbb == 0):
        xb = ""
    else:
       xb = " + ``%d000" % (xbb)

    if (xcc == 0):
        xc = ""
    else:
        xc = " + ``%d00" % (xcc)

    if (xdd == 0):
        xd = ""
    else:
        xd = " + `` %d0" % (xdd)

    if (xee == 0):
        xe = ""
    else:
        xe = " + `` %d" % (xee)


    aa = np.random.randint(1, 10)
    while True:
        bb = np.random.randint(0, 10)
        cc = np.random.randint(0, 10)

        dd = np.random.randint(0, 10)
        ee = np.random.randint(0, 10)
        temp_list = [bb, cc, dd, ee]

        if temp_list.count(0) < 4:
            break

    a = "%d0000" % (aa)
    if (bb == 0):
        b = ""
    else:
        b = " + %d000" % (bb)

    if (cc == 0):
        c = ""
    else:
        c = " + %d00" % (cc)

    if (dd == 0):
        d = ""
    else:
        d = " + %d0 " % (dd)

    if (ee == 0):
        e = ""
    else:
        e = " + %d" % (ee)


    boxone = "%d%d%d%d%d = %s%s%s%s%s" % (xaa, xbb, xcc, xdd, xee, xa, xb, xc, xd, xe)
    boxtwo = "(답) : "

    stem = stem.format(aa=aa, bb=bb, cc=cc, dd=dd, ee=ee, boxone=boxone, boxtwo=boxtwo)
    answer = answer.format(a=a, b=b, c=c, d=d, e=e)

    return stem, answer, comment







# 4-1-1-16
def bignum411_Stem_012():
    stem = "다음 중 만의 자리 숫자가 $$수식$${aa}$$/수식$$인 수는 어느 것인가요?\n① $$수식$${lb}$$/수식$$\n② $$수식$${lc}$$/수식$$\n③ $$수식$${ld}$$/수식$$\n④ $$수식$${le}$$/수식$$\n⑤ $$수식$${lf}$$/수식$$\n"
    answer = "(정답)\n{a}\n"
    comment = "(해설)\n"\
              "각 수의 만의 자리 숫자를 알아보면 \n" \
              "① {a1}\n" \
              "② {a2}\n" \
              "③ {a3}\n" \
              "④ {a4}\n" \
              "⑤ {a5}\n" \
              "따라서 만의 자리 숫자가 $$수식$${aa} $$/수식$$인 수는 $$수식$${bb} `` $$/수식$$입니다.\n\n"


    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers = random.sample(number, 5)

    aa = numbers[0]
    c = numbers[1]
    d = numbers[2]
    e = numbers[3]
    f = numbers[4]

    while True:
        b1 = np.random.randint(0, 10000)
        b1_list = list(str(b1))
        if b1_list.count(str(aa)) == 0:
            break

    while True:
        c1 = np.random.randint(1000, 10000)
        c1_list = list(str(c1))
        if c1_list.count(str(aa)) == 1 and (str(c1))[-4] == str(aa):
            break
    #
    while True:
        d1 = np.random.randint(100, 10000)
        d1_list = list(str(d1))
        if d1_list.count(str(aa)) == 1 and (str(d1))[-3] == str(aa):
            break

    while True:
        e1 = np.random.randint(10, 10000)
        e1_list = list(str(e1))
        if e1_list.count(str(aa)) == 1 and (str(e1))[-2] == str(aa):
            break

    while True:
        f1 = np.random.randint(0, 10000)
        f1_list = list(str(f1))
        if f1_list.count(str(aa)) == 1 and (str(f1))[-1] == str(aa):
            break

    bb = aa * 10000 + b1
    cc = c * 10000 + c1
    dd = d * 10000 + d1
    ee = e * 10000 + e1
    ff = f * 10000 + f1

    candidates = [bb, cc, dd, ee, ff]
    np.random.shuffle(candidates)
    lb, lc, ld, le, lf = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == bb:
            correct_idx = i
            break

    a1 = " $$수식$$%d$$/수식$$ → $$수식$$%d$$/수식$$ " % (lb, int(lb/10000))
    a2 = " $$수식$$%d$$/수식$$ → $$수식$$%d$$/수식$$ " % (lc, int(lc/10000))
    a3 = " $$수식$$%d$$/수식$$ → $$수식$$%d$$/수식$$ " % (ld, int(ld/10000))

    a4 = " $$수식$$%d$$/수식$$ → $$수식$$%d$$/수식$$ " % (le, int(le/10000))
    a5 = " $$수식$$%d$$/수식$$ → $$수식$$%d$$/수식$$ " % (lf, int(lf/10000))

    stem = stem.format(aa=aa, lb=lb, lc=lc, ld=ld, le=le, lf=lf)
    answer = answer.format(a=answer_dict[correct_idx])
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, aa=aa, bb=bb)

    return stem, answer, comment






# 4-1-1-17
def bignum411_Stem_013():
    stem = "수를 읽어 보세요.\n$$수식$${boxone}$$/수식$$ $$수식$${boxtwo}$$/수식$$\n"
    answer = "(정답)\n{a}{b}{c}{d}{e}{a2}\n"
    comment = "(해설)\n"\
              "일의 자리는 숫자만 읽어야 합니다.\n"\
              "따라서 바르게 읽으면 {a}{b}{c}{d}{e}{a2} 입니다.\n\n"


    aa = np.random.randint(1, 10)
    bb = np.random.randint(0, 10)
    cc = np.random.randint(0, 10)

    dd = np.random.randint(0, 10)
    ee = np.random.randint(0, 10)

    number = {1:"일",2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}

    if (bb == 0):
        b = ""
    elif (bb == 1):
        b = "천"
    else:
        b = "%s천" % (number[bb])

    if (cc == 0):
        c = ""
    elif (cc == 1):
        c = "백"
    else:
        c = "%s백" % (number[cc])

    if (dd == 0):
        d = ""
    elif (dd == 1):
        d = "십"
    else:
        d = "%s십" % (number[dd])

    if (ee == 0):
        e = ""
    else:
        e = "%s" % (number[ee])

    if (aa == 1):
        a2 = " 또는 만%s%s%s%s" % (b, c, d, e)
        a = "%s만" % (number[aa])
    else:
        a2 = ""
        a = "%s만" % (number[aa])


    boxone = "%d%d%d%d%d" %(aa,bb,cc,dd,ee)
    boxtwo = "box{　　　````````````````````}"

    stem = stem.format(boxone=boxone, boxtwo=boxtwo)
    answer = answer.format(a=a, b=b, c=c, d=d, e=e, a2=a2)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, a2=a2)

    return stem, answer, comment







# 4-1-1-19
def bignum411_Stem_014():
    stem = "$$수식$$1000$$/수식$$원짜리 지폐 $$수식$${m}$$/수식$$장, $$수식$$100$$/수식$$원짜리 동전 $$수식$${n}$$/수식$$개가 있습니다. 모두 얼마인가요?\n"
    answer = "(정답)\n$$수식$${ss}$$/수식$$원\n"
    comment = "(해설)\n"\
              "$$수식$$1000 `` $$/수식$$원 짜리 지폐 $$수식$${m}$$/수식$$장은 $$수식$${aa}$$/수식$$원이고, "\
              "$$수식$$100 `` $$/수식$$원 짜리 동전 $$수식$${n} `` $$/수식$$개는 $$수식$${bb}$$/수식$$원입니다.\n"\
              "따라서 돈은 모두 $$수식$${aa} ` + ` {bb} ` = ` {ss} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    while True:
        m = np.random.randint(1, 100)
        n = np.random.randint(1, 1000)

        if ((10*m + n) > 100) and ((10*m + n) < 1000):
            break

    aa = 1000 * m
    bb = 100 * n
    ss = aa + bb

    stem = stem.format(m=m, n=n)
    answer = answer.format(ss=ss)
    comment = comment.format(m=m, n=n, aa=aa, bb=bb, ss=ss)

    return stem, answer, comment







# 4-1-1-20
def bignum411_Stem_015():
    stem = "다음 수 중 숫자 $$수식$${kk}$$/수식$${j1} 나타내는 값은 얼마인가요?\n$$수식$${boxone}$$/수식$$\n"
    answer = "(정답)\n$$수식$${ff}$$/수식$$\n"
    comment = "(해설)\n"\
              "$$수식$${aa}{bb}{cc}{dd}{ee}$$/수식$$에서 $$수식$${kk}$$/수식$${j2} "\
              "{tt}의 자리 숫자이므로 $$수식$${ff}$$/수식$$을 나타냅니다.\n\n"


    while True:
        aa = np.random.randint(1, 10)
        number = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
        num = random.sample(number, 4)
        bb = num[0]
        cc = num[1]
        dd = num[2]
        ee = num[3]
        if ((aa != bb) and (aa != cc) and (aa != dd) and (aa != ee)):
            break

    k = [aa, bb, cc, dd, ee]
    kk = random.choice(k)
    ktf = [[ee, '일', 1], [dd, '십', 10], [cc, '백', 100], [bb, '천', 1000], [aa, '만', 10000]]

    tt = ""
    f = ""

    for i in range(0, 5):
      if (ktf[i][0] == kk):
        tt = ktf[i][1]
        f = ktf[i][2]
        break

    ff = kk * f

    if(kk==2 or kk==4 or kk==5 or kk==9):
        j1 = "가"
        j2=  "는"
    else:
        j1 = "이"
        j2 = "은"

    boxone = "%d%d%d%d%d" % (aa, bb, cc, dd, ee)

    stem = stem.format(boxone=boxone, kk=kk, j1=j1)
    answer = answer.format(kk=kk, ff=ff)
    comment = comment.format(aa=aa, bb=bb, cc=cc, dd=dd, ee=ee, kk=kk, tt=tt, ff=ff, j2=j2)

    return stem, answer, comment







# 4-1-1-21
def bignum411_Stem_016():
    stem = "{tt}가 집안일을 하고 받는 용돈입니다. 이번 주에 {kk}를 $$수식$${m}$$/수식$$번, {ll}를 $$수식$${n}$$/수식$$번 했다면 이번 주에 받은 용돈은 모두 얼마인가요?\n$$표$$ {kk} : $$수식$$1$$/수식$$번 $$수식$${aa}$$/수식$$원    {ll}: $$수식$$1$$/수식$$번 $$수식$${bb}$$/수식$$원 $$/표$$\n"
    answer = "(정답)\n$$수식$${cc}$$/수식$$원 또는 {a}{b}{c}{d}{e}원 또는 {f}{g}{h}{i}{j}원\n"
    comment = "(해설)\n" \
              "{kk}를 $$수식$${m}$$/수식$$번 하였으므로 $$수식$${aa}$$/수식$$원씩 "\
              "$$수식$${m}$$/수식$$번이므로 $$수식$${dd}$$/수식$$원이고,\n" \
              "{ll}를 $$수식$${n}$$/수식$$번 하였으므로 " \
              "$$수식$${bb}$$/수식$$원씩 $$수식$${n}$$/수식$$번이므로 $$수식$${ee}$$/수식$$원입니다.\n" \
              "따라서 모두 $$수식$${dd} ` + ` {ee} ` = ` {cc} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    t = ["지원이", "수진이", "사홍이", "은영이", "시현이", "주원이"]
    tt = random.choice(t)

    k = ["청소", "분리수거", "설거지", "쓰레기 버리기"]
    k1 = random.sample(k, 2)

    kk = k1[0]
    ll = k1[1]

    while True:
        m = np.random.randint(1, 30)
        n = np.random.randint(1, 30)

        a1 = random.sample([100, 500, 1000, 3000, 5000], 2)
        aa = a1[0]
        bb = a1[1]
        dd =aa*m

        ee = bb*n
        cc = dd+ee

        if ((cc>10000) & (cc<100000)):
            break

    c1= int(cc/10000)
    c2 = int((cc-c1*10000)/1000)
    c3 = int((cc-c1*10000-c2*1000)/100)

    c4= int((cc-c1*10000-c2*1000-c3*100)/10)
    c5 = int(cc-c1*10000-c2*1000-c3*100-10*c4)

    number = {1: "일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}

    if(c1==1):
      a = "만"
      f = "만"
    elif(c1==0):
      a=""
      f=""
    else:
        a = "$$수식$$%d$$/수식$$만" % (c1)
        f = "%s만" % number[c1]

    if(c2==1):
      b = "천"
      g = "천"
    elif(c2==0):
        b=""
        g=""
    else:
        b = "$$수식$$%d$$/수식$$천" % (c2)
        g = "%s천" % number[c2]

    if(c3==1):
      c = "백"
      h ="백"
    elif(c3==0):
        c=""
        h=""
    else:
        c = "$$수식$$%d$$/수식$$백" % (c3)
        h = "%s백" % number[c3]

    if(c4==1):
      d = "십"
      i = "십"
    elif(c4==0):
        d=""
        i=""
    else:
        d = "$$수식$$%d$$/수식$$십" % (c4)
        i = "%s십" % number[c4]
    if(c5==0):
        e = ""
        j=""
    else:
        e = c5
        j = "%s" % number[c5]

    stem = stem.format(tt=tt, aa=aa, bb=bb, kk=kk, ll=ll, m=m, n=n)
    answer = answer.format(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, j=j, cc=cc)
    comment = comment.format(aa=aa, kk=kk, m=m, dd=dd, ll=ll, n=n, ee=ee, cc=cc, bb=bb)

    return stem, answer, comment








# 4-1-1-22
def bignum411_Stem_017():
    stem = "㉠과 ㉡이 나타내는 값의 차는 얼마인가요?\n$$표$$ $$수식$${aa}{bb}{cc}{dd}{ee}$$/수식$$  $$수식$${ff}{gg}{hh}{ii}{jj}$$/수식$$\n㉠: 첫번째 숫자의 $$수식$${aa}$$/수식$${j1} 나타내는 값\n㉡: 두번째 숫자의 뒤에서 $$수식$${k3}$$/수식$$번째 자리 수가 나타내는 값 $$/표$$\n"
    answer = "(정답)\n$$수식$${pp}$$/수식$$\n"
    comment = "(해설)\n"\
              "㉠과 ㉡이 나타내는 값을 각각 알아보면\n"\
              "$$수식$${aa}{bb}{cc}{dd}{ee}$$/수식$$에서 ㉠은 만의 자리 숫자이므로 $$수식$${mm}$$/수식$$을,\n"\
              "$$수식$${ff}{gg}{hh}{ii}{jj}$$/수식$$에서 ㉡은 {ss}의 자리 숫자이므로 $$수식$${nn}$$/수식$$을 나타냅니다.\n"\
              "$$수식$$LEFT ($$/수식$$㉠과 ㉡이 나타내는 값의 차$$수식$$RIGHT )$$/수식$$\n$$수식$$ ` = `  {mm} `  -  ` {nn} ` =  ` {pp}$$/수식$$\n\n"


    while True:
        aa = np.random.randint(1,10)
        bb = np.random.randint(1,10)
        cc = np.random.randint(1,10)
        dd = np.random.randint(1,10)

        ee = np.random.randint(1,10)
        ff = np.random.randint(1,10)
        gg = np.random.randint(1,10)
        hh = np.random.randint(1,10)

        ii = np.random.randint(1,10)
        jj = np.random.randint(1,10)

        k1 = np.random.randint(0,5)
        k2 = [ff,gg,hh,ii,jj]
        k3 = 5 - k1
        kk = k2[k1]

        if (k1 == 0):
            ss = "만"
        elif (k1 == 1):
            ss = "천"
        elif (k1 == 2):
            ss = "백"
        elif (k1 == 3):
            ss = "십"
        elif (k1 == 4):
            ss = "일"

        mm = aa * 10000
        n = [10000, 1000, 100, 10, 1]

        nn = kk * n[k1]
        pp = mm - nn

        if pp > 0:
            break

    j1 = proc_jo(aa, 0)


    stem = stem.format(aa=aa, bb=bb, cc=cc, dd=dd, ee=ee, ff=ff, gg=gg, hh=hh, ii=ii, jj=jj, k3=k3, j1=j1)
    answer = answer.format(pp=pp)
    comment = comment.format(aa=aa, bb=bb, cc=cc, dd=dd, ee=ee, ff=ff, gg=gg, hh=hh, ii=ii, jj=jj, kk=kk, mm=mm, nn=nn, pp=pp, ss=ss)

    return stem, answer, comment









# 4-1-1-23
def bignum411_Stem_018():
    stem = "$$수식$${a} $$/수식$$원짜리 지폐 $$수식$${b}$$/수식$$장, $$수식$${c}$$/수식$$원짜리 지폐 $$수식$${d}$$/수식$$장, $$수식$${e}$$/수식$$원짜리 동전 $$수식$${f}$$/수식$$개가 있습니다. 모두 얼마인가요?\n"
    answer = "(정답)\n$$수식$${k}$$/수식$$원\n"
    comment = "(해설)\n"\
              "$$수식$${a} ``` $$/수식$$원 짜리 지폐 $$수식$${b}$$/수식$$장이면 $$수식$${g}$$/수식$$원이고, "\
              "$$수식$${c}$$/수식$$원 짜리 지폐 $$수식$${d}$$/수식$$장은 $$수식$${h}$$/수식$$원이고, "\
              "$$수식$${e}$$/수식$$원 짜리 동전 $$수식$${f}$$/수식$$개는 $$수식$${i}$$/수식$$원 입니다.\n"\
              "따라서 모두 $$수식$${g} + {h} + {i} ` = ` {k} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    number = [10000, 5000, 1000]
    number2 = [500, 100, 50, 10]

    while True:
      num = random.sample(number, 2)
      a = num[0]
      c = num[1]

      if(a > c):
          break

    while True:
      e = random.choice(number2)

      b = np.random.randint(1, 10)
      d = np.random.randint(1, 90)
      f = np.random.randint(1, 890)

      g = a*b
      h = c*d
      i = e*f
      k = g+h+i

      if ( k < 100000 ):
          break

    stem = stem.format(a=a, b=b, c=c, d=d, e=e, f=f)
    answer = answer.format(k=k)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, k=k)

    return stem, answer, comment








# 4-1-1-25
def bignum411_Stem_019():
    stem = "$$수식$$10000$$/수식$$이 $$수식$${aa}$$/수식$$개인 수를 쓰고 읽어 보세요.\n$$수식$${boxone}$$/수식$$\n$$수식$${boxtwo}$$/수식$$\n"
    answer = "(정답)\n$$수식$${bb}$$/수식$$또는 $$수식$${aa}$$/수식$$만, {dd}만\n"
    comment = "(해설)\n"\
              "$$수식$$10000$$/수식$$이 $$수식$${aa}$$/수식$$인 수는 $$수식$${bb}$$/수식$$또는 " \
              "$$수식$${aa}$$/수식$$만 이라 쓰고, {dd}만 이라고 읽습니다.\n\n"

    aa = np.random.randint(11, 10000)
    bb = aa * 10000

    a1 = int(aa/1000)
    a2 = int((aa - a1*1000)/100)
    a3 = int((aa - a1*1000 - a2*100)/10)
    a4 = int(aa % 10)

    number = {1:"일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}

    if ( a1 == 0 ):
        d1 = ""
    elif(a1 == 1):
        d1 = "천"
    else:
        d1 = "%s천" %(number[a1])

    if ( a2 == 0 ):
        d2 = ""
    elif(a2 == 1):
        d2 = "백"
    else:
        d2 = "%s백" %(number[a2])

    if ( a3 == 0 ):
        d3 = ""
    elif(a3 == 1):
        d3 = "십"
    else:
        d3 = "%s십" %(number[a3])

    if ( a4 == 0 ):
        d4 = ""
    else:
        d4 = "%s" %(number[a4])

    dd = "%s%s%s%s"%(d1,d2,d3,d4)

    boxone = "box{(쓰기)````````````````````````````````````````````````````````````}"
    boxtwo = "box{(읽기)````````````````````````````````````````````````````````````}"


    stem = stem.format(boxone=boxone, boxtwo=boxtwo, aa=aa)
    answer = answer.format(bb=bb, aa=aa, dd=dd)
    comment = comment.format(aa=aa, bb=bb, dd=dd)

    return stem, answer, comment







# 4-1-1-26
def bignum411_Stem_020():
    stem = "설명하는 수를 써 보세요.\n$$표$$ {a1}{b1}{c1}{d1}인 수 $$/표$$\n"
    answer = "(정답)\n$$수식$${a2}{b2}{c2}{d2}0000$$/수식$$ 또는 $$수식$${a2}{b2}{c2}{d2}만$$/수식$$\n"
    comment = "(해설)\n" \
              "{a1}{b1}{c1}{d1}이면\n" \
              "$$수식$${a2}{b2}{c2}{d2}0000$$/수식$$ 또는 $$수식$${a2}{b2}{c2}{d2}$$/수식$$만 이라 씁니다. \n\n"


    while True:
        aa = np.random.randint(0, 10)
        bb = np.random.randint(0, 10)
        cc = np.random.randint(0, 10)
        dd = np.random.randint(0, 10)
        temp_list = [aa, bb, cc, dd]
        if temp_list.count(0) <= 2:
            break

    if (aa == 0):
        a1 = ""
    else:
        a1 = "$$수식$$1000$$/수식$$만이 $$수식$$%d$$/수식$$개," % aa

    if (bb == 0):
        b1 = ""
    elif (cc == 0) and (dd == 0):
        b1 = " $$수식$$100$$/수식$$만이 $$수식$$%d$$/수식$$개" % bb
    else:
        b1 = " $$수식$$100$$/수식$$만이 $$수식$$%d$$/수식$$개," % bb

    if (cc == 0):
        c1 = ""
    elif (dd == 0):
        c1 = " $$수식$$10$$/수식$$만이 $$수식$$%d$$/수식$$개" % cc
    else:
        c1 = " $$수식$$10$$/수식$$만이 $$수식$$%d$$/수식$$개," % cc

    if (dd == 0):
        d1 = ""
    else:
        d1 = " 만이 $$수식$$%d$$/수식$$개" % dd

    if (aa == 0):
        a2 = ""
        if (bb == 0):
            b2 = ""
            if (cc == 0):
                c2 = ""
                if (dd == 0):
                    d2 = ""
                else:
                    d2 = dd
            else:
                c2 = cc
                d2 = dd
        else:
            b2 = bb
            c2 = cc
            d2 = dd
    else:
        a2 = aa
        b2 = bb
        c2 = cc
        d2 = dd

    stem = stem.format(a1=a1, b1=b1, c1=c1, d1=d1)
    answer = answer.format(a2=a2, b2=b2, c2=c2, d2=d2)
    comment = comment.format(a1=a1, b1=b1, c1=c1, d1=d1, a2=a2, b2=b2, c2=c2, d2=d2)

    return stem, answer, comment








# 4-1-1-28
def bignum411_Stem_021():
    stem = "다음 중 나타내는 수가 다른 하나를 찾아 기호를 써 보세요.\n$$표$$ ㉠ {qq1}\n㉡ {qq2}\n㉢ {qq3} $$/표$$ \n"
    answer = "(정답)\n{an}\n"
    comment = "(해설)\n" \
              "{c2}\n" \
              "{c3}\n\n"


    while True:
        num = [10, 100, 1000]

        aa = random.choice(num)
        bb = random.choice(num)
        cc = random.choice(num)

        dd = 10000 * bb
        ff = 1000 * cc
        gg = int(ff/10000)

        if (aa == bb and aa != gg):
            break
        elif (aa == gg and aa != bb):
            break
        elif (bb == gg and bb != gg):
            break

    q1 = "$$수식$$%d$$/수식$$만" % (aa)
    q2 = "$$수식$$%d$$/수식$$이 $$수식$$%d$$/수식$$개인 수" % (10000, bb)
    q3 = "$$수식$$%d$$/수식$$이 $$수식$$%d$$/수식$$배인 수" % (1000, cc)

    c2 = "$$수식$$%d$$/수식$$이 $$수식$$%d$$/수식$$개이면 $$수식$$%d$$/수식$$ 또는 $$수식$$%d$$/수식$$만입니다." % (10000, bb, dd, bb)
    c3 = "$$수식$$%d$$/수식$$이 $$수식$$%d$$/수식$$배이면 $$수식$$%d$$/수식$$ 또는 $$수식$$%d$$/수식$$만입니다." % (1000, cc, ff, gg)

    q = random.sample([0,1,2], 3)
    q11, q12, q13 = q[0], q[1], q[2]
    question = [q1, q2, q3]

    qq1= question[q11]
    qq2 = question[q12]
    qq3 = question[q13]

    a = [aa, bb, gg]
    aa1 = a[q11]
    aa2 = a[q12]
    aa3 = a[q13]

    a2 = ["㉠", "㉡", "㉢"]

    if (aa1 == aa2):
        an = a2[2]

    elif (aa1 == aa3):
        an = a2[1]

    elif (aa2 == aa3):
        an = a2[0]

    stem = stem.format(qq1=qq1, qq2=qq2, qq3=qq3)
    answer = answer.format(an=an)
    comment = comment.format(c2=c2, c3=c3)

    return stem, answer, comment









# 4-1-1-29
def bignum411_Stem_022():
    stem = "{A} 자리 숫자가 다른 수는 어느 것인가요?\n① $$수식$${Q1}$$/수식$$   ② $$수식$${Q2}$$/수식$$   ③ $$수식$${Q3}$$/수식$$\n④ $$수식$${Q4}$$/수식$$   ⑤ $$수식$${Q5}$$/수식$$\n"
    answer = "(정답)\n{a}\n"
    comment = "(해설)\n{A} 자리 숫자를 알아보면 ① $$수식$${a1}$$/수식$$, ② $$수식$${a2}$$/수식$$, ③ $$수식$${a3}$$/수식$$," \
              " ④ $$수식$${a4}$$/수식$$, ⑤ $$수식$${a5}$$/수식$$입니다.\n" \
              "따라서 {A}의 자리 숫자가 다른 수는 {a} 입니다.\n\n"


    A = random.choice(["십만", "백만", "천만"])

    su = {6: 0, 7: 1, 8: 2}
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    k = np.random.randint(1, 10)
    num.remove(k)
    s = random.choice(num)

    while True:
        if (A == "십만"):
            B = np.random.randint(100000, 99999999)
            C = np.random.randint(100000, 99999999)
            D = np.random.randint(100000, 99999999)
            E = np.random.randint(100000, 99999999)
            F = np.random.randint(100000, 99999999)

            B, C, D, E, F = list(str(B)), list(str(C)), list(str(D)), list(str(E)), list(str(F))
            b, c, d, e, f = len(B), len(C), len(D), len(E), len(F)

            B[su[b]] = str(k)
            C[su[c]] = str(s)
            D[su[d]] = str(s)
            E[su[e]] = str(s)
            F[su[f]] = str(s)

        elif (A == "백만"):
            B = np.random.randint(1000000, 99999999)
            C = np.random.randint(1000000, 99999999)
            D = np.random.randint(1000000, 99999999)
            E = np.random.randint(1000000, 99999999)
            F = np.random.randint(1000000, 99999999)

            B, C, D, E, F = list(str(B)), list(str(C)), list(str(D)), list(str(E)), list(str(F))
            b, c, d, e, f = len(B), len(C), len(D), len(E), len(F)

            B[su[b] - 1] = str(k)
            C[su[c] - 1] = str(s)
            D[su[d] - 1] = str(s)
            E[su[e] - 1] = str(s)
            F[su[f] - 1] = str(s)

        elif (A == "천만"):
            B = np.random.randint(10000000, 99999999)
            C = np.random.randint(10000000, 99999999)
            D = np.random.randint(10000000, 99999999)
            E = np.random.randint(10000000, 99999999)
            F = np.random.randint(10000000, 99999999)

            B, C, D, E, F = list(str(B)), list(str(C)), list(str(D)), list(str(E)), list(str(F))
            b, c, d, e, f = len(B), len(C), len(D), len(E), len(F)

            B[su[b] - 2] = str(k)
            C[su[c] - 2] = str(s)
            D[su[d] - 2] = str(s)
            E[su[e] - 2] = str(s)
            F[su[f] - 2] = str(s)

        B = "".join(B)
        B = int(B)
        C = "".join(C)
        C = int(C)

        D = "".join(D)
        D = int(D)
        E = "".join(E)
        E = int(E)

        F = "".join(F)
        F = int(F)

        if len(str(B)) == 8 and len(str(C)) == 8 and len(str(D)) == 8 and len(str(E)) == 8 and len(str(F)) == 8:
            break


    candidates = [B, C, D, E, F]
    np.random.shuffle(candidates)
    Q1, Q2, Q3, Q4, Q5 = candidates
    correct_idx = 0

    for i, c in enumerate(candidates):
        if c == B:
            correct_idx = i
            break

    aa = [s, s, s, s, s]
    aa[correct_idx] = k
    a1 = aa[0]
    a2 = aa[1]
    a3 = aa[2]
    a4 = aa[3]
    a5 = aa[4]

    stem = stem.format(Q1=Q1, Q2=Q2, Q3=Q3, Q4=Q4, Q5=Q5, A=A)
    answer = answer.format(a=answer_dict[correct_idx])
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, A=A, a=answer_dict[correct_idx])

    return stem, answer, comment








# 4-1-1-30
def bignum411_Stem_023():
    stem = "$$수식$${a}{b}{c}{d}0000$$/수식$$을 각 자리의 숫자가 나타내는 값의 합으로 나타내어 보세요.\n$$수식$${a}{b}{c}{d}0000$$/수식$$\n$$수식$$ ` = ` $$/수식$$ {boxsum}\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n"\
              "$$수식$${a}{b}{c}{d}0000 ` = ` {comme}$$/수식$$\n\n"


    while True:
        a = np.random.randint(0, 10)
        b = np.random.randint(0, 10)
        c = np.random.randint(0, 10)
        d = np.random.randint(0, 10)

        temp_list = [a, b, c, d]
        if temp_list.count(0) <= 1:
            break

    a0 = ""
    if a != 0:
        a0 = "$$수식$$%d0000000$$/수식$$" % a
        a00 = "%d0000000" % a

    b0 = ""
    if b != 0:
        b0 = "$$수식$$%d000000$$/수식$$" % b
        b00 = "%d000000" % b

    c0 = ""
    if c != 0:
        c0 = "$$수식$$%d00000$$/수식$$" % c
        c00 = "%d00000" % c

    d0 = ""
    if d != 0:
        d0 = "$$수식$$%d0000$$/수식$$" % d
        d00 = "%d0000" % d


    temp_list = [a, b, c, d]

    if temp_list.count(0) == 0:
        boxsum = "$$수식$$box{㉠``````````````````````````````}$$/수식$$  + $$수식$$box{㉡``````````````````````````````}$$/수식$$  +  $$수식$$box{㉢``````````````````````````````}$$/수식$$  + $$수식$$box{㉣``````````````````````````````}$$/수식$$"
        ans = a0 + ", " + b0 + ", " + c0 + ", " + d0
        comme = a00 + " + " + b00 + " + " + c00 + " + " + d00

    else:
        boxsum = "$$수식$$box{㉠``````````````````````````````}$$/수식$$  + $$수식$$box{㉡``````````````````````````````}$$/수식$$  + $$수식$$box{㉢``````````````````````````````}$$/수식$$"

        if (a == 0):
            a = ""
            ans = b0 + ", " + c0 + ", " + d0
            comme = b00 + " + " + c00 + " + " + d00

        elif (b == 0):
            ans = a0 + ", " + c0 + ", " + d0
            comme = a00 + " + " + c00 + " + " + d00

        elif (c == 0):
            ans = a0 + ", " + b0 + ", " + d0
            comme = a00 + " + " + b00 + " + " + d00

        elif (d == 0):
            ans = a0 + ", " + b0 + ", " + c0
            comme = a00 + " + " + b00 + " + " + c00

    stem = stem.format(a=a, b=b, c=c, d=d, boxsum=boxsum)
    answer = answer.format(ans=ans)
    comment = comment.format(a=a, b=b, c=c, d=d, comme=comme)

    return stem, answer, comment








# 4-1-1-31
def bignum411_Stem_024():
    stem = "설명하는 수가 얼마인지 써 보세요.\n$$표$$ $$수식$$100$$/수식$$만이 $$수식$${a}$$/수식$$개, $$수식$$10$$/수식$$만이 $$수식$${b}$$/수식$$개, 만이 $$수식$${c}$$/수식$$개인 수 $$/표$$\n"
    answer = "(정답)\n$$수식$${dd}{j}{k}{ii}0000$$/수식$$  또는  $$수식$${dd}{j}{k}{ii}$$/수식$$만\n"
    comment = "(해설)\n"\
              "{a0}{b0}{c0}"\
              "따라서 설명하는 수는 $$수식$$1000$$/수식$$만이 $$수식$${d}$$/수식$$개, $$수식$$100$$/수식$$만이 "\
              "$$수식$${j}$$/수식$$개, $$수식$$10$$/수식$$만이 $$수식$${k}$$/수식$$개, 만이 $$수식$${ii}$$/수식$$개인 수인"\
              "$$수식$${dd}{j}{k}{ii}0000$$/수식$$ 입니다.\n\n"


    while True:
        a = np.random.randint(1, 100)
        b = np.random.randint(1, 100)
        c = np.random.randint(1, 100)

        if (a>10 and b>10 and c<=10):
            d = int(a / 10)
            e = int(a % 10)
            f = int(b / 10)

            g = int(b % 10)
            h = int(c / 10)
            ii = int(c % 10)

            j = e + f
            k = g + h
            s = [d, e, f, g, h, ii, j,k]

            for i in range(8):
                if(s[i] >= 0 and s[i] < 10):
                    s[i] = 1

            if (s.count(1) == 8):
                break

        elif(a>10 and b<=10 and c>10):
            d = int(a / 10)
            e = int(a % 10)
            f = int(b / 10)

            g = int(b % 10)
            h = int(c / 10)
            ii = int(c % 10)

            j = e + f
            k = g + h
            s = [d, e, f, g, h, ii, j, k]

            for i in range(8):
                if(s[i] >= 0 and s[i] < 10):
                    s[i] = 1

            if(s.count(1) == 8):
                break

        elif(a<=10 and b>10 and c>10):
            d = int(a / 10)
            e = int(a % 10)
            f = int(b / 10)

            g = int(b % 10)
            h = int(c / 10)
            ii = int(c % 10)

            j = e + f
            k = g + h
            s = [d, e, f, g, h, ii, j, k]

            for i in range(8):
                if(s[i] >= 0 and s[i] < 10):
                    s[i] = 1

            if(s.count(1) == 8):
                break

    if(d == 0):
        dd = ""
    else:
        dd= d

    if(a < 10):
        a0 = ""
    else:
        a0 = "$$수식$$%d $$/수식$$만이 $$수식$$%d$$/수식$$개인 수는 $$수식$$%d$$/수식$$만 $$수식$$%d$$/수식$$개," \
             " $$수식$$%d$$/수식$$만이 $$수식$$%d$$/수식$$개인 수와 같습니다.\n" % (100, a, 1000, d, 100, e)

    if(b < 10):
        b0 = ""
    else:
        b0 = "$$수식$$%d $$/수식$$만이 $$수식$$%d$$/수식$$개인 수는 $$수식$$%d$$/수식$$만 $$수식$$%d$$/수식$$개," \
             " $$수식$$%d$$/수식$$만이 $$수식$$%d$$/수식$$개인 수와 같습니다.\n" % (10, b, 100, f, 10, g)

    if(c < 10):
        c0 = ""
    else:
        c0 = "만이 $$수식$$%d$$/수식$$개인 수는 $$수식$$%d$$/수식$$만이 $$수식$$%d$$/수식$$개,"\
             " 만이 $$수식$$%d$$/수식$$개인 수와 같습니다.\n" % (c,10,h,ii)


    stem = stem.format(a=a, b=b, c=c)
    answer = answer.format(dd=dd, j=j, k=k, ii=ii)
    comment = comment.format(a0=a0, b0=b0, c0=c0, a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, j=j, k=k, ii=ii, dd=dd)

    return stem, answer, comment








#4-1-1-32
def bignum411_Stem_025():
    stem = "어느 {tt} 공장에서 {tt} $$수식$${aa}$$/수식$$만 개를 수출하려고 합니다. 이 {tt}을 $$수식$${bb}$$/수식$$개씩 묶어서 포장하면 모두 몇 묶음으로 포장할 수 있나요?\n"
    answer = "(정답)\n$$수식$${cc}$$/수식$$ 묶음\n"
    comment = "(해설)\n"\
              "$$수식$${aa}$$/수식$$만은 $$수식$${bb}$$/수식$$이 $$수식$${cc}$$/수식$$개인 수입니다.\n"\
              "따라서 {tt}을 $$수식$${bb}$$/수식$$개씩 묶어서 포장하면 모두 $$수식$${cc}$$/수식$$ 묶음을 포장할 수 있습니다.\n\n"


    while True:
        aa = np.random.randint(11, 10000)
        b = np.random.randint(1, 5)
        bb = b * 10000

        if aa % b == 0:
            break

    cc = int(aa / b)

    t = ["인형", "장난감", "물총", "수건", "필통", "연필"]
    tt = random.choice(t)

    stem = stem.format(tt=tt, aa=aa, bb=bb)
    answer = answer.format(cc=cc)
    comment = comment.format(tt=tt, aa=aa, bb=bb, cc=cc)

    return stem, answer, comment








#4-1-1-33
def bignum411_Stem_026():
    stem = "■에 알맞은 수는 얼마인가요?\n$$표$$ $$수식$${aa}$$/수식$$만은 $$수식$$10000$$/수식$$이 ▲개인 수\n$$수식$${bb}$$/수식$$만은 $$수식$$100000$$/수식$$이 $$수식$$LEFT ($$/수식$$▲$$수식$$+$$/수식$$■$$수식$$RIGHT )$$/수식$$개인 수$$/표$$\n"
    answer = "(정답)\n$$수식$${dd}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${aa}$$/수식$$만은 $$수식$$10000$$/수식$$이 $$수식$${aa}$$/수식$$개인 수입니다.\n" \
              "→ ▲$$수식$$ ` = ` {aa} ` $$/수식$$\n"\
              "$$수식$${bb}$$/수식$$만은 $$수식$$100000$$/수식$$이 $$수식$${cc}$$/수식$$개인 수입니다.\n "\
              "→ ▲$$수식$$+$$/수식$$■$$수식$$= ` {cc}$$/수식$$\n " \
              "▲$$수식$$+$$/수식$$■$$수식$$= ` {aa} ` +$$/수식$$■$$수식$$= ` {cc}$$/수식$$\n" \
              "■$$수식$$= ` {cc} ` - ` {aa} ` = ` {dd}$$/수식$$\n\n"


    while True:
        aa = np.random.randint(10, 1000)
        b = np.random.randint(10, 1000)

        bb = b * 10
        if (aa * 10 < bb):
            break

    cc = int(bb / 10)
    dd = cc - aa

    stem = stem.format(aa=aa, bb=bb)
    answer = answer.format(dd=dd)
    comment = comment.format(aa=aa, bb=bb, cc=cc, dd=dd)

    return stem, answer, comment








#4-1-1-34
def bignum411_Stem_027():
    stem = "$$수식$${aa}{bb}{cc}{dd}{ee}{ff}{gg}{hh}$$/수식$$에서 {tt}의 자리 숫자가 나타내는 값과 {ss}의 자리 숫자가 나타내는 값의 합을 구해보세요.\n"
    answer = "(정답)\n$$수식$${zz}$$/수식$$\n"
    comment = "(해설)\n"\
              "$$수식$${aa}{bb}{cc}{dd}{ee}{ff}{gg}{hh}\n"\
              "{tt}의 자리 숫자는 $$수식$${kk}$$/수식$$이고 나타내는 값은 $$수식$${ll}$$/수식$$입니다.\n" \
              "{ss}의 자리 숫자는 $$수식$${mm}$$/수식$$이고 나타내는 값은 $$수식$${nn}$$/수식$$입니다.\n"\
              "따라서 {tt}의 자리 숫자가 나타내는 값과 {ss}의 자리 숫자가 나타내는 값의 합은 $$수식$${zz}$$/수식$$입니다.\n\n"


    aa = np.random.randint(1, 10)
    bb = np.random.randint(0, 10)
    cc = np.random.randint(0, 10)

    dd = np.random.randint(0, 10)
    ee = np.random.randint(0, 10)
    ff = np.random.randint(0, 10)

    gg = np.random.randint(0, 10)
    hh = np.random.randint(0, 10)

    while True:
        t = ["백만", "천만"]
        s = ["십만", "백만"]

        tt = random.choice(t)
        ss = random.choice(s)

        if( tt != ss):
            break

    if(tt == "백만"):
         kk = bb
         ll = bb* 1000000
    elif(tt == "천만"):
         kk = aa
         ll = aa* 10000000

    if(ss == "십만"):
         mm = cc
         nn = cc * 100000
    elif(ss == "백만"):
         mm = bb
         nn =bb * 1000000

    zz = ll + nn

    stem = stem.format(aa=aa, bb=bb, cc=cc, dd=dd, ee=ee, ff=ff, gg=gg, hh=hh, tt=tt, ss=ss)
    answer = answer.format(zz=zz)
    comment = comment.format(aa=aa, bb=bb, cc=cc, dd=dd, ee=ee, ff=ff, gg=gg, hh=hh, tt=tt, ss=ss, kk=kk, ll=ll, mm=mm, nn=nn, zz=zz)

    return stem, answer, comment









#4-1-1-36
def bignum411_Stem_028():
    stem = "모형 돈은 모두 얼마인가요?\n$$표$$ $$수식$${aa}$$/수식$$만원 짜리 모형 돈 $$수식$${bb}$$/수식$$장\n$$수식$${cc}$$/수식$$만원 짜리 모형 돈 $$수식$${dd}$$/수식$$장\n{ee} 원 짜리 모형 돈 $$수식$${ff}$$/수식$$장\n$$수식$${gg}$$/수식$$원 짜리 모형 돈 $$수식$${hh}$$/수식$$개 $$/표$$\n"
    answer = "(정답)\n$$수식$${oo}$$/수식$$원\n"
    comment = "(해설)\n"\
              "$$수식$${aa}$$/수식$$만 원짜리 모형 돈 $$수식$${bb}$$/수식$$장은 $$수식$${kk}$$/수식$$원입니다.\n" \
              "$$수식$${cc}$$/수식$$만 원짜리 모형 돈 $$수식$${dd}$$/수식$$장은 $$수식$${ll}$$/수식$$원입니다.\n" \
              "{ee} 원짜리 모형 돈 $$수식$${ff}$$/수식$$장은 $$수식$${mm}$$/수식$$원입니다.\n" \
              "$$수식$${gg}$$/수식$$ 원짜리 모형 돈 $$수식$${hh}$$/수식$$장은 $$수식$${nn}$$/수식$$원입니다.\n" \
              "따라서 모형 돈은 모두 $$수식$${kk} ` + ` {ll} ` + ` {mm} ` +  ` {nn} ` = ` {oo} `$$/수식$$(원)입니다."


    aa = random.choice([1000, 100])

    if (aa == 100):
        cc = 10
        bb = np.random.randint(1, 100)
    else:
        cc = random.choice([10, 100])
        bb = np.random.randint(1, 10)

    if (cc == 10):
        ee = random.choice(["$$수식$$5$$/수식$$만", "만", "$$수식$$1000$$/수식$$"])
    else:
        ee = random.choice(["$$수식$$10$$/수식$$만", "$$수식$$5$$/수식$$만", "만", "$$수식$$1000$$/수식$$"])

    gg = random.choice([500, 100, 50, 10])

    dd = np.random.randint(1, 100)
    ff = np.random.randint(1, 100)
    hh = np.random.randint(1, 100)

    kk = bb * aa * 10000
    ll = cc * dd * 10000

    if (ee == "$$수식$$10$$/수식$$만"):
        e = 100000
    elif (ee == "$$수식$$5$$/수식$$만"):
        e = 50000
    elif (ee == "만"):
        e = 10000
    elif (ee == "$$수식$$1000$$/수식$$"):
        e = 1000

    mm = e * ff
    nn = gg * hh
    oo = kk + ll + mm + nn

    stem = stem.format(aa=aa, bb=bb, cc=cc, dd=dd, ee=ee, ff=ff, gg=gg, hh=hh)
    answer = answer.format(oo=oo)
    comment = comment.format(aa=aa, bb=bb, cc=cc, dd=dd, ee=ee, ff=ff, gg=gg, hh=hh, ll=ll, mm=mm, nn=nn, oo=oo, kk=kk)

    return stem, answer, comment









#4-1-1-37
def bignum411_Stem_029():
    stem = "$$수식$${aa}$$/수식$$만 원짜리 수표 $$수식$${bb}$$/수식$$장, {cc}원 짜리 지폐 $$수식$${dd}$$/수식$$장이 있습니다. 이 돈을 모두 $$수식$$10$$/수식$$만원 짜리 수표로 바꾼다면 몇 장으로 바꿀 수 있나요?\n"
    answer = "(정답)\n$$수식$${hh}$$/수식$$장\n"
    comment = "(해설)\n"\
              "$$수식$${aa}$$/수식$$만 원짜리 수표 $$수식$${bb}$$/수식$$장은 $$수식$${ee}$$/수식$$원이고, "\
              "{cc}원짜리 지폐 $$수식$${dd}$$/수식$$장은 $$수식$${ff}$$/수식$$원입니다.\n"\
              "따라서 돈은 모두 $$수식$${ee} ` + ` {ff} ` = ` {gg} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$이므로 " \
              "$$수식$$10$$/수식$$만 원짜리 수표 $$수식$${hh}$$/수식$$장을 바꿀 수 있습니다.\n\n"


    a = [1000, 100, 10]
    aa = random.choice(a)

    c = ["$$수식$$5$$/수식$$만", "만", 5000, 1000]
    cc = random.choice(c)

    if (aa == 1000):
        bb = np.random.randint(1, 10)
    elif(aa == 100):
        bb = np.random.randint(1, 100)
    else:
        bb = np.random.randint(1, 500)

    d1 = np.random.randint(1, 250)
    d2 = np.random.randint(1, 50)

    d3 = np.random.randint(1, 25)
    d4 = np.random.randint(1, 5)

    if (cc == "$$수식$$5$$/수식$$만"):
        dd = 2 * d1
    elif (cc == "만"):
        dd = 10 * d2
    elif (cc == 5000):
        dd = 20 * d3
    elif (cc == 1000):
        dd = 100 *d4

    ee = aa * bb *10000

    if (cc == "$$수식$$5$$/수식$$만"):
        c1 = 50000
    elif (cc == "만"):
        c1 = 10000
    elif (cc == 5000):
        c1 = 5000
    elif (cc == 1000):
        c1 = 1000

    ff = c1 * dd
    gg = ee + ff
    hh = int(gg/100000)

    stem = stem.format(aa=aa, bb=bb, cc=cc, dd=dd)
    answer = answer.format(hh=hh)
    comment = comment.format(aa=aa, bb=bb, cc=cc, dd=dd, ee=ee, ff=ff, gg=gg, hh=hh)

    return stem, answer, comment








#4-1-1-38
def bignum411_Stem_030():
    stem = "수로 써 보세요.\n$$표$${aa1}{aa2}{aa3}{aa4}억 {aa5}{aa6}{aa7}{aa8}만$$/표$$\n"
    answer = "(정답)\n$$수식$${dd}$$/수식$$\n"
    comment = "(해설)\n"\
              "{aa1}{aa2}{aa3}{aa4}억 {aa5}{aa6}{aa7}{aa8}만 → "\
              "$$수식$${bb}$$/수식$$ 억 $$수식$${cc}$$/수식$$ 만 → "\
              "$$수식$${dd}$$/수식$$\n\n"


    while True:
        a1 = np.random.randint(0, 10)
        a2 = np.random.randint(0, 10)
        a3 = np.random.randint(0, 10)
        a4 = np.random.randint(0, 10)

        a5 = np.random.randint(0, 10)
        a6 = np.random.randint(0, 10)
        a7 = np.random.randint(0, 10)
        a8 = np.random.randint(0, 10)

        if (a1 == 0) and (a2 == 0) and (a3 == 0) and (a4 == 0):
            continue
        else:
            break

    number = {1:"일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}

    if (a1 == 0):
        aa1 = ""
    elif (a1 == 1):
        aa1 = "천"
    else:
        aa1= "%s천" % (number[a1])

    if (a2 == 0):
        aa2 = ""
    elif(a2 == 1):
        aa2 = "백"
    else:
        aa2 = "%s백" % (number[a2])

    if (a3 == 0):
        aa3 = ""
    elif(a3 == 1):
        aa3 = "십"
    else:
        aa3 = "%s십" % (number[a3])

    if (a4 == 0):
        aa4 = ""
    else:
        aa4 = "%s" % (number[a4])

    if(a5 == 0):
        aa5 = ""
    elif(a5 == 1):
        aa5 = "천"
    else:
        aa5 = "%s천" % (number[a5])

    if (a6 == 0):
        aa6 = ""
    elif(a6 == 1):
        aa6 = "백"
    else:
        aa6 = "%s백" % (number[a6])

    if (a7 == 0):
        aa7 = ""
    elif(a7 == 1):
        aa7 = "십"
    else:
        aa7 = "%s십" % (number[a7])

    if (a8 == 0):
        aa8 = ""
    else:
        aa8 = "%s" % (number[a8])

    a = (a1 *10000000 + a2*1000000 + a3*100000 + a4*10000 + a5*1000 + a6*100 + a7*10 + a8) * 10000
    bb = int(a/100000000)
    cc = int((a % 100000000)/10000)
    dd = a

    stem = stem.format(aa1=aa1, aa2=aa2, aa3=aa3, aa4=aa4, aa5=aa5, aa6=aa6, aa7=aa7, aa8=aa8)
    answer = answer.format(dd=dd)
    comment = comment.format(aa1=aa1, aa2=aa2, aa3=aa3, aa4=aa4, aa5=aa5, aa6=aa6, aa7=aa7, aa8=aa8, bb=bb, cc=cc, dd=dd)

    return stem, answer, comment









#4-1-1-39
def bignum411_Stem_031():
    stem = "설명하는 수를 수로 써 보세요.\n$$표$$ $$수식$${aa}$$/수식$$억보다 $$수식$${bb}$$/수식$$억 큰 수$$/표$$\n"
    answer = "(정답)\n$$수식$$1000000000000$$/수식$$ 또는 $$수식$$1$$/수식$$조\n"
    comment = "(해설)\n"\
              "$$수식$${aa}$$/수식$$억보다 $$수식$${bb}$$/수식$$억 큰 수는 $$수식$$1$$/수식$$조 입니다.\n"\
              "$$수식$$1$$/수식$$조 → $$수식$$1000000000000$$/수식$$\n\n"


    while True:
        aa = np.random.randint(101, 9999)
        if (aa % 10 == 0):
            break

    bb = 10000 - aa

    stem = stem.format(aa=aa, bb=bb)
    answer = answer.format()
    comment = comment.format(aa=aa, bb=bb)

    return stem, answer, comment












# 4-1-1-40
def bignum411_Stem_032():
    stem = "나타내는 수가 다른 것은 어느 것인가요?\n① {q1}\n② {q2}\n③ {q3}\n④ {q4}\n⑤ {q5}\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "{a2}는 $$수식$$1$$/수식$$억을 나타내고 {a1}은 {U}입니다. → $$수식$${W}$$/수식$$\n\n"

    def factor(number):
        f = []
        for i in range(1, number + 1):
            if (number % i == 0):
                f.append(i)
        return f

    A = factor(10000)
    while True:
        A1 = random.choice(A)
        A2 = random.choice(A)
        if (A1 != A2):
            break

    B1 = int(10000 / A1)
    B2 = int(10000 / A2)

    while True:
        C3 = np.random.randint(1, 10000)
        C4 = np.random.randint(1, 10000)
        if (C3 != C4):
            break

    D3 = int(10000 - C3)
    D4 = int(10000 - C4)

    while True:
        E = np.random.randint(1, 10000)
        F = np.random.randint(1, 10000)
        if (E * F != 10000):
            break

    while True:
        G = np.random.randint(1, 10000)
        H = np.random.randint(1, 10000)
        if (G * 10000 + H != 100000000):
            break

    T1 = "$$수식$$%d$$/수식$$만이 $$수식$$%d$$/수식$$개인 수" % (A1, B1)
    T2 = "$$수식$$%d$$/수식$$만이 $$수식$$%d$$/수식$$개인 수" % (A2, B2)
    T3 = "$$수식$$%d$$/수식$$만보다 $$수식$$%d$$/수식$$만 큰 수" % (C3, D3)
    T4 = "$$수식$$%d$$/수식$$만보다 $$수식$$%d$$/수식$$만 큰 수" % (C4, D4)
    T5 = "$$수식$$%d$$/수식$$만이 $$수식$$%d$$/수식$$개인 수" % (E, F)
    T6 = "$$수식$$%d$$/수식$$만보다 $$수식$$%d$$/수식$$ 큰 수" % (G, H)

    c1 = [T1, T2, T3, T4, T5]
    c2 = [T1, T2, T3, T4, T6]
    c = random.choice([c1, c2])
    aa1 = 0
    q1, q2, q3, q4, q5 = "", "", "", "", ""
    if (c == c1):
        W = E * 10000 * F
        num1 = [A1, A2, E]
        num2 = [C3, C4]
        num1.sort()
        num2.sort()
        if (num1[0] == A1):
            q1 = T1
            if (num1[1] == A2):
                q2 = T2
                q3 = T5
                aa1 = 2
            else:
                q2 = T5
                q3 = T2
                aa1 = 1
        elif (num1[0] == A2):
            q1 = T2
            if (num1[1] == A1):
                q2 = T1
                q3 = T5
                aa1 = 2
            else:
                q2 = T5
                q3 = T1
                aa1 = 1
        elif (num1[0] == E):
            q1 = T5
            aa1 = 0
            if (num1[1] == A1):
                q2 = T1
                q3 = T2
            else:
                q2 = T2
                q3 = T1

        if (num2[0] == C3):
            q4 = T3
            q5 = T4
        elif (num2[0] == C4):
            q4 = T4
            q5 = T3
    else:
        W = G * 10000 + H
        num1 = [A1, A2]
        num2 = [C3, C4, G]
        num1.sort()
        num2.sort()

        if (num1[0] == A1):
            q1 = T1
            q2 = T2
        elif (num1[0] == A2):
            q1 = T2
            q2 = T1

        if (num2[0] == C3):
            q3 = T3
            if (num2[1] == C4):
                q4 = T4
                q5 = T6
                aa1 = 4
            else:
                q4 = T6
                q5 = T4
                aa1 = 3
        elif (num2[0] == C4):
            q3 = T4
            if (num2[1] == C3):
                q4 = T3
                q5 = T6
            else:
                q2 = T6
                q3 = T3
        elif (num2[0] == G):
            q3 = T6
            aa1 = 2
            if (num2[1] == C3):
                q4 = T3
                q5 = T4
            else:
                q4 = T4
                q5 = T3

    a1 = answer_dict[aa1]
    a = [0, 1, 2, 3, 4]
    a.remove(aa1)
    a2 = "%s" % (answer_dict[a[0]])
    for i in range(1, 4):
        s = ", %s" % (answer_dict[a[i]])
        a2 += s

    # U1은 억, u2는 만 U3는 나머지
    W1 = int(W / 100000000)
    W2 = int((W - W1 * 100000000) / 10000)
    W3 = int((W - W1 * 100000000) % 10000)
    if (W1 == 0):
        U1 = ""
    else:
        U1 = "$$수식$$%d$$/수식$$억 " % (W1)
    if (W2 == 0):
        U2 = ""
    else:
        U2 = "$$수식$$%d$$/수식$$만 " % (W2)
    if (W3 == 0):
        U3 = ""
    else:
        U3 = "$$수식$$%d$$/수식$$" % (W3)

    U = U1 + U2 + U3

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(a1=a1)
    comment = comment.format(a1=a1, a2=a2, U=U, W=W)

    return stem, answer, comment













#4-1-1-41
def bignum411_Stem_033():
    stem = "설명하는 수를 읽어 보세요.\n$$표$$ 억이 $$수식$${aa}$$/수식$$개인 수 $$/표$$\n"
    answer = "(정답)\n{tt}억\n"
    comment = "(해설)\n"\
              "억이 $$수식$${aa}$$/수식$$개인 수는 $$수식$${bb}$$/수식$$입니다. 따라서 수를 읽어보면 {tt}억 입니다.\n\n"


    aa = np.random.randint(2, 10000)
    bb = aa * 100000000

    number = {1: "일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}

    t1 = int(aa/1000)
    t2 = int((aa - t1*1000)/100)

    t3 = int((aa - t1*1000 - t2*100)/10)
    t4 = int(aa - t1*1000 - t2*100 - t3*10)

    if (t1 == 0):
        tt1 = ""
    elif (t1 == 1):
        tt1 = "천"
    else:
        tt1 = "%s천" % (number[t1])

    if (t2 == 0):
        tt2 = ""
    elif (t2 == 1):
        tt2 = "백"
    else:
        tt2 = "%s백" % (number[t2])

    if (t3== 0):
        tt3 = ""
    elif (t3 == 1):
        tt3 = "십"
    else:
        tt3= "%s십" % (number[t3])

    if (t4 == 0):
        tt4 = ""
    else:
        tt4 = "%s" % (number[t4])

    tt = "%s%s%s%s" % (tt1, tt2, tt3, tt4)

    stem = stem.format(aa=aa)
    answer = answer.format(tt=tt)
    comment = comment.format(aa=aa,bb=bb,tt=tt)

    return stem, answer, comment









#4-1-1-42
def bignum411_Stem_034():
    stem = "숫자 $$수식$${A}$$/수식$${j1} 나타내는 값을 두 가지로 써 보세요.\n$$수식$${boxone}$$/수식$$\n"
    answer = "(정답)\n$$수식$${C}$$/수식$$, $$수식$${D}$$/수식$$억\n"
    comment = "(해설)\n"\
              "$$수식$${B}$$/수식$$에서 $$수식$${A}$$/수식$${j1} 나타내는 수는 $$수식$${C}$$/수식$$ 또는 $$수식$${D}$$/수식$$억입니다.\n\n"




    A = np.random.randint(1, 10)

    choice = np.random.randint(0, 3)

    if choice == 0:
        C = A * 100000000000
        D = A * 1000
        while True:
            temp = ""
            flag = 0
            for adx in range(11):
                temp_a = np.random.randint(0, 10)
                temp = temp + str(temp_a)
                if temp_a == 0:
                    flag += 1
            temp_list = list(temp)
            if flag <= 3 and temp_list.count(str(A)) == 0:
                B = C + int(temp)
                break

    elif choice == 1:
        C = A * 10000000000
        D = A * 100
        while True:
            ini = np.random.randint(1, 10)
            if ini != A:
                ini = ini * 100000000000
                break
        while True:
            temp = ""
            flag = 0
            for bdx in range(10):
                temp_b = np.random.randint(0, 10)
                temp = temp + str(temp_b)
                if temp_b == 0:
                    flag += 1
            temp_list = list(temp)
            if flag <= 3 and temp_list.count(str(A)) == 0:
                B = ini + C + int(temp)
                break

    elif choice == 2:
        C = A * 1000000000
        D = A * 10
        while True:
            ini1 = np.random.randint(1, 10)
            ini2 = np.random.randint(0, 10)
            if ini1 != A and ini2 != A:
                ini = ini1 * 100000000000 + ini2 * 10000000000
                break
        while True:
            temp = ""
            if ini2 == 0:
                flag = 1
            else:
                flag = 0
            for cdx in range(9):
                temp_c = np.random.randint(0, 10)
                temp = temp + str(temp_c)
                if temp_c == 0:
                    flag += 1
            temp_list = list(temp)
            if flag <= 3 and temp_list.count(str(A)) == 0:
                B = ini + C + int(temp)
                break

    boxone = "%d" % B

    j1 = proc_jo(A, 0)


    stem = stem.format(A=A, boxone=boxone, j1=j1)
    answer = answer.format(C=C, D=D)
    comment = comment.format(B=B, A=A, C=C, D=D, j1=j1)

    return stem, answer, comment







#4-1-1-43
def bignum411_Stem_035():
    stem = "□ 안에 알맞게 써넣으세요.\n$$표$$ $$수식$$1$$/수식$$조는 $$수식$${aa}$$/수식$$억보다 $$수식$${boxone}$$/수식$$억 큰 수이고 $$수식$${bb}$$/수식$$억보다 $$수식$${boxtwo}$$/수식$$억 큰 수입니다.$$/표$$\n"
    answer = "(정답)\n㉠ $$수식$${cc}$$/수식$$,  ㉡ $$수식$${dd}$$/수식$$\n"
    comment = "(해설)\n"\
              "$$수식$$1$$/수식$$조는 $$수식$${aa}$$/수식$$억보다 $$수식$${cc}$$/수식$$억 큰 수이고 "\
              "$$수식$${bb}$$/수식$$억보다 $$수식$${dd}$$/수식$$억 큰 수입니다.\n\n"


    while True:
        aa = np.random.randint(1, 100)
        bb = np.random.randint(1, 10000)
        if (aa != bb):
            break

    cc = 10000 - aa
    dd = 10000 - bb

    boxone = "box{㉠``````````````````````````````}"
    boxtwo = "box{㉡``````````````````````````````}"

    stem = stem.format(boxone=boxone, boxtwo=boxtwo, aa=aa, bb=bb)
    answer = answer.format(cc=cc, dd=dd)
    comment = comment.format(aa=aa, bb=bb, cc=cc, dd=dd)

    return stem, answer, comment










#4-1-1-44
def bignum411_Stem_036():
    stem = "설명하는 수를 읽어 보세요.\n$$표$$ 조가 $$수식$${aa}$$/수식$$개, 억 $$수식$${bb}$$/수식$$개, 만이 $$수식$${cc}$$/수식$$개인 수 $$/표$$\n"
    answer = "(정답)\n{ee}조 {ff}억 {gg}만\n"
    comment = "(해설)\n"\
              "조가 $$수식$${aa}$$/수식$$개, 억 $$수식$${bb}$$/수식$$개, 만이 $$수식$${cc}$$/수식$$개인 수\n"\
              "→ $$수식$${dd}$$/수식$$\n"\
              "→ {ee}조 {ff}억 {gg}만\n\n"


    aa = np.random.randint(11, 10000)
    bb = np.random.randint(11, 10000)
    cc = np.random.randint(11, 10000)

    dd = aa * 1000000000000 + bb * 100000000 + cc * 10000

    number = {1: "일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}

    e1 = int(aa / 1000)
    e2 = int((aa - e1 * 1000) / 100)
    e3 = int((aa - e1 * 1000 - e2 * 100) / 10)

    e4 = int(aa - e1 * 1000 - e2 * 100 - e3 * 10)

    if (e1 == 0):
        ee1 = ""
    elif (e1 == 1):
        ee1 = "천"
    else:
        ee1 = "%s천" % (number[e1])

    if (e2 == 0):
        ee2 = ""
    elif (e2 == 1):
        ee2 = "백"
    else:
        ee2 = "%s백" % (number[e2])

    if (e3 == 0):
        ee3 = ""
    elif (e3 == 1):
        ee3 = "십"
    else:
        ee3= "%s십" % (number[e3])

    if (e4 == 0):
        ee4 = ""
    else:
        ee4 = "%s" % (number[e4])

    ee = "%s%s%s%s" % (ee1, ee2, ee3, ee4)

    f1 = int(bb/1000)
    f2 = int((bb-f1*1000)/100)

    f3 = int((bb-f1*1000-f2*100)/10)
    f4 = int(bb-f1*1000-f2*100-f3*10)

    if (f1 == 0):
        ff1 = ""
    elif (f1 == 1):
        ff1 = "천"
    else:
        ff1 = "%s천" % (number[f1])

    if (f2 == 0):
        ff2 = ""
    elif (f2 == 1):
        ff2 = "백"
    else:
        ff2 = "%s백" % (number[f2])

    if (f3 == 0):
        ff3 = ""
    elif (f3 == 1):
        ff3 = "십"
    else:
        ff3= "%s십" % (number[f3])

    if (f4 == 0):
        ff4 = ""
    else:
        ff4 = "%s" % (number[f4])

    ff = "%s%s%s%s" % (ff1, ff2, ff3, ff4)

    g1 = int(cc/1000)
    g2 = int((cc-g1*1000)/100)

    g3 = int((cc-g1*1000-g2*100)/10)
    g4 = int(cc-g1*1000-g2*100-g3*10)

    if (g1 == 0):
        gg1 = ""
    elif (g1 == 1):
        gg1 = "천"
    else:
        gg1 = "%s천" % (number[g1])

    if (g2 == 0):
        gg2 = ""
    elif (g2 == 1):
        gg2 = "백"
    else:
        gg2 = "%s백" % (number[g2])

    if (g3== 0):
        gg3 = ""
    elif (g3 == 1):
        gg3 = "십"
    else:
        gg3= "%s십" % (number[g3])

    if (g4 == 0):
        gg4 = ""
    else:
        gg4 = "%s" % (number[g4])

    gg = "%s%s%s%s" % (gg1, gg2, gg3, gg4)

    stem = stem.format(aa=aa, bb=bb, cc=cc)
    answer = answer.format(ee=ee, ff=ff, gg=gg)
    comment = comment.format(aa=aa, bb=bb, cc=cc, dd=dd, ee=ee, ff=ff, gg=gg)

    return stem, answer, comment









#4-1-1-45
def bignum411_Stem_037():
    stem = "$$수식$${aa}$$/수식$$만 원짜리 수표로 $$수식$$1$$/수식$$억을 만들려고 합니다. $$수식$${aa}$$/수식$$만 원짜리 수표는 모두 몇 장이 필요한가요?\n"
    answer = "(정답)\n{bb} 장 또는 $$수식$${cc}$$/수식$$ 장\n"
    comment = "(해설)\n" \
              "$$수식$${aa}$$/수식$$만이 $$수식$$10$$/수식$$개이면 {d10}{e10}$$수식$$1$$/수식$$억입니다.\n"\
              "따라서 $$수식$${aa}$$/수식$$만이 {bb} 개이면 $$수식$$1$$/수식$$억이므로 "\
              "$$수식$${aa}$$/수식$$만 원짜리 수표는 모두 {bb} 장이 필요합니다.\n\n"


    aa = random.choice([10, 100, 1000])
    cc = int(10000/aa)

    if (cc == 1000):
        bb = "천"
    elif(cc == 100):
        bb = "백"
    else:
        bb = "열"

    if (aa == 10):
        dd = 100
        ee = 1000
        cc = 1000
        e10 = "$$수식$$%d$$/수식$$만, $$수식$$%d$$/수식$$만이 $$수식$$%d$$/수식$$개이면 " % (ee,ee, 10)
        d10 = "$$수식$$%d$$/수식$$만, $$수식$$%d$$/수식$$만이 $$수식$$%d$$/수식$$개이면 " % (dd,dd, 10)

    if (aa == 100):
        dd = 1000
        cc = 100
        e10 = ""
        d10 = "$$수식$$%d$$/수식$$만, $$수식$$%d$$/수식$$만이 $$수식$$%d$$/수식$$개이면 " % (dd,dd, 10)

    if (aa == 1000):
        cc = 10
        e10 = ""
        d10 = ""

    stem = stem.format(aa=aa)
    answer = answer.format(bb=bb, cc=cc)
    comment = comment.format(aa=aa, bb=bb, e10=e10, d10=d10)

    return stem, answer, comment









#4-1-1-46
def bignum411_Stem_038():
    stem = "다음 중 {t}억의 자리 숫자가 $$수식$${aa}$$/수식$$인 수는 어느 것인가요?\n① $$수식$${lb}$$/수식$$\n② $$수식$${lc}$$/수식$$\n③ $$수식$${ld}$$/수식$$\n④ $$수식$${le}$$/수식$$\n⑤ $$수식$${lf}$$/수식$$\n"
    answer = "(정답)\n{a}\n"
    comment = "(해설)\n"\
              "각 수의 {t}억의 자리 숫자를 알아보면 \n" \
              "① {a1}\n" \
              "② {a2}\n" \
              "③ {a3}\n" \
              "④ {a4}\n" \
              "⑤ {a5}\n\n"


    while True:
        number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        numbers = random.sample(number, 5)

        aa = numbers[0]
        c = numbers[1]
        d = numbers[2]
        e = numbers[3]
        f = numbers[4]

        num = [aa, c, d, e, f]

        t = random.choice(["십", "백", "천"])

        if (t == "십"):
            bb = (np.random.randint(10, 100)) * 10000000000 + aa * 1000000000 + np.random.randint(100000000, 1000000000)
            cc = (np.random.randint(10, 100)) * 10000000000 + c * 1000000000 + np.random.randint(100000000, 1000000000)
            dd = (np.random.randint(10, 100)) * 10000000000 + d * 1000000000 + np.random.randint(100000000, 1000000000)
            ee = (np.random.randint(10, 100)) * 10000000000 + e * 1000000000 + np.random.randint(100000000, 1000000000)
            ff = (np.random.randint(10, 100)) * 10000000000 + f * 1000000000 + np.random.randint(100000000, 1000000000)
            break

        elif (t == "백"):
            bb = (np.random.randint(1, 10)) * 100000000000 + aa * 10000000000 + np.random.randint(0, 100) * 100000000 + np.random.randint(0, 10000) * 10000 + np.random.randint(0, 10000)
            cc = (np.random.randint(1, 10)) * 100000000000 + c * 10000000000 + np.random.randint(0, 100) * 100000000 + np.random.randint(0, 10000) * 10000 + np.random.randint(0, 10000)
            dd = (np.random.randint(1, 10)) * 100000000000 + d * 10000000000 + np.random.randint(0, 100) * 100000000 + np.random.randint(0, 10000) * 10000 + np.random.randint(0, 10000)
            ee = (np.random.randint(1, 10)) * 100000000000 + e * 10000000000 + np.random.randint(0, 100) * 100000000 + np.random.randint(0, 10000) * 10000 + np.random.randint(0, 10000)
            ff = (np.random.randint(1, 10)) * 100000000000 + f * 10000000000 + np.random.randint(0, 100) * 100000000 + np.random.randint(0, 10000) * 10000 + np.random.randint(0, 10000)
            break

        elif (t == "천") and (num.count(0) == 0):
            bb = aa * 100000000000 + np.random.randint(10, 1000) * 100000000 + np.random.randint(0, 10000) * 10000 + np.random.randint(0, 10000)
            cc = c * 100000000000 + np.random.randint(10, 1000) * 100000000 + np.random.randint(0, 10000) * 10000 + np.random.randint(0, 10000)
            dd = d * 100000000000 + np.random.randint(10, 1000) * 100000000 + np.random.randint(0, 10000) * 10000 + np.random.randint(0, 10000)
            ee = e * 100000000000 + np.random.randint(10, 1000) * 100000000 + np.random.randint(0, 10000) * 10000 + np.random.randint(0, 10000)
            ff = f * 100000000000 + np.random.randint(10, 1000) * 100000000 + np.random.randint(0, 10000) * 10000 + np.random.randint(0, 10000)
            break

    candidates = [bb, cc, dd, ee, ff]
    np.random.shuffle(candidates)
    lb, lc, ld, le, lf = candidates

    correct_idx = 0
    for i, sdx in enumerate(candidates):
        if sdx == bb:
            correct_idx = i
            break

    if (t == "십"):
        lbx = int(str(lb)[2])
        lcx = int(str(lc)[2])
        ldx = int(str(ld)[2])
        lex = int(str(le)[2])
        lfx = int(str(lf)[2])

    elif (t == "백"):
        lbx = int(str(lb)[1])
        lcx = int(str(lc)[1])
        ldx = int(str(ld)[1])
        lex = int(str(le)[1])
        lfx = int(str(lf)[1])

    elif (t == "천"):
        lbx = int(str(lb)[0])
        lcx = int(str(lc)[0])
        ldx = int(str(ld)[0])
        lex = int(str(le)[0])
        lfx = int(str(lf)[0])


    a1 = "$$수식$$%d$$/수식$$ → $$수식$$%d$$/수식$$" % (lb, lbx)
    a2 = "$$수식$$%d$$/수식$$ → $$수식$$%d$$/수식$$" % (lc, lcx)
    a3 = "$$수식$$%d$$/수식$$ → $$수식$$%d$$/수식$$" % (ld, ldx)
    a4 = "$$수식$$%d$$/수식$$ → $$수식$$%d$$/수식$$" % (le, lex)
    a5 = "$$수식$$%d$$/수식$$ → $$수식$$%d$$/수식$$" % (lf, lfx)

    stem = stem.format(t=t, aa=aa, lb=lb, lc=lc, ld=ld, le=le, lf=lf)
    answer = answer.format(a=answer_dict[correct_idx])
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, aa=aa, bb=bb, t=t)

    return stem, answer, comment









#4-1-1-47
def bignum411_Stem_039():
    stem = "빈 곳에 알맞게 써넣으세요.\n{boxfirst} → $$수식$${boxpointer}$$/수식$$배 → {boxsecond} → $$수식$${boxpointer}$$/수식$$배 → {boxone} → $$수식$${boxpointer}$$/수식$$배 → {boxtwo}\n"
    answer = "(정답)\n㉠ {ee}, ㉡ {ff}\n"
    comment = "(해설)\n"\
              "$$수식$${a}$$/수식$$억의 $$수식$${kk}$$/수식$$배는 $$수식$${b}$$/수식$$억이고, " \
              "$$수식$${b}$$/수식$$억의 $$수식$${kk}$$/수식$$배는 {cc}이고, "\
              "{cc}의 $$수식$${kk}$$/수식$$배는 {dd}입니다.\n\n"


    a = np.random.randint(2, 101)

    kk = np.random.randint(2, 51)

    b = a * kk

    c = b * kk

    if c < 10000:
        cc = "$$수식$$%d$$/수식$$억" % c
    else:
        c1 = c // 10000
        c2 = c % 10000
        cc = "$$수식$$%d$$/수식$$조 $$수식$$%d$$/수식$$억" % (c1, c2)

    d = c * kk

    if d < 10000:
        dd = "$$수식$$%d$$/수식$$억" % d
    else:
        d1 = d // 10000
        d2 = d % 10000
        dd = "$$수식$$%d$$/수식$$조 $$수식$$%d$$/수식$$억" % (d1, d2)

    boxfirst = "$$수식$$%s$$/수식$$억" % a
    boxpointer = "(%d)" % kk

    choice = np.random.randint(0, 3)

    if choice == 0:
        boxsecond = "$$수식$$%s$$/수식$$억" % b
        boxone = "$$수식$$box{㉠````````````````````}$$/수식$$"
        boxtwo = "$$수식$$box{㉡````````````````````}$$/수식$$"
        ee = cc
        ff = dd

    elif choice == 1:
        boxsecond = "$$수식$$box{㉠````````````````````}$$/수식$$"
        boxtwo = "$$수식$$box{㉡````````````````````}$$/수식$$"
        ee = "$$수식$$%d$$/수식$$억" % b
        ff = dd

        if c < 10000:
            boxone = "$$수식$$%s$$/수식$$억" % c
        else:
            boxone = "$$수식$$%d$$/수식$$조    $$수식$$%d$$/수식$$억" % (c1, c2)

    else:
        boxsecond = "$$수식$$box{㉠````````````````````}$$/수식$$"
        boxone = "$$수식$$box{㉡````````````````````}$$/수식$$"
        ee = "$$수식$$%d$$/수식$$억" % b
        ff = cc

        if d < 10000:
            boxtwo = "$$수식$$%s$$/수식$$억" % d
        else:
            boxtwo = "$$수식$$%d$$/수식$$조    $$수식$$%d$$/수식$$억" % (d1, d2)

    stem = stem.format(boxpointer=boxpointer, boxone=boxone, boxtwo=boxtwo, boxfirst=boxfirst, boxsecond=boxsecond)
    answer = answer.format(ee=ee, ff=ff)
    comment = comment.format(a=a, b=b, cc=cc, dd=dd, kk=kk)

    return stem, answer, comment








#4-1-1-48
def bignum411_Stem_040():
    stem = "수로 나타내면 $$수식$$0$$/수식$$은 모두 몇 개인지 구해 보세요.\n$$표$${boxone}$$/표$$\n"
    answer = "(정답)\n$$수식$${gg}$$/수식$$\n"
    comment = "(해설)\n"\
              "→ {aa}\n"\
              "→ $$수식$${bb}$$/수식$$조 {C} {D} {E}\n"\
              "→ $$수식$${ff}$$/수식$$\n"\
              "따라서 $$수식$${ff}$$/수식$$에 $$수식$$0$$/수식$$은 $$수식$${gg}$$/수식$$개입니다.\n\n"


    ff = np.int64(random.randint(1000000000000, 10000000000000000))
    sf = str(ff)
    gg = sf.count("0")

    bb = int(ff/1000000000000)
    c1 = int(ff % 1000000000000)
    cc = int(c1 /100000000)

    dd = int((c1%100000000)/10000)
    ee = int((c1%100000000)%10000)


    C = "$$수식$$%d$$/수식$$억" % cc
    D = "$$수식$$%d$$/수식$$만" % dd
    E = "$$수식$$%d$$/수식$$" % ee

    number = {1: "일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}

    bb1 = int(bb/1000)
    bb2 = int((bb-bb1*1000)/100)
    bb3 = int((bb-bb1*1000-bb2*100)/10)
    bb4 = int(bb-bb1*1000-bb2*100-bb3*10)

    if(bb1==0):
        b1 = ""
    elif(bb1==1):
        b1 = "천"
    else:
        b1 = "%s천" % number[bb1]

    if(bb2==0):
        b2 = ""
    elif(bb2==1):
        b2 = "백"
    else:
        b2 = "%s백" % number[bb2]

    if(bb3==0):
        b3 = ""
    elif(bb3==1):
        b3= "십"
    else:
        b3 = "%s십" % number[bb3]

    if(bb4==0):
        b4= ""
    else:
        b4= "%s" % number[bb4]

    cc1 = int(cc/1000)
    cc2 = int((cc-cc1*1000)/100)

    cc3 = int((cc-cc1*1000-cc2*100)/10)
    cc4 = int(cc-cc1*1000-cc2*100-cc3*10)

    if (cc1 == 0):
        c1 = ""
    elif(cc1==1):
        c1 = "천"
    else:
        c1 = "%s천" % number[cc1]

    if (cc2 == 0):
        c2 = ""
    elif(cc2==1):
        c2 = "백"
    else:
        c2 = "%s백" % number[cc2]

    if (cc3 == 0):
        c3 = ""
    elif(cc3==1):
        c3 = "십"
    else:
        c3 = "%s십" % number[cc3]

    if (cc4 == 0):
        c4 = ""
    else:
        c4 = "%s" % number[cc4]

    dd1 = int(dd/1000)
    dd2 = int((dd-dd1*1000)/100)

    dd3 = int((dd-dd1*1000-dd2*100)/10)
    dd4 = int(dd-dd1*1000-dd2*100-dd3*10)

    if (dd1 == 0):
        d1 = ""
    elif(dd1==1):
        d1 = "천"
    else:
        d1 = "%s천" % number[dd1]

    if (dd2 == 0):
        d2 = ""
    elif(dd2==1):
        d2 = "백"
    else:
        d2 = "%s백" % number[dd2]

    if (dd3 == 0):
        d3 = ""
    elif(dd3==1):
        d3 = "십"
    else:
        d3 = "%s십" % number[dd3]

    if (dd4 == 0):
        d4 = ""
    else:
        d4 = "%s" % number[dd4]

    ee1 = int(ee/1000)
    ee2 = int((ee-ee1*1000)/100)

    ee3 = int((ee-ee1*1000-ee2*100)/10)
    ee4 = int(ee-ee1*1000-ee2*100-ee3*10)

    if (ee1 == 0):
        e1 = ""
    elif(ee1 ==1):
        e1 = "천"
    else:
        e1 = "%s천" % number[ee1]

    if (ee2 == 0):
        e2 = ""
    elif(ee2 ==1):
        e2 = "백"
    else:
        e2 = "%s백" % number[ee2]

    if (ee3 == 0):
        e3 = ""
    elif(ee3 ==1):
        e3 = "십"
    else:
        e3 = "%s십" % number[ee3]

    if (ee4 == 0):
        e4 = ""
    else:
        e4 = "%s" % number[ee4]


    b = "%s%s%s%s" % (b1, b2, b3, b4)
    c = "%s%s%s%s" % (c1, c2, c3, c4)
    d = "%s%s%s%s" % (d1, d2, d3, d4)
    e = "%s%s%s%s" % (e1, e2, e3, e4)


    if(cc==0):
        ac = ""
    else:
        ac = "%s억" % (c)

    if(dd==0):
        ad = ""
    else:
        ad = "%s만" % (d)

    ab = "%s조" % b
    aa = "%s   %s   %s   %s" % (ab, ac, ad, e)
    boxone = "%s %s %s %s" % (ab, ac, ad, e)

    stem = stem.format(boxone=boxone)
    answer = answer.format(gg=gg)
    comment = comment.format(aa=aa, gg=gg, bb=bb, C=C, D=D, E=E, ff=ff)

    return stem, answer, comment















#4-1-1-49
def bignum411_Stem_041():
    stem = "{AA}조의 자리의 숫자와 {BB}억의 자리 숫자의 합을 구해 보세요.\n$$표$${boxone}$$/표$$\n"
    answer = "(정답)\n$$수식$${F}$$/수식$$\n"
    comment = "(해설)\n"\
              "$$수식$${a}{b}{c}{d}$$/수식$$|$$수식$${e}{f}{g}{h}$$/수식$$|$$수식$${i}{j}{k}{l}$$/수식$$|"\
              "$$수식$${m}{n}{o}{p} $$/수식$$\n"\
              "  조|  억|  만|  일\n"\
              "따라서 {AA}조의 자리 숫자는 $$수식$${D}$$/수식$$이고 {BB}억의 자리 숫자는 "\
              "$$수식$${E}$$/수식$$이므로 두 수의 합은 $$수식$${D} ` + ` {E} ` =  ` {F}$$/수식$$입니다.\n\n"


    a = np.random.randint(1, 9)
    b = np.random.randint(1, 9)
    c = np.random.randint(1, 9)
    d = np.random.randint(1, 9)

    e = np.random.randint(1, 9)
    f = np.random.randint(1, 9)
    g = np.random.randint(1, 9)
    h = np.random.randint(1, 9)

    i = np.random.randint(1, 9)
    j = np.random.randint(1, 9)
    k = np.random.randint(1, 9)
    l = np.random.randint(1, 9)

    m = np.random.randint(1, 9)
    n = np.random.randint(1, 9)
    o = np.random.randint(1, 9)
    p = np.random.randint(1, 9)

    A = random.choice(["천", "백", "십", "일"])
    B = random.choice(["천", "백", "십", "일"])

    if(A=="일"):
        AA = ""
    else:
        AA = A

    if(B=="일"):
        BB=""
    else:
        BB = B

    if(A=="천"):
        D = a
    elif(A =="백"):
        D = b
    elif(A=="십"):
        D = c
    elif(A=="일"):
        D = d

    if(B=="천"):
        E = e
    elif(B =="백"):
        E = f
    elif(B=="십"):
        E = g
    elif(B=="일"):
        E = h

    F = D+E

    boxone = "%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d" %(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p)

    stem = stem.format(AA=AA, BB=BB, boxone=boxone)
    answer = answer.format(F=F)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, j=j, k=k, l=l, m=m, n=n, o=o, p=p, AA=AA, D=D, BB=BB, E=E, F=F)

    return stem, answer, comment









# 4-1-1-51
def bignum411_Stem_042():
    stem = "숫자 $$수식$${A}$$/수식$$를(을) 나타내는 값이 더 큰 수를 써 보세요.\n$$수식$${boxone}$$/수식$$ $$수식$${boxtwo}$$/수식$$\n"
    answer = "(정답)\n$$수식$${B}$$/수식$$\n"
    comment = "(해설)\n"\
              "각 수에서 숫자 $$수식$${A}$$/수식$$이 나타내는 값을 각각 알아보면 {c1}, {c2}입니다.\n"\
              "따라서 숫자가 $$수식$${A}$$/수식$$이 나타내는 값이 더 큰 수는\n"\
              "$$수식$${B}$$/수식$$입니다.\n\n"


    A  = np.random.randint(2, 10)
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num.remove(A)

    B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    C = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    a = np.random.randint(0, 6)
    while True:
        B[0] = np.random.randint(1, 10)
        C[0] = np.random.randint(1, 10)

        if B[0] != A and C[0] != A: break

    for i in range(1, 16):
        B[i] = random.choice(num)
    for i in range(1, 15):
        C[i] = random.choice(num)

    B[a] = A
    C[a] = A

    e = ["천조","백조","십조","조","천억","백억"]
    g = ["백조","십조","조","천억","백억","십억"]

    E = e[a]
    G = g[a]

    f = [1000, 100, 10, 1, 1000, 100]
    ff = ["조", "조", "조", "조", "억", "억"]
    h = [100, 10, 1, 1000, 100, 10]
    hh = ["조", "조", "조", "억", "억", "억"]

    F = "$$수식$$%d$$/수식$$%s" % (A*f[a], ff[a])
    H = "$$수식$$%d$$/수식$$%s" % (A*h[a], hh[a])

    B = list(map(str, B))
    C = list(map(str, C))

    B1 = "".join(B)
    B = int(B1)
    C1 = "".join(C)
    C = int(C1)

    ba = "$$수식$$%d$$/수식$$에서 $$수식$$%d$$/수식$$은 %s의 자리 숫자이므로 %s" % (B, A, E, F)
    ca = "$$수식$$%d$$/수식$$에서 $$수식$$%d$$/수식$$은 %s의 자리 숫자이므로 %s" % (C, A, G, H)

    BC = [B, C]
    random.shuffle(BC)

    b = BC[0]
    c = BC[1]

    if b == B:
        c1 = ba
        c2 = ca
    else:
        c1 = ca
        c2 = ba

    boxone = "box{%d}" % (b)
    boxtwo = "box{%d}" % (c)

    stem = stem.format(A=A, boxone=boxone, boxtwo = boxtwo)
    answer = answer.format(B=B)
    comment = comment.format(A=A, B=B, c1=c1, c2=c2)

    return stem, answer, comment










#4-1-1-52
def bignum411_Stem_043():
    stem = "□ 안에 알맞은 수를 차례대로 쓰시오\n{box1} → {box2} → {box3} → {box4} → {box5} → {box6} → {box7}\n"
    answer = "(정답)\n{answer_result}\n"
    comment = "(해설)\n"\
              "$$수식$${e}$$/수식$$만은 $$수식$${d}$$/수식$$의 $$수식$${a}$$/수식$$배이고, " \
              "$$수식$${e}$$/수식$$만의 $$수식$${b}$$/수식$$배는 $$수식$${f}$$/수식$$억, " \
              "$$수식$${f}$$/수식$$억의 $$수식$${c}$$/수식$$배는 $$수식$${g}$$/수식$$조입니다.\n\n"



    num = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
    answer_seq = dict()

    g = random.choice(num)
    f = random.choice(num)
    e = random.choice(num)
    d = random.choice(num)

    c = int((g*10000)/f)
    b = int((f*10000)/e)
    a = int((e*10000)/d)

    box2 = "$$수식$$%d$$/수식$$배" % a
    box4 = "$$수식$$%d$$/수식$$배" % b
    box6 = "$$수식$$%d$$/수식$$배" % c

    while True:
        choice1 = np.random.choice([2, 4, 6])
        choice2 = np.random.choice([1, 3, 5])
        choice3 = np.random.choice([3, 5, 7])
        if (choice2 < choice3) and abs(choice1-choice2) != 1 and abs(choice3-choice1) != 1:
            break
    
    if choice1 == 2:
        box2 = "$$수식$$box{　　　}$$/수식$$배"
        aa1 = "$$수식$$%d$$/수식$$" % a
    elif choice1 == 4:
        box4 = "$$수식$$box{　　　}$$/수식$$배"
        aa1 = "$$수식$$%d$$/수식$$" % a
    else:
        box6 = "$$수식$$box{　　　}$$/수식$$배"
        aa1 = "$$수식$$%d$$/수식$$" % a

    answer_seq[choice1] = aa1

    box1 = "$$수식$$%d$$/수식$$" % d
    box3 = "$$수식$$%d$$/수식$$만" % e
    box5 = "$$수식$$%s$$/수식$$억" % f
    box7 = "$$수식$$%d$$/수식$$조" % g

    

    if choice2 == 1:
        box1 = "$$수식$$box{　　　}$$/수식$$"
        aa2 = "$$수식$$%d$$/수식$$" % d
    elif choice2 == 3:
        box3 = "$$수식$$box{　　　}$$/수식$$만"
        aa2 = "$$수식$$%d$$/수식$$" % e
    elif choice2 == 5:
        box5 = "$$수식$$box{　　　}$$/수식$$억"
        aa2 = "$$수식$$%d$$/수식$$" % f

    if choice3 == 3:
        box3 = "$$수식$$box{　　　}$$/수식$$만"
        aa3 = "$$수식$$%d$$/수식$$" % e
    elif choice3 == 5:
        box5 = "$$수식$$box{　　　}$$/수식$$억"
        aa3 = "$$수식$$%d$$/수식$$" % f
    elif choice3 == 7:
        box7 = "$$수식$$box{　　　}$$/수식$$조"
        aa3 = "$$수식$$%d$$/수식$$" % g
        
    answer_seq[choice2] = aa2
    answer_seq[choice3] = aa3
    
    answer_seq = sorted(answer_seq.items())
    answer_result = []
    
    for i in answer_seq:
        answer_result.append(i[-1])
        
    answer_result = ", ".join(answer_result)

    stem = stem.format(box1=box1, box2=box2, box3=box3, box4=box4, box5=box5, box6=box6, box7=box7)
    answer = answer.format(answer_result=answer_result)
    comment = comment.format(c=c, d=d, e=e, b=b, a=a, f=f, g=g)

    return stem, answer, comment










#4-1-1-53
def bignum411_Stem_044():
    stem = "다음을 수로 쓸 때 $$수식$$0$$/수식$$의 개수가 더 많은 것의 기호를 써 보세요.\n$$표$$ ㉠ {q1}\n ㉡ {q2} $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n"\
              "㉠ {cc1}\n"\
              "㉡ {cc2}\n\n"



    while True:
        while True:
            A = np.random.randint(100, 10000)
            b = np.random.randint(1, 100)
            B = 10 * b
            D = int(A * B / 10000)
            if (A * B) % 10000 == 0:
                break

        E = D * 100000000
        f = str(E)
        F = f.count("0")

        c = np.int64(random.randint(1000000000, 999999999999))

        G = int(c/100000000)
        H = int((c%100000000)/10000)
        I = int((c%100000000)%10000)

        J = G *100000000+H*10000+I
        j = str(J)
        K = j.count("0")

        pp = F - K
        if abs(pp) < 4:
            break


    if (F == K):
        A = A * 10
        D = int(A * B / 10000)
        E = D * 100000000
        f = str(E)
        F = f.count("0")

    number = {1: "일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}

    G1 = int(G / 1000)
    G2 = int((G - G1 * 1000) / 100)
    G3 = int((G - G1 * 1000 - G2 * 100) / 10)
    G4 = int(G- G1 * 1000 - G2 * 100 - G3 * 10)

    if (G1 == 0):
        g1 = ""
    elif (G1 == 1):
        g1 = "천"
    else:
        g1 = "%s천" % number[G1]

    if (G2 == 0):
        g2 = ""
    elif (G2 == 1):
        g2 = "백"
    else:
        g2 = "%s백" % number[G2]

    if (G3 == 0):
        g3 = ""
    elif (G3 == 1):
        g3 = "천"
    else:
        g3 = "%s십" % number[G3]

    if (G4 == 0):
        g4 = ""
    else:
        g4 = "%s" % number[G4]

    H1 = int(H / 1000)
    H2 = int((H - H1 * 1000) / 100)
    H3 = int((H - H1 * 1000 - H2 * 100) / 10)
    H4 = int(H- H1 * 1000 - H2 * 100 - H3 * 10)

    if (H1 == 0):
        h1 = ""
    elif (H1 == 1):
        h1 = "천"
    else:
        h1 = "%s천" % number[H1]

    if (H2 == 0):
        h2 = ""
    elif (H2 == 1):
        h2 = "백"
    else:
        h2 = "%s백" % number[H2]

    if (H3 == 0):
        h3 = ""
    elif (H3 == 1):
        h3 = "천"
    else:
        h3 = "%s십" % number[H3]

    if (H4 == 0):
        h4 = ""
    else:
        h4 = "%s" % number[H4]

    I1 = int(I / 1000)
    I2 = int((I - I1 * 1000) / 100)
    I3 = int((I - I1 * 1000 - I2 * 100) / 10)
    I4 = int(I- I1 * 1000 - I2 * 100 - I3 * 10)

    if (I1 == 0):
        i1 = ""
    elif (I1 == 1):
        i1 = "천"
    else:
        i1 = "%s천" % number[I1]

    if (I2 == 0):
        i2 = ""
    elif (I2 == 1):
        i2 = "백"
    else:
        i2 = "%s백" % number[I2]

    if (I3 == 0):
        i3 = ""
    elif (I3 == 1):
        i3 = "천"
    else:
        i3 = "%s십" % number[I3]

    if (I4 == 0):
        i4 = ""
    else:
        i4 = "%s" % number[I4]

    g = "%s%s%s%s" % (g1, g2, g3, g4)
    h = "%s%s%s%s" % (h1, h2, h3, h4)
    i = "%s%s%s%s" % (i1, i2, i3, i4)

    cg = "%s억" % g
    ch = "%s만" % h
    ci = "%s" % i

    C = "%s %s %s" % (cg, ch, ci)
    
    
    qq1 = "$$수식$$%d$$/수식$$만의 $$수식$$%d$$/수식$$배인 수" % (A, B)
    qq2 = C

    qq = [qq1, qq2]
    random.shuffle(qq)
    q1, q2 = qq[0], qq[1]
    L = max(F, K)

    if (L==F):
        if(qq1==q1):
            a1 = "㉠"
        else:
            a1 = "㉡"

    else:
        if(qq1==q1):
            a1 = "㉡"
        else:
            a1 = "㉠"

    c1 = "$$수식$$%d$$/수식$$만의 $$수식$$%d$$/수식$$배인 수는 $$수식$$%d$$/수식$$억입니다.\n"\
         "→ $$수식$$%d$$/수식$$ → $$수식$$%d$$/수식$$이 $$수식$$%d$$/수식$$개" % (A, B, D, E, 0, F)

    c2 = "%s → $$수식$$%d$$/수식$$억 $$수식$$%d$$/수식$$만 $$수식$$%d$$/수식$$"\
         "→ $$수식$$%d$$/수식$$ → $$수식$$%d$$/수식$$이 $$수식$$%d$$/수식$$개" % (C, G, H, I, J, 0, K)

    c3 = "\n따라서 수로 쓸 때 $$수식$$0$$/수식$$의 개수가 더 많은 것은 $$수식$$%s$$/수식$$입니다." % a1


    if(qq1 == q1):
        cc1 = c1
        cc2 = c2 + c3
    else:
        cc2 = c1 + c3
        cc1 = c2

    stem = stem.format(q1=q1, q2=q2)
    answer = answer.format(a1=a1)
    comment = comment.format(cc1=cc1, cc2=cc2)

    return stem, answer, comment










#4-1-1-55
def bignum411_Stem_045():
    stem = "어느 회사의 올해 총 자산은 $$수식$${A}$$/수식$$억 원입니다. 이 회사의 자산이 매년 $$수식$${B}$$/수식$$배가 된다면 $$수식$$5$$/수식$$년 후 이 회사의 총 자산은 얼마인가요?\n"
    answer = "(정답)\n{H}원\n"
    comment = "(해설)\n"\
              "수를 $$수식$${B}$$/수식$$배씩 하면\n" \
              "$$수식$${A}$$/수식$$억 ― {D} ― {E} ― {F} ― {G} ― {H}입니다.\n"\
               "따라서 $$수식$${B}$$/수식$$배씩 $$수식$$5$$/수식$$번 한 수가 {H}이므로 $$수식$$5$$/수식$$"\
               "년 후 이 회사의 총 자산은 {H}원입니다.\n\n"


    A = np.random.randint(11, 1000)
    B = np.random.randint(2, 11)


    d = A * B

    if d >= 10000:
        d1 = int(d // 10000)
        d2 = int(d % 10000)
        D = "$$수식$$%d$$/수식$$조 $$수식$$%d$$/수식$$억" % (d1, d2)
    else:
        D = "$$수식$$%d$$/수식$$억" % d


    e = d * B

    if (e >= 10000) and (e % 10000) == 0:
        e1 = int(e // 10000)
        E = "$$수식$$%d$$/수식$$조" % (e1)
    elif e >= 10000:
        e1 = int(e // 10000)
        e2 = int(e % 10000)
        E = "$$수식$$%d$$/수식$$조 $$수식$$%d$$/수식$$억" % (e1, e2)
    else:
        E = "$$수식$$%d$$/수식$$억" % e


    f = e * B

    if (f >= 10000) and (f % 10000) == 0:
        f1 = int(f // 10000)
        F = "$$수식$$%d$$/수식$$조" % (f1)
    elif f >= 10000:
        f1 = int(f // 10000)
        f2 = int(f % 10000)
        F = "$$수식$$%d$$/수식$$조 $$수식$$%d$$/수식$$억" % (f1, f2)
    else:
        F = "$$수식$$%d$$/수식$$억" % f



    g = f * B

    if (g >= 10000) and (g % 10000) == 0:
        g1 = int(g // 10000)
        G = "$$수식$$%d$$/수식$$조" % (g1)
    elif g >= 10000:
        g1 = int(g // 10000)
        g2 = int(g % 10000)
        G = "$$수식$$%d$$/수식$$조 $$수식$$%d$$/수식$$억" % (g1, g2)
    else:
        G = "$$수식$$%d$$/수식$$억" % g


    h = g * B

    if (h >= 10000) and (h % 10000) == 0:
        h1 = int(h // 10000)
        H = "$$수식$$%d$$/수식$$조" % (h1)
    elif h >= 10000:
        h1 = int(h // 10000)
        h2 = int(h % 10000)
        H = "$$수식$$%d$$/수식$$조 $$수식$$%d$$/수식$$억" % (h1, h2)
    else:
        H = "$$수식$$%d$$/수식$$억" % h

    stem = stem.format(A=A, B=B)
    answer = answer.format(H=H)
    comment = comment.format(A=A, B=B, D=D, E=E, F=F, G=G, H=H)

    return stem, answer, comment










#4-1-1-56
def bignum411_Stem_046():
    stem = "$$수식$$LEFT ($$/수식$$가$$수식$$RIGHT )$$/수식$$에서 숫자 $$수식$${A}$$/수식$${a} 나타내는 값은 $$수식$$LEFT ($$/수식$$나$$수식$$RIGHT )$$/수식$$에서 숫자 $$수식$${A}$$/수식$${a} 나타내는 값의 몇 배인가요?\n$$표$$$$수식$$LEFT ($$/수식$$가$$수식$$RIGHT )$$/수식$$ $$수식$${B}$$/수식$$              $$수식$$LEFT ($$/수식$$나$$수식$$RIGHT )$$/수식$$ $$수식$${C}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${K}$$/수식$$배 또는 {L}배 또는 {M}배\n"
    comment = "(해설)\n"\
              "$$수식$$LEFT ($$/수식$$가$$수식$$RIGHT )$$/수식$$ 숫자 $$수식$${A}$$/수식$${a} 나타내는 값:\n" \
              "$$수식$${D}  LEFT ( 0$$/수식$$이 $$수식$${E}$$/수식$$개$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$LEFT ($$/수식$$나$$수식$$RIGHT )$$/수식$$ 숫자 $$수식$${A}$$/수식$${a} 나타내는 값:\n" \
              "$$수식$${F}  LEFT ( 0$$/수식$$이 $$수식$${G}$$/수식$$개$$수식$$RIGHT )$$/수식$$\n"\
              "따라서 $$수식$${D}$$/수식$$은 $$수식$${F}$$/수식$$보다 $$수식$$0$$/수식$$이 $$수식$${H}$$/수식$$개 더 많으므로 $$수식$${K}$$/수식$$배입니다.\n\n"


    A = np.random.randint(1, 10)

    if(A==2 or A==4 or A==5 or A==9):
        a = "가"
    else:
        a = "이"

    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    num.remove(A)

    while True:
        bk = np.random.randint(12,16)
        b = list(range(bk))
        bj = np.random.randint(0,6)
        ck = np.random.randint(7,16)
        c = list(range(ck))
        cj = np.random.randint(0,6)

        for i in range(bk):
            b[i] = random.choice(num)
        b[bj] = A

        for i in range(ck):
            c[i] = random.choice(num)
        c[cj] = A

        b = list(map(str,b))
        c = list(map(str,c))
        B = "".join(b)
        C = "".join(c)

        for i in range(bj):
            b[i]=""
        for i in range(bj+1,bk):
            b[i] ="0"
        for i in range(cj):
            c[i]=""
        for i in range(cj+1,ck):
            c[i] ="0"

        b = list(map(str,b))
        c = list(map(str,c))
        D = "".join(b)
        F = "".join(c)

        E = D.count("0")
        G = F.count("0")

        H = E-G
        if(H <= 0):
            bj = bj+1
            continue
        else:
            break

    L=""
    M=""
    K = 10**H

    if(H==1):
        L = "십"
        M = "$$수식$$1$$/수식$$십"
    elif(H==2):
        L = "백"
        M = "$$수식$$1$$/수식$$백"
    elif(H==3):
        L = "천"
        M = "$$수식$$1$$/수식$$천"
    elif(H==4):
        L = "만"
        M = "$$수식$$1$$/수식$$만"
    elif(H==5):
        L ="십만"
        M = "$$수식$$10$$/수식$$만"
    elif(H==6):
        L = "백만"
        M = "$$수식$$100$$/수식$$만"
    elif(H==7):
        L = "천만"
        M = "$$수식$$1000$$/수식$$만"
    elif(H==8):
        L = "억"
        M = "$$수식$$1$$/수식$$억"
    elif(H==9):
        L = "십억"
        M = "$$수식$$10$$/수식$$억"
    elif(L==10):
        L = "백억"
        M = "$$수식$$100$$/수식$$억"
    elif(L==11):
        L = "천억"
        M = "$$수식$$1000$$/수식$$억"
    elif(L==12):
        L = "조"
        M = "$$수식$$1$$/수식$$조"
    elif(L==13):
        L = "십조"
        M = "$$수식$$10$$/수식$$조"


    stem = stem.format(A=A, B=B, C=C, a=a)
    answer = answer.format(K=K, L=L, M=M)
    comment = comment.format(A=A, F=F, G=G, D=D, H=H, K=K, a=a, E=E)

    return stem, answer, comment











#4-1-1-57
def bignum411_Stem_047():
    stem = "$$수식$${A}$$/수식$$만 씩 뛰어 세보세요.\n$$수식$${B}$$/수식$$만 ― $$수식$${C}$$/수식$$만 ― $$수식$${D}$$/수식$$만 ― $$수식$${boxone}$$/수식$$ ― $$수식$${boxtwo}$$/수식$$ ― $$수식$${boxthree}$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${E}$$/수식$$만, ㉡ $$수식$${F}$$/수식$$만, ㉢ $$수식$${G}$$/수식$$만\n"
    comment = "(해설)\n"\
              "$$수식$${A}$$/수식$$만씩 뛰어 세면 {T}의 자리 수가 $$수식$$1$$/수식$$씩 커집니다.\n\n"\


    A = random.choice([1, 10, 100, 1000])

    if (A == 1):
        T = "만"
    elif (A == 10):
        T = "십만"
    elif (A == 100):
        T = "백만"
    elif (A == 1000):
        T = "천만"

    B = np.random.randint(2, 5000)

    C = B + A
    D = C + A
    E = D + A
    F = E + A
    G = F + A
    
    boxone = "box{㉠``````````````````````````````}"
    boxtwo = "box{㉡``````````````````````````````}"
    boxthree = "box{㉢``````````````````````````````}"

    stem = stem.format(A=A, B=B, C=C, D=D, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree)
    answer = answer.format(E=E, F=F, G=G)
    comment = comment.format(A=A, T=T)

    return stem, answer, comment










#4-1-1-58
def bignum411_Stem_048():
    stem = "다음은 얼마만큼씩 뛰어 센 것인가요?\n$$수식$${A}$$/수식$$억 ― $$수식$${B}$$/수식$$억 ― $$수식$${C}$$/수식$$억 ―\n― $$수식$${D}$$/수식$$억 ― $$수식$${E}$$/수식$$억 ― $$수식$${F}$$/수식$$억\n$$수식$${boxone}$$/수식$$씩\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$억 또는 {S1}억\n"
    comment = "(해설)\n"\
              "{T}의 자리 수가 $$수식$${Q}$$/수식$$씩 커지므로 $$수식$${S}$$/수식$$억씩 뛰어 센 것입니다.\n\n"\


    A = np.random.randint(2, 5000)
    T = random.choice(["일억", "십억", "백억", "천억"])
    Q = np.random.randint(1, 10)

    if (T == "일억"):
        R = 1
    elif (T == "십억"):
        R = 10
    elif (T == "백억"):
        R = 100
    elif (T == "천억"):
        R = 1000

    S = Q * R
    B = A + S
    C = B + S

    D = C + S
    E = D + S
    F = E + S

    if (F > 10000):
        Q = Q - 1
        if (T == "일억"):
            R = 1
        elif (T == "십억"):
            R = 10
        elif (T == "백억"):
            R = 100
        elif (T == "천억"):
            R = 1000

        S = Q * R
        B = A + S
        C = B + S
        D = C + S
        E = D + S
        F = E + S

    number = {1: "일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}

    if (R == 1):
        S1 = number[Q]
        S2 = "$$수식$$%d$$/수식$$" % (Q)
    elif (R == 10):
        if(Q == 1):
            S1 = "십"
        else:
            S1 = number[Q] + "십"
        S2 = "$$수식$$%d$$/수식$$십" % (Q)
        
    elif (R == 100):
        if (Q == 1):
            S1 = "백"
        else:
            S1 = number[Q] + "백"
        S2 = "$$수식$$%d$$/수식$$백" % (Q)
    elif (R == 1000):
        if (Q == 1):
            S1 = "천"
        else:
            S1 = number[Q] +"천"
        S2 = "$$수식$$%d$$/수식$$천" % (Q)
   

    boxone = "box{　　　``````````}"

    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, boxone=boxone)
    answer = answer.format(S=S, S1=S1, S2=S2)
    comment = comment.format(T=T, Q=Q, S=S)

    return stem, answer, comment










# 4-1-1-59
def bignum411_Stem_049():
    stem = "규칙에 따라 빈칸에 알맞은 말을 써넣으세요.\n{A} ― {B1} ― {C1}\n―$$수식$${boxone}$$/수식$$ ― $$수식$${boxtwo}$$/수식$$ ― $$수식$${boxthree}$$/수식$$\n"
    answer = "(정답)\n{D1}, {E1}, {F1}\n"
    comment = "(해설)\n" \
              "$$수식$${a}$$/수식$$억―{B}―{C}에서 {T}억의 자리 수가 $$수식$${Q}$$/수식$$씩 커지므로 $$수식$${R}$$/수식$$" \
              "억씩 뛰어 센 것입니다.\n따라서 빈칸에 {D1}, {E1}, {F1}을 써넣어야 합니다.\n\n"

    while True:
        a = np.random.randint(101, 9000)
        T = random.choice(["일", "십", "백", "천"])
        Q = np.random.randint(1, 10)
        if (T == "일"):
            t = 1
        elif (T == "십"):
            t = 10
        elif (T == "백"):
            t = 100
        elif (T == "천"):
            t = 1000
        R = Q * t
        b = a + R
        c = b + R
        d = c + R
        e = d + R
        f = e + R
        if (f < 100000000):
            break

    number = {1: "일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}
    a1 = int(a / 1000)
    a2 = int((a - a1 * 1000) / 100)
    a3 = int((a - a1 * 1000 - a2 * 100) / 10)
    a4 = int(a - a1 * 1000 - a2 * 100 - a3 * 10)

    if (a1 == 0):
        A1 = ""
    elif (a1 == 1):
        A1 = "천"
    else:
        A1 = "%s천" % number[a1]

    if (a2 == 0):
        A2 = ""
    elif (a2 == 1):
        A2 = "백"
    else:
        A2 = "%s백" % number[a2]

    if (a3 == 0):
        A3 = ""
    elif (a3 == 1):
        A3 = "십"
    else:
        A3 = "%s십" % number[a3]

    if (a4 == 0):
        A4 = ""
    else:
        A4 = "%s" % number[a4]
    A = A1 + A2 + A3 + A4 + "억"

    if (b >= 10000):
        B = "$$수식$$%d$$/수식$$조 $$수식$$%d$$/수식$$억" % (int(b / 10000), int(b % 10000))
    else:
        B = "$$수식$$%d$$/수식$$억" % (int(b % 10000))
    if (c >= 10000):
        C = "$$수식$$%d$$/수식$$조 $$수식$$%d$$/수식$$억" % (int(c / 10000), int(c % 10000))
    else:
        C = "$$수식$$%d$$/수식$$억" % (int(c % 10000))

    cj = int(c / 10000)
    cu = int(c % 10000)
    cj1 = int(cj / 1000)
    cj2 = int((cj - cj1 * 1000) / 100)
    cj3 = int((cj - cj1 * 1000 - cj2 * 100) / 10)
    cj4 = int(cj - cj1 * 1000 - cj2 * 100 - cj3 * 10)
    cu1 = int(cu / 1000)
    cu2 = int((cu - cu1 * 1000) / 100)
    cu3 = int((cu - cu1 * 1000 - cu2 * 100) / 10)
    cu4 = int(cu - cu1 * 1000 - cu2 * 100 - cu3 * 10)

    if (cj1 == 0):
        CJ1 = ""
    elif (cj1 == 1):
        CJ1 = "천"
    else:
        CJ1 = "%s천" % number[cj1]

    if (cj2 == 0):
        CJ2 = ""
    elif (cj2 == 1):
        CJ2 = "백"
    else:
        CJ2 = "%s백" % number[cj2]

    if (cj3 == 0):
        CJ3 = ""
    elif (cj3 == 1):
        CJ3 = "십"
    else:
        CJ3 = "%s십" % number[cj3]

    if (cj4 == 0):
        CJ4 = ""
    else:
        CJ4 = "%s조" % number[cj4]
    if (cu1 == 0):
        CU1 = ""
    elif (cu1 == 1):
        CU1 = "천"
    else:
        CU1 = "%s천" % number[cu1]

    if (cu2 == 0):
        CU2 = ""
    elif (cu2 == 1):
        CU2 = "백"
    else:
        CU2 = "%s백" % number[cu2]

    if (cu3 == 0):
        CU3 = ""
    elif (cu3 == 1):
        CU3 = "십"
    else:
        CU3 = "%s십" % number[cu3]

    if (cu4 == 0):
        CU4 = ""
    else:
        CU4 = "%s" % number[cu4]
    C1 = CJ1 + CJ2 + CJ3 + CJ4 + CU1 + CU2 + CU3 + CU4 + "억"

    bj = int(b / 10000)
    bu = int(b % 10000)
    bj1 = int(bj / 1000)
    bj2 = int((bj - bj1 * 1000) / 100)
    bj3 = int((bj - bj1 * 1000 - bj2 * 100) / 10)
    bj4 = int(bj - bj1 * 1000 - bj2 * 100 - bj3 * 10)
    bu1 = int(bu / 1000)
    bu2 = int((bu - bu1 * 1000) / 100)
    bu3 = int((bu - bu1 * 1000 - bu2 * 100) / 10)
    bu4 = int(bu - bu1 * 1000 - bu2 * 100 - bu3 * 10)

    if (bj1 == 0):
        BJ1 = ""
    elif (bj1 == 1):
        BJ1 = "천"
    else:
        BJ1 = "%s천" % number[bj1]

    if (bj2 == 0):
        BJ2 = ""
    elif (bj2 == 1):
        BJ2 = "백"
    else:
        BJ2 = "%s백" % number[bj2]

    if (bj3 == 0):
        BJ3 = ""
    elif (bj3 == 1):
        BJ3 = "십"
    else:
        BJ3 = "%s십" % number[bj3]

    if (bj4 == 0):
        BJ4 = ""
    else:
        BJ4 = "%s조" % number[bj4]
    if (bu1 == 0):
        BU1 = ""
    elif (bu1 == 1):
        BU1 = "천"
    else:
        BU1 = "%s천" % number[bu1]

    if (bu2 == 0):
        BU2 = ""
    elif (bu2 == 1):
        BU2 = "백"
    else:
        BU2 = "%s백" % number[bu2]

    if (bu3 == 0):
        BU3 = ""
    elif (bu3 == 1):
        BU3 = "십"
    else:
        BU3 = "%s십" % number[bu3]

    if (bu4 == 0):
        BU4 = ""
    else:
        BU4 = "%s" % number[bu4]
    B1 = BJ1 + BJ2 + BJ3 + BJ4 + BU1 + BU2 + BU3 + BU4 + "억"

    dj = int(d / 10000)
    du = int(d % 10000)
    dj1 = int(dj / 1000)
    dj2 = int((dj - dj1 * 1000) / 100)
    dj3 = int((dj - dj1 * 1000 - dj2 * 100) / 10)
    dj4 = int(dj - dj1 * 1000 - dj2 * 100 - dj3 * 10)
    du1 = int(du / 1000)
    du2 = int((du - du1 * 1000) / 100)
    du3 = int((du - du1 * 1000 - du2 * 100) / 10)
    du4 = int(du - du1 * 1000 - du2 * 100 - du3 * 10)

    if (dj1 == 0):
        DJ1 = ""
    elif (dj1 == 1):
        DJ1 = "천"
    else:
        DJ1 = "%s천" % number[dj1]

    if (dj2 == 0):
        DJ2 = ""
    elif (dj2 == 1):
        DJ2 = "백"
    else:
        DJ2 = "%s백" % number[dj2]

    if (dj3 == 0):
        DJ3 = ""
    elif (dj3 == 1):
        DJ3 = "십"
    else:
        DJ3 = "%s십" % number[dj3]

    if (dj4 == 0):
        DJ4 = ""
    else:
        DJ4 = "%s조" % number[dj4]
    if (du1 == 0):
        DU1 = ""
    elif (du1 == 1):
        DU1 = "천"
    else:
        DU1 = "%s천" % number[du1]

    if (du2 == 0):
        DU2 = ""
    elif (du2 == 1):
        DU2 = "백"
    else:
        DU2 = "%s백" % number[du2]

    if (du3 == 0):
        DU3 = ""
    elif (du3 == 1):
        DU3 = "십"
    else:
        DU3 = "%s십" % number[du3]

    if (du4 == 0):
        DU4 = ""
    else:
        DU4 = "%s" % number[du4]
    D1 = DJ1 + DJ2 + DJ3 + DJ4 + DU1 + DU2 + DU3 + DU4 + "억"

    ej = int(e / 10000)
    eu = int(e % 10000)
    ej1 = int(ej / 1000)
    ej2 = int((ej - ej1 * 1000) / 100)
    ej3 = int((ej - ej1 * 1000 - ej2 * 100) / 10)
    ej4 = int(ej - ej1 * 1000 - ej2 * 100 - ej3 * 10)
    eu1 = int(eu / 1000)
    eu2 = int((eu - eu1 * 1000) / 100)
    eu3 = int((eu - eu1 * 1000 - eu2 * 100) / 10)
    eu4 = int(eu - eu1 * 1000 - eu2 * 100 - eu3 * 10)

    if (ej1 == 0):
        EJ1 = ""
    elif (ej1 == 1):
        EJ1 = "천"
    else:
        EJ1 = "%s천" % number[ej1]

    if (ej2 == 0):
        EJ2 = ""
    elif (ej2 == 1):
        EJ2 = "백"
    else:
        EJ2 = "%s백" % number[ej2]

    if (ej3 == 0):
        EJ3 = ""
    elif (ej3 == 1):
        EJ3 = "십"
    else:
        EJ3 = "%s십" % number[ej3]

    if (ej4 == 0):
        EJ4 = ""
    else:
        EJ4 = "%s조" % number[ej4]
    if (eu1 == 0):
        EU1 = ""
    elif (eu1 == 1):
        EU1 = "천"
    else:
        EU1 = "%s천" % number[eu1]

    if (eu2 == 0):
        EU2 = ""
    elif (eu2 == 1):
        EU2 = "백"
    else:
        EU2 = "%s백" % number[eu2]

    if (eu3 == 0):
        EU3 = ""
    elif (eu3 == 1):
        EU3 = "십"
    else:
        EU3 = "%s십" % number[eu3]

    if (eu4 == 0):
        EU4 = ""
    else:
        EU4 = "%s" % number[eu4]
    E1 = EJ1 + EJ2 + EJ3 + EJ4 + EU1 + EU2 + EU3 + EU4 + "억"

    fj = int(f / 10000)
    fu = int(f % 10000)
    fj1 = int(fj / 1000)
    fj2 = int((fj - fj1 * 1000) / 100)
    fj3 = int((fj - fj1 * 1000 - fj2 * 100) / 10)
    fj4 = int(fj - fj1 * 1000 - fj2 * 100 - fj3 * 10)
    fu1 = int(fu / 1000)
    fu2 = int((fu - fu1 * 1000) / 100)
    fu3 = int((fu - fu1 * 1000 - fu2 * 100) / 10)
    fu4 = int(fu - fu1 * 1000 - fu2 * 100 - fu3 * 10)

    if (fj1 == 0):
        FJ1 = ""
    elif (fj1 == 1):
        FJ1 = "천"
    else:
        FJ1 = "%s천" % number[fj1]

    if (fj2 == 0):
        FJ2 = ""
    elif (fj2 == 1):
        FJ2 = "백"
    else:
        FJ2 = "%s백" % number[fj2]

    if (fj3 == 0):
        FJ3 = ""
    elif (fj3 == 1):
        FJ3 = "십"
    else:
        FJ3 = "%s십" % number[fj3]

    if (fj4 == 0):
        FJ4 = ""
    else:
        FJ4 = "%s조" % number[fj4]
    if (fu1 == 0):
        FU1 = ""
    elif (fu1 == 1):
        FU1 = "천"
    else:
        FU1 = "%s천" % number[fu1]

    if (fu2 == 0):
        FU2 = ""
    elif (fu2 == 1):
        FU2 = "백"
    else:
        FU2 = "%s백" % number[fu2]

    if (fu3 == 0):
        FU3 = ""
    elif (fu3 == 1):
        FU3 = "십"
    else:
        FU3 = "%s십" % number[fu3]

    if (fu4 == 0):
        FU4 = ""
    else:
        FU4 = "%s" % number[fu4]
    F1 = FJ1 + FJ2 + FJ3 + FJ4 + FU1 + FU2 + FU3 + FU4 + "억"

    boxone = "box{㉠``````````````````````````````````````````````````}"
    boxtwo = "box{㉡``````````````````````````````````````````````````}"
    boxthree = "box{㉢``````````````````````````````````````````````````}"

    stem = stem.format(A=A, B1=B1, C1=C1, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree)
    answer = answer.format(D1=D1, E1=E1, F1=F1)
    comment = comment.format(R=R, a=a, B=B, C=C, T=T, Q=Q, D1=D1, E1=E1, F1=F1)

    return stem, answer, comment











#4-1-1-60
def bignum411_Stem_050():
    stem = "$$수식$${A}$$/수식$$조씩 뛰어 세었을 때 ㉠을 구해보세요\n$$수식$${B}$$/수식$$조 $$수식$${C}$$/수식$$억 ― $$수식$${D}$$/수식$$조 $$수식$${C}$$/수식$$억 ― $$수식$${emptybox}$$/수식$$\n― $$수식$${emptybox}$$/수식$$ ― $$수식$${emptybox}$$/수식$$ ― $$수식$${boxone}$$/수식$$\n"
    answer = "(정답)\n$$수식$${E}$$/수식$$조 $$수식$${C}$$/수식$$억\n"
    comment = "(해설)\n"\
              "$$수식$${A}$$/수식$$조씩 뛰어 세면 조의 자리 숫자가 $$수식$${A}$$/수식$$씩 커지므로 "\
              "$$수식$${B}$$/수식$$조 $$수식$${C}$$/수식$$억 ― $$수식$${D}$$/수식$$조 $$수식$${C}$$/수식$$억 ― "\
              "$$수식$${D1}$$/수식$$조 $$수식$${C}$$/수식$$억 ― $$수식$${D2}$$/수식$$조 $$수식$${C}$$/수식$$억 ― "\
              "$$수식$${D3}$$/수식$$조 $$수식$${C}$$/수식$$억 ― $$수식$${E}$$/수식$$조 $$수식$${C}$$/수식$$억입니다.\n"\
              "따라서 ㉠에 들어갈 수는 $$수식$${E}$$/수식$$조 $$수식$${C}$$/수식$$억입니다.\n\n"


    A = np.random.randint(2, 100)
    B = np.random.randint(2, 1000)
    C = np.random.randint(2, 10000)

    D = B + A
    D1 = D + A

    D2 = D + 2 * A
    D3 = D + 3 * A
    E = D + 4 * A

    boxone = "box{㉠``````````````````````````````````````````````````}"
    emptybox = "[``````````````````````````````````````````````````]"

    stem = stem.format(A=A, B=B, C=C, D=D, emptybox=emptybox, boxone=boxone)
    answer = answer.format(E=E, C=C)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, D1=D1, D2=D2, D3=D3)

    return stem, answer, comment











#4-1-1-61
def bignum411_Stem_051():
    stem = "뛰어 세기를 하였습니다. 빈칸에 알맞은 수를 써넣으세요.\n$$수식$${boxone}$$/수식$$  $$수식$${boxtwo}$$/수식$$  $$수식$${boxthree}$$/수식$$  $$수식$${boxfour}$$/수식$$  $$수식$${boxfive}$$/수식$$\n"
    answer = "(정답)\n$$수식$${F}$$/수식$$, $$수식$${G}$$/수식$$\n"
    comment = "(해설)\n"\
              "{H}의 자리 수가 $$수식$${K}$$/수식$$씩 커지므로 $$수식$${M}$$/수식$$씩 뛰어 센 것입니다.\n\n"


    A = np.random.randint(100000, 99999999)
    K = np.random.randint(1, 10)
    H = random.choice(["천", "만", "십만", "백만", "천만"])

    if (H == "천"):
        h = 1000
    elif (H == "만"):
        h = 10000
    elif (H == "십만"):
        h = 100000

    elif (H == "백만"):
        h = 1000000
    elif (H == "천만"):
        h = 10000000

    M = h * K
    B = A + M
    C = B + M

    D = C + M
    E = D + M

    q = random.sample([0, 1, 2], 2)

    q1, q2 = q[0], q[1]

    cde = [C, D, E]
    qq1 = cde[q1]
    qq2 = cde[q2]

    if (q1 > q2):
        cde[q2]= "㉠"
        cde[q1]= "㉡"
        F = qq2
        G = qq1
    else:
        cde[q1]= "㉠"
        cde[q2]= "㉡"
        F = qq1
        G = qq2

    C,D,E = cde[0], cde[1], cde[2]
    C,D,E = str(C), str(D), str(E)

    boxone = "box{%d}" % (A)
    boxtwo = "box{%d}" % (B)
    boxthree = "box{%s```````````````}" % (C)

    boxfour = "box{%s```````````````}" % (D)
    boxfive = "box{%s```````````````}" % (E)

    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour, boxfive=boxfive)
    answer = answer.format(F=F, G=G)
    comment = comment.format(H=H, K=K, M=M)

    return stem, answer, comment











#4-1-1-62
def bignum411_Stem_052():
    stem = "어떤 수에서 $$수식$${A}$$/수식$$억씩 뛰어 세기를 $$수식$${B}$$/수식$$번 한 수가 $$수식$${C}$$/수식$$억이었습니다. 어떤 수를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$억\n"
    comment = "(해설)\n"\
              "$$수식$${C}$$/수식$$억에서 $$수식$${A}$$/수식$$억씩 거꾸로 $$수식$${B}$$/수식$$번 뛰어 세면 "\
              "$$수식$${C}$$/수식$$억 ― $$수식$${CA}$$/수식$$억 ― $$수식$${CA2}$$/수식$$억 ― $$수식$${CA3}$$/수식$$억"\
              " {CA4} {CA5} {CA6}입니다.\n\n"


    A = np.random.randint(2, 1000)
    B = np.random.randint(3, 7)
    C = np.random.randint(A * B, 10000)

    D = C - B * A
    CA = C -A

    CA2 = C - 2 * A
    CA3 = C - 3 * A

    if (B == 3):
        CA4 = ""
        CA5 = ""
        CA6 = ""

    if (B == 4):
        CA4 = "- $$수식$$%d$$/수식$$억" % (C - 4 * A)
        CA5 = ""
        CA6 = ""

    elif (B == 5):
        CA4 = "- $$수식$$%d$$/수식$$억" % (C - 4 * A)
        CA5 = "- $$수식$$%d$$/수식$$억" % (C - 5 * A)
        CA6 = ""

    elif (B == 6):
        CA4 = "- $$수식$$%d$$/수식$$억" % (C - 4 * A)
        CA5 = "- $$수식$$%d$$/수식$$억" % (C - 5 * A)
        CA6 = "- $$수식$$%d$$/수식$$억" % (C - 6 * A)

    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(D=D)
    comment = comment.format(A=A, B=B, C=C, CA=CA, CA2=CA2, CA3=CA3, CA4=CA4, CA5=CA5, CA6=CA6)

    return stem, answer, comment








#4-1-1-63
def bignum411_Stem_053():
    stem = "■에 알맞은 수에서 $$수식$${A}$$/수식$$억씩 뛰어 세기를 $$수식$$5$$/수식$$번 했더니 다음과 같았습니다. ■에 알맞은 수를 구해 보세요.\n$$수식$${boxone}$$/수식$$―$$수식$${boxblank}$$/수식$$―$$수식$${boxblank}$$/수식$$\n―$$수식$${boxblank}$$/수식$$―$$수식$${boxblank}$$/수식$$―$$수식$${boxsix}$$/수식$$\n"
    answer = "(정답)\n$$수식$${C}$$/수식$$억\n"
    comment = "(해설)\n"\
              "$$수식$${B}$$/수식$$억에서 $$수식$${A}$$/수식$$억씩 거꾸로 뛰어 세기를 $$수식$$5$$/수식$$번 하면 "\
              "$$수식$${B}$$/수식$$억―$$수식$${BA}$$/수식$$억―$$수식$${BA2}$$/수식$$억―$$수식$${BA3}$$/수식$$억"\
              "―$$수식$${BA4}$$/수식$$억―$$수식$${BA5}$$/수식$$억입니다.\n" \
              "따라서 ■에 알맞은 수는 $$수식$${C}$$/수식$$억입니다.\n\n"


    A = np.random.randint(1, 100)
    B = np.random.randint(1001, 10000)

    BA = B - A

    BA2 = B - 2 * A
    BA3 = B - 3 * A
    BA4 = B - 4 * A
    BA5 = B - 5 * A

    C = BA5

    boxone = "■"
    boxblank = "[````````````````````]"
    boxsix = "%s억" % B

    stem = stem.format(A=A, boxone=boxone, boxblank=boxblank, boxsix=boxsix)
    answer = answer.format(C=C)
    comment = comment.format(A=A, B=B, BA=BA, BA2=BA2, BA3=BA3, BA4=BA4, BA5=BA5, C=C)

    return stem, answer, comment









# 4-1-1-65
def bignum411_Stem_054():
    stem = "{T}네 가족은 {S}에 $$수식$${A}$$/수식$$월부터 매월 $$수식$${B}$$/수식$$원씩 기부하기로 하였습니다. 기부한 전체 금액이 {C}원이 되는 달은 몇 월인가요?\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$월\n"
    comment = "(해설)\n" \
              "매월 $$수식$${B}$$/수식$$원씩 기부하므로 $$수식$${B}$$/수식$$씩 뛰어 세면 {b}{nb}이므로 " \
              "{C}원이 되는 달은 $$수식$${D}$$/수식$$월입니다.\n\n"


    T = random.choice(["진경이", "경선이", "경국이", "소민이", "철민이", "사랑이"])
    S = random.choice(["아동 보호 단체", "결핍 아동 보호 단체", "굿네이버스", "유니세프", "초록우산", "아름다운 재단"])

    A = np.random.randint(1, 5)
    b = np.random.randint(1, 20)
    B = b * 5000
    N = np.random.randint(5, 9)
    c = N * B
    D = A + N - 1
    if (B / 10000 == 0):
        b = "$$수식$$%d$$/수식$$천$$수식$$LEFT ( %d$$/수식$$월$$수식$$RIGHT ) $$/수식$$" % (int((int(B % 10000) / 1000)), A)
    else:
        if (B % 10000 == 0):
            b = "$$수식$$%d$$/수식$$만$$수식$$LEFT ( %d$$/수식$$월$$수식$$RIGHT ) $$/수식$$" % (int(B / 10000), A)
        else:
            b = "$$수식$$%d$$/수식$$만 $$수식$$%d$$/수식$$천$$수식$$LEFT ( %d$$/수식$$월$$수식$$RIGHT ) $$/수식$$" \
                % (int(B / 10000), int((int(B % 10000) / 1000)), A)
    nb = ""
    for i in range(1, N):
        ss = B * (i + 1)
        if (ss / 10000 == 0):
            s = "→$$수식$$%d$$/수식$$천$$수식$$LEFT ( %d$$/수식$$월$$수식$$RIGHT ) $$/수식$$" % (int((int(ss % 10000) / 1000)), A + i)
        else:
            if (ss % 10000 == 0):
                s = "→$$수식$$%d$$/수식$$만$$수식$$LEFT ( %d$$/수식$$월$$수식$$RIGHT ) $$/수식$$" % (int(ss / 10000), A + i)
            else:
                s = "→$$수식$$%d$$/수식$$만 $$수식$$%d$$/수식$$천$$수식$$LEFT ( %d$$/수식$$월$$수식$$RIGHT ) $$/수식$$" \
                    % (int(ss / 10000), int((int(ss % 10000) / 1000)), A + i)
        nb = nb + s

    if (c / 10000 == 0):
        C = "$$수식$$%d$$/수식$$천" % int((int(c % 10000) / 1000))
    else:
        if (c % 10000 == 0):
            C = "$$수식$$%d$$/수식$$만" % int(c / 10000)
        else:
            C = "$$수식$$%d$$/수식$$만 $$수식$$%d$$/수식$$천" \
                % (int(c / 10000), int((int(c % 10000) / 1000)))
    stem = stem.format(T=T, S=S, A=A, B=B, C=C)
    answer = answer.format(D=D)
    comment = comment.format(C=C, D=D, B=B, b=b, nb=nb)

    return stem, answer, comment














#4-1-1-66
def bignum411_Stem_055():
    stem = "얼마만큼씩 뛰어 센 것인지 규칙을 찾아 빈 곳에 써넣으세요.\n$$수식$${boxone}$$/수식$$―$$수식$${boxtwo}$$/수식$$―$$수식$${boxthree}$$/수식$$\n―$$수식$${boxfour}$$/수식$$―$$수식$${boxfive}$$/수식$$―$$수식$${boxsix}$$/수식$$\n"
    answer = "(정답)\n㉠ {G}, ㉡ {H}\n"
    comment = "(해설)\n"\
              "$$수식$${K}$$/수식$$만씩 뛰어 세었습니다.\n"\
              "$$수식$${A}$$/수식$$만―$$수식$${B}$$/수식$$만―$$수식$${C}$$/수식$$만―$$수식$${D}$$/수식$$만"\
              "―$$수식$${E}$$/수식$$만―$$수식$${F}$$/수식$$만\n\n"


    F = np.random.randint(6001, 9999)
    k = np.random.randint(1, 100)

    K = k * 10

    E = F - K
    D = E - K

    C = D - K
    B = C - K
    A = B - K

    a = "%d만" % (A)
    b = "%d만" % (B)
    c = "%d만" % (C)

    d = "%d만" % (D)
    e = "%d만" % (E)
    f = "%d만" % (F)


    while True:
        q1 = np.random.randint(0, 4)
        q2 = np.random.randint(1, 5)
        if q1 < q2:
            break

    boxone = "%s" % (a)
    boxtwo = "%s" % (b)
    boxthree = "%s" % (c)
    boxfour = "%s" % (d)
    boxfive = "%s" % (e)
    boxsix = "%s" % (f)

    if q1 == 0:
        boxtwo = "box{㉠``````````````````````````````}"
        G = "$$수식$$%d$$/수식$$만" % B
    elif q1 == 1:
        boxthree = "box{㉠``````````````````````````````}"
        G = "$$수식$$%d$$/수식$$만" % C
    elif q1 == 2:
        boxfour = "box{㉠``````````````````````````````}"
        G = "$$수식$$%d$$/수식$$만" % D
    elif q1 == 3:
        boxfive = "box{㉠``````````````````````````````}"
        G = "$$수식$$%d$$/수식$$만" % E

    if q2 == 1:
        boxthree = "box{㉡``````````````````````````````}"
        H = "$$수식$$%d$$/수식$$만" % C
    elif q2 == 2:
        boxfour = "box{㉡``````````````````````````````}"
        H = "$$수식$$%d$$/수식$$만" % D
    elif q2 == 3:
        boxfive = "box{㉡``````````````````````````````}"
        H = "$$수식$$%d$$/수식$$만" % E
    elif q2 == 4:
        boxsix = "box{㉡``````````````````````````````}"
        H = "$$수식$$%d$$/수식$$만" % F


    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour, boxfive=boxfive, boxsix=boxsix)
    answer = answer.format(G=G, H=H)
    comment = comment.format(K=K, A=A, B=B, C=C, D=D, E=E, F=F)

    return stem, answer, comment












#4-1-1-67
def bignum411_Stem_056():
    stem = "{T}네 가족은 {S} 여행을 가기 위해 매월 $$수식$${A}$$/수식$$만 원씩 저금하여 $$수식$${B}$$/수식$$만원을 모으기로 하였습니다. {T}네 가족이 {S} 여행에 필요한 돈을 모으려면 모두 몇 개월이 걸리는지 구해보세요.\n"
    answer = "(정답)\n$$수식$${N}$$/수식$$개월\n"
    comment = "(해설)\n"\
              "{a1}\n따라서 {T}네 가족이 {S} 여행에 필요한 돈을 모으려면 모두 $$수식$${N}$$/수식$$개월이 걸립니다.\n\n"


    T = random.choice(["진경이", "경선이", "경국이", "소민이", "철민이", "사랑이"])
    S = random.choice(["제주도", "대부도", "동해", "남해", "부산", "전주"])

    while True:
        A = np.random.randint(2, 100)
        N = np.random.randint(2, 20)
        B = N * A
        if B >= 50:
            break

    a1 = "$$수식$$%d$$/수식$$만" % (A)

    for i in range(2, N+1):
        s = "―$$수식$$%d$$/수식$$만" % (A * i)
        a1 = a1 + s

    stem = stem.format(T=T, S=S, A=A, B=B)
    answer = answer.format(N=N)
    comment = comment.format(a1=a1, T=T, S=S, N=N)

    return stem, answer, comment










#4-1-1-68
def bignum411_Stem_057():
    stem = "어떤 수에서 $$수식$${A}$$/수식$$억씩 뛰어 세기를 $$수식$${N}$$/수식$$번 한 수가 {B}입니다. 어떤 수는 얼마인가요?\n"
    answer = "(정답)\n{C}\n"
    comment = "(해설)\n"\
              "{B}에서 $$수식$${A}$$/수식$$억씩 거꾸로 뛰어 세기를 $$수식$${N}$$/수식$$번 합니다.\n"\
              "{B}{a1}\n따라서 어떤 수는 {C}입니다.\n\n"


    while True:
        a = np.random.randint(1, 500)
        A = 10 * a
        N = np.random.randint(4, 7)
        b = np.random.randint(1000, 999999)
        if ((b - N * A) > 0):
            break

    if (int(b / 10000) == 0):
        B = "$$수식$$%d$$/수식$$억" % (int(b % 10000))
    elif (int(b % 10000) == 0):
        B = "$$수식$$%d$$/수식$$조" % (int(b / 10000))
    else:
        B = "$$수식$$%d$$/수식$$조 $$수식$$%d$$/수식$$억" %(int(b / 10000), int(b % 10000))

    a1 = ""

    for i in range(1, N + 1):
        if (int((b-i*A) / 10000) == 0):
            s = "―$$수식$$%d$$/수식$$억" % (int((b-i*A) % 10000))
        elif (int((b-i*A)%10000==0)):
            s = "―$$수식$$%d$$/수식$$조" % (int((b-i*A) / 10000))
        else:
            s = "―$$수식$$%d$$/수식$$조 $$수식$$%d$$/수식$$억" % (int((b-i*A) / 10000), int((b-i*A) % 10000))

        if(i==N):
            C = s.replace("―","")

        a1 = a1 + s

    stem = stem.format(A=A, B=B, N=N)
    answer = answer.format(C=C)
    comment = comment.format(A=A, B=B, C=C, a1=a1, N=N)

    return stem, answer, comment







#4-1-1-69
def bignum411_Stem_058():
    stem = "어떤 수 ■에서 $$수식$${A}$$/수식$$만씩 커지게 뛰어 세어야 할 것을 잘못하여 $$수식$${B}$$/수식$$만씩 커지게 뛰었더니 $$수식$${C}$$/수식$$만이 되었습니다. 바르게 뛰어 세면 얼마인가요?\n$$수식$${boxone}$$/수식$$―$$수식$${boxtwo}$$/수식$$―$$수식$${boxtwo}$$/수식$$―$$수식$${boxfour}$$/수식$$\n"
    answer = "(정답)\n$$수식$${DA3}$$/수식$$만\n"
    comment = "(해설)\n"\
              "$$수식$${B}$$/수식$$만씩 $$수식$$3$$/수식$$번 뛰어 세어 $$수식$${C}$$/수식$$만이 되었으므로 "\
              "$$수식$${C}$$/수식$$만에서 $$수식$${B}$$/수식$$만씩 거꾸로 $$수식$$3$$/수식$$번 뛰어 센 수가 ■입니다.\n"\
              "$$수식$${C}$$/수식$$만―$$수식$${CB}$$/수식$$만―$$수식$${CB2}$$/수식$$만―$$수식$${CB3}$$/수식$$만이므로 "\
              "■ $$수식$$` = ` {D}$$/수식$$만이고 바르게 뛰어 세면 $$수식$${D}$$/수식$$만―$$수식$${DA}$$/수식$$만―"\
              "$$수식$${DA2}$$/수식$$만―$$수식$${DA3}$$/수식$$만입니다.\n\n"


    while True:
        A = np.random.randint(2, 100)
        B = np.random.randint(2, 200)
        if(A != B):
            break

    C = np.random.randint(601, 10000)

    D = C - 3*B
    CB = C-B
    CB2= C-2*B
    CB3 = C-3*B

    DA = D+A
    DA2 = D+2*A
    DA3 = D+3*A

    boxone = "■"
    boxtwo = "[````````````````````]"
    boxfour ="%d만" % (C)

    stem = stem.format(A=A, B=B, C=C, boxone=boxone, boxtwo=boxtwo, boxfour=boxfour)
    answer = answer.format(DA3=DA3)
    comment = comment.format(B=B, C=C, CB=CB, CB2=CB2, CB3=CB3, D=D, DA=DA, DA2=DA2, DA3=DA3)

    return stem, answer, comment








#4-1-1-70
def bignum411_Stem_059():
    stem = "두 수의 크기를 비교하여 □안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$ 를 알맞게 써넣으세요.\n$$표$$ $$수식$${A}$$/수식$${T} $$수식$${B}$$/수식$${S} □ $$수식$${C}$$/수식$${T} $$수식$${D}$$/수식$${S}$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
              "$$수식$${A}$$/수식$${T} $$수식$${B}$$/수식$${S} $$수식$${a1}$$/수식$$ $$수식$${C}$$/수식$${T} $$수식$${D}$$/수식$${S}\n"\
              "$$수식$${A}$$/수식$$는 {K} 자리 수이고 $$수식$${C}$$/수식$$는 {M} 자리 수\n\n"


    while True:
        ts = random.sample([0, 1, 2], 2)
        t = ts[0]
        s = ts[1]
        if(t > s):
            break

    TS = ["만","억","조"]
    T = TS[t]
    S = TS[s]

    B = np.random.randint(1, 10000)
    D = np.random.randint(1, 10000)

    while True:
        A = np.random.randint(1, 10000)
        C = np.random.randint(1, 10000)
        k = len(str(A))
        m = len(str(C))
        if(k != m):
            break

    num = {1:"한", 2:"두", 3:"세", 4:"네"}
    K = num[k]
    M = num[m]

    if (k > m):
        a1 = "&gt;"
    elif (k < m):
        a1 = "&lt;"
    elif (k == m):
        if(A == C and B == D):
            a1= "="

    stem = stem.format(A=A, T=T, B=B, S=S, C=C, D=D)
    answer = answer.format(a1=a1)
    comment = comment.format(A=A, T=T, B=B, S=S, C=C, D=D, K=K, M=M, a1=a1)

    return stem, answer, comment










#4-1-1-71
def bignum411_Stem_060():
    stem = "두 수의 크기를 비교하여 □안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$ 를 알맞게 써넣으세요.\n$$표$$$$수식$${A}$$/수식$$조 $$수식$${b}{c}{d}{e}$$/수식$$억 □ $$수식$${A}$$/수식$$조 $$수식$${f}{g}{h}{i}$$/수식$$억$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
              "$$수식$${A}$$/수식$$조 $$수식$${b}{c}{d}{e}$$/수식$$억 " \
              "$$수식$${a1}$$/수식$$ $$수식$${A}$$/수식$$조 {f}{g}{h}{i}$$/수식$$억\n"\
              "{m}에 해당하는 숫자: $$수식$${M} {a1} {N}$$/수식$$\n\n"


    A = np.random.randint(1, 10000)
    num = [0,0,0,0,0,0,0,0]

    for i in range(8):
        num[i] = np.random.randint(0,10)

    B,C,D,E,F,G,H,I =num[0],num[1],num[2],num[3],num[4],num[5],num[6],num[7]
    if(B==0):
        b=""
        if(C==0):
            c = ""
            if(D==0):
                d = ""
                if(E==0):
                    e=""
                else:
                    e = "$$수식$$%d$$/수식$$" %E
            else:
                d ="$$수식$$%d$$/수식$$" %D
                e = "$$수식$$%d$$/수식$$" % E
        else:
            c = "$$수식$$%d$$/수식$$" %C
            d = "$$수식$$%d$$/수식$$" % D
            e = "$$수식$$%d$$/수식$$" % E
    else:
        b = "$$수식$$%d$$/수식$$" %B
        c = "$$수식$$%d$$/수식$$" % C
        d = "$$수식$$%d$$/수식$$" % D
        e = "$$수식$$%d$$/수식$$" % E


    if(F==0):
        f=""
        if(G==0):
            g = ""
            if(H==0):
                h = ""
                if(I==0):
                    i =""
                else:
                    i  = "$$수식$$%d$$/수식$$" %I
            else:
                h ="$$수식$$%d$$/수식$$" %H
                i = "$$수식$$%d$$/수식$$" % I

        else:
            g = "$$수식$$%d$$/수식$$" %G
            h = "$$수식$$%d$$/수식$$" % H
            i = "$$수식$$%d$$/수식$$" % I
    else:
        f = "$$수식$$%d$$/수식$$" %F
        g = "$$수식$$%d$$/수식$$" % G
        h = "$$수식$$%d$$/수식$$" % H
        i = "$$수식$$%d$$/수식$$" % I

    if(B==F):
        if(C==G):
            if(D==H):
                if(E==I):
                    M = E
                    N = I
                    m = "억"
                    a1 = "="
                elif(E>I):
                    M = E
                    N = I
                    m = "억"
                    a1 = "&gt;"
                else:
                    M = E
                    N = I
                    m = "억"
                    a1 = "&lt;"
            elif(D>H):
                M = D
                N = H
                m = "십억"
                a1=  "&gt;"
            else:
                M = D
                N = H
                m = "십억"
                a1= "&lt;"
        elif(C>G):
            M = C
            N = G
            m = "백억"
            a1 = "&gt;"
        else:
            M = C
            N = G
            m = "백억"
            a1= "&lt;"
    elif(B>F):
        M = B
        N = F
        m = "천억"
        a1 = "&gt;"
    else:
        M = B
        N = F
        m = "천억"
        a1 = "&lt;"

    stem = stem.format(A=A,b=b,c=c,d=d,e=e,f=f,g=g,h=h,i=i)
    answer = answer.format(a1=a1)
    comment = comment.format(A=A,b=b,c=c,d=d,e=e,f=f,g=g,h=h,i=i,M=M,N=N,a1=a1,m=m)

    return stem, answer, comment









#4-1-1-72
def bignum411_Stem_061():
    stem = "두 수 중 더 작은 수를 써 보세요.\n$$수식$${boxone}$$/수식$$ $$수식$${boxtwo}$$/수식$$\n"
    answer = "(정답)\n$$수식$${C}$$/수식$$\n"
    comment = "(해설)\n"\
              "$$수식$${A} {a1} {B}$$/수식$$\n"\
              "$$수식$${M}$$/수식$$자리 수      $$수식$${N}$$/수식$$자리 수\n\n"

    while True:
        A = np.int64(random.randint(10000000, 9999999999))
        B = np.int64(random.randint(10000000, 9999999999))

        M = len(str(A))
        N = len(str(B))

        if(M != N):
            break

    C = min(A, B)

    if (M > N):
        a1 = "&gt;"
    else:
        a1 = "&lt;"

    boxone = "box{%d}" % (A)
    boxtwo = "box{%d}" % (B)

    stem = stem.format(boxone=boxone, boxtwo = boxtwo)
    answer = answer.format(C=C)
    comment = comment.format(A=A, B=B, M=M, N=N, a1=a1)

    return stem, answer, comment







#4-1-1-74
def bignum411_Stem_062():
    stem = "큰 수부터 차례대로 기호를 써 보세요.\n$$표$$ {boxone} $$/표$$"
    answer = "(정답)\n{T}\n"
    comment = "(해설)\n"\
              "㉠ $$수식$${M}$$/수식$$자리 수, ㉡ $$수식$${N}$$/수식$$자리 수, ㉢ $$수식$${O}$$/수식$$자리 수\n"\
              "따라서 자릿수가 많은 쪽이 크므로 큰 수부터 차례대로 쓰면 {T}입니다.\n\n"


    while True:
        A = np.int64(random.randint(10000000, 999999999999))
        B = np.int64(random.randint(10000000, 999999999999))
        C = np.int64(random.randint(10000000, 999999999999))

        M = len(str(A))
        N = len(str(B))
        O = len(str(C))

        if(M != N and N != O and M != O):
            break

    mno = [M, N, O]
    mno.sort(reverse=True)

    if(mno[0]==M and mno[1]==N and mno[2]==O):
        T = "㉠, ㉡, ㉢"
    elif(mno[0]==M and mno[1]==O and mno[2]==N):
        T = "㉠, ㉢, ㉡"
    elif(mno[0]==N and mno[1]==M and mno[2]==O):
        T = "㉡, ㉠, ㉢"
    elif (mno[0] == N and mno[1] == O and mno[2] == M):
        T = "㉡, ㉢, ㉠"
    elif(mno[0]==O and mno[1]==M and mno[2]==N):
        T = "㉢, ㉠, ㉡"
    elif (mno[0] == O and mno[1] == N and mno[2] == M):
        T = "㉢, ㉡, ㉠"

    boxone = "㉠$$수식$$%d$$/수식$$\n ㉡$$수식$$%d$$/수식$$\n  ㉢$$수식$$%d$$/수식$$" % (A, B, C)

    stem = stem.format(boxone=boxone)
    answer = answer.format(T=T)
    comment = comment.format(M=M, N=N, O=O, T=T)

    return stem, answer, comment










#4-1-1-75
def bignum411_Stem_063():
    stem = "$$수식$$0$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 중에서 □ 안에 들어갈 수 있는 수를 모두 써 보세요.\n$$표$${boxone}$$/표$$\n"
    answer = "(정답)\n$$수식$${T}$$/수식$$\n"
    comment = "(해설)\n"\
              "두 수의 자릿수가 같으므로 가장 높은 자리의 수부터 비교하면 십만, 만의 자리 수가 같습니다.\n"\
              "따라서 백의 자리 숫자를 비교하면 $$수식$${D} ` &gt; ` {I}$$/수식$$ 이므로 □ $$수식$$&lt; ` {H}$$/수식$$"\
              "  에서 □ 안에는 {T}{j1} 들어갈 수 있습니다.\n\n"

    while True:
        A = np.random.randint(1, 10)
        B = np.random.randint(1, 10)
        D = np.random.randint(1, 10)

        E = np.random.randint(1, 10)
        F = np.random.randint(1, 10)
        H = np.random.randint(1, 10)

        I = np.random.randint(1, 10)
        J = np.random.randint(1, 10)
        K = np.random.randint(1, 10)

        if (D > I):
            break

    T = ""
    temp = ""

    for i in range(0, H):
        if (i == 0):
            T = "$$수식$$%d$$/수식$$" % (i)
            temp = str(i)
        else:
            s = "$$수식$$%d$$/수식$$" % (i)
            T = T + ", " +s
            temp = temp + str(i)

    if temp[-1] == "2" or temp[-1] == "4" or temp[-1] == "5" or temp[-1] == "9":
        j1 = "가"
    else:
        j1 = "이"

    boxone = "$$수식$$%d%d□%d%d%d&lt;%d%d%d%d%d%d$$/수식$$" % (A, B, D, E, F, A, B, H, I, J, K)

    stem = stem.format(boxone=boxone)
    answer = answer.format(T=T)
    comment = comment.format(D=D, I=I, H=H, T=T, j1=j1)

    return stem, answer, comment











#4-1-1-76
def bignum411_Stem_064():
    stem = "{T} 피해를 입은 사람들을 돕기 위해 {A} 기업은 $$수식$${B}$$/수식$$원을, {C} 기업은 $$수식$${D}$$/수식$$원을 기부하였습니다. 어느 기업이 더 많이 기부하였나요?\n"
    answer = "(정답)\n{S} 기업\n"
    comment = "(해설)\n"\
              "$$수식$${B}$$/수식$$은 $$수식$${E}$$/수식$$자리 수이고, $$수식$${D}$$/수식$$은 $$수식$${F}$$/수식$$자리 수입니다."\
              "\n자릿수가 많은 쪽이 더 큰 수 이므로\n$$수식$${H} ` &gt; ` {I}$$/수식$$ 입니다.\n"\
              "따라서 {S} 기업이 더 많이 기부하였습니다.\n\n"


    T = random.choice(["태풍", "가뭄", "홍수", "지진"])
    ac = random.sample(["햇님", "달님", "별님", "청솔", "한국", "소리"],2)

    A,C = ac[0],ac[1]

    while True:
        B = np.int64(random.randint(10000000, 99999999999999))
        D = np.int64(random.randint(10000000, 99999999999999))

        E = len(str(B))
        F = len(str(D))

        if (abs(E - F) == 1):
            break

    H = max(B, D)
    I = min(B, D)

    if (H == B):
        S = A
    else:
        S = C

    stem = stem.format(A=A, B=B, C=C ,D=D, T=T)
    answer = answer.format(S=S)
    comment = comment.format(B=B, E=E, F=F, H=H, I=I, S=S, D=D)

    return stem, answer, comment








#4-1-1-78
def bignum411_Stem_065():
    stem = "□ 안에는 $$수식$$0$$/수식$$부터 $$수식$$9$$/수식$$까지의 숫자가 들어갈 수 있는 수들이 있습니다. 큰 수부터 차례대로 기호를 써 보세요\n$$표$$㉠ $$수식$${a}$$/수식$$\n㉡ $$수식$${b}$$/수식$$\n㉢ $$수식$${c}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{t1}, {t2}, {t3}\n"
    comment = "(해설)\n"\
              "세 수의 자릿수가 모두 같으므로 □ 안에 $$수식$$9$$/수식$$를 넣은 후"\
              " 앞 자리 수부터 차례대로 수의 크기를 비교합니다.\n"\
              "㉠ $$수식$${A1}$$/수식$$\n㉡ $$수식$${B1}$$/수식$$\n㉢ $$수식$${C1}$$/수식$$\n"\
              "따라서 {t1} $$수식$$&gt;$$/수식$$ {t2} $$수식$$&gt;$$/수식$$ {t3}입니다.\n\n"


    five = np.random.randint(10000, 99999)
    fv = str(five)

    aa = fv
    bb = fv
    cc = fv

    l = np.random.randint(7,12)

    for i in range(l):
        l1 = np.random.randint(0,10)
        aa = aa + str(l1)
        l2 = np.random.randint(0,10)
        bb = bb + str(l2)
        l3 = np.random.randint(0,10)
        cc = cc + str(l3)

    aaa = list(aa)
    bbb = list(bb)
    ccc = list(cc)

    x = random.sample([2,3,4,5,6,7,8,9],3)

    x1,x2,x3 = x[0],x[1],x[2]

    aaa[x1] = "□"
    bbb[x2] = "□"
    ccc[x3] = "□"

    a = "".join(aaa)
    b = "".join(bbb)
    c = "".join(ccc)

    aaa[x1] = "9"
    bbb[x2] = "9"
    ccc[x3] = "9"

    a1 = "".join(aaa)
    b1 = "".join(bbb)
    c1 = "".join(ccc)

    A1 = int(a1)
    B1 = int(b1)
    C1 = int(c1)
    ABC = [A1,B1,C1]
    ABC.sort(reverse=True)

    if(ABC[0]==A1):
        t1 = "㉠"
        if(ABC[1]==B1):
            t2 = "㉡"
            t3 = "㉢"
        else:
            t2 = "㉢"
            t3 = "㉡"

    elif(ABC[0]==B1):
        t1 = "㉡"
        if(ABC[1]==A1):
            t2 = "㉠"
            t3 = "㉢"
        else:
            t2 = "㉢"
            t3 = "㉠"

    elif(ABC[0]==C1):
        t1 = "㉢"
        if(ABC[1]==A1):
            t2 = "㉠"
            t3 = "㉡"
        else:
            t2 = "㉡"
            t3 = "㉠"

    stem = stem.format(a=a, b=b, c=c)
    answer = answer.format(t1=t1, t2=t2, t3=t3)
    comment = comment.format(A1=A1, B1=B1, C1=C1, t1=t1, t2=t2, t3=t3)

    return stem, answer, comment














#4-1-1-79
def bignum411_Stem_066():
    stem = "$$수식$${M}$$/수식$$부터 $$수식$${N}$$/수식$$까지의 수를 모두 두 번씩 사용하여 {T}의 자리 숫자가 $$수식$${a}$$/수식$$이고 {S}의 자리 숫자가 $$수식$${b}$$/수식$$인 수를 만들려고 합니다. 만들 수 있는 가장 큰 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${C}$$/수식$$\n"
    comment = "(해설)\n"\
              "{T}의 자리 숫자가 $$수식$${a}$$/수식$$이고 {S}의 자리 숫자가 $$수식$${b}$$/수식$$인 $$수식$$16$$/수식$$자리 수는\n" \
              "{sqr_str}입니다.\n" \
              "가장 큰 수는 높은 자리부터 큰 수를 차례대로 놓으면 되므로 $$수식$${C}$$/수식$$ 입니다.\n\n"


    while True:
        while True:
            M = random.choice([0, 1, 2])
            N = M + 7

            a = np.random.randint(M, N + 1)
            b = np.random.randint(M, N + 1)

            if a != b:
                break

        T = ["백조", "조", "천억", "백억", "십억"][np.random.randint(0, 5)]
        S = ["억", "천만", "백만", "십만", "만"][np.random.randint(0, 5)]

        A, B = str(a), str(b)
        number = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
        sqr = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]

        if T == "백조":
            number[1] = A
            sqr[1] = "$$수식$$%s$$/수식$$" % A
        elif T == "조":
            number[3] = A
            sqr[3] = "$$수식$$%s$$/수식$$" % A
        elif T == "천억":
            number[4] = A
            sqr[4] = "$$수식$$%s$$/수식$$" % A
        elif T == "백억":
            number[5] = A
            sqr[5] = "$$수식$$%s$$/수식$$" % A
        elif T == "십억":
            number[6] = A
            sqr[6] = "$$수식$$%s$$/수식$$" % A

        if S == "억":
            number[7] = B
            sqr[7] = "$$수식$$%s$$/수식$$" % B
        elif S == "천만":
            number[8] = B
            sqr[8] = "$$수식$$%s$$/수식$$" % B
        elif S == "백만":
            number[9] = B
            sqr[9] = "$$수식$$%s$$/수식$$" % B
        elif S == "십만":
            number[10] = B
            sqr[10] = "$$수식$$%s$$/수식$$" % B
        elif S == "만":
            number[11] = B
            sqr[11] = "$$수식$$%s$$/수식$$" % B

        num = "".join(number)
        num = num.replace("0", "□")

        sqr_str = "".join(sqr)
        sqr_str = sqr_str.replace("0", "□")

        temp_list = list(num)
        sqr_list = list(sqr_str)

        if (temp_list.count("□") == 14) and (sqr_list.count("□") == 14):
            break

    sample = []

    for i in range(N - M + 1):
        sample.append(M + i)
        sample.append(M + i)

    sample.sort(reverse=True)
    sample.remove(a)
    sample.remove(b)


    sdx = 0
    for idx in range(16):
        if temp_list[idx] == "□":
            temp_list[idx] = str(sample[sdx])
            sdx += 1

    C = "".join(temp_list)


    stem = stem.format(M=M, N=N, T=T, a=a, S=S, b=b)
    answer = answer.format(C=C)
    comment = comment.format(T=T, a=a, S=S, b=b, C=C, sqr_str=sqr_str)

    return stem, answer, comment











# 4-1-1-80
def bignum411_Stem_067():
    stem = "$$수식$$0$$/수식$$부터 $$수식$$9$$/수식$$까지의 수를 한 번씩 사용하여 만들 수 있는 {T}의 자리 숫자가 $$수식$${A}$$/수식$$인 여덟 자리 수 중에서 가장 큰 수와 가장 작은 수를 차례대로 써 보세요.\n"
    answer = "(정답)\n$$수식$${C}$$/수식$$, $$수식$${D}$$/수식$$\n"
    comment = "(해설)\n" \
              "{T}의 자리 숫자가 $$수식$${A}$$/수식$$인 여덟 자리 숫자는 {num}입니다.\n" \
              "따라서 가장 큰 여덟 자리 수는 $$수식$${C}$$/수식$$이고 가장 작은 여덟 자리 수는 " \
              "$$수식$${D}$$/수식$$입니다.\n\n"


    T = random.choice(["만", "십만", "백만"])

    A = np.random.randint(0, 9)

    # a = str(A)

    number = ["0", "0", "0", "0", "0", "0", "0", "0"]

    if T == "만":
        number[3] = "*"
    elif T == "십만":
        number[2] = "*"
    elif T == "백만":
        number[1] = "*"

    num = "".join(number)
    num = num.replace("0", "□")
    num = num.replace("*", str(A))

    sampled = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sampled.remove(A)
    samplec = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    samplec.remove(A)
    samplec.sort(reverse=True)
    # number = list(map(int, number))

    numberc = [0, 0, 0, 0, 0, 0, 0, 0]
    numberd = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(8):
        if (number[i] == "0"):
            numberc[i] = samplec[0]
            samplec.remove(numberc[i])
            if (i == 0 and sampled[0] == 0):
                numberd[i] = sampled[1]
                sampled.remove(numberd[i])
            else:
                numberd[i] = sampled[0]
                sampled.remove(numberd[i])
        else:
            numberc[i] = A
            numberd[i] = A

    numberc = list(map(str, numberc))
    C1 = "".join(numberc)
    C = int(C1)

    numberd = list(map(str, numberd))
    D1 = "".join(numberd)
    D = int(D1)

    stem = stem.format(T=T, A=A)
    answer = answer.format(C=C, D=D)
    comment = comment.format(T=T, A=A, num=num, C=C, D=D)

    return stem, answer, comment





