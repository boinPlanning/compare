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
        check =(num - 44032) % 28
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



def addandsub122_Stem_001(): #1-2-2-01
    stem = "빈 곳에 알맞은 수를 써넣으시오.\n$$표$$$$수식$${boxone}{boxtwo}→{boxblank}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1} + {x2}$$/수식$${j1} $$수식$$10$$/수식$$개씩 묶음 $$수식$${x3}$$/수식$$개와 낱개 $$수식$${x4}$$/수식$$개이므로 $$수식$${a1}$$/수식$$입니다.\n"\
              "→ $$수식$${x1} + {x2} = {a1}$$/수식$$\n\n"

    while True:
        x1 = np.random.randint(11, 90)
        x2 = np.random.randint(1, 9)
        
        xx1 = x1 % 10
        if xx1 + x2 < 10:
            break
        
    a1 = x1 + x2
    j1 = proc_jo(x2, -1)
    x3 = a1 // 10
    x4 = a1 % 10

    boxone = "%d" % x1
    boxtwo = "+%d" % x2
    boxblank = "□"

    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxblank=boxblank) # 매핑시키기
    answer = answer.format(a1 = a1)
    comment = comment.format(x1 = x1, x2 = x2, j1 = j1, x3 = x3, x4 = x4, a1 = a1)

    return stem, answer, comment




def addandsub122_Stem_002(): #1-2-2-02
    stem = "가장 큰 수와 가장 작은 수의 합은 얼마인가요?\n$$표$$$$수식$${boxone}````{boxtwo}````{boxthree}````{boxfour}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${y1} &gt; {y2} &gt; {y3} &gt; {y4}$$/수식$$이므로 가장 큰 수는 $$수식$${y1}$$/수식$$, 가장 작은 수는 $$수식$${y4}$$/수식$$입니다.\n"\
              "$$수식$$($$/수식$$가장 큰 수$$수식$$) +($$/수식$$가장 작은 수$$수식$$) = {y1} + {y4} = {a1}$$/수식$$\n\n"

    while True:
        y1 = np.random.randint(50, 90)
        y2 = np.random.randint(11, y1)
        y3 = np.random.randint(10, y2)
        y4 = np.random.randint(1, 10)
        
        yy1 = y1 % 10
        if yy1 + y4 < 10:
            break

    candidates = [y1, y2, y3, y4]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4] = candidates

    a1 = y1 + y4

    #boxone = "BOX{````%d````}" % x1
    #boxtwo = "BOX{````%d````}" % x2
    #boxthree = "BOX{````%d````}" % x3
    #boxfour = "BOX{````%d````}" % x4

    stem = stem.format(boxone=x1, boxtwo=x2, boxthree=x3, boxfour=x4) # 매핑시키기
    answer = answer.format(a1 = a1)
    comment = comment.format(y1 = y1, y2 = y2, y3 = y3, y4 = y4, a1 = a1)

    return stem, answer, comment




def addandsub122_Stem_003(): #1-2-2-04
    stem = "계산 결과가 더 큰 것의 기호를 써 보세요.\n$$표$$㉠ {x1}\n㉡ {x2}$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n㉠ {x1} $$수식$$={x3}$$/수식$$\n㉡ {x2} $$수식$$={x4}$$/수식$$\n"\
              "따라서 $$수식$$ {x3} {s1} {x4}$$/수식$$ 이므로 계산 결과가 더 큰 것은 {a1}입니다.\n\n"

    while True:
        x3 = np.random.randint(11, 99)
        x4 = np.random.randint(11, 99)

        while x3 == x4 :
            x4 = np.random.randint(11,99)

        t1 = np.random.randint(1,10)
        t1_ = x3 - t1
        t2 = np.random.randint(1,10)
        t2_ = x4 - t2
        
        tt1 = t1_ % 10
        tt2 = t2_ % 10
        
        if tt1 + t1 < 10 and tt2 + t2 < 10:
            break

    x1 = "$$수식$$" + str(t1_)+"+"+str(t1)+"$$/수식$$"
    x2 = "$$수식$$" + str(t2_)+"+"+str(t2)+"$$/수식$$"

    if x3 > x4 :
        s1 = "&gt;"
        a1 = "㉠"
    else :
        s1 = "&lt;"
        a1 = "㉡"

    stem = stem.format(x1 = x1, x2 = x2)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, s1 = s1, a1 = a1)

    return stem, answer, comment





def addandsub122_Stem_004(): #1-2-2-05
    stem = "{s1}에 학생이 $$수식$${x1}$$/수식$$명 있습니다. 잠시 후 학생 $$수식$${x2}$$/수식$$명이 더 왔습니다. {s1}에 있는 학생은 모두 몇 명일까요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$명\n"
    comment = "(해설)\n$$수식$$($$/수식$${s1}에 있는 학생 수$$수식$$)$$/수식$$\n"\
              "$$수식$$= ````($$/수식$$처음에 있던 학생 수$$수식$$) +($$/수식$$더 온 학생 수$$수식$$)$$/수식$$\n"\
              "$$수식$$= {x1} + {x2} = {a1}($$/수식$$명$$수식$$)$$/수식$$\n\n"

    s1 = ['운동장', '교실', '체육관', '놀이공원'][np.random.randint(0,4)]
    
    while True:
        x1 = np.random.randint(11, 90)
        x2 = np.random.randint(1, 9)
        
        xx1 = x1 % 10
        if xx1 + x2 < 10:
            break
        
    a1 = x1 + x2

    stem = stem.format(x1 = x1, x2 = x2, s1 = s1)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1 = x1, x2 = x2,a1 = a1, s1 = s1)

    return stem, answer, comment



def addandsub122_Stem_005(): #1-2-2-06
    stem = "수 카드 중에서 $$수식$$2$$/수식$$장을 골라 한 번씩만 사용하여 몇십몇을 만들어 남은 수와 더하려고 합니다. 합이 가장 큰 덧셈식을 써 보세요.\n$$수식$${boxone}$$/수식$$  $$수식$${boxtwo}$$/수식$$  $$수식$${boxthree}$$/수식$$\n$$표$${boxoneone}$$수식$$ `` {y3} `` + ``$$/수식$${boxtwotwo}$$수식$$``= ``$$/수식$${boxthreethree}$$/표$$\n"
    answer = "(정답)\n① $$수식$${y1}$$/수식$$, ② $$수식$${y2}$$/수식$$, ③ $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n합이 가장 크려면 $$수식$$10$$/수식$$개를 묶음의 수가 가장 큰 몇십몇을 만들면 됩니다.\n"\
              "$$수식$$ {y1}````&gt;````{y3}````&gt;{y2}$$/수식$$이므로 $$수식$$10$$/수식$$개씩 묶음의 수가 $$수식$${y1}$$/수식$$인 몇십몇을 만듭니다.\n"\
              "→ $$수식$${x4}`+`{y2}`=`{a1}$$/수식$$\n\n"

    while True:
        y1 = np.random.randint(4, 10)
        y3 = np.random.randint(2, y1)
        y2 = np.random.randint(1, y3)

        if y1 == 9 : # 답이 100이 넘지 않게
            while y3 + y2 >= 10:
                y3 = np.random.randint(2, y1)
                y2 = np.random.randint(1, y3)

        candidates = [y1, y2, y3]
        np.random.shuffle(candidates)
        [x1, x2, x3] = candidates

        x4 = y1*10 + y3
        a1 = x4 + y2
        
        xx4 = x4 % 10
        if xx4 + y2 < 10:
            break

    boxone = "BOX{````%d````}" % x1
    boxtwo = "BOX{````%d````}" % x2
    boxthree = "BOX{````%d````}" % x3
    boxoneone = "①"
    boxtwotwo = "②"
    boxthreethree = "③"

    stem = stem.format(y3=y3, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxoneone=boxoneone, boxtwotwo=boxtwotwo, boxthreethree=boxthreethree)  # 매핑시키기
    answer = answer.format(y1 = y1, y2 = y2, a1 = a1)
    comment = comment.format(y1 = y1, y2 = y2, y3 = y3, x4 = x4, a1 = a1)

    return stem, answer, comment



def addandsub122_Stem_006(): #1-2-2-07
    stem = "수 카드 $$수식$${boxone}$$/수식$$, $$수식$${boxtwo}$$/수식$$, $$수식$${boxthree}$$/수식$${j1} 한 번씩 모두 사용하여 다음과 같은 덧셈식을 만들었습니다. 만든 덧셈식의 합이 가장 클 때의 합을 구해 보세요.\n$$표$${boxa} {boxb} $$수식$$+$$/수식$$ {boxc}$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n{boxa} {boxb} $$수식$$+$$/수식$$ {boxc}\n"\
              "합이 가장 크려면 ㉠은 가장 큰 수인 $$수식$${x3}$$/수식$${j1} 놓습니다. → $$수식$${x4}`+`{x1}`=`{a1}$$/수식$$\n\n"

    while True:
        x3 = np.random.randint(4, 10)
        x2 = np.random.randint(2, x3)
        x1 = np.random.randint(1, x2)

        if x3 == 9 :
            while x2 + x1 >= 10 :
                x2 = np.random.randint(2, x3)
                x1 = np.random.randint(1, x2)
        x4 = x3 * 10 + x2
        
        xx4 = x4 % 10
        if xx4 + x1 < 10:
            break
        
    a1 = x4 + x1

    j1 = proc_jo(x3, 4)

    boxone = "BOX{``%d``}" % x1
    boxtwo = "BOX{``%d``}" % x2
    boxthree = "BOX{``%d``}" % x3
    boxblank = "BOX{　}"
    boxa = "㉠"
    boxb = "㉡"
    boxc = "㉢"

    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxblank=boxblank, j1 = j1, boxa=boxa, boxb=boxb, boxc=boxc)  # 매핑시키기
    answer = answer.format(a1 = a1)
    comment = comment.format(boxa=boxa, boxb=boxb, boxc=boxc, x1=x1, x3 = x3, x4 = x4, j1 = j1, a1 = a1)

    return stem, answer, comment



def addandsub122_Stem_007(): #1-2-2-12
    stem = "$$수식$${x1} `+` {x2} `=` {x3}$$/수식$${j1} 이용하여 $$수식$${boxblank}$$/수식$$ 안에 알맞을 수를 써넣으세요.\n$$표$$ $$수식$${x4} `+` {x5} `=` {boxblank}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1} `+` {x2} `=` {x3}$$/수식$$이므로 $$수식$${x4} `+` {x5}$$/수식$$은 $$수식$$10$$/수식$$개씩 묶음이 $$수식$${x1} `+` {x2} `=` {x3}$$/수식$$(개)입니다.\n"\
              "따라서 $$수식$$10$$/수식$$개씩 묶음 $$수식$${x3}$$/수식$$개는 $$수식$${a1}$$/수식$$이므로 $$수식$${boxblank}$$/수식$$ 안에 알맞은 수는 $$수식$${a1}$$/수식$$입니다.\n\n"

    x1 = np.random.randint(1, 9)
    x2 = np.random.randint(1, 9)

    while x1 == x2 or x1 + x2 >= 10 :
        x2 = np.random.randint(1, 10)

    x3 = x1 + x2
    x4 = x1 * 10
    x5 = x2 * 10
    a1 = x4 + x5

    j1 = proc_jo(x3, 4)

    boxblank = "□"
    boxone = "①"

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, j1 = j1, boxblank=boxblank)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, a1 = a1, boxblank=boxblank)

    return stem, answer, comment



def addandsub122_Stem_008(): #1-2-2-13
    stem = "{s1}{j1} {wh1}{j2} $$수식$${x1}$$/수식$$번 하였고 {wh2}{j3} $$수식$${x2}$$/수식$$번 하였습니다. {wh1}{j4} {wh2}{j5} 한 {s1}{j6} 모두 몇 번인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$번\n"
    comment = "(해설)\n$$수식$$($$/수식$${wh1}{j4} {wh2}{j5} 한 {s1}의 수의 합$$수식$$)$$/수식$$\n"\
              "$$수식$$= ````($$/수식$${wh1}{j7} 한 {s1}의 수$$수식$$) +($$/수식$${wh2}{j5} 한 {s1}의 수$$수식$$)$$/수식$$\n"\
              "$$수식$$=` {x1} `+` {x2} `=` {a1}($$/수식$$번$$수식$$ )$$/수식$$\n\n"

    s1 = ['윗몸 일으키기', '팔굽혀 펴기', '줄넘기', '훌라후프'][np.random.randint(0, 4)]
    wh1 = ['경진이', '민지', '예원이', '유나'][np.random.randint(0, 4)]
    wh2 = ['정우', '우찬이', '현수', '은정이'][np.random.randint(0, 4)]

    j1 = proc_jo(s1, 4)
    j2 = proc_jo(wh1, -1)
    j3 = proc_jo(wh2, -1)
    j4 = proc_jo(wh1, 2)
    j5 = proc_jo(wh2, 0)
    j6 = proc_jo(s1, -1)
    j7 = proc_jo(wh1, 0)

    x1 = np.random.randint(1, 9) * 10
    x2 = np.random.randint(1, 9) * 10

    while x1 == x2 or x1 + x2 >= 100 :
        x2 = np.random.randint(1, 9) * 10

    a1 = x1 + x2

    stem = stem.format(s1 = s1, wh1 = wh1, wh2 = wh2, x1 = x1, x2 = x2, j1 = j1, j2 = j2, j3 = j3, j4 = j4, j5 = j5, j6 = j6)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(s1 = s1, wh1 = wh1, wh2 = wh2, x1 = x1, x2 = x2, a1 = a1, j4 = j4, j5 = j5, j7 = j7)

    return stem, answer, comment



def addandsub122_Stem_009(): #1-2-2-15
    stem = "계산 결과의 크기를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$표$$$$수식$${boxone} ○ {boxtwo}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1} `+` {x2} `=` {x5}$$/수식$$, $$수식$${x3} `+` {x4} `=` {x6}$$/수식$$\n"\
              "$$수식$${x5} `{a1}` {x6} $$/수식$$이므로 $$수식$${x1} `+` {x2} `{a1}` {x3} `+` {x4} $$/수식$$입니다.\n\n"

    x5 = np.random.randint(30, 100)
    x6 = np.random.randint(30, 100)

    while(x5 == x6) :
        x5 = np.random.randint(20, 100)

    if(x5 > x6) :
        a1 = "&gt;"
    else :
        a1 = "&lt;"

    while True:
        x1 = np.random.randint(10, x5)
        x2 = x5 - x1

        x3 = np.random.randint(10, x6)
        x4 = x6 - x3
        
        xx1 = x1 % 10
        xx3 = x3 % 10
        if xx1 + x2 < 10 and xx3 + x4 < 10:
            break

    boxone = "%s``+``%s" %(x1, x2)
    boxtwo = "%s``+``%s" %(x3, x4)

    stem = stem.format(boxone=boxone, boxtwo=boxtwo)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 =x6, a1 = a1)

    return stem, answer, comment



def addandsub122_Stem_010(): #1-2-2-18
    stem = "$$수식$$0$$/수식$$부터 $$수식$$9$$/수식$$까지의 숫자 중에서 $$수식$${boxblank}$$/수식$$ 안에 들어갈 수 있는 숫자는 모두 몇 개인가요?\n$$표$$ $$수식$${x1} `+` {x2} `&gt;` {x3}`{boxblank} $$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n$$수식$${x1} `+` {x2} `=` {x4}$$/수식$$이므로 $$수식$$ {x4} `&gt;` {x3}`{boxblank}$$/수식$$입니다.\n"\
              "$$수식$$10$$/수식$$개씩 묶음의 수가 같으므로 $$수식$${boxblank}$$/수식$$ 안에 들어갈 수 있는 숫자는 $$수식$${x3}$$/수식$$보다 작은 {s1}이므로 "\
              "$$수식$${a1}$$/수식$$개입니다.\n\n"

    x4 = np.random.randint(30, 100)
    while x4 % 10 == 0 :
        x4 = np.random.randint(30, 100)
    x1 = np.random.randint(11, x4)
    x2 = x4 - x1
    x3 = x4 // 10

    s1 = ""
    a1 = x4 % 10
    for i in range(0, x4 % 10) :
        s1 = s1 + "$$수식$$" + str(i) + "$$/수식$$" +", "
    s1 = s1[0:-2]

    boxblank = "□"

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, boxblank=boxblank)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, s1 = s1, a1 = a1, boxblank=boxblank)

    return stem, answer, comment



def addandsub122_Stem_011(): #1-2-2-23
    stem = "바구니에 {s1}{j1} $$수식$${x1}$$/수식$$개 있었습니다. {wh1}{j2} 바구니에 있는 {s1} $$수식$${x2}$$/수식$$개를 먹었습니다. 바구니에 남아 있는 {s1}{j3} 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n$$수식$$($$/수식$$남아 있는 {s1}의 수$$수식$$)$$/수식$$\n"\
              "$$수식$$= ````($$/수식$$처음 {s1}의 수$$수식$$) - ($$/수식$$먹은 {s1}의 수$$수식$$)$$/수식$$\n"\
              "$$수식$$=` {x1} `-` {x2} `=` {a1}($$/수식$$개$$수식$$)$$/수식$$\n\n"

    s1 = ['귤', '사과', '사탕', '과자', '자두'][np.random.randint(0, 5)]
    wh1 = ['진수', '민수', '하성이', '정후'][np.random.randint(0, 4)]
    j1 = proc_jo(s1, 0)
    j2 = proc_jo(wh1, 0)
    j3 = proc_jo(s1, -1)

    while True:
        x1 = np.random.randint(11, 100)
        x2 = np.random.randint(1, 10)
        
        xx1 = x1 % 10
        if xx1 - x2 >= 0:
            break
    a1 = x1 - x2

    stem = stem.format(x1 = x1, x2 = x2, s1 = s1, wh1 = wh1, j1 = j1, j2 = j2, j3 = j3)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(s1 = s1, x1 = x1, x2 = x2, a1 = a1)

    return stem, answer, comment



def addandsub122_Stem_012(): #1-2-2-25
    stem = "{wh1}{j1} {wh2}{j2} 말한 수의 차는 얼마인지 구해 보세요.\n$$표$$[{wh1}]  $$수식$${x1}$$/수식$$보다 $$수식$$1$$/수식$$ 큰 수\n[{wh2}]  $$수식$${x2}$$/수식$$보다 $$수식$$1$$/수식$$ 작은 수$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n{wh1} : $$수식$${x1}$$/수식$$보다 $$수식$$1$$/수식$$ 큰 수는 $$수식$${x1}$$/수식$$ 바로 뒤의 수이므로 $$수식$${x3}$$/수식$$입니다.\n"\
              "{wh2} : $$수식$${x2}$$/수식$$보다 $$수식$$1$$/수식$$ 작은 수는 $$수식$${x2}$$/수식$$ 바로 앞의 수이므로 $$수식$${x4}$$/수식$$입니다.\n"\
              "따라서 $$수식$${y1} `>` {y2}$$/수식$$ 이므로 {wh1}{j1} {wh2}{j2} 각각 말한 수의 차는 $$수식$${y1} `-` {y2} `=` {a1} $$/수식$$입니다.\n\n"

    wh1 = ['현지', '민재', '성은', '주성'][np.random.randint(0, 4)]
    wh2 = ['종찬', '현오', '세호', '정환'][np.random.randint(0, 4)]

    j1 = proc_jo(wh1, 2)
    j2 = proc_jo(wh2, 0)

    while True:
        x1 = np.random.randint(11, 98)
        x2 = np.random.randint(11, 98)

        while x1 == x2 :
            x2 = np.random.randint(11, 98)

        x3 = x1 + 1
        x4 = x2 - 1

        if x3 > x4 :
            y1 = x3
            y2 = x4
        else :
            y1 = x4
            y2 = x3
            
        yy1 = y1 % 10
        yy2 = y2 % 10
        if yy1 - yy2 >= 0:
            break

    a1 = y1 - y2

    stem = stem.format(wh1 = wh1, wh2 = wh2, j1 = j1, j2 = j2, x1 = x1, x2 = x2)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(wh1 = wh1, wh2 = wh2, x1 = x1, x2 = x2, x3 = x3, x4 = x4, y1 = y1, y2 = y2, a1 = a1, j1 = j1, j2 = j2)

    return stem, answer, comment



def addandsub122_Stem_013(): #1-2-2-27
    stem = "가와 나의 차가 얼마인지 구해 보세요.\n$$표$$가 : {boxone} \n나 : {boxtwo}$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n가 : {s1} → $$수식$${x1}$$/수식$$, 나 : {s2} → $$수식$${x2}$$/수식$$\n"\
              "$$수식$$($$/수식$$가와 나의 차$$수식$$) ```` =` {x1} `-` {x2} `=` {a1}$$/수식$$\n\n"

    s_list = ['열', '스물', '서른', '마흔', '쉰', '예순', '일흔', '여든', '아흔']
    s2_list = ['십', '이십', '삼십', '사십', '오십', '육십', '칠십', '팔십', '구십']

    t1 = np.random.randint(1, 9)
    t2 = np.random.randint(0, t1)

    s1 = s_list[t1]
    s2 = s2_list[t2]

    x1 =(t1+1)*10
    x2 =(t2+1)*10

    a1 = x1 - x2

    #boxone = "BOX{````%s````}" % s1
    #boxtwo = "BOX{````%s````}" % s2

    stem = stem.format(boxone=s1, boxtwo=s2)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(s1 = s1, s2 = s2, x1 = x1, x2 = x2, a1 = a1)

    return stem, answer, comment



def addandsub122_Stem_014(): #1-2-2-29
    stem = "계산 결과의 크기를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$표$$$$수식$${boxone} BIGCIRC {boxtwo}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1} `-` {x2} `=` {x5}$$/수식$$, $$수식$${x3} `-` {x4} `=` {x6}$$/수식$$\n" \
              "$$수식$${x5} `{a1}` {x6} $$/수식$$이므로 $$수식$${x1} `-` {x2} `{a1}` {x3} `-` {x4} $$/수식$$입니다.\n\n"

    while True :
        x1 = np.random.randint(50, 100)
        x3 = np.random.randint(50, 100)
        x2 = np.random.randint(10, x1)
        x4 = np.random.randint(10, x3)
        x5 = x1 - x2
        x6 = x3 - x4
        
        xx1 = x1 % 10
        xx2 = x2 % 10
        
        xx3 = x3 % 10
        xx4 = x4 % 10
        if(x1 != x3) and (x5 != x6) and (xx1 - xx2) >= 0 and (xx3 - xx4) >= 0:
            break

    if x5 > x6 :
        a1 = "&gt;"
    else :
        a1 = "&lt;"

    boxone = "%s - %s" %(x1, x2)
    boxtwo = "%s - %s" %(x3, x4)

    stem = stem.format(boxone=boxone, boxtwo=boxtwo)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6, a1 = a1)

    return stem, answer, comment



def addandsub122_Stem_015(): #1-2-2-31
    stem = "{wh1}{j1} 모은 {s1}{j2} $$수식$${x1}$$/수식$$개이고, {wh2}{j3} 모은 {s1}{j2} $$수식$${x2}$$/수식$$개입니다. 누가 {s1}{j4} 몇 개 더 많이 모았는지 구해 보세요.\n$$표$$$$수식$${boxone}$$/수식$$가 {s1}{j4} $$수식$${boxtwo}$$/수식$$개 더 많이 모았습니다.$$/표$$\n"
    answer = "(정답)\n① {a1}, ② $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n$$수식$$ {x1} `{s2}` {x2}$$/수식$$이므로\n"\
              "$$수식$$($$/수식$${wh3}{j5} 모은 {s1}의 수$$수식$$) -($$/수식$${wh4}{j6} 모은 {s1}의 수$$수식$$)$$/수식$$\n"\
              "$$수식$$=` {x3} `-` {x4} `=` {a2}($$/수식$$개$$수식$$)$$/수식$$\n"\
              "따라서 {wh3}{j5} {s1}{j4} $$수식$${a2}$$/수식$$개 더 많이 모았습니다.\n\n"

    wh1 = ['철우', '종현', '지환', '주현'][np.random.randint(0, 4)]
    wh2 = ['현서', '재성', '영서', '한결'][np.random.randint(0, 4)]
    s1 = ['구슬', '딱지', '칭찬 스티커'][np.random.randint(0, 3)]

    j1 = proc_jo(wh1, 0)
    j2 = proc_jo(s1, -1)
    j3 = proc_jo(wh2, 0)
    j4 = proc_jo(s1, 4)

    while True:
        x1 = np.random.randint(11, 100)
        x2 = np.random.randint(11, 100)
        while x1 == x2 :
            x2 = np.random.randint(11, 100)
            
        xx1 = x1 % 10
        xx2 = x2 % 10
        
        if x1 > x2 :
            if xx1 - xx2 >= 0:
                break
        else:
            if xx2 - xx1 >= 0:
                break

    if x1 > x2 :
        a1 = wh1
        a2 = x1 - x2
        s2 = "&gt;"
        wh3 = wh1
        wh4 = wh2
        x3 = x1
        x4 = x2
    else :
        a1 = wh2
        a2 = x2 - x1
        s2 = "&lt;"
        wh3 = wh2
        wh4 = wh1
        x3 = x2
        x4 = x1

    j5 = proc_jo(wh3, 0)
    j6 = proc_jo(wh4, 0)

    boxone = "BOX{````①````}"
    boxtwo = "BOX{````②````}"

    stem = stem.format(s1 = s1, wh1 = wh1, wh2 = wh2, j1 = j1, j2 = j2, j3 = j3, j4 = j4, x1 = x1, x2 = x2, boxone=boxone, boxtwo=boxtwo)  # 매핑시키기
    answer = answer.format(a1=a1, a2 = a2)
    comment = comment.format(wh1 = wh1, wh2 = wh2, wh3 = wh3, wh4 = wh4, j4 = j4, j5 = j5, j6 = j6, x1= x1, x2 = x2, x3 = x3, x4 = x4, s1 = s1, s2 = s2, a2 = a2)

    return stem, answer, comment



def addandsub122_Stem_016(): #1-2-2-32
    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 숫자 중에서 $$수식$${boxblank}$$/수식$$ 안에 들어갈 수 있는 가장 작은 숫자를 구해 보세요.\n$$표$$$$수식$$ {x1} `-` {x2} `&lt;` {boxblank} ``{x3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1} `-` {x2} `=` {x4}$$/수식$$이므로 "\
              "$$수식$${x4} `&lt;` {boxblank} ``{x3}$$/수식$$입니다.\n"\
              "낱개의 수를 비교해 보면 $$수식$${x5} `{s1}` {x3}$$/수식$$이므로 □ 안에 "\
              "들어 갈 수 있는 숫자는 {s2}보다 큰 숫자입니다. \n"\
              "따라서 $$수식$${boxblank}$$/수식$$ 안에 들어갈 수 있는 가장 작은 숫자는 $$수식$${a1}$$/수식$$입니다.\n\n"

    while True:
        x1 = np.random.randint(20, 100)
        x2 = np.random.randint(10, x1)
        x4 = x1 - x2
        x5 = x4 % 10
        x3 = np.random.randint(1, 10)
        
        xx1 = x1 % 10
        xx2 = x2 % 10
        if(x5 != x3) and xx1 - xx2 >= 0:
            break

    if( x5 > x3):
        s1 = "&gt;"
        a1 = x4 // 10 + 1
        s2 = "$$수식$$"+str(x4 // 10)+"$$/수식$$"
    else :
        s1 = "&lt;"
        a1 = x4 // 10
        s2 = "$$수식$$" + str(a1) +"$$/수식$$이거나 "+"$$수식$$"+str(a1)+"$$/수식$$"

    boxblank = "□"

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, boxblank=boxblank)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, s1 = s1, s2 = s2, a1 = a1, boxblank=boxblank)

    return stem, answer, comment



def addandsub122_Stem_017(): #1-2-2-33
    stem = "㉠, ㉡에 각각 알맞은 숫자를 구해 보세요.\n$$표$$ {boxa}$$수식$$ `{x1} `-` {x2}`$$/수식$${boxb}$$수식$$`=` {x3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n낱개끼리 빼면 $$수식$${x1} `-` $$/수식$$ ㉡ $$수식$$=` {x4}$$/수식$$에서 "\
              "$$수식$${x1} `-` {a2} `=` {x4}$$/수식$$이므로 ㉡ $$수식$$=` {a2}$$/수식$$입니다.\n"\
              "$$수식$$10$$/수식$$개씩 묶음끼리 빼면 ㉠ $$수식$$-` {x2} `=` {x5}$$/수식$$에서 "\
              "$$수식$${a1} `-` {x2} `=` {x5}$$/수식$$이므로 ㉠ $$수식$$=` {a1}$$/수식$$입니다.\n\n"
    
    x1 = np.random.randint(2, 10)
    a2 = np.random.randint(1, x1)

    a1 = np.random.randint(1, 10)
    x2 = np.random.randint(1, a1)

    x3 =(a1*10 + x1) -(x2*10 + a2)
    x4 = x3 % 10
    x5 = x3 // 10

    boxa = "㉠"
    boxb = "㉡"

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, boxa=boxa, boxb=boxb)  # 매핑시키기
    answer = answer.format(a1=a1, a2 = a2)
    comment = comment.format(x1 = x1, x2 = x2, x4 = x4, x5 = x5, a1 = a1, a2 = a2)

    return stem, answer, comment



def addandsub122_Stem_018(): #1-2-2-34
    stem = "수 카드를 한 번씩만 사용하여 몇십몇을 만들려고 합니다. 만들 수 있는 가장 큰 수와 가장 작은 수의 차를 구해 보세요.\n$$수식$${boxone}$$/수식$$$$수식$${boxtwo}$$/수식$$$$수식$${boxthree}$$/수식$$$$수식$${boxfour}$$/수식$$$$수식$${boxfive}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n가장 큰 수는 큰 숫자부터 $$수식$$10$$/수식$$개씩 묶음의 수, 낱개의 수에 차례대로 놓습니다. → $$수식$${x6}$$/수식$$\n"\
              "가장 작은 수는 작은 숫자부터 $$수식$$10$$/수식$$개씩 묶음의 수, 낱개의 수에 차례대로 놓습니다. → $$수식$${x7}$$/수식$$\n"\
              "$$수식$$($$/수식$$가장 큰 수$$수식$$)`-`($$/수식$$가장 작은 수$$수식$$)`=` {x6} `-` {x7} `=` {a1}$$/수식$$\n\n"

    while True:
        nset = []
        for i in range(1, 10) :
            nset.append(i)
        nlist = []
        for i in range(5):
            nlist.append(nset.pop(np.random.randint(0, len(nset))))
        nlist.sort()

        x1 = nlist[0]
        x2 = nlist[1]
        x3 = nlist[2]
        x4 = nlist[3]
        x5 = nlist[4]
        
        if x4 - x2 >= 0:
            break

    x6 = x5*10 + x4
    x7 = x1*10 + x2
    a1 = x6 - x7

    boxone = "BOX{``%d``}" % x1
    boxtwo = "BOX{``%d``}" % x2
    boxthree = "BOX{``%d``}" % x3
    boxfour = "BOX{``%d``}" % x4
    boxfive = "BOX{``%d``}" % x5

    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour, boxfive=boxfive)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x6 = x6, x7 = x7, a1 = a1)

    return stem, answer, comment



def addandsub122_Stem_019(): #1-2-2-36
    stem = "▲에 알맞은 수를 구해 보세요.\n$$표$$ $$수식$${x1} `-` {x2} `=` $$/수식$$ ★\n★ $$수식$$+$$/수식$$ ★ $$수식$$=$$/수식$$ ●\n● $$수식$$+$$/수식$$ ● $$수식$$=$$/수식$$ ▲$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1} `-` {x2} `=` {x3}$$/수식$$ → ★ $$수식$$=` {x3}$$/수식$$\n"\
              "$$수식$${x3} `+` {x3} `=` {x4}$$/수식$$ → ● $$수식$$=` {x4}$$/수식$$\n"\
              "$$수식$${x4} `+` {x4} `=` {a1}$$/수식$$ → ▲ $$수식$$=` {a1}$$/수식$$\n"\
              "따라서 ▲에 알맞은 수는 $$수식$${a1}$$/수식$$입니다.\n\n"

    while True:
        x1 = np.random.randint(11, 25)
        x2 = np.random.randint(1, 10)
        
        xx1 = x1 % 10
        if xx1 - x2 >= 0:
            break
        
    x3 = x1 - x2
    x4 = x3 + x3
    a1 = x4 + x4

    stem = stem.format(x1 = x1, x2 = x2)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, a1 = a1)

    return stem, answer, comment



def addandsub122_Stem_020(): #1-2-2-37
    stem = "어떤 수에 $$수식$${x1}$$/수식$${j1} 더했더니 $$수식$${x2}$$/수식$${j2} 되었습니다. 어떤 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n어떤 수를 $$수식$${boxblank}$$/수식$$라 하면 $$수식$${boxblank} `+` {x1} `=` {x2}$$/수식$$입니다.\n"\
              "→ $$수식$${x2} `-` {x1} `=` {a1}$$/수식$$\n\n"

    while True:
        x2 = np.random.randint(30, 100)
        a1 = np.random.randint(10, x2)
        
        xx2 = x2 % 10
        aa1 = a1 % 10
        if xx2 - aa1 >= 0:
            break
        
    x1 = x2 - a1

    j1 = proc_jo(x1, 4)
    j2 = proc_jo(x2, 0)

    boxblank = "□"

    stem = stem.format(x1 = x1, x2 = x2, j1 = j1, j2 = j2)  # 매핑시키기
    answer = answer.format(a1=a1)
    comment = comment.format(x1 = x1, x2 = x2, a1 = a1, boxblank=boxblank)

    return stem, answer, comment

