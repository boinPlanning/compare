import random
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





















# 2-2-3-02
def measuringlen223_Stem_001():
    stem = "알맞은 수를 찾아 $$수식$${boxblank}$$/수식$$ 안에 알맞은 수를 써넣으세요.\n$$표$$$$수식$$1$$/수식$$    $$수식$$10$$/수식$$    $$수식$$100$$/수식$$    $$수식$$1000$$/수식$$$$/표$$\n$$수식$${problem1}$$/수식$$는 $$수식$${problem2}$$/수식$$를 $$수식$${boxblank}$$/수식$$번 이은 것과 같습니다.\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$10$$/수식$$이 $$수식$$10$$/수식$$개이면 $$수식$$100$$/수식$$이고 " \
              "$$수식$$1 ` rm m ` = ` 100 ` rm cm$$/수식$$이므로 $$수식$${explain1}$$/수식$$는 $$수식$${explain2}$$/수식$$를 " \
              "$$수식$${explain3}$$/수식$$번 이은 것과 같습니다.\n\n"

    num1 = random.randint(1, 9)
    num2 = random.choice([1, 10, 100])
    num3 = 100 // num2
    num2 = num1 * num2

    boxblank = "□"

    problem1 = '{0} ` rm m'.format(num1)
    problem2 = '{0} ` rm cm'.format(num2)
    explain1 = problem1
    explain2 = problem2
    explain3 = num3
    answer_num = num3

    stem = stem.format(problem1=problem1, problem2=problem2, boxblank=boxblank)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3)

    return stem, answer, comment























# 2-2-3-03
def measuringlen223_Stem_002():
    stem = "$$수식$${problem}$$/수식$$ 단위를 사용하여 나타내기에 알맞은 것을 모두 찾아 기호를 써 보세요.\n$$표$$㉠ {problem1}    ㉡ {problem2}\n㉢ {problem3}    ㉣ {problem4}$$/표$$\n"
    answer = "(정답)\n{answer_lst}\n"
    comment = "(해설)\n" \
              "$$수식$$1 ` rm m$$/수식$$보다 짧은 것은 {explain1}이고, " \
              "$$수식$$1 ` rm m$$/수식$$보다 큰 것은 {explain2}입니다.\n" \
              "따라서 $$수식$${explain3}$$/수식$$ 단위를 사용하여 나타내기에 알맞은 것은 {explain4} 입니다.\n\n"

    centimeter = ['연필의 길이', '발의 길이', '손가락의 길이', '물병의 높이', '필통의 길이', ]
    meter = ['건물의 높이', '버스의 길이', '기린의 키', '비행기의 길이']

    problem = random.choice(['rm m', 'rm cm'])
    sign_lst = ['㉠', '㉡', '㉢', '㉣']
    centi_cnt, meter_cnt = random.choice([[1, 3], [2, 2], [3, 1]])
    centi_lst = random.sample(centimeter, centi_cnt)
    meter_lst = random.sample(meter, meter_cnt)

    lst = []
    for i in centi_lst:
        lst.append(i)
    for i in meter_lst:
        lst.append(i)
    random.shuffle(lst)

    problem1, problem2, problem3, problem4 = lst

    explain_centi = []
    explain_meter = []
    answer_lst = []

    for idx, i in enumerate(lst):
        if i in centi_lst:
            explain_centi.append(i)
            if problem == 'rm cm':
                answer_lst.append(sign_lst[idx])
        else:
            explain_meter.append(i)
            if problem == 'rm m':
                answer_lst.append(sign_lst[idx])

    explain1 = ', '.join(explain_centi)
    explain2 = ', '.join(explain_meter)
    explain3 = problem
    explain4 = ', '.join(answer_lst)

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, problem4=problem4,
                       problem=problem)
    answer = answer.format(answer_lst=explain4)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4)

    return stem, answer, comment
























# 2-2-3-04
def measuringlen223_Stem_003():
    stem = "$$수식$${boxblank}$$/수식$$ 안에 알맞은 수를 써넣으세요.\n(1) {problem1}\n(2) {problem2}\n"
    answer = "(정답)\n{answer_lst}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( ` 1 ` RIGHT ) ```` {explain1}$$/수식$$\n" \
              "$$수식$${explain2}$$/수식$$\n" \
              "$$수식$${explain3}$$/수식$$\n" \
              "$$수식$$LEFT ( ` 2 ` RIGHT ) ```` {explain4}$$/수식$$\n" \
              "$$수식$${explain5}$$/수식$$\n" \
              "$$수식$${explain6}$$/수식$$\n\n"

    boxblank = "□"

    while 1:
        num1, num2 = random.sample(range(101, 1000), 2)
        if str(num1)[1] == '0' and str(num1)[-1] == '0':
            continue
        if str(num2)[1] == '0' and str(num2)[-1] == '0':
            continue
        break

    num1_1, num1_2 = str(num1)[0], str(num1)[1:3]
    num2_1, num2_2 = str(num2)[0], str(num2)[1:3]

    boxone = "Box{`①`}"
    boxtwo = "Box{`②`}"
    boxthree = "Box{`③`}"


    problem1 = '$$수식$${num1}$$/수식$$ $$수식$$rm cm ` = `$$/수식$$$$수식$${boxone}$$/수식$$ $$수식$$rm m$$/수식$$ $$수식$${boxtwo}$$/수식$$ $$수식$$rm cm$$/수식$$'.format(num1=num1, boxone=boxone, boxtwo=boxtwo)
    problem2 = '$$수식$${num2_1} ` rm m ` {num2_2} ` rm cm ` =$$/수식$$ $$수식$${boxthree}$$/수식$$ $$수식$$rm cm$$/수식$$'.format(
        num2_1=int(num2_1), num2_2=int(num2_2), boxthree=boxthree)

    explain1 = '{0} ` rm cm ` = ` {1} ` rm cm ` + ` {2} ` rm cm'.format(num1, int(num1_1) * 100, int(num1_2))
    explain2 = '= ` {0} ` rm m ` + ` {1} ` rm cm'.format(num1_1, int(num1_2))
    explain3 = '= ` {0} ` rm m ` {1} ` rm cm'.format(num1_1, int(num1_2))

    explain4 = '{0} ` rm m ` {1} ` rm cm ` = ` {0} ` rm m ` + ` {1} ` rm cm'.format(num2_1, int(num2_2))
    explain5 = '= ` {0} ` rm cm ` + ` {1} ` rm cm'.format(int(num2_1) * 100, int(num2_2))
    explain6 = '= ` {0} ` rm cm'.format(num2)
    answer_lst = '$$수식$${0}$$/수식$$, $$수식$${1}$$/수식$$, $$수식$${2}$$/수식$$'.format(num1_1, int(num1_2), num2)

    stem = stem.format(problem1=problem1, problem2=problem2, boxblank=boxblank)
    answer = answer.format(answer_lst=answer_lst)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             explain5=explain5, explain6=explain6)

    return stem, answer, comment

























# 2-2-3-05
def measuringlen223_Stem_004():
    stem = "다음 중 길이가 가장 {problem} 것은 어느 것인가요?\n① $$수식$${p1}$$/수식$$\n② $$수식$${p2}$$/수식$$\n③ $$수식$${p3}$$/수식$$\n④ $$수식$${p4}$$/수식$$\n⑤ $$수식$${p5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}\n"
    comment = "(해설)\n" \
              "{explain1}" \
              "따라서 $$수식$${explain2}$$/수식$$이므로 가장 {problem} 것은 {answer_num}입니다.\n\n"

    sign_lst = ['①', '②', '③', '④', '⑤']
    problem = random.choice(['짧은', '긴'])
    num_lst = random.sample(range(100, 1000), 5)

    rand_num = random.randint(2, 3)
    lst = []

    for idx, val in enumerate(num_lst):
        if idx < rand_num:
            lst.append(['{0} ` rm cm'.format(val), 0, val])
        else:
            lst.append(['{0} ` rm m ` {1} ` rm cm'.format(str(val)[0], int(str(val)[1:3])) if int(str(val)[1:3]) != 0
                        else '{0} ` rm m'.format(str(val)[0]), 1, val])

    random.shuffle(lst)
    p1, p2, p3, p4, p5 = lst[0][0], lst[1][0], lst[2][0], lst[3][0], lst[4][0]
    explain1 = ''

    for idx, val in enumerate(lst):
        lst[idx].append(sign_lst[idx])
        if val[1] == 1:
            explain1 += '{0} $$수식$${1} ` = ` {2} ` rm cm$$/수식$$\n'.format(sign_lst[idx], val[0], val[2])

    if problem == '짧은':
        lst.sort(key=lambda x: x[2], reverse=True)
        explain2 = '{0} ` rm cm ` &gt; ` {1} ` rm cm ` &gt; ` {2} ` rm cm ` &gt; ` {3} ` rm cm ` &gt; ` {4} ` rm cm'\
            .format(lst[0][2], lst[1][2], lst[2][2], lst[3][2], lst[4][2])
    else:
        lst.sort(key=lambda x: x[2])
        explain2 = '{0} ` rm cm ` &lt; ` {1} ` rm cm ` &lt; ` {2} ` rm cm ` &lt; ` {3} ` rm cm ` &lt; ` {4} ` rm cm' \
            .format(lst[0][2], lst[1][2], lst[2][2], lst[3][2], lst[4][2])
    answer_num = lst[4][3]

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, problem=problem)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, problem=problem, answer_num=answer_num)

    return stem, answer, comment


































# 2-2-3-06
def measuringlen223_Stem_005():
    stem = "길이가 $$수식$$1`rm cm$$/수식$$인 {problem}{j1} 겹치는 부분 없이 한 줄로 $$수식$${problem1}$$/수식$$개 이으면 전체 길이는 몇 $$수식$$rm m$$/수식$$가 되나요?\n"
    answer = "(정답)\n$$수식$${answer_num}`rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$1`rm cm$$/수식$$를 $$수식$$100$$/수식$$개 이으면 $$수식$$100`rm cm$$/수식$$이므로 " \
              "$$수식$$1`rm m$$/수식$$입니다.\n" \
              "$$수식$${explain1}$$/수식$$이므로 전체 길이는 $$수식$${explain2}$$/수식$$가 됩니다.\n\n"

    problem = random.choice(['테이프', '종이', '지우개', '연필심', '나무조각'])

    j1 = '를' if josa_check(problem[-1]) == ' ' else '을'
    num = random.randint(1, 9)
    problem1 = num * 100
    explain1 = '{0} ` rm cm ` = ` {1} ` rm m'.format(problem1, num)
    explain2 = '{0} ` rm m'.format(num)
    answer_num = num

    stem = stem.format(problem=problem, problem1=problem1, j1=j1)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2)

    return stem, answer, comment



































# 2-2-3-07
def measuringlen223_Stem_006():
    stem = "길이를 잘못 나타낸 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$\n㉡ $$수식$${problem2}$$/수식$$\n㉢ $$수식$${problem3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{answer_num}\n"
    comment = "(해설) $$수식$${explain1}$$/수식$$이므로\n" \
              "$$수식$${explain2}$$/수식$$\n" \
              "$$수식$${explain3}$$/수식$$\n" \
              "$$수식$${explain4}$$/수식$$\n" \
              "따라서 길이를 잘못 나타낸 것은 {explain5}입니다.\n\n"

    sign = ['㉠', '㉡', '㉢']
    num1, num2, num3 = random.sample(range(1, 10), 3)
    num1 = num1 * 100 + num2 * 10 + num3
    num4, num5 = random.sample(range(1, 10), 2)
    num6, num7 = random.sample(range(1, 10), 2)
    num2 = num4 * 100 + num6
    num3 = num5 * 100 + num7

    lst = [['{0}` rm m ` {1} ` rm cm ` = ` {2} ` rm cm'.format(num1 // 100, num1 % 100, num1), 0],
           ['{0} ` rm m ` {1} ` rm cm ` = ` {2} ` rm cm'.format(num2 // 100, num2 % 100, num4 * 10 + num6), 1],
           ['{0} ` rm cm ` = ` {1} ` rm m ` {2} ` rm cm'.format(num3, num3 // 100, num3 % 100), 0]]
    random.shuffle(lst)

    problem1, problem2, problem3 = lst[0][0], lst[1][0], lst[2][0]
    for idx, val in enumerate(lst):
        if val[1] == 1:
            answer_num = sign[idx]
    explain1 = '{0} ` rm m ` = ` {1} ` rm cm'.format(num4, num4 * 100)
    explain2 = '{0} ` rm m ` {1} ` rm cm ` = ` {0} ` rm m ` + ` {1} ` rm cm'.format(num4, num6)
    explain3 = '= ` {0} `rm cm ` + ` {1} ` rm cm'.format(num4 * 100, num6)
    explain4 = '= ` {0} ` rm cm'.format(num2)
    explain5 = answer_num

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             explain5=explain5)

    return stem, answer, comment




































# 2-2-3-11
def measuringlen223_Stem_007():
    stem = "가장 긴 길이와 가장 짧은 길이의 {problem}{prob_j1} 몇 $$수식$$rm m$$/수식$$ 몇 $$수식$$rm cm$$/수식$$인가요?\n$$표$$㉠ $$수식$${problem1}$$/수식$$    ㉡ $$수식$${problem2}$$/수식$$    ㉢ $$수식$${problem3}$$/수식$$$$/표$$\n"\
        "{boxblank} $$수식$$rm m$$/수식$$ {boxblank} $$수식$$rm cm$$/수식$$"
    answer = "(정답)\n{answer_txt}\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$이므로\n" \
              "가장 긴 길이 : $$수식$${explain2}$$/수식$$\n" \
              "가장 짧은 길이 : $$수식$${explain3}$$/수식$$\n" \
              "→ $$수식$${explain4}$$/수식$$\n\n"

    problem = random.choice(['합', '차'])
    prob_j1 = '는' if josa_check(problem[-1]) == ' ' else '은'
    while 1:
        num1, num2, num3 = random.sample(range(101, 1000), 3)
        if str(num1)[-1] == '0' and str(num2)[-1] == '0' and str(num3)[-1] == '0':
            continue
        num_lst = [num1, num2, num3]
        if problem == '합':
            added = max(num_lst) + min(num_lst)
            if added < 1000 and str(added)[1:3] != '00':
                break
        else:
            added = max(num_lst) - min(num_lst)
            if 100 < added and str(added)[1:3] != '00' and int(str(max(num_lst))[1:3]) > int(str(min(num_lst))[1:3]):
                break

    rand_lst = [0, 0, 1]
    random.shuffle(rand_lst)
    problem_lst = []

    for idx, val in enumerate(num_lst):
        if rand_lst[idx] == 1:
            problem_lst.append('{0} ` rm cm'.format(val))
            explain1 = '{0} ` rm cm ` = ` {1} ` rm m ` {2} ` rm cm'.format(val, str(val)[0], int(str(val)[1:3]))
        else:
            problem_lst.append('{0} ` rm m ` {1} ` rm cm'.format(str(val)[0], int(str(val)[1:3])))

    problem1, problem2, problem3 = problem_lst
    explain2 = '{0} ` rm m ` {1} ` rm cm'.format(str(max(num_lst))[0], int(str(max(num_lst))[1:3]))
    explain3 = '{0} ` rm m ` {1} ` rm cm'.format(str(min(num_lst))[0], int(str(min(num_lst))[1:3]))
    if problem == '합':
        explain4 = '{0} ` + ` {1} ` = ` {2} ` rm m ` {3} ` rm cm'\
            .format(explain2, explain3, str(added)[0], int(str(added)[1:3]))
    else:
        explain4 = '{0} ` - ` {1} ` = ` {2} ` rm m ` {3} ` rm cm' \
            .format(explain2, explain3, str(added)[0], int(str(added)[1:3]))
    answer_txt = '$$수식$${0}$$/수식$$, $$수식$${1}$$/수식$$'.format(str(added)[0], int(str(added)[1:3]))

    boxblank = "$$수식$$box{　　　}$$/수식$$"
    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, problem=problem, prob_j1=prob_j1, boxblank=boxblank)
    answer = answer.format(answer_txt=answer_txt)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4)

    return stem, answer, comment


































# 2-2-3-12
def measuringlen223_Stem_008():
    stem = "긴 끈의 길이는 $$수식$${problem1}$$/수식$$이고, 짧은 끈의 길이는 $$수식$${problem2}$$/수식$$입니다. 두 끈의 길이의 {problem} 몇 $$수식$$rm m$$/수식$$ 몇 $$수식$$rm cm$$/수식$$인가요?\n"\
        "{boxblank} $$수식$$rm m$$/수식$$ {boxblank} $$수식$$rm cm$$/수식$$"
    answer = "(정답)\n{answer_txt}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$두 끈의 길이의 {problem}$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${explain1}$$/수식$$\n" \
              "$$수식$${explain2}$$/수식$$\n\n"

    while 1:
        num1 = random.randint(10, 15)
        num2 = random.randint(1, 99)
        num3 = random.randint(1, 5)
        num4 = random.randint(1, 99)
        if num2 + num4 < 100 and num2 - num4 > 0:
            break

    problem_1, problem_2 = random.choice([['합은', '합'], ['차는', '차']])
    problem1 = '{0} ` rm m ` {1} ` rm cm'.format(num1, num2)
    problem2 = '{0} ` rm m ` {1} ` rm cm'.format(num3, num4)

    if problem_2 == '합':
        explain1 = '= ` {0} ` + ` {1}'.format(problem1, problem2)
        num5, num6 = num1 + num3, num2 + num4
    else:
        explain1 = '= ` {0} ` - ` {1}'.format(problem1, problem2)
        num5, num6 = num1 - num3, num2 - num4

    explain2 = '= ` {0} ` rm m ` {1} ` rm cm'.format(num5, num6)
    
    answer_txt = '$$수식$${0}$$/수식$$, $$수식$${1}$$/수식$$'.format(num5, num6)

    boxblank = "$$수식$$box{　　　}$$/수식$$"

    stem = stem.format(problem1=problem1, problem2=problem2, problem=problem_1, boxblank=boxblank)
    answer = answer.format(answer_txt=answer_txt)
    comment = comment.format(explain1=explain1, explain2=explain2, problem=problem_2)

    return stem, answer, comment


































# 2-2-3-13
def measuringlen223_Stem_009():
    stem = "두 길이의 {problem}{prob_j1} 몇 $$수식$$rm m$$/수식$$ 몇 $$수식$$rm cm$$/수식$$인가요?\n$$표$$$$수식$${problem1}$$/수식$$    $$수식$${problem2}$$/수식$$$$/표$$\n"\
        "{boxblank} $$수식$$rm m$$/수식$$ {boxblank} $$수식$$rm cm$$/수식$$"
    answer = "(정답)\n{answer_txt}\n"
    comment = "(해설)\n" \
              "{explain1}\n" \
              "$$수식$${explain2}$$/수식$$\n" \
              "$$수식$${explain3}$$/수식$$\n" \
              "$$수식$${explain4}$$/수식$$\n\n"

    problem = random.choice(['합', '차'])
    prob_j1 = '는' if josa_check(problem[-1]) == ' ' else '은'

    while 1:
        num1, num3 = random.sample(range(1, 10), 2)
        num2 = random.randint(1, 99)
        num4 = random.randint(1, 99)
        if problem == '차':
            if num1 > num3:
                if num2 - num4 > 0:
                    break
            else:
                if num4 - num2 > 0:
                    break
        else:
            if num2 + num4 < 100:
                break

    problem1 = '{0} ` rm m ` {1} ` rm cm'.format(num1, num2)
    problem2 = '{0} ` rm m ` {1} ` rm cm'.format(num3, num4)

    if problem == '차':
        if num1 > num3:
            explain1 = '$$수식$${0} ` rm m ` {1} ` rm cm ` &lt; ` {2} ` rm m ` {3} ` rm cm$$/수식$$'.format(num3, num4, num1, num2)
            explain2 = '= ` {0} ` rm m ` {1} ` rm cm ` - ` {2} ` rm m ` {3} ` rm cm'.format(num1, num2, num3, num4)
            explain3 = '= ` LEFT ( ` {0} ` rm m ` - ` {1} ` rm m ` RIGHT ) ` + ` LEFT ( ` {2} ` rm cm ` - ` {3} ` rm cm ` RIGHT )'\
                .format(num1, num3, num2, num4)
            explain4 = '= ` {0} ` rm m ` {1} ` rm cm'.format(num1 - num3, num2 - num4)
            answer_txt = '$$수식$${0}$$/수식$$, $$수식$${1}$$/수식$$'.format(num1 - num3, num2 - num4)
        else:
            explain1 = '$$수식$${0} ` rm m ` {1} ` rm cm ` &lt; ` {2} ` rm m ` {3} ` rm cm$$/수식$$'.format(num1, num2, num3, num4)
            explain2 = '=` {0} ` rm m ` {1} ` rm cm ` - ` {2} ` rm m ` {3} ` rm cm'.format(num3, num4, num1, num2)
            explain3 = '= ` LEFT ( ` {0} ` rm m ` - ` {1} ` rm m ` RIGHT ) ` + ` LEFT ( ` {2} ` rm cm ` - ` {3} ` rm cm ` RIGHT )' \
                .format(num3, num1, num4, num2)
            explain4 = '= ` {0} ` rm m ` {1} ` rm cm'.format(num3 - num1, num4 - num2)
            answer_txt = '$$수식$${0}$$/수식$$, $$수식$${1}$$/수식$$'.format(num3 - num1, num4 - num2)
    else:
        explain1 = '$$수식$$LEFT ($$/수식$$두 길이의 합$$수식$$RIGHT )$$/수식$$'
        explain2 = '= ` {0} ` rm m ` {1} ` rm cm ` + ` {2} ` rm m ` {3} ` rm cm'.format(num1, num2, num3, num4)
        explain3 = '= ` LEFT ( ` {0} ` rm m ` + ` {1} ` rm m ` RIGHT ) ` + ` LEFT ( ` {2} ` rm cm ` + ` {3} ` rm cm ` RIGHT )' \
            .format(num1, num3, num2, num4)
        explain4 = '= ` {0} ` rm m ` {1} ` rm cm'.format(num1 + num3, num2 + num4)
        answer_txt = '$$수식$${0}$$/수식$$, $$수식$${1}$$/수식$$'.format(num1 + num3, num2 + num4)

    boxblank = "$$수식$$box{　　　}$$/수식$$"
    stem = stem.format(problem1=problem1, problem2=problem2, prob_j1=prob_j1, problem=problem, boxblank=boxblank)
    answer = answer.format(answer_txt=answer_txt)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4)

    return stem, answer, comment


































# 2-2-3-14
def measuringlen223_Stem_010():
    stem = "길이의 차가 가장 {problem} 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${problem1}$$/수식$$\n㉡ $$수식$${problem2}$$/수식$$\n㉢ $$수식$${problem3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{answer_num}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${explain1}$$/수식$$\n" \
              "㉡ $$수식$${explain2}$$/수식$$\n" \
              "㉢ $$수식$${explain3}$$/수식$$\n" \
              "따라서 $$수식$${explain4}$$/수식$$이므로 길이의 차가 가장 {problem} 것은 {answer_num}입니다.\n\n"

    problem = random.choice(['큰', '작은'])
    sign_lst = ['㉠', '㉡', '㉢']

    while 1:
        num1, num3 = random.sample(range(1, 9), 2)
        if num3 > num1:
            num1, num3 = num3, num1
        num2, num4 = random.sample(range(11, 100), 2)
        if num2 % 100 == 0 or num4 % 100 == 0:
            continue
        if num4 > num2:
            num2, num4 = num4, num2

        num5, num7 = random.sample(range(1, 9), 2)
        if num7 > num5:
            num5, num7 = num7, num5
        num6, num8 = random.sample(range(11, 100), 2)
        if num6 % 100 == 0 or num8 % 100 == 0:
            continue
        if num8 > num6:
            num6, num8 = num8, num6

        num9, num11 = random.sample(range(1, 9), 2)
        if num11 > num9:
            num9, num11 = num11, num9
        num10, num12 = random.sample(range(11, 100), 2)
        if num10 % 100 == 0 or num12 % 100 == 0:
            continue
        if num12 > num10:
            num10, num12 = num12, num10

        n1, n2 = num1 - num3, num2 - num4
        n3, n4 = num5 - num7, num6 - num8
        n5, n6 = num9 - num11, num10 - num12
        if n1 * 100 + n2 != n3 * 100 + n4 and n1 * 100 + n2 != n5 * 100 + n6 and n3 * 100 + n4 != n5 * 100 + n6:
            break

    problem1 = '{0} ` rm m ` {1} ` rm cm ` - ` {2} ` rm m ` {3} ` rm cm'.format(num1, num2, num3, num4)
    problem2 = '{0} ` rm m ` {1} ` rm cm ` - ` {2} ` rm m ` {3} ` rm cm'.format(num5, num6, num7, num8)
    problem3 = '{0} ` rm m ` {1} ` rm cm ` - ` {2} ` rm m ` {3} ` rm cm'.format(num9, num10, num11, num12)

    explain1 = '{0} ` = ` {1} ` rm m ` {2} ` rm cm'.format(problem1, n1, n2)
    explain2 = '{0} ` = ` {1} ` rm m ` {2} ` rm cm'.format(problem2, n3, n4)
    explain3 = '{0} ` = ` {1} ` rm m ` {2} ` rm cm'.format(problem3, n5, n6)

    lst = [[n1 * 100 + n2, n1, n2, 0], [n3 * 100 + n4, n3, n4, 1], [n5 * 100 + n6, n5, n6, 2]]
    lst.sort(key=lambda x: x[0], reverse=True)
    explain4 = '{0} ` rm m ` {1} ` rm cm ` &gt; ` {2} ` rm m ` {3} ` rm cm ` &gt; ` {4} ` rm m ` {5} ` rm cm'\
        .format(lst[0][1], lst[0][2], lst[1][1], lst[1][2], lst[2][1], lst[2][2])

    if problem == '큰':
        answer_num = sign_lst[lst[0][3]]
    else:
        answer_num = sign_lst[lst[2][3]]

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, problem=problem)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             answer_num=answer_num, problem=problem)

    return stem, answer, comment
































# 2-2-3-15
def measuringlen223_Stem_011():
    stem = "$$수식$${boxblank}$$/수식$$ 안에 알맞은 수는 얼마인가요?\n$$표$$$$수식$${problem1}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${answer_num}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$ \n" \
              "$$수식$${explain2}$$/수식$$이므로 " \
              "$$수식$${explain3}$$/수식$$\n" \
              "따라서 $$수식$${boxblank}$$/수식$$ 안에 알맞은 수는 $$수식$${explain4}$$/수식$$입니다.\n\n"

    boxblank = "□"

    while 1:
        num1, num2 = random.sample(range(101, 1000), 2)
        if str(num1)[1:3] == '00' or str(num2)[1:3] == '00':
            continue
        if num2 > num1:
            num1, num2 = num2, num1
        num3 = num1 - num2
        if str(num3)[1:3] != '00' and num3 > 100:
            break

    problem1 = '%s ` rm m ` %d ` rm cm ` - ` %s ` rm cm ` = ` %s ` rm m ` %d ` rm cm' % (str(num1)[0], int(str(num1)[1:3]), boxblank, str(num3)[0], int(str(num3)[1:3]))

    explain1 = '%s ` rm cm ` = ` %s ` rm m ` %d ` rm cm ` - ` %s ` rm m ` %d ` rm cm ` = ` %s ` rm m ` %d ` rm cm' \
               % (boxblank, str(num1)[0], int(str(num1)[1:3]), str(num3)[0], int(str(num3)[1:3]), str(num2)[0], int(str(num2)[1:3]))
    explain2 = '{0} ` rm m ` {1} ` rm cm ` = ` {2} ` rm cm'.format(str(num2)[0], int(str(num2)[1:3]), num2)
    explain3 = '%s ` = ` %d' % (boxblank, num2)

    explain4 = num2
    answer_num = num2

    stem = stem.format(problem1=problem1, boxblank=boxblank)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             answer_num=answer_num, boxblank=boxblank)

    return stem, answer, comment




































# 2-2-3-16
def measuringlen223_Stem_012():
    stem = "$$수식$${boxblank}$$/수식$$ 안에 알맞은 수를 써넣으세요.\n{problem1}\n"
    answer = "(정답)\n{answer_lst}\n"
    comment = "(해설)\n" \
              "$$수식$${explain1}$$/수식$$\n" \
              "→ $$수식$${explain2}$$/수식$$\n" \
              "‧ $$수식$$rm cm$$/수식$$ 단위 : $$수식$${explain3}$$/수식$$, $$수식$${explain4}$$/수식$$\n" \
              "‧ $$수식$$rm m$$/수식$$ 단위 : $$수식$${explain5}$$/수식$$, $$수식$${explain6}$$/수식$$\n\n"

    while 1:
        num1, num2 = random.sample(range(101, 1000), 2)
        if str(num1)[1:3] == '00' or str(num2)[1:3] == '00':
            continue
        if int(str(num1)[1:3]) + int(str(num2)[1:3]) >= 100:
            continue
        num3 = num1 + num2
        if str(num3)[1:3] != '00' and num3 < 1000:
            break

    boxblank = "□"
    boxone = "BOX{`①`}"
    boxtwo = "BOX{`②`}"

    problem1 = '$$수식$$%d ` rm cm ` + ` %s ` rm m$$/수식$$ $$수식$$%s$$/수식$$ $$수식$$rm cm ` =$$/수식$$ $$수식$$%s$$/수식$$ $$수식$$rm m ` %d ` rm cm$$/수식$$' % (num1, str(num2)[0], boxone, boxtwo, int(str(num3)[1:3]))
    explain1 = '%d ` rm cm ` + ` %s ` rm m ` %s ` rm cm ` = ` %s ` rm m ` %d ` rm cm' % (num1, str(num2)[0], boxblank, boxblank, int(str(num3)[1:3]))
    explain2 = '%s ` rm m ` %d ` rm cm ` + ` %s ` rm m ` %s ` rm cm ` = ` %s ` rm m ` %d ` rm cm' % (str(num1)[0], int(str(num1)[1:3]), str(num2)[0], boxblank, boxblank, int(str(num3)[1:3]))

    explain3 = '%d ` + ` %s ` = ` %d' % (int(str(num1)[1:3]), boxblank, int(str(num3)[1:3]))
    explain4 = '%s ` = ` %d ` - ` %d ` = ` %d' % (boxblank, int(str(num3)[1:3]), int(str(num1)[1:3]), int(str(num2)[1:3]))
    explain5 = '%s ` + ` %s ` = ` %s' % (str(num1)[0], str(num2)[0], boxblank)
    explain6 = '%s ` = ` %s' % (boxblank, str(num3)[0])

    answer_lst = '$$수식$${0}$$/수식$$, $$수식$${1}$$/수식$$'.format(int(str(num2)[1:3]), str(num3)[0])

    stem = stem.format(problem1=problem1, boxblank=boxblank)
    answer = answer.format(answer_lst=answer_lst)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             explain5=explain5,  explain6=explain6)

    return stem, answer, comment



































# 2-2-3-19
def measuringlen223_Stem_013():
    stem = "{people}{j1}는 높이가 $$수식$${problem1}`rm cm$$/수식$$인 {objects1} 위에 올라가서 {objects1} 바닥부터 머리 끝까지의 길이를 재었더니 $$수식$${problem2}`rm cm$$/수식$$였습니다. 이번에는 {objects2} 위에 올라가서 같은 방법으로 길이를 재었더니 $$수식$${problem3}$$/수식$$였습니다. {objects2}의 높이는 몇 $$수식$$rm cm$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${answer_num}`rm cm$$/수식$$\n"
    comment = "(해설)\n" \
              "({people}{j1}의 키)\n" \
              "$$수식$${explain1}$$/수식$$\n" \
              "→ ({objects2}의 높이)\n" \
              "$$수식$${explain2}$$/수식$$\n" \
              "$$수식$${explain3}$$/수식$$\n" \
              "$$수식$${explain4}$$/수식$$\n\n"

    objects1 = random.choice(['돌', '단상', '상자'])
    objects2 = random.choice(['책상', '의자', '탁자'])
    people = random.choice(person_nam+person_yeo)
    j1 = '' if josa_check(people[-1]) == ' ' else '이'

    while 1:
        people_h = random.randint(130, 160)
        objects1_h = random.randint(10, 40)
        if objects2 == '책상':
            objects2_h = random.randint(50, 90)
        else:
            objects2_h = random.randint(40, 60)
        num1 = people_h + objects1_h
        if str(num1)[1:3] == '00':
            continue
        num2 = people_h + objects2_h
        if int(str(num2)[0]) > 1 and str(num2)[1:3] != '00' and int(str(num2)[1:3]) < int(str(people_h)[1:3]):
            break

    problem1 = objects1_h
    problem2 = num1
    problem3 = '{0} ` rm m ` {1} ` rm cm'.format(str(num2)[0], int(str(num2)[1:3]))

    explain1 = '= ` {0} ` rm m ` {1} ` rm cm ` - ` {2} ` rm cm ` = ` {3} ` rm m ` {4} ` rm cm'\
        .format(str(num1)[0], int(str(num1)[1:3]), objects1_h, str(people_h)[0], int(str(people_h)[1:3]))
    explain2 = '= ` {0} ` rm m ` {1} ` rm cm ` - ` {2} ` rm m ` {3} ` rm cm'\
        .format(str(num2)[0], int(str(num2)[1:3]), str(people_h)[0], int(str(people_h)[1:3]))
    explain3 = '= ` {0} ` rm m ` {1} ` rm cm ` - ` {2} ` rm m ` {3} ` rm cm' \
        .format(int(str(num2)[0]) - 1, int(str(num2)[1:3]) + 100, str(people_h)[0], int(str(people_h)[1:3]))

    explain4 = '= ` {0} ` rm cm'.format(objects2_h)
    answer_num = objects2_h

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3, people=people,
                       objects1=objects1, objects2=objects2, j1=j1)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             people=people, objects2=objects2, j1=j1)

    return stem, answer, comment


































# 2-2-3-20
def measuringlen223_Stem_014():
    stem = "수 카드 $$수식$$4$$/수식$$장 중에서 $$수식$$3$$/수식$$장을 골라 한 번씩만 사용하여 길이를 나타내려고 합니다. 나타낼 수 있는 가장 긴 길이와 가장 짧은 길이의 차는 몇 $$수식$$rm m$$/수식$$ 몇 $$수식$$rm cm$$/수식$$인가요?\n{problem1}\n" \
        "{boxblank} $$수식$$rm m$$/수식$$ {boxblank} $$수식$$rm cm$$/수식$$"
    answer = "(정답)\n$$수식$${answer_lst}$$/수식$$\n"
    comment = "(해설)\n" \
              "나타낼 수 있는 가장 긴 길이는 $$수식$${explain1}$$/수식$$이고 " \
              "나타낼 수 있는 가장 짧은 길이는 $$수식$${explain2}$$/수식$$입니다.\n" \
              "따라서 두 길이의 차는 $$수식$${explain3}$$/수식$$\n\n"

    num1, num2, num3, num4 = random.sample(range(1, 9), 4)
    problem1 = '$$수식$$box{``%d``}$$/수식$$  $$수식$$box{``%d``}$$/수식$$  $$수식$$box{``%d``}$$/수식$$  $$수식$$box{``%d``}$$/수식$$' % (num1, num2, num3, num4)

    lst = [num1, num2, num3, num4]
    lst.sort()
    num1, num2, num3, num4 = lst
    explain1 = '{0} ` rm m ` {1}{2} ` rm cm'.format(num4, num3, num2)
    explain2 = '{0} ` rm m ` {1}{2} ` rm cm'.format(num1, num2, num3)
    num5 = num4 * 100 + num3 * 10 + num2 - (num1 * 100 + num2 * 10 + num3)
    explain3 = '{0} ` rm m ` {1}{2} ` rm cm ` - ` {3} ` rm m ` {4}{5} ` rm cm ` = ` {6} ` rm m ` {7} ` rm cm'\
        .format(num4, num3, num2, num1, num2, num3, str(num5)[0], int(str(num5)[1:3]))
    answer_lst = '{0}$$/수식$$, $$수식$${1}'.format(str(num5)[0], int(str(num5)[1:3]))

    boxblank = "$$수식$$box{　　　}$$/수식$$"
    
    stem = stem.format(problem1=problem1, boxblank=boxblank)
    answer = answer.format(answer_lst=answer_lst)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3)

    return stem, answer, comment


































# 2-2-3-21
def measuringlen223_Stem_015():
    stem = "{people}{j1}의 한 뼘의 길이는 $$수식$${problem1} ` rm cm$$/수식$$입니다. {people}{j1}가 {objects} 짧은 쪽의 길이를 뼘으로 재었더니 약 $$수식$${problem2}$$/수식$$번이었습니다. {objects} 짧은 쪽의 길이는 약 몇 $$수식$$rm cm$$/수식$$인가요?\n"
    answer = "(정답)\n약 $$수식$${answer_num} ` rm cm$$/수식$$\n"
    comment = "(해설)\n" \
              "{objects} 짧은 쪽의 길이는 $$수식$${explain1} ` rm cm$$/수식$$가 약 $$수식$${explain2}$$/수식$$번입니다.\n" \
              "→ $$수식$${explain3} ` LEFT ( ` rm cm ` RIGHT )$$/수식$$\n" \
              "따라서 {objects} 짧은 쪽의 길이는 약 $$수식$${explain4} ` rm cm$$/수식$$입니다.\n\n"

    objects = random.choice(['책상', '탁상', '선반', '식탁'])
    people = random.choice(person_nam+person_yeo)
    j1 = '' if josa_check(people[-1]) == ' ' else '이'

    while 1:
        num1 = random.randint(10, 16)
        num2 = random.randint(3, 7)
        num3 = num1 * num2
        if num3 < 100:
            break

    problem1, problem2 = num1, num2
    explain1, explain2 = num1, num2

    explain3 = ' ` + ` '.join([str(num1) for i in range(num2)])
    explain3 += ' ` = ` {0}'.format(num3)

    explain4 = num3
    answer_num = num3

    stem = stem.format(problem1=problem1, problem2=problem2, people=people, objects=objects, j1=j1)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             objects=objects)

    return stem, answer, comment







































# 2-2-3-22
def measuringlen223_Stem_016():
    stem = "길이가 $$수식$${problem1}$$/수식$$인 {objects}{j3} 보고 {people1}{j1}와 {people2}{j2}가 어림한 것입니다. 실제 길이에 더 가깝게 어림한 사람은 누구인가요?\n$$표$$$$수식$$LEFT [$$/수식$${people1}$$수식$$RIGHT ]$$/수식$$ 약 $$수식$${problem2}$$/수식$$야.\n$$수식$$LEFT [$$/수식$${people2}$$수식$$RIGHT ]$$/수식$$ $$수식$${problem3}$$/수식$$ 정도 되는 것 같아.$$/표$$\n"
    answer = "(정답)\n{answer_num}\n"
    comment = "(해설)\n" \
              "어림한 길이와 $$수식$${explain1}$$/수식$$의 차를 각각 구하면\n" \
              "{people1} : $$수식$${explain2}$$/수식$$\n" \
              "{people2} : $$수식$${explain3}$$/수식$$\n" \
              "따라서 $$수식$${explain4}$$/수식$$이므로 실제 길이에 더 가깝게 어림한 사람은 {answer_num}입니다.\n\n"

    objects = random.choice(['테이프', '붕대', '밧줄', '줄자'])
    j3 = '를' if josa_check(objects[-1]) == ' ' else '을'
    terms = [random.choice(person_nam), random.choice(person_yeo)]
    random.shuffle(terms)
    people1, people2 = terms

    j1 = '' if josa_check(people1[-1]) == ' ' else '이'
    j2 = '' if josa_check(people2[-1]) == ' ' else '이'

    while 1:
        num1 = random.randint(101, 250)
        if num1 == 200:
            continue
        num2, num3 = random.sample(range(1, 20), 2)
        num2, num3 = num2 * random.choice([1, -1]), num3 * random.choice([1, -1])
        num4, num5 = num1 + num2, num1 + num3
        if num4 > 100 and num5 > 100:
            break

    problem1 = '{0} ` rm m ` {1} ` rm cm'.format(str(num1)[0], int(str(num1)[1:3]))
    problem2 = '{0} ` rm m ` {1} ` rm cm'.format(str(num4)[0], int(str(num4)[1:3]))
    problem3 = '{0} ` rm m ` {1} ` rm cm'.format(str(num5)[0], int(str(num5)[1:3]))
    explain1 = problem1
    explain2 = '{0} ` - ` {1} ` = ` {2} ` rm cm'.format(problem2, problem1, abs(num2))
    explain3 = '{0} ` - ` {1} ` = ` {2} ` rm cm'.format(problem3, problem1, abs(num3))

    if abs(num2) > abs(num3):
        explain4 = '{0} ` rm cm ` &gt; ` {1} ` rm cm'.format(abs(num2), abs(num3))
        answer_num = people2
    else:
        explain4 = '{0} ` rm cm ` &gt; ` {1} ` rm cm'.format(abs(num3), abs(num2))
        answer_num = people1

    stem = stem.format(problem1=problem1, problem2=problem2, problem3=problem3,
                       people1=people1, people2=people2, objects=objects, j1=j1, j2=j2, j3=j3)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(explain1=explain1, explain2=explain2, explain3=explain3, explain4=explain4,
                             answer_num=answer_num, people1=people1, people2=people2)

    return stem, answer, comment










# if __name__ == '__main__':
#     MeasureLength_Stem_001()
#     MeasureLength_Stem_002()
#     MeasureLength_Stem_003()
#     MeasureLength_Stem_004()
#     MeasureLength_Stem_005()
#     MeasureLength_Stem_006()
#     MeasureLength_Stem_007()
#     MeasureLength_Stem_008()
#     MeasureLength_Stem_009()
#     MeasureLength_Stem_010()
#     MeasureLength_Stem_011()
#     MeasureLength_Stem_012()
#     MeasureLength_Stem_013()
#     MeasureLength_Stem_014()
#     MeasureLength_Stem_015()
#     MeasureLength_Stem_016()







