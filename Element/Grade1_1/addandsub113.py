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


def ImgPath(pathcheck,shape,ranNum): ## 응용 or 기본 / 모양 / 번호 
    if pathcheck==0:
        temps = "Element/Grade1_1/Normal"
    else:
        temps = "Element/Grade1_1/Applications"
    tempimg_list = ["/shape/","/box/","/cynlinder/"]
    want = tempimg_list[shape]
    want = temps+want+str(ranNum).zfill(2)
    return want



def addandsub113_Stem_001(): #1-1-3-07
    stem = "{wh1}{j1} $$수식$${x1}$$/수식$${j2} $$수식$${x2}$$/수식$${j3} 모으기 했고, {wh2}{j4} $$수식$${x3}$$/수식$${j5} $$수식$${x4}$$/수식$${j6} 모으기 했습니다.\n모으기 한 수가 더 큰 사람은 누구일까요?\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n"\
              "$$수식$${x1}$$/수식$${j2} $$수식$${x2}$$/수식$${j3} 모으면 $$수식$${x5}$$/수식$$입니다.\n"\
              "$$수식$${x3}$$/수식$${j5} $$수식$${x4}$$/수식$${j6} 모으면 $$수식$${x6}$$/수식$$입니다.\n"\
              "$$수식$${x7}$$/수식$${j7} $$수식$${x8}$$/수식$$보다 크므로 모으기 한 수가 더 큰 사람은 {a1}입니다.\n\n"

    wh1 = ['성수', '지환', '지은', '연우'][np.random.randint(0, 4)]
    wh2 = ['종현', '지웅', '재현', '민상'][np.random.randint(0, 4)]

    x5 = np.random.randint(3, 10)
    x6 = np.random.randint(3, 10)
    while x5 == x6 :
        x6 = np.random.randint(3, 10)

    x1 = np.random.randint(1, x5)
    x2 = x5 - x1
    x3 = np.random.randint(1, x6)
    x4 = x6 - x3

    if x5 > x6 :
        a1 = wh1
        x7 = x5
        x8 = x6
    else :
        a1 = wh2
        x7 = x6
        x8 = x5

    j1 = proc_jo(wh1, -1)
    j2 = proc_jo(x1, 2)
    j3 = proc_jo(x2, 4)
    j4 = proc_jo(wh2, -1)
    j5 = proc_jo(x3, 2)
    j6 = proc_jo(x4, 4)
    j7 = proc_jo(x7, 0)

    stem = stem.format(wh1 = wh1, wh2 = wh2, x1 = x1, x2 = x2, x3 = x3, x4 = x4, j1 = j1, j2 = j2, j3 = j3, j4 = j4, j5 = j5, j6 = j6) # 매핑시키기
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6, x7 = x7, x8 = x8, a1 = a1, j2 = j2, j3 = j3, j4 = j4, j5 = j5, j6 = j6, j7 = j7)

    return stem, answer, comment




def addandsub113_Stem_002(): #1-1-3-08
    stem = "$$수식$${x1}$$/수식$${j1} 잘못 가르기 한 것은 어느 것인가요?\n① {x2}\n② {x3}\n③ {x4}\n④ {x5}\n⑤ {x6}\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n"\
              "$$수식$${x1}$$/수식$${j2} {y1}, {y2}, {y3}, {y4}로 가를 수 있습니다. "\
              "따라서 $$수식$${x1}$$/수식$${j1} 잘못 가르기 한 것은 {a1} {y5} 입니다.\n\n"

    x1 = np.random.randint(8, 10)

    y1 = "$$수식$$" + str(1) + "$$/수식$$과 $$수식$$"+ str(x1 - 1)+"$$/수식$$"
    y2 = "$$수식$$" + str(2) + "$$/수식$$와 $$수식$$"+ str(x1 - 2)+"$$/수식$$"
    y3 = "$$수식$$" + str(3) + "$$/수식$$과 $$수식$$"+ str(x1 - 3) + "$$/수식$$"
    y4 = "$$수식$$" + str(4) + "$$/수식$$와 $$수식$$"+ str(x1 - 4) + "$$/수식$$"
    t1 = np.random.randint(1, 8)
    j3 = proc_jo(t1, 2)
    y5 = "$$수식$$" + str(t1) + f"$$/수식$${j3} $$수식$$"+ str(x1 - t1 + 1) + "$$/수식$$"

    j1 = proc_jo(x1, 4)
    j2 = proc_jo(x1, -1)
    candidates = [y1, y2, y3, y4, y5]
    np.random.shuffle(candidates)
    [x2, x3, x4, x5, x6] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):       #[a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y5 :
            correct_idx = idx

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4 = x4, x5 = x5, x6 = x6, j1 = j1)  # 매핑시키기
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(x1 = x1, y1 = y1, y2 = y2, y3 = y3, y4 = y4, y5 = y5, j1 = j1, j2 = j2, a1=answer_dict[correct_idx])

    return stem, answer, comment



def addandsub113_Stem_003(): #1-1-3-12
    stem = "똑같은 두 수로 가를 수 없는 수는 어느 것일까요?\n① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n"\
              "$$수식$${x6}$$/수식$${j1} {s1}로 가를 수 있으므로 똑같은 두 수로는 가를 수 없습니다.\n\n"

    y1 = "$$수식$$"+str(2)+"$$/수식$$"
    y2 = "$$수식$$"+str(4)+"$$/수식$$"
    y3 = "$$수식$$"+str(6)+"$$/수식$$"
    y4 = "$$수식$$"+str(8)+"$$/수식$$"
    t1 = np.random.randint(2, 9)
    if t1 % 2 == 0 :
        t1 = t1 + 1
    y5 = "$$수식$$"+str(t1)+"$$/수식$$"

    x6 = t1
    j1 = proc_jo(x6, -1)

    s1 = ""
    for i in range(1, x6):
        j2 = proc_jo(i, 2)
        s1 = s1 + "$$수식$$" +str(i)+f"$$/수식$${j2} $$수식$$" + str(x6 - i) +"$$/수식$$, "
    s1 = s1[0:-2]
    candidates = [y1, y2, y3, y4, y5]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4, x5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y5:
            correct_idx = idx

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4 = x4, x5 = x5)  # 매핑시키기
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(x6 = x6, s1 = s1, j1 = j1)

    return stem, answer, comment



def addandsub113_Stem_004(): #1-1-3-14
    stem = "{s1} $$수식$${x1}$$/수식$$개를 {wh1}{j1} {wh2}{j2} 나누어 가지려고 합니다. {wh1}{j3} {wh2}보다 {s1}{j4} 더 많이 가지게 되는 경우는 모두 몇 가지인지 구하세요. (단, 한 사람이 {s1}{j4} 적어도 한 개씩 갖습니다.)\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
              "$$수식$${x1}$$/수식$${j5} 가르기 하면 {s2}이 됩니다. 이 중에서 {wh1}{j3} {wh2}보다 {s1}{j4} 더 많이 가지게 되는 경우는 "\
              "{s3}일 때이므로 모두 $$수식$${a1}$$/수식$$가지입니다.\n\n"

    s1 = ['초콜릿', '사탕', '과자', '아이스크림'][np.random.randint(0, 4)]
    wh1 = ['재영이', '정후', '우영이', '세형이'][np.random.randint(0, 4)]
    wh2 = ['영수', '가람이', '선화', '제희'][np.random.randint(0, 4)]

    x1 = np.random.randint(3, 10)

    j1 = proc_jo(wh1, 2)
    j2 = proc_jo(wh2, 0)
    j3 = proc_jo(wh1, 0)
    j4 = proc_jo(s1, 4)
    j5 = proc_jo(x1, 4)
    s2 = ""
    s3 = ""
    a1 = 0

    for i in range(1, x1) :
        j = x1 - i
        j6 = proc_jo(i, 2)
        s2 = s2 + "$$수식$$"+str(i)+f"$$/수식$${j6} "+"$$수식$$"+str(j)+"$$/수식$$, "
        if (i > j) :
            s3 = s3 + "$$수식$$" + str(i) + f"$$/수식$${j6} " + "$$수식$$" + str(j) + "$$/수식$$, "
            a1 = a1 + 1

    s2 = s2[0:-2]
    s3 = s3[0:-2]

    stem = stem.format(s1 = s1, x1 = x1, wh1 = wh1, wh2 = wh2, j1 = j1, j2 = j2, j3 = j3, j4 = j4)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1 = x1, s1 = s1, s2 = s2, s3 = s3, j3 = j3, j4 = j4, j5 = j5, a1 = a1, wh1 = wh1, wh2 = wh2)

    return stem, answer, comment



def addandsub113_Stem_005(): #1-1-3-16
    stem = "{s1} $$수식$${x1}$$/수식$$개를 {wh1}{j1} {wh2}{j2} 나누어 가졌습니다. {wh1}{j3} {wh2}보다 $$수식$$1$$/수식$$개 더 많이 가졌다면 {wh1}{j1} {wh2}{j2} 가진 {s1}{j4} 각각 몇 개일까요?\n{wh1} $$수식$${boxone}$$/수식$$개, {wh2} $$수식$${boxtwo}$$/수식$$개\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n"\
              "$$수식$${x1}$$/수식$${j5} 가르기 하면 {s2}이 됩니다. \n"\
              "따라서 {s1}{j5} {wh1}{j3} $$수식$$1$$/수식$$개 더 많이 가졌으므로 {wh1}{j6} $$수식$${a1}$$/수식$$개, {wh2}{j7} $$수식$${a2}$$/수식$$개 가졌습니다.\n\n"

    s1 = ['초콜릿', '사탕', '과자', '아이스크림'][np.random.randint(0, 4)]
    wh1 = ['진영이', '지영이', '서영이', '경아'][np.random.randint(0, 4)]
    wh2 = ['민수', '용택이', '재용이', '소민이'][np.random.randint(0, 4)]

    x1 = np.random.randint(3, 9)
    if ( x1 % 2 == 0) :
        x1 = x1 + 1

    s2 = ""
    for i in range(1, x1) :
        j8 = proc_jo(i, 2)
        j = x1 - i
        s2 = s2 + "$$수식$$"+str(i)+f"$$/수식$${j8} "+"$$수식$$"+str(j)+"$$/수식$$, "
        if j+1 == i :
            a1 = i
            a2 = j

    s2 = s2[0:-2]

    j1 = proc_jo(wh1, 2)
    j2 = proc_jo(wh2, 0)
    j3 = proc_jo(wh1, 0)
    j4 = proc_jo(s1, -1)
    j5 = proc_jo(s1, 4)
    j6 = proc_jo(wh1, -1)
    j7 = proc_jo(wh2, -1)

    boxone = "①"
    boxtwo = "②"

    stem = stem.format(s1 = s1, wh1 = wh1, wh2 = wh2, x1 = x1, j1 = j1, j2 = j2, j3 = j3, j4 = j4, boxone=boxone, boxtwo=boxtwo)  # 매핑시키기
    answer = answer.format(a1=a1, a2 = a2)
    comment = comment.format(x1 = x1, wh1 = wh1, wh2 = wh2, j3 = j3, j5 = j5, j6 = j6, j7 = j7, a1 = a1, a2 = a2, s1 = s1, s2 = s2)

    return stem, answer, comment



def addandsub113_Stem_006(): #1-1-3-21
    stem = "계산 결과가 가장 큰 것을 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${x1} `+` {x2}$$/수식$$    ㉡ $$수식$${x3} `+` {x4}$$/수식$$    ㉢ $$수식$${x5} `+` {x6}$$/수식$$    $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n"\
              "㉠ $$수식$${x1}$$/수식$${j1} $$수식$${x2}$$/수식$${j2} 모으면 $$수식$${x7}$$/수식$$이므로 $$수식$${x1} `+` {x2} `=` {x7}$$/수식$$입니다.\n"\
              "㉡ $$수식$${x3}$$/수식$${j3} $$수식$${x4}$$/수식$${j4} 모으면 $$수식$${x8}$$/수식$$이므로 $$수식$${x3} `+` {x4} `=` {x8}$$/수식$$입니다.\n"\
              "㉢ $$수식$${x5}$$/수식$${j5} $$수식$${x6}$$/수식$${j6} 모으면 $$수식$${x9}$$/수식$$이므로 $$수식$${x5} `+` {x6} `=` {x9}$$/수식$$입니다.\n"\
              "$$수식$${x7}$$/수식$$, $$수식$${x8}$$/수식$$, $$수식$${x9}$$/수식$${j7} 큰 수부터 차례로 쓰면 $$수식$${y1}$$/수식$$, $$수식$${y2}$$/수식$$, $$수식$${y3}$$/수식$$입니다.\n"\
              "따라서 계산 결과가 가장 큰 것은 {a1}입니다.\n\n"

    y1 = np.random.randint(4, 10)
    y2 = np.random.randint(3, y1)
    y3 = np.random.randint(2, y2)

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [x7, x8, x9] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y1:
            correct_idx = idx

    x1 = np.random.randint(1, x7)
    x2 = x7 - x1
    x3 = np.random.randint(1, x8)
    x4 = x8 - x3
    x5 = np.random.randint(1, x9)
    x6 = x9 - x5

    j1 = proc_jo(x1, 2)
    j2 = proc_jo(x2, 4)
    j3 = proc_jo(x3, 2)
    j4 = proc_jo(x4, 4)
    j5 = proc_jo(x5, 2)
    j6 = proc_jo(x6, 4)
    j7 = proc_jo(x9, 4)

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6)  # 매핑시키기
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(y1 = y1, y2 = y2, y3 = y3, x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6, x7 = x7, x8 = x8, x9 = x9, a1=answer_kodict[correct_idx], j1 = j1, j2 = j2, j3 = j3, j4 = j4, j5 = j5, j6 = j6, j7 = j7)

    return stem, answer, comment



def addandsub113_Stem_007(): #1-1-3-25
    stem = "뺄셈의 결과가 가장 큰 것을 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${x1} `-` {x2}$$/수식$$    ㉡ $$수식$${x3} `-` {x4}$$/수식$$    ㉢ $$수식$${x5} `-` {x6}$$/수식$$    $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n"\
              "㉠ $$수식$${x1}$$/수식$${j1} 가르면 $$수식$${x2}$$/수식$${j2} $$수식$${x7}$$/수식$$이므로 $$수식$${x1} `-` {x2} `=` {x7}$$/수식$$입니다.\n"\
              "㉡ $$수식$${x3}$$/수식$${j3} 가르면 $$수식$${x4}$$/수식$${j4} $$수식$${x8}$$/수식$$이므로 $$수식$${x3} `-` {x4} `=` {x8}$$/수식$$입니다.\n"\
              "㉢ $$수식$${x5}$$/수식$${j5} 가르면 $$수식$${x6}$$/수식$${j6} $$수식$${x9}$$/수식$$이므로 $$수식$${x5} `-` {x6} `=` {x9}$$/수식$$입니다.\n"\
              "$$수식$${x7}$$/수식$$, $$수식$${x8}$$/수식$$, $$수식$${x9}$$/수식$${j7} 큰 수부터 차례로 쓰면 $$수식$${y1}$$/수식$$, $$수식$${y2}$$/수식$$, $$수식$${y3}$$/수식$$입니다.\n"\
              "따라서 계산 결과가 가장 큰 것은 {a1}입니다.\n\n"

    y1 = np.random.randint(3, 9)
    y2 = np.random.randint(2, y1)
    y3 = np.random.randint(1, y2)

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [x7, x8, x9] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y1:
            correct_idx = idx

    x1 = np.random.randint(x7 + 1, 10)
    x2 = x1 - x7
    x3 = np.random.randint(x8 + 1, 10)
    x4 = x3 - x8
    x5 = np.random.randint(x9 + 1, 10)
    x6 = x5 - x9

    j1 = proc_jo(x1, 4)
    j2 = proc_jo(x2, 2)
    j3 = proc_jo(x3, 4)
    j4 = proc_jo(x4, 2)
    j5 = proc_jo(x5, 4)
    j6 = proc_jo(x6, 2)
    j7 = proc_jo(x9, 4)

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6)  # 매핑시키기
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(y1 = y1, y2 = y2, y3 = y3, x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6, x7 = x7, x8 = x8, x9 = x9, a1=answer_kodict[correct_idx], j1 = j1, j2 = j2, j3 = j3, j4 = j4, j5 = j5, j6 = j6, j7 = j7)

    return stem, answer, comment



def addandsub113_Stem_008(): #1-1-3-26
    stem = "㉠과 ㉡ 중에서 더 작은 수를 찾아 기호를 써 보세요.\n$$표$$$$수식$${boxone} `+` {boxzero} `=` {boxa}$$/수식$$\n$$수식$${boxtwo} `-` {boxzero} `=` {boxb}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n"\
              "㉠ $$수식$$ {x1} `+` 0 `=` {x1}$$/수식$$\n"\
              "㉡ $$수식$$ {x2} `-` 0 `=` {x2}$$/수식$$\n"\
              "$$수식$${x1}$$/수식$$, $$수식$${x2}$$/수식$${j1} 큰 수부터 차례로 쓰면 $$수식$${x3}$$/수식$$, $$수식$${x4}$$/수식$$입니다.\n"\
              "따라서 ㉠과 ㉡ 중에서 더 작은 수는 $$수식$${x4}$$/수식$$인 {a1}입니다.\n\n"

    x1 = np.random.randint(1, 10)
    x2 = np.random.randint(1, 10)
    while x1 == x2 :
        x2 = np.random.randint(1, 10)

    if x1 > x2 :
        a1 = "㉡"
        x3 = x1
        x4 = x2
    else :
        a1 = "㉠"
        x3 = x2
        x4 = x1

    j1 = proc_jo(x2, 4)

    #boxone = "BOX{````%s````}" % x1
    #boxtwo = "BOX{````%s````}" % x2
    #boxzero = "BOX{````0````}"
    #boxa = "BOX{````㉠````}"
    #boxb = "BOX{````㉡````}"
    
    boxone = "%s" % x1
    boxtwo = "%s" % x2
    boxzero = "0"
    boxa = "㉠"
    boxb = "㉡"

    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxzero=boxzero, boxa=boxa, boxb=boxb)  # 매핑시키기
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, x2 = x2, j1 = j1, x3 = x3, x4 = x4, a1 = a1)

    return stem, answer, comment



def addandsub113_Stem_009(): #1-1-3-27
    stem = "우리 안에 있던 {s1} $$수식$${x1}$$/수식$$마리가 모두 풀밭으로 나왔습니다. 우리 안에 있는 {s1}{j1} 풀밭에 있는 {s1}{j2} 모두 몇 마리인지 구하는 덧셈을 써보세요.\n$$표$$$$수식$${boxone}$$/수식$$$$수식$$`+`$$/수식$$$$수식$${boxtwo}$$/수식$$$$수식$$`=`$$/수식$$$$수식$${boxthree}$$/수식$$$$/표$$\n"
    answer = "(정답)\n① $$수식$$0$$/수식$$, ② $$수식$${x1}$$/수식$$, ③ $$수식$${x1}$$/수식$$\n"
    comment = "(해설)\n"\
              "우리 안에 있던 {s1} $$수식$${x1}$$/수식$$마리가 모두 풀밭으로 나왔으므로 우리 안에는 {s1} $$수식$$0$$/수식$$마리, 풀밭에는 {s1} $$수식$${x1}$$/수식$$마리가 있습니다.\n"\
              "따라서 우리 안과 풀밭에 있는 {s1}{j3} 덧셈식으로 쓰면 $$수식$$0 `+` {x1} `=` {x1}$$/수식$$입니다.\n\n"

    s1 = ['송아지', '돼지', '양', '말'][np.random.randint(0, 4)]
    x1 = np.random.randint(1, 10)

    j1 = proc_jo(s1, 2)
    j2 = proc_jo(s1, -1)
    j3 = proc_jo(s1, 4)

    #boxone = "①"
    #boxtwo = "②"
    #boxthree = "③"
    
    boxone = "box{`①`}"
    boxtwo = "box{`②`}"
    boxthree = "box{`③`}"

    stem = stem.format(s1 = s1, x1 = x1, j1 = j1, j2 = j2, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree)  # 매핑시키기
    answer = answer.format(x1 = x1)
    comment = comment.format(s1 = s1, x1 = x1, j3 = j3)

    return stem, answer, comment



def addandsub113_Stem_010(): #1-1-3-29
    stem = "{wh1}{j1} {s1} $$수식$${x1}$$/수식$$개 중에서 $$수식$${x1}$$/수식$$개를 먹었습니다. 남은 {s1}{j2} 모두 몇 개인지 뺄셈식을 써 보세요.\n$$표$$$$수식$${boxone}$$/수식$$$$수식$$`-`$$/수식$$$$수식$${boxtwo}$$/수식$$$$수식$$`=`$$/수식$$$$수식$${boxthree}$$/수식$$$$/표$$\n"
    answer = "(정답)\n① $$수식$${x1}$$/수식$$, ② $$수식$${x1}$$/수식$$, ③ $$수식$$0$$/수식$$\n"
    comment = "(해설)\n"\
              "{s1} $$수식$${x1}$$/수식$$개에서 $$수식$${x1}$$/수식$$개를 모두 먹었으므로 남은 {s1}{j2} $$수식$$0$$/수식$$개이고, 뺄셈식으로 쓰면 $$수식$${x1} `-` {x1} `=` 0$$/수식$$입니다.\n\n"

    wh1 = ['주현이', '경훈이', '산하', '윤범이'][np.random.randint(0, 4)]
    s1 = ['고구마', '감자', '사과', '아몬드', '감귤'][np.random.randint(0, 5)]

    j1 = proc_jo(wh1, -1)
    j2 = proc_jo(s1, -1)
    x1 = np.random.randint(1, 10)

    boxone = "box{`①`}"
    boxtwo = "box{`②`}"
    boxthree = "box{`③`}"

    stem = stem.format(wh1 = wh1, s1 = s1, j1 = j1, j2 = j2, x1 = x1, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree)  # 매핑시키기
    answer = answer.format(x1=x1)
    comment = comment.format(s1 = s1, x1 = x1, j2 = j2)

    return stem, answer, comment



def addandsub113_Stem_011(): #1-1-3-31
    stem = "$$수식$${boxblank}$$/수식$$ 안에 $$수식$$+$$/수식$$, $$수식$$-$$/수식$$를 알맞게 써넣으세요.\n$$표$$ $$수식$$ {x1} `` {boxone} `` {x2} `=` {x3} $$/수식$$ $$/표$$\n$$표$$ $$수식$$ {x4} `` {boxtwo} `` {x5} `=` {x6} $$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n"\
              "$$수식$$ {x1}` `{boxblank} ``{x2} `=` {x3}$$/수식$$\n"\
              "→ 계산 결과가 {s1} 이용하면 $$수식$$ {x1} `{a1}` {x2} `=` {x3}$$/수식$$입니다.\n" \
              "$$수식$$ {x4}` `{boxblank} ``{x5} `=` {x6}$$/수식$$\n" \
              "→ 계산 결과가 {s2} 이용하면 $$수식$$ {x4} `{a2}` {x5} `=` {x6}$$/수식$$입니다.\n\n"


    clist = ['+', '-']
    a1 = clist[np.random.randint(0, 2)]
    if ( a1 == '+') :
        x3 = np.random.randint(2, 10)
        x1 = np.random.randint(1, x3)
        x2 = x3 - x1
        s1 = "왼쪽의 두 수보다 크므로 덧셈을"
        a2 = '-'
        x4 = np.random.randint(2, 10)
        x5 = np.random.randint(1, x4)
        x6 = x4 - x5
        s2 = "가장 왼쪽의 수보다 작아졌으므로 뺄셈을"
    else :
        x1 = np.random.randint(2, 10)
        x2 = np.random.randint(1, x1)
        x3 = x1 - x2
        s1 = "가장 왼쪽의 수보다 작아졌으므로 뺄셈을"
        a2 = '+'
        x6 = np.random.randint(2, 10)
        x4 = np.random.randint(1, x6)
        x5 = x6 - x4
        s2 = "왼쪽의 두 수보다 크므로 덧셈을"

    boxblank = "□"
    boxone = "□"
    boxtwo = "□"

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6, boxblank=boxblank, boxone=boxone, boxtwo=boxtwo)  # 매핑시키기
    answer = answer.format(a1 = a1, a2 = a2)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6, s1 = s1, s2 = s2, a1 = a1, a2 = a2, boxblank=boxblank)

    return stem, answer, comment



def addandsub113_Stem_012(): #1-1-3-33
    stem = "가장 큰 수와 가장 작은 수의 차를 구해 보세요.\n$$표$$ $$수식$${x1}$$/수식$$    $$수식$${x2}$$/수식$$    $$수식$${x3}$$/수식$$    $$수식$${x4}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
              "큰 수부터 차례로 쓰면 $$수식$${y1}$$/수식$$, $$수식$${y2}$$/수식$$, $$수식$${y3}$$/수식$$, $$수식$${y4}$$/수식$$이므로 "\
              "가장 큰 수는 $$수식$${y1}$$/수식$$이고 가장 작은 수는 $$수식$${y4}$$/수식$$입니다.\n"\
              "→ $$수식$${y1} `-` {y4} `=` {a1}$$/수식$$\n\n"

    y1 = np.random.randint(6, 10)
    y2 = np.random.randint(4, y1)
    y3 = np.random.randint(2, y2)
    y4 = np.random.randint(1, y3)

    candidates = [y1, y2, y3, y4]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4] = candidates

    a1 = y1 - y4

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4)  # 매핑시키기
    answer = answer.format(a1 = a1)
    comment = comment.format(y1=y1, y2=y2, y3=y3, y4=y4, a1 = a1)

    return stem, answer, comment



def addandsub113_Stem_013(): #1-1-3-34
    stem = "{s1}{j1} 마당에 $$수식$${x1}$$/수식$$마리 있고, 집 안에 $$수식$${x2}$$/수식$$마리 있습니다. 마당과 집 안에 있는 {s1}{j2} 모두 몇 마리일까요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$마리\n"
    comment = "(해설)\n"\
              "$$수식$$LEFT ($$/수식$$전체 {s1}의 수$$수식$$)$$/수식$$\n"\
              "$$수식$$= ```` LEFT ($$/수식$$마당에 있는 {s1}의 수$$수식$$) + ($$/수식$$집 안에 있는 {s1}의 수$$수식$$)$$/수식$$\n"\
              "$$수식$$=` {x1} `+` {x2} `=` {a1} LEFT ($$/수식$$마리$$수식$$)$$/수식$$\n\n"

    s1 = ['병아리', '닭', '강아지', '고양이'][np.random.randint(0, 4)]

    a1 = np.random.randint(3, 10)
    x1 = np.random.randint(1, a1)
    x2 = a1 - x1

    j1 = proc_jo(s1, 0)
    j2 = proc_jo(s1, -1)

    stem = stem.format(x1=x1, x2=x2, s1 = s1, j1 = j1, j2=j2)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(s1 = s1, x1 = x1, x2 = x2, a1 = a1)

    return stem, answer, comment



def addandsub113_Stem_014(): #1-1-3-35
    stem = "{wh1}의 나이는 $$수식$${x1}$$/수식$$살이고 {wh2}의 나이는 $$수식$${x2}$$/수식$$살입니다. {wh1}{j1} {wh2}보다 몇 살 더 많을까요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$살\n"
    comment = "(해설)\n"\
              "{wh1}의 나이에서 {wh2}의 나이를 빼면 되므로 $$수식$${x1} `-` {x2}$$/수식$${j2} 계산합니다.\n"\
              "따라서 {wh1}{j1} {wh2}보다 $$수식$${x1} `-` {x2} `=` {a1} LEFT ($$/수식$$살$$수식$$ )$$/수식$$ 더 많습니다.\n\n"

    wh1 = ['현정이', '성주', '대한이', '승현이'][np.random.randint(0, 4)]
    wh2 = ['동생', '수아', '세화', '연주'][np.random.randint(0, 4)]

    x1 = np.random.randint(6, 10)
    x2 = np.random.randint(1, x1)
    a1 = x1 - x2
    # 은는 -1, 이가 0 와과 2 이(라고)3 을를 4
    j1 = proc_jo(wh1, -1)
    j2 = proc_jo(x2, 4)

    stem = stem.format(wh1 = wh1, wh2 = wh2, x1 = x1, x2 = x2, j1 = j1)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(wh1 = wh1, wh2 = wh2, x1 = x1, x2 = x2, j1 = j1, j2 = j2, a1 = a1)

    return stem, answer, comment



def addandsub113_Stem_015(): #1-1-3-36
    stem = "{wh1}{j7}네 모둠 학생들은 합이 같은 덧셈식을 만들고 있습니다. 빈칸에 알맞은 덧셈식을 써 보세요.\n{wh1} : $$수식$${x1} `+` {x2}$$/수식$$\n{wh2} : $$수식$${x3} `+` {x4}$$/수식$$\n{wh3} : $$수식$${x5} `+` {x6}$$/수식$$\n{wh4} : $$수식$${boxone}$$/수식$$$$수식$$`+` {x7}$$/수식$$\n{wh5} : $$수식$${x9} `+`$$/수식$$$$수식$${boxtwo}$$/수식$$\n{wh6} : $$수식$${boxthree}$$/수식$$$$수식$$`+` {x10}$$/수식$$\n"
    answer = "(정답)\n① $$수식$${a1}$$/수식$$, ② $$수식$${a2}$$/수식$$, ③ $$수식$${a3}$$/수식$$\n"
    comment = "(해설)\n"\
              "$$수식$${x1} `+` {x2} `=` {x8}$$/수식$$, $$수식$${x3} `+` {x4} `=` {x8}$$/수식$$, $$수식$${x5} `+` {x6} `=` {x8}$$/수식$$이므로 "\
              "{wh1}{j7}네 모둠 학생들은 합이 $$수식$${x8}$$/수식$${j1} 되는 덧셈식을 만들고 있습니다.\n"\
              "$$수식$${x8}$$/수식$${j2} 가르기 한 두 수로 덧셈식을 만듭니다.\n"\
              "$$수식$${x1}$$/수식$${j3} $$수식$${x2}$$/수식$$ → $$수식$${x1} `+` {x2} `=` {x8}$$/수식$$, "\
              "$$수식$${x3}$$/수식$${j4} $$수식$${x4}$$/수식$$ → $$수식$${x3} `+` {x4} `=` {x8}$$/수식$$, "\
              "$$수식$${x5}$$/수식$${j5} $$수식$${x6}$$/수식$$ → $$수식$${x5} `+` {x6} `=` {x8}$$/수식$$, "\
              "$$수식$${a1}$$/수식$${j6} $$수식$${x7}$$/수식$$ → $$수식$${a1} `+` {x7} `=` {x8}$$/수식$$"\
              "{s1}{s2}\n\n"

    wh1 = ['희영', '혜주', '지호', '자윤'][np.random.randint(0, 4)]
    wh2 = ['준수', '윤호', '창민', '재중'][np.random.randint(0, 4)]
    wh3 = ['나연', '지효', '채영', '다현'][np.random.randint(0, 4)]
    wh4 = ['소영', '근명', '주연', '찬식'][np.random.randint(0, 4)]
    wh5 = ['우정', '우람', '민경', '혜지'][np.random.randint(0, 4)]
    wh6 = ['선희', '효원', '상욱', '상언'][np.random.randint(0, 4)]

    x8 = np.random.randint(5, 10)
    x9 = np.random.randint(0, x8 - 4)
    x10 = np.random.randint(0, x8 - 4)
    a2 = x8 - x9
    a3 = x8 - x10
    if ( x9 != 0 ):
        j8 = proc_jo(x9, 2)
        if (x10 != 0) :
            j9 = proc_jo(a3, 2)
            s1 = f", $$수식$${x9}$$/수식$${j8} $$수식$${a2}$$/수식$$ → $$수식$${x9} `+` {a2} `=` {x8}$$/수식$$"\
                 f", $$수식$${a3}$$/수식$${j9} $$수식$${x10}$$/수식$$ → $$수식$${a3} `+` {x10} `=` {x8}$$/수식$$"
            s2 = "\n\n"
        else :
            s1 = f", $$수식$${x9}$$/수식$${j8} $$수식$${a2}$$/수식$$ → $$수식$${x9} `+` {a2} `=` {x8}$$/수식$$\n"
            s2 = f"또한 $$수식$$LEFT ($$/수식$$어떤 수$$수식$$) +` 0 `=` LEFT ($$/수식$$어떤 수$$수식$$)$$/수식$$임을 이용하여 덧셈식을 만듭니다.\n"\
                 f"$$수식$${a3} `+` 0 `=` {x8}$$/수식$$\n\n"
    else : #x9 = 0
        if (x10 == 0) :
            s1 = "\n"
            s2 = f"또한 $$수식$$LEFT ($$/수식$$어떤 수$$수식$$) +` 0 `=` LEFT ($$/수식$$어떤 수$$수식$$)$$/수식$$임을 이용하여 덧셈식을 만듭니다.\n" \
                 f"$$수식$$0 `+` {a2} `=` {x8}$$/수식$$, $$수식$${a3} `+` 0 `=` {x8}$$/수식$$\n\n "
        else : #x9 = 0 , x 10 != 0
            j8  = proc_jo(x10, 2)
            s1 = f", $$수식$${x10}$$/수식$${j8} $$수식$${a3}$$/수식$$ → $$수식$${x10} `+` {a3} `=` {x8}$$/수식$$\n"
            s2 = f"또한 $$수식$$LEFT ($$/수식$$어떤 수$$수식$$) +` 0 `=` LEFT ($$/수식$$어떤 수$$수식$$)$$/수식$$임을 이용하여 덧셈식을 만듭니다.\n" \
                 f"$$수식$$0 `+` {a2} `=` {x8}$$/수식$$\n\n"

    nset = []
    nlist = []

    for i in range(1, x8) :
        nset.append([i, x8-i])

    for i in range(4) :
        nlist.append(nset.pop(np.random.randint(0, len(nset))))

    x1 = nlist[0][0]
    x2 = nlist[0][1]
    x3 = nlist[1][0]
    x4 = nlist[1][1]
    x5 = nlist[2][0]
    x6 = nlist[2][1]
    a1 = nlist[3][0]
    x7 = nlist[3][1]

    j1 = proc_jo(x8, 0)
    j2 = proc_jo(x8, 4)
    j3 = proc_jo(x1, 2)
    j4 = proc_jo(x3, 2)
    j5 = proc_jo(x5, 2)
    j6 = proc_jo(a1, 2)
    j7 = proc_jo(wh1, 3)

    boxone = "box{`①`}"
    boxtwo = "box{`②`}"
    boxthree = "box{`③`}"

    stem = stem.format(wh1=wh1, wh2=wh2, wh3 = wh3, wh4 = wh4, wh5 = wh5, wh6 = wh6, x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6, x7 = x7, x9 = x9, x10 = x10, j7 = j7, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree)  # 매핑시키기
    answer = answer.format(a1=a1, a2 = a2, a3 = a3)
    comment = comment.format(s1 = s1, s2 = s2, a1 = a1, wh1 = wh1, j7 = j7, x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6, x7 = x7, x8 = x8, j1 = j1, j2 = j2, j3 = j3, j4 = j4, j5 = j5, j6 = j6)

    return stem, answer, comment



def addandsub113_Stem_016(): #1-1-3-37
    stem = "두 수의 차가 $$수식$${x1}$$/수식$$인 뺄셈식을 $$수식$$6$$/수식$$개 만들어 보세요.\n$$수식$$9 `-`$$/수식$$$$수식$${boxone}$$/수식$$$$수식$$`=` {x1}$$/수식$$\n$$수식$$8 `-`$$/수식$$$$수식$${boxtwo}$$/수식$$$$수식$$`=` {x1}$$/수식$$\n$$수식$$7 `-`$$/수식$$$$수식$${boxthree}$$/수식$$$$수식$$`=` {x1}$$/수식$$\n$$수식$$6 `-`$$/수식$$$$수식$${boxfour}$$/수식$$$$수식$$`=` {x1}$$/수식$$\n$$수식$$5 `-`$$/수식$$$$수식$${boxfive}$$/수식$$$$수식$$`=` {x1}$$/수식$$\n$$수식$$4 `-`$$/수식$$$$수식$${boxsix}$$/수식$$$$수식$$`=` {x1}$$/수식$$\n"
    answer = "(정답)\n① $$수식$${a1}$$/수식$$, ② $$수식$${a2}$$/수식$$, ③ $$수식$${a3}$$/수식$$, ④ $$수식$${a4}$$/수식$$, ⑤ $$수식$${a5}$$/수식$$, ⑥ $$수식$${a6}$$/수식$$\n"
    comment = "(해설)\n"\
              "차가 $$수식$${x1}$$/수식$${j1} 되는 경우를 모두 만들어 봅니다.\n"\
              "→ 뺄셈식 : $$수식$$9 `-` {a1} `=` {x1}$$/수식$$, $$수식$$8 `-` {a2} `=` {x1}$$/수식$$, "\
              "$$수식$$7 `-` {a3} `=` {x1}$$/수식$$, $$수식$$6 `-` {a4} `=` {x1}$$/수식$$, "\
              "$$수식$$5 `-` {a5} `=` {x1}$$/수식$$, $$수식$$4 `-` {a6} `=` {x1}$$/수식$$\n\n"

    x1 = np.random.randint(1, 5)
    a1 = 9 - x1
    a2 = 8 - x1
    a3 = 7 - x1
    a4 = 6 - x1
    a5 = 5 - x1
    a6 = 4 - x1
    j1 = proc_jo(x1, 0)

    boxone = "box{`①`}"
    boxtwo = "box{`②`}"
    boxthree = "box{`③`}"
    boxfour = "box{`④`}"
    boxfive = "box{`⑤`}"
    boxsix = "box{`⑥`}"

    stem = stem.format(x1 = x1, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour, boxfive=boxfive, boxsix=boxsix)  # 매핑시키기
    answer = answer.format(a1=a1, a2=a2, a3 = a3, a4 = a4, a5 = a5, a6 = a6)
    comment = comment.format(a1=a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5, a6 = a6, x1 =x1, j1 = j1)

    return stem, answer, comment



def addandsub113_Stem_017(): #1-1-3-39
    stem = "합이 $$수식$${x1}$$/수식$${j1}고 차가 $$수식$${x2}$$/수식$$인 두 수가 있습니다. 두 수 중에서 더 큰 수보다 $$수식$${x3}$$/수식$$ 큰 수를 구하세요.\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
              "두 수의 합이 $$수식$${x1}$$/수식$$이므로 $$수식$${x1}$$/수식$${j2} 가르기 하면 {s1}입니다. "\
              "이 중에서 차가 $$수식$${x2}$$/수식$$인 두 수를 찾으면 {s2}이므로 $$수식$${x4}$$/수식$${j3} $$수식$${x5}$$/수식$$입니다.\n"\
              "따라서 두 수 중에서 더 큰 수는 $$수식$${x6}$$/수식$${j4}고, "\
              "$$수식$${x6}$$/수식$$보다 $$수식$${x3}$$/수식$$ 큰 수는 $$수식$${x6} `+` {x3} `=` {a1}$$/수식$$입니다.\n\n"

    x1 = np.random.randint(3, 10)
    x4 = np.random.randint(1, x1)
    x5 = x1 - x4
    while x4 == x5 :
        x4 = np.random.randint(1, x1)
        x5 = x1 - x4

    if x4 > x5 :
        x6 = x4
        x2 = x6 - x5
    else :
        x6 = x5
        x2 = x6 - x4
    x3 = np.random.randint(1, 10-x6)
    a1 = x6 + x3

    s1 = ""
    s2 = ""
    for i in range(1, int(x1 / 2)+1) :
        j5 = proc_jo(i, 2)
        s1 = s1 + "$$수식$$"+str(i)+f"$$/수식$${j5} $$수식$$" + str(x1 - i) + "$$/수식$$, "
        s2 = s2 + "$$수식$$"+str(x1 - i)+"`-`"+str(i)+"`=`"+str(x1-i-i)+"$$/수식$$, "
    s1 = s1[0:-2]
    s2 = s2[0:-2]
    j1 = proc_jo(x1, 3)
    j2 = proc_jo(x1, 4)
    j3 = proc_jo(x4, 2)
    j4 = proc_jo(x6, 3)

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, j1 = j1)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6, j2 = j2, j3 = j3, j4 = j4, s1 = s1, s2 = s2, a1 = a1)

    return stem, answer, comment



def addandsub113_Stem_018(): #1-1-3-40
    stem = "어떤 수에서 $$수식$${x1}$$/수식$${j1} 빼야 할 것을 잘못하여 더했더니 $$수식$${x2}$$/수식$${j2} 되었습니다. 바르게 계산하면 얼마인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
              "잘못 계산한 덧셈식 : $$수식$${boxblank} `+` {x1} `=` {x2}$$/수식$$\n"\
              "$$수식$${boxblank} `+` {x1} `=` {x2}$$/수식$$에서 $$수식$${x3} `+` {x1} `=` {x2}$$/수식$$이므로 $$수식$${boxblank}$$/수식$$ 안에 알맞은 수는 $$수식$${x3}$$/수식$$입니다.\n"\
              "→ $$수식$${x3} `-` {x1} `=` {a1}$$/수식$$\n\n"

    x3 = np.random.randint(2, 8)
    if x3 > 10 - x3 :
        x1 = np.random.randint(1, 10 - x3)
    else :
        x1 = np.random.randint(1, x3)
    x2 = x3 + x1
    a1 = x3 - x1

    j1 = proc_jo(x1, 4)
    j2 = proc_jo(x2, 0)

    boxblank = "□"

    stem = stem.format(x1=x1, x2=x2, j1 = j1, j2 = j2)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, a1 = a1, boxblank=boxblank)

    return stem, answer, comment



def addandsub113_Stem_019(): #1-1-3-41
    stem = "주어진 수 카드 중에서 $$수식$$2$$/수식$$장을 뽑아 한 번씩만 사용하여 덧셈식을 만들려고 합니다. 두 수의 합이 가장 크게 되도록 덧셈식을 만들었을 때, 그 합을 구해보세요.\n$$수식$${boxone}$$/수식$$  $$수식$${boxtwo}$$/수식$$  $$수식$${boxthree}$$/수식$$  $$수식$${boxfour}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
              "두 수의 합이 가장 크게 되려면 가장 큰 수와 두 번째로 큰 수를 더하면 됩니다. 가장 큰 수는 $$수식$${y1}$$/수식$$이고, "\
              "두 번째로 큰 수는 $$수식$${y2}$$/수식$$이므로 $$수식$${y1} `+` {y2} `=` {a1}$$/수식$$입니다.\n\n"

    y1 = np.random.randint(4, 7)
    if y1 > 10 - y1:
        y2 = np.random.randint(3, 10 - y1)
    else :
        y2 = np.random.randint(3, y1)
    y3 = np.random.randint(2, y2)
    y4 = np.random.randint(1, y3)

    candidates = [y1, y2, y3, y4]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4] = candidates

    a1 = y1 + y2

    boxone = "BOX{````%d````}" % x1
    boxtwo = "BOX{````%d````}" % x2
    boxthree = "BOX{````%d````}" % x3
    boxfour = "BOX{````%d````}" % x4

    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(y1 = y1, y2= y2, a1 = a1)

    return stem, answer, comment



def addandsub113_Stem_020(): #1-1-3-42
    stem = "{wh1}{j1} {s1} $$수식$${x1}$$/수식$$개를 먹고 {wh2}{j2} $$수식$${x2}$$/수식$$개를 먹었더니 $$수식$${x3}$$/수식$$개가 남았습니다. 처음에 있던 {s1}{j3} 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
              "{wh2}{j2} 먹기 전에 있던 {s1}{j3} $$수식$${x3} `+` {x2} `=` {x4} LEFT ($$/수식$$개$$수식$$)$$/수식$$이고, "\
              "{wh1}{j1} 먹기 전에 있던 {s1}{j3} $$수식$${x4} `+` {x1} `=` {a1} LEFT ($$/수식$$개$$수식$$)$$/수식$$입니다.\n\n"

    # 은는 -1, 이가 0 와과 2 이(라고)3 을를 4
    wh1 = ['주현이', '종현이', '호준이', '예원이'][np.random.randint(0, 4)]
    wh2 = ['기운이', '요섭이', '동생', '나영이'][np.random.randint(0, 4)]
    s1 = ['귤', '옥수수', '사과', '복숭아'][np.random.randint(0, 4)]

    a1 = np.random.randint(3, 10)
    x1 = np.random.randint(1, a1 - 1)
    x2 = np.random.randint(1, a1 - x1)
    x3 = a1 - x1 - x2
    x4 = x2 + x3
    j1 = proc_jo(wh1, 0)
    j2 = proc_jo(wh2, 0)
    j3 = proc_jo(s1, -1)

    stem = stem.format(wh1 = wh1, wh2 = wh2, s1 = s1, j1 = j1, j2 = j2, j3 = j3, x1 = x1, x2 = x2, x3 = x3)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(wh1 = wh1, wh2 = wh2, s1 = s1, j1 = j1, j2 = j2, j3 = j3, a1 = a1, x1 = x1, x2 = x2, x3 = x3, x4 = x4)

    return stem, answer, comment










def addandsub113_Stem_021(): #1-1-3-42
    stem = "모으기를 하여 빈칸에 들어갈 수를 쓰세요. \n \n"    

    check =1000
    while check > 20 or check < 10: 
        x1 = np.random.randint(1, 20)
        x2 = np.random.randint(1, 20)
        check = x2+x1
    stem += "$$표t00$$ "+str(x1)+" $$/표t00$$ "+str(x2)+" $$표t01$$  $$/표t01$$ \n\n"

    answer  = "(정답)\n$$수식$$ "+str(check)+" $$/수식$$\n"
    comment = "(해설)\n"
    comment +=   str(x2)+"와 "+str(x1)+"를 모으기 하면 "+str(check)+"입니다.\n"    
    return stem, answer, comment


def addandsub113_Stem_022(): #1-1-3-42
    stem = "모으기를 하여 덧셈식을 완성했을 때 빈칸에 공통으로 들어갈 수를 쓰세요. \n \n"    
    box = 'box{　}'
    check =1000
    while check > 20 or check < 10: 
        x1 = np.random.randint(1, 20)
        x2 = np.random.randint(1, 20)
        check = x2+x1
    stem += "$$표t00$$ "+str(x1)+" $$/표t00$$ "+str(x2)+" $$표t01$$  $$/표t01$$ \n\n"
    stem +=   "$$수식$$"+str(x2)+" + "+str(x1)+" = $$/수식$$$$수식$$"+box+"$$/수식$$"
    
    answer  = "(정답)\n$$수식$$ "+str(check)+" $$/수식$$\n"
    comment = "(해설)\n"
    comment +=   str(x2)+"와 "+str(x1)+"를 모으기 하면 "+str(check)+"입니다.\n"    
    return stem, answer, comment



def addandsub113_Stem_023(): #1-1-3-42
    stem = "그림을 보고 모으기를 해 보고, ㄱ와 ㄴ에 들어갈 숫자를 순서대로 쓰세요. \n \n "    
    check =1000
    while check > 20 or check < 10: 
        x1 = np.random.randint(1, 20)
        x2 = np.random.randint(1, 20)
        check = x2+x1
    stem += "$$표t20$$ "
    temp1 = np.random.randint(1, 20)
    right_shape= np.random.randint(0, 2)
    for i in range(0,x1):
        stem += "$$이미지3$$"+ImgPath(1,right_shape ,temp1 )+".png" +"$$/이미지3$$   "
    stem += "$$/표t20$$ "
    
    temp1 = np.random.randint(1, 20)
    right_shape= np.random.randint(0, 2)
    for i in range(0,x2):
        stem += "$$이미지3$$"+ImgPath(1,right_shape ,temp1 )+".png" +"$$/이미지3$$   "
    stem += "$$표t21$$ "+str(x1)+"$$/표t21$$ ㄱ $$표t22$$  ㄴ $$/표t22$$ "
    
    answer  = "(정답)\n$$수식$$ "+str(x2)+" $$/수식$$ ,$$수식$$ "+str(check)+" $$/수식$$\n"
    comment = "(해설)\n"
    comment +=   str(x2)+"와 "+str(x1)+"를 모으기 하면 "+str(check)+"입니다.\n"    
    return stem, answer, comment

def addandsub113_Stem_024(): #1-1-3-42
    path_list = [
        [
            [1,1,1,1],
            [0,0,0,1],
            [0,0,0,1],
            [0,0,0,1]
        ],
        [
            [1,	1,	1,	0],
            [0,	0,	1,	0],
            [0,	0,	1,	0],
            [0,	0,	1,	1]
        ],
        [
            [1,	1,	0,	0],
            [0,	1,	0,	0],
            [0,	1,	0,	0],
            [0,	1,	1,	1]
        ],
        [
            [1,	0,	0,	0],
            [1,	0,	0,	0],
            [1,	0,	0,	0],
            [1,	1,	1,	1]
        ],[
            [1,0,0,0],
            [1,1,1,1],
            [0,0,0,1],
            [0,0,0,1]
        ],[
            [1,0,0,0],
            [1,0,0,0],
            [1,1,1,1],
            [0,0,0,1]
        ],[
            [1,0,0,0],
            [1,1,0,0],
            [0,1,1,1],
            [0,0,0,1]
        ],[
            [1,0,0,0],
            [1,1,1,0],
            [0,0,1,1],
            [0,0,0,1]
        ],[
            [1,0,0,0],
            [1,1,0,0],
            [0,1,1,0],
            [0,0,1,1]
        ]
    ]
    
    path_want_list =  path_list[np.random.randint(0, len(path_list))] 
    want =np.random.randint(10, 20)
    stem = "모으기를 하여 "+str(want)+"이 되는 것을 따라 가세요 \n"    
    stem += "$$테이블s$$ $$/테이블s$$"    
    answer ="(정답)\n"
    answer +="$$테이블s$$ $$/테이블s$$"    
    for i in range(0,4):
        stem   += "$$테이블trs$$ $$/테이블trs$$"    
        answer += "$$테이블trs$$ $$/테이블trs$$"    
        for j in range(0,4):
            x1 = np.random.randint(1, 20)
            x2 = np.random.randint(1, 20)
            check = x1+x2
            if  path_want_list[i][j]==1:
                while check != want or check < 10 or check >20: 
                    x1 = np.random.randint(1, 20)
                    x2 = np.random.randint(1, 20)
                    check = x1+x2
                answer += "$$테이블td$$   $$빨강$$"+str(x1)+"+"+str(x2)+"="+str(check)+" $$/빨강$$ $$/테이블td$$"                        
            else:
                while check == want or check < 10 or check >20: 
                    x1 = np.random.randint(1, 20)
                    x2 = np.random.randint(1, 20)
                    check = x1+x2
                answer += "$$테이블td$$ "+str(x1)+"+"+str(x2)+"="+str(check)+"$$/테이블td$$"                                            
            stem += "$$테이블td$$"+str(x1)+"+"+str(x2)+"=$$/테이블td$$"    
        stem   += "$$테이블tre$$ $$/테이블tre$$"    
        answer += "$$테이블tre$$ $$/테이블tre$$"    
    stem += "$$테이블e$$ $$/테이블e$$"    
    answer += "$$테이블e$$ $$/테이블e$$"    
    comment="(해설)\n"
    return stem, answer, comment

def addandsub113_Stem_025(): 
    stem = "가르기를 하여 빈칸에 들어갈 수를 쓰세요.\n \n "    
    check =1000
    while check > 20 or check < 10: 
        x1 = np.random.randint(1, 20)
        x2 = np.random.randint(1, 20)
        check = x2+x1
    stem += "$$테이블s$$ $$/테이블s$$" 
    stem += "$$테이블trs$$ $$/테이블trs$$" 
    stem += "$$테이블tdcol2$$"+str(check)+" $$/테이블tdcol2$$" 
    stem += "$$테이블tre$$ $$/테이블tre$$" 
    stem += "$$테이블trs$$ $$/테이블trs$$" 
    stem += "$$테이블td$$"+str(x1)+"$$/테이블td$$"    
    stem += "$$테이블td$$  $$/테이블td$$"    
    stem += "$$테이블tre$$ $$/테이블tre$$" 
    stem += "$$테이블e$$ $$/테이블e$$" 
    answer  = "(정답)\n$$수식$$ "+str(x2)+" $$/수식$$\n"
    comment = "(해설)\n"
    comment +=   str(check)+"는 "+str(x1)+"와 "+str(x2)+"로 가르기 됩니다. \n"    
    return stem, answer, comment



def addandsub113_Stem_026(): 
    stem = "가르기를 하여 뺄셈식을 완성했을 때 빈칸에 공통으로 들어갈 수를 쓰세요. \n "    
    check =1000
    while check > 20 or check < 10: 
        x1 = np.random.randint(1, 20)
        x2 = np.random.randint(1, 20)
        check = x2+x1
    stem += "$$테이블s$$ $$/테이블s$$" 
    stem += "$$테이블trs$$ $$/테이블trs$$" 
    stem += "$$테이블tdcol2$$"+str(check)+" $$/테이블tdcol2$$" 
    stem += "$$테이블tre$$ $$/테이블tre$$" 
    stem += "$$테이블trs$$ $$/테이블trs$$" 
    stem += "$$테이블td$$"+str(x1)+"$$/테이블td$$"    
    stem += "$$테이블td$$  $$/테이블td$$"    



    stem += "$$테이블tre$$ $$/테이블tre$$" 
    stem += "$$테이블e$$ $$/테이블e$$\n \n "    
    box = 'box{　}'
    stem +=   "$$수식$$ "+str(check)+" - "+str(x1)+" = $$/수식$$$$수식$$"+box+"$$/수식$$"
    answer  = "(정답)\n$$수식$$ "+str(x2)+" $$/수식$$\n"
    comment = "(해설)\n"
    comment +=   str(check)+"는 "+str(x1)+"와 "+str(x2)+"로 가르기 됩니다. \n"    
    return stem, answer, comment

def addandsub113_Stem_027(): 
    stem = "가르기 하여 빈칸에 들어갈 알맞은 수를 쓰세요. \n \n "    
    check =1000
    while check > 20 or check < 10: 
        x1 = np.random.randint(1, 20)
        x2 = np.random.randint(1, 20)
        check = x2+x1
    stem += "$$테이블s$$ $$/테이블s$$" 
    stem += "$$테이블trs$$ $$/테이블trs$$" 
    stem += "$$테이블tdcol2$$"+str(check)+" $$/테이블tdcol2$$" 
    stem += "$$테이블tre$$ $$/테이블tre$$" 
    stem += "$$테이블trs$$ $$/테이블trs$$" 
    stem += "$$테이블td$$"+str(x1)+"$$/테이블td$$"    
    stem += "$$테이블td$$  $$/테이블td$$"    
    stem += "$$테이블tre$$ $$/테이블tre$$" 
    stem += "$$테이블e$$ $$/테이블e$$\n \n "    
    box = 'box{　}'
    stem +=   "$$수식$$ "+str(check)+" - $$수식$$"+box+"$$/수식$$ ="+str(x1)+"$$/수식$$"
    answer  = "(정답)\n$$수식$$ "+str(x2)+" $$/수식$$\n"
    comment = "(해설)\n"
    comment +=   str(check)+"는 "+str(x1)+"와 "+str(x2)+"로 가르기 됩니다. \n"    
    return stem, answer, comment

def addandsub113_Stem_028(): 
    stem = "그림을 보고 덧셈식에서 ?에 들어갈 값을 쓰세요. "    
    check =1000
    while check > 20 or check < 10: 
        x1 = np.random.randint(1, 20)
        x2 = np.random.randint(1, 20)
        check = x2+x1
    stem += "$$표$$" 
    temp1 = np.random.randint(1, 20)
    right_shape= np.random.randint(0, 2)
    for i in range(0,x1):
        stem += "$$이미지3$$"+ImgPath(1,right_shape ,temp1 )+".png" +"$$/이미지3$$   "
    stem += "\n$$표1$$ ? $$/표1$$\n"     
    stem += "$$/표$$" 
    stem += "▼"     
    stem += "$$표$$" 
    for i in range(0,check):
        stem += "$$이미지3$$"+ImgPath(1,right_shape ,temp1 )+".png" +"$$/이미지3$$   "    
    stem += "$$/표$$" 
    box = 'box{?}'
    stem +=   "$$수식$$ "+str(x1)+" + $$수식$$"+box+"$$/수식$$ ="+str(check)+"$$/수식$$"    
    answer  = "(정답)\n$$수식$$ "+str(x2)+" $$/수식$$\n"
    comment = "(해설)\n"
    comment +=   str(x1)+"에 "+str(x2)+"를 더하면,  "+str(check)+"가 됩니다. \n"      
    return stem, answer, comment

def addandsub113_Stem_029(): 
    stem = "그림을 보고 덧셈식을 완성하도록 ㄱ와 ㄴ에 들어갈 숫자를 순서대로 쓰세요."    
    check =1000
    while check > 20 or check < 10: 
        x1 = np.random.randint(1, 20)
        x2 = np.random.randint(1, 20)
        check = x2+x1
    stem += "$$표$$" 
    temp1 = np.random.randint(1, 20)
    right_shape= np.random.randint(0, 2)
    for i in range(0,x1):
        stem += "$$이미지3$$"+ImgPath(1,right_shape ,temp1 )+".png" +"$$/이미지3$$   "
    stem += "\n$$표1$$ ㄱ $$/표1$$\n"     
    stem += "$$/표$$" 
    stem += "▼"     
    stem += "$$표$$" 
    for i in range(0,check):
        stem += "$$이미지3$$"+ImgPath(1,right_shape ,temp1 )+".png" +"$$/이미지3$$   "    
    stem += "$$/표$$" 
    box = 'box{ㄱ}'
    box1 = 'box{ㄴ}'
    stem +=   "$$수식$$ "+str(x1)+" + $$수식$$"+box+"$$/수식$$ =$$수식$$"+box1+"$$/수식$$ $$/수식$$"    
    answer  = "(정답)\n$$수식$$ "+str(x2)+" $$/수식$$,$$수식$$ "+str(check)+" $$/수식$$\n"
    comment = "(해설)\n"
    comment +=   str(x1)+"에 "+str(x2)+"를 더하면,  "+str(check)+"가 됩니다. \n"      
    return stem, answer, comment

def addandsub113_Stem_030(): 
    stem = "그림을 보고 뺄셈식을 완성하도록 빈칸에 들어갈 숫자를 쓰세요."    
    check =1000
    while check > 20 or check < 10: 
        x1 = np.random.randint(1, 20)
        x2 = np.random.randint(1, 20)
        check = x2+x1
    stem += "$$표$$" 
    temp1 = np.random.randint(1, 20)
    right_shape= np.random.randint(0, 2)
    for i in range(0,check):
        stem += "$$이미지3$$"+ImgPath(1,right_shape ,temp1 )+".png" +"$$/이미지3$$   "    
    stem += "$$/표$$" 
    stem += "▼"     
    stem += "$$표$$" 
    for i in range(0,x1):
        stem += "$$이미지3$$"+ImgPath(1,right_shape ,temp1 )+".png" +"$$/이미지3$$   "    
    stem += "\n$$표1$$  $$/표1$$\n"     
    stem += "$$/표$$" 
    box = 'box{　}'
    stem +=   "$$수식$$ "+str(check)+" - $$수식$$"+box+"$$/수식$$ =$$수식$$"+str(x1)+"$$/수식$$ $$/수식$$"    
    answer  = "(정답)\n$$수식$$ "+str(x2)+" $$/수식$$\n"
    comment = "(해설)\n"
    comment +=   str(check)+"에서 "+str(x2)+"를 빼면,  "+str(x1)+"가 됩니다. \n"      
    return stem, answer, comment

def addandsub113_Stem_031(): 
    stem = "ㄱ와 ㄴ에 들어갈 숫자를 순서대로 쓰세요.\n"    
    check =1000
    while check > 20 or check < 10: 
        x1 = np.random.randint(1, 20)
        x2 = np.random.randint(1, 20)
        check = x2+x1
    box = 'box{ㄱ}'
    box1 = 'box{ㄴ}'
    stem += str(x1)+" + $$수식$$"+box+"$$/수식$$ = "+str(check)+"\n"
    stem += "☞"+str(check)+" - $$수식$$"+box1+"$$/수식$$ = "+str(x2)+"\n"
    answer  = "(정답)\n$$수식$$ "+str(x2)+" $$/수식$$,$$수식$$ "+str(x1)+" $$/수식$$\n"
    comment = "(해설)\n"
    comment +=   str(x1)+"에서 "+str(x2)+"를 더하면,  "+str(check)+"가 됩니다. \n"      
    comment +=   str(check)+"에서 "+str(x2)+"를 빼면,  "+str(x1)+"가 됩니다. \n"      
    return stem, answer, comment


def addandsub113_Stem_032(): 
    stem = "□ 안에 들어갈 알맞은 수를 쓰세요.\n"    
    check =1000
    while check > 20 or check < 10: 
        x1 = np.random.randint(1, 20)
        x2 = np.random.randint(1, 20)
        check = x2+x1
    box = 'box{　}'
    stem +=   "$$수식$$ "+str(x1)+" + ☆ = "+str(check)+"$$/수식$$ \n"    
    stem +=   "→ $$수식$$ "+ str(check)+" - "+str(x1)+" = ☆ $$/수식$$ \n"    
    stem +=   "→ $$수식$$  ☆ = $$수식$$"+box+"$$/수식$$   $$/수식$$ \n"    
    answer  = "(정답)\n$$수식$$ "+str(x2)+" $$/수식$$\n"
    comment = "(해설)\n"
    comment +=   str(x1)+"에서 "+str(x2)+"를 더하면,  "+str(check)+"가 됩니다. \n"      
    comment +=   str(check)+"에서 "+str(x2)+"를 빼면,  "+str(x1)+"가 됩니다. \n"      
    return stem, answer, comment

def addandsub113_Stem_033(): 
    stem = "□ 안에 들어갈 알맞은 수를 쓰세요.\n"    
    check =1000
    while check > 20 or check < 10: 
        x1 = np.random.randint(1, 20)
        x2 = np.random.randint(1, 20)
        check = x2+x1
    box = 'box{　}'
    stem +=   "$$수식$$ "+str(check)+" - ☆ = "+str(x1)+"$$/수식$$ \n"    
    stem +=   "→ $$수식$$ "+ str(check)+" - "+str(x1)+" = ☆ $$/수식$$ \n"    
    stem +=   "→ $$수식$$  ☆ = $$수식$$"+box+"$$/수식$$   $$/수식$$ \n"    
    answer  = "(정답)\n$$수식$$ "+str(x2)+" $$/수식$$\n"
    comment = "(해설)\n"
    comment +=   str(check)+"에서 "+str(x2)+"를 빼면,  "+str(x1)+"가 됩니다. \n"      
    comment +=   str(check)+"에서 "+str(x1)+"를 빼면,  "+str(x2)+"가 됩니다. \n"      
    return stem, answer, comment

def addandsub113_Stem_034(): 
    stem = "그림에 알맞은 뺄셈식을 만드는 문제입니다. ㄱ, ㄴ, ㄷ에 들어갈 숫자를 순서대로 쓰세요.\n"    
    check =1000
    while check > 20 or check < 10: 
        x1 = np.random.randint(1, 20)
        x2 = np.random.randint(1, 20)
        check = x2+x1
    stem += "$$표$$" 
    temp1 = np.random.randint(1, 20)
    right_shape= np.random.randint(0, 2)
    for i in range(0,x1):
        stem += "$$이미지3$$"+ImgPath(1,right_shape ,temp1 )+".png" +"$$/이미지3$$   "    
    
    
    stem += "\n$$표3$$" 
    for i in range(0,x2):
        stem += "$$이미지3$$"+ImgPath(1,right_shape ,temp1 )+".png" +"$$/이미지3$$   "    
    stem += "$$/표3$$\n"     
    stem += "$$/표$$" 
    box =  'box{ㄱ}'
    stem +="$$수식$$ "+str(check)+" -"+str(x2)+" = $$수식$$"+box+"$$/수식$$ $$/수식$$ \n"    
    box =  'box{ㄴ}'
    stem +="$$수식$$ "+str(check)+" 빼기 "+str(x2)+" 는 $$수식$$"+box+"$$/수식$$ 와 같습니다. $$/수식$$\n"    
    box =  'box{ㄷ}'
    stem +="$$수식$$ "+str(check)+"와 "+str(x2)+"의 차는 $$수식$$"+box+"$$/수식$$ 입니다.$$/수식$$"    
    answer  = "(정답)\n$$수식$$ "+str(x1)+" $$/수식$$,$$수식$$ "+str(x1)+" $$/수식$$,$$수식$$ "+str(x1)+" $$/수식$$\n"
    comment = "(해설)\n"
    comment +=   str(check)+"에서 "+str(x2)+"를 빼면,  "+str(x1)+"가 됩니다. \n"      
    return stem, answer, comment

def addandsub113_Stem_035(): 
    stem = "문장을 뺄셈식으로 나타내기 위해 ㄱ, ㄴ, ㄷ에 들어갈 숫자를 순서대로 쓰세요.\n"    
    check =1000
    while check > 20 or check < 10: 
        x1 = np.random.randint(1, 20)
        x2 = np.random.randint(1, 20)
        check = x2+x1
    stem += "$$표$$" 
    stem +="$$수식$$ "+str(check)+" 빼기 "+str(x1)+"는 "+str(x2)+" 입니다. "    
    stem += "$$/표$$" 
    box0 =  'box{ㄱ}'
    box1 =  'box{ㄴ}'
    box2 =  'box{ㄷ}'
    stem +="$$수식$$ $$수식$$"+box0+"$$/수식$$ - $$수식$$"+box1+"$$/수식$$ = $$수식$$"+box2+"$$/수식$$  $$/수식$$ \n"    
    answer  = "(정답)\n$$수식$$ "+str(check)+" $$/수식$$,$$수식$$ "+str(x1)+" $$/수식$$,$$수식$$ "+str(x2)+" $$/수식$$\n"
    comment = "(해설)\n"
    comment +=   str(check)+"에서 "+str(x1)+"를 빼면,  "+str(x2)+"가 됩니다. \n"      
    return stem, answer, comment


def addandsub113_Stem_036(): 
    stem = "그림에 알맞은 덧셈식을 만드는 문제입니다. ㄱ, ㄴ, ㄷ에 들어갈 숫자를 순서대로 쓰세요.\n"    
    check =1000
    while check > 20 or check < 10: 
        x1 = np.random.randint(1, 20)
        x2 = np.random.randint(1, 20)
        check = x2+x1    
    temp1 = np.random.randint(1, 20)
    right_shape= np.random.randint(0, 2)
    stem += "\n$$테이블s$$ $$/테이블s$$ $$테이블trs$$  $$/테이블trs$$" 
    stem += '$$테이블td2$$'    
    for i in range(0,x1):
        stem += "$$이미지3$$"+ImgPath(1,right_shape ,temp1 )+".png" +"$$/이미지3$$   "    
    stem += '$$/테이블td2$$'
    stem += '$$테이블td2$$'
    for i in range(0,x2):
        stem += "$$이미지3$$"+ImgPath(1,right_shape ,temp1 )+".png" +"$$/이미지3$$   "    
    stem += '$$/테이블td2$$'        
    stem += '$$테이블tre$$ $$/테이블tre$$'
    stem += '$$테이블e$$ $$/테이블e$$'
    stem += "\n"     
    box =  'box{ㄱ}'
    stem +="$$수식$$ "+str(x1)+"+"+str(x2)+" = $$수식$$"+box+"$$/수식$$ $$/수식$$ \n"    
    box =  'box{ㄴ}'
    stem +="$$수식$$ "+str(x1)+" 더하기 "+str(x2)+" 는 $$수식$$"+box+"$$/수식$$ 와 같습니다. $$/수식$$\n"    
    box =  'box{ㄷ}'
    stem +="$$수식$$ "+str(x1)+"와 "+str(x2)+"의 합은 $$수식$$"+box+"$$/수식$$ 입니다.$$/수식$$"    
    answer  = "(정답)\n$$수식$$ "+str(check)+" $$/수식$$,$$수식$$ "+str(check)+" $$/수식$$,$$수식$$ "+str(check)+" $$/수식$$\n"
    comment = "(해설)\n"
    comment +="$$수식$$ "+str(x1)+"+"+str(x2)+" = $$수식$$"+str(check)+"$$/수식$$ $$/수식$$ \n"    
    comment +="$$수식$$ "+str(x1)+" 더하기 "+str(x2)+" 는 $$수식$$"+str(check)+"$$/수식$$ 와 같습니다. $$/수식$$\n"    
    comment +="$$수식$$ "+str(x1)+"와 "+str(x2)+"의 합은 $$수식$$"+str(check)+"$$/수식$$ 입니다.$$/수식$$"    
    return stem, answer, comment

def addandsub113_Stem_037(): 
    stem = "문장을 덧셈식으로 나타내기 위해 ㄱ, ㄴ, ㄷ에 들어갈 숫자를 순서대로 쓰세요.\n"    
    check =1000
    while check > 20 or check < 10: 
        x1 = np.random.randint(1, 20)
        x2 = np.random.randint(1, 20)
        check = x2+x1
    stem += "$$표$$" 
    stem +="$$수식$$"+ str(x1)+" 더하기 "+str(x2)+"는 "+str(check)+" 입니다. "    
    stem += "$$/표$$" 
    box0 =  'box{ㄱ}'
    box1 =  'box{ㄴ}'
    box2 =  'box{ㄷ}'
    stem +="$$수식$$ $$수식$$"+box0+"$$/수식$$ + $$수식$$"+box1+"$$/수식$$ = $$수식$$"+box2+"$$/수식$$  $$/수식$$ \n"    
    answer  = "(정답)\n$$수식$$ "+str(x1)+" $$/수식$$,$$수식$$ "+str(x2)+" $$/수식$$,$$수식$$ "+str(check)+" $$/수식$$\n"
    comment = "(해설)\n"
    comment +=   str(x1)+"에서 "+str(x1)+"를 더하면,  "+str(check)+"가 됩니다. \n"      
    return stem, answer, comment
