import numpy as np

answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤"
}

answer_kodict = {
    0: "㉠",
    1: "㉡",
    2: "㉢",
    3: "㉣",
    4: "㉤"
}

def bool_jo(num):
    if type(num) == int:
        num = int(str(num)[-1])

        lee_nums = [0, 1, 3, 6, 7, 8]
        if num in lee_nums:
            return True
        else:
            return False
    else:
        num = str(num)[-1]
        num = ord(num)
        check = (num - 44032) % 28
        if check:
            return True
        return False


def proc_jo(num, check=0):
    if check < 0:
        # 은는
        if bool_jo(num):
            return "은"
        return "는"
    elif check == 0:
        # 이가
        if bool_jo(num):
            return "이"
        return "가"
    elif check == 2:
        # 와과
        if bool_jo(num):
            return "과"
        return "와"
    elif check == 3:
        #이(라고)
        if bool_jo(num):
            return "이"
        return ""
    elif bool_jo(num):
        # 을를
        return "을"
    return "를"




def uptohun121_Stem_001(): #1-2-1-03
    stem = "□ 안에 알맞은 수를 써넣으세요.\n(1) $$수식$${x1}$$/수식$${j1} $$수식$$10$$/수식$$개씩 묶음 $$수식$${boxone}$$/수식$$개입니다.\n(2) $$수식$${boxtwo}$$/수식$$은 $$수식$$10$$/수식$$개씩 묶음 $$수식$${x2}$$/수식$$개입니다.\n"
    answer = "(정답)\n① $$수식$${a1}$$/수식$$, ② $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n$$수식$$LEFT ( 1 RIGHT ) ```` {x1}$$/수식$$ → $$수식$$10$$/수식$$개씩 묶음 $$수식$${a1}$$/수식$$개\n"\
              "$$수식$$LEFT ( 2 RIGHT ) ```` 10$$/수식$$개씩 묶음 $$수식$${x2}$$/수식$$개 → $$수식$${a2}$$/수식$$\n\n"

    a1 = np.random.randint(1, 11)
    x1 = a1 * 10

    x2 = np.random.randint(1, 11)
    while (x1 == a1) :
        x2 = np.random.randint(1, 11)
    a2 = x2 * 10

    boxone = "BOX{````①````}"
    boxtwo = "BOX{````②````}"

    j1 = proc_jo(x1, -1)
    stem = stem.format(x1 = x1, x2 = x2, j1 = j1, boxone = boxone, boxtwo = boxtwo) # 매핑시키기
    answer = answer.format(a1 = a1, a2 = a2)
    comment = comment.format(x1 = x1, x2 = x2, a1 = a1, a2 = a2)

    return stem, answer, comment



def uptohun121_Stem_002(): #1-2-1-05
    stem = "나타내는 수가 나머지와 다른 것을 찾아 기호를 써보세요.\n$$표$$ ㉠ {x1}, ㉡ {x2}, ㉢ {x3}, ㉣{x4} $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n$$수식$${y2}$$/수식$$ → {y1}, {y4}\n"\
              "$$수식$${x5}$$/수식$$ → {y3}, {x6}\n"\
              "따라서 나타내는 수가 나머지와 다른 것은 {a1}{y3}입니다.\n\n"

    s_list = ['열', '스물', '서른', '마흔', '쉰', '예순', '일흔', '여든', '아흔']
    s2_list = ['십', '이십', '삼십', '사십', '오십', '육십', '칠십', '팔십', '구십']

    r1 = np.random.randint(0, 9)
    r2 = np.random.randint(0, 9)
    while r1 == r2 :
        r2 = np.random.randint(0, 9)

    y1 = s_list[r1]
    y2 = "$$수식$$"+str((r1+1) * 10) + "$$/수식$$"
    y3 = s_list[r2]
    y4 = s2_list[r1]

    x5 = (r2+1) * 10
    x6 = s2_list[r2]

    candidates = [y1, y2, y3, y4]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):       #[a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y3 :
            correct_idx = idx
            break

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4)  # 매핑시키기
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(y1 = y1, y2 = y2, y3 = y3, y4 = y4, x5 = x5, x6 = x6, x3 = x3, a1 = answer_kodict[correct_idx])

    return stem, answer, comment



def uptohun121_Stem_003(): #1-2-1-10
    stem = "다음 수를 두 가지 방법으로 읽어 보세요.\n$$표$$$$수식$${x1}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{a1}, {a2}\n"
    comment = "(해설)\n$$수식$${x1}$$/수식$${j1} {a1} 또는 {a2}{j2}라고 읽습니다.\n\n"

    s_list = ['십', '이십', '삼십', '사십', '오십', '육십', '칠십', '팔십', '구십']
    s2_list = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    s3_list = ['열', '스물', '서른', '마흔', '쉰', '예순', '일흔', '여든', '아흔']
    s4_list = ['', '하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉']

    x1 = np.random.randint(10, 100)
    t1 = x1 // 10
    t2 = x1 % 10

    a1 = s_list[t1-1] + s2_list[t2]
    a2 = s3_list[t1-1] + s4_list[t2]
    j1 = proc_jo(x1, -1)
    j2 = proc_jo(a2, 3)

    stem = stem.format(x1 = x1)  # 매핑시키기
    answer = answer.format(a1= a1, a2 = a2)
    comment = comment.format(x1 = x1, j1 = j1, j2 = j2, a1 = a1, a2 = a2)

    return stem, answer, comment



def uptohun121_Stem_004(): #1-2-1-12
    stem = "잘못 짝 지어진 것을 찾아 기호를 써 보세요.\n$$표$$㉠ {x1}\n㉡ {x2}\n㉢ {x3}\n㉣ {x4}$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n$$수식$${y3}$$/수식$$ → {s1}, {s2}\n\n"


    s_list = ['십', '이십', '삼십', '사십', '오십', '육십', '칠십', '팔십', '구십']
    s2_list = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    s3_list = ['열', '스물', '서른', '마흔', '쉰', '예순', '일흔', '여든', '아흔']
    s4_list = ['', '하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉']

    r1 = np.random.randint(11, 100)
    while (r1 % 10 == 0):
        r1 = np.random.randint(11, 100)
    r2 = np.random.randint(11, 100)
    while r1 == r2 or (r2 % 10 == 0):
        r2 = np.random.randint(11, 100)
    r3 = np.random.randint(11, 100)
    while r2 == r3 or (r3 % 10 == 0):
        r3 = np.random.randint(11, 100)
    r4 = np.random.randint(11, 100)
    while r3 == r4 or (r4 % 10 == 0):
        r4 = np.random.randint(11, 100)

    t1 = r1 // 10
    t2 = r1 % 10
    y1 = "$$수식$$"+ str(r1) + "$$/수식$$ - " + s_list[t1 - 1]+s2_list[t2] + " - " + s3_list[t1 - 1] + s4_list[t2]

    t1 = r2 // 10
    t2 = r2 % 10
    y2 = "$$수식$$"+str(r2) + "$$/수식$$ - " + s_list[t1 - 1]+s2_list[t2] + " - " + s3_list[t1 - 1] + s4_list[t2]

    t1 = r3 // 10
    t2 = r3 % 10
    y3 = "$$수식$$"+str(r3) + "$$/수식$$ - " + s_list[t1 - 1]+s4_list[t2] + " - " +s3_list[t1 - 1] + s2_list[t2]
    s1 = s_list[t1 - 1] + s2_list[t2]
    s2 = s3_list[t1 - 1] + s4_list[t2]

    t1 = r4 // 10
    t2 = r4 % 10
    y4 = "$$수식$$"+str(r4) + "$$/수식$$ - " + s_list[t1 - 1]+s2_list[t2] + " - " + s3_list[t1 - 1] + s4_list[t2]

    candidates = [y1, y2, y3, y4]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):       #[a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y3 :
            correct_idx = idx
            break

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4)  # 매핑시키기
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(y3 = r3, s1 = s1, s2 = s2)

    return stem, answer, comment



def uptohun121_Stem_005(): #1-2-1-13
    stem = "{s1}{j1} $$수식$$10$$/수식$$개씩 묶음 $$수식$${x1}$$/수식$$개와 낱개 $$수식$${x2}$$/수식$$개 있습니다. {s1}{j2} 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n낱개 $$수식$${x2}$$/수식$$개는 $$수식$$10$$/수식$$개씩 묶음 $$수식$${x3}$$/수식$$개와 낱개 $$수식$${x4}$$/수식$$개 입니다. "\
              "따라서 $$수식$$10$$/수식$$개씩 묶음 $$수식$${x1}$$/수식$$개와 낱개 $$수식$${x2}$$/수식$$개는 $$수식$$10$$/수식$$개씩 묶음 $$수식$${x5}$$/수식$$개와 낱개 $$수식$${x4}$$/수식$$개와 같으므로 " \
              "{s1}{j2} 모두 $$수식$${a1}$$/수식$$개입니다.\n\n"

    s1 = ['빵', '음료수', '물감', '스티커'][np.random.randint(0,4)]
    j1 = proc_jo(s1, 0)
    j2 = proc_jo(s1, -1)
    x1 = np.random.randint(1, 10)
    x2 = np.random.randint(1, 100-x1*10)
    a1 = x1*10 + x2
    x3 = x2 // 10
    x4 = x2 % 10
    x5 = x1 + x3

    stem = stem.format(s1 = s1, j1 = j1, j2 = j2, x1 = x1, x2 = x2)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x2 = x2, x3 = x3, x4 = x4, x1 = x1, x5 = x5, s1 = s1, j2 = j2, a1 = a1)

    return stem, answer, comment



def uptohun121_Stem_006(): #1-2-1-15
    stem = "수를 잘못 읽은 것을 찾아 기호를 써 보세요.\n$$표$$㉠ {x1}\n㉡ {x2}\n㉢ {x3}$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n번호를 나타낼 때에는 $$수식$${x4}$$/수식$${j1} {s3}{j2}라고 읽으므로 {wh1}의 번호는 {s3} 번으로 읽어야 합니다.\n\n"

    wh1 = ['성희', '유나', '혜정이', '정윤이'][np.random.randint(0,4)]
    s1 = ['색연필', '연필', '볼펜'][np.random.randint(0,3)]
    s2 = ['영화관', '우리 반', '은정이네 집', '피아노 학원'][np.random.randint(0,4)]

    s_list = ['십', '이십', '삼십', '사십', '오십', '육십', '칠십', '팔십', '구십']
    s2_list = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    s3_list = ['열', '스물', '서른', '마흔', '쉰', '예순', '일흔', '여든', '아흔']
    s4_list = ['', '하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉']

    r1 = np.random.randint(11, 100)
    r2 = np.random.randint(11, 100)
    r3 = np.random.randint(11, 100)

    t1 = r1 // 10
    t2 = r1 % 10
    n1 = s3_list[t1-1] + s4_list[t2]
    s3 = s_list[t1 - 1] + s2_list[t2]

    t1 = r2 // 10
    t2 = r2 % 10
    n2 = s_list[t1 - 1] + s2_list[t2]

    t1 = r3 // 10
    t2 = r3 % 10
    n3 = s_list[t1 - 1] + s2_list[t2]

    y1 = f"{wh1}의 번호는 {n1} 번입니다."
    y2 = f"{s1}은 {n2} 자루입니다."
    y3 = f"{s2}은 {n3} 층에 있습니다."
    j1 = proc_jo(r1, 1)
    j2 = proc_jo(s3, 3)

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [x1, x2, x3] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y1:
            correct_idx = idx
            break

    stem = stem.format(x1=x1, x2=x2, x3=x3)  # 매핑시키기
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(x4 = r1, j1 = j1, j2 = j2, s3 = s3, wh1 = wh1)

    return stem, answer, comment



def uptohun121_Stem_007():  # 1-2-1-16
    stem = "다음은 {wh}의 일기입니다. 밑줄 친 ㉠과 ㉡을 숫자로 나타내어 보세요.\n$$표$$오늘 학교에서 $$수식$$99$$/수식$$까지의 수를 배웠다. 집에 오는 길에 준비물을 사려고 문방구에 들려 색종이를 모두 ㉠ $$수식$${underlineone}$$/수식$$ 장을 샀다. 집에 돌아와 내가 이때까지 접은 {s1}{j1} 세어 보니 모두 ㉡ $$수식$${underlinetwo}$$/수식$$ 개이었다.$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n{x1} → $$수식$${a1}$$/수식$$, {x2} → $$수식$${a2}$$/수식$$\n\n"

    wh = ['현지', '윤아', '세윤', '소희'][np.random.randint(0, 4)]
    s1 = ['종이학', '종이별', '장미꽃', '딱지'][np.random.randint(0, 4)]
    j1 = proc_jo(s1, 1)
    a1 = np.random.randint(11, 100)
    a2 = np.random.randint(11, 100)
    while a1 == a2:
        a2 = np.random.randint(11, 100)

    s_list = ['십', '이십', '삼십', '사십', '오십', '육십', '칠십', '팔십', '구십']
    s2_list = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    s3_list = ['열', '스물', '서른', '마흔', '쉰', '예순', '일흔', '여든', '아흔']
    s4_list = ['', '한', '두', '세', '네', '다섯', '여섯', '일곱', '여덟', '아홉']

    t1 = a1 // 10
    t2 = a1 % 10
    x1 = s_list[t1 - 1] + s2_list[t2]
    t1 = a2 // 10
    t2 = a2 % 10
    x2 = s3_list[t1 - 1] + s4_list[t2]

    if (a2 == 20):
        x2 = '스무'

    underlineone = "under{%s}" % x1
    underlinetwo = "under{%s}" % x2

    stem = stem.format(wh=wh, underlineone=underlineone, underlinetwo=underlinetwo, s1=s1, j1=j1)  # 매핑시키기
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(x1=x1, a2=a2, x2=x2, a1=a1)

    return stem, answer, comment




def uptohun121_Stem_008(): #1-2-1-18
    stem = "낱개의 수가 다른 하나를 찾아 기호를 써 보세요.\n$$표$$㉠ {x1}  ㉡ {x2}  ㉢ {x3}  ㉣ {x4} $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n{y1_}, {y3_}, {y4_}에서 {y1}, {y2}, {y3}{j1} 낱개의 수가 $$수식$${r0}$$/수식$$이고, "\
              "{y4}{j2} 낱개의 수가 $$수식$${r0_}$$/수식$$입니다.\n"\
              "따라서 낱개의 수가 다른 하나는 {y4}입니다.\n\n"

    s_list = ['십', '이십', '삼십', '사십', '오십', '육십', '칠십', '팔십', '구십']
    s2_list = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    s3_list = ['열', '스물', '서른', '마흔', '쉰', '예순', '일흔', '여든', '아흔']
    s4_list = ['', '하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉']

    r0 = np.random.randint(0, 10)
    r0_ = np.random.randint(1, 10)
    while (r0 == r0_):
        r0_ = np.random.randint(1, 10)

    r1 = np.random.randint(1, 10)
    r2 = np.random.randint(1, 10)
    while (r2 == r1) :
        r2 = np.random.randint(1, 10)
    r3 = np.random.randint(1, 10)
    while (r3 == r2):
        r3 = np.random.randint(1, 10)
    r4 = np.random.randint(1, 10)

    y1 = s3_list[r1-1] + s4_list[r0]
    y2 = "$$수식$$"+str(r2*10 + r0)+"$$/수식$$"
    y3 = s_list[r3-1] + s2_list[r0]
    y4 = s3_list[r4-1] + s4_list[r0_]

    candidates = [y1, y2, y3, y4]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y4:
            correct_idx = idx
            break

    y1_ = y1 +": $$수식$$"+ str(r1*10 + r0)+"$$/수식$$"
    y3_ = y3 +": $$수식$$"+ str(r3*10 + r0)+"$$/수식$$"
    y4_ = y4 +": $$수식$$"+ str(r4*10 + r0_)+"$$/수식$$"

    j1 = proc_jo(y3, -1)
    j2 = proc_jo(y4, -1)

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4 = x4)  # 매핑시키기
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(y1_ = y1_, y3_ = y3_, y4_ = y4_, y1 = y1, y2 = y2, y3 = y3, y4 = y4, r0 = r0, r0_ = r0_, j1 = j1, j2 = j2)

    return stem, answer, comment



def uptohun121_Stem_009(): #1-2-1-20
    stem = "▲에 알맞은 수를 구해 보세요.\n$$표$$$$수식$${boxone}$$/수식$$ - $$수식$${boxtwo}$$/수식$$ - $$수식$${boxthree}$$/수식$$ - $$수식$${boxfour}$$/수식$$ - $$수식$${boxfive}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1}$$/수식$$ - $$수식$${x2}$$/수식$$ - $$수식$${x3}$$/수식$$ - $$수식$${x4}$$/수식$$ - $$수식$${x5}$$/수식$$의 순서입니다.\n"\
              "따라서 ▲에 알맞은 수는 $$수식$${x5}$$/수식$$입니다.\n\n"

    x1 = np.random.randint(11, 96)
    x2 = x1 + 1
    x3 = x2 + 1
    x4 = x3 + 1
    x5 = a1 = x4 + 1

    boxone = "%s" % x1
    boxtwo = "%s" % x2
    boxthree = "%s" % x3
    boxfour = "□"
    boxfive = "▲"

    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour, boxfive=boxfive)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, a1 = a1)

    return stem, answer, comment



def uptohun121_Stem_010(): #1-2-1-24
    stem = "수의 순서를 거꾸로 하여 쓸 때 ㉠에 알맞은 수를 구해 보세요.\n$$표$$$$수식$${boxone}$$/수식$$ - $$수식$${boxtwo}$$/수식$$ - $$수식$${boxblank}$$/수식$$ - $$수식$${boxblank}$$/수식$$ - $$수식$${boxthree}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1}$$/수식$$부터 수의 순서를 거꾸로 하여 쓰면 $$수식$${x1}$$/수식$$, $$수식$${x2}$$/수식$$, $$수식$${x3}$$/수식$$, $$수식$${x4}$$/수식$$, $$수식$${x5}$$/수식$$입니다.\n\n"

    x1 = np.random.randint(14, 99)
    x2 = x1 - 1
    x3 = x2 - 1
    x4 = x3 - 1
    x5 = a1 = x4 - 1

    boxone = "%s" % x1
    boxtwo = "%s" % x2
    boxblank = "□"
    boxthree = "㉠"

    stem = stem.format(boxone = boxone, boxtwo = boxtwo, boxblank = boxblank, boxthree = boxthree)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, a1 = a1)

    return stem, answer, comment



def uptohun121_Stem_011(): #1-2-1-25
    stem = "알맞은 수를 찾아 빈칸에 써 보세요.\n$$표$$ $$수식$${x1}````{x2}````{x3}$$/수식$$ $$/표$$\n$$표$$・$$수식$${x4}$$/수식$$보다 $$수식$$1$$/수식$$ 작은 수 $$수식$${boxone}$$/수식$$\n・$$수식$${x5}$$/수식$$보다 $$수식$$1$$/수식$$ 큰 수 $$수식$${boxtwo}$$/수식$$$$/표$$\n"
    answer = "(정답)\n① $$수식$${a1}$$/수식$$, ② $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n・$$수식$${x4}$$/수식$$보다 $$수식$$1$$/수식$$ 작은 수는 $$수식$${x4}$$/수식$$ 바로 앞의 수이므로 $$수식$${x1}$$/수식$$입니다.\n"\
              "・$$수식$${x2}$$/수식$$보다 $$수식$$1$$/수식$$ 큰 수는 $$수식$${x2}$$/수식$$ 바로 뒤의 수이므로 $$수식$${x3}$$/수식$$입니다.\n\n"

    x4 = np.random.randint(11, 99)
    x5 = x4 + 1

    x1 = x4 - 1
    x2 = x5
    x3 = x5 + 1

    a1 = x1
    a2 = x3

    boxone = "BOX{````①````}"
    boxtwo = "BOX{````②````}"

    stem = stem.format(x1=x1, x2=x2, x3 = x3, x4 = x4, x5 = x5, boxone = boxone, boxtwo = boxtwo)  # 매핑시키기
    answer = answer.format(a1=a1, a2 = a2)
    comment = comment.format(x4 = x4, x1 = x1, x2 = x2, x3 = x3)

    return stem, answer, comment



def uptohun121_Stem_012(): #1-2-1-26
    stem = "설명하는 수를 써 보세요.\n$$표$$$$수식$$LEFT ($$/수식$$가$$수식$$RIGHT ) ```` {x1}$$/수식$$보다 $$수식$$1$$/수식$$ 큰 수입니다.\n$$수식$$LEFT ($$/수식$$나$$수식$$RIGHT ) ```` 10$$/수식$$개씩 묶음 $$수식$${x2}$$/수식$$개입니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n・ $$수식$${x1}$$/수식$$보다 $$수식$$1$$/수식$$ 큰 수는 $$수식$${x1}$$/수식$$ 바로 뒤의 수이므로 $$수식$${a1}$$/수식$$입니다.\n"\
              "・ $$수식$$10$$/수식$$개씩 묶음 $$수식$${x2}$$/수식$$개는 $$수식$${a1}$$/수식$$개입니다.\n\n"

    x1 = np.random.randint(1, 10)*10 + 9
    a1 = x1 + 1
    x2 = a1 // 10

    stem = stem.format(x1 = x1, x2 = x2)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1 = x1, x2 = x2, a1 = a1)

    return stem, answer, comment




def uptohun121_Stem_013(): #1-2-1-27
    stem = "수 카드의 수를 모았을 때 $$수식$$100$$/수식$$이 되는 두 수를 찾아 써 보세요.\n$$표$$$$수식$${boxone}````````{boxtwo}````````{boxthree}````````{boxfour}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n모아서 $$수식$$100$$/수식$$이 되는 두 수는 $$수식$${y1}$$/수식$${j1} $$수식$${y3}$$/수식$$입니다.\n\n"

    y1 = np.random.randint(1, 10)
    while y1 == 5:
        y1 = np.random.randint(1, 10)
    y3 = y2 = y4 = 10 - y1

    while y2 == y1 or y2 == y3 :
        y2 = np.random.randint(1, 10)

    while y4 == y1 or y4 == y3 or y4 == (10-y2) or y4 == y2:
        y4 = np.random.randint(1, 10)

    y1 = y1 * 10
    y2 = y2 * 10
    y3 = y3 * 10
    y4 = y4 * 10
    j1 = proc_jo(y1, 2)

    candidates = [y1, y2, y3, y4]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4] = candidates

    boxone = "%d" % x1
    boxtwo = "%d" % x2
    boxthree = "%d" % x3
    boxfour = "%d" % x4

    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour)  # 매핑시키기
    answer = answer.format(a1 = y1, a2 = y3)
    comment = comment.format(y1 = y1, j1 = j1, y3 = y3)

    return stem, answer, comment




def uptohun121_Stem_014(): #1-2-1-28
    stem = "$$수식$${x1}$$/수식$$과 $$수식$${x2}$$/수식$$ 사이에 있는 수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$ 개\n"
    comment = "(해설)\n$$수식$${x1}$$/수식$$부터 $$수식$${x2}$$/수식$$까지의 수를 순서대로 쓰면, {s1}입니다.\n"\
              "따라서 $$수식$${x1}$$/수식$${j1} $$수식$${x2}$$/수식$$ 사이에 있는 수는 {s2}로 모두 $$수식$${a1}$$/수식$$개입니다.\n\n"

    x1 = np.random.randint(11, 92)
    x2 = x1 + np.random.randint(2, 10)
    a1 = x2 - x1 - 1

    s1 = "$$수식$$"+str(x1) +"$$/수식$$, "
    s2 = ""

    for i in range(x1+1, x2):
        s1 = s1 + "$$수식$$"+str(i) + "$$/수식$$, "
        s2 = s2 + "$$수식$$"+str(i) + "$$/수식$$, "
    s1 = s1 + str(x2)
    s2 = s2[0:-2]

    j1 = proc_jo(x1, 2)
    stem = stem.format(x1 = x1, x2 = x2)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1 = x1, x2 = x2, s1 = s1, s2 = s2, j1 = j1, a1 = a1)

    return stem, answer, comment




def uptohun121_Stem_015(): #1-2-1-29
    stem = "$$수식$${boxblank}$$/수식$$ 안에 알맞은 수를 써넣으세요.\n$$표$$$$수식$${boxblank}$$/수식$$보다 $$수식$$1$$/수식$$ 큰 수는 $$수식$${x1}$$/수식$$입니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${boxblank}$$/수식$$보다 $$수식$$1$$/수식$$ 큰 수는 $$수식$${x1}$$/수식$$이므로 $$수식$${boxblank}$$/수식$$는 $$수식$${x1}$$/수식$$보다 $$수식$$1$$/수식$$ 작은 수입니다.\n"\
              "$$수식$${x1}$$/수식$$보다 $$수식$$1$$/수식$$ 작은 수는 $$수식$${x1}$$/수식$$ 바로 앞의 수이므로 $$수식$${boxblank}$$/수식$$안에 알맞은 수는 $$수식$${a1}$$/수식$$입니다.\n\n"

    x1 = np.random.randint(11, 99)
    a1 = x1 - 1

    boxblank = "□"

    stem = stem.format(x1 = x1, boxblank = boxblank)  # 매핑시키기
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, a1 = a1, boxblank = boxblank)

    return stem, answer, comment



def uptohun121_Stem_016(): #1-2-1-30
    stem = "{s1} 체험에서 {wh1}{j1} 뽑은 번호표의 수는 $$수식$${x1}$$/수식$${j2}고 {wh2}{j3} 뽑은 번호표의 수는 {wh1}{j1} 뽑은 번호표의 수보다 $$수식$$1$$/수식$$ {s2} 수 입니다. {wh2}{j3} 뽑은 번호표는 몇 번인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1}$$/수식$$보다 $$수식$$1$$/수식$$ {s2} 수는 $$수식$${x1}$$/수식$$ 바로 {s3}의 수이므로 $$수식$${a1}$$/수식$$입니다.\n따라서 {wh2}{j3} 뽑은 번호표는 $$수식$${a1}$$/수식$$입니다.\n\n"

    s1 = ['은행', '우체국', '동사무소', '상담센터'][np.random.randint(0, 4)]
    r = np.random.randint(0, 2)
    s2 = ['큰', '작은'][r]
    s3 = ['뒤', '앞'][r]
    wh1 = ['미연이', '성운이', '지선이', '지수'][np.random.randint(0,4)]
    wh2 = ['혁진이', '성수', '재우', '민정이'][np.random.randint(0,4)]
    j1 = proc_jo(wh1, 0)
    x1 = np.random.randint(11, 99)
    j2 = proc_jo(x1, 3)
    j3 = proc_jo(wh2, 0)

    if r == 0 :
        a1 = x1 + 1
    else :
        a1 = x1 - 1

    stem = stem.format(s1 = s1, s2 = s2, wh1 = wh1, wh2 = wh2, j1 = j1, j2 = j2, j3 = j3, x1 = x1)  # 매핑시키기
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, a1 = a1, wh2 = wh2, j3 = j3, s2 = s2, s3 = s3)

    return stem, answer, comment


def uptohun121_Stem_017(): #1-2-1-31
    stem = "{wh1}{j1} {s1}{j2} $$수식$${x1}$$/수식$$장 모았습니다. 오늘 {wh2}에게 {s1} $$수식$${x2}$$/수식$$장을 더 받았다면 {wh1}{j3} 가지고 있는 {s1}{j4} 모두 몇 장인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n{wh1}{j3} 가지고 있는 {s1}{j4} 모두 $$수식$${a1}$$/수식$$장입니다.\n\n"

    wh1 = ['수진이', '현진이', '도희', '소원이'][np.random.randint(0, 4)]
    wh2 = ['오빠', '언니', '동생', '민지', '경환'][np.random.randint(0,5)]
    s1 = ['우표', '스티커', '엽서', '색종이', '사진'][np.random.randint(0, 5)]
    j1 = proc_jo(wh1, -1)
    j2 = proc_jo(s1, 1)
    j3 = proc_jo(wh1, 0)
    j4 = proc_jo(s1, -1)

    x1 = np.random.randint(10, 100)
    if 100 - x1 < 10 :
        x2 = np.random.randint(1, 100-x1+1)
    else :
        x2 = np.random.randint(1, 10)
    a1 = x1 + x2

    stem = stem.format(wh1 = wh1, wh2 = wh2, j1 = j1, j2 =j2, j3 = j3, j4 = j4, s1 = s1, x1 = x1, x2 = x2)  # 매핑시키기
    answer = answer.format(a1 = a1)
    comment = comment.format(wh1 = wh1, j3 = j3, s1 = s1, j4 = j4, a1 = a1)

    return stem, answer, comment



def uptohun121_Stem_018(): #1-2-1-32
    stem = "다음 수를 잘못 나타낸 것을 찾아 기호를 써 보세요.\n$$수식$${boxone}$$/수식$$\n$$표$$㉠ {x2}\n㉡ {x3}\n㉢ {x4}$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n㉠ {x4}\n㉡ {x5}\n㉢ {x6}\n"\
              "따라서 수를 잘못 나타낸 것은 {a1}입니다.\n\n"

    s_list = ['십', '이십', '삼십', '사십', '오십', '육십', '칠십', '팔십', '구십']
    s2_list = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    s3_list = ['열', '스물', '서른', '마흔', '쉰', '예순', '일흔', '여든', '아흔']
    s4_list = ['', '하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉']

    x1 = np.random.randint(11, 99)
    n2 = x1 - 1
    s1 = s3_list[n2//10-1] + s4_list[n2%10]
    n3 = x1 + 1
    s2 = s_list[n3//10-1] + s2_list[n3%10]
    n1 = x1 - np.random.randint(2, 5)
    n4 = n1 + 2
    s3 = s3_list[n4//10-1] + s4_list[n4%10]
    n5 = n4 - 1

    j1 = proc_jo(n1, 2)
    j2 = proc_jo(s1, -1)
    j3 = proc_jo(s2, -1)
    j4 = proc_jo(s3, -1)

    y_list = [f"{s1}보다 $$수식$$1$$/수식$$ 큰 수",
              f"{s2}보다 $$수식$$1$$/수식$$ 작은 수",
              f"$$수식$${n1}$$/수식$${j1} {s3} 사이에 있는 수"]
    y2_list = [f"{s1}{j2} $$수식$${n2}$$/수식$$이므로 $$수식$${n2}$$/수식$$보다 $$수식$$1$$/수식$$ 큰 수는 $$수식$${x1}$$/수식$$입니다.",
               f"{s2}{j3} $$수식$${n3}$$/수식$$이므로 $$수식$${n3}$$/수식$$보다 $$수식$$1$$/수식$$ 작은 수는 $$수식$${x1}$$/수식$$입니다.",
               f"{s3}{j4} $$수식$${n4}$$/수식$$이므로 $$수식$${n1}$$/수식$${j1} $$수식$${n4}$$/수식$$ 사이에 있는 수는 $$수식$${n5}$$/수식$$입니다."]
    rand = [0, 1, 2]
    np.random.shuffle(rand)

    boxone = "BOX{````%d````}" % x1

    correct_idx = 0
    for idx, sdx in enumerate(rand):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == 2:
            correct_idx = idx
            break

    stem = stem.format(boxone = boxone, x2 = y_list[rand[0]], x3 = y_list[rand[1]], x4 = y_list[rand[2]])  # 매핑시키기
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(x4 = y2_list[rand[0]], x5 = y2_list[rand[1]], x6 = y2_list[rand[2]], a1=answer_kodict[correct_idx])

    return stem, answer, comment



def uptohun121_Stem_019(): #1-2-1-33
    stem = "{s1} 입구에 사람들이 한 줄로 서 있습니다. 앞에서부터 {s2} 번째와 {s3} 번째 사이에 서 있는 사람은 모두 몇 명인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n{s2} → $$수식$${n1}$$/수식$$, {s3} → $$수식$${n2}$$/수식$$\n"\
              "$$수식$${n1}$$/수식$${j1} $$수식$${n2}$$/수식$$ 사이에 있는 수는 $$수식$${s4}$$/수식$$이므로 {s2} 번째와 {s3} 번째 사이에 있는 사람은 모두 $$수식$${a1}$$/수식$$명입니다.\n\n"

    s_list = ['열', '스물', '서른', '마흔', '쉰', '예순', '일흔', '여든', '아흔']
    s2_list = ['', '한', '두', '세', '네', '다섯', '여섯', '일곱', '여덟', '아홉']

    s1 = ['축구장', '야구장', '농구장', '콘서트장', '극장'][np.random.randint(0, 5)]
    n1 = np.random.randint(11, 98)
    if (100 - n1) > 10 :
        n2 = n1 + np.random.randint(2, 10)
    else :
        n2 = n1 + np.random.randint(2, 100 - n1)

    a1 = n2 - n1 - 1
    s2 = s_list[n1//10 - 1] + s2_list[n1 % 10]
    s3 = s_list[n2//10 - 1] + s2_list[n2 % 10]
    s4 = ""

    for i in range(n1+1, n2):
        s4 = s4 + str(i) +", "
    s4 = s4[0:-2]
    j1 = proc_jo(n1, 2)

    stem = stem.format(s1 = s1, s2 = s2, s3 = s3)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(s2 = s2, s3 = s3, s4 = s4, n1 = n1, n2 = n2, a1 = a1, j1 =j1)

    return stem, answer, comment


def uptohun121_Stem_020(): #1-2-1-34
    stem = "○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${x1} BIGCIRC {x2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$$10$$/수식$$개씩 묶음의 수를 비교하면 $$수식$${x3}{a1}{x4}$$/수식$$이므로 $$수식$${x1}{a1}{x2}$$/수식$$입니다.\n\n"

    x1 = np.random.randint(11, 100)
    x2 = np.random.randint(11, 100)

    while (x1 == x2) or ((x1//10) == (x2//10)) :
        x2 = np.random.randint(11, 100)

    x3 = x1 // 10
    x4 = x2 // 10

    if x1 > x2 :
        a1 = "&gt;"
    else :
        a1 = "&lt;"

    stem = stem.format(x1 = x1, x2 = x2)  # 매핑시키기
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, a1 = a1)

    return stem, answer, comment



def uptohun121_Stem_021(): #1-2-1-35
    stem = "다음을 $$수식$$&gt;$$/수식$$, $$수식$$&lt;$$/수식$$를 사용하여 나타내어 보세요.\n$$표$$$$수식$${x1}$$/수식$${j1} $$수식$${x2}$$/수식$$보다 {s1}니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${x1}````{a1}````{x2}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1}$$/수식$${j1} $$수식$${x2}$$/수식$$보다 {s1}니다. → $$수식$${x1}{a1}{x2}$$/수식$$\n\n"

    s1 = ['큽', '작습'][np.random.randint(0, 2)]
    x1 = np.random.randint(11, 99)

    if s1 == '작습' :
        x2 = np.random.randint(x1+1, 100)
        a1 = "&lt;"
    else :
        x2 = np.random.randint(10, x1)
        a1 = "&gt;"

    j1 = proc_jo(x1, -1)

    stem = stem.format(x1 = x1, x2 = x2, s1 = s1, j1 = j1)  # 매핑시키기
    answer = answer.format(a1 = a1, x1 = x1, x2 = x2)
    comment = comment.format(x1 = x1, x2 = x2, s1 = s1, a1 = a1, j1 = j1)

    return stem, answer, comment


def uptohun121_Stem_022(): #1-2-1-36
    stem = "□ 안에 알맞은 수를 쓰고, ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${x1}$$/수식$$보다 $$수식$$1$$/수식$$ 큰 수 $$수식$${boxone}$$/수식$$ $$수식$$BIGCIRC$$/수식$$ $$수식$${x2}$$/수식$$보다 $$수식$$1$$/수식$$ 작은 수 $$수식$${boxtwo}$$/수식$$\n"
    answer = "(정답)\n① $$수식$${a1}$$/수식$$, ② $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1}$$/수식$$보다 $$수식$$1$$/수식$$ 큰 수는 $$수식$${x1}$$/수식$$ 바로 뒤의 수이므로 $$수식$${a1}$$/수식$$입니다.\n"\
              "$$수식$${x2}$$/수식$$보다 $$수식$$1$$/수식$$ 작은 수는 $$수식$${x2}$$/수식$$ 바로 앞의 수이므로 $$수식$${a2}$$/수식$$입니다.\n"\
              "$$수식$$10$$/수식$$개씩 묶음의 수가 같으므로 낱개의 수를 비교하면 $$수식$${a1} {a3} {a2}$$/수식$$입니다.\n\n"

    r1 = np.random.randint(0, 2)
    if r1 == 0 :
        tmp1 = np.random.randint(1, 10)
        tmp2 = np.random.randint(0, tmp1)
        a3 = "&gt;"
    else :
        tmp1 = np.random.randint(0, 9)
        tmp2 = np.random.randint(tmp1+1, 10)
        a3 = "&lt;"
    a1 = np.random.randint(1, 10)*10 + tmp1
    a2 = a1//10 * 10 + tmp2

    x1 = a1 - 1
    x2 = a2 + 1

    #boxblank = "BOX{````````}"

    boxone = "BOX{````①````}"
    boxtwo = "BOX{````②````}"
    
    stem = stem.format(x1=x1, x2 = x2, boxone=boxone, boxtwo=boxtwo)  # 매핑시키기
    answer = answer.format(a1 = a1, a2 = a2, a3 = a3)
    comment = comment.format(x1 = x1, x2 = x2, a1 = a1, a2 = a2, a3 = a3)

    return stem, answer, comment



def uptohun121_Stem_023(): #1-2-1-37
    stem = "{s1}{j1} {wh1}{j2} $$수식$${x1}$$/수식$$개, {wh2}{j3} $$수식$${x2}$$/수식$$개 가지고 있습니다. {s1}{j1} 더 적게 가지고 있는 어린이는 누구인가요?\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n$$수식$${x1}$$/수식$${j4} $$수식$$10$$/수식$$개씩 묶음 $$수식$${x3}$$/수식$$개와 낱개 $$수식$${x4}$$/수식$$이고, " \
              "$$수식$${x2}$$/수식$${j5} $$수식$$10$$/수식$$개씩 묶음 $$수식$${x5}$$/수식$$개와 낱개 $$수식$${x6}$$/수식$$개입니다.\n"\
              "$$수식$${x1}$$/수식$${j6} $$수식$${x2}$$/수식$$의 $$수식$$10$$/수식$$개씩 묶음의 수를 비교하면 $$수식$${x1}{s2}{x2}$$/수식$$입니다.\n"\
              "따라서 {s1}{j1} 더 적게 갖고 있는 어린이는 {a1}입니다.\n\n"

    s1 = ['구슬', '인형', '칭찬 스티커', '딱지'][np.random.randint(0, 4)]
    wh1 = ['영호', '대한이', '규호', '세운이'][np.random.randint(0, 4)]
    wh2 = ['서희', '제희', '석호', '연수'][np.random.randint(0, 4)]

    x1 = np.random.randint(11, 100)
    x2 = np.random.randint(11, 100)

    while x1//10 == x2//10 :
        x2 = np.random.randint(11, 100)

    x3 = x1 // 10
    x4 = x1 % 10
    x5 = x2 // 10
    x6 = x2 % 10

    j1 = proc_jo(s1, 1)
    j2 = proc_jo(wh1, -1)
    j3 = proc_jo(wh2, -1)
    j4 = proc_jo(x1, -1)
    j5 = proc_jo(x2, -1)
    j6 = proc_jo(x1, 2)
    if x1 > x2 :
        a1 = wh2
        s2 = "&gt;"
    else :
        a1 = wh1
        s2 = "&lt;"

    stem = stem.format(s1 = s1, wh1 = wh1, wh2 = wh2, x1 = x1, x2 = x2, j1 = j1, j2 = j2, j3 = j3)  # 매핑시키기
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6, a1 = a1, s1 = s1, s2 = s2, j4 = j4, j5 = j5, j6 = j6, j1 = j1)

    return stem, answer, comment



def uptohun121_Stem_024(): #1-2-1-39
    stem = "$$수식$${x1}$$/수식$$보다 크고 $$수식$${x2}$$/수식$$보다 작은 수를 모두 고르세요.\n① $$수식$${x3}$$/수식$$  ② $$수식$${x4}$$/수식$$  ③ $$수식$${x5}$$/수식$$ ④ $$수식$${x6}$$/수식$$  ⑤ $$수식$${x7}$$/수식$$\n"
    answer = "(정답)\n{a1}, {a2}\n"
    comment = "(해설)\n$$수식$$10$$/수식$$개씩 묶음의 수가 $$수식$${x8}$$/수식$$이고 낱개의 수가 $$수식$${x9}$$/수식$$보다 큰 수는 $$수식$${y4}$$/수식$$, $$수식$${y6}$$/수식$$, $$수식$${y7}$$/수식$$입니다. "\
              "$$수식$$10$$/수식$$개씩 묶음의 수가 $$수식$${x10}$$/수식$$이고, 낱개의 수가 $$수식$${x11}$$/수식$$보다 작은 수는 $$수식$${y3}$$/수식$$, $$수식$${y4}$$/수식$$, $$수식$${y5}$$/수식$$, $$수식$${y6}$$/수식$$입니다.\n"\
              "따라서 $$수식$${x1}$$/수식$$보다 크고 $$수식$${x2}$$/수식$$보다 작은 수는 $$수식$${y4}$$/수식$$, $$수식$${y6}$$/수식$$입니다.\n\n"

    x1 = np.random.randint(15, 94)
    x2 = np.random.randint(x1+5, 99)

    y3 = np.random.randint(10, x1)
    y4 = x2 - np.random.randint(1, 5)
    y5 = np.random.randint(10, x1)

    while y3 == y5 :
        y5 = np.random.randint(10, x1)

    y6 = x1 + np.random.randint(1, 5)
    y7 = np.random.randint(x2, 100)

    x8 = x1 // 10
    x9 = x1 % 10
    x10 = x2 // 10
    x11 = x2 % 10

    candidates = [y3, y4, y5, y6, y7]
    np.random.shuffle(candidates)
    [x3, x4, x5, x6, x7] = candidates

    correct_idx = 0
    correct_idx2 = 0
    temp_list = []
    for idx, sdx in enumerate(candidates):       #[a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y4 :
            temp_list.append(idx)
        if sdx == y6 :
            temp_list.append(idx)

    temp_list.sort()
    [correct_idx, correct_idx2] = temp_list

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6, x7 = x7)  # 매핑시키기
    answer = answer.format(a1=answer_dict[correct_idx], a2 = answer_dict[correct_idx2])
    comment = comment.format(x1 = x1, x2 = x2, x8 = x8, x9 = x9, y3 = y3, y4 = y4, y5 = y5, y6 = y6, y7 = y7, x10 = x10, x11 = x11, a1 = answer_dict[correct_idx], a2 = answer_dict[correct_idx2])

    return stem, answer, comment



def uptohun121_Stem_025(): #1-2-1-40
    stem = "{s1} 농장에서 {s1}{j1} {wh1}{j2} $$수식$${x1}$$/수식$$개, {wh2}{j3} $$수식$${x2}$$/수식$$개 땄습니다. {wh3}{j4} {wh2}보다 $$수식$${x3}$$/수식$$개 더 {s2} 땄습니다. {s1}{j1} 많이 딴 순서대로 이름을 써 보세요.\n"
    answer = "(정답)\n{a1}, {a2}, {a3}\n"
    comment = "(해설)\n{wh3}{j4} {wh2}보다 {s1}{j1} $$수식$${x3}$$/수식$$개 더 {s2} 땄으므로 {wh3}{j5} 딴 {s1}의 수는 $$수식$${x2}$$/수식$$보다 $$수식$${x3}$$/수식$$ {s3} 수인 $$수식$${x4}$$/수식$$입니다.\n"\
              "$$수식$${x1}$$/수식$$, $$수식$${x2}$$/수식$$, $$수식$${x4}$$/수식$$의 묶음의 수와 낱개의 수를 비교하면 {s4}입니다.\n"\
              "따라서 {s1}{j1} 많이 딴 순서대로 이름을 쓰면 {a1}, {a2}, {a3}입니다.\n\n"

    s1 = ['귤', '사과', '딸기', '복숭아', '자두'][np.random.randint(0, 5)]
    wh1 = ['민희', '세화', '정규', '한수'][np.random.randint(0, 4)]
    wh2 = ['경우', '주영', '선호', '민재'][np.random.randint(0, 4)]
    wh3 = ['지효', '효진', '소민', '선화'][np.random.randint(0, 4)]
    s2 = ['적게', '많이'][np.random.randint(0, 2)]
    w_list = [wh1, wh2, wh3]
    x1 = np.random.randint(10, 99)
    x2 = np.random.randint(19, 90)

    while x1 == x2 :
        x2 = np.random.randint(19, 90)

    x3 = np.random.randint(1, 10)
    if (s2 == '적게') :
        x4 = x2 - x3
        s3 = '작은'
        if(x1 > x2) :
            a1 = wh1
            a2 = wh2
            a3 = wh3
            s4 = f"$$수식$${x1} `&gt;` {x2} `&gt;` {x4}$$/수식$$"
        elif (x4 > x1):
            a1 = wh2
            a2 = wh3
            a3 = wh1
            s4 = f"$$수식$${x2} `&gt;` {x4} `&gt;` {x1}$$/수식$$"
        else :
            a1 = wh2
            a2 = wh1
            a3 = wh3
            s4 = f"$$수식$${x2} `&gt;` {x1} `&gt;` {x4}$$/수식$$"
    else :
        x4 = x2 + x3
        s3 = '큰'
        if ( x1 > x4 ):
            a1 = wh1
            a2 = wh3
            a3 = wh2
            s4 = f"$$수식$${x1} `&gt;` {x4} `&gt;` {x2}$$/수식$$"
        elif ( x2 > x1):
            a1 = wh3
            a2 = wh2
            a3 = wh1
            s4 = f"$$수식$${x4} `&gt;` {x2} `&gt;` {x1}$$/수식$$"
        else :
            a1 = wh3
            a2 = wh1
            a3 = wh2
            s4 = f"$$수식$${x4} `&gt;` {x1} `&gt;` {x2}$$/수식$$"

    j1= proc_jo(s1, 1)
    j2= proc_jo(wh1, -1)
    j3 = proc_jo(wh2, -1)
    j4 = proc_jo(wh3, -1)
    j5 = proc_jo(wh3, 0)
    j6 = proc_jo(x1, 0)

    stem = stem.format(s1 = s1, s2 = s2, j1 = j1, j2 = j2, j3 = j3, j4 = j4, wh1 = wh1, wh2 = wh2, wh3 = wh3, x1 = x1, x2 = x2, x3 = x3)  # 매핑시키기
    answer = answer.format(a1=a1, a2 = a2, a3 = a3)
    comment = comment.format(a1 = a1, a2 = a2, a3 = a3, s1 = s1, s2 = s2, s3 = s3, s4 = s4, wh2 = wh2, wh3 = wh3, j1 = j1, j4 = j4, j5 = j5, j6 = j6, x1 = x1, x2 = x2, x3 = x3, x4 = x4)

    return stem, answer, comment



def uptohun121_Stem_026(): #1-2-1-41
    stem = "수 카드 중에서 $$수식$$2$$/수식$$장을 골라 한 번씩만 사용하여 몇십몇을 만들려고 합니다. 만들 수 있는 수 중에서 $$수식$${x1}$$/수식$$보다 큰 수는 모두 몇 개인가요?\n$$수식$${boxtwo}$$/수식$$ $$수식$${boxthree}$$/수식$$ $$수식$${boxfour}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n만들 수 있는 수는 {s1}입니다. 이 중에서 $$수식$${x1}$$/수식$$보다 큰 수는 {s2}로 모두 $$수식$${a1}$$/수식$$개 입니다.\n\n"

    x1 = np.random.randint(11, 90)
    x2 = np.random.randint(x1//10+1, 10)
    x3 = np.random.randint(1, 10)
    while x2 == x3 :
        x3 = np.random.randint(1, 10)

    x4 = np.random.randint(1, 10)
    while x3 == x4 or x3 == x2:
        x4 = np.random.randint(1, 10)

    a1 = 0
    s1 = ""
    s2 = ""
    for i in [x2, x3, x4] :
        for j in [x2, x3, x4] :
            if i!= j :
                s1 = s1 + "$$수식$$"+str(i*10+j) +"$$/수식$$, "
                if i*10+j > x1 :
                    s2 = s2 + "$$수식$$"+str(i*10+j) + "$$/수식$$, "
                    a1 = a1 + 1

    s1 = s1[0:-2]
    s2 = s2[0:-2]

    boxtwo = "BOX{````%s````}" % x2
    boxthree = "BOX{````%s````}" % x3
    boxfour = "BOX{````%s````}" % x4

    stem = stem.format(x1 = x1, boxtwo = boxtwo, boxthree = boxthree, boxfour = boxfour)  # 매핑시키기
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, s1 = s1, s2 = s2, a1 = a1)

    return stem, answer, comment



def uptohun121_Stem_027(): #1-2-1-42
    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 중에서 □ 안에 들어갈 수 있는 수는 모두 몇 개인가요?\n$$표$$□$$수식$${x1}````&gt;````{x2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$ 개\n"
    comment = "(해설)\n낱개의 수를 비교하면 $$수식$${x1}{s1}{x3}$$/수식$$이므로 $$수식$$10$$/수식$$개씩 묶음의 수를 비교하면 □ 안에는 $$수식$${x4}$$/수식$${s2}큰 수가 들어갈 수 있습니다.\n"\
              "따라서 □ 안에 들어갈 수 있는 수는 {s3}로 모두 $$수식$${a1}$$/수식$$개 입니다.\n\n"

    x1 = np.random.randint(0, 10)
    x2 = np.random.randint(10, 90)
    x3 = x2 % 10
    x4 = x2 // 10
    s3 = ""
    a1 = 0
    if (x1 > x3) :
        s1 = "&gt;"
        s2 = "하고 같거나 "
        for i in range(x4, 10) :
            s3 = s3 + "$$수식$$"+str(i) + "$$/수식$$, "
            a1 = a1 + 1
    else:
        if (x1 == x3 ):
            s1 = "="
        else :
            s1 = "&lt;"
        s2 = "보다 "
        for i in range(x4+1, 10):
            s3 = s3 + "$$수식$$"+str(i) + "$$/수식$$, "
            a1 = a1 + 1
    s3 = s3[0:-2]

    stem = stem.format(x1 = x1, x2 = x2)  # 매핑시키기
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, x3 = x3, x4 = x4, s1 = s1, s2 = s2, s3 = s3, a1 = a1)

    return stem, answer, comment



def uptohun121_Stem_028(): #1-2-1-45
    stem = "$$수식$${x1}$$/수식$$부터 $$수식$${x2}$$/수식$$까지의 수 중에서 짝수와 홀수는 각각 몇 개인지 구해 보세요.\n홀수 : $$수식$${boxone}$$/수식$$개, 짝수 : $$수식$${boxtwo}$$/수식$$개\n"
    answer = "(정답)\n① $$수식$${a1}$$/수식$$, ② $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n낱개의 수가 $$수식$$1$$/수식$$, $$수식$$3$$/수식$$, $$수식$$5$$/수식$$, $$수식$$7$$/수식$$, $$수식$$9$$/수식$$는 홀수이고, " \
              "낱개의 수가 $$수식$$2$$/수식$$, $$수식$$4$$/수식$$, $$수식$$6$$/수식$$, $$수식$$8$$/수식$$은 짝수입니다.\n"\
              "따라서 $$수식$${x1}$$/수식$$부터 $$수식$${x2}$$/수식$$까지의 수 중에서 홀수는 {s1}로 $$수식$${a1}$$/수식$$개이고, 짝수는 {s2}로 $$수식$${a2}$$/수식$$개입니다.\n\n"

    x1 = np.random.randint(10, 85)
    x2 = np.random.randint(x1+3, x1+15)

    s1 = ""
    s2 = ""
    a1 = a2 = 0

    for i in range(x1, x2+1):
        if i % 2 != 0 :
            s1 = s1 + "$$수식$$"+str(i) + "$$/수식$$, "
            a1 = a1 + 1
        else :
            s2 = s2 + "$$수식$$"+str(i) + "$$/수식$$, "
            a2 = a2 + 1

    s1 = s1[0:-2]
    s2 = s2[0:-2]

    boxone = "BOX{````①````}"
    boxtwo = "BOX{````②````}"

    stem = stem.format(x1 = x1, x2 = x2, boxone=boxone, boxtwo=boxtwo)  # 매핑시키기
    answer = answer.format(a1 = a1, a2 = a2)
    comment = comment.format(x1 = x1, x2 = x2, s1 = s1, s2 = s2, a1 = a1, a2 = a2)

    return stem, answer, comment



def uptohun121_Stem_029(): #1-2-1-46
    stem = "다음 중 홀수인 것을 찾아 기호를 써 보세요.\n$$표$$㉠ {x1}\n㉡ {x2}\n㉢ {x3}\n㉣ {x4}$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n㉠ {x1} → {x5}\n㉡ {x2} → {x6}\n㉢ {x3} → {x7}\n㉣ {x4} → {x8}\n"\
              "따라서 홀수인 것은 {a1}입니다.\n\n"

    s3_list = ['열', '스물', '서른', '마흔', '쉰', '예순', '일흔', '여든', '아흔']
    s4_list = ['', '하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉']

    n1 = np.random.randint(11, 100)
    while n1 % 2 == 0 :
        n1 = np.random.randint(11, 100)
    n2 = np.random.randint(11, 100)
    while n2 % 2 != 0 :
        n2 = np.random.randint(11, 100)
    n2_ = n2 - 1
    n3 = np.random.randint(11, 100)
    while n3 % 2 != 0 :
        n3 = np.random.randint(11, 100)
    n3_ = n3 + 1
    n4 = np.random.randint(1, 10) * 10
    n4_ = n4 // 10

    y1 = s3_list[n1//10-1] + s4_list[n1%10]
    y2 = f"$$수식$${n2_}$$/수식$$보다 $$수식$$1$$/수식$$ 큰 수"
    y3 = f"$$수식$${n3_}$$/수식$$보다 $$수식$$1$$/수식$$ 작은 수"
    y4 = f"$$수식$$10$$/수식$$개씩 묵음 $$수식$${n4_}$$/수식$$개"
    ylist = [y1, y2, y3, y4]

    y1_ = "$$수식$$"+str(n1)+"$$/수식$$, 홀수"
    y2_ = "$$수식$$"+str(n2)+"$$/수식$$, 짝수"
    y3_ = "$$수식$$"+str(n3)+"$$/수식$$, 짝수"
    y4_ = "$$수식$$"+str(n4)+"$$/수식$$, 짝수"
    y_list = [y1_, y2_, y3_, y4_]

    rand = [0, 1, 2, 3]
    np.random.shuffle(rand)
    correct_idx = 0
    for idx, sdx in enumerate(rand):
        if sdx == 0:
            correct_idx = idx
            break

    stem = stem.format(x1 = ylist[rand[0]], x2 = ylist[rand[1]], x3 = ylist[rand[2]], x4 = ylist[rand[3]])  # 매핑시키기
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(x1 = ylist[rand[0]], x2 = ylist[rand[1]], x3 = ylist[rand[2]], x4 = ylist[rand[3]], x5 = y_list[rand[0]], x6 = y_list[rand[1]], x7 = y_list[rand[2]], x8 = y_list[rand[3]], a1 = answer_kodict[correct_idx])

    return stem, answer, comment



def uptohun121_Stem_030(): #1-2-1-47
    stem = "세 조건을 만족하는 수를 구해 보세요.\n$$표$$$$수식$$LEFT ($$/수식$$가$$수식$$RIGHT ) ```` {x1}$$/수식$$보다 크고 $$수식$${x2}$$/수식$$보다 작은 수 입니다.\n$$수식$$LEFT ($$/수식$$나$$수식$$RIGHT ) ```` 10$$/수식$$개씩 묶음 $$수식$${x3}$$/수식$$개입니다.\n$$수식$$LEFT ($$/수식$$다$$수식$$ RIGHT )$$/수식$$ {s1}입니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1}$$/수식$$보다 크고 $$수식$${x2}$$/수식$$보다 작은 수는 $$수식$${x1}$$/수식$${j1} $$수식$${x2}$$/수식$$ 사이에 있는 수이므로 {s2}입니다. "\
              "이 중에서 $$수식$$10$$/수식$$개씩 묶음이 $$수식$${x3}$$/수식$$개인 수는 {s3}이고 {s1}는 $$수식$${a1}$$/수식$$입니다.\n\n"

    s1 = ['홀수', '짝수'][np.random.randint(0, 2)]
    r1 = np.random.randint(0, 2)
    if ( s1 == '홀수') : #홀수일 경우
        if r1 == 0 :
            a1 = np.random.randint(1, 9)*10 + 1
        else :
            a1 = np.random.randint(1, 9)*10 + 9
    else :
        if r1 == 0 :
            a1 = np.random.randint(1, 9)*10
        else :
            a1 = np.random.randint(1, 9)*10 + 8
    if r1 == 1 :
        x1 = a1 - 2
        x2 = a1 + np.random.randint(3, 10)
    else :
        x1 = a1 - np.random.randint(3, 10)
        x2 = a1 + 2
    x3 = a1 // 10
    j1 = proc_jo(x1, 2)

    s2 = ""
    s3 = ""
    for i in range(x1+1, x2):
        s2 = s2 + "$$수식$$"+str(i) + "$$/수식$$, "
        if i//10 == x3 :
            s3 = s3 + "$$수식$$"+str(i) +"$$/수식$$, "
    s2 = s2[0:-2]
    s3 = s3[0:-2]

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, s1 = s1)  # 매핑시키기
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, j1 = j1, s1 = s1, s2 = s2, s3 = s3, a1 = a1)
    return stem, answer, comment




