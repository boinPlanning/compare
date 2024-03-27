import numpy as np
import math

answer_dict = {
    0 : "①",
    1 : "②",
    2 : "③",
    3 : "④",
    4 : "⑤"
}

answer_kodict={
    0 : "ㄱ",
    1 : "ㄴ",
    2 : "ㄷ",
    3 : "ㄹ",
    4 : "ㅁ"
}

answer_koonedict={
    0 : "㉠",
    1 : "㉡",
    2 : "㉢",
    3 : "㉣",
    4 : "㉤"
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




#2-1-1-01
def threedigits211_Stem_001():
    stem = "$$수식$${boxblank}$$/수식$$안에 알맞은 수를 써넣으세요.\n$$수식$$LEFT ( 1 RIGHT ) ```` 100$$/수식$$은 $$수식$${sa}$$/수식$$이 $$수식$${boxone}$$/수식$$개인 수입니다.\n$$수식$$LEFT ( 2 RIGHT ) $$/수식$$ $$수식$${boxtwo}$$/수식$$은 $$수식$${sb}$$/수식$$보다 $$수식$${sc}$$/수식$$ 큰 수입니다.\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "$$수식$$`LEFT ( `1` RIGHT ) ```` 100$$/수식$$은 $$수식$${sa}$$/수식$$이 $$수식$${sd}$$/수식$$개인 수입니다.\n" \
              "$$수식$$`LEFT ( `2` RIGHT ) ```` {sb}$$/수식$$보다 $$수식$${sc}$$/수식$$ 큰 수는 $$수식$$100$$/수식$$입니다.\n\n"

    one = "①"
    two = "②"

# (1)
    sa = [10, 20, 50][np.random.randint(0, 3)]
    if sa == 10:
        sd = 10
    elif sa == 20:
        sd = 5
    elif sa == 50:
        sd = 2

# (2)
    sc = np.random.randint(1, 11)
    sb = 100 - sc

    boxblank = "□"
    boxone = "BOX{````%s````}" % one
    boxtwo = "BOX{````%s````}" % two

    ans = "$$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$" % (sd, 100)

    stem = stem.format(sa=sa, sb=sb, sc=sc, boxblank=boxblank, boxone=boxone, boxtwo=boxtwo)
    answer = answer.format(ans=ans)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd)

    return stem, answer, comment




# 2-1-1-04
def threedigits211_Stem_002():
    stem = "{p}이는 한 묶음에 $$수식$${a}$$/수식$$개씩 들어 있는 {s}를 $$수식$$`{b}`$$/수식$$묶음 샀습니다. {p}이가 산 {s}는 모두 몇 장인가요?\n"
    answer = "(정답)\n$$수식$$`{ans}`$$/수식$$장\n"
    comment = "(해설)\n" \
              "$$수식$$`{a}`$$/수식$$이 $$수식$${b}$$/수식$$개이면 $$수식$$100$$/수식$$입니다.\n" \
              "따라서 {p}이가 산 {s}는 모두 $$수식$$100$$/수식$$장입니다.\n\n"

    p = ["형준", "민진", "수진", "소연", "민석"][np.random.randint(0, 5)]
    s = ["색종이", "도화지", "한지"][np.random.randint(0, 3)]

# (1)
    a = [10, 20, 50][np.random.randint(0, 3)]
    if a == 10:
        b = 10
    elif a == 20:
        b = 5
    elif a == 50:
        b = 2

    stem = stem.format(a=a, b=b, p=p, s=s)
    answer = answer.format(ans=100)
    comment = comment.format(a=a, b=b, p=p, s=s)

    return stem, answer, comment





# 2-1-1-05
def threedigits211_Stem_003():
    stem = "$$수식$${boxblank}$$/수식$$안에 들어갈 수가 다른 하나를 찾아 기호를 써 보세요.\n$$표$$ ㉠ {sa}\n㉡ {sb}\n㉢ {sc} $$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "㉠ {ca}\n" \
              "㉡ {cb}\n" \
              "㉢ {cc}\n" \
              "따라서 $$수식$${boxblank}$$/수식$$안에 들어갈 수가 다른 하나는 {ans}입니다.\n\n"

# (ㄱ)
    a = np.random.randint(91, 99)
    b = 99 - a

# (ㄴ), (ㄷ)
    while True:
        c = np.random.randint(6, 10)
        e = np.random.randint(6, 10)
        if c != e:
            break

    c = c * 10
    d = 100 - c
    e = e * 10
    f = 100 - e

    sa = "$$수식$$%d$$/수식$$보다 $$수식$$%d$$/수식$$ 큰 수는 $$수식$$%s$$/수식$$입니다." % (a, b, "□")
    sb = "$$수식$$%d$$/수식$$보다 $$수식$$%d$$/수식$$ 큰 수는 $$수식$$%s$$/수식$$입니다." % (c, d, "□")
    sc = "$$수식$$%d$$/수식$$보다 $$수식$$%d$$/수식$$ 큰 수는 $$수식$$%s$$/수식$$입니다." % (e, f, "□")

    ca = "$$수식$$%d$$/수식$$보다 $$수식$$%d$$/수식$$ 큰 수는 $$수식$$%d$$/수식$$입니다." % (a, b, 99)
    cb = "$$수식$$%d$$/수식$$보다 $$수식$$%d$$/수식$$ 큰 수는 $$수식$$%d$$/수식$$입니다." % (c, d, 100)
    cc = "$$수식$$%d$$/수식$$보다 $$수식$$%d$$/수식$$ 큰 수는 $$수식$$%d$$/수식$$입니다." % (e, f, 100)

    boxblank = "□"

    candidates = [[sa, ca], [sb, cb], [sc, cc]]
    ans = candidates[0]

    np.random.shuffle(candidates)

    [sa, ca], [sb, cb], [sc, cc] = candidates

    correct_idx = 0

    for i, s in enumerate(candidates):
        if s == ans:
            correct_idx = i
            break

    stem = stem.format(sa=sa, sb=sb, sc=sc, boxblank=boxblank)
    answer = answer.format(ans=answer_koonedict[correct_idx])
    comment = comment.format(ca=ca, cb=cb, cc=cc, ans=answer_koonedict[correct_idx], boxblank=boxblank)

    return stem, answer, comment





# 2-1-1-06
def threedigits211_Stem_004():
    stem = "$$수식$${boxblank}$$/수식$$안에 알맞은 수를 써넣으세요.\n$$수식$$LEFT ( 1 RIGHT ) ```` 100$$/수식$$이 $$수식$${a}$$/수식$$개이면 $$수식$${boxone}$$/수식$$입니다.\n$$수식$$LEFT ( 2 RIGHT ) ```` 100$$/수식$$이 $$수식$${c}$$/수식$$개이면 $$수식$${boxtwo}$$/수식$$입니다.\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1 RIGHT ) ```` 100$$/수식$$이 $$수식$${a}$$/수식$$개이면 $$수식$${b}$$/수식$$입니다.\n" \
              "$$수식$$LEFT ( 2 RIGHT ) ```` 100$$/수식$$이 $$수식$${c}$$/수식$$개이면 $$수식$${d}$$/수식$$입니다.\n\n"

    one = "①"
    two = "②"

    while True:
        a = np.random.randint(2, 10)
        c = np.random.randint(2, 10)
        if a != c:
            break

    b = 100 * a
    d = 100 * c

    boxblank = "□"
    boxone = "BOX{````%s````}" % one
    boxtwo = "BOX{````%s````}" % two

    ans = "$$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$" % (b, d)

    stem = stem.format(a=a, c=c, boxblank=boxblank, boxone=boxone, boxtwo=boxtwo)
    answer = answer.format(ans=ans)
    comment = comment.format(a=a, b=b, c=c, d=d)

    return stem, answer, comment



# 2-1-1-07
def threedigits211_Stem_005():
    stem = "다음 중 옳은 것을 모두 고르세요.\n① {sta}\n② {stb}\n③ {stc}\n④ {std}\n⑤ {ste}\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "$$수식$${ca}$$/수식$$\n" \
              "$$수식$${cb}$$/수식$$\n" \
              "$$수식$${cc}$$/수식$$\n\n"

    while True:
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10)
        tmp = b - a
        e = np.random.randint(1, 10)
        g = np.random.randint(1, 10)
        i = np.random.randint(1, 10)
        if (a < b) & (a != e) & (b != e):
            a = 100 * a
            b = 100 * b
            e = 100 * e
            if g != i:
                break

    # sa
    c = [tmp, tmp*10][np.random.randint(0, 2)]
    sa = "$$수식$$%d$$/수식$$은 $$수식$$%d$$/수식$$보다 $$수식$$%d$$/수식$$ 작은 수입니다." % (a, b, c)
    coa = "$$수식$$%d$$/수식$$은 $$수식$$%d$$/수식$$보다 $$수식$$%d$$/수식$$ 작은 수입니다." % (a, b, b-a)

    sb = "$$수식$$%d$$/수식$$는 $$수식$$%d$$/수식$$보다 $$수식$$%d$$/수식$$ 큰 수 입니다." % (b, a, b - a)

    sc = "$$수식$$%d$$/수식$$는 $$수식$$100$$/수식$$이 $$수식$$%d$$/수식$$개인 수 입니다." % (e, e / 100)

    # sd
    h = [g, g*10][np.random.randint(0, 2)]
    sd = "$$수식$$100$$/수식$$이 $$수식$$%d$$/수식$$개이면 $$수식$$%d$$/수식$$입니다." % (g, h)
    cod = "$$수식$$100$$/수식$$이 $$수식$$%d$$/수식$$개이면 $$수식$$%d$$/수식$$입니다." % (g, 100 * g)

    # se
    j = [i, i*10][np.random.randint(0, 2)]
    se = "$$수식$$100$$/수식$$이 $$수식$$%d$$/수식$$개이면 $$수식$$%d$$/수식$$입니다." % (i, j)
    coe = "$$수식$$100$$/수식$$이 $$수식$$%d$$/수식$$개이면 $$수식$$%d$$/수식$$입니다." % (i, 100 * i)

    ans = [sb, sc]
    correct = [[sa, coa], [sd, cod], [se, coe]]
    candidates = [sa, sb, sc, sd, se]
    np.random.shuffle(candidates)
    sta, stb, stc, std, ste = candidates

    correct_idx = []
    comment_idx = []
    com = []

    for i, s in enumerate(candidates):
        if s in ans:
            correct_idx.append(i)
        if s not in ans:
            comment_idx.append(i)
            com.append(s)

    ans = ""
    for i in correct_idx:
        ans = ans + "%s, " % (answer_dict[i])
    ans = ans[: -2]

    com_ans = ["a", "b", "c"]
    for i, s in enumerate(correct):
        for j, r in enumerate(com):
            if s[0] == r:
                com_ans[j] = s[1]

    ca = "%s %s" % (answer_dict[comment_idx[0]], com_ans[0])
    cb = "%s %s" % (answer_dict[comment_idx[1]], com_ans[1])
    cc = "%s %s" % (answer_dict[comment_idx[2]], com_ans[2])

    stem = stem.format(sta=sta, stb=stb, stc=stc, std=std, ste=ste)
    answer = answer.format(ans=ans)
    comment = comment.format(ca=ca, cb=cb, cc=cc)

    return stem, answer, comment




# 2-1-1-09
def threedigits211_Stem_006():
    stem = "㉠, ㉡, ㉢의 $$수식$${boxblank}$$/수식$$ 안에 들어갈 수 있는 수 중 가장 큰 것은 어느 것인가요?\n$$표$$㉠ {sa}\n㉡ {sb}\n㉢ {sc}$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${b}$$/수식$$ ㉡ $$수식$${d}$$/수식$$ ㉢ $$수식$${f}$$/수식$$\n" \
              "따라서 가장 큰 수는 {ans}입니다.\n\n"

# (ㄱ)
    b = np.random.randint(2, 10)
    a = b * 100

# (ㄴ), (ㄷ)
    while True:
        d = np.random.randint(2, 10)
        f = np.random.randint(2, 10)
        if d != f:
            break

    d = d * 10
    c = d * 10

    f = f * 10
    e = f * 10

    ans = max(d, f)

    sa = "$$수식$$%d$$/수식$$은 $$수식$$100$$/수식$$이 %s개입니다." % (a, "□")
    sb = "$$수식$$%d$$/수식$$은 $$수식$$10$$/수식$$이 %s개입니다." % (c, "□")
    sc = "$$수식$$%d$$/수식$$은 $$수식$$10$$/수식$$이 %s개입니다." % (e, "□")

    candidates = [[sa, b], [sb, d], [sc, f]]

    np.random.shuffle(candidates)

    [sa, b], [sb, d], [sc, f] = candidates

    correct_idx = 0

    for i, s in enumerate(candidates):
        if s[1] == ans:
            correct_idx = i
            break

    boxblank = "□"

    stem = stem.format(sa=sa, sb=sb, sc=sc, boxblank=boxblank)
    answer = answer.format(ans=answer_koonedict[correct_idx])
    comment = comment.format(b=b, d=d, f=f, ans=answer_koonedict[correct_idx])

    return stem, answer, comment





# 2-1-1-10
def threedigits211_Stem_007():
    stem = "$$수식$$10$$/수식$$원짜리 동전 $$수식$${a}$$/수식$$개는 $$수식$$100$$/수식$$원짜리 동전 몇 개와 같나요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$10$$/수식$$원짜리 동전 $$수식$${a}$$/수식$$개는 $$수식$${b}$$/수식$$원입니다.\n" \
              "$$수식$${b}$$/수식$$은 $$수식$$100$$/수식$$이 $$수식$${c}$$/수식$$개인 수입니다.\n" \
              "따라서 $$수식$$10$$/수식$$원짜리 동전 $$수식$${a}$$/수식$$개는 $$수식$$100$$/수식$$원짜리 동전 $$수식$${c}$$/수식$$개와 같습니다.\n\n"

    c = np.random.randint(2, 10)
    b = c * 100
    a = c * 10

    stem = stem.format(a=a)
    answer = answer.format(ans=c)
    comment = comment.format(a=a, b=b, c=c)

    return stem, answer, comment




# 2-1-1-12
def threedigits211_Stem_008():
    stem = "다음 수를 읽어 보세요.\n$$표$$ $$수식$$100$$/수식$$이 $$수식$${a}$$/수식$$개, $$수식$$10$$/수식$$이 $$수식$${b}$$/수식$$개, $$수식$$1$$/수식$$이 $$수식$${c}$$/수식$$개인 수 $$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "$$수식$$100$$/수식$$이 $$수식$${a}$$/수식$$개이면 $$수식$${ca}$$/수식$$, $$수식$$10$$/수식$$이 $$수식$${b}$$/수식$$개이면 $$수식$${cb}$$/수식$$," \
              " $$수식$$1$$/수식$$이 $$수식$${c}$$/수식$$개이면 $$수식$${cc}$$/수식$$이므로 $$수식$$100$$/수식$$이 $$수식$${a}$$/수식$$개, " \
              "$$수식$$10$$/수식$$이 $$수식$${b}$$/수식$$개, $$수식$$1$$/수식$$이 $$수식$${c}$$/수식$$개인 수는 $$수식$${sum}$$/수식$$입니다.\n" \
              "$$수식$${sum}$$/수식$$는 {read}{ii}라고 읽습니다.\n\n"

    a = np.random.randint(2, 10)
    b = np.random.randint(2, 10)
    c = np.random.randint(2, 10)

    ca = 100 * a
    cb = 10 * b
    cc = c
    sum = ca + cb + cc

    read_dict = {
        2: "이",
        3: "삼",
        4: "사",
        5: "오",
        6: "육",
        7: "칠",
        8: "팔",
        9: "구"
    }

    ra = read_dict[a]
    rb = read_dict[b]
    rc = read_dict[c]
    read = "%s백%s십%s" % (ra, rb, rc)
    ii = ""
    if (c == 3) or (c == 6) or (c == 7) or (c == 8) :
        ii = " 이"

    stem = stem.format(a=a, b=b, c=c)
    answer = answer.format(ans=read)
    comment = comment.format(a=a, b=b, c=c, ca=ca, cb=cb, cc=cc, sum = sum, read=read, ii=ii)

    return stem, answer, comment




# 2-1-1-13
def threedigits211_Stem_009():
    stem = "{p}이는 $$수식$$100$$/수식$$원짜리 동전 $$수식$${a}$$/수식$$개, $$수식$$50$$/수식$$원짜리 동전 $$수식$${b}$$/수식$$개, $$수식$$10$$/수식$$원짜리 동전 $$수식$${c}$$/수식$$개, $$수식$$1$$/수식$$원짜리 동전 $$수식$${d}$$/수식$$개를 가지고 있습니다. {p}이가 가지고 있는 돈은 모두 얼마인가요?\n"
    answer = "(정답)\n$$수식$$`{ans}`$$/수식$$원\n"
    comment = "(해설)\n" \
              "$$수식$$100$$/수식$$원짜리 동전 $$수식$${a}$$/수식$$개는 $$수식$${ca}$$/수식$$원, $$수식$$50$$/수식$$원짜리 동전 $$수식$${b}$$/수식$$개와 " \
              "$$수식$$10$$/수식$$원짜리 동전 $$수식$${c}$$/수식$$개는 {cb}원, $$수식$$1$$/수식$$원짜리 동전 $$수식$${d}$$/수식$$개는 $$수식$${cc}$$/수식$$원 ➡ " \
              "$$수식$${sum}$$/수식$$원\n\n"

    p = ["영진", "채원", "혜윤", "재훈", "은빈"][np.random.randint(0, 5)]

# (1)
    a = np.random.randint(2, 10)
    b = 1
    c = np.random.randint(1, 5)
    d = np.random.randint(2, 10)

    ca = a * 100
    cb = 50 + (c * 10)
    cc = d

    sum = ca + cb + cc

    stem = stem.format(a=a, b=b, c=c, d=d, p=p)
    answer = answer.format(ans=sum)
    comment = comment.format(a=a, b=b, c=c, d=d, ca=ca, cb=cb, cc=cc, sum=sum)

    return stem, answer, comment





# 2-1-1-14
def threedigits211_Stem_010():
    stem = "다음이 나타내는 수를 구해 보세요.\n$$표$$ $$수식$$100$$/수식$$이 $$수식$${a}$$/수식$$개, $$수식$$10$$/수식$$이 $$수식$${b}$$/수식$$개, $$수식$$1$$/수식$$이 $$수식$${c}$$/수식$$개인 수 $$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$100$$/수식$$이 $$수식$${a}$$/수식$$개이면 $$수식$${ca}$$/수식$$, $$수식$$10$$/수식$$이 $$수식$${b}$$/수식$$개이면 $$수식$${cb}$$/수식$$," \
              " $$수식$$1$$/수식$$이 $$수식$${c}$$/수식$$개이면 $$수식$${cc}$$/수식$$입니다.\n" \
              "따라서 나타내는 수는 $$수식$${sum}$$/수식$$입니다.\n\n"

# (ㄱ)
    a = np.random.randint(2, 10) # 백자리
    b = np.random.randint(2, 20)
    c = np.random.randint(2, 30)

    ca = 100 * a
    cb = 10 * b
    cc = c
    sum = ca + cb + cc

    stem = stem.format(a=a, b=b, c=c)
    answer = answer.format(ans=sum)
    comment = comment.format(a=a, b=b, c=c, ca=ca, cb=cb, cc=cc, sum = sum)

    return stem, answer, comment





# 2-1-1-15
def threedigits211_Stem_011():
    stem = "다음 중 일의 자리 숫자가 $$수식$${one}$$/수식$$인 수는 어느 것입니까?\n① $$수식$${a}$$/수식$$                ② $$수식$${b}$$/수식$$                ③ $$수식$${c}$$/수식$$\n④ $$수식$${d}$$/수식$$                ⑤ $$수식$${e}$$/수식$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "일의 자리 숫자를 각각 알아보면\n" \
              "① $$수식$${a}$$/수식$$ → $$수식$${onea}$$/수식$$          ② $$수식$${b}$$/수식$$ → $$수식$${oneb}$$/수식$$         ③ $$수식$${c}$$/수식$$ → $$수식$${onec}$$/수식$$\n" \
              "④ $$수식$${d}$$/수식$$ → $$수식$${oned}$$/수식$$          ⑤ $$수식$${e}$$/수식$$ → $$수식$${onee}$$/수식$$\n\n"

    while True:
        a = np.random.randint(100, 1000)
        onea = a % 10
        b = np.random.randint(100, 1000)
        oneb = b % 10
        c = np.random.randint(100, 1000)
        onec = c % 10
        d = np.random.randint(100, 1000)
        oned = d % 10
        e = np.random.randint(100, 1000)
        onee = e % 10

        if (onea != oneb) & (onea != onec) & (onea != oned) & (onea != onee) & (oneb != onec) & (oneb != oned) & (oneb != onee) & (onec != oned) & (onec != onee) & (oned != onee):
            break

    candidates = [[a, onea], [b, oneb], [c, onec], [d, oned], [e, onee]]
    ans = onea
    np.random.shuffle(candidates)

    [a, onea], [b, oneb], [c, onec], [d, oned], [e, onee] = candidates

    correct_idx = 0

    for i, s in enumerate(candidates):
        if s[1] == ans:
            correct_idx = i
            break

    stem = stem.format(a=a, b=b, c=c, d=d, e=e, one=ans)
    answer = answer.format(ans=answer_dict[correct_idx])
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, onea=onea, oneb=oneb, onec=onec, oned=oned, onee=onee)

    return stem, answer, comment




# 2-1-1-17
def threedigits211_Stem_012():
    stem = "백의 자리 숫자가 가장 작은 수를 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${a}$$/수식$$            ㉡ $$수식$${b}$$/수식$$            ㉢ $$수식$${c}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "백의 자리 숫자를 각각 알아보면\n" \
              "㉠ $$수식$${a}$$/수식$$ → $$수식$${ca}$$/수식$$\n" \
              "㉡ $$수식$${b}$$/수식$$ → $$수식$${cb}$$/수식$$\n" \
              "㉢ $$수식$${c}$$/수식$$ → $$수식$${cc}$$/수식$$\n" \
              "따라서 $$수식$${max}`&gt;`{mid}`&gt;`{min}`$$/수식$$이므로 백의 자리 숫자가 가장 작은 수는 {ans}입니다.\n\n"

    while True:
        a = np.random.randint(100, 1000)
        ca = a // 100
        b = np.random.randint(100, 1000)
        cb = b // 100
        c = np.random.randint(100, 1000)
        cc = c // 100
        if (ca != cb) & (ca != cc) & (cb != cc):
            break

    list = [ca, cb, cc]
    list = sorted(list)
    min, mid, max = list

    candidates = [[a, ca], [b, cb], [c, cc]]

    np.random.shuffle(candidates)

    [a, ca], [b, cb], [c, cc] = candidates

    correct_idx = 0

    for i, s in enumerate(candidates):
        if s[1] == min:
            correct_idx = i
            break

    stem = stem.format(a=a, b=b, c=c)
    answer = answer.format(ans=answer_koonedict[correct_idx])
    comment = comment.format(a=a, b=b, c=c, ca=ca, cb=cb, cc=cc, ans=answer_koonedict[correct_idx], max=max, mid=mid, min=min)

    return stem, answer, comment




# 2-1-1-18
def threedigits211_Stem_013():
    stem = "숫자 $$수식$${s}$$/수식$${j1} 나타내는 값이 가장 큰 수를 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${a}$$/수식$$                 ㉡ $$수식$${b}$$/수식$$\n㉢ $$수식$${c}$$/수식$$                 ㉣ $$수식$${d}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${a}$$/수식$$ → $$수식$${ca}$$/수식$$\n" \
              "㉡ $$수식$${b}$$/수식$$ → $$수식$${cb}$$/수식$$\n" \
              "㉢ $$수식$${c}$$/수식$$ → $$수식$${cc}$$/수식$$\n" \
              "㉣ $$수식$${d}$$/수식$$ → $$수식$${cd}$$/수식$$\n" \
              "따라서 나타내는 수가 가장 큰 수는 {ko} $$수식$${ans}$$/수식$$입니다.\n\n"

    s = np.random.randint(1, 10)

    while True:
        a = np.random.randint(100, 1000) # 백
        b = np.random.randint(100, 1000) # 십
        c = np.random.randint(100, 1000) # 십
        d = np.random.randint(100, 1000) # 일

        if (a != b) & (a != c) & (a != d) & (b != c) & (b != d) & (c != d):
            if (a // 100 == s) & ((b // 10) % 10 == s) & ((c // 10) % 10 == s) & (d % 10 == s) & ((b //100) != s) & ((c //100) != s) & ((d //100) != s) :
                break
    ans = a

    candidates = [[a, s*100], [b, s * 10], [c, s * 10], [d, s]]

    np.random.shuffle(candidates)

    [a, ca], [b, cb], [c, cc], [d, cd] = candidates

    j1 = proc_jo(s, 0)

    correct_idx = 0

    for i, enum in enumerate(candidates):
        if enum[0] == ans:
            correct_idx = i
            break

    stem = stem.format(a=a, b=b, c=c, d=d, s=s, j1=j1)
    answer = answer.format(a1=answer_koonedict[correct_idx])
    comment = comment.format(a=a, b=b, c=c, d=d, ca=ca, cb=cb, cc=cc, cd=cd, ko=answer_koonedict[correct_idx], ans=ans)

    return stem, answer, comment




# 2-1-1-20
def threedigits211_Stem_014():
    stem = "보기와 같이 나타내려고 합니다. 수확한 {p}는 모두 얼마인지 구해 보세요.\n$$표$$ 보기\n{p} $$수식$$100$$/수식$$개: ■\n{p} $$수식$$10$$/수식$$개: ★\n{p} $$수식$$1$$/수식$$개: ●$$/표$$\n$$표$$ $$수식$$LEFT [$$/수식$$수확한 {p}의 수$$수식$$RIGHT ]$$/수식$$\n{sa}{sb}{sc}$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "■가 $$수식$${a}$$/수식$$개, ★가 $$수식$${b}$$/수식$$개, ●가 $$수식$${c}$$/수식$$개 입니다.\n" \
              "$$수식$$100$$/수식$$ $$수식$${a}$$/수식$$개이면 $$수식$${ca}$$/수식$$, $$수식$$10$$/수식$$이 $$수식$${b}$$/수식$$개이면 $$수식$${cb}$$/수식$$, " \
              "$$수식$$1$$/수식$$이 $$수식$${c}$$/수식$$개이면 $$수식$${cc}$$/수식$$입니다.\n" \
              "→ $$수식$${ca}`+`{cb}`+`{cc}`=`{sum}`$$/수식$$\n" \
              "따라서 수확한 {p}는 모두 $$수식$${sum}$$/수식$$입니다.\n\n"


    p = ["옥수수", "사과", "오렌지", "바나나", "감자", "배", "배추", "양배추"][np.random.randint(0, 8)]
    boxblank = "□"

    a = np.random.randint(1, 10) # 백
    ca = 100 * a
    b = np.random.randint(1, 10)  # 십
    cb = 10 * b
    c = np.random.randint(1, 10)  # 일
    cc = c

    square = ""
    for i in range(a):
        square = square + "■"

    star = ""
    for i in range(b):
        square = square + "★"

    circle = ""
    for i in range(c):
        square = square + "●"

    sum = ca + cb + cc

    stem = stem.format(sa=square, sb=star, sc=circle, p=p, boxblank=boxblank)
    answer = answer.format(ans=sum)
    comment = comment.format(a=a, b=b, c=c, ca=ca, cb=cb, cc=cc, sum=sum, p=p)

    return stem, answer, comment




# 2-1-1-21
def threedigits211_Stem_015():
    stem = "다음 수에서 ㉠이 나타내는 값은 ㉡이 나타내는 값이 몇 개인 수인가요?\n$$표$$$$수식$${a}````{b}````{a}$$/수식$$\n㉠          ㉡$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠의 $$수식$${a}$$/수식$$은 백의 자리 숫자이므로 ㉠이 나타내는 값은 $$수식$${c}$$/수식$$입니다.\n" \
              "㉡의 $$수식$${a}$$/수식$$은 일의 자리 숫자이므로 ㉡이 나타내는 값은 $$수식$${a}$$/수식$$입니다.\n" \
              "따라서 $$수식$${c}$$/수식$$은 $$수식$${a}$$/수식$$이 $$수식$$100$$/수식$$개인 수이므로 ㉠이 나타내는 값은 ㉡이 나타내는 값 $$수식$$100$$/수식$$개인 수입니다.\n\n"

    a = np.random.randint(1, 10) # 백
    b = np.random.randint(1, 10)  # 십
    c = a * 100

    stem = stem.format(a=a, b=b)
    answer = answer.format(ans=100)
    comment = comment.format(a=a, b=b, c=c)

    return stem, answer, comment




# 2-1-1-22
def threedigits211_Stem_016():
    stem = "$$수식$$4$$/수식$$장의 수 카드 중에서 $$수식$$3$$/수식$$장을 뽑아 한 번씩만 사용하여 세 자리 수를 만들려고 합니다. 가장 큰 세 자리 수와 가장 작은 세 자리 수를 각각 만들어 보세요.\n$$수식$${boxa}$$/수식$$  $$수식$${boxb}$$/수식$$  $$수식$${boxc}$$/수식$$  $$수식$${boxd}$$/수식$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "$$수식$${ca}`&gt;`{cb}`&gt;`{cc}`&gt;`{cd}`$$/수식$$이므로 만들 수 있는 가장 큰 세 자리 수는 $$수식$${max}$$/수식$$이고 " \
              "만들 수 있는 가장 작은 세 자리 수는 $$수식$${min}$$/수식$$입니다.\n\n"

    while True:
        a = np.random.randint(0, 10) # 백
        b = np.random.randint(0, 10)  # 십
        c = np.random.randint(0, 10)  # 십
        d = np.random.randint(0, 10)  # 십
        if (a > b) and (b > c) and (c > d) :
            break

    ca = a
    cb = b
    cc = c
    cd = d

    max = (100 * a) + (10 * b) + c

    if d == 0:
        min = (100 * c)  + b
    else:
        min = (100 * d) + (10 * c) + b

    candidates = [a, b, c, d]

    np.random.shuffle(candidates)

    a, b, c, d = candidates

    ans = "$$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$" % (max, min)

    boxa = "BOX{````%d````}" % a
    boxb = "BOX{````%d````}" % b
    boxc = "BOX{````%d````}" % c
    boxd = "BOX{````%d````}" % d

    stem = stem.format(boxa=boxa, boxb=boxb, boxc=boxc, boxd=boxd)
    answer = answer.format(ans=ans)
    comment = comment.format(ca=ca, cb=cb, cc=cc, cd=cd, max=max, min=min)

    return stem, answer, comment




# 2-1-1-25
def threedigits211_Stem_017():
    stem = "뛰어서 센 규칙을 찾아 {boxblank}안에 알맞은 수를 써넣으세요.\n$$표$$ $$수식$$``{a}``$$/수식$$-$$수식$$``{b}``$$/수식$$-$$수식$$``{c}``$$/수식$$-$$수식$$``{d}``$$/수식$$-$$수식$$``{e}$$/수식$$ $$/표$$\n $$수식$${boxone}$$/수식$$ 씩 커집니다.\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "십의 자리 숫자가 $$수식$${ca}$$/수식$$씩 커지므로 $$수식$${cb}$$/수식$$씩 뛰어서 센 것입니다. → $$수식$${cb}$$/수식$$씩 커집니다.\n\n"

    boxblank = "□"
    boxone = "BOX{　　}"

    while True:
        ca = np.random.randint(1, 10) # 백
        cb = 10 * ca
        a = np.random.randint(100, 1000)  # 십

        if (a + (cb * 4)) < 1000 :
            break

    b = cb + a
    c = cb + b
    d = cb + c
    e = cb + d

    stem = stem.format(a=a, b=b, c=c, d=d, e=e, boxblank=boxblank, boxone=boxone)
    answer = answer.format(ans=cb)
    comment = comment.format(ca=ca, cb=cb, )

    return stem, answer, comment



# 2-1-1-28
def threedigits211_Stem_018():
    stem = "다음 중 나타내는 수가 다른 하나를 찾아 기호를 써 보세요.\n$$표$$㉠ {sa}\n㉡ {sb}\n㉢ {sc}$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "㉠ {ca}\n" \
              "㉡ {cb}\n" \
              "㉢ {cc}\n" \
              "따라서 나타내는 수가 다른 하나는 {ans}입니다.\n\n"

    while True:
        a = np.random.randint(11, 100)
        b = np.random.randint(11, 100)
        c = np.random.randint(101, 1000)
        if a != b:
            a = a * 10
            b = b * 10

            ra = ["큰", "작은"][np.random.randint(0, 2)]
            rb = ["큰", "작은"][np.random.randint(0, 2)]
            rc = ["큰", "작은"][np.random.randint(0, 2)]

            if ra == "큰":
                na = a + 100
            else:
                na = a - 100

            if rc == "큰":
                nc = c + 1
            else:
                nc = c - 1

            if na == nc:
                if rb == "큰":
                    nb = b + 10
                else:
                    nb = b - 10

                if nb != na:
                    break

    sa = "$$수식$$%d$$/수식$$보다 $$수식$$100$$/수식$$ %s 수" % (a, ra)
    sb = "$$수식$$%d$$/수식$$보다 $$수식$$10$$/수식$$ %s 수" % (b, rb)
    sc = "$$수식$$%d$$/수식$$보다 $$수식$$1$$/수식$$ %s 수" % (c, rc)

    candidates = [[sa, na], [sb, nb], [sc, nc]]
    ans = candidates[1][1]

    np.random.shuffle(candidates)

    [sa, na], [sb, nb], [sc, nc] = candidates
    ca = "%s: $$수식$$%d$$/수식$$" % (sa, na)
    cb = "%s: $$수식$$%d$$/수식$$" % (sb, nb)
    cc = "%s: $$수식$$%d$$/수식$$" % (sc, nc)

    correct_idx = 0

    for i, s in enumerate(candidates):
        if s[1] == ans:
            correct_idx = i
            break

    stem = stem.format(sa=sa, sb=sb, sc=sc)
    answer = answer.format(ans=answer_koonedict[correct_idx])
    comment = comment.format(ca=ca, cb=cb, cc=cc, ans=answer_koonedict[correct_idx])

    return stem, answer, comment




# 2-1-1-30
def threedigits211_Stem_019():
    stem = "세 자리 수인 암호를 $$수식$$1$$/수식$$개월마다 $$수식$${s}$$/수식$$씩 뛰어 세기를 하여 바꾸고 있습니다. 이번 달 암호가 $$수식$${a}$$/수식$$이라면 $$수식$$3$$/수식$$개월 전의 암호는 무엇이었는지 구하세요.\n$$수식$${boxblank}$$/수식$$$$수식$$-$$/수식$$$$수식$${boxblank}$$/수식$$$$수식$$-$$/수식$$$$수식$${boxblank}$$/수식$$$$수식$$-{a}$$/수식$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a}$$/수식$$부터 $$수식$${s}$$/수식$$씩 거꾸로 $$수식$$3$$/수식$$번 뛰어서 세면 $$수식$$``{a}``$$/수식$$-$$수식$$``{b}``$$/수식$$-$$수식$$``{c}``$$/수식$$-$$수식$$``{d}``$$/수식$$입니다.\n" \
              "따라서 $$수식$$3$$/수식$$개월 전의 암호는 $$수식$${d}$$/수식$$입니다.\n\n"

    blank = "````"
    boxblank = "BOX{　　　}"

    while True:
        ss = np.random.randint(1, 10)
        s = 10 * ss
        a = np.random.randint(100, 1000)
        if (a - (s * 3)) > 100:
            break

    b = a - s
    c = b - s
    d = c - s

    stem = stem.format(boxblank=boxblank, s=s, a=a)
    answer = answer.format(ans=d)
    comment = comment.format(a=a, b=b, c=c, d=d, s=s)

    return stem, answer, comment




# 2-1-1-32
def threedigits211_Stem_020():
    stem = "다음 수에서 $$수식$${s}$$/수식$$씩 $$수식$${n}$$/수식$$번 거꾸로 뛰어서 센 수를 구하세요.\n$$표$$$$수식$$3$$/수식$$장의 수 카드 $$수식$${fa}$$/수식$$, $$수식$${fb}$$/수식$$, $$수식$${fc}$$/수식$$를 한 번씩만 사용하여 만들 수 있는 가장 큰 세 자리 수 $$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${c}`&gt;`{b}`&gt;`{a}$$/수식$$이므로 만들 수 있는 가장 큰 세 자리 수는 $$수식$${num}$$/수식$$입니다.\n" \
              "➡ {com}\n\n"

    while True:
        ss = np.random.randint(1, 10)
        s = 10 * ss
        n = np.random.randint(3, 10)

        a = np.random.randint(0, 10)
        b = np.random.randint(0, 10)
        c = np.random.randint(0, 10)

        if (a != b) & (a != c) & (b != c):
            list = sorted([a, b, c])
            a, b, c = list
            num = (100 * c) + (10 * b) + a

            if (num - (s * n)) > 100:
                break

    candidates = [a, b, c]
    np.random.shuffle(candidates)
    sa, sb, sc = candidates

    com = "$$수식$$%d$$/수식$$" % num
    temp = num
    for i in range(n):
        temp = temp - s
        com = com + " - " + "$$수식$$%d$$/수식$$" % temp

    ans = num - (s * n)

    fa = "BOX{`%s`}" % sa
    fb = "BOX{`%s`}" % sb
    fc = "BOX{`%s`}" % sc

    stem = stem.format(s=s, n=n, fa=fa, fb=fb, fc=fc)
    answer = answer.format(ans=ans)
    comment = comment.format(a=a, b=b, c=c, num=num, com=com)

    return stem, answer, comment



# 2-1-1-33
def threedigits211_Stem_021():
    stem = "두 수의 크기를 비교하여 □ 안에 들어갈  $$수식$$&gt;$$/수식$$ 또는 $$수식$$&lt;$$/수식$$를 알맞게 써 보세요.\n$$수식$$``{a}````$$/수식$$$$수식$${boxblank}$$/수식$$$$수식$$````{b}``$$/수식$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "백의 자리 숫자와 십의 자리 숫자가 각각 같으므로 일의 자리 숫자를 비교합니다.\n" \
              "일의 자리 숫자를 비교하면 $$수식$${ca}$$/수식$$입니다.\n" \
              "➡ $$수식$${cb}$$/수식$$\n\n"

    boxblank = "BOX{　}"
    while True:
        hun = np.random.randint(1, 10) # 백자리
        ten = np.random.randint(1, 10) # 십자리
        onea = np.random.randint(1, 10) # 일자리
        oneb = np.random.randint(1, 10) # 일자리
        if onea != oneb:
            break

    a = (100 * hun) + (10 * ten) + onea
    b = (100 * hun) + (10 * ten) + oneb

    if a > b:
        ans = "&gt;"
    elif a < b:
        ans = "&lt;"

    ca = "%d %s %d" % (onea, ans, oneb)
    cb = "%d %s %d" % (a, ans, b)

    stem = stem.format(a=a, b=b, boxblank=boxblank)
    answer = answer.format(ans=ans)
    comment = comment.format(ca=ca, cb=cb)

    return stem, answer, comment




# 2-1-1-34
def threedigits211_Stem_022():
    stem = "수의 크기를 비교하여 가장 작은 수를 찾아 써 보세요.\n$$표$$ $$수식$${a}````````````{b}````````````{c}````````````$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "백의 자리 수를 비교하면 $$수식$${ca}$$/수식$$이므로 $$수식$${min}$$/수식$$가 가장 작은 수이고 " \
              "백의 자리 수가 $$수식$${hun}$$/수식$$인 $$수식$${mid}$$/수식$$과 $$수식$${max}$$/수식$$의 십의 자리 수를 비교하면 " \
              "$$수식$${cb}$$/수식$$이므로 $$수식$${cc}$$/수식$$입니다.\n" \
              "따라서 $$수식$${cd}$$/수식$$이므로 가장 작은 수는 $$수식$${min}$$/수식$$입니다.\n\n"

    while True:
        a = np.random.randint(100, 1000) # 백자리 // min
        b = np.random.randint(100, 1000) # 백자리 // mid
        c = np.random.randint(100, 1000) # 백자리 // max

        if ((b // 100) == (c // 100)) & ((c // 10) % 10 > (b // 10) % 10):
            if (a // 100) < (b // 100):
                break

    min = a
    mid = b
    max = c
    hun = b // 100
    minhun = a // 100

    ca = "%d``&lt;``%d" % (minhun, hun)

    tenmid = (b // 10) % 10
    tenmax = (c // 10) % 10

    cb = "%d``&lt;``%d" % (tenmid, tenmax)
    cc = "%d``&lt;``%d" % (mid, max)
    cd = "%d``&lt;``%d``&lt;``%d" % (min, mid, max)

    candidates = [a, b, c]
    np.random.shuffle(candidates)
    a, b, c = candidates

    stem = stem.format(a=a, b=b, c=c)
    answer = answer.format(ans=min)
    comment = comment.format(ca=ca, cb=cb, cc=cc, cd=cd, min=min, mid=mid, max=max, hun=hun)

    return stem, answer, comment



# 2-1-1-35
def threedigits211_Stem_023():
    stem = "{s}를 {p1}는 $$수식$${s1}$$/수식$$번, {p2}는 $$수식$${s2}$$/수식$$번, {p3}는 $$수식$${s3}$$/수식$$번 했습니다. {s}를 가장 많이 한 사람은 누구인가요?\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "$$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$$의 크기를 비교합니다.\n" \
              "백의 자리 수를 비교하면 $$수식$${min}$$/수식$$이 가장 작습니다.\n" \
              "$$수식$${mid}$$/수식$$과 $$수식$${max}$$/수식$$의 십의 자리 숫자를 비교하면 " \
              "$$수식$${ca}$$/수식$$이므로 {s}를 가장 많이 한 사람은 {ans}입니다.\n\n"

    while True:
        p1 = ["연주", "영서", "정미", "예나", "철수", "현지", "민호", "홍기", "찬우", "지유"][np.random.randint(0, 10)]
        p2 = ["연주", "영서", "정미", "예나", "철수", "현지", "민호", "홍기", "찬우", "지유"][np.random.randint(0, 10)]
        p3 = ["연주", "영서", "정미", "예나", "철수", "현지", "민호", "홍기", "찬우", "지유"][np.random.randint(0, 10)]
        if (p1 != p2) & (p1 != p3) & (p2 != p3):
            break

    s = ["줄넘기", "뜀뛰기", "왕복달리기"][np.random.randint(0, 3)]

    while True:
        s1 = np.random.randint(100, 1000) # 백자리 // min
        s2 = np.random.randint(100, 1000) # 백자리 // mid
        s3 = np.random.randint(100, 1000) # 백자리 // max

        if ((s2 // 100) == (s3 // 100)) & ((s3 // 10) % 10 > (s2 // 10) % 10):
            if (s1 // 100) < (s2 // 100):
                break

    min = s1
    mid = s2
    max = s3

    ca = "%d``&lt;``%d" % (mid, max)
    ans = p3


    candidates = [[p1, s1], [p2, s2], [p3, s3]]
    np.random.shuffle(candidates)
    [p1, s1], [p2, s2], [p3, s3] = candidates

    stem = stem.format(s=s, p1=p1, p2=p2, p3=p3, s1=s1, s2=s2, s3=s3)
    answer = answer.format(ans=ans)
    comment = comment.format(s1=s1, s2=s2, s3=s3, min=min, mid=mid, max=max, ca=ca, s=s, ans=ans)

    return stem, answer, comment



# 2-1-1-36
def threedigits211_Stem_024():
    stem = "$$수식$$0$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 중에서 {boxblank}안에 들어갈 수 있는 수는 모두 몇 개인가요?\n$$표$$ $$수식$$`{aa}``{boxblank}``{ac}`&lt;`{b}`$$/수식$$ $$/표$$ \n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "백의 자리 수가 같고 일의 자리 수가 $$수식$${ca}$$/수식$$입니다.\n" \
              "따라서 {boxblank}안에 들어갈 수 있는 수는 {cb} " \
              "$$수식$${cc}$$/수식$$로 $$수식$${ans}$$/수식$$개입니다.\n\n"

    boxblank = "□"

    aa = np.random.randint(1, 10)  # a 백자리
    ba = aa # b 백자리

    while True:
        bb = np.random.randint(0, 10)  # b 십자리
        ac = np.random.randint(0, 10)  # a 일자리
        bc = np.random.randint(0, 10)  # b 일자리

        if ac > bc:
            if bb > 1:
                ca = "%d``&gt;``%d" % (ac, bc)
                cb = "$$수식$$%d$$/수식$$보다 작아야 하므로" % (bb)
                ab = bb - 1
                break
        elif ac < bc:
            ca = "%d``&lt;``%d" % (ac, bc)
            cb = "$$수식$$%d$$/수식$$보다 작거나 $$수식$$%d$$/수식$$와 같아야 하므로" % (bb, bb)
            ab = bb
            break

    cc = "0"
    if ab > 0:
        for i in range(1, ab+1):
            cc = cc + ", %d" % i

    ans = ab + 1
    b = (ba * 100) + (bb * 10) + bc

    stem = stem.format(aa=aa, ac=ac, boxblank=boxblank, b=b)
    answer = answer.format(ans=ans)
    comment = comment.format(ca=ca, boxblank=boxblank, cb=cb, cc=cc, ans=ans)

    return stem, answer, comment




# 2-1-1-37
def threedigits211_Stem_025():
    stem = "글을 읽고 나는 어떤 수인지 써 보세요.\n$$표$$(가) {sa}\n(나) {sb}\n(다) {sc}\n(라) {sd}$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "{com}\n\n"

    sa = ["나는 세자리 수입니다.", "나는 백의 자리까지 있는 숫자입니다."][np.random.randint(0, 2)]
    if sa == "나는 세자리 수입니다.":
        ca = "세 자리 수이고"
    else:
        ca = "백의 자리까지 있는 수이고"

    candv = []
    sc = ["백의 자리 숫자와 일의 자리 숫자는 같습니다", "일의 자리 숫자는 백의 자리 숫자의 $$수식$$2$$/수식$$배입니다"][np.random.randint(0, 2)]
    if sc == "백의 자리 숫자와 일의 자리 숫자는 같습니다":
        cc = "백의 자리 숫자와 일의 자리 숫자가 같은 수는"
        while True:
            a = np.random.randint(100, 1000)
            b = np.random.randint(100, 1000)
            # 차이를 정해주기(백자리와 일자리가 같은 숫자가 2개 이상이며 너무 많지 않도록)
            diff = (a // 100) + 10
            if (b - a > diff) & (b - a < 50):
                for i in range(a, b+1):
                    hun = i // 100
                    one = i % 10
                    if hun == one:
                        candv.append(i)
                break
    else: # "일의 자리 숫자는 백의 자리 숫자의 2배입니다"
        cc = "일의 자리 숫자가 백의 자리 숫자의 $$수식$$2$$/수식$$배인 수는"
        while True:
            a = np.random.randint(100, 500)  # a 백자리
            b = np.random.randint(100, 500)  # a 백자리
            # 차이를 정해주기(일자리가 백자리의 두배인 숫자가 2개 이상이며 너무 많지 않도록)
            if (b - a > 20) & (b - a < 50):
                for i in range(a, b+1):
                    hun = i // 100
                    one = i % 10
                    if (2 * hun) == one:
                        candv.append(i)
                break

    sb = "나는 $$수식$$%d$$/수식$$ 보다 크고 $$수식$$%d$$/수식$$ 보다 작습니다" % (a, b)

    test = []
    for i in candv:
        hun = i // 100
        ten = (i // 10) % 10
        if ten - hun > 0:
            test.append(ten - hun)

    if not test:
        randc = 0
    else:
        randc = np.random.randint(0, 2)

    cands = ""
    candtmp = []
    if randc == 0: # "백의 자리 숫자와 십의 자리 숫자의 합은 C입니다"
        candc = []
        for i in candv:
            hun = i // 100
            ten = (i // 10) % 10
            candc.append(hun + ten)
            candtmp.append(i)
            cands = cands + "%d,````" % (i)
        if len(candc) == 1:
            c = candc[0]
        else:
            c = candc[np.random.randint(0, len(candc))]
        sd = "백의 자리 숫자와 십의 자리 숫자의 합은 $$수식$$%d$$/수식$$입니다" % (c)
        cd = "백의 자리 숫자와 십의 자리 숫자의 합이 $$수식$$%d$$/수식$$인" % (c)
        index = candc.index(c)
        ans = candtmp[index]
    else: #  "십의 자리 숫자는 백의 자리 숫자보다 C만큼 큽니다"
        candc = []
        for i in candv:
            hun = i // 100
            ten = (i // 10) % 10
            if ten - hun > 0:
                candc.append(ten - hun)
                candtmp.append(i)
                cands = cands + "%d,````" % (i)
        if len(candc) == 1:
            c = candc[0]
        else:
            c = candc[np.random.randint(0, len(candc))]
        sd = "십의 자리 숫자는 백의 자리 숫자보다 $$수식$$%d$$/수식$$만큼 큽니다" % (c)
        cd = "십의 자리 숫자가 백의 자리 숫자보다 $$수식$$%d$$/수식$$만큼 큰" % (c)
        index = candc.index(c)
        ans = candtmp[index]

    cands = cands[:-5]

    com = "%s $$수식$$%d$$/수식$$보다 크고 $$수식$$%d$$/수식$$보다 작은 수 중에서 %s $$수식$$%s$$/수식$$입니다. " \
          "이 중에서 %s 수는 $$수식$$%d$$/수식$$입니다." % (ca, a, b, cc, cands, cd, ans)

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(ans=ans)
    comment = comment.format(com=com)

    return stem, answer, comment




# 2-1-1-38
def threedigits211_Stem_026():
    stem = "작은 수부터 차례로 기호를 써 보세요.\n$$표$$㉠ {sta}\n㉡ {stb}\n㉢ {stc}\n㉣ {std}$$/표$$\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${aa}$$/수식$$  ㉡ $$수식$${ab}$$/수식$$  ㉢ $$수식$${ac}$$/수식$$  ㉣ $$수식$${ad}$$/수식$$\n" \
              "→ $$수식$${com}$$/수식$$\n"

    while True:
        a = np.random.randint(451, 650)
        b = np.random.randint(2, 4)
        c = np.random.randint(401, 700)
        d = np.random.randint(31, 80)
        e = np.random.randint(1, 10)
        f = np.random.randint(1, 20)
        g = np.random.randint(11, 40)
        j = np.random.randint(1, 10)
        h = np.random.randint(100, 1000)
        hhun = h // 100
        hten = (h // 10) % 10
        hone = h % 10
        hlist = [hhun, hten, hone]
        if (hhun != hten) & (hhun != hone) & (hten != hone):
            if j in hlist:
                break

    tmpa = np.random.randint(0, 2)
    if tmpa == 0:
        sta = "$$수식$$%d$$/수식$$에서 $$수식$$100$$/수식$$씩 $$수식$$%d$$/수식$$번 뛰어서 센 수" % (a, b)
        aa = a + (100 * b)
    elif tmpa == 1:
        sta = "$$수식$$%d$$/수식$$에서 $$수식$$100$$/수식$$씩 $$수식$$%d$$/수식$$번 줄인 수" % (a, b)
        aa = a - (100 * b)

    tmpb = np.random.randint(0, 2)
    if tmpb == 0:
        stb = "$$수식$$%d$$/수식$$보다 $$수식$$%d$$/수식$$ 큰 수" % (c, d)
        ab =  c + d
    elif tmpb == 1:
        stb = "$$수식$$%d$$/수식$$보다 $$수식$$%d$$/수식$$ 작은 수" % (c, d)
        ab = c - d

    stc = "$$수식$$100$$/수식$$이 $$수식$$%d$$/수식$$, $$수식$$10$$/수식$$이 $$수식$$%d$$/수식$$, $$수식$$1$$/수식$$이 $$수식$$%d$$/수식$$인 수" % (e, f, g)
    ac = (100 * e) + (10 * f) + g

    j1 = proc_jo(j, 0)
    std = "$$수식$$%d$$/수식$$에서 $$수식$$%d$$/수식$$%s 나타내는 값" % (h, j, j1)
    index = hlist.index(j)
    if index == 0:
        ad = j * 100
    elif index == 1:
        ad = j * 10
    elif index == 2:
        ad = j

    candidates = [[sta, aa], [stb, ab], [stc, ac], [std, ad]]
    np.random.shuffle(candidates)
    [sta, aa], [stb, ab], [stc, ac], [std, ad] = candidates

    maxlist = sorted([aa, ab, ac, ad])
    com = ""
    for i in maxlist:
        com = com + "%d``&lt;``" % (i)
    com = com[:-8]
    anslist = []

    for i, s in enumerate(maxlist):
        for j, r in enumerate(candidates):
            if s in r:
                anslist.append(j)

    ans = ""
    for i in anslist:
        ans = ans + "%s, " % (answer_koonedict[i])
    ans = ans[0:-2]

    stem = stem.format(sta=sta, stb=stb, stc=stc, std=std)
    answer = answer.format(ans=ans)
    comment = comment.format(aa=aa, ab=ab, ac=ac, ad=ad, com=com)

    return stem, answer, comment




# 2-1-1-39
def threedigits211_Stem_027():
    stem = "어떤 수보다 $$수식$${a}$$/수식$$ 큰 수는 $$수식$${b}$$/수식$$입니다. 어떤 수보다 $$수식$${c}$$/수식$$ 작은 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수보다 $$수식$${a}$$/수식$$ 큰 수가 $$수식$${b}$$/수식$$이므로 어떤 수는 $$수식$${b}$$/수식$$보다 $$수식$${a}$$/수식$$ 작은 수인 $$수식$${d}$$/수식$$입니다.\n" \
              "➡ $$수식$${d}$$/수식$$보다 $$수식$${c}$$/수식$$ 작은 수는 $$수식$${e}$$/수식$$입니다.\n\n"

    while True:
        aa = np.random.randint(1, 10)
        a = aa * 10
        b = np.random.randint(100, 1000)
        if b - a > 100:
            d = b - a
            cc = np.random.randint(1, 10)
            c = cc * 100
            if d - c > 100:
                e = d - c
                break

    stem = stem.format(a=a, b=b, c=c)
    answer = answer.format(ans=e)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e)

    return stem, answer, comment



