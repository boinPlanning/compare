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








# 3-1-1-02
def addandsub311_Stem_001():
    stem = "$$수식$${n1}$$/수식$$ 보다 $$수식$${n2}$$/수식$$ 더 큰 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${n3}$$/수식$$\n"
    comment = "(해설)\n$$수식$${n1}$$/수식$$ 보다 $$수식$${n2}$$/수식$$ 더 큰 수는 $$수식$${n1} + {n2}$$/수식$$  {j1} 계산합니다.\n" \
              "$$수식$${nn1}``{nn2}``{nn3}``+``{nn4}``{nn5}``{nn6}``=``{nn7}``{nn8}``{nn9}$$/수식$$\n" \

    while(1):
        while(1):
            nn1 = np.random.randint(1, 10)
            nn2 = np.random.randint(0, 10)
            nn3 = np.random.randint(0, 10)
            if(nn1!=nn2 or nn2 != nn3 or nn1 != nn3):
                if(nn2 != 0 and nn3 !=0):
                    break

        while(1):
            nn4 = np.random.randint(1, 10)
            nn5 = np.random.randint(0, 10)
            nn6 = np.random.randint(0, 10)
            if (nn4 != nn5 or nn4 != nn6 or nn5 != nn6):
                if (nn5 != 0 and nn6 != 0):
                    break

        nn7 = nn1+nn4
        nn8 = nn2+nn5
        nn9 = nn3+nn6
        n1 = nn1 * 100 + nn2 * 10 + nn3
        n2 = nn4 * 100 + nn5 * 10 + nn6
        n3 = nn7 * 100 + nn8 * 10 + nn9
        if(nn7 < 10 and nn8 < 10 and nn9 <10 ):
            if(n1 != n2):
                break

    j1 = proc_jo(n2, 1)

    stem = stem.format(n1=n1, n2=n2)
    answer = answer.format(n3=n3)
    comment = comment.format(n1=n1, n2=n2, n3=n3, nn1=nn1, nn2=nn2, nn3=nn3, nn4=nn4, nn5=nn5, nn6=nn6, nn7=nn7, nn8=nn8, nn9=nn9, j1=j1)

    return stem, answer, comment







# 3-1-1-03
def addandsub311_Stem_002():
    stem = "계산 결과를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$ 를 알맞게 써넣으세요.\n$$수식$${A}+{B}$$/수식$$  ○  $$수식$${C}+{D}$$/수식$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a1}``{a2}``{a3}``+``{b1}``{b2}``{b3}``=``{ta1}``{ta2}``{ta3}$$/수식$$\n"\
              "$$수식$${c1}``{c2}``{c3}``+``{d1}``{d2}``{d3}``=``{tb1}``{tb2}``{tb3}$$/수식$$\n"\
              "따라서 $$수식$${TA1}$$/수식$$ {j1} $$수식$${TB1}$$/수식$${S1}므로 $$수식$${TA1}$$/수식$$ $$수식$${S}$$/수식$$ $$수식$${TB1}$$/수식$$ 입니다.\n\n"


    while(1):
        while(1):
            a1 = np.random.randint(1, 10)
            a2 = np.random.randint(0, 10)
            a3 = np.random.randint(0, 10)
            if(a1!=a2 or a2 != a3 or a1 != a3):
                if(a2 != 0 and a3 !=0):
                    break

        while(1):
            b1 = np.random.randint(1, 10)
            b2 = np.random.randint(0, 10)
            b3 = np.random.randint(0, 10)
            if (b1 != b2 or b2 != b3 or b1 != b3):
                if (b2 != 0 and b3 != 0):
                    break

        while (1):
            c1 = np.random.randint(1, 10)
            c2 = np.random.randint(0, 10)
            c3 = np.random.randint(0, 10)
            if (c1 != c2 or c2 != c3 or c1 != c3):
                if (c2 != 0 and c3 != 0):
                    break

        while (1):
            d1 = np.random.randint(1, 10)
            d2 = np.random.randint(0, 10)
            d3 = np.random.randint(0, 10)
            if (d1 != d2 or d2 != d3 or d1 != d3):
                if (d2 != 0 and d3 != 0):
                    break

        A = a1*100 + a2*10 + a3
        B = b1*100 + b2*10 + b3
        C = c1*100 + c2*10 + c3
        D = d1*100 + d2*10 + d3

        ta1 = a1 + b1
        ta2 = a2 + b2
        ta3 = a3 + b3

        tb1 = c1 + d1
        tb2 = c2 + d2
        tb3 = c3 + d3

        if(A!=B and A!=C and A!=D and B!=C and B!=D and C!=D):
            if(ta1 < 10 and ta2 < 10 and ta3 < 10 and tb1 < 10 and tb2 < 10 and tb3 < 10):
                break


    TA1 = ta1*100 + ta2*10 + ta3
    TB1 = tb1*100 + tb2*10 + tb3

    j1 = proc_jo(TA1, -1)
    j2 = proc_jo(TB1, 2)


    if (TA1-TB1) > 0:
        S = "$$수식$$&gt;$$/수식$$"
        S1 = "보다 크"
    elif (TA1-TB1)<0:
        S = "$$수식$$&lt;$$/수식$$"
        S1 = "보다 작으"
    else:
        S = "="
        S1 = "%s 같으" % j2


    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(S=S)
    comment = comment.format(a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, c1=c1, c2=c2, c3=c3, d1=d1, d2=d2, d3=d3, ta1=ta1, ta2=ta2, ta3=ta3, tb1=tb1, tb2=tb2, tb3=tb3, TA1=TA1, TB1=TB1, S=S, S1=S1, j1=j1)

    return stem, answer, comment


















# 3-1-1-05
def addandsub311_Stem_003():
    stem = "{N} 방문자가 어제는 $$수식$${A}$$/수식$$명, 오늘은 $$수식$${B}$$/수식$$명입니다. 어제와 오늘 이틀 동안의 {N} 방문자는 모두 몇 명인가요?\n"
    answer = "(정답)\n$$수식$${S2}$$/수식$$명\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$어제 방문자 수$$수식$$RIGHT ) + LEFT ($$/수식$$오늘 방문자 수$$수식$$RIGHT )$$/수식$$\n $$수식$$= {A} + {B} = {S2} ` LEFT ( 명 RIGHT )$$/수식$$\n\n"


    while(1):
        N = ["식물원", "동물원", "박물관", "미술관", "전시관"][np.random.randint(0, 5)]

        while (1):
            a1 = np.random.randint(1, 10)
            a2 = np.random.randint(0, 10)
            a3 = np.random.randint(0, 10)
            if (a1 != a2 or a2 != a3 or a1 != a3):
                if (a2 != 0 and a3 != 0):
                    break
        while (1):
            b1 = np.random.randint(1, 10)
            b2 = np.random.randint(0, 10)
            b3 = np.random.randint(0, 10)
            if (b1 != b2 or b2 != b3 or b1 != b3):
                if (b2 != 0 and b3 != 0):
                    break
        s1 = a1 + b1
        s2 = a2 + b2
        s3 = a3 + b3

        A = a1 * 100 + a2 * 10 + a3
        B = b1 * 100 + b2 * 10 + b3

        if(s1 < 10 and s2 < 10 and s3 < 10 and A!= B):
            break

    S2 = s1*100 + s2*10 + s3

    stem = stem.format(A=A, B=B, N=N)
    answer = answer.format(S2=S2)
    comment = comment.format(A=A, B=B, S2=S2)

    return stem, answer, comment





# 3-1-1-06
def addandsub311_Stem_004():
    stem = "계산 결과가 가장 {N}을 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${A} + {B}$$/수식$$    ㉡ $$수식$${C} + {D}$$/수식$$    ㉢ $$수식$${E} + {F}$$/수식$$    $$/표$$\n"
    answer = "(정답)\n{S}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${A} + {B} = {T1}$$/수식$$\n"\
              "㉡ $$수식$${C} + {D} = {T2}$$/수식$$\n" \
              "㉢ $$수식$${E} + {F} = {T3}$$/수식$$\n" \
              "따라서 $$수식$${G} &lt; {H} &lt; {J}$$/수식$$ 이므로 계산 결과가 가장 {N}은 {S} 입니다.\n\n"


    while (1):
        while (1):
            a1 = np.random.randint(1, 10)
            a2 = np.random.randint(0, 10)
            a3 = np.random.randint(0, 10)
            if (a1 != a2 or a2 != a3 or a1 != a3):
                if (a2 != 0 and a3 != 0):
                    break

        while (1):
            b1 = np.random.randint(1, 10)
            b2 = np.random.randint(0, 10)
            b3 = np.random.randint(0, 10)
            if (b1 != b2 or b2 != b3 or b1 != b3):
                if (b2 != 0 and b3 != 0):
                    break

        while (1):
            c1 = np.random.randint(1, 10)
            c2 = np.random.randint(0, 10)
            c3 = np.random.randint(0, 10)
            if (c1 != c2 or c2 != c3 or c1 != c3):
                if (c2 != 0 and c3 != 0):
                    break

        while (1):
            d1 = np.random.randint(1, 10)
            d2 = np.random.randint(0, 10)
            d3 = np.random.randint(0, 10)
            if (d1 != d2 or d2 != d3 or d1 != d3):
                if (d2 != 0 and d3 != 0):
                    break

        while (1):
            e1 = np.random.randint(1, 10)
            e2 = np.random.randint(0, 10)
            e3 = np.random.randint(0, 10)
            if (e1 != e2 or e2 != e3 or e1 != e3):
                if (e2 != 0 and e3 != 0):
                    break

        while (1):
            f1 = np.random.randint(1, 10)
            f2 = np.random.randint(0, 10)
            f3 = np.random.randint(0, 10)
            if (f1 != f2 or f2 != f3 or f1 != a3):
                if (f2 != 0 and f3 != 0):
                    break

        s1 = a1+b1
        s2 = a2+b2
        s3 = a3+b3
        s4 = c1+d1
        s5 = c2+d2
        s6 = c3+d3
        s7 = e1+f1
        s8 = e2+f2
        s9 = e3+f3

        A = a1*100 + a2*10 + a3
        B = b1*100 + b2*10 + b3
        C = c1*100 + c2*10 + c3
        D = d1*100 + d2*10 + d3
        E = e1*100 + e2*10 + e3
        F = f1*100 + f2*10 + f3

        T1 = A+B
        T2 = C+D
        T3 = E+F

        if(s1<10 and s2<10 and s3<10 and s4<10 and s5<10 and s6<10 and s7<10 and s8<10 and s9<10):
            if(A!=B and A!=C and A!=D and A!=E and A!=F and B!=C and B!=D and B!=E and B!=F and C!=D and C!=E and C!=F and D!=E and D!=F and E!=F):
                if T1 != T2 and T1 != T3 and T2 != T3:
                    break


    if(T1>T2):
        if(T1>T3):
            if(T2>T3):
                J = T1
                H = T2
                G = T3
            else:
                J = T1
                H = T3
                G = T2
        else:
            J = T3
            H = T1
            G = T2
    elif(T2>T1):
        if(T3>T1):
            if(T2>T3):
                J = T2
                H = T3
                G = T1
            else:
                J = T3
                H = T2
                G = T1
        else:
            J = T2
            H = T1
            G = T3


    if(J == T1):
        S1 = "㉠"
    elif(J == T2):
        S1 = "㉡"
    else:
        S1 = "㉢"

    if(G==T1):
        S2 = "㉠"
    elif(G==T2):
        S2 = "㉡"
    else:
        S2 = "㉢"

    n = np.random.randint(0, 2)

    if (n == 0):
        N = "작은 것"
        S = S2
    else:
        N = "큰 것"
        S = S1

    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F,N=N)
    answer = answer.format(S=S)
    comment = comment.format(A=A,B=B,C=C,D=D,E=E,F=F,T1=T1,T2=T2,T3=T3,G=G,H=H,J=J,N=N,S=S)

    return stem, answer, comment






# 3-1-1-08
def addandsub311_Stem_005():
    stem = "{N} 합을 구해 보세요.\n$$표$$ $$수식$$````{E}````````{F}````````{G}````````{H}````$$/수식$$    $$/표$$\n"
    answer = "(정답)\n$$수식$${SSS}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ {A}&gt;{C}&gt;{D}&gt;{B} $$/수식$$ 이므로 {X}는 $$수식$${x}$$/수식$$이고, {Y}는 $$수식$${y}$$/수식$$입니다.\n" \
              "$$수식$$LEFT ($$/수식$${X}$$수식$$RIGHT ) + LEFT ($$/수식$${Y}$$수식$$RIGHT ) = {x} + {y} = {SSS}$$/수식$$\n\n"


    while True:
        while (1):
            while (1):
                a1 = np.random.randint(1, 10)
                a2 = np.random.randint(0, 10)
                a3 = np.random.randint(0, 10)
                b1 = np.random.randint(1, 10)
                b2 = np.random.randint(0, 10)
                b3 = np.random.randint(0, 10)
                if (a1 != a2 or a2 != a3 or a1 != a3 or b1 != b2 or b2 != b3 or b1 != b3):
                    if (a2 != 0 and a3 != 0 and b2 != 0 and b3 != 0):
                        if (a1 + b1 >= 10):
                            if ((a2 + b2) < 10) and ((a3 + b3) < 10):
                                break
                        elif(a1+b1<10):
                            if ((a2 + b2) >= 10) and ((a3 + b3) < 10):
                                if(a1+b1 != 9):
                                    break
                            if ((a2 + b2) < 10) and ((a3 + b3) >= 10):
                                if(a2+b2 != 9):
                                    break

            while (1):
                c1 = np.random.randint(1, 10)
                c2 = np.random.randint(0, 10)
                c3 = np.random.randint(0, 10)
                if (c1 != c2 or c2 != c3 or c1 != c3):
                    if (c2 != 0 and c3 != 0):
                        break

            while (1):
                d1 = np.random.randint(1, 10)
                d2 = np.random.randint(0, 10)
                d3 = np.random.randint(0, 10)
                if (d1 != d2 or d2 != d3 or d1 != d3):
                    if (d2 != 0 and d3 != 0):
                        break

            A = a1 * 100 + a2 * 10 + a3
            B = b1 * 100 + b2 * 10 + b3
            C = c1 * 100 + c2 * 10 + c3
            D = d1 * 100 + d2 * 10 + d3

            if (A>C) and (C>D) and (D>B):
                break

        N = [A,B,C,D]

        np.random.shuffle(N)

        E,F,G,H = N

        R = np.random.randint(0,3)

        if(R == 0):
            N = "가장 큰 수와 가장 작은 수의"
            X = "가장 큰 수"
            Y = "가장 작은 수"
            x = A
            y = B
            SSS = A + B
        elif(R == 1):
            N = "두번째로 큰 수와 가장 작은 수의"
            X = "두번째로 큰 수"
            Y = "가장 작은 수"
            x = C
            y = B
            SSS = C + B
        else:
            N = "가장 큰 수와 두번째로 큰 수의"
            X = "가장 큰 수"
            Y = "두번 째로 작은 수"
            x = A
            y = C
            SSS = A + C

        if SSS < 1000 :
            break

    stem = stem.format(E=E, F=F, G=G, H=H, N=N)
    answer = answer.format(SSS=SSS)
    comment = comment.format(A=A, B=B, C=C, D=D, SSS=SSS, X=X, Y=Y, x=x, y=y)

    return stem, answer, comment





# 3-1-1-09
def addandsub311_Stem_006():
    stem = "□ 안에 알맞은 수를 구해 보세요.\n$$표$$ {N}$$수식$$- {A} = {B}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "{N}$$수식$$- {A} = {B}$$/수식$$에서 {N}$$수식$$= {B} + {A} = {S}$$/수식$$\n\n" \


    while (1):
        while (1):
            a1 = np.random.randint(1, 10)
            a2 = np.random.randint(0, 10)
            a3 = np.random.randint(0, 10)
            b1 = np.random.randint(1, 10)
            b2 = np.random.randint(0, 10)
            b3 = np.random.randint(0, 10)
            if (a1 != a2 or a2 != a3 or a1 != a3 or b1 != b2 or b2 != b3 or b1 != b3):
                if (a2 != 0 and a3 != 0 and b2 != 0 and b3 != 0):
                    if (a1 + b1 >= 10):
                        if ((a2 + b2) < 10) and ((a3 + b3) < 10):
                            break
                    elif(a1+b1<10):
                        if ((a2 + b2) >= 10) and ((a3 + b3) < 10):
                            if(a1+b1 != 9):
                                break
                        if ((a2 + b2) < 10) and ((a3 + b3) >= 10):
                            if(a2+b2 != 9):
                                break

        A = a1 * 100 + a2 * 10 + a3
        B = b1 * 100 + b2 * 10 + b3
        N = "□"

        S = A + B

        if (A!=B):
            break

    stem = stem.format(N=N, A=A, B=B)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, N=N, S=S)

    return stem, answer, comment






# 3-1-1-14
def addandsub311_Stem_007():
    stem = "짝수를 모두 찾아 짝수들의 합을 구해 보세요.\n$$표$$ $$수식$${F}````````{G}````````{H}````````{I}````````{J}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n짝수를 모두 찾으면 $$수식$${A}$$/수식$$, $$수식$${B}$$/수식$$ 입니다.\n" \
              "$$수식$$LEFT ( $$/수식$$짝수들의 합$$수식$$ RIGHT ) $$/수식$$  = $$수식$${A}+{B}={S}$$/수식$$\n\n" \

    while (1):
        while (1):
            a1 = np.random.randint(1, 10)
            a2 = np.random.randint(1, 10)
            a3 = np.random.randint(0, 5)
            b1 = np.random.randint(1, 10)
            b2 = np.random.randint(1, 10)
            b3 = np.random.randint(0, 5)
            if (a1 != a2 or a2 != a3 or a1 != a3 or b1 != b2 or b2 != b3 or b1 != b3):
                if (a2 != 0 and a3 != 0 and b2 != 0 and b3 != 0):
                    if(a3 % 2 == 0 and b3 % 2 == 0):
                        if (a1 + b1 >= 10):
                            if ((a2 + b2) < 10) and ((a3 + b3) < 10):
                                break
                        elif (a1 + b1 < 10):
                            if ((a2 + b2) >= 10) and ((a3 + b3) < 10):
                                if (a1 + b1 != 9):
                                    break
                            if ((a2 + b2) < 10) and ((a3 + b3) >= 10):
                                if (a2 + b2 != 9):
                                    break

        while (1):
            c1 = np.random.randint(1, 10)
            c2 = np.random.randint(1, 10)
            c3 = np.random.randint(1, 6)
            if (c1 != c2 or c2 != c3 or c1 != c3):
                break

        while (1):
            d1 = np.random.randint(1, 10)
            d2 = np.random.randint(1, 10)
            d3 = np.random.randint(1, 6)
            if (d1 != d2 or d2 != d3 or d1 != d3):
                break

        while (1):
            e1 = np.random.randint(1, 10)
            e2 = np.random.randint(1, 10)
            e3 = np.random.randint(1, 6)
            if (e1 != e2 or e2 != e3 or e1 != e3):
                break

        A = a1 * 100 + a2 * 10 + a3
        B = b1 * 100 + b2 * 10 + b3
        C = c1 * 100 + c2 * 10 + c3
        D = d1 * 100 + d2 * 10 + d3
        E = e1 * 100 + e2 * 10 + e3

        S = A + B

        if(A!=B):
            if(C!=D and C!=E and D!=E):
                if(c3 % 2 != 0 and d3 % 2 !=0 and e3 % 2 !=0):
                    break

    N = [A, B, C, D, E]

    np.random.shuffle(N)

    F, G, H, I, J = N

    stem = stem.format(F=F, G=G, H=H, I=I, J=J)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, S=S)

    return stem, answer, comment





# 3-1-1-15
def addandsub311_Stem_008():
    stem = "{N}이네 {place}에서 작년에는 {S1}를 {A}개 수확했고, 올해는 작년보다 {B}개 더 많이 수확했습니다. {N}이네 {place}에서 올해에 수확한 {S1}는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$올해에 수확한 {S1} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$ = LEFT ($$/수식$$작년에 수확한 {S1} 수$$수식$$ RIGHT ) + LEFT ( $$/수식$$ 작년보다 더 많이 " \
              "수확한 {S1} 수$$수식$$ RIGHT ) = {A} + {B} = {S}$$/수식$$\n\n"


    while(1):
        while (1):
            N = ["효정", "우진", "형철", "영선", "인영", "민준", "희철", "소율", "은설", "하은"][np.random.randint(0, 10)]
            place = ["농장", "과수원"][np.random.randint(0, 2)]
            if place == "농장" :
                S1 = ["고구마", "감자", "돼지감자", "옥수수", "순무"][np.random.randint(0, 5)]
            else :
                S1 = ["사과", "포도", "배", "복숭아", "자두"][np.random.randint(0, 5)]
            a1 = np.random.randint(1, 10)
            a2 = np.random.randint(0, 10)
            a3 = np.random.randint(0, 10)
            b1 = np.random.randint(1, 10)
            b2 = np.random.randint(0, 10)
            b3 = np.random.randint(0, 10)
            if (a1 != a2 or a2 != a3 or a1 != a3 or b1 != b2 or b2 != b3 or b1 != b3):
                if (a2 != 0 and a3 != 0 and b2 != 0 and b3 != 0):
                    if (a1 + b1 >= 10):
                        if ((a2 + b2) < 10) and ((a3 + b3) < 10):
                            break
                    elif (a1 + b1 < 10):
                        if ((a2 + b2) >= 10) and ((a3 + b3) < 10):
                            if (a1 + b1 != 9):
                                break
                        if ((a2 + b2) < 10) and ((a3 + b3) >= 10):
                            if (a2 + b2 != 9):
                                break

        A = a1 * 100 + a2 * 10 + a3
        B = b1 * 100 + b2 * 10 + b3

        S = A+B

        if(A!=B):
            break


    stem = stem.format(N=N, S1=S1, A=A, B=B, place=place)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, S=S, N=N, S1=S1)

    return stem, answer, comment














# 3-1-1-16
def addandsub311_Stem_009():
    stem = "㉠, ㉡, ㉢에 들어갈 알맞은 숫자를 차례대로 써넣으세요.\n             $$수식$${a1}$$/수식$$  ㉠  ㉡\n  $$수식$$+$$/수식$$      ㉢$$수식$$``{b2}``{b3}$$/수식$$ \n───────\n              $$수식$${c1}``{c2}``{c3}$$/수식$$ \n"
    answer = "(정답)\n$$수식$${S1}$$/수식$$, $$수식$${S2}$$/수식$$, $$수식$${S3}$$/수식$$\n"
    comment = "(해설)\n" \
              "일의 자리 계산은 ㉡$$수식$$+ {b3} = {T1}$$/수식$$에서 ㉡$$수식$$= {S2}$$/수식$$,\n" \
              "십의 자리 계산은 $$수식$$1 +$$/수식$$㉠$$수식$$+ {b2} = {T2}$$/수식$$에서 ㉠$$수식$$= {S1}$$/수식$$,\n" \
              "백의 자리 계산은 $$수식$${a1} +$$/수식$$㉢$$수식$$= {c1}$$/수식$$에서 ㉢$$수식$$= {S3}$$/수식$$ 입니다.\n" \
              "따라서 ㉠ $$수식$${S1}$$/수식$$, ㉡ $$수식$${S2}$$/수식$$, ㉢ $$수식$${S3}$$/수식$$ 입니다.\n\n"


    while(1):
        a1 = np.random.randint(1, 10)
        b2 = np.random.randint(0, 10)
        b3 = np.random.randint(0, 10)
        c1 = np.random.randint(1,10)
        c2 = np.random.randint(0,10)
        c3 = np.random.randint(0,10)
        if (c1 != c2 or c2 != c3 or c1 != c3):
            if (c2 != 0 and c3 != 0):
                if(c1 > a1 and c2 > 1 + b2 and c3 < b3):
                    break

    T1 = 10 + c3
    T2 = c2

    S1 = c2-1-b2
    S2 = 10+c3-b3
    S3 = c1-a1

    stem = stem.format(a1=a1, b2=b2, b3=b3, c1=c1, c2=c2, c3=c3)
    answer = answer.format(S1=S1,S2=S2, S3=S3)
    comment = comment.format(b3=b3, T1=T1, S2=S2, b2=b2, T2=T2, S1=S1, a1=a1, c1=c1, S3=S3)

    return stem, answer, comment




















# 3-1-1-19
def addandsub311_Stem_010():
    stem = "두 수의 합을 구해 보세요.\n$$표$$ $$수식$${A}$$/수식$$  $$수식$${B}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a1}``{a2}``{a3}``+``{b1}``{b2}``{b3}``=``{s1}``{s2}``{s3}$$/수식$$ \n" \

    while(1):
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(1, 10)
        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(1, 10)
        b3 = np.random.randint(1, 10)
        if(a1 != a2 or a2 != a3 or a1 != a3):
            if(a1+b1 < 9 and a2+b2 >9 and a3+b3 > 10):
                break

    A = a1*100+a2*10+a3
    B = b1*100+b2*10+b3

    s1 = 1+a1+b1
    s2 = 1+a2+b2-10
    s3 = a3+b3-10

    S = s1*100+s2*10+s3

    stem = stem.format(A=A, B=B)
    answer = answer.format(S=S)
    comment = comment.format(a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, s1=s1, s2=s2, s3=s3)

    return stem, answer, comment















# 3-1-1-20
def addandsub311_Stem_011():
    stem = "계산 결과를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$ 를 알맞게 써넣으세요.\n$$수식$${A} + {B}$$/수식$$  ○  $$수식$${C} + {D}$$/수식$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a1}``{a2}``{a3}``+``{b1}``{b2}``{b3}``=``{s1}``{s2}``{s3}$$/수식$$ \n" \
              "$$수식$${c1}``{c2}``{c3}``+``{d1}``{d2}``{d3}``=``{t1}``{t2}``{t3}$$/수식$$ \n" \
              "따라서 $$수식$${T1}$$/수식$${j1} $$수식$${T2}$$/수식$${S1}므로 $$수식$${T1} {S} {T2}$$/수식$$ 입니다.\n\n"


    while(1):
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(1, 10)
        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(1, 10)
        b3 = np.random.randint(1, 10)
        c1 = np.random.randint(1, 10)
        c2 = np.random.randint(1, 10)
        c3 = np.random.randint(1, 10)
        d1 = np.random.randint(1, 10)
        d2 = np.random.randint(1, 10)
        d3 = np.random.randint(1, 10)
        if(a1 != a2 or a2 != a3 or a1 != a3):
            if(a1+b1 < 9 and a2+b2 >9 and a3+b3 > 10):
                if (c1 != c2 or c2 != c3 or c1 != c3):
                    if (c1 + d1 < 9 and c2 + d2 > 9 and c3 + d3 > 10):
                        break

    A = a1*100+a2*10+a3
    B = b1*100+b2*10+b3

    s1 = 1+a1+b1
    s2 = 1+a2+b2-10
    s3 = a3+b3-10

    T1 = s1 * 100 + s2 * 10 + s3

    C = c1 * 100 + c2 * 10 + c3
    D = d1 * 100 + d2 * 10 + d3

    t1 = 1 + c1 + d1
    t2 = 1 + c2 + d2 - 10
    t3 = c3 + d3 - 10

    T2 = t1 * 100 + t2 * 10 + t3

    j1 = proc_jo(T1, -1)
    j2 = proc_jo(T2, 2)

    if ((T1 - T2) > 0):
        S = "&gt;"
        S1 = "보다 크"
    elif ((T1 - T2) < 0):
        S = "&lt;"
        S1 = "보다 작으"
    else:
        S = "="
        S1 = "%s 같으" % j2


    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(S=S)
    comment = comment.format(a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, s1=s1, s2=s2, s3=s3, t1=t1, t2=t2, t3=t3, T1=T1, T2=T2, S1=S1, S=S, c1=c1, c2=c2, c3=c3, d1=d1, d2=d2, d3=d3, j1=j1)

    return stem, answer, comment















# 3-1-1-23
def addandsub311_Stem_012():
    stem = "계산 결과가 가장 큰 것을 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${A} ` + ` {B}$$/수식$$  ㉡ $$수식$${C} ` + ` {D}$$/수식$$  ㉢ $$수식$${E} ` + ` {F}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{S}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${A} ` + ` {B} ` = ` {S1} $$/수식$$\n" \
              "㉡ $$수식$${C} ` + ` {D} ` = ` {S2} $$/수식$$\n" \
              "㉢ $$수식$${E} ` + ` {F} ` = ` {S3} $$/수식$$\n" \
              "따라서 $$수식$${T1} &lt; {T2} &lt; {T3}$$/수식$$ 이므로 계산 결과가 가장 큰 것은 {S}입니다.\n\n" \


    while(1):
        while(1):
            a1 = np.random.randint(1, 10)
            a2 = np.random.randint(0, 10)
            a3 = np.random.randint(0, 10)
            b1 = np.random.randint(1, 10)
            b2 = np.random.randint(1, 10)
            b3 = np.random.randint(1, 10)
            c1 = np.random.randint(1, 10)
            c2 = np.random.randint(0, 10)
            c3 = np.random.randint(0, 10)
            d1 = np.random.randint(1, 10)
            d2 = np.random.randint(1, 10)
            d3 = np.random.randint(1, 10)
            e1 = np.random.randint(1, 10)
            e2 = np.random.randint(0, 10)
            e3 = np.random.randint(0, 10)
            f1 = np.random.randint(1, 10)
            f2 = np.random.randint(1, 10)
            f3 = np.random.randint(1, 10)
            if(a1 != a2 or a2 != a3 or a1 != a3):
                if (c1 != c2 or c2 != c3 or c1 != c3):
                    if (e1 != e2 or e2 != e3 or e1 != e3):
                        if(a1+b1 < 9 and a2+b2 >9 and a3+b3 > 10):
                            if (c1 + d1 < 9 and c2 + d2 > 9 and c3 + d3 > 10):
                                    if (e1 + f1 < 9 and e2 + f2 > 9 and e3 + f3 > 10):
                                        break

        A = a1*100+a2*10+a3
        B = b1*100+b2*10+b3
        C = c1*100+c2*10+c3

        D = d1 * 100 + d2 * 10 + d3
        E = e1 * 100 + e2 * 10 + e3
        F = f1 * 100 + f2 * 10 + f3

        S1 = A + B
        S2 = C + D
        S3 = E + F


        if A != C and A != E and C != E:
            if S1 != S2 and S1 != S3 and S2 != S3:
                break


    if (S1 > S2):
        if (S1 > S3):
            if (S2 > S3):
                T3 = S1
                T2 = S2
                T1 = S3
            else:
                T3 = S1
                T2 = S3
                T1 = S2
        else:
            T3 = S3
            T2 = S1
            T1 = S2
    elif (S2 > S1):
        if (S3 > S1):
            if (S2 > S3):
                T3 = S2
                T2 = S3
                T1 = S1
            else:
                T3 = S3
                T2 = S2
                T1 = S1
        else:
            T3 = S2
            T2 = S1
            T1 = S3

    if (T3 == S1):
        S = "㉠"
    elif (T3 == S2):
        S = "㉡"
    else:
        S = "㉢"


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, S1=S1, S2=S2, S3=S3, T1=T1, T2=T2, T3=T3, S=S)

    return stem, answer, comment









# 3-1-1-24
def addandsub311_Stem_013():
    stem = "㉠과 ㉡의 합을 구해 보세요.\n$$표$$㉠ $$수식$$100$$/수식$$이 $$수식$${A}$$/수식$$개, $$수식$$10$$/수식$$이 $$수식$${B}$$/수식$$개, $$수식$$1$$/수식$$이 $$수식$${C}$$/수식$$개인 수\n㉡ $$수식$$100$$/수식$$이 $$수식$${D}$$/수식$$개, $$수식$$10$$/수식$$이 $$수식$${E}$$/수식$$개, $$수식$$1$$/수식$$이 $$수식$${F}$$/수식$$개인 수$$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$100$$/수식$$이 $$수식$${A}$$/수식$$개이면 $$수식$${S1}$$/수식$$, " \
              "$$수식$$10$$/수식$$이 $$수식$${B}$$/수식$$개이면 $$수식$${S2}$$/수식$$, $$수식$$1$$/수식$$이 $$수식$${C}$$/수식$$개이면 $$수식$${S3}$$/수식$$이므로 " \
              "$$수식$${S1} ` + ` {S2} ` + ` {S3} ` = ` {S4}$$/수식$$입니다.\n" \
              "$$수식$$100$$/수식$$이 $$수식$${D}$$/수식$$개이면 $$수식$${T1}$$/수식$$, " \
              "$$수식$$10$$/수식$$이 $$수식$${E}$$/수식$$개이면 $$수식$${T2}$$/수식$$, $$수식$$1$$/수식$$이 $$수식$${F}$$/수식$$개이면 $$수식$${T3}$$/수식$$이므로 " \
              "$$수식$${T1} ` + ` {T2} ` + ` {T3} ` = ` {T4}$$/수식$$입니다.\n" \
              "따라서 ㉠$$수식$$+$$/수식$$㉡$$수식$$= ` {S4} ` + ` {T4} ` = ` {S}$$/수식$$입니다.\n\n"

    while(1):
        A = np.random.randint(1,9)
        B = np.random.randint(11,19)
        C = np.random.randint(11,20)

        S1 = A*100
        S2 = B*10
        S3 = C*1

        X = S1+S2+S3

        s1 = math.floor(X / 100)
        s2 = math.floor((X%100) / 10)
        s3 = math.floor(((X%100) % 10 ))

        S4 = s1*100+s2*10+s3

        D = np.random.randint(1, 9)
        E = np.random.randint(11, 19)
        F = np.random.randint(1, 10)

        T1 = D*100
        T2 = E*10
        T3 = F*1

        Y = T1+T2+T3

        t1 = math.floor(Y / 100)
        t2 = math.floor((Y % 100) / 10)
        t3 = math.floor(((Y % 100) % 10))

        if(s1+t1 < 9 and s2+t2>9 and s3+t3 >10):
            break

    T4 = t1*100+t2*10+t3

    S = S4+T4


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F)
    answer = answer.format(S=S)
    comment = comment.format(s1=s1,s2=s2,s3=s3,A=A, B=B, C=C, D=D, E=E, F=F, S1=S1, S2=S2, S3=S3, T1=T1, T2=T2, T3=T3, S=S,T4=T4,S4=S4)

    return stem, answer, comment







# 3-1-1-25
def addandsub311_Stem_014():
    stem = "{N}네 {people}들이 이틀 동안 빈 병을 모았습니다. 첫째 날에 $$수식$${A}$$/수식$$병, 둘째 날에 $$수식$${B}$$/수식$$병을 모았습니다. {N}네 {people}들이 이틀 동안 모은 빈 병은 모두 몇 병인가요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$ 이틀 동안 모은 빈 병의 수 $$수식$$RIGHT ) = {A} ` + ` {B} ` = ` {S} LEFT ($$/수식$$병$$수식$$RIGHT )$$/수식$$\n\n"


    while(1):
        N = ["준호", "영수", "희주", "영희", "수호", "예주", "은지", "건우", "찬수", "지아"][np.random.randint(0, 10)]
        people = ["학교 학생", "아파트 주민", "마을 사람", "동네 사람"][np.random.randint(0, 4)]
        a1 = np.random.randint(1,10)
        a2 = np.random.randint(0,10)
        a3 = np.random.randint(0,10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(0, 10)
        b3 = np.random.randint(0, 10)

        if(a1!=a2 or a1!=a3 or a2!=a3):
            if(a2!=0 and a3!=0):
                if(a1+b1<9 and a2+b2>9 and a3+b3>10):
                    break

    A = a1*100 + a2*10 + a3
    B = b1*100 + b2*10 + b3

    S = A+B

    stem = stem.format(N=N, A=A, B=B, people=people)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, S=S)

    return stem, answer, comment





# 3-1-1-29
def addandsub311_Stem_015():
    stem = "㉠, ㉡에 알맞은 숫자를 차례대로 구해 보세요.\n             $$수식$${a1}$$/수식$$ ㉠ $$수식$${a3}$$/수식$$ \n    $$수식$$+$$/수식$$   ㉡ $$수식$${b2}``{b3}$$/수식$$ \n───────\n         $$수식$$1``{c1}``{c2}``{c3}$$/수식$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$, $$수식$${T}$$/수식$$\n"
    comment = "(해설)\n" \
            "일의 자리 계산은 $$수식$${a3} ` + ` {b3} ` = ` {S1}$$/수식$$\n" \
            "십의 자리 계산은 $$수식$$1 ` + ` $$/수식$$㉠$$수식$$ ` + ` {b2} ` = ` {S2}$$/수식$$ 에서 ㉠$$수식$$= {S}$$/수식$$\n" \
            "백의 자리 계산은 $$수식$$1 ` + ` {a1} ` + ` $$/수식$$㉡$$수식$$ ` = ` {S3}$$/수식$$ 에서 ㉡$$수식$$= {T}$$/수식$$\n" \
            "따라서 ㉠ $$수식$${S}$$/수식$$, ㉡ $$수식$${T}$$/수식$$입니다.\n\n"


    while(1):
        a1 = np.random.randint(1,10)
        a2 = np.random.randint(0,10)
        a3 = np.random.randint(1,10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(0, 10)
        b3 = np.random.randint(1, 10)


        if(a1+b1>=9 and a2+b2>=9 and a3+b3>=10):
            break

    c1 = a1+b1-10+1
    c2 = a2+b2-10+1
    c3 = a3+b3-10

    C = 1*1000 + c1*100+c2*10+c3

    S1 = a3+b3
    S2 = 1+a2+b2
    S3 = 1+a1+b1

    S = S2-1-b2
    T = S3-1-a1

    stem = stem.format(a1=a1, a3=a3, b2=b2, b3=b3, c1=c1, c2=c2, c3=c3)
    answer = answer.format(S=S, T=T)
    comment = comment.format(a3=a3, b3=b3, S1=S1, a2=a2, b2=b2, S2=S2, S=S, a1=a1, b1=b1, S3=S3, T=T, c1=c1, c2=c2,
                             c3=c3)


    return stem, answer, comment





# 3-1-1-30
def addandsub311_Stem_016():
    stem = "계산 결과가 가장 큰 것부터 차례대로 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${A} + {B}$$/수식$$  ㉡ $$수식$${C} + {D}$$/수식$$  ㉢ $$수식$${E} + {F}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{TT1}, {TT2}, {TT3}\n"
    comment = "(해설)\n" \
             "$$수식$$㉠``{a1}``{a2}``{a3}``+``{b1}``{b2}``{b3}``=``1``{s1}``{s2}``{s3}$$/수식$$ \n" \
             "$$수식$$㉡``{c1}``{c2}``{c3}``+``{d1}``{d2}``{d3}``=``1``{t1}``{t2}``{t3}$$/수식$$ \n" \
             "$$수식$$㉢``{e1}``{e2}``{e3}``+``{f1}``{f2}``{f3}``=``1``{u1}``{u2}``{u3}$$/수식$$ \n" \
             "따라서 $$수식$${T1} &gt; {T2} &gt; {T3}$$/수식$$ 이므로 계산 결과가 가장 큰 것부터 차례대로 {TT1}, {TT2}, {TT3} 입니다.\n\n"


    while(1):
        a1 = np.random.randint(1,10)
        a2 = np.random.randint(0,10)
        a3 = np.random.randint(1,10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(0, 10)
        b3 = np.random.randint(1, 10)

        if(a1+b1>=9 and a2+b2>=9 and a3+b3>=10):
            if(a1!=a2 or a1!=a3 or a2!=a3):
                break

    A = a1*100+a2*10+a3
    B = b1*100+b2*10+b3

    s1 = 1+a1+b1-10
    s2 = 1+a2+b2-10
    s3 = a3+b3-10

    S1 = 1*1000+s1*100+10*s2+s3

    while (1):
        c1 = np.random.randint(1, 10)
        c2 = np.random.randint(0, 10)
        c3 = np.random.randint(1, 10)

        d1 = np.random.randint(1, 10)
        d2 = np.random.randint(0, 10)
        d3 = np.random.randint(1, 10)

        C = c1 * 100 + c2 * 10 + c3
        D = d1 * 100 + d2 * 10 + d3

        t1 = 1 + c1 + d1 - 10
        t2 = 1 + c2 + d2 - 10
        t3 = c3 + d3 - 10

        S2 = 1 * 1000 + t1 * 100 + t2 * 10 + t3

        if (c1 + d1 >= 9 and c2 + d2 >= 9 and c3 + d3 >= 10):
            if (c1 != c2 or c1 != c3 or c2 != c3):
                if(A!=C):
                    break


    while (1):
        e1 = np.random.randint(1, 10)
        e2 = np.random.randint(0, 10)
        e3 = np.random.randint(1, 10)

        f1 = np.random.randint(1, 10)
        f2 = np.random.randint(0, 10)
        f3 = np.random.randint(1, 10)

        E = e1*100 + e2*10 + e3
        F = f1*100 + f2*10 + f3

        u1 = 1+e1+f1-10
        u2 = 1+e2+f2-10
        u3 = e3+f3-10

        S3 = 1*1000 + u1*100 + u2*10 + u3

        if (e1 + f1 >= 9 and e2 + f2 >= 9 and e3 + f3 >= 10):
            if (e1 != e2 or e1 != e3 or e2 != e3):
                if(A!=E and C!=E):
                    break

    if (S1 > S2):
        if (S1 > S3):
            if (S2 > S3):
                T1 = S1
                TT1 = "㉠"
                T2 = S2
                TT2 = "㉡"
                T3 = S3
                TT3 = "㉢"
            else:
                T1 = S1
                TT1 = "㉠"
                T2 = S3
                TT2 = "㉢"
                T3 = S2
                TT3 = "㉡"
        else:
            T1 = S3
            TT1 = "㉢"
            T2 = S1
            TT2 = "㉠"
            T3 = S2
            TT3 = "㉡"
    elif (S2 > S1):
        if (S3 > S1):
            if (S2 > S3):
                T1 = S2
                TT1 = "㉡"
                T2 = S3
                TT2 = "㉢"
                T3 = S1
                TT3 = "㉠"
            else:
                T1 = S3
                TT1 = "㉢"
                T2 = S2
                TT2 = "㉡"
                T3 = S1
                TT3 = "㉠"
        else:
            T1 = S2
            TT1 = "㉡"
            T2 = S1
            TT2 = "㉠"
            T3 = S3
            TT3 = "㉢"

    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F)
    answer = answer.format(TT1=TT1, TT2=TT2, TT3=TT3)
    comment = comment.format(a3=a3, b3=b3, a2=a2, b2=b2, a1=a1, b1=b1, c1=c1, c2=c2, c3=c3, e1=e1, e2=e2, e3=e3, f1=f1, f2=f2, f3=f3, s1=s1, t1=t1, s2=s2, t2=t2, s3=s3, t3=t3, u1=u1, u2=u2, u3=u3, T1=T1, T2=T2, T3=T3, TT1=TT1, TT2=TT2, TT3=TT3, d1=d1, d2=d2, d3=d3)

    return stem, answer, comment





# 3-1-1-32
def addandsub311_Stem_017():
    stem = "다음 수 중에서 두 수를 골라 합이 가장 크게 나오도록 덧셈식을 만들어 보세요. $$수식$$LEFT ($$/수식$$단, 두 수 중 큰 수를 앞에 씁니다.$$수식$$RIGHT )$$/수식$$\n$$표$$ $$수식$${E}$$/수식$$  $$수식$${F}$$/수식$$  $$수식$${G}$$/수식$$  $$수식$${H}$$/수식$$ $$/표$$\n$$수식$${boxone}$$/수식$$ $$수식$$` + `$$/수식$$ $$수식$${boxtwo}$$/수식$$ $$수식$$` = `$$/수식$$ $$수식$${boxthree}$$/수식$$\n"
    answer = "(정답)\n$$수식$${A}$$/수식$$, $$수식$${B}$$/수식$$, $$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
            "수의 크기를 비교하면\n" \
            "$$수식$${A} &gt; {B} &gt; {C} &gt; {D}$$/수식$$이므로 가장 큰 수는 $$수식$${A}$$/수식$$, 두 번째로 큰 수는 $$수식$${B}$$/수식$$입니다. " \
            "따라서 합이 가장 큰 덧셈식은 $$수식$${A}`+`{B}`=`{S}$$/수식$$입니다.\n\n"

    while(1):
        a1 = np.random.randint(1,10)
        a2 = np.random.randint(0,10)
        a3 = np.random.randint(0,10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(1, 10)
        b3 = np.random.randint(1, 10)

        A = a1*100 + a2*10 + a3
        B = b1*100 + b2*10 + b3

        if(a1+b1>=9 and a2+b2>9 and a3+b3>10):
            if(a1!=a2 or a1!=a3 or a2!=a3):
                if(a2!=0 and a3!=0):
                    if(A>B):
                        break

    while (1):
        c1 = np.random.randint(1, 10)
        c2 = np.random.randint(0, 10)
        c3 = np.random.randint(0, 10)

        d1 = np.random.randint(1, 10)
        d2 = np.random.randint(1, 10)
        d3 = np.random.randint(1, 10)

        C = c1 * 100 + c2 * 10 + c3
        D = d1 * 100 + d2 * 10 + d3

        if (c1 != c2 or c1 != c3 or c2 != c3):
            if (c2 != 0 and c3 != 0):
                if (d1 != d2 or d1 != d3 or d2 != d3):
                    if(C>D):
                        if(B>C):
                            break

    S = A+B

    N = [A, B, C, D]
    np.random.shuffle(N)
    E, F, G, H = N

    boxone = "box{　　　}"
    boxtwo = "box{　　　}"
    boxthree = "box{　　　}"

    stem = stem.format(E=E, F=F, G=G, H=H, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree)
    answer = answer.format(A=A, B=B, S=S)
    comment = comment.format(A=A, B=B, C=C, D=D, S=S)

    return stem, answer, comment












# 3-1-1-33
def addandsub311_Stem_018():
    stem = "어떤 세 자리 수 ㉠㉡$$수식$${X}$$/수식$${josa} $$수식$${Y}$$/수식$$㉢의 합은 $$수식$${Z}$$/수식$$입니다.\n㉠㉡㉢과 ㉢㉡㉠의 합을 구해 보세요.\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "일의 자리 계산은 $$수식$${X} ` + `$$/수식$$㉢$$수식$$= ` {S1}$$/수식$$에서 ㉢$$수식$$= ` {S2}$$/수식$$,\n" \
              "십의 자리 계산은 $$수식$$1 ` + `$$/수식$$㉡$$수식$$+ ` {b2} ` = ` {S3}$$/수식$$에서 ㉡$$수식$$= ` {S4}$$/수식$$,\n" \
              "백의 자리 계산은 $$수식$$1 ` + `$$/수식$$㉠$$수식$$+ ` {b1} ` = ` {S5}$$/수식$$에서 ㉠$$수식$$= ` {S6}$$/수식$$입니다.\n" \
              "㉠㉡㉢ $$수식$$+$$/수식$$ ㉢㉡㉠ $$수식$$= {S7} ` + ` {S8} ` = ` {S}$$/수식$$입니다.\n\n"


    while(1):
        a1 = np.random.randint(1,10)
        a2 = np.random.randint(5,10)
        a3 = np.random.randint(0,10)

        b1 = np.random.randint(0, 10)
        b2 = np.random.randint(0, 10)
        b3 = np.random.randint(0, 10)

        if(a1+b1>=9 and a2+b2>=9 and a3+b3>10 and a1+b3>10):
            if(a1!=a2 or a1!=a3 or a2!=a3):
                if(a2!=0 and a3!=0):
                    break

    s1 = 1+a1+b1-10
    s2 = 1+a2+b2-10
    s3 = a3+b3-10

    X = a3
    Y = b1*10+b2*1
    Z = 1*1000 + s1*100 + s2*10 + s3
    S1 = a3+b3
    S2 = S1-a3
    S3 = 1+a2+b2
    S4 = S3-1-b2
    S5 = 1+a1+b1
    S6 = S5-1-b1
    S7 = S6*100+S4*10+S2
    S8 = S2*100 + S4*10 + S6

    S = S7+S8

    if X in [0,1,3,6,7,8]:
        josa="과"
    else:
        josa="와"

    stem = stem.format(X=X, Y=Y, Z=Z,josa=josa)
    answer = answer.format(S=S)
    comment = comment.format(X=X, S1=S1, S2=S2, b2=b2, S3=S3, S4=S4, b1=b1, S5=S5, S6=S6, S7=S7, S8=S8, S=S)

    return stem, answer, comment











# 3-1-1-34
def addandsub311_Stem_019():
    stem = "{N}에 토요일에 입장한 남자는 $$수식$${A}$$/수식$$명, 여자는 $$수식$${B}$$/수식$$명이고 일요일에 입장한 남자는 $$수식$${C}$$/수식$$명, 여자는 $$수식$${D}$$/수식$$명입니다. 토요일과 일요일 중 입장객이 더 많은 요일은 언제인가요?\n"
    answer = "(정답)\n{S}\n"
    comment = "(해설)\n" \
              "$$수식$$ LEFT ( $$/수식$$ 토요일 입장객 수 $$수식$$ RIGHT ) = {A} ` + ` {B} ` = ` {S1} LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$ LEFT ( $$/수식$$ 일요일 입장객 수 $$수식$$ RIGHT ) = {C} ` + ` {D} ` = ` {S2} LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 $$수식$${S1} ` {T} ` {S2}$$/수식$$ 이므로 입장객이 더 많은 요일은 {S}입니다."



    while True:
        while(1):
            a1 = np.random.randint(1, 10)
            a2 = np.random.randint(0, 10)
            a3 = np.random.randint(0, 10)

            b1 = np.random.randint(1, 10)
            b2 = np.random.randint(1, 10)
            b3 = np.random.randint(1, 10)

            c1 = np.random.randint(1, 10)
            c2 = np.random.randint(0, 10)
            c3 = np.random.randint(0, 10)

            d1 = np.random.randint(1, 10)
            d2 = np.random.randint(1, 10)
            d3 = np.random.randint(1, 10)

            if a1+b1 >= 9 and a2+b2 >= 9 and a3+b3 > 10:
                if c1 + d1 >= 9 and c2 + d2 >= 9 and c3 + d3 > 10:
                    if a1 != a2 or a1 != a3 or a2 != a3:
                        if c1 != c2 or c1 != c3 or c2 != c3:
                            if a2 != 0 and a3 != 0:
                                if c2 != 0 and c3 != 0:
                                    break

        A = a1*100 + a2*10 + a3
        B = b1*100 + b2*10 + b3
        C = c1*100 + c2*10 + c3
        D = d1*100 + d2*10 + d3

        S1 = A + B
        S2 = C + D

        if S1 != S2:
            break



    N = ["놀이공원", "캠핑장", "수영장", "스키장", "박물관", "미술관", "전시회"][np.random.randint(0, 7)]

    if(S1 > S2):
        T = "&gt;"
        S = "토요일"
    else:
        T = "&lt;"
        S = "일요일"

    stem = stem.format(A=A, B=B, C=C, D=D, N=N)
    answer = answer.format(S=S)
    comment = comment.format(S=S, S1=S1, S2=S2, T=T, C=C, D=D, A=A, B=B)

    return stem, answer, comment














# 3-1-1-35
def addandsub311_Stem_020():
    stem = "두 수의 차를 구해 보세요.\n$$표$$ $$수식$${C}$$/수식$$  $$수식$${D}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ {A} ` &gt; ` {B} $$/수식$$ 이므로\n" \
              "$$수식$${a1}``{a2}``{a3}``-``{b1}``{b2}``{b3}``=``{s1}``{s2}``{s3}$$/수식$$\n" \

    while(1):
        a1 = np.random.randint(1,10)
        a2 = np.random.randint(0,10)
        a3 = np.random.randint(0,10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(0, 10)
        b3 = np.random.randint(0, 10)

        if(a1>b1 and a2>b2 and a3>b3):
            if(a1!=a2 or a1!=a3 or a2!=a3):
                if(a2!=0 and a3!=0):
                    if(b1!=b2 or b1!=b3 or b2!=b3):
                        if(b2!=0 and b3!=0):
                            break

    s1 = a1 - b1
    s2 = a2 - b2
    s3 = a3 - b3

    A = a1*100 + a2*10 + a3
    B = b1*100 + b2*10 + b3
    S = s1*100 + s2*10 + s3

    N = [A, B]
    np.random.shuffle(N)
    C, D = N

    stem = stem.format(C=C, D=D)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, s1=s1, s2=s2, s3=s3)

    return stem, answer, comment




















# 3-1-1-39
def addandsub311_Stem_021():
    stem = "계산 결과가 더 큰 것의 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${A} ` - ` {B}$$/수식$$  ㉡ $$수식$${C} ` - ` {D}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$㉠``{a1}``{a2}``{a3}``-``{b1}``{b2}``{b3}``=``{s1}``{s2}``{s3}$$/수식$$\n" \
              "$$수식$$㉡``{c1}``{c2}``{c3}``-``{d1}``{d2}``{d3}``=``{t1}``{t2}``{t3}$$/수식$$\n" \
              "따라서 $$수식$${S1} ` {T} ` {S2}$$/수식$$ 이므로 계산 결과가 더 큰 것은 {S} 입니다.\n\n"



    while(1):
        a1 = np.random.randint(1,10)
        a2 = np.random.randint(0,10)
        a3 = np.random.randint(0,10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(0, 10)
        b3 = np.random.randint(0, 10)

        if(a1>b1 and a2>b2 and a3>b3):
            if(a1!=a2 or a1!=a3 or a2!=a3):
                if(a2!=0 and a3!=0):
                    if(b1!=b2 or b1!=b3 or b2!=b3):
                        if(b2!=0 and b3!=0):
                            break

    while (1):
        c1 = np.random.randint(1, 10)
        c2 = np.random.randint(0, 10)
        c3 = np.random.randint(0, 10)

        d1 = np.random.randint(1, 10)
        d2 = np.random.randint(0, 10)
        d3 = np.random.randint(0, 10)

        if (c1 > d1 and c2 > d2 and c3 > d3):
            if (c1 != c2 or c1 != c3 or c2 != c3):
                if (d2 != 0 and d3 != 0):
                    if (d1 != d2 or d1 != d3 or d2 != d3):
                        if (c2 != 0 and c3 != 0):
                            break

    s1 = a1 - b1
    s2 = a2 - b2
    s3 = a3 - b3

    t1 = c1 - d1
    t2 = c2 - d2
    t3 = c3 - d3

    A = a1*100 + a2*10 + a3
    B = b1*100 + b2*10 + b3
    C = c1*100 + c2*10 + c3
    D = d1*100 + d2*10 + d3
    S1 = s1*100 + s2*10 + s3
    S2 = t1 * 100 + t2 * 10 + t3

    if(S1>S2):
        T = "&gt;"
        S = "㉠"
    else:
        T = "&lt;"
        S = "㉡"

    stem = stem.format(A=A,B=B,C=C,D=D)
    answer = answer.format(S=S)
    comment = comment.format(S=S,S1=S1,T=T,S2=S2,a1=a1,a2=a2,a3=a3,b1=b1,b2=b2,b3=b3,s1=s1,s2=s2,s3=s3,c1=c1,c2=c2,c3=c3,d1=d1,d2=d2,d3=d3,t1=t1,t2=t2,t3=t3)

    return stem, answer, comment

















# 3-1-1-40
def addandsub311_Stem_022():
    stem = "가장 큰 수와 가장 작은 수의 차를 구해 보세요.\n$$표$$ $$수식$${D}$$/수식$$  $$수식$${E}$$/수식$$  $$수식$${F}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "가장 큰 수는 $$수식$$ {S1} $$/수식$$, 가장 작은 수는 $$수식$$ {S2} $$/수식$$입니다.\n" \
              "$$수식$${a1}``{a2}``{a3}``-``{c1}``{c2}``{c3}``=``{s1}``{s2}``{s3}$$/수식$$\n" \


    while(1):
        a1 = np.random.randint(1,10)
        a2 = np.random.randint(0,10)
        a3 = np.random.randint(0,10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(0, 10)
        b3 = np.random.randint(0, 10)

        c1 = np.random.randint(1, 10)
        c2 = np.random.randint(0, 10)
        c3 = np.random.randint(0, 10)

        A = a1 * 100 + a2 * 10 + a3
        B = b1 * 100 + b2 * 10 + b3
        C = c1 * 100 + c2 * 10 + c3

        if(a1>c1 and a2>c2 and a3>c3):
            if(a1!=a2 or a1!=a3 or a2!=a3):
                if(a2!=0 and a3!=0):
                    if(b1!=b2 or b1!=b3 or b2!=b3):
                        if(b2!=0 and b3!=0):
                            if (c1 != c2 or a1 != c3 or c2 != c3):
                                if (c2 != 0 and c3 != 0):
                                    if(A>B and B>C):
                                        break


    s1 = a1-c1
    s2 = a2-c2
    s3 = a3-c3

    S = s1*100+s2*10+s3
    S1 = a1*100+a2*10+a3
    S2 = c1*100 + c2*10 + c3

    N = [A, B, C]
    np.random.shuffle(N)
    D, E, F = N

    stem = stem.format(E=E,F=F,D=D)
    answer = answer.format(S=S)
    comment = comment.format(S1=S1,S2=S2,a1=a1,a2=a2,a3=a3,s1=s1,s2=s2,s3=s3,c1=c1,c2=c2,c3=c3, S=S)

    return stem, answer, comment



















# 3-1-1-41
def addandsub311_Stem_023():
    stem = "{depart}에서 {N}으로 가는 비행기에 남자 $$수식$${A}$$/수식$$명, 여자 $$수식$${B}$$/수식$$명이 탔습니다. {T1}는 {T2}보다 몇 명 더 많이 탔나요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$명\n"
    comment = "(해설)\n" \
              "{T1} 수에서 {T2} 수를 빼어 구합니다.\n" \
              "$$수식$$LEFT ( $$/수식$$비행기에 탄 {T1} 수$$수식$$ RIGHT ) - LEFT ( $$/수식$$비행기에 탄 {T2} 수$$수식$$ RIGHT )$$/수식$$\n$$수식$$ = {S1} - {S2} = {S}$$/수식$$\n\n"



    while(1):
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(0, 10)
        a3 = np.random.randint(0, 10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(0, 10)
        b3 = np.random.randint(0, 10)

        A = a1 * 100 + a2 * 10 + a3
        B = b1 * 100 + b2 * 10 + b3

        if a1 != a2 or a1 != a3 or a2 != a3:
            if a2 != 0 and a3 != 0:
                if b1 != b2 or b1 != b3 or b2 != b3:
                    if b2 != 0 and b3 != 0:
                        if A != B:
                            break


    if A > B:
        T1 = "남자"
        T2 = "여자"
        S1 = A
        S2 = B
    else:
        T1 = "여자"
        T2 = "남자"
        S1 = B
        S2 = A

    S = S1 - S2

    N = ["런던", "베이징", "홍콩", "워싱턴", "괌", "뉴욕", "방콕", "베를린", "멜버른"][np.random.randint(0, 9)]
    depart = ["인천", "김해", "김포"][np.random.randint(0, 3)]


    stem = stem.format(N=N, A=A, B=B, T1=T1, T2=T2, depart=depart)
    answer = answer.format(S=S)
    comment = comment.format(S1=S1, S2=S2, T1=T1, T2=T2, S=S)

    return stem, answer, comment

















# 3-1-1-43
def addandsub311_Stem_024():
    stem = "어떤 수에서 $$수식$${A}$$/수식$${j1} 빼야 할 것을 잘못하여 더했더니 $$수식$${B}$$/수식$${j2} 되었습니다. 바르게 계산한 값은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □라 하면, 잘못 계산한 식은\n" \
              "□ $$수식$$+ {A} ` = ` {B}$$/수식$$, □ $$수식$$= {B} ` - ` {A} ` = ` {S1}$$/수식$$\n" \
              "따라서 바르게 계산하면\n" \
              "$$수식$${S1} ` - ` {A} ` = ` {S}$$/수식$$ 입니다.\n\n" \


    while(1):
        a1 = np.random.randint(1,10)
        a2 = np.random.randint(0,10)
        a3 = np.random.randint(0,10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(0, 10)
        b3 = np.random.randint(0, 10)

        A = a1 * 100 + a2 * 10 + a3
        B = b1 * 100 + b2 * 10 + b3

        if(2*a1<b1 and 2*a2<b2 and 2*a3<b3):
            if(a1!=a2 or a1!=a3 or a2!=a3):
                if(a2!=0 and a3!=0):
                    if(b1!=b2 or b1!=b3 or b2!=b3):
                        if(b2!=0 and b3!=0):
                            if(A!=B):
                                break

    S1 = B - A
    S = S1 - A

    j1 = proc_jo(A, 1)
    j2 = proc_jo(B, 0)


    stem = stem.format(A=A, B=B, j1=j1, j2=j2)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, S1=S1, S=S)

    return stem, answer, comment
















# 3-1-1-45
def addandsub311_Stem_025():
    stem = "○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${A} ` - ` {B}$$/수식$$  ○  $$수식$${C}$$/수식$$\n"
    answer = "(정답)\n$$수식$${T}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A} ` - ` {B} ` = ` {S1}$$/수식$$ 이므로 $$수식$${S1} ` {T} ` {C}$$/수식$$ 입니다.\n\n"


    while 1:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(0, 10)
        a3 = np.random.randint(0, 10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(0, 10)
        b3 = np.random.randint(0, 10)

        A = a1 * 100 + a2 * 10 + a3
        B = b1 * 100 + b2 * 10 + b3

        if a1 > b1:
            if a1 != a2 or a1 != a3 or a2 != a3:
                if a2 != 0 and a3 != 0:
                    if A != B:
                        if (a2-1) > b2 and a3 < b3:
                            s1 = a1 - b1
                            s2 = a2 - b2 - 1
                            s3 = 10 + a3 - b3
                            break
                        elif a2 < b2 and (a1 - 1) > b1 and a3 > b3:
                            s1 = a1 - b1 - 1
                            s2 = 10 + a2 - b2
                            s3 = a3 - b3
                            break


    S1 = s1*100 + s2*10 + s3

    while 1:
        c1 = np.random.randint(1, 10)
        c2 = np.random.randint(0, 10)
        c3 = np.random.randint(0, 10)
        if c1 != c2 or c1 != c3 or c2 != c3:
            if c2 != 0 and c3 != 0:
                break

    C = c1*100 + c2*10 + c3

    if S1 > C:
        T = "&gt;"
    elif S1 == C:
        T = "="
    else:
        T = "&lt;"

    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(T=T)
    comment = comment.format(A=A, B=B, S1=S1, T=T, C=C)

    return stem, answer, comment
















# 3-1-1-46
def addandsub311_Stem_026():
    stem = "$$수식$$100$$/수식$$이 $$수식$${a1}$$/수식$$개, $$수식$$10$$/수식$$이 $$수식$${a2}$$/수식$$개, $$수식$$1$$/수식$$이 $$수식$${a3}$$/수식$$인 수 보다 $$수식$${B}$$/수식$$ 작은 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$100$$/수식$$이 $$수식$${a1}$$/수식$$개, $$수식$$10$$/수식$$이 $$수식$${a2}$$/수식$$개, " \
              "$$수식$$1$$/수식$$이 $$수식$${a3}$$/수식$$인 수는 $$수식$${A}$$/수식$$입니다.\n" \
              "따라서 $$수식$${A} ` - ` {B} ` = ` {S}$$/수식$$입니다.\n\n"

    while(1):
        a1 = np.random.randint(1,10)
        a2 = np.random.randint(1,10)
        a3 = np.random.randint(1,10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(0, 10)
        b3 = np.random.randint(0, 10)

        A = a1 * 100 + a2 * 10 + a3
        B = b1 * 100 + b2 * 10 + b3

        if (a1 > b1):
            if (a1 != a2 or a1 != a3 or a2 != a3):
                if (a2 != 0 and a3 != 0):
                    if (A != B):
                        if ((a2 - 1) > b2 and a3 < b3):
                            s1 = a1 - b1
                            s2 = a2 - b2 - 1
                            s3 = 10 + a3 - b3
                            break
                        elif (a2 < b2 and (a1 - 1) > b1 and a3 > b3):
                            s1 = a1 - b1 - 1
                            s2 = 10 + a2 - b2
                            s3 = a3 - b3
                            break

    S = s1 * 100 + s2 * 10 + s3

    stem = stem.format(A=A, B=B, a1=a1, a2=a2, a3=a3)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, a1=a1, a2=a2, a3=a3,S=S)

    return stem, answer, comment
















# 3-1-1-48
def addandsub311_Stem_027():
    stem = "계산 결과가 $$수식$${S}$$/수식$$인 것을 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${A} ` - ` {B}$$/수식$$  ㉡ $$수식$${C} ` - ` {D}$$/수식$$  ㉢ $$수식$${E} ` - ` {F}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{T}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${A} ` - ` {B} ` = ` {S1}$$/수식$$\n" \
              "㉡ $$수식$${C} ` - ` {D} ` = ` {S2}$$/수식$$\n" \
              "㉢ $$수식$${E} ` - ` {F} ` = ` {S3}$$/수식$$\n" \
              "따라서 계산 결과가 $$수식$${S}$$/수식$$인 것은 {T}입니다.\n\n"


    while(1):
        while(1):
            a1 = np.random.randint(1,10)
            a2 = np.random.randint(1,10)
            a3 = np.random.randint(1,10)

            b1 = np.random.randint(1, 10)
            b2 = np.random.randint(0, 10)
            b3 = np.random.randint(0, 10)

            A = a1 * 100 + a2 * 10 + a3
            B = b1 * 100 + b2 * 10 + b3

            if (a1 > b1):
                if (a1 != a2 or a1 != a3 or a2 != a3):
                    if (a2 != 0 and a3 != 0):
                        if (A != B):
                            if ((a2 - 1) > b2 and a3 < b3):
                                s1 = a1 - b1
                                s2 = a2 - b2 - 1
                                s3 = 10 + a3 - b3
                                break
                            elif (a2 < b2 and (a1 - 1) > b1 and a3 > b3):
                                s1 = a1 - b1 - 1
                                s2 = 10 + a2 - b2
                                s3 = a3 - b3
                                break

        S1 = s1 * 100 + s2 * 10 + s3

        while(1):
            c1 = np.random.randint(1,10)
            c2 = np.random.randint(1,10)
            c3 = np.random.randint(1,10)

            d1 = np.random.randint(1, 10)
            d2 = np.random.randint(0, 10)
            d3 = np.random.randint(0, 10)

            C = c1 * 100 + c2 * 10 + c3
            D = d1 * 100 + d2 * 10 + d3

            if (c1 > d1):
                if (c1 != c2 or c1 != c3 or c2 != c3):
                    if (c2 != 0 and c3 != 0):
                        if (C != D):
                            if ((c2 - 1) > d2 and c3 < d3):
                                t1 = c1 - d1
                                t2 = c2 - d2 - 1
                                t3 = 10 + c3 - d3
                                break
                            elif (c2 < d2 and (c1 - 1) > d1 and c3 > d3):
                                t1 = c1 - d1 - 1
                                t2 = 10 + c2 - d2
                                t3 = c3 - d3
                                break

        S2 = t1 * 100 + t2 * 10 + t3

        while (1):
            e1 = np.random.randint(1, 10)
            e2 = np.random.randint(1, 10)
            e3 = np.random.randint(1, 10)

            f1 = np.random.randint(1, 10)
            f2 = np.random.randint(0, 10)
            f3 = np.random.randint(0, 10)

            E = e1 * 100 + e2 * 10 + e3
            F = f1 * 100 + f2 * 10 + f3

            if (e1 > f1):
                if (e1 != e2 or e1 != e3 or e2 != e3):
                    if (e2 != 0 and e3 != 0):
                        if (C != D):
                            if ((e2 - 1) > f2 and e3 < f3):
                                u1 = e1 - f1
                                u2 = e2 - f2 - 1
                                u3 = 10 + e3 - f3
                                break
                            elif (c2 < d2 and (c1 - 1) > d1 and c3 > d3):
                                u1 = e1 - f1 - 1
                                u2 = 10 + e2 - f2
                                u3 = e3 - f3
                                break

        S3 = u1 * 100 + u2 * 10 + u3

        if S1 != S2 and S1 != S3 and S2 != S3:
            break


    S = [S1, S2, S3][np.random.randint(0, 3)]

    if S == S1:
        T = "㉠"
    elif S == S2:
        T = "㉡"
    else:
        T = "㉢"


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, S=S)
    answer = answer.format(T=T)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, S1=S1, S2=S2, S3=S3, T=T, S=S)

    return stem, answer, comment

















# 3-1-1-50
def addandsub311_Stem_028():
    stem = "어느 {place}에 {animal}{j1} 모두 $$수식$${A}$$/수식$$마리 있습니다. {animal1}{j2} $$수식$${B}$$/수식$$마리라면, {animal1}{j3} {animal2} 중 {place}에 더 많이 있는 것은 무엇인가요?\n"
    answer = "(정답)\n{S}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${animal2} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ( $$/수식$$ 전체 {animal} 수 $$수식$$ RIGHT ) ` - ` LEFT ( $$/수식$$ {animal1} 수 $$수식$$ RIGHT )$$/수식$$\n" \
              "$$수식$$= {A} ` - ` {B} ` = ` {S1} LEFT ($$/수식$$마리$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 $$수식$${B} ` {T} ` {S1}$$/수식$$ 이므로 {S}{j4} 더 많이 있습니다.\n\n"


    # while(1):
    #     a1 = np.random.randint(1,10)
    #     a2 = np.random.randint(1,10)
    #     a3 = np.random.randint(1,10)
    #
    #     b1 = np.random.randint(1, 10)
    #     b2 = np.random.randint(0, 10)
    #     b3 = np.random.randint(0, 10)
    #
    #     A = a1 * 100 + a2 * 10 + a3
    #     B = b1 * 100 + b2 * 10 + b3
    #
    #     if (a1 > b1):
    #         if (a1 != a2 or a1 != a3 or a2 != a3):
    #             if (a2 != 0 and a3 != 0):
    #                 if (A != B):
    #                     if ((a2 - 1) > b2 and a3 < b3):
    #                         s1 = a1 - b1
    #                         s2 = a2 - b2 - 1
    #                         s3 = 10 + a3 - b3
    #                         break
    #                     elif (a2 < b2 and (a1 - 1) > b1 and a3 > b3):
    #                         s1 = a1 - b1 - 1
    #                         s2 = 10 + a2 - b2
    #                         s3 = a3 - b3
    #                         break
    #
    # S1 = s1 * 100 + s2 * 10 + s3



    while True:
        while 1:
            a1 = np.random.randint(1, 10)
            a2 = np.random.randint(1, 10)
            a3 = np.random.randint(1, 10)

            b1 = np.random.randint(1, 10)
            b2 = np.random.randint(0, 10)
            b3 = np.random.randint(0, 10)

            A = a1 * 100 + a2 * 10 + a3
            B = b1 * 100 + b2 * 10 + b3

            if a1 > b1:
                if a1 != a2 or a1 != a3 or a2 != a3:
                    if (a2 != 0 and a3 != 0):
                        if (A != B):
                            if ((a2 - 1) > b2 and a3 < b3):
                                s1 = a1 - b1
                                s2 = a2 - b2 - 1
                                s3 = 10 + a3 - b3
                                break
                            elif (a2 < b2 and (a1 - 1) > b1 and a3 > b3):
                                s1 = a1 - b1 - 1
                                s2 = 10 + a2 - b2
                                s3 = a3 - b3
                                break

        S1 = s1 * 100 + s2 * 10 + s3

        if B != S1:
            break


    choice = np.random.randint(0, 3)
    place = ["양계장", "농장", "농장"][choice]
    animal = ["닭", "돼지", "소"][choice]
    animal1 = ["암탉", "암퇘지", "암소"][choice]
    animal2 = ["수탉", "수퇘지", "수소"][choice]

    j1 = proc_jo(animal, 0)
    j2 = proc_jo(animal1, 0)
    j3 = proc_jo(animal1, 2)


    if(B > S1):
        T = "&gt;"
        S = animal1
    else:
        T = "&lt;"
        S = animal2

    j4 = proc_jo(S, 0)


    stem = stem.format(A=A, B=B, place=place, animal=animal, j1=j1, animal1=animal1, animal2=animal2, j2=j2, j3=j3)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, S1=S1, S=S, T=T, animal=animal, animal1=animal1, animal2=animal2, j4=j4)

    return stem, answer, comment

















# 3-1-1-51
def addandsub311_Stem_029():
    stem = "다음 수 중에서 $$수식$$2$$/수식$$개를 골라 뺄셈식을 만들려고 합니다. □ 안에 알맞은 수를 써넣으세요. (단, 두 수 중 큰 수를 앞에 씁니다.)\n$$표$$ $$수식$${E}$$/수식$$  $$수식$${F}$$/수식$$  $$수식$${G}$$/수식$$ $$/표$$\n$$수식$${boxone}$$/수식$$ $$수식$$` - `$$/수식$$ $$수식$${boxone}$$/수식$$ $$수식$$` = ` {D} $$/수식$$\n"
    answer = "(정답)\n$$수식$${T1}$$/수식$$, $$수식$${T2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$, $$수식$${B}$$/수식$$, $$수식$${C}$$/수식$$을 각각 " \
              "$$수식$${S1}$$/수식$$, $$수식$${S2}$$/수식$$, $$수식$${S3}$$/수식$$으로 어림하여 어림한 값의 차가 " \
              "$$수식$${D}$$/수식$$에 가까운 경우를 찾으면 $$수식$${S1}$$/수식$$과 $$수식$${S2}$$/수식$$, $$수식$${S2}$$/수식$$과 $$수식$${S3}$$/수식$$입니다.\n" \
              "$$수식$${A} ` - ` {B} ` = ` {S4}$$/수식$$, $$수식$${B} ` - ` {C} ` = ` {S5}$$/수식$$이므로 " \
              "알맞은 뺄셈식은 $$수식$${T1} ` - ` {T2} ` = ` {D}$$/수식$$ 입니다.\n\n"



    while 1:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(1, 5)
        a3 = np.random.randint(1, 10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(0, 5)
        b3 = np.random.randint(0, 10)

        c1 = np.random.randint(1, 10)
        c2 = np.random.randint(0, 5)
        c3 = np.random.randint(0, 10)

        A = a1 * 100 + a2 * 10 + a3
        B = b1 * 100 + b2 * 10 + b3
        C = c1 * 100 + c2 * 10 + c3

        if (a1 > b1):
            if (a1 != a2 or a1 != a3 or a2 != a3):
                if (a2 != 0 and a3 != 0):
                    if (A != B):
                        if ((a2 - 1) > b2 and a3 < b3):
                            s1 = a1 - b1
                            s2 = a2 - b2 - 1
                            s3 = 10 + a3 - b3
                            if (b1 > c1):
                                if ((b2 - 1) > c2 and b3 < c3):
                                    t1 = b1 - c1
                                    t2 = b2 - c2 - 1
                                    t3 = 10 + b3 - c3
                                    break
                                elif (b2 < c2 and (b1 - 1) > c1 and b3 > c3):
                                    t1 = b1 - c1 - 1
                                    t2 = 10 + b2 - c2
                                    t3 = b3 - c3
                                    break
                        elif (a2 < b2 and (a1 - 1) > b1 and a3 > b3):
                            s1 = a1 - b1 - 1
                            s2 = 10 + a2 - b2
                            s3 = a3 - b3
                            if (b1 > c1):
                                if ((b2 - 1) > c2 and b3 < c3):
                                    t1 = b1 - c1
                                    t2 = b2 - c2 - 1
                                    t3 = 10 + b3 - c3
                                    break
                                elif (b2 < c2 and (b1 - 1) > c1 and b3 > c3):
                                    t1 = b1 - c1 - 1
                                    t2 = 10 + b2 - c2
                                    t3 = b3 - c3
                                    break

    S1 = round(A, -2)
    S2 = round(B, -2)
    S3 = round(C, -2)

    S4 = s1 * 100 + s2 * 10 + s3
    S5 = t1 * 100 + t2 * 10 + t3

    D = [S4, S5][np.random.randint(0, 2)]

    N = [A, B, C]

    np.random.shuffle(N)

    E, F, G = N

    if(D == S4):
        T1 = A
        T2 = B
    else:
        T1 = B
        T2 = C

    boxone = "box{　　　}"

    stem = stem.format(D=D, E=E, F=F, G=G, boxone=boxone)
    answer = answer.format(T1=T1, T2=T2)
    comment = comment.format(A=A, B=B, C=C, S1=S1, S2=S2, S3=S3, D=D, S4=S4, S5=S5, T1=T1, T2=T2 )

    return stem, answer, comment


















# 3-1-1-52
def addandsub311_Stem_030():
    stem = "다음은 {N1}이와 친구들이 각각 일주일 동안 {exercise}를 {doing} 횟수입니다. {exercise}를 가장 많이 {doing} 학생과 가장 적게 {doing} 학생의 횟수의 차는 몇 회 인가요?\n$$표$$ {N1} : $$수식$${D}$$/수식$$회, {N2} : $$수식$${E}$$/수식$$회, {N3} : $$수식$${F}$$/수식$$회 $$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$회\n"
    comment = "(해설)\n" \
              "$$수식$${A} &gt; {B} &gt; {C}$$/수식$$ 이므로 가장 많이 {doing} {exercise} 횟수는 $$수식$${A}$$/수식$$회, " \
              "가장 적게 {doing} {exercise} 횟수는 $$수식$${C}$$/수식$$회입니다.\n" \
              "$$수식$$LEFT ($$/수식$${exercise} 횟수의 차$$수식$$ RIGHT ) ` = ` {A} ` - ` {C} ` = ` {S} LEFT ($$/수식$$회$$수식$$RIGHT )$$/수식$$\n\n"



    while 1:
        a1 = np.random.randint(5, 10)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(1, 10)

        b1 = np.random.randint(5, 10)
        b2 = np.random.randint(0, 10)
        b3 = np.random.randint(0, 10)

        c1 = np.random.randint(5, 10)
        c2 = np.random.randint(0, 10)
        c3 = np.random.randint(0, 10)

        A = a1 * 100 + a2 * 10 + a3
        B = b1 * 100 + b2 * 10 + b3
        C = c1 * 100 + c2 * 10 + c3

        if (a1 > b1):
            if (a1 != a2 or a1 != a3 or a2 != a3):
                if (a2 != 0 and a3 != 0):
                    if (A != B):
                        if ((a2 - 1) > b2 and a3 < b3):
                            if (b1 > c1):
                                if ((a2 - 1) > c2 and a3 < c3):
                                    t1 = a1 - c1
                                    t2 = a2 - c2 - 1
                                    t3 = 10 + a3 - c3
                                    break
                                elif (a2 < c2 and (a1 - 1) > c1 and a3 > c3):
                                    t1 = a1 - c1 - 1
                                    t2 = 10 + a2 - c2
                                    t3 = a3 - c3
                                    break
                        elif (a2 < b2 and (a1 - 1) > b1 and a3 > b3):
                            if (b1 > c1):
                                if ((a2 - 1) > c2 and a3 < c3):
                                    t1 = a1 - c1
                                    t2 = a2 - c2 - 1
                                    t3 = 10 + a3 - c3
                                    break
                                elif (a2 < c2 and (a1 - 1) > c1 and a3 > c3):
                                    t1 = a1 - c1 - 1
                                    t2 = 10 + a2 - c2
                                    t3 = a3 - c3
                                    break

    S = t1 * 100 + t2 * 10 + t3

    N1 = ["진영", "서훈", "수진", "장훈", "석원", "채원", "윤슬", "서연", "하은", "수빈"][np.random.randint(0, 10)]
    N2 = ["수호", "선희", "형주", "지아", "하준", "승민", "도현", "수영", "현준", "의찬"][np.random.randint(0, 10)]
    N3 = ["수지", "영호", "유수", "태환", "성민", "정호", "승현", "승리", "한솔", "나라"][np.random.randint(0, 10)]

    choice = np.random.randint(0, 3)
    exercise = ["줄넘기", "턱걸이", "팔굽혀펴기", "윗몸 일으키기"][choice]
    doing = ["넘은", "한", "한", "한"][choice]

    N = [A, B, C]
    np.random.shuffle(N)
    D, E, F = N

    stem = stem.format(D=D, E=E, F=F, N1=N1, N2=N2, N3=N3, exercise=exercise, doing=doing)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, C=C, S=S, exercise=exercise, doing=doing)

    return stem, answer, comment














# 3-1-1-56
def addandsub311_Stem_031():
    stem = "계산 결과를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$ 를 알맞게 써넣으세요.\n$$수식$${A} ` - ` {B}$$/수식$$    ○  $$수식$${C} ` - ` {D}$$/수식$$\n"
    answer = "(정답)\n$$수식$${T}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a1}``{a2}``{a3}``-``{b1}``{b2}``{b3}``=``{s1}``{s2}``{s3}$$/수식$$\n" \
              "$$수식$${c1}``{c2}``{c3}``-``{d1}``{d2}``{d3}``=``{t1}``{t2}``{t3}$$/수식$$\n" \
              "따라서 $$수식$${S1}$$/수식$$ {j1} $$수식$${S2}$$/수식$$ 보다 {T1}므로 $$수식$${S1}$$/수식$$ $$수식$${T}$$/수식$$ $$수식$${S2}$$/수식$$ 입니다.\n\n"



    while(1):
        a1 = np.random.randint(1,10)
        a2 = np.random.randint(0,10)
        a3 = np.random.randint(0,10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(1, 10)
        b3 = np.random.randint(1, 10)

        A = a1 * 100 + a2 * 10 + a3
        B = b1 * 100 + b2 * 10 + b3

        if (a1 > b1 and a2<b2 and a3<b3):
            if (a1 != a2 or a1 != a3 or a2 != a3):
                if (a2 != 0 and a3 != 0):
                    if (A != B):
                        s1 = a1-b1-1
                        s2 = 10+a2-b2-1
                        s3 = 10+a3-b3
                        break

    S1 = s1 * 100 + s2 * 10 + s3

    while (1):
        c1 = np.random.randint(1, 10)
        c2 = np.random.randint(0, 10)
        c3 = np.random.randint(0, 10)

        d1 = np.random.randint(1, 10)
        d2 = np.random.randint(1, 10)
        d3 = np.random.randint(1, 10)

        C = c1 * 100 + c2 * 10 + c3
        D = d1 * 100 + d2 * 10 + d3

        if (c1 > d1 and c2 < d2 and c3 < d3):
            if (c1 != c2 or c1 != c3 or c2 != c3):
                if (c2 != 0 and c3 != 0):
                    t1 = c1 - d1 - 1
                    t2 = 10 + c2 - d2 - 1
                    t3 = 10 + c3 - d3
                    break

    S2 = t1 * 100 + t2 * 10 + t3

    if(S1>S2):
        T1 = "크"
        T = "&gt;"
    elif(S1<S2):
        T1 = "작으"
        T = "&lt;"
    else:
        T1 = "같으"
        T = "="

    j1 = proc_jo(S1, -1)


    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(T=T)
    comment = comment.format(a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, c1=c1, c2=c2, c3=c3, d1=d1, d2=d2, d3=d3, s1=s1, s2=s2, s3=s3, t1=t1, t2=t2, t3=t3, S1=S1, S2=S2, T1=T1, T=T, j1=j1)

    return stem, answer, comment





# 3-1-1-57
def addandsub311_Stem_032():
    stem = "계산 결과가 가장 {choice} 것을 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${A} ` - ` {B}$$/수식$$    ㉡ $$수식$${C} ` - ` {D}$$/수식$$    ㉢ $$수식$${E} ` - ` {F}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{S}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${A} ` - ` {B} = {T1}$$/수식$$\n" \
              "㉡ $$수식$${C} ` - ` {D} = {T2}$$/수식$$\n" \
              "㉢ $$수식$${E} ` - ` {F} = {T3}$$/수식$$\n" \
              "따라서 $$수식$${J} &gt; {H} &gt; {G}$$/수식$$ 이므로 계산 결과가 가장 {choice} 것은 {S} 입니다.\n\n"



    while 1:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(0, 10)
        a3 = np.random.randint(0, 10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(1, 10)
        b3 = np.random.randint(1, 10)

        A = a1 * 100 + a2 * 10 + a3
        B = b1 * 100 + b2 * 10 + b3

        if a1 > b1 and a2 < b2 and a3 < b3:
            if a1 != a2 or a1 != a3 or a2 != a3:
                if a2 != 0 and a3 != 0:
                    if A != B:
                        s1 = a1 - b1 - 1
                        s2 = 10 + a2 - b2 - 1
                        s3 = 10 + a3 - b3
                        break

    T1 = s1 * 100 + s2 * 10 + s3

    while (1):
        c1 = np.random.randint(1, 10)
        c2 = np.random.randint(0, 10)
        c3 = np.random.randint(0, 10)

        d1 = np.random.randint(1, 10)
        d2 = np.random.randint(1, 10)
        d3 = np.random.randint(1, 10)

        C = c1 * 100 + c2 * 10 + c3
        D = d1 * 100 + d2 * 10 + d3

        if (c1 > d1 and c2 < d2 and c3 < d3):
            if (c1 != c2 or c1 != c3 or c2 != c3):
                if (c2 != 0 and c3 != 0):
                    if(c1!=a1 and c2!=a2 and c3!=a3):
                        t1 = c1 - d1 - 1
                        t2 = 10 + c2 - d2 - 1
                        t3 = 10 + c3 - d3
                        break

    T2 = t1 * 100 + t2 * 10 + t3

    while (1):
        e1 = np.random.randint(1, 10)
        e2 = np.random.randint(0, 10)
        e3 = np.random.randint(0, 10)

        f1 = np.random.randint(1, 10)
        f2 = np.random.randint(1, 10)
        f3 = np.random.randint(1, 10)

        E = e1 * 100 + e2 * 10 + e3
        F = f1 * 100 + f2 * 10 + f3

        if (e1 > f1 and e2 < f2 and e3 < f3):
            if (e1 != e2 or e1 != e3 or e2 != e3):
                if (e2 != 0 and e3 != 0):
                    if(e1!=a1 and e2!=a2 and e3!=a3 and e1!=c1 and e2!=c2 and e3!=c3):
                        u1 = e1 - f1 - 1
                        u2 = 10 + e2 - f2 - 1
                        u3 = 10 + e3 - f3
                        break

    T3 = u1 * 100 + u2 * 10 + u3

    if(T1>T2):
        if(T1>T3):
            if(T2>T3):
                J = T1
                H = T2
                G = T3
            else:
                J = T1
                H = T3
                G = T2
        else:
            J = T3
            H = T1
            G = T2
    elif(T2>T1):
        if(T3>T1):
            if(T2>T3):
                J = T2
                H = T3
                G = T1
            else:
                J = T3
                H = T2
                G = T1
        else:
            J = T2
            H = T1
            G = T3


    if(G == T1):
        S = "㉠"
    elif(G == T2):
        S = "㉡"
    else:
        S = "㉢"

    choice =["작은", "큰"][np.random.randint(0, 2)]
    if choice == "큰" :
        if J == T1 :
            S = "㉠"
        elif J == T2 :
            S = "㉡"
        else :
            S = "㉢"


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, choice=choice)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, T1=T1, T2=T2, T3=T3, S=S, G=G, H=H, J=J, choice=choice)

    return stem, answer, comment













# 3-1-1-58
def addandsub311_Stem_033():
    stem = "가장 큰 수와 가장 작은 수의 차를 구해 보세요.\n$$표$$ $$수식$${E}$$/수식$$  $$수식$${F}$$/수식$$  $$수식$${G}$$/수식$$  $$수식$${H}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A} &gt; {D} &gt; {C} &gt; {B}$$/수식$$ 이므로 가장 큰 수는 $$수식$$ {A} $$/수식$$, 가장 작은 수는 $$수식$$ {B} $$/수식$$입니다.\n" \
              "따라서\n" \
              "$$수식$${a1}``{a2}``{a3}``-``{b1}``{b2}``{b3}``=``{s1}``{s2}``{s3}$$/수식$$\n" \



    while(1):
        a1 = np.random.randint(1,10)
        a2 = np.random.randint(0,10)
        a3 = np.random.randint(0,10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(1, 10)
        b3 = np.random.randint(1, 10)

        c1 = np.random.randint(1, 10)
        c2 = np.random.randint(0, 10)
        c3 = np.random.randint(0, 10)

        d1 = np.random.randint(1, 10)
        d2 = np.random.randint(1, 10)
        d3 = np.random.randint(1, 10)

        A = a1 * 100 + a2 * 10 + a3
        B = b1 * 100 + b2 * 10 + b3
        C = c1 * 100 + c2 * 10 + c3
        D = d1 * 100 + d2 * 10 + d3

        if(A>C>B and A>D>C):
            if (a1 > b1 and a2 < b2 and a3 < b3):
                if (a1 != a2 or a1 != a3 or a2 != a3):
                    if (a2 != 0 and a3 != 0):
                        if (c1 != c2 or c1 != c3 or c2 != c3):
                            if (c2 != 0 and c3 != 0):
                                s1 = a1-b1-1
                                s2 = 10+a2-b2-1
                                s3 = 10+a3-b3
                                break

    S = s1*100+s2*10+s3
    N = [A,B,C,D]

    np.random.shuffle(N)

    E, F, G, H = N

    stem = stem.format(E=E,F=F,G=G,H=H)
    answer = answer.format(S=S)
    comment = comment.format(A=A,B=B,a1=a1,a2=a2,a3=a3,b1=b1,b2=b2,b3=b3,s1=s1,s2=s2,s3=s3,C=C,D=D)

    return stem, answer, comment




# 3-1-1-59
def addandsub311_Stem_034():
    stem = "□ 안에 들어갈 수 있는 가장 큰 세자리 수를 구해 보세요.\n$$표$$ $$수식$${A} ` - $$/수식$$□$$수식$$&gt; ` {B}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A} ` - $$/수식$$□$$수식$$ = ` {B}$$/수식$$ {ra} 하면\n" \
              "□$$수식$$= ` {A} ` - ` {B} ` = ` {S1}$$/수식$$\n" \
              "$$수식$${A} ` - $$/수식$$□$$수식$$&gt; ` {B}$$/수식$$ 에서 □는 $$수식$${S1}$$/수식$$보다 작아야 합니다.\n" \
              "따라서 □ 안에 들어갈 수 있는 가장 큰 세 자리 수는 $$수식$${S}$$/수식$$입니다.\n\n" \

    while(1):
        a1 = np.random.randint(1,10)
        a2 = np.random.randint(0,10)
        a3 = np.random.randint(0,10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(1, 10)
        b3 = np.random.randint(1, 10)

        A = a1 * 100 + a2 * 10 + a3
        B = b1 * 100 + b2 * 10 + b3

        if (a1 > b1+1 and a2 < b2 and a3 < b3):
            if (a1 != a2 or a1 != a3 or a2 != a3):
                if (a2 != 0 and a3 != 0):
                    s1 = a1-b1-1
                    s2 = 10+a2-b2-1
                    s3 = 10+a3-b3
                    break

    S1 = s1*100+s2*10+s3
    S = S1-1

    if int((str(B))[-1]) == 2 or int((str(B))[-1]) == 4 or int((str(B))[-1]) == 5 or int((str(B))[-1]) == 9 :
        ra = "라"
    else :
        ra = "이라"


    stem = stem.format(A=A, B=B)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, S1=S1, S=S, ra=ra)

    return stem, answer, comment







# 3-1-1-61
def addandsub311_Stem_035():
    stem = "{N}에서 출발하는 기차에 $$수식$${A}$$/수식$$명이 탔습니다. 다음 역에서 $$수식$${B}$$/수식$$명이 내리고 새로 탄 사람은 없었습니다. 기차에는 몇 명이 타고 있나요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 기차에``탄``사람``수 RIGHT ) - LEFT ( 내린``사람``수 RIGHT ) $$/수식$$ \n $$수식$$ = {A} - {B} = {S} ` LEFT ( 명 RIGHT )$$/수식$$\n\n"



    while(1):
        a1 = np.random.randint(1,10)
        a2 = np.random.randint(0,10)
        a3 = np.random.randint(0,10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(1, 10)
        b3 = np.random.randint(1, 10)

        A = a1 * 100 + a2 * 10 + a3
        B = b1 * 100 + b2 * 10 + b3

        if (a1 > b1 and a2 < b2 and a3 < b3):
            if (a1 != a2 or a1 != a3 or a2 != a3):
                if (a2 != 0 and a3 != 0):
                    s1 = a1-b1-1
                    s2 = 10+a2-b2-1
                    s3 = 10+a3-b3
                    break

    S = s1*100 + s2*10 + s3

    N = ["서울역", "대구역", "춘천역", "경주역", "광주역", "수원역", "동대구역", "부산역", "천안역", "대전역"][np.random.randint(0, 10)]

    stem = stem.format(A=A, B=B, N=N)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, S=S)

    return stem, answer, comment





# 3-1-1-62
def addandsub311_Stem_036():
    stem = "㉠, ㉡, ㉢에 들어갈 알맞은 숫자를 차례대로 써넣으세요.\n             $$수식$${a1}``{a2}``{a3}$$/수식$$ \n    $$수식$$-$$/수식$$   ㉠ ㉡ $$수식$${b3}$$/수식$$ \n──────\n             $$수식$${s1}``{s2}$$/수식$$ ㉢\n"
    answer = "(정답)\n㉠ $$수식$${b1}$$/수식$$, ㉡ $$수식$${b2}$$/수식$$, ㉢ $$수식$${s3}$$/수식$$\n"
    comment = "(해설)\n일의 자리 계산은 $$수식$$10 + {a3} ` - ` {b3} ` = $$/수식$$㉢에서 ㉢$$수식$$= ` {s3}$$/수식$$,\n" \
              "십의 자리 계산은 $$수식$${a2} ` - ` 1 ` + ` 10 ` - $$/수식$$㉡$$수식$$= ` {s2}$$/수식$$에서 ㉡$$수식$$= ` {b2}$$/수식$$,\n" \
              "백의 자리 계산은 $$수식$${a1} ` - ` 1 ` - `$$/수식$$㉠$$수식$$= ` {s1}$$/수식$$에서 ㉠$$수식$$= ` {b1}$$/수식$$ 입니다.\n" \
              "따라서 ㉠ $$수식$${b1}$$/수식$$, ㉡ $$수식$${b2}$$/수식$$, ㉢ $$수식$${s3}$$/수식$$ 입니다.\n\n"



    while(1):
        a1 = np.random.randint(1,10)
        a2 = np.random.randint(0,10)
        a3 = np.random.randint(0,10)

        b1 = np.random.randint(1, 10)
        b2 = np.random.randint(1, 10)
        b3 = np.random.randint(1, 10)

        A = a1 * 100 + a2 * 10 + a3
        B = b1 * 100 + b2 * 10 + b3

        if (a1 > b1+1 and a2 < b2 and a3 < b3):
            if (a1 != a2 or a1 != a3 or a2 != a3):
                if (a2 != 0 and a3 != 0):
                    s1 = a1-b1-1
                    s2 = 10+a2-b2-1
                    s3 = 10+a3-b3
                    break

    S = s1*100 + s2*10 + s3

    stem = stem.format(A=A, B=B, a1=a1, a2=a2, a3=a3, b3=b3, s1=s1, s2=s2)
    answer = answer.format(b1=b1, b2=b2, s3=s3)
    comment = comment.format(a3=a3, b3=b3, s3=s3, a2=a2, s2=s2, b2=b2, a1=a1, b1=b1, s1=s1)

    return stem, answer, comment



