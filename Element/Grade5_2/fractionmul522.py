import codecs
import os
import random
import numpy as np





PATH = '/home/boin-service/Visang/Dictionary/'



person_nam = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XY.txt'), 'r', 'utf-8').readlines()]
person_yeo = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XX.txt'), 'r', 'utf-8').readlines()]


multiple_choice_nums = {0: '①', 1: '②', 2: '③', 3: '④', 4: '⑤'}
multiple_choice_hangul = {0: '㉠', 1: '㉡', 2: '㉢', 3: '㉣', 4: '㉤'}


box = boxblank = '□'





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










def josa_check(name):
    '''
    한글 단어 조사 확인
    :param name:
    :return:
    '''
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
















def postposition(num, flag=0):
    num = abs(num)
    num_str = str(num)
    num = int(num_str[-1])

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









def get_josa(a, b):
    if b == "라면" or b == "이라면":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "라면"
        else:
            return "이라면"

















# 5-2-2-02
def fractionmul522_Stem_001():
    stem = "계산 결과 가장 작은 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$    ㉡ $$수식$${problem2}$$/수식$$    ㉢ $$수식$${problem3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{answer_sign}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${explain1}$$/수식$$\n" \
              "㉡ $$수식$${explain2}$$/수식$$\n" \
              "㉢ $$수식$${explain3}$$/수식$$\n" \
              "$$수식$${explain4}$$/수식$$이므로 계산 결과가 가장 작은 것은 {explain5}입니다.\n\n"


    while 1:
        a1 = random.randint(21, 49)
        a2 = random.randint(2, 9)
        if is_gcd(a2, a1):
            a3 = 1
            a4 = random.randint(2, 9)
            a5 = a1 + a2
            a6, a7 = reduce(a5 * a4, a1)
            if a7 != 1 and a6 < 100:
                a_result = a6 / a7
                break

    a8 = a6 // a7
    a9 = a6 % a7
    prob1 = '{0} {{ {1} }} over {{ {2} }} `TIMES` {3}'.format(a3, a2, a1, a4)
    equ1 = '{0} `=` {{ {1} }} over {{ {2} }} `TIMES` {3} `=` {{ {4} }} over {{ {5} }} `=` ' \
           '{6} {{ {7} }} over {{ {8} }}'.format(prob1, a5, a1, a4, a6, a7, a8, a9, a7)

    while 1:
        b1 = random.randint(2, 9)
        b2 = random.randint(2, 9)
        if is_gcd(b2, b1) and b1 > b2:
            b3 = 1
            b4 = random.randint(2, 9)
            b5 = b1 + b2
            b6, b7 = reduce(b5 * b4, b1)
            b_result = b6 / b7
            if b7 != 1 and a_result != b_result and b6 < 100:
                break

    b8 = b6 // b7
    b9 = b6 % b7
    prob2 = '{0} {{ {1} }} over {{ {2} }} `TIMES` {3}'.format(b3, b2, b1, b4)
    equ2 = '{0} `=` {{ {1} }} over {{ {2} }} `TIMES` {3} `=` {{ {4} }} over {{ {5} }} `=` ' \
           '{6} {{ {7} }} over {{ {8} }}'.format(prob2, b5, b1, b4, b6, b7, b8, b9, b7)

    while 1:
        c1, c3 = random.choice([(12, 15), (12, 18), (14, 18), (14, 21), (15, 18), (15, 21), (16, 18), (16, 20)])
        c2 = random.randint(2, 9)
        if is_gcd(c1, c2) and c2 < c1:
            c4, c5 = reduce(c2 * c3, c1)
            c_result = c4 / c5
            if c5 != 1 and c_result != a_result and c_result != b_result:
                break

    c6 = c4 // c5
    c7 = c4 % c5
    prob3 = '{{ {0} }} over {{ {1} }} `TIMES` {2}'.format(c2, c1, c3)
    equ3 = '{0} `=` {{ {1} }} over {{ {2} }} `=` {3} {{ {4} }} over {{ {5} }}'.format(prob3, c4, c5, c6, c7, c5)

    lst = [[prob1, equ1, a_result, '{0} {{ {1} }} over {{ {2} }}'.format(a8, a9, a7)],
           [prob2, equ2, b_result, '{0} {{ {1} }} over {{ {2} }}'.format(b8, b9, b7)],
           [prob3, equ3, c_result, '{0} {{ {1} }} over {{ {2} }}'.format(c6, c7, c5)]]

    random.shuffle(lst)

    problem1, problem2, problem3 = lst[0][0], lst[1][0], lst[2][0]
    explain1, explain2, explain3 = lst[0][1], lst[1][1], lst[2][1]

    lst[0].append('㉠')
    lst[1].append('㉡')
    lst[2].append('㉢')

    lst.sort(key=lambda x: x[2])

    explain4 = '{0} `&lt;` {1} `&lt;` {2}'.format(lst[0][3], lst[1][3], lst[2][3])
    explain5 = lst[0][4]
    answer_sign = explain5


    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3,
                             explain4=explain4, explain5=explain5)

    return stem, answer, comment











































# 5-2-2-05
def fractionmul522_Stem_002():
    stem = "$$수식$${boxblank}$$/수식$$ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${problem1}~~{boxblank}~~{problem2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${answer_sign}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$\n" \
              "$$수식$${explain2}$$/수식$$이므로 $$수식$${explain3}$$/수식$$입니다.\n\n"


    while 1:
        a1, a3 = random.choice([(12, 15), (12, 18), (14, 18), (14, 21), (15, 18), (15, 21), (16, 18), (16, 20)])
        a2 = random.randint(2, 9)
        if is_gcd(a1, a2):
            a4, a5 = reduce(a3, a1)
            if a5 != 1 and a4 != 1:
                break

    a6 = a4 * a2
    a7 = a6 // a5
    a8 = a6 % a5

    prob1 = '{{ {0} }} over {{ {1} }} `TIMES` {2}'.format(a2, a1, a3)
    prob2 = '{0} {{ {1} }} over {{ {2} }}'.format(a7, a8, a5)

    explain1 = '{0} `=` {{ {1} `TIMES` {2} }} over {{ {3} }} `=` {{ {4} }} over {{ {5} }} `=` {6}' \
        .format(prob1, a2, a4, a5, a6, a5, prob2)

    a_result = a6 / a5

    b1 = random.randint(2, 9)
    b2 = 1
    b3 = 2
    b_result = (b1 * b3 + 1) / 2
    prob3 = '{0} {{ {1} }} over  {{ {2} }}'.format(b1, b2, b3)

    lst = [[a_result, prob1, prob2], [b_result, prob3, prob3]]
    random.shuffle(lst)
    problem1, problem2 = lst[0][1], lst[1][1]

    answer_sign = '&gt;' if lst[0][0] > lst[1][0] else '&lt;' if lst[0][0] < lst[1][0] else '='
    explain2 = '{0} `{1}` {2}'.format(lst[0][2], answer_sign, lst[1][2])
    explain3 = '{0} `{1}` {2}'.format(lst[0][1], answer_sign, lst[1][1])


    stem = stem.format(problem1=problem1, problem2=problem2, boxblank=boxblank)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3)

    return stem, answer, comment









































# 5-2-2-07
def fractionmul522_Stem_003():
    stem = "계산 결과를 비교하여 $$수식$${boxblank}$$/수식$$ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${problem1}~~{boxblank}~~{problem2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${answer_sign}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$\n" \
              "$$수식$${explain2}$$/수식$$\n" \
              "$$수식$${explain3}$$/수식$$이므로 $$수식$${explain4}$$/수식$$입니다.\n\n"


    while 1:
        a1, a4 = random.choice([(12, 15), (12, 18), (14, 18), (14, 21), (15, 18), (15, 21), (16, 18), (16, 20)])
        a2 = random.randint(2, 9)
        a3 = random.randint(2, 9)
        if is_gcd(a1, a2):
            a5 = a3 * a1 + a2
            a6, a7 = reduce(a4, a1)
            a8 = a5 * a6
            if a7 != 1 and a6 != 1 and a8 < 100:
                break

    a9 = a8 // a7
    a10 = a8 % a7

    a_prob1 = ' {0} {{ {1} }} over {{ {2} }} `TIMES` {3}'.format(a3, a2, a1, a4)
    a_prob2 = '{0} {{ {1} }} over {{ {2} }}'.format(a9, a10, a7)
    a_exp1 = '{0} `=` {{ {1} }} over {{ {2} }} `TIMES` {3} `=` {{ {4} `TIMES` {5} }} over {{ {6} }} `=` ' \
             '{{ {7} }} over {{ {8} }} `=` {9}'.format(a_prob1, a5, a1, a4, a5, a6, a7, a8, a7, a_prob2)

    a_result = a8 / a7

    while 1:
        b6 = random.randint(2, 9)
        b1 = random.randint(2, 9)
        b2 = random.randint(2, 9)
        b3 = a3 - 1
        b4 = b1 * b6
        if is_gcd(b1, b2) and b2 < b1:
            b5 = b1 * b3 + b2
            b7 = b5 * b6
            if b7 < 100:
                break

    b_result = b7
    b_prob1 = ' {0} {{ {1} }} over {{ {2} }} `TIMES` {3}'.format(b3, b2, b1, b4)
    b_prob2 = b7
    b_exp1 = '{0} `=` {{ {1} }} over {{ {2} }} `TIMES` {3} `=` {4} `TIMES` {5} `=` {6}' \
        .format(b_prob1, b5, b1, b4, b5, b6, b_prob2)

    lst = [[a_result, a_prob1, a_prob2, a_exp1], [b_result, b_prob1, b_prob2, b_exp1]]
    random.shuffle(lst)
    problem1, problem2 = lst[0][1], lst[1][1]
    explain1, explain2 = lst[0][3], lst[1][3]

    answer_sign = '&gt;' if lst[0][0] > lst[1][0] else '&lt;' if lst[0][0] < lst[1][0] else '='

    explain3 = '{0} `{1}` {2}'.format(lst[0][2], answer_sign, lst[1][2])
    explain4 = '{0} `{1}` {2}'.format(lst[0][1], answer_sign, lst[1][1])


    stem = stem.format(problem1=problem1, problem2=problem2, boxblank=boxblank)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4)

    return stem, answer, comment










































# 5-2-2-09
def fractionmul522_Stem_004():
    stem = "{person}{post1} 길이가 $$수식$${problem1}$$/수식$$인 끈을 $$수식$${problem2}$$/수식$$개 가지고 있습니다. {person}{post2} 가지고 있는 끈은 모두 몇 $$수식$$rm m`$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${answer_num}rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${person}{post2} 가지고 있는 끈의 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${explain1} LEFT ( rm m RIGHT )$$/수식$$\n\n"


    person = random.choice(person_yeo + person_nam)

    post1 = '는' if josa_check(person[-1]) == ' ' else '이는'
    post2 = '가' if josa_check(person[-1]) == ' ' else '이가'

    while 1:
        a1, a4 = random.sample(range(2, 10), 2)
        a2 = 1
        a3 = 1
        a5 = a1 + 1
        a6, a7 = reduce(a5 * a4, a1)
        if a7 != 1:
            break

    a8 = a6 // a7
    a9 = a6 % a7

    problem1 = '{0} {{ {1} }} over {{ {2} }}'.format(a3, a2, a1)
    problem2 = a4
    answer_num = '{0} {{ {1} }} over {{ {2} }}'.format(a8, a9, a7)

    explain1 = '=` {0} `TIMES` {1} `=` {{ {2} }} over {{ {3} }} `TIMES` {4} `=` {{ {5} }} over {{ {6} }} `=` {7}' \
        .format(problem1, problem2, a5, a1, a4, a6, a7, answer_num)


    stem = stem.format(problem1=problem1, problem2=problem2, person=person, post1=post1, post2=post2)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, person=person, post2=post2)

    return stem, answer, comment








































# 5-2-2-10
def fractionmul522_Stem_005():
    stem = "하루에 $$수식$${problem1}$$/수식$$분씩 일정하게 빨라지는 시계가 있습니다. 이 시계를 오늘 오후 $$수식$${problem2}$$/수식$$시에 정확하게 맞추었다면 $$수식$${problem3}$$/수식$$일 후 오후 $$수식$${problem2}$$/수식$$시에 이 시계가 가리키는 시각은 오후 몇 시 몇 분인가요?\n"
    answer = "(정답)\n$$수식$${answer_num1}$$/수식$$시 $$수식$${answer_num2}$$/수식$$분\n"
    comment = "(해설)\n" \
              "하루에 $$수식$${explain1}$$/수식$$분씩 빨라지므로\n" \
              "$$수식$$LEFT ( {explain2}$$/수식$$일 후에 빨라지는 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${explain3} LEFT ($$/수식$$분$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 $$수식$${explain2}$$/수식$$일 후 오후 $$수식$${problem2}$$/수식$$시에 이 시계가 가리키는 시각은\n" \
              "오후 $$수식$${answer_num1}$$/수식$$시 $$수식$${answer_num2}$$/수식$$분입니다.\n\n"


    a1 = random.randint(2, 5)
    a2 = 1
    a3 = random.randint(1, 2)
    n = random.randint(2, 5)
    A = random.randint(1, 11)
    B = a1 * n
    s1 = a3 * a1 + a2
    s2 = a1
    S1 = int(s1 * B / s2)

    problem1 = '{0} {{ {1} }} over {{ {2} }}'.format(a3, a2, a1)
    problem2 = A
    problem3 = B

    explain1 = problem1
    explain2 = B
    explain3 = '=` {0} `TIMES` {1} `=` {{ {2} }} over {{ {3} }} `TIMES` {4} `=` {5}'.format(problem1, B, s1, s2, B, S1)

    answer_num1 = A
    answer_num2 = S1


    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3)
    answer = answer.format(answer_num1=answer_num1, answer_num2=answer_num2)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3,
                             answer_num1=answer_num1, answer_num2=answer_num2, problem2=problem2)

    return stem, answer, comment








































# 5-2-2-11
def fractionmul522_Stem_006():
    stem = "어떤 수에 $$수식$${problem1}$$/수식$${post1} 곱해야 하는데 잘못하여 더했더니 $$수식$${problem2}$$/수식$${post2} 되었습니다. 바르게 계산한 값은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$어떤 수$$수식$$RIGHT ) ` {explain1}$$/수식$$,\n" \
              "$$수식$$LEFT ($$/수식$$어떤 수$$수식$$RIGHT ) ` {explain2}$$/수식$$\n" \
              "따라서 바르게 계산하면\n" \
              "$$수식$${explain3}$$/수식$$입니다.\n\n"


    while 1:
        a1 = random.choice([4, 6, 8])
        a2 = a1 - 1
        A = a1 * 2 + int(a1 / 2)
        a3 = random.randint(A + 2, A + 4)
        s1 = a3 - A
        s2 = a1
        s3 = a2
        s4 = s2
        s5 = s1 * s2 + s3
        s6, s7 = reduce(s4, A)
        s7 = s7 * s5
        if s6 != 1 and s7 < 100:
            break

    s8 = s7 // s6
    s9 = s6
    s10 = s7 % s6

    problem1 = A
    problem2 = '{0} {{ {1} }} over {{ {2} }}'.format(a3, a2, a1)

    post1 = postposition(A, flag=1)
    post2 = postposition(a2, flag=0)

    explain1 = '`+` {0} `=` {1}'.format(problem1, problem2)
    explain2 = '`=` {0} `-` {1} `=` {2} {{ {3} }} over {{ {4} }}'.format(problem2, problem1, s1, s3, s2)
    explain3 = '{0} {{ {1} }} over {{ {2} }} `TIMES` {3} `=` {{ {4} }} over {{ {5} }} `TIMES` {6} `=` {{ {7} }} over ' \
               '{{ {8} }} `=` {9} {{ {10} }} over {{ {11} }}' \
        .format(s1, s3, s2, A, s5, s4, A, s7, s6, s8, s10, s9)

    answer_num = '{0} {{ {1} }} over {{ {2} }}'.format(s8, s10, s9)


    stem = stem.format(problem1=problem1, problem2=problem2, post1=post1, post2=post2)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3)

    return stem, answer, comment







































# 5-2-2-12
def fractionmul522_Stem_007():
    stem = "이번 주에 {person1}{post1} 한 시간에 $$수식$${problem1}``rm {{km}}`$$/수식$$씩 $$수식$${problem2}$$/수식$$시간을 달렸고\n {person2}{post2} 한 시간에 $$수식$${problem3}``rm {{km}}`$$/수식$$씩 $$수식$${problem4}$$/수식$$시간을 달렸습니다. 누가 더 많이 달렸나요?\n"
    answer = "(정답)\n{answer_person}\n"
    comment = "(해설)\n" \
              "{person1} : $$수식$${explain1} LEFT ( rm {{km}} RIGHT )$$/수식$$\n" \
              "{person2} : $$수식$${explain2} LEFT ( rm {{km}} RIGHT )$$/수식$$\n" \
              "$$수식$${explain3}$$/수식$$이므로 {answer_person}{post3} 더 많이 달렸습니다.\n\n"


    person1 = random.choice(['선희', '영수', '현주', '수지', '정호'])
    person2 = random.choice(['원주', '은서', '현우', '진호', '석희'])

    post1 = '는' if josa_check(person1[-1]) == ' ' else '이는'
    post2 = '는' if josa_check(person2[-1]) == ' ' else '이는'

    while 1:
        while 1:
            n = random.randint(1, 9)
            a1 = random.randint(3, 9)
            a2 = random.randint(2, 9)
            if a1 > a2 and n * a2 != a1 and is_gcd(a1, a2):
                break
        a3 = random.randint(5, 9)
        A = a1

        s1 = a3 * a1 + a2
        s2 = a1
        s3 = s1

        b1 = random.randint(3, 4)
        b2 = 1
        b3 = random.randint(a3 - 3, a3 - 1)
        B = b1 * 2
        t1 = b3 * b1 + b2
        t2 = b1
        t3 = t1 * 2
        if s3 != t3:
            break

    if s3 > t3:
        sign = '&gt;'
        answer_person = person1
    else:
        sign = '&lt;'
        answer_person = person2

    problem1 = '{0} {{ {1} }} over {{ {2} }}'.format(a3, a2, a1)
    problem2 = A
    problem3 = '{0} {{ {1} }} over {{ {2} }}'.format(b3, b2, b1)
    problem4 = B

    explain1 = '{0} `TIMES` {1} `=` {{ {2} }} over {{ {3} }} `TIMES` {4} `=` {5}'.format(problem1, A, s1, s2, A, s3)
    explain2 = '{0} `TIMES` {1} `=` {{ {2} }} over {{ {3} }} `TIMES` {4} `=` {5}'.format(problem3, B, t1, t2, B, t3)
    explain3 = '{0} `{1}` {2}'.format(s3, sign, t3)

    post3 = '가' if josa_check(answer_person[-1]) == ' ' else '이가'


    stem = stem.format(problem1=problem1, problem2=problem2, post1=post1, post2=post2, person1=person1, person2=person2,
                       problem3=problem3, problem4=problem4)
    answer = answer.format(answer_person=answer_person)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, answer_person=answer_person,
                             post3=post3, person1=person1, person2=person2)

    return stem, answer, comment








































# 5-2-2-13
def fractionmul522_Stem_008():
    stem = "계산 결과가 가장 작은 것부터 차례대로 기호를 써 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$    ㉡ $$수식$${problem2}$$/수식$$    ㉢ $$수식$${problem3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{answer_sign}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${explain1}$$/수식$$\n" \
              "㉡ $$수식$${explain2}$$/수식$$\n" \
              "㉢ $$수식$${explain3}$$/수식$$\n" \
              "따라서 $$수식$${explain4}$$/수식$$이므로 계산 결과가 가장 작은 것부터 기호를 쓰면 {answer_sign}입니다.\n\n"


    while 1:
        a1 = random.randint(2, 5)
        a2 = a1 - 1
        a3 = 1
        A = random.randint(2, 5)
        if is_gcd(a2, a1) and is_gcd(a1, A):
            break

    s1 = a3 * a1 + a2
    s2 = a1
    s3 = A * s1
    s4 = a1
    s5 = s3 // s4
    s6 = s3 - s4 * s5
    s7 = a1

    a_result = (s5 * s7 + s6) / s7
    prob1 = '{0} `TIMES` {1} {{ {2} }} over {{ {3} }}'.format(A, a3, a2, a1)
    equ1 = '{0} `=` {1} `TIMES` {{ {2} }} over {{ {3} }} `=` {{ {4} }} over {{ {5} }} `=` ' \
           '{6} {{ {7} }} over {{ {8} }}'.format(prob1, A, s1, s2, s3, s4, s5, s6, s7)

    while 1:
        b1 = random.randint(2, 4)
        if a1 != b1:
            break
    b2 = 1
    b3 = 2
    B = b1 * random.choice([2, 3])
    t1 = b3 * b1 + b2
    t2 = b1
    t3 = B * t1 // t2
    b_result = t3

    prob2 = '{0} `TIMES` {1} {{ {2} }} over {{ {3} }}'.format(B, b3, b2, b1)
    equ2 = '{0} `=` {1} `TIMES` {{ {2} }} over {{ {3} }} `=` {4}'.format(prob2, B, t1, t2, t3)

    while 1:
        while 1:
            c1 = random.randint(2, 5)
            if a1 != c1 and b1 != c1:
                break
        c2 = 1
        c3 = 1
        C = c1 * 2
        u1 = c3 * c1 + c2
        u2 = c1
        u3 = C * u1 // u2
        c_result = u3
        if b_result != c_result:
            break

    prob3 = '{0} `TIMES` {1} {{ {2} }} over {{ {3} }}'.format(C, c3, c2, c1)
    equ3 = '{0} `=` {1} `TIMES` {{ {2} }} over {{ {3} }} `=` {4}'.format(prob3, C, u1, u2, u3)

    lst = [[prob1, equ1, a_result, '{0} {{ {1} }} over {{ {2} }}'.format(s5, s6, s7)],
           [prob2, equ2, b_result, '{0}'.format(t3)],
           [prob3, equ3, c_result, '{0}'.format(u3)]]

    # random.shuffle(lst)
    problem1, problem2, problem3 = lst[0][0], lst[1][0], lst[2][0]
    explain1, explain2, explain3 = lst[0][1], lst[1][1], lst[2][1]

    lst[0].append('㉠')
    lst[1].append('㉡')
    lst[2].append('㉢')

    lst.sort(key=lambda x: x[2])

    explain4 = '{0} `&lt;` {1} `&lt;` {2}'.format(lst[0][3], lst[1][3], lst[2][3])
    answer_sign = '{0}, {1}, {2}'.format(lst[0][4], lst[1][4], lst[2][4])


    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3,
                             explain4=explain4, answer_sign=answer_sign)

    return stem, answer, comment









































# 5-2-2-15
def fractionmul522_Stem_009():
    stem = "계산 결과가 가장 큰 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$    ㉡ $$수식$${problem2}$$/수식$$    ㉢ $$수식$${problem3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{answer_sign}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${explain1}$$/수식$$\n" \
              "㉡ $$수식$${explain2}$$/수식$$\n" \
              "㉢ $$수식$${explain3}$$/수식$$\n" \
              "$$수식$${explain4}$$/수식$$이므로 계산 결과가 가장 큰 것은 {answer_sign}입니다.\n\n"


    while 1:
        a1 = random.randint(4, 9)
        a2 = random.randint(2, 8)
        if is_gcd(a2, a1) and a2 < a1:
            A = random.randint(11, 19)
            s1, s2 = reduce(A, a1)
            s3 = s1 * a2
            if s3 < 100 and s2 != 1:
                break

    s4 = s2
    s5 = s3 // s4
    s6 = s3 % s4
    s7 = s2
    a_result = s3 / s4

    prob1 = '{0} `TIMES` {{ {1} }} over {{ {2} }}'.format(A, a2, a1)
    equ1 = '{0} `=` {{ {1} `TIMES` {2} }} over {{ {3} }} `=` {{ {4} }} over {{ {5} }} `=` ' \
           '{6} {{ {7} }} over {{ {8} }}'.format(prob1, s1, a2, s2, s3, s4, s5, s6, s7)

    while 1:
        b1 = random.randint(2, 9)
        b2 = 1
        B = random.randint(21, 39)
        t2, t1 = reduce(B, b1)
        if t1 == 1:
            continue
        t3 = t2 // t1
        t4 = t2 % t1
        t5 = t1
        b_result = t2 / t1
        if a_result != b_result:
            break

    prob2 = '{0} `TIMES` {{ {1} }} over {{ {2} }}'.format(B, b2, b1)
    equ2 = '{0} `=` {{ {1} }} over {{ {2} }} `=` {3} {{ {4} }} over {{ {5} }}'.format(prob2, t2, t1, t3, t4, t5)

    while 1:
        C = random.choice([15, 25, 35, 45])
        c1 = 10
        c2 = random.choice([3, 7, 9])
        u1, u2 = reduce(C, c1)
        if u2 == 1:
            continue
        u3 = u1 * c2
        u4 = u2
        u5 = u3 // u4
        u6 = u3 % u4
        u7 = u2
        c_result = u3 / u4
        if a_result != c_result and b_result != c_result:
            break

    prob3 = '{0} `TIMES` {{ {1} }} over {{ {2} }}'.format(C, c2, c1)
    equ3 = '{0} `=` {{ {1} `TIMES` {2} }} over {{ {3} }} `=` {{ {4} }} over {{ {5} }} `=` {6} {{ {7} }} over {{ {8} }}' \
        .format(prob3, u1, c2, u2, u3, u4, u5, u6, u7)

    lst = [[prob1, equ1, a_result, '{0} {{ {1} }} over {{ {2} }}'.format(s5, s6, s7)],
           [prob2, equ2, b_result, '{0} {{ {1} }} over {{ {2} }}'.format(t3, t4, t5)],
           [prob3, equ3, c_result, '{0} {{ {1} }} over {{ {2} }}'.format(u5, u6, u7)]]

    random.shuffle(lst)
    problem1, problem2, problem3 = lst[0][0], lst[1][0], lst[2][0]
    explain1, explain2, explain3 = lst[0][1], lst[1][1], lst[2][1]

    lst[0].append('㉠')
    lst[1].append('㉡')
    lst[2].append('㉢')

    lst.sort(reverse=True, key=lambda x: x[2])

    explain4 = '{0} `&gt;` {1} `&gt;` {2}'.format(lst[0][3], lst[1][3], lst[2][3])
    answer_sign = '{0}'.format(lst[0][4])


    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3,
                             explain4=explain4, answer_sign=answer_sign)

    return stem, answer, comment








































# 5-2-2-18
def fractionmul522_Stem_010():
    stem = "다음이 나타내는 수는 얼마인가요?\n$$표$$$$수식$${problem1}$$/수식$$의 $$수식$${problem2}$$/수식$$배인 수$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$의 $$수식$${explain2}$$/수식$$배인 수는\n" \
              "$$수식$${explain3}$$/수식$$입니다.\n\n"


    while 1:
        A = random.randint(10, 19)
        a3 = random.randint(1, 5)
        a1 = random.randint(1, 9)
        a2 = random.randint(1, 9)
        s1 = a3 * a1 + a2
        s2 = a1
        s3, s5 = reduce(A, s2)
        s4 = s1
        s6 = s3 * s4
        if is_gcd(a1, a2) and a2 < a1 and s5 != 1 and s6 < 100:
            break

    s7 = s5
    s8 = s6 // s7
    s9 = s6 % s7
    s10 = s5

    problem1 = A
    problem2 = '{0} {{ {1} }} over {{ {2} }}'.format(a3, a2, a1)

    explain1, explain2 = problem1, problem2
    explain3 = '{0} `TIMES` {1} `=` {2} `TIMES` {{ {3} }} over {{ {4} }} `=` {{ {5} `TIMES` {6} }} over {{ {7} }} `=` ' \
               '{{ {8} }} over {{ {9} }} `=` {10} {{ {11} }} over {{ {12} }}' \
        .format(problem1, problem2, A, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10)

    answer_num = '{0} {{ {1} }} over {{ {2} }}'.format(s8, s9, s10)


    stem = stem.format(problem1=problem1, problem2=problem2)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3)

    return stem, answer, comment












































# 5-2-2-19
def fractionmul522_Stem_011():
    stem = "변이 $$수식$${problem1}$$/수식$$개인 정다각형이 있습니다. 이 정다각형의 한 변이 $$수식$${problem2} ``rm {{cm}}`$$/수식$$일 때, 둘레는 몇 $$수식$$rm {{cm}}`$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${answer_num} ``rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$정다각형의 둘레$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${explain1}$$/수식$$\n" \
              "$$수식$${explain2} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n\n"


    while 1:
        A = random.randint(3, 9)
        a3 = random.randint(1, 5)
        a1 = random.randint(11, 19)
        a2 = random.randint(2, 9)
        s1 = a3 * a1 + a2
        s2 = a1
        s3, s5 = reduce(A, s2)
        s4 = s1
        s6 = s3 * s4
        if is_gcd(a1, a2) and a2 < a1 and s5 != 1 and s6 < 100:
            break

    s7 = s5
    s8 = s6 // s7
    s9 = s6 % s7
    s10 = s5

    problem1 = A
    problem2 = '{0} {{ {1} }} over {{ {2} }}'.format(a3, a2, a1)

    explain1 = '=` {0} `TIMES` {1} `=` {2} `TIMES` {{ {3} }} over {{ {4} }} `=` {{ {5} `TIMES` {6} }} over {{ {7} }} ' \
               '`=` {{ {8} }} over {{ {9} }}'.format(problem1, problem2, A, s1, s2, s3, s4, s5, s6, s7)
    explain2 = '=` {0} {{ {1} }} over {{ {2} }}'.format(s8, s9, s10)
    answer_num = '{0} {{ {1} }} over {{ {2} }}'.format(s8, s9, s10)


    stem = stem.format(problem1=problem1, problem2=problem2)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2)

    return stem, answer, comment










































# 5-2-2-20
def fractionmul522_Stem_012():
    stem = "계산 결과가 $$수식$${problem1}$$/수식$$보다 큰 식을 모두 골라 보세요.\n① $$수식$${problem2}$$/수식$$\n② $$수식$${problem3}$$/수식$$\n③ $$수식$${problem4}$$/수식$$\n④ $$수식$${problem5}$$/수식$$\n⑤ $$수식$${problem6}$$/수식$$\n"
    answer = "(정답)\n{answer_num1}, {answer_num2}\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$에 진분수를 곱하면 곱한 결과가 $$수식$${explain1}$$/수식$$보다 작아지고.\n"\
              "$$수식$${explain1}$$/수식$$에 대분수를 곱하면 곱한 결과가 $$수식$${explain1}$$/수식$$보다 커집니다.\n" \
              "{answer_num1} $$수식$${explain2}$$/수식$$\n" \
              "{answer_num2} $$수식$${explain3}$$/수식$$\n\n"\


    A = random.randint(4, 9)
    a1 = random.randint(2, A - 1)
    a2 = a1 - 1
    b1 = random.randint(2, A - 1)
    b2 = 1
    c1 = 1

    while 1:
        d1 = random.randint(2, 9)
        d2 = 1
        d3 = random.randint(1, 5)
        s1 = d3 * d1 + 1
        s2 = d1
        s3, s4 = reduce(A * s1, s2)
        if s4 != 1 and s3 < 100:
            break

    s5 = s3 // s4
    s6 = s3 % s4
    s7 = s4

    while 1:
        e3 = random.randint(1, 5)
        e1 = random.randint(3, A - 1)
        e2 = random.randint(2, e1 - 1)
        t1 = e3 * e1 + e2
        t2 = e1
        t3, t4 = reduce(A * t1, t2)
        if is_gcd(e1, e2) and t4 != 1 and t3 < 100:
            break

    t5 = t3 // t4
    t6 = t3 % t4
    t7 = t4

    problem1 = A
    prob1 = '{0} `TIMES` {{ {1} }} over {{ {2} }}'.format(A, a2, a1)
    prob2 = '{0} `TIMES` {{ {1} }} over {{ {2} }}'.format(A, b2, b1)
    prob3 = '{0} `TIMES` {1}'.format(A, c1)
    prob4 = '{0} `TIMES` {1} {{ {2} }} over {{ {3} }}'.format(A, d3, d2, d1)
    prob5 = '{0} `TIMES` {1} {{ {2} }} over {{ {3} }}'.format(A, e3, e2, e1)

    exp1 = '{0} `=` {1} `TIMES` {{ {2} }} over {{ {3} }} `=` {{ {4} }} over {{ {5} }} `=` ' \
           '{6} {{ {7} }} over {{ {8} }} `&gt;` {9}'.format(prob4, A, s1, s2, s3, s4, s5, s6, s7, A)
    exp2 = '{0} `=` {1} `TIMES` {{ {2} }} over {{ {3} }} `=` {{ {4} }} over {{ {5} }} `=` ' \
           '{6} {{ {7} }} over {{ {8} }} `&gt;` {9}'.format(prob5, A, t1, t2, t3, t4, t5, t6, t7, A)

    sign_lst = ['①', '②', '③', '④', '⑤']
    lst = [[prob1, 1], [prob2, 1], [prob3, 1], [prob4, exp1], [prob5, exp2]]
    random.shuffle(lst)
    problem2, problem3, problem4, problem5, problem6 = lst[0][0], lst[1][0], lst[2][0], lst[3][0], lst[4][0]
    flag = 0

    for idx, value in enumerate(lst):
        if value[1] != 1:
            if flag == 0:
                explain2 = value[1]
                answer_num1 = sign_lst[idx]
                flag = 1
            else:
                explain3 = value[1]
                answer_num2 = sign_lst[idx]

    explain1 = A


    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, problem4=problem4,
                       problem5=problem5, problem6=problem6)
    answer = answer.format(answer_num1=answer_num1, answer_num2=answer_num2)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3,
                             answer_num1=answer_num1, answer_num2=answer_num2)

    return stem, answer, comment










































# 5-2-2-22
def fractionmul522_Stem_013():
    stem = "{person}{post1} 세로가 $$수식$${problem1}``rm {{cm}}`$$/수식$$인 {obj}{post2} 만들었습니다. {obj}의 가로는 세로의 $$수식$${problem2}$$/수식$${ra1} {person}{post3} 만든 {obj}의 가로는 몇 $$수식$$rm {{cm}}`$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${answer_num} ``rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${obj}의 가로$$수식$$RIGHT ) {explain1} ` LEFT ( rm {{cm}} RIGHT )$$/수식$$\n\n"


    person = random.choice(['선희', '영수', '진우', '지수', '수지'])
    obj = random.choice(['방패연', '액자', '책상', '덮개'])

    post1 = '는' if josa_check(person[-1]) == ' ' else '이는'
    post2 = '를' if josa_check(obj[-1]) == ' ' else '을'
    post3 = '가' if josa_check(person[-1]) == ' ' else '이가'

    while 1:
        A = random.choice([30, 40, 50, 60])
        a1 = random.randint(3, 9)
        a2 = a1 - 1
        if A % a1 == 0:
            break

    s1 = A // a1
    s2 = a2
    s3 = s1 * s2

    problem1 = A
    problem2 = '{{ {0} }} over {{ {1} }}'.format(a2, a1)
    explain1 = '`=` {0} `TIMES` {{ {1} }} over {{ {2} }} `=` {3} `TIMES` {4} `=` {5}'.format(A, a2, a1, s1, s2, s3)
    answer_num = '{0}'.format(s3)

    ra1 = get_josa(a2, "라면")


    stem = stem.format(problem1=problem1, problem2=problem2, person=person, post1=post1, post2=post2, post3=post3,
                       obj=obj, ra1=ra1)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, obj=obj)

    return stem, answer, comment










































# 5-2-2-23
def fractionmul522_Stem_014():
    stem = "{person}{post1} 일정한 빠르기로 한 시간에 $$수식$${problem1}``rm {{km}}`$$/수식$$를 걷습니다. 같은 빠르기로 {person}{post2} $$수식$${problem2}$$/수식$$시간 $$수식$${problem3}$$/수식$$분 동안 걸은 거리는 몇 $$수식$$rm {{km}}`$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${answer_num} ``rm {{km}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$시간 $$수식$${explain2}$$/수식$$분" \
              "$$수식$$`=` {explain3}$$/수식$$시간$$수식$$`=` {explain4}$$/수식$$시간\n" \
              "따라서 {person}{post2} $$수식$${explain5}$$/수식$$시간 $$수식$${explain6}$$/수식$$분 동안 걸은 거리는\n" \
              "$$수식$${explain7} LEFT ( rm {{km}} RIGHT )$$/수식$$입니다.\n\n"


    person = random.choice(['우희', '선우', '수희', '영지', '선호'])
    post1 = '는' if josa_check(person[-1]) == ' ' else '이는'
    post2 = '가' if josa_check(person[-1]) == ' ' else '이가'


    while 1:
        A = random.randint(2, 4)
        B = random.randint(1, 2)
        C = random.choice([10, 15, 20, 30, 40, 45, 50])
        s1 = B
        s2 = C
        s3 = 60
        s4 = B
        s5, s6 = reduce(s2, s3)
        s7 = s4 * s6 + s5
        s8 = s6
        s9, s10 = reduce(s7 * A, s8)
        if s9 < 100 and s6 != 1 and s10 != 1:
            break

    s11 = s9 // s10
    s12 = s9 % s10
    s13 = s10

    problem1 = A
    problem2 = B
    problem3 = C

    explain1, explain2 = B, C
    explain3 = '{0} {{ {1} }} over {{ {2} }}'.format(s1, s2, s3)
    explain4 = '{0} {{ {1} }} over {{ {2} }}'.format(s4, s5, s6)
    explain5, explain6 = B, C
    explain7 = '{0} `TIMES` {1} `=` {2} `TIMES` {{ {3} }} over {{ {4} }} `=` {{ {5} }} over {{ {6} }} `=` ' \
               '{7} {{ {8} }} over {{ {9} }}'.format(A, explain4, A, s7, s8, s9, s10, s11, s12, s13)
    answer_num = '{0} {{ {1} }} over {{ {2} }}'.format(s11, s12, s13)


    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, person=person, post1=post1, post2=post2)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             explain5=explain5, explain6=explain6, explain7=explain7, person=person, post2=post2)

    return stem, answer, comment










































# 5-2-2-24
def fractionmul522_Stem_015():
    stem = "어느 {obj1}의 평일 {obj2} 관람료는 $$수식$${problem1}$$/수식$$원입니다. 주말에는 평일 {obj2} 관람료의 $$수식$${problem2}$$/수식$$만큼 내야 한다고 합니다.\n주말에 $$수식$${problem3}$$/수식$$명이 {obj2}{post} 보기 위해 내야 하는 금액은 모두 얼마인가요?\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$원\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$주말 관람료$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${explain1} LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$주말에 $$수식$${explain2}$$/수식$$명이 {obj2}{post} 보기 위해 " \
              "내야 하는 금액$$수식$$RIGHT )$$/수식$$\n$$수식$$ {explain3} LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$\n\n"


    obj1, obj2 = random.choice([['영화관', '영화'], ['공연장', '연극'], ['전시장', '전시']])
    post = '를' if josa_check(obj2[-1]) == ' ' else '을'

    while 1:
        A = random.choice([6000, 7000, 8000, 9000])
        B = random.randint(2, 5)
        a1 = A // 1000
        a2 = random.randint(1, 8)
        if is_gcd(a1, a2) and a2 < a1:
            break

    a3 = 1
    s1 = a3 * a1 + a2
    s2 = a1
    S1 = (A * s1) // s2
    S2 = S1 * B

    problem1 = A
    problem2 = '{0} {{ {1} }} over {{ {2} }}'.format(a3, a2, a1)
    problem3 = B

    explain1 = '=` {0} `TIMES` {1} `=` {2} `TIMES` {{ {3} }} over {{ {4} }} `=` {5}'.format(A, problem2, A, s1, s2, S1)
    explain2 = B
    explain3 = '`=` {0} `TIMES` {1} `=` {2}'.format(S1, B, S2)

    answer_num = S2


    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, obj1=obj1, obj2=obj2, post=post)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, obj2=obj2, post=post)

    return stem, answer, comment








































# 5-2-2-25
def fractionmul522_Stem_016():
    stem = "가 ★ 나$$수식$$`=`$$/수식$$가$$수식$$`TIMES`$$/수식$$나$$수식$$`+` {problem1}$$/수식$${post} 약속할 때, 다음은 얼마인가요?\n$$표$$$$수식$${problem2}$$/수식$$ ★ $$수식$${problem3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$ ★ $$수식$${explain2}$$/수식$$\n\n"


    while 1:
        n = random.randint(2, 5)
        A = random.randint(11, 19)
        B = random.randint(2, 4)
        a1 = B * n
        a2 = random.randint(1, 8)
        a3 = random.randint(1, 2)
        s1 = a3 * a1 + a2
        s2 = a1
        s3, s4 = reduce(B * s1, s2)
        if is_gcd(a1, a2) and a2 < a1 and s3 < 100 and s4 != 1:
            break

    s5 = (s3 // s4) + A
    s6 = s3 % s4
    s7 = s4

    post = postposition(int(str(A)[-1]), flag=4)
    problem1 = A
    problem2 = B
    problem3 = '{0} {{ {1} }} over {{ {2} }}'.format(a3, a2, a1)

    explain1 = B
    explain2 = '{0} `=` {1} `TIMES` {{ {2} }} over {{ {3} }} `+` {4} `=` {{ {5} }} over {{ {6} }} `+` {7} `=` ' \
               '{8} {{ {9} }} over {{ {10} }}'.format(problem3, B, s1, s2, A, s3, s4, A, s5, s6, s7)
    answer_num = '{0} {{ {1} }} over {{ {2} }}'.format(s5, s6, s7)


    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, post=post)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2)

    return stem, answer, comment













































# 5-2-2-28
def fractionmul522_Stem_017():
    stem = "계산 결과를 비교하여 $$수식$${box}$$/수식$$ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${frac_1} ` TIMES ` {frac_2} ~~{box}~~ {frac_3} ` TIMES ` {frac_4}$$/수식$$\n"
    answer = "(정답)\n$$수식$${T}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${frac_1} ` TIMES ` {frac_2} `=` {frac_5}$$/수식$$, $$수식$${frac_3} ` TIMES ` {frac_4} `=` {frac_6}$$/수식$$\n" \
              "단위분수는 분모가 작을수록 더 큰 수입니다.\n" \
              "$$수식$${frac_5} `{T}` {frac_6}$$/수식$$ 이므로 $$수식$${frac_1} ` TIMES ` {frac_2} `{T}` {frac_3} ` TIMES ` {frac_4}$$/수식$$ 입니다.\n\n"


    flag = True
    while flag:
        a1, a2, b1, b2 = np.random.choice(range(2, 9 + 1), 4, replace=False)
        s1 = a1 * a2
        s2 = b1 * b2

        # 분자의 범위(곱셈 결과)가 100이 넘지 않고, 분모들의 차가 50이 넘지 않도록 조건 부여
        if s1 < 100 and s2 < 100 and abs(s1 - s2) < 50:
            flag = False

            frac_1 = "{1} over {%s}" % a1
            frac_2 = "{1} over {%s}" % a2
            frac_3 = "{1} over {%s}" % b1
            frac_4 = "{1} over {%s}" % b2
            frac_5 = "{1} over {%s}" % s1
            frac_6 = "{1} over {%s}" % s2

            if s1 > s2:
                T = "&lt;"
            elif s1 == s2:
                T = "="
            else:
                T = "&gt;"


    stem = stem.format(box=box, frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4)
    answer = answer.format(T=T)
    comment = comment.format(T=T, frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4, frac_5=frac_5,
                             frac_6=frac_6)

    return stem, answer, comment













































# 5-2-2-29
def fractionmul522_Stem_018():
    stem = "계산 결과가 $$수식$${frac_1}$$/수식$$보다 큰 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${exp_1}$$/수식$$    ㉡ $$수식$${exp_2}$$/수식$$\n \n㉢ $$수식$${exp_3}$$/수식$$    ㉣ $$수식$${exp_4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{S}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${exp_1} `=` {ans_1}$$/수식$$\n" \
              "㉡ $$수식$${exp_2} `=` {ans_2}$$/수식$$\n" \
              "㉢ $$수식$${exp_3} `=` {ans_3}$$/수식$$\n" \
              "㉣ $$수식$${exp_4} `=` {ans_4}$$/수식$$\n" \
              "따라서 계산 결과가 $$수식$${frac_1}$$/수식$$보다 큰 것 {S}입니다.\n\n"


    flag = True
    while flag:
        a1 = random.randint(11, 19)
        a2 = random.randint(2, 9)
        b1 = a2 * random.randint(2, 5)

        # b1의 약수가 아닌 수 찾기
        b1_non_divisors = [b for b in range(2, b1) if b1 % b != 0 and b < 10]
        b2 = random.choice(b1_non_divisors)

        if a1 > a2 and get_gcd(a1, a2) == 1 and get_gcd(b1, b2) == 1:
            t1 = a2 * b2
            t2 = a1 * b1
            G1 = get_gcd(t1, t2)
            s1 = t1 // G1
            s2 = t2 // G1

            c1 = a2 * 2
            c2 = c1 - 1

            t3 = c2 * a2
            t4 = c1 * a1
            G2 = get_gcd(t3, t4)
            s3 = t3 // G2
            s4 = t4 // G2

            d1 = random.randint(1, 9)
            d1_multiples = [d1 * n for n in range(1, 10)]

            if a1 not in d1_multiples:
                t5 = a2 * d1
                t6 = a1
                G3 = get_gcd(t5, t6)
                t7 = t5 // G3
                t8 = t6 // G3
                s5 = t7 // t8
                s6 = t5 - (t6 * s5)
                s7 = t8

                e1 = a2
                e2 = e1 - 1

                t9 = a2 * e2
                t10 = a1 * e1
                G4 = get_gcd(t9, t10)
                s8 = t9 // G4
                s9 = t10 // G4

                # 분모 분자 조건 확인
                if 0 not in [s5, s1, s2, s3, s4, s6, s7, s8, s9] and 1 not in [s2, s4, s7, s9]:
                    # 계산 결과의 분모가 100이 넘지 않도록 조정
                    if s2 < 100 and s4 < 100 and s7 < 100 and s9 < 100:
                        flag = False

    frac_1 = "{%s} over {%s}" % (a2, a1)
    exp_1 = "{%s} over {%s} `TIMES` {%s} over {%s}" % (a2, a1, b2, b1)
    exp_2 = "{%s} over {%s} `TIMES` {%s} over {%s}" % (c2, c1, a2, a1)
    exp_3 = "{%s} over {%s} `TIMES` {%s}" % (a2, a1, d1)
    exp_4 = "{%s} over {%s} `TIMES` {%s} over {%s}" % (a2, a1, e2, e1)
    ans_1 = "{%s} over {%s}" % (s1, s2)
    ans_2 = "{%s} over {%s}" % (s3, s4)
    ans_3 = "%s {%s} over {%s}" % (s5, s6, s7)
    ans_4 = "{%s} over {%s}" % (s8, s9)

    # 보기, 해설 쌍을 사전으로 만들어서 랜덤하게 섞음
    q_dict = {exp_1: ans_1, exp_2: ans_2, exp_3: ans_3, exp_4: ans_4}
    exp_list = random.sample(list(q_dict.keys()), 4)

    ans_list = []
    for i, exp in enumerate(exp_list):
        ans = q_dict[exp]
        ans_list.append(ans)
        if ans[0] != "{":
            S = multiple_choice_hangul[i]

    ans_1, ans_2, ans_3, ans_4 = ans_list
    exp_1, exp_2, exp_3, exp_4 = exp_list


    stem = stem.format(frac_1=frac_1, exp_1=exp_1, exp_2=exp_2, exp_3=exp_3, exp_4=exp_4)
    answer = answer.format(S=S)
    comment = comment.format(frac_1=frac_1, exp_1=exp_1, exp_2=exp_2, exp_3=exp_3, exp_4=exp_4,
                             ans_1=ans_1, ans_2=ans_2, ans_3=ans_3, ans_4=ans_4, S=S)

    return stem, answer, comment












































# 5-2-2-30
def fractionmul522_Stem_019():
    stem = "크기 비교를 바르게 한 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${exp_1}$$/수식$$\n \n㉡ $$수식$${exp_2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{S1}\n"
    comment = "(해설)\n" \
              "{S2} $$수식$${frac_1} `TIMES` {frac_left} `=` {frac_3}$$/수식$$, " \
              "$$수식$${frac_1} `TIMES` {frac_right} `=` {frac_5}$$/수식$$에서\n" \
              "$$수식$${frac_3} ` {compare_result} ` {frac_5}$$/수식$$ 이므로 " \
              "$$수식$${frac_1} `TIMES` {frac_left} ` {compare_result} ` {frac_1} `TIMES` {frac_right}$$/수식$$입니다.\n\n"


    flag = True
    while flag:
        a1 = random.randint(11, 19)
        a2 = random.randint(1, 9)

        if get_gcd(a1, a2) == 1:
            b1 = random.randint(2, 8)
            c1 = b1 + 1
            t1 = a2 * 1
            t2 = a1 * b1
            G1 = get_gcd(t1, t2)
            s1 = t1
            s2 = t2
            t3 = a1 * c1
            G2 = get_gcd(t1, t3)
            s3 = t1
            s4 = t3
            d1 = random.randint(3, 9)
            d2 = d1 - 1
            e1 = d2
            e2 = random.randint(1, e1 - 1)


            if get_gcd(e1, e2) == 1:

                show_choice = np.random.randint(0, 2)

                if show_choice == 0:
                    frac_1 = "{%s} over {%s}" % (a2, a1)
                    frac_2 = "{%s} over {%s}" % (1, b1)
                    frac_3 = "{%s} over {%s}" % (s1, s2)
                    frac_4 = "{%s} over {%s}" % (1, c1)
                    frac_5 = "{%s} over {%s}" % (s3, s4)

                    exp_1 = "%s `TIMES` %s `&lt;` %s `TIMES` %s" % (frac_1, frac_2, frac_1, frac_4)
                    exp_2 = "{%s} over {%s} `TIMES` {%s} over {%s} `=` {%s} over {%s} `TIMES` {%s} over {%s}" % (d2, d1, e2, e1, e2, e1, d2, d1)

                    tmp_list = [(exp_1, exp_2, '㉡', '㉠'), (exp_2, exp_1, '㉠', '㉡')]

                    exp_1, exp_2, S1, S2 = random.choice(tmp_list)

                    compare_result = "&gt;"

                    frac_left = frac_2
                    frac_right = frac_4

                    flag = False

                else:
                    frac_1 = "{%s} over {%s}" % (a2, a1)
                    frac_2 = "{%s} over {%s}" % (1, b1)
                    frac_3 = "{%s} over {%s}" % (s1, s4)
                    frac_4 = "{%s} over {%s}" % (1, c1)
                    frac_5 = "{%s} over {%s}" % (s3, s2)

                    exp_1 = "%s `TIMES` %s `&gt;` %s `TIMES` %s" % (frac_1, frac_4, frac_1, frac_2)
                    exp_2 = "{%s} over {%s} `TIMES` {%s} over {%s} `=` {%s} over {%s} `TIMES` {%s} over {%s}" % (
                    d2, d1, e2, e1, e2, e1, d2, d1)

                    tmp_list = [(exp_1, exp_2, '㉡', '㉠'), (exp_2, exp_1, '㉠', '㉡')]

                    exp_1, exp_2, S1, S2 = random.choice(tmp_list)

                    compare_result = "&lt;"

                    frac_left = frac_4
                    frac_right = frac_2

                    flag = False


    stem = stem.format(exp_1=exp_1, exp_2=exp_2)
    answer = answer.format(S1=S1)
    comment = comment.format(S2=S2, frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4, frac_5=frac_5, compare_result=compare_result, frac_left=frac_left, frac_right=frac_right)

    return stem, answer, comment












































# 5-2-2-32
def fractionmul522_Stem_020():
    stem = "{N1}{N1_josa} 선물을 포장하는데 {N2} $$수식$${frac_1} `rm m$$/수식$$의 $$수식$${frac_2}$$/수식$${b2_josa} 사용했습니다. 사용한 {N2}{N2_josa} 몇 $$수식$$rm m$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${frac_3} `rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$사용한 {N2}의 길이$$수식$$RIGHT ) ` = ` {frac_1} `TIMES` {frac_2} `=` {frac_3} LEFT ( rm m RIGHT )$$/수식$$\n\n"


    STEM_20_DICT = ['리본', '끈']

    flag = True
    while flag:
        N1 = random.choice(person_nam + person_yeo)
        N1_josa = "는" if josa_check(N1[-1]) == ' ' else "이는"

        N2 = random.choice(STEM_20_DICT)
        N2_josa = "는" if josa_check(N2[-1]) == ' ' else "은"

        a1 = random.randint(3, 8)
        a2 = a1 - 1
        b1 = a2
        b2 = b1 - 1
        s1 = b2
        s2 = a1

        b2_josa = num_josa(b2)[2]

        frac_1 = "{%s} over {%s}" % (a2, a1)
        frac_2 = "{%s} over {%s}" % (b2, b1)
        frac_3 = "{%s} over {%s}" % (s1, s2)

        # 분모 조건 확인
        if 0 not in [a2, b2] and get_gcd(s1, s2) == 1:
            flag = False


    stem = stem.format(N1=N1, N1_josa=N1_josa, N2=N2, N2_josa=N2_josa, frac_1=frac_1, frac_2=frac_2, b2_josa=b2_josa)
    answer = answer.format(frac_3=frac_3)
    comment = comment.format(N2=N2, frac_1=frac_1, frac_2=frac_2, frac_3=frac_3)

    return stem, answer, comment















































# 5-2-2-33
def fractionmul522_Stem_021():
    stem = "다음 수 중에서 가장 큰 수와 두 번째로 큰 수의 곱을 구해 보세요.\n$$표$$$$수식$${frac_1}$$/수식$$    $$수식$${frac_2}$$/수식$$    $$수식$${frac_3}$$/수식$$    $$수식$${frac_4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${frac_5}$$/수식$$\n"
    comment = "(해설)\n" \
              "가장 큰 수는 $$수식$${max_1}$$/수식$$이고, 두 번째 큰 수는 $$수식$${max_2}$$/수식$$입니다.\n" \
              "따라서 두 수의 곱을 구해 보면 $$수식$${max_1} `TIMES` {max_2} `=` {frac_5}$$/수식$$입니다.\n\n"


    flag = True
    
    while flag:
        a1, b1, c1, d1 = sorted(random.sample(range(2, 9), 4), reverse=True)
        a2 = a1 - 1
        b2 = b1 - 1
        c2 = c1 - 1
        d2 = d1 - 1

        t1 = a1 * b1
        t2 = a2 * b2
        G = get_gcd(t1, t2)

        if G != 1:
            s1 = t1 // G
            s2 = t2 // G

            frac_1 = "{%s} over {%s}" % (a2, a1)
            frac_2 = "{%s} over {%s}" % (b2, b1)
            frac_3 = "{%s} over {%s}" % (c2, c1)
            frac_4 = "{%s} over {%s}" % (d2, d1)
            frac_5 = "{%s} over {%s}" % (s2, s1)

            max_1 = "{%s} over {%s}" % (a2, a1)
            max_2 = "{%s} over {%s}" % (b2, b1)

            # 보기 랜덤 배치를 위해 섞었음
            frac_1, frac_2, frac_3, frac_4 = random.sample([frac_1, frac_2, frac_3, frac_4], 4)

            flag = False


    stem = stem.format(frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4)
    answer = answer.format(frac_5=frac_5)
    comment = comment.format(frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4, frac_5=frac_5, max_1=max_1,
                             max_2=max_2)

    return stem, answer, comment











































# 5-2-2-34
def fractionmul522_Stem_022():
    stem = "계산 결과가 $$수식$${frac_1}$$/수식$$보다 작은 것을 모두 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${exp_1}$$/수식$$    ㉡ $$수식$${exp_2}$$/수식$$\n \n㉢ $$수식$${exp_3}$$/수식$$    ㉣ $$수식$${exp_4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${ans_1}$$/수식$$\n" \
              "㉡ $$수식$${ans_2}$$/수식$$\n" \
              "㉢ $$수식$${ans_3}$$/수식$$\n" \
              "㉣ $$수식$${ans_4}$$/수식$$\n" \
              "따라서 계산 결과가 $$수식$${frac_1}$$/수식$$보다 작은 것은 {ans} 입니다.\n\n"


    flag = True
    
    while flag:
        # 계산 결과가 frac_1보다 작은 것(참) 사전, 큰 것(거짓) 사전, 참에 해당하는 기호 리스트, 해설 리스트
        true_dict, false_dict, answers, comments = {}, {}, [], []

        a1 = 2
        frac_1 = "{%s} over {%s}" % (1, a1)

        # 원본문항 ㉠
        b1 = random.randint(a1 + 1, 8)
        c1 = random.randint(b1 + 1, 9)
        c2 = random.randint(1, c1)

        if get_gcd(c1, c2) == 1:
            t1 = c2
            t2 = b1 * c1
            G1 = get_gcd(t1, t2)
            s1 = t1 // G1
            s2 = t2 // G1
            x1 = s1 / s2
            x2 = 1 / 2
            exp_1 = "{1} over {%s} `TIMES` {%s} over {%s}" % (b1, c2, c1)
            ans_1 = "%s `=` {%s} over {%s} `%s` {1} over {%s}"
            if x1 > x2:
                T1 = "&gt;"
                false_dict[exp_1] = ans_1 % (exp_1, s1, s2, T1, a1)
            elif x1 < x2:
                T1 = "&lt;"
                true_dict[exp_1] = ans_1 % (exp_1, s1, s2, T1, a1)
            else:
                continue

            # 원본문항 ㉡
            d1 = random.randint(a1 + 1, 9)
            s3 = 1
            s4 = d1 * a1
            exp_2 = "{1} over {%s} `TIMES` {1} over {%s}" % (d1, a1)
            ans_2 = "%s `=` {%s} over {%s} `%s` {1} over {%s}"
            if s4 > a1:
                T2 = "&lt;"
                true_dict[exp_2] = ans_2 % (exp_2, s3, s4, T2, a1)
            elif s4 < a1:
                T2 = "&gt;"
                false_dict[exp_2] = ans_2 % (exp_2, s3, s4, T2, a1)
            else:
                continue

            # 원본문항 ㉢
            e1 = random.randint(3, 9)
            e2 = random.randint(2, e1)
            if get_gcd(e1, e2) == 1:
                f1 = e2
                f2 = f1 - 1
                t3 = e2 * f2
                t4 = e1 * f1
                G2 = get_gcd(t3, t4)
                s5 = t3 // G2
                s6 = t4 // G2
                x3 = s5 / s6
                x4 = 1 / 2
                exp_3 = "{%s} over {%s} `TIMES` {%s} over {%s}" % (e2, e1, f2, f1)
                ans_3 = "%s `=` {%s} over {%s} `%s` {1} over {%s}"
                if x3 > x4:
                    T3 = "&gt;"
                    false_dict[exp_3] = ans_3 % (exp_3, s5, s6, T3, a1)
                elif x3 < x4:
                    T3 = "&lt;"
                    true_dict[exp_3] = ans_3 % (exp_3, s5, s6, T3, a1)
                else:
                    continue

                # 원본문항 ㉣
                g1 = random.randint(3, 9)
                g2 = g1 - 1
                h1 = random.randint(11, 19)
                h2 = h1 - 1
                t5 = g2 * h2
                t6 = g1 * h1
                G3 = get_gcd(t5, t6)
                s7 = t5 // G3
                s8 = t6 // G3
                x5 = s7 / s8
                x6 = 1 / 2
                exp_4 = "{%s} over {%s} `TIMES` {%s} over {%s}" % (g2, g1, h2, h1)
                ans_4 = "%s `=` {%s} over {%s} `%s` {1} over {%s}"
                if x5 > x6:
                    T4 = "&gt;"
                    false_dict[exp_4] = ans_4 % (exp_4, s7, s8, T4, a1)
                elif x5 < x6:
                    T4 = "&lt;"
                    true_dict[exp_4] = ans_4 % (exp_4, s7, s8, T4, a1)
                else:
                    continue

                # 계산 결과가 {1} over {a1} 보다 작은 것이 2개 이하인 경우만 사용
                if 1 <= len(true_dict) <= 2:
                    # 선택지 랜덤 작업
                    exp_list = random.sample(list(true_dict.keys()) + list(false_dict.keys()), 4)
                    exp_1, exp_2, exp_3, exp_4 = exp_list

                    for i, e in enumerate(exp_list):
                        if e in true_dict:
                            answers.append(multiple_choice_hangul[i])
                            comments.append(true_dict[e])
                        else:
                            comments.append(false_dict[e])

                    ans_1, ans_2, ans_3, ans_4 = comments
                    ans = ", ".join(answers)

                    flag = False


    stem = stem.format(frac_1=frac_1, exp_1=exp_1, exp_2=exp_2, exp_3=exp_3, exp_4=exp_4)
    answer = answer.format(ans=ans)
    comment = comment.format(ans_1=ans_1, ans_2=ans_2, ans_3=ans_3, ans_4=ans_4, frac_1=frac_1, ans=ans)

    return stem, answer, comment











































# 5-2-2-35
def fractionmul522_Stem_023():
    stem = "한 시간에 $$수식$${frac_1} `rm {{km}}$$/수식$$를 가는 {N1}{N1_josa} 같은 빠르기로 $$수식$${frac_2}$$/수식$$시간 동안 갈 수 있는 거리는 몇 $$수식$$rm {{km}}$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${frac_3} `rm {{km}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$$$수식$${frac_2}$$/수식$$시간 동안 갈 수 있는 거리$$수식$$RIGHT ) ` = ` {frac_1} `TIMES` {frac_2} `=` {frac_3} ` LEFT ( rm {{km}} RIGHT )$$/수식$$\n\n"


    STEM_023_DICT = ['낙타', '기린', '소', '코뿔소']

    flag = True
    while flag:
        N1 = random.choice(STEM_023_DICT)
        if josa_check(N1[-1]) == ' ':
            N1_josa = "가"
        else:
            N1_josa = "이"

        a1 = random.randint(4, 9)
        a2 = a1 - 1
        b1 = random.randint(10, 20)
        b2 = a1

        t1 = a1 * b1
        t2 = a2 * b2
        G = get_gcd(t1, t2)
        s1 = t1 // G
        s2 = t2 // G

        # 곱셈 계산 결과가 100이 넘지 않도록 제한
        if s1 < 100 and s2 < 100:
            frac_1 = "{%s} over {%s}" % (a2, a1)
            frac_2 = "{%s} over {%s}" % (b2, b1)
            frac_3 = "{%s} over {%s}" % (s2, s1)

            flag = False


    stem = stem.format(frac_1=frac_1, frac_2=frac_2, N1=N1, N1_josa=N1_josa)
    answer = answer.format(frac_3=frac_3)
    comment = comment.format(frac_1=frac_1, frac_2=frac_2, frac_3=frac_3)

    return stem, answer, comment










































# 5-2-2-36
def fractionmul522_Stem_024():
    stem = "$$수식$${box}$$/수식$$ 안에 들어갈 수 있는 $$수식$$2$$/수식$$ 이상인 자연수는 모두 몇 개인가요?\n$$표$$$$수식$${frac_1} `&lt;` {frac_2} `TIMES` {frac_3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${frac_2} `TIMES` {frac_3} `=` {frac_4}$$/수식$$이고 $$수식$${frac_1} `&lt;` {frac_4}$$/수식$$이므로\n" \
              "$$수식$${b1} `&gt;` {a1} `TIMES` {box}$$/수식$$입니다.\n" \
              "$$수식$${a1} `TIMES` {s1} `=` {S1}$$/수식$$, $$수식$${a1} `TIMES` {s2} `=` {S2}$$/수식$$이므로 $$수식$${box}$$/수식$$ 안에 " \
              "들어갈 수 있는 $$수식$$2$$/수식$$ 이상이고 $$수식$${S3}$$/수식$$ 이하인 수는 $$수식$${X1}$$/수식$${X1_josa} $$수식$${S}$$/수식$$개입니다.\n\n"


    flag = True
    while flag:
        n = np.random.choice(range(2, 8))
        a1 = np.random.choice(range(5, 10))
        t1 = a1 * n
        b1 = np.random.choice([t1 + a1 - 1, t1 + a1 - 2, t1 + a1 - 3, t1 + a1 - 4])
        s1 = n
        s2 = n + 1
        S1 = a1 * s1
        S2 = a1 * s2
        S3 = s1
        S = S3 - 1
        X1_list = list(range(2, 2 + S))
        X1 = "$$/수식$$, $$수식$$".join(map(str, X1_list))
        X1_josa = num_josa(X1_list[-1])[4]

        # 2 이상인 자연수가 2개 이상이도록 제한
        if len(X1_list) >= 2:
            frac_1 = "{1} over {%s}" % b1
            frac_2 = "{1} over {%s}" % a1
            frac_3 = "{1} over {%s}" % box
            frac_4 = "{1} over {%s `TIMES` %s}" % (a1, box)

            flag = False


    stem = stem.format(box=box, frac_1=frac_1, frac_2=frac_2, frac_3=frac_3)
    answer = answer.format(S=S)
    comment = comment.format(frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4, a1=a1, b1=b1, s1=s1, s2=s2,
                             S=S, S1=S1, S2=S2, S3=S3, X1=X1, X1_josa=X1_josa, box=box)

    return stem, answer, comment















































# 5-2-2-37
def fractionmul522_Stem_025():
    stem = "$$수식$${A}$$/수식$$분의 $$수식$${frac_1}$$/수식$${a2_josa} 몇 시간인가요?\n"
    answer = "(정답)\n$$수식$${frac_4}$$/수식$$시간\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$분$$수식$$`=` {frac_2}$$/수식$$시간$$수식$$`=` {frac_3}$$/수식$$시간\n" \
              "$$수식$${A}$$/수식$$분의 $$수식$${frac_1}$$/수식$${a2_josa} " \
              "$$수식$${frac_3} `TIMES` {frac_1} `=` {frac_4} LEFT ($$/수식$$시간$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    flag = True
    
    while flag:
        A, a1 = random.choice([(20, 2), (24, 2), (36, 3), (42, 7), (45, 3), (48, 4)])
        a2 = a1 - 1
        s1 = A
        s2 = 60
        G1 = get_gcd(s1, s2)
        s3 = s1 // G1
        s4 = s2 // G1
        t1 = s3 * a2
        t2 = s4 * a1
        G2 = get_gcd(t1, t2)
        s5 = t1 // G2
        s6 = t2 // G2

        a2_josa = num_josa(a2)[1]

        if t1 % G2 == 0 and t2 % G2 == 0 and s5 < s6:
            flag = False

            frac_1 = "{%s} over {%s}" % (a2, a1)
            frac_2 = "{%s} over {%s}" % (s1, s2)
            frac_3 = "{%s} over {%s}" % (s3, s4)
            frac_4 = "{%s} over {%s}" % (s5, s6)


    stem = stem.format(A=A, frac_1=frac_1, a2_josa=a2_josa)
    answer = answer.format(frac_4=frac_4)
    comment = comment.format(A=A, frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4, a2_josa=a2_josa)

    return stem, answer, comment












































# 5-2-2-38
def fractionmul522_Stem_026():
    stem = "{N1}{N1_josa1} {N2}{N2_josa1} 같이 서점에 가서 같은 문제집을 한 권씩 샀습니다. {N1}{N1_josa2} 첫째 날에는 전체의 $$수식$${frac_1}$$/수식$${frac_1_josa}, 둘째 날에는 남은 양의 $$수식$${frac_2}$$/수식$${frac_2_josa} 풀었고, {N2}{N2_josa1} 첫째 날에는 전체의 $$수식$${frac_2}$$/수식$${frac_2_josa} 풀고 둘째 날에는 남은 양의 $$수식$${frac_3}$$/수식$${frac_3_josa} 풀었습니다. 둘째 날 문제집을 푼 양은 누가 더 많은가요?\n"
    answer = "(정답)\n{S}\n"
    comment = "(해설)\n" \
              "둘째 날 푼 양이 한 권의 얼마인지 알아보면\n" \
              "{N1} : $$수식$$LEFT ( 1 `-` {frac_1} RIGHT ) `TIMES` {frac_2} `=` {frac_4} `TIMES` {frac_2} `=` {frac_5}$$/수식$$\n" \
              "{N2} : $$수식$$LEFT ( 1 `-` {frac_2} RIGHT ) `TIMES` {frac_3} `=` {frac_6} `TIMES` {frac_3} `=` {frac_7}$$/수식$$\n" \
              "$$수식$${frac_7} `=` {frac_8}$$/수식$$이므로 {S}{S_josa} 더 많이 풀었습니다.\n\n"


    flag = True
    while flag:
        N1, N2 = np.random.choice(person_nam + person_yeo, 2, replace=False)
        N1_josa1, N1_josa2, N1_josa3 = ["와", "는", "가"] if josa_check(N1[-1]) == ' ' else ["이와", "이는", "이가"]
        N2_josa1, N2_josa2 = ["는", "가"] if josa_check(N2[-1]) == ' ' else ["이는", "이가"]

        # a1 = random.randint(6, 9)
        # a2 = random.randint(1, a1 - 1)

        while True:
            a1 = random.randint(2, 10)
            a2 = random.randint(1, 10)
            if a1 > a2:
                break


        if get_gcd(a1, a2) == 1:
            # b1 = random.randint(3, a1 - 1)
            b2 = 1
            # c1 = random.randint(2, b1 - 1)
            c2 = 1

            b1 = random.randint(2, 10)
            c1 = random.randint(2, 10)

            s1 = a1 - a2
            s2 = a1
            t1 = s1 * b2
            t2 = s2 * b1
            G1 = get_gcd(t1, t2)

            if get_gcd(t1, t2) == 1:
                s3 = t1 // G1
                s4 = t2 // G1
                s5 = b1 - b2
                s6 = b1
                t3 = s5 * c2
                t4 = s6 * c1
                G2 = get_gcd(t3, t4)
                s7 = t3 // G2
                s8 = t4 // G2
                s10 = s4
                s9 = s7 * (s4 // s8)

                if s4 % s8 != 0 or s4 == s8:
                    continue

                if s3 > s9:
                    S = N1
                    S_josa = N1_josa3
                elif s3 < s9:
                    S = N2
                    S_josa = N2_josa2
                else:
                    continue

                flag = False

    frac_1 = "{%s} over {%s}" % (a2, a1)
    frac_2 = "{%s} over {%s}" % (b2, b1)
    frac_3 = "{%s} over {%s}" % (c2, c1)
    frac_4 = "{%s} over {%s}" % (s1, s2)
    frac_5 = "{%s} over {%s}" % (s3, s4)
    frac_6 = "{%s} over {%s}" % (s5, s6)
    frac_7 = "{%s} over {%s}" % (s7, s8)
    frac_8 = "{%s} over {%s}" % (s9, s10)

    frac_1_josa = num_josa(a2)[2]
    frac_2_josa = num_josa(b2)[2]
    frac_3_josa = num_josa(c2)[2]


    stem = stem.format(N1=N1, N1_josa1=N1_josa1, N1_josa2=N1_josa2, N2=N2, N2_josa1=N2_josa1, frac_1=frac_1,
                       frac_2=frac_2, frac_3=frac_3, frac_1_josa=frac_1_josa, frac_2_josa=frac_2_josa,
                       frac_3_josa=frac_3_josa)
    answer = answer.format(S=S)
    comment = comment.format(N1=N1, N2=N2, frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4, frac_5=frac_5,
                             frac_6=frac_6,
                             frac_7=frac_7, frac_8=frac_8, S=S, S_josa=S_josa)

    return stem, answer, comment














































# 5-2-2-39
def fractionmul522_Stem_027():
    stem = "{N1}{N1_josa} 어제까지 책 한 권의 $$수식$${frac_1}$$/수식$${frac_1_josa} 읽었습니다. 그리고 오늘은 어제까지 읽고 난 나머지의 $$수식$${frac_2}$$/수식$${frac_2_josa} 읽었습니다. 책 한 권이 $$수식$${A}$$/수식$$쪽일 때, 어제와 오늘 읽고 난 나머지는 몇 쪽인가요?\n"
    answer = "(정답)\n$$수식$${S1}$$/수식$$쪽\n"
    comment = "(해설)\n" \
              "어제까지 읽고 난 나머지는 책 전체의 $$수식$$1 `-` {frac_1} `=` {frac_3} `-` {frac_1} `=` {frac_4}$$/수식$$이고,\n" \
              "오늘 읽은 양은 책 전체의 $$수식$${frac_4} `TIMES` {frac_2} `=` {frac_5}$$/수식$$입니다.\n" \
              "따라서 오늘까지 읽은 양은 책 전체의 $$수식$${frac_1} `+` {frac_5} `=` {frac_6} `+` {frac_5} `=` {frac_7}$$/수식$$입니다.\n" \
              "오늘까지 읽고 난 나머지는 책 전체의 $$수식$$1 `-` {frac_7} `=` {frac_8} `-` {frac_7} `=` {frac_9}$$/수식$$이므로\n" \
              "오늘까지 읽고 난 나머지는 $$수식$${A} `TIMES` {frac_9} `=` {S1} ` LEFT ($$/수식$$쪽$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    flag = True
    
    while flag:
        N1 = np.random.choice(person_nam + person_yeo)
        N1_josa = "는" if josa_check(N1[-1]) == " " else "이는"

        a1 = random.randint(6, 9)
        a2 = random.randint(2, a1)

        if get_gcd(a1, a2) == 1:
            b1 = random.randint(2, a1)
            b2 = 1
            s1 = a1 - a2
            s2 = a1
            s3 = s1 * b2
            s4 = s2 * b1
            s6 = s4
            s5 = a2 * (s4 // a1)
            G = get_gcd(s5 + s3, s6)
            s7 = (s5 + s3) // G
            s8 = s4 // G
            s9 = s8 - s7
            s10 = s8

            tmp = random.randint(5, 20)
            A = s10 * tmp
            S1 = s9 * tmp

            frac_1 = "{%s} over {%s}" % (a2, a1)
            frac_1_josa = num_josa(a2)[2]
            frac_2 = "{%s} over {%s}" % (b2, b1)
            frac_2_josa = num_josa(b2)[2]
            frac_3 = "{%s} over {%s}" % (a1, a1)
            frac_4 = "{%s} over {%s}" % (s1, s2)
            frac_5 = "{%s} over {%s}" % (s3, s4)
            frac_6 = "{%s} over {%s}" % (s5, s6)
            frac_7 = "{%s} over {%s}" % (s7, s8)
            frac_8 = "{%s} over {%s}" % (s8, s8)
            frac_9 = "{%s} over {%s}" % (s9, s10)

            # 책의 페이지 수가 500쪽이 넘지 않도록 제한
            if S1 < 500 and A < 500:
                flag = False


    stem = stem.format(N1=N1, N1_josa=N1_josa, frac_1=frac_1, frac_1_josa=frac_1_josa, frac_2=frac_2,
                       frac_2_josa=frac_2_josa, A=A)
    answer = answer.format(S1=S1)
    comment = comment.format(frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4, frac_5=frac_5, frac_6=frac_6,
                             frac_7=frac_7, frac_8=frac_8, frac_9=frac_9, A=A, S1=S1)

    return stem, answer, comment















































# 5-2-2-40
def fractionmul522_Stem_028():
    stem = "{N1}{N1_josa} 가방 무게는 $$수식$${frac_1} `rm kg$$/수식$$이고, {N2}{N2_josa} 가방 무게는 {N1}{N1_josa} 가방 무게의 $$수식$${frac_2}$$/수식$$배보다 $$수식$${frac_3} `rm kg$$/수식$$ 더 가볍습니다. {N2}{N2_josa} 가방 무게는 몇 $$수식$$rm kg$$/수식$$인지 가장 간단한 분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${ans}` rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$$$수식$${frac_1} `rm kg$$/수식$$의 $$수식$${frac_2}$$/수식$$배" \
              "$$수식$$RIGHT ) ` = ` {frac_1} `TIMES` {frac_2} `=` {frac_4} ` LEFT ( rm kg RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${N2}{N2_josa} 가방 무게$$수식$$RIGHT ) ` = ` {frac_4} `-` {frac_3} `=` {frac_5} ` LEFT ( rm kg RIGHT )$$/수식$$\n\n"


    flag = True
    
    while flag:
        N1, N2 = np.random.choice(person_nam + person_yeo, 2, replace=False)
        N1_josa = "의" if josa_check(N1[-1]) == ' ' else "이의"
        N2_josa = "의" if josa_check(N2[-1]) == ' ' else "이의"

        a1 = random.randint(6, 9)
        a2 = a1 - 1

        b1 = random.randint(2, a1 - 1)
        b2 = b1 - 1
        t1 = a1 * b1
        t2 = a2 * b2
        G1 = get_gcd(t1, t2)
        c1 = t1 // G1
        c2 = 1

        s1 = t2 // G1
        s2 = c1
        t3 = s1 - c2
        t4 = c1
        G2 = get_gcd(t3, t4)

        s3 = t3 // G2
        s4 = t4 // G2

        frac_1 = "{%s} over {%s}" % (a2, a1)
        frac_2 = "{%s} over {%s}" % (b2, b1)
        frac_3 = "{%s} over {%s}" % (c2, c1)
        frac_4 = "{%s} over {%s}" % (s1, s2)
        if G2 != 1:
            frac_5 = "{%s} over {%s} `=` {%s} over {%s}" % (t3, t4, s3, s4)
        else:
            frac_5 = "{%s} over {%s}" % (s3, s4)
        ans = "{%s} over {%s}" % (s3, s4)

        if s3 < s4 and 0 not in [s1, s2, s3, s4]:
            flag = False


    stem = stem.format(N1=N1, N1_josa=N1_josa, N2=N2, N2_josa=N2_josa, frac_1=frac_1, frac_2=frac_2, frac_3=frac_3)
    answer = answer.format(ans=ans)
    comment = comment.format(N2=N2, N2_josa=N2_josa, frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4,
                             frac_5=frac_5)

    return stem, answer, comment
















































# 5-2-2-43
def fractionmul522_Stem_029():
    stem = "$$수식$${box}$$/수식$$안에 들어갈 수 있는 자연수는 모두 몇 개인가요?\n$$표$$$$수식$${box}`{frac_1} `&lt;` {frac_2} `TIMES` {frac_3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${frac_2} `TIMES` {frac_3} `=` {frac_4} `TIMES` {frac_5} `=` {frac_6} `=` {frac_7}$$/수식$$이므로\n" \
              "$$수식$${box}`{frac_1} `&lt;` {frac_7}$$/수식$$입니다.\n" \
              "따라서 $$수식$${box}$$/수식$$ 안에 들어갈 수 있는 자연수는 " \
              "$$수식$${X1}$$/수식$${X1_josa} 모두 $$수식$${S}$$/수식$$개입니다.\n\n"


    flag = True
    while flag:
        a1, b1 = random.choice([(2, 4), (2, 6), (2, 8), (3, 6), (3, 9), (4, 8)])
        a2, b2 = 1, 1
        a3 = random.randint(1, 4)
        b3 = 5 - a1

        s1 = (b3 * b1) + b2
        s2 = b1
        s3 = (a3 * a1) + a2
        s4 = a1
        t1 = s1 * s3
        t2 = s2 * s4
        G1 = get_gcd(t1, t2)
        s5 = t1 // G1
        s6 = t2 // G1
        s7 = s5 // s6
        s8 = s5 - (s6 * s7)
        s9 = s6
        c1 = s9
        c2 = c1 - 1

        S = s7 - 1
        if S > 1:
            X1_list = list(range(1, S + 1))
            X1 = "$$/수식$$, $$수식$$".join(map(str, X1_list))
            X1_josa = num_josa(X1_list[-1])[4]

            # box 안에 들어갈 수 있는 자연수 개수를 2개 이상 8개 이하로 제한
            if 8 >= len(X1_list) >= 2:
                flag = False

                frac_1 = "{%s} over {%s}" % (c2, c1)
                frac_2 = "%s {%s} over {%s}" % (b3, b2, b1)
                frac_3 = "%s {%s} over {%s}" % (a3, a2, a1)
                frac_4 = "{%s} over {%s}" % (s1, s2)
                frac_5 = "{%s} over {%s}" % (s3, s4)
                frac_6 = "{%s} over {%s}" % (s5, s6)
                frac_7 = "%s {%s} over {%s}" % (s7, s8, s9)


    stem = stem.format(box=box, frac_1=frac_1, frac_2=frac_2, frac_3=frac_3)
    answer = answer.format(S=S)
    comment = comment.format(frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4, frac_5=frac_5, frac_6=frac_6,
                             frac_7=frac_7, box=box, X1=X1, X1_josa=X1_josa, S=S)

    return stem, answer, comment
















































# 5-2-2-45
def fractionmul522_Stem_030():
    stem = "$$수식$$1$$/수식$$분에 $$수식$${frac_1} `rm L$$/수식$$씩 나오는 수도가 있습니다. 이 수도에서 $$수식$${frac_2}$$/수식$$분 동안 받은 물은 모두 몇 $$수식$$rm L$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${S}`rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$받은 물의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$=` {frac_1} `TIMES` {frac_2} `=` {frac_3} `TIMES` {frac_4} `=` {S} ` LEFT ( rm L RIGHT )$$/수식$$\n\n"


    flag = True
    while flag:
        n = random.randint(2, 6)
        s1, s2 = random.choice([(12, 2), (12, 3), (12, 4), (12, 6), (14, 2), (14, 7), (16, 2), (16, 4), (16, 8),
                                (18, 2), (18, 3), (18, 6), (18, 9), (20, 2), (20, 4), (20, 5), (20, 10),
                                (24, 2), (24, 3), (24, 4), (24, 6), (24, 8), (24, 12), (28, 2), (28, 4), (28, 7),
                                (28, 14)])

        s3 = random.randint(2, s1)
        s4 = n * s3
        if get_gcd(s1, s3) == 1 and get_gcd(s2, s4) == 1 and s4 > s2:
            a1 = s3
            a2 = s1 // s3
            a3 = s1 - (a2 * a1)
            b1 = s2
            b2 = s4 // s2
            b3 = s4 - (b2 * b1)

            t1 = s1 * s4
            t2 = s3 * s2

            S = (s1 // s2) * (s4 // s3)

            frac_1 = "%s {%s} over {%s}" % (a2, a3, a1)
            frac_2 = "%s {%s} over {%s}" % (b2, b3, b1)
            frac_3 = "{%s} over {%s}" % (s1, s3)
            frac_4 = "{%s} over {%s}" % (s4, s2)

            # 물의 양을 100리터 이하로 제한
            if S < 100:
                flag = False


    stem = stem.format(frac_1=frac_1, frac_2=frac_2)
    answer = answer.format(S=S)
    comment = comment.format(frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4, S=S)

    return stem, answer, comment













































# 5-2-2-51
# 모델링 다시 : S1, S2 조건 수정
def fractionmul522_Stem_031():
    stem = "지난달 {N1}{N1_josa1} {N2}{N2_josa1} 몸무게는 각각 $$수식$${frac_1} ` rm kg$$/수식$$, $$수식$${frac_2} `rm kg$$/수식$$이었습니다. 이번 달에 몸무게를 재어 보니 지난달보다 {N1}{N1_josa2} $$수식$${frac_3}$$/수식$$만큼 늘었고, {N2}{N2_josa2} $$수식$${frac_4}$$/수식$$만큼 줄었습니다. 이번 달에는 누가 더 무겁나요?\n"
    answer = "(정답)\n{S}\n"
    comment = "(해설)\n" \
              "이번 달 {N1}{N1_josa3} 몸무게는 $$수식$${frac_1} `TIMES` 1 {frac_3} `=` {frac_5} `TIMES` {frac_6} `=` {frac_7} `=` {S1} ` LEFT ( rm kg RIGHT )$$/수식$$이고,\n" \
              "이번 달 {N2}{N2_josa1} 몸무게는 $$수식$${frac_2} `TIMES` {frac_8} `=` {frac_9} `TIMES` {frac_10} `=` {frac_11} `=` {S2} ` LEFT ( rm kg RIGHT )$$/수식$$입니다.\n" \
              "$$수식$${S1} `{T}` {S2}$$/수식$$이므로 {S}{S_josa} 몸무게가 더 무겁습니다.\n\n"


    flag = True
    while flag:
        N1, N2 = np.random.choice(person_nam + person_yeo, 2, replace=False)

        if N1[0] == N2[0] or N1[1] == N2[1] or N1[0] == N2[1] or N1[1] == N2[0]:
            continue

        N1_josa1, N1_josa2, N1_josa3 = ["와", "는", "의"] if josa_check(N1[-1]) == ' ' else ["이와", "이는", "이의"]
        N2_josa1, N2_josa2 = ["의", "는"] if josa_check(N2[-1]) == ' ' else ["이의", "이는"]

        a1, b1 = np.random.choice(range(2, 10), 2)
        a2, b2 = sorted(np.random.choice(range(31, 45), 2), reverse=False)
        c1, d1 = np.random.choice(range(6, 9), 2)
        d2 = d1 - 1
        s1 = (a2 * a1) + 1
        s2 = a1
        s3 = c1 + 1
        s4 = c1
        t1 = s1 * s3
        t2 = s2 * s4
        G1 = get_gcd(t1, t2)
        s5 = t1 // G1
        s6 = t2 // G1
        s7 = s5 // s6
        s8 = s5 - (s6 * s7)
        s9 = s6

        if s8 == s9:
            S1 = s7
            _S1 = s7
        elif s8 == 0 and s9 == 1 and s7 >= 1:
            S1 = s7
            _S1 = s7
        else:
            S1 = "%s {%s} over {%s}" % (s7, s8, s9)
            _S1 = s7 + (s8 / s9)

        r1 = (b2 * b1) + 1
        r2 = b1
        t3 = r1 * (d1 - 1)
        t4 = r2 * d1

        G2 = get_gcd(t3, t4)
        r3 = t3 // G2
        r4 = t4 // G2

        r5 = r3 // r4
        r6 = r3 - (r4 * r5)
        r7 = r4

        if r5 == r6:
            S2 = r5
            _S2 = r5
        elif r5 >= 1 and r6 == 0 and r7 == 1:
            S2 = r5
            _S2 = r5
        else:
            S2 = "%s {%s} over {%s}" % (r5, r6, r7)
            _S2 = r5 + (r6 / r7)

        # 곱셈 과정에서 곱셈 결과가 1000이 넘지 않도록 제한, 분모 조건 확인
        if r3 < 1000 and s5 < 1000 and 0 not in [s5, s6, r3, r4]:
            if _S1 > _S2:
                T = "&gt;"
                S = N1
                S_josa = N1_josa3
                flag = False
            elif _S1 < _S2:
                T = "&lt;"
                S = N2
                S_josa = N2_josa1
                flag = False
            else:
                continue

    frac_1 = "%s {1} over {%s}" % (a2, a1)
    frac_2 = "%s {1} over {%s}" % (b2, b1)
    frac_3 = "{1} over {%s}" % c1
    frac_4 = "{1} over {%s}" % d1
    frac_5 = "{%s} over {%s}" % (s1, s2)
    frac_6 = "{%s} over {%s}" % (s3, s4)
    frac_7 = "{%s} over {%s}" % (s5, s6)
    frac_8 = "{%s} over {%s}" % (d2, d1)
    frac_9 = "{%s} over {%s}" % (r1, r2)
    frac_10 = "{%s} over {%s}" % (d2, d1)
    frac_11 = "{%s} over {%s}" % (r3, r4)


    stem = stem.format(N1=N1, N1_josa1=N1_josa1, N1_josa2=N1_josa2, N2=N2, N2_josa1=N2_josa1, N2_josa2=N2_josa2,
                       frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4)
    answer = answer.format(S=S)
    comment = comment.format(N1=N1, N1_josa3=N1_josa3, N2=N2, N2_josa1=N2_josa1,
                             frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4, frac_5=frac_5, frac_6=frac_6,
                             frac_7=frac_7, frac_8=frac_8, frac_9=frac_9, frac_10=frac_10, frac_11=frac_11,
                             S1=S1, S2=S2, S=S, S_josa=S_josa, T=T)

    return stem, answer, comment













































# 5-2-2-52
# 모델링 다시 : r4, r5 조건 수정
def fractionmul522_Stem_032():
    stem = "$$수식$${frac_1}$$/수식$$에 어떤 수를 곱해야 할 것을 잘못하여 뺐더니 $$수식$${frac_2}$$/수식$${b2_josa} 되었습니다. 바르게 계산한 값은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${frac_8}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 $$수식$${box}$$/수식$$라 하면 잘못 계산한 식은\n" \
              "$$수식$${frac_1} `-` {box} `=` {frac_2}$$/수식$$입니다.\n" \
              "$$수식$${box} `=` {frac_1} `-` {frac_2} `=` {frac_3} `-` {frac_2} `=` {frac_4} `-` {frac_2} `=` {frac_5} `=` {frac_6}$$/수식$$\n" \
              "바르게 계산하면\n" \
              "$$수식$${frac_1} `TIMES` {frac_6} `=` {frac_3} `TIMES` {frac_5} `=` {frac_7} `=` {frac_8}$$/수식$$입니다.\n\n"


    flag = True
    while flag:
        a1 = random.randint(2, 4)
        a2 = a1 - 1
        a3 = random.randint(2, 9)
        b1 = a1 * 2
        b2 = random.randint(2, b1)

        if get_gcd(b1, b2) == 1:
            s1 = a3 * a1 + a2
            s2 = a1
            s3 = s1 * 2
            s4 = s2 * 2
            s5 = s3 - b2
            s6 = s4
            s7 = s5 // s6
            s8 = s5 - s6 * s7
            s9 = s6

            t1 = s1 * s5
            t2 = s2 * s6
            G1 = get_gcd(t1, t2)

            r1 = t1 // G1
            r2 = t2 // G1

            r3 = r1 // r2
            r4 = r1 - r3 * r2
            r5 = r2

            # 곱셈 결과값이 1000이 넘지 않도록 제한, 분모 및 분자 조건 확인
            if r1 < 1000 and 0 not in [s5, s6, r1, r2] and 1 not in [s6, r2, s9, r5]:
                if get_gcd(r4, r5) != 1:
                    print("0")
                flag = False

    frac_1 = "%s {%s} over {%s}" % (a3, a2, a1)
    frac_2 = "{%s} over {%s}" % (b2, b1)
    frac_3 = "{%s} over {%s}" % (s1, s2)
    frac_4 = "{%s} over {%s}" % (s3, s4)
    frac_5 = "{%s} over {%s}" % (s5, s6)
    frac_6 = "%s {%s} over {%s}" % (s7, s8, s9)
    frac_7 = "{%s} over {%s}" % (r1, r2)
    frac_8 = "%s {%s} over {%s}" % (r3, r4, r5)

    b2_josa = num_josa(b2)[3]


    stem = stem.format(frac_1=frac_1, frac_2=frac_2, b2_josa=b2_josa)
    answer = answer.format(frac_8=frac_8)
    comment = comment.format(frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4, frac_5=frac_5, frac_6=frac_6,
                             frac_7=frac_7, frac_8=frac_8, box=box)

    return stem, answer, comment












































# 5-2-2-53
def fractionmul522_Stem_033():
    stem = "하루에 $$수식$${frac_1}$$/수식$$분씩 빨라지는 시계가 있습니다. 이 시계를 오늘 오전 $$수식$${A}$$/수식$$시에 정확하게 맞추어 놓았습니다. $$수식$${B}$$/수식$$일 후 오전 $$수식$${A}$$/수식$$시에 이 시계가 가리키는 시각은 오전 몇 시 몇 분 몇 초인가요?\n"
    answer = "(정답)\n$$수식$${A}$$/수식$$시 $$수식$${S1}$$/수식$$분 $$수식$${S2}$$/수식$$초\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( {B}$$/수식$$일 동안 빨라지는 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$=` {frac_1} `TIMES` {B} `=` {frac_2} `TIMES` {B} `=` {frac_3} `=` {frac_4} ` LEFT ($$/수식$$분$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${frac_4}$$/수식$$분$$수식$$ `=` {frac_5}$$/수식$$분$$수식$$`=` {S1}$$/수식$$분 $$수식$${S2}$$/수식$$초\n" \
              "따라서 $$수식$${B}$$/수식$$일 후 오전 $$수식$${A}$$/수식$$시에 이 시계가 가리키는 시각은 오전 $$수식$${A}$$/수식$$시 $$수식$${S1}$$/수식$$분 $$수식$${S2}$$/수식$$초입니다.\n\n"


    flag = True
    while flag:
        a1 = random.choice([2, 3, 4, 6])
        a2 = 1
        a3 = 1
        n = random.randint(1, 8)
        A = random.randint(6, 11)
        B = random.randint(3, 9)

        if B % a1 != 0:
            s1 = a3 * a1 + a2
            s2 = a1
            t1 = s1 * B
            t2 = s2
            # G1 = get_gcd(s1, s2)
            G1 = get_gcd(t1, t2)
            s3 = t1 // G1
            s4 = t2 // G1
            s5 = s3 // s4
            s6 = s3 - s4 * s5
            s7 = s4
            t3 = 60 // s7
            r1 = s5
            r2 = s6 * t3
            r3 = 60
            S1 = s5
            S2 = r2

            frac_1 = "%s {%s} over {%s}" % (a3, a2, a1)
            frac_2 = "{%s} over {%s}" % (s1, s2)
            frac_3 = "{%s} over {%s}" % (s3, s4)
            frac_4 = "%s {%s} over {%s}" % (s5, s6, s7)
            frac_5 = "%s {%s} over {%s}" % (r1, r2, r3)

            # 곱셈 결과값이 1000이 넘지 않도록 제한, 분모 조건 확인
            if s6 < 1000 and 0 not in [s6, s7, r2, r3, s5]:
                flag = False


    stem = stem.format(frac_1=frac_1, A=A, B=B)
    answer = answer.format(A=A, S1=S1, S2=S2)
    comment = comment.format(S1=S1, S2=S2, A=A, B=B, frac_1=frac_1, frac_2=frac_2, frac_3=frac_3, frac_4=frac_4,
                             frac_5=frac_5)

    return stem, answer, comment





























# if __name__ == '__main__':
#     FracMultiple_Stem_001()
#     FracMultiple_Stem_002()
#     FracMultiple_Stem_003()
#     FracMultiple_Stem_004()
#     FracMultiple_Stem_005()
#     FracMultiple_Stem_006()
#     FracMultiple_Stem_007()
#     FracMultiple_Stem_008()
#     FracMultiple_Stem_009()
#     FracMultiple_Stem_010()
#     FracMultiple_Stem_011()
#     FracMultiple_Stem_012()
#     FracMultiple_Stem_013()
#     FracMultiple_Stem_014()
#     FracMultiple_Stem_015()
#     FracMultiple_Stem_016()
#     FracMultiple_Stem_017()
#     FracMultiple_Stem_018()
#     FracMultiple_Stem_019()
#     FracMultiple_Stem_020()
#     FracMultiple_Stem_021()
#     FracMultiple_Stem_022()
#     FracMultiple_Stem_023()
#     FracMultiple_Stem_024()
#     FracMultiple_Stem_025()
#     FracMultiple_Stem_026()
#     FracMultiple_Stem_027()
#     FracMultiple_Stem_028()
#     FracMultiple_Stem_029()
#     FracMultiple_Stem_030()
#     FracMultiple_Stem_031()
#     FracMultiple_Stem_032()
#     FracMultiple_Stem_033()






