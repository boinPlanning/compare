import random
import itertools
import codecs
import os


PATH = '/home/boin-service/Visang/Dictionary/'

person_nam = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XY.txt'), 'r', 'utf-8').readlines()]
person_yeo = [name.strip() for name in codecs.open(os.path.join(PATH, 'name_XX.txt'), 'r', 'utf-8').readlines()]

STEM_008_DICT = ['장미꽃', '튤립', '카네이션', '무궁화', '국화꽃', '해바라기', '동백꽃']


multiple_choice_nums = {0: '①', 1: '②', 2: '③', 3: '④', 4: '⑤'}
multiple_choice_hangul = {0: '㉠', 1: '㉡', 2: '㉢', 3: '㉣', 4: '㉤'}



def check_josa(number):
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



def num2hangul(num_list, flag=True):
    '''
    1000의 자리 자연수를 한글로 읽은 것을 리턴함
    '''
    results = []
    num_dict = {'0':'', '1':'', '2':'이', '3':'삼', '4':'사', '5':'오', '6':'육', '7':'칠', '8':'팔', '9':'구'}
    num_dict_false = {'1':'일', '2':'이', '3':'삼', '4':'사', '5':'오', '6':'육', '7':'칠', '8':'팔', '9':'구'}

    for num in num_list:
        num = str(num)
        result = ''
        for i, n in enumerate(num):
            if flag:
                if n != '0':
                    if i == 0:
                        result += num_dict[n] + "천"
                    elif i == 1:
                        result += num_dict[n] + "백"
                    elif i == 2:
                        result += num_dict[n] + "십"
                    elif i == 3:
                        if n == 1:
                            result += "일"
                        else:
                            result += num_dict[n]
            else:
                if n == '0':
                    result += '영'
                else:
                    if i == 0:
                        result += num_dict_false[n] + "천"
                    elif i == 1:
                        result += num_dict_false[n] + "백"
                    elif i == 2:
                        result += num_dict_false[n] + "십"
                    elif i == 3:
                        result += num_dict_false[n]
        results.append(result)

    return results

















# 2-2-1-01
def fourdigits221_Stem_001():
    stem = "다음 중 $$수식$$1000$$/수식$$을 나타내는 수가 아닌 것은 어느 것일까요?\n① {a1}\n② {a2}\n③ {a3}\n④ {a4}\n⑤ {a5}\n"
    answer = "(정답)\n{ans_num}\n"
    comment = "(해설)\n" \
              "{ans_num} {com_text}\n\n"

    flag = True
    while flag:
        answer_dict, comment_dict = {}, {}
        ans_key = 0

        answers, comments = [], []

        # 100개씩 n묶음인 수
        s1 = random.randint(2, 9)
        true = "$$수식$$100$$/수식$$개씩 $$수식$$10$$/수식$$묶음인 수"
        false = "$$수식$$100$$/수식$$개씩 $$수식$$%s$$/수식$$묶음인 수" % s1
        com = "$$수식$$100$$/수식$$개씩 $$수식$$%s$$/수식$$묶음인 수는 $$수식$$%s$$/수식$$입니다." % (s1, 100*s1)
        answer_dict[ans_key] = [true, false]
        comment_dict[false] = com
        ans_key += 1

        # 999보다 1 큰 수
        s2 = random.randint(2, 5)
        true = "$$수식$$999$$/수식$$보다 $$수식$$1$$/수식$$ 큰 수"
        false = "$$수식$$999$$/수식$$보다 $$수식$$%s$$/수식$$ 큰 수" % s2
        com = "$$수식$$999$$/수식$$보다 $$수식$$%s$$/수식$$ 큰 수는 $$수식$$%s$$/수식$$입니다." % (s2, s2+999)
        answer_dict[ans_key] = [true, false]
        comment_dict[false] = com
        ans_key += 1

        # n보다 n 큰 수 (10의 단위)
        for _ in range(2):
            numbers = list(range(10, 100, 10))
            s3, s4 = random.sample(numbers, 2)
            true = "$$수식$$%s$$/수식$$보다 $$수식$$%s$$/수식$$ 큰 수" % (1000 - s3, s3)
            false = "$$수식$$%s$$/수식$$보다 $$수식$$%s$$/수식$$ 큰 수" % (1000 - s3, s4)
            com = "$$수식$$%s$$/수식$$보다 $$수식$$%s$$/수식$$ 큰 수는 $$수식$$%s$$/수식$$입니다." % (1000 - s3, s4, 1000 - s3 + s4)
            answer_dict[ans_key] = [true, false]
            comment_dict[false] = com
            ans_key += 1

        # n보다 n 큰 수 (100의 단위)
        for _ in range(2):
            numbers = list(range(100, 1000, 100))
            s5, s6 = random.sample(numbers, 2)
            true = "$$수식$$%s$$/수식$$보다 $$수식$$%s$$/수식$$ 큰 수" % (1000 - s5, s5)
            false = "$$수식$$%s$$/수식$$보다 $$수식$$%s$$/수식$$ 큰 수" % (1000 - s5, s6)
            com = "$$수식$$%s$$/수식$$보다 $$수식$$%s$$/수식$$ 큰 수는 $$수식$$%s$$/수식$$입니다." % (1000 - s5, s6, 1000 - s5 + s6)
            answer_dict[ans_key] = [true, false]
            comment_dict[false] = com
            ans_key += 1

        # 보기의 개수가 5개 이상인지 확인
        if len(answer_dict.keys()) >= 5 and len(comment_dict.keys()) >= 5:
            # 보기에 사용할 문제번호 5개
            ans_keys = list(answer_dict.keys())
            ans_keys = random.sample(ans_keys, 5)

            # 정답 번호 랜덤선택
            ans_index = random.randint(0, 4)
            ans_num = multiple_choice_nums[ans_index]

            for i, num in enumerate(ans_keys):
                if i == ans_index:
                    ans_text = answer_dict[num][1]
                    com_text = comment_dict[ans_text]
                    answers.append(ans_text)
                else:
                    answers.append(answer_dict[num][0])

            if len(answers) == len(set(answers)):
                flag = False

    a1, a2, a3, a4, a5 = answers

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(ans_num=ans_num)
    comment = comment.format(ans_num=ans_num, com_text=com_text)

    return stem, answer, comment


























# 2-2-1-05
def fourdigits221_Stem_002():
    '''
    :param r1: s1의 최솟값 [int] {2:3}
    :param r2: s2의 최댓값 [int] {8:9}
    '''
    stem = "㉠에 알맞은 수를 구해 보세요.\n$$표$${s1}$$/표$$\n"
    answer = "(정답)\n$$수식$${ans_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "{c1}\n" \
              "따라서 ㉠에 알맞은 수는 $$수식$${ans_text}$$/수식$$입니다.\n\n"
              

    r1 = 2
    r2 = 8


    flag = True

    while flag:
        true_list, com_dict = [], {}
        s2 = random.randint(r1, r2)
        ans_text = 1000 * s2

        # ㄱ은 1000이 s2개인 수입니다.
        true = "㉠은 $$수식$$1000$$/수식$$이 $$수식$${s2}$$/수식$$개인 수입니다.".format(s2=s2)
        com = "$$수식$$1000$$/수식$$이 $$수식$${s2}$$/수식$$개이면 $$수식$${ans_text}$$/수식$$입니다.".format(s2=s2, ans_text=ans_text)
        true_list.append(true)
        com_dict[true] = com

        # 1000이 s2개인 수는 ㄱ입니다.
        true = "$$수식$$1000$$/수식$$이 $$수식$${s2}$$/수식$$개인 수는 ㉠입니다.".format(s2=s2)
        com = "$$수식$$1000$$/수식$$이 $$수식$${s2}$$/수식$$개이면 $$수식$${ans_text}$$/수식$$입니다.".format(s2=s2, ans_text=ans_text)
        true_list.append(true)
        com_dict[true] = com

        # ㄱ은 1000이 s2개 모인 수입니다.
        true = "㉠은 $$수식$$1000$$/수식$$이 $$수식$${s2}$$/수식$$개 모인 수입니다.".format(s2=s2)
        com = "$$수식$$1000$$/수식$$이 $$수식$${s2}$$/수식$$개 모인 수는 $$수식$${ans_text}$$/수식$$입니다.".format(s2=s2, ans_text=ans_text)
        true_list.append(true)
        com_dict[true] = com

        # 1000이 s2개 모인 수는 ㄱ입니다.
        true = "$$수식$$1000$$/수식$$이 $$수식$${s2}$$/수식$$개 모인 수는 ㉠입니다.".format(s2=s2)
        com = "$$수식$$1000$$/수식$$이 $$수식$${s2}$$/수식$$개 모인 수는 $$수식$${ans_text}$$/수식$$입니다.".format(s2=s2, ans_text=ans_text)
        true_list.append(true)
        com_dict[true] = com

        if ans_text < 10000:
            flag = False

            s1 = random.choice(true_list)
            c1 = com_dict[s1]

    stem = stem.format(s1=s1)
    answer = answer.format(ans_text=ans_text)
    comment = comment.format(c1=c1, ans_text=ans_text)

    return stem, answer, comment


























# 2-2-1-06
def fourdigits221_Stem_003():
    '''
    :param r1: 나타내는 수의 최솟값 [int] {2000:3000}
    :param r2: 나타내는 수의 최댓값 [int] {8000:9000}
    '''
    stem = "나타내는 수가 다른 것을 찾아 기호를 써 보세요.\n$$표$$㉠ {a1}\n㉡ {a2}\n㉢ {a3}\n㉣ {a4}$$/표$$\n"
    answer = "(정답)\n{ans_num}\n"
    comment = "(해설)\n" \
              "㉠ {c1}\n" \
              "㉡ {c2}\n" \
              "㉢ {c3}\n" \
              "㉣ {c4}\n" \
              "따라서 나타내는 수가 다른 것은 {ans_num}입니다.\n\n"


    r1 = 2000
    r2 = 8000


    flag = True

    while flag:
        answers = []
        true_list, false_list, comment_dict = [], [], {}
        ans_key = 0

        # 나타내는 수
        s1 = random.randrange(r1, r2, 1000) # 나타내는 수가 5000인 경우

        s2 = s1 // 1000     # 5000은 1000이 5(s2)개인 수
        s3 = s1 // 100      # 5000은 100이 50(s3)인 수
        s4 = s1 // 10       # 5000은 10이 500(s4)인 수

        # 해당 단원에서는 1000 * 1의 배수 계산만 가능한 것으로 보여 (1000 * 20은 불가해 보임)
        # 오답은 (100, 1의 배수), (10, 1의 배수), (10, 10의 배수) 3개로 제한

        # 1000이 n개인 수
        tmp_a, tmp_b = random.sample([s2, 1000], 2)
        true = "$$수식$$%s$$/수식$$%s $$수식$$%s$$/수식$$개인 수" % (tmp_a, check_josa(tmp_a)[3], tmp_b)
        true_com = "%s → $$수식$$%s$$/수식$$" % (true, s1)
        true_list.append(true)
        comment_dict[true] = true_com
        ans_key += 1

        # 100이 n0개인 수
        tmp_a, tmp_b = random.sample([s3, 100], 2)
        true = "$$수식$$%s$$/수식$$이 $$수식$$%s$$/수식$$개인 수" % (tmp_a, tmp_b)
        true_com = "%s → $$수식$$%s$$/수식$$" % (true, s1)
        true_list.append(true)
        comment_dict[true] = true_com

        tmp_a, tmp_b = random.sample([s2, 100], 2)
        false = "$$수식$$%s$$/수식$$%s $$수식$$%s$$/수식$$개인 수" % (tmp_a, check_josa(tmp_a)[3], tmp_b)
        false_com = "%s → $$수식$$%s$$/수식$$" % (false, 100*s2)
        false_list.append(false)
        comment_dict[false] = false_com

        # 10이 n00개인 수
        tmp_a, tmp_b = random.sample([s4, 10], 2)
        true = "$$수식$$%s$$/수식$$이 $$수식$$%s$$/수식$$개인 수" % (tmp_a, tmp_b)
        true_com = "%s → $$수식$$%s$$/수식$$" % (true, s1)
        true_list.append(true)
        comment_dict[true] = true_com

        tmp_a, tmp_b = random.sample([s3, 10], 2)
        false_a = "$$수식$$%s$$/수식$$이 $$수식$$%s$$/수식$$개인 수" % (tmp_a, tmp_b)
        false_a_com = "%s → $$수식$$%s$$/수식$$" % (false_a, 10 * s3)
        false_list.append(false_a)
        comment_dict[false_a] = false_a_com

        tmp_a, tmp_b = random.sample([s2, 10], 2)
        false_b = "$$수식$$%s$$/수식$$%s $$수식$$%s$$/수식$$개인 수" % (tmp_a, check_josa(tmp_a)[3], tmp_b)
        false_b_com = "%s → $$수식$$%s$$/수식$$" % (false_b, 10 * s2)
        false_list.append(false_b)
        comment_dict[false_b] = false_b_com

        # 정답 조건 확인
        if len(true_list) == 3 and len(false_list) >= 1:
            # 보기 만들기
            answers = random.sample(true_list, 3)

            # 정답 텍스트 뽑고, 인덱스에 맞춰서 answers 리스트에 넣어줌
            ans_text = random.choice(false_list)
            answers.append(ans_text)
            random.shuffle(answers)
            ans_num = multiple_choice_hangul[answers.index(ans_text)]

            flag = False

    a1, a2, a3, a4 = answers
    c1 = comment_dict[a1]
    c2 = comment_dict[a2]
    c3 = comment_dict[a3]
    c4 = comment_dict[a4]

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4)
    answer = answer.format(ans_num=ans_num)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, ans_num=ans_num)

    return stem, answer, comment

































# 2-2-1-07
def fourdigits221_Stem_004():
    '''
    :param r1: 나타내는 수의 최솟값 [int] {2000:3000}
    :param r2: 나타내는 수의 최댓값 [int] {8000:9000}
    '''
    stem = "다음 수를 쓰고 읽어 보세요.\n$$표$$$$수식$${s1}$$/수식$$이 $$수식$${s2}$$/수식$$개{word}$$/표$$\n"
    answer = "(정답)\n$$수식$${write}$$/수식$$, {read}\n"
    comment = "(해설)\n" \
              "$$수식$${s1}$$/수식$$이 $$수식$${s3}$$/수식$$개이면 $$수식$$1000$$/수식$$이므로 $$수식$${s1}$$/수식$$이 " \
              "$$수식$${s2}$$/수식$$개이면 $$수식$${write}$$/수식$$입니다.\n" \
              "$$수식$${write}$$/수식$$은 {read}이라고 읽습니다.\n\n"


    r1 = 2000
    r2 = 8000


    num_dict = {1:'', 2:'이', 3:'삼', 4:'사', 5:'오', 6:'육', 7:'칠', 8:'팔', 9:'구'}

    flag = True

    while flag:
        # 나타내는 수
        write = random.randrange(r1, r2, 1000)  # 나타내는 수가 5000인 경우
        read = num_dict[write//1000] + "천"

        word = random.choice(["인 수", " 모인 수", " 있는 수"])

        t1 = write // 1000  # 5000은 1000이 5(t1)개인 수
        t2 = write // 100  # 5000은 100이 50(t2)인 수
        t3 = write // 10  # 5000은 10이 500(t3)인 수

        # 해당 단원에서는 1000 * 1의 배수 계산만 가능한 것으로 보여 (1000 * 20은 불가해 보임)
        # 답이 될 수 있는 경우의 수를 (100, 10), (10, 100), (1000, 1) 3개로 제한

        s2 = random.choice([t1, t2, t3])
        s1 = write // s2
        s3 = 1000 // s1

        if 1000 < write < 10000 and 0 < s3 < 1000 and s1 % 10 == 0:
            flag = False

    stem = stem.format(s1=s1, s2=s2, word=word)
    answer = answer.format(write=write, read=read)
    comment = comment.format(s1=s1, s2=s2, s3=s3, write=write, read=read)

    return stem, answer, comment
































# 2-2-1-08
def fourdigits221_Stem_005():
    '''
    :param r1: 나타내는 수의 최솟값 [int] {2000:3000}
    :param r2: 나타내는 수의 최댓값 [int] {8000:9000}
    '''
    stem = "{t1}{t1_josa} $$수식$${s1}$$/수식$$송이 있습니다. 이 {t1}{t1_josa2} 바구니 한 개에 $$수식$${s2}$$/수식$$송이씩 담으려고 합니다. 바구니는 몇 개 필요한가요?\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$개\n"
    comment = "(해설)\n" \
              "{c1}입니다.\n" \
              "따라서 {t1} $$수식$${s1}$$/수식$$송이를 바구니 한 개에 $$수식$${s2}$$/수식$$송이씩 담으려면 바구니는 " \
              "$$수식$${cor_text}$$/수식$$개 필요합니다.\n\n"


    r1 = 2000
    r2 = 8000


    flag = True
    
    while flag:
        # 꽃 이름 설정
        t1 = random.choice(STEM_008_DICT)
        if josa_check(t1[-1]) == ' ':
            t1_josa = "가"
            t1_josa2 = "를"
        else:
            t1_josa = "이"
            t1_josa2 = "을"

        # 나타내는 수
        s1 = random.randrange(r1, r2, 1000)  # 나타내는 수가 5000인 경우

        a1 = s1 // 1000  # 5000은 1000이 5(t1)개인 수
        a2 = s1 // 100  # 5000은 100이 50(t2)인 수
        a3 = s1 // 10  # 5000은 10이 500(t3)인 수

        # 해당 단원에서는 1000 * 1의 배수 계산만 가능한 것으로 보여 (1000 * 20은 불가해 보임)
        # 답이 될 수 있는 경우의 수를 (100, 10), (10, 100), (1000, 1) 3개로 제한

        cor_text = random.choice([a1, a2, a3])
        s2 = s1 // cor_text     # s2는 10, 100, 1000만 존재함

        if s2 == 1000:
            c1 = "$$수식$$%s$$/수식$$은 $$수식$$1000$$/수식$$이 $$수식$$%s$$/수식$$인 수" % (s1, cor_text)
        elif s2 == 100:
            c1 = "$$수식$$%s$$/수식$$은 $$수식$$1000$$/수식$$이 $$수식$$%s$$/수식$$인 수이고, $$수식$$1000$$/수식$$은 " \
                 "$$수식$$100$$/수식$$이 $$수식$$10$$/수식$$인 수이므로 $$수식$$%s$$/수식$$은 " \
                 "$$수식$$%s$$/수식$$이 $$수식$$%s$$/수식$$인 수" % (s1, s1 // 1000, s1, s2, cor_text)
        elif s2 == 10:
            c1 = "$$수식$$%s$$/수식$$은 $$수식$$1000$$/수식$$이 $$수식$$%s$$/수식$$인 수이고, $$수식$$1000$$/수식$$은 " \
                 "$$수식$$10$$/수식$$이 $$수식$$100$$/수식$$인 수이므로 $$수식$$%s$$/수식$$은 " \
                 "$$수식$$%s$$/수식$$이 $$수식$$%s$$/수식$$인 수" % (s1, s1 // 1000, s1, s2, cor_text)

        if s2 % 10 == 0 and cor_text < 1000:
            flag = False

    stem = stem.format(t1=t1, t1_josa=t1_josa, t1_josa2=t1_josa2, s1=s1, s2=s2)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1, s1=s1, s2=s2, cor_text=cor_text, t1=t1)

    return stem, answer, comment




























# 2-2-1-10
def fourdigits221_Stem_006():
    '''
    :param r1: 등장하는 수의 최솟값 [int] {1001:1002}
    :param r2: 등장하는 수의 최댓값 [int] {9998:9999}
    '''
    stem = "다음 중 수를 잘못 읽은 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${a1}$$/수식$$ → {w1}\n㉡ $$수식$${a2}$$/수식$$ → {w2}\n㉢ $$수식$${a3}$$/수식$$ → {w3}\n㉣ $$수식$${a4}$$/수식$$ → {w4}$$/표$$\n"
    answer = "(정답)\n{cor_num}\n"
    comment = "(해설)\n" \
              "{cor_num} {c1}\n" \
              "{c2}\n\n"


    r1 = 1001
    r2 = 9998


    flag = True
    
    while flag:
        answers = random.sample(list(range(r1, r2)), 3)
        hanguls = num2hangul(answers)

        false = str(random.randint(1001, 9999))
        if "0" not in false and "1" not in false:
            if random.choice(['0', '1']) == '0':
                tmp = random.randint(1, 3)
                false = false[:tmp] + "0" + false[tmp + 1:]
                false2hangul = num2hangul([int(false)], False)[0]
                c1 = "자리 숫자가 $$수식$$0$$/수식$$이면 읽지 않습니다."
                c2 = "$$수식$$%s$$/수식$$ → %s" % (false, num2hangul([int(false)])[0])
            else:
                tmp = random.randint(0, 2)
                false = false[:tmp] + "1" + false[tmp + 1:]
                false2hangul = num2hangul([int(false)], False)[0]
                c1 = "자리 숫자가 $$수식$$1$$/수식$$이면 그 자릿값만을 읽습니다."
                c2 = "$$수식$$%s$$/수식$$ → %s" % (false, num2hangul([int(false)])[0])

            ans_index = random.randint(0, 3)
            cor_num = multiple_choice_hangul[ans_index]
            answers.insert(ans_index, false)
            hanguls.insert(ans_index, false2hangul)

            flag = False

    a1, a2, a3, a4 = answers
    w1, w2, w3, w4 = hanguls

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, w1=w1, w2=w2, w3=w3, w4=w4)
    answer = answer.format(cor_num=cor_num)
    comment = comment.format(cor_num=cor_num, c1=c1, c2=c2)

    return stem, answer, comment




















# 2-2-1-11
def fourdigits221_Stem_007():
    stem = "다음 수를 써 보세요.\n$$표$$$$수식$$1000$$/수식$$이 $$수식$${s1}$$/수식$$개, $$수식$$100$$/수식$$이 $$수식$${s2}$$/수식$$개, $$수식$$10$$/수식$$이 $$수식$${s3}$$/수식$$개, $$수식$$1$$/수식$$이 $$수식$${s4}$$/수식$$개인 수$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$1000$$/수식$$이 $$수식$${s1}$$/수식$$개이면 $$수식$${c1}$$/수식$$, $$수식$$100$$/수식$$이 " \
              "$$수식$${s2}$$/수식$$개이면 $$수식$${c2}$$/수식$$, $$수식$$10$$/수식$$이 $$수식$${s3}$$/수식$$개이면 " \
              "$$수식$${c3}$$/수식$$, $$수식$$1$$/수식$$이 $$수식$${s4}$$/수식$$개이면 $$수식$${c4}$$/수식$$입니다.\n" \
              "→ $$수식$${c1} ` + ` {c2} ` + ` {c3} ` + ` {c4} ` = ` {cor_text}$$/수식$$\n\n"

    flag = True

    while flag:
        s1 = random.randint(1, 9)
        s2 = random.randint(1, 20)
        s3 = random.randint(1, 20)
        s4 = random.randint(1, 40)

        c1 = 1000 * s1
        c2 = 100 * s2
        c3 = 10 * s3
        c4 = s4

        cor_text = c1 + c2 + c3 + c4

        if (1000 < cor_text) and ( cor_text < 10000 ):
            flag = False

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, c1=c1, c2=c2, c3=c3, c4=c4, cor_text=cor_text)

    return stem, answer, comment
























# 2-2-1-13
def fourdigits221_Stem_008():
    stem = "{t1}{t1_josa1} $$수식$${s1}$$/수식$$원을 모으려고 합니다. 지금까지 모은 돈이 $$수식$$1000$$/수식$$원짜리 지폐 $$수식$${s2}$$/수식$$장, $$수식$$100$$/수식$$원짜리 동전 $$수식$${s3}$$/수식$$개, $$수식$$10$$/수식$$원짜리 동전 $$수식$${s4}$$/수식$$개라면 {t1}{t1_josa2} 더 모아야 하는 금액은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${s1}$$/수식$$은 $$수식$$1000$$/수식$$이 $$수식$${c1}$$/수식$$개, $$수식$$100$$/수식$$이 $$수식$${c2}$$/수식$$개, " \
              "$$수식$$10$$/수식$$이 $$수식$${c3}$$/수식$$개인 수이므로 $$수식$$1000$$/수식$$원짜리 지폐 $$수식$${c4}$$/수식$$장, $$수식$$100$$/수식$$원짜리 " \
              "동전 $$수식$${c5}$$/수식$$개, $$수식$$10$$/수식$$원짜리 동전 $$수식$${c6}$$/수식$$개를 더 모아야 합니다.\n" \
              "따라서 {t1}{t1_josa2} 더 모아야 하는 금액은 $$수식$${cor_text}$$/수식$$원입니다.\n\n"

    flag = True
    while flag:
        t1 = random.choice(person_yeo+person_nam)
        if josa_check(t1[-1]) == ' ':
            t1_josa1 = '는'
            t1_josa2 = '가'
        else:
            t1_josa1 = '이는'
            t1_josa2 = '이가'

        # 모은 돈
        s2 = random.randint(1, 8)   # 1000
        s3 = random.randint(1, 8)   # 100
        s4 = random.randint(1, 8)   # 10

        # 모자라는 돈
        c4 = random.randint(1, 8)   # 1000
        c5 = random.randint(1, 8)   # 100
        c6 = random.randint(1, 8)   # 10

        s1 = (1000 * s2) + (100 * s3) + (10 * s4) + (1000 * c4) + (100  * c5) + (10 * c6)
        cor_text = (1000 * c4) + (100  * c5) + (10 * c6)

        c1 = str(s1)[0]
        c2 = str(s1)[1]
        c3 = str(s1)[2]

        if 1000 < s1 < 10000 and str(s1).count("0") == 1:
            flag = False

    stem = stem.format(t1=t1, t1_josa1=t1_josa1, t1_josa2=t1_josa2, s1=s1, s2=s2, s3=s3, s4=s4)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s1=s1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, t1=t1, t1_josa2=t1_josa2, cor_text=cor_text)

    return stem, answer, comment

































# 2-2-1-14
def fourdigits221_Stem_009():
    stem = "천의 자리 숫자가 가장 큰 수를 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${s1}$$/수식$$    ㉡ $$수식$${s2}$$/수식$$    ㉢ $$수식$${s3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_num}\n"
    comment = "(해설)\n" \
              "천의 자리 숫자를 각각 알아보면\n" \
              "㉠ $$수식$${s1}$$/수식$$ → $$수식$${c1}$$/수식$$  ㉡ $$수식$${s2}$$/수식$$ → $$수식$${c2}$$/수식$$  ㉢ $$수식$${s3}$$/수식$$ → $$수식$${c3}$$/수식$$\n" \
              "따라서 $$수식$${c4}$$/수식$$이므로 천의 자리 숫자가 가장 큰 수는 {cor_num}입니다.\n\n"

    flag = True
    while flag:
        s1, s2, s3 = random.sample(list(range(1000, 9999)), 3)
        c1 = s1 // 1000
        c2 = s2 // 1000
        c3 = s3 // 1000

        tmp_list = [c1, c2, c3]
        tmp_list.sort(reverse=True)

        if len(tmp_list) == len(set(tmp_list)):
            c4 = " ` &gt; ` ".join(map(str, tmp_list))

            answers = [s1, s2, s3]
            cor_text = max(answers)
            cor_num = multiple_choice_hangul[answers.index(cor_text)]

            flag = False

    stem = stem.format(s1=s1, s2=s2, s3=s3)
    answer = answer.format(cor_num=cor_num)
    comment = comment.format(s1=s1, s2=s2, s3=s3, c1=c1, c2=c2, c3=c3, c4=c4, cor_num=cor_num)

    return stem, answer, comment

































# 2-2-1-15
def fourdigits221_Stem_010():
    stem = "다음은 {t1}{t1_josa} 네 자리 수인 핸드폰 비밀번호를 설명한 것입니다. 핸드폰 비밀번호는 몇 번인가요?\n$$표$$㉠ {s1}의 자리 숫자와 {s2}의 자리 숫자는 각각 $$수식$${s3}$$/수식$$입니다.\n㉡ {s4}의 자리 숫자와 {s5}의 자리 숫자는 각각 {s6}의 자리 숫자보다 $$수식$${s7}$$/수식$$ {q1}.$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "{s4}의 자리 숫자와 {s5}의 자리 숫자는 각각 {s6}의 자리 숫자보다 $$수식$${s7}$$/수식$$ {q2} $$수식$${c5}$$/수식$$입니다.\n" \
              "천의 자리 숫자가 $$수식$${c1}$$/수식$$, 백의 자리 숫자가 $$수식$${c2}$$/수식$$, 십의 자리 숫자가 $$수식$${c3}$$/수식$$, " \
              "일의 자리 숫자가 $$수식$${c4}$$/수식$$인 수는 $$수식$${cor_text}$$/수식$$입니다.\n" \
              "따라서 {t1}{t1_josa} 핸드폰 비밀번호는 $$수식$${cor_text}$$/수식$$번입니다.\n\n"

    flag = True
    while flag:
        t1 = random.choice(person_yeo+person_nam)
        if josa_check(t1[-1]) == ' ':
            t1_josa = '의'
        else:
            t1_josa = '이의'

        q1, q2 = random.choice([('큽니다', '크므로'), ('작습니다', '작으므로')])

        tmp_list = ['일', '십', '백', '천']
        s1, s2, s4, s5 = random.sample(tmp_list, 4)
        s6 = random.choice([s1, s2])
        s3 = random.randint(1, 8)
        s7 = random.randint(1, 8)

        if q1 == "큽니다":
            c5 = s3 + s7
        else:
            c5 = s3 - s7

        if 0 < c5 < 10:
            cor_text = 0
            for i, num in enumerate([s1, s2, s4, s5]):
                if i <= 1:
                    if num == "일":
                        cor_text += s3
                    elif num == "십":
                        cor_text += s3 * 10
                    elif num == "백":
                        cor_text += s3 * 100
                    elif num == "천":
                        cor_text += s3 * 1000
                else:
                    if num == "일":
                        cor_text += c5
                    elif num == "십":
                        cor_text += c5 * 10
                    elif num == "백":
                        cor_text += c5 * 100
                    elif num == "천":
                        cor_text += c5 * 1000

            if cor_text >= 1000:
                c1 = str(cor_text)[0]
                c2 = str(cor_text)[1]
                c3 = str(cor_text)[2]
                c4 = str(cor_text)[3]

                flag = False

    stem = stem.format(t1=t1, t1_josa=t1_josa, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, q1=q1)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s4=s4, s5=s5, s6=s6, s7=s7, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, q2=q2, cor_text=cor_text, t1=t1, t1_josa=t1_josa)

    return stem, answer, comment































# 2-2-1-16
def fourdigits221_Stem_011():
    stem = "{s1}{s1_josa} 나타내는 값이 가장 {q1} 수를 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${a1}$$/수식$$    ㉡ $$수식$${a2}$$/수식$$    ㉢ $$수식$${a3}$$/수식$$    ㉣ $$수식$${a4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_num}\n"
    comment = "(해설)\n" \
              "{s1}{s1_josa} 나타내는 값을 각각 알아보면 \n" \
              "㉠ $$수식$${c1}$$/수식$$, ㉡ $$수식$${c2}$$/수식$$, ㉢ $$수식$${c3}$$/수식$$, ㉣ $$수식$${c4}$$/수식$$입니다.\n" \
              "따라서 {s1}{s1_josa} 나타내는 값이 가장 {q1} 수는 {cor_num}입니다.\n\n"

    flag = True
    while flag:
        q1 = random.choice(['큰', '작은'])

        num_list = list(range(1, 10))
        s1 = random.randint(2, 9)
        s1_josa = check_josa(s1)[3]

        num_list.remove(s1)

        # 1000
        a1 = str(s1) + "".join(map(str, random.sample(num_list, 3)))

        # 100
        a2 = str(random.choice(num_list)) + str(s1) + "".join(map(str, random.sample(num_list, 2)))

        # 10
        a3 = "".join(map(str, random.sample(num_list, 2))) + str(s1) + str(random.choice(num_list))

        # 1
        a4 = "".join(map(str, random.sample(num_list, 3))) + str(s1)

        answers = [int(a) for a in [a1, a2, a3, a4]]
        random.shuffle(answers)

        comments = []
        for i, ans in enumerate(answers):
            if str(ans).index(str(s1)) == 0:
                comments.append(s1 * 1000)
                if q1 == "큰":
                    cor_num = multiple_choice_hangul[i]
            elif str(ans).index(str(s1)) == 1:
                comments.append(s1 * 100)
            elif str(ans).index(str(s1)) == 2:
                comments.append(s1 * 10)
            elif str(ans).index(str(s1)) == 3:
                comments.append(s1)
                if q1 == "작은":
                    cor_num = multiple_choice_hangul[i]

        if len(comments) == len(set(comments)):
            flag = False

    c1, c2, c3, c4 = comments
    a1, a2, a3, a4 = answers

    stem = stem.format(s1=s1, s1_josa=s1_josa, a1=a1, a2=a2, a3=a3, a4=a4, q1=q1)
    answer = answer.format(cor_num=cor_num)
    comment = comment.format(s1=s1, s1_josa=s1_josa, c1=c1, c2=c2, c3=c3, c4=c4, q1=q1, cor_num=cor_num)

    return stem, answer, comment






































# 2-2-1-17
def fourdigits221_Stem_012():
    stem = "다음 수 카드를 한 번씩만 사용하여 만들 수 있는 네 자리 수 중에서 {s1}의 자리 숫자가 $$수식$${s2}$$/수식$$인 수 중에서 $$수식$${s6}$$/수식$$보다 {q1} 수는 모두 몇 개인가요?\n$$수식$${box_s2}$$/수식$$  $$수식$${box_s3}$$/수식$$  $$수식$${box_s4}$$/수식$$  $$수식$${box_s5}$$/수식$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "{s1}의 자리 숫자가 $$수식$${s2}$$/수식$$인 네 자리 수를 $$수식$${c1}$$/수식$$라 하고 $$수식$${box}$$/수식$$ " \
              "안에 남은 숫자 $$수식$${s3}$$/수식$$, $$수식$${s4}$$/수식$$, $$수식$${s5}$$/수식$${s5_josa} 한 번씩 넣으면 됩니다.\n" \
              "→ {c2}\n" \
              "{s1}의 자리 숫자가 $$수식$${s2}$$/수식$$인 수 중에서 $$수식$${s6}$$/수식$$보다 {q1} 수는 {c3} 입니다.\n" \
              "따라서 만들 수 있는 네 자리 수 중에서 {s1}의 자리 숫자가 $$수식$${s2}$$/수식$$인 수 중에서 $$수식$${s6}$$/수식$$보다 {q1} 수는 " \
              "모두 $$수식$${cor_text}$$/수식$$개입니다.\n\n"

    box = '□'

    flag = True

    while flag:
        num_list = list(range(1, 10))
        s1 = random.choice(['일', '십', '백', '천'])
        s2 = random.choice(num_list)
        num_list.remove(s2)

        nums = random.sample(num_list, 3)
        s3, s4, s5 = nums
        answers = list(map(str, [s2, s3, s4, s5]))
        random.shuffle(answers)
        perm_list = list(map(''.join, itertools.permutations(answers)))
        c2_list = []
        for perm in perm_list:
            if s1 == "일" and str(perm).index(str(s2)) == 3:
                c2_list.append(perm)
                c1 = "□ ` □ ` □ ` %s" % s2
            elif s1 == "십" and str(perm).index(str(s2)) == 2:
                c2_list.append(perm)
                c1 = "□ ` □ ` %s ` □" % s2
            elif s1 == "백" and str(perm).index(str(s2)) == 1:
                c2_list.append(perm)
                c1 = "□ ` %s ` □ ` □" % s2
            elif s1 == "천" and str(perm).index(str(s2)) == 0:
                c2_list.append(perm)
                c1 = "%s ` □ ` □ ` □" % s2

        # 6개의 수 중에서 s6보다 크거나 작은 수 리스트를 구하는 과정
        c2_list.sort()
        s6_min = int(c2_list[0])//100*100
        s6_max = int(c2_list[-1])//100*100
        s6_list = list(range(s6_min, s6_max+100, 100))
        s6 = random.choice(s6_list)

        q1 = random.choice(['큰', '작은'])
        results = []
        if q1 == "큰":
            for num in c2_list:
                if int(num) > s6:
                    results.append(num)
        else:
            for num in c2_list:
                if int(num) < s6:
                    results.append(num)

        if len(results) > 0:
            cor_text = len(results)
            results.sort()
            c2 = "$$수식$$" + "$$/수식$$, $$수식$$".join(c2_list) + "$$/수식$$"
            c3 = "$$수식$$" + "$$/수식$$, $$수식$$".join(results) + "$$/수식$$"

            flag = False

    box_answers = ['box{``%s``}' % a for a in answers]
    _s2 = answers[0]
    box_s2, box_s3, box_s4, box_s5 = box_answers
    answers.remove(str(s2))
    s3, s4, s5 = answers
    s5_josa = check_josa(s5)[2]

    stem = stem.format(s1=s1, s2=s2, s6=s6, q1=q1, box_s2=box_s2, box_s3=box_s3, box_s4=box_s4, box_s5=box_s5)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s1=s1, s2=s2, _s2=_s2, s6=s6, q1=q1, c1=c1, box=box, s3=s3, s4=s4, s5=s5, s5_josa=s5_josa, c2=c2, c3=c3, cor_text=cor_text)

    return stem, answer, comment



































# 2-2-1-18
def fourdigits221_Stem_013():
    stem = "천의 자리 숫자가 나타내는 값이 $$수식$${s3}$$/수식$$이고, {s1}의 자리 숫자가 $$수식$${s4}$$/수식$$, {s2}의 자리 숫자가 $$수식$${s5}$$/수식$$인 네 자리 수 중에서 $$수식$${s7}$$/수식$$보다 {q1} 수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "천의 자리 숫자가 $$수식$${s6}$$/수식$$, {s1}의 자리 숫자가 $$수식$${s4}$$/수식$$, {s2}의 자리 숫자가 " \
              "$$수식$${s5}$$/수식$$인 네 자리 수는 {c1}입니다.\n" \
              "따라서 $$수식$${box}$$/수식$$ 안에는 $$수식$$0$$/수식$$부터 $$수식$$9$$/수식$$까지의 숫자가 들어갈 " \
              "수 있으므로 $$수식$${s7}$$/수식$$보다 {q1} 수는 $$수식$${c2}$$/수식$$ 입니다.\n" \
              "따라서 조건에 맞는 수는 $$수식$${cor_text}$$/수식$$개입니다.\n\n"

    box = '□'

    flag = True
    while flag:
        s3 = random.randint(1, 9)
        s4 = random.randint(0, 9)
        s5 = random.randint(0, 9)
        s6 = s3 * 1000

        tmp = random.choice(['일', '십', '백'])

        if tmp == "일":
            s1 = "백"
            s2 = "십"
            c1 = "$$수식$$%s ` %s ` %s ` □/수식$$" % (s3, s4, s5)
            s7_min = int("%s%s%s%s" % (s3, s4, s5, 0))
            s7_max = int("%s%s%s%s" % (s3, s4, s5, 9))
            s7_list = list(range(s7_min, s7_max+1))
        elif tmp == "십":
            s1 = "백"
            s2 = "일"
            c1 = "$$수식$$%s ` %s ` □ ` %s$$/수식$$" % (s3, s4, s5)
            s7_min = int("%s%s%s%s" % (s3, s4, 0, s5))
            s7_max = int("%s%s%s%s" % (s3, s4, 9, s5))
            s7_list = list(range(s7_min, s7_max+10, 10))
        elif tmp == "백":
            s1 = "십"
            s2 = "일"
            c1 = "$$수식$$%s ` □ ` %s ` %s$$/수식$$" % (s3, s4, s5)
            s7_min = int("%s%s%s%s" % (s3, 0, s4, s5))
            s7_max = int("%s%s%s%s" % (s3, 9, s4, s5))
            s7_list = list(range(s7_min, s7_max+100, 100))

        s7 = random.choice(s7_list)
        q1 = random.choice(['큰', '작은'])

        results = []
        if q1 == "큰":
            for num in s7_list:
                if int(num) > s7:
                    results.append(num)
        else:
            for num in s7_list:
                if int(num) < s7:
                    results.append(num)

        if len(results) > 0:
            cor_text = len(results)
            c2 = "$$수식$$" + "$$/수식$$, $$수식$$".join(map(str, results)) + "$$/수식$$"
            flag = False

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s7=s7, q1=q1)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s1=s1, s2=s2, s4=s4, s5=s5, s6=s6, s7=s7, c1=c1, c2=c2, q1=q1, cor_text=cor_text, box=box)

    return stem, answer, comment








































# 2-2-1-19
def fourdigits221_Stem_014():
    stem = "{t1}{t1_josa} 어떤 수를 $$수식$${box_1000}$$/수식$$ $$수식$${s1}$$/수식$$개, $$수식$${box_100}$$/수식$$ $$수식$${s2}$$/수식$$개, $$수식$${box_10}$$/수식$$ $$수식$${s3}$$/수식$$개, $$수식$${box_1}$$/수식$$ $$수식$${s4}$$/수식$$개로 나타내었습니다. 어떤 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$100$$/수식$$이 $$수식$${s2}$$/수식$$개이면 {c1}이고, $$수식$$10$$/수식$$이 " \
              "$$수식$${s3}$$/수식$$개이면 {c2}입니다. $$수식$$1$$/수식$$이 $$수식$${s4}$$/수식$$개이면 " \
              "{c3}이므로 어떤 수는 $$수식$$1000$$/수식$$이 $$수식$${c5}$$/수식$$개, $$수식$$100$$/수식$$이 " \
              "$$수식$${c6}$$/수식$$개, $$수식$$10$$/수식$$이 $$수식$${c7}$$/수식$$개, $$수식$$1$$/수식$$이 " \
              "$$수식$${c8}$$/수식$$개인 수입니다.\n" \
              "따라서 어떤 수는 $$수식$${cor_text}$$/수식$$입니다.\n\n"

    flag = True
    while flag:
        t1 = random.choice(person_yeo+person_nam)
        if josa_check(t1[-1]) == ' ':
            t1_josa = '는'
        else:
            t1_josa = '이는'

        s1 = random.randint(1, 8)   # 1000
        s2 = random.randint(1, 40)  # 100
        s3 = random.randint(1, 40)  # 10
        s4 = random.randint(1, 40)  # 1
        if len(list(set([s1, s2, s3, s4]))) > 2 :
            c5, c6, c7, c8 = s1, 0, 0, 0

            # 100
            if s2 >= 10 and s2 % 10 != 0:
                c1 = "$$수식$$1000$$/수식$$이 $$수식$$%s$$/수식$$개, $$수식$$100$$/수식$$이 $$수식$$%s$$/수식$$개" % (s2 // 10, s2 % 10)
                c5 += s2 // 10
                c6 += s2 % 10
            elif s2 >= 10 and s2 % 10 == 0:
                c1 = "$$수식$$1000$$/수식$$이 $$수식$$%s$$/수식$$개" % int(s2 // 10)
                c5 += s2 // 10
            else:
                c1 = "$$수식$$100$$/수식$$이 $$수식$$%s$$/수식$$개" % s2
                c6 += s2

            # 10
            if s3 >= 10 and s3 % 10 != 0:
                c2 = "$$수식$$100$$/수식$$이 $$수식$$%s$$/수식$$개, $$수식$$10$$/수식$$이 $$수식$$%s$$/수식$$개" % (s3 // 10, s3 % 10)
                c6 += s3 // 10
                c7 += s3 % 10
            elif s3 >= 10 and s3 % 10 == 0:
                c2 = "$$수식$$100$$/수식$$이 $$수식$$%s$$/수식$$개" % int(s3 // 10)
                c6 += s3 // 10
            else:
                c2 = "$$수식$$10$$/수식$$이 $$수식$$%s$$/수식$$개" % s3
                c7 += s3
            # 1
            if s4 >= 10 and s4 % 10 != 0:
                c3 = "$$수식$$10$$/수식$$이 $$수식$$%s$$/수식$$개, $$수식$$1$$/수식$$이 $$수식$$%s$$/수식$$개" % (s4 // 10, s4 % 10)
                c7 += s4 // 10
                c8 += s4 % 10
            elif s4 >= 10 and s4 % 10 == 0:
                c3 = "$$수식$$10$$/수식$$이 $$수식$$%s$$/수식$$개" % int(s4 // 10)
                c7 += s4 // 10
            else:
                c3 = "$$수식$$1$$/수식$$이 $$수식$$%s$$/수식$$개" % s4
                c8 += s4

            if c5 < 10 and c6 < 10 and c7 < 10 and c8 < 10 :
                cor_text = "%s%s%s%s" % (c5, c6, c7, c8)
                if int(cor_text) < 10000 :
                    flag = False

    box_1000 = 'box{``1000``}'
    box_100 = 'box{``100``}'
    box_10 = 'box{``10``}'
    box_1 = 'box{``1``}'

    stem = stem.format(t1=t1, t1_josa=t1_josa, s1=s1, s2=s2, s3=s3, s4=s4, box_1=box_1, box_10=box_10, box_100=box_100, box_1000=box_1000)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c5=c5, c6=c6, c7=c7, c8=c8, s2=s2, s3=s3, s4=s4, cor_text=cor_text)

    return stem, answer, comment





































# 2-2-1-20
def fourdigits221_Stem_015():
    stem = "다음 조건에 맞는 수 중에서 두 번째로 큰 네 자리 수는 얼마인가요?\n$$표$$㉠ {s1}의 자리 숫자는 $$수식$${s2}$$/수식$${s2_josa} 나타냅니다.\n㉡ {s3}의 자리 숫자와 {s4}의 자리 숫자의 합은 $$수식$${s5}$$/수식$$입니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "{s1}의 자리 숫자가 $$수식$${s2}$$/수식$${s2_josa} 나타내므로 {s1}의 자리 숫자는 $$수식$${c1}$$/수식$$입니다. 네 자리 수는 {c2}{c2_josa} 같이 나타낼 수 있습니다.\n" \
              "가장 큰 네 자리 수는 {h1}$$수식$$`=`9$$/수식$$이고 {h2}$$수식$$`+`$$/수식$${h3}$$수식$$`=` {s5}$$/수식$$이므로 {h2}$$수식$$`=` {s5}$$/수식$$일 때 {h3}$$수식$$`=` 0$$/수식$$이므로 $$수식$${c5}$$/수식$$입니다.\n" \
              "따라서 두 번째로 큰 네 자리 수는 {h1}$$수식$$`=` 9$$/수식$$이고 {h2}$$수식$$`=` {c3}$$/수식$$일 때 {h3}$$수식$$`=` 1$$/수식$$이므로 $$수식$${cor_text}$$/수식$$입니다.\n\n"

    flag = True
    while flag:
        s1 = random.choice(['천', '백', '십', '일'])
        s2 = random.randint(2, 9)
        s5 = random.randint(3, 9)

        if s1 == "천":
            c1 = s2
            s2 = s2 * 1000
            c2 = "$$수식$$%s$$/수식$$㉠㉡㉢" % c1
            c2_josa = "과"
            c3 = s5-1

            s3, s4, num = random.sample(['백', '십', '일'], 3)
            if num == "백":
                h1, h2, h3 = "㉠", "㉡", "㉢"
                cor_text = "%s%s%s%s" % (c1, 9, c3, 1)
                c5 = "%s%s%s%s" % (c1, 9, s5, 0)
            elif num == "십":
                h1, h2, h3 = "㉡", "㉠", "㉢"
                cor_text = "%s%s%s%s" % (c1, c3, 9, 1)
                c5 = "%s%s%s%s" % (c1, s5, 9, 0)
            else:
                h1, h2, h3 = "㉡", "㉢", "㉠"
                cor_text = "%s%s%s%s" % (c1, c3, 1, 9)
                c5 = "%s%s%s%s" % (c1, s5, 0, 9)
        elif s1 == "백":
            c1 = s2
            s2 = s2 * 100
            c2 = "㉠$$수식$$%s$$/수식$$㉡㉢" % c1
            c2_josa = "과"
            c3 = s5 - 1

            s3, s4, num = random.sample(['천', '십', '일'], 3)
            if num == "천":
                h1, h2, h3 = "㉠", "㉡", "㉢"
                cor_text = "%s%s%s%s" % (9, c1, c3, 1)
                c5 = "%s%s%s%s" % (9, c1, s5, 0)
            else:
                # 천의 자리 숫자와 일의 자리 숫자의 합이 n인 경우 천의 자리에는 0이 올 수 없기 때문에 제외함
                continue
        elif s1 == "십":
            c1 = s2
            s2 = s2 * 10
            c2 = "㉠㉡$$수식$$%s$$/수식$$㉢" % c1
            c2_josa = "과"
            c3 = s5 - 1
            s3, s4, num = random.sample(['천', '백', '일'], 3)
            if num == "천":
                h1, h2, h3 = "㉠", "㉡", "㉢"
                cor_text = "%s%s%s%s" % (9, c3, c1, 1)
                c5 = "%s%s%s%s" % (9, s5, c1, 0)
            else:
                # 천의 자리 숫자와 일의 자리 숫자의 합이 n인 경우 천의 자리에는 0이 올 수 없기 때문에 제외함
                continue
        else:
            c1 = s2
            c2 = "㉠㉡㉢$$수식$$%s$$/수식$$" % c1
            c2_josa = check_josa(c2)[0]
            c3 = s5 - 1
            s3, s4, num = random.sample(['천', '십', '백'], 3)
            if num == "천":
                h1, h2, h3 = "㉠", "㉡", "㉢"
                cor_text = "%s%s%s%s" % (9, c3, 1, c1)
                c5 = "%s%s%s%s" % (9, s5, 0, c1)
            else:
                # 천의 자리 숫자와 일의 자리 숫자의 합이 n인 경우 천의 자리에는 0이 올 수 없기 때문에 제외함
                continue

        if cor_text[0] != 0:
            s2_josa = check_josa(s2)[2]
            flag = False

    stem = stem.format(s1=s1, s2=s2, s2_josa=s2_josa, s3=s3, s4=s4, s5=s5, h1=h1, h2=h2, h3=h3)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s1=s1, s2=s2, s2_josa=s2_josa, c1=c1, c2=c2, c2_josa=c2_josa, s5=s5, c5=c5, c3=c3, cor_text=cor_text, h1=h1, h2=h2, h3=h3)

    if s3 == "천":
        result = []

    return stem, answer, comment








































# 2-2-1-21
def fourdigits221_Stem_016():
    stem = "수 카드를 한 번씩만 사용하여 네 자리 수를 만들려고 합니다. {s1}의 자리 숫자가 $$수식$${s2}$$/수식$$인 가장 큰 네 자리 수는 얼마인가요?\n$$수식$${a1}$$/수식$$  $$수식$${a2}$$/수식$$  $$수식$${a3}$$/수식$$  $$수식$${a4}$$/수식$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "{s1}의 자리 숫자가 $$수식$${s2}$$/수식$$인 네 자리 수는 $$수식$${c1}$$/수식$${c1_josa} 나타낼 수 있습니다.\n" \
              "남은 수 카드의 수를 비교하면 {c2}이므로 {c3}의 자리부터 $$수식$${box}$$/수식$$ 안에 큰 수를 차례대로 넣으면 $$수식$${cor_text}$$/수식$${cor_text_josa} 됩니다. " \
              "따라서 {s1}의 자리 숫자가 $$수식$${s2}$$/수식$$인 가장 큰 네 자리 수는 $$수식$${cor_text}$$/수식$$입니다.\n\n"

    box = '□'

    flag = True
    while flag:
        num_list = list(range(1, 10))
        s1 = random.choice(['일', '십', '백', '천'])
        s2 = random.choice(num_list)
        num_list.remove(s2)

        s3, s4, s5 = random.sample(num_list, 3)
        card_list = [s3, s4, s5]
        card_list.sort(reverse=True)

        if s1 == "천":
            c1 = "%s ` □ ` □ ` □" % s2
            c1_josa = "로"
            c2 = "$$수식$$" + "` &gt; `".join(map(str, card_list)) + "$$/수식$$"
            c3 = "백"
            cor_text = "%s%s" % (s2, "".join(map(str, card_list)))
        elif s1 == "백":
            c1 = "□ ` %s ` □ ` □" % s2
            c1_josa = "로"
            c2 = "$$수식$$" + "` &gt; `".join(map(str, card_list)) + "$$/수식$$"
            c3 = "천"
            cor_text = "%s%s%s%s" % (card_list[0], s2, card_list[1], card_list[2])
        elif s1 == "십":
            c1 = "□ ` □ ` %s ` □" % s2
            c1_josa = "로"
            c2 = "$$수식$$" + "` &gt; `".join(map(str, card_list)) + "$$/수식$$"
            c3 = "천"
            cor_text = "%s%s%s%s" % (card_list[0], card_list[1], s2, card_list[2])
        else:
            c1 = "□ ` □ ` □ ` %s" % s2
            c1_josa = check_josa(s2)[4]
            c2 = "$$수식$$" + "` &gt; `".join(map(str, card_list)) + "$$/수식$$"
            c3 = "천"
            cor_text = "%s%s%s%s" % (card_list[0], card_list[1], card_list[2], s2)

        if 1000 < int(cor_text) < 10000:
            flag = False
            cor_text_josa = check_josa(cor_text)[3]

    # 카드 등장 순서 셔플
    while True:
        answers = [s2, s3, s4, s5]
        random.shuffle(answers)
        if "".join(map(str, answers)) != cor_text:
            break

    box_num = ['box{``%d``}' % a for a in answers]
    a1, a2, a3, a4 = box_num
    stem = stem.format(s1=s1, s2=s2, a1=a1, a2=a2, a3=a3, a4=a4)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s1=s1, s2=s2, c1=c1, c2=c2, c3=c3, cor_text=cor_text, c1_josa=c1_josa, cor_text_josa=cor_text_josa, box=box)

    return stem, answer, comment

































# 2-2-1-22
def fourdigits221_Stem_017():
    '''
    :param r1: 보기에 등장하는 수의 최솟값 [int] {3:4}
    :param r2: 보기에 등장하는 수의 최댓값 [int] {5:6}
    '''
    stem = "다음 수들은 얼마씩 뛰어 센 것인지 구해 보세요.\n$$표$$$$수식$${a1}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${c3}$$/수식$$\n"
    comment = "(해설)\n" \
              "{c1}의 자리 숫자가 $$수식$${c2}$$/수식$$씩 커지므로 $$수식$${c3}$$/수식$$씩 뛰어 센 것입니다.\n\n"


    r1 = 3
    r2 = 5


    flag = True
    
    while flag:
        # 보기에 나오는 숫자 개수와 처음 시작하는 seed 설정
        count = random.randint(r1, r2)
        seed = random.randint(1000, 6000)

        # 건너뛰는 수의 단위 설정
        c1 = random.choice(['천', '백', '십'])
        c2 = random.randint(1, 9)
        if c1 == "천":
            c2 = random.randint(1, 3)
            c3 = c2 * 1000
        elif c1 == "백":
            c3 = c2 * 100
        else:
            c3 = c2 * 10

        # count만큼 반복하며 뛰어 세는 수 리스트 완성
        answers = [seed]
        tmp = seed + c3
        for _ in range(count):
            if tmp > 10000:
                break
            answers.append(tmp)
            tmp += c3

        a1 = " ~ - ~ ".join(map(str, answers))

        if r1 <= len(answers) <= r2:
            flag = False

    stem = stem.format(a1=a1)
    answer = answer.format(c3=c3)
    comment = comment.format(c1=c1, c2=c2, c3=c3)

    return stem, answer, comment




# 2-2-1-23
def fourdigits221_Stem_018():
    '''
    :param r1: s1의 최솟값 [int] {1000:1001}
    :param r2: s1의 최댓값 [int] {9998:9999}
    '''
    stem = "바닥에 $$수식$${s1}$$/수식$$부터 $$수식$${s2}$$/수식$$씩 커지는 수 카드가 놓여 있습니다. 빈 카드에 알맞은 수를 써넣으세요.\n{a}\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${s1}$$/수식$$부터 $$수식$${s2}$$/수식$$씩 뛰어 세면 \n" \
              "$$수식$${c1}$$/수식$$입니다.\n" \
              "따라서 빈 카드에 알맞은 수는 $$수식$${cor_text}$$/수식$$입니다.\n\n"


    r1 = 1000
    r2 = 9998


    flag = True
    
    while flag:
        s1 = random.randint(r1, r2)
        s2 = random.choice([10, 100, 1000])

        # 숫자 카드 리스트 생성
        answers = [s1]
        tmp = s1 + s2
        for _ in range(6):
            if tmp > 10000:
                break
            answers.append(tmp)
            tmp += s2

        # 해설 작성
        c1 = " ~ - ~ ".join(map(str, answers))

        if len(answers) == 7:
            # 정답 고르기
            index = random.randint(1, 5)
            cor_text = answers[index]
            answers[index] = '　　　'
            #random.shuffle(answers)

            # 보기 만들기
            a1, a2, a3, a4, a5, a6, a7 = answers
            a = "$$수식$$BOX{`%s`}$$/수식$$   $$수식$$BOX{`%s`}$$/수식$$   " \
                 "$$수식$$BOX{`%s`}$$/수식$$   $$수식$$BOX{`%s`}$$/수식$$   $$수식$$BOX{`%s`}$$/수식$$   " \
                 "$$수식$$BOX{`%s`}$$/수식$$   $$수식$$BOX{`%s`}$$/수식$$" % (a1, a2, a3, a4, a5, a6, a7)

            flag = False

    stem = stem.format(s1=s1, s2=s2, a=a)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s1=s1, s2=s2, c1=c1, cor_text=cor_text)

    return stem, answer, comment






























# 2-2-1-24
def fourdigits221_Stem_019():
    '''
    :param r1: s1의 최솟값 [int] {1000:1001}
    :param r2: s1의 최댓값 [int] {5999:6000}
    :param r3: s3의 최솟값 [int] {3:4}
    :param r4: s3의 최댓값 [int] {6:7}
    '''
    stem = "$$수식$${s1}$$/수식$$부터 $$수식$${s2}$$/수식$$씩 $$수식$${s3}$$/수식$$번 {q1} 센 수를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${s1}$$/수식$$부터 $$수식$${s2}$$/수식$$씩 {q1} 세면\n" \
              "$$수식$${c1}$$/수식$$입니다.\n\n"


    r1 = 1000
    r2 = 5999
    r3 = 3
    r4 = 6


    flag = True
    
    while flag:
        s1 = random.randint(r1, r2)
        s2 = random.choice([10, 100, 1000])
        s3 = random.randint(r3, r4)

        q1 = random.choice(['뛰어', '빼서'])

        num_list = [s1]
        if q1 == "뛰어":
            tmp = s1 + s2
            for _ in range(s3):
                if tmp > 10000:
                    break
                num_list.append(tmp)
                tmp += s2
        else:
            tmp = s1 - s2
            for _ in range(s3):
                if tmp < 0:
                    break
                num_list.append(tmp)
                tmp -= s2

        if len(num_list) == s3 + 1:
            flag = False

            c1 = " ~ - ~ ".join(map(str, num_list))
            cor_text = num_list[-1]

    stem = stem.format(s1=s1, s2=s2, s3=s3, q1=q1)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s1=s1, s2=s2, c1=c1, q1=q1)

    return stem, answer, comment

































# 2-2-1-25
def fourdigits221_Stem_020():
    '''
    :param r1: s1의 최솟값 [int] {100:101}
    :param r2: s1의 최댓값 [int] {499:599}
    :param r3: s3의 최솟값 [int] {3:4}
    :param r4: s3의 최댓값 [int] {6:7}
    '''
    stem = "{t1}{t1_josa1} $$수식$${s1}$$/수식$$원을 가지고 있습니다. 내일부터 {s3}일 동안 하루에 $$수식$${s2}$$/수식$$원씩 계속 {q1} {t1}{t1_josa2} 가진 돈은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "{s3}일 동안 하루에 $$수식$${s2}$$/수식$$원씩 {q2} $$수식$${s1}$$/수식$$원에서 $$수식$${s2}$$/수식$$씩 $$수식$${c2}$$/수식$$번 뛰어 셉니다.\n" \
              "$$수식$${c1}$$/수식$$입니다.\n\n"


    r1 = 100
    r2 = 599
    r3 = 3
    r4 = 7


    flag = True
    
    while flag:
        t1 = random.choice(person_yeo+person_nam)
        if josa_check(t1[-1]) == ' ':
            t1_josa1 = '는'
            t1_josa2 = '가'
        else:
            t1_josa1 = '이는'
            t1_josa2 = '이가'

        s1 = random.randint(r1, r2) * 10
        s2 = random.choice([10, 100, 1000])
        s3 = random.randint(r3, r4)
        c2 = s3

        num_list = [s1]
        tmp = s1 + s2
        for _ in range(s3):
            if tmp > 10000:
                break
            num_list.append(tmp)
            tmp += s2

        if len(num_list) == s3 + 1:
            flag = False

            c1 = " ~ - ~ ".join(map(str, num_list))
            cor_text = num_list[-1]

    if s3 == 7:
        s3 = "일주"
    else:
        s3 = "$$수식$$%s$$/수식$$" % s3

    q1 = random.choice(['저금한다면', '모은다면'])
    if q1 == "저금한다면" :
        q2 = "저금하므로"
    else :
        q2 = "모았으므로"

    stem = stem.format(t1=t1, t1_josa1=t1_josa1, t1_josa2=t1_josa2, s1=s1, s2=s2, s3=s3, q1=q1)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(s1=s1, s2=s2, s3=s3, c1=c1, c2=c2, q1=q1, q2=q2)

    return stem, answer, comment


























# 2-2-1-28
def fourdigits221_Stem_021():
    stem = "두 수의 크기를 비교하여 □ 안에 $$수식$$&gt;$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${s1} ~ $$/수식$$$$수식$${box}$$/수식$$$$수식$$ ~ {s2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$\n"
    comment = "(해설)\n" \
              "{c1}의 자리 수를 비교하면 $$수식$${c3} ` {cor_text} ` {c4}$$/수식$$이므로 $$수식$${s1} ` {cor_text} ` {s2}$$/수식$$입니다.\n\n"

    box = 'box{　}'
    flag = True
    while flag:
        diff = random.choice([10, 100])
        a = random.randint(1000, 9999)

        if diff == 10:
            plus_num = random.randint(1, 9)
            num = int(str(a)[2])
            if str(a)[2] != 9 and num + plus_num < 10:
                b = a + (10 * plus_num)
                c1 = "천의 자리, 백의 자리 수는 같으므로 십"
                # a, b 셔플
                a, b = random.sample([a, b], 2)
                c3 = int(str(a)[2])
                c4 = int(str(b)[2])
            else:
                continue
        else:
            plus_num = random.randint(1, 9)
            num = int(str(a)[1])
            if str(a)[1] != 9 and num + plus_num < 10:
                b = a + (100 * plus_num)
                c1 = "천의 자리 수는 같으므로 백"
                # a, b 셔플
                a, b = random.sample([a, b], 2)
                c3 = int(str(a)[1])
                c4 = int(str(b)[1])
            else:
                continue

        if c3 < c4:
            cor_text = "&lt;"
        else:
            cor_text = "&gt;"

        if a < 10000 and b < 10000:
            flag = False

    stem = stem.format(s1=a, s2=b, box=box)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1, c3=c3, c4=c4, s1=a, s2=b, cor_text=cor_text)

    return stem, answer, comment

































# 2-2-1-29
def fourdigits221_Stem_022():
    '''
    :param r1: s1의 최솟값 [int] {1000:1001}
    :param r2: s1의 최댓값 [int] {5999:6000}
    '''
    stem = "다음 중 $$수식$${s1}$$/수식$$보다 {q1} 수는 몇 개인지 구해 보세요.\n$$표$$$$수식$${a}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${c1}$$/수식$$\n" \
              "$$수식$${s1}$$/수식$$보다 {q1} 수는 $$수식$${c2}$$/수식$${c2_josa} $$수식$${cor_text}$$/수식$$개입니다.\n\n"


    r1 = 1000
    r2 = 5999


    flag = True

    while flag:
        q1 = random.choice(["큰", "작은"])

        s1 = random.randint(r1, r2)
        count = random.randint(3, 4)

        # 보기 샘플 만들기
        answers = []
        # 10
        for _ in range(3):
            plus = s1 + (10 * random.randint(1, 5))
            minus = s1 - (10 * random.randint(1, 5))
            if 0 < plus < 10000:
                answers.append(plus)
            if 0 < minus < 10000:
                answers.append(minus)

        # 100
        for _ in range(3):
            plus = s1 + (100 * random.randint(1, 5))
            minus = s1 - (100 * random.randint(1, 5))
            if 0 < plus < 10000:
                answers.append(plus)
            if 0 < minus < 10000:
                answers.append(minus)

        # 1000
        for _ in range(3):
            plus = s1 + (1000 * random.randint(1, 5))
            minus = s1 - (1000 * random.randint(1, 5))
            if 0 < plus < 10000:
                answers.append(plus)
            if 1000 < minus < 10000:
                answers.append(minus)

        random.shuffle(answers)
        if len(answers) >= count:
            answers = random.sample(answers, count)

            comments, cor_list = [], []
            cor_text = 0
            for ans in answers:
                if ans < s1:
                    comments.append("%s &lt; %s" % (ans, s1))
                    if q1 == "작은":
                        cor_text += 1
                        cor_list.append(ans)
                else:
                    comments.append("%s &gt; %s" % (ans, s1))
                    if q1 == "큰":
                        cor_text += 1
                        cor_list.append(ans)

            if len(cor_list) >= 1 and len(answers) == len(set(answers)):
                flag = False

                c1 = "$$/수식$$, $$수식$$".join(comments)
                c2 = "$$/수식$$, $$수식$$".join(map(str, cor_list))
                c2_josa = check_josa(cor_list[-1])[4]

                random.shuffle(answers)
                a = "$$/수식$$, $$수식$$".join(map(str, answers))

    stem = stem.format(s1=s1, a=a, q1=q1)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1, c2=c2, c2_josa=c2_josa, cor_text=cor_text, s1=s1, q1=q1)

    return stem, answer, comment






























# 2-2-1-30
def fourdigits221_Stem_023():
    stem = "{q1} 수부터 차례대로 기호를 써 보세요.\n$$표$$㉠ $$수식$${a1}$$/수식$$    ㉡ $$수식$${a2}$$/수식$$    ㉢ $$수식$${a3}$$/수식$$    ㉣ $$수식$${a4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{cor_text}\n"
    comment = "(해설)\n" \
              "천의 자리 수가 $$수식$${c1}$$/수식$$인 수를 비교하면 \n" \
              "$$수식$${c2}$$/수식$$입니다.\n" \
              "천의 자리 수가 $$수식$${c3}$$/수식$$인 수를 비교하면\n" \
              "$$수식$${c4}$$/수식$$입니다.\n" \
              "따라서 네 수의 크기를 비교하면\n" \
              "$$수식$${c5}$$/수식$$이므로 {q1} 수부터 차례대로 기호를 쓰면 {cor_text}입니다.\n\n"

    flag = True
    while flag:
        q1 = random.choice(['큰', '작은'])

        s1 = random.randint(1000, 9999)
        s2 = random.randint(1000, 9999)

        if s1 // 1000 != s2 // 1000:
            mul_s1 = random.choice([1, 10, 100])
            mul_s2 = random.choice([1, 10, 100])
            s3 = s1 + (mul_s1 * random.randint(1, 8))
            s4 = s2 + (mul_s2 * random.randint(1, 8))

            if s1 // 1000 == s3 // 1000 and s2 // 1000 == s4 // 1000:
                c1 = s1 // 1000
                s1, s3 = random.sample([s1, s3], 2)
                if s1 < s3:
                    c2 = "%s ` &lt; ` %s" % (s1, s3)
                else:
                    c2 = "%s ` &gt; ` %s" % (s1, s3)

                c3 = s2 // 1000
                s2, s4 = random.sample([s2, s4], 2)
                if s2 < s4:
                    c4 = "%s ` &lt; ` %s" % (s2, s4)
                else:
                    c4 = "%s ` &gt; ` %s" % (s2, s4)

                # 보기 생성
                answers = [s1, s2, s3, s4]
                random.shuffle(answers)
                a1, a2, a3, a4 = answers

                # 순서대로 정렬
                num_list = sorted(answers, reverse=False)
                c5 = " ` &lt; ` ".join(map(str, num_list))

                # 기호 설정
                if q1 == "작은":
                    num_list = sorted(answers, reverse=True)
                comments = []
                for i, num in enumerate(num_list):
                    comments.insert(0, multiple_choice_hangul[answers.index(num)])
                cor_text = ", ".join(comments)

                flag = False

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, q1=q1)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, q1=q1, cor_text=cor_text)

    return stem, answer, comment




































# 2-2-1-31
def fourdigits221_Stem_024():
    stem = "나타내는 수가 더 {q1} 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${s1}$$/수식$$부터 $$수식$${s2}$$/수식$$씩 $$수식$${s3}$$/수식$$번 뛰어 센 수\n㉡ $$수식$${s4}$$/수식$$부터 $$수식$${s5}$$/수식$$씩 $$수식$${s6}$$/수식$$번 뛰어 센 수$$/표$$\n"
    answer = "(정답)\n{cor_num}\n"
    comment = "(해설)\n" \
              "$$수식$${s1}$$/수식$$부터 $$수식$${s2}$$/수식$$씩 $$수식$${s3}$$/수식$$번 뛰어 세면\n" \
              "$$수식$${c1}$$/수식$$이므로 ㉠$$수식$$`=` {c2}$$/수식$$입니다.\n" \
              "$$수식$${s4}$$/수식$$부터 $$수식$${s5}$$/수식$$씩 $$수식$${s6}$$/수식$$번 뛰어 세면\n" \
              "$$수식$${c3}$$/수식$$이므로 ㉡$$수식$$`=` {c4}$$/수식$$입니다.\n" \
              "따라서 $$수식$${c5}$$/수식$$이므로 {cor_num}이 더 {q2}.\n\n"

    flag = True
    while flag:
        q1, q2 = random.choice([('큰', '큽니다'), ('작은', '작습니다')])

        # s1/s4부터 s2/s5씩 s3/s6번 뛰어 센 수
        s1 = random.randrange(1000, 9990, 10)
        s4 = random.randrange(1000, 9990, 10)

        tmp = random.choice([10, 100])
        s2 = tmp * random.randint(2, 5)
        s5 = tmp * random.randint(2, 5)

        s3, s6 = random.sample(list(range(3, 7)), 2)

        if s1 != s4 and s2 != s5 and s3 != s6:
            a_list = [s1]
            a_num = s1 + s2
            for _ in range(s3+1):
                if a_num >= 10000:
                    break
                a_list.append(a_num)
                a_num += s2

            b_list = [s4]
            b_num = s4 + s5
            for _ in range(s6+1):
                if b_num >= 10000:
                    break
                b_list.append(b_num)
                b_num += s5

            if len(a_list) == s3+1 and len(b_list) == s6+1:
                c1 = " ~ - ~ ".join(map(str, a_list))
                c3 = " ~ - ~ ".join(map(str, b_list))

                c2 = a_list[-1]
                c4 = b_list[-1]

                if c2 > c4:
                    c5 = "%s `&gt;` %s" % (c2, c4)
                    if q1 == "큰":
                        cor_num = multiple_choice_hangul[0]
                    else:
                        cor_num = multiple_choice_hangul[1]
                    flag = False
                elif c2 < c4:
                    c5 = "%s `&lt;` %s" % (c2, c4)
                    if q1 == "큰":
                        cor_num = multiple_choice_hangul[1]
                    else:
                        cor_num = multiple_choice_hangul[0]
                    flag = False

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, q1=q1)
    answer = answer.format(cor_num=cor_num)
    comment = comment.format(q2=q2, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, cor_num=cor_num)

    return stem, answer, comment

































# 2-2-1-32
def fourdigits221_Stem_025():
    '''
    :param r1: s1의 최솟값 [int] {1000:1001}
    :param r2: s1의 최댓값 [int] {9998:9999}
    '''
    stem = "네 자리 수의 크기를 비교했습니다. $$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 중에서 $$수식$${box}$$/수식$$ 안에 들어갈 수 있는 수는 모두 몇 개인가요?\n$$표$$$$수식$${a1}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${cor_text}$$/수식$$개\n"
    comment = "(해설)\n" \
              "{c1} 같으므로 {c2}의 자리 수를 비교하면 $$수식$${c3}$$/수식$$입니다.\n" \
              "따라서 $$수식$${box}$$/수식$$ 안에 들어갈 수 있는 수는 $$수식$${c4}$$/수식$${c4_josa} 모두 $$수식$${cor_text}$$/수식$$개입니다.\n\n"


    r1 = 1000
    r2 = 9998


    box = '□'
    
    flag = True
    
    while flag:
        s1 = random.randint(r1, r2)
        s2 = random.choice(['천', '백', '십'])

        ineq = random.choice(['&lt;', '&gt;'])      # &gt; > / &lt; <

        # 부등호 표시에 맞추어서  box 안에 들어갈 수 있는 수 지정
        if ineq == "&lt;":
            s3 = random.randint(2, 6)
            num_list = list(range(s3+1, 10))
        else:
            s3 = random.randint(5, 9)
            num_list = list(range(1, s3))

        # 빈칸 위치에 맞는 해설, 보기 설정하고 s1 수정
        if s2 == "천":
            s1 = str(s1)[0] + str(s3) + str(s1)[2:]
            c1 = "천의 자리 수가"
            c2 = "백"
            c3 = "%s ` %s ` □ `" % (str(s1)[1], ineq)
            a1 = "%s ` %s ` %s ` □ ` %s" % (s1, ineq, str(s1)[0], str(s1)[2:])
        elif s2 == "백":
            s1 = str(s1)[:2] + str(s3) + str(s1)[-1]
            c1 = "천의 자리, 백의 자리 수가 각각"
            c2 = "십"
            c3 = "%s ` %s ` □ `" % (str(s1)[2], ineq)
            a1 = "%s ` %s ` %s ` □ ` %s" % (s1, ineq, str(s1)[0:2], str(s1)[3])
        elif s2 == "십":
            s1 = str(s1)[:3] + str(s3)
            c1 = "천의 자리, 백의 자리, 십의 자리 수가 각각"
            c2 = "일"
            c3 = "%s ` %s ` □ `" % (str(s1)[3], ineq)
            a1 = "%s ` %s ` %s ` □" % (s1, ineq, str(s1)[:3])

        if len(num_list) > 0:
            flag = False
            c4 = "$$/수식$$, $$수식$$".join(map(str, num_list))
            c4_josa = check_josa(num_list[-1])[4]
            cor_text = len(num_list)

    stem = stem.format(a1=a1, box=box)
    answer = answer.format(cor_text=cor_text)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c4_josa=c4_josa, cor_text=cor_text, box=box)

    return stem, answer, comment






# if __name__ == '__main__':
#     FourDigitNum_Stem_001()
#     FourDigitNum_Stem_002()
#     FourDigitNum_Stem_003()
#     FourDigitNum_Stem_004()
#     FourDigitNum_Stem_005()
#     FourDigitNum_Stem_006()
#     FourDigitNum_Stem_007()
#     FourDigitNum_Stem_008()
#     FourDigitNum_Stem_009()
#     FourDigitNum_Stem_010()
#     FourDigitNum_Stem_011()
#     FourDigitNum_Stem_012()
#     FourDigitNum_Stem_013()
#     FourDigitNum_Stem_014()
#     FourDigitNum_Stem_015()
#     FourDigitNum_Stem_016()
#     FourDigitNum_Stem_017()
#     FourDigitNum_Stem_018()
#     FourDigitNum_Stem_019()
#     FourDigitNum_Stem_020()
#     FourDigitNum_Stem_021()
#     FourDigitNum_Stem_022()
#     FourDigitNum_Stem_023()
#     FourDigitNum_Stem_024()
#     FourDigitNum_Stem_025()





