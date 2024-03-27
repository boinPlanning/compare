import random
import numpy as np
import math


















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
    if b == "로" or b == "으로":
        if (str(a))[-1] == "0" or (str(a))[-1] == "3" or (str(a))[-1] == "6":
            return "으로"
        else:
            return "로"











def soro_so(a, b):
    while True:
        rest_ab = max(a, b) % min(a, b)
        a = min(a, b)
        b = rest_ab
        if rest_ab == 0 or rest_ab == 1:
            break
    return rest_ab
























# 3-2-4-02
def fraction324_Stem_001():
    stem = "{S} $$수식$${A}$$/수식$$개를 똑같이 나눌 수 있는 방법을 잘못 말한 학생은 누구인가요?\n$$표$$ {A1} : $$수식$${a1}$$/수식$$개씩 나눌 수 있습니다.\n{A2} : $$수식$${a2}$$/수식$$개씩 나눌 수 있습니다.\n{A3} : $$수식$${a3}$$/수식$$개씩 나눌 수 있습니다. $$/표$$\n"
    answer = "(정답)\n$$수식$${P3}$$/수식$$\n"
    comment = "(해설)\n" \
              "{S} $$수식$${A}$$/수식$$개는 {B} 똑같이 나눌 수 있습니다.\n" \
              "{S} $$수식$${A}$$/수식$$개를 $$수식$${c}$$/수식$$개씩 나누면 $$수식$${d}$$/수식$$묶음이 되고 " \
              "$$수식$${e}$$/수식$$개가 남으므로 잘못 말한 학생은 {P3}입니다.$$/수식$$\n\n"


    S = ["인형", "지우개", "알사탕", "초콜릿", "밤", "방울토마토", "호두"][np.random.randint(0, 7)]

    N = ["정호", "현기", "보아", "영서", "은지", "연주", "주호", "혁구", "영기", "상수", "은서", "동우", "재우", "진희", "준서", "유라", "수미", "현수",
         "채아", "민주", "지호", "연아", "은우", "시우", "혁재", "민하"]

    while True:
        N2 = np.random.choice(N, 3)
        P1, P2, P3 = N2

        if P1 != P2 and P2 != P3 and P3 != P1 : break

    term = np.random.randint(0, 7)

    if (term == 0):
        A = 14
        a = 2
        b = 7
        c = 3 or 4 or 5
        B = "$$수식$$1$$/수식$$개씩, $$수식$$2$$/수식$$개씩, $$수식$$7$$/수식$$개씩"

    elif (term == 1):
        A = 16
        a = 4
        b = 8
        c = 3 or 5 or 6
        B = "$$수식$$1$$/수식$$개씩, $$수식$$2$$/수식$$개씩, $$수식$$4$$/수식$$개씩, $$수식$$8$$/수식$$개씩"

    elif (term == 2):
        A = 20
        a = 4
        b = 5
        c = 3 or 6 or 7
        B = "$$수식$$1$$/수식$$개씩, $$수식$$2$$/수식$$개씩, $$수식$$4$$/수식$$개씩, $$수식$$5$$/수식$$개씩, $$수식$$10$$/수식$$개씩"

    elif (term == 3):
        A = 18
        a = 6
        b = 9
        c = 4 or 5 or 7
        B = "$$수식$$1$$/수식$$개씩, $$수식$$2$$/수식$$개씩, $$수식$$3$$/수식$$개씩, $$수식$$6$$/수식$$개씩, $$수식$$9$$/수식$$개씩"

    elif (term == 4):
        A = 27
        a = 3
        b = 9
        c = 4 or 5 or 6
        B = "$$수식$$1$$/수식$$개씩, $$수식$$3$$/수식$$개씩, $$수식$$9$$/수식$$개씩"

    elif (term == 5):
        A = 28
        a = 4
        b = 7
        c = 5 or 6
        B = "$$수식$$1$$/수식$$개씩, $$수식$$2$$/수식$$개씩, $$수식$$4$$/수식$$개씩, $$수식$$7$$/수식$$개씩, $$수식$$14$$/수식$$개씩"

    elif (term == 6):
        A = 30
        a = 5
        b = 6
        c = 4 or 7
        B = "$$수식$$1$$/수식$$개씩, $$수식$$2$$/수식$$개씩, $$수식$$3$$/수식$$개씩, $$수식$$5$$/수식$$개씩,$$수식$$6$$/수식$$개씩, $$수식$$10$$/수식$$개씩, $$수식$$15$$/수식$$개씩"

    d = math.trunc(A / c)
    e = A - c * d

    AAA = [P1, P2, P3]
    np.random.shuffle(AAA)
    A1, A2, A3 = AAA

    if (A1 == P1):
        a1 = a
    elif (A1 == P2):
        a1 = b
    else:
        a1 = c

    if (A2 == P1):
        a2 = a
    elif (A2 == P2):
        a2 = b
    else:
        a2 = c

    if (A3 == P1):
        a3 = a
    elif (A3 == P2):
        a3 = b
    else:
        a3 = c


    stem = stem.format(S=S, A=A, A1=A1, A2=A2, A3=A3, a1=a1, a2=a2, a3=a3)
    answer = answer.format(P3=P3)
    comment = comment.format(S=S, A=A, B=B, c=c, d=d, e=e, P3=P3)

    return stem, answer, comment







































# 3-2-4-06
def fraction324_Stem_002():
    stem = "□ 안에 알맞은 수를 차례대로 구하세요.\n$$수식$$LEFT ( 1 RIGHT ) ```` {A}$$/수식$${j1} $$수식$${a}$$/수식$$씩 묶으면 $$수식$${a}$$/수식$${j3} $$수식$${A}$$/수식$$의 $$수식$${{□}} over {n}$$/수식$$입니다.\n$$수식$$LEFT ( 2 RIGHT ) ```` {B}$$/수식$${j2} $$수식$${b}$$/수식$$씩 묶으면 $$수식$${C}$$/수식$${j4} $$수식$${B}$$/수식$$의 $$수식$${{□}} over {n}$$/수식$$입니다.\n"
    answer = "(정답)\n$$수식$$1$$/수식$$, $$수식$${d}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1 RIGHT ) ```` {A}$$/수식$${j1} $$수식$${a}$$/수식$$씩 묶으면 $$수식$${n}$$/수식$$묶음 중에서 " \
              "$$수식$${a}$$/수식$${j3} $$수식$$1$$/수식$$묶음이므로 $$수식$${A}$$/수식$$의 $$수식$$1 over {n}$$/수식$$입니다.\n" \
              "$$수식$$LEFT ( 2 RIGHT ) ```` {B}$$/수식$${j2} $$수식$${b}$$/수식$$씩 묶으면 $$수식$${n}$$/수식$$묶음 중에서 " \
              "$$수식$${C}$$/수식$${j4} $$수식$${d}$$/수식$$묶음이므로 $$수식$${B}$$/수식$$의 $$수식$${d} over {n}$$/수식$$입니다.\n\n"


    while (1):
        a = np.random.randint(4, 10)
        n = np.random.randint(4, 10)
        A = a * n
        b = np.random.randint(4, 10)
        B = b * n
        d = np.random.randint(2, n)
        C = b * d
        if (b != a):
            break

    s = "□"

    j1 = proc_jo(A, 1)
    j2 = proc_jo(B, 1)

    j3 = proc_jo(a, -1)
    j4 = proc_jo(C, -1)


    stem = stem.format(A=A, a=a, n=n, B=B, b=b, C=C, j1=j1, j2=j2, j3=j3, j4=j4)
    answer = answer.format(d=d)
    comment = comment.format(A=A, a=a, n=n, B=B, b=b, C=C, d=d, j1=j1, j2=j2, j3=j3, j4=j4)

    return stem, answer, comment



































# 3-2-4-07
def fraction324_Stem_003():
    stem = "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$${j2} 각각 $$수식$${a}$$/수식$$씩 묶을 때, □ 안에 알맞은 수가 더 큰 것의 기호를 써보세요.\n$$표$$ ㉠ $$수식$${a}$$/수식$${j3} $$수식$${A}$$/수식$$의 $$수식$${lg}1{rg} over {lg}□{rg}$$/수식$$입니다.\n㉡ $$수식$${C}$$/수식$${j4} $$수식$${B}$$/수식$$의 $$수식$${lg}□{rg} over {n}$$/수식$$입니다. $$/표$$\n"
    answer = "(정답)\n{X}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${A}$$/수식$${j5} $$수식$${a}$$/수식$$씩 묶으면 $$수식$${a}$$/수식$${j3} $$수식$${A}$$/수식$$의 $$수식$${lg}1{rg} over {m}$$/수식$$입니다. → □ $$수식$$= ` {m}$$/수식$$\n" \
              "㉡ $$수식$${B}$$/수식$${j2} $$수식$${a}$$/수식$$씩 묶으면 $$수식$${C}$$/수식$${j4} $$수식$${B}$$/수식$$의 $$수식$${d} over {n}$$/수식$$입니다. → □ $$수식$$= ` {d}$$/수식$$\n" \
              "따라서 □ 안에 알맞은 수가 더 큰 것은 {X} 입니다.\n\n"


    while (1):
        a = np.random.randint(4, 10)
        n = np.random.randint(4, 10)
        m = np.random.randint(4, 10)
        A = a * m
        B = a * n
        d = np.random.randint(2, n)
        C = a * d
        if (d != m):
            if (m < n):
                break

    s = "□"
    one = "1"

    lg = "{"
    rg = "}"

    if (m > d):
        X = "㉠"
    else:
        X = "㉡"

    j1 = proc_jo(A, 2)
    j2 = proc_jo(B, 1)
    j3 = proc_jo(a, -1)
    j4 = proc_jo(C, -1)
    j5 = proc_jo(A, 1)


    stem = stem.format(A=A, a=a, n=n, B=B, C=C, j1=j1, j2=j2, j3=j3, j4=j4, lg=lg, rg=rg)
    answer = answer.format(X=X)
    comment = comment.format(A=A, a=a, m=m, n=n, B=B, C=C, d=d, X=X, j2=j2, j3=j3, j4=j4, j5=j5, lg=lg, rg=rg)

    return stem, answer, comment




































# 3-2-4-08
def fraction324_Stem_004():
    stem = "$$수식$${A}$$/수식$$명의 {S1}들이 $$수식$${a}$$/수식$$명씩 한 {S2}{j2} 되어 놀이를 하려고 합니다. 한 {S2}에 있는 {S1}{j1} 전체의 얼마인지 분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$$1 over {n}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$명을 $$수식$${a}$$/수식$$명씩 묶으면 $$수식$${n}$$/수식$${S2}{j2} 되고, $$수식$${a}$$/수식$$명은 $$수식$${n}$$/수식$${S2} 중의 한 {S2}입니다.\n" \
              "따라서 한 {S2}에 있는 {S1} $$수식$${a}$$/수식$$명은 전체의 $$수식$$1 over {n}$$/수식$$입니다.\n\n"


    S1 = ["어린이", "학생", "사람"][np.random.randint(0, 3)]
    S2 = ["팀", "조", "모둠"][np.random.randint(0, 3)]

    a = np.random.randint(4, 10)
    n = np.random.randint(4, 10)
    A = a * n

    j1 = proc_jo(S1, -1)
    j2 = proc_jo(S2, 0)


    stem = stem.format(A=A, S1=S1, a=a, S2=S2, j1=j1, j2=j2)
    answer = answer.format(n=n)
    comment = comment.format(A=A, a=a, n=n, S2=S2, S1=S1, j2=j2)

    return stem, answer, comment







































# 3-2-4-09
def fraction324_Stem_005():
    stem = "어느 {S}에 오늘 하루 입장한 사람 수를 조사한 것입니다. 어린이 수는 입장한 전체 사람 수의 얼마인지 분수로 잘못 나타낸 것은 어느 것인가요?\n$$표$$ 어린이 $$수식$${A}$$/수식$$명, 청소년 $$수식$${B}$$/수식$$명, 어른 $$수식$${C}$$/수식$$명 $$/표$$\n① $$수식$${s1}$$/수식$$\n② $$수식$${s2}$$/수식$$\n③ $$수식$${s3}$$/수식$$\n④ $$수식$${s4}$$/수식$$\n⑤ $$수식$${s5}$$/수식$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$ 전체 입장객 수 $$수식$$ RIGHT ) ` = ` {A} ` + ` {B} ` + ` {C} ` = ` {D} ` LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${A}$$/수식$${j1} $$수식$${D}$$/수식$${j2} 각각 $$수식$${a}$$/수식$$씩, $$수식$${b}$$/수식$$씩, $$수식$${c}$$/수식$$씩, $$수식$${d}$$/수식$$씩 묶을 수 있습니다.\n" \
              "$$수식$${D}$$/수식$${j3} $$수식$${a}$$/수식$$씩 묶으면 $$수식$${m1}$$/수식$$묶음이 되고, $$수식$${A}$$/수식$${j4} $$수식$${m1}$$/수식$$묶음 중 " \
              "$$수식$${m2}$$/수식$$묶음 이므로 $$수식$${D}$$/수식$$의 $$수식$${m2} over {m1}$$/수식$$입니다.\n" \
              "$$수식$${D}$$/수식$${j3} $$수식$${b}$$/수식$$씩 묶으면 $$수식$${n1}$$/수식$$묶음이 되고, $$수식$${A}$$/수식$${j4} $$수식$${n1}$$/수식$$묶음 중 " \
              "$$수식$${n2}$$/수식$$묶음 이므로 $$수식$${D}$$/수식$$의 $$수식$${n2} over {n1}$$/수식$$입니다.\n" \
              "$$수식$${D}$$/수식$${j3} $$수식$${c}$$/수식$$씩 묶으면 $$수식$${p1}$$/수식$$묶음이 되고, $$수식$${A}$$/수식$${j4} $$수식$${p1}$$/수식$$묶음 중 " \
              "$$수식$${p2}$$/수식$$묶음 이므로 $$수식$${D}$$/수식$$의 $$수식$${p2} over {p1}$$/수식$$입니다.\n" \
              "$$수식$${D}$$/수식$${j3} $$수식$${d}$$/수식$$씩 묶으면 $$수식$${q1}$$/수식$$묶음이 되고, $$수식$${A}$$/수식$${j4} $$수식$${q1}$$/수식$$묶음 중 " \
              "$$수식$${q2}$$/수식$$묶음 이므로 $$수식$${D}$$/수식$$의 $$수식$${q2} over {q1}$$/수식$$입니다.\n\n"


    S = ["미술관", "전시관", "박물관", "체험장"][np.random.randint(0, 4)]

    while (1):
        b = [2, 3, 5, 7, 11][np.random.randint(0, 5)]
        c = [2, 3, 5, 7, 11][np.random.randint(0, 5)]

        a = b * c
        d = 1
        A = a

        D = np.random.randint(30, 71)

        B = np.random.randint((D - A) / 2 - 3, (D - A) / 2 + 4)

        C = D - (A + B)

        if (c + 1 < b):
            if (b * c <= 39):
                if (D == A * 2 or D == A * 3 or D == A * 5):
                    if (B != A and B != D - 2 * A):
                        break

    e = np.random.randint((c + 1), b)
    m1 = math.floor(D / a)
    m2 = math.floor(A / a)
    n1 = math.floor(D / b)
    n2 = math.floor(A / b)
    p1 = math.floor(D / c)
    p2 = math.floor(A / c)
    q1 = math.floor(D / d)
    q2 = math.floor(A / d)
    x1 = math.floor(b * e)
    x2 = e
    if (D == 50):
        x2 = e + 1

    s1 = "{%g} over {%g}" % (m2, m1)
    s2 = "{%g} over {%g}" % (n2, n1)
    s3 = "{%g} over {%g}" % (p2, p1)
    s4 = "{%g} over {%g}" % (q2, q1)
    s5 = "{%g} over {%g}" % (x2, x1)

    s6 = s5

    candidates = [s1, s2, s3, s4, s5]
    np.random.shuffle(candidates)

    s1, s2, s3, s4, s5 = candidates

    correct_idx = 0
    for i, t in enumerate(candidates):
        if t == s6:
            correct_idx = i
            break

    j1 = proc_jo(A, 2)
    j2 = proc_jo(D, -1)

    j3 = proc_jo(D, 1)
    j4 = proc_jo(A, -1)


    stem = stem.format(S=S, A=A, B=B, C=C, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(A=A, B=B, C=C, D=D, a=a, b=b, c=c, d=d, m1=m1, m2=m2, n1=n1, n2=n2, p1=p1, p2=p2, q1=q1,
                             q2=q2, j1=j1, j2=j2, j3=j3, j4=j4)

    return stem, answer, comment



































# 3-2-4-10
def fraction324_Stem_006():
    stem = "{S} $$수식$${A}$$/수식$$장을 $$수식$${a}$$/수식$$장씩 묶은 후 그 중 $$수식$${B}$$/수식$$장은 {P1}가 가지고, $$수식$${C}$$/수식$$장은 {P2}가 가졌습니다. 잘못 말한 사람은 누구인가요?\n$$표$$ {A1} : 내가 가진 {S} $$수식$${T1}$$/수식$$장은 $$수식$${A}$$/수식$$장의 $$수식$${T2} over {T3}$$/수식$$야.\n{A2} : 내가 가진 {S} $$수식$${T4}$$/수식$$장은 $$수식$${A}$$/수식$$장의 $$수식$${T5} over {T6}$$/수식$$야. $$/표$$\n"
    answer = "(정답)\n{P2}\n"
    comment = "(해설)\n" \
              "{A1} : $$수식$${A}$$/수식$$를 $$수식$${a}$$/수식$$씩 묶으면 $$수식$${T1}$$/수식$$는 $$수식$${n}$$/수식$$묶음 중 " \
              "$$수식$${T2}$$/수식$$묶음이므로 $$수식$${A}$$/수식$$의 $$수식$${T2} over {n}$$/수식$$입니다.\n" \
              "{A2} : $$수식$${A}$$/수식$$를 $$수식$${a}$$/수식$$씩 묶으면 $$수식$${T4}$$/수식$$는 $$수식$${n}$$/수식$$묶음 중 " \
              "$$수식$${T5}$$/수식$$묶음이므로 $$수식$${A}$$/수식$$의 $$수식$${T5} over {n}$$/수식$$입니다.\n" \
              "따라서 잘못 말한 사람은 {P2}입니다.\n\n"


    S = ["색종이", "도화지", "색도화지", "한지", "포장지"][np.random.randint(0, 5)]

    N = ["정호", "현기", "보아", "영서", "은지", "연주", "주호", "혁구", "영기", "상수", "은서", "동우", "재우", "진희", "준서", "유라", "수미", "현수",
         "채아", "민주", "지호", "연아", "은우", "시우", "혁재", "민하"]

    while True:
        N2 = np.random.choice(N, 2)
        P1, P2 = N2

        if P1 != P2: break

    while (1):
        a = np.random.randint(4, 13)
        n = np.random.randint(4, 10)
        A = a * n
        b = np.random.randint(2, n - 1)
        c = n - b
        B = a * b
        C = a * c
        if (20 <= a * n) and (a * n <= 90):
            if (b != n / 2):
                break

    P = [P1, P2]
    np.random.shuffle(P)
    A1, A2 = P

    if (A1 == P1):
        T1 = B
        T2 = b
        T3 = n

    else:
        T1 = C
        T2 = c
        T3 = A

    if (A2 == P1):
        T4 = B
        T5 = b
        T6 = n

    else:
        T4 = C
        T5 = c
        T6 = A


    stem = stem.format(a=a, S=S, A=A, P1=P1, P2=P2, n=n, b=b, c=c, B=B, C=C, T1=T1, T2=T2, T3=T3, T4=T4, A1=A1, A2=A2,
                       T5=T5, T6=T6)
    answer = answer.format(P2=P2)
    comment = comment.format(S=S, A=A, B=B, a=a, b=b, n=n, C=C, c=c, P2=P2, A1=A1, A2=A2, T1=T1, T2=T2, T4=T4, T5=T5,
                             P1=P1)

    return stem, answer, comment







































# 3-2-4-11
def fraction324_Stem_007():
    stem = "{P1}네 학교에서 {P2}에게 {S}을 배달하는 봉사 활동을 했습니다. {P1}는 전체 {S} $$수식$${A}$$/수식$$개 중에서 $$수식$${B}$$/수식$$개를 배달했습니다. 전체 {S}을 $$수식$${a}$$/수식$$개씩 묶으면 {P1}가 배달한 {S} $$수식$${B}$$/수식$$개는 전체의 몇 분의 몇인가요?\n"
    answer = "(정답)\n$$수식$${b} over {n}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$를 $$수식$${a}$$/수식$$씩 묶으면 $$수식$${n}$$/수식$$묶음이 되고, " \
              "$$수식$${B}$$/수식$$은 $$수식$${n}$$/수식$$묶음 중 $$수식$${b}$$/수식$$묶음이므로 $$수식$${A}$$/수식$$의 $$수식$${b} over {n}$$/수식$$입니다.\n\n"


    P1 = \
    ["정호", "현기", "재수", "영서", "은지", "연주", "주호", "혁구", "영기", "상수", "은서", "동우", "재우", "진희", "준서", "유라", "수미", "현수", "채아",
     "민주", "지호", "연아", "은우", "시우", "혁재", "민하"][np.random.randint(0, 26)]

    P2 = ["홀몸 노인", "소년소녀 가장"][np.random.randint(0, 2)]

    S = ["도시락", "반찬통", "김치통"][np.random.randint(0, 3)]

    a = np.random.randint(4, 10)
    n = np.random.randint(6, 10)
    A = a * n
    b = np.random.randint(2, n - 3)
    B = a * b


    stem = stem.format(P1=P1, P2=P2, S=S, A=A, B=B, a=a)
    answer = answer.format(b=b, n=n)
    comment = comment.format(A=A, B=B, a=a, b=b, n=n)

    return stem, answer, comment









































# 3-2-4-12
def fraction324_Stem_008():
    stem = "나타내는 수가 다른 하나를 찾아 기호를 써 보세요.\n$$표$$ ㉠ {X1}  ㉡ {X2}  ㉢ {X3} $$/표$$\n"
    answer = "(정답)\n{X}\n"
    comment = "(해설)\n" \
              "㉠ {X1}은 $$수식$${Y1}$$/수식$$입니다.\n" \
              "㉡ {X2}은 $$수식$${Y2}$$/수식$$입니다.\n" \
              "㉢ {X3}은 $$수식$${Y3}$$/수식$$입니다.\n" \
              "따라서 나타내는 수가 다른 것은 {X}입니다.\n\n"


    while (1):
        a = np.random.randint(4, 10)
        b = np.random.randint(4, 10)
        c = np.random.randint(4, 10)
        D = np.random.randint(6, 10)
        E = np.random.randint(6, 10)
        F = np.random.randint(6, 10)
        A = a * D
        B = b * E
        C = c * F
        if (a != b and b != c and c != a):
            if (E == D and F != D):
                break


    XA = "$$수식$$%s$$/수식$$의 $$수식$${1} over {%s}$$/수식$$" % (A, a)
    XB = "$$수식$$%s$$/수식$$의 $$수식$${1} over {%s}$$/수식$$" % (B, b)
    XC = "$$수식$$%s$$/수식$$의 $$수식$${1} over {%s}$$/수식$$" % (C, c)

    XXX = [XA, XB, XC]
    np.random.shuffle(XXX)
    X1, X2, X3 = XXX

    if (X1 == XA):
        Y1 = D
    elif (X1 == XB):
        Y1 = E
    else:
        Y1 = F
        X = "㉠"

    if (X2 == XA):
        Y2 = D
    elif (X2 == XB):
        Y2 = E
    else:
        Y2 = F
        X = "㉡"

    if (X3 == XA):
        Y3 = D
    elif (X3 == XB):
        Y3 = E
    else:
        Y3 = F
        X = "㉢"


    stem = stem.format(X1=X1, X2=X2, X3=X3)
    answer = answer.format(X=X)
    comment = comment.format(X1=X1, X2=X2, X3=X3, Y1=Y1, Y2=Y2, Y3=Y3, X=X)

    return stem, answer, comment











































# 3-2-4-16
def fraction324_Stem_009():
    stem = "나타내는 수가 가장 큰 것의 기호를 써 보세요.\n$$표$$ ㉠ {XA}  ㉡ {XB}  ㉢ {XC} $$/표$$\n"
    answer = "(정답)\n{X}\n"
    comment = "(해설)\n" \
              "㉠ {XA}{ja1} $$수식$${A}$$/수식$${jb1} 똑같이 $$수식$${a1}$$/수식$$묶음으로 나눈 것 중의 $$수식$${a2}$$/수식$$묶음이므로 $$수식$${D}$$/수식$$입니다.\n" \
              "㉡ {XB}{ja2} $$수식$${B}$$/수식$${jb2} 똑같이 $$수식$${b1}$$/수식$$묶음으로 나눈 것 중의 $$수식$${b2}$$/수식$$묶음이므로 $$수식$${E}$$/수식$$입니다.\n" \
              "㉢ {XC}{ja3} $$수식$${C}$$/수식$${jb3} 똑같이 $$수식$${c1}$$/수식$$묶음으로 나눈 것 중의 $$수식$${c2}$$/수식$$묶음이므로 $$수식$${F}$$/수식$$입니다.\n" \
              "따라서 $$수식$${G} &gt; {H} &gt; {I}$$/수식$$이므로 가장 큰 것은 {X}입니다.\n\n"


    while (1):
        n = np.random.randint(3, 8)
        p = np.random.randint(3, 8)
        q = np.random.randint(3, 8)

        a2 = np.random.randint(1, 5)
        b2 = np.random.randint(1, 5)
        c2 = np.random.randint(1, 5)

        a1 = np.random.randint(5, 10)
        b1 = np.random.randint(5, 10)
        c1 = np.random.randint(5, 10)

        if (n != p and n != q and p != q):
            if (a2 != b2 and b2 != c2 and c2 != a2):
                if (a2 * n != b2 * p and b2 * p != c2 * q and c2 * q != a2 * n):
                    if (a1 != b1 and b1 != c1 and c1 != a1):
                        if (a1 * n != b1 * p and b1 * p != c1 * q and c1 * q != a1 * n):
                            break


    A = a1 * n
    B = b1 * p
    C = c1 * q

    D = a2 * n
    E = b2 * p
    F = c2 * q

    if (D > E):
        if (D > F):
            if (E > F):
                G = D
                H = E
                I = F
            else:
                G = D
                H = F
                I = E
        else:
            G = F
            H = D
            I = E
    elif (E > D):
        if (F > D):
            if (E > F):
                G = E
                H = F
                I = D
            else:
                G = F
                H = E
                I = D
        else:
            G = E
            H = D
            I = F

    XA = "$$수식$$%s$$/수식$$의 $$수식$${%s} over {%s}$$/수식$$" % (A, a2, a1)
    XB = "$$수식$$%s$$/수식$$의 $$수식$${%s} over {%s}$$/수식$$" % (B, b2, b1)
    XC = "$$수식$$%s$$/수식$$의 $$수식$${%s} over {%s}$$/수식$$" % (C, c2, c1)

    if (G == D):
        X = "㉠"
    elif (G == E):
        X = "㉡"
    else:
        X = "㉢"

    ja1 = proc_jo(a2, -1)
    jb1 = proc_jo(A, 1)

    ja2 = proc_jo(b2, -1)
    jb2 = proc_jo(B, 1)

    ja3 = proc_jo(c2, -1)
    jb3 = proc_jo(C, 1)


    stem = stem.format(XA=XA, XB=XB, XC=XC)
    answer = answer.format(X=X)
    comment = comment.format(XA=XA, XB=XB, XC=XC, A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, I=I, a1=a1, b1=b1, a2=a2,
                             b2=b2, c1=c1, c2=c2, X=X, ja1=ja1, jb1=jb1, ja2=ja2, jb2=jb2, ja3=ja3, jb3=jb3)

    return stem, answer, comment











































# 3-2-4-17
def fraction324_Stem_010():
    stem = "틀린 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${A}$$/수식$$의 $$수식$${a2} over {a1}$$/수식$${j1} $$수식$${T3}$$/수식$$입니다.\n㉡ $$수식$${A}$$/수식$$의 $$수식$${b2} over {b1}$$/수식$${j2} $$수식$${U3}$$/수식$$입니다.\n㉢ $$수식$${A}$$/수식$$의 $$수식$${c2} over {c1}$$/수식$${j3} $$수식$${V3}$$/수식$$입니다.$$/표$$\n"
    answer = "(정답)\n{X}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${A}$$/수식$$의 $$수식$${a2} over {a1}$$/수식$${j1} $$수식$${A}$$/수식$${j4} 똑같이 $$수식$${a1}$$/수식$$묶음으로 나눈 것 중의 $$수식$${a2}$$/수식$$묶음이므로 $$수식$${B}$$/수식$$입니다.\n" \
              "㉡ $$수식$${A}$$/수식$$의 $$수식$${b2} over {b1}$$/수식$${j2} $$수식$${A}$$/수식$${j4} 똑같이 $$수식$${b1}$$/수식$$묶음으로 나눈 것 중의 $$수식$${b2}$$/수식$$묶음이므로 $$수식$${C}$$/수식$$입니다.\n" \
              "㉢ $$수식$${A}$$/수식$$의 $$수식$${c2} over {c1}$$/수식$${j3} $$수식$${A}$$/수식$${j4} 똑같이 $$수식$${c1}$$/수식$$묶음으로 나눈 것 중의 $$수식$${c2}$$/수식$$묶음이므로 $$수식$${D}$$/수식$$입니다.\n" \
              "따라서 틀린 것은 {X}입니다.\n\n"


    term = np.random.randint(0, 8)
    if (term == 0):
        n = 2
        p = 2
        q = 5
    elif (term == 1):
        n = 2
        p = 2
        q = 7
    elif (term == 2):
        n = 2
        p = 3
        q = 5
    elif (term == 3):
        n = 2
        p = 3
        q = 7
    elif (term == 4):
        n = 3
        p = 3
        q = 5
    elif (term == 5):
        n = 3
        p = 3
        q = 7
    elif (term == 6):
        n = 3
        p = 4
        q = 4
    elif (term == 7):
        n = 3
        p = 4
        q = 5

    while (1):
        a1 = [n, p, q, n * p][np.random.randint(0, 4)]
        b1 = [n, p, q, n * p][np.random.randint(0, 4)]
        c1 = [n, p, q, n * p][np.random.randint(0, 4)]
        A = n * p * q
        a2 = np.random.randint(1, a1)
        b2 = np.random.randint(1, b1)
        c2 = np.random.randint(1, c1)
        if (a1 != b1 and b1 != c1 and c1 != a1):
            if (a2 != b2 and b2 != c2 and c2 != a2):
                if (a1 * a2 < A and b1 * b2 < A and c1 * c2 < A):
                    break


    B = math.floor((A / a1) * a2)
    C = math.floor((A / b1) * b2)
    D = math.floor((A / c1) * c2)
    E = c1 * c2

    XX = np.random.randint(0, 3)
    N = [B, C, D]
    N[XX] = E

    T3, U3, V3 = N

    if (XX == 0):
        X = "㉠"
    elif (XX == 1):
        X = "㉡"
    else:
        X = "㉢"

    j1 = proc_jo(a2, -1)
    j2 = proc_jo(b2, -1)
    j3 = proc_jo(c2, -1)
    j4 = proc_jo(A, 1)


    stem = stem.format(A=A, a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, T3=T3, V3=V3, U3=U3, j1=j1, j2=j2, j3=j3)
    answer = answer.format(X=X)
    comment = comment.format(A=A, a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, B=B, C=C, D=D, X=X, j1=j1, j2=j2, j3=j3,
                             j4=j4)

    return stem, answer, comment












































# 3-2-4-18
def fraction324_Stem_011():
    stem = "{S} $$수식$${A}$$/수식$$자루의 $$수식$${a2} over {a1}$$/수식$$은 {C}입니다. {C} {S}은 몇 자루인가요?\n"
    answer = "(정답)\n$$수식$${B}$$/수식$$자루\n"
    comment = "(해설)\n" \
              "{S} $$수식$${A}$$/수식$$자루의 $$수식$${a2} over {a1}$$/수식$${j1} $$수식$${A}$$/수식$${j2} 똑같이 " \
              "$$수식$${a1}$$/수식$$묶음으로 나눈 것 중의 $$수식$${a2}$$/수식$$묶음이므로 $$수식$${B}$$/수식$$자루입니다.\n\n"


    S = ["색연필", "볼펜", "사인펜"][np.random.randint(0, 3)]
    C = ["빨간색", "검은색", "파란색", "초록색"][np.random.randint(0, 4)]

    n = np.random.randint(4, 10)
    a1 = np.random.randint(4, 10)
    a2 = np.random.randint(1, a1)

    A = a1 * n
    B = math.floor((A / a1) * a2)

    j1 = proc_jo(a2, -1)
    j2 = proc_jo(A, 1)


    stem = stem.format(S=S, A=A, a2=a2, a1=a1, C=C)
    answer = answer.format(B=B)
    comment = comment.format(S=S, A=A, a2=a2, a1=a1, B=B, j1=j1, j2=j2)

    return stem, answer, comment













































# 3-2-4-19
def fraction324_Stem_012():
    stem = "{P1}는 {S}를 $$수식$${A}$$/수식$$장 가지고 있습니다. 이 중에서 $$수식$${a2} over {a1}$$/수식$${j1} 친구에게 주었습니다. 친구에게 준 {S}는 몇 장인가요?\n"
    answer = "(정답)\n$$수식$${B}$$/수식$$장\n"
    comment = "(해설)\n" \
              "{S} $$수식$${A}$$/수식$$장의 $$수식$${a2} over {a1}$$/수식$${j2} $$수식$${A}$$/수식$${j3} 똑같이 " \
              "$$수식$${a1}$$/수식$$묶음으로 나눈 것 중의 $$수식$${a2}$$/수식$$묶음이므로 $$수식$${B}$$/수식$$장입니다.\n\n"


    P1 = ["정호", "현기", "보아", "주호", "혁구", "영기", "상수", "동우", "재우", "준서", "현수", "시우", "혁재"][np.random.randint(0, 13)]
    P2 = ["친구", "동생", "사촌 동생", "사촌 형"][np.random.randint(0, 4)]
    S = ["딱지", "색도화지", "색종이"][np.random.randint(0, 3)]

    n = np.random.randint(4, 10)
    a1 = np.random.randint(4, 10)
    a2 = np.random.randint(1, (a1 / 2) + 1)

    A = a1 * n
    B = math.floor((A / a1) * a2)

    j1 = proc_jo(a2, 1)
    j2 = proc_jo(a2, -1)
    j3 = proc_jo(A, 1)


    stem = stem.format(P1=P1, S=S, A=A, a2=a2, a1=a1, P2=P2, j1=j1)
    answer = answer.format(B=B)
    comment = comment.format(S=S, A=A, a2=a2, a1=a1, B=B, j2=j2, j3=j3)

    return stem, answer, comment












































# 3-2-4-20
def fraction324_Stem_013():
    stem = "{P}는 새로 산 건전지 $$수식$${A}$$/수식$$개의 $$수식$${a2} over {a1}$$/수식$${j1} {S}에 사용하였습니다. {P}가 {S}에 사용한 건전지는 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${B}$$/수식$$개\n"
    comment = "(해설)\n" \
              "건전지 $$수식$${A}$$/수식$$개의 $$수식$${a2} over {a1}$$/수식$${j2} $$수식$${A}$$/수식$${j3} 똑같이 " \
              "$$수식$${a1}$$/수식$$묶음으로 나눈 것 중의 $$수식$${a2}$$/수식$$묶음이므로 $$수식$${B}$$/수식$$개입니다.\n\n"


    P = ["정호", "현기", "보아", "주호", "혁구", "영기", "상수", "동우", "재우", "준서", "현수", "시우", "혁재"][np.random.randint(0, 13)]
    S = ["드론", "무선 조종기", "장난감 자동차", "장난감 비행기", "장난감 보트"][np.random.randint(0, 5)]

    n = np.random.randint(3, 6)
    a1 = np.random.randint(4, 7)
    a2 = np.random.randint(1, (a1 / 2) + 1)

    A = a1 * n
    B = math.floor(n * a2)

    j1 = proc_jo(a2, 1)
    j2 = proc_jo(a2, -1)
    j3 = proc_jo(A, 1)


    stem = stem.format(P=P, S=S, A=A, a2=a2, a1=a1, j1=j1)
    answer = answer.format(B=B)
    comment = comment.format(S=S, A=A, a2=a2, a1=a1, B=B, j2=j2, j3=j3)

    return stem, answer, comment















































# 3-2-4-21
def fraction324_Stem_014():
    stem = "공책 $$수식$${A}$$/수식$$권 중 {P1}는 전체의 $$수식$${a2} over {a1}$$/수식$${j1}, {P2}{j6} 전체의 $$수식$${b2} over {b1}$$/수식$${j2} 가졌습니다. {P1}와 {P2} 중에서 공책을 더 많이 가진 사람은 누구인가요?\n"
    answer = "(정답)\n{X}\n"
    comment = "(해설)\n" \
              "{P1} : 공책 $$수식$${A}$$/수식$$권의 $$수식$${a2} over {a1}$$/수식$${j3} $$수식$${A}$$/수식$${j5} " \
              "똑같이 $$수식$${a1}$$/수식$$묶음으로 나눈 것 중의 $$수식$${a2}$$/수식$$묶음이므로 $$수식$${B}$$/수식$$권입니다.\n" \
              "{P2} : 공책 $$수식$${A}$$/수식$$권의 $$수식$${b2} over {b1}$$/수식$${j4} $$수식$${A}$$/수식$${j5} " \
              "똑같이 $$수식$${b1}$$/수식$$묶음으로 나눈 것 중의 $$수식$${b2}$$/수식$$묶음이므로 $$수식$${C}$$/수식$$권입니다.\n" \
              "따라서 공책을 더 많이 가진 사람은 {X}입니다.\n\n"


    P1 = ["효리", "은지", "연주", "은서", "진희", "유라", "수미", "채아", "민주", "지수", "연아", "은하", "민아"][np.random.randint(0, 13)]

    P2 = ["동생", "오빠", "친구", "언니"][np.random.randint(0, 4)]

    term = np.random.randint(0, 8)

    if (term == 0):
        n = 2
        p = 2
        q = 5
    elif (term == 1):
        n = 2
        p = 2
        q = 7
    elif (term == 2):
        n = 2
        p = 3
        q = 5
    elif (term == 3):
        n = 2
        p = 3
        q = 7
    elif (term == 4):
        n = 3
        p = 3
        q = 5
    elif (term == 5):
        n = 3
        p = 3
        q = 7
    elif (term == 6):
        n = 3
        p = 4
        q = 4
    elif (term == 7):
        n = 3
        p = 4
        q = 5

    while (1):
        a1 = [q, n * p, n * q, p * q][np.random.randint(0, 4)]
        b1 = [q, n * p, n * q, p * q][np.random.randint(0, 4)]
        A = n * p * q
        a2 = np.random.randint(2, (a1 / 2) + 1)
        b2 = np.random.randint(1, (b1 / 2) + 1)
        if (a1 != b1):
            if (a2 != b2):
                break

    B = math.floor((A / a1) * a2)
    C = math.floor((A / b1) * b2)

    if (B > C):
        X = P1
    else:
        X = P2

    j1 = proc_jo(a2, 1)
    j2 = proc_jo(b2, 1)

    j3 = proc_jo(a2, -1)
    j4 = proc_jo(b2, -1)

    j5 = proc_jo(A, 1)
    j6 = proc_jo(P2, -1)


    stem = stem.format(A=A, P1=P1, a2=a2, a1=a1, P2=P2, b2=b2, b1=b1, j1=j1, j2=j2, j6=j6)
    answer = answer.format(X=X)
    comment = comment.format(A=A, P1=P1, a2=a2, a1=a1, P2=P2, b2=b2, b1=b1, B=B, C=C, X=X, j3=j3, j4=j4, j5=j5)

    return stem, answer, comment












































# 3-2-4-25
def fraction324_Stem_015():
    stem = "$$수식$${A}$$/수식$$시간의 $$수식$$1 over {a1}$$/수식$$은 몇 시간인가요?\n"
    answer = "(정답)\n$$수식$${B}$$/수식$$시간\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$${j1} 똑같이 $$수식$${a1}$$/수식$${j2} 나눈 것 중의 1은 $$수식$${B}$$/수식$$이므로 " \
              "$$수식$${A}$$/수식$$시간의 $$수식$$1 over {a1}$$/수식$$은 $$수식$${B}$$/수식$$시간입니다.\n\n"


    while (1):
        n = np.random.randint(2, 7)
        a1 = np.random.randint(4, 7)
        A = a1 * n
        B = math.floor(A / a1)
        if (10 <= A) and (A <= 24):
            break

    j1 = proc_jo(A, 1)

    if a1 == 6:
        j2 = "으로"
    else:
        j2 = "로"


    stem = stem.format(A=A, a1=a1)
    answer = answer.format(B=B)
    comment = comment.format(A=A, a1=a1, B=B, j1=j1, j2=j2)

    return stem, answer, comment













































# 3-2-4-27
def fraction324_Stem_016():
    stem = "두 사람의 대화를 읽고 하루에 잠을 더 많이 자는 사람은 누구인가요?\n$$표$${P1} : 나는 하루 $$수식$$24$$/수식$$시간 중 $$수식$${a2} over {a1}$$/수식$$만큼 잠을 자.\n{P2} : 나는 하루 $$수식$$24$$/수식$$시간 중 $$수식$${b2} over {b1}$$/수식$$ 만큼 잠을 자.$$/표$$\n"
    answer = "(정답)\n{X}\n"
    comment = "(해설)\n" \
              "{P1} : $$수식$$24$$/수식$$시간을 똑같이 $$수식$${a1}$$/수식$${j1} 나눈 것 중의 $$수식$$1$$/수식$$은 $$수식$${m}$$/수식$$이므로 " \
              "$$수식$$24$$/수식$$시간의 $$수식$${a2} over {a1}$$/수식$${j3} $$수식$${A}$$/수식$$시간입니다.\n" \
              "{P2} : $$수식$$24$$/수식$$시간을 똑같이 $$수식$${b1}$$/수식$${j2} 나눈 것 중의 $$수식$$1$$/수식$$은 $$수식$${n}$$/수식$$이므로 " \
              "$$수식$$24$$/수식$$시간의 $$수식$${b2} over {b1}$$/수식$${j4} $$수식$${B}$$/수식$$시간입니다.\n" \
              "따라서 하루에 잠을 더 많이 자는 사람은 {X}입니다.\n\n"


    N = ["정호", "현기", "태희", "영서", "은지", "연주", "주호", "혁구", "영기", "상수", "은서", "동우", "재우", "진희", "준서", "유라", "수미", "현수",
         "채아", "민주", "지호", "연아", "은우", "시우", "혁재", "민하"]

    while True:
        N2 = np.random.choice(N, 2)
        P1, P2 = N2

        if P1 != P2: break

    while (1):
        term = np.random.randint(0, 8)
        if (term == 0):
            a1 = 3
            a2 = 1
        elif (term == 1):
            a1 = 4
            a2 = 1
        elif (term == 2):
            a1 = 6
            a2 = 2
        elif (term == 3):
            a1 = 8
            a2 = 2
        elif (term == 4):
            a1 = 8
            a2 = 3
        elif (term == 5):
            a1 = 12
            a2 = 3
        elif (term == 6):
            a1 = 12
            a2 = 4
        elif (term == 7):
            a1 = 12
            a2 = 5

        term1 = np.random.randint(0, 8)
        if (term1 == 0):
            b1 = 3
            b2 = 1
        elif (term1 == 1):
            b1 = 4
            b2 = 1
        elif (term1 == 2):
            b1 = 6
            b2 = 2
        elif (term1 == 3):
            b1 = 8
            b2 = 2
        elif (term1 == 4):
            b1 = 8
            b2 = 3
        elif (term1 == 5):
            b1 = 12
            b2 = 3
        elif (term1 == 6):
            b1 = 12
            b2 = 4
        elif (term1 == 7):
            b1 = 12
            b2 = 5

        if (a2 * b1 != b2 * a1):
            break

    A = math.floor((24 / a1) * a2)
    B = math.floor((24 / b1) * b2)

    if (A > B):
        X = P1
    else:
        X = P2

    m = math.floor(24 / a1)
    n = math.floor(24 / b1)

    if (str(a1))[-1] == "3" or (str(a1))[-1] == "6":
        j1 = "으로"
    else:
        j1 = "로"

    if (str(b1))[-1] == "3" or (str(b1))[-1] == "6":
        j2 = "으로"
    else:
        j2 = "로"

    j3 = proc_jo(a2, -1)
    j4 = proc_jo(b2, -1)


    stem = stem.format(A=A, a1=a1, a2=a2, P1=P1, b1=b1, b2=b2, P2=P2)
    answer = answer.format(X=X)
    comment = comment.format(A=A, a1=a1, a2=a2, B=B, b1=b1, b2=b2, P1=P1, P2=P2, X=X, m=m, n=n, j1=j1, j2=j2, j3=j3,
                             j4=j4)

    return stem, answer, comment



















































# 3-2-4-28
def fraction324_Stem_017():
    stem = "{P}는 길이가 $$수식$${A} rm {{cm}}$$/수식$$인 {S}의 $$수식$${a2} over {a1}$$/수식$${j1} 사용하였습니다. 남은 {S}{j2} 몇 $$수식$$rm {{cm}}$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${C} rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A} rm {{cm}}$$/수식$$를 똑같이 $$수식$${a1}$$/수식$$부분으로 나눈 것 중의 $$수식$${a2}$$/수식$$부분은 $$수식$${B} rm {{cm}}$$/수식$$이므로 " \
              "사용한 {S}{j2} $$수식$${B} rm {{cm}}$$/수식$$입니다.\n" \
              "따라서 남은 {S}{j2} $$수식$${A} ` - ` {B} ` = ` {C} LEFT ( rm {{cm}} RIGHT )$$/수식$$입니다.\n\n"


    P = \
    ["정호", "현기", "보아", "영서", "은지", "연주", "주호", "혁구", "영기", "상수", "은서", "동우", "재우", "진희", "준서", "유라", "수미", "현수", "채아",
     "민주", "지호", "연아", "은우", "시우", "혁재", "민하"][np.random.randint(0, 26)]

    S = ["철사", "리본", "노끈", "종이테이프", "색테이프"][np.random.randint(0, 5)]

    n = np.random.randint(4, 10)
    a1 = np.random.randint(4, 10)
    a2 = np.random.randint(1, a1 - 1)

    A = a1 * n
    B = a2 * n
    C = A - B

    j1 = proc_jo(a2, 1)
    j2 = proc_jo(S, -1)


    stem = stem.format(P=P, S=S, A=A, a2=a2, a1=a1, j1=j1, j2=j2)
    answer = answer.format(C=C)
    comment = comment.format(S=S, A=A, a2=a2, a1=a1, B=B, C=C, j2=j2)

    return stem, answer, comment












































# 3-2-4-29
def fraction324_Stem_018():
    stem = "일정하게 물이 나오는 수도로 빈 {S}에 물을 가득 받는 데 $$수식$${A}$$/수식$$분이 걸립니다. 지금까지 물을 {S}의 $$수식$${a2} over {a1}$$/수식$$만큼 받았다면, 몇 분 동안 물을 틀어 놓은 것인가요?\n"
    answer = "(정답)\n$$수식$${B}$$/수식$$분\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 $$수식$${a2} over {a1}$$/수식$${j1} $$수식$${A}$$/수식$${j2} $$수식$${a1}$$/수식$${j3} 똑같이 나눈 것 중의 $$수식$${a2}$$/수식$$이므로 $$수식$${B}$$/수식$$입니다.\n" \
              "따라서 $$수식$${A}$$/수식$$분의 $$수식$${a2} over {a1}$$/수식$${j1} $$수식$${B}$$/수식$$분입니다.\n\n"


    S = ["욕조", "수조", "수족관", "물탱크", "드럼통"][np.random.randint(0, 5)]

    while (1):
        n = np.random.randint(2, 10)
        a1 = np.random.randint(4, 10)
        a2 = np.random.randint(1, a1 - 1)
        A = a1 * n
        B = a2 * n
        if (10 <= a1 * n) and (a1 * n <= 30):
            break

    j1 = proc_jo(a2, -1)
    j2 = proc_jo(A, 1)

    if (str(a1))[-1] == "3" or (str(a1))[-1] == "6":
        j3 = "으로"
    else:
        j3 = "로"


    stem = stem.format(S=S, A=A, a1=a1, a2=a2)
    answer = answer.format(B=B)
    comment = comment.format(A=A, a2=a2, a1=a1, B=B, j1=j1, j2=j2, j3=j3)

    return stem, answer, comment














































# 3-2-4-30
def fraction324_Stem_019():
    stem = "{P}는 {S1} 한 {S2}{j1} 똑같이 나눈 것 중 $$수식$${B}$$/수식$$조각을 먹었습니다. {P}가 먹은 {S1}{j2} 한 {S2}의 $$수식$${a2} over {a1}$$/수식$$일 때, {S1} 한 {S2}{j3} 모두 몇 조각인가요?\n"
    answer = "(정답)\n$$수식$${A}$$/수식$$조각\n"
    comment = "(해설)\n" \
              "$$수식$${a2} over {a1}$$/수식$${j4} $$수식$$1 over {a1}$$/수식$$의 $$수식$${a2}$$/수식$$배이므로, " \
              "{S1} 한 {S2}의 $$수식$$1 over {a1}$$/수식$$은 $$수식$${B} DIV {a2} ` = `{n} LEFT ($$/수식$$조각$$수식$$RIGHT )$$/수식$$입니다.\n" \
              "{S1} 한 {S2}{j1} 똑같이 $$수식$${a1}$$/수식$${j5} 나눈 것 중의 $$수식$$1$$/수식$$이 $$수식$${n}$$/수식$$조각이므로, " \
              "{S1} 한 {S2}{j3} 모두 $$수식$${n} TIMES {a1} ` = ` {A} LEFT ($$/수식$$조각$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    P = \
    ["철우", "지우", "정호", "현기", "재수", "영서", "은지", "연주", "주호", "혁구", "영기", "상수", "은서", "동우", "재우", "진희", "준서", "유라", "수미",
     "현수", "채아", "민주", "지호", "연아", "은우", "시우", "혁재", "민하"][np.random.randint(0, 28)]

    term = np.random.randint(0, 5)
    if (term == 0):
        S1 = "피자"
        S2 = "판"
    elif (term == 1):
        S1 = "호두파이"
        S2 = "개"
    elif (term == 2):
        S1 = "사과파이"
        S2 = "개"
    elif (term == 3):
        S1 = "빈대떡"
        S2 = "개"
    elif (term == 4):
        S1 = "부침개"
        S2 = "개"

    while (1):
        a1 = np.random.randint(4, 10)
        a2 = np.random.randint(2, a1)
        n = np.random.randint(2, 6)
        B = a2 * n
        A = a1 * n

        if (n <= (20 / a1)):
            break

    j1 = proc_jo(S2, 1)
    j2 = proc_jo(S1, -1)
    j3 = proc_jo(S2, -1)

    j4 = proc_jo(a2, -1)

    if (str(a1))[-1] == "3" or (str(a1))[-1] == "6":
        j5 = "으로"
    else:
        j5 = "로"


    stem = stem.format(P=P, S1=S1, S2=S2, B=B, a1=a1, a2=a2, j1=j1, j2=j2, j3=j3)
    answer = answer.format(A=A)
    comment = comment.format(a1=a1, a2=a2, S1=S1, S2=S2, B=B, n=n, A=A, j1=j1, j3=j3, j4=j4, j5=j5)

    return stem, answer, comment

















































# 3-2-4-32
def fraction324_Stem_020():
    stem = "떨어진 높이의 $$수식$${a2} over {a1}$$/수식$$만큼 튀어 오르는 공이 있습니다. $$수식$${A} rm m$$/수식$$ 높이에서 이 공을 떨어트린다면, 두 번째로 튀어 오르는 공의 높이는 몇 $$수식$$rm m$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${C} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "공이 첫 번째로 튀어 오르는 높이는 $$수식$${A} rm m$$/수식$$의 $$수식$${a2} over {a1}$$/수식$$인 $$수식$${B} rm m$$/수식$$이고, " \
              "두 번째로 튀어 오르는 높이는 $$수식$${B} rm m$$/수식$$의 $$수식$${a2} over {a1}$$/수식$$인 $$수식$${C} rm m$$/수식$$입니다.\n\n"


    while (1):
        a1 = np.random.randint(4, 8)
        a2 = np.random.randint(2, (a1 / 2) + 1)
        n = np.random.randint(2, 7)
        A = a1 * a1 * n
        B = math.floor((A / a1) * a2)
        C = math.floor((B / a1) * a2)

        if (n <= 99 / (a1 * a1)) and soro_so(a1, a2) == 1:
            break

    stem = stem.format(a1=a1, a2=a2, A=A)
    answer = answer.format(C=C)
    comment = comment.format(a1=a1, a2=a2, A=A, B=B, C=C)

    return stem, answer, comment












































# 3-2-4-33
def fraction324_Stem_021():
    stem = "$$수식$${lg}{S}{rg} over {A}$$/수식$$ 는 진분수입니다. 다음 중 {S}가 될 수 없는 수를 고르세요.\n① $$수식$${AA}$$/수식$$  ② $$수식$${BB}$$/수식$$  ③ $$수식$${CC}$$/수식$$  ④ $$수식$${DD}$$/수식$$  ⑤ $$수식$${EE}$$/수식$$\n"
    answer = "(정답)\n{ANS}\n"
    comment = "(해설)\n" \
              "진분수는 분자가 분모보다 작은 분수이므로 {S}는 $$수식$${A}$$/수식$$보다 작은 수이어야 합니다.\n\n"


    S = ["☆", "★", "○", "●", "◇", "◆", "□", "■"][np.random.randint(0, 8)]

    A = np.random.randint(5, 21)

    while (1):
        a = np.random.randint(1, A)
        b = np.random.randint(1, A)
        c = np.random.randint(1, A)
        d = np.random.randint(1, A)
        e = np.random.randint(A, A + 5)
        if (1 <= a) and (a < b) and (b < c) and (c < d) and (d <= A - 1):
            break

    N = [a, b, c, d, e]
    np.random.shuffle(N)
    AA, BB, CC, DD, EE = N

    if (AA == e):
        ANS = "①"
    elif (BB == e):
        ANS = "②"
    elif (CC == e):
        ANS = "③"
    elif (DD == e):
        ANS = "④"
    elif (EE == e):
        ANS = "⑤"

    lg = "{"
    rg = "}"


    stem = stem.format(S=S, A=A, AA=AA, BB=BB, CC=CC, DD=DD, EE=EE, lg=lg, rg=rg)
    answer = answer.format(ANS=ANS)
    comment = comment.format(S=S, A=A)

    return stem, answer, comment














































# 3-2-4-35
def fraction324_Stem_022():
    stem = "진분수는 모두 몇 개인가요?\n$$표$$ $$수식$${a} over {A}$$/수식$$  $$수식$${b} over {B}$$/수식$$  $$수식$${c} over {C}$$/수식$$  $$수식$${d} over {D}$$/수식$$\n \n$$수식$${e} over {E}$$/수식$$  $$수식$${f} over {F}$$/수식$$  $$수식$${g} over {G}$$/수식$$  $$수식$${h} over {H}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${Y}$$/수식$$개\n"
    comment = "(해설)\n" \
              "진분수를 모두 찾으면 {X}으로 $$수식$${Y}$$/수식$$개입니다.\n\n"


    while (1):
        A = np.random.randint(3, 16)
        B = np.random.randint(3, 16)
        C = np.random.randint(3, 16)
        D = np.random.randint(3, 16)
        E = np.random.randint(3, 16)
        F = np.random.randint(3, 16)
        G = np.random.randint(3, 16)
        H = np.random.randint(3, 16)

        a = np.random.randint(1, A + 4)
        c = np.random.randint(1, C + 4)
        d = np.random.randint(1, D + 4)
        e = np.random.randint(1, E + 4)
        f = np.random.randint(1, F + 4)
        h = np.random.randint(1, H + 4)

        b = np.random.randint(1, B)
        g = np.random.randint(G, G + 6)
        if (a != b != c != d != e != f != g != h and A != B != C != D != E != F != G != H):
            break

    AA = "$$수식$${%s} over {%s}$$/수식$$" % (a, A)
    BB = "$$수식$${%s} over {%s}$$/수식$$" % (b, B)
    CC = "$$수식$${%s} over {%s}$$/수식$$" % (c, C)
    DD = "$$수식$${%s} over {%s}$$/수식$$" % (d, D)
    EE = "$$수식$${%s} over {%s}$$/수식$$" % (e, E)
    FF = "$$수식$${%s} over {%s}$$/수식$$" % (f, F)
    GG = "$$수식$${%s} over {%s}$$/수식$$" % (g, G)
    HH = "$$수식$${%s} over {%s}$$/수식$$" % (h, H)

    count = 8
    if (a >= A):
        AA = ""
        count = count - 1
    if (b >= B):
        BB = ""
        count = count - 1
    if (c >= C):
        CC = ""
        count = count - 1
    if (d >= D):
        DD = ""
        count = count - 1
    if (e >= E):
        EE = ""
        count = count - 1
    if (f >= F):
        FF = ""
        count = count - 1
    if (g >= G):
        GG = ""
        count = count - 1
    if (h >= H):
        HH = ""
        count = count - 1

    # X = "{%s}``{%s}``{%s}``{%s}``{%s}``{%s}``{%s}``{%s}" % (AA, BB, CC, DD, EE, FF, GG, HH)
    Y = count

    finding = ""
    temp_list = [AA, BB, CC, DD, EE, FF, GG, HH]

    for idx in temp_list:
        if (idx != "") and finding == "":
            finding += str(idx)
        elif idx != "":
            finding = finding + ", " + str(idx)


    stem = stem.format(a=a, A=A, b=b, B=B, c=c, C=C, d=d, D=D, e=e, E=E, f=f, F=F, g=g, G=G, h=h, H=H)
    answer = answer.format(Y=Y)
    comment = comment.format(X=finding, Y=Y)

    return stem, answer, comment
















































# 3-2-4-36
def fraction324_Stem_023():
    stem = "자연수 $$수식$$1$$/수식$$을 분모가 $$수식$${A}$$/수식$$인 분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${A} over {A}$$/수식$$\n"
    comment = "(해설)\n" \
              "자연수 $$수식$$1$$/수식$$은 분모와 분자가 같은 분수로 나타내면 됩니다.\n" \
              "따라서 자연수 $$수식$$1$$/수식$$을 분모가 $$수식$${A}$$/수식$$인 분수로 나타내면 $$수식$${A} over {A}$$/수식$$입니다.\n\n"


    A = np.random.randint(3, 21)

    stem = stem.format(A=A)
    answer = answer.format(A=A)
    comment = comment.format(A=A)

    return stem, answer, comment














































# 3-2-4-37
def fraction324_Stem_024():
    stem = "분모가 $$수식$${A}$$/수식$$ 인 진분수를 모두 써 보세요.\n"
    answer = "(정답)\n{X2}\n"
    comment = "(해설)\n" \
              "분모가 $$수식$${A}$$/수식$$인 진분수는 분자가 $$수식$${A}$$/수식$$보다 작습니다.\n" \
              "따라서 분모가 $$수식$${A}$$/수식$$인 진분수는 {X2}입니다.\n\n"


    A = np.random.randint(3, 11)
    a = np.random.randint(1, A)

    X = []

    for i in range(1, A):
        X.append("$$수식$${%s} over {%s}$$/수식$$" % (i, A))

    X2 = ', '.join(X)


    stem = stem.format(A=A)
    answer = answer.format(X2=X2)
    comment = comment.format(A=A, X2=X2)

    return stem, answer, comment











































# 3-2-4-38
def fraction324_Stem_025():
    stem = "분모와 분자의 합이 $$수식$${D}$$/수식$$이고, 가분수를 찾아 써 보세요.\n$$표$$ $$수식$${E}$$/수식$$  $$수식$${F}$$/수식$$  $$수식$${G}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${b} over {B}$$/수식$$\n"
    comment = "(해설)\n" \
              "분모가 분자의 합이 $$수식$${D}$$/수식$$인 분수는 $$수식$${a} over {A}$$/수식$$, $$수식$${b} over {B}$$/수식$$입니다.\n" \
              "이 중에서 가분수는 $$수식$${b} over {B}$$/수식$$입니다.$$/수식$$\n\n"


    while (1):
        D = np.random.randint(11, 30)
        A = np.random.randint(math.trunc(D / 2) + 1, D)
        a = D - A
        B = np.random.randint(2, math.trunc(D / 2) + 1)
        b = D - B
        E = D - 2
        C = np.random.randint(2, math.trunc(E / 2) + 1)
        c = E - C
        if (b > B):
            break

    E = "{%s} over {%s}" % (a, A)
    F = "{%s} over {%s}" % (b, B)
    G = "{%s} over {%s}" % (c, C)

    N = [E, F, G]
    np.random.shuffle(N)
    E, F, G = N


    stem = stem.format(D=D, E=E, F=F, G=G)
    answer = answer.format(b=b, B=B)
    comment = comment.format(D=D, A=A, B=B, a=a, b=b)

    return stem, answer, comment














































# 3-2-4-39
def fraction324_Stem_026():
    stem = "가분수는 진분수보다 몇 개 더 많은지 구해 보세요.\n$$표$$ $$수식$${P}$$/수식$$, $$수식$${Q}$$/수식$$, $$수식$${R}$$/수식$$, $$수식$${S}$$/수식$$, $$수식$${T}$$/수식$$, $$수식$${U}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${X}$$/수식$$개\n"
    comment = "(해설)\n" \
              "가분수는 {p}으로 $$수식$${m}$$/수식$$개입니다.\n" \
              "진분수는 {q}으로 $$수식$${n}$$/수식$$개입니다.\n" \
              "따라서 가분수는 진분수보다 $$수식$${X}$$/수식$$개 더 많습니다.\n\n"


    term = np.random.randint(0, 2)
    if (term == 0):
        m = 4
        n = 2
    else:
        m = 5
        n = 1

    X = m - n

    while (1):
        A = np.random.randint(3, 15)
        B = np.random.randint(3, 15)
        C = np.random.randint(3, 15)
        D = np.random.randint(3, 15)
        E = np.random.randint(3, 15)

        F = np.random.randint(3, 15)
        G = np.random.randint(3, 15)
        H = np.random.randint(3, 15)

        a = np.random.randint(A, A + 6)
        b = np.random.randint(B, B + 6)
        c = np.random.randint(C, C + 6)
        d = np.random.randint(E, E + 6)
        e = np.random.randint(E, E + 6)

        f = np.random.randint(1, F)
        g = np.random.randint(1, G)
        h = np.random.randint(1, H)

        if (A != B and a != b):
            if (A != C and a != c):
                if (A != D and a != d):
                    if (A != E and a != e):
                        if (B != C and b != c):
                            if (B != D and b != d):
                                if (B != E and b != e):
                                    if (C != D and c != d):
                                        if (C != E and c != e):
                                            if (D != E and d != e):
                                                if (f != g and F != G):
                                                    if (g != h and G != H):
                                                        if (h != f and H != F):
                                                            break


    if (term == 0):
        x1 = "$$수식$${%s} over {%s}$$/수식$$" % (a, A)
        x2 = "$$수식$${%s} over {%s}$$/수식$$" % (b, B)
        x3 = "$$수식$${%s} over {%s}$$/수식$$" % (c, C)
        x4 = "$$수식$${%s} over {%s}$$/수식$$" % (d, D)
        x5 = "$$수식$${%s} over {%s}$$/수식$$" % (e, E)
        y1 = "$$수식$${%s} over {%s}$$/수식$$" % (f, F)
        y2 = "$$수식$${%s} over {%s}$$/수식$$" % (g, G)
        y3 = "$$수식$${%s} over {%s}$$/수식$$" % (h, H)

        xx = [x1, x2, x3, x4, x5]
        xxx = random.sample(xx, 4)
        yy = [y1, y2, y3]
        yyy = random.sample(yy, 2)

        I, J, K, L = xxx
        M, O = yyy
        p = xxx
        p = ', '.join(p)
        q = yyy
        q = ', '.join(q)

    else:
        x1 = "$$수식$${%s} over {%s}$$/수식$$" % (a, A)
        x2 = "$$수식$${%s} over {%s}$$/수식$$" % (b, B)
        x3 = "$$수식$${%s} over {%s}$$/수식$$" % (c, C)
        x4 = "$$수식$${%s} over {%s}$$/수식$$" % (d, D)
        x5 = "$$수식$${%s} over {%s}$$/수식$$" % (e, E)
        y1 = "$$수식$${%s} over {%s}$$/수식$$" % (f, F)
        y2 = "$$수식$${%s} over {%s}$$/수식$$" % (g, G)
        y3 = "$$수식$${%s} over {%s}$$/수식$$" % (h, H)

        xx = [x1, x2, x3, x4, x5]
        yy = [y1, y2, y3]
        yyy = random.sample(yy, 1)

        I, J, K, L, M = xx
        O = yyy
        O = ''.join(O)
        p = xx
        p = ', '.join(p)
        q = yyy
        q = ', '.join(q)

    W3 = [I, J, K, L, M, O]
    np.random.shuffle(W3)
    P, Q, R, S, T, U = W3

    # X2 = ','.join(X)


    stem = stem.format(P=P, Q=Q, R=R, S=S, T=T, U=U)
    answer = answer.format(X=X)
    comment = comment.format(p=p, q=q, m=m, n=n, X=X)

    return stem, answer, comment












































# 3-2-4-40
def fraction324_Stem_027():
    stem = "다음을 모두 만족하는 분수는 어느 것인가요?\n$$표$$∙ 가분수입니다.\n∙ 분모와 분자의 차는 $$수식$${m}$$/수식$$입니다.\n∙ 분모와 분자의 합은 $$수식$${n}$$/수식$$입니다.$$/표$$\n① $$수식$${s1}$$/수식$$\n② $$수식$${s2}$$/수식$$\n③ $$수식$${s3}$$/수식$$\n④ $$수식$${s4}$$/수식$$\n⑤ $$수식$${s5}$$/수식$$\n"
    answer = "(정답)\n{X}\n"
    comment = "(해설)\n" \
              "∙ 가분수 : {T1}, {T2}, {T3}\n" \
              "∙ 분모와 분자의 차는 $$수식$${m}$$/수식$$ : {T4}, {T5}, {T6}\n" \
              "∙ 분모와 분자의 합은 $$수식$${n}$$/수식$$ : {T7}, {T8}, {T9}, {T10}\n" \
              "따라서 모두 만족하는 것은 {X}입니다.\n\n"


    while (1):
        m = np.random.randint(5, 11)
        if ((m % 2) == 0):
            while (1):
                n = np.random.randint(15, 29)
                if ((n % 2) == 0):
                    break
        else:
            while (1):
                n = np.random.randint(15, 29)
                if ((n % 2) == 1):
                    break

        A = (n - m) / 2
        a = (m + n) / 2
        B = np.random.randint(2, 8)
        b = B + m
        c = np.random.randint(1, 8)
        C = n - c
        d = (n - m) / 2
        D = (m + n) / 2
        E = np.random.randint(2, 8)
        e = n - E

        if (B != A):
            if (b != (n - B)):
                if (E != A and E != B):
                    if (e != (E + m)):
                        if (c != d):
                            if (C != (c + m)):
                                break


    s1 = "{%g} over {%g}" % (a, A)
    s2 = "{%g} over {%g}" % (b, B)
    s3 = "{%g} over {%g}" % (c, C)
    s4 = "{%g} over {%g}" % (d, D)
    s5 = "{%g} over {%g}" % (e, E)

    s6 = s1
    s7 = s2
    s8 = s3
    s9 = s4
    s10 = s5

    candidates = [s1, s2, s3, s4, s5]
    np.random.shuffle(candidates)
    s1, s2, s3, s4, s5 = candidates

    correct_idx = 0
    for i, t in enumerate(candidates):
        if t == s6:
            correct_idx = i
            break

    TT1 = []

    if (s1 == s6 or s1 == s7 or s1 == s10):
        TT1.append("①")
    if (s2 == s6 or s2 == s7 or s2 == s10):
        TT1.append("②")
    if (s3 == s6 or s3 == s7 or s3 == s10):
        TT1.append("③")
    if (s4 == s6 or s4 == s7 or s4 == s10):
        TT1.append("④")
    if (s5 == s6 or s5 == s7 or s5 == s10):
        TT1.append("⑤")

    T1, T2, T3 = TT1

    TT2 = []

    if (s1 == s6 or s1 == s7 or s1 == s9):
        TT2.append("①")
    if (s2 == s6 or s2 == s7 or s2 == s9):
        TT2.append("②")
    if (s3 == s6 or s3 == s7 or s3 == s9):
        TT2.append("③")
    if (s4 == s6 or s4 == s7 or s4 == s9):
        TT2.append("④")
    if (s5 == s6 or s5 == s7 or s5 == s9):
        TT2.append("⑤")

    T4, T5, T6 = TT2

    TT3 = []

    if (s1 == s6 or s1 == s8 or s1 == s9 or s1 == s10):
        TT3.append("①")
    if (s2 == s6 or s2 == s8 or s2 == s9 or s2 == s10):
        TT3.append("②")
    if (s3 == s6 or s3 == s8 or s3 == s9 or s3 == s10):
        TT3.append("③")
    if (s4 == s6 or s4 == s8 or s4 == s9 or s4 == s10):
        TT3.append("④")
    if (s5 == s6 or s5 == s8 or s5 == s9 or s5 == s10):
        TT3.append("⑤")

    T7, T8, T9, T10 = TT3


    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, m=m, n=n)
    answer = answer.format(X=answer_dict[correct_idx])
    comment = comment.format(T1=T1, T2=T2, T3=T3, T4=T4, T5=T5, T6=T6, T7=T7, T8=T8, T9=T9, T10=T10,
                             X=answer_dict[correct_idx], m=m, n=n)

    return stem, answer, comment








































# 3-2-4-41
def fraction324_Stem_028():
    stem = "분모가 $$수식$${A}$$/수식$$인 진분수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${B}$$/수식$$개\n"
    comment = "(해설)\n" \
              "분모가 $$수식$${A}$$/수식$$인 진분수는 분자가 $$수식$${A}$$/수식$$보다 작습니다.\n" \
              "따라서 분모가 $$수식$${A}$$/수식$$인 진분수는 {X2}이므로$$/수식$$\n모두 $$수식$${B}$$/수식$$개입니다.\n\n"


    A = np.random.randint(5, 16)
    a = np.random.randint(1, A)

    B = A - 1

    X = []
    for i in range(1, A):
        X.append("$$수식$${%s} over {%s}$$/수식$$" % (i, A))

    X2 = ', '.join(X)


    stem = stem.format(A=A)
    answer = answer.format(B=B)
    comment = comment.format(A=A, X2=X2, B=B)

    return stem, answer, comment












































# 3-2-4-42
def fraction324_Stem_029():
    stem = "분모가 $$수식$${A}$$/수식$$인 가분수 중 분자가 가장 작은 수를 써 보세요.\n"
    answer = "(정답)\n$$수식$${A} over {A}$$/수식$$\n"
    comment = "(해설)\n" \
              "분모가 $$수식$${A}$$/수식$$인 가분수는 분자가 $$수식$${A}$$/수식$${j1} 같거나 $$수식$${A}$$/수식$$보다 커야 하므로 분자가 가장 작은 경우는 $$수식$${A}$$/수식$$입니다.\n" \
              "따라서 분모가 $$수식$${A}$$/수식$$인 가분수 중 분자가 가장 작은 수는 $$수식$${A} over {A}$$/수식$$입니다.\n\n"


    A = np.random.randint(10, 21)

    j1 = proc_jo(A, 2)

    stem = stem.format(A=A)
    answer = answer.format(A=A)
    comment = comment.format(A=A, j1=j1)

    return stem, answer, comment











































# 3-2-4-44
def fraction324_Stem_030():
    stem = "대분수는 가분수로, 가분수는 대분수로 나타내어 보세요.\n$$수식$$LEFT ( 1 RIGHT ) ```` {a3} ` {a2} over {a1}$$/수식$$\n$$수식$$LEFT ( 2 RIGHT ) ```` {B} over {b1}$$/수식$$\n"
    answer = "(정답)\n$$수식$${A} over {a1}$$/수식$$, $$수식$${b3} ` {b2} over {b1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1 RIGHT ) ```` {a3} ` {a2} over {a1}$$/수식$$ → $$수식$${a3}$$/수식$${j1} $$수식$${a2} over {a1}$$/수식$$ → $$수식$${a4} over {a1}$$/수식$${j2} " \
              "$$수식$${a2} over {a1}$$/수식$$ → $$수식$${A} over {a1}$$/수식$$\n" \
              "$$수식$$LEFT ( 2 RIGHT ) ```` {B} over {b1}$$/수식$$ → $$수식$${b4} over {b1}$$/수식$${j3} $$수식$${b2} over {b1}$$/수식$$ → $$수식$${b3}$$/수식$${j4} " \
              "$$수식$${b2} over {b1}$$/수식$$ → $$수식$${b3} ` {b2} over {b1}$$/수식$$\n\n"


    while (1):
        a1 = np.random.randint(2, 11)
        a2 = np.random.randint(1, a1)
        a3 = np.random.randint(1, 6)

        a4 = a3 * a1
        A = a4 + a2

        b1 = np.random.randint(2, 11)
        b2 = np.random.randint(1, b1)
        b3 = np.random.randint(1, 6)

        b4 = b3 * b1
        B = b4 + b2

        if (b1 != a1):
            break


    j1 = proc_jo(a3, 2)
    j2 = proc_jo(a4, 2)

    j3 = proc_jo(b4, 2)
    j4 = proc_jo(b3, 2)


    stem = stem.format(a1=a1, a2=a2, a3=a3, B=B, b1=b1)
    answer = answer.format(A=A, a1=a1, b3=b3, b2=b2, b1=b1)
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, A=A, B=B, b1=b1, b2=b2, b3=b3, b4=b4, j1=j1, j2=j2, j3=j3,
                             j4=j4)

    return stem, answer, comment









































# 3-2-4-45
def fraction324_Stem_031():
    stem = "$$수식$${a3} ` {a2} over {a1}$$/수식$${j1} $$수식$$1 over {a1}$$/수식$$이 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${A}$$/수식$$개\n"
    comment = "(해설)\n" \
              "자연수 $$수식$${a3}$$/수식$${j2} $$수식$${a4} over {a1}$$/수식$${j3} 나타내면 $$수식$${a3} ` {a2} over {a1}$$/수식$${j1} " \
              "$$수식$$1 over {a1}$$/수식$$이 $$수식$${A}$$/수식$$개입니다.\n\n"


    a1 = np.random.randint(5, 11)
    a2 = np.random.randint(1, a1)
    a3 = np.random.randint(1, 6)

    a4 = a3 * a1
    A = a4 + a2

    j1 = proc_jo(a2, -1)
    j2 = proc_jo(a3, 1)

    if (str(a4))[-1] == "3" or (str(a4))[-1] == "6" or (str(a4))[-1] == "0":
        j3 = "으로"
    else:
        j3 = "로"


    stem = stem.format(a1=a1, a2=a2, a3=a3, j1=j1)
    answer = answer.format(A=A)
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, A=A, j1=j1, j2=j2, j3=j3)

    return stem, answer, comment













































# 3-2-4-46
def fraction324_Stem_032():
    stem = "대분수는 모두 몇 개인가요?\n$$표$$ {P}, {Q}, {R}, {S}, {T} $$/표$$\n"
    answer = "(정답)\n$$수식$${n}$$/수식$$개\n"
    comment = "(해설)\n" \
              "대분수는 자연수와 진분수로 이루어진 분수입니다.\n" \
              "따라서 대분수를 찾으면 {p}으로 $$수식$${n}$$/수식$$개입니다.\n\n"


    n = np.random.randint(1, 4)

    while (1):

        a1 = np.random.randint(2, 11)
        a2 = np.random.randint(1, a1)
        a3 = np.random.randint(1, 6)

        b1 = np.random.randint(2, 11)
        b2 = np.random.randint(1, b1)
        b3 = np.random.randint(1, 6)

        c1 = np.random.randint(2, 11)
        c2 = np.random.randint(1, c1)
        c3 = np.random.randint(1, 6)

        d1 = np.random.randint(3, 13)
        d2 = np.random.randint(1, d1)

        e1 = np.random.randint(3, 13)
        e2 = np.random.randint(e1, e1 + 4)

        f1 = np.random.randint(3, 13)
        f2 = np.random.randint(1, f1 + 4)

        g1 = np.random.randint(3, 13)
        g2 = np.random.randint(1, g1 + 4)

        if (b1 != a1 and b3 != a3):
            if (c1 != a1 and c1 != b1 and c3 != a3 and c3 != b3):
                if (e1 != d1):
                    if (f1 != d1 and f1 != e1):
                        if (g1 != d1 and g1 != e1 and g1 != f1):
                            break

    if (n == 1):
        x1 = "$$수식$${%s} ` {%s} over {%s}$$/수식$$" % (a3, a2, a1)
        x2 = "$$수식$${%s} ` {%s} over {%s}$$/수식$$" % (b3, b2, b1)
        x3 = "$$수식$${%s} ` {%s} over {%s}$$/수식$$" % (c3, c2, c1)
        y1 = "$$수식$${%s} over {%s}$$/수식$$" % (d2, d1)
        y2 = "$$수식$${%s} over {%s}$$/수식$$" % (e2, e1)
        y3 = "$$수식$${%s} over {%s}$$/수식$$" % (f2, f1)
        y4 = "$$수식$${%s} over {%s}$$/수식$$" % (g2, g1)

        xx = [x1, x2, x3]
        xxx = random.sample(xx, 1)
        yy = [y1, y2, y3, y4]
        yyy = random.sample(yy, 4)

        A = xxx
        A = ''.join(A)
        B, C, D, E = yyy

        p = xxx
        p = ''.join(p)

    elif (n == 2):
        x1 = "$$수식$${%s} ` {%s} over {%s}$$/수식$$" % (a3, a2, a1)
        x2 = "$$수식$${%s} ` {%s} over {%s}$$/수식$$" % (b3, b2, b1)
        x3 = "$$수식$${%s} ` {%s} over {%s}$$/수식$$" % (c3, c2, c1)
        y1 = "$$수식$${%s} over {%s}$$/수식$$" % (d2, d1)
        y2 = "$$수식$${%s} over {%s}$$/수식$$" % (e2, e1)
        y3 = "$$수식$${%s} over {%s}$$/수식$$" % (f2, f1)
        y4 = "$$수식$${%s} over {%s}$$/수식$$" % (g2, g1)

        xx = [x1, x2, x3]
        xxx = random.sample(xx, 2)
        yy = [y1, y2, y3, y4]
        yyy = random.sample(yy, 3)

        A, B = xxx
        C, D, E = yyy
        p = xxx
        p = ', '.join(p)

    else:
        x1 = "$$수식$${%s} ` {%s} over {%s}$$/수식$$" % (a3, a2, a1)
        x2 = "$$수식$${%s} ` {%s} over {%s}$$/수식$$" % (b3, b2, b1)
        x3 = "$$수식$${%s} ` {%s} over {%s}$$/수식$$" % (c3, c2, c1)
        y1 = "$$수식$${%s} over {%s}$$/수식$$" % (d2, d1)
        y2 = "$$수식$${%s} over {%s}$$/수식$$" % (e2, e1)
        y3 = "$$수식$${%s} over {%s}$$/수식$$" % (f2, f1)
        y4 = "$$수식$${%s} over {%s}$$/수식$$" % (g2, g1)

        xx = [x1, x2, x3]
        xxx = random.sample(xx, 3)
        yy = [y1, y2, y3, y4]
        yyy = random.sample(yy, 2)

        A, B, C = xxx
        D, E = yyy
        p = xxx
        p = ', '.join(p)

    W3 = [A, B, C, D, E]
    np.random.shuffle(W3)
    P, Q, R, S, T = W3


    stem = stem.format(P=P, Q=Q, R=R, S=S, T=T)
    answer = answer.format(n=n)
    comment = comment.format(p=p, n=n)

    return stem, answer, comment
















































# 3-2-4-47
def fraction324_Stem_033():
    stem = "다음 분수들을 가분수로 나타내었을 때 분자가 가장 작은 분수는 어느 것인가요?\n$$표$$ $$수식$${a3} ` {a2} over {a1}$$/수식$$   $$수식$${b3} ` {b2} over {b1}$$/수식$$   $$수식$${c3} ` {c2} over {c1}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${X}$$/수식$$\n"
    comment = "(해설)\n" \
              "∙ $$수식$${a3} ` {a2} over {a1}$$/수식$$에서 $$수식$${a3} ` = ` {a4} over {a1}$$/수식$$이므로 $$수식$${a3} ` {a2} over {a1} = {A} over {a1}$$/수식$$\n" \
              "∙ $$수식$${b3} ` {b2} over {b1}$$/수식$$에서 $$수식$${b3} ` = ` {b4} over {b1}$$/수식$$이므로 $$수식$${b3} ` {b2} over {b1} = {B} over {b1}$$/수식$$\n" \
              "∙ $$수식$${c3} ` {c2} over {c1}$$/수식$$에서 $$수식$${c3} ` = ` {c4} over {c1}$$/수식$$이므로 $$수식$${c3} ` {c2} over {c1} = {C} over {c1}$$/수식$$\n" \
              "따라서 가분수로 나타내었을 때 분자가 가장 작은 분수는 $$수식$${X}$$/수식$$ 입니다.\n\n"


    while (1):
        a1 = np.random.randint(2, 11)
        a2 = np.random.randint(1, a1)
        a3 = np.random.randint(1, 6)
        a4 = a3 * a1
        A = a4 + a2

        b1 = np.random.randint(2, 11)
        b2 = np.random.randint(1, b1)
        b3 = np.random.randint(1, 6)
        b4 = b3 * b1
        B = b4 + b2

        c1 = np.random.randint(2, 11)
        c2 = np.random.randint(1, c1)
        c3 = np.random.randint(1, 6)
        c4 = c3 * c1
        C = c4 + c2

        if (b1 != a1):
            if (b3 != a1 and b3 != ((a3 * a1 + a2 - b2) / b1)):
                if (c1 != a1 and c1 != b1):
                    if (c3 != a1 and c3 != b1):
                        if (c3 != ((a3 * a1 + a2 - c2) / c1) and c3 != ((b3 * b1 + b2 - c2) / c1)):
                            break

    if (A < B and A < C):
        X = "{%s} ` {%s} over {%s}" % (a3, a2, a1)
    elif (B < C and B < A):
        X = "{%s} ` {%s} over {%s}" % (b3, b2, b1)
    elif (C < A and C < B):
        X = "{%s} ` {%s} over {%s}" % (c3, c2, c1)


    stem = stem.format(a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, c1=c1, c2=c2, c3=c3)
    answer = answer.format(X=X)
    comment = comment.format(a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, c1=c1, c2=c2, c3=c3, a4=a4, A=A, b4=b4, B=B,
                             c4=c4, C=C, X=X)

    return stem, answer, comment















































# 3-2-4-48
def fraction324_Stem_034():
    stem = "다음이 나타내는 수를 대분수로 나타내어 보세요.\n$$표$$ $$수식$$1 over {a1}$$/수식$$이 $$수식$${A}$$/수식$$개인 수 $$/표$$\n"
    answer = "(정답)\n$$수식$${X}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$1 over {a1}$$/수식$$이 $$수식$${A}$$/수식$$개이면 $$수식$${A} over {a1}$$/수식$$입니다.\n" \
              "$$수식$${A} over {a1}$$/수식$$ → $$수식$${a4} over {a1}$$/수식$${j1} $$수식$${a2} over {a1}$$/수식$$ → $$수식$${a3}$$/수식$${j2} " \
              "$$수식$${a2} over {a1}$$/수식$$ → $$수식$${a3} ` {a2} over {a1}$$/수식$$\n\n"


    a1 = np.random.randint(2, 11)
    a2 = np.random.randint(1, a1)
    a3 = np.random.randint(1, 6)
    a4 = a3 * a1
    A = a4 + a2

    X = "{%s} ` {%s} over {%s}" % (a3, a2, a1)

    j1 = proc_jo(a4, 2)
    j2 = proc_jo(a3, 2)

    stem = stem.format(a1=a1, A=A)
    answer = answer.format(X=X)
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, A=A, j1=j1, j2=j2)

    return stem, answer, comment





















































# 3-2-4-49
def fraction324_Stem_035():
    stem = "크기가 다른 분수 하나를 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${X1}$$/수식$$   ㉡ $$수식$${X2}$$/수식$$   ㉢ $$수식$${X3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{X}\n"
    comment = "(해설)\n" \
              "$$수식$${a3} ` {a2} over {a1}$$/수식$$ → $$수식$${a3}$$/수식$${j1} $$수식$${a2} over {a1}$$/수식$$ → $$수식$${a4} over {a1}$$/수식$${j2} " \
              "$$수식$${a2} over {a1}$$/수식$$ → $$수식$${A} over {a1}$$/수식$$\n\n"


    a1 = np.random.randint(4, 11)
    a2 = np.random.randint(3, a1)
    a3 = np.random.randint(2, 6)

    a4 = a3 * a1
    A = a4 + a2
    B = a3 * a2 + a1

    X1 = "{%s} ` {%s} over {%s}" % (a3, a2, a1)
    X2 = "{%s} over {%s}" % (A, a1)
    X3 = "{%s} over {%s}" % (B, a1)

    X4 = X3

    XXX = [X1, X2, X3]
    np.random.shuffle(XXX)
    X1, X2, X3 = XXX

    if (X1 == X4):
        X = "㉠"
    elif (X2 == X4):
        X = "㉡"
    else:
        X = "㉢"

    j1 = proc_jo(a3, 2)
    j2 = proc_jo(a4, 2)


    stem = stem.format(a1=a1, a2=a2, a3=a3, A=A, B=B, X1=X1, X2=X2, X3=X3)
    answer = answer.format(X=X)
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, A=A, j1=j1, j2=j2)

    return stem, answer, comment





















































# 3-2-4-51
def fraction324_Stem_036():
    stem = "$$수식$${a3} ` {lg}□{rg} over {a1}$$/수식$$인 대분수 중 분자가 가장 큰 대분수를 가분수로 나타내 보세요.\n"
    answer = "(정답)\n$$수식$${A} over {a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a3} ` {lg}□{rg} over {a1}$$/수식$$에서 분자가 가장 큰 대분수는 $$수식$${a3} ` {a2} over {a1}$$/수식$$입니다.\n" \
              "$$수식$${a3} ` {a2} over {a1}$$/수식$$ → $$수식$${a3}$$/수식$${j1} $$수식$${a2} over {a1}$$/수식$$ → $$수식$${a4} over {a1}$$/수식$${j2} " \
              "$$수식$${a2} over {a1}$$/수식$$ → $$수식$${A} over {a1}$$/수식$$\n\n"


    a1 = np.random.randint(4, 11)
    a2 = a1 - 1
    a3 = np.random.randint(2, 8)
    a4 = a3 * a1
    A = a4 + a2

    nemo = "□"

    j1 = proc_jo(a3, 2)
    j2 = proc_jo(a4, 2)

    lg = "{"
    rg = "}"


    stem = stem.format(a1=a1, a3=a3, lg=lg, rg=rg)
    answer = answer.format(A=A, a1=a1)
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, A=A, nemo=nemo, j1=j1, j2=j2, lg=lg, rg=rg)

    return stem, answer, comment






































# 3-2-4-53
def fraction324_Stem_037():
    stem = "{P}는 {S}를 매일 $$수식$$1 over {a1}$$/수식$$컵씩 마십니다. {P}가 $$수식$${B}$$/수식$$주일 동안 매일 {S}를 마셨다면 모두 몇 컵을 마신 것인지 대분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${a3} ` {a2} over {a1}$$/수식$$컵\n"
    comment = "(해설)\n" \
              "$$수식$${B}$$/수식$$주일은 $$수식$$7 TIMES {B} ` = ` {A} LEFT ($$/수식$$일$$수식$$RIGHT )$$/수식$$이므로 $$수식$${B}$$/수식$$주일 동안 마신 {S}는 $$수식$${A} over {a1}$$/수식$$컵입니다.\n" \
              "$$수식$${A} over {a1}$$/수식$$ → $$수식$${a4} over {a1}$$/수식$${j1} $$수식$${a2} over {a1}$$/수식$$ → $$수식$${a3}$$/수식$${j2} " \
              "$$수식$${a2} over {a1}$$/수식$$ → $$수식$${a3} ` {a2} over {a1}$$/수식$$\n\n"


    P = \
        ["윤서", "지우", "정호", "현기", "재수", "영서", "은지", "연주", "주호", "혁구", "영기", "상수", "은서", "동우", "재우", "진희", "준서", "유라",
         "수미",
         "현수", "채아", "민주", "지호", "연아", "은우", "시우", "혁재", "민하"][np.random.randint(0, 28)]

    S = ["우유", "사과주스", "토마토주스", "포도주스", "딸기주스"][np.random.randint(0, 5)]

    while (1):
        B = np.random.randint(2, 7)
        A = 7 * B
        a1 = np.random.randint(4, 11)
        a3 = math.floor(A / a1)
        a4 = a3 * a1
        a2 = A - a4
        if (B != a1):
            if (a2 != 0):
                break

    j1 = proc_jo(a4, 2)
    j2 = proc_jo(a3, 2)


    stem = stem.format(a1=a1, P=P, S=S, B=B)
    answer = answer.format(a1=a1, a2=a2, a3=a3)
    comment = comment.format(B=B, A=A, a1=a1, a2=a2, a3=a3, a4=a4, S=S, j1=j1, j2=j2)

    return stem, answer, comment














































# 3-2-4-54
def fraction324_Stem_038():
    stem = "분자와 분모의 합이 $$수식$${n}$$/수식$$이고, 차가 $$수식$${m}$$/수식$$인 가분수가 있습니다. 이 가분수를 대분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${a3} ` {a2} over {a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a1} ` + ` {A} ` = ` {n}$$/수식$$, $$수식$${A} ` - ` {a1} ` = ` {m}$$/수식$$이므로 분자와 분모가 될 수 있는 두 수는 $$수식$${a1}$$/수식$$, $$수식$${A}$$/수식$$입니다.\n" \
              "가분수는 분자가 분모와 같거나 분모보다 더 크므로 $$수식$${A} over {a1}$$/수식$$입니다.\n" \
              "$$수식$${A} over {a1}$$/수식$$ → $$수식$${a4} over {a1}$$/수식$${j1} $$수식$${a2} over {a1}$$/수식$$ → $$수식$${a3}$$/수식$${j2} " \
              "$$수식$${a2} over {a1}$$/수식$$ → $$수식$${a3} ` {a2} over {a1}$$/수식$$ \n\n"


    while True:
        m = np.random.randint(5, 11)

        if ((m % 2) == 1):
            while (1):
                n = np.random.randint(15, 29)
                if ((n % 2) == 1):
                    break
        else:
            while (1):
                n = np.random.randint(15, 29)
                if ((n % 2) == 0):
                    break

        a1 = math.floor((n - m) / 2)
        A = math.floor((m + n) / 2)
        a3 = math.floor(A / a1)

        a4 = a3 * a1
        a2 = A - a4
        if a2 != 0:
            break

    j1 = proc_jo(a4, 2)
    j2 = proc_jo(a3, 2)


    stem = stem.format(n=n, m=m)
    answer = answer.format(a1=a1, a2=a2, a3=a3)
    comment = comment.format(a1=a1, n=n, A=A, m=m, a2=a2, a3=a3, a4=a4, j1=j1, j2=j2)

    return stem, answer, comment















































# 3-2-4-56
def fraction324_Stem_039():
    stem = "대분수 $$수식$${a3} ` {lg}{S1}{rg} over {a1}$$/수식$$를 가분수로 나타내면 {S2}입니다. {S2}가 될 수 있는 가분수를 모두 써보세요.\n"
    answer = "(정답)\n{Y}\n"
    comment = "(해설)\n" \
              "대분수 $$수식$${a3} ` {lg}{S1}{rg} over {a1}$$/수식$$는 자연수 $$수식$${a3}$$/수식$${j1} 진분수 $$수식$${lg}{S1}{rg} over {a1}$$/수식$$로 이루어져 있으므로 " \
              "{S1}가 될 수 있는 수는 $$수식$${a1}$$/수식$$보다 작은 수입니다.\n" \
              "따라서 $$수식$${a3} ` {S1} over {a1}$$/수식$$가 될 수 있는 대분수는 {X}이므로\n" \
              "가분수로 나타내면 {Y}입니다.\n\n"


    S1 = ["☆", "○", "◇", "□", "△"][np.random.randint(0, 5)]
    S2 = ["★", "●", "◆", "■", "▲"][np.random.randint(0, 5)]

    a1 = np.random.randint(3, 6)
    a3 = np.random.randint(2, 6)

    A = a3 * a1 + 1
    B = a3 * a1 + 2
    C = a3 * a1 + 3
    D = a3 * a1 + 4

    if (a1 == 3):
        x1 = "$$수식$${%s} ` 1 over 3$$/수식$$" % (a3)
        x2 = "$$수식$${%s} ` 2 over 3$$/수식$$" % (a3)
        X = [x1, x2]
        X = ', '.join(X)

        y1 = "$$수식$${%s} over 3$$/수식$$" % (A)
        y2 = "$$수식$${%s} over 3$$/수식$$" % (B)
        Y = [y1, y2]
        Y = ', '.join(Y)

    elif (a1 == 4):
        x1 = "$$수식$${%s} ` 1 over 4$$/수식$$" % (a3)
        x2 = "$$수식$${%s} ` 2 over 4$$/수식$$" % (a3)
        x3 = "$$수식$${%s} ` 3 over 4$$/수식$$" % (a3)

        X = [x1, x2, x3]
        X = ', '.join(X)

        y1 = "$$수식$${%s} over 4$$/수식$$" % (A)
        y2 = "$$수식$${%s} over 4$$/수식$$" % (B)
        y3 = "$$수식$${%s} over 4$$/수식$$" % (C)
        Y = [y1, y2, y3]
        Y = ', '.join(Y)

    else:
        x1 = "$$수식$${%s} ` 1 over 5$$/수식$$" % (a3)
        x2 = "$$수식$${%s} ` 2 over 5$$/수식$$" % (a3)
        x3 = "$$수식$${%s} ` 3 over 5$$/수식$$" % (a3)
        x4 = "$$수식$${%s} ` 4 over 5$$/수식$$" % (a3)

        X = [x1, x2, x3, x4]
        X = ', '.join(X)

        y1 = "$$수식$${%s} over 5$$/수식$$" % (A)
        y2 = "$$수식$${%s} over 5$$/수식$$" % (B)
        y3 = "$$수식$${%s} over 5$$/수식$$" % (C)
        y4 = "$$수식$${%s} over 5$$/수식$$" % (D)
        Y = [y1, y2, y3, y4]
        Y = ', '.join(Y)

    j1 = proc_jo(a3, 2)

    lg = "{"
    rg = "}"


    stem = stem.format(S1=S1, a1=a1, a3=a3, S2=S2, lg=lg, rg=rg)
    answer = answer.format(Y=Y)
    comment = comment.format(a3=a3, S1=S1, a1=a1, X=X, Y=Y, j1=j1, lg=lg, rg=rg)

    return stem, answer, comment










































# 3-2-4-57
def fraction324_Stem_040():
    stem = "더 큰 분수의 기호를 써 보세요.\n$$표$$ ㉠ $$수식$$1 over {a}$$/수식$$이 $$수식$${A}$$/수식$$개인 수   ㉡$$수식$${B} over {a}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{Y}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$$1 over {a}$$/수식$$이 $$수식$${A}$$/수식$$개인 수는 $$수식$${A} over {a}$$/수식$$입니다.\n" \
              "분자의 크기를 비교하면 $$수식$${A} ` {X} ` {B}$$/수식$$이므로 $$수식$${A} over {a} ` {X} ` {B} over {a}$$/수식$$입니다.\n\n"


    while (1):
        a = np.random.randint(8, 16)
        A = np.random.randint(a + 3, 2 * a)
        B = np.random.randint(a + 3, 2 * a)
        if (B != A):
            break

    if (A > B):
        X = "&gt;"
        Y = "㉠"
    else:
        X = "&lt;"
        Y = "㉡"


    stem = stem.format(a=a, A=A, B=B)
    answer = answer.format(Y=Y)
    comment = comment.format(a=a, A=A, B=B, X=X, Y=Y)

    return stem, answer, comment















































# 3-2-4-58
def fraction324_Stem_041():
    stem = "분수의 크기를 잘못 비교한 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${T1}$$/수식$$          ㉡ $$수식$${T2}$$/수식$$\n㉢ $$수식$${T3}$$/수식$$          ㉣ $$수식$${T4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{X}\n"
    comment = "(해설)\n" \
              "{X}. $$수식$${d3} ` {d2} over {d1} ` = ` {d4} over {d1}$$/수식$$이므로 $$수식$${d4} over {d1} ` &gt; ` {D} over {d1}$$/수식$$ " \
              "따라서 $$수식$${d3} ` {d2} over {d1} ` &gt; ` {D} over {d1}$$/수식$$입니다.\n\n"


    while (1):
        a1 = np.random.randint(3, 10)
        a2 = np.random.randint(1, a1)
        a3 = np.random.randint(2, 6)
        A = np.random.randint(a3 * a1 + a2 + 1, a3 * a1 + a2 + 6)

        b1 = np.random.randint(3, 10)
        b2 = np.random.randint(1, b1)
        b3 = np.random.randint(2, 6)
        B = np.random.randint(b3 * b1 + b2 + 1, b3 * b1 + b2 + 6)

        c1 = np.random.randint(3, 10)
        c2 = np.random.randint(1, c1)
        c3 = np.random.randint(2, 6)
        C = np.random.randint(c3 * c1 + c2 - 5, c3 * c1 + c2)

        d1 = np.random.randint(3, 10)
        d2 = np.random.randint(1, d1)
        d3 = np.random.randint(2, 6)
        d4 = d3 * d1 + d2
        D = np.random.randint(d3 * d1 + d2 - 5, d3 * d1 + d2)

        if (b1 != a1):
            if (b3 != a3):
                if (c1 != a1 and c1 != b1):
                    if (c3 != a3 and c3 != b3):
                        if (d1 != a1 and d1 != b1 and d1 != c1):
                            if (d3 != a3 and d3 != b3 and d3 != c3):
                                break

    T1 = "{%s} over {%s} ` &gt; ` {%s} ` {%s} over {%s}" % (A, a1, a3, a2, a1)
    T2 = "{%s} ` {%s} over {%s} ` &lt; ` {%s} over {%s}" % (b3, b2, b1, B, b1)
    T3 = "{%s} over {%s} ` &lt; ` {%s} ` {%s} over {%s}" % (C, c1, c3, c2, c1)
    T4 = "{%s} ` {%s} over {%s} ` &lt; ` {%s} over {%s}" % (d3, d2, d1, D, d1)

    T5 = T4

    TT = [T1, T2, T3, T4]
    np.random.shuffle(TT)
    T1, T2, T3, T4 = TT

    if (T1 == T5):
        X = "㉠"
    elif (T2 == T5):
        X = "㉡"
    elif (T3 == T5):
        X = "㉢"
    else:
        X = "ㄹ"


    stem = stem.format(T1=T1, T2=T2, T3=T3, T4=T4)
    answer = answer.format(X=X)
    comment = comment.format(d3=d3, d2=d2, d1=d1, d4=d4, D=D, X=X)

    return stem, answer, comment














































# 3-2-4-60
def fraction324_Stem_042():
    stem = "$$수식$${A} over {a}$$/수식$$보다 작은 분수는 모두 몇 개인가요?\n$$표$$ $$수식$${T1}$$/수식$$, $$수식$${T2}$$/수식$$, $$수식$${T3}$$/수식$$, $$수식$${T4}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${n}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${A} over {a} ` = ` {B} ` {f} over {a}$$/수식$$\n" \
              "자연수와 분모가 모두 같으므로 분자가 $$수식$${f}$$/수식$$보다 작은 수를 모두 찾아보면\n{X}{ro1} 모두 $$수식$${n}$$/수식$$개입니다.\n\n"


    n = np.random.randint(1, 4)

    while (1):
        a = np.random.randint(6, 11)
        B = np.random.randint(2, 6)
        b = np.random.randint(1, a)
        c = np.random.randint(1, a)
        d = np.random.randint(1, a)
        e = np.random.randint(1, a)
        f = np.random.randint(1, a)

        if (n == 1):
            if (1 <= b) and (b < f) and (f < c) and (c < d) and (d < e) and (e <= a - 1):
                break
        elif (n == 2):
            if (1 <= b) and (b < c) and (c < f) and (f < d) and (d < e) and (e <= a - 1):
                break
        else:
            if (1 <= b) and (b < c) and (c < d) and (d < f) and (f < e) and (e <= a - 1):
                break

    A = B * a + f

    if (n == 1):
        X = "$$수식$${%s} ` {%s} over {%s}$$/수식$$" % (B, b, a)
        ro1 = get_josa(b, "로")

    elif (n == 2):
        x1 = "$$수식$${%s} ` {%s} over {%s}$$/수식$$" % (B, b, a)
        x2 = "$$수식$${%s} ` {%s} over {%s}$$/수식$$" % (B, c, a)
        X = [x1, x2]
        X = ', '.join(X)
        ro1 = get_josa(c, "로")

    else:
        x1 = "$$수식$${%s} ` {%s} over {%s}$$/수식$$" % (B, b, a)
        x2 = "$$수식$${%s} ` {%s} over {%s}$$/수식$$" % (B, c, a)
        x3 = "$$수식$${%s} ` {%s} over {%s}$$/수식$$" % (B, d, a)
        X = [x1, x2, x3]
        X = ', '.join(X)
        ro1 = get_josa(d, "로")

    T1 = "{%s} ` {%s} over {%s}" % (B, b, a)
    T2 = "{%s} ` {%s} over {%s}" % (B, c, a)
    T3 = "{%s} ` {%s} over {%s}" % (B, d, a)
    T4 = "{%s} ` {%s} over {%s}" % (B, e, a)

    TT = [T1, T2, T3, T4]
    np.random.shuffle(TT)
    T1, T2, T3, T4 = TT


    stem = stem.format(T1=T1, T2=T2, T3=T3, T4=T4, a=a, A=A)
    answer = answer.format(n=n)
    comment = comment.format(A=A, a=a, B=B, c=c, f=f, X=X, n=n, ro1=ro1)

    return stem, answer, comment
















































# 3-2-4-61
def fraction324_Stem_043():
    stem = "크기가 작은 분수부터 차례대로 기호를 찾아 써 보세요.\n$$표$$ ㉠ $$수식$${y1}$$/수식$$  ㉡ $$수식$${y2}$$/수식$$  ㉢ $$수식$${y3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{X}\n"
    comment = "(해설)\n" \
              "대분수를 가분수로 나타낸 후 크기를 비교합니다.\n" \
              "$$수식$${c} ` {b} over {a} ` = ` {C} over {a}$$/수식$$이므로 $$수식$${F} ` &lt; ` {E} ` &lt; ` {D}$$/수식$$입니다.\n\n"


    while True:
        while (1):
            a = np.random.randint(5, 10)
            b = np.random.randint(1, a)
            c = np.random.randint(2, 6)

            C = c * a + b
            A = np.random.randint(C - 3, C + 4)
            B = np.random.randint(C - 3, C + 4)
            if ((15 / a) <= c) and (c <= (30 / a)):
                if (A != C):
                    if (B != C and A != B):
                        break

        T1 = [A, "{%s} over {%s}" % (A, a)]
        T2 = [B, "{%s} over {%s}" % (B, a)]
        T3 = [C, "{%s} ` {%s} over {%s}" % (c, b, a)]

        TT = [T1, T2, T3]
        np.random.shuffle(TT)
        abc1, abc2, abc3 = TT

        D = ""
        E = ""
        F = ""
        X = ""

        if abc1[0] > abc2[0]:
            if abc2[0] > abc3[0]:
                D = abc1[1]
                E = abc2[1]
                F = abc3[1]
                X = "㉢, ㉡, ㉠"
            elif (abc1[0] > abc3[0]) and (abc3[0] > abc2[0]):
                D = abc1[1]
                E = abc3[1]
                F = abc2[1]
                X = "㉡, ㉢, ㉠"

        elif abc2[0] > abc1[0]:
            if abc1[0] > abc3[0]:
                D = abc2[1]
                E = abc1[1]
                F = abc3[1]
                X = "㉢, ㉠, ㉡"
            elif (abc2[0] > abc3[0]) and (abc3[0] > abc1[0]):
                D = abc2[1]
                E = abc3[1]
                F = abc1[1]
                X = "㉠, ㉢, ㉡"

        elif abc3[0] > abc1[0]:
            if abc1[0] > abc2[0]:
                D = abc3[1]
                E = abc1[1]
                F = abc2[1]
                X = "㉡, ㉠, ㉢"
            elif (abc3[0] > abc2[0]) and (abc2[0] > abc1[0]):
                D = abc3[1]
                E = abc2[1]
                F = abc1[1]
                X = "㉠, ㉡, ㉢"

        if (D != "") and (E != "") and (F != "") and (X != ""):
            break


    stem = stem.format(y1=abc1[1], y2=abc2[1], y3=abc3[1])
    answer = answer.format(X=X)
    comment = comment.format(a=a, b=b, c=c, C=C, D=D, E=E, F=F)

    return stem, answer, comment












































# 3-2-4-63
def fraction324_Stem_044():
    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 자연수 중에서 □ 안에 들어갈 수 있는 수를 모두 구해보세요.\n$$표$$ $$수식$${A} over {a} ` &gt;$$/수식$$□$$수식$${d} over {a}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{X}\n"
    comment = "(해설)\n" \
              "$$수식$${A} over {a} ` = ` {c} ` {b} over {a}$$/수식$$이므로 $$수식$${c} ` {b} over {a} ` &gt;$$/수식$$□$$수식$${d} over {a}$$/수식$$에서 " \
              "□ 안에 들어갈 수 있는 수는 $$수식$${c}$$/수식$$보다 작은 수입니다.\n" \
              "따라서 □ 안에 들어갈 수 있는 수는 {X}입니다.\n\n"


    a = np.random.randint(5, 8)
    b = np.random.randint(1, a - 1)
    c = np.random.randint(3, 8)

    A = c * a + b
    d = np.random.randint(b + 1, a)

    X = list(range(1, c))
    # X = ', '.join(map(str, X))

    tempX = []

    for idx in X:
        temp = "$$수식$$%d$$/수식$$" % idx
        tempX.append(temp)

    X = ', '.join(map(str, tempX))


    stem = stem.format(A=A, a=a, d=d)
    answer = answer.format(X=X)
    comment = comment.format(A=A, a=a, c=c, b=b, d=d, X=X)

    return stem, answer, comment













































# 3-2-4-64
def fraction324_Stem_045():
    stem = "조건을 모두 만족하는 분수는 모두 몇 개인가요?\n$$표$$∙분모가 $$수식$${a}$$/수식$$인 가분수입니다.\n∙$$수식$${c}`{b} over {a}$$/수식$$보다 작습니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${n}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${c} ` {b} over {a} ` = ` {A} over {a}$$/수식$$이므로 분모가 $$수식$${a}$$/수식$$인 가분수 중 " \
              "$$수식$${A} over {a}$$/수식$$보다 작은 분수는\n{X}로 모두 $$수식$${n}$$/수식$$개입니다.\n\n"


    a = np.random.randint(5, 10)
    b = np.random.randint(1, a - 1)
    c = 1

    A = c * a + b
    B = np.random.randint(a, A)
    n = A - a

    X = []
    for i in range(a, A):
        X.append("$$수식$${%s} over {%s}$$/수식$$" % (i, a))

    X = ', '.join(X)


    stem = stem.format(A=A, a=a, b=b, c=c)
    answer = answer.format(n=n)
    comment = comment.format(c=c, b=b, a=a, A=A, X=X, n=n)

    return stem, answer, comment














