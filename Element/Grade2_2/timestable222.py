import random
import numpy as np
import codecs
import os



PATH = '/home/boin-service/Visang/Dictionary/'

person_nam = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XY.txt'), 'r', 'utf-8').readlines()]
person_yeo = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XX.txt'), 'r', 'utf-8').readlines()]


have_jongsung_num = [0, 1, 3, 6, 7, 8]


def josa_check(name):
    JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                     'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    char_code = ord(name) - 44032
    ch1 = int(char_code / 588)
    ch2 = int((char_code - (588 * ch1)) / 28)
    ch3 = int((char_code - (588 * ch1) - (28 * ch2)))

    return JONGSUNG_LIST[ch3]









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








# 2-2-2-03
def timestable222_Stem_001():
    stem = "생선 한 손은 $$수식$$2$$/수식$$마리입니다. {people}는 오늘 {fish1} $$수식$${problem1}$$/수식$$손과 {fish2} $$수식$${problem2}$$/수식$$손을 사왔습니다. {people}가 오늘 사온 {fish1}는 {fish2}보다 몇 마리 더 {problem3}?\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$마리\n"
    comment = "(해설)\n" \
              "생선 한 손은 $$수식$$2$$/수식$$마리이므로\n" \
              "{fish1} $$수식$${explain1}$$/수식$$손 → $$수식$${explain2}$$/수식$$, " \
              "{fish2} $$수식$${explain3}$$/수식$$손 → $$수식$${explain4}$$/수식$$\n" \
              "$$수식$${explain2}$$/수식$${j1} $$수식$${explain4}$$/수식$$보다 $$수식$$2$$/수식$$씩 " \
              "$$수식$${explain7}$$/수식$$만큼 더 {explain8}.\n" \
              "따라서 {people}가 오늘 사온 {fish1}는 {fish2}보다 $$수식$${answer_num}$$/수식$$마리 더 {explain9}.\n\n"


    num1, num2 = random.sample(range(2, 10), 2)
    people = random.choice(['어머니', '아버지', '할머니', '할아버지'])

    fish = np.random.choice(['꽁치', '고등어', '조기'], 2, False)
    random.shuffle(fish)
    fish1, fish2 = fish

    problem1, problem2 = num1, num2
    explain1, explain3 = num1, num2
    explain2 = '2 `TIMES` {0}'.format(num1)
    explain4 = '2 `TIMES` {0}'.format(num2)
    j1 = '은' if num1 in have_jongsung_num else '는'

    if num1 > num2:
        explain8 = '큽니다'
        explain7 = num1 - num2
        problem3 = '많을까요'
        explain9 = '많습니다'
    else:
        explain8 = '작습니다'
        explain7 = abs(num1 - num2)
        problem3 = '적을까요'
        explain9 = '적습니다'

    answer_num = explain7 * 2
    stem = stem.format(problem1=problem1, problem2=problem2, people=people, fish1=fish1, fish2=fish2, problem3=problem3)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             explain7=explain7, explain8=explain8,
                             fish1=fish1, fish2=fish2, people=people, answer_num=answer_num, explain9=explain9, j1=j1)

    return stem, answer, comment


















# 2-2-2-06
def timestable222_Stem_002():
    stem = "{sports}{j1} $$수식$${problem1}$$/수식$$명의 선수가 한 팀이 되어 경기를 합니다. $$수식$${problem2}$$/수식$$팀의 선수는 모두 몇 명인가요?\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$명\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$선수 수$$수식$$RIGHT ) ` = ` LEFT ($$/수식$$한 팀의 선수 수$$수식$$RIGHT ) ` TIMES ` LEFT ($$/수식$$팀 수$$수식$$RIGHT )$$/수식$$" \
              "$$수식$${explain1} ` LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 $$수식$${explain2}$$/수식$$팀의 선수는 모두 $$수식$${explain3}$$/수식$$명입니다.\n\n"

    sports, num1 = random.choice([['족구', 4], ['농구', 5], ['배구', 6], ['핸드볼', 7], ['야구', 9]])
    j1 = '는' if josa_check(sports[-1]) == ' ' else '은'
    num2 = random.randint(3, 9)
    answer_num = num1 * num2

    problem1, problem2 = num1, num2
    explain1 = '` = ` {0} ` TIMES ` {1} ` = ` {2}'.format(num1, num2, answer_num)
    explain2 = num2
    explain3 = answer_num

    stem = stem.format(problem1=problem1, problem2=problem2, sports=sports, j1=j1)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3)

    return stem, answer, comment

















# 2-2-2-11
def timestable222_Stem_003():
    stem = "{cookie}이 한 {t1}에 $$수식$${problem1}$$/수식$$개씩 들어 있습니다. $$수식$${problem2}$$/수식$$개의 {t1}에 들어 있는 {cookie}{j1} 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( ` {explain1}$$/수식$${t1}에 들어 있는 {cookie} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$한 {t1}에 들어 있는 {cookie} 수$$수식$$RIGHT ) ` TIMES ` LEFT ($$/수식$${t1} 수$$수식$$RIGHT )$$/수식$$"\
              "$$수식$${explain2} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 {cookie}은 모두 $$수식$${explain3}$$/수식$$개입니다.\n\n"

    t1 = random.choice(['상자', '봉지', '바구니'])
    cookie = random.choice(['초콜릿', '도넛', '사탕', '아이스크림', '캐러멜', '달걀'])

    j1 = '는' if josa_check(cookie[-1]) == ' ' else '은'
    num1 = random.randint(3, 9)
    num2 = random.randint(4, 9)
    answer_num = num1 * num2

    problem1, problem2 = num1, num2
    explain1 = num2
    explain2 = '` = ` {0} ` TIMES ` {1} ` = ` {2}'.format(num1, num2, answer_num)
    explain3 = answer_num

    stem = stem.format(problem1=problem1, problem2=problem2, cookie=cookie, j1=j1, t1=t1)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, cookie=cookie, t1=t1)

    return stem, answer, comment























# 2-2-2-15
def timestable222_Stem_004():
    stem = "{vehicle} 한 대에 $$수식$${problem1}$$/수식$$명이 탈 수 있습니다. {vehicle} $$수식$${problem2}$$/수식$$대에 탈 수 있는 사람은 모두 몇 명인가요?\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$명\n"
    comment = "(해설)\n" \
              "{vehicle} 한 대에 $$수식$${explain1}$$/수식$$명씩 $$수식$${explain2}$$/수식$$대에 탈 수 있으므로 " \
              "$$수식$${explain3} ` LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$입니다.\n\n"

    vehicle, num1 = random.choice([['자동차', random.randint(4, 8)],
                                   ['보트', random.randint(4, 9)],
                                   ['요트', random.randint(4, 9)],
                                   ['롤러코스터', random.choice([2, 4, 6, 8])],
                                   ['청룡열차', random.choice([2, 4, 6, 8])],
                                   ['$$수식$$2$$/수식$$인용 자전거', 2]])

    num2 = random.randint(3, 9)
    answer_num = num1 * num2

    problem1, problem2 = num1, num2
    explain1 = num1
    explain2 = num2
    explain3 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num1, num2, answer_num)

    stem = stem.format(problem1=problem1, problem2=problem2, vehicle=vehicle)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, vehicle=vehicle)

    return stem, answer, comment


















# 2-2-2-16
def timestable222_Stem_005():
    stem = "{objects}{ob_j1} {people1}{p1_j}는 $$수식$${problem1}$$/수식$${unit} 가지고 있고 {people2}{p2_j}는 {people1}{p1_j}의 $$수식$${problem2}$$/수식$$배만큼 가지고 있습니다. {people2}{p2_j}가 가지고 있는 {objects}{ob_j2} 몇 {unit}인가요?\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$${unit}\n"
    comment = "(해설)\n" \
              "{people2}{p2_j}가 가지고 있는 {objects}{ob_j2} $$수식$${explain1}$$/수식$${unit}의 $$수식$${explain2}$$/수식$$배이므로 " \
              "$$수식$${explain3} ` LEFT ($$/수식$${unit}$$수식$$RIGHT )$$/수식$$입니다.\n\n"

    object_dict = {'자루' : ['연필', '붓', '색연필', '싸인펜', '볼펜'],
                    '장' : ['색종이', '학종이', '포장지', '우편엽서', '메모지'],
                    '권' : ['공책', '동화책', '국어책', '문제집', '위인전']}

    unit = random.choice(list(object_dict.keys()))
    objects = random.choice(object_dict.get(unit))

    terms = [random.choice(person_nam), random.choice(person_yeo)]
    random.shuffle(terms)
    people1, people2 = terms

    ob_j1 = '를' if josa_check(objects[-1]) == ' ' else '을'
    ob_j2 = '는' if josa_check(objects[-1]) == ' ' else '은'
    p1_j = '' if josa_check(people1[-1]) == ' ' else '이'
    p2_j = '' if josa_check(people2[-1]) == ' ' else '이'

    num1 = random.randint(3, 9)
    num2 = random.randint(3, 9)
    answer_num = num1 * num2

    problem1, problem2 = num1, num2
    explain1, explain2 = num1, num2
    explain3 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num1, num2, answer_num)

    stem = stem.format(problem1=problem1, problem2=problem2, people1=people1, people2=people2, objects=objects, ob_j1=ob_j1, ob_j2=ob_j2, p1_j=p1_j, p2_j=p2_j, unit=unit)
    answer = answer.format(answer_num=answer_num, unit=unit)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, people2=people2, objects=objects, p2_j=p2_j, ob_j2=ob_j2, unit=unit)

    return stem, answer, comment


















# 2-2-2-19
def timestable222_Stem_006():
    stem = "한 {t1}에 {objects}{ob_j} $$수식$${problem1}$$/수식$$개씩 담겨 있습니다. {t1} $$수식$${problem2}$$/수식$$개에는 {objects}{ob_j} 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$개\n"
    comment = "(해설)\n" \
              "한 {t1}에 {objects}{ob_j} $$수식$${explain1}$$/수식$$개씩 담겨 있으므로 \n" \
              "$$수식$$LEFT ($$/수식$${t1} $$수식$${explain2}$$/수식$$개에 담겨 있는 {objects} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$한 {t1}에 들어 있는 " \
              "{objects} 수$$수식$$RIGHT ) ` TIMES ` LEFT ($$/수식$${objects} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {explain3} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"

    t1 = random.choice(['상자', '봉지', '바구니'])
    objects = random.choice(['사과', '포도', '오렌지', '복숭아', '배', '딸기', '귤', '참외', '자두', '키위', '망고'])

    ob_j = '가' if josa_check(objects[-1]) == ' ' else '이'
    num1 = random.randint(3, 9)
    num2 = random.randint(3, 9)
    answer_num = num1 * num2

    problem1, problem2 = num1, num2
    explain1, explain2 = num1, num2
    explain3 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num1, num2, answer_num)

    stem = stem.format(problem1=problem1, problem2=problem2, objects=objects, ob_j=ob_j, t1=t1)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, objects=objects, ob_j=ob_j, t1=t1)

    return stem, answer, comment






















# 2-2-2-21
def timestable222_Stem_007():
    stem = "㉠과 ㉡의 {problem}{prob_j1} 구해 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$    ㉡ $$수식$${problem2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${explain1}$$/수식$$, ㉡ $$수식$${explain2}$$/수식$$\n" \
              "{explain3}\n\n"
    
    problem = random.choice(['합', '차'])
    prob_j1 = '를' if josa_check(problem[-1]) == ' ' else '을'
    prob_j2 = '는' if josa_check(problem[-1]) == ' ' else '은'
    
    while 1:
        num1, num2 = random.sample(range(3, 9), 2)
        num4, num5 = random.sample(range(3, 9), 2)
        num3, num6 = num1 * num2, num4 * num5
        if num3 != num6:
            if problem == '합':
                answer_num = num3 + num6
                if 0 < answer_num < 100:
                    break
            else:
                answer_num = abs(num3 - num6)
                break

    problem1 = '{0} ` TIMES ` {1}'.format(num1, num2)
    problem2 = '{0} ` TIMES ` {1}'.format(num4, num5)
    explain1 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num1, num2, num3)
    explain2 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num4, num5, num6)
    if problem == '차':
        if num3 > num6:
            e3 = '{0} ` &gt; ` {1}'.format(num3, num6)
            e4 = '{0} ` - ` {1} ` = ` {2}'.format(num3, num6, answer_num)
        else:
            e3 = '{0} ` &lt; ` {1}'.format(num3, num6)
            e4 = '{0} ` - ` {1} ` = ` {2}'.format(num6, num3, answer_num)
        explain3 = '따라서 $$수식$${e3}$$/수식$$이므로 ㉠과 ㉡의 {problem}{prob_j2} $$수식$${e4}$$/수식$$'\
            .format(e3=e3, problem=problem, prob_j2=prob_j2, e4=e4)
    else:
        e3 = '{0} ` + ` {1} ` = ` {2}'.format(num6, num3, answer_num)
        explain3 = '따라서 ㉠과 ㉡의 {problem}{prob_j2} $$수식$${e3}$$/수식$$'\
            .format(problem=problem, prob_j2=prob_j2, e3=e3)

    stem = stem.format(problem1=problem1, problem2=problem2, prob_j1=prob_j1, problem=problem)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, problem=problem)

    return stem, answer, comment
























# 2-2-2-22
def timestable222_Stem_008():
    stem = "{objects1} 한 개를 장식하는 데 {objects2} $$수식$${problem1}$$/수식$$개가 필요합니다. {objects1} $$수식$${problem2}$$/수식$$개를 장식하는 데 필요한 {objects2}{ob_j1} 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$개\n"
    comment = "(해설)\n" \
              "{objects1} 한 개에 {objects2} $$수식$${explain1}$$/수식$$개씩, {objects1} $$수식$${explain2}$$/수식$$개를 " \
              "장식하는 데 필요한 {objects2}{ob_j1} 모두 $$수식$${explain3}$$/수식$$입니다.\n\n"
    
    objects1 = random.choice(['케이크', '와플', '디저트'])

    num1, num2 = random.sample(range(3, 9), 2)

    if num1 < 4 :
        objects2 = random.choice(['귤', '오렌지', '복숭아', '사과', '망고', '키위'])
    else :
        objects2 = random.choice(['체리', '딸기', '초콜릿', '쿠키', '포도', '바나나'])

    ob_j1 = '는' if josa_check(objects2[-1]) == ' ' else '은'

    answer_num = num1 * num2

    problem1, problem2 = num1, num2
    explain1, explain2 = num1, num2
    explain3 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num1, num2, answer_num)

    stem = stem.format(problem1=problem1, problem2=problem2, objects1=objects1, objects2=objects2, ob_j1=ob_j1)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3,
                             objects1=objects1, objects2=objects2, ob_j1=ob_j1)

    return stem, answer, comment

































# 2-2-2-23
def timestable222_Stem_009():
    stem = "{problem}\n$$표$$㉠ $$수식$${problem1}$$/수식$$    ㉡ $$수식$${problem2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$개\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${explain1}$$/수식$$  ㉡ $$수식$${explain2}$$/수식$$\n" \
              "{explain3} {explain5}{e5_j}로 " \
              "모두 $$수식$${explain6}$$/수식$$개입니다.\n\n"

    rand_num = random.randint(0, 1)
    if rand_num == 0:
        problem = '㉠보다 크고 ㉡보다 작은 수는 모두 몇 개인가요?'
    else:
        problem = '㉠보다 작고 ㉡보다 큰 수는 모두 몇 개인가요?'

    while 1:
        num1, num2 = random.sample(range(3, 9), 2)
        num4, num5 = random.sample(range(3, 9), 2)
        num3, num6 = num1 * num2, num4 * num5
        answer_num = num6 - num3 - 1
        if 1 < num6 - num3 - 1 < 10:
            break

    if rand_num == 0:
        problem1 = '{0} ` TIMES ` {1}'.format(num1, num2)
        problem2 = '{0} ` TIMES ` {1}'.format(num4, num5)
        explain1 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num1, num2, num3)
        explain2 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num4, num5, num6)
        e3, e4 = num3, num6
        explain3 = '따라서 $$수식$${e3}$$/수식$$보다 크고 $$수식$${e4}$$/수식$$보다 작은 수는'.format(e3=e3, e4=e4)

    else:
        problem1 = '{0} ` TIMES ` {1}'.format(num4, num5)
        problem2 = '{0} ` TIMES ` {1}'.format(num1, num2)
        explain1 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num4, num5, num6)
        explain2 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num1, num2, num3)
        e3, e4 = num6, num3
        explain3 = '따라서 $$수식$${e3}$$/수식$$보다 작고 $$수식$${e4}$$/수식$$보다 큰 수는'.format(e3=e3, e4=e4)

    explain5 = '$$수식$$'
    explain5 += '$$/수식$$, $$수식$$'.join([str(i) for i in range(num3 + 1, num6)])
    explain5 += '$$/수식$$'
    explain6 = answer_num

    e5_j = '으' if int(str(num6 - 1)[-1]) in [0, 3, 6] else ''

    stem = stem.format(problem1=problem1, problem2=problem2, problem=problem)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3,
                             explain5=explain5, explain6=explain6, e5_j=e5_j)

    return stem, answer, comment

























# 2-2-2-24
def timestable222_Stem_010():
    stem = "{sign}에 알맞은 수를 구해 보세요.\n$$표$${problem1}$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$이고, {explain2}이므로 {sign}$$수식$${explain3}$$/수식$$입니다.\n\n"

    sign = random.choice(['★', '●', '◆', '■', '▲'])
    num = random.choice([18, 12, 36, 24, 16])

    tmp = []
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            if i < 10 and num // i < 10:
                tmp.append([i, num // i])

    lst1 = random.choice(tmp)
    random.shuffle(lst1)
    idx = 0
    while 1:
        if tmp[idx][1] not in lst1:
            lst2 = tmp[idx]
            break
        idx += 1
    random.shuffle(lst2)
    num1, num2 = lst1
    num4, num5 = lst2
    num3, num6 = num1 * num2, num4 * num5

    problem1 = '$$수식$${0} ` TIMES `$$/수식$${1}$$수식$$` = ` {2} ` TIMES ` {3}$$/수식$$'.format(num1, sign, num4, num5)

    explain1 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num4, num5, num6)
    explain2 = '$$수식$${0} ` TIMES `$$/수식$${1}$$수식$$` = ` {2}$$/수식$$'.format(num1, sign, num3)
    explain3 = '` = ` {0}'.format(num2)

    answer_num = num2

    stem = stem.format(problem1=problem1, sign=sign)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, sign=sign)

    return stem, answer, comment





































# 2-2-2-25
def timestable222_Stem_011():
    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 {boxblank} 안에 들어갈 수 있는 수는 모두 몇 개인가요?\n$$표$$$$수식$${problem1}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$개\n"
    comment = "(해설)\n" \
              "{explain1}\n" \
              "{boxblank} 안에 들어갈 수 있는 수는 {explain2}{e2_j}로 모두 " \
              "$$수식$${explain3}$$/수식$$개입니다.\n\n"

    num1 = random.randint(3, 9)
    num1 = 6
    num2 = random.randint(num1 * 3 + 1, num1 * 9 - 1)

    boxblank = "□"

    if random.randint(0, 1) == 0:
        lst2 = ['$$수식$${0}$$/수식$$'.format(i) for i in range(1, 10) if num1 * i > num2]
        problem1 = '%s ` TIMES ` %d ` &gt; ` %d' % (boxblank, num1, num2)
    else:
        lst2 = ['$$수식$${0}$$/수식$$'.format(i) for i in range(1, 10) if num1 * i < num2]
        problem1 = '%s ` TIMES ` %d ` &lt; ` %d' % (boxblank, num1, num2)

    lst = ['$$수식$${0} ` TIMES ` {1} ` = ` {2}$$/수식$$'.format(num1, i, num1 * i) for i in range(1, 10)]

    explain1 = ', '.join(lst)
    explain2 = ', '.join(lst2)
    explain3 = len(lst2)
    answer_num = explain3

    e2_j = '으' if int(lst2[-1].replace('$$수식$$', '').replace('$$/수식$$', '')) in [0, 3, 6] else ''

    stem = stem.format(problem1=problem1, boxblank=boxblank)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, e2_j=e2_j, boxblank=boxblank)

    return stem, answer, comment




































# 2-2-2-26
def timestable222_Stem_012():
    stem = "곱이 {problem} 것부터 차례대로 기호를 써 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$    ㉡ $$수식$${problem2}$$/수식$$    ㉢ $$수식$${problem3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{answer_lst}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${explain1}$$/수식$$, ㉡ $$수식$${explain2}$$/수식$$, ㉢ $$수식$${explain3}$$/수식$$\n" \
              "따라서 $$수식$${explain4}$$/수식$$이므로 곱이 {problem} 것부터 차례대로 기호를 쓰면 {explain5}입니다.\n\n"
    while 1:
        num1, num2 = random.sample(range(3, 9), 2)
        num4, num5 = random.sample(range(3, 9), 2)
        num7, num8 = random.sample(range(3, 9), 2)
        num3, num6, num9 = num1 * num2, num4 * num5, num7 * num8
        if num3 != num6 and num3 != num9 and num6 != num9:
            break

    problem = random.choice(['큰', '작은'])
    problem1 = '{0} ` TIMES ` {1}'.format(num1, num2)
    problem2 = '{0} ` TIMES ` {1}'.format(num4, num5)
    problem3 = '{0} ` TIMES ` {1}'.format(num7, num8)

    explain1 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num1, num2, num3)
    explain2 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num4, num5, num6)
    explain3 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num7, num8, num9)
    tmp = [['㉠', num3], ['㉡', num6], ['㉢', num9]]

    if problem == '큰':
        tmp.sort(key=lambda x: x[1], reverse=True)
        explain4 = '$$수식$${0} ` &gt; ` {1} ` &gt; ` {2}$$/수식$$'.format(tmp[0][1], tmp[1][1], tmp[2][1])
    else:
        tmp.sort(key=lambda x: x[1])
        explain4 = '$$수식$${0} ` &lt; ` {1} ` &lt; ` {2}$$/수식$$'.format(tmp[0][1], tmp[1][1], tmp[2][1])

    explain5 = '{0}, {1}, {2}'.format(tmp[0][0], tmp[1][0], tmp[2][0])

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, problem=problem)
    answer = answer.format(answer_lst=explain5)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3,
                             explain4=explain4, explain5=explain5, problem=problem)

    return stem, answer, comment






































# 2-2-2-27
def timestable222_Stem_013():
    stem = "어떤 수에 $$수식$${problem1}$$/수식$${post1} 곱해야 하는데 잘못하여 $$수식$${problem2}$$/수식$${post2} 곱했더니 $$수식$${problem3}$$/수식$${post3} 되었습니다. 바르게 계산한 값은 얼마일까요?\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □라 하면 $$수식$${explain1}$$/수식$$이므로 " \
              "$$수식$${explain2}$$/수식$$에서 $$수식$${explain3}$$/수식$$입니다.\n" \
              "따라서 바르게 계산하면 $$수식$${explain4}$$/수식$$입니다.\n\n"

    num1 = random.randint(2, 9)
    num2, num4 = random.sample(range(2, 9), 2)
    num3, num5 = num1 * num2, num1 * num4
    answer_num = num3

    problem1, problem2, problem3 = num2, num4, num5

    boxblank = "□"

    explain1 = '%s ` TIMES ` %d ` = ` %d' % (boxblank, num4, num5)
    explain2 = '%d ` TIMES ` %d ` = ` %d' % (num1, num4, num5)
    explain3 = '%s ` = ` %d' % (boxblank, num1)
    explain4 = '%d ` TIMES ` %d ` = ` %d' % (num1, num2, num3)

    post1 = postposition(num2, flag=1)
    post2 = postposition(num4, flag=1)
    post3 = postposition(int(str(num5)[-1]))

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, post1=post1, post2=post2, post3=post3)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4)

    return stem, answer, comment



































# 2-2-2-28
def timestable222_Stem_014():
    stem = "조건에 알맞은 수를 구해 보세요.\n$$표$$㉮ $$수식$${problem1}$$/수식$$의 단 곱셈구구에 나오는 수입니다.\n㉯ $$수식$${problem2}$$/수식$$보다 큽니다.\n㉰ $$수식$${problem3}$$/수식$$의 단 곱셈구구에도 있습니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$의 단 곱셈구구에 나오는 수는 {explain2}입니다.\n" \
              "이 중에서 $$수식$${explain3}$$/수식$$보다 큰 수는 {explain4}이고, {explain5} 중에서 " \
              "$$수식$${explain6}$$/수식$$의 단 곱셈구구에도 있는 수는 $$수식$${explain7}$$/수식$$입니다.\n\n"

    while 1:
        num1, num4 = random.sample(range(2, 9), 2)
        num2, num3 = random.sample(range(2, 9), 2)
        num5, num6 = num1 * num4, num2 * num3
        if num5 > num6 and num1 < num6:
            break

    problem1, problem3 = num1, num4
    problem2 = '{0} ` TIMES ` {1}'.format(num2, num3)

    explain1 = num1
    explain2 = '$$수식$$'
    explain2 += '$$/수식$$, $$수식$$'.join([str(i * num1) for i in range(1, 10)])
    explain2 += '$$/수식$$'
    explain3 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num2, num3, num6)
    explain4 = '$$수식$$'
    explain4 += '$$/수식$$, $$수식$$'.join([str(i * num1) for i in range(1, 10) if num1 * i > num6])
    explain4 += '$$/수식$$'
    explain5 = explain4
    explain6 = num4
    explain7 = num5
    answer_num = num5

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             explain5=explain5, explain6=explain6, explain7=explain7)

    return stem, answer, comment



































# 2-2-2-30
def timestable222_Stem_015():
    stem = "수 카드를 한 번씩 모두 사용하여 만들 수 있는 곱셈식을 모두 구하려고 합니다. 만들 수 있는 곱셈식은 모두 몇 개인가요?\n$$표$$$$수식$${problem1}$$/수식$$ ➜ $$수식$${problem2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$의 단 곱셈구구에서 곱하는 수가 {explain2}인 경우를 차례대로 구합니다.\n" \
              "$$수식$${explain3}$$/수식$$, $$수식$${explain4}$$/수식$$, $$수식$${explain5}$$/수식$$\n" \
              "따라서 곱하는 수는 $$수식$${explain6}$$/수식$${e6_j} 될 수 있으므로 " \
              "만들 수 있는 곱셈식은 {explain7}입니다.\n\n"

    num1, num2, num3, cnt = random.choice([[2, 6, 1, 1], [6, 2, 1, 1],
                                           [3, 5, 1, 1], [5, 3, 1, 1],
                                           [4, 1, 6, 1],
                                           [4, 6, 2, 1], [6, 4, 2, 1],
                                           [5, 7, 3, 1], [7, 5, 3, 1],
                                           [5, 9, 4, 1], [9, 5, 4, 1],
                                           [6, 8, 4, 2], [8, 6, 4, 2],
                                           [7, 4, 9, 1],
                                           [9, 8, 1, 1]])


    box = '□'

    tmp = [num1, num2, num3]
    tmp.sort()

    boxzero = "$$수식$$BOX{``%d``}$$/수식$$" % tmp[0]
    boxone = "$$수식$$BOX{``%d``}$$/수식$$" % tmp[1]
    boxtwo = "$$수식$$BOX{``%d``}$$/수식$$" % tmp[2]

    problem1 = "%s %s %s" % (boxzero, boxone, boxtwo)
    # problem1 = '$$수식$$BOX{{``{0}``}}$$/수식$$  $$수식$$BOX{{``{1}``}}$$/수식$$  $$수식$$BOX{{``{2}``}}$$/수식$$'.format(tmp[0], tmp[1], tmp[2])
    problem2 = '{0} ` TIMES ` {1} ` = ` {2} ` {3}'.format(num1, box, box, box)

    explain1 = num1
    explain2 = '$$수식$$'
    explain2 += '$$/수식$$, $$수식$$'.join([str(i) for i in tmp])
    explain2 += '$$/수식$$'
    explain3 = '{0} ` TIMES ` {1} ` = ` {2}'\
        .format(num1, (num2 if num2 < num3 else num3), num1 * (num2 if num2 < num3 else num3))
    explain4 = '{0} ` TIMES ` {1} ` = ` {2}'\
        .format(num1, (num2 if num2 > num3 else num3), num1 * (num2 if num2 > num3 else num3))
    explain5 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num1, num1, num1 * num1)

    tmp = [[num1, num2, num3, num3], [num1, num3, num2, num2], [num1, num1, num2, num3]]
    tmp_lst = []

    for x, y, z, k in tmp:
        if str(z) in str(x * y):
            if str(k) in str(x * y):
                if y not in tmp_lst:
                    tmp_lst.append(y)
                if y not in tmp_lst:
                    tmp_lst.append(y)

    tmp_lst.sort()

    if len(tmp_lst) == 1:
        explain6 = '$$수식$${0}$$/수식$$'.format(tmp_lst[0])
        explain7 = '$$수식$${0} ` TIMES ` {1} ` = ` {2}$$/수식$$'.format(num1, tmp_lst[0], num1 * tmp_lst[0])
        e6_j = '이' if tmp_lst[0] in have_jongsung_num else '가'
    else:
        explain6 = '$$수식$${0}$$/수식$$ 또는 $$수식$${1}$$/수식$$'.format(tmp_lst[0], tmp_lst[1])
        explain7 = '$$수식$${0} ` TIMES ` {1} ` = ` {2}$$/수식$$, $$수식$${0} ` TIMES ` {3} ` = ` {4}$$/수식$$' \
            .format(num1, tmp_lst[0], num1 * tmp_lst[0], tmp_lst[1], num1 * tmp_lst[1])
        e6_j = '이' if tmp_lst[1] in have_jongsung_num else '가'

    answer_num = cnt
    stem = stem.format(problem1=problem1, problem2=problem2)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             explain5=explain5, explain6=explain6, explain7=explain7, e6_j=e6_j)

    return stem, answer, comment





























# 2-2-2-32
def timestable222_Stem_016():
    stem = "$$수식$${problem}$$/수식$${post} 곱이 같은 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$    ㉡ $$수식$${problem2}$$/수식$$    ㉢ $$수식$${problem3}$$/수식$$    ㉣ $$수식$${problem4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{answer_lst}\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$\n" \
              "㉠ $$수식$${explain2}$$/수식$$  ㉡ $$수식$${explain3}$$/수식$$\n" \
              "㉢ $$수식$${explain4}$$/수식$$  ㉣ $$수식$${explain5}$$/수식$$\n" \
              "따라서 $$수식$${explain6}$$/수식$${post} 곱이 같은 것은 {explain7}입니다.\n\n"

    num1 = random.randint(1, 9)

    while 1:
        num2, num3, num4, num5 = random.sample(range(2, 9), 4)
        if num1 not in [num2, num3, num4, num5]:
            break

    tmp = [[0, 0, 1, random.randint(2, 9)], [0, 1, 1, random.randint(2, 9)], [0, 0, 1, 0],
           [0, random.randint(2, 9), 1, random.randint(2, 9)]]
    tmp = random.choice(tmp)
    random.shuffle(tmp)
    num11, num12, num13, num14 = tmp

    rand = random.randint(1, 2)
    problem = '{0} ` TIMES ` {1}'.format(num1 if rand == 1 else 0, num1 if rand == 2 else 0)
    post = postposition(int(problem[-1]), flag=2)
    explain1 = '{0} ` = ` {1}'.format(problem, 0)

    rand = random.randint(1, 2)
    lst1 = '{0} ` TIMES ` {1}'.format(num2 if rand == 1 else num11, num2 if rand == 2 else num11)
    rand = random.randint(1, 2)
    lst2 = '{0} ` TIMES ` {1}'.format(num3 if rand == 1 else num12, num3 if rand == 2 else num12)
    rand = random.randint(1, 2)
    lst3 = '{0} ` TIMES ` {1}'.format(num4 if rand == 1 else num13, num4 if rand == 2 else num13)
    rand = random.randint(1, 2)
    lst4 = '{0} ` TIMES ` {1}'.format(num5 if rand == 1 else num14, num5 if rand == 2 else num14)
    tmp_lst = [[lst1, num2 * num11], [lst2, num3 * num12], [lst3, num4 * num13], [lst4, num5 * num14]]
    random.shuffle(tmp_lst)

    problem1, problem2, problem3, problem4 = tmp_lst[0][0], tmp_lst[1][0], tmp_lst[2][0], tmp_lst[3][0]
    explain2 = '{0} ` = ` {1}'.format(tmp_lst[0][0], tmp_lst[0][1])
    explain3 = '{0} ` = ` {1}'.format(tmp_lst[1][0], tmp_lst[1][1])
    explain4 = '{0} ` = ` {1}'.format(tmp_lst[2][0], tmp_lst[2][1])
    explain5 = '{0} ` = ` {1}'.format(tmp_lst[3][0], tmp_lst[3][1])
    sign = ['㉠', '㉡', '㉢', '㉣']

    answer_lst = []

    for idx, lst in enumerate(tmp_lst):
        if lst[1] == 0:
            answer_lst.append(sign[idx])

    explain6 = problem
    explain7 = ', '.join(answer_lst)
    answer_lst = explain7

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, problem=problem, problem4=problem4,
                       post=post)
    answer = answer.format(answer_lst=answer_lst)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, post=post,
                             explain4=explain4, explain5=explain5, explain6=explain6, explain7=explain7)

    return stem, answer, comment



































# 2-2-2-33
def timestable222_Stem_017():
    stem = "$$수식$${problem1}$$/수식$${sign}에서 {sign}에 알맞은 수를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$이므로 $$수식$${explain2}$$/수식$${sign}의 곱도 " \
              "$$수식$${explain3}$$/수식$$입니다.\n" \
              "$$수식$${explain4}$$/수식$$이므로 {sign}에 알맞은 수는 " \
              "$$수식$${explain5}$$/수식$$입니다.\n\n"

    sign = random.choice(['★', '●', '◆', '■', '▲'])

    if random.randint(1, 4) == 1:
        # 4, 9
        if random.randint(1, 2) == 1:
            tmp = [[4, 1], [2, 2]]
        else:
            tmp = [[9, 1], [3, 3]]
        random.shuffle(tmp)
        tmp1, tmp2 = tmp[0], tmp[1]
        random.shuffle(tmp1)
        random.shuffle(tmp2)
        num1, num2 = tmp1
        num3, num4 = tmp2
    else:
        n1, n2 = random.sample(range(1, 9), 2)
        tmp = [[0, n1], [n2, 0]]
        tmp1, tmp2 = tmp[0], tmp[1]
        random.shuffle(tmp1)
        num1, num2 = tmp1
        num3, num4 = tmp2

    problem1 = '{0} ` TIMES ` {1} ` = ` {2} ` TIMES `'.format(num1, num2, num3)
    explain1 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num1, num2, num1 * num2)
    explain2 = '{0} ` TIMES `'.format(num3)
    explain3 = num1 * num2
    explain4 = '{0} ` TIMES ` {1} ` = ` {2}'.format(num3, num4, num3 * num4)
    explain5 = num4
    answer_num = num4

    stem = stem.format(problem1=problem1, sign=sign)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             explain5=explain5, sign=sign)

    return stem, answer, comment





































# 2-2-2-34
def timestable222_Stem_018():
    stem = "{problem} {objects2}{ob_j} $$수식$${problem1}$$/수식$$개 만들려면 {objects1}가 몇 장 필요한가요?\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$장\n"
    comment = "(해설)\n" \
              "{objects2} 한 개를 만드는 데 {objects1} $$수식$$1$$/수식$$장이 사용되므로 " \
              "{objects2} $$수식$${explain1}$$/수식$$개를 만들기 위해서는 {objects1} " \
              "$$수식$${explain1}$$/수식$$장이 필요합니다.\n\n"

    objects1 = random.choice(['색종이', '색지', '학종이', '한지'])
    objects2 = random.choice(['종이학', '종이배', '장미', '종이별'])
    ob_j = '를' if josa_check(objects2[-1]) == ' ' else '을'

    num1 = random.randint(2, 9)
    problem1 = num1
    explain1 = num1
    answer_num = num1

    if random.randint(0, 1) == 0:
        problem = '{objects1} $$수식$$1$$/수식$$장을 사용하여 {objects2}{ob_j} 만들 수 있습니다.'\
            .format(objects1=objects1, objects2=objects2, ob_j=ob_j)
    else:
        problem = '{objects2} $$수식$$1$$/수식$$개를 만들려면 {objects1} $$수식$$1$$/수식$$장이 사용됩니다.'\
            .format(objects2=objects2, objects1=objects1)

    stem = stem.format(problem=problem, problem1=problem1, objects1=objects1, objects2=objects2, ob_j=ob_j)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, objects1=objects1, objects2=objects2)

    return stem, answer, comment



































# 2-2-2-35
def timestable222_Stem_019():
    stem = "{sports} 경기에서 $$수식$$1$$/수식$$등은 $$수식$${rand1}$$/수식$$점, $$수식$$2$$/수식$$등은 $$수식$${rand2}$$/수식$$점, $$수식$$3$$/수식$$등은 $$수식$${rand3}$$/수식$$점을 얻습니다. {people}{j1}네 모둠은 $$수식$$1$$/수식$$등이 $$수식$${problem1}$$/수식$$명, $$수식$$2$$/수식$$등이 $$수식$${problem2}$$/수식$$명, $$수식$$3$$/수식$$등이 $$수식$${problem3}$$/수식$$명입니다. {people}{j1}네 모둠의 {sports} 점수는 모두 몇 점인가요?\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$점\n"
    comment = "(해설)\n" \
              "$$수식$$1$$/수식$$등이 $$수식$${explain1}$$/수식$$명 → $$수식$${explain2} ` LEFT ($$/수식$$점$$수식$$RIGHT )$$/수식$$, \n" \
              "$$수식$$2$$/수식$$등이 $$수식$${explain3}$$/수식$$명 → $$수식$${explain4} ` LEFT ($$/수식$$점$$수식$$RIGHT )$$/수식$$, \n" \
              "$$수식$$3$$/수식$$등이 $$수식$${explain5}$$/수식$$명 → $$수식$${explain6} ` LEFT ($$/수식$$점$$수식$$RIGHT )$$/수식$$\n" \
              "→ $$수식$$LEFT ($$/수식$${people}{j1}네 모둠의 {sports} 점수$$수식$$RIGHT ) ` {explain7} ` LEFT ($$/수식$$점$$수식$$RIGHT )$$/수식$$\n\n"

    sports = random.choice(['달리기', '멀리뛰기', '줄넘기', '림보'])
    people = random.choice(person_nam+person_yeo)
    j1 = '' if josa_check(people[-1]) == ' ' else '이'

    while 1:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        num3 = random.randint(2, 9)
        rand1, rand2, rand3 = random.choice([[3, 2, 1], [5, 3, 1], [4, 2, 1], [4, 3, 2], [5, 4, 3], [4, 3, 1]])

        num4, num5, num6 = num1 * rand1, num2 * rand2, num3 * rand3
        answer_num = num4 + num5 + num6
        if answer_num < 100:
            break

    problem1, problem2, problem3 = num1, num2, num3
    explain1, explain3, explain5 = num1, num2, num3

    explain2 = '{0} ` TIMES ` {1} ` = ` {2}'.format(rand1, num1, num4)
    explain4 = '{0} ` TIMES ` {1} ` = ` {2}'.format(rand2, num2, num5)
    explain6 = '{0} ` TIMES ` {1} ` = ` {2}'.format(rand3, num3, num6)
    explain7 = '` = ` {0} ` + ` {1} ` + ` {2} ` = ` {3}'.format(num4, num5, num6, answer_num)

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, people=people, sports=sports, j1=j1,
                       rand1=rand1, rand2=rand2, rand3=rand3)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             explain5=explain5, explain6=explain6, explain7=explain7, people=people, sports=sports, j1=j1,
                             ran1=rand1, rand2=rand2, rand3=rand3)

    return stem, answer, comment







































# 2-2-2-36
def timestable222_Stem_020():
    stem = "$$수식$$4$$/수식$$장의 수 카드 중에서 $$수식$$2$$/수식$$장을 뽑아 두 수의 곱을 구하려고 합니다. 가장 큰 곱과 가장 작은 곱을 각각 구해 보세요.\n{problem1}\n"
    answer = "(정답)\n$$수식$${answer_num1}$$/수식$$, $$수식$${answer_num2}$$/수식$$\n"
    comment = "(해설)\n" \
              "수의 크기를 비교하면 $$수식$${explain1}$$/수식$$입니다.\n" \
              "가장 큰 수는 $$수식$${explain2}$$/수식$$이고, 두 번째로 큰 수는 $$수식$${explain3}$$/수식$$이므로 " \
              "가장 큰 곱은 $$수식$${explain4}$$/수식$$입니다.\n" \
              "가장 작은 수는 $$수식$${explain5}$$/수식$$이고, 두 번째로 작은 수는 $$수식$${explain6}$$/수식$$이므로 " \
              "가장 작은 곱은 $$수식$${explain7}$$/수식$$입니다.\n\n"

    num1, num2, num3, num4 = random.sample(range(10), 4)

    problem1 = '$$수식$$BOX{``%d``}$$/수식$$  $$수식$$BOX{``%d``}$$/수식$$  ' \
               '$$수식$$BOX{``%d``}$$/수식$$  $$수식$$BOX{``%d``}$$/수식$$' % (num1, num2, num3, num4)

    tmp = [num1, num2, num3, num4]
    tmp.sort()
    explain1 = '` &lt; `'.join([str(i) for i in tmp])
    explain2 = tmp[-1]
    explain3 = tmp[-2]
    answer_num1 = explain2 * explain3
    explain4 = '{0} ` TIMES ` {1} ` = ` {2}'.format(explain2, explain3, answer_num1)
    explain5 = tmp[0]
    explain6 = tmp[1]
    answer_num2 = explain5 * explain6
    explain7 = '{0} ` TIMES ` {1} ` = ` {2}'.format(explain5, explain6, answer_num2)

    stem = stem.format(problem1=problem1)
    answer = answer.format(answer_num1=answer_num1, answer_num2=answer_num2)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             explain5=explain5, explain6=explain6, explain7=explain7)

    return stem, answer, comment




































# 2-2-2-39
def timestable222_Stem_021():
    stem = "{objects} $$수식$${problem1}$$/수식$$개씩 $$수식$${problem2}$$/수식$$묶음은 {objects} $$수식$${problem2}$$/수식$$개씩 몇 묶음과 같은지 구해 보세요.\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$묶음\n"
    comment = "(해설)\n" \
              "곱셈구구에서 곱하는 두 수의 순서를 바꾸어도 곱은 같으므로 " \
              "$$수식$${explain1}$$/수식$$개씩 $$수식$${explain2}$$/수식$$묶음은 " \
              "$$수식$${explain2}$$/수식$$개씩 $$수식$${explain1}$$/수식$$묶음과 같습니다.\n" \
              "→ $$수식$${explain3}$$/수식$$\n\n"

    objects = random.choice(['사과', '포도', '오렌지', '복숭아', '석류', '젤리', '배', '딸기', '지우개'])

    num1, num2 = random.sample(range(2, 10), 2)

    problem1, problem2 = num1, num2
    explain1, explain2 = num1, num2
    explain3 = '{0} ` TIMES ` {1} ` = ` {1} ` TIMES ` {0}'.format(num1, num2)

    stem = stem.format(problem1=problem1, problem2=problem2, objects=objects)
    answer = answer.format(answer_num=num1)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, objects=objects)

    return stem, answer, comment











# if __name__ == '__main__':
#     TimesTable_Stem_001()
#     TimesTable_Stem_002()
#     TimesTable_Stem_003()
#     TimesTable_Stem_004()
#     TimesTable_Stem_005()
#     TimesTable_Stem_006()
#     TimesTable_Stem_007()
#     TimesTable_Stem_008()
#     TimesTable_Stem_009()
#     TimesTable_Stem_010()
#     TimesTable_Stem_011()
#     TimesTable_Stem_012()
#     TimesTable_Stem_013()
#     TimesTable_Stem_014()
#     TimesTable_Stem_015()
#     TimesTable_Stem_016()
#     TimesTable_Stem_017()
#     TimesTable_Stem_018()
#     TimesTable_Stem_019()
#     TimesTable_Stem_020()
#     TimesTable_Stem_021()






