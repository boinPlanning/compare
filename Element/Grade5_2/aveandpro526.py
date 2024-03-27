import numpy as np


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






#5-2-6-05
def aveandpro526_Stem_001():
    stem = "다음 $$수식$$4$$/수식$$개의 수의 평균은 얼마인가요?\n$$표$$$$수식$${sa}$$/수식$$    $$수식$${sb}$$/수식$$    $$수식$${sc}$$/수식$$    $$수식$${sd}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$, $$수식$${sb}$$/수식$$, $$수식$${sc}$$/수식$$, $$수식$${sd}$$/수식$$의 수를 고르게 하면 " \
              "$$수식$${m}$$/수식$$, $$수식$${m}$$/수식$$, $$수식$${m}$$/수식$$, $$수식$${m}$$/수식$$이므로 평균은 $$수식$${m}$$/수식$$입니다.\n\n"


    m = np.random.randint(4, 10)
    a = m
    b = m - 1
    c = m + 2
    d = m - 1

    candidates = [a, b, c, d]
    np.random.shuffle(candidates)
    sa, sb, sc, sd = candidates

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(ans=m)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, m=m)

    return stem, answer, comment

















#5-2-6-13
def aveandpro526_Stem_002():
    stem = "$$수식$${sa}$$/수식$$월 한 달 동안 어느 {n1} 방문자 수는 모두 $$수식$${sb}$$/수식$$명이었습니다. {n1} 방문자 수는 하루 평균 몇 명인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$명\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$평균$$수식$$RIGHT ) ` = ` LEFT ( {sa}$$/수식$$월 한 달 동안 방문자 수$$수식$$RIGHT ) ` div ` LEFT ( {sa}$$/수식$$월의 날 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {sb} ` div ` {day} ` = ` {s1} ` LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$\n\n"


    n1 = ["전시회", "미술관", "박물관", "동물원"][np.random.randint(0, 4)]

    while True:
        sa = np.random.randint(1, 13)
        if sa != 2:
            break

    list30 = [4, 6, 9, 11]

    if sa in list30:
        day = 30
    else:
        day = 31

    n = np.random.randint(34, 50) # s1
    sb = n * day


    stem = stem.format(sa=sa, sb=sb, n1=n1)
    answer = answer.format(ans=n)
    comment = comment.format(sa=sa, sb=sb, day=day, s1=n)

    return stem, answer, comment







#5-2-6-22
def aveandpro526_Stem_003():
    stem = "{n1}는 {t}를 타고 $$수식$${a} ` rm {{km}}$$/수식$$를 가는 데 $$수식$${sa}$$/수식$$시간이 걸렸고, {n2}는 {t}를 타고 $$수식$${b} ` rm {{km}}$$/수식$$를 가는 데 $$수식$${sb}$$/수식$$시간이 걸렸습니다. 두 사람 중 누가 $$수식$$1$$/수식$$시간당 평균 몇 $$수식$$rm {{km}}$$/수식$$를 더 갔나요?\n"
    answer = "(정답)\n{n}, $$수식$${s3} rm {{km}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$1$$/수식$$시간 동안 간 평균 거리를 구해 보면\n" \
              "{n1}: $$수식$${a} ` div ` {sa} ` = ` {s1} LEFT ( rm {{km}} RIGHT )$$/수식$$,\n" \
              "{n2}: $$수식$${b} ` div ` {sb} ` = ` {s2} LEFT ( rm {{km}} RIGHT )$$/수식$$입니다.\n" \
              "따라서 {n}가 $$수식$$1$$/수식$$시간당 평균 $$수식$${x1} ` - ` {x2} ` = ` {s3} LEFT ( rm {{km}} RIGHT )$$/수식$$ 더 갔습니다.\n\n"


    n1 = ["현우", "준수", "우희", "희수", "현지"][np.random.randint(0, 5)]
    n2 = ["선하", "수아", "진우", "연수", "선희"][np.random.randint(0, 5)]
    t = ["자전거", "자동차"][np.random.randint(0, 2)]

    if t == "자전거":
        while True:
            sa = np.random.randint(2, 10)
            sb = np.random.randint(2, 10)
            if sa != sb:
                s1 = np.random.randint(8, 12)
                s2 = np.random.randint(8, 12)
                if s1 != s2:
                    a = s1 * sa
                    b = s2 * sb
                    break

    elif t == "자동차":
        while True:
            sa = np.random.randint(2, 7)
            sb = np.random.randint(2, 7)
            if sa != sb:
                s1 = np.random.randint(70, 81)
                s2 = np.random.randint(70, 81)
                if s1 != s2:
                    a = s1 * sa
                    b = s2 * sb
                    break

    if s1 > s2:
        n = n1
        x1 = s1
        x2 = s2
    elif s1 < s2:
        n = n2
        x1 = s2
        x2 = s1

    s3 = x1 - x2

    stem = stem.format(sa=sa, sb=sb, a=a, b=b, n1=n1, n2=n2, t=t)
    answer = answer.format(n=n, s3=s3)
    comment = comment.format(sa=sa, sb=sb, a=a, b=b, n1=n1, n2=n2, s1=s1, s2=s2, x1=x1, x2=x2, s3=s3, n=n)

    return stem, answer, comment






#5-2-6-25
def aveandpro526_Stem_004():
    stem = "{n1}네 과수원에 {n2}가 $$수식$${a}$$/수식$$그루 있습니다. {n2} 한 그루에 {n3}{j1} 평균 $$수식$${b}$$/수식$$개씩 열린다고 할 때, 이 {n3}{j2} 한 개에 $$수식$$1000$$/수식$$원씩 받고 모두 판다면 {n3}{j2} 판 금액은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$원\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${n2}에 열린 {n3}의 수$$수식$$RIGHT ) ` = ` {b} ` times ` {a} ` = ` {s1} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${n3}{j2} 판 금액$$수식$$RIGHT ) ` = ` {s1} ` times ` 1000 ` = ` {s2} ` LEFT ($$/수식$$원$$수식$$RIGHT )$$/수식$$\n\n"


    n1 = ["현주", "준오", "유호", "희수", "상우"][np.random.randint(0, 5)]
    [n2, n3] = [["사과나무", "사과"], ["배나무", "배"], ["감나무", "감"]][np.random.randint(0, 3)]
    j1 = proc_jo(n3, 0)
    j2 = proc_jo(n3, 1)

    a = np.random.randint(71, 100)
    sb = np.random.randint(6, 10)

    b = sb * 10
    s1 = b * a
    s2 = s1 * 1000

    stem = stem.format(n1=n1, n2=n2, n3=n3, a=a, b=b, j1=j1, j2=j2)
    answer = answer.format(ans=s2)
    comment = comment.format(n1=n1, n2=n2, n3=n3, a=a, b=b, s1=s1, s2=s2, j2=j2)

    return stem, answer, comment







#5-2-6-26
def aveandpro526_Stem_005():
    stem = "{n1}가 {z1}네 과수원에는 $$수식$${a}$$/수식$$그루 있고, {z2}네 과수원에는 $$수식$${b}$$/수식$$그루 있습니다. {n1} 한 그루에서 수확한 {n2}의 수의 평균이 $$수식$${m}$$/수식$$개일 때, {z1}와 {z2}네 과수원에서 수확한 {n2}{j1} 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${z1}와 {z2}네의 {n1}의 수$$수식$$RIGHT )$$/수식$$\n$$수식$$ ` = ` {a} ` + ` {b} ` = ` {s1} ` LEFT ($$/수식$$그루$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${z1}와 {z2}네가 수확한 {n2}의 수$$수식$$RIGHT )$$/수식$$\n$$수식$$ ` = ` {s1} ` times ` {m} ` = ` {s2} ` LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"


    [n1, n2] = [["사과나무", "사과"], ["배나무", "배"], ["감나무", "감"]][np.random.randint(0, 3)]
    j1 = proc_jo(n2, -1)

    z1 = ["성주", "준우", "유희", "희주", "상호"][np.random.randint(0, 5)]
    z2 = ["선기", "미희", "현서", "우호", "석우"][np.random.randint(0, 5)]

    a = np.random.randint(301, 320)
    b = np.random.randint(185, 200)
    m = np.random.randint(125, 147)

    s1 = a + b
    s2 = s1 * m

    stem = stem.format(n1=n1, n2=n2, z1=z1, z2=z2, j1=j1, a=a, b=b, m=m)
    answer = answer.format(ans=s2)
    comment = comment.format(n1=n1, n2=n2, z1=z1, z2=z2, a=a, b=b, s1=s1, s2=s2, m=m)

    return stem, answer, comment






#5-2-6-27
def aveandpro526_Stem_006():
    stem = "{n1}{j1} {z1}와 {z2} 점수의 평균은 $$수식$${a}$$/수식$$점이고 {z3}, {z4}, {z5} 점수의 평균은 $$수식$${b}$$/수식$$점입니다. {n1}의 다섯 과목 점수의 평균은 몇 점인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$점\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$다섯 과목 점수의 합$$수식$$RIGHT )$$/수식$$\n$$수식$$ ` = ` {a} ` times ` 2 ` + ` {b} ` times ` 3 ` = ` {s1} ` + ` {s2} ` = ` {s3} ` LEFT ($$/수식$$점$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$다섯 과목 점수의 평균$$수식$$RIGHT )$$/수식$$\n$$수식$$ ` = ` {s3} ` div ` 5 ` = ` {m} ` LEFT ($$/수식$$점$$수식$$RIGHT )$$/수식$$입니다.\n\n"


    n1 = ["성우", "준성", "우철", "희정", "현영"][np.random.randint(0, 5)]
    j1 = proc_jo(n1, -1)

    subject = ["국어", "영어", "수학", "사회", "과학"]
    np.random.shuffle(subject)
    z1, z2, z3, z4, z5 = subject

    m = np.random.randint(80, 99)
    a = m -3
    b = m + 2

    s1 = a * 2
    s2 = b * 3
    s3 = s1 + s2

    stem = stem.format(n1=n1, z1=z1, z2=z2, z3=z3, z4=z4, z5=z5, j1=j1, a=a, b=b)
    answer = answer.format(ans=m)
    comment = comment.format(a=a, b=b, s1=s1, s2=s2, s3=s3, m=m)

    return stem, answer, comment






#5-2-6-29
def aveandpro526_Stem_007():
    stem = "{n1}의 단원별 {n2} 시험 점수를 나타낸 것입니다. {n2} 시험 점수의 평균이 $$수식$${m}$$/수식$$점 이상이 되어야 교내 {n2} 경시대회에 참가할 수 있습니다. {n1}가 교내 {n2} 경시대회에 참가하려면 마지막에 적어도 몇 점을 받아야 하나요?\n$$표$$$$수식$${a}$$/수식$$    $$수식$${b}$$/수식$$    $$수식$${c}$$/수식$$    $$수식$${d}$$/수식$$    $$수식$${e}$$/수식$$    $$수식$$□$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$점\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${n1}의 단원별 {n2} 시험 점수의 합$$수식$$RIGHT )$$/수식$$\n$$수식$$ ` = ` {a} ` + ` {b} ` + ` {c} ` + ` {d} ` + ` {e} ` + `$$/수식$$" \
              "□$$수식$$` = ` {s1} ` + `$$/수식$$□$$수식$$LEFT ($$/수식$$점$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$${s1} ` + `$$/수식$$□가 $$수식$${m} ` times ` 6 ` $$/수식$$과 같거나 커야 합니다.\n" \
              "$$수식$${s1} ` + `$$/수식$$□$$수식$$` = ` {m} ` times ` 6 `$$/수식$$일 때\n" \
              "$$수식$${s1} ` + `$$/수식$$□$$수식$$` = ` {s2}$$/수식$$, □$$수식$$` = ` {s2} ` - ` {s1} ` = ` {s3}`$$/수식$$이므로 마지막에 적어도 $$수식$${s3}$$/수식$$점을 받아야 합니다.\n\n"


    n1 = ["성우", "준호", "영희", "희우", "현수"][np.random.randint(0, 5)]
    n2 = ["수학", "과학"][np.random.randint(0, 2)]

    while True:
        m = np.random.randint(90, 93)
        m1 = np.random.randint(m-1, m+4)
        a = m1 + 4
        b = m1 - 4
        c = m1 - 6
        d = m1 + 5
        e = m1 + 1

        s1 = a + b + c + d + e
        s2 = m * 6
        s3 = s2 - s1

        if s3 <= 100:
            break

    candidates = [a, b, c, d, e]
    np.random.shuffle(candidates)
    a, b, c, d, e = candidates

    stem = stem.format(n1=n1, n2=n2, a=a, b=b, c=c, d=d, e=e, m=m)
    answer = answer.format(ans=s3)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, s1=s1, s2=s2, s3=s3, m=m, n1=n1, n2=n2)

    return stem, answer, comment






#5-2-6-30
def aveandpro526_Stem_008():
    stem = "{n1}, {n2}, {n3} 세 사람의 줄넘기 기록의 평균은 $$수식$${m1}$$/수식$$번이고, {n4}의 기록을 포함한 네 사람의 줄넘기 기록의 평균은 $$수식$${m2}$$/수식$$번입니다. {n4}의 줄넘기 기록은 몇 번인가요?\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$번\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$네 사람의 줄넘기 기록의 합$$수식$$RIGHT ) ` = ` {m2} ` times ` 4 ` = ` {s1} ` LEFT ($$/수식$$번$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$$세 사람의 줄넘기 기록의 합$$수식$$RIGHT ) ` = ` {m1} ` times ` 3 ` = ` {s2} ` LEFT ($$/수식$$번$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${n4}의 줄넘기 기록$$수식$$RIGHT ) ` = ` {s1} ` - ` {s2} ` = ` {s3} ` LEFT ($$/수식$$번$$수식$$RIGHT )$$/수식$$\n\n"


    n1 = ["지수", "영지", "선우", "석호", "명주"][np.random.randint(0, 5)]
    n2 = ["명호", "우주", "현희", "금호", "선주"][np.random.randint(0, 5)]
    n3 = ["진우", "영희", "현지", "영우", "동희"][np.random.randint(0, 5)]
    n4 = ["선희", "우호", "진희", "희수", "덕호"][np.random.randint(0, 5)]

    while True:
        m1 = np.random.randint(61, 70)
        m2 = np.random.randint(61, 70)
        if m1 < m2:
            break

    s1 = m2 * 4
    s2 = m1 * 3
    s3 = s1 - s2

    stem = stem.format(n1=n1, n2=n2, n3=n3, n4=n4, m1=m1, m2=m2)
    answer = answer.format(ans=s3)
    comment = comment.format(s1=s1, s2=s2, s3=s3, m1=m1, m2=m2, n4=n4)

    return stem, answer, comment
























#5-2-6-34
def aveandpro526_Stem_009():
    stem = "$$수식$$1$$/수식$$번부터 $$수식$$10$$/수식$$번까지의 번호표가 들어 있는 상자에서 번호표 $$수식$$1$$/수식$$개를 꺼낼 때 $$수식$${s1}$$/수식$$번 번호표를 꺼낼 가능성을 말로 표현해 보세요.\n"
    answer = "(정답)\n{ans}\n"
    comment = "(해설)\n" \
              "상자 안에는 $$수식$$1$$/수식$$번부터 $$수식$$10$$/수식$$번까지의 번호표가 있으므로 $$수식$${s1}$$/수식$$번 번호표를 꺼낼 가능성은 ‘{t}’입니다.\n\n"


    s1 = np.random.randint(11, 20)
    t = "불가능하다"

    stem = stem.format(s1=s1)
    answer = answer.format(ans=t)
    comment = comment.format(s1=s1, t=t)

    return stem, answer, comment


























#5-2-6-41
def aveandpro526_Stem_010():
    stem = "상자에 {n1} 공만 $$수식$${a}$$/수식$$개가 들어 있습니다. 상자에서 공 한 개를 꺼낼 때 꺼낸 공이 {n2}일 가능성을 수로 표현해 보세요.\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "상자에 들어 있는 공이 모두 {n1} 공이므로 공 한 개를 꺼낼 때 공이 {n2}일 가능성은 ‘{t}’입니다.\n" \
              "따라서 꺼낸 공이 {n2}일 가능성을 수로 표현하면 $$수식$${s1}$$/수식$$입니다.\n\n"


    n1 = ["파란색", "빨간색", "노란색", "초록색"][np.random.randint(0, 4)]
    n2 = ["파란색", "빨간색", "노란색", "초록색"][np.random.randint(0, 4)]

    a = np.random.randint(2, 10)

    if n1 == n2:
        t = "확실하다"
        s1 = 1
    else:
        t = "불가능하다"
        s1 = 0


    stem = stem.format(n1=n1, n2=n2, a=a)
    answer = answer.format(ans=s1)
    comment = comment.format(s1=s1, n1=n1, n2=n2, t=t)

    return stem, answer, comment







#5-2-6-47
def aveandpro526_Stem_011():
    stem = "지갑 속에 $$수식$${money1}$$/수식$$원짜리 지폐 $$수식$${a}$$/수식$$장과 $$수식$${money2}$$/수식$$원짜리 지폐 $$수식$${a}$$/수식$$장이 있습니다. 지갑에서 지폐 $$수식$$1$$/수식$$장을 꺼낼 때 꺼낸 지폐가 $$수식$${s1}$$/수식$$원짜리일 가능성을 가장 간단한 분수로 표현해 보세요.\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "지갑 속에 $$수식$${money1}$$/수식$$원짜리 지폐가 반, $$수식$${money2}$$/수식$$원짜리 지폐가 반이므로 " \
              "지폐 $$수식$$1$$/수식$$장을 꺼낼 때 꺼낸 지폐가 $$수식$${s1}$$/수식$$원짜리일 가능성은 ‘반반이다’입니다.\n" \
              "따라서 가능성을 수로 표현하면 $$수식$${s2}$$/수식$$입니다.\n\n"


    a = np.random.randint(1, 10)

    while True:
        money1 = [1000, 5000, 10000, 50000][np.random.randint(0, 4)]
        money2 = [1000, 5000, 10000, 50000][np.random.randint(0, 4)]
        if money1 != money2:
            break

    s1 = [money1, money2][np.random.randint(0, 2)]

    s2 = "1 over 2"


    stem = stem.format(a=a, s1=s1, money1=money1, money2=money2)
    answer = answer.format(ans=s2)
    comment = comment.format(s1=s1, s2=s2, money1=money1, money2=money2)

    return stem, answer, comment




