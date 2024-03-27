import numpy as np
import random
import codecs
import decimal
import os



PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../Dictionary')



person_nam = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XY.txt'), 'r', 'utf-8').readlines()]
person_yeo = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XX.txt'), 'r', 'utf-8').readlines()]


have_jongsung_num = [0, 1, 3, 6, 7, 8]
multiple_choice_jaem = {0: '㉠', 1: '㉡', 2: '㉢', 3: '㉣'}
multiple_choice_nums = {0: '①', 1: '②', 2: '③', 3: '④', 4: '⑤'}
multiple_choice_nums_2 = {0: '㉠', 1: '㉡', 2: '㉢', 3: '㉣', 4: '㉤'}



circle_snack = ['초코파이', '피자', '파이', '수박', '애플파이']
box = "□"
box_1 = "box{　　　}"
box_2 = "box{　　　}"
left = '&gt;'
right = '&lt;'
equal = '='



# 조사 확인(숫자 뒤)
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







# 조사 확인(이름 뒤)
def josa_check(name):
    JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                     'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    char_code = ord(name) - 44032
    ch1 = int(char_code / 588)
    ch2 = int((char_code - (588 * ch1)) / 28)
    ch3 = int((char_code - (588 * ch1) - (28 * ch2)))

    return JONGSUNG_LIST[ch3]










# 약수
def get_factors(num) :
    factors = []
    for i in range(1, num+1) :
        if num % i == 0 :
            factors.append(i)

    return factors



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



# 조사 확인(숫자 뒤) ver2
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



# 조사 확인(이름 뒤) ver2
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



# 조사 확인(숫자 뒤) ver3
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












# 3-1-6-13
def fraanddec316_Stem_001():
    stem = "분모가 $$수식$${s1}$$/수식$$이고 분자가 $$수식$${s2}$$/수식$$인 분수를 써 보세요.\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "분모가 $$수식$${s1}$$/수식$$이고 분자가 $$수식$${s2}$$/수식$$인 수는 $$수식$${cor_text}$$/수식$$입니다.\n\n"


    while True :
        s1 = np.random.randint(1, 10, 1)[0]
        s2 = np.random.randint(2, 10, 1)[0]
        checking = check_simFrac(s1, s2)

        if s1 > s2 and checking == True:
            break

    cor_text = "{%d} over {%d}" % (s2, s1)

    stem = stem.format(s1=s1, s2=s2)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s1=s1, s2=s2, cor_text=cor_text)

    return stem, answer, comment





















# 3-1-6-22
def fraanddec316_Stem_002():
    stem = "$$수식$${box}$$/수식$$ 안에 알맞은 수를 써 넣으세요.\n$$수식$$LEFT ( 1 RIGHT ) ```` {f1}$$/수식$${j1} $$수식$${f2}$$/수식$$이 $$수식$${box_1}$$/수식$$개입니다.\n$$수식$$LEFT ( 2 RIGHT ) ```` {f3}$$/수식$${j2} $$수식$${f4}$$/수식$$이 $$수식$${box_2}$$/수식$$개입니다.\n"
    answer = "(정답)\n$$수식$${s1}$$/수식$$, $$수식$${s3}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1 RIGHT ) ```` {f1}$$/수식$${j1} $$수식$${f2}$$/수식$$이 $$수식$${s1}$$/수식$$개입니다.\n" \
              "$$수식$$LEFT ( 2 RIGHT ) ```` {f3}$$/수식$${j2} $$수식$${f4}$$/수식$$이 $$수식$${s3}$$/수식$$개입니다.\n\n"


    flag = True

    while flag:
        s1, s2, s3, s4 = np.random.choice(np.arange(2, 10), 4, False)
        s1_factor = get_factors(s1)
        s3_factor = get_factors(s3)

        if (s2 not in s1_factor) and (s4 not in s3_factor) and (check_simFrac(s1, s2) == True) and (check_simFrac(s3, s4) == True):
            s1, s2 = sorted([s1, s2])
            s3, s4 = sorted([s3, s4])
            flag = False

    f1 = "{%d} over {%d}" % (s1, s2)
    f2 = "{1} over {%d}" % (s2)
    f3 = "{%d} over {%d}" % (s3, s4)
    f4 = "{1} over {%d}" % (s4)

    j1 = '은' if s1 in have_jongsung_num else '는'
    j2 = '은' if s3 in have_jongsung_num else '는'

    stem = stem.format(box=box, f1=f1, f2=f2, f3=f3, f4=f4, box_1=box_1, box_2=box_2, j1=j1, j2=j2)
    answer = answer.format(s1=s1, s3=s3)
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, s1=s1, s3=s3, j1=j1, j2=j2)

    return stem, answer, comment



















# 3-1-6-23
def fraanddec316_Stem_003():
    stem = "분수의 크기를 비교하여 $$수식$${box}$$/수식$$안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$표$$$$수식$${f1} ~ {box} ~ {f2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "분자의 크기를 비교하면 $$수식$${s2} ` {cor_text} ` {s3}$$/수식$$이므로 $$수식$${f1} ` {cor_text} ` {f2}$$/수식$$입니다.\n\n"


    flag = True

    while flag:
        s1 = np.random.randint(3, 10, 1)[0]
        s2, s3 = np.random.choice(np.arange(1, 10), 2)
        if s2 < s1 and s3 < s1:
            if check_simFrac(s1, s2) == True and check_simFrac(s1, s3) == True:
                flag = False

    f1 = "{%d} over {%d}" % (s2, s1)
    f2 = "{%d} over {%d}" % (s3, s1)

    cor_text = left if s2 > s3 else equal if s2 == s3 else right

    stem = stem.format(box=box, f1=f1, f2=f2)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s2=s2, s3=s3, f1=f1, f2=f2, cor_text=cor_text)

    return stem, answer, comment


























# 3-1-6-24
def fraanddec316_Stem_004():
    stem = "$$수식$${f1}$$/수식$${j1} 바르게 설명한 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${f2}$$/수식$$이 $$수식$${s2}$$/수식$$개인 수입니다.\n㉡ $$수식$${f3}$$/수식$$이 $$수식$${s1}$$/수식$$개인 수입니다.$$/표$$\n"
    answer = "(정답)\n{cor_text}\n"
    comment = "(해설)\n" \
              "$$수식$${f1}$$/수식$${j2} $$수식$${f4}$$/수식$$이 $$수식$${s3}$$/수식$$개인 수입니다.\n\n"


    flag = True

    while flag:
        s1, s2 = np.random.choice(np.arange(2, 10), 2, False)

        if check_simFrac(s1, s2) == True:
            f2 = "{1} over {%d}" % (s1)
            f3 = "{1} over {%d}" % (s2)
            cor_text = "㉠" if s1 > s2 else "㉡"
            flag = False

    s3, s4 = sorted([s1, s2])
    f1 = "{%d} over {%d}" % (s3, s4)
    f4 = "{1} over {%d}" % (s4)


    j1, j2 = ['을', '은'] if s3 in have_jongsung_num else ['를', '는']


    stem = stem.format(f1=f1, f2=f2, f3=f3, s1=s1, s2=s2, j1=j1)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(f1=f1, f4=f4, j2=j2, s3=s3)

    return stem, answer, comment






















# 3-1-6-26
def fraanddec316_Stem_005():
    stem = "분수의 크기를 비교하여 큰 수부터 기호를 차례대로 써 보세요.\n$$표$$㉠ $$수식$${a1}$$/수식$$    ㉡ $$수식$${a2}$$/수식$$    ㉢ $$수식$${a3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{xa}\n"
    comment = "(해설)\n" \
              "분모가 같으므로 분자의 크기를 비교하면 $$수식$${c1}$$/수식$$이므로 $$수식$${cor_text}$$/수식$$입니다.\n\n"


    flag = True

    while flag:
        s1 = np.random.randint(11, 20, 1)[0]
        nums = np.random.choice(np.arange(1, 20), 3, False)
        np.random.shuffle(nums)
        s2, s3, s4 = nums
        if s1 != s2 and s1 != s3 and s1 != s4 and s1 > max([s2, s3, s4]):
            if check_simFrac(s1, s2) == True and check_simFrac(s1, s3) == True and check_simFrac(s1, s4) == True:
                flag = False

    ans_dict = {}
    answers = []

    for i in [s2, s3, s4] :
        ans_dict[i] = '{%d} over {%d}' % (i, s1)
        answers.append('{%d} over {%d}' % (i, s1))

    a1, a2, a3 = answers

    numers = list(map(str, sorted(list(ans_dict.keys()), reverse=True)))
    cor_text = [ans_dict.get(int(i)) for i in numers]
    cor_text = ('`%s`' % left).join(cor_text)
    c1 = ('`%s`' % left).join(numers)

    if s2 > s3 and s3 > s4:
        xa = "㉠, ㉡, ㉢"
    elif s2 > s3 and s2 > s4 and s4 > s3:
        xa = "㉠, ㉢, ㉡"
    elif s3 > s2 and s2 > s4:
        xa = "㉡, ㉠, ㉢"
    elif s3 > s2 and s3 > s4 and s4 > s2:
        xa = "㉡, ㉢, ㉠"
    elif s4 > s2 and s2 > s3:
        xa = "㉢, ㉠, ㉡"
    else:
        xa = "㉢, ㉡, ㉠"

    stem = stem.format(a1=a1, a2=a2, a3=a3)
    answer = answer.format(xa=xa)
    comment = comment.format(c1=c1, cor_text=cor_text)


    return stem, answer, comment























# 3-1-6-27
def fraanddec316_Stem_006():
    stem = "가장 큰 분수와 가장 작은 분수를 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${a1}$$/수식$$    ㉡ $$수식$${a2}$$/수식$$    ㉢ $$수식$${a3}$$/수식$$    ㉣ $$수식$${a4}$$/수식$$$$/표$$\n" \
        "가장 큰 분수 : {boxblank}, 가장 작은 분수 : {boxblank}"
    answer = "(정답)\n{cor_num1}, {cor_num2}\n"
    comment = "(해설)\n" \
              "분모가 같은 분수는 분자가 클수록 큰 수이므로 가장 큰 분수는 $$수식$${c1}$$/수식$$이고, 가장 작은 분수는 $$수식$${c2}$$/수식$$입니다.\n\n"

    boxblank = "$$수식$$box{　　}$$/수식$$"
    
    flag = True

    while flag:
        s1 = np.random.randint(11, 30, 1)[0]
        s2, s3, s4, s5 = np.random.choice(np.arange(1, s1), 4, False)
        if check_simFrac(s1, s2) and check_simFrac(s1, s3) and check_simFrac(s1, s4) and check_simFrac(s1, s5):
            flag = False

    numers = [s2, s3, s4, s5]
    ans_dict = {}
    answers = []

    for i in numers:
        ans_dict[i] = '{%d} over {%d}' % (i, s1)
        answers.append('{%d} over {%d}' % (i, s1))

    a1, a2, a3, a4 = answers
    cor_num1 = multiple_choice_jaem.get(numers.index(max(numers)))
    cor_num2 = multiple_choice_jaem.get(numers.index(min(numers)))

    c1 = ans_dict.get(max(numers))
    c2 = ans_dict.get(min(numers))

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, boxblank=boxblank)
    answer = answer.format(cor_num1=cor_num1, cor_num2=cor_num2)
    comment = comment.format(c1=c1, c2=c2)

    return stem, answer, comment
























# 3-1-6-28
def fraanddec316_Stem_007():
    stem = "분모가 $$수식$${s1}$$/수식$$인 분수 중에서 $$수식$${f1}$$/수식$$보다 크고 $$수식$${f2}$$/수식$$보다 작은 분수를 모두 찾아 써보세요.\n$$표$$$$수식$${a1}$$/수식$$    $$수식$${a2}$$/수식$$    $$수식$${a3}$$/수식$$    $$수식$${a4}$$/수식$$    $$수식$${a5}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${f3}$$/수식$$, $$수식$${f4}$$/수식$$\n"
    comment = "(해설)\n" \
              "분모가 같은 분수는 분자가 클수록 큰 수이므로 분자가 $$수식$${s2}$$/수식$$보다 크고 $$수식$${s8}$$/수식$$보다 작은 분수를 모두 찾습니다.\n" \
              "따라서 분모가 $$수식$${s1}$$/수식$$인 분수 중에서 $$수식$${f1}$$/수식$$보다 크고 $$수식$${f2}$$/수식$$보다 작은 분수는 $$수식$${f3}$$/수식$$, $$수식$${f4}$$/수식$$입니다.\n\n"


    flag = True

    while flag:
        s1 = np.random.randint(21, 30, 1)[0]
        s2 = np.random.randint(11, s1-1, 1)[0]
        try:
            s3, s4 = sorted(list(np.random.choice(np.arange(s2, s1-1), 2, False)))
            s5, s6 = np.random.choice(np.arange(1, s2-1), 2, False)
            s7, s8 = np.random.choice(np.arange(s1+1, 30), 2, False)
            if len(set([s1, s2, s3, s4, s5, s6, s7, s8])) == 8:
                if check_simFrac(s1, s2) and check_simFrac(s1, s3) and check_simFrac(s1, s4) and check_simFrac(s1, s5) \
                    and check_simFrac(s1, s6) and check_simFrac(s1, s7) and check_simFrac(s1, s8):
                    s5, s6, s7 = np.random.choice([s5, s6, s7, s8], 3, False)
                    s8 = s1-1
                    flag = False
                    
        except:
            continue


    f1 = '{%d} over {%d}' % (s2, s1)
    f2 = '{%d} over {%d}' % (s8, s1)
    f3 = '{%d} over {%d}' % (s3, s1)
    f4 = '{%d} over {%d}' % (s4, s1)

    numers = [s3, s4, s5, s6, s7]
    np.random.shuffle(numers)
    answers = []

    for n in numers:
        answers.append('{%d} over {%d}' % (n, s1))

    a1, a2, a3, a4, a5 = answers

    stem = stem.format(s1=s1, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, f1=f1, f2=f2)
    answer = answer.format(f3=f3, f4=f4)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s8=s8, f1=f1, f2=f2, f3=f3, f4=f4)
    return stem, answer, comment






















# 3-1-6-29
def fraanddec316_Stem_008():
    stem = "$$수식$${box}$$/수식$$ 안에 들어갈 수 있는 자연수 중에서 가장 작은 수를 구해보세요.\n$$표$$$$수식$${f1} ` {right} ` {f2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "분모가 같은 분수는 분자가 클수록 큰 수입니다.\n" \
              "$$수식$${f1} ` {right} ` {f2}$$/수식$$에서 $$수식$${s2} ` {right} ` {box}$$/수식$$이므로 $$수식$${box} ` = `$$/수식$$ {c1}입니다.\n" \
              "따라서 가장 작은 수는 $$수식$${cor_text}$$/수식$$입니다.\n\n"


    flag = True
    while flag :
        s1 = np.random.randint(2, 8, 1)[0]
        s2 = np.random.randint(s1, s1+4, 1)[0]
        if check_simFrac(s1, s2) :
            flag = False

    f1 = '{%d} over {%d}' % (s2, s1)
    f2 = '{%s} over {%d}' % (box, s1)

    c1 = '$$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$CDOTS$$/수식$$' % (s2+1, s2+2, s2+3)
    cor_text = s2+1

    stem = stem.format(box=box, f1=f1, f2=f2, right=right)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(f1=f1, f2=f2, right=right, s2=s2, box=box, c1=c1, cor_text=cor_text)

    return stem, answer, comment





# 3-1-6-30
def fraanddec316_Stem_009():
    stem = "{t1}{j1}와 {t2}{j2}는 각각 같은 {t3}{j5} 한 병씩 사서 마신 후 남은 양을 알아보니 {t1}{j1}는 전체의 $$수식$${f1}$$/수식$$, {t2}{j2}는 전체의 $$수식$${f2}$$/수식$${j3} 남았습니다. {t3}{j5} 더 많이 마신 사람은 누구인가요?\n"
    answer = "(정답)\n{cor_text}\n"
    comment = "(해설)\n" \
              "남은 {t3}의 양을 비교하면 $$수식$${c1}$$/수식$$입니다.\n" \
              "남은 {t3}의 양이 적은 사람이 {t3}{j5} 더 많이 마신 것이므로 {cor_text}{j4}가 {t3}{j5} 더 많이 마셨습니다.\n\n"


    t1, t2 = np.random.choice(person_nam+person_yeo, 2, False)
    j1 = '' if josa_check(t1[-1]) == ' ' else '이'
    j2 = '' if josa_check(t2[-1]) == ' ' else '이'

    t3 = np.random.choice(['음료수', '우유', '물', '주스'], 1)[0]
    j5 = '를' if josa_check(t3[-1]) == ' ' else '을'

    flag = True
    while flag :
        s2 = np.random.randint(3, 10, 1)[0]
        s3 = np.random.randint(s2, 10, 1)[0]
        s1 = np.random.randint(s3, 20, 1)[0]

        if len(set([s1, s2, s3])) == 3 :
            if check_simFrac(s1, s2) and check_simFrac(s1, s3) :
                s2, s3 = sorted([s2, s3])
                flag = False

    c1 = '{%d} over {%d} ` %s ` {%d} over {%d}' % (s2, s1, right, s3, s1)
    mode = np.random.choice([0, 1], 1)[0]
    if mode == 0 :
        f1 = '{%d} over {%d}' % (s2, s1)
        f2 = '{%d} over {%d}' % (s3, s1)
        j3 = '이' if s3 % 10 in have_jongsung_num else '가'
        cor_text = t1
        j4 = j1

    else :
        f1 = '{%d} over {%d}' % (s3, s1)
        f2 = '{%d} over {%d}' % (s2, s1)
        j3 = '이' if s2 % 10 in have_jongsung_num else '가'
        cor_text = t2
        j4 = j2


    stem = stem.format(f1=f1, f2=f2, t1=t1, t2=t2, t3=t3, j1=j1, j2=j2, j3=j3, j5=j5)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(t3=t3, c1=c1, j4=j4, j5=j5, cor_text=cor_text)

    return stem, answer, comment















# 3-1-6-31
def fraanddec316_Stem_010():
    stem = "다음 조건에 알맞은 분수는 모두 몇 개인가요? $$수식$$LEFT ($$/수식$$단, 분모는 $$수식$${s1}$$/수식$$보다 큽니다.$$수식$$RIGHT )$$/수식$$\n$$표$$나는 $$수식$${f1}$$/수식$$보다 크고 분자는 $$수식$${s1}$$/수식$${j1}야.$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$개\n"
    comment = "(해설)\n" \
              "분자가 $$수식$${s1}$$/수식$${j1}고 $$수식$${f1}$$/수식$$보다 크려면 분모가 $$수식$${s2}$$/수식$$보다 작아야 합니다.\n" \
              "분모가 될 수 있는 수는 $$수식$${c1}$$/수식$$입니다.\n" \
              "따라서 조건에 알맞은 분수는 $$수식$${c2}$$/수식$${j2}로 모두 $$수식$${cor_text}$$/수식$$개입니다.\n\n"


    flag = True

    while flag:
        s1 = np.random.randint(2, 10, 1)[0]
        s2 = np.random.randint(s1+7, 20, 1)[0]
        if check_simFrac(s1, s2):
            flag = False

    f1 = '{%d} over {%d}' % (s1, s2)
    c_nums = list(np.arange(s1+1, s2))
    answers = ['{%d} over {%d}' % (s1, i) for i in c_nums]

    if len(answers) < 5:
        c1 = '$$/수식$$, $$수식$$'.join(c_nums)
        c2 = '$$/수식$$, $$수식$$'.join(answers)
    else:
        c_nums = list(map(str, c_nums))
        c1 = '$$/수식$$, $$수식$$'.join(c_nums[:3]) + '$$/수식$$, $$수식$$CDOTS$$/수식$$, $$수식$$%s' % (c_nums[-1])
        c2 = '$$/수식$$, $$수식$$'.join(answers[:3]) + '$$/수식$$, $$수식$$CDOTS$$/수식$$, $$수식$$%s' % (answers[-1])

    j2 = '으' if int(c_nums[-1]) % 10 in have_jongsung_num else ''
    cor_text = len(c_nums)
    j1 = '이' if s1 % 10 in have_jongsung_num else ''

    stem = stem.format(s1=s1, f1=f1, j1=j1)
    answer = answer.format(cor_text= cor_text)
    comment = comment.format(s1=s1, s2=s2, c1=c1, c2=c2, j1=j1, j2=j2, f1=f1, cor_text=cor_text)

    return stem, answer, comment


















# 3-1-6-33
def fraanddec316_Stem_011():
    """
    :param r1: 분모 범위 최솟값 [int] {2:2}
    :param r2: 분모 범위 최댓값 [int] {20:21}
    """
    stem = "$$수식$${b1}$$/수식$$ 안에 알맞은 분수를 써넣으세요.\n$$표$$세 분수 {f1}, {f2}, {f3} 중에서 가장 큰 분수는 $$수식$${b1}$$/수식$$ 입니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "분자가 모두 $$수식$$1$$/수식$$이므로 분모의 크기를 비교합니다.\n" \
              "따라서 $$수식$${c1} ` &gt; ` {c2} ` &gt; ` {c3}$$/수식$$에서 $$수식$${c4} ` &lt; ` {c5} ` &lt; ` {c6}$$/수식$$이므로 가장 큰 분수는 $$수식$${ans}$$/수식$$입니다.\n\n"



    r1 = 2
    r2 = 21


    b1 = "□"

    d1, d2, d3 = random.sample(range(r1, r2), 3)
    d_list = [d1, d2, d3]
    d_list.sort(reverse=True)

    c1, c2, c3 = d_list

    c4 = "{1} over {%d}" % (c1)
    c5 = "{1} over {%d}" % (c2)
    c6 = "{1} over {%d}" % (c3)

    f1 = "$$수식$${1} over {%d}$$/수식$$" % (d1)
    f2 = "$$수식$${1} over {%d}$$/수식$$" % (d2)
    f3 = "$$수식$${1} over {%d}$$/수식$$" % (d3)

    ans = c6

    stem = stem.format(b1=b1, f1=f1, f2=f2, f3=f3)
    answer = answer.format(ans=ans)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, ans=ans)

    return stem, answer, comment





















# 3-1-6-34
def fraanddec316_Stem_012():
    """
    :param r1: 분모 범위 최솟값 [int] {2:2}
    :param r2: 분모 범위 최댓값 [int] {15:16}
    """
    stem = "두 분수의 크기를 비교하여 $$수식$${box}$$/수식$$ 안에 $$수식$$&gt;$$/수식$$, $$수식$$&lt;$$/수식$$를 차례대로 알맞게 써넣으세요.\n(1) $$수식$${f1} ~ {box} ~ {f2}$$/수식$$\n(2) $$수식$${f3} ~ {box} ~ {f4}$$/수식$$\n"
    answer = "(정답)\n(1) $$수식$${ans1}$$/수식$$, (2) $$수식$${ans2}$$/수식$$\n"
    comment = "(해설)\n" \
              "(1) $$수식$${c1}$$/수식$$이므로 $$수식$${c2}$$/수식$$입니다.\n" \
              "(2) $$수식$${c3}$$/수식$$이므로 $$수식$${c4}$$/수식$$입니다.\n\n"



    r1 = 2
    r2 = 16


    d1, d2, d3, d4 = random.sample(range(r1, r2), 4)

    f1 = "{1} over {%d}" % d1
    f2 = "{1} over {%d}" % d2
    f3 = "{1} over {%d}" % d3
    f4 = "{1} over {%d}" % d4

    if d1 > d2:
        c1 = "%d ` &gt; ` %d" % (d1, d2)
        c2 = "{1} over {%d} ` &lt; ` {1} over {%d}" % (d1, d2)
        ans1 = "&lt;"
    else:
        c1 = "%d ` &lt; ` %d" % (d1, d2)
        c2 = "{1} over {%d} ` &gt; ` {1} over {%d}" % (d1, d2)
        ans1 = "&gt;"

    if d3 > d4:
        c3 = "%d ` &gt; ` %d" % (d3, d4)
        c4 = "{1} over {%d} ` &lt; ` {1} over {%d}" % (d3, d4)
        ans2 = "&lt;"
    else:
        c3 = "%d ` &lt; ` %d" % (d3, d4)
        c4 = "{1} over {%d} ` &gt; ` {1} over {%d}" % (d3, d4)
        ans2 = "&gt;"

    stem = stem.format(f1=f1, f2=f2, f3=f3, f4=f4, box=box)
    answer = answer.format(ans1=ans1, ans2=ans2)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4)

    return stem, answer, comment






















# 3-1-6-35
def fraanddec316_Stem_013():
    """
    :param r1: 분모 범위 최솟값 [int] {2:2}
    :param r2: 분모 범위 최댓값 [int] {15:16}
    """
    stem = "분수의 크기를 비교하여 작은 수부터 차례대로 써 보세요.\n$$표$$$$수식$${f1}$$/수식$$    $$수식$${f2}$$/수식$$    $$수식$${f3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ans1}$$/수식$$, $$수식$${ans2}$$/수식$$, $$수식$${ans3}$$/수식$$\n"
    comment = "(해설)\n" \
              "분모를 비교하면 $$수식$${c1} ` &gt; ` {c2} ` &gt; ` {c3}$$/수식$$이므로 단위분수의 크기를 비교하면 $$수식$${ans1} ` &lt; ` {ans2} ` &lt; ` {ans3}$$/수식$$ 입니다.\n" \
              "따라서 작은 수부터 차례대로 쓰면 $$수식$${ans1}$$/수식$$, $$수식$${ans2}$$/수식$$, $$수식$${ans3}$$/수식$$입니다.\n\n"



    r1 = 2
    r2 = 16


    d1, d2, d3 = random.sample(range(r1, r2), 3)
    f1 = "{1} over {%d}" % d1
    f2 = "{1} over {%d}" % d2
    f3 = "{1} over {%d}" % d3

    d_list = [d1, d2, d3]
    d_list.sort(reverse=True)

    c1, c2, c3 = d_list
    ans1 = "{1} over {%d}" % c1
    ans2 = "{1} over {%d}" % c2
    ans3 = "{1} over {%d}" % c3

    stem = stem.format(f1=f1, f2=f2, f3=f3)
    answer = answer.format(ans1=ans1, ans2=ans2, ans3=ans3)
    comment = comment.format(c1=c1, c2=c2, c3=c3, ans1=ans1, ans2=ans2, ans3=ans3)

    return stem, answer, comment





















# 3-1-6-36
def fraanddec316_Stem_014():
    """
    :param r1: 분모 범위 최솟값 [int] {2:2}
    :param r2: 분모 범위 최댓값 [int] {25:26}
    """
    stem = "분수의 크기를 잘못 비교한 것은 어느 것인가요?\n① $$수식$${a1}$$/수식$$\n② $$수식$${a2}$$/수식$$\n③ $$수식$${a3}$$/수식$$\n④ $$수식$${a4}$$/수식$$\n⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "{c1}\n\n"



    r1 = 2
    r2 = 26


    d1, d2, d3, d4, d5, d6, d7, d8, d9, d10 = random.sample(range(r1, r2), 10)

    if d1 > d2:
        t1 = "{1} over {%d} ` &lt; ` {1} over {%d}" % (d1, d2)
    else:
        t1 = "{1} over {%d} ` &gt; ` {1} over {%d}" % (d1, d2)

    if d3 > d4:
        t2 = "{1} over {%d} ` &lt; ` {1} over {%d}" % (d3, d4)
    else:
        t2 = "{1} over {%d} ` &gt; ` {1} over {%d}" % (d3, d4)

    if d5 > d6:
        t3 = "{1} over {%d} ` &lt; ` {1} over {%d}" % (d5, d6)
    else:
        t3 = "{1} over {%d} ` &gt; ` {1} over {%d}" % (d5, d6)

    if d7 > d8:
        t4 = "{1} over {%d} ` &lt; ` {1} over {%d}" % (d7, d8)
    else:
        t4 = "{1} over {%d} ` &gt; ` {1} over {%d}" % (d7, d8)

    if d9 > d10:
        t5 = "{1} over {%d} ` &gt; ` {1} over {%d}" % (d9, d10)
        c1 = "$$수식$$%d ` &gt; ` %d$$/수식$$이므로 $$수식$${1} over {%d} ` &lt; ` {1} over {%d}$$/수식$$입니다." % (d9, d10, d9, d10)
    else:
        t5 = "{1} over {%d} ` &lt; ` {1} over {%d}" % (d9, d10)
        c1 = "$$수식$$%d ` &lt; ` %d$$/수식$$이므로 $$수식$${1} over {%d} ` &gt; ` {1} over {%d}$$/수식$$입니다." % (d9, d10, d9, d10)

    answers = [t1, t2, t3, t4, t5]
    random.shuffle(answers)

    a1, a2, a3, a4, a5 = answers
    ans = multiple_choice_nums[answers.index(t5)]

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(ans=ans)
    comment = comment.format(c1=c1)

    return stem, answer, comment



















# 3-1-6-37
def fraanddec316_Stem_015():
    """
    :param r1: 분모 범위 최솟값 [int] {2:2}
    :param r2: 분모 범위 최댓값 [int] {9:9}
    """
    stem = "가장 큰 분수와 가장 작은 분수를 각각 찾아 기호를 써보세요.\n$$표$$㉠ $$수식$${f1}$$/수식$$    ㉡ $$수식$${f2}$$/수식$$    ㉢ $$수식$${f3}$$/수식$$    ㉣ $$수식$${f4}$$/수식$$    ㉤ $$수식$${f5}$$/수식$$$$/표$$\n" \
        "가장 큰 분수 : {boxblank}, 가장 작은 분수 : {boxblank}"
    answer = "(정답)\n{ans1}, {ans2}\n"
    comment = "(해설)\n" \
              "분모가 모두 $$수식$$1$$/수식$$이므로 분모의 크기를 비교합니다.\n" \
              "$$수식$${c1} ` &gt; ` {c2} ` &gt; ` {c3} ` &gt; ` {c4} ` &gt; ` {c5}$$/수식$$이므로\n" \
              "$$수식$${c6} ` &lt; ` {c7} ` &lt; ` {c8} ` &lt; ` {c9} ` &lt; ` {c10}$$/수식$$입니다.\n" \
              "따라서 가장 큰 분수는 $$수식$${c10}$$/수식$$, 가장 작은 분수는 $$수식$${c6}$$/수식$$입니다.\n\n"

    boxblank = "$$수식$$box{　　}$$/수식$$"

    r1 = 2
    r2 = 9


    t_choice = random.randint(r1, r2)

    t1 = [t_choice * 10, t_choice][np.random.randint(0, 2)]
    t2 = 100
    t3 = 1000
    t4 = 10
    t5 = t_choice * 100

    d_list = [t1, t2, t3, t4, t5]
    random.shuffle(d_list)

    d1, d2, d3, d4, d5 = d_list

    f1 = "{1} over {%d}" % d1
    f2 = "{1} over {%d}" % d2
    f3 = "{1} over {%d}" % d3
    f4 = "{1} over {%d}" % d4
    f5 = "{1} over {%d}" % d5

    f_list = [f1, f2, f3, f4, f5]

    d_list.sort(reverse=True)

    c1, c2, c3, c4, c5 = d_list

    c6 = "{1} over {%d}" % c1
    c7 = "{1} over {%d}" % c2
    c8 = "{1} over {%d}" % c3
    c9 = "{1} over {%d}" % c4
    c10 = "{1} over {%d}" % c5

    ans1 = multiple_choice_nums_2[f_list.index(c10)]
    ans2 = multiple_choice_nums_2[f_list.index(c6)]

    stem = stem.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, boxblank=boxblank)
    answer = answer.format(ans1=ans1, ans2=ans2)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10)

    return stem, answer, comment
























# 3-1-6-38
def fraanddec316_Stem_016():
    """
    :param r1: 분모 범위 최솟값 [int] {2:2}
    :param r2: 분모 범위 최댓값 [int] {9:9}
    """
    stem = "{s1}{j1} {name1}{j2} 전체의 $$수식$${f1}$$/수식$$, {name2}{j3} 전체의 $$수식$${f2}$$/수식$$, {name3}{j4} 전체의 $$수식$${f3}$$/수식$$을 먹었습니다. 가장 많이 먹은 사람은 누구인가요?\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "분자가 $$수식$$1$$/수식$$로 모두 같으므로 분모의 크기를 비교하면 $$수식$${c1} `&gt;` {c2} `&gt;` {c3}$$/수식$$이므로 $$수식$${c4} `&gt;` {c5} `&gt;` {c6}$$/수식$$입니다.\n" \
              "따라서 {s1}{j1} 가장 많이 먹은 사람은 {ans}입니다.\n\n"



    r1 = 2
    r2 = 11


    d1, d2, d3 = random.sample(range(r1, r2), 3)
    name1, name2, name3 = random.sample(person_nam + person_yeo, 3)
    s1 = random.choice(circle_snack)

    if josa_check(s1[-1]) == ' ':
        j1 = '를'
    else:
        j1 = '을'

    if josa_check(name1[-1]) == ' ':
        j2 = '는'
    else:
        j2 = '이는'

    if josa_check(name2[-1]) == ' ':
        j3 = '는'
    else:
        j3 = '이는'

    if josa_check(name3[-1]) == ' ':
        j4 = '는'
    else:
        j4 = '이는'


    f1 = "{1} over {%d}" % d1
    f2 = "{1} over {%d}" % d2
    f3 = "{1} over {%d}" % d3

    c_list = [d1, d2, d3]
    c_list.sort(reverse=True)
    c1, c2, c3 = c_list

    c4 = "{1} over {%d}" % c3
    c5 = "{1} over {%d}" % c2
    c6 = "{1} over {%d}" % c1

    name_list = {0: name1, 1: name2, 2: name3}
    ans_list = [f1, f2, f3]

    ans = name_list[ans_list.index(c4)]

    stem = stem.format(s1=s1, name1=name1, name2=name2, name3=name3, j1=j1, j2=j2, j3=j3, j4=j4, f1=f1, f2=f2, f3=f3)
    answer = answer.format(ans=ans)
    comment = comment.format(s1=s1, j1=j1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, ans=ans)

    return stem, answer, comment















# 3-1-6-39
def fraanddec316_Stem_017():
    """
    :param r1: 분모 범위 최솟값 [int] {2:2}
    :param r2: 분모 범위 최댓값 [int] {8:8}
    """
    stem = "$$수식$$2$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 중에서 $$수식$${b}$$/수식$$ 안에 들어갈 수 있는 수는 모두 몇 개인가요?\n$$표$$$$수식$${f1} ` &gt; ` {f2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${f1} ` &gt; ` {f2}$$/수식$$에서 $$수식$${d1} ` &lt; ` {b}$$/수식$$이므로 $$수식$${b}$$/수식$$ 안에 들어갈 수 있는 수는 {c1}{j1} 모두 $$수식$${ans}$$/수식$$개입니다.\n\n"



    r1 = 2
    r2 = 8


    b = "□"
    d1 = random.randint(r1, r2)
    f1 = "{1} over {%d}" % d1
    f2 = "{1} over {%s}" % b

    ans = 9 - d1

    c_list = [i for i in range(d1 + 1, 10)]

    c1 = ''
    for i in c_list:
        if i != 9:
            c1 += "$$수식$$%d$$/수식$$, " % i
        else:
            c1 += "$$수식$$%d$$/수식$$" % i

    j1 = check_jongsung(c_list[-1])[4]

    stem = stem.format(b=b, f1=f1, f2=f2)
    answer = answer.format(ans=ans)
    comment = comment.format(f1=f1, f2=f2, d1=d1, b=b, c1=c1, j1=j1, ans=ans)

    return stem, answer, comment





















# 3-1-6-40
def fraanddec316_Stem_018():
    """
    :param r1: 분모 범위 최솟값 [int] {2:2}
    :param r2: 분모 범위 최댓값 [int] {8:9}
    """
    stem = "{n1}, {n2}, {n3}{j1} 똑같은 컵에 물을 가득 따라 마셨습니다. 컵에 물이 $$수식$${f1}$$/수식$$, $$수식$${f2}$$/수식$$, $$수식$${f3}$$/수식$$만큼 남았습니다. 누구의 물이 가장 적게 남았나요?\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "분자가 $$수식$$1$$/수식$$로 모두 같으므로 분모의 크기를 비교하면 $$수식$${c1} ` &gt; ` {c2} ` &gt; ` {c3}$$/수식$$이므로 $$수식$${c4} ` &lt; ` {c5} ` &lt; ` {c6}$$/수식$$입니다.\n" \
              "따라서 물이 가장 적게 남은 사람은 {ans}입니다.\n\n"



    r1 = 2
    r2 = 9


    n1, n2, n3 = random.sample(person_nam + person_yeo, 3)

    if josa_check(n3[-1]) == ' ':
        j1 = '가'
    else:
        j1 = '이가'

    d1, d2, d3 = random.sample(range(r1, r2), 3)

    f1 = "{1} over {%d}" % d1
    f2 = "{1} over {%d}" % d2
    f3 = "{1} over {%d}" % d3

    c_list = [d1, d2, d3]
    c_list.sort(reverse=True)
    c1, c2, c3 = c_list

    c4 = "{1} over {%d}" % c1
    c5 = "{1} over {%d}" % c2
    c6 = "{1} over {%d}" % c3

    name_list = {0: n1, 1: n2, 2: n3}
    ans_list = [f1, f2, f3]

    ans = name_list[ans_list.index(c4)]

    stem = stem.format(n1=n1, n2=n2, n3=n3, j1=j1, f1=f1, f2=f2, f3=f3)
    answer = answer.format(ans=ans)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, ans=ans)

    return stem, answer, comment







# 3-1-6-41
def fraanddec316_Stem_019():
    """
    :param r1: 분모 범위 최솟값 [int] {2:2}
    :param r2: 분모 범위 최댓값 [int] {9:10}
    """

    stem = "분수를 소수로, 소수를 분수로 나타내어 보세요.\n$$수식$$LEFT ( 1 RIGHT ) ```` {f1} ` = ` $$/수식$$\n$$수식$$LEFT ( 2 RIGHT ) ```` {e1} ` = ` $$/수식$$\n"
    answer = "(정답)\n$$수식$${ans1}$$/수식$$, $$수식$${ans2} over {ans3}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1 RIGHT ) ```` {f1} ` = ` {ans1}$$/수식$$\n" \
              "$$수식$$LEFT ( 2 RIGHT ) ```` {e1} ` = ` {c1}$$/수식$$\n\n"


    r1 = 2
    r2 = 10



    d1, ans2 = random.sample(range(r1, r2), 2)

    f1 = "{%d} over {10}" % (d1)
    ans1 = "0.%d" % d1
    ans3 = 10

    e1 = "0.%d" % ans2
    f2 = "{%s} over {%s}" % (box, box)
    c1 = "{%d} over {%d}" % (ans2, ans3)

    stem = stem.format(f1=f1, e1=e1)
    answer = answer.format(ans1=ans1, ans2=ans2, ans3=ans3)
    comment = comment.format(f1=f1, ans1=ans1, e1=e1, c1=c1)

    return stem, answer, comment





















# 3-1-6-47
def fraanddec316_Stem_020():
    """
    :param r1: 분모 범위 최솟값 [int] {2:2}
    :param r2: 분모 범위 최댓값 [int] {9:9}
    """
    stem = "$$수식$${f}$$/수식$$이 $$수식$${d1}$$/수식$$개인 수를 분수와 소수로 각각 나타내어 보세요.\n" \
        "분수 : {boxblank}, 소수 : {boxblank}"
    answer = "(정답)\n$$수식$${ans1} over {ans2}$$/수식$$, $$수식$${ans3}.{ans4}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${f}$$/수식$$이 $$수식$${d1}$$/수식$$개인 수를 분수로 나타내면 $$수식$${c1}$$/수식$$이고, 소수로 나타내면 $$수식$${c2}$$/수식$$입니다.\n\n"

    boxblank = "$$수식$$box{　　}$$/수식$$"

    r1 = 2
    r2 = 9



    f = "{1} over {10}"
    d1 = random.randint(r1, r2)
    f1 = "{%s} over {%s}" % (box, box)

    ans1 = d1
    ans2 = 10
    ans3 = 0
    ans4 = d1

    c1 = "{%d} over {10}" % d1
    c2 = "0.%d" % d1

    stem = stem.format(f=f, d1=d1, f1=f1, box=box, boxblank=boxblank)
    answer = answer.format(ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4)
    comment = comment.format(f=f, d1=d1, c1=c1, c2=c2)

    return stem, answer, comment






# 3-1-6-50
def fraanddec316_Stem_021():
    '''
    :param r1: s1의 분자의 최솟값 [int] {2:3}
    :param r2: s1의 분자의 최댓값 [int] {8:9}
    :param r3: s2의 최솟값 [int] {2:3}
    :param r4: s2의 최댓값 [int] {8:9}
    '''
    stem = "㉠과 ㉡에 알맞은 수의 합은 얼마인가요?\n$$표$$$$수식$${s1}$$/수식$${s1_josa} $$수식$$0.1$$/수식$$이 ㉠개인 수와 같고, $$수식$${s2}$$/수식$${s2_josa} $$수식$${s3}$$/수식$$이 ㉡개인 수와 같습니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${s1}$$/수식$${s1_josa} $$수식$$0.1$$/수식$$이 $$수식$${c1}$$/수식$$개인 수와 같고,\n" \
              "$$수식$${s2}$$/수식$${s2_josa} $$수식$${s3}$$/수식$$이 $$수식$${c2}$$/수식$$개인 수와 같습니다.\n" \
              "따라서 ㉠$$수식$$` = ` {c1}$$/수식$$, ㉡$$수식$$` = ` {c2}$$/수식$$이므로\n" \
              "㉠$$수식$$` + `$$/수식$$㉡$$수식$$` = ` {c1} ` + ` {c2} = {cor_text}$$/수식$$입니다.\n\n"


    r1 = 2
    r2 = 9
    r3 = 2
    r4 = 9


    flag = True
    
    while flag:
        s1_nume = random.randint(r1, r2)
        s2 = random.randint(r3, r4)
        s3 = "{1} over {10}"

        if s1_nume != s2:
            c1 = s1_nume
            s1 = "{%s} over {%s}" % (s1_nume, 10)
            s1_josa = num_josa(s1_nume)[1]

            c2 = s2
            s2_josa = num_josa(s2)[1]
            s2 = decimal.Decimal('0.1') * s2

            cor_text = c1 + c2

            if r1 + r3 < cor_text < r2 + r4:
                flag = False

    stem = stem.format(s1=s1, s2=s2, s3=s3, s1_josa=s1_josa, s2_josa=s2_josa)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s1_josa=s1_josa, s2_josa=s2_josa, c1=c1, c2=c2, cor_text=cor_text)

    return stem, answer, comment
















# 3-1-6-51
def fraanddec316_Stem_022():
    '''
    :param r1: a의 최솟값 [int] {2:3}
    :param r2: a의 최댓값 [int] {8:9}
    '''
    stem = "{n1}{n1_josa} {n2} 한 통으로 $$수식$$10$$/수식$$개의 컵에 똑같이 나누어 담아서 그중 $$수식$${a}$$/수식$$컵을 마셨습니다. {n1}{n1_josa} 마신 {n2}{n2_josa} {n2} 한 통의 얼마인지 소수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "한 개의 컵에 담긴 {n2}{n2_josa} {n2} 한 통을 똑같이 $$수식$$10$$/수식$$으로 나눈 것 중의 $$수식$$1$$/수식$$이므로 $$수식$$0.1$$/수식$$입니다.\n" \
              "따라서 $$수식$$0.1$$/수식$$이 $$수식$${a}$$/수식$$개이면 $$수식$${cor_text}$$/수식$$입니다.\n\n"


    r1 = 2
    r2 = 9


    flag = True

    while flag:
        # 사람 이름 정하기
        n1 = random.choice(person_yeo + person_nam)
        if han_josa(n1[-1]) == ' ':
            n1_josa = '가'
        else:
            n1_josa = '이가'

        # 음료 이름 정하기
        n2 = random.choice(['우유', '주스', '물'])
        if han_josa(n2[-1]) == ' ':
            n2_josa = '는'
        else:
            n2_josa = '은'

        # a값 정하기
        a = random.randint(r1, r2)

        # 답
        cor_text = decimal.Decimal('0.1') * a

        if 0.1 < cor_text < 1.0:
            flag = False


    stem = stem.format(n1=n1, n1_josa=n1_josa, n2=n2, n2_josa=n2_josa, a=a)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(n2=n2, n2_josa=n2_josa, a=a, cor_text=cor_text)

    return stem, answer, comment




















# 3-1-6-52
def fraanddec316_Stem_023():
    '''
    :param r1: 소수 첫째자리 수의 최솟값 [int] {2:3}
    :param r2: 소수 첫째자리 수의 최댓값 [int] {8:9}
    :param r3: 소금과 설탕 판매 가격 / 10의 최솟값 [int] {1:2}
    :param r4: 소금과 설탕 판매 가격 / 10의 최댓값 [int] {8:9}
    '''
    stem = "{n1}{n1_josa1} $$수식$${A} ` rm kg$$/수식$$을 $$수식$${s1}$$/수식$$원에 파는 설탕을 $$수식$${B} ` rm kg$$/수식$$ 샀습니다. {n2}{n2_josa1} $$수식$${C} ` rm kg$$/수식$$을 $$수식$${s2}$$/수식$$원에 파는 소금을 $$수식$${D} ` rm kg$$/수식$$ 샀습니다. {n1}{n1_josa2} {n2}{n2_josa2} 쓴 돈은 모두 얼마인가요?\n"
    answer = "(정답)\n$$수식$${x5}$$/수식$$원\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$${A_josa} $$수식$$0.1$$/수식$$이 $$수식$${a}$$/수식$$개인 수이고, $$수식$${B}$$/수식$${B_josa} $$수식$$0.1$$/수식$$이 $$수식$${b}$$/수식$$개인 수이므로 " \
              "설탕 $$수식$${B} ` rm kg$$/수식$$ 산 것은 $$수식$${A} ` rm kg$$/수식$$씩 $$수식$${b} ` DIV ` {a} ` = ` {x1} ` LEFT ($$/수식$$번$$수식$$RIGHT )$$/수식$$ 산 것과 같습니다.\n" \
              "{n1}{n1_josa3} 쓴 돈은 $$수식$${s1} ` TIMES ` {x1} ` = ` {x2} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$입니다.\n" \
              "$$수식$${C}$$/수식$${C_josa} $$수식$$0.1$$/수식$$이 $$수식$${c}$$/수식$$개인 수이고, $$수식$${D}$$/수식$${D_josa} $$수식$$0.1$$/수식$$이 $$수식$${d}$$/수식$$개인 수이므로 " \
              "소금 $$수식$${D} ` rm kg$$/수식$$ 산 것은 $$수식$${C} ` rm kg$$/수식$$씩 $$수식$${d} ` DIV ` {c} ` = ` {x3} ` LEFT ($$/수식$$번$$수식$$RIGHT )$$/수식$$ 산 것과 같습니다.\n" \
              "{n2}{n2_josa2} 쓴 돈은 $$수식$${s2} ` TIMES ` {x3} ` = ` {x4} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$입니다.\n" \
              "따라서 {n1}{n1_josa2} {n2}{n2_josa2} 쓴 돈은\n" \
              "$$수식$${x2} ` + ` {x4} ` = ` {x5} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$입니다.\n\n"



    r1 = 2
    r2 = 9
    r3 = 1
    r4 = 9


    flag = True

    while flag:
        n1 = random.choice(person_nam)
        if han_josa(n1[-1]) == ' ':
            n1_josa1 = '는'
            n1_josa2 = '와'
            n1_josa3 = '가'
        else:
            n1_josa1 = '이는'
            n1_josa2 = '이와'
            n1_josa3 = '이가'

        n2 = random.choice(person_yeo)
        if han_josa(n2[-1]) == ' ':
            n2_josa1 = '는'
            n2_josa2 = '가'
        else:
            n2_josa1 = '이는'
            n2_josa2 = '이가'

        # n = random.randint(2, 4)
        # a = random.randint(r1, r2)
        # b = n * a
        # c = random.randint(r1, r2)
        # d = n * c

        while True:
            random_n1 = np.random.randint(2, 5)
            random_n2 = np.random.randint(2, 5)

            a = np.random.randint(r1, r2)
            b = random_n1 * a

            c = np.random.randint(r1, r2)
            d = random_n2 * c

            if random_n1 != random_n2 and a != c:
                break


        e = random.randint(r3, r4)
        f = random.randint(r3, r4)

        if a != c and b < 10 and d < 10 and e != f:
            A = decimal.Decimal('0.1') * a
            B = decimal.Decimal('0.1') * b
            C = decimal.Decimal('0.1') * c
            D = decimal.Decimal('0.1') * d

            A_josa = num_josa(a)[1]
            B_josa = num_josa(b)[1]
            C_josa = num_josa(c)[1]
            D_josa = num_josa(d)[1]

            s1 = e * 10
            s2 = f * 10

            x1 = b // a
            x2 = s1 * x1
            x3 = d // c
            x4 = s2 * x3

            x5 = x2 + x4

            flag = False


    stem = stem.format(n1=n1, n1_josa1=n1_josa1, n1_josa2=n1_josa2, n2=n2, n2_josa1=n2_josa1, n2_josa2=n2_josa2,
                       s1=s1, s2=s2, A=A, B=B, C=C, D=D)
    answer = answer.format(x5=x5)
    comment = comment.format(A=A, A_josa=A_josa, a=a, s1=s1, B=B, B_josa=B_josa, b=b, s2=s2, C=C, C_josa=C_josa, c=c, D=D, D_josa=D_josa, d=d,
                             x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, n1=n1, n1_josa2=n1_josa2, n1_josa3=n1_josa3, n2=n2, n2_josa2=n2_josa2)

    return stem, answer, comment




















# 3-1-6-55
def fraanddec316_Stem_024():
    stem = "나타내는 수가 다른 하나를 찾아 소수로 나타내어 보세요.\n$$표$${show1},  {show2},  {show3}$$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "{U}{U_josa} $$수식$${S1}$$/수식$${S1_josa} 나타냅니다.\n" \
              "$$수식$$0.1$$/수식$$이 $$수식$${A}$$/수식$$개인 수인 수는 $$수식$${S2}$$/수식$$입니다.\n" \
              "{X}{X_josa} $$수식$${S3}$$/수식$${S3_josa} 나타냅니다.\n" \
              "따라서 나타내는 수가 다른 하나는 {T}이고 소수로 나타내면 $$수식$${S}$$/수식$$입니다.\n\n"


    flag = True
    while flag:
        U_X_list = ['일', '이', '삼', '사', '오', '육', '칠', '팔', '구']

        U1 = random.choice(U_X_list)
        U2 = random.choice(U_X_list)
        U = "%s 점 %s" % (U1, U2)
        if han_josa(U2[-1]) == ' ':
            U_josa = '는'
        else:
            U_josa = '은'

        s_dict = {'일':1, '이':2, '삼':3, '사':4, '오':5, '육':6, '칠':7, '팔':8, '구':9}
        s1 = s_dict[U1]
        s2 = s_dict[U2]
        S1 = s1 + decimal.Decimal('0.1') * (s2)
        S1_josa = num_josa(s2)[4]

        a = random.randint(2, 9)
        b = random.randint(2, 9)
        A = (a * 10) + b
        S2 = decimal.Decimal('0.1') * A

        x_dict = dict((v,k) for k,v in s_dict.items())
        X1 = x_dict[a]
        X2 = x_dict[b]
        X = "%s 점 %s" % (X1, X2)
        if han_josa(X2[-1]) == ' ':
            X_josa = '는'
        else:
            X_josa = '은'

        s3 = s_dict[X1]
        s4 = s_dict[X2]
        S3 = s3 + decimal.Decimal('0.1') * (s4)
        S3_josa = num_josa(b)[4]

        T = U
        S = S1

        flag = False

    selec1 = U
    selec2 = "$$수식$$0.1$$/수식$$이 $$수식$$%d$$/수식$$개인 수" % A
    selec3 = X

    candidates = [selec1, selec2, selec3]
    np.random.shuffle(candidates)
    [show1, show2, show3] = candidates

    stem = stem.format(show1=show1, show2=show2, show3=show3)
    answer = answer.format(S=S)
    comment = comment.format(U=U, U_josa=U_josa, S1=S1, S1_josa=S1_josa, A=A, S2=S2, X=X, X_josa=X_josa, S3=S3, S3_josa=S3_josa, T=T, S=S)


    return stem, answer, comment




















# 3-1-6-57
def fraanddec316_Stem_025():
    stem = "소수를 읽어 보세요.\n$$수식$$LEFT ( 1 RIGHT ) ```` {s1}$$/수식$$ → $$수식$${box_1}$$/수식$$\n$$수식$$LEFT ( 2 RIGHT ) ```` {s2}$$/수식$$ → $$수식$${box_2}$$/수식$$\n"
    answer = "(정답)\n{U}, {X}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1 RIGHT ) ```` {S1}$$/수식$${S1_josa} {U}{U_josa} 읽습니다.\n" \
              "$$수식$$LEFT ( 2 RIGHT ) ```` {S2}$$/수식$${S2_josa} {X}{X_josa} 읽습니다.\n\n"


    flag = True
    while flag:
        num_list = list(range(1, 10))
        a, c = random.sample(num_list, 2)
        b, d = random.sample(num_list, 2)

        S1 = a + decimal.Decimal('0.1') * b
        S2 = c + decimal.Decimal('0.1') * d
        S1_josa = num_josa(b)[1]
        S2_josa = num_josa(d)[1]

        num2han = {1:'일', 2:'이', 3:'삼', 4:'사', 5:'오', 6:'육', 7:'칠', 8:'팔', 9:'구'}

        U1 = num2han[a]
        U2 = num2han[b]
        U = "%s 점 %s" % (U1, U2)
        if han_josa(U2[-1]) == ' ':
            U_josa = '라고'
        else:
            U_josa = '이라고'

        X1 = num2han[c]
        X2 = num2han[d]
        X = "%s 점 %s" % (X1, X2)
        if han_josa(X2[-1]) == ' ':
            X_josa = '라고'
        else:
            X_josa = '이라고'

        flag = False

    s1 = "%s" % (S1)
    s2 = "%s" % (S2)
    box_1 = "box{　　　}"
    box_2 = "box{　　　}"

    stem = stem.format(s1=s1, box_1=box_1, s2=s2, box_2=box_2)
    answer = answer.format(U=U, X=X)
    comment = comment.format(S1=S1, S1_josa=S1_josa, U=U, U_josa=U_josa, S2=S2, S2_josa=S2_josa, X=X, X_josa=X_josa)

    return stem, answer, comment




















# 3-1-6-58
def fraanddec316_Stem_026():
    stem = "$$수식$${box}$$/수식$$ 안에 알맞은 소수를 써넣으세요.\n$$수식$$LEFT ( 1 RIGHT ) ```` {A} ` rm {{cm}} ~ {B} ` rm {{mm}} ` = `$$/수식$$ $$수식$${box_1}$$/수식$$ $$수식$$` rm {{cm}}$$/수식$$\n$$수식$$LEFT ( 2 RIGHT ) ```` {C} ` rm {{mm}} ` = `$$/수식$$ $$수식$${box_2}$$/수식$$ $$수식$$` rm {{cm}}$$/수식$$\n"
    answer = "(정답)\n$$수식$${S1}$$/수식$$, $$수식$${S2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1 RIGHT ) ```` {A} ` rm {{cm}} ~ {B} ` rm {{mm}} ` = ` {S1} ` rm {{cm}}$$/수식$$\n" \
              "$$수식$$LEFT ( 2 RIGHT ) ```` {C} ` rm {{mm}} ` = ` {U1} ` rm {{cm}} ~ {U2} ` rm {{mm}} ` = ` {S2} ` rm {{cm}}$$/수식$$\n\n"


    box = '□'
    flag = True
    while True:
        A = random.randint(2, 9)
        B = random.randint(2, 9)

        S1 = (A * 10) + B
        S1 = decimal.Decimal('0.1') * S1

        a = random.randint(2, 9)
        b = random.randint(2, 9)
        C = (a * 10) + b

        U1 = a
        U2 = b

        S2 = decimal.Decimal('0.1') * C

        if ((A * 10) + B) != ((a * 10) + b):
            break

    box_1 = "box{　　　}"
    box_2 = "box{　　　}"

    stem = stem.format(box=box, A=A, B=B, C=C, box_1=box_1, box_2=box_2)
    answer = answer.format(S1=S1, S2=S2)
    comment = comment.format(A=A, B=B, C=C, S1=S1, S2=S2, U1=U1, U2=U2)

    return stem, answer, comment

















# 3-1-6-59
def fraanddec316_Stem_027():
    stem = "$$수식$${box}$$/수식$$ 안에 알맞은 수를 써넣으세요.\n$$수식$$LEFT ( 1 RIGHT ) ```` {A}$$/수식$${A_josa} $$수식$$0.1$$/수식$$이 $$수식$${box_1}$$/수식$$개입니다.\n$$수식$$LEFT ( 2 RIGHT ) ```` 0.1$$/수식$$이 $$수식$${box_2}$$/수식$$개이면 $$수식$${B}$$/수식$$입니다.\n"
    answer = "(정답)\n$$수식$${S1}$$/수식$$, $$수식$${S2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1 RIGHT ) ```` {A}$$/수식$${A_josa} $$수식$$0.1$$/수식$$이 $$수식$${S1}$$/수식$$개입니다.$$/수식$$\n" \
              "$$수식$$LEFT ( 2 RIGHT ) ```` 0.1$$/수식$$이 $$수식$${S2}$$/수식$$개이면 $$수식$${B}$$/수식$$입니다.$$/수식$$\n\n"


    box = '□'
    box_1 = "box{　　　}"
    box_2 = "box{　　　}"

    flag = True
    while flag:
        a = random.randint(2, 99)
        b = random.randint(2, 99)

        if a != b:
            A = decimal.Decimal('0.1') * a
            B = decimal.Decimal('0.1') * b
            A_josa = num_josa(a)[1]

            S1 = a
            S2 = b

            flag = False

    stem = stem.format(box=box, A=A, A_josa=A_josa, box_1=box_1, box_2=box_2, B=B)
    answer = answer.format(S1=S1, S2=S2)
    comment = comment.format(A=A, A_josa=A_josa, S1=S1, S2=S2, B=B)

    return stem, answer, comment



















# 3-1-6-61
def fraanddec316_Stem_028():
    '''
    :param r1: A의 최솟값 [int] {2:3}
    :param r2: A의 최댓값 [int] {8:9}
    :param r1: S1의 소수 첫째 자리수의 최솟값 [int] {2:3}
    :param r2: S1의 소수 첫째 자리수의 최댓값 [int] {8:9}
    '''
    stem = "소수로 쓰고, 읽어 보세요.\n$$표$$$$수식$${A}$$/수식$${A_josa} $$수식$${S1}$$/수식$$만큼$$/표$$\n쓰기: $$수식$${box_1}$$/수식$$     읽기: $$수식$${box_2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${S2}$$/수식$$, {X}\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$${A_josa} $$수식$${S1}$$/수식$$만큼을 소수로 쓰면 $$수식$${S2}$$/수식$$입니다.\n"\
              "$$수식$${S2}$$/수식$${S2_josa} {X}{X_josa} 읽습니다.\n\n"



    r1 = 2
    r2 = 9
    r3 = 2
    r4 = 9


    box_1 = "box{　　　}"
    box_2 = "box{　　　}"

    flag = True
    while flag:
        A = random.randint(r1, r2)
        b = random.randint(r3, r4)
        S1 = decimal.Decimal('0.1') * b
        S2 = A + S1

        A_josa = num_josa(A)[0]
        S2_josa = num_josa(b)[1]

        num2han = {1:'일', 2:'이', 3:'삼', 4:'사', 5:'오', 6:'육', 7:'칠', 8:'팔', 9:'구'}
        X1 = num2han[A]
        X2 = num2han[b]
        X = "%s 점 %s" % (X1, X2)

        # if han_josa(X2[-1]) == ' ':
        #     X_josa = '로'
        # else:
        #     X_josa = '으로'

        if X2 == "삼" or X2 == "육":
            X_josa = "으로"
        else:
            X_josa = "로"

        flag = False

    stem = stem.format(A=A, A_josa=A_josa, S1=S1, box_1=box_1, box_2=box_2)
    answer = answer.format(S2=S2, X=X)
    comment = comment.format(A=A, A_josa=A_josa, S1=S1, S2=S2, S2_josa=S2_josa, X=X, X_josa=X_josa)

    return stem, answer, comment







# 3-1-6-63
def fraanddec316_Stem_029() :
    stem = "{t1}{j1}가 산 {t2}의 길이는 $$수식$${s1} ` rm {{mm}}$$/수식$$입니다. {t1}{j1}가 산 {t2}의 길이는 몇 $$수식$$rm {{cm}}$$/수식$$인지 소수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${cor_text} ` rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${c1}$$/수식$$\n\n"


    t1 = np.random.choice(person_nam+person_yeo, 1)[0]
    t2 = np.random.choice(['막대', '리본', '철사'], 1)[0]
    j1 = '' if han_josa(t1[-1]) == ' ' else '이'

    n1 = np.random.randint(1, 10, 1)[0]
    n2 = np.random.randint(1, 10, 1)[0]
    n3 = np.random.randint(1, 10, 1)[0]
    s1 = n1 * 100 + n2 * 10 + n3

    cor_text = '%d%d.%d' % (n1, n2, n3)
    c1 = '%d ` rm {{mm}} ` = ` %d%d ` rm {{cm}} ~ %d ` rm {{mm}} ` = ` %s ` rm {{cm}}' % (s1, n1, n2, n3, cor_text)

    stem = stem.format(t1=t1, t2=t2, j1=j1, s1=s1)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1)

    return stem, answer, comment


















# 3-1-6-64
def fraanddec316_Stem_030() :
    stem = "{t1}{j1}가 그은 선분의 길이는 $$수식$${s1} ` rm {{cm}}$$/수식$$보다 $$수식$${s2} ` rm {{mm}}$$/수식$$ 더 깁니다. {t1}{j1}가 그은 선분의 길이는 몇 $$수식$$rm {{cm}}$$/수식$$인지 소수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${cor_text} ` rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${s2} ` rm {{mm}} ` = ` {s3} ` rm {{cm}}$$/수식$$입니다.\n" \
              "따라서 {t1}{j1}가 그은 선분의 길이는 $$수식$${s1} ` rm {{cm}}$$/수식$$와 $$수식$${s3} ` rm {{cm}}$$/수식$$만큼이므로 $$수식$${cor_text} ` rm {{cm}}$$/수식$$입니다.\n\n"


    t1 = np.random.choice(person_nam+person_yeo, 1)[0]
    j1 = '' if han_josa(t1[-1]) == ' ' else '이'

    s1 = np.random.randint(11, 100, 1)[0]
    s2 = np.random.randint(1, 10, 1)[0]
    s3 = '0.%d' % (s2)
    cor_text = '%d.%d' % (s1, s2)

    stem = stem.format(s1=s1, s2=s2, t1=t1, j1=j1)
    answer = answer.format(cor_text=cor_text)
    comment= comment.format(s1=s1, s2=s2, s3=s3, cor_text=cor_text, t1=t1, j1=j1)

    return stem, answer, comment



















# 3-1-6-66
def fraanddec316_Stem_031():
    stem = "두 수의 크기를 비교하여 $$수식$${boxblank}$$/수식$$ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$표$$ $$수식$${problem1}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${answer_sign}$$/수식$$\n"
    comment = "(해설)\n" \
              "자연수의 크기를 비교하면 $$수식$${explain1}$$/수식$$이므로 $$수식$${explain2}$$/수식$$입니다.\n\n"


    boxblank = "□"

    while True:
        num1, num3 = random.sample(range(2, 10), 2)
        num2, num4 = random.sample(range(2, 10), 2)

        problem1 = '{0}.{1} ```` □ ```` {2}.{3} '.format(num1, num2, num3, num4)

        if num1 < num3:
            explain1 = '{0} ` &lt; ` {1}'.format(num1, num3)
            explain2 = '{0}.{1} ` &lt; ` {2}.{3}'.format(num1, num2, num3, num4)
            answer_sign = '&lt;'
            break

        elif num1 > num3:
            explain1 = '{0} ` &gt; ` {1}'.format(num1, num3)
            explain2 = '{0}.{1} ` &gt; ` {2}.{3}'.format(num1, num2, num3, num4)
            answer_sign = '&gt;'
            break


    stem = stem.format(problem1=problem1, boxblank=boxblank)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2)

    return stem, answer, comment




















# 3-1-6-67
def fraanddec316_Stem_032():
    stem = "길이가 더 짧은 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$      ㉡ $$수식$${problem2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{answer_sign}\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$\n" \
              "따라서 $$수식$${explain2}$$/수식$$이므로 더 짧은 것의 기호는 {explain3}입니다.\n\n"


    num1 = random.randint(2, 9)
    num2, num3 = random.sample(range(2, 10), 2)

    equ1 = '{0} ` rm {{cm}} ~ {1} ` rm {{mm}}'.format(num1, num3)
    equ2 = '{0}.{1} ` rm {{cm}}'.format(num1, num2)
    explain1 = '{0} ` rm {{cm}} ~ {1} ` rm {{mm}} `=` {0} ` rm {{cm}} ` + ` 0.{1} ` rm {{cm}} ` = ` {0}.{1} ` rm {{cm}}'.format(num1, num3)

    lst = [[equ1, num3], [equ2, num2]]
    random.shuffle(lst)

    equ1, equ2 = lst[0][0], lst[1][0]
    num3, num2 = lst[0][1], lst[1][1]

    if num3 > num2:
        explain2 = '{0}.{1} ` rm {{cm}} ` &gt; {0}.{2} ` rm {{cm}} `'.format(num1, num3, num2)
        answer_sign = '㉡'
    else:
        explain2 = '{0}.{1} ` rm {{cm}} ` &lt; {0}.{2} ` rm {{cm}} `'.format(num1, num3, num2)
        answer_sign = '㉠'


    explain3 = answer_sign

    stem = stem.format(problem1=equ1, problem2=equ2)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3)

    return stem, answer, comment



























# 3-1-6-68
def fraanddec316_Stem_033():
    stem = "더 {choice} 수를 찾아 소수로 써 보세요.\n$$표$$$$수식$$0.1$$/수식$$이 $$수식$${problem1}$$/수식$$개인 수, $$수식$$0.1$$/수식$$이 $$수식$${problem2}$$/수식$$개인 수$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$0.1$$/수식$$이 $$수식$${explain1}$$/수식$$개인 수는 $$수식$${explain2}$$/수식$$이고, " \
              "$$수식$$0.1$$/수식$$이 $$수식$${explain3}$$/수식$$개인 수는 $$수식$${explain4}$$/수식$$입니다.\n" \
              "따라서 $$수식$${explain5}$$/수식$$입니다.\n\n"


    while 1:
        num1, num2 = random.sample(range(11, 100), 2)
        if abs(num1 - num2) < 10:
            if num1 % 10 != 0 and num2 % 10 != 0:
                break

    problem1, problem2 = num1, num2
    explain1, explain2 = num1, num1 / 10
    explain3, explain4 = num2, num2 / 10

    if num1 > num2:
        explain5 = '{0} ` &gt; ` {1}'.format(num1 / 10, num2 / 10)
        # answer_num = num1 / 10
    else:
        explain5 = '{0} ` &lt; ` {1}'.format(num1 / 10, num2 / 10)
        # answer_num = num2 / 10

    choice = ["큰", "작은"][np.random.randint(0, 2)]

    if choice == "큰":
        answer_num = max(num1 / 10, num2 / 10)
    else:
        answer_num = min(num1 / 10, num2 / 10)

    stem = stem.format(problem1=problem1, problem2=problem2, choice=choice)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             explain5=explain5)

    return stem, answer, comment





























# 3-1-6-69
def fraanddec316_Stem_034():
    stem = "다음 중 가장 큰 수를 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$      ㉡ $$수식$${problem2}$$/수식$$      ㉢ $$수식$${problem3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_sign}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$${post1} $$수식$$0.1$$/수식$$이 $$수식$${explain2}$$/수식$$개, " \
              "$$수식$${explain3}$$/수식$${post2} $$수식$$0.1$$/수식$$이 $$수식$${explain4}$$/수식$$개, " \
              "$$수식$${explain5}$$/수식$${post3} $$수식$$0.1$$/수식$$이 $$수식$${explain6}$$/수식$$개입니다. " \
              "따라서 $$수식$${explain7}$$/수식$$이므로 $$수식$${explain8}$$/수식$$입니다.\n\n"


    while 1:
        num1, num2, num3 = random.sample(range(11, 100), 3)
        if abs(num1 - num2) < 10 and abs(num1 - num3) < 10:
            if num1 % 10 != 0 and num2 % 10 != 0 and num3 % 10 != 0:
                break

    tmp = [num1, num2, num3]
    random.shuffle(tmp)
    num1, num2, num3 = tmp
    num4, num5, num6 = num1 / 10, num2 / 10, num3 / 10

    problem1, problem2, problem3 = num4, num5, num6
    explain1, explain3, explain5 = problem1, problem2, problem3

    post1, post2, post3 = postposition(int(str(num1)[-1]), flag=3), postposition(int(str(num2)[-1]), flag=3), \
                          postposition(int(str(num3)[-1]), flag=3)

    explain2, explain4, explain6 = num1, num2, num3

    lst = [['㉠', num1, num4], ['㉡', num2, num5], ['㉢', num3, num6]]
    lst.sort(key=lambda x: x[1], reverse=True)

    explain7 = '{0} ` &gt; ` {1} ` &gt; ` {2}'.format(lst[0][1], lst[1][1], lst[2][1])
    explain8 = '{0} ` &gt; ` {1} ` &gt; ` {2}'.format(lst[0][2], lst[1][2], lst[2][2])
    answer_sign = lst[0][0]

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3)
    answer = answer.format(answer_sign=answer_sign)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             explain5=explain5, explain6=explain6, explain7=explain7, explain8=explain8,
                             post1=post1, post2=post2, post3=post3)

    return stem, answer, comment




















# 3-1-6-70
def fraanddec316_Stem_035():
    stem = "$$수식$${problem1}$$/수식$${post} $$수식$${problem2} over 10$$/수식$$의 크기를 비교하여 더 큰 수를 써 보세요.\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$입니다.\n\n"


    num1, num2 = random.sample(range(2, 10), 2)

    problem1 = num1 / 10
    post = postposition(num1, flag=2)

    problem2 = num2
    explain1 = '{0} over 10 ` = ` {1}'.format(num2, num2 / 10)

    if num1 > num2:
        answer_num = num1 / 10
    else:
        answer_num = '{0} over 10'.format(num2)

    stem = stem.format(problem1=problem1, problem2=problem2, post=post)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1)

    return stem, answer, comment




























# 3-1-6-71
def fraanddec316_Stem_036():
    stem = "{people}{post1} 가지고 있는 {obj1}의 길이는 $$수식$${problem1} ` rm {{mm}}$$/수식$$, {obj2}의 길이는 $$수식$${problem2} ` rm {{cm}}$$/수식$$입니다. {obj1}{post} {obj2} 중 길이가 더 긴 것은 어느 것인가요?\n"
    answer = "(정답)\n{answer_obj}\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$입니다.\n" \
              "따라서 $$수식$${explain2}$$/수식$$이므로 길이가 더 긴 것은 {answer_obj}입니다.\n\n"


    num1 = random.randint(91, 99)
    num2 = random.randint(1, 9)

    people = random.choice(['영석', '준영', '소진', '현석', '우성'])
    obj1 = random.choice(['연필', '철사', '크레파스'])
    obj2 = random.choice(['볼펜', '자', '색연필'])

    post = '와' if josa_check(obj1[-1]) == ' ' else '과'
    post1 = '가' if josa_check(people[-1]) == ' ' else '이가'

    problem1 = num1
    problem2 = '10.{0}'.format(num2)

    explain1 = '{0} ` rm {{mm}} ` = ` {1} ` rm {{cm}}'.format(num1, num1 / 10)
    explain2 = '{0} ` rm {{cm}} ` &lt; ` 10.{1} ` rm {{cm}}'.format(num1 / 10, num2)

    answer_obj = obj2

    stem = stem.format(problem1=problem1, problem2=problem2, post=post, obj1=obj1, obj2=obj2, people=people, post1=post1)
    answer = answer.format(answer_obj=answer_obj)
    comment = comment.format(explain1=explain1, explain2=explain2, answer_obj=answer_obj)

    return stem, answer, comment





























# 3-1-6-72
def fraanddec316_Stem_037():
    stem = "학교에서 {people1}{post1}네 집까지의 거리는 $$수식$${problem1} ` rm {{km}}$$/수식$$, {people2}{post2}네 집까지의 거리는 $$수식$${problem2} ` rm {{km}}$$/수식$$, {people3}{post3}네 집까지의 거리는  $$수식$${problem3} ` rm {{km}}$$/수식$$입니다. 세 사람 중 학교에서 가장 먼 곳에 사는 사람은 누구인가요?\n"
    answer = "(정답)\n{answer_peo}\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$, $$수식$${explain2}$$/수식$$, $$수식$${explain3}$$/수식$$의 소수점 위에 크기를 " \
              "비교하면 $$수식$${explain4}$$/수식$${post4} 가장 작고 $$수식$${explain1}$$/수식$$과 $$수식$${explain2}$$/수식$$는 같습니다.\n" \
              "$$수식$${explain5}$$/수식$${post5} $$수식$${explain6}$$/수식$${post6} 비교하면 " \
              "$$수식$${explain7}$$/수식$$입니다.\n" \
              "따라서 $$수식$${explain8}$$/수식$$이므로 학교에서 {answer_peo}{post7}네 집이 가장 멉니다.\n\n"


    people1 = random.choice(['정훈', '우진', '희정', '석훈', '우성'])
    people2 = random.choice(['현지', '소유', '정희', '희호', '선우'])
    people3 = random.choice(['영주', '강호', '선호', '진주', '경희'])

    num1, num2, num3 = random.sample(range(2, 10), 3)
    num1, num2, num3 = num1 / 10, 1 + num2 / 10, 1 + num3 / 10
    tmp_lst = [[people1, num1], [people2, num2], [people3, num3]]
    random.shuffle(tmp_lst)

    people1, people2, people3 = tmp_lst[0][0], tmp_lst[1][0], tmp_lst[2][0]
    num1, num2, num3 = tmp_lst[0][1], tmp_lst[1][1], tmp_lst[2][1]

    post1 = '' if josa_check(people1[-1]) == ' ' else '이'
    post2 = '' if josa_check(people2[-1]) == ' ' else '이'
    post3 = '' if josa_check(people3[-1]) == ' ' else '이'

    problem1, problem2, problem3 = num1, num2, num3
    explain1, explain2, explain3 = num1, num2, num3

    tmp_lst.sort(key=lambda x: x[1])
    explain4 = tmp_lst[0][1]

    tmp = []
    for i in [num1, num2, num3]:
        if i != explain4:
            tmp.append(i)

    post4 = postposition(int(str(explain4)[-1]), flag=0)
    explain5 = tmp[0]
    post5 = postposition(int(str(explain5)[-1]), flag=2)
    explain6 = tmp[1]
    post6 = postposition(int(str(explain6)[-1]), flag=1)

    if explain5 > explain6:
        explain7 = '{0} ` &gt; ` {1}'.format(explain5, explain6)
    else:
        explain7 = '{0} ` &lt; ` {1}'.format(explain5, explain6)

    explain8 = '{0} ` &gt; ` {1} ` &gt; ` {2}'.format(tmp_lst[2][1], tmp_lst[1][1], tmp_lst[0][1])

    answer_peo = tmp_lst[2][0]
    post7 = '' if josa_check(answer_peo[-1]) == ' ' else '이'

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3,
                       post1=post1, post2=post2, post3=post3,
                       people1=people1, people2=people2, people3=people3)
    answer = answer.format(answer_peo=answer_peo)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             explain5=explain5, explain6=explain6, explain7=explain7, explain8=explain8,
                             post4=post4, post5=post5, post6=post6, post7=post7, answer_peo=answer_peo)

    return stem, answer, comment





































# 3-1-6-73
def fraanddec316_Stem_038():
    stem = "{people1}{post1}는 {obj}의 $$수식$${problem1}$$/수식$${post2} 먹었고, {people2}{post3}는 {people1}{post4}가 처음 가지고 있던 것과 크기가 같은 {obj}의 $$수식$${problem2}$$/수식$${post5} 먹었습니다. 누가 {obj}{post} 더 많이 먹었나요?\n"
    answer = "(정답)\n{answer_peo}\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$이므로 $$수식$${explain2}$$/수식$$입니다.\n" \
              "따라서 {obj}{post5} 더 많이 먹은 사람은 {answer_peo}{post6}입니다.\n\n"


    people1 = random.choice(['정진', '우영', '희정', '훈석', '성우'])
    people2 = random.choice(['영주', '소유', '선호', '경희', '선우'])
    obj = random.choice(['사과파이', '피자', '호두파이', '케이크'])

    while 1:
        num1, num2 = random.sample(range(2, 10), 2)
        if num1 + num2 < 10:
            break

    post1 = '' if josa_check(people1[-1]) == ' ' else '이'
    post2 = postposition(num1, flag=1)
    post3 = '' if josa_check(people2[-1]) == ' ' else '이'
    post4 = '' if josa_check(people1[-1]) == ' ' else '이'
    post5 = postposition(num2, flag=1)
    post = '를' if josa_check(obj[-1]) == ' ' else '을'

    if random.randint(0, 1) == 0:
        problem1 = '{0} over 10'.format(num1)
        problem2 = num2 / 10
        explain1 = '{0} ` = ` {1}'.format(problem1, num1 / 10)
    else:
        problem2 = '{0} over 10'.format(num2)
        problem1 = num1 / 10
        explain1 = '{0} ` = ` {1}'.format(problem2, num2 / 10)

    if num1 > num2:
        explain2 = '{0} ` &gt; ` {1}'.format(num1 / 10, num2 / 10)
        answer_peo = people1
    else:
        explain2 = '{0} ` &lt; ` {1}'.format(num1 / 10, num2 / 10)
        answer_peo = people2

    post6 = '' if josa_check(answer_peo[-1]) == ' ' else '이'

    stem = stem.format(problem1=problem1, problem2=problem2, obj=obj,
                       post1=post1, post2=post2, post3=post3, post4=post4, post5=post5,
                       people1=people1, people2=people2, post=post)
    answer = answer.format(answer_peo=answer_peo)
    comment = comment.format(explain1=explain1, explain2=explain2, post5=post, post6=post6,
                             obj=obj, answer_peo=answer_peo)

    return stem, answer, comment







































# 3-1-6-74
def fraanddec316_Stem_039():
    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 중에서 $$수식$${boxblank}$$/수식$$ 안에 들어갈 수 있는 수를 모두 구해 보세요.\n$$표$$$$수식$${problem1}.{boxblank} ` &gt; ` {problem1}.{problem2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${problem1}.{boxblank} ` &gt; ` {problem1}.{problem2}$$/수식$$에서 " \
              "$$수식$${boxblank} ` &gt; ` {explain1}$$/수식$$이므로 " \
              "$$수식$${boxblank}$$/수식$$ 안에 들어갈 수 있는 수는 {answer_num}입니다.\n\n"


    boxblank = "□"
    num1 = random.randint(1, 9)
    num2 = random.randint(6, 8)

    problem1 = num1
    problem2 = num2
    explain1 = num2

    lst = [str(i) for i in range(num2 + 1, 10)]
    answer_num = '$$수식$$'
    answer_num += '$$/수식$$, $$수식$$'.join(lst)
    answer_num += '$$/수식$$'

    stem = stem.format(problem1=problem1, problem2=problem2, boxblank=boxblank)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, answer_num=answer_num, problem1=problem1, problem2=problem2, boxblank=boxblank)

    return stem, answer, comment



























# 3-1-6-76
def fraanddec316_Stem_040() :
    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 자연수 중에서 $$수식$${box}$$/수식$$ 안에 공통으로 들어갈 수 있는 수는 모두 몇 개인가요?\n$$표$$$$수식$${a1}$$/수식$$,    $$수식$${a2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${a1}$$/수식$$에서 소수의 크기를 비교하면 $$수식$${c1}$$/수식$$이므로 $$수식$${box}$$/수식$$ 안에 들어갈 수 있는 수는 $$수식$${c2}$$/수식$$입니다.\n" \
              "$$수식$${a2}$$/수식$$에서 소수의 크기를 비교하면 $$수식$${c3}$$/수식$$이므로 $$수식$${box}$$/수식$$ 안에 들어갈 수 있는 수는 $$수식$${c4}$$/수식$$입니다.\n" \
              "따라서 $$수식$${box}$$/수식$$ 안에 공통으로 들어갈 수 있는 수는 $$수식$${c5}$$/수식$$이므로 $$수식$${cor_text}$$/수식$$개입니다.\n\n" \


    flag= True
    while flag :
        # a1
        s1 = np.random.randint(6, 10, 1)[0]
        nums1 = np.arange(1, s1)
        a1 = '0.%s ` %s ` 0.%d' % (box, right, s1)
        c1 = '%s ` %s ` %d' % (box, right, s1)
        c2 = '$$/수식$$, $$수식$$'.join(list(map(str, nums1))) if len(nums1) < 5 else '$$/수식$$, $$수식$$'.join(list(map(str, nums1[:3]))) + '$$/수식$$, $$수식$$CDOTS$$/수식$$, $$수식$$%d' % (nums1[-1])

        # a2
        s2 = np.random.randint(1, 10, 1)[0]
        s3 = np.random.randint(1, 5, 1)[0]

        nums2 = np.arange(s3 + 1, 10)
        a2 = '%d.%d ` %s ` %d.%s' % (s2, s3, right, s2, box)
        c3 = '%d ` %s %s' % (s3, right, box)
        c4 = '$$/수식$$, $$수식$$'.join(list(map(str, nums2))) if len(nums2) < 5 else '$$/수식$$, $$수식$$'.join(list(map(str, nums2[:3]))) + '$$/수식$$, $$수식$$CDOTS$$/수식$$, $$수식$$%d' % (nums2[-1])

        cor_nums = []
        for i in nums1 :
            if i in nums2 :
                cor_nums.append(i)

        cor_text = len(cor_nums)

        if cor_text > 0 :
            flag = False

    c5 = '$$/수식$$, $$수식$$'.join(list(map(str, cor_nums)))

    stem = stem.format(box=box, a1=a1, a2=a2)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(a1=a1, a2=a2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, cor_text=cor_text, box=box)

    return stem, answer, comment






















# if __name__ == '__main__':
#     FracAndDeci_Stem_001()
#     FracAndDeci_Stem_002()
#     FracAndDeci_Stem_003()
#     FracAndDeci_Stem_004()
#     FracAndDeci_Stem_005()
#     FracAndDeci_Stem_006()
#     FracAndDeci_Stem_007()
#     FracAndDeci_Stem_008()
#     FracAndDeci_Stem_009()
#     FracAndDeci_Stem_010()
#     FracAndDeci_Stem_011()
#     FracAndDeci_Stem_012()
#     FracAndDeci_Stem_013()
#     FracAndDeci_Stem_014()
#     FracAndDeci_Stem_015()
#     FracAndDeci_Stem_016()
#     FracAndDeci_Stem_017()
#     FracAndDeci_Stem_018()
#     FracAndDeci_Stem_019()
#     FracAndDeci_Stem_020()
#     FracAndDeci_Stem_021()
#     FracAndDeci_Stem_022()
#     FracAndDeci_Stem_023()
#     FracAndDeci_Stem_024()
#     FracAndDeci_Stem_025()
#     FracAndDeci_Stem_026()
#     FracAndDeci_Stem_027()
#     FracAndDeci_Stem_028()
#     FracAndDeci_Stem_029()
#     FracAndDeci_Stem_030()
#     FracAndDeci_Stem_031()
#     FracAndDeci_Stem_032()
#     FracAndDeci_Stem_033()
#     FracAndDeci_Stem_034()
#     FracAndDeci_Stem_035()
#     FracAndDeci_Stem_036()
#     FracAndDeci_Stem_037()
#     FracAndDeci_Stem_038()
#     FracAndDeci_Stem_039()
#     FracAndDeci_Stem_040()







