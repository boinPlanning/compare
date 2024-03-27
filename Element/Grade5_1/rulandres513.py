import numpy as np
import random




answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤"
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
    elif bool_jo(num):
        # 을를
        return "을"
    return "를"







# 5-1-3-11
def rulandres513_Stem_001():
    stem = "■와 ● 사이의 대응 관계를 나타낸 표입니다. ㉡ $$수식$$DIV$$/수식$$ ㉠의 값을 구해 보세요.\n$$수식$${boxone}$$/수식$$$$수식$${boxtwo}$$/수식$$$$수식$${boxthree}$$/수식$$$$수식$${boxfour}$$/수식$$$$수식$${boxfive}$$/수식$$$$수식$${boxsix}$$/수식$$\n$$수식$${boxseven}$$/수식$$$$수식$${boxeight}$$/수식$$$$수식$${boxnine}$$/수식$$$$수식$${boxten}$$/수식$$$$수식$${boxeleven}$$/수식$$$$수식$${boxtwelve}$$/수식$$\n"
    answer = "(정답)\n$$수식$${sss}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$1 TIMES {saa} = {saa}$$/수식$$, $$수식$${a2} TIMES {saa} = {c2}$$/수식$$, $$수식$${a3} TIMES {saa} = {c3}$$/수식$$\n" \
              "→ ●는 ■의 $$수식$${saa}$$/수식$$배입니다.\n" \
              "$$수식$${a1} TIMES {saa} = {c1}$$/수식$$, ㉠$$수식$$= {c1}$$/수식$$, $$수식$${a4} TIMES {saa} = {c4}$$/수식$$, ㉡$$수식$$= {c4}$$/수식$$\n" \
              "따라서 ㉡$$수식$$DIV$$/수식$$㉠$$수식$$= {c4} DIV {c1} = {sss}$$/수식$$입니다.\n\n"


    while True:
        saa = np.random.randint(3, 8)
        a_list = random.sample(range(1, 10), 4)
        a_list.sort()

        a1 = a_list[0]
        a2 = a_list[1]
        a3 = a_list[2]
        a4 = a_list[3]

        if (a4 % a1) == 0:
            break

    b2 = saa * a2
    b3 = saa * a3

    c1 = saa * a1
    c2 = saa * a2

    c3 = saa * a3
    c4 = saa * a4

    sss = int(c4/c1)


    boxone = "box{%s}" % "■"
    boxtwo = "box{%s}" % "1"

    boxthree = "box{%s}" % a1
    boxfour = "box{%s}" % a2
    boxfive = "box{%s}" % a3
    boxsix = "box{%s}" % a4

    boxseven = "box{%s}" % "●"
    boxeight = "box{%s}" % saa
    boxnine = "box{%s}" % "㉠"

    if b2 > 9:
        boxten = "box{%d}" % b2
    else:
        boxten = "box{%d}" % b2

    if b3 > 9:
        boxeleven = "box{%d}" % b3
    else:
        boxeleven = "box{%d}" % b3

    boxtwelve = "box{%s}" % "㉡"


    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour, boxfive=boxfive, boxsix=boxsix, boxseven=boxseven, boxeight=boxeight, boxnine=boxnine, boxten=boxten, boxeleven=boxeleven, boxtwelve=boxtwelve)
    answer = answer.format(sss=sss)
    comment = comment.format(saa=saa, a1=a1, a2=a2, a3=a3, a4=a4, c1=c1, c2=c2, c3=c3, c4=c4, sss=sss)

    return stem, answer, comment










# 5-1-3-12
def rulandres513_Stem_002():
    stem = "{saa}각형의 수와 변의 수 사이의 대응 관계를 $$수식$$2$$/수식$$가지로 써 보세요.\n$$수식$${boxone}$$수식$$$$/수식$${boxtwo}$$수식$$$$/수식$${boxthree}$$수식$$$$/수식$${boxfour}$$수식$$$$/수식$${boxfive}$$/수식$$\n$$수식$${boxsix}$$수식$$$$/수식$${boxseven}$$수식$$$$/수식$${boxeight}$$수식$$$$/수식$${boxnine}$$수식$$$$/수식$${boxten}$$/수식$$\n$$수식$$LEFT [$$/수식$$방법 $$수식$$1 RIGHT ]$$/수식$$ $$수식$${boxeleven}$$/수식$$의 수를 $$수식$${boxtwelve}$$/수식$$배 하면 변의 수와 같습니다.\n$$수식$$LEFT [$$/수식$$방법 $$수식$$2 RIGHT ]$$/수식$$ 변의 수를 $$수식$${boxthirteen}$$/수식$${ro} 나누면 $$수식$${boxfourteen}$$/수식$$의 수와 같습니다.\n"
    answer = "(정답)\n㉠ {saa}각형, ㉡ $$수식$${a1}$$/수식$$, ㉢ $$수식$${a1}$$/수식$$, ㉣ {saa}각형\n"
    comment = "(해설)\n" \
              "{saa}각형의 수가 $$수식$$1$$/수식$$개, $$수식$$2$$/수식$$개, $$수식$$3$$/수식$$개$$수식$$CDOTS CDOTS$$/수식$$일 때 변의 수는 " \
              "$$수식$${a1}$$/수식$$개, $$수식$${a2}$$/수식$$개, $$수식$${a3}$$/수식$$개$$수식$$CDOTS CDOTS$$/수식$$이므로 " \
              "{saa}각형의 수를 $$수식$${a1}$$/수식$$배 하면 변의 수와 같습니다.\n" \
              "또는 {saa}각형의 변의 수를 $$수식$${a1}$$/수식$${ro} 나누면 {saa}각형의 수와 같습니다.\n\n"


    saa = ["삼", "사", "오","육","칠","팔"][np.random.randint(0, 6)]

    if saa == "삼":
        a1 = 3
    elif saa == "사":
        a1 = 4
    elif saa == "오":
        a1 = 5
    elif saa == "육":
        a1 = 6
    elif saa == "칠":
        a1 = 7
    elif saa == "팔":
        a1 = 8
        
    a2 = 2 * a1
    a3 = 3 * a1

    boxone = "[%s각형의 수(개)]" % saa
    boxtwo = "box{%d}" % 1

    if a2 > 9:
        boxthree = "box{%d}" % 2
    else :
        boxthree = "box{%d}" % 2

    if a3 > 9:
        boxfour = "box{%d}" % 3
    else :
        boxfour = "box{%d}" % 3

    boxfive = "CDOTS CDOTS"

    boxsix = "[변의 수(개)]"

    boxseven = "box{%d}" % a1
    boxeight = "box{%d}" % a2

    boxnine = "box{%d}" % a3
    boxten = "CDOTS CDOTS"

    boxeleven = "box{%s````````````````````}"%"㉠"
    boxtwelve = "box{%s````````````````````}"%"㉡"
    boxthirteen = "box{%s````````````````````}"%"㉢"
    boxfourteen = "box{%s````````````````````}"%"㉣"

    if a1 == 3 or a1 == 6:
        ro = "으로"
    else:
        ro = "로"

    stem = stem.format(saa=saa, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour, boxfive=boxfive, boxsix=boxsix, boxseven=boxseven, boxeight=boxeight, boxnine=boxnine, boxten=boxten, boxeleven=boxeleven, boxtwelve=boxtwelve, boxthirteen=boxthirteen, boxfourteen=boxfourteen, ro=ro)
    answer = answer.format(saa=saa, a1=a1)
    comment = comment.format(saa=saa, a1=a1, a2=a2, a3=a3, ro=ro)

    return stem, answer, comment








# 5-1-3-18
def rulandres513_Stem_003():
    stem = "상자에 {p}를 $$수식$${saa}$$/수식$$개씩 담았습니다. 상자의 수와 {p}의 수 사이의 대응 관계를 알아보고 ㉠ $$수식$$+$$/수식$$ ㉡의 값을 구해보세요.\n$$수식$${boxone}$$/수식$$ $$수식$${boxtwo}$$/수식$$ $$수식$${boxthree}$$/수식$$ $$수식$${boxfour}$$/수식$$ $$수식$${boxfive}$$/수식$$ $$수식$${boxsix}$$/수식$$\n$$수식$${boxseven}$$/수식$$ $$수식$${boxeight}$$/수식$$ $$수식$${boxnine}$$/수식$$ $$수식$${boxten}$$/수식$$ $$수식$${boxeleven}$$/수식$$ $$수식$${boxtwelve}$$/수식$$\n"
    answer = "(정답)\n$$수식$${s3}$$/수식$$\n"
    comment = "(해설)\n" \
              "상자가 $$수식$$1$$/수식$$개씩 늘어날수록 {p}는 $$수식$${saa}$$/수식$$개씩 늘어납니다.\n" \
              "$$수식$$LEFT ($$/수식$${p}의 수 $$수식$$RIGHT ) = LEFT ($$/수식$$상자의 수$$수식$$RIGHT ) TIMES {saa}$$/수식$$이므로\n" \
              "㉠$$수식$$= 3 TIMES {saa} = {s1} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$, " \
              "㉡$$수식$$= 4 TIMES {saa} = {s2} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$입니다.\n" \
              "따라서 ㉠$$수식$$+$$/수식$$㉡$$수식$$= {s1} + {s2} = {s3}$$/수식$$입니다.\n\n"


    p = ["복숭아", "사과", "포도", "망고", "자두", "딸기", "감자", "고구마", "토마토", "오이"][np.random.randint(0, 10)]

    saa = [3, 4, 6, 7, 8][np.random.randint(0, 5)]
    s1 = 3 * saa
    s2 = 4 * saa
    s3 = s1 + s2

    boxone = "[%s]" % "상자의 수(개)"
    boxtwo = "box{%d}" % 1

    if (2*saa) > 9:
        boxthree = "box{%d}" % 2
    else :
        boxthree = "box{%d}" % 2

    boxfour = "box{%d}" % 3
    boxfive = "box{%d}" % 4
    boxsix = "CDOTS CDOTS"

    if len(p) == 2:
        boxseven = "[%s%s]" % (p,"의 수(개)")
    else :
        boxseven = "[%s%s]" % (p, "의 수(개)")

    boxeight = "box{%d}" % saa
    boxnine = "box{%d}" % (2*saa)

    boxten = "box{%s}" % "㉠"
    boxeleven = "box{%s}" % "㉡"
    boxtwelve = "CDOTS CDOTS"

    stem = stem.format(p=p, saa=saa, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour, boxfive=boxfive, boxsix=boxsix, boxseven=boxseven, boxeight=boxeight, boxnine=boxnine, boxten=boxten, boxeleven=boxeleven, boxtwelve=boxtwelve)
    answer = answer.format(s3=s3)
    comment = comment.format(p=p, saa=saa, s1=s1, s2=s2, s3=s3)

    return stem, answer, comment










# 5-1-3-19
def rulandres513_Stem_004():
    stem = "바구니에 {p}를 $$수식$${saa}$$/수식$$개씩 담았습니다. 바구니의 수와 {p}의 수 사이의 대응 관계를 식으로 써 보세요.\n$$수식$$LEFT ($$/수식$$바구니의 수$$수식$$RIGHT ) TIMES $$/수식$$ $$수식$${boxone}$$/수식$$  $$수식$$= LEFT ( $$/수식$$ $$수식$${boxtwo}$$/수식$$의 수$$수식$$RIGHT )$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${saa}$$/수식$$, ㉡ {p}\n"
    comment = "(해설)\n" \
              "바구니에 {p}를 $$수식$${saa}$$/수식$$개씩 담았으므로\n" \
              "$$수식$$LEFT ($$/수식$$바구니의 수$$수식$$RIGHT ) TIMES {saa} = LEFT ($$/수식$${p}의 수$$수식$$RIGHT )$$/수식$$,\n" \
              "$$수식$$LEFT ($$/수식$${p}의 수$$수식$$RIGHT ) DIV {saa} = LEFT ($$/수식$$바구니의 수$$수식$$RIGHT )$$/수식$$로 나타낼 수 있습니다.\n\n"


    p = ["복숭아", "사과", "포도", "망고", "자두", "딸기", "감자", "고구마", "토마토", "오이"][np.random.randint(0, 10)]
    saa = [3, 4, 6, 7, 8][np.random.randint(0, 5)]

    boxone = "box{%s````````````````````}"%"㉠"
    boxtwo = "box{%s````````````````````}"%"㉡"

    stem = stem.format(p=p, saa=saa, boxone=boxone, boxtwo=boxtwo)
    answer = answer.format(saa=saa, p=p)
    comment = comment.format(p=p, saa=saa)

    return stem, answer, comment









# 5-1-3-20
def rulandres513_Stem_005():
    stem = "형과 동생이 저금을 하려고 합니다. 형은 가지고 있던 $$수식$${saa}$$/수식$$원을 먼저 저금통에 넣었고, 두 사람은 다음 날부터 매일 $$수식$${sbb}$$/수식$$원씩 저금하기로 하였습니다. 형이 모은 돈은 {bro1}, 동생이 모은 돈은 {bro2}라고 할 때, 두 양 사이의 관계를 식으로 나타내어 보세요.\n{bro1}$$수식$$- $$수식$${boxone}$$/수식$$ = $$수식$${boxtwo}$$/수식$$$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${saa}$$/수식$$, ㉡ {bro2}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$형이 모은 돈$$수식$$RIGHT ) - {saa} = LEFT ($$/수식$$동생이 모은 돈$$수식$$RIGHT )$$/수식$$이므로\n" \
              "{bro1}$$수식$$- {saa} =$$/수식$${bro2}입니다. 또는\n" \
              "$$수식$$LEFT ($$/수식$$동생이 모은 돈$$수식$$RIGHT ) + {saa} = LEFT ($$/수식$$형이 모은 돈$$수식$$RIGHT )$$/수식$$이므로\n" \
              "{bro2}$$수식$$+ {saa} =$$/수식$${bro1}입니다.\n\n"


    while True:
        bro1 = ["■", "▲", "★", "◆", "♥", "♣"][np.random.randint(0, 6)]
        bro2 = ["■", "▲", "★", "◆", "♥", "♣"][np.random.randint(0, 6)]
        if bro1 != bro2:
            break

    saa = [500, 600, 700, 800, 900, 1000][np.random.randint(0, 6)]
    sbb = [100, 200, 300][np.random.randint(0, 3)]

    boxone = "box{%s````````````````````}"%"㉠"
    boxtwo = "box{%s````````````````````}"%"㉡"

    stem = stem.format(saa=saa, sbb=sbb, boxone=boxone, boxtwo=boxtwo, bro1=bro1, bro2=bro2)
    answer = answer.format(saa=saa, bro2=bro2)
    comment = comment.format(saa=saa, bro1=bro1, bro2=bro2)

    return stem, answer, comment










# 5-1-3-22
def rulandres513_Stem_006():
    stem = "자전거를 탄 시간과 소모된 열량 사이의 대응 관계를 알아보려고 합니다. 자전거를 탄 시간이 {time}$$수식$$LEFT ($$/수식$$분$$수식$$RIGHT )$$/수식$$이고 소모된 열량을 {kcal}$$수식$$LEFT ( rm kcal RIGHT )$$/수식$$라고 할 때, 자전거를 탄 시간과 소모된 열량 사이의 관계를 식으로 나타내어 보세요.\n$$수식$${boxone}$$/수식$$$$수식$${boxtwo}$$/수식$$$$수식$${boxthree}$$/수식$$$$수식$${boxfour}$$/수식$$$$수식$${boxfive}$$/수식$$$$수식$${boxsix}$$/수식$$\n$$수식$${boxseven}$$/수식$$$$수식$${boxeight}$$/수식$$$$수식$${boxnine}$$/수식$$$$수식$${boxten}$$/수식$$$$수식$${boxeleven}$$/수식$$$$수식$${boxtwelve}$$/수식$$\n{time}$$수식$$ $$수식$$TIMES$$/수식$$ $$수식$${boxthirteen}$$/수식$$ = $$수식$${boxfourteen}$$/수식$$$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${saa}$$/수식$$, ㉡ {kcal}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$자전거를 탄 시간$$수식$$RIGHT ) TIMES {saa} = LEFT ($$/수식$$소모된 열량$$수식$$RIGHT )$$/수식$$이므로\n" \
              "{time}$$수식$$TIMES {saa} =$$/수식$${kcal}입니다. 또는\n" \
              "$$수식$$LEFT ($$/수식$$소모된 열량$$수식$$RIGHT ) DIV {saa} = LEFT ($$/수식$$자전거를 탄 시간$$수식$$RIGHT )$$/수식$$이므로\n" \
              "{kcal}$$수식$$DIV {saa} =$$/수식$${time}입니다.\n\n"


    saa = [3, 4, 6, 7, 8][np.random.randint(0, 5)]

    boxone = "[``%s``]" % "시간(분)"
    boxtwo = "box{%d}" % 1

    if (2*saa) > 9:
        boxthree = "box{%d}" % 2
    else :
        boxthree = "box{%d}" % 2

    if (3*saa) > 9:
        boxfour = "box{%d}" % 3
    else:
        boxfour = "box{%d}" % 3

    if (4*saa) > 9:
        boxfive = "box{%d}" % 4
    else :
        boxfive = "box{%d}" % 4

    boxsix = "CDOTS CDOTS"

    boxseven = "[``%s``]" % "열량(rm kcal)"
    boxeight = "box{%d}" % saa
    boxnine = "box{%d}" % (2*saa)

    boxten = "box{%d}" % (3*saa)
    boxeleven = "box{%d}" % (4*saa)
    boxtwelve = "CDOTS CDOTS"

    boxthirteen = "box{%s````````````````````}"%"㉠"
    boxfourteen = "box{%s````````````````````}"%"㉡"

    while True:
        time = ["□", "△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 7)]
        kcal = ["□", "△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 7)]
        if time != kcal:
            break

    stem = stem.format(saa=saa, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour, boxfive=boxfive, boxsix=boxsix, boxseven=boxseven, boxeight=boxeight, boxnine=boxnine, boxten=boxten, boxeleven=boxeleven, boxtwelve=boxtwelve, boxthirteen=boxthirteen, boxfourteen=boxfourteen, time=time, kcal=kcal)
    answer = answer.format(saa=saa, kcal=kcal)
    comment = comment.format(saa=saa, time=time, kcal=kcal)

    return stem, answer, comment












# 5-1-3-23
def rulandres513_Stem_007():
    stem = "표를 완성하고 {va1}와 {va2} 사이의 대응 관계를 식으로 나타내어 보세요.\n$$수식$${boxone}$$/수식$$$$수식$${boxtwo}$$/수식$$$$수식$${boxthree}$$/수식$$$$수식$${boxfour}$$/수식$$$$수식$${boxfive}$$/수식$$$$수식$${boxsix}$$/수식$$$$수식$${boxseven}$$/수식$$\n$$수식$${boxeight}$$/수식$$$$수식$${boxnine}$$/수식$$$$수식$${boxten}$$/수식$$$$수식$${boxeleven}$$/수식$$$$수식$${boxtwelve}$$/수식$$$$수식$${boxthirteen}$$/수식$$$$수식$${boxfourteen}$$/수식$$\n{va1}$$수식$$TIMES {boxfifteen} = {boxsixteen}$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${s1}$$/수식$$, ㉡ $$수식$${s2}$$/수식$$, ㉢ $$수식$${saa}$$/수식$$, ㉣ {va2}\n"
    comment = "(해설)\n" \
              "$$수식$$1 TIMES {saa} = {saa}$$/수식$$이므로 $$수식$$4 TIMES {saa} = {s1}$$/수식$$, $$수식$$5 TIMES {saa} = {s2}$$/수식$$입니다.\n" \
              "{va1}가 $$수식$$1$$/수식$$, $$수식$$2$$/수식$$, $$수식$$3$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$으로 늘어날 때, " \
              "{va2}는 $$수식$${saa}$$/수식$$, $$수식$${saa2}$$/수식$$, $$수식$${saa3} CDOTS CDOTS$$/수식$$으로 늘어납니다.\n" \
              "따라서 {va1}$$수식$$TIMES {saa} =$$/수식$${va2} 또는 {va2}$$수식$$DIV {saa} =$$/수식$${va1}입니다.\n\n"


    while True:
        va1 = ["□", "△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 7)]
        va2 = ["□", "△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 7)]
        if va1 != va2:
            break

    saa = [3, 4, 6, 7, 8][np.random.randint(0, 5)]

    saa2 = 2 * saa
    saa3 = 3 * saa

    s1 = 4 * saa
    s2 = 5 * saa

    boxone = "box{%s}" % va1
    boxtwo = "box{%d}" % 1

    if saa2 > 9:
        boxthree = "box{%d}" % 2
    else :
        boxthree = "box{%d}" % 2

    if saa3 > 9:
        boxfour = "box{%d}" % 3
    else :
        boxfour = "box{%d}" % 3

    boxfive = "box{%d}" % 4
    boxsix = "box{%d}" % 5

    boxseven = "CDOTS CDOTS"

    boxeight = "box{%s}" % va2

    boxnine = "box{%d}" % (saa)
    boxten = "box{%d}" % (saa2)
    boxeleven = "box{%d}" % (saa3)

    boxtwelve = "box{㉠}"
    boxthirteen = "box{㉡}"
    boxfourteen = "CDOTS CDOTS"

    boxfifteen = "㉢"
    boxsixteen = "㉣"

    stem = stem.format(saa=saa, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour, boxfive=boxfive, boxsix=boxsix, boxseven=boxseven, boxeight=boxeight, boxnine=boxnine, boxten=boxten, boxeleven=boxeleven, boxtwelve=boxtwelve, boxthirteen=boxthirteen, boxfourteen=boxfourteen, boxfifteen=boxfifteen, boxsixteen=boxsixteen, va1=va1, va2=va2)
    answer = answer.format(s1=s1, s2=s2, saa=saa, va2=va2)
    comment = comment.format(s1=s1, s2=s2, saa=saa, saa2=saa2, saa3=saa3, va1=va1, va2=va2)

    return stem, answer, comment










# 5-1-3-24
def rulandres513_Stem_008():
    stem = "{p1} 한 개를 만드는 데 {p2}{j1} $$수식$${saa}$$/수식$$개 필요합니다. {p1}의 수를 {va1}, {p2}의 수를 {va2}라고 할 때, 두 양 사이의 대응 관계를 식으로 나타내어 보세요.\n{va1}$$수식$$ $$수식$$TIMES$$/수식$$ {boxone} = {boxtwo}$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${saa}$$/수식$$, ㉡ {va2}\n"
    comment = "(해설)\n" \
              "{p1} 한 개를 만드는 데 {p2}{j1} $$수식$${saa}$$/수식$$개 필요하므로 {p1}의 수가 $$수식$$1$$/수식$$개씩 늘어날 때마다 " \
              "{p2}{j1} $$수식$${saa}$$/수식$$개씩 늘어납니다.\n" \
              "따라서 {va1}$$수식$$TIMES {saa} =$$/수식$${va2} 또는 {va2}$$수식$$DIV {saa} =$$/수식$${va1}입니다.\n\n"


    p1_list = ["식빵", "토스트", "딸기잼", "사과잼", "주먹밥"]
    p2_list = ["달걀", "버터", "딸기", "사과", "햄"]

    p_num = np.random.randint(0, 5)
    p1 = p1_list[p_num]
    p2 = p2_list[p_num]

    saa = np.random.randint(2, 6)

    boxone = "$$수식$$box{㉠````````````````````}$$/수식$$"
    boxtwo = "$$수식$$box{㉡````````````````````}$$/수식$$"

    j1 = proc_jo(p2, 0)

    while True:
        va1 = ["★", "●", "◆", "■", "▲", "♠", "♥", "♣"][np.random.randint(0, 8)]
        va2 = ["★", "●", "◆", "■", "▲", "♠", "♥", "♣"][np.random.randint(0, 8)]
        if va1 != va2:
            break

    stem = stem.format(p1=p1, p2=p2, saa=saa, boxone=boxone, boxtwo=boxtwo, j1=j1, va1=va1, va2=va2)
    answer = answer.format(saa=saa, va2=va2)
    comment = comment.format(p1=p1, p2=p2, saa=saa, j1=j1, va1=va1, va2=va2)

    return stem, answer, comment














# 5-1-3-25
def rulandres513_Stem_009():
    stem = "한 모둠에 $$수식$${saa}$$/수식$$명씩 앉아 있습니다. 모둠의 수를 {va1}, 사람의 수를 {va2}라고 할 때, 두 양 사이의 대응 관계를 식으로 나타내어 보세요.\n{va1}$$수식$$TIMES$$/수식$$ $$수식$${boxone}$$/수식$$ $$수식$$=$$/수식$$ $$수식$${boxtwo}$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${saa}$$/수식$$, ㉡ {va2}\n"
    comment = "(해설)\n" \
              "$$수식$${saa}$$/수식$$명이 한 모둠으로 모둠의 수에 $$수식$${saa}$$/수식$${j1} 곱하면 사람의 수가 됩니다. " \
              "또는 $$수식$${saa}$$/수식$$명이 한 모둠이므로 사람의 수를 $$수식$${saa}$$/수식$${ro} 나누면 모둠의 수가 됩니다.\n\n"


    saa = np.random.randint(3, 8)

    boxone = "$$수식$$box{㉠````````````````````}$$/수식$$"
    boxtwo = "$$수식$$box{㉡````````````````````}$$/수식$$"

    j1 = proc_jo(saa, 1)

    if saa == 3 or saa == 6:
        ro = "으로"
    else:
        ro = "로"

    while True:
        va1 = ["★", "●", "◆", "■", "▲", "♠", "♥", "♣"][np.random.randint(0, 8)]
        va2 = ["★", "●", "◆", "■", "▲", "♠", "♥", "♣"][np.random.randint(0, 8)]
        if va1 != va2:
            break

    stem = stem.format(saa=saa, boxone=boxone, boxtwo=boxtwo, va1=va1, va2=va2)
    answer = answer.format(saa=saa, va2=va2)
    comment = comment.format(saa=saa, ro=ro, j1=j1)

    return stem, answer, comment














# 5-1-3-28
def rulandres513_Stem_010():
    stem = "한 모둠에 $$수식$${saa}$$/수식$$명씩 앉아 있습니다. 모둠의 수를 {va1}, 사람의 수를 {va2}라고 할 때, 대응 관계를 나타낸 식에 대한 친구들의 생각입니다. 생각이 틀린 친구의 이름을 써 보세요.\n$$표$$ {x1}\n{x2}\n{x3} $$/표$$\n"
    answer = "(정답)\n{p2}\n"
    comment = "(해설)\n" \
              "모둠의 수는 사람의 수에 따라 변하기 때문입니다.\n\n"


    p_name = ["기주", "현서", "진수", "민주", "진우", "혁진", "민재", "소현", "태현", "우영", "나은", "로미", "희정", "대희"]
    p_list = random.sample(p_name, 3)

    p1 = p_list[0]
    p2 = p_list[1]
    p3 = p_list[2]

    saa = np.random.randint(3, 8)


    while True:
        va1 = ["★", "●", "◆", "■", "▲", "♠", "♥", "♣"][np.random.randint(0, 8)]
        va2 = ["★", "●", "◆", "■", "▲", "♠", "♥", "♣"][np.random.randint(0, 8)]
        if va1 != va2:
            break

    y1 = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ %s는 모둠의 수를 나타내니까 $$수식$$1$$/수식$$, $$수식$$2$$/수식$$, $$수식$$3$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$과 같이 여러 가지 수가 될 수 있어." % (p1, va1)
    y2 = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ %s는 %s와 관계없이 변할 수 있어." % (p2, va1, va2)
    y3 = "$$수식$$LEFT [$$/수식$$%s$$수식$$RIGHT ]$$/수식$$ 모둠의 수를 %s, 사람의 수를 %s로 바꿔서 나타낼 수 있어." % (p3, va2, va1)

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    x1, x2, x3 = candidates


    stem = stem.format(saa=saa, va1=va1, va2=va2, x1=x1, x2=x2, x3=x3)
    answer = answer.format(p2=p2)

    return stem, answer, comment












# 5-1-3-29
def rulandres513_Stem_011():
    stem = "{saa}각형의 수와 변의 수 사이의 대응 관계를 기호를 사용하여 식으로 나타내어 보세요.\n$$표$$ {saa}각형의 수를 {va1}, 변의 수를 {va2}라고 할 때, 두 양 사이의 대응 관계를 식으로 나타내면 $$수식$${boxone} $$수식$$TIMES$$/수식$$ {boxtwo} = {boxthree}$$/수식$$입니다. $$/표$$\n"
    answer = "(정답)\n㉠ {va1}, ㉡ $$수식$${sbb}$$/수식$$, ㉢ {va2}\n"
    comment = "(해설)\n" \
              "{saa}각형의 수를 {va1}, 변의 수를 {va2}라 하면\n" \
              "$$수식$$LEFT ($$/수식$${saa}각형의 수$$수식$$RIGHT ) TIMES {sbb} = LEFT ($$/수식$$변의 수 $$수식$$RIGHT )$$/수식$$이므로\n" \
              "{va1}$$수식$$TIMES {sbb} =$$/수식$${va2}입니다. 또는\n" \
              "$$수식$$LEFT ($$/수식$$변의 수$$수식$$RIGHT ) DIV {sbb} = LEFT ($$/수식$${saa}각형의 수$$수식$$RIGHT )$$/수식$$이므로\n" \
              "{va2}$$수식$$DIV {sbb} =$$/수식$${va1}입니다.\n\n"


    while True:
        va1 = ["□", "△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 7)]
        va2 = ["□", "△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 7)]
        if va1 != va2:
            break

    saa = ["삼", "사", "오"][np.random.randint(0, 3)]

    if saa == "삼":
        sbb = 3
    elif saa == "사":
        sbb = 4
    else :
        sbb = 5

    boxone = "$$수식$$box{㉠````````````````````}$$/수식$$"
    boxtwo = "$$수식$$box{㉡````````````````````}$$/수식$$"
    boxthree = "$$수식$$box{㉢````````````````````}$$/수식$$"

    stem = stem.format(saa=saa, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, va1=va1, va2=va2)
    answer = answer.format(sbb=sbb, va1=va1, va2=va2)
    comment = comment.format(saa=saa, sbb=sbb, va1=va1, va2=va2)

    return stem, answer, comment











# 5-1-3-30
def rulandres513_Stem_012():
    stem = "{p1}는 매일 운동을 오전에 $$수식$${saa}$$/수식$$분, 오후에 $$수식$${sbb}$$/수식$$분합니다. {p1}가 운동하는 날수를 {va1}$$수식$$LEFT ($$/수식$$일$$수식$$RIGHT )$$/수식$$, 전체 운동하는 시간을 {va2}$$수식$$LEFT ($$/수식$$분$$수식$$RIGHT )$$/수식$$이라고 할 때, 두 양 사이의 대응 관계를 식으로 나타내어 보세요.\n$$수식$${boxone}$$/수식$$ $$수식$$TIMES$$/수식$$ $$수식$${boxtwo}$$/수식$$ $$수식$$=$$/수식$${va2}\n"
    answer = "(정답)\n㉠{va1}, ㉡$$수식$${sss}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$하루에 운동하는 시간$$수식$$RIGHT ) = {saa} + {sbb} = {sss} LEFT ($$/수식$$분$$수식$$RIGHT )$$/수식$$\n" \
              "날수가 $$수식$$1$$/수식$$일씩 늘어날 때마다 운동하는 시간은 $$수식$${sss}$$/수식$$분씩 늘어납니다.\n" \
              "따라서 {va1}$$수식$$TIMES {sss} =$$/수식$${va2} 또는 {va2}$$수식$$DIV {sss} =$$/수식$${va1}입니다.\n\n"


    while True:
        va1 = ["△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 6)]
        va2 = ["△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 6)]
        if va1 != va2:
            break

    p1 = ["현서", "민주", "선우", "진우", "선미", "현주", "중기", "지혜", "영주", "홍기"][np.random.randint(0, 10)]

    saa = [10, 15, 20, 25][np.random.randint(0, 4)]
    sbb = [10, 15, 20, 25][np.random.randint(0, 4)]
    sss = saa + sbb

    boxone = "$$수식$$box{㉠````````````````````}$$/수식$$"
    boxtwo = "$$수식$$box{㉡````````````````````}$$/수식$$"

    stem = stem.format(p1=p1, saa=saa, sbb=sbb, boxone=boxone, boxtwo=boxtwo, va1=va1, va2=va2)
    answer = answer.format(sss=sss, va1=va1)
    comment = comment.format(saa=saa, sbb=sbb, sss=sss, va1=va1, va2=va2)

    return stem, answer, comment













# 5-1-3-33
def rulandres513_Stem_013():
    stem = "피자 한 판이 $$수식$${saa}$$/수식$$조각으로 똑같이 나누어져 있습니다. 표를 완성하고, □ 안에 알맞은 수를 써넣으세요.\n{boxone}{boxtwo}{boxthree}{boxfour}{boxfive}{boxsix}\n{boxseven}{boxeight}{boxnine}{boxten}{boxeleven}{boxtwelve}\n$$수식$$LEFT ($$/수식$$조각의 수$$수식$$RIGHT ) = LEFT ($$/수식$$피자의 수$$수식$$RIGHT )$$/수식$$ $$수식$$TIMES$$/수식$$ $$수식$${boxthirteen}$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${a3}$$/수식$$, ㉡ $$수식$${a4}$$/수식$$, ㉢ $$수식$${saa}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$1 TIMES {saa} = {a1}$$/수식$$, $$수식$$2 TIMES {saa} = {a2}$$/수식$$이므로\n" \
              "$$수식$$3 TIMES {saa} = {a3}$$/수식$$, $$수식$$4 TIMES {saa} = {a4}$$/수식$$입니다.\n" \
              "피자의 수가 $$수식$$1$$/수식$$개씩 늘어날 때마다 조각의 수는 $$수식$${saa}$$/수식$$개씩 늘어납니다. " \
              "조각의 수는 피자 수의 $$수식$${saa}$$/수식$$배 입니다.\n\n"


    saa = [4, 6, 8, 10][np.random.randint(0, 4)]
    a1 = saa
    a2 = 2 * saa
    a3 = 3 * saa
    a4 = 4 * saa

    boxone = "[%s]" % "피자의 수 $$수식$$LEFT ( 판 RIGHT )$$/수식$$"

    if a1 > 9:
        boxtwo = "$$수식$$box{%d}$$/수식$$" % 1
    else :
        boxtwo = "$$수식$$box{%d}$$/수식$$" % 1

    if a2 > 9:
        boxthree = "$$수식$$box{%d}$$/수식$$" % 2
    else :
        boxthree = "$$수식$$box{%d}$$/수식$$" % 2

    boxfour = "$$수식$$box{%d}$$/수식$$" % 3
    boxfive = "$$수식$$box{%d}$$/수식$$" % 4
    boxsix = "$$수식$$CDOTS CDOTS$$/수식$$"

    boxseven = "[%s]" % "조각의 수 $$수식$$LEFT ( 개 RIGHT )$$/수식$$"
    boxeight = "$$수식$$box{%d}$$/수식$$" % a1
    boxnine = "$$수식$$box{%d}$$/수식$$" % a2

    boxten = "$$수식$$box{%s}$$/수식$$"%"㉠"
    boxeleven = "$$수식$$box{%s}$$/수식$$"%"㉡"
    boxtwelve = "$$수식$$CDOTS CDOTS$$/수식$$"

    boxthirteen = "box{%s}"%"㉢"

    stem = stem.format(saa=saa, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour, boxfive=boxfive, boxsix=boxsix, boxseven=boxseven, boxeight=boxeight, boxnine=boxnine, boxten=boxten, boxeleven=boxeleven, boxtwelve=boxtwelve, boxthirteen=boxthirteen)
    answer = answer.format(a3=a3, a4=a4, saa=saa)
    comment = comment.format(saa=saa, a1=a1, a2=a2, a3=a3, a4=a4)

    return stem, answer, comment












# 5-1-3-34
def rulandres513_Stem_014():
    stem = "{p1}와 {p2}가 수 카드와 연산 카드를 각각 한 장씩 골라 대응 관계를 만들고 알아맞히기를 하고 있습니다. {p1}가 말한 수를 {va1}, {p2}가 답한 수를 {va2}라고 할 때, 두 양 사이의 대응 관계를 식으로 나타내어 보시오.\n$$표$$ $$수식$$LEFT [$$/수식$${p1}$$수식$$RIGHT ]````{a1}$$/수식$$이면 → $$수식$$LEFT [$$/수식$${p2}$$수식$$RIGHT ]````{a1saa}$$/수식$$\n$$수식$$LEFT [$$/수식$${p1}$$수식$$RIGHT ]````{a2}$$/수식$$이면 → $$수식$$LEFT [$$/수식$${p2}$$수식$$RIGHT ]````{a2saa}$$/수식$$\n$$수식$$LEFT [$$/수식$${p1}$$수식$$RIGHT ]````{a3}$$/수식$$이면 → $$수식$$LEFT [$$/수식$${p2}$$수식$$RIGHT ]````{a3saa}$$/수식$$ $$/표$$\n{va1}$$수식$$+ {boxone} = {boxtwo}$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${saa}$$/수식$$, ㉡ {va2}\n"
    comment = "(해설)\n" \
              "{p1}가 만든 대응 관계는\n" \
              "$$수식$$LEFT ($$/수식$${p2}가 말한 수 $$수식$$RIGHT ) + {saa} = LEFT ($$/수식$${p2}가 답한 수$$수식$$RIGHT )$$/수식$$입니다.\n" \
              "따라서 {va1}$$수식$$+ {saa} =$$/수식$${va2} 또는 {va2}$$수식$$- {saa} =$$/수식$${va1}입니다.\n" \
              "$$수식$$LEFT ($$/수식$$힌트$$수식$$RIGHT )$$/수식$$\n" \
              "{p1}가 말한 수와 {p2}가 답한 수의 대응 관계를 알아봅시다.\n\n"



    while True:
        va1 = ["△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 6)]
        va2 = ["△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 6)]
        if va1 != va2:
            break

    p = ["현서", "민주", "선우", "진우", "선미", "현주", "은지", "수호", "태수", "혜지", "윤수", "연아", "기태"]
    p_list = random.sample(p, 2)
    p1 = p_list[0]
    p2 = p_list[1]

    saa = np.random.randint(3, 9)
    a_list = random.sample(range(6, 20), 3)
    a_list.sort()

    a1 = a_list[0]
    a2 = a_list[1]
    a3 = a_list[2]

    a1saa = a1 + saa
    a2saa = a2 + saa
    a3saa = a3 + saa

    boxone = "$$수식$$box{㉠````````````````````}$$/수식$$"
    boxtwo = "$$수식$$box{㉡````````````````````}$$/수식$$"

    stem = stem.format(a1=a1, a2=a2, a3=a3, p1=p1, p2=p2, saa=saa, boxone=boxone, boxtwo=boxtwo, a1saa=a1saa, a2saa=a2saa, a3saa=a3saa, va1=va1, va2=va2)
    answer = answer.format(saa=saa, va2=va2)
    comment = comment.format(saa=saa, a1=a1, a2=a2, a3=a3, p1=p1, p2=p2, va1=va1, va2=va2)

    return stem, answer, comment












# 5-1-3-36
def rulandres513_Stem_015():
    stem = "{p1}의 수를 {va1}, {p1} 다리의 수를 {va2}라 할 때, {va1}와 {va2} 사이의 대응 관계를 나타낸 표입니다. 표를 완성하고 {va1}와 {va2} 사이의 대응 관계를 식으로 나타내어 보세요.\n{boxone}{boxtwo}{boxthree}{boxfour}{boxfive}{boxsix}{boxseven}\n{boxeight}{boxnine}{boxten}{boxeleven}{boxtwelve}{boxthirteen}{boxfourteen}\n{va1}$$수식$$ $$수식$$TIMES$$/수식$$ {boxfifteen} = {boxsixteen}$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${a4}$$/수식$$, ㉡ $$수식$${a5}$$/수식$$, ㉢ $$수식$${saa}$$/수식$$, ㉣ {va2}\n"
    comment = "(해설)\n" \
              "$$수식$$1 TIMES {saa} = {a1}$$/수식$$, $$수식$$2 TIMES {saa} = {a2}$$/수식$$, $$수식$$3 TIMES {saa} = {a3}$$/수식$$, \n" \
              "$$수식$$4 TIMES {saa} = {a4}$$/수식$$, $$수식$$5 TIMES {saa} = {a5} CDOTS CDOTS$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${p1} 수$$수식$$RIGHT ) TIMES {saa} = LEFT ($$/수식$${p1}다리의 수$$수식$$RIGHT )$$/수식$$이므로\n" \
              "{va1}$$수식$$TIMES {saa} =$$/수식$${va2}입니다. 또는 \n" \
              "$$수식$$LEFT ($$/수식$${p1} 다리의 수$$수식$$RIGHT ) DIV {saa} =  LEFT ($$/수식$${p1}$$수식$$RIGHT )$$/수식$$이므로\n" \
              "{va2}$$수식$$DIV {saa} =$$/수식$${va1}입니다.\n\n"




    while True:
        va1 = ["△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 6)]
        va2 = ["△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 6)]
        if va1 != va2:
            break

    p1_list = ["오징어", "문어", "강아지", "의자"]
    saa_list = [10, 8, 4, 4]
    num = np.random.randint(0, 4)

    p1 = p1_list[num]
    saa = saa_list[num]

    a1 = saa
    a2 = 2 * saa
    a3 = 3 * saa
    a4 = 4 * saa
    a5 = 5 * saa


    boxone = "[%s]" % va1
    boxtwo = "$$수식$$box{%d}$$/수식$$" % 1
    boxthree = "$$수식$$box{%d}$$/수식$$" % 2
    boxfour = "$$수식$$box{%d}$$/수식$$" % 3

    boxfive = "$$수식$$box{%d}$$/수식$$" % 4
    boxsix = "$$수식$$box{%d}$$/수식$$" % 5
    boxseven = "$$수식$$CDOTS CDOTS$$/수식$$"

    boxeight = "[%s]" % va2
    boxnine = "$$수식$$box{%d}$$/수식$$" % a1
    boxten = "$$수식$$box{%d}$$/수식$$" % a2
    boxeleven = "$$수식$$box{%d}$$/수식$$" % a3

    if saa == 4:
        boxnine = "$$수식$$box{%d}$$/수식$$" % a1
        boxten = "$$수식$$box{%d}$$/수식$$" % a2
    elif saa == 8:
        boxnine = "$$수식$$box{%d}$$/수식$$" % a1

    boxtwelve = "$$수식$$box{㉠````````````````````}$$/수식$$"
    boxthirteen = "$$수식$$box{㉡````````````````````}$$/수식$$"
    boxfourteen = "$$수식$$CDOTS CDOTS$$/수식$$"

    boxfifteen = "$$수식$$box{㉢````````````````````}$$/수식$$"
    boxsixteen = "$$수식$$box{㉣````````````````````}$$/수식$$"

    stem = stem.format(p1=p1, a1=a1, a2=a2, a3=a3, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour, boxfive=boxfive, boxsix=boxsix, boxseven=boxseven, boxeight=boxeight, boxnine=boxnine, boxten=boxten, boxeleven=boxeleven, boxtwelve=boxtwelve, boxthirteen=boxthirteen, boxfourteen=boxfourteen, boxfifteen=boxfifteen, boxsixteen=boxsixteen, va1=va1, va2=va2)
    answer = answer.format(a4=a4, a5=a5, saa=saa, va2=va2)
    comment = comment.format(p1=p1, saa=saa, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, va1=va1, va2=va2)

    return stem, answer, comment














# 5-1-3-38
def rulandres513_Stem_016():
    stem = "{p1}네 샤워기에서는 $$수식$$1$$/수식$$분에 $$수식$${saa} rm L$$/수식$$의 물이 나옵니다. □ 안에 기호를 정하고 식을 알맞게 써넣으세요\n$$표$$ 샤워기를 사용한 시간을 {va1}$$수식$$LEFT ($$/수식$$분$$수식$$RIGHT )$$/수식$$, 나온 물의 양을 {va2}$$수식$$LEFT ( rm L RIGHT )$$/수식$$ 라고 할 때, 두 양 사이의 대응 관계를 식으로 나타내면\n$$수식$${boxone} $$수식$$TIMES$$/수식$$ {boxtwo} = {boxthree}$$/수식$$입니다.$$/표$$\n"
    answer = "(정답)\n㉠ {va1}, ㉡ $$수식$${saa}$$/수식$$, ㉢ {va2}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$샤워기를 사용한 시간$$수식$$RIGHT ) TIMES {saa} = LEFT ($$/수식$$물의 양$$수식$$RIGHT )$$/수식$$이므로\n" \
              "{va1}$$수식$$TIMES {saa} =$$/수식$${va2}입니다.\n\n"



    while True:
        va1 = ["△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 6)]
        va2 = ["△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 6)]
        if va1 != va2:
            break


    p1 = ["현서", "민주", "선우", "진우", "선미", "현주", "은지", "수호", "서희"][np.random.randint(0, 9)]
    saa = [10, 15, 20][np.random.randint(0, 3)]

    boxone = "$$수식$$box{㉠````````````````````}$$/수식$$"
    boxtwo = "$$수식$$box{㉡````````````````````}$$/수식$$"
    boxthree = "$$수식$$box{㉢````````````````````}$$/수식$$"

    stem = stem.format(p1=p1, saa=saa, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, va1=va1, va2=va2)
    answer = answer.format(saa=saa, va1=va1, va2=va2)
    comment = comment.format(saa=saa, va1=va1, va2=va2)

    return stem, answer, comment














# 5-1-3-39
def rulandres513_Stem_017():
    stem = "{p1}는 하루에 문제집을 $$수식$${saa}$$/수식$$쪽씩 푼다고 합니다. 문제집을 푼 날수를 {va1}, 푼 쪽수를 {va2}라고 할 때, {va1}와 {va2} 사이의 대응 관계를 식으로 나타내어 보세요.\n$$수식$${boxone} $$수식$$TIMES$$/수식$$ {boxtwo} = {boxthree}$$/수식$$\n"
    answer = "(정답)\n㉠ {va1}, ㉡ $$수식$${saa}$$/수식$$, ㉢ {va2}\n"
    comment = "(해설)\n" \
              "날수가 $$수식$$1$$/수식$$일씩 늘어날 때마다 문제집을 푼 쪽수는 $$수식$${saa}$$/수식$$쪽씩 늘어납니다.\n" \
              "$$수식$$LEFT ($$/수식$$문제집을 푼 날수$$수식$$RIGHT ) TIMES {saa} = LEFT ($$/수식$$문제집을 푼 쪽수$$수식$$RIGHT )$$/수식$$이므로 " \
              "{va1}$$수식$$TIMES {saa} =$$/수식$${va2}입니다. 또는\n" \
              "$$수식$$LEFT ($$/수식$$문제집을 푼 쪽수$$수식$$RIGHT ) DIV {saa} = LEFT ($$/수식$$문제집을 푼 날수$$수식$$RIGHT )$$/수식$$이므로 " \
              "{va2}$$수식$$DIV {saa} =$$/수식$${va1}입니다.\n\n"



    while True:
        va1 = ["△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 6)]
        va2 = ["△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 6)]
        if va1 != va2:
            break

    p1 = ["현서", "민주", "선우", "진우", "선미", "현주", "은지", "수호", "서희"][np.random.randint(0, 9)]
    saa = np.random.randint(4, 10)

    boxone = "$$수식$$box{㉠````````````````````}$$/수식$$"
    boxtwo = "$$수식$$box{㉡````````````````````}$$/수식$$"
    boxthree = "$$수식$$box{㉢````````````````````}$$/수식$$"

    stem = stem.format(p1=p1, saa=saa, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, va1=va1, va2=va2)
    answer = answer.format(saa=saa, va1=va1, va2=va2)
    comment = comment.format(saa=saa, va1=va1, va2=va2)

    return stem, answer, comment














# 5-1-3-40
def rulandres513_Stem_018():
    stem = "{p1} 한 봉지의 무게는 $$수식$${saa} rm g$$/수식$$입니다. {p1} 봉지의 수를 {va1}, {p1}의 무게를 {va2}라고 할 때, 두 양 사이의 대응 관계를 식으로 나타내고, {p1}의 무게가 $$수식$${sbb} rm g$$/수식$$일 때 {p1}{j1} 몇 봉지인지 써 보세요.\n$$수식$${boxone} $$수식$$TIMES$$/수식$$ {boxtwo} = {boxthree}$$/수식$$\n"
    answer = "(정답)\n㉠ {va1}, ㉡ $$수식$${saa}$$/수식$$, ㉢ {va2}, $$수식$${sss}$$/수식$$봉지\n"
    comment = "(해설)\n" \
              "{p1}{j2} 한 봉지씩 늘어갈 때마다 {p1}의 무게는 $$수식$${saa} rm g$$/수식$$씩 늘어나므로\n" \
              "$$수식$$LEFT ($$/수식$${p1}의 봉지의 수$$수식$$RIGHT ) TIMES {saa} = LEFT ($$/수식$${p1}의 무게$$수식$$RIGHT )$$/수식$$이므로\n" \
              "{va1}$$수식$$TIMES {saa} =$$/수식$${va2}입니다. 또는\n" \
              "$$수식$$LEFT ($$/수식$${p1}의 무게$$수식$$RIGHT ) DIV {saa} = LEFT ($$/수식$${p1}의 봉지의 수$$수식$$RIGHT )$$/수식$$이므로\n" \
              "{va2}$$수식$$DIV {saa} =$$/수식$${va1}입니다.\n\n"


    while True:
        va1 = ["△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 6)]
        va2 = ["△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 6)]
        if va1 != va2:
            break

    p1 = ["과자", "사과", "포도", "귤", "사탕", "초콜릿"][np.random.randint(0, 6)]

    saa = [60, 70, 80, 90][np.random.randint(0, 4)]
    sss = [6, 7, 8, 9][np.random.randint(0, 4)]
    sbb = saa * sss


    boxone = "$$수식$$box{㉠````````````````````}$$/수식$$"
    boxtwo = "$$수식$$box{㉡````````````````````}$$/수식$$"
    boxthree = "$$수식$$box{㉢````````````````````}$$/수식$$"

    j1 = proc_jo(p1, -1)
    j2 = proc_jo(p1, 0)

    stem = stem.format(p1=p1, saa=saa, sbb=sbb, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, j1=j1, va1=va1, va2=va2)
    answer = answer.format(saa=saa, sss=sss, va1=va1, va2=va2)
    comment = comment.format(saa=saa, p1=p1, j2=j2, va1=va1, va2=va2)

    return stem, answer, comment














# 5-1-3-41
def rulandres513_Stem_019():
    stem = "길이가 $$수식$${saa} rm {{cm}}$$/수식$$인 철사를 겹치지 않게 남김없이 모두 사용하여 직사각형 모양을 한 개 만들려고 합니다. 만든 직사각형의 긴 변의 길이를 {va1}, 짧은 변의 길이를 {va2}라고 할 때, 두 양 사이의 대응 관계를 식으로 나타내어 보세요.\n$$수식$${boxone} + {boxtwo} = {boxthree}$$/수식$$\n"
    answer = "(정답)\n㉠ {va1}, ㉡ {va2}, ㉢ $$수식$${sss}$$/수식$$\n"
    comment = "(해설)\n" \
              "길이가 $$수식$${saa} rm {{cm}}$$/수식$$인 철사로 직사각형 모양을 만들었으므로 직사각형의 네 변의 길이의 합은 $$수식$${saa} rm {{cm}}$$/수식$$입니다.\n" \
              "직사각형을 마주 보는 두 변의 길이가 같으므로\n" \
              "$$수식$$LEFT ($$/수식$$긴 변의 길이$$수식$$RIGHT ) + LEFT ($$/수식$$짧은 변의 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {saa} DIV 2 = {sss} LEFT ( rm {{cm}} RIGHT )$$/수식$$입니다.\n" \
              "따라서 {va1}$$수식$$ + {va2} =$$/수식$${sss} 또는 {va1}$$수식$$= {sss} -$$/수식$${va2} 또는\n" \
              "{va2}$$수식$$= {sss} -$$/수식$${va1}입니다.\n\n"


    while True:
        va1 = ["△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 6)]
        va2 = ["△", "☆", "◇", "♤", "♡", "♧"][np.random.randint(0, 6)]
        if va1 != va2:
            break

    while True:
        saa = np.random.randint(22, 50)
        if (saa % 2) == 0:
            break

    sss = int(saa/2)


    boxone = "$$수식$$box{㉠````````````````````}$$/수식$$"
    boxtwo = "$$수식$$box{㉡````````````````````}$$/수식$$"
    boxthree = "$$수식$$box{㉢````````````````````}$$/수식$$"

    stem = stem.format(saa=saa, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, va1=va1, va2=va2)
    answer = answer.format(sss=sss, va1=va1, va2=va2)
    comment = comment.format(saa=saa, sss=sss, va1=va1, va2=va2)

    return stem, answer, comment







