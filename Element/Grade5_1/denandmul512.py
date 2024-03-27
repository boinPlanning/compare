import numpy as np
import random






answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤",
    5: "⑥",
    6: "⑦",
    7: "⑧",
    8: "⑨",
    9: "⑩",
    10: "⑪",
    11: "⑫",
    12: "⑬",
    13: "⑭",
    14: "⑮"
}






answer_kodict = {
    0: "㉠",
    1: "㉡",
    2: "㉢",
    3: "㉣",
    4: "㉤"
}






answer_kodict2 = {
    0: 'ㄱ',
    1: 'ㄴ',
    2: 'ㄷ',
    3: 'ㄹ',
    4: 'ㅁ'
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







def name_jo(num):
    # 이
    if bool_jo(num):
        return "이"
    return ""








def getdivisor(num):
    if num < 1:
        return 0
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor








def is_prime(number):
    if number != 1:
        for i in range(2, number):
            if number % i == 0:
                return False
    else:
        return False
    return True






def getfactor(n):
    result = []
    for i in range(2, int(n/2) + 1):
        if not is_prime(i):
            continue
        count = 0
        while n % i == 0:
            count = count + 1
            n = int(n / i)
        if count != 0:
            result.append((i, count))
            # (소수, 개수) 형태로 리스트에 추가됨
        if n == 1:
            break
    return result







def getfactor2(n):
    result = []
    for i in range(2, int(n/2) + 1):
        if not is_prime(i):
            continue
        while n % i == 0:
            result.append(i)
            n = int(n / i)
        if n == 1:
            break
    return result















# 5-1-2-02
def denandmul512_Stem_001():
    stem = "$$수식$${a}$$/수식$$의 배수를 모두 고르세요.\n① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(정답)\n{k1}, {k2}, {k3}\n"
    comment = "(해설)\n" \
              "{k1} $$수식$${a} TIMES {tt1} = {ts1}$$/수식$$, {k2} $$수식$${a} TIMES {tt2} = {ts2}$$/수식$$,\n" \
              "{k3} $$수식$${a} TIMES {tt3} = {ts3}$$/수식$$\n\n"


    a = np.random.randint(6, 15)
    n = random.sample(list(range(2, 15)), 5)
    n1, n2, n3, n4, n5 = n

    another_n = [n1, n2, n3, n4, n5]
    another_n.sort()

    for i in range(0, len(n)):
        n[i] = n[i] * a

    n[3] = n[3] + 2
    n[4] = n[4] + 3

    n.sort()
    c1, c2, c3, c4, c5 = n

    k = []
    tt = []

    for i in range(0, len(n)):
        if n[i] % a == 0:
            k.append(answer_dict[i])
            tt.append(another_n[i])

    k1, k2, k3 = k

    tt1, tt2, tt3 = tt
    ts1 = a*tt1
    ts2 = a*tt2
    ts3 = a*tt3

    stem = stem.format(a=a, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(k1=k1, k2=k2, k3=k3)
    comment = comment.format(a=a, k1=k1, k2=k2, k3=k3, tt1=tt1, tt2=tt2, tt3=tt3, ts1=ts1, ts2=ts2, ts3=ts3)

    return stem, answer, comment


















# 5-1-2-04
def denandmul512_Stem_002():
    stem = "$$수식$${b}$$/수식$$의 약수를 모두 찾아 써 보세요.\n$$표$$$$수식$${a1}$$/수식$$     $$수식$${a2}$$/수식$$     $$수식$${a3}$$/수식$$     $$수식$${a4}$$/수식$$     $$수식$${a5}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${b} DIV {s1} = {x1}$$/수식$$, $$수식$${b} DIV {s2} = {x2}$$/수식$$, " \
              "$$수식$${b} DIV {s3} = {x3}$$/수식$$\n\n"


    while True:
        b = np.random.randint(20, 50)
        divisor = getdivisor(b)
        if len(divisor) >= 5:
            break


    while True:
        flag = True
        s = random.sample(divisor, 3)
        if 1 in s:
            flag = False
        if flag:
            break


    s.sort()
    s1, s2, s3 = s
    x = []

    for i in range(0, len(s)):
        x.append(int(b / s[i]))

    x1, x2, x3 = x

    while True:
        ex = random.sample(list(range(2, b)), 2)
        if b % ex[0] != 0 and b % ex[1] != 0:
            break

    a = s + ex
    a.sort()
    a1, a2, a3, a4, a5 = a

    stem = stem.format(b=b, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(s1=s1, s2=s2, s3=s3)
    comment = comment.format(b=b, s1=s1, s2=s2, s3=s3, x1=x1, x2=x2, x3=x3)

    return stem, answer, comment











# 5-1-2-05
def denandmul512_Stem_003():
    stem = "$$수식$${b}$$/수식$$의 약수가 아닌 것은 어느 것인가요?\n① $$수식$${a1}$$/수식$$     ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n④ $$수식$${a4}$$/수식$$     ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{k}\n"
    comment = "(해설)\n" \
              "$$수식$${b} DIV {c1} = {x1}$$/수식$$, $$수식$${b} DIV {c2} = {x2}$$/수식$$, " \
              "$$수식$${b} DIV {c3} = {x3}$$/수식$$, $$수식$${b} DIV {c4} = {x4}$$/수식$$\n" \
              "따라서 $$수식$${b}$$/수식$$의 약수는 $$수식$${c1}$$/수식$$, $$수식$${c2}$$/수식$$, " \
              "$$수식$${c3}$$/수식$$, $$수식$${c4}$$/수식$$입니다.\n\n"


    while True:
        blist = random.sample([6, 8, 10, 14, 15, 18], 1)
        #b = blist[0]
        b = random.randint(6,30)
        divisor = getdivisor(b)
        if len(divisor) >= 4:
            break

    c = random.sample(divisor, 4)
    c.sort()
    c1, c2, c3, c4 = c

    x = []
    for i in range(0, len(c)):
        x.append(int(b / c[i]))
    x1, x2, x3, x4 = x

    while True:
        ex = np.random.randint(2, b)
        if b % ex != 0:
            break

    a = c.copy()

    a.append(ex)
    a.sort()
    a1, a2, a3, a4, a5 = a

    for i in range(0, len(a)):
        if a[i] == ex:
            k = answer_dict[i]
            break

    stem = stem.format(b=b, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5)
    answer = answer.format(k=k)
    comment = comment.format(b=b, c1=c1, c2=c2, c3=c3, c4=c4, x1=x1, x2=x2, x3=x3, x4=x4)

    return stem, answer, comment











# 5-1-2-06
def denandmul512_Stem_004():
    stem = "왼쪽 수가 오른쪽 수의 약수인 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$$LEFT ( {a1}$$/수식$$, $$수식$${A1} RIGHT )$$/수식$$     ㉡ $$수식$$LEFT ( {a2}$$/수식$$, $$수식$${A2} RIGHT )$$/수식$$     ㉢ $$수식$$LEFT ( {a3}$$/수식$$, $$수식$${A3} RIGHT )$$/수식$$$$/표$$\n"
    answer = "(정답)\n{k}\n"
    comment = "(해설)\n" \
              "오른쪽 수를 왼쪽 수로 나누었을 때 나누어떨어지면 왼쪽 수가 오른쪽 수의 약수입니다.\n" \
              "㉠ $$수식$${A1} DIV {a1} = {b1}$$/수식$${c1}\n" \
              "㉡ $$수식$${A2} DIV {a2} = {b2}$$/수식$${c2}\n" \
              "㉢ $$수식$${A3} DIV {a3} = {b3}$$/수식$${c3}\n" \
              "따라서 왼쪽 수가 오른쪽 수의 약수인 것은 {k}입니다.\n\n"


    D1, D2, D3 = random.sample(list(range(6, 25)), 3)
    D1 = D1 * 2
    D2 = D2 * 2
    D3 = D3 * 2

    div1 = getdivisor(D1)
    div2 = getdivisor(D2)
    div3 = getdivisor(D3)

    while True:
        while True:
            d1 = random.sample(div1, 1)[0]
            if d1 != 1 and d1 != D1:
                break

        while True:
            d2 = np.random.randint(2, 10)
            flag = True
            if d2 in div2:
                flag = False
            if flag:
                break

        while True:
            d3 = np.random.randint(2, 10)
            flag = True
            if d3 in div3:
                flag = False
            if flag:
                break

        if d1 != d2 and d2 != d3 and d1 != d3:
            break

    Dlist = [[d1, D1], [d2, D2], [d3, D3]]
    np.random.shuffle(Dlist)
    [[a1, A1], [a2, A2], [a3, A3]] = Dlist

    b1 = int(A1 / a1)
    b2 = int(A2 / a2)
    b3 = int(A3 / a3)

    c = []

    c.append('$$수식$$` CDOTS ` {c1}$$/수식$$'.format(c1=A1 % a1))
    c.append('$$수식$$` CDOTS ` {c2}$$/수식$$'.format(c2=A2 % a2))
    c.append('$$수식$$` CDOTS ` {c3}$$/수식$$'.format(c3=A3 % a3))

    for i in range(0, len(Dlist)):
        if Dlist[i][0] == d1:
            k = answer_kodict[i]
            c[i] = ''
            break

    c1, c2, c3 = c

    stem = stem.format(a1=a1, a2=a2, a3=a3, A1=A1, A2=A2, A3=A3)
    answer = answer.format(k=k)
    comment = comment.format(a1=a1, a2=a2, a3=a3, A1=A1, A2=A2, A3=A3, b1=b1, b2=b2, b3=b3, c1=c1, c2=c2, c3=c3, k=k)

    return stem, answer, comment










# 5-1-2-07
def denandmul512_Stem_005():
    stem = "$$수식$${A}$$/수식$$의 모든 약수의 합은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "{sol}\n" \
              "$$수식$${A}$$/수식$$의 약수: {divisor}\n" \
              "$$수식$$LEFT ( {A}$$/수식$$의 약수의 합$$수식$$RIGHT ) ={sums}= {S}$$/수식$$\n\n"


    while True:
        A = np.random.randint(11, 26)
        divs = getdivisor(A)
        if len(divs) >= 3 and len(divs) <= 5:
            break

    sol = ''
    divisor = ''
    sums = ''

    S = 0

    for i in range(0, len(divs)):
        S = S + divs[i]
        sol = sol + "$$수식$${A} DIV {a} = {b}$$/수식$$".format(A=A, a=divs[i], b=int(A/divs[i]))
        divisor = divisor + "$$수식$${num}$$/수식$$".format(num=divs[i])
        sums = sums + "{num}".format(num=divs[i])

        if i != len(divs) - 1:
            sol = sol + ", "
            divisor = divisor + ', '
            sums = sums + '+'

    stem = stem.format(A=A)
    answer = answer.format(S=S)
    comment = comment.format(A=A, S=S, sol=sol, divisor=divisor, sums=sums)

    return stem, answer, comment













# 5-1-2-08
def denandmul512_Stem_006():
    stem = "다음 중 약수가 가장 많은 수는 어느 것인가요?\n① $$수식$${A1}$$/수식$$     ② $$수식$${A2}$$/수식$$     ③ $$수식$${A3}$$/수식$$\n④ $$수식$${A4}$$/수식$$     ⑤ $$수식$${A5}$$/수식$$\n"
    answer = "(정답)\n{k}\n"
    comment = "(해설)\n" \
              "① $$수식$${A1}$$/수식$$의 약수: {x1}\n" \
              "② $$수식$${A2}$$/수식$$의 약수: {x2}\n" \
              "③ $$수식$${A3}$$/수식$$의 약수: {x3}\n" \
              "④ $$수식$${A4}$$/수식$$의 약수: {x4}\n" \
              "⑤ $$수식$${A5}$$/수식$$의 약수: {x5}\n" \
              "따라서 약수가 가장 많은 수는 {k}입니다.\n\n"


    while True:
        A = random.sample(list(range(6, 51)), 5)
        div = []
        divnum = []
        for i in range(0, len(A)):
            A[i] = A[i] * 2
            div.append(getdivisor(A[i]))
            divnum.append(len(div[i]))
        divnum2 = divnum.copy()
        divnum2.sort()
        maxnum = divnum2[len(divnum2)-1]
        secnum = divnum2[len(divnum2)-2]
        if maxnum != secnum:
            break

    A1, A2, A3, A4, A5 = A

    x = []
    for i in range(0, len(A)):
        temp = ''
        for j in range(0, len(div[i]) - 1):
            temp = temp + "$$수식$${bn}$$/수식$$, ".format(bn=div[i][j])
        temp = temp + "$$수식$${bn}$$/수식$$ → $$수식$${b}$$/수식$$개".format(bn=div[i][len(div[i]) - 1], b=divnum[i])
        x.append(temp)

    x1, x2, x3, x4, x5 = x

    for i in range(0, len(divnum)):
        if divnum[i] == maxnum:
            k = answer_dict[i]
            break

    stem = stem.format(A1=A1, A2=A2, A3=A3, A4=A4, A5=A5)
    answer = answer.format(k=k)
    comment = comment.format(A1=A1, A2=A2, A3=A3, A4=A4, A5=A5, k=k, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)

    return stem, answer, comment

















# 5-1-2-09
def denandmul512_Stem_007():
    stem = "다음 수 중에서 $$수식$${A}$$/수식$$의 배수는 모두 몇 개인가요?\n$$표$$$$수식$${a1}$$/수식$$     $$수식$${a2}$$/수식$$     $$수식$${a3}$$/수식$$     $$수식$${a4}$$/수식$$     $$수식$${a5}$$/수식$$\n$$수식$${a6}$$/수식$$     $$수식$${a7}$$/수식$$     $$수식$${a8}$$/수식$$     $$수식$${a9}$$/수식$$     $$수식$${a10}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${s}$$/수식$$개\n"
    comment = "(해설)\n" \
              "{sol}\n" \
              "$$수식$${A}$$/수식$$의 배수는 {muls}이므로 모두 $$수식$${s}$$/수식$$개입니다.\n\n"


    A = [3, 4, 6, 7][np.random.randint(0, 4)]
    s = np.random.randint(3, 6)
    k = random.sample(list(range(2, 35)), s)

    while True:
        a = random.sample(list(range(2, 100)), 10 - s)
        flag = True
        for i in range(0, len(a)):
            if a[i] % A == 0:
                flag = False
                break
        if flag:
            break

    sol = ''
    muls = ''

    for i in range(0, len(k)):
        an = A*k[i]
        a.append(an)
        sol = sol + "$$수식$${A} TIMES {kn} = {an}$$/수식$$".format(A=A, kn=k[i], an=an)
        muls = muls + "$$수식$${an}$$/수식$$".format(an=an)
        if i != len(k) - 1:
            sol = sol + ", "
            muls = muls + ", "

    np.random.shuffle(a)

    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = a

    stem = stem.format(A=A, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7, a8=a8, a9=a9, a10=a10)
    answer = answer.format(s=s)
    comment = comment.format(A=A, s=s, sol=sol, muls=muls)

    return stem, answer, comment









# 5-1-2-10
def denandmul512_Stem_008():
    stem = "$$수식$${B}$$/수식$$보다 크고 $$수식$${C}$$/수식$$보다 작은 수 중에서 $$수식$${A}$$/수식$$의 배수는 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "{sol}\n" \
              "따라서 $$수식$${B}$$/수식$$보다 크고 $$수식$${C}$$/수식$$보다 작은 수 중에서 $$수식$${A}$$/수식$$의 배수는 " \
              "{muls}{jo}로 $$수식$${S}$$/수식$$개입니다.\n\n"


    while True:
        A = np.random.randint(3, 9)
        k = np.random.randint(7, 15)
        a = np.random.randint(4, 7)
        S = a - 1
        B = A*k
        C = A*(k+a)
        if B < 100 and C < 100:
            break


    sol = ''
    muls = ''

    for i in range(1, a):
        kn = k + i
        an = A * kn
        sol = sol + "$$수식$${A} TIMES {kn} = {an}$$/수식$$".format(A=A, kn=kn, an=an)
        muls = muls + "$$수식$${an}$$/수식$$".format(an=an)
        if i != a - 1:
            sol = sol + ', '
            muls = muls + ', '


    jo = ""
    last = (A*(k+a-1)) % 10

    if last == 0 or last == 3 or last == 6:
        jo = "으"

    stem = stem.format(A=A, B=B, C=C)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, C=C, S=S, sol=sol, muls=muls, jo=jo)

    return stem, answer, comment









# 5-1-2-11
def denandmul512_Stem_009():
    stem = "$$수식$${A}$$/수식$$의 배수 중에서 $$수식$${B}$$/수식$$에 가장 가까운 수를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A} TIMES {a} = {C}$$/수식$$, $$수식$${A} TIMES {a2} = {D}$$/수식$$\n" \
              "$$수식$${B} - {C} = {b}$$/수식$$, $$수식$${D} - {B} = {c}$$/수식$$" \
              "이므로 $$수식$${A}$$/수식$$의 배수 중에서 $$수식$${B}$$/수식$$에 가장 가까운 수는 $$수식$${S}$$/수식$$입니다.\n\n"


    while True:
        A = np.random.randint(6, 10)
        while True:
            B = np.random.randint(51, 100)
            if B % A != 0:
                break
        a = int(B/A)
        C = A*a
        D = A*(a + 1)
        b = B - C
        c = D - B
        if b != c:
            break

    if b < c:
        S = C
    else:
        S = D

    stem = stem.format(A=A, B=B)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, S=S, a=a, a2=a+1, C=C, D=D, b=b, c=c)

    return stem, answer, comment












# 5-1-2-12
def denandmul512_Stem_010():
    stem = "$$수식$${A}$$/수식$${j1} 어떤 수로 나누었을 때 나누어 떨어지는 수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$${j1} 어떤 수로 나누었을 때 나누어 떨어지는 수는 $$수식$${A}$$/수식$$의 약수입니다.\n" \
              "즉, 어떤 수는 $$수식$${A}$$/수식$$의 약수입니다.\n" \
              "$$수식$${A}$$/수식$$의 약수: {divs}\n따라서 어떤 수는 $$수식$${S}$$/수식$$개입니다.\n\n"


    while True:
        A = np.random.randint(12, 40)
        divisor = getdivisor(A)
        S = len(divisor)
        if S > 2:
            break

    divs = ''

    for i in range(0, S):
        divs = divs + "$$수식$${an}$$/수식$$".format(an=divisor[i])
        if i != S - 1:
            divs = divs + ", "

    j1 = proc_jo(A, 1)

    stem = stem.format(A=A, j1=j1)
    answer = answer.format(S=S)
    comment = comment.format(A=A, S=S, divs=divs, j1=j1)

    return stem, answer, comment









# 5-1-2-14
def denandmul512_Stem_011():
    stem = "어떤 수의 배수를 가장 작은 수부터 차례로 쓴 것입니다. $$수식$${box}$$/수식$$ 안에 알맞은 수를 써넣으세요.\n$$수식$${A1}$$/수식$$, $$수식$${A2}$$/수식$$, $$수식$${A3}$$/수식$$, $$수식$${A4}$$/수식$$, $$수식$${A5}$$/수식$$, $$수식$${A6}$$/수식$$, $$수식$${A7}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n"
    answer = "(정답)\n$$수식$${S1}$$/수식$$, $$수식$${S2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${B}$$/수식$${j1} $$수식$$1$$/수식$$배, $$수식$$2$$/수식$$배, $$수식$$3$$/수식$$배, $$수식$$CDOTS CDOTS$$/수식$$한 것이므로\n" \
              "$$수식$${B} TIMES {k1} = {S1}$$/수식$$, $$수식$${B} TIMES {k2} = {S2}$$/수식$$입니다.\n\n"


    box = "□"
    box1 = "box{%s````````````````````}"%"㉠"
    box2 = "box{%s````````````````````}"%"㉡"

    B = np.random.randint(6, 10)
    k = random.sample(list(range(2, 8)), 2)
    k.sort()
    k1, k2 = k

    A = []
    for i in range(1, 8):
        if i == k1:
            A.append(box1)
        elif i == k2:
            A.append(box2)
        else:
            A.append(B * i)

    A1, A2, A3, A4, A5, A6, A7 = A
    S1 = B*k1
    S2 = B*k2

    j1 = proc_jo(B, 1)

    stem = stem.format(box=box, A1=A1, A2=A2, A3=A3, A4=A4, A5=A5, A6=A6, A7=A7)
    answer = answer.format(S1=S1, S2=S2)
    comment = comment.format(B=B, S1=S1, S2=S2, k1=k1, k2=k2, j1=j1)

    return stem, answer, comment












# 5-1-2-15
def denandmul512_Stem_012():
    stem = "{A} $$수식$${B}$$/수식$$개를 학생들에게 남김없이 똑같이 나누어 주려고 합니다. {A}을 학생들에게 나누어 줄 수 있는 방법은 모두 몇 가지인가요? $$수식$$LEFT ($$/수식$$단, {A} $$수식$${B}$$/수식$$개를 학생 한 명에게 모두 주지는 않습니다.$$수식$$RIGHT )$$/수식$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$가지\n"
    comment = "(해설)\n" \
              "{A} $$수식$${B}$$/수식$$개를 학생들에게 남김없이 똑같이 나누어 주려면 " \
              "$$수식$${B}$$/수식$${jo} 나누어 떨어지게 하는 수, 즉 $$수식$${B}$$/수식$$의 약수를 구하면 됩니다.\n" \
              "{sol}\n→ $$수식$${B}$$/수식$$의 약수: {divs}\n" \
              "{A}을 학생 {divs2}에게 똑같이 나누어 줄 수 있습니다.\n" \
              "따라서 나누어 줄 수 있는 방법은 모두 $$수식$${S}$$/수식$$가지입니다.\n\n"


    A = ['사탕', '초콜릿', '공책', '연필', '구슬'][np.random.randint(0, 5)]

    while True:
        B = np.random.randint(31, 50)
        divisor = getdivisor(B)
        if len(divisor) >= 3:
            break

    S = len(divisor)

    last = B % 10

    jo = "을"

    if last == 2 or last == 4 or last == 5 or last == 9:
        jo = "를"

    sol = ''
    divs = ''
    divs2 = ''

    for i in range(0, len(divisor)):
        an = divisor[i]
        bn = int(B / an)
        sol = sol + "$$수식$${B} DIV {an} = {bn}$$/수식$$".format(B=B, an=an, bn=bn)
        divs = divs + "$$수식$${an}$$/수식$$".format(an=an)
        divs2 = divs2 + "$$수식$${an}$$/수식$$명".format(an=an)
        if i != len(divisor) - 1:
            sol = sol + ', '
            divs = divs + ', '
            divs2 = divs2 + ', '

    stem = stem.format(A=A, B=B)
    answer = answer.format(S=S)
    comment = comment.format(S=S, A=A, B=B, jo=jo, sol=sol, divs=divs, divs2=divs2)

    return stem, answer, comment










# 5-1-2-16
def denandmul512_Stem_013():
    stem = "터미널에서 {P1}으로 가는 버스가 오전 $$수식$${B}$$/수식$$시부터 $$수식$${A}$$/수식$$분 간격으로 출발합니다. 오전 $$수식$${C}$$/수식$$시까지 버스는 모두 몇 번 출발하나요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$번\n"
    comment = "(해설)\n" \
              "오전 $$수식$${B}$$/수식$$시에 첫차가 출발하고 $$수식$${A}$$/수식$$분 간격으로 출발하므로 " \
              "$$수식$${A}$$/수식$$의 배수가 출발 시각입니다.\n따라서 출발 시각은 {times}$$수식$$CDOTS CDOTS$$/수식$$이므로 " \
              "오전 $$수식$${B}$$/수식$$시부터 오전 $$수식$${C}$$/수식$$시까지 버스는 모두 $$수식$${S}$$/수식$$번 출발합니다.\n\n"


    P1 = ['동물원', '식물원', '놀이공원', '박물관', '미술관'][np.random.randint(0, 5)]

    pick = np.random.randint(0, 3)

    A = [15, 20, 30][pick]
    gap = [[0, 15, 30, 45], [0, 20, 40], [0, 30]][pick]
    gapsize = len(gap)

    B = np.random.randint(9, 11)
    C = 11
    S = int((C*60 - B*60)/A) + 1

    times = ''
    hour = B - 1

    for i in range(0, S):
        minute = gap[i % gapsize]
        if minute == 0:
            hour = hour + 1
        times = times + "오전 $$수식$${hour}$$/수식$$시".format(hour=hour)
        if minute != 0:
            times = times + " $$수식$${minute}$$/수식$$분".format(minute=minute)
        if i != S - 1:
            times = times + ", "

    stem = stem.format(P1=P1, A=A, B=B, C=C)
    answer = answer.format(S=S)
    comment = comment.format(S=S, A=A, B=B, C=C, times=times)

    return stem, answer, comment














# 5-1-2-17
def denandmul512_Stem_014():
    stem = "어떤 수의 배수를 가장 작은 수부터 쓴 것입니다. $$수식$${A}$$/수식$$번째의 수를 구해 보세요.\n$$표$$$$수식$${B1}$$/수식$$, $$수식$${B2}$$/수식$$, $$수식$${B3}$$/수식$$, $$수식$${B4}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${B1}$$/수식$$, $$수식$${B2}$$/수식$$, $$수식$${B3}$$/수식$$, $$수식$${B4}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$는 " \
              "$$수식$${B1}$$/수식$$의 배수입니다.\n따라서 $$수식$${A}$$/수식$$번째의 수는 $$수식$${B1} TIMES {A} = {S}$$/수식$$입니다.\n\n"


    A = np.random.randint(11, 16)
    B1 = np.random.randint(3, 7)

    S = A*B1

    B2 = B1 * 2
    B3 = B1 * 3
    B4 = B1 * 4

    stem = stem.format(A=A, B1=B1, B2=B2, B3=B3, B4=B4)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B1=B1, B2=B2, B3=B3, B4=B4, S=S)

    return stem, answer, comment









# 5-1-2-18
def denandmul512_Stem_015():
    stem = "다음 중 $$수식$${A}$$/수식$$의 약수를 찾아 그 수의 약수는 몇 개인지 구해 보세요.\n$$표$$$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$, $$수식$${a4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${m}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 약수: {divs1}\n" \
              "$$수식$${b1}$$/수식$$의 약수: {divs2} → $$수식$${m}$$/수식$$개\n\n"

    while True:
        while True:
            A = np.random.randint(20, 60)
            divisor1 = getdivisor(A)
            if len(divisor1) > 3:
                break
    
        b1 = random.sample(divisor1, 1)[0]
        divisor2 = getdivisor(b1)

        b2, b3, b4 = random.sample(list(range(5, A)), 3)
        dv1 = getdivisor(b2)
        dv2 = getdivisor(b3)
        dv3 = getdivisor(b4)
    
        if b1 > 5 and b1 < A and len(divisor2) > 3 and (b2 not in divisor1) and (b3 not in divisor1) and (b4 not in divisor1) and len(dv1) > 2 and len(dv2) > 2 and len(dv3) > 2:
            break

    aa = [b1, b2, b3, b4]
    aa.sort()
    a1, a2, a3, a4 = aa

    m = len(divisor2)

    divs1 = ''
    for i in range(0, len(divisor1)):
        divs1 = divs1 + "$$수식$${div}$$/수식$$".format(div=divisor1[i])
        if i != len(divisor1) - 1:
            divs1 = divs1 + ', '

    divs2 = ''
    for i in range(0, len(divisor2)):
        divs2 = divs2 + "$$수식$${div}$$/수식$$".format(div=divisor2[i])
        if i != len(divisor2) - 1:
            divs2 = divs2 + ', '

    stem = stem.format(A=A, a1=a1, a2=a2, a3=a3, a4=a4)
    answer = answer.format(m=m)
    comment = comment.format(A=A, b1=b1, divs1=divs1, divs2=divs2, m=m)

    return stem, answer, comment












# 5-1-2-19
def denandmul512_Stem_016():
    stem = "과수원에서 {P1}를 한 상자에 $$수식$${A}$$/수식$$개씩 담고 있습니다. 상자에 담은 {P1}가 $$수식$${B1}$$/수식$$개보다 많고 $$수식$${B2}$$/수식$$개보다 적을 때 {P1}를 담은 상자는 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${A} TIMES {a1} = {b1}$$/수식$$, $$수식$${A} TIMES {a2} = {b2}$$/수식$$, " \
              "$$수식$${A} TIMES {a3} = {b3}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "$$수식$${B1}$$/수식$$보다 크고 $$수식$${B2}$$/수식$$보다 작은 " \
              "$$수식$${A}$$/수식$$의 배수는 $$수식$${b2}$$/수식$$입니다.\n" \
              "따라서 {P1}를 담은 상자는 $$수식$${S}$$/수식$$개입니다.\n\n"


    P1 = ['사과', '딸기', '포도', '복숭아', '배', '참외'][np.random.randint(0, 6)]

    while True:
        A = np.random.randint(6, 14)
        B1 = np.random.randint(6, 10) * 10
        B2 = B1 + 10
        a2 = int(B1 / A) + 1
        a1 = a2 - 1
        a3 = a2 + 1
        b1 = A*a1
        b2 = A*a2
        b3 = A*a3
        flag = True

        if (b2 <= B1 or b2 >= B2) or (b1 > B1 and b1 < B2) or (b3 > B1 and b3 < B2):
            flag = False
        if flag:
            break

    S = a2

    stem = stem.format(P1=P1, A=A, B1=B1, B2=B2)
    answer = answer.format(S=S)
    comment = comment.format(P1=P1, A=A, B1=B1, B2=B2, S=S, a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3)

    return stem, answer, comment













# 5-1-2-20
def denandmul512_Stem_017():
    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지 수 중 $$수식$${box}$$/수식$$ 안에 들어갈 수 있는 수를 모두 구해 보세요.\n$$표$$$$수식$${A}$$/수식$$의 배수는 모두 $$수식$${box}$$/수식$$의 배수입니다.$$/표$$\n"
    answer = "(정답)\n{S}\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 약수는 {divs}이므로 $$수식$${A}$$/수식$$의 배수는 {divs}의 배수입니다.\n" \
              "따라서 $$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지 수 중 $$수식$${box}$$/수식$$ 안에 들어갈 수 있는 수는 {S}입니다.\n\n"

    box = "□"

    while True:
        A = np.random.randint(11, 30)
        divisor = getdivisor(A)
        if len(divisor) > 2:
            break

    divs = ''

    for i in range(0, len(divisor)):
        divs = divs + "$$수식$${an}$$/수식$$".format(an=divisor[i])
        if i != len(divisor) - 1:
            divs = divs + ", "
    S = ''

    for i in range(0, len(divisor)):
        if divisor[i] > 9:
            break
        S = S + "$$수식$${an}$$/수식$$".format(an=divisor[i])
        if i + 1 < len(divisor) and divisor[i + 1] <= 9:
            S = S + ", "

    stem = stem.format(A=A, box=box)
    answer = answer.format(S=S)
    comment = comment.format(A=A, box=box, S=S, divs=divs)

    return stem, answer, comment














# 5-1-2-21
def denandmul512_Stem_018():
    stem = "두 수가 서로 약수와 배수의 관계인 것은 어느 것인가요?\n① $$수식$$LEFT ( {a1}$$/수식$$, $$수식$${b1} RIGHT )$$/수식$$     ② $$수식$$LEFT ( {a2}$$/수식$$, $$수식$${b2} RIGHT )$$/수식$$     ③ $$수식$$LEFT ( {a3}$$/수식$$, $$수식$${b3} RIGHT )$$/수식$$\n④ $$수식$$LEFT ( {a4}$$/수식$$, $$수식$${b4} RIGHT )$$/수식$$     ⑤ $$수식$$LEFT ( {a5}$$/수식$$, $$수식$${b5} RIGHT )$$/수식$$\n"
    answer = "(정답)\n{K}\n"
    comment = "(해설)\n" \
              "큰 수를 작은 수로 나누었을 때 나누어떨어지는 것을 찾습니다.\n" \
              "{K} $$수식$${c1} DIV {d1} = {a}$$/수식$$\n\n"

    while True:
        c = random.sample(list(range(11, 60)), 5)
        d = random.sample(list(range(3, 10)), 5)
        for i in range(1, len(c)):
            while c[i] % d[i] == 0:
                d[i] = np.random.randint(3, 10)
        if c[0] % d[0] == 0:
            break

    c1 = c[0]
    d1 = d[0]
    a = int(c1/d1)

    cd = []
    for i in range(0, len(c)):
        row = [c[i], d[i]]
        np.random.shuffle(row)
        cd.append(row)
    np.random.shuffle(cd)

    [[a1, b1], [a2, b2], [a3, b3], [a4, b4], [a5, b5]] = cd

    for i in range(0, len(cd)):
        if cd[i][0] == c1 or cd[i][1] == c1:
            K = answer_dict[i]

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, b1=b1, b2=b2, b3=b3, b4=b4, b5=b5)
    answer = answer.format(K=K)
    comment = comment.format(K=K, a=a, c1=c1, d1=d1)

    return stem, answer, comment
















# 5-1-2-23
def denandmul512_Stem_019():
    stem = "$$수식$${A}$$/수식$${joA} ■의 배수입니다. ■에 알맞지 않은 수를 모두 고르세요.\n$$표$$$$수식$${b1}$$/수식$$   $$수식$${b2}$$/수식$$   $$수식$${b3}$$/수식$$   $$수식$${s1}$$/수식$$   $$수식$${s2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$\n"
    comment = "(해설)\n" \
              "■는 $$수식$${A}$$/수식$$의 약수입니다.\n" \
              "$$수식$${b1}$$/수식$$, $$수식$${b2}$$/수식$$, $$수식$${b3}$$/수식$${joB3} $$수식$${A}$$/수식$$의 약수이고 " \
              "$$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$${joS2} $$수식$${A}$$/수식$$의 배수입니다.\n\n"


    while True:
        A = np.random.randint(11, 30)
        divisor = getdivisor(A)
        if len(divisor) >= 4:
            break

    b = random.sample(divisor, 3)
    b.sort()
    b1, b2, b3 = b

    s1 = A*2
    s2 = A*3

    joA = "은"
    lastA = A % 10
    if lastA == 2 or lastA == 4 or lastA == 5 or lastA == 9:
        joA = "는"

    joB3 = "은"
    lastB = b3 % 10
    if lastB == 2 or lastB == 4 or lastB == 5 or lastB == 9:
        joB3 = "는"

    joS2 = "은"
    lastS = s2 % 10
    if lastS == 2 or lastS == 4 or lastS == 5 or lastS == 9:
        joS2 = "는"

    stem = stem.format(s1=s1, s2=s2, b1=b1, b2=b2, b3=b3, A=A, joA=joA)
    answer = answer.format(s1=s1, s2=s2)
    comment = comment.format(s1=s1, s2=s2, b1=b1, b2=b2, b3=b3, A=A, joB3=joB3, joS2=joS2)

    return stem, answer, comment










# 5-1-2-24
def denandmul512_Stem_020():
    stem = "식을 보고 바르게 설명한 것을 모두 골라 보세요.\n$$표$$$$수식$${b1} TIMES {b2} = {A}$$/수식$$$$/표$$\n{Y1}\n"
    answer = "(정답)\n{k1}, {k2}\n"
    comment = "(해설)\n" \
              "{Y2}⑤ $$수식$${A}$$/수식$$의 약수는 {divs}로 모두 $$수식$${divnum}$$/수식$$개입니다.\n\n"


    pick = np.random.randint(0, 2)

    while True:
        A = np.random.randint(16, 50)
        divisor = getdivisor(A)
        if len(divisor) >= 4:
            break

    divisor2 = divisor.copy()
    divisor2.remove(1)
    divisor2.remove(A)
    b1 = random.sample(divisor2, 1)[0]
    b2 = int(A/b1)

    divnum = len(divisor)
    divs = ''
    for i in range(0, len(divisor)):
        divs = divs + "$$수식$${an}$$/수식$$".format(an=divisor[i])
        if i != len(divisor) - 1:
            divs = divs + ', '

    j1 = proc_jo(A, -1)
    j2 = proc_jo(b1, -1)
    j3 = proc_jo(b2, -1)


    Y1 = ["① $$수식$${A}$$/수식$${j1} $$수식$${b1}$$/수식$$의 배수입니다.\n"
          "② $$수식$${A}$$/수식$${j1} $$수식$${b2}$$/수식$$의 약수입니다.\n"
          "③ $$수식$${b1}$$/수식$${j2} $$수식$${A}$$/수식$$의 배수입니다.\n"
          "④ $$수식$${b2}$$/수식$${j3} $$수식$${A}$$/수식$$의 약수입니다.\n"
          "⑤ $$수식$${A}$$/수식$$의 약수는 모두 $$수식$$2$$/수식$$개입니다.".format(A=A, b1=b1, b2=b2, j1=j1, j2=j2, j3=j3),
          "① $$수식$${b1}$$/수식$${j2} $$수식$${A}$$/수식$$의 배수입니다.\n"
          "② $$수식$${b2}$$/수식$${j3} $$수식$${A}$$/수식$$의 약수입니다.\n"
          "③ $$수식$${A}$$/수식$${j1} $$수식$${b1}$$/수식$$의 배수입니다.\n"
          "④ $$수식$${A}$$/수식$${j1} $$수식$${b2}$$/수식$$의 약수입니다.\n"
          "⑤ $$수식$${A}$$/수식$$의 약수는 모두 $$수식$$2$$/수식$$개입니다.".format(A=A, b1=b1, b2=b2, j1=j1, j2=j2, j3=j3)][pick]

    Y2 = ["② $$수식$${A}$$/수식$${j1} $$수식$${b2}$$/수식$$의 배수입니다.\n"
          "③ $$수식$${b1}$$/수식$${j2} $$수식$${A}$$/수식$$의 약수입니다.\n".format(A=A, b1=b1, b2=b2, j1=j1, j2=j2),
          "① $$수식$${b1}$$/수식$${j2} $$수식$${A}$$/수식$$의 약수입니다.\n"
          "④ $$수식$${A}$$/수식$${j1} $$수식$${b2}$$/수식$$의 배수입니다.\n".format(A=A, b1=b1, b2=b2, j1=j1, j2=j2)][pick]

    k1, k2 = [['①', '④'], ['②', '③']][pick]

    stem = stem.format(b1=b1, b2=b2, A=A, Y1=Y1)
    answer = answer.format(k1=k1, k2=k2)
    comment = comment.format(A=A, divs=divs, divnum=divnum, Y2=Y2)

    return stem, answer, comment














# 5-1-2-25
def denandmul512_Stem_021():
    stem = "{P1}일 때, $$수식$${box}$$/수식$$ 안에 들어갈 수 있는 수는 모두 몇 개인가요?\n$$표$$$$수식$$LEFT ( {A}$$/수식$$, $$수식$${box} ` RIGHT )$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${n}$$/수식$$개\n"
    comment = "(해설)\n" \
              "{P2}\n" \
              "$$수식$${A}$$/수식$$의 약수는 {divs} 이므로 " \
              "$$수식$${box}$$/수식$$ 안에 들어갈 수 있는 수는 모두 $$수식$${n}$$/수식$$개입니다.\n\n"


    box = "□"

    while True:
        A = np.random.randint(11, 40)
        divisor = getdivisor(A)
        if len(divisor) >= 4:
            break

    n = len(divisor)

    divs = ''

    for i in range(0, len(divisor)):
        divs = divs + "$$수식$${an}$$/수식$$".format(an=divisor[i])
        if i != len(divisor) - 1:
            divs = divs + ', '

    pick = np.random.randint(0, 2)

    P1 = ['왼쪽 수가 오른쪽 수의 배수', '오른쪽 수가 왼쪽 수의 약수'][pick]
    P2 = ['$$수식$${A}$$/수식$$가 $$수식$${box}$$/수식$$의 배수이므로 $$수식$${box}$$/수식$$는 $$수식$${A}$$/수식$$의 약수입니다'.format(A=A, box=box),
          '$$수식$${box}$$/수식$$는 $$수식$${A}$$/수식$$의 약수입니다'.format(A=A, box=box)][pick]

    stem = stem.format(P1=P1, box=box, A=A)
    answer = answer.format(n=n)
    comment = comment.format(P2=P2, A=A, divs=divs, box=box, n=n)

    return stem, answer, comment













# 5-1-2-26
def denandmul512_Stem_022():
    stem = "$$수식$${A}$$/수식$${j1} 약수와 배수의 관계인 수를 모두 찾아 써 보세요.\n$$표$$$$수식$${a1}$$/수식$$   $$수식$${a2}$$/수식$$   $$수식$${a3}$$/수식$$   $$수식$${a4}$$/수식$$   $$수식$${a5}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$$\n"
    comment = "(해설)\n" \
              "큰 수를 작은 수로 나누었을 때 나누어떨어지면 두 수는 약수와 배수의 관계입니다.\n" \
              "{S}\n" \
              "따라서 $$수식$${A}$$/수식$${j1} 약수와 배수의 관계인 수는 $$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$$입니다.\n\n"


    while True:
        A = np.random.randint(11, 30)
        divisor = getdivisor(A)
        if len(divisor) >= 4:
            break

    divisor2 = divisor.copy()
    divisor2.remove(1)
    divisor2.remove(A)
    b1 = random.sample(divisor2, 1)[0]

    while True:
        k2, k3 = random.sample(list(range(2, 10)), 2)
        b2 = A * k2
        b3 = A * k3
        if b2 < 100 and b3 < 100:
            break

    while True:
        b4, b5 = random.sample(list(range(1, A)), 2)
        if A % b4 != 0 and A % b5 != 0:
            break

    b = [b1, b2, b3, b4, b5]
    b.sort()
    a1, a2, a3, a4, a5 = b

    s = [b1, b2, b3]
    s.sort()
    s1, s2, s3 = s
    S = ''

    for i in range(0, 3):
        if A % b[i] == 0:
            S = S + "$$수식$${A} DIV {bn} = {cn}$$/수식$$".format(A=A, bn=b[i], cn=int(A/b[i]))
        else:
            S = S + "$$수식$${A} DIV {bn} = {cn} CDOTS {dn}$$/수식$$".format(A=A, bn=b[i], cn=int(A / b[i]), dn=A%b[i])
        S = S + ", "

    for i in range(3, len(b)):
        if b[i] % A == 0:
            S = S + "$$수식$${bn} DIV {A} = {cn}$$/수식$$".format(A=A, bn=b[i], cn=int(b[i]/A))
        else:
            S = S + "$$수식$${bn} DIV {A} = {cn} CDOTS {dn}$$/수식$$".format(A=A, bn=b[i], cn=int(b[i]/A), dn=b[i]%A)
        if i != len(b) - 1:
            S = S + ", "

    j1 = proc_jo(A, 2)

    stem = stem.format(A=A, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, j1=j1)
    answer = answer.format(s1=s1, s2=s2, s3=s3)
    comment = comment.format(S=S, A=A, s1=s1, s2=s2, s3=s3, j1=j1)

    return stem, answer, comment
















# 5-1-2-27
def denandmul512_Stem_023():
    stem = "두 수가 약수와 배수의 관계인 것을 찾아 기호를 써 보세요.\n㉠ $$수식$${box1}$$/수식$$$$수식$${box2}$$/수식$$    ㉡ $$수식$${box3}$$/수식$$$$수식$${box4}$$/수식$$\n"
    answer = "(정답)\n{K}\n"
    comment = "(해설)\n" \
              "{P}\n" \
              "따라서 두 수가 약수와 배수의 관계인 것은 {K}입니다.\n\n"


    while True:
        a1, a2 = random.sample(list(range(3, 9)), 2)
        b1, b2 = random.sample(list(range(31, 80)), 2)
        if b1 % a1 == 0 and b2 % a2 != 0:
            K = '㉠'
            P = "㉠ $$수식$${b1} DIV {a1} = {c1}$$/수식$$, " \
                "㉡ $$수식$${b2} DIV {a2} = {c2} CDOTS {d2}$$/수식$$".format(a1=a1, a2=a2, b1=b1, b2=b2, c1=int(b1/a1), c2=int(b2/a2), d2=b2 % a2)
            break
        elif b1 % a1 != 0 and b2 % a2 == 0:
            K = '㉡'
            P = "㉠ $$수식$${b1} DIV {a1} = {c1} CDOTS {d1}$$/수식$$, " \
                "㉡ $$수식$${b2} DIV {a2} = {c2}$$/수식$$".format(a1=a1, a2=a2, b1=b1, b2=b2, c1=int(b1 / a1), c2=int(b2 / a2), d1=b1 % a1)
            break


    box1 = "box{%d}" % a1
    box2 = "box{%d}" % b1

    box3 = "box{%d}" % a2
    box4 = "box{%d}" % b2


    stem = stem.format(a1=a1, a2=a2, b1=b1, b2=b2, box1=box1, box2=box2, box3=box3, box4=box4)
    answer = answer.format(K=K)
    comment = comment.format(K=K, P=P)

    return stem, answer, comment












# 5-1-2-28
def denandmul512_Stem_024():
    stem = "다음에서 공통으로 설명하고 있는 수를 모두 구해 보세요.\n$$표$$∙ $$수식$${A}$$/수식$${josa} 이 수의 약수입니다.\n∙ $$수식$${B}$$/수식$$보다 큰 두 자리 수입니다.\n∙ $$수식$${C}$$/수식$$의 배수입니다.$$/표$$\n"
    answer = "(정답)\n{S}\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 배수이고, $$수식$${B}$$/수식$$보다 큰 두 자리 수는 {an}입니다.\n" \
              "이 중에서 $$수식$${C}$$/수식$$의 배수는 {S}입니다.\n\n"


    A = np.random.randint(6, 10)
    B = np.random.randint(4, 7) * 10
    an = ''

    anlist = []
    for i in range(0, 20):
        cur = A * i
        if cur > B and cur < 100:
            an = an + "$$수식$${cur}$$/수식$$".format(cur=cur)
            anlist.append(cur)
            next = A * (i+1)
            if next > B and next < 100:
                an = an + ", "

    while True:
        C = np.random.randint(2, 10)
        if A % C != 0:
            break

    S = ''

    for i in range(0, len(anlist)):
        if anlist[i] % C == 0:
            S = S + "$$수식$${sn}$$/수식$$, ".format(sn=anlist[i])

    S = S[:-2]

    if A in [2,4,5,9]:
        josa = "는"
    else:
        josa = "은"

    stem = stem.format(A=A, B=B, C=C, josa=josa)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, C=C, S=S, an=an)

    return stem, answer, comment















# 5-1-2-29
def denandmul512_Stem_025():
    stem = "$$수식$${A}$$/수식$$이 $$수식$${box}$$/수식$$의 배수일 때, $$수식$${box}$$/수식$$에 들어갈 수 있는 수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${n}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$이 $$수식$${box}$$/수식$$의 배수이므로 $$수식$${box}$$/수식$$는 $$수식$${A}$$/수식$$의 약수입니다.\n" \
              "$$수식$${A}$$/수식$$의 약수: {divs}\n" \
              "따라서 $$수식$${box}$$/수식$$에 들어갈 수 있는 수는 {divs}으로 모두 $$수식$${n}$$/수식$$개입니다.\n\n"


    box = "□"

    while True:
        A = np.random.randint(11, 90)
        divisor = getdivisor(A)
        if len(divisor) >= 5:
            break

    n = len(divisor)

    divs = ''

    for i in range(0, len(divisor)):
        divs = divs + "$$수식$${an}$$/수식$$".format(an=divisor[i])
        if i != len(divisor) - 1:
            divs = divs + ', '

    stem = stem.format(A=A, box=box)
    answer = answer.format(n=n)
    comment = comment.format(A=A, box=box, divs=divs, n=n)

    return stem, answer, comment
















# 5-1-2-31
def denandmul512_Stem_026():
    stem = "다음 중 $$수식$${box}$$/수식$$안에 공통으로 들어갈 수 있는 수를 찾아 기호를 써 보세요.\n$$표$$∙ $$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$${josa} $$수식$${box}$$/수식$$의 약수입니다.\n∙ $$수식$${box}$$/수식$$는 $$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 배수입니다.$$/표$$\n$$표$$㉠ $$수식$${a1}$$/수식$$   ㉡ $$수식$${a2}$$/수식$$   ㉢ $$수식$${a3}$$/수식$$   ㉣ $$수식$${a4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{K}\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 곱이 들어 있는 수를 찾으면\n" \
              "{K} $$수식$${S} = {divsmul}$$/수식$$이므로 " \
              "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$는 $$수식$${S}$$/수식$$의 약수이고, " \
              "$$수식$${S}$$/수식$$은 $$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 배수입니다.\n" \
              "따라서 $$수식$${box}$$/수식$$안에 공통으로 들어갈 수 있는 수를 찾아 기호를 쓰면 {K}입니다.\n\n"


    box = "□"

    while True:
        A = np.random.randint(2, 8)
        B = np.random.randint(2, 6)
        if A != B:
            break

    while True:
        S = np.random.randint(41, 90)
        if S % A == 0 and S % B == 0:
            break

    while True:
        s2, s3, s4 = random.sample(list(range(41, 90)), 3)
        if (s2 % A != 0 or s2 % B != 0) and (s3 % A != 0 or s3 % B != 0) and (s4 % A != 0 or s4 % B != 0):
            break

    slist = [S, s2, s3, s4]
    slist.sort()
    a1, a2, a3, a4 = slist

    for i in range(0, len(slist)):
        if slist[i] == S:
            K = answer_kodict[i]

    divisor = getdivisor(S)
    divisor.remove(1)
    divisor.remove(S)

    divsmul = ''

    for i in range(0, len(divisor)):
        divsmul = divsmul + "{an}".format(an=divisor[i])
        if i != len(divisor) - 1:
            divsmul = divsmul + 'TIMES'

    j1 = proc_jo(A, 2)

    if B in [2,4,5,9]:
        josa = "는"
    else:
        josa = "은"

    stem = stem.format(box=box, A=A, B=B, a1=a1, a2=a2, a3=a3, a4=a4, j1=j1, josa=josa)
    answer = answer.format(K=K)
    comment = comment.format(A=A, B=B, box=box, K=K, S=S, divsmul=divsmul, j1=j1)

    return stem, answer, comment














# 5-1-2-32
def denandmul512_Stem_027():
    stem = "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 약수: {divs1}\n" \
              "$$수식$${B}$$/수식$$의 약수: {divs2}\n" \
              "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수: {divs3} → $$수식$${S}$$/수식$$개\n\n"


    while True:
        A = np.random.randint(10, 31)
        B = np.random.randint(31, 51)

        divisor1 = getdivisor(A)
        divisor2 = getdivisor(B)
        divisor3 = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        divisor3.sort()

        S = len(divisor3)
        if S > 1:
            break

    divs1 = ''

    for i in range(0, len(divisor1)):
        divs1 = divs1 + "$$수식$${an}$$/수식$$".format(an=divisor1[i])
        if i != len(divisor1) - 1:
            divs1 = divs1 + ', '

    divs2 = ''

    for i in range(0, len(divisor2)):
        divs2 = divs2 + "$$수식$${an}$$/수식$$".format(an=divisor2[i])
        if i != len(divisor2) - 1:
            divs2 = divs2 + ', '

    divs3 = ''

    for i in range(0, len(divisor3)):
        divs3 = divs3 + "$$수식$${an}$$/수식$$".format(an=divisor3[i])
        if i != len(divisor3) - 1:
            divs3 = divs3 + ', '

    j1 = proc_jo(A, 2)

    stem = stem.format(A=A, B=B, j1=j1)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, S=S, divs1=divs1, divs2=divs2, divs3=divs3, j1=j1)

    return stem, answer, comment

















# 5-1-2-34
def denandmul512_Stem_028():
    stem = "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수가 아닌 것은 어느 것인가요?\n① $$수식$${a1}$$/수식$$     ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n④ $$수식$${a4}$$/수식$$     ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{K}\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 약수: {divs1}\n" \
              "$$수식$${B}$$/수식$$의 약수: {divs2}\n" \
              "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수: {divs3}\n\n"


    while True:
        A = np.random.randint(10, 41)
        B = np.random.randint(41, 71)

        divisor1 = getdivisor(A)
        divisor2 = getdivisor(B)
        divisor3 = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        divisor3.sort()

        S = len(divisor3)
        if S >= 4:
            break

    while True:
        c5 = np.random.randint(10, B)
        if c5 not in divisor3:
            break

    c = random.sample(divisor3, 4)
    c.sort()
    # c1, c2, c3, c4 = c

    c.append(c5)
    c.sort()
    a1, a2, a3, a4, a5 = c
    for i in range(0, len(c)):
        if c[i] == c5:
            K = answer_dict[i]

    divs1 = ''
    for i in range(0, len(divisor1)):
        divs1 = divs1 + "$$수식$${an}$$/수식$$".format(an=divisor1[i])
        if i != len(divisor1) - 1:
            divs1 = divs1 + ', '
    divs2 = ''
    for i in range(0, len(divisor2)):
        divs2 = divs2 + "$$수식$${an}$$/수식$$".format(an=divisor2[i])
        if i != len(divisor2) - 1:
            divs2 = divs2 + ', '
    divs3 = ''
    for i in range(0, len(divisor3)):
        divs3 = divs3 + "$$수식$${an}$$/수식$$".format(an=divisor3[i])
        if i != len(divisor3) - 1:
            divs3 = divs3 + ', '

    j1 = proc_jo(A, 2)

    stem = stem.format(A=A, B=B, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, j1=j1)
    answer = answer.format(K=K)
    comment = comment.format(A=A, B=B, divs1=divs1, divs2=divs2, divs3=divs3, j1=j1)

    return stem, answer, comment


















# 5-1-2-35
def denandmul512_Stem_029():
    stem = "다음 중 $$수식$${A}$$/수식$${josa} $$수식$${B}$$/수식$$의 공약수는 모두 몇 개인가요?\n$$표$$$$수식$$1$$/수식$$,     $$수식$$2$$/수식$$,     $$수식$$3$$/수식$$,     $$수식$$4$$/수식$$,     $$수식$$5$$/수식$$,     $$수식$$6$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 약수: {divs1}\n" \
              "$$수식$${B}$$/수식$$의 약수: {divs2}\n" \
              "따라서 $$수식$${A}$$/수식$${josa} $$수식$${B}$$/수식$$의 공약수는 {divs3}으로 모두 $$수식$${S}$$/수식$$개입니다.\n\n"


    while True:
        A = np.random.randint(8, 13)
        B = np.random.randint(14, 21)

        divisor1 = getdivisor(A)
        divisor2 = getdivisor(B)
        divisor3 = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        divisor3.sort()
        count = 0
        for i in range(0, len(divisor3)):
            if divisor3[i] > 6:
                count = count + 1
        S = len(divisor3) - count
        if S > 1:
            break


    divs1 = ''

    for i in range(0, len(divisor1)):
        divs1 = divs1 + "$$수식$${an}$$/수식$$".format(an=divisor1[i])
        if i != len(divisor1) - 1:
            divs1 = divs1 + ', '

    divs2 = ''

    for i in range(0, len(divisor2)):
        divs2 = divs2 + "$$수식$${an}$$/수식$$".format(an=divisor2[i])
        if i != len(divisor2) - 1:
            divs2 = divs2 + ', '

    divs3 = ''

    for i in range(0, S):
        divs3 = divs3 + "$$수식$${an}$$/수식$$".format(an=divisor3[i])
        if i != S - 1:
            divs3 = divs3 + ', '

    if int(str(A)[-1]) in [2,4,5,9]:
        josa = "와"
    else:
        josa = "과"

    stem = stem.format(A=A, B=B, josa=josa)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, divs1=divs1, divs2=divs2, divs3=divs3, S=S, josa=josa)

    return stem, answer, comment











# 5-1-2-36
def denandmul512_Stem_030():
    stem = "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수 중 가장 큰 수를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${maxnum}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 약수: {divs1}\n" \
              "$$수식$${B}$$/수식$$의 약수: {divs2}\n" \
              "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수: {divs3}\n" \
              "따라서 $$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수 중 가장 큰 수는 $$수식$${maxnum}$$/수식$$입니다.\n\n"


    while True:
        A = np.random.randint(21, 30)
        B = np.random.randint(41, 80)

        divisor1 = getdivisor(A)
        divisor2 = getdivisor(B)
        divisor3 = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        divisor3.sort()

        S = len(divisor3)
        if S > 2:
            break

    maxnum = divisor3[len(divisor3) - 1]

    divs1 = ''

    for i in range(0, len(divisor1)):
        divs1 = divs1 + "$$수식$${an}$$/수식$$".format(an=divisor1[i])
        if i != len(divisor1) - 1:
            divs1 = divs1 + ', '

    divs2 = ''

    for i in range(0, len(divisor2)):
        divs2 = divs2 + "$$수식$${an}$$/수식$$".format(an=divisor2[i])
        if i != len(divisor2) - 1:
            divs2 = divs2 + ', '

    divs3 = ''

    for i in range(0, len(divisor3)):
        divs3 = divs3 + "$$수식$${an}$$/수식$$".format(an=divisor3[i])
        if i != len(divisor3) - 1:
            divs3 = divs3 + ', '

    j1 = proc_jo(A, 2)

    stem = stem.format(A=A, B=B, j1=j1)
    answer = answer.format(maxnum=maxnum)
    comment = comment.format(A=A, B=B, divs1=divs1, divs2=divs2, divs3=divs3, maxnum=maxnum, j1=j1)

    return stem, answer, comment















# 5-1-2-37
def denandmul512_Stem_031():
    stem = "{P1}가 어떤 두 수의 공약수를 모두 말한 것입니다. 이 두 수의 최대공약수를 구해 보세요.\n$$표$${divs1}$$/표$$\n"
    answer = "(정답)\n$$수식$${maxnum}$$/수식$$\n"
    comment = "(해설)\n" \
              "공약수 중에서 가장 큰 수가 최대공약수입니다.\n" \
              "따라서 두 수의 최대공약수는 $$수식$${maxnum}$$/수식$$입니다.\n\n"


    P1 = ['연우', '민희', '지호', '민서', '수지', '영호', '선미', '윤지'][np.random.randint(0, 8)]

    while True:
        A = np.random.randint(6, 30)
        divisor1 = getdivisor(A)
        S = len(divisor1)
        if S >= 4 and S <= 6:
            break

    maxnum = divisor1[S - 1]

    divs1 = ''

    for i in range(0, len(divisor1)):
        divs1 = divs1 + "$$수식$${an}$$/수식$$".format(an=divisor1[i])
        if i != len(divisor1) - 1:
            divs1 = divs1 + ', '

    stem = stem.format(P1=P1, divs1=divs1)
    answer = answer.format(maxnum=maxnum)
    comment = comment.format(maxnum=maxnum)

    return stem, answer, comment














# 5-1-2-38
def denandmul512_Stem_032():
    stem = "$$수식$${A}$$/수식$${josa} $$수식$${B}$$/수식$$의 최대공약수를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${maxnum}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 약수: {divs1}\n" \
              "$$수식$${B}$$/수식$$의 약수: {divs2}\n" \
              "따라서 " \
              "$$수식$${A}$$/수식$${josa} $$수식$${B}$$/수식$$의 최대공약수는 $$수식$${maxnum}$$/수식$$입니다.\n\n"


    while True:
        while True:
            A = np.random.randint(11, 20)
            B = np.random.randint(11, 30)
            if A != B:
                break

        divisor1 = getdivisor(A)
        divisor2 = getdivisor(B)
        divisor3 = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        divisor3.sort()

        S = len(divisor3)
        if len(divisor1) >= 3 and len(divisor2) >= 3 and S >= 2:
            break

    maxnum = divisor3[len(divisor3) - 1]

    divs1 = ''

    for i in range(0, len(divisor1)):
        divs1 = divs1 + "$$수식$${an}$$/수식$$".format(an=divisor1[i])
        if i != len(divisor1) - 1:
            divs1 = divs1 + ', '

    divs2 = ''

    for i in range(0, len(divisor2)):
        divs2 = divs2 + "$$수식$${an}$$/수식$$".format(an=divisor2[i])
        if i != len(divisor2) - 1:
            divs2 = divs2 + ', '

    divs3 = ''

    for i in range(0, len(divisor3)):
        divs3 = divs3 + "$$수식$${an}$$/수식$$".format(an=divisor3[i])
        if i != len(divisor3) - 1:
            divs3 = divs3 + ', '

    if int(str(A)[-1]) in [2,4,5,9]:
        josa = "와"
    else:
        josa = "과"
    stem = stem.format(A=A, B=B, josa=josa)
    answer = answer.format(divs3=divs3, maxnum=maxnum)
    comment = comment.format(A=A, B=B, divs1=divs1, divs2=divs2, divs3=divs3, maxnum=maxnum, josa=josa)

    return stem, answer, comment















# 5-1-2-39
def denandmul512_Stem_033():
    stem = "두 수의 최대공약수 중 더 큰 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${A}$$/수식$$, $$수식$${B}$$/수식$$     ㉡ $$수식$${C}$$/수식$$, $$수식$${D}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{K}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${A}$$/수식$$과 $$수식$${B}$$/수식$$의 최대공약수: $$수식$${maxnum1}$$/수식$$\n" \
              "㉡ $$수식$${C}$$/수식$$과 $$수식$${D}$$/수식$$의 최대공약수: $$수식$${maxnum2}$$/수식$$\n" \
              "$$수식$${maxnum1} {op} {maxnum2}$$/수식$$이므로 두 수의 최대공약수 중 더 큰 것은 {K}입니다.\n\n"


    while True:
        A, B, C, D = random.sample(list(range(31, 80)), 4)

        divisor1 = getdivisor(A)
        divisor2 = getdivisor(B)
        divisor3 = getdivisor(C)
        divisor4 = getdivisor(D)
        inter1 = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        inter1.sort()
        inter2 = list(set(divisor3) & set(divisor4))
        inter2.sort()
        maxnum1 = inter1[len(inter1) - 1]
        maxnum2 = inter2[len(inter2) - 1]
        if len(inter1) >= 3 and len(inter2) >= 3 and maxnum1 != maxnum2:
            break

    if maxnum1 > maxnum2:
        K = '㉠'
        op = '&gt;'
    else:
        K = '㉡'
        op = '&lt;'

    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(K=K)
    comment = comment.format(A=A, B=B, C=C, D=D, maxnum1=maxnum1, maxnum2=maxnum2, K=K, op=op)

    return stem, answer, comment















# 5-1-2-40
def denandmul512_Stem_034():
    stem = "잘못된 설명을 찾아 기호를 써 보세요.\n$$표$$㉠ {p1}\n㉡ {p2}$$/표$$\n"
    answer = "(정답)\n{K}\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 약수: {divs1}\n" \
              "$$수식$${B}$$/수식$$의 약수: {divs2}\n" \
              "따라서 $$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수는 {divs3}이고, " \
              "이 중에서 가장 큰 수는 $$수식$${maxnum}$$/수식$$입니다.\n\n"


    A, B = [[4, 12], [4, 16], [6, 12], [6, 18], [8, 16], [9, 18]][np.random.randint(0, 6)]

    divisor1 = getdivisor(A)
    divisor2 = getdivisor(B)
    divisor3 = list(set(divisor1) & set(divisor2))  # 교집합 구하기
    divisor3.sort()

    maxnum = divisor3[len(divisor3) - 1]

    while True:
        C = random.sample(divisor3, 1)[0]
        if C != maxnum:
            break

    divs1 = ''

    for i in range(0, len(divisor1)):
        divs1 = divs1 + "$$수식$${an}$$/수식$$".format(an=divisor1[i])
        if i != len(divisor1) - 1:
            divs1 = divs1 + ', '

    divs2 = ''

    for i in range(0, len(divisor2)):
        divs2 = divs2 + "$$수식$${an}$$/수식$$".format(an=divisor2[i])
        if i != len(divisor2) - 1:
            divs2 = divs2 + ', '

    divs3 = ''

    for i in range(0, len(divisor3)):
        divs3 = divs3 + "$$수식$${an}$$/수식$$".format(an=divisor3[i])
        if i != len(divisor3) - 1:
            divs3 = divs3 + ', '

    j1 = proc_jo(A, 2)

    P = [['$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수는 두 수를 모두 나누어떨어지게 할 수 있습니다.'.format(A=A, B=B, j1=j1), False],
         ['$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수 중에서 가장 큰 수는 $$수식$${C}$$/수식$$입니다.'.format(A=A, B=B, C=C, j1=j1), True]]

    np.random.shuffle(P)

    [[p1, k1], [p2, k2]] = P

    if k1:
        K = '㉠'
    else:
        K = '㉡'

    stem = stem.format(p1=p1, p2=p2)
    answer = answer.format(K=K)
    comment = comment.format(A=A, B=B, divs1=divs1, divs2=divs2, divs3=divs3, maxnum=maxnum, j1=j1)

    return stem, answer, comment














# 5-1-2-41
def denandmul512_Stem_035():
    stem = "어떤 두 수의 최대공약수가 $$수식$${A}$$/수식$$일 때, 두 수의 공약수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$개\n"
    comment = "(해설)\n" \
              "어떤 두 수의 공약수는 최대공약수의 약수와 같습니다.\n" \
              "$$수식$${A}$$/수식$$의 약수는 {divs1}이므로 모두 $$수식$${S}$$/수식$$개입니다.\n\n"


    while True:
        A = np.random.randint(16, 40)
        divisor = getdivisor(A)
        S = len(divisor)
        if S > 3:
            break

    divs1 = ''

    for i in range(0, len(divisor)):
        divs1 = divs1 + "$$수식$${an}$$/수식$$".format(an=divisor[i])
        if i != len(divisor) - 1:
            divs1 = divs1 + ', '

    stem = stem.format(A=A)
    answer = answer.format(S=S)
    comment = comment.format(A=A, S=S, divs1=divs1)

    return stem, answer, comment

















# 5-1-2-42
def denandmul512_Stem_036():
    stem = "{P1} $$수식$${A}$$/수식$$ {T1}{wa} {P2} $$수식$${B}$$/수식$$ {T2}{eul} 최대한 많은 친구에게 남김없이 똑같이 나누어 주려고 합니다. 최대 몇 명의 친구에게 나누어 줄 수 있나요?\n"
    answer = "(정답)\n$$수식$${maxnum}$$/수식$$명\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 약수: {divs1}\n" \
              "$$수식$${B}$$/수식$$의 약수: {divs2}\n" \
              "$$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 최대공약수: $$수식$${maxnum}$$/수식$$\n" \
              "따라서 최대 $$수식$${maxnum}$$/수식$$명의 친구에게 나누어 줄 수 있다.\n\n"


    [[P1, T1], [P2, T2]] = random.sample([['연필', '자루'], ['지우개', '개'], ['샤프', '개'], ['공책', '권']], 2)

    wa = proc_jo(T1, 2)
    eul = proc_jo(T2, 1)

    while True:
        A = np.random.randint(11, 20)
        B = np.random.randint(21, 30)
        divisor1 = getdivisor(A)
        divisor2 = getdivisor(B)
        divisor3 = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        if len(divisor1) > 3 and len(divisor2) > 3 and len(divisor3) > 1:
            break

    divisor3.sort()

    maxnum = divisor3[len(divisor3) - 1]

    divs1 = ''

    for i in range(0, len(divisor1)):
        divs1 = divs1 + "$$수식$${an}$$/수식$$".format(an=divisor1[i])
        if i != len(divisor1) - 1:
            divs1 = divs1 + ', '

    divs2 = ''

    for i in range(0, len(divisor2)):
        divs2 = divs2 + "$$수식$${an}$$/수식$$".format(an=divisor2[i])
        if i != len(divisor2) - 1:
            divs2 = divs2 + ', '

    stem = stem.format(P1=P1, P2=P2, T1=T1, T2=T2, A=A, B=B, wa=wa, eul=eul)
    answer = answer.format(maxnum=maxnum)
    comment = comment.format(A=A, B=B, divs1=divs1, divs2=divs2, maxnum=maxnum)

    return stem, answer, comment















# 5-1-2-43
def denandmul512_Stem_037():
    stem = "가로가 $$수식$${A} rm {{cm}}$$/수식$$, 세로가 $$수식$${B} rm {{cm}}$$/수식$$인 직사각형 모양의 종이를 크기가 같은 정사각형 모양으로 남는 부분 없이 자르려고 합니다. 자를 수 있는 가장 큰 정사각형의 한 변의 길이는 몇 $$수식$$rm {{cm}}$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${maxnum} rm {{cm}}$$/수식$$\n"
    comment = "(해설)\n" \
              "정사각형 모양의 종이를 크기가 같은 가장 큰 정사각형 모양으로 남는 부분 없이 자르려면 " \
              "정사각형의 한 변의 길이는 직사각형 모양의 종이의 가로와 세로의 최대공약수가 되어야 합니다.\n" \
              "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 최대공약수: $$수식$${maxnum}$$/수식$$\n" \
              "따라서 가장 큰 정사각형의 한 변의 길이는 $$수식$${maxnum} rm {{cm}}$$/수식$$입니다.\n\n"


    while True:
        A = np.random.randint(31, 40)
        B = np.random.randint(21, 30)
        divisor1 = getdivisor(A)
        divisor2 = getdivisor(B)
        divisor3 = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        if len(divisor3) >= 3:
            break

    divisor3.sort()
    maxnum = divisor3[len(divisor3) - 1]

    j1 = proc_jo(A, 2)

    stem = stem.format(A=A, B=B)
    answer = answer.format(maxnum=maxnum)
    comment = comment.format(A=A, B=B, maxnum=maxnum, j1=j1)

    return stem, answer, comment


















# 5-1-2-44
def denandmul512_Stem_038():
    stem = "$$수식$${A}$$/수식$${j1} 어떤 수의 최대공약수는 $$수식$${B}$$/수식$$입니다. $$수식$${A}$$/수식$${j1} 어떤 수의 공약수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$${j1} 어떤 수의 공약수는 $$수식$${A}$$/수식$${j1} 어떤 수의 최대공약수인 " \
              "$$수식$${B}$$/수식$$의 약수와 같습니다.\n" \
              "$$수식$${B}$$/수식$$의 약수는 {divs}이므로 모두 $$수식$${S}$$/수식$$개입니다.\n\n"


    while True:
        while True:
            A = np.random.randint(31, 70)
            divisor1 = getdivisor(A)
            if len(divisor1) >= 4:
                break
        B = divisor1[-2]
        divisor = getdivisor(B)
        S = len(divisor)
        if S > 2:
            break

    divs = ''

    for i in range(0, len(divisor)):
        divs = divs + "$$수식$${an}$$/수식$$".format(an=divisor[i])
        if i != len(divisor) - 1:
            divs = divs + ', '

    j1 = proc_jo(A, 2)

    stem = stem.format(A=A, B=B, j1=j1)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, S=S, divs=divs, j1=j1)

    return stem, answer, comment



















# 5-1-2-45
def denandmul512_Stem_039():
    stem = "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수 중에서 $$수식$${C}$$/수식$$의 배수를 모두 구해 보세요.\n"
    answer = "(정답)\n{muls}\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 약수: {divs1}\n" \
              "$$수식$${B}$$/수식$$의 약수: {divs2}\n" \
              "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수: {divs3}\n" \
              "따라서 $$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수 중에서 $$수식$${C}$$/수식$$의 배수는 {muls}입니다.\n\n"


    while True:
        while True:
            A, B = random.sample(list(range(21, 80)), 2)
            divisor1 = getdivisor(A)
            divisor2 = getdivisor(B)
            divisor3 = list(set(divisor1) & set(divisor2))  # 교집합 구하기
            if len(divisor3) > 2:
                break

        divisor3.sort()
        inter = divisor3.copy()
        inter.remove(1)
        inter.remove(divisor3[-1])
        C = random.sample(inter, 1)[0]
        mulslist = []
        for i in range(0, len(divisor3)):
            if divisor3[i] % C == 0:
                mulslist.append(divisor3[i])
        if len(mulslist) >= 2:
            break


    muls = ''

    for i in range(0, len(mulslist)):
        muls = muls + "$$수식$${an}$$/수식$$".format(an=mulslist[i])
        if i != len(mulslist) - 1:
            muls = muls + ', '

    divs1 = ''

    for i in range(0, len(divisor1)):
        divs1 = divs1 + "$$수식$${an}$$/수식$$".format(an=divisor1[i])
        if i != len(divisor1) - 1:
            divs1 = divs1 + ', '

    divs2 = ''

    for i in range(0, len(divisor2)):
        divs2 = divs2 + "$$수식$${an}$$/수식$$".format(an=divisor2[i])
        if i != len(divisor2) - 1:
            divs2 = divs2 + ', '

    divs3 = ''

    for i in range(0, len(divisor3)):
        divs3 = divs3 + "$$수식$${an}$$/수식$$".format(an=divisor3[i])
        if i != len(divisor3) - 1:
            divs3 = divs3 + ', '

    j1 = proc_jo(A, 2)

    stem = stem.format(A=A, B=B, C=C, j1=j1)
    answer = answer.format(muls=muls)
    comment = comment.format(A=A, B=B, C=C, divs1=divs1, divs2=divs2, divs3=divs3, muls=muls, j1=j1)

    return stem, answer, comment

















# 5-1-2-46
def denandmul512_Stem_040():
    stem = "접시에 {P1} $$수식$${A}$$/수식$$개와 {P2} $$수식$${B}$$/수식$$개를 남김없이 똑같이 나누어 담을 수 있는 방법은 모두 몇 가지인가요? $$수식$$LEFT ($$/수식$$단, 접시 한 개에 {P1}{wa} {P2}{jo2} 모두 담지는 않습니다.$$수식$$RIGHT )$$/수식$$\n"
    answer = "(정답)\n$$수식$${n}$$/수식$$가지\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$는 " \
              "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수 {divs3}으로 나누어떨어지므로 " \
              "{dishdivs}에 남김없이 똑같이 나누어 담을 수 있습니다.\n" \
              "{explain}따라서 접시에 {P1} $$수식$${A}$$/수식$$개와 {P2} $$수식$${B}$$/수식$$개를 " \
              "남김없이 똑같이 나누어 담을 수 있는 방법은 모두 $$수식$${n}$$/수식$$가지입니다.\n\n"


    P1, P2 = random.sample(['사과', '배', '귤', '감', '딸기', '바나나', '참외', '키위'], 2)

    wa = proc_jo(P1, 2)
    jo1 = proc_jo(P1, 1)
    jo2 = proc_jo(P2, 1)

    while True:
        A = np.random.randint(21, 40)
        B = np.random.randint(11, 20)
        divisor1 = getdivisor(A)
        divisor2 = getdivisor(B)
        divisor3 = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        if len(divisor3) >= 3:
            break

    n = len(divisor3) - 1

    divs3 = ''

    for i in range(0, len(divisor3)):
        divs3 = divs3 + "$$수식$${an}$$/수식$$".format(an=divisor3[i])
        if i != len(divisor3) - 1:
            divs3 = divs3 + ', '

    dishdivs = ''

    for i in range(1, len(divisor3)):
        dishdivs = dishdivs + "접시 $$수식$${an}$$/수식$$개".format(an=divisor3[i])
        if i != len(divisor3) - 1:
            dishdivs = dishdivs + ', '

    explain = ''

    for i in range(1, len(divisor3)):
        explain = explain + "한 접시에 {P1}{jo1} $$수식$${a}$$/수식$$개씩, " \
                            "{P2}{jo2} $$수식$${b}$$/수식$$개씩 " \
                            "접시 $$수식$${c}$$/수식$$개에 나누어 담습니다.\n".format(P1=P1, P2=P2, jo1=jo1, jo2=jo2, a=int(A/divisor3[i]), b=int(B/divisor3[i]), c=divisor3[i])

    j1 = proc_jo(A, 2)

    stem = stem.format(A=A, B=B, P1=P1, P2=P2, wa=wa, jo2=jo2)
    answer = answer.format(n=n)
    comment = comment.format(A=A, B=B, divs3=divs3, P1=P1, P2=P2, n=n, dishdivs=dishdivs, explain=explain, j1=j1)

    return stem, answer, comment



















# 5-1-2-47
def denandmul512_Stem_041():
    stem = "대화를 읽고 공약수에 대해 잘못 말한 사람을 찾아 써 보세요.\n$$표$$$$수식$$LEFT [$$/수식$${P1}$$수식$$RIGHT ]$$/수식$$ {x1}\n$$수식$$LEFT [$$/수식$${P2}$$수식$$RIGHT ]$$/수식$$ {x2}\n$$수식$$LEFT [$$/수식$${P3}$$수식$$RIGHT ]$$/수식$$ {x3}$$/표$$\n"
    answer = "(정답)\n{P}\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수는 {divs3}이고 " \
              "이 중에서 가장 큰 수는 $$수식$${maxnum}$$/수식$$입니다.\n\n"


    P1, P2, P3 = random.sample(['진우', '민수', '은지', '민희', '지효', '민서', '선미', '수지', '영호'], 3)

    while True:
        A, B = random.sample(list(range(21, 50)), 2)
        divisor1 = getdivisor(A)
        divisor2 = getdivisor(B)
        divisor3 = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        if len(divisor3) >= 4:
            break

    divisor3.sort()

    maxnum = divisor3[-1]

    # while True:
    #     num = random.sample(divisor3, 1)[0]
    #     if num != maxnum and num != 1:
    #         break

    num = divisor3[np.random.randint(2, len(divisor3)-1 )]

    divs3 = ''

    for i in range(0, len(divisor3)):
        divs3 = divs3 + "$$수식$${an}$$/수식$$".format(an=divisor3[i])
        if i != len(divisor3) - 1:
            divs3 = divs3 + ', '

    j1 = proc_jo(A, 2)

    X = [['$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수는 두 수를 모두 나누어떨어지게 할 수 있어.'.format(A=A, B=B, j1=j1), False],
         ['$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수 중에서 가장 작은 수는 $$수식$$1$$/수식$$이야.'.format(A=A, B=B, j1=j1), False],
         ['$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공약수 중에서 가장 큰 수는 $$수식$${num}$$/수식$$이야.'.format(A=A, B=B, num=num, j1=j1), True]]

    np.random.shuffle(X)

    [[x1, _], [x2, _], [x3, _]] = X
    people = [P1, P2, P3]

    for i in range(0, len(X)):
        if X[i][1]:
            P = people[i]
            break

    stem = stem.format(P1=P1, P2=P2, P3=P3, x1=x1, x2=x2, x3=x3)
    answer = answer.format(P=P)
    comment = comment.format(A=A, B=B, divs3=divs3, maxnum=maxnum, j1=j1)

    return stem, answer, comment
















# 5-1-2-48
def denandmul512_Stem_042():
    stem = "곱셈식을 보고 $$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 최대공약수를 구해 보세요.\n$$표$$$$수식$${A} = {divmul1}$$/수식$$\n$$수식$${B} = {divmul2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${maxnum}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 최대공약수는 $$수식$${divmul3}{maxnum}$$/수식$$입니다.\n\n"


    while True:
        A, B = random.sample(list(range(21, 50)), 2)
        divisor1 = getdivisor(A)
        divisor2 = getdivisor(B)
        divisor3 = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        if len(divisor3) >= 2:
            break

    divisor3.sort()
    maxnum = divisor3[-1]

    factor1 = getfactor2(A)
    factor2 = getfactor2(B)
    factor3 = getfactor2(maxnum)

    divmul1 = ''
    for i in range(0, len(factor1)):
        divmul1 = divmul1 + "{an}".format(an=factor1[i])
        if i != len(factor1) - 1:
            divmul1 = divmul1 + 'TIMES'

    divmul2 = ''
    for i in range(0, len(factor2)):
        divmul2 = divmul2 + "{an}".format(an=factor2[i])
        if i != len(factor2) - 1:
            divmul2 = divmul2 + 'TIMES'

    divmul3 = ''
    for i in range(0, len(factor3)):
        divmul3 = divmul3 + "{an}".format(an=factor3[i])
        if i != len(factor3) - 1:
            divmul3 = divmul3 + 'TIMES'
    if len(factor3) > 1:
        divmul3 = divmul3 + "="

    stem = stem.format(A=A, B=B, divmul1=divmul1, divmul2=divmul2)
    answer = answer.format(maxnum=maxnum)
    comment = comment.format(A=A, B=B, divmul3=divmul3, maxnum=maxnum)

    return stem, answer, comment
















# 5-1-2-49
def denandmul512_Stem_043():
    stem = "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$${j2} 여러 수의 곱으로 나타내어 최대공약수를 구하려고 합니다. $$수식$${box}$$/수식$$ 안에 $$수식$$1$$/수식$$이 아닌 알맞은 수를 써넣으세요.\n$$수식$${A} ` = ` $$/수식$$ $$수식$${box1}$$/수식$$ $$수식$$ ` TIMES ` $$/수식$$ $$수식$${box2}$$/수식$$ $$수식$$ ` TIMES ` $$/수식$$ $$수식$${box3}$$/수식$$\n$$수식$${B} ` = ` $$/수식$$ $$수식$${box4}$$/수식$$ $$수식$$ ` TIMES ` $$/수식$$ $$수식$${box5}$$/수식$$ $$수식$$ ` TIMES ` $$/수식$$ $$수식$${box6}$$/수식$$\n$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 최대공약수는\n$$수식$${box7}$$/수식$$ $$수식$$ ` TIMES ` $$/수식$$ $$수식$${box8}$$/수식$$ $$수식$$ ` = ` $$/수식$$ $$수식$${box9}$$/수식$$입니다.\n"
    answer = "(정답)\n{divmul11} {divmul22} {divmul33}㉨ $$수식$${maxnum}$$/수식$$\n"
    comment = "(해설)\n" \
              "여러 수의 곱으로 나타낸 곱셈식 중에서 공통으로 들어 있는 곱셈식을 찾아 최대공약수를 구합니다.\n" \
              "$$수식$${A} =$$/수식$${divmul1}\n" \
              "$$수식$${B} =$$/수식$${divmul2}\n" \
              "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 최대공약수는 {divmul3}$$수식$${maxnum}$$/수식$$입니다.\n\n"


    box = '□'

    # box1 = "$$수식$$①$$/수식$$"
    # box2 = "$$수식$$②$$/수식$$"
    # box3 = "$$수식$$③$$/수식$$"
    # box4 = "$$수식$$④$$/수식$$"
    #
    # box5 = "$$수식$$⑤$$/수식$$"
    # box6 = "$$수식$$⑥$$/수식$$"
    # box7 = "$$수식$$⑦$$/수식$$"
    #
    # box8 = "$$수식$$⑧$$/수식$$"
    # box9 = "$$수식$$⑨$$/수식$$"

    box1 = "box{%s````````````````````}"%"㉠"
    box2 = "box{%s````````````````````}"%"㉡"
    box3 = "box{%s````````````````````}"%"㉢"

    box4 = "box{%s````````````````````}"%"㉣"
    box5 = "box{%s````````````````````}"%"㉤"
    box6 = "box{%s````````````````````}"%"㉥"

    box7 = "box{%s````````````````````}"%"㉦"
    box8 = "box{%s````````````````````}"%"㉧"
    box9 = "box{%s````````````````````}"%"㉨"



    while True:
        while True:
            A, B = random.sample(list(range(21, 50)), 2)
            divisor1 = getdivisor(A)
            divisor2 = getdivisor(B)
            divisor3 = list(set(divisor1) & set(divisor2))  # 교집합 구하기
            if len(divisor3) >= 2:
                break
        divisor3.sort()
        maxnum = divisor3[-1]

        factor1 = getfactor2(A)
        factor2 = getfactor2(B)
        factor3 = getfactor2(maxnum)
        if len(factor1) == 3 and len(factor2) == 3 and len(factor3) == 2:
            break
    
    divmul1 = ''

    for i in range(0, len(factor1)):
        divmul1 = divmul1 + "$$수식$${an}$$/수식$$".format(an=factor1[i])
        if i != len(factor1) - 1:
            divmul1 = divmul1 + '$$수식$$TIMES$$/수식$$'

    divmul11 = '$$수식$$LEFT ($$/수식$$'

    for i in range(0, len(factor1)):
        divmul11 = divmul11 + "$$수식$${an}$$/수식$$".format(an=factor1[i])
        if i != len(factor1) - 1:
            divmul11 = divmul11 + '$$수식$$TIMES$$/수식$$'

    divmul11 = divmul11 + "$$수식$$RIGHT )$$/수식$$"

    divmul2 = ''

    for i in range(0, len(factor2)):
        divmul2 = divmul2 + "$$수식$${an}$$/수식$$".format(an=factor2[i])
        if i != len(factor2) - 1:
            divmul2 = divmul2 + '$$수식$$TIMES$$/수식$$'

    divmul22 = '$$수식$$LEFT ($$/수식$$'

    for i in range(0, len(factor2)):
        divmul22 = divmul22 + "$$수식$${an}$$/수식$$".format(an=factor2[i])
        if i != len(factor2) - 1:
            divmul22 = divmul22 + '$$수식$$TIMES$$/수식$$'

    divmul22 = divmul22 + "$$수식$$RIGHT )$$/수식$$"

    divmul3 = ''

    for i in range(0, len(factor3)):
        divmul3 = divmul3 + "$$수식$${an}$$/수식$$".format(an=factor3[i])
        if i != len(factor3) - 1:
            divmul3 = divmul3 + '$$수식$$TIMES$$/수식$$'

    if len(factor3) > 1:
        divmul3 = divmul3 + "$$수식$$=$$/수식$$"

    divmul33 = '$$수식$$LEFT ($$/수식$$'

    for i in range(0, len(factor3)):
        divmul33 = divmul33 + "$$수식$${an}$$/수식$$".format(an=factor3[i])
        if i != len(factor3) - 1:
            divmul33 = divmul33 + '$$수식$$TIMES$$/수식$$'

    divmul33 = divmul33 + "$$수식$$RIGHT )$$/수식$$"
    
    divmul11 = "㉠ $$수식$${a}$$/수식$$, ㉡ $$수식$${b}$$/수식$$, ㉢ $$수식$${c}$$/수식$$,".format(a=factor1[0], b=factor1[1], c=factor1[2])
    divmul22 = "㉣ $$수식$${d}$$/수식$$, ㉤ $$수식$${e}$$/수식$$, ㉥ $$수식$${f}$$/수식$$,".format(d=factor2[0], e=factor2[1], f=factor2[2])
    divmul33 = "㉦ $$수식$${g}$$/수식$$, ㉧ $$수식$${h}$$/수식$$\n".format(g=factor3[0], h=factor3[1])

    j1 = proc_jo(A, 2)

    j2 = proc_jo(B, 1)

    stem = stem.format(A=A, B=B, box=box, box1=box1, box2=box2, box3=box3, box4=box4, box5=box5,
                       box6=box6, box7=box7, box8=box8, box9=box9, j1=j1, j2=j2)
    answer = answer.format(divmul11=divmul11, divmul22=divmul22, divmul33=divmul33, maxnum=maxnum)
    comment = comment.format(A=A, B=B, divmul1=divmul1, divmul2=divmul2, divmul3=divmul3, maxnum=maxnum, j1=j1)

    return stem, answer, comment















# 5-1-2-54
def denandmul512_Stem_044():
    stem = "최대공약수가 $$수식$${S}$$/수식$$인 두 수를 여러 수의 곱으로 나타낸 것입니다. $$수식$${box}$$/수식$$ 안에 $$수식$$1$$/수식$$이 아닌 알맞은 수를 써넣으세요.\n$$수식$${box1}$$/수식$$ $$수식$$ = {a1} TIMES {a2} TIMES$$/수식$$ $$수식$${box2}$$/수식$$\n$$수식$${box3}$$/수식$$ $$수식$$  = {b1} TIMES $$/수식$$ $$수식$${box4}$$/수식$$ $$수식$$ TIMES $$/수식$$ $$수식$${box5}$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${A}$$/수식$$, $$수식$${ak}$$/수식$$, ㉢ $$수식$${B}$$/수식$$, ㉣ $$수식$${bk}$$/수식$$, ㉤ $$수식$${bl}$$/수식$$\n"
    comment = "(해설)\n" \
              "최대공약수가 $$수식$${S}$$/수식$$이므로 $$수식$$1$$/수식$$이 아닌 수들의 곱셈식으로 나타내었을 때 " \
              "공통으로 $$수식$${s1} TIMES {s2}$$/수식$${j1} 들어가야 합니다.\n" \
              "$$수식$${A} = {a1} TIMES {a2} TIMES {a3}$$/수식$$, $$수식$${B} = {b1} TIMES {b2} TIMES {b3}$$/수식$$\n\n"

    box = '□'

    box1 = "box{%s````````````````````}"%"㉠"
    box2 = "box{%s````````````````````}"%"㉡"
    box3 = "box{%s````````````````````}"%"㉢"

    box4 = "box{%s````````````````````}"%"㉣"
    box5 = "box{%s````````````````````}"%"㉤"



    while True:
        while True:
            while True:
                # A, B = random.sample(list(range(21, 50)), 2)
                while True:
                    A = np.random.randint(21, 150)
                    B = np.random.randint(21, 80)
                    if A != B:
                        break
                divisor1 = getdivisor(A)
                divisor2 = getdivisor(B)
                divisor3 = list(set(divisor1) & set(divisor2))  # 교집합 구하기
                if len(divisor3) >= 2:
                    break

            divisor3.sort()
            maxnum = divisor3[-1]

            factor1 = getfactor2(A)
            factor2 = getfactor2(B)
            factor3 = getfactor2(maxnum)
            if len(factor1) == 3 and len(factor2) == 3 and len(factor3) == 2:
                break

        a1, a2, a3 = factor1
        b1, b2, b3 = factor2
        s1, s2 = factor3
        S = maxnum

        ak = a3
        bk = b2
        bl = b3

        if maxnum % (a1 * a2) != 0 and maxnum % b1 != 0:
            break
        elif maxnum % a1 == 0 and maxnum % a2 != 0 and maxnum % b1 != 0:
            break



    j1 = proc_jo(s2, 0)

    stem = stem.format(S=S, box=box, box1=box1, box2=box2, box3=box3, box4=box4, box5=box5,
                       a1=a1, a2=a2, b1=b1)
    answer = answer.format(A=A, B=B, ak=ak, bk=bk, bl=bl)
    comment = comment.format(A=A, B=B, a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, S=S, s1=s1, s2=s2, j1=j1)

    return stem, answer, comment


















# 5-1-2-58
def denandmul512_Stem_045():
    stem = "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 최소공배수를 구해 보세요."
    answer = "(정답)\n$$수식$${s1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 배수: {muls1}, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "$$수식$${B}$$/수식$$의 배수: {muls2}, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 최소공배수: $$수식$${s1}$$/수식$$\n\n"


    while True:
        while True:
            while True:
                A = np.random.randint(21, 30)
                B = np.random.randint(11, 20)
                if A != B * 2:
                    break
            divisor1 = getdivisor(A)
            divisor2 = getdivisor(B)
            divisor3 = list(set(divisor1) & set(divisor2))  # 교집합 구하기
            if len(divisor3) >= 2:
                break
        divisor3.sort()
        maxnum = divisor3[-1]

        s1 = int(A * B / maxnum)
        s2 = s1 * 2
        s3 = s1 * 3
        if s1 < 100:
            break

    muls1 = ''

    for i in range(1, 6):
        muls1 = muls1 + "$$수식$${an}$$/수식$$".format(an=A*i)
        if i != 5:
            muls1 = muls1 + ', '

    muls2 = ''

    for i in range(1, 6):
        muls2 = muls2 + "$$수식$${an}$$/수식$$".format(an=B * i)
        if i != 5:
            muls2 = muls2 + ', '

    j1 = proc_jo(A, 2)

    stem = stem.format(A=A, B=B, j1=j1)
    answer = answer.format(s1=s1, s2=s2, s3=s3)
    comment = comment.format(A=A, B=B, s1=s1, s2=s2, s3=s3, muls1=muls1, muls2=muls2, j1=j1)

    return stem, answer, comment



















# 5-1-2-59
def denandmul512_Stem_046():
    stem = "$$수식$$10$$/수식$$부터 $$수식$$50$$/수식$$까지의 수 중에서 $$수식$${A}$$/수식$$의 배수이면서 $$수식$${B}$$/수식$$의 배수인 수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 배수: {muls1}, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "$$수식$${B}$$/수식$$의 배수: {muls2}, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "$$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 공배수: $$수식$${c1}$$/수식$$, $$수식$${c2}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "따라서 $$수식$$10$$/수식$$부터 $$수식$$50$$/수식$$까지의 수 중에서 " \
              "$$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 공배수는 {muls3}로 모두 $$수식$${S}$$/수식$$개입니다.\n\n"


    A, B = [[2, 5], [2, 7], [3, 4], [3, 5]][np.random.randint(0, 4)]

    divisor1 = getdivisor(A)
    divisor2 = getdivisor(B)

    divisor3 = list(set(divisor1) & set(divisor2))  # 교집합 구하기
    divisor3.sort()
    maxnum = divisor3[-1]

    c1 = int(A*B/maxnum)
    c2 = c1 * 2

    muls1 = ''

    for i in range(1, 6):
        muls1 = muls1 + "$$수식$${an}$$/수식$$".format(an=A*i)
        if i != 5:
            muls1 = muls1 + ', '

    muls2 = ''

    for i in range(1, 6):
        muls2 = muls2 + "$$수식$${an}$$/수식$$".format(an=B * i)
        if i != 5:
            muls2 = muls2 + ', '

    S = int(50/c1)

    muls3 = ''

    for i in range(1, S + 1):
        muls3 = muls3 + "$$수식$${an}$$/수식$$".format(an=c1 * i)
        if i != S:
            muls3 = muls3 + ', '

    stem = stem.format(A=A, B=B)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, c1=c1, c2=c2, muls1=muls1, muls2=muls2, muls3=muls3, S=S)

    return stem, answer, comment

















# 5-1-2-60
def denandmul512_Stem_047():
    stem = "어떤 두 수의 최소공배수가 $$수식$${A}$$/수식$$일 때, 두 수의 공배수를 작은 수부터 $$수식$$3$$/수식$$개 써 보세요.\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 두 수의 공배수는 최소공배수의 배수와 같습니다.\n" \
              "$$수식$${A}$$/수식$$의 배수: $$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n\n"


    A = np.random.randint(11, 20)
    a1 = A
    a2 = A * 2
    a3 = A * 3

    stem = stem.format(A=A)
    answer = answer.format(a1=a1, a2=a2, a3=a3)
    comment = comment.format(A=A, a1=a1, a2=a2, a3=a3)

    return stem, answer, comment
















# 5-1-2-61
def denandmul512_Stem_048():
    stem = "$$수식$${A}$$/수식$$부터 $$수식$${B}$$/수식$$까지의 수 중에서 $$수식$${C}$$/수식$$의 배수이면서 $$수식$${D}$$/수식$$의 배수인 수를 모두 써 보세요.\n"
    answer = "(정답)\n{muls}\n"
    comment = "(해설)\n" \
              "$$수식$${C}$$/수식$$와 $$수식$${D}$$/수식$$의 공배수: " \
              "$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$, $$수식$${a4}$$/수식$$, $$수식$${a5}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "따라서 $$수식$${A}$$/수식$$부터 $$수식$${B}$$/수식$$까지의 수 중에서 " \
              "$$수식$${C}$$/수식$$와 $$수식$${D}$$/수식$$의 공배수는 {muls}입니다.\n\n"


    while True:
        A = np.random.randint(10, 21)
        B = np.random.randint(21, 70)
        C, D = [[2, 3], [2, 7], [3, 4], [3, 5], [3, 7]][np.random.randint(0, 5)]
        a1 = C * D
        if A <= a1:
            break

    a2 = a1 * 2
    a3 = a1 * 3
    a4 = a1 * 4
    a5 = a1 * 5

    end = int(B/a1)

    muls = ''

    for i in range(1, end + 1):
        muls = muls + "$$수식$${an}$$/수식$$".format(an=a1 * i)
        if i != end:
            muls = muls + ', '

    stem = stem.format(A=A, B=B, C=C, D=D)
    answer = answer.format(muls=muls)
    comment = comment.format(A=A, B=B, C=C, D=D, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, muls=muls)

    return stem, answer, comment




















# 5-1-2-62
def denandmul512_Stem_049():
    stem = "{P1}가 설명하는 수를 구해 보세요.\n$$표$$$$수식$$LEFT [$$/수식$${P1}$$수식$$RIGHT ]$$/수식$$ 이 수는 $$수식$${A}$$/수식$${josa} $$수식$${B}$$/수식$$의 공배수야.\n$$수식$$LEFT [$$/수식$${P2}$$수식$$RIGHT ]$$/수식$$ 공배수는 많이 있는데 $$수식$$CDOTS CDOTS$$/수식$$.\n$$수식$$LEFT [$$/수식$${P1}$$수식$$RIGHT ]$$/수식$$ $$수식$${C}$$/수식$$보다 크고 $$수식$${D}$$/수식$$보다 작아.\n$$수식$$LEFT [$$/수식$${P2}$$수식$$RIGHT ]$$/수식$$ 음. $$수식$$CDOTS CDOTS$$/수식$$, 어떤 수일까?$$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 배수: $$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$, " \
              "$$수식$${a4}$$/수식$$, $$수식$${a5}$$/수식$$, $$수식$${a6}$$/수식$$, $$수식$${a7}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "$$수식$${B}$$/수식$$의 배수: $$수식$${b1}$$/수식$$, $$수식$${b2}$$/수식$$, $$수식$${b3}$$/수식$$, " \
              "$$수식$${b4}$$/수식$$, $$수식$${b5}$$/수식$$, $$수식$${b6}$$/수식$$, $$수식$${b7}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "$$수식$${A}$$/수식$${josa} $$수식$${B}$$/수식$$의 공배수: $$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "따라서 $$수식$${C}$$/수식$$보다 크고 $$수식$${D}$$/수식$$보다 작은 " \
              "$$수식$${A}$$/수식$${josa} $$수식$${B}$$/수식$$의 공배수는 $$수식$${S}$$/수식$$입니다.\n\n"


    P1, P2 = random.sample(['진우', '민수', '은지', '민희', '지효', '민서', '선미', '수지', '영호', '은서', '선주'], 2)


    while True:
        A, B = [[3, 4], [3, 5], [3, 7], [4, 5], [4, 7], [5, 6]][np.random.randint(0, 6)]

        a = []
        b = []

        for i in range(1, 8):
            a.append(A*i)
            b.append(B*i)

        a1, a2, a3, a4, a5, a6, a7 = a
        b1, b2, b3, b4, b5, b6, b7 = b

        s1 = A*B
        s2 = s1 * 2
        s3 = s1 * 3

        S = s1 * np.random.randint(2, 8)
        C = int(S / 10) * 10
        D = C + 10
        if S < 90 and S != C:
            break

    if A in [2,4,5,9]:
        josa = "와"
    else:
        josa = "과"

    stem = stem.format(P1=P1, P2=P2, A=A, B=B, C=C, D=D, josa=josa)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, S=S, C=C, D=D, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7,
                             b1=b1, b2=b2, b3=b3, b4=b4, b5=b5, b6=b6, b7=b7, s1=s1, s2=s2, s3=s3, josa=josa)

    return stem, answer, comment



















# 5-1-2-63
def denandmul512_Stem_050():
    stem = "두 수의 최소공배수 중 가장 큰 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$$LEFT ( {a1}$$/수식$$, $$수식$${a2} RIGHT )$$/수식$$     ㉡ $$수식$$LEFT ( {b1}$$/수식$$, $$수식$${b2} RIGHT )$$/수식$$     ㉢ $$수식$$LEFT ( {c1}$$/수식$$, $$수식$${c2} RIGHT )$$/수식$$$$/표$$\n"
    answer = "(정답)\n{K}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${a1}$$/수식$$와 $$수식$${a2}$$/수식$$의 최소공배수: $$수식$${A}$$/수식$$\n" \
              "㉡ $$수식$${b1}$$/수식$$와 $$수식$${b2}$$/수식$$의 최소공배수: $$수식$${B}$$/수식$$\n" \
              "㉢ $$수식$${c1}$$/수식$$와 $$수식$${c2}$$/수식$$의 최소공배수: $$수식$${C}$$/수식$$\n" \
              "따라서 두 수의 최소공배수 중 가장 큰 것은 {K}입니다.\n\n"


    while True:
        a1, a2, b1, b2, c1, c2 = random.sample(list(range(2, 19)), 6)

        divisor1 = getdivisor(a1)
        divisor2 = getdivisor(a2)
        inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        inter.sort()
        maxnum = inter[-1]
        A = int(a1*a2/maxnum)

        divisor1 = getdivisor(b1)
        divisor2 = getdivisor(b2)
        inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        inter.sort()
        maxnum = inter[-1]
        B = int(b1 * b2 / maxnum)

        divisor1 = getdivisor(c1)
        divisor2 = getdivisor(c2)
        inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        inter.sort()
        maxnum = inter[-1]
        C = int(c1 * c2 / maxnum)

        if A != B and B != C and A != C:
            break

    if A > B and A > C:
        K = answer_kodict[0]
    elif B > A and B > C:
        K = answer_kodict[1]
    else:
        K = answer_kodict[2]

    stem = stem.format(a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2)
    answer = answer.format(K=K)
    comment = comment.format(A=A, B=B, C=C, a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, K=K)

    return stem, answer, comment
















# 5-1-2-64
def denandmul512_Stem_051():
    stem = "$$수식$${A}$$/수식$${josa} $$수식$${B}$$/수식$$의 공배수 중에서 가장 작은 수를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${s1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 배수: $$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$, " \
              "$$수식$${a4}$$/수식$$, $$수식$${a5}$$/수식$$, $$수식$${a6}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "$$수식$${B}$$/수식$$의 배수: $$수식$${b1}$$/수식$$, $$수식$${b2}$$/수식$$, $$수식$${b3}$$/수식$$, " \
              "$$수식$${b4}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "$$수식$${A}$$/수식$${josa} $$수식$${B}$$/수식$$의 공배수: $$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "따라서 $$수식$${A}$$/수식$${josa} $$수식$${B}$$/수식$$의 공배수 중에서 가장 작은 수는 $$수식$${s1}$$/수식$$입니다.\n\n"


    A = [6, 8][np.random.randint(0, 2)]
    B = [12, 14, 16, 18][np.random.randint(0, 4)]

    if A in [2,4,5,9]:
        josa = "와"
    else:
        josa = "과"

    a = []
    b = []

    for i in range(1, 7):
        a.append(A*i)
        b.append(B*i)

    a1, a2, a3, a4, a5, a6 = a
    b1, b2, b3, b4 = b[:4]

    divisor1 = getdivisor(A)
    divisor2 = getdivisor(B)

    inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
    inter.sort()
    maxnum = inter[-1]

    s1 = int(A*B / maxnum)
    s2 = s1 * 2

    stem = stem.format(A=A, B=B, josa=josa)
    answer = answer.format(s1=s1)
    comment = comment.format(A=A, B=B, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6,
                             b1=b1, b2=b2, b3=b3, b4=b4, s1=s1, s2=s2, josa=josa)

    return stem, answer, comment


















# 5-1-2-65
def denandmul512_Stem_052():
    stem = "어떤 두 수의 공배수를 가장 작은 수부터 쓴 것입니다. 두 수의 최소공배수를 구해 보세요.\n$$표$$$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$, $$수식$${a4}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "두 수의 공배수 중 가장 작은 수가 최소공배수입니다.\n" \
              "따라서 두 수의 최소공배수는 $$수식$${a1}$$/수식$$입니다.\n\n"


    a1 = np.random.randint(11, 20)

    a2 = a1 * 2
    a3 = a1 * 3
    a4 = a1 * 4

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4)
    answer = answer.format(a1=a1)
    comment = comment.format(a1=a1)

    return stem, answer, comment



















# 5-1-2-66
def denandmul512_Stem_053():
    stem = "두 수의 최소공배수의 배수를 가장 작은 수부터 차례대로 구해 보세요.\n$$표$$$$수식$${A}$$/수식$$     $$수식$${B}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 배수: $$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$, " \
              "$$수식$${a4}$$/수식$$, $$수식$${a5}$$/수식$$, $$수식$${a6}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "$$수식$${B}$$/수식$$의 배수: $$수식$${b1}$$/수식$$, $$수식$${b2}$$/수식$$, $$수식$${b3}$$/수식$$, " \
              "$$수식$${b4}$$/수식$$, $$수식$${b5}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "$$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 최소공배수: $$수식$${s1}$$/수식$$\n" \
              "$$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 최소공배수의 배수: $$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n\n"


    while True:
        A = np.random.randint(3, 6) * 5
        B = np.random.randint(6, 9) * 5
        if B != 2 * A:
            break

    a = []
    b = []

    for i in range(1, 7):
        a.append(A*i)
        b.append(B*i)

    a1, a2, a3, a4, a5, a6 = a
    b1, b2, b3, b4, b5 = b[:5]

    divisor1 = getdivisor(A)
    divisor2 = getdivisor(B)

    inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
    inter.sort()
    maxnum = inter[-1]

    s1 = int(A * B / maxnum)
    s2 = s1 * 2

    stem = stem.format(A=A, B=B)
    answer = answer.format(s1=s1, s2=s2)
    comment = comment.format(A=A, B=B, s1=s1, s2=s2, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6,
                             b1=b1, b2=b2, b3=b3, b4=b4, b5=b5)

    return stem, answer, comment
















# 5-1-2-67
def denandmul512_Stem_054():
    stem = "$$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 최소공배수는 $$수식$${s1}$$/수식$$입니다. 다음 중에서 $$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공배수가 아닌 것은 어느 것인가요?\n① $$수식$${a1}$$/수식$$     ② $$수식$${a2}$$/수식$$     ③ $$수식$${a3}$$/수식$$\n④ $$수식$${a4}$$/수식$$     ⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(정답)\n{K}\n"
    comment = "(해설)\n" \
              "두 수의 공배수는 두 수의 최소공배수의 배수이므로 $$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 " \
              "공배수는 $$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$$, " \
              "$$수식$${s4}$$/수식$$, $$수식$${s5}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$입니다.\n" \
              "따라서 $$수식$${A}$$/수식$${j1} $$수식$${B}$$/수식$$의 공배수가 아닌 것은 {K} $$수식$${ak}$$/수식$$입니다.\n\n"


    while True:
        while True:
            A = np.random.randint(11, 20)
            B = np.random.randint(3, 10)
            if A % B != 0:
                break

        divisor1 = getdivisor(A)
        divisor2 = getdivisor(B)

        inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        inter.sort()
        maxnum = inter[-1]

        s1 = int(A * B / maxnum)

        if s1 % 5 != 0 and s1 < 50:
            break

    s2 = s1 * 2
    s3 = s1 * 3
    s4 = s1 * 4
    s5 = s1 * 5

    S = [s1, s2, s3, s4, s5]

    pick = np.random.randint(0, 5)

    S[pick] = S[pick] - 2

    ak = S[pick]
    S.sort()
    a1, a2, a3, a4, a5 = S

    for i in range(0, len(S)):
        if S[i] == ak:
            K = answer_dict[i]

    j1 = proc_jo(A, 2)

    stem = stem.format(A=A, B=B, s1=s1, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, j1=j1)
    answer = answer.format(K=K)
    comment = comment.format(A=A, B=B, K=K, ak=ak, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, j1=j1)

    return stem, answer, comment



















# 5-1-2-68
def denandmul512_Stem_055():
    stem = "$$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 공배수 중에서 $$수식$$100$$/수식$$보다 작은 수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 배수: $$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$, " \
              "$$수식$${a4}$$/수식$$, $$수식$${a5}$$/수식$$, $$수식$${a6}$$/수식$$, $$수식$${a7}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "$$수식$${B}$$/수식$$의 배수: $$수식$${b1}$$/수식$$, $$수식$${b2}$$/수식$$, $$수식$${b3}$$/수식$$, " \
              "$$수식$${b4}$$/수식$$, $$수식$${b5}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "$$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 공배수: $$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "따라서 $$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 공배수 중에서 $$수식$$100$$/수식$$보다 작은 수는 " \
              "{muls}으로 모두 $$수식$${S}$$/수식$$개입니다.\n\n"


    while True:
        while True:
            A = np.random.randint(2, 20)
            B = np.random.randint(11, 20)
            if A != B:
                break

        a = []
        b = []

        for i in range(1, 8):
            a.append(A * i)
            b.append(B * i)

        a1, a2, a3, a4, a5, a6, a7 = a
        b1, b2, b3, b4, b5 = b[:5]

        divisor1 = getdivisor(A)
        divisor2 = getdivisor(B)

        inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        inter.sort()
        maxnum = inter[-1]

        s1 = int(A * B / maxnum)
        s2 = s1 * 2
        S = int(100/s1)

        if S > 1:
            break


    muls = ''

    for i in range(1, S + 1):
        muls = muls + "$$수식$${an}$$/수식$$".format(an=s1 * i)
        if i != S:
            muls = muls + ', '

    stem = stem.format(A=A, B=B)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, s1=s1, s2=s2, muls=muls, S=S,
                             a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7, b1=b1, b2=b2, b3=b3, b4=b4, b5=b5)

    return stem, answer, comment




















# 5-1-2-70
def denandmul512_Stem_056():
    stem = "{P1}는 $$수식$$1$$/수식$$부터 $$수식$${end}$$/수식$$까지의 수를 차례대로 말하면서 다음 $$수식$$&lt;$$/수식$$규칙$$수식$$&gt;$$/수식$$으로 놀이를 했습니다. {P1}가 말하는 대신 손뼉을 치면서 동시에 제자리 뛰기를 해야 하는 수는 모두 몇 개인가요?\n$$표$$$$수식$$&lt;$$/수식$$규칙$$수식$$&gt;$$/수식$$\n∙ $$수식$${A}$$/수식$$의 배수에서는 말하는 대신 손뼉을 칩니다.\n∙ $$수식$${B}$$/수식$$의 배수에서는 말하는 대신 제자리 뛰기를 합니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$의 배수: $$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$, " \
              "$$수식$${a4}$$/수식$$, $$수식$${a5}$$/수식$$, $$수식$${a6}$$/수식$$, $$수식$${a7}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "$$수식$${B}$$/수식$$의 배수: $$수식$${b1}$$/수식$$, $$수식$${b2}$$/수식$$, $$수식$${b3}$$/수식$$, " \
              "$$수식$${b4}$$/수식$$, $$수식$${b5}$$/수식$$, $$수식$${b6}$$/수식$$, $$수식$${b7}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "$$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 공배수: $$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "따라서 {P1}가 말하는 대신 손뼉을 치면서 동시에 제자리 뛰기를 해야 하는 수는 " \
              "{muls}으로 모두 $$수식$${S}$$/수식$$개입니다.\n\n"


    P1 = ['창기', '진우', '민수', '은지', '민희', '지효', '민서', '선미', '수지', '영호', '은서', '선주'][np.random.randint(0, 12)]

    end = np.random.randint(4, 10) * 10

    while True:
        A, B = [[2, 3], [2, 7], [3, 4], [3, 5]][np.random.randint(0, 4)]
        a = []
        b = []
        for i in range(1, 8):
            a.append(A * i)
            b.append(B * i)
        a1, a2, a3, a4, a5, a6, a7 = a
        b1, b2, b3, b4, b5, b6, b7 = b
        divisor1 = getdivisor(A)
        divisor2 = getdivisor(B)
        inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        inter.sort()
        maxnum = inter[-1]
        s1 = int(A * B / maxnum)
        s2 = s1 * 2
        s3 = s1 * 3
        S = int(end / s1)
        if S > 1:
            break

    muls = ''

    for i in range(1, S + 1):
        muls = muls + "$$수식$${an}$$/수식$$".format(an=s1 * i)
        if i != S:
            muls = muls + ', '

    stem = stem.format(P1=P1, A=A, B=B, end=end)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, s1=s1, s2=s2, s3=s3, muls=muls, S=S, P1=P1,
                             a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7, b1=b1, b2=b2, b3=b3, b4=b4, b5=b5, b6=b6, b7=b7)

    return stem, answer, comment

















# 5-1-2-71
def denandmul512_Stem_057():
    stem = "어떤 두 수의 최소공배수가 $$수식$${A}$$/수식$$일 때 두 수의 공배수 중에서 {P} 번째로 작은 수를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "두 수의 공배수는 두 수의 최소공배수 $$수식$${A}$$/수식$$의 배수와 같습니다.\n" \
              "$$수식$$LEFT ($$/수식$$공배수 중에서 {P} 번째로 작은 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {A} TIMES {B} = {S}$$/수식$$\n\n"


    A = np.random.randint(16, 30)
    pick = np.random.randint(0, 3)

    P = ['두', '세', '네'][pick]
    B = pick + 2
    S = A*B

    stem = stem.format(A=A, P=P)
    answer = answer.format(S=S)
    comment = comment.format(A=A, P=P, B=B, S=S)

    return stem, answer, comment























# 5-1-2-72
def denandmul512_Stem_058():
    stem = "식을 완성한 뒤 $$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 최소공배수를 구해 보세요.\n$$수식$${A} ` = ` {a1} ` TIMES ` {a2} ` TIMES ` $$/수식$$ $$수식$${box1}$$/수식$$\n$$수식$${B} ` = ` {b1} ` TIMES ` $$/수식$$ $$수식$${box2}$$/수식$$ $$수식$$ ` TIMES ` $$/수식$$ $$수식$${box3}$$/수식$$\n최소공배수: $$수식$${box4}$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${s1}$$/수식$$, ㉡ $$수식$${s2}$$/수식$$, ㉢ $$수식$${s3}$$/수식$$, ㉣ $$수식$${C}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A} = {a1} TIMES {a2} TIMES {a3}$$/수식$$\n" \
              "$$수식$${B} = {b1} TIMES {b2} TIMES {b3}$$/수식$$\n" \
              "최소공배수: {muls}$$수식$$= {C}$$/수식$$\n\n"


    box1 = "box{%s````````````````````}"%"㉠"
    box2 = "box{%s````````````````````}"%"㉡"
    box3 = "box{%s````````````````````}"%"㉢"
    box4 = "box{%s````````````````````}"%"㉣"

    while True:
        prime = [2, 3, 5, 7]
        a = []
        a.append(random.sample(prime, 1)[0])
        a.append(random.sample(prime, 1)[0])
        a.append(random.sample(prime, 1)[0])
        a.sort()
        a1, a2, a3 = a
        A = a1 * a2 * a3
        b = []
        b.append(random.sample(prime, 1)[0])
        b.append(random.sample(prime, 1)[0])
        b.append(random.sample(prime, 1)[0])
        b.sort()
        b1, b2, b3 = b
        B = b1 * b2 * b3

        divisor1 = getdivisor(A)
        divisor2 = getdivisor(B)
        inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        inter.sort()
        maxnum = inter[-1]
        C = int(A * B / maxnum)
        s1 = a3
        s2 = b2
        s3 = b3

        factor = getfactor2(C)
        if len(factor) > 1 and A != B:
            break

    muls = ''

    for i in range(0, len(factor)):
        muls = muls + "$$수식$${an}$$/수식$$".format(an=factor[i])
        if i != len(factor) - 1:
            muls = muls + '$$수식$$TIMES$$/수식$$'

    stem = stem.format(A=A, B=B, a1=a1, a2=a2, b1=b1, box1=box1, box2=box2, box3=box3, box4=box4)
    answer = answer.format(s1=s1, s2=s2, s3=s3, C=C)
    comment = comment.format(A=A, B=B, a1=a1, a2=a2, a3=a3, b1=b1, b2=b2, b3=b3, C=C, muls=muls)

    return stem, answer, comment





















# 5-1-2-74
def denandmul512_Stem_059():
    stem = "두 수의 최소공배수 중 가장 큰 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$$LEFT ( {a1}$$/수식$$, $$수식$${a2} RIGHT )$$/수식$$     ㉡ $$수식$$LEFT ( {b1}$$/수식$$, $$수식$${b2} RIGHT )$$/수식$$\n㉢ $$수식$$LEFT ( {c1}$$/수식$$, $$수식$${c2} RIGHT )$$/수식$$     ㉣ $$수식$$LEFT ( {d1}$$/수식$$, $$수식$${d2} RIGHT )$$/수식$$$$/표$$\n"
    answer = "(정답)\n{K}\n"
    comment = "(해설)\n" \
              "두 수의 최소공배수를 각각 구해 보면\n" \
              "㉠ $$수식$${A}$$/수식$$, ㉡ $$수식$${B}$$/수식$$, ㉢ $$수식$${C}$$/수식$$, ㉣ $$수식$${D}$$/수식$$입니다. " \
              "$$수식$${H} &gt; {G} &gt; {F} &gt; {E}$$/수식$$이므로 최소공배수가 가장 큰 것은 {K}입니다.\n\n"


    while True:
        a1, a2, b1, b2, c1, c2, d1, d2 = random.sample(list(range(10, 70)), 8)

        divisor1 = getdivisor(a1)
        divisor2 = getdivisor(a2)
        inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        inter.sort()
        maxnum = inter[-1]
        A = int(a1*a2/maxnum)

        divisor1 = getdivisor(b1)
        divisor2 = getdivisor(b2)
        inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        inter.sort()
        maxnum = inter[-1]
        B = int(b1 * b2 / maxnum)

        divisor1 = getdivisor(c1)
        divisor2 = getdivisor(c2)
        inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        inter.sort()
        maxnum = inter[-1]
        C = int(c1 * c2 / maxnum)

        divisor1 = getdivisor(d1)
        divisor2 = getdivisor(d2)
        inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        inter.sort()
        maxnum = inter[-1]
        D = int(d1 * d2 / maxnum)

        flag = True
        if A >= 400 or B >= 400 or C >= 400 or D >= 400:
            flag = False
        if A == B or A == C or A == D or B == C or B == D or C == D:
            flag = False
        if flag:
            break

    if A > B and A > C and A > D:
        K = answer_kodict[0]
    elif B > A and B > C and B > D:
        K = answer_kodict[1]
    elif C > A and C > B and C > D:
        K = answer_kodict[2]
    else:
        K = answer_kodict[3]

    nums = [A, B, C, D]
    nums.sort()
    E, F, G, H = nums

    stem = stem.format(a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, d1=d1, d2=d2)
    answer = answer.format(K=K)
    comment = comment.format(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H, K=K)

    return stem, answer, comment


















# 5-1-2-76
def denandmul512_Stem_060():
    stem = "다음 조건을 모두 만족하는 수를 구해 보세요.\n$$표$$∙ $$수식$$100$$/수식$$보다 크고 $$수식$${end}$$/수식$$보다 작은 수입니다.\n∙ $$수식$${A}$$/수식$$로 나누어도, $$수식$${B}$$/수식$$로 나누어도 나누어떨어집니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$로 나누어도, $$수식$${B}$$/수식$$로 나누어도 나누어떨어지므로 " \
              "$$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 공배수입니다.\n" \
              "$$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 최소공배수는 $$수식$${C}$$/수식$$이므로 " \
              "$$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 공배수는 " \
              "$$수식$${c1}$$/수식$$, $$수식$${c2}$$/수식$$, $$수식$${c3}$$/수식$$, $$수식$${c4}$$/수식$$, $$수식$${c5}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$입니다.\n" \
              "이 중에서 $$수식$$100$$/수식$$보다 크고 $$수식$${end}$$/수식$$보다 작은 수는 $$수식$${S}$$/수식$$입니다.\n\n"


    while True:
        A, B = random.sample(list(range(3, 10)), 2)
        divisor1 = getdivisor(A)
        divisor2 = getdivisor(B)
        inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
        inter.sort()
        maxnum = inter[-1]
        C = int(A*B / maxnum)
        c1 = C
        c2 = c1 * 2
        c3 = c1 * 3
        c4 = c1 * 4
        c5 = c1 * 5

        S = (int(100/C) + 1) * C
        end = 100 + (int(C/10) + 1) * 10
        if S + C >= end:
            break

    stem = stem.format(A=A, B=B, end=end)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, S=S, C=C, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, end=end)

    return stem, answer, comment




















# 5-1-2-79
def denandmul512_Stem_061():
    stem = "{P1}는 $$수식$${A}$$/수식$$일마다, {P2}는 $$수식$${B}$$/수식$$일마다 운동을 합니다. 두 사람이 $$수식$${C}$$/수식$$월 $$수식$$1$$/수식$$일에 같이 운동을 했다면 $$수식$${C}$$/수식$$월 한 달 동안 두 사람은 운동을 모두 몇 번 같이 하게 되나요?\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$번\n"
    comment = "(해설)\n" \
              "두 사람이 같이 운동하는 날은 $$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 공배수만큼 날이 지날 때마다입니다.\n" \
              "$$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 최소공배수는 $$수식$${D}$$/수식$$이므로 " \
              "$$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 공배수는 $$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$입니다.\n" \
              "$$수식$${C}$$/수식$$월은 $$수식$$31$$/수식$$일까지 있으므로 두 사람이 같이 운동하는 날은 $$수식$$1$$/수식$$일, {days}, $$수식$$CDOTS CDOTS$$/수식$$입니다.\n" \
              "따라서 $$수식$${C}$$/수식$$월 한 달 동안 두 사람은 운동을 모두 $$수식$${S}$$/수식$$번 같이 하게 됩니다.\n\n"


    P1, P2 = random.sample(['진우', '민수', '은지', '민희', '지효', '민서', '선미', '은서', '영미'], 2)

    A, B = [[2, 3], [2, 5], [2, 7], [3, 4], [3, 5]][np.random.randint(0, 5)]
    C = [1, 3, 5, 7, 8, 10, 12][np.random.randint(0, 7)]

    divisor1 = getdivisor(A)
    divisor2 = getdivisor(B)

    inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
    inter.sort()
    maxnum = inter[-1]

    a1 = int(A * B / maxnum)
    a2 = a1 * 2
    a3 = a1 * 3
    D = a1

    days = ''

    S = 1

    for i in range(1, 10):
        cur = 1 + D*i
        if cur > 31:
            break
        days = days + "$$수식$$1 + {dn} = {sn} LEFT ($$/수식$$일$$수식$$RIGHT )$$/수식$$".format(dn=D*i, sn=cur)
        S = S + 1
        if D*(i+1) + 1 <= 31:
            days = days + ", "

    stem = stem.format(P1=P1, P2=P2, A=A, B=B, C=C)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, S=S, C=C, D=D, a1=a1, a2=a2, a3=a3, days=days)

    return stem, answer, comment


















# 5-1-2-81
def denandmul512_Stem_062():
    stem = "{P1}는 $$수식$${A}$$/수식$$일마다, {P2}는 $$수식$${B}$$/수식$$일마다 도서관을 갑니다. 두 사람이 $$수식$${C}$$/수식$$월 $$수식$$1$$/수식$$일에 도서관에서 만났다면 그 다음 번 도서관에서 다시 만나는 날짜를 구하고, 그때까지 {P2}는 도서관에 몇 번 더 가야 하는지 차례대로 구해 보세요.\n"
    answer = "(정답)\n$$수식$${C}$$/수식$$월 $$수식$${S1}$$/수식$$일, $$수식$${S2}$$/수식$$번\n"
    comment = "(해설)\n" \
              "$$수식$${A}$$/수식$$와 $$수식$${B}$$/수식$$의 최소공배수는 $$수식$${D}$$/수식$$입니다.\n" \
              "{P1}와 {P2}가 다시 만나는 날은 $$수식$$1 + {D} = {S1} LEFT ($$/수식$$일$$수식$$RIGHT )$$/수식$$입니다.\n" \
              "$$수식$${D}$$/수식$$일 동안 {P2}는 $$수식$${D} DIV {B} = {S2} LEFT ($$/수식$$번$$수식$$RIGHT )$$/수식$$ " \
              "도서관에 가야 합니다.\n\n"


    P1, P2 = random.sample(['진우', '민수', '은지', '민희', '지효', '민서', '선미', '은서', '영미'], 2)

    A, B = [[2, 5], [2, 7], [3, 4], [3, 5]][np.random.randint(0, 4)]
    C = np.random.randint(1, 13)

    divisor1 = getdivisor(A)
    divisor2 = getdivisor(B)

    inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
    inter.sort()
    maxnum = inter[-1]

    D = int(A * B / maxnum)
    S1 = D + 1
    S2 = int(D/B)

    stem = stem.format(P1=P1, P2=P2, A=A, B=B, C=C)
    answer = answer.format(S1=S1, S2=S2, C=C)
    comment = comment.format(A=A, B=B, C=C, D=D, S1=S1, S2=S2, P1=P1, P2=P2)

    return stem, answer, comment





















# 5-1-2-82
def denandmul512_Stem_063():
    stem = "$$수식$${A}$$/수식$${ro1} 나누어도 $$수식$${C}$$/수식$${j1} 남고, $$수식$${B}$$/수식$${ro2} 나누어도 $$수식$${C}$$/수식$${j1} 남는 어떤 수 중에서 가장 작은 두 자리 수를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${S}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수에서 $$수식$${C}$$/수식$${j2} 뺀 수는 $$수식$${A}$$/수식$${j3} $$수식$${B}$$/수식$${ro2} 나누면 " \
              "나누어떨어지므로 $$수식$${A}$$/수식$${j3} $$수식$${B}$$/수식$$의 공배수입니다.\n" \
              "$$수식$${A}$$/수식$${j3} $$수식$${B}$$/수식$$의 공배수는 $$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$, $$수식$$CDOTS CDOTS$$/수식$$이므로 " \
              "가장 작은 수는 $$수식$${a1}$$/수식$$입니다.\n" \
              "$$수식$$LEFT ($$/수식$$어떤 수$$수식$$RIGHT ) - {C} = LEFT ( {A}$$/수식$${j3} $$수식$${B}$$/수식$$의 최소공배수$$수식$$RIGHT )$$/수식$$이므로\n" \
              "$$수식$$LEFT ($$/수식$$어떤 수$$수식$$RIGHT ) - {C} = {a1}$$/수식$$,\n" \
              "$$수식$$LEFT ($$/수식$$어떤 수$$수식$$RIGHT ) = {S}$$/수식$$\n\n"


    A, B = random.sample(list(range(3, 10)), 2)

    if A < B:
        C = np.random.randint(1, A)
    else:
        C = np.random.randint(1, B)

    divisor1 = getdivisor(A)
    divisor2 = getdivisor(B)

    inter = list(set(divisor1) & set(divisor2))  # 교집합 구하기
    inter.sort()
    maxnum = inter[-1]

    a1 = int(A * B / maxnum)

    a2 = a1 * 2
    a3 = a1 * 3
    S = a1 + C

    if A == 3 or A == 6:
        ro1 = "으로"
    else:
        ro1 = "로"

    if B == 3 or B == 6:
        ro2 = "으로"
    else:
        ro2 = "로"

    j1 = proc_jo(C, 0)

    j2 = proc_jo(C, 1)

    j3 = proc_jo(A, 2)

    stem = stem.format(A=A, B=B, C=C, ro1=ro1, ro2=ro2, j1=j1)
    answer = answer.format(S=S)
    comment = comment.format(A=A, B=B, C=C, a1=a1, a2=a2, a3=a3, S=S, j2=j2, j3=j3, ro2=ro2)

    return stem, answer, comment
