import fractions
import numpy as np
import math
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



def soroso(a, b):
    while True:
        rest_ab = max(a, b) % min(a, b)
        a = min(a, b)
        b = rest_ab
        if rest_ab == 0 or rest_ab == 1:
            break
    return rest_ab





#6-1-4-01
def ratandpro614_Stem_001():
    stem = "체육관에 {A}이 $$수식$${C}$$/수식$$개, {B}이 $$수식$${D}$$/수식$$개 있습니다. 두 수를 바르게 비교한 것을 찾아 기호를 써 보세요.\n$$표$$㉠ {aa}\n㉡ {bb}\n㉢ {cc}\n㉣ {dd}$$/표$$\n"
    answer = "(정답)\n$$수식$${I}$$/수식$$\n"
    comment = "(해설)\n" \
              "{X} {a1}\n" \
              "{Y} {b1}\n" \
              "{Z} {c1}\n\n"


    N = ["축구공", "야구공", "농구공", "배구공", "테니스공"]

    while 1:
        N2 = np.random.choice(N, 2)
        A, B = N2
        if A != B:
            break

    while (1):
        C = np.random.randint(10,100)
        D = np.random.randint(2,10)
        E = C-D
        F = np.math.floor(C/D)
        J = np.random.randint(2,50)

        G = "1 over {%s}" % (J)
        H1 = np.math.floor(C/D)
        H = "1 over {%s}" % (H1)
        if C % D == 0:
            if G != H:
                break



    aa = "%s은 %s 보다 $$수식$$%s$$/수식$$개 더 적습니다." % (A,B,E)
    bb = "%s은 %s 보다 $$수식$$%s$$/수식$$개 더 많습니다." % (B,A,E)

    cc = "%s 수는 %s 수의 $$수식$$%s$$/수식$$배입니다." % (A,B,F)
    dd = "%s 수는 %s 수의 $$수식$$%s$$/수식$$배입니다." % (B,A,G)

    aaa = aa
    bbb = bb

    ccc = cc
    # ddd = dd

    NN = [aa,bb,cc,dd]
    np.random.shuffle(NN)
    aa, bb, cc, dd = NN

    for i in NN:
        if(i == ccc and i == aa):
            I = "㉠"
            NN.remove(aa)
            break
        if (i == ccc and i == bb):
            NN.remove(bb)
            I = "㉡"
            break
        if (i == ccc and i == cc):
            NN.remove(cc)
            I = "㉢"
            break
        if (i == ccc and i == dd):
            NN.remove(dd)
            I = "㉣"
            break

    a1, b1, c1= NN

    if a1 == aaa:
        a1 = "%s은 %s 보다 $$수식$$%s ` - ` %s ` = ` %s$$/수식$$개 더 많습니다." % (A, B, C, D, E)
    elif a1 == bbb:
        a1 = "%s은 %s 보다 $$수식$$%s ` - ` %s ` = ` %s$$/수식$$개 더 적습니다." % (B, A, C, D, E)
    else:
        a1 = "%s 수는 %s 수의 $$수식$$%s DIV %s ` = ` %s ` LEFT ($$/수식$$배$$수식$$RIGHT )$$/수식$$입니다." % (B, A, D, C, H)

    if (b1 == aaa):
        b1 = "%s은 %s 보다 $$수식$$%s ` - ` %s ` = ` %s$$/수식$$개 더 많습니다." % (A, B, C, D, E)
    elif (b1 == bbb):
        b1 = "%s은 %s 보다 $$수식$$%s ` - ` %s ` = ` %s$$/수식$$개 더 적습니다." % (B, A, C, D, E)
    else:
        b1 = "%s 수는 %s 수의 $$수식$$%s DIV %s ` = ` %s ` LEFT ($$/수식$$배$$수식$$RIGHT )$$/수식$$입니다." % (B, A, D, C, H)

    if (c1 == aaa):
        c1 = "%s은 %s 보다 $$수식$$%s ` - ` %s ` = ` %s$$/수식$$개 더 많습니다." % (A, B, C, D, E)
    elif (c1 == bbb):
        c1 = "%s은 %s 보다 $$수식$$%s ` - ` %s ` = ` %s$$/수식$$개 더 적습니다." % (B, A, C, D, E)
    else:
        c1 = "%s 수는 %s 수의 $$수식$$%s DIV %s ` = ` %s ` LEFT ($$/수식$$배$$수식$$RIGHT )$$/수식$$입니다." % (B, A, D, C, H)

    XX = ["㉠", "㉡", "㉢", "㉣"]
    XX.remove(I)
    X,Y,Z = XX

    stem = stem.format(A=A,B=B,C=C,D=D,aa=aa,bb=bb,cc=cc,dd=dd)
    answer = answer.format(I=I)
    comment = comment.format(X=X,Y=Y,Z=Z,a1=a1,b1=b1,c1=c1)

    return stem, answer, comment















#6-1-4-03
def ratandpro614_Stem_002():
    stem = "{A}네 반 학생은 $$수식$${B}$$/수식$$명이고, 학교에서 각 반에 어린이날 선물로 준 {C}은 $$수식$${D}$$/수식$$개입니다. 학생 수와 {C} 수를 나눗셈으로 비교하려고 합니다. □ 안에 알맞은 수를 써 넣으세요.\n$$표$$$$수식$${D} DIV {B} ` = ` $$/수식$$□\n{C} 수는 학생 수의 □배입니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${E}$$/수식$$\n"
    comment = "(해설)\n" \
              "{C} 수는 학생 수의 $$수식$${D} DIV {B} ` = ` {E} ` LEFT ($$/수식$$배$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    while(1):
        A = ["민지","승하","주희","현수","동아"][np.random.randint(0,5)]
        B = np.random.randint(11,100)

        C = ["공책","볼펜","연필","수첩","필통"][np.random.randint(0,5)]
        D = np.random.randint(100,1000)

        E = np.math.floor(D/B)
        if D % B == 0:
            break


    stem = stem.format(A=A,B=B,C=C,D=D)
    answer = answer.format(E=E)
    comment = comment.format(D=D,B=B,E=E,C=C)

    return stem, answer, comment











#6-1-4-06
def ratandpro614_Stem_003():
    stem = "어느 종합 병원 여자 의사가 $$수식$${A}$$/수식$$명, 남자 의사가 $$수식$${B}$$/수식$$명입니다. 여자 의사 수와 남자 의사 수를 비교한 것입니다. 차례대로 알맞은 수를 쓰세요.\n$$수식$$LEFT [$$/수식$$뺄셈으로 비교하기$$수식$$RIGHT ]$$/수식$$\n$$수식$${B} ` - ` {A} ` = ` $$/수식$$ $$수식$${box1}$$/수식$$\n여자 의사는 남자 의사보다 $$수식$${box2}$$/수식$$명 더 적습니다.\n$$수식$$LEFT [$$/수식$$나눗셈으로 비교하기$$수식$$RIGHT ]$$/수식$$\n$$수식$${A} DIV {B} ` = ` {box3} over {box4}$$/수식$$\n여자 의사는 남자 의사의 $$수식$${box5} over {box6}$$/수식$$배입니다.\n"
    answer = "(정답)\n$$수식$${C}$$/수식$$, $$수식$${C}$$/수식$$, $$수식$${D}$$/수식$$, $$수식$${E}$$/수식$$, $$수식$${D}$$/수식$$, $$수식$${E}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT [$$/수식$$뺄셈으로 비교하기$$수식$$RIGHT ]$$/수식$$\n" \
              "여자 의사는 남자 의사보다 $$수식$${B} ` - ` {A} ` = ` {C} ` LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$ 더 적습니다.\n" \
              "$$수식$$LEFT [$$/수식$$나눗셈으로 비교하기$$수식$$RIGHT ]$$/수식$$\n" \
              "여자 의사는 남자 의사의 $$수식$${A} DIV {B} ` = ` {D} over {E} ` LEFT ($$/수식$$배$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    while(1):
        A = np.random.randint(10, 20)
        B = np.random.randint(A + 1, 100)

        C = B - A
        F = fractions.Fraction(A, B)
        D = F.numerator
        E = F.denominator

        if(B % A ==0):
            break

    box1 = "%s" % "①"
    box2 = "%s" % "②"
    box3 = "%s" % "③"

    box4 = "%s" % "④"
    box5 = "%s" % "⑤"
    box6 = "%s" % "⑥"

    stem = stem.format(A=A, B=B, box1=box1, box2=box2, box3=box3, box4=box4, box5=box5, box6=box6)
    answer = answer.format(C=C, D=D, E=E)
    comment = comment.format(D=D, B=B, E=E, C=C, A=A)

    return stem, answer, comment













#6-1-4-10
def ratandpro614_Stem_004():
    stem = "다음은 비에 대한 설명입니다. 틀린 것을 찾아 기호를 써 보세요.\n$$표$$㉠ {a}\n㉡ {b}\n㉢ {c}$$/표$$\n"
    answer = "(정답)\n{G}\n"
    comment = "(해설)\n" \
              "{G} $$수식$${C}$$/수식$$대 $$수식$${D}$$/수식$${j2} $$수식$${C}$$/수식$$:$$수식$${D}$$/수식$$입니다.$$/수식$$\n\n"


    while 1:
        A = np.random.randint(2, 10)
        B = np.random.randint(2, 10)

        if A != B and soroso(A, B):
            break

    while 1:
        C = np.random.randint(2, 10)
        D = np.random.randint(2, 10)

        if C != D and soroso(C, D):
            break

    while 1:
        E = np.random.randint(2, 10)
        F = np.random.randint(2, 10)

        if E != F and soroso(E, F):
            break


    j1 = proc_jo(E, 2)

    j2 = proc_jo(D, -1)

    a = "$$수식$$%s$$/수식$$에 대한 $$수식$$%s$$/수식$$의 비는 $$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$입니다." % (A, B, B, A)
    b = "$$수식$$%s$$/수식$$대 $$수식$$%s$$/수식$$%s $$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$입니다." % (C, D, j2, D, C)
    c = "$$수식$$%s$$/수식$$%s $$수식$$%s$$/수식$$의 비는 $$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$입니다." % (E, j1, F, E, F)

    # aa = a
    bb = b
    # cc = c

    NN = [a, b, c]
    np.random.shuffle(NN)
    a, b, c = NN

    for i in NN:
        if (i == bb and i == a):
            G = "㉠"
            break
        if (i == bb and i == b):
            G = "㉡"
            break
        if (i == bb and i == c):
            G = "㉢"
            break


    stem = stem.format(a=a, b=b, c=c)
    answer = answer.format(G=G)
    comment = comment.format(C=C, D=D, G=G, j2=j2)

    return stem, answer, comment













#6-1-4-11
def ratandpro614_Stem_005():
    stem = "$$수식$${A}$$/수식$$:$$수식$${B}$$/수식$${j1} 바르게 읽은 사람은 누구인가요?\n$$표$${aa}\n{bb}$$/표$$\n"
    answer = "(정답)\n{D}\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$:$$수식$${B}$$/수식$$ → $$수식$${B}$$/수식$$에 대한 $$수식$${A}$$/수식$$의 비, $$수식$${A}$$/수식$$의 $$수식$${B}$$/수식$$에 대한 비\n\n"


    N = ["남식", "동현", "성일", "수원", "재홍", "기철", "용석", "대희", "도윤", "영래", "종국"]

    while 1:
        A = np.random.randint(2, 10)
        B = np.random.randint(2, 10)

        N2 = np.random.choice(N, 2)

        C, D = N2

        if A != B and C != D and soroso(A, B):
            break


    choice = np.random.randint(0, 2)

    if choice == 0:
        aa = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ $$수식$$%d$$/수식$$에 대한 $$수식$$%d$$/수식$$의 비" % (C, A, B)
        bb = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ $$수식$$%d$$/수식$$에 대한 $$수식$$%d$$/수식$$의 비" % (D, B, A)
    else:
        aa = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ $$수식$$%d$$/수식$$에 대한 $$수식$$%d$$/수식$$의 비" % (D, B, A)
        bb = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ $$수식$$%d$$/수식$$에 대한 $$수식$$%d$$/수식$$의 비" % (C, A, B)

    j1 = proc_jo(B, 1)

    stem = stem.format(A=A, B=B, j1=j1, aa=aa, bb=bb)
    answer = answer.format(D=D)
    comment = comment.format(B=B, A=A)

    return stem, answer, comment
















#6-1-4-16
def ratandpro614_Stem_006():
    stem = "꽃병에 {A} $$수식$${C}$$/수식$$송이, {B} $$수식$${D}$$/수식$$송이가 꽂혀 있습니다. 전체 꽃 수에 대한 {B} 수의 비를 써 보세요.\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$:$$수식$${E}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$전체 꽃 수$$수식$$RIGHT ) `` = `` {C} ` + ` {D} ` = ` {E} ` LEFT ($$/수식$$송이$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 $$수식$$LEFT ($$/수식$${B} 수$$수식$$RIGHT ) ``$$/수식$$:$$수식$$`` LEFT ($$/수식$$전체 꽃 수$$수식$$RIGHT ) ` = ` {D} `$$/수식$$:$$수식$$` {E}$$/수식$$입니다.\n\n"


    N = ["장미꽃", "나팔꽃", "국화꽃", "매화꽃", "동백꽃"]

    while 1:
        C = np.random.randint(2, 50)
        D = np.random.randint(2, 50)

        N2 = np.random.choice(N, 2)
        A, B = N2
        E = C + D

        if A != B and C != D and soroso(D, E):
            break


    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(D=D, E=E)
    comment = comment.format(B=B, C=C, D=D, E=E)

    return stem, answer, comment














#6-1-4-17
def ratandpro614_Stem_007():
    stem = "{A}가 비에 대해 이야기 한 것이 틀립니다. 그 이유를 찾아 기호를 써 보세요.\n$$표$$$$수식$$LEFT [$$/수식$${A}$$수식$$RIGHT ]$$/수식$$ $$수식$${C}$$/수식$$:$$수식$${D}$$/수식$${j1} $$수식$${D}$$/수식$$:$$수식$${C}$$/수식$${j2} 같아.$$/표$$\n$$표$$ ㉠ {a}\n㉡ {b}$$/표$$\n"
    answer = "(정답)\n{B}\n"
    comment = "(해설)\n" \
              "$$수식$${C}$$/수식$$:$$수식$${D}$$/수식$${j1} $$수식$${D}$$/수식$$:$$수식$${C}$$/수식$${j2} 다릅니다.\n" \
              "두 비는 기준이 되는 수가 서로 다릅니다.\n" \
              "즉, $$수식$${C}$$/수식$$:$$수식$${D}$$/수식$${j3} 기준이 $$수식$${D}$$/수식$$이지만, $$수식$${D}$$/수식$$:$$수식$${C}$$/수식$${j2} 기준이 $$수식$${C}$$/수식$$입니다.\n\n"


    A = ["상호", "병우", "승희", "혜교", "남주", "준서", "은아", "민지", "아라", "영미"][np.random.randint(0, 10)]


    while 1:
        C = np.random.randint(2, 10)
        D = np.random.randint(2, 10)

        if C != D and soroso(C, D):
            break

    j1 = proc_jo(D, 2)
    j2 = proc_jo(C, -1)

    j3 = proc_jo(D, -1)

    a = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$%s 기준이 $$수식$$%s$$/수식$$이지만 $$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$%s 기준이 $$수식$$%s$$/수식$$입니다." % (C, D, j3, D, D, C, j2, C)
    b = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$%s 기준이 $$수식$$%s$$/수식$$이지만 $$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$%s 기준이 $$수식$$%s$$/수식$$입니다." % (C, D, j3, C, D, C, j2, D)

    aa = a
    # bb = b

    NN = [a, b]
    np.random.shuffle(NN)
    a, b = NN

    for i in NN:
        if (i == aa and i == a):
            B = "㉠"
            break
        if (i == aa and i == b):
            B = "㉡"
            break



    stem = stem.format(A=A,b=b,a=a,C=C,D=D, j1=j1, j2=j2)
    answer = answer.format(B=B)
    comment = comment.format(C=C,D=D, j1=j1, j2=j2, j3=j3)

    return stem, answer, comment




















#6-1-4-18
def ratandpro614_Stem_008():
    stem = "{A}는 $$수식$${B} rm m$$/수식$$ 달리기를 하고 있습니다. 출발점부터 $$수식$${C} rm m$$/수식$$를 달렸다면 도착점까지 남은 거리에 대한 출발점에서부터 달린 거리의 비를 구해보세요.\n"
    answer = "(정답)\n$$수식$${C}$$/수식$$:$$수식$${D}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$남은 거리$$수식$$RIGHT ) ` = ` {B} ` - ` {C} ` = ` {D} ` LEFT ( ` rm m ` RIGHT )$$/수식$$\n" \
              "도착지까지 남은 거리에 대한 출발점에서부터 달린 거리의 비는 $$수식$${C}$$/수식$$:$$수식$${D}$$/수식$$입니다.\n\n"


    A = ["민수", "수지", "지호", "준수", "나래", "운재", "은배", "한기", "연우", "대희"][np.random.randint(0, 10)]

    while True:
        B = np.random.randint(50, 100)
        C = np.random.randint(10, 50)
        D = B - C

        if soroso(C, D):
            break

    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(C=C, D=D)
    comment = comment.format(B=B, C=C, D=D)

    return stem, answer, comment















#6-1-4-21
def ratandpro614_Stem_009():
    stem = "다음 중 기준량이 비교하는 양보다 작은 것은 어느 것인가요?\n① {a}\n② {b}\n③ {c}\n④ {d}\n⑤ {e}\n"
    answer = "(정답)\n{K}\n"
    comment = "(해설)\n" \
              "{a1}\n" \
              "{b1}\n" \
              "{c1}\n" \
              "{d1}\n" \
              "{e1}\n" \
              "따라서 기준량이 비교하는 양보다 작은 것은 {K}입니다.\n\n"

    while 1:
        A = np.random.randint(2, 10)
        B = np.random.randint(2, 10)

        E = np.random.randint(2, 10)
        F = np.random.randint(2, 10)

        if A < B and E < F and A != E and B != F and soroso(A, B)and soroso(E, F):
            break

    while (1):
        C = np.random.randint(2, 10)
        D = np.random.randint(2, 10)

        if D < C and soroso(C, D):
                break

    while (1):
        G = np.random.randint(2, 10)
        H = np.random.randint(2, 10)

        if G < H and soroso(G, H):
                break

    while (1):
        I = np.random.randint(2, 10)
        J = np.random.randint(2, 10)

        if I < J and soroso(I, J):
                break

    a = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$" % (A, B)
    b = "$$수식$$%s$$/수식$$에 대한 $$수식$$%s$$/수식$$의 비" % (D, C)
    c = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$" % (E, F)
    d = "$$수식$$%s$$/수식$$의 $$수식$$%s$$/수식$$에 대한 비" % (G, H)
    e = "$$수식$$%s$$/수식$$와 $$수식$$%s$$/수식$$의 비" % (I, J)

    aa = a
    bb = b
    cc = c
    dd = d
    # ee = e

    NN = [a, b, c, d, e]
    np.random.shuffle(NN)
    a, b, c, d, e = NN

    for i in NN:
        if(i == bb and i == a):
            K = "①"
            break
        if (i == bb and i == b):
            K = "②"
            break
        if (i == bb and i == c):
            K = "③"
            break
        if (i == bb and i == d):
            K = "④"
            break
        if (i == bb and i == e):
            K = "⑤"
            break

    if(a == aa):
        a1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (A, B, A, B)
    elif(a == bb):
        a1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &gt; `` %s$$/수식$$" % (C, D, C, D)
    elif(a == cc):
        a1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (E, F, E, F)
    elif(a == dd):
        a1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (G, H, G, H)
    else:
        a1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (I, J, I, J)

    if (b == aa):
        b1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (A, B, A, B)
    elif (b == bb):
        b1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &gt; `` %s$$/수식$$" % (C, D, C, D)
    elif (b == cc):
        b1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (E, F, E, F)
    elif (b == dd):
        b1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (G, H, G, H)
    else:
        b1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (I, J, I, J)

    if (c == aa):
        c1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (A, B, A, B)
    elif (c == bb):
        c1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &gt; `` %s$$/수식$$" % (C, D, C, D)
    elif (c == cc):
        c1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (E, F, E, F)
    elif (c == dd):
        c1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (G, H, G, H)
    else:
        c1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (I, J, I, J)

    if (d == aa):
        d1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (A, B, A, B)
    elif (d == bb):
        d1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &gt; `` %s$$/수식$$" % (C, D, C, D)
    elif (d == cc):
        d1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (E, F, E, F)
    elif (d == dd):
        d1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (G, H, G, H)
    else:
        d1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (I, J, I, J)

    if (e == aa):
        e1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (A, B, A, B)
    elif (e == bb):
        e1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &gt; `` %s$$/수식$$" % (C, D, C, D)
    elif (e == cc):
        e1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (E, F, E, F)
    elif (e == dd):
        e1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (G, H, G, H)
    else:
        e1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (I, J, I, J)


    stem = stem.format(a=a, b=b, c=c, d=d, e=e)
    answer = answer.format(K=K)
    comment = comment.format(a1=a1, b1=b1, c1=c1, d1=d1, e1=e1, K=K)

    return stem, answer, comment















#6-1-4-22
def ratandpro614_Stem_010():
    stem = "기준량이 비교하는 양보다 큰 것을 모두 찾아 기호를 써 보세요.\n$$표$$㉠ {a}\n㉡ {b}\n㉢ {c}\n㉣ {d}$$/표$$\n"
    answer = "(정답)\n{I}, {J}\n"
    comment = "(해설)\n" \
              "{a1}\n" \
              "{b1}\n" \
              "{c1}\n" \
              "{d1}\n" \
              "따라서 기준량이 비교하는 양보다 큰 것은 {I}, {J}입니다.\n\n"



    while 1:
        A = np.random.randint(2, 20)
        B = np.random.randint(2, 20)

        if A < B and soroso(A, B):
            break

    while 1:
        C = np.random.randint(2, 20)
        D = np.random.randint(2, 20)

        if C < D and soroso(C, D):
            break

    while 1:
        E = np.random.randint(2, 20)
        F = np.random.randint(2, 20)

        if F < E and soroso(E, F):
            break

    while 1:
        G = np.random.randint(2, 20)
        H = np.random.randint(2, 20)

        if G < H and soroso(G, H):
            break

    a = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$" % (A, B)
    b = "$$수식$$%s$$/수식$$에 대한 $$수식$$%s$$/수식$$의 비" % (C, D)
    c = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$" % (E, F)
    d = "$$수식$$%s$$/수식$$에 대한 $$수식$$%s$$/수식$$의 비" % (H, G)

    aa = a
    bb = b
    cc = c
    dd = d

    NN = [a, b, c, d]
    np.random.shuffle(NN)
    a, b, c, d = NN

    for i in NN:
        if(i == aa and i == a):
            I = "㉠"
            break
        if (i == aa and i == b):
            I = "㉡"
            break
        if (i == aa and i == c):
            I = "㉢"
            break
        if (i == aa and i == d):
            I = "㉣"
            break

    for i in NN:
        if(i == dd and i == a):
            J = "㉠"
            break
        if (i == dd and i == b):
            J = "㉡"
            break
        if (i == dd and i == c):
            J = "㉢"
            break
        if (i == dd and i == d):
            J = "㉣"
            break

    if(I == "㉡" and J == "㉠" or I == "㉢" and J == "㉠" or I == "㉢" and J == "㉡" or I == "㉣" and J == "㉢" or I == "㉣" and J =="㉡" or I == "㉣" and J =="㉠"):
        K = I
        I = J
        J = K



    if(a == aa):
        a1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (A, B, A, B)
    elif(a == bb):
        a1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &gt; `` %s$$/수식$$" % (D, C, D, C)
    elif(a == cc):
        a1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &gt; `` %s$$/수식$$" % (E, F, E, F)
    else:
        a1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (G, H, G, H)


    if (b == aa):
        b1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (A, B, A, B)
    elif (b == bb):
        b1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &gt; `` %s$$/수식$$" % (D, C, D, C)
    elif (b == cc):
        b1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &gt; `` %s$$/수식$$" % (E, F, E, F)
    else:
        b1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (G, H, G, H)

    if (c == aa):
        c1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (A, B, A, B)
    elif (c == bb):
        c1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &gt; `` %s$$/수식$$" % (D, C, D, C)
    elif (c == cc):
        c1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &gt; `` %s$$/수식$$" % (E, F, E, F)
    else:
        c1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (G, H, G, H)

    if (d == aa):
        d1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (A, B, A, B)
    elif (d == bb):
        d1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &gt; `` %s$$/수식$$" % (D, C, D, C)
    elif (d == cc):
        d1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &gt; `` %s$$/수식$$" % (E, F, E, F)
    else:
        d1 = "비교하는 양 : $$수식$$%s$$/수식$$, 기준량 : $$수식$$%s$$/수식$$ → $$수식$$%s `` &lt; `` %s$$/수식$$" % (G, H, G, H)


    stem = stem.format(a=a,b=b,c=c,d=d)
    answer = answer.format(I=I,J=J)
    comment = comment.format(a1=a1,b1=b1,c1=c1,d1=d1,I=I,J=J)

    return stem, answer, comment





















#6-1-4-23
def ratandpro614_Stem_011():
    stem = "기준량을 나타내는 수가 다른 하나를 찾아 기호를 써 보세요.\n$$표$$㉠ {aa}\n㉡ {bb}\n㉢ {cc}\n㉣ {dd}$$/표$$\n"
    answer = "(정답)\n{C}\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 비, " \
              "$$수식$${A}$$/수식$$대 $$수식$${B}$$/수식$$, " \
              "$$수식$${B}$$/수식$$에 대한 $$수식$${A}$$/수식$$의 비 → " \
              "$$수식$${A}$$/수식$$:$$수식$${B}$$/수식$$ → 기준량 : $$수식$${B}$$/수식$$\n" \
              "$$수식$${A}$$/수식$$에 대한 $$수식$${B}$$/수식$$의 비 → " \
              "$$수식$${B}$$/수식$$:$$수식$${A}$$/수식$$ → 기준량 : $$수식$${A}$$/수식$$\n\n"


    while 1:
        A = np.random.randint(2, 10)
        B = np.random.randint(2, 10)
        if A != B and soroso(A, B):
            break

    aa = "$$수식$$%s$$/수식$$와 $$수식$$%s$$/수식$$의 비" % (A, B)
    bb = "$$수식$$%s$$/수식$$ 대 $$수식$$%s$$/수식$$" % (A, B)
    cc = "$$수식$$%s$$/수식$$에 대한 $$수식$$%s$$/수식$$의 비" % (A, B)
    dd = "$$수식$$%s$$/수식$$에 대한 $$수식$$%s$$/수식$$의 비" % (B, A)

    # aaa = aa
    # bbb = bb
    ccc = cc
    # ddd = dd

    NN = [aa, bb, cc, dd]
    np.random.shuffle(NN)
    aa, bb, cc, dd = NN

    for i in NN:
        if(i == ccc and i == aa):
            C = "㉠"
            break
        if (i == ccc and i == bb):
            C = "㉡"
            break
        if (i == ccc and i == cc):
            C = "㉢"
            break
        if (i == ccc and i == dd):
            C = "㉣"
            break

    stem = stem.format(aa=aa, bb=bb, cc=cc, dd=dd)
    answer = answer.format(C=C)
    comment = comment.format(A=A, B=B)

    return stem, answer, comment


















#6-1-4-24
def ratandpro614_Stem_012():
    stem = "같은 크기의 컵으로 그릇에 밀가루 $$수식$${A}$$/수식$$컵과 우유 $$수식$${B}$$/수식$$컵을 넣어 빵을 만들려고 합니다. 밀가루 양에 대한 우유의 양의 비율을 분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${B} over {A}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$우유의 양$$수식$$RIGHT )$$/수식$$" \
              ":$$수식$$LEFT ($$/수식$$밀가루의 양$$수식$$RIGHT )$$/수식$$ → $$수식$${B}$$/수식$$:$$수식$${A}$$/수식$$ → $$수식$${B} over {A}$$/수식$$\n\n"


    while(1):
        A = np.random.randint(2, 10)
        B = np.random.randint(2, 10)
        if A > B and soroso(A, B):
            break

    stem = stem.format(A=A, B=B)
    answer = answer.format(A=A, B=B)
    comment = comment.format(A=A, B=B)

    return stem, answer, comment



















#최대공약수 (서로소 구할 때 사용)
def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a


#6-1-4-26
def ratandpro614_Stem_013():
    stem = "비율이 높은 것부터 차례대로 기호를 써 보세요.\n$$표$$㉠ {aa}\n㉡ {bb}\n㉢ {cc}$$/표$$\n"
    answer = "(정답)\n{J}, {K}, {L}\n"
    comment = "(해설)\n" \
              "{a1}\n" \
              "{b1}\n" \
              "{c1}\n" \
              "비율이 큰 것부터 차례대로 기호를 쓰면 {J}, {K}, {L}입니다.\n\n"


    while(1):
        A = np.random.randint(2,10)
        C = np.random.randint(2,10)
        E = np.random.randint(2,10)

        N = [5, 10, 20]
        np.random.shuffle(N)
        B, D, F = N

        if(gcd(A,B) == 1 and A < B):
            if (gcd(C, D) == 1 and C < D):
                if (gcd(E, F) == 1 and E < F):
                    break


    G = A/B
    H = C/D
    I = E/F

    aa = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$" % (A, B)
    bb = "$$수식$$%s$$/수식$$의 $$수식$$%s$$/수식$$에 대한 비" % (C, D)
    cc = "$$수식$$%s$$/수식$$에 대한 $$수식$$%s$$/수식$$의 비" % (F, E)

    aaa = aa
    bbb = bb
    ccc = cc

    NN = [aa,bb,cc]
    np.random.shuffle(NN)
    aa, bb, cc = NN

    a1 = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$ → $$수식$$LEFT ($$/수식$$비율$$수식$$RIGHT ) `` = `` %s over %s `` = `` %s$$/수식$$" % (A, B, A, B, G)
    b1 = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$ → $$수식$$LEFT ($$/수식$$비율$$수식$$RIGHT ) `` = `` %s over %s `` = `` %s$$/수식$$" % (C, D, C, D, H)
    c1 = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$ → $$수식$$LEFT ($$/수식$$비율$$수식$$RIGHT ) `` = `` %s over %s `` = `` %s$$/수식$$" % (E, F, E, F, I)


    for i in NN:
        if(i == aaa and i == aa):
            a1 = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$ → $$수식$$LEFT ($$/수식$$비율$$수식$$RIGHT ) `` = `` %s over %s `` = `` %s$$/수식$$" % (A, B, A, B, G)
            gg = G
            break
        if (i == aaa and i == bb):
            b1 = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$ → $$수식$$LEFT ($$/수식$$비율$$수식$$RIGHT ) `` = `` %s over %s `` = `` %s$$/수식$$" % (A, B, A, B, G)
            hh = G
            break
        if (i == aaa and i == cc):
            c1 = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$ → $$수식$$LEFT ($$/수식$$비율$$수식$$RIGHT ) `` = `` %s over %s `` = `` %s$$/수식$$" % (A, B, A, B, G)
            ii = G
            break

    for i in NN:
        if(i == bbb and i == aa):
            a1 = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$ → $$수식$$LEFT ($$/수식$$비율$$수식$$RIGHT ) `` = `` %s over %s `` = `` %s$$/수식$$" % (C, D, C, D, H)
            gg = H
            break
        if (i == bbb and i == bb):
            b1 = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$ → $$수식$$LEFT ($$/수식$$비율$$수식$$RIGHT ) `` = `` %s over %s `` = `` %s$$/수식$$" % (C, D, C, D, H)
            hh = H
            break
        if (i == bbb and i == cc):
            c1 = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$ → $$수식$$LEFT ($$/수식$$비율$$수식$$RIGHT ) `` = `` %s over %s `` = `` %s$$/수식$$" % (C, D, C, D, H)
            ii = H
            break

    for i in NN:
        if(i == ccc and i == aa):
            a1 = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$ → $$수식$$LEFT ($$/수식$$비율$$수식$$RIGHT ) `` = `` %s over %s `` = `` %s$$/수식$$" % (E, F, E, F, I)
            gg = I
            break
        if (i == ccc and i == bb):
            b1 = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$ → $$수식$$LEFT ($$/수식$$비율$$수식$$RIGHT ) `` = `` %s over %s `` = `` %s$$/수식$$" % (E, F, E, F, I)
            hh = I
            break
        if (i == ccc and i == cc):
            c1 = "$$수식$$%s$$/수식$$:$$수식$$%s$$/수식$$ → $$수식$$LEFT ($$/수식$$비율$$수식$$RIGHT ) `` = `` %s over %s `` = `` %s$$/수식$$" % (E, F, E, F, I)
            ii = I
            break


    if (gg > hh):
        if (gg > ii):
            if (hh > ii):
                J = "㉠"
                K = "㉡"
                L = "㉢"
            else:
                J = "㉠"
                K = "㉢"
                L = "㉡"
        else:
            J = "㉢"
            K = "㉠"
            L = "㉡"
    elif (hh > gg):
        if (ii > gg):
            if (hh > ii):
                J = "㉡"
                K = "㉢"
                L = "㉠"
            else:
                J = "㉢"
                K = "㉡"
                L = "㉠"
        else:
            J = "㉡"
            K = "㉠"
            L = "㉢"

    stem = stem.format(aa=aa,bb=bb,cc=cc)
    answer = answer.format(J=J,K=K,L=L)
    comment = comment.format(a1=a1,b1=b1,c1=c1,J=J,K=K,L=L)

    return stem, answer, comment




















#6-1-4-27
def ratandpro614_Stem_014():
    stem = "종이배를 흐르는 강물에 띄웠더니 $$수식$${A} rm m$$/수식$$를 가는 데 $$수식$${B}$$/수식$$분이 걸렸습니다. 종이배가 $$수식$${A} rm m$$/수식$$를 가는 데 걸린 시간에 대한 간 거리의 비율을 가장 간단한 수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${C}$$/수식$$\n"
    comment = "(해설)\n" \
              "종이배가 가는데 걸린 시간은 $$수식$${B}$$/수식$$분이고, 간 거리는 $$수식$${A} rm m$$/수식$$입니다.\n" \
              "따라서 종이배가 가는데 걸린 시간에 대한 간 거리의 비율은 $$수식$${A} over {B} ` = ` {C}$$/수식$$입니다.\n\n"


    while(1):
        A = np.random.randint(1,1000)
        B = np.random.randint(2,61)
        C = math.floor(A/B)
        if(A != B):
            if(B != 10):
                if(A % B == 0):
                    break


    stem = stem.format(A=A,B=B)
    answer = answer.format(C=C)
    comment = comment.format(A=A,B=B,C=C)

    return stem, answer, comment














#6-1-4-28
def ratandpro614_Stem_015():
    stem = "벽에 색칠 할 색을 만들기 위해 {A}과 {B} 페인트를 $$수식$${C}$$/수식$$:$$수식$${D}$$/수식$$로 섞었습니다. {B} 페인트의 양과 {A} 페인트의 양의 비율을 분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${D} over {C}$$/수식$$\n"
    comment = "(해설)\n" \
              "{A}과 {B} 페인트를 $$수식$${C}$$/수식$$:$$수식$${D}$$/수식$$로 섞었으므로 {A} 페인트의 양 $$수식$${C}$$/수식$${j1} " \
              "{B} 페인트의 양 $$수식$${D}$$/수식$${j2} 기준으로 섞은 것입니다.\n" \
              "{B} 페인트 양과 {A} 페인트 양의 비는 {B} 페인트의 양 $$수식$${D}$$/수식$${j2} " \
              "{A} 페인트의 양 $$수식$${C}$$/수식$${j1} 기준으로 비교한 비이므로 $$수식$${D}$$/수식$$:$$수식$${C}$$/수식$$입니다.\n" \
              "따라서 비율을 분수로 나타내면 $$수식$${D} over {C}$$/수식$$입니다.\n\n"


    N = ["빨간색", "초록색", "파란색", "노란색", "분홍색"]

    while 1:
        C = np.random.randint(2, 10)
        D = np.random.randint(2, 10)

        N2 = np.random.choice(N, 2)

        A, B = N2

        if C != D and A != B and soroso(C, D):
            break

    j1 = proc_jo(C, 1)
    j2 = proc_jo(D, 1)

    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(C=C, D=D)
    comment = comment.format(A=A, B=B, C=C, D=D, j1=j1, j2=j2)

    return stem, answer, comment

















#6-1-4-30
def ratandpro614_Stem_016():
    stem = "{who}네 가족과 친척들이 $$수식$${A}$$/수식$$인승과 $$수식$${B}$$/수식$$인승 차에 각각 나누어 탔습니다. $$수식$${A}$$/수식$$인승 차에는 $$수식$${C}$$/수식$$명이 탔고, $$수식$${B}$$/수식$$인승 차에는 $$수식$${D}$$/수식$$명이 탔을 때 어느 차에 사람들이 더 넓게 느꼈을 지 구해보세요.\n$$수식$${box}$$/수식$$ 인승 차에 탄 사람들이 더 넓게 느꼈습니다.\n"
    answer = "(정답)\n$$수식$${E}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$인승 차의 정원에 대한 탄 사람 수의 비\n" \
              "→ $$수식$${C}$$/수식$$:$$수식$${A}$$/수식$$ → $$수식$$LEFT ($$/수식$$비율$$수식$$RIGHT ) = {C} over {A} {sca}$$/수식$$\n" \
              "$$수식$${B}$$/수식$$인승 차의 정원에 대한 탄 사람 수의 비\n" \
              "→ $$수식$${D}$$/수식$$:$$수식$${B}$$/수식$$ → $$수식$$LEFT ($$/수식$$비율$$수식$$RIGHT ) = {D} over {B} {sdb}$$/수식$$\n" \
              "비율이 더 낮은 $$수식$${E}$$/수식$$인승 차에 탄 사람들이 더 넓게 느꼈을 것입니다.\n\n"


    who = ["정수", "준수", "종국이", "서현이", "태연이", "보라", "윤미", "희정이", "도철이", "준혁이", "나래", "솔미"][np.random.randint(0, 12)]

    A = np.random.randint(4, 41)
    B = np.random.randint(4, 41)

    C = np.random.randint(2, A)
    D = np.random.randint(2, B)

    if (C/A) < (D/B):
        E = A
    else:
        E = B

    fra1 = fractions.Fraction(C, A)

    if fra1.denominator == A:
        sca = ""
    else:
        sca = "= {%s} over {%s}" % (fra1.numerator, fra1.denominator)

    fra2 = fractions.Fraction(D, B)

    if fra2.denominator == B:
        sdb = ""
    else:
        sdb = "= {%s} over {%s}" % (fra2.numerator, fra2.denominator)

    box = "box{　　　}"

    stem = stem.format(A=A, B=B, C=C, D=D, who=who, box=box)
    answer = answer.format(E=E)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, sca=sca, sdb=sdb)

    return stem, answer, comment















#6-1-4-31
def ratandpro614_Stem_017():
    stem = "{who}는 집에서 $$수식$${A} rm {{km}}$$/수식$$ 떨어져 있는 할머니 댁까지 $$수식$${B}$$/수식$$시간 $$수식$${C}$$/수식$$분 동안 기차를 타고 갔습니다. {who}가 기차를 타고 할머니 댁까지 가는 데 걸린 시간에 대한 간 거리의 비율을 구하려고 합니다.\n걸린 시간을 분, 간 거리를 $$수식$$rm {{km}}$$/수식$$로 하여 비율을 가장 간단한 수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${E}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${B}$$/수식$$시간 $$수식$${C}$$/수식$$분 $$수식$$= `` 60 TIMES {B}$$/수식$$분 $$수식$$+ `` {C}$$/수식$$분 $$수식$$= `` {D}$$/수식$$분이므로\n" \
              "$$수식$${a} over {b} ` = ` {A} over {D} ` = ` {E}$$/수식$$입니다.\n\n"


    who = ["수지", "영기", "혜선이", "주영이", "주상이", "윤주", "시언이", "준혁이", "석훈이", "태희", "세나", "백호"][np.random.randint(0, 12)]

    while(1):
        A = np.random.randint(100,500)
        B = np.random.randint(1,4)
        C = np.random.randint(1,61)
        D = 60*B+C
        E = math.floor(A/D)
        if(A % D == 0):
            break

    a = "{간 거리}"
    b = "{걸린 시간}"

    stem = stem.format(A=A, B=B, C=C, who=who)
    answer = answer.format(E=E)
    comment = comment.format(B=B, C=C, D=D, a=a, b=b, A=A, E=E)

    return stem, answer, comment
















#6-1-4-33
def ratandpro614_Stem_018():
    stem = "{who}는 $$수식$${A} rm m$$/수식$$를 달리는 데 $$수식$${B}$$/수식$$초가 걸렸습니다. {who}가 $$수식$${A} rm m$$/수식$$를 달리는 데 걸린 시간에 대한 달린 거리의 비율을 가장 간단한 수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${C}$$/수식$$\n"
    comment = "(해설)\n" \
              "기준량은 $$수식$${B}$$/수식$$초이고, 비교하는 양은 $$수식$${A} rm m$$/수식$$입니다.\n" \
              "따라서 비로 나타내면 $$수식$${A}$$/수식$$:$$수식$${B}$$/수식$$이고, 비율을 가장 간단한 수로 나타내면 $$수식$${A} over {B} ` = ` {C}$$/수식$$입니다.\n\n"


    who = ["윤서", "세진이", "준기", "태현이", "석재", "창훈이", "은주", "정환이", "아라", "우주", "하나", "정재"][np.random.randint(0, 12)]

    while(1):
        A = np.random.randint(50,201)
        B = np.random.randint(10,61)
        C = math.floor(A/B)
        if(A % B == 0):
            break

    stem = stem.format(A=A, B=B, who=who)
    answer = answer.format(C=C)
    comment = comment.format(A=A, B=B, C=C)

    return stem, answer, comment














#6-1-4-34
def ratandpro614_Stem_019():
    stem = "(가) 비커에 소금 $$수식$${A} rm g$$/수식$$을 녹여 소금물 $$수식$${B} rm g$$/수식$$을 만들었고, (나) 비커에 소금 $$수식$${F} rm g$$/수식$$을 녹여 소금물 $$수식$${G} rm g$$/수식$$을 만들었습니다. (가) 비커와 (나) 비커의 소금물의 양에 대한 소금의 양의 비율을 각각 소수로 나타내어 순서대로 쓰세요.\n"
    answer = "(정답)\n$$수식$${E}$$/수식$$, $$수식$${J}$$/수식$$\n"
    comment = "(해설)\n" \
              "(가) 비커의 소금물의 양에 대한 소금의 양의 비\n" \
              "→ $$수식$${A}$$/수식$$:$$수식$${B}$$/수식$$ → $$수식$$LEFT ($$/수식$$비율$$수식$$RIGHT ) = {A} over {B} ` = ` {C} over {D} ` = ` {E}$$/수식$$\n" \
              "(나) 비커의 소금물의 양에 대한 소금의 양의 비\n" \
              "→ $$수식$${F}$$/수식$$:$$수식$${G}$$/수식$$ → $$수식$$LEFT ($$/수식$$비율$$수식$$RIGHT ) = {F} over {G} ` = ` {H} over {I} ` = ` {J}$$/수식$$\n\n"

    while (1):
        a = np.random.randint(0, 7)
        b = np.random.randint(0, 3)
        c = pow(2, a) * pow(5, b)

        A = np.random.randint(10, 100)
        B = np.random.randint(100, 1000)

        aa = fractions.Fraction(A, B)
        C = aa.numerator
        D = aa.denominator
        E = C / D
        F = np.random.randint(10, 100)
        G = np.random.randint(100, 1000)
        bb = fractions.Fraction(F, G)
        H = bb.numerator
        I = bb.denominator
        J = H / I

        Z = [1, 2, 4, 8, 16, 32, 64, 5, 25, 10, 20, 40, 80, 50]

        if D in Z:
            if (D < 100):
                if I in Z:
                    if (I < 100):
                        if (aa != bb):
                            # break
                            if len(str(J)) < 5:
                                if len(str(E)) < 5:
                                    break


    stem = stem.format(A=A, B=B, F=F, G=G)
    answer = answer.format(E=E, J=J)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J)

    return stem, answer, comment


















#6-1-4-35
def ratandpro614_Stem_020():
    stem = "{A}와 {B}는 농구공 던져 넣기를 했습니다. 두 친구의 성공률을 각각 소수로 나타내어 순서대로 쓰세요.\n$$표$$$$수식$$LEFT [$$/수식$${A}$$수식$$ RIGHT ]$$/수식$$ 난 공을 $$수식$${C}$$/수식$$번 던져 $$수식$${D}$$/수식$$번 넣었어.\n$$수식$$LEFT [$$/수식$${B}$$수식$$RIGHT ]$$/수식$$ 난 공을 $$수식$${H}$$/수식$$번 던져 $$수식$${I}$$/수식$$번 넣었어.$$/표$$\n"
    answer = "(정답)\n$$수식$${G}$$/수식$$, $$수식$${L}$$/수식$$\n"
    comment = "(해설)\n" \
              "{A}의 성공률은 $$수식$${D} over {C} ` = ` {F} over {E} ` = ` {G}$$/수식$$이고,\n" \
              "{B}의 성공률은 $$수식$${I} over {H} ` = ` {K} over {J} ` = ` {L}$$/수식$$입니다.\n\n"


    N = ["기호", "준서", "승하", "민하", "성희", "연아", "권기", "나래", "솔미", "정재", "선우", "지혜", "윤수", "세나", "은배", "동후", "보배"]

    while(1):
        A, B = np.random.choice(N, 2)
        C = np.random.randint(10,100)
        H = np.random.randint(10,100)
        D = np.random.randint(2,C)
        I = np.random.randint(2,H)
        aa = fractions.Fraction(D,C)
        F = aa.numerator
        E = aa.denominator
        G = F/E
        bb = fractions.Fraction(I,H)
        K = bb.numerator
        J = bb.denominator
        L = K/J

        Z = [1,2,4,8,16,32,64,5,25,10,20,40,80,50]

        if E in Z:
            if (aa != bb):
                if J in Z:
                    if (A != B):
                        break

    stem = stem.format(A=A, B=B, C=C, D=D, H=H, I=I)
    answer = answer.format(G=G, L=L, A=A, B=B)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L)

    return stem, answer, comment

















#6-1-4-37
def ratandpro614_Stem_021():
    stem = "빨간 버스는 $$수식$${A} rm {{km}}$$/수식$$를 가는 데 $$수식$${B}$$/수식$$시간이 걸렸고, 파란 버스는 $$수식$${C} rm {{km}}$$/수식$$를 가는 데 $$수식$${D}$$/수식$$시간이 걸렸습니다. □ 안에 알맞은 수나 말을 차례대로 쓰세요.\n" \
        "$$표$$두 버스의 걸린 시간에 대한 달린 거리의 비율을 가장 간단한 수로 각각 나타내면 빨간버스는 {boxblank}, 파란 버스는 {boxblank} 입니다. 따라서 {boxblank} 버스가 더 빠릅니다.$$/표$$"
    answer = "(정답)\n$$수식$${E}$$/수식$$, $$수식$${F}$$/수식$$, {G}\n"
    comment = "(해설)\n" \
              "걸린 시간에 대한 달린 거리의 비율을 가장 간단한 수로 각각 구하면\n" \
              "빨간 버스 : $$수식$${A} over {B} ` = ` {E}$$/수식$$, 파란 버스 : $$수식$${C} over {D} ` = `{F}$$/수식$$\n" \
              "{H}\n\n"

    boxblank = "$$수식$$BOX{　　}$$/수식$$"

    while(1):
        A = np.random.randint(101,501)
        B = np.random.randint(2,10)
        C = np.random.randint(101,501)
        D = np.random.randint(2,10)
        E = math.floor(A/B)
        F = math.floor(C/D)
        if(A % B == 0):
            if(C % D == 0):
                if(C!=A):
                    if(D!=B):
                        if(F!=E):
                            break

    if(E<F):
        G = "파란"
        H = "$$수식$$%s &lt; %s$$/수식$$이므로 파란 버스가 더 빠릅니다." % (E, F)
    else:
        G = "빨간"
        H = "$$수식$$%s &gt; %s$$/수식$$이므로 빨간 버스가 더 빠릅니다." % (E, F)

    stem = stem.format(A=A, C=C, B=B, D=D, boxblank=boxblank)
    answer = answer.format(E=E, F=F, G=G)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, H=H)

    return stem, answer, comment













#6-1-4-38
def ratandpro614_Stem_022():
    stem = "{A}와 {B}는 야구 경기에 나갔습니다. 전체 타수에 대한 안타 수의 비율을 비교하면 누구의 타율이 더 높은가요?\n$$표$$$$수식$$LEFT [$$/수식$${A}$$수식$$RIGHT ]$$/수식$$ 난 $$수식$${C}$$/수식$$타수 중에서 안타를 $$수식$${D}$$/수식$$개 쳤어.\n$$수식$$LEFT [$$/수식$${B}$$수식$$RIGHT ]$$/수식$$ 난 $$수식$${H}$$/수식$$타수 중에서 안타를 $$수식$${I}$$/수식$$개 쳤어.$$/표$$\n"
    answer = "(정답)\n{M}\n"
    comment = "(해설)\n" \
              "전체 타수에 대한 안타 수의 비율을 각각 구하면\n" \
              "{sent_a}" \
              "{sent_b}" \
              "{X}\n\n"

    N = ["원기", "준규", "슬기", "송하", "시우", "종수", "대희", "근호", "필교", "정주", "현배", "선구", "용희"]

    while (1):
        A, B = np.random.choice(N, 2)
        C = np.random.randint(11, 100)
        H = np.random.randint(11, 100)
        D = np.random.randint(2, C)
        I = np.random.randint(2, H)
        aa = fractions.Fraction(D, C)
        F = aa.numerator
        E = aa.denominator
        G = F / E
        bb = fractions.Fraction(I, H)
        K = bb.numerator
        J = bb.denominator
        L = K / J

        Z = [1, 2, 4, 8, 16, 32, 64, 5, 25, 10, 20, 40, 80, 50]

        if E in Z:
            if (aa != bb):
                if J in Z:
                    if (A != B):
                        if (C != H and I != D):
                            # break
                            if len(str(G)) < 5:
                                if len(str(L)) < 5:
                                    break

    if D == F and C == E:
        sent_a = "%s : $$수식$$%s over %s ` = ` %s$$/수식$$\n" % (A, D, C, G)
    else:
        sent_a = "%s : $$수식$$%s over %s ` = ` %s over %s ` = ` %s$$/수식$$\n" % (A, D, C, F, E, G)

    if I == K and H == J:
        sent_b = "%s : $$수식$$%s over %s ` = ` %s$$/수식$$\n" % (B, I, H, L)
    else:
        sent_b = "%s : $$수식$$%s over %s ` = ` %s over %s ` = ` %s$$/수식$$\n" % (B, I, H, K, J, L)

    if (G < L):
        M = B
        X = "$$수식$$%s &lt; %s$$/수식$$이므로 %s의 타율이 더 높습니다." % (G, L, B)
    else:
        M = A
        X = "$$수식$$%s &gt; %s$$/수식$$이므로 %s의 타율이 더 높습니다." % (G, L, A)


    stem = stem.format(A=A, B=B, C=C, D=D, H=H, I=I)
    answer = answer.format(M=M)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, X=X, sent_a=sent_a,
                             sent_b=sent_b)

    return stem, answer, comment


















#6-1-4-41
def ratandpro614_Stem_023():
    stem = "{A}, {B}, {C}가 축구공을 차서 많이 넣기를 하였습니다. 전체 찬 공 수에 대한 넣은 공 수의 비율이 가장 높은 사람은 누구인가요?\n$$표$$$$수식$$LEFT [$$/수식$${A}$$수식$$RIGHT ]$$/수식$$ 공 $$수식$${D}$$/수식$$개를 차서 $$수식$${E}$$/수식$$개를 넣었지.\n$$수식$$LEFT [$$/수식$${B}$$수식$$RIGHT ]$$/수식$$ 공 $$수식$${I}$$/수식$$개를 차서 $$수식$${J}$$/수식$$개를 넣었지.\n$$수식$$LEFT [$$/수식$${C}$$수식$$RIGHT ]$$/수식$$ 전체 찬 공 수에 대한 넣은 공 수의 비율은 $$수식$${P}$$/수식$${ya}.$$/표$$\n"
    answer = "(정답)\n{Q}\n"
    comment = "(해설)\n" \
              "전체 찬 공 수에 대한 넣은 공 수의 비율을 각각 구하면\n" \
              "{sent_a}" \
              "{sent_b}" \
              "{C} : $$수식$${P}$$/수식$$\n" \
              "{X}\n\n"

    # while (1):
        # ZZ = ["연서", "준호", "선재", "상호", "지후", "수하", "민규", "승리", "희재", "현우", "정수"]
        # A, B, C = np.random.choice(ZZ, 3)
        #
        # D = np.random.randint(11, 100)
        # I = np.random.randint(11, 100)
        #
        # E = np.random.randint(2, D)
        # J = np.random.randint(2, I)
        #
        # aa = fractions.Fraction(E, D)
        # G = aa.numerator
        # F = aa.denominator
        # H = G / F
        #
        # bb = fractions.Fraction(J, I)
        # L = bb.numerator
        # K = bb.denominator
        # M = L / K
        #
        # N = np.random.randint(10, 100)
        # P = N / 100
        #
        # # Z = [1, 2, 4, 8, 16, 32, 64, 5, 25, 10, 20, 40, 80, 50]
        # Z = [1, 2, 4, 8, 5, 25, 10, 20, 50]
        #
        # if K in Z:
        #     if (aa != bb):
        #         if F in Z:
        #             if (A != B != C):
        #                 if (D != I and J != E):
        #                     # break
        #                     if len(str(H)) < 5:
        #                         if len(str(M)) < 5:
        #                             break

    while True:
        ZZ = ["연서", "준호", "선재", "상호", "지후", "수하", "민규", "승리", "희재", "현우", "정수"]
        A, B, C = np.random.choice(ZZ, 3)

        if A == B or A == C or B == C:
            continue
        else:
            break

    while True:
        Z = [1, 2, 4, 8, 5, 25, 10, 20, 50]

        D = np.random.randint(11, 100)
        I = np.random.randint(11, 100)

        if D == I:
            continue

        E = np.random.randint(2, D)
        J = np.random.randint(2, I)

        if E == J:
            continue

        aa = fractions.Fraction(E, D)
        G = aa.numerator
        F = aa.denominator
        H = G / F

        if F not in Z:
            continue

        bb = fractions.Fraction(J, I)
        L = bb.numerator
        K = bb.denominator
        M = L / K

        if K not in Z:
            continue

        if aa == bb:
            continue

        N = np.random.randint(10, 100)
        P = N / 100

        if len(str(H)) < 5:
            if len(str(M)) < 5:
                break


    if int((str(H))[-1]) == 2 or int((str(H))[-1]) == 4 or int((str(H))[-1]) == 5 or int((str(H))[-1]) == 9:
        j1 = "가"
    else:
        j1 = "이"

    if int((str(M))[-1]) == 2 or int((str(M))[-1]) == 4 or int((str(M))[-1]) == 5 or int((str(M))[-1]) == 9:
        j2 = "가"
    else:
        j2 = "이"

    if int((str(P))[-1]) == 2 or int((str(P))[-1]) == 4 or int((str(P))[-1]) == 5 or int((str(P))[-1]) == 9:
        ya = "야"
        j3 = "가"
    else:
        ya = "이야"
        j3 = "이"

    Q = ""

    while True:
        if (H > M and H > P):
            Q = A
            X = "$$수식$$%s$$/수식$$%s 가장 크므로 전체 찬 공 수에 대한 넣은 공 수의 비율이 가장 높은 사람은 %s입니다." % (H, j1, Q)
        elif (M > H and M > P):
            Q = B
            X = "$$수식$$%s$$/수식$$%s 가장 크므로 전체 찬 공 수에 대한 넣은 공 수의 비율이 가장 높은 사람은 %s입니다." % (M, j2, Q)
        elif (P > H and P > M):
            Q = C
            X = "$$수식$$%s$$/수식$$%s 가장 크므로 전체 찬 공 수에 대한 넣은 공 수의 비율이 가장 높은 사람은 %s입니다." % (P, j3, Q)

        if Q != "":
            break

    if E == G and D == F:
        sent_a = "%s : $$수식$$%s over %s ` = ` %s$$/수식$$\n" % (A, E, D, H)
    else:
        sent_a = "%s : $$수식$$%s over %s ` = ` %s over %s ` = ` %s$$/수식$$\n" % (A, E, D, G, F, H)

    if J == L and I == K:
        sent_b = "%s : $$수식$$%s over %s ` = ` %s$$/수식$$\n" % (B, J, I, M)
    else:
        sent_b = "%s : $$수식$$%s over %s ` = ` %s over %s ` = ` %s$$/수식$$\n" % (B, J, I, L, K, M)

    stem = stem.format(A=A, B=B, C=C, D=D, I=I, E=E, J=J, P=P, ya=ya)
    answer = answer.format(Q=Q)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, M=M, X=X, P=P, sent_a=sent_a,
                             sent_b=sent_b)

    return stem, answer, comment


















#6-1-4-42
def ratandpro614_Stem_024():
    stem = "물에 포도 원액을 {A}는 $$수식$${E} rm mL$$/수식$$를 넣어 포도 주스 $$수식$${D} rm mL$$/수식$$, {B}는 $$수식$${J} rm mL$$/수식$$를 넣어 포도 주스 $$수식$${I} rm mL$$/수식$$, {C}는 $$수식$${O} rm mL$$/수식$$를 넣어 포도 주스 $$수식$${N} rm mL$$/수식$$를 각각 만들었습니다. 포도 주스 양에 대한 포도 원액 양의 비율을 구해 누가 만든 포도 주스가 가장 진한지 구해 보세요.\n"
    answer = "(정답)\n{S}\n"
    comment = "(해설)\n" \
              "포도 주스 양에 대한 포도 원액 양의 비율을 각각 구하면\n" \
              "{sent_a}" \
              "{sent_b}" \
              "{sent_c}" \
              "{X}\n\n"


    # while(1):
    #     ZZ = ["민수", "지우", "수지", "영호", "진희", "세미"]
    #     A, B, C = np.random.choice(ZZ, 3)
    #
    #     D = np.random.randint(101, 1000)
    #     I = np.random.randint(101, 1000)
    #     N = np.random.randint(101, 1000)
    #
    #     E = np.random.randint(50, D)
    #     J = np.random.randint(50, I)
    #     O = np.random.randint(50, N)
    #
    #     aa = fractions.Fraction(E, D)
    #     G = aa.numerator
    #     F = aa.denominator
    #     H = G/F
    #
    #     bb = fractions.Fraction(J, I)
    #     L = bb.numerator
    #     K = bb.denominator
    #     M = L/K
    #
    #     cc = fractions.Fraction(O, N)
    #     Q = cc.numerator
    #     P = cc.denominator
    #     R = Q/P
    #
    #     Z = [1, 2, 4, 8, 16, 32, 64, 5, 25, 10, 20, 40, 80, 50]
    #
    #     if F in Z:
    #         if (J != E and O != E and O != J):
    #             if P in Z:
    #                 if(aa != bb and bb != cc and cc != aa):
    #                     if K in Z:
    #                         break

    # 위 코드는 값이 나오는데 너무 느림

    while True:
        ZZ = ["민수", "지우", "수지", "영호", "진희", "세미"]
        A, B, C = np.random.choice(ZZ, 3)

        if A != B and A != C and B != C:
            break

    z_list = [2, 4, 8, 16, 32, 64, 5, 25, 10, 20, 40, 80, 50]

    # while True:
    #     choice1 = np.random.randint(0, 13)
    #     choice2 = np.random.randint(0, 13)
    #     choice3 = np.random.randint(0, 13)
    #     if choice1 != choice2 and choice1 != choice3 and choice2 != choice3:
    #         break
    #
    # F = z_list[choice1]
    # K = z_list[choice2]
    # P = z_list[choice3]
    #
    # while True:
    #     G = np.random.randint(1, 70)
    #     check1 = 50 / G
    #     if gcd(F, G) == 1 and G < F and check1 * F < 1000:
    #         break
    #
    # while True:
    #     L = np.random.randint(1, 70)
    #     check2 = 50 / L
    #     if gcd(K, L) == 1 and L < K and check2 * K < 1000:
    #         break
    #
    # while True:
    #     Q = np.random.randint(1, 70)
    #     check3 = 50 / Q
    #     if gcd(P, Q) == 1 and Q < P and check3 * P < 1000:
    #         break
    #
    # while True:
    #     while True:
    #         mu1 = np.random.randint(1, 501)
    #         E = mu1 * G
    #         D = mu1 * F
    #         if E >= 50 and D > 100 and D < 1000:
    #             break
    #
    #     while True:
    #         mu2 = np.random.randint(1, 501)
    #         J = mu2 * L
    #         I = mu2 * K
    #         if J >= 50 and I > 100 and I < 1000:
    #             break
    #
    #     while True:
    #         mu3 = np.random.randint(1, 501)
    #         O = mu3 * Q
    #         N = mu3 * P
    #         if O >= 50 and N > 100 and N < 1000:
    #             break
    #
    #     if mu1 != mu2 and mu1 != mu3 and mu2 != mu3:
    #         break
    #
    # H = G / F
    # M = L / K
    # R = Q / P


    while True:
        while True:
            choice1 = np.random.randint(0, 13)
            choice2 = np.random.randint(0, 13)
            choice3 = np.random.randint(0, 13)
            if choice1 != choice2 and choice1 != choice3 and choice2 != choice3:
                break

        F = z_list[choice1]
        K = z_list[choice2]
        P = z_list[choice3]

        while True:
            G = np.random.randint(1, 70)
            check1 = 50 / G
            if gcd(F, G) == 1 and G < F and check1 * F < 1000:
                break

        while True:
            L = np.random.randint(1, 70)
            check2 = 50 / L
            if gcd(K, L) == 1 and L < K and check2 * K < 1000:
                break

        while True:
            Q = np.random.randint(1, 70)
            check3 = 50 / Q
            if gcd(P, Q) == 1 and Q < P and check3 * P < 1000:
                break

        H = G / F
        M = L / K
        R = Q / P

        if len(str(H)) < 5:
            if len(str(M)) < 5:
                if len(str(R)) < 5:
                    break


    while True:
        while True:
            mu1 = np.random.randint(1, 501)
            E = mu1 * G
            D = mu1 * F
            if E >= 50 and D > 100 and D < 1000:
                break

        while True:
            mu2 = np.random.randint(1, 501)
            J = mu2 * L
            I = mu2 * K
            if J >= 50 and I > 100 and I < 1000:
                break

        while True:
            mu3 = np.random.randint(1, 501)
            O = mu3 * Q
            N = mu3 * P
            if O >= 50 and N > 100 and N < 1000:
                break

        if mu1 != mu2 and mu1 != mu3 and mu2 != mu3:
            break




    if int((str(H))[-1]) == 2 or int((str(H))[-1]) == 4 or int((str(H))[-1]) == 5 or int((str(H))[-1]) == 9:
        j1 = "가"
    else:
        j1 = "이"

    if int((str(M))[-1]) == 2 or int((str(M))[-1]) == 4 or int((str(M))[-1]) == 5 or int((str(M))[-1]) == 9:
        j2 = "가"
    else:
        j2 = "이"

    if int((str(R))[-1]) == 2 or int((str(R))[-1]) == 4 or int((str(R))[-1]) == 5 or int((str(R))[-1]) == 9:
        j3 = "가"
    else:
        j3 = "이"



    if H > M and H > R:
        S = A
        X = "$$수식$$%s$$/수식$$%s 가장 크므로 포도주스 양에 대한 포도 원액 양의 비율이 가장 높은 사람은 %s입니다." % (H, j1, S)
    elif M > H and M > R:
        S = B
        X = "$$수식$$%s$$/수식$$%s 가장 크므로 포도주스 양에 대한 포도 원액 양의 비율이 가장 높은 사람은 %s입니다." % (M, j2, S)
    elif R > H and R > M:
        S = C
        X = "$$수식$$%s$$/수식$$%s 가장 크므로 포도주스 양에 대한 포도 원액 양의 비율이 가장 높은 사람은 %s입니다." % (R, j3, S)



    if E == G and D == F:
        sent_a = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ $$수식$$%s over %s ` = ` %s$$/수식$$\n" % (A, E, D, H)
    else:
        sent_a = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ $$수식$$%s over %s ` = ` %s over %s ` = ` %s$$/수식$$\n" % (A, E, D, G, F, H)

    if J == L and I == K:
        sent_b = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ $$수식$$%s over %s ` = ` %s$$/수식$$\n" % (B, J, I, M)
    else:
        sent_b = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ $$수식$$%s over %s ` = ` %s over %s ` = ` %s$$/수식$$\n" % (B, J, I, L, K, M)

    if O == Q and N == P:
        sent_c = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ $$수식$$%s over %s ` = ` %s$$/수식$$\n" % (C, O, N, R)
    else:
        sent_c = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ $$수식$$%s over %s ` = ` %s over %s ` = ` %s$$/수식$$\n" % (C, O, N, Q, P, R)


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, J=J, I=I, O=O, N=N)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, M=M, O=O, P=P, Q=Q, R=R, X=X, N=N, sent_a=sent_a, sent_b=sent_b, sent_c=sent_c)

    return stem, answer, comment














#6-1-4-44
def ratandpro614_Stem_025():
    stem = "비율을 백분율로 바르게 나타낸 것은 어느 것인가요?\n$$표$$㉠ {a}%  ㉡ {b}%\n㉢ {c}%  ㉣ {d}%$$/표$$\n"
    answer = "(정답)\n{L}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${a1} LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n" \
              "㉡ $$수식$${b1} LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n" \
              "㉢ $$수식$${c1} LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n" \
              "㉣ $$수식$${d1} LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 비율을 백분율로 바르게 나타낸 것은 {L}입니다.\n\n"


    A = np.random.randint(10, 50)
    B = np.random.randint(11, 100)
    C = round(B/10, 2)

    D = np.random.randint(1, 20)
    E = 5*D
    G = np.random.randint(101, 1000)

    F = round(G/10)
    H = round(F/10, 2)
    I = 2*A
    J = 10*B
    K = 5*D

    a = "$$수식$$%s over 50$$/수식$$ → $$수식$$%s$$/수식$$" % (A, A)
    b = "$$수식$$%s$$/수식$$ → $$수식$$%s$$/수식$$" % (C, B)
    c = "$$수식$$%s over 20$$/수식$$ → $$수식$$%s$$/수식$$" % (D, E)
    d = "$$수식$$%s$$/수식$$ → $$수식$$%s$$/수식$$" % (H, F)

    aa = a
    bb = b
    cc = c
    dd = d

    N = [a, b, c, d]
    np.random.shuffle(N)
    a, b, c, d = N

    if (a == cc):
        L = "㉠"
    elif(b == cc):
        L = "㉡"
    elif(c == cc):
        L = "㉢"
    else:
        L = "㉣"

    if (a == aa):
        a1 = "{%s} over 50 `` TIMES 100 ` = ` {%s}" % (A,I)
    elif(a == bb):
        a1 = "{%s} TIMES 100 ` = ` {%s}" % (C,J)
    elif(a == cc):
        a1 = "{%s} over 20 `` TIMES 100 ` = ` {%s}" % (D,K)
    else:
        a1 = "{%s} TIMES 100 ` = ` {%s}" % (H, G)

    if (b == aa):
        b1 = "{%s} over 50 `` TIMES 100 ` = ` {%s}" % (A,I)
    elif(b == bb):
        b1 = "{%s} TIMES 100 ` = ` {%s}" % (C,J)
    elif(b == cc):
        b1 = "{%s} over 20 `` TIMES 100 ` = ` {%s}" % (D,K)
    else:
        b1 = "{%s} TIMES 100 ` = ` {%s}" % (H, G)

    if (c == aa):
        c1 = "{%s} over 50 `` TIMES 100 ` = ` {%s}" % (A,I)
    elif(c == bb):
        c1 = "{%s} TIMES 100 ` = ` {%s}" % (C,J)
    elif(c == cc):
        c1 = "{%s} over 20 `` TIMES 100 ` = ` {%s}" % (D,K)
    else:
        c1 = "{%s} TIMES 100 ` = ` {%s}" % (H, G)

    if (d == aa):
        d1 = "{%s} over 50 `` TIMES 100 ` = ` {%s}" % (A,I)
    elif(d == bb):
        d1 = "{%s} TIMES 100 ` = ` {%s}" % (C,J)
    elif(d == cc):
        d1 = "{%s} over 20 `` TIMES 100 ` = ` {%s}" % (D,K)
    else:
        d1 = "{%s} TIMES 100 ` = ` {%s}" % (H, G)

    stem = stem.format(a=a,b=b,c=c,d=d)
    answer = answer.format(L=L)
    comment = comment.format(L=L,a1=a1,b1=b1,c1=c1,d1=d1)

    return stem, answer, comment


















#6-1-4-45
def ratandpro614_Stem_026():
    stem = "비율을 소수로 고치고 백분율로 나타내어 보세요.\n$$표$$$$수식$${A} over 20 ` = ` {box1}$$/수식$$, 백분율 : $$수식$${box2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${C}$$/수식$$, $$수식$${B}$$/수식$$%\n"
    comment = "(해설)\n" \
              "$$수식$${A} over 20 ` = ` {a} over {b} ` = ` {B} over 100 ` = ` {C}$$/수식$$\n" \
              "→ $$수식$${C} TIMES 100 ` = ` {B} LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n\n"


    A = np.random.randint(1, 20)
    B = 5*A
    C = B/100

    box1 = "%s" % "①"
    box2 = "%s" % "②"

    a = "{{%s} TIMES 5}" % (A)
    b = "{20 TIMES 5}"

    stem = stem.format(A=A, box1=box1, box2=box2)
    answer = answer.format(C=C, B=B)
    comment = comment.format(A=A, B=B, C=C, a=a, b=b)

    return stem, answer, comment

















#6-1-4-46
def ratandpro614_Stem_027():
    stem = "비율을 비교하여 ○안에 알맞은 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 써넣으세요.\n$$수식$${D}$$/수식$$  ○  $$수식$${B}$$/수식$$%\n"
    answer = "(정답)\n$$수식$${E}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${D} TIMES 100 ` = ` {A} LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${A}$$/수식$$%$$수식$$` {E} ` {B}$$/수식$$%이므로 $$수식$${D} ` {E} ` {B}$$/수식$$%입니다.\n\n"


    A = np.random.randint(1, 100)
    B = np.random.randint(1, 100)
    D = A/100

    if (A>B):
        E = "&gt;"
    elif(A==B):
        E = "="
    else:
        E = "&lt;"

    stem = stem.format(D=D, B=B)
    answer = answer.format(E=E)
    comment = comment.format(A=A, B=B, D=D, E=E)

    return stem, answer, comment



















#6-1-4-47
def ratandpro614_Stem_028():
    stem = "백분율을 분수와 소수로 각각 나타내어 보세요.\n$$표$$$$수식$${A}$$/수식$$%$$/표$$\n"
    answer = "(정답)\n$$수식$${A} over 100$$/수식$$, $$수식$${C}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$% → $$수식$${A} TIMES {B} ` = ` {A} over 100$$/수식$$\n" \
              "→ $$수식$${A} DIV 100 ` = ` {C}$$/수식$$\n\n"


    while 1:
        A = np.random.randint(1, 100)
        if gcd(A, 100) == 1:
            break
    C = A/100

    B = "{1 over 100}"

    stem = stem.format(A=A)
    answer = answer.format(A=A, C=C)
    comment = comment.format(A=A, C=C, B=B)

    return stem, answer, comment
















#6-1-4-48
def ratandpro614_Stem_029():
    stem = "전체 피자 양에 대한 선아가 먹은 피자 양의 비율은 $$수식$${A}$$/수식$$입니다. 전체 피자 양에 대한 선아가 먹은 피자 양의 비율을 백분율로 나타내면 몇 %인가요?\n"
    answer = "(정답)\n$$수식$${E}$$/수식$$%\n"
    comment = "(해설)\n" \
              "$$수식$${B} over 8 ` = ` {b} over {s} ` = ` {C} over 1000 ` = ` {D} over 100 ` = ` {E} LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 전체 피자 양에 대한 선아가 먹은 피자 양의 비율을 백분율로 나타내면 $$수식$${E}$$/수식$$%입니다.\n\n"

    Blist = [1,3,5,7]
    B = random.choice(Blist)
    A = "{%s} over 8" % (B)

    C = 125*B
    D = C/10
    E = D

    b = "{{%s} TIMES 125}" % (B)
    s = "{8 TIMES 125}"

    stem = stem.format(A=A)
    answer = answer.format(E=E)
    comment = comment.format(B=B, s=s, C=C, D=D, E=E, b=b)

    return stem, answer, comment


















#6-1-4-50
def ratandpro614_Stem_030():
    stem = "공장에서 인형을 $$수식$${A}$$/수식$$개 만들 때 불량품이 $$수식$${B}$$/수식$$개 나온다고 합니다. 전체 인형 수에 대한 불량품 수의 비율을 백분율로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${E}$$/수식$$%\n"
    comment = "(해설)\n" \
              "전체 인형 수에 대한 불량품 수의 비율은 $$수식$${B} over {A} ` = ` {D} over {C}$$/수식$$입니다.\n" \
              "→ $$수식$${F} TIMES 100 ` = ` {E} LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n\n"


    while(1):
        A = np.random.randint(100, 1000)
        B = np.random.randint(1, A)
        aa = fractions.Fraction(B, A)
        D = aa.numerator
        C = aa.denominator

        Z = [2, 4, 5, 10, 20, 25, 50, 100]
        if C in Z:
            break

    E = 100*aa
    F = "{%s} over {%s}" % (D, C)

    stem = stem.format(A=A, B=B)
    answer = answer.format(E=E)
    comment = comment.format(A=A, D=D, C=C, B=B, E=E, F=F)

    return stem, answer, comment



















#6-1-4-51
def ratandpro614_Stem_031():
    stem = "퀴즈 대회에서 어떤 문제를 $$수식$$1$$/수식$$반 학생 $$수식$${A}$$/수식$$명 중 $$수식$${B}$$/수식$$명이 맞혔고, $$수식$$2$$/수식$$반 학생 $$수식$${C}$$/수식$$명 중 $$수식$${D}$$/수식$$명이 맞혔습니다. 반 학생 수에 대한 문제를 맞힌 학생 수의 비율을 백분율로 나타내었을 때 어느 반이 더 높은가요?\n"
    answer = "(정답)\n$$수식$${K}$$/수식$$반\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT [ 1$$/수식$$반$$수식$$RIGHT ]$$/수식$$ 반 학생 수에 대한 문제를 맞힌 학생 수의 비율 → $$수식$${B} over {A}$$/수식$$ → $$수식$${f} TIMES 100 ` = ` {G} LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT [ 2$$/수식$$반$$수식$$RIGHT ]$$/수식$$ 반 학생 수에 대한 문제를 맞힌 학생 수의 비율 → $$수식$${D} over {C}$$/수식$$ → $$수식$${i} TIMES 100 ` = ` {J} LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n" \
              "→ {X}\n\n"


    while 1:
        A = np.random.randint(20, 41)
        B = np.random.randint(1, A)
        C = np.random.randint(20, 41)
        D = np.random.randint(1, C)
        aa = fractions.Fraction(B, A)

        F = aa.numerator
        E = aa.denominator

        bb = fractions.Fraction(D, C)
        I = bb.numerator
        H = bb.denominator

        G = 100*aa
        J = 100*bb

        Z = [2, 4, 5, 10, 20, 25, 50, 100]
        if A != C and B != D:
            if aa != bb:
                if E in Z:
                    if H in Z:
                        break

    if G < J:
        K = 2
        X = "$$수식$$%s &lt; %s$$/수식$$이므로 $$수식$$2$$/수식$$반이 더 높습니다." % (G, J)
    else:
        K = 1
        X = "$$수식$$%s &gt; %s$$/수식$$이므로 $$수식$$1$$/수식$$반이 더 높습니다." % (G, J)

    f = "{%s} over {%s}" % (F,E)
    i = "{%s} over {%s}" % (I,H)

    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(K=K)
    comment = comment.format(A=A, D=D, C=C, B=B, G=G, f=f, i=i, J=J, X=X)

    return stem, answer, comment

















#6-1-4-52
def ratandpro614_Stem_032():
    stem = "다음에서 비율이 가장 높은 것과 가장 낮은 것을 각각 찾아 차례대로 기호를 써 보세요.\n$$표$$㉠ {a}  ㉡ {b}  ㉢ {c}$$/표$$\n"
    answer = "(정답)\n{G}, {H}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${a1} `` LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n" \
              "㉡ $$수식$${b1} `` LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n" \
              "㉢ $$수식$${c1} `` LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${x} &gt; {y} &gt; {z}$$/수식$$이므로 비율이 가장 높은 것은 {G}, 비율이 가장 낮은 것은 {H}입니다.\n\n"


    while(1):
        A = np.random.randint(10, 100)
        E = np.random.randint(10, 100)
        C = [2, 4, 5, 10, 20, 25, 50, 100][np.random.randint(0, 8)]

        D = np.random.randint(10, 100)
        B = E/100
        F = math.floor((D/C)*100)

        if D < C:
            if gcd(D, C) == 1:
                break


    a = "$$수식$$%s$$/수식$$" % (A)
    a = a + "%"
    b = "$$수식$$%s$$/수식$$" % (B)
    c = "$$수식$$%s over %s$$/수식$$" % (D, C)

    aa = a
    bb = b
    cc = c


    N = [a, b, c]
    np.random.shuffle(N)
    a, b, c = N

    G = ""
    H = ""
    x = ""
    y = ""
    z = ""

    if(A>E and A>F and E>F):
        x = A
        y = E
        z = F
        if(a == aa):
            G = "㉠"
        elif(b == aa):
            G = "㉡"
        else:
            G = "㉢"

        if (a == cc):
            H = "㉠"
        elif (b == cc):
            H = "㉡"
        else:
            H = "㉢"

    elif(A>E and A>F and F>E):
        x = A
        y = F
        z = E
        if (a == aa):
            G = "㉠"
        elif (b == aa):
            G = "㉡"
        else:
            G = "㉢"

        if (a == bb):
            H = "㉠"
        elif (b == bb):
            H = "㉡"
        else:
            H = "㉢"

    elif(E>A and E>F and A>F):
        x = E
        y = A
        z = F
        if (a == bb):
            G = "㉠"
        elif (b == bb):
            G = "㉡"
        else:
            G = "㉢"

        if (a == cc):
            H = "㉠"
        elif (b == cc):
            H = "㉡"
        else:
            H = "㉢"

    elif(E>A and E>F and F>A):
        x = E
        y = F
        z = A
        if (a == bb):
            G = "㉠"
        elif (b == bb):
            G = "㉡"
        else:
            G = "㉢"

        if (a == aa):
            H = "㉠"
        elif (b == aa):
            H = "㉡"
        else:
            H = "㉢"

    elif(F>A and F>E and A>E):
        x = F
        y = A
        z = E
        if (a == cc):
            G = "㉠"
        elif (b == cc):
            G = "㉡"
        else:
            G = "㉢"

        if (a == bb):
            H = "㉠"
        elif (b == bb):
            H = "㉡"
        else:
            H = "㉢"

    elif(F>A and F>E and E>A):
        x = F
        y = E
        z = A
        if (a == cc):
            G = "㉠"
        elif (b == cc):
            G = "㉡"
        else:
            G = "㉢"

        if (a == aa):
            H = "㉠"
        elif (b == aa):
            H = "㉡"
        else:
            H = "㉢"

    ZZ = "{%s} over {%s}" % (D, C)

    if (a == aa):
        a1 = "{%s}" % (A)
    elif (a == bb):
        a1 = "{%s} ` = ` {%s} TIMES 100 ` = ` {%s}" % (B, B, E)
    elif (a == cc):
        a1 = "{%s} `` TIMES 100 ` = ` {%s}" % (ZZ, F)

    if (b == aa):
        b1 = "{%s}" % (A)
    elif (b == bb):
        b1 = "{%s} ` = ` {%s} TIMES 100 ` = ` {%s}" % (B, B, E)
    elif (b == cc):
        b1 = "{%s} `` TIMES 100 ` = ` {%s}" % (ZZ, F)

    if (c == aa):
        c1 = "{%s}" % (A)
    elif (c == bb):
        c1 = "{%s} ` = ` {%s} TIMES 100 ` = ` {%s}" % (B, B, E)
    elif (c == cc):
        c1 = "{%s} `` TIMES 100 ` = ` {%s}" % (ZZ, F)


    stem = stem.format(a=a, b=b, c=c)
    answer = answer.format(G=G, H=H)
    comment = comment.format(a1=a1, b1=b1, c1=c1, x=x, y=y, z=z, G=G, H=H)

    return stem, answer, comment
























#6-1-4-54
def ratandpro614_Stem_033():
    stem = "소금물 양에 대한 소금 양의 비율이 $$수식$${A}$$/수식$$%인 $$수식$$100 rm g$$/수식$$에 물 $$수식$${B} rm g$$/수식$$을 더 넣었습니다. 새로 만든 소금물에서 소금물 양에 대한 소금 양의 비율은 몇 %인가요?\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$%\n"
    comment = "(해설)\n" \
               "$$수식$${A}$$/수식$$%을 분수로 나타내면 $$수식$${A} over 100$$/수식$$이므로 소금물 $$수식$$100 rm g$$/수식$$에 녹아 있는 소금의 양은 $$수식$${A} rm g$$/수식$$입니다.\n" \
              "새로 만든 소금물의 양은 $$수식$$100 ` + ` {B} ` = ` {C} ` LEFT ( ` rm g ` RIGHT )$$/수식$$이므로 새로 만든 소금물에서 소금물 양에 대한 소금 양의 비율은 " \
              "$$수식$${a} TIMES 100 ` = ` {f} TIMES 100 ` = ` {D} ` LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    while(1):
        A = np.random.randint(10, 50)
        B = np.random.randint(100, 1000)

        C = B + 100
        dd = fractions.Fraction(A, C)
        F = dd.numerator
        E = dd.denominator
        Z = [2, 4, 5, 10, 20, 25, 50, 100]
        D = 100*dd

        if E in Z:
            if A % 2 == 0 or A % 5 == 0 or A % 6 == 0:
                break

    a = "{%s} over {%s}" % (A, C)
    f = "{%s} over {%s}" % (F, E)

    stem = stem.format(A=A, B=B)
    answer = answer.format(D=D)
    comment = comment.format(A=A, B=B, C=C, a=a, f=f, D=D)

    return stem, answer, comment
















#6-1-4-56
def ratandpro614_Stem_034():
    stem = "{who}가 {place}에 갔습니다. {place}의 입장료는 $$수식$${A}$$/수식$$원인데 {who}는 할인권을 이용하여 입장료 $$수식$${B}$$/수식$$원을 냈습니다. {who}는 입장료 중 몇 % 할인받은 것인가요?\n"
    answer = "(정답)\n$$수식$${F}$$/수식$$%\n"
    comment = "(해설)\n" \
              "할인 받은 금액은 $$수식$${A} ` - ` {B} ` = ` {C} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$이므로\n" \
              "$$수식$$LEFT ($$/수식$$할인율$$수식$$RIGHT ) ` = ` {c} ` TIMES ` 100 ` = ` {e} ` TIMES ` 100 ` = ` {F} ` LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    who = ["현수", "하나", "세라", "지호", "석희", "윤수", "은지", "홍기", "보배", "은채", "광태", "진표"][np.random.randint(0, 12)]
    place = ["미술관", "박물관", "동물원", "영화관", "전시회"][np.random.randint(0, 5)]

    while 1:
        G = np.random.randint(10, 100)
        A = 1000*G
        H = np.random.randint(10, 100)
        B = 1000*H
        C = A - B
        aa = fractions.Fraction(C, A)
        E = aa.numerator
        D = aa.denominator

        Z = [2, 4, 5, 10, 20, 25, 50, 100]
        F = 100*aa

        if D in Z:
            if H < G:
                break

    c = "{%s} over {%s}" % (C, A)
    e = "{%s} over {%s}" % (E, D)

    stem = stem.format(A=A, B=B, who=who, place=place)
    answer = answer.format(F=F)
    comment = comment.format(A=A, B=B, C=C, c=c, e=e, F=F)

    return stem, answer, comment



















#6-1-4-57
def ratandpro614_Stem_035():
    stem = "{who1}네 반 회장 선거에서 $$수식$${A}$$/수식$$명이 투표에 참여했습니다. {who1}는 $$수식$${B}$$/수식$$표를 얻었고, {who2}는 $$수식$${C}$$/수식$$표를 얻었습니다. {who1}와 {who2}의 득표율은 각각 몇 %인지 순서대로 쓰세요.\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$%, $$수식$${E}$$/수식$$%\n"
    comment = "(해설)\n" \
              "득표율을 각각 구해보면\n" \
              "{who1} : $$수식$${b} TIMES 100 {word_g} ` = ` {D} ` LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n"\
              "{who2} : $$수식$${c} TIMES 100 {word_i} ` = ` {E} ` LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n\n"


    while True:
        who1 = ["서주", "지우", "현수", "하나", "세라", "대호", "석희", "윤수", "은지", "홍기", "보배", "은채", "광태", "진표"][np.random.randint(0, 14)]
        who2 = ["서주", "지우", "현수", "하나", "세라", "대호", "석희", "윤수", "은지", "홍기", "보배", "은채", "광태", "진표"][np.random.randint(0, 14)]
        if who1 != who2:
            break

    while 1:
        A = np.random.randint(20, 51)
        B = np.random.randint(1, A)
        C = A - B

        aa = fractions.Fraction(B, A)
        G = aa.numerator
        F = aa.denominator

        bb = fractions.Fraction(C, A)
        I = bb.numerator
        H = bb.denominator

        Z = [2, 4, 5, 10, 20, 25, 50, 100]
        D = 100*aa
        E = 100*bb

        if F in Z:
            if H in Z:
                if A % 5 == 0:
                    break


    b = "{%s} over {%s}" % (B, A)
    c = "{%s} over {%s}" % (C, A)
    g = "{%s} over {%s}" % (G, F)
    i = "{%s} over {%s}" % (I, H)


    if A == F:
        word_g = ""
    else:
        word_g = f"` = ` {g} TIMES 100"

    if A == H:
        word_i = ""
    else:
        word_i = f"` = ` {i} TIMES 100"

    stem = stem.format(A=A, B=B, C=C, who1=who1, who2=who2)
    answer = answer.format(D=D, E=E, who1=who1, who2=who2)
    comment = comment.format(b=b, c=c, g=g, i=i, D=D, E=E, who1=who1, who2=who2, word_g=word_g, word_i=word_i)

    return stem, answer, comment
















#6-1-4-58
def ratandpro614_Stem_036():
    stem = "어느 공장에서 인형을 $$수식$${A}$$/수식$$개 만들 때 불량품이 $$수식$${B}$$/수식$$개 나온다고 합니다. 전체 인형 수에 대한 불량품 수의 비율은 몇 %인가요?\n"
    answer = "(정답)\n$$수식$${E}$$/수식$$%\n"
    comment = "(해설)\n" \
              "전체 인형 수에 대한 불량품 수의 비\n" \
              "→ $$수식$${B}$$/수식$$:$$수식$${A}$$/수식$$ → $$수식$$LEFT ($$/수식$$비율$$수식$$RIGHT ) = {B} over {A}$$/수식$$\n"\
              "→ $$수식$${a} TIMES 100 ` = ` {d} TIMES 100 ` = ` {E} ` LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n\n"


    while 1:
        A = np.random.randint(500, 2001)
        B = np.random.randint(10, A)

        aa = fractions.Fraction(B, A)
        D = aa.numerator
        C = aa.denominator

        E = 100*aa

        Z = [2, 4, 5, 10, 20, 25, 50, 100]

        if C in Z:
            if A % 5 == 0:
                break

    a = "{%s} over {%s}" % (B, A)
    d = "{%s} over {%s}" % (D, C)

    stem = stem.format(A=A, B=B)
    answer = answer.format(E=E)
    comment = comment.format(a=a, d=d, A=A, B=B, E=E)

    return stem, answer, comment



















#6-1-4-59
def ratandpro614_Stem_037():
    stem = " {who}는 태권도 경기를 $$수식$${A}$$/수식$$번 하여 그 중 $$수식$${B}$$/수식$$경기를 졌습니다. {who}의 승률은 몇 %인가요?\n"
    answer = "(정답)\n$$수식$${F}$$/수식$$%\n"
    comment = "(해설)\n" \
              "전체 경기 수 : $$수식$${A}$$/수식$$번,\n" \
              "이긴 경기 수 : $$수식$${A} ` - ` {B} ` = ` {C} ` LEFT ($$/수식$$번$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 승률은 $$수식$${formu} ` = ` {F} ` LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$입니다.\n\n"



    who = ["선아", "서주", "지우", "현수", "하나", "세라", "대호", "석희", "윤수", "은지", "홍기", "보배", "은채", "광태", "진표"][np.random.randint(0, 15)]

    while 1:
        A = np.random.randint(10, 51)
        B = np.random.randint(1, A)
        C = A - B

        aa = fractions.Fraction(C, A)
        E = aa.numerator
        D = aa.denominator

        F = 100*aa

        Z = [2, 4, 5, 10, 20, 25, 50, 100]

        if D in Z:
            break

    a = "{%s} over {%s}" % (C, A)
    e = "{%s} over {%s}" % (E, D)

    if a == e:
        formu = "%s TIMES 100" % a
    else:
        formu = "%s TIMES 100 ` = ` %s TIMES 100" % (a, e)

    stem = stem.format(A=A, B=B, who=who)
    answer = answer.format(F=F)
    comment = comment.format(A=A, B=B, C=C, a=a, e=e, F=F, formu=formu)

    return stem, answer, comment


















#6-1-4-60
def ratandpro614_Stem_038():
    stem = "{A}는 설탕 $$수식$${C} rm g$$/수식$$을 녹여 설탕물 $$수식$${D} rm g$$/수식$$을 만들었고, {B}는 설탕 $$수식$${E} rm g$$/수식$$을 녹여 설탕물 $$수식$${F} rm g$$/수식$$을 만들었습니다. 누가 만든 설탕물이 더 진한가요?\n"
    answer = "(정답)\n{M}\n"
    comment = "(해설)\n" \
              "{A} : 설탕의 양 $$수식$${C} rm g$$/수식$$, 설탕물의 양 $$수식$${D} rm g$$/수식$$\n" \
              "→ $$수식$${c} TIMES 100 ` = ` {g} TIMES 100 ` = ` {I} ` LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n" \
              "{B} : 설탕의 양 $$수식$${E} rm g$$/수식$$, 설탕물의 양 $$수식$${F} rm g$$/수식$$\n" \
              "→ $$수식$${e} TIMES 100 ` = ` {j} TIMES 100 ` = ` {L} ` LEFT ($$/수식$$%$$수식$$RIGHT )$$/수식$$\n" \
              "{X}\n\n"


    # while 1:
    #     N = ["정미", "은주", "지희", "호수"]
    #     A, B = np.random.choice(N, 2)
    #
    #     C = np.random.randint(10, 100)
    #     E = np.random.randint(10, 100)
    #     D = np.random.randint(100, 1000)
    #     F = np.random.randint(100, 1000)
    #
    #     aa = fractions.Fraction(C, D)
    #     G = aa.numerator
    #     H = aa.denominator
    #
    #     bb = fractions.Fraction(E, F)
    #     J = bb.numerator
    #     K = bb.denominator
    #
    #     I = 100*aa
    #     L = 100*bb
    #
    #     Z = [2, 4, 5, 10, 20, 25, 50, 100]
    #
    #     if K in Z:
    #         if H in Z:
    #             if A != B and C != E and D != F and aa != bb:
    #                 break


    # 위 공식은 계산이 너무 느림

    while True:
        A = ["정미", "은주", "지희", "호수"][np.random.randint(0, 4)]
        B = ["정미", "은주", "지희", "호수"][np.random.randint(0, 4)]
        if A != B:
            break

    while True:
        Z = [2, 4, 5, 10, 20, 25, 50, 100]

        H = Z[np.random.randint(0, 8)]
        K = Z[np.random.randint(0, 8)]

        G = np.random.randint(1, H)
        J = np.random.randint(1, K)

        mu1 = np.random.randint(2, 500)
        mu2 = np.random.randint(2, 500)

        D = mu1*H
        F = mu2*K

        C = mu1*G
        E = mu2*J

        I = 100 * G / H

        if I - (I // 1) == 0:
            I = round(I)

        L = 100 * J / K

        if L - (L // 1) == 0:
            L = round(L)

        if H != K and gcd(G, H) == 1 and gcd(J, K) == 1 and 9 < C and C < 100 and 99 < D and D < 1000 and 9 < E and E < 100 and 99 < F and F < 1000 and C != E and D != F:
            if D % 10 == 0 and F % 10 == 0 and I != L:
                break


    c = "{%s} over {%s}" % (C, D)
    g = "{%s} over {%s}" % (G, H)
    e = "{%s} over {%s}" % (E, F)
    j = "{%s} over {%s}" % (J, K)

    if I < L:
        M = B
        X = "$$수식$$%s &lt; %s$$/수식$$이므로 %s가 만든 설탕물이 더 진합니다." % (I, L, B)
    else:
        M = A
        X = "$$수식$$%s &gt; %s$$/수식$$이므로 %s가 만든 설탕물이 더 진합니다." % (I, L, A)

    stem = stem.format(A=A, C=C, D=D, B=B, E=E, F=F)
    answer = answer.format(M=M)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, c=c, g=g, e=e, j=j, I=I, L=L, X=X)

    return stem, answer, comment






