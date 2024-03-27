import numpy as np
import codecs
import os


PATH = '/home/boin-service/Visang/Dictionary/'

person_nam = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XY.txt'), 'r', 'utf-8').readlines()]
person_yeo = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XX.txt'), 'r', 'utf-8').readlines()]
city_name = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_city.txt'), 'r', 'utf-8').readlines()]


month_date_dict = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
week_idx_dict = {0 : '일', 1 : '월', 2 : '화', 3 : '수', 4 : '목', 5 : '금', 6 : '토'}
week_name = '일월화수목금토'

multiple_choice_nums = {0 : '①', 1 : '②', 2 : '③', 3 : '④', 4 : '⑤'}
multiple_choice_jaum = {0 : '㉠', 1 : '㉡', 2 : '㉢', 3 : '㉣'}

have_jongsung_num = [0, 1, 3, 6, 7, 8]


def josa_check(name):
    JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                     'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    char_code = ord(name) - 44032
    ch1 = int(char_code / 588)
    ch2 = int((char_code - (588 * ch1)) / 28)
    ch3 = int((char_code - (588 * ch1) - (28 * ch2)))

    return JONGSUNG_LIST[ch3]








# 2-2-4-03
def timeandhour224_Stem_001() :
    stem = "$$수식$${box}$$/수식$$ 안에 알맞은 수나 말을 써넣어 $$수식$${s1}$$/수식$$시 $$수식$${s5}$$/수식$$분을 설명해 보세요.\n$$표$$시계의 $$수식$${box_1}$$/수식$$바늘이 $$수식$${box_2}$$/수식$${j1} $$수식$${box_3}$$/수식$$ 사이에 있고, $$수식$${box_4}$$/수식$$ 바늘이 $$수식$${box_5}$$/수식$${j2} 가리키면 $$수식$${s1}$$/수식$$시 $$수식$${s5}$$/수식$$분입니다.$$/표$$\n"
    answer = "(정답)\n{t1}, $$수식$${s3}$$/수식$$, $$수식$${s4}$$/수식$$, {t2}, $$수식$${s2}$$/수식$$\n"
    comment = "(해설)\n" \
              "시계의 짧은 바늘과 긴바늘의 위치와 시계의 수 사이의 관계를 알아보면 \n" \
              "시계의 짧은 바늘이 $$수식$${s3}$$/수식$${j1} $$수식$${s4}$$/수식$$ 사이에 있으면 $$수식$${s1}$$/수식$$시이고, " \
              "긴 바늘이 $$수식$${s2}$$/수식$${j2} 가리키면 $$수식$${s5}$$/수식$$분입니다.\n\n"

    box = '□'
    box_1 = 'box{~①~}'
    box_2 = 'box{~②~}'
    box_3 = 'box{~③~}'
    box_4 = 'box{~④~}'
    box_5 = 'box{~⑤~}'

    s1 = np.random.randint(2, 12, 1)[0]
    s2 = np.random.randint(1, 12, 1)[0]

    s3 = s1 - 1
    s4 = s1 + 1
    s5 = s2 * 5

    j1 = '과' if s3 % 10 in have_jongsung_num else '와'
    j2 = '을' if s2 % 10 in have_jongsung_num else '를'
    t1, t2 = '짧은', '긴'

    stem = stem.format(box=box, box_1=box_1, box_2=box_2, box_3=box_3, box_4=box_4, box_5=box_5, s1=s1, s5=s5, j1=j1, j2=j2)
    answer = answer.format(t1=t1, t2=t2, s3=s3, s4=s4, s2=s2)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, j1=j1, j2=j2)

    return stem, answer, comment





















# 2-2-4-05
def timeandhour224_Stem_002():
    stem = "시계가 나타내는 시각은 몇 시 몇 분인가요?\n$$표$$∙ 시계의 짧은 바늘은 $$수식$${s2}$$/수식$${j1} $$수식$${s3}$$/수식$$ 사이를 가리킵니다.\n∙ 시계의 긴 바늘은 $$수식$${s4}$$/수식$$에서 작은 눈금으로 $$수식$${s5}$$/수식$$칸 더 간 곳을 가리킵니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${s1}$$/수식$$시 $$수식$${s6}$$/수식$$분\n"
    comment = "(해설)\n" \
              "시계의 짧은 바늘은 $$수식$${s2}$$/수식$${j1} $$수식$${s3}$$/수식$$ 사이를 가리키고, 긴 바늘은 $$수식$${s4}$$/수식$$에서 작은 눈금으로 " \
              "$$수식$${s5}$$/수식$$칸 더 간 곳을 가리키므로 $$수식$${s1}$$/수식$$시 $$수식$${s6}$$/수식$$분입니다.\n\n"

    s1 = np.random.randint(2, 11, 1)[0]
    s2 = s1 - 1
    s3 = s1 + 1
    s4 = np.random.randint(1, 13, 1)[0]
    s5 = np.random.randint(1, 5, 1)[0]
    if s4 == 12:
        s6 = s5
    else:
        s6 = s4 * 5 + s5

    j1 = '과' if s2 % 10 in have_jongsung_num else '와'

    stem = stem.format(s2=s2, s3=s3, s4=s4, s5=s5, j1=j1)
    answer = answer.format(s1=s1, s6=s6)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, j1=j1)

    return stem, answer, comment



















# 2-2-4-08
def timeandhour224_Stem_003():
    stem = "{t1}{j1}와 {t2}{j2}가 오늘 아침에 일어난 시각입니다. 두 사람 중에서 더 {stem_condition} 일어난 사람은 누구인가요?\n$$표$${t1} : {a1},  {t2} : {a2}$$/표$$\n"
    answer = "(정답)\n{cor_text}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT [$$/수식$${t1}$$수식$$RIGHT ]$$/수식$$ {c1}\n" \
              "$$수식$$LEFT [$$/수식$${t2}$$수식$$RIGHT ]$$/수식$$ {c2}\n" \
              "따라서 더 {stem_condition} 일어난 사람은 {cor_text}입니다.\n\n"

    stem_condition = np.random.choice(['일찍', '늦게'], 1)[0]
    s1 = np.random.randint(7, 9, 1)[0]
    s2 = np.random.randint(2, 5, 1)[0] * 5
    s3 = 12 if s1 == 1 else s1 - 1
    s4 = 60 - s2 + np.random.choice([-5, 5], 1)[0]
    s5 = 60 - s2

    terms = [np.random.choice(person_nam, 1)[0], np.random.choice(person_yeo, 1)[0]]
    np.random.shuffle(terms)
    t1, t2 = terms

    if stem_condition == '일찍' :
        cor_text = t1 if s5 < s4 else t2
    else :
        cor_text = t2 if s5 < s4 else t1


    ans_dict = {'$$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분 전' % (s1, s2) : ['$$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분 전 → $$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분' % (s1, s2, s3, s5), t1],
                '$$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분' % (s3, s4) : ['$$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분' % (s3, s4), t2]}

    ans = list(set(list(ans_dict.keys())))
    a1, a2 = ans
    c1, t1 = ans_dict.get(a1)
    c2, t2 = ans_dict.get(a2)

    j1 = '' if josa_check(t1[-1]) == ' ' else '이'
    j2 = '' if josa_check(t2[-1]) == ' ' else '이'


    stem = stem.format(t1=t1, t2=t2, j1=j1, j2=j2, a1=a1, a2=a2, stem_condition=stem_condition)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(t1=t1, t2=t2, c1=c1, c2=c2, cor_text=cor_text, stem_condition=stem_condition)

    return stem, answer, comment
























# 2-2-4-09
def timeandhour224_Stem_004():
    stem = "나타내는 시각이 다른 하나를 찾아 기호를 써 보세요.\n$$표$$㉠ {a1}\n㉡ {a2}\n㉢ {a3}$$/표$$\n"
    answer = "(정답)\n{cor_num}\n"
    comment = "(해설)\n" \
              "㉠ {c1}\n㉡ {c2}\n㉢ {c3}\n따라서 나타내는 시각이 다른 하나는 {cor_num}입니다.\n\n"

    flag = True
    while flag :
        s1 = np.random.randint(1, 13, 1)[0]
        s2 = np.random.choice([3, 4, 6, 7, 8, 9], 1)[0] + np.random.choice([0, 10], 1)[0]

        s3 = 12 if s1 == 1 else s1 -1
        s4 = 60 - s2

        s5 = np.random.choice([10, 15, 20], 1)[0] - (s2 % 10)
        s6 = 60 - s5

        if s5 > 3 and s2 != s5:
            flag = False

    ans_dict = {'$$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분 전' % (s1, s2) : '$$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분 전 → $$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분' % (s1, s2, s3, s4),
                '$$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분' % (s3, s4) : '$$수식$$%d$$수식$$시 $$수식$$%d$$/수식$$분' % (s3, s4),
                '$$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분 전' % (s1, s5) : '$$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분 전 → $$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분' % (s1, s5, s3, s6)}

    answers = list(set(list(ans_dict.keys())))
    a1, a2, a3 = answers
    c1 = ans_dict.get(a1)
    c2 = ans_dict.get(a2)
    c3 = ans_dict.get(a3)

    cor_text = '$$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분 전' % (s1, s5)

    cor_num = multiple_choice_jaum.get(answers.index(cor_text))

    stem = stem.format(a1=a1, a2=a2, a3=a3)
    answer = answer.format(cor_num=cor_num)
    comment = comment.format(c1=c1, c2=c2, c3=c3, cor_num=cor_num)

    return stem, answer, comment




























# 2-2-4-10
def timeandhour224_Stem_005():
    stem = "{n1}{j1}는 매일 $$수식$${s4}$$/수식$$분 동안 {t1}. 어느 날 {t2} 난 뒤 시계를 보니 $$수식$${s2}$$/수식$$시 $$수식$${s5}$$/수식$$분이었습니다. {n1}{j1}가 이날 {t3} 시작한 시각은 몇 시 몇 분인가요?\n"
    answer = "(정답)\n$$수식$${s2}$$/수식$$시 $$수식$${s6}$$/수식$$분\n"
    comment = "(해설)\n" \
              "{n1}{j1}가 {t3} 시작한 시각은 $$수식$${s2}$$/수식$$시 $$수식$${s5}$$/수식$$분에서 $$수식$${s4}$$/수식$$분 전의 시각이므로 " \
              "긴바늘이 $$수식$${s3} LEFT ( {s5}$$/수식$$분$$수식$$RIGHT )$$/수식$$에서 시계 반대 방향으로 " \
              "작은 눈금 $$수식$${s4}$$/수식$$칸$$수식$$LEFT ($$/수식$$큰 눈금 $$수식$${s1}$$/수식$$칸$$수식$$RIGHT )$$/수식$$을 움직인 시각입니다.\n" \
              "따라서 {n1}{j1}가 {t3} 시작한 시각은 $$수식$${s2}$$/수식$$시 $$수식$${s6}$$/수식$$분입니다.\n\n"

    terms_dict = {0 : ['그림을 그립니다', '그림을 다 그리고', '그림을 그리기'],
                  1 : ['책을 읽습니다', '책을 다 읽고', '책을 읽기'],
                  2 : ['숙제를 합니다', '숙제를 다 하고', '숙제를 하기'],
                  3 : ['피아노를 칩니다', '피아노를 다 치고', '피아노를 치기'],
                  4 : ['운동을 합니다', '운동을 다 하고', '운동을 하기']}

    n1 = np.random.choice(person_nam+person_yeo, 1)[0]
    j1 = '' if josa_check(n1[-1]) == ' ' else '이'
    mode = np.random.randint(0, 4, 1)[0]
    t1, t2, t3 = terms_dict.get(mode)

    flag = True

    while flag :
        s1 = np.random.randint(5, 12, 1)[0]
        s2 = np.random.randint(4, 10, 1)[0]
        s3 = np.random.randint(1, 13, 1)[0]
        s4 = s1 * 5
        s5 = s3 * 5
        s6 = s2 - 1 if s5 - s4 < 0 else s2

        if s5 - s4 > 0 and s1 != s3 and (s5 != 60) :
            s6 = s5 - s4
            flag = False

    stem = stem.format(s2=s2, s4=s4, s5=s5, t1=t1, t2=t2, t3=t3, n1=n1, j1=j1)
    answer = answer.format(s2=s2, s6=s6)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, t3=t3, n1=n1, j1=j1)

    return stem, answer, comment
























# 2-2-4-11
def timeandhour224_Stem_006():
    stem = "다음 중 잘못된 것을 모두 찾아 기호를 써 보세요.\n$$표$$㉠ {a1}\n㉡ {a2}\n㉢ {a3}$$/표$$\n"
    answer = "(정답)\n{cor_num}\n"
    comment = "(해설)\n" \
              "㉠ {c1}\n㉡ {c2}\n㉢ {c3}\n" \
              "따라서 잘못된 것은 {cor_num}입니다.\n\n"

    flag = True
    while flag :
        s1, s4, s7, s10 = np.random.choice(np.arange(13, 30), 4, False) * np.reshape([10]*4, -1)
        if s1 % 60 != 0 and s4 % 60 != 0 and s7 % 60 != 0 and s10 % 60 != 0 :
            s2, s3 = divmod(s1, 60)
            s5, s6 = divmod(s4, 60)
            s8, s9 = divmod(s7, 60)
            s11, s12 = divmod(s10, 60)

            flag = False

    ans_dict = {s1: ['$$수식$$%d$$/수식$$시간 $$수식$$%d$$/수식$$분$$수식$$` = ` %d$$/수식$$분' % (s2, s3, s1),
                     '$$수식$$%d$$/수식$$시간 $$수식$$%d$$/수식$$분$$수식$$` = ` %d$$/수식$$분' % (s2, s3, (s2+np.random.choice([-1, 1], 1)[0])*60+s3)],
                s4: ['$$수식$$%d$$/수식$$시간 $$수식$$%d$$/수식$$분$$수식$$` = ` %d$$/수식$$분' % (s5, s6, s4),
                     '$$수식$$%d$$/수식$$시간 $$수식$$%d$$/수식$$분$$수식$$` = ` %d$$/수식$$분' % (s5, s6, (s5+np.random.choice([-1, 1], 1)[0])*60+s3)],
                s7: ['$$수식$$%d$$/수식$$분$$수식$$` = ` %d$$/수식$$시간 $$수식$$%d$$/수식$$분' % (s7, s8, s9),
                     '$$수식$$%d$$/수식$$분$$수식$$` = ` %s$$/수식$$시간 $$수식$$%d$$/수식$$분' % (s7, str(s7)[0], s9)],
                s10: ['$$수식$$%d$$/수식$$분$$수식$$` = ` %d$$/수식$$시간 $$수식$$%d$$/수식$$분' % (s10, s11, s12),
                      '$$수식$$%d$$/수식$$분$$수식$$` = ` %d$$/수식$$시간 $$수식$$%d$$/수식$$분' % (s10, s11, s9 + np.random.choice([10, -10], 1)[0])]
                }

    targets = np.random.choice([s1, s4, s7, s10], 3, False)
    mode = [1, 1, 0]
    np.random.shuffle(mode)

    answers = []
    comments = []
    cor_num = []
    for i, m in enumerate(mode):
        a = ans_dict.get(targets[i])[m]
        c = a.split('= `')[0].strip()
        c += '= ` %d$$/수식$$분$$수식$$` + ` %d$$/수식$$분$$수식$$` = `' % (targets[i] - targets[i] % 60, targets[i] % 60)
        c += ans_dict.get(targets[i])[0].split('` = `')[1].strip()

        if m == 1:
            cor_num.append(multiple_choice_jaum.get(i))
        answers.append(a)
        comments.append(c)

    a1, a2, a3 = answers
    c1, c2, c3 = comments
    cor_num = ', '.join(cor_num)

    stem = stem.format(a1=a1, a2=a2, a3=a3)
    answer = answer.format(cor_num=cor_num)
    comment = comment.format(c1=c1, c2=c2, c3=c3, cor_num=cor_num)

    return stem, answer, comment




























# 2-2-4-12
def timeandhour224_Stem_007():
    stem = "놀이터에서 {t1}, {t2}, {t3}{j3_2} 놀고 있습니다. 놀이터에 온 지 {t1}{j1}는 {a1}, {t2}{j2}는 {a2}, {t3}{j3_1}는 {a3}이 지났다고 할 때 가장 {stem_condition} 놀이터에 온 어린이는 누구인가요?\n"
    answer = "(정답)\n{cor_text}\n"
    comment = "(해설)\n" \
              "{c1}\n" \
              "따라서 {c2}이므로 가장 {stem_condition} 놀이터에 온 어린이는 {cor_text}입니다.\n\n"

    stem_condition = np.random.choice(['먼저', '늦게'], 1)[0]
    terms = np.random.choice(person_nam + person_yeo, 3, False)
    mode = np.random.choice([0, 1], 1)[0]
    mode = [0, 0, 1] if mode == 0 else [1, 1, 0]
    np.random.shuffle(mode)

    flag = True
    while flag :
        s1, s2, s3, s4 = np.random.choice(np.arange(13, 30), 4, False) * np.reshape([5] * 4, -1)
        if s1 % 60 != 0 and s2 % 60 != 0 and s3 % 60 != 0 and s4 % 60 != 0:
            flag = False

    targets = list(np.random.choice([s1, s2, s3, s4], 3, False))
    target_name_dict = {targets[0] : terms[0], targets[1] : terms[1], targets[2] : terms[2]}

    answers, comments = [], []
    for i, t in enumerate(targets) :
        if mode[i] == 0 :
            answers.append('$$수식$$%d$$/수식$$분' % (t))
        else :
            n1, n2 = divmod(t, 60)
            answers.append('$$수식$$%d$$/수식$$시간 $$수식$$%d$$/수식$$분' % (n1, n2))
            comments.append('%s: $$수식$$%d$$/수식$$시간 $$수식$$%d$$/수식$$분$$수식$$` = ` %d$$/수식$$분'
                            '$$수식$$` + ` %d$$/수식$$분$$수식$$` = ` %d$$/수식$$분' % (terms[i], n1, n2, n1*60, n2, t))

    t1, t2, t3 = terms
    j1 = '' if josa_check(t1[-1]) == ' ' else '이'
    j2 = '' if josa_check(t2[-1]) == ' ' else '이'
    j3_1 = '' if josa_check(t3[-1]) == ' ' else '이'
    j3_2 = '가' if josa_check(t3[-1]) == ' ' else '이'

    a1, a2, a3 = answers
    c1 = '\n'.join(comments)
    if stem_condition == '먼저' :
        targets.sort(reverse=True)
        c2 = '$$수식$$' + '$$/수식$$분$$수식$$` &gt; ` '.join(list(map(str, targets))) + '$$/수식$$분'
        cor_text = target_name_dict.get(max(targets))
    else :
        targets.sort()
        c2 = '$$수식$$' + '$$/수식$$분$$수식$$` &lt; ` '.join(list(map(str, targets))) + '$$/수식$$분'
        cor_text = target_name_dict.get(min(targets))

    stem = stem.format(t1=t1, t2=t2, t3=t3, a1=a1, a2=a2, a3=a3, j1=j1, j2=j2, j3_1=j3_1, j3_2=j3_2, stem_condition=stem_condition)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1, c2=c2, cor_text=cor_text, stem_condition=stem_condition)

    return stem, answer, comment


































# 2-2-4-15
def timeandhour224_Stem_008():
    stem = "다음을 읽고 $$수식$${s1}$$/수식$$교시 수업이 {stem_condition} 시각은 몇 시 몇 분인가요?\n$$표$${t1}{j1}네 학교는 $$수식$$9$$/수식$$시에 $$수식$$1$$/수식$$교시 수업을 시작합니다. 수업은 $$수식$${s2}$$/수식$$분 동안 하고, $$수식$${s3}$$/수식$$분 동안 쉽니다.$$/표$$\n"
    answer = "(정답)\n{cor_text}\n"
    comment = "(해설)\n" \
              "{c1}{c2}\n\n"

    t1 = np.random.choice(person_nam+person_yeo, 1)[0]
    j1 = '' if josa_check(t1[-1]) == ' ' else '이'

    stem_condition = np.random.choice(['시작하는', '끝나는'], 1)[0]

    s1 = np.random.choice([2, 3], 1)[0]
    s2 = np.random.choice([35, 40, 45], 1)[0]
    s3 = np.random.choice([10, 15], 1)[0]

    c1 = ['$$수식$$9$$/수식$$시']
    time = 540
    for _ in range(0, s1) :
        c1.append('$$수식$$LEFT ( %d$$/수식$$분 후$$수식$$RIGHT )$$/수식$$' % (s2))

        time += s2
        d, m = divmod(time, 60)
        c1.append('$$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분' % (d, m))
        c1.append('$$수식$$LEFT ( %d$$/수식$$분 후$$수식$$RIGHT )$$/수식$$' % (s3))

        time += s3
        d, m = divmod(time, 60)
        c1.append('$$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분' % (d, m))

    comments = []
    for i in range(0, s1*4, 4) :

        c = ' → '.join(c1[i:i+5]) + '이므로 $$수식$$%d$$/수식$$교시 수업이 끝나는 시각은 ' % ((i//4)+1) + c1[i+2] + \
            '이고 $$수식$$%d$$/수식$$교시 수업이 시작하는 시각은 %s입니다.' % ((i//4)+2, c1[i+4])
        c2 = ' → '.join(c1[i:i+3])
        c = c.replace(' $$수식$$0$$/수식$$분', '')
        c2 = c2.replace(' $$수식$$0$$/수식$$분', '')

        comments.append(c)

        start_time = c1[i].replace(' $$수식$$0$$/수식$$분', '')
        end_time = c1[i+2].replace(' $$수식$$0$$/수식$$분', '')


    comments.pop()

    cor_text = start_time if stem_condition == '시작하는' else end_time
    c1 = '\n'.join(comments)
    c2 = '\n' if stem_condition == '시작하는' else '\n' + c2
    stem = stem.format(s1=s1, s2=s2, s3=s3, stem_condition=stem_condition, t1=t1, j1=j1)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1, c2=c2)

    return stem, answer, comment

































# 2-2-4-16
def timeandhour224_Stem_009():
    stem = "{t1}{j1}는 {a2} 동안 책 읽기를 했습니다. 책 읽기를 {t2} 시각이 {t3}이라면 책 읽기를 {stem_condition} 시각은 몇 시 몇 분인가요?\n"
    answer = "(정답)\n{cor_text}\n"
    comment = "(해설)\n" \
              "책 읽기를 {stem_condition} 시각은 {t3}에서 {a2} {t4}입니다.\n" \
              "{c1}\n\n"

    t1 = np.random.choice(person_yeo+person_nam, 1)[0]
    j1 = '' if josa_check(t1[-1]) == ' ' else '이'
    flag = True
    while flag :
        stem_condition = np.random.choice(['끝낸', '시작한'], 1)[0]
        s1 = np.random.randint(40, 140, 1)[0] * 5
        s2 = np.random.randint(15, 37, 1)[0] * 5
        s3 = s1 - s2
        s1_d, s1_m = divmod(s1, 60)
        s2_d, s2_m = divmod(s2, 60)
        s3_d, s3_m = divmod(s3, 60)

        a1 = '$$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분' % (s1_d, s1_m)
        a2 = '$$수식$$%d$$/수식$$시간 $$수식$$%d$$/수식$$분' % (s2_d, s2_m)
        a3 = '$$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분' % (s3_d, s3_m)

        if s1_m != 0 and s2_m != 0 and s1_m != s2_m :
            if stem_condition == "시작한" :
                cor_text, t2, t3, t4 = a3, "끝낸", a1, "전"
                c1 = '%s → $$수식$$LEFT ( %d$$/수식$$시간 전$$수식$$RIGHT )$$/수식$$ → $$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분 → $$수식$$LEFT ( %d$$/수식$$분 전$$수식$$RIGHT )$$/수식$$ → $$수식$$%d$$/수식$$시 → $$수식$$LEFT ( %d$$/수식$$분 전$$수식$$RIGHT )$$/수식$$ → %s' % (a1, s2_d, s1_d-s2_d, s1_m, s1_m, s1_d-s2_d, s2_m-s1_m, cor_text)

                if s3_d > 0 and s1_d < 12 and s2_m > s1_m :
                    flag = False

            elif stem_condition == "끝낸" :
                cor_text, t2, t3, t4 = a1, "시작한", a3, "후"
                a3 = a3.replace('$$수식$$0$$/수식$$시', '$$수식$$12$$/수식$$시')
                c1 = '%s → $$수식$$LEFT ( %d$$/수식$$시간 후$$수식$$RIGHT )$$/수식$$ → $$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분 → $$수식$$LEFT ( %d$$/수식$$분 후$$수식$$RIGHT )$$/수식$$ → $$수식$$%d$$/수식$$시 → $$수식$$LEFT ( %d$$/수식$$분 후$$수식$$RIGHT )$$/수식$$ → %s' % (a3, s2_d, s3_d+s2_d, s3_m, 60 - s3_m, s1_d, s2_m-(60 - s3_m), cor_text)
                if s3_m + s2_m > 60 :
                    flag = False


    t1 = np.random.choice(person_nam+person_yeo, 1)[0]
    j1 = '' if josa_check(t1[-1]) == ' ' else '이'

    stem = stem.format(a2=a2, t1=t1, t2=t2, t3=t3, j1=j1, stem_condition=stem_condition)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(stem_condition=stem_condition, a2=a2, t3=t3, t4=t4, c1=c1)

    return stem, answer, comment







































# 2-2-4-17
def timeandhour224_Stem_010():
    stem = "오전 $$수식$${s1}$$/수식$$시에서 오후 $$수식$${s2}$$/수식$$시까지 시계의 긴바늘은 몇 바퀴를 돌까요?\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$바퀴\n"
    comment = "(해설)\n" \
              "긴바늘이 $$수식$$1$$/수식$$바퀴를 도는 데 걸리는 시간은 $$수식$$1$$/수식$$시간이고 " \
              "$$수식$$1$$/수식$$시간 동안 짧은 바늘은 큰 눈금 한 칸을 움직입니다.\n" \
              "따라서 짧은바늘이 $$수식$${s1}$$/수식$$시에서 낮 $$수식$$12$$/수식$$시까지 큰 눈금을 " \
              "$$수식$${s3}$$/수식$$칸 움직이므로 $$수식$${s3}$$/수식$$시간, " \
              "낮 $$수식$$12$$/수식$$시에서 오후 $$수식$${s2}$$/수식$$시까지 큰 눈금 $$수식$${s2}$$/수식$$칸이 움직인 " \
              "것이므로 $$수식$${s2}$$/수식$$시간입니다.\n" \
              "따라서 $$수식$${s3}$$/수식$$시간$$수식$$` + ` {s2}$$/수식$$시간$$수식$$` = ` {cor_text}$$/수식$$시간이므로 " \
              "시계의 긴 바늘은 $$수식$${cor_text}$$/수식$$바퀴 돕니다.\n\n"

    flag = True
    while flag :
        s1 = np.random.randint(7, 11, 1)[0]
        s2 = np.random.randint(2, 10, 1)[0]
        if s1 != s2:
            flag = False

    s3 = 12 - s1
    cor_text = s2 + s3

    stem = stem.format(s1=s1, s2=s2)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s1=s1, s2=s2, s3=s3, cor_text=cor_text)

    return stem, answer, comment






































# 2-2-4-18
def timeandhour224_Stem_011():
    stem = "다음 중 틀린 것은 어느 것인가요?\n① {a1}\n② {a2}\n③ {a3}\n④ {a4}\n⑤ {a5}\n"
    answer = "(정답)\n{cor_num}\n"
    comment = "(해설)\n" \
              "{cor_num} {c}\n\n"

    flag = True
    while flag :
        s1, s2, s3, s4, s5, s6 = np.random.choice(np.arange(30, 81, 1), 6, False)
        if s1 % 24 != 0 and s2 % 24 != 0 and s3 % 24 != 0 and s4 % 24 != 0 and s5 % 24 != 0 and s6 % 24 != 0 :

            unique_check_list = []
            ans_dict = {}
            for num in [s1, s2, s3] :
                day, time = divmod(num, 24)
                u_num = num + np.random.choice([-2, -1, 1, 2, 3])
                ans_dict[num] = ['$$수식$$%d$$/수식$$일 $$수식$$%d$$/수식$$시간$$수식$$` = ` %d$$/수식$$시간' % (day, time, num),
                                 '$$수식$$%d$$/수식$$일 $$수식$$%d$$/수식$$시간$$수식$$` = ` %d$$/수식$$시간' % (day, time, u_num)]

                unique_check_list.append('%d일 %d시간' % (day, time))
                unique_check_list.append('%d시간' % (u_num))

            for num in [s4, s5, s6]:
                day, time = divmod(num, 24)
                u_day, u_time = divmod(num, 20)
                ans_dict[num] = ['$$수식$$%d$$/수식$$시간$$수식$$` = ` %d$$/수식$$일 $$수식$$%d$$/수식$$시간' % (num, day, time),
                                 '$$수식$$%d$$/수식$$시간$$수식$$` = ` %d$$/수식$$일 $$수식$$%d$$/수식$$시간' % (num, u_day, u_time)]

                unique_check_list.append('%d일 %d시간' % (u_day, u_time))
                unique_check_list.append('%d시간' % (num))

            if len(list(set(unique_check_list))) == 10 :
                flag = False

    s_idx = np.random.choice([0, 1], 1)[0]
    targets = list(ans_dict.keys())[s_idx:s_idx+5]
    cor_idx = np.random.randint(0, 5, 1)[0]

    answers = []
    for i, t in enumerate(targets) :
        if i == cor_idx :
            answers.append(ans_dict.get(t)[1])
            d, m = divmod(t, 24)

            if ans_dict.get(t)[1].split('=')[0].find('일') == -1 :
                c = '$$수식$$%s$$/수식$$시간$$수식$$` = ` %s%d$$/수식$$시간$$수식$$` = ` %d$$/수식$$일 $$수식$$%d$$/수식$$시간' % (t, '24$$/수식$$시간$$수식$$` + ` '*d, m, d, m)

            else :
                c = '$$수식$$%d$$/수식$$일 $$수식$$%d$$/수식$$시간$$수식$$` = ` %s%d$$/수식$$시간$$수식$$` = ` %d$$/수식$$시간' % (d, m, '24$$/수식$$시간$$수식$$` + ` '*d, m, t)
        else :
            answers.append(ans_dict.get(t)[0])

    a1, a2, a3, a4, a5 = answers
    cor_num = multiple_choice_nums.get(cor_idx)

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(cor_num=cor_num)
    comment = comment.format(cor_num=cor_num, c=c)

    return stem, answer, comment


































# 2-2-4-19
def timeandhour224_Stem_012():
    stem = "하루는 낮과 밤으로 이루어져 있습니다. 어느 날 낮의 길이가 $$수식$${s1}$$/수식$$시간이라면 그날 밤의 길이는 몇 시간인가요?\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$시간\n"
    comment = "(해설)\n" \
              "하루는 $$수식$$24$$/수식$$시간입니다.\n" \
              "낮의 길이가 $$수식$${s1}$$/수식$$시간이므로 밤의 길이는 {c} ` LEFT ($$/수식$$시간$$수식$$RIGHT )$$/수식$$입니다.\n\n"

    s1 = np.random.randint(10, 15, 1)[0]
    cor_text = 24 - s1
    c = '$$수식$$24 ` - ` %d ` = ` %d' % (s1, cor_text)

    stem = stem.format(s1=s1)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s1=s1, c=c)

    return stem, answer, comment
































# 2-2-4-20
def timeandhour224_Stem_013():
    stem = "{t1}{j1}네 가족은 $$수식$${s1}$$/수식$$월 $$수식$${s2}$$/수식$$일 오전 $$수식$${s4}$$/수식$$시부터 $$수식$${s1}$$/수식$$월 $$수식$${s3}$$/수식$$일 오후 $$수식$${s5}$$/수식$$시까지 {t2}에 있었습니다. {t1}{j1}네 가족이 {t2}에 있었던 시간은 모두 몇 시간인가요?\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$시간\n"
    comment = "(해설)\n" \
              "하루는 $$수식$$24$$/수식$$시간이므로 " \
              "$$수식$${s1}$$/수식$$월 $$수식$${s2}$$/수식$$일 오전 $$수식$${s4}$$/수식$$시부터 " \
              "$$수식$${s1}$$/수식$$월 $$수식$${s3}$$/수식$$일 오전 $$수식$${s4}$$/수식$$시까지는 " \
              "$$수식$${c1} ` LEFT ($$/수식$$시간$$수식$$RIGHT )$$/수식$$입니다.\n" \
              "따라서 $$수식$${s1}$$/수식$$월 $$수식$${s3}$$/수식$$일 오전 $$수식$${s4}$$/수식$$시부터 " \
              "$$수식$${s1}$$/수식$$월 $$수식$${s3}$$/수식$$일 오후 $$수식$${s5}$$/수식$$시까지는 " \
              "$$수식$${s8}$$/수식$$시간이므로 " \
              "{t1}{j1}네 가족이 {t2}에 있었던 시간은 $$수식$${c2} ` LEFT ($$/수식$$시간$$수식$$RIGHT )$$/수식$$입니다.\n\n"

    flag = True
    while flag :
        s1 = np.random.randint(1, 13, 1)[0]

        s2 = np.random.randint(1, 28, 1)[0]
        s3 = s2 + np.random.choice([2, 3], 1)[0]

        s4 = np.random.randint(6, 12, 1)[0]
        s5 = np.random.randint(7, 12, 1)[0]

        s6 = s3 - s2
        s7 = 24 * s6
        s8 = 12 - s4 + s5
        cor_text = s7 + s8

        if s1 != 2:
            flag = False
        elif s1 == 2 and s3 < 29:
            flag = False

    t1 = np.random.choice(person_nam+person_yeo, 1)[0]
    j1 = '' if josa_check(t1[-1]) == ' ' else '이'
    t2 = np.random.choice(city_name, 1)[0]
    c1 = '%s ` = ` %d' % (' ` + ` '.join(['24']*s6), s7)
    c2 = '%d ` + ` %d ` = ` %d' % (s7, s8, cor_text)

    stem = stem.format(t1=t1, t2=t2, j1=j1, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(cor_text=cor_text)
    comment= comment.format(t1=t1, t2=t2, j1=j1, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s8=s8, c1=c1, c2=c2)

    return stem, answer, comment



































# 2-2-4-21
def timeandhour224_Stem_014():
    stem = "오늘 {t1} $$수식$${s3}$$/수식$$시부터 내일 {t2} $$수식$${s4}$$/수식$$시까지는 몇 시간인가요?\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$시간\n"
    comment = "(해설)\n" \
              "{c1}\n" \
              "따라서 오늘 {t1} $$수식$${s3}$$/수식$$시부터 내일 {t2} $$수식$${s4}$$/수식$$시까지는 $$수식$${c2} LEFT ($$/수식$$시간$$수식$$RIGHT )$$/수식$$입니다.\n\n"

    flag = True
    while flag :
        s1 = np.random.randint(1, 23, 1)[0]
        s2 = np.random.randint(1, 23, 1)[0]

        t1, s3 = ['오후', s1-12] if s1 > 12 else ['오전', s1]
        t2, s4 = ['오후', s2-12] if s2 > 12 else ['오전', s2]
        s5 = s3 + s4

        if s1 != s2 and t1 != t2 and s5 > 12 and s3 != 12 and s4 != 12:
            s6 = 12-s3 if t1 == '오후' else 24-s3
            if t1 == '오전' :
                m = 12-s3
                n = s3-m
                c1 = '오늘 오전 $$수식$$%d$$/수식$$시 → $$수식$$LEFT ( %d$$/수식$$시간 후$$수식$$RIGHT )$$/수식$$ → 오늘 낮 $$수식$$12$$/수식$$시 → $$수식$$LEFT ( 12$$/수식$$시간 후$$수식$$RIGHT )$$/수식$$ → 밤 $$수식$$12$$/수식$$시' % (s3, m)
                cor_text = s6
                c2 = '%d `+` 12' % m
            else :
                c1 = '오늘 오후 $$수식$$%d$$/수식$$시 → $$수식$$LEFT ( %d$$/수식$$시간 후$$수식$$RIGHT )$$/수식$$ → 밤 $$수식$$12$$/수식$$시' % (s3, s6)
                cor_text = s6
                c2 = '%d' % s6


            if t2 == '오전' :
                c1 += ' → $$수식$$LEFT ( %d$$/수식$$시간 후$$수식$$RIGHT )$$/수식$$ → 내일 오전 $$수식$$%d$$/수식$$시' % (s4, s4)
                cor_text += s4

                c2 += ' `+` %d `=` %d' % (s4, cor_text)
            else :
                c1 += ' → $$수식$$LEFT ( 12$$/수식$$시간 후$$수식$$RIGHT )$$/수식$$ → 내일 낮 $$수식$$12$$/수식$$시 → $$수식$$LEFT ( %d$$/수식$$시간 후$$수식$$RIGHT )$$/수식$$ → 내일 오후 $$수식$$%d$$/수식$$시' % (s4, s4)
                cor_text += 12 + s4

                c2 += ' `+` 12 `+` %d `=` %d' % (s4, cor_text)

            if cor_text > 12 and cor_text % 12 != 0 :
                flag = False


    stem = stem.format(s3=s3, s4=s4, t1=t1, t2=t2)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1, c2=c2, t1=t1, t2=t2, s3=s3, s4=s4)

    return stem, answer, comment









































# 2-2-4-22
def timeandhour224_Stem_015():
    stem = "$$수식$$1$$/수식$$시간에 $$수식$${s2}$$/수식$$분씩 빨라지는 시계가 있습니다. 이 시계의 시각을 오늘 {t1} $$수식$${s1}$$/수식$$시에 정확하게 맞추었습니다. 내일 {t1} $$수식$${s1}$$/수식$$시에 이 시계가 나타내는 시각은 {t1} 몇 시 몇 분인가요?\n"
    answer = "(정답)\n{cor_text}\n"
    comment = "(해설)\n" \
              "오늘 {t1} $$수식$${s1}$$/수식$$시부터 내일 {t1} $$수식$${s1}$$/수식$$시까지는 하루이고, " \
              "하루는 $$수식$$24$$/수식$$시간이므로 시계는 $$수식$${c1}$$/수식$$분 빨라진다. " \
              "{c2} 내일 {t1} $$수식$${s1}$$/수식$$시에 이 시계가 나타내는 시각은 {t1} {cor_text}이다.\n\n"



    s1 = np.random.randint(1, 11, 1)[0]
    s2 = np.random.choice([1, 2, 3], 1)[0]
    t1 = '오후' if s1 < 7 else '오전'
    s3 = 24 * s2
    c1 = '24 ` TIMES ` %d `=` %d' % (s2, s3) if s2 != 1 else '24'
    if s3 == 72 :
        c2 = '$$수식$$72$$/수식$$분은 $$수식$$1$$/수식$$시간 $$수식$$12$$/수식$$분이므로'
        cor_text = '$$수식$$%d$$/수식$$시 $$수식$$12$$/수식$$분' % (s1+1)

    else :
        c2 = '따라서'
        cor_text = '$$수식$$%d$$/수식$$시 $$수식$$%d$$/수식$$분' % (s1, s3)

    stem = stem.format(t1=t1, s1=s1, s2=s2)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(t1=t1, s1=s1, c1=c1, c2=c2, cor_text=cor_text)

    return stem, answer, comment






































# 2-2-4-24
def timeandhour224_Stem_016():
    stem = "오늘은 $$수식$${s1}$$/수식$$월 $$수식$${s2}$$/수식$$일입니다. 오늘부터 $$수식$${s3}$$/수식$$일 {stem_condition} 몇 월 며칠일까요?\n"
    answer = "(정답)\n{cor_text}\n"
    comment = "(해설)\n" \
              "$$수식$${s2}$$/수식$$일에서 $$수식$${s3}$$/수식$$일 {stem_condition} " \
              "$$수식$${c1}$$/수식$$(일)입니다.\n" \
              "따라서 오늘부터 $$수식$${s3}$$/수식$$일 {stem_condition} {cor_text}입니다.\n\n"

    flag = True
    while flag :
        s1 = np.random.randint(1, 13, 1)[0]
        s2 = np.random.randint(1, month_date_dict.get(s1), 1)[0]
        s3 = np.random.randint(10, 30, 1)[0]

        if s2 + s3 < month_date_dict.get(s1) :
            stem_condition = '후는'
            op = '+'
            s4 = s2 + s3
            flag = False
        elif s2 - s3 > 0 :
            stem_condition = '전은'
            op = '-'
            s4 = s2 - s3
            flag = False

    c1 = '%d `%s` %d `=` %d' % (s2, op, s3, s4)
    cor_text = '$$수식$$%d$$/수식$$월 $$수식$$%d$$/수식$$일' % (s1, s4)
    stem = stem.format(s1=s1, s2=s2, s3=s3, stem_condition=stem_condition)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s2=s2, s3=s3, c1=c1, stem_condition=stem_condition, cor_text=cor_text)

    return stem, answer, comment










































# 2-2-4-25
def timeandhour224_Stem_017():
    stem = "{t1}{j1}는 $$수식$${s1}$$/수식$$일 동안 매일 {t2}. {t1}{j1}가 {t3} 기간은 몇 주일 며칠인가요?\n"
    answer = "(정답)\n{cor_text}\n"
    comment = "(해설)\n" \
              "{c1}\n\n"

    terms = {0 : ['피아노를 쳤습니다', '피아노를 친'],
             1 : ['그림을 그렸습니다', '그림을 그린'],
             2 : ['줄넘기를 했습니다', '줄넘기를 한'],
             3 : ['달리기를 했습니다', '달리기를 한']}

    t1 = np.random.choice(person_nam+person_yeo, 1)[0]
    idx = np.random.randint(0, 4, 1)[0]
    t2= terms.get(idx)[0]
    t3= terms.get(idx)[1]
    j1 = '' if josa_check(t1[-1]) == ' ' else '이'

    flag = True
    while flag :
        s1 = np.random.randint(8, 60, 1)[0]
        if s1 % 7 != 0 :
            flag = False

    m, d = divmod(s1, 7)
    c1 = '$$수식$$%d$$/수식$$일$$수식$$` = ` %s$$수식$$` + ` %d$$/수식$$일\n$$수식$$= ` %d$$/수식$$주일 ' \
         '$$수식$$%d$$/수식$$일' % (s1, '$$수식$$` + ` '.join(['7$$/수식$$일'] * m), d, m, d)
    cor_text = '$$수식$$%d$$/수식$$주일 $$수식$$%d$$/수식$$일' % (m, d)

    stem = stem.format(t1=t1, t2=t2, t3=t3, j1=j1, s1=s1)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1)

    return stem, answer, comment







































# 2-2-4-26
def timeandhour224_Stem_018():
    stem = "{t1}{j1}는 {t2}에 가입하여 $$수식$${s1}$$/수식$$년 $$수식$${s2}$$/수식$$개월 동안 {t2} 활동을 하고 있습니다. {t1}{j1}는 몇 개월째 {t2} 활동을 하고 있나요?\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$개월\n"
    comment = "(해설)\n" \
              "$$수식$$1$$/수식$$년은 $$수식$$12$$/수식$$개월이므로\n" \
              "{c1}\n" \
              "따라서 {t1}{j1}는 $$수식$${cor_text}$$/수식$$개월째 {t2} 활동을 하고 있습니다.\n\n"

    t1 = np.random.choice(person_nam+person_yeo, 1)[0]
    t2 = np.random.choice(['아람단', '스카우트', '봉사단체'], 1)[0]
    j1 = '' if josa_check(t1[-1]) == ' 'else '이'

    s1 = np.random.randint(1, 3, 1)[0]
    s2 = np.random.randint(3, 12, 1)[0]
    cor_text = s1 * 12 + s2

    c1 = '$$수식$$%d$$/수식$$년 $$수식$$%d$$/수식$$개월$$수식$$` = ` %s$$수식$$` + ` %d$$/수식$$개월$$수식$$` = ` %d$$/수식$$개월' \
         '' % (s1, s2, '$$수식$$` + ` '.join(['12$$/수식$$개월']*s1), s2, cor_text)

    stem = stem.format(t1=t1, t2=t2, j1=j1, s1=s1, s2=s2)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(t1=t1, t2=t2, j1=j1, c1=c1, cor_text=cor_text)

    return stem, answer, comment








































# 2-2-4-27
def timeandhour224_Stem_019():
    stem = "날수가 같은 달끼리 짝 지은 것을 찾아 기호를 써보세요.\n$$표$$㉠ {a1}    ㉡ {a2}    ㉢ {a3}    ㉣ {a4}$$/표$$\n"
    answer = "(정답)\n{cor_num}\n"
    comment = "(해설) ㉠ {c1}\n" \
              "㉡ {c2}\n" \
              "㉢ {c3}\n" \
              "㉣ {c4}\n\n"

    flag = True
    while flag :
        month_list = list(np.arange(1, 13, 1))
        np.random.shuffle(month_list)

        month_pair = [sorted([month_list[i], month_list[i+1]]) for i in range(0, 12, 2)]
        ans_list, unans_list = [], []
        for m1, m2 in month_pair :
            m1_date = month_date_dict.get(m1)
            m2_date = month_date_dict.get(m2)
            if m1_date == m2_date :
                ans_list.append([m1, m2])
            else :
                unans_list.append([m1, m2])

        if len(ans_list) > 1 and len(unans_list) >= 3 :
            flag = False

    ans = ans_list[np.random.randint(0, len(ans_list), 1)[0]]
    bogi_list = [unans_list[i] for i in np.random.choice(np.arange(0, len(unans_list), 1), 3, False)]
    bogi_list.append(ans)

    np.random.shuffle(bogi_list)
    cor_idx = bogi_list.index(ans)

    answers, comments = [], []
    for i, [b1, b2] in enumerate(bogi_list) :
        b1_text = '$$수식$$%d$$/수식$$월' % (b1)
        b2_text = '$$수식$$%d$$/수식$$월' % (b2)

        b1_date = '$$수식$$28$$/수식$$일($$수식$$29$$/수식$$일)' if b1 == 2 else '$$수식$$%d$$/수식$$일' % (month_date_dict.get(b1))
        b2_date = '$$수식$$28$$/수식$$일($$수식$$29$$/수식$$일)' if b2 == 2 else '$$수식$$%d$$/수식$$일' % (month_date_dict.get(b2))

        answers.append('%s, %s' % (b1_text, b2_text))
        comments.append('%s → %s, %s → %s' % (b1_text, b1_date, b2_text, b2_date))

    a1, a2, a3, a4 = answers
    c1, c2, c3, c4 = comments
    cor_num = multiple_choice_jaum.get(cor_idx)

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4)
    answer = answer.format(cor_num=cor_num)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4)

    return stem, answer, comment








































# 2-2-4-28
def timeandhour224_Stem_020():
    stem = "{t1}{j1}네 학교에서는 $$수식$${s1}$$/수식$$월 $$수식$${s2}$$/수식$$일부터 $$수식$${s4}$$/수식$$월 $$수식$${s5}$$/수식$$일까지 어린이 {t2} 작품 전시회를 합니다. 전시회를 하는 기간은 며칠인가요?\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$일\n"
    comment = "(해설)\n" \
              "$$수식$${s1}$$/수식$$월은 $$수식$${s3}$$/수식$$일까지 있으므로 $$수식$${s2}$$/수식$$일부터 " \
              "$$수식$${s3}$$/수식$$일까지 $$수식$${s6}$$/수식$$일 동안 전시회를 하고, " \
              "$$수식$${s4}$$/수식$$월은 $$수식$$1$$/수식$$일부터 $$수식$${s5}$$/수식$$일 동안 전시회를 합니다. " \
              "전시회를 하는 기간은 $$수식$${c1} ` LEFT ($$/수식$$일$$수식$$RIGHT )$$/수식$$입니다.\n\n"

    t1 = np.random.choice(person_nam+person_yeo, 1)[0]
    j1 = '' if josa_check(t1[-1]) == ' ' else '이'
    t2 = np.random.choice(['공예', '미술'])

    while True :
        s1 = np.random.randint(1, 12, 1)[0]
        if s1 != 2 :
            break
    s2 = np.random.randint(1, 20, 1)[0]
    s3 = month_date_dict.get(s1)

    s4 = s1 + 1
    s5 = np.random.randint(s2+1, month_date_dict.get(s4), 1)[0]

    s6 = s3 - s2 + 1
    cor_text = s5 + s6
    c1 = '%s ` + ` %s ` = ` %s' % (s6, s5, cor_text)

    stem = stem.format(t1=t1, t2=t2, j1=j1, s1=s1, s2=s2, s4=s4, s5=s5)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, c1=c1)

    return stem, answer, comment





































# 2-2-4-30
def timeandhour224_Stem_021():
    stem = "어느 해의 $$수식$${s1}$$/수식$$월 $$수식$${s2}$$/수식$$일은 {s3}요일입니다. 같은 해 $$수식$${s1}$$/수식$$월의 마지막 날은 무슨 요일인가요?\n"
    answer = "(정답)\n{cor_text}요일\n"
    comment = "(해설)\n" \
              "$$수식$${s1}$$/수식$$월은 $$수식$${s4}$$/수식$$일까지 있습니다. $$수식$${s1}$$/수식$$월 $$수식$${s2}$$/수식$$일은 {s3}요일이므로 {c1}도 {s3}요일입니다.\n" \
              "{c2}이므로 $$수식$${s1}$$/수식$$월의 마지막 날인 $$수식$${s4}$$/수식$$일은 {cor_text}요일입니다.\n\n"

    flag = True
    while flag :
        s1 = np.random.randint(1, 13, 1)[0]
        s2 = np.random.randint(1, 11, 1)[0]
        s3 = week_idx_dict.get(np.random.randint(0, 7, 1)[0])
        s4 = month_date_dict.get(s1)
        if s1 != 2 and (s4 - s2) % 7 > 2 :
            c1_list = [str(i) for i in range(s2, s4, 7)]
            c1 = '$$수식$$' + '$$/수식$$일, $$수식$$'.join(c1_list[1:]) + '$$/수식$$일'
            c2_list = []
            for i, day in enumerate(np.arange(int(c1_list[-1])+1, s4+1)) :
                cor_text = week_idx_dict.get(('일월화수목금토'.index(s3)+i+1) % 7)
                c2_list.append('$$수식$$%d$$/수식$$월 $$수식$$%d$$/수식$$일은 %s요일' % (s1, day, cor_text))

            if cor_text != s3:
                flag = False

    c2 = ', '.join(c2_list)
    stem = stem.format(s1=s1, s2=s2, s3=s3)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, c1=c1, c2=c2, cor_text=cor_text)

    return stem, answer, comment











# if __name__ == '__main__':
#     TimeAndHour_Stem_001()
#     TimeAndHour_Stem_002()
#     TimeAndHour_Stem_003()
#     TimeAndHour_Stem_004()
#     TimeAndHour_Stem_005()
#     TimeAndHour_Stem_006()
#     TimeAndHour_Stem_007()
#     TimeAndHour_Stem_008()
#     TimeAndHour_Stem_009()
#     TimeAndHour_Stem_010()
#     TimeAndHour_Stem_011()
#     TimeAndHour_Stem_012()
#     TimeAndHour_Stem_013()
#     TimeAndHour_Stem_014()
#     TimeAndHour_Stem_015()
#     TimeAndHour_Stem_016()
#     TimeAndHour_Stem_017()
#     TimeAndHour_Stem_018()
#     TimeAndHour_Stem_019()
#     TimeAndHour_Stem_020()
#     TimeAndHour_Stem_021()








