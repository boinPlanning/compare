import numpy as np
import codecs
import os
import random
import copy
import fractions




PATH = '/home/boin-service/Visang/Dictionary/'



person_nam = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XY.txt'), 'r', 'utf-8').readlines()]
person_yeo = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XX.txt'), 'r', 'utf-8').readlines()]



have_jongsung_num = [0, 1, 3, 6, 7, 8]
multiple_choice_jaem = {0: '㉠', 1: '㉡', 2: '㉢', 3: '㉣', 4: '㉤'}
multiple_choice_jaem_2 = {0: 'ㄱ', 1: 'ㄴ', 2: 'ㄷ', 3: 'ㄹ'}
multiple_choice_nums = {0: '①', 1: '②', 2: '③', 3: '④', 4: '⑤'}




box = "□"
box_1 = "①"
box_2 = "②"
box_a = '㉠'
box_b = '㉡'
box_j1 = '[㉠]'
box_j2 = '[㉡]'
left = '&gt;'
right = '&lt;'
equal = '='





def num_josa(number):
    '''
    숫자 뒤에 오는 조사 설정
    :param number: 숫자
    :return: 조사
    '''
    have_jongsung_num = ['0', '1', '3', '6', '7', '8']
    have_euro_num = ['1', '7', '8']

    try:
        mention = number.mention
    except:
        mention = str(number)

    if mention[-1] in have_jongsung_num:
        if mention[-1] in have_euro_num:
            return ["과", "은", "을", "이", "로"]
        else:
            return ["과", "은", "을", "이", "으로"]
    else:
        return ["와", "는", "를", "가", "로"]












# 서로소
def is_gcd(num1, num2):
    x, y = abs(num1), abs(num2)
    if x != y:
        while 1:
            r = x % y
            if r == 0:
                break
            x, y = y, r
        if y == 1:
            return True
    return False















# 최소공배수
def least_common_multiple(num1, num2):
    if num1 > num2:
        lcm = num1
    else:
        lcm = num2
    while lcm:
        if lcm % num1 == 0 and lcm % num2 == 0:
            break
        lcm += 1
    return lcm

















# 약분
def reduce(num1, num2):
    x, y = abs(num1), abs(num2)
    commonDivisor = 2
    if x > y:
        while commonDivisor <= abs(num2):
            if x % commonDivisor == 0 and y % commonDivisor == 0:
                x, y = int(x / commonDivisor), int(y / commonDivisor)
            else:
                commonDivisor += 1
    else:
        while commonDivisor <= abs(num1):
            if x % commonDivisor == 0 and y % commonDivisor == 0:
                x, y = int(x / commonDivisor), int(y / commonDivisor)
            else:
                commonDivisor += 1
    return x, y











# 최대공약수
def gcd(num1, num2):
    x, y = abs(num1), abs(num2)
    commonDivisor = 2
    if x > y:
        while commonDivisor <= abs(num2):
            if x % commonDivisor == 0 and y % commonDivisor == 0:
                x, y = int(x / commonDivisor), int(y / commonDivisor)
            else:
                commonDivisor += 1
    else:
        while commonDivisor <= abs(num1):
            if x % commonDivisor == 0 and y % commonDivisor == 0:
                x, y = int(x / commonDivisor), int(y / commonDivisor)
            else:
                commonDivisor += 1
    return commonDivisor












def postposition(num, flag=0):
    num = abs(num)
    # 조사 이, 가
    if flag == 0:
        if num in [2, 4, 5, 9]:
            return '가'
        return '이'
    # 조사 을, 를
    if flag == 1:
        if num in [2, 4, 5, 9]:
            return '를'
        return '을'
    # 조사 와, 과
    elif flag == 2:
        if num in [2, 4, 5, 9]:
            return '와'
        return '과'
    # 조사 로, 으로
    elif flag == 3:
        if num in [2, 4, 5, 7, 8, 9]:
            return '로'
        return '으로'
    # 조사 라고, 이라고
    elif flag == 4:
        if num in [2, 4, 5, 9]:
            return '라고'
        return '이라고'
    # 조사 은, 는
    else:
        if num in [2, 4, 5, 9]:
            return '는'
        return '은'






def get_josa(a, b):
    nobachim_list = ["2", "4", "5", "9"]
    ro_uro_list = ["0", "3", "6"]

    if b == "가" or b == "이":
        if (str(a))[-1] in nobachim_list:
            return "가"
        else:
            return "이"

    elif b == "를" or b == "을":
        if (str(a))[-1] in nobachim_list:
            return "를"
        else:
            return "을"

    elif b == "로" or b == "으로":
        if (str(a))[-1] in ro_uro_list:
            return "으로"
        else:
            return "로"














def check_jongsung(number):
    '''
    숫자 뒤에 오는 조사 설정
    :param number: 숫자
    :return: 조사
    '''
    have_jongsung_num = ['0', '1', '3', '6', '7', '8']

    try:
        mention = number.mention
    except:
        mention = str(number)

    if mention[-1] in have_jongsung_num:
        return ["과", "은", "을", "이", '으로']
    else:
        return ["와", "는", "를", "가", '로']












# 조사 확인(이름 뒤)
def josa_check(name):
    JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                     'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    char_code = ord(name) - 44032
    ch1 = int(char_code / 588)
    ch2 = int((char_code - (588 * ch1)) / 28)
    ch3 = int((char_code - (588 * ch1) - (28 * ch2)))

    return JONGSUNG_LIST[ch3]













# 최대공약수
def get_gcd(num1, num2):
    num1, num2 = sorted([num1, num2])
    gcd = 1
    for i in range(num1, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
            break

    return gcd














# 최소공배수
def get_lcm(num1, num2):
    return num1 * num2 // get_gcd(num1, num2)











# 기약분수 여부 확인
def check_simFrac(num1, num2):
    if get_gcd(num1, num2) == 1:
        return True
    else:
        return False





def get_soroso(a, b):
    while True:
        rest_ab = max(a, b) % min(a, b)
        a = min(a, b)
        b = rest_ab
        if rest_ab == 0 or rest_ab == 1:
            break

    return rest_ab








def soroso_select(a):
    if yaksu_count(a) < 3:
        return 1

    result_list = []

    for v_dx in range(1, a):
        if get_soroso(v_dx, a):
            result_list.append(v_dx)

    candidate_list = random.sample(result_list, 1)

    result_one = candidate_list[0]

    return result_one














def get_giyak(a, b):
    boon_su = fractions.Fraction(a, b)
    boon_ja = boon_su.numerator
    boon_mo = boon_su.denominator
    return boon_ja, boon_mo












def yaksu_count(a):

    yaksu_list = []

    for i_dx in range(1, a + 1):
        if a % i_dx == 0:
            yaksu_list.append(i_dx)

    final_result = len(yaksu_list)

    return final_result








def yaksu_list(a):

    result_list = []

    for s_dx in range(1, a + 1):
        if a % s_dx == 0:
            result_list.append(s_dx)

    return result_list






def not_yaksu_list(a):

    result_list = []

    for t_dx in range(2, a):
        if a % t_dx != 0:
            result_list.append(t_dx)

    return result_list


















# 5-1-5-02
def fractionaddsub515_Stem_001():
    stem = "다음이 나타내는 수를 구해 보세요.\n$$표$$$$수식$${f1}$$/수식$$보다 $$수식$${f2}$$/수식$$만큼 더 큰 수$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${c1}$$/수식$$\n\n"


    flag = True
    while flag:
        c, d, e = np.random.choice(np.arange(2, 8), 3)
        if get_gcd(d, e) == 1 and c * d * e <= 99:

            A = c * d
            B = c * e
            C = c * d * e
            a = np.random.randint(1, A, 1)[0]
            b = np.random.randint(1, B, 1)[0]
            f1 = '{%d} over {%d}' % (a, A)
            f2 = '{%d} over {%d}' % (b, B)

            if get_gcd(a, A) == 1 and get_gcd(b, B) == 1 and a + b < C and f1 != f2:
                a1 = a * e
                b1 = b * d
                D = a1 + b1
                n = get_gcd(C, D)
                C1 = C // n
                D1 = D // n

                if C1 == C and D1 < C1:
                    flag = False

    cor_frac = '{%d} over {%d}' % (D1, C1)
    c1 = '%s `+` %s `=` {%d} over {%d} `+` {%d} over {%d} `=` %s' % (f1, f2, a1, C, b1, C, cor_frac)


    stem = stem.format(f1=f1, f2=f2)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(c1=c1)

    return stem, answer, comment





































# 5-1-5-03
def fractionaddsub515_Stem_002():
    stem = "두 분모의 곱을 공통분모로 통분하여 계산하여 보세요.\n$$표$$$$수식$${f1} `+` {f2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${c1}$$/수식$$\n\n"


    flag = True
    while flag:
        A, B = np.random.choice(np.arange(2, 16), 2)
        C = A * B
        if get_gcd(A, B) == 1 and 12 <= C <= 99:
            a = np.random.randint(1, A, 1)[0]
            b = np.random.randint(1, B, 1)[0]
            a1 = a * B
            b1 = b * A
            D = a1 + b1
            if get_gcd(a, A) == 1 and get_gcd(b, B) == 1 and D < C and get_gcd(C, D) == 1:
                f1 = '{%d} over {%d}' % (a, A)
                f2 = '{%d} over {%d}' % (b, B)
                if f1 != f2:
                    flag = False

    cor_frac = '{%d} over {%d}' % (D, C)
    c1 = '%s `+` %s `=` {%d} over {%d} `+` {%d} over {%d} `=` %s' % (f1, f2, a1, C, b1, C, cor_frac)


    stem = stem.format(f1=f1, f2=f2)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(c1=c1)

    return stem, answer, comment










































# 5-1-5-04
def fractionaddsub515_Stem_003():
    stem = "계산 결과를 비교하여 $$수식$${box}$$/수식$$ 안에 $$수식$${left}$$/수식$$, $$수식$${equal}$$/수식$$, $$수식$${right}$$/수식$$를 알맞게 써넣으세요.\n$$수식$${exp_1}~~{box}~~{exp_2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${cor_sign}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${exp_3}$$/수식$$,\n" \
              "$$수식$${exp_4}$$/수식$$\n" \
              "$$수식$${exp_5}$$/수식$$이므로 " \
              "$$수식$${exp_1}`{cor_sign}`{exp_2}$$/수식$$입니다.\n\n"



    while True:
        while True:
            p = np.random.randint(2, 4)
            h = np.random.randint(2, 8)
            i = np.random.randint(2, 8)
            k = np.random.randint(2, 8)
            j = k * p
            if get_soroso(i, k) and h * i <= 15 and h * k <= 14 and get_soroso(i, j):
                break

        A = h * i
        B = h * j
        C = h * k
        D = h * i

        a = soroso_select(A)
        b = soroso_select(B)
        c = soroso_select(C)
        d = soroso_select(D)

        M = h * i * j
        N1 = h * i * k


        a1 = a * j
        b1 = b * i
        c1 = c * i
        d1 = d * k

        if a1 + b1 >= M or c1 + d1 >= N1:
            continue

        m = a1 + b1
        n1 = c1 + d1
        n = n1 * p

        if (m / p) - 10 > n1 or (m / p) + 10 < n1 or get_soroso(M, m) == 0:
            continue


        f1 = '{%d} over {%d}' % (a, A)
        f2 = '{%d} over {%d}' % (b, B)
        f3 = '{%d} over {%d}' % (c, C)
        f4 = '{%d} over {%d}' % (d, D)

        break


    cor_sign = equal if m == n else right if m < n else left

    exp_1 = '%s `+` %s' % (f1, f2)
    exp_2 = '%s `+` %s' % (f3, f4)

    cor_f1 = '{%d} over {%d}' % (m, M)
    cor_f2 = '{%d} over {%d}' % (n, M)

    exp_3 = '%s `=` {%d} over {%d} `+` {%d} over {%d} `=` %s' % (exp_1, a1, M, b1, M, cor_f1)
    exp_4 = '%s `=` {%d} over {%d} `+` {%d} over {%d} `=` {%d} over {%d} `=` %s' % (exp_2, c1, N1, d1, N1, n1, N1, cor_f2)
    exp_5 = '%s `%s` %s' % (cor_f1, cor_sign, cor_f2)


    stem = stem.format(exp_1=exp_1, exp_2=exp_2, box=box, left=left, right=right, equal=equal)
    answer = answer.format(cor_sign=cor_sign)
    comment = comment.format(exp_1=exp_1, exp_2=exp_2, exp_3=exp_3, exp_4=exp_4, exp_5=exp_5, cor_sign=cor_sign)

    return stem, answer, comment






    # flag = True
    # while flag:
    #     p = np.random.choice([2, 3], 1)[0]
    #     h, i, j, k = np.random.choice(np.arange(2, 8), 4)
    #     A = h * i
    #     B = h * j
    #     C = h * k
    #     D = h * i
    #
    #     if get_gcd(i, k) == 1 and get_gcd(i, j) == 1 and A <= 15 and C <= 14:
    #         M = h * i * j
    #         N1 = h * i * k
    #         a = np.random.randint(1, A, 1)[0]
    #         b = np.random.randint(1, B, 1)[0]
    #         c = np.random.randint(1, C, 1)[0]
    #         d = np.random.randint(1, D, 1)[0]
    #         a1 = a * j
    #         b1 = b * i
    #         c1 = c * i
    #         d1 = d * k
    #         m = a1 + b1
    #         n1 = c1 + d1
    #         n = n1 * p
    #
    #         if M % N1 != 0 or n * N1 != n1 * M:
    #             continue
    #
    #         if get_gcd(a, A) == 1 and get_gcd(b, B) == 1 and get_gcd(c, C) == 1 and get_gcd(d, D) == 1 and m < M and n < M and n1 < N1 \
    #                 and (m // p) - 10 <= n1 <= (m // p) + 10:
    #             f1 = '{%d} over {%d}' % (a, A)
    #             f2 = '{%d} over {%d}' % (b, B)
    #             f3 = '{%d} over {%d}' % (c, C)
    #             f4 = '{%d} over {%d}' % (d, D)
    #             if len(set([f1, f2, f3, f4])) == 4:
    #                 flag = False




































# 5-1-5-07
def fractionaddsub515_Stem_004():
    stem = "계산 결과가 더 {stem_condition} 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${exp_1}$$/수식$$    ㉡ $$수식$${exp_2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_jaem}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${exp_3}$$/수식$$\n" \
              "㉡ $$수식$${exp_4}$$/수식$$\n" \
              "$$수식$${exp_5}$$/수식$$이므로 계산 결과가 더 {stem_condition} 것은 {cor_jaem}입니다.\n\n"


    stem_condition = np.random.choice(['작은', '큰'], 1)[0]

    flag = True
    while flag:
        B, C = np.random.choice(np.arange(2, 8), 2)
        if get_gcd(B, C) == 1:
            A = D = B * C
            a, d = np.random.choice(np.arange(1, A), 2, False)
            b = np.random.randint(1, B, 1)[0]
            c = np.random.randint(1, C, 1)[0]
            b1 = b * C
            c1 = c * B
            k = a + b1
            n = c1 + d
            if get_gcd(a, A) == 1 and get_gcd(b, B) == 1 and get_gcd(c, C) == 1 and get_gcd(d, D) == 1 and k > A and n > D \
                    and k != n and (k - 5) <= n <= (k + 5) and k < A * 2 and n < D * 2:
                flag = False

    cor_sign = right if k < n else left

    if stem_condition == '작은':
        cor_jaem = '㉠' if k < n else '㉡'
    else:
        cor_jaem = '㉡' if k < n else '㉠'

    exp_1 = '{%d} over {%d} `+` {%d} over {%d}' % (a, A, b, B)
    exp_2 = '{%d} over {%d} `+` {%d} over {%d}' % (c, C, d, D)

    cor_f1 = '1 {%d} over {%d}' % (k - A, A)
    cor_f2 = '1 {%d} over {%d}' % (n - D, D)

    exp_3 = '%s `=` {%d} over {%d} `+` {%d} over {%d} `=` {%d} over {%d} `=` %s' % (exp_1, a, A, b1, A, k, A, cor_f1)
    exp_4 = '%s `=` {%d} over {%d} `+` {%d} over {%d} $$/수식$$\n$$수식$$ `=` {%d} over {%d} `=` %s' % (exp_2, c1, D, d, D, n, D, cor_f2)
    exp_5 = '%s `%s` %s' % (cor_f1, cor_sign, cor_f2)


    stem = stem.format(exp_1=exp_1, exp_2=exp_2, stem_condition=stem_condition)
    answer = answer.format(cor_jaem=cor_jaem)
    comment = comment.format(exp_3=exp_3, exp_4=exp_4, exp_5=exp_5, cor_jaem=cor_jaem, stem_condition=stem_condition)

    return stem, answer, comment









































# 5-1-5-09
def fractionaddsub515_Stem_005():
    stem = "가장 큰 분수와 가장 작은 분수의 합을 구해 보세요.\n$$표$$$$수식$${frac_1}$$/수식$$    $$수식$${frac_2}$$/수식$$    $$수식$${frac_3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${frac_1}$$/수식$$, $$수식$${frac_2}$$/수식$$, $$수식$${frac_3}$$/수식$$의 크기를 비교하면\n" \
              "{exp_1} → {exp_2} → $$수식$${exp_3}$$/수식$$\n" \
              "따라서 가장 큰 분수는 $$수식$${frac_F}$$/수식$$이고, 가장 작은 분수는 $$수식$${frac_D}$$/수식$$이므로\n" \
              "$$수식$${exp_4}$$/수식$$입니다.\n\n"


    flag = True
    while flag:
        A, B = np.random.choice(np.arange(2, 8), 2, False)
        C = A * B
        a = np.random.randint(A // 2, A, 1)[0]
        b = np.random.randint(B // 2, B, 1)[0]
        c = np.random.randint(C // 2, C, 1)[0]
        if get_gcd(a, A) == 1 and get_gcd(b, B) == 1 and get_gcd(c, C) == 1:
            a1 = a * B
            b1 = b * A
            numers = [a1, b1, c]

            if len(set(numers)) == 3:
                frac_1 = '{%d} over {%d}' % (a, A)
                frac_2 = '{%d} over {%d}' % (b, B)
                frac_3 = '{%d} over {%d}' % (c, C)
                frac_4 = '{%d} over {%d}' % (a1, C)
                frac_5 = '{%d} over {%d}' % (b1, C)
                frac_6 = '{%d} over {%d}' % (c, C)

                D_dict = {a1: frac_1, b1: frac_2, c: frac_3}
                d = min(numers)
                f = max(numers)
                frac_D = D_dict.get(d)
                frac_F = D_dict.get(f)
                frac_E = D_dict.get(sorted(list(D_dict.keys()))[1])
                g = f + d
                h = g - C
                if h > 0 and get_gcd(h, C) == 1:
                    flag = False


    exp_1 = '$$수식$$LEFT ( %s$$/수식$$, $$수식$$%s$$/수식$$, $$수식$$%s RIGHT )$$/수식$$' % (frac_1, frac_2, frac_3)
    exp_2 = '$$수식$$LEFT ( %s$$/수식$$, $$수식$$%s$$/수식$$, $$수식$$%s RIGHT )$$/수식$$' % (frac_4, frac_5, frac_6)
    exp_3 = '%s `%s` %s `%s` %s' % (frac_D, right, frac_E, right, frac_F)

    
    cor_frac = '1 {%d} over {%d}' % (h, C)

    exp_4 = '%s `+` %s `=` {%d} over {%d} `+` {%d} over {%d} `=` {%d} over {%d} `=` %s' % (frac_F, frac_D, f, C, d, C, g, C, cor_frac)


    stem = stem.format(frac_1=frac_1, frac_2=frac_2, frac_3=frac_3)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, exp_1=exp_1, exp_2=exp_2, exp_3=exp_3,
                             exp_4=exp_4, frac_D=frac_D, frac_F=frac_F)

    return stem, answer, comment














































# 5-1-5-10
def fractionaddsub515_Stem_006():
    stem = "계산 결과가 $$수식$$1$$/수식$$보다 큰 것을 모두 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${exp_1}$$/수식$$    ㉡ $$수식$${exp_2}$$/수식$$\n \n㉢ $$수식$${exp_3}$$/수식$$    ㉣ $$수식$${exp_4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_jaem}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${exp_5}$$/수식$$\n" \
              "㉡ $$수식$${exp_6}$$/수식$$\n" \
              "㉢ $$수식$${exp_7}$$/수식$$\n" \
              "㉣ $$수식$${exp_8}$$/수식$$\n" \
              "따라서 계산 결과가 $$수식$$1$$/수식$$보다 큰 것은 {cor_jaem}입니다.\n\n"


    flag = True
    while flag:
        denoms = list(np.random.choice(np.arange(2, 16), 8))
        if len(set(denoms)) > 5:
            d1, d2, d3, d4, d5, d6, d7, d8 = denoms
            numers = [np.random.randint(1, d, 1)[0] for d in denoms]
            n1, n2, n3, n4, n5, n6, n7, n8 = numers
            if check_simFrac(n1, d1) and check_simFrac(n2, d2) and check_simFrac(n3, d3) and check_simFrac(n4, d4) \
                    and check_simFrac(n5, d5) and check_simFrac(n6, d6) and check_simFrac(n7, d7) and check_simFrac(n8, d8) \
                    and d1 != d2 and d3 != d4 and d5 != d6 and d7 != d8:

                b1, b2, b3, b4 = get_lcm(d1, d2), get_lcm(d3, d4), get_lcm(d5, d6), get_lcm(d7, d8)
                a1, a2, a3, a4, a5, a6, a7, a8 = numers * np.reshape(
                    [b1 // d1, b1 // d2, b2 // d3, b2 // d4, b3 // d5, b3 // d6, b4 // d7, b4 // d8], -1)
                c1, c2, c3, c4 = [a1, a3, a5, a7] + np.reshape([a2, a4, a6, a8], -1)

                values_dict = {0: [n1, d1, n2, d2, a1, a2, c1, b1], 1: [n3, d3, n4, d4, a3, a4, c2, b2],
                               2: [n5, d5, n6, d6, a5, a6, c3, b3], 3: [n7, d7, n8, d8, a7, a8, c4, b4]}
                cor_jaem = []
                for i, [a, b] in enumerate([[c1, b1], [c2, b2], [c3, b3], [c4, b4]]):
                    if a > b and a - b < b:
                        values_dict[i].append(a % b)
                        cor_jaem.append(multiple_choice_jaem.get(i))
                    else:
                        values_dict[i].append(0)

                if max([b1, b2, b3, b4]) < 50 and len(cor_jaem) == 2:
                    flag = False

    bogi, comments = [], []
    for _, v in values_dict.items():
        exp = '{%d} over {%d} `+` {%d} over {%d}' % (v[0], v[1], v[2], v[3])
        giyak_six, giyak_seven = get_giyak(v[6], v[7])
        com = '%s `=` {%d} over {%d} `+` {%d} over {%d} `=` {%d} over {%d}' % (exp, v[4], v[7], v[5], v[7], giyak_six, giyak_seven)
        giyak_boonja, giyak_boonmo = get_giyak(v[8], v[7])
        com += ' `=` 1 {%d} over {%d}' % (giyak_boonja, giyak_boonmo) if v[-1] != 0 else ''
        bogi.append(exp)
        comments.append(com)

    exp_1, exp_2, exp_3, exp_4 = bogi
    exp_5, exp_6, exp_7, exp_8 = comments
    cor_jaem = ', '.join(cor_jaem)


    stem = stem.format(exp_1=exp_1, exp_2=exp_2, exp_3=exp_3, exp_4=exp_4)
    answer = answer.format(cor_jaem=cor_jaem)
    comment = comment.format(exp_5=exp_5, exp_6=exp_6, exp_7=exp_7, exp_8=exp_8, cor_jaem=cor_jaem)

    return stem, answer, comment















































# 5-1-5-12
def fractionaddsub515_Stem_007():
    stem = "다음이 나타내는 수를 구해 보세요.\n$$표$$$$수식$${frac_1}$$/수식$$보다 $$수식$${frac_2}$$/수식$$ 큰 수$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${exp_1}$$/수식$$\n\n"


    flag = True
    while flag:
        p = np.random.randint(2, 6, 1)[0]
        q, r = np.random.choice(np.arange(2, 8), 2, False)
        A = p * q
        B = p * r
        a = np.random.randint(1, A, 1)[0]
        b = np.random.randint(1, B, 1)[0]
        A1 = p * q * r
        a1 = a * r
        b1 = b * q
        c = a1 + b1
        d = c - A1
        n = get_gcd(A1, d)
        A2 = A1 // n
        d1 = d // n

        if list(set([get_gcd(q, r), get_gcd(a, A), get_gcd(b, B)])) == [1] and max(A, B) <= 15 and c > A1 and d < A1 and check_simFrac(d, A1):
            flag = False

    frac_1 = '{%d} over {%d}' % (a, A)
    frac_2 = '{%d} over {%d}' % (b, B)
    cor_frac = '1 {%d} over {%d}' % (d, A1)

    exp_1 = '%s `+` %s `=` {%d} over {%d} `+` {%d} over {%d} `=` {%d} over {%d} `=` %s' % (frac_1, frac_2, a1, A1, b1, A1, c, A1, cor_frac)


    stem = stem.format(frac_1=frac_1, frac_2=frac_2)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(exp_1=exp_1)

    return stem, answer, comment

















































# 5-1-5-15
def fractionaddsub515_Stem_008():
    stem = "{t1}{j1}는 상자를 묶는 데 {t2}색 {t4} $$수식$${frac_1}`rm m$$/수식$$와 {t3}색 {t4} $$수식$${frac_2}`rm m$$/수식$$를 사용했습니다. {t1}{j1}가 사용한 {t4}{j4} 모두 몇 $$수식$$rm m$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${cor_frac} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${t1}{j1}가 사용한 " \
              "{t4}의 길이$$수식$$RIGHT )$$/수식$$ \n $$수식$$ ` = ` {exp_1} ` LEFT ( ` rm m ` RIGHT )$$/수식$$\n\n"


    t1 = np.random.choice(person_nam + person_yeo, 1)[0]
    j1 = '' if josa_check(t1[-1]) == ' ' else '이'
    t2, t3 = np.random.choice('빨간 파란 노란 초록 주황 연두 남 보라'.split(' '), 2, False)
    t4 = np.random.choice('끈 노끈 종이테이프 리본 테이프'.split(' '), 1)[0]
    j4 = '는' if josa_check(t4[-1]) == ' ' else '은'

    flag = True
    while flag:
        A, B = np.random.choice(np.arange(2, 16), 2, False)
        a = np.random.randint(1, A, 1)[0]
        b = np.random.randint(1, B, 1)[0]
        a1 = a * B
        b1 = b * A
        C = A * B
        c = a1 + b1
        d = c - C
        if [get_gcd(A, B), get_gcd(a, A), get_gcd(b, B)] == [1, 1, 1] and C <= 72 and 0 < d < C:
            flag = False

    frac_1 = '{%d} over {%d}' % (a, A)
    frac_2 = '{%d} over {%d}' % (b, B)
    # cor_frac = '1 {%d} over {%d}' % (d, C)

    giyak_boonja, giyak_boonmo = get_giyak(d, C)
    cor_frac = '1 {%d} over {%d}' % (giyak_boonja, giyak_boonmo)

    exp_1 = '%s `+` %s `=` {%d} over {%d} `+` {%d} over {%d} `=` {%d} over {%d} `=` %s' % (frac_1, frac_2, a1, C, b1, C, c, C, cor_frac)


    stem = stem.format(t1=t1, t2=t2, t3=t3, t4=t4, j1=j1, j4=j4, frac_1=frac_1, frac_2=frac_2)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(t1=t1, t4=t4, j1=j1, exp_1=exp_1)

    return stem, answer, comment


















































# 5-1-5-16
def fractionaddsub515_Stem_009():
    stem = "{t1}{j1}네 집에서 {t2}에 가려면 {t3}{j3} 지나야 합니다. {t1}{j1}네 집에서 {t3}까지는 $$수식$${frac_1}`rm {{km}}$$/수식$$이고, {t3}에서 {t2}까지는 $$수식$${frac_2}`rm {{km}}$$/수식$$입니다. {t1}{j1}네 집에서 {t2}까지의 거리가 $$수식$$1`rm {{km}}$$/수식$$보다 가까우면 걸어가고, $$수식$$1`rm {{km}}$$/수식$$가 넘으면 자전거를 타고 가려고 합니다. {t1}{j1}네 집에서 {t2}까지 어느 방법으로 가야 하나요?\n"
    answer = "(정답)\n{cor_text}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( {t1}{j1}네 집에서 {t2}까지의 거리 RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ( {t1}{j1}네 집에서 {t3}까지의 거리 RIGHT )$$/수식$$ \n $$수식$$ ` + ` LEFT ( {t3}에서 {t2}까지의 거리 RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {exp_1} LEFT ( rm {{km}} RIGHT )$$/수식$$\n" \
              "{t1}{j1}네 집에서 {t2}까지의 거리는 $$수식$$1 ` rm {{km}}$$/수식$$가\n {ans_text} 합니다.\n\n"


    t1 = np.random.choice(person_nam + person_yeo, 1)[0]
    j1 = '' if josa_check(t1[-1]) == ' ' else '이'
    t2, t3 = np.random.choice('병원 도서관 소방서 경찰서 우체국 지하철역 학교 공원 놀이터'.split(' '), 2, False)
    j3 = '를' if josa_check(t3[-1]) == ' ' else '을'

    flag = True
    while flag:
        B = np.random.randint(4, 16, 1)[0]
        p = np.random.choice([2, 3], 1)[0]
        A = B * p
        a = np.random.randint(1, A, 1)[0]
        b = np.random.randint(1, B, 1)[0]
        b1 = b * p
        a1 = a + b1
        n = get_gcd(A, a1)
        C = A // n
        a2 = a1 // n

        n1 = a2 - C if a2 - C > 0 else a2
        if [get_gcd(a, A), get_gcd(b, B)] == [1, 1] and C != a2 and a2 - C < C and check_simFrac(n1, C):
            flag = False
            ans_text = '넘으므로 자전거를 타고 가야' if a2 > C else '넘지 않으므로 걸어가야'
            cor_text = '자전거' if a2 > C else '걸어가기'

    frac_1 = '{%d} over {%d}' % (a, A)
    frac_2 = '{%d} over {%d}' % (b, B)
    exp_1 = '%s `+` %s `=` {%d} over {%d} `+` {%d} over {%d} `=` {%d} over {%d}' % (frac_1, frac_2, a, A, b1, A, a2, C)
    exp_1 += ' `=` 1 {%d} over {%d}' % (a2 - C, C) if a2 > C else ''


    stem = stem.format(t1=t1, t2=t2, t3=t3, j1=j1, j3=j3, frac_1=frac_1, frac_2=frac_2)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(t1=t1, t2=t2, t3=t3, j1=j1, exp_1=exp_1, ans_text=ans_text)

    return stem, answer, comment


















































# 5-1-5-20
def fractionaddsub515_Stem_010():
    stem = "가장 큰 수와 가장 작은 수의 합을 기약분수로 나타내 보세요.\n$$표$$$$수식$${frac_1}$$/수식$$    $$수식$${frac_2}$$/수식$$    $$수식$${frac_3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "자연수 부분의 크기를 비교하면 가장 큰 수는 $$수식$${frac_4}$$/수식$$이고, 가장 작은 수는 $$수식$${frac_5}$$/수식$$입니다.\n" \
              "$$수식$${exp_1}$$/수식$$\n" \
              "따라서 가장 큰 수와 가장 작은 수의 합은 $$수식$${cor_frac}$$/수식$$입니다.\n\n"


    flag = True
    while flag:
        s1, s4, s7 = sorted(list(np.random.choice(np.arange(1, 5), 3, False)))
        s3, s6, s9 = np.random.choice(np.arange(2, 16), 3)
        s2 = np.random.randint(1, s3, 1)[0]
        s5 = np.random.randint(1, s6, 1)[0]
        s8 = np.random.randint(1, s9, 1)[0]
        if check_simFrac(s2, s3) and check_simFrac(s5, s6) and check_simFrac(s8, s9):
            s10 = get_lcm(s9, s3)
            s11 = s8 * (s10 // s9)
            s12 = s2 * (s10 // s3)
            s13 = s1 + s7
            s14 = s11 + s12

            if s10 <= 30 and s14 < s10 and get_gcd(s14, s10) != 1:
                s15 = s14 // get_gcd(s14, s10)
                s16 = s10 // get_gcd(s14, s10)
                flag = False

    frac_dict = {s1: '%d {%d} over {%d}' % (s1, s2, s3), s4: '%d {%d} over {%d}' % (s4, s5, s6),
                 s7: '%d {%d} over {%d}' % (s7, s8, s9)}

    answers = list(frac_dict.keys())
    np.random.shuffle(answers)

    frac_1, frac_2, frac_3 = [frac_dict.get(k) for k in answers]
    frac_4 = frac_dict.get(max(answers))
    frac_5 = frac_dict.get(min(answers))

    cor_frac = '%d {%d} over {%d}' % (s13, s15, s16)
    exp_1 = '%s `+` %s `=` %d {%d} over {%d} `+` %d {%d} over {%d} `=` %d {%d} over {%d} `=` %s' \
            % (frac_4, frac_5, s7, s11, s10, s1, s12, s10, s13, s14, s10, cor_frac)


    stem = stem.format(frac_1=frac_1, frac_2=frac_2, frac_3=frac_3)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(frac_4=frac_4, frac_5=frac_5, exp_1=exp_1, cor_frac=cor_frac)

    return stem, answer, comment
















































# 5-1-5-22
def fractionaddsub515_Stem_011():
    stem = "계산 결과를 비교하여 $$수식$${box}$$/수식$$ 안에 $$수식$${left}$$/수식$$, $$수식$${equal}$$/수식$$, $$수식$${right}$$/수식$$를 알맞게 써넣으세요.\n$$수식$${exp_1}~~{box}~~{exp_2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${cor_sign}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${exp_3}$$/수식$$\n" \
              "$$수식$${exp_4}$$/수식$$이므로 $$수식$${exp_5}$$/수식$$입니다.\n\n"


    flag = True
    while flag:
        a2, b2 = np.random.choice(np.arange(1, 5), 2)
        c2 = a2 + b2
        A, B = np.random.choice(np.arange(2, 16), 2, False)
        C = A * B

        if 10 > C or C > 75:
            continue

        a1 = soroso_select(A)
        b1 = soroso_select(B)
        c1 = soroso_select(C)

        d1 = a1 * B
        d2 = b1 * A
        d3 = d1 + d2
        d4 = a2 + b2
        cor_sign = equal if d3 == c1 else left if d3 > c1 else right

        if d3 < C and d3 - 5 <= c1 <= d3 + 5:
            flag = False


    exp_1 = '%d {%d} over {%d} `+` %d {%d} over {%d}' % (a2, a1, A, b2, b1, B)
    exp_2 = '%d {%d} over {%d}' % (c2, c1, C)
    frac_1 = '%d {%d} over {%d}' % (d4, d3, C)

    exp_3 = '%s `=` %d {%d} over {%d} `+` %d {%d} over {%d} `=` %s' % (exp_1, a2, d1, C, b2, d2, C, frac_1)
    exp_4 = '%s `%s` %s' % (frac_1, cor_sign, exp_2)
    exp_5 = '%s `%s` %s' % (exp_1, cor_sign, exp_2)


    stem = stem.format(exp_1=exp_1, exp_2=exp_2, box=box, left=left, right=right, equal=equal)
    answer = answer.format(cor_sign=cor_sign)
    comment = comment.format(exp_3=exp_3, exp_4=exp_4, exp_5=exp_5)

    return stem, answer, comment





    # flag = True
    # while flag:
    #     a2, b2 = np.random.choice(np.arange(1, 5), 2)
    #     c2 = a2 + b2
    #     A, B = np.random.choice(np.arange(2, 16), 2, False)
    #     C = A * B
    #     a1 = np.random.randint(1, A, 1)[0]
    #     b1 = np.random.randint(1, B, 1)[0]
    #     c1 = np.random.randint(1, C, 1)[0]
    #     d1 = a1 * B
    #     d2 = b1 * A
    #     d3 = d1 + d2
    #     d4 = a2 + b2
    #     cor_sign = equal if d3 == c1 else left if d3 > c1 else right
    #
    #     if check_simFrac(a1, A) and check_simFrac(b1, B) and check_simFrac(c1, C) and 10 <= C <= 75 and d3 < C and d3 - 5 <= c1 <= d3 + 5:
    #         flag = False















































# 5-1-5-24
def fractionaddsub515_Stem_012():
    stem = "{t3}{j3} {t1}{j1}는 $$수식$${frac_1}`rm m$$/수식$$, {t2}{j2}는 $$수식$${frac_2}`rm m$$/수식$$ 가지고 있습니다. {t1}{j1}와 {t2}{j2}가 가지고 있는 {t3}{j4} 모두 몇 $$수식$$rm m$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${cor_frac} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${t1}{j1}가 가지고 있는 {t3}의 길이$$수식$$RIGHT ) ` + ` LEFT ($$/수식$${t2}{j2}가 가지고 있는 {t3}의 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {exp_1} LEFT ( rm m RIGHT )$$/수식$$\n\n"


    terms = [np.random.choice(person_nam, 1)[0], np.random.choice(person_yeo, 1)[0]]
    np.random.shuffle(terms)
    t1, t2 = terms
    j1, j2 = ['' if josa_check(t[-1]) == ' ' else '이' for t in terms]
    t3 = np.random.choice('끈 철사 노끈 리본'.split(' '), 1)[0]
    j3 = '를' if josa_check(t3[-1]) == ' ' else '을'
    j4 = '는' if josa_check(t3[-1]) == ' ' else '은'

    flag = True
    while flag:
        a2, b2 = np.random.choice(np.arange(1, 5), 2)
        p, q, r = np.random.choice(np.arange(2, 8), 3)
        A = p * q
        B = p * r
        C = p * q * r
        if check_simFrac(q, r) and max(A, B) <= 21 and C < 100:
            a1 = np.random.randint(1, A, 1)[0]
            b1 = np.random.randint(1, B, 1)[0]
            a3 = a1 * r
            b3 = b1 * q
            c1 = a3 + b3
            c2 = a2 + b2
            n = get_gcd(C, c1)
            C1 = C // n
            c3 = c1 // n
            if c1 < C and check_simFrac(A, a1) and check_simFrac(B, b1):
                flag = False

    frac_1 = '%d {%d} over {%d}' % (a2, a1, A)
    frac_2 = '%d {%d} over {%d}' % (b2, b1, B)
    cor_frac = '%d {%d} over {%d}' % (c2, c3, C1)

    exp_1 = '%s `+` %s `=` %d {%d} over {%d} `+` %d {%d} over {%d} `=` %s' % (
    frac_1, frac_2, a2, a3, C, b2, b3, C, cor_frac)


    stem = stem.format(frac_1=frac_1, frac_2=frac_2, t1=t1, t2=t2, t3=t3, j1=j1, j2=j2, j3=j3, j4=j4)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(t1=t1, t2=t2, t3=t3, j1=j1, j2=j2, exp_1=exp_1)

    return stem, answer, comment


















































# 5-1-5-25
def fractionaddsub515_Stem_013():
    stem = "{t1}{j1}는 {t2} 페인트를 만들기 위해 {t3} 페인트 $$수식$${frac_1}`rm L$$/수식$$와 {t4} 페인트 $$수식$${frac_2}`rm L$$/수식$$를 섞었습니다. {t1}{j1}가 만든 {t2} 페인트는 모두 몇 $$수식$$rm L$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${cor_frac} rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${t3} 페인트의 양$$수식$$RIGHT ) ` + ` LEFT ($$/수식$${t4} 페인트의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {exp_1} LEFT ( rm L RIGHT )$$/수식$$\n\n"


    colors = ['회색 흰색 검은색', '분홍색 빨간색 흰색', '초록색 파란색 노란색', '보라색 빨간색 파란색', '주황색 노란색 빨간색', '하늘색 흰색 파란색']
    t1 = np.random.choice(person_nam + person_yeo, 1)[0]
    j1 = '' if josa_check(t1[-1]) == ' ' else '이'
    colors = colors[np.random.randint(0, len(colors), 1)[0]].split(' ')
    t2 = colors[0]
    t3, t4 = np.random.choice(colors[1:], 2, False)

    flag = True
    while flag:
        a2, b2 = np.random.choice(np.arange(1, 5), 2)
        p, q, r = np.random.choice(np.arange(2, 8), 3)
        A, B, C = [p, p, p] * np.reshape([q, r, q * r], -1)

        a1 = np.random.randint(1, A, 1)[0]
        b1 = np.random.randint(1, B, 1)[0]
        a3 = a1 * r
        b3 = b1 * q
        c1 = a3 + b3
        c2 = a2 + b2
        c3 = c1 - C
        c4 = c2 + 1
        n = get_gcd(C, c3)
        C1 = C // n
        c5 = c3 // n
        if max(A, B) <= 21 and C < 100 and c3 < C and c5 > 0:
            flag = False

    frac_1 = '%d {%d} over {%d}' % (a2, a1, A)
    frac_2 = '%d {%d} over {%d}' % (b2, b1, B)
    cor_frac = '%d {%d} over {%d}' % (c4, c5, C1)
    exp_1 = '%s `+` %s `=` %d {%d} over {%d} `+` %d {%d} over {%d} `=` %d {%d} over {%d} `=` %s' \
            '' % (frac_1, frac_2, a2, a3, C, b2, b3, C, c2, c1, C, cor_frac)


    stem = stem.format(t1=t1, t2=t2, t3=t3, t4=t4, j1=j1, frac_1=frac_1, frac_2=frac_2)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(t3=t3, t4=t4, exp_1=exp_1)

    return stem, answer, comment

























































# 5-1-5-27
def fractionaddsub515_Stem_014():
    stem = "계산 결과가 더 큰 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${exp_1}$$/수식$$    ㉡ $$수식$${exp_2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_jaem}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${exp_1} `=` {exp_3}$$/수식$$\n" \
              "㉡ $$수식$${exp_2} `=` {exp_4}$$/수식$$\n" \
              "→ $$수식$${exp_5}$$/수식$$ → $$수식$${exp_6}$$/수식$$ → $$수식$${exp_7}$$/수식$$\n" \
              "따라서 계산 결과가 더 큰 것은 {cor_jaem}입니다.\n\n"


    while True:
        while True:
            lcm_1 = np.random.randint(15, 85)
            lcm_2 = np.random.randint(15, 85)
            if yaksu_count(lcm_1) >= 4 and yaksu_count(lcm_2) >= 4:
                break

        s2, s4, s6 = random.sample(yaksu_list(lcm_1), 3)
        if 1 in [s2, s4, s6]:
            continue

        if least_common_multiple(least_common_multiple(s2, s4), s6) != lcm_1:
            continue

        s8, s10, s12 = random.sample(yaksu_list(lcm_2), 3)
        if 1 in [s8, s10, s12]:
            continue

        if least_common_multiple(least_common_multiple(s8, s10), s12) != lcm_2:
            continue


        s1 = soroso_select(s2)
        s3 = soroso_select(s4)
        s5 = soroso_select(s6)

        s7 = soroso_select(s8)
        s9 = soroso_select(s10)
        s11 = soroso_select(s12)


        s13 = s1 * int(lcm_1 / s2)
        s14 = s3 * int(lcm_1 / s4)
        s15 = s5 * int(lcm_1 / s6)

        big_head_boonja1 = s13 + s14 + s15

        s18 = s7 * int(lcm_2 / s8)
        s19 = s9 * int(lcm_2 / s10)
        s20 = s11 * int(lcm_2 / s12)

        big_head_boonja2 = s18 + s19 + s20

        res1_boonmo = lcm_1
        res1_boonja = big_head_boonja1 - lcm_1

        res2_boonmo = lcm_2
        res2_boonja = big_head_boonja2 - lcm_2

        if res1_boonja < 1 or res1_boonja >= res1_boonmo or res2_boonja < 1 or res2_boonja >= res2_boonmo:
            continue

        giyak_boonja1, giyak_boonmo1 = get_giyak(res1_boonja, res1_boonmo)
        giyak_boonja2, giyak_boonmo2 = get_giyak(res2_boonja, res2_boonmo)

        if giyak_boonmo1 == giyak_boonmo2:
            continue

        lcm_res = least_common_multiple(giyak_boonmo1, giyak_boonmo2)

        if lcm_res >= 100:
            continue

        boonja1 = giyak_boonja1 * int(lcm_res / giyak_boonmo1)
        boonja2 = giyak_boonja2 * int(lcm_res / giyak_boonmo2)

        if boonja1 == boonja2:
            continue

        elif boonja1 > boonja2:
            cor_sign = "&gt;"
            cor_jaem = "㉠"

        else:
            cor_sign = "&lt;"
            cor_jaem = "㉡"

        break



    frac_1 = '{%d} over {%d}' % (s1, s2)
    frac_2 = '{%d} over {%d}' % (s3, s4)
    frac_3 = '{%d} over {%d}' % (s5, s6)

    exp_1 = '%s `+` %s `+` %s' % (frac_1, frac_2, frac_3)

    if giyak_boonja1 == res1_boonja:
        exp_3 = '{%d} over {%d} `+` {%d} over {%d} `+` {%d} over {%d}$$/수식$$\n$$수식$$ `=` {%d} over {%d} `=` 1 {%d} over {%d}' % (s13, lcm_1, s14, lcm_1, s15, lcm_1, big_head_boonja1, res1_boonmo, res1_boonja, res1_boonmo)
    else:
        exp_3 = '{%d} over {%d} `+` {%d} over {%d} `+` {%d} over {%d}$$/수식$$\n$$수식$$ `=` {%d} over {%d} `=` 1 {%d} over {%d} `=` 1 {%d} over {%d}' % (s13, lcm_1, s14, lcm_1, s15, lcm_1, big_head_boonja1, res1_boonmo, res1_boonja, res1_boonmo, giyak_boonja1, giyak_boonmo1)

    frac_4 = '{%d} over {%d}' % (s7, s8)
    frac_5 = '{%d} over {%d}' % (s9, s10)
    frac_6 = '{%d} over {%d}' % (s11, s12)

    exp_2 = '%s `+` %s `+` %s' % (frac_4, frac_5, frac_6)

    if giyak_boonja2 == res2_boonja:
        exp_4 = '{%d} over {%d} `+` {%d} over {%d} `+` {%d} over {%d}$$/수식$$\n$$수식$$`=` {%d} over {%d} `=` 1 {%d} over {%d}' % (s18, lcm_2, s19, lcm_2, s20, lcm_2, big_head_boonja2, res2_boonmo, res2_boonja, res2_boonmo)
    else:
        exp_4 = '{%d} over {%d} `+` {%d} over {%d} `+` {%d} over {%d}$$/수식$$\n$$수식$$`=` {%d} over {%d} `=` 1 {%d} over {%d} `=` 1 {%d} over {%d}' % (s18, lcm_2, s19, lcm_2, s20, lcm_2, big_head_boonja2, res2_boonmo, res2_boonja, res2_boonmo, giyak_boonja2, giyak_boonmo2)


    cor_frac_1 = '1 {%d} over {%d}' % (giyak_boonja1, giyak_boonmo1)
    cor_frac_2 = '1 {%d} over {%d}' % (giyak_boonja2, giyak_boonmo2)

    exp_5 = 'LEFT ( %s, ~%s RIGHT )' % (cor_frac_1, cor_frac_2)
    exp_6 = 'LEFT ( 1 {%d} over {%d}, ~ 1 {%d} over {%d} RIGHT )' % (boonja1, lcm_res, boonja2, lcm_res)
    exp_7 = '%s `%s` %s' % (cor_frac_1, cor_sign, cor_frac_2)




    stem = stem.format(exp_1=exp_1, exp_2=exp_2)
    answer = answer.format(cor_jaem=cor_jaem)
    comment = comment.format(exp_1=exp_1, exp_2=exp_2, exp_3=exp_3, exp_4=exp_4, exp_5=exp_5, exp_6=exp_6, exp_7=exp_7, cor_jaem=cor_jaem)

    return stem, answer, comment






    # flag = True
    # while flag:
    #     denoms = np.random.choice(np.arange(2, 16), 3, False)
    #     s1, s3, s5 = [np.random.randint(1, d, 1)[0] for d in denoms]
    #     s2, s4, s6 = denoms
    #     denoms = np.random.choice(np.arange(2, 16), 3, False)
    #     s7, s9, s11 = [np.random.randint(1, d, 1)[0] for d in denoms]
    #     s8, s10, s12 = denoms
    #
    #     if check_simFrac(s1, s2) and check_simFrac(s3, s4) and check_simFrac(s5, s6) and check_simFrac(s7, s8) and check_simFrac(s9, s10) and check_simFrac(s11, s12):
    #         frac_1 = '{%d} over {%d}' % (s1, s2)
    #         frac_2 = '{%d} over {%d}' % (s3, s4)
    #         frac_3 = '{%d} over {%d}' % (s5, s6)
    #         frac_4 = '{%d} over {%d}' % (s7, s8)
    #         frac_5 = '{%d} over {%d}' % (s9, s10)
    #         frac_6 = '{%d} over {%d}' % (s11, s12)
    #         frac_list = [frac_1, frac_2, frac_3, frac_4, frac_5, frac_6]
    #
    #         lcm_1 = get_lcm(get_lcm(s2, s4), s6)
    #         lcm_2 = get_lcm(get_lcm(s8, s10), s12)
    #
    #         s13 = s1 * (lcm_1 // s2)
    #         s14 = s3 * (lcm_1 // s4)
    #         s15 = s5 * (lcm_1 // s6)
    #         s16 = s13 + s14 + s15
    #         s17 = s16 - lcm_1
    #
    #         s18 = s7 * (lcm_2 // s8)
    #         s19 = s9 * (lcm_2 // s10)
    #         s20 = s11 * (lcm_2 // s12)
    #         s21 = s17 + s18 + s19
    #         s22 = s21 - lcm_2
    #
    #         if len(set(frac_list)) == 6 and max(lcm_1, lcm_2) <= 84 and lcm_1 < s16 < lcm_1 * 2 and lcm_2 < s21 < lcm_2 * 2:
    #             exp_1 = '%s `+` %s `+` %s' % (frac_1, frac_2, frac_3)
    #             exp_2 = '%s `+` %s `+` %s' % (frac_4, frac_5, frac_6)
    #
    #             exp_3 = '{%d} over {%d} `+` {%d} over {%d} `+` {%d} over {%d} `=` {%d} over {%d} `=` 1 {%d} over {%d}' \
    #                     '' % (s13, lcm_1, s14, lcm_1, s15, lcm_1, s16, lcm_1, s17, lcm_1)
    #             exp_4 = '{%d} over {%d} `+` {%d} over {%d} `+` {%d} over {%d} `=` {%d} over {%d} `=` 1 {%d} over {%d}' \
    #                     '' % (s18, lcm_2, s19, lcm_2, s20, lcm_2, s21, lcm_2, s22, lcm_2)
    #
    #             cor_nums_list = []
    #
    #             if get_gcd(s17, lcm_1) == 1:
    #                 cor_frac_1 = '1 {%d} over {%d}' % (s17, lcm_1)
    #                 cor_nums_list.append([s17, lcm_1])
    #                 n1, d1 = s17, lcm_1
    #             else:
    #                 n1 = s17 // get_gcd(s17, lcm_1)
    #                 d1 = lcm_1 // get_gcd(s17, lcm_1)
    #                 cor_frac_1 = '1 {%d} over {%d}' % (n1, d1)
    #                 cor_nums_list.append([n1, d1])
    #                 exp_3 += ' `=` %s' % (cor_frac_1)
    #
    #             if get_gcd(s22, lcm_2) == 1:
    #                 cor_frac_2 = '1 {%d} over {%d}' % (s22, lcm_2)
    #                 cor_nums_list.append([s22, lcm_2])
    #                 n2, d2 = s22, lcm_2
    #
    #             else:
    #                 n2 = s22 // get_gcd(s22, lcm_2)
    #                 d2 = lcm_2 // get_gcd(s22, lcm_2)
    #                 cor_frac_2 = '1 {%d} over {%d}' % (n2, d2)
    #                 cor_nums_list.append([n2, d2])
    #                 exp_4 += ' `=` %s' % (cor_frac_2)
    #
    #             lcm_3 = get_lcm(d1, d2)
    #
    #             s23, s24 = cor_nums_list[0]
    #             s25, s26 = cor_nums_list[1]
    #             s27 = s23 * (lcm_3 // s24)
    #             s28 = s25 * (lcm_3 // s26)
    #
    #             if lcm_3 <= 150 and d1 != d2 and n1 != n2 and s27 != s28:
    #                 cor_jaem = 'ㄱ' if s27 > s28 else 'ㄴ'
    #                 cor_sign = left if s27 > s28 else right
    #                 flag = False
    #
    #
    # exp_5 = 'LEFT ( %s, ~%s RIGHT )' % (cor_frac_1, cor_frac_2)
    # exp_6 = 'LEFT ( 1 {%d} over {%d}, ~ 1 {%d} over {%d} RIGHT )' % (s27, lcm_3, s28, lcm_3)
    # exp_7 = '%s `%s` %s' % (cor_frac_1, cor_sign, cor_frac_2)






















































# 5-1-5-28
def fractionaddsub515_Stem_015():
    stem = "어떤 수에 $$수식$${frac_1}$$/수식$${j1} 더해야 할 것을 잘못하여 뺐더니 $$수식$${frac_2}$$/수식$${j2} 되었습니다. 바르게 계산하면 얼마인가요?\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 $$수식$${box}$$/수식$$라 하면 잘못 계산한 식은 $$수식$${exp_1}$$/수식$$이므로\n" \
              "$$수식$${exp_2}$$/수식$$입니다.\n" \
              "따라서 바르게 계산하면 $$수식$${exp_3}$$/수식$$입니다.\n\n"


    flag = True
    while flag:
        a2, b2 = np.random.choice(np.arange(1, 4), 2)
        n = np.random.choice([2, 3, 4], 1)[0]
        B = np.random.choice([2, 3, 5, 7], 1)[0]
        A = B * n
        a1 = np.random.randint(1, A, 1)[0]
        b1 = np.random.randint(1, B, 1)[0]
        b3 = b1 * n
        a3 = a1 + b3
        a4 = a2 + b2
        a5 = a3 + b3
        a6 = a4 + b2
        a7 = a5 - A
        a8 = a6 + 1
        m = get_gcd(A, a7)
        A1 = A // m
        a9 = a7 // m

        if a9 >= A1:
            continue

        if check_simFrac(A, a1) and check_simFrac(B, b1) and A < a3 < A * 2:
            flag = False

    frac_1 = '%d {%d} over {%d}' % (b2, b1, B)
    frac_2 = '%d {%d} over {%d}' % (a2, a1, A)
    frac_3 = '%d {%d} over {%d}' % (a4, a3, A)
    cor_frac = '%d {%d} over {%d}' % (a8, a9, A1)

    exp_1 = '%s `-` %s `=` %s' % (box, frac_1, frac_2)
    exp_2 = '%s `=` %s `+` %s `=` %s `+` %d {%d} over {%d} `=` %s' % (box, frac_2, frac_1, frac_2, b2, b3, A, frac_3)
    exp_3 = '%s `+` %s `=` %s `+` %d {%d} over {%d} `=` %d {%d} over {%d} `=` %s' % (frac_3, frac_1, frac_3, b2, b3, A, a6, a5, A, cor_frac)

    j1 = '을' if b1 % 10 in have_jongsung_num else '를'
    j2 = '이' if a1 % 10 in have_jongsung_num else '가'


    stem = stem.format(frac_1=frac_1, frac_2=frac_2, j1=j1, j2=j2)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(box=box, exp_1=exp_1, exp_2=exp_2, exp_3=exp_3)

    return stem, answer, comment

















































# 5-1-5-29
def fractionaddsub515_Stem_016():
    stem = "{t3}{j3} {t1}{j1}네 모둠은 $$수식$${frac_1} ` rm L$$/수식$$ 마셨고, {t2}{j2}네 모둠은 {t1}{j1}네 모둠보다 $$수식$${frac_2} ` rm L$$/수식$$ 더 마셨습니다. 두 모둠이 마신 {t3}{j4} 모두 몇 $$수식$$rm L$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${cor_frac} ` rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${t2}{j2}네 모둠이 마신 {t3}의 양$$수식$$RIGHT )$$/수식$$ \n $$수식$$ ` = ` {exp_1}$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$두 모둠이 마신 {t3}의 양$$수식$$RIGHT )$$/수식$$ \n $$수식$$ ` = ` {exp_2}$$/수식$$\n\n"


    terms = [np.random.choice(person_nam, 1)[0], np.random.choice(person_yeo, 1)[0]]
    np.random.shuffle(terms)

    t1, t2 = terms
    j1, j2 = ['' if josa_check(t[-1]) == ' ' else '이' for t in terms]
    t3 = np.random.choice('우유 음료수 물 주스'.split(' '), 1)[0]
    j3 = '를' if josa_check(t3[-1]) == ' ' else '을'
    j4 = '는' if josa_check(t3[-1]) == ' ' else '은'



    while True:
        b2 = 1
        a2 = np.random.randint(2, 5)

        p = np.random.randint(2, 8)
        q = np.random.randint(2, 8)
        r = np.random.randint(2, 8)

        if get_soroso(q, r) == 0 or p * q > 21 or p * r > 21 or p * q * r > 99:
            continue

        A = p * q
        B = p * r
        C = p * q * r

        a1 = soroso_select(A)
        b1 = soroso_select(B)


        if (a1 * r * 2) + (b1 * q) > C - 1:
            continue

        a3 = a1 * r
        b3 = b1 * q

        c1 = a3 + b3
        c2 = a2 + b2

        c3 = a3 + c1
        c4 = a2 + c2

        C1, c5 = get_giyak(C, c3)

        break



    frac_1 = '%d {%d} over {%d}' % (a2, a1, A)
    frac_2 = '%d {%d} over {%d}' % (b2, b1, B)
    frac_3 = '%d {%d} over {%d}' % (c2, c1, C)
    cor_frac = '%d {%d} over {%d}' % (c4, c5, C1)

    exp_1 = '%s `+` %s `=` %d {%d} over {%d} `+` %d {%d} over {%d} `=` %s' % (frac_1, frac_2, a2, a3, C, b2, b3, C, frac_3)
    exp_2 = '%s `+` %s `=` %d {%d} over {%d} `+` %d {%d} over {%d} `=` %s' % (frac_1, frac_3, a2, a3, C, c2, c1, C, cor_frac)


    stem = stem.format(frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, t1=t1, t2=t2, t3=t3, j1=j1, j2=j2, j3=j3, j4=j4)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(exp_1=exp_1, exp_2=exp_2, t2=t2, t3=t3, j2=j2)

    return stem, answer, comment





    # flag = True
    # while flag:
    #     a2 = np.random.randint(2, 5, 1)[0]
    #     b2 = 1
    #     p, q, r = np.random.choice(np.arange(2, 8), 3)
    #     A, B, C = [p, p, p] * np.reshape([q, r, q * r], -1)
    #     a1 = np.random.randint(1, A, 1)[0]
    #     b1 = np.random.randint(1, B, 1)[0]
    #     a3 = a1 * 4
    #     b3 = b1 * q
    #     c1 = a3 + b3
    #     c2 = a2 + b2
    #     c3 = a3 + c1
    #     c4 = a2 + c2
    #     n = get_gcd(C, c3)
    #     C1 = C // n
    #     c5 = c3 // n
    #
    #     if check_simFrac(q, r) and max(A, B) <= 21 and C < 100 and check_simFrac(A, a1) and check_simFrac(B, b1) and a3 * 2 + b3 < C:
    #         flag = False
    #
    # frac_1 = '%d {%d} over {%d}' % (a2, a1, A)
    # frac_2 = '%d {%d} over {%d}' % (b2, b1, B)
    # frac_3 = '%d {%d} over {%d}' % (c2, c1, C)
    # cor_frac = '%d {%d} over {%d}' % (c4, c5, C1)
    #
    # exp_1 = '%s `+` %s `=` %d {%d} over {%d} `+` %d {%d} over {%d} `=` %s' % (frac_1, frac_2, a2, a3, C, b2, b3, C, frac_3)
    # exp_2 = '%s `+` %s `=` %d {%d} over {%d} `+` %d {%d} over {%d} `=` %s' % (frac_1, frac_3, a2, a3, C, c2, c1, C, cor_frac)








































# 5-1-5-31
def fractionaddsub515_Stem_017():
    stem = "$$수식$${box}$$/수식$$ 안에 알맞은 대분수를 구해 보세요.\n$$표$$$$수식$${box} `-` {frac_1} `=` {frac_2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${exp_1}$$/수식$$\n\n"


    flag = True
    while flag:
        a2, b2 = np.random.choice(np.arange(1, 6), 2)
        p, q, r = np.random.choice(np.arange(2, 9), 3)
        A, B, C = [p, p, p] * np.reshape([q, r, q * r], -1)
        a1 = np.random.randint(1, A, 1)[0]
        b1 = np.random.randint(1, B, 1)[0]
        a3 = a1 * r
        b3 = b1 * q
        c1 = a3 + b3
        c2 = a2 + b2
        c3 = c1 - C
        c4 = c2 + 1
        n = get_gcd(C, c3)
        C1 = C // n
        c5 = c3 // n

        if check_simFrac(q, r) and max(A, B) <= 21 and C <= 100 and c1 > C:
            flag = False

    frac_1 = '%d {%d} over {%d}' % (b2, b1, B)
    frac_2 = '%d {%d} over {%d}' % (a2, a1, A)
    cor_frac = '%d {%d} over {%d}' % (c4, c5, C1)

    exp_1 = '%s `=` %s `+` %s `=` %d {%d} over {%d} `+` %d {%d} over {%d} `=` %d {%d} over {%d} `=` %s' % (
    box, frac_2, frac_1, a2, a3, C, b2, b3, C, c2, c1, C, cor_frac)


    stem = stem.format(frac_1=frac_1, frac_2=frac_2, box=box)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(exp_1=exp_1)

    return stem, answer, comment














































# 5-1-5-32
def fractionaddsub515_Stem_018():
    stem = "{t1}{j1}는 {t2}댁에 가는데 {t3}를 $$수식$${frac_1}$$/수식$$시간, {t4}를 $$수식$${frac_2}$$/수식$$시간 탔습니다. {t3}와 {t4}를 탄 시간은 모두 몇 시간 몇 분인지 구해 보세요.\n"
    answer = "(정답)\n{cor_text}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${t3}와 {t4}를 탄 시간$$수식$$RIGHT )$$/수식$$ \n $$수식$$` = ` {exp_1} ` LEFT ($$/수식$$시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${frac_3}$$/수식$$시간$$수식$$`=` {frac_4}$$/수식$$시간$$수식$$`=` {minute}$$/수식$$분이므로 " \
              "{t3}와 {t4}를 탄 시간은 {cor_text}입니다.\n\n"


    AB_pairs = [[2, 3], [2, 5], [2, 15], [3, 4], [3, 5], [3, 10], [4, 5], [5, 6]]

    t1 = np.random.choice(person_nam + person_yeo, 1)[0]
    j1 = '' if josa_check(t1[-1]) == ' ' else '이'
    t2 = np.random.choice('할머니 할아버지 이모 큰아버지 삼촌'.split(' '), 1)[0]
    t3, t4 = np.random.choice('버스 기차 배'.split(' '), 2, False)

    flag = True
    while flag:
        a2, b2 = np.random.choice(np.arange(1, 5), 2)
        A, B = AB_pairs[np.random.randint(0, len(AB_pairs), 1)[0]]
        C = A * B
        if a2 + b2 <= 6:
            a1 = np.random.randint(1, A, 1)[0]
            b1 = np.random.randint(1, B, 1)[0]
            a3 = a1 * B
            b3 = b1 * A
            c1 = a3 + b3
            c2 = a2 + b2
            c3 = c1 - C
            c4 = c2 + 1
            minute = c3 * (60 // C)
            if check_simFrac(a1, A) and check_simFrac(b1, B) and c1 > C:
                flag = False


    frac_1 = '%d {%d} over {%d}' % (a2, a1, A)
    frac_2 = '%d {%d} over {%d}' % (b2, b1, B)
    frac_3 = '{%d} over {%d}' % (c3, C)
    frac_4 = '{%d} over {60}' % (minute)

    cor_frac = '%d {%d} over {%d}' % (c4, c3, C)
    cor_text = '$$수식$$%d$$/수식$$시간 $$수식$$%d$$/수식$$분' % (c4, minute)

    exp_1 = '%s `+` %s `=` %d {%d} over {%d} `+` %d {%d} over {%d} `=` %d {%d} over {%d} `=` %s' % (frac_1, frac_2, a2, a3, C, b2, b3, C, c2, c1, C, cor_frac)


    stem = stem.format(frac_1=frac_1, frac_2=frac_2, t1=t1, t2=t2, t3=t3, t4=t4, j1=j1)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(exp_1=exp_1, frac_3=frac_3, frac_4=frac_4, minute=minute, cor_text=cor_text, t3=t3, t4=t4)

    return stem, answer, comment

















































# 5-1-5-36
def fractionaddsub515_Stem_019():
    stem = "계산 결과가 더 큰 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${exp_1}$$/수식$$    ㉡ $$수식$${exp_2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_jaem}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${exp_3}$$/수식$$\n" \
              "㉡ $$수식$${exp_4}$$/수식$$\n" \
              "$$수식$${exp_5}$$/수식$$이므로 계산 결과가 더 큰 것은 {cor_jaem}입니다.\n\n"


    pqr_pairs = [[2, 3, 5], [2, 3, 7], [3, 5, 7]]

    flag = True
    while flag:
        p, q, r = pqr_pairs[np.random.randint(0, len(pqr_pairs), 1)[0]]
        A = p
        B = q * r
        C = p * q
        D = p * r
        A1 = p * q * r
        a = np.random.randint(1, A, 1)[0]
        b = np.random.randint(1, B, 1)[0]
        a1 = a * q * r
        b1 = b * p
        a2 = a1 - b1
        c = np.random.randint(1, C, 1)[0]
        d = np.random.randint(1, D, 1)[0]
        C1 = p * q * r
        c1 = c * r
        d1 = d * q
        c2 = c1 - d1

        if check_simFrac(a, A) and check_simFrac(b, B) and check_simFrac(c, C) and check_simFrac(d, D) and a2 >= 1 and c2 >= 1 and c2 != a2 and a2 - 10 <= c2 <= a2 + 10:
            cor_jaem, cor_sign = ['㉠', left] if a2 > c2 else ['㉡', right]

            flag = False

    exp_1 = '{%d} over {%d} `-` {%d} over {%d}' % (a, A, b, B)
    exp_2 = '{%d} over {%d} `-` {%d} over {%d}' % (c, C, d, D)

    frac_1 = '{%d} over {%d}' % (a2, A1)
    frac_2 = '{%d} over {%d}' % (c2, C1)

    exp_3 = '%s `=` {%d} over {%d} `-` {%d} over {%d} `=` %s' % (exp_1, a1, A1, b1, A1, frac_1)
    exp_4 = '%s `=` {%d} over {%d} `-` {%d} over {%d} `=` %s' % (exp_2, c1, C1, d1, C1, frac_2)
    exp_5 = '%s `%s` %s' % (frac_1, cor_sign, frac_2)


    stem = stem.format(exp_1=exp_1, exp_2=exp_2)
    answer = answer.format(cor_jaem=cor_jaem)
    comment = comment.format(exp_3=exp_3, exp_4=exp_4, exp_5=exp_5, cor_jaem=cor_jaem)

    return stem, answer, comment












































# 5-1-5-37
def fractionaddsub515_Stem_020():
    stem = "㉠과 ㉡의 차를 구해 보세요.\n$$표$$㉠ $$수식$${frac_1}$$/수식$$이 $$수식$${s1}$$/수식$$개인 수    ㉡ $$수식$${frac_2}$$/수식$$이 $$수식$${s4}$$/수식$$개인 수$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${frac_1}$$/수식$$이 $$수식$${s1}$$/수식$$개인 수는 $$수식$${frac_3}$$/수식$$입니다.\n" \
              "㉡ $$수식$${frac_2}$$/수식$$이 $$수식$${s4}$$/수식$$개인 수는 $$수식$${frac_4}$$/수식$$입니다.\n" \
              "따라서 ㉠과 ㉡의 차는 $$수식$${exp_1}$$/수식$$입니다.\n\n"



    flag = True
    while flag:
        s2 = np.random.randint(2, 16)
        s5 = np.random.randint(2, 16)

        if get_soroso(s2, s5) == 0 or 10 > s2 * s5 or s2 * s5 > 99:
            continue

        s1 = soroso_select(s2)
        s4 = soroso_select(s5)

        lcm = get_lcm(s2, s5)

        if lcm > 84:
            continue

        s3 = s1 * (lcm // s2)
        s6 = s4 * (lcm // s5)

        if s3 <= s6:
            continue

        s7 = s3 - s6

        giyak_boonja, giyak_boonmo = get_giyak(s7, lcm)

        break


    frac_1 = '{1} over {%d}' % (s2)
    frac_2 = '{1} over {%d}' % (s5)
    frac_3 = '{%d} over {%d}' % (s1, s2)
    frac_4 = '{%d} over {%d}' % (s4, s5)
    frac_5 = '{%d} over {%d}' % (s3, lcm)
    frac_6 = '{%d} over {%d}' % (s6, lcm)

    cor_frac = '{%d} over {%d}' % (giyak_boonja, giyak_boonmo)

    exp_1 = '%s `-` %s `=` %s `-` %s `=` %s' % (frac_3, frac_4, frac_5, frac_6, cor_frac)

    # j1 = '이' if s3 % 10 in have_jongsung_num else '가'
    # j2 = '이' if s6 % 10 in have_jongsung_num else '가'


    stem = stem.format(frac_1=frac_1, frac_2=frac_2, s1=s1, s4=s4)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(frac_1=frac_1, frac_2=frac_2, s1=s1, s4=s4, frac_3=frac_3, frac_4=frac_4, exp_1=exp_1)

    return stem, answer, comment






    # flag = True
    # while flag:
    #     s2, s5 = np.random.choice(np.arange(2, 16), 2)
    #     s1 = np.random.randint(1, s2, 1)[0]
    #     s4 = np.random.randint(1, s5, 1)[0]
    #     if check_simFrac(s1, s2) and check_simFrac(s4, s5):
    #         lcm = get_lcm(s2, s5)
    #         s3 = s1 * (lcm // s2)
    #         s6 = s4 * (lcm // s5)
    #         s7 = s3 - s6
    #         if lcm <= 84 and s3 > s6 and check_simFrac(s7, lcm):
    #             flag = False






































# 5-1-5-39
def fractionaddsub515_Stem_021():
    stem = "계산 결과를 비교하여 $$수식$${box}$$/수식$$ 안에 $$수식$${left}$$/수식$$, $$수식$${equal}$$/수식$$, $$수식$${right}$$/수식$$를 알맞게 써넣으세요.\n$$수식$${exp_1}~~{box}~~{exp_2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${cor_sign}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${exp_3}$$/수식$$,\n" \
              "$$수식$${exp_4}$$/수식$$\n" \
              "$$수식$${exp_5}$$/수식$$이므로 $$수식$${exp_6}$$/수식$$입니다.\n\n"


    flag = True
    while flag:
        # p, q, r = np.random.choice(np.arange(2, 8), 3)
        # A, B, C, D, A1 = [p, p, p, p, p] * np.reshape([q, r, q, r, q * r], -1)

        p = np.random.randint(2, 8)
        q = np.random.randint(2, 8)
        r = np.random.randint(2, 8)

        if get_soroso(p, r) == 0 or get_soroso(q, r) == 0 or p * q * r > 105:
            continue

        A = p * q
        B = p * r
        C = p * q
        D = q * r
        A1 = p * q * r

        if A == B or C == D:
            continue


        # a = np.random.randint(1, A, 1)[0]
        # b = np.random.randint(1, A, 1)[0]
        a = soroso_select(A)
        b = soroso_select(B)

        a1 = a * r
        b1 = b * q
        a2 = a1 - b1

        # c = np.random.randint(1, C, 1)[0]
        # d = np.random.randint(1, D, 1)[0]
        c = soroso_select(C)
        d = soroso_select(D)

        C1 = p * q * r
        c1 = c * r
        d1 = d * p
        c2 = c1 - d1
        frac_1 = '{%d} over {%d}' % (a, A)
        frac_2 = '{%d} over {%d}' % (b, B)
        frac_3 = '{%d} over {%d}' % (c, C)
        frac_4 = '{%d} over {%d}' % (d, D)

        # if len(set([frac_1, frac_2, frac_3, frac_4])) > 2 and A1 <= 105 and a2 > 0 and a != c and check_simFrac(c, C) and check_simFrac(d, D) and a2 - 10 < c2 <= a2 + 10 and min(a2, c2) > 0:
        #     cor_sign = equal if a2 == c2 else left if a2 > c2 else right
        #     flag = False

        if len(set([frac_1, frac_2, frac_3, frac_4])) > 2 and A1 <= 105 and a2 > 0 and a != c and a2 - 10 < c2 <= a2 + 10 and min(a2, c2) > 0:
            cor_sign = equal if a2 == c2 else left if a2 > c2 else right
            flag = False


    exp_1 = '%s `-` %s' % (frac_1, frac_2)
    exp_2 = '%s `-` %s' % (frac_3, frac_4)

    frac_5 = '{%d} over {%d}' % (a2, A1)
    frac_6 = '{%d} over {%d}' % (c2, C1)

    exp_3 = '%s `=` {%d} over {%d} `-` {%d} over {%d} $$/수식$$\n$$수식$$ `=` %s' % (exp_1, a1, A1, b1, A1, frac_5)
    exp_4 = '%s `=` {%d} over {%d} `-` {%d} over {%d} $$/수식$$\n$$수식$$ `=` %s' % (exp_2, c1, C1, d1, C1, frac_6)
    exp_5 = '%s `%s` %s' % (frac_5, cor_sign, frac_6)
    exp_6 = '%s `%s` %s' % (exp_1, cor_sign, exp_2)


    stem = stem.format(exp_1=exp_1, exp_2=exp_2, box=box, right=right, left=left, equal=equal)
    answer = answer.format(cor_sign=cor_sign)
    comment = comment.format(exp_3=exp_3, exp_4=exp_4, exp_5=exp_5, exp_6=exp_6)

    return stem, answer, comment












































# 5-1-5-40
def fractionaddsub515_Stem_022():
    stem = "같은 양의 물이 담긴 두 비커에 {t1}의 양을 다르게 하여 {t1}물을 만들었습니다. ㉠ 비커에는 {t1}을 $$수식$${frac_1}$$/수식$$컵 넣었고, ㉡ 비커에는 ㉠ 비커보다 $$수식$${frac_2}$$/수식$$컵 적게 {t1}을 넣었습니다. ㉡ 비커에 넣은 {t1}의 양은 몇 컵인지 기약분수로 써 보세요.\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$컵\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$㉡ 비커에 넣은 {t1}의 양$$수식$$RIGHT )$$/수식$$ \n $$수식$$ ` = ` {exp_1} ` LEFT ($$/수식$$컵$$수식$$RIGHT )$$/수식$$\n\n"


    t1 = np.random.choice('소금 설탕 꿀'.split(' '), 1)[0]

    flag = True
    while flag:
        s2, s5 = sorted(list(np.random.choice(np.arange(2, 16), 2)))
        # s1 = np.random.randint(1, s2, 1)[0]
        # s4 = np.random.randint(1, s5, 1)[0]

        s1 = soroso_select(s2)
        s4 = soroso_select(s5)


        lcm = get_lcm(s2, s5)
        # s3 = s1 * lcm // s2
        # s6 = s4 * lcm // s2
        s3 = s1 * int(lcm / s2)
        s6 = s4 * int(lcm / s5)



        if lcm <= 84 and s3 > s6:
            s7 = s3 - s6
            gcd = get_gcd(s7, lcm)
            s8 = s7 // gcd
            s9 = lcm // gcd

            if s9 == lcm:
                continue

            flag = False

    frac_1 = '{%d} over {%d}' % (s1, s2)
    frac_2 = '{%d} over {%d}' % (s4, s5)
    cor_frac = '{%d} over {%d}' % (s8, s9)

    exp_1 = '%s `-` %s `=` {%d} over {%d} `-` {%d} over {%d} `=` {%d} over {%d} `=` %s' % (frac_1, frac_2, s3, lcm, s6, lcm, s7, lcm, cor_frac)


    stem = stem.format(t1=t1, frac_1=frac_1, frac_2=frac_2)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(exp_1=exp_1, t1=t1)

    return stem, answer, comment















































# 5-1-5-41
def fractionaddsub515_Stem_023():
    stem = "{t1} $$수식$${frac_1} ` rm kg$$/수식$$ 중에서 밥을 짓는데 $$수식$${frac_2} ` rm kg$$/수식$$을 사용했습니다. 남은 {t1}{j1} 몇 $$수식$$rm kg$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${cor_frac} ` rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$남은 {t1}의 무게$$수식$$RIGHT )$$/수식$$ \n $$수식$$ ` = ` {exp_1} ` LEFT ( rm kg RIGHT )$$/수식$$\n\n"


    t1 = np.random.choice('쌀 햅쌀 현미 흑미'.split(' '), 1)[0]
    j1 = '를' if josa_check(t1[-1]) == ' ' else '을'

    flag = True
    while flag:
        p, q, r = np.random.choice(np.arange(2, 8), 3)
        A, B, C = [p, p, p] * np.reshape([q, r, q * r], -1)
        a = np.random.randint(1, A, 1)[0]
        b = np.random.randint(1, B, 1)[0]
        c1 = a * r
        c2 = b * q
        c3 = c1 - c2
        n = get_gcd(C, c3)
        C1 = C // n
        c4 = c3 // n

        if check_simFrac(q, r) and check_simFrac(a, A) and check_simFrac(b, B) and C <= 105 and c3 > 0:
            flag = False


    j1 = '는' if josa_check(t1[-1]) == ' ' else '은'
    frac_1 = '{%d} over {%d}' % (a, A)
    frac_2 = '{%d} over {%d}' % (b, B)

    cor_frac = '{%d} over {%d}' % (c4, C1)
    exp_1 = '%s `-` %s `=` {%d} over {%d} `-` {%d} over {%s} `=` %s' % (frac_1, frac_2, c1, C, c2, C, cor_frac)


    stem = stem.format(t1=t1, frac_1=frac_1, frac_2=frac_2, j1=j1)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(exp_1=exp_1, t1=t1)

    return stem, answer, comment















































# 5-1-5-43
def fractionaddsub515_Stem_024():
    stem = "{t1}{j1}네 반 학급 문고에는 {t2}, {t3}, {t4}{j4_1} 있습니다. {t2}{j2} 전체의 $$수식$${frac_1}$$/수식$$, {t3}{j3} 전체의 $$수식$${frac_2}$$/수식$$입니다. 나머지는 모두 {t4}{j4_2}라면 {t4}{j4_3} 전체의 얼마인가요?\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "먼저 전체 $$수식$$1$$/수식$$에서 {t2} $$수식$${frac_1}$$/수식$${j5} 빼면 $$수식$${exp_1}$$/수식$$이고, \n" \
              "$$수식$${frac_3}$$/수식$$에서 {t3} $$수식$${frac_2}$$/수식$${j6} 빼면 $$수식$${exp_2}$$/수식$$입니다.\n" \
              "따라서 {t4}{j4_3} 전체의 $$수식$${cor_frac}$$/수식$$입니다.\n\n"


    t1 = np.random.choice(person_nam + person_yeo, 1)[0]
    j1 = '' if josa_check(t1[-1]) == ' ' else '이'
    terms = np.random.choice('동화책 과학책 학습만화 위인전 소설책'.split(' '), 3, False)

    t2, t3, t4 = terms
    j2, j3, j4_3 = ['는' if josa_check(t[-1]) == ' ' else '은' for t in terms]
    j4_1 = '가' if josa_check(t4[-1]) == ' ' else '이'
    j4_2 = '' if josa_check(t4[-1]) == ' ' else '이'

    flag = True
    while flag:
        A, B = np.random.choice(np.arange(2, 13), 2)
        a = np.random.randint(1, A, 1)[0]
        b = np.random.randint(1, B, 1)[0]
        a1 = A - a
        C = A * B
        c1 = a1 * B
        c2 = b * A
        c3 = c1 - c2
        n = get_gcd(c3, C)
        C1 = C // n
        c4 = c3 // n

        if check_simFrac(A, B) and check_simFrac(a, A) and check_simFrac(b, B) and C < 100 and c3 > A:
            flag = False


    frac_1 = '{%d} over {%d}' % (a, A)
    frac_2 = '{%d} over {%d}' % (b, B)
    frac_3 = '{%d} over {%d}' % (a1, A)

    cor_frac = '{%d} over {%d}' % (c4, C1)
    exp_1 = '1 `-` %s `=` {%d} over {%d} `-` {%d} over {%d} `=` %s' % (frac_1, A, A, a, A, frac_3)
    exp_2 = '%s `-` %s `=` {%d} over {%d} `-` {%d} over {%d} `=` %s' % (frac_3, frac_2, c1, C, c2, C, cor_frac)

    # j5 = '를' if a % 10 in have_jongsung_num else '을'
    # j6 = '를' if b % 10 in have_jongsung_num else '을'
    j5 = get_josa(a, "를")
    j6 = get_josa(b, "를")


    stem = stem.format(t1=t1, t2=t2, t3=t3, t4=t4, j1=j1, j2=j2, j3=j3, j4_1=j4_1, j4_2=j4_2, j4_3=j4_3, frac_1=frac_1,
                       frac_2=frac_2)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(t2=t2, t3=t3, t4=t4, j4_3=j4_3, j5=j5, j6=j6, frac_1=frac_1, frac_2=frac_2, frac_3=frac_3,
                             exp_1=exp_1, exp_2=exp_2, cor_frac=cor_frac)

    return stem, answer, comment

















































# 5-1-5-45
def fractionaddsub515_Stem_025():
    stem = "가장 큰 수에서 나머지 두 수를 뺀 값은 얼마인가요?\n$$표$$$$수식$${frac_1}$$/수식$$    $$수식$${frac_2}$$/수식$$    $$수식$${frac_3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${exp_1}$$/수식$$, $$수식$${exp_2}$$/수식$$이므로 가장 큰 분수는 $$수식$${frac_4}$$/수식$$입니다.\n" \
              "따라서 가장 큰 수에서 나머지 두 수를 뺀 값은\n" \
              "$$수식$${exp_3}$$/수식$$입니다.\n\n"


    flag = True
    while flag:
        s2, s4, s6 = np.random.choice(np.arange(2, 16), 3, False)
        s1, s3, s5 = [np.random.randint(1, a, 1)[0] for a in [s2, s4, s6]]

        lcm = get_lcm(get_lcm(s2, s4), s6)
        if check_simFrac(s1, s2) and check_simFrac(s3, s4) and check_simFrac(s5, s6) and lcm <= 80:
            s7 = s1 * (lcm // s2)
            s8 = s3 * (lcm // s4)
            s9 = s5 * (lcm // s6)

            if s7 != s8 and s8 != s9 and s7 != s9:
                frac_dict = {s7: '{%d} over {%d}' % (s1, s2), s8: '{%d} over {%d}' % (s3, s4), s9: '{%d} over {%d}' % (s5, s6)}
                dict_keys = list(frac_dict.keys())
                np.random.shuffle(dict_keys)

                frac_1, frac_2, frac_3 = [frac_dict.get(k) for k in dict_keys]
                n4 = max(dict_keys)

                frac_4 = frac_dict.get(n4)
                frac_5, frac_6 = [frac_dict.get(k) for k in dict_keys if frac_dict.get(k) != frac_4]
                n5, n6 = [k for k in dict_keys if k != n4]

                s10 = n4 - n5
                s11 = s10 - n6
                if s10 > 0 and s11 > 0 and check_simFrac(lcm, s11):
                    flag = False


    exp_1 = '%s `%s` %s' % (frac_5, right, frac_4)
    exp_2 = '%s `%s` %s' % (frac_6, right, frac_4)
    cor_frac = '{%s} over {%d}' % (s11, lcm)

    exp_3 = '%s `-` %s `-` %s `=` {%d} over {%d} `-` {%d} over {%d} `-` {%d} over {%d}$$/수식$$\n$$수식$$ `=` {%d} over {%d} `-` {%d} over {%d} `=` %s'\
            % (frac_4, frac_5, frac_6, n4, lcm, n5, lcm, n6, lcm, s10, lcm, n6, lcm, cor_frac)


    stem = stem.format(frac_1=frac_1, frac_2=frac_2, frac_3=frac_3)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(exp_1=exp_1, exp_2=exp_2, frac_4=frac_4, exp_3=exp_3)

    return stem, answer, comment














































# 5-1-5-47
def fractionaddsub515_Stem_026():
    stem = "두 수의 차를 구해 보세요.\n$$표$$$$수식$${frac_1}$$/수식$$    $$수식$${frac_2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "두 수의 차는 큰 수에서 작은 수를 빼면 되므로\n" \
              "$$수식$${exp_1}$$/수식$$입니다.\n\n"


    flag = True
    while flag:
        p, q, r = np.random.choice(np.arange(2, 8), 3)
        A = p * q
        B = p * r
        a = np.random.randint(1, A, 1)[0]
        b = np.random.randint(1, B, 1)[0]
        b1, a1 = sorted(list(np.random.choice(np.arange(1, 10), 2, False)))
        C = p * q * r
        c1 = a * r
        c2 = b * q
        c3 = c1 - c2
        c4 = a1 - b1

        if check_simFrac(a, A) and check_simFrac(b, B) and c3 > 0 and C < 100 and check_simFrac(C, c3):
            flag = False

    frac_1 = '%d {%d} over {%d}' % (a1, a, A)
    frac_2 = '%d {%d} over {%d}' % (b1, b, B)
    cor_frac = '%d {%d} over {%d}' % (c4, c3, C)

    exp_1 = '%s `-` %s `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %s' % (
    frac_1, frac_2, a1, c1, C, b1, c2, C, cor_frac)

    frac_1, frac_2 = np.random.choice([frac_1, frac_2], 2, False)


    stem = stem.format(frac_1=frac_1, frac_2=frac_2)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(exp_1=exp_1)

    return stem, answer, comment















































# 5-1-5-48
def fractionaddsub515_Stem_027():
    stem = "㉠과 ㉡ 중에서 계산 결과가 더 큰 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${exp_1}$$/수식$$    ㉡ $$수식$${exp_2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_jaem}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${exp_3}$$/수식$$\n" \
              "㉡ $$수식$${exp_4}$$/수식$$\n" \
              "따라서 $$수식$${exp_5}$$/수식$$이므로 계산 결과가 더 큰 것은 {cor_jaem}입니다.\n\n"


    while True:
        s1 = np.random.randint(2, 16)
        s4 = np.random.randint(1, s1)

        s7 = np.random.randint(2, 16)
        s10 = np.random.randint(1, s7)

        if (s1 - s4) - (s7 - s10) != 1:
            if (s7 - s10) - (s1 - s4) != 1:
                continue

        while True:
            p = [2, 3, 5, 7][np.random.randint(0, 4)]
            q = np.random.randint(2, 5)
            r = np.random.randint(2, 5)

            if q != r and p * q * r <= 60:
                break

        s3 = p * q
        s6 = p * q * r
        s9 = p
        s12 = p * q

        s2 = soroso_select(s3)
        s5 = soroso_select(s6)
        s8 = soroso_select(s9)
        s11 = soroso_select(s12)

        f1_lcm = s6
        s13 = s2 * r
        s14 = s5

        f2_lcm = s12
        s16 = s8 * q
        s17 = s11

        s19 = s1 - s4
        s15 = s13 - s14

        if s15 <= 0:
            continue

        s20 = s7 - s10
        s21 = s16 - s17

        if s21 <= 0:
            continue

        giyak_boonja1, giyak_boonmo1 = get_giyak(s15, f1_lcm)
        giyak_boonja2, giyak_boonmo2 = get_giyak(s21, f2_lcm)

        if s19 > s20:
            cor_sign = "&gt;"
            cor_jaem = "㉠"
            break

        elif s19 < s20:
            cor_sign = "&lt;"
            cor_jaem = "㉡"
            break

        else:
            continue


    exp_1 = '%d {%d} over {%d} `-` %d {%d} over {%d}' % (s1, s2, s3, s4, s5, s6)
    exp_2 = '%d {%d} over {%d} `-` %d {%d} over {%d}' % (s7, s8, s9, s10, s11, s12)

    frac_1 = '%d {%d} over {%d}' % (s19, giyak_boonja1, giyak_boonmo1)
    frac_2 = '%d {%d} over {%d}' % (s20, giyak_boonja2, giyak_boonmo2)

    exp_3 = '%s `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %s' % (exp_1, s1, s13, f1_lcm, s4, s14, f1_lcm, frac_1)
    exp_4 = '%s `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %s' % (exp_2, s7, s16, f2_lcm, s10, s17, f2_lcm, frac_2)

    exp_5 = '%s `%s` %s' % (frac_1, cor_sign, frac_2)



    stem = stem.format(exp_1=exp_1, exp_2=exp_2)
    answer = answer.format(cor_jaem=cor_jaem)
    comment = comment.format(exp_3=exp_3, exp_4=exp_4, exp_5=exp_5, cor_jaem=cor_jaem)

    return stem, answer, comment






    # flag = True
    # while flag:
    #     s1, s4 = sorted(list(np.random.choice(np.arange(1, 16), 2, False)), reverse=True)
    #     s3, s6 = np.random.choice(np.arange(2, 16), 2, False)
    #     s2 = np.random.randint(1, s3, 1)[0]
    #     s5 = np.random.randint(1, s6, 1)[0]
    #
    #     s7, s10 = sorted(list(np.random.choice(np.arange(1, 16), 2, False)), reverse=True)
    #     s9, s12 = np.random.choice(np.arange(2, 16), 2, False)
    #     s8, s11 = [np.random.randint(1, s9, 1)[0], np.random.randint(1, s12, 1)[0]]
    #
    #     f1_lcm = get_lcm(s3, s6)
    #     f2_lcm = get_lcm(s9, s12)
    #
    #     s19 = s1 - s4
    #     s20 = s7 - s10
    #     if f1_lcm <= 60 and f2_lcm <= 60 and s19 > 0 and s20 > 0:
    #         s13 = s2 * (f1_lcm // s3)
    #         s14 = s5 * (f1_lcm // s6)
    #         s15 = s13 - s14
    #
    #         s16 = s8 * (f2_lcm // s9)
    #         s17 = s11 * (f2_lcm // s12)
    #         s18 = s16 - s17
    #
    #         if s15 > 0 and s18 > 0 and check_simFrac(s15, f1_lcm) and check_simFrac(s16, f2_lcm) and s19 != s20:
    #             flag = False
    #
    # exp_1 = '%d {%d} over {%d} `-` %d {%d} over {%d}' % (s1, s2, s3, s4, s5, s6)
    # exp_2 = '%d {%d} over {%d} `-` %d {%d} over {%d}' % (s7, s8, s9, s10, s11, s12)
    #
    # frac_1 = '%d {%d} over {%d}' % (s19, s15, f1_lcm)
    # frac_2 = '%d {%d} over {%d}' % (s20, s16, f2_lcm)
    #
    # exp_3 = '%s `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %s' % (exp_1, s1, s13, f1_lcm, s4, s14, f1_lcm, frac_1)
    # exp_4 = '%s `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %s' % (exp_2, s7, s16, f2_lcm, s10, s17, f2_lcm, frac_2)
    #
    # cor_jaem = 'ㄱ' if s19 > s20 else 'ㄴ'
    # cor_sign = left if s19 > s20 else right
    # exp_5 = '%s `%s` %s' % (frac_1, cor_sign, frac_2)







































# 5-1-5-49
def fractionaddsub515_Stem_028():
    stem = "계산 결과를 비교하여 $$수식$${box}$$/수식$$ 안에 $$수식$${left}$$/수식$$, $$수식$${equal}$$/수식$$, $$수식$${right}$$/수식$$를 알맞게 써넣으세요.\n$$수식$${exp_1}~~{box}~~{exp_2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${cor_sign}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${exp_3}$$/수식$$\n" \
              "$$수식$${exp_4}$$/수식$$\n" \
              "$$수식$${exp_5}$$/수식$$이므로 $$수식$${exp_6}$$/수식$$입니다.\n\n"


    flag = True
    while flag:
        p = np.random.randint(2, 8)
        q = np.random.randint(2, 8)
        r = np.random.randint(2, 8)

        A = p * q * q
        B = r
        C = p * q
        D = p * r

        if get_soroso(p, r) == 0 or get_soroso(q, r) == 0 or p * q * q * r > 140:
            continue

        a1 = np.random.randint(3, 10)
        b1 = np.random.randint(1, 8)
        c1 = np.random.randint(3, 10)
        d1 = np.random.randint(1, 8)

        if a1 - b1 <= 1 or c1 - d1 <= 1:
            continue

        a = soroso_select(A)
        b = soroso_select(B)

        E = A * B

        a2 = a1 - 1
        e1 = a * B
        e2 = b * A
        e3 = e1 + E
        e4 = e3 - e1
        e5 = a2 - b1

        res1 = e3 - e2

        if e2 <= e1 or e4 <= 0:
            continue


        c = soroso_select(C)
        d = soroso_select(D)

        F = p * q * r
        c2 = c1 - 1
        f1 = c * r
        f2 = d * q

        if f2 <= f1:
            continue

        f3 = f1 + F
        f4 = f3 - f2
        f5 = c2 - d1
        F1 = F * q
        f6 = f4 * q


        if e4 != f6:

            if (e5 + (res1 / e4)) > (f5 + (f6 / F1)):
                cor_sign = "&gt;"
            elif (e5 + (res1 / e4)) < (f5 + (f6 / F1)):
                cor_sign = "&lt;"
            elif (e5 + (res1 / e4)) == (f5 + (f6 / F1)):
                cor_sign = "="
            elif e5 == f5 and res1 == f6 and e4 == F1:
                cor_sign = "="
            else:
                continue

            flag = False



    exp_1 = '%d {%d} over {%d} `-` %d {%d} over {%d}' % (a1, a, A, b1, b, B)
    exp_2 = '%d {%d} over {%d} `-` %d {%d} over {%d}' % (c1, c, C, d1, d, D)

    frac_1 = '%d {%d} over {%d}' % (e5, res1, e4)
    frac_2 = '%d {%d} over {%d}' % (f5, f6, F1)

    exp_3 = '%s `=` %d {%d} over {%d} `-` %d {%d} over {%d} $$/수식$$\n$$수식$$ `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %s' \
            '' % (exp_1, a1, e1, E, b1, e2, E, a2, e3, E, b1, e2, E, frac_1)
    exp_4 = '%s `=` %d {%d} over {%d} `-` %d {%d} over {%d} $$/수식$$\n$$수식$$`=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %d {%d} over {%d} `=` %s' \
            '' % (exp_2, c1, f1, F, d1, f2, F, c2, f3, F, d1, f2, F, f5, f4, F, frac_2)

    exp_5 = '%s `%s` %s' % (frac_1, cor_sign, frac_2)
    exp_6 = '%s `%s` %s' % (exp_1, cor_sign, exp_2)



    stem = stem.format(exp_1=exp_1, exp_2=exp_2, box=box, right=right, equal=equal, left=left)
    answer = answer.format(cor_sign=cor_sign)
    comment = comment.format(exp_3=exp_3, exp_4=exp_4, exp_5=exp_5, exp_6=exp_6)

    return stem, answer, comment







    # flag = True
    # while flag:
    #     p, q, r = np.random.choice(np.arange(2, 8), 3)
    #     A = p * q * q
    #     B = r
    #     C = p * q
    #     D = p * r
    #     a1, c1 = np.random.choice(np.arange(3, 10), 2)
    #     b1, d1 = np.random.choice(np.arange(1, 8), 2)
    #     a = np.random.randint(1, A, 1)[0]
    #     b = np.random.randint(1, B, 1)[0]
    #     E = A * B
    #     if E <= 140 and check_simFrac(p, r) and check_simFrac(q, r) and check_simFrac(a, A) and check_simFrac(b, B):
    #         a2 = a1 - 1
    #         e1 = a * B
    #         e2 = b * A
    #         e3 = e1 + E
    #         e4 = e3 - e1
    #         e5 = a2 - b1
    #         c = np.random.randint(1, C, 1)[0]
    #         d = np.random.randint(1, D, 1)[0]
    #         F = p * q * r
    #         c2 = c1 - 1
    #         f1 = c * r
    #         f2 = d * q
    #         f3 = f1 + F
    #         f4 = f3 - f2
    #         f5 = c2 - d1
    #         F1 = F * q
    #         f6 = f4 * q
    #         if e4 > 0 and check_simFrac(c, C) and check_simFrac(d, D) and f2 - f1 > 0 and e4 != f6:
    #             cor_sign = right if e4 > f6 else left
    #             flag = False
    #
    # exp_1 = '%d {%d} over {%d} `-` %d {%d} over {%d}' % (a1, a, A, b1, b, B)
    # exp_2 = '%d {%d} over {%d} `-` %d {%d} over {%d}' % (c1, c, C, d1, d, D)
    #
    # frac_1 = '%d {%d} over {%d}' % (e5, e4, E)
    # frac_2 = '%d {%d} over {%d}' % (f5, f6, F1)
    # exp_3 = '%s `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %s' \
    #         '' % (exp_1, a1, e1, E, b1, e2, E, a2, e3, E, b1, e2, E, frac_1)
    # exp_4 = '%s `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %d {%d} over {%d} `=` %s' \
    #         '' % (exp_2, c1, f1, F, d1, f2, F, c2, f3, F, d1, f2, F, f5, f4, F, frac_2)
    # exp_5 = '%s `%s` %s' % (frac_1, cor_sign, frac_2)
    # exp_6 = '%s `%s` %s' % (exp_1, cor_sign, exp_2)
















































# 5-1-5-50
def fractionaddsub515_Stem_029():
    stem = "$$수식$${frac_1}$$/수식$$보다 $$수식$${frac_2}$$/수식$$ 작은 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${exp_1}$$/수식$$\n\n"


    flag = True
    while flag:
        A, B = np.random.choice(np.arange(2, 16), 2)
        a = np.random.randint(1, A, 1)[0]
        b = np.random.randint(1, B, 1)[0]
        b1, a1 = sorted(list(np.random.choice(np.arange(1, 10), 2, False)))
        C = A * B
        c1 = a * B
        c2 = b * A
        c3 = c1 - c2
        c4 = a1 - b1
        if check_simFrac(A, B) and 10 <= C < 100 and c3 > 0:
            flag = False

    frac_1 = '%d {%d} over {%d}' % (a1, a, A)
    frac_2 = '%d {%d} over {%d}' % (b1, b, B)

    # cor_frac = '%d {%d} over {%d}' % (c4, c3, C)

    boonja, boonmo = get_giyak(c3, C)
    cor_frac = '%d {%d} over {%d}' % (c4, boonja, boonmo)

    exp_1 = '%s `-` %s `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %s' % (frac_1, frac_2, a1, c1, C, b1, c2, C, cor_frac)


    stem = stem.format(frac_1=frac_1, frac_2=frac_2)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(exp_1=exp_1)

    return stem, answer, comment



















































# 5-1-5-53
def fractionaddsub515_Stem_030():
    stem = "두 수를 골라 차가 가장 큰 뺄셈식을 만들어 그 차를 구해 보세요.\n$$표$$$$수식$${frac_4}$$/수식$$    $$수식$${frac_5}$$/수식$$    $$수식$${frac_6}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "두 수의 차가 가장 크게 되려면 가장 큰 수에서 가장 작은 수를 빼야 합니다.\n" \
              "$$수식$${exp_1}$$/수식$$이므로 가장 큰 수는 $$수식$${frac_1}$$/수식$$, 가장 작은 수는 $$수식$${frac_3}$$/수식$$입니다.\n" \
              "$$수식$${exp_2}$$/수식$$\n\n"


    flag = True
    while flag:
        p, q, r = np.random.choice(np.arange(2, 8), 3)

        if get_soroso(q, r) == 0:
            continue

        A = p * q
        B = p * r
        C = np.random.choice([p, q, r, q * r], 1)[0]
        b1, c1, a1 = sorted(list(np.random.choice(np.arange(1, 10), 3, False)))

        a = soroso_select(A)
        b = soroso_select(B)
        c = soroso_select(C)

        D = p * q * r

        if D > 99:
            continue

        a2 = a1 - 1
        d1 = a * r
        d2 = b * q

        if d2 <= d1:
            continue

        d3 = r + D
        d4 = d3 - d2
        d5 = a2 - b1

        D1, d6 = get_giyak(D, d4)

        break

    frac_1 = '%d {1} over {%d}' % (a1, A)
    frac_3 = '%d {%d} over {%d}' % (b1, b, B)
    frac_2 = '%d {%d} over {%d}' % (c1, c, C)

    frac_4, frac_5, frac_6 = np.random.choice([frac_1, frac_2, frac_3], 3, False)

    cor_frac = '%d {%d} over {%d}' % (d5, d6, D1)

    exp_1 = '%s `%s` %s `%s` %s' % (frac_1, left, frac_2, left, frac_3)
    exp_2 = '%s `-` %s `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %s' \
            '' % (frac_1, frac_3, a1, r, D, b1, d2, D, a2, d3, D, b1, d2, D, cor_frac)


    stem = stem.format(frac_4=frac_4, frac_5=frac_5, frac_6=frac_6)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(exp_1=exp_1, exp_2=exp_2, frac_1=frac_1, frac_3=frac_3)

    return stem, answer, comment





    # flag = True
    # while flag:
    #     p, q, r = np.random.choice(np.arange(2, 8), 3)
    #     A = p * q
    #     B = p * r
    #     C = np.random.choice([p, q, r, q * r], 1)[0]
    #     b1, c1, a1 = sorted(list(np.random.choice(np.arange(1, 10), 3, False)))
    #     a = np.random.randint(1, A, 1)[0]
    #     b = np.random.randint(1, B, 1)[0]
    #     c = np.random.randint(1, C, 1)[0]
    #     D = p * q * r
    #     a2 = a1 - 1
    #     d1 = a * r
    #     d2 = b * q
    #     d3 = d1 + D
    #     d4 = d3 - d2
    #     d5 = a2 - b1
    #     n = get_gcd(D, d4)
    #     D1 = D // n
    #     d6 = d4 // n
    #
    #     if check_simFrac(q, r) and D <= 99 and check_simFrac(a, A) and check_simFrac(b, B) and check_simFrac(c, C) and d2 - d1 > 0:
    #         flag = False
    #
    # frac_1 = '%d {1} over {%d}' % (a1, A)
    # frac_2 = '%d {%d} over {%d}' % (b1, b, B)
    # frac_3 = '%d {%d} over {%d}' % (c1, c, C)
    #
    # frac_4, frac_5, frac_6 = np.random.choice([frac_1, frac_2, frac_3], 3, False)
    #
    # cor_frac = '%d {%d} over {%d}' % (d5, d6, D1)
    #
    # exp_1 = '%s `%s` %s `%s` %s' % (frac_1, left, frac_2, left, frac_3)
    # exp_2 = '%s `-` %s `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %s' \
    #         '' % (frac_1, frac_3, a1, d1, D, b1, d2, D, a2, d3, D, b1, d2, D, cor_frac)














































# 5-1-5-56
def fractionaddsub515_Stem_031():
    stem = "제주 올레길은 $$수식$$2007$$/수식$$년 $$수식$$9$$/수식$$월에 개발되어 도보 여행길로 주목을 받고 있습니다. {who}는 거리가 $$수식$${problem1}``rm {{km}}`$$/수식$$인 올레 제$$수식$${problem2}$$/수식$$코스를 $$수식$${problem3}``rm {{km}}`$$/수식$$만큼 걸었습니다. 남은 거리는 몇 $$수식$$rm {{km}}`$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${answer_num}``rm {{km}}$$/수식$$\n"
    comment = "(해설)\n" \
              "올레 제$$수식$${explain1}$$/수식$$코스 중에서 남은 거리는\n" \
              "$$수식$${explain2} LEFT ( rm {{km}} RIGHT )$$/수식$$입니다.\n\n"



    who = ["지우", "나래", "석우", "수지", "준수", "시아", "윤아", "솔미", "혁재", "권기"][np.random.randint(0, 10)]

    N, a1, a, A = random.choice([(2, 17, 1, 5), (6, 14, 2, 5), (7, 15, 1, 10), (8, 17, 3, 5), (9, 8, 4, 5),
                                 (10, 15, 1, 2), (11, 21, 1, 2), (12, 17, 3, 5), (13, 15, 3, 10), (14, 19, 3, 10),
                                 (16, 17, 4, 5), (17, 18, 2, 5), (18, 18, 1, 5), (19, 18, 3, 5), (10, 17, 2, 5),
                                 (21, 11, 3, 10)])
    while 1:
        p = random.randint(2, 4)
        if A * p <= 20:
            break

    B = A * p

    while 1:
        b = random.randint(1, B - 1)
        if is_gcd(b, B) and b - a * p >= 1:
            break

    b1 = random.randint(3, 6)
    a2 = a * p
    a3 = a1 - 1
    a4 = a2 + B
    c2 = a3 - b1
    c1, C = reduce(a4 - b, B)

    problem1 = '{0} {{ {1} }} over {{ {2} }}'.format(a1, a, A)
    problem2 = N
    problem3 = '{0} {{ {1} }} over {{ {2} }}'.format(b1, b, B)
    explain1 = N
    explain2 = '{0} `-` {1} `=` {2} {{ {3} }} over {{ {4} }} `-` {5} {{ {6} }} over {{ {4} }} $$/수식$$\n$$수식$$`=` {7} {{ {8} }} over {{ {4} }} `-` {5} {{ {6} }} over {{ {4} }} `=`  {9} {{ {10} }} over {{ {11} }}' \
        .format(problem1, problem3, a1, a2, B, b1, b, a3, a4, c2, c1, C)
    answer_num = '{0} {{ {1} }} over {{ {2} }}'.format(c2, c1, C)


    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, who=who)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2)

    return stem, answer, comment




















































# 5-1-5-57
def fractionaddsub515_Stem_032():
    stem = "계산 결과가 가장 작은 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$    ㉡ $$수식$${problem2}$$/수식$$    ㉢ $$수식$${problem3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{answer_sign}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${explain1}$$/수식$$\n" \
              "㉡ $$수식$${explain2}$$/수식$$\n" \
              "㉢ $$수식$${explain3}$$/수식$$\n" \
              "따라서 $$수식$${explain4}$$/수식$$이므로 계산 결과가 가장 작은 것은 {explain5}입니다.\n\n"


    while 1:
        p, q = random.sample(range(2, 8), 2)
        if is_gcd(p, q) and p * p * q <= 147:
            break

    A, B, C, D, E, F = p, p * q, p * q, p * p, p * p, q

    a1, c1, e1 = random.sample(range(2, 10), 3)
    b1, d1, f1 = a1 - 1, c1 - 1, e1 - 1

    while 1:
        a, b = random.randint(1, A - 1), random.randint(1, B - 1)
        if is_gcd(a, A) and is_gcd(b, B) and b - a * q >= 1:
            break

    while 1:
        c, d = random.randint(1, C - 1), random.randint(1, D - 1)
        if is_gcd(c, C) and is_gcd(d, D) and d * q - c * p >= 1 and d * q - c * p != b - a * q:
            break

    while 1:
        e, f = random.randint(1, E - 1), random.randint(1, F - 1)
        if is_gcd(e, E) and is_gcd(f, F) and f * p * p - e * q >= 1 and f * p * p - e * q != b - a * q \
                and f * p * p - e * q != d * q - c * p:
            break

    a2, a3, a4, a5 = a * q, a1 - 1, a * q + B, a * q + B - b
    G, g1 = B * p, a5 * p
    c2, d2, c3, c4, g2 = c * p, d * q, c1 - 1, c * p + G, c * p + G - d * q
    e2 = e * q;
    f2 = f * p * p;
    e3 = e1 - 1;
    e4 = e2 + G;
    g3 = e4 - f2
    tmp = [g1, g2, g3]
    tmp.sort(reverse=True)
    g4, g5, g6 = tmp

    if g6 == g1:
        X = '㉠'
    elif g6 == g2:
        X = '㉡'
    else:
        X = '㉢'

    problem1 = '{0} {{ {1} }} over {{ {2} }} `-` {3} {{ {4} }} over {{ {5} }}'.format(a1, a, A, b1, b, B)
    problem2 = '{0} {{ {1} }} over {{ {2} }} `-` {3} {{ {4} }} over {{ {5} }}'.format(c1, c, C, d1, d, D)
    problem3 = '{0} {{ {1} }} over {{ {2} }} `-` {3} {{ {4} }} over {{ {5} }}'.format(e1, e, E, f1, f, F)

    explain1 = '{0} `=` {1} {{ {2} }} over {{ {3} }} `-` {4} {{ {5} }} over {{ {3} }} $$/수식$$\n$$수식$$`=` ' \
               '{6} {{ {7} }} over {{ {3} }} `-` {4} {{ {5} }} over {{ {3} }} `=` ' \
               '{{ {8} }} over {{ {3} }} `=` {{ {9} }} over {{ {10} }}' \
        .format(problem1, a1, a2, B, b1, b, a3, a4, a5, g1, G)

    explain2 = '{0} `=` {1} {{ {2} }} over {{ {3} }} `-` {4} {{ {5} }} over {{ {3} }} $$/수식$$\n$$수식$$`=` ' \
               '{6} {{ {7} }} over {{ {3} }} `-` {4} {{ {5} }} over {{ {3} }} `=` ' \
               '{{ {8} }} over {{ {3} }}' \
        .format(problem2, c1, c2, G, d1, d2, c3, c4, g2)

    explain3 = '{0} `=` {1} {{ {2} }} over {{ {3} }} `-` {4} {{ {5} }} over {{ {3} }} $$/수식$$\n$$수식$$`=` ' \
               '{6} {{ {7} }} over {{ {3} }} `-` {4} {{ {5} }} over {{ {3} }} `=` ' \
               '{{ {8} }} over {{ {3} }}' \
        .format(problem3, e1, e2, G, f1, f2, e3, e4, g3)

    answer_sign = X
    explain4 = '{0} over {1} `&gt;` {2} over {1} `&gt;` {3} over {1}'.format(g4, G, g5, g6)
    explain5 = X


    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             explain5=explain5)

    return stem, answer, comment





















































# 5-1-5-58
def fractionaddsub515_Stem_033():
    stem = "{P1}께서 {S}{post1} $$수식$${problem1}``rm L$$/수식$$ 담아 오셨습니다. 그중에서 {P2}댁에 $$수식$${problem2}``rm L$$/수식$$를 드렸다면 남은 {S}{post2} 몇 $$수식$$rm L`$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${answer_num}``rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$남은 {S}의 " \
              "양$$수식$$RIGHT )$$/수식$$ \n $$수식$$ ` = ` {explain1} ` LEFT ( rm L RIGHT )$$/수식$$입니다.\n\n"


    P1, P2 = random.sample(['할머니', '이모', '고모', '외할머니', '삼촌', '큰아버지', '외삼촌'], 2)
    S = random.choice(['복분자 주스', '매실청', '백년초즙', '식초', '오디즙'])

    post1 = '를' if josa_check(S[-1]) == ' ' else '을'
    post2 = '는' if josa_check(S[-1]) == ' ' else '은'

    while 1:
        A = random.randint(2, 15)
        B = random.randint(2, 15)
        if is_gcd(A, B) and 10 <= A * B <= 99:
            break

    while 1:
        a = random.randint(1, A - 1)
        b = random.randint(1, B - 1)
        if is_gcd(a, A) and is_gcd(b, B) and b * A - a * B >= 1:
            break

    while 1:
        a1 = random.randint(3, 5)
        b1 = random.randint(1, 5)
        if a1 - b1 >= 2:
            break


    C = A * B
    a2 = a1 - 1
    c1 = a * B
    c2 = b * A
    c3 = c1 + C
    c4 = c3 - c2
    c5 = a2 - b1
    c6, C1 = reduce(c3 - c2, C)

    problem1 = '{0} {{ {1} }} over {{ {2} }}'.format(a1, a, A)
    problem2 = '{0} {{ {1} }} over {{ {2} }}'.format(b1, b, B)
    explain1 = '{0} `-` {1} `=` {2} {{ {3} }} over {{ {4} }} `-` {5} {{ {6} }} over {{ {4} }} $$/수식$$\n$$수식$$ `=`' \
               ' {7} {{ {8} }} over {{ {4} }} `-` {5} {{ {6} }} over {{ {4} }} `=`  {9} {{ {10} }} over {{ {11} }}' \
        .format(problem1, problem2, a1, c1, C, b1, c2, a2, c3, c5, c6, C1)
    answer_num = '{0} {{ {1} }} over {{ {2} }}'.format(c5, c6, C1)


    stem = stem.format(problem1=problem1, problem2=problem2, P1=P1, P2=P2, S=S, post1=post1, post2=post2)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, S=S)

    return stem, answer, comment

















































# 5-1-5-59
def fractionaddsub515_Stem_034():
    stem = "실과 시간에 {S1}{S1_josa} 만들고 있습니다. {P1}{P1_josa} {S2}{S2_josa} $$수식$${frac_1}$$/수식$$개 사용했고, {P2}{P2_josa} $$수식$${frac_2}$$/수식$$개 사용했습니다. 누가 {S2}{S2_josa} 몇 개 더 많이 사용했나요?\n"
    answer = "(정답)\n{P3}, $$수식$${frac_7}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${frac_1} `{X}` {frac_2}$$/수식$$이므로 {P3}{P3_josa1} {S2}{S2_josa} 더 많이 사용했습니다.\n" \
              "{P3}{P3_josa2} {S2}{S2_josa} $$수식$${frac_3} `-` {frac_4} `=` {frac_5} `-` {frac_6} `=` {frac_7} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$ 더 많이 사용했습니다.\n\n"



    S1, S2 = random.choice([('자동차 모형', '찰흙'), ('공룡 모형', '찰흙'), ('샐러드', '사과'), ('샐러드', '귤'), ('샐러드', '토마토')])
    S1_josa = "를" if josa_check(S1[-1]) == ' ' else "을"
    S2_josa = "를" if josa_check(S2[-1]) == ' ' else "을"

    flag = True
    while flag:
        P1, P2 = np.random.choice(person_nam + person_yeo, 2, replace=False)
        P1_josa = "는" if josa_check(P1[-1]) == ' ' else "이는"
        P2_josa = "는" if josa_check(P2[-1]) == ' ' else "이는"

        p = random.randint(2, 4)
        B = random.randint(2, 9)
        A = B * p
        a1, b1 = np.random.choice(range(1, 6), 2, replace=False)
        a = random.randint(1, A - 1)
        b = random.randint(1, B - 1)

        if get_gcd(a, A) == 1 and get_gcd(b, B) == 1:
            if a1 > b1 and a - b * p < 1:
                continue
            elif a1 < b1 and b * p - a < 1:
                continue

            if a1 > b1:
                C, c, c1 = A, a, a1
                D, d, d1 = B, b, b1
                e1, e2 = a, b * p
                P3 = P1
                X = "&gt;"
            elif a1 < b1:
                C, c, c1 = B, b, b1
                D, d, d1 = A, a, a1
                e1, e2 = b * p, a
                P3 = P2
                X = "&lt;"

            E = A
            e3 = e1 - e2
            e4 = c1 - d1
            n = get_gcd(E, e3)
            E1 = E // n
            e5 = e3 // n

            P3_josa1, P3_josa2 = ['가', '는'] if josa_check(P3[-1]) == ' ' else ['이가', '이는']

            flag = False

    frac_1 = "%s {%s} over {%s}" % (a1, a, A)
    frac_2 = "%s {%s} over {%s}" % (b1, b, B)
    frac_3 = "%s {%s} over {%s}" % (c1, c, C)
    frac_4 = "%s {%s} over {%s}" % (d1, d, D)
    frac_5 = "%s {%s} over {%s}" % (c1, e1, E)
    frac_6 = "%s {%s} over {%s}" % (d1, e2, E)
    frac_7 = "%s {%s} over {%s}" % (e4, e5, E1)


    stem = stem.format(S1=S1, S1_josa=S1_josa, S2=S2, S2_josa=S2_josa, P1=P1, P1_josa=P1_josa, P2=P2, P2_josa=P2_josa,
                       frac_1=frac_1, frac_2=frac_2)
    answer = answer.format(P3=P3, frac_7=frac_7)
    comment = comment.format(S2=S2, S2_josa=S2_josa, P3=P3, P3_josa1=P3_josa1, P3_josa2=P3_josa2, X=X,
                             frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4, frac_5=frac_5,
                             frac_6=frac_6, frac_7=frac_7)

    return stem, answer, comment













































# 5-1-5-60
def fractionaddsub515_Stem_035():
    stem = "$$수식$${frac_1}$$/수식$$에 어떤 수를 더했더니 $$수식$${frac_2}$$/수식$${a_josa} 되었습니다. 어떤 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${frac_6}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 $$수식$${box}$$/수식$$라고 하면 $$수식$${frac_1} `+` {box} `=` {frac_2}$$/수식$$에서\n" \
              "$$수식$${box} `=` {frac_2} `-` {frac_1} `=` {frac_3} `-` {frac_4}$$/수식$$\n$$수식$$ `=` {frac_5} `-` {frac_4} `=` {frac_6}$$/수식$$입니다.\n" \
              "따라서 어떤 수는 $$수식$${frac_6}$$/수식$$입니다.\n\n"


    flag = True
    while flag:
        A, B = np.random.choice(range(2, 16), 2, replace=False)

        if get_gcd(A, B) == 1 and 10 <= A * B <= 99:
            a = random.randint(1, A - 1)
            b = random.randint(1, B - 1)

            a_josa = num_josa(a)[3]

            if get_gcd(A, a) == 1 and get_gcd(b, B) == 1 and b * A - a * B >= 1:
                a1 = random.randint(3, 9)
                b1 = random.randint(1, 7)

                if a1 - b1 >= 2:
                    C = A * B
                    a2 = a1 - 1

                    c1 = a * B
                    c2 = b * A
                    c3 = c1 + C
                    c4 = c3 - c2
                    c5 = a2 - b1

                    n = get_gcd(C, c4)
                    C1 = C // n
                    c6 = c4 // n

                    # 대분수에서 자연수가 0이 되지 않도록 제한
                    if c5 >= 1:
                        flag = False

    frac_1 = "%s {%s} over {%s}" % (b1, b, B)
    frac_2 = "%s {%s} over {%s}" % (a1, a, A)
    frac_3 = "%s {%s} over {%s}" % (a1, c1, C)
    frac_4 = "%s {%s} over {%s}" % (b1, c2, C)
    frac_5 = "%s {%s} over {%s}" % (a2, c3, C)
    frac_6 = "%s {%s} over {%s}" % (c5, c6, C1)


    stem = stem.format(frac_1=frac_1, frac_2=frac_2, a_josa=a_josa)
    answer = answer.format(frac_6=frac_6)
    comment = comment.format(box=box, frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4, frac_5=frac_5,
                             frac_6=frac_6)

    return stem, answer, comment
















































# 5-1-5-62
def fractionaddsub515_Stem_036():
    stem = "{name1}{josa1}의 몸무게는 동생보다 $$수식$${s_exp1}`rm kg$$/수식$$ 더 무겁습니다. {name1}{josa1}의 몸무게가 $$수식$${s_exp2}`rm kg$$/수식$$일 때, {name1}{josa1}와 동생의 몸무게의 합은 몇 $$수식$$rm kg$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${ans_frac}`rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${name1}{josa1} 동생의 몸무게$$수식$$RIGHT )$$/수식$$\n$$수식$$ ` = ` {c_exp1}$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${name1}{josa1}와 동생의 몸무게의 합$$수식$$RIGHT )$$/수식$$\n$$수식$$ ` = ` {c_exp2}$$/수식$$\n\n"


    name1 = np.random.choice(np.array(person_nam + person_yeo))
    josa1 = '' if josa_check(name1[-1]) == " " else '이'

    while True:
        A, B = np.random.randint(4, 16, size=2)
        a = np.random.randint(1, A // 2)
        b = np.random.randint(B // 2, B - 1)
        C = A * B
        a1 = np.random.randint(30, 40)
        b1 = np.random.randint(1, 5)
        a2 = a * B
        b2 = b * A
        a3 = a1 - 1
        a4 = a2 + C
        c = a4 - b2
        c1 = a3 - b1
        c2 = a2 + c
        c3 = a1 + c1
        c4 = c2 - C
        c5 = c3 + 1
        n = get_gcd(C, c4)
        C1 = C // n
        c6 = c4 // n

        if 10 <= A * B <= 60 and check_simFrac(A, a) and check_simFrac(B, b) and c2 > C:
            break

    s_exp1 = "%d {%d} over {%d}" % (b1, b, B)
    s_exp2 = "%d {%d} over {%d}" % (a1, a, A)

    c_exp1 = "%s `-` %s `=` %d {%d} over {%d} `-` %d {%d} over {%d} $$/수식$$\n$$수식$$`=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %d {%d} over {%d}" \
             % (s_exp2, s_exp1, a1, a2, C, b1, b2, C, a3, a4, C, b1, b2, C, c1, c, C)
    c_exp2 = "%s `+` %d {%d} over {%d} `=` %d {%d} over {%d} `+` %d {%d} over {%d} $$/수식$$\n$$수식$$`=` %d {%d} over {%d} `=` %d {%d} over {%d}" \
             % (s_exp2, c1, c, C, a1, a2, C, c1, c, C, c3, c2, C, c5, c6, C1)

    ans_frac = "%d {%d} over {%d}" % (c5, c6, C1)


    stem = stem.format(s_exp1=s_exp1, s_exp2=s_exp2, name1=name1, josa1=josa1)
    answer = answer.format(ans_frac=ans_frac)
    comment = comment.format(name1=name1, josa1=josa1, c_exp1=c_exp1, c_exp2=c_exp2)

    return stem, answer, comment





















































# 5-1-5-64
def fractionaddsub515_Stem_037():
    stem = "$$수식$${box}$$/수식$$ 안에 들어갈 수 있는 자연수는 모두 몇 개인가요?\n$$표$$ $$수식$${s_exp1}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${ans_num}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${c_exp1}$$/수식$$\n" \
              "$$수식$${c_exp2}$$/수식$$\n" \
              "따라서 $$수식$${c_exp3}$$/수식$$에서 $$수식$${box}$$/수식$$ 안에 들어갈 있는 자연수는 {c_exp4}{josa1} 모두 $$수식$${ans_num}$$/수식$$개 입니다.\n\n"


    while True:
        A, B = np.random.randint(2, 10, size=2)
        a = np.random.randint(1, A)
        b = np.random.randint(1, B)

        if not check_simFrac(A, B) or not check_simFrac(a, A) or not check_simFrac(b, B):
            continue

        p, q, r = np.random.randint(2, 8, size=3)

        F = p * q * r

        if F >= 100:
            continue

        C = p * q
        D = p * r
        c = np.random.randint(1, C)
        d = np.random.randint(1, D)

        if not check_simFrac(c, C) or not check_simFrac(d, D):
            continue

        c2 = c * r
        d2 = d * q

        if c2 >= d2:
            continue

        a1, b1 = np.random.randint(1, 4, size=2)
        c1 = np.random.randint(8, 10)
        d1 = np.random.randint(1, 3)

        a2 = a * B
        b2 = b * A
        E = A * B
        e = a2 + b2
        e1 = a1 + b1
        m = get_gcd(E, e)
        E1 = E // m
        e2 = e // m

        if e2 >= E1:
            continue

        c3 = c1 - 1
        c4 = c2 + F
        f = c4 - d2
        f1 = c3 - d1
        n = get_gcd(F, f)
        F1 = F // n
        f2 = f // n

        if a1 + b1 <= 4 and c1 - d1 >= 7:
            break

    s_exp1 = "%d {%d} over {%d} `+` %d {%d} over {%d} `&lt;` %s `&lt;` %d {%d} over {%d} `-` %d {%d} over {%d}" % (a1, a, A, b1, b, B, box, c1, c, C, d1, d, D)

    c_exp1 = "%d {%d} over {%d} `+` %d {%d} over {%d} `=` %d {%d} over {%d} + %d {%d} over {%d} `=` %d {%d} over {%d}" % (a1, a, A, b1, b, B, a1, a2, E, b1, b2, E, e1, e2, E1)

    c_exp2 = "%d {%d} over {%d} `-` %d {%d} over {%d} `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %d {%d} over {%d}"\
             % (c1, c, C, d1, d, D, c1, c2, F, d1, d2, F, c3, c4, F, d1, d2, F, f1, f2, F1)

    c_exp3 = "%d {%d} over {%d} `&lt;` %s `&lt;` %d {%d} over {%d}" % (e1, e2, E1, box, f1, f2, F1)
    c_exp4 = ", ".join(["$$수식$$%d$$/수식$$" % i for i in range(e1 + 1, f1 + 1)])

    ans_num = f1 - e1
    # josa1 = check_jongsung(f1)[4]
    josa1 = get_josa(f1, "로")


    stem = stem.format(box=box, s_exp1=s_exp1)
    answer = answer.format(ans_num=ans_num)
    comment = comment.format(box=box, josa1=josa1, c_exp1=c_exp1, c_exp2=c_exp2, c_exp3=c_exp3, c_exp4=c_exp4,
                             ans_num=ans_num)

    return stem, answer, comment







    # while True:
    #     A, B = np.random.randint(2, 10, size=2)
    #     a = np.random.randint(1, A)
    #     b = np.random.randint(1, B)
    #
    #     p, q, r = np.random.randint(2, 8, size=3)
    #     C = p * q
    #     D = p * r
    #     c = np.random.randint(1, C)
    #     d = np.random.randint(1, D)
    #
    #     a1, b1 = np.random.randint(1, 4, size=2)
    #     c1 = np.random.randint(8, 10)
    #     d1 = np.random.randint(1, 3)
    #
    #     a2 = a * B
    #     b2 = b * A
    #     E = A * B
    #     e = a2 + b2
    #     e1 = a1 + b1
    #     m = get_gcd(E, e)
    #     E1 = E // m
    #     e2 = e // m
    #     c2 = c * r
    #     d2 = d * q
    #     F = p * q * r
    #     c3 = c1 - 1
    #     c4 = c2 + F
    #     f = c4 - d2
    #     f1 = c3 - d1
    #     n = get_gcd(F, f)
    #     F1 = F // n
    #     f2 = f // n
    #
    #     if F < 100 and c2 < d2 and e2 < E1 and check_simFrac(A, B) and check_simFrac(a, A) and check_simFrac(b, B) and check_simFrac(c, C) and check_simFrac(d, D) and a1 + b1 <= 4 and c1 - d1 >= 7:
    #         break













































# 5-1-5-66
def fractionaddsub515_Stem_038():
    """

    :param r1: 분모의 최솟값 [int] {2:2}
    :param r2: 분모의 최댓값 [int] {16:16}
    :return:
    """
    stem = "{figure}{josa1} 담은 바구니의 무게가 $$수식$${s_exp1} ` rm kg$$/수식$$입니다. {figure}의 반을 팔고 무게를 재어 보니 $$수식$${s_exp2} ` rm kg$$/수식$$이었습니다. 빈 바구니의 무게는 몇 $$수식$$rm kg$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${ans_frac} ` rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${figure}의 반의 무게$$수식$$RIGHT )$$/수식$$\n$$수식$$ {c_exp1} LEFT ( rm kg RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$빈 바구니의 무게$$수식$$RIGHT )$$/수식$$\n$$수식$$ {c_exp2} LEFT ( rm kg RIGHT )$$/수식$$\n\n"


    figure = np.random.choice(np.array(["땅콩", '딸기', '방울토마토', '호두', '밤', '고구마', '감자', '방울토마토']))
    josa1 = "를" if josa_check(figure[-1]) == ' ' else '을'

    while True:
        A, B = np.random.randint(2, 16, size=2)
        a = np.random.randint(1, A)
        b = np.random.randint(1, B // 2 + 1)

        a1, b1 = random.choice([(4, 3), (6, 4), (7, 5), (8, 5), (9, 6)])
        C = A * B
        a2 = a * B
        b2 = b * A

        if check_simFrac(a, A) and check_simFrac(b, B) and a2 - b2 >= 1 and a2 - b2 * 2 >= 1 and A != B:
            break

    c = a2 - b2
    c1 = a1 - b1

    b3 = b1 - 1
    b4 = b2 + C
    c2 = b4 - c
    c3 = b3 - c1

    n = get_gcd(C, c2)
    C1 = C // n
    c4 = c2 // n

    s_exp1 = "%d {%d} over {%d}" % (a1, a, A)
    s_exp2 = "%d {%d} over {%d}" % (b1, b, B)

    c_exp1 = "`=` %s `-` %s `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %d {%d} over {%d}" % (s_exp1, s_exp2, a1, a2, C, b1, b2, C, c1, c, C)
    c_exp2 = "`=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %d {%d} over {%d} `-` %d {%d} over {%d} $$/수식$$\n$$수식$$`=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %d {%d} over {%d}"\
             % (b1, b, B, c1, c, C, b1, b2, C, c1, c, C, b3, b4, C, c1, c, C, c3, c4, C1)

    ans_frac = "%d {%d} over {%d}" % (c3, c4, C1)


    stem = stem.format(figure=figure, josa1=josa1, s_exp1=s_exp1, s_exp2=s_exp2)
    answer = answer.format(ans_frac=ans_frac)
    comment = comment.format(c_exp2=c_exp2, c_exp1=c_exp1, figure=figure)

    return stem, answer, comment


















































# 5-1-5-68
def fractionaddsub515_Stem_039():
    stem = "어떤 수에서 $$수식$${s_exp1}$$/수식$${josa1} 빼야 할 것을 잘못하여 더했더니 $$수식$${s_exp2}$$/수식$${josa2} 되었습니다. 바르게 계산한 값을 구해 보세요.\n"
    answer = "(정답)\n$$수식$${ans_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 $$수식$${box}$$/수식$$라고 하면 $$수식$${c_exp1}$$/수식$$입니다.\n" \
              "$$수식$${c_exp2}$$/수식$$\n" \
              "따라서 바르게 계산하면 \n$$수식$${c_exp3}$$/수식$$입니다.\n\n"


    while True:
        p = np.random.randint(2, 6)
        B = np.random.randint(2, 10)
        A = p * B
        a = np.random.randint(1, A)
        b = np.random.randint(1, B)
        a1 = np.random.randint(4, 11)
        b1 = np.random.randint(1, 5)

        a2 = a + A
        a3 = a1 - 1
        b2 = b * p

        c = a2 - b2
        c1 = a3 - b1
        c2 = c - b2
        c3 = c1 - b1
        n = get_gcd(A, c2)
        A1 = A // n
        c4 = c2 // n

        if check_simFrac(a, A) and check_simFrac(b, B) and a1 - b1 * 2 >= 2 and b2 > a and c > b2:
            break


    josa1 = check_jongsung(b)[2]
    josa2 = check_jongsung(a)[3]

    s_exp1 = "%d {%d} over {%d}" % (b1, b, B)
    s_exp2 = "%d {%d} over {%d}" % (a1, a, A)

    c_exp1 = "%s `+` %s `=` %s" % (box, s_exp1, s_exp2)

    c_exp2 = "%s `=` %s `-` %s `=` %s `-` %d {%d} over {%d} $$/수식$$\n$$수식$$`=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %d {%d} over {%d}"\
             % (box, s_exp2, s_exp1, s_exp2, b1, b2, A, a3, a2, A, b1, b2, A, c1, c, A)

    c_exp3 = "%d {%d} over {%d} `-` %d {%d} over {%d} `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %d {%d} over {%d}"\
             % (c1, c, A, b1, b, B, c1, c, A, b1, b2, A, c3, c4, A1)

    ans_frac = "%d {%d} over {%d}" % (c3, c4, A1)


    stem = stem.format(josa2=josa2, josa1=josa1, s_exp1=s_exp1, s_exp2=s_exp2)
    answer = answer.format(ans_frac=ans_frac)
    comment = comment.format(box=box, c_exp1=c_exp1, c_exp2=c_exp2, c_exp3=c_exp3)

    return stem, answer, comment





































# if __name__ == '__main__':
#     G5_FracPlusMinus_Stem_001()
#     G5_FracPlusMinus_Stem_002()
#     G5_FracPlusMinus_Stem_003()
#     G5_FracPlusMinus_Stem_004()
#     G5_FracPlusMinus_Stem_005()
#     G5_FracPlusMinus_Stem_006()
#     G5_FracPlusMinus_Stem_007()
#     G5_FracPlusMinus_Stem_008()
#     G5_FracPlusMinus_Stem_009()
#     G5_FracPlusMinus_Stem_010()
#     G5_FracPlusMinus_Stem_011()
#     G5_FracPlusMinus_Stem_012()
#     G5_FracPlusMinus_Stem_013()
#     G5_FracPlusMinus_Stem_014()
#     G5_FracPlusMinus_Stem_015()
#     G5_FracPlusMinus_Stem_016()
#     G5_FracPlusMinus_Stem_017()
#     G5_FracPlusMinus_Stem_018()
#     G5_FracPlusMinus_Stem_019()
#     G5_FracPlusMinus_Stem_020()
#     G5_FracPlusMinus_Stem_021()
#     G5_FracPlusMinus_Stem_022()
#     G5_FracPlusMinus_Stem_023()
#     G5_FracPlusMinus_Stem_024()
#     G5_FracPlusMinus_Stem_025()
#     G5_FracPlusMinus_Stem_026()
#     G5_FracPlusMinus_Stem_027()
#     G5_FracPlusMinus_Stem_028()
#     G5_FracPlusMinus_Stem_029()
#     G5_FracPlusMinus_Stem_030()
#     G5_FracPlusMinus_Stem_031()
#     G5_FracPlusMinus_Stem_032()
#     G5_FracPlusMinus_Stem_033()
#     G5_FracPlusMinus_Stem_034()
#     G5_FracPlusMinus_Stem_035()
#     G5_FracPlusMinus_Stem_036()
#     G5_FracPlusMinus_Stem_037()
#     G5_FracPlusMinus_Stem_038()
#     G5_FracPlusMinus_Stem_039()






