import numpy as np
import codecs
import os
import random

#PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), './../../Dictionary')
PATH = '/home/boin-service/Visang/Dictionary/'


person_nam = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XY.txt'), 'r', 'utf-8').readlines()]
person_yeo = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XX.txt'), 'r', 'utf-8').readlines()]

have_jongsung_num = [0, 1, 3, 6, 7, 8]
multiple_choice_jaem = {0: '㉠', 1: '㉡', 2: '㉢', 3: '㉣'}
multiple_choice_nums = {0: '①', 1: '②', 2: '③', 3: '④', 4: '⑤'}
multiple_choice_nums_2 = {0: '㉠', 1: '㉡', 2: '㉢', 3: '㉣', 4: '㉤'}






box = "□"
box_1 = "①"
box_2 = "②"
box_1a = "box{㉠````````````````````}"
box_2a = "box{㉡````````````````````}"
right = "&lt;"
left = "&gt;"





# 조사 확인(이름 뒤)
def josa_check(name):
    JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                     'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    char_code = ord(name) - 44032
    ch1 = int(char_code / 588)
    ch2 = int((char_code - (588 * ch1)) / 28)
    ch3 = int((char_code - (588 * ch1) - (28 * ch2)))

    return JONGSUNG_LIST[ch3]








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
        return ["과", "은", "을", "이", "으로"]
    else:
        return ["와", "는", "를", "가", "로"]












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
    # 조사 은, 는
    else:
        if num in [2, 4, 5, 9]:
            return '는'
        return '은'













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












def han_josa(name):
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













def get_divisors(number):
    '''
    numbers의 약수 리스트 리턴 함수
    :param number:
    :return:
    '''
    divisors = []
    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)

    return divisors











# 최대공약수
def get_gcd(num1, num2) :
    num1, num2 = sorted([num1, num2])
    gcd = 1
    for i in range(num1, 0, -1) :
        if num1 % i == 0 and num2 % i == 0 :
            gcd = i
            break

    return gcd









# 최대공배수
def get_lcm(num1, num2) :
    return num1 * num1 // get_gcd(num1, num2)
















# 5-1-1-01
def naturalmixcal511_Stem_001() :
    stem = "계산 결과의 크기를 비교하여 $$수식$${box}$$/수식$$ 안에 $$수식$${left}$$/수식$$, $$수식$$=$$/수식$$, $$수식$${right}$$/수식$$를 알맞게 써넣으세요.\n$$수식$${a1}~~{box}~~{a2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a1} ` = ` {c1}$$/수식$$,\n" \
              "$$수식$${a2} ` = ` {c2}$$/수식$$\n" \
              "$$수식$${c3}$$/수식$$이므로\n" \
              "$$수식$${a1}~{cor_text}~{a2}$$/수식$$입니다.\n\n"


    flag = True

    while flag :
        s1 = np.random.randint(15, 30, 1)[0]
        s2 = np.random.randint(10, 15, 1)[0]
        s3 = np.random.randint(10, 30, 1)[0]
        s4, s5 = np.random.choice(np.arange(10, 31), 2, False)
        s6 = np.random.randint(10, 20, 1)[0]
        s7 = s1 - s2
        s8 = s4 + s5
        s9 = s7 + s3
        s10 = s8 - s6
        if len(set([s1, s2, s3, s4, s5, s6])) == 6 and s8 > 0 and s10 > 0 :
            flag = False

    a1 = '%d ` - ` %d ` + ` %d' % (s1, s2, s3)
    a2 = '%d ` + ` %d ` - ` %d' % (s4, s5, s6)


    c1 = '%d ` + ` %d ` = ` %d' % (s7, s3, s9)
    c2 = '%d ` - ` %d ` = ` %d' % (s8, s6, s10)

    cor_text = ' = ' if s9 == s10 else right if s9 < s10 else left
    c3 = '%d ` %s ` %d' % (s9, cor_text, s10)

    stem = stem.format(box=box, left=left, right=right, a1=a1, a2=a2)
    answer = answer.format(cor_text=cor_text)
    comment= comment.format(a1=a1, a2=a2, c1=c1, c2=c2, c3=c3, cor_text=cor_text)

    return stem, answer, comment
























# 5-1-1-03
def naturalmixcal511_Stem_002() :
    stem = "다음을 보고 하나의 식으로 나타내어 계산해 보세요.\n$$표$${a1}$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_exp}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${c1}$$/수식$$\n\n"


    mode = np.random.choice([0, 1], 1)[0]

    flag = True

    while flag:

        s1 = np.random.randint(31, 70, 1)[0]
        s2 = np.random.randint(11, 25, 1)[0]
        s3 = np.random.randint(11, 30, 1)[0]
        j2 = '을' if (s2 % 10) in have_jongsung_num else '를'
        j3 = '을' if (s3 % 10) in have_jongsung_num else '를'

        if mode == 0:
            s4 = s1 - s2
            s5 = s4 + s3
            a1 = '$$수식$${s1}$$/수식$$에서 $$수식$${s2}$$/수식$${j2} 뺀 후, $$수식$${s3}$$/수식$${j3} 더합니다.'.format(s1=s1, s2=s2, s3=s3, j2=j2, j3=j3)
            c1 = '%d ` - ` %d ` + ` %d ` = ` %d ` + ` %d ` = ` %d' % (s1, s2, s3, s4, s3, s5)
            cor_exp = '%d ` - ` %d ` + ` %d ` = ` %d' % (s1, s2, s3, s5)
        else:
            s4 = s1 + s2
            s5 = s4 - s3
            a1 = '$$수식$${s1}$$/수식$$에서 $$수식$${s2}$$/수식$${j2} 더한 후, $$수식$${s3}$$/수식$${j3} 뺍니다.'.format(s1=s1, s2=s2, s3=s3, j2=j2, j3=j3)
            c1 = '%d ` + ` %d ` - ` %d ` = ` %d ` - ` %d ` = ` %d' % (s1, s2, s3, s4, s3, s5)
            cor_exp = '%d ` + ` %d ` - ` %d ` = ` %d' % (s1, s2, s3, s5)

        if s4 > 0 and s5 > 0 and s2 != s3:
            flag = False


    stem = stem.format(a1=a1)
    answer = answer.format(cor_exp=cor_exp)
    comment = comment.format(c1=c1)

    return stem, answer,comment































# 5-1-1-04
def naturalmixcal511_Stem_003() :
    stem = "$$수식$$LEFT ( ~~ RIGHT )$$/수식$$가 없어도 계산 결과가 같은 식은 어느 것인가요?\n① $$수식$${a1}$$/수식$$\n② $$수식$${a2}$$/수식$$\n③ $$수식$${a3}$$/수식$$\n④ $$수식$${a4}$$/수식$$\n⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{cor_num}\n"
    comment = "(해설)\n" \
              "$$수식$${c1}$$/수식$$\n" \
              "$$수식$${c2}$$/수식$$\n" \
              "따라서 $$수식$$LEFT ( ~~ RIGHT )$$/수식$$가 없어도 계산 결과가 같은 식은 {cor_num}입니다.\n\n"


    flag = True

    while flag:
        s1, s4, s7, s10, s13 = np.random.choice(np.arange(11, 30), 5, False)
        answers = []
        # A - (a + b)
        s2, s3 = np.random.choice(np.arange(1, 5), 2, False)
        answers.append('%d ` - ` LEFT ( %d ` + ` %d RIGHT )' % (s1, s2, s3))

        # B - (c + d)
        s5, s6 = np.random.choice(np.arange(1, 5), 2, False)
        answers.append('%d ` - ` LEFT ( %d ` + ` %d RIGHT )' % (s4, s5, s6))

        # C + (e - f)
        s8 = np.random.randint(6, 10, 1)[0]
        s9 = np.random.randint(1, 5, 1)[0]
        s16 = s8 - s9
        s17 = s7 + s8
        s18 = s17 - s9
        cor_text = '%d ` + ` LEFT ( %d ` - ` %d RIGHT )' % (s7, s8, s9)
        c1 = '%s ` = ` %d ` + ` %d ` = ` %d' % (cor_text, s7, s16, s18)
        c2 = '%d ` + ` %d ` - ` %d ` = ` %d ` - ` %d ` = ` %d' % (s7, s8, s9, s17, s9, s18)
        answers.append(cor_text)

        # D - (g - h)
        s11 = np.random.randint(6, 10, 1)[0]
        s12 = np.random.randint(1, 5, 1)[0]
        answers.append('%d `-` LEFT ( %d `-` %d RIGHT )' % (s10, s11, s12))

        # E - (i + j)
        s14, s15 = np.random.choice(np.arange(1, 5), 2, False)
        answers.append('%d `-` LEFT ( %d `+` %d RIGHT )' % (s13, s14, s15))

        if len(set([s2, s5, s8, s11, s14])) > 3 and len(set([s3, s6, s9, s12, s15])) > 3 and s16 > 0 and s18 > 0:
            flag = False


    np.random.shuffle(answers)
    a1, a2, a3, a4, a5 = answers
    cor_num = multiple_choice_nums.get(answers.index(cor_text))

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(cor_num=cor_num)
    comment = comment.format(c1=c1, c2=c2, cor_num=cor_num)

    return stem, answer, comment





























# 5-1-1-06
def naturalmixcal511_Stem_004() :
    stem = "식이 성립하도록 $$수식$${box}$$/수식$$ 안에 $$수식$$+$$/수식$$, $$수식$$-$$/수식$$를 알맞게 한 번씩 써넣으세요.\n$$표$$ $$수식$${s1}$$/수식$$ $$수식$${box_1a}$$/수식$$ $$수식$${s2}$$/수식$$ $$수식$${box_2a}$$/수식$$ $$수식$${s3} = {s4}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{cor_text}\n"
    comment = "(해설)\n" \
              "$$수식$${c1}$$/수식$$\n" \
              "$$수식$${c2}$$/수식$$\n\n"


    s1 = np.random.randint(41, 80, 1)[0]
    s2 = np.random.randint(11, 30, 1)[0]
    s3 = np.random.randint(2, 10, 1)[0]

    s4, s5 = [s1 - s2 + s3, s1 + s2 - s3] if s1 % 2 == 0 else [s1 + s2 - s3, s1 - s2 + s3]

    s7, s8 = [s1 - s2, s1 + s2] if s1 % 2 == 0 else [s1 + s2, s1 - s2]

    op1, op2 = ['+', '-'] if s1 % 2 == 0 else ['-', '+']

    c1 = '%d ` %s ` %d ` %s ` %d ` = ` %d ` %s ` %d ` = ` %d ~ LEFT ( ` rm X RIGHT )' % (s1, op1, s2, op2, s3, s8, op2, s3, s5)
    c2 = '%d ` %s ` %d ` %s ` %d ` = ` %d ` %s ` %d ` = ` %d ~ LEFT ( ` rm O RIGHT )' % (s1, op2, s2, op1, s3, s7, op1, s3, s4)

    cor_text = '$$수식$$%s$$/수식$$, $$수식$$%s$$/수식$$' % (op2, op1)

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, box=box, box_1a=box_1a, box_2a=box_2a)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1, c2=c2)

    return stem, answer, comment



































# 5-1-1-07
def naturalmixcal511_Stem_005() :
    stem = "두 식을 계산해 보고, 계산 결과가 더 큰 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${a1}$$/수식$$    ㉡ $$수식$${a2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_jaem}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${a1} ` = ` {c1}$$/수식$$\n" \
              "㉡ $$수식$${a2} ` = ` {c2}$$/수식$$\n" \
              "$$수식$${c3}$$/수식$$이므로 계산 결과가 더 큰 것은 {cor_jaem}입니다.\n\n"


    flag = True

    while flag:
        s1 = np.random.randint(51, 80, 1)[0]
        s2 = np.random.randint(11, 20, 1)[0]
        s3 = np.random.randint(11, 30, 1)[0]
        s4 = s1 - s2
        s5 = s2 + s3
        s6 = s1 - s2 + s3
        s7 = s1 - (s2 + s3)

        if s6 != s7:
            flag = False

    mode = 0 if s6 > s7 else 1
    a1 = '%d ` - ` %d ` + ` %d' % (s1, s2, s3)
    a2 = '%d ` - ` LEFT ( %d ` + ` %d RIGHT )' % (s1, s2, s3)
    c1 = '%d ` + ` %d ` = ` %d' % (s4, s3, s6)
    c2 = '%d ` - ` %d ` = ` %d' % (s1, s5, s7)

    if mode == 0 :
        c3 = '%d ` %s ` %d' % (s6, left, s7)
        cor_jaem = '㉠'
    else :
        c3 = '%d ` %s ` %d' % (s7, left, s6)
        cor_jaem = '㉡'

    flag1 = random.randint(0,1)

    if flag1 == 0:
        c3 = '%d ` %s ` %d' % (s6, left, s7)
        cor_jaem = '㉠'
        stem= stem.format(a1=a1, a2=a2)
        answer = answer.format(cor_jaem=cor_jaem)
        comment = comment.format(a1=a1, a2=a2, c1=c1, c2=c2, c3=c3, cor_jaem=cor_jaem)
    else:
        c3 = '%d ` %s ` %d' % (s7, left, s6)
        cor_jaem = '㉡'
        stem= stem.format(a1=a2, a2=a1)
        answer = answer.format(cor_jaem=cor_jaem)
        comment = comment.format(a1=a2, a2=a1, c1=c2, c2=c1, c3=c3, cor_jaem=cor_jaem)

    return stem, answer, comment








































# 5-1-1-08
def naturalmixcal511_Stem_006() :
    stem = "$$수식$${box}$$/수식$$ 안에 알맞은 수를 구해 보세요.\n$$표$$$$수식$${s1} ` - ` {box} ` + ` {s2} ` = ` {s3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${s1} ` - ` {box} ` = ` $$/수식$$△라 하면\n" \
              "△$$수식$$ ` + ` {s2} ` = ` {s3}$$/수식$$, △$$수식$$ ` = ` {s3} ` - ` {s2}$$/수식$$, △$$수식$$ ` = ` {s4}$$/수식$$입니다.\n" \
              "△$$수식$$ ` = ` {s1} ` - ` {box} ` = ` {s4}$$/수식$$이므로,\n" \
              "$$수식$${box} ` + ` {s4} ` = ` {s1}$$/수식$$, $$수식$${box} ` = ` {s1} ` - ` {s4}$$/수식$$, $$수식$${box} ` = ` {cor_text}$$/수식$$입니다.\n\n"


    flag = True

    while flag :
        s1, s2 = np.random.choice(np.arange(11, 20), 2, False)
        s3 = np.random.randint(21, 30, 1)[0]
        s4 = s3 - s2
        cor_text = s1 - s4
        if cor_text > 0 :
            flag = False

    stem = stem.format(box=box, s1=s1, s2=s2, s3=s3)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, cor_text=cor_text, box=box)

    return stem, answer, comment






































# 5-1-1-09
def naturalmixcal511_Stem_007() :
    stem = "운동장에 남학생이 $$수식$${s1}$$/수식$$명, 여학생이 $$수식$${s2}$$/수식$$명 있습니다. 이 중 체육복을 입은 학생이 $$수식$${s3}$$/수식$$명이라면 체육복을 입지 않은 학생은 몇 명인가요?\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$명\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$체육복을 입지 않은 학생 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$남학생 수$$수식$$RIGHT ) ` + ` LEFT ($$/수식$$여학생 수$$수식$$RIGHT ) ` - ` LEFT ($$/수식$$체육복을 입은 학생 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {c1} LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$\n\n"


    s1 = np.random.randint(18, 22, 1)[0]
    s2 = np.random.randint(16, 20, 1)[0]
    s3 = np.random.randint(28, 32, 1)[0]

    s4 = s1 + s2
    cor_text = s1 + s2 - s3

    c1 = '%d ` + ` %d ` - ` %d ` = ` %d ` - ` %d ` = ` %d' % (s1, s2, s3, s4, s3, cor_text)

    stem = stem.format(s1=s1, s2=s2, s3=s3)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1)

    return stem, answer, comment






































# 5-1-1-11
def naturalmixcal511_Stem_008() :
    stem = "{t1}{j1}의 키는 $$수식$${s1} ` rm {{cm}}$$/수식$$이고, 아버지의 키는 $$수식$${s2} ` rm {{cm}}$$/수식$$입니다. 언니의 키는 {t1}{j1} 보다 $$수식$${s3} ` rm {{cm}}$$/수식$$ 더 클 때, 아버지와 언니의 키의 차는 몇 $$수식$$rm {{cm}}$$/수식$$인지 식을 하나로 써서 구해 보세요.\n"
    answer = "(정답)\n$$수식$${cor_exp}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$아버지의 키$$수식$$RIGHT ) ` - ` LEFT ($$/수식$$언니의 키$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {s2} ` - ` LEFT ( {s1} + {s3} RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {s2} ` - ` {s4}$$/수식$$\n" \
              "$$수식$$= ` {s5} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n\n"


    t1 = np.random.choice(person_yeo, 1)[0]
    j1 = '' if josa_check(t1[-1]) == ' ' else '이'

    s1 = np.random.randint(141, 155, 1)[0]
    s2 = np.random.randint(171, 185, 1)[0]
    s3 = np.random.randint(4, 10, 1)[0]
    s4 = s1 + s3
    s5 = s2 - s1 - s3

    cor_exp = '%d `-` LEFT ( %d `+` %d RIGHT ) `=` %d' % (s2, s1, s3, s5)

    stem = stem.format(s1=s1, s2=s2, s3=s3, t1=t1, j1=j1)
    answer = answer.format(cor_exp=cor_exp)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)

    return stem, answer, comment












































# 5-1-1-12
def naturalmixcal511_Stem_009() :
    stem = "다음 두 식의 계산 결과의 차를 구해 보세요.\n$$표$$$$수식$${a1}$$/수식$$           $$수식$${a2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${c1}$$/수식$$\n" \
              "$$수식$${c2}$$/수식$$\n" \
              "따라서 계산 결과의 차는 $$수식$${c3}$$/수식$$입니다.\n\n"


    flag = True

    while flag:
        s1 = np.random.randint(3, 10, 1)[0]
        s2 = np.random.randint(5, 8, 1)[0] * 2
        s3 = np.random.randint(2, 6, 1)[0]

        s4 = np.random.randint(16, 30, 1)[0] * 2
        s5, s6 = np.random.choice(np.arange(2, 6), 2, False)
        s7 = s1 * s2

        s8 = int(s1 * s2 / s3)
        s9 = int(s4 / s5)
        s10 = int(s4 / s5 * s6)

        if s1 != s3 and (s1 * s2) % s3 == 0 and s4 % s5 == 0 and s8 != s10 :
            flag = False

    mode = np.random.choice([0, 1], 1)[0]

    if mode == 0:
        a1 = '%d ` TIMES ` %d ` DIVIDE ` %d' % (s1, s2, s3)
        a2 = '%d ` DIVIDE ` %d ` TIMES ` %d' % (s4, s5, s6)
        c1 = '%s ` = ` %d ` DIVIDE ` %d ` = ` %d' % (a1, s7, s3, s8)
        c2 = '%s ` = ` %d ` TIMES ` %d ` = ` %d' % (a2, s9, s6, s10)


    else:
        a1 = '%d ` DIVIDE ` %d ` TIMES ` %d' % (s4, s5, s6)
        a2 = '%d ` TIMES ` %d ` DIVIDE ` %d' % (s1, s2, s3)
        c1 = '%s ` = ` %d ` TIMES ` %d ` = ` %d' % (a1, s9, s6, s10)
        c2 = '%s ` = ` %d ` DIVIDE ` %d ` = ` %d' % (a2, s7, s3, s8)

    s11, s12 = sorted([s8, s10])
    cor_text = s12 - s11
    c3 = '%d ` - ` %d ` = ` %d' % (s12, s11, cor_text)

    stem = stem.format(a1=a1, a2=a2)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1, c2=c2, c3=c3)

    return stem, answer, comment












































# 5-1-1-14
def naturalmixcal511_Stem_010() :
    stem = "계산 결과를 비교하여 가장 큰 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${a1}$$/수식$$\n㉡ $$수식$${a2}$$/수식$$\n㉢ $$수식$${a3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_jaem}\n"
    comment = "(해설)\n" \
              "㉠$$수식$${c1}$$/수식$$\n" \
              "㉡$$수식$${c2}$$/수식$$\n" \
              "㉢$$수식$${c3}$$/수식$$\n" \
              "$$수식$${c4}$$/수식$$이므로 계산 결과가 가장 큰 것은 {cor_jaem}입니다.\n\n"


    flag = True

    while flag :
        # A ÷ (B X C)
        s1 = np.random.randint(11, 100, 1)[0]
        s2, s3 = np.random.choice(np.arange(2, 6,), 2, False)
        s4 = s2 * s3
        s5 = int(s1 // s4)

        # D ÷ (E ÷ F) X G
        s6 = np.random.randint(11, 40, 1)[0]
        s7 = np.random.randint(11, 50, 1)[0]
        s8 = np.random.randint(5, 10, 1)[0]
        s9 = np.random.randint(2, 4, 1)[0]
        s10 = int(s7 // s8)
        s11 = int(s6 // s10)
        s12 = s11 * s9

        # H X I ÷ (J X K)
        s13 = np.random.randint(11, 20, 1)[0]
        s14 = np.random.randint(2, 5, 1)[0]
        s15, s16 = np.random.choice([2, 3], 2)
        s17 = s15 * s16
        s18 = s13 * s14
        s19 = int(s18 // s17)

        if s1 % s4 == 0 and s7 % s8 == 0 and s6 % s10 == 0 and s18 % s17 == 0 and s5 != s12 and s5 != s19 and s12 != s19 :
            flag = False

            a1 = '%d ` DIVIDE ` LEFT ( %d ` TIMES ` %d RIGHT )' % (s1, s2, s3)
            c1 = '%s ` = ` %d ` DIVIDE ` %d ` = ` %d' % (a1, s1, s4, s5)

            a2 = '%d ` DIVIDE ` LEFT ( %d ` DIVIDE ` %d RIGHT ) ` TIMES ` %d' % (s6, s7, s8, s9)
            c2 = '%s ` = ` %d ` DIVIDE ` %d ` TIMES ` %d ` = ` %d ` TIMES ` %d ` = ` %d' % (a2, s6, s10, s9, s11, s9, s12)

            a3 = '%d ` TIMES ` %d ` DIVIDE ` LEFT ( %d ` TIMES ` %d RIGHT )' % (s13, s14, s15, s16)
            c3 = '%s ` = ` %d ` TIMES ` %d ` DIVIDE ` %d ` = ` %d ` DIVIDE ` %d ` = ` %d' % (a3, s13, s14, s17, s18, s17, s19)

    ans_com_dict = {s5 : [a1, c1], s12 : [a2, c2], s19 : [a3, c3]}
    dict_keys = list(ans_com_dict.keys())
    np.random.shuffle(dict_keys)

    answers = []

    comments = []

    for b in dict_keys :
        answers.append(ans_com_dict.get(b)[0])
        comments.append(ans_com_dict.get(b)[1])

    a1, a2, a3 = answers
    c1, c2, c3 = comments
    n1, n2, n3 = sorted(list(dict_keys))

    cor_jaem = multiple_choice_jaem.get(dict_keys.index(max(dict_keys)))

    c4 = '%d ` %s ` %d ` %s ` %d ' % (n1, right, n2, right, n3)

    stem = stem.format(a1=a1, a2=a2, a3=a3)
    answer = answer.format(cor_jaem=cor_jaem)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, cor_jaem=cor_jaem)

    return stem, answer, comment












































# 5-1-1-15
def naturalmixcal511_Stem_011():
    stem = "바르게 계산한 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${a1}$$/수식$$\n㉡ $$수식$${a2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_jaem}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${c1}$$/수식$$\n" \
              "㉡ $$수식$${c2}$$/수식$$\n" \
              "따라서 바르게 계산한 것은 {cor_jaem}입니다.\n\n"


    mode = np.random.choice([0, 1], 1)[0]

    flag = True

    while flag:
        s1 = np.random.randint(31, 100, 1)[0]
        s2, s3 = np.random.choice(np.arange(2, 5), 2, False)
        s4 = s2 * s3
        s5 = s1 // s4
        s6 = s5 + np.random.choice([-2, -1, 1, 2], 1)[0]

        s7, s8 = np.random.choice(np.arange(3, 10), 2, False)
        s9 = np.random.randint(2, 10, 1)[0]
        s10 = s7 * s8
        s11 = s10 // s9
        s12 = s11 + np.random.choice([-2, -1, 1, 2], 1)[0]

        if s1 % s4 == 0 and s6 > 0 and s10 % s9 == 0 and s12 > 0 and s7 != s9 and s8 != s9:

            flag = False

            if mode == 1:
                a1 = '%d ` DIVIDE ` LEFT ( %d ` TIMES ` %d RIGHT ) ` = ` %d' % (s1, s2, s3, s6)
                c1 = '%d ` DIVIDE ` LEFT ( %d ` TIMES ` %d RIGHT ) ` = ` %d `DIVIDE %d ` = ` %d' % (s1, s2, s3, s1, s4, s5)
                a2 = '%d ` TIMES ` %d ` DIVIDE ` %d ` = ` %d' % (s7, s8, s9, s11)
                c2 = '%d ` TIMES ` %d ` DIVIDE ` %d ` = ` %d ` DIVIDE ` %d ` = ` %d' % (s7, s8, s9, s10, s9, s11)
                cor_text = a2
            else:
                a1 = '%d ` DIVIDE ` LEFT ( %d ` TIMES ` %d RIGHT ) ` = ` %d' % (s1, s2, s3, s5)
                c1 = '%d ` DIVIDE ` LEFT ( %d ` TIMES ` %d RIGHT ) ` = ` %d ` DIVIDE %d ` = ` %d' % (s1, s2, s3, s1, s4, s5)
                a2 = '%d ` TIMES ` %d ` DIVIDE ` %d ` = ` %d' % (s7, s8, s9, s12)
                c2 = '%d ` TIMES ` %d ` DIVIDE ` %d ` = ` %d ` DIVIDE ` %d ` = ` %d' % (s7, s8, s9, s10, s9, s11)
                cor_text = a1


    ans_com_dict = {a1 : c1, a2 : c2}
    answers = list(ans_com_dict.keys())
    np.random.shuffle(answers)

    comments = [ans_com_dict.get(b) for b in answers]
    a1, a2 = answers
    c1, c2 = comments

    cor_jaem = multiple_choice_jaem.get(answers.index(cor_text))

    stem = stem.format(a1=a1, a2=a2)
    answer = answer.format(cor_jaem=cor_jaem)
    comment = comment.format(c1=c1, c2=c2, cor_jaem=cor_jaem)

    return stem, answer, comment
















































# 5-1-1-16
def naturalmixcal511_Stem_012() :
    stem = "두 식을 $$수식$$LEFT ( ~~ RIGHT )$$/수식$$를 사용하여 하나의 식으로 나타내어 보세요.\n$$표$$$$수식$${a1}$$/수식$$,    $$수식$${a2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_exp}$$/수식$$\n"
    comment = "(해설)\n" \
              "두 식에 $$수식$${s3}$$/수식$${j1} 공통으로 들어 있으므로\n" \
              "$$수식$${a2}$$/수식$$에서 $$수식$${s3}$$/수식$$ 대신 $$수식$${c1}$$/수식$${j2} 넣습니다.\n" \
              "즉, $$수식$${cor_exp}$$/수식$$입니다.\n\n"


    s1 = np.random.randint(2, 7, 1)[0]
    s2 = np.random.randint(2, 5, 1)[0]
    s3 = s1 * s2
    a1 = '%d ` TIMES ` %d ` = ` %d' % (s1, s2, s3)

    s5 = np.random.randint(2, 5, 1)[0]
    s4 = s3 * s5
    a2 = '%d ` DIVIDE ` %d ` = ` %d' % (s4, s3, s5)
    c1 = '%d ` TIMES ` %d' % (s1, s2)


    j1 = '이' if (s3 % 10) in have_jongsung_num else '가'
    j2 = '을' if (s2 % 10) in have_jongsung_num else '를'

    mode = np.random.choice([0, 1], 1)[0]
    a1, a2 = [a2, a1] if mode == 0 else [a1, a2]

    cor_exp = '%d ` DIVIDE ` LEFT ( %d ` TIMES ` %d RIGHT ) ` = ` %d' % (s4, s1, s2, s5)

    stem = stem.format(a1=a1, a2=a2)
    answer = answer.format(cor_exp=cor_exp)
    comment = comment.format(s3=s3, j1=j1, j2=j2, c1=c1, a2=a2, cor_exp=cor_exp)

    return stem, answer, comment















































# 5-1-1-17
def naturalmixcal511_Stem_013() :
    stem = "계산 결과가 작은 것부터 차례대로 기호를 써 보세요.\n$$표$$㉠ $$수식$${a1}$$/수식$$\n㉡ $$수식$${a2}$$/수식$$\n㉢ $$수식$${a3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_text}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${c1}$$/수식$$\n" \
              "㉡ $$수식$${c2}$$/수식$$\n" \
              "㉢ $$수식$${c3}$$/수식$$\n" \
              "$$수식$${c4}$$/수식$$이므로 계산 결과가 작은 것부터 기호를 써 보면 {cor_text}입니다.\n\n"


    flag = True

    while flag:
        s1 = np.random.randint(11, 20, 1)[0]
        s2, s7, s12 = np.random.choice(np.arange(3, 6), 3, False)
        s3, s8 = np.random.choice(np.arange(2, 4), 2, False)
        s4 = s1 * s2
        s5 = s4 // s3

        s6 = np.random.randint(11, 30, 1)[0]
        s9 = s6 // s7
        s10 = s9 * s8

        s11 = np.random.randint(31, 50, 1)[0]
        s13 = np.random.randint(2, 10, 1)[0]
        s14 = s11 // s12
        s15 = s14 * s13

        if s4 % s3 == 0 and s6 % s7 == 0 and s11 % s12 == 0 and s5 != s10 and s10 != s15 and s5 != s15 :
            flag = False

    a1 = '%d ` TIMES ` %d ` DIVIDE ` %d' % (s1, s2, s3)
    c1 = '%s ` = ` %d ` DIVIDE ` %d ` = %d' % (a1, s4, s3, s5)
    a2 = '%d ` DIVIDE ` %d ` TIMES ` %d' % (s6, s7, s8)
    c2 = '%s ` = ` %d ` TIMES ` %d ` = ` %d' % (a2, s9, s8, s10)
    a3 = '%d ` DIVIDE ` %d ` TIMES ` %d' % (s11, s12, s13)
    c3 = '%s ` = ` %d ` TIMES ` %d ` = ` %d' % (a3, s14, s13, s15)

    ans_com_dict = {s5 : [a1, c1], s10 : [a2, c2], s15 : [a3, c3]}
    bogi_raw = sorted(list(ans_com_dict.keys()))
    bogi = list(set(bogi_raw))

    answers, comments = [], []

    for b in bogi:
        answers.append(ans_com_dict.get(b)[0])
        comments.append(ans_com_dict.get(b)[1])

    a1, a2, a3 = answers
    c1, c2, c3 = comments

    c4 = (' ` %s ` ' % right ).join(list(map(str, sorted([s5, s10, s15]))))
    cor_text = [multiple_choice_jaem.get(bogi.index(b)) for b in bogi_raw ]
    cor_text = ', '.join(cor_text)

    stem = stem.format(a1=a1, a2=a2, a3=a3)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, cor_text=cor_text)

    return stem, answer, comment




















































# 5-1-1-18
def naturalmixcal511_Stem_014():
    stem = "{t1}{j1}네 반은 {t2}학생이 $$수식$${s1}$$/수식$$명, {t3}학생이 $$수식$${s2}$$/수식$$명입니다. 이 중에서 안경을 쓴 학생이 $$수식$${s3}$$/수식$$명이라면 안경을 쓰지 않은 학생은 몇 명인가요?\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$명\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$안경을 쓰지 않은 학생 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$${t2}학생 수$$수식$$RIGHT ) ` + ` LEFT ($$/수식$${t3}학생 수$$수식$$RIGHT ) ` - ` LEFT ($$/수식$$안경을 쓴 학생 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {c1} LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$\n\n"


    t2, t3 = np.random.choice(['남', '여'], 2, False)
    s1 = np.random.randint(16, 20, 1)[0]
    s2 = np.random.randint(14, 18, 1)[0]
    s3 = np.random.randint(6, 15, 1)[0]
    s4 = s1 + s2
    cor_text = s4 - s3
    c1 = '%d ` + ` %d ` - ` %d ` = ` %d ` - ` %d ` = ` %d' % (s1, s2, s3, s4, s3, cor_text)

    t1 = np.random.choice(person_nam+person_yeo, 1)[0]
    j1 = '' if josa_check(t1[-1]) == ' ' else '이'

    stem = stem.format(s1=s1, s2=s2, s3=s3, t1=t1, t2=t2, t3=t3, j1=j1)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1, t2=t2, t3=t3)

    return stem, answer, comment














































# 5-1-1-19
def naturalmixcal511_Stem_015():
    stem = "{t1}{j1}네 반 $$수식$${s1}$$/수식$$명의 학생들은 $$수식$${s2}$$/수식$$명씩 한 모둠을 만들어 하천 주변에서 쓰레기 줍기를 하였습니다. 한 모둠 당 쓰레기봉투를 $$수식$${s3}$$/수식$$개씩 받았다면 나누어 준 쓰레기봉투는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$나누어 준 쓰레기봉투 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$학생 수$$수식$$RIGHT ) ` DIVIDE ` LEFT ($$/수식$$한 모둠의 학생 수$$수식$$RIGHT ) ` TIMES ` LEFT ($$/수식$$한 모둠 당 받은 쓰레기봉투 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$=` {c1} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"


    flag = True

    while flag:
        s1 = np.random.randint(26, 40, 1)[0]
        s2, s3 = np.random.choice(np.arange(2, 5), 2, False)
        s4 = s1 // s2
        cor_text = s4 * s3
        if s1 % s2 == 0:
            flag = False

    c1 = '%d `DIVIDE` %d `TIMES` %d `=` %d `TIMES` %d `=` %d' % (s1, s2, s3, s4, s3, cor_text)
    t1 = np.random.choice(person_nam+person_yeo, 1)[0]
    j1 = '' if josa_check(t1[-1]) == ' ' else '이'

    stem = stem.format(t1=t1, j1=j1, s1=s1, s2=s2, s3=s3)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1)

    return stem, answer, comment



















































# 5-1-1-20
def naturalmixcal511_Stem_016():
    stem = "한 사람이 한 시간에 {t1}{j1} $$수식$${s1}$$/수식$$개씩 만들 수 있습니다. $$수식$${s2}$$/수식$$명이 {t1} $$수식$${s3}$$/수식$$개를 만들려면 몇 시간이 걸리는지 식을 하나로 써서 구해보세요.\n"
    answer = "(정답)\n$$수식$${cor_exp}$$/수식$$시간\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$걸리는 시간$$수식$$RIGHT ) ` = ` {c1}$$/수식$$\n" \
              "$$수식$$= ` {cor_text} LEFT ($$/수식$$시간$$수식$$RIGHT )$$/수식$$\n\n"


    flag = True

    while flag:
        t1 = np.random.choice(['종이학', '종이배'])
        j1 = '를' if josa_check(t1[-1]) == ' ' else '을'

        s1 = np.random.randint(6, 10, 1)[0]
        s2 = np.random.randint(4, 8, 1)[0]
        s3 = np.random.randint(61, 100, 1)[0]
        s4 = s1 * s2
        cor_text = s3 // s4

        if s3 % s4 == 0:
            flag = False

    c1 = '%d ` DIVIDE ` LEFT ( %d ` TIMES ` %d RIGHT ) ` = ` %d ` DIVIDE ` %d' % (s3, s1, s2, s3, s4)
    cor_exp = '%d ` DIVIDE ` LEFT ( %d ` TIMES ` %d RIGHT ) ` = ` %d' % (s3, s1, s2, cor_text)

    stem = stem.format(t1=t1, j1=j1, s1=s1, s2=s2, s3=s3)
    answer = answer.format(cor_exp=cor_exp)
    comment = comment.format(c1=c1, cor_text=cor_text)

    return stem, answer, comment












































# 5-1-1-21
def naturalmixcal511_Stem_017():
    stem = "$$수식$${box}$$/수식$$ 안에 들어갈 수 있는 가장 작은 자연수는 얼마인가요?\n$$표$$$$수식$${a1}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${c1}$$/수식$$\n" \
              "→ $$수식$${c2}$$/수식$$\n" \
              "따라서 $$수식$${box}$$/수식$$ 안에 들어갈 수 있는 가장 작은 자연수는 $$수식$${cor_text}$$/수식$$입니다.\n\n"


    flag = True

    while flag :
        s1 = np.random.randint(11, 30, 1)[0]
        s2 = np.random.randint(11, 60, 1)[0]
        s3 = np.random.randint(2, 9, 1)[0]
        s4 = np.random.randint(2, 5, 1)[0]
        s5 = s2 // s3
        s6 = s1 // s5
        s7 = s6 * s4
        cor_text = s7 + 1
        if s2 % s3 == 0 and s1 % s5 == 0 :
            flag = False

    a1 = '%d ` DIVIDE ` LEFT ( %d ` DIVIDE ` %d RIGHT ) ` TIMES ` %d ` %s ` %s' % (s1, s2, s3, s4, right, box)
    c1 = '%d ` DIVIDE ` LEFT ( %d ` DIVIDE ` %d RIGHT ) ` TIMES ` %d ` = ` %d ` DIVIDE ` %d ` TIMES ` %d ` = ` %d ` TIMES ` %d ` = ` %d' \
         '' % (s1, s2, s3, s4, s1, s5, s4, s6, s4, s7)

    c2 = '%d ` %s ` %s' % (s7, right, box)

    stem = stem.format(box=box, a1=a1)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1, c2=c2, box=box, cor_text=cor_text)

    return stem, answer, comment



















































# 5-1-1-23
def naturalmixcal511_Stem_018():
    stem = "두 식의 계산 결과의 합은 얼마인가요?\n$$표$$$$수식$${a1}$$/수식$$\n$$수식$${a2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${c1}$$/수식$$\n" \
              "$$수식$${c2}$$/수식$$\n" \
              "따라서 두 식의 계산 결과의 합은 " \
              "$$수식$${c3}$$/수식$$입니다.\n\n"


    s1 = np.random.randint(11, 20, 1)[0]
    s2, s3 = np.random.choice(np.arange(2, 5), 2, False)
    s4 = np.random.randint(2, 10, 1)[0]
    s5 = s2 * s3
    s6 = s1 + s5
    s7 = s6 - s4

    a1 = '%d ` + ` %d ` TIMES ` %d ` - ` %d' % (s1, s2, s3, s4)
    c1 = '%s ` = ` %d ` + ` %d ` - ` %d `  = ` %d ` - ` %d ` = ` %d' % (a1, s1, s5, s4, s6, s4, s7)

    s8 = np.random.randint(31, 60, 1)[0]
    s9 = np.random.randint(11, 30, 1)[0]
    s10 = np.random.randint(2, 5, 1)[0]
    s11 = np.random.randint(2, 10, 1)[0]
    s12 = s10 * s11
    s13 = s8 - s9
    s14 = s13 + s12

    a2 = '%d ` - ` %d ` + ` %d ` TIMES ` %d' % (s8, s9, s10, s11)
    c2 = '%s ` = ` %d ` - ` %d ` + ` %d ` = ` %d ` + ` %d ` = ` %d' % (a2, s8, s9, s12, s13, s12, s14)

    ans_com_dict = {s7 : [a1, c1], s14 : [a2, c2]}

    bogi = [s7, s14]
    np.random.shuffle(bogi)

    answers, comments = [], []
    for b in bogi :
        answers.append(ans_com_dict.get(b)[0])
        comments.append(ans_com_dict.get(b)[1])

    a1, a2 = answers
    c1, c2 = comments
    cor_text = s7 + s14

    c3 = '%d ` + ` %d ` = ` %d' % (bogi[0], bogi[1], cor_text)
    stem = stem.format(a1=a1, a2=a2)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1, c2=c2, c3=c3)

    return stem, answer, comment














































# 5-1-1-24
def naturalmixcal511_Stem_019():
    stem = "$$수식$${exp}$$/수식$$의 계산에 대한 설명으로 옳은 것을 모두 고르세요.\n① {a1}\n② {a2}\n③ {a3}\n④ {a4}\n⑤ {a5}\n"
    answer = "(정답)\n{cor_nums}\n"
    comment = "(해설)\n" \
              "$$수식$${exp_com}$$/수식$$\n" \
              "{c1}\n" \
              "따라서 설명으로 옳은 것은 {cor_nums}입니다.\n\n"


    flag = True

    while flag:
        s1 = np.random.randint(11, 20, 1)[0]
        s2 = np.random.randint(21, 30, 1)[0]
        s3 = np.random.randint(2, 5, 1)[0]
        s4 = np.random.randint(4, 8, 1)[0]
        s5 = s3 * s4
        s6 = s1 + s2
        s7 = s6 - s5
        s8 = (s1 + s2 - s3) * s4
        if s7 != s8:
            flag = False

    exp = '%d ` + ` %d ` - ` %d ` TIMES ` %d' % (s1, s2, s3, s4)
    exp_com = '%s ` = ` %d ` + ` %d ` - ` %d ` = ` %d ` - ` %d ` = ` %d' % (exp, s1, s2, s5, s6, s5, s7)
    j1 = '을' if s4 in have_jongsung_num else '를'

    a1 = '$$수식$$%d ` TIMES ` %d$$/수식$$%s 가장 먼저 계산합니다.' % (s3, s4, j1)
    a2 = '$$수식$$LEFT ( %d ` + ` %d RIGHT ) ` - ` %d ` TIMES ` %d$$/수식$$과 계산 결과가 같습니다.' % (s1, s2, s3, s4)
    a3 = '계산 결과는 $$수식$$%d$$/수식$$입니다.' % (s7)
    a4 = '계산 결과는 $$수식$$%d$$/수식$$입니다.' % (s8)
    a5 = '앞에서부터 차례대로 계산합니다.'

    c1 = a1
    c2 = '$$수식$$LEFT ( %d ` + ` %d RIGHT ) ` - ` %d ` TIMES ` %d ` = ` %d ` - ` %d ` = ` %d$$/수식$$' % (s1, s2, s3, s4, s6, s5, s7)
    c3 = a3

    ans_com_dict = {0 : [a1, c1], 1 : [a2, c2], 2 : [a3, c3], 3 : [a4, ''], 4 : [a5, '']}
    key_idx = np.random.choice([0, 1, 2, 3, 4], 5, False)
    answers, comments, cor_nums = [], [], []

    for i, k in enumerate(key_idx):
        ans, com = ans_com_dict.get(k)
        answers.append(ans)

        if com != '':
            cor_nums.append(multiple_choice_nums.get(i))
            comments.append('%s %s' % (multiple_choice_nums.get(i), com))

    a1, a2, a3, a4, a5 = answers
    c1 = '\n'.join(comments)
    cor_nums = ', '.join(cor_nums)

    stem = stem.format(exp=exp, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(cor_nums=cor_nums)
    comment = comment.format(exp_com=exp_com, c1=c1, cor_nums=cor_nums)

    return stem, answer, comment













































# 5-1-1-25
def naturalmixcal511_Stem_020():
    stem = "하나의 식으로 나타내고 답을 구해 보세요.\n$$표$$$$수식$${s1}$$/수식$$에 $$수식$${s2}$$/수식$${j1} $$수식$${s3}$$/수식$$의 차를 $$수식$${s4}$$/수식$$로 나눈 값을 더한 수$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_exp}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${c1}$$/수식$$\n\n"


    flag = True

    while flag:
        s1 = np.random.randint(2, 20, 1)[0]
        s2 = np.random.randint(31, 50, 1)[0]
        s3 = np.random.randint(11, 30, 1)[0]
        s4 = np.random.randint(2, 8, 1)[0]

        if (s2 - s3) % s4 == 0:
            flag = False

    s5 = s2 - s3
    s6 = s5 // s4
    s7 = s1 + s6

    c1 = '%d ` + ` LEFT ( %d ` - ` %d RIGHT ) ` DIVIDE ` %d ` = ` %d ` + ` %d ` DIVIDE ` %d ` = ` %d ` + ` %d ` = ` %d' \
         '' % (s1, s2, s3, s4, s1, s5, s4, s1, s6, s7)

    cor_exp = '%d ` + ` LEFT ( %d ` - ` %d RIGHT ) ` DIVIDE ` %d ` = ` %d' % (s1, s2, s3, s4, s7)

    j1 = '과' if (s2 % 10) in have_jongsung_num else '와'

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, j1=j1)
    answer = answer.format(cor_exp=cor_exp)
    comment = comment.format(c1=c1)

    return stem, answer, comment








































# 5-1-1-26
def naturalmixcal511_Stem_021():
    """

    :param r1: n1 자연수 최솟값 [int] {10:10}
    :param r2: n1 자연수 최댓값 [int] {20:20}
    :param r3: n2 자연수 최솟값 [int] {1:1}
    :param r4: n2 자연수 최댓값 [int] {10:10}
    :param r5: n3 자연수 최솟값 [int] {5:5}
    :param r6: n3 자연수 최댓값 [int] {10:10}
    :param r7: n4 자연수 최솟값 [int] {1:1}
    :param r8: n5 자연수 최댓값 [int] {5:5}
    :return:
    """
    stem = "$$수식$$LEFT ( ~~ RIGHT )$$/수식$$가 없어도 계산 결과가 같은 식을 찾아 기호를 써보세요.\n$$표$$㉠ $$수식$${d1}$$/수식$$\n㉡ $$수식$${d2}$$/수식$$\n㉢ $$수식$${d3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "덧셈, 뺄셈, 곱셈이 섞여 있는 식은 $$수식$$LEFT ( ~~ RIGHT )$$/수식$$가 없어도 곱셈을 먼저 계산해야 합니다.\n" \
              "따라서 $$수식$$LEFT ( ~~ RIGHT )$$/수식$$가 없어도 계산 결과가 같은 것은 {ans}입니다.\n\n"


    r1 = 10
    r2 = 20
    r3 = 1
    r4 = 10
    r5 = 5
    r6 = 10
    r7 = 1
    r8 = 5


    while True:
        n1 = random.randint(r1, r2)
        n2 = random.randint(r3, r4)
        n3 = random.randint(r5, r6)
        n4 = random.randint(r7, r8)

        v1 = (n1 + n2) * n3 - n4
        v2 = n1 + (n2 * n3) - n4
        v3 = n1 + n2 * (n3 - n4)
        if len(set([n1, n2, n3, n4])) == 4 and len(set([v1, v2, v3])) == 3:
            break

    t1 = "LEFT ( %d ` + ` %d RIGHT ) ` TIMES ` %d ` - ` %d" % (n1, n2, n3, n4)
    t2 = "%d ` + ` LEFT ( %d ` TIMES ` %d RIGHT ) ` - ` %d" % (n1, n2, n3, n4)
    t3 = "%d ` + ` %d ` TIMES ` LEFT ( %d ` - ` %d RIGHT )" % (n1, n2, n3, n4)

    answers = [t1, t2, t3]
    random.shuffle(answers)
    d1, d2, d3 = answers

    ans = multiple_choice_nums_2[answers.index(t2)]

    stem = stem.format(d1=d1, d2=d2, d3=d3)
    answer = answer.format(ans=ans)
    comment = comment.format(ans=ans)

    return stem, answer, comment


































# 5-1-1-27
def naturalmixcal511_Stem_022():
    stem = "계산 결과를 비교하여 $$수식$${box}$$/수식$$ 안에 $$수식$${left}$$/수식$$, $$수식$$=$$/수식$$, $$수식$${right}$$/수식$$를 알맞게 써넣으세요.\n$$수식$${a1} ~~ {box} ~~ {a2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${cor_eq}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${c1}$$/수식$$,\n" \
              "$$수식$${c2}$$/수식$$\n" \
              "$$수식$${c3}$$/수식$$이므로\n" \
              "$$수식$${c4}$$/수식$$입니다.\n\n"


    flag = True

    while flag:
        s1 = np.random.randint(10, 25, 1)[0]
        s2 = np.random.randint(2, 8, 1)[0]
        s3 = np.random.randint(2, 8, 1)[0]
        s4 = np.random.randint(11, 20, 1)[0]

        s5, s6 = np.random.choice(np.arange(3, 10), 2, False)
        s7 = np.random.randint(2, 6, 1)[0]
        s8 = np.random.randint(11, 30, 1)[0]

        s9 = s2 * s3
        s10 = s1 + s9
        s11 = s5 + s6
        s12 = s11 * s7

        s13 = s10 - s4
        s14 = s12 - s8

        if len(set([s1, s2, s3, s4])) == 4 and len(set([s5, s6, s7, s8])) == 4 and s2 * s3 < 30 and s13 > 0 and s14 > 0 and abs(s13-s14) < 10 :
            flag = False

    a1 = '%d ` + ` %d ` TIMES ` %d ` - ` %d' % (s1, s2, s3, s4)
    a2 = 'LEFT ( %d ` + ` %d RIGHT ) ` TIMES ` %d ` - ` %d' % (s5, s6, s7, s8)

    c1 = '%s ` = ` %d ` + ` %d ` - ` %d ` = ` %d ` - ` %d ` = ` %d' % (a1, s1, s9, s4, s10, s4, s13)
    c2 = '%s ` = ` %d ` TIMES ` %d ` - ` %d ` = ` %d ` - ` %d ` = ` %d' % (a2, s11, s7, s8, s12, s8, s14)

    cor_eq = right if s13 < s14 else left if s13 > s14 else '='
    c3 = '%d ` %s ` %d' % (s13, cor_eq, s14)
    c4 = '%s ` %s ` %s' % (a1, cor_eq, a2)

    stem = stem.format(box=box, left=left, right=right, a1=a1, a2=a2)
    answer = answer.format(cor_eq=cor_eq)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4)

    return stem, answer, comment






























# 5-1-1-29
def naturalmixcal511_Stem_023():
    """

    :param r1: 과일 개수의 최솟값 [int] {30:30}
    :param r2: 과일 개수의 최댓값 [int] {40:40}
    :param r3: 학생 수의 최솟값 [int] {2:2}
    :param r4: 학생 수의 최댓값 [int] {6:6}
    :param r5: 학생들이 먹은 개수 최솟값 [int] {2:2}
    :param r6: 학생들이 먹은 개수 최댓값 [int] {4:4}
    :return:
    """
    stem = "문제에 알맞은 식은 어느 것인가요?\n$$표$${s1}{j1} $$수식$${n1}$$/수식$$개 있습니다. 남학생 $$수식$${n2}$$/수식$$명과 여학생 $$수식$${n3}$$/수식$$명이 각각 $$수식$${n4}$$/수식$$개씩 먹었습니다. 남은 {s1}{j2} 몇 개인지 하나의 식으로 나타내어 구해 보세요.$$/표$$\n① $$수식$${a1}$$/수식$$\n② $$수식$${a2}$$/수식$$\n③ $$수식$${a3}$$/수식$$\n④ $$수식$${a4}$$/수식$$\n⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$전체 {s1}의 수$$수식$$RIGHT ) ` - ` LEFT ($$/수식$$남학생과 여학생이 먹은 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {c1}$$/수식$$\n" \
              "따라서 문제에 알맞은 식은 {ans}입니다.\n\n"


    r1 = 30
    r2 = 40
    r3 = 2
    r4 = 6
    r5 = 2
    r6 = 4


    fruits = ['사과', '망고', '바나나', '토마토', '배', '자두', '귤']

    s1 = random.choice(fruits)
    j1 = '가' if josa_check(s1[-1]) == ' ' else '이'
    j2 = '는' if josa_check(s1[-1]) == ' ' else '은'

    while True:
        n1 = random.randint(r1, r2)
        n2, n3 = random.sample(range(r3, r4), 2)
        n4 = random.randint(r5, r6)

        if n1 > (n2 + n3) * n4:
            break

    t1 = "%d ` - ` %d ` + ` %d ` TIMES ` %d" % (n1, n2, n3, n4)
    t2 = "LEFT ( %d ` - ` %d RIGHT ) ` + ` %d ` TIMES ` %d" % (n1, n2, n3, n4)
    t3 = "%d ` - ` LEFT ( %d ` + ` %d RIGHT ) ` TIMES ` %d" % (n1, n2, n3, n4)
    t4 = "LEFT ( %d ` - ` %d ` + ` %d RIGHT ) ` TIMES ` %d" % (n1, n2, n3, n4)
    t5 = "%d ` - ` LEFT ( %d ` + ` %d ` TIMES ` %d RIGHT )" % (n1, n2, n3, n4)

    answers = [t1, t2, t3, t4, t5]
    random.shuffle(answers)
    a1, a2, a3, a4, a5 = answers

    ans = multiple_choice_nums[answers.index(t3)]
    c1 = t3

    stem = stem.format(s1=s1, j1=j1, j2=j2, n1=n1, n2=n2, n3=n3, n4=n4, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(ans=ans)
    comment = comment.format(s1=s1, c1=c1, ans=ans)

    return stem, answer, comment










































# 5-1-1-30
def naturalmixcal511_Stem_024():
    """
    :param r1: 첫 번째 자연수 범위 최솟값 [int] {30:30}
    :param r2: 첫 번째 자연수 범위 최댓값 [int] {40:40}
    :param r3: 두 번째 자연수 범위 최솟값 [int] {16:16}
    :param r4: 두 번째 자연수 범위 최댓값 [int] {24:24}
    :param r5: 세 번째 자연수 범위 최솟값 [int] {2:2}
    :param r6: 세 번째 자연수 범위 최댓값 [int] {4:4}
    :param r7: 네 번째 자연수 범위 최솟값 [int] {11:11}
    :param r8: 네 번째 자연수 범위 최댓값 [int] {29:29}
    :return:
    """
    stem = "식을 세우고 계산해 보세요.\n$$표$$$$수식$${n1}$$/수식$${j1} $$수식$${n2}$$/수식$$의 차에 $$수식$${n3}$$/수식$${j2} 곱하고 $$수식$${n4}$$/수식$${j3} 더한 수$$/표$$\n"
    answer = "(정답)\n$$수식$${ans1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${n1}$$/수식$${j1} $$수식$${n2}$$/수식$$의 차에 $$수식$${n3}$$/수식$${j2} 곱해야 하므로 $$수식$$LEFT ( ~~ RIGHT )$$/수식$$를 사용하여 식을 세웁니다.\n" \
              "따라서 $$수식$${c1} ` = ` {c2}$$/수식$$\n" \
              "$$수식$$= ` {c3} ` = ` {c4}$$/수식$$입니다.\n\n"


    r1 = 30
    r2 = 40
    r3 = 16
    r4 = 24
    r5 = 2
    r6 = 4
    r7 = 11
    r8 = 29


    n1 = random.randint(r1, r2)
    n2 = random.randint(r3, r4)
    n3 = random.randint(r5, r6)
    n4 = random.randint(r7, r8)

    j1 = check_jongsung(n1)[0]
    j2 = check_jongsung(n3)[2]
    j3 = check_jongsung(n4)[2]

    b1 = '①'
    b2 = '②'

    c1 = "LEFT ( %d ` - ` %d RIGHT ) ` TIMES ` %d ` + ` %d" % (n1, n2, n3, n4)
    c2 = "%d TIMES %d ` + ` %d" % (n1 - n2, n3, n4)
    c3 = "%d ` + ` %d" % ((n1 - n2) * n3, n4)
    c4 = (n1 - n2) * n3 + n4

    ans1 = c1 + " ` = ` " + str(c4)
    ans2 = c4

    stem = stem.format(n1=n1, n2=n2, n3=n3, n4=n4, j1=j1, j2=j2, j3=j3, b1=b1, b2=b2)
    answer = answer.format(ans1=ans1, ans2=ans2)
    comment = comment.format(n1=n1, n2=n2, n3=n3, j1=j1, j2=j2, c1=c1, c2=c2, c3=c3, c4=c4)

    return stem, answer, comment

































# 5-1-1-31
def naturalmixcal511_Stem_025():
    """

    :param r1: 좌항 자연수 범위 최솟값 [int] {11:11}
    :param r2: 좌항 자연수 범위 최댓값 [int] {15:15}
    :param r3: 우항 자연수 범위 최솟값 [int] {2:2}
    :param r4: 우항 자연수 범위 최댓값 [int] {6:6}
    :return:
    """
    stem = "기호 {g1}에 대하여 ㉠ {g1} ㉡ $$수식$$` = `$$/수식$$ ㉠ $$수식$$` - `$$/수식$$ ㉡ $$수식$$` + `$$/수식$$ ㉠ $$수식$$` TIMES `$$/수식$$ ㉡일 때, {n1} {g1} {n2}{j1} 구해 보세요.\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ {g1} ㉡ $$수식$$` = `$$/수식$$ ㉠ $$수식$$` - `$$/수식$$ ㉡ $$수식$$` + `$$/수식$$ ㉠ $$수식$$` TIMES `$$/수식$$ ㉡이므로\n" \
              "$$수식$${n1}$$/수식$$ {g1} $$수식$${n2} ` = ` {c1} ` = ` {c2}$$/수식$$\n" \
              "$$수식$$= ` {c3} ` = ` {ans}$$/수식$$입니다.\n\n"


    r1 = 11
    r2 = 15
    r3 = 2
    r4 = 6


    g_s = ['◆', '○', '■', '▲']

    n1 = random.randint(r1, r2)
    n2 = random.randint(r3, r4)

    g1 = random.choice(g_s)

    c1 = "%d ` - ` %d ` + ` %d ` TIMES ` %d" % (n1, n2, n1, n2)
    c2 = "%d ` - ` %d ` + ` %d" % (n1, n2, n1 * n2)
    c3 = "%d ` + ` %d" % (n1 - n2, n1 * n2)
    ans = (n1 - n2) + (n1 * n2)

    j1 = '을' if (n2 % 10) in have_jongsung_num else '를'

    stem = stem.format(g1=g1, n1=n1, n2=n2, j1=j1)
    answer = answer.format(ans=ans)
    comment = comment.format(g1=g1, n1=n1, n2=n2, c1=c1, c2=c2, c3=c3, ans=ans)

    return stem, answer, comment










































# 5-1-1-33
def naturalmixcal511_Stem_026():
    """
    :param r1: 기간 최솟값 [int] {10:10}
    :param r2: 기간 최댓값 [int] {15:15}
    :return:
    """
    stem = "대화를 읽고 {name1}{j1} {name2}{j2} $$수식$${n1}$$/수식$$일 동안 {s1}{j3} 모두 몇 번 했는지 식을 하나로 써서 구해 보세요.\n$$표$${name1}: 난 $$수식$${n1}$$/수식$$일 동안 {s1}{j3} $$수식$${n2}$$/수식$$번씩 했어.\n{name2}: 난 $$수식$${n1}$$/수식$$일 중 $$수식$${n3}$$/수식$$일은 쉬고 나머지 날은 매일 {s1}{j3} $$수식$${n4}$$/수식$$번씩 했어.$$/표$$\n"
    answer = "(정답)\n$$수식$${ans1}$$/수식$$(번)\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${name1}{j1} {name2}{j2} $$수식$${n1}$$/수식$$일 동안 한 {s1} 횟수의 합$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {c1}$$/수식$$\n" \
              "$$수식$$= ` {c2}$$/수식$$\n" \
              "$$수식$$= ` {c3}$$/수식$$\n" \
              "$$수식$$= ` {c4} LEFT ($$/수식$$번$$수식$$RIGHT )$$/수식$$\n\n"


    r1 = 10
    r2 = 15


    exercises = ['윗몸일으키기', '줄넘기', '턱걸이', '팔굽혀펴기']


    n1 = random.randint(r1, r2)
    n2 = random.choice([20, 30])
    n3 = random.randint(2, 4)
    n4 = n2 + 10

    b1 = 'box{~~①~~}'
    b2 = 'box{~②~}'

    name1, name2 = random.sample(person_nam + person_yeo, 2)
    s1 = random.choice(exercises)

    if josa_check(name1[-1]) == ' ':
        j1 = '와'
    else:
        j1 = '이와'

    if josa_check(name2[-1]) == ' ':
        j2 = '가'
    else:
        j2 = '이가'

    if josa_check(s1[-1]) == ' ':
        j3 = '를'
    else:
        j3 = '을'

    c1 = "%d ` TIMES ` %d ` + ` LEFT ( %d ` - ` %d RIGHT ) ` TIMES ` %d" % (n1, n2, n1, n3, n4)
    c2 = "%d ` TIMES ` %d ` + ` %d ` TIMES ` %d" % (n1, n2, n1 - n3, n4)
    c3 = "%d ` + ` %d" % (n1 * n2, (n1 - n3) * n4)
    c4 = (n1 * n2) + ((n1 - n3) * n4)

    ans1 = c1 + ' ` = ` ' + str(c4)
    ans2 = c4

    stem = stem.format(name1=name1, name2=name2, s1=s1, j1=j1, j2=j2, j3=j3, n1=n1, n2=n2, n3=n3, n4=n4, b1=b1, b2=b2)
    answer = answer.format(ans1=ans1, ans2=ans2)
    comment = comment.format(name1=name1, name2=name2, s1=s1, j1=j1, j2=j2, j3=j3, n1=n1, c1=c1, c2=c2, c3=c3, c4=c4)


    return stem, answer, comment












































# 5-1-1-34
def naturalmixcal511_Stem_027():
    """

    :param r1: 첫 번째 자연수 범위 최솟값 [int] {2:2}
    :param r2: 첫 번째 자연수 범위 최댓값 [int] {5:5}
    :param r3: 두 번째 자연수 범위 최솟값 [int] {11:11}
    :param r4: 두 번째 자연수 범위 최댓값 [int] {19:19}
    :param r5: 세 번째 자연수 범위 최솟값 [int] {2:2}
    :param r6: 세 번째 자연수 범위 최댓값 [int] {4:4}
    :param r7: 네 번째 자연수 범위 최솟값 [int] {2:2}
    :param r8: 네 번째 자연수 범위 최댓값 [int] {9:9}
    :return:
    """
    stem = "$$수식$${b1}$$/수식$$ 안에 알맞은 수를 구해 보세요.\n$$표$$$$수식$${b1} ` TIMES ` {n1} ` - ` LEFT ( {n2} ` + ` {n3} RIGHT ) ` = ` {n4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${c1}$$/수식$$에서\n" \
              "$$수식$${c2}$$/수식$$, $$수식$${c3}$$/수식$$,\n" \
              "$$수식$${c4}$$/수식$$, $$수식$${c5}$$/수식$$, $$수식$${c6}$$/수식$$입니다.\n\n"


    r1 = 2
    r2 = 5
    r3 = 11
    r4 = 19
    r5 = 2
    r6 = 4
    r7 = 2
    r8 = 9


    while True:
        n1 = random.randint(r1, r2)
        n2 = random.randint(r3, r4)
        n3 = random.randint(r5, r6)
        n4 = random.randint(r7, r8)

        if (n2 + n3 + n4) % n1 == 0:
            break

    b1 = '□'

    c1 = '%s ` TIMES ` %d ` - ` LEFT ( %d ` + ` %d RIGHT ) ` = ` %d' % (b1, n1, n2, n3, n4)
    c2 = "%s ` TIMES ` %d ` - ` %d ` = ` %d" % (b1, n1, n2 + n3, n4)
    c3 = "%s ` TIMES ` %d ` = ` %d ` + ` %d" % (b1, n1, n4, n2 + n3)
    c4 = "%s ` TIMES ` %d ` = ` %d" % (b1, n1, n2 + n3 + n4)
    c5 = "%s ` = ` %d ` DIV ` %d" % (b1, n2 + n3 + n4, n1)
    c6 = "%s ` = ` %d" % (b1, (n2 + n3 + n4) // n1)
    ans = (n2 + n3 + n4) // n1

    stem = stem.format(b1=b1, n1=n1, n2=n2, n3=n3, n4=n4)
    answer =answer.format(ans=ans)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)

    return stem, answer, comment







































# 5-1-1-35
def naturalmixcal511_Stem_028():
    stem = "계산 결과가 $$수식$${ans_num}$$/수식$$인 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${a1}$$/수식$$\n㉡ $$수식$${a2}$$/수식$$\n㉢ $$수식$${a3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_jaem}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${c1}$$/수식$$\n$$수식$$= ` {c2}$$/수식$$\n" \
              "㉡ $$수식$${c3}$$/수식$$\n$$수식$$= ` {c4}$$/수식$$\n" \
              "㉢ $$수식$${c5}$$/수식$$\n$$수식$$= ` {c6}$$/수식$$\n" \
              "따라서 계산 결과가 $$수식$${ans_num}$$/수식$$인 것은 {cor_jaem}입니다.\n\n"


    flag = True

    while flag:
        s1, s2 = np.random.choice(np.arange(11, 40), 2, False)
        s3 = np.random.randint(11, 40, 1)[0]
        s4 = np.random.choice(get_divisors(s3), 1)[0]

        s5 = np.random.randint(31, 50, 1)[0]
        s6 = np.random.randint(21, 40, 1)[0]
        s7 = np.random.choice(get_divisors(s6), 1)[0]
        s8 = np.random.randint(11, 30, 1)[0]

        s9 = np.random.randint(41, 80, 1)[0]
        s10 = np.random.choice(get_divisors(s9), 1)[0]
        s11 = np.random.randint(21, 30, 1)[0]
        s12 = np.random.randint(41, 80, 1)[0]
        s13 = np.random.choice(get_divisors(s12), 1)[0]

        if 1 < s4 < 10 and 1 < s7 < 10 and 1 < s10 < 10 and 1 < s13 < 13 :
            # 14a 15b 16c 17d 18e 19f 20g 21h 22i 23j 24k 25l 26m 27n
            s14 = s3 // s4
            s15 = s1 + s2
            s16 = s6 // s7
            s17 = s5 - s16
            s18 = s9 // s10
            s19 = s12 // s13
            s20 = s18 + s11

            v1 = s15 - s14
            v2 = s17 + s8
            v3 = s20 - s19

            if s16 > 0 and len(set([v1, v2, v3])) == 3 and min(v1, v2, v3) > 0 :
                flag = False

    a1 = '%d ` + ` %d ` - ` %d ` DIVIDE ` %d' % (s1, s2, s3, s4)
    c1 = '%s ` = ` %d ` + ` %d - %d' % (a1, s1, s2, s14)
    c2 = '%d ` - ` %d ` = ` %d' % (s15, s14, v1)

    a2 = '%d ` - ` %d ` DIVIDE ` %d ` + ` %d' % (s5, s6, s7, s8)
    c3 = '%s ` = ` %d ` - ` %d ` + ` %d' % (a2, s5, s16, s8)
    c4 = '%d ` + ` %d ` = ` %d' % (s17, s8, v2)

    a3 = '%d ` DIVIDE ` %d ` + ` %d ` - ` %d ` DIVIDE ` %d' % (s9, s10, s11, s12, s13)
    c5 = '%s ` = ` %d ` + ` %d ` - ` %d' % (a3, s18, s11, s19)
    c6 = '%d ` - ` %d ` = ` %d' % (s20, s19, v3)

    ans_num = np.random.choice([v1, v2, v3], 1)[0]
    cor_jaem = '㉠' if ans_num == v1 else '㉡' if ans_num == v2 else '㉢'

    stem = stem.format(a1=a1, a2=a2, a3=a3, ans_num=ans_num)
    answer = answer.format(cor_jaem=cor_jaem)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, ans_num=ans_num, cor_jaem=cor_jaem)

    return stem, answer, comment













































# 5-1-1-36
def naturalmixcal511_Stem_029():
    stem = "두 식의 계산 결과의 차를 구해 보세요.\n$$표$$∙ $$수식$${a1}$$/수식$$\n∙ $$수식$${a2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "∙ $$수식$${c1}$$/수식$$\n" \
              "∙ $$수식$${c2}$$/수식$$\n" \
              "에서 $$수식$${c3}$$/수식$$이므로 계산 결과의 차를 구해 보면\n" \
              "$$수식$${c4}$$/수식$$입니다.\n\n"


    flag = True

    while flag:
        s3 = np.random.randint(2, 8, 1)[0]
        s1, s2 = [s3, s3] * np.reshape(np.random.choice(np.arange(2, 5), 2, False), -1)
        s4 = np.random.randint(2, 5, 1)[0]
        if 10 < s1 < 40 and 10 < s2 < 49 :
            s5 = s1 + s2
            s6 = s5 // s3
            s7 = s2 // s3
            s8 = s1 + s7
            v1 = s6 - s4
            v2 = s8 - s4
            if v1 > 0 and v2 > 0 and v1 != v2 and s6 != s3 and s8 != s3 :
                flag = False

    mode = np.random.choice([0, 1], 1)[0]

    if mode == 0:
        a1 = 'LEFT ( %d ` + ` %d RIGHT ) ` DIVIDE ` %d ` - ` %d' % (s1, s2, s3, s4)
        c1 = '%s ` = ` %d ` DIVIDE ` %d ` - ` %d ` = ` %d ` - ` %d ` = ` %d' % (a1, s5, s3, s4, s6, s4, v1)
        a2 = '%d ` + ` %d ` DIVIDE ` %d ` - ` %d' % (s1, s2, s3, s4)
        c2 = '%s ` = ` %d ` + ` %d ` - ` %d ` = ` %d ` - ` %d ` = ` %d' % (a2, s1, s7, s4, s8, s4, v2)

        eq = right if v1 < v2 else left
        c3 = '%d ` %s ` %d' % (v1, eq, v2)

    else:
        a1 = '%d ` + ` %d ` DIVIDE ` %d ` - ` %d' % (s1, s2, s3, s4)
        c1 = '%s ` = ` %d ` + ` %d ` - ` %d ` = ` %d ` - ` %d ` = ` %d' % (a1, s1, s7, s4, s8, s4, v2)
        a2 = 'LEFT ( %d ` + ` %d RIGHT ) ` DIVIDE ` %d ` - ` %d' % (s1, s2, s3, s4)
        c2 = '%s ` = ` %d ` DIVIDE ` %d ` - ` %d ` = ` %d ` - ` %d ` = ` %d' % (a2, s5, s3, s4, s6, s4, v1)

        eq = left if v1 < v2 else right
        c3 = '%d ` %s ` %d' % (v2, eq, v1)

    v1, v2 = [v1, v2] if v1 > v2 else [v2, v1]
    cor_text = v1 - v2
    c4 = '%d ` - ` %d ` = ` %d' % (v1, v2, cor_text)

    stem = stem.format(a1=a1, a2=a2)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4)

    return stem, answer, comment











































# 5-1-1-37
def naturalmixcal511_Stem_030():
    stem = "바르게 계산한 사람은 누구인가요?\n$$표$$ {t1}: $$수식$${a1}$$/수식$$\n{t2}: $$수식$${a2}$$/수식$$$$/표$$\n"
    answer = '(정답)\n{cor_person}\n'
    comment = '(해설)\n' \
              '덧셈, 뺄셈, 나눗셈, $$수식$$LEFT ( ~~ RIGHT )$$/수식$$가 섞여 있는 식은 가장 먼저 $$수식$$LEFT ( ~~ RIGHT )$$/수식$$ 안부터 계산합니다.\n' \
              '잘못 계산한 {uncor_person}의 식을 계산하면\n' \
              '$$수식$${c1}$$/수식$$입니다.\n\n'


    flag = True

    while flag :
        # 1A 2B 3C 4D 5E 6F 7G 8H 9I 10J 11K 12L 13M 14N
        # 15O 16P 17Q 18R 19S 20T 21U 22V 23W 25X 25Y 26Z
        # 27a 28b 29c 30d 31e 32f 33g 34h 35i 36j 37k 38l 39m 40n

        s2, s3 = np.random.choice(np.arange(2, 7), 2, False)
        s1 = get_lcm(s2, s3) * np.random.randint(1, 10, 1)[0]
        s4 = s1 // s2
        s5 = s3 + s4
        s6 = np.random.choice([12, 18, 24, 30, 36], 1)[0]
        s7 = np.random.randint(9, 15, 1)[0]
        s8 = s7 - np.random.choice([2, 3], 1)[0]
        s9 = s7 - s8
        s10 = s6 // s9

        s11 = s2 + s3
        s12 = s1 // s11
        if 20 < s1 < 100 and s6 % s9 == 0 and s1 % s11 == 0:
            flag = False

    terms = [np.random.choice(person_nam, 1)[0], np.random.choice(person_yeo, 1)[0]]
    np.random.shuffle(terms)
    t1, t2 = terms

    mode = np.random.choice([0, 1], 1)[0]

    if mode == 0:
        a1 = '%d ` DIVIDE ` LEFT ( %d ` + ` %d RIGHT ) ` = ` %d ` + ` %d ` = ` %d' % (s1, s2, s3, s4, s3, s5)
        a2 = '%d ` DIVIDE ` LEFT ( %d ` - ` %d RIGHT ) ` = ` %d ` DIVIDE ` %d ` = ` %d' % (s6, s7, s8, s6, s9, s10)
        uncor_person, cor_person = terms
    else:
        a1 = '%d ` DIVIDE ` LEFT ( %d ` - ` %d RIGHT ) ` = ` %d ` DIVIDE ` %d ` = ` %d' % (s6, s7, s8, s6, s9, s10)
        a2 = '%d ` DIVIDE ` LEFT ( %d ` + ` %d RIGHT ) ` = ` %d ` + ` %d ` = ` %d' % (s1, s2, s3, s4, s3, s5)
        [cor_person, uncor_person] = terms

    c1 = '%d ` DIVIDE ` LEFT ( %d ` + ` %d RIGHT ) ` = ` %d ` DIVIDE ` %d ` = ` %d' % (s1, s2, s3, s1, s11, s12)

    stem = stem.format(a1=a1, a2=a2, t1=t1, t2=t2)
    answer = answer.format(cor_person=cor_person)
    comment = comment.format(c1=c1, uncor_person=uncor_person)

    return stem, answer, comment








































# 5-1-1-38
def naturalmixcal511_Stem_031():
    stem = "계산 결과가 가장 큰 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$\n㉡ $$수식$${problem2}$$/수식$$\n㉢ $$수식$${problem3}$$/수식$$\n㉣ $$수식$${problem4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{answer_sign}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${explain1}$$/수식$$\n" \
              "$$수식$${explain2}$$/수식$$\n" \
              "㉡ $$수식$${explain3}$$/수식$$\n" \
              "$$수식$${explain4}$$/수식$$\n" \
              "㉢ $$수식$${explain5}$$/수식$$\n" \
              "$$수식$${explain6}$$/수식$$\n" \
              "㉣ $$수식$${explain7}$$/수식$$\n" \
              "$$수식$${explain8}$$/수식$$\n" \
              "$$수식$${explain9}$$/수식$$이므로 계산 결과가 가장 큰 것은 {answer_sign}입니다.\n\n"


    while 1:
        num3 = random.randint(2, 7)
        while 1:
            num2 = random.randint(3, 9)
            if 15 < num2 * num3 < 30:
                num2 = num2 * num3
                break
        num1 = random.randint(51, 69)
        num4 = random.randint(2, 9)
        s1 = num1 + int(num2 / num3) - num4
        if 0 < s1 < 100:
            break

    while 1:
        num5 = random.randint(51, 69)
        num6 = random.randint(2, 4)
        num7 = random.randint(2, 4)
        num8 = random.randint(11, 14)
        s2 = num5 - num6 * num7 + num8
        if 0 < s2 < 100 and s1 != s2:
            break

    while 1:
        num11 = random.randint(6, 9)
        num12 = num11 - 4
        num9 = random.randint(51, 69)
        num10 = random.choice([28, 32, 36, 40])
        s3 = num9 + int(num10 / (num11 - num12))
        if 0 < s3 < 100 and s1 != s3 and s2 != s3:
            break

    while 1:
        num13 = random.randint(51, 69)
        num14 = random.choice([2, 3])
        num15 = random.randint(3, 5)
        num16 = num15 - 1
        s4 = num13 - num14 * (num15 + num16)
        if 0 < s4 < 100 and s1 != s4 and s2 != s4 and s3 != s4:
            break


    problem1 = '{0} ` + ` {1} ` DIVIDE ` {2} ` - ` {3}'.format(num1, num2, num3,  num4)
    explain1 = '{0} ` = ` {1} ` + ` {2} ` - ` {3}'.format(problem1, num1, int(num2 / num3), num4)
    explain2 = '= ` {0} ` - ` {1} ` = ` {2}'.format(num1 + int(num2 / num3), num4, s1)

    problem2 = '{0} ` - ` {1} ` TIMES ` {2} ` + ` {3}'.format(num5, num6, num7, num8)
    explain3 = '{0} ` = ` {1} ` - ` {2} ` + ` {3}'.format(problem2, num5, num6 * num7, num8)
    explain4 = '= ` {0} ` + ` {1} ` = ` {2}'.format(num5 - num6 * num7, num8, s2)

    problem3 = '{0} ` + ` {1} ` DIVIDE ` LEFT ( {2} ` - ` {3} RIGHT )'.format(num9, num10, num11, num12)
    explain5 = '{0} ` = ` {1} ` + ` {2} ` DIVIDE ` {3}'.format(problem3, num9, num10, num11 - num12)
    explain6 = '= ` {0} ` + ` {1} ` = ` {2}'.format(num9, int(num10 / (num11 - num12)), s3)

    problem4 = '{0} ` - ` {1} ` TIMES ` LEFT ( {2} ` + ` {3} RIGHT )'.format(num13, num14, num15, num16)
    explain7 = '{0} ` = ` {1} ` - ` {2} ` TIMES ` {3}'.format(problem4, num13, num14, num15 + num16)
    explain8 = '= ` {0} ` - ` {1} ` = ` {2}'.format(num13, num14 * (num15 + num16), s4)

    lst = [[s1, '㉠'], [s2, '㉡'], [s3, '㉢'], [s4, '㉣']]
    lst.sort(reverse=True, key=lambda x: x[0])

    explain9 = '{0} ` &gt; ` {1} ` &gt; ` {2} ` &gt; ` {3}'.format(lst[0][0], lst[1][0], lst[2][0], lst[3][0])
    answer_sign = lst[0][1]

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, problem4=problem4)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             explain5=explain5, explain6=explain6, explain7=explain7, explain8=explain8,
                             explain9=explain9, answer_sign=answer_sign)

    return stem, answer, comment









































# 5-1-1-39
def naturalmixcal511_Stem_032():
    stem = "남학생 $$수식$${problem1}$$/수식$$명은 $$수식$${problem2}$$/수식$$명씩 한 모둠을 만들고, 여학생 $$수식$${problem3}$$/수식$$명은 $$수식$${problem4}$$/수식$$명씩 한 모둠을 만들었습니다. 만든 모둠은 모두 몇 모둠인가요?\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$모둠\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$만든 모둠 수$$수식$$RIGHT ) {explain1}$$/수식$$\n" \
              "$$수식$${explain2} LEFT ($$/수식$$모둠$$수식$$RIGHT )$$/수식$$\n\n"


    num2, num4 = random.sample(range(2, 5), 2)

    while 1:
        num1 = random.randint(2, 9)
        num3 = random.randint(2, 9)
        num5 = num1 * num2
        num6 = num3 * num4
        if 9 < num5 < 20 and 9 < num6 < 20 and num5 != num6:
            break

    answer_num = num1 + num3
    problem1, problem2, problem3, problem4 = num5, num2, num6, num4

    explain1 = '` = ` {0} ` DIVIDE ` {1} ` + ` {2} ` DIVIDE ` {3}'.format(num5, num2, num6, num4)
    explain2 = '= ` {0} ` + ` {1} ` = ` {2}'.format(num1, num3, answer_num)

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, problem4=problem4)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2)

    return stem, answer, comment












































# 5-1-1-41
def naturalmixcal511_Stem_033():
    stem = "□ 안에 알맞은 수를 구해 보세요.\n$$표$$$$수식$${problem1}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$에서\n" \
              "$$수식$${explain2}$$/수식$$, $$수식$${explain3}$$/수식$$,\n" \
              "$$수식$${explain4}$$/수식$$, $$수식$${explain5}$$/수식$$, $$수식$${explain6}$$/수식$$입니다.\n\n"


    while 1:
        answer_num = random.randint(5, 9)
        tmp = random.randint(5, 9)
        num3 = answer_num * tmp
        if 40 < num3 < 60:
            break

    num1 = random.randint(22, 24)
    num2 = random.randint(11, 13)

    num4 = num1 - num2 + tmp

    problem1 = '{0} ` - ` {1} ` + ` {2} ` DIVIDE ` {3} ` = ` {4}'.format(num1, num2, num3, box, num4)
    explain1 = problem1

    explain2 = '{0} ` + ` {1} ` DIVIDE ` {2} ` = ` {3}'.format(num1-num2, num3, box, num4)
    explain3 = '{0} ` DIVIDE ` {1} ` = ` {2} ` - ` {3}'.format(num3, box, num4, num1-num2)
    explain4 = '{0} ` DIVIDE ` {1} ` = ` {2}'.format(num3, box, tmp)
    explain5 = '{0} ` = ` {1} ` DIVIDE ` {2}'.format(box, num3, tmp)
    explain6 = '{0} ` = ` {1}'.format(box, answer_num)

    stem = stem.format(problem1=problem1)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             explain5=explain5, explain6=explain6)

    return stem, answer, comment














































# 5-1-1-42
def naturalmixcal511_Stem_034():
    stem = "무게가 같은 감자 $$수식$${problem1}$$/수식$$개의 무게는 $$수식$${problem2} ` rm g$$/수식$$, 고구마 한 개의 무게는 $$수식$${problem3} ` rm g$$/수식$$, 무게가 같은 달걀 $$수식$${problem4}$$/수식$$개의 무게는 $$수식$${problem5} ` rm g$$/수식$$입니다. 감자 한 개와 고구마 한 개의 무게의 합은 달걀 한 개의 무게보다 몇 $$수식$$rm g$$/수식$$ 더 무거운지 식을 하나로 써서 구해 보세요.\n"
    answer = "(정답)\n$$수식$${answer_equ} rm g$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$감자 한 개의 무게$$수식$$RIGHT ) ` + ` LEFT ($$/수식$$고구마 한 개의 무게$$수식$$RIGHT ) $$/수식$$\n$$수식$$` - ` LEFT ($$/수식$$달걀 한 개의 무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${explain1}$$/수식$$\n" \
              "$$수식$${explain2} LEFT ( rm g RIGHT )$$/수식$$\n\n"


    num1, num4 = random.sample(range(2, 4), 2)
    num3 = random.choice([i for i in range(51, 100) if i % 2 == 0])
    num2 = random.choice([120, 180, 240, 300])

    while 1:
        num5 = random.choice([i for i in range(101, 200) if i % 12 == 0])
        if num2 != num5:
            break

    problem1, problem2, problem3, problem4, problem5 = num1, num2, num3, num4, num5
    answer_equ = '{0} ` DIVIDE ` {1} ` + ` {2} ` - ` {3} ` DIVIDE ` {4}'.format(num2, num1, num3, num5, num4)

    explain1 = '= `' + answer_equ
    answer_num = int(num2 / num1) + num3 - int(num5 / num4)

    explain2 = '= ` {0} ` + ` {1} ` - ` {2} ` = ` {3} ` - ` {2} ` = ` {4}'\
        .format(int(num2 / num1), num3, int(num5 / num4), int(num2 / num1) + num3, answer_num)

    answer_equ = answer_equ + '` = ` {answer_num}'.format(answer_num=answer_num)

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, problem4=problem4, problem5=problem5)
    answer = answer.format(answer_num=answer_num, answer_equ=answer_equ)
    comment = comment.format(explain1=explain1, explain2=explain2)

    return stem, answer, comment












































# 5-1-1-44
def naturalmixcal511_Stem_035():
    stem = "{person}{post} 문구점에서 $$수식$${problem1}$$/수식$$권에 $$수식$${problem2}$$/수식$$원인 공책 한 권과 {object1} 한 개를 사고 $$수식$${problem3}$$/수식$$원을 냈습니다. 거스름돈으로 $$수식$${problem4}$$/수식$$원을 받았다면 {object1} 한 개의 값은 얼마인지 식을 하나로 써서 구해 보세요.\n"
    answer = "(정답)\n$$수식$${answer_equ}$$/수식$$원\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${object1} 한 개의 값$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$ = {explain1}$$/수식$$\n" \
              "$$수식$${explain2}$$/수식$$\n" \
              "$$수식$${explain3}$$/수식$$\n" \
              "$$수식$${explain4} LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$\n\n"


    person = random.choice(person_yeo + person_nam)
    post = '는' if josa_check(person[-1]) == ' ' else '이는'
    object1 = random.choice(['샤프', '볼펜', '화일', '팽이', '연필', '색종이'])

    while 1:
        num1 = random.randint(3, 5)
        num2 = random.choice([i for i in range(30, 46) if i % num1 == 0]) * 100
        num3 = random.randint(40, 50) * 100
        num4 = random.randint(20, 30) * 100
        answer_num = num3 - (num2 // num1 + num4)
        if answer_num != 0:
            break

    problem1, problem2, problem3, problem4 = num1, num2, num3, num4
    answer_equ = '{0} ` - ` LEFT ( {1} ` DIVIDE ` {2} ` + ` {3} RIGHT )'.format(num3, num2, num1, num4)

    explain1 = answer_equ
    explain2 = '= ` {0} ` - ` LEFT ( {1} ` + ` {2} RIGHT )'.format(num3, num2 // num1, num4)
    explain3 = '= ` {0} ` - ` {1}'.format(num3, num2 // num1 + num4)
    explain4 = '= ` {0}'.format(answer_num)
    answer_equ = answer_equ + '` = ` {0}'.format(answer_num)


    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, problem4=problem4,
                       person=person, post=post, object1=object1)
    answer = answer.format(answer_num=answer_num, answer_equ=answer_equ)
    comment = comment.format(object1=object1, explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4)

    return stem, answer, comment









































# 5-1-1-45
def naturalmixcal511_Stem_036():
    stem = "계산 결과가 큰 것부터 차례대로 기호를 써 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$\n㉡ $$수식$${problem2}$$/수식$$\n㉢ $$수식$${problem3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{answer_sign}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${explain1}$$/수식$$\n" \
              "$$수식$${explain2}$$/수식$$\n" \
              "㉡ $$수식$${explain3}$$/수식$$\n" \
              "$$수식$${explain4}$$/수식$$\n" \
              "㉢ $$수식$${explain5}$$/수식$$\n" \
              "$$수식$${explain6}$$/수식$$\n" \
              "$$수식$${explain7}$$/수식$$이므로 계산 결과가 큰 것부터 차례대로 기호를 쓰면 {answer_sign}입니다.\n\n"


    num1 = random.randint(2, 5)
    num2 = random.choice([12, 15, 16, 18, 20])
    num3 = random.choice([i for i in range(2, 6) if num2 % i == 0])

    num4, num5 = random.sample(range(2, 6), 2)

    s1 = num1 * num2 // num3 + num4 - num5

    problem1 = '{0} `TIMES` {1} `DIVIDE` {2} `+` {3} `-` {4}'.format(num1, num2, num3, num4, num5)
    explain1 = problem1 + '`=` {0} `DIVIDE` {1} `+` {2} `-` {3}'.format(num1 * num2, num3, num4, num5)
    explain2 = '=` {0} `+` {1} `-` {2} `=` {3} `-` {2} `=` {4}'\
        .format(num1 * num2 // num3, num4, num5, num1 * num2 // num3 + num4, s1)

    while 1:
        num1 = random.randint(2, 3)
        num3 = random.randint(11, 19)
        num4 = random.choice([num3 - 3, num3 - 5, num3 - 7])
        num2 = random.choice([i for i in range(16, 30) if i % (num3 - num4) == 0])
        num5 = random.randint(2, 9)
        s2 = num1 * num2 // (num3 - num4) + num5
        if s1 != s2:
            break

    problem2 = '{0} `TIMES` {1} `DIVIDE` LEFT ( {2} `-` {3} RIGHT ) `+` {4}'.format(num1, num2, num3, num4, num5)
    explain3 = problem2 + '`=` {0} `TIMES` {1} `DIVIDE` {2} `+` {3}'.format(num1, num2, num3 - num4, num5)
    explain4 = '=` {0} `DIVIDE` {1} `+` {2} `=` {3} `+` {2} `=` {4}' \
        .format(num1 * num2, num3 - num4, num5, (num1 * num2) // (num3 - num4), s2)

    while 1:
        num1 = random.randint(11, 16)
        num2 = random.choice([2, 3, 5])
        num4 = random.choice([3, 5])
        num3 = random.choice([i for i in range(41, 61) if i % num4 == 0])
        num5 = random.randint(2, 9)
        s3 = num1 * num2 - (num3 // num4) + num5
        if s1 != s3 and s2 != s3:
            break

    problem3 = '{0} `TIMES` {1} `-` {2} `DIVIDE` {3} `+` {4}'.format(num1, num2, num3, num4, num5)

    explain5 = problem3 + '`=` {0} `-` {1} `+` {2}'.format(num1 * num2, num3 // num4, num5)
    explain6 = '=` {0} `+` {1} `=` {2}' \
        .format(num1 * num2 - num3 // num4, num5, s3)

    tmp = [[problem1, explain1, explain2, s1], [problem2, explain3, explain4, s2], [problem3, explain5, explain6, s3]]
    random.shuffle(tmp)

    problem1, problem2, problem3 = tmp[0][0], tmp[1][0], tmp[2][0]
    explain1, explain3, explain5 = tmp[0][1], tmp[1][1], tmp[2][1]
    explain2, explain4, explain6 = tmp[0][2], tmp[1][2], tmp[2][2]

    s1, s2, s3 = tmp[0][3], tmp[1][3], tmp[2][3]


    lst = [[s1, '㉠'], [s2, '㉡'], [s3, '㉢']]
    lst.sort(key=lambda x: x[0], reverse=True)

    explain7 = '{0} `&gt;` {1} `&gt;` {2}'.format(lst[0][0], lst[1][0], lst[2][0])
    answer_sign = '{0}, {1}, {2}'.format(lst[0][1], lst[1][1], lst[2][1])

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             explain5=explain5, explain6=explain6, explain7=explain7,  answer_sign=answer_sign)

    return stem, answer, comment















































# 5-1-1-46
def naturalmixcal511_Stem_037():
    stem = "계산 결과가 틀린 것의 기호를 쓰고, 바르게 계산한 답을 구해 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$\n㉡ $$수식$${problem2}$$/수식$$\n㉢ $$수식$${problem3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{answer_sign}, $$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "{answer_sign} $$수식$${explain1}$$/수식$$\n" \
              "$$수식$${explain2}$$/수식$$\n\n"


    rand_answer = [0, 0, 1]
    random.shuffle(rand_answer)

    num1 = random.randint(41, 49)
    num2 = random.choice([i for i in range(2, 10) if i != 6])
    num3 = 6
    num4 = random.randint(2, 3)
    num5 = random.randint(21, 29)
    s1 = num1 - num2 * num3 // num4 + num5
    problem1 = '{0} `-` {1} `TIMES` {2} `DIVIDE` {3} `+` {4}'.format(num1, num2, num3, num4, num5)
    if rand_answer[0] == 1:
        explain1 = problem1 + '`=` {0} `-` {1} `DIVIDE` {2} `+` {3}'.format(num1, num2 * num3, num4, num5)
        problem1 += '`=` {0}'.format(abs(num1 - num2 * num3 // num4 - num5))
        explain2 = '=` {0} `-` {1} `+` {2} `=` {3} `+` {2} `=` {4}'\
            .format(num1, num2 * num3 // num4, num5, num1 - num2 * num3 // num4, s1)
    else:
        problem1 += '`=` {0}'.format(s1)

    num2 = random.choice([11, 12, 13])
    num1 = num2 * 3
    num3 = random.randint(4, 7)
    num4 = random.choice([i for i in range(6, 8) if i != num3])
    num5 = random.randint(11, 19)
    s2 = num1 // num2 + num3 * num4 - num5
    problem2 = '{0} `DIVIDE` {1} `+` {2} `TIMES` {3} `-` {4}'.format(num1, num2, num3, num4, num5)
    if rand_answer[1] == 1:
        explain1 = problem2 + '`=` {0} `+` {1} `-` {2}'.format(num1 // num2, num3 * num4, num5)
        problem2 += '`=` {0}'.format(abs(num1 // num2 - num3 * num4 - num5))
        explain2 = '=` {0} `-` {1} `=` {2}' \
            .format(num1 // num2 + num3 * num4, num5, (num1 // num2 + num3 * num4) - num5)
    else:
        problem2 += '`=` {0}'.format(s2)

    num1 = random.randint(3, 6)
    num2 = random.choice([i for i in range(5, 10) if i != num1])
    num4 = random.choice([3, 4, 5])
    num3 = num4 * 8
    num5 = random.randint(15, 19)
    s3 = num1 * num2 + num3 // num4 - num5
    problem3 = '{0} `TIMES` {1} `+` {2} `DIVIDE` {3} `-` {4}'.format(num1, num2, num3, num4, num5)
    if rand_answer[2] == 1:
        explain1 = problem3 + '`=` {0} `+` {1} `-` {2}'.format(num1 * num2, num3 // num4, num5)
        problem3 += '`=` {0}'.format(abs(num1 * num2 - num3 // num4 - num5))
        explain2 = '=` {0} `-` {1} `=` {2}' \
            .format(num1 * num2 + num3 // num4, num5, s3)
    else:
        problem3 += '`=` {0}'.format(s3)

    lst = [[s1, '㉠', rand_answer[0]], [s2, '㉡', rand_answer[1]], [s3, '㉢', rand_answer[2]]]
    for a, b, c in lst:
        if c == 1:
            answer_num = a
            answer_sign = b

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3)
    answer = answer.format(answer_sign=answer_sign, answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, answer_sign=answer_sign)

    return stem, answer, comment













































# 5-1-1-47
def naturalmixcal511_Stem_038():
    stem = "크기를 비교하여 $$수식$${boxblank}$$/수식$$ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$표$$$$수식$${problem1}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_sign}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$\n" \
              "$$수식$${explain2}$$/수식$$이므로 $$수식$${explain3}$$/수식$$입니다.\n\n"


    boxblank = "□"
    num2 = random.randint(3, 5)
    num1 = random.choice([i for i in range(16, 30) if i % num2 == 0])
    num3 = random.randint(4, 8)
    num4 = random.choice([i for i in range(4, 8) if i != num3])
    num5 = random.randint(2, 9)

    problem1 = '{0} `DIVIDE` {1} `+` {2} `TIMES` {3} `-` {4}'.format(num1, num2, num3, num4, num5)
    result = num1 // num2 + num3 * num4 - num5

    explain1 = problem1 + '`=` {0} `+` {1} `-` {2} `=` {3} `-` {2} `=` {4}'\
        .format(num1 // num2, num3 * num4, num5, num1 // num2 + num3 * num4, result)

    problem1 += '~~□~~'
    rand_answer = random.choice([[result - 10, '&gt;'], [result, '`=`'], [result + 10, '&lt;']])
    problem1 += str(rand_answer[0])

    explain2 = '{0} {1} {2}'.format(result, rand_answer[1], rand_answer[0])

    explain3 = '{0} `DIVIDE` {1} `+` {2} `TIMES` {3} `-` {4} {5} {6}'\
        .format(num1, num2, num3, num4, num5, rand_answer[1], rand_answer[0])

    answer_sign = rand_answer[1]

    stem = stem.format(problem1=problem1, boxblank=boxblank)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3)

    return stem, answer, comment














































# 5-1-1-48
def naturalmixcal511_Stem_039():
    stem = "$$수식$$LEFT ( ~~ RIGHT )$$/수식$$가 없어도 계산 결과가 같은 식을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$\n㉡ $$수식$${problem2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{answer_sign}\n"
    comment = "(해설)\n" \
              "㉠ {explain1}\n" \
              "㉡ {explain2}\n" \
              "따라서 $$수식$$LEFT ( ~~ RIGHT )$$/수식$$가 없어도 계산 결과가 같은 식은 {answer_sign}입니다.\n\n"



    while True:
        while 1:
            num1 = random.choice([i for i in range(10, 21) if i % 2 == 0])
            num2 = random.randint(5, 8)
            tmp = []
            for i in range(11, 20):
                if (num1 * num2) % i == 0:
                    tmp.append(i)
            if len(tmp) > 0:
                break

        num3 = random.choice(tmp)
        num4 = num3 - num2
        s1 = (num1 * num2) // (num3 - num4)

        problem1 = 'LEFT ( {0} `TIMES` {1} RIGHT ) `DIVIDE` LEFT ( {2} `-` {3} RIGHT )'.format(num1, num2, num3, num4)
        ex1 = '$$수식$${0} `=` {1} `DIVIDE` {2} `=` {3}$$/수식$$\n'.format(problem1, num1 * num2, num3 - num4, s1)
        ex1 += '$$수식$${0} `TIMES` {1} `DIVIDE` {2} `-` {3} `=` {4} `DIVIDE` {2} `-` {3} `=` {5} `-` {3} `=` {6}$$/수식$$'\
            .format(num1, num2, num3, num4, num1 * num2, (num1 * num2) // num3, (num1 * num2) // num3 - num4)

        check_ing = (num1 * num2) // num3 - num4

        num1 = random.randint(11, 18)
        num2 = random.randint(4, 8)
        num3 = random.randint(2, 4)
        num4 = random.randint(12, 18)
        num5 = random.choice([i for i in range(2, 10) if (num3 * num4) % i == 0])

        s2 = (num1 - num2) + (num3 * num4) // num5

        problem2 = 'LEFT ( {0} `-` {1} RIGHT ) `+` LEFT ( {2} `TIMES` {3} RIGHT ) `DIVIDE` {4}'\
            .format(num1, num2, num3, num4, num5)

        ex2 = "$$수식$${0} `=` {1} `+` {2} `DIVIDE` {3}$$/수식$$\n".format(problem2, num1 - num2, num3 * num4, num5)
        ex2 += "$$수식$$=` {0} `+` {1} `=` {2}$$/수식$$\n".format(num1 - num2, (num3 * num4) // num5, s2)
        ex2 += "$$수식$${0} `-` {1} `+` {2} `TIMES` {3} `DIVIDE` {4} `=` {0} `-` {1} `+` {5} `DIVIDE` {4}$$/수식$$\n"\
            .format(num1, num2, num3, num4, num5, num3 * num4)

        ex2 += "$$수식$$=` {0} `-` {1} `+` {2} `=` {3} `+` {2} `=` {4}$$/수식$$"\
            .format(num1, num2, (num3 * num4) // num5, num1 - num2, s2)

        lst = [[problem1, ex1, 0], [problem2, ex2, 1]]
        random.shuffle(lst)
        problem1, problem2 = lst[0][0], lst[1][0]
        explain1, explain2 = lst[0][1], lst[1][1]
        sign = ['㉠', '㉡']

        for idx, i in enumerate(lst):
            if i[2] == 1:
                answer_sign = sign[idx]

        if check_ing >= 0 and s2 >= 0:
            break



    stem = stem.format(problem1=problem1, problem2=problem2)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2, answer_sign=answer_sign)

    return stem, answer, comment


















































# 5-1-1-49
def naturalmixcal511_Stem_040():
    stem = "계산 결과의 크기를 비교하여 $$수식$${boxblank}$$/수식$$ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$표$$$$수식$${problem1}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_sign}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$\n" \
              "$$수식$${explain2}$$/수식$$\n" \
              "$$수식$${explain3}$$/수식$$\n" \
              "$$수식$${explain4}$$/수식$$\n" \
              "$$수식$${explain5}$$/수식$$이므로\n" \
              "$$수식$${explain6}$$/수식$$입니다.\n\n"



    boxblank = "□"

    while 1:
        num1 = random.randint(23, 29)
        num2 = random.randint(16, 19)
        tmp = []
        for i in range(2, 8):
            if (num1 + num2) % i == 0 and num2 % i == 0:
                tmp.append(i)
        if len(tmp) > 0:
            break

    num3 = random.choice(tmp)
    num4 = random.randint(5, 8)
    num5 = random.randint(21, 24)

    equ1 = 'LEFT ( {0} `+` {1} RIGHT ) `DIVIDE` {2} `TIMES` {3} `-` {4}'.format(num1, num2, num3, num4, num5)
    equ2 = '{0} `+` {1} `DIVIDE` {2} `TIMES` {3} `-` {4}'.format(num1, num2, num3, num4, num5)
    s1 = (num1 + num2) // num3 * num4 - num5

    explain1 = equ1 + '`=` {0} `DIVIDE` {1} `TIMES` {2} `-` {3}'.format(num1 + num2, num3, num4, num5)
    explain2 = '=` {0} `TIMES` {1} `-` {2} `=` {3} `-` {2} `=` {4}'\
        .format((num1 + num2) // num3, num4, num5, (num1 + num2) // num3 * num4, s1)

    s2 = num1 + num2 // num3 * num4 - num5

    explain3 = equ2 + '`=` {0} `+` {1} `TIMES` {2} `-` {3}'.format(num1, num2 // num3, num4, num5)
    explain4 = '=` {0} `+` {1} `-` {2} `=` {3} `-` {2} `=` {4}' \
        .format(num1, num2 // num3 * num4, num5, num1 + num2 // num3 * num4, s2)

    lst = [[equ1, s1, explain1, explain2], [equ2, s2, explain3, explain4]]
    random.shuffle(lst)

    equ1, equ2 = lst[0][0], lst[1][0]
    s1, s2 = lst[0][1], lst[1][1]
    explain1, explain3 = lst[0][2], lst[1][2]
    explain2, explain4 = lst[0][3], lst[1][3]

    problem1 = '{0} ~~□~~ {1}'.format(equ1, equ2)

    if s1 > s2:
        explain5 = '{0} `&gt;` {1}'.format(s1, s2)
        explain6 = '{0} `&gt;` {1}'.format(equ1, equ2)
        answer_sign = '&gt;'
    elif s1 < s2:
        explain5 = '{0} `&lt;` {1}'.format(s1, s2)
        explain6 = '{0} `&lt;` {1}'.format(equ1, equ2)
        answer_sign = '&lt;'
    else:
        explain5 = '{0} `=` {1}'.format(s1, s2)
        explain6 = '{0} `=` {1}'.format(equ1, equ2)
        answer_sign = '='

    stem = stem.format(problem1=problem1, boxblank=boxblank)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3,
                             explain4=explain4, explain5=explain5, explain6=explain6)

    return stem, answer, comment





































# 5-1-1-50
def naturalmixcal511_Stem_041():
    stem = "$$수식$${box}$$/수식$$ 안에 알맞은 수를 구해 보세요.\n$$표$$$$수식$${A} `TIMES` LEFT ( {B} `+` {box}` RIGHT ) `DIVIDE` LEFT ( {C} `-` {D} RIGHT ) `=` {E}`$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A} `TIMES` LEFT ( {B} `+` {box}` RIGHT ) `DIVIDE` LEFT ( {C} `-` {D} RIGHT ) `=` {E}$$/수식$$에서\n" \
              "$$수식$${A} `TIMES` LEFT ( {B} `+` {box}` RIGHT ) `DIVIDE` {a} `=` {E}$$/수식$$, $$수식$${A} ` TIMES ` LEFT ( {B} `+` {box}` RIGHT ) `=` {E} `TIMES` {a}$$/수식$$\n" \
              "$$수식$${A} `TIMES` LEFT ( {B} `+` {box}` RIGHT ) `=` {b}$$/수식$$, $$수식$${B} `+` {box} `=` {b} `DIVIDE` {A}$$/수식$$\n" \
              "$$수식$${B} `+` {box} `=` {c}$$/수식$$, $$수식$${box} `=` {c} `-` {B}$$/수식$$, $$수식$${box} `=` {S}$$/수식$$입니다.\n\n"


    box = '□'

    flag = True
    while flag:
        B = random.randint(3, 6)
        C = random.randint(6, 9)
        D = random.randint(2, 6)
        E = random.randint(5, 14)

        if C - D >= 2:
            # A조건(E-(C-D))의 약수 구하기
            F = E * (C-D)
            divsor_list = get_divisors(F)
            A = random.choice(divsor_list)

            a = C - D
            b = E * a
            c = b // A
            S = c - B

            if S > 0 and a >= 2 and A != B and 1 < A < 7:
                flag = False

    stem = stem.format(box=box, A=A, B=B, C=C, D=D, E=E)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, a=a, b=b, c=c, box=box, S=S)

    return stem, answer, comment









































# 5-1-1-51
def naturalmixcal511_Stem_042():
    stem = "식이 성립하도록 $$수식$${box}$$/수식$$ 안에 $$수식$$+$$/수식$$, $$수식$$-$$/수식$$, $$수식$$TIMES$$/수식$$, $$수식$$DIVIDE$$/수식$$를 알맞게 써넣으세요.\n$$표$$$$수식$${A} `+` LEFT ( {B} `-` {C} RIGHT ) `DIVIDE` {D} `TIMES` {E} `=` {F} ~{box}~ {G} `TIMES` {H}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${K}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A} `+` LEFT ( {B} `-` {C} RIGHT ) `DIVIDE` {D} `TIMES` {E} `=` {A} `+` {a} `DIVIDE` {D} `TIMES` {E}$$/수식$$에서\n" \
              "$$수식$$=` {A} `+` {b} `TIMES` {E} `=` {A} `+` {c} `=` {S}$$/수식$$\n" \
              "$$수식$${F} ``{box}`` {G} `TIMES` {H}$$/수식$$에서 $$수식$${F} `{K}` {G} `TIMES` {H} `=` {F} `{K}` {d} `=` {S}$$/수식$$이므로\n" \
              "$$수식$${box}$$/수식$$ 안에는 $$수식$${K}$$/수식$$가 들어갑니다.\n\n"



    box = '□'

    flag = True
    while flag:
        A = random.randint(11, 14)
        B = random.randint(16, 24)
        C = random.randint(5, 9)
        E = random.randint(2, 5)

        # D조건(B-C)의 약수 구하기
        F = B - C
        divsor_list = get_divisors(F)

        D = random.choice(divsor_list)

        if 1 < D < 7 and D != E:
            a = B - C
            if a % D == 0:
                b = a // D
                c = b * E
                S = A + c

                G = random.randint(3, 8)
                H = random.randint(3, 8)
                d = G * H

                if G != H and S % (G * H) == 0:
                    F_K_list = [(S - (G * H), '+'), (S + (G * H), '-'), (S // (G * H), 'TIMES'), (S*G*H, 'DIV')]
                    F, K = random.choice(F_K_list)

                    if 1 < F < 99:
                        flag = False


    stem = stem.format(box=box, A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H)
    answer = answer.format(K=K)
    comment = comment.format(box=box, A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, K=K, S=S, a=a, b=b, c=c, d=d)

    return stem, answer, comment







































# 5-1-1-52
def naturalmixcal511_Stem_043():
    '''
    :param r1: 한 상자에 들어있는 구슬의 개수 최솟값 [int] {4:5}
    :param r2: 한 상자에 들어있는 구슬의 개수 최댓값 [int] {6:7}
    :param r3: 구슬 상자 개수의 최솟값 [int] {5:6}
    :param r4: 구슬 상자 개수의 최댓값 [int] {7:8}
    '''
    stem = "{t}{t_josa1} 한 상자에 $$수식$${A}$$/수식$$개씩 들어 있는 구슬 $$수식$${B}$$/수식$$상자를 똑같이 $$수식$${C}$$/수식$$묶음으로 나누어 한 묶음을 가졌습니다. 이 중에서 $$수식$${D}$$/수식$$개를 동생에게 주고, $$수식$${E}$$/수식$$개를 형에게서 받았다면 {t}{t_josa2} 가지고 있는 구슬은 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${t}{t_josa2} 가지고 있는 구슬 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$=` {A} `TIMES` {B} `DIVIDE` {C} `-` {D} `+` {E} `=` {a} `DIVIDE` {C} `-` {D} `+` {E}$$/수식$$\n" \
              "$$수식$$=` {b} `-` {D} `+` {E} `=` {c} `+` {E} `=` {S} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"


    r1 = 4
    r2 = 7
    r3 = 5
    r4 = 8


    box = '□'

    flag = True
    while flag:
        # 사람 이름 정하기
        t = random.choice(person_nam)
        if han_josa(t[-1]) == ' ':
            t_josa1 = '는'
            t_josa2 = "가"
        else:
            t_josa1 = '이는'
            t_josa2 = '이가'

        A = random.randint(r1, r2)
        B = random.randint(r3, r4)

        if A != B:
            F = A * B
            C_list = [2, 3, random.choice(get_divisors(F))]
            C = random.choice(C_list)
            D = random.randint(2, 6)
            E = random.randint(2, 8)

            a = A * B
            if D != E and a % C == 0:
                b = a // C
                c = b - D
                S = c + E

                if S > 0 and C > 0 and c >= 0:
                    flag = False


    stem = stem.format(t=t, t_josa1=t_josa1, t_josa2=t_josa2, A=A, B=B, C=C, D=D, E=E)
    answer = answer.format(S=S)
    comment = comment.format(t=t, t_josa2=t_josa2, A=A, B=B, C=C, D=D, E=E, S=S, a=a, b=b, c=c)

    return stem, answer, comment









































# 5-1-1-53
def naturalmixcal511_Stem_044():
    '''
    :param r1: A, B, C에 들어갈 수 있는 수의 최솟값 [int] {11:12}
    :param r2: A, B, C에 들어갈 수 있는 수의 최댓값 [int] {39:40}
    :param r3: D의 최솟값 [int] {2:3}
    :param r4: D의 최댓값 [int] {6:7}
    '''
    stem = "식이 성립하도록 $$수식$${box}$$/수식$$ 안에 $$수식$$-$$/수식$$, $$수식$$TIMES$$/수식$$, $$수식$$DIVIDE$$/수식$$를 알맞게 한 번씩 써넣으세요.\n$$수식$${A} ~{box}~ LEFT ( {B} ~{box}~ {C} RIGHT ) ~{box}~ {D} `=` {E}$$/수식$$\n"
    answer = "(정답)\n$$수식$${K1}$$/수식$$, $$수식$${K2}$$/수식$$, $$수식$${K3}$$/수식$$\n"
    comment = "(해설)\n" \
              "적절하게 부호를 넣어서 식을 계산해 봅니다.\n" \
              "$$수식$${A} `{K1} ` LEFT ( {B} `{K2}` {C} RIGHT ) `{K3}` {D} `=` {A} `{K1}` {a} `{K3}` {D}$$/수식$$\n" \
              "$$수식$$=` {c} `{K3}` {D} `=` {E}$$/수식$$\n\n"


    r1 = 11
    r2 = 40
    r3 = 2
    r4 = 7


    box = '□'

    flag = True

    while flag:
        K2 = '-'
        K1, K3 = random.sample(['DIVIDE', 'TIMES'], 2)

        A, B, C = random.sample(list(range(r1, r2+1)), 3)
        D = random.randint(r3, r4)
        if C + 4 > B > C + 1:
            a = B - C
            if a % D == 0 and A % a == 0:
                if K3 == 'DIVIDE':
                    E = A * (B - C) // D
                    b = a // D
                    c = A * a

                    if (A * (B - C)) % D == 0:
                        flag = False
                else:
                    E = A // (B - C) * D
                    b = a * D
                    c = A // a

                    if A % (B-C) == 0:
                        flag = False


    stem = stem.format(box=box, A=A, B=B, C=C, D=D, E=E)
    answer = answer.format(K1=K1, K2=K2, K3=K3)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, a=a, c=c, K1=K1, K2=K2, K3=K3)

    return stem, answer, comment














































# 5-1-1-54
def naturalmixcal511_Stem_045():
    '''
    :param r1: 문제에 등장하는 수의 최솟값 [int] {2:3}
    :param r2: 문제에 등장하는 수의 최댓값 [int] {8:9}
    '''
    stem = "$$수식$${box}$$/수식$$ 안에 주어진 수를 한 번씩 써넣어서 식을 만들고 계산 결과를 구해 보세요.\n$$표$$$$수식$${A}$$/수식$$    $$수식$${B}$$/수식$$    $$수식$${C}$$/수식$$    $$수식$${D}$$/수식$$$$/표$$\n$$수식$${E} `TIMES` LEFT ( `{box} `+` {box}` RIGHT ) ` DIVIDE` {box} `-` {box} `=` {box}$$/수식$$\n"
    answer = "(정답)\n$$수식$${E} `TIMES` LEFT ( `{S1} `+` {S2}` RIGHT ) ` DIVIDE` {S3} `-` {S4} `=` {S5}$$/수식$$\n"
    comment = "(해설)\n" \
              "뺄셈이나 나눗셈이 계산되지 않는 경우가 되지 않도록 주의하여 $$수식$${box}$$/수식$$ 안에 주어진 수를 한 번씩 써넣습니다.\n" \
              "$$수식$${E} `TIMES` LEFT ( {S1} `+` {S2} RIGHT ) `DIVIDE` {S3} `-` {S4} `=` {E} `TIMES` {a} `DIVIDE` {S3} `-` {S4}$$/수식$$\n" \
              "$$수식$$=` {b} `DIVIDE` {S3} `-` {S4} `=` {c} `-` {S4} `=` {S5}$$/수식$$\n\n"


    r1 = 2
    r2 = 9


    box = '□'
    box_1, box_2, box_3, box_4, box_5 = 'box{`①`}', 'box{`②`}', 'box{`③`}', 'box{`④`}', 'box{`⑤`}'

    flag = True
    while flag:
        A, B, C, D, E = random.sample(list(range(r1, r2+1)), 5)
        S1, S2, S3, S4 = random.sample([A, B, C, D], 4)

        if E * (S1 + S2) % S3 == 0:
            if E * (S1 + S2) // S3 > S4:
                S5 = (E * (S1 + S2) // S3) - S4

                a = S1 + S2
                b = E * a
                if b % S3 == 0:
                    c = b // S3
                    flag = False

    stem = stem.format(box=box, box_1=box_1, box_2=box_2, box_3=box_3, box_4=box_4, box_5=box_5, A=A, B=B, C=C, D=D, E=E)
    answer = answer.format(S1=S1, S2=S2, S3=S3, S4=S4, S5=S5, E=E)
    comment = comment.format(box=box, S1=S1, S2=S2, S3=S3, S4=S4, S5=S5, E=E, a=a, b=b, c=c)

    return stem, answer, comment











































# 5-1-1-56
def naturalmixcal511_Stem_046():
    stem = "온도를 나타내는 단위에서는 섭씨$$수식$$LEFT ( ° rm C RIGHT )$$/수식$$와 화씨$$수식$$LEFT ( ° rm F RIGHT )$$/수식$$가 있습니다. 화씨온도에서 $$수식$$32$$/수식$$를 뺀 수에 $$수식$$5$$/수식$$를 곱하고 $$수식$$9$$/수식$$로 나누면 섭씨온도가 됩니다. 화씨온도 $$수식$${A} LEFT ( ° rm F RIGHT )$$/수식$$를 섭씨로 나타내면 몇 도$$수식$$LEFT ( ° rm C RIGHT )$$/수식$$인지 하나의 식으로 나타내어 구해 보세요.\n"
    answer = "(정답)\n$$수식$$LEFT ( {A} `-` 32 RIGHT ) `TIMES` 5 `DIVIDE` 9 `=` {S} LEFT ( ° rm C RIGHT )$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( {A} `-` 32 RIGHT ) ` TIMES ` 5 `DIVIDE` 9 `=` {a}` TIMES ` 5 `DIVIDE` 9$$/수식$$\n" \
              "$$수식$$=` {b} `DIVIDE` 9 `=` {S} LEFT ( ° rm C RIGHT )$$/수식$$\n" \
              "따라서 식으로 나타내면 $$수식$$LEFT ( {A} `-` 32 RIGHT ) `TIMES` 5 `DIVIDE` 9 `=` {S}$$/수식$$이고 답은 $$수식$${S} LEFT ( ° rm C RIGHT )$$/수식$$입니다.\n\n"


    box = '□'
    box_1, box_2 = '①', '②'

    flag = True
    while flag:
        A = random.choice([50, 59, 68, 77, 86])
        a = A-32
        b= a * 5

        if b % 9 == 0:
            S = b // 9
            flag = False

    stem = stem.format(A=A, box_1=box_1, box_2=box_2)
    answer = answer.format(A=A, S=S)
    comment = comment.format(A=A, a=a, b=b, S=S)

    return stem, answer, comment




































# 5-1-1-57
def naturalmixcal511_Stem_047():
    stem = "$$수식$${box}$$/수식$$ 안에 들어갈 수 있는 자연수의 개수를 구해 보세요.\n$$표$$$$수식$${A} `-` {B} `+` {C} `&lt;` {box} `&lt;` {D} `-` {E} `TIMES` {F}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${A} `-` {B} `+` {C} `=` {a} `+` {C} `=` {S1}$$/수식$$\n" \
              "$$수식$${D} `-` {E} ` TIMES ` {F} `=` {D} `-` {b} `=` {S2}$$/수식$$\n" \
              "$$수식$${S1} `&lt;` {box} `&lt;` {S2}$$/수식$$이므로 $$수식$${box}$$/수식$$ 안에 알맞은 자연수는\n" \
              "$$수식$${R}$$/수식$$로 모두 $$수식$${S}$$/수식$$개입니다.\n\n"


    box = '□'

    flag = True

    while True:
        A = random.randint(30,99)
        B = random.randint(10,99)
        C = random.randint(10,99)

        D = random.randint(50,110)
        E = random.randint(20,99)
        F = random.randint(2,9)

        if A > B and D > E:
            S1 = A - B + C
            S2 = D - E * F
            if S1 < S2 and S2 - S1 >=2 and S2 - S1 <= 6: break

    a = A-B
    b = E*F
    temp = []
    for i in range(S1+1,S2):
        temp.append(str(i))

    S = len(temp)
    R = ', '.join(temp)
    '''
    while flag:
        A = random.randint(46, 49)
        B = random.randint(36, 39)
        C = random.randint(11, 19)
        E = random.randint(21, 24)
        F = 2
        D = (A - B + C + E) * F + 5

        a = A - B
        b = E * F

        S1 = a + C
        S2 = D - b
        S = 4

        E1, E2, E3, E4 = list(range(S1 + 1, S1 + 4 + 1))

        flag = False
    '''

    stem = stem.format(box=box, A=A, B=B, C=C, D=D, E=E, F=F)
    answer = answer.format(S=S)
    comment = comment.format(box=box, A=A, B=B, C=C, D=D, E=E, F=F, a=a, b=b, S=S, S1=S1, S2=S2, R=R)

    return stem, answer, comment






































# 5-1-1-58
def naturalmixcal511_Stem_048():
    stem = "어떤 수를 구해 보세요.\n$$표$$$$수식$${A}$$/수식$${A_josa} $$수식$${B}$$/수식$$의 곱에서 어떤 수와 $$수식$${C}$$/수식$$의 합을 $$수식$${D}$$/수식$${D_josa} 나눈 몫을 빼면 $$수식$${E}$$/수식$$입니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 $$수식$${box}$$/수식$$라 하면\n" \
              "$$수식$${A} ` TIMES ` {B} `-` LEFT ( {box} `+` {C} RIGHT ) `DIVIDE` {D} `=` {E}$$/수식$$입니다.\n" \
              "$$수식$${A} ` TIMES ` {B} `= ` {a}$$/수식$$, $$수식$$LEFT ( {box} `+` {C} RIGHT ) `DIVIDE` {D} `=` △$$/수식$$라 하면\n" \
              "$$수식$${a} `-` △ `=` {E}$$/수식$$, $$수식$$△ `=` {a} `-` {E}$$/수식$$, $$수식$$△ `=` {b}$$/수식$$입니다.\n" \
              "$$수식$$△ `=` LEFT ( {box} `+` {C} RIGHT ) `DIVIDE` {D} `=` {b}$$/수식$$, $$수식$${box} `+` {C} `=` {b} ` TIMES ` {D}$$/수식$$,\n" \
              "$$수식$${box} `+` {C} `=` {c}$$/수식$$, $$수식$${box} `=` {c} `-` {C}$$/수식$$, $$수식$${box} `=` {S}$$/수식$$입니다.\n\n"



    box = '□'

    flag = True
    while flag:
        A = random.randint(31, 34)
        B = 2
        C = random.randint(21, 29)
        D = random.randint(2, 3)
        E = random.randint(31, 39)

        A_josa = num_josa(A)[0]
        D_josa = num_josa(D)[4]

        if A != C and C != E and A != E:
            a = A * B
            b = a - E
            c = b * D
            S = c - C

            flag = False

    stem = stem.format(A=A, A_josa=A_josa, B=B, C=C, D=D, D_josa=D_josa, E=E)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, a=a, b=b, c=c, box=box, S=S)

    return stem, answer, comment














































# 5-1-1-59
def naturalmixcal511_Stem_049():
    stem = "$$수식$${A}$$/수식$$명씩 $$수식$${B}$$/수식$$줄로 학생들이 서 있습니다. $$수식$${C}$$/수식$$명이 한 모둠이 되어 줄넘기를 할 때, 모두 몇 모둠을 만들 수 있는지 하나의 식으로 나타내어 구해 보세요.\n"
    answer = "(정답)\n$$수식$${A} ` TIMES ` {B} `DIVIDE` {C} `=` {S}` LEFT ($$/수식$$모둠$$수식$$RIGHT )$$/수식$$\n"
    comment = "(해설)\n" \
              "전체 학생 수를 한 모둠의 학생 수로 나누면 되므로 $$수식$${A} ` TIMES ` {B} `DIVIDE` {C}$$/수식$${C_josa} 계산합니다.\n" \
              "따라서 모두 $$수식$${A} ` TIMES ` {B} `DIVIDE` {C} `= ` {a} `DIVIDE` {C} `=` {S}` LEFT ($$/수식$$모둠$$수식$$RIGHT )$$/수식$$을 만들 수 있습니다.\n\n"


    box = '□'
    box_1, box_2 = '①', '②'

    flag = True
    while flag:
        A, B = random.sample([4, 6, 8, 9], 2)
        C = random.randint(2, 6)
        C_josa = num_josa(C)[2]

        if A != C and B != C and A * B % C == 0:
            a = A * B
            if a % C == 0:
                S = a // C
                flag = False

    stem = stem.format(A=A, B=B, C=C, box_1=box_1, box_2=box_2)
    answer = answer.format(A=A, B=B, C=C, S=S)
    comment = comment.format(A=A, B=B, C=C, S=S, a=a, C_josa=C_josa)

    return stem, answer, comment
































# 5-1-1-61
def naturalmixcal511_Stem_050():
    '''
    :param r1: 나무 기둥 1m의 무게 최솟값 [int] {50:51}
    :param r2: 나무 기둥 1m의 무게 최댓값 [int] {99:100}
    :param r3: 쇠기둥 5cm의 무게 최솟값 [int] {10:11}
    :param r4: 쇠기둥 5cm의 무게 최댓값 [int] {19:20}
    :param r5: 쇠기둥 Dcm의 무게 최솟값 [int] {10:11}
    :param r6: 쇠기둥 Dcm의 무게 최댓값 [int] {13:14}
    :param r7: 무게가 Ekg인 상자의 무게 최솟값 [int] {2:3}
    :param r8: 무게가 Ekg인 상자의 무게 최댓값 [int] {4:5}
    '''
    stem = "굵기가 일정한 나무 기둥 $$수식$$1` rm m$$/수식$$의 무게는 $$수식$${A}` rm kg$$/수식$$이고, 쇠기둥 $$수식$$5` rm {{cm}}$$/수식$$의 무게는 $$수식$${B}` rm kg$$/수식$$입니다. 나무 기둥 $$수식$$20` rm {{cm}}$$/수식$$와 쇠기둥 $$수식$${D}` rm {{cm}}$$/수식$$를 무게가 $$수식$${E}` rm kg$$/수식$$인 상자에 넣으면 모두 몇 $$수식$$rm kg$$/수식$$인지 구해 보세요.\n"
    answer = "(정답)\n$$수식$${S} rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$1` rm m$$/수식$$는 $$수식$$100` rm {{cm}}$$/수식$$이므로 $$수식$$20` rm {{cm}}$$/수식$$의 $$수식$$5$$/수식$$배입니다.\n" \
              "$$수식$$LEFT ($$/수식$$나무 기둥 $$수식$$20` rm m$$/수식$$의 무게$$수식$$RIGHT ) ` + ` LEFT ($$/수식$$쇠기둥 $$수식$${D}` rm {{cm}}$$/수식$$의 무게$$수식$$RIGHT ) ` + ` LEFT ($$/수식$$상자의 무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$=` {A} `DIVIDE` 5 `+` {B} `DIVIDE` 5 ` TIMES ` {D} `+` {E}$$/수식$$\n" \
              "$$수식$$=` {a} `+` {b} ` TIMES ` {D} `+` {E}$$/수식$$\n" \
              "$$수식$$=` {d} `+` {E} `=` {S} ` LEFT ( ` rm kg ` RIGHT )$$/수식$$\n\n"


    r1 = 50
    r2 = 100
    r3 = 10
    r4 = 20
    r5 = 10
    r6 = 14
    r7 = 2
    r8 = 5


    box = '□'

    flag = True
    while flag:
        A = random.randrange(r1, r2, 5)
        B = random.randrange(r3, r4, 5)
        D = random.randint(r5, r6)
        E = random.randint(r7, r8)

        if A % 5 == 0 and B % 5 == 0:
            a = A // 5
            b = B // 5
            c = b * D
            d = a + c
            S = d + E

            flag = False

    stem = stem.format(A=A, B=B, D=D, E=E)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, D=D, E=E, S=S, a=a, b=b, d=d)

    return stem, answer, comment























# if __name__ == '__main__':
#     # 강슬기
#     MixCalOfNatural_Stem_001()
#     MixCalOfNatural_Stem_002()
#     MixCalOfNatural_Stem_003()
#     MixCalOfNatural_Stem_004()
#     MixCalOfNatural_Stem_005()
#     MixCalOfNatural_Stem_006()
#     MixCalOfNatural_Stem_007()
#     MixCalOfNatural_Stem_008()
#     MixCalOfNatural_Stem_009()
#     MixCalOfNatural_Stem_010()
#     MixCalOfNatural_Stem_011()
#     MixCalOfNatural_Stem_012()
#     MixCalOfNatural_Stem_013()
#     MixCalOfNatural_Stem_014()
#     MixCalOfNatural_Stem_015()
#     MixCalOfNatural_Stem_016()
#     MixCalOfNatural_Stem_017()
#     MixCalOfNatural_Stem_018()
#     MixCalOfNatural_Stem_019()
#     MixCalOfNatural_Stem_020()
#
#     # 신현호
#     MixCalOfNatural_Stem_021()
#
#     # 강슬기
#     MixCalOfNatural_Stem_022()
#
#     # 신현호
#     MixCalOfNatural_Stem_023()
#     MixCalOfNatural_Stem_024()
#     MixCalOfNatural_Stem_025()
#     MixCalOfNatural_Stem_026()
#     MixCalOfNatural_Stem_027()
#
#     # 강슬기
#     MixCalOfNatural_Stem_028()
#     MixCalOfNatural_Stem_029()
#     MixCalOfNatural_Stem_030()
#
#     # 이명훈
#     MixCalOfNatural_Stem_031()
#     MixCalOfNatural_Stem_032()
#     MixCalOfNatural_Stem_033()
#     MixCalOfNatural_Stem_034()
#     MixCalOfNatural_Stem_035()
#     MixCalOfNatural_Stem_036()
#     MixCalOfNatural_Stem_037()
#     MixCalOfNatural_Stem_038()
#     MixCalOfNatural_Stem_039()
#     MixCalOfNatural_Stem_040()
#
#     # 지선영
#     MixCalOfNatural_Stem_041()
#     MixCalOfNatural_Stem_042()
#     MixCalOfNatural_Stem_043()
#     MixCalOfNatural_Stem_044()
#     MixCalOfNatural_Stem_045()
#     MixCalOfNatural_Stem_046()
#     MixCalOfNatural_Stem_047()
#     MixCalOfNatural_Stem_048()
#     MixCalOfNatural_Stem_049()
#     MixCalOfNatural_Stem_050()











