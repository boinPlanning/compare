import numpy as np
import random
import codecs
import os
import fractions




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
box_a = '㉠'
box_b = '㉡'
box_j1 = '㉠'
box_j2 = '㉡'
left = '&gt;'
right = '&lt;'
equal = '='




shapes = ['리본', '나비', '꽃']
lines = ['색 테이프', '줄', '종이끈']
juices = ['토마토 주스', '오렌지 주스', '망고 주스', '사과 주스', '포도 주스']




STEM_DICT_CAKE = ['케이크','식빵','떡',]
STEM_DICT_MAT = ['밀가루','쌀가루']
STEM_DICT_SHOP = ['제과점','방앗간']





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
    JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ',
                     'ㅅ',
                     'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    char_code = ord(name) - 44032
    ch1 = int(char_code / 588)
    ch2 = int((char_code - (588 * ch1)) / 28)
    ch3 = int((char_code - (588 * ch1) - (28 * ch2)))

    return JONGSUNG_LIST[ch3]












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
def get_gcd(num1, num2) :
    num1, num2 = sorted([num1, num2])
    gcd = 1
    for i in range(num1, 0, -1) :
        if num1 % i == 0 and num2 % i == 0 :
            gcd = i
            break

    return gcd














# 기약분수 여부 확인
def check_simFrac(num1, num2) :
    if get_gcd(num1, num2) == 1 :
        return True
    else :
        return False














def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a













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




def soroso(a, b):
    while True:
        rest_ab = max(a, b) % min(a, b)
        a = min(a, b)
        b = rest_ab

        if rest_ab == 0 or rest_ab == 1:
            break

    return rest_ab






def giyak(boon_ja, boon_mo):
    sample_frac = fractions.Fraction(boon_ja, boon_mo)
    giyak_boon_ja = sample_frac.numerator
    giyak_boon_mo = sample_frac.denominator

    return giyak_boon_ja, giyak_boon_mo









# 4-2-1-02
def fractionaddsub421_Stem_001():
    """

    :param r1: 분모의 범위 최솟값 [int] {4:5}
    :param r2: 분모의 범위 최댓값 [int] {18:19}
    :return:
    """
    stem = "크기를 비교하여 $$수식$${box}$$/수식$$ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${f1} ` + ` {f2} ~ {box} ~ {f3}$$/수식$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${f1} ` + ` {f2} ` = ` {c1} ` = ` {c2}$$/수식$$\n" \
              "따라서 $$수식$${c2} ` {ans} ` {f3}$$/수식$$이므로 $$수식$${f1} ` + ` {f2} ` {ans} ` {f3}$$/수식$$\n\n"



    r1 = 4
    r2 = 19


    while True:
        n1 = random.randint(r1, r2)
        n2, n3, n4 = random.sample(range(1, n1), 3)
        n2, n3, n4 = random.sample([i for i in range(1, 19) if i < n1], 3)

        if n1 < n2 + n3 < 2 * n1 and n1 % n2 != 0 and n1 % n3 != 0 and n1 % n4 != 0:
            if soroso(n1, n2) == 1 and soroso(n1, n3) == 1 and soroso(n1, n4) == 1:
                break


    f1 = "{%d} over {%d}" % (n2, n1)
    f2 = "{%d} over {%d}" % (n3, n1)
    f3 = "1 {%d} over {%d}" % (n4, n1)

    c1 = "{%d} over {%d}" % (n2 + n3, n1)
    c2 = "1 {%d} over {%d}" % (n2 + n3 - n1, n1)


    if (n2 + n3 - n1) < n4:
        ans = "&lt;"
    elif (n2 + n3 - n1) > n4:
        ans = "&gt;"
    else:
        ans = "="


    stem = stem.format(box=box, f1=f1, f2=f2, f3=f3)
    answer = answer.format(ans=ans)
    comment = comment.format(f1=f1, f2=f2, f3=f3, c1=c1, c2=c2, ans=ans)


    return stem, answer, comment






















# 4-2-1-03
def fractionaddsub421_Stem_002():
    """

    :param r1: 분모의 범위 최솟값 [int] {2:3}
    :param r2: 분모의 범위 최댓값 [int] {8:9}
    :return:
    """

    stem = "두 분수의 합을 구해 보세요.\n$$표$$$$수식$${f1}$$/수식$$    $$수식$${f2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$ 또는 $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${f1} ` + ` {f2} ` = ` {c1} LEFT ( = ` {ans1} RIGHT )$$/수식$$\n\n"



    r1 = 2
    r2 = 9


    while True:
        n1 = random.randint(r1, r2)
        n2, n3 = random.sample(range(r1, r2), 2)

        if n1 > n2 and n1 > n3 and n1 % n2 != 0 and n1 % n3 != 0 and (n2 + n3) % n1 == 0:
            break


    f1 = "{%d} over {%d}" % (n2, n1)
    f2 = "{%d} over {%d}" % (n3, n1)

    c1 = "{%d} over {%d}" % (n2 + n3, n1)
    ans1 = (n2 + n3) // n1
    ans2 = (n2 + n3)
    ans3 = n1

    a1 = ans1
    a2 = "{%s} over {%s}" % (ans2, ans3)


    stem = stem.format(f1=f1, f2=f2)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(f1=f1, f2=f2, c1=c1, ans1=ans1)


    return stem, answer, comment

























# 4-2-1-04
def fractionaddsub421_Stem_003():
    """

    :param r1: 분모의 범위 최솟값 [int] {5:6}
    :param r2: 분모의 범위 최댓값 [int] {8:9}
    :return:
    """
    stem = "$$수식$$㉠$$/수식$$에 알맞은 분수를 구해 보세요.\n$$수식$${f1}  `+ ` {c1} ` = ` {box_j1}$$/수식$$\n"
    answer = "(정답)\n$$수식$${final_ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${f1} ` + ` {c1} ` = ` {ans}{saying1}$$/수식$$\n\n"


    r1 = 5
    r2 = 10


    while True:
        n1 = random.randint(r1, r2)
        n2, n3 = random.sample(range(1, n1), 2)

        if n3 + n2 < n1:
            break


    f1 = "{%d} over {%d}" % (n2, n1)
    c1 = "{%d} over {%d}" % (n3, n1)
    ans = "{%d} over {%d}" % (n2 + n3, n1)

    giyak_boon_ja, giyak_boon_mo = giyak((n2+n3), n1)

    if giyak_boon_ja == (n2+n3) and giyak_boon_mo == n1:
        saying1 = ""
        final_ans = ans

    else:
        saying1 = "` = ` %s over %s" % (giyak_boon_ja, giyak_boon_mo)
        final_ans = "%s over %s" % (giyak_boon_ja, giyak_boon_mo)


    stem = stem.format(f1=f1, c1=c1, box_j1=box_j1)
    answer = answer.format(final_ans=final_ans)
    comment = comment.format(f1=f1, c1=c1, ans=ans, saying1=saying1)


    return stem, answer, comment

























# 4-2-1-05
def fractionaddsub421_Stem_004():
    """

    :param r1: 분모의 범위 최솟값 [int] {4:5}
    :param r2: 분모의 범위 최댓값 [int] {48:49}
    :return:
    """
    stem = "$$수식$$㉠$$/수식$$, $$수식$$㉡$$/수식$$에 알맞은 분수를 구해 보세요.\n$$수식$${f2} ` + ` {f1} ` = ` {box_j1}$$/수식$$\n$$수식$${f3} ` + ` {f1} ` = ` {box_j2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${final_ans1}$$/수식$$, $$수식$${final_ans2}$$/수식$$"
    comment = "(해설)\n" \
              "$$수식$$ ㉠ ~ {f2} ` + ` {f1} ` = ` {ans1}{saying1}$$/수식$$\n" \
              "$$수식$$ ㉡ ~ {f3} ` + ` {f1} ` = ` {ans2}{saying2}$$/수식$$\n\n"



    r1 = 4
    r2 = 49


    while True:
        n1 = random.randint(r1, r2)
        n2, n3, n4 = random.sample(range(1, n1), 3)

        if n2 + n3 < n1 and n2 + n4 < n1 and gcd(n1, n2) == 1 and gcd(n1, n3) == 1 and gcd(n1, n4) == 1:
            break


    f1 = "{%d} over {%d}" % (n2, n1)
    f2 = "{%d} over {%d}" % (n3, n1)
    f3 = "{%d} over {%d}" % (n4, n1)

    ans1 = "{%d} over {%d}" % (n2 + n3, n1)
    ans2 = "{%d} over {%d}" % (n2 + n4, n1)

    giyak1_boon_ja, giyak1_boon_mo = giyak((n2 + n3), n1)
    giyak2_boon_ja, giyak2_boon_mo = giyak((n2 + n4), n1)

    if giyak1_boon_ja == (n2 + n3) and giyak1_boon_mo == n1:
        saying1 = ""
        final_ans1 = ans1
    else:
        saying1 = "` = ` %s over %s" % (giyak1_boon_ja, giyak1_boon_mo)
        final_ans1 = "%s over %s" % (giyak1_boon_ja, giyak1_boon_mo)

    if giyak2_boon_ja == (n2 + n4) and giyak2_boon_mo == n1:
        saying2 = ""
        final_ans2 = ans2
    else:
        saying2 = "` = ` %s over %s" % (giyak2_boon_ja, giyak2_boon_mo)
        final_ans2 = "%s over %s" % (giyak2_boon_ja, giyak2_boon_mo)



    stem = stem.format(f1=f1, f2=f2, f3=f3, box_j1=box_j1, box_j2=box_j2)
    answer = answer.format(final_ans1=final_ans1, final_ans2=final_ans2)
    comment = comment.format(f1=f1, f2=f2, f3=f3, ans1=ans1, ans2=ans2, saying1=saying1, saying2=saying2)


    return stem, answer, comment



























# 4-2-1-06
def fractionaddsub421_Stem_005():
    """

    :param r1: 분모의 범위 최솟값 [int] {10:11}
    :param r2: 분모의 범위 최댓값 [int] {98:99}
    :return:
    """
    stem = "$$수식$$㉠$$/수식$$에 알맞은 대분수를 구해 보세요.\n$$표$$$$수식$${box_j1} ` - ` {f1} ` = ` {f2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${box_j1} ` - ` {f1} ` = ` {f2}$$/수식$$에서\n" \
              "$$수식$${box_j1} ` = ` {f1} ` + ` {f2} ` = ` {c1} ` = ` {c2}$$/수식$$입니다.\n\n"


    r1 = 10
    r2 = 99


    while True:
        n1 = random.randint(r1, r2)
        n2, n3 = random.sample(range(1, n1), 2)

        if n1 > n2 and n1 > n3 and n1 % n2 != 0 and n1 % n3 != 0 and n2 + n3 > n1:
            break


    f1 = "{%d} over {%d}" % (n2, n1)
    f2 = "{%d} over {%d}" % (n3, n1)
    c1 = "{%d} over {%d}" % (n2 + n3, n1)
    c2 = "%d {%d} over {%d}" % ((n2 + n3) // n1, (n2 + n3) % n1, n1)

    a1 = (n2 + n3) // n1
    a2 = (n2 + n3) % n1
    a3 = n1

    ans = "%s {%s} over {%s}" % (a1, a2, a3)

    giyak_boon_ja, giyak_boon_mo = giyak(a2, a3)
    ans = c2 = "%s {%s} over {%s}" % (a1, giyak_boon_ja, giyak_boon_mo)


    stem = stem.format(f1=f1, f2=f2, c1=c1, c2=c2, box_j1=box_j1)
    answer =answer.format(ans=ans)
    comment = comment.format(f1=f1, f2=f2, c1=c1, c2=c2, box_j1=box_j1)


    return stem, answer, comment

























# 4-2-1-07
def fractionaddsub421_Stem_006():
    """

    :param r1: 분모의 범위 최솟값 [int] {10:11}
    :param r2: 분모의 범위 최댓값 [int] {98:99}
    :return:
    """
    stem = "다음 중 가장 큰 수와 가장 작은 수의 합은 얼마인가요?\n$$표$$$$수식$${f1}$$/수식$$    $$수식$${f2}$$/수식$$    $$수식$${f3}$$/수식$$    $$수식$${f4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${final_ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "가장 큰 수는 $$수식$${c2}$$/수식$$이고 가장 작은 수는 $$수식$${c1}$$/수식$$입니다.\n" \
              "따라서 두 수의 합은 $$수식$${c2} ` + ` {c1} ` = ` {c3}{saying1}$$/수식$$입니다.\n\n"



    r1 = 10
    r2 = 100


    while True:
        n1 = random.randint(r1, r2)
        n2, n3, n4, n5 = random.sample(range(1, n1), 4)

        t_list = [n2, n3, n4, n5]
        t_list.sort()

        small = t_list[0]
        big = t_list[-1]

        if n1 > big + small and (big + small) % n1 != 0 and n1 % n2 != 0 and n1 % n3 != 0 and n1 % n4 != 0 and n1 % n5 != 0:
            break


    ans1 = big + small
    ans2 = n1


    ans = "{%s} over {%s}" % (ans1, ans2)


    f1 = "{%d} over {%d}" % (n2, n1)
    f2 = "{%d} over {%d}" % (n3, n1)
    f3 = "{%d} over {%d}" % (n4, n1)
    f4 = "{%d} over {%d}" % (n5, n1)

    c1 = "{%d} over {%d}" % (small, n1)
    c2 = "{%d} over {%d}" % (big, n1)
    c3 = "{%d} over {%d}" % (ans1, n1)

    giyak_boon_ja, giyak_boon_mo = giyak(ans1, n1)

    if giyak_boon_ja == ans1 and giyak_boon_mo == n1:
        saying1 = ""
        final_ans = ans
    else:
        saying1 = "` = ` %s over %s" % (giyak_boon_ja, giyak_boon_mo)
        final_ans = "%s over %s" % (giyak_boon_ja, giyak_boon_mo)


    stem = stem.format(f1=f1, f2=f2, f3=f3, f4=f4)
    answer = answer.format(final_ans=final_ans)
    comment = comment.format(c1=c1, c2=c2, c3=c3, saying1=saying1)


    return stem, answer, comment

























# 4-2-1-08
def fractionaddsub421_Stem_007():
    """

    :param r1: 분모의 범위 최솟값 [int] {10:11}
    :param r2: 분모의 범위 최댓값 [int] {98:99}
    :return:
    """
    stem = "{s1} 모양을 만드는 데 {s2}{j1} {name1}{j2} $$수식$${f1} ` rm m$$/수식$$, {name2}{j3} $$수식$${f2} ` rm m$$/수식$$ 사용하였습니다. {name1}{j4} {name2}{j5} 사용한 {s2}{j6} 모두 몇 $$수식$$rm m$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${ans} ` rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${name1}{j4} {name2}{j5} 사용한 {s2}$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$${name1}{j7} 사용한 {s2})$$수식$$` + ` LEFT ($$/수식$${name2}{j5} 사용한 {s2}$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {f1} ` + ` {f2} ` = ` {c1} ` = ` {ans} LEFT ( rm m RIGHT )$$/수식$$\n\n"


    r1 = 10
    r2 = 100


    shapes = ['리본', '나비', '꽃']
    lines = ['색 테이프', '줄', '종이끈']

    s1 = random.choice(shapes)
    s2 = random.choice(lines)
    name1, name2 = random.sample(person_yeo + person_nam, 2)

    if josa_check(s2[-1]) == ' ':
        j1 = '를'
        j6 = '는'
    else:
        j1 = '을'
        j6 = '은'

    if josa_check(name1[-1]) == ' ':
        j2 = '는'
        j4 = '와'
        j7 = '가'
    else:
        j2 = '이는'
        j4 = '이와'
        j7 = '이가'

    if josa_check(name2[-1]) == ' ':
        j3 = '는'
        j5 = '가'
    else:
        j3 = '이는'
        j5 = '이가'

    while True:
        n1 = random.randint(r1, r2)
        n2, n3 = random.sample(range(1, n1), 2)

        if n1 > n2 and n1 > n3 and n1 % n2 != 0 and n1 % n3 != 0 and n2 + n3 > n1:
            break

    f1 = "{%d} over {%d}" % (n2, n1)
    f2 = "{%d} over {%d}" % (n3, n1)
    c1 = "{%d} over {%d}" % (n2 + n3, n1)
    ans = "%d {%d} over {%d}" % ((n2 + n3) // n1, (n2 + n3) % n1, n1)

    giyak_boon_ja, giyak_boon_mo = giyak((n2 + n3) % n1, n1)
    ans = "%d {%d} over {%d}" % ((n2 + n3) // n1, giyak_boon_ja, giyak_boon_mo)

    stem = stem.format(f1=f1, f2=f2, s1=s1, s2=s2, name1=name1, name2=name2, j1=j1, j2=j2, j3=j3, j4=j4, j5=j5, j6=j6)
    answer = answer.format(ans=ans)
    comment = comment.format(name1=name1, name2=name2, s2=s2, j4=j4, j5=j5, j7=j7, f1=f1, f2=f2, c1=c1, ans=ans)

    return stem, answer, comment





















# 4-2-1-09
def fractionaddsub421_Stem_008():
    """

    :param r1: 분모의 범위 최솟값 [int] {2:3}
    :param r2: 분모의 범위 최댓값 [int] {28:29}
    :return:
    """
    stem = "다음 덧셈의 결과는 진분수입니다. $$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 중에서 $$수식$${b1}$$/수식$$ 안에 들어갈 수 있는 수는 모두 몇 개인가요?\n$$표$$$$수식$${f1} ` + ` {f2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${f1} ` + ` {f2} ` = ` {c1}$$/수식$$이고 덧셈의 계산 결과로 나올 수 있는 가장 큰 수는 $$수식$${c2}$$/수식$$입니다.\n" \
              "따라서 $$수식$${b1}$$/수식$$ 안에 들어갈 수 있는 수는 {c3}{j1} 모두 $$수식$${ans}$$/수식$$개입니다.\n\n"


    r1 = 2
    r2 = 29


    b1 = '□'

    while True:
        n1 = random.randint(r1, r2)
        n2 = random.choice(range(1, n1))

        f1 = '{%d} over {%d}' % (n2, n1)
        f2 = '{%s} over {%d}' % (b1, n1)
        c1 = '{%d `+` %s} over {%d}' % (n2, b1, n1)
        c2 = '{%d} over {%d}' % (n1 - 1, n1)

        if n1 > n2 + 2 and (n1 -1 ) < 10 and soroso(n1 -1, n1) == 1:
            break


    t_list = []
    for i in range(1, n1 - n2):
        t_list.append('$$수식$$%d$$/수식$$' % i)


    c3 = ', '.join(t_list)
    ans = len(t_list)
    j1 = num_josa(ans)[4]


    stem = stem.format(f1=f1, f2=f2, b1=b1)
    answer = answer.format(ans=ans)
    comment = comment.format(f1=f1, f2=f2, c1=c1, c2=c2, b1=b1, c3=c3, ans=ans, j1=j1)


    return stem, answer, comment





    # while True:
    #     n1 = random.randint(r1, r2)
    #     n2 = random.choice(range(1, n1))
    #
    #     if n1 > n2 + 2:
    #         break
    #
    # f1 = '{%d} over {%d}' % (n2, n1)
    # f2 = '{%s} over {%d}' % (b1, n1)
    # c1 = '{%d `+` %s} over {%d}' % (n2, b1, n1)
    # c2 = '{%d} over {%d}' % (n1 - 1, n1)




































# 4-2-1-10
def fractionaddsub421_Stem_009():
    """

    :param r1: 분모의 범위 최솟값 [int] {1:1}
    :param r2: 분모의 범위 최댓값 [int] {19:20}
    :return:
    """
    stem = "한 변이 $$수식$${f1} ` rm m$$/수식$$인 정사각형이 있습니다. 이 정사각형의 네 변의 길이의 합은 몇 $$수식$$rm m$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${ans} ` rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "정사각형의 네 변의 길이가 모두 같으므로\n" \
              "$$수식$${f1} ` + ` {f1} ` + ` {f1} ` + ` {f1} ` = ` {c1} ` = ` {ans} ` LEFT ( ` rm m RIGHT )$$/수식$$입니다.\n\n"


    r1 = 2
    r2 = 20


    while True:
        n1 = random.randint(r1, r2)
        n2 = random.randint(1, n1-1)

        if n2 < n1 < n2 * 4 and n1 % n2 != 0:
            break


    f1 = '{%d} over {%d}' % (n2, n1)
    c1 = '{%d} over {%d}' % (n2 * 4, n1)
    ans = '%d {%d} over {%d}' % ((n2 * 4) // n1, (n2 * 4) % n1, n1)

    giyak_boon_ja, giyak_boon_mo = giyak((n2 * 4) % n1, n1)
    ans = '%d {%d} over {%d}' % ((n2 * 4) // n1, giyak_boon_ja, giyak_boon_mo)

    stem = stem.format(f1=f1)
    answer = answer.format(ans=ans)
    comment = comment.format(f1=f1, c1=c1, ans=ans)


    return stem, answer, comment






















# 4-2-1-11
def fractionaddsub421_Stem_010():
    """

    :param r1: 분모의 범위 최솟값 [int] {3:4}
    :param r2: 분모의 범위 최댓값 [int] {28:29}
    :return:
    """
    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 중에서 $$수식$${box}$$/수식$$ 안에 들어갈 수 있는 수는 모두 몇 개인가요?\n$$표$$$$수식$${f1} `+` {f2} `&lt;` {f3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${f1} ` + ` {f2} ` = ` {c1}$$/수식$$이고 $$수식$${f3} ` = ` {c2}$$/수식$$이므로 $$수식$${c1} ` &lt; ` {c2}$$/수식$$ → $$수식$${c3} ` &lt; ` {c4}$$/수식$$입니다.\n" \
              "따라서 $$수식$${box}$$/수식$$ 안에 들어갈 수 있는 수는 {c5}{c5_josa} 모두 $$수식$${ans}$$/수식$$개입니다.\n\n"



    r1 = 3
    r2 = 29


    while True:
        n1 = random.randint(r1, r2)
        n2, n3 = random.sample(range(1, n1), 2)

        if n1 > n2 and n1 > n3 and n1 % n2 != 0 and n1 % n3 != 0 and 1 < n1 + n3 - n2 - 1 < 10 :
            break


    b1 = "□"

    f1 = "{%d} over {%d}" % (n2, n1)
    f2 = "{%s} over {%d}" % (b1, n1)
    f3 = "1 {%d} over {%d}" % (n3, n1)

    c1 = "{%d `+` %s} over {%d}" % (n2, b1, n1)
    c2 = "{%d} over {%d}" % (n1 + n3, n1)
    c3 = "%d `+` %s" % (n2, b1)
    c4 = n1 + n3

    ans = n1 + n3 - n2 - 1
    t_list = []


    for i in range(1, ans + 1):
        t_list.append("$$수식$$%d$$/수식$$" % i)

        if i == ans:
            c5_josa = num_josa(i)[4]


    c5 = ", ".join(t_list)


    stem =stem.format(box=box, f1=f1, f2=f2, f3=f3)
    answer = answer.format(ans=ans)
    comment = comment.format(box=box, f1=f1, f2=f2, f3=f3, c1=c1, c2=c2, c3=c3, c4=c4, ans=ans, c5=c5, c5_josa=c5_josa)


    return stem, answer, comment

























# 4-2-1-12
def fractionaddsub421_Stem_011():
    """

    :param r1: 분모의 범위 최솟값 [int] {3:4}
    :param r2: 분모의 범위 최댓값 [int] {29:30}
    :return:
    """
    stem = "{name1}{j1} {s1}를 어제는 $$수식$${f1} ` rm L$$/수식$$ 마셨고 오늘은 어제보다 $$수식$${f2} ` rm L$$/수식$$ 더 많이 마셨습니다. {name1}{j2} 어제와 오늘 마신 {s1}는 모두 몇 $$수식$$rm L$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${ans} ` rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${name1}{j2} 오늘 마신 주스의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {f1} ` + ` {f2} ` = ` {c1} LEFT ( rm L RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${name1}{j2} 어제 오늘 마신 주스의 양의 합$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {f1} ` + ` {c1} ` = ` {c2} ` = ` {ans} LEFT ( rm L RIGHT )$$/수식$$\n\n"



    r1 = 3
    r2 = 30


    while True:
        n1 = random.randint(r1, r2)
        n2, n3 = random.sample(range(1, n1), 2)

        if n1 > n2 and n1 > n3 and  2 * n1 > n2 + n3 + n2 > n1 and n1 % n2 != 0 and n1 % n3 != 0\
                and check_simFrac(n1, n2) and check_simFrac(n1, n3) :
            break


    f1 = "{%d} over {%d}" % (n2, n1)
    f2 = "{%d} over {%d}" % (n3, n1)
    c1 = "{%d} over {%d}" % (n2 + n3, n1)
    c2 = "{%d} over {%d}" % (n2 + n2 + n3, n1)
    ans = "%d {%d} over {%d}" % ((n2 + n2 + n3) // n1, (n2 + n2 + n3) % n1, n1)


    giyak_boon_ja, giyak_boon_mo = giyak((n2 + n2 + n3) % n1, n1)
    ans = "%d {%d} over {%d}" % ((n2 + n2 + n3) // n1, giyak_boon_ja, giyak_boon_mo)


    name1 = random.choice(person_nam + person_yeo)
    s1 = random.choice(juices)


    if josa_check(name1[-1]) == ' ':
        j1 = '는'
        j2 = '가'
    else:
        j1 = '이는'
        j2 = '이가'


    stem = stem.format(f1=f1, f2=f2, name1=name1, j1=j1, j2=j2, s1=s1)
    answer= answer.format(ans=ans)
    comment = comment.format(c1=c1, c2=c2, ans=ans, name1=name1, j2=j2, f1=f1, f2=f2)


    return stem, answer, comment























# 4-2-1-14
def fractionaddsub421_Stem_012():
    """

    :param r1: 분모의 범위 최솟값 [int] {10:11}
    :param r2: 분모의 범위 최댓값 [int] {98:99}
    :return:
    """
    stem = "㉠에 알맞은 수를 구해 보세요.\n$$수식$${s1} ` - ` {s2} ` = ` {box_j1}$$/수식$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${c1} ` - ` {c2} ` = ` {ans}$$/수식$$\n\n"



    r1 = 10
    r2 = 99


    while True:
        n1 = random.randint(r1, r2)
        n2, n3 = random.sample(range(1, n1), 2)

        if n1 > n2 > n3 and n1 % n2 != 0 and n1 % n3 != 0 and check_simFrac(n2-n3, n1):
            break


    s1 = "{%d} over {%d}" % (n2, n1)
    s2 = "{%d} over {%d}" % (n3, n1)

    c1 = "{%d} over {%d}" % (n2, n1)
    c2 = "{%d} over {%d}" % (n3, n1)
    ans = "{%d} over {%d}" % (n2 - n3, n1)


    stem = stem.format(s1=s1, s2=s2, box_j1=box_j1)
    answer = answer.format(ans=ans)
    comment = comment.format(c1=c1, c2=c2, ans=ans)


    return stem, answer, comment






















# 4-2-1-15
def fractionaddsub421_Stem_013():
    """

    :param r1: 분자, 분모의 범위 최솟값 [int] {10:11}
    :param r2: 분자, 분모의 범위 최댓값 [int] {98:99}
    :return:
    """
    stem = "두 수의 차를 구해보세요.\n$$표$$$$수식$${f1}$$/수식$$    $$수식$${f2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${f1} ` - ` {f2} ` = ` {c1} ` = ` {ans}$$/수식$$"



    r1 = 10
    r2 = 99


    while True:
        n1 = random.randint(r1, r2)
        n2, n3 = random.sample(range(1, n1), 2)

        if n3 < n2 < n1 and n1 % n2 != 0 and n1 % n3 != 0 and check_simFrac(n2-n3, n1):
            break


    f1 = "{%d} over {%d}" % (n2, n1)
    f2 = "{%d} over {%d}" % (n3, n1)

    c1 = "{%d `-` %d} over {%d}" % (n2, n3, n1)
    ans = "{%d} over {%d}" % (n2 - n3, n1)


    stem = stem.format(f1=f1, f2=f2)
    answer = answer.format(ans=ans)
    comment = comment.format(f1=f1, f2=f2, c1=c1, ans=ans)


    return stem, answer, comment























# 4-2-1-16
def fractionaddsub421_Stem_014():
    stem = "계산 결과를 비교하여 $$수식$${box}$$/수식$$ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$표$$$$수식$${problem1}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_sign}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$,\n" \
              "$$수식$${explain2}$$/수식$$\n" \
              "따라서 $$수식$${explain3}$$/수식$$이므로 $$수식$${explain4}$$/수식$$입니다.\n\n"


    while 1:
        num1 = random.randint(4, 30)
        num2, num3, num4 = random.sample(range(1, num1), 3)
        num5 = random.randint(1, num1 - 1)
        if is_gcd(num1, num2) and is_gcd(num1, num3):
            lst = [num2, num3, num4, num5]
            lst.sort(reverse=True)
            num2, num4, num3, num5 = lst
            num6, num7 = num2 - num3, num4 - num5
            if is_gcd(num1, num6) and is_gcd(num1, num7):
                break


    equ1 = '{0} over {1} ` - ` {2} over {3}'.format(num2, num1, num3, num1)
    equ2 = '{0} over {1} ` - ` {2} over {3}'.format(num4, num1, num5, num1)
    problem1 = '{0} ```` {1} ```` {2}'.format(equ1, box, equ2)


    explain1 = '{0} ` = ` {{ {1} ` - ` {2} }} over {3} ` = ` {4} over {3}'.format(equ1, num2, num3, num1, num6)
    explain2 = '{0} ` = ` {{ {1} ` - ` {2} }} over {3} ` = ` {4} over {3}'.format(equ2, num4, num5, num1, num7)


    answer_sign = '&gt;' if num6 > num7 else '&lt;' if num6 < num7 else '='
    explain3 = '{0} over {1} ` {2} ` {3} over {1}'.format(num6, num1, answer_sign, num7, num1)
    explain4 = '{0} ` {1} ` {2}'.format(equ1, answer_sign, equ2)


    stem = stem.format(problem1=problem1, box=box)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4)


    return stem, answer, comment

























# 4-2-1-17
def fractionaddsub421_Stem_015():
    stem = "계산 결과가 더 작은 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$       ㉡ $$수식$${problem2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{answer_sign}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${explain1}$$/수식$$\n" \
              "㉡ $$수식$${explain2}$$/수식$$\n" \
              "따라서 $$수식$${explain3}$$/수식$$이므로 계산 결과가 더 작은 것은 {answer_sign}입니다.\n\n"


    while 1:
        num1 = random.randint(10, 20)
        num2, num3, num4 = random.sample(range(2, num1), 3)
        num5 = random.randint(1, num1 - 1)
        if is_gcd(num1, num2) and is_gcd(num1, num3) and is_gcd(num1, num3) and is_gcd(num1, num3):
            lst = [num2, num3, num4, num5]
            lst.sort(reverse=True)
            num2, num4, num3, num5 = lst
            num6, num7 = num2 - num3, num4 - num5
            if is_gcd(num1, num6) and is_gcd(num1, num7) and num6 != num7:
                break


    problem1 = '{0} over {1} ` - ` {2} over {3} '.format(num2, num1, num3, num1)
    problem2 = '{0} over {1} ` - ` {2} over {3} '.format(num4, num1, num5, num1)


    explain1 = '{0} ` = ` {{ {1} ` - ` {2} }} over {3} ` = ` {4} over {3}'.format(problem1, num2, num3, num1, num6)
    explain2 = '{0} ` = ` {{ {1} ` - ` {2} }} over {3} ` = ` {4} over {3}'.format(problem2, num4, num5, num1, num7)


    sign = '&gt;' if num6 > num7 else '&lt;'
    answer_sign = '㉠' if num6 < num7 else '㉡'
    explain3 = '{0} over {1} ` {2} ` {3} over {1}'.format(num6, num1, sign, num7, num1)


    stem = stem.format(problem1=problem1, problem2=problem2)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, answer_sign=answer_sign)


    return stem, answer, comment























# 4-2-1-18
def fractionaddsub421_Stem_016():
    stem = "㉠에 알맞은 수를 구해 보세요.\n$$표$$$$수식$${problem1}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$\n\n"


    while 1:
        num1 = random.randint(2, 9)
        num2 = random.randint(1, num1 - 1)
        if is_gcd(num1, num2):
            break

    num3 = num1 - num2

    problem1 = '1 ` - ` {0} over {1} ` = ` {2}'.format(num2, num1, box_j1)
    answer_num = '{0} over {1}'.format(num3, num1)

    explain1 = '{0} ` = ` {1} over {1} ` - ` {2} over {1} ` = ` {{ {1} ` - ` {2} }} over {1} ` = ` {3} over {1}'\
        .format(problem1, num1, num2, num3)


    stem = stem.format(problem1=problem1, box_a=box_a)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1)


    return stem, answer, comment

























# 4-2-1-19
def fractionaddsub421_Stem_017():
    stem = "다음 두 분수의 차를 구해 보세요.\n$$표$$$$수식$$1$$/수식$$    $$수식$${problem1}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$\n\n"


    while 1:
        num1 = random.randint(10, 20)
        num2 = random.randint(1, num1 - 1)
        num3 = num1 - num2
        if is_gcd(num1, num2) and is_gcd(num1, num3):
            break


    problem1 = '{0} over {1}'.format(num2, num1)


    explain1 = '1 ` - ` {0} ` = ` {1} over {1} ` - ` {2} over {1} ` = ` {{ {1} ` - ` {2} }} over {1} ` = ` {3} over {1}'\
        .format(problem1, num1, num2, num3)


    answer_num = '{0} over {1}'.format(num3, num1)


    stem = stem.format(problem1=problem1)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1)


    return stem, answer, comment
























# 4-2-1-20
def fractionaddsub421_Stem_018():
    stem = "㉠과 ㉡의 차는 얼마인가요?\n$$표$$㉠ $$수식$${problem1}$$/수식$${j1} $$수식$${problem2}$$/수식$$개인 수    ㉡ $$수식$$1$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${explain1}$$/수식$${j1} $$수식$${explain2}$$/수식$$개인 수는 $$수식$${explain3}$$/수식$$입니다.\n" \
              "따라서 ㉠과 ㉡의 차는\n" \
              "$$수식$${explain4}$$/수식$$\n\n"


    while 1:
        num1 = random.randint(10, 20)
        num2 = random.randint(1, 5)
        num3 = random.choice([i for i in range(1, num1 // num2)])
        if is_gcd(num1, num2):
            result = num1 - (num2 * num3)
            if is_gcd(num1, result) and result > 0:
                break

    problem1 = '{0} over {1}'.format(num2, num1)
    problem2 = num3

    j1 = '이' if (num2 % 10) in have_jongsung_num else '가'

    explain1 = problem1
    explain2 = num3

    explain3 = '{0} over {1}'.format(num2 * num3, num1)
    explain4 = '1 ` - ` {0} ` = ` {1} over {1} ` - ` {2} over {1} ` = ` {{ {1} ` - ` {2} }} over {1} ` = ` {3} over {1} '\
        .format(explain3, num1, num2 * num3, result)

    answer_num = '{0} over {1}'.format(result, num1)


    stem = stem.format(problem1=problem1, problem2=problem2, j1=j1)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4, j1=j1)


    return stem, answer, comment
























# 4-2-1-21
def fractionaddsub421_Stem_019():
    stem = "계산 결과가 가장 큰 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$    ㉡ $$수식$${problem2}$$/수식$$    ㉢ $$수식$${problem3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{answer_sign}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${explain1}$$/수식$$\n" \
              "㉡ $$수식$${explain2}$$/수식$$\n" \
              "㉢ $$수식$${explain3}$$/수식$$\n" \
              "따라서 $$수식$${explain4}$$/수식$$이므로 계산 결과가 가장 큰 것은 {answer_sign}입니다.\n\n"


    while 1:
        num1, num2 = random.sample(range(10, 20), 2)
        tmp_num = random.randint(1, num2 - 2)
        if is_gcd(tmp_num, num2) and is_gcd(num2 - tmp_num, num2):
            break

    tmp = [[num1, num1 - 1, 1 / num1],
           [num2, tmp_num, (num2 - tmp_num) / num2],
           [num2, num2 - 1, 1 / num2]]

    random.shuffle(tmp)

    tmp[0].append(0)
    tmp[1].append(1)
    tmp[2].append(2)

    num1, num3, num5 = tmp[0][0], tmp[1][0], tmp[2][0]
    num2, num4, num6 = tmp[0][1], tmp[1][1], tmp[2][1]


    problem1 = '1 ` - ` {0} over {1}'.format(num2, num1)
    problem2 = '1 ` - ` {0} over {1}'.format(num4, num3)
    problem3 = '1 ` - ` {0} over {1}'.format(num6, num5)


    explain1 = '{0} ` = ` {1} over {1} ` - ` {2} over {1} ` = ` {{ {1} ` - ` {2} }} over {1} ` = ` {3} over {1}'\
        .format(problem1, num1, num2, num1 - num2)
    explain2 = '{0} ` = ` {1} over {1} ` - ` {2} over {1} ` = ` {{ {1} ` - ` {2} }} over {1} ` = ` {3} over {1}' \
        .format(problem2, num3, num4, num3 - num4)
    explain3 = '{0} ` = ` {1} over {1} ` - ` {2} over {1} ` = ` {{ {1} ` - ` {2} }} over {1} ` = ` {3} over {1}' \
        .format(problem3, num5, num6, num5 - num6)


    tmp.sort(key=lambda x: x[2])


    num1, num3, num5 = tmp[0][0], tmp[1][0], tmp[2][0]
    num2, num4, num6 = tmp[0][1], tmp[1][1], tmp[2][1]
    explain4 = '{0} over {1} ` &lt; ` {2} over {3} ` &lt; ` {4} over {5}'\
        .format(num1 - num2, num1, num3 - num4, num3, num5 - num6, num5)


    sign_lst = ['㉠', '㉡', '㉢']
    answer_sign = sign_lst[tmp[2][3]]


    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             answer_sign=answer_sign)


    return stem, answer, comment



















# 4-2-1-22
def fractionaddsub421_Stem_020():
    stem = "분모가 $$수식$${problem1}$$/수식$$인 진분수가 $$수식$$2$$/수식$$개 있습니다. 합이 $$수식$${problem2}$$/수식$$, 차가 $$수식$${problem3}$$/수식$$인 두 진분수를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${answer_num1}$$/수식$$, $$수식$${answer_num2}$$/수식$$\n"
    comment = "(해설)\n" \
              "분모가 같은 분수의 덧셈과 뺄셈은 분모는 그대로 두고 분자끼리 더하고 빼어 계산합니다.\n" \
              "분자의 합이 $$수식$${explain1}$$/수식$$이고 차가 $$수식$${explain2}$$/수식$$인 두 수를 찾습니다.\n" \
              "$$수식$${explain3}$$/수식$$, $$수식$${explain4}$$/수식$$이므로 두 진분수는 " \
              "$$수식$${answer_num1}$$/수식$$, $$수식$${answer_num2}$$/수식$$입니다.\n\n"


    while True:
        num1 = random.randint(3, 30)
        num2 = random.randint(2, num1 - 1)
        num4 = random.randint(1, num2 - 1)
        num5 = num2 - num4
        if num4 > num5:
            num4, num5 = num5, num4
        num3 = num5 - num4

        if num3 != 0 and soroso(num4, num1) == 1 and soroso(num5, num1) == 1:
            problem1 = num1
            problem2 = '{0} over {1}'.format(num2, num1)
            problem3 = '{0} over {1}'.format(num3, num1)
            explain1, explain2 = num2, num3
            explain3 = '{0} ` + ` {1} ` = ` {2}'.format(num4, num5, num2)
            explain4 = '{0} ` - ` {1} ` = ` {2}'.format(num5, num4, num3)
            answer_num1 = '{0} over {1}'.format(num4, num1)
            answer_num2 = '{0} over {1}'.format(num5, num1)
            break


    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3)
    answer = answer.format(answer_num1=answer_num1, answer_num2=answer_num2)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             answer_num1=answer_num1, answer_num2=answer_num2)


    return stem, answer, comment






















# 4-2-1-23
def fractionaddsub421_Stem_021():
    stem = "{obj} $$수식$$1 ` rm L$$/수식$$를 어제는 $$수식$${problem1} ` rm L$$/수식$$, 오늘은 $$수식$${problem2} ` rm L$$/수식$$ 마셨습니다. 남은 {obj}{post} 몇 $$수식$$rm L$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${answer_num}` rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$어제 마시고 남은 {obj}의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${explain1} LEFT ( rm L RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$오늘 마시고 남은 {obj}의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${explain2} LEFT ( rm L RIGHT )$$/수식$$\n" \
              "따라서 남은 {obj}의 양은 $$수식$${answer_num} ` rm L$$/수식$$입니다.\n\n"


    obj = random.choice(['주스', '우유', '물'])
    post = '는' if josa_check(obj[-1]) == ' ' else '은'

    while 1:
        num1 = random.randint(3, 30)
        num2 = random.randint(1, num1 - 2)
        num3 = random.randint(1, num1 - num2 - 1)
        num4 = num1 - num2 - num3
        if is_gcd(num1, num2) and is_gcd(num1, num3) and is_gcd(num1, num4):
            break


    problem1 = '{0} over {1}'.format(num2, num1)
    problem2 = '{0} over {1}'.format(num3, num1)


    explain1 = '` = ` 1 ` - ` {0} over {1} ` = ` {1} over {1} ` - ` {0} over {1} ` = ` {{ {1} ` - ` {0} }} over {1} ' \
               '` = ` {2} over {1}'.format(num2, num1, num1 - num2)
    explain2 = '` = ` {0} over {1} ` - ` {2} over {1} ` = ` {{ {0} ` - ` {2} }} over {1} ` = ` {3} over {1}'\
        .format(num1 - num2, num1, num3, num4)
    answer_num = '{0} over {1}'.format(num4, num1)


    stem = stem.format(problem1=problem1, problem2=problem2, obj=obj, post=post)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, answer_num=answer_num, obj=obj)


    return stem, answer, comment























# 4-2-1-24
def fractionaddsub421_Stem_022():
    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 중에서 $$수식$${box}$$/수식$$ 안에 들어갈 수 있는 수는 모두 몇 개인가요?\n$$표$$$$수식$${problem1}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$이고\n" \
              "$$수식$${explain2}$$/수식$$에서 $$수식$${explain3}$$/수식$$입니다.\n" \
              "따라서 $$수식$${box}$$/수식$$ 안에 들어갈 수 있는 수는 {explain4}{post} 모두 " \
              "$$수식$${answer_num}$$/수식$$개입니다.\n\n"


    while 1:
        num1 = random.randint(10, 20)
        num2 = random.randint(2, num1 - 1)
        num3 = random.randint(1, num2 - 1)
        num4 = num2 - num3
        if is_gcd(num1, num2) and is_gcd(num1, num3) and 2 < num4 < 6:
            break

    problem1 = '{0} over {1} ` - ` {{□}} over {1} ` &gt; ` {3} over {1}'.format(num2, num1, box, num3)

    explain1 = '{0} over {1} ` - ` {{□}} over {1} ` = ` {{ {0} ` - ` {{□}} }} over {1}'.format(num2, num1, box)
    explain2 = '{{ {0} ` - ` {1} }} over {2} ` &gt; ` {3} over {2}'.format(num2, box, num1, num3)
    explain3 = '{0} ` - ` {1} ` &gt; ` {2}'.format(num2, box, num3)


    lst = [str(i) for i in range(1, num2 - num3)]

    explain4 = '$$수식$$'
    explain4 += '$$/수식$$, $$수식$$'.join(lst)
    explain4 += '$$/수식$$'

    answer_num = len(lst)
    post = postposition(int(lst[-1]), flag=3)


    stem = stem.format(problem1=problem1, box=box)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             answer_num=answer_num, post=post, box=box)


    return stem, answer, comment























# 4-2-1-26
def fractionaddsub421_Stem_023():
    stem = "㉠에 알맞은 수를 구해 보세요.\n$$표$$$$수식$${problem1}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$\n" \
              "$$수식$$= ` {explain2}$$/수식$$\n\n"


    num1, num2 = random.sample(list(range(1, 11)), 2)

    while 1:
        num3 = random.randint(3, 30)
        num4 = random.randint(1, num3 - 2)
        num5 = random.randint(1, num3 - num4 - 1)

        r1, r2 = num1 + num2, num4 + num5

        if num1 == num2 and num4 == num5:
            continue

        if is_gcd(num3, num4) and is_gcd(num3, num5) and soroso(r2, num3) == 1:
            break

    problem1 = '{0} {1} over {2} ` + ` {3} {4} over {2} ` = ` {5}'.format(num1, num4, num3, num2, num5, box_j1)
    answer_num = '{0} {1} over {2}'.format(r1, r2, num3)

    explain1 = '{0} ` = ` LEFT ( {1} ` + ` {2} RIGHT ) ` + ` LEFT ( {3} over {4} ` + ` {5} over {4} RIGHT )'\
        .format(problem1, num1, num2, num4, num3, num5)

    explain2 = '{0} ` + ` {1} over {2} ` = ` {3}'.format(r1, r2, num3, answer_num)


    stem = stem.format(problem1=problem1, box_a=box_a)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2)


    return stem, answer, comment






















# 4-2-1-27
def fractionaddsub421_Stem_024():
    stem = "다음 두 분수의 합을 구해 보세요.\n$$표$$$$수식$${problem1}$$/수식$$    $$수식$${problem2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$\n" \
              "$$수식$${explain2}$$/수식$$\n\n"


    while 1:
        num1 = random.randint(1, 10)
        num4 = random.randint(1, 10)
        num2 = random.randint(3, 30)

        num3 = random.randint(1, num2 - 2)
        num5 = random.randint(1, num2 - num3 - 1)

        if is_gcd(num1, num2) and is_gcd(num1, num3) and is_gcd(num1, num5) and not (num1 == num4 and num3 == num5) and soroso(num3 + num5, num2) == 1:
            break


    problem1 = '{0} {1} over {2}'.format(num1, num3, num2)
    problem2 = '{0} {1} over {2}'.format(num4, num5, num2)

    explain1 = '{0} `+` {1} `=` LEFT ( {2} `+` {3} RIGHT ) `+` LEFT (  {4} over {5} `+` {6} over {5} RIGHT )'\
        .format(problem1, problem2, num1, num4, num3, num2, num5)

    explain2 = '=` {0} `+` {1} over {2} `=` {0} {1} over {2}'.format(num1 + num4, num3 + num5, num2)

    answer_num = '{0} {1} over {2}'.format(num1 + num4, num3 + num5, num2)


    stem = stem.format(problem1=problem1, problem2=problem2)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2)


    return stem, answer, comment




























# 4-2-1-28
def fractionaddsub421_Stem_025():
    stem = "계산 결과가 잘못된 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$    ㉡ $$수식$${problem2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{answer_sign}\n"
    comment = "(해설)\n" \
              "{answer_sign} $$수식$${explain1}$$/수식$$\n" \
              "$$수식$${explain2}$$/수식$$\n\n"


    while True:
        r1 = random.randint(4, 10)
        num1, num5 = random.sample(range(1, r1 - 1), 2)
        num2, num6 = r1 - num1, r1 - num5


        while 1:
            num = random.randint(5, 30)
            num3, num7 = random.sample(range(2, num - 1), 2)
            num4 = random.randint(1, num - num3)
            num8 = random.randint(2, num - num7)
            if (num1 == num2 and num3 == num4) or (num5 == num6 and num7 == num8):
                continue
            if is_gcd(num, num3) and is_gcd(num, num4) and is_gcd(num, num3 + num4) \
                    and is_gcd(num, num7) and is_gcd(num, num8) and is_gcd(num, num7 + num8) and (num3 != num8 and num7 != num4):
                break


        problem1 = '{0} {1} over {2} ` + ` {3} {4} over {2} ` = ` {5} {6} over {2}'\
            .format(num1, num3, num, num2, num4, r1, num3 + num4)

        random_num = random.choice([i for i in range(1, num7 + num8) if i != num7])

        problem2 = '{0} {1} over {2} ` + ` {3} {4} over {2} ` = ` {5} {6} over {2}' \
            .format(num5, num7, num, num6, num8, r1, random_num)

        explain1 = '{0} {1} over {2} ` + ` {3} {4} over {2} ` = ` LEFT ( {0} ` + ` {3} RIGHT ) ` + ` ' \
                   'LEFT ( {1} over {2} ` + ` {4} over {2} RIGHT )' \
            .format(num5, num7, num, num6, num8)

        explain2 = '=` {0} ` + ` {1} over {2} ` = ` {0} {1} over {2}'.format(r1, num7 + num8, num)

        if soroso(random_num, num) == 1 and (num7 + num8) - 2 <= random_num and random_num <= (num7 + num8) + 2:
            break


    lst = [[problem1, 0], [problem2, 1]]
    random.shuffle(lst)
    problem1, problem2 = lst[0][0], lst[1][0]


    for idx, x in enumerate(lst):
        if x[1] == 1:
            answer_sign = '㉠' if idx == 0 else '㉡'


    stem = stem.format(problem1=problem1, problem2=problem2)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2, answer_sign=answer_sign)


    return stem, answer, comment






























# 4-2-1-29
def fractionaddsub421_Stem_026():
    stem = "다음 수를 구해 보세요.\n$$표$$$$수식$${problem1}$$/수식$$보다 $$수식$${problem2}$$/수식$$ 큰 수$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$보다 $$수식$${explain2}$$/수식$$ 큰 수는 덧셈을 이용합니다.\n" \
              "$$수식$${explain3}$$/수식$$\n" \
              "$$수식$${explain4}$$/수식$$\n\n"


    num1 = random.randint(1, 10)
    num4 = random.randint(1, 10)

    while 1:
        num2 = random.randint(3, 30)
        num3 = random.randint(1, num2 - 2)
        num5 = random.randint(1, num2 - num3 - 1)
        num6 = num3 + num5
        if is_gcd(num2, num3) and is_gcd(num2, num6) and is_gcd(num2, num5) and not (num1 == num4 and num3 == num5):
            break

    problem1 = '{0} {1} over {2}'.format(num1, num3, num2)
    problem2 = '{0} {1} over {2}'.format(num4, num5, num2)

    explain1, explain2 = problem1, problem2

    explain3 = '{0} ` + ` {1} ` = ` LEFT ( {2} ` + ` {3} RIGHT ) ` + ` LEFT ( {4} over {5} ` + ` {6} over {5} RIGHT )'\
        .format(problem1, problem2, num1, num4, num3, num2, num5)

    explain4 = '= ` {0} ` + ` {1} over {2} ` = ` {0} {1} over {2}'.format(num1 + num4, num6, num2)
    answer_num = '{0} {1} over {2}'.format(num1 + num4, num6, num2)


    stem = stem.format(problem1=problem1, problem2=problem2)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4)


    return stem, answer, comment
























# 4-2-1-30
def fractionaddsub421_Stem_027():
    '''
    :param r1: 분모의 최솟값 [int] {2:3}
    :param r2: 분모의 최댓값 [int] {29:30}
    :param r3: 자연수의 최솟값 [int] {2:3}
    :param r4: 자연수의 최댓값 [int] {9:10}
    '''
    stem = "계산 결과가 더 큰 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${saying1}$$/수식$$    ㉡ $$수식$${saying2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "㉠ {saying1_comment}\n" \
              "㉡ {saying2_comment}\n\n"



    r1 = 2
    r2 = 30
    r3 = 2
    r4 = 10


    flag = True

    while flag:
        B = random.randint(r1, r2)
        C, E, G, I = np.random.choice(list(range(1, B)), 4)

        if C + E < B and G + I < B and C + E < G + 1:
            A, D, F, H = np.random.choice(list(range(r3, r4+1)), 4)

            if A + D < F + H:
                J = A + D
                K = C + E
                L = F + H
                M = G + I

                Frac_1 = "%s {%s} over {%s} ` + ` %s {%s} over {%s}" % (A, C, B, D, E, B)
                Frac_2 = "%s {%s} over {%s} ` + ` %s {%s} over {%s}" % (F, G, B, H, I, B)
                Frac_3 = "{%s} over {%s} ` + ` {%s} over {%s}" % (C, B, E, B)

                Frac_4 = "{%s} over {%s}" % (K, B)
                Frac_5 = "{%s} over {%s} ` + ` {%s} over {%s}" % (G, B, I, B)
                Frac_6 = "{%s} over {%s}" % (M, B)

                if soroso(K, B) == 1 and soroso(M, B) == 1:
                    flag = False

    choice_shuffle = np.random.randint(0, 2)

    if choice_shuffle == 0:
        saying1 = Frac_1
        saying1_comment = f"$$수식$${Frac_1} ` = ` LEFT ( {A} ` + ` {D} RIGHT ) ` + ` LEFT ( {Frac_3} RIGHT )$$/수식$$\n" \
                          f"$$수식$$= ` {J} ` + ` {Frac_4} ` = ` {J} {Frac_4}$$/수식$$\n"
        saying2 = Frac_2
        saying2_comment = f"$$수식$${Frac_2} ` = ` LEFT ( {F} ` + ` {H} RIGHT ) ` + ` LEFT ( {Frac_5} RIGHT )$$/수식$$\n" \
                          f"$$수식$$= ` {L} ` + ` {Frac_6} ` = ` {L} {Frac_6}$$/수식$$\n"
        ans = "㉡"

    else:
        saying1 = Frac_2
        saying1_comment = f"$$수식$${Frac_2} ` = ` LEFT ( {F} ` + ` {H} RIGHT ) ` + ` LEFT ( {Frac_5} RIGHT )$$/수식$$\n" \
                          f"$$수식$$= ` {L} ` + ` {Frac_6} ` = ` {L} {Frac_6} $$/수식$$"
        saying2 = Frac_1
        saying2_comment = f"$$수식$${Frac_1} ` = ` LEFT ( {A} ` + ` {D} RIGHT ) ` + ` LEFT ( {Frac_3} RIGHT )$$/수식$$\n" \
                          f"$$수식$$= ` {J} ` + ` {Frac_4} ` = ` {J} {Frac_4} $$/수식$$"
        ans = "㉠"


    stem = stem.format(saying1=saying1, saying2=saying2)
    answer = answer.format(ans=ans)
    comment = comment.format(saying1_comment=saying1_comment, saying2_comment=saying2_comment)


    return stem, answer, comment

























# 4-2-1-32
def fractionaddsub421_Stem_028():
    '''
    :param r1: 분모의 최솟값 [int] {2:3}
    :param r2: 분모의 최댓값 [int] {29:30}
    :param r3: 자연수의 최솟값 [int] {2:3}
    :param r4: 자연수의 최댓값 [int] {9:10}
    '''
    stem = "㉠과 ㉡에 알맞은 수를 구해 보세요.\n$$수식$${Frac_1} ` + ` {Frac_2} ` = ` {box_j1}$$/수식$$\n$$수식$${box_j1} ` + ` {Frac_3} ` = ` {box_j2}$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${H} {Frac_6}$$/수식$$, ㉡ $$수식$${J} {Frac_8}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${Frac_1} ` + ` {Frac_2} ` = ` LEFT ( {A} ` + ` {D} RIGHT ) ` + ` LEFT ( {Frac_4} ` + ` {Frac_5} RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {H} ` + ` {Frac_6} ` = ` {H} {Frac_6}$$/수식$$\n" \
              "㉡ $$수식$${H} {Frac_6} ` + ` {Frac_3} ` = ` LEFT ( {H} ` + ` {F} RIGHT ) ` + ` LEFT ( {Frac_6} ` + ` {Frac_7} RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {J} ` + ` {Frac_8} ` = ` {J} {Frac_8}$$/수식$$\n\n"


    r1 = 2
    r2 = 30
    r3 = 2
    r4 = 10


    flag = True

    while flag:
        B = random.randint(r1, r2)
        A, D, F = np.random.choice(list(range(r3, r4+1)), 3)
        C, E, G = np.random.choice(list(range(1, B)), 3)

        if C + E + G < B:
            H = A + D
            I = C + E
            J = H + F
            K = I + G

            Frac_1 = "%s {%s} over {%s}" % (A, C, B)
            Frac_2 = "%s {%s} over {%s}" % (D, E, B)
            Frac_3 = "%s {%s} over {%s}" % (F, G, B)
            Frac_4 = "{%s} over {%s}" % (C, B)
            Frac_5 = "{%s} over {%s}" % (E, B)
            Frac_6 = "{%s} over {%s}" % (I, B)
            Frac_7 = "{%s} over {%s}" % (G, B)
            Frac_8 = "{%s} over {%s}" % (K, B)

            if check_simFrac(I, B) and check_simFrac(K, B) :
                flag = False


    stem = stem.format(Frac_1=Frac_1, Frac_2=Frac_2, Frac_3=Frac_3, box_j1=box_j1, box_j2=box_j2)
    answer = answer.format(H=H, J=J, Frac_6=Frac_6, Frac_8=Frac_8)
    comment = comment.format(Frac_1=Frac_1, Frac_2=Frac_2, Frac_3=Frac_3, Frac_4=Frac_4, Frac_5=Frac_5, Frac_6=Frac_6,
                             Frac_7=Frac_7, Frac_8=Frac_8, A=A, D=D, H=H, F=F, J=J)


    return stem, answer, comment
























# 4-2-1-33
def fractionaddsub421_Stem_029():
    '''
    :param r1: 분모의 최솟값 [int] {2:3}
    :param r2: 분모의 최댓값 [int] {29:30}
    :param r3: 자연수의 최솟값 [int] {2:3}
    :param r4: 자연수의 최댓값 [int] {9:10}
    '''
    stem = "다음 대분수 중 $$수식$$2$$/수식$$개를 선택하여 합이 가장 큰 덧셈식을 만들어 계산해 보세요.\n$$표$$$$수식$${Frac_1}$$/수식$$   $$수식$${Frac_2}$$/수식$$   $$수식$${Frac_3}$$/수식$$   $$수식$${Frac_4}$$/수식$$   $$수식$${Frac_5}$$/수식$$   $$수식$${Frac_6}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${N} {Frac_11}$$/수식$$\n"
    comment = "(해설)\n" \
              "합이 가장 큰 덧셈식을 만들려면 가장 큰 수와 두 번째 큰 수를 더해야 합니다.\n" \
              "주어진 대분수의 크기를 비교하면\n" \
              "$$수식$${compar_exp}$$/수식$$\n" \
              "가장 큰 수는 $$수식$${Frac_7}$$/수식$$, 두 번째 큰 수는 $$수식$${Frac_8}$$/수식$$입니다.\n" \
              "따라서 두 수의 합은\n" \
              "$$수식$${Frac_7} ` + ` {Frac_8} ` = ` LEFT ( {J} ` + ` {F} RIGHT ) ` + ` LEFT ( {Frac_9} ` + ` {Frac_10} RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {N} ` + ` {Frac_11} ` = ` {N} {Frac_11}$$/수식$$\n\n"


    r1 = 2
    r2 = 30
    r3 = 2
    r4 = 10


    flag = True

    while flag:
        A = random.randint(r1, r2)

        B, D, F, H, J, L = np.random.choice(list(range(r3, r4+1)), 6)
        J, F, B, D, H, L = sorted([B, D, F, H, J, L], reverse=True)

        C, E, G, I, K, M = np.random.choice(list(range(1, A)), 6)

        if K + G < A and J != F and F != B and B != D and D != H and H != L:
            N = J + F
            O = K + G

            Frac_1 = "%s {%s} over {%s}" % (B, C, A)
            Frac_2 = "%s {%s} over {%s}" % (D, E, A)
            Frac_3 = "%s {%s} over {%s}" % (F, G, A)

            Frac_4 = "%s {%s} over {%s}" % (H, I, A)
            Frac_5 = "%s {%s} over {%s}" % (J, K, A)
            Frac_6 = "%s {%s} over {%s}" % (L, M, A)

            Frac_1, Frac_2, Frac_3, Frac_4, Frac_5, Frac_6 = random.sample([Frac_1, Frac_2, Frac_3, Frac_4, Frac_5, Frac_6], 6)

            compar_exp = "%s {%s} over {%s} ` &gt; ` %s {%s} over {%s} ` &gt; ` %s {%s} over {%s} ` &gt; ` " \
                         "%s {%s} over {%s} ` &gt; ` %s {%s} over {%s} ` &gt; ` %s {%s} over {%s}"  % (

            J, K, A, F, G, A, B, C, A, D, E, A, H, I, A, L, M, A)

            Frac_7 = "%s {%s} over {%s}" % (J, K, A)
            Frac_8 = "%s {%s} over {%s}" % (F, G, A)
            Frac_9 = "{%s} over {%s}" % (K, A)

            Frac_10 = "{%s} over {%s}" % (G, A)
            Frac_11 = "{%s} over {%s}" % (O, A)

            if check_simFrac(O, A) and len(set([Frac_1, Frac_2, Frac_3, Frac_4, Frac_5, Frac_6])) == 6:
                flag = False


    stem = stem.format(Frac_1=Frac_1, Frac_2=Frac_2, Frac_3=Frac_3, Frac_4=Frac_4, Frac_5=Frac_5, Frac_6=Frac_6)
    answer = answer.format(N=N, Frac_11=Frac_11)
    comment = comment.format(compar_exp=compar_exp, Frac_5=Frac_5, Frac_3=Frac_3, Frac_7=Frac_7, Frac_8=Frac_8,
                             Frac_9=Frac_9, Frac_10=Frac_10, Frac_11=Frac_11, J=J, F=F, N=N)


    return stem, answer, comment






























# 4-2-1-34
def fractionaddsub421_Stem_030():
    '''
    :param r1: 분모의 최솟값 [int] {2:3}
    :param r2: 분모의 최댓값 [int] {29:30}
    :param r3: 자연수의 최솟값 [int] {2:3}
    :param r4: 자연수의 최댓값 [int] {9:10}
    '''
    stem = "{T}{T_josa1} 운동을 {W1}요일에 $$수식$${Frac_1}$$/수식$$시간, {W2}요일에 $$수식$${Frac_2}$$/수식$$시간 했습니다. {T}{T_josa2} 이틀 동안 운동을 모두 몇 시간 했나요?\n"
    answer = "(정답)\n$$수식$${F} {Frac_5}$$/수식$$시간\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${T}{T_josa2} 이틀 동안 운동한 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$${T}{T_josa2} {W1}요일에 운동한 시간$$수식$$RIGHT ) ` + ` LEFT ($$/수식$${T}{T_josa2} {W2}요일에 운동한 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {Frac_1} ` + ` {Frac_2} ` = ` LEFT ( {A} ` + ` {D} RIGHT ) ` + ` LEFT ( {Frac_3} ` + ` {Frac_4} RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {F} + {Frac_5} ` = ` {F} {Frac_5}$$/수식$$\n\n"


    r1 = 2
    r2 = 30
    r3 = 2
    r4 = 10


    week_list = ['월', '화', '수', '목', '금', '토']

    w_idx = np.random.randint(0, 5, 1)[0]

    W1, W2 = week_list[w_idx], week_list[w_idx+1]

    flag = True


    while flag:
        T = random.choice(person_yeo + person_nam)

        if han_josa(T[-1]) == ' ':
            T_josa1 = '는'
            T_josa2 = '가'
        else:
            T_josa1 = '이는'
            T_josa2 = '이가'

        B = random.randint(r1, r2)
        A, D = np.random.choice(list(range(r3, r4+1)), 2)
        C, E = np.random.choice(list(range(1, B)), 2)

        if C + E < B:
            F = A + D
            G = C + E

            Frac_1 = "%s {%s} over {%s}" % (A, C, B)
            Frac_2 = "%s {%s} over {%s}" % (D, E, B)

            Frac_3 = "{%s} over {%s}" % (C, B)
            Frac_4 = "{%s} over {%s}" % (E, B)
            Frac_5 = "{%s} over {%s}" % (G, B)

            if check_simFrac(C, B) and check_simFrac(E, B) and check_simFrac(G, B):
                flag = False


    stem = stem.format(T=T, T_josa1=T_josa1, T_josa2=T_josa2, Frac_1=Frac_1, Frac_2=Frac_2, W1=W1, W2=W2)
    answer = answer.format(F=F, Frac_5=Frac_5)
    comment = comment.format(T=T, T_josa2=T_josa2, A=A, D=D, F=F, Frac_1=Frac_1, Frac_2=Frac_2, Frac_3=Frac_3, Frac_4=Frac_4, Frac_5=Frac_5, W1=W1, W2=W2)


    return stem, answer, comment





























# 4-2-1-35
def fractionaddsub421_Stem_031():
    '''
    :param r1: 분모의 최솟값 [int] {2:3}
    :param r2: 분모의 최댓값 [int] {29:30}
    :param r3: 자연수의 최솟값 [int] {2:3}
    :param r4: 자연수의 최댓값 [int] {9:10}
    '''
    stem = "{T1}{T1_josa} 가족이 한 달 동안 먹은 쌀의 양은 $$수식$${Frac_1} ` rm kg$$/수식$$이고, {T2}{T2_josa} 가족은 {T1}{T1_josa} 가족보다 $$수식$${Frac_2} ` rm kg$$/수식$$ 더 많이 먹었습니다. {T2}{T2_josa} 가족이 한 달 동안 먹은 쌀은 몇 $$수식$$rm kg$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${Frac_7} ` rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${T2}{T2_josa} 가족이 한 달 동안 먹은 쌀의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$${T1}{T1_josa} 가족이 한 달 동안 먹은 쌀의 양$$수식$$RIGHT ) ` + ` {Frac_2}$$/수식$$\n" \
              "$$수식$$= ` {Frac_1} ` + ` {Frac_2} ` = ` LEFT ( {A} ` + ` {D} RIGHT ) ` + ` LEFT ( {Frac_3} ` + ` {Frac_4} RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {F} + {Frac_5} ` = ` {F} ` + ` 1 {Frac_6} ` = ` {Frac_7} LEFT ( rm kg RIGHT )$$/수식$$\n\n"


    r1 = 2
    r2 = 30
    r3 = 2
    r4 = 10


    flag = True

    while flag:
        T1, T2 = random.sample(person_yeo + person_nam, 2)
        if han_josa(T1[-1]) == ' ':
            T1_josa = '네'
        else:
            T1_josa = '이네'
        if han_josa(T2[-1]) == ' ':
            T2_josa = '네'
        else:
            T2_josa = '이네'

        B = random.randint(r1, r2)
        A, D = np.random.choice(list(range(r3, r4)), 2)
        C, E = np.random.choice(list(range(1, B)), 2)

        if C + E > B:
            F = A + D
            G = C + E
            H = G - B
            I = F + 1

            Frac_1 = "%s {%s} over {%s}" % (A, C, B)
            Frac_2 = "%s {%s} over {%s}" % (D, E, B)

            Frac_3 = "{%s} over {%s}" % (C, B)
            Frac_4 = "{%s} over {%s}" % (E, B)
            Frac_5 = "{%s} over {%s}" % (G, B)
            Frac_6 = "{%s} over {%s}" % (H, B)

            Frac_7 = "%s {%s} over {%s}" % (I, H, B)

            if check_simFrac(C, B) and check_simFrac(E, B) and check_simFrac(H, B):
                flag = False


    stem = stem.format(T1=T1, T1_josa=T1_josa, T2=T2, T2_josa=T2_josa, Frac_1=Frac_1, Frac_2=Frac_2)
    answer = answer.format(Frac_7=Frac_7)
    comment = comment.format(T1=T1, T1_josa=T1_josa, T2=T2, T2_josa=T2_josa, Frac_1=Frac_1, Frac_2=Frac_2, Frac_3=Frac_3,
                             Frac_4=Frac_4, Frac_5=Frac_5, Frac_6=Frac_6, Frac_7=Frac_7, A=A, D=D, F=F)


    return stem, answer, comment
























# 4-2-1-36
def fractionaddsub421_Stem_032():
    '''
    :param r1: 분모의 최솟값 [int] {2:3}
    :param r2: 분모의 최댓값 [int] {29:30}
    :param r3: 자연수의 최솟값 [int] {2:3}
    :param r4: 자연수의 최댓값 [int] {9:10}
    '''
    stem = "{T}{T_josa} 어머니는 마트에서 쌀, 보리, 콩을 샀습니다. 쌀은 $$수식$${Frac_1} ` rm kg$$/수식$$, 보리는 $$수식$${Frac_2} ` rm kg$$/수식$$, 콩은 $$수식$${Frac_3} ` rm kg$$/수식$$을 샀다면 {T}{T_josa} 어머니가 산 쌀, 보리, 콩은 모두 몇 $$수식$$rm kg$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${K} {Frac_7} ` rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$쌀, 보리, 콩의 무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {Frac_1} ` + ` {Frac_2} ` + ` {Frac_3} ` = ` {Frac_4} ` + ` {Frac_5} ` = ` {G} ` + ` {Frac_6}$$/수식$$\n" \
              "$$수식$$= ` {G} ` + ` 1 {Frac_7} ` = ` {K} {Frac_7} LEFT ( `rm kg RIGHT )$$/수식$$\n\n" \


    r1 = 2
    r2 = 30
    r3 = 2
    r4 = 10


    flag = True

    while flag:
        T = random.choice(person_yeo + person_nam)
        if han_josa(T[-1]) == ' ':
            T_josa = '네'
        else:
            T_josa = '이네'

        A = random.randint(r1, r2)
        B, D = np.random.choice(list(range(r3, r4)), 2)
        C, E, F = np.random.choice(list(range(1, A)), 3)

        if C + E < A and C + E < A and C + E + F > A:
            G = B + D
            H = C + E
            I = H + F
            J = I - A
            K = G + 1

            if I > A and J < A:
                Frac_1 = "%s {%s} over {%s}" % (B, C, A)
                Frac_2 = "%s {%s} over {%s}" % (D, E, A)

                Frac_3 = "{%s} over {%s}" % (F, A)
                Frac_4 = "%s {%s} over {%s}" % (G, H, A)

                Frac_5 = "{%s} over {%s}" % (F, A)
                Frac_6 = "{%s} over {%s}" % (I, A)
                Frac_7 = "{%s} over {%s}" % (J, A)

                if check_simFrac(C, A) and check_simFrac(E, A) and check_simFrac(F, A) and check_simFrac(J, A) :
                    flag = False


    stem = stem.format(T=T, T_josa=T_josa, Frac_1=Frac_1, Frac_2=Frac_2, Frac_3=Frac_3)
    answer = answer.format(K=K, Frac_7=Frac_7)
    comment = comment.format(Frac_1=Frac_1, Frac_2=Frac_2, Frac_3=Frac_3, Frac_4=Frac_4, Frac_5=Frac_5, Frac_6=Frac_6,
                             Frac_7=Frac_7, G=G, F=F, K=K)


    return stem, answer, comment





















# 4-2-1-37
def fractionaddsub421_Stem_033():
    stem = "합이 $$수식$${s13}$$/수식$${j1} 되는 두 분수를 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${a1}$$/수식$$    ㉡ $$수식$${a2}$$/수식$$    ㉢ $$수식$${a3}$$/수식$$    ㉣ $$수식$${a4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_jaem}\n"
    comment = "(해설)\n" \
              "분자의 합이 $$수식$${s13}$$/수식$${j1} 되는 두 분수끼리 더해 보면\n" \
              "$$수식$${sbb} ` {scc} over {s13} + {sdd} ` {see} over {s13} = LEFT ( {sbb} + {sdd} RIGHT ) + LEFT ( {scc} over {s13} + {see} over {s13} RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {sjj} + 1 = {sll} != {s13} LEFT ( ` rm X RIGHT )$$/수식$$\n" \
              "$$수식$${sff} ` {sgg} over {s13} + {shh} ` {sii} over {s13} = LEFT ( {sff} + {shh} RIGHT ) + LEFT ( {sgg} over {s13} + {sii} over {s13} RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {smm} + 1 = {s13} LEFT ( ` rm O RIGHT )$$/수식$$\n\n"
    

    while True:
        s13 = np.random.randint(2, 31)

        sbb = np.random.randint(1, 11)
        sdd = np.random.randint(1, 11)
        sff = np.random.randint(1, 11)
        shh = np.random.randint(1, 11)

        scc = np.random.randint(1, s13)
        see = np.random.randint(1, s13)

        sjj = sbb + sdd

        sll = sjj + 1

        sgg = np.random.randint(1, s13)
        sii = np.random.randint(1, s13)

        smm = sff + shh

        if scc + see == s13 and sjj + 1 != s13 and smm + 1 == s13 and sgg + sii == s13 and scc != sgg:
            break


    temp_list1 = [[sff, sgg, s13], [shh, sii, s13]]
    temp_list2 = [[sbb, scc, s13], [sdd, see, s13]]

    ans_shuffle = np.random.randint(0, 6)

    if ans_shuffle == 0:
        cor_jaem = "㉠, ㉡"
        [natural_a1, boon_ja_a1, boon_mo_a1], [natural_a2, boon_ja_a2, boon_mo_a2] = temp_list1
        [natural_a3, boon_ja_a3, boon_mo_a3], [natural_a4, boon_ja_a4, boon_mo_a4] = temp_list2

    elif ans_shuffle == 1:
        cor_jaem = "㉠, ㉢"
        [natural_a1, boon_ja_a1, boon_mo_a1], [natural_a3, boon_ja_a3, boon_mo_a3] = temp_list1
        [natural_a2, boon_ja_a2, boon_mo_a2], [natural_a4, boon_ja_a4, boon_mo_a4] = temp_list2

    elif ans_shuffle == 2:
        cor_jaem = "㉠, ㉣"
        [natural_a1, boon_ja_a1, boon_mo_a1], [natural_a4, boon_ja_a4, boon_mo_a4] = temp_list1
        [natural_a2, boon_ja_a2, boon_mo_a2], [natural_a3, boon_ja_a3, boon_mo_a3] = temp_list2

    elif ans_shuffle == 3:
        cor_jaem = "㉡, ㉢"
        [natural_a2, boon_ja_a2, boon_mo_a2], [natural_a3, boon_ja_a3, boon_mo_a3] = temp_list1
        [natural_a1, boon_ja_a1, boon_mo_a1], [natural_a4, boon_ja_a4, boon_mo_a4] = temp_list2

    elif ans_shuffle == 4:
        cor_jaem = "㉡, ㉣"
        [natural_a2, boon_ja_a2, boon_mo_a2], [natural_a4, boon_ja_a4, boon_mo_a4] = temp_list1
        [natural_a1, boon_ja_a1, boon_mo_a1], [natural_a3, boon_ja_a3, boon_mo_a3] = temp_list2

    else:
        cor_jaem = "㉢, ㉣"
        [natural_a3, boon_ja_a3, boon_mo_a3], [natural_a4, boon_ja_a4, boon_mo_a4] = temp_list1
        [natural_a1, boon_ja_a1, boon_mo_a1], [natural_a2, boon_ja_a2, boon_mo_a2] = temp_list2


    a1 = "%s {%s} over {%s}" % (natural_a1, boon_ja_a1, boon_mo_a1)
    a2 = "%s {%s} over {%s}" % (natural_a2, boon_ja_a2, boon_mo_a2)
    a3 = "%s {%s} over {%s}" % (natural_a3, boon_ja_a3, boon_mo_a3)
    a4 = "%s {%s} over {%s}" % (natural_a4, boon_ja_a4, boon_mo_a4)

    if (str(s13))[-1] == "2" or (str(s13))[-1] == "4" or (str(s13))[-1] == "5" or (str(s13))[-1] == "9":
        j1 = "가"
    else:
        j1 = "이"

    stem = stem.format(s13=s13, j1=j1, a1=a1, a2=a2, a3=a3, a4=a4)
    answer = answer.format(cor_jaem=cor_jaem)
    comment = comment.format(s13=s13, j1=j1, sbb=sbb, scc=scc, sdd=sdd, see=see, sjj=sjj, sll=sll, sff=sff, sgg=sgg, shh=shh, sii=sii, smm=smm)

    return stem, answer, comment






    # comment = "(해설)\n" \
    #           "분자의 합이 $$수식$${s1}$$/수식$${j2} 되는 두 분수끼리 더해 보면\n" \
    #           "$$수식$${c1}$$/수식$$\n" \
    #           "$$수식$$= ` {c2} LEFT ( ` rm {op1} RIGHT )$$/수식$$\n" \
    #           "$$수식$${c3}$$/수식$$\n" \
    #           "$$수식$$= ` {c4} LEFT ( ` rm {op2} RIGHT )$$/수식$$\n\n"


    # flag = True
    #
    # while flag:
    #     s1 = np.random.randint(3, 31, 1)[0]
    #     s2, s4, s6, s8 = np.random.choice(np.arange(2, 10), 4)
    #     s3, s5 = np.random.choice(np.arange(1, s1), 2)
    #
    #     s7 = s1 - s3
    #     s9 = s1 - s5
    #     s10 = s2 + s4
    #
    #     s11 = s10 + 1
    #     s12 = s6 + s8
    #     s13 = s12 + 1
    #
    #     if s2 + s4 != s1-1 and s6 + s8 == s1 and s7 > 0 and s9 > 0 and len(set([s3, s5, s7, s9])) == 4 and s11 != s13:
    #         f1 = '%d {%d} over {%d}' % (s2, s3, s1)
    #         f2 = '%d {%d} over {%d}' % (s4, s5, s1)
    #         f3 = '%d {%d} over {%d}' % (s6, s7, s1)
    #         f4 = '%d {%d} over {%d}' % (s8, s9, s1)
    #
    #         if check_simFrac(s1, s3) and check_simFrac(s1, s5) and check_simFrac(s1, s7) and check_simFrac(s1, s9):
    #             flag = False
    #
    #
    # ans_com_dict = {f1 : 0, f3 : 0, f2 : 1, f4 : 1}
    #
    # answers = [f1, f2, f3, f4]
    # np.random.shuffle(answers)
    #
    # c1_fs, c3_fs, cor_jaem = [], [], []
    #
    # for f in answers:
    #     if ans_com_dict.get(f) == 0 :
    #         c1_fs.append(f)
    #         cor_jaem.append(multiple_choice_jaem.get(answers.index(f)))
    #     else:
    #         c3_fs.append(f)
    #
    # cor_jaem = ', '.join(cor_jaem)
    #
    # if cor_jaem.startswith('㉡'):
    #     c1 = '%s ` + ` %s ` = ` LEFT ( %d ` + ` %d RIGHT ) ` + ` LEFT ( {%d} over {%d} ` + ` {%d} over {%d} RIGHT )' % (c1_fs[0], c1_fs[1], s2, s4, s3, s1, s5, s1)
    #     c2 = '%d ` + ` 1 ` = ` %d' % (s10, s11)
    #     c3 = '%s ` + ` %s ` = ` LEFT ( %d ` + ` %d RIGHT ) ` + ` LEFT ( {%d} over {%d} ` + ` {%d} over {%d} RIGHT )' % (c3_fs[0], c3_fs[1], s6, s8, s7, s1, s9, s1)
    #     c4 = '%d ` + ` 1 ` = ` %d' % (s12, s13)
    #     op1, op2 = ['X', 'O']
    #
    # else:
    #     c1 = '%s ` + ` %s ` = ` LEFT ( %d ` + ` %d RIGHT ) ` + ` LEFT ( {%d} over {%d} ` + ` {%d} over {%d} RIGHT )' % (c3_fs[0], c3_fs[1], s6, s8, s7, s1, s9, s1)
    #     c2 = '%d ` + ` 1 ` = ` %d' % (s12, s13)
    #     c3 = '%s ` + ` %s ` = ` LEFT ( %d ` + ` %d RIGHT ) ` + ` LEFT ( {%d} over {%d} ` + ` {%d} over {%d} RIGHT )' % (c1_fs[0], c1_fs[1], s2, s4, s3, s1, s5, s1)
    #     c4 = '%d ` + ` 1 ` = ` %d' % (s10, s11)
    #     op1, op2 = ['O', 'X']
    #
    #
    #
    # j1 = '이' if (s13 % 10) in have_jongsung_num else '가'
    # j2 = '이' if (s1 % 10) in have_jongsung_num else '가'
    #
    # a1, a2, a3, a4 = answers


    # stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, s13=s13, j1=j1)
    # answer = answer.format(cor_jaem=cor_jaem)
    # comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, s1=s1, j2=j2, op1=op1, op2=op2, s13=s13)

    





































# 4-2-1-38
def fractionaddsub421_Stem_034():
    '''
    :param r1: 분모의 최솟값 [int] {2:3}
    :param r2: 분모의 최댓값 [int] {29:30}
    :param r3: 자연수의 최솟값 [int] {1:2}
    :param r4: 자연수의 최댓값 [int] {9:10}
    '''
    stem = "우유를 {T1}{T1_josa1} $$수식$${Frac_1} ` rm L$$/수식$$ 마셨고, {T2}{T2_josa1} {T1}{T1_josa2} $$수식$${C} ` rm L$$/수식$$ 더 많이 마셨습니다. {T1}{T1_josa3} {T2}{T2_josa2} 마신 우유는 모두 몇 $$수식$$rm L$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${F} {Frac_3} ` rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${T2}{T2_josa2} 마신 우유의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {Frac_1} ` + ` {C} ` = ` {C} {Frac_1} ` LEFT ( rm L RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${T1}{T1_josa3} {T2}{T2_josa2} 마신 우유의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {Frac_1} ` + ` {C} {Frac_1} ` = ` {C} ` + ` {Frac_2} ` = ` {C} ` + ` 1 {Frac_3} ` = ` {F} {Frac_3} LEFT ( ` rm L RIGHT )$$/수식$$\n\n"


    r1 = 2
    r2 = 30
    r3 = 1
    r4 = 10


    flag = True

    while flag:
        T1, T2 = np.random.choice(person_nam + person_yeo, 2)
        if han_josa(T1[-1]) == ' ':
            T1_josa1 = '는'
            T1_josa2 = '보다'
            T1_josa3 = '와'
        else:
            T1_josa1 = '이는'
            T1_josa2 = '이보다'
            T1_josa3 = '이와'

        if han_josa(T2[-1]) == ' ':
            T2_josa1 = '는'
            T2_josa2 = '가'
        else:
            T2_josa1 = '이는'
            T2_josa2 = '이가'

        A = random.randint(r1, r2)
        B = random.randint(1, A-1)
        C = random.randint(r3, r4)

        if B+B > A:
            D = B+B
            E = D-A
            F = C+1

            if E < A:
                Frac_1 = "{%s} over {%s}" % (B, A)
                Frac_2 = "{%s} over {%s}" % (D, A)
                Frac_3 = "{%s} over {%s}" % (E, A)
                if check_simFrac(A, B) and check_simFrac(A, E):
                    flag = False


    stem = stem.format(T1=T1, T1_josa1=T1_josa1, T1_josa2=T1_josa2, T1_josa3=T1_josa3, T2=T2, T2_josa1=T2_josa1, T2_josa2=T2_josa2,
                       Frac_1=Frac_1, C=C)
    answer = answer.format(F=F, Frac_3=Frac_3)
    comment = comment.format(T1=T1, T1_josa3=T1_josa3, T2=T2, T2_josa2=T2_josa2, Frac_1=Frac_1, Frac_2=Frac_2, Frac_3=Frac_3, C=C, F=F)


    return stem, answer, comment



























# 4-2-1-39
def fractionaddsub421_Stem_035():
    '''
    :param r1: 분모의 최솟값 [int] {2:3}
    :param r2: 분모의 최댓값 [int] {29:30}
    :param r3: 자연수의 최솟값 [int] {1:2}
    :param r4: 자연수의 최댓값 [int] {9:10}
    '''
    stem = "㉠에 알맞은 분수를 구해 보세요.\n$$수식$${Frac_1} ` - ` {Frac_2} ` = ` {box_j1}$$/수식$$\n"
    answer = "(정답)\n$$수식$${F} {Frac_5}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${Frac_1} ` - ` {Frac_2} ` = ` LEFT ( {B} ` - ` {D} RIGHT ) ` + ` LEFT ( {Frac_3} ` - ` {Frac_4} RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {F} ` + ` {Frac_5} ` = ` {F} {Frac_5}$$/수식$$\n\n"


    r1 = 2
    r2 = 30
    r3 = 1
    r4 = 10


    flag = True

    while flag:
        A = random.randint(r1, r2)

        B, D = np.random.choice(list(range(r3, r4+1)), 2)
        C, E = np.random.choice((list(range(1, A+1))), 2)

        if B > D and C > E:
            F = B - D
            G = C - E

            Frac_1 = "%s {%s} over {%s}" % (B, C, A)
            Frac_2 = "%s {%s} over {%s}" % (D, E, A)

            Frac_3 = "{%s} over {%s}" % (C, A)
            Frac_4 = "{%s} over {%s}" % (E, A)
            Frac_5 = "{%s} over {%s}" % (G, A)

            if check_simFrac(A, C) and check_simFrac(A, E) and check_simFrac(A, G):
                flag = False


    stem = stem.format(Frac_1=Frac_1, Frac_2=Frac_2, box_j1=box_j1)
    answer = answer.format(F=F, Frac_5=Frac_5)
    comment = comment.format(Frac_1=Frac_1, Frac_2=Frac_2, Frac_3=Frac_3, Frac_4=Frac_4, Frac_5=Frac_5,
                             B=B, D=D, F=F)


    return stem, answer, comment




























# 4-2-1-40
def fractionaddsub421_Stem_036():
    '''
    :param r1: 분모의 최솟값 [int] {2:3}
    :param r2: 분모의 최댓값 [int] {29:30}
    :param r3: 자연수의 최솟값 [int] {1:2}
    :param r4: 자연수의 최댓값 [int] {9:10}
    '''
    stem = "$$수식$${Frac_1} ` - ` {Frac_2}$$/수식$${E_josa} 구하려고 합니다. ㉠과 ㉡에 알맞은 분수를 구해 보세요.\n$$수식$${Frac_1} ` - ` {D} ` = ` {box_j1}$$/수식$$\n$$수식$${box_j1} ` - ` {Frac_3} ` = ` {box_j2}$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${Frac_4}$$/수식$$, ㉡ $$수식$${Frac_6}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${Frac_1} - {D} ` = ` {Frac_4}$$/수식$$ → $$수식$${Frac_4} ` - ` {Frac_5} ` = ` {Frac_6}$$/수식$$\n\n"


    r1 = 2
    r2 = 30
    r3 = 1
    r4 = 10


    flag = True

    while flag:
        A = random.randint(r1, r2)

        B, D = np.random.choice(list(range(r3, r4+1)), 2)
        C, E = np.random.choice(list(range(1, A+1)), 2)

        E_josa = num_josa(E)[2]

        if B > D and C > E:
            F = B-D
            G = C-E

            Frac_1 = "%s {%s} over {%s}" % (B, C, A)
            Frac_2 = "%s {%s} over {%s}" % (D, E, A)
            Frac_3 = "{%s} over {%s}" % (E, A)

            Frac_4 = "%s {%s} over {%s}" % (F, C, A)
            Frac_5 = "{%s} over {%s}" % (E, A)
            Frac_6 = "%s {%s} over {%s}" % (F, G, A)

            if check_simFrac(A, C) and check_simFrac(E, A) and check_simFrac(G, A) :
                flag = False


    stem = stem.format(Frac_1=Frac_1, Frac_2=Frac_2, Frac_3=Frac_3, D=D, E_josa=E_josa, box_j1=box_j1, box_j2=box_j2)
    answer = answer.format(Frac_4=Frac_4, Frac_6=Frac_6)
    comment = comment.format(Frac_1=Frac_1, Frac_4=Frac_4, Frac_5=Frac_5, Frac_6=Frac_6, D=D)


    return stem, answer, comment


























# 4-2-1-41
def fractionaddsub421_Stem_037():
    '''
    :param r1: 분모의 최솟값 [int] {2:3}
    :param r2: 분모의 최댓값 [int] {29:30}
    :param r3: 자연수의 최솟값 [int] {1:2}
    :param r4: 자연수의 최댓값 [int] {9:10}
    '''
    stem = "계산 결과를 비교하여 $$수식$${box}$$/수식$$ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${Frac_1} ` - ` {Frac_2} ~~ {box} ~~ {Frac_3} ` - ` {Frac_4}$$/수식$$\n"
    answer = "(정답)\n$$수식$${N}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${Frac_1} ` - ` {Frac_2} ` = ` LEFT ( {B} ` - ` {D} RIGHT ) ` + ` LEFT ( {Frac_5} ` - ` {Frac_6} RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {F} ` + ` {Frac_7} ` = ` {F} {Frac_7}$$/수식$$\n" \
              "$$수식$${Frac_3} ` - ` {Frac_4} ` = ` LEFT ( {H} ` - ` {J} RIGHT ) ` + ` LEFT ( {Frac_8} ` - ` {Frac_9} RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {L} ` + ` {Frac_10} ` = ` {L} {Frac_10}$$/수식$$\n" \
              "따라서 $$수식$${F} {Frac_7} ` {N} ` {L} {Frac_10}$$/수식$$\n\n"


    r1 = 2
    r2 = 30
    r3 = 1
    r4 = 10


    flag = True

    while flag:
        A = random.randint(r1, r2)

        B, D, H, J = np.random.choice(list(range(r3, r4+1)), 4)
        C, E, I, K = np.random.choice(list(range(1, A)), 4)

        if B == H and D == J:
            continue

        if B > D and H > J and C > E and I > K:
            F = B-D
            G = C-E
            L = H-J
            M = I-K

            if F > L:
                N = "&gt;"
            elif F < L:
                N = "&lt;"
            else:
                if G > M:
                    N = "&gt;"
                elif G < M:
                    N = "&lt;"
                else:
                    N = "="

            Frac_1 = "%s {%s} over {%s}" % (B, C, A)
            Frac_2 = "%s {%s} over {%s}" % (D, E, A)
            Frac_3 = "%s {%s} over {%s}" % (H, I, A)
            Frac_4 = "%s {%s} over {%s}" % (J, K, A)

            Frac_5 = "{%s} over {%s}" % (C, A)
            Frac_6 = "{%s} over {%s}" % (E, A)
            Frac_7 = "{%s} over {%s}" % (G, A)

            Frac_8 = "{%s} over {%s}" % (I, A)
            Frac_9 = "{%s} over {%s}" % (K, A)
            Frac_10 = "{%s} over {%s}" % (M, A)

            if check_simFrac(C, A) and check_simFrac(E, A) and check_simFrac(G, A) and check_simFrac(I, A) and check_simFrac(K, A) and check_simFrac(M, A):
                flag = False


    stem = stem.format(Frac_1=Frac_1, Frac_2=Frac_2, Frac_3=Frac_3, Frac_4=Frac_4, box=box)
    answer = answer.format(N=N)
    comment = comment.format(Frac_1=Frac_1, Frac_2=Frac_2, Frac_3=Frac_3, Frac_4=Frac_4, Frac_5=Frac_5, Frac_6=Frac_6,
                             Frac_7=Frac_7, Frac_8=Frac_8, Frac_9=Frac_9, Frac_10=Frac_10, B=B, D=D, F=F, H=H, J=J, L=L,
                             N=N)


    return stem, answer, comment





























# 4-2-1-42
def fractionaddsub421_Stem_038():
    '''
    :param r1: 분모의 최솟값 [int] {2:3}
    :param r2: 분모의 최댓값 [int] {29:30}
    :param r3: 자연수의 최솟값 [int] {1:2}
    :param r4: 자연수의 최댓값 [int] {9:10}
    '''
    stem = "㉠에 알맞은 수를 구해 보세요.\n$$수식$${Frac_1} ` - ` {Frac_2} ` = ` {box_j1}$$/수식$$\n"
    answer = "(정답)\n$$수식$${F} {Frac_5}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${Frac_1} ` - ` {Frac_2} ` = ` LEFT ( {B} ` - ` {D} RIGHT ) ` + ` LEFT ( {Frac_3} ` - ` {Frac_4} RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {F} ` + ` {Frac_5} ` = ` {F} {Frac_5}$$/수식$$\n\n"


    r1 = 2
    r2 = 30
    r3 = 1
    r4 = 10


    flag = True

    while flag:
        A = random.randint(r1, r2)

        B, D = np.random.choice(list(range(r3, r4 + 1)), 2)
        C, E = np.random.choice(list(range(1, A)), 2)

        if B > D and C > E:
            F = B-D
            G = C-E

            Frac_1 = "%s {%s} over {%s}" % (B, C, A)
            Frac_2 = "%s {%s} over {%s}" % (D, E, A)

            Frac_3 = "{%s} over {%s}" % (C, A)
            Frac_4 = "{%s} over {%s}" % (E, A)
            Frac_5 = "{%s} over {%s}" % (G, A)

            if check_simFrac(A, C) and check_simFrac(E, A) and check_simFrac(G, A):
                flag = False


    stem = stem.format(Frac_1=Frac_1, Frac_2=Frac_2, box_j1=box_j1)
    answer = answer.format(F=F, Frac_5=Frac_5)
    comment = comment.format(Frac_1=Frac_1, Frac_2=Frac_2, Frac_3=Frac_3, Frac_4=Frac_4, Frac_5=Frac_5,
                             B=B, D=D, F=F)


    return stem, answer, comment





























# 4-2-1-43
def fractionaddsub421_Stem_039():
    '''
    :param r1: 분모의 최솟값 [int] {2:3}
    :param r2: 분모의 최댓값 [int] {29:30}
    :param r3: 자연수의 최솟값 [int] {1:2}
    :param r4: 자연수의 최댓값 [int] {9:10}
    '''
    stem = "대분수로만 만들어진 뺄셈식에서 ㉠$$수식$$` + `$$/수식$$㉡이 가장 큰 때의 값을 구해 보세요.\n$$표$$$$수식$${Frac_1} ` - ` {Frac_2} ` = ` {Frac_3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${H}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠$$수식$$` - `$$/수식$$㉡$$수식$$` = ` {E}$$/수식$$이고 ㉠, ㉡은 $$수식$${A}$$/수식$$보다 작아야 합니다.\n" \
              "따라서 ㉠$$수식$$` = ` {F}$$/수식$$, ㉡$$수식$$` = ` {G}$$/수식$$일 때\n" \
              "㉠$$수식$$` + `$$/수식$$㉡$$수식$$` = ` {F} ` + ` {G} ` = ` {H}$$/수식$${ro1} 가장 큽니다.\n\n"



    r1 = 2
    r2 = 30
    r3 = 1
    r4 = 10


    flag = True

    while flag:
        A = random.randint(r1, r2)

        B, C = np.random.choice(list(range(r3, r4+1)), 2)

        if B > C:
            D = B-C
            E = random.randint(1, A-1)

            F = A-1
            G = F-E
            H = F+G

            Frac_1 = "%s {㉠} over {%s}" % (B, A)
            Frac_2 = "%s {㉡} over {%s}" % (C, A)
            Frac_3 = "%s {%s} over {%s}" % (D, E, A)

            if F > 0 and G > 0 and soroso(E, A):
                flag = False


    if (str(H))[-1] == "0" or (str(H))[-1] == "3" or (str(H))[-1] == "6":
        ro1 = "으로"
    else:
        ro1 = "로"


    stem = stem.format(Frac_1=Frac_1, Frac_2=Frac_2, Frac_3=Frac_3)
    answer = answer.format(H=H)
    comment = comment.format(A=A, E=E, F=F, G=G, H=H, ro1=ro1)


    return stem, answer, comment



































# 4-2-1-44
def fractionaddsub421_Stem_040():
    stem = "밀가루가 $$수식$${f1} ` rm kg$$/수식$$ 있습니다. {t1} 한 {gae1}를 만드는 데 밀가루 $$수식$${f2} ` rm kg$$/수식$$ 필요합니다. {t1}{j2} 모두 몇 {gae1}까지 만들 수 있고, 남는 밀가루는 몇 $$수식$$rm kg$$/수식$$인지 차례대로 쓰시오.\n"
    answer = "(정답)\n$$수식$$3$$/수식$${gae1}, $$수식$${f5} ` rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${f1} ` - ` {f2} ` = ` {f3} LEFT ( ` rm kg RIGHT )$$/수식$$,\n" \
              "$$수식$${f3} ` - ` {f2} ` = ` {f4} LEFT ( ` rm kg RIGHT )$$/수식$$,\n" \
              "$$수식$${f4} ` - ` {f2} ` = ` {f5} LEFT ( ` rm kg RIGHT )$$/수식$$\n\n"


    t1 = np.random.choice(['케이크', '빵', '초콜릿', '떡볶이'])

    if t1 == "떡볶이":
        gae1 = "접시"
    else:
        gae1 = "개"

    j1 = '가' if josa_check(t1[-1]) == ' ' else '이'
    j2 = '는' if josa_check(t1[-1]) == ' ' else '은'


    flag = True

    while flag:
        # B = 3, D = 1, F = 2, H = 1
        s1 = np.random.randint(3, 31, 1)[0]    # A
        s2, s3 = sorted(list(np.random.choice(np.arange(1, s1), 2, False)), reverse=True)    # C, E
        s4 = s2 - s3    # G
        s5 = s4 - s3    # I
        s6 = s5 - s3    # J
        if s2 - (3*s3) > 0 and check_simFrac(s6, s1) and check_simFrac(s2, s1) and check_simFrac(s1, s3):
            flag = False


    f1 = '3 {%d} over {%d}' % (s2, s1)
    f2 = '1 {%d} over {%d}' % (s3, s1)
    f3 = '2 {%d} over {%d}' % (s4, s1)
    f4 = '1 {%d} over {%d}' % (s5, s1)

    f5 = '{%d} over {%d}' % (s6, s1)


    stem = stem.format(t1=t1, j1=j1, j2=j2, f1=f1, f2=f2, gae1=gae1)
    answer = answer.format(t1=t1, j2=j2, f5=f5, gae1=gae1)
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5)


    return stem, answer, comment
































# 4-2-1-45
def fractionaddsub421_Stem_041() :
    stem = "{t1}{j1}와 {t2}{j2}가 블록 쌓기 놀이를 해서 {t1}{j1}는 $$수식$${f1} ` rm {{cm}}$$/수식$$만큼, {t2}{j2}는 $$수식$${f2} ` rm {{cm}}$$/수식$$만큼 쌓았습니다. 누가 몇 $$수식$$rm {{cm}}$$/수식$$ 더 높이 쌓았나요?\n"
    answer = "(정답)\n{t1}{j1}가 $$수식$${f6} ` rm {{cm}}$$/수식$$만큼 더 높이 쌓았습니다.\n"
    comment = "(해설)\n" \
              "$$수식$${f1} ` {left} ` {f2}$$/수식$$이므로 {t1}{j1}가\n" \
              "$$수식$${f1} ` - ` {f2} ` = ` {s2} ` - ` {s3} ` + ` LEFT ( {f3} ` - ` {f4} RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {s6} ` + ` {f5} ` = ` {f6} LEFT ( ` rm {{cm}} RIGHT )$$/수식$$ 더 높이 쌓았습니다.\n\n"


    terms = [np.random.choice(person_nam, 1)[0], np.random.choice(person_yeo, 1)[0]]

    np.random.shuffle(terms)

    t1, t2 = terms

    j1 = '' if josa_check(t1[-1]) == ' ' else '이'
    j2 = '' if josa_check(t2[-1]) == ' ' else '이'


    flag = True

    while flag:
        s1 = np.random.randint(3, 31, 1)[0]     # A

        s2, s3 = sorted(list(np.random.choice(np.arange(20, 31), 2, False)), reverse=True)    # B, D
        s4, s5 = sorted(list(np.random.choice(np.arange(1, s1), 2, False)), reverse=True)    # C, E

        s6 = s2 - s3    # F
        s7 = s4 - s5    # G

        if check_simFrac(s1, s4) and check_simFrac(s1, s5) and check_simFrac(s1, s7):
            flag = False


    f1 = '%d {%d} over {%d}' % (s2, s4, s1)
    f2 = '%d {%d} over {%d}' % (s3, s5, s1)

    f3 = '{%d} over {%d}' % (s4, s1)
    f4 = '{%d} over {%d}' % (s5, s1)
    f5 = '{%d} over {%d}' % (s7, s1)

    f6 = '%d {%d} over {%d}' % (s6, s7, s1)


    stem = stem.format(t1=t1, t2=t2, j1=j1, j2=j2, f1=f1, f2=f2)
    answer = answer.format(t1=t1, j1=j1, f6=f6)
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, s2=s2, s3=s3, s6=s6, t1=t1, j1=j1, left=left)


    return stem, answer, comment































# 4-2-1-46
def fractionaddsub421_Stem_042() :
    stem = "다음 수를 구해 보세요.\n$$표$$$$수식$${s1}$$/수식$$보다 $$수식$${f1}$$/수식$$ 작은 수$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${s1} ` - ` {f1} ` = ` LEFT ( {s1} ` - ` 1 RIGHT ) {f2} ` - ` {f1}$$/수식$$\n" \
              "$$수식$$= ` LEFT ( {s1} ` - ` 1 ` - ` {s3} RIGHT ) ` + ` LEFT ( {f2} ` - ` {f3} RIGHT ) ` = ` {s5} ` + ` {f4} ` = ` {cor_frac}$$/수식$$\n\n"


    flag = True

    while flag:
        s1 = np.random.randint(5, 21, 1)[0]    # A
        s2 = np.random.randint(2, 31, 1)[0]    # B
        s3 = np.random.randint(1, s1, 1)[0]    # C
        s4 = np.random.randint(1, s2, 1)[0]    # D

        s5 = s1 - 1 - s3    # E
        s6 = s2 - s4    # F

        if check_simFrac(s6, s2) and check_simFrac(s2, s4):
            flag = False


    f1 = '%d {%d} over {%d}' % (s3, s4, s2)

    f2 = '{%d} over {%d}' % (s2, s2)
    f3 = '{%d} over {%d}' % (s4, s2)
    f4 = '{%d} over {%d}' % (s6, s2)

    cor_frac = '%d {%d} over {%d}' % (s5, s6, s2)

    if s5 == 0:
        cor_frac = '{%d} over {%d}' % (s6, s2)


    stem = stem.format(s1=s1, f1=f1)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(s1=s1, s3=s3, s5=s5, f1=f1, f2=f2, f3=f3, f4=f4, cor_frac=cor_frac)


    return stem, answer, comment























# 4-2-1-47
def fractionaddsub421_Stem_043():
    stem = "계산 결과가 잘못된 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${a1}$$/수식$$    ㉡ $$수식$${a2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_jaem}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${c1} ```` LEFT ( {ox_1} RIGHT )$$/수식$$\n" \
              "㉡ $$수식$${c2} ```` LEFT ( {ox_2} RIGHT )$$/수식$$\n" \
              "따라서 계산 결과가 잘못된 것은 {cor_jaem}입니다.\n\n"


    flag = True

    while flag:
        s1, s2, s6, s7 = np.random.choice(np.arange(2, 31), 4, False)    # A, B, F, G
        s3 = np.random.randint(1, s2, 1)[0]    # C
        s4 = s1 - 1     # D
        s5 = s2 - s3    # E
        s8 = np.random.randint(1, s7, 1)[0]    # H
        s9 = s6 - 1    # I
        s10 = np.random.randint(1, s7, 1)[0]    # J
        s11 = s6 - 1    # K
        s12 = s7 - s8    # L

        if s10 != s12 and check_simFrac(s2, s5) and check_simFrac(s2, s3) and check_simFrac(s7, s8) \
            and check_simFrac(s7, s10) and check_simFrac(s7, s12):
            if (s7 - s8) - 2 <= s10 and s10 <= (s7 - s8) + 2 and s10 < s7:
                flag = False


    a1 = '%d ` - ` {%d} over {%d} ` = ` %d {%d} over {%d}' % (s1, s3, s2, s4, s5, s2)
    a2 = '%d ` - ` {%d} over {%d} ` = ` %d {%d} over {%d}' % (s6, s8, s7, s9, s10, s7)


    c1 = '%d ` - ` {%d} over {%d} ` = ` %d {%d} over {%d} ` - ` {%d} over {%d} ` = ` %d {%d} over {%d}' \
         '' % (s1, s3, s2, s1-1, s2, s2, s3, s3, s4, s5, s2)
    c2 = '%d ` - ` {%d} over {%d} ` = ` %d {%d} over {%d} ` - ` {%d} over {%d} ` = ` %d {%d} over {%d}' \
         '' % (s6, s8, s7, s6-1, s7, s7, s8, s7, s11, s12, s7)


    cor_text = a1
    ans_com_dict = {a1:c1, a2:c2}
    answers = [a1, a2]
    np.random.shuffle(answers)


    a1, a2 = answers
    c1 = ans_com_dict.get(a1)
    c2 = ans_com_dict.get(a2)


    ox_1, ox_2, cor_jaem = ['` rm O', '` rm X', '㉡'] if answers.index(cor_text) == 0 else ['rm X', 'rm O', '㉠']


    stem = stem.format(a1=a1, a2=a2)
    answer = answer.format(cor_jaem=cor_jaem)
    comment = comment.format(c1=c1, c2=c2, ox_1=ox_1, ox_2=ox_2, cor_jaem=cor_jaem)


    return stem, answer, comment


































# 4-2-1-48
def fractionaddsub421_Stem_044() :
    stem = "㉠에 알맞은 수를 구해 보세요.\n$$수식$${s1} ` - ` {f1} ` = ` {box_j1}$$/수식$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${s1} ` - ` {f1} ` = ` {f2} ` - ` {f1}$$/수식$$\n" \
              "$$수식$$= ` LEFT ( {s7} ` - ` 1 RIGHT ) ` + ` LEFT ( {f3} ` - ` {f4} RIGHT ) ` = ` {s5} ` + ` {f5} ` = ` {cor_frac}$$/수식$$\n\n"


    flag = True

    while flag:
        s1 = np.random.randint(2, 20, 1)[0]
        s2 = np.random.randint(2, 31, 1)[0]
        s3 = np.random.randint(1, s1, 1)[0]
        s4 = np.random.randint(1, s2, 1)[0]

        s5 = s1 - 1 - s3
        s6 = s2 - s4
        s7 = s1 - 1

        if s5 != 0 and check_simFrac(s2, s6):
            flag = False


    f1 = '%d {%d} over {%d}' % (s3, s4, s2)
    f2 = '%d {%d} over {%d}' % (s7, s2, s2)

    f3 = '{%d} over {%d}' % (s2, s2)
    f4 = '{%d} over {%d}' % (s4, s2)
    f5 = '{%d} over {%d}' % (s6, s2)

    cor_frac = '%d {%d} over {%d}' % (s5, s6, s2)


    stem = stem.format(s1=s1, f1=f1, box_j1=box_j1)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(s1=s1, s5=s5, s7=s7, f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, cor_frac=cor_frac)


    return stem, answer, comment



































# 4-2-1-49
def fractionaddsub421_Stem_045() :
    stem = "㉠에 알맞은 수를 구해 보세요.\n$$수식$${s1} ` - ` {f1} ` = ` {box_j1}$$/수식$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${s1} ` - ` {f1} ` = ` {f2} ` - ` {f3} ` = ` {cor_frac}$$/수식$$\n\n"


    flag = True

    while flag:
        s1 = np.random.randint(1, 31, 1)[0]
        s2 = np.random.randint(2, 31, 1)[0]
        s3 = np.random.randint(1, s2, 1)[0]

        s4 = s1 - 1
        s5 = s2 - s3

        if s4 != 0 and check_simFrac(s2, s5) and check_simFrac(s2, s3):
            flag = False


    f1 = '{%d} over {%d}' % (s3, s2)
    f2 = '%d {%d} over {%d}' % (s4, s2, s2)
    f3 = '{%d} over {%d}' % (s3, s2)

    cor_frac = '%d {%d} over {%d}' % (s4, s5, s2)


    stem = stem.format(s1=s1, f1=f1, box_j1=box_j1)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(s1=s1, f1=f1, f2=f2, f3=f3, cor_frac=cor_frac)


    return stem, answer, comment




































# 4-2-1-50
def fractionaddsub421_Stem_046() :
    stem = "두 수의 차를 구해 보세요.\n$$표$${a1}$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${s1} ` {left} ` {f1}$$/수식$$이므로\n" \
              "$$수식$${s1} ` - ` {f1} ` = ` {f2} ` - ` {f1} ` = ` LEFT ( {s7} ` - ` {s3} RIGHT ) ` + ` LEFT ( {f3} ` - ` {f4} RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {s5} ` + ` {cor_frac} ` = ` {cor_frac}$$/수식$$\n\n"


    flag = True

    while flag:
        s1, s2 = np.random.choice(np.arange(2, 31), 2, False)

        s3 = np.random.randint(1, s1, 1)[0]
        s4 = np.random.randint(1, s2, 1)[0]

        s5 = s1 - 1 - s3
        s6 = s2 - s4
        s7 = s1 - 1

        if s5 != 0 and check_simFrac(s2, s6):
            flag = False


    f1 = '%d {%d} over {%d}' % (s3, s4, s2)
    f2 = '%d {%d} over {%d}' % (s7, s2, s2)

    f3 = '{%d} over {%d}' % (s2, s2)
    f4 = '{%d} over {%d}' % (s4, s2)

    cor_frac = '%d {%d} over {%d}' % (s5, s6, s2)

    mode = np.random.choice([0, 1], 1)[0]

    if mode == 0:
        a1 = '$$수식$$%s$$/수식$$    $$수식$$%d$$/수식$$' % (f1, s1)
    else:
        a1 = '$$수식$$%d$$/수식$$    $$수식$$%s$$/수식$$' % (s1, f1)


    stem = stem.format(a1=a1)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(s1=s1, s3=s3, s5=s5, s7=s7, f1=f1, f2=f2, f3=f3, f4=f4, cor_frac=cor_frac, left=left)


    return stem, answer, comment







































# 4-2-1-51
def fractionaddsub421_Stem_047() :
    stem = "계산 결과가 더 큰 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${a1}$$/수식$$    ㉡ $$수식$${a2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_jaem}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${c1}$$/수식$$\n" \
              "㉡ $$수식$${c2}$$/수식$$\n" \
              "따라서 $$수식$${c3}$$/수식$$이므로 계산 결과가 더 큰 것은 {cor_jaem}입니다.\n\n" \


    flag = True

    while flag:
        try:
            s1, s5 = np.random.choice(np.arange(1, 21), 2, False)
            s2 = np.random.randint(3, 21, 1)[0]
            s8 = s1 - 1
            s3 = np.random.randint(1, s8, 1)[0]
            s9 = s8 - s3
            s4, s7 = np.random.choice(np.arange(1, s2), 2, False)
            s11 = s5 - 1
            s6 = np.random.randint(1, s11, 1)[0]
            s12 = s11 - s6
            s10 = s2 - s4
            s13 = s2 - s7

            if s9 != 0 and s12 != 0 and check_simFrac(s2, s10) and check_simFrac(s2, s13):
                if s9 != s12 and s10 != s13:
                    flag = False
        except:
            continue


    a1 = '%d ` - ` %d {%d} over {%d}' % (s1, s3, s4, s2)

    c1 = '%s ` = ` %d {%d} over {%d} ` - ` %d {%d} over {%d}$$/수식$$\n' \
         '$$수식$$= ` LEFT ( %d ` - ` %d RIGHT ) ` + ` LEFT ( {%d} over {%d} ` - ` {%d} over {%d} RIGHT ) ` = ` %d ` + ` {%d} over {%d} ` = ` %d {%d} over {%d}' \
         '' % (a1, s8, s2, s2, s3, s4, s2, s8, s3, s2, s2, s4, s2, s9, s10, s2, s9, s10, s2)

    a2 = '%d ` - ` %d {%d} over {%d}' % (s5, s6, s7, s2)

    c2 = '%s ` = ` %d {%d} over {%d} ` - ` %d {%d} over {%d}$$/수식$$\n' \
         '$$수식$$= ` LEFT ( %d ` - ` %d RIGHT ) ` + ` LEFT ( {%d} over {%d} ` - ` {%d} over {%d} RIGHT ) ` = ` %d ` + ` {%d} over {%d} ` = ` %d {%d} over {%d}' \
         '' % (a2, s11, s2, s2, s6, s7, s2, s11, s6, s2, s2, s7, s2, s12, s13, s2, s12, s13, s2)


    f1 = '%d {%d} over {%d}' % (s9, s10, s2)
    f2 = '%d {%d} over {%d}' % (s12, s13, s2)

    a1_value = s9 + (s10 / s2)
    a2_value = s12 + (s13 / s2)

    eq = right if a1_value < a2_value else left

    c3 = '%s ` %s ` %s' % (f1, eq, f2)

    cor_jaem = '㉡' if a1_value < a2_value else '㉠'


    stem = stem.format(a1=a1, a2=a2)
    answer = answer.format(cor_jaem=cor_jaem)
    comment = comment.format(c1=c1, c2=c2, c3=c3, cor_jaem=cor_jaem)


    return stem, answer, comment




































# 4-2-1-52
def fractionaddsub421_Stem_048() :
    stem = "계산 결과가 가장 큰 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${a1}$$/수식$$    ㉡ $$수식$${a2}$$/수식$$    ㉢ $$수식$${a3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_jaem}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${c1}$$/수식$$\n" \
              "㉡ $$수식$${c2}$$/수식$$\n" \
              "㉢ $$수식$${c3}$$/수식$$\n" \
              "따라서 자연수가 같고 분자가 같은 분수는 분모가 작을수록 큰 수이므로 $$수식$${c4}$$/수식$$입니다.\n\n"



    flag = True

    while flag:
        s1 = np.random.randint(1, 11, 1)[0]

        s2, s4, s6 = sorted(list(np.random.choice(np.arange(2, 15), 3, False)))
        s9 = np.random.choice(np.arange(1, s2), 1)

        s3 = s2 - s9
        s5 = s4 - s9
        s7 = s6 - s9

        s8 = s1 - 1

        if s2 - s9 > 0 and s8 != 0:
            if soroso(s9, s2) and soroso(s9, s4) and soroso(s9, s6):
                flag = False


    a1 = '%d ` - ` {%d} over {%d}' % (s1, s3, s2)
    f1 = '%d {%d} over {%d}' % (s8, s9, s2)
    c1 = '%s ` = ` %d {%d} over {%d} ` - ` {%d} over {%d} ` = ` %s' % (a1, s8, s2, s2, s3, s2, f1)

    a2 = '%d ` - ` {%d} over {%d}' % (s1, s5, s4)
    f2 = '%d {%d} over {%d}' % (s8, s9, s4)
    c2 = '%s ` = ` %d {%d} over {%d} ` - ` {%d} over {%d} ` = ` %s' % (a2, s8, s4, s4, s5, s4, f2)

    a3 = '%d ` - ` {%d} over {%d}' % (s1, s7, s6)
    f3 = '%d {%d} over {%d}' % (s8, s9, s6)
    c3 = '%s ` = ` %d {%d} over {%d} ` - ` {%d} over {%d} ` = ` %s' % (a3, s8, s6, s6, s7, s6, f3)


    ans_com_dict = {s2 : [a1, c1, f1], s4 : [a2, c2, f2], s6 : [a3, c3, f3]}


    ans_keys = list(ans_com_dict.keys())
    c4 = [ans_com_dict.get(a)[2] for a in sorted(ans_keys)]
    c4 = (' ` %s ` ' % left).join(c4)


    np.random.shuffle(ans_keys)
    a1, a2, a3 = [ans_com_dict.get(a)[0] for a in ans_keys]
    c1, c2, c3 = [ans_com_dict.get(a)[1] for a in ans_keys]


    cor_jaem = multiple_choice_jaem.get(ans_keys.index(min([s2, s4, s6])))


    stem = stem.format(a1=a1, a2=a2, a3=a3)
    answer = answer.format(cor_jaem=cor_jaem)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4)


    return stem, answer, comment











































# 4-2-1-53
def fractionaddsub421_Stem_049() :
    stem = "{t1}{j1}는 벽의 네 면을 칠하기 위해 페인트 $$수식$${f1} ` rm L$$/수식$$를 사 왔습니다. 한 면을 칠하는 데 페인트가 $$수식$${s4} ` rm L$$/수식$$ 필요하다면 네 면을 모두 칠하기 위해서는 몇 $$수식$$rm L$$/수식$$ 더 사야 하나요?\n"
    answer = "(정답)\n$$수식$${cor_frac} ` rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$필요한 페인트의 양$$수식$$RIGHT ) ` = ` {s4} ` TIMES ` 4 ` = ` {s7} LEFT ( ` rm L RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$더 사야 하는 페인트의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {s7} ` - ` {f1} ` = ` {f2} ` - ` {f1}$$/수식$$\n" \
              "$$수식$$= ` LEFT ( {s8} ` - ` {s1} RIGHT ) ` + ` LEFT ( {f3} ` - ` {f4} RIGHT ) ` = ` {s5} ` + ` {f5} ` = ` {cor_frac}$$/수식$$\n\n"


    flag = True

    while flag:
        s1 = np.random.randint(1, 21, 1)[0]
        s2 = np.random.randint(2, 31, 1)[0]
        s3 = np.random.randint(1, s2, 1)[0]
        s4 = np.random.randint(1, 6, 1)[0]

        s6 = s2 - s3
        s7 = 4 * s4
        s8 = s7 - 1
        s5 = s8 - s1

        if s5 > 0 and check_simFrac(s2, s6):
            flag = False


    t1 = np.random.choice(person_nam+person_yeo, 1)[0]

    j1 = '' if josa_check(t1[-1]) == ' ' else '이'

    f1 = '%d {%d} over {%d}' % (s1, s3, s2)
    f2 = '%d {%d} over {%d}' % (s8, s2, s2)

    f3 = '{%d} over {%d}' % (s2, s2)
    f4 = '{%d} over {%d}' % (s3, s2)
    f5 = '{%d} over {%d}' % (s6, s2)

    cor_frac = '%d {%d} over {%d}' % (s5, s6, s2)


    stem = stem.format(t1=t1, j1=j1, f1=f1, s4=s4)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(s1=s1, s4=s4, s5=s5, s7=s7, s8=s8, f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, cor_frac=cor_frac)


    return stem, answer, comment









































# 4-2-1-54
def fractionaddsub421_Stem_050():
    stem = "$$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$$ 중에서 두 수를 골라 ㉠과 ㉡에 써 넣어 계산 결과가 가장 큰 뺄셈식을 만들고 계산한 값을 구해 보세요.\n$$표$$$$수식$${a1}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "계산 결과가 가장 크게 되려면 대분수의 자연수에는 가장 작은 수를, 분자에는 두 번째 작은 수를 써넣어야 합니다. 따라서\n" \
              "$$수식$${s4} `-` {f1} `=` {f2} `-` {f1} $$/수식$$\n$$수식$$ `=` LEFT ( {s8} `-` {s1} RIGHT ) `+` LEFT ( {f3} `-` {f4} RIGHT )$$/수식$$\n" \
              "$$수식$$=` {s6} `+` {f5} `=` {cor_frac}$$/수식$$\n\n"


    flag = True

    while flag:
        s1, s2, s3 = sorted(list(np.random.choice(np.arange(1, 31), 3, False)))

        s4 = s1 + np.random.choice([1, 2, 3, 4], 1)[0]
        s5 = np.random.randint(2, 31, 1)[0]

        s8 = s4 - 1
        s6 = s8 - s1
        s7 = s5 - s2

        if s8 > 0 and s6 > 0 and s7 > 0 and check_simFrac(s5, s7):
            flag = False


    a1 = '%d `-` ㉠ {㉡} over {%d}' % (s4, s5)

    f1 = '%d {%d} over {%d}' % (s1, s2, s5)
    f2 = '%d {%d} over {%d}' % (s8, s5, s5)

    f3 = '{%d} over {%d}' % (s5, s5)
    f4 = '{%d} over {%d}' % (s2, s5)
    f5 = '{%d} over {%d}' % (s7, s5)

    cor_frac = '%d {%d} over {%d}' % (s6, s7, s5)


    stem = stem.format(s1=s1, s2=s2, s3=s3, a1=a1)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, s1=s1, s4=s4, s5=s5, s6=s6, s8=s8, cor_frac=cor_frac)


    return stem, answer, comment













































# 4-2-1-55
def fractionaddsub421_Stem_051() :
    stem = "다음 중 가장 큰 수와 가장 작은 수의 차를 구해 보세요.\n$$표$$$$수식$${a1}$$/수식$$    $$수식$${a2}$$/수식$$    $$수식$${a3}$$/수식$$    $$수식$${a4}$$/수식$$    $$수식$${a5}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sdd} &gt; {saa} {scc} over {sbb} &gt; {sff} &gt; {sgg} {shh} over {sbb} &gt; {see} over {sbb}$$/수식$$이므로 " \
              "가장 큰 수는 $$수식$${sdd}$$/수식$$이고, 가장 작은 수는 $$수식$${see} over {sbb}$$/수식$$입니다.\n" \
              "따라서 가장 큰 수와 가장 작은 수의 차는\n" \
              "$$수식$${sdd} ` - ` {see} over {sbb} ` = ` {sii} {sbb} over {sbb} ` - ` {see} over {sbb} ` = ` {cor_frac}$$/수식$$입니다.\n\n"



    while True:
        saa = np.random.randint(1, 11)

        sbb = np.random.randint(2, 31)

        scc = np.random.randint(1, sbb)
        see = np.random.randint(1, sbb)
        shh = np.random.randint(1, sbb)

        sdd = np.random.randint(saa+1, saa+11)

        sff = np.random.randint(1, 11)

        sgg = np.random.randint(1, 11)

        sii = sdd - 1

        sjj = sbb - see

        if soroso(sbb, sjj) and sff < saa and sgg < sff:
            break


    cor_frac = "%s {%s} over {%s}" % (sii, sjj, sbb)

    x1 = "%s {%s} over {%s}" % (saa, scc, sbb)
    x2 = sdd
    x3 = "{%s} over {%s}" % (see, sbb)
    x4 = sff
    x5 = "%s {%s} over {%s}" % (sgg, shh, sbb)

    temp_list = [x1, x2, x3, x4, x5]
    np.random.shuffle(temp_list)

    [a1, a2, a3, a4, a5] = temp_list


    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(sdd=sdd, saa=saa, scc=scc, sbb=sbb, sff=sff, sgg=sgg, shh=shh, see=see, sii=sii, cor_frac=cor_frac)

    return stem, answer, comment
    
    
    
    

    # comment = "(해설)\n" \
    #           "$$수식$${c1}$$/수식$$이므로 가장 큰 수는 $$수식$${s4}$$/수식$$이고, 가장 작은 수는 $$수식$${f2}$$/수식$$입니다.\n" \
    #           "따라서 가장 큰 수와 가장 작은 수의 차는\n" \
    #           "$$수식$${s4} ` - ` {f2} ` = ` {f4} ` - ` {f2} ` = ` {cor_frac}$$/수식$$입니다.\n\n"

    # flag = True
    #
    # while flag:
    #     try:
    #         s1 = np.random.randint(3, 11, 1)[0]
    #         s2 = np.random.randint(2, 31, 1)[0]
    #         s3, s5, s8 = np.random.choice(np.arange(1, s2), 3)
    #         s4 = np.random.randint(s1, s1+10, 1)[0]
    #         s6 = np.random.randint(2, s1, 1)[0]
    #         s7 = np.random.randint(1, s6, 1)[0]
    #         s9 = s4 - 1
    #         s10 = s2 - s5
    #
    #         if s9 > 0 and s10 > 0 and check_simFrac(s2, s10):
    #             flag = False
    #     except:
    #         continue
    #
    #
    #
    # f1 = '%d {%d} over {%d}' % (s1, s3, s2)
    # f2 = '{%d} over {%d}' % (s5, s2)
    # f3 = '%d {%d} over {%d}' % (s7, s8, s2)
    # f4 = '%d {%d} over {%d}' % (s9, s2, s2)
    # # f5 = '{%d} over {%d}' % (s5, s2)
    #
    # cor_frac = '%d {%d} over {%d}' % (s9, s10, s2)
    #
    #
    # answers = [str(s4), f1, str(s6), f2, f3]
    # c1 = (' ` %s ` ' % left).join(answers)
    #
    #
    # np.random.shuffle(answers)
    # a1, a2, a3, a4, a5 = answers

    # comment = comment.format(c1=c1, s4=s4, f2=f2, f4=f4, cor_frac=cor_frac)







































# 4-2-1-56
def fractionaddsub421_Stem_052() :
    stem = "자연수가 $$수식$${s1}$$/수식$$이고 분모가 $$수식$${s2}$$/수식$$인 가장 큰 대분수와 $$수식$${s3}$$/수식$$의 차를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "자연수가 $$수식$${s1}$$/수식$$이고 분모가 $$수식$${s2}$$/수식$$인 가장 큰 대분수는 $$수식$${f1}$$/수식$$입니다.\n" \
              "따라서 $$수식$${f1}$$/수식$$과 $$수식$${s3}$$/수식$$의 차는 $$수식$${f1} ` {right} ` {s3}$$/수식$$이므로\n" \
              "$$수식$${s3} ` - ` {f1} ` = ` {f2} ` - ` {f1}$$/수식$$\n" \
              "$$수식$$= ` LEFT ( {s7} ` - ` {s1} RIGHT ) ` + ` LEFT ( {f3} ` - ` {f4} RIGHT ) ` = ` {s4} ` + ` {f5} ` = ` {cor_frac}$$/수식$$\n" \
              "입니다.\n\n"


    flag = True

    while flag:
        s1, s3 = np.random.choice(np.arange(1, 21), 2, False)
        s2 = np.random.randint(2, 31, 1)[0]

        s6 = s2 - 1
        s7 = s3 - 1
        s4 = s7 - s1
        s5 = s2 - s6

        if s6 > 0 and s7 > 0 and s4 > 0 and s5 > 0 and check_simFrac(s2, s5):
            flag = False


    f1 = '%d {%d} over {%d}' % (s1, s6, s2)
    f2 = '%d {%d} over {%d}' % (s7, s2, s2)

    f3 = '{%d} over {%d}' % (s2, s2)
    f4 = '{%d} over {%d}' % (s6, s2)
    f5 = '{%d} over {%d}' % (s5, s2)

    cor_frac = '%d {%d} over {%d}' % (s4, s5, s2)


    stem = stem.format(s1=s1, s2=s2, s3=s3)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s7=s7, f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, cor_frac=cor_frac, right=right)


    return stem, answer, comment





































# 4-2-1-57
def fractionaddsub421_Stem_053() :
    stem = "{t1}{j1}는 운동을 어제는 $$수식$${f1}$$/수식$$시간 했고, 오늘은 $$수식$${f2}$$/수식$$시간 했습니다. {t1}{j1}가 내일까지 모두 $$수식$${s4}$$/수식$$시간 운동하려고 한다면 내일은 운동을 몇 시간해야 하나요?\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$시간\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$어제와 오늘 운동한 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {f1} ` + ` {f2} ` = ` {f3} ` = ` {f4} LEFT ($$/수식$$시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$내일 운동을 해야 하는 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {s4} ` - ` {f4} ` = ` {f5} ` - ` {f4}$$/수식$$\n" \
              "$$수식$$= ` LEFT ( {s8} ` - ` {s6} RIGHT ) ` + ` LEFT ( {f6} ` - ` {f7} RIGHT ) ` = ` {s9} ` + ` {f8} ` = ` {cor_frac}$$/수식$$\n\n"


    flag = True

    while flag:
        s1 = np.random.randint(3, 31, 1)[0]
        s2, s3 = np.random.choice(np.arange(1, s1), 2, False)

        s5 = s2 + s3
        s6 = s5 // s1
        s4 = np.random.randint(s6, s6+3, 1)[0]

        s7 = s5 - (s6*s1)
        s8 = s4 - 1
        s9 = s8 - s6
        s10 = s1 - s7

        if s2 + s3 > s1 and s6 > 0 and s7 > 0 and s8 > 0 and s9 > 0 and s10 > 0 and check_simFrac(s1, s2) and check_simFrac(s1, s3) and check_simFrac(s1, s10):
            flag = False


    t1 = np.random.choice(person_nam+person_yeo, 1)[0]

    j1 = '' if josa_check(t1[-1]) == ' ' else '이'

    f1 = '{%d} over {%d}' % (s2, s1)
    f2 = '{%d} over {%d}' % (s3, s1)
    f3 = '{%d} over {%d}' % (s5, s1)

    f4 = '%d {%d} over {%d}' % (s6, s7, s1)
    f5 = '%d {%d} over {%d}' % (s8, s1, s1)

    f6 = '{%d} over {%d}' % (s1, s1)
    f7 = '{%d} over {%d}' % (s7, s1)
    f8 = '{%d} over {%d}' % (s10, s1)

    cor_frac = '%d {%d} over {%d}' % (s9, s10, s1)


    stem = stem.format(f1=f1, f2=f2, s4=s4, t1=t1, j1=j1)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(s4=s4, s6=s6, s8=s8, s9=s9, f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, cor_frac=cor_frac)


    return stem, answer, comment




































# 4-2-1-58
def fractionaddsub421_Stem_054() :
    stem = "두 분수의 차를 구해 보세요.\n$$표$$$$수식$${f1}$$/수식$$    $$수식$${f2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${f1} ` - ` {f2} ` = ` {f3} ` - ` {f2} ` = ` {cor_frac}$$/수식$$\n\n"


    flag = True
    
    while flag:
        try:
            s1 = np.random.randint(2, 31, 1)[0]
            s2 = np.random.randint(2, 31, 1)[0]
            s3 = np.random.randint(1, s2, 1)[0]
            s4 = np.random.randint(1, s1, 1)[0]
            s5 = np.random.randint(s3+1, s2, 1)[0]

            s6 = s1 - 1
            s7 = s3 + s2
            s8 = s6 - s4
            s9 = s7 - s5

            if s9 < s2 and s6 > 0 and s8 > 0 and s9 > 0 and check_simFrac(s2, s3) and check_simFrac(s2, s5) and check_simFrac(s2, s9):
                flag = False

        except:
            continue


    f1 = '%d {%d} over {%d}' % (s1, s3, s2)
    f2 = '%d {%d} over {%d}' % (s4, s5, s2)
    f3 = '%d {%d} over {%d}' % (s6, s7, s2)

    cor_frac = '%d {%d} over {%d}' % (s8, s9, s2)


    stem = stem.format(f1=f1, f2=f2)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(f1=f1, f2=f2, f3=f3, cor_frac=cor_frac)


    return stem, answer, comment
































# 4-2-1-59
def fractionaddsub421_Stem_055() :
    stem = "두 분수의 차를 구해 보세요.\n$$표$$$$수식$${f1}$$/수식$$    $$수식$${f2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${f1} ` - ` {f2} ` = ` {f3} ` - ` {f2}$$/수식$$\n" \
              "$$수식$$=` LEFT ( {s6} ` - ` {s4} RIGHT ) ` + ` LEFT ( {f4} ` - ` {f5} RIGHT ) ` = ` {s8} ` + ` {f6} ` = ` {cor_frac}$$/수식$$\n\n"


    flag = True

    while flag:
        try:
            s1 = np.random.randint(2, 31, 1)[0]
            s2 = np.random.randint(2, 31, 1)[0]
            s3 = np.random.randint(1, s2, 1)[0]
            s4 = np.random.randint(1, s1, 1)[0]
            s5 = np.random.randint(s3+1, s2, 1)[0]

            s6 = s1 - 1
            s7 = s2 + s3
            s8 = s6 - s4
            s9 = s7 - s5

            if s9 < s2 and s6 > 0 and s8 > 0 and s9 > 0 and check_simFrac(s2, s3) and check_simFrac(s2, s5) and check_simFrac(s2, s9):
                flag = False

        except:
            continue


    f1 = '%d {%d} over {%d}' % (s1, s3, s2)
    f2 = '%d {%d} over {%d}' % (s4, s5, s2)
    f3 = '%d {%d} over {%d}' % (s6, s7, s2)

    f4 = '{%d} over {%d}' % (s7, s2)
    f5 = '{%d} over {%d}' % (s5, s2)
    f6 = '{%d} over {%d}' % (s9, s2)

    cor_frac = '%d {%d} over {%d}' % (s8, s9, s2)


    stem = stem.format(f1=f1 ,f2=f2)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(s4=s4, s6=s6, s8=s8, f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, cor_frac=cor_frac)


    return stem, answer, comment


























# 4-2-1-60
def fractionaddsub421_Stem_056():
    stem = "㉠과 ㉡에 알맞은 수를 구해 보세요.\n$$수식$${f1} ` - ` {f2} ` = ` {box_j1}$$/수식$$\n$$수식$${box_j1} ` - ` {f7} ` = ` {box_j2}$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${cor_frac1}$$/수식$$, ㉡ $$수식$${cor_frac2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${f1} ` - ` {f2} ` = ` {f3} ` - ` {f2}$$/수식$$\n" \
              "$$수식$$=` LEFT ( {s8} ` - ` {s4} RIGHT ) ` + ` LEFT ( {f4} ` - ` {f5} RIGHT ) ` = ` {s10} ` + ` {f6} ` = ` {cor_frac1}$$/수식$$\n" \
              "$$수식$${cor_frac1} ` - ` {f7} ` = ` {f8} ` - ` {f7}$$/수식$$\n" \
              "$$수식$$=` LEFT ( {s12} ` - ` {s6} RIGHT ) ` + ` LEFT ( {f9} ` - ` {f10} RIGHT ) ` = ` {s14} ` + ` {f11} ` = ` {cor_frac2}$$/수식$$\n\n"


    flag = True

    while flag:
        try:
            s1 = np.random.randint(2, 31, 1)[0]
            s2 = np.random.randint(2, 31, 1)[0]
            s3 = np.random.randint(1, s2, 1)[0]
            s4 = np.random.randint(1, s1, 1)[0]
            s5 = np.random.randint(s3+1, s2, 1)[0]
            s6 = np.random.randint(1, s4, 1)[0]

            s8 = s1 - 1
            s9 = s2 + s3
            s10 = s8 - s4
            s11 = s9 - s5

            s7 = np.random.randint(s11+1, s2, 1)[0]

            s12 = s10 - 1
            s13 = s11 + s2
            s14 = s12 - s6
            s15 = s13 - s7

            if s8 > 0 and s10 > 0 and s11 > 0 and s12 > 0 and s14 > 0 and s15 > 0 and check_simFrac(s2, s3) and check_simFrac(s2, s5) and check_simFrac(s2, s7) and check_simFrac(s2, s11) and check_simFrac(s2, s15)\
                    and s2 > s11 and s2 > s15:
                flag = False

        except:
            continue


    f1 = '%d {%d} over {%d}' % (s1, s3, s2)
    f2 = '%d {%d} over {%d}' % (s4, s5, s2)
    f3 = '%d {%d} over {%d}' % (s8, s9, s2)

    f4 = '{%d} over {%d}' % (s9, s2)
    f5 = '{%d} over {%d}' % (s5, s2)
    f6 = '{%d} over {%d}' % (s11, s2)

    cor_frac1 = '%d {%d} over {%d}' % (s10, s11, s2)

    f7 = '%d {%d} over {%d}' % (s6, s7, s2)
    f8 = '%d {%d} over {%d}' % (s12, s13, s2)

    f9 = '{%d} over {%d}' % (s13, s2)
    f10 = '{%d} over {%d}' % (s7, s2)
    f11 = '{%d} over {%d}' % (s15, s2)

    cor_frac2 = '%d {%d} over {%d}' % (s14, s15, s2)


    stem = stem.format(f1=f1, f2=f2, f7=f7, box_j1=box_j1, box_j2=box_j2)
    answer = answer.format(cor_frac1=cor_frac1, cor_frac2=cor_frac2)
    comment =comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, f10=f10, f11=f11,
                            s4=s4, s6=s6, s8=s8, s10=s10, s12=s12, s14=s14, cor_frac1=cor_frac1, cor_frac2=cor_frac2)


    return stem, answer, comment





































# 4-2-1-61
def fractionaddsub421_Stem_057():
    stem = "계산 결과가 큰 것부터 차례대로 써 보세요.\n$$표$$㉠ $$수식$${a1}$$/수식$$   ㉡ $$수식$${a2}$$/수식$$\n㉢ $$수식$${a3}$$/수식$$   ㉣ $$수식$${a4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_text}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${c1}$$/수식$$\n" \
              "㉡ $$수식$${c2}$$/수식$$\n" \
              "㉢ $$수식$${c3}$$/수식$$\n" \
              "㉣ $$수식$${c4}$$/수식$$\n" \
              "따라서 $$수식$${c5}$$/수식$$이므로 계산 결과가 가장 큰 것부터 차례대로 {cor_text}입니다.\n\n"


    flag = True

    while flag:
        try:
            s1, s6, s10, s14 = np.random.choice(np.arange(5, 51), 4)
            s2 = np.random.randint(2, 31, 1)[0]
            s4 = np.random.randint(1, s1, 1)[0]
            s8 = np.random.randint(1, s6, 1)[0]

            s12 = np.random.randint(1, s10, 1)[0]
            s16 = np.random.randint(1, s14, 1)[0]

            s3, s7, s11, s15 = np.random.choice(np.arange(1, s2), 4)
            s5 = np.random.randint(s3+1, s2, 1)[0]
            s9 = np.random.randint(s7+1, s2, 1)[0]
            s13 = np.random.randint(s11+1, s2, 1)[0]
            s17 = np.random.randint(s15+1, s2, 1)[0]

            s18, s22, s26, s30 = [s1, s6, s10, s14] + np.reshape([-1, -1, -1, -1], -1)
            s19, s23, s27, s31 = [s1, s7, s11, s15] + np.reshape([s2]*4, -1)
            s20, s24, s28, s32 = [s18, s22, s26, s30] - np.reshape([s4, s8, s12, s16], -1)
            s21, s25, s29, s33 = [s19, s23, s27, s31] - np.reshape([s5, s9, s13, s18], -1)

            if s20*s24*s28*s32 > 0 and 0 < s21 < s2 and 0 < s25 < s2 and 0 < s29 < s2 and 0 < s33 < s2:
                if len(set([s20, s24, s28, s32])) == 4:
                    flag = False

        except:
            continue


    a1 = '%d {%d} over {%d} `-` %d {%d} over {%d}' % (s1, s3, s2, s4, s5, s2)
    a2 = '%d {%d} over {%d} `-` %d {%d} over {%d}' % (s6, s7, s2, s8, s9, s2)
    a3 = '%d {%d} over {%d} `-` %d {%d} over {%d}' % (s10, s11, s2, s12, s13, s2)
    a4 = '%d {%d} over {%d} `-` %d {%d} over {%d}' % (s14, s15, s2, s16, s17, s2)

    f1 = '%d {%d} over {%d}' % (s20, s21, s2)
    f2 = '%d {%d} over {%d}' % (s24, s25, s2)
    f3 = '%d {%d} over {%d}' % (s28, s29, s2)
    f4 = '%d {%d} over {%d}' % (s32, s33, s2)

    c1 = '%s `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %s' % (a1, s18, s19, s2, s4, s5, s2, f1)
    c2 = '%s `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %s' % (a2, s22, s23, s2, s8, s9, s2, f2)
    c3 = '%s `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %s' % (a3, s26, s27, s2, s12, s13, s2, f3)
    c4 = '%s `=` %d {%d} over {%d} `-` %d {%d} over {%d} `=` %s' % (a4, s30, s31, s2, s16, s17, s2, f4)


    ans_com_dict = {s20 :[a1, c1, f1], s24 : [a2, c2, f2], s28 : [a3, c3, f3], s32 : [a4, c4, f4]}

    ans_keys = list(ans_com_dict.keys())
    np.random.shuffle(ans_keys)

    answers = [ans_com_dict.get(a)[0] for a in ans_keys]
    comments = [ans_com_dict.get(a)[1] for a in ans_keys]

    c5 = [ans_com_dict.get(a)[2] for a in sorted(ans_keys, reverse=True)]
    c5 = (' `%s` ' % left).join(c5)

    cor_text = ', '.join([multiple_choice_jaem.get(ans_keys.index(v)) for v in sorted(ans_keys, reverse=True)])


    a1, a2, a3, a4 = answers
    c1, c2, c3, c4 = comments


    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, cor_text=cor_text)


    return stem, answer, comment











































# 4-2-1-64
def fractionaddsub421_Stem_058():
    stem = "방앗간에서 떡 $$수식$${s1}$$/수식$$상자를 만들기 위해 쌀 $$수식$${f1} ` rm kg$$/수식$$을 준비했습니다. 떡 한 상자를 만드는 데 쌀 $$수식$${f2} ` rm kg$$/수식$$씩 사용한다면 떡 $$수식$${s1}$$/수식$$상자를 모두 만들기 위해서는 쌀 몇 $$수식$$rm kg$$/수식$$이 더 필요한가요?\n"
    answer = "(정답)\n$$수식$${cor_frac} ` rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$떡 $$수식$${s1}$$/수식$$상자를 만들기 위해 필요한 쌀$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {c1} LEFT ( rm kg RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {f2} times {s1} = {f3} LEFT ( rm kg RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$떡 $$수식$${s1}$$/수식$$상자를 만들기 위해 더 준비해야 할 쌀$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${f3} ` - ` {f1} ` = ` {f4} ` - ` {f1} ` = ` {cor_frac} LEFT ( rm kg RIGHT )$$/수식$$\n\n"


    flag = True

    while flag:
        try:
            s1 = np.random.randint(3, 6, 1)[0]
            s2 = np.random.randint(1, 21, 1)[0]
            s3 = np.random.randint(2, 31, 1)[0]
            s4 = np.random.randint(1, s3, 1)[0]
            s5 = np.random.choice([1, 2, 3], 1)[0]
            s6 = np.random.choice([1, 2], 1)[0]

            s7 = s1 * s5
            s8 = s1 * s6
            s9 = s7 - 1

            s10 = s3 + s8
            s11 = s9 - s2
            s12 = s10 - s4

            if s7 > s2 and s8 < s4 and s9 > 0 and s11 > 0 and s12 > 0  and s8 < s2 and s12 < s2 and check_simFrac(s3, s4) and check_simFrac(s3, s6) and check_simFrac(s3, s12):
                flag = False

        except:
            continue


    f1 = '%d {%d} over {%d}' % (s2, s4, s3)
    f2 = '%d {%d} over {%d}' % (s5, s6, s3)
    f3 = '%d {%d} over {%d}' % (s7, s8, s3)

    c1 = ' ` + ` '.join([f2]*s1) + '` = ` %s' % (f3)

    f4 = '%d {%d} over {%d}' % (s9, s10, s3)
    cor_frac = '%d {%d} over {%d}' % (s11, s12, s3)


    stem = stem.format(s1=s1, f1=f1, f2=f2)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(c1=c1, s1=s1, f1=f1, f3=f3, f4=f4, cor_frac=cor_frac, f2=f2)


    return stem, answer, comment







































# 4-2-1-65
def fractionaddsub421_Stem_059():
    stem = "어느 제과점에 밀가루가 $$수식$${f1} ` rm kg$$/수식$$있습니다. 케이크 한 개를 만드는 데 밀가루가 $$수식$${f2} ` rm kg$$/수식$$ 필요하다면 만들 수 있는 케이크는 몇 개이고, 남는 밀가루는 몇 $$수식$$rm kg$$/수식$$인가요?\n"
    answer = "(정답)\n케이크는 모두 $$수식$${cor_text}$$/수식$$개 까지 만들 수 있고, 밀가루는 $$수식$${cor_frac} ` rm kg$$/수식$$이 남습니다.\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$케이크 한 개를 만들고 남은 밀가루의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {f1} ` - ` {f2} ` = ` {f3} LEFT ( rm kg RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$케이크 $$수식$$2$$/수식$$개를 만들고 남은 밀가루의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {second_ap} ` - ` {f2} ` = ` {second_di} ` - ` {f2} ` = ` {second_result} LEFT ( rm kg RIGHT )$$/수식$$" \
              "{saying1}" \
              "{saying2}\n\n"



    while True:
        saa = np.random.randint(2, 21)
        sbb = np.random.randint(2, 31)
        scc = np.random.randint(1, 31)
        sdd = np.random.randint(1, 21)
        see = np.random.randint(1, 31)

        sff = saa - sdd
        sgg = scc - see


        second_ap_natural = sff
        second_ap_boon_ja = sgg

        second_di_natural = second_ap_natural - 1
        second_di_boon_ja = second_ap_boon_ja + sbb

        second_result_natural = second_di_natural - sdd
        second_result_boon_ja = second_di_boon_ja - see

        third_ap_natural = second_result_natural
        third_ap_boon_ja = second_result_boon_ja

        third_di_natural = third_ap_natural - 1
        third_di_boon_ja = third_ap_boon_ja + sbb

        third_result_natural = third_di_natural - sdd
        third_result_boon_ja = third_di_boon_ja - see

        fourth_ap_natural = third_result_natural
        fourth_ap_boon_ja = third_result_boon_ja

        fourth_di_natural = fourth_ap_natural - 1
        fourth_di_boon_ja = fourth_ap_boon_ja + sbb

        fourth_result_natural = fourth_di_natural - sdd
        fourth_result_boon_ja = fourth_di_boon_ja - see

        ans_choice = np.random.randint(2, 5)

        if scc < sbb and sdd < saa and see < scc and sgg < see:
            if ans_choice == 2 and (second_result_natural + (second_result_boon_ja * sbb)) < (sdd + (see * sbb)) and soroso(second_result_boon_ja, sbb) and second_result_natural > 0:
                saying1 = ""
                saying2 = ""
                cor_text = 2
                cor_frac = "%s {%s} over {%s}" % (second_result_natural, second_result_boon_ja, sbb)
                break

            elif ans_choice == 3 and (third_result_natural + (third_result_boon_ja * sbb)) < (sdd + (see * sbb)) and soroso(third_result_boon_ja, sbb) and third_result_natural > 0 and second_result_boon_ja < see:
                saying1 = f"\n$$수식$$LEFT ($$/수식$$케이크 $$수식$$3$$/수식$$개를 만들고 남은 밀가루의 양$$수식$$RIGHT )$$/수식$$\n" \
                          f"$$수식$$= ` {third_ap_natural} {third_ap_boon_ja} over {sbb} ` - ` {sdd} {see} over {sbb} ` = ` {third_di_natural} {third_di_boon_ja} over {sbb} ` - ` {sdd} {see} over {sbb} " \
                          f"` = ` {third_result_natural} {third_result_boon_ja} over {sbb} LEFT ( rm kg RIGHT )$$/수식$$"
                saying2 = ""
                cor_text = 3
                cor_frac = "%s {%s} over {%s}" % (third_result_natural, third_result_boon_ja, sbb)
                break

            elif ans_choice == 4 and (fourth_result_natural + (fourth_result_boon_ja * sbb)) < (sdd + (see * sbb)) and soroso(fourth_result_boon_ja, sbb) and fourth_result_natural > 0 and second_result_boon_ja < see and third_result_boon_ja < see:
                saying1 = f"\n$$수식$$LEFT ($$/수식$$케이크 $$수식$$3$$/수식$$개를 만들고 남은 밀가루의 양$$수식$$RIGHT )$$/수식$$\n" \
                          f"$$수식$$= ` {third_ap_natural} {third_ap_boon_ja} over {sbb} ` - ` {sdd} {see} over {sbb} ` = ` {third_di_natural} {third_di_boon_ja} over {sbb} ` - ` {sdd} {see} over {sbb} " \
                          f"` = ` {third_result_natural} {third_result_boon_ja} over {sbb} LEFT ( rm kg RIGHT )$$/수식$$"
                saying2 = f"\n$$수식$$LEFT ($$/수식$$케이크 $$수식$$4$$/수식$$개를 만들고 남은 밀가루의 양$$수식$$RIGHT )$$/수식$$\n" \
                          f"$$수식$$= ` {fourth_ap_natural} {fourth_ap_boon_ja} over {sbb} ` - ` {sdd} {see} over {sbb} ` = ` {fourth_di_natural} {fourth_di_boon_ja} over {sbb} ` - ` {sdd} {see} over {sbb} " \
                          f"` = ` {fourth_result_natural} {fourth_result_boon_ja} over {sbb} LEFT ( rm kg RIGHT )$$/수식$$"
                cor_text = 4
                cor_frac = "%s {%s} over {%s}" % (fourth_result_natural, fourth_result_boon_ja, sbb)
                break


    f1 = "%s {%s} over {%s}" % (saa, scc, sbb)
    f2 = "%s {%s} over {%s}" % (sdd, see, sbb)
    f3 = "%s {%s} over {%s}" % (sff, sgg, sbb)


    second_ap = "%s {%s} over {%s}" % (second_ap_natural, second_ap_boon_ja, sbb)
    second_di = "%s {%s} over {%s}" % (second_di_natural, second_di_boon_ja, sbb)
    second_result = "%s {%s} over {%s}" % (second_result_natural, second_result_boon_ja, sbb)


    stem = stem.format(f1=f1, f2=f2)
    answer = answer.format(cor_text=cor_text, cor_frac=cor_frac)
    comment = comment.format(f1=f1, f2=f2, f3=f3, second_ap=second_ap, second_di=second_di, second_result=second_result,
                             saying1=saying1, saying2=saying2)

    return stem, answer, comment




    # stem = "어느 제과점에 밀가루가 $$수식$${f1} ` rm kg$$/수식$$있습니다. 케이크 한 개를 만드는 데 밀가루가 $$수식$${f2} ` rm kg$$/수식$$ 필요하다면 만들 수 있는 케이크는 몇 개이고, 남는 밀가루는 몇 $$수식$$rm kg$$/수식$$인가요?\n"
    # answer = "(정답)\n케이크는 모두 $$수식$${cor_text}$$/수식$$개 까지 만들 수 있고, 밀가루는 $$수식$${cor_frac} ` rm kg$$/수식$$이 남습니다.\n"
    # comment = "(해설)\n" \
    #           "$$수식$$LEFT ($$/수식$$케이크 한 개를 만들고 남은 밀가루의 양$$수식$$RIGHT )$$/수식$$\n" \
    #           "$$수식$$= ` {f1} ` - ` {f2} ` = ` {f3} LEFT ( rm kg RIGHT )$$/수식$$\n" \
    #           "$$수식$$LEFT ($$/수식$$케이크 $$수식$${cor_text}$$/수식$$개를 만들고 남은 밀가루의 양$$수식$$RIGHT )$$/수식$$\n" \
    #           "$$수식$$= ` {f3} ` - ` {f2} ` = ` {f4} ` - ` {f2} ` = ` {cor_frac} LEFT ( rm kg RIGHT )$$/수식$$\n\n"

    # flag = True
    #
    # while flag:
    #     try:
    #         s1 = np.random.randint(2, 21, 1)[0]    # A
    #         s2 = np.random.randint(2, 31, 1)[0]    # B
    #         s3 = np.random.randint(1, s2, 1)[0]    # C
    #         s4 = np.random.randint(1, s1, 1)[0]    # D
    #         s5 = np.random.randint(1, s3, 1)[0]    # E
    #
    #         s6 = s1 - s4    # F
    #         s7 = s3 - s5    # G
    #         s8 = s6 - 1     # H
    #
    #         s9 = s2 + s7     # I
    #         s10 = s8 - s4    # J
    #         s11 = s9 - s5    # K
    #
    #         if s7 < s5 and s6 > 0 and s7 > 0 and s8 > 0 and s10 > 0 and s11 > 0 and s10 < s4 and check_simFrac(s2, s3) and \
    #             check_simFrac(s2, s5) and check_simFrac(s2, s11):
    #             flag = False
    #
    #     except:
    #         continue
    #
    #
    # f1 = '%d {%d} over {%d}' % (s1, s3, s2)
    # f2 = '%d {%d} over {%d}' % (s4, s5, s2)
    # f3 = '%d {%d} over {%d}' % (s6, s7, s2)
    # f4 = '%d {%d} over {%d}' % (s8, s9, s2)
    #
    # cor_frac = '%d {%d} over {%d}' % (s10, s11, s2)
    # cor_text = 2


    # stem = stem.format(f1=f1, f2=f2)
    # answer = answer.format(cor_text=cor_text, cor_frac=cor_frac)
    # comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, cor_frac=cor_frac, cor_text=cor_text)




























# 4-2-1-66
def fractionaddsub421_Stem_060():
    stem = "어떤 대분수에서 $$수식$${f1}$$/수식$${j1} 빼야 할 것을 잘못하여 더했더니 $$수식$${f2}$$/수식$${j2} 되었습니다. 바르게 계산하면 얼마인가요?\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 대분수를 $$수식$${box}$$/수식$$라 하면\n" \
              "$$수식$${box} ` + ` {f1} ` = ` {f2}$$/수식$$, $$수식$${box} ` = ` {f2} ` - ` {f1} ` = ` {f3} ` - ` {f1} ` = ` {f4}$$/수식$$입니다.\n" \
              "바르게 계산하면\n" \
              "$$수식$${f4} ` - ` {f1} ` = ` {f5} ` - ` {f1} ` = ` {cor_frac}$$/수식$$입니다.\n\n"


    flag = True

    while flag:
        try:
            s1 = np.random.randint(1, 21, 1)[0]
            s2 = np.random.randint(2, 31, 1)[0]
            s3 = np.random.randint(1, s2, 1)[0]
            s4 = np.random.randint(s1+1, s1+5, 1)[0]
            s5 = np.random.randint(1, s3, 1)[0]
            s6 = s4 - 1
            s7 = s2 + s5
            s8 = s6 - s1
            s9 = s7 - s3
            s10 = s8 - 1
            s11 = s9 + s2
            s12 = s10 - s1
            s13 = s11 - s3
            if s9 < s3 and s6 > 0 and s8 > 0 and s9 > 0 and s10 > 0 and s12 > 0 and s13 > 0 and \
                    check_simFrac(s2, s3) and check_simFrac(s2, s5) and check_simFrac(s2, s9) and check_simFrac(s2, s13):
                flag = False

        except:
            continue

    f1 = '%d {%d} over {%d}' % (s1, s3, s2)
    f2 = '%d {%d} over {%d}' % (s4, s5, s2)
    f3 = '%d {%d} over {%d}' % (s6, s7, s2)
    f4 = '%d {%d} over {%d}' % (s8, s9, s2)
    f5 = '%d {%d} over {%d}' % (s10, s11, s2)

    cor_frac = '%d {%d} over {%d}' % (s12, s13, s2)


    j1 = '을' if (s3 % 10) in have_jongsung_num else '를'
    j2 = '이' if (s5 % 10) in have_jongsung_num else '가'


    stem = stem.format(f1=f1, f2=f2, j1=j1, j2=j2)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(box=box, f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, cor_frac=cor_frac)


    return stem, answer, comment
































# 4-2-1-68
def fractionaddsub421_Stem_061():
    stem = "㉠과 ㉡의 차를 구해보세요.\n$$표$$㉠ $$수식$${f1}$$/수식$${j1} $$수식$${f2}$$/수식$$의 합    ㉡ $$수식$${f5}$$/수식$${j2} $$수식$${f6}$$/수식$$의 차$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_frac}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${f1}$$/수식$${j1} $$수식$${f2}$$/수식$$의 합은\n" \
              "$$수식$${f1} ` + ` {f2} ` = ` {f4}$$/수식$$이고,\n" \
              "㉡ $$수식$${f5}$$/수식$${j2} $$수식$${f6}$$/수식$$의 차는\n" \
              "$$수식$${f5} ` - ` {f6} ` = ` {f8}$$/수식$$입니다.\n" \
              "따라서 $$수식$${f4} ` {left} ` {f8}$$/수식$$이므로 두 수의 차는\n" \
              "$$수식$${f4} ` - ` {f8} ` = ` {f9} ` - ` {f8} ` = ` {cor_frac}$$/수식$$입니다.\n\n"


    flag = True

    while flag:
        try:
            s1, s2, s4, s13, s14 = np.random.choice(np.arange(2, 10), 5)
            s3, s5, s6, s7 = np.random.choice(np.arange(1, s2), 4)

            s8 = s1 + s4 + 1
            s9 = s3 + s5 - s2
            s10 = s13 - s14 - 1
            s11 = s6 + s2 - s7

            s15 = s8 - 1
            s16 = s9 + s2
            s17 = s15 - s10
            s18 = s16 - s11

            if s1 + s4 > s13 + s14 and s3 + s5 > s2 and s6 < s7 and min([s9, s10, s11, s15, s17, s18]) > 0 \
                    and check_simFrac(s2, s3) and check_simFrac(s2, s5) and check_simFrac(s2, s6) \
                    and check_simFrac(s2, s7) and check_simFrac(s2, s9) and check_simFrac(s2, s18):
                flag = False
        except:
                continue


    f1 = '%d {%d} over {%d}' % (s1, s3, s2)
    f2 = '%d {%d} over {%d}' % (s4, s5, s2)
    f4 = '%d {%d} over {%d}' % (s8, s9, s2)

    f5 = '%d {%d} over {%d}' % (s13, s6, s2)
    f6 = '%d {%d} over {%d}' % (s14, s7, s2)
    f8 = '%d {%d} over {%d}' % (s10, s11, s2)
    f9 = '%d {%d} over {%d}' % (s15, s16, s2)

    cor_frac = '%d {%d} over {%d}' % (s17, s18, s2)



    j1 = '과' if (s3 % 10) in have_jongsung_num else '와'
    j2 = '과' if (s6 % 10) in have_jongsung_num else '와'


    stem = stem.format(f1=f1, f2=f2, f5=f5, f6=f6, j1=j1, j2=j2)
    answer = answer.format(cor_frac=cor_frac)
    comment = comment.format(f1=f1, f2=f2, f4=f4, f5=f5, f6=f6, f8=f8, f9=f9, cor_frac=cor_frac, j1=j1, j2=j2, left=left)


    return stem, answer, comment





























# 4-2-1-69
def fractionaddsub421_Stem_062():
    stem = "하루에 $$수식$${f1}$$/수식$$분씩 빨라지는 시계가 있습니다. 이 시계를 오늘 낮 $$수식$$12$$/수식$$시에 정확하게 맞추어 놓았습니다. $$수식$${s4}$$/수식$$일 후 낮 $$수식$$12$$/수식$$시에 이 시계는 몇 시 몇 분 몇 초를 가리키나요?\n"
    answer = "(정답)\n{cor_text}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( {s4}$$/수식$$일 동안 빨라진 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {c1}$$/수식$$\n" \
              "$$수식$$ = `{f2}` = ` {f3} LEFT ($$/수식$$분$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${c2} ` = ` 60$$/수식$$이므로\n$$수식$$60$$/수식$$초의 {saying1}$$수식$${f5}$$/수식$${j1} $$수식$${s11}$$/수식$$초입니다.\n" \
              "$$수식$${f6}$$/수식$$분$$수식$$` = ` {s8}$$/수식$$분 $$수식$${f5}$$/수식$$초$$수식$$` = ` {s8}$$/수식$$분 $$수식$${s11}$$/수식$$초\n" \
              "따라서 $$수식$${s4}$$/수식$$일 후 낮 $$수식$$12$$/수식$$시에 이 시계는 {cor_text}를 가리킵니다.\n\n"


    flag = True

    while flag:
        s1, s3, s4 = np.random.choice(np.arange(2, 10), 3)
        s2 = np.random.choice([2, 3, 4, 5, 6], 1)[0]

        s6 = s1 * s4
        s7 = s3 * s4
        s8 = s6 + (s7 // s2)
        s9 = s7 % s2
        s10 = 60 // s2 # x
        s11 = s9 * s10 # z
        if s2 > s3 and s10 > 0 and s8 < 60 and s11 > 0:
            flag = False


    f1 = '%d {%d} over {%d}' % (s1, s3, s2)
    c1 = ' ` + ` '.join([f1] * s4)

    f2 = '%d {%d} over {%d}' % (s6, s7, s2)
    f3 = '%d {%d} over {%d}' % (s8, s9, s2)
    c2 = ' ` + ` '.join([str(s10)] * s2)

    f4 = '{1} over {%d}' % (s2)
    f5 = '{%d} over {%d}' % (s9, s2)
    f6 = '%d {%d} over {%d}' % (s8, s9, s2)


    cor_text = '$$수식$$12$$/수식$$시 $$수식$$%d$$/수식$$분 $$수식$$%d$$/수식$$초' % (s8, s11)

    j1 = '은' if (s9 % 10) in have_jongsung_num else '는'

    if s9 == 1:
        saying1 = ""
    else:
        saying1 = f"$$수식$${f4}$$/수식$$은 $$수식$${s10}$$/수식$$초, "


    stem = stem.format(f1=f1, s4=s4)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s4=s4, s8=s8, s10=s10, s11=s11, f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, c1=c1, c2=c2, cor_text=cor_text, j1=j1, saying1=saying1)


    return stem, answer, comment




















# if __name__ == '__main__' :
#     # 신현호
#     FracPlusMinus_Stem_001()
#     FracPlusMinus_Stem_002()
#     FracPlusMinus_Stem_003()
#     FracPlusMinus_Stem_004()
#     FracPlusMinus_Stem_005()
#     FracPlusMinus_Stem_006()
#     FracPlusMinus_Stem_007()
#     FracPlusMinus_Stem_008()
#     FracPlusMinus_Stem_009()
#     FracPlusMinus_Stem_010()
#     FracPlusMinus_Stem_011()
#     FracPlusMinus_Stem_012()
#     FracPlusMinus_Stem_013()
#
#     # 이명훈
#     FracPlusMinus_Stem_014()
#     FracPlusMinus_Stem_015()
#     FracPlusMinus_Stem_016()
#     FracPlusMinus_Stem_017()
#     FracPlusMinus_Stem_018()
#     FracPlusMinus_Stem_019()
#     FracPlusMinus_Stem_020()
#     FracPlusMinus_Stem_021()
#     FracPlusMinus_Stem_022()
#     FracPlusMinus_Stem_023()
#     FracPlusMinus_Stem_024()
#     FracPlusMinus_Stem_025()
#     FracPlusMinus_Stem_026()
#
#     # 지선영
#     FracPlusMinus_Stem_027()
#     FracPlusMinus_Stem_028()
#     FracPlusMinus_Stem_029()
#     FracPlusMinus_Stem_030()
#     FracPlusMinus_Stem_032()
#
#     # 강슬기
#     FracPlusMinus_Stem_033()
#
#     # 지선영
#     FracPlusMinus_Stem_034()
#     FracPlusMinus_Stem_035()
#     FracPlusMinus_Stem_036()
#     FracPlusMinus_Stem_037()
#     FracPlusMinus_Stem_038()
#     FracPlusMinus_Stem_039()
#
#     # 강슬기
#     FracPlusMinus_Stem_040()
#     FracPlusMinus_Stem_041()
#     FracPlusMinus_Stem_042()
#     FracPlusMinus_Stem_043()
#     FracPlusMinus_Stem_044()
#     FracPlusMinus_Stem_045()
#     FracPlusMinus_Stem_046()
#     FracPlusMinus_Stem_047()
#     FracPlusMinus_Stem_048()
#     FracPlusMinus_Stem_049()
#     FracPlusMinus_Stem_050()
#     FracPlusMinus_Stem_051()
#     FracPlusMinus_Stem_052()
#     FracPlusMinus_Stem_053()
#     FracPlusMinus_Stem_054()
#     FracPlusMinus_Stem_055()
#     FracPlusMinus_Stem_056()
#     FracPlusMinus_Stem_057()
#     FracPlusMinus_Stem_058()
#     FracPlusMinus_Stem_059()
#     FracPlusMinus_Stem_060()
#     FracPlusMinus_Stem_061()
#     FracPlusMinus_Stem_062()







