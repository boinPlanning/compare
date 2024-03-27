import numpy as np
import math
from math import gcd





answer_dict = {
    0 : "①",
    1 : "②",
    2 : "③",
    3 : "④",
    4 : "⑤",
    5 : "⑥"
}





answer_kodict={
    0: "ㄱ",
    1: "ㄴ",
    2: "ㄷ",
    3: "ㄹ",
    4: "ㅁ"
}



circle_one = "①"
circle_two = "②"
circle_three = "③"
circle_four = "④"




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









# 3-2-2-유형01-1
def division322_Stem_001():
    stem = "다음을 보고 ㉡은 ㉠의 몇 배인지 구하시오.\n$$수식$$ ` {sa} ` div ` {a} ` = ` $$/수식$$㉠ → $$수식$$ ` {sb} ` div ` {a} ` = ` $$/수식$$㉡\n"
    answer = "(답): $$수식$${a1}$$/수식$$배\n"
    comment = "(해설)\n" \
              "$$수식$$ ` {sa} ` div ` {a} ` = ` {sc} ` $$/수식$$ → $$수식$$ ` {sb} ` div ` {a} ` = ` {sd} ` $$/수식$$이므로 " \
              "㉠$$수식$$` = ` {sc} `$$/수식$$, ㉡$$수식$$` = `{sd} `$$/수식$$입니다.\n" \
              "따라서 ㉡은 ㉠의 $$수식$$` {se} `$$/수식$$배입니다.\n\n"


    while True:
        a = np.random.randint(2, 10)
        sa = np.random.randint(2, 10)

        if sa % a == 0:
            break

    sb = sa * 10
    sc = round(sa / a)
    sd = round(sb / a)
    se = round(sd / sc)

    stem = stem.format(sa=sa, sb=sb, a=a)
    answer = answer.format(a1=se)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, a=a)

    return stem, answer, comment









# 3-2-2-유형01-2
def division322_Stem_002():
    stem = "나눗셈의 몫이 다른 하나를 찾아 기호를 쓰시오.\n$$표$$ ㄱ. $$수식$$` {s1} `$$/수식$$    ㄴ. $$수식$$` {s2} `$$/수식$$    ㄷ. $$수식$$` {s3} `$$/수식$$ $$/표$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "ㄱ. $$수식$$` {c1} `$$/수식$$, ㄴ. $$수식$$` {c2} `$$/수식$$, ㄷ. $$수식$$` {c3} `$$/수식$$\n\n"


    a = [10, 20, 30][np.random.randint(0, 3)]
    b = a

    while True:
        c = [10, 20, 30, 40][np.random.randint(0, 4)]
        if a != c:
            break
    while True:
        sb = np.random.randint(2, 10)
        if a * sb >= 20 & a * sb <= 90:
            sa = a * sb
            break
    while True:
        sd = np.random.randint(2, 10)
        if (sb != sd):
            if b * sd >= 20 & b * sd <= 90:
                sc = b * sd
                if sc != sa:
                    break
    while True:
        sf = np.random.randint(2, 10)
        if (sf != sb) & (sf != sd):
            if c * sf >= 20 & c * sf <= 90:
                se = c * sf
                if se != sa & se != sc:
                    break

    st1 = ["{%d} ` div ` {%d}" % (sa, sb), "` = ` {%d} ``" % (a)]
    st2 = ["{%d} ` div ` {%d}" % (sc, sd), "` = ` {%d} ``" % (b)]
    st3 = ["{%d} ` div ` {%d}" % (se, sf), "` = ` {%d} ``" % (c)]

    candidates = [st1, st2, st3]
    np.random.shuffle(candidates)
    # print(candidates)

    correct_idx = 0

    for idx, sdx in enumerate(candidates):
        if sdx == st3:
            correct_idx = idx
            break

    s1 = candidates[0][0]
    s2 = candidates[1][0]
    s3 = candidates[2][0]
    c1 = candidates[0][0] + candidates[0][1]
    c2 = candidates[1][0] + candidates[1][1]
    c3 = candidates[2][0] + candidates[2][1]

    stem = stem.format(s1=s1, s2=s2, s3=s3)
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(c1=c1, c2=c2, c3=c3)

    return stem, answer, comment










# 3-2-2-유형01-3
def division322_Stem_003():
    stem = "몫이 $$수식$$20$$/수식$$보다 큰 나눗셈을 말한 친구의 이름을 쓰시오.\n$$표$$ $$수식$${s1}$$/수식$$\n$$수식$${s2}$$/수식$$\n$$수식$${s3}$$/수식$$ $$/표$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${c1}$$/수식$$, $$수식$${c2}$$/수식$$, $$수식$${c3}$$/수식$$\n\n"


    while True:
        p1 = ["선재", "지은", "명규", "동호", "혜수", "규민", "준희", "유나", "민준", "시언", "아라", "도윤"][np.random.randint(0, 12)]
        p2 = ["선재", "지은", "명규", "동호", "혜수", "규민", "준희", "유나", "민준", "시언", "아라", "도윤"][np.random.randint(0, 12)]
        p3 = ["선재", "지은", "명규", "동호", "혜수", "규민", "준희", "유나", "민준", "시언", "아라", "도윤"][np.random.randint(0, 12)]
        if (p1 != p2) and (p1 != p3) and (p2 != p3):
            break

    while True:
        a = [30, 40][np.random.randint(0, 2)]
        b = [10, 20][np.random.randint(0, 2)]

        if b == 10:
            c = 20
        else:
            c = 10

        if a == 30:
            sb = [2, 3][np.random.randint(0, 2)]
        else:
            sb = 2

        sa = a * sb

        while True:
            sd = np.random.randint(2, 10)
            if (b * sd >= 20) and (b * sd <= 90):
                sc = b * sd
                if (sa != sc):
                    break

        sf = np.random.randint(2, 10)

        if (sd != sf):
            if (c * sf >= 20) and (c * sf <= 90):
                se = c * sf
                if (sa != se) and (sc != se):
                    break

    st1 = [p1, "{%d} div {%d}" % (sa, sb), "` = ` {%d} ``" % (a)]
    st2 = [p2, "{%d} div {%d}" % (sc, sd), "` = ` {%d} ``" % (b)]
    st3 = [p3, "{%d} div {%d}" % (se, sf), "` = ` {%d} ``" % (c)]


    candidates = [st1, st2, st3]
    np.random.shuffle(candidates)


    s1 = candidates[0][0] + " : " + candidates[0][1]
    s2 = candidates[1][0] + " : " + candidates[1][1]
    s3 = candidates[2][0] + " : " + candidates[2][1]


    c1 = s1 + candidates[0][2]
    c2 = s2 + candidates[1][2]
    c3 = s3 + candidates[2][2]


    stem = stem.format(s1=s1, s2=s2, s3=s3)
    answer = answer.format(a1=st1[0])
    comment = comment.format(c1=c1, c2=c2, c3=c3)


    return stem, answer, comment
















# 3-2-2-유형01-4
def division322_Stem_004():
    stem = "다음 식을 만족하지 않는 ㉠, ㉡으로 짝지어진 것을 고르시오.\n$$표$$$$수식$$` {sa} ` div ` {sb} ` = `$$/수식$$㉠$$수식$$` div `$$/수식$$㉡$$/표$$\n{one} {s1}\n{two} {s2}\n{three} {s3}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$` {sa} ` div ` {sb} ` = ` {a} `$$/수식$$\n" \
              "{one} $$수식$${c1}$$/수식$$\n" \
              "{two} $$수식$${c2}$$/수식$$\n" \
              "{three} $$수식$${c3}$$/수식$$\n\n"


    a = [10, 20][np.random.randint(0, 2)]

    b = a
    c = a

    while True:
        sb = np.random.randint(2, 10)
        if (a * sb >= 20) and (a * sb <= 90):
            sa = a * sb
            # print("sa: " + str(sa))
            break

    while True:
        sd = np.random.randint(2, 10)
        if (b * sd >= 20) and (b * sd <= 90):
            sc = b * sd
            if sc != sa:
                # print("sc: " + str(sc))
                break

    while True:
        sf = np.random.randint(2, 10)
        if (c * sf >= 20) and (c * sf <= 90):
            se = c * sf
            if (se != sa) and (se != sc):
                # print("se: " + str(se))
                break

    while True:
        sh = np.random.randint(2, 10)
        d = [10, 20, 30, 40][np.random.randint(0, 4)]

        if d != a:
            if (d * sh >= 20) and (d * sh <= 90):
                sg = d * sh
                if (sg != sa) and (sg != sc) & (sg != se):
                    # print("sg: " + str(sg))
                    break

    st1 = ["{%d}" % (sc), "{%d}" % (sd), "{%d}" % (b)]
    st2 = ["{%d}" % (se), "{%d}" % (sf), "{%d}" % (c)]
    st3 = ["{%d}" % (sg), "{%d}" % (sh), "{%d}" % (d)]


    candidates = [st1, st2, st3]
    np.random.shuffle(candidates)


    correct_idx = 0

    for idx, sdx in enumerate(candidates):
        if sdx == st3:
            correct_idx = idx
            break

    s1 = "㉠ $$수식$$" + candidates[0][0] + "$$/수식$$, ㉡ $$수식$$" + candidates[0][1] + "$$/수식$$"
    s2 = "㉠ $$수식$$" + candidates[1][0] + "$$/수식$$, ㉡ $$수식$$" + candidates[1][1] + "$$/수식$$"
    s3 = "㉠ $$수식$$" + candidates[2][0] + "$$/수식$$, ㉡ $$수식$$" + candidates[2][1] + "$$/수식$$"

    c1 = "` {%s} ` div ` {%s} ` = ` {%s}" % (candidates[0][0], candidates[0][1], candidates[0][2])
    c2 = "` {%s} ` div ` {%s} ` = ` {%s}" % (candidates[1][0], candidates[1][1], candidates[1][2])
    c3 = "` {%s} ` div ` {%s} ` = ` {%s}" % (candidates[2][0], candidates[2][1], candidates[2][2])

    one = "①"
    two = "②"
    three = "③"

    stem = stem.format(s1=s1, s2=s2, s3=s3, sa=sa, sb=sb, one=one, two=two, three=three)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(c1=c1, c2=c2, c3=c3, sa=sa, sb=sb, a=a, one=one, two=two, three=three)

    return stem, answer, comment










# 3-2-2-유형02-1
def division322_Stem_005():
    stem = "빈칸에 알맞은 수를 구하시오.\n$$수식$$LEFT ( {sb} RIGHT )$$/수식$$ → $$수식$$LEFT ( {s1} RIGHT )$$/수식$$ → $$수식$$LEFT ( {su} RIGHT )$$/수식$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$` {sb} ` div ` {sa} ` = ` {a} `$$/수식$$\n\n"


    while True:
        a = np.random.randint(12, 46)
        sa = [2, 4, 5, 6][np.random.randint(0, 4)]
        sb = 10 * np.random.randint(3, 10)

        if a * sa == sb:
            if a % 10 != 0:
                break

    su = "````````"
    s1 = "{div ` {%d}}" % (sa)

    stem = stem.format(sb=sb, s1=s1, su=su)
    answer = answer.format(a1=a)
    comment = comment.format(sa=sa, sb=sb, a=a)

    return stem, answer, comment














# 3-2-2-유형02-2
def division322_Stem_006():
    stem = "나눗셈의 몫이 $$수식$$`{a}`$$/수식$$인 것을 찾아 기호를 쓰시오.\n$$표$$ ㄱ. $$수식$$`{s1}`$$/수식$$    ㄴ. $$수식$$`{s2}`$$/수식$$ $$/표$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "ㄱ. $$수식$$`{c1}`$$/수식$$, ㄴ. $$수식$$`{c2}`$$/수식$$\n\n"


    while True:
        a = np.random.randint(12, 46)
        sa = [2, 4, 5, 6][np.random.randint(0, 4)]
        sb = 10 * np.random.randint(3, 10)

        if a * sa == sb:
            if a % 10 != 0:
                break

    while True:
        b = np.random.randint(12, 46)
        sc = [2, 4, 5, 6][np.random.randint(0, 4)]
        sd = 10 * np.random.randint(3, 10)

        if a != b:
            if b * sc == sd:
                if b % 10 != 0:
                    break

    st1 = ["{%d} ` div ` {%d}" % (sb, sa), "` = ` {%d} ``" % (a)]
    st2 = ["{%d} ` div ` {%d}" % (sd, sc), "` = ` {%d} ``" % (b)]


    candidates = [st1, st2]
    np.random.shuffle(candidates)

    correct_idx = 0

    for idx, sdx in enumerate(candidates):
        if sdx == st1:
            correct_idx = idx
            break

    s1 = candidates[0][0]
    s2 = candidates[1][0]

    c1 = candidates[0][0] + candidates[0][1]
    c2 = candidates[1][0] + candidates[1][1]

    stem = stem.format(s1=s1, s2=s2, a=a)
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(c1=c1, c2=c2)

    return stem, answer, comment


















# 3-2-2-유형02-3
def division322_Stem_007():
    stem = "나눗셈을 계산하여 몫을 작은 것부터 순서대로 쓰시오.\n$$표$$$$수식$$` {sb} ` div ` {sa} `````````````` {sd} ` div ` {sc} `````````````` {sf} ` div ` {se} `$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${d}$$/수식$$, $$수식$${e}$$/수식$$, $$수식$${f}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$` {sb} ` div ` {sa} ` = ` {a} `$$/수식$$, $$수식$$` {sd} ` div ` {sc} ` = ` {b} `$$/수식$$, $$수식$$` {sf} ` div ` {se} ` = ` {c} `$$/수식$$\n" \
              "따라서 $$수식$${d} ` &lt; ` {e} ` &lt; ` {f} `$$/수식$$이므로 몫을 작은 것부터 순서대로 쓰면 $$수식$${d}$$/수식$$, $$수식$${e}$$/수식$$, $$수식$${f}$$/수식$$입니다.\n\n"


    while True:
        a = np.random.randint(12, 46)
        sa = [2, 4, 5, 6][np.random.randint(0, 4)]
        sb = 10 * np.random.randint(3, 10)

        if a * sa == sb:
            if a % 10 != 0:
                break

    while True:
        b = np.random.randint(12, 46)
        sc = [2, 4, 5, 6][np.random.randint(0, 4)]
        sd = 10 * np.random.randint(3, 10)

        if a != b:
            if b * sc == sd:
                if b % 10 != 0:
                    break

    while True:
        c = np.random.randint(12, 46)
        se = [2, 4, 5, 6][np.random.randint(0, 4)]
        sf = 10 * np.random.randint(3, 10)

        if (c != a) & (c != b):
            if c * se == sf:
                if c % 10 != 0:
                    break

    candidates = sorted([a, b, c])

    d = candidates[0]
    e = candidates[1]
    f = candidates[2]

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf)
    answer = answer.format(d=d, e=e, f=f)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, a=a, b=b, c=c, sf=sf, d=d, e=e, f=f)

    return stem, answer, comment




















# 3-2-2-유형02-4
def division322_Stem_008():
    stem = "가장 큰 수를 가장 작은 수로 나눈 몫을 구하시오.\n$$표$$ $$수식$$`{s1}````{s2}````{s3}````{s4}````{s5}`$$/수식$$ $$/표$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}`&gt;`{sb}`&gt;`{sc}`&gt;`{a}`&gt;`{b}`$$/수식$$이므로\n" \
              "가장 큰 수 : $$수식$${sa}$$/수식$$, 가장 작은 수 : $$수식$${b}$$/수식$$\n" \
              "→ $$수식$${sa}`div`{b}`=`{sd}`$$/수식$$\n\n"


    a = np.random.randint(3, 10)

    while True:
        b = [2, 4, 5, 6][np.random.randint(0, 4)]
        if a > b:
            break

    if b == 2:
        sa = [50, 70, 90][np.random.randint(0, 3)]
    elif b == 4:
        sa = 60
    elif b == 5:
        sa = [60, 70, 80, 90][np.random.randint(0, 4)]
    elif b == 6:
        sa = 90

    while True:
        sb = 10 * np.random.randint(4, 9)
        if sa > sb:
            break

    while True:
        sc = 10 * np.random.randint(3, 8)
        if sb > sc:
            break

    sd = round(sa / b)

    candidates=[sa, sb, sc, a, b]
    np.random.shuffle(candidates)
    s1, s2, s3, s4, s5 = candidates

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, a=a, b=b)

    return stem, answer, comment
    





















# 3-2-2-유형03-1
def division322_Stem_009():
    stem = "{p}는 {s} $$수식$${sa}$$/수식$$장을 가지고 있습니다. 이 {s}를 친구 한 명에게 $$수식$${sb}$$/수식$$장씩 나누어 준다면 몇 명에게 나누어 줄 수 있습니까?\n"
    answer = "(답): $$수식$${a1}$$/수식$$명\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${s}를 나누어 줄 수 있는 친구 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$`LEFT ($$/수식$$전체 {s} 수$$수식$$RIGHT ) `div` LEFT ($$/수식$$한 명에게 나누어 주는 {s} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$`=`{sa}`div`{sb}`=`{sc}` LEFT ($$/수식$$명$$수식$$RIGHT )`$$/수식$$\n\n"


    p = ["예나", "은수", "지호", "현규", "지우"][np.random.randint(0, 5)]
    s = ["도화지", "색도화지", "색종이", "한지", "골판지", "편지지"][np.random.randint(0, 6)]

    a = 10 * np.random.randint(1, 5)
    print(a)

    while True:
        sb = np.random.randint(2, 10)
        if (a*sb >= 20) & (a*sb <= 90):
            break

    sa = a * sb
    sc = round(sa/sb)

    stem = stem.format(p=p, s=s, sa=sa, sb=sb)
    answer = answer.format(a1=sc)
    comment = comment.format(s=s, sa=sa, sb=sb, sc=sc)

    return stem, answer, comment

















# 3-2-2-유형03-2
def division322_Stem_010():
    stem = "길이가 $$수식$${sa}rm {{cm}}$$/수식$$인 {s}{j1} 똑같이 $$수식$${sb}$$/수식$$도막으로 잘랐습니다. 자른 {s} 한 도막의 길이는 몇 $$수식$$rm {{cm}}$$/수식$$입니까?\n"
    answer = "(답): $$수식$${a1}rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$자른 {s} 한 도막의 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$`=`LEFT ($$/수식$$전체 길이$$수식$$RIGHT ) `div` LEFT ($$/수식$$자른 도막 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$`=`{sa}`div`{sb}`=`{sc}`LEFT ( rm {{cm}} RIGHT )`$$/수식$$\n\n"


    s = ["나무 막대", "긴 막대", "수수깡", "색 테이프", "종이테이프", "노끈"][np.random.randint(0, 6)]
    j1 = proc_jo(s, 1)

    while True:
        a = np.random.randint(12, 46)
        if (a % 10) != 0:
            break

    while True:
        sa = 10 * np.random.randint(3, 10)
        sb = [2, 4, 5, 6][np.random.randint(0, 4)]
        if (sa % sb) == 0:
            break

    sc = round(sa/sb)

    stem = stem.format(sa=sa, s=s, j1=j1, sb=sb)
    answer = answer.format(a1=sc)
    comment = comment.format(s=s, sa=sa, sb=sb, sc=sc)

    return stem, answer, comment














# 3-2-2-유형03-3
def division322_Stem_011():
    stem = "{p}이가 문제집 한 쪽을 푸는 데 걸리는 시간은 항상 같습니다. 이 문제집 $$수식$${sa}$$/수식$$쪽을 푸는 데 $$수식$$1$$/수식$$시간 $$수식$${sb}$$/수식$$분이 걸렸다면 한 쪽을 푸는 데 걸린 시간은 몇 분입니까?\n"
    answer = "(답): $$수식$${a1}$$/수식$$분\n"
    comment = "(해설)\n" \
              "$$수식$$1$$/수식$$시간 $$수식$${sb}$$/수식$$분$$수식$$`=`1$$/수식$$시간$$수식$$`+`{sb}`$$/수식$$분$$수식$$`=`60$$/수식$$분$$수식$$`+`{sb}`$$/수식$$분$$수식$$`=`{sc}`$$/수식$$분\n" \
              "$$수식$$LEFT ($$/수식$$한 쪽을 푸는 데 걸린 시간$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$`=`LEFT ( {sa}$$/수식$$쪽을 푸는 데 걸린 시간$$수식$$RIGHT )`div`{sa}$$/수식$$\n" \
              "$$수식$$`=`{sc}`div`{sa}`=`{sd}`LEFT ($$/수식$$분$$수식$$RIGHT )`$$/수식$$\n\n"


    p = ["도윤", "현석", "은혁", "한선", "은영", "나연", "기백", "찬성", "병건", "영훈", "희정", "주원"][np.random.randint(0, 12)]

    sb = 10 * np.random.randint(1, 4)
    sc = 60 + sb

    while True:
        sa = np.random.randint(2, 10)
        if (sc/sa >= 10) and (sc % sa == 0):
            break

    sd = round(sc/sa)

    stem = stem.format(p=p, sa=sa, sb=sb)
    answer = answer.format(a1=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd)

    return stem, answer, comment


















# 3-2-2-유형03-4
def division322_Stem_012():
    stem = "{s}{j1} 한 상자에 $$수식$$10$$/수식$$개씩 $$수식$${sa}$$/수식$$상자가 있습니다. 이 {s}{j2} $$수식$${sb}$$/수식$$명이 똑같이 나누어 먹는다면 한 명이 먹는 {s}{j3} 몇 개입니까?\n"
    answer = "(답): $$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$전체 {s} 수$$수식$$RIGHT )`=`10`times`{sa}`=`{sc}` LEFT ($$/수식$$개$$수식$$RIGHT )`$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$한 명이 먹는 {s} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$`=`LEFT ($$/수식$$전체 {s} 수$$수식$$RIGHT )`div`LEFT ($$/수식$$나누어 먹는 사람 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$`=`{sc}`div`{sb}`=`{sd}`LEFT ($$/수식$$개$$수식$$RIGHT )`$$/수식$$\n\n"


    s = ["호두과자", "초콜릿", "찹쌀떡", "밤과자", "마카롱"][np.random.randint(0, 5)]

    j1 = proc_jo(s, 0)
    j2 = proc_jo(s, 1)
    j3 = proc_jo(s, -1)

    sa = np.random.randint(3, 10)
    sc = 10 * sa

    while True:
        sb = np.random.randint(2, 10)
        if (sc/sb >= 10) & (sc % sb == 0):
            break

    sd = round(sc/sb)

    stem = stem.format(s=s, sa=sa, sb=sb, j1=j1, j2=j2, j3=j3)
    answer = answer.format(a1=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, s=s)

    return stem, answer, comment



















# 3-2-2-유형04-1
def division322_Stem_013():
    stem = "㉠, ㉡, ㉢에 알맞은 수로 짝지어진 것을 고르시오.\n$$표$$$$수식$$`{sa}`div`{sd}`=`$$/수식$$㉠, $$수식$$`{sb}`div`{sd}`=`$$/수식$$㉡이므로 $$수식$$`{sc}`div`{sd}`=`$$/수식$$㉢입니다.$$/표$$\n① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`div`{sd}`=`{a}`$$/수식$$, $$수식$$`{sb}`div`{sd}`=`{b}`$$/수식$$이므로 " \
              "$$수식$$`{sc}`div`{sd}`=`{a}`+`{b}`=`{c}`$$/수식$$입니다.\n\n"


    while True:
        e = np.random.randint(2, 10)
        sa = e * 10
        sb = np.random.randint(2, 10)
        alist = []
        cdlist = []

        for i in range(2, e+1):
            if e % i ==0:
                alist.append(i)
        for i in alist:
            if sb % i == 0:
                cdlist.append(i)
        if len(cdlist) > 0:
            break

    sd = cdlist[np.random.randint(0, len(cdlist))]

    sc = sa + sb
    a = round(sa / sd)
    b = round(sb / sd)
    c = a + b
    d = a - b

    st1 = "%s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$" % ("㉠", a, "㉡", b, "㉢", c)
    st2 = "%s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$" % ("㉠", a, "㉡", b, "㉢", d)
    st3 = "%s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$" % ("㉠", b, "㉡", a, "㉢", c)
    st4 = "%s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$" % ("㉠", b, "㉡", a, "㉢", d)
    st5 = "%s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$, %s $$수식$$%d$$/수식$$" % ("㉠", b, "㉡", b, "㉢", d)

    candidates = [st1, st2, st3, st4, st5]
    np.random.shuffle(candidates)
    [s1, s2, s3, s4, s5] = candidates

    correct_idx = 0

    for idx, sdx in enumerate(candidates):
        if sdx == st1:
            correct_idx = idx
            break

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, a=a, b=b, c=c, d=d)

    return stem, answer, comment
























# 3-2-2-유형04-2
def division322_Stem_014():
    stem = "계산을 하시오.\n$$표$$ $$수식$$`{sa}`div`{sb}`$$/수식$$ $$/표$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sc}`div`{sb}`=`{se}`$$/수식$$, $$수식$$`{sd}`div`{sb}`=`{sf}`$$/수식$$이므로 " \
              "$$수식$$`{sa}`div`{sb}`=`{sg}`$$/수식$$입니다.\n\n"


    while True:
        a = np.random.randint(2, 10)
        b = np.random.randint(2, 10)

        alist = []
        cdlist = []

        for i in range(2, a + 1):
            if a % i == 0:
                alist.append(i)
        for i in alist:
            if b % i == 0:
                cdlist.append(i)
        if len(cdlist) > 0:
            break

    sb = cdlist[np.random.randint(0, len(cdlist))]

    sa = 10 * a + b
    sc = 10 * a
    sd = b

    se = round(sc/sb)
    sf = round(sd/sb)
    sg = round(sa/sb)

    stem = stem.format(sa=sa, sb=sb)
    answer = answer.format(a1=sg)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg)

    return stem, answer, comment























# 3-2-2-유형04-3
def division322_Stem_015():
    stem = "다음 중 몫이 가장 큰 것을 고르시오.\n① $$수식$${s1}$$/수식$$\n② $$수식$${s2}$$/수식$$\n③ $$수식$${s3}$$/수식$$\n④ $$수식$${s4}$$/수식$$\n⑤ $$수식$${s5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "① $$수식$${c1}$$/수식$$\n" \
              "② $$수식$${c2}$$/수식$$\n" \
              "③ $$수식$${c3}$$/수식$$\n" \
              "④ $$수식$${c4}$$/수식$$\n" \
              "⑤ $$수식$${c5}$$/수식$$\n\n"


    def stem_03():
        while True:
            ta = np.random.randint(2, 10)
            tb = np.random.randint(2, 10)
            taa = ta * 10 + tb
            alist = []

            for idxa in range(2, ta+1):
                if ta % idxa == 0:
                    alist.append(idxa)

            blist=[]

            for idxb in range(2,tb+1):
                if tb % idxb == 0:
                    blist.append(idxb)

            common_list=[]

            for idxcommon in alist:
                if (blist.count(idxcommon)) > 0:
                    common_list.append(idxcommon)

            if len(common_list) > 0:
                tbblist = np.random.choice(common_list,1,replace=False)
                tbb = tbblist[0]
                if (ta/tbb) <= 3:
                    tkk = round(taa/tbb)
                    return ta, tb, taa, tbb, tkk

    while True:
        a, b, sa, sb, sk = stem_03()
        c, d, sc, sd, sl = stem_03()
        e, f, se, sf, sm = stem_03()
        g, h, sg, sh, sn = stem_03()
        i, j, si, sj, so = stem_03()

        if (sa != sc):
            if (sa != se) & (sc != se):
                if (sa != sg) & (sc != sg) & (se != sg):
                    if (sa != si) & (sc != si) & (se != si) & (sg != si):
                        if (sk > sl) & (sk > sm) & (sk > sn) & (sk > so):
                            break

    st1 = ["{%d}`div`{%d}" % (sa, sb), sk]
    st2 = ["{%d}`div`{%d}" % (sc, sd), sl]
    st3 = ["{%d}`div`{%d}" % (se, sf), sm]
    st4 = ["{%d}`div`{%d}" % (sg, sh), sn]
    st5 = ["{%d}`div`{%d}" % (si, sj), so]

    candidates = [st1, st2, st3, st4, st5]
    np.random.shuffle(candidates)

    correct_idx = 0

    for idx, sdx in enumerate(candidates):
        if sdx == st1:
            correct_idx = idx
            break

    s1 = candidates[0][0]
    s2 = candidates[1][0]
    s3 = candidates[2][0]
    s4 = candidates[3][0]
    s5 = candidates[4][0]

    c1 = s1 + "`=`{%d}`" % (candidates[0][1])
    c2 = s2 + "`=`{%d}`" % (candidates[1][1])
    c3 = s3 + "`=`{%d}`" % (candidates[2][1])
    c4 = s4 + "`=`{%d}`" % (candidates[3][1])
    c5 = s5 + "`=`{%d}`" % (candidates[4][1])

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)

    return stem, answer, comment



























# 3-2-2-유형04-4
def division322_Stem_016():
    stem = "두 나눗셈의 몫의 합을 구하시오.\n$$표$$ $$수식$$`{sa}`div`{sb}`````````````{sc}`div`{sd}$$/수식$$ $$/표$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`div`{sb}`=`{se}`$$/수식$$, $$수식$$`{sc}`div`{sd}`=`{sf}`$$/수식$$이므로 몫의 합은 $$수식$$`{se}`+`{sf}`=`{sg}`$$/수식$$입니다.\n\n"


    while True:
        a = np.random.randint(2, 10)
        b = np.random.randint(2, 10)
        sa = 10 * a + b

        alist = []
        cdlist = []

        for i in range(2, a + 1):
            if a % i == 0:
                alist.append(i)
        for i in alist:
            if b % i == 0:
                cdlist.append(i)
        if len(cdlist) > 0:
            sb = cdlist[np.random.randint(0, len(cdlist))]
            break

    while True:
        c = np.random.randint(2, 10)
        d = np.random.randint(2, 10)
        sc = 10 * c + d

        clist = []
        cdlist = []

        for i in range(2, c + 1):
            if c % i == 0:
                clist.append(i)
        for i in clist:
            if d % i == 0:
                cdlist.append(i)
        if len(cdlist) > 0:
            sd = cdlist[np.random.randint(0, len(cdlist))]
            if (sc != sa) and (sd != sb):
                break

    se = round(sa/sb)
    sf = round(sc/sd)
    sg = se + sf

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(a1=sg)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, sg=sg)

    return stem, answer, comment














    
# 3-2-2-유형05-1
def division322_Stem_017():
    stem = "□ 안에 알맞은 수를 구하시오.\n$$수식$${saa} `Times`$$/수식$$□$$수식$$`=` {sbb}$$/수식$$\n"
    answer = "(답): $$수식$${scc}$$/수식$$\n"
    comment = "(해설)\n" \
              "곱셈과 나눗셈의 관계를 이용합니다.\n" \
              "$$수식$${saa} `Times`$$/수식$$□$$수식$$`=` {sbb}$$/수식$$ → $$수식$${sbb} `Div` {saa} `=`$$/수식$$□, □$$수식$$`=` {scc}$$/수식$$\n\n"


    while True:
        sa = np.random.randint(2, 10)
        sb = np.random.randint(2, 10)
        tempa = []

        for idxa in range(2, sa+1):
            if sa % idxa == 0:
                tempa.append(idxa) # tempa 리스트에 sa 변수의 약수들을 모음

        tempb = []
        for idxb in range(2,sb+1):
            if sb % idxb == 0:
                tempb.append(idxb) # tempb 리스트에 sb 변수의 약수들을 모음

        tempcommon = []
        for idxcommon in tempa:
            if tempb.count(idxcommon)>0:
                tempcommon.append(idxcommon) # 두 리스트를 비교하여 공통되는 약수들만 따로 모음

        if len(tempcommon) > 0: # 1을 제외하고 공통되는 약수가 있다면 진행
            saalist = np.random.choice(tempcommon, 1, replace=False) # 1을 제외하고 공통되는 약수 중에 하나만 뽑기 (리스트 형태)
            saa = saalist[0]
            break


    sbb = (sa * 10) + sb
    scc = int(sbb / saa)


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(scc=scc)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc)


    return stem, answer, comment


























# 3-2-2-유형05-2
def division322_Stem_018():
    stem = "□ 안에 알맞은 수를 구하시오.\n□$$수식$$`Times` {saa} `=` {sbb}$$/수식$$\n"
    answer = "(답): $$수식$${scc}$$/수식$$\n"
    comment = "(해설)\n" \
              "곱셈과 나눗셈의 관계를 이용합니다.\n" \
              "□$$수식$$`Times` {saa} `=` {sbb}$$/수식$$ → $$수식$${sbb} `Div` {saa} `=`$$/수식$$□, □$$수식$$`=` {scc}$$/수식$$\n\n"


    while True:
        sa = np.random.randint(2, 10)
        sb = np.random.randint(2, 10)
        tempa = []

        for idxa in range(2, sa+1):
            if sa % idxa == 0:
                tempa.append(idxa) # tempa 리스트에 sa 변수의 약수들을 모음

        tempb = []
        for idxb in range(2, sb+1):
            if sb % idxb == 0:
                tempb.append(idxb) # tempb 리스트에 sb 변수의 약수들을 모음

        tempcommon = []
        for idxcommon in tempa:
            if tempb.count(idxcommon) > 0:
                tempcommon.append(idxcommon) # 두 리스트를 비교하여 공통되는 약수들만 따로 모음

        if len(tempcommon) > 0: # 1을 제외하고 공통되는 약수가 있다면 진행
            saalist = np.random.choice(tempcommon, 1, replace=False) # 1을 제외하고 공통되는 약수 중에 하나만 뽑기 (리스트 형태)
            saa = saalist[0]
            break


    sbb = (sa * 10) + sb
    scc = int(sbb / saa)

    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(scc=scc)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc)

    return stem, answer, comment























# 3-2-2-유형05-3
def division322_Stem_019():
    stem = "{p1}이와 {p2}이가 만든 식의 계산 결과가 같을 때 □ 안에 알맞은 수를 구하시오.\n$$표$${p1} : $$수식$${saa} `Div` {sbb}$$/수식$$\n{p2} : $$수식$${scc} `Times`$$/수식$$□$$/표$$\n"
    answer = "(답): $$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} `Div` {sbb} `=` {sdd}$$/수식$$이고 두 식의 계산 결과가 같으므로\n" \
              "$$수식$${scc} `Times`$$/수식$$□$$수식$$`=` {sdd}$$/수식$$ → $$수식$${sdd} `Div` {scc} `=`$$/수식$$□, □$$수식$$`=` {see}$$/수식$$입니다.\n\n"


    while True:
        p1 = ['서준', '우진', '명훈', '은정', '하은', '진명', '희원', "도철", "호창", "우성", "태섭", "소율"][np.random.randint(0, 12)]
        p2 = ['서준', '우진', '명훈', '은정', '하은', '진명', '희원', "도철", "호창", "우성", "태섭", "소율"][np.random.randint(0, 12)]
        if p1 != p2:
            break

    while True:

        scc = 1

        while True:
            sa = np.random.randint(2, 10)
            sb = np.random.randint(2, 10)
            tempa=[]
            for idxa in range(2,sa+1):
                if sa%idxa==0:
                    tempa.append(idxa) # tempa 리스트에 sa 변수의 약수들을 모음

            tempb=[]
            for idxb in range(2,sb+1):
                if sb%idxb==0:
                    tempb.append(idxb) # tempb 리스트에 sb 변수의 약수들을 모음

            tempcommon=[]
            for idxcommon in tempa:
                if tempb.count(idxcommon)>0:
                    tempcommon.append(idxcommon) # 두 리스트를 비교하여 공통되는 약수들만 따로 모음

            if len(tempcommon)>0: # 1을 제외하고 공통되는 약수가 있다면 진행
                sbblist=np.random.choice(tempcommon,1,replace=False) # 1을 제외하고 공통되는 약수 중에 하나만 뽑기 (리스트 형태)
                sbb=sbblist[0]
                break


        saa = sa * 10 + sb

        while True:
            sc = np.random.randint(2, 10)
            sd = np.random.randint(2, 10)
            tempc = []
            for idxc in range(2, sc+1):
                if sc % idxc == 0:
                    tempc.append(idxc) # tempc 리스트에 sc 변수의 약수들을 모음

            tempd = []
            for idxd in range(2, sd+1):
                if sd % idxd == 0:
                    tempd.append(idxd) # tempd 리스트에 sd 변수의 약수들을 모음

            tempcommon2 = []
            for idxcommon2 in tempc:
                if tempd.count(idxcommon2) > 0:
                    tempcommon2.append(idxcommon2) # 두 리스트를 비교하여 공통되는 약수들만 따로 모음

            if len(tempcommon2) > 0: # 1을 제외하고 공통되는 약수가 있다면 진행
                scclist = np.random.choice(tempcommon2, 1, replace=False) # 1을 제외하고 공통되는 약수 중에 하나만 뽑기 (리스트 형태)
                scc = scclist[0]
            break


        sdd = sc * 10 + sd


        if sdd == (saa / sbb) and ((saa / sbb) % scc == 0) and scc != 1:
            break


    see = int(sdd / scc)


    stem = stem.format(p1=p1, p2=p2, saa=saa, sbb=sbb, scc=scc)
    answer = answer.format(see=see)
    comment = comment.format(saa=saa, sbb=sbb, sdd=sdd, scc=scc, see=see)

    return stem, answer, comment





















# 3-2-2-유형05-4
def division322_Stem_020():
    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 자연수 중에서 □ 안에 들어갈 수 있는 수는 모두 몇 개인가요?\n$$수식$${scc} `Times`$$/수식$$□ $$수식$$&lt; {saa} `Div` {sbb}$$/수식$$\n"
    answer = "(답): $$수식$${sff}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${saa} `Div` {sbb} `=` {sdd}$$/수식$$이므로 $$수식$${scc} `Times`$$/수식$$□$$수식$$`=` {sdd}$$/수식$$라고 하면 " \
              "$$수식$${sdd} `Div` {scc} `=`$$/수식$$□, □$$수식$$`=` {see}$$/수식$$입니다.\n" \
              "$$수식$${scc} `Times`$$/수식$$□ $$수식$$&lt; {sdd}$$/수식$$이므로 □ 안에는 $$수식$${see}$$/수식$$보다 작은 수가 들어가야 합니다.\n" \
              "따라서 □ 안에 들어갈 수 있는 수는 모두 $$수식$${sff}$$/수식$$개입니다.\n\n"


    while True:
        while True:
            sa = np.random.randint(2, 10)
            sb = np.random.randint(2, 10)
            sn = np.random.randint(3, 10)

            tempa = []

            for idxa in range(2, sa + 1):
                if sa % idxa == 0:
                    tempa.append(idxa) # tempa 리스트에 sa 변수의 약수들을 모음

            tempb = []

            for idxb in range(2, sb + 1):
                if sb % idxb == 0:
                    tempb.append(idxb) # tempb 리스트에 sb 변수의 약수들을 모음

            tempcommon = []

            for idxcommon in tempa:
                if tempb.count(idxcommon) > 0:
                    tempcommon.append(idxcommon) # 두 리스트를 비교하여 공통되는 약수들만 따로 모음

            if len(tempcommon) > 0: # 1을 제외하고 공통되는 약수가 있다면 진행
                sbblist = np.random.choice(tempcommon, 1, replace=False) # 1을 제외하고 공통되는 약수 중에 하나만 뽑기 (리스트 형태)
                sbb = sbblist[0]
                break

        saa=sa*10+sb
        sdd=int(saa/sbb)
        scc=np.random.randint(2,10)
        if (sdd/scc)==sn:
            break

    see=int(sdd/scc)
    sff=see-1

    stem=stem.format(scc=scc,saa=saa,sbb=sbb)
    answer=answer.format(sff=sff)
    comment=comment.format(saa=saa,sbb=sbb,sdd=sdd,scc=scc,see=see,sff=sff)

    return stem,answer,comment




















# 3-2-2-유형06-1
def division322_Stem_021():
    stem = "계산을 하시오.\n$$표$$$$수식$${saa} `Div` {sbb}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${scc}$$/수식$$\n"
    comment = "(해설)\n" \
            "$$수식$${saa} `Div` {sbb} `=` {scc}$$/수식$$입니다.\n\n"


    while True:
        sa=np.random.randint(3,10)
        sb=np.random.randint(1,10)
        saa=sa*10+sb

        tempa=[]

        for idxa in range(1,sa+1):
            if sa%idxa==0:
                tempa.append(idxa) # tempa 리스트에 sa 변수의 약수들을 모음

        tempaa=[]

        for idxaa in range(1,saa+1):
            if saa%idxaa==0:
                tempaa.append(idxaa) # tempaa 리스트에 saa 변수의 약수들을 모음

        sbblist=np.random.choice(tempaa,1,replace=False) # saa 변수의 약수 중에 하나만 뽑기 (리스트 형태)
        sbb=sbblist[0]

        if (tempa.count(sbb)==0)and(2<=sbb)and(sbb<sa):
            break

    scc=int(saa/sbb)

    stem=stem.format(saa=saa,sbb=sbb)
    answer=answer.format(scc=scc)
    comment=comment.format(saa=saa,sbb=sbb,scc=scc)

    return stem,answer,comment





















# 3-2-2-유형06-2
def division322_Stem_022():
    stem = "몫이 더 작은 식을 찾아 기호를 쓰시오.\n$$표$$ㄱ. $$수식$${saa} `Div` {sbb}$$/수식$$      ㄴ.$$수식$${scc} `Div` {sdd}$$/수식$$$$/표$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "ㄱ. $$수식$${saa} `Div` {sbb} `=` {see}$$/수식$$, ㄴ. $$수식$${scc} `Div` {sdd} `=` {sff}$$/수식$$\n\n"


    while True:
        sa=np.random.randint(3,10)
        sc=np.random.randint(3,10)
        sb=np.random.randint(1,10)
        sd=np.random.randint(1,10)

        saa=sa*10+sb
        scc=sc*10+sd
        tempa=[]

        for idxa in range(1, sa + 1):
            if sa % idxa == 0:
                tempa.append(idxa)  # tempa 리스트에 sa 변수의 약수들을 모음

        tempaa = []
        for idxaa in range(1, saa + 1):
            if saa % idxaa == 0:
                tempaa.append(idxaa)  # tempaa 리스트에 saa 변수의 약수들을 모음

        sbblist = np.random.choice(tempaa, 1, replace=False)  # saa 변수의 약수 중에 하나만 뽑기 (리스트 형태)
        sbb = sbblist[0]
        tempc=[]

        for idxc in range(1,sc+1):
            if sc%idxc==0:
                tempc.append(idxc) # tempc 리스트에 sc 변수의 약수들을 모음

        tempcc=[]
        for idxcc in range(1,scc+1):
            if scc%idxcc==0:
                tempcc.append(idxcc) # tempcc 리스트에 scc 변수의 약수들을 모음

        sddlist=np.random.choice(tempcc,1,replace=False) # scc 변수의 약수 중에 하나만 뽑기 (리스트 형태)
        sdd=sddlist[0]

        see=int(saa/sbb)
        sff=int(scc/sdd)

        if (tempa.count(sbb) == 0) and (2 <= sbb) and (sbb < sa)and(tempc.count(sdd) == 0) and (2 <= sdd) and (sdd < sc)and(sbb!=sdd)and(see!=sff)and((see-5)<=sff)and(sff<=(see+5)):
            break

    if see<sff:
        a1="ㄱ"
    elif see>sff:
        a1="ㄴ"

    stem=stem.format(saa=saa,sbb=sbb,scc=scc,sdd=sdd)
    answer=answer.format(a1=a1)
    comment=comment.format(saa=saa,sbb=sbb,see=see,scc=scc,sdd=sdd,sff=sff)

    return stem,answer,comment























# 3-2-2-유형06-3
def division322_Stem_023():
    stem = "두 나눗셈의 몫의 차를 구하시오.\n$$표$$$$수식$${saa} `Div` {sbb}````````````````````````{scc} `Div` {sdd}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${sii}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${saa} `Div` {sbb} `=` {see}$$/수식$$, $$수식$${scc} `Div` {sdd} `=` {sff}$$/수식$$\n" \
              "→ $$수식$$LEFT ($$/수식$$두 나눗셈의 몫의 차$$수식$$RIGHT ) `=` {sgg} `-` {shh} `=` {sii}$$/수식$$\n\n"


    while True:
        sa=np.random.randint(3,10)
        sc=np.random.randint(3,10)
        sb=np.random.randint(1,10)
        sd=np.random.randint(1,10)

        saa=sa*10+sb
        scc=sc*10+sd

        tempa=[]

        for idxa in range(1, sa + 1):
            if sa % idxa == 0:
                tempa.append(idxa)  # tempa 리스트에 sa 변수의 약수들을 모음

        tempaa = []
        for idxaa in range(1, saa + 1):
            if saa % idxaa == 0:
                tempaa.append(idxaa)  # tempaa 리스트에 saa 변수의 약수들을 모음

        sbblist = np.random.choice(tempaa, 1, replace=False)  # saa 변수의 약수 중에 하나만 뽑기 (리스트 형태)
        sbb = sbblist[0]
        tempc=[]
        for idxc in range(1,sc+1):
            if sc%idxc==0:
                tempc.append(idxc) # tempc 리스트에 sc 변수의 약수들을 모음

        tempcc=[]
        for idxcc in range(1,scc+1):
            if scc%idxcc==0:
                tempcc.append(idxcc) # tempcc 리스트에 scc 변수의 약수들을 모음

        sddlist=np.random.choice(tempcc,1,replace=False) # scc 변수의 약수 중에 하나만 뽑기 (리스트 형태)
        sdd=sddlist[0]
        see=int(saa/sbb)
        sff=int(scc/sdd)

        if (sa!=sc)and(tempa.count(sbb) == 0) and (2 <= sbb) and (sbb < sa)and(tempc.count(sdd) == 0) and (2 <= sdd) and (sdd < sc)and(sbb!=sdd)and(see!=sff):
            break

    sgg=max(see,sff)
    shh=min(see,sff)
    sii=sgg-shh

    stem=stem.format(saa=saa,sbb=sbb,scc=scc,sdd=sdd)
    answer=answer.format(sii=sii)
    comment=comment.format(saa=saa,sbb=sbb,see=see,scc=scc,sdd=sdd,sff=sff,sgg=sgg,shh=shh,sii=sii)

    return stem,answer,comment

























# 3-2-2-유형06-4
def division322_Stem_024():
    stem = "다음 중 큰 수를 작은 수로 나눈 몫이 $$수식$${skk}$$/수식$$인 것을 고르시오.\n① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
            "① {z1}\n" \
            "② {z2}\n" \
            "③ {z3}\n" \
            "④ {z4}\n" \
            "⑤ {z5}\n\n"


    while True:
        while True:
            sa=np.random.randint(3,10)
            sb = np.random.randint(1, 10)

            saa=sa*10+sb

            tempa=[]

            for idxa in range(1, sa + 1):
                if sa % idxa == 0:
                    tempa.append(idxa)  # tempa 리스트에 sa 변수의 약수들을 모음

            tempaa = []

            for idxaa in range(1, saa + 1):
                if saa % idxaa == 0:
                    tempaa.append(idxaa)  # tempaa 리스트에 saa 변수의 약수들을 모음

            sbblist = np.random.choice(tempaa, 1, replace=False)  # saa 변수의 약수 중에 하나만 뽑기 (리스트 형태)

            sbb = sbblist[0]

            if (tempa.count(sbb)==0)and(2<=sbb)and(sbb<=sa):
                break

        while True:
            sc = np.random.randint(3, 10)
            sd = np.random.randint(1, 10)

            scc=sc*10+sd
            tempc = []

            for idxc in range(1, sc + 1):
                if sc % idxc == 0:
                    tempc.append(idxc)  # tempc 리스트에 sc 변수의 약수들을 모음

            tempcc = []

            for idxcc in range(1, scc + 1):
                if scc % idxcc == 0:
                    tempcc.append(idxcc)  # tempcc 리스트에 scc 변수의 약수들을 모음

            sddlist = np.random.choice(tempcc, 1, replace=False)  # scc 변수의 약수 중에 하나만 뽑기 (리스트 형태)
            sdd = sddlist[0]

            if (tempc.count(sdd)==0)and(2<=sdd)and(sdd<sc):
                break

        while True:
            se = np.random.randint(3, 10)
            sf = np.random.randint(1, 10)

            see = se * 10 + sf
            tempe = []

            for idxe in range(1, se + 1):
                if se % idxe == 0:
                    tempe.append(idxe)  # tempe 리스트에 se 변수의 약수들을 모음

            tempee = []
            for idxee in range(1, see + 1):
                if see % idxee == 0:
                    tempee.append(idxee)  # tempee 리스트에 see 변수의 약수들을 모음

            sfflist = np.random.choice(tempee, 1, replace=False)  # see 변수의 약수 중에 하나만 뽑기 (리스트 형태)
            sff = sfflist[0]

            if (tempe.count(sff)==0)and(2<=sff)and(sff<se):
                break

        while True:
            sg=np.random.randint(3,10)
            sh = np.random.randint(1, 10)

            sgg=sg*10+sh
            tempg = []

            for idxg in range(1, sg + 1):
                if sg % idxg == 0:
                    tempg.append(idxg)  # tempg 리스트에 sg 변수의 약수들을 모음

            tempgg = []
            for idxgg in range(1, sgg + 1):
                if sgg % idxgg == 0:
                    tempgg.append(idxgg)  # tempgg 리스트에 sgg 변수의 약수들을 모음

            shhlist = np.random.choice(tempgg, 1, replace=False)  # sgg 변수의 약수 중에 하나만 뽑기 (리스트 형태)
            shh = shhlist[0]

            if (tempg.count(shh)==0)and(2<=shh)and(shh<sg):
                break

        while True:
            si=np.random.randint(3,10)
            sj=np.random.randint(1,10)

            sii=si*10+sj
            tempi = []

            for idxi in range(1, si + 1):
                if si % idxi == 0:
                    tempi.append(idxi)  # tempi 리스트에 si 변수의 약수들을 모음

            tempii = []
            for idxii in range(1, sii + 1):
                if sii % idxii == 0:
                    tempii.append(idxii)  # tempii 리스트에 sii 변수의 약수들을 모음

            sjjlist = np.random.choice(tempii, 1, replace=False)  # sgg 변수의 약수 중에 하나만 뽑기 (리스트 형태)
            sjj = sjjlist[0]

            if (tempi.count(sjj)==0)and(2<=sjj)and(sjj<si):
                break

        skk=int(saa/sbb)
        sll=int(scc/sdd)
        smm=int(see/sff)
        snn=int(sgg/shh)
        soo=int(sii/sjj)

        if (skk!=sll)and(skk!=smm)and(skk!=snn)and(skk!=soo)and(sll!=smm)and(sll!=snn)and(sll!=soo)and(smm!=snn)and(smm!=soo)and(snn!=soo):
            break

    y1=["$$수식$$%s$$/수식$$, $$수식$$%s$$/수식$$"%(saa,sbb),"$$수식$$%s `Div` %s `=` %s$$/수식$$"%(saa,sbb,skk)]
    y2=["$$수식$$%s$$/수식$$, $$수식$$%s$$/수식$$"%(scc,sdd),"$$수식$$%s `Div` %s `=` %s$$/수식$$"%(scc,sdd,sll)]
    y3=["$$수식$$%s$$/수식$$, $$수식$$%s$$/수식$$"%(see,sff),"$$수식$$%s `Div` %s `=` %s$$/수식$$"%(see,sff,smm)]
    y4=["$$수식$$%s$$/수식$$, $$수식$$%s$$/수식$$"%(sgg,shh),"$$수식$$%s `Div` %s `=` %s$$/수식$$"%(sgg,shh,snn)]
    y5=["$$수식$$%s$$/수식$$, $$수식$$%s$$/수식$$"%(sii,sjj),"$$수식$$%s `Div` %s `=` %s$$/수식$$"%(sii,sjj,soo)]

    candidates=[y1,y2,y3,y4,y5]
    np.random.shuffle(candidates)
    [[x1,z1],[x2,z2],[x3,z3],[x4,z4],[x5,z5]]=candidates

    correct_idx=0
    for idx,sdx in enumerate(candidates):
        if sdx==y1:
            correct_idx=idx
            break

    stem=stem.format(skk=skk,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a1=answer_dict[correct_idx])
    comment=comment.format(z1=z1,z2=z2,z3=z3,z4=z4,z5=z5)

    return stem,answer,comment






















# 3-2-2-유형07-1
def division322_Stem_025():
    stem = "{sss} $$수식$${saa}$$/수식$$장을 $$수식$${sbb}$$/수식$$명이 똑같이 나누어 가지려고 합니다. 한 명이 {sss}를 몇 장씩 가질 수 있습니까?\n"
    answer = "(답): $$수식$${scc}$$/수식$$장\n"
    comment = "(해설)\n" \
            "$$수식$$LEFT ($$/수식$$한 명이 가질 수 있는 {sss} 수$$수식$$RIGHT )$$/수식$$\n" \
            "$$수식$$= LEFT ($$/수식$$전체 {sss} 수 $$수식$$RIGHT ) `Div` LEFT ($$/수식$$나누어 가지는 {sss} 수$$수식$$RIGHT )$$/수식$$\n" \
            "$$수식$$= {saa} `Div` {sbb} `=` {scc} LEFT ($$/수식$$장$$수식$$RIGHT )$$/수식$$\n\n"


    sss=["붙임딱지","색종이","도화지","딱지","한지"][np.random.randint(0,5)]

    while True:
        sa=np.random.randint(2,10)
        sb=np.random.randint(2,10)

        saa=sa*10+sb
        tempa=[]
        for idxa in range(2,sa+1):
            if sa%idxa==0:
                tempa.append(idxa) # tempa 리스트에 sa 변수의 약수들을 모음

        tempb=[]
        for idxb in range(2,sb+1):
            if sb%idxb==0:
                tempb.append(idxb) # tempb 리스트에 sb 변수의 약수들을 모음

        tempcommon=[]

        for idxcommon in tempa:
            if tempb.count(idxcommon)>0:
                tempcommon.append(idxcommon) # 두 리스트를 비교하여 공통되는 약수들만 따로 모음

        if len(tempcommon)>0: # 1을 제외하고 공통되는 약수가 있다면 진행
            sbblist=np.random.choice(tempcommon,1,replace=False) # 1을 제외하고 공통되는 약수 중에 하나만 뽑기 (리스트 형태)
            sbb=sbblist[0]
            break

    scc=int(saa/sbb)

    stem=stem.format(sss=sss,saa=saa,sbb=sbb)
    answer=answer.format(scc=scc)
    comment=comment.format(sss=sss,saa=saa,sbb=sbb,scc=scc)

    return stem,answer,comment




















# 3-2-2-유형07-2
def division322_Stem_026():
    stem = "{sss} $$수식$${saa}$$/수식$$개를 한 명에게 $$수식$${sbb}$$/수식$$개씩 나누어 주려고 합니다. {sss}{j1} 몇 명에게 나누어 줄 수 있습니까?\n"
    answer = "(답): $$수식$${scc}$$/수식$$명\n"
    comment = "(해설)\n" \
            "$$수식$$LEFT ($$/수식$${sss}{j1} 나누어 줄 수 있는 사람 수$$수식$$RIGHT )$$/수식$$\n" \
            "$$수식$$= LEFT ($$/수식$$전체 {sss} 수$$수식$$RIGHT ) `Div` LEFT ($$/수식$$한 명에게 나누어 주는 {sss} 수$$수식$$RIGHT )$$/수식$$\n" \
            "$$수식$$= {saa} `Div` {sbb} `=` {scc} LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$\n\n"


    sss=["빵","사탕","초콜릿","사과","귤","방울토마토"][np.random.randint(0,6)]
    j1=proc_jo(sss,1)

    while True:
        sa=np.random.randint(2,10)
        sb=np.random.randint(2,10)
        saa=sa*10+sb
        tempa=[]
        for idxa in range(2,sa+1):
            if sa%idxa==0:
                tempa.append(idxa) # tempa 리스트에 sa 변수의 약수들을 모음
        tempb=[]
        for idxb in range(2,sb+1):
            if sb%idxb==0:
                tempb.append(idxb) # tempb 리스트에 sb 변수의 약수들을 모음
        tempcommon=[]
        for idxcommon in tempa:
            if tempb.count(idxcommon)>0:
                tempcommon.append(idxcommon) # 두 리스트를 비교하여 공통되는 약수들만 따로 모음
        if len(tempcommon)>0: # 1을 제외하고 공통되는 약수가 있다면 진행
            sbblist=np.random.choice(tempcommon,1,replace=False) # 1을 제외하고 공통되는 약수 중에 하나만 뽑기 (리스트 형태)
            sbb=sbblist[0]
            break

    scc=int(saa/sbb)

    stem=stem.format(sss=sss,saa=saa,sbb=sbb,j1=j1)
    answer=answer.format(scc=scc)
    comment=comment.format(sss=sss,j1=j1,saa=saa,sbb=sbb,scc=scc)

    return stem,answer,comment

























# 3-2-2-유형07-3
def division322_Stem_027():
    stem = "어느 꽃 가게에서 {sss} $$수식$${saa}$$/수식$$송이를 $$수식$${sbb}$$/수식$$송이씩 묶어서 팔려고 합니다. {sss}{j1} 모두 몇 묶음 팔 수 있습니까?\n"
    answer = "(답): $$수식$${scc}$$/수식$$묶음\n"
    comment = "(해설)\n" \
            "$$수식$$LEFT ($$/수식$${sss}{j1} 팔 수 있는 묶음 수$$수식$$RIGHT )$$/수식$$\n" \
            "$$수식$$= LEFT ($$/수식$$전체 {sss} 수$$수식$$RIGHT ) `Div` LEFT ($$/수식$$한 묶음의 {sss} 수$$수식$$RIGHT )$$/수식$$\n" \
            "$$수식$$= {saa} `Div` {sbb} `=` {scc} LEFT ($$/수식$$묶음$$수식$$RIGHT )$$/수식$$\n\n"


    sss=["장미","국화","백합","튤립","카네이션"][np.random.randint(0,5)]
    j1=proc_jo(sss,1)

    while True:
        sa=np.random.randint(3,10)
        sb=np.random.randint(1,10)
        saa=sa*10+sb
        tempa=[]
        for idxa in range(1,sa+1):
            if sa%idxa==0:
                tempa.append(idxa) # tempa 리스트에 sa 변수의 약수들을 모음

        tempaa=[]
        for idxaa in range(1,saa+1):
            if saa%idxaa==0:
                tempaa.append(idxaa) # tempaa 리스트에 saa 변수의 약수들을 모음

        sbblist=np.random.choice(tempaa,1,replace=False)
        sbb=sbblist[0]
        if (tempa.count(sbb)==0)and(2<=sbb)and(sbb<sa):
            break

    scc=int(saa/sbb)

    stem=stem.format(sss=sss,saa=saa,sbb=sbb,j1=j1)
    answer=answer.format(scc=scc)
    comment=comment.format(sss=sss,j1=j1,saa=saa,sbb=sbb,scc=scc)

    return stem,answer,comment


























# 3-2-2-유형07-4
def division322_Stem_028():
    stem = "{s1} $$수식$${saa}$$/수식$$권과 {s2} $$수식$${sbb}$$/수식$$권이 있습니다. 이 책을 종류에 상관없이 $$수식$${scc}$$/수식$$단 책장에 똑같이 나누어 꽂으려고 합니다. 책을 책장 한 단에 몇 권씩 꽂아야 합니까?\n"
    answer = "(답): $$수식$${see}$$/수식$$권\n"
    comment = "(해설)\n" \
            "$$수식$$LEFT ( 전체``책``수 RIGHT ) `=` LEFT ( {s1}``수 RIGHT ) `+` LEFT ( {s2}``수 RIGHT ) $$/수식$$\n" \
              "$$수식$$`=`{saa} `+` {sbb} `=` {sdd} LEFT ( 권 RIGHT )$$/수식$$\n" \
            "$$수식$$LEFT ( 책장``한``단에``꽂아야``하는``책 수 RIGHT ) $$/수식$$\n $$수식$$`=` LEFT ( 전체``책``수 RIGHT ) `Div` {scc}$$/수식$$\n" \
              "$$수식$$`=` {sdd} `Div` {scc} `=` {see} LEFT ( 권 RIGHT )$$/수식$$\n\n"


    while True:
        s1=["동화책","위인전","과학책","소설책","학습 만화책","시집"][np.random.randint(0,6)]
        s2=["동화책","위인전","과학책","소설책","학습 만화책","시집"][np.random.randint(0,6)]
        if s1!=s2:
            break

    while True:
        sa=np.random.randint(3,10)
        sb=np.random.randint(1,10)
        sdd=sa*10+sb
        tempa = []
        for idxa in range(1, sa + 1):
            if sa % idxa == 0:
                tempa.append(idxa)  # tempa 리스트에 sa 변수의 약수들을 모음

        tempdd = []
        for idxdd in range(1, sdd + 1):
            if sdd % idxdd == 0:
                tempdd.append(idxdd)  # tempdd 리스트에 sdd 변수의 약수들을 모음

        scclist = np.random.choice(tempdd, 1, replace=False)
        scc = scclist[0]
        if (tempa.count(scc) == 0) and (2 <= scc) and (scc < sa):
            break

    saa=np.random.randint(11,sdd-10)
    sbb=sdd-saa
    see=int(sdd/scc)

    stem=stem.format(s1=s1,saa=saa,s2=s2,sbb=sbb,scc=scc)
    answer=answer.format(see=see)
    comment=comment.format(s1=s1,s2=s2,saa=saa,sbb=sbb,sdd=sdd,scc=scc,see=see)

    return stem,answer,comment
























# 3-2-2-유형08-1
def division322_Stem_029():
    stem = "수 카드 $$수식$$LEFT ( {x1} RIGHT )$$/수식$$, $$수식$$LEFT ( {x2} RIGHT )$$/수식$$, $$수식$$LEFT ( {x3} RIGHT )$$/수식$$을 골라 한 번씩 사용하여 만들 수 있는 가장 큰 두 자리 수를 남은 수 카드의 수로 나누었을 때의 몫을 구하시오.\n"
    answer = "(답): $$수식$${sbb}$$/수식$$\n"
    comment = "(해설)\n" \
              "만들 수 있는 가장 큰 두 자리 수 : $$수식$${saa}$$/수식$$\n" \
              "→ $$수식$${saa} `Div` {sa} `=` {sbb}$$/수식$$\n\n"


    while True:
        sa=np.random.randint(2,8)
        sb=np.random.randint(sa+1,9)
        sc=np.random.randint(sb+1,10)
        if ((sc*10+sb)%sa)==0:
            break

    saa=sc*10+sb
    sbb=int(saa/sa)

    candidates=[sa,sb,sc]
    np.random.shuffle(candidates)
    [x1,x2,x3]=candidates

    stem=stem.format(x1=x1,x2=x2,x3=x3)
    answer=answer.format(sbb=sbb)
    comment=comment.format(saa=saa,sa=sa,sbb=sbb)

    return stem,answer,comment




















# 3-2-2-유형08-2
def division322_Stem_030():
    stem = "$$수식$$4$$/수식$$장의 수 카드 중에서 $$수식$$2$$/수식$$장을 골라 한 번씩 사용하여 만들 수 있는 가장 큰 두 자리 수를 가장 작은 수 카드의 수로 나누었을 때의 몫을 구하시오.\n$$수식$$LEFT ( {x1} RIGHT )$$/수식$$, $$수식$$LEFT ( {x2} RIGHT )$$/수식$$, $$수식$$LEFT ( {x3} RIGHT )$$/수식$$, $$수식$$LEFT ( {x4} RIGHT )$$/수식$$\n"
    answer = "(답): $$수식$${sbb}$$/수식$$\n"
    comment = "(해설)\n" \
              "만들 수 있는 가장 큰 두 자리 수 : $$수식$${saa}$$/수식$$\n" \
              "가장 작은 수 카드의 수 : $$수식$${sa}$$/수식$$\n" \
              "→ $$수식$${saa} `Div` {sa} `=` {sbb}$$/수식$$\n\n"

    while True:
        sa=np.random.randint(2,5)
        sc=np.random.randint(sa+2,9)
        sd=np.random.randint(sc+1,10)
        sb=np.random.randint(sa+1,sc)
        if ((sd*10+sc)%sa)==0:
            break

    saa=sd*10+sc
    sbb=int(saa/sa)

    candidates=[sa,sb,sc,sd]
    np.random.shuffle(candidates)
    [x1,x2,x3,x4]=candidates

    stem=stem.format(x1=x1,x2=x2,x3=x3,x4=x4)
    answer=answer.format(sbb=sbb)
    comment=comment.format(saa=saa,sa=sa,sbb=sbb)

    return stem,answer,comment





















# 3-2-2-유형08-3
def division322_Stem_031():
    stem = "$$수식$$3$$/수식$$장의 수 카드 중에서 $$수식$$2$$/수식$$장을 골라 한 번씩 사용하여 $$수식$${sxx}$$/수식$$에 가장 가까운 두 자리 수를 만들었습니다. 만든 두 자리 수를 $$수식$$2$$/수식$$로 나누었을 때의 몫을 구하시오.\n$$수식$$LEFT ( {x1} RIGHT )$$/수식$$, $$수식$$LEFT ( {x2} RIGHT )$$/수식$$, $$수식$$LEFT ( {x3} RIGHT )$$/수식$$\n"
    answer = "(답): $$수식$${shh}$$/수식$$\n"
    comment = "(해설)\n" \
            "만들 수 있는 두 자리 수 : $$수식$${saa}$$/수식$$, $$수식$${sbb}$$/수식$$, $$수식$${scc}$$/수식$$, $$수식$${sdd}$$/수식$$, $$수식$${see}$$/수식$$, $$수식$${sff}$$/수식$$\n" \
            "이 중에서 $$수식$${sxx}$$/수식$$에 가장 가까운 수는 $$수식$${sgg}$$/수식$$이므로 $$수식$${sgg} `Div` 2 `=` {shh}$$/수식$$입니다.\n\n"


    while True:
        while True:
            sa=np.random.randint(2,9)
            sb=np.random.randint(2,9)
            sc=np.random.randint(2,9)
            if (sa<sb)and(sb<sc)and((sa+sc)!=10)and(sa%2==0)and(sc%2==0)and(sb%2!=0):
                break

        if (sc*10+sa)>=(sa*10+sc+1):
            sxx=np.random.randint(sa*10+sc+1,sc*10+sa)
            if (sxx%10==0)and(sxx>9):
                break
                
    saa=sa*10+sb
    sbb=sa*10+sc
    scc=sb*10+sa

    sdd=sb*10+sc
    see=sc*10+sa
    sff=sc*10+sb

    most_close=[[abs(sxx-saa),saa],[abs(sxx-sbb),sbb],[abs(sxx-scc),scc],[abs(sxx-sdd),sdd],[abs(sxx-see),see],[abs(sxx-sff),sff]]
    most_target=min(abs(sxx-saa),abs(sxx-sbb),abs(sxx-scc),abs(sxx-sdd),abs(sxx-see))

    for idx in most_close:
        if idx[0]==most_target:
            sgg=idx[1]
            break

    shh=int(sgg/2)

    candidates=[sa,sb,sc]
    np.random.shuffle(candidates)
    [x1,x2,x3]=candidates

    stem=stem.format(sxx=sxx,x1=x1,x2=x2,x3=x3)
    answer=answer.format(shh=shh)
    comment=comment.format(saa=saa,sbb=sbb,scc=scc,sdd=sdd,see=see,sff=sff,sxx=sxx,sgg=sgg,shh=shh)

    return stem,answer,comment

















# 3-2-2-유형09-1
def division322_Stem_032():
    stem = "나눗셈식에서 몫과 나머지를 차례로 쓰시오.\n$$수식$${saa} `Div` {sbb} `=` {scc} `CDOTS` {sdd}$$/수식$$\n"
    answer = "(답): $$수식$${scc}$$/수식$$, $$수식$${sdd}$$/수식$$\n"
    comment = "(해설)\n" \
            "$$수식$${saa} `Div` {sbb} `=` {scc} `CDOTS` {sdd}$$/수식$$에서 몫은 $$수식$${scc}$$/수식$$, 나머지는 $$수식$${sdd}$$/수식$$입니다.\n\n"


    while True:
        sbb=np.random.randint(4,10)
        scc=np.random.randint(5,10)
        sdd=np.random.randint(1,sbb)

        if sdd!=scc:
            break

    saa=sbb*scc+sdd

    stem=stem.format(saa=saa,sbb=sbb,scc=scc,sdd=sdd)
    answer=answer.format(scc=scc,sdd=sdd)
    comment=comment.format(saa=saa,sbb=sbb,scc=scc,sdd=sdd)

    return stem,answer,comment




















# 3-2-2-유형09-2
def division322_Stem_033():
    stem = "계산을 하여 몫과 나머지를 차례로 쓰시오.\n$$표$$$$수식$${saa} `Div` {sbb}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${scc}$$/수식$$, $$수식$${sdd}$$/수식$$\n"
    comment = "(해설)\n" \
            "$$수식$${saa} `Div` {sbb} `=` {scc} `CDOTS` {sdd}$$/수식$$에서 몫은 $$수식$${scc}$$/수식$$, 나머지는 $$수식$${sdd}$$/수식$$입니다.\n\n"


    while True:
        sbb=np.random.randint(4,10)
        scc=np.random.randint(3,10)
        sdd=np.random.randint(1,sbb)
        if sdd!=scc:
            break

    saa=sbb*scc+sdd

    stem=stem.format(saa=saa,sbb=sbb)
    answer=answer.format(scc=scc,sdd=sdd)
    comment=comment.format(saa=saa,sbb=sbb,scc=scc,sdd=sdd)

    return stem,answer,comment




















# 3-2-2-유형09-3
def division322_Stem_034():
    stem = "나머지가 더 큰 나눗셈의 기호를 쓰시오.\n$$표$$ㄱ. $$수식$${saa} `Div` {sbb}$$/수식$$      ㄴ. $$수식$${scc} `Div` {sdd}$$/수식$$$$/표$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
            "ㄱ. $$수식$${saa} `Div` {sbb} `=` {sa} `CDOTS` {sb}$$/수식$$에서 몫은 $$수식$${sa}$$/수식$$, 나머지는 $$수식$${sb}$$/수식$$입니다.\n" \
            "ㄴ. $$수식$${scc} `Div` {sdd} `=` {sc} `CDOTS` {sd}$$/수식$$에서 몫은 $$수식$${sc}$$/수식$$, 나머지는 $$수식$${sd}$$/수식$$입니다.\n\n"


    while True:
        sbb=np.random.randint(4,10)
        sa=np.random.randint(3,10)
        sb=np.random.randint(1,sbb-1)
        saa=sbb*sa+sb

        sdd=np.random.randint(4,10)
        sc=np.random.randint(3,10)
        sd=np.random.randint(1,sdd)
        scc=sdd*sc+sd

        if (sbb!=sdd)and(sb!=sd)and(saa!=scc):
            break

    if sb>sd:
        a1="ㄱ"
    elif sb<sd:
        a1="ㄴ"

    stem=stem.format(saa=saa,sbb=sbb,scc=scc,sdd=sdd)
    answer=answer.format(a1=a1)
    comment=comment.format(saa=saa,sbb=sbb,sa=sa,sb=sb,scc=scc,sdd=sdd,sc=sc,sd=sd)

    return stem,answer,comment























# 3-2-2-유형09-4
def division322_Stem_035():
    stem = "$$수식$${sff}$$/수식$$로 나누었을 때 나머지가 $$수식$${sr}$$/수식$$인 수를 고르시오.\n① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
            "각 수를 $$수식$${sff}$$/수식$$로 나누어 봅니다.\n" \
            "① $$수식$${z1}$$/수식$$\n" \
            "② $$수식$${z2}$$/수식$$\n" \
            "③ $$수식$${z3}$$/수식$$\n" \
            "④ $$수식$${z4}$$/수식$$\n" \
            "⑤ $$수식$${z5}$$/수식$$\n\n"


    while True:
        while True:
            sff=np.random.randint(6,10)
            sf = np.random.randint(1, sff)
            sg = np.random.randint(1, sff)
            sh = np.random.randint(1, sff)
            si = np.random.randint(1, sff)
            sj = np.random.randint(1, sff)
            if (sf<sg)and(sg<sh)and(sh<si)and(si<sj):
                srlist = np.random.choice([sf,sg,sh,si,sj],1,replace=False)
                sr=srlist[0]
                break

        sa = np.random.randint(3,10)
        sb = np.random.randint(3, 10)
        sc = np.random.randint(3, 10)
        sd = np.random.randint(3, 10)
        se = np.random.randint(3, 10)
        saa = sff * sa + sf
        sbb = sff * sb + sg
        scc = sff * sc + sh
        sdd = sff * sd + si
        see = sff * se + sj
        if (saa!=sbb)and(saa!=scc)and(saa!=sdd)and(saa!=see)and(sbb!=scc)and(sbb!=sdd)and(sbb!=see)and(scc!=sdd)and(scc!=see)and(sdd!=see):
            break

    y1=[saa,"%s `Div` %s `=` %s `CDOTS` %s"%(saa,sff,sa,sf),sf]
    y2=[sbb,"%s `Div` %s `=` %s `CDOTS` %s"%(sbb,sff,sb,sg),sg]
    y3=[scc,"%s `Div` %s `=` %s `CDOTS` %s"%(scc,sff,sc,sh),sh]
    y4=[sdd,"%s `Div` %s `=` %s `CDOTS` %s"%(sdd,sff,sd,si),si]
    y5=[see,"%s `Div` %s `=` %s `CDOTS` %s"%(see,sff,se,sj),sj]

    candidates=[y1,y2,y3,y4,y5]
    np.random.shuffle(candidates)
    [[x1,z1,a1],[x2,z2,a2],[x3,z3,a3],[x4,z4,a4],[x5,z5,a5]]=candidates

    correct_idx=0

    for idx,sdx in enumerate(candidates):
        if sdx[2]==sr:
            correct_idx=idx
            break

    stem=stem.format(sff=sff,sr=sr,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a1=answer_dict[correct_idx])
    comment=comment.format(sff=sff,z1=z1,z2=z2,z3=z3,z4=z4,z5=z5)

    return stem,answer,comment





















# 3-2-2-유형09-5
def division322_Stem_036():
    stem = "두 나눗셈의 나머지의 차를 구하시오.\n$$표$$$$수식$${saa} `Div` {sbb}````````````````````````{scc} `Div` {sdd}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
            "$$수식$${saa} `Div` {sbb} `=` {sa} `CDOTS` {sb}$$/수식$$에서 몫은 $$수식$${sa}$$/수식$$, 나머지는 $$수식$${sb}$$/수식$$입니다.\n" \
            "$$수식$${scc} `Div` {sdd} `=` {sc} `CDOTS` {sd}$$/수식$$에서 몫은 $$수식$${sc}$$/수식$$, 나머지는 $$수식$${sd}$$/수식$$입니다.\n" \
            "따라서 나머지의 차는 $$수식$${see}$$/수식$$입니다.\n\n"


    while True:
        sbb=np.random.randint(4,10)
        sa=np.random.randint(3,10)
        sb=np.random.randint(1,sbb)
        saa=sbb*sa+sb

        sdd=np.random.randint(4,10)
        sc=np.random.randint(3,10)
        sd=np.random.randint(1,sdd)
        scc=sdd*sc+sd

        if (sbb!=sdd)and(saa!=scc):
            break

    see=abs(sb-sd)

    stem=stem.format(saa=saa,sbb=sbb,scc=scc,sdd=sdd)
    answer=answer.format(see=see)
    comment=comment.format(saa=saa,sbb=sbb,sa=sa,sb=sb,scc=scc,sdd=sdd,sc=sc,sd=sd,see=see)

    return stem,answer,comment




















# 3-2-2-유형10-1
def division322_Stem_037():
    stem = "나머지를 잘못 구한 나눗셈의 기호를 쓰시오.\n$$표$$ㄱ. {x1}      ㄴ. {x2}$$/표$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
            "나눗셈에서 나머지는 항상 나누는 수보다 작아야 합니다.\n" \
            "ㄱ. {z1}\n" \
            "ㄴ. {z2}\n\n"


    while True:
        saa=np.random.randint(3,9)
        sa=np.random.randint(saa+1,10)
        sbb=np.random.randint(3,10)
        sb=np.random.randint(1,sbb)
        if (saa!=sbb):
            break

    scc = np.random.randint(5, 10)
    sdd = np.random.randint(5,10)

    if sa in [2,4,5,9]:
        josa1 = "는"
    else:
        josa1 = "은"

    if sb in [2,4,5,9]:
        josa2 = "는"
    else:
        josa2 = "은"

    y1=["■$$수식$$`Div` %s `=` %s `CDOTS` %s$$/수식$$"%(saa,scc,sa),"■$$수식$$`Div` %s `=` %s `CDOTS` %s$$/수식$$ → 나머지 $$수식$$%s$$/수식$$%s 나누는 수 $$수식$$%s$$/수식$$보다 큽니다."%(saa,scc,sa,sa,josa1,saa)]
    y2=["■$$수식$$`Div` %s `=` %s `CDOTS` %s$$/수식$$"%(sbb,sdd,sb),"■$$수식$$`Div` %s `=` %s `CDOTS` %s$$/수식$$ → 나머지 $$수식$$%s$$/수식$$%s 나누는 수 $$수식$$%s$$/수식$$보다 작습니다."%(sbb,sdd,sb,sb,josa2,sbb)]

    candidates=[y1,y2]
    np.random.shuffle(candidates)
    [[x1,z1],[x2,z2]]=candidates

    correct_idx=0

    for idx,sdx in enumerate(candidates):
        if sdx[0]==y1[0]:
            correct_idx=idx
            break

    stem=stem.format(x1=x1,x2=x2)
    answer=answer.format(a1=answer_kodict[correct_idx])
    comment=comment.format(z1=z1,z2=z2)

    return stem,answer,comment


















# 3-2-2-유형10-2
def division322_Stem_038():
    stem = "어떤 수를 $$수식$${saa}$$/수식$${ro1} 나누었을 때 나머지가 될 수 없는 수를 쓰시오.\n$$표$$$$수식$${x1}````````````{x2}````````````{x3}````````````{x4}````````````{x5}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${se}$$/수식$$\n"
    comment = "(해설)\n" \
            "어떤 수를 $$수식$${saa}$$/수식$${ro1} 나누면 나머지가 $$수식$${saa}$$/수식$$보다 작아야 하므로 $$수식$${saa}$$/수식$${eun1} 나머지가 될 수 없습니다.\n\n"


    while True:
        sa=np.random.randint(1,10)
        sb=np.random.randint(1,10)
        sc=np.random.randint(1,10)
        sd=np.random.randint(1,10)
        se=np.random.randint(1,10)
        if (sa<sb)and(sb<sc)and(sc<sd)and(sd<se):
            break

    saa=se

    candidates=[sa,sb,sc,sd,se]
    np.random.shuffle(candidates)
    [x1,x2,x3,x4,x5]=candidates

    if saa == 3 or saa == 6:
        ro1 = "으로"
    else:
        ro1 = "로"

    if saa == 2 or saa == 4 or saa == 5 or saa == 9:
        eun1 = "는"
    else:
        eun1 = "은"


    stem = stem.format(saa=saa, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, ro1=ro1)
    answer = answer.format(se=se)
    comment = comment.format(saa=saa, ro1=ro1, eun1=eun1)


    return stem,answer,comment

















# 3-2-2-유형10-3
def division322_Stem_039():
    stem = "다음 중 나머지가 $$수식$${sr}$$/수식$${ga1} 될 수 있는 나눗셈을 찾아 기호를 쓰시오.\n{one} {x1}\n{two} {x2}\n{three} {x3}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
            "나머지는 나누는 수보다 작아야 하므로 나머지가 $$수식$${sr}$$/수식$${ga1} 되려면 나누는 수는 $$수식$${sr}$$/수식$$보다 커야 합니다.\n\n"


    while True:
        sa = np.random.randint(3, 10)
        sb = np.random.randint(3, 10)
        sr = np.random.randint(3, 10)
        sc = np.random.randint(3, 10)

        if (sa < sb) and (sb <= sr) and (sr < sc):
            break


    y1 = "□$$수식$$ ` Div ` %s$$/수식$$" % (sa)
    y2 = "□$$수식$$ ` Div ` %s$$/수식$$" % (sb)
    y3 = "□$$수식$$ ` Div ` %s$$/수식$$" % (sc)
    

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [x1, x2, x3] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):
        if sdx == y3:
            correct_idx = idx
            break

    if sr == 2 or sr == 4 or sr == 5 or sr == 9:
        ga1 = "가"
    else:
        ga1 = "이"

    one = "①"
    two = "②"
    three = "③"


    stem = stem.format(sr=sr, x1=x1, x2=x2, x3=x3, ga1=ga1, one=one, two=two, three=three)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(sr=sr, ga1=ga1)

    return stem,answer,comment

























# 3-2-2-유형10-4
def division322_Stem_040():
    stem = "다음 나눗셈에서 나올 수 있는 나머지 중 가장 큰 수는 $$수식$${sr}$$/수식$$입니다. {sss}에 알맞은 한 자리 수는 얼마입니까?\n$$표$$□$$수식$$`Div` {sss}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${saa}$$/수식$$\n"
    comment = "(해설)\n" \
              "나머지는 항상 나누는 수보다 작아야 하므로 나누는 수는 $$수식$${sr}$$/수식$$보다 큰 수입니다.\n" \
              "이 때 나머지 중 가장 큰 수가 $$수식$${sr}$$/수식$$이므로 $$수식$${sss}$$/수식$$에 " \
              "알맞은 한 자리 수는 $$수식$${sr}$$/수식$$보다 $$수식$$1$$/수식$$ 큰 수인 $$수식$${saa}$$/수식$$입니다.\n\n"


    sss = ["●", "◆", "▲", "▼", "★"][np.random.randint(0, 5)]
    sr = np.random.randint(3, 9)
    saa = sr + 1


    stem = stem.format(sr=sr, sss=sss)
    answer = answer.format(saa=saa)
    comment = comment.format(sr=sr, sss=sss, saa=saa)


    return stem,answer,comment




















# 3-2-2-유형11-1
def division322_Stem_041():
    stem = "다음 중 $$수식$${sxx}$$/수식$$로 나누었을 때 나누어떨어지는 수는 어느 것입니까?\n① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
            "나누어떨어지는 경우는 나머지가 $$수식$$0$$/수식$$일 때입니다.\n" \
            "① {z1}\n" \
            "② {z2}\n" \
            "③ {z3}\n" \
            "④ {z4}\n" \
            "⑤ {z5}\n\n"


    sxx = np.random.randint(5, 10)

    sa = np.random.randint(4, 10)
    sb = np.random.randint(4, 10)
    sc = np.random.randint(4, 10)
    sd = np.random.randint(4, 10)
    se = np.random.randint(4, 10)

    while True:
        sg = np.random.randint(1, sxx)
        sh = np.random.randint(1, sxx)
        si = np.random.randint(1, sxx)
        sj = np.random.randint(1, sxx)
        if (sg!=sh)and(sg!=si)and(sg!=sj)and(sh!=si)and(sh!=sj)and(si!=sj):
            break

    saa = sxx * sa
    sbb = sxx * sb + sg
    scc = sxx * sc + sh
    sdd = sxx * sd + si
    see = sxx * se + sj

    # candidates=[saa,sbb,scc,sdd,see]
    # candidates.sort()
    # this_answer=candidates[0]


    y1 = [saa, "$$수식$$%s `Div` %s `=` %s$$/수식$$" % (saa, sxx, sa)]
    y2 = [sbb, "$$수식$$%s `Div` %s `=` %s `CDOTS` %s$$/수식$$" % (sbb, sxx, sb, sg)]
    y3 = [scc, "$$수식$$%s `Div` %s `=` %s `CDOTS` %s$$/수식$$" % (scc, sxx, sc, sh)]
    y4 = [sdd, "$$수식$$%s `Div` %s `=` %s `CDOTS` %s$$/수식$$" % (sdd, sxx, sd, si)]
    y5 = [see, "$$수식$$%s `Div` %s `=` %s `CDOTS` %s$$/수식$$" % (see, sxx, se, sj)]

    candidates=[y1,y2,y3,y4,y5]
    candidates.sort()
    [[x1,z1],[x2,z2],[x3,z3],[x4,z4],[x5,z5]]=candidates

    correct_idx=0
    for idx,sdx in enumerate(candidates):
        if sdx==y1:
            correct_idx=idx
            break

    stem=stem.format(sxx=sxx,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a1=answer_dict[correct_idx])
    comment=comment.format(z1=z1,z2=z2,z3=z3,z4=z4,z5=z5)

    return stem,answer,comment






















# 3-2-2-유형11-2
def division322_Stem_042():
    stem = "나누어떨어지지 않는 나눗셈을 찾아 기호를 쓰시오.\n$$표$$ㄱ. {x1}      ㄴ. {x2}      ㄷ. {x3}$$/표$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
            "나누어떨어지지 않는 경우는 나머지가 $$수식$$0$$/수식$$이 아닐 때입니다.\n" \
            "ㄱ. {z1}\n" \
            "ㄴ. {z2}\n" \
            "ㄷ. {z3}\n\n"


    while True:
        sa=np.random.randint(4,10)
        sb=np.random.randint(4,10)
        sc=np.random.randint(4,10)

        sdd=np.random.randint(6,10)
        see=np.random.randint(6,10)
        sff=np.random.randint(6,10)

        sr=np.random.randint(1,sc)
        saa=sa*sdd
        sbb=sb*see
        scc=sff*sc+sr

        if (saa!=sbb)and(saa!=scc)and(sbb!=scc):
            break

    y1=["$$수식$$%s `Div` %s$$/수식$$"%(saa,sa),"$$수식$$%s `Div` %s `=` %s$$/수식$$"%(saa,sa,sdd)]
    y2=["$$수식$$%s `Div` %s$$/수식$$"%(sbb,sb),"$$수식$$%s `Div` %s `=` %s$$/수식$$"%(sbb,sb,see)]
    y3=["$$수식$$%s `Div` %s$$/수식$$"%(scc,sc),"$$수식$$%s `Div` %s `=` %s `CDOTS` %s$$/수식$$"%(scc,sc,sff,sr)]

    candidates=[y1,y2,y3]
    np.random.shuffle(candidates)
    [[x1,z1],[x2,z2],[x3,z3]]=candidates

    correct_idx=0
    for idx,sdx in enumerate(candidates):
        if sdx==y3:
            correct_idx=idx
            break

    stem=stem.format(x1=x1,x2=x2,x3=x3)
    answer=answer.format(a1=answer_kodict[correct_idx])
    comment=comment.format(z1=z1,z2=z2,z3=z3)

    return stem,answer,comment























# 3-2-2-유형11-3
def division322_Stem_043():
    stem = "나눗셈 $$수식$${saa} `Div`$$/수식$$□는 나누어떨어집니다. □ 안에 들어갈 수 있는 가장 큰 한 자리 수를 구하시오.\n"
    answer = "(답): $$수식$${sa}$$/수식$$\n"
    comment = "(해설)\n" \
            "□ 안에 $$수식$$9$$/수식$$, $$수식$$8$$/수식$$, $$수식$$7 CDOTS CDOTS$$/수식$$순서로 수를 넣어 나머지가 $$수식$$0$$/수식$$일 때를 알아봅니다.\n" \
            "$$수식$${saa} `Div` {sa} `=` {sbb}$$/수식$$은 나누어떨어지므로 □ 안에 들어갈 수 있는 가장 큰 한 자리 수는 $$수식$${sa}$$/수식$$입니다.\n\n"


    sa=np.random.randint(6,10)
    sbb=np.random.randint(5,sa)
    saa=sa*sbb

    stem=stem.format(saa=saa)
    answer=answer.format(sa=sa)
    comment=comment.format(saa=saa,sa=sa,sbb=sbb)

    return stem,answer,comment
























# 3-2-2-유형11-4
def division322_Stem_044():
    stem = "나눗셈 □$$수식$$`Div` {saa}$$/수식$$은 나누어떨어집니다. □ 안에 들어갈 수 있는 두 자리 수 중 $$수식$${sbb}$$/수식$$에 가장 가까운 수를 구하시오.\n"
    answer = "(답): $$수식$${see}$$/수식$$\n"
    comment = "(해설)\n" \
            "□$$수식$$`Div` {saa}$$/수식$$의 몫을 ㉠이라고 하면 □$$수식$$`Div` {saa} `=`$$/수식$$㉠입니다.\n" \
            "곱셈과 나눗셈의 관계를 이용하면 □$$수식$$`Div` {saa} `=`$$/수식$$㉠ → $$수식$${saa} `Times`$$/수식$$㉠$$수식$$`=`$$/수식$$□입니다.\n" \
            "$$수식$${saa} `Times` {sa} `=` {scc}$$/수식$$, $$수식$${saa} `Times` {sb} `=` {sdd}$$/수식$$이므로 " \
            "□ 안에 들어갈 수 있는 두 자리 수 중 $$수식$${sbb}$$/수식$$에 가장 가까운 수는 $$수식$${see}$$/수식$$입니다.\n\n"


    while True:
        saa=np.random.randint(7,10)

        while True:
            sbb=np.random.randint(40,61)
            if (sbb%7!=0)and(sbb%8!=0)and(sbb%9!=0):
                break

        sa=int(sbb/saa)

        if sa!=(sbb/saa-0.5):
            break

    sb=sa+1
    scc=saa*sa
    sdd=saa*sb

    if (sbb-scc)<(sdd-sbb):
        see=scc
    elif (sbb-scc)>(sdd-sbb):
        see=sdd

    stem=stem.format(saa=saa,sbb=sbb)
    answer=answer.format(see=see)
    comment=comment.format(saa=saa,sa=sa,scc=scc,sb=sb,sdd=sdd,sbb=sbb,see=see)

    return stem,answer,comment


















# 3-2-2-유형12-1
def division322_Stem_045():
    stem = "계산을 하여 몫과 나머지를 차례로 쓰시오.\n$$표$$$$수식$${saa} `Div` {sbb}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${scc}$$/수식$$, $$수식$${sr}$$/수식$$\n"
    comment = "(해설)\n" \
            "$$수식$${saa} `Div` {sbb} `=` {scc} `CDOTS` {sr}$$/수식$$입니다.\n\n"


    while True:
        sbb = np.random.randint(2, 10)
        scc = np.random.randint(11, 30)
        sr = np.random.randint(1, sbb)

        saa=sbb*scc+sr

        if (30<=saa)and(saa<=99):
            break

    stem=stem.format(saa=saa,sbb=sbb)
    answer=answer.format(scc=scc,sr=sr)
    comment=comment.format(saa=saa,sbb=sbb,scc=scc,sr=sr)

    return stem,answer,comment




















# 3-2-2-유형12-2
def division322_Stem_046():
    stem = "다음 나눗셈의 몫과 나머지의 합을 구하시오.\n$$표$$$$수식$${saa} `Div` {sbb}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${sdd}$$/수식$$\n"
    comment = "(해설)\n" \
            "$$수식$${saa} `Div` {sbb} `=` {scc} `CDOTS` {sr}$$/수식$$이므로 몫과 나머지의 합은 $$수식$${scc} `+` {sr} `=` {sdd}$$/수식$$입니다.\n\n"


    while True:
        sbb=np.random.randint(2,10)
        scc=np.random.randint(11,30)
        sr=np.random.randint(1,sbb)

        saa=sbb*scc+sr

        if (30<=saa)and(saa<=99):
            break

    sdd=scc+sr

    stem=stem.format(saa=saa,sbb=sbb)
    answer=answer.format(sdd=sdd)
    comment=comment.format(saa=saa,sbb=sbb,scc=scc,sr=sr,sdd=sdd)

    return stem,answer,comment
























# 3-2-2-유형12-3
def division322_Stem_047():
    stem = "다음 중 나눗셈의 몫과 나머지를 잘못 구한 것을 고르시오.\n{one} {x1}\n{two} {x2}\n{three} {x3}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
            "① {z1}\n" \
            "② {z2}\n" \
            "③ {z3}\n\n"


    while True:
        sbb = np.random.randint(2, 10)
        sdd = np.random.randint(2, 10)
        sff = np.random.randint(2, 10)

        sa = np.random.randint(11, 30)
        sc = np.random.randint(11, 30)
        se = np.random.randint(11, 30)

        sb = np.random.randint(1, sbb)
        sd = np.random.randint(1, sdd)
        sf = np.random.randint(1, sff)

        saa=sbb*sa+sb
        scc=sdd*sc+sd
        see=sff*se+sf

        if (sbb!=sdd)and(sbb!=sff)and(sdd!=sff)and(saa!=scc)and(saa!=see)and(scc!=see)and(30<=saa)and(saa<=99)and(30<=scc)and(scc<=99)and(30<=see)and(see<=99):
            break

    sg=[se-1,se+1][np.random.randint(0,2)]

    y1=["$$수식$$%s `Div` %s$$/수식$$ → 몫 : $$수식$$%s$$/수식$$, 나머지 : $$수식$$%s$$/수식$$"%(saa,sbb,sa,sb),"$$수식$$%s `Div` %s `=` %s `CDOTS` %s$$/수식$$ → 몫 : $$수식$$%s$$/수식$$, 나머지 : $$수식$$%s$$/수식$$"%(saa,sbb,sa,sb,sa,sb)]
    y2=["$$수식$$%s `Div` %s$$/수식$$ → 몫 : $$수식$$%s$$/수식$$, 나머지 : $$수식$$%s$$/수식$$"%(scc,sdd,sc,sd),"$$수식$$%s `Div` %s `=` %s `CDOTS` %s$$/수식$$ → 몫 : $$수식$$%s$$/수식$$, 나머지 : $$수식$$%s$$/수식$$"%(scc,sdd,sc,sd,sc,sd)]
    y3=["$$수식$$%s `Div` %s$$/수식$$ → 몫 : $$수식$$%s$$/수식$$, 나머지 : $$수식$$%s$$/수식$$"%(see,sff,sg,sf),"$$수식$$%s `Div` %s `=` %s `CDOTS` %s$$/수식$$ → 몫 : $$수식$$%s$$/수식$$, 나머지 : $$수식$$%s$$/수식$$"%(see,sff,se,sf,se,sf)]

    candidates=[y1,y2,y3]
    np.random.shuffle(candidates)
    [[x1,z1],[x2,z2],[x3,z3]]=candidates

    correct_idx=0
    for idx,sdx in enumerate(candidates):
        if sdx==y3:
            correct_idx=idx
            break


    one = "①"
    two = "②"
    three = "③"


    stem = stem.format(x1=x1, x2=x2, x3=x3, one=one, two=two, three=three)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(z1=z1, z2=z2, z3=z3)


    return stem, answer, comment


























# 3-2-2-유형12-4
def division322_Stem_048():
    stem = "다음 중 나머지가 가장 큰 나눗셈을 고르시오.\n{one} {x1}\n{two} {x2}\n{three} {x3}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
            "① {z1}\n" \
            "② {z2}\n" \
            "③ {z3}\n\n"


    while True:
        sbb = np.random.randint(4, 10)
        sdd = np.random.randint(4, 10)
        sff = np.random.randint(4, 10)

        sa = np.random.randint(11, 30)
        sc = np.random.randint(11, 30)
        se = np.random.randint(11, 30)

        sb = np.random.randint(1, sbb)
        sd = np.random.randint(2, sdd)
        sf = np.random.randint(3, sff)

        saa=sbb*sa+sb
        scc=sdd*sc+sd
        see=sff*se+sf

        if (sbb!=sdd)and(sbb!=sff)and(sdd!=sff)and(sb<sd)and(sd<sf)and(saa!=scc)and(saa!=see)and(scc!=see)and(30<=saa)and(saa<=99)and(30<=scc)and(scc<=99)and(30<=see)and(see<=99):
            break

    y1=["$$수식$$%s `Div` %s$$/수식$$"%(saa,sbb),"$$수식$$%s `Div` %s `=` %s `CDOTS` %s$$/수식$$"%(saa,sbb,sa,sb)]
    y2=["$$수식$$%s `Div` %s$$/수식$$"%(scc,sdd),"$$수식$$%s `Div` %s `=` %s `CDOTS` %s$$/수식$$"%(scc,sdd,sc,sd)]
    y3=["$$수식$$%s `Div` %s$$/수식$$"%(see,sff),"$$수식$$%s `Div` %s `=` %s `CDOTS` %s$$/수식$$"%(see,sff,se,sf)]

    candidates=[y1,y2,y3]
    np.random.shuffle(candidates)
    [[x1,z1],[x2,z2],[x3,z3]]=candidates

    correct_idx=0
    for idx,sdx in enumerate(candidates):
        if sdx==y3:
            correct_idx=idx
            break

    one = "①"
    two = "②"
    three = "③"


    stem = stem.format(x1=x1, x2=x2, x3=x3, one=one, two=two, three=three)
    answer=answer.format(a1=answer_dict[correct_idx])
    comment=comment.format(z1=z1,z2=z2,z3=z3)

    return stem,answer,comment























# 3-2-2-유형12-5
def division322_Stem_049():
    stem = "다음 중 나머지가 다른 나눗셈을 고르시오.\n{circle_one} {x1}\n{circle_two} {x2}\n{circle_three} {x3}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
            "① {z1}\n" \
            "② {z2}\n" \
            "③ {z3}\n\n"


    while True:
        sbb = np.random.randint(3, 10)
        sdd = np.random.randint(3, 10)
        sff = np.random.randint(3, 10)

        sa = np.random.randint(11, 30)
        sc = np.random.randint(11, 30)
        se = np.random.randint(11, 30)

        sb = np.random.randint(2, sbb)
        sd = np.random.randint(2, sdd)
        sf = np.random.randint(1, sff)

        saa=sbb*sa+sb
        scc=sdd*sc+sd
        see=sff*se+sf

        if (sbb!=sdd)and(sbb!=sff)and(sdd!=sff)and(sb==sd)and(sf<=(sb-1))and(30<=saa)and(saa<=99)and(30<=scc)and(scc<=99)and(30<=see)and(see<=99):
            break

    y1=["$$수식$$%s `Div` %s$$/수식$$"%(saa,sbb),"$$수식$$%s `Div` %s `=` %s `CDOTS` %s$$/수식$$"%(saa,sbb,sa,sb)]
    y2=["$$수식$$%s `Div` %s$$/수식$$"%(scc,sdd),"$$수식$$%s `Div` %s `=` %s `CDOTS` %s$$/수식$$"%(scc,sdd,sc,sd)]
    y3=["$$수식$$%s `Div` %s$$/수식$$"%(see,sff),"$$수식$$%s `Div` %s `=` %s `CDOTS` %s$$/수식$$"%(see,sff,se,sf)]

    candidates=[y1,y2,y3]
    np.random.shuffle(candidates)
    [[x1,z1],[x2,z2],[x3,z3]]=candidates

    correct_idx=0
    for idx,sdx in enumerate(candidates):
        if sdx==y3:
            correct_idx=idx
            break


    stem = stem.format(x1=x1, x2=x2, x3=x3, circle_one=circle_one, circle_two=circle_two, circle_three=circle_three)
    answer=answer.format(a1=answer_dict[correct_idx])
    comment=comment.format(z1=z1,z2=z2,z3=z3)

    return stem,answer,comment




















# 3-2-2-유형13-1
def division322_Stem_050():
    stem = "{sss} $$수식$${saa}$$/수식$$개를 한 명에게 $$수식$${sbb}$$/수식$$개씩 나누어 주려고 합니다. {sss}{j1} 몇 명까지 나누어 줄 수 있고 남는 {sss}{j2} 몇 개입니까?\n"
    answer = "(답): $$수식$${scc}$$/수식$$명, $$수식$${sdd}$$/수식$$개\n"
    comment = "(해설)\n" \
            "$$수식$${saa} `Div` {sbb} `=` {scc} `CDOTS` {sdd}$$/수식$$이므로\n" \
            "{sss}{j1} $$수식$${scc}$$/수식$$명까지 나누어 줄 수 있고 남는 {sss}{j2} $$수식$${sdd}$$/수식$$개입니다.\n\n"


    sss=["귤","밤","체리","앵두","살구"][np.random.randint(0,5)]
    j1=proc_jo(sss,1)
    j2=proc_jo(sss,-1)

    sbb=np.random.randint(3,10)
    scc=np.random.randint(7,10)
    sdd=np.random.randint(1,sbb)

    saa=sbb*scc+sdd

    stem=stem.format(sss=sss,saa=saa,sbb=sbb,j1=j1,j2=j2)
    answer=answer.format(scc=scc,sdd=sdd)
    comment=comment.format(saa=saa,sbb=sbb,scc=scc,sdd=sdd,sss=sss,j1=j1,j2=j2)

    return stem,answer,comment



















# 3-2-2-유형13-2
def division322_Stem_051():
    stem = "{spp}이는 친구들에게 줄 {sss} $$수식$${saa}$$/수식$$개를 $$수식$${sbb}$$/수식$$명에게 똑같이 나누어 주고, 남는 것을 먹으려고 합니다. {spp}이가 먹을 수 있는 {sss}{j1} 몇 개 입니까?\n"
    answer = "(답): $$수식$${sdd}$$/수식$$개\n"
    comment = "(해설)\n" \
            "$$수식$${saa} `Div` {sbb} `=` {scc} `CDOTS` {sdd}$$/수식$$이므로\n" \
            "{sss}{j2} $$수식$${sbb}$$/수식$$명에게 $$수식$${scc}$$/수식$$개씩 나누어 주고, $$수식$${sdd}$$/수식$$개가 남습니다. " \
            "따라서 {spp}이가 먹을 수 있는 {sss}{j1} 남는 $$수식$${sdd}$$/수식$$개입니다.\n\n"


    spp = ["지은", "도윤", "예준", "은진", "희선", "가영", "민혁", "수원", "요환", "정석", "종국", "하율"][np.random.randint(0, 12)]
    sss = ["초콜릿", "사탕", "찹쌀떡", "젤리"][np.random.randint(0, 4)]

    j1=proc_jo(sss,-1)
    j2=proc_jo(sss,1)

    while True:
        sbb=np.random.randint(3,10)
        scc=np.random.randint(11,30)
        sdd=np.random.randint(1,sbb)
        saa=sbb*scc+sdd
        if (34<=saa)and(saa<=99):
            break

    stem=stem.format(spp=spp,sss=sss,saa=saa,sbb=sbb,j1=j1)
    answer=answer.format(sdd=sdd)
    comment=comment.format(saa=saa,sbb=sbb,scc=scc,sdd=sdd,sss=sss,j2=j2,spp=spp,j1=j1)

    return stem,answer,comment





















# 3-2-2-유형13-3
def division322_Stem_052():
    stem = "{sss} $$수식$${sbb} rm {{cm}}$$/수식$$로 리본 한 개를 만들 수 있습니다. {sss} $$수식$${saa} rm {{cm}}$$/수식$$로 같은 크기의 리본을 몇 개까지 만들 수 있고, 남는 {sss}{j1} 몇 $$수식$$rm {{cm}}$$/수식$$입니까?\n"
    answer = "(답): $$수식$${scc}$$/수식$$개, $$수식$${sdd} rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
            "$$수식$${saa} `Div` {sbb} `=` {scc} `CDOTS` {sdd}$$/수식$$이므로\n" \
            "리본을 $$수식$${scc}$$/수식$$개까지 만들 수 있고 남는 {sss}{j1} $$수식$${sdd} rm {{cm}}$$/수식$$입니다.\n\n"


    sss=["색 테이프","종이테이프","띠지","노끈"][np.random.randint(0,4)]
    j1=proc_jo(sss,-1)

    while True:
        sbb=np.random.randint(5,10)
        scc=np.random.randint(11,30)
        sdd=np.random.randint(1,sbb)
        saa=sbb*scc+sdd
        if (56<=saa)and(saa<=99):
            break

    stem=stem.format(sss=sss,sbb=sbb,saa=saa,j1=j1)
    answer=answer.format(scc=scc,sdd=sdd)
    comment=comment.format(saa=saa,sbb=sbb,scc=scc,sdd=sdd,sss=sss,j1=j1)

    return stem,answer,comment






















# 3-2-2-유형13-4
def division322_Stem_053():
    stem = "'타'는 물건 $$수식$$12$$/수식$$개를 한 단위로 세는 말입니다. {s1} $$수식$${sa}$$/수식$$타를 {s2} 한 개에 $$수식$${sbb}$$/수식$$자루씩 나누어 담으면 {s1}을 {s2} 몇 개에 나누어 담을 수 있고, 남는 {s1}은 몇 자루입니까?\n"
    answer = "(답): $$수식$${scc}$$/수식$$개, $$수식$${sdd}$$/수식$$자루\n"
    comment = "(해설)\n" \
            "{s1} 한 타는 $$수식$$12$$/수식$$자루이므로 $$수식$$LEFT ( {sa}$$/수식$$타의 {s1} 수$$수식$$RIGHT ) $$/수식$$\n $$수식$$ `=` 12 `Times` {sa} `=` {saa} LEFT ($$/수식$$자루$$수식$$RIGHT )$$/수식$$입니다.\n" \
            "$$수식$${saa} `Div` {sbb} `=` {scc} `CDOTS` {sdd}$$/수식$$이므로\n" \
            "{s1}을 {s2} $$수식$${scc}$$/수식$$개에 나누어 담을 수 있고, 남는 {s1}은 $$수식$${sdd}$$/수식$$자루입니다.\n\n"


    s1=["연필","색연필","볼펜","사인펜"][np.random.randint(0,4)]
    s2=["필통","상자","연필꽂이"][np.random.randint(0,3)]

    sa=[4,8][np.random.randint(0,2)]
    saa=sa*12
    sbb=[5,7][np.random.randint(0,2)]

    scc=int(saa/sbb)
    sdd=saa-(sbb*scc)

    stem=stem.format(s1=s1,sa=sa,s2=s2,sbb=sbb)
    answer=answer.format(scc=scc,sdd=sdd)
    comment=comment.format(s1=s1,sa=sa,saa=saa,sbb=sbb,scc=scc,sdd=sdd,s2=s2)

    return stem,answer,comment
























# 3-2-2-유형13-5
def division322_Stem_054():
    stem = "{spp}이가 하루에 $$수식$${sa}$$/수식$$쪽씩 $$수식$${sb}$$/수식$$일 동안 다 읽은 {sss}을 동생이 하루에 $$수식$${sbb}$$/수식$$쪽씩 읽으려고 합니다. 동생은 이 {sss}을 모두 읽는 데 며칠이 걸리겠습니까?\n"
    answer = "(답): $$수식$${see}$$/수식$$일\n"
    comment = "(해설)\n" \
            "하루에 $$수식$${sa}$$/수식$$쪽씩 $$수식$${sb}$$/수식$$일 동안 읽었으므로 {sss}은 모두 $$수식$${sa} `Times` {sb} `=` {saa} LEFT ($$/수식$$쪽$$수식$$RIGHT )$$/수식$$입니다.\n" \
            "$$수식$${saa} `Div` {sbb} `=` {scc} `CDOTS` {sdd}$$/수식$$이므로\n" \
            "동생이 이 {sss}을 모두 읽는 데는 $$수식$${scc} `+` 1 `=` {see} LEFT ($$/수식$$일$$수식$$RIGHT )$$/수식$$이 걸립니다.\n\n"


    spp = ["민준", "연진", "명국", "혜영", "준섭", "재인", "주환", "소연", "보람", "지현", "초롱", "하은"][np.random.randint(0, 12)]
    sss=["책","동화책","소설책","과학책","위인전"][np.random.randint(0,5)]


    while True:
        sa=[11,13,17,19][np.random.randint(0,4)]
        sb=[3,5,7,9][np.random.randint(0,4)]
        if (50<sa*sb)and(sa*sb<100):
            break


    saa=sa*sb

    if sb==3:
        sbb = [4, 5, 7, 8][np.random.randint(0, 4)]
    elif sb==5:
        sbb = [3, 4, 6, 7, 8, 9][np.random.randint(0, 6)]
    elif sb==7:
        sbb = [3, 4, 5, 6, 8, 9][np.random.randint(0, 6)]
    elif sb==9:
        sbb = [4, 5, 6, 7, 8][np.random.randint(0, 5)]


    scc=int(saa/sbb)
    sdd=saa-(sbb*scc)
    see=scc+1

    stem=stem.format(spp=spp,sa=sa,sb=sb,sss=sss,sbb=sbb)
    answer=answer.format(see=see)
    comment=comment.format(sa=sa,sb=sb,sss=sss,saa=saa,sbb=sbb,scc=scc,sdd=sdd,see=see)

    return stem,answer,comment



















# 3-2-2-유형14-1
def division322_Stem_055():
    stem = "계산을 하시오.\n$$표$$$$수식$${saa} `Div` {sbb}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${scc}$$/수식$$\n"
    comment = "(해설)\n" \
            "$$수식$${saa} `Div` {sbb} `=` {scc}$$/수식$$입니다.\n\n"


    while True:
        sbb=np.random.randint(2,10)
        scc=np.random.randint(11,200)
        saa=sbb*scc

        if (101<=saa)and(saa<=891):
            break

    stem=stem.format(saa=saa,sbb=sbb)
    answer=answer.format(scc=scc)
    comment=comment.format(saa=saa,sbb=sbb,scc=scc)

    return stem,answer,comment



















# 3-2-2-유형14-2
def division322_Stem_056():
    # stem = "㉠, ㉡, ㉢에 알맞은 수로 짝지어진 것을 고르시오.\n$$수식$${saa} `Div` {sbb} `=`$$/수식$$㉠, $$수식$${scc} `Div` {sdd} `=`$$/수식$$㉡, $$수식$${see} `Div` {sff} `=`$$/수식$$㉢\n   ㉠   ㉡   ㉢\n① {z1}\n② {z2}\n③ {z3}\n④ {z4}\n⑤ {z5}\n⑥ {z6}\n"
    stem = "㉠, ㉡, ㉢에 알맞은 수로 짝지어진 것을 고르시오.\n$$표$$$$수식$${saa} `Div` {sbb} `=`$$/수식$$㉠, $$수식$${scc} `Div` {sdd} `=`$$/수식$$㉡, $$수식$${see} `Div` {sff} `=`$$/수식$$㉢$$/표$$\n① {z1}\n② {z2}\n③ {z3}\n④ {z4}\n⑤ {z5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
            "$$수식$${saa} `Div` {sbb} `=` {sa}$$/수식$$, $$수식$${scc} `Div` {sdd} `=` {sb}$$/수식$$, $$수식$${see} `Div` {sff} `=` {sc}$$/수식$$\n\n"


    while True:
        sbb = np.random.randint(4, 8)
        sdd = sbb + 1
        sff = sdd + 1

        sa = np.random.randint(21, 50)
        sr = [2, 3][np.random.randint(0, 2)]

        sb = sa + sr
        sc = sb + sr
        saa = sbb * sa
        scc = sdd * sb
        see = sff * sc

        if (112 <= saa) and (saa <= 891) and (112 <= scc) and (scc <= 891) and (112 <= see) and (see <= 891):
            break


    y1 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", sa, "㉡", sb, "㉢", sc)
    y2 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", sa, "㉡", sc, "㉢", sb)
    y3 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", sb, "㉡", sa, "㉢", sc)
    y4 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", sb, "㉡", sc, "㉢", sa)
    y5 = "%s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$, %s $$수식$$%s$$/수식$$" % ("㉠", sc, "㉡", sa, "㉢", sb)
    # y6 = "$$수식$$%s````````%s````````%s$$/수식$$" % (sc, sb, sa)


    # candidates = [y1, y2, y3, y4, y5, y6]
    # np.random.shuffle(candidates)
    # [z1, z2, z3, z4, z5, z6] = candidates

    candidates = [y1, y2, y3, y4, y5]
    np.random.shuffle(candidates)
    [z1, z2, z3, z4, z5] = candidates


    correct_idx = 0
    for idx, sdx in enumerate(candidates):
        if sdx == y1:
            correct_idx = idx
            break


    # stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, z1=z1, z2=z2, z3=z3, z4=z4, z5=z5, z6=z6)
    stem = stem.format(saa=saa, sbb=sbb, scc=scc, sdd=sdd, see=see, sff=sff, z1=z1, z2=z2, z3=z3, z4=z4, z5=z5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(saa=saa, sbb=sbb, sa=sa, scc=scc, sdd=sdd, sb=sb, see=see, sff=sff, sc=sc)

    return stem,answer,comment






















# 3-2-2-유형14-3
def division322_Stem_057():
    stem = "큰 수를 작은 수로 나눈 몫을 구하시오.\n$$표$$$$수식$${saa}````````````{sbb}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${scc}$$/수식$$\n"
    comment = "(해설)\n" \
            "$$수식$${saa} `&gt;` {sbb}$$/수식$$이므로 $$수식$${saa} `Div` {sbb} `=` {scc}$$/수식$$입니다.\n\n"


    while True:
        sbb = np.random.randint(2, 10)
        scc = np.random.randint(105, 300)
        saa = sbb * scc

        if (301 <= saa) and (saa <= 998):
            break


    stem = stem.format(saa=saa, sbb=sbb)
    answer = answer.format(scc=scc)
    comment = comment.format(saa=saa, sbb=sbb, scc=scc)

    return stem, answer, comment

























# 3-2-2-유형14-4
def division322_Stem_058():
    stem = "두 나눗셈의 몫의 합을 구하시오.\n$$표$$$$수식$${saa} `Div` {sbb}$$/수식$$$$/표$$    $$표$$$$수식$${scc} `Div` {sdd}$$/수식$$$$/표$$\n"
    answer = "(답): $$수식$${sc}$$/수식$$\n"
    comment = "(해설)\n" \
            "$$수식$${saa} `Div` {sbb} `=` {sa}$$/수식$$, $$수식$${scc} `Div` {sdd} `=` {sb}$$/수식$$\n" \
            "$$수식$$LEFT ($$/수식$$두 나눗셈의 몫의 합$$수식$$RIGHT ) `=` {sa} `+` {sb} `=` {sc}$$/수식$$\n\n"


    while True:
        sbb=np.random.randint(2,10)
        sa = np.random.randint(105, 300)
        saa=sbb*sa
        if (301<=saa)and(saa<=998):
            break

    while True:
        sdd=np.random.randint(2,10)
        sb=np.random.randint(105,300)
        scc=sdd*sb
        if (301<=scc)and(scc<=998):
            break

    sc=sa+sb

    stem=stem.format(saa=saa,sbb=sbb,scc=scc,sdd=sdd)
    answer=answer.format(sc=sc)
    comment=comment.format(saa=saa,sbb=sbb,sa=sa,scc=scc,sdd=sdd,sb=sb,sc=sc)

    return stem,answer,comment
























# 3-2-2-유형14-5
def division322_Stem_059():
    stem = "{p1}와 {p2} 중 몫이 더 큰 나눗셈을 들고 있는 사람은 누구입니까?\n{p1} : $$수식$${saa} `Div` {sbb}$$/수식$$\n{p2} : $$수식$${scc} `Div` {sdd}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
            "{p1} : $$수식$${saa} `Div` {sbb} `=` {sa}$$/수식$$, {p2} : $$수식$${scc} `Div` {sdd} `=` {sb}$$/수식$$\n" \
            "따라서 몫이 더 큰 나눗셈을 들고 있는 사람은 {a1}입니다.\n\n"


    while True:
        p1 = ["지수", "은서", "미호", "시우", "명우", "근호", "나래", "필교", "영래", "솔미", "혜교", "중기", "현화", "진표", "규태", "유나"][np.random.randint(0, 16)]
        p2 = ["지수", "은서", "미호", "시우", "명우", "근호", "나래", "필교", "영래", "솔미", "혜교", "중기", "현화", "진표", "규태", "유나"][np.random.randint(0, 16)]
        if p1 != p2:
            break

    while True:
        sbb=np.random.randint(2,10)
        sdd=np.random.randint(2,10)
        sa=np.random.randint(105,300)
        sb=np.random.randint(105,300)

        saa=sbb*sa
        scc=sdd*sb

        if (sa!=sb)and(-9<=(sa-sb))and((sa-sb)<=9)and(301<=saa)and(saa<=998)and(301<=scc)and(scc<=998):
            break


    if sa > sb:
        a1 = p1
    elif sa < sb:
        a1 = p2


    stem = stem.format(p1=p1, p2=p2, saa=saa, sbb=sbb, scc=scc, sdd=sdd)
    answer = answer.format(a1=a1)
    comment = comment.format(p1=p1, saa=saa, sbb=sbb, sa=sa, p2=p2, scc=scc, sdd=sdd, sb=sb, a1=a1)

    return stem,answer,comment














# 3-2-2-유형15-1
def division322_Stem_060():
    stem = "계산을 하여 몫과 나머지를 차례로 쓰시오.\n$$표$$ $$수식$$`{sa}`div`{sb}`$$/수식$$ $$/표$$\n"
    answer = "(답): $$수식$${sc}$$/수식$$, $$수식$${sd}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$입니다.\n\n"


    while True:
        sb = np.random.randint(2, 10)
        sc = np.random.randint(1, 100)
        sd = np.random.randint(1, sb)
        sa = np.random.randint(101, 892)

        if (sb * sc + sd) == sa:
            break

    stem = stem.format(sa=sa, sb=sb)
    answer = answer.format(sc=sc, sd=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd)

    return stem, answer, comment





















# 3-2-2-유형15-2
def division322_Stem_061():
    stem = "큰 수를 작은 수로 나눈 몫과 나머지를 각각 구하시오.\n$$표$$ $$수식$$`{sa}````````{sb}`$$/수식$$ $$/표$$\n"
    answer = "(답): $$수식$${sc}$$/수식$$, $$수식$${sd}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`&gt;`{sb}``$$/수식$$ 이므로, $$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$입니다.\n\n"


    while True:
        sb = np.random.randint(2, 10)
        sc = np.random.randint(102, 200)
        sd = np.random.randint(1, sb)
        sa = np.random.randint(125, 999)

        if (sb * sc + sd) == sa:
            break


    stem = stem.format(sa=sa, sb=sb)
    answer = answer.format(sc=sc, sd=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd)

    return stem, answer, comment























# 3-2-2-유형15-3
def division322_Stem_062():
    stem = "두 나눗셈의 나머지의 합을 구하시오.\n$$표$$ $$수식$$`{sa}`div`{sb}`$$/수식$$ $$/표$$  $$표$$ $$수식$$`{sc}`div`{sd}`$$/수식$$ $$/표$$\n"
    answer = "(답): $$수식$$`{a1}`$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`div`{sb}`=`{a}`CDOTS`{b}`$$/수식$$, $$수식$$`{sc}`div`{sd}`=`{c}`CDOTS`{d}`$$/수식$$\n" \
              "$$수식$$`LEFT ($$/수식$$두 나눗셈의 나머지의 합$$수식$$RIGHT )`=`{b}`+`{d}`=`{e}`$$/수식$$\n\n"


    while True:
        sb = np.random.randint(2, 10)
        a = np.random.randint(11, 100)
        b = np.random.randint(1, sb)
        sa = np.random.randint(101, 892)
        if (sb * a + b) == sa:
            break

    while True:
        sd = np.random.randint(2, 10)
        c = np.random.randint(102, 200)
        d = np.random.randint(1, sd)
        sc = np.random.randint(125, 999)

        if (sd * c + d == sc) & (sc != sa):
            break

    e = b + d

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(a1=e)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, a=a, b=b, c=c, d=d, e=e)

    return stem, answer, comment
























# 3-2-2-유형15-4
def division322_Stem_063():
    stem = "나머지가 가장 작은 나눗셈을 고르시오.\n{circle_one} $$수식$${sa}`div`{sb}`$$/수식$$\n{circle_two} $$수식$${sc}`div`{sd}`$$/수식$$\n{circle_three} $$수식$${se}`div`{sf}`$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "① $$수식$${sa}`div`{sb}`=`{a}`CDOTS`{b}`$$/수식$$\n" \
              "② $$수식$${sc}`div`{sd}`=`{c}`CDOTS`{d}`$$/수식$$\n" \
              "③ $$수식$${se}`div`{sf}`=`{e}`CDOTS`{f}`$$/수식$$\n\n"


    while True:
        sb = np.random.randint(2, 10)
        a = np.random.randint(11, 100)
        b = np.random.randint(1, sb)
        sa = np.random.randint(101, 892)

        if sb * a + b == sa:
            break

    while True:
        sd = np.random.randint(2, 10)
        c = np.random.randint(11, 200)
        d = np.random.randint(1, sd)
        sc = np.random.randint(125, 999)

        if (sd * c + d == sc) & (sc != sa) & (sd != sb) & (d != b):
            break

    while True:
        sf = np.random.randint(2, 10)
        e = np.random.randint(11, 100)
        f = np.random.randint(1, sf)
        se = np.random.randint(101, 892)

        if (sf * e + f == se) & (se != sa) & (se != sc) & (sf != sb) & (sf != sd) & (f != b) & (f != d):
            break

    ans = min(b, d, f)
    candidates = [b, d, f]

    correct_idx = 0
    for idx, sdx in enumerate(candidates):
        if sdx == ans:
            correct_idx = idx
            break

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, circle_one=circle_one, circle_two=circle_two, circle_three=circle_three)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, sf=sf, a=a, b=b, c=c, d=d, e=e, f=f)

    return stem, answer, comment



























# 3-2-2-유형15-5
def division322_Stem_064():
    stem = "㉠과 ㉡에 알맞은 수의 합을 구하시오.\n$$수식$$`{sa}`div`{sb}`=`$$/수식$$㉠$$수식$$`CDOTS`{b}`$$/수식$$, $$수식$$`{sc}`div`{sd}`=`{c}`CDOTS`$$/수식$$㉡\n"
    answer = "(답): $$수식$$`{a1}`$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}`div`{sb}`=`{a}`CDOTS`{b}`$$/수식$$ → ㉠$$수식$$`=`{a}`$$/수식$$\n" \
              "$$수식$${sc}`div`{sd}`=`{c}`CDOTS`{d}`$$/수식$$ → ㉡$$수식$$`=`{d}`$$/수식$$\n" \
              "따라서 ㉠$$수식$$`+`$$/수식$$㉡$$수식$$`=`{a}`+`{d}`=`{e}`$$/수식$$ 입니다.\n\n"


    while True:
        sb = np.random.randint(2, 10)
        a = np.random.randint(102, 200)
        b = np.random.randint(1, sb)
        sa = np.random.randint(125, 999)

        if sb * a + b == sa:
            break

    while True:
        sd = np.random.randint(2, 10)
        c = np.random.randint(102, 200)
        d = np.random.randint(1, sd)
        sc = np.random.randint(125, 999)

        if (sd * c + d == sc) & (sc != sa) & (sd != sb) & (d != b):
            break


    e = a + d

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, b=b, c=c)
    answer = answer.format(a1=e)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, a=a, b=b, c=c, d=d, e=e)

    return stem, answer, comment






















# 3-2-2-유형16-1
def division322_Stem_065():
    stem = "{s} $$수식$${sa}$$/수식$$장을 $$수식$${sb}$$/수식$$명에게 똑같이 나누어 주려고 합니다. 한 명에게 {s}를 몇 장씩 나누어 줄 수 있습니까?\n"
    answer = "(답): $$수식$${a1}$$/수식$$장\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`div`{sb}`=`{sc}`$$/수식$$이므로\n" \
              "한 명에게 {s}를 $$수식$${sc}$$/수식$$장씩 나누어 줄 수 있습니다.\n\n"


    s = ["도화지", "색도화지", "색종이", "한지"][np.random.randint(0, 4)]

    while True:
        sb = np.random.randint(2, 10)
        sc = np.random.randint(11, 100)
        sa = sb * sc
        if (sa >= 101) & (sa <= 891):
            break

    stem = stem.format(s=s, sa=sa, sb=sb)
    answer = answer.format(a1=sc)
    comment = comment.format(s=s, sa=sa, sb=sb, sc=sc)

    return stem, answer, comment

























# 3-2-2-유형16-2
def division322_Stem_066():
    stem = "길이가 $$수식$${sa} rm {{cm}}$$/수식$$인 {s}{j1} 한 도막이 $$수식$${sb} rm {{cm}}$$/수식$$가 되도록 자르려고 합니다. $$수식$${sb} rm {{cm}}$$/수식$$짜리 도막은 몇 개까지 만들 수 있고 남는 {s}{j2} 몇 $$수식$$rm {{cm}}$$/수식$$입니까?\n"
    answer = "(답): $$수식$${sc}$$/수식$$개, $$수식$${sd} rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$이므로 \n" \
              "$$수식$${sb} rm {{cm}}$$/수식$$짜리 도막은 $$수식$${sc}$$/수식$$개까지 만들 수 있고 남는 {s}{j2} $$수식$${sd} rm {{cm}}$$/수식$$ 입니다.\n\n"


    s = ["끈", "철사", "종이테이프", "노끈"][np.random.randint(0, 4)]

    j1 = proc_jo(s, 1)
    j2 = proc_jo(s, -1)

    while True:
        sb = np.random.randint(2, 10)
        sc = np.random.randint(102, 200)
        sd = np.random.randint(1, sb)
        sa = np.random.randint(125, 999)

        if sb * sc + sd == sa:
            break


    stem = stem.format(sa=sa, s=s, j1=j1, sb=sb, j2=j2)
    answer = answer.format(sc=sc, sd=sd)
    comment = comment.format(s=s, sa=sa, sb=sb, sc=sc, sd=sd, j2=j2)

    return stem, answer, comment



























# 3-2-2-유형16-3
def division322_Stem_067():
    stem = "{p}네 과수원에서 수확한 {s}{j1} $$수식$${sa}rm kg$$/수식$$입니다. 이 {s}{j2} 한 상자에 $$수식$${sb}rm kg$$/수식$$씩 포장하여 판다면 몇 상자까지 팔 수 있습니까?\n"
    answer = "(답): $$수식$${a1}$$/수식$$상자\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$이므로 \n" \
              "수확한 {s}{j2} $$수식$${sb}rm kg$$/수식$$씩 포장하면 $$수식$${sc}$$/수식$$상자가 되고 $$수식$${sd}rm kg$$/수식$$이 남습니다.\n" \
              "따라서 {s}{j2} $$수식$${sc}$$/수식$$상자까지 팔 수 있습니다.\n\n"


    p = ["지희", "호아", "시우", "재하", "윤서", "율희", "홍기", "준표", "혁재", "경미", "보라", "연주"][np.random.randint(0, 12)]
    s = ["포도", "딸기", "사과", "복숭아", "귤"][np.random.randint(0, 5)]

    j1 = proc_jo(s, -1)
    j2 = proc_jo(s, 1)

    while True:
        sb = np.random.randint(2, 10)
        sc = np.random.randint(11, 100)
        sd = np.random.randint(1, sb)
        sa = np.random.randint(101, 892)

        if sb * sc + sd == sa:
            break


    stem = stem.format(p=p, sa=sa, sb=sb, s=s, j1=j1, j2=j2)
    answer = answer.format(a1=sc)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, s=s, j2=j2)

    return stem, answer, comment



























# 3-2-2-유형16-4
def division322_Stem_068():
    stem = "{q1} {s} $$수식$${sd}$$/수식$$개와 {q2} {s} $$수식$${se}$$/수식$$개가 있습니다. 이 {s}{j1} $$수식$${sb}$$/수식$$상자에 똑같이 나누어 담으려면 한 상자에 몇 개씩 담아야 합니까?\n"
    answer = "(답): $$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$전체 {s} 수$$수식$$RIGHT )`=`{sd}`+`{se}`=`{sa}`LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$한 상자에 담아야 하는 {s} 수$$수식$$RIGHT )`=`{sa}`div`{sb}`=`{sc}`LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"


    while True:
        q1 = ["빨간색", "파란색", "보라색", "노란색", "초록색"][np.random.randint(0, 5)]
        q2 = ["빨간색", "파란색", "보라색", "노란색", "초록색"][np.random.randint(0, 5)]

        if q1 != q2:
            break

    s = ["구슬", "공깃돌", "클립"][np.random.randint(0, 3)]
    j1 = proc_jo(s, 1)


    while True:
        sb = np.random.randint(5, 10)
        sc = np.random.randint(56, 99)
        sa = sb * sc
        if sa % 2 == 0:
            if (sa >= 490) & (sa <= 882):
                break


    a = np.random.randint(51, 100)

    sd = round(sa/2) - a
    se = round(sa/2) + a

    stem = stem.format(q1=q1, q2=q2, s=s, j1=j1, sb=sb, sd=sd, se=se)
    answer = answer.format(a1=sc)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, s=s)

    return stem, answer, comment


























# 3-2-2-유형16-5
def division322_Stem_069():
    stem = "길이가 $$수식$${sa}rm m$$/수식$$인 도로의 한쪽에 처음부터 끝까지 {s}{j1} 심으려고 합니다. $$수식$${sb}rm m$$/수식$$ 간격으로 {s}{j1} 심는다면 {s}{j2} 모두 몇 그루가 필요합니까?\n"
    answer = "(답): $$수식$${a1}$$/수식$$그루\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$간격 수$$수식$$RIGHT )`=`{sa}`div`{sb}`=`{sc}`LEFT ($$/수식$$군데$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$도로 한쪽에 심는 {s} 수$$수식$$RIGHT )`=`LEFT ($$/수식$$간격 수$$수식$$RIGHT )`+`1`$$/수식$$ $$수식$$\n ={sc}`+`1`=`{sd}`LEFT ($$/수식$$그루$$수식$$RIGHT )$$/수식$$\n\n"


    s = ["나무", "가로수", "무궁화", "은행나무"][np.random.randint(0, 4)]

    j1 = proc_jo(s, 1)
    j2 = proc_jo(s, -1)

    while True:
        sb = np.random.randint(5, 10)
        sc = np.random.randint(102, 200)
        sa = sb * sc
        if (sa >= 125) & (sa <= 998):
            break

    sd = sc + 1

    stem = stem.format(s=s, j1=j1, sa=sa, sb=sb, j2=j2)
    answer = answer.format(a1=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, s=s)

    return stem, answer, comment
















# 3-2-2-유형17-1
def division322_Stem_070():
    stem = "{s} $$수식$${sa}$$/수식$$개를 모두 봉지에 나누어 담으려고 합니다. 한 봉지에 {s}{j1} $$수식$${sb}$$/수식$$개까지 담을 수 있을 때 봉지는 적어도 몇 봉지 필요합니까?\n"
    answer = "(답): $$수식$${a1}$$/수식$$봉지\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$이므로 \n" \
              "{s}{j1} $$수식$${sb}$$/수식$$개씩 $$수식$${sc}$$/수식$$봉지에 담으면 $$수식$${sd}$$/수식$$개가 남습니다. " \
              "남은 {s} $$수식$${sd}$$/수식$$개도 담아야 하므로 봉지는 적어도 $$수식$$`{sc}`+`1`=`{se}LEFT (`$$/수식$$봉지$$수식$$`RIGHT )`$$/수식$$필요합니다.\n\n"


    s = ["감", "귤", "토마토", "당근", "오이"][np.random.randint(0, 5)]

    j1 = proc_jo(s, 1)

    while True:
        sb = np.random.randint(3, 10)
        sc = np.random.randint(11, 40)
        sd = np.random.randint(1, sb)
        sa = np.random.randint(31, 99)

        if sa == sb * sc + sd:
            break

    se = sc + 1

    stem = stem.format(s=s, sa=sa, sb=sb, j1=j1)
    answer = answer.format(a1=se)
    comment = comment.format(s=s, sa=sa, sb=sb, sc=sc, sd=sd, se=se, j1=j1)

    return stem, answer, comment





















# 3-2-2-유형17-2
def division322_Stem_071():
    stem = "{p}{jp} 전체 쪽수가 $$수식$${sa}$$/수식$$쪽인 {s}{js} 모두 읽으려고 합니다. 하루에 $$수식$${sb}$$/수식$$쪽씩 읽으면 다 읽는 데 며칠이 걸립니까?\n"
    answer = "(답): $$수식$${se}$$/수식$$일\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$이므로\n"\
              "하루에 $$수식$${sb}$$/수식$$쪽씩 $$수식$${sc}$$/수식$$일을 읽으면 $$수식$${sd}$$/수식$$쪽이 남습니다.\n"\
              "따라서 {s}{js} 다 읽는 데 $$수식$$`{sc}`+`1`=`{se} LEFT (`$$/수식$$일$$수식$$`RIGHT )`$$/수식$$이 걸립니다.\n\n"


    p = ["은호", "은지", "지우", "미래"][np.random.randint(0, 4)]
    s = ["위인전", "소설책", "동화 시리즈"][np.random.randint(0, 3)]

    jp = proc_jo(p, -1)
    js = proc_jo(s, 1)

    while True:
        sb = np.random.randint(3, 10)
        sc = np.random.randint(12, 40)
        sd = np.random.randint(1, sb)
        sa = np.random.randint(101, 299)

        if sb * sc + sd == sa:
            break


    se = sc + 1

    stem = stem.format(sa=sa, s=s, jp=jp, sb=sb, js=js, p=p)
    answer = answer.format(se=se)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, s=s, js=js)

    return stem, answer, comment

























# 3-2-2-유형17-3
def division322_Stem_072():
    stem = "{p}이가 $$수식$$`1rm kg$$/수식$$짜리 {s} $$수식$${sa}$$/수식$$개를 체육관으로 옮기려고 합니다. {p}이는 한 번에 $$수식$${sb}rm kg$$/수식$$까지 옮길 수 있을 때, {s}{j1} 모두 옮기려면 {s}{j1} 들고 적어도 몇 번 움직여야 합니까?\n"
    answer = "(답): $$수식$${se}$$/수식$$번\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$이므로\n"\
              "{s}{j1} $$수식$${sb}rm kg$$/수식$$씩 $$수식$${sc}$$/수식$$번 옮기면 $$수식$${sd}rm kg$$/수식$$이 남습니다. " \
              "남은 {s} $$수식$${sd}rm kg$$/수식$$도 옮겨야 하므로 {p}이는 적어도 $$수식$$`{sc}`+`1`=`{se} LEFT (`$$/수식$$번$$수식$$`RIGHT )`$$/수식$$ 움직여야 합니다.\n\n"


    p = ["지선", "서준", "도윤", "민준", "은혁", "하율", "현민", "준섭", "태준", "대원", "애란", "수연", "미진"][np.random.randint(0, 13)]
    s = ["모래주머니", "야구방망이", "아령", "운동 기구"][np.random.randint(0, 4)]

    j1 = proc_jo(s, 1)

    while True:
        sb = np.random.randint(3, 9)
        sc = np.random.randint(12, 30)
        sd = np.random.randint(1, sb)
        sa = np.random.randint(31, 99)

        if sb * sc + sd == sa:
            break

    se = sc + 1

    stem = stem.format(sa=sa, s=s, j1=j1, sb=sb, p=p)
    answer = answer.format(se=se)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, s=s, j1=j1, p=p)

    return stem, answer, comment















# 3-2-2-유형18-1
def division322_Stem_073():
    stem = "$$수식$$`3`$$/수식$$장의 수 카드를 한 번씩 사용하여 몫이 가장 큰 $$수식$$`LEFT ($$/수식$$두 자리 수$$수식$$`RIGHT )`div`LEFT (`$$/수식$$한 자리 수$$수식$$`RIGHT )$$/수식$$의 나눗셈을 만들었습니다. 만든 나눗셈의 몫과 나머지를 차례로 쓰시오.\n$$수식$$LEFT ( {s1} RIGHT )$$/수식$$, $$수식$$LEFT ( {s2} RIGHT )$$/수식$$, $$수식$$LEFT ( {s3} RIGHT )$$/수식$$\n"
    answer = "(답): $$수식$${sc}$$/수식$$, $$수식$${sd}$$/수식$$\n"
    comment = "(해설)\n" \
              "몫이 가장 큰 나눗셈을 만들려면 나누어지는 수는 가장 크게, 나누는 수는 가장 작게 해야 합니다.\n" \
              "만들 수 있는 가장 큰 두 자리 수 : $$수식$$`{sa}`$$/수식$$\n" \
              "가장 작은 수 카드의 수 : $$수식$$`{sb}`$$/수식$$\n" \
              "→ $$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$\n\n"


    while True:
        a = np.random.randint(2, 10)
        b = np.random.randint(2, 10)
        c = np.random.randint(2, 10)

        if a < b < c:
            sa = 10 * c + b
            if sa % a != 0:
                sb = a
                sc = round(sa / sb)
                sd = sa - (sc * sb)
                if sd > 1:
                    break

    candidates = [a, b, c]
    np.random.shuffle(candidates)
    s1, s2, s3 = candidates

    stem = stem.format(s1=s1, s2=s2, s3=s3)
    answer = answer.format(sc=sc, sd=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd)

    return stem, answer, comment























# 3-2-2-유형18-2
def division322_Stem_074():
    stem = "$$수식$$`4`$$/수식$$장의 수 카드 중 $$수식$$`3`$$/수식$$장을 골라 한 번씩 사용하여 몫이 가장 큰 $$수식$$`LEFT ($$/수식$$두 자리 수$$수식$$`RIGHT )`div`LEFT ($$/수식$$한 자리 수$$수식$$RIGHT )$$/수식$$의 나눗셈을 만들었습니다. 만든 나눗셈의 몫과 나머지를 차례로 쓰시오.\n$$수식$$LEFT ( {s1} RIGHT )$$/수식$$, $$수식$$LEFT ( {s2} RIGHT )$$/수식$$, $$수식$$LEFT ( {s3} RIGHT )$$/수식$$, $$수식$$LEFT ( {s4} RIGHT )$$/수식$$\n"
    answer = "(답): $$수식$${sc}$$/수식$$, $$수식$${sd}$$/수식$$\n"
    comment = "(해설)\n" \
              "몫이 가장 큰 나눗셈을 만들려면 나누어지는 수는 가장 크게, 나누는 수는 가장 작게 해야 합니다.\n" \
              "만들 수 있는 가장 큰 두 자리 수 : $$수식$$`{sa}`$$/수식$$\n" \
              "가장 작은 수 카드의 수 : $$수식$$`{sb}`$$/수식$$\n" \
              "→ $$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$\n\n"


    while True:
        a = np.random.randint(2, 10)
        b = np.random.randint(2, 10)
        c = np.random.randint(2, 10)
        d = np.random.randint(2, 10)

        if a < b < c < d:
            sa = 10 * d + c
            if sa % a != 0:
                sb = a
                sc = round(sa / sb)
                sd = sa - (sb * sc)
                if sd > 1:
                    break

    candidates = [a, b, c, d]
    np.random.shuffle(candidates)
    s1, s2, s3, s4 = candidates

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4)
    answer = answer.format(sc=sc, sd=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd)

    return stem, answer, comment



























# 3-2-2-유형18-3
def division322_Stem_075():
    stem = "$$수식$$`4`$$/수식$$장의 수 카드를 한 번씩 사용하여 몫이 가장 큰 $$수식$$LEFT ($$/수식$$세 자리 수$$수식$$RIGHT )`div`LEFT ($$/수식$$한 자리 수$$수식$$RIGHT )$$/수식$$의 나눗셈을 만들었습니다. 만든 나눗셈의 몫과 나머지를 차례로 쓰시오.\n$$수식$$LEFT ( {s1} RIGHT )$$/수식$$, $$수식$$LEFT ( {s2} RIGHT )$$/수식$$, $$수식$$LEFT ( {s3} RIGHT )$$/수식$$, $$수식$$LEFT ( {s4} RIGHT )$$/수식$$\n"
    answer = "(답): $$수식$${sc}$$/수식$$, $$수식$${sd}$$/수식$$\n"
    comment = "(해설)\n" \
              "몫이 가장 큰 나눗셈을 만들려면 나누어지는 수는 가장 크게, 나누는 수는 가장 작게 해야 합니다.\n" \
              "만들 수 있는 가장 큰 세 자리 수 : $$수식$$`{sa}`$$/수식$$\n" \
              "가장 작은 수 카드의 수 : $$수식$$`{sb}`$$/수식$$\n" \
              "→ $$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$\n\n"


    while True:
        d = np.random.randint(2, 10)
        c = np.random.randint(2, 10)
        b = np.random.randint(2, 10)
        a = np.random.randint(2, 10)

        if a < b < c < d:
            #sorting = sorted([a, b, c, d])
            #a, b, c, d = sorting
            sa = 100 * d + 10 * c + b
            if sa % a != 0:
                sb = a
                sc = round(sa / sb)
                sd = sa - (sb * sc)
                if sd > 1:
                    break


    candidates = [a, b, c, d]
    np.random.shuffle(candidates)
    s1, s2, s3, s4 = candidates


    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4)
    answer = answer.format(sc=sc, sd=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd)


    return stem, answer, comment




























# 3-2-2-유형18-4
def division322_Stem_076():
    stem = "$$수식$$`3`$$/수식$$장의 수 카드를 한 번씩 사용하여 몫이 가장 작은 $$수식$$LEFT ($$/수식$$두 자리 수$$수식$$RIGHT )`div`LEFT ($$/수식$$한 자리 수$$수식$$RIGHT )$$/수식$$의 나눗셈을 만들었습니다. 만든 나눗셈의 몫과 나머지를 차례로 쓰시오.\n$$수식$$LEFT ( {s1} RIGHT )$$/수식$$, $$수식$$LEFT ( {s2} RIGHT )$$/수식$$, $$수식$$LEFT ( {s3} RIGHT )$$/수식$$\n"
    answer = "(답): $$수식$${sc}$$/수식$$, $$수식$${sd}$$/수식$$\n"
    comment = "(해설)\n" \
              "몫이 가장 작은 나눗셈을 만들려면 나누어지는 수는 가장 작게, 나누는 수는 가장 크게 해야 합니다.\n" \
              "만들 수 있는 가장 작은 두 자리 수 : $$수식$$`{sa}`$$/수식$$\n" \
              "가장 큰 수 카드의 수 : $$수식$$`{sb}`$$/수식$$\n" \
              "→ $$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$\n\n"


    while True:
        a = np.random.randint(2, 10)
        b = np.random.randint(2, 10)
        c = np.random.randint(2, 10)

        if a < b < c:
            sa = 10 * a + b
            if sa % a != 0:
                sb = c
                sc = round(sa / sb)
                sd = sa - (sc * sb)
                if sd > 1:
                    break


    candidates = [a, b, c]
    np.random.shuffle(candidates)
    s1, s2, s3 = candidates

    stem = stem.format(s1=s1, s2=s2, s3=s3)
    answer = answer.format(sc=sc, sd=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd)

    return stem, answer, comment
    












# 3-2-2-유형19-1
def division322_Stem_077():
    stem = "어떤 수를 $$수식$$`{sb}`$$/수식$$로 나누어야 할 것을 잘못하여 어떤 수에 $$수식$$`{sb}`$$/수식$${j1} 곱했더니 $$수식$$`{se}`$$/수식$${j2} 되었습니다. 바르게 계산한 몫과 나머지를 차례로 쓰시오.\n"
    answer = "(답): $$수식$${sc}$$/수식$$, $$수식$${sd}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □로 놓으면 □$$수식$$`times`{sb}`=`{se}`$$/수식$$ → $$수식$$`{se}`div`{sb}`=`$$/수식$$□, □$$수식$$`=`{sa}`$$/수식$$\n" \
              "바른 계산 : $$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$\n\n"


    while True:
        sb = np.random.randint(2, 10)
        sc = np.random.randint(4, 10)
        sd = np.random.randint(1, sb)

        se = np.random.randint(29, 100)
        sa = round(se/sb)

        if se % sb == 0 and 11 <= se/sb:
            if sb * sc + sd == sa:
                break


    j1 = proc_jo(sb, 1)
    j2 = proc_jo(se, 0)

    stem = stem.format(sb=sb, se=se, j1=j1, j2=j2)
    answer = answer.format(sc=sc, sd=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)

    return stem, answer, comment



















# 3-2-2-유형19-2
def division322_Stem_078():
    stem = "어떤 수를 $$수식$$`{sb}`$$/수식$$로 나누어야 할 것을 잘못하여 어떤 수에 $$수식$$`{sb}`$$/수식$${j1} 더했더니 $$수식$$`{se}`$$/수식$${j2} 되었습니다. 바르게 계산한 몫과 나머지를 차례로 쓰시오.\n"
    answer = "(답): $$수식$${sc}$$/수식$$, $$수식$${sd}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □로 놓으면 □$$수식$$`+`{sb}`=`{se}`$$/수식$$ → $$수식$$`{se}`-`{sb}`=`$$/수식$$□, □$$수식$$`=`{sa}`$$/수식$$\n" \
              "바른 계산 : $$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$\n\n"


    while True:
        sb = np.random.randint(5, 10)
        sc = np.random.randint(4, 10)
        sd = np.random.randint(1, sb)

        se = np.random.randint(29, 100)
        sa = se - sb

        if sb * sc + sd == sa:
            break

    j1 = proc_jo(sb, 1)
    j2 = proc_jo(se, 0)

    stem = stem.format(sb=sb, se=se, j1=j1, j2=j2)
    answer = answer.format(sc=sc, sd=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)

    return stem, answer, comment






















# 3-2-2-유형19-3
def division322_Stem_079():
    stem = "어떤 수를 $$수식$$`{sb}`$$/수식$$로 나누어야 할 것을 잘못하여 어떤 수에 $$수식$$`{sb}`$$/수식$${j1} 뺏더니 $$수식$$`{se}`$$/수식$${j2} 되었습니다. 바르게 계산한 몫과 나머지를 차례로 쓰시오.\n"
    answer = "(답): $$수식$${sc}$$/수식$$, $$수식$${sd}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □로 놓으면 □$$수식$$`-`{sb}`=`{se}`$$/수식$$ → $$수식$$`{se}`+`{sb}`=`$$/수식$$□, □$$수식$$`=`{sa}`$$/수식$$\n" \
              "바른 계산 : $$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$\n\n"


    while True:
        sb = np.random.randint(5, 10)
        sc = np.random.randint(4, 10)
        sd = np.random.randint(1, sb)

        se = np.random.randint(29, 90)
        sa = se + sb

        if sb * sc + sd == sa:
            break

    j1 = proc_jo(sb, 1)
    j2 = proc_jo(se, 0)

    stem = stem.format(sb=sb, se=se, j1=j1, j2=j2)
    answer = answer.format(sc=sc, sd=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)

    return stem, answer, comment























# 3-2-2-유형19-4
def division322_Stem_080():
    stem = "$$수식$$`{sa}`$$/수식$${j1} 어떤 수로 나누어야 할 것을 잘못하여 $$수식$$`{sa}`$$/수식$$에서 어떤 수를 뺏더니 $$수식$$`{se}`$$/수식$${j2} 되었습니다. 바르게 계산한 몫과 나머지를 차례로 쓰시오.\n"
    answer = "(답): $$수식$${sc}$$/수식$$, $$수식$${sd}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □로 놓으면 $$수식$$`{sa}`-`$$/수식$$□$$수식$$`=`{se}`$$/수식$$ → $$수식$$`{sa}`-`{se}`=`$$/수식$$□$$수식$$`$$/수식$$, □$$수식$$`=`{sb}`$$/수식$$\n" \
              "바른 계산 : $$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$\n\n"


    while True:
        sb = np.random.randint(4, 10)
        sc = np.random.randint(4, 20)
        sd = np.random.randint(1, sb)

        se = np.random.randint(29, 90)
        sa = se + sb

        if sb * sc + sd == sa:
            break

    j1 = proc_jo(sb, 1)
    j2 = proc_jo(se, 0)

    stem = stem.format(sa=sa, se=se, j1=j1, j2=j2)
    answer = answer.format(sc=sc, sd=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)

    return stem, answer, comment























# 3-2-2-유형19-5
def division322_Stem_081():
    stem = "어떤 수를 $$수식$$`{sb}`$$/수식$$로 나누어야 할 것을 잘못하여 어떤 수에 $$수식$$`{sb}`$$/수식$${j1} 곱했더니 $$수식$$`{se}`$$/수식$${j2} 되었습니다. 바르게 계산한 몫과 나머지를 차례로 쓰시오.\n"
    answer = "(답): $$수식$${sc}$$/수식$$, $$수식$${sd}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □로 놓으면 □$$수식$$`times`{sb}`=`{se}`$$/수식$$ → $$수식$$`{se}`div`{sb}`=`$$/수식$$□, □$$수식$$`=`{sa}`$$/수식$$\n" \
              "바른 계산 : $$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$\n\n"


    while True:
        sb = np.random.randint(2, 10)
        sc = np.random.randint(11, 200)
        sd = np.random.randint(1, sb)

        se = np.random.randint(201, 999)
        sa = round(se/sb)

        if (se % sb == 0) and (101 <= se/sb):
            if sb * sc + sd == sa:
                break


    j1 = proc_jo(sb, 1)
    j2 = proc_jo(se, 0)

    stem = stem.format(sb=sb, se=se, j1=j1, j2=j2)
    answer = answer.format(sc=sc, sd=sd)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)

    return stem, answer, comment
















# 3-2-2-유형21-1
def division322_Stem_082():
    stem = "나눗셈을 맞게 계산했는지 확인하려고 합니다. ㉠, ㉡, ㉢에 알맞은 수를 차례로 쓰시오.\n$$표$$$$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$\n$$수식$$`LEFT [`$$/수식$$확인$$수식$$`RIGHT ]````{sb}`times`$$/수식$$㉠$$수식$$`=`{se}`$$/수식$$ → $$수식$$`{se}`+`$$/수식$$㉡$$수식$$`=`$$/수식$$㉢$$/표$$\n"
    answer = "(답): $$수식$${sc}$$/수식$$, $$수식$${sd}$$/수식$$, $$수식$${sa}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$에서 나누는 수는 $$수식$${sb}$$/수식$$이고 몫은 $$수식$${sc}$$/수식$$, 나머지는 $$수식$${sd}$$/수식$$입니다.\n" \
              "$$수식$$`{sb}`times`{sc}`=`{se}`$$/수식$$ → $$수식$$`{se}`+`{sd}`=`{sa}`$$/수식$$이므로 맞게 계산했습니다.\n\n"


    while True:
        sb = np.random.randint(3, 10)
        sc = np.random.randint(3, 10)
        sd = np.random.randint(1, sb)
        sa = np.random.randint(29, 100)

        if sb * sc + sd == sa:
            break

    se = sb * sc

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)
    answer = answer.format(sc=sc, sd=sd, sa=sa)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)

    return stem, answer, comment
























# 3-2-2-유형21-2
def division322_Stem_083():
    stem = "$$수식$$LEFT ($$/수식$$두 자리 수$$수식$$RIGHT )`div`LEFT ($$/수식$$한 자리 수$$수식$$RIGHT )$$/수식$$의 나눗셈을 하고 맞게 계산했는지 확인한 식이 다음과 같습니다. 계산한 나눗셈의 몫과 나머지를 차례로 쓰시오.\n$$수식$$`LEFT [`$$/수식$$확인$$수식$$`RIGHT ]````{sb}`times`{sc}`=`$$/수식$$㉠ → ㉠$$수식$$`+`{sd}`=`$$/수식$$㉡\n"
    answer = "(답): $$수식$${sc}$$/수식$$, $$수식$${sd}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$`{sb}`times`{sc}`=`{se}`$$/수식$$ → $$수식$$`{se}`+`{sd}`=`{sa}`$$/수식$$이므로\n" \
              "나누어지는 수 $$수식$$`{sa}`$$/수식$${j1} 나누는 수 $$수식$$`{sb}`$$/수식$${j2} 몫 $$수식$$`{sc}`$$/수식$$의 곱에 나머지 $$수식$$`{sd}`$$/수식$${j3} 더한 값과 같습니다.\n" \
              "따라서 계산한 나눗셈 식은 $$수식$$`{sa}`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$입니다.\n\n"


    while True:
        sb = np.random.randint(3, 10)
        sc = np.random.randint(11, 30)
        sd = np.random.randint(1, sb)
        sa = np.random.randint(49, 100)

        if sb * sc + sd == sa:
            break

    se = sb * sc

    j1 = proc_jo(sa, -1)
    j2 = proc_jo(sb, 2)
    j3 = proc_jo(sd, 1)

    stem = stem.format(sb=sb, sc=sc, sd=sd)
    answer = answer.format(sc=sc, sd=sd, sa=sa)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, j1=j1, j2=j2, j3=j3)

    return stem, answer, comment

















# 3-2-2-유형22-1
def division322_Stem_084():
    stem = "□ 안에 알맞은 수를 구하시오.\n□$$수식$$`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$\n"
    answer = "(답): $$수식$$`{sa}`$$/수식$$\n"
    comment = "(해설)\n" \
              "나누는 수가 $$수식$${sb}$$/수식$$이고 몫은 $$수식$${sc}$$/수식$$, 나머지는 $$수식$${sd}$$/수식$$입니다.\n" \
              "$$수식$$`{sb}`times`{sc}`=`{se}`$$/수식$$ → $$수식$$`{se}`+`{sd}`=`{sa}`$$/수식$$이므로 □$$수식$$`=`{sa}`$$/수식$$입니다.\n\n"


    while True:
        sb = np.random.randint(3, 10)
        sc = np.random.randint(3, 10)
        sd = np.random.randint(1, sb)

        if sb * sc >= 21 & sb * sc <= 79:
            break

    sa = sb * sc + sd
    se = sb * sc

    stem = stem.format(sb=sb, sc=sc, sd=sd)
    answer = answer.format(sa=sa)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)

    return stem, answer, comment





















# 3-2-2-유형22-2
def division322_Stem_085():
    stem = "어떤 수를 $$수식$$`{sb}`$$/수식$$로 나누었더니 몫이 $$수식$$`{sc}`$$/수식$$이고 나머지가 $$수식$$`{sd}`$$/수식$$였습니다. 어떤 수를 구하시오.\n"
    answer = "(답): $$수식$$`{sa}`$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □로 놓으면 나누는 수가 $$수식$${sb}$$/수식$$이고 몫이 $$수식$${sc}$$/수식$$, 나머지가 $$수식$${sd}$$/수식$$입니다.\n" \
              "$$수식$$`{sb}`times`{sc}`=`{se}`$$/수식$$ → $$수식$$`{se}`+`{sd}`=`{sa}`$$/수식$$이므로 □$$수식$$`=`{sa}`$$/수식$$입니다.\n\n"


    while True:
        sb = np.random.randint(3, 10)
        sc = np.random.randint(11, 30)
        sd = np.random.randint(1, sb)

        if sb * sc >= 41 & sb * sc <= 99:
            break

    sa = sb * sc + sd
    se = sb * sc

    stem = stem.format(sb=sb, sc=sc, sd=sd)
    answer = answer.format(sa=sa)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se)

    return stem, answer, comment
























# 3-2-2-유형22-3
def division322_Stem_086():
    stem = "{s} 한 줄을 $$수식$$`{sb}rm {{cm}}$$/수식$$씩 자르고 나니 $$수식$$`{sc}`$$/수식$$도막이 되고 $$수식$$`{sd}rm {{cm}}$$/수식$$가 남았습니다. 자르기 전의 {s}{j1} 몇 $$수식$$rm {{cm}}$$/수식$$입니까?\n"
    answer = "(답): $$수식$$`{sa}rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "자르기 전의 {s}의 길이를 어떤 수를 □$$수식$$rm {{cm}}$$/수식$$로 놓으면\n" \
              "□$$수식$$`div`{sb}`=`{sc}`CDOTS`{sd}`$$/수식$$이므로 나누는 수가 $$수식$${sb}$$/수식$$, 몫이 $$수식$${sc}$$/수식$$, 나머지가 $$수식$${sd}$$/수식$$입니다.\n" \
              "$$수식$$`{sb}`times`{sc}`=`{se}`$$/수식$$ → $$수식$$`{se}`+`{sd}`=`{sa}`$$/수식$$이므로 □$$수식$$`=`{sa}`$$/수식$$입니다.\n\n"


    s = ["가래떡", "털실", "철사", "노끈"][np.random.randint(0, 4)]
    j1 = proc_jo(s, -1)

    while True:
        sb = np.random.randint(3, 8)
        sc = np.random.randint(11, 30)
        sd = np.random.randint(1, sb)
        if sb * sc >= 41 and sb * sc <= 99:
            break


    sa = sb * sc + sd
    se = sb * sc

    stem = stem.format(sb=sb, sc=sc, sd=sd, s=s, j1=j1)
    answer = answer.format(sa=sa)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, se=se, s=s)

    return stem, answer, comment


























# 3-2-2-유형22-4
def division322_Stem_087():
    stem = "두 나눗셈식에서 같은 모양은 같은 수를 나타냅니다. ㉠에 알맞은 수를 구하시오.\n$$표$$ □$$수식$$`div`{a}`=`{b}`$$/수식$$\n□$$수식$$`div`{sb}`=`$$/수식$$㉠ $$/표$$\n"
    answer = "(답): $$수식$$`{sc}`$$/수식$$\n"
    comment = "(해설)\n" \
              "곱셈과 나눗셈의 관계를 이용하면 □$$수식$$`div`{a}`=`{b}`$$/수식$$ → $$수식$$`{a}`times`{b}`=`$$/수식$$□, □$$수식$$`=`{sa}`$$/수식$$\n" \
              "□$$수식$$`div`{sb}`=`$$/수식$$㉠에서 $$수식$$`{sa}`div`{sb}`=`{sc}`$$/수식$$이므로 ㉠$$수식$$`=`{sc}`$$/수식$$입니다.\n\n"


    while True:
        a = [4, 6, 8, 9][np.random.randint(0, 4)]
        b = np.random.randint(11, 26)
        sb = np.random.randint(2, 8)

        ablist = []

        for i in range(2, 8):
            if a*b % i == 0:
                ablist.append(i)

        if len(ablist) > 0:
            sb = ablist[np.random.randint(0, len(ablist))]
            if (b % a == 0) & (sb != a):
                break


    sa = a * b
    sc = round(sa / sb)

    stem = stem.format(sb=sb, a=a, b=b)
    answer = answer.format(sc=sc)
    comment = comment.format(sa=sa, sb=sb, sc=sc, a=a, b=b)

    return stem, answer, comment


















