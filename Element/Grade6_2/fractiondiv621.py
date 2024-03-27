import numpy as np
import random
import math
import fractions












answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤",
    5: "⑥",
    6: "⑦",
    7: "⑧",
    8: "⑨",
    9: "⑩",
    10: "⑪",
    11: "⑫",
    12: "⑬",
    13: "⑭",
    14: "⑮"
}


















answer_kodict = {
    0: "㉠",
    1: "㉡",
    2: "㉢",
    3: "㉣",
    4: "㉤"
}

















answer_kodict2 = {
    0: 'ㄱ',
    1: 'ㄴ',
    2: 'ㄷ',
    3: 'ㄹ',
    4: 'ㅁ'
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




















def name_jo(num):
    # 이
    if bool_jo(num):
        return "이"
    return ""














def getdivisor(num):
    if num < 1:
        return 0
    divisor = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)

    return divisor














def is_coprime(n1, n2):
    divisor1 = getdivisor(n1)
    divisor2 = getdivisor(n2)
    inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
    if len(inter) > 1:
        return False
    else:
        return True



















def get_GCD(n1, n2):  # 최대공약수
    divisor1 = getdivisor(n1)
    divisor2 = getdivisor(n2)
    inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
    inter.sort()
    maxnum = inter[-1]
    return maxnum


















def get_LCM(n1, n2):  # 최소공배수
    divisor1 = getdivisor(n1)
    divisor2 = getdivisor(n2)
    inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
    inter.sort()
    maxnum = inter[-1]
    if maxnum == 1:
        lcm = n1 * n2
    else:
        lcm = int(n1 * n2 / maxnum)
    return lcm



















def giyak(boon_ja, boon_mo):
    giyak_frac = fractions.Fraction(boon_ja, boon_mo)

    giyak_boon_ja = giyak_frac.numerator

    giyak_boon_mo = giyak_frac.denominator

    return giyak_boon_ja, giyak_boon_mo







def get_yaksu_list(a):
    temp_list = []

    for i_dx in range(a + 1):
        if i_dx == 0:
            pass
        else:
            if a % i_dx == 0:
                temp_list.append(i_dx)

    return temp_list


















# 6-2-1-02
def fractiondiv621_Stem_001():
    stem = "빈칸에 알맞은 수를 써넣으세요.\n$$수식$${B} over {A} DIV {C} over {A} = $$/수식$$ $$수식$${box1}$$/수식$$\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${B} over {A} DIV {C} over {A} = {B} div {C} = {D}$$/수식$$\n\n"



    box1 = 'box{　　　}'

    while True:
        A = np.random.randint(10, 100)
        B = np.random.randint(10, 51)
        C = np.random.randint(2, 10)
        D = int(B / C)

        if A > B and is_coprime(A, B) and is_coprime(A, C) and B % C == 0 and D == B / C:
            break

    stem = stem.format(A=A, B=B, C=C, box1=box1)
    answer = answer.format(D=D)
    comment = comment.format(A=A, B=B, C=C, D=D)

    return stem, answer, comment



    # while True:
    #     A, B = random.sample(list(range(11, 20)), 2)
    #     C = np.random.randint(2, 10)
    #     if A > B and is_coprime(A, B) and is_coprime(A, C) and B % C == 0:
    #         break




































# 6-2-1-03
def fractiondiv621_Stem_002():
    stem = "계산 결과가 $$수식$$1$$/수식$$보다 작은 것을 찾아 기호를 써 보세요.\n$$표$$㉠ {y1}     ㉡ {y2}     ㉢ {y3}$$/표$$\n"
    answer = "(정답)\n{K}\n"
    comment = "(해설)\n" \
              "㉠ {s1}\n㉡ {s2}\n㉢ {s3}\n따라서 계산 결과가 $$수식$$1$$/수식$$보다 작은 것은 {K}입니다.\n\n"



    while True:
        A, B, C, D, E, F = random.sample(list(range(2, 10)), 6)

        if is_coprime(A, B) and is_coprime(A, C) and is_coprime(D, B) and is_coprime(D, C) and B > C and B % C != 0 and E % F != 0 and E > F:
            break


    G = int(B / C)

    H = B % C

    I = int(E / F)

    J = E % F

    pick = np.random.randint(0, 6)

    x1 = '$$수식$${B} over {A} DIV {C} over {A}$$/수식$$'.format(A=A, B=B, C=C)
    x2 = '$$수식$${C} over {D} DIV {B} over {D}$$/수식$$'.format(B=B, C=C, D=D)
    x3 = '$$수식$${E} over {B} DIV {F} over {B}$$/수식$$'.format(B=B, E=E, F=F)

    new1_H, new1_C = giyak(H, C)

    new2_C, new2_B = giyak(C, B)

    new3_J, new3_F = giyak(J, F)

    p1 = '$$수식$${B} over {A} DIV {C} over {A} = {B} DIV {C} = {G} {new1_H} over {new1_C}$$/수식$$'.format(A=A, B=B, C=C, G=G, H=H, new1_H=new1_H, new1_C=new1_C)
    p2 = '$$수식$${C} over {D} DIV {B} over {D} = {C} DIV {B} = {new2_C} over {new2_B}$$/수식$$'.format(B=B, C=C, D=D, new2_C=new2_C, new2_B=new2_B)
    p3 = '$$수식$${E} over {B} DIV {F} over {B} = {E} DIV {F} = {I} {new3_J} over {new3_F}$$/수식$$'.format(B=B, E=E, F=F, I=I, J=J, new3_J=new3_J, new3_F=new3_F)

    x = [[x1, x2, x3], [x3, x2, x1], [x2, x1, x3], [x2, x3, x1], [x3, x1, x2], [x1, x3, x2]][pick]

    y1, y2, y3 = x

    p = [[p1, p2, p3], [p3, p2, p1], [p2, p1, p3], [p2, p3, p1], [p3, p1, p2], [p1, p3, p2]][pick]

    s1, s2, s3 = p

    K = ['㉡', '㉡', '㉠', '㉠', '㉢', '㉢'][pick]


    stem = stem.format(y1=y1, y2=y2, y3=y3)
    answer = answer.format(K=K)
    comment = comment.format(K=K, s1=s1, s2=s2, s3=s3)

    return stem, answer, comment




























# 6-2-1-04
def fractiondiv621_Stem_003():
    stem = "계산 결과를 비교하여 $$수식$${box}$$/수식$$안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${B} over {A} DIV {C} over {A} ```` {box} ```` {E} over {D} DIV {F} over {D}$$/수식$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${B} over {A} DIV {C} over {A} = {B} DIV {C} = {G}$$/수식$$, " \
              "$$수식$${E} over {D} DIV {F} over {D} = {E} DIV {F} = {H}$$/수식$$\n" \
              "→ $$수식$${G} {S} {H}$$/수식$$\n\n"


    box = '□'

    while True:
        A, B, C, E, F = random.sample(list(range(2, 10)), 5)
        D = np.random.randint(11, 20)
        if is_coprime(A, B) and is_coprime(A, C) and is_coprime(D, E) and is_coprime(D, F) and B % C == 0 and E % F == 0:
            break

    G = int(B / C)
    H = int(E / F)

    if G > H:
        S = '&gt;'
    elif G < H:
        S = '&lt;'
    else:
        S = '='


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, box=box)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, S=S)

    return stem, answer, comment





































# 6-2-1-06
def fractiondiv621_Stem_004():
    stem = "계산 결과가 가장 큰 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${B} over {A} DIV {C} over {A}$$/수식$$     ㉡ $$수식$${E} over {D} DIV {F} over {D}$$/수식$$     ㉢ $$수식$${I} over {G} DIV {J} over {H}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{Q}\n"
    comment = "(해설)\n" \
              "$$수식$${B} over {A} DIV {C} over {A} = {B} DIV {C} = {N}$$/수식$$\n" \
              "$$수식$${E} over {D} DIV {F} over {D} = {E} DIV {F} = {M}$$/수식$$\n" \
              "$$수식$${I} over {G} DIV {J} over {H} = {K} over {H} DIV {J} over {H} = {K} DIV {J} = {L}$$/수식$$\n" \
              "→ $$수식$${S1} &gt; {S2} &gt; {S3}$$/수식$$이므로 계산 결과가 가장 큰 것은 {Q}입니다.\n\n"

    # while True:
    #     A, C, F, G, J = random.sample(list(range(2, 10)), 5)
    #     D = np.random.randint(11, 20)
    #     H = G * 2
    #     L, M, N = random.sample(list(range(2, 5)), 3)
    #
    #     B = C * N
    #     E = F * M
    #     I = J * L
    #
    #     L = L * 2
    #     K = I * 2
    #
    #     if K % J == 0 and is_coprime(A, B) and is_coprime(D, E) and is_coprime(I, G) and L != M and L != N:
    #         break


    while True:
        while True:
            A = np.random.randint(2, 10)
            B = np.random.randint(1, 10)
            C = np.random.randint(1, 10)

            if is_coprime(A, B) and is_coprime(A, C) and B % C == 0:
                break

        while True:
            D = np.random.randint(10, 100)
            E = np.random.randint(10, 100)
            F = np.random.randint(1, 10)

            if is_coprime(D, E) and D > E and E % F == 0:
                break


        while True:
            G = np.random.randint(2, 10)
            H = np.random.randint(10, 100)
            I = np.random.randint(1, 10)
            J = np.random.randint(1, 10)

            if H % G == 0 and is_coprime(H, I) and is_coprime(H, J) and I % J == 0:
                break


        K = int((H / G) * I)

        N = int(B / C)
        if N != B / C:
            continue

        M = int(E / F)
        if M != E / F:
            continue

        L = int(K / J)
        if L != K / J:
            continue

        if N == M or N == L or M == L:
            continue

        ss = [L, M, N]
        ss.sort()
        ss.reverse()

        S1, S2, S3 = ss

        if N == S1:
            Q = '㉠'
        elif M == S1:
            Q = '㉡'
        else:
            Q = '㉢'

        break


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J)
    answer = answer.format(Q=Q)
    comment = comment.format(Q=Q, A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, M=M, N=N, S1=S1, S2=S2, S3=S3)

    return stem, answer, comment
































# 6-2-1-07
def fractiondiv621_Stem_005():
    stem = "계산 결과가 다른 하나를 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${B} over {A} DIV {C} over {A}$$/수식$$     ㉡ $$수식$${E} over {D} DIV {F} over {D}$$/수식$$     ㉢ $$수식$${H} over {G} DIV {I} over {G}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{Q}\n"
    comment = "(해설)\n" \
              "$$수식$${B} over {A} DIV {C} over {A} = {B} DIV {C} = {X1}$$/수식$$\n" \
              "$$수식$${E} over {D} DIV {F} over {D} = {E} DIV {F} = {X2}$$/수식$$\n" \
              "$$수식$${H} over {G} DIV {I} over {G} = {H} DIV {I} = {X3}$$/수식$$\n" \
              "따라서 계산 결과가 다른 하나는 {Q}입니다.\n\n"



    while True:
        A, D, G = random.sample(list(range(11, 20)), 3)
        C, F, I = random.sample(list(range(2, 10)), 3)
        J, K = random.sample(list(range(2, 5)), 2)

        pick = np.random.randint(0, 3)
        muls = [[K, J, J], [J, K, J], [J, J, K]][pick]

        B = C * muls[0]
        E = F * muls[1]
        H = I * muls[2]

        if is_coprime(A, B) and is_coprime(D, E) and is_coprime(G, H):
            break


    X1, X2, X3 = muls

    Q = answer_kodict[pick]


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I)
    answer = answer.format(Q=Q)
    comment = comment.format(Q=Q, A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, X1=X1, X2=X2, X3=X3)

    return stem, answer, comment


























# 6-2-1-08
def fractiondiv621_Stem_006():
    stem = "가장 큰 수를 가장 작은 수로 나눈 값을 구해 보세요.\n$$표$$$$수식$${B} over {A}$$/수식$$     $$수식$${C} over {A}$$/수식$$     $$수식$${D} over {A}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${E} ` {F} over {G}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${X1} over {A} &gt; {X2} over {A} &gt; {X3} over {A}$$/수식$$\n" \
              "→ $$수식$${X1} over {A} DIV {X3} over {A} = {X1} DIV {X3} = {E} {F} over {G}$$/수식$$\n\n"


    while True:
        A = np.random.randint(11, 20)
        B, C, D = random.sample(list(range(2, 10)), 3)

        X = [B, C, D]
        X.sort()
        X.reverse()
        X1, X2, X3 = X

        if is_coprime(A, B) and is_coprime(A, C) and is_coprime(A, D) and X1 % X3 != 0:
            break


    E = int(X1 / X3)
    F = X1 % X3
    G = X3

    F, G = giyak(F, G)


    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(E=E, F=F, G=G)
    comment = comment.format(A=A, E=E, F=F, G=G, X1=X1, X2=X2, X3=X3)

    return stem, answer, comment





























# 6-2-1-09
def fractiondiv621_Stem_007():
    stem = "㉠과 ㉡의 차를 구해 보세요.\n$$표$$㉠ $$수식$${B} over {A} DIV {C} over {A}$$/수식$$     ㉡ $$수식$${E} over {D} DIV {F} over {D}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${I}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${B} over {A} DIV {C} over {A} = {B} DIV {C} = {G}$$/수식$$\n" \
              "㉡ $$수식$${E} over {D} DIV {F} over {D} = {E} DIV {F} = {H}$$/수식$$\n" \
              "→ ㉠$$수식$$-$$/수식$$㉡$$수식$$= {G} - {H} = {I}$$/수식$$\n\n"


    while True:
        A, D = random.sample(list(range(11, 20)), 2)
        C, F = random.sample(list(range(2, 10)), 2)
        G, H = random.sample(list(range(2, 5)), 2)

        B = C * G
        E = F * H

        I = G - H

        if is_coprime(A, B) and is_coprime(D, E) and I > 0:
            break


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F)
    answer = answer.format(I=I)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I)

    return stem, answer, comment































# 6-2-1-11
def fractiondiv621_Stem_008():
    stem = "{P1}가 물을 $$수식$${B} over {A} `` rm L$$/수식$$, {P2}는 $$수식$${C} over {A} `` rm L$$/수식$$ 마셨습니다. {P1}가 마신 물의 양은 {P2}가 마신 물의 양의 몇 배인지 구해 보세요.\n"
    answer = "(정답)\n$$수식$${D} ` {E} over {F}$$/수식$$배\n"
    comment = "(해설)\n" \
              "$$수식$${B} over {A} DIV {C} over {A} = {B} DIV {C} = {B} over {C} = {D} {E} over {F}$$/수식$$배\n" \
              "따라서 {P1}가 마신 물의 양은 {P2}가 마신 물의 양의 $$수식$${D} {E} over {F}$$/수식$$배입니다.\n\n"


    P1, P2 = random.sample(['현주', '진아', '민수', '은지', '민희', '지효', '민서', '선미', '수지', '영호', '은서', '선주'], 2)

    while True:
        A, B, C = random.sample(list(range(2, 10)), 3)

        if is_coprime(A, B) and is_coprime(A, C) and B > C and B % C != 0:
            break


    D = int(B / C)
    E = B % C
    F = C

    E, F = giyak(E, F)


    stem = stem.format(A=A, B=B, C=C, P1=P1, P2=P2)
    answer = answer.format(D=D, E=E, F=F)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, P1=P1, P2=P2)

    return stem, answer, comment


































# 6-2-1-12
def fractiondiv621_Stem_009():
    stem = "㉠에 알맞은 수를 구해 보세요.\n$$표$$ $$수식$${{㉠}} over {A}$$/수식$$ $$수식$$DIV$$/수식$$ $$수식$${B} over {A}$$/수식$$ $$수식$$ = {C}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${{㉠}} over {A} DIV {B} over {A} =$$/수식$$㉠$$수식$$DIV {B} = {C}$$/수식$$이므로 ㉠$$수식$$= {D}$$/수식$$입니다.\n\n"


    #C = '㉠'

    while True:
        A = random.randint(11,20)
        D = random.randint(11,20)
        B = random.randint(2,9)
        if math.gcd(A,D) == 1 and D%B == 0: break


    C = int(D/B)


    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(D=D)
    comment = comment.format(A=A, B=B, C=C, D=D)

    return stem, answer, comment




























# 6-2-1-13
def fractiondiv621_Stem_010():
    stem = "{P1}이는 물 $$수식$${B} over {A} `` rm L$$/수식$$를 한 컵에 $$수식$${C} over {A} `` rm L$$/수식$$씩 나누어 담고, {P2}이는 물 $$수식$${E} over {D} `` rm L$$/수식$$를 한 컵에 $$수식$${F} over {D} `` rm L$$/수식$$씩 나누어 담으려고 합니다. {P1}이와 {P2}이가 각자 가지고 있는 물을 남김없이 컵에 나누어 담으려면 컵은 모두 몇 개 필요한가요?\n"
    answer = "(정답)\n$$수식$${I}$$/수식$$개\n"
    comment = "(해설)\n" \
              "{P1}: $$수식$${B} over {A} DIV {C} over {A} = {B} DIV {C} = {G} LEFT ($$/수식$$컵$$수식$$RIGHT )$$/수식$$\n" \
              "{P2}: $$수식$${E} over {D} DIV {F} over {D} = {E} DIV {F} = {H} LEFT ($$/수식$$컵$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 필요한 전체 컵의 수는 $$수식$${G} + {H} = {I} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    P1, P2 = random.sample(['우영', '승연', '소연', '정연', '주형', '선민', '영신', '태운'], 2)

    while True:
        A, D = random.sample(list(range(11, 20)), 2)
        C, F = random.sample(list(range(2, 10)), 2)
        G, H = random.sample(list(range(2, 5)), 2)
        B = C * G
        E = F * H

        if is_coprime(A, B) and is_coprime(D, E):
            break

    I = G + H


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, P1=P1, P2=P2)
    answer = answer.format(I=I)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, P1=P1, P2=P2)

    return stem, answer, comment































# 6-2-1-14
def fractiondiv621_Stem_011():
    stem = "다음 $$수식$$&lt;$$/수식$$조건$$수식$$&gt;$$/수식$$을 만족하는 분수의 나눗셈을 쓰시오.\n$$표$$‧ $$수식$${B} DIV {A}$$/수식$$을 이용하여 계산할 수 있습니다.\n‧ 분모가 $$수식$${C}$$/수식$$보다 작은 진분수의 나눗셈입니다.\n‧ 두 분수의 분모는 같습니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${B} over {H} ` div ` {A} over {H}$$/수식$$\n"
    comment = "(해설)\n" \
              "분모가 같은 분수끼리의 나눗셈은 분자끼리 나누어 계산할 수 있으므로 " \
              "$$수식$${B} over {box} DIV {A} over {box}$$/수식$${gwa1} 같이 나타낼 수 있습니다.\n" \
              "$$수식$${A} over {box}$$/수식$$의 분모가 $$수식$${C}$$/수식$$보다 작은 진분수이므로\n" \
              "$$수식$${box}$$/수식$$는 $$수식$${A}$$/수식$$보다 크고 $$수식$${C}$$/수식$$보다 작습니다.\n" \
              "따라서 $$수식$$&lt;$$/수식$$조건$$수식$$&gt;$$/수식$$을 만족하는 분수의 나눗셈은\n" \
              "$$수식$${B} over {H} DIV {A} over {H}$$/수식$$입니다.\n\n"


    box = '□'

    while True:
        A, B, C, H = random.sample(list(range(2, 10)), 4)

        # if is_coprime(A, B) and A > B and A < H and H < C:
        if is_coprime(A, B) and A > B and A == H - 1 and H + 1 == C:
            break

    if A == "2" or A == "4" or A == "5" or A == "9":
        gwa1 = "와"
    else:
        gwa1 = "과"


    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(A=A, B=B, H=H)
    comment = comment.format(A=A, B=B, C=C, H=H, box=box, gwa1=gwa1)

    return stem, answer, comment





























# 6-2-1-15
def fractiondiv621_Stem_012():
    stem = "$$수식$${B} over {A}$$/수식$${rur1} 어떤 수로 나누었더니 $$수식$${C} over {A}$$/수식$${ga1} 되었습니다. 어떤 수를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${D} ` {E} over {F}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 $$수식$${box}$$/수식$$라 하면 $$수식$${B} over {A} DIV {box} ` = {C} over {A}$$/수식$$,\n" \
              "$$수식$${box} ` = {B} over {A} DIV {C} over {A} = {B} DIV {C} = {B} over {C} = {D} {E} over {F}$$/수식$$\n\n"


    box = '□'

    while True:
        A, B = random.sample(list(range(11, 20)), 2)
        C = np.random.randint(2, 10)

        if A < B and is_coprime(A, B) and is_coprime(A, C) and B % C != 0:
            break

    D = int(B / C)
    E = B % C
    F = C

    E, F = giyak(E, F)

    if (str(B))[-1] == "2" or (str(B))[-1] == "4" or (str(B))[-1] == "5" or (str(B))[-1] == "9":
        rur1 = "를"
    else:
        rur1 = "을"

    if (str(C))[-1] == "2" or (str(C))[-1] == "4" or (str(C))[-1] == "5" or (str(C))[-1] == "9":
        ga1 = "가"
    else:
        ga1 = "이"


    stem = stem.format(A=A, B=B, C=C, rur1=rur1, ga1=ga1)
    answer = answer.format(D=D, E=E, F=F)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, box=box)

    return stem, answer, comment































# 6-2-1-16
def fractiondiv621_Stem_013():
    stem = "가로가 $$수식$${B} over {A} `` rm m$$/수식$$이고 넓이가 $$수식$${C} over {A} `` rm m^2$$/수식$$인 직사각형이 있습니다. 이 직사각형의 둘레는 몇 $$수식$$rm m$$/수식$$인지 구해 보세요.\n"
    answer = "(정답)\n$$수식$${M} ` {N} over {O} ` rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$직사각형의 세로$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {C} over {A} DIV {B} over {A} = {C} DIV {B} = {C} over {B} = {D} {E} over {F} LEFT ( rm m RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$직사각형의 둘레$$수식$$RIGHT ) = LEFT ( {B} over {A} + {D} {E} over {F} RIGHT ) TIMES 2$$/수식$$\n" \
              "$$수식$$= LEFT ( {B} over {A} + {H} over {G} RIGHT ) TIMES 2 = LEFT ( {J} over {I} + {K} over {I} RIGHT ) TIMES 2$$/수식$$\n" \
              "$$수식$${L} over {I} TIMES 2 = {L2} over {I} = {M} {N} over {O} LEFT ( rm m RIGHT )$$/수식$$\n\n"


    while True:
        A, B, C = random.sample(list(range(2, 10)), 3)

        if B < C and is_coprime(A, B) and is_coprime(A, C) and is_coprime(B, C):
            break

    D = int(C / B)
    E = C % B
    F = B

    E, F = giyak(E, F)

    G = F
    H = F * D + E

    I = get_LCM(A, G)
    J = int(I / A) * B
    K = int(I / G) * H

    L = J + K
    L2 = L * 2

    # gcd = get_GCD(L2, I)
    M = int(L2 / I)

    N, O = giyak(L2 % I, I)


    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(M=M, N=N, O=O)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, L2=L2, M=M, N=N, O=O)

    return stem, answer, comment



































# 6-2-1-17
def fractiondiv621_Stem_014():
    stem = "빈칸에 알맞은 수를 써넣으세요.\n$$수식$${B} over {A} DIV {D} over {C} = `$$/수식$$ $$수식$$ {box}$$/수식$$\n"
    answer = "(정답)\n$$수식$${I} ` {H} over {G}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${B} over {A} DIV {D} over {C} = {F} over {E} DIV {G} over {E} = {F} DIV {G} = {F} over {G} = {I} {H} over {G}$$/수식$$\n\n"


    box = '□'

    while True:
        A, B, C, D = random.sample(list(range(2, 10)), 4)
        E = get_LCM(A, C)
        F = int(E / A * B)
        G = int(E / C * D)

        if A > B and C > D and is_coprime(A, B) and is_coprime(C, D) and F > G and is_coprime(F, G):
            break

    I = int(F / G)
    H = F % G

    H, G = giyak(H, G)


    stem = stem.format(A=A, B=B, C=C, D=D, box=box)
    answer = answer.format(G=G, H=H, I=I)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I)

    return stem, answer, comment


































# 6-2-1-18
def fractiondiv621_Stem_015():
    stem = "계산 결과가 다른 하나를 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${B} over {A} DIV {D} over {C}$$/수식$$     ㉡ $$수식$${F} over {E} DIV {H} over {G}$$/수식$$\n㉢ $$수식$${J} over {I} DIV {L} over {K}$$/수식$$     ㉣ $$수식$${N} over {M} DIV {P} over {O}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{Q}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${B} over {A} DIV {D} over {C} = {B} over {A} DIV {Y1} over {A} = {X1}$$/수식$$\n" \
              "㉡ $$수식$${F} over {E} DIV {H} over {G} = {F} over {E} DIV {Y2} over {E} = {X2}$$/수식$$\n" \
              "㉢ $$수식$${J} over {I} DIV {L} over {K} = {Y3} over {K} DIV {L} over {K} = {X3}$$/수식$$\n" \
              "㉣ $$수식$${N} over {M} DIV {P} over {O} = {Y4} over {O} DIV {P} over {O} = {X4}$$/수식$$\n" \
              "따라서 계산 결과가 다른 하나는 {Q}입니다.\n\n"


    while True:
        C, D, G, H, I, J, M, N = random.sample(list(range(2, 10)), 8)
        muls = [2, 2, 3, 3]

        np.random.shuffle(muls)
        A = C * muls[0]
        B = D * muls[0]
        E = G * muls[1]
        F = H * muls[1]
        K = I * muls[2]
        L = J * muls[2]
        O = M * muls[3]
        P = N * muls[3]

        if is_coprime(C, D) and is_coprime(G, H) and is_coprime(I, J) and is_coprime(M, N):
            break


    pick = np.random.randint(0, 4)
    Q = answer_kodict[pick]

    X = [1, 1, 1, 1]
    Y1, Y2, Y3, Y4 = B, F, L, P

    if pick == 0:
        B = B * muls[0]
        Y1 = D * muls[0]
        X[pick] = muls[0]
    elif pick == 1:
        F = F * muls[1]
        Y2 = H * muls[1]
        X[pick] = muls[1]
    elif pick == 2:
        K = K * muls[2]
        Y3 = L * muls[2]
        X[pick] = muls[2]
    else:
        O = O * muls[3]
        Y4 = P * muls[3]
        X[pick] = muls[3]

    X1, X2, X3, X4 = X


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, M=M, N=N, O=O, P=P)
    answer = answer.format(Q=Q)
    comment = comment.format(Q=Q, A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, M=M, N=N, O=O, P=P, X1=X1, X2=X2, X3=X3, X4=X4, Y1=Y1, Y2=Y2, Y3=Y3, Y4=Y4)

    return stem, answer, comment




































# 6-2-1-19
def fractiondiv621_Stem_016():
    stem = "㉠보다 크고 ㉡보다 작은 자연수를 써 보세요.\n$$표$$㉠ $$수식$${B} over {A} DIV {D} over {C}$$/수식$$     ㉡ $$수식$${F} over {E} DIV {H} over {G}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${M}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${B} over {A} DIV {D} over {C} = {I} over {C} DIV {D} over {C} = {I} DIV {D} = {J}$$/수식$$\n" \
              "㉡ $$수식$${F} over {E} DIV {H} over {G} = {K} over {G} DIV {H} over {G} = {K} DIV {H} = {L}$$/수식$$\n" \
              "따라서 $$수식$${J}$$/수식$$보다 크고 $$수식$${L}$$/수식$$보다 작은 수는 $$수식$${M}$$/수식$$입니다.\n\n"


    while True:
        A, B = random.sample(list(range(2, 10)), 2)
        E, F = random.sample(list(range(10, 20)), 2)

        J = np.random.randint(2, 4)
        L = J + 2

        C = A * J
        D = B

        G = E * L
        H = F

        if is_coprime(A, B) and is_coprime(C, D) and is_coprime(E, F) and is_coprime(G, H):
            break


    I = B * J
    K = F * L

    M = J + 1


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H)
    answer = answer.format(M=M)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, M=M)

    return stem, answer, comment



































# 6-2-1-20
def fractiondiv621_Stem_017():
    stem = "빈칸에 알맞은 수를 써넣으세요.\n$$수식$${B} over {A} DIV {D} over {C} = ` {box1}$$/수식$$\n"
    answer = "(정답)\n$$수식$${F}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${B} over {A} DIV {D} over {C} = {E} over {C} DIV {D} over {C} = {E} DIV {D} = {F}$$/수식$$\n\n"


    box1 = '□'

    while True:
        A, B, D = random.sample(list(range(2, 10)), 3)
        muls = np.random.randint(2, 5)
        C = A * muls
        E = int(B * (C / A))
        F = int(E / D)

        if is_coprime(A, B) and is_coprime(C, D) and E > D and E % D == 0 and E == B * (C / A) and F == E / D:
            break


    stem = stem.format(A=A, B=B, C=C, D=D, box1=box1)
    answer = answer.format(F=F)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F)

    return stem, answer, comment

































# 6-2-1-21
def fractiondiv621_Stem_018():
    stem = "계산 결과를 비교하여 $$수식$${box}$$/수식$$안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${B} over {A} DIV {D} over {C} ```` {box} ```` {F} over {E} DIV {H} over {G}$$/수식$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${B} over {A} DIV {D} over {C} = {J} over {I} DIV {K} over {I} = {J} DIV {K} = {J1} over {K1} {sentence1}$$/수식$$,\n" \
              "$$수식$${F} over {E} DIV {H} over {G} = {N} over {M} DIV {O} over {M} = {N} DIV {O} = {N1} over {O1} {sentence2}$$/수식$$\n" \
              "→ $$수식$${saying1} {S} {saying2}$$/수식$$\n\n"


    box = '□'

    while True:
        A, B, C, D, E, F, G, H = random.sample(list(range(2, 10)), 8)

        I = A * C
        J = B * C
        K = A * D
        M = E * G
        N = F * G
        O = E * H

        J1, K1 = giyak(J, K)

        N1, O1 = giyak(N, O)

        L = int(J1 / K1)
        R = J1 % K1

        P = int(N1 / O1)
        Q = N1 % O1

        if Q != 0 and is_coprime(A, B) and is_coprime(C, D) and is_coprime(E, F) and is_coprime(G, H) and is_coprime(J, K) and is_coprime(Q, O) and is_coprime(I, M):
            break

    if L != 0:
        sentence1 = "= %s ` %s over %s" % (L, R, K1)
        saying1 = "%s ` %s over %s" % (L, R, K1)
    else:
        sentence1 = ""
        saying1 = "%s over %s" % (J1, K1)

    if P != 0:
        sentence2 = "= %s ` %s over %s" % (P, Q, O1)
        saying2 = "%s ` %s over %s" % (P, Q, O1)
    else:
        sentence2 = ""
        saying2 = "%s over %s" % (N1, O1)

    if J / K > N / O:
        S = '&gt;'
    elif J / K < N / O:
        S = '&lt;'
    else:
        S = '='


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, box=box)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, M=M, N=N, O=O, S=S, sentence1=sentence1, sentence2=sentence2, saying1=saying1, saying2=saying2, J1=J1, K1=K1, N1=N1, O1=O1)

    return stem, answer, comment
































# 6-2-1-22
def fractiondiv621_Stem_019():
    stem = "계산 결과가 $$수식$$1$$/수식$$보다 작은 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${B} over {A} DIV {D} over {C}$$/수식$$     ㉡ $$수식$${F} over {E} DIV {H} over {G}$$/수식$$     ㉢ $$수식$${J} over {I} DIV {L} over {K}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{Q}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${B} over {A} DIV {D} over {C} = {S1} {op1} 1$$/수식$$\n" \
              "㉡ $$수식$${F} over {E} DIV {H} over {G} = {S2} {op2} 1$$/수식$$\n" \
              "㉢ $$수식$${J} over {I} DIV {L} over {K} = {S3} {op3} 1$$/수식$$\n" \
              "따라서 계산 결과가 $$수식$$1$$/수식$$보다 작은 것은 {Q}입니다.\n\n"


    while True:
        op1, op2, op3 = ['&gt;', '&gt;', '&gt;']

        A, B, C, D = random.sample(list(range(2, 10)), 4)
        E, F, G, H = random.sample(list(range(2, 10)), 4)
        I, J = random.sample(list(range(2, 10)), 2)
        K, L = random.sample(list(range(11, 30)), 2)

        count = 0
        if ((B / A) / (D / C)) < 1:
            Q = '㉠'
            op1 = '&lt;'
            count += 1
        if ((F / E) / (H / G)) < 1:
            Q = '㉡'
            op2 = '&lt;'
            count += 1
        if ((J / I) / (L / K)) < 1:
            Q = '㉢'
            op3 = '&lt;'
            count += 1

        if count == 1 and is_coprime(A, B) and is_coprime(C, D) and is_coprime(E, F) and is_coprime(G, H) and is_coprime(I, J) and is_coprime(K, L):
            break

    c1 = get_LCM(A, C)
    a1 = int(c1 / A * B)
    b1 = int(c1 / C * D)
    gcd1 = get_GCD(a1, b1)
    d1 = int(a1 / gcd1)
    e1 = int(b1 / gcd1)
    p1 = int(d1 / e1)
    q1 = d1 % e1
    r1 = e1

    if p1 == 0:
        S1 = '{a} over {c} DIV {b} over {c} = {a} DIV {b} = {d} over {e}'.format(a=a1, b=b1, c=c1, d=d1, e=e1)
    else:
        S1 = '{a} over {c} DIV {b} over {c} = {a} DIV {b} = {d} over {e} = {p} {q} over {r}'.format(a=a1, b=b1, c=c1, d=d1, e=e1, p=p1, q=q1, r=r1)

    c2 = get_LCM(E, G)
    a2 = int(c2 / E * F)
    b2 = int(c2 / G * H)
    gcd2 = get_GCD(a2, b2)
    d2 = int(a2 / gcd2)
    e2 = int(b2 / gcd2)
    p2 = int(d2 / e2)
    q2 = d2 % e2
    r2 = e2

    if p2 == 0:
        S2 = '{a} over {c} DIV {b} over {c} = {a} DIV {b} = {d} over {e}'.format(a=a2, b=b2, c=c2, d=d2, e=e2)
    else:
        S2 = '{a} over {c} DIV {b} over {c} = {a} DIV {b} = {d} over {e} = {p} {q} over {r}'.format(a=a2, b=b2, c=c2, d=d2, e=e2, p=p2, q=q2, r=r2)

    c3 = get_LCM(I, K)
    a3 = int(c3 / I * J)
    b3 = int(c3 / K * L)
    gcd3 = get_GCD(a3, b3)
    d3 = int(a3 / gcd3)
    e3 = int(b3 / gcd3)
    p3 = int(d3 / e3)
    q3 = d3 % e3
    r3 = e3

    if p3 == 0:
        S3 = '{a} over {c} DIV {b} over {c} = {a} DIV {b} = {d} over {e}'.format(a=a3, b=b3, c=c3, d=d3, e=e3)
    else:
        S3 = '{a} over {c} DIV {b} over {c} = {a} DIV {b} = {d} over {e} = {p} {q} over {r}'.format(a=a3, b=b3, c=c3, d=d3, e=e3, p=p3, q=q3, r=r3)



    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L)
    answer = answer.format(Q=Q)
    comment = comment.format(Q=Q, A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, S1=S1, S2=S2, S3=S3, op1=op1, op2=op2, op3=op3)

    return stem, answer, comment































# 6-2-1-23
def fractiondiv621_Stem_020():
    stem = "다음 중 계산 결과가 가장 큰 것은 어느 것인가요?\n① $$수식$${b1} over {a1} DIV {d1} over {c1}$$/수식$$     ② $$수식$${b2} over {a2} DIV {d2} over {c2}$$/수식$$     ③ $$수식$${b3} over {a3} DIV {d3} over {c3}$$/수식$$\n④ $$수식$${b4} over {a4} DIV {d4} over {c4}$$/수식$$     ⑤ $$수식$${b5} over {a5} DIV {d5} over {c5}$$/수식$$\n"
    answer = "(정답)\n{Q}\n"
    comment = "(해설)\n" \
              "① $$수식$${b1} over {a1} DIV {d1} over {c1} = {x1} over {z1} DIV {y1} over {z1} = {x1} DIV {y1} = {gx1} over {gy1} {saying1}$$/수식$$\n" \
              "② $$수식$${b2} over {a2} DIV {d2} over {c2} = {x2} over {z2} DIV {y2} over {z2} = {x2} DIV {y2} = {gx2} over {gy2} {saying2}$$/수식$$\n" \
              "③ $$수식$${b3} over {a3} DIV {d3} over {c3} = {x3} over {z3} DIV {y3} over {z3} = {x3} DIV {y3} = {gx3} over {gy3} {saying3}$$/수식$$\n" \
              "④ $$수식$${b4} over {a4} DIV {d4} over {c4} = {x4} over {z4} DIV {y4} over {z4} = {x4} DIV {y4} = {gx4} over {gy4} {saying4}$$/수식$$\n" \
              "⑤ $$수식$${b5} over {a5} DIV {d5} over {c5} = {x5} over {z5} DIV {y5} over {z5} = {x5} DIV {y5} = {gx5} over {gy5} {saying5}$$/수식$$\n" \
              "계산 결과가 가장 큰 것은 {Q}입니다.\n\n"


    while True:
        a1, b1, c1, d1 = random.sample(list(range(2, 10)), 4)
        a2, b2, c2, d2 = random.sample(list(range(2, 10)), 4)
        a3, b3, c3, d3 = random.sample(list(range(2, 10)), 4)
        a4, b4, c4, d4 = random.sample(list(range(2, 10)), 4)
        a5, b5, c5, d5 = random.sample(list(range(2, 10)), 4)

        c3 = np.random.randint(11, 30)
        a4 = np.random.randint(11, 30)
        c4 = np.random.randint(11, 30)
        a5 = np.random.randint(11, 30)

        a = [a1, a2, a3, a4, a5]
        b = [b1, b2, b3, b4, b5]
        c = [c1, c2, c3, c4, c5]
        d = [d1, d2, d3, d4, d5]

        x = []
        y = []
        z = []
        p = []
        q = []
        r = []
        s = []

        for i in range(0, 5):
            lcm = get_LCM(a[i], c[i])
            x.append(int(lcm / a[i] * b[i]))
            y.append(int(lcm / c[i] * d[i]))
            z.append(lcm)
            gcd = get_GCD(x[i], y[i])
            p.append(int(x[i] / gcd))
            q.append(int(y[i] / gcd))
            r.append(int(p[i] / q[i]))
            s.append(p[i] % q[i])

        x1, x2, x3, x4, x5 = x
        y1, y2, y3, y4, y5 = y
        z1, z2, z3, z4, z5 = z
        q1, q2, q3, q4, q5 = q
        r1, r2, r3, r4, r5 = r
        s1, s2, s3, s4, s5 = s

        gx1, gy1 = giyak(x1, y1)
        gx2, gy2 = giyak(x2, y2)
        gx3, gy3 = giyak(x3, y3)
        gx4, gy4 = giyak(x4, y4)
        gx5, gy5 = giyak(x5, y5)

        if gy1 >= 100 or gy2 >= 100 or gy3 >= 100 or gy4 >= 100 or gy5 >= 100:
            continue

        check_list = [int(x1 / y1), int(x2 / y2), int(x3 / y3), int(x4 / y4), int(x5 / y5)]
        max_check_list = max(check_list)
        if check_list.count(max_check_list) >= 2:
            continue

        if 0 not in s:
            break



    if r1 != 0:
        saying1 = f"= {r1} {s1} over {q1}"
    else:
        saying1 = ""

    if r2 != 0:
        saying2 = f"= {r2} {s2} over {q2}"
    else:
        saying2 = ""

    if r3 != 0:
        saying3 = f"= {r3} {s3} over {q3}"
    else:
        saying3 = ""

    if r4 != 0:
        saying4 = f"= {r4} {s4} over {q4}"
    else:
        saying4 = ""

    if r5 != 0:
        saying5 = f"= {r5} {s5} over {q5}"
    else:
        saying5 = ""

    maxi = 0

    for i in range(1, 5):
        if p[i] / q[i] > p[maxi] / q[maxi]:
            maxi = i

    Q = answer_dict[maxi]


    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, b1=b1, b2=b2, b3=b3, b4=b4, b5=b5, c1=c1, c2=c2, c3=c3, c4=c4,
                       c5=c5, d1=d1, d2=d2, d3=d3, d4=d4, d5=d5)
    answer = answer.format(Q=Q)
    comment = comment.format(Q=Q, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, b1=b1, b2=b2, b3=b3, b4=b4, b5=b5, c1=c1, c2=c2,
                             c3=c3, c4=c4, c5=c5, d1=d1, d2=d2, d3=d3, d4=d4, d5=d5, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5,
                             y1=y1, y2=y2, y3=y3, y4=y4, y5=y5, z1=z1, z2=z2, z3=z3, z4=z4, z5=z5, gx1=gx1, gy1=gy1,
                             gx2=gx2, gy2=gy2, gx3=gx3, gy3=gy3, gx4=gx4, gy4=gy4, gx5=gx5, gy5=gy5, saying1=saying1,
                             saying2=saying2, saying3=saying3, saying4=saying4, saying5=saying5)

    return stem, answer, comment































# 6-2-1-24
def fractiondiv621_Stem_021():
    stem = "큰 수를 작은 수로 나눈 몫을 구해 보세요.\n$$수식$${box_a}$$/수식$$    $$수식$${box_b}$$/수식$$\n"
    answer = "(정답)\n$$수식$${H} ` {I} over {F}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${B} over {A} = {F} over {E}$$/수식$$, $$수식$${D} over {C} = {G} over {E}$$/수식$$이므로 " \
              "$$수식$${F} over {E} {op} {G} over {E}$$/수식$$입니다.\n" \
              "→ $$수식$${M1} over {N1} DIV {M2} over {N2} = {X1} over {E} DIV {X2} over {E} " \
              "= {X1} DIV {X2} = {X1} over {X2} = {H} {I} over {NF}$$/수식$$\n\n"


    while True:
        A, B, C, D = random.sample(list(range(2, 10)), 4)

        E = get_LCM(A, C)
        F = int((E / A) * B)
        G = int((E / C) * D)
        gcd = get_GCD(F, G)

        if B / A > D / C:
            M1, M2 = B, D
            N1, N2 = A, C
            X1, X2 = F, G
            op = '&gt;'
        else:
            M1, M2 = D, B
            N1, N2 = C, A
            X1, X2 = G, F
            op = '&lt;'

        Y1, Y2 = int(X1 / gcd), int(X2 / gcd)
        H = int(Y1 / Y2)
        I = Y1 % Y2
        NF = Y2

        if is_coprime(A, B) and is_coprime(C, D) and B / A != D / C and Y1 % Y2 != 0:
            break

    box_a = "%s over %s" % (B, A)
    box_b = "%s over %s" % (D, C)


    stem = stem.format(box_a=box_a, box_b=box_b)
    answer = answer.format(H=H, I=I, F=F)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, N1=N1, N2=N2, M1=M1, M2=M2, X1=X1, X2=X2, op=op, NF=NF)

    return stem, answer, comment




































# 6-2-1-25
def fractiondiv621_Stem_022():
    stem = "평행사변형의 밑변의 길이는 $$수식$${B} over {A} `` rm m$$/수식$$이고 높이는 $$수식$${D} over {C} `` rm m$$/수식$$입니다. 평행사변형의 밑면의 길이는 높이의 몇 배인가요?\n"
    answer = "(정답)\n$$수식$${F}$$/수식$$배\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$밑변의 길이$$수식$$RIGHT ) `` DIV `` LEFT ($$/수식$$높이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$ = {B} over {A} DIV {D} over {C} = {E} over {C} DIV {D} over {C} = {E} DIV {D} = {F} LEFT ($$/수식$$배$$수식$$RIGHT )$$/수식$$\n\n"


    while True:
        A = np.random.randint(11, 20)
        C = A * np.random.randint(2, 5)
        B, D = random.sample(list(range(2, 10)), 2)
        E = int((C / A) * B)

        if is_coprime(A, B) and is_coprime(C, D) and E % D == 0 and E == (C / A) * B:
            break

    F = int(E / D)


    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(F=F)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F)

    return stem, answer, comment





































# 6-2-1-26
def fractiondiv621_Stem_023():
    stem = "$$수식$${box}$$/수식$$ 안에 들어갈 수 있는 자연수 중에서 가장 작은 수를 구해 보세요.\n$$표$$$$수식$${B} over {A} DIV {D} over {C} &lt; ` {box}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${G}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${B} over {A} DIV {D} over {C} = {B} over {A} DIV {E} over {A} = {B} DIV {E} = {F}$$/수식$$\n" \
              "$$수식$${F} &lt; ` {box}$$/수식$$에서 $$수식$${box}$$/수식$$ 안에 " \
              "들어갈 수 있는 가장 작은 자연수는 $$수식$${G}$$/수식$$입니다.\n\n"



    box = '□'

    while True:
        C, D = random.sample(list(range(2, 10)), 2)
        A, B = random.sample(list(range(11, 100)), 2)
        E = int((A / C) * D)

        if A % C == 0 and B % D == 0 and B % E == 0 and is_coprime(C, D) and E == (A / C) * D:
            break

    F = int(B / E)
    G = F + 1


    stem = stem.format(A=A, B=B, C=C, D=D, box=box)
    answer = answer.format(G=G)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, box=box)

    return stem, answer, comment







































# 6-2-1-27
def fractiondiv621_Stem_024():
    stem = "어느 달팽이는 $$수식$${B} over {A} `` rm {{cm}}$$/수식$$를 기어가는 데 $$수식$${D} over {C}$$/수식$$분이 걸립니다. 이 달팽이가 같은 빠르기로 기어간다면 $$수식$$1$$/수식$$분 동안 갈 수 있는 거리는 몇 $$수식$$rm {{cm}}$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${H} ` {I} over {J} ` rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1$$/수식$$분 동안 갈 수 있는 거리$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ( $$/수식$$기어간 거리$$수식$$RIGHT ) DIV LEFT ($$/수식$$걸린 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {B} over {A} DIV {D} over {C} = {G} over {E} DIV {F} over {E} = {G} DIV {F} " \
              "= {G} over {F} = {H} {I} over {J} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n\n"


    while True:
        A, C = random.sample(list(range(11, 20)), 2)
        B, D = random.sample(list(range(2, 10)), 2)

        E = get_LCM(A, C)
        G = int(E / A * B)
        F = int(E / C * D)
        gcd = get_GCD(G, F)

        g = int(G / gcd)
        f = int(F / gcd)
        H = int(g / f)
        I = g % f
        J = f

        if E < 100 and is_coprime(A, B) and is_coprime(C, D) and g > f and I != 0:
            break


    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(H=H, I=I, J=J)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J)

    return stem, answer, comment




































# 6-2-1-28
def fractiondiv621_Stem_025():
    stem = "$$수식$${box}$$/수식$$ 안에 들어갈 수 있는 자연수는 모두 몇 개인가요?\n$$표$$$$수식$${B} over {A} DIV {D} over {C} &lt; ` {box} `&lt; {F} over {E} DIV {H} over {G}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${P}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${B} over {A} DIV {D} over {C} = {N} over {C} DIV {D} over {C} = {N} DIV {D} = {O}$$/수식$$\n" \
              "$$수식$${F} over {E} DIV {H} over {G} = {J} over {I} DIV {K} over {I} = {J} DIV {K} = {J} over {K} = {L} {M} over {k}$$/수식$$\n" \
              "$$수식$${O} &lt; ` {box} ` &lt; {L} {M} over {k}$$/수식$$이므로 " \
              "$$수식$${box}$$/수식$$ 안에 들어갈 수 있는 자연수는 모두 $$수식$${P}$$/수식$$개입니다.\n\n"



    box = '□'

    while True:
        while True:
            A, B = random.sample(list(range(2, 10)), 2)

            C = A * np.random.randint(2, 6)

            if C <= 10 or C >= 30:
                continue

            E, F = random.sample(list(range(2, 10)), 2)
            D, H = random.sample(list(range(2, 10)), 2)


            G = np.random.randint(11, 20)

            I = get_LCM(E, G)
            J = int(I / E * F)
            K = int(I / G * H)
            gcd = get_GCD(J, K)

            j = int(J / gcd)
            k = int(K / gcd)
            L = int(j / k)
            M = j % k

            N = int((C / A) * B)
            O = int(N / D)

            if N % D == 0 and I < 100 and is_coprime(A, B) and is_coprime(C, D) and is_coprime(E, F) and is_coprime(G, H) and j > k and M != 0:
                break

        P = L - O

        if P > 0:
            break



    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, box=box)
    answer = answer.format(P=P)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, M=M, N=N, O=O, P=P, k=k, box=box)

    return stem, answer, comment

































# 6-2-1-29
def fractiondiv621_Stem_026():
    stem = "같은 모양은 같은 수를 나타낼 때 ▲에 알맞은 대분수를 구해 보세요.\n$$표$$■$$수식$$TIMES {D} over {C} = {B} over {A}$$/수식$$     ■$$수식$$TIMES$$/수식$$▲$$수식$$= {F} over {E}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${M} ` {O} over {P}$$/수식$$\n"
    comment = "(해설)\n" \
              "■$$수식$$= {B} over {A} DIV {D} over {C} = {H} over {G} DIV {I} over {G} " \
              "= {H} DIV {I} = {H} over {I} = {h} over {i}$$/수식$$\n" \
              "■$$수식$$TIMES$$/수식$$▲$$수식$$ = {h} over {i} TIMES$$/수식$$▲$$수식$$= {F} over {E}$$/수식$$\n" \
              "▲$$수식$$= {F} over {E} DIV {h} over {i} = {K} over {J} DIV {L} over {J} " \
              "= {K} DIV {L} = {K} over {L} = {M} {O} over {P}$$/수식$$\n\n"


    while True:
        A, B, C, D = random.sample(list(range(2, 10)), 4)
        E, F = random.sample(list(range(2, 10)), 2)

        G = get_LCM(A, C)
        H = int(G / A * B)
        I = int(G / C * D)

        gcd1 = get_GCD(H, I)
        h = int(H / gcd1)
        i = int(I / gcd1)

        J = get_LCM(E, i)
        K = int(J / E * F)
        L = int(J / i * h)
        gcd2 = get_GCD(K, L)

        k = int(K / gcd2)
        l = int(L / gcd2)
        M = int(k / l)

        O = k % l
        if O == 0:
            continue

        P = l

        if gcd1 > 1 and J < 100 and K < 100 and is_coprime(A, B) and is_coprime(C, D) and is_coprime(E, F) and k > l and P > 1:
            break


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F)
    answer = answer.format(M=M, O=O, P=P)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, M=M, O=O, P=P, h=h, i=i)

    return stem, answer, comment






































# 6-2-1-032
def fractiondiv621_Stem_027():
    stem = "계산 결과를 비교하여 $$수식$${box}$$/수식$$안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${A} DIV {C} over {B} ```` {box} ```` {D} DIV {F} over {E}$$/수식$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A} DIV {C} over {B} = LEFT ( {A} DIV {C} RIGHT ) TIMES {B} = {G} TIMES {B} = {H}$$/수식$$\n" \
              "$$수식$${D} DIV {F} over {E} = LEFT ( {D} DIV {F} RIGHT ) TIMES {E} = {I} TIMES {E} = {J}$$/수식$$\n" \
              "→ $$수식$${H} {S} {J}$$/수식$$\n\n"


    box = '□'

    while True:
        B, C = random.sample(list(range(2, 10)), 2)
        E, F = random.sample(list(range(2, 10)), 2)
        G = np.random.randint(2, 6)
        I = np.random.randint(2, 6)

        A = C * G
        D = F * I
        H = G * B
        J = I * E

        if is_coprime(B, C) and is_coprime(E, F):
            break

    if H > J:
        S = '&gt;'
    elif H < J:
        S = '&lt;'
    else:
        S = '='


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, box=box)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, S=S)

    return stem, answer, comment



































# 6-2-1-033
def fractiondiv621_Stem_028():
    stem = "자연수를 분수로 나눈 몫을 구해 보세요.\n$$표$$$$수식$${A}$$/수식$$     $$수식$${C} over {B}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${E}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A} DIV {C} over {B} = LEFT ( {A} DIV {C} RIGHT ) TIMES {B} = {D} TIMES {B} = {E}$$/수식$$\n\n"


    while True:
        B, C = random.sample(list(range(2, 10)), 2)
        D = np.random.randint(2, 6)
        A = C * D

        if is_coprime(B, C):
            break

    E = B * D


    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(E=E)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E)

    return stem, answer, comment



































# 6-2-1-34
def fractiondiv621_Stem_029():
    stem = "계산 결과가 큰 것부터 차례대로 기호를 써 보세요.\n$$표$$㉠ $$수식$${A} DIV {C} over {B}$$/수식$$     ㉡ $$수식$${D} DIV {F} over {E}$$/수식$$     ㉢ $$수식$${G} DIV {I} over {H}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{S}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${A} DIV {C} over {B} = LEFT ( {A} DIV {C} RIGHT ) TIMES {B} = {J} TIMES {B} = {K}$$/수식$$\n" \
              "㉡ $$수식$${D} DIV {F} over {E} = LEFT ( {D} DIV {F} RIGHT ) TIMES {E} = {L} TIMES {E} = {M}$$/수식$$\n" \
              "㉢ $$수식$${G} DIV {I} over {H} = LEFT ( {G} DIV {I} RIGHT ) TIMES {H} = {N} TIMES {H} = {O}$$/수식$$\n" \
              "$$수식$${x1} &gt; {x2} &gt; {x3}$$/수식$$이므로 계산 결과가 가장 큰 것부터 차례대로 쓰면 {S}입니다.\n\n"


    while True:
        B, C = random.sample(list(range(2, 10)), 2)
        E, F = random.sample(list(range(2, 10)), 2)
        H, I = random.sample(list(range(2, 10)), 2)

        J = np.random.randint(2, 7)
        L = np.random.randint(2, 7)
        N = np.random.randint(2, 7)

        A = C * J
        D = F * L
        G = I * N

        K = J * B
        M = L * E
        O = N * H

        if is_coprime(B, C) and is_coprime(E, F) and is_coprime(H, I) and K != M and K != O and M != O:
            break

    if K > M and K > O:
        if M > O:
            S = '㉠, ㉡, ㉢'
            x1, x2, x3 = K, M, O
        else:
            S = '㉠, ㉢, ㉡'
            x1, x2, x3 = K, O, M
    elif M > K and M > O:
        if K > O:
            S = '㉡, ㉠, ㉢'
            x1, x2, x3 = M, K, O
        else:
            S = '㉡, ㉢, ㉠'
            x1, x2, x3 = M, O, K
    else:
        if K > M:
            S = '㉢, ㉠, ㉡'
            x1, x2, x3 = O, K, M
        else:
            S = '㉢, ㉡, ㉠'
            x1, x2, x3 = O, M, K


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, M=M, N=N, O=O,
                             S=S, x1=x1, x2=x2, x3=x3)

    return stem, answer, comment



































# 6-2-1-35
def fractiondiv621_Stem_030():
    stem = "$$수식$${box}$$/수식$$ 안에 알맞은 기약분수를 구해 보세요.\n$$표$$$$수식$${A} DIV ` {box} ` = LEFT ( {A} DIV {C} RIGHT ) TIMES {B}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${C} over {B}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A} DIV ` {box_frac} ` = LEFT ( {A} DIV {C} RIGHT ) TIMES {B}$$/수식$$\n\n"


    box = '□'

    while True:
        B, C = random.sample(list(range(2, 10)), 2)
        A = C * np.random.randint(2, 7)

        if is_coprime(B, C):
            break

    box_frac = "%s over %s" % (C, B)


    stem = stem.format(box=box, A=A, B=B, C=C)
    answer = answer.format(B=B, C=C)
    comment = comment.format(A=A, B=B, C=C, box_frac=box_frac)

    return stem, answer, comment



































# 6-2-1-36
def fractiondiv621_Stem_031():
    stem = "$$수식$${box}$$/수식$$ 안에 알맞은 수를 구해 보세요.\n$$표$$$$수식$${A} DIV ` {B} over {box} ` = {C}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${E}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A} DIV ` {B} over {box} ` = LEFT ( {A} DIV {B} RIGHT ) TIMES ` {box} ` = {D} TIMES ` {box}$$/수식$$\n" \
              "→ $$수식$${D} TIMES ` {box} ` = {C}$$/수식$$, " \
              "$$수식$${box} ` = {E}$$/수식$$\n\n"


    box = '□'

    while True:
        B = np.random.randint(2, 10)
        D = np.random.randint(2, 52)
        A = D * B
        E = np.random.randint(5, 21)

        C = D * E

        if is_coprime(B, E) and A >= 10 and A < 100:
            break


    stem = stem.format(box=box, A=A, B=B, C=C)
    answer = answer.format(E=E)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, box=box)

    return stem, answer, comment


    # while True:
    #     B, E = random.sample(list(range(2, 10)), 2)
    #     D = np.random.randint(2, 7)
    #     A = B * D
    #     C = int(A / B * E)
    #
    #     if is_coprime(B, E):
    #         break


































# 6-2-1-37
def fractiondiv621_Stem_032():
    stem = "길이가 $$수식$${A} `` rm m$$/수식$$인 철사를 $$수식$${C} over {B} `` rm m$$/수식$$씩 자르려고 합니다. 철사를 모두 몇 도막으로 자를 수 있나요?\n"
    answer = "(정답)\n$$수식$${E}$$/수식$$도막\n"
    comment = "(해설)\n" \
              "$$수식$${A} DIV {C} over {B} = LEFT ( {A} DIV {C} RIGHT ) TIMES {B} = {D} TIMES {B} = {E}$$/수식$$\n" \
              "따라서 철사를 모두 $$수식$${E}$$/수식$$도막으로 자를 수 있습니다.\n\n"


    while True:
        B, C = random.sample(list(range(2, 10)), 2)
        D = np.random.randint(2, 7)
        A = C * D
        E = D * B

        if is_coprime(B, C):
            break


    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(E=E)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E)

    return stem, answer, comment





































# 6-2-1-38
def fractiondiv621_Stem_033():
    stem = "다음에서 ㉮와 ㉯의 차는 얼마인가요?\n$$표$$㉮ $$수식$${A} DIV {C} over {B}$$/수식$$     ㉯ $$수식$${D} DIV {F} over {E}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${K}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉮ $$수식$${A} DIV {C} over {B} = LEFT ( {A} DIV {C} RIGHT ) TIMES {B} = {G} TIMES {B} = {H}$$/수식$$\n" \
              "㉯ $$수식$${D} DIV {F} over {E} = LEFT ( {D} DIV {F} RIGHT ) TIMES {E} = {I} TIMES {E} = {J}$$/수식$$\n" \
              "→ {max_circle}$$수식$$-$$/수식$${min_circle}$$수식$$= {hj_max} - {hj_min} = {K}$$/수식$$\n\n"


    while True:
        B, C = random.sample(list(range(2, 10)), 2)
        E, F = random.sample(list(range(2, 10)), 2)

        G = np.random.randint(2, 7)
        I = np.random.randint(2, 7)
        # N = np.random.randint(2, 7)

        A = C * G
        D = F * I

        H = G * B
        J = I * E

        max_circle = "㉮"
        min_circle = "㉯"

        if J > H:
            max_circle = "㉯"
            min_circle = "㉮"

        # K = H - J
        hj_max = max(H, J)
        hj_min = min(H, J)
        K = max(H, J) - min(H, J)

        if is_coprime(B, C) and is_coprime(E, F) and K > 0:
            break


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F)
    answer = answer.format(K=K)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, hj_max=hj_max, hj_min=hj_min, max_circle=max_circle, min_circle=min_circle)

    return stem, answer, comment







































# 6-2-1-39
def fractiondiv621_Stem_034():
    stem = "어머니께서 $$수식$${A} rm kg$$/수식$$짜리 {G}을 $$수식$${B}$$/수식$$통 사서 이웃 사람들에게 $$수식$${D} over {C} rm kg$$/수식$$씩 나누어 주려고 합니다. 몇 명에게 나누어 줄 수 있나요?\n"
    answer = "(정답)\n$$수식$${F}$$/수식$$명\n"
    comment = "(해설)\n" \
              "$$수식$${A} rm kg$$/수식$$짜리 {G}을 $$수식$${B}$$/수식$$통 샀으므로\n" \
              "$$수식$$LEFT ($$/수식$$전체 {G}의 양$$수식$$RIGHT ) = {A} TIMES {B} = {E} LEFT ( rm kg RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$나누어 줄 수 있는 사람 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$$전체 {G}의 양$$수식$$RIGHT ) DIV LEFT ($$/수식$$한 사람당 나누어 주는 {G}의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {E} DIV {D} over {C} = LEFT ( {E} DIV {D} RIGHT ) TIMES {C} = {F} LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$\n\n"



    G = ["된장", "고추장", "꿀", "소금", "설탕"][np.random.randint(0, 5)]

    while True:
        A = np.random.randint(2, 6)
        B = np.random.randint(2, 6)
        C = np.random.randint(2, 6)
        D = np.random.randint(2, 6)

        E = A * B

        F = int((E / D) * C)

        if is_coprime(C, D) and E % D == 0 and F == (E / D) * C and F >= 15 and F <= 40:
            break


    stem = stem.format(A=A, B=B, C=C, D=D, G=G)
    answer = answer.format(F=F)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G)

    return stem, answer, comment




    # while True:
    #     C, D = random.sample(list(range(2, 10)), 2)
    #     A, B = random.sample(list(range(2, 10)), 2)
    #     E = A * B
    #     F = int((E / D) * C)
    #
    #     if E % D == 0 and is_coprime(C, D):
    #         break































# 6-2-1-40
def fractiondiv621_Stem_035():
    stem = "넓이가 $$수식$${B} over {A} rm m^2$$/수식$$인 삼각형이 있습니다. 이 삼각형의 높이가 $$수식$${D} over {C} rm m$$/수식$$일 때 밑변의 길이는 몇 $$수식$$rm m$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${H} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$밑변의 길이$$수식$$RIGHT ) TIMES {D} over {C} DIV 2 = {B} over {A}$$/수식$$,\n" \
              "$$수식$$LEFT ($$/수식$$밑변의 길이$$수식$$RIGHT ) TIMES {D} over {C} = {B} over {A} TIMES 2 " \
              "= {E} over {A} = {B} over {F}$$/수식$$,\n" \
              "$$수식$$LEFT ($$/수식$$밑변의 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {B} over {F} DIV {D} over {C} {saying1} = {G} DIV {D} = {H} LEFT ( rm m RIGHT )$$/수식$$\n\n"


    while True:
        A = np.random.randint(10, 100)
        C = np.random.randint(10, 100)

        B = np.random.randint(2, 10)
        D = np.random.randint(2, 10)

        E = 2 * B
        F = int(A / 2)

        G = int(B * (C / F))
        H = int(G / D)

        if is_coprime(A, B) and is_coprime(C, D) and A % 2 == 0 and C % 2 == 0 and C % F == 0 and G % D == 0 and is_coprime(F, B):
            break


    if B == G and F == C:
        saying1 = ""
    else:
        saying1 = f"= {G} over {C} DIV {D} over {C}"


    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(H=H)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, saying1=saying1)

    return stem, answer, comment





    # while True:
    #     H = np.random.randint(2, 10)
    #     D = np.random.randint(2, 10)
    #     G = D * H
    #     C = np.random.randint(11, 30)
    #
    #     gcd = get_GCD(G, C)
    #     B = int(G / gcd)
    #     F = int(C / gcd)
    #
    #     A = F * 2
    #     E = B * 2
    #
    #     if is_coprime(A, B) and is_coprime(C, D):
    #         break































# 6-2-1-41
def fractiondiv621_Stem_036():
    stem = "$$수식$${box}$$/수식$$ 안에 들어갈 수 있는 자연수는 모두 몇 개인가요?\n$$표$$$$수식$${A} DIV {C} over {B} ` &lt; ` {D} DIV {E} over {box} ` &lt; ` {F} DIV {H} over {G}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${L}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${A} DIV {C} over {B} = LEFT ( {A} DIV {C} RIGHT ) TIMES {B} = {I}$$/수식$$\n" \
              "$$수식$${D} DIV {E} over {box} = LEFT ( {D} DIV {E} RIGHT ) TIMES {box} = {J} TIMES {box}$$/수식$$\n" \
              "$$수식$${F} DIV {H} over {G} = LEFT ( {F} DIV {H} RIGHT ) TIMES {G} = {K}$$/수식$$\n" \
              "따라서 $$수식$${box}$$/수식$$ 안에 들어갈 수 있는 자연수는 모두 $$수식$${L}$$/수식$$개입니다.\n\n"


    box = '□'

    while True:
        A = random.randint(10, 100)
        D = random.randint(10, 100)
        F = random.randint(10, 100)

        B = random.randint(1, 10)
        C = random.randint(1, 10)
        E = random.randint(1, 10)

        G = random.randint(2, 10)
        H = random.randint(2, 10)


        I = int((A / C) * B)
        if I != (A / C) * B:
            continue

        J = int(D / E)
        if J != D / E:
            continue

        K = int((F / H) * G)
        if K != (F / H) * G:
            continue

        L = math.floor(K / J) - math.ceil(I / J)

        if K % J == 0 and I % J == 0:
            L -= 1
        elif K % J != 0 and I % J != 0:
            L += 1

        if A % C == 0 and D % E == 0 and F % H == 0 and L > 0 and L < 11 and is_coprime(B, C) and is_coprime(G, H):
            break


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, box=box)
    answer = answer.format(L=L)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, box=box)

    return stem, answer, comment




    # A, D, F = random.sample(list(range(11, 50)), 3)
    # B, C, E, G, H = random.sample(list(range(2, 10)), 5)




































# 6-2-1-42
def fractiondiv621_Stem_037():
    stem = "㉠, ㉡에 알맞은 수를 각각 구해 보세요.\n$$표$$$$수식$${B} over {A} DIV {D} over {C} = ` {box1}$$/수식$$\n \n$$수식$${box1} ` DIV {F} over {E} = ` {box2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${H} over {G}$$/수식$$, $$수식$${J} over {I}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$$= {B} over {A} DIV {D} over {C} = {B} over {A} TIMES {C} over {D} = {H} over {G}$$/수식$$\n" \
              "㉡ $$수식$$= {H} over {G} DIV {F} over {E} = {H} over {G} TIMES {E} over {F} = {J} over {I}$$/수식$$\n\n"


    box1 = '㉠'
    box2 = '㉡'


    while True:
        A = np.random.randint(2, 10)
        C = np.random.randint(2, 10)
        E = np.random.randint(2, 10)

        B = np.random.randint(1, 10)
        D = np.random.randint(1, 10)
        F = np.random.randint(1, 10)

        if not is_coprime(A, B) or not is_coprime(C, D) or not is_coprime(E, F) or not is_coprime(B, D) or not is_coprime(A, C):
            continue

        G = A * D
        H = B * C

        if not is_coprime(G, E) or not is_coprime(G, H) or H >= G:
            continue


        I = G * F
        J = E * H

        if not is_coprime(I, J) or J >= I or J >= 100 or I >= 100:
            continue

        break


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, box1=box1, box2=box2)
    answer = answer.format(H=H, G=G, J=J, I=I)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J)

    return stem, answer, comment




    # while True:
    #     A, B, C, D, E, F = random.sample(list(range(2, 10)), 6)
    #
    #     G = A * D
    #     H = B * C
    #     I = G * F
    #     J = H * E
    #
    #     if is_coprime(A, B) and is_coprime(C, D) and is_coprime(E, F) and is_coprime(G, H) and is_coprime(I, J):
    #         break































# 6-2-1-43
def fractiondiv621_Stem_038():
    stem = "㉠, ㉡, ㉢에 알맞은 수들의 합을 구해 보세요.\n$$표$$$$수식$${B} over {A} DIV {D} over {C} = {B} over {{㉠}} TIMES {{㉡}} over {D} = {{㉢}} over {E}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${G}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${B} over {A} DIV {D} over {C} = {B} over {A} TIMES {C} over {D} = {F} over {E}$$/수식$$\n" \
              "→ ㉠$$수식$$= {A}$$/수식$$, ㉡$$수식$$= {C}$$/수식$$, ㉢$$수식$${F}$$/수식$$\n" \
              "따라서 ㉠, ㉡, ㉢에 알맞은 수들의 합은 $$수식$${A} + {C} + {F} = {G}$$/수식$$입니다.\n\n"



    while True:
        A = np.random.randint(2, 10)
        B = np.random.randint(1, 10)
        C = np.random.randint(2, 10)
        D = np.random.randint(1, 10)

        if not is_coprime(A, B) or not is_coprime(C, D) or not is_coprime(B, D) or not is_coprime(A, C):
            continue

        E = A * D
        F = B * C

        if F >= E or not is_coprime(E, F):
            continue

        G = A + C + F

        break


    stem = stem.format(A=A, B=B, C=C, D=D, E=E)
    answer = answer.format(G=G)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G)

    return stem, answer, comment



    # while True:
    #     A, B, C, D = random.sample(list(range(2, 10)), 4)
    #     E = A * D
    #     F = B * C
    #     gcd = get_GCD(E, F)
    #
    #     E = int(E / gcd)
    #     F = int(F / gcd)
    #     G = A + C + F
    #
    #     if is_coprime(A, B) and is_coprime(C, D) and is_coprime(E, F):
    #         break


































# 6-2-1-44
def fractiondiv621_Stem_039():
    stem = "㉠에 알맞은 수를 구해 보세요.\n$$표$$$$수식$${B} over {A} DIV {D} over {C} =$$/수식$$㉠$$/표$$\n"
    answer = "(정답)\n$$수식$${F} over {E}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${B} over {A} DIV {D} over {C} = {B} over {A} TIMES {C} over {D} = {F} over {E}$$/수식$$\n\n"


    while True:
        A = np.random.randint(2, 10)
        B = np.random.randint(1, 10)
        C = np.random.randint(2, 10)
        D = np.random.randint(1, 10)

        if not is_coprime(A, B) or not is_coprime(C, D) or not is_coprime(B, D) or not is_coprime(A, C):
            continue

        E = A * D
        F = B * C

        if not is_coprime(E, F) or F >= E:
            continue

        break


    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(E=E, F=F)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F)

    return stem, answer, comment



    # while True:
    #     A, B, C, D = random.sample(list(range(2, 10)), 4)
    #     E = A * D
    #     F = B * C
    #     gcd = get_GCD(E, F)
    #
    #     E = int(E / gcd)
    #     F = int(F / gcd)
    #
    #     if is_coprime(A, B) and is_coprime(C, D) and is_coprime(E, F):
    #         break
































# 6-2-1-47
def fractiondiv621_Stem_040():
    stem = "계산 결과가 $$수식$$1$$/수식$$보다 작은 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${B} over {A} DIV {D} over {C}$$/수식$$     ㉡ $$수식$${F} over {E} DIV {H} over {G}$$/수식$$     ㉢ $$수식$${J} over {I} DIV {L} over {K}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{S}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${B} over {A} DIV {D} over {C} = {B} over {A} TIMES {C} over {D} = {N} over {M}$$/수식$$\n" \
              "㉡ $$수식$${F} over {E} DIV {H} over {G} = {F} over {E} TIMES {G} over {H} = {P} over {O}$$/수식$$\n" \
              "㉢ $$수식$${J} over {I} DIV {L} over {K} = {J} over {I} TIMES {K} over {L} = {R} over {Q}$$/수식$$\n" \
              "계산 결과가 $$수식$$1$$/수식$$보다 작은 것은 {S}입니다.\n\n"



    ans_choice = np.random.randint(0, 3)

    if ans_choice == 0:
        S = "㉠"

        while True:
            while True:
                A = np.random.randint(2, 10)
                B = np.random.randint(1, 10)
                C = np.random.randint(10, 100)
                D = np.random.randint(1, 10)

                if not is_coprime(A, B) or not is_coprime(C, D) or not is_coprime(C, A) or not is_coprime(B, D):
                    continue

                M = A * D
                N = B * C

                if N >= M:
                    continue

                N, M = giyak(N, M)

                break

            while True:
                E = np.random.randint(2, 10)
                F = np.random.randint(1, 10)
                G = np.random.randint(2, 10)
                H = np.random.randint(1, 10)

                if not is_coprime(E, F) or not is_coprime(G, H) or not is_coprime(F, H) or not is_coprime(E, G):
                    continue

                O = E * H
                P = F * G

                if P <= O:
                    continue

                P, O = giyak(P, O)

                break

            while True:
                I = np.random.randint(2, 10)
                J = np.random.randint(1, 10)
                K = np.random.randint(2, 10)
                L = np.random.randint(1, 10)

                if not is_coprime(I, J) or not is_coprime(K, L) or not is_coprime(J, L) or not is_coprime(K, I):
                    continue

                Q = I * L
                R = J * K

                if R <= Q:
                    continue

                R, Q = giyak(R, Q)

                break

            if A != E and A != I and E != I and B != F and B != J and F != J:
                break

    elif ans_choice == 1:
        S = "㉡"

        while True:
            while True:
                A = np.random.randint(2, 10)
                B = np.random.randint(1, 10)
                C = np.random.randint(10, 100)
                D = np.random.randint(1, 10)

                if not is_coprime(A, B) or not is_coprime(C, D) or not is_coprime(C, A) or not is_coprime(B, D):
                    continue

                M = A * D
                N = B * C

                if N <= M:
                    continue

                N, M = giyak(N, M)

                break

            while True:
                E = np.random.randint(2, 10)
                F = np.random.randint(1, 10)
                G = np.random.randint(2, 10)
                H = np.random.randint(1, 10)

                if not is_coprime(E, F) or not is_coprime(G, H) or not is_coprime(F, H) or not is_coprime(E, G):
                    continue

                O = E * H
                P = F * G

                if P >= O:
                    continue

                P, O = giyak(P, O)

                break

            while True:
                I = np.random.randint(2, 10)
                J = np.random.randint(1, 10)
                K = np.random.randint(2, 10)
                L = np.random.randint(1, 10)

                if not is_coprime(I, J) or not is_coprime(K, L) or not is_coprime(J, L) or not is_coprime(K, I):
                    continue

                Q = I * L
                R = J * K

                if R <= Q:
                    continue

                R, Q = giyak(R, Q)

                break

            if A != E and A != I and E != I and B != F and B != J and F != J:
                break

    elif ans_choice == 2:
        S = "㉢"

        while True:
            while True:
                A = np.random.randint(2, 10)
                B = np.random.randint(1, 10)
                C = np.random.randint(10, 100)
                D = np.random.randint(1, 10)

                if not is_coprime(A, B) or not is_coprime(C, D) or not is_coprime(C, A) or not is_coprime(B, D):
                    continue

                M = A * D
                N = B * C

                if N <= M:
                    continue

                N, M = giyak(N, M)

                break

            while True:
                E = np.random.randint(2, 10)
                F = np.random.randint(1, 10)
                G = np.random.randint(2, 10)
                H = np.random.randint(1, 10)

                if not is_coprime(E, F) or not is_coprime(G, H) or not is_coprime(F, H) or not is_coprime(E, G):
                    continue

                O = E * H
                P = F * G

                if P <= O:
                    continue

                P, O = giyak(P, O)

                break

            while True:
                I = np.random.randint(2, 10)
                J = np.random.randint(1, 10)
                K = np.random.randint(2, 10)
                L = np.random.randint(1, 10)

                if not is_coprime(I, J) or not is_coprime(K, L) or not is_coprime(J, L) or not is_coprime(K, I):
                    continue

                Q = I * L
                R = J * K

                if R >= Q:
                    continue

                R, Q = giyak(R, Q)

                break

            if A != E and A != I and E != I and B != F and B != J and F != J:
                break


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L,
                             M=M, N=N, O=O, P=P, Q=Q, R=R, S=S)

    return stem, answer, comment




    # while True:
    #     A, B, C, D = random.sample(list(range(2, 10)), 4)
    #     E, F, G, H = random.sample(list(range(2, 10)), 4)
    #     I, J, K, L = random.sample(list(range(2, 10)), 4)
    #
    #     N = B * C
    #     M = A * D
    #
    #     P = F * G
    #     O = E * H
    #
    #     R = J * K
    #     Q = I * L
    #
    #     count = 0
    #     if N < M:
    #         count += 1
    #         S = '㉠'
    #     if P < O:
    #         count += 1
    #         S = '㉡'
    #     if R < Q:
    #         count += 1
    #         S = '㉢'
    #
    #     if count == 1 and is_coprime(A, B) and is_coprime(C, D) and is_coprime(E, F) and is_coprime(G, H) and is_coprime(I, J) and is_coprime(
    #             K, L):
    #         break
    #
    #
    # gcd1 = get_GCD(N, M)
    # N = int(N / gcd1)
    # M = int(M / gcd1)
    #
    # gcd2 = get_GCD(P, O)
    # P = int(P / gcd2)
    # O = int(O / gcd2)
    #
    # gcd3 = get_GCD(R, Q)
    # R = int(R / gcd3)
    # Q = int(Q / gcd3)












































# 6-2-1-48
def fractiondiv621_Stem_041():
    stem = "나무 막대 $$수식$${B} over {A} rm m$$/수식$$의 무게가 $$수식$${D} over {C} rm kg$$/수식$$입니다. 나무 막대 $$수식$$1 rm m$$/수식$$의 무게는 몇  $$수식$$rm kg$$/수식$$인지 구해 보세요.\n"
    answer = "(정답)\n$$수식$${F} over {E} ` rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "나무 막대의 무게를 나무 막대의 길이로 나누면 되므로 $$수식$${D} over {C} DIV {B} over {A}$$/수식$${josa} 계산합니다.\n" \
              "따라서 나무 막대 $$수식$$1 rm m$$/수식$$의 무게는\n" \
              "$$수식$${D} over {C} DIV {B} over {A} = {D} over {C} TIMES {A} over {B} = {F} over {E} LEFT ( rm kg RIGHT )$$/수식$$입니다.\n\n"



    while True:
        A = np.random.randint(10, 100)

        B = np.random.randint(1, 10)
        C = np.random.randint(2, 10)
        D = np.random.randint(1, 10)

        F = A * D
        E = B * C

        if is_coprime(A, B) and is_coprime(C, D) and is_coprime(B, D) and is_coprime(E, F) and F < E:
            break

    if B in [2,4,5,9]:
        josa = "를"
    else:
        josa = "을"

    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(F=F, E=E)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, josa=josa)

    return stem, answer, comment




    # while True:
    #     A = np.random.randint(11, 20)
    #     B, C, D = random.sample(list(range(2, 10)), 3)
    #
    #     F = A * D
    #     E = B * C
    #
    #     gcd = get_GCD(E, F)
    #     E = int(E / gcd)
    #     F = int(F / gcd)
    #
    #     if is_coprime(A, B) and is_coprime(C, D):
    #         break






























# 6-2-1-50
def fractiondiv621_Stem_042():
    stem = "연비는 휘발유 $$수식$$1 rm L$$/수식$$로 갈 수 있는 거리입니다. 가 자동차는 휘발유 $$수식$${B} over {A} rm L$$/수식$$로 $$수식$${D} over {C} rm {{km}}$$/수식$$를 갈 수 있고, 나 자동차는 휘발유 $$수식$${F} over {E} rm L$$/수식$$로 $$수식$${H} over {G} rm {{km}}$$/수식$$를 갈 수 있습니다. 가와 나 자동차 중 연비가 더 높은 자동차는 어느 자동차인가요?\n"
    answer = "(정답)\n{Q}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$가 자동차의 연비$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${D} over {C} DIV {B} over {A} = {D} over {C} TIMES {A} over {B} = {J} over {I}$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$나 자동차의 연비$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${H} over {G} DIV {F} over {E} = {H} over {G} TIMES {E} over {F} = {L} over {K}$$/수식$$\n" \
              "$$수식$${J} over {I} {op} {L} over {K}$$/수식$$이므로 연비가 더 높은 자동차는 {Q} 자동차입니다.\n\n"



    while True:
        while True:
            A = np.random.randint(10, 100)
            B = np.random.randint(1, 10)
            C = np.random.randint(2, 10)
            D = np.random.randint(1, 10)

            if not is_coprime(A, B) or not is_coprime(A, C) or not is_coprime(C, D) or not is_coprime(B, D):
                continue

            J = A * D
            I = B * C

            if J >= I:
                continue

            break

        while True:
            E = np.random.randint(10, 100)
            F = np.random.randint(1, 10)
            G = np.random.randint(10, 100)
            H = np.random.randint(1, 10)

            if not is_coprime(E, F) or not is_coprime(G, H) or not is_coprime(G, E) or not is_coprime(H, F):
                continue

            K = F * G
            L = E * H

            if L >= K:
                continue

            break

        if J / I == L / K:
            continue

        if J / I > L / K:
            Q = '가'
            op = '&gt;'
        else:
            Q = '나'
            op = '&lt;'


        J, I = giyak(J, I)
        L, K = giyak(L, K)

        break


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H)
    answer = answer.format(Q=Q)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, Q=Q, op=op)

    return stem, answer, comment



    # while True:
    #     A, E, G = random.sample(list(range(11, 30)), 3)
    #     B, C, D, F, H = random.sample(list(range(2, 10)), 5)
    #
    #     J = D * A
    #     I = B * C
    #     L = H * E
    #     K = G * F
    #
    #     if J / I != L / K and is_coprime(A, B) and is_coprime(C, D) and is_coprime(E, F) and is_coprime(G, H):
    #         break
    #
    # gcd1 = get_GCD(J, I)
    # J = int(J / gcd1)
    # I = int(I / gcd1)
    #
    # gcd2 = get_GCD(L, K)
    # L = int(L / gcd2)
    # K = int(K / gcd2)
    #
    # if J / I > L / K:
    #     Q = '가'
    #     op = '&gt;'
    # else:
    #     Q = '나'
    #     op = '&lt;'




































# 6-2-1-51
def fractiondiv621_Stem_043():
    stem = "$$수식$${B} over {A}$$/수식$${rur1} 어떤 수로 나누었더니 $$수식$${D} over {C}$$/수식$${ga1} 되었습니다. 어떤 수는 얼마인지 구해 보시오.\n"
    answer = "(정답)\n$$수식$${F} over {E}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 $$수식$${box}$$/수식$$라 하면 " \
              "$$수식$${B} over {A} DIV {box} ` = {D} over {C}$$/수식$$입니다.\n" \
              "$$수식$${box} ` = {B} over {A} DIV {D} over {C} " \
              "= {B} over {A} TIMES {C} over {D} = {F} over {E}$$/수식$$\n\n"


    box = '□'

    while True:
        A = np.random.randint(11, 20)
        B, C, D = random.sample(list(range(2, 10)), 3)

        E = A * D
        F = B * C
        gcd = get_GCD(E, F)

        E = int(E / gcd)
        F = int(F / gcd)

        if is_coprime(A, B) and is_coprime(C, D):
            break

    if B == 2 or B == 4 or B == 5 or B == 9:
        rur1 = "를"
    else:
        rur1 = "을"

    if D == 2 or D == 4 or D == 5 or D == 9:
        ga1 = "가"
    else:
        ga1 = "이"


    stem = stem.format(A=A, B=B, C=C, D=D, rur1=rur1, ga1=ga1)
    answer = answer.format(F=F, E=E)
    comment = comment.format(box=box, A=A, B=B, C=C, D=D, E=E, F=F)

    return stem, answer, comment



































# 6-2-1-52
def fractiondiv621_Stem_044():
    stem = "㉠에 알맞은 수를 구해 보세요.\n$$수식$${box1} {box2} {box3}$$/수식$$\n"
    answer = "(정답)\n$$수식$${G} ` {H} over {I}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${B} over {A} DIV {D} over {C} = {B} over {A} TIMES {C} over {D} = {F} over {E} = {G} {H} over {I}$$/수식$$\n\n"


    while True:
        A = np.random.randint(11, 20)
        B, C, D = random.sample(list(range(2, 10)), 3)

        E = A * D
        F = B * C
        gcd = get_GCD(E, F)
        e = int(E / gcd)
        f = int(F / gcd)

        G = int(f / e)
        H = f % e
        I = e

        if G > 0 and H > 0 and is_coprime(A, B) and is_coprime(C, D):
            break


    box1 = "%s over %s" % (B, A)
    box2 = "div %s over %s =" % (D, C)
    box3 = "㉠"


    stem = stem.format(box1=box1, box2=box2, box3=box3)
    answer = answer.format(G=G, H=H, I=I)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I)

    return stem, answer, comment





































# 6-2-1-53
def fractiondiv621_Stem_045():
    stem = "가분수를 진분수로 나눈 몫을 가장 간단한 분수로 나타내어 보세요.\n{x1}$$수식$$``````$$/수식$${x2}$$수식$$``````$$/수식$${x3}\n"
    answer = "(정답)\n$$수식$${J} ` {K} over {H}$$/수식$$\n"
    comment = "(해설)\n" \
              "가분수: $$수식$${G} over {F}$$/수식$$, 진분수: $$수식$${E} over {D}$$/수식$$\n" \
              "→ $$수식$${G} over {F} DIV {E} over {D} = {G} over {F} TIMES {D} over {E} " \
              "= {I} over {H} = {J} {K} over {H}$$/수식$$\n\n"


    while True:
        A, B, C = random.sample(list(range(2, 10)), 3)
        D, E, F = random.sample(list(range(2, 10)), 3)
        G = np.random.randint(11, 20)

        I = G * D
        H = F * E

        gcd = get_GCD(I, H)
        I = int(I / gcd)
        H = int(H / gcd)
        J = int(I / H)

        K = I % H

        if J > 0 and K > 0 and is_coprime(A, C) and is_coprime(D, E) and is_coprime(G, F) and E < D:
            break


    x = ['$$수식$$%s ` %s over %s$$/수식$$' % (B, C, A),
         '$$수식$$%s over %s$$/수식$$' % (E, D),
         '$$수식$$%s over %s$$/수식$$' % (G, F)]

    np.random.shuffle(x)
    x1, x2, x3 = x


    stem = stem.format(x1=x1, x2=x2, x3=x3)
    answer = answer.format(J=J, K=K, H=H)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K)

    return stem, answer, comment




































# 6-2-1-54
def fractiondiv621_Stem_046():
    stem = "계산 결과가 자연수인 것을 찾아 기호를 써 보세요.\n$$수식$${saying1} ```` {saying2}$$/수식$$\n"
    answer = "(정답)\n{X}\n"
    comment = "(해설)\n" \
              "㉠ {y1}\n㉡ {y2}\n따라서 계산 결과가 자연수인 것은 {X}입니다.\n\n"



    while True:
        O = np.random.randint(1, 10)
        M = [2, 4, 6, 8, 9][np.random.randint(0, 5)]

        if not is_coprime(O, M):
            continue

        N = np.random.randint(1, 10)

        L = N * M + O

        S = np.random.randint(1, 10)

        ms_result = M * S
        ms_result_yaksu_list = get_yaksu_list(ms_result)

        while True:
            c_candidate = random.sample(ms_result_yaksu_list, 1)
            C = c_candidate[0]
            if C != 1:
                break

        D = ms_result / C

        if D not in ms_result_yaksu_list or D != int(D):
            continue

        D = int(D)

        ls_result = L * S
        ls_result_yaksu_list = get_yaksu_list(ls_result)

        while True:
            k_candidate = random.sample(ls_result_yaksu_list, 1)
            K = k_candidate[0]
            E = ls_result / K
            if E != 1:
                break

        if E not in ls_result_yaksu_list or E != int(E):
            continue

        E = int(E)

        if K <= C or E <= D or not is_coprime(D, E) or K % C == 0 or E % C == 0:
            continue

        A = K // C

        B = K % C

        break

    while True:
        I = np.random.randint(2, 10)
        J = [2, 4, 6, 8, 9][np.random.randint(0, 5)]

        if not is_coprime(I, J) or J <= I:
            continue

        P = I * (np.random.randint(1, 11))

        while True:
            j_yaksu_list = get_yaksu_list(J)
            h_candidate = random.sample(j_yaksu_list, 1)
            H = h_candidate[0]
            if H != 1:
                break

        if P <= H or not is_coprime(P, H):
            continue

        Q = int(P * (J / H))

        if Q != P * (J / H):
            continue

        F = P // H

        G = P % H

        R = Q / I

        if R == R // 1:
            R = int(R)
            break


    new_L = K * E
    new_M = C * D

    giyak_L, giyak_M = giyak(new_L, new_M)

    new_N = giyak_L // giyak_M
    new_O = giyak_L % giyak_M



    pick = np.random.randint(0, 2)

    x = ['{A} {B} over {C} DIV {D} over {E}'.format(A=A, B=B, C=C, D=D, E=E),
         '{F} {G} over {H} DIV {I} over {J}'.format(F=F, G=G, H=H, I=I, J=J)]

    y = [
        '$$수식$${A} {B} over {C} DIV {D} over {E} = {K} over {C} DIV {D} over {E} = {K} over {C} TIMES {E} over {D} = {giyak_L} over {giyak_M} = {new_N} {new_O} over {giyak_M}$$/수식$$'.format(
            A=A, B=B, C=C, D=D, E=E, K=K, giyak_L=giyak_L, giyak_M=giyak_M, new_N=new_N, new_O=new_O),
        '$$수식$${F} {G} over {H} DIV {I} over {J} = {P} over {H} DIV {I} over {J} = {Q} over {J} times {J} over {I} = {Q} DIV {I} = {R}$$/수식$$'.format(
            F=F, G=G, H=H, I=I, J=J, P=P, Q=Q, R=R)]

    if pick:
        x1, x2 = x
        y1, y2 = y
        X = '㉡'
    else:
        x2, x1 = x
        y2, y1 = y
        X = '㉠'

    saying1 = "㉠%s" % x1
    saying2 = "㉡%s" % x2


    stem = stem.format(saying1=saying1, saying2=saying2)
    answer = answer.format(X=X)
    comment = comment.format(y1=y1, y2=y2, X=X)

    return stem, answer, comment





    # while True:
    #     M = 2 * np.random.randint(1, 5)
    #     N, O = random.sample(list(range(2, 10)), 2)
    #     L = N * M + O
    #
    #     S = np.random.randint(2, 10)
    #
    #     divs1 = getdivisor(M * S)
    #     divs1.remove(1)
    #     divs1.remove(M * S)
    #     if len(divs1) < 2:
    #         continue
    #     C, D = random.sample(divs1, 2)
    #
    #     divs2 = getdivisor(L * S)
    #     divs2.remove(1)
    #     divs2.remove(L * S)
    #     if len(divs2) < 2:
    #         continue
    #     K, E = random.sample(divs2, 2)
    #
    #     A = int(K / C)
    #     B = K % C
    #
    #     ij = random.sample(list(range(2, 10)), 2)
    #     ij.sort()
    #     I, J = ij
    #
    #     P = I * np.random.randint(2, 7)
    #     divs3 = getdivisor(J)
    #     divs3.remove(1)
    #     divs3.remove(J)
    #     if len(divs3) < 1:
    #         continue
    #     H = random.sample(divs3, 1)[0]
    #
    #     Q = int(P * J / H)
    #     F = int(P / H)
    #     G = P % H
    #     R = int(Q / I)
    #
    #     new_L = K * E
    #     new_M = C * D
    #
    #     giyak_L, giyak_M = giyak(new_L, new_M)
    #
    #     new_N = giyak_L // giyak_M
    #     new_O = giyak_L % giyak_M
    #
    #     if P > H and is_coprime(P, H) and is_coprime(O, M) and is_coprime(D, E) and K % C != 0 and E % C != 0 and A > 0 and F > 0:
    #         break
































# 6-2-1-55
def fractiondiv621_Stem_047():
    stem = "㉠과 ㉡에 들어갈 숫자를 순서대로 써넣으세요.\n$$수식$${box_first}$$/수식$$ $$수식$${box_second}$$/수식$$ $$수식$${box1}$$/수식$$\n$$수식$${box1}$$/수식$$ $$수식$${box_third}$$/수식$$ $$수식$${box2}$$/수식$$\n"
    answer = "(정답)\n㉠$$수식$${I}$$/수식$$, ㉡$$수식$${K}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${C} {B} over {A} DIV {E} over {A} = {H} over {A} DIV {E} over {A} = {H} DIV {E} = {I}$$/수식$$\n" \
              "$$수식$${I} DIV {G} over {F} = {J} over {F} DIV {G} over {F} = {J} DIV {G} = {K}$$/수식$$\n\n"



    box1 = 'box{㉠````````````````````}'
    box2 = 'box{㉡````````````````````}'

    while True:
        A, B, C, E = random.sample(list(range(2, 10)), 4)
        F, G = random.sample(list(range(2, 10)), 2)
        H = A * C + B
        I = int(H / E)
        J = F * I
        K = int(J / G)

        if H % E == 0 and J % G == 0 and is_coprime(A, B) and is_coprime(A, E) and is_coprime(F, G):
            break



    box_first = "%s ` %s over %s" % (C, B, A)
    box_second = "`div`%s over %s = " % (E, A)
    box_third = "`div`%s over %s = " % (G, F)


    stem = stem.format(box_first=box_first, box_second=box_second, box_third=box_third, box1=box1, box2=box2)
    answer = answer.format(I=I, K=K)
    comment = comment.format(A=A, B=B, C=C, E=E, F=F, G=G, H=H, I=I, J=J, K=K)

    return stem, answer, comment



































# 6-2-1-56
def fractiondiv621_Stem_048():
    stem = "계산 결과를 비교하여 $$수식$${box}$$/수식$$안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${C} {B} over {A} DIV {F} {E} over {D} ```` {box} ```` {H} {I} over {G} DIV {K} {L} over {J}$$/수식$$\n"
    answer = "(정답)\n$$수식$${Y}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${C} {B} over {A} DIV {F} {E} over {D} = {M} over {A} DIV {N} over {D} = {M} over {A} TIMES {D} over {N} = {P} over {O} = {Q} {R} over {O}$$/수식$$,\n" \
              "$$수식$${H} {I} over {G} DIV {K} {L} over {J} = {S} over {G} DIV {T} over {J} = {S} over {G} TIMES {J} over {T} = {V} over {U} = {W} {X} over {U}$$/수식$$\n" \
              "→ $$수식$${Q} {R} over {O} {Y} {W} {X} over {U}$$/수식$$\n\n"


    box = '□'


    while True:
        while True:
            while True:
                A = np.random.randint(2, 10)
                B = np.random.randint(1, 10)
                if is_coprime(A, B):
                    break

            while True:
                D = np.random.randint(2, 10)
                E = np.random.randint(1, 10)
                if is_coprime(D, E):
                    break

            C = np.random.randint(1, 10)
            F = np.random.randint(1, 10)

            M = (A * C) + B
            N = (F * D) + E
            O = A * N
            P = D * M

            P, O = giyak(P, O)

            Q = P // O

            if Q < 1:
                continue

            R = P % O
            if O<10 and C!=F and Q!=0:
                break

        while True:
            while True:
                G = np.random.randint(2, 10)
                I = np.random.randint(1, 10)
                if is_coprime(G, I):
                    break

            while True:
                J = np.random.randint(2, 10)
                L = np.random.randint(1, 10)
                if is_coprime(J, L):
                    break

            H = np.random.randint(1, 10)
            K = np.random.randint(1, 10)

            S = (H * G) + I
            T = (K * J) + L
            U = G * T
            V = S * J

            V, U = giyak(V, U)

            W = V // U

            if W < 1:
                continue

            X = V % U
            if U<20 and S/G!=T/J and W!=0:
                break


        if P / O > V / U:
            Y = "&gt;"
            break

        elif P / O < V / U:
            Y = "&lt;"
            break

        elif P / O == V / U:
            Y = "="
            break

        else:
            continue



    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, box=box)
    answer = answer.format(Y=Y)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, M=M, N=N, O=O, P=P, Q=Q, R=R, S=S, T=T, U=U, V=V, W=W, X=X, Y=Y)

    return stem, answer, comment







    # stem = "계산 결과를 비교하여 $$수식$${box}$$/수식$$안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${C} {B} over {A} DIV {F} {E} over {D} ```` {box} ```` {I} {H} over {G} DIV {L} {K} over {J}$$/수식$$\n"
    # answer = "(정답)\n$$수식$${op}$$/수식$$\n"
    # comment = "(해설)\n" \
    #           "$$수식$${C} {B} over {A} DIV {F} {E} over {D} = {X1} over {A} DIV {Y1} over {D} " \
    #           "= {X1} over {A} TIMES {D} over {Y1} = {Q1} over {P1} = {R1} {S1} over {P1}$$/수식$$,\n" \
    #           "$$수식$${I} {H} over {G} DIV {L} {K} over {J} = {X2} over {G} DIV {Y1} over {J} " \
    #           "= {X2} over {G} TIMES {J} over {Y2} = {Q2} over {P2} = {R2} {S2} over {P2}$$/수식$$\n" \
    #           "→ $$수식$${R1} {S1} over {P1} {op} {R2} {S2} over {P2}$$/수식$$\n\n"

    # box = '□'

    # while True:
    #     A, B, C = random.sample(list(range(2, 10)), 3)
    #     D, E, F = random.sample(list(range(2, 10)), 3)
    #     G, H, I = random.sample(list(range(2, 10)), 3)
    #     J, K, L = random.sample(list(range(2, 10)), 3)
    #
    #     X1 = C * A + B
    #     Y1 = F * D + E
    #     P1 = A * Y1
    #     Q1 = X1 * D
    #
    #     gcd1 = get_GCD(P1, Q1)
    #     P1 = int(P1 / gcd1)
    #     Q1 = int(Q1 / gcd1)
    #     R1 = int(Q1 / P1)
    #     S1 = Q1 % P1
    #
    #     X2 = I * G + H
    #     Y2 = L * J + K
    #     P2 = G * Y2
    #     Q2 = X2 * J
    #
    #     gcd2 = get_GCD(P2, Q2)
    #     P2 = int(P2 / gcd2)
    #     Q2 = int(Q2 / gcd2)
    #     R2 = int(Q2 / P2)
    #     S2 = Q2 % P2
    #
    #     if P1 < 150 and P2 < 150 and R1 > 0 and S1 > 0 and R2 > 0 and S2 > 0 and is_coprime(A, B) and is_coprime(D, E) and is_coprime(G, H) and is_coprime(J, K):
    #         break
    #
    #
    # if Q1 / P1 > Q2 / P2:
    #     op = '&gt;'
    # elif Q1 / P1 < Q2 / P2:
    #     op = '&lt;'
    # else:
    #     op = '='
    #
    # stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, box=box)
    # answer = answer.format(op=op)
    # comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, op=op,
    #                          X1=X1, X2=X2, Y1=Y1, Y2=Y2, P1=P1, P2=P2, Q1=Q1, Q2=Q2, R1=R1, R2=R2, S1=S1, S2=S2)




























# 6-2-1-57
def fractiondiv621_Stem_049():
    stem = "계산 결과가 큰 것부터 차례대로 기호를 써 보세요.\n$$표$$㉠ $$수식$${A} DIV {C} over {B}$$/수식$$     ㉡ $$수식$${E} {F} over {D} DIV {H} over {G}$$/수식$$     ㉢ $$수식$${J} over {I} DIV {L} over {I}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${A} DIV {C} over {B} = LEFT ( {A} DIV {C} RIGHT ) TIMES {B} = {M} TIMES {B} = {N}$$/수식$$\n" \
              "㉡ $$수식$${E} {F} over {D} DIV {H} over {G} = {O} over {D} DIV {H} over {G} = {O} over {D} TIMES {G} over {H} = {Q} over {P}$$/수식$$\n" \
              "㉢ $$수식$${J} over {I} DIV {L} over {I} = {J} DIV {L} = {R}$$/수식$$\n" \
              "$$수식$${x1} &gt; {x2} &gt; {x3}$$/수식$$이므로 계산 결과가 가장 큰 것부터 차례대로 쓰면 {ans}입니다.\n\n"




    while True:
        while True:
            B = np.random.randint(2, 10)
            C = np.random.randint(1, 10)

            M = np.random.randint(1, 10)

            A = M * C

            N = B * M

            if is_coprime(B, C) and A < 10:
                break

        while True:
            D = np.random.randint(2, 10)
            E = np.random.randint(1, 10)
            F = np.random.randint(1, 10)

            O = (D * E) + F

            if is_coprime(D, F):
                break

        while True:
            G = np.random.randint(2, 10)
            H = np.random.randint(1, 10)

            if is_coprime(G, H):
                break

        P = D * H

        Q = O * G

        Q, P = giyak(Q, P)

        while True:
            L = np.random.randint(1, 10)
            I = np.random.randint(11, 30)
            R = np.random.randint(11, 31)
            J = R * L

            if is_coprime(I, L) and is_coprime(I, J) and J > 10 and J < 30:
                break

        if N != Q / P and N != R and Q / P != R:
            break

    result_list = [N, Q / P, R]
    result_list.sort()
    [min, mid, max] = result_list

    if min == N:
        x3 = "%s" % N
        ans3 = "㉠"
    elif mid == N:
        x2 = "%s" % N
        ans2 = "㉠"
    elif max == N:
        x1 = "%s" % N
        ans1 = "㉠"

    if min == Q / P:
        x3 = "%s over %s" % (Q, P)
        ans3 = "㉡"
    elif mid == Q / P:
        x2 = "%s over %s" % (Q, P)
        ans2 = "㉡"
    elif max == Q / P:
        x1 = "%s over %s" % (Q, P)
        ans1 = "㉡"

    if min == R:
        x3 = "%s" % R
        ans3 = "㉢"
    elif mid == R:
        x2 = "%s" % R
        ans2 = "㉢"
    elif max == R:
        x1 = "%s" % R
        ans1 = "㉢"

    ans = ans1 + ", " + ans2 + ", " + ans3



    stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, L=L)
    answer = answer.format(ans=ans)
    comment = comment.format(A=A, B=B, C=C, M=M, N=N, E=E, D=D, F=F, G=G, H=H, O=O, P=P, Q=Q, I=I, J=J, L=L, R=R, x1=x1, x2=x2, x3=x3, ans=ans)

    return stem, answer, comment




    # stem = "계산 결과가 큰 것부터 차례대로 기호를 써 보세요.\n$$표$$㉠ $$수식$${A} DIV {C} over {B}$$/수식$$     ㉡ $$수식$${D} {F} over {E} DIV {H} over {G}$$/수식$$     ㉢ $$수식$${J} over {I} DIV {L} over {K}$$/수식$$$$/표$$\n"
    # answer = "(정답)\n{Y}\n"
    # comment = "(해설)\n" \
    #           "㉠ $$수식$${A} DIV {C} over {B} = LEFT ( {A} DIV {C} RIGHT ) TIMES {B} = {M} TIMES {B} = {N}$$/수식$$\n" \
    #           "㉡ $$수식$${D} {F} over {E} DIV {H} over {G} = {O} over {E} DIV {H} over {G} " \
    #           "= {O} over {E} TIMES {G} over {H} = {Q} over {P} = {R} {S} over {P}$$/수식$$\n" \
    #           "㉢ $$수식$${J} over {I} DIV {L} over {K} = {J} DIV {L} = {T}$$/수식$$\n" \
    #           "$$수식$${x1} &gt; {x2} &gt; {x3}$$/수식$$이므로 계산 결과가 가장 큰 것부터 차례대로 쓰면 {Y}입니다.\n\n"

    # while True:
    #     B, C = random.sample(list(range(2, 10)), 2)
    #     M = np.random.randint(2, 5)
    #     A = C * M
    #     N = M * B
    #
    #     I = np.random.randint(11, 20)
    #     K = I
    #     L = np.random.randint(2, 10)
    #     T = np.random.randint(2, 10)
    #     J = L * T
    #
    #     D, E, F, G, H = random.sample(list(range(2, 10)), 5)
    #     O = D * E + F
    #     P = E * H
    #     Q = O * G
    #     gcd = get_GCD(P, Q)
    #     P = int(P / gcd)
    #     Q = int(Q / gcd)
    #     R = int(Q / P)
    #     S = Q % P
    #
    #     y = [N, Q / P, T]
    #
    #     if R > 0 and S > 0 and is_coprime(B, C) and is_coprime(E, F) and is_coprime(G, H) and is_coprime(J, I) and is_coprime(K, L) and y[0] != y[1] and y[0] != y[2] and y[1] != y[2]:
    #         break
    #
    #
    # x = ['{N}'.format(N=N), '{R} {S} over {P}'.format(P=P, S=S, R=R), '{T}'.format(T=T)]
    #
    # if y[0] > y[1] and y[0] > y[2]:
    #     if y[1] > y[2]:
    #         Y = '㉠, ㉡, ㉢'
    #         x1, x2, x3 = x[0], x[1], x[2]
    #     else:
    #         Y = '㉠, ㉢, ㉡'
    #         x1, x2, x3 = x[0], x[2], x[1]
    # elif y[1] > y[0] and y[1] > y[2]:
    #     if y[0] > y[2]:
    #         Y = '㉡, ㉠, ㉢'
    #         x1, x2, x3 = x[1], x[0], x[2]
    #     else:
    #         Y = '㉡, ㉢, ㉠'
    #         x1, x2, x3 = x[1], x[2], x[0]
    # else:
    #     if y[0] > y[1]:
    #         Y = '㉢, ㉠, ㉡'
    #         x1, x2, x3 = x[2], x[0], x[1]
    #     else:
    #         Y = '㉢, ㉡, ㉠'
    #         x1, x2, x3 = x[2], x[1], x[0]


    # stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L)
    # answer = answer.format(Y=Y)
    # comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, M=M, N=N,
    #                          O=O, P=P, Q=Q, R=R, S=S, T=T, x1=x1, x2=x2, x3=x3, Y=Y)


























# 6-2-1-58
def fractiondiv621_Stem_050():
    stem = "길이가 $$수식$${C} {B} over {A} rm {{cm}}$$/수식$$인 양초에 불을 붙이고 $$수식$${E} {D} over {C}$$/수식$$시간이 지난 후 불을 끄고 남은 양초의 길이를 재었더니 $$수식$${H} {G} over {F} rm {{cm}}$$/수식$$가 되었습니다. 이 양초는 $$수식$$1$$/수식$$시간동안 몇 $$수식$$rm {{cm}}$$/수식$$씩 탄 셈인가요?\n"
    answer = "(정답)\n$$수식$${Q} ` {P} over {N} ` rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${E} {D} over {C}$$/수식$$시간 동안 탄 양초의 길이는\n" \
              "$$수식$${C} {B} over {A} - {H} {G} over {F} = {K} {J} over {I} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n" \
              "따라서 $$수식$$1$$/수식$$시간동안 탄 양초의 길이는\n" \
              "$$수식$${K} {J} over {I} DIV {E} {D} over {C} = {L} over {I} DIV {M} over {C} " \
              "= {L} over {I} TIMES {C} over {M} = {O} over {N} = {Q} {P} over {N} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n\n"




    while True:
        while True:
            A = np.random.randint(2, 10)
            B = np.random.randint(1, 10)

            F = A * np.random.randint(1, 51)

            I = get_LCM(A, F)

            G = np.random.randint(1, 10)

            if is_coprime(A, B) and is_coprime(G, F) and 10 <= F and F <= 20 and I<=20:
                break


        while True:
            C = np.random.randint(2, 5)
            D = np.random.randint(1, 10)

            H = np.random.randint(1, 10)

            if is_coprime(C, D) and C > H:
                break


        E = np.random.randint(1, 5)

        K = C - H

        J = int((B * (I / A)) - (G * (I / F)))

        if J <= 0 or J != (B * (I / A)) - (G * (I / F)) or not is_coprime(J, I) or J >= I:
            continue

        L = (K * I) + J

        O = C * L

        M = (E * C) + D

        N = M * I

        O, N = giyak(O, N)

        if N >= 100 or O <= N:
            continue

        Q = O // N

        P = O % N

        if is_coprime(P, N) and O<40:
            break


    stem = stem.format(C=C, A=A, B=B, E=E, D=D, H=H, F=F, G=G)
    answer = answer.format(Q=Q, P=P, N=N)
    comment = comment.format(E=E, C=C, D=D, A=A, B=B, H=H, F=F, G=G, K=K, I=I, J=J, L=L, M=M, N=N, O=O, Q=Q, P=P)

    return stem, answer, comment





    # stem = "길이가 $$수식$${C} {B} over {A} rm {{cm}}$$/수식$$인 양초에 불을 붙이고 $$수식$${F} {E} over {D}$$/수식$$시간이 지난 후 불을 끄고 남은 양초의 길이를 재었더니 $$수식$${I} {H} over {G} rm {{cm}}$$/수식$$가 되었습니다. 이 양초는 $$수식$$1$$/수식$$시간에 몇 $$수식$$rm {{cm}}$$/수식$$씩 탄 셈인가요?\n"
    # answer = "(정답)\n$$수식$${Q} ` {R} over {O} ` rm {{cm}}$$/수식$$\n"
    # comment = "(해설)\n" \
    #           "$$수식$${F} {E} over {D}$$/수식$$시간 동안 탄 양초의 길이는\n" \
    #           "$$수식$${C} {B} over {A} - {I} {H} over {G} = {L} {K} over {J} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n" \
    #           "따라서 $$수식$$1$$/수식$$시간에 탄 양초의 길이는\n" \
    #           "$$수식$${L} {K} over {J} DIV {F} {E} over {D} = {M} over {J} DIV {N} over {D} " \
    #           "= {M} over {J} TIMES {D} over {N} = {P} over {O} = {Q} {R} over {O} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n\n"

    # while True:
    #     D, E, F = random.sample(list(range(2, 10)), 3)
    #     H, I = random.sample(list(range(2, 10)), 2)
    #     G = np.random.randint(11, 20)
    #
    #     J = G
    #     L, K = random.sample(list(range(2, 10)), 2)
    #
    #     tempB = I * G + H + L * J + K
    #     A = G
    #     gcd1 = get_GCD(A, tempB)
    #
    #     A = int(A / gcd1)
    #     tempB = int(tempB / gcd1)
    #
    #     C = int(tempB / A)
    #     B = tempB % A
    #
    #     M = L * J + K
    #     N = F * D + E
    #
    #     O = J * N
    #     P = M * D
    #     gcd2 = get_GCD(O, P)
    #
    #     O = int(O / gcd2)
    #     P = int(P / gcd2)
    #     Q = int(P / O)
    #     R = P % O
    #
    #     if O < 150 and B > 0 and Q > 0 and R > 0 and is_coprime(A, B) and is_coprime(D, E) and is_coprime(G, H) and is_coprime(K, J):
    #         break


    # stem = stem.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I)
    # answer = answer.format(Q=Q, R=R, O=O)
    # comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, M=M, N=N, O=O, P=P, Q=Q, R=R)




















# 6-2-1-59
def fractiondiv621_Stem_051():
    stem = "$$수식$${box}$$/수식$$ 안에 알맞은 수를 구해 보세요.\n$$표$$$$수식$${box} ` TIMES {B} over {A} = {D} over {C} DIV {F} over {E}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${L} ` {K} over {I}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${D} over {C} DIV {F} over {E} = {D} over {C} TIMES {E} over {F} = {H} over {G}$$/수식$$이므로 " \
              "$$수식$${box} ` TIMES {B} over {A} = {H} over {G}$$/수식$$입니다.\n" \
              "→ $$수식$${box} ` = {H} over {G} DIV {B} over {A} = {H} over {G} TIMES {A} over {B} " \
              "= {J} over {I} = {L} {K} over {I}$$/수식$$\n\n"



    box = '□'

    while True:
        A, B, C, E, F = random.sample(list(range(2, 10)), 5)
        D = np.random.randint(11, 20)

        gcd1 = get_GCD(C * F, D * E)
        G = int(C * F / gcd1)
        H = int(D * E / gcd1)

        gcd2 = get_GCD(G * B, H * A)
        I = int(B * G / gcd2)
        J = int(H * A / gcd2)
        L = int(J / I)
        K = J % I

        if D % F != 0 and L > 0 and K > 0 and is_coprime(A, B) and is_coprime(C, D) and is_coprime(E, F):
            break


    stem = stem.format(box=box, A=A, B=B, C=C, D=D, E=E, F=F)
    answer = answer.format(L=L, K=K, I=I)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, J=J, K=K, L=L, box=box)

    return stem, answer, comment



































# 6-2-1-61
def fractiondiv621_Stem_052():
    stem = "$$수식$${A} {C} over {B}$$/수식$$을 ■로 나누어야 할 것을 잘못하여 $$수식$${C} over {B}$$/수식$$을 ■로 나누었더니 $$수식$${D} over {E}$$/수식$$가 되었습니다. 바르게 계산한 값을 구하시오.\n"
    answer = "(정답)\n$$수식$${X}$$/수식$$\n"
    comment = "(해설)\n" \
              "잘못 계산한 식을 세우면\n" \
              "$$수식$${C} over {B} DIV$$/수식$$■$$수식$$= {D} over {E}$$/수식$$ " \
              "→ ■$$수식$$= {C} over {B} DIV {D} over {E} = {C} over {B} TIMES {E} over {D} = {P} over {Q}$$/수식$$\n" \
              "따라서 바르게 계산하면\n" \
              "$$수식$${A} {C} over {B} DIV$$/수식$$■$$수식$$= {A} {C} over {B} DIV {P} over {Q} " \
              "= {F} over {B} DIV {P} over {Q} = {new_F} over {new_B} TIMES {new_Q} over {new_P} = {X}$$/수식$$\n\n"


    while True:
        A, B, C = random.sample(list(range(2, 10)), 3)
        D, E = random.sample(list(range(2, 10)), 2)
        F = A * B + C

        P = C * E
        Q = B * D
        gcd1 = get_GCD(P, Q)
        P = int(P / gcd1)
        Q = int(Q / gcd1)

        X = int((F * Q) / (B * P))

        if (F * Q) % (B * P) == 0 and is_coprime(Q, P) and is_coprime(B, C) and is_coprime(D, E) and X<50:
            break

    yak_F = int(F / P)
    yak_Q = int(Q / B)

    '''
    new_F = "{pile{` _{%s} `#not%s}" % (yak_F, F)
    new_B = "{pile{not%s#`^{1} `}}" % B
    new_Q = "{pile{` _{%s} `#not%s}" % (yak_Q, Q)
    new_P = "{pile{not%s#`^{1} `}}" % P
    '''

    new_F = "{%s}" % (yak_F)
    new_B = "{1}"
    new_Q = "{%s}" % (yak_Q)
    new_P = "{1}"  

    stem = stem.format(A=A, B=B, C=C, D=D, E=E)
    answer = answer.format(X=X)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, P=P, Q=Q, X=X, new_F=new_F, new_B=new_B, new_Q=new_Q, new_P=new_P)

    return stem, answer, comment



































# 6-2-1-62
def fractiondiv621_Stem_053():
    stem = "나무에서 $$수식$${B} over {A} rm L$$/수식$$의 수액을 채취하는 데 $$수식$${C}$$/수식$$분이 걸립니다. 같은 나무의 수액을 $$수식$${D} rm L$$/수식$$ 채취하는 데 걸리는 시간은 몇 시간 몇 분인가요?\n" \
        "{boxblank} 시간 {boxblank} 분"
    answer = "(정답)\n$$수식$${H}$$/수식$$, $$수식$${I}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${C}$$/수식$$분$$수식$$= {C} over 60$$/수식$$시간$$수식$$= {K} over {L}$$/수식$$시간\n" \
              "$$수식$$LEFT ( {D} rm L$$/수식$$를 채취하는 데 걸리는 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {K} over {L} DIV {B} over {A} TIMES {D} = {K} over {L} TIMES {A} over {B} TIMES {D} " \
              "= {E} over {F} = {H} {G} over {F} LEFT ($$/수식$$시간$$수식$$RIGHT )$$/수식$$\n" \
              "→ $$수식$${H} {G} over {F} = {H} {I} over 60$$/수식$$이므로 $$수식$${H}$$/수식$$시간 $$수식$${I}$$/수식$$분입니다.\n\n"

    boxblank = "$$수식$$BOX{　　}$$/수식$$"
    
    while True:
        while True:
            C = 10 * np.random.randint(2, 6)
            gcdC = get_GCD(C, 60)
            K = int(C / gcdC)
            L = int(60 / gcdC)

            D = np.random.randint(2, 10)

            divisors = getdivisor(60)
            divisors.remove(1)
            divisors.remove(60)
            S = random.sample(divisors, 1)[0]
            if S > L:
                break

        B = int(S / L)
        A = np.random.randint(B + 1, B + 15)

        t1 = K * A * D
        t2 = L * B
        gcd = get_GCD(t1, t2)

        E = int(t1 / gcd)
        F = int(t2 / gcd)

        H = int(E // F)
        G = E % F

        I = int(G * 60 / F)

        if H > 0 and G > 0 and I > 0 and is_coprime(A, B):
            break


    stem = stem.format(A=A, B=B, C=C, D=D, boxblank=boxblank)
    answer = answer.format(H=H, I=I)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, K=K, L=L)

    return stem, answer, comment













def ImgPath(pathcheck,shape,ranNum):
    if pathcheck==0:
        temps = "Element/Grade1_1/Normal"
    else:
        temps = "Element/Grade1_1/Applications"
    tempimg_list = ["/shape/shape","/box/box","/cynlinder/cynlinder"]
    want = tempimg_list[shape]
    want = temps+want+str(ranNum).zfill(2)
    return want

def geometry_ft_0(right_cnt,view_cnt,right_shape): #right_cnt : 정답 갯수, view_cnt : 보기 갯수, right_shape : 정답 모양
    if right_cnt > view_cnt: 
        print("정답 갯수보다 보기 갯수를 더 많이 입력하셔야 합니다.")
    else: 
        choose_img_list = [] 
        right_img = [] 
        temp_choose = random.sample(range(1, 22), right_cnt)        
        for i in range(0,right_cnt):
            choose_img_list += [[right_shape,str(temp_choose[i]).zfill(2)] ]
            right_img += [[right_shape,str(temp_choose[i]).zfill(2)] ]
        temp_choose = random.sample(range(1, 22), view_cnt - right_cnt)
        shape_list = [0,1,2]
        shape_list.remove(right_shape)
        for i in range(0,view_cnt - right_cnt):           
            int_shape = shape_list[random.sample(range(0, 2), 1)[0]]
            choose_img_list += [[int_shape,str(temp_choose[i]).zfill(2)] ]
        random.shuffle(choose_img_list)            
        return right_img,choose_img_list


def fractiondiv621_Stem_054():
    right_cnt =1
    view_cnt = 5
    right_shape = np.random.randint(0, 2)

    comment = "(해설) 생략"
    answer = "(정답) "     
    if right_cnt > 1:
        stem = "알맞은 모양을 모두 찾아 선택하세요.\n "
    else: 
        stem = "알맞은 모양을 찾아 선택하세요.\n "
    stem +="$$표$$"        
    want = geometry_ft_0(right_cnt,view_cnt,right_shape)
    for i in range(0,len(want[0])) :
        answer += "$$이미지$$"+ImgPath(0, want[0][i][0], want[0][i][1]) +"$$/이미지$$   "
        stem += "$$이미지$$"+ImgPath(0, want[0][i][0], want[0][i][1]) +"$$/이미지$$   "
    stem +="$$/표$$"                
    stem +="\n   "
    for i in range(0,len(want[1])) :
        stem += answer_dict[i] +" $$이미지$$"+ImgPath(1, want[1][i][0], want[1][i][1]) +"$$/이미지$$ \n"        
    return stem,answer, comment

"""
    want = geometry_ft_0(right_cnt,view_cnt,right_shape)
    for i in range(0,len(want[0])) :
        answer += "$$이미지$$"+ImgPath(0, want[0][i][0], want[0][i][1]) +"$$/이미지$$   "
        stem += "$$이미지$$"+ImgPath(0, want[0][i][0], want[0][i][1]) +"$$/이미지$$   "
    stem +="\n  \n  "
    for i in range(0,len(want[1])) :
        stem += answer_dict[i] +" $$이미지$$"+ImgPath(1, want[1][i][0], want[1][i][1]) +"$$/이미지$$ \n"        
    return stem,answer, comment
"""




def fractiondiv621_Stem_055():
    right_cnt =2
    view_cnt = 5
    right_shape = np.random.randint(0, 2)

    comment = "(해설) 생략"
    answer = "(정답) "     
    if right_cnt > 1:
        stem = "알맞은 모양을 모두 찾아 선택하세요.\n "
    else: 
        stem = "알맞은 모양을 찾아 선택하세요.\n "
    stem +="$$표$$"        
    want = geometry_ft_0(right_cnt,view_cnt,right_shape)
    for i in range(0,len(want[0])) :
        answer += "$$이미지$$"+ImgPath(0, want[0][i][0], want[0][i][1]) +"$$/이미지$$   "
        stem += "$$이미지$$"+ImgPath(0, want[0][i][0], want[0][i][1]) +"$$/이미지$$   "
    stem +="$$/표$$"   
    stem +="\n "
    for i in range(0,len(want[1])) :
        stem += answer_dict[i] +" $$이미지$$"+ImgPath(1, want[1][i][0], want[1][i][1]) +"$$/이미지$$ \n"        
    return stem,answer, comment












