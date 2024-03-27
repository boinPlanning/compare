import numpy as np
import operator
import fractions




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






def gcd (a, b):
    if b == 0:
        return a
    else :
        if a < b:
            a, b = b, a
        return gcd(b, a % b)





def lcm(a, b):
    return a * b // gcd(a, b)





# 6-1-1-04
def fractiondiv611_Stem_001():
    stem = "$$수식$${x1} ` div ` {x2}$$/수식$$의 몫과 같은 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${x3}$$/수식$$   ㉡ $$수식$${x4}$$/수식$$   ㉢ $$수식$${x5}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n$$수식$${x1} ` div ` {x2} ` = ` {x1}over{x2}$$/수식$$이므로 {a1}과 같습니다.\n\n"


    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(2, 10)
        t2 = t2_ = np.random.randint(t1, 100)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    x1 = t1
    x2 = t2

    y1 = f"{x2} over {x1}"
    y2 = f"{x1} over {x2}"
    y3 = f"{x2} ` div ` {x1}"

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [x3, x4, x5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y2:
            correct_idx = idx
            break

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(x1=x1, x2=x2, a1=answer_kodict[correct_idx])

    return stem, answer, comment











# 6-1-1-06
def fractiondiv611_Stem_002():
    stem = "나눗셈의 몫을 분수로 바르게 나타낸 것은 어느 것인가요?\n① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n"\
              "① {c1}\n"\
              "② {c2}\n"\
              "③ {c3}\n"\
              "④ {c4}\n"\
              "⑤ {c5}\n \n\n"


    y_list = []
    z_list = []
    #서로소

    ch = 0

    while ch == 0 :
        t1 = t1_ = np.random.randint(2, 80)
        t2 = t2_ = np.random.randint(t1, 100)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1 :
            ch = 1

    y_list.append(f"$$수식$$ {t1} ` div ` {t2} ` = ` "+str(t1*t2)+"$$/수식$$")
    z_list.append(f"$$수식$$ {t1} ` div ` {t2} ` = ` {t1} over {t2} $$/수식$$")

    ch = 0
    while ch == 0:
        t1 = t1_ = np.random.randint(2, 80)
        t2 = t2_ = np.random.randint(t1, 100)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    y_list.append(f"$$수식$$ {t1} ` div ` {t2} ` = ` {t1} over {t2} $$/수식$$")
    z_list.append(f"$$수식$$ {t1} ` div ` {t2} ` = ` {t1} over {t2} $$/수식$$")

    ch = 0
    while ch == 0:
        t1 = t1_ = np.random.randint(2, 80)
        t2 = t2_ = np.random.randint(t1, 100)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    y_list.append(f"$$수식$$ {t1} ` div ` {t2} ` = ` {t2}over"+str(t1*t2)+"$$/수식$$")
    z_list.append(f"$$수식$$ {t1} ` div ` {t2} ` = ` {t1}over{t2} $$/수식$$")

    ch = 0
    while ch == 0:
        t1 = t1_ = np.random.randint(2, 80)
        t2 = t2_ = np.random.randint(t1, 100)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    y_list.append(f"$$수식$$ {t1} ` div ` {t2} ` = ` "+str(t2-t1)+"$$/수식$$")
    z_list.append(f"$$수식$$ {t1} ` div ` {t2} ` = ` {t1}over{t2} $$/수식$$")

    ch = 0
    while ch == 0:
        t1 = t1_ = np.random.randint(2, 80)
        t2 = t2_ = np.random.randint(t1, 100)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    y_list.append(f"$$수식$$ {t1} ` div ` {t2} ` = ` {t2}over{t1} $$/수식$$")
    z_list.append(f"$$수식$$ {t1} ` div ` {t2} ` = ` {t1}over{t2} $$/수식$$")

    num_list = [0, 1, 2, 3, 4]

    num = num_list.pop(np.random.randint(0, len(num_list)))

    x1 = y_list[num]
    c1 = z_list[num]

    if num == 1 :
        a1 = "①"

    num = num_list.pop(np.random.randint(0, len(num_list)))

    x2 = y_list[num]
    c2 = z_list[num]

    if num == 1:
        a1 = "②"
    num = num_list.pop(np.random.randint(0, len(num_list)))
    x3 = y_list[num]
    c3 = z_list[num]
    if num == 1:
        a1 = "③"

    num = num_list.pop(np.random.randint(0, len(num_list)))

    x4 = y_list[num]
    c4 = z_list[num]

    if num == 1:
        a1 = "④"

    num = num_list.pop(np.random.randint(0, len(num_list)))

    x5 = y_list[num]
    c5 = z_list[num]

    if num == 1:
        a1 = "⑤"

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=a1)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)

    return stem, answer, comment











# 6-1-1-07
def fractiondiv611_Stem_003():
    stem = "□ 안에 알맞은 분수를 구해 보세요.\n$$표$$ □$$수식$$ ` times ` {x1} ` = ` {x2}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1} over {a2}$$/수식$$\n"
    comment = "(해설)\n□$$수식$$` times ` {x1} ` = ` {x2}$$/수식$$ → □$$수식$$` = ` {x2} ` div ` {x1} ` = ` {x2} over {x1}$$/수식$$\n\n"


    ch = 0

    while ch == 0:
        x1 = x1_ = np.random.randint(2, 80)
        x2 = x2_ = np.random.randint(x1, 100)
        while x2_:
            r = max(x1_, x2_) % min(x1_, x2_)
            x1_ = min(x1_, x2_)
            x2_ = r
        if x1_ == 1:
            ch = 1

    stem = stem.format(x1=x1, x2=x2)
    answer = answer.format(a1=x2, a2=x1)
    comment = comment.format(x1=x1, x2=x2)

    return stem, answer, comment














# 6-1-1-08
def fractiondiv611_Stem_004():
    stem = "나눗셈의 몫의 크기를 비교하여 ○ 안에 $$수식$$ ` &gt; ` $$/수식$$, $$수식$$ ` = ` $$/수식$$, $$수식$$ ` &lt; ` $$/수식$$를 알맞게 써넣으세요.\n$$수식$$ {x1} ` div ` {x2} $$/수식$$ ○ $$수식$$ {x3} ` div ` {x4} $$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$$ {x1} ` div ` {x2} ` = ` {x1} over {x2} ` = ` {x5} over {x6} $$/수식$$, $$수식$$ {x3} ` div ` {x4} ` = ` {x3} over {x4} ` = ` {x7} over {x8} $$/수식$$\n"\
              "따라서 $$수식$$ {x5} over {x6} ` {a1} ` {x7} over {x8}$$/수식$$이므로 $$수식$$ {x1} ` div ` {x2} ` {a1} ` {x3} ` div ` {x4} $$/수식$$입니다.\n\n"


    break_out = 1
    while break_out:
        ch = 0
        while ch == 0:
            x1 = x1_ = np.random.randint(2, 80)
            x2 = x2_ = np.random.randint(x1, 100)
            while x2_:
                r = max(x1_, x2_) % min(x1_, x2_)
                x1_ = min(x1_, x2_)
                x2_ = r
            if x1_ == 1:
                ch = 1

        ch = 0
        while ch == 0:
            x3 = x3_ = np.random.randint(2, 80)
            x4 = x4_ = np.random.randint(x3, 100)
            while x4_:
                r = max(x3_, x4_) % min(x3_, x4_)
                x3_ = min(x3_, x4_)
                x4_ = r
            if x3_ == 1:
                ch = 1

        if x1 == x3 and x2 == x4 and x3 == x4:
            continue
        else:
            first_thing = x2
            second_thing = x4
            while True:
                rest_piece = max(first_thing, second_thing) % min(first_thing, second_thing)
                first_thing = min(first_thing, second_thing)
                second_thing = rest_piece
                if second_thing == 0 or second_thing == 1:
                    break

        if second_thing == 1:
            break


    x5 = x1 * x4
    x6 = x2 * x4
    x7 = x2 * x3
    x8 = x2 * x4

    if x1/x2 > x3/x4 :
        a1 = "&gt;"
    elif x1/x2 < x3/x4 :
        a1 = "&lt;"
    else :
        a1 = "="

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8, a1=a1)

    return stem, answer, comment













# 6-1-1-11
def fractiondiv611_Stem_005():
    stem = "나눗셈을 분수로 나타내었을 때 $$수식$$1$$/수식$$보다 큰 것은 어느 것인가요?\n① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "① {c1}\n" \
              "② {c2}\n" \
              "③ {c3}\n" \
              "④ {c4}\n" \
              "⑤ {c5}\n\n"


    y_list = []
    z_list = []
    # 서로소

    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(2, 80)
        t2 = t2_ = np.random.randint(t1, 100)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    y_list.append(f"$$수식$$ {t1} ` div ` {t2} $$/수식$$")
    z_list.append(f"$$수식$$ {t1} ` div ` {t2} ` = ` {t1}over{t2} $$/수식$$")

    ch = 0
    while ch == 0:
        t1 = t1_ = np.random.randint(2, 80)
        t2 = t2_ = np.random.randint(t1, 100)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1
        q = t2 // t1
        p = t2 % t1

    y_list.append(f"$$수식$$ {t2} ` div ` {t1} $$/수식$$")
    z_list.append(f"$$수식$$ {t2} ` div ` {t1} ` = ` {q} {p}over{t1} $$/수식$$")

    ch = 0
    while ch == 0:
        t1 = t1_ = np.random.randint(2, 80)
        t2 = t2_ = np.random.randint(t1, 100)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    y_list.append(f"$$수식$$ {t1} ` div ` {t2} $$/수식$$")
    z_list.append(f"$$수식$$ {t1} ` div ` {t2} ` = ` {t1}over{t2} $$/수식$$")

    ch = 0
    while ch == 0:
        t1 = t1_ = np.random.randint(2, 80)
        t2 = t2_ = np.random.randint(t1, 100)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    y_list.append(f"$$수식$$ {t1} ` div ` {t2} $$/수식$$")
    z_list.append(f"$$수식$$ {t1} ` div ` {t2} ` = ` {t1}over{t2} $$/수식$$")

    ch = 0
    while ch == 0:
        t1 = t1_ = np.random.randint(2, 80)
        t2 = t2_ = np.random.randint(t1, 100)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    y_list.append(f"$$수식$$ {t1} ` div ` {t2} $$/수식$$")
    z_list.append(f"$$수식$$ {t1} ` div` {t2} ` = ` {t1}over{t2} $$/수식$$")

    num_list = [0, 1, 2, 3, 4]

    num = num_list.pop(np.random.randint(0, len(num_list)))

    x1 = y_list[num]
    c1 = z_list[num]

    if num == 1:
        a1 = "①"

    num = num_list.pop(np.random.randint(0, len(num_list)))

    x2 = y_list[num]
    c2 = z_list[num]

    if num == 1:
        a1 = "②"

    num = num_list.pop(np.random.randint(0, len(num_list)))

    x3 = y_list[num]
    c3 = z_list[num]

    if num == 1:
        a1 = "③"

    num = num_list.pop(np.random.randint(0, len(num_list)))

    x4 = y_list[num]
    c4 = z_list[num]

    if num == 1:
        a1 = "④"

    num = num_list.pop(np.random.randint(0, len(num_list)))

    x5 = y_list[num]
    c5 = z_list[num]

    if num == 1:
        a1 = "⑤"

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=a1)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)

    return stem, answer, comment















# 6-1-1-12
def fractiondiv611_Stem_006():
    stem = "□ 안에 알맞은 자연수를 구해 보세요.\n$$표$$ $$수식$$ {x1} ` div ` $$/수식$$□$$수식$$ ` = ` {x1} over {x2} $$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ {x1} ` div ` $$/수식$$□$$수식$$ ` = ` {x1} over {lg}□{rg} ` = ` {x1} over {x2} $$/수식$$\n" \
              "□에 알맞은 자연수는 $$수식$$ {x2} $$/수식$$입니다.\n\n"


    ch = 0

    while ch == 0:
        x1 = x1_ = np.random.randint(2, 80)
        x2 = x2_ = np.random.randint(x1, 100)
        while x2_:
            r = max(x1_, x2_) % min(x1_, x2_)
            x1_ = min(x1_, x2_)
            x2_ = r
        if x1_ == 1:
            ch = 1

    squ = "□"

    lg = "{"
    rg = "}"

    stem = stem.format(x1=x1, x2=x2)
    answer = answer.format(a1=x2)
    comment = comment.format(x1=x1, x2=x2, squ=squ, lg=lg, rg=rg)

    return stem, answer, comment












# 6-1-1-13
def fractiondiv611_Stem_007():
    stem = "둘레가 $$수식$$ {x1} `` rm {{cm}} `$$/수식$$인 정{kogak}각형이 있습니다. 이 정{kogak}각형의 한 변의 길이는 몇 $$수식$$rm {{cm}} `$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$$ {a1} {a2} over {a3} rm {{cm}} $$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$정{kogak}각형의 한 변의 길이$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` LEFT ($$/수식$$정{kogak}각형의 둘레$$수식$$RIGHT ) div ` {gak}$$/수식$$\n$$수식$$`" \
              "= ` {x1} ` div ` {gak} ` = ` {x1} over {gak} ` = ` {x2} {x3} over {gak} {s1} ```` LEFT ( rm {{cm}} RIGHT )$$/수식$$\n\n"


    gak = np.random.randint(3, 9)

    kogak_dict = {3:"삼", 4:"사", 5:"오", 6:"육", 7:"칠", 8:"팔"}
    kogak = kogak_dict[gak]

    x1 = np.random.randint(7, 100)

    while x1 % gak == 0 :
        x1 = np.random.randint(7, 100)

    x2 = a1 = x1 // gak
    x3 = a2 = x1 % gak

    a3 = gak
    x4 = x3
    x5 = gak

    for i in range(1, gak+1):
        if x4 % i == 0 and x5 % i == 0 :
            x4 = x4 // i
            x5 = x5 // i
            i = 1

    s1 = ""

    if x5 != gak :
        s1 = f"` = ` {x2} {x4} over {x5}"
        a2 = x4
        a3 = x5


    # while x1 % 6 == 0 :
    #     x1 = np.random.randint(7, 100)
    #
    # x2 = a1 = x1 // 6
    # x3 = a2 = x1 % 6
    #
    # a3 = 6
    # x4 = x3
    # x5 = 6
    #
    # for i in range(1, 7):
    #     if x4 % i == 0 and x5 % i == 0 :
    #         x4 = x4 // i
    #         x5 = x5 // i
    #         i = 1
    #
    # s1 = ""
    #
    # if x5 != 6 :
    #     s1 = f"`=` {x2} {x4}over{x5}"
    #     a2 = x4
    #     a3 = x5


    stem = stem.format(x1=x1, kogak=kogak)
    answer = answer.format(a1=a1, a2=a2, a3=a3)
    comment = comment.format(x1=x1, x2=x2, x3=x3, s1=s1, kogak=kogak, gak=gak)

    return stem, answer, comment














# 6-1-1-14
def fractiondiv611_Stem_008():
    stem = "㉠, ㉡, ㉢에 알맞은 수의 합을 구해 보세요.\n$$표$$ $$수식$${x1} ` div ` {x2} ` = ` {x3} CDOTS$$/수식$$㉠, 나머지 ㉠을 $$수식$${x2}$$/수식$${ro1} 나누면 $$수식$$ {lg}㉡{rg} over {x6} $$/수식$$\n→ $$수식$$ {x1} ` div ` {x2} ` = ` {x3} {lg}㉡{rg} over {x6} ` = ` {lg}㉢{rg} over {x6}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1} ` div ` {x2} ` = ` {x3} CDOTS {x4}$$/수식$$\n" \
              "나머지 $$수식$${x4}$$/수식$${j1} $$수식$${x2}$$/수식$${ro1} 나누면 $$수식$${x5} over {x6}$$/수식$$ → "\
              "$$수식$${x1} ` div ` {x2} ` = ` {x3} {x5} over {x6} ` = ` {x7} over {x6}$$/수식$$\n"\
              "따라서 ㉠$$수식$$` = ` {x4}$$/수식$$, ㉡$$수식$$` = ` {x5}$$/수식$$, ㉢$$수식$$` = ` {x7}$$/수식$$이므로 "\
              "㉠$$수식$$` + `$$/수식$$㉡$$수식$$` + `$$/수식$$㉢$$수식$$` = ` {x4} ` + ` {x5} ` + ` {x7} ` = ` {a1}$$/수식$$입니다.\n\n"


    x1 = np.random.randint(3, 50)
    x2 = x6 = np.random.randint(2, x1)

    while x1 % x2 == 0 :
        x2 = x6 = np.random.randint(1, x1)

    x3 = x1 // x2
    x4 = x5 = x1 % x2

    for i in range(1, x2+1):
        if x5 % (x2+1 - i) == 0 and x6 % (x2+1 - i) == 0 :
            x5 = x5 // (x2+1 - i)
            x6 = x6 // (x2+1 - i)

    x7 = x3 * x6 + x5
    a1 = x4 + x5 + x7

    j1 = proc_jo(x4, 4)

    lg = "{"
    rg = "}"

    if (str(x2))[-1] == "0" or (str(x2))[-1] == "3" or (str(x2))[-1] == "6":
        ro1 = "으로"
    else:
        ro1 = "로"

    stem = stem.format(x1=x1, x2=x2, x3=x3, x6=x6, lg=lg, rg=rg, ro1=ro1)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, j1=j1, a1=a1, ro1=ro1)

    return stem, answer, comment











# 6-1-1-15
def fractiondiv611_Stem_009():
    stem = "한 병에 $$수식$${x1} over {x2} `` rm L `$$/수식$$씩 들어 있는 {s1}{j1} $$수식$${x3}$$/수식$$병 있습니다. 이 {s1}{j2} $$수식$${x4}$$/수식$$일 동안 똑같이 나누어 마시려면 하루에 마셔야 할 {s1}{j3} 몇 $$수식$$rm L `$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${a1} over {a2} rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$전체의 {s1}의 양$$수식$$RIGHT ) ` = ` {x1} over {x2} ` times ` {x3} ` = ` {x5} LEFT ( rm L RIGHT )$$/수식$$\n"\
              "$$수식$$LEFT ($$/수식$$하루에 마셔야 하는 {s1}의 양$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` LEFT ($$/수식$$전체 " \
              "{s1}의 양$$수식$$RIGHT ) ` div ` LEFT ($$/수식$$날 수$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` {x5} ` div ` {x4} ` = ` {x6} over {x7} LEFT ( rm L RIGHT )$$/수식$$\n\n"


    s1 = ['식혜', '우유', '주스', '두유', '미숫가루'][np.random.randint(0, 5)]

    ch = 0
    while ch == 0:
        t1 = t1_ = np.random.randint(1, 9)
        t2 = t2_ = np.random.randint(t1, 10)
        while t2==1:
            t2 = t2_ = np.random.randint(t1, 10)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    x1 = t1
    x2 = t2

    x3 = x2 * np.random.randint(1, 10)

    while x3 > 20 :
        x3 = x2 * np.random.randint(1, 10)

    x4 = np.random.randint(1, 30)

    while x3 % x4 == 0 :
        x4 = np.random.randint(1, 30)

    x5 = int(x1 / x2 * x3)
    x6 = x5
    x7 = x4

    j = x4 + 1

    for i in range(1, j):
        if x6 % (j - i) == 0 and x7 % (j - i) == 0:
            x6 = x6 // (j - i)
            x7 = x7 // (j - i)

    j1 = proc_jo(s1, 0)
    j2 = proc_jo(s1, 4)
    j3 = proc_jo(s1, -1)


    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, s1=s1, j1=j1, j2=j2, j3=j3)
    answer = answer.format(a1=x6, a2=x7)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, s1=s1)

    return stem, answer, comment














# 6-1-1-17
def fractiondiv611_Stem_010():
    stem = "둘레가 $$수식$${x1} ``rm m`$$/수식$$인 정{kogak}각형이 있습니다. 이 정{kogak}각형의 한 변의 길이는 몇 $$수식$$rm m `$$/수식$$인지 대분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${a1} {a2} over {a3} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$정{kogak}각형의 한 변의 길이$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` LEFT ($$/수식$$정{kogak}각형의 " \
              "둘레$$수식$$RIGHT ) ` div ` {gak}$$/수식$$\n$$수식$$` = ` {x1} ` div ` {gak} ` = ` {x1} over {gak} ` = ` {x2} {x3} over {x4} ` LEFT ( rm m RIGHT )$$/수식$$\n\n"


    gak = np.random.randint(3, 9)

    kogak_dict = {3:"삼", 4:"사", 5:"오", 6:"육", 7:"칠", 8:"팔"}
    kogak = kogak_dict[gak]

    x1 = np.random.randint(5, 20)

    while x1 % gak == 0 or x1 < gak:
        x1 = np.random.randint(5, 20)

    x2 = x1 // gak
    t1 = x1 % gak
    t2 = gak

    for i in range(1, gak+1):
        if t1 % (gak + 1 - i) == 0 and t2 % (gak + 1 - i) == 0:
            t1 = t1 // (gak + 1 - i)
            t2 = t2 // (gak + 1 - i)

    x3 = t1
    x4 = t2

    stem = stem.format(x1=x1, kogak=kogak)
    answer = answer.format(a1=x2, a2=x3, a3=x4)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, kogak=kogak, gak=gak)

    return stem, answer, comment













# 6-1-1-19
def fractiondiv611_Stem_011():
    stem = "□ 안에 들어갈 수 있는 자연수는 모두 몇 개인가요?\n$$표$$ $$수식$$□ &lt; {x1} ` div ` {x2} $$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${x1} ` div ` {x2} ` = ` {x1} over {x2} ` = ` {x3} {x4} over {x5}$$/수식$$이므로 " \
              "□$$수식$$ ` &lt; ` {x3} {x4} over {x5}$$/수식$$입니다.\n"\
              "따라서 □ 안에 들어갈 수 있는 자연수는 {s1}로 모두 $$수식$${a1}$$/수식$$개입니다.\n\n"


    x1 = np.random.randint(10, 100)
    x2 = np.random.randint(1, 10)

    while x1 % x2 == 0 :
        x2 = np.random.randint(1, 10)

    x3 = x1 // x2
    j = x2 + 1

    t1 = x1 % x2
    t2 = x2

    for i in range(1, j):
        if t1 % (j - i) == 0 and t2 % (j - i) == 0:
            t1 = t1 // (j - i)
            t2 = t2 // (j - i)

    x4 = t1
    x5 = t2
    s1 = ""
    a1 = x3

    if x3 > 3 :
        for i in range(1, 4):
            s1 = s1 + "$$수식$$" + str(i) + "$$/수식$$, "
        s1 = s1[0:-2]
        s1 = s1 + ", …, $$수식$$" + str(x3) +"$$/수식$$"
    else :
        for i in range(1, x3+1):
            s1 = s1 + "$$수식$$" + str(i) + "$$/수식$$, "
        s1 = s1[0:-2]

    stem = stem.format(x1=x1, x2=x2)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, s1=s1, a1=a1)

    return stem, answer, comment















# 6-1-1-23
def fractiondiv611_Stem_012():
    stem = "나눗셈의 몫이 더 큰 것의 기호를 써 보세요.\n$$표$$ ㉠ $$수식$$ {x1} over {x2} ` div ` {x3} $$/수식$$     ㉡ $$수식$$ {x4} over {x5} ` div ` {x6} $$/수식$$ $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$$ {x1} over {x2} ` div ` {x3} ` = ` {s2} {lg}{x7} ` div ` {x3}{rg} over {x8} ` = ` {x9} over {x8} $$/수식$$\n" \
              "㉡ $$수식$$ {x4} over {x5} ` div ` {x6} ` = ` {s3} {lg}{x10} ` div ` {x6}{rg} over {x11} ` = ` {x12} over {x11} $$/수식$$\n" \
              "$$수식$$ {x9} over {x8} ` = ` {lg}{x9} ` times ` {x13_1}{rg} over {lg}{x8} ` times ` {x13_1}{rg} ` = ` {x14_1} over {x13} $$/수식$$, " \
              "$$수식$$ {x12} over {x11} ` = ` {lg}{x12} ` times ` {x13_2}{rg} over {lg}{x11} ` times ` {x13_2}{rg} ` = ` {x16_1} over {x13} $$/수식$$이므로 " \
              "$$수식$$ {x9} over {x8} {s1} {x12} over {x11}$$/수식$$이므로 몫이 더 큰 것은 {a1}입니다.\n\n"


    while True:
        while True:
            t1 = np.random.randint(1, 7)
            t2 = np.random.randint(t1+1, 10)
            t3 = fractions.Fraction(t1,t2)
            t4 = np.random.randint(1, 7)
            t5 = np.random.randint(t4+1, 16)
            t6 = fractions.Fraction(t4,t5)

            if t3!=t6 and t3.numerator!=t6.numerator and t3.denominator!=t6.denominator:
                break

        x1 = t3.numerator
        x2 = t3.denominator
        x4 = t6.numerator
        x5 = t6.denominator

        while True:
            x3 = np.random.randint(2, 6)
            x6 = np.random.randint(2, 5)

            if x3!=x6:
                break

        if x1 % x3 == 0 :
            x7 = x1
            x8 = x2
            s2 = ""
        else :
            x7 = x1 * x3//gcd(x1, x3)
            x8 = x2 * x3 // gcd(x1, x3)
            s2 = f"{x7} over {x8} ` div ` {x3} ` = `"


        if x4 % x6 == 0 :
            x10 = x4
            x11 = x5
            s3 = ""
        else :
            x10 = x4 * x6 // gcd(x4, x6)
            x11 = x5 * x6 // gcd(x4, x6)
            s3 = f"{x10} over {x11} ` div ` {x6} ` = `"

        x9 = x7 // x3
        x12 = x10 // x6
        x13 = lcm(x8, x11)

        x13_1 = int(x13 / x8)
        x13_2 = int(x13 / x11)

        x14_1 = x9 * x13_1
        x16_1 = x12 * x13_2

        x14 = x9 * x13
        x15 = x8 * x13
        x16 = x12 * x13

        lg = "{"
        rg = "}"

        if x14_1 > x16_1 :
            s1 = "` &gt; `"
            a1 = "㉠"
        else :
            s1 = "` &lt; `"
            a1 = "㉡"
        
        if x13<=150:
            break
   

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6)
    answer = answer.format(a1=a1)
    comment = comment.format(lg=lg, rg=rg, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8, x9=x9, x10=x10, x11=x11, x12=x12, x13=x13, x14_1=x14_1, x16_1=x16_1, s1=s1, s2=s2, s3=s3, a1=a1, x13_1=x13_1, x13_2=x13_2)

    return stem, answer, comment












# 6-1-1-24
def fractiondiv611_Stem_013():
    stem = "㉠과 ㉡에 알맞은 수를 각각 구해 보세요.\n$$표$$ $$수식$$ {x1} over {x2} ` div ` {x3} ` = ` {x1} over {x2} ` times ` 1 over {box1} ` = ` {x4} over {box2} $$/수식$$ $$/표$$\n"
    answer = "(정답)\n㉠ $$수식$${a1}$$/수식$$, ㉡ $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n$$수식$$ {x1} over {x2} ` div ` {x3} ` = ` {x1} over {x2} ` times ` 1 over {x3} ` = ` {x4} over {x5}$$/수식$$이므로 "\
              "㉠$$수식$$` = ` {x3}$$/수식$$, ㉡$$수식$$` = ` {x5}$$/수식$$입니다.\n\n"


    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(2, 21)
        t2 = t2_ = np.random.randint(2, 21)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    x1 = t1
    x2 = t2

    x3 = np.random.randint(2, 21)
    x4 = x1 // gcd(x1, x3)
    x5 = x2 * x3 // gcd(x1, x3)

    box1 = "㉠"
    box2 = "㉡"

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, box1=box1, box2=box2)
    answer = answer.format(a1=x3, a2=x5)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)

    return stem, answer, comment

















# 6-1-1-25
def fractiondiv611_Stem_014():
    stem = "㉠에 알맞은 분수를 구해 보세요.\n$$표$$ $$수식$$ {x1} over {x2} ` div ` {x3}$$/수식$$ → $$수식$$㉠$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1} over {a2}$$/수식$$\n"
    comment = "(해설)\n$$수식$$ {x1} over {x2} ` div ` {x3} ` = ` {x1} over {x2} ` times ` 1 over {x3} ` = ` {x4} over {x5}$$/수식$$\n\n"


    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(1, 50)
        t2 = t2_ = np.random.randint(2, 50)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    x1 = t1
    x2 = t2

    x3 = np.random.randint(2, 20)
    x4 = x1 // gcd(x1, x3)
    x5 = x2 * x3 // gcd(x1, x3)

    stem = stem.format(x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=x4, a2=x5)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)

    return stem, answer, comment











# 6-1-1-26
def fractiondiv611_Stem_015():
    stem = "{s1} $$수식$${x1} over {x2} `` rm kg `$$/수식$$을 $$수식$${x3}$$/수식$$봉지에 똑같이 나누어 담았습니다. 한 봉지에 담은 {s1}{j1} 몇 $$수식$$rm kg `$$/수식$$인지 분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${a1} over {a2} rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$한 봉지에 담은 {s1}의 양$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` LEFT ($$/수식$$전체 {s1}의 양$$수식$$RIGHT ) ` div ` LEFT ($$/수식$$봉지 수$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$= ` {x1} over {x2} ` div ` {x3} ` = ` {x1} over {x2} ` times ` 1 over {x3} ` = ` {x4} over {x5} ` LEFT ( rm kg RIGHT )$$/수식$$\n\n"


    s1 = ['설탕', '소금', '미숫가루', '과자'][np.random.randint(1, 4)]

    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(1, 50)
        t2 = t2_ = np.random.randint(2, 50)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    x1 = t1
    x2 = t2

    x3 = np.random.randint(2, 20)
    x4 = x1 // gcd(x1, x3)
    x5 = x2 * x3 // gcd(x1, x3)
    j1 = proc_jo(s1, -1)

    stem = stem.format(s1=s1, j1=j1, x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=x4, a2=x5)
    comment = comment.format(s1=s1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)

    return stem, answer, comment










# 6-1-1-27
def fractiondiv611_Stem_016():
    stem = "넓이가 $$수식$${x1} over {x2} `` rm {{km}} ^2 `$$/수식$$인 {s1}네 논에 모내기를 하려고 $$수식$${x3}$$/수식$$명이 모였습니다. $$수식$${x3}$$/수식$$명이 똑같이 일을 할 때, 한 사람이 모내기를 해야 하는 논의 넓이는 몇 $$수식$$rm {{km}} ^2$$/수식$$인지 분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${a1} over {a2} rm {{km}} ^2$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$한 사람이 모내기를 해야 하는 논의 넓이$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` LEFT ($$/수식$${s1}네 논의 넓이$$수식$$RIGHT ) ` div ` LEFT ($$/수식$$사람 수$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$` = ` {x1} over {x2} ` div ` {x3} ` = ` {x1} over {x2} ` times ` 1 over {x3} ` = ` {x4} over {x5} ` LEFT ( rm {{km}} ^2RIGHT )$$/수식$$\n\n"


    s1 = ['동수', '현주', '민수', '정수'][np.random.randint(1, 4)]

    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(1, 50)
        t2 = t2_ = np.random.randint(2, 50)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    x1 = t1
    x2 = t2

    x3 = np.random.randint(2, 20)
    x4 = x1 // gcd(x1, x3)
    x5 = x2 * x3 // gcd(x1, x3)
    # j1 = proc_jo(s1, -1)

    stem = stem.format(s1=s1, x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=x4, a2=x5)
    comment = comment.format(s1=s1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)

    return stem, answer, comment












# 6-1-1-28
def fractiondiv611_Stem_017():
    stem = "계산을 잘못한 사람은 누구인가요?\n$$수식$$LEFT [$$/수식$${wh1}$$수식$$RIGHT ] ```` {z1}$$/수식$$\n$$수식$$LEFT [$$/수식$${wh2}$$수식$$RIGHT ] ```` {z2}$$/수식$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT [$$/수식$${wh1}$$수식$$RIGHT ] ```` {z3}$$/수식$$\n" \
              "$$수식$$LEFT [$$/수식$${wh2}$$수식$$RIGHT ] ```` {z4}$$/수식$$\n" \
              "따라서 계산을 잘못한 사람은 {a1}입니다.\n\n"


    wh_list = ['지우', '윤주', '윤성', '지성', '사랑', '소정', '수현', '소현', '동훈']
    wh1 = wh_list[np.random.randint(0, 9)]
    wh2 = wh_list[np.random.randint(0, 9)]

    while wh1 == wh2 :
        wh2 = wh_list[np.random.randint(0, 9)]

    ch = 0
    while ch == 0:
        t1 = t1_ = np.random.randint(2, 50)
        t2 = t2_ = np.random.randint(2, 50)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    x1 = t1
    x2 = t2

    x3 = np.random.randint(2, 20)

    x4 = x1 // gcd(x1, x3)
    x5 = x2 * x3 // gcd(x1, x3)

    y1 = f"{x1} over {x2} ` div ` {x3} ` = ` {x4} over {x5}"
    y3 = f"{x1} over {x2} ` div ` {x3} ` = ` {x1} over {x2} ` times ` 1 over {x3} ` = ` {x4} over {x5}"

    ch = 0
    while ch == 0:
        t1 = t1_ = np.random.randint(2, 50)
        t2 = t2_ = np.random.randint(2, 50)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    x6 = t1 #k
    x7 = t2 #g

    x8 = np.random.randint(2, 20) #h

    x9 = x6 // gcd(x6, x8) #i
    x10 = x7 * x8 // gcd(x6, x8) #j
    x11 = x6 * x8 //gcd(x7, x8)#y
    x12 = x7 * x8 // gcd(x7, x8)#z

    y2 = f"{x6} over {x7} ` div ` {x8} ` = ` {x11} over {x12}"
    y4 = f"{x6} over {x7} ` div ` {x8} ` = ` {x6} over {x7} ` times ` 1 over {x8} ` = ` {x9} over {x10}"

    num = np.random.randint(0, 2)
    if num == 0 :
        a1 = wh2
        z1 = y1
        z3 = y3
        z2 = y2
        z4 = y4
    else :
        a1 = wh1
        z1 = y2
        z3 = y4
        z2 = y1
        z4 = y3


    stem = stem.format(wh1=wh1, wh2=wh2, z1=z1, z2=z2)
    answer = answer.format(a1=a1)
    comment = comment.format(a1=a1, z3=z3, z4=z4, wh1=wh1, wh2=wh2)

    return stem, answer, comment













# 6-1-1-29
def fractiondiv611_Stem_018():
    stem = "나눗셈의 몫이 가장 작은 것의 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${x1} over {x2} ` div ` {x3}$$/수식$$   ㉡ $$수식$${x1} over {x2} ` div ` {x4}$$/수식$$   ㉢ $$수식$${x1} over {x2} ` div ` {x5}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n나누어지는 수가 같을 때 나누는 수가 클수록 몫은 작아집니다.\n"\
              "$$수식$${s1}$$/수식$$이므로 나눗셈의 몫이 가장 작은 것은 나누는 수가 가장 큰 {a1}입니다.\n\n"


    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(2, 26)
        t2 = t2_ = np.random.randint(2, 26)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    x1 = t1
    x2 = t2

    while True:
        y1 = np.random.randint(2, 10)
        y2 = np.random.randint(y1, 18)
        y3 = np.random.randint(y2, 21)
        if y1 != y2 and y1 != y3 and y2!= y3:
            break

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [x3, x4, x5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):       #[a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y3 :
            correct_idx = idx
            break

    s1 = str(y3) + "` &gt; `" + str(y2) + "` &gt; `" + str(y1)

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(s1=s1, a1=answer_kodict[correct_idx])

    return stem, answer, comment















# 6-1-1-32
def fractiondiv611_Stem_019():
    stem = "과학 시간에 실험을 하기 위해 {s1} $$수식$${x1} over {x2} `` rm L ` $$/수식$${j1} 크기가 같은 비커 $$수식$${x3}$$/수식$$개에 똑같이 나누어 담았습니다.\n비커 한 개에 담은 {s1}{j2} 몇 $$수식$$rm L `$$/수식$$인지 기약분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${a1} over {a2} rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$비커 한 개에 담은 {s1}의 양$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` LEFT ($$/수식$$전체 {s1}의 양$$수식$$RIGHT ) ` div ` LEFT ($$/수식$$비커 수$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$` = ` {x1} over {x2} ` div ` {x3} ` = ` {x1} over {x2} ` times ` 1 over {x3} ` = ` {x1} over {x4} {s2} ` LEFT ( rm L )$$/수식$$\n\n"


    s1 = ['식초', '염산', '소금물', '설탕물'][np.random.randint(1, 4)]

    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(2, 26)
        t2 = t2_ = np.random.randint(2, 50)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    x1 = t1
    x2 = t2
    x3 = np.random.randint(2, 21)
    x4 = x2 * x3

    x5 = x1
    x6 = x4

    if x5 > x6 :
        j = x5+1
    else :
        j = x6 + 1

    for i in range(1, j):
        if x5 % (j - i) == 0 and x6 % (j - i) == 0:
            x5 = x5 // (j - i)
            x6 = x6 // (j - i)

    if x5 == x1 :
        s2 = ""
    else :
        s2 = f"` = ` {x5} over {x6}"

    j1 = proc_jo(s1, 4)
    j2 = proc_jo(s1, -1)

    stem = stem.format(s1=s1, x1=x1, x2=x2, x3=x3, j1=j1, j2=j2)
    answer = answer.format(a1=x5, a2=x6)
    comment = comment.format(s1=s1, x1=x1, x2=x2, x3=x3, x4=x4, s2=s2)

    return stem, answer, comment















# 6-1-1-34
def fractiondiv611_Stem_020():
    stem = "㉠$$수식$$` div `$$/수식$$㉡의 몫을 구해 보세요.\n$$표$$ ㉠ $$수식$${x1} over {x2} ` div ` {x3}$$/수식$$    ㉡ $$수식$${x4}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1} over {a2}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$$ {x1} over {x2} ` div ` {x3} ` = ` {x1} over {x2} ` times ` {one} over {x3} ` = ` {x5} over {x6} $$/수식$$ "\
              "→ ㉠$$수식$$` div `$$/수식$$㉡$$수식$$` = ` {x5} over {x6} ` div ` {x4} ` = ` {x5} over {x6} ` times ` {one} over {x4} ` = ` {x7} over {x8}$$/수식$$\n\n"


    # ch = 0
    #
    # while ch == 0:
    #     t1 = t1_ = np.random.randint(2, 26)
    #     t2 = t2_ = np.random.randint(2, 26)
    #     while t2_:
    #         r = max(t1_, t2_) % min(t1_, t2_)
    #         t1_ = min(t1_, t2_)
    #         t2_ = r
    #     if t1_ == 1:
    #         ch = 1
    #
    # x1 = t1
    # x2 = t2
    #
    # x3 = np.random.randint(2, 21)
    # x4 = np.random.randint(2, 21)
    #
    # x5 = x1
    # x6 = x2 * x3
    #
    # if x5 > x6 :
    #     j = x5+1
    # else :
    #     j = x6 + 1
    #
    # for i in range(1, j):
    #     if x5 % (j - i) == 0 and x6 % (j - i) == 0:
    #         x5 = x5 // (j - i)
    #         x6 = x6 // (j - i)
    #
    # x7 = x5
    # x8 = x6 * x4
    #
    # if x7 > x8:
    #     j = x7 + 1
    # else:
    #     j = x8 + 1
    #
    # for i in range(1, j):
    #     if x7 % (j - i) == 0 and x8 % (j - i) == 0:
    #         x7 = x7 // (j - i)
    #         x8 = x8 // (j - i)


    while True:
        ch = 0

        while ch == 0:
            t1 = t1_ = np.random.randint(2, 26)
            t2 = t2_ = np.random.randint(2, 26)

            while t2_:
                r = max(t1_, t2_) % min(t1_, t2_)
                t1_ = min(t1_, t2_)
                t2_ = r

            if t1_ == 1:
                ch = 1

        x1 = t1
        x2 = t2

        x3 = np.random.randint(2, 21)
        x4 = np.random.randint(2, 21)

        x5 = x1
        x6 = x2 * x3

        if x5 > x6 :
            j = x5+1
        else :
            j = x6 + 1

        for i in range(1, j):
            if x5 % (j - i) == 0 and x6 % (j - i) == 0:
                x5 = x5 // (j - i)
                x6 = x6 // (j - i)

        x7 = x5
        x8 = x6 * x4

        if x7 > x8:
            j = x7 + 1
        else:
            j = x8 + 1

        for i in range(1, j):
            if x7 % (j - i) == 0 and x8 % (j - i) == 0:
                x7 = x7 // (j - i)
                x8 = x8 // (j - i)

        if len(str(x6)) < 3:
            if len(str(x8)) < 3:
                break



    one = "1"


    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4)
    answer = answer.format(a1=x7, a2=x8)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8, one=one)

    return stem, answer, comment















# 6-1-1-35
def fractiondiv611_Stem_021():
    stem = "{wh1}{j1} {wh2}{j2} 각자 가지고 있던 {s1} $$수식$$ {x1} over {x2} `` rm kg `$$/수식$${j3} $$수식$$ {x3} over {x4} `` rm kg `$$/수식$$을 섞어서 똑같이 나누어 가졌습니다. {wh1}{j4} 지금 가지고 있는 {s1}{j5} 몇 $$수식$$rm kg `$$/수식$$인지 기약분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${a1} over {a2} rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$두 사람이 가지고 있던 {s1}의 " \
              "무게$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` {x1} over {x2} ` + ` {x3} over {x4} ` = ` {x5} over {x6} ` + ` {x7} over {x6} ` = ` {x8} over {x9} LEFT ( rm kg RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${wh1}{j4} 지금 가지고 있던 {s1}의 무게$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` LEFT ($$/수식$$두 사람이 가지고 있던 {s1}의 무게$$수식$$RIGHT ) ` div ` 2 " \
              "$$/수식$$\n$$수식$$` = ` {x8} over {x9} ` div ` 2 ` = ` {x8} over {x9} ` times ` 1 over 2 ` = ` {x10} over {x11} LEFT ( rm kg RIGHT ) $$/수식$$\n\n"


    wh_list = ['진수', '현지', '현수', '지수', '연지', '곤지', '상수', '선지']

    wh1 = wh_list[np.random.randint(0, 8)]
    wh2 = wh_list[np.random.randint(0, 8)]

    while wh1 == wh2 :
        wh2 = wh_list[np.random.randint(0, 8)]

    s1 = ['찰흙', '점토', '클레이', '샌드'][np.random.randint(0, 4)]


    while True:
        t1 = np.random.randint(2, 6)
        t2 = np.random.randint(t1+1, 11)

        t3 = fractions.Fraction(t1,t2)

        x1 = t3.numerator
        x2 = t3.denominator

        while True:
            t4 = np.random.randint(2, 6)
            t5 = np.random.randint(t1+1, 11)
            t6 = fractions.Fraction(t4,t5)

            if t3!=t6:
                break

        x3 = t6.numerator
        x4 = t6.denominator

        first_thing = x2
        second_thing = x4

        while True:
            rest_peace = max(first_thing, second_thing) % min(first_thing, second_thing)
            first_thing = rest_peace
            second_thing = min(first_thing, second_thing)
            if rest_peace == 0 or rest_peace == 1:
                break

        if rest_peace != 0 and 2*lcm(x2,x4)<=50:
            break

    x6 = lcm(x2, x4)

    x5 = x1 * x6 // x2
    x7 = x3 * x6 // x4

    x8 = x5 + x7
    x9 = x6

    if x8 > x9:
        j = x8 + 1
    else:
        j = x8 + 1

    for i in range(1, j):
        if x8 % (j - i) == 0 and x9 % (j - i) == 0:
            x8 = x8 // (j - i)
            x9 = x9 // (j - i)

    x10 = x8
    x11 = 2 * x9

    if x10 > x11:
        j = x10 + 1
    else:
        j = x11 + 1

    for i in range(1, j):
        if x10 % (j - i) == 0 and x11 % (j - i) == 0:
            x10 = x10 // (j - i)
            x11 = x11 // (j - i)

    j1 = proc_jo(wh1, 2)
    j2 = proc_jo(wh2, -1)

    j3 = proc_jo(s1, 2)
    j4 = proc_jo(wh1, 0)
    j5 = proc_jo(s1, -1)

    stem = stem.format(wh1=wh1, wh2=wh2, s1=s1, j1=j1, j2=j2, j3=j3, j4=j4, j5=j5, x1=x1, x2=x2, x3=x3, x4=x4)
    answer = answer.format(a1=x10, a2=x11)
    comment = comment.format(j4=j4, wh1=wh1, s1=s1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8, x9=x9, x10=x10, x11=x11)

    return stem, answer, comment










# 6-1-1-36
def fractiondiv611_Stem_022():
    stem = "{s1} $$수식$${x1} {x2} over {x3} `` rm L `$$/수식$$중에서 전을 부치는 데 $$수식$$ {x4} over {x5} `` rm L `$$/수식$$를 사용하고 남은 {s1}{j1} 작은 병 $$수식$${x6}$$/수식$$개에 똑같이 나누어 담았습니다. 작은 병 한 개에 담은 {s1}{j2} 몇 $$수식$$rm L `$$/수식$$인지 기약분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${a1} over {a2} rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$사용하고 남은 {s1}의 양$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` {x1} {x2} over {x3} ` - ` {x4} over {x5} ` = ` {x7} over {x3} ` - ` {x4} over {x5} "\
              "` = ` {x8} over {x9} ` - ` {x10} over {x9} ` = ` {x11} over {x12} LEFT ( rm L RIGHT )$$/수식$$\n"\
              "$$수식$$LEFT ($$/수식$$작은 병 한 개에 담은 {s1}의 양$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$` = ` LEFT ($$/수식$$사용하고 남은 {s1}의 양$$수식$$RIGHT ) ` div ` LEFT ($$/수식$$작은 병의 " \
              "수$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` {x11} over {x12} ` times` 1 over {x6} ` = ` {x13} over {x14} LEFT ( rm L RIGHT )$$/수식$$\n\n"


    s1 = ['식용유', '카놀라유', '올리브유'][np.random.randint(1, 3)]

    x1 = np.random.randint(1, 4)
    x2 = np.random.randint(1, 10)

    x3 = np.random.randint(x2+1, 11)
    x4 = np.random.randint(1, 10)

    while x2 == x4 == 9:
        x4 = np.random.randint(1, 10)

    x5 = np.random.randint(x4+1, 11)

    while x3 == x5 :
        x3 = np.random.randint(x2+1, 11)
        x5 = np.random.randint(x4+1, 11)

    x6 = np.random.randint(2, 10)
    x7 = x1 * x3 + x2

    x9 = lcm(x3, x5)
    x8 = x7 * lcm(x3, x5) // x3
    x10 = x4 * lcm(x3, x5) // x5

    x11 = x8 - x10
    x12 = x9

    if x11 > x12 :
        j = x11+1
    else :
        j = x12 + 1

    for i in range(1, j):
        if x11 % (j - i) == 0 and x12 % (j - i) == 0:
            x11 = x11 // (j - i)
            x12 = x12 // (j - i)

    x13 = x11
    x14 = x12 * x6

    if x13 > x14:
        j = x13 + 1
    else:
        j = x14 + 1

    for i in range(1, j):
        if x13 % (j - i) == 0 and x14 % (j - i) == 0:
            x13 = x13 // (j - i)
            x14 = x14 // (j - i)

    j1 = proc_jo(s1, 4)
    j2 = proc_jo(s1, -1)

    stem = stem.format(s1=s1, j1=j1, j2=j2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6)
    answer = answer.format(a1=x13, a2=x14)
    comment = comment.format(s1=s1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8, x9=x9, x10=x10, x11=x11, x12=x12, x13=x13, x14=x14)

    return stem, answer, comment












# 6-1-1-37
def fractiondiv611_Stem_023():
    stem = "길이가 $$수식$$ {x1} over {x2} `` rm {{km}} `$$/수식$$인 도로의 한쪽에 처음부터 끝까지 같은 간격으로 가로수 $$수식$${x3}$$/수식$$그루를 심으려고 합니다. 가로수 사이의 간격을 몇 $$수식$$rm {{km}} `$$/수식$$로 해야 하는지 기약분수로 나타내어 보세요. $$수식$$LEFT ($$/수식$$단, 가로수의 두께는 생각하지 않습니다.$$수식$$RIGHT )$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1} over {a2} rm {{km}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$가로수 사이의 간격 수$$수식$$RIGHT ) ` = ` {x3} ` - ` 1 ` = ` {x4} LEFT ($$/수식$$군데$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$LEFT ($$/수식$$가로수 사이의 " \
              "간격$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` {x1} over {x2} ` div ` {x4} ` = ` {x1} over {x2} ` times ` 1 over {x4} ` = ` {x1} over {x5} {s1} LEFT ( rm {{km}} RIGHT )$$/수식$$\n\n"


    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(1, 21)
        t2 = t2_ = np.random.randint(2, 21)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    x1 = t1
    x2 = t2

    x3 = np.random.randint(10, 21)
    x4 = x3 - 1
    x5 = x2 * x4

    x6 = x1
    x7 = x5

    if x6 > x7 :
        j = x6+1
    else :
        j = x7 + 1

    for i in range(1, j):
        if x6 % (j - i) == 0 and x7 % (j - i) == 0:
            x6 = x6 // (j - i)
            x7 = x7 // (j - i)

    if x6 == x1 :
        s1 = ""
    else :
        s1 = f"`=` {x6} over {x7}"

    a1 = x6
    a2 = x7

    stem = stem.format(x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(s1=s1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7)

    return stem, answer, comment










# 6-1-1-38
def fractiondiv611_Stem_024():
    stem = "□ 안에 들어갈 수 있는 자연수 중 가장 큰 수를 구해 보세요.\n$$표$$ $$수식$$ {x1} over {x2} ` div ` {x3} `&gt;` {lg}□{rg} over {x4} $$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ {x1} over {x2} ` div ` {x3} ` = ` {x1} over {x2} ` times ` 1 over {x3} ` = ` {x1} over {x5} {s1}$$/수식$$이므로 "\
              "$$수식$$ {x6} over {x4} `&gt;` {lg}□{rg} over {x4}$$/수식$$입니다.\n"\
              "따라서 □ 안에 들어갈 수 있는 가장 큰 자연수는 $$수식$${a1}$$/수식$$입니다.\n\n"


    x6 = 1

    while x6 == 1:
        ch = 0
        while ch == 0:
            t1 = t1_ = np.random.randint(2, 31)
            t2 = t2_ = np.random.randint(4, 31)
            while t2_:
                r = max(t1_, t2_) % min(t1_, t2_)
                t1_ = min(t1_, t2_)
                t2_ = r
            if t1_ == 1:
                ch = 1

        x1 = t1
        x2 = t2
        x3 = np.random.randint(1, 31)
        while x1 == x3 :
            x3 = np.random.randint(1, 31)

        x5 = x2 * x3
        x4 = x5 // gcd(x1, x5)
        x6 = x1 // gcd(x1, x5)

    if x4 == x5 :
        s1 = ""
    else :
        s1 = f"` = ` {x6} over {x4}"

    x7 = x6 - 1
    lg = "{"
    rg = "}"

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, lg=lg, rg=rg)
    answer = answer.format(a1=x7)
    comment = comment.format(lg=lg, rg=rg, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, s1=s1,  a1=x7)

    return stem, answer, comment














# 6-1-1-39
def fractiondiv611_Stem_025():
    stem = "어떤 분수를 $$수식$${x1}$$/수식$${josa} 나누어야 할 것을 잘못하여 곱했더니 $$수식$${x2} over {x3}$$/수식$${j1} 되었습니다. 바르게 계산한 값을 기약분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${a1} over {a2}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 분수를 □라고 하여 잘못 계산한 식을 세우면 $$수식$${lg}□{rg} ` times ` {x1} ` = ` {x2} over {x3} $$/수식$$이므로 \n"\
              "$$수식$${lg}□{rg} ` = ` {x2} over {x3} ` div ` {x1} ` = ` {x2} over {x3} ` times ` 1 over {x1} ` = ` {x2} over {x4} {s1}$$/수식$$입니다.\n"\
              "따라서 바르게 계산하면\n"\
              "$$수식$$ {x5} over {x6} ` div ` {x1} ` = ` {x5} over {x6} ` times ` 1 over {x1} ` = ` {x7} over {x8}$$/수식$$입니다.\n\n"



    while True:
        # x1 = np.random.randint(2, 10)

        ch = 0

        while ch == 0:
            t1 = t1_ = np.random.randint(1, 26)
            t2 = t2_ = np.random.randint(2, 26)
            x1 = np.random.randint(2, 10)

            if x1*x1*t2 <= 100:
                while t2_:
                    r = max(t1_, t2_) % min(t1_, t2_)
                    t1_ = min(t1_, t2_)
                    t2_ = r
                if t1_ == 1:
                    ch = 1

        x2 = t1
        x3 = t2

        first_check = x1
        second_check = x3

        while True:
            rest_peace = max(first_check, second_check) % min(first_check, second_check)
            first_check = rest_peace
            second_check = min(first_check, second_check)
            if rest_peace == 0 or rest_peace == 1:
                break

        if rest_peace != 0:
            break


    x4 = x1 * x3
    x5 = x2
    x6 = x4

    if x5 > x6 :
        j = x5+1
    else :
        j = x6 + 1

    for i in range(1, j):
        if x5 % (j - i) == 0 and x6 % (j - i) == 0:
            x5 = x5 // (j - i)
            x6 = x6 // (j - i)

    if x5 != x2 :
        s1 = f"` = ` {x5} over {x6}"
    else :
        s1 = ""

    lg = "{"
    rg = "}"

    x7 = x5
    x8 = x6 * x1

    if x7 > x8 :
        j = x7+1
    else :
        j = x8 + 1

    for i in range(1, j):
        if x7 % (j - i) == 0 and x8 % (j - i) == 0:
            x7 = x7 // (j - i)
            x8 = x8 // (j - i)

    j1 = proc_jo(x2, 0)

    if x1 in [10,3,6]:
        josa = "으로"
    else:
        josa = "로"

    stem = stem.format(x1=x1, x2=x2, x3=x3, lg=lg, rg=rg, j1=j1, josa=josa)
    answer = answer.format(a1=x7, a2 = x8)
    comment = comment.format(lg=lg, rg=rg, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8, s1=s1)

    return stem, answer, comment















# 6-1-1-40
def fractiondiv611_Stem_026():
    stem = "계산을 한 다음 맞게 계산했는지 알아보려고 합니다. ㉠과 ㉡에 알맞은 분수를 구해 보세요. $$수식$$LEFT ($$/수식$$단, ㉡은 대분수로 나타냅니다.$$수식$$RIGHT )$$/수식$$\n$$수식$$ {x1} {x2} over {x3} ` div ` {x4} ` = ` {lg}㉠{rg} $$/수식$$ → 확인: ㉠$$수식$$` times ` {x4} ` = `$$/수식$$㉡\n"
    answer = "(정답)\n㉠$$수식$$``{x6} over {x7}$$/수식$$, ㉡$$수식$$``{x1} {x2} over {x3}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ {x1} {x2} over {x3} ` div ` {x4} ` = ` {x5} over {x3} ` div ` {x4} ` = ` {x5} over {x3} ` times ` 1 over {x4} ` = ` {x6} over {x7} $$/수식$$\n"\
              "→ 확인: $$수식$$ {x6} over {x7} ` times ` {x4} ` = ` {x5} over {x3} ` = ` {x1} {x2} over {x3}$$/수식$$\n"\
              "따라서 ㉠$$수식$$` = ` {x6} over {x7}$$/수식$$, ㉡$$수식$$` = ` {x1} {x2} over {x3}$$/수식$$입니다.\n\n"


    x1 = np.random.randint(1, 6)

    ch = 0

    while ch == 0:
        t1 = t1_ = [2, 3, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20][np.random.randint(0, 13)]
        t2 = t2_ = np.random.randint(2, 21)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    x2 = t1
    x3 = t2

    x4 = np.random.randint(2, 11)
    x5 = x1 * x3 + x2
    x6 = x5 // gcd(x4, x5)
    x7 = x3 * x4 // gcd(x4, x5)

    lg = "{"
    rg = "}"

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, lg=lg, rg=rg)
    answer = answer.format(x6=x6, x7=x7, x1=x1, x2=x2, x3=x3)
    comment = comment.format(lg=lg, rg=rg, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7)

    return stem, answer, comment













# 6-1-1-44
def fractiondiv611_Stem_027():
    stem = "나눗셈의 몫의 크기를 비교하여 ○ 안에 $$수식$$`&gt;`$$/수식$$, $$수식$$`=`$$/수식$$, $$수식$$`&lt;`$$/수식$$를 알맞게 써넣으세요.\n$$수식$$ {x1} over {x2} ` div ` {x3} $$/수식$$ ○ $$수식$$ {x4} {x5} over {x6} ` div ` {x7}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ {x1} over {x2} ` div ` {x3} ` = ` {x1} over {x2} ` times ` 1 over {x3} ` = ` {x1} over {x8}$$/수식$$\n" \
              "$$수식$$ {x4} {x5} over {x6} ` div ` {x7} ` = ` {x1} over {x6} ` times ` 1 over {x7} ` = ` {x1} over {x9}$$/수식$$\n"\
              "{comment_sentence}"


    while True:
        while True:
            x1 = 29

            while x1 > 28 :
                ch = 0
                while ch == 0:
                    t1 = t1_ = np.random.randint(1, 31)
                    t2 = t2_ = np.random.randint(t1, 31)
                    while t2_:
                        r = max(t1_, t2_) % min(t1_, t2_)
                        t1_ = min(t1_, t2_)
                        t2_ = r
                    if t1_ == 1:
                        ch = 1

                x5 = t1
                x6 = t2

                x4 = np.random.randint(1, 4)
                x1 = x4 * x6 + x5

            ch = 0

            while ch == 0:
                t1 = t1_ = x1
                t2 = t2_ = np.random.randint(t1, 30)
                while t2_:
                    r = max(t1_, t2_) % min(t1_, t2_)
                    t1_ = min(t1_, t2_)
                    t2_ = r
                if t1_ == 1:
                    ch = 1

            x2 = t2

            ch = 0

            while ch == 0:
                # t1 = t1_ = x1
                t2 = t2_ = np.random.randint(2, 11)
                while t2_:
                    r = max(t1_, t2_) % min(t1_, t2_)
                    t1_ = min(t1_, t2_)
                    t2_ = r
                if t1_ == 1:
                    ch = 1

            x3 = t2

            ch = 0

            while ch == 0:
                # t1 = x1
                t2 = t2_ = np.random.randint(2, 11)
                while t2_:
                    r = max(t1_, t2_) % min(t1_, t2_)
                    t1_ = min(t1_, t2_)
                    t2_ = r
                if t1_ == 1:
                    ch = 1

            x7 = t2
            x8 = x2 * x3
            x9 = x6 * x7

            if x8 > x9 :
                a1 = "&lt;"
            else :
                a1 = "&gt;"

            if x8 != x9:
                comment_sentence = f"분자가 같은 진분수는 분모가 작은 분수가 더 큽니다.\n" \
                                   f"$$수식$$ {x1} over {x8} ` {a1} ` {x1} over {x9} $$/수식$$이므로 " \
                                   f"$$수식$$ {x1} over {x2} ` div ` {x3} {a1} {x4} {x5} over {x6} ` div ` {x7} $$/수식$$입니다.\n\n"
                break

            elif x8 == x9:
                comment_sentence = "\n"
                a1 = "="
                break

        ef_first = x5
        ef_second = x6

        while True:
            ef_rest = max(ef_first, ef_second) % min(ef_first, ef_second)
            ef_first = ef_rest
            ef_second = min(ef_first, ef_second)
            if ef_rest == 0 or ef_rest == 1:
                break

        ab_first = x1
        ab_second = x2

        while True:
            ab_rest = max(ab_first, ab_second) % min(ab_first, ab_second)
            ab_first = ab_rest
            ab_second = min(ab_first, ab_second)
            if ab_rest == 0 or ab_rest == 1:
                break

        ac_first = x1
        ac_second = x3

        while True:
            ac_rest = max(ac_first, ac_second) % min(ac_first, ac_second)
            ac_first = ac_rest
            ac_second = min(ac_first, ac_second)
            if ac_rest == 0 or ac_rest == 1:
                break

        ag_first = x1
        ag_second = x7

        while True:
            ag_rest = max(ag_first, ag_second) % min(ag_first, ag_second)
            ag_first = ag_rest
            ag_second = min(ag_first, ag_second)
            if ag_rest == 0 or ag_rest == 1:
                break

        if ef_rest == 1 and ab_rest == 1 and ac_rest == 1 and ag_rest:
            break


    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7)
    answer = answer.format(a1=a1)
    comment = comment.format(a1=a1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8, x9=x9, comment_sentence=comment_sentence)

    return stem, answer, comment















# 6-1-1-45
def fractiondiv611_Stem_028():
    stem = "나눗셈의 몫이 큰 것부터 차례대로 기호를 써 보세요.\n$$표$$ ㉠ $$수식$$ {x1} $$/수식$$    ㉡ $$수식$$ {x2} $$/수식$$ \n \n㉢ $$수식$$ {x3} $$/수식$$    ㉣ $$수식$$ {x4} $$/수식$$ $$/표$$\n"
    answer = "(정답)\n{a1}, {a2}, {a3}, {a4}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$$ {z1} $$/수식$$\n" \
              "㉡ $$수식$$ {z2} $$/수식$$\n" \
              "㉢ $$수식$$ {z3} $$/수식$$\n" \
              "㉣ $$수식$$ {z4} $$/수식$$\n" \
              "$$수식$${s1}$$/수식$$이므로 나눗셈의 몫이 큰 것부터 차례대로 기호를 써 보면 {a1}, {a2}, {a3}, {a4} 입니다.\n\n"


    z1 = np.random.randint(1, 10)

    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(1, 9)
        t2 = t2_ = np.random.randint(t1+1, 10)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    z2 = t1
    z3 = t2

    z4 = np.random.randint(2, 20)

    z5 = z1 * z3 + z2
    z6 = z3 * z4
    r1 = z5 / z6

    z7 = z5 // gcd(z5, z6)
    z8 = z6 // gcd(z5, z6)

    z9 = z7 // z8
    z10 = z7 % z8

    w1 = f"{z1} {z2} over {z3} ` div ` {z4}"
    y1 = f"{w1} ` = ` {z5} over {z3} ` times ` 1 over {z4} ` = ` {z5} over {z6}"
    v1 = f"{z5} over {z6}"

    if z5 != z7:
        y1 = y1 + f" ` = ` {z7} over {z8} "
        v1 = f"{z7} over {z8}"

    if z5 > z6:
        y1 = y1 + f" ` = ` {z9} {z10} over {z8}"
        v1 = f"{z9} {z10} over {z8}"

    z1 = np.random.randint(1, 10)

    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(1, 9)
        t2 = t2_ = np.random.randint(t1+1, 10)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    z2 = t1
    z3 = t2
    z4 = np.random.randint(2, 20)

    z5 = z1 * z3 + z2
    z6 = z3 * z4
    r2 = z5 / z6

    z7 = z5 // gcd(z5, z6)
    z8 = z6 // gcd(z5, z6)

    z9 = z7 // z8
    z10 = z7 % z8

    w2 = f"{z1} {z2} over {z3} ` div ` {z4}"
    y2 = f"{w2} ` = ` {z5} over {z3} ` times ` 1 over {z4} ` = ` {z5} over {z6}"
    v2 = f"{z5} over {z6}"

    if z5 != z7:
        y2 = y2 + f" ` = ` {z7} over {z8} "
        v2 = f"{z7} over {z8} "

    if z5 > z6:
        y2 = y2 + f" ` = ` {z9} {z10} over {z8}"
        v2 = f"{z9} {z10} over {z8}"

    z1 = np.random.randint(1, 10)

    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(1, 9)
        t2 = t2_ = np.random.randint(t1+1, 10)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    z2 = t1
    z3 = t2
    z4 = np.random.randint(2, 20)

    z5 = z1 * z3 + z2
    z6 = z3 * z4
    r3 = z5 / z6

    z7 = z5 // gcd(z5, z6)
    z8 = z6 // gcd(z5, z6)

    z9 = z7 // z8
    z10 = z7 % z8

    w3 = f"{z1} {z2} over {z3} ` div ` {z4}"
    y3 = f"{w3} ` = ` {z5} over {z3} ` times ` 1 over {z4} ` = ` {z5} over {z6}"
    v3 = f"{z5} over {z6}"

    if z5 != z7:
        y3 = y3 + f" ` = ` {z7} over {z8} "
        v3 = f"{z7} over {z8}"

    if z5 > z6:
        y3 = y3 + f" ` = ` {z9} {z10} over {z8}"
        v3 = f"{z9} {z10} over {z8}"

    z1 = np.random.randint(1, 10)

    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(1, 9)
        t2 = t2_ = np.random.randint(t1+1, 10)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    z2 = t1
    z3 = t2
    z4 = np.random.randint(2, 20)

    z5 = z1 * z3 + z2
    z6 = z3 * z4
    r4 = z5 / z6

    z7 = z5 // gcd(z5, z6)
    z8 = z6 // gcd(z5, z6)
    z9 = z7 // z8
    z10 = z7 % z8

    w4 = f"{z1} {z2} over {z3} ` div ` {z4}"
    y4 = f"{w4} ` = ` {z5} over {z3} ` times ` 1 over {z4} ` = ` {z5} over {z6}"
    v4 = f"{z5} over {z6}"

    if z5 != z7:
        y4 = y4 + f" ` = ` {z7} over {z8} "
        v4 = f"{z7} over {z8}"

    if z5 > z6:
        y4 = y4 + f" ` = ` {z9} {z10} over {z8}"
        v4 = f"{z9} {z10} over {z8}"

    dic = {0 : r1, 1 : r2, 2 : r3, 3 : r4}
    dlist = sorted(dic.items(), key = operator.itemgetter(1), reverse = True)
    vlist = [v1, v2, v3, v4]

    a1 = answer_kodict[dlist[0][0]]
    a2 = answer_kodict[dlist[1][0]]
    a3 = answer_kodict[dlist[2][0]]
    a4 = answer_kodict[dlist[3][0]]

    s1 = str(vlist[dlist[0][0]]) +"` &gt; `"+str(vlist[dlist[1][0]]) +"` &gt; `"+str(vlist[dlist[2][0]]) +"` &gt; `"+str(vlist[dlist[3][0]])

    stem = stem.format(x1=w1, x2=w2, x3=w3, x4=w4)
    answer = answer.format(a1=a1, a2=a2, a3=a3, a4=a4)
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, z1=y1, z2=y2, z3=y3, z4=y4, s1=s1)

    return stem, answer, comment















# 6-1-1-46
def fractiondiv611_Stem_029():
    stem = "넓이가 $$수식$${x1} {x2} over {x3} `` rm {{cm}} ^2 `$$/수식$$이고 가로가 $$수식$${x4} `` rm {{cm}} `$$/수식$$인 직사각형입니다. 세로는 몇 $$수식$$rm {{cm}} `$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${a1} over {a2} rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$직사각형의 세로$$수식$$RIGHT ) ` = ` LEFT ($$/수식$$넓이$$수식$$RIGHT ) ` div ` LEFT ($$/수식$$가로$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {x1} {x2} over {x3} ` div ` {x4} ` = ` {x5} over {x3} ` times ` 1 over {x4} ` = ` {x6} over {x7} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n\n"


    x1 = np.random.randint(1, 10)

    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(1, 29)
        t2 = t2_ = np.random.randint(t1+1, 30)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            t2_ = r
        if t1_ == 1:
            ch = 1

    x2 = t1
    x3 = t2

    x4 = np.random.randint(2, 20)
    x5 = x1 * x3 + x2
    x6 = x5
    x7 = x3 * x4

    if x6 > x7 :
        j = x6+1
    else :
        j = x7 + 1

    for i in range(1, j):
        if x6 % (j - i) == 0 and x7 % (j - i) == 0:
            x6 = x6 // (j - i)
            x7 = x7 // (j - i)

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4)
    answer = answer.format(a1=x6, a2=x7)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7)

    return stem, answer, comment














# 6-1-1-47
def fractiondiv611_Stem_030():
    stem = "{s1}는 {s2} $$수식$${x1} {x2} over {x3} `` rm L `$$/수식$$를 일주일 동안 똑같이 나누어 마셨습니다. 하루에 몇 $$수식$$rm L$$/수식$$씩 마셔야 하나요?\n"
    answer = "(정답)\n$$수식$${a1} over {a2} rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$하루에 마신 {s2}의 양$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` LEFT ($$/수식$$일주일 동안 마신 {s2}의 양$$수식$$RIGHT ) ` div ` LEFT ($$/수식$$날수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {x1} {x2} over {x3} ` div ` 7 ` = ` {x4} over {x3} ` times ` 1 over 7 ` = ` {x5} over {x6} LEFT ( rm L RIGHT )$$/수식$$\n\n"


    s1 = ['선주', '시진이', '동국이', '종찬이', '설희', '주선이'][np.random.randint(0, 6)]
    s2 = ['식혜', '우유', '주스', '두유', '미숫가루'][np.random.randint(0, 5)]

    x1 = np.random.randint(1, 5)
    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(1, 9)
        t2 = t2_ = np.random.randint(t1+1, 10)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            t2_ = r
        if t1_ == 1:
            ch = 1

    x2 = t1
    x3 = t2
    x4 = x1 * x3 + x2

    if x4 % 7 == 0 :
        x5 = x4 // 7
        x6 = x3
    else :
        x5 = x4
        x6 = 7 * x3

    stem = stem.format(s1=s1, s2=s2, x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=x5, a2=x6)
    comment = comment.format(s2=s2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6)

    return stem, answer, comment














# 6-1-1-48
def fractiondiv611_Stem_031():
    stem = "□ 안에 들어갈 수 있는 가장 작은 자연수를 구해 보세요.\n$$표$$ $$수식$$ {x1} {x2} over {x3} ` div ` {x4} ` &lt; ` {lg}□{rg} $$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ {x1} {x2} over {x3} ` div ` {x4} ` = ` {x5} over {x3} ` times ` 1 over {x4} ` = ` {x5} over {x6} {s1} {s2}$$/수식$$이므로 \n" \
              "$$수식$$ {s3} ` &lt; ` {lg}□{rg}$$/수식$$입니다.\n" \
              "따라서 □ 안에 들어갈 수 있는 가장 작은 자연수는 $$수식$${a1}$$/수식$$입니다.\n\n"


    x1 = np.random.randint(1, 50)

    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(1, 9)
        t2 = t2_ = np.random.randint(t1+1, 10)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    x2 = t1
    x3 = t2

    x4 = np.random.randint(2, 11)
    x5 = x3 * x1 + x2
    x6 = x3 * x4

    x7 = x5
    x8 = x6

    s3 = f"{x5} over {x6}"

    if x7 > x8 :
        j = x7+1
    else :
        j = x8 + 1

    for i in range(1, j):
        if x7 % (j - i) == 0 and x8 % (j - i) == 0:
            x7 = x7 // (j - i)
            x8 = x8 // (j - i)

    if x7 == x5:
        s1 = ""
    else:
        s1 = f"` = ` {x7} over {x8}"
        s3 = f"{x7} over {x8}"

    x9 = x7 // x8
    x10 = x7 % x8

    if x7 > x8 :
        s2 = f"` = ` {x9} {x10} over {x8}"
        s3 = f"{x9} {x10} over {x8}"
        a1 = x9 + 1
    else :
        s2 = ""
        a1 = 1

    lg = "{"
    rg = "}"

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, lg=lg, rg=rg)
    answer = answer.format(a1=a1)
    comment = comment.format(lg=lg, rg=rg, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8, s1=s1, s2=s2, s3=s3, a1=a1)

    return stem, answer, comment














# 6-1-1-50
def fractiondiv611_Stem_032():
    stem = "길이가 $$수식$$ {x1} {x2} over {x3} `` rm {{km}} `$$/수식$$인 길의 한쪽에 처음부터 끝까지 같은 간격으로 {s1}를 $$수식$${x4}$$/수식$${s2} 세우려고 합니다. {s1} 사이의 간격을 몇 $$수식$$rm {{km}} `$$/수식$$로 해야 하는지 기약분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${a1} over {a2} rm {{km}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${s1} 사이의 간격 수$$수식$$RIGHT ) ` = ` {x4} ` - ` 1 ` = ` {x5} LEFT ($$/수식$$군데$$수식$$RIGHT )$$/수식$$\n"\
              "$$수식$$LEFT ($$/수식$${s1} 사이의 간격$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` {x1} {x2} over {x3} ` div ` {x5} ` = ` {x6} over {x3} ` times ` 1 over {x5} ` = ` {x6} over {x7} {s3} LEFT ( rm {{km}} RIGHT )$$/수식$$\n\n"


    num = [0, 1][np.random.randint(0, 2)]

    s1 = ['전봇대', '나무'][num]
    s2 = ['개', '그루'][num]

    x1 = np.random.randint(1, 10)
    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(1, 29)
        t2 = t2_ = np.random.randint(t1+1, 30)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    x2 = t1
    x3 = t2

    x4 = np.random.randint(11, 30)
    x5 = x4 - 1
    x6 = x3 * x1 + x2
    x7 = x3 * x5

    x8 = x6
    x9 = x7

    if x8 > x9 :
        j = x8+1
    else :
        j = x9 + 1

    for i in range(1, j):
        if x8 % (j - i) == 0 and x9 % (j - i) == 0:
            x8 = x8 // (j - i)
            x9 = x9 // (j - i)

    if x8 == x6 :
        s3 = ""
    else :
        s3 = f"`=` {x8} over {x9}"

    a1 = x8
    a2 = x9

    stem = stem.format(s1=s1, s2=s2, x1=x1, x2=x2, x3=x3, x4=x4)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(s1=s1, s3=s3, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8)

    return stem, answer, comment













# 6-1-1-51
def fractiondiv611_Stem_033():
    stem = "㉠에 알맞은 기약분수를 구해 보세요.\n$$표$$$$수식$$ {x1} ` times `$$/수식$$㉠$$수식$$` = ` {x2} {x3} over {x4} ` div ` {x5}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1} over {a2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ {x2} {x3} over {x4} ` div ` {x5} ` = ` {x6} over {x4} ` times ` 1 over {x5} ` = ` {x6} over {x7} {s1}$$/수식$$이므로 "\
              "$$수식$${x1} ` times `$$/수식$$㉠$$수식$$` = ` {s2}$$/수식$$입니다.\n"\
              "→ ㉠ $$수식$$ ` = ` {s2} ` div ` {x1} ` = ` {s2} ` times ` 1 over {x1} ` = ` {x10} over {x11}$$/수식$$\n\n"


    x1 = np.random.randint(2, 10)
    x2 = np.random.randint(1, 15)
    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(1, 10)
        t2 = t2_ = np.random.randint(t1+1, 15)
        while t2_:
            r = max(t1_, t2_) % min(t1_, t2_)
            t1_ = min(t1_, t2_)
            t2_ = r
        if t1_ == 1:
            ch = 1

    x3 = t1
    x4 = t2

    x5 = np.random.randint(2, 20)
    x6 = x4 * x2 + x3
    x7 = x4 * x5

    x8 = x6
    x9 = x7

    if x8 > x9 :
        j = x8+1
    else :
        j = x9 + 1

    for i in range(1, j):
        if x8 % (j - i) == 0 and x9 % (j - i) == 0:
            x8 = x8 // (j - i)
            x9 = x9 // (j - i)

    if x8 == x6 :
        s1 = ""
    else :
        s1 = f"` = ` {x8} over {x9}"

    s2 = f"{x8} over {x9}"
    x10 = x8
    x11 = x9 * x1

    if x10 > x11 :
        j = x10+1
    else :
        j = x11 + 1

    for i in range(1, j):
        if x10 % (j - i) == 0 and x11 % (j - i) == 0:
            x10 = x10 // (j - i)
            x11 = x11 // (j - i)

    a1 = x10
    a2 = x11

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(s1=s1, s2=s2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8, x9=x9, x10=x10, x11=x11)

    return stem, answer, comment















# 6-1-1-53
def fractiondiv611_Stem_034():
    stem = "끈 $$수식$${x1} {x2} over {x3} `` rm m `$$/수식$$를 모두 사용하여 가장 크고 크기가 같은 정사각형 모양을 $$수식$${x4}$$/수식$$개 만들었습니다. 만든 정사각형 $$수식$$1$$/수식$$개의 넓이는 몇 $$수식$$rm m^2$$/수식$$인지 기약분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${a1} over {a2} rm m ^2$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$정사각형 모양 $$수식$$1$$/수식$$개를 만드는데 사용한 끈의 " \
              "길이$$수식$$RIGHT )$$/수식$$\n$$수식$$= ` {x1} {x2} over {x3} ` div ` {x4} ` = ` {x5} over {x3} ` times ` 1 over {x4} ` = ` {x6} over {x7} rm LEFT ( m RIGHT )$$/수식$$\n"\
              "$$수식$$LEFT ($$/수식$$정사각형의 한 변의 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {x6} over {x7} ` div ` 4 ` = ` {x6} over {x7} ` times ` 1 over 4 ` = ` {x6} over {x8} {s1} rm LEFT ( m RIGHT )$$/수식$$\n"\
              "→ $$수식$$LEFT ($$/수식$$정사각형의 넓이$$수식$$RIGHT )$$/수식$$\n$$수식$$= ` {x9} over {x10} ` times ` {x9} over {x10} ` = ` {x11} over {x12} LEFT ( rm m^2 RIGHT )$$/수식$$\n\n"


    
    ch = 0

    while ch == 0:
        t1 = t1_ = np.random.randint(1, 6)
        t2 = t2_ = np.random.randint(t1+1, 10)
        x1 = np.random.randint(1, 6)

        if fractions.Fraction(x1*t2+t1,t2*12).denominator <= 10:
            while t2_:
                r = max(t1_, t2_) % min(t1_, t2_)
                t1_ = min(t1_, t2_)
                t2_ = r
            if t1_ == 1:
                ch = 1

    x2 = t1
    x3 = t2

    x4 = 3
    x5 = x3 * x1 + x2
    x6 = x5
    x7 = x3 * x4

    if x6 > x7 :
        j = x6+1
    else :
        j = x7 + 1

    for i in range(1, j):
        if x6 % (j - i) == 0 and x7 % (j - i) == 0:
            x6 = x6 // (j - i)
            x7 = x7 // (j - i)

    x8 = 4 * x7

    if x6 > x8 :
        j = x6+1
    else :
        j = x8 + 1

    tmp = x6
    tmp2 = x8

    for i in range(1, j):
        if tmp % (j - i) == 0 and tmp2 % (j - i) == 0:
            tmp = tmp // (j - i)
            tmp2 = tmp2 // (j - i)

    if tmp == x6 :
        s1 = ""
    else :
        s1 = f"`=` {tmp} over {tmp2}"

    x9 = x6
    x10 = x8

    if x9 > x10 :
        j = x9+1
    else :
        j = x10 + 1

    for i in range(1, j):
        if x9 % (j - i) == 0 and x10 % (j - i) == 0:
            x9 = x9 // (j - i)
            x10 = x10 // (j - i)

    x11 = x9 * x9
    x12 = x10 * x10

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4)
    answer = answer.format(a1 =  x11, a2 = x12)
    comment = comment.format(s1 = s1, x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6, x7 = x7, x8 = x8, x9 = x9, x10 = x10, x11 = x11, x12 = x12)

    return stem, answer, comment













# 6-1-1-55
def fractiondiv611_Stem_035():
    stem = "거리가 $$수식$${x1} {x2} over {x3} `` rm {{km}} `$$/수식$$인 산책로를 토끼와 거북이가 각각 일정한 빠르기로 달렸더니 토끼는 $$수식$${x4}$$/수식$$분이 걸렸고 거북이는 $$수식$${x5}$$/수식$$시간이 걸렸습니다. $$수식$${x4}$$/수식$$분 동안 토끼는 거북이보다 몇 $$수식$$rm {{km}} `$$/수식$$를 더 많이 간 것인지 대분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${a1} {a2} over {a3} rm {{km}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${x5}$$/수식$$시간은 $$수식$${x6}$$/수식$$분이고 $$수식$${x6}$$/수식$$분은 $$수식$${x4}$$/수식$$분의 $$수식$${x7}$$/수식$$배이므로\n" \
              "$$수식$$LEFT ($$/수식$$거북이가 $$수식$${x4}$$/수식$$분 동안 간 " \
              "거리$$수식$$RIGHT )$$/수식$$\n$$수식$$= ` {x1} {x2} over {x3} ` div ` {x7} ` = ` {x8} over {x3} ` times ` 1 over {x7} ` = ` {x8} over {x9} {s1} LEFT ( rm {{km}} RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$토끼가 $$수식$${x4}$$/수식$$분 동안 간 거리 $$수식$$ RIGHT )-LEFT ($$/수식$$거북이가 $$수식$${x4}$$/수식$$분 동안 간 거리$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {x1} {x2} over {x3} ` - ` {x10} over {x11} ` = ` {x12} over {x3} ` - ` {x10} over {x11} ` = ` {x13} over {x14} ` - ` {x15} over {x14}$$/수식$$\n$$수식$$` = ` {x16} over {x14} ` = ` {x17} {x18} over {x19} LEFT ( rm {{km}} RIGHT )$$/수식$$\n\n"


    k1 = 0
    k2 = 1

    # while k1 <= k2 :
    #     x4 = [10, 20, 30, 60][np.random.randint(0, 4)]
    #     x5 = np.random.randint(1, 5)
    #     x6 = x5 * 60
    #     x7 = x6 // x4
    #
    #     x1 = np.random.randint(1, 6)
    #     ch = 0
    #     while ch == 0:
    #         t1 = t1_ = np.random.randint(1, 20)
    #         t2 = t2_ = np.random.randint(t1+1, 21)
    #         while t2_:
    #             r = max(t1_, t2_) % min(t1_, t2_)
    #             t1_ = min(t1_, t2_)
    #             t2_ = r
    #         if t1_ == 1:
    #             ch = 1
    #
    #     x2 = t1
    #     x3 = t2
    #     x8 = x1 * x3 + x2
    #     x9 = x3 * x7
    #     k1 = (x1 * x3 + x2) // x3
    #     k2 = x8 // x9
    #
    # x10 = x8
    # x11 = x9
    #
    # if x10 > x11 :
    #     j = x10+1
    # else :
    #     j = x11 + 1
    #
    # for i in range(1, j):
    #     if x10 % (j - i) == 0 and x11 % (j - i) == 0:
    #         x10 = x10 // (j - i)
    #         x11 = x11 // (j - i)
    #
    # if x10 == x8 :
    #     s1 = ""
    # else :
    #     s1 = f"` = `{x10} over {x11}"
    #
    # x12 = x3*x1 + x2
    # x13 = x12 * x11
    # x14 = x3 * x11
    #
    # x15 = x10 * x3
    # x16 = x13 - x15
    # x17 = x16 // x14
    #
    # x19 = x14 // gcd(x16, x14)
    # x18 = x16 // gcd(x16, x14) - x17 * x19


    while True:

        k1 = 0
        k2 = 1

        while k1 <= k2:
            x4 = [10, 20, 30, 60][np.random.randint(0, 4)]
            x5 = np.random.randint(1, 5)
            x6 = x5 * 60
            x7 = x6 // x4

            x1 = np.random.randint(1, 6)
            ch = 0
            while ch == 0:
                t1 = t1_ = np.random.randint(1, 20)
                t2 = t2_ = np.random.randint(t1+1, 21)
                while t2_:
                    r = max(t1_, t2_) % min(t1_, t2_)
                    t1_ = min(t1_, t2_)
                    t2_ = r
                if t1_ == 1:
                    ch = 1

            x2 = t1
            x3 = t2
            x8 = x1 * x3 + x2
            x9 = x3 * x7
            k1 = (x1 * x3 + x2) // x3
            k2 = x8 // x9

        x10 = x8
        x11 = x9

        if x10 > x11 :
            j = x10+1
        else :
            j = x11 + 1

        for i in range(1, j):
            if x10 % (j - i) == 0 and x11 % (j - i) == 0:
                x10 = x10 // (j - i)
                x11 = x11 // (j - i)

        if x10 == x8:
            s1 = ""
        else:
            s1 = f"` = `{x10} over {x11}"

        x12 = x3*x1 + x2
        x13 = x12 * x11
        x14 = x3 * x11

        if x14 > 100:
            continue

        x15 = x10 * x3
        x16 = x13 - x15
        x17 = x16 // x14

        x19 = x14 // gcd(x16, x14)
        x18 = x16 // gcd(x16, x14) - x17 * x19

        if 0 < x17 and x17 < 10:
            break





    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=x17, a2=x18, a3=x19)
    comment = comment.format(s1=s1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8, x9=x9, x10=x10, x11=x11, x12=x12, x13=x13, x14=x14, x15=x15, x16=x16, x17=x17, x18=x18, x19=x19)

    return stem, answer, comment














# 6-1-1-56
def fractiondiv611_Stem_036():
    stem = "철사를 겹치지 않게 모두 사용하여 한 변의 길이가 $$수식$${x1} {x2} over {x3} `` rm {{cm}} `$$/수식$$인 {s1} 모양을 만들었습니다. 이 철사를 펴서 똑같이 두 도막으로 나눈 후 그 중 한 도막으로 {s2} 모양을 만들었다면 만든 {s2}의 한 변의 길이는 몇 인지 기약분수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${a1} {a2} over {a3} rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$전체 철사의 길이$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` {x1} {x2} over {x3} ` times ` {x11} ` = ` {x4} over {x3} ` times ` {x11} ` = ` {x5} over {x6} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$철사 한 도막의 길이$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` {x5} over {x6} ` div ` 2 ` = ` {x5} over {x6} ` times ` 1 over 2 ` = ` {x7} over {x8} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${s2}의 한 변의 길이$$수식$$RIGHT )$$/수식$$\n$$수식$$` = ` {x7} over {x8} ` div ` {x12} ` = ` {x7} over {x8} ` times ` 1 over {x12} ` = ` {x7} over {x18} {s3} ` = `  {x15} {x16} over {x14} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n\n"


    # x1 = np.random.randint(1, 11)
    # ch = 0
    #
    # while ch == 0:
    #     t1 = t1_ = np.random.randint(1, 20)
    #     t2 = t2_ = np.random.randint(t1+1, 21)
    #     while t2_:
    #         r = max(t1_, t2_) % min(t1_, t2_)
    #         t1_ = min(t1_, t2_)
    #         t2_ = r
    #     if t1_ == 1:
    #         ch = 1
    #
    # x2 = t1
    # x3 = t2
    #
    # s_list = ['정팔각형', '정육각형', '정오각형', '정사각형', '정삼각형']
    # s1 = s_list[np.random.randint(0, 5)]
    #
    # if s1 == '정팔각형' :
    #     x11 = 8
    # elif s1 == '정육각형' :
    #     x11 = 6
    # elif s1 == '정오각형' :
    #     x11 = 5
    # elif s1 == '정사각형' :
    #     x11 = 4
    # else :
    #     x11 = 3
    #
    # s2 = s_list[np.random.randint(0, 5)]
    #
    # while s1 == s2 :
    #     s2 = s_list[np.random.randint(0, 5)]
    #
    # if s2 == '정팔각형' :
    #     x12 = 8
    # elif s2 == '정육각형' :
    #     x12 = 6
    # elif s2 == '정오각형' :
    #     x12 = 5
    # elif s2 == '정사각형' :
    #     x12 = 4
    # else :
    #     x12 = 3
    #
    # x4 = x3 * x1 + x2
    # x5 = x4 * x11
    # x6 = x3
    #
    # if x5 > x6 :
    #     j = x5+1
    # else :
    #     j = x6 + 1
    #
    # for i in range(1, j):
    #     if x5 % (j - i) == 0 and x6 % (j - i) == 0:
    #         x5 = x5 // (j - i)
    #         x6 = x6 // (j - i)
    #
    # x7 = x5
    # x8 = x6 * 2
    #
    # if x7 > x8 :
    #     j = x7+1
    # else :
    #     j = x8 + 1
    #
    # for i in range(1, j):
    #     if x7 % (j - i) == 0 and x8 % (j - i) == 0:
    #         x7 = x7 // (j - i)
    #         x8 = x8 // (j - i)
    #
    # x18 = x8 * x12
    # x13 = x7
    # x14 = x18
    #
    # if x13 > x14 :
    #     j = x13+1
    # else :
    #     j = x14 + 1
    #
    # for i in range(1, j):
    #     if x13 % (j - i) == 0 and x14 % (j - i) == 0:
    #         x13 = x13 // (j - i)
    #         x14 = x14 // (j - i)
    #
    # if x13 == x7 :
    #     s3 = ""
    # else :
    #     s3 = f"`=` {x13} over {x14}"
    #
    # x15 = x13 // x14
    # x16 = x13 % x14
    # h 8 i 9 j 10 k 11 l 12 m 13 n 14 o 15 p 16 q 17 r 18


    while True:
        x1 = np.random.randint(1, 11)
        ch = 0

        while ch == 0:
            t1 = t1_ = np.random.randint(1, 20)
            t2 = t2_ = np.random.randint(t1+1, 21)

            while t2_:
                r = max(t1_, t2_) % min(t1_, t2_)
                t1_ = min(t1_, t2_)
                t2_ = r

            if t1_ == 1:
                ch = 1

        x2 = t1
        x3 = t2

        s_list = ['정팔각형', '정육각형', '정오각형', '정사각형', '정삼각형']
        s1 = s_list[np.random.randint(0, 5)]

        if s1 == '정팔각형' :
            x11 = 8
        elif s1 == '정육각형' :
            x11 = 6
        elif s1 == '정오각형' :
            x11 = 5
        elif s1 == '정사각형' :
            x11 = 4
        else :
            x11 = 3

        s2 = s_list[np.random.randint(0, 5)]

        while s1 == s2 :
            s2 = s_list[np.random.randint(0, 5)]

        if s2 == '정팔각형' :
            x12 = 8
        elif s2 == '정육각형' :
            x12 = 6
        elif s2 == '정오각형' :
            x12 = 5
        elif s2 == '정사각형' :
            x12 = 4
        else :
            x12 = 3

        x4 = x3 * x1 + x2
        x5 = x4 * x11
        x6 = x3

        if x5 > x6 :
            j = x5+1
        else :
            j = x6 + 1

        for i in range(1, j):
            if x5 % (j - i) == 0 and x6 % (j - i) == 0:
                x5 = x5 // (j - i)
                x6 = x6 // (j - i)

        x7 = x5
        x8 = x6 * 2

        if x7 > x8 :
            j = x7+1
        else :
            j = x8 + 1

        for i in range(1, j):
            if x7 % (j - i) == 0 and x8 % (j - i) == 0:
                x7 = x7 // (j - i)
                x8 = x8 // (j - i)

        x18 = x8 * x12
        x13 = x7
        x14 = x18

        if x13 > x14 :
            j = x13+1
        else :
            j = x14 + 1

        for i in range(1, j):
            if x13 % (j - i) == 0 and x14 % (j - i) == 0:
                x13 = x13 // (j - i)
                x14 = x14 // (j - i)

        if x13 == x7 :
            s3 = ""
        else :
            s3 = f"`=` {x13} over {x14}"

        x15 = x13 // x14
        x16 = x13 % x14

        if 0 < x15 and x15 < 10:
            if x16 > 0:
                if len(str(x14)) < 3:
                    break



    stem = stem.format(s1=s1, s2=s2, x1=x1, x2=x2, x3=x3, x4=x4)
    answer = answer.format(a1=x15, a2=x16, a3=x14)
    comment = comment.format(s2=s2, s3=s3, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8, x11=x11, x12=x12, x13=x13, x14=x14, x15=x15, x16=x16, x18=x18)

    return stem, answer, comment









