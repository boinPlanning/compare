import numpy as np
import math



















answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤"
}





















answer_kodict = {
    0: "ㄱ",
    1: "ㄴ",
    2: "ㄷ",
    3: "ㄹ",
    4: "ㅁ"
}



























answer_koonedict = {
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
    elif bool_jo(num):
        # 을를 = 1
        return "을"
    return "를"















def get_josa(a, b):
    if b == "을" or b == "를":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "를"
        else:
            return "을"

    elif b == "가" or b == "이":
        if (str(a))[-1] == "2" or (str(a))[-1] == "4" or (str(a))[-1] == "5" or (str(a))[-1] == "9":
            return "가"
        else:
            return "이"

















# 3-2-1-03
def multiplication321_Stem_001():
    stem = "계산 결과가 더 큰 쪽의 기호를 써 보세요.\n$$표$$㉠ $$수식$${sa} ` times ` {c}$$/수식$$\n㉡ $$수식$${sb} ` times ` {d}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${sa} ` times ` {c} ` = ` {a}$$/수식$$\n" \
              "㉡ $$수식$${sb} ` times ` {d} ` = ` {b}$$/수식$$\n" \
              "따라서 $$수식$${a} {x} {b}$$/수식$$이므로 계산 결과가 더 큰 쪽은 {y}입니다.\n\n"


    while True:
        c = np.random.randint(2, 10)
        d = np.random.randint(1, 5)
        if c != d:
            a1 = np.random.randint(1, 10)
            b1 = np.random.randint(1, 5)
            if ((a1 * c) == (b1 * d)) & (a1 * c <= 9) & (b1 * d <= 9) & (a1 != b1):
                a2 = np.random.randint(0, 10)
                b2 = np.random.randint(0, 5)
                if (a2 * c <= 9) & (b2 * d <= 9) & (a2 != b2):
                    a3 = np.random.randint(1, 10)
                    b3 = np.random.randint(1, 5)
                    if (a3 * c <= 9) & (b3 * d <= 9) & (a3 != b3):
                        sa = (100 * a1) + (10 * a2) + a3
                        sb = (100 * b1) + (10 * b2) + b3

                        a = sa * c
                        b = sb * d

                        if a != b:
                            break

    if a - b > 0:
        x = "&gt;"
        y = "㉠"
    else:
        x = "&lt;"
        y = "㉡"


    stem = stem.format(sa=sa, sb=sb, c=c, d=d)
    answer = answer.format(ans=y)
    comment = comment.format(sa=sa, sb=sb, a=a, b=b, c=c, d=d, x=x, y=y)

    return stem, answer, comment



































# 3-2-1-06
def multiplication321_Stem_002():
    stem = "계산 결과가 가장 큰 곱셈을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${sa} ` times ` {sd}$$/수식$$\n㉡ $$수식$${sb} ` times ` {se}$$/수식$$\n㉢ $$수식$${sc} ` times ` {sf}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${sa} ` times ` {sd} ` = ` {a}$$/수식$$\n㉡ $$수식$${sb} ` times ` {se} ` = ` {b}$$/수식$$\n㉢ $$수식$${sc} ` times ` {sf} ` = ` {c}$$/수식$$\n" \
              "따라서 $$수식$${d} ` &gt; ` {e} ` &gt; ` {f}$$/수식$$이므로 계산 결과가 가장 큰 것은 {y}입니다.\n\n"


    while True:
        sd, se, sf = [[2, 3, 4], [2, 4, 3], [3, 2, 4], [3, 4, 2], [4, 2, 3], [4, 3, 2]][np.random.randint(0, 6)]
        a1 = np.random.randint(2, 5)
        b1 = np.random.randint(2, 5)
        c1 = np.random.randint(2, 5)
        if (a1 * sd <= 9) & (b1 * se <= 9) & (c1 * sf <= 9):
            a2 = np.random.randint(0, 5)
            b2 = np.random.randint(0, 5)
            c2 = np.random.randint(0, 5)
            if (a2 * sd <= 9) & (b2 * se <= 9) & (c2 * sf <= 9) & (a2 != b2) & (b2 != c2):
                a3 = np.random.randint(1, 5)
                b3 = np.random.randint(1, 5)
                c3 = np.random.randint(1, 5)
                if (a3 * sd <= 9) & (b3 * se <= 9) & (c3 * sf <= 9) & (a3 != b3) & (b3 != c3):
                    sa = (100 * a1) + (10 * a2) + a3
                    sb = (100 * b1) + (10 * b2) + b3
                    sc = (100 * c1) + (10 * c2) + c3
                    a = sa * sd
                    b = sb * se
                    c = sc * sf
                    if (a != b) & (a != c) & (b != c):
                        break


    list = [a, b, c]
    list = sorted(list)

    d = list[2]
    e = list[1]
    f = list[0]

    if a == d:
        y = "㉠"
    elif b == d:
        y = "㉡"
    elif c == d:
        y = "㉢"


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf)
    answer = answer.format(ans=y)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, a=a, b=b, c=c, d=d, e=e, f=f, y=y)

    return stem, answer, comment








































# 3-2-1-07
def multiplication321_Stem_003():
    stem = "다음을 $$수식$${sb}$$/수식$$배 한 수를 구해 보세요.\n$$표$$백 모형이 $$수식$${a1}$$/수식$$개, 십 모형이 $$수식$${a2}$$/수식$$개, 일 모형이 $$수식$${a3}$$/수식$$개인 수$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "백 모형이 $$수식$${a1}$$/수식$$개, 십 모형이 $$수식$${a2}$$/수식$$개, 일 모형이 $$수식$${a3}$$/수식$$개인 수는 $$수식$${a}$$/수식$$입니다.\n" \
              "따라서 $$수식$${a} ` times ` {sb} ` = ` {b}$$/수식$$입니다.\n\n"


    while True:
        sb = np.random.randint(2, 5)
        a1 = np.random.randint(2, 5)
        if a1 * sb <= 9:
            a2 = np.random.randint(0, 5)
            if (a2 * sb <= 9) & (a2 != a1):
                a3 = np.random.randint(1, 5)
                if (a3 * sb <= 9) & (a3 != a2):
                    break


    a = (100 * a1) + (10 * a2) + a3
    b = a * sb


    stem = stem.format(sb=sb, a1=a1, a2=a2, a3=a3)
    answer = answer.format(ans=b)
    comment = comment.format(a=a, b=b, sb=sb, a1=a1, a2=a2, a3=a3)

    return stem, answer, comment







































# 3-2-1-08
def multiplication321_Stem_004():
    stem = "{s}{j1} 한 상자에 $$수식$${a1}{a2}{a3}$$/수식$$개씩 들어 있습니다. $$수식$${sb}$$/수식$$상자에는 {s}{j1} 모두 몇 개 들어 있나요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( {sb}$$/수식$$상자에 들어 있는 {s}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$한 상자에 들어 있는 {s}의 수$$수식$$RIGHT ) times LEFT ($$/수식$$상자의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {a} ` times ` {sb}$$/수식$$\n" \
              "$$수식$$= ` {b} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"


    s = ["귤", "키위", "방울토마토", "체리", "살구", "앵두"][np.random.randint(0, 6)]
    j1 = proc_jo(s, 0)

    while True:
        sb = np.random.randint(2, 5)
        a1 = np.random.randint(2, 5)
        if a1 * sb <= 9:
            a2 = np.random.randint(0, 5)
            if (a2 * sb <= 9) & (a2 != a1):
                a3 = np.random.randint(1, 5)
                if (a3 * sb <= 9):
                    break


    a = (100 * a1) + (10 * a2) + a3
    b = a * sb


    stem = stem.format(sb=sb, a1=a1, a2=a2, a3=a3, s=s, j1=j1)
    answer = answer.format(ans=b)
    comment = comment.format(a=a, b=b, sb=sb, s=s)

    return stem, answer, comment






































# 3-2-1-09
def multiplication321_Stem_005():
    stem = "{p}이는 {s}을 {day} $$수식$${a1}{a2}{a3}$$/수식$$쪽씩 읽습니다. {p}이가 $$수식$${sb}$$/수식$$일 동안 읽는 {s}은 모두 몇 쪽인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$쪽\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${p}이가 $$수식$${sb}$$/수식$$일 동안 읽는 {s}의 쪽수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$${day} 읽는 {s}의 쪽수$$수식$$RIGHT ) times LEFT ($$/수식$$날수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {a} ` times ` {sb}$$/수식$$\n" \
              "$$수식$$= ` {b} ` LEFT ($$/수식$$쪽$$수식$$RIGHT )$$/수식$$\n\n"


    p = ["서준", "민영", "혁진", "혜란", "도윤", "주현"][np.random.randint(0, 6)]
    s = ["동화책", "소설책", "위인전"][np.random.randint(0, 3)]
    day = ["하루에", "매일"][np.random.randint(0, 2)]


    while True:
        sb = np.random.randint(3, 5)
        a1 = 1
        a2 = np.random.randint(0, 4)
        if a2 * sb <= 9:
            a3 = np.random.randint(2, 4)
            if (a3 * sb <= 9):
                break


    a = (100 * a1) + (10 * a2) + a3
    b = a * sb


    stem = stem.format(sb=sb, a1=a1, a2=a2, a3=a3, s=s, p=p, day=day)
    answer = answer.format(ans=b)
    comment = comment.format(a=a, b=b, sb=sb, s=s, p=p, day=day)

    return stem, answer, comment




































# 3-2-1-10
def multiplication321_Stem_006():
    stem = "수학 {book}에 있는 문제를 {p1}는 매일 $$수식$${a1}{a2}{a3}$$/수식$$문제씩 $$수식$${sc}$$/수식$$일 동안 풀었고, {p2}는 매일 $$수식$${b1}{b2}{b3}$$/수식$$문제씩 $$수식$${sd}$$/수식$$일 동안 풀었습니다. 두 사람 중 누가 문제를 몇 문제 더 풀었나요?\n"
    answer = "(정답)\n{p3}, $$수식$${z}$$/수식$$문제\n"
    comment = "(해설)\n" \
              "{p1}: $$수식$${a} ` times ` {sc} ` = ` {c} LEFT ($$/수식$$문제$$수식$$RIGHT )$$/수식$$\n {p2}: $$수식$${b} ` times ` {sd} ` = ` {d} LEFT ($$/수식$$문제$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 $$수식$${x} ` &gt; ` {y}$$/수식$$이므로 {p3}가 $$수식$${x} ` - ` {y} ` = ` {z} 문제$$/수식$$ 더 풀었습니다.\n\n"


    book = ["연산책", "문제집", "교과서", "학습지"][np.random.randint(0, 4)]

    while True:
        p1 = ["지호", "연아", "은우", "시우", "혁재", "민하"][np.random.randint(0, 6)]
        p2 = ["지호", "연아", "은우", "시우", "혁재", "민하"][np.random.randint(0, 6)]
        if p1 != p2:
            break

    while True:
        sc, sd = [[2, 3], [2, 4], [3, 2], [3, 4], [4, 2], [4, 3]][np.random.randint(0, 6)]
        if sc > sd:
            a1 = 1
            b1 = 2
        else:
            a1 = 2
            b1 = 1
        a2 = np.random.randint(0, 5)
        b2 = np.random.randint(0, 5)
        if (a2 * sc <= 9) & (b2 * sd <= 9):
            a3 = np.random.randint(1, 5)
            b3 = np.random.randint(1, 5)
            if (a3 * sc <= 9) & (b3 * sd <= 9) & (a3 != b3):
                break

    a = (100 * a1) + (10 * a2) + a3
    b = (100 * b1) + (10 * b2) + b3
    c = a * sc
    d = b * sd

    # max
    x = max(c, d)
    # min
    y = min(c, d)

    if x == c:
        p3 = p1
    else:
        p3 = p2

    z = x - y


    stem = stem.format(a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, sc=sc, sd=sd, p1=p1, p2=p2, book=book)
    answer = answer.format(p3=p3, z=z)
    comment = comment.format(a=a, b=b, c=c, d=d, sc=sc, sd=sd, x=x, y=y, z=z, p3=p3, p1=p1, p2=p2)

    return stem, answer, comment





































# 3-2-1-12
def multiplication321_Stem_007():
    stem = "덧셈식을 곱셈식으로 고쳐서 계산하려고 합니다. ㉠, ㉡, ㉢에 알맞은 수를 차례로 쓰세요.\n$$수식$${a1}{a2}{a3}$$/수식$${f}\n→ $$수식$${one}$$/수식$$ $$수식$$` times `$$/수식$$ $$수식$${two}$$/수식$$ $$수식$$` = `$$/수식$$ $$수식$${thr}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a}$$/수식$$, $$수식$${n}$$/수식$$, $$수식$${b}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a}$$/수식$$을 $$수식$${n}$$/수식$$번 더하는 것이므로 곱셈식으로 나타내면 $$수식$${a} ` times ` {n}$$/수식$$입니다.\n" \
              "$$수식$${a} ` times ` {n} ` = ` {b}$$/수식$$\n\n"


    one = "box{㉠````````````````````}"
    two = "box{㉡````````````````````}"
    thr = "box{㉢````````````````````}"

    while True:
        n = np.random.randint(3, 6)
        a3 = np.random.randint(2, 9)
        if 10 <= a3 * n:
            sb = math.floor((a3 * n) / 10)
            a2 = np.random.randint(0, 3)
            if a2 * n <= 9 - sb:
                a1 = np.random.randint(1, 3)
                if a1 * n <= 9:
                    break

    a = (100 * a1) + (10 * a2) + a3
    b = a * n

    f = ""
    for i in range(n - 1):
        f = f + "+$$수식$$%d$$/수식$$" % a


    stem = stem.format(one=one, two=two, thr=thr, f=f, a1=a1, a2=a2, a3=a3)
    answer = answer.format(a=a, n=n, b=b)
    comment = comment.format(a=a, b=b, n=n)

    return stem, answer, comment


































# 3-2-1-15
def multiplication321_Stem_008():
    stem = "계산 결과를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${a1}{a2}{a3} ` times ` {sc}$$/수식$$  ○  $$수식$${b1}{b2}{b3} ` times ` {sd}$$/수식$$\n"
    answer = "(정답)\n$$수식$${x}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` times ` {sc} ` = ` {c}$$/수식$$, $$수식$${b} ` times ` {sd} ` = ` {d}$$/수식$$이므로 $$수식$${c} ` {x} ` {d}$$/수식$$입니다.\n\n"


    while True:
        sc, sd = [[2, 3], [2, 4], [3, 2], [4, 2]][np.random.randint(0, 4)]
        a3 = np.random.randint(3, 10)
        if 10 <= a3 * sc:
            se = math.floor((a3 * sc) / 10)
            a2 = np.random.randint(0, 5)
            if a2 * sc <= 9 - se:
                a1 = sd
                b3 = np.random.randint(3, 10)
                if 10 <= b3 * sd:
                    sf = math.floor((b3 * sd) / 10)
                    b2 = np.random.randint(0, 5)
                    if (b2 * sd <= 9 - sf) & (b2 != a2):
                        b1 = sc
                        break


    a = (100 * a1) + (10 * a2) + a3
    b = (100 * b1) + (10 * b2) + b3
    c = a * sc
    d = b * sd

    if c > d:
        x = "&gt;"
    elif c == d:
        x = "="
    elif c < d:
        x = "&lt;"


    stem = stem.format(a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, sc=sc, sd=sd)
    answer = answer.format(x=x)
    comment = comment.format(a=a, b=b, c=c, d=d, sc=sc, sd=sd, x=x)

    return stem, answer, comment






































# 3-2-1-17
def multiplication321_Stem_009():
    stem = "계산 결과가 더 큰 곱셈식을 고른 사람은 누구인가요?\n$$표$$ {p1}: $$수식$${a1}{a2}{a3} ` times ` {sc}$$/수식$$    {p2}: $$수식$${b1}{b2}{b3} ` times ` {sd}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{p3}\n"
    comment = "(해설)\n" \
              "{p1}: $$수식$${a} ` times ` {sc} ` = ` {c} LEFT ($$/수식$$문제$$수식$$RIGHT )$$/수식$$\n {p2}: $$수식$${b} ` times ` {sd} ` = ` {d} LEFT ($$/수식$$문제$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 $$수식$${c} {x} {d}$$/수식$$이므로 {p3}가 고른 곱셈식의 계산 결과가 더 큽니다.\n\n"


    while True:
        p1 = ["민주", "지호", "연아", "은우", "시우", "혁재", "민하"][np.random.randint(0, 7)]
        p2 = ["민주", "지호", "연아", "은우", "시우", "혁재", "민하"][np.random.randint(0, 7)]
        if p1 != p2:
            break


    while True:
        sc, sd = [[2, 3], [2, 4], [3, 2], [4, 2]][np.random.randint(0, 4)]
        a3 = np.random.randint(3, 10)
        if 10 <= a3 * sc:
            se = math.floor((a3 * sc) / 10)
            a2 = np.random.randint(0, 5)
            if a2 * sc <= 9 - se:
                a1 = sd
                b3 = np.random.randint(3, 10)
                if 10 <= b3 * sd:
                    sf = math.floor((b3 * sd) / 10)
                    b2 = np.random.randint(0, 5)
                    if (b2 * sd <= 9 - sf) & (b2 != a2):
                        b1 = sc
                        break


    a = (100 * a1) + (10 * a2) + a3
    b = (100 * b1) + (10 * b2) + b3
    c = a * sc
    d = b * sd

    if c > d:
        x = "&gt;"
        p3 = p1
    else:
        x = "&lt;"
        p3 = p2


    stem = stem.format(a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, sc=sc, sd=sd, p1=p1, p2=p2)
    answer = answer.format(p3=p3)
    comment = comment.format(a=a, b=b, c=c, d=d, sc=sc, sd=sd, x=x, p3=p3, p1=p1, p2=p2)

    return stem, answer, comment






































# 3-2-1-18
def multiplication321_Stem_010():
    stem = "설명하는 수를 $$수식$${sb}$$/수식$$배 한 수는 얼마인가요?\n$$표$$$$수식$$100$$/수식$$이 $$수식$${a1}$$/수식$$개, $$수식$$10$$/수식$$이 $$수식$${a2}$$/수식$$개, $$수식$$1$$/수식$$이 $$수식$${a3}$$/수식$$개$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$100$$/수식$$이 $$수식$${a1}$$/수식$$개, $$수식$$10$$/수식$$이 $$수식$${a2}$$/수식$$개, $$수식$$1$$/수식$$이 $$수식$${a3}$$/수식$$개인 수는 $$수식$${a}$$/수식$$입니다.\n" \
              "따라서 $$수식$${a} ` times ` {sb} ` = ` {b}$$/수식$$입니다.\n\n"


    while True:
        sb = np.random.randint(3, 6)
        a3 = np.random.randint(3, 10)
        if a3 * sb >= 10:
            sc = math.floor((a3 * sb) / 10)
            a2 = np.random.randint(0, 5)
            if a2 * sb <= 9 - sc:
                a1 = np.random.randint(1, 4)
                if a1 * sb <= 9:
                    break

    a = (100 * a1) + (10 * a2) + a3
    b = a * sb


    stem = stem.format(sb=sb, a1=a1, a2=a2, a3=a3)
    answer = answer.format(ans=b)
    comment = comment.format(a=a, b=b, sb=sb, a1=a1, a2=a2, a3=a3)

    return stem, answer, comment







































# 3-2-1-20
def multiplication321_Stem_011():
    stem = "어떤 수에 $$수식$${sb}$$/수식$$를 곱해야 하는데 잘못하여 더했더니 $$수식$${a}$$/수식$$이 되었습니다. 바르게 계산한 값은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □ 라 하면\n" \
              "□$$수식$$+ ` {sb} ` = ` {a}$$/수식$$, □$$수식$$= ` {a} ` - ` {sb}$$/수식$$, □$$수식$$= ` {b}$$/수식$$입니다.\n" \
              "따라서 바르게 계산하면 $$수식$${b} ` times ` {sb} ` = ` {c}$$/수식$$입니다.\n\n"


    while True:
        sb = np.random.randint(3, 6)
        a3 = np.random.randint(3, 10)
        if a3 * sb >= 10:
            sc = math.floor((a3 * sb) / 10)
            a2 = np.random.randint(0, 5)
            if a2 * sb <= 9 - sc:
                a1 = np.random.randint(1, 4)
                if a1 * sb <= 9:
                    break

    b = (100 * a1) + (10 * a2) + a3
    a = b + sb
    c = b * sb


    stem = stem.format(sb=sb, a=a)
    answer = answer.format(ans=c)
    comment = comment.format(a=a, b=b, sb=sb, c=c)

    return stem, answer, comment



































# 3-2-1-24
def multiplication321_Stem_012():
    stem = "다음 중 올림이 두 번 있는 계산은 어느 것인가요?\n① $$수식$${sa}$$/수식$$ ② $$수식$${sb}$$/수식$$ ③ $$수식$${sc}$$/수식$$\n④ $$수식$${sd}$$/수식$$ ⑤ $$수식$${se}$$/수식$$\n"
    answer = "(정답)\n{x}\n"
    comment = "(해설)\n" \
              "{x} 일의 자리: $$수식$${one}$$/수식$$, 십의 자리: $$수식$${ten}$$/수식$$, 백의 자리: $$수식$${hun}$$/수식$$\n" \
              "따라서 올림이 두 번 있는 계산은 {x}입니다.\n\n"


    # a
    while True:
        a4 = np.random.randint(3, 7)
        a3 = np.random.randint(2, 7)
        if a3 * a4 >= 10:
            a2 = np.random.randint(2, 7)
            if a2 * a4 >= 10:
                a1 = 1
                break

    # b
    while True:
        b4 = np.random.randint(3, 7)
        b3 = np.random.randint(2, 7)
        if b3 * b4 >= 10:
            b5 = math.floor((b3 * b4) / 10)
            b2 = np.random.randint(0, 5)
            if b2 * b4 <= 9 - b5:
                b1 = np.random.randint(1, 4)
                if b1 * b4 <= 9:
                    break

    # c
    while True:
        c4 = np.random.randint(3, 7)
        if c4 != a4:
            c3 = np.random.randint(0, 3)
            if c3 * c4 <= 9:
                c2 = np.random.randint(2, 7)
                if c2 * c4 >= 10:
                    c5 = math.floor((c2 * c4) / 10)
                    c1 = np.random.randint(1, 4)
                    if c1 * c4 <= 9 - c5:
                        break

    # d
    while True:
        d4 = np.random.randint(3, 6)
        d3 = np.random.randint(1, 6)
        if d3 * d4 <= 9:
            d2 = np.random.randint(0, 5)
            if d2 * d4 <= 9:
                d1 = np.random.randint(1, 4)
                if d1 * d4 <= 9:
                    break

    # e
    while True:
        e4 = np.random.randint(3, 7)
        if e4 != b4:
            e3 = np.random.randint(2, 7)
            if e3 * e4 >= 10:
                e5 = math.floor((e3 * e4) / 10)
                e2 = np.random.randint(0, 5)
                if e2 * e4 <= 9 - e5:
                    e1 = np.random.randint(1, 4)
                    if e1 * e4 <= 9:
                        break

    sa = "%d%d%d ` times ` %d" % (a1, a2, a3, a4)
    sb = "%d%d%d ` times ` %d" % (b1, b2, b3, b4)
    sc = "%d%d%d ` times ` %d" % (c1, c2, c3, c4)
    sd = "%d%d%d ` times ` %d" % (d1, d2, d3, d4)
    se = "%d%d%d ` times ` %d" % (e1, e2, e3, e4)

    ans = sa

    a = a3 * a4
    b = math.floor(a / 10)
    c = b + (a2 * a4)
    d = math.floor(c / 10)
    e = d + (a1 * a4)

    one = "%d ` times ` %d ` = ` %d" % (a3, a4, a)
    ten = "%d ` + ` %d ` times ` %d ` = ` %d" % (b, a2, a4, c)
    hun = "%d ` + ` %d ` times ` %d ` = ` %d" % (d, a1, a4, e)

    candidates = [sa, sb, sc, sd, se]
    np.random.shuffle(candidates)

    sa, sb, sc, sd, se = candidates

    correct_idx = 0

    for i, s in enumerate(candidates):
        if s == ans:
            correct_idx = i
            break

    x = answer_dict[correct_idx]


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)
    answer = answer.format(x=x)
    comment = comment.format(one=one, ten=ten, hun=hun, x=x)

    return stem, answer, comment






































# 3-2-1-28
def multiplication321_Stem_013():
    stem = "계산 결과를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${a1}{a2}{a3} ` times ` {sc}$$/수식$$  ○  $$수식$${b1}{b2}{b3} ` times ` {sd}$$/수식$$\n"
    answer = "(정답)\n$$수식$${x}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` times ` {sc} ` = ` {c}$$/수식$$, $$수식$${b} ` times ` {sd} ` = ` {d}$$/수식$$이므로 $$수식$${c} ` {x} ` {d}$$/수식$$입니다.\n\n"


    while True:
        sc, sd = [[2, 3], [2, 4], [3, 2], [4, 2]][np.random.randint(0, 4)]
        a3 = np.random.randint(1, 5)
        if a3 * sc <= 9:
            a2 = np.random.randint(4, 10)
            if a2 * sc >= 10:
                a1 = np.random.randint(3, 9)
                b1 = np.random.randint(3, 9)
                if (10 <= a1 * sc) & (10 <= b1 * sd) & (-3 <= (a1 * sc) - (b1 * sd)) & ((a1 * sc) - (b1 * sd) <= 3):
                    b3 = np.random.randint(1, 10)
                    if b3 * sd <= 9:
                        b2 = np.random.randint(4, 10)
                        if (10 <= b2 * sd) & (b2 != a2):
                            break


    a = (100 * a1) + (10 * a2) + a3
    b = (100 * b1) + (10 * b2) + b3
    c = a * sc
    d = b * sd

    if c > d:
        x = "&gt;"
    elif c == d:
        x = "="
    elif c < d:
        x = "&lt;"


    stem = stem.format(a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, sc=sc, sd=sd)
    answer = answer.format(x=x)
    comment = comment.format(a=a, b=b, c=c, d=d, sc=sc, sd=sd, x=x)

    return stem, answer, comment







































# 3-2-1-29
def multiplication321_Stem_014():
    stem = "어느 시 {s}의 어린이 요금은 $$수식$${a}$$/수식$$원입니다. 어린이 $$수식$${sb}$$/수식$$명이 {s}{j1} 타려면 얼마를 준비해야 하나요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$원\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$어린이 $$수식$${sb}$$/수식$$명의 요금$$수식$$RIGHT ) ` = ` LEFT ($$/수식$$어린이 요금$$수식$$RIGHT ) ` times ` LEFT ($$/수식$$어린이의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$ = ` {a} ` times ` {sb} ` = ` {b} LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$\n\n"


    s = ["지하철", "버스", "마을버스"][np.random.randint(0, 3)]
    j1 = proc_jo(s, 1)

    sb = np.random.randint(4, 9)
    a3 = 0
    a2 = np.random.randint(3, 10)
    a1 = np.random.randint(4, 7)

    a = (100 * a1) + (10 * a2) + a3
    b = a * sb


    stem = stem.format(sb=sb, a=a, s=s, j1=j1)
    answer = answer.format(ans=b)
    comment = comment.format(a=a, b=b, sb=sb)

    return stem, answer, comment






































# 3-2-1-31
def multiplication321_Stem_015():
    stem = "{s}을 매일 {p1}는 $$수식$${a}$$/수식$$쪽씩, {p2}는 $$수식$${b}$$/수식$$쪽씩 읽었습니다. 이 두 사람이 $$수식$${sb}$$/수식$$일 동안 읽은 {s}은 모두 몇 쪽인가요?\n"
    answer = "(정답)\n$$수식$${d}$$/수식$$쪽\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$두 사람이 매일 읽은 쪽수$$수식$$RIGHT ) ` = ` {a} ` + ` {b} ` = ` {c} ` $$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$두 사람이 $$수식$${sb}$$/수식$$일 동안 읽은 쪽수$$수식$$RIGHT )$$/수식$$\n$$수식$$ ` = ` LEFT ($$/수식$$두 사람이 매일 읽은 쪽수$$수식$$RIGHT ) ` times ` LEFT ($$/수식$$날수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$ = ` {c} ` times ` {sb} ` = ` {d} LEFT ($$/수식$$쪽$$수식$$RIGHT )$$/수식$$\n\n"


    s = ["동화책", "소설책", "위인전"][np.random.randint(0, 3)]

    while True:
        p1 = ["채아", "민주", "지호", "연아", "은우", "시우", "혁재", "민하"][np.random.randint(0, 8)]
        p2 = ["채아", "민주", "지호", "연아", "은우", "시우", "혁재", "민하"][np.random.randint(0, 8)]
        if p1 != p2:
            break

    while True:
        sb = np.random.randint(3, 5)
        a2 = np.random.randint(3, 7)
        if 10 <= a2 * sb:
            break

    a3 = 2
    a1 = 1

    c = (100 * a1) + (10 * a2) + a3
    sc = np.random.randint(4, 10)
    a = int((c / 2) - sc)
    b = int((c / 2) + sc)
    d = c * sb


    stem = stem.format(p1=p1, p2=p2, s=s, a=a, b=b, sb=sb)
    answer = answer.format(d=d)
    comment = comment.format(a=a, b=b, c=c, d=d, sb=sb)

    return stem, answer, comment





































# 3-2-1-32
def multiplication321_Stem_016():
    stem = "어떤 수에 $$수식$${sb}$$/수식$${j1} 곱해야 하는데 잘못하여 $$수식$${sb}$$/수식$${j1} 뺐더니 $$수식$${a}$$/수식$$이 되었습니다. 바르게 계산한 값은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □ 라 하면\n" \
              "□$$수식$$- ` {sb} ` = ` {a}$$/수식$$, □$$수식$$= ` {a} ` + ` {sb}$$/수식$$, □$$수식$$` = ` {b}$$/수식$$입니다.\n" \
              "따라서 바르게 계산하면 $$수식$${b} ` times ` {sb} ` = ` {c}$$/수식$$입니다.\n\n"


    while True:
        sb = np.random.randint(3, 6)
        a3 = np.random.randint(1, 4)
        if a3 * sb <= 9:
            break

    a2 = np.random.randint(4, 10)
    a1 = 1
    b = (100 * a1) + (10 * a2) + a3
    a = b - sb
    c = b * sb
    j1 = proc_jo(sb, 1)


    stem = stem.format(sb=sb, a=a, j1=j1)
    answer = answer.format(ans=c)
    comment = comment.format(a=a, b=b, sb=sb, c=c)

    return stem, answer, comment






































# 3-2-1-34
def multiplication321_Stem_017():
    stem = "{p1}는 $$수식$${a}$$/수식$$쪽짜리 책을 $$수식$${sc}$$/수식$$권을 읽었고, {p2}는 $$수식$${b}$$/수식$$쪽짜리 책을 $$수식$${sd}$$/수식$$권 읽었습니다. 두 사람이 읽은 책은 모두 몇 쪽인가요?\n"
    answer = "(정답)\n$$수식$${e}$$/수식$$쪽\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${p1}가 읽은 책의 쪽수$$수식$$RIGHT ) ` = {a} ` times ` {sc} ` = ` {c} LEFT ($$/수식$$쪽$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${p2}가 읽은 책의 쪽수$$수식$$RIGHT ) ` = {b} ` times ` {sd} ` = ` {d} LEFT ($$/수식$$쪽$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 두 사람이 읽은 책은 모두 $$수식$${c} ` + ` {d} ` = ` {e} LEFT ($$/수식$$쪽$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    while True:
        p1 = ["현수", "채아", "민주", "지호", "연아", "은우", "시우", "혁재", "민하"][np.random.randint(0, 9)]
        p2 = ["현수", "채아", "민주", "지호", "연아", "은우", "시우", "혁재", "민하"][np.random.randint(0, 9)]
        if p1 != p2:
            break

    while True:
        sc = np.random.randint(2, 5)
        sd = np.random.randint(2, 5)
        a3 = 2 * np.random.randint(1, 2)
        b3 = 2 * np.random.randint(1, 2)

        if (a3 * sc <= 9) & (b3 * sd <= 9):
            a2 = np.random.randint(3, 10)
            b2 = np.random.randint(3, 10)
            if (a2 * sc >= 10) & (b2 * sd >= 10) & (a2 != b2):
                break

    a1 = 1
    b1 = 1

    a = (100 * a1) + (10 * a2) + a3
    b = (100 * b1) + (10 * b2) + b3

    c = a * sc
    d = b * sd
    e = c + d


    stem = stem.format(a=a, b=b, sc=sc, sd=sd, p1=p1, p2=p2)
    answer = answer.format(e=e)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, sc=sc, sd=sd, p1=p1, p2=p2)

    return stem, answer, comment




































# 3-2-1-37
def multiplication321_Stem_018():
    stem = "□ 안에 들어갈 수가 다른 하나를 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${sa}$$/수식$$\n㉡ $$수식$${sb}$$/수식$$\n㉢ $$수식$${sc}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${aa}$$/수식$$\n" \
              "㉡ $$수식$${ab}$$/수식$$\n" \
              "㉢ $$수식$${ac}$$/수식$$\n" \
              "따라서 □ 안에 들어갈 수가 다른 하나는 {x}입니다.\n\n"


    while True:
        a, b, c, d = [[3, 4, 2, 6], [2, 9, 3, 6], [4, 4, 8, 2], [3, 8, 4, 6], [6, 6, 4, 9]][np.random.randint(0, 5)]
        e = np.random.randint(2, 10)
        f = np.random.randint(2, 10)

        if (e != f) & (e != a) & (e != b) & (e != c) & (e != d) & (f != a) & (f != b) & (f != c) & (f != d):
            break


    g = a * b
    h = c * d
    i = e * f

    sa = "%d0 ` times ` %d0 ` = ` □00 `" % (a, b)
    sb = "%d0 ` times ` %d0 ` = ` □00 `" % (c, d)
    sc = "%d0 ` times ` %d0 ` = ` □00 `" % (e, f)

    aa = "%d0 ` times ` %d0 ` = ` %d00 `" % (a, b, g)
    ab = "%d0 ` times ` %d0 ` = ` %d00 `" % (c, d, h)
    ac = "%d0 ` times ` %d0 ` = ` %d00 `" % (e, f, i)

    candidates = [[sa, aa], [sb, ab], [sc, ac]]
    ans = candidates[2]
    np.random.shuffle(candidates)

    [sa, aa], [sb, ab], [sc, ac] = candidates

    correct_idx = 0

    for i, s in enumerate(candidates):
        if s == ans:
            correct_idx = i
            break

    x = answer_kodict[correct_idx]


    stem = stem.format(sa=sa, sb=sb, sc=sc)
    answer = answer.format(ans=x)
    comment = comment.format(aa=aa, ab=ab, ac=ac, x=x)

    return stem, answer, comment



































# 3-2-1-39
def multiplication321_Stem_019():
    stem = "계산 결과가 두 번째로 작은 곱셈을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${sa}0 ` times ` {sb}0$$/수식$$    ㉡ $$수식$${sc}0 ` times ` {sd}0$$/수식$$\n㉢ $$수식$${se}0 ` times ` {sf}0$$/수식$$    ㉣ $$수식$${sg}0 ` times ` {sh}0$$/수식$$$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${sa}0 ` times ` {sb}0 ` = ` {a}$$/수식$$    ㉡ $$수식$${sc}0 ` times ` {sd}0 ` = ` {b}$$/수식$$\n" \
              "㉢ $$수식$${se}0 ` times ` {sf}0 ` = ` {c}$$/수식$$    ㉣ $$수식$${sg}0 ` times ` {sh}0 ` = ` {d}$$/수식$$\n" \
              "따라서 $$수식$${e} ` &lt; ` {f} ` &lt; ` {g} ` &lt; ` {h}$$/수식$$이므로 계산 결과가 두 번째로 작은 곱셈은 {x}입니다.\n\n"


    while True:
        sa = np.random.randint(2, 10)
        sb = np.random.randint(2, 10)
        sc = np.random.randint(2, 10)
        sd = np.random.randint(2, 10)
        if (sa * sb) != (sc * sd):
            se = np.random.randint(2, 10)
            sf = np.random.randint(2, 10)
            if (sa * sb != se * sf) & (se * sf != sc * sd):
                sg = np.random.randint(2, 10)
                sh = np.random.randint(2, 10)
                if (sa * sb != sg * sh) & (sg * sh != sc * sd) & (sg * sh != se * sf):
                    break


    a = sa * sb * 100
    b = sc * sd * 100
    c = se * sf * 100
    d = sg * sh * 100

    list = [a, b, c, d]
    list = sorted(list)

    e = list[0]
    f = list[1]
    g = list[2]
    h = list[3]

    if a == f:
        x = "ㄱ"
    elif b == f:
        x = "ㄴ"
    elif c == f:
        x = "ㄷ"
    elif d == f:
        x = "ㄹ"


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sh=sh)
    answer = answer.format(ans=x)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg, sh=sh, a=a, b=b, c=c, d=d, e=e, f=f, g=g,
                             h=h, x=x)

    return stem, answer, comment
































# 3-2-1-40
def multiplication321_Stem_020():
    stem = "계산 결과를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${a} ` times ` {sa}0$$/수식$$  ○  $$수식$${b} ` times ` {sb}0$$/수식$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` times ` {sa}0 ` = ` {c}$$/수식$$, $$수식$${b} ` times ` {sb}0 ` = ` {d}$$/수식$$이므로 $$수식$${c} ` {x} ` {d}$$/수식$$입니다.\n\n"


    while True:
        sa = np.random.randint(3, 9)
        sb = np.random.randint(2, 10)
        if sa != sb:
            a = np.random.randint(11, 92)
            if a % 10 != 0:
                b = np.random.randint(21, 82)
                if (b % 10 != 0) & (a != b):
                    if (((a * sa) - 10) / sb <= b) & (((a * sa) + 10) / sb >= b):
                        break


    c = a * sa * 10
    d = b * sb * 10

    if c > d:
        x = "&gt;"
    elif c == d:
        x = "="
    elif c < d:
        x = "&lt;"


    stem = stem.format(a=a, b=b, sa=sa, sb=sb)
    answer = answer.format(ans=x)
    comment = comment.format(a=a, b=b, sa=sa, sb=sb, c=c, d=d, x=x)

    return stem, answer, comment


































# 3-2-1-41
def multiplication321_Stem_021():
    stem = "□ 안에 알맞은 수를 구하세요.\n$$수식$${a} ` times ` {b} ` = ` {c} ` times $$/수식$$ $$수식$${box}$$/수식$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` times ` {b} ` = ` {e}$$/수식$$이고, $$수식$${sc} ` times ` {sd} ` = ` {se}$$/수식$$이므로 $$수식$${c} ` times ` {d} ` = ` {e}$$/수식$$입니다.\n" \
              "따라서 □ 안에 알맞은 수는 $$수식$${d}$$/수식$$입니다.\n\n"

    box = "box{　　　}"
    sa, sb, sc, sd = \
    [[3, 4, 2, 6], [6, 2, 4, 3], [2, 9, 3, 6], [6, 3, 9, 2], [4, 4, 8, 2], [8, 2, 4, 4], [3, 8, 4, 6], [6, 4, 8, 3],
     [6, 6, 4, 9], [9, 4, 6, 6]][np.random.randint(0, 10)]
    se = sc * sd
    a = sa * 10
    b = sb * 10
    c = sc * 10
    d = sd * 10
    e = a * b


    stem = stem.format(a=a, b=b, c=c, box=box)
    answer = answer.format(ans=d)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, sc=sc, sd=sd, se=se)

    return stem, answer, comment

































# 3-2-1-42
def multiplication321_Stem_022():
    stem = "하루는 $$수식$$24$$/수식$$시간이고, $$수식$$1$$/수식$$시간은 $$수식$$60$$/수식$$분입니다. {s}{j1} 몇 분인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$분\n"
    comment = "(해설)\n" \
              "{s}{j1} $$수식$${a}$$/수식$$시간이고, $$수식$$1$$/수식$$시간은 $$수식$$60$$/수식$$분이므로 " \
              "{s}{j1} $$수식$${a} ` times ` 60 ` = ` {b} LEFT ($$/수식$$분$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    s = ["오전", "오후", "하루", "이틀", "사흘", "나흘"][np.random.randint(0, 6)]

    if s == "오전" or s == "오후":
        a = 12
    elif s == "하루":
        a = 24
    elif s == "이틀":
        a = 48
    elif s == "사흘":
        a = 72
    elif s == "나흘":
        a = 96

    b = a * 60

    j1 = proc_jo(s, -1)


    stem = stem.format(s=s, j1=j1)
    answer = answer.format(ans=b)
    comment = comment.format(s=s, a=a, b=b, j1=j1)

    return stem, answer, comment





































# 3-2-1-43
def multiplication321_Stem_023():
    stem = "한 대에 $$수식$${a}$$/수식$$명씩 탈 수 있는 {vehi}가 있습니다. 이 {vehi} $$수식$${b}$$/수식$$대에 탈 수 있는 사람은 모두 몇 명인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$명\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${vehi}에 탈 수 있는 사람 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` LEFT ($$/수식$${vehi} 한 대에 탈 수 있는 사람 수$$수식$$RIGHT ) ` times ` LEFT ($$/수식$${vehi}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {a} ` times ` {b} ` = ` {c} LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$\n\n"


    vehi = ["버스", "차", "기차", "비행기", "배"][np.random.randint(0, 5)]
    a = [12, 14, 15, 16, 17, 25, 28, 31, 35, 45][np.random.randint(0, 10)]
    b = 10 * np.random.randint(2, 10)
    c = a * b


    stem = stem.format(a=a, b=b, vehi=vehi)
    answer = answer.format(ans=c)
    comment = comment.format(a=a, b=b, c=c, vehi=vehi)

    return stem, answer, comment






































# 3-2-1-44
def multiplication321_Stem_024():
    stem = "과일 가게에 {s}{j1} $$수식$${a}$$/수식$$개씩 $$수식$${b}$$/수식$$줄로 놓여 있습니다. 과일 가게에 놓여 있는 {s}{j2} 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$전체 {s}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` LEFT ($$/수식$$한 줄에 놓여 있는 {s}의 수$$수식$$RIGHT ) ` times ` LEFT ($$/수식$$줄 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {a} ` times ` {b} ` = ` {c} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"


    s = ["귤", "한라봉", "사과", "토마토", "복숭아", "배", "참외", "망고", "파파야", "자두"][np.random.randint(0, 10)]
    j1 = proc_jo(s, 0)
    j2 = proc_jo(s, -1)

    while True:
        a = np.random.randint(21, 72)
        if a % 10 != 0:
            break

    b = 10 * np.random.randint(2, 7)
    c = a * b


    stem = stem.format(a=a, b=b, s=s, j1=j1, j2=j2)
    answer = answer.format(ans=c)
    comment = comment.format(a=a, b=b, c=c, s=s)

    return stem, answer, comment






































# 3-2-1-45
def multiplication321_Stem_025():
    stem = "{p}네 반 학생 수는 $$수식$${b}$$/수식$$명입니다. 선생님께서 학생들에게 {pen}을 $$수식$${a}$$/수식$$자루씩 나누어 주었더니 $$수식$${d}$$/수식$$자루가 남았습니다. 처음에 {pen}은 몇 자루 있었나요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$자루\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$학생들에게 나누어 준 {pen}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` LEFT ($$/수식$$학생 한 명에게 나누어 준 {pen}의 수$$수식$$RIGHT ) ` times ` LEFT ($$/수식$$학생 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {a} ` times ` {b} ` = ` {c} LEFT ($$/수식$$자루$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$처음 {pen}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` LEFT ($$/수식$$학생들에게 나누어 준 {pen}의 수$$수식$$RIGHT ) ` + ` LEFT ($$/수식$$남은 {pen}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {c} ` + ` {d} ` = ` {e} LEFT ($$/수식$$자루$$수식$$RIGHT )$$/수식$$\n\n"


    p = ["현수", "채아", "민주", "지호", "연아", "은우", "시우", "혁재", "민하"][np.random.randint(0, 9)]
    pen = ["연필", "만년필", "볼펜", "펜", "색연필"][np.random.randint(0, 5)]

    while True:
        a = np.random.randint(21, 72)
        if a % 10 != 0:
            break

    b = 10 * np.random.randint(2, 5)
    c = a * b
    d = np.random.randint(11, b)
    e = c + d


    stem = stem.format(a=a, b=b, p=p, d=d, pen=pen)
    answer = answer.format(ans=e)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, pen=pen)

    return stem, answer, comment



































# 3-2-1-46
def multiplication321_Stem_026():
    stem = "{p}는 $$수식$${a}$$/수식$$원짜리 {s} $$수식$${b}$$/수식$$자루를 사고 $$수식$${d}$$/수식$$원을 냈습니다. {p}가 받아야 하는 거스름돈은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$원\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${s} $$수식$${b}$$/수식$$자루의 값$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` LEFT ($$/수식$${s} 한 자루의 값$$수식$$RIGHT ) ` times ` LEFT ($$/수식$${s}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {a} ` times ` {b} ` = ` {c} LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$\n" \
              "따라서 {p}가 받아야 하는 거스름돈은 $$수식$${d} ` - ` {c} ` = ` {e} LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    p = ["현수", "채아", "민주", "지호", "연아", "은우", "시우", "혁재", "민하"][np.random.randint(0, 9)]
    s = ["연필", "볼펜", "색연필", "사인펜", "형광펜"][np.random.randint(0, 5)]

    while True:
        sa = np.random.randint(25, 93)
        if sa % 10 != 0:
            break

    a = 10 * sa

    while True:
        b = np.random.randint(3, 10)
        if b != 5:
            if (sa * b) % 100 != 0:
                break

    c = a * b
    sc = math.floor(c / 1000)
    d = (sc + 1) * 1000
    e = d - c


    stem = stem.format(a=a, b=b, p=p, d=d, s=s)
    answer = answer.format(ans=e)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, s=s, p=p)

    return stem, answer, comment




































# 3-2-1-49
def multiplication321_Stem_027():
    stem = "계산 결과가 큰 것부터 차례대로 기호를 써 보세요.\n$$표$$㉠ $$수식$${sa}`times`{a}$$/수식$$\n㉡ $$수식$${sb}`times`{b}$$/수식$$\n㉢ $$수식$${sc}`times`{c}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${sa} ` times ` {a} ` = ` {d}$$/수식$$, ㉡ $$수식$${sb} ` times ` {b} ` = ` {e}$$/수식$$, ㉢ $$수식$${sc} ` times ` {c} ` = ` {f}$$/수식$$\n" \
              "따라서 $$수식$${g} ` &gt; ` {h} ` &gt; ` {i}$$/수식$$이므로 큰 것부터 차례대로 기호를 써 보면 {x}입니다.\n\n"


    while True:
        sa = np.random.randint(4, 8)
        sb = np.random.randint(3, 9)
        sc = np.random.randint(2, 10)
        if (sa != sb) & (sa != sc) & (sb != sc):
            a = np.random.randint(33, 74)
            if (a % 10 != 0):
                b = np.random.randint(23, 84)
                if (b % 10 != 0) & (b != a) & ((sa * a - 15) / sb <= b) & (b <= (sa * a + 15) / sb):
                    c = np.random.randint(13, 94)
                    if (c % 10 != 0) & (c != a) & (c != b) & ((sb * b - 15) / sc <= c) & (c <= (sb * b + 15) / sc):
                        d = sa * a
                        e = sb * b
                        f = sc * c
                        if (d != e) & (d != f) & (e != f):
                            break


    list = [d, e, f]
    list = sorted(list)

    g = list[2]
    h = list[1]
    i = list[0]

    if d == g:
        if e == h:
            x = "ㄱ, ㄴ, ㄷ"
        elif f == h:
            x = "ㄱ, ㄷ, ㄴ"

    elif e == g:
        if f == h:
            x = "ㄴ, ㄷ, ㄱ"
        elif d == h:
            x = "ㄴ, ㄱ, ㄷ"

    elif f == g:
        if d == h:
            x = "ㄷ, ㄱ, ㄴ"
        elif e == h:
            x = "ㄷ, ㄴ, ㄱ"


    stem = stem.format(sa=sa, sb=sb, sc=sc, a=a, b=b, c=c)
    answer = answer.format(ans=x)
    comment = comment.format(sa=sa, sb=sb, sc=sc, a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, x=x)

    return stem, answer, comment



































# 3-2-1-50
def multiplication321_Stem_028():
    stem = "곱이 가장 작은 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${sa} ` times ` {a}$$/수식$$\n㉡ $$수식$${sb} ` times ` {b}$$/수식$$\n㉢ $$수식$${sc} ` times ` {c}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${sa} ` times ` {a} ` = ` {d}$$/수식$$ ㉡ $$수식$${sb} ` times ` {b} ` = ` {e}$$/수식$$ ㉢ $$수식$${sc} ` times ` {c} ` = ` {f}$$/수식$$\n" \
              "따라서 $$수식$${g} ` &lt; ` {h} ` &lt; ` {i}$$/수식$$이므로 곱이 가장 작은 것은 {x}입니다.\n\n"


    while True:
        sa = np.random.randint(4, 8)
        sb = np.random.randint(3, 9)
        sc = np.random.randint(2, 10)
        if (sa != sb) & (sa != sc) & (sb != sc):
            a = np.random.randint(33, 74)
            if (a % 10 != 0):
                b = np.random.randint(23, 84)
                if (b % 10 != 0) & (b != a) & ((sa * a - 15) / sb <= b) & (b <= (sa * a + 15) / sb):
                    c = np.random.randint(13, 94)
                    if (c % 10 != 0) & (c != a) & (c != b) & ((sb * b - 15) / sc <= c) & (c <= (sb * b + 15) / sc):
                        d = sa * a
                        e = sb * b
                        f = sc * c
                        if (d != e) & (d != f) & (e != f):
                            break


    list = [d, e, f]
    list = sorted(list)

    g = list[0]
    h = list[1]
    i = list[2]

    if d == g:
        x = "ㄱ"

    elif e == g:
        x = "ㄴ"

    elif f == g:
        x = "ㄷ"


    stem = stem.format(sa=sa, sb=sb, sc=sc, a=a, b=b, c=c)
    answer = answer.format(ans=x)
    comment = comment.format(sa=sa, sb=sb, sc=sc, a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, x=x)

    return stem, answer, comment



































# 3-2-1-52
def multiplication321_Stem_029():
    stem = "가장 작은 수와 가장 큰 수의 곱은 얼마인가요?\n$$표$$$$수식$${sa}$$/수식$$    $$수식$${sb}$$/수식$$    $$수식$${sc}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "가장 작은 수는 $$수식$${a}$$/수식$$이고 가장 큰 수는 $$수식$${c}$$/수식$$입니다.\n" \
              "따라서 곱은 $$수식$${a} ` times ` {c} ` = ` {d}$$/수식$$입니다.\n\n"


    while True:
        sa = np.random.randint(3, 10)
        sb = np.random.randint(13, 93)
        sc = np.random.randint(13, 93)
        if (sb % 10 != 0) & (sc % 10 != 0):
            if sb < sc:
                break


    d = sa * sc
    a = sa
    c = sc

    candidates = [sa, sb, sc]
    np.random.shuffle(candidates)
    sa, sb, sc = candidates


    stem = stem.format(sa=sa, sb=sb, sc=sc)
    answer = answer.format(ans=d)
    comment = comment.format(a=a, c=c, d=d)

    return stem, answer, comment




































# 3-2-1-53
def multiplication321_Stem_030():
    stem = "옷 한 벌에 {s}{j1} $$수식$${a}$$/수식$$개씩 달려 있습니다. 옷 $$수식$${b}$$/수식$$벌에 달려 있는 {s}{j2} 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$모든 {s}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` LEFT ($$/수식$$옷 한 벌에 달려 있는 {s}의 수$$수식$$RIGHT ) ` times ` LEFT ($$/수식$$옷의 벌 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {a} ` times ` {b} ` = ` {c} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"


    s = ["단추", "장식", "리본", "구슬"][np.random.randint(0, 4)]
    j1 = proc_jo(s, 0)
    j2 = proc_jo(s, -1)


    while True:
        b = np.random.randint(14, 53)
        if b % 10 != 0:
            break

    a = np.random.randint(3, 7)
    c = a * b


    stem = stem.format(a=a, b=b, s=s, j1=j1, j2=j2)
    answer = answer.format(ans=c)
    comment = comment.format(a=a, b=b, c=c, s=s)

    return stem, answer, comment


































# 3-2-1-54
def multiplication321_Stem_031():
    stem = "{s}{j1} 한 줄에 $$수식$${a}$$/수식$$개씩 $$수식$${b}$$/수식$$줄 있습니다. 이 중에서 {s} $$수식$${d}$$/수식$$개를 먹었다면 남은 {s}{j2} 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$처음에 있던 {s}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` LEFT ($$/수식$$한 줄에 있는 {s}의 수$$수식$$RIGHT ) ` times ` LEFT ($$/수식$$줄 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {a} ` times ` {b} ` = ` {c} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$남은 {s}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` LEFT ($$/수식$$처음에 있던 {s}의 수$$수식$$RIGHT ) ` - ` LEFT ($$/수식$$먹은 {s}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {c} ` - ` {d} ` = ` {e} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"


    s = ["곶감", "초콜릿", "호두과자", "마카롱"][np.random.randint(0, 4)]
    j1 = proc_jo(s, 0)
    j2 = proc_jo(s, -1)

    a = np.random.randint(5, 10)

    while True:
        b = np.random.randint(14, 40)
        d = np.random.randint(3, 16)
        if (b % 10 != 0) and (d % 10 != 0):
            break

    c = a * b
    e = c - d


    stem = stem.format(a=a, b=b, d=d, s=s, j1=j1, j2=j2)
    answer = answer.format(ans=e)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, s=s)

    return stem, answer, comment



































# 3-2-1-55
def multiplication321_Stem_032():
    stem = "설명하는 두 수의 곱은 얼마인가요?\n$$표$$∙ $$수식$${sa}$$/수식$$씩 $$수식$${sb}$$/수식$$묶음인 수\n∙ $$수식$$10$$/수식$$이 $$수식$${sc}$$/수식$$개, $$수식$$1$$/수식$$이 $$수식$${sd}$$/수식$$개인 수$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "∙ $$수식$${sa}$$/수식$$씩 $$수식$${sb}$$/수식$$묶음인 수는 $$수식$${sa} ` times ` {sb} ` = ` {a}$$/수식$$입니다.\n" \
              "∙ $$수식$$10$$/수식$$이 $$수식$${sc}$$/수식$$개, $$수식$$1$$/수식$$이 $$수식$${sd}$$/수식$$개인 수는 $$수식$${b} ` + ` {sd} ` = ` {c}$$/수식$$입니다.\n" \
              "따라서 두 수의 곱은 $$수식$${a} ` times ` {c} ` = ` {d}$$/수식$$입니다.\n\n"

    while True:
        sa = np.random.randint(2, 9)
        sb = np.random.randint(2, 9)
        if sa * sb <= 9:
            sc = np.random.randint(2, 9)
            if (sc != sa) and (sc != sb):
                sd = np.random.randint(2, 9)
                if (sd != sb) and (sd != sc):
                    break


    a = sa * sb
    b = sc * 10
    c = b + sd
    d = a * c


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(ans=d)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, a=a, b=b, c=c, d=d)

    return stem, answer, comment


































# 3-2-1-56
def multiplication321_Stem_033():
    stem = "봉지 한 장에 {s1}를 $$수식$${a}$$/수식$$개씩 담았더니 $$수식$${b}$$/수식$$봉지가 되었고, 봉지 한 장에 {s2}를 $$수식$${c}$$/수식$$개씩 담았더니 $$수식$${d}$$/수식$$봉지가 되었습니다. 어떤 과일이 몇 개 더 많은지 구해 보세요.\n"
    answer = "(정답)\n{s3}, $$수식$${i}$$/수식$$개\n"
    comment = "(해설)\n" \
              "{s1}는 $$수식$${a} ` times ` {b} ` = ` {e} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$이고, " \
              "{s2}는 $$수식$${c} ` times ` {d} ` = ` {f} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$입니다.\n" \
              "따라서 $$수식$${e} ` {x} ` {f}$$/수식$$이므로 {s3}가 $$수식$${g} ` - ` {h} ` = ` {i} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$ 더 많이 있습니다.\n\n"


    while True:
        s1 = ["사과", "배", "토마토", "복숭아", "참외", "키위", "자두", "바나나"][np.random.randint(0, 8)]
        s2 = ["사과", "배", "토마토", "복숭아", "참외", "키위", "자두", "바나나"][np.random.randint(0, 8)]
        if s1 != s2:
            break

    while True:
        while True:
            a = np.random.randint(5, 9)
            b = np.random.randint(17, 27)
            c = np.random.randint(4, 10)
            d = np.random.randint(13, 42)
            if (b % 10 != 0) and (a != c) and (d % 10 != 0) and ((a * b - 20) / c <= d) and (d <= (a * b + 20) / c):
                break
        e = a * b
        f = c * d
        if e != f:
            break


    if e > f:
        x = "&gt;"
        s3 = s1
        g = e
        h = f

    elif e < f:
        x = "&lt;"
        s3 = s2
        g = f
        h = e

    i = g - h


    stem = stem.format(a=a, b=b, c=c, d=d, s1=s1, s2=s2)
    answer = answer.format(s3=s3, i=i)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, s1=s1, s2=s2, s3=s3, x=x)

    return stem, answer, comment




































# 3-2-1-60
def multiplication321_Stem_034():
    stem = "㉠과 ㉡의 합은 얼마인가요?\n$$표$$㉠ $$수식$${a1}{a2} ` times ` {b1}{b2}$$/수식$$    ㉡ $$수식$${c1}{c2}$$/수식$$의 $$수식$${d1}{d2}$$/수식$$배$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${a} ` times ` {b} ` = ` {e}$$/수식$$입니다.\n" \
              "㉡ $$수식$${c}$$/수식$$의 $$수식$${d}$$/수식$$배는 $$수식$${c} ` times ` {d} ` = ` {f}$$/수식$$입니다.\n" \
              "따라서 ㉠$$수식$$` + `$$/수식$$㉡$$수식$$` = ` {e} ` + ` {f} ` = ` {g}$$/수식$$입니다.\n\n"


    while True:
        a1 = np.random.randint(1, 4)
        b1 = np.random.randint(1, 4)
        a2 = np.random.randint(1, 10)
        b2 = np.random.randint(1, 10)
        if a2 != b2:
            if (a2 * b2 <= 9):
                if (a1 * b2 >= 10) & (a2 * b1 <= 9):
                    break
            elif (a2 * b2 >= 10):
                if (a1 * b2 <= 9) & (a2 * b1 <= 9):
                    break


    while True:
        c1 = np.random.randint(1, 4)
        d1 = np.random.randint(1, 4)
        c2 = np.random.randint(1, 10)
        d2 = np.random.randint(1, 10)
        if c2 != d2:
            if (c2 * d2 <= 9):
                if (c1 * d2 >= 10) & (c2 * d1 <= 9):
                    break
            elif (c2 * d2 >= 10):
                if (c1 * d2 <= 9) & (c2 * d1 <= 9):
                    break


    a = a1 * 10 + a2
    b = b1 * 10 + b2
    c = c1 * 10 + c2
    d = d1 * 10 + d2

    e = a * b
    f = c * d
    g = e + f


    stem = stem.format(a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, d1=d1, d2=d2)
    answer = answer.format(ans=g)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f, g=g)

    return stem, answer, comment



































# 3-2-1-61
def multiplication321_Stem_035():
    stem = "가장 큰 수와 가장 작은 수의 곱을 구해 보세요.\n$$표$$$$수식$${sa}$$/수식$$    $$수식$${sb}$$/수식$$    $$수식$${sc}$$/수식$$    $$수식$${sd}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` &gt; ` {c} ` &gt; ` {d} ` &gt; ` {b}$$/수식$$이므로 가장 큰 수는 $$수식$${a}$$/수식$$이고, 가장 작은 수는 $$수식$${b}$$/수식$$입니다.\n" \
              "따라서 가장 큰 수와 가장 작은 수의 곱은 $$수식$${a} ` times ` {b} ` = ` {e}$$/수식$$입니다.\n\n"


    while True:
        a1 = np.random.randint(1, 4)
        b1 = np.random.randint(1, 4)
        a2 = np.random.randint(1, 10)
        b2 = np.random.randint(1, 10)
        if (a2 > b2) and (a1 > b1):
            if (a2 * b2 <= 9):
                if (a1 * b2 >= 10) and (a2 * b1 <= 9):
                    break
            elif (a2 * b2 >= 10):
                if (a1 * b2 <= 9) and (a2 * b1 <= 9):
                    break


    a = a1 * 10 + a2
    b = b1 * 10 + b2

    while True:
        c = np.random.randint(b + 1, a)
        d = np.random.randint(b + 1, a)
        if c > d:
            break

    e = a * b

    candidates = [a, b, c, d]
    np.random.shuffle(candidates)
    sa, sb, sc, sd = candidates


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(ans=e)
    comment = comment.format(a=a, c=c, d=d, b=b, e=e)

    return stem, answer, comment


































# 3-2-1-63
def multiplication321_Stem_036():
    stem = "$$수식$$2$$/수식$$개의 수를 골라 $$수식$$LEFT ($$/수식$$몇십몇$$수식$$RIGHT ) ` times ` LEFT ($$/수식$$몇십몇$$수식$$RIGHT )$$/수식$$의 곱셈식을 만들려고 합니다. ㉠, ㉡에 알맞은 수를 차례로 써 보세요.\n$$표$$$$수식$${sa}$$/수식$$    $$수식$${sb}$$/수식$$    $$수식$${sc}$$/수식$$    $$수식$${sd}$$/수식$$$$/표$$\n$$수식$${one} ` times ` {two} ` = ` {e}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a}$$/수식$$, $$수식$${b}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} ` times ` {b} ` = ` {e}$$/수식$$이므로 곱이 $$수식$${e}$$/수식$$이 되는 두 수는 $$수식$${a}$$/수식$$, $$수식$${b}$$/수식$$입니다.\n\n"


    one = "㉠"
    two = "㉡"


    while True:
        a2, b2, c2, d2 = [[4, 6, 1, 1], [5, 5, 1, 1], [6, 6, 1, 1], [8, 6, 1, 1]][np.random.randint(0, 4)]

        while True:
            a1 = np.random.randint(1, 4)
            b1 = np.random.randint(1, 4)
            c1 = np.random.randint(2, 5)
            d1 = np.random.randint(2, 5)
            if (c1 != d1):
                if (a1 * b2 <= 9) & (a2 * b1 <= 9) & (a2 * c1 >= 9) & (a2 * d1 >= 9):
                    break

        a = a1 * 10 + a2
        # print("a: %d" % a)
        b = b1 * 10 + b2
        # print("b: %d" % b)
        c = c1 * 10 + c2
        d = d1 * 10 + d2
        e = a * b

        if a != b:
            break


    while True:
        candidates = [a, b, c, d]
        np.random.shuffle(candidates)
        sa, sb, sc, sd = candidates
        ai = candidates.index(a)
        bi = candidates.index(b)
        if ai <= bi:
            break


    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, one=one, two=two, e=e)
    answer = answer.format(a=a, b=b)
    comment = comment.format(a=a, b=b, e=e)

    return stem, answer, comment




































# 3-2-1-65
def multiplication321_Stem_037():
    stem = "선물 한 개를 포장하는 데 {s1} 리본 $$수식$${c} ` rm {{cm}}$$/수식$$, {s2} 리본 $$수식$${d} ` rm {{cm}}$$/수식$$가 필요합니다. 같은 선물 $$수식$${b}$$/수식$$개를 포장하는 데 필요한 리본은 모두 몇 $$수식$$rm {{cm}}$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${ans} ` rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$선물 한 개를 포장하는 데 필요한 리본의 길이$$수식$$RIGHT )$$/수식$$\n$$수식$$ ` = ` {c} ` + ` {d} ` = ` {a} ` LEFT ( ` rm {{cm}} ` RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$선물 $$수식$${b}$$/수식$$개를 포장하는 데 필요한 리본의 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` LEFT ($$/수식$$선물 한 개를 포장하는 데 필요한 리본의 길이$$수식$$RIGHT )$$/수식$$\n$$수식$$ ` times ` LEFT ($$/수식$$선물의 개수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {a} ` times ` {b} ` = ` {e} ` LEFT ( ` rm {{cm}} ` RIGHT )$$/수식$$\n\n"


    while True:
        s1 = ["파란색", "빨간색", "노란색", "초록색", "분홍색", "하늘색", "주황색", "보라색", "남색"][np.random.randint(0, 9)]
        s2 = ["파란색", "빨간색", "노란색", "초록색", "분홍색", "하늘색", "주황색", "보라색", "남색"][np.random.randint(0, 9)]
        if s1 != s2:
            break


    while True:
        a1 = np.random.randint(2, 4)
        b1 = 1
        a2 = np.random.randint(4, 10)
        b2 = np.random.randint(1, 5)
        if a2 != b2:
            if (a2 * b2 >= 10) and (a1 * b2 <= 9) and (a2 * b1 <= 9):
                break


    a = a1 * 10 + a2
    b = b1 * 10 + b2

    while True:
        sc = np.random.randint(-9, 10)
        if not (-2 <= sc) & (sc <= 2):
            c = math.floor(a / 2) + sc
            if (11 <= c) & (11 <= a - sc):
                break

    d = a - c
    e = a * b


    stem = stem.format(b=b, c=c, d=d, s1=s1, s2=s2)
    answer = answer.format(ans=e)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e)

    return stem, answer, comment



































# 3-2-1-66
def multiplication321_Stem_038():
    stem = "{p}네 학교 $$수식$$3$$/수식$$학년 선생님과 학생이 {s}을 가려고 $$수식$${c}$$/수식$$인승 버스 $$수식$${b}$$/수식$$대에 나누어 탔습니다. 버스마다 $$수식$${d}$$/수식$$자리씩 비어 있다면 $$수식$$3$$/수식$$학년 선생님과 학생은 모두 몇 명인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$명\n"
    comment = "(해설)\n" \
              "버스 한 대에 탄 선생님과 학생은 $$수식$${c} ` - ` {d} ` = ` {a} LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$입니다.\n" \
              "따라서 $$수식$$3$$/수식$$학년 선생님과 학생은 모두 $$수식$${a} ` times ` {b} ` = ` {e} LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    p = ["현수", "채아", "민주", "지호", "연아", "은우", "시우", "혁재", "민하"][np.random.randint(0, 9)]
    s = ["소풍", "체험 학습", "박물관 관람", "수학여행", "봉사활동"][np.random.randint(0, 5)]

    while True:
        c = [16, 17, 25, 28, 31, 35, 45][np.random.randint(0, 7)]
        d = np.random.randint(2, 5)
        a1 = (c - d) // 10
        a2 = (c - d) % 10
        b1 = 1
        b2 = np.random.randint(1, 10)
        if (a2 * b2 <= 9):
            if (a1 * b2 >= 10):
                break
        if (a2 * b2 > 9):
            if (a1 * b2 <= 9):
                break


    a = c - d
    b = b1 * 10 + b2
    e = a * b


    stem = stem.format(b=b, c=c, d=d, p=p, s=s)
    answer = answer.format(ans=e)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e)

    return stem, answer, comment



































# 3-2-1-68
def multiplication321_Stem_039():
    stem = "계산 결과가 다른 하나를 찾아 기호를 써 보세요.\n$$표$$㉠ {ca}    ㉡ {cb}    ㉢ {cc}$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "㉠ {ca}{cg},  ㉡ {cb}{ch},  ㉢ {cc}{ci}\n" \
              "따라서 계산 결과가 다른 것은 {x}입니다.\n\n"


    while True:
        list = [2, 3, 4, 6, 7, 9]
        np.random.shuffle(list)
        sa, sb, sc, sd, se, sf = list
        if sa < sb < sc < sd < se:
            # print("%d %d %d %d %d" % (sa, sb, sc, sd, se))
            break


    a = sa * sd
    b = sb * sc
    c = sb * sd
    d = sa * sc
    e = se * sd
    f = sb * se

    g = a * b
    h = c * d
    i = e * f


    ca = "$$수식$$%d ` times ` %d$$/수식$$" % (a, b)
    cb = "$$수식$$%d ` times ` %d$$/수식$$" % (c, d)
    cc = "$$수식$$%d ` times ` %d$$/수식$$" % (e, f)

    ans = cc

    cg = "$$수식$$` = `%d$$/수식$$" % (g)
    ch = "$$수식$$` = `%d$$/수식$$" % (h)
    ci = "$$수식$$` = `%d$$/수식$$" % (i)

    candidates = [[ca, cg], [cb, ch], [cc, ci]]
    np.random.shuffle(candidates)
    [ca, cg], [cb, ch], [cc, ci] = candidates

    for i, s in enumerate(candidates):
        if s[0] == ans:
            correct_idx = i
            break

    x = answer_kodict[correct_idx]


    stem = stem.format(ca=ca, cb=cb, cc=cc)
    answer = answer.format(ans=x)
    comment = comment.format(ca=ca, cb=cb, cc=cc, cg=cg, ch=ch, ci=ci, x=x)

    return stem, answer, comment




































# 3-2-1-69
def multiplication321_Stem_040():
    stem = "계산 결과가 큰 것부터 차례대로 기호를 써 보세요.\n$$표$$㉠ $$수식$${a} ` times ` {b}$$/수식$$      ㉡ $$수식$${c} ` times ` {d}$$/수식$$      ㉢ $$수식$${e} ` times ` {f}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${a} ` times ` {b} ` = ` {g}$$/수식$$,  ㉡ $$수식$${c} ` times ` {d} ` = ` {h}$$/수식$$,\n  ㉢ $$수식$${e} ` times ` {f} ` = ` {i}$$/수식$$\n" \
              "따라서 $$수식$${sa} ` &gt; ` {sb} ` &gt; ` {sc}$$/수식$$이므로 계산 결과가 큰 것부터 기호를 쓰면 {x}입니다.\n\n"


    while True:
        a = np.random.randint(34, 72)
        b = np.random.randint(33, 74)
        c = np.random.randint(24, 82)
        e = np.random.randint(14, 92)
        if (a != c) & (a != e) & (c != e):
            if (a % 10 != 0) & (b % 10 != 0) & (c % 10 != 0) & (e % 10 != 0):
                d = np.random.randint(23, 84)
                if (d % 10 != 0) & (d != b) & ((a * b - 100) / c <= d) & (d <= (a * b + 100) / c):
                    f = np.random.randint(13, 94)
                    if (f % 10 != 0) & (f != b) & (f != d) & ((c * d - 100) / e <= f) & (f <= (c * d + 100) / e):
                        break


    g = a * b
    h = c * d
    i = e * f

    list = [g, h, i]
    list = sorted(list)

    sa = list[2]
    sb = list[1]
    sc = list[0]

    if g == sa:
        if h == sb:
            x = "ㄱ, ㄴ, ㄷ"
        elif i == sb:
            x = "ㄱ, ㄷ, ㄴ"

    elif h == sa:
        if i == sb:
            x = "ㄴ, ㄷ, ㄱ"
        elif g == sb:
            x = "ㄴ, ㄱ, ㄷ"

    elif i == sa:
        if g == sb:
            x = "ㄷ, ㄱ, ㄴ"
        elif h == sb:
            x = "ㄷ, ㄴ, ㄱ"


    stem = stem.format(a=a, b=b, c=c, d=d, e=e, f=f)
    answer = answer.format(ans=x)
    comment = comment.format(sa=sa, sb=sb, sc=sc, a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, x=x)

    return stem, answer, comment


































# 3-2-1-72
def multiplication321_Stem_041():
    stem = "{instru}의 틀 안에 길이가 다른 현 $$수식$${a}$$/수식$$개가 끼워져 있습니다. 이 {instru} $$수식$${b}$$/수식$$개에는 현이 모두 몇 개 있나요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${instru} $$수식$${b}$$/수식$$개의 현의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` LEFT ($$/수식$${instru} 한 개의 현의 수$$수식$$RIGHT ) ` times ` LEFT ($$/수식$${instru}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {a} ` times ` {b} ` = ` {c} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"


    instru = ["하프", "현악기"][np.random.randint(0, 2)]

    while True:
        a1 = np.random.randint(1, 5)
        a2 = np.random.randint(3, 8)
        b1 = np.random.randint(2, 5)
        b2 = np.random.randint(3, 10)
        if (a1 * b2 >= 10) & (a2 * b2 >= 10):
            break

    a = a1 * 10 + a2
    b = b1 * 10 + b2
    c = a * b


    stem = stem.format(a=a, b=b, instru=instru)
    answer = answer.format(ans=c)
    comment = comment.format(a=a, b=b, c=c, instru=instru)

    return stem, answer, comment




































# 3-2-1-73
def multiplication321_Stem_042():
    stem = "{p}는 {s}을 하루에 $$수식$${a}$$/수식$$쪽씩 읽으려고 합니다. $$수식$${b}$$/수식$$주 동안 읽을 수 있는 {s}은 모두 몇 쪽인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$쪽\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( {b}$$/수식$$주$$수식$$RIGHT ) ` = ` 7 ` times ` {b} ` = ` {c} LEFT ($$/수식$$일$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ( {b}$$/수식$$주 동안 읽을 수 있는 {s}의 쪽수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` LEFT ($$/수식$$하루에 읽을 수 있는 {s}의 쪽수$$수식$$RIGHT ) ` times ` LEFT ($$/수식$$날 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {a} ` times ` {c} ` = ` {d} LEFT ($$/수식$$쪽$$수식$$RIGHT )$$/수식$$\n\n"


    p = ["현수", "채아", "민주", "지호", "연아", "은우", "시우", "혁재", "민하"][np.random.randint(0, 9)]
    s = ["동화책", "소설책", "위인전", "영어책", "과학책"][np.random.randint(0, 5)]

    a1 = np.random.randint(2, 5)
    a2 = np.random.randint(4, 10)
    a = a1 * 10 + a2

    b = np.random.randint(4, 9)
    c = 7 * b
    d = a * c


    stem = stem.format(a=a, b=b, s=s, p=p)
    answer = answer.format(ans=d)
    comment = comment.format(a=a, b=b, c=c, d=d, s=s)

    return stem, answer, comment



































# 3-2-1-76
def multiplication321_Stem_043():
    stem = "합이 $$수식$${a}$$/수식$$인 연속된 두 자연수가 있습니다. 두 수의 곱은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "연속된 두 자연수를 각각 □, □$$수식$$` + ` 1$$/수식$$이라 하면\n" \
              "□$$수식$$` + `$$/수식$$□$$수식$$` + ` 1 ` = ` {a}$$/수식$$, □$$수식$$` + `$$/수식$$□$$수식$$` = ` {b}$$/수식$$이므로 □$$수식$$` = ` {c}$$/수식$$입니다.\n" \
              "따라서 연속된 두 자연수가 $$수식$${c}$$/수식$$, $$수식$${d}$$/수식$$이므로 두 수의 곱은 $$수식$${c} ` times ` {d} ` = ` {e}$$/수식$$입니다.\n\n"


    a1 = np.random.randint(4, 10)

    if a1 % 2 == 0:
        a2 = [1, 7, 9][np.random.randint(0, 3)]

    elif a1 % 2 != 0:
        a2 = [1, 3, 5, 7, 9][np.random.randint(0, 5)]

    a = a1 * 10 + a2
    b = a - 1
    c = int(b / 2)
    d = c + 1
    e = c * d


    stem = stem.format(a=a)
    answer = answer.format(ans=e)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e)

    return stem, answer, comment






































# 3-2-1-77
def multiplication321_Stem_044():
    stem = "{p}는 {s} 문제를 매일 풀었습니다. $$수식$${b}$$/수식$$일 동안은 하루에 $$수식$${a}$$/수식$$개씩 풀었고, $$수식$${d}$$/수식$$일 동안은 하루에 $$수식$${c}$$/수식$$개씩 풀었습니다. {p}가 $$수식$${e}$$/수식$$일 동안 푼 {s} 문제는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${b}$$/수식$$일 동안 푼 {s} 문제 수는 $$수식$${a} ` times ` {b} ` = ` {f} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$입니다.\n" \
              "$$수식$${d}$$/수식$$일 동안 푼 {s} 문제 수는 $$수식$${c} ` times ` {d} ` = ` {g} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$입니다.\n" \
              "따라서 $$수식$${e}$$/수식$$일 동안 푼 {s} 문제 수는 $$수식$${f} ` + ` {g} ` = ` {h} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    p = ["현수", "채아", "민주", "지호", "연아", "은우", "시우", "혁재", "민하"][np.random.randint(0, 9)]
    s = ["수학", "국어", "영어", "사회", "과학"][np.random.randint(0, 5)]

    a1 = np.random.randint(2, 4)
    a2 = np.random.randint(5, 10)
    a = a1 * 10 + a2

    c1 = np.random.randint(2, 4)
    c2 = np.random.randint(0, 6)
    c = c1 * 10 + c2

    b = np.random.randint(13, 20)
    d = np.random.randint(24, 30)

    e = b + d
    f = a * b
    g = c * d
    h = f + g


    stem = stem.format(a=a, b=b, c=c, d=d, e=e, s=s, p=p)
    answer = answer.format(ans=h)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, s=s, p=p)

    return stem, answer, comment





































# 3-2-1-78
def multiplication321_Stem_045():
    stem = "어떤 수에 $$수식$${a}$$/수식$${rur1} 곱해야 할 것을 잘못하여 $$수식$${b}$$/수식$${rur2} 더했더니 $$수식$${c}$$/수식$${ga1} 되었습니다. 바르게 계산한 값과 잘못 계산한 값의 차는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □라 하면\n" \
              "$$수식$$LEFT [$$/수식$$잘못한 계산$$수식$$RIGHT ] `$$/수식$$ □$$수식$$` + ` {b} ` = ` {c}$$/수식$$, □$$수식$$` = ` {c} ` - ` {b}$$/수식$$, □$$수식$$` = ` {d}$$/수식$$\n" \
              "$$수식$$LEFT [$$/수식$$바른 계산$$수식$$RIGHT ] ```` {d} ` times ` {a} ` = ` {e}$$/수식$$\n" \
              "따라서 바른 계산과 잘못 계산한 값의 차는 $$수식$${e} ` - ` {c} ` = ` {f}$$/수식$$입니다.\n\n"


    while True:
        a1 = np.random.randint(1, 3)
        a2 = np.random.randint(5, 10)

        a = a1 * 10 + a2
        b = a2 * 10 + a1

        c = np.random.randint(120, 171)

        if (c - b >= 31) & (c - b <= 98):
            break


    d = c - b
    e = d * a
    f = e - c

    rur1 = get_josa(a, "를")
    rur2 = get_josa(b, "를")
    ga1 = get_josa(c, "가")


    stem = stem.format(a=a, b=b, c=c, rur1=rur1, rur2=rur2, ga1=ga1)
    answer = answer.format(ans=f)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f)

    return stem, answer, comment




































# 3-2-1-79
def multiplication321_Stem_046():
    stem = "□ 안에 들어갈 수 있는 수 중에서 가장 작은 두 자리 수를 구해 보세요.\n$$표$$$$수식$${a} ` times `$$/수식$$□$$수식$$` &gt; ` {b}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a}$$/수식$$을 $$수식$${d}$$/수식$$으로 어림하면 $$수식$${d} ` times ` {e} ` = ` {f}$$/수식$$이므로\n" \
              "□ 안에 들어갈 수는 $$수식$${e}$$/수식$$으로 예상하고 확인합니다.\n" \
              "$$수식$${x}$$/수식$$\n이므로 □ 안에 들어갈 수 있는 수 있는 가장 작은 두 자리 수는\n $$수식$${c}$$/수식$$입니다.\n\n"


    a1 = np.random.randint(4, 9)
    a2 = np.random.randint(2, 5)
    c1 = np.random.randint(2, 6)
    c2 = np.random.randint(8, 10)

    a = a1 * 10 + a2
    c = c1 * 10 + c2

    b = np.random.randint(a * c - 25, a * c - 10)
    # print("b: %d" % b)

    d = a1 * 10
    e = (c1 + 1) * 10
    f = d * e

    n = 0
    x = ""
    # print("ddd")

    while True:
        g = e - n
        h = a * g

        if h > b:
            x = x + "$$수식$$ %d`times`%d`=`%d $$/수식$$\n" % (a, g, h)
            n = n + 1

        elif h < b:
            x = x + "$$수식$$ %d`times`%d`=`%d $$/수식$$\n" % (a, g, h)
            break


    stem = stem.format(a=a, b=b)
    answer = answer.format(ans=c)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f, x=x)

    return stem, answer, comment












