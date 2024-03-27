import numpy as np
import random
import codecs
import os


multiple_choice_nums = {0: '①', 1: '②', 2: '③', 3: '④', 4: '⑤'}


PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../Dictionary')


person_nam = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XY.txt'), 'r', 'utf-8').readlines()]
person_yeo = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XX.txt'), 'r', 'utf-8').readlines()]



have_jongsung_num = [0, 1, 3, 6, 7, 8]

books = ["세계 명작 동화책", "우리나라 전래 동화책", "이솝우화 동화책", "창작 동화책", "영어 동화책", "유아 동화책"]
fruits = ["포도", "사과", "배", "망고", "바나나", "자몽"]
animals = ["사자", "강아지", "고양이", "코끼리", "사슴", "호랑이", "돼지", "말"]
culture = ['연극', '공연', '전시회', '영화', '시사회', '인형극', '오페라', '콘서트', '연주회']

snack = ['초코파이', '과자', '사탕', '초콜릿', '애플파이']
stem_020_list = ['비행기', '종이학', '공', '종이배', '별']



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




# 2-1-3-04
def addandsub213_Stem_001():
    """
    :param r1: 두자리 수의 범위 최솟값 [int] {10:20}
    :param r2: 두자리 수의 범위 최댓값 [int] {80:99}
    :param r3: 한자리 수의 범위 최솟값 [int] {1:2}
    :param r4: 한자리 수의 범위 최댓값 [int] {9:9}
    :return:
    """
    stem = "{s1}{j1} $$수식$${d1}$$/수식$${e1}, {s2}{j2} $$수식$${d2}$$/수식$${e1} 있습니다. {s3}{j3} 모두 몇 {e1}인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$${e1}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$전체 {s3} 수$$수식$$RIGHT ) = ` LEFT ( ` $$/수식$${s1} 수$$수식$$RIGHT ) ` + ` LEFT ( `$$/수식$${s2} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {d1} ` + ` {d2} ` LEFT ($$/수식$${e1}$$수식$$RIGHT )$$/수식$$\n\n"


    r1 = 20
    r2 = 99
    r3 = 2
    r4 = 9


    while True:
        d1 = random.randint(r1, r2)
        d2 = random.randint(r3, r4)

        if (d1 % 10) + d2 > 10 and d1 + d2 < 100:
            break

    s_list = random.choice([books, fruits, animals])
    s1, s2 = random.sample(s_list, 2)

    s3 = ""
    e1 = ""
    if s_list == books:
        e1 = "권"
        s3 = "동화책"
    elif s_list == fruits:
        e1 = "개"
        s3 = "과일"
    elif s_list == animals:
        e1 = "마리"
        s3 = "동물"

    ans = d1 + d2

    if josa_check(s1[-1]) == ' ':
        j1 = '가'
    else:
        j1 = '이'

    if josa_check(s2[-1]) == ' ':
        j2 = '가'
    else:
        j2 = '이'

    if josa_check(s3[-1]) == ' ':
        j3 = '는'
    else:
        j3 = '은'

    stem = stem.format(s1=s1, s2=s2, s3=s3, j1=j1, j2=j2, j3=j3, d1=d1, d2=d2, e1=e1)
    answer = answer.format(ans=ans, e1=e1)
    comment = comment.format(s1=s1, s2=s2, d1=d1, d2=d2, e1=e1, s3=s3)

    return stem, answer, comment




























# 2-1-3-09
def addandsub213_Stem_002():
    """

    :param r1: 두 자리 수 범위의 최솟값 [int] {10:20}
    :param r2: 두 자리 수 범위의 최댓값 [int] {90:99}
    """

    stem = "어떤 {s1}{j1} 오전에는 $$수식$${d1}$$/수식$$명이 보았고, 오후에는 $$수식$${d2}$$/수식$$명이 보았습니다. 하루 동안 이 {s1}{j1} 본 사람은 모두 몇 명인지 구해 보세요.\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$명\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( $$/수식$$하루 동안 {s1}{j1} 본 사람 수$$수식$$ RIGHT )$$/수식$$\n" \
              "$$수식$$= ` ($$/수식$$오전에 {s1}{j1} 본 사람 수$$수식$$) ` + ` ($$/수식$$오후에 {s1}{j1} 본 사람 수$$수식$$)$$/수식$$\n" \
              "$$수식$$= ` {d1} ` + ` {d2} ` = ` {ans}$$/수식$$\n\n"


    r1 = 20
    r2 = 99


    while True:
        d1, d2 = random.sample(range(r1, r2), 2)
        ans = d1 + d2

        if ans > 100 and (d1 % 10) + (d2 % 10) > 10:
            break

    s1 = random.choice(culture)

    if josa_check(s1[-1]) == ' ':
        j1 = '를'
    else:
        j1 = '을'

    stem = stem.format(s1=s1, j1=j1, d1=d1, d2=d2)
    answer = answer.format(ans=ans)
    comment = comment.format(s1=s1, j1=j1, d1=d1, d2=d2, ans=ans)

    return stem, answer, comment
























# 2-1-3-010
def addandsub213_Stem_003():
    """

    :param r1: 두 자리 수 범위의 최솟값 [int] {10:20}
    :param r2: 두 자리 수 범위의 최댓값 [int] {90:99}
    :param r3: 정답1 값 범위의 최솟값 [int] {2:2}
    :param r4: 정답1 값 범위의 최댓값 [int] {9:9}
    :return:
    """
    stem = "$$수식$${d1} ` + ` {d2}$$/수식$${j1} 다음과 같은 방법으로 계산하려고 합니다. $$수식$${b1}$$/수식$$ 안에 알맞은 수를 써넣고, 계산하는 과정을 설명한 기호를 찾아보세요.\n" \
           "$$표$$$$수식$${d2}$$/수식$${j1} $$수식$${d3}$$/수식$${j2} 생각하고 계산한 후 $$수식$${b2}$$/수식$$을 뺍니다.$$/표$$\n" \
           "$$수식$${d1} ` + ` {d2}$$/수식$$\n" \
           "$$표$$㉠ {exp1}\n㉡ {exp2}$$/표$$\n" \
           "$$수식$${b3}$$/수식$$\n"
    answer = "(정답)\n$$수식$${ans1}$$/수식$$, {ans2}\n"
    comment = "(해설)\n" \
              "{c1}\n\n"


    r1 = 20
    r2 = 99
    r3 = 2
    r4 = 9


    while True:
        d1, d2 = random.sample(range(r1, r2), 2)
        ans1 = random.randint(r3, r4)

        if ((d2 + ans1) % 10 == 0) and (d1 > d2) and ((d1 % 10) + (d2 % 10) > 10) and (d1 + d2 > 100) :
            break

    b1 = "□"
    b2 = "box{~①~}"
    b3 = "box{~~②~~}"

    d3 = d2 + ans1

    j1 = check_jongsung(d2)[2]
    j2 = check_jongsung(d3)[4]
    j3 = check_jongsung(d2)[1]
    j4 = check_jongsung(d3)[2]
    j5 = check_jongsung(ans1)[2]

    while True:
        p1 = "$$수식$${d2}$$/수식$$ {j3} $$수식$${d3}$$/수식$$보다 $$수식$${ans1}$$/수식$$ 작은 수이므로 " \
             "$$수식$${d2}$$/수식$$ 대신에 $$수식$${d3}$$/수식$${j4} 더하고 $$수식$${ans1}$$/수식$${j5} 더해 줍니다."\
            .format(d2=d2, d3=d3, ans1=ans1, j3=j3, j4=j4, j5=j5)
        p2 = "$$수식$${d2}$$/수식$${j3} $$수식$${d3}$$/수식$$보다 $$수식$${ans1}$$/수식$$ 작은 수이므로 " \
             "$$수식$${d2}$$/수식$$ 대신에 $$수식$${d3}$$/수식$${j4} 더하고 $$수식$${ans1}$$/수식$${j5} 빼줍니다."\
            .format(d2=d2, d3=d3, ans1=ans1, j3=j3, j4=j4, j5=j5)

        p_list = [p1, p2]

        exp1 = random.choice(p_list)
        exp2 = random.choice(p_list)

        if exp1 != exp2:
            break

    ans2_list = ['㉠', '㉡']

    i = 0
    for exp in [exp1, exp2]:
        if exp == p_list[1]:
            break
        else:
            i += 1

    ans2 = ans2_list[i]
    c1 = p2

    stem = stem.format(b1=b1, b2=b2, b3=b3, d1=d1, d2=d2, d3=d3, j1=j1, j2=j2, exp1=exp1, exp2=exp2)
    answer = answer.format(ans1=ans1, ans2=ans2)
    comment = comment.format(c1=c1)

    return stem, answer, comment






































# 2-1-3-011
def addandsub213_Stem_004():
    """

    :param r1: 두 자리 수 범위의 최솟값 [int] {10:20}
    :param r2: 두 자리 수 범위의 최댓값 [int] {90:99}
    :return:
    """
    stem = "{name1}{j1} $$수식$${d1} ` + ` {d2}$$/수식$$ {j2} 보기와 같이 계산하였습니다. {name1}{j3} 계산한 방법으로 $$수식$${d3} ` + ` {d4}$$/수식$$ {j4} 계산하는 과정을 써보세요.\n$$표$$$$수식$${d2}$$/수식$$ {j2} $$수식$${d6} ` + ` {d7}$$/수식$$ {j5} 생각하여 $$수식$${d2}$$/수식$$에 있는 $$수식$${d6}$$/수식$$ {j6} $$수식$${d1}$$/수식$$ 에 더해서 $$수식$${d8}$$/수식$$ {j7} 만들고 $$수식$${d7}$$/수식$$ {j20} 더합니다.\n→ $$수식$${d1} ` + ` {d2} ` = ` {d1} ` + ` {d6} ` + ` {d7} ` = ` {d8} ` + ` {d7} ` = ` {d9}$$/수식$$$$/표$$\n$$수식$${d3} ` + ` {d4} ` = ` {b2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${d4}$$/수식$$ {j4} $$수식$${d10} ` + ` {d11}$$/수식$$ {j8} 생각하여 $$수식$${d4}$$/수식$$에 있는 " \
              "$$수식$${d10}$$/수식$$ {j9} $$수식$${d3}$$/수식$$ 에 더해서 $$수식$${d12}$$/수식$$ {j10} 만들고 $$수식$${d11}$$/수식$$ {j21} 더합니다.\n" \
              "따라서 $$수식$${d3} ` + ` {d4} ` = ` {d3} ` + ` {d10} ` + ` {d11} ` = ` {d12} ` + ` {d11} ` = ` {d13}$$/수식$$\n\n"


    r1 = 20
    r2 = 99

    b2 = "□"

    while True:
        d1, d2, d3, d4 = random.sample(range(r1, r2), 4)

        if (d1 % 10) + (d2 % 10) > 10 and d1 + d2 < 100 and (d3 % 10) + (d4 % 10) > 10 and d3 + d4 < 100:
            break

    d6 = 10 - (d1 % 10)
    d7 = d2 - d6
    d8 = d1 + d6
    d9 = d1 + d2

    d10 = 10 - (d3 % 10)
    d11 = d4 - d10
    d12 = d3 + d10
    d13 = d3 + d4

    name1 = random.choice(person_nam+person_yeo)

    j1 = ""
    if josa_check(name1[-1]) == ' ':
        j1 = '는'
    else:
        j1 = '이는'

    j2 = check_jongsung(d2)[2]

    j3 = ""
    if josa_check(name1[-1]) == ' ':
        j3 = '가'
    else:
        j3 = '이가'

    j4 = check_jongsung(d4)[2]

    j5 = check_jongsung(d7)[4]
    j6 = check_jongsung(d6)[2]
    j7 = check_jongsung(d8)[2]
    j20 = check_jongsung(d7)[2]

    j8 = check_jongsung(d11)[4]
    j9 = check_jongsung(d10)[2]
    j10 = check_jongsung(d12)[2]
    j21 = check_jongsung(d11)[2]

    ans = "{d3} ` + ` {d10} ` + ` {d11} ` = ` {d12} ` + ` {d11} ` = ` {d13}"\
        .format(d3=d3, d10=d10, d11=d11, d12=d12, d13=d13)

    stem = stem.format(name1=name1, b2=b2, d1=d1, d2=d2, d3=d3, d4=d4, d6=d6, d7=d7, d8=d8, d9=d9, j1=j1, j2=j2, j3=j3, j4=j4, j5=j5, j6=j6, j7=j7, j20=j20)
    answer = answer.format(ans=ans)
    comment = comment.format(d3=d3, d4=d4, d10=d10, d11=d11, d12=d12, d13=d13, j4=j4, j8=j8, j9=j9, j10=j10, j21=j21)

    return stem, answer, comment




# 2-1-3-013
def addandsub213_Stem_005():
    """

    :param r1: 두 자리 수 범위의 최솟값 [int] {20:20}
    :param r2: 두 자리 수 범위의 최댓값 [int] {99:99}
    """
    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 중에서 $$수식$${b1}$$/수식$$ 안에 들어갈 수 있는 수는 모두 몇 개일까요?\n$$표$$$$수식$${d1} ` + ` {b1} ` {d2} ` &lt; ` {d3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$개\n"
    comment = "(해설)\n" \
              "{c1}\n\n"


    r1 = 20
    r2 = 99


    while True:
        d1, t1, d3 = random.sample(range(r1, r2), 3)

        if d1 + (((t1 // 10) - 1) * 10) + (t1 % 10) < d3 < d1 + t1 and (d1 % 10) + (t1 % 10) > 10 and 2 < t1 // 10 < 7:
            break

    d2 = t1 % 10
    ans = (t1 // 10) - 1

    b1 = "□"

    c1_1 = ""
    c1_2_i = ""
    for j in range(1, ans + 1):
        if j != ans:
            c1_2_i += "$$수식$$%d$$/수식$$, " % j
        else:
            c1_2_i += "$$수식$$%d$$/수식$$" % j

    j1 = check_jongsung(ans)[4]

    for i in range(1, ans + 2):

        if d1 + (i * 10 + d2) < d3:
            c1_1 += "$$수식$$%s ` = ` %d$$/수식$$일 때 $$수식$$%d ` + ` %d ` = ` %d ` &lt; ` %d ` LEFT ($$/수식$$○$$수식$$RIGHT )$$/수식$$,\n" % (b1, i, d1, (i * 10 + d2), d1 + (i * 10 + d2), d3)
        elif d1 + (i * 10 + d2) > d3:
            c1_1 += "$$수식$$%s ` = ` %d$$/수식$$일 때 $$수식$$%d ` + ` %d ` = ` %d ` &gt; ` %d ` LEFT ($$/수식$$×$$수식$$RIGHT )$$/수식$$\n" % (b1, i, d1, (i * 10 + d2), d1 + (i * 10 + d2), d3)

    c1_2 = "따라서 $$수식$${b1}$$/수식$$ 안에 알맞은 수는 {c1_2_i} {j1} $$수식$${ans}$$/수식$$개입니다.".format(b1=b1, c1_2_i=c1_2_i, ans=ans, j1=j1)

    c1 = c1_1 + c1_2

    stem = stem.format(b1=b1, d1=d1, d2=d2, d3=d3)
    answer = answer.format(ans=ans)
    comment = comment.format(c1=c1)

    return stem, answer, comment





# 2-1-3-014
def addandsub213_Stem_006():
    """

    :param r1: 한 자리 수 범위의 최솟값 [int] {1:1}
    :param r2: 한 자리 수 범위의 최댓값 [int] {10:10}
    """
    stem = "수 카드를 한 번씩 사용하여 두 자리 수를 만들려고 합니다. 만들 수 있는 수 중에서 가장 큰 수와 가장 작은 수의 합을 구해보세요\n$$수식$${b1}$$/수식$$  $$수식$${b2}$$/수식$$  $$수식$${b3}$$/수식$$  $$수식$${b4}$$/수식$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "수의 크기를 비교하면 $$수식$${d4} ` &gt; ` {d3} ` &gt; ` {d2} ` &gt; ` {d1}$$/수식$$ 이므로 만들 수 있는 두 자리 수 중 가장 큰 수는 " \
              "$$수식$${c1}$$/수식$$이고 가장 작은 수는 $$수식$${c2}$$/수식$$입니다.\n" \
              "→ $$수식$${c1} ` + ` {c2} ` = ` {ans}$$/수식$$\n\n"


    r1 = 2
    r2 = 9


    while True:
        t1, t2, t3, t4 = random.sample(range(r1, r2), 4)
        d1, d2, d3, d4 = sorted([t1, t2, t3, t4])
        if d3 + d2 > 10:
            break

    c1 = (d4 * 10) + d3
    c2 = (d1 * 10) + d2
    ans = c1 + c2

    b1 = "box{``%s``}" % t1
    b2 = "box{``%s``}" % t2
    b3 = "box{``%s``}" % t3
    b4 = "box{``%s``}" % t4

    stem = stem.format(b1=b1, b2=b2, b3=b3, b4=b4)
    answer = answer.format(ans=ans)
    comment = comment.format(d1=d1, d2=d2, d3=d3, d4=d4, c1=c1, c2=c2, ans=ans)

    return stem, answer, comment





# 2-1-3-017
def addandsub213_Stem_007():
    """
    :param r1: 두 자리 수 범위의 최솟값 [int] {10:20}
    :param r2: 두 자리 수 범위의 최댓값 [int] {90:100}
    :param r3: 한 자리 수 범위의 최솟값 [int] {1:2}
    :param r4: 한 자리 수 범위의 최댓값 [int] {9:10}
    """
    stem = "계산 결과의 크기를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써 넣으세요.\n$$수식$${d1} ` - ` {d2}BIGCIRC{d3} ` - ` {d4}$$/수식$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${d1} ` - ` {d2} ` = ` {c1}$$/수식$$, $$수식$${d3} ` - {d4} ` = ` {c2}$$/수식$$\n" \
              "$$수식$${c1} ` {c3} ` {c2}$$/수식$$이므로 $$수식$${d1} ` - ` {d2} ` {c3} ` {d3} ` - ` {d4}$$/수식$$입니다.\n\n"


    r1 = 20
    r2 = 100
    r3 = 2
    r4 = 10


    while True:
        d1, d3 = random.sample(range(r1, r2), 2)
        d2, d4 = random.sample(range(r3, r4), 2)

        c1 = d1 - d2
        c2 = d3 - d4

        if ((d1 // 10) == (d3 // 10)) and (c1 != c2) and (c1 > 10) and (c2 > 10) and ((d1 % 10) < d2) and ((d3 % 10) < d4) and ((d1 % 10) != 0) and ((d3 % 10) != 0) :
            break

    c3 = ""

    if c1 > c2:
        c3 = "&gt;"
    elif c1 < c2:
        c3 = "&lt;"

    ans = c3

    stem = stem.format(d1=d1, d2=d2, d3=d3, d4=d4)
    answer = answer.format(ans=ans)
    comment = comment.format(d1=d1, d2=d2, d3=d3, d4=d4, c1=c1, c2=c2, c3=c3)

    return stem, answer, comment




# 2-1-3-018
def addandsub213_Stem_008():
    """
    :param r1: 두 자리 수 범위의 최솟값 [int] {10:20}
    :param r2: 두 자리 수 범위의 최댓값 [int] {90:99}
    :param r3: 한 자리 수 범위의 최솟값 [int] {1:2}
    :param r4: 한 자리 수 범위의 최댓값 [int] {9:9}
    """
    stem = "{name}{j1} {s1}{j2} $$수식$${d1}$$/수식$$개 가지고 있습니다. 친구에게 $$수식$${d2}$$/수식$$개를 주면 {name}{j3}에게 남는 {s1}{j4} 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$남은 {s1} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$처음에 가지고 있던 {s1} 수$$수식$$RIGHT ) ` - ` LEFT ($$/수식$$친구에게 준 {s1} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {d1} ` - ` {d2} ` = ` {ans} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"


    r1 = 20
    r2 = 99
    r3 = 1
    r4 = 9


    while True:
        d1 = random.randint(r1, r2)
        d2 = random.randint(r3, r4)
        ans = d1 - d2

        if d1 > d2 > (d1 % 10) and d1 % 10 != 0 and ans % 10 != 0:
            break

    name = random.choice(person_nam+person_yeo)
    s1 = random.choice(fruits + snack)

    j1 = ""
    if josa_check(name[-1]) == ' ':
        j1 = '는'
    else:
        j1 = '이는'

    j2 = ""
    if josa_check(s1[-1]) == ' ':
        j2 = '를'
    else:
        j2 = '을'

    j3 = ""
    if josa_check(name[-1]) == ' ':
        j3 = ''
    else:
        j3 = '이'

    j4 = ""
    if josa_check(s1[-1]) == ' ':
        j4 = '는'
    else:
        j4 = '은'

    stem = stem.format(d1=d1, d2=d2, name=name, s1=s1, j1=j1, j2=j2, j3=j3, j4=j4)
    answer = answer.format(ans=ans)
    comment = comment.format(d1=d1, d2=d2, ans=ans, s1=s1)

    return stem, answer, comment


























# 2-1-3-020
def addandsub213_Stem_009():
    """
    :param r1: 앞쪽 두 자리 수 범위의 최솟값 [int] {51:51}
    :param r2: 앞쪽 두 자리 수 범위의 최댓값 [int] {90:100}
    :param r3: 뒤쪽 두 자리 수 범위의 최솟값 [int] {10:20}
    :param r4: 뒤쪽 두 자리 수 범위의 최댓값 [int] {51:51}
    """
    stem = "다음 중 계산 결과가 가장 {s1} 것은 어느 것입니까?\n① $$수식$${d1} ` - ` {d2}$$/수식$$\n② $$수식$${d3} ` - ` {d4}$$/수식$$\n③ $$수식$${d5} ` - ` {d6}$$/수식$$\n④ $$수식$${d7} ` - ` {d8}$$/수식$$\n⑤ $$수식$${d9} ` - ` {d10}$$/수식$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "① $$수식$${d1} ` - ` {d2} ` = ` {c1}$$/수식$$\n" \
              "② $$수식$${d3} ` - ` {d4} ` = ` {c2}$$/수식$$\n" \
              "③ $$수식$${d5} ` - ` {d6} ` = ` {c3}$$/수식$$\n" \
              "④ $$수식$${d7} ` - ` {d8} ` = ` {c4}$$/수식$$\n" \
              "⑤ $$수식$${d9} ` - ` {d10} ` = ` {c5}$$/수식$$\n" \
              "$$수식$${c6}$$/수식$$이므로\n" \
              "계산 결과가 가장 {s1} 것은 {ans}입니다.\n\n"


    r1 = 51
    r2 = 100
    r3 = 10
    r4 = 51


    while True:
        d1, d3, d5, d7, d9 = random.sample([i for i in range(r1, r2) if i % 10 != 0], 5)
        d2, d4, d6, d8, d10 = random.sample([i for i in range(r3, r4) if i % 10 != 0], 5)

        c1 = d1 - d2
        c2 = d3 - d4
        c3 = d5 - d6
        c4 = d7 - d8
        c5 = d9 - d10

        if c1 != c2 and c1 != c3 and c1 != c4 and c1 != c5 and c2 != c3 and c2 != c4 and c2 != c5 and c3 != c4 and c3 != c5 \
                and c4 != c5 and (d1 % 10) < (d2 % 10) and (d3 % 10) < (d4 % 10) and (d5 % 10) < (d6 % 10) and (d7 % 10) < (d8 % 10) \
                and (d9 % 10) < (d10 % 10):
            break

    c_list = [c1, c2, c3, c4, c5]
    c_list_1 = list(reversed(sorted(c_list)))

    s1 = random.choice(['큰', '작은'])

    if s1 == '큰':
        ans = multiple_choice_nums[c_list.index(c_list_1[0])]
    else:
        ans = multiple_choice_nums[c_list.index(c_list_1[-1])]

    c6 = "`&gt;`".join(list(map(str, c_list_1)))

    stem = stem.format(s1=s1, d1=d1, d2=d2, d3=d3, d4=d4, d5=d5, d6=d6, d7=d7, d8=d8, d9=d9, d10=d10)
    answer = answer.format(ans=ans)
    comment = comment.format(s1=s1, d1=d1, d2=d2, d3=d3, d4=d4, d5=d5, d6=d6, d7=d7, d8=d8, d9=d9, d10=d10, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, ans=ans)

    return stem, answer, comment




# 2-1-3-022
def addandsub213_Stem_010():
    """
    :param r1: 두 자리 수 범위의 최솟값 [int] {10:10}
    :param r2: 두 자리 수 범위의 최댓값 [int] {90:100}
    """
    stem = "{name}{j1} 색종이를 $$수식$${d1}$$/수식$$장 가지고 있습니다. 그중에서 $$수식$${d2}$$/수식$$장으로 {s1}{j2} 접었습니다. 남은 색종이는 몇 장인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$장\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$남은 색종이 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$처음에 가지고 있던 색종이 수$$수식$$RIGHT ) ` - ` LEFT ($$/수식$${s1}{j2} 접은 색종이 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {d1} ` - ` {d2} ` = ` {ans} ` LEFT ($$/수식$$장$$수식$$RIGHT )$$/수식$$\n\n"


    r1 = 10
    r2 = 100


    while True:
        d1, d2 = random.sample([i for i in range(r1, r2) if i % 10 != 0], 2)

        if d1 > d2 and (d1 % 10) < (d2 % 10):
            break

    ans = d1 - d2
    name = random.choice(person_nam+person_yeo)
    s1 = random.choice(stem_020_list)

    j1 = ""
    if josa_check(name[-1]) == ' ':
        j1 = '는'
    else:
        j1 = '이는'

    j2 = ""
    if josa_check(s1[-1]) == ' ':
        j2 = '를'
    else:
        j2 = '을'


    stem = stem.format(d1=d1, d2=d2, name=name, s1=s1, j1=j1, j2=j2)
    answer = answer.format(ans=ans)
    comment = comment.format(d1=d1, d2=d2, ans=ans, s1=s1, j2=j2)

    return stem, answer, comment






























# 2-1-3-23
def addandsub213_Stem_011():
    """

    :param r1: 두자리 수 범위의 최솟값 [int] {10:10}
    :param r2: 두자리 수 범위의 최댓값 [int] {50:100}
    :return:
    """

    stem = "{name}{j1} {s1} $$수식$${d1}$$/수식$$개 중에서 $$수식$${d2}$$/수식$$개를 먹었습니다. 남은 {s1}{j2} 몇 개일까요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$남은 {s1}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$처음에 가지고 있던 {s1}의 수$$수식$$RIGHT ) ` - ` LEFT ($$/수식$$먹은 {s1}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {d1} ` - ` {d2} ` = ` {ans} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"


    r1 = 10
    r2 = 100


    while True:
        d1, d2 = random.sample([i for i in range(r1, r2) if i % 10 != 0], 2)

        if d1 > d2 and (d1 % 10) < (d2 % 10):
            break

    ans = d1 - d2
    name = random.choice(person_nam+person_yeo)
    s1 = random.choice(fruits + snack)

    j1 = ""
    if josa_check(name[-1]) == ' ':
        j1 = '는'
    else:
        j1 = '이는'

    j2 = ""
    if josa_check(s1[-1]) == ' ':
        j2 = '는'
    else:
        j2 = '은'


    stem = stem.format(d1=d1, d2=d2, name=name, s1=s1, j1=j1, j2=j2)
    answer = answer.format(ans=ans)
    comment = comment.format(d1=d1, d2=d2, ans=ans, s1=s1, j2=j2)

    return stem, answer, comment























# 2-1-3-26
def addandsub213_Stem_012():
    """

    :param r1: 두자리 수 범위의 최솟값 [int] {10:11}
    :param r2: 두자리 수 범위의 최댓값 [int] {99:100}
    :return:
    """
    stem = "$$수식$$0$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 중에서 $$수식$${b1}$$/수식$$ 안에 들어갈 수 있는 수의 합을 구해 보세요.\n$$표$$$$수식$${d1} ` - ` {d2} ` {b1} ` &gt; ` {d3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "{c1}\n\n"


    r1 = 10
    r2 = 100


    while True:
        d1, t1, d3 = random.sample(range(r1, r2), 3)

        if ((d1 - t1) == d3) and ((d1 - t1 + 1) > d3) and ((d1 % 10) < (t1 % 10)) and ((d1 % 10) < ((t1 - 1) % 10)) and ((t1 % 10) < 5) :
            break

    d2 = t1 // 10
    p = (t1 % 10)
    ans = (p * (p - 1)) // 2

    b1 = "□"

    c1_1 = ""
    c1_2_i = ""

    for j in range(p):
        if j != p - 1:
            c1_2_i += "$$수식$$%d$$/수식$$, " % j
        else:
            c1_2_i += "$$수식$$%d$$/수식$$" % j

    for i in range(p + 1):

        if d1 - (d2 * 10 + i) > d3:
            c1_1 += "$$수식$$%s ` = ` %d$$/수식$$일 때 $$수식$$%d ` - ` %d ` = ` %d ` &gt; ` %d ` LEFT ($$/수식$$○$$수식$$RIGHT )$$/수식$$,\n" % (b1, i, d1, (d2 * 10 + i), d1 - (d2 * 10 + i), d3)
        elif d1 - (d2 * 10 + i) == d3:
            c1_1 += "$$수식$$%s ` = ` %d$$/수식$$일 때 $$수식$$%d ` - ` %d ` = ` %d ` = ` %d ` LEFT ($$/수식$$×$$수식$$RIGHT )$$/수식$$\n" % (b1, i, d1, (d2 * 10 + i), d1 - (d2 * 10 + i), d3)

    c1_2 = "따라서 $$수식$${b1}$$/수식$$ 안에 들어갈 있는 수는 {c1_2_i}이므로 합은 $$수식$${ans}$$/수식$$입니다.".format(b1=b1, c1_2_i=c1_2_i, ans=ans)

    c1 = c1_1 + c1_2

    stem = stem.format(b1=b1, d1=d1, d2=d2, d3=d3)
    answer = answer.format(ans=ans)
    comment = comment.format(c1=c1)

    return stem, answer, comment


























# 2-1-3-27
def addandsub213_Stem_013():
    """

    :param r1: 두자리 수의 범위 최솟값 [int] {11:11}
    :param r2: 두자리 수의 범위 최댓값 [int] {100:100}
    :param r3: 한자리 수의 범위 최솟값 [int] {1:1}
    :param r4: 한자리 수의 범위 최댓값 [int] {9:9}
    :return:
    """
    stem = "숫자 카드 $$수식$${d1}$$/수식$$, $$수식$${d2}$$/수식$$, $$수식$${d3}$$/수식$${j2} 모두 사용하여 다음과 같은 식을 완성하려고 합니다. ㉠, ㉡, ㉢에 알맞은 수를 구해 보세요.\n$$수식$${b1}$$/수식$$ $$수식$${b2}$$/수식$$$$수식$$` - `$$/수식$$$$수식$${b3}$$/수식$$$$수식$$` = `$$/수식$$$$수식$${d4}$$/수식$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "계산 결과의 일의 자리 숫자가 $$수식$${c1}$$/수식$$이므로\n" \
              "$$수식$${b} ` {b} ` - ` {b}$$/수식$$에서 $$수식$${c2}$$/수식$${j1} 십의 자리에 쓰고 받아내림이 있는 뺄셈식을 만들어야 합니다.\n" \
              "→ $$수식$${c3} ` - ` {c4} ` = ` {d4}$$/수식$$\n\n"


    r1 = 11
    r2 = 100
    r3 = 1
    r4 = 9


    while True:
        c3 = random.randint(r1, r2)
        c4 = random.randint(r3, r4)

        d1 = random.choice([c4, c3 // 10, c3 % 10])
        d2 = random.choice([c4, c3 // 10, c3 % 10])
        d3 = random.choice([c4, c3 // 10, c3 % 10])
        j2 = check_jongsung(d3)[2]

        if d1 != d2 and d1 != d3 and d2 != d3 and d1 > 0 and d2 > 0 and d3 > 0 and c3 % 10 < c4:
            break

    d1 = "box{``%d``}" % d1
    d2 = "box{``%d``}" % d2
    d3 = "box{``%d``}" % d3


    d4 = c3 - c4
    c1 = d4 % 10
    c2 = c3 // 10
    j1 = check_jongsung(c2)[2]

    b = "□"
    b1 = "box{``㉠``}"
    b2 = "box{``㉡``}"
    b3 = "box{``㉢``}"

    ans = "$$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$" % (c3 // 10,  c3 % 10, c4)

    stem = stem.format(j2=j2, d1=d1, d2=d2, d3=d3, d4=d4, b1=b1, b2=b2, b3=b3)
    answer = answer.format(ans=ans)
    comment = comment.format(j1=j1, b=b, c1=c1, c2=c2, c3=c3, c4=c4, d4=d4)

    return stem, answer, comment
























# 2-1-3-28
def addandsub213_Stem_014():
    """

    :param r1: 숫자 카드 범위 최솟값 [int] {1:1}
    :param r2: 숫자 카드 범위 최댓값 [int] {9:9}
    :return:
    """
    stem = "숫자 카드로 만든 두 자리 수 중에서 십의 자리 숫자가 $$수식$${d1}$$/수식$$인 가장 큰 수와 십의 자리 숫자가 $$수식$${d2}$$/수식$$인 가장 작은 수의 차를 구하세요.\n$$수식$${b1}$$/수식$$  $$수식$${b2}$$/수식$$  $$수식$${b3}$$/수식$$  $$수식$${b4}$$/수식$$  $$수식$${b5}$$/수식$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${c1}$$/수식$$이므로 십의 자리 숫자가 $$수식$${d1}$$/수식$$인 가장 큰 두 자리 수 → $$수식$${c2}$$/수식$$\n" \
              "$$수식$${c4}$$/수식$$이므로 십의 자리 숫자가 $$수식$${d2}$$/수식$$인 가장 작은 두 자리 수 → $$수식$${c3}$$/수식$$\n" \
              "따라서 두 수의 차는 $$수식$${c3} `-` {c2} `=` {ans}$$/수식$$입니다.\n\n"


    r1 = 1
    r2 = 9


    while True:
        t1, t2, t3, t4, t5 = random.sample(range(r1, r2), 5)
        t_list = [t1, t2, t3, t4, t5]
        d1, d2 = random.sample(t_list, 2)
        t_list_1 = sorted(t_list)

        if t_list_1[0] != d1 and t_list_1[0] != d2 and t_list_1[-1] != d1 and t_list_1[-1] != d2 and d1 < d2:
            break

    b1 = "box{``%d``}" % t1
    b2 = "box{``%d``}" % t2
    b3 = "box{``%d``}" % t3
    b4 = "box{``%d``}" % t4
    b5 = "box{``%d``}" % t5

    c2 = d1 * 10 + t_list_1[-1]
    c3 = d2 * 10 + t_list_1[0]

    c1 = " ` &lt; ` ".join(list(map(str, t_list_1)))
    c4 = " ` &gt; ` ".join(list(reversed(list(map(str, t_list_1)))))

    ans = c3 - c2

    stem = stem.format(b1=b1, b2=b2, b3=b3, b4=b4, b5=b5, d1=d1, d2=d2)
    answer = answer.format(ans=ans)
    comment = comment.format(d1=d1, d2=d2, c1=c1, c2=c2, c3=c3, c4=c4, ans=ans)

    return stem, answer, comment
















# 2-1-3-31
def addandsub213_Stem_015():
    """

    :param r1: 정수 범위 최솟값 [int] {10:10}
    :param r2: 정수 범위 최댓값 [int] {99:99}
    :param r3: 숫자 카드 범위 최솟값 [int] {1:1}
    :param r4: 숫자 카드 범위 최댓값 [int] {9:9}
    :return:
    """
    stem = "숫자 카드 $$수식$$2$$/수식$$장을 골라 두 자리 수를 만들어 $$수식$${d1}$$/수식$$에서 빼려고 합니다. 계산 결과가 가장 작은 수가 되는 뺄셈식을 쓰고 계산해 보세요.\n$$수식$${b1}$$/수식$$  $$수식$${b2}$$/수식$$  $$수식$${b3}$$/수식$$  $$수식$${b4}$$/수식$$\n$$수식$${d1} ` - ` $$/수식$$ $$수식$${b5}$$/수식$$$$수식$$` = `$$/수식$$$$수식$${b6}$$/수식$$\n"
    answer = "(정답)\n$$수식$${ans1}$$/수식$$, $$수식$${ans2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${d1}$$/수식$$에서 뺀 계산 결과가 가장 작은 수가 되려면 가장 큰 수를 만들어 빼 주어야 합니다. 그러므로 숫자 카드 $$수식$$2$$/수식$$장을 골라 만들 수 있는 가장 큰 수는 $$수식$${ans1}$$/수식$$입니다.\n" \
              "→ $$수식$${d1} ` - ` {ans1} ` = ` {ans2}$$/수식$$\n\n"


    r1 = 10
    r2 = 99
    r3 = 1
    r4 = 9


    while True:
        d1 = random.randint(r1, r2)

        t1, t2, t3, t4 = random.sample([j for j in range(r3, r4) if d1 // 10 != j], 4)

        a_list = [i for i in [t1, t2, t3, t4] if d1 % 10 < i]
        b_list = [i for i in [t1, t2, t3, t4] if d1 // 10 > i]


        if len(a_list) > 0 and len(b_list) > 0 and d1 % 10 != 0 and max(a_list) != max(b_list):
            break

    ans1 = max(b_list) * 10 + max(a_list)
    ans2 = d1 - ans1


    b1 = "box{``%d``}" % t1
    b2 = "box{``%d``}" % t2
    b3 = "box{``%d``}" % t3
    b4 = "box{``%d``}" % t4
    b5 = "box{~%s~}" % "①"
    b6 = "box{~%s~}" % "②"

    stem = stem.format(b1=b1, b2=b2, b3=b3, b4=b4, b5=b5, b6=b6, d1=d1)
    answer = answer.format(ans1=ans1, ans2=ans2)
    comment = comment.format(d1=d1, ans1=ans1, ans2=ans2)

    return stem, answer, comment


























# 2-1-3-32
def addandsub213_Stem_016():
    """

    :param r1: 정수 범위 최솟값 [int] {10:10}
    :param r2: 정수 범위 최댓값 [int] {100:100}
    :return:
    """
    stem = "$$수식$${b1}$$/수식$$ 안에 알맞은 수가 더 큰 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${d1} ` + ` {b1} ` = ` {d2}$$/수식$$   ㉡ $$수식$${b1} ` + ` {d3} ` = ` {d4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${d1} ` + ` {b1} ` = ` {d2}$$/수식$$ → $$수식$${d2} ` - ` {d1} ` = ` {b1}$$/수식$$, $$수식$${b1} ` = ` {c1}$$/수식$$\n" \
              "㉡ $$수식$${b1} ` + ` {d3} ` = ` {d4}$$/수식$$ → $$수식$${d4} ` - ` {d3} ` = ` {b1}$$/수식$$, $$수식$${b1} ` = ` {c2}$$/수식$$\n" \
              "따라서 $$수식$${c3}$$/수식$$이므로 $$수식$${b1}$$/수식$$ 안에 알맞은 수가 더 큰 것은 {ans}입니다.\n\n"


    r1 = 10
    r2 = 100


    while True:
        d1, d2, d3, d4 = random.sample(range(r1, r2), 4)

        if d2 > d1 and d4 > d3 and d2 % 10 < d1 % 10 and d4 % 10 < d3 % 10:
            c1 = d2 - d1
            c2 = d4 - d3
            if c1 != c2:
                break


    if c1 > c2:
        ans = "㉠"
        c3 = "%d ` &gt; ` %d" % (c1, c2)
    else:
        ans = "㉡"
        c3 = "%d ` &lt; ` %d" % (c1, c2)

    b1 = "□"

    stem = stem.format(d1=d1, d2=d2, d3=d3, d4=d4, b1=b1)
    answer = answer.format(ans=ans)
    comment = comment.format(d1=d1, d2=d2, d3=d3, d4=d4, c1=c1, c2=c2, c3=c3, b1=b1, ans=ans)

    return stem, answer, comment



























# 2-1-3-33
def addandsub213_Stem_017():
    """

    :param r1: 정수 범위 최솟값 [int] {10:10}
    :param r2: 정수 범위 최댓값 [int] {100:100}
    :return:
    """
    stem = "$$수식$${b1}$$/수식$$의 값을 구하는 방법이 잘못된 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${a1}$$/수식$$\n㉡ $$수식$${a2}$$/수식$$\n㉢ $$수식$${a3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "{ans} {c1}\n\n"


    r1 = 10
    r2 = 100


    while True:
        t1, t2, t3, t4, t5, t6 = random.sample(range(r1, r2), 6)

        if t1 > t2 and t4 > t3 and t6 > t5 and (t1 % 10) < (t2 % 10) and (t1 % 10) + (t2 % 10) > 10 and (t4 % 10) < (t3 % 10) \
                and (t4 % 10) + (t3 % 10) > 10 and (t6 % 10) < (t5 % 10) and (t6 % 10) + (t5 % 10) > 10:
            break

    b1 = "□"
    ans_num = random.randint(0, 2)

    exp_dict = [{True: "$$수식$$%d ` - ` %s ` = ` %d$$/수식$$ → $$수식$$%d ` - ` %d ` = ` %s$$/수식$$" % (t1, b1, t2, t1, t2, b1),
                 False: "$$수식$$%d ` - ` %s ` = ` %d$$/수식$$ → $$수식$$%d ` + ` %d ` = ` %s$$/수식$$" % (t1, b1, t2, t1, t2, b1)},
                {True: "$$수식$$%s ` + ` %d ` = ` %d$$/수식$$ → $$수식$$%d ` - ` %d ` = ` %s$$/수식$$" % (b1, t3, t4, t4, t3, b1),
                 False: "$$수식$$%s ` + ` %d ` = ` %d$$/수식$$ → $$수식$$%d ` + ` %d ` = ` %s$$/수식$$" % (b1, t3, t4, t4, t3, b1)},
                {True: "$$수식$$%s ` - ` %d ` = ` %d$$/수식$$ → $$수식$$%d ` + ` %d ` = ` %s$$/수식$$" % (b1, t5, t6, t6, t5, b1),
                 False: "$$수식$$%s ` - ` %d ` = ` %d$$/수식$$ → $$수식$$%d ` - ` %d ` = ` %s$$/수식$$" % (b1, t5, t6, t6, t5, b1)},
                ]

    c_list = ["$$수식$$%d ` - ` %s ` = ` %d$$/수식$$ → $$수식$$%d ` - ` %d ` = ` %s$$/수식$$" % (t1, b1, t2, t1, t2, b1), "$$수식$$%s ` + ` %d ` = ` %d$$/수식$$ → $$수식$$%d ` - ` %d ` = ` %s$$/수식$$" % (b1, t3, t4, t4, t3, b1), "$$수식$$%s ` - ` %d ` = ` %d$$/수식$$ → $$수식$$%d ` + ` %d ` = ` %s$$/수식$$" % (b1, t5, t6, t6, t5, b1)]

    c1 = ""
    answers_t = []
    for i in range(3):
        if i == ans_num:
            answers_t.append(exp_dict[i][False])
            c1 = c_list[i]
        else:
            answers_t.append(exp_dict[i][True])

    multiple_choice = ["㉠", "㉡", "㉢"]

    random.shuffle(answers_t)
    a1, a2, a3 = answers_t

    ans = multiple_choice[answers_t.index(exp_dict[ans_num][False])]

    stem = stem.format(a1=a1, a2=a2, a3=a3, b1=b1)
    answer = answer.format(ans=ans)
    comment = comment.format(ans=ans, c1=c1)

    return stem, answer, comment























# 2-1-3-34
def addandsub213_Stem_018():
    """

    :param r1: 정수 범위 최솟값 [int] {10:10}
    :param r2: 정수 범위 최댓값 [int] {100:100}
    :return:
    """
    stem = "어떤 수보다 $$수식$${d1}$$/수식$$ 작은 수는 $$수식$${d2}$$/수식$${j1} $$수식$${d3}$$/수식$$의 합과 같습니다. 어떤 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 $$수식$${b1}$$/수식$$라고 하면\n" \
              "$$수식$${b1} ` - ` {d1} ` = ` {d2} ` + ` {d3}$$/수식$$, $$수식$${b1} ` - ` {d1} ` = ` {c1}$$/수식$$\n" \
              "→ $$수식$${c1} ` + ` {d1} ` = ` {b1}$$/수식$$, $$수식$${b1} ` = ` {ans}$$/수식$$\n" \
              "따라서 어떤 수는 $$수식$${ans}$$/수식$$입니다.\n\n"


    r1 = 10
    r2 = 100


    while True:
        d1, d2, d3 = random.sample(range(r1, r2), 3)

        if (d2 % 10) + (d3 % 10) > 10 and ((d2 + d3) % 10) + (d1 % 10) > 10 and d1 + d2 + d3 < 100:
            break

    ans = d1 + d2 + d3
    b1 = "□"
    c1 = d2 + d3
    j1 = check_jongsung(d2)[0]

    stem = stem.format(d1=d1, d2=d2, d3=d3, j1=j1)
    answer = answer.format(ans=ans)
    comment = comment.format(d1=d1, d2=d2, d3=d3, b1=b1, c1=c1, ans=ans)

    return stem, answer, comment























# 2-1-3-35
def addandsub213_Stem_019():
    """

    :param r1: 정수 범위 최솟값 [int] {10:10}
    :param r2: 정수 범위 최댓값 [int] {100:100}
    :return:
    """
    stem = "$$수식$${d1}$$/수식$$에 어떤 수를 더할 것을 잘못하여 뺐더니 $$수식$${d2}$$/수식$${j1} 되었습니다. 바르게 계산하면 얼마일까요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 $$수식$${b1}$$/수식$$라 하면 $$수식$${d1} ` - ` {b1} ` = ` {d2}$$/수식$$이므로\n" \
              "$$수식$${d1} ` - ` {d2} ` = ` {b1}$$/수식$$, $$수식$${b1} ` = ` {c1}$$/수식$$입니다.\n" \
              "따라서 바르게 계산하면 $$수식$${d1} ` + ` {c1} ` = ` {ans}$$/수식$$입니다.\n\n"


    r1 = 10
    r2 = 100


    while True:
        d1, d2 = random.sample([i for i in range(r1, r2) if i % 10 != 0], 2)

        if d1 > d2 and d1 % 10 < d2 % 10 and 10 < d1 + d1 - d2 < 100 and ((d1 - d2) % 10) + (d1 % 10) > 10:
            break

    c1 = d1 - d2
    ans = d1 + c1
    b1 = "□"

    j1 = check_jongsung(d2)[3]

    stem = stem.format(d1=d1, d2=d2, j1=j1)
    answer = answer.format(ans=ans)
    comment = comment.format(b1=b1, c1=c1, d1=d1, d2=d2, ans=ans)

    return stem, answer, comment
























# 2-1-3-37
def addandsub213_Stem_020():
    """

    :param r1: 두자리 정수 범위 최솟값 [int] {10:10}
    :param r2: 두자리 정수 범위 최댓값 [int] {100:100}
    :param r3: 한자리 정수 범위 최솟값 [int] {1:1}
    :param r4: 한자리 정수 범위 최댓값 [int] {10:10}
    :return:
    """
    stem = "계산 결과가 더 큰 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${s1}$$/수식$$    ㉡ $$수식$${s2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${a1}$$/수식$$\n" \
              "㉡ $$수식$${a2}$$/수식$$\n" \
              "따라서 $$수식$${c1}$$/수식$$이므로 계산 결과가 더 큰 것은 {ans}입니다.\n\n"


    r1 = 10
    r2 = 100
    r3 = 1
    r4 = 10


    while True:
        d1, d2, d4, d6 = random.sample([i for i in range(r1, r2) if i % 10 != 0], 4)
        d3, d5 = random.sample(range(r3, r4), 2)

        t1 = d1 - d2 + d3
        t2 = d4 + d5 - d6

        s1 = "{d1} ` - ` {d2} ` + ` {d3}".format(d1=d1, d2=d2, d3=d3)
        s2 = "{d4} ` + ` {d5} ` - ` {d6}".format(d4=d4, d5=d5, d6=d6)

        a3 = "%s ` + ` %s ` = ` %s" % (d1-d2, d3, t1)
        a4 = "%s ` - ` %s ` = ` %s" % (d4+d5, d6, t2)

        if 100 > t1 > 10 and 100 > t2 > 10 and t1 != t2 and d1 - d2 > 0 and d4 + d5 < 100 and d1 % 10 < d2 % 10 and ((d1 - d2) % 10) + d3 > 10\
            and (d4 % 10) + d5 > 10 and (d4 + d5) % 10 < d6 % 10:
            break

    a_list = [(s1, t1, "{d1} ` - ` {d2} ` + ` {d3} ` = ` {a3}".format(d1=d1, d2=d2, d3=d3, a3=a3)), (s2, t2, "{d4} ` + ` {d5} ` - ` {d6} ` = ` {a4}".format(d4=d4, d5=d5, d6=d6, a4=a4))]
    random.shuffle(a_list)

    s1, t1, a1 = a_list[0]
    s2, t2, a2 = a_list[1]

    if t1 > t2:
        c1 = "%d ` &gt; ` %d" % (t1, t2)
        ans = "㉠"
    else:
        c1 = "%d ` &lt; ` %d" % (t1, t2)
        ans = "㉡"

    stem = stem.format(s1=s1, s2=s2)
    answer = answer.format(ans=ans)
    comment = comment.format(a1=a1, a2=a2, c1=c1, ans=ans)

    return stem, answer, comment


























# 2-1-3-38
def addandsub213_Stem_021():
    stem = "계산 결과가 $$수식$${s10}$$/수식$${j10} 되도록 □ 안에 $$수식$$+$$/수식$$, $$수식$$-$$/수식$$를 알맞게 써넣으세요.\n{a1}\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "{c1}\n\n"

    box = 'Box{　}'

    flag = True
    while flag:
        s1 = np.random.randint(10, 50, 1)[0]
        s2 = np.random.randint(10, 50, 1)[0]
        s3 = np.random.randint(10, 50, 1)[0]

        cor_text = []
        if s1 % 10 != 0 and s2 % 10 != 0 and s3 % 10 != 0 and s1 - s2 > 0:
            s4 = s1 + s2
            s5 = s1 - s2

            if s4 // 10 > (s1 // 10 + s2 // 10):
                cor_text.append('+')
                s6 = s4
            elif s5 // 10 < (s1 // 10 - s2 // 10):
                cor_text.append('-')
                s6 = s5

            if len(cor_text) == 1 and s6 % 10 != 0 and s6 - s3 > 0:
                s7 = s6 + s3
                s8 = s6 - s3
                if s7 // 10 > (s6 // 10 + s3 // 10):
                    cor_text.append('+')
                elif s8 // 10 < (s6 // 10 - s3 // 10):
                    cor_text.append('-')

                if len(cor_text) == 2:
                    s10_text = '%d %s %d %s %d' % (s1, cor_text[0], s2, cor_text[1], s3)
                    s10 = eval(s10_text)
                    if 0 < s10 < 100:

                        a1 = '$$수식$$%d$$/수식$$ $$수식$$%s$$/수식$$ $$수식$$%d$$/수식$$ $$수식$$%s$$/수식$$ $$수식$$%d$$/수식$$' % (s1, box, s2, box, s3)
                        cor_text = '$$/수식$$, $$수식$$'.join(cor_text).strip()

                        mode = [['+', '+'], ['-', '-'], ['+', '-'], ['-', '+']]
                        ans = []
                        comments = []
                        for m1, m2 in mode:
                            a_str = '%d %s %d %s %d' % (s1, m1, s2, m2, s3)
                            a_int = eval(a_str)
                            ans.append(a_int)

                            c = '$$수식$$%s ` = ` %d %s %d ` = ` %d ` ' % (a_str, eval('%d %s %d' % (s1, m1, s2)), m2, s3, a_int)
                            if a_int == s10:
                                c += 'LEFT ($$/수식$$○$$수식$$RIGHT )$$/수식$$'
                            else:
                                c += 'LEFT ($$/수식$$×$$수식$$RIGHT )$$/수식$$'

                            c = c.replace('+', ' ` + ` ').replace('-', ' ` - ` ')
                            comments.append(c)

                        if (((s1+s2) % 10 + s3 % 10) > 10 or ((s1-s2) % 10 - s3 % 10) < 0) and min(ans) > 0 and max(ans) < 100 :
                            flag = False

    c1 = '\n'.join(comments)
    cor_text = cor_text.replace('+', '` + `').replace('-', '` - `')
    j10 = '이' if int(str(s10)[-1]) in have_jongsung_num else '가'

    stem = stem.format(s10=s10, j10=j10, box=box, a1=a1)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1)

    return stem, answer, comment

























# 2-1-3-39
def addandsub213_Stem_022():
    stem = "{t1}{j1}는 {t2} $$수식$${s1}$$/수식$$장 중에서 {t3}{j3} 접는 데에 $$수식$${s2}$$/수식$$장을 쓰고, {t4}{j4} 접는 데에는 {t3}{j3} 접는 데에 쓴 {t2}보다 $$수식$${s3}$$/수식$$장을 더 많이 썼습니다. 남은 {t2}는 몇 장인가요?\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$장\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${t4}{j4} 접는 데 쓴 {t2}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$${t3}{j3} 접는 데 쓴 {t2}의 수$$수식$$RIGHT ) ` + ` {s3}$$/수식$$\n" \
              "$$수식$$= ` {s2} ` + ` {s3} ` = ` {s4} ` LEFT ($$/수식$$장$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$남은 {t2}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$처음에 가지고 있던 {t2}의 수$$수식$$RIGHT ) ` - ` LEFT ($$/수식$${t3}{j3} 접는 데 " \
              "쓴 {t2}의 수$$수식$$RIGHT ) ` - ` LEFT ($$/수식$${t4}{j4} 접는 데 쓴 색종이의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {s1} ` - ` {s2} ` - ` {s4} ` = ` {s5} ` - ` {s4} ` = ` {cor_text} ` LEFT ($$/수식$$장$$수식$$RIGHT )$$/수식$$\n\n"

    t1 = np.random.choice(person_nam+person_yeo, 1)[0]
    t2 = np.random.choice(['색종이'], 1)[0]
    t3, t4 = np.random.choice(['종이학', '종이배', '공', '장미'], 2, False)

    j1 = '' if josa_check(t1[-1]) == ' ' else '이'
    j2 = '를' if josa_check(t2[-1]) == ' ' else '을'
    j3 = '를' if josa_check(t3[-1]) == ' ' else '을'
    j4 = '를' if josa_check(t4[-1]) == ' ' else '을'

    flag = True
    while flag :
        s1 = np.random.randint(50, 100, 1)[0]
        s2 = np.random.randint(10, 100, 1)[0]
        s3 = np.random.randint(10, 100, 1)[0]

        if (s1 - s2*2 - s3) > 0 and s2 != s3 and s2 % 10 !=0 and s3 % 10 !=0 :
            s4 = s2 + s3
            if s4 // 10 > (s2 // 10 + s3 // 10) :
                s5 = s1 - s2
                if s5 // 10 < (s1 // 10 - s2 // 10) :
                    cor_text = s5 - s4
                    if cor_text // 10 < (s5 // 10 - s4 // 10) :
                        flag = False


    stem = stem.format(s1=s1, s2=s2, s3=s3, t1=t1, t2=t2, t3=t3, t4=t4, j1=j1, j2=j2, j3=j3, j4=j4)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, cor_text=cor_text, t1=t1, t2=t2, t3=t3, t4=t4, j1=j1, j2=j2, j3=j3, j4=j4)

    return stem, answer, comment


























# 2-1-3-40
def addandsub213_Stem_023():
    """

    :param r1: 정수 범위 최솟값 [int] {10:10}
    :param r2: 정수 범위 최댓값 [int] {100:100}
    :return:
    """
    stem = "■$$수식$$` = `{d1}$$/수식$$일 때 ●의 값을 구하세요.\n$$표$$(가) ■$$수식$$` + `$$/수식$$■$$수식$$` + `$$/수식$$★$$수식$$` = `{d2}$$/수식$$\n(나) ■$$수식$$` + `$$/수식$$★$$수식$$` + `$$/수식$$★$$수식$$` = `$$/수식$$●$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
             "■$$수식$$` = `{d1}$$/수식$$이므로 $$수식$${d1} ` + ` {d1} ` + `$$/수식$$★$$수식$$` = ` {d2}$$/수식$$, $$수식$${c1} ` + `$$/수식$$★$$수식$$` = ` {d2}$$/수식$$\n" \
             "→ $$수식$${d2} ` - ` {c1} ` = `$$/수식$$★, ★$$수식$$` = ` {c2}$$/수식$$\n" \
             "■$$수식$$` + `$$/수식$$★$$수식$$` + `$$/수식$$★$$수식$$` = ` {d1} ` + ` {c2} ` + ` {c2} ` = ` {c3} ` + ` {c2} ` = ` {ans}$$/수식$$\n" \
             "따라서 ●의 값은 $$수식$${ans}$$/수식$$입니다.\n\n"


    r1 = 10
    r2 = 100


    while True:
        d1, c2 = random.sample(range(r1, r2), 2)
        d2 = d1 + d1 + c2
        c1 = d1 + d1
        c3 = d1 + c2
        ans = c2 + c3

        if d2 < 100 and c1 < 100 and c3 < 100 and ans < 100 and ans % 10 != 0 and ((d1 * 2) % 10) + (c2 % 10) > 10 and (d1 % 10) * 2 > 10 and (d1 % 10) + (c2 % 10) > 10:
            break

    stem = stem.format(d1=d1, d2=d2)
    answer = answer.format(ans=ans)
    comment = comment.format(d1=d1, d2=d2, c1=c1, c2=c2, c3=c3, ans=ans)

    return stem, answer, comment




# if __name__ == '__main__':
#
#     AddAndSub_Stem_001()
#     AddAndSub_Stem_002()
#     AddAndSub_Stem_003()
#     AddAndSub_Stem_004()
#     AddAndSub_Stem_005()
#     AddAndSub_Stem_006()
#     AddAndSub_Stem_007()
#     AddAndSub_Stem_008()
#     AddAndSub_Stem_009()
#     AddAndSub_Stem_010()
#     AddAndSub_Stem_011()
#     AddAndSub_Stem_012()
#     AddAndSub_Stem_013()
#     AddAndSub_Stem_014()
#     AddAndSub_Stem_015()
#     AddAndSub_Stem_016()
#     AddAndSub_Stem_017()
#     AddAndSub_Stem_018()
#     AddAndSub_Stem_019()
#     AddAndSub_Stem_020()
#     AddAndSub_Stem_021()
#     AddAndSub_Stem_022()
#     AddAndSub_Stem_023()
