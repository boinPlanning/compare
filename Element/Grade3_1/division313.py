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






# 3-1-3-01
def division313_Stem_001():
    stem = "나눗셈식으로 나타내어 보세요.\n$$표$$$$수식$${x1}$$/수식$$ 나누기 $$수식$${x2}$$/수식$${j1} $$수식$${x3}$$/수식$${j2} 같습니다.$$/표$$\n$$수식$${x1} ` div ` $$/수식$$ $$수식$${box1}$$/수식$$ $$수식$$ ` = ` $$/수식$$ $$수식$${box2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1}$$/수식$${j3} $$수식$${x2}$$/수식$${ro1} 나누어 $$수식$${x3}$$/수식$${j4} 된 것이므로\n"\
              "$$수식$${x1} ` div ` {x2} ` = ` {x3}$$/수식$$입니다.\n\n"


    x2 = np.random.randint(2, 10)
    x3 = np.random.randint(2, 10)
    x1 = x2 * x3

    j1 = proc_jo(x2, -1)
    j2 = proc_jo(x3, 2)
    j3 = proc_jo(x1, 4)
    j4 = proc_jo(x3, 0)

    box1 = "box{　　　}"
    box2 = "box{　　　}"

    # box1 = "LEFT ( ① RIGHT )"
    # box2 = "LEFT ( ② RIGHT )"

    if x2 == 3 or x2 == 6:
        ro1 = "으로"
    else:
        ro1 = "로"

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, j1 = j1, j2 = j2, box1 = box1, box2 = box2)
    answer = answer.format(a1 = x2, a2 = x3)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, j3 = j3, j4 = j4, ro1=ro1)

    return stem, answer, comment













#3-1-3-02
def division313_Stem_002():
    stem = "나눗셈식을 보고 몫을 찾아 써 보세요.\n$$표$$ $$수식$${x1} ` div ` {x2} ` = ` {x3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1} ` div ` {x2} ` = ` {x3}$$/수식$$에서 몫은 $$수식$${x3}$$/수식$$입니다.\n\n"


    x2 = np.random.randint(2, 10)
    a1 = x3 = np.random.randint(2, 10)
    x1 = x2 * x3

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3)
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3)

    return stem, answer, comment










#3-1-3-05
def division313_Stem_003():
    stem = "다음은 나눗셈식 $$수식$${x1} ` div ` {x2} ` = ` {x3}$$/수식$${j1} 나타낸 문장입니다. □ 안에 알맞은 수를 써넣으세요.\n$$표$$ {s1} $$수식$${box1}$$/수식$$장을 $$수식$${x2}$$/수식$$명이 똑같이 나누어 가지려면 한 명이 $$수식$${box2}$$/수식$$장씩 가지면 됩니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1} ` div ` {x2} ` = ` {x3}$$/수식$$에서 $$수식$${x3}$$/수식$${j2} $$수식$${x1}$$/수식$${j3} $$수식$${x2}$$/수식$${ro1} 나눈 몫입니다.\n\n"


    s1 = ['색종이', '도화지', '한지', '딱지'][np.random.randint(0, 4)]
    while True:
        x2 = np.random.randint(2, 10)
        x3 = np.random.randint(2, 10)

        if x2 != x3: break
    x1 = x2 * x3
    a1 = x1
    a2 = x3

    j1 = proc_jo(x3, 4)
    j2 = proc_jo(x3, -1)
    j3 = proc_jo(x1, 4)

    box1 = "box{　　　}"
    box2 = "box{　　　}"

    if x2 == 3 or x2 == 6:
        ro1 = "으로"
    else:
        ro1 = "로"

    stem = stem.format(s1 = s1, x1 = x1, x2 = x2, x3 = x3, j1 = j1, box1 = box1, box2 = box2)
    answer = answer.format(a1 = a1, a2 = a2)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, j2 = j2, j3 = j3, ro1=ro1)

    return stem, answer, comment










#3-1-3-06
def division313_Stem_004():
    stem = "다음을 나눗셈식으로 나타낼 때 몫은 얼마인가요?\n$$표$$ $$수식$${x1}$$/수식$$ 나누기 $$수식$${x2}$$/수식$${j1} $$수식$${x3}$$/수식$${j2} 같습니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1}$$/수식$${j3} $$수식$${x2}$$/수식$${ro1} 나누어 $$수식$${x3}$$/수식$${j4} 된 것이므로 "\
              "나눗셈식으로 나타내면 $$수식$${x1} ` div ` {x2} ` = ` {x3}$$/수식$$입니다.\n"\
              "나눗셈식 $$수식$${x1} ` div ` {x2} ` = ` {x3}$$/수식$$에서 몫은 $$수식$${x3}$$/수식$$입니다.\n\n"


    x2 = np.random.randint(2, 10)
    x3 = np.random.randint(2, 10)
    x1 = x2 * x3
    a1 = x3

    j1 = proc_jo(x2, -1)
    j2 = proc_jo(x3, 2)
    j3 = proc_jo(x1, 4)
    j4 = proc_jo(x3, 0)

    if x2 == 3 or x2 == 6:
        ro1 = "으로"
    else:
        ro1 = "로"

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, j1 = j1 ,j2 = j2)
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, j3 = j3, j4 = j4, ro1=ro1)

    return stem, answer, comment












#3-1-3-09
def division313_Stem_005():
    stem = "{s1}{j1} 과수원에서 오전에 딴 {s2} $$수식$${x1}$$/수식$$개와 오후에 딴 {s2} $$수식$${x2}$$/수식$$개를 봉지 $$수식$${x3}$$/수식$$장에 똑같이 나누어 담으려고 합니다. 한 봉지에 {s2}{j2} 몇 개씩 담아야 하나요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$전체 {s2} 수$$수식$$RIGHT ) = ` {x1} ` + ` {x2} ` = ` {x4} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$LEFT ($$/수식$$한 봉지에 담아야 하는 {s2} 수$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$` = LEFT ($$/수식$$전체 {s2} 수$$수식$$RIGHT ) div LEFT ($$/수식$$봉지 수$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$` = ` {x4} ` div ` {x3} ` = ` {a1} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"


    s1 = ['선희', '수호', '철수', '은주', '진희', '대희', '주미', '휘재', '민호', '건우'][np.random.randint(0, 10)]
    s2 = ['사과', '배', '복숭아', '감', '자두', '딸기', '포도'][np.random.randint(0, 7)]

    x3 = np.random.randint(2, 10)
    a1 = np.random.randint(2,10)
    x4 = x3 * a1

    if x3 > a1 :
        x1 = np.random.randint(a1, x4)
    else :
        x1 = np.random.randint(x3, x4)
    x2 = x4 - x1

    j1 = proc_jo(s1, -1)
    j2 = proc_jo(s2, 4)

    stem = stem.format(s1 = s1, s2 = s2, x1 = x1, x2 = x2, x3 = x3, j1 = j1 ,j2 = j2)
    answer = answer.format(a1 = a1)
    comment = comment.format(s2 = s2, x1 = x1, x2 = x2, x3 = x3, x4 = x4, a1 = a1)

    return stem, answer, comment













#3-1-3-11
def division313_Stem_006():
    stem = "남김없이 똑같이 나누어 가질 수 있는 경우를 말한 사람은 누구인가요?\n$$표$$ ∙ {wh1} : {s1} $$수식$${x1}$$/수식$$개를 $$수식$${x2}$$/수식$$명이 나누어 가지기\n∙ {wh2} : {s2} $$수식$${x3}$$/수식$$개를 $$수식$${x4}$$/수식$$명이 나누어 가지기\n∙ {wh3} : {s3} $$수식$${x5}$$/수식$$개를 $$수식$${x6}$$/수식$$명이 나누어 가지기$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n∙ $$수식$${x2}$$/수식$$명이 {s1} $$수식$${x1}$$/수식$$개를 $$수식$$1$$/수식$$개씩 번갈아 가며 가지면 한 명이 $$수식$${x7}$$/수식$$개씩 {s4}\n"\
              "∙ $$수식$${x4}$$/수식$$명이 {s2} $$수식$${x3}$$/수식$$개를 $$수식$$1$$/수식$$개씩 번갈아 가며 가지면 한 명이 $$수식$${x7}$$/수식$$개씩 {s5}\n" \
              "∙ $$수식$${x6}$$/수식$$명이 {s3} $$수식$${x5}$$/수식$$개를 $$수식$$1$$/수식$$개씩 번갈아 가며 가지면 한 명이 $$수식$${x7}$$/수식$$개씩 {s6}\n\n"


    wh1 = ['영진', '진석', '소영', '미영', '혜선', '혜주', '지웅', '우성', '정주', '경호'][np.random.randint(0, 10)]
    wh2 = ['석호', '진수', '선희', '라희', '라영', '도경', '요환', '수진', '호진', '시우'][np.random.randint(0, 10)]
    wh3 = ['진영', '우석', '희진', '우주', '아중', '아라', '보아', '태일', '승민', '상민'][np.random.randint(0, 10)]

    s_list = ['감', '귤', '배', '사과', '사탕', '초콜렛', '복숭아', '구슬', '자두', '빵']

    s1 = s_list[np.random.randint(0, 10)]
    s2 = s_list[np.random.randint(0, 10)]

    while s1 == s2:
        s2 = s_list[np.random.randint(0, 10)]

    s3 = s_list[np.random.randint(0, 10)]

    while s1 == s3 or s2 == s3:
        s3 = s_list[np.random.randint(0, 10)]

    x7 = np.random.randint(2, 10)

    x2 = np.random.randint(2, 10)
    x4 = np.random.randint(2, 10)

    while x2 == x4:
        x4 = np.random.randint(2, 10)

    x6 = np.random.randint(2, 10)

    while x2 == x6 or x4 == x6:
        x6 = np.random.randint(2, 10)

    tmp = np.random.randint(0, 3)

    if tmp == 0:
        x1 = x2 * x7
        x3 = x4 * x7 + np.random.randint(1, x4)
        x5 = x6 * x7 + np.random.randint(1, x6)
        a1 = wh1
        s4 = "갖습니다."
        s5 = "갖고 $$수식$$" + str(x3 % x4) + "$$/수식$$개 남습니다."
        s6 = "갖고 $$수식$$" + str(x5 % x6) + "$$/수식$$개 남습니다."

    elif tmp == 1:
        x1 = x2 * x7 + np.random.randint(1, x2)
        x3 = x4 * x7
        x5 = x6 * x7 + np.random.randint(1, x6)
        a1 = wh2
        s4 = "갖고 $$수식$$" + str(x1 % x2) + "$$/수식$$개 남습니다."
        s5 = "갖습니다."
        s6 = "갖고 $$수식$$" + str(x5 % x6) + "$$/수식$$개 남습니다."

    else:
        x1 = x2 * x7 + np.random.randint(1, x2)
        x3 = x4 * x7 + np.random.randint(1, x4)
        x5 = x6 * x7
        a1 = wh3
        s4 = "갖고 $$수식$$" + str(x1 % x2) + "$$/수식$$개 남습니다."
        s5 = "갖고 $$수식$$" + str(x3 % x4) + "$$/수식$$개 남습니다."
        s6 = "갖습니다."

    stem = stem.format(wh1 = wh1, wh2 = wh2, wh3 = wh3, s1 = s1, s2 = s2, s3 = s3, x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6)
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6, x7 = x7, s1 = s1, s2 = s2, s3 = s3, s4 = s4, s5 = s5, s6 = s6)

    return stem, answer, comment















#3-1-3-12
def division313_Stem_007():
    stem = "$$수식$${x1}$$/수식$$명이 {s1} {t1} 타를 똑같이 나누어 가졌습니다. 한 명이 가진 {s1}은 몇 자루인가요?(단, 한 타는 12자루 입니다.)\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$자루\n"
    comment = "(해설)\n{s1} $$수식$$1$$/수식$$ 타는 $$수식$$12$$/수식$$자루입니다.\n"\
              "$$수식$$LEFT ($$/수식$$한 명이 가진 {s1} 수$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$` = ` LEFT ($$/수식$$전체 {s1} 수$$수식$$RIGHT ) ` div ` LEFT ($$/수식$$나누어 가지는 사람 수$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$` = ` {t2} ` div ` {x1} ` = ` {a1} LEFT ($$/수식$$자루$$수식$$RIGHT )$$/수식$$\n\n"


    s1 = ['연필', '볼펜', '만년필'][np.random.randint(0, 3)]
    t1 = ['한', '두', '세'][np.random.randint(0, 3)]

    if t1 == '한' :
        t2 = 12
    elif t1 == '두' :
        t2 = 24
    else :
        t2 = 36

    # x1 = np.random.randint(1, 13)
    #
    # while t2 % x1 != 0:
    #     x1 = np.random.randint(1, 13)

    x1 = np.random.randint(2, 13)

    while t2 % x1 != 0:
        x1 = np.random.randint(2, 13)

    a1 = t2 // x1

    stem = stem.format(s1 = s1, x1 = x1, t1=t1)
    answer = answer.format(a1 = a1)
    comment = comment.format(s1 = s1, x1 = x1, a1 = a1, t2=t2)

    return stem, answer, comment













#3-1-3-14
def division313_Stem_008():
    stem = "{s1}{j1} $$수식$${x1}$$/수식$${s2} 있습니다. 한 {s3}에 $$수식$${x2}$$/수식$${s2}씩 {s4} {s3}{j2} 몇 개 만들어지는지를 구하는 나눗셈식을 써 보세요.\n$$수식$${box1}$$/수식$$ $$수식$$` div `$$/수식$$ $$수식$${box2}$$/수식$$ $$수식$$` = `$$/수식$$ $$수식$${box3}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$\n"
    comment = "(해설)\n" \
              "{s1} $$수식$${x1}$$/수식$${s2}{j3} 한 {s3}에 $$수식$${x2}$$/수식$${s2}씩 {s4} {s3}{j2} $$수식$${x3}$$/수식$$개 만들어집니다.\n"\
              "따라서 나눗셈식으로 나타내면 $$수식$${x1} ` div ` {x2} ` = ` {x3}$$/수식$$입니다.\n\n"


    while True:
        x2 = np.random.randint(2, 10)
        x3 = np.random.randint(2, 10)
        x1 = x2 * x3

        if x1 != 1:
            break

    box1 = "box{　　}"
    box2 = "box{　　}"
    box3 = "box{　　}"

    choice = np.random.randint(0, 3)

    if choice == 0:
        s1 = ['학생', '어린이', '운동선수'][np.random.randint(0, 3)]
        s2 = "명"
        s3 = "모둠"
        s4 = "나누면"

    elif choice == 1:
        s1 = ['사과', '자두', '복숭아', '배', '망고', '딸기', '토마토', '오이', '당근', '양파'][np.random.randint(0, 10)]
        s2 = "개"
        s3 = ['상자', '바구니'][np.random.randint(0, 2)]
        s4 = "담으면"

    else:
        s1 = ['인형', '구슬', '장난감', '목걸이'][np.random.randint(0, 4)]
        s2 = "개"
        s3 = ['상자', '바구니'][np.random.randint(0, 2)]
        s4 = "담으면"

    j1 = proc_jo(s1, 0)
    j2 = proc_jo(s3, 0)
    j3 = proc_jo(s2, 1)

    stem = stem.format(x1 = x1, x2 = x2, box1 = box1, box2 = box2, box3 = box3, s1=s1, j1=j1, s2=s2, s3=s3, s4=s4, j2=j2)
    answer = answer.format(a1 = x1, a2 = x2, a3 = x3)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, s1=s1, s2=s2, j3=j3, s3=s3, s4=s4, j2=j2)

    return stem, answer, comment







#3-1-3-18
def division313_Stem_009():
    stem = "{wh1}{j1}네 반 학생 $$수식$${x1}$$/수식$$명이 {s1}을 가려고 합니다. 한 모둠을 $$수식$${x2}$$/수식$$명으로 하면 몇 모둠이 되는지 뺄셈을 이용하여 몫을 구해 보세요.\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$모둠\n"
    comment = "(해설)\n$$수식$${x1}{x4} ` = ` 0$$/수식$$\n"\
              "→ $$수식$${x1} ` div ` {x2} ` = ` {x3}$$/수식$$\n\n"


    wh1 = ['진희', '연수', '수호', '선우', '철호', '선미', '민준', '가영', '봉준', '성희'][np.random.randint(0, 10)]
    s1 = ['감자 캐기 체험 학습', '고구마 캐기 체험 학습', '당근 캐기 체험 학습', '수학여행', '봉사활동', '직업 체험 학습', '소풍'][np.random.randint(0, 7)]

    j1 = proc_jo(wh1, 3)
    x2 = np.random.randint(2, 10)
    x3 = a1 = np.random.randint(2,10)

    x1 = x2 * x3
    x4 = ""

    for i in range(x3):
        x4 = x4 + "` - `" + str(x2)

    stem = stem.format(wh1 = wh1, j1 = j1, s1 = s1, x1 = x1, x2 = x2)
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4)

    return stem, answer, comment











#3-1-3-19
def division313_Stem_010():
    stem = "{wh1}{j1} {s1} $$수식$${x1}$$/수식$$개를 사서 $$수식$${x2}$$/수식$$개를 먹고 남는 {s1}{j2} 한 봉지에 $$수식$${x3}$$/수식$$개씩 담아 포장하려고 합니다. 필요한 봉지는 몇 장인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$장\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$먹고 남은 {s1} 수$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$` = ` {x1} ` - ` {x2} ` = ` {x4} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$LEFT ($$/수식$$필요한 봉지 수$$수식$$RIGHT ) ` = ` {x4} ` div ` {x3} ` = ` {a1}$$/수식$$\n\n"


    wh1 = ['연우', '현지', '선호', '태우', '진수', '준서', '진우', '은비', '규비', '민하'][np.random.randint(0, 10)]
    s1 = ['초콜릿', '사탕', '쿠키', '바나나', '사과', '빵', '과자'][np.random.randint(0, 7)]

    x2 = np.random.randint(2,10)
    x3 = np.random.randint(2,10)
    a1 = np.random.randint(2,10)

    x4 = x3 * a1
    x1 = x4 + x2

    j1 = proc_jo(wh1, -1)
    j2 = proc_jo(s1, 4)
    stem = stem.format(wh1 = wh1, j1 = j1, j2 = j2, s1 = s1, x1 = x1, x2 = x2, x3 = x3)
    answer = answer.format(a1 = a1)
    comment = comment.format(s1 = s1, x1 = x1, x2 = x2, x3 = x3, x4 = x4, a1 = a1)

    return stem, answer, comment














#3-1-3-21
def division313_Stem_011():
    stem = "{s1} 한 {s2}{j1} 봉지 $$수식$${x1}$$/수식$$장에 똑같이 나누어 담으려고 합니다. {s1}{j2} 한 봉지에 몇 {s3}씩 담아야 하나요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$${s3}\n"
    comment = "(해설)\n{s1} 한 {s2}{j3} $$수식$${x2}$$/수식$${s3}입니다.\n"\
              "$$수식$$LEFT ($$/수식$$한 봉지에 담아야 하는 {s1} 수$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$` = ` LEFT ($$/수식$$전체 {s1} 수$$수식$$RIGHT ) ` div ` LEFT ($$/수식$$나누어 담는 봉지 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {x2} ` div ` {x1} ` = ` {a1} LEFT ($$/수식$${s3}$$수식$$RIGHT )$$/수식$$\n\n"


    tmp = np.random.randint(0, 3)

    s1 = ['굴비', '달걀', '연필'][tmp]
    s2 = ['두름', '판', '타'][tmp]
    s3 = ['마리', '개', '자루'][tmp]

    x2 = [20, 30, 12][tmp]
    x1 = np.random.randint(2, x2)

    while x2 % x1 != 0:
        x1 = np.random.randint(3, x2)

    a1 = x2 // x1

    j1 = proc_jo(s2, 4)
    j2 = proc_jo(s1, 4)
    j3 = proc_jo(s2, -1)

    stem = stem.format(s1 = s1, s2 = s2, s3 = s3, j1 = j1, j2 = j2, x1 = x1)
    answer = answer.format(a1 = a1, s3=s3)
    comment = comment.format(s1 = s1, s2 = s2, s3 = s3, j3 = j3, x1 = x1, x2 = x2, a1 = a1)

    return stem, answer, comment















#3-1-3-24
def division313_Stem_012():
    stem = "{s1}{j1} 한 상자에 $$수식$${x1}$$/수식$$개씩 $$수식$${x2}$$/수식$$상자 있습니다. 이 {s1}{j2} 한 명에게 $$수식$${x3}$$/수식$$개씩 나누어 주면 몇 명에게 나누어 줄 수 있나요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$명\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$전체 {s1} 수$$수식$$RIGHT ) ` = ` {x1} ` times ` {x2} ` = ` {x4} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$LEFT ($$/수식$$나누어 줄 수 있는 사람 수$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$` = ` LEFT ($$/수식$$전체 {s1} 수$$수식$$RIGHT ) ` div ` LEFT ($$/수식$$한 명에게 나누어 주는 {s1} 수$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$` = ` {x4} ` div ` {x3} ` = ` {a1} LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$\n"\
              "따라서 {s1}{j2} $$수식$${a1}$$/수식$$명에게 나누어 줄 수 있습니다.\n\n"


    s1 = ['주사위', '장난감', '장난감 자동차', '연필꽂이', '계산기', '인형', '구슬', '과자'][np.random.randint(0, 8)]

    x1 = np.random.randint(2,10)
    x2 = np.random.randint(2,10)
    x4 = x1 * x2
    x3 = np.random.randint(2,10)

    while x4 % x3 != 0 or x4 // x3 > 9:
        x1 = np.random.randint(2,10)
        x2 = np.random.randint(2,10)
        x4 = x1 * x2
        x3 = np.random.randint(2,10)

    a1 = x4 // x3

    j1 = proc_jo(s1, 0)
    j2 = proc_jo(s1, 4)

    stem = stem.format(s1 = s1, j1 = j1, j2 = j2, x1 = x1, x2 = x2, x3 = x3)
    answer = answer.format(a1 = a1)
    comment = comment.format(s1 = s1, x1 = x1 , x2 = x2, x3 = x3, x4 = x4, a1 = a1, j2 = j2)

    return stem, answer, comment















#3-1-3-26
def division313_Stem_013():
    stem = "곱셈식을 나눗셈식으로 바꾸었습니다. □ 안에 알맞은 수를 써넣으세요.\n$$표$$ $$수식$${x1} ` times ` {x2} ` = ` {x3}$$/수식$$ $$/표$$\n→ $$수식$${x3} ` div ` {x2} ` = `$$/수식$$ $$수식$${box1}$$/수식$$      $$수식$${x3} ` div ` {x1} ` = ` $$/수식$$ $$수식$${box2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1} ` times ` {x2} ` = ` {x3}$$/수식$$\n"\
              "→ $$수식$${x3} ` div ` {x2} ` = ` {x1}$$/수식$$, $$수식$${x3} ` div ` {x1} ` = ` {x2}$$/수식$$\n\n"


    x1 = a1 = np.random.randint(2, 10)
    x2 = a2 = np.random.randint(2, 10)
    x3 = x1 * x2

    box1 = "box{　　}"
    box2 = "box{　　}"

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, box1 = box1, box2 = box2)
    answer = answer.format(a1 = a1, a2 = a2)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3)

    return stem, answer, comment













#3-1-3-34
def division313_Stem_014():
    stem = "□ 안에 알맞은 수를 써넣으세요\n$$수식$${x1} ` div ` {x2} ` = ` $$/수식$$ $$수식$${box1}$$/수식$$ → $$수식$${x2} ` times ` $$/수식$$ $$수식$${box2}$$/수식$$ $$수식$$ ` = ` {x1}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x2} ` times ` {x3} ` = ` {x1}$$/수식$$이므로 $$수식$${x1} ` div ` {x2}$$/수식$$의 몫은 $$수식$${x3}$$/수식$$입니다.\n\n"


    x2 = np.random.randint(2, 10)
    x3 = np.random.randint(2, 10)
    x1 = x2 * x3

    box1 = "box{　　　}"
    box2 = "box{　　　}"

    stem = stem.format(x1 = x1, x2 = x2, box1 = box1, box2 = box2)
    answer = answer.format(a1 = x3, a2 = x3)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3)

    return stem, answer, comment











#3-1-3-36
def division313_Stem_015():
    stem = "{s1} $$수식$${x1}$$/수식$$개를 $$수식$${x2}$$/수식$$명에게 똑같이 나누어 주었습니다. 한 명에게 {s1}{j1} 몇 개씩 주었나요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x2} ` times ` {x3} ` = ` {x1}$$/수식$$이므로 $$수식$${x1} ` div ` {x2} ` = ` {x3}$$/수식$$입니다.\n"\
              "따라서 한 명에게 {s1}{j1} $$수식$${x3}$$/수식$$개씩 주었습니다.\n\n"


    s1 = ['초콜릿', '사탕', '빵', '귤', '감', '구슬', '인형', '장난감'][np.random.randint(0, 8)]

    x2 = np.random.randint(2, 10)
    x3 = a1 = np.random.randint(2, 10)

    x1 = x2 * x3
    j1 = proc_jo(s1, 4)

    stem = stem.format(s1 = s1, x1 = x1, x2 = x2, j1 = j1)
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, j1 = j1, s1 = s1)

    return stem, answer, comment













#3-1-3-38
def division313_Stem_016():
    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 자연수 중에서 □ 안에 들어갈 수 있는 수를 모두 구해 보세요.\n$$표$$ $$수식$${x1} ` div ` {x2} ` &lt; ` $$/수식$$□$$/표$$\n"
    answer = "(정답)\n{a1} \n"
    comment = "(해설)\n$$수식$${x2} ` times ` {x3} ` = ` {x1}$$/수식$$에서 $$수식$${x1} ` div ` {x2} ` = ` {x3}$$/수식$$이므로 $$수식$${x3} ` &lt; `$$/수식$$□ 입니다.\n"\
              "따라서 □ 안에 들어갈 수 있는 수는 $$수식$${x3}$$/수식$$보다 큰 {s1}입니다.\n\n"


    while True:
        x2 = np.random.randint(2, 10)
        x3 = np.random.randint(2, 9)

        x1 = x2 * x3
        if x1 > 10 and x1 < 100:
            break

    s1 = ""

    for i in range(0, 9-x3):
        s1 = s1 + "$$수식$$" + str(x3 + i + 1) + "$$/수식$$" + ", "

    s1 = s1[0:-2]

    stem = stem.format(x1 = x1, x2 = x2)
    answer = answer.format(a1 = s1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, s1 = s1)

    return stem, answer, comment















#3-1-3-42
def division313_Stem_017():
    stem = "몫의 크기를 비교하여 ○ 안에 $$수식$$ &gt; $$/수식$$, $$수식$$=$$/수식$$, $$수식$$ &lt; $$/수식$$를 알맞게 써넣으세요.\n$$수식$${x1} ` div ` {x2}$$/수식$$ ○ $$수식$${x3} ` div ` {x4}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n곱셈구구를 이용하여 나눗셈의 몫을 구합니다.\n"\
              "$$수식$${x1} ` div ` {x2} ` = ` {x5}$$/수식$$, $$수식$${x3} ` div ` {x4} ` = ` {x6}$$/수식$$이므로 $$수식$${x1} ` div ` {x2} {a1} {x3} ` div ` {x4}$$/수식$$입니다.\n\n"


    while True:
        x2 = np.random.randint(2, 10)
        x5 = np.random.randint(2, 10)
        x1 = x2 * x5
        x4 = np.random.randint(2, 10)
        x6 = np.random.randint(2,10)
        x3 = x4 * x6

        if x2 != x4 and x1 > 10 and x3 > 10 and x1 != x3:
            break


    if x5 > x6:
        a1 = "&gt;"
    elif x5 == x6:
        a1 = "="
    else:
        a1 = "&lt;"

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4)
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6, a1 = a1)

    return stem, answer, comment












#3-1-3-43
def division313_Stem_018():
    stem = "$$수식$${x1}$$/수식$${ro1} 남김없이 나누어지는 수는 모두 몇 개인가요?\n$$표$$ $$수식$$ {x2}````{x3}````{x4}````{x5}````{x6}````{x7} $$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n$$수식$${x1}$$/수식$${ro1} 남김없이 나누어지는 수는 $$수식$${x1}$$/수식$$의 단 곱셈구구에서 찾습니다.\n"\
              "{s1}"\
              "따라서 $$수식$${x1}$$/수식$${ro1} 남김없이 나누어지는 수는 {s2}{ro2} 모두 $$수식$${a1}$$/수식$$개입니다.\n\n"



    while True:
        x1 = np.random.randint(2, 10)
        a1 = np.random.randint(1, 5)

        x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        num_list = []

        s1 = ""
        s2 = ""
        s3 = ""

        for i in range(a1):
            num = x_list.pop(np.random.randint(0, len(x_list)))
            num_list.append(num * x1)

            s1 = s1 + f"$$수식$${x1} ` times ` {num} ` = ` " + str(num * x1) + "$$/수식$$ → $$수식$$" + \
                 str(num * x1) + f" ` div ` {x1} ` = ` {num} $$/수식$$\n"

            s2 = s2 + "$$수식$$" + str(num * x1) + "$$/수식$$, "
            s3 = s3 + str(num * x1)


        s2 = s2[0:-2]

        for i in range(6 - a1):
            tmp = np.random.randint(11, 81)

            while tmp % x1 == 0:
                tmp = np.random.randint(11, 81)

            num_list.append(tmp)

        x2 = num_list.pop(np.random.randint(0, len(num_list)))
        x3 = num_list.pop(np.random.randint(0, len(num_list)))
        x4 = num_list.pop(np.random.randint(0, len(num_list)))
        x5 = num_list.pop(np.random.randint(0, len(num_list)))
        x6 = num_list.pop(np.random.randint(0, len(num_list)))
        x7 = num_list.pop(np.random.randint(0, len(num_list)))

        if 30 < x2 < 100 and 30 < x3 < 100 and 30 < x4 < 100 and 30 < x5 < 100 and 30 < x6 < 100 and 30 < x7 < 100:
            break


    if x1 == 3 or x1 == 6:
        ro1 = "으로"
    else:
        ro1 = "로"

    if (str(s3))[-1] == "3" or (str(s3))[-1] == "6" or (str(s3))[-1] == "0":
        ro2 = "으로"
    else:
        ro2 = "로"

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6, x7 = x7, ro1=ro1)
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, s1 = s1, s2 = s2, a1 = a1, ro1=ro1, ro2=ro2)

    return stem, answer, comment














#3-1-3-44
def division313_Stem_019():
    stem = "다음은 주어진 곱셈식을 나눗셈식으로 나타낸 것입니다. □ 안에 알맞은 수를 써넣으세요.\n$$표$$ $$수식$${x1} ` times ` {x2} ` = ` {x3}$$/수식$$ $$/표$$\n$$수식$${x3} ` div ` {x1} ` = ` $$/수식$$ $$수식$${box1}$$/수식$$ → 몫 : $$수식$${box2}$$/수식$$\n$$수식$${x3} ` div ` $$/수식$$ $$수식$${box3}$$/수식$$ $$수식$$ ` = ` {x1}$$/수식$$ → 몫 : $$수식$${box4}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$, $$수식$${a4}$$/수식$$ \n"
    comment = "(해설)\n$$수식$${x3} ` div ` {x1} ` = ` {x2}$$/수식$$, $$수식$${x3} ` div ` {x2} ` = ` {x1}$$/수식$$이므로 몫은 각각 $$수식$${x2}$$/수식$$, $$수식$${x1}$$/수식$$입니다.\n\n"


    x1 = np.random.randint(2,10)
    x2 = np.random.randint(2,10)

    while x1 == x2:
        x2 = np.random.randint(2,10)

    x3 = x1 * x2

    box1 = "box{　　　}"
    box2 = "box{　　　}"
    box3 = "box{　　　}"
    box4 = "box{　　　}"

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, box1 = box1, box2 = box2, box3 = box3, box4 = box4)
    answer = answer.format(a1 = x2, a2 = x2, a3 = x2, a4 = x1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3)

    return stem, answer, comment
















#3-1-3-47
def division313_Stem_020():
    stem = "나눗셈의 몫을 곱셈구구를 이용하여 구하려고 합니다. 몫을 구해 보세요.\n$$표$$ $$수식$${x1} ` div ` {x2}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x2}$$/수식$$의 단 곱셈구구에서 곱이 $$수식$${x1}$$/수식$$인 곱셈식은 $$수식$${x2} ` times ` {x3} ` = ` {x1}$$/수식$$입니다.\n"\
              "따라서 $$수식$${x1} ` div ` {x2} ` = ` {x3}$$/수식$$이므로 몫은 $$수식$${x3}$$/수식$$입니다.\n\n"


    x2 = np.random.randint(2,10)
    x3 = a1 = np.random.randint(2,10)

    x1 = x2 * x3

    while x1 < 30:
        x2 = np.random.randint(2,10)
        x3 = a1 = np.random.randint(2,10)
        x1 = x2 * x3

    stem = stem.format(x1 = x1, x2 = x2)
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3)

    return stem, answer, comment












#3-1-3-48
def division313_Stem_021():
    stem = "어떤 수를 $$수식$${x1}$$/수식$${j2} 나누었더니 몫이 $$수식$${x2}$$/수식$${j1} 되었습니다. 어떤 수를 $$수식$${x3}$$/수식$${j3} 나눈 몫을 구해보세요.\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n어떤 수를 □라고 하면 □$$수식$$ ` div ` {x1} ` = ` {x2}$$/수식$$입니다.\n → $$수식$${x1} ` times ` {x2} ` = ` $$/수식$$□, □$$수식$$` = ` {x4}$$/수식$$\n"\
              "따라서 어떤 수를 $$수식$${x3}$$/수식$${j3} 나누면 $$수식$${x4} ` div ` {x3} ` = ` {a1}$$/수식$$이므로 몫은 $$수식$${a1}$$/수식$$입니다.\n\n"


    # x1 = np.random.randint(2, 10)
    # x2 = np.random.randint(2, 10)
    # x3 = np.random.randint(2, 10)
    #
    # while x3 == x1 or x3 == x2:
    #     x3 = np.random.randint(2, 10)
    #
    # x4 = x1 * x2
    # a1 = x4 // x3
    #
    # while x4 % x3 != 0 or a1 > 9:
    #     x1 = np.random.randint(2, 10)
    #     x2 = np.random.randint(2, 10)
    #     x3 = np.random.randint(2, 10)
    #
    #     while x3 == x1 or x3 == x2:
    #         x3 = np.random.randint(2, 10)
    #
    #     x4 = x1 * x2
    #     a1 = x4 // x3

    while True:
        x1 = np.random.randint(2, 10)
        x2 = np.random.randint(2, 10)

        x4 = x1 * x2

        x3 = np.random.randint(2, 10)

        a1 = int(x4 / x3)

        if x4 % x3 == 0 and x3 != x1 and x3 != x2:
            break

    j1 = proc_jo(x2, 0)

    if x1 == 3 or x1 == 6:
        j2 = "으로"
    else:
        j2 = "로"

    if x3 == 3 or x3 == 6:
        j3 = "으로"
    else:
        j3 = "로"

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, j1 = j1, j2=j2, j3=j3)
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, a1 = a1, j3=j3)

    return stem, answer, comment






