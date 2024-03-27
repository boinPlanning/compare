import random
import codecs
import os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../Dictionary')


person_nam = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XY.txt'), 'r', 'utf-8').readlines()]
person_yeo = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XX.txt'), 'r', 'utf-8').readlines()]



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













# 2-1-6-08
def multiplication216_Stem_001():
    stem = "보기와 같이 나타내어 보세요.\n$$표$$[보기]\n$$수식$${problem1}$$/수식$$의 $$수식$${problem2}$$/수식$$배 → {problem3}$$/표$$\n$$수식$${problem4}$$/수식$$의 $$수식$${problem5}$$/수식$$배 → $$수식$${boxblank}$$/수식$$\n"
    answer = "(정답)\n{cor_num}\n"
    comment = "(해설)\n" \
              "$$수식$${problem4}$$/수식$$의 $$수식$${problem5}$$/수식$$배 → {explain3}\n\n"
    while 1:
        num1, num2, num3, num4 = random.sample(range(2, 10), 4)
        if num2 <= 6 and num4 <= 6:
            break

    problem3 = '$$수식$${num1}'.format(num1=num1)
    for i in range(num2- 1):
        problem3 += ' ` + ` ' + str(num1)
    problem3 += ' ` = ` {num1_num2}$$/수식$$'.format(num1_num2=num1*num2)

    explain3 = '$$수식$${num3}'.format(num3=num3)
    for i in range(num4 - 1):
        explain3 += ' ` + ` ' + str(num3)
    explain3 += ' ` = ` {num3_num4}$$/수식$$'.format(num3_num4=num3 * num4)

    boxblank = "BOX{　　　　　　　　　　　}"
    
    stem = stem.format(problem1=num1, problem2=num2, problem3=problem3, problem4=num3, problem5=num4, boxblank=boxblank)
    answer = answer.format(cor_num=explain3)
    comment = comment.format(problem4=num3, problem5=num4, explain3=explain3)

    return stem, answer, comment





















# 2-1-6-11
def multiplication216_Stem_002():
    stem = "곱셈식 $$수식$${problem1}$$/수식$${post} 잘못 읽은 것을 찾아 기호를 써 보세요.\n$$표$$㉠ {problem2}\n㉡ {problem3}\n㉢ {problem4}\n㉣ {problem5}$$/표$$\n"
    answer = "(정답)\n{answer_num}\n"
    comment = "(해설)\n" \
              "{explain}\n\n"

    num1, num2 = random.sample(range(2, 10), 2)
    num3 = num1 * num2
    problem1 = '{num1} `TIMES` {num2} `=` {num3}'.format(num1=num1, num2=num2, num3=num3)

    rand_prob = random.choice([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    if rand_prob[0] == 1:
        lst1 = '$$수식$${num1}$$/수식$${post1} $$수식$${num2}$$/수식$${post2} 더하면 $$수식$${num3}$$/수식$$입니다.'\
            .format(num1=num1, post1=postposition(num1, flag=2), num2=num2, post2=postposition(num2, flag=1), num3=num3)
    else:
        lst1 = '$$수식$${num1}$$/수식$${post1} $$수식$${num2}$$/수식$${post2} 곱하면 $$수식$${num3}$$/수식$$입니다.' \
            .format(num1=num1, post1=postposition(num1, flag=2), num2=num2, post2=postposition(num2, flag=1), num3=num3)
    e1 = '$$수식$${num1}$$/수식$${post1} $$수식$${num2}$$/수식$${post2} 곱하면 $$수식$${num3}$$/수식$$입니다.' \
        .format(num1=num1, post1=postposition(num1, flag=2), num2=num2, post2=postposition(num2, flag=1), num3=num3)

    if rand_prob[1] == 1:
        lst2 = '$$수식$${num1}$$/수식$$ 더하기 $$수식$${num2}$$/수식$${post1} $$수식$${num3}$$/수식$$입니다.'\
            .format(num1=num1, num2=num2, post1=postposition(num2, flag=3), num3=num3)
    else:
        lst2 = '$$수식$${num1}$$/수식$$ 곱하기 $$수식$${num2}$$/수식$${post1} $$수식$${num3}$$/수식$$입니다.' \
            .format(num1=num1, num2=num2, post1=postposition(num2, flag=3), num3=num3)
    e2 = '$$수식$${num1}$$/수식$$ 곱하기 $$수식$${num2}$$/수식$${post1} $$수식$${num3}$$/수식$$입니다.' \
        .format(num1=num1, num2=num2, post1=postposition(num2, flag=3), num3=num3)
    if rand_prob[2] == 1:
        lst3 = '$$수식$${num1}$$/수식$$ 더하기 $$수식$${num2}$$/수식$${post1} $$수식$${num3}$$/수식$${post2} 같습니다.' \
            .format(num1=num1, num2=num2, post1=postposition(num2, flag=3), num3=num3,
                    post2=postposition(int(str(num3)[-1]), flag=2))
    else:
        lst3 = '$$수식$${num1}$$/수식$$ 곱하기 $$수식$${num2}$$/수식$${post1} $$수식$${num3}$$/수식$${post2} 같습니다.' \
            .format(num1=num1, num2=num2, post1=postposition(num2, flag=3), num3=num3,
                    post2=postposition(int(str(num3)[-1]), flag=2))
    e3 = '$$수식$${num1}$$/수식$$ 곱하기 $$수식$${num2}$$/수식$${post1} $$수식$${num3}$$/수식$${post2} 같습니다.' \
        .format(num1=num1, num2=num2, post1=postposition(num2, flag=3), num3=num3,
                post2=postposition(int(str(num3)[-1]), flag=2))
    if rand_prob[3] == 1:
        lst4 = '$$수식$${num1}$$/수식$${post1} $$수식$${num2}$$/수식$$의 합은 $$수식$${num3}$$/수식$$입니다.' \
            .format(num1=num1, post1=postposition(num1, flag=2), num2=num2, num3=num3)
    else:
        lst4 = '$$수식$${num1}$$/수식$${post1} $$수식$${num2}$$/수식$$의 곱은 $$수식$${num3}$$/수식$$입니다.' \
            .format(num1=num1, post1=postposition(num1, flag=2), num2=num2, num3=num3)
    e4 = '$$수식$${num1}$$/수식$${post1} $$수식$${num2}$$/수식$$의 곱은 $$수식$${num3}$$/수식$$입니다.' \
        .format(num1=num1, post1=postposition(num1, flag=2), num2=num2, num3=num3)

    lst = [[lst1, rand_prob[0], e1], [lst2, rand_prob[1], e2], [lst3, rand_prob[2], e3], [lst4, rand_prob[3], e4]]
    random.shuffle(lst)

    problem2, problem3, problem4, problem5 = lst[0][0], lst[1][0], lst[2][0], lst[3][0]
    tmp = ['㉠', '㉡', '㉢', '㉣']

    for idx, i in enumerate(lst):
        if i[1] == 1:
            answer_num = tmp[idx]
            explain = answer_num + ' ' + i[2]

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, problem4=problem4, problem5=problem5,
                       post=postposition(int(str(num3)[-1]), flag=1))
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain=explain)

    return stem, answer, comment
















# 2-1-6-12
def multiplication216_Stem_003():
    stem = "곱셈식을 덧셈식으로 나타낸 것입니다. 틀린 것을 찾아 기호를 써 보세요.\n$$표$$㉠ {problem1}\n㉡ {problem2}\n㉢ {problem3}$$/표$$\n"
    answer = "(정답)\n{answer_num}\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$${post} 덧셈식으로 나타내면 $$수식$${explain2}$$/수식$$입니다.\n\n"


    while 1:
        num1, num2 = random.sample(range(2, 10), 2)
        num4, num5 = random.sample(range(2, 10), 2)
        num7, num8 = random.sample(range(2, 10), 2)
        if (num1, num2) != (num4, num5) and (num1, num2) != (num7, num8) and (num7, num8) != (num4, num5):
            break
    num3 = num1 * num2
    num6 = num4 * num5
    num9 = num7 * num8

    lst1 = '$$수식$${num1} ` TIMES ` {num2} ` = ` {num3}$$/수식$$\n' \
           '→ $$수식$${num} ` = ` {num3}$$/수식$$'.format(num1=num1, num2=num2, num3=num3,
                                                    num=' ` + ` '.join([str(num1) for i in range(num2)]))
    lst2 = '$$수식$${num4} ` TIMES ` {num5} ` = ` {num6}$$/수식$$\n' \
           '→ $$수식$${num} ` = ` {num6}$$/수식$$'.format(num4=num4, num5=num5, num6=num6,
                                                    num=' ` + ` '.join([str(num4) for i in range(num5)]))
    lst3 = '$$수식$${num7} ` TIMES ` {num8} ` = ` {num9}$$/수식$$\n' \
           '→ $$수식$${num} ` = ` {num9}$$/수식$$'.format(num7=num7, num8=num8, num9=num9,
                                                    num=' ` + ` '.join([str(num8) for i in range(num8)]))
    explain1 = '{num7} ` TIMES ` {num8} ` = ` {num9}'.format(num7=num7, num8=num8, num9=num9)
    explain2 = '{num} ` = ` {num9}'.format(num9=num9, num=' ` + ` '.join([str(num7) for i in range(num8)]))

    # lst4가 정답....
    lst = [[lst1, 0], [lst2, 0], [lst3, 1]]
    random.shuffle(lst)
    problem1, problem2, problem3 = lst[0][0], lst[1][0], lst[2][0]

    tmp = ['㉠', '㉡', '㉢']
    for idx, i in enumerate(lst):
        if i[1] == 1:
            answer_num = tmp[idx]

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, post=postposition(int(str(num9)[-1]), flag=1))

    return stem, answer, comment
























# 2-1-6-16
def multiplication216_Stem_004():
    stem = "㉠과 ㉡이 나타내는 수의 차는 얼마인가요?\n$$표$$㉠ {problem1}    ㉡ {problem2}$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ {problem1}\n" \
              "→ $$수식$${explain1}$$/수식$$\n" \
              "㉡ {problem2}\n" \
              "→ $$수식$${explain2}$$/수식$$\n" \
              "$$수식$${explain3}$$/수식$$\n\n"

    while 1:
        num1, num2, num4, num5 = random.sample(range(2, 10), 4)
        num3 = num1 * num2
        num6 = num4 * num5
        if 0 < abs(num3 - num6) < 10:
            break

    p1 = '$$수식$${num1}$$/수식$$의 $$수식$${num2}$$/수식$$배'.format(num1=num1, num2=num2)
    p2 = '$$수식$${num4}$$/수식$$ 곱하기 $$수식$${num5}$$/수식$$'.format(num4=num4, num5=num5)

    e1 = '{num1} ` TIMES ` {num2} ` = ` {num} ` = ` {num3}'\
        .format(num1=num1, num2=num2, num3=num3, num=' ` + ` '.join([str(num1) for i in range(num2)]))
    e2 = '{num4} ` TIMES ` {num5} ` = ` {num} ` = ` {num6}' \
        .format(num4=num4, num5=num5, num6=num6, num=' ` + ` '.join([str(num4) for i in range(num5)]))

    lst = [[p1, e1, num3], [p2, e2, num6]]
    random.shuffle(lst)

    if lst[0][2] > lst[1][2]:
        answer_num = lst[0][2] - lst[1][2]
        explain3 = '㉠ ` - ` ㉡ ` = ` {num3} ` - ` {num6} ` = ` {answer_num}'\
            .format(num3=lst[0][2], num6=lst[1][2], answer_num=answer_num)
    else:
        answer_num = lst[1][2] - lst[0][2]
        explain3 = '㉡ ` - ` ㉠ ` = ` {num6} ` - ` {num3} ` = ` {answer_num}'\
            .format(num3=lst[0][2], num6=lst[1][2], answer_num=answer_num)

    problem1, problem2 = lst[0][0], lst[1][0]
    explain1, explain2 = lst[0][1], lst[1][1]

    stem = stem.format(problem1=problem1, problem2=problem2)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(problem1=problem1, problem2=problem2,
                             explain1=explain1, explain2=explain2, explain3=explain3)

    return stem, answer, comment






















# 2-1-6-17
def multiplication216_Stem_005():
    stem = "{t1}{j1}는 {object}{j2_1} $$수식$${problem1}$$/수식$${unit}씩 $$수식$${problem2}$$/수식$$묶음을 가지고 있습니다. 그중에서 {t2}에게 $$수식$${problem3}$$/수식$${unit}{j3} 주었다면 남은 {object}{j2_2} 몇 {unit}인가요?\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$${unit}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$처음에 가지고 있던 {object}의 수$$수식$$RIGHT ) ` {explain1} ` LEFT ($$/수식$${unit}$$수식$$RIGHT )$$/수식$$\n" \
              "→ $$수식$$LEFT ($$/수식$$남은 {object}의 수$$수식$$RIGHT ) ` {explain2} ` LEFT ($$/수식$${unit}$$수식$$RIGHT )$$/수식$$\n\n"

    num1, num2 = random.sample(range(2, 10), 2)
    num3 = num1 * num2
    num4 = random.choice(range(1, num3 - 4))
    answer_num = num3 - num4

    object_dict = {'자루' : ['연필', '붓', '색연필'],
                    '장' : ['색종이', '학종이', '포장지'],
                    '권' : ['공책', '동화책', '국어책']}

    t1 = random.choice(person_nam+person_yeo)
    t2 = random.choice(['언니', '오빠', '동생']) if t1 in person_yeo else random.choice(['형', '누나', '동생'])
    j1 = '' if josa_check(t1[-1]) == ' ' else '이'

    unit = random.choice(list(object_dict.keys()))
    object = random.choice(object_dict.get(unit))

    j2_1 = '를' if josa_check(object[-1]) == ' ' else '을'
    j2_2 = '는' if j2_1 == '를' else '은'
    j3 = '를' if josa_check(unit[-1]) == ' ' else '을'

    explain1 = ' ` = ` {num1} ` TIMES ` {num2} ` = ` {num3}'.format(num1=num1, num2=num2, num3=num3)
    explain2 = ' ` = ` {num3} ` - ` {num4} ` = ` {answer_num}'.format(num3=num3, num4=num4, answer_num=answer_num)

    stem = stem.format(problem1=num1, problem2=num2, problem3=num4, t1=t1, t2=t2, object=object, unit=unit, j1=j1, j2_1=j2_1, j2_2=j2_2, j3=j3)
    answer = answer.format(answer_num=answer_num, unit=unit)
    comment = comment.format(object=object, explain1=explain1, explain2=explain2, unit=unit)

    return stem, answer, comment
























# 2-1-6-19
def multiplication216_Stem_006():
    stem = "{objects}{ob_j} {people1}{p1_j1}는 $$수식$${problem1}$$/수식$${unit}씩 $$수식$${problem2}$$/수식$$묶음 가지고 있고, {people2}{p2_j}는 $$수식$${problem3}$$/수식$${unit}씩 $$수식$${problem4}$$/수식$$묶음을 가지고 있습니다. {people1}{p1_j2} {people2} 중 {objects}{ob_j} 더 많이 가지고 있는 사람은 누구인가요?\n"
    answer = "(정답)\n{answer_people}\n"
    comment = "(해설)\n" \
              "{people1} : $$수식$${problem1}$$/수식$$장씩 $$수식$${problem2}$$/수식$$묶음 " \
              "→ $$수식$${explain1} ` LEFT ($$/수식$${unit}$$수식$$RIGHT )$$/수식$$\n" \
              "{people2} : $$수식$${problem3}$$/수식$$장씩 $$수식$${problem4}$$/수식$$묶음 " \
              "→ $$수식$${explain2} ` LEFT ($$/수식$${unit}$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 $$수식$${explain3}$$/수식$$이므로 {objects}{ob_j} 더 많이 가지고 있는 사람은 {answer_people}입니다.\n\n"

    object_dict = {'자루' : ['연필', '붓', '색연필'],
                    '장' : ['색종이', '학종이', '포장지'],
                    '권' : ['공책', '동화책', '국어책']}
    unit = random.choice(list(object_dict.keys()))
    objects = random.choice(object_dict.get(unit))

    ob_j = '를' if josa_check(objects[-1]) == ' ' else '을'
    terms = [random.choice(person_nam), random.choice(person_yeo)]
    random.shuffle(terms)
    people1, people2 = terms

    p1_j1 = '' if josa_check(people1[-1]) == ' ' else '이'
    p1_j2 = '와' if josa_check(people1[-1]) == ' ' else '과'
    p2_j = '' if josa_check(people2[-1]) == ' ' else '이'


    while 1:
        num1, num2, num4, num5 = random.sample(range(2, 10), 4)
        num3 = num1 * num2
        num6 = num4 * num5
        if 0 < abs(num3 - num6) < 10:
            break

    if num3 > num6:
        answer_people = people1
        explain3 = '{num3} ` &gt; ` {num6}'.format(num3=num3, num6=num6)
    else:
        answer_people = people2
        explain3 = '{num3} ` &lt; ` {num6}'.format(num3=num3, num6=num6)

    explain1 = '{num1} ` TIMES ` {num2} ` = ` {num3}'.format(num1=num1, num2=num2, num3=num3)
    explain2 = '{num4} ` TIMES ` {num5} ` = ` {num6}'.format(num4=num4, num5=num5, num6=num6)

    stem = stem.format(problem1=num1, problem2=num2, problem3=num4, problem4=num5,
                       people1=people1, people2=people2, objects=objects, ob_j=ob_j, p1_j1=p1_j1, p1_j2=p1_j2, p2_j=p2_j, unit=unit)
    answer = answer.format(answer_people=answer_people)
    comment = comment.format(problem1=num1, problem2=num2, problem3=num4, problem4=num5, answer_people=answer_people,
                             objects=objects, explain1=explain1, explain2=explain2, explain3=explain3,
                             people1=people1, people2=people2, ob_j=ob_j, unit=unit)

    return stem, answer, comment




























# 2-1-6-20
def multiplication216_Stem_007():
    stem = "한 묶음에 $$수식$${problem1}$$/수식$${unit}씩 묶여 있는 {objects}{ob_j} {people1}{p1_j}는 $$수식$${problem2}$$/수식$$묶음 가지고 있고, {people2}{p2_j}는 $$수식$${problem3}$$/수식$$묶음 가지고 있습니다. 누가 {objects}{ob_j} 몇 {unit} 더 많이 가지고 있을까요?\n$$수식$${boxone}$$/수식$$가 $$수식$${boxtwo}$$/수식$${unit} 더 많이 가지고 있습니다.\n"
    answer = "(정답)\n{answer_people}, $$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "{explain1}보다 {objects}을 $$수식$${explain2} ` LEFT ($$/수식$$묶음$$수식$$RIGHT )$$/수식$$ 더 많이 가지고 있으므로 " \
              "$$수식$${explain3} ` LEFT ($$/수식$${unit}$$수식$$RIGHT )$$/수식$$ 더 많이 가지고 있습니다.\n\n"

    object_dict = {'자루' : ['연필', '붓', '색연필'],
                    '장' : ['색종이', '학종이', '포장지'],
                    '권' : ['공책', '동화책', '국어책']}

    unit = random.choice(list(object_dict.keys()))
    objects = random.choice(object_dict.get(unit))
    ob_j = '를' if josa_check(objects[-1]) == ' ' else '을'

    terms = [random.choice(person_nam), random.choice(person_yeo)]
    random.shuffle(terms)
    people1, people2 = terms
    p1_j = '' if josa_check(people1[-1]) == ' ' else '이'
    p2_j = '' if josa_check(people2[-1]) == ' ' else '이'

    while 1:
        num1 = random.choice(range(4, 10))
        num2, num3 = random.sample(range(2, 10), 2)
        num4 = abs(num2 - num3)
        num5 = num1 * num4
        if num5 < 10:
            break

    if num2 > num3:
        explain1 = '{people1}{p1_j}는 {people2}'.format(people1=people1, people2=people2, p1_j=p1_j)
        explain2 = '{num2} ` - ` {num3} ` = ` {num4}'.format(num2=num2, num3=num3, num4=num4)
        answer_people = '{people1}'.format(people1=people1)
    else:
        explain1 = '{people2}{p2_j}는 {people1}'.format(people1=people1, people2=people2, p2_j=p2_j)
        explain2 = '{num3} ` - ` {num2} ` = ` {num4}'.format(num2=num2, num3=num3, num4=num4)
        answer_people = '{people2}'.format(people2=people2)

    explain3 = '{num1} ` TIMES ` {num4} ` = ` {num5}'.format(num1=num1, num4=num4, num5=num5)
    answer_num = num5

    boxone = "BOX{~①~}"
    boxtwo = "BOX{~②~}"

    stem = stem.format(problem1=num1, problem2=num2, problem3=num3, people1=people1, people2=people2, objects=objects,
                       unit=unit, p1_j=p1_j, p2_j=p2_j, ob_j=ob_j, boxone=boxone, boxtwo=boxtwo)
    answer = answer.format(answer_people=answer_people, answer_num=answer_num)
    comment = comment.format(objects=objects, explain1=explain1, explain2=explain2, explain3=explain3, unit=unit)

    return stem, answer, comment






























# 2-1-6-21
def multiplication216_Stem_008():
    stem = "□ 안에 알맞은 수가 큰 순서대로 기호를 써 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$    ㉡ $$수식$${problem2}$$/수식$$\n㉢ $$수식$${problem3}$$/수식$$    ㉣ $$수식$${problem4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{answer_lst}\n"
    comment = "(해설)\n" \
              "㉠ {explain1}\n" \
              "㉡ {explain2}\n" \
              "㉢ {explain3}\n" \
              "㉣ {explain4}\n" \
              "→ {explain5}\n\n"

    box = '□'

    while 1:
        num2, num5, num7, num10 = random.sample(range(2, 10), 4)
        num1, num4, num8, num11 = random.sample(range(2, 10), 4)
        num3, num6, num9, num12 = num1 * num2, num4 * num5, num7 * num8, num10 * num11
        if num3 != num6 and num3 != num9 and num3 != num12 and num6 != num9 and num6 != num12 and num9 != num12:
            break

    p1 = '{num1} ` TIMES ` {box} ` = ` {num3}'.format(num1=num1, num3=num3, box=box)
    e1 = '$$수식$${num1} ` TIMES ` {num2} ` = ` {num3}$$/수식$$이므로 $$수식$${box} ` = ` {num2}$$/수식$$입니다.'\
        .format(num1=num1, num2=num2, num3=num3, box=box)
    p2 = '{num4} ` TIMES ` {box} ` = ` {num6}'.format(num4=num4, num6=num6, box=box)
    e2 = '$$수식$${num4} ` TIMES ` {num5} ` = ` {num6}$$/수식$$이므로 $$수식$${box} ` = ` {num5}$$/수식$$입니다.' \
        .format(num4=num4, num5=num5, num6=num6, box=box)
    p3 = '{box} ` TIMES ` {num8} ` = ` {num9}'.format(num8=num8, num9=num9, box=box)
    e3 = '$$수식$${num7} ` TIMES ` {num8} ` = ` {num9}$$/수식$$이므로 $$수식$${box} ` = ` {num7}$$/수식$$입니다.' \
        .format(num7=num7, num8=num8, num9=num9, box=box)
    p4 = '{box} ` TIMES ` {num11} ` = ` {num12}'.format(num11=num11, num12=num12, box=box)
    e4 = '$$수식$${num10} ` TIMES ` {num11} ` = ` {num12}$$/수식$$이므로 $$수식$${box} ` = ` {num10}$$/수식$$입니다.' \
        .format(num10=num10, num11=num11, num12=num12, box=box)

    tmp_lst = [[p1, e1, num2], [p2, e2, num5], [p3, e3, num7], [p4, e4, num10]]
    random.shuffle(tmp_lst)
    problem1, explain1 = tmp_lst[0][0], tmp_lst[0][1]
    problem2, explain2 = tmp_lst[1][0], tmp_lst[1][1]
    problem3, explain3 = tmp_lst[2][0], tmp_lst[2][1]
    problem4, explain4 = tmp_lst[3][0], tmp_lst[3][1]

    tmp = [[tmp_lst[0][2], '㉠'], [tmp_lst[1][2], '㉡'], [tmp_lst[2][2], '㉢'], [tmp_lst[3][2], '㉣']]
    tmp.sort(key=lambda x: x[0], reverse=True)

    explain5 = '{0} $$수식$$&gt;$$/수식$$ {1} $$수식$$&gt;$$/수식$$ {2} $$수식$$&gt;$$/수식$$ {3}'.format(tmp[0][1], tmp[1][1], tmp[2][1], tmp[3][1])
    answer_lst = '{0}, {1}, {2}, {3}'.format(tmp[0][1], tmp[1][1], tmp[2][1], tmp[3][1])

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, problem4=problem4, box=box)
    answer = answer.format(answer_lst=answer_lst)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3,
                             explain4=explain4, explain5=explain5)

    return stem, answer, comment





























# 2-1-6-22
def multiplication216_Stem_009():
    stem = "㉠과 ㉡에 알맞은 수의 {problem} 구해 보세요.\n$$표$${problem1}\n{problem2}$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "• {explain1}\n" \
              "• {explain2}\n" \
              "따라서 {explain3}$$수식$${explain4}$$/수식$$입니다.\n\n"

    problem = random.choice(['합을', '차를'])

    while 1:
        num1 = random.randint(2, 9)
        num2, num3 = random.sample(range(2, 10), 2)
        num4, num5 = num1 * num2, num1 * num3
        if problem == '합을':
            if num2 + num5 < 100:
                break
        else:
            break

    p1 = '$$수식$${num1}$$/수식$$의 {sign}배는 $$수식$${num4}$$/수식$$입니다.'
    e1 = '$$수식$${num1} ` TIMES ` {num2} ` = ` {num4}$$/수식$$이므로 {sign}$$수식$$` = ` {num2}$$/수식$$'

    p2 = '$$수식$${num1}$$/수식$$의 $$수식$${num3}$$/수식$$배는 {sign}입니다.'
    e2 = '$$수식$${num1} ` TIMES ` {num3} ` = ` {num5}$$/수식$$이므로 {sign}$$수식$$` = ` {num5}$$/수식$$'

    tmp_lst = [[p1, e1, num2], [p2, e2, num5]]
    random.shuffle(tmp_lst)
    problem1 = tmp_lst[0][0].format(num1=num1, num3=num3, num4=num4, sign='㉠')
    problem2 = tmp_lst[1][0].format(num1=num1, num3=num3, num4=num4, sign='㉡')
    explain1 = tmp_lst[0][1].format(num1=num1, num2=num2, num3=num3, num4=num4, num5=num5, sign='㉠')
    explain2 = tmp_lst[1][1].format(num1=num1, num2=num2, num3=num3, num4=num4, num5=num5, sign='㉡')

    if problem == '합을':
        answer_num = num2 + num5
        explain3 = '㉠$$수식$$` + `$$/수식$$㉡'
        explain4 = '` = ` {0} ` + ` {1} ` = ` {2}'.format(tmp_lst[0][2], tmp_lst[1][2], answer_num)
    else:
        if tmp_lst[0][2] >= tmp_lst[1][2]:
            answer_num = tmp_lst[0][2] - tmp_lst[1][2]
            explain3 = '㉠$$수식$$` - `$$/수식$$㉡'
            explain4 = '` = ` {0} ` - ` {1} ` = ` {2}'.format(tmp_lst[0][2], tmp_lst[1][2], answer_num)
        else:
            answer_num = tmp_lst[1][2] - tmp_lst[0][2]
            explain3 = '㉡$$수식$$` - `$$/수식$$㉠'
            explain4 = '` = ` {0} ` - ` {1} ` = ` {2}'.format(tmp_lst[1][2], tmp_lst[0][2], answer_num)

    stem = stem.format(problem1=problem1, problem2=problem2, problem=problem)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4)

    return stem, answer, comment































# 2-1-6-23
def multiplication216_Stem_010():
    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 중에서 □안에 들어갈 수 있는 수는 모두 몇 개인가요?\n$$표$${problem1}$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$이므로 $$수식$${explain2}$$/수식$$입니다.\n" \
              "{explain3}이므로 $$수식$${box}$$/수식$$ 안에 들어갈 수 있는 수는 {explain4}로 모두 $$수식$${explain5}$$/수식$$개입니다.\n\n"

    box = '□'

    while 1:
        num3, num4 = random.sample(range(2, 10), 2)
        if abs(num3 - num4) > 1:
            break

    num5 = num3 * num4
    tmp1, tmp2 = num3, num4

    if tmp1 > tmp2:
        tmp1, tmp2 = tmp2, tmp1

    num1 = random.randint(tmp1 + 1, tmp2 - 1)
    num2 = []
    cnt = 1

    while 1:
        if num1 * cnt < num5:
            num2.append(cnt)
        else:
            num2.append(cnt)
            break
        cnt += 1

    problem1 = '$$수식$${num1} ` TIMES ` {box} ` &lt; ` {num3} ` TIMES ` {num4}$$/수식$$'\
        .format(num1=num1, num3=num3, num4=num4, box=box)
    explain1 = '{num3} ` TIMES ` {num4} ` = ` {num5}'.format(num3=num3, num4=num4, num5=num5)
    explain2 = '{num1} ` TIMES ` {box} ` &lt; ` {num5}'.format(num1=num1, num5=num5, box=box)
    explain3 = ''

    for i in num2:
        explain3 += '$$수식$${0} ` TIMES ` {1} ` = ` {2}$$/수식$$, '.format(num1, i, num1 * i)

    explain3 = explain3[:-2]

    num2 = num2[0:-1]
    explain4 = '$$수식$$'
    explain4 += '$$/수식$$, $$수식$$'.join([str(i) for i in num2])
    explain4 += '$$/수식$$'

    if num2[-1] in [3, 6]:
        explain4 += '으'

    answer_num = len(num2)

    stem = stem.format(problem1=problem1, box=box)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3,
                             explain4=explain4, explain5=answer_num, box=box)

    return stem, answer, comment

































# 2-1-6-25
def multiplication216_Stem_011():
    stem = "숫자 카드 중에서 $$수식$$2$$/수식$$장을 뽑아 두 수의 곱을 구할 때, {problem1}과 {problem2}의 {problem4} 구해 보세요.\n{problem3}\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "수의 크기를 비교하면 $$수식$${explain1}$$/수식$$이므로 {problem1}은 $$수식$${explain2}$$/수식$$이고, " \
              "{problem2}은 $$수식$${explain3}$$/수식$$입니다.\n" \
              "→ $$수식$${explain4}$$/수식$$\n\n"

    num1, num2, num3, num4 = random.sample(range(2, 10), 4)
    problem1, problem2 = random.choice([['가장 큰 곱', '가장 작은 곱'], ['가장 큰 곱', '두 번째로 작은 곱'],
                                        ['가장 큰 곱', '세 번째로 작은 곱'],
                                        ['두 번째로 작은 곱', '가장 작은 곱'], ['세 번째로 작은 곱', '두 번째로 작은 곱'],
                                        ['세 번째로 작은 곱', '가장 작은 곱']])

    problem3 = "$$수식$$BOX{``%d``}$$/수식$$  $$수식$$BOX{``%d``}$$/수식$$  " \
               "$$수식$$BOX{``%d``}$$/수식$$  $$수식$$BOX{``%d``}$$/수식$$" % (num1, num2, num3, num4)

    problem4 = random.choice(['합을', '차를'])

    lst = [num1, num2, num3, num4]
    lst.sort(reverse=True)

    explain1 = '{0} ` &gt; ` {1} ` &gt; ` {2} ` &gt; ` {3}'.format(lst[0], lst[1], lst[2], lst[3])
    if problem1 == '가장 큰 곱':
        num5 = lst[0] * lst[1]
        explain2 = '{0} ` TIMES ` {1} ` = ` {2}'.format(lst[0], lst[1], num5)
    elif problem1 == '두 번째로 작은 곱':
        num5 = lst[1] * lst[3]
        explain2 = '{0} ` TIMES ` {1} ` = ` {2}'.format(lst[1], lst[3], num5)
    else:
        num5 = lst[0] * lst[3]
        explain2 = '{0} ` TIMES ` {1} ` = ` {2}'.format(lst[0], lst[3], num5)

    if problem2 == '가장 작은 곱':
        num6 = lst[2] * lst[3]
        explain3 = '{0} ` TIMES ` {1} ` = ` {2}'.format(lst[2], lst[3], num6)
    elif problem2 == '두 번째로 작은 곱':
        num6 = lst[1] * lst[3]
        explain3 = '{0} ` TIMES ` {1} ` = ` {2}'.format(lst[1], lst[3], num6)
    else:
        num6 = lst[0] * lst[3]
        explain3 = '{0} ` TIMES ` {1} ` = ` {2}'.format(lst[0], lst[3], num6)

    if problem4 == '합을':
        answer_num = num5 + num6
        explain4 = '{0} ` + ` {1} ` = ` {2}'.format(num5, num6, answer_num)
    else:
        answer_num = num5 - num6
        explain4 = '{0} ` - ` {1} ` = ` {2}'.format(num5, num6, answer_num)

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, problem4=problem4)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3,
                             explain4=explain4, problem1=problem1, problem2=problem2)

    return stem, answer, comment




# if __name__ == '__main__':
#     Multiplication_Stem_001()
#     Multiplication_Stem_002()
#     Multiplication_Stem_003()
#     Multiplication_Stem_004()
#     Multiplication_Stem_005()
#     Multiplication_Stem_006()
#     Multiplication_Stem_007()
#     Multiplication_Stem_008()
#     Multiplication_Stem_009()
#     Multiplication_Stem_010()
#     Multiplication_Stem_011()


