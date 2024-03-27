import numpy as np
import random
import statistics
from math import gcd




















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







def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp

    return abs(a)





#약수 구하는 함수
def factor(number):
    f = []
    for i in range(1, number + 1):
        if (number % i == 0):
            f.append(i)

    return f





def lcm(x,y):
    return x*y//gcd(x,y)





def soroso(a, b):
    while True:
        rest_ab = max(a, b) % min(a, b)
        a = min(a, b)
        b = rest_ab
        if rest_ab == 0 or rest_ab == 1:
            break

    return rest_ab





def two_digits(a):
    if a >= 10 and a < 100:
        return 1

    else:
        return 0



def get_yaksu(a):
    temp_list = []

    for idx in range(a+1):
        if idx == 0:
            pass
        else:
            if a % idx == 0:
                temp_list.append(idx)

    return temp_list




def get_gcd(a, b):
    if a < b:
        (a, b) = (b, a)

    while b != 0:
        (a, b) = (b, a % b)

    return a




def get_lcm(a, b):
    c = get_gcd(a, b)
    d = (a * b) / c
    e = int(d)

    return e




def show_int(a):
    if a - (a // 1) == 0:
        a = int(a)

    return a





def get_josa(a, b):
    if b == "과" or b == "와":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "와"
        else:
            return "과"

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

    elif b == "이" or b == "가":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "가"
        else:
            return "이"

    elif b == "을" or b == "를":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "를"
        else:
            return "을"

    elif b == "라면" or b == "이라면":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "라면"
        else:
            return "이라면"








#6-2-4-01
def proandpro624_Stem_001():
    stem = "다음 중 전항이 $$수식$${A}$$/수식$$인 비는 어느 것인가요?\n① {q1}  ② {q2}  ③ {q3}\n④ {q4}  ⑤ {q5}\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n"\
              "① {uq1}  ② {uq2}  ③ {uq3}  ④ {uq4}  ⑤ {uq5}\n"\
              "따라서 전항이 $$수식$${A}$$/수식$$인 비는 {a1}입니다.\n\n"


    while True:
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        A = random.choice(num)
        B = random.choice(num)
        D = random.choice(num)
        F = random.choice(num)
        H = random.choice(num)
        J = random.choice(num)

        num.remove(A)
        num2 = num
        C = random.choice(num2)
        E = random.choice(num2)
        G = random.choice(num2)
        I = random.choice(num2)

        if (gcd(A, B) == 1 and gcd(C, D) == 1 and gcd(E, F) == 1 and gcd(G, H) == 1 and gcd(I, J) == 1):
            t1, t2, t3, t4, t5 = (A, B), (C, D), (E, F), (G, H), (I, J)
            if (t1 != t2 and t1 != t3 and t1 != t4 and t1 != t5 and t2 != t3 and t2 != t4 and t2 != t5 and t3 != t4 and t3 != t5 and t4 != t5):
                break

    qq1 = "$$수식$$%d$$/수식$$:$$수식$$%d$$/수식$$" % (A, B)
    qq2 = "$$수식$$%d$$/수식$$:$$수식$$%d$$/수식$$" % (C, D)
    qq3 = "$$수식$$%d$$/수식$$:$$수식$$%d$$/수식$$" % (E, F)
    qq4 = "$$수식$$%d$$/수식$$:$$수식$$%d$$/수식$$" % (G, H)
    qq5 = "$$수식$$%d$$/수식$$:$$수식$$%d$$/수식$$" % (I, J)

    uqq1 = "$$수식$$under{%d}$$/수식$$:$$수식$$%d$$/수식$$" % (A, B)
    uqq2 = "$$수식$$under{%d}$$/수식$$:$$수식$$%d$$/수식$$" % (C, D)
    uqq3 = "$$수식$$under{%d}$$/수식$$:$$수식$$%d$$/수식$$" % (E, F)
    uqq4 = "$$수식$$under{%d}$$/수식$$:$$수식$$%d$$/수식$$" % (G, H)
    uqq5 = "$$수식$$under{%d}$$/수식$$:$$수식$$%d$$/수식$$" % (I, J)

    # candidates = [qq1, qq2, qq3, qq4, qq5]
    # np.random.shuffle(candidates)
    # q1, q2, q3, q4, q5 = candidates
    #
    # correct_idx = 0
    #
    # for i, c in enumerate(candidates):
    #     if c == qq1:
    #         correct_idx = i
    #         break

    candidates = [[qq1, uqq1], [qq2, uqq2], [qq3, uqq3], [qq4, uqq4], [qq5, uqq5]]
    np.random.shuffle(candidates)
    setq1, setq2, setq3, setq4, setq5 = candidates

    correct_idx = 0

    for idx, cdx in enumerate(candidates):
        if cdx == [qq1, uqq1]:
            correct_idx = idx
            break


    # stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, A=A)
    # answer = answer.format(a1=answer_dict[correct_idx])
    # comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, a1=answer_dict[correct_idx], A=A)
    stem = stem.format(q1=setq1[0], q2=setq2[0], q3=setq3[0], q4=setq4[0], q5=setq5[0], A=A)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(uq1=setq1[1], uq2=setq2[1], uq3=setq3[1], uq4=setq4[1], uq5=setq5[1], a1=answer_dict[correct_idx], A=A)


    return stem, answer, comment



























#6-2-4-02
def proandpro624_Stem_002():
    stem = "다음 중 후항이 다른 하나를 찾아 기호를 써 보세요.\n$$표$$㉠ {q1} ㉡ {q2} ㉢ {q3} $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n"\
              "후항은 기호 ':' 뒤에 있는 수이므로 비에서 후항을 각각 찾아보면\n"\
              "㉠ {q11}  ㉡ {q22}  ㉢ {q33}\n"\
              "따라서 후항이 다른 하나는 {a1}입니다.\n\n"


    while True:
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        B = random.choice(num)
        A = random.choice(num)
        D = random.choice(num)
        num.remove(A)
        C = random.choice(num)
        num.append(A)
        num.remove(B)
        E = random.choice(num)

        if (gcd(A, B) == 1 and gcd(B, C) == 1 and gcd(D, E) == 1):
            break

    qq1 = "$$수식$$%d$$/수식$$:$$수식$$%d$$/수식$$" % (A, B)
    qq2 = "$$수식$$%d$$/수식$$:$$수식$$%d$$/수식$$" % (C, B)
    qq3 = "$$수식$$%d$$/수식$$:$$수식$$%d$$/수식$$" % (D, E)

    candidates = [qq1, qq2, qq3]
    np.random.shuffle(candidates)
    q1, q2, q3 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == qq3:
            correct_idx = i
            break

    a = ["㉠", "㉡", "㉢"]
    a1 = a[correct_idx]

    qq = [B, B, B]
    qq[correct_idx] = E
    q11 = qq[0]
    q22 = qq[1]
    q33 = qq[2]


    stem = stem.format(q1=q1, q2=q2, q3=q3)
    answer = answer.format(a1=a1)
    comment = comment.format(q11=q11, q22=q22, q33=q33, a1=a1)

    return stem, answer, comment

























#6-2-4-03
def proandpro624_Stem_003():
    stem = "다음 중 후항이 가장 큰 비의 비율을 소수로 나타내어 보세요.\n$$표$${q1}  {q2}  {q3}  {q4} $$/표$$\n"
    answer = "(정답)\n$$수식$${I}$$/수식$$\n"
    comment = "(해설)\n" \
              "비의 후항이 각각 $$수식$${c1}$$/수식$$, $$수식$${c2}$$/수식$$, $$수식$${c3}$$/수식$$, $$수식$${c4}$$/수식$$이므로\n" \
              "후항이 가장 큰 비는 {aa1}입니다.\n" \
              "따라서 {aa1}의 비율은 $$수식$${A} over {B} ` = ` {I} $$/수식$$입니다.\n\n"


    while True:
        A = np.random.randint(1, 30)
        C = np.random.randint(1, 30)
        E = np.random.randint(1, 30)
        G = np.random.randint(1, 30)
        B = random.choice([5, 10, 20])
        D = np.random.randint(1, 30)
        F = np.random.randint(1, 30)
        H = np.random.randint(1, 30)

        I = round(A / B, 6)

        if gcd(A, B) == 1 and gcd(C, D) == 1 and gcd(E, F) == 1 and gcd(G, H) == 1 and B > D and B > F and B > H:
            t1, t2, t3, t4 = (A, B), (C, D), (E, F), (G, H)
            if t1 != t2 and t1 != t3 and t1 != t4 and t2 != t3 and t2 != t4 and t3 != t4:
                if I - (I // 1) != 0:
                    break


    qq1 = "$$수식$$%d$$/수식$$:$$수식$$%d$$/수식$$" % (A, B)
    qq2 = "$$수식$$%d$$/수식$$:$$수식$$%d$$/수식$$" % (C, D)
    qq3 = "$$수식$$%d$$/수식$$:$$수식$$%d$$/수식$$" % (E, F)
    qq4 = "$$수식$$%d$$/수식$$:$$수식$$%d$$/수식$$" % (G, H)

    cc1 = "$$수식$$%d$$/수식$$" % (B)
    cc2 = "$$수식$$%d$$/수식$$" % (D)
    cc3 = "$$수식$$%d$$/수식$$" % (F)
    cc4 = "$$수식$$%d$$/수식$$" % (H)

    q = [qq1, qq2, qq3, qq4]
    c = [cc1, cc2, cc3, cc4]
    a = random.sample([0, 1, 2, 3], 4)
    a1, a2, a3, a4 = a[0], a[1], a[2], a[3]
    q1, q2, q3, q4 = q[a1], q[a2], q[a3], q[a4]
    c1, c2, c3, c4 = c[a1], c[a2], c[a3], c[a4]

    aa1 = qq1


    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4)
    answer = answer.format(I=I)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, aa1=aa1, A=A, B=B, I=I)

    return stem, answer, comment






























#6-2-4-04
def proandpro624_Stem_004():
    stem = "$$수식$${A} : {B} $$/수식$${gwa1} 비율이 다른 비를 찾아 기호를 써 보세요.\n$$표$$㉠ {Q2}  ㉡ {Q3}\n㉢ {Q4}  ㉣ {Q5} $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "$$수식$${A} : {B} $$/수식$${nun1} 전항과 후항을 각각 " \
              "$$수식$${time1}$$/수식$${ro1} 나눈 $$수식$${ap1} : {di1}$$/수식$$, " \
              "$$수식$${time2}$$/수식$${ro2} 나눈 $$수식$${ap2} : {di2}$$/수식$$, " \
              "$$수식$${time3}$$/수식$${ro3} 나눈 $$수식$${ap3} : {di3}$$/수식$${gwa2} 비율이 같습니다.\n" \
              "따라서 $$수식$${A} : {B} $$/수식$$ 과 비율이 다른 비는 $$수식$${ap4} : {di4}$$/수식$$ 입니다.\n\n"



    while True:
        A = np.random.randint(10, 100)
        B = np.random.randint(10, 100)

        A_yaksu_list = get_yaksu(A)
        B_yaksu_list = get_yaksu(B)

        ab_gcd = get_gcd(A, B)
        ab_gcd_yaksu_list = get_yaksu(ab_gcd)

        if A == B or len(ab_gcd_yaksu_list) < 4:
            continue

        while True:
            [a, b, c] = random.sample(ab_gcd_yaksu_list, 3)
            if 1 not in [a, b, c]:
                temp_list = [a, b, c]
                temp_list.sort()
                [a, b, c] = temp_list
                break

        C = int(A / a)
        D = int(B / a)

        E = int(A / b)
        F = int(B / b)

        G = int(A / c)
        H = int(B / c)

        if two_digits(C) * two_digits(D) * two_digits(E) * two_digits(F) * two_digits(G) * two_digits(H) != 1:
            continue

        while True:
            times_list = [a, b, c]
            ij_times = random.sample(times_list, 1)

            I = np.random.randint(2, 20)
            J = np.random.randint(2, 20)

            if I != J and I not in A_yaksu_list and J not in B_yaksu_list:
                I = I * ij_times[0]
                J = J * ij_times[0]

                if two_digits(I) * two_digits(J) == 1:
                    break

        break


    q2 = ["$$수식$$%d : %d $$/수식$$" % (C, D), a, C, D]
    q3 = ["$$수식$$%d : %d $$/수식$$" % (E, F), b, E, F]
    q4 = ["$$수식$$%d : %d $$/수식$$" % (G, H), c, G, H]
    q5 = ["$$수식$$%d : %d $$/수식$$" % (I, J), I, J]

    qq = [q2, q3, q4, q5]
    random.shuffle(qq)
    Q2, Q3, Q4, Q5 = qq[0][0], qq[1][0], qq[2][0], qq[3][0]

    if (Q2 == q5[0]):
        a1 = "㉠"
        time1 = qq[1][1]
        ap1 = qq[1][2]
        di1 = qq[1][3]
        time2 = qq[2][1]
        ap2 = qq[2][2]
        di2 = qq[2][3]
        time3 = qq[3][1]
        ap3 = qq[3][2]
        di3 = qq[3][3]
        ap4 = qq[0][1]
        di4 = qq[0][2]

    elif (Q3 == q5[0]):
        a1 = "㉡"
        time1 = qq[0][1]
        ap1 = qq[0][2]
        di1 = qq[0][3]
        time2 = qq[2][1]
        ap2 = qq[2][2]
        di2 = qq[2][3]
        time3 = qq[3][1]
        ap3 = qq[3][2]
        di3 = qq[3][3]
        ap4 = qq[1][1]
        di4 = qq[1][2]

    elif (Q4 == q5[0]):
        a1 = "㉢"
        time1 = qq[0][1]
        ap1 = qq[0][2]
        di1 = qq[0][3]
        time2 = qq[1][1]
        ap2 = qq[1][2]
        di2 = qq[1][3]
        time3 = qq[3][1]
        ap3 = qq[3][2]
        di3 = qq[3][3]
        ap4 = qq[2][1]
        di4 = qq[2][2]

    else:
        a1 = "㉣"
        time1 = qq[0][1]
        ap1 = qq[0][2]
        di1 = qq[0][3]
        time2 = qq[1][1]
        ap2 = qq[1][2]
        di2 = qq[1][3]
        time3 = qq[2][1]
        ap3 = qq[2][2]
        di3 = qq[2][3]
        ap4 = qq[3][1]
        di4 = qq[3][2]


    gwa1 = get_josa(B, "과")
    nun1 = get_josa(B, "는")
    ro1 = get_josa(time1, "로")
    ro2 = get_josa(time2, "로")
    ro3 = get_josa(time3, "로")
    gwa2 = get_josa(di3, "과")



    stem = stem.format(A=A, B=B, Q2=Q2, Q3=Q3, Q4=Q4, Q5=Q5, gwa1=gwa1)
    answer = answer.format(a1=a1)
    comment = comment.format(A=A, B=B, time1=time1, time2=time2, time3=time3, ap1=ap1, di1=di1, ap2=ap2, di2=di2,
                             ap3=ap3, di3=di3, ap4=ap4, di4=di4, nun1=nun1, ro1=ro1, ro2=ro2, ro3=ro3, gwa2=gwa2,
                             gwa1=gwa1)

    return stem, answer, comment




























#6-2-4-05
def proandpro624_Stem_005():
    stem = "두 비의 비율이 같을 때 ㉠에 알맞은 수를 구해 보세요.\n$$수식$${boxone}$$/수식$$   $$수식$${boxtwo}$$/수식$$\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$\n"
    comment = "(해설)\n" \
              "두 비의 비율이 같고 $$수식$${A}$$/수식$$:$$수식$${B}$$/수식$$ 후항에 $$수식$${k}$$/수식$${rur1} 곱하면 " \
              "$$수식$${C}$$/수식$${ga1} 되므로 전항에 $$수식$${k}$$/수식$${rur1} 곱하면 ㉠이 됩니다.\n" \
              "→ ㉠ $$수식$$ = {A} ` TIMES ` {k} ` = {D}$$/수식$$\n\n"


    while True:
        A = np.random.randint(1, 21)
        B = np.random.randint(1, 21)
        if A != B:
            break

    k = np.random.randint(2, 6)
    C = B * k
    D = A * k

    boxone = "%d : %d" % (A, B)
    boxtwo = "%s : %d" % ("㉠", C)

    rur1 = get_josa(k, "를")
    ga1 = get_josa(C, "가")


    stem = stem.format(boxtwo=boxtwo, boxone=boxone)
    answer = answer.format(D=D)
    comment = comment.format(A=A, B=B, C=C, D=D, k=k, rur1=rur1, ga1=ga1)

    return stem, answer, comment























#6-2-4-07
def proandpro624_Stem_006():
    stem = "비의 성질을 이용하여 비율이 같은 비를 만들려고 합니다. □ 안에 공통으로 들어갈 수 없는 수는 무엇인가요?\n$$표$$$$수식$${A}$$/수식$$:$$수식$${B}$$/수식$$ → $$수식$$LEFT ( {A} ` TIMES □ RIGHT ) $$/수식$$:$$수식$$LEFT ( {B} ` TIMES □ RIGHT ) $$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$$0$$/수식$$\n"
    comment = "(해설)\n"\
              "비의 전항과 후항에 $$수식$$0$$/수식$$이 아닌 같은 수를 곱해야 하므로 $$수식$$0$$/수식$$은 들어갈 수 없습니다.\n\n"


    while True:
        A = np.random.randint(1, 100)
        B = np.random.randint(1, 100)
        if A != B:
            break


    stem = stem.format(A=A, B=B)

    return stem, answer, comment






















#6-2-4-09
def proandpro624_Stem_007():
    stem = "다음 중 비율이 같은 비를 만드는 과정이 옳은 것을 모두 골라 보세요.\n① {Q1}\n② {Q2}\n③ {Q3}\n④ {Q4}\n⑤ {Q5}\n"
    answer = "(정답)\n{a1}, {a2}\n"
    comment = "(해설)\n"\
              "① {Q1}\n{A1}\n② {Q2}\n{A2}\n③ {Q3}\n{A3}\n④ {Q4}\n{A4}\n⑤ {Q5}\n{A5}\n"\
              "따라서 비율이 같은 비를 만드는 과정이 옳은 것은 {a1}, {a2}입니다.\n\n"



    a = np.random.randint(2, 10)
    b = np.random.randint(2, 10)

    temp_list1 = [2, 3, 4, 5, 6, 7, 8, 9]

    [c, c_cp1, c_cp2, d, d_cp1, d_cp2] = random.sample(temp_list1, 6)
    [e, e_cp1, e_cp2, f, f_cp1, f_cp2] = random.sample(temp_list1, 6)

    g = np.random.randint(2, 10)
    h = np.random.randint(2, 10)
    i = np.random.randint(2, 10)
    j = np.random.randint(2, 10)

    g_cp1 = np.random.randint(2, 10)
    h_cp1 = np.random.randint(2, 10)
    i_cp1 = np.random.randint(2, 10)
    j_cp1 = np.random.randint(2, 10)

    g_cp2 = np.random.randint(2, 10)
    h_cp2 = np.random.randint(2, 10)
    i_cp2 = np.random.randint(2, 10)
    j_cp2 = np.random.randint(2, 10)


    temp_list2 = []
    for idx in range(1, 100):
        temp_list2.append(idx)

    [A, B] = random.sample(temp_list2, 2)

    [E, F, E_cp1, F_cp1, E_cp2, F_cp2] = random.sample(temp_list2, 6)
    [G, H, G_cp1, H_cp1, G_cp2, H_cp2] = random.sample(temp_list2, 6)


    while True:
        C = b * (np.random.randint(2, 51))
        D = b * (np.random.randint(2, 51))

        if C != D and C < 100 and D < 100:
            break


    while True:
        I = e * (np.random.randint(2, 51))
        I_cp1 = e_cp1 * (np.random.randint(2, 51))
        I_cp2 = e_cp2 * (np.random.randint(2, 51))

        J = e * (np.random.randint(2, 51))
        J_cp1 = f_cp1 * (np.random.randint(2, 51))
        J_cp2 = f_cp2 * (np.random.randint(2, 51))

        if I != J and I_cp1 != J_cp1 and I_cp2 != J_cp2:
            if I < 100 and I_cp1 < 100 and I_cp2 < 100:
                if J < 100 and J_cp1 < 100 and J_cp2 < 100:
                    break

    while True:
        L = h * (np.random.randint(2, 51))
        L_cp1 = h_cp1 * (np.random.randint(2, 51))
        L_cp2 = h_cp2 * (np.random.randint(2, 51))

        K = np.random.randint(1, 100)
        K_cp1 = np.random.randint(1, 100)
        K_cp2 = np.random.randint(1, 100)

        if L != K and L_cp1 != K_cp1 and L_cp2 != K_cp2:
            if L < 100 and L_cp1 < 100 and L_cp2 < 100:
                break

    while True:
        M = i * (np.random.randint(2, 51))
        M_cp1 = i_cp1 * (np.random.randint(2, 51))
        M_cp2 = i_cp2 * (np.random.randint(2, 51))

        N = np.random.randint(1, 100)
        N_cp1 = np.random.randint(1, 100)
        N_cp2 = np.random.randint(1, 100)

        if M != N and M_cp1 != N_cp1 and M_cp2 != N_cp2:
            if M < 100 and M_cp1 < 100 and M_cp2 < 100:
                break



    q1 = "$$수식$$%d : %d $$/수식$$    →    $$수식$$LEFT ( %d TIMES %d RIGHT ):LEFT ( %d TIMES %d RIGHT )$$/수식$$" % (
    A, B, A, a, B, a)
    q2 = "$$수식$$%d : %d $$/수식$$    →    $$수식$$LEFT ( %d div %d RIGHT ):LEFT ( %d div %d RIGHT )$$/수식$$" % (
    C, D, C, b, D, b)

    q3 = "$$수식$$%d : %d $$/수식$$    →    $$수식$$LEFT ( %d TIMES %d RIGHT ):LEFT ( %d TIMES %d RIGHT )$$/수식$$" % (
    E, F, E, 0, F, 0)
    q4 = "$$수식$$%d : %d $$/수식$$    →    $$수식$$LEFT ( %d TIMES %d RIGHT ):LEFT ( %d TIMES %d RIGHT )$$/수식$$" % (
    G, H, G, c, H, d)
    q5 = "$$수식$$%d : %d $$/수식$$    →    $$수식$$LEFT ( %d div %d RIGHT ):LEFT ( %d div %d RIGHT )$$/수식$$" % (
    I, J, I, e, J, f)
    q6 = "$$수식$$%d : %d $$/수식$$    →    $$수식$$LEFT ( %d TIMES %d RIGHT ):LEFT ( %d div %d RIGHT )$$/수식$$" % (
    K, L, K, g, L, h)
    q7 = "$$수식$$%d : %d $$/수식$$    →    $$수식$$LEFT ( %d div %d RIGHT ):LEFT ( %d TIMES %d RIGHT )$$/수식$$" % (
    M, N, M, i, N, j)

    q3_cp1 = "$$수식$$%d : %d $$/수식$$    →    $$수식$$LEFT ( %d TIMES %d RIGHT ):LEFT ( %d TIMES %d RIGHT )$$/수식$$" % (
        E_cp1, F_cp1, E_cp1, 0, F_cp1, 0)
    q4_cp1 = "$$수식$$%d : %d $$/수식$$    →    $$수식$$LEFT ( %d TIMES %d RIGHT ):LEFT ( %d TIMES %d RIGHT )$$/수식$$" % (
        G_cp1, H_cp1, G_cp1, c_cp1, H_cp1, d_cp1)
    q5_cp1 = "$$수식$$%d : %d $$/수식$$    →    $$수식$$LEFT ( %d div %d RIGHT ):LEFT ( %d div %d RIGHT )$$/수식$$" % (
        I_cp1, J_cp1, I_cp1, e_cp1, J_cp1, f_cp1)
    q6_cp1 = "$$수식$$%d : %d $$/수식$$    →    $$수식$$LEFT ( %d TIMES %d RIGHT ):LEFT ( %d div %d RIGHT )$$/수식$$" % (
        K_cp1, L_cp1, K_cp1, g_cp1, L_cp1, h_cp1)
    q7_cp1 = "$$수식$$%d : %d $$/수식$$    →    $$수식$$LEFT ( %d div %d RIGHT ):LEFT ( %d TIMES %d RIGHT )$$/수식$$" % (
        M_cp1, N_cp1, M_cp1, i_cp1, N_cp1, j_cp1)

    q3_cp2 = "$$수식$$%d : %d $$/수식$$    →    $$수식$$LEFT ( %d TIMES %d RIGHT ):LEFT ( %d TIMES %d RIGHT )$$/수식$$" % (
        E_cp2, F_cp2, E_cp2, 0, F_cp2, 0)
    q4_cp2 = "$$수식$$%d : %d $$/수식$$    →    $$수식$$LEFT ( %d TIMES %d RIGHT ):LEFT ( %d TIMES %d RIGHT )$$/수식$$" % (
        G_cp2, H_cp2, G_cp2, c_cp2, H_cp2, d_cp2)
    q5_cp2 = "$$수식$$%d : %d $$/수식$$    →    $$수식$$LEFT ( %d div %d RIGHT ):LEFT ( %d div %d RIGHT )$$/수식$$" % (
        I_cp2, J_cp2, I_cp2, e_cp2, J_cp2, f_cp2)
    q6_cp2 = "$$수식$$%d : %d $$/수식$$    →    $$수식$$LEFT ( %d TIMES %d RIGHT ):LEFT ( %d div %d RIGHT )$$/수식$$" % (
        K_cp2, L_cp2, K_cp2, g_cp2, L_cp2, h_cp2)
    q7_cp2 = "$$수식$$%d : %d $$/수식$$    →    $$수식$$LEFT ( %d div %d RIGHT ):LEFT ( %d TIMES %d RIGHT )$$/수식$$" % (
        M_cp2, N_cp2, M_cp2, i_cp2, N_cp2, j_cp2)


    rur1 = get_josa(a, "를")
    ro1 = get_josa(b, "로")

    rur2 = get_josa(c, "를")
    rur3 = get_josa(d, "를")

    ro2 = get_josa(e, "로")
    ro3 = get_josa(f, "로")

    rur4 = get_josa(g, "를")
    ro4 = get_josa(h, "로")

    ro5 = get_josa(i, "로")
    rur5 = get_josa(j, "를")

    rur2_cp1 = get_josa(c_cp1, "를")
    rur3_cp1 = get_josa(d_cp1, "를")

    ro2_cp1 = get_josa(e_cp1, "로")
    ro3_cp1 = get_josa(f_cp1, "로")

    rur4_cp1 = get_josa(g_cp1, "를")
    ro4_cp1 = get_josa(h_cp1, "로")

    ro5_cp1 = get_josa(i_cp1, "로")
    rur5_cp1 = get_josa(j_cp1, "를")

    rur2_cp2 = get_josa(c_cp2, "를")
    rur3_cp2 = get_josa(d_cp2, "를")

    ro2_cp2 = get_josa(e_cp2, "로")
    ro3_cp2 = get_josa(f_cp2, "로")

    rur4_cp2 = get_josa(g_cp2, "를")
    ro4_cp2 = get_josa(h_cp2, "로")

    ro5_cp2 = get_josa(i_cp2, "로")
    rur5_cp2 = get_josa(j_cp2, "를")



    a1 = "비의 항과 후항에 같은 수 $$수식$$%d$$/수식$$%s 곱하였으므로 옳습니다." % (a, rur1)
    a2 = "비의 전항과 후항에 같은 수 $$수식$$%d$$/수식$$%s 나누었으므로 옳습니다." % (b, ro1)

    a3 = "비의 전항과 후항에 $$수식$$%d$$/수식$$을 곱하였으므로 옳지 않습니다." % (0)
    a4 = "비의 전항에는 $$수식$$%d$$/수식$$%s 곱하고 후항에는 $$수식$$%d$$/수식$$%s 곱하였으므로 옳지 않습니다." % (c, rur2, d, rur3)
    a5 = "비의 전항은 $$수식$$%d$$/수식$$%s 나누고 후항은 $$수식$$%d$$/수식$$%s 나누었으므로 옳지 않습니다." % (e, ro2, f, ro3)
    a6 = "비의 전항에는 $$수식$$%d$$/수식$$%s 곱하고 후항은 $$수식$$%d$$/수식$$%s 나누었으므로 옳지 않습니다." % (g, rur4, h, ro4)
    a7 = "비의 전항은 $$수식$$%d$$/수식$$%s 나누고 후항에는 $$수식$$%d$$/수식$$%s 곱하였으므로 옳지 않습니다." % (i, ro5, j, rur5)

    a3_cp1 = "비의 전항과 후항에 $$수식$$%d$$/수식$$을 곱하였으므로 옳지 않습니다." % (0)
    a4_cp1 = "비의 전항에는 $$수식$$%d$$/수식$$%s 곱하고 후항에는 $$수식$$%d$$/수식$$%s 곱하였으므로 옳지 않습니다." % (c_cp1, rur2_cp1, d_cp1, rur3_cp1)
    a5_cp1 = "비의 전항은 $$수식$$%d$$/수식$$%s 나누고 후항은 $$수식$$%d$$/수식$$%s 나누었으므로 옳지 않습니다." % (e_cp1, ro2_cp1, f_cp1, ro3_cp1)
    a6_cp1 = "비의 전항에는 $$수식$$%d$$/수식$$%s 곱하고 후항은 $$수식$$%d$$/수식$$%s 나누었으므로 옳지 않습니다." % (g_cp1, rur4_cp1, h_cp1, ro4_cp1)
    a7_cp1 = "비의 전항은 $$수식$$%d$$/수식$$%s 나누고 후항에는 $$수식$$%d$$/수식$$%s 곱하였으므로 옳지 않습니다." % (i_cp1, ro5_cp1, j_cp1, rur5_cp1)

    a3_cp2 = "비의 전항과 후항에 $$수식$$%d$$/수식$$을 곱하였으므로 옳지 않습니다." % (0)
    a4_cp2 = "비의 전항에는 $$수식$$%d$$/수식$$%s 곱하고 후항에는 $$수식$$%d$$/수식$$%s 곱하였으므로 옳지 않습니다." % (c_cp2, rur2_cp2, d_cp2, rur3_cp2)
    a5_cp2 = "비의 전항은 $$수식$$%d$$/수식$$%s 나누고 후항은 $$수식$$%d$$/수식$$%s 나누었으므로 옳지 않습니다." % (e_cp2, ro2_cp2, f_cp2, ro3_cp2)
    a6_cp2 = "비의 전항에는 $$수식$$%d$$/수식$$%s 곱하고 후항은 $$수식$$%d$$/수식$$%s 나누었으므로 옳지 않습니다." % (g_cp2, rur4_cp2, h_cp2, ro4_cp2)
    a7_cp2 = "비의 전항은 $$수식$$%d$$/수식$$%s 나누고 후항에는 $$수식$$%d$$/수식$$%s 곱하였으므로 옳지 않습니다." % (i_cp2, ro5_cp2, j_cp2, rur5_cp2)

    # nq = [0, 1, 2, 3, 4]
    # n = random.sample(nq, 3)
    # NQ = [q3, q4, q5, q6, q7]
    # NA = [a3, a4, a5, a6, a7]
    # nq1, nq2, nq3 = NQ[n[0]], NQ[n[1]], NQ[n[2]]
    # na1, na2, na3 = NA[n[0]], NA[n[1]], NA[n[2]]

    nq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    n = random.sample(nq, 3)
    NQ = [q3, q4, q5, q6, q7, q3_cp1, q4_cp1, q5_cp1, q6_cp1, q7_cp1, q3_cp2, q4_cp2, q5_cp2, q6_cp2, q7_cp2]
    NA = [a3, a4, a5, a6, a7, a3_cp1, a4_cp1, a5_cp1, a6_cp1, a7_cp1, a3_cp2, a4_cp2, a5_cp2, a6_cp2, a7_cp2]

    nq1, nq2, nq3 = NQ[n[0]], NQ[n[1]], NQ[n[2]]
    na1, na2, na3 = NA[n[0]], NA[n[1]], NA[n[2]]


    Q = [q1, q2, nq1, nq2, nq3]
    A = [a1, a2, na1, na2, na3]
    q = [0, 1, 2, 3, 4]
    random.shuffle(q)
    Q1, Q2, Q3, Q4, Q5 = Q[q[0]], Q[q[1]], Q[q[2]], Q[q[3]], Q[q[4]]
    A1, A2, A3, A4, A5 = A[q[0]], A[q[1]], A[q[2]], A[q[3]], A[q[4]]

    aa1 = q.index(0)
    aa2 = q.index(1)

    if (aa1 > aa2):
        a1 = answer_dict[aa2]
        a2 = answer_dict[aa1]
    else:
        a1 = answer_dict[aa1]
        a2 = answer_dict[aa2]



    stem = stem.format(Q1=Q1, Q2=Q2, Q3=Q3, Q4=Q4, Q5=Q5)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(Q1=Q1, Q2=Q2, Q3=Q3, Q4=Q4, Q5=Q5, A1=A1, A2=A2, A3=A3, A4=A4, A5=A5,
                             a1=a1, a2=a2)

    return stem, answer, comment































#6-2-4-11
def proandpro624_Stem_008():
    stem = "어떤 비의 후항은 $$수식$${A}$$/수식$$이고 전항은 후항보다 $$수식$${k}$$/수식$$ 더 큽니다. 어떤 비를 구해 보세요.\n$$수식$${boxone}$$/수식$$ : $$수식$${boxtwo}$$/수식$$\n"
    answer = "(정답)\n$$수식$${B}$$/수식$$, $$수식$${A}$$/수식$$\n"
    comment = "(해설)\n"\
              "$$수식$$LEFT ($$/수식$$전항$$수식$$RIGHT ) ` = ` LEFT ($$/수식$$후항$$수식$$RIGHT ) ` + ` {k} ` = ` {A} ` + ` {k} ` = ` {B} $$/수식$$\n"\
              "전항이 $$수식$${B}$$/수식$$, 후항이 $$수식$${A}$$/수식$$인 비이므로 $$수식$${B}$$/수식$$ : $$수식$${A}$$/수식$$입니다.\n\n"


    while True:
        A = np.random.randint(1, 100)
        B = np.random.randint(1, 100)

        if B > A and gcd(A, B) == 1:
            break

    k = B - A
    boxone = "box{㉠````````````````````}"
    boxtwo = "box{㉡````````````````````}"


    stem = stem.format(A=A, k=k, boxone=boxone, boxtwo=boxtwo)
    answer = answer.format(B=B, A=A)
    comment = comment.format(A=A, B=B, k=k)

    return stem, answer, comment































#6-2-4-12
def proandpro624_Stem_009():
    stem = "전항이 $$수식$${A}$$/수식$$이고 비율이 $$수식$${B} over {C}$$/수식$$인 비가 있습니다. 이 비의 후항은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$\n"
    comment = "(해설)\n"\
              "후항을 □라고 하면\n"\
              "$$수식$${A}$$/수식$$ : □ → $$수식$${A} over {lg}□{rg}  ` = ` {B} over {C} ` = ` {bk} over {ck}  ` = ` {A} over {D}$$/수식$$,\n" \
              "□ $$수식$$` = ` {D}$$/수식$$\n" \
              "따라서 후항은 $$수식$${D}$$/수식$$입니다.\n\n"


    while True:
        B = np.random.randint(1, 20)
        C = np.random.randint(1, 20)

        if B < C and gcd(B, C) == 1:
            break

    k = np.random.randint(2, 10)
    A = B * k
    D = C * k

    blank = "□"
    bk = "{%d TIMES %d}" % (B, k)
    ck = "{%d TIMES %d}" % (C, k)

    lg = "{"
    rg = "}"


    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(D=D)
    comment = comment.format(A=A, B=B, C=C, D=D, blank=blank, bk=bk, ck=ck, lg=lg, rg=rg)

    return stem, answer, comment































#6-2-4-13
def proandpro624_Stem_010():
    stem = "비의 비율이 모두 같도록 비의 성질을 이용하여 ㉠과 ㉡에 알맞은 수를 각각 구해 순서대로 쓰세요.\n$$표$$$$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$$        ㉠ : $$수식$${C}$$/수식$$        $$수식$${D}$$/수식$$ : ㉡ $$/표$$\n"
    answer = "(정답)\n㉠ $$수식$${E}$$/수식$$, ㉡ $$수식$${F}$$/수식$$\n"
    comment = "(해설)\n"\
              "$$수식$${B} TIMES {k} ` = ` {C}$$/수식$$이므로 $$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$$의 전항과 후항에 "\
              "$$수식$${k}$$/수식$${rur1} 곱하면 $$수식$${E}$$/수식$$ : $$수식$${C}$$/수식$${ga1} 됩니다.\n"\
              "→ ㉠ $$수식$$ ` = ` {E}$$/수식$$\n" \
              "$$수식$${A} TIMES {l} ` = ` {D}$$/수식$$이므로 $$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$$의 전항과 후항에 " \
              "$$수식$${l}$$/수식$${rur2} 곱하면 $$수식$${D}$$/수식$$ : $$수식$${F}$$/수식$${ga2} 됩니다.\n" \
              "→ ㉡ $$수식$$` = ` {F}$$/수식$$\n\n"


    while True:
        A = np.random.randint(1, 21)
        B = np.random.randint(1, 21)
        if (gcd(A, B) == 1):
            break

    while True:
        k = np.random.randint(2, 10)
        l = np.random.randint(2, 10)
        if (k != l):
            break

    C = B * k
    D = A * l
    E = A * k
    F = B * l

    rur1 = get_josa(k, "를")
    rur2 = get_josa(l, "를")

    ga1 = get_josa(C, "가")
    ga2 = get_josa(F, "가")

    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(E=E, F=F)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, k=k, l=l, rur1=rur1, rur2=rur2, ga1=ga1, ga2=ga2)

    return stem, answer, comment































#6-2-4-14
def proandpro624_Stem_011():
    stem = "간단한 자연수의 비로 나타낸 것은 어느 것인가요?\n$$표$$$$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$$ $$/표$$\n① {Q1}  ② {Q2}  ③ {Q3}\n④ {Q4}  ⑤ {Q5}\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$$\n" \
              "→ $$수식$$LEFT ( {A} ` TIMES {k} RIGHT ) $$/수식$$  : $$수식$$LEFT ( {B} ` TIMES {k} RIGHT ) $$/수식$$\n" \
              "→ $$수식$${C}$$/수식$$ : $$수식$${D}$$/수식$$\n\n"

    k = 10
    while True:
        C = np.random.randint(1, 100)
        D = np.random.randint(1, 100)

        if gcd(C, D) == 1:
            break

    A, B = C / 10, D / 10
    e, f = A * 10, B * 100

    ef = [e, f]
    random.shuffle(ef)
    E, F = ef[0], ef[1]

    g, h = A * 100, B * 10
    gh = [g, h]
    random.shuffle(gh)
    G, H = gh[0], gh[1]
    I, J = B * 10, A * 10
    K, L = B * 100, A * 100

    qc = "$$수식$$%d$$/수식$$ : $$수식$$%d$$/수식$$" % (C, D)
    qe = "$$수식$$%d$$/수식$$ : $$수식$$%d$$/수식$$" % (E, F)
    qg = "$$수식$$%d$$/수식$$ : $$수식$$%d$$/수식$$" % (G, H)
    qi = "$$수식$$%d$$/수식$$ : $$수식$$%d$$/수식$$" % (I, J)
    qk = "$$수식$$%d$$/수식$$ : $$수식$$%d$$/수식$$" % (K, L)

    candidates = [qc, qe, qg, qi, qk]
    np.random.shuffle(candidates)
    Q1, Q2, Q3, Q4, Q5 = candidates

    correct_idx = 0

    for i, c in enumerate(candidates):
        if c == qc:
            correct_idx = i
            break


    stem = stem.format(A=A, B=B, Q1=Q1, Q2=Q2, Q3=Q3, Q4=Q4, Q5=Q5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(A=A, B=B, C=C, D=D, k=k)

    return stem, answer, comment


































#6-2-4-16
def proandpro624_Stem_012():
    stem = "$$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$${rur1} 간단히 자연수의 비로 나타내었더니 $$수식$${C}$$/수식$$ : $$수식$${D}$$/수식$${ga1} 되었습니다. 전항과 후항을 얼마로 나누었나요?\n"
    answer = "(정답)\n$$수식$${E}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$$의 전항과 후항을 □ 로 나누었다면\n" \
              "$$수식$${A} div $$/수식$$ □ $$수식$$` = ` {C}$$/수식$$에서 □ $$수식$$` = ` {A} div {C} ` = ` {E}$$/수식$$\n" \
              "$$수식$${B} div $$/수식$$ □ $$수식$$` = ` {D}$$/수식$$에서 □ $$수식$$` = ` {B} div {D} ` = ` {E}$$/수식$$\n" \
              "따라서 전항과 후항을 $$수식$${E}$$/수식$${ro1} 나누었습니다.\n\n"


    E = np.random.randint(2, 20)

    while True:
        C = np.random.randint(1, 20)
        D = np.random.randint(1, 20)
        if (gcd(C, D) == 1):
            break

    A = C * E
    B = D * E

    rur1 = get_josa(B, "를")
    ga1 = get_josa(D, "가")
    ro1 = get_josa(E, "로")


    stem = stem.format(A=A, B=B, C=C, D=D, rur1=rur1, ga1=ga1)
    answer = answer.format(E=E)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, ro1=ro1)

    return stem, answer, comment































#6-2-4-17
def proandpro624_Stem_013():
    stem = "{A}와 {B}의 저금액의 비는 $$수식$${C}$$/수식$$ : $$수식$${D}$$/수식$$입니다. {A}와 {B}의 저금액의 비를 가장 간단한 자연수의 비로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${E}$$/수식$$ : $$수식$${F}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${C}$$/수식$$ : $$수식$${D}$$/수식$$\n" \
              "→ $$수식$$LEFT ( {C} div {k} RIGHT ) `` $$/수식$$ : $$수식$$LEFT ( {D} div {k} RIGHT ) $$/수식$$\n" \
              "→ $$수식$${E}$$/수식$$ : $$수식$${F}$$/수식$$\n\n"


    ab = random.sample(["지훈이", "지수", "영훈이", "정수", "소연이", "수진이"], 2)
    A, B = ab[0], ab[1]

    while True:
        E = np.random.randint(1, 21)
        F = np.random.randint(1, 21)
        if (gcd(E, F) == 1):
            break

    kk = np.random.randint(1, 21)
    k = kk * 500

    C, D = E * k, F * k


    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(E=E, F=F)
    comment = comment.format(C=C, D=D, E=E, F=F, k=k)

    return stem, answer, comment
































#6-2-4-18
def proandpro624_Stem_014():
    stem = "다음 비를 간단한 자연수의 비로 나타내었을 때 비의 전항이 $$수식$${A}$$/수식$$인 것을 찾아 기호를 써 보세요.\n$$표$$㉠ {Q1}     ㉡ {Q2}     ㉢ {Q3} $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "㉠ {c1}\n" \
              "㉡ {c2}\n" \
              "㉢ {c3}\n" \
              "따라서 간단한 자연수의 비로 나타냈을 때의 비의 전항이 $$수식$${A}$$/수식$$인 것은 {a1}입니다.\n\n"


    while True:
        A = np.random.randint(1, 21)
        B = np.random.randint(1, 21)
        C = np.random.randint(1, 21)
        D = np.random.randint(1, 21)
        E = np.random.randint(1, 21)
        F = np.random.randint(1, 21)

        # if gcd(A, B) == 1 and gcd(C, D) == 1 and D != B and gcd(E, F) == 1 and F != B and A != B:
        if gcd(A, B) == 1 and gcd(C, D) == 1 and A != C and gcd(E, F) == 1 and A != E and A != B:
            break

    p = random.choice([10, 100])
    q = random.choice([10, 100])
    r = random.choice([10, 100])

    # a = A / p
    # b = B / p
    # c = C / q
    # d = D / q
    # e = E / r
    # f = F / r

    a = round(A / p, 2)
    b = round(B / p, 2)
    c = round(C / q, 2)
    d = round(D / q, 2)
    e = round(E / r, 2)
    f = round(F / r, 2)

    a = show_int(a)
    b = show_int(b)
    c = show_int(c)
    d = show_int(d)
    e = show_int(e)
    f = show_int(f)

    # qa = " $$수식$$%0.2f$$/수식$$ : $$수식$$%0.2f$$/수식$$" % (a, b)
    # qc = " $$수식$$%0.2f$$/수식$$ : $$수식$$%0.2f$$/수식$$" % (c, d)
    # qe = " $$수식$$%0.2f$$/수식$$ : $$수식$$%0.2f$$/수식$$" % (e, f)

    qa = " $$수식$$%s$$/수식$$ : $$수식$$%s$$/수식$$" % (a, b)
    qc = " $$수식$$%s$$/수식$$ : $$수식$$%s$$/수식$$" % (c, d)
    qe = " $$수식$$%s$$/수식$$ : $$수식$$%s$$/수식$$" % (e, f)

    ga1 = get_josa(B, "가")
    ga2 = get_josa(D, "가")
    ga3 = get_josa(F, "가")

    ca = "전항과 후항에 $$수식$$%d$$/수식$$을 곱하면 $$수식$$%d$$/수식$$ : $$수식$$%d$$/수식$$%s 됩니다." % (p, A, B, ga1)
    cc = "전항과 후항에 $$수식$$%d$$/수식$$을 곱하면 $$수식$$%d$$/수식$$ : $$수식$$%d$$/수식$$%s 됩니다." % (q, C, D, ga2)
    ce = "전항과 후항에 $$수식$$%d$$/수식$$을 곱하면 $$수식$$%d$$/수식$$ : $$수식$$%d$$/수식$$%s 됩니다." % (r, E, F, ga3)


    qq = [qa, qc, qe]
    ccc = [ca, cc, ce]
    num = [0, 1, 2]
    random.shuffle(num)
    Q1, Q2, Q3 = qq[num[0]], qq[num[1]], qq[num[2]]
    c1, c2, c3 = ccc[num[0]], ccc[num[1]], ccc[num[2]]

    if (Q1 == qa):
        a1 = "㉠"
    elif (Q2 == qa):
        a1 = "㉡"
    else:
        a1 = "㉢"


    stem = stem.format(Q1=Q1, Q2=Q2, Q3=Q3, A=A)
    answer = answer.format(a1=a1)
    comment = comment.format(c1=c1, c2=c2, c3=c3, A=A, a1=a1)

    return stem, answer, comment





























#6-2-4-20
def proandpro624_Stem_015():
    stem = "{A}의 인형 무게는 $$수식$${B} rm kg$$/수식$$이고, {C}의 인형 무게는 $$수식$${D} rm kg$$/수식$$입니다. {A}와 {C}의 인형 무게의 비를 가장 간단한 자연수의 비로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${E}$$/수식$$ : $$수식$${F}$$/수식$$\n"
    comment = "(해설)\n" \
              "{A}와 {C}의 인형 무게의 비는 $$수식$${B}$$/수식$$ : $$수식$${D}$$/수식$$입니다.\n" \
              "$$수식$${B}$$/수식$$ : $$수식$${D}$$/수식$$의 전항과 후항에 $$수식$${k}$$/수식$${rur1} " \
              "곱하면 $$수식$${E}$$/수식$$ : $$수식$${F}$$/수식$${ga1} 됩니다.\n\n"


    ac = random.sample(["원우", "석민이", "희영이", "민희", "슬기", "유나"], 2)

    A, C = ac[0], ac[1]

    # while True:
    #     E = np.random.randint(1, 1000)
    #     F = np.random.randint(1, 1000)
    #     kk = np.random.randint(1, 11)
    #     k = 10 * kk
    #     B = E / k
    #     D = F / k
    #
    #     if gcd(E, F) == 1:
    #         break

    while True:
        kk = np.random.randint(1, 11)
        k = 10 * kk

        B = round((np.random.randint(1, 10) + np.random.randint(1, 100) * 10) / 100, 2)
        D = round((np.random.randint(1, 10) + np.random.randint(1, 100) * 10) / 100, 2)

        E = B * k
        F = D * k

        E = show_int(E)
        F = show_int(F)

        if soroso(E, F) and E < 1000 and F < 1000:
            break


    rur1 = get_josa(k, "를")
    ga1 = get_josa(F, "가")



    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(E=E, F=F)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, k=k, rur1=rur1, ga1=ga1)

    return stem, answer, comment
































#6-2-4-22
def proandpro624_Stem_016():
    stem = "후항이 $$수식$${A}$$/수식$$인 어떤 비를 간단한 자연수의 비로 나타내었더니 $$수식$${B}$$/수식$$ : $$수식$${C}$$/수식$${ga1} 되었습니다. 어떤 비의 전항은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 비의 전항과 후항을 □ 로 나누었다면 $$수식$${A} div $$/수식$$□ $$수식$$` = ` {C}$$/수식$$에서 " \
              "□ $$수식$$` = ` {A} div {C} ` = ` {k}$$/수식$$\n" \
              "→ 전항과 후항을 $$수식$${k}$$/수식$${ro1} 나눈 것입니다.\n" \
              "어떤 비의 전항을 $$수식$${k}$$/수식$${ro1} 나눈 값이 $$수식$${B}$$/수식$$이고\n" \
              "$$수식$${D} div {k} ` = ` {B}$$/수식$$이므로 어떤 비의 전항은 $$수식$${D}$$/수식$$입니다.\n\n"


    while True:
        B = np.random.randint(1, 21)
        C = np.random.randint(1, 21)

        if gcd(B, C) == 1 and B != C:
            break


    k = np.random.randint(2, 10)
    A = C * k
    D = B * k

    ga1 = get_josa(C, "가")
    ro1 = get_josa(k, "로")


    stem = stem.format(A=A, B=B, C=C, ga1=ga1)
    answer = answer.format(D=D)
    comment = comment.format(A=A, B=B, C=C, D=D, k=k, ro1=ro1)

    return stem, answer, comment
































#6-2-4-23
def proandpro624_Stem_017():
    stem = "$$수식$${lg}□{rg} over {A}$$/수식$$ : $$수식$${B} over {C}$$/수식$${rur1} 간단한 자연수의 비로 나타내었더니 $$수식$${D}$$/수식$$ : $$수식$${E}$$/수식$${ga1} 되었습니다. □ 안에 알맞은 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${F}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${lg}□{rg} over {A}$$/수식$$ : $$수식$${B} over {C}$$/수식$$의 전항과 후항에 $$수식$${k}$$/수식$${rur2} " \
              "곱하면 $$수식$$LEFT ( {blank} TIMES {l} RIGHT )$$/수식$$ : $$수식$${E}$$/수식$${ga1} 됩니다.\n" \
              "간단한 자연수의 비로 나타낸 비의 전항이 $$수식$${D}$$/수식$$이고 □$$수식$$TIMES {l} ` = ` {D}  $$/수식$$이므로 □ $$수식$$` = ` {D} div {l} ` = ` {F}$$/수식$$입니다.\n\n"


    while True:
        B = np.random.randint(1, 21)
        F = np.random.randint(1, 21)
        A = np.random.randint(1, 21)
        C = np.random.randint(1, 21)

        k = lcm(A, C)
        l = int(k / A)
        E = int(B * k / C)
        D = int(F * k / A)

        if A > F and C > B:
            break


    # k = lcm(A, C)
    # l = int(k / A)
    # E = int(B * k / C)
    # D = int(F * k / A)
    blank = "□"

    rur1 = get_josa(B, "를")
    ga1 = get_josa(E, "가")
    rur2 = get_josa(k, "를")

    lg = "{"
    rg = "}"


    stem = stem.format(A=A, B=B, C=C, D=D, E=E, blank=blank, rur1=rur1, ga1=ga1, lg=lg, rg=rg)
    answer = answer.format(F=F)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, l=l, F=F, blank=blank, k=k, rur2=rur2, ga1=ga1, lg=lg, rg=rg)

    return stem, answer, comment






























#6-2-4-24
def proandpro624_Stem_018():
    stem = "다음 두 비를 각각 가장 간단한 자연수의 비로 나타내면 서로 같습니다. □ 안에 알맞은 기약 분수를 구해보세요.\n$$수식$${box1}$$/수식$$   $$수식$${box2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${E} over {F}$$/수식$$\n"
    comment = "(해설)\n" \
              "전항의 $$수식$${A} over {B}$$/수식$${rur1} $$수식$${G}$$/수식$${ro1} 바꾼 후\n" \
              "$$수식$${G}$$/수식$$ : $$수식$${C}$$/수식$$의 전항과 후항에 $$수식$${k}$$/수식$${rur2} 곱하면 " \
              "$$수식$${X}$$/수식$$ : $$수식$${Y}$$/수식$${ga1} 됩니다.\n" \
              "두 비를 가장 간단한 자연수의 비로 나타내면 서로 같으므로\n" \
              "$$수식$${D}$$/수식$$ : □의 전항과 후항에 같은 수를 곱하면 $$수식$${X}$$/수식$$ : $$수식$${Y}$$/수식$${ga1} 됩니다.\n" \
              "$$수식$${D} TIMES {l} ` = ` {X}$$/수식$$이므로 $$수식$${D}$$/수식$$ : □의 전항과 후항에 $$수식$${l}$$/수식$${rur3} " \
              "곱하면 $$수식$${X}$$/수식$$ : $$수식$$ LEFT ( □ TIMES {l} RIGHT )$$/수식$${ga2} 됩니다.\n" \
              "따라서 □ $$수식$$ TIMES {l} ` = ` {Y}$$/수식$$    , □ $$수식$$ = ` {Y} div {l} ` = ` {Y} over {l}  ` = ` {E} over {F}$$/수식$$입니다.\n\n"



    while True:
        B = random.choice([2, 5, 10])
        A = np.random.randint(1, 10)

        if A >= B:
            continue

        G = round(A / B, 1)
        cc = np.random.randint(1, 10)
        C = round(cc / 10, 1)

        if G == C:
            continue

        if (G * 10) % 2 == 0 and cc % 2 == 0:
            k = 5
        else:
            k = 10

        X = int(G * k)
        Y = int(C * k)

        if soroso(X, Y) == 0:
            continue

        dd = np.random.randint(1, 10)
        D = round(dd / 10, 1)

        if G == D:
            continue

        l = int(X / D)
        if l - (l // 1) != 0:
            continue

        Yl_gcd = get_gcd(Y, l)

        E = int(Y / Yl_gcd)
        F = int(l / Yl_gcd)

        if E == Y or F < E or F == 1:
            continue

        break


    box1 = "%s over %s : %s" % (A, B, C)
    box2 = "%s : □" % D

    rur1 = get_josa(A, "를")
    ro1 = get_josa(G, "로")
    rur2 = get_josa(k, "를")
    ga1 = get_josa(Y, "가")
    rur3 = get_josa(l, "를")
    ga2 = get_josa(l, "가")


    stem = stem.format(box1=box1, box2=box2)
    answer = answer.format(E=E, F=F)
    comment = comment.format(k=k, A=A, B=B, G=G, C=C, X=X, Y=Y, D=D, l=l, E=E, F=F, rur1=rur1, ro1=ro1, rur2=rur2, ga1=ga1, rur3=rur3, ga2=ga2)

    return stem, answer, comment



    # while True:
    #     B = random.choice([2, 5, 10])
    #     A = np.random.randint(1, 10)
    #     if B > A:
    #         break
    #
    # while True:
    #     G = A / B
    #     cc = np.random.randint(1, 10)
    #     dd = np.random.randint(1, 10)
    #     gg = int(G * 10)
    #     C = cc / 10
    #     D = dd / 10
    #     if G != C and G != D:
    #         break

    # if cc % 2 == 0 and gg % 2 == 0:
    #     k = 5
    # else:
    #     k = 10
    #
    # X = int(G * k)
    # Y = int(C * k)
    # l = int(X / D)
    #
    # ef = gcd(Y, l)
    # E = int(Y / ef)
    # F = int(l / ef)
































#6-2-4-26
def proandpro624_Stem_019():
    stem = "비율이 $$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$${gwa1} 같은 비를 찾아 비례식으로 나타내어 보세요.\n$$표$${Q1}   {Q2}   {Q3}$$/표$$\n"
    answer = "(정답)\n$$수식$${G}$$/수식$$ : $$수식$${H}$$/수식$$\n"
    comment = "(해설)\n" \
              "각 비의 비율을 알아봅시다.\n" \
              "$$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$$ → $$수식$${A} over {B}$$/수식$$,\n" \
              "{saying1},\n" \
              "{saying2},\n" \
              "{saying3}\n" \
              "$$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$${gwa1} 비율이 같은 비는 $$수식$${G}$$/수식$$ : $$수식$${H}$$/수식$$이므로 " \
              "비례식으로 나타내면 $$수식$${A}$$/수식$$ : $$수식$${B} ` = ` {G}`$$/수식$$  : $$수식$${H}$$/수식$$입니다.\n\n"



    while True:
        A = np.random.randint(1, 10)
        B = np.random.randint(1, 10)
        C = np.random.randint(1, 50)
        D = np.random.randint(1, 50)

        E = np.random.randint(1, 50)
        F = np.random.randint(1, 50)
        ef = gcd(E, F)
        EE = E / ef
        FF = F / ef

        if B > A and gcd(A, B) == 1 and D > C and gcd(C, D) == 1 and (C / D) != (A / B):
            if F > E and EE / FF != A / B:
                if F != D and C != E:
                    break


    k = np.random.randint(2, 6)
    G = A * k
    H = B * k

    if gcd(E, F) == 1:
        efs = ""
    else:
        efs = "` = ` {%d} over {%d} " % (EE, FF)

    q1 = "$$수식$$%d$$/수식$$ : $$수식$$%d$$/수식$$" % (C, D)
    q2 = "$$수식$$%d$$/수식$$ : $$수식$$%d$$/수식$$" % (E, F)
    q3 = "$$수식$$%d$$/수식$$ : $$수식$$%d$$/수식$$" % (G, H)

    q1_comme = f"$$수식$${C}$$/수식$$ : $$수식$${D}$$/수식$$ → $$수식$${C} over {D}$$/수식$$"
    q2_comme = f"$$수식$${E}$$/수식$$ : $$수식$${F}$$/수식$$ → $$수식$${E} over {F} {efs}$$/수식$$"
    q3_comme = f"$$수식$${G}$$/수식$$ : $$수식$${H}$$/수식$$ → $$수식$${G} over {H} ` = ` {A} over {B}$$/수식$$"

    Q = [[q1, q1_comme], [q2, q2_comme], [q3, q3_comme]]
    random.shuffle(Q)
    Q1, Q2, Q3 = Q[0][0], Q[1][0], Q[2][0]
    saying1, saying2, saying3 = Q[0][1], Q[1][1], Q[2][1]


    gwa1 = get_josa(B, "과")


    stem = stem.format(A=A, B=B, Q1=Q1, Q2=Q2, Q3=Q3, gwa1=gwa1)
    answer = answer.format(G=G, H=H)
    comment = comment.format(A=A, B=B, G=G, H=H, ef=efs, saying1=saying1, saying2=saying2, saying3=saying3, gwa1=gwa1)

    return stem, answer, comment


    # Q = [q1, q2, q3]
    # random.shuffle(Q)
    # Q1, Q2, Q3 = Q[0], Q[1], Q[2]

    # if (gcd(E, F) == 1):
    #     ef = ""
    # else:
    #     ef = "$$수식$$` = ` {%d} over {%d} $$/수식$$" % (EE, FF)































#6-2-4-27
def proandpro624_Stem_020():
    stem = "비례식을 보고 □ 안에 알맞은 수를 쓰세요.\n$$표$$ $$수식$${A}$$/수식$$ : $$수식$${B} ` = ` {C} $$/수식$$  : $$수식$${D}$$/수식$$ $$/표$$\n" \
        "외항 : $$수식$${A}$$/수식$$, $$수식$${boxblank}$$/수식$$\n내항 : $$수식$${boxblank}$$/수식$$, $$수식$${C}$$/수식$$"
    answer = "(정답)\n$$수식$${D}$$/수식$$, $$수식$${B}$$/수식$$\n"
    comment = "(해설)\n" \
              "비례식 $$수식$${A}$$/수식$$ : $$수식$${B} ` = ` {C} $$/수식$$  : $$수식$${D}$$/수식$$에서 내항은 " \
              "$$수식$${B}$$/수식$${gwa1} $$수식$${C}$$/수식$$이고, 외항은 $$수식$${A}$$/수식$${gwa2} $$수식$${D}$$/수식$$입니다.\n\n"

    boxblank = "BOX{　　}"
    while True:
        A = np.random.randint(1, 31)
        B = np.random.randint(1, 31)
        k = np.random.randint(1, 31)
        C = A * k
        D = B * k

        if C <= 30 and D <= 30 and A != C and B != D:
            break

    gwa1 = get_josa(B, "과")
    gwa2 = get_josa(A, "과")

    stem = stem.format(A=A, B=B, C=C, D=D, boxblank=boxblank)
    answer = answer.format(A=A, B=B, C=C, D=D)
    comment = comment.format(A=A, B=B, C=C, D=D, gwa1=gwa1, gwa2=gwa2)

    return stem, answer, comment































#6-2-4-28
def proandpro624_Stem_021():
    stem = "{P}{y1}와 {Q}{y2}가 비례식 $$수식$${A}$$/수식$$ : $$수식$${B} ` = ` {C}$$/수식$$  : $$수식$${D}$$/수식$${rur1} 보고 한 생각입니다. 잘못 생각한 사람은 누구인가요?\n$$표$${Q1}\n{Q2} $$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "비례식 $$수식$${A}$$/수식$$ : $$수식$${B} ` = ` {C} $$/수식$$ : $$수식$${D}$$/수식$$에서 내항은 " \
              "$$수식$${B}$$/수식$${gwa2} $$수식$${C}$$/수식$$이고, 외항은 $$수식$${A}$$/수식$${gwa1} $$수식$${D}$$/수식$$입니다.\n\n"


    pq = random.sample(["한솔", "태민", "기범", "수정", "준수", "현우"], 2)
    P, Q = pq[0], pq[1]

    y1 = ""
    y2 = ""

    other_name = ["준수", "현우"]
    if P not in other_name:
        y1 = "이"
    if Q not in other_name:
        y2 = "이"

    while True:
        E = np.random.randint(1, 21)
        F = np.random.randint(1, 21)
        k = np.random.randint(1, 51)
        l = np.random.randint(1, 51)
        A = E * k
        B = F * k
        C = E * l
        D = F * l
        if (F > E and gcd(E, F) == 1 and A <= 50 and B <= 50 and C <= 50 and D <= 50 and A != C and B != D):
            break

    gwa1 = get_josa(A, "과")
    gwa2 = get_josa(B, "과")
    ro1 = get_josa(E, "로")

    q1 = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ 비례식 $$수식$$%d$$/수식$$ : $$수식$$%d ` = ` %d  $$/수식$$ : $$수식$$%d$$/수식$$에서 내항은 $$수식$$%d$$/수식$$%s " \
         "$$수식$$%d$$/수식$$이고, 외항은 $$수식$$%d$$/수식$$%s $$수식$$%d$$/수식$$이야." % (P, A, B, C, D, A, gwa1, C, B, gwa2, D)
    q2 = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ 비례식으로 나타낸 두 비의 비율은 $$수식$${%d} over {%d}$$/수식$$%s 같아." % (Q, E, F, ro1)

    ans = P

    qq = [q1, q2]
    random.shuffle(qq)
    Q1, Q2 = qq[0], qq[1]

    if qq[0] == q2:
        P, Q = Q, P

    rur1 = get_josa(D, "를")


    stem = stem.format(P=P, Q=Q, A=A, B=B, C=C, D=D, Q1=Q1, Q2=Q2, y1=y1, y2=y2, rur1=rur1)
    answer = answer.format(ans=ans)
    comment = comment.format(A=A, B=B, C=C, D=D, gwa1=gwa1, gwa2=gwa2)

    return stem, answer, comment



































#6-2-4-29
def proandpro624_Stem_022():
    stem = "비율을 보고 비례식으로 나타내어 보세요\n$$수식$${A} over {B} ` = ` {C} over {D} $$/수식$$\n"
    answer = "(정답)\n$$수식$${A}$$/수식$$ : $$수식$${B} ` = ` {C}$$/수식$$ : $$수식$${D}$$/수식$$, $$수식$${C}$$/수식$$ : $$수식$${D} ` = ` {A}$$/수식$$ : $$수식$${B}$$/수식$$\n"
    comment = "(해설)\n" \
              "비율을 비로 나타낼 때에는 분자를 전항에, 분모를 후항에 씁니다.\n" \
              "$$수식$${A} over {B}$$/수식$$ → $$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$$, $$수식$${C} over {D}$$/수식$$ → $$수식$${C}$$/수식$$ : $$수식$${D}$$/수식$$\n" \
              "따라서 비례식으로 나타내면\n" \
              "$$수식$${A}$$/수식$$ : $$수식$${B} ` = ` {C} $$/수식$$ : $$수식$${D}$$/수식$$ 또는 $$수식$${C}$$/수식$$ : $$수식$${D} ` = ` {A} $$/수식$$ : $$수식$${B}$$/수식$$\n\n"


    while True:
        A = np.random.randint(1, 31)
        B = np.random.randint(1, 31)
        k = np.random.randint(2, 31)
        C = A * k
        D = B * k

        if (B > A and D > C and C <= 30 and D <= 30):
            break


    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(A=A, B=B, C=C, D=D)
    comment = comment.format(A=A, B=B, C=C, D=D)

    return stem, answer, comment

































#6-2-4-30
def proandpro624_Stem_023():
    stem = "후항이 $$수식$${P}$$/수식$$ 또는 $$수식$${Q}$$/수식$$인 비 중에서 비율이 같은 비를 찾아 비례식으로 나타내어 보세요.\n$$표$${Q1}    {Q2}    {Q3}\n{Q4}    {Q5}    {Q6}$$/표$$\n"
    answer = "(정답)\n$$수식$${A}$$/수식$$ : $$수식$${P} ` = ` {C}$$/수식$$ : $$수식$${Q}$$/수식$$, $$수식$${C}$$/수식$$ : $$수식$${Q} ` = ` {A}$$/수식$$ : $$수식$${P}$$/수식$$\n"
    comment = "(해설)\n" \
              "후항이 $$수식$${P}$$/수식$$인 비 → $$수식$${A}$$/수식$$ : $$수식$${P}$$/수식$$, $$수식$${B}$$/수식$$ : $$수식$${P}$$/수식$$\n" \
              "후항이 $$수식$${Q}$$/수식$$인 비 → $$수식$${C}$$/수식$$ : $$수식$${Q}$$/수식$$, $$수식$${D}$$/수식$$ : $$수식$${Q}$$/수식$$\n" \
              "각 비의 비율을 알아봅시다.\n" \
              "$$수식$${A}$$/수식$$ : $$수식$${P}$$/수식$$ → $$수식$${A} over {P} ` = ` {a} over {b} $$/수식$$,\n" \
              "$$수식$${B}$$/수식$$ : $$수식$${P}$$/수식$$ → $$수식$${B} over {P} ` = ` {c} over {d} $$/수식$$,\n" \
              "$$수식$${C}$$/수식$$ : $$수식$${Q}$$/수식$$ → $$수식$${C} over {Q} ` = ` {a} over {b} $$/수식$$,\n" \
              "$$수식$${D}$$/수식$$ : $$수식$${Q}$$/수식$$ → $$수식$${D} over {Q} ` = ` {e} over {f} $$/수식$$\n" \
              "$$수식$${A}$$/수식$$ : $$수식$${P}$$/수식$${gwa1} $$수식$${C}$$/수식$$ : $$수식$${Q}$$/수식$$의 비율이 같으므로 비례식으로 나타낼 수 있습니다.\n" \
              "→ $$수식$${A}$$/수식$$ : $$수식$${P} ` = ` {C} $$/수식$$ : $$수식$${Q}$$/수식$$ 또는 $$수식$${C}$$/수식$$ : $$수식$${Q} ` = ` {A} $$/수식$$ : $$수식$${P}$$/수식$$\n\n"


    while True:
        temp_list = []

        for idx in range(2, 11):
            temp_list.append(idx)

        two_list = random.sample(temp_list, 2)
        two_list.sort()

        a, b = two_list

        if soroso(a, b) == 0:
            continue

        p_times, q_times = random.sample(temp_list, 2)

        A = a * p_times
        P = b * p_times

        C = a * q_times
        Q = b * q_times

        P_yaksu_list = get_yaksu(P)
        Q_yaksu_list = get_yaksu(Q)

        if P > 20 or Q > 20 or len(P_yaksu_list) < 4 or len(Q_yaksu_list) < 4:
            continue



        while True:
            while True:
                P_yaksu_res = random.sample(P_yaksu_list, 1)
                P_yaksu = P_yaksu_res[0]
                if P_yaksu != 1 and P_yaksu != P and P_yaksu != p_times:
                    break

            d = int(P / P_yaksu)

            while True:
                c = np.random.randint(1, 21)
                if c < d:
                    break

            B = c * P_yaksu


            while True:
                Q_yaksu_res = random.sample(Q_yaksu_list, 1)
                Q_yaksu = Q_yaksu_res[0]
                if Q_yaksu != 1 and Q_yaksu != Q and Q_yaksu != q_times:
                    break

            f = int(Q / Q_yaksu)

            while True:
                e = np.random.randint(1, 21)
                if e < f:
                    break

            D = e * Q_yaksu

            cd_gcd = get_gcd(c, d)
            c = int(c / cd_gcd)
            d = int(d / cd_gcd)

            ef_gcd = get_gcd(e, f)
            e = int(e / ef_gcd)
            f = int(f / ef_gcd)

            if c != e:
                break

        break




    temp_list2 = []

    for sdx in range(2, 21):
        temp_list2.append(sdx)


    while True:
        ef_list = random.sample(temp_list2, 2)
        ef_list.sort()
        E, F = ef_list

        gh_list = random.sample(temp_list2, 2)
        gh_list.sort()
        G, H = gh_list

        if F != P and F != Q and H != P and H != Q and a / b != E / F and a / b != G / H:
            break




    q1 = "$$수식$$%d : %d $$/수식$$" % (A, P)
    q2 = "$$수식$$%d : %d $$/수식$$" % (B, P)
    q3 = "$$수식$$%d : %d $$/수식$$" % (C, Q)
    q4 = "$$수식$$%d : %d $$/수식$$" % (D, Q)
    q5 = "$$수식$$%d : %d $$/수식$$" % (E, F)
    q6 = "$$수식$$%d : %d $$/수식$$" % (G, H)

    qq = [q1, q2, q3, q4, q5, q6]
    random.shuffle(qq)
    Q1, Q2, Q3, Q4, Q5, Q6 = qq[0], qq[1], qq[2], qq[3], qq[4], qq[5]

    gwa1 = get_josa(P, "과")


    stem = stem.format(Q=Q, P=P, Q1=Q1, Q2=Q2, Q3=Q3, Q4=Q4, Q5=Q5, Q6=Q6)
    answer = answer.format(A=A, P=P, C=C, Q=Q)
    comment = comment.format(P=P, A=A, B=B, C=C, D=D, Q=Q, a=a, b=b, c=c, d=d, e=e, f=f, gwa1=gwa1)

    return stem, answer, comment




    # 무한루프
    # while True:
    #     P = np.random.randint(1, 21)
    #     Q = np.random.randint(1, 21)
    #     pq = gcd(P, Q)
    #     if pq >= 2 and pq <= 9 and P != Q:
    #         break
    #
    # while True:
    #     A = np.random.randint(1, P)
    #     B = np.random.randint(1, P)
    #     C = np.random.randint(1, Q)
    #     D = np.random.randint(1, Q)
    #     if A != B and C != D and (A * Q) == (C * P):
    #         break
    #
    # while True:
    #     a = np.random.randint(1, 10)
    #     b = np.random.randint(1, 10)
    #     c = np.random.randint(1, 10)
    #     d = np.random.randint(1, 10)
    #     e = np.random.randint(1, 10)
    #     f = np.random.randint(1, 10)
    #     if (gcd(a, b) == 1 and gcd(c, d) == 1 and gcd(e, f) == 1 and (A * b) == (P * a) and (C * b) == (Q * a) and (
    #             B * d) == (P * c) and (D * f) == (Q * e)):
    #         break
    #
    # while True:
    #     F = np.random.randint(1, 21)
    #     H = np.random.randint(1, 21)
    #     if (P != Q):
    #         break


































#6-2-4-31
def proandpro624_Stem_024():
    stem = "비율이 $$수식$${A} over {B}$$/수식$${ga1} 되도록 □ 안에 알맞은 수를 써넣으세요.\n$$수식$${C}$$/수식$$ : $$수식$${box1}$$/수식$$ $$수식$$` = ` {D}$$/수식$$ : $$수식$${box2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${E}$$/수식$$, $$수식$${F}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${C}$$/수식$$ : ㉠ $$수식$$` = ` {D}$$/수식$$ : ㉡이라 하면 각 비율이 $$수식$${A} over {B}$$/수식$$이므로 " \
              "$$수식$${C} over {blank1} ` = ` {A} over {B}$$/수식$$에서 ㉠ $$수식$$` = ` {E}$$/수식$$이고,\n" \
              "$$수식$${D} over {blank2} ` = ` {A} over {B}$$/수식$$에서 ㉡ $$수식$$` = ` {F}$$/수식$$입니다.\n\n"


    while True:
        B = np.random.randint(1, 11)
        A = np.random.randint(1, 11)
        k = np.random.randint(1, 11)
        l = np.random.randint(1, 11)
        C = A * k
        E = B * k
        D = A * l
        F = B * l

        if B > A and gcd(A, B) == 1 and C <= 20 and D <= 20 and C != D:
            break


    blank1 = "㉠"
    blank2 = "㉡"

    box1 = "box{㉠````````````````````}"
    box2 = "box{㉡````````````````````}"
    ga1 = get_josa(A, "가")


    stem = stem.format(A=A, B=B, C=C, D=D, ga1=ga1, box1=box1, box2=box2)
    answer = answer.format(E=E, F=F)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, blank1=blank1, blank2=blank2)

    return stem, answer, comment






























#6-2-4-32
def proandpro624_Stem_025():
    stem = "$$수식$$4$$/수식$$장의 수 카드 $$수식$${boxone}$$/수식$$, $$수식$${boxtwo}$$/수식$$, $$수식$${boxthree}$$/수식$$, $$수식$${boxfour}$$/수식$${rur1} 한 번씩 모두 사용하여 비율이 $$수식$${p} over {q}$$/수식$$인 두 비를 구했습니다. 구한 두 비를 이용하여 비례식으로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${A}$$/수식$$ : $$수식$${B} ` = ` {C}$$/수식$$ : $$수식$${D}$$/수식$$, $$수식$${C}$$/수식$$ : $$수식$${D} ` = ` {A}$$/수식$$ : $$수식$${B}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A} over {B} ` = ` {p} over {q}$$/수식$$이므로 비로 나타내면 $$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$$,\n" \
              "$$수식$${C} over {D} ` = ` {p} over {q}$$/수식$$이므로 비로 나타내면 $$수식$${C}$$/수식$$ : $$수식$${D}$$/수식$$입니다.\n" \
              "따라서 두 비를 이용하여 비례식으로 나타내면\n" \
              "$$수식$${A}$$/수식$$ : $$수식$${B} ` = ` {C} $$/수식$$ : $$수식$${D}$$/수식$$ 또는 " \
              "$$수식$${C}$$/수식$$ : $$수식$${D} ` = ` {A} $$/수식$$ : $$수식$${B}$$/수식$$입니다.\n\n"


    # while True:
    #     p = np.random.randint(1, 11)
    #     q = np.random.randint(1, 11)
    #     if gcd(p, q) == 1 and q > p:
    #         break
    #
    # while True:
    #     k = np.random.randint(2, 11)
    #     l = np.random.randint(2, 11)
    #     A = p * k
    #     B = q * k
    #     C = p * l
    #     D = q * l
    #
    #     if k < l and A <= 30 and B <= 30 and C <= 30 and D <= 30:
    #         break

    while True:
        p = np.random.randint(1, 11)
        q = np.random.randint(1, 11)

        k = np.random.randint(2, 11)
        l = np.random.randint(2, 11)

        A = p * k
        B = q * k
        C = p * l
        D = q * l

        if gcd(p, q) == 1 and q > p and k < l and A <= 30 and B <= 30 and C <= 30 and D <= 30:
            break


    num = [A, B, C, D]
    random.shuffle(num)
    a, b, c, d = num[0], num[1], num[2], num[3]

    boxone = "%d" % (a)
    boxtwo = "%d" % (b)
    boxthree = "%d" % (c)
    boxfour = "%d" % (d)

    rur1 = get_josa(d, "를")


    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour, p=p, q=q, rur1=rur1)
    answer = answer.format(A=A, B=B, C=C, D=D)
    comment = comment.format(A=A, B=B, C=C, D=D, p=p, q=q)

    return stem, answer, comment































#6-2-4-33
def proandpro624_Stem_026():
    stem = "다음 비례식의 외항의 곱이 $$수식$${A}$$/수식$$일 때, ㉠ $$수식$$+$$/수식$$ ㉡의 값은 얼마인가요?\n$$표$$㉠ : $$수식$${B} ` = ` $$/수식$$ ㉡ : $$수식$${C}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$$TIMES {C} ` = ` {A}$$/수식$$이므로 ㉠ $$수식$$ ` = ` {A} div {C} ` = ` {P}$$/수식$$입니다.\n" \
              "내항의 곱도 $$수식$${A}$$/수식$$이므로 $$수식$${B} TIMES $$/수식$$ ㉡ $$수식$$` = ` {A}$$/수식$$, " \
              "㉡ $$수식$$` = ` {A} div {B} ` = ` {Q}$$/수식$$입니다.\n" \
              "따라서 ㉠ $$수식$$+$$/수식$$ ㉡ $$수식$$` = ` {P} + {Q} ` = ` {D}$$/수식$$입니다.\n\n"


    while True:
        B = np.random.randint(1, 51)
        C = np.random.randint(1, 51)
        P = np.random.randint(1, 51)
        # Q = np.random.randint(1, 51)
        Q = (P * C) / B

        if gcd(B, C) >= 2 and gcd(B, C) <= 15 and P < B and Q < C and int(Q) == Q:
            Q = int(Q)
            break

    A = P * C
    D = P + Q


    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(D=D)
    comment = comment.format(A=A, B=B, C=C, D=D, P=P, Q=Q)

    return stem, answer, comment


































#6-2-4-34
def proandpro624_Stem_027():
    stem = "다음 조건에 맞게 비례식을 완성해 보세요.\n$$표$$비율은 $$수식$${A} over {B}$$/수식$$입니다.\n외항의 곱은 $$수식$${C}$$/수식$$입니다.$$/표$$\n$$수식$${A}$$/수식$$ : $$수식$${box} ` = ` {box} $$/수식$$ : $$수식$${box}$$/수식$$\n"
    answer = "(정답)\n$$수식$${A}$$/수식$$ : $$수식$${B} ` = ` {D}$$/수식$$ : $$수식$${E}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$ :  ㉠ $$수식$$` = ` $$/수식$$ ㉡ : ㉢이라 하면\n" \
              "$$수식$${A}$$/수식$$ : ㉠의 비율이 $$수식$${A} over {B}$$/수식$$이므로 ㉠ $$수식$$` = `{B}$$/수식$$입니다.\n" \
              "외항의 곱이 $$수식$${C}$$/수식$$이므로 $$수식$${A} TIMES $$/수식$$ ㉢ $$수식$$` = ` {C}$$/수식$$, ㉢ $$수식$$` = ` {E}$$/수식$$입니다.\n" \
              "㉡ : $$수식$${E}$$/수식$$의 비율이 $$수식$${A} over {B}$$/수식$$이므로 $$수식$${{㉡}} over {E} ` = ` {A} over {B}$$/수식$$에서 ㉡ $$수식$$` = ` {D}$$/수식$$입니다.\n\n"


    # while True:
    #     A = np.random.randint(1, 11)
    #     B = np.random.randint(1, 11)
    #     if gcd(A, B) == 1 and B > A:
    #         break
    #
    # while True:
    #     k = np.random.randint(1, 20)
    #     D = A * k
    #     E = B * k
    #     if D >= 10 and D <= 40:
    #         break

    while True:
        A = np.random.randint(1, 11)
        B = np.random.randint(1, 11)

        k = np.random.randint(1, 20)
        D = A * k
        E = B * k

        if gcd(A, B) == 1 and B > A and D >= 10 and D <= 40:
            break

    C = A * E
    box = "□"


    stem = stem.format(A=A, B=B, C=C, box=box)
    answer = answer.format(A=A, B=B, D=D, E=E)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E)

    return stem, answer, comment
































#6-2-4-35
def proandpro624_Stem_028():
    stem = "비례식의 성질을 이용하여 ㉠에 알맞은 소수를 구해 보세요.\n$$표$$$$수식$${A}$$/수식$$ : ㉠ $$수식$$` = ` {B}$$/수식$$ : $$수식$${C}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$ : ㉠ $$수식$$` = ` {B}$$/수식$$ : $$수식$${C}$$/수식$$\n" \
              "→ $$수식$${A} TIMES {C} ` = ` $$/수식$$ ㉠ $$수식$$ TIMES {B}$$/수식$$, ㉠ $$수식$$TIMES {B} ` = ` {E}$$/수식$$, ㉠ $$수식$$` = ` {D}$$/수식$$\n\n"


    # while True:
    #     B = np.random.randint(1, 11)
    #     C = np.random.randint(1, 11)
    #     if C > B and gcd(C, B) == 1:
    #         break
    #
    # while True:
    #     k = np.random.randint(1, 51)
    #     a = B * k
    #     if a <= 100:
    #         break

    while True:
        B = np.random.randint(1, 11)
        C = np.random.randint(1, 11)

        k = np.random.randint(1, 51)
        a = B * k

        if C > B and gcd(C, B) == 1 and a <= 100:
            break


    d = C * k
    A = round(a / 100, 2)
    D = round(d / 100, 2)
    E = A * C
    E = round(E, 2)

    A = show_int(A)
    D = show_int(D)
    E = show_int(E)


    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(D=D)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E)

    return stem, answer, comment

































#6-2-4-36
def proandpro624_Stem_029():
    stem = "다음 비례식에서 □ $$수식$$TIMES {B}$$/수식$$ 의 값을 구해 보세요.\n$$표$$$$수식$${A}$$/수식$$ : □ $$수식$$` = ` {B}$$/수식$$ : $$수식$${C}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$\n"
    comment = "(해설)\n" \
              "내항의 곱 □$$수식$$ TIMES {B}$$/수식$${eun1} 외항의 곱 $$수식$${A} TIMES {C} ` = ` {D}$$/수식$${gwa1} 같습니다.\n\n"


    while True:
        B = np.random.randint(1, 11)
        C = np.random.randint(1, 11)
        A = np.random.randint(1, 31)
        if C > B and gcd(B, C) == 1 and A % B == 0:
            break


    D = A * C

    eun1 = get_josa(B, "는")
    gwa1 = get_josa(D, "과")


    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(D=D)
    comment = comment.format(A=A, B=B, C=C, D=D, eun1=eun1, gwa1=gwa1)

    return stem, answer, comment







































#6-2-4-37
def proandpro624_Stem_030():
    stem = "옳은 비례식을 찾아 기호를 써 보세요.\n$$표$$㉠ {Q1}\n㉡ {Q2}\n㉢ {Q3}\n㉣ {Q4} $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "㉠ {A1}\n" \
              "㉡ {A2}\n" \
              "㉢ {A3}\n" \
              "㉣ {A4}\n" \
              "비례식은 외항의 곱과 내항의 곱은 같으므로 옳은 비례식은 {a1}입니다.\n\n"



    temp_list1 = []
    for s_dx in range(1, 31):
        temp_list1.append(s_dx)

    temp_list2 = []
    for i_dx in range(2, 11):
        temp_list2.append(i_dx)

    temp_list3 = []
    for t_dx in range(1, 301):
        t_dx_dec = round(t_dx / 10, 1)
        temp_list3.append(t_dx_dec)


    this_ans = np.random.randint(0, 4)

    if this_ans == 0:
        while True:
            s_bb, s_dd = random.sample(temp_list1, 2)
            s_aa = np.random.randint(1, 31)
            s_cc = (s_aa * s_dd) / s_bb

            if s_cc == int(s_cc) and s_cc <= 30:
                break

        while True:
            ef_list = random.sample(temp_list2, 2)
            ef_list.sort()
            s_ee, s_ff = ef_list

            while True:
                ef_times = np.random.randint(1, 16)
                s_jj = s_ff * ef_times
                if s_jj <= 30:
                    break

            gh_list = random.sample(temp_list2, 2)
            gh_list.sort()
            s_gg, s_hh = gh_list

            if s_ff == s_hh and s_ee == s_gg:
                continue

            while True:
                gh_times = np.random.randint(1, 16)
                s_ii = s_hh * gh_times
                if s_ii <= 30:
                    break

            if s_gg * gh_times != s_ee * ef_times:
                break

        while True:
            s_ll, s_nn = random.sample(temp_list3, 2)
            for_k = random.sample(temp_list3, 1)
            s_kk = for_k[0]
            for_m = random.sample(temp_list3, 1)
            s_mm = for_m[0]

            if s_kk * s_nn != s_ll * s_mm:
                break

        while True:
            s_pp, s_rr = random.sample(temp_list3, 2)
            for_o = random.sample(temp_list3, 1)
            s_oo = for_o[0]
            for_q = random.sample(temp_list3, 1)
            s_qq = for_q[0]

            if s_oo * s_rr != s_pp * s_qq:
                break


    elif this_ans == 1:
        while True:
            s_bb, s_dd = random.sample(temp_list1, 2)
            for_a = random.sample(temp_list1, 1)
            s_aa = for_a[0]
            for_c = random.sample(temp_list1, 1)
            s_cc = for_c[0]

            if s_aa * s_dd != s_bb * s_cc:
                break

        while True:
            ef_list = random.sample(temp_list2, 2)
            ef_list.sort()
            s_ee, s_ff = ef_list

            while True:
                ef_times = np.random.randint(1, 16)
                s_jj = s_ff * ef_times
                if s_jj <= 30:
                    break

            gh_list = random.sample(temp_list2, 2)
            gh_list.sort()
            s_gg, s_hh = gh_list

            if s_ff == s_hh and s_ee == s_gg:
                continue

            while True:
                gh_times = np.random.randint(1, 16)
                s_ii = s_hh * gh_times
                if s_ii <= 30:
                    break

            if s_gg * gh_times == s_ee * ef_times:
                break

        while True:
            s_ll, s_nn = random.sample(temp_list3, 2)
            for_k = random.sample(temp_list3, 1)
            s_kk = for_k[0]
            for_m = random.sample(temp_list3, 1)
            s_mm = for_m[0]

            if s_kk * s_nn != s_ll * s_mm:
                break

        while True:
            s_pp, s_rr = random.sample(temp_list3, 2)
            for_o = random.sample(temp_list3, 1)
            s_oo = for_o[0]
            for_q = random.sample(temp_list3, 1)
            s_qq = for_q[0]

            if s_oo * s_rr != s_pp * s_qq:
                break


    elif this_ans == 2:
        while True:
            s_bb, s_dd = random.sample(temp_list1, 2)
            for_a = random.sample(temp_list1, 1)
            s_aa = for_a[0]
            for_c = random.sample(temp_list1, 1)
            s_cc = for_c[0]

            if s_aa * s_dd != s_bb * s_cc:
                break

        while True:
            ef_list = random.sample(temp_list2, 2)
            ef_list.sort()
            s_ee, s_ff = ef_list

            while True:
                ef_times = np.random.randint(1, 16)
                s_jj = s_ff * ef_times
                if s_jj <= 30:
                    break

            gh_list = random.sample(temp_list2, 2)
            gh_list.sort()
            s_gg, s_hh = gh_list

            if s_ff == s_hh and s_ee == s_gg:
                continue

            while True:
                gh_times = np.random.randint(1, 16)
                s_ii = s_hh * gh_times
                if s_ii <= 30:
                    break

            if s_gg * gh_times != s_ee * ef_times:
                break

        while True:
            s_ll, s_nn = random.sample(temp_list3, 2)
            for_k = random.sample(temp_list3, 1)
            s_kk = for_k[0]

            s_mm = (s_kk * s_nn) / s_ll
            s_mm = round(s_mm, 1)

            if s_mm in temp_list3 and s_kk * s_nn == s_ll * s_mm:
                break

        while True:
            s_pp, s_rr = random.sample(temp_list3, 2)
            for_o = random.sample(temp_list3, 1)
            s_oo = for_o[0]
            for_q = random.sample(temp_list3, 1)
            s_qq = for_q[0]

            if s_oo * s_rr != s_pp * s_qq:
                break


    elif this_ans == 3:
        while True:
            s_bb, s_dd = random.sample(temp_list1, 2)
            for_a = random.sample(temp_list1, 1)
            s_aa = for_a[0]
            for_c = random.sample(temp_list1, 1)
            s_cc = for_c[0]

            if s_aa * s_dd != s_bb * s_cc:
                break

        while True:
            ef_list = random.sample(temp_list2, 2)
            ef_list.sort()
            s_ee, s_ff = ef_list

            while True:
                ef_times = np.random.randint(1, 16)
                s_jj = s_ff * ef_times
                if s_jj <= 30:
                    break

            gh_list = random.sample(temp_list2, 2)
            gh_list.sort()
            s_gg, s_hh = gh_list

            if s_ff == s_hh and s_ee == s_gg:
                continue

            while True:
                gh_times = np.random.randint(1, 16)
                s_ii = s_hh * gh_times
                if s_ii <= 30:
                    break

            if s_gg * gh_times != s_ee * ef_times:
                break

        while True:
            s_ll, s_nn = random.sample(temp_list3, 2)
            for_k = random.sample(temp_list3, 1)
            s_kk = for_k[0]
            for_m = random.sample(temp_list3, 1)
            s_mm = for_m[0]

            if s_kk * s_nn != s_ll * s_mm:
                break

        while True:
            s_pp, s_rr = random.sample(temp_list3, 2)
            for_o = random.sample(temp_list3, 1)
            s_oo = for_o[0]

            s_qq = (s_oo * s_rr) / s_pp
            s_qq = round(s_qq, 1)

            if s_qq in temp_list3 and s_oo * s_rr == s_pp * s_qq:
                break



    s_cc = show_int(s_cc)

    s_kk = show_int(s_kk)
    s_ll = show_int(s_ll)
    s_mm = show_int(s_mm)
    s_nn = show_int(s_nn)

    s_oo = show_int(s_oo)
    s_pp = show_int(s_pp)
    s_qq = show_int(s_qq)
    s_rr = show_int(s_rr)


    s_a = s_aa * s_dd
    s_b = s_bb * s_cc

    s_c = s_ee * ef_times
    s_d = s_gg * gh_times

    s_e = round(s_kk * s_nn, 2)
    s_e = show_int(s_e)

    s_f = round(s_ll * s_mm, 2)
    s_f = show_int(s_f)

    s_g = round(s_oo * s_rr, 2)
    s_g = show_int(s_g)

    s_h = round(s_pp * s_qq, 2)
    s_h = show_int(s_h)



    x1 = "$$수식$$%s$$/수식$$ : $$수식$$%s ` = ` %s$$/수식$$ : $$수식$$%s$$/수식$$" % (s_aa, s_bb, s_cc, s_dd)
    x2 = "$$수식$$%s over %s$$/수식$$ : $$수식$$%s over %s$$/수식$$ = $$수식$$%s$$/수식$$ : $$수식$$%s$$/수식$$" % (s_ee, s_ff, s_gg, s_hh, s_ii, s_jj)
    x3 = "$$수식$$%s$$/수식$$ : $$수식$$%s$$/수식$$ = $$수식$$%s$$/수식$$ : $$수식$$%s$$/수식$$" % (s_kk, s_ll, s_mm, s_nn)
    x4 = "$$수식$$%s$$/수식$$ : $$수식$$%s$$/수식$$ = $$수식$$%s$$/수식$$ : $$수식$$%s$$/수식$$" % (s_oo, s_pp, s_qq, s_rr)

    y1 = "$$수식$$LEFT ($$/수식$$외항의 곱$$수식$$RIGHT ) ` = ` %s TIMES %s ` = ` %s$$/수식$$\n $$수식$$LEFT ($$/수식$$내항의 곱$$수식$$RIGHT ) ` = ` %s TIMES %s ` = ` %s$$/수식$$" % (s_aa, s_dd, s_a, s_bb, s_cc, s_b)
    y2 = "$$수식$$LEFT ($$/수식$$외항의 곱$$수식$$RIGHT ) ` = ` %s over %s TIMES %s `= ` %s$$/수식$$\n $$수식$$LEFT ($$/수식$$내항의 곱$$수식$$RIGHT ) ` = `%s over %s TIMES %s ` = ` %s$$/수식$$" % (s_ee, s_ff, s_jj, s_c, s_gg, s_hh, s_ii, s_d)
    y3 = "$$수식$$LEFT ($$/수식$$외항의 곱$$수식$$RIGHT ) ` = ` %s TIMES %s ` = ` %s$$/수식$$\n $$수식$$LEFT ($$/수식$$내항의 곱$$수식$$RIGHT ) ` = ` %s TIMES %s ` = ` %s$$/수식$$" % (s_kk, s_nn, s_e, s_ll, s_mm, s_f)
    y4 = "$$수식$$LEFT ($$/수식$$외항의 곱$$수식$$RIGHT ) ` = ` %s TIMES %s ` = ` %s$$/수식$$\n $$수식$$LEFT ($$/수식$$내항의 곱$$수식$$RIGHT ) ` = ` %s TIMES %s ` = ` %s$$/수식$$" % (s_oo, s_rr, s_g, s_pp, s_qq, s_h)


    before_list = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
    random.shuffle(before_list)

    Q1, Q2, Q3, Q4 = before_list[0][0], before_list[1][0], before_list[2][0], before_list[3][0]
    A1, A2, A3, A4 = before_list[0][1], before_list[1][1], before_list[2][1], before_list[3][1]

    if this_ans == 0:
        if Q1 == x1:
            a1 = "㉠"
        elif Q2 == x1:
            a1 = "㉡"
        elif Q3 == x1:
            a1 = "㉢"
        elif Q4 == x1:
            a1 = "㉣"

    elif this_ans == 1:
        if Q1 == x2:
            a1 = "㉠"
        elif Q2 == x2:
            a1 = "㉡"
        elif Q3 == x2:
            a1 = "㉢"
        elif Q4 == x2:
            a1 = "㉣"

    elif this_ans == 2:
        if Q1 == x3:
            a1 = "㉠"
        elif Q2 == x3:
            a1 = "㉡"
        elif Q3 == x3:
            a1 = "㉢"
        elif Q4 == x3:
            a1 = "㉣"

    elif this_ans == 3:
        if Q1 == x4:
            a1 = "㉠"
        elif Q2 == x4:
            a1 = "㉡"
        elif Q3 == x4:
            a1 = "㉢"
        elif Q4 == x4:
            a1 = "㉣"



    stem = stem.format(Q1=Q1, Q2=Q2, Q3=Q3, Q4=Q4)
    answer = answer.format(a1=a1)
    comment = comment.format(A1=A1, A2=A2, A3=A3, A4=A4, a1=a1)


    return stem, answer, comment




    # aa1 = np.random.randint(0, 4)
    #
    # while True:
    #     A = np.random.randint(1, 31)
    #     B = np.random.randint(1, 31)
    #     C = np.random.randint(1, 31)
    #     D = np.random.randint(1, 31)
    #     F = np.random.randint(2, 11)
    #     E = np.random.randint(1, F)
    #     H = np.random.randint(2, 11)
    #     G = np.random.randint(1, H)
    #     I = np.random.randint(1, 31)
    #     J = np.random.randint(1, 31)
    #     k = np.random.randint(1, 301)
    #     K = k / 10
    #     ll = np.random.randint(1, 301)
    #     L = ll / 10
    #     m = np.random.randint(1, 301)
    #     M = m / 10
    #     n = np.random.randint(1, 301)
    #     N = n / 10
    #     o = np.random.randint(1, 301)
    #     O = o / 10
    #     p = np.random.randint(1, 301)
    #     P = p / 10
    #     q = np.random.randint(1, 301)
    #     Q = q / 10
    #     r = np.random.randint(1, 301)
    #     R = r / 10
    #     a = A * D
    #     b = B * C
    #     c = int(E / F * J)
    #     d = int(G / H * I)
    #     e = K * N
    #     f = L * M
    #     g = O * R
    #     h = P * Q
    #
    #     if (I % H == 0 and J % F == 0):
    #         if (aa1 == 0):
    #             if (a == b and c != d and e != f and g != h):
    #                 break
    #         elif (aa1 == 1):
    #             if (a != b and c == d and e == f and g == h):
    #                 break
    #         elif (aa1 == 2):
    #             if (a != b and c != d and e == f and g != h):
    #                 break
    #         elif (aa1 == 3):
    #             if (a != b and c != d and e != f and g == h):
    #                 break
    #
    # QQ1 = "$$수식$$%d : %d ` = ` %d: %d$$/수식$$" % (A, B, C, D)
    # QQ2 = "$$수식$$%d over %d : %d over %d = %d : %d$$/수식$$" % (E, F, G, H, I, J)
    # QQ3 = "$$수식$$%d : %d = %d : %d" % (K, L, M, N)
    # QQ4 = "$$수식$$%d : %d = %d: %d" % (O, P, Q, R)
    #
    # QQ = [QQ1, QQ2, QQ3, QQ4]
    # random.shuffle(QQ)
    # Q1, Q2, Q3, Q4 = QQ[0], QQ[1], QQ[2], QQ[3]
    #
    # A1 = "(외항의 곱)$$수식$$` = ` %d TIMES %d ` = ` %d$$/수식$$, (내항의 곱)$$수식$$` = ` %d TIMES %d ` = ` %d$$/수식$$" % (A, D, a, B, C, b)
    # A2 = "(외항의 곱)$$수식$$` = ` %d over %d TIMES %d `= ` %d$$/수식$$, (내항의 곱)$$수식$$` = `%d over %d TIMES %d ` = ` %d$$/수식$$" % (E, F, J, c, G, H, I, d)
    # A3 = "(외항의 곱)$$수식$$` = ` %d TIMES %d ` = ` %d$$/수식$$, (내항의 곱)$$수식$$` = ` %d TIMES %d ` = ` %d$$/수식$$" % (K, N, e, L, M, f)
    # A4 = "(외항의 곱)$$수식$$` = ` %d TIMES %d ` = ` %d$$/수식$$, (내항의 곱)$$수식$$` = ` %d TIMES %d ` = ` %d$$/수식$$" % (O, R, g, P, Q, h)
    #
    # aa = ["㉠", "㉡", "㉢", "㉣"]




































#6-2-4-38
def proandpro624_Stem_031():
    stem = "비례식의 성질을 이용하여 □ 안에 들어갈 알맞은 수를 구해 보세요.\n$$표$$$$수식$${A}$$/수식$$ : $$수식$${B} ` = ` $$/수식$$ □ : $$수식$${C} over {D}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${F} over {E}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$ : $$수식$${B} ` = ` $$/수식$$ □  : $$수식$${C} over {D}$$/수식$$ → " \
              "$$수식$${A} TIMES {C} over {D} ` = ` {B} TIMES {blank}$$/수식$$, " \
              "$$수식$${B} TIMES {blank}` = `{k}$$/수식$$, $$수식$${blank} ` = ` {F} over {E}$$/수식$$\n\n"

    while True:
        D = np.random.randint(2, 11)
        E = np.random.randint(2, 11)
        a = np.random.randint(2, 50)
        A = D * a
        b = np.random.randint(2, 50)
        B = E * b
        C = np.random.randint(1, D)
        F = np.random.randint(1, E)

        if (A < 100 and B < 100 and A != B and C < D and F < E and gcd(C, D) == 1 and gcd(E, F) == 1 and A * C * E == B * D * F):
            break

    k = int(A * C / D)
    blank = "□"


    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(E=E, F=F)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, k=k, blank=blank)

    return stem, answer, comment




































#6-2-4-39
def proandpro624_Stem_032():
    stem = "□ 안에 들어갈 수가 가장 큰 비례식을 찾아 기호를 써 보세요.\n$$표$$㉠ {Q1}\n ㉡ {Q2}\n ㉢ {Q3} $$/표$$\n"
    answer = "(정답)\n{a}\n"
    comment = "(해설)\n" \
              "㉠ {A1}\n" \
              "㉡ {A2}\n" \
              "㉢ {A3}\n" \
              "$$수식$${dhn1} &gt; `````{dhn2} &gt;````` {dhn3}$$/수식$$이므로 □ 안에 들어갈 수가 가장 큰 비례식은 {a}입니다.\n\n"


    while True:
        A = np.random.randint(1, 11)
        B = np.random.randint(1, 11)
        C = np.random.randint(1, 51)
        if gcd(A, B) == 1 and C % B == 0 and A != B:
            break

    D = A * C / B
    k = A * C

    while True:
        F = np.random.randint(1, 11)
        G = np.random.randint(1, 11)
        e = np.random.randint(10, 50)
        if gcd(F, G) == 1 and e % F == 0 and F != G:
            break

    E = round(e / 10, 1)
    E = show_int(E)

    l = round(E * G, 1)
    l = show_int(l)

    H = round(l / F, 3)
    H = show_int(H)

    while True:
        J = np.random.randint(2, 11)
        L = np.random.randint(2, 11)
        K = np.random.randint(1, J)
        M = np.random.randint(1, L)
        if gcd(K, J) == 1 and gcd(M, L) == 1 and (K / J) != (M / L):
            break

    while True:
        I = np.random.randint(1, 51)
        if I % J == 0:
            break

    m = I * K / J
    m = show_int(m)

    N = m * (L / M)

    D = round(D, 3)
    H = round(H, 3)
    N = round(N, 3)

    D = show_int(D)
    H = show_int(H)
    N = show_int(N)


    a1 = "$$수식$$%s : %s ` = ` □ : %s$$/수식$$\n" \
         "→ $$수식$$%s TIMES %s ` = ` %sTIMES □$$/수식$$, $$수식$$%s TIMES □ ` = ` %s$$/수식$$, $$수식$$ □` = ` %s$$/수식$$" % (A, B, C, A, C, B, B, k, D)

    a2 = "$$수식$$%s: □ ` = ` %s : %s$$/수식$$\n" \
         "→ $$수식$$%s TIMES %s ` = ` □ TIMES %s$$/수식$$, $$수식$$□ TIMES %s ` = ` %s$$/수식$$, $$수식$$□ ` = ` %s$$/수식$$" % (E, F, G, E, G, F, F, l, H)

    a3 = "$$수식$$□ : %s ` = ` %s over %s : %s over %s$$/수식$$\n" \
         "→ $$수식$$□ TIMES %s over %s ` = ` %s TIMES %s over %s$$/수식$$, $$수식$$□ TIMES %s over %s ` = ` %s$$/수식$$, $$수식$$□ ` = ` %s$$/수식$$" % (I, K, J, M, L, M, L, I, K, J, M, L, m, N)


    q1 = "$$수식$$%s$$/수식$$ : $$수식$$%s ` = `$$/수식$$ □ : $$수식$$%s$$/수식$$" % (A, B, C)
    q2 = "$$수식$$%s$$/수식$$ : □ $$수식$$` = ` %s$$/수식$$ : $$수식$$%s$$/수식$$" % (E, F, G)
    q3 = "□ : $$수식$$%s ` = ` %s over %s$$/수식$$ : $$수식$$%s over %s$$/수식$$" % (I, K, J, M, L)


    aa = [a1, a2, a3]
    qq = [q1, q2, q3]
    cc = [D, H, N]
    num = [0, 1, 2]
    random.shuffle(num)
    num1 = num[0]
    num2 = num[1]
    num3 = num[2]

    A1, A2, A3 = aa[num1], aa[num2], aa[num3]
    Q1, Q2, Q3 = qq[num1], qq[num2], qq[num3]

    dhn1 = max(cc)
    dhn2 = statistics.median(cc)
    dhn3 = min(cc)

    an = ["㉠", "㉡", "㉢"]
    a = ""

    if (dhn1 == D):
        if (num1 == 0):
            a = an[0]
        elif (num2 == 0):
            a = an[1]
        elif (num3 == 0):
            a = an[2]

    elif (dhn1 == H):
        if (num1 == 1):
            a = an[0]
        elif (num2 == 1):
            a = an[1]
        elif (num3 == 1):
            a = an[2]

    elif (dhn1 == N):
        if (num1 == 2):
            a = an[0]
        elif (num2 == 2):
            a = an[1]
        elif (num3 == 2):
            a = an[2]


    stem = stem.format(Q1=Q1, Q2=Q2, Q3=Q3)
    answer = answer.format(a=a)
    comment = comment.format(A1=A1, A2=A2, A3=A3, dhn1=dhn1, dhn2=dhn2, dhn3=dhn3, a=a)

    return stem, answer, comment



































#6-2-4-40
def proandpro624_Stem_033():
    stem = "소금과 물의 양의 비가 $$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$$인 소금물이 있습니다. 소금의 양이 $$수식$${C} rm g $$/수식$$이면 물의 양은 몇 $$수식$$ rm g $$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${D} rm g$$/수식$$\n"
    comment = "(해설)\n" \
              "물의 양을 □$$수식$$rm g$$/수식$$이라고 하면\n" \
              "$$수식$${A}$$/수식$$ : $$수식$${B} ` = ` {C}$$/수식$$ : □\n" \
              "→ $$수식$${A} TIMES $$/수식$$ □ $$수식$$` = ` {B} TIMES {C}$$/수식$$, $$수식$${A} TIMES $$/수식$$ □ $$수식$$` = `{k}$$/수식$$, □ $$수식$$` = ` {D}$$/수식$$\n" \
              "따라서 물의 양은 $$수식$${D} rm g$$/수식$$입니다.\n\n"


    while True:
        B = np.random.randint(2, 21)
        A = np.random.randint(1, B)
        C = np.random.randint(20, 101)

        if gcd(A, B) == 1 and C % A == 0:
            break

    D = B * int(C / A)
    k = B * C


    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(D=D)
    comment = comment.format(A=A, B=B, C=C, D=D, k=k)

    return stem, answer, comment


































#6-2-4-41
def proandpro624_Stem_034():
    stem = "비 ㉠ : ㉡을 간단한 자연수의 비로 나타낸 것은 어느 것인가요?\n$$표$$㉠$$수식$$TIMES {A} ` = ` $$/수식$$ ㉡$$수식$$TIMES {B}$$/수식$$ $$/표$$\n① {Q1}   ② {Q2}   ③ {Q3}\n④ {Q4}   ⑤ {Q5}\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "㉠$$수식$$TIMES {A} ` = ` $$/수식$$ ㉡$$수식$$TIMES {B}$$/수식$$\n" \
              "→ ㉠ : ㉡ $$수식$$` = ` {B}$$/수식$$ : $$수식$${A} ` = ` LEFT ( {B} TIMES 10 RIGHT )$$/수식$$ : $$수식$$LEFT ( {A} TIMES 10 RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {H}$$/수식$$ : $$수식$${G} ` = ` LEFT ( {H} div {p} RIGHT )$$/수식$$ : $$수식$$LEFT ( {G} div {p} RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {D}$$/수식$$ : $$수식$${C}$$/수식$$\n\n"


    # while True:
    #     G = np.random.randint(1, 50)
    #     H = np.random.randint(1, 50)
    #     if G % 10 != 0 and H % 10 != 0:
    #         break
    #
    # A = G * 0.1
    # A = round(A, 1)
    # B = H * 0.1
    # B = round(B, 1)
    # p = gcd(G, H)
    # C = int(G / p)
    # D = int(H / p)

    while True:
        G = np.random.randint(1, 50)
        H = np.random.randint(1, 50)

        A = G * 0.1
        A = round(A, 1)
        B = H * 0.1
        B = round(B, 1)
        p = gcd(G, H)
        C = int(G / p)
        D = int(H / p)

        if G % 10 != 0 and H % 10 != 0 and p != 1:
            break

    while True:
        e = np.random.randint(1, 50)
        f = np.random.randint(1, 50)
        if e != G and f != H:
            break

    E = e * 0.1
    F = f * 0.1

    q1 = "$$수식$$%0.1f$$/수식$$ : $$수식$$%0.1f$$/수식$$" % (A, B)
    q2 = "$$수식$$%0.1f$$/수식$$ : $$수식$$%0.1f$$/수식$$" % (B, A)
    q3 = "$$수식$$%d$$/수식$$ : $$수식$$%d$$/수식$$" % (C, D)
    q4 = "$$수식$$%d$$/수식$$ : $$수식$$%d$$/수식$$" % (D, C)
    q5 = "$$수식$$%0.1f$$/수식$$ : $$수식$$%0.1f$$/수식$$" % (E, F)


    Q = [q1, q2, q3, q4, q5]
    random.shuffle(Q)
    Q1, Q2, Q3, Q4, Q5 = Q[0], Q[1], Q[2], Q[3], Q[4]


    if (Q1 == q4):
        aa1 = 0
    elif (Q2 == q4):
        aa1 = 1
    elif (Q3 == q4):
        aa1 = 2
    elif (Q4 == q4):
        aa1 = 3
    else:
        aa1 = 4



    stem = stem.format(Q1=Q1, Q2=Q2, Q3=Q3, Q4=Q4, Q5=Q5, A=A, B=B)
    answer = answer.format(a1=answer_dict[aa1])
    comment = comment.format(A=A, B=B, C=C, D=D, G=G, H=H, p=p)

    return stem, answer, comment







































#6-2-4-43
def proandpro624_Stem_035():
    stem = "삼각형의 밑변의 길이와 높이의 비는 $$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$$입니다. 밑변의 길이가 $$수식$${C} rm {{cm}}$$/수식$$일 때 삼각형의 넓이는 몇 $$수식$$rm {{cm}}^2$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${P} rm {{cm}}^2$$/수식$$\n"
    comment = "(해설)\n" \
              "삼각형의 높이를 □ $$수식$$rm {{cm}}$$/수식$$라고 하면\n" \
              "$$수식$${A}$$/수식$$ : $$수식$${B} ` = ` {C}$$/수식$$ : □\n" \
              "→ $$수식$${A} TIMES $$/수식$$ □ $$수식$$` = ` {B} TIMES {C}$$/수식$$, $$수식$${A} TIMES $$/수식$$ □ $$수식$$` = ` {k}$$/수식$$, □ $$수식$$` = ` {D}$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$삼각형의 넓이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$밑변의 길이$$수식$$RIGHT ) ` TIMES ` LEFT ($$/수식$$높이$$수식$$RIGHT ) ` div 2 $$/수식$$\n" \
              "$$수식$$` = ` {C} TIMES {D} div 2 ` = ` {P} LEFT ( rm {{cm}}^2 RIGHT )$$/수식$$\n\n"


    while True:
        A = np.random.randint(1, 11)
        B = np.random.randint(1, 11)
        C = np.random.randint(1, 21)
        if gcd(A, B) == 1 and C % A == 0:
            break

    m = int(C / A)
    D = B * m
    k = B * C

    if ((C * D) % 2 == 0):
        P = int((C * D) / 2)
    else:
        P = (C * D) / 2


    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(P=P)
    comment = comment.format(A=A, B=B, C=C, D=D, P=P, k=k)

    return stem, answer, comment






































#6-2-4-44
def proandpro624_Stem_036():
    stem = "각 비의 비율이 $$수식$${A} over {B}$$/수식$${ga1} 되도록 □ 안에 알맞은 수를 써넣으세요.\n□ : $$수식$${C} ` = ` $$/수식$$ □ : $$수식$${D}$$/수식$$\n"
    answer = "(정답)\n$$수식$${E}$$/수식$$, $$수식$${F}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${{□}} over {C} ` = ` {A} over {B} $$/수식$$에서 □ $$수식$$` = ` {E}$$/수식$$이고,\n" \
              "$$수식$${{□}} over {D} ` = ` {A} over {B} $$/수식$$에서 □ $$수식$$` = ` {F}$$/수식$$입니다.\n\n"


    while True:
        B = np.random.randint(2, 11)
        A = np.random.randint(1, B)
        if gcd(B, A) == 1:
            break

    while True:
        c = np.random.randint(1, 51)
        d = np.random.randint(1, 51)
        if c % B == 0 and d % B == 0 and c != d:
            break

    if c % 10 == 0:
        C = int(c / 10)
    else:
        C = c / 10

    if d % 10 == 0:
        D = int(d / 10)
    else:
        D = d / 10

    if A * (c / B) % 10 == 0:
        E = int(A * (c / B) / 10)
    else:
        E = A * (c / B) / 10

    if A * (d / B) % 10 == 0:
        F = int(A * (d / B) / 10)
    else:
        F = A * (d / B) / 10

    blank = "□"

    ga1 = get_josa(A, "가")


    stem = stem.format(A=A, B=B, C=C, D=D, ga1=ga1)
    answer = answer.format(E=E, F=F)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F)

    return stem, answer, comment








































#6-2-4-45
def proandpro624_Stem_037():
    stem = "어머니께서 흰쌀과 {T}{rur1} $$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$${ro1} 섞어서 밥을 지으시려고 합니다. 흰쌀을 $$수식$${C} rm g$$/수식$$ 넣었다면 {T}{eun1} 몇 $$수식$$rm g$$/수식$$을 넣어야 하나요?\n"
    answer = "(정답)\n$$수식$${D} rm g$$/수식$$\n"
    comment = "(해설)\n" \
              "넣어야 하는 {T}{rur1} □ $$수식$$rm g$$/수식$$이라 놓고 비례식을 세우면 $$수식$${A}$$/수식$$ : $$수식$${B} ` = ` {C} $$/수식$$ : □ 입니다.\n" \
              "→ $$수식$${A} TIMES $$/수식$$ □ $$수식$$` = ` {B} TIMES {C}$$/수식$$, $$수식$${A} TIMES $$/수식$$ □ $$수식$$` = ` {k}$$/수식$$, □ $$수식$$` = ` {D}$$/수식$$\n" \
              "따라서 {T} $$수식$${D} rm g$$/수식$$을 넣어야 합니다.\n\n"


    T = random.choice(["콩", "흑미", "현미", "보리"])

    while True:
        A = np.random.randint(2, 11)
        B = np.random.randint(1, A)
        if gcd(A, B) == 1:
            break

    while True:
        C = np.random.randint(500, 1001)
        if C % A == 0:
            break

    D = B * int(C / A)
    k = B * C

    rur1 = proc_jo(T, 1)
    ro1 = get_josa(B, "로")
    eun1 = proc_jo(T, -1)


    stem = stem.format(A=A, B=B, C=C, T=T, rur1=rur1, ro1=ro1, eun1=eun1)
    answer = answer.format(D=D)
    comment = comment.format(A=A, B=B, C=C, D=D, k=k, T=T, rur1=rur1)

    return stem, answer, comment

































#6-2-4-46
def proandpro624_Stem_038():
    stem = "어떤 은행은 $$수식$${A}$$/수식$$원을 $$수식$${n}$$/수식$$년 동안 예금하면 이자가 $$수식$${B}$$/수식$$원입니다. 이 은행에 $$수식$${C}$$/수식$$원을 $$수식$${n}$$/수식$$년 동안 예금했을 때의 이자는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$원\n"
    comment = "(해설)\n" \
              "$$수식$${C}$$/수식$$원을 $$수식$${n}$$/수식$$년 동안 예금했을 때의 이자를 □원이라 놓고 비례식을 세우면\n" \
              "$$수식$${A}$$/수식$$ : $$수식$${B} ` = ` {C} $$/수식$$ : □ \n" \
              "→ $$수식$${A} TIMES $$/수식$$ □ $$수식$$` = ` {B} TIMES {C}$$/수식$$, " \
              "$$수식$${A} TIMES $$/수식$$ □ $$수식$$` = ` {k}$$/수식$$, □ $$수식$$` = ` {D}$$/수식$$\n" \
              "따라서 $$수식$${C}$$/수식$$원을 $$수식$${n}$$/수식$$년 동안 예금했을 때의 이자는 $$수식$${D}$$/수식$$원입니다.\n\n"


    n = np.random.randint(1, 11)
    a = np.random.randint(1, 101)
    b = np.random.randint(1, 51)
    A = a * 1000
    B = b * 10


    # while True:
    #     C = np.random.randint(10000, 5000000)
    #     if C % A == 0:
    #         break

    while True:
        C = np.random.randint(10, 5001) * A
        if 10000 <= C and C <= 5000000:
            break


    D = B * int(C / A)
    k = B * C


    stem = stem.format(A=A, B=B, C=C, n=n)
    answer = answer.format(D=D)
    comment = comment.format(A=A, B=B, C=C, D=D, k=k, n=n)

    return stem, answer, comment






































#6-2-4-47
def proandpro624_Stem_039():
    stem = "복사기는 $$수식$${A}$$/수식$$초에 $$수식$${B}$$/수식$$장을 복사할 수 있습니다. $$수식$${C}$$/수식$$장을 복사하려면 시간이 몇 초 걸리나요?\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$초\n"
    comment = "(해설)\n" \
              "$$수식$${C}$$/수식$$장을 복사하는 데 걸리는 시간을 □초라 놓고 비례식을 세우면\n" \
              "$$수식$${A}$$/수식$$ : $$수식$${B} ` = `$$/수식$$ □ : $$수식$${C}$$/수식$$ 입니다.\n" \
              "→ $$수식$${A} TIMES {C} ` =  ` {B} TIMES $$/수식$$□, $$수식$${B} TIMES $$/수식$$ □$$수식$$` = ` {k}$$/수식$$, □ $$수식$$` = `{D}$$/수식$$\n" \
              "따라서 $$수식$${C}$$/수식$$장을 복사하는 데 걸리는 시간은 $$수식$${D}$$/수식$$초입니다.\n\n"


    while True:
        A = np.random.randint(1, 15)
        B = np.random.randint(1, 15)
        if gcd(A, B) == 1:
            break

    while True:
        C = np.random.randint(30, 201)
        if C % B == 0:
            break

    D = A * int(C / B)
    k = A * C


    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(D=D)
    comment = comment.format(A=A, B=B, C=C, D=D, k=k)

    return stem, answer, comment
































#6-2-4-48
def proandpro624_Stem_040():
    stem = "태극기의 가로와 세로의 비는 $$수식$$3$$/수식$$ : $$수식$$2$$/수식$$입니다. 가로가 $$수식$${A} rm {{cm}}$$/수식$$인 태극기를 만들려면 세로는 몇 $$수식$$rm {{cm}}$$/수식$$로 해야 하나요?\n"
    answer = "(정답)\n$$수식$${B} rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "태극기의 세로를 □ $$수식$$rm {{cm}}$$/수식$$라 놓고 비례식을 세우면 $$수식$$3$$/수식$$ : $$수식$$2 ` = `{A} $$/수식$$ : □ 입니다.\n" \
              "→ $$수식$$3 TIMES $$/수식$$ □ $$수식$$` = ` 2 TIMES {A}$$/수식$$, $$수식$$3 TIMES $$/수식$$ □$$수식$$` = ` {k}$$/수식$$, □ $$수식$$` = ` {B}$$/수식$$\n" \
              "따라서 만들려고 하는 태극기의 세로는 $$수식$${B} rm {{cm}}$$/수식$$입니다.\n\n"


    a = np.random.randint(34, 167)
    A = 3 * a
    B = 2 * a
    k = 2 * A

    stem = stem.format(A=A)
    answer = answer.format(B=B)
    comment = comment.format(A=A, B=B, k=k)

    return stem, answer, comment




































#6-2-4-49
def proandpro624_Stem_041():
    stem = "두 친구가 나누어 가진 구슬 수의 비는 $$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$$입니다. 더 많이 가진 친구의 구슬 수가 $$수식$${C}$$/수식$$개라면 더 적게 가진 친구의 구슬 수는 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$개\n"
    comment = "(해설)\n" \
              "더 적게 가진 친구의 구슬 수를 □개라 놓고 비례식을 세우면 $$수식$${A}$$/수식$$ : $$수식$${B} ` = ` $$/수식$$ □ : $$수식$${C}$$/수식$$입니다.\n" \
              "→ $$수식$${A} TIMES {C} ` = ` {B} TIMES$$/수식$$□, $$수식$${B} TIMES $$/수식$$ □ $$수식$$` = `{k}$$/수식$$, □ $$수식$$` = ` {D}$$/수식$$\n" \
              "따라서 더 적게 가진 친구의 구슬 수는 $$수식$${D}$$/수식$$개입니다.\n\n"


    while True:
        B = np.random.randint(2, 11)
        A = np.random.randint(1, B)
        if gcd(A, B) == 1:
            break

    while True:
        C = np.random.randint(20, 71)
        if C % B == 0:
            break

    D = A * int(C / B)
    k = A * C


    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(D=D)
    comment = comment.format(A=A, B=B, C=C, D=D, k=k)

    return stem, answer, comment




































#6-2-4-50
def proandpro624_Stem_042():
    stem = "{T}는 {S}에서 $$수식$${n}$$/수식$$일 동안 일하고 $$수식$${A}$$/수식$$원을 받았습니다. {T}가 {S}에서 $$수식$${m}$$/수식$$일 동안 일하면 얼마를 받을 수 있나요?\n"
    answer = "(정답)\n$$수식$${B}$$/수식$$원\n"
    comment = "(해설)\n" \
              "$$수식$${m}$$/수식$$일 동안 일하고 받을 수 있는 돈을 □원이라 놓고 비례식을 세우면\n" \
              "$$수식$${n}$$/수식$$ : $$수식$${m} ` = ` {A} $$/수식$$ : □ 입니다.\n" \
              "→ $$수식$${n} TIMES$$/수식$$ □ $$수식$$` = ` {m} TIMES {A}$$/수식$$, $$수식$${n} TIMES $$/수식$$ □ $$수식$$` = ` {k}$$/수식$$, □ $$수식$$` = ` {B}$$/수식$$\n" \
              "따라서 {T}가 {S}에서 $$수식$${m}$$/수식$$일 동안 받을 수 있는 돈은 $$수식$${B}$$/수식$$원입니다.\n\n"


    T = random.choice(["성규", "종현이", "우리", "진영이"])
    S = random.choice(["서점", "카페", "가게"])
    n = random.randint(2, 5)
    m = random.randint(5, 16)

    while True:
        a = random.randint(100, 201)
        A = 1000 * a
        if A % n == 0:
            break

    q = int(A / n)
    B = m * q
    k = m * A


    stem = stem.format(T=T, S=S, A=A, m=m, n=n)
    answer = answer.format(B=B)
    comment = comment.format(m=m, n=n, A=A, k=k, B=B, T=T, S=S)

    return stem, answer, comment





































#6-2-4-51
def proandpro624_Stem_043():
    stem = "직사각형의 가로가 $$수식$${C} rm {{cm}}$$/수식$$이고 가로와 세로의 비가 $$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$$일 때, 직사각형의 넓이는 몇 $$수식$$rm {{cm}}^2$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${P} rm {{cm}}^2$$/수식$$\n"
    comment = "(해설)\n" \
              "직사각형의 세로를 □$$수식$$rm {{cm}}$$/수식$$라 놓고 비례식을 세우면 $$수식$${A}$$/수식$$ : $$수식$${B} ` = ` {C} $$/수식$$ : □ 입니다.\n" \
              "→ $$수식$${A} TIMES $$/수식$$ □ $$수식$$` = ` {B} TIMES {C}$$/수식$$, $$수식$${A} TIMES $$/수식$$ □ $$수식$$` = ` {k}$$/수식$$, □ $$수식$$` = ` {D}$$/수식$$\n" \
              "따라서 직사각형의 넓이는 $$수식$${C} TIMES {D} ` = `{P} LEFT ( rm {{cm}}^2 RIGHT ) $$/수식$$입니다.\n\n"


    while True:
        A = np.random.randint(1, 11)
        B = np.random.randint(1, 11)
        if gcd(A, B) == 1:
            break

    while True:
        C = np.random.randint(1, 31)
        if C % A == 0:
            break

    D = B * int(C / A)
    k = B * C
    P = C * D


    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(P=P)
    comment = comment.format(A=A, B=B, C=C, D=D, k=k, P=P)

    return stem, answer, comment






































#6-2-4-52
def proandpro624_Stem_044():
    stem = "맞물려 돌아가는 두 톱니바퀴 ㉮, ㉯가 있습니다. 톱니바퀴 ㉮의 톱니 수는 $$수식$${A}$$/수식$$개이고, 톱니바퀴 ㉯의 톱니 수는 $$수식$${B}$$/수식$$개입니다. $$수식$${n}$$/수식$$분 동안 톱니바퀴 ㉯가 $$수식$${C}$$/수식$$바퀴 돈다면 톱니바퀴 ㉮는 몇 바퀴 돌게 되나요?\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$ 바퀴\n"
    comment = "(해설)\n" \
              "㉮의 톱니 수는 $$수식$${A}$$/수식$$개, ㉯의 톱니 수는 $$수식$${B}$$/수식$$개이므로 ㉮와 ㉯의 톱니 수의 비는 $$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$$입니다.\n" \
              "$$수식$${A}$$/수식$$ : $$수식$${B}$$/수식$$의 전항과 후항을 $$수식$${k}$$/수식$${ro1} 나누면 $$수식$${p}$$/수식$$ : $$수식$${q}$$/수식$${ga1} 됩니다.\n" \
              "㉮와 ㉯의 톱니 수의 비가 $$수식$${p}$$/수식$$ : $$수식$${q}$$/수식$$이므로 $$수식$${n}$$/수식$$분 동안 도는 회전 수의 비는 $$수식$${q}$$/수식$$ : $$수식$${p}$$/수식$$입니다.\n" \
              "$$수식$${n}$$/수식$$분 동안 톱니바퀴 ㉮가 □ 바퀴 돈다고 하면\n" \
              "$$수식$${q}$$/수식$$ : $$수식$${p} ` = `$$/수식$$ □ : $$수식$${C}$$/수식$$\n" \
              "→ $$수식$${q} TIMES {C} ` = ` {p} TIMES $$/수식$$ □, $$수식$${p} TIMES $$/수식$$ □ $$수식$$` = ` {l}$$/수식$$, □ $$수식$$` = ` {D}$$/수식$$\n" \
              "따라서 $$수식$${n}$$/수식$$분 동안 톱니바퀴 ㉮는 $$수식$${D}$$/수식$$바퀴 돌게 됩니다.\n\n"


    k = np.random.randint(2, 10)

    while True:
        p = np.random.randint(1, 11)
        q = np.random.randint(1, 11)
        if gcd(p, q) == 1:
            break

    n = np.random.randint(1, 6)
    A = p * k
    B = q * k

    while True:
        C = np.random.randint(1, 31)
        if C % p == 0:
            break

    D = q * int(C / p)
    l = q * C

    ro1 = get_josa(k, "로")
    ga1 = get_josa(q, "가")


    stem = stem.format(A=A, B=B, n=n, C=C)
    answer = answer.format(D=D)
    comment = comment.format(A=A, B=B, p=p, q=q, l=l, C=C, D=D, n=n, k=k, ro1=ro1, ga1=ga1)

    return stem, answer, comment






































#6-2-4-53
def proandpro624_Stem_045():
    stem = "{T}네 반 전체 학생의 $$수식$${A}$$/수식$$%가 {S}{rur1} 좋아합니다. {S}{rur1} 좋아하는 학생이 $$수식$${B}$$/수식$$명이라면 {T}네 반 전체 학생은 몇 명인가요?\n"
    answer = "(정답)\n$$수식$${C}$$/수식$$명\n"
    comment = "(해설)\n" \
              "{T}네 반 전체 학생을 □명이라 놓고 비례식을 세우면 $$수식$$100$$/수식$$ : □ $$수식$$` = `{A}$$/수식$$ : $$수식$${B}$$/수식$$입니다.\n" \
              "→ $$수식$$100 TIMES {B} ` = ` $$/수식$$ □ $$수식$$TIMES {A}$$/수식$$ , □ $$수식$$TIMES {A} `=`{k}$$/수식$$, □ $$수식$$` = ` {C}$$/수식$$\n" \
              "따라서 {T}네 반 전체 학생은 $$수식$${C}$$/수식$$명입니다.\n\n"


    T = random.choice(["정호", "승철이", "미연이", "정한이"])
    S = random.choice(["축구", "미술", "수학", "영어"])

    ff = factor(100)


    while True:
        C = np.random.randint(20, 41)
        B = np.random.randint(1, C)
        kk = gcd(B, C)

        if B / kk in ff and C / kk in ff:
            break

    A = int((B / C) * 100)
    k = 100 * B

    rur1 = proc_jo(S, 1)


    stem = stem.format(T=T, S=S, B=B, A=A, rur1=rur1)
    answer = answer.format(C=C)
    comment = comment.format(A=A, B=B, C=C, k=k, T=T)

    return stem, answer, comment


































#6-2-4-54
def proandpro624_Stem_046():
    stem = "길이가 $$수식$${A} rm {{cm}}$$/수식$$인 리본을 주어진 비로 나누려고 합니다. 나누어진 두 리본의 길이는 각각 몇 $$수식$$rm {{cm}}$$/수식$$가 되는지 구하려고 합니다. □ 안에 알맞은 수를 써넣으세요.\n$$수식$${p}$$/수식$$ : $$수식$${q}$$/수식$$ → $$수식$${boxone} rm {{cm}}$$/수식$$, $$수식$${boxone} rm {{cm}}$$/수식$$\n"
    answer = "(정답)\n$$수식$${B}$$/수식$$, $$수식$${C}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A} TIMES {p} over {pq} ` = ` {A} TIMES {p} over {k}` = ` {B} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n" \
              "$$수식$${A} TIMES {q} over {pq} ` = ` {A} TIMES {q} over {k}` = ` {C} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n\n"


    while True:
        p = np.random.randint(1, 11)
        q = np.random.randint(1, 11)
        if gcd(p, q) == 1:
            break

    pq = "{%d ` + `  %d}" % (p, q)

    k = p + q

    while True:
        A = np.random.randint(30, 101)
        if A % k == 0:
            break

    B = int((A * p) / k)
    C = int((A * q) / k)

    boxone = "□"


    stem = stem.format(A=A, p=p, q=q, boxone=boxone)
    answer = answer.format(B=B, C=C)
    comment = comment.format(A=A, B=B, p=p, q=q, k=k, C=C, pq=pq)

    return stem, answer, comment


































#6-2-4-56
def proandpro624_Stem_047():
    stem = "나무 $$수식$${A}$$/수식$$그루를 {T}{gwa1} {S}에 $$수식$${p} : {q}$$/수식$${ro1} 나누어 심었습니다. {T}{gwa1} {S}에 심은 나무는 각각 몇 그루 인가요?\n" \
        "{T} : $$수식$${boxblank}$$/수식$$, {S} : $$수식$${boxblank}$$/수식$$"
    answer = "(정답)\n$$수식$${B}$$/수식$$그루, $$수식$${C}$$/수식$$그루\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${T}$$수식$$RIGHT ) ` =  {A} TIMES {p} over {pq} ` = ` {A} TIMES {p} over {k}` = ` {B} ` LEFT ($$/수식$$그루$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${S}$$수식$$RIGHT ) ` =  {A} TIMES {q} over {pq} ` = ` {A} TIMES {q} over {k}` = ` {C} ` LEFT ($$/수식$$그루$$수식$$RIGHT )$$/수식$$\n\n"


    ts = random.sample(["공원", "호수", "학교", "도서관"], 2)

    T = ts[0]
    S = ts[1]

    while True:
        p = np.random.randint(1, 11)
        q = np.random.randint(1, 11)
        if gcd(p, q) == 1:
            break


    pq = "{%d ` + `  %d}" % (p, q)

    k = p + q

    while True:
        A = np.random.randint(50, 301)
        if A % k == 0:
            break

    B = int(A * p / k)
    C = int(A * q / k)

    gwa1 = proc_jo(T, 2)
    ro1 = get_josa(q, "로")

    boxblank = "BOX{　　}"
    
    stem = stem.format(A=A, T=T, S=S, p=p, q=q, gwa1=gwa1, ro1=ro1, boxblank=boxblank)
    answer = answer.format(B=B, C=C, T=T, S=S)
    comment = comment.format(A=A, B=B, C=C, p=p, q=q, k=k, T=T, S=S, pq=pq)

    return stem, answer, comment




































#6-2-4-57
def proandpro624_Stem_048():
    stem = "종이학 $$수식$${A}$$/수식$$개를 {S}와 {T}가 $$수식$${p} : {q}$$/수식$${ro1} 나누어 접었습니다. {T}는 {S}보다 종이학을 몇 개 더 많이 접었나요?\n"
    answer = "(정답)\n$$수식$${D}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${S}$$수식$$RIGHT ) ` = ` {A} TIMES {p} over {pq} ` = ` {A} TIMES {p} over {k}` = ` {B} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${T}$$수식$$RIGHT ) ` = ` {A} TIMES {q} over {pq} ` = ` {A} TIMES {q} over {k}` = ` {C} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 {S}가 {T}보다 $$수식$${B} ` - ` {C} ` = ` {D} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$ 더 많이 접었습니다.\n\n"


    ts = random.sample(["민규", "영호", "정수", "수진이"], 2)

    T = ts[0]
    S = ts[1]


    while True:
        p = np.random.randint(1, 11)
        q = np.random.randint(1, 11)
        if gcd(p, q) == 1 and p > q:
            break

    pq = "{%d ` + `  %d}" % (p, q)

    k = p + q

    while True:
        A = np.random.randint(50, 201)
        if A % k == 0:
            break

    while True:
        B = int(A * p / k)
        C = int(A * q / k)
        if B > C:
            break

    D = B - C

    ro1 = get_josa(q, "로")


    stem = stem.format(A=A, S=S, T=T, p=p, q=q, ro1=ro1)
    answer = answer.format(D=D)
    comment = comment.format(A=A, B=B, p=p, q=q, C=C, D=D, k=k, S=S, T=T, pq=pq)

    return stem, answer, comment







































#6-2-4-58
def proandpro624_Stem_049():
    stem = "형과 {T}의 몸무게의 합은 $$수식$${A} rm kg$$/수식$$입니다. 형과 {T}의 몸무게의 비가 $$수식$${p} : {q}$$/수식$$ 일 때, 형의 몸무게는 몇 $$수식$$rm kg$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${B} ` rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$형$$수식$$RIGHT ) ` = ` {A} TIMES {p} over {pq} ` = ` {A} TIMES {p} over {k}` = ` {B} LEFT ( rm kg RIGHT )$$/수식$$\n\n"


    T = random.choice(["우진이", "동운이", "영민이"])

    while True:
        while True:
            p = np.random.randint(1, 11)
            q = np.random.randint(1, 11)
            if gcd(p, q) == 1:
                break

        pq = "{%d ` + `  %d}" % (p, q)

        k = p + q

        while True:
            A = np.random.randint(60, 141)
            if A % k == 0:
                break

        B = int(A * p / k)

        if B >= 30:
            break


    stem = stem.format(A=A, T=T, p=p, q=q)
    answer = answer.format(B=B)
    comment = comment.format(A=A, B=B, p=p, pq=pq, k=k)

    return stem, answer, comment




































#6-2-4-59
def proandpro624_Stem_050():
    stem = "넓이가 $$수식$${A} rm m^2$$/수식$$인 밭을 $$수식$${P} : {Q}$$/수식$${ro1} 나누어 {T}밭과 {S}밭으로 만들었습니다. {S}밭의 넓이는 몇 $$수식$$ rm m^2$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${B} rm m^2$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${P} : {Q} ` = ` LEFT ( {P} div {m} RIGHT ) : LEFT ( {Q} div {m} RIGHT ) ` = ` {p} : {q}$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${S}밭$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` {A} TIMES {q} over {pq} ` = ` {A} TIMES {q} over {k}` = ` {B} LEFT ( rm m^2 RIGHT )$$/수식$$\n" \
              "따라서 {S}밭의 넓이는 $$수식$${B} rm m^2$$/수식$$입니다.\n\n"


    ts = random.sample(["고추", "고구마", "무", "감자", "딸기"], 2)

    T = ts[0]
    S = ts[1]

    while True:
        p = np.random.randint(1, 11)
        q = np.random.randint(1, 11)
        if gcd(p, q) == 1 and p > q:
            break

    pq = "{%d ` + `  %d}" % (p, q)

    k = p + q

    while True:
        A = np.random.randint(1500, 5001)
        if A % k == 0:
            break


    B = int(A * q / k)
    m = np.random.randint(1, 31)

    P = p * m
    Q = q * m

    ro1= get_josa(Q, "로")


    stem = stem.format(A=A, S=S, Q=Q, P=P, T=T, ro1=ro1)
    answer = answer.format(B=B)
    comment = comment.format(P=P, Q=Q, m=m, p=p, q=q, A=A, B=B, S=S, pq=pq, k=k)

    return stem, answer, comment










































#6-2-4-60
def proandpro624_Stem_051():
    stem = "가로가 $$수식$${A} rm {{cm}} $$/수식$$, 세로가 $$수식$${B} rm {{cm}}$$/수식$$인 직사각형 모양의 도화지를 넓이의 비가 $$수식$${p} : {q}$$/수식$${ga1} 되도록 나누려고 합니다. 나누어진 두 개의 도화지 중 더 넓은 도화지의 넓이는 몇 $$수식$$rm {{cm}}^2$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${a1} rm {{cm}}^2$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$도화지의 넓이$$수식$$RIGHT ) ` = ` {A} TIMES {B} ` = ` {C} LEFT ( rm {{cm}}^2 RIGHT ) $$/수식$$\n" \
              "＊$$수식$${C} TIMES {p} over {pq} ` = ` {C} TIMES {p} over {k}` = ` {D} LEFT ( rm {{cm}}^2 RIGHT )$$/수식$$\n" \
              "＊$$수식$${C} TIMES {q} over {pq} ` = ` {C} TIMES {q} over {k}` = ` {E} LEFT ( rm {{cm}}^2 RIGHT )$$/수식$$\n" \
              "따라서 더 넓은 도화지의 넓이는 $$수식$${a1} rm {{cm}}^2$$/수식$$입니다.\n\n"


    while True:
        p = np.random.randint(1, 11)
        q = np.random.randint(1, 11)
        if gcd(p, q) == 1:
            break

    pq = "{%d ` + `  %d}" % (p, q)

    k = p + q

    while True:
        A = np.random.randint(10, 51)
        B = np.random.randint(10, 51)
        C = A * B
        if C % k == 0:
            break

    D = int(C * p / k)
    E = int(C * q / k)
    a1 = max(D, E)

    ga1 = get_josa(q, "가")


    stem = stem.format(A=A, B=B, p=p, q=q, ga1=ga1)
    answer = answer.format(a1=a1)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, p=p, q=q, pq=pq, k=k, a1=a1)

    return stem, answer, comment








































#6-2-4-62
def proandpro624_Stem_052():
    stem = "어느 날 낮과 밤의 길이의 비가 $$수식$${p} : {q}$$/수식$${ra1} 낮은 밤보다 몇 시간 더 긴지 구해보세요.\n"
    answer = "(정답)\n$$수식$${C}$$/수식$$시간\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$낮의 길이$$수식$$RIGHT ) ` = ` 24 TIMES {p} over {pq} ` = ` 24 TIMES {p} over {k}` = ` {A} ` LEFT ($$/수식$$시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$밤의 길이$$수식$$RIGHT ) ` = ` 24 TIMES {q} over {pq} ` = ` 24 TIMES {q} over {k}` = ` {B} ` LEFT ($$/수식$$시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${A} &gt; {B}$$/수식$$이므로\n" \
              "낮은 밤보다 $$수식$${A} ` - ` {B} ` = ` {C} ` LEFT ($$/수식$$시간$$수식$$RIGHT )$$/수식$$ 더 깁니다.\n\n"


    while True:
        p = np.random.randint(1, 11)
        q = np.random.randint(1, 11)
        k = p + q
        m = factor(24)

        if gcd(p, q) == 1 and p / q > 1 and p / q <= 2 and k in m:
            break

    pq = "{%d ` + `  %d}" % (p, q)

    A = int(24 * p / k)
    B = int(24 * q / k)
    C = A - B

    ra1 = get_josa(q, "라면")


    stem = stem.format(p=p, q=q, ra1=ra1)
    answer = answer.format(C=C)
    comment = comment.format(p=p, q=q, k=k, A=A, B=B, C=C, pq=pq)

    return stem, answer, comment






































#6-2-4-63
def proandpro624_Stem_053():
    stem = "{T}{yi}는 가지고 있던 연필 $$수식$${A}$$/수식$$자루 중 일부를 {S}에게 주었습니다. {S}{ga1} 받은 연필 수가 {T}에게 남아 있는 연필 수의 $$수식$${k}$$/수식$$배라면 {S}{eun1} 연필 몇 자루를 받은 것인가요?\n"
    answer = "(정답)\n$$수식$${B}$$/수식$$자루\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${T}$$수식$$RIGHT )$$/수식$$ : $$수식$$LEFT ($$/수식$${S}$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` 1 : {k} ` = ` LEFT (1 TIMES 10 RIGHT ) : LEFT ({k} TIMES 10 RIGHT ) ` = ` 10 : {K}$$/수식$$\n" \
              "$$수식$$` = ` LEFT (10 div {m} RIGHT ) : LEFT ( {K} div {m} RIGHT ) ` = ` {p} : {q}$$/수식$$\n" \
              "→ $$수식$$LEFT ($$/수식$${S}{ga1} 받은 연필 수$$수식$$RIGHT ) ` = ` {A} TIMES {q} over {pq} ` = ` {B} ` LEFT ($$/수식$$자루$$수식$$RIGHT )$$/수식$$\n\n"


    T = random.choice(["영우", "승관", "민호"])
    S = random.choice(["형", "친구", "동생"])

    yi = ""
    if T == "승관":
        yi = "이"

    while True:
        kk = np.random.randint(2, 51)

        if kk % 10 == 0:
            continue

        k = kk / 10
        k = round(k, 1)

        K = int(10 * k)
        m = gcd(10, K)

        if m == 1:
            continue

        p = int(10 / m)
        q = int(K / m)
        A = np.random.randint(10, 41)
        ppq = p + q

        if A % ppq == 0:
            break

    B = int(A * q / ppq)
    pq = "{%d ` + `  %d}" % (p, q)

    ga1 = proc_jo(S, 0)
    eun1 = proc_jo(S, -1)


    stem = stem.format(A=A, S=S, k=k, T=T, ga1=ga1, eun1=eun1, yi=yi)
    answer = answer.format(B=B)
    comment = comment.format(T=T, S=S, A=A, B=B, m=m, q=q, p=p, k=k, K=K, pq=pq, ga1=ga1)

    return stem, answer, comment




































#6-2-4-64
def proandpro624_Stem_054():
    stem = "{T}가 {R}을 사서 $$수식$${n}$$/수식$$개를 먹고, 남은 것을 {S}와 {V}가 $$수식$${p} : {q}$$/수식$${ro1} 나누었더니 {V}가 $$수식$${m}$$/수식$$개를 가지게 되었습니다. {T}가 산 {R}은 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${B}$$/수식$$개\n"
    comment = "(해설)\n" \
              "{T}가 먹고 남은 {R}의 개수를 □ 개라고 하면\n" \
              "□$$수식$$TIMES {q} over {pq} ` = `  □ ` TIMES {q} over {k} ` = ` {m}$$/수식$$\n" \
              "□$$수식$$` = ` {m} div {q} over {k} ` = ` {m} TIMES {k} over {q} ` = ` {A} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${T}가 산 {R}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$$먹고 남은 {R}의 수$$수식$$RIGHT ) + LEFT ($$/수식$$먹은 {R}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {A} + {n} ` = ` {B} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"


    tsv = random.sample(["동우", "두준이", "나연이", "영수", "진석이", "소진이"], 3)

    T = tsv[0]
    S = tsv[1]
    V = tsv[2]

    R = random.choice(["초콜릿", "사탕", "캐러맬"])


    while True:
        p = np.random.randint(1, 11)
        q = np.random.randint(1, 11)
        k = p + q
        m = np.random.randint(1, 31)

        if m % q == 0 and soroso(p, q):
            break

    A = int(m * k / q)
    n = np.random.randint(1, 16)
    B = A + n

    pq = "{%d ` + `  %d}" % (p, q)

    ro1 = get_josa(q, "로")


    stem = stem.format(T=T, R=R, S=S, V=V, p=p, q=q, n=n, m=m, ro1=ro1)
    answer = answer.format(B=B)
    comment = comment.format(A=A, B=B, n=n, p=p, q=q, k=k, m=m, T=T, R=R, pq=pq)

    return stem, answer, comment






