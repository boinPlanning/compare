import numpy as np
import operator
import random






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
    4: "㉤",
    5: "㉥"
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
        # 이(라고)
        if bool_jo(num):
            return "이"
        return ""
    elif bool_jo(num):
        # 을를
        return "을"
    return "를"













def get_josa(a, b):
    if b == "로" or b == "으로":
        if type(a) == int:
            if (str(a))[-1] == "3" or (str(a))[-1] == "6" or (str(a))[-1] == "0":
                return "으로"
            else:
                return "로"
        else:
            if a[-1] == "3" or a[-1] == "6" or a[-1] == "0":
                return "으로"
            else:
                return "로"
















def show_int(a):
    if a == a // 1:
        b = int(a)
        return b
    else:
        return a






















# 4-2-3-01
def decimaladdsub423_Stem_001():
    stem = "□ 안에 알맞은 소수를 써넣으세요.\n$$수식$$ LEFT ( 1 RIGHT ) $$/수식$$ $$수식$${a}$$/수식$${j1} $$수식$${m}$$/수식$$개, $$수식$${b}$$/수식$${j2} $$수식$${n}$$/수식$$개, $$수식$${c}$$/수식$${j3} $$수식$${p}$$/수식$$개인 수는 $$수식$${box1}$$/수식$$입니다.\n$$수식$$ LEFT ( 2 RIGHT ) $$/수식$$ $$수식$${d}$$/수식$${j4} $$수식$${x}$$/수식$$개, $$수식$${a}$$/수식$${j1} $$수식$${y}$$/수식$$개, $$수식$${f}$$/수식$${j5} $$수식$${z}$$/수식$$개, $$수식$${g}$$/수식$${j6} $$수식$${u}$$/수식$$개인 수는 $$수식$${box2}$$/수식$$입니다.\n"
    answer = "(정답)\n㉠ $$수식$${a1}$$/수식$$, ㉡ $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n$$수식$$ LEFT ( 1 RIGHT ) $$/수식$$ $$/수식$$ $$수식$${a}$$/수식$${j1} $$수식$${m}$$/수식$$개, $$수식$${b}$$/수식$${j2} $$수식$${n}$$/수식$$개, " \
              "$$수식$${c}$$/수식$${j3} $$수식$${p}$$/수식$$개인 수는 $$수식$${t}$$/수식$$입니다.\n" \
              "$$수식$$ LEFT ( 2 RIGHT ) $$/수식$$ $$수식$${d}$$/수식$${j4} $$수식$${x}$$/수식$$개, $$수식$${a}$$/수식$${j1} $$수식$${y}$$/수식$$개, " \
              "$$수식$${f}$$/수식$${j5} $$수식$${z}$$/수식$$개, $$수식$${g}$$/수식$${j6} $$수식$${u}$$/수식$$개인 수는 $$수식$${r}$$/수식$$입니다.\n\n"


    a = np.random.randint(1, 3)
    m = np.random.randint(1, 10)
    n = np.random.randint(1, 10)
    p = np.random.randint(1, 10)

    x = np.random.randint(1, 10)
    y = np.random.randint(1, 10)
    z = np.random.randint(1, 10)
    u = np.random.randint(1, 10)

    b = round(a / 10, 1)
    c = round(a / 100, 2)

    d = 10 * a

    f = f"{a} over 10"
    g = f"{a} over 100"

    j1 = proc_jo(a, 0)
    j2 = proc_jo(b, 0)
    j3 = proc_jo(c, 0)

    j4 = proc_jo(d, 0)
    j5 = proc_jo(f, 0)
    j6 = proc_jo(g, 0)

    t = round(a * m + b * n + c * p, 2)
    r = round(d * x + a * y + (a / 10) * z + (a / 100) * u, 2)

    box1 = "box{㉠````````````````````}"
    box2 = "box{㉡````````````````````}"

    stem = stem.format(box1=box1, box2=box2, a=a, m=m, b=b, n=n, c=c, p=p, d=d, x=x, y=y, f=f, z=z, g=g, u=u, j1=j1,
                       j2=j2, j3=j3, j4=j4, j5=j5, j6=j6)
    answer = answer.format(a1=t, a2=r)
    comment = comment.format(a=a, m=m, b=b, n=n, c=c, p=p, d=d, x=x, y=y, f=f, z=z, g=g, u=u, j1=j1, j2=j2, j3=j3,
                             j4=j4, j5=j5, j6=j6, t=t, r=r)

    return stem, answer, comment



































# 4-2-3-02
def decimaladdsub423_Stem_002():
    stem = "다음 중 소수 둘째 자리 숫자가 가장 큰 수를 찾아 써 보세요.\n$$표$$ $$수식$${x1}$$/수식$$   $$수식$${x2}$$/수식$$   $$수식$${x3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n소수 둘째 자리 숫자를 각각 알아보면 \n" \
              "{z1}, {z2}, {z3}입니다.\n" \
              "따라서 $$수식$$ {s1} $$/수식$$" \
              "이므로 소수 둘째 자리 숫자가 가장 큰 수는 $$수식$${a1}$$/수식$$입니다.\n\n"


    a = np.random.randint(1, 10)
    b = np.random.randint(0, 10)
    c = np.random.randint(1, 10)

    d = np.random.randint(1, 10)
    e = np.random.randint(0, 10)
    f = np.random.randint(1, 10)

    while c == f:
        f = np.random.randint(1, 10)

    g = np.random.randint(1, 10)
    h = np.random.randint(1, 10)

    i = np.random.randint(0, 10)
    j = np.random.randint(1, 10)

    while c == j or f == j:
        j = np.random.randint(1, 10)

    m = a * 100 + b * 10 + c
    n = d * 100 + e * 10 + f

    l = g * 1000 + h * 100 + i * 10 + j

    a = round(m / 100, 2)
    b = round(n / 100, 2)
    c = round(l / 100, 2)

    candidates = [a, b, c]
    np.random.shuffle(candidates)
    [x1, x2, x3] = candidates

    y1 = round((x1 * 100) % 10)
    y2 = round((x2 * 100) % 10)
    y3 = round((x3 * 100) % 10)

    z1 = f"$$수식$$ {x1} $$/수식$$" + f" → $$수식$$ {y1} $$/수식$$"
    z2 = f"$$수식$$ {x2} $$/수식$$" + f" → $$수식$$ {y2} $$/수식$$"
    z3 = f"$$수식$$ {x3} $$/수식$$" + f" → $$수식$$ {y3} $$/수식$$"

    y_list = [y1, y2, y3]
    y_list.sort(reverse=True)

    s1 = str(y_list[0]) + "` &gt; `" + str(y_list[1]) + "` &gt; `" + str(y_list[2])

    if y_list[0] == y1:
        a1 = x1
    elif y_list[0] == y2:
        a1 = x2
    else:
        a1 = x3

    stem = stem.format(x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=a1)
    comment = comment.format(z1=z1, z2=z2, z3=z3, s1=s1, a1=a1)

    return stem, answer, comment






























# 4-2-3-03
def decimaladdsub423_Stem_003():
    stem = "소수 둘째 자리 수가 가장 작은 수는 어느 것인가요?\n① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n소수 둘째 자리 수를 각각 찾아봅니다.\n" \
              "① $$수식$${x6}$$/수식$$  ② $$수식$${x7}$$/수식$$  ③ $$수식$${x8}$$/수식$$  " \
              "④ $$수식$${x9}$$/수식$$  ⑤ $$수식$${x10}$$/수식$$\n\n"


    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    x6 = num_list.pop(np.random.randint(0, len(num_list)))
    x7 = num_list.pop(np.random.randint(0, len(num_list)))
    x8 = num_list.pop(np.random.randint(0, len(num_list)))

    x9 = num_list.pop(np.random.randint(0, len(num_list)))
    x10 = num_list.pop(np.random.randint(0, len(num_list)))

    x1 = round((np.random.randint(1, 10) * 100 + np.random.randint(0, 10) * 10 + x6) / 100, 2)
    x2 = round((np.random.randint(1, 10) * 100 + np.random.randint(0, 10) * 10 + x7) / 100, 2)
    x3 = round((np.random.randint(1, 10) * 100 + np.random.randint(0, 10) * 10 + x8) / 100, 2)

    x4 = round((np.random.randint(1, 10) * 100 + np.random.randint(0, 10) * 10 + x9) / 100, 2)
    x5 = round((np.random.randint(1, 10) * 100 + np.random.randint(0, 10) * 10 + x10) / 100, 2)

    answerd = {x6: 0, x7: 1, x8: 2, x9: 3, x10: 4}
    answer_list = sorted(answerd.items(), key=operator.itemgetter(0))
    a1 = answer_dict[answer_list[0][1]]

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=a1)
    comment = comment.format(x6=x6, x7=x7, x8=x8, x9=x9, x10=x10)

    return stem, answer, comment
































# 4-2-3-04
def decimaladdsub423_Stem_004():
    stem = "일의 자리 숫자가 $$수식$${x1}$$/수식$$, 소수 첫째 자리 숫자가 $$수식$${x2}$$/수식$$, 소수 둘째 자리 숫자가 $$수식$${x3}$$/수식$$인 소수 두 자리 수를 쓰고 읽어 보세요.\n$$수식$${box1}$$/수식$$\n$$수식$${box2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, {a2}\n"
    comment = "(해설)\n일의 자리 숫자가 $$수식$${x1}$$/수식$$, 소수 첫째 자리 숫자가 $$수식$${x2}$$/수식$$, 소수 둘째 자리 숫자가 $$수식$${x3}$$/수식$$인 " \
              "수는 $$수식$${a1}$$/수식$$입니다. $$수식$${a1}$$/수식$${j1} {a2} {rago} 읽습니다.\n\n"


    num = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']

    x1 = np.random.randint(0, 10)
    x2 = np.random.randint(0, 10)
    x3 = np.random.randint(1, 10)

    a1 = round(x1 + x2 / 10 + x3 / 100, 2)
    a2 = num[x1] + " 점 " + num[x2] + num[x3]

    j1 = proc_jo(a2, -1)

    box1 = "box{(쓰기)``````````````````````````````}"
    box2 = "box{(읽기)``````````````````````````````}"

    if x3 == 2 or x3 == 4 or x3 == 5 or x3 == 9:
        rago = "라고"
    else:
        rago = "이라고"

    stem = stem.format(x1=x1, x2=x2, x3=x3, box1=box1, box2=box2)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(x1=x1, x2=x2, x3=x3, a1=a1, a2=a2, j1=j1, rago=rago)

    return stem, answer, comment





























# 4-2-3-05
def decimaladdsub423_Stem_005():
    stem = "소수를 읽은 것입니다. 잘못 읽은 것을 찾아 기호를 써 보세요.\n$$표$$ ㉠ {s1}\n㉡ {s2}\n㉢ {s3} $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n{a1} $$수식$${z1}$$/수식$${j1} '{k1}'{rago} 읽습니다.\n\n"


    num = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']

    k = np.random.randint(1, 1000)

    while k % 10 == 0:
        k = np.random.randint(1, 1000)

    m = np.random.randint(1, 1000)

    while m == k or m % 10 == 0:
        m = np.random.randint(1, 1000)

    n = np.random.randint(1, 1000)

    while n == m or n == k or n % 10 == 0:
        n = np.random.randint(1, 1000)

    z1 = round(k / 100, 2)
    z2 = round(m / 100, 2)
    z3 = round(n / 100, 2)

    k1 = num[int(z1)] + " 점 " + num[int((k % 100 - k % 10) // 10)] + num[int(k % 10)]
    k1_ = num[int(z1)] + " 점 " + num[int((k % 100 - k % 10) // 10)] + "십" + num[int(k % 10)]
    if num[int((k % 100 - k % 10) // 10)] == "일":
        k1_ = num[int(z1)] + " 점 " + "십" + num[int(k % 10)]

    k2 = num[int(z2)] + " 점 " + num[int((m % 100 - m % 10) // 10)] + num[int(m % 10)]
    k3 = num[int(z3)] + " 점 " + num[int((n % 100 - n % 10) // 10)] + num[int(n % 10)]

    t1 = f"$$수식$${z1}$$/수식$$ → {k1_}"
    t2 = f"$$수식$${z2}$$/수식$$ → {k2}"
    t3 = f"$$수식$${z3}$$/수식$$ → {k3}"

    j1 = proc_jo(k1, -1)
    j2 = proc_jo(k1, 3)

    candidates = [t1, t2, t3]
    np.random.shuffle(candidates)
    [s1, s2, s3] = candidates

    correct_idx = 0

    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == t1:
            correct_idx = idx
            break

    if int((str(k))[-1]) == 2 or int((str(k))[-1]) == 4 or int((str(k))[-1]) == 5 or int((str(k))[-1]) == 9:
        rago = "라고"
    else:
        rago = "이라고"

    stem = stem.format(s1=s1, s2=s2, s3=s3)
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(a1=answer_kodict[correct_idx], z1=z1, k1=k1, j1=j1, j2=j2, rago=rago)

    return stem, answer, comment



































# 4-2-3-07
def decimaladdsub423_Stem_006():
    stem = "$$수식$${x1}$$/수식$${j3} 바르게 설명한 것을 찾아 기호를 써 보세요.\n$$표$$ ㉠ {s1}\n㉡ {s2}\n㉢ {s3} $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n{na1} {z1}\n" \
              "{na2} {z2}\n\n"

    m = np.random.randint(101, 1000)

    while m % 10 == 0 or m // 100 == m % 10 or m // 100 == (m % 100 - m % 10) // 10 or m % 10 == (m % 100 - m % 10) // 10:
        m = np.random.randint(101, 1000)

    x1 = round(m / 100, 2)

    # b = np.random.randint(0, 10)
    #
    # while b == int((m % 100 - m % 10) // 10):
    #     b = np.random.randint(0, 10)

    m_str = str(m)
    m_str1 = m_str[0]
    m_str2 = m_str[1]

    m_str1_int = int(m_str1)
    m_str2_int = int(m_str2)

    b = [m_str1_int, m_str2_int][np.random.randint(0, 2)]

    b_ = int(m % 10)

    c_choice = np.random.randint(0, 2)
    if c_choice == 0:
        c = m % 10
        c_ = round(0.01 * c, 2)
    else:
        c = m_str2_int
        c_ = round(0.1 * c, 1)

    # c = m % 10
    # c_ = 0.01 * c

    j1 = proc_jo(c, -1)
    j2 = proc_jo(c, 4)
    j3 = proc_jo(m % 10, 4)

    y1 = f"$$수식$$0.01$$/수식$$이 $$수식$${m}$$/수식$$개인 수입니다."
    y2 = f"소수 둘째 자리 숫자는 $$수식$${b}$$/수식$$입니다."
    y3 = f"$$수식$${c}$$/수식$${j1} $$수식$${c}$$/수식$${j2} 나타냅니다."

    y2_ = f"소수 둘째 자리 숫자는 $$수식$${b_}$$/수식$$입니다."
    y3_ = f"$$수식$${c}$$/수식$${j1} $$수식$${c_}$$/수식$${j2} 나타냅니다."

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [s1, s2, s3] = candidates

    na1 = na2 = -1

    correct_idx = 0

    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y1:
            correct_idx = idx
        elif sdx == y2:
            if na1 == -1:
                na1 = idx
                z1 = y2_
            else:
                na2 = idx
                z2 = y2_
        else:
            if na1 == -1:
                na1 = idx
                z1 = y3_
            else:
                na2 = idx
                z2 = y3_

    stem = stem.format(x1=x1, s1=s1, s2=s2, s3=s3, j3=j3)
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(na1=answer_kodict[na1], z1=z1, na2=answer_kodict[na2], z2=z2)

    return stem, answer, comment






































# 4-2-3-08
def decimaladdsub423_Stem_007():
    stem = "{who}와 친구들은 과수원에서 {fruit}{j3} $$수식$$100$$/수식$$개 땄습니다. 그중에서 {who}가 $$수식$${x1}$$/수식$$개를 가졌다면 {who}가 가진 {fruit}{j2} 전체 {fruit}의 얼마인지 소수로 나타내 보세요.\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n{who}가 가진 {fruit}{j2} $$수식$$100$$/수식$$개 중의 $$수식$${x1}$$/수식$$개이므로 전체 {fruit}의 $$수식$${x1} over 100$$/수식$$입니다.\n" \
              "분수 $$수식$${x1} over 100$$/수식$${j1} 소수로 나타내면 $$수식$${a1}$$/수식$$입니다.\n\n"

    who = ["정우", "준기", "미나", "은하", "재호", "지희", "영래", "은배", "혜수", "석우", "희주"][np.random.randint(0, 11)]

    fruit = ["감", "사과", "배", "복숭아", "참외", "포도", "자두"][np.random.randint(0, 7)]

    j3 = proc_jo(fruit, 1)
    j2 = proc_jo(fruit, -1)

    x1 = np.random.randint(11, 100)

    while x1 % 10 == 0:
        x1 = np.random.randint(11, 100)

    a1 = round(x1 / 100, 2)
    j1 = proc_jo(x1, 4)

    stem = stem.format(x1=x1, who=who, j3=j3, j2=j2, fruit=fruit)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, a1=a1, j1=j1, who=who, j2=j2, fruit=fruit)

    return stem, answer, comment






































# 4-2-3-10
def decimaladdsub423_Stem_008():
    stem = "{who}가 종이에 적힌 소수를 잘못하여 소수 첫째 자리 숫자와 소수 둘째 자리 숫자를 서로 바꿔 읽었더니 {s1}{da}. 종이에 적힌 소수는 무엇인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n{s1}{j1} 소수로 쓰면 $$수식$${x1}$$/수식$$입니다.\n" \
              "$$수식$${x1}$$/수식$$에서 소수 첫째 자리 숫자와 소수 둘째 자리 숫자를 바꾸면 $$수식$${x2}$$/수식$$입니다.\n\n"


    who = ["정우", "준기", "미나", "은하", "재호", "지희", "영래", "은배", "혜주", "석우", "희주"][np.random.randint(0, 11)]

    num = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']

    x = np.random.randint(0, 10)
    y = np.random.randint(0, 10)
    z = np.random.randint(1, 10)

    while y == z:
        z = np.random.randint(1, 10)

    x1 = round(x + y * 0.1 + z * 0.01, 2)
    x2 = round(x + z * 0.1 + y * 0.01, 2)

    s1 = num[x] + " 점 " + num[y] + num[z]
    j1 = proc_jo(s1, 4)

    if z == 2 or z == 4 or z == 5 or z == 9:
        da = "였습니다"
    else:
        da = "이였습니다"

    stem = stem.format(s1=s1, da=da, who=who)
    answer = answer.format(a1=x2)
    comment = comment.format(s1=s1, j1=j1, x1=x1, x2=x2)

    return stem, answer, comment









































# 4-2-3-11
def decimaladdsub423_Stem_009():
    stem = "$$수식$$1$$/수식$$이 $$수식$${x1}$$/수식$$개, $$수식$$0.1$$/수식$$이 $$수식$${x2}$$/수식$$개, $$수식$$0.01$$/수식$$이 $$수식$${x3}$$/수식$$개인 수를 구해 보세요.\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$$1$$/수식$$이 $$수식$${x1}$$/수식$$개이면 $$수식$${x4}$$/수식$$, " \
              "$$수식$$0.1$$/수식$$이 $$수식$${x2}$$/수식$$개이면 $$수식$${x5}$$/수식$$, " \
              "$$수식$$0.01$$/수식$$이 $$수식$${x3}$$/수식$$개이면 $$수식$${x6}$$/수식$$입니다.\n" \
              "즉, $$수식$${x4} + {x5} + {x6} = {a1}$$/수식$$\n"\
              "따라서 $$수식$$1$$/수식$$이 $$수식$${x1}$$/수식$$개, $$수식$$0.1$$/수식$$이 $$수식$${x2}$$/수식$$개, $$수식$$0.01$$/수식$$이 $$수식$${x3}$$/수식$$개인 수는 $$수식$${a1}$$/수식$$입니다.\n\n"


    x1 = np.random.randint(1, 10)
    x2 = np.random.randint(11, 100)

    while x2 % 10 == 0:
        x2 = np.random.randint(11, 100)

    x3 = np.random.randint(11, 100)

    while x3 % 10 == 0:
        x3 = np.random.randint(11, 100)

    x4 = x1
    x5 = round(x2 * 0.1, 1)
    x6 = round(x3 * 0.01, 2)
    a1 = round(x4 + x5 + x6, 2)

    stem = stem.format(x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, a1=a1)

    return stem, answer, comment



































# 4-2-3-13
def decimaladdsub423_Stem_010():
    stem = "밑줄 친 $$수식$${x1}$$/수식$${j1} 나타내는 수를 써 보세요.\n$$수식$$ LEFT ( 1 RIGHT ) `` {x2}{lg}under{lg}{x1}{rg}{rg}$$/수식$$ → $$수식$$ {box1} $$/수식$$\n$$수식$$ LEFT ( 2 RIGHT ) `` {x3}{lg}under{lg}{x1}{rg}{rg}{x4}$$/수식$$ → $$수식$$ {box2} $$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${a1}$$/수식$$, ㉡ $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ LEFT ( 1 RIGHT ) `` {x2}{lg}under{lg}{x1}{rg}{rg}$$/수식$$ → 소수 셋째 자리 숫자,\n" \
              "나타내는 수는 $$수식$${a1}$$/수식$$입니다.\n" \
              "$$수식$$ LEFT ( 2 RIGHT ) `` {x3}{lg}under{lg}{x1}{rg}{rg}{x4}$$/수식$$ → 소수 둘째 자리 숫자,\n" \
              "나타내는 수는 $$수식$${a2}$$/수식$$입니다.\n\n"

    x1 = np.random.randint(1, 10)
    x2 = round(np.random.randint(100, 1000) / 100, 2)

    x3 = round(np.random.randint(10, 100) / 10, 1)
    x4 = np.random.randint(1, 10)

    a1 = round(x1 * 0.001, 3)
    a2 = round(x1 * 0.01, 2)

    lg = "{"
    rg = "}"

    j1 = proc_jo(x1, 0)

    box1 = "box{%s````````````````````}"%"㉠"
    box2 = "box{%s````````````````````}"%"㉡"

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, lg=lg, rg=rg, j1=j1, box1=box1, box2=box2)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, lg=lg, rg=rg, a1=a1, a2=a2)

    return stem, answer, comment






































# 4-2-3-14
def decimaladdsub423_Stem_011():
    stem = "다음 중 소수 셋째 자리 수가 가장 작은 수를 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${x1}$$/수식$$   ㉡ $$수식$${x2}$$/수식$$   ㉢ $$수식$${x3}$$/수식$$\n㉣ $$수식$${x4}$$/수식$$   ㉤ $$수식$${x5}$$/수식$$   ㉥ $$수식$${x6}$$/수식$$   $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n소수 셋째 자리 수를 각각 구해 보면\n" \
              "㉠ $$수식$${x1}$$/수식$$ → $$수식$${z1}$$/수식$$  ㉡ $$수식$${x2}$$/수식$$ → $$수식$${z2}$$/수식$$  ㉢ $$수식$${x3}$$/수식$$ → $$수식$${z3}$$/수식$$\n" \
              "㉣ $$수식$${x4}$$/수식$$ → $$수식$${z4}$$/수식$$  ㉤ $$수식$${x5}$$/수식$$ → $$수식$${z5}$$/수식$$  ㉥ $$수식$${x6}$$/수식$$ → $$수식$${z6}$$/수식$$\n" \
              "따라서 소수 셋째 자리 수는\n" \
              "$$수식$${s1}$$/수식$$\n" \
              "이므로 가장 작은 수는 {a1}입니다.\n\n"


    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    z1 = num_list.pop(np.random.randint(0, len(num_list)))
    z2 = num_list.pop(np.random.randint(0, len(num_list)))
    z3 = num_list.pop(np.random.randint(0, len(num_list)))

    z4 = num_list.pop(np.random.randint(0, len(num_list)))
    z5 = num_list.pop(np.random.randint(0, len(num_list)))
    z6 = num_list.pop(np.random.randint(0, len(num_list)))

    x1 = round(np.random.randint(100, 1000) / 100 + z1 * 0.001, 3)
    x2 = round(np.random.randint(100, 1000) / 100 + z2 * 0.001, 3)
    x3 = round(np.random.randint(100, 1000) / 100 + z3 * 0.001, 3)

    x4 = round(np.random.randint(100, 1000) / 100 + z4 * 0.001, 3)
    x5 = round(np.random.randint(100, 1000) / 100 + z5 * 0.001, 3)
    x6 = round(np.random.randint(100, 1000) / 100 + z6 * 0.001, 3)

    z_dict = {z1: 0, z2: 1, z3: 2, z4: 3, z5: 4, z6: 5}

    z_list = sorted(z_dict.items(), key=operator.itemgetter(0), reverse=True)

    s1 = ""

    for i in range(len(z_list)):
        s1 = s1 + str(z_list[i][0]) + "` &gt; `"

    s1 = s1[0:-6]

    a1 = answer_kodict[z_list[5][1]]

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6)
    answer = answer.format(a1=a1)
    comment = comment.format(a1=a1, s1=s1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, z1=z1, z2=z2, z3=z3, z4=z4, z5=z5,
                             z6=z6)

    return stem, answer, comment






































# 4-2-3-15
def decimaladdsub423_Stem_012():
    stem = "다음은 분수를 소수로 나타낸 것입니다. 틀린 것을 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${x1}$$/수식$$   ㉡ $$수식$${x2}$$/수식$$\n㉢ $$수식$${x3}$$/수식$$   ㉣ $$수식$${x4}$$/수식$$  $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n{a1} $$수식$${y2_}$$/수식$${j1} 소수로 나타내면 $$수식$${z1}$$/수식$$입니다.\n\n"


    a = np.random.randint(1, 10)
    b = np.random.randint(0, 10)
    c = np.random.randint(1, 10)

    d = np.random.randint(1, 10)
    e = np.random.randint(1, 10)
    f = np.random.randint(1, 10)

    g = np.random.randint(1, 10)
    h = np.random.randint(0, 10)
    i = np.random.randint(1, 10)
    m = np.random.randint(1, 10)

    y1 = str(a * 100 + b * 10 + c) + f" over 1000 ` = ` 0.{a}{b}{c}"
    y2 = str(d * 10 + e) + f" over 1000 ` = ` 0.{d}{e}"

    y3 = f"{f} " + str(g * 100 + h * 10 + i) + f" over 1000 ` = ` {f}.{g}{h}{i}"
    y4 = f"{m} over 1000 ` = ` 0.00{m}"

    y2_ = str(d * 10 + e) + f" over 1000"

    candidates = [y1, y2, y3, y4]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4] = candidates

    correct_idx = 0

    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y2:
            correct_idx = idx
            break

    z1 = round((10 * d + e) / 1000, 3)
    j1 = proc_jo(e, 4)

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4)
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(a1=answer_kodict[correct_idx], z1=z1, y2_=y2_, j1=j1)

    return stem, answer, comment


































# 4-2-3-17
def decimaladdsub423_Stem_013():
    stem = "□ 안에 알맞은 소수를 써넣으세요.\n$$수식$$ LEFT ( 1 RIGHT ) ````1 $$/수식$$이 $$수식$${a}$$/수식$$개, $$수식$$0.1$$/수식$$이 $$수식$${b}$$/수식$$개, $$수식$$0.001$$/수식$$이 $$수식$${c}$$/수식$$개인 수는 $$수식$${box1}$$/수식$$입니다.\n$$수식$$ LEFT ( 2 RIGHT ) ````10 $$/수식$$이 $$수식$${x}$$/수식$$개, $$수식$$1$$/수식$$이 $$수식$${y}$$/수식$$개, $$수식$$ 1 over 10 $$/수식$$이 $$수식$${z}$$/수식$$개, $$수식$$ 1 over 100 $$/수식$$이 $$수식$${w}$$/수식$$개, $$수식$$ 1 over 1000 $$/수식$$이 $$수식$${u}$$/수식$$개인 수는 $$수식$${box2}$$/수식$$입니다.\n"
    answer = "(정답)\n㉠ $$수식$${a}.{b}0{c}$$/수식$$, ㉡ $$수식$${x}{y}.{z}{w}{u}$$/수식$$\n"
    comment = "(해설)\n$$수식$$ LEFT ( 1 RIGHT ) ````1 $$/수식$$이 $$수식$${a}$$/수식$$개, $$수식$$0.1$$/수식$$이 $$수식$${b}$$/수식$$개, " \
              "$$수식$$0.001$$/수식$$이 $$수식$${c}$$/수식$$개인 수는 $$수식$${a}.{b}0{c}$$/수식$$입니다.\n" \
              "$$수식$$ LEFT ( 2 RIGHT ) ````10 $$/수식$$이 $$수식$${x}$$/수식$$개, $$수식$$1$$/수식$$이 $$수식$${y}$$/수식$$개, " \
              "$$수식$$ 1 over 10 $$/수식$$이 $$수식$${z}$$/수식$$개, $$수식$$ 1 over 100 $$/수식$$이 $$수식$${w}$$/수식$$개, " \
              "$$수식$$ 1 over 1000 $$/수식$$이 $$수식$${u}$$/수식$$개인 수는 $$수식$${x}{y}.{z}{w}{u}$$/수식$$입니다.\n\n"


    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = np.random.randint(1, 10)

    x = np.random.randint(1, 10)
    y = np.random.randint(1, 10)
    z = np.random.randint(1, 10)

    u = np.random.randint(1, 10)
    w = np.random.randint(1, 10)

    box1 = "box{%s````````````````````}"%"㉠"
    box2 = "box{%s````````````````````}"%"㉡"

    stem = stem.format(box1=box1, box2=box2, a=a, b=b, c=c, x=x, y=y, z=z, w=w, u=u)
    answer = answer.format(a=a, b=b, c=c, x=x, y=y, z=z, w=w, u=u)
    comment = comment.format(a=a, b=b, c=c, x=x, y=y, z=z, w=w, u=u)

    return stem, answer, comment


































# 4-2-3-18
def decimaladdsub423_Stem_014():
    stem = "{wh1}는 선물을 포장하는 데 리본을 $$수식$${a} `` rm m `$$/수식$$ 사용했습니다. {wh1}가 사용한 리본은 소수로 몇 $$수식$$rm {{km}} `$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${a1} `` rm {{km}}$$/수식$$\n"
    comment = "(해설)\n$$수식$$1 `` rm m ` ` = ` 0.001 `` rm {{km}} `$$/수식$$이므로\n" \
              "$$수식$${a} `` rm m ` ` = ` {b} `` rm {{km}} `$$/수식$$\n" \
              "따라서 $$수식$${a} `` rm m ` ` = ` {b} `` rm {{km}} `$$/수식$$입니다.\n\n"


    wh1 = ['연주', '선화', '현주', '재희', "정우", "준기", "미나", "은하", "재호", "지희", "영래", "은배", "혜주", "석우", "희주"][
                np.random.randint(0, 15)]

    a = np.random.randint(1, 1000)
    b = round(a * 0.001, 3)

    stem = stem.format(a=a, wh1=wh1)
    answer = answer.format(a1=b)
    comment = comment.format(a=a, b=b)

    return stem, answer, comment


































# 4-2-3-19
def decimaladdsub423_Stem_015():
    stem = "{wh1}네 집에서 {s1}까지의 거리는 $$수식$$1000 `` rm m `$$/수식$$입니다. {wh1}네 집에서 {s1}{j1} 향해 출발하여 $$수식$${x1} `` rm m `$$/수식$$를 갔습니다. {s1}까지 가는 데 남은 거리는 전체의 얼마인지 소수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${a1} rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$남은 거리$$수식$$RIGHT ) ` = ` 1000 ` - ` {x1} ` = ` {x2} `` LEFT ( rm m RIGHT )$$/수식$$\n" \
              "남은 거리는 $$수식$$ 1000 `` rm m ` $$/수식$$ 중의 $$수식$$ {x2} `` rm m ` $$/수식$$이므로 전체의 $$수식$$ {x2} over 1000 $$/수식$$입니다.\n" \
              "분수 $$수식$$ {x2} over 1000 $$/수식$${j2} 소수로 나타내면 $$수식$${a1}$$/수식$$입니다.\n\n"


    wh1 = ['지수', '현지', '지아', '성호', '연주', '선화', '현주', '재희', "정우", "준기", "미나", "은하", "재호", "지희", "영래", "은배", "혜주", "석우", "희주"][np.random.randint(0, 19)]

    s1 = ['학교', '도서관', '학원', '놀이터', '공원'][np.random.randint(0, 5)]

    x1 = np.random.randint(100, 1000)
    x2 = 1000 - x1

    a1 = round(x2 / 1000, 3)

    j1 = proc_jo(s1, 4)
    j2 = proc_jo(x2, 4)

    stem = stem.format(wh1=wh1, s1=s1, x1=x1, j1=j1)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, a1=a1, j2=j2)

    return stem, answer, comment
































# 4-2-3-20
def decimaladdsub423_Stem_016():
    stem = "어느 {s1} 대회 예선에서 $$수식$$1000$$/수식$$명이 지원하여 $$수식$${x1}$$/수식$$명이 통과하였습니다. 예선을 통과한 사람은 전체의 얼마인지 소수로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n예선을 통과한 사람은 전체의 $$수식$${x1} over 1000$$/수식$$입니다.\n" \
              "따라서 $$수식$$ {x1} over 1000 $$/수식$${j1} 소수로 나타내면 $$수식$${a1}$$/수식$$입니다.\n\n"


    s1 = ['바둑', '피아노', '태권도', '씨름'][np.random.randint(0, 4)]

    x1 = np.random.randint(100, 1000)
    a1 = round(x1 / 1000, 3)
    j1 = proc_jo(x1, 4)

    stem = stem.format(s1=s1, x1=x1, a1=a1)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, a1=a1, j1=j1)

    return stem, answer, comment






























# 4-2-3-21
def decimaladdsub423_Stem_017():
    stem = "$$수식$$ 1 $$/수식$$이 $$수식$$ {a} $$/수식$$개, $$수식$$ 0.1 $$/수식$$이 $$수식$$ {b} $$/수식$$개, $$수식$$ 0.01 $$/수식$$이 $$수식$$ {c} $$/수식$$개, $$수식$$ 0.001 $$/수식$$이 $$수식$$ {d} $$/수식$$개인 수의 소수 둘째 자리가 나타내는 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$$ 1 $$/수식$$이 $$수식$$ {a} $$/수식$$개 → $$수식$$ {q} $$/수식$$\n" \
              "$$수식$$ 0.1 $$/수식$$이 $$수식$$ {b} $$/수식$$개 → $$수식$$ {w} $$/수식$$\n" \
              "$$수식$$ 0.01 $$/수식$$이 $$수식$$ {c} $$/수식$$개 → $$수식$$ {e} $$/수식$$\n" \
              "$$수식$$ 0.001 $$/수식$$이 $$수식$$ {d} $$/수식$$개 → $$수식$$ {r} $$/수식$$\n" \
              " → $$수식$$ {z} $$/수식$$\n" \
              "$$수식$$ 1 $$/수식$$이 $$수식$$ {a} $$/수식$$개, $$수식$$ 0.1 $$/수식$$이 $$수식$$ {b} $$/수식$$개, " \
              "$$수식$$ 0.01 $$/수식$$이 $$수식$$ {c} $$/수식$$개, $$수식$$ 0.001 $$/수식$$이 $$수식$$ {d} $$/수식$$개인 수는 $$수식$${z}$$/수식$$입니다.\n" \
              "따라서 $$수식$${z}$$/수식$$의 소수 둘째 자리 숫자는 $$수식$${k}$$/수식$$이고 $$수식$$0.0{k}$$/수식$${j1} 나타냅니다.\n\n"


    a = np.random.randint(10, 100)
    d = np.random.randint(10, 100)

    b = np.random.randint(1, 10)
    c = np.random.randint(1, 10)

    while int(((c * 10 + d) // 10) % 10) == 0:
        c = np.random.randint(1, 10)

    q = 1 * a
    w = round(0.1 * b, 1)
    e = round(0.01 * c, 2)
    r = round(0.001 * d, 3)

    z = round(q + w + e + r, 3)

    k = int(((z * 1000) % 100) // 10)

    a1 = k * 0.01
    j1 = proc_jo(k, 4)

    stem = stem.format(a=a, b=b, c=c, d=d)
    answer = answer.format(a1=a1)
    comment = comment.format(a=a, b=b, c=c, d=d, q=q, w=w, e=e, r=r, z=z, k=k, j1=j1)

    return stem, answer, comment


































# 4-2-3-22
def decimaladdsub423_Stem_018():
    stem = "조건을 만족하는 소수를 쓰고 읽어 보세요.\n$$표$$ ● 소수 세 자리 수입니다.\n ● $$수식$${x1}$$/수식$$보다 크고 $$수식$${x2}$$/수식$$보다 작습니다.\n ● 소수 첫째 자리 숫자는 $$수식$${x3}$$/수식$$입니다.\n ● 소수 둘째 자리 숫자는 $$수식$${x4}$$/수식$$입니다.\n ● 소수 셋째 자리 숫자는 $$수식$${x5}$$/수식$$입니다. $$/표$$\n$$수식$${box1}$$/수식$$\n$$수식$${box2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, {a2}\n"
    comment = "(해설)\n$$수식$${x1}$$/수식$$보다 크고 $$수식$${x2}$$/수식$$보다 작으므로 일의 자리 숫자는 $$수식$${x1}$$/수식$$입니다.\n" \
              "소수 첫째, 둘째, 셋째 자리 숫자가 각각 $$수식$${x3}$$/수식$$, $$수식$${x4}$$/수식$$, $$수식$${x5}$$/수식$$이므로 조건을 만족하는 소수는 $$수식$${a1}$$/수식$$입니다.\n" \
              "$$수식$${a1}$$/수식$${j1} '{s1}'{j2}라고 읽습니다.\n\n"


    num = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']

    x1 = np.random.randint(1, 9)
    x3 = np.random.randint(0, 10)

    x4 = np.random.randint(0, 10)
    x5 = np.random.randint(1, 10)
    x2 = x1 + 1

    s1 = num[x1] + " 점 " + num[x3] + num[x4] + num[x5]

    j1 = proc_jo(x5, -1)
    j2 = proc_jo(s1, 3)

    a1 = round(x1 + x3 * 0.1 + x4 * 0.01 + x5 * 0.001, 3)

    box1 = "box{(쓰기)``````````````````````````````}"
    box2 = "box{(읽기)``````````````````````````````}"

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, box1=box1, box2=box2)
    answer = answer.format(a1=a1, a2=s1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, s1=s1, a1=a1, j1=j1, j2=j2)

    return stem, answer, comment
































# 4-2-3-24
def decimaladdsub423_Stem_019():
    stem = "두 수의 크기를 비교하여 ○ 안에 $$수식$$ &gt; $$/수식$$, $$수식$$ = $$/수식$$, $$수식$$ &lt; $$/수식$$를 알맞게 써넣으세요.\n$$수식$${x1}$$/수식$$ ○ $$수식$${x2}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n소수의 크기를 비교할 때는 같은 자리끼리 비교해야 합니다.\n" \
              "따라서 $$수식$$ {x3} {a1} {x4} $$/수식$$이므로 $$수식$${x1} {a1} {x2} $$/수식$$입니다.\n\n"

    a = np.random.randint(1, 10)
    b = np.random.randint(0, 10)

    c = np.random.randint(1, 10)
    d = np.random.randint(1, 10)

    y1 = round(a + b * 0.1 + c * 0.01, 2)
    y2 = round(a + b * 0.1 + c * 0.01 + d * 0.001, 3)

    candidates = [y1, y2]
    np.random.shuffle(candidates)
    [x1, x2] = candidates

    if x1 == y2:
        a1 = "&gt;"
        x3 = d
        x4 = 0
    else:
        a1 = "&lt;"
        x3 = 0
        x4 = d

    stem = stem.format(x1=x1, x2=x2)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, a1=a1)

    return stem, answer, comment



































# 4-2-3-25
def decimaladdsub423_Stem_020():
    stem = "더 큰 수를 나타내는 것의 기호를 써 보세요. \n$$표$$㉠ $$수식$$ {x1} $$/수식$$이 $$수식$${x2}$$/수식$$개인 수\n㉡ $$수식$$ {x3} $$/수식$$이 $$수식$${x4}$$/수식$$개인 수 $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n㉠ $$수식$$ {x1} $$/수식$$이 $$수식$${x2}$$/수식$$개인 수는 $$수식$${x5}$$/수식$$입니다.\n" \
              "㉡ $$수식$$ {x3} $$/수식$$이 $$수식$${x4}$$/수식$$개인 수는 $$수식$${x6}$$/수식$$입니다.\n" \
              "따라서 $$수식$$ {x7} {k} {x8}$$/수식$$ 이므로 $$수식$${z1}.{z2}{lg}under{lg}{zl1}{rg}{rg}{zl2} `{k}` {z1}.{z2}{lg}under{lg}{zl3}{rg}{rg}{zl4}$$/수식$$입니다.\n\n"


    y1 = 0.01
    y3 = 0.001

    candidates = [y1, y3]
    np.random.shuffle(candidates)
    [x1, x3] = candidates

    z1 = np.random.randint(1, 10)
    z2 = np.random.randint(0, 10)

    # z3 = np.random.randint(2, 10)
    #
    # z4 = np.random.randint(1, z3)
    while True:
        z3 = np.random.randint(1, 10)
        z4 = np.random.randint(1, 10)
        if z3 - z4 == 1 or z4 - z3 == 1:
            break

    z5 = np.random.randint(1, 10)

    if x1 == y1:
        x2 = z1 * 100 + z2 * 10 + z3
        x4 = z1 * 1000 + z2 * 100 + z4 * 10 + z5
        x5 = round(x2 / 100, 3)
        x6 = round(x4 / 1000, 4)
        x7 = z3
        x8 = z4
        zl1 = z3
        zl2 = ""
        zl3 = z4
        zl4 = z5
        # a1 = "㉠"
        # k = "`&gt;`"

    else:
        x2 = z1 * 1000 + z2 * 100 + z4 * 10 + z5
        x4 = z1 * 100 + z2 * 10 + z3
        x5 = round(x2 / 1000, 4)
        x6 = round(x4 / 100, 3)
        x7 = z4
        x8 = z3
        zl1 = z4
        zl2 = z5
        zl3 = z3
        zl4 = ""
        # a1 = "㉡"
        # k = "`&lt;`"

    if x7 > x8:
        k = "`&gt;`"
        a1 = "㉠"
    else:
        k = "`&lt;`"
        a1 = "㉡"


    lg = "{"
    rg = "}"

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4)
    answer = answer.format(a1=a1)
    comment = comment.format(lg=lg, rg=rg, zl1=zl1, zl2=zl2, zl3=zl3, zl4=zl4, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6,
                             x7=x7, x8=x8, z1=z1, z2=z2, z3=z3, z4=z4, z5=z5, a1=a1, k=k)

    return stem, answer, comment


































# 4-2-3-26
def decimaladdsub423_Stem_021():
    stem = "다음 중 크기가 같은 소수끼리 짝지어진 것은 어느 것인가요?\n① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n소수는 오른쪽 끝자리에 $$수식$$0$$/수식$$을 붙여서 나타낼 수 있습니다.\n" \
              "크기가 같은 소수는 {a1} $$수식$${z1} `=` {z2} $$/수식$$ 입니다.\n\n"


    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = np.random.randint(1, 10)

    d = np.random.randint(1, 10)
    e = np.random.randint(1, 10)
    f = np.random.randint(1, 10)

    m = np.random.randint(1, 10)
    p = np.random.randint(1, 10)

    n = np.random.randint(101, 1000)

    while n % 10 == 0:
        n = np.random.randint(101, 1000)

    r = np.random.randint(101, 1000)

    q = a * 1000 + b * 10 + c
    s = a * 1000 + c * 100 + b * 10
    z = d * 100 + e * 10 + f
    x = d * 1000 + e * 100 + f

    ya = round(m / 10, 1)
    yb = round(m / 100, 2)
    yc = round(n / 10, 2)

    yd = str(round(n / 10, 2)) + "0"
    ye = round(q / 100, 2)
    yf = round(s / 1000, 2)

    yg = p
    yh = round(p / 100, 2)
    yz = round(r / 10, 1)
    yx = round(r / 100, 2)

    y1 = f"$$수식$${ya}$$/수식$$, $$수식$${yb}$$/수식$$"
    y2 = f"$$수식$${yc}$$/수식$$, $$수식$${yd}$$/수식$$"
    y3 = f"$$수식$${ye}$$/수식$$, $$수식$${yf}$$/수식$$"

    y4 = f"$$수식$${yg}$$/수식$$, $$수식$${yh}$$/수식$$"
    y5 = f"$$수식$${yz}$$/수식$$, $$수식$${yx}$$/수식$$"

    z1 = yc
    z2 = yd
    candidates = [y1, y2, y3, y4, y5]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4, x5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y2:
            correct_idx = idx
            break

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, a1=answer_dict[correct_idx], z1=z1, z2=z2)

    return stem, answer, comment































# 4-2-3-27
def decimaladdsub423_Stem_022():
    stem = "$$수식$${x1}$$/수식$$보다 크고 $$수식$${x2}$$/수식$$보다 작은 소수 세 자리 수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n$$수식$${x1}$$/수식$$보다 큰 소수 세 자리 수는 {s1}이고 이 중에서 $$수식$${x2}$$/수식$$보다 작은 소수 세 자리 수는 " \
              "{s2}{ro1} 모두 $$수식$${a1}$$/수식$$개입니다.\n\n"



    m = np.random.randint(1000, 10000)

    while m % 10 == 0:
        m = np.random.randint(1000, 10000)

    n = m + np.random.randint(2, 10)


    x1 = round(m / 1000, 3)
    x2 = round(n / 1000, 3)

    x1 = show_int(x1)
    x2 = show_int(x2)


    s1 = ""

    # for i in range(m + 1, m + 4):
    #     s1 = s1 + "$$수식$$" + str(round(i / 1000, 3)) + "$$/수식$$, "

    for i in range(m + 1, m + 4):
        sample_decimal = round(i / 1000, 3)
        sample_decimal = show_int(sample_decimal)
        s1 = s1 + "$$수식$$" + str(sample_decimal) + "$$/수식$$, "

    s1 = s1 + "$$수식$$ CDOTS $$/수식$$"
    s2 = ""
    a1 = 0

    # for i in range(m + 1, n):
    #     s2 = s2 + "$$수식$$" + str(round(i / 1000, 3)) + "$$/수식$$, "
    #     a1 = a1 + 1

    for i in range(m + 1, n):
        sample_decimal2 = round(i / 1000, 3)
        sample_decimal2 = show_int(sample_decimal2)
        s2 = s2 + "$$수식$$" + str(sample_decimal2) + "$$/수식$$, "
        a1 = a1 + 1

    s2 = s2[0:-2]


    ro1_source1 = n - 1

    if ro1_source1 % 1000 == 0:
        ro1_source = (str(ro1_source1))[0]
    elif ro1_source1 % 100 == 0:
        ro1_source = (str(ro1_source1))[1]
    elif ro1_source1 % 10 == 0:
        ro1_source = (str(ro1_source1))[2]
    elif ro1_source1 % 10 != 0:
        ro1_source = (str(ro1_source1))[-1]


    ro1 = get_josa(ro1_source, "로")



    stem = stem.format(x1=x1, x2=x2)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, s1=s1, s2=s2, a1=a1, ro1=ro1)

    return stem, answer, comment













































# 4-2-3-28
def decimaladdsub423_Stem_023():
    stem = "작은 수부터 차례대로 써 보세요.\n$$표$$ $$수식$${x1}$$/수식$$   $$수식$${x2}$$/수식$$   $$수식$${x3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$\n"
    comment = "(해설)\n자연수 부분이 같으므로 소수 첫째 자리 수를 비교합니다.\n" \
              "따라서 $$수식$$ {y1} `&lt;` {y2} `&lt;` {y3}$$/수식$$이므로 " \
              "작은 수부터 차례대로 쓰면 $$수식$${y1}$$/수식$$, $$수식$${y2}$$/수식$$, $$수식$${y3}$$/수식$$ 입니다.\n\n"


    num = np.random.randint(1, 10)
    a = np.random.randint(1, 8)
    b = a + 1
    c = b + 1

    y1 = round((num * 100 + a * 10 + np.random.randint(1, 10)) / 100, 2)
    y2 = round((num * 100 + b * 10 + np.random.randint(1, 10)) / 100, 2)
    y3 = round((num * 100 + c * 10 + np.random.randint(1, 10)) / 100, 2)

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [x1, x2, x3] = candidates

    stem = stem.format(x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=y1, a2=y2, a3=y3)
    comment = comment.format(y1=y1, y2=y2, y3=y3)

    return stem, answer, comment



































# 4-2-3-29
def decimaladdsub423_Stem_024():
    stem = "다음 중 가장 큰 소수를 찾아 써 보세요.\n$$표$$ $$수식$${x1}$$/수식$$   $$수식$${x2}$$/수식$$   $$수식$${x3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "자연수 부분을 비교하면 $$수식$$ {a} ` &gt; ` 0$$/수식$$이므로, $$수식$${y1}$$/수식$$, $$수식$${y3}$$/수식$${j1} $$수식$${y2}$$/수식$$보다 더 큽니다.\n" \
              "$$수식$${y1}$$/수식$$, $$수식$${y3}$$/수식$$의 소수 첫째 자리 수를 비교하면 $$수식$${b} ` &gt; ` {e}$$/수식$$이므로 $$수식$${y1} ` &gt; ` {y3}$$/수식$$입니다.\n\n"


    a = np.random.randint(1, 10)
    b = np.random.randint(2, 10)
    c = np.random.randint(1, 10)

    d = np.random.randint(1, 10)
    e = np.random.randint(1, b)

    f = np.random.randint(1, 10)
    g = np.random.randint(1, 10)

    p = np.random.randint(1000, 10000)

    while p % 10 == 0 or p // 1000 >= a:
        p = np.random.randint(100, 1000)

    m = a * 1000 + b * 100 + c * 10 + d
    n = a * 1000 + e * 100 + f * 10 + g

    y1 = round(m / 1000, 3)
    y2 = round(p / 1000, 3)
    y3 = round(n / 1000, 3)

    j1 = proc_jo(g, 0)
    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [x1, x2, x3] = candidates

    stem = stem.format(x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=y1)
    comment = comment.format(j1=j1, y1=y1, y2=y2, y3=y3, a=a, b=b, e=e)

    return stem, answer, comment



































# 4-2-3-30
def decimaladdsub423_Stem_025():
    stem = "{wh1}의 키는 $$수식$${x1} `` rm {{cm}} `$$/수식$$이고, {wh2}의 키는 $$수식$${x2} `` rm m `$$/수식$$입니다. {wh1}와 {wh2} 중에서 키가 더 큰 사람은 누구인가요?\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "{wh1}의 키는 $$수식$$ {x1} `` rm {{cm}} ` = ` {x3} `` rm m `$$/수식$$입니다.\n" \
              "따라서 $$수식$${x3} {k1} {x2}$$/수식$$이므로 키가 더 큰 사람은 {a1}입니다.\n\n"


    wh_list = ['진수', '진희', '진수', '진미', '지수', '현지', '지아', '성호', '연주', '선화', '현주', '재희', "정우", "준기", "미나", "은하", "재호",
               "지희", "영래", "은배", "혜주", "석우", "희주"]

    wh1 = wh_list[np.random.randint(0, 23)]
    wh2 = wh_list[np.random.randint(0, 23)]

    while wh1 == wh2:
        wh2 = wh_list[np.random.randint(0, 23)]

    m = np.random.randint(141, 160)
    n = np.random.randint(141, 160)

    while m == n:
        n = np.random.randint(141, 160)

    x1 = m
    x2 = round(n / 100, 2)
    x3 = round(m / 100, 2)

    if x2 > x3:
        a1 = wh2
        k1 = "`&lt;`"
    else:
        a1 = wh1
        k1 = "`&gt;`"

    stem = stem.format(x1=x1, x2=x2, x3=x3, wh1=wh1, wh2=wh2)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, wh1=wh1, a1=a1, k1=k1)

    return stem, answer, comment

































# 4-2-3-32
def decimaladdsub423_Stem_026():
    stem = "□ 안에는 $$수식$$0$$/수식$$부터 $$수식$$9$$/수식$$까지의 어느 수를 넣어도 됩니다. 틀린 것을 찾아 기호를 써 보세요.\n$$표$$ ㉠ {x1}\n㉡ {x2}\n㉢ {x3} $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "{a1}의 □ 안에 $$수식$${k1}$$/수식$$, $$수식$${k2}$$/수식$${j1} 차례로 넣으면 \n" \
              "$$수식$${k1}.{m}{n} ` &lt; ` {l}.{k}{k2}$$/수식$$이므로 □.$$수식$${m}{n} ` &lt; ` {l}.{k}$$/수식$$□입니다.\n\n"


    a = 9
    l = 9
    b = np.random.randint(2, 10)
    c = np.random.randint(1, b)
    d = np.random.randint(1, 10)

    x = np.random.randint(1, 10)
    y = np.random.randint(1, 10)
    z = np.random.randint(1, 9)
    w = np.random.randint(z + 1, 10)

    m = np.random.randint(1, 9)
    n = np.random.randint(1, 10)
    k = np.random.randint(m + 1, 10)

    k1 = l
    k2 = 0

    j1 = proc_jo(k2, 4)

    y1 = f"□.$$수식$${a}{b} ` &gt; ` 0$$/수식$$.□$$수식$${c}{d}$$/수식$$"
    y2 = f"$$수식$${x}.{y}0{z} ` &lt; ` {x}.{y}$$/수식$$□$$수식$${w}$$/수식$$"
    y3 = f"□.$$수식$${m}{n} ` &gt; ` {l}.{k}$$/수식$$□"

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [x1, x2, x3] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y3:
            correct_idx = idx
            break

    stem = stem.format(x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(j1=j1, k1=k1, k2=k2, m=m, n=n, l=l, k=k, a1=answer_kodict[correct_idx])

    return stem, answer, comment
































# 4-2-3-33
def decimaladdsub423_Stem_027():
    stem = "□ 안에 알맞은 수를 써넣으세요.\n$$수식$$ LEFT ( 1 RIGHT ) `` {x1}$$/수식$${j1} $$수식$${x2}$$/수식$$의 $$수식$${box1}$$/수식$$입니다.\n$$수식$$ LEFT ( 2 RIGHT ) `` {x3}$$/수식$${j2} $$수식$${x4}$$/수식$$의 $$수식$${box2}$$/수식$$배입니다.\n"
    answer = "(정답)\n㉠ $$수식$${a1}$$/수식$$, ㉡ $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ LEFT ( 1 RIGHT ) `` {x1}$$/수식$${j1} $$수식$${x2}$$/수식$$의 수가 오른쪽으로 {n} 자리 이동한 것이므로 " \
              "$$수식$${x2}$$/수식$$의 $$수식$$1 over {a1}$$/수식$$입니다.\n" \
              "$$수식$$ LEFT ( 2 RIGHT ) `` {x3}$$/수식$${j2} $$수식$${x4}$$/수식$$의 수가 왼쪽으로 {n} 자리 이동한 것이므로 " \
              "$$수식$${x4}$$/수식$$의 $$수식$${a1}$$/수식$$배입니다.\n\n"


    num = np.random.randint(0, 2)
    n = ['한', '두'][num]
    p = np.random.randint(1000, 10000)

    while p % 10 == 0:
        p = np.random.randint(1000, 10000)

    q = np.random.randint(1000, 10000)

    while q % 10 == 0:
        q = np.random.randint(1000, 10000)

    if num == 0:
        a1 = 10
        x1 = round(p / 1000, 3)
        x2 = round(p / 100, 2)
        x3 = round(q / 10, 1)
        x4 = round(q / 100, 2)
    else:
        a1 = 100
        x1 = round(p / 1000, 3)
        x2 = round(p / 10, 1)
        x3 = round(q / 10, 1)
        x4 = round(q / 1000, 3)

    j1 = proc_jo(x1, -1)
    j2 = proc_jo(x3, -1)

    lg = "{"
    rg = "}"

    box1 = "box{　　　}"
    box2 = "box{　　　}"

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, j1=j1, j2=j2, box1=box1, box2=box2)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, j1=j1, j2=j2, n=n, a1=a1)

    return stem, answer, comment
































# 4-2-3-34
def decimaladdsub423_Stem_028():
    stem = "다음 중 □ 안에 들어갈 수가 다른 하나를 찾아 기호를 써 보세요.\n$$표$$ ㉠ {s1}\n㉡ {s2}\n㉢ {s3} $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "㉠ {z1}\n" \
              "㉡ {z2}\n" \
              "㉢ {z3}\n\n"


    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    x = np.random.randint(1, 10)
    y = np.random.randint(1, 10)

    z = np.random.randint(1, 10)
    p = np.random.randint(1, 10)
    q = np.random.randint(1, 10)
    n = np.random.randint(3, 10)

    nd = n - 1

    num = ['한', '두', '세', '네', '다섯', '여섯', '일곱', '여덟', '아홉'][n - 1]
    numd = ['한', '두', '세', '네', '다섯', '여섯', '일곱', '여덟', '아홉'][n - 2]

    c_ = round(a + 0.1 * b, 1)
    d_ = round(x + 0.1 * y + 0.01 * z, 2)
    k_ = round(0.1 * p + 0.01 * q, 2)

    c = int(c_ * 10 ** n)
    d = int(d_ * 10 ** (nd))
    k = int(k_ * 10 ** n)

    if c % 10 == 9:
        c = c + 1

    if d % 10 == 9:
        d = d + 1

    if k % 10 == 9:
        k = k + 1

    hund = 1
    for idx in range(n):
        hund *= 10

    hundd = 1
    for sdx in range(nd):
        hundd *= 10

    y1 = f"$$수식$$ {a}.{b}$$/수식$$의 □배는 $$수식$${c}$$/수식$$입니다."

    y2 = f"$$수식$$ {x}.{y}{z}$$/수식$$의 □배는 $$수식$${d}$$/수식$$입니다."

    y3 = f"$$수식$$ 0.{p}{q}$$/수식$$의 □배는 $$수식$${k}$$/수식$$입니다."

    x1 = f"$$수식$${c_}$$/수식$$의 소수점을 기준으로 수가 왼쪽으로 {num} 자리 이동하면 $$수식$${c}$$/수식$$이므로 " \
         f"$$수식$${c_}$$/수식$$의 $$수식$${hund}$$/수식$$배는 $$수식$${c}$$/수식$$입니다.\n"

    x2 = f"$$수식$$ {d_}$$/수식$$의 소수점을 기준으로 수가 왼쪽으로 {numd} 자리 이동하면 $$수식$${d}$$/수식$$이므로 " \
         f"$$수식$${d_}$$/수식$$의 $$수식$${hundd}$$/수식$$배는 $$수식$${d}$$/수식$$입니다.\n"

    x3 = f"$$수식$$ {k_}$$/수식$$의 소수점을 기준으로 수가 왼쪽으로 {num} 자리 이동하면 $$수식$${k}$$/수식$$이므로 " \
         f"$$수식$${k_}$$/수식$$의 $$수식$${hund}$$/수식$$배는 $$수식$${k}$$/수식$$입니다.\n"

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [s1, s2, s3] = candidates

    zch1 = 0
    zch2 = 0

    correct_idx = 0

    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == y2:
            correct_idx = idx

        if sdx == y1:
            if zch1 == 0:
                z1 = x1
                zch1 = 1
            elif zch2 == 0:
                z2 = x1
                zch2 = 1
            else:
                z3 = x1
        elif sdx == y2:
            if zch1 == 0:
                z1 = x2
                zch1 = 1
            elif zch2 == 0:
                z2 = x2
                zch2 = 1
            else:
                z3 = x2
        else:
            if zch1 == 0:
                z1 = x3
                zch1 = 1
            elif zch2 == 0:
                z2 = x3
                zch2 = 1
            else:
                z3 = x3

    stem = stem.format(s1=s1, s2=s2, s3=s3)
    answer = answer.format(a1=answer_kodict[correct_idx])
    comment = comment.format(a1=answer_kodict[correct_idx], z1=z1, z2=z2, z3=z3)

    return stem, answer, comment
































# 4-2-3-35
def decimaladdsub423_Stem_029():
    stem = "다음 중 □ 안에 들어갈 수가 가장 작은 것은 어느 것인가요?\n① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n□ 안에 들어갈 수를 각각 알아보면\n" \
              "① $$수식$${z1}$$/수식$$  ② $$수식$${z2}$$/수식$$  ③ $$수식$${z3}$$/수식$$ ④ $$수식$${z4}$$/수식$$  ⑤ $$수식$${z5}$$/수식$$\n" \
              "분자가 $$수식$$1$$/수식$$인 분수는 분모가 클수록 더 작은 수이므로 □ 안에 들어갈 수가 가장 작은 것은 {a1} $$수식$${y5}$$/수식$$입니다.\n\n"


    b = round(np.random.randint(1, 10) / 10, 1)
    d = np.round(1, 10)
    f = round(np.random.randint(10, 100) / 10, 1)

    h = np.random.randint(10, 100)
    y = np.random.randint(100, 1000)

    a = round(b / 10, 3)
    c = round(d / 100, 3)
    e = round(f / 100, 3)

    g = round(h / 100, 2)
    x = round(y / 1000, 3)

    j1 = proc_jo(a % 0.01, -1)
    x1 = f"$$수식$${a}$$/수식$${j1} $$수식$${b}$$/수식$$의 □입니다."
    y1 = "1 over 10"

    j2 = proc_jo(c % 0.01, -1)
    x2 = f"$$수식$${c}$$/수식$${j2} $$수식$${d}$$/수식$$의 □입니다."
    y2 = "1 over 100"

    j3 = proc_jo(e % 0.001, -1)
    x3 = f"$$수식$${e}$$/수식$${j3} $$수식$${f}$$/수식$$의 □입니다."
    y3 = "1 over 100"

    j4 = proc_jo(g % 0.01, -1)
    x4 = f"$$수식$${g}$$/수식$${j4} $$수식$${h}$$/수식$$의 □입니다."
    y4 = "1 over 100"

    j5 = proc_jo(x % 0.001, -1)
    x5 = f"$$수식$${x}$$/수식$${j1} $$수식$${y}$$/수식$$의 □입니다."
    y5 = "1 over 1000"

    candidates = [x1, x2, x3, x4, x5]
    np.random.shuffle(candidates)
    [s1, s2, s3, s4, s5] = candidates

    xy_dict = {x1: y1, x2: y2, x3: y3, x4: y4, x5: y5}

    z1 = xy_dict[s1]
    z2 = xy_dict[s2]
    z3 = xy_dict[s3]
    z4 = xy_dict[s4]
    z5 = xy_dict[s5]

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == x5:
            correct_idx = idx
            break

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(a1=answer_dict[correct_idx], z1=z1, z2=z2, z3=z3, z4=z4, z5=z5, y5=y5)

    return stem, answer, comment

































# 4-2-3-36
def decimaladdsub423_Stem_030():
    stem = "$$수식$${x1}$$/수식$${j1} $$수식$${x2}$$/수식$$배 한 수와 $$수식$${x1}$$/수식$$의 $$수식$$ 1 over {n}$$/수식$$인 수를 차례대로 구해 보세요.\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1}$$/수식$${j1} $$수식$${x2}$$/수식$$배 한 수는 $$수식$${a1}$$/수식$$고, " \
              "$$수식$${x1}$$/수식$$의 $$수식$$1 over {n}$$/수식$$인 수는 $$수식$${a2}$$/수식$$입니다.\n\n"


    k = np.random.randint(1, 100)

    while k % 10 == 0:
        k = np.random.randint(1, 100)

    x1 = round(k / 10, 1)
    m = np.random.randint(1, 4)

    n = 10 ** m
    a1 = round(x1 * n)

    x2 = n
    a2 = round(x1 / n, m + 1)
    j1 = proc_jo(x1, 4)

    stem = stem.format(x1=x1, x2=x2, n=n, j1=j1)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(a1=a1, a2=a2, x1=x1, j1=j1, x2=x2, n=n)

    return stem, answer, comment






























# 4-2-3-38
def decimaladdsub423_Stem_031():
    stem = "더 큰 수를 나타내는 수를 찾아 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${a}$$/수식$${j1} $$수식$${x}$$/수식$$개, $$수식$${b}$$/수식$${j2} $$수식$${y}$$/수식$$개, $$수식$${c}$$/수식$${j3} $$수식$${z}$$/수식$$개, $$수식$${d}$$/수식$${j4} $$수식$${w}$$/수식$$개인 수\n㉡ $$수식$${a}$$/수식$${j1} $$수식$${m}$$/수식$$개, $$수식$${b}$$/수식$${j2} $$수식$${n}$$/수식$$개, $$수식$${c}$$/수식$${j3} $$수식$${p}$$/수식$$개, $$수식$${d}$$/수식$${j4} $$수식$${k}$$/수식$$개인 수 $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n㉠ $$수식$${a}$$/수식$${j1} $$수식$${x}$$/수식$$개 → $$수식$${e}$$/수식$$\n" \
              "$$수식$${b}$$/수식$${j2} $$수식$${y}$$/수식$$개 → $$수식$${f}$$/수식$$\n" \
              "$$수식$${c}$$/수식$${j3} $$수식$${z}$$/수식$$개 → $$수식$${g}$$/수식$$\n" \
              "$$수식$${d}$$/수식$${j4} $$수식$${w}$$/수식$$개 → $$수식$${h}$$/수식$$\n" \
              "→ $$수식$${i}$$/수식$$\n" \
              "㉡ $$수식$${a}$$/수식$${j1} $$수식$${m}$$/수식$$개 → $$수식$${j}$$/수식$$\n" \
              "$$수식$${b}$$/수식$${j2} $$수식$${n}$$/수식$$개 → $$수식$${o}$$/수식$$\n" \
              "$$수식$${c}$$/수식$${j3} $$수식$${p}$$/수식$$개 → $$수식$${u}$$/수식$$\n" \
              "$$수식$${d}$$/수식$${j4} $$수식$${k}$$/수식$$개 → $$수식$${v}$$/수식$$\n" \
              "→ $$수식$${l}$$/수식$$\n" \
              "따라서 $$수식$${i} {xd} {l}$$/수식$$이므로 더 큰 것의 기호는 {a1}입니다."


    # a = np.random.randint(1, 10)
    a = [1, 2, 5][np.random.randint(0, 3)]

    b = round(a / 10, 1)
    c = round(a / 100, 2)
    d = round(a / 1000, 3)

    x = np.random.randint(1, 10)
    m = np.random.randint(1, 10)

    y = np.random.randint(10, 100)
    z = np.random.randint(10, 100)
    w = np.random.randint(10, 100)

    n = np.random.randint(10, 100)
    p = np.random.randint(10, 100)
    k = np.random.randint(10, 100)

    e = a * x
    f = round(b * y, 1)
    g = round(c * z, 2)
    h = round(d * w, 3)
    i = round(e + f + g + h, 3)

    j = a * m
    o = round(b * n, 1)
    u = round(c * p, 2)
    v = round(d * k, 3)
    l = round(j + o + u + v, 3)

    # j1 = proc_jo(a, 0)
    # j2 = proc_jo(b, 0)
    # j3 = proc_jo(c, 0)
    # j4 = proc_jo(d, 0)

    if a == 1:
        j1 = j2 = j3 = j4 = "이"
    else:
        j1 = j2 = j3 = j4 = "가"


    if i > l:
        xd = "`&gt;`"
        a1 = "㉠"
    else:
        xd = "`&lt;`"
        a1 = "㉡"

    stem = stem.format(j1=j1, j2=j2, j3=j3, j4=j4, a=a, x=x, b=b, y=y, c=c, z=z, d=d, w=w, m=m, n=n, p=p, k=k)
    answer = answer.format(a1=a1)
    comment = comment.format(j1=j1, j2=j2, j3=j3, j4=j4, a1=a1, a=a, e=e, f=f, g=g, h=h, j=j, o=o, k=k, u=u, v=v, x=x,
                             b=b, y=y, c=c, z=z, d=d, w=w, m=m, n=n, p=p, i=i, l=l, xd=xd)

    return stem, answer, comment










































# 4-2-3-39
def decimaladdsub423_Stem_032():
    stem = "전자저울은 저울판 위에 올려놓은 물건의 무게가 수로 표시되는 저울입니다. 돌 반지 $$수식$${x1}$$/수식$$개의 무게는 $$수식$${x2} `` rm g `$$/수식$$일 때, 무게가 같은 돌 반지 $$수식$${x3}$$/수식$$개의 무게는 몇 $$수식$$rm g `$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${a1} `` rm g$$/수식$$\n"
    comment = "(해설)\n돌 반지 $$수식$${x3}$$/수식$$개의 무게는 돌 반지 $$수식$${x1}$$/수식$$개의 무게의 $$수식$${n}$$/수식$$배입니다.\n" \
              "따라서 $$수식$${x2} `` rm g `$$/수식$$의 $$수식$${n}$$/수식$$배인 $$수식$${x4} `` rm g `$$/수식$$입니다.\n\n"


    k = np.random.randint(100, 1000)
    x1 = np.random.randint(1, 10)
    n = np.random.randint(1, 10)

    nd = 10 ** n
    x2 = round(k / 100, 2)

    x3 = x1 * nd
    x4 = round(x2 * nd, 1)

    if (x4 * 10) % 10 == 0:
        x4 = int(x4)

    stem = stem.format(x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=x4)
    comment = comment.format(n=nd, x1=x1, x3=x3, x2=x2, x4=x4)

    return stem, answer, comment













































# 4-2-3-40
def decimaladdsub423_Stem_033():
    stem = "설명하는 수의 $$수식$${a}$$/수식$${j1} 구해 보세요.\n$$표$$십의 자리 숫자가 $$수식$${x}$$/수식$$, 일의 자리 숫자가 $$수식$${y}$$/수식$$, 소수 첫째 자리 숫자가 $$수식$${z}$$/수식$$, 소수 둘째 자리 숫자가 $$수식$${w}$$/수식$$인 소수 두 자리 수$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n십의 자리 숫자가 $$수식$${x}$$/수식$$, 일의 자리 숫자가 $$수식$${y}$$/수식$$, " \
              "소수 첫째 자리 숫자가 $$수식$${z}$$/수식$$, 소수 둘째 자리 숫자가 $$수식$${w}$$/수식$$인 소수 두 자리 수는 $$수식$${l}$$/수식$$입니다.\n" \
              "따라서 $$수식$${l}$$/수식$$의 $$수식$${a}$$/수식$${j2} $$수식$${k}$$/수식$$입니다.\n\n"


    m = np.random.randint(1, 5)
    n = 10 ** m
    a = f"1 over {n}"

    x = np.random.randint(1, 10)
    y = np.random.randint(1, 10)
    z = np.random.randint(1, 10)
    w = np.random.randint(1, 10)

    l = round(x * 10 + y + z * 0.1 + w * 0.01, 2)
    k = round(l / n, m + 2)

    j1 = "을"
    j2 = "은"

    stem = stem.format(a=a, j1=j1, x=x, y=y, z=z, w=w)
    answer = answer.format(a1=k)
    comment = comment.format(x=x, y=y, z=z, w=w, l=l, a=a, j2=j2, k=k)

    return stem, answer, comment


































# 4-2-3-41
def decimaladdsub423_Stem_034():
    stem = "$$수식$${a}$$/수식$${j1} $$수식$${x}$$/수식$$개, $$수식$${b}$$/수식$${j1} $$수식$${y}$$/수식$$개, $$수식$${c}$$/수식$${j1} $$수식$${z}$$/수식$$개인 수를 $$수식$${k}$$/수식$$배 하면 얼마인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${a}$$/수식$${j1} $$수식$${x}$$/수식$$개 → $$수식$${p}$$/수식$$\n" \
              "$$수식$${b}$$/수식$${j1} $$수식$${y}$$/수식$$개 → $$수식$${q}$$/수식$$\n" \
              "$$수식$${c}$$/수식$${j1} $$수식$${z}$$/수식$$개 → $$수식$${r}$$/수식$$\n" \
              "→ $$수식$${n}$$/수식$$\n" \
              "따라서 $$수식$${n}$$/수식$$의 $$수식$${k}$$/수식$$배 한 수는 $$수식$${m}$$/수식$$입니다.\n\n"


    # a = np.random.randint(1, 10)

    a = [1, 2, 5][np.random.randint(0, 3)]
    b = round(a / 10, 1)
    c = round(a / 100, 2)

    x = np.random.randint(1, 10)
    y = np.random.randint(10, 100)
    z = np.random.randint(1, 10)

    p = a * x
    q = round(b * y, 1)
    r = round(c * z, 2)
    n = round(p + q + r, 2)

    num = np.random.randint(1, 8)

    k = 10 ** num
    m = round(n * k, 1)
    j1 = proc_jo(a, 0)

    if (m * 10) % 10 == 0:
        m = int(m)

    stem = stem.format(a=a, j1=j1, x=x, b=b, y=y, c=c, z=z, k=k)
    answer = answer.format(a1=m)
    comment = comment.format(x=x, y=y, z=z, a=a, b=b, c=c, j1=j1, p=p, q=q, r=r, n=n, m=m, k=k)

    return stem, answer, comment





































# 4-2-3-42
def decimaladdsub423_Stem_035():
    stem = "혜주는 $$수식$${x1} `` rm {{cm}} `$$/수식$$ 높이의 의자 위에서 키를 재었더니 $$수식$${x2} `` rm {{cm}} `$$/수식$$였습니다. 혜주의 실제 키는 몇 $$수식$$rm m `$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${a1} `` rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$혜주의 실제 키$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$의자 위에 올라가서 잰 키$$수식$$RIGHT ) - LEFT ($$/수식$$의자의 높이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {x2} ` - ` {x1} ` = ` {x3} LEFT ( rm {{cm}} RIGHT )$$/수식$$\n" \
              "따라서 $$수식$${x3} `` rm {{cm}} ` = ` {a1} `` rm m `$$/수식$$입니다.\n\n"


    x1 = np.random.randint(100, 1000)
    x3 = np.random.randint(100, 200)

    x2 = x1 + x3
    x4 = round(x3 / 100, 2)

    stem = stem.format(x1=x1, x2=x2)
    answer = answer.format(a1=x4)
    comment = comment.format(x1=x1, x2=x2, x3=x3, a1=x4)

    return stem, answer, comment

































# 4-2-3-43
def decimaladdsub423_Stem_036():
    stem = "어떤 수를 $$수식$${a}$$/수식$$배 한 수를 구해야 할 것을 잘못하여 어떤 수의 $$수식$$1 over {a}$$/수식$$을 구했더니 $$수식$${c}$$/수식$$이었습니다. 어떤 수를 $$수식$${a}$$/수식$$배 한 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n어떤 수의 $$수식$$1 over {a}$$/수식$$이 $$수식$${c}$$/수식$$이므로 어떤 수는 $$수식$${c}$$/수식$$의 " \
              "$$수식$${a}$$/수식$$배인 $$수식$${k}$$/수식$$입니다.\n" \
              "따라서 어떤 수를 $$수식$${a}$$/수식$$배 한 수는 $$수식$${k}$$/수식$$의 $$수식$${a}$$/수식$$배인 $$수식$${p}$$/수식$$입니다.\n\n"


    n = np.random.randint(1, 5)
    a = 10 ** n

    z = np.random.randint(1000, 10000)
    c = round(z / 1000, 3)

    k = round(a * c, 2)

    if (k * 10) % 10 == 0:
        k = int(k)

    p = round(a * k, 1)

    if (p * 10) % 10 == 0:
        p = int(p)

    stem = stem.format(a=a, c=c)
    answer = answer.format(a1=p)
    comment = comment.format(a=a, c=c, k=k, p=p)

    return stem, answer, comment

































# 4-2-3-44
def decimaladdsub423_Stem_037():
    stem = "㉠과 ㉡에 알맞은 수를 구해 보세요.\n$$수식$${x1} ` + ` {x3}$$/수식$$ → $$수식$${box1}$$/수식$$\n$$수식$${x2} ` + ` {x3}$$/수식$$ → $$수식$${box2}$$/수식$$\n"
    answer = "(정답)\n㉠ $$수식$${a1}$$/수식$$, ㉡ $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n$$수식$${x1} ` + ` {x3} ` = ` {a1}$$/수식$$, $$수식$${x2} ` + ` {x3} ` = ` {a2}$$/수식$$\n\n"


    while True:
        x = np.random.randint(10, 100)
        y = np.random.randint(10, 100)
        if x != y:
            break

    z = np.random.randint(10, 100)

    x1 = round(x / 10, 1)
    x2 = round(y / 10, 1)
    x3 = round(z / 10, 1)

    a1 = round(x1 + x3, 1)
    a2 = round(x2 + x3, 1)

    box1 = "box{㉠````````````````````}"
    box2 = "box{㉡````````````````````}"

    stem = stem.format(x1=x1, x2=x2, x3=x3, box1=box1, box2=box2)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(x1=x1, x2=x2, x3=x3, a1=a1, a2=a2)

    return stem, answer, comment

































# 4-2-3-48
def decimaladdsub423_Stem_038():
    stem = "계산 결과가 $$수식$$1$$/수식$$보다 큰 것을 모두 고르세요.\n① $$수식$${s1}$$/수식$$\n② $$수식$${s2}$$/수식$$\n③ $$수식$${s3}$$/수식$$\n④ $$수식$${s4}$$/수식$$\n⑤ $$수식$${s5}$$/수식$$\n"
    answer = "(정답)\n{a1}, {a2}\n"
    comment = "(해설)\n" \
              "① $$수식$${z1}$$/수식$$,  " \
              "② $$수식$${z2}$$/수식$$,\n" \
              "③ $$수식$${z3}$$/수식$$,  " \
              "④ $$수식$${z4}$$/수식$$,\n" \
              "⑤ $$수식$${z5}$$/수식$$\n\n"




    while True:
        m_ = np.random.randint(11, 19)
        p_ = np.random.randint(11, 19)

        while m_ == p_:
            p_ = np.random.randint(11, 19)

        m = round(m_ / 10, 1)
        p = round(p_ / 10, 1)

        l_ = np.random.randint(2, 10)
        n_ = np.random.randint(2, 10)

        while l_ == n_:
            n_ = np.random.randint(2, 10)

        o_ = np.random.randint(2, 10)

        while o_ == l_ or o_ == n_:
            o_ = np.random.randint(2, 10)

        l = round(l_ / 10, 1)
        n = round(n_ / 10, 1)
        o = round(o_ / 10, 1)

        b = round(np.random.randint(1, l_) / 10, 1)
        c = round(l - b, 1)

        d = e = 1

        while d >= 1 or e >= 1:
            d = round(np.random.randint(1, m_) / 10, 1)
            e = round(m - d, 1)

        f = round(np.random.randint(1, n_) / 10, 1)
        g = round(n - f, 1)

        h = round(np.random.randint(1, o_) / 10, 1)
        i = round(o - h, 1)

        x = y = 1

        while x >= 1 or y >= 1:
            x = round(np.random.randint(1, p_) / 10, 1)
            y = round(p - x, 1)

        check_list = [b, c, d, e, f, g, h, i, x, y]
        check_list.sort()

        check_thing = 0

        for i_dx in range(len(check_list) - 2):
            if check_list[i_dx] == check_list[i_dx + 1] and check_list[i_dx] == check_list[i_dx + 2]:
                check_thing = 1
                break

        if check_thing == 0:
            break


    x1 = f"{b} ` + ` {c}"
    y1 = f"{x1} ` = ` {l}"

    x2 = f"{d} ` + ` {e}"
    y2 = f"{x2} ` = ` {m}"

    x3 = f"{f} ` + ` {g}"
    y3 = f"{x3} ` = ` {n}"

    x4 = f"{h} ` + ` {i}"
    y4 = f"{x4} ` = ` {o}"

    x5 = f"{x} ` + ` {y}"
    y5 = f"{x5} ` = ` {p}"

    candidates = [x1, x2, x3, x4, x5]
    np.random.shuffle(candidates)
    [s1, s2, s3, s4, s5] = candidates

    xy_dict = {x1: y1, x2: y2, x3: y3, x4: y4, x5: y5}

    z1 = xy_dict[s1]
    z2 = xy_dict[s2]
    z3 = xy_dict[s3]
    z4 = xy_dict[s4]
    z5 = xy_dict[s5]

    correct_idx1 = 0
    correct_idx2 = 0

    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == x2:
            correct_idx1 = idx
        if sdx == x5:
            correct_idx2 = idx

    if correct_idx1 > correct_idx2:
        tmp = correct_idx1
        correct_idx1 = correct_idx2
        correct_idx2 = tmp

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=answer_dict[correct_idx1], a2=answer_dict[correct_idx2])
    comment = comment.format(z1=z1, z2=z2, z3=z3, z4=z4, z5=z5)

    return stem, answer, comment




    # m_ = np.random.randint(11, 19)
    # p_ = np.random.randint(11, 19)
    #
    # while m_ == p_:
    #     p_ = np.random.randint(11, 19)
    #
    # m = round(m_ / 10, 1)
    # p = round(p_ / 10, 1)
    #
    # l_ = np.random.randint(2, 10)
    # n_ = np.random.randint(2, 10)
    #
    # while l_ == n_:
    #     n_ = np.random.randint(2, 10)
    #
    # o_ = np.random.randint(2, 10)
    #
    # while o_ == l_ or o_ == n_:
    #     o_ = np.random.randint(2, 10)
    #
    # l = round(l_ / 10, 1)
    # n = round(n_ / 10, 1)
    # o = round(o_ / 10, 1)
    #
    # b = round(np.random.randint(1, l_) / 10, 1)
    # c = round(l - b, 1)
    #
    # d = e = 1
    #
    # while d >= 1 or e >= 1:
    #     d = round(np.random.randint(1, m_) / 10, 1)
    #     e = round(m - d, 1)
    #
    # f = round(np.random.randint(1, n_) / 10, 1)
    # g = round(n - f, 1)
    #
    # h = round(np.random.randint(1, o_) / 10, 1)
    # i = round(o - h, 1)
    #
    # x = y = 1
    #
    # while x >= 1 or y >= 1:
    #     x = round(np.random.randint(1, p_) / 10, 1)
    #     y = round(p - x, 1)









































# 4-2-3-49
def decimaladdsub423_Stem_039():
    stem = "$$수식$$0$$/수식$$부터 $$수식$$9$$/수식$$까지의 자연수 중에서 □ 안에 들어갈 수 있는 수는 모두 몇 개인가요?\n$$표$$ $$수식$${x1} ` + ` {x2} ` &lt; `$$/수식$$□.$$수식$${x4}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n$$수식$${x1} ` + ` {x2} ` = ` {x3}$$/수식$$이므로 $$수식$${x3} ` &lt; `$$/수식$$□.$$수식$${x4}$$/수식$$입니다.\n" \
              "따라서 □ 안에 들어갈 수 있는 자연수는 $$수식$${x3}$$/수식$$의 일의 자리수{s1} 큰 숫자입니다.\n\n"


    x3 = 10

    while x3 >= 9:
        x = np.random.randint(11, 100)
        while x % 10 == 0:
            x = np.random.randint(11, 100)
        x1 = round(x / 10, 1)
        y = np.random.randint(11, 100)
        while y % 10 == 0 or x == y:
            y = np.random.randint(11, 100)
        x2 = round(y / 10, 1)
        x3 = round(x1 + x2, 1)

    x4 = np.random.randint(1, 10)

    if (x + y) % 10 > x4:
        s1 = "보다"
        a1 = 9 - int(x3)
    else:
        s1 = "와 같거나"
        a1 = 9 - int(x3) + 1


    stem = stem.format(x1=x1, x2=x2, x4=x4)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, s1=s1)

    return stem, answer, comment
































# 4-2-3-50
def decimaladdsub423_Stem_040():
    stem = "{who}네 집에서 {place1}까지의 거리는 $$수식$${x1} `` rm {{km}} `$$/수식$$이고, {place1}에서 {place2}까지의 거리는 $$수식$${x2} `` rm {{km}} `$$/수식$$입니다. {who}네 집에서 {place1}을 지나 {place2}까지의 거리는 몇 $$수식$$rm {{km}} `$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${a1} `` rm {{km}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${who}네 집 ~ {place1} ~ {place2}$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$${who}네 집 ~ {place1}$$수식$$RIGHT ) + LEFT ($$/수식$${place1} ~ {place2}$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {x1} ` + ` {x2} ` = ` {x3} LEFT ( rm {{km}} RIGHT )$$/수식$$\n\n"


    who = ['미주', '지수', '현지', '지아', '성호', '연주', '선화', '현주', '재희', "정우", "준기", "미나", "은하", "재호", "지희", "영래", "은배", "혜주", "석우", "희주"][np.random.randint(0, 20)]

    while True:
        place1 = ["서점", "학원", "도서관", "공원", "우체국", "미용실", "문구점", "편의점", "식당", "병원", "영화관", "박물관"][
            np.random.randint(0, 12)]
        place2 = ["서점", "학원", "도서관", "공원", "우체국", "미용실", "문구점", "편의점", "식당", "병원", "영화관", "박물관"][
            np.random.randint(0, 12)]
        if place1 != place2:
            break

    x = np.random.randint(1, 10)
    x1 = round(x / 10, 1)

    y = np.random.randint(1, 10)
    x2 = round(y / 10, 1)

    x3 = round(x1 + x2, 1)
    x3 = show_int(x3)

    stem = stem.format(x1=x1, x2=x2, who=who, place1=place1, place2=place2)
    answer = answer.format(a1=x3)
    comment = comment.format(x1=x1, x2=x2, x3=x3, who=who, place1=place1, place2=place2)

    return stem, answer, comment







































# 4-2-3-51
def decimaladdsub423_Stem_041():
    stem = "$$수식$${a}$$/수식$${j1} $$수식$${k}$$/수식$$개인 수와 $$수식$${y}$$/수식$$의 합은 얼마인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$${a}$$/수식$${j1} $$수식$${k}$$/수식$$개인 수는 $$수식$${x}$$/수식$$입니다.\n" \
              "$$수식$${x}$$/수식$${j2} $$수식$${y}$$/수식$$의 합은 $$수식$${x} ` + ` {y} ` = ` {c} $$/수식$$입니다.\n\n"


    # q = np.random.randint(1, 10)

    q = [1, 2, 5][np.random.randint(0, 3)]

    a = round(q / 10, 1)
    k = np.random.randint(10, 100)
    p = np.random.randint(10, 100)

    y = round(p / 10, 1)
    x = round(a * k, 1)

    y = show_int(y)
    x = show_int(x)

    c = round(x + y, 1)

    c = show_int(c)

    j1 = proc_jo(a, 0)
    j2 = proc_jo(x, 2)


    stem = stem.format(a=a, k=k, y=y, j1=j1)
    answer = answer.format(a1=c)
    comment = comment.format(a=a, j1=j1, k=k, x=x, j2=j2, y=y, c=c)

    return stem, answer, comment




































# 4-2-3-52
def decimaladdsub423_Stem_042():
    stem = "{who1}와 {who2}가 생각하는 소수의 합을 구해 보세요.\n$$표$${who1} : 내가 생각하는 수는 $$수식$${a}$$/수식$${j1} $$수식$${m}$$/수식$$개인 수야.\n{who2} : 내가 생각하는 소수 한 자리 수는 일의 자리 숫자가 $$수식$${b}$$/수식$${j2}고, 소수 첫째 자리 숫자가 $$수식$${c}$$/수식$$인 수야.$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT [$$/수식$${who1}$$수식$$RIGHT ] ```` {a}$$/수식$${j1} $$수식$${m}$$/수식$$개인 수는 $$수식$${x}$$/수식$$입니다.\n" \
              "$$수식$$LEFT [$$/수식$${who2}$$수식$$RIGHT ]$$/수식$$ 일의 자리 숫자가 $$수식$${b}$$/수식$${j2}고, 소수 첫째 자리 숫자가 $$수식$${c}$$/수식$$인 소수 한 자리 수는 $$수식$${y}$$/수식$$입니다.\n" \
              "따라서 두 사람이 생각하는 수의 합은\n" \
              "$$수식$${x} ` + ` {y} ` = ` {k}$$/수식$$입니다.\n\n"


    while True:
        who1 = ['미주', '지수', '현지', '지아', '성호', '연주', '선화', '현주', '재희', "정수", "준기", "미나", "은지", "재호", "지희", "영래", "은배", "솔미", "석우", "희주"][np.random.randint(0, 20)]
        who2 = ['미주', '지수', '현지', '지아', '성호', '연주', '선화', '현주', '재희', "정수", "준기", "미나", "은지", "재호", "지희", "영래", "은배", "솔미", "석우", "희주"][np.random.randint(0, 20)]
        if who1 != who2:
            break

    p = np.random.randint(1, 10)
    q = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    m = np.random.randint(1, 10)

    a = round(p / 10, 1)

    # c = round(q / 10, 1)
    c = q

    x = round(a * m, 1)

    x = show_int(x)

    # y = round(b + c, 1)
    y = round(b + (c / 10), 1)

    k = round(x + y, 1)

    k = show_int(k)

    j1 = proc_jo(p, 0)
    j2 = proc_jo(3)

    stem = stem.format(a=a, m=m, b=b, c=c, j1=j1, j2=j2, who1=who1, who2=who2)
    answer = answer.format(a1=k)
    comment = comment.format(j1=j1, j2=j2, b=b, c=c, y=y, a=a, m=m, x=x, k=k, who1=who1, who2=who2)

    return stem, answer, comment

































# 4-2-3-53
def decimaladdsub423_Stem_043():
    stem = "{who}는 딸기 과즙 $$수식$${x1} `` rm L `$$/수식$$와 바나나 과즙 $$수식$${x2} `` rm L `$$/수식$$를 섞어 딸기바나나 주스를 만들었습니다. {who}가 만든 딸기바나나 주스의 양은 모두 몇 $$수식$$rm L `$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${a1} `` rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$딸기바나나 주스의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$딸기 과즙의 양$$수식$$RIGHT ) ` + ` LEFT ($$/수식$$바나나 과즙의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {x1} ` + ` {x2} ` = ` {x3} LEFT ( rm L RIGHT )$$/수식$$\n\n"


    who = ["선미", '미주', '지수', '현지', '지아', '성호', '연주', '선화', '현주', '재희', "정수", "준기", "미나", "은지", "재호", "지희", "영래", "은배", "혜주", "석우", "희주"][np.random.randint(0, 21)]

    k = np.random.randint(1, 10)
    l = np.random.randint(1, 10)

    x1 = round(k / 10, 1)
    x2 = round(l / 10, 1)

    x3 = round(x1 + x2, 1)

    stem = stem.format(x1=x1, x2=x2, who=who)
    answer = answer.format(a1=x3)
    comment = comment.format(x1=x1, x2=x2, x3=x3)

    return stem, answer, comment







































# 4-2-3-54
def decimaladdsub423_Stem_044():
    stem = "㉠과 ㉡에 알맞은 수를 차례대로 구해 보세요.\n$$표$$$$수식$${x1} ` + ` {x2}$$/수식$$ → $$수식$${box1}$$/수식$$\n$$수식$${box1} ` + ` {x3} $$/수식$$ → $$수식$${box2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n㉠ $$수식$${a1}$$/수식$$, ㉡ $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${x1} ` + ` {x2} ` = ` {a1}$$/수식$$\n" \
              "㉡ $$수식$${a1} ` + ` {x3} ` = ` {a2}$$/수식$$\n\n"


    x = np.random.randint(100, 1000)
    while x % 10 == 0:
        x = np.random.randint(100, 1000)

    y = np.random.randint(100, 1000)
    while y % 10 == 0:
        y = np.random.randint(100, 1000)

    z = np.random.randint(100, 1000)
    while z % 10 == 0:
        z = np.random.randint(100, 1000)

    x1 = round(x / 100, 2)
    x2 = round(y / 100, 2)
    x3 = round(z / 100, 2)

    a1 = round(x1 + x2, 2)
    a2 = round(a1 + x3, 2)

    box1 = "㉠"
    box2 = "㉡"

    stem = stem.format(x1=x1, x2=x2, x3=x3, box1=box1, box2=box2)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(x1=x1, x2=x2, x3=x3, a1=a1, a2=a2)

    return stem, answer, comment

































# 4-2-3-55
def decimaladdsub423_Stem_045():
    stem = "두 수의 합을 구해 보세요.\n$$수식$${boxl}{x1}{boxr}$$/수식$$  $$수식$${boxl}{x2}{boxr}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$$ {x1} ` + ` {x2} ` = ` {x3}$$/수식$$\n\n"


    x = np.random.randint(100, 1000)

    while x % 10 == 0:
        x = np.random.randint(100, 1000)

    y = np.random.randint(100, 1000)

    while y % 10 == 0:
        y = np.random.randint(100, 1000)

    x1 = round(x / 100, 2)
    x2 = round(y / 100, 2)
    x3 = round(x1 + x2, 2)

    boxl = "["
    boxr = "]"

    stem = stem.format(boxl=boxl, boxr=boxr, x1=x1, x2=x2)
    answer = answer.format(a1=x3)
    comment = comment.format(x1=x1, x2=x2, x3=x3)

    return stem, answer, comment


































# 4-2-3-56
def decimaladdsub423_Stem_046():
    stem = "설명하는 수를 구해 보세요.\n$$표$$ $$수식$${x1}$$/수식$$보다 $$수식$${x2}$$/수식$$ 큰 수 $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$$ {x1} ` + ` {x2} ` = ` {x3}$$/수식$$\n\n"


    m = np.random.randint(1, 10)
    n = np.random.randint(100, 1000)

    while n % 10 == 0:
        n = np.random.randint(100, 1000)

    x1 = round(m / 10, 1)
    x2 = round(n / 100, 2)

    x3 = round(x1 + x2, 2)

    stem = stem.format(x1=x1, x2=x2)
    answer = answer.format(a1=x3)
    comment = comment.format(x1=x1, x2=x2, x3=x3)

    return stem, answer, comment





































# 4-2-3-57
def decimaladdsub423_Stem_047():
    stem = "㉠과 ㉡에 알맞은 수를 차례대로 구해 보세요.\n$$표$$ $$수식$${x1} ` + ` {x2}$$/수식$$ → ㉠\n㉠ $$수식$$+ ` {x3}$$/수식$$ → ㉡ $$/표$$\n"
    answer = "(정답)\n㉠ $$수식$${a1}$$/수식$$, ㉡ $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n$$수식$$ {x1} ` + ` {x2} ` = ` {a1}$$/수식$$,\n" \
              "$$수식$$ {a1} ` + ` {x3} ` = ` {a2}$$/수식$$\n\n"


    m = np.random.randint(100, 1000)

    while m % 10 == 0:
        m = np.random.randint(100, 1000)

    n = np.random.randint(100, 1000)

    while n % 10 == 0:
        n = np.random.randint(100, 1000)

    p = np.random.randint(100, 1000)

    while p % 10 == 0:
        p = np.random.randint(100, 1000)

    x1 = round(m / 100, 2)
    x2 = round(n / 100, 2)
    x3 = round(p / 100, 2)

    a1 = round(x1 + x2, 2)
    a2 = round(a1 + x3, 2)

    stem = stem.format(x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(x1=x1, x2=x2, x3=x3, a1=a1, a2=a2)

    return stem, answer, comment




































# 4-2-3-59
def decimaladdsub423_Stem_048():
    stem = "가장 큰 수와 가장 작은 수의 합을 구해 보세요.\n$$표$$ $$수식$${x1}$$/수식$$   $$수식$${x2}$$/수식$$   $$수식$${x3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$$ {y1} ` &gt; ` {y2} ` &gt; ` {y3}$$/수식$$이므로 가장 큰 수는 $$수식$${y1}$$/수식$$이고 가장 작은 수는 $$수식$${y3}$$/수식$$입니다.\n" \
              "따라서 가장 큰 수와 가장 작은 수의 합은\n" \
              "$$수식$$ {y1} ` + ` {y3} ` = ` {a1}$$/수식$$\n\n"


    # m = np.random.randint(100, 1000)
    # n = np.random.randint(100, 1000)
    #
    # while m == n:
    #     n = np.random.randint(100, 1000)
    #
    # p = np.random.randint(100, 1000)
    #
    # while m == p or n == p:
    #     p = np.random.randint(100, 1000)

    while True:
        m = np.random.randint(10, 100) * 10 + np.random.randint(1, 10)
        n = np.random.randint(10, 100) * 10 + np.random.randint(1, 10)
        p = np.random.randint(10, 100) * 10 + np.random.randint(1, 10)

        if m != n and m != p and n != p:
            break


    num_list = [m, n, p]
    num_list.sort(reverse=True)

    y1 = round(num_list[0] / 100, 2)
    y2 = round(num_list[1] / 100, 2)
    y3 = round(num_list[2] / 100, 2)

    a1 = round(y1 + y3, 2)

    a1 = show_int(a1)


    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [x1, x2, x3] = candidates


    stem = stem.format(x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=a1)
    comment = comment.format(y1=y1, y2=y2, y3=y3, a1=a1)

    return stem, answer, comment













































# 4-2-3-60
def decimaladdsub423_Stem_049():
    stem = "다음 중 계산 결과가 $$수식$${m}$$/수식$$인 것을 찾아보세요.\n① $$수식$${s1}$$/수식$$\n② $$수식$${s2}$$/수식$$\n③ $$수식$${s3}$$/수식$$\n④ $$수식$${s4}$$/수식$$\n⑤ $$수식$${s5}$$/수식$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "① $$수식$${z1}$$/수식$$, " \
              "② $$수식$${z2}$$/수식$$,\n" \
              "③ $$수식$${z3}$$/수식$$, " \
              "④ $$수식$${z4}$$/수식$$,\n" \
              "⑤ $$수식$${z5}$$/수식$$\n\n"



    while True:
        a_source = np.random.randint(11, 100)
        b_source = np.random.randint(11, 100)
        c_source = np.random.randint(11, 100)
        d_source = np.random.randint(11, 100)
        e_source = np.random.randint(11, 100)
        f_source = np.random.randint(11, 100)
        g_source = np.random.randint(11, 100)
        h_source = np.random.randint(11, 100)
        j_source = np.random.randint(11, 100)
        k_source = np.random.randint(11, 100)

        a = round(a_source / 100, 2)
        b = round(b_source / 100, 2)
        l = round(a + b, 2)

        c = round(c_source / 100, 2)
        d = round(d_source / 100, 2)
        m = round(c + d, 2)

        e = round(e_source / 100, 2)
        f = round(f_source / 100, 2)
        n = round(e + f, 2)

        g = round(g_source / 100, 2)
        h = round(h_source / 100, 2)
        o = round(g + h, 2)

        j = round(j_source / 100, 2)
        k = round(k_source / 100, 2)
        p = round(j + k, 2)

        double_check_point1 = 0
        double_check_list1 = [a_source, c_source, e_source, g_source, j_source]
        double_check_list1.sort()
        for i_dx in range(4):
            if double_check_list1[i_dx] == double_check_list1[i_dx + 1]:
                double_check_point1 = 1
                break

        if double_check_point1 == 1:
            continue

        double_check_list2 = [l, n, o, p]
        if double_check_list2.count(m) > 0:
            continue

        l = show_int(l)
        m = show_int(m)
        n = show_int(n)
        o = show_int(o)
        p = show_int(p)

        break



    x1 = f"{a} ` + ` {b}"
    y1 = f"{x1} ` = ` {l}"

    x2 = f"{c} ` + ` {d}"
    y2 = f"{x2} ` = ` {m}"

    x3 = f"{e} ` + ` {f}"
    y3 = f"{x3} ` = ` {n}"

    x4 = f"{g} ` + ` {h}"
    y4 = f"{x4} ` = ` {o}"

    x5 = f"{j} ` + ` {k}"
    y5 = f"{x5} ` = ` {p}"

    candidates = [x1, x2, x3, x4, x5]
    np.random.shuffle(candidates)
    [s1, s2, s3, s4, s5] = candidates

    xy_dict = {x1: y1, x2: y2, x3: y3, x4: y4, x5: y5}

    z1 = xy_dict[s1]
    z2 = xy_dict[s2]
    z3 = xy_dict[s3]
    z4 = xy_dict[s4]
    z5 = xy_dict[s5]

    correct_idx = 0

    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == x2:
            correct_idx = idx
            break


    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, m=m)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(z1=z1, z2=z2, z3=z3, z4=z4, z5=z5, a1=answer_dict[correct_idx])

    return stem, answer, comment





    # m = np.random.randint(12, 100)
    #
    # while m % 10 == 0:
    #     m = np.random.randint(12, 100)
    #
    # a = round(np.random.randint(11, 100) / 100, 2)
    # b = round(np.random.randint(11, 100) / 100, 2)
    #
    # while a + b == round(m / 100, 2):
    #     b = round(np.random.randint(11, 100) / 100, 2)
    #
    # l = round(a + b, 2)
    #
    #
    # e = round(np.random.randint(11, 100) / 100, 2)
    # f = round(np.random.randint(11, 100) / 100, 2)
    #
    # while e + f == round(m / 100, 2):
    #     f = round(np.random.randint(11, 100) / 100, 2)
    #
    # n = round(e + f, 2)
    #
    #
    # g = round(np.random.randint(11, 100) / 100, 2)
    # h = round(np.random.randint(11, 100) / 100, 2)
    #
    # while g + h == round(m / 100, 2):
    #     h = round(np.random.randint(11, 100) / 100, 2)
    #
    # o = round(g + h, 2)
    #
    #
    # j = round(np.random.randint(11, 100) / 100, 2)
    # k = round(np.random.randint(11, 100) / 100, 2)
    #
    # while k + j == round(m / 100, 2):
    #     k = round(np.random.randint(11, 100) / 100, 2)
    #
    # p = round(j + k, 2)
    #
    #
    # c = round(np.random.randint(11, m) / 100, 2)
    #
    # d = round(m / 100 - c, 2)
    # m = round(m / 100, 2)
















































# 4-2-3-62
def decimaladdsub423_Stem_050():
    stem = "{who}는 {family}와 함께 농장에서 {fruit}를 땄습니다. {fruit}를 {who}는 $$수식$${x1} ``rm kg`$$/수식$$땄고, {family}는 {who}보다 $$수식$${x2} ``rm kg`$$/수식$$ 더 많이 따셨습니다. {family}께서 따신 {fruit}는 몇 $$수식$$rm kg`$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${a1} `` rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${family}께서 따신 {fruit}의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$${who}가 딴 {fruit}의 양$$수식$$RIGHT ) ` + ` {x2}$$/수식$$\n" \
              "$$수식$$= ` {x1} ` + ` {x2} ` = ` {x3} LEFT ( rm kg RIGHT )$$/수식$$\n\n"


    who = ["지우", "유지", "대호", "은하", "보아", "중기", "석재", "대희", "나나", "종국이", "가영이"][np.random.randint(0, 11)]
    family = ["아버지", "할아버지", "할머니", "어머니"][np.random.randint(0, 4)]
    fruit = ["딸기", "배", "사과", "복숭아", "참외", "자두", "포도"][np.random.randint(0, 7)]

    m = np.random.randint(100, 1000)

    while m % 10 == 0:
        m = np.random.randint(100, 1000)

    n = np.random.randint(100, 1000)

    while n % 10 == 0:
        n = np.random.randint(100, 1000)

    x1 = round(m / 100, 2)
    x2 = round(n / 100, 2)

    x3 = round(x1 + x2, 2)

    stem = stem.format(x1=x1, x2=x2, who=who, family=family, fruit=fruit)
    answer = answer.format(a1=x3)
    comment = comment.format(x1=x1, x2=x2, x3=x3, who=who, family=family, fruit=fruit)

    return stem, answer, comment






































# 4-2-3-64
def decimaladdsub423_Stem_051():
    stem = "설명하는 수는 얼마인가요?\n$$표$$ $$수식$${a}$$/수식$${j1} $$수식$${x}$$/수식$$개, $$수식$${b}$$/수식$${j1} $$수식$${y}$$/수식$$개, $$수식$${c}$$/수식$${j1} $$수식$${z}$$/수식$$개인 수보다 $$수식$${p}$$/수식$$ 큰 수 $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a}$$/수식$${j1} $$수식$${x}$$/수식$$개, " \
              "$$수식$${b}$$/수식$${j1} $$수식$${y}$$/수식$$개, " \
              "$$수식$${c}$$/수식$${j1} $$수식$${z}$$/수식$$개인 수는 $$수식$${u}$$/수식$$입니다.\n" \
              "따라서 $$수식$${u}$$/수식$$보다 $$수식$${p}$$/수식$$ 큰 수는 $$수식$${u} ` + ` {p} ` = ` {k}$$/수식$$입니다.\n\n"


    # a = np.random.randint(1, 10)
    a = [1, 2, 5][np.random.randint(0, 3)]

    b = round(a / 10, 1)
    c = round(a / 100, 2)

    x = np.random.randint(1, 10)
    y = np.random.randint(1, 10)
    z = np.random.randint(1, 10)

    u = round(a * x + b * y + c * z, 2)

    m = np.random.randint(11, 100)

    while m % 10 == 0:
        m = np.random.randint(11, 100)

    p = round(m / 10, 1)

    k = round(u + p, 2)
    k = show_int(k)

    j1 = proc_jo(a, 0)


    stem = stem.format(a=a, x=x, b=b, y=y, p=p, c=c, z=z, j1=j1)
    answer = answer.format(a1=k)
    comment = comment.format(a=a, x=x, b=b, y=y, c=c, z=z, u=u, p=p, k=k, j1=j1)

    return stem, answer, comment




































# 4-2-3-65
def decimaladdsub423_Stem_052():
    stem = "$$수식$$500$$/수식$$원짜리 동전 $$수식$${x}$$/수식$$개의 무게는 $$수식$${A} rm g$$/수식$$이고, $$수식$$100$$/수식$$원짜리 동전 $$수식$${y}$$/수식$$개의 무게는 $$수식$${B} rm g$$/수식$$입니다. 모든 동전의 무게의 합은 몇 $$수식$$rm g$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${C} `` rm g$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$모든 동전의 무게의 합$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ( ` 500$$/수식$$원짜리 동전 $$수식$${x}$$/수식$$개의 무게$$수식$$RIGHT ) ` + ` LEFT ( ` 100$$/수식$$원짜리 동전 $$수식$${y}$$/수식$$개의 무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {A} ` + ` {B} ` = ` {C} LEFT ( rm g RIGHT )$$/수식$$\n\n"



    [x, y] = random.sample([1, 2, 3], 2)

    A = round(x * 7.7, 1)
    B = round(y * 5.42, 2)
    C = round(A + B, 2)


    stem = stem.format(x=x, A=A, y=y, B=B)
    answer = answer.format(C=C)
    comment = comment.format(x=x, y=y, A=A, B=B, C=C)

    return stem, answer, comment



    # stem = "$$수식$$100$$/수식$$원짜리 동전의 무게는 $$수식$${x1} `` rm g `$$/수식$$이고, $$수식$$500$$/수식$$원짜리 동전의 무게는 $$수식$${x2} `` rm g `$$/수식$$입니다. 두 동전의 무게의 합은 몇 $$수식$$rm g `$$/수식$$인가요?\n"
    # answer = "(정답)\n$$수식$${a1} `` rm g$$/수식$$\n"
    # comment = "(해설)\n" \
    #           "$$수식$$LEFT ($$/수식$$두 동전의 무게의 합$$수식$$RIGHT )$$/수식$$\n" \
    #           "$$수식$$= ` LEFT ( ` 100$$/수식$$원짜리 동전의 무게$$수식$$RIGHT ) + ` LEFT ( ` 500$$/수식$$원짜리 동전의 무게$$수식$$RIGHT )$$/수식$$\n" \
    #           "$$수식$$= ` {x1} ` + ` {x2} ` = ` {a1} LEFT ( rm g RIGHT )$$/수식$$\n\n"


    # while True:
    #     m = np.random.randint(10, 100)
    #
    #     while m % 10 == 0:
    #         m = np.random.randint(10, 100)
    #
    #     n = np.random.randint(100, 1000)
    #
    #     while n % 10 == 0:
    #         n = np.random.randint(100, 1000)
    #
    #     x1 = round(m / 100, 1)
    #     x2 = round(n / 100, 2)
    #
    #     if x1 < x2:
    #         break
    #
    # a1 = round(x1 + x2, 2)
    #
    # stem = stem.format(x1=x1, x2=x2)
    # answer = answer.format(a1=a1)
    # comment = comment.format(x1=x1, x2=x2, a1=a1)
    #
    # return stem, answer, comment

































# 4-2-3-66
def decimaladdsub423_Stem_053():
    stem = "계산 결과를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${x1} ` - ` {x2} $$/수식$$ ○ $$수식$${x3} ` - ` {x4}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ {x1} ` - ` {x2} ` = ` {x5}$$/수식$$, $$수식$${x3} ` - ` {x4} ` = ` {x6}$$/수식$$\n" \
              "따라서 $$수식$${x5} ` {a1} ` {x6}$$/수식$$이므로 $$수식$${x1} ` - ` {x2} ` {a1} ` {x3} ` - ` {x4}$$/수식$$입니다.\n\n"



    m = np.random.randint(10, 100)

    while m % 10 == 0:
        m = np.random.randint(10, 100)

    n = np.random.randint(10, 100)

    while n % 10 == 0 or m == n:
        n = np.random.randint(10, 100)

    p = np.random.randint(10, 100)

    while p % 10 == 0:
        p = np.random.randint(10, 100)

    q = np.random.randint(10, 100)

    while q % 10 == 0 or p == q:
        q = np.random.randint(10, 100)

    if m > n:
        x1 = round(m / 10, 1)
        x2 = round(n / 10, 1)
    else:
        x1 = round(n / 10, 1)
        x2 = round(m / 10, 1)

    x5 = round(x1 - x2, 1)

    if p > q:
        x3 = round(p / 10, 1)
        x4 = round(q / 10, 1)
    else:
        x3 = round(q / 10, 1)
        x4 = round(p / 10, 1)

    x6 = round(x3 - x4, 1)


    if x5 > x6:
        a1 = "&gt;"
    elif x5 < x6:
        a1 = "&lt;"
    else:
        a1 = "="


    x5 = show_int(x5)
    x6 = show_int(x6)



    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, a1=a1)

    return stem, answer, comment







































# 4-2-3-67
def decimaladdsub423_Stem_054():
    stem = "계산 결과가 다른 하나는 어느 것인가요?\n① $$수식$${s1}$$/수식$$\n② $$수식$${s2}$$/수식$$\n③ $$수식$${s3}$$/수식$$\n④ $$수식$${s4}$$/수식$$\n⑤ $$수식$${s5}$$/수식$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "① $$수식$${z1}$$/수식$$,  " \
              "② $$수식$${z2}$$/수식$$,\n" \
              "③ $$수식$${z3}$$/수식$$,  " \
              "④ $$수식$${z4}$$/수식$$,\n" \
              "⑤ $$수식$${z5}$$/수식$$\n" \
              "따라서 계산 결과가 다른 하나는 {a1}입니다.\n\n"

    k = np.random.randint(15, 100)

    while k % 10 == 0:
        k = np.random.randint(15, 100)

    l = np.random.randint(15, 100)

    while l % 10 == 0 or l == k or abs(k-l)>20:
        l = np.random.randint(15, 100)

    a = round(np.random.randint(10, k) / 10, 1)
    c = round(np.random.randint(10, k) / 10, 1)

    while a == c:
        c = round(np.random.randint(10, k) / 10, 1)

    e = round(np.random.randint(10, l) / 10, 1)
    g = round(np.random.randint(10, k) / 10, 1)

    while a == g or c == g:
        g = round(np.random.randint(10, k) / 10, 1)

    i = round(np.random.randint(10, k) / 10, 1)

    while i == a or i == c or i == g:
        i = round(np.random.randint(10, k) / 10, 1)


    k = round(k / 10, 1)
    l = round(l / 10, 1)

    b = round(k + a, 1)

    if a < b:
        tmp = a
        a = b
        b = tmp

    d = round(k + c, 1)
    if c < d:
        tmp = c
        c = d
        d = tmp

    f = round(l + e, 1)
    if e < f:
        tmp = e
        e = f
        f = tmp

    h = round(k + g, 1)
    if g < h:
        tmp = g
        g = h
        h = tmp

    j = round(k + i, 1)
    if i < j:
        tmp = i
        i = j
        j = tmp

    x1 = f"{a} ` - ` {b}"
    y1 = f"{x1} ` = ` {k}"
    x2 = f"{c} ` - ` {d}"
    y2 = f"{x2} ` = ` {k}"

    x3 = f"{e} ` - ` {f}"
    y3 = f"{x3} ` = ` {l}"
    x4 = f"{g} ` - ` {h}"
    y4 = f"{x4} ` = ` {k}"

    x5 = f"{i} ` - ` {j}"
    y5 = f"{x5} ` = ` {k}"

    candidates = [x1, x2, x3, x4, x5]
    np.random.shuffle(candidates)
    [s1, s2, s3, s4, s5] = candidates

    xy_dict = {x1: y1, x2: y2, x3: y3, x4: y4, x5: y5}

    z1 = xy_dict[s1]
    z2 = xy_dict[s2]
    z3 = xy_dict[s3]
    z4 = xy_dict[s4]
    z5 = xy_dict[s5]

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == x3:
            correct_idx = idx
            break

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(z1=z1, z2=z2, z3=z3, z4=z4, z5=z5, a1=answer_dict[correct_idx])

    return stem, answer, comment





































# 4-2-3-68
def decimaladdsub423_Stem_055():
    stem = "㉠에 알맞은 수를 구해 보세요.\n$$수식$${x1}$$/수식$$ → $$수식$$LEFT ( ` - ` {x2} ` RIGHT ) $$/수식$$ → $$수식$${box1}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n$$수식$$ {x1} ` - ` {x2} ` = ` {a1} $$/수식$$\n\n"


    m = np.random.randint(15, 100)

    while m % 10 == 0:
        m = np.random.randint(15, 100)

    n = np.random.randint(10, m)

    while n % 10 == 0:
        n = np.random.randint(10, m)

    x1 = round(m / 10, 1)
    x2 = round(n / 10, 1)

    a1 = round(x1 - x2, 1)

    box1 = "box{㉠````````````````````}"

    stem = stem.format(x1=x1, x2=x2, box1=box1)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, a1=a1)

    return stem, answer, comment








































# 4-2-3-69
def decimaladdsub423_Stem_056():
    stem = "가장 큰 수와 가장 작은 수의 차를 구해 보세요.\n$$표$$ $$수식$${x1}$$/수식$$   $$수식$${x2}$$/수식$$   $$수식$${x3}$$/수식$$   $$수식$${x4}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ {y1} ` &gt; ` {y2} ` &gt; ` {y3} ` &gt; ` {y4}$$/수식$$이므로 가장 큰 수는 $$수식$${y1}$$/수식$$이고 " \
              "가장 작은 수는 $$수식$${y4}$$/수식$$입니다.\n" \
              "따라서 가장 큰 수와 가장 작은 수의 차이는 $$수식$${y1} ` - ` {y4} ` = ` {a1}$$/수식$$입니다.\n\n"


    p = np.random.randint(10, 100)

    while p % 10 == 0:
        p = np.random.randint(10, 100)

    q = np.random.randint(10, 100)

    while q % 10 == 0 or q == p:
        q = np.random.randint(10, 100)

    r = np.random.randint(10, 100)

    while r % 10 == 0 or r == p or r == q:
        r = np.random.randint(10, 100)

    s = np.random.randint(10, 100)

    while s % 10 == 0 or s == p or s == q or s == r:
        s = np.random.randint(10, 100)

    num_list = [p, q, r, s]
    num_list.sort(reverse=True)

    y1 = round(num_list[0] / 10, 1)
    y2 = round(num_list[1] / 10, 1)
    y3 = round(num_list[2] / 10, 1)
    y4 = round(num_list[3] / 10, 1)

    a1 = round(y1 - y4, 1)

    candidates = [y1, y2, y3, y4]
    np.random.shuffle(candidates)
    [x1, x2, x3, x4] = candidates

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4)
    answer = answer.format(a1=a1)
    comment = comment.format(y1=y1, y2=y2, y3=y3, y4=y4, a1=a1)

    return stem, answer, comment



































# 4-2-3-71
def decimaladdsub423_Stem_057():
    stem = "다음 중 계산 결과가 $$수식$${l}$$/수식$$인 것은 어느 것인가요?\n① $$수식$${s1}$$/수식$$\n② $$수식$${s2}$$/수식$$\n③ $$수식$${s3}$$/수식$$\n④ $$수식$${s4}$$/수식$$\n⑤ $$수식$${s5}$$/수식$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "① $$수식$${z1}$$/수식$$,  " \
              "② $$수식$${z2}$$/수식$$,\n" \
              "③ $$수식$${z3}$$/수식$$,  " \
              "④ $$수식$${z4}$$/수식$$,\n" \
              "⑤ $$수식$${z5}$$/수식$$\n" \
              "따라서 계산 결과가 $$수식$${l}$$/수식$$인 것은 {a1}입니다.\n\n"


    k = np.random.randint(15, 100)
    while k % 10 == 0:
        k = np.random.randint(15, 100)

    l = np.random.randint(15, 100)
    while l % 10 == 0 or l == k:
        l = np.random.randint(15, 100)

    m = np.random.randint(15, 100)
    while m % 10 == 0 or m == k or m == l:
        m = np.random.randint(15, 100)

    n = np.random.randint(15, 100)
    while n % 10 == 0 or n == k or n == l or n == m:
        n = np.random.randint(15, 100)

    o = np.random.randint(15, 100)
    while o % 10 == 0 or o == k or o == l or o == m or o == n:
        o = np.random.randint(15, 100)

    a = round(np.random.randint(10, k) / 10, 1)
    c = round(np.random.randint(10, m) / 10, 1)
    e = round(np.random.randint(10, l) / 10, 1)

    g = round(np.random.randint(10, n) / 10, 1)
    i = round(np.random.randint(10, o) / 10, 1)

    k = round(k / 10, 1)
    l = round(l / 10, 1)
    m = round(m / 10, 1)

    n = round(n / 10, 1)
    o = round(o / 10, 1)

    b = round(k + a, 1)
    if a < b:
        tmp = a
        a = b
        b = tmp

    d = round(m + c, 1)
    if c < d:
        tmp = c
        c = d
        d = tmp

    f = round(l + e, 1)
    if e < f:
        tmp = e
        e = f
        f = tmp

    h = round(n + g, 1)
    if g < h:
        tmp = g
        g = h
        h = tmp

    j = round(o + i, 1)
    if i < j:
        tmp = i
        i = j
        j = tmp

    x1 = f"{a} ` - ` {b}"
    y1 = f"{x1} ` = ` {k}"
    x2 = f"{c} ` - ` {d}"
    y2 = f"{x2} ` = ` {m}"

    x3 = f"{e} ` - ` {f}"
    y3 = f"{x3} ` = ` {l}"
    x4 = f"{g} ` - ` {h}"
    y4 = f"{x4} ` = ` {n}"

    x5 = f"{i} ` - ` {j}"
    y5 = f"{x5} ` = ` {o}"

    candidates = [x1, x2, x3, x4, x5]
    np.random.shuffle(candidates)
    [s1, s2, s3, s4, s5] = candidates

    xy_dict = {x1: y1, x2: y2, x3: y3, x4: y4, x5: y5}
    z1 = xy_dict[s1]
    z2 = xy_dict[s2]
    z3 = xy_dict[s3]
    z4 = xy_dict[s4]
    z5 = xy_dict[s5]

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == x3:
            correct_idx = idx
            break

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, l=l)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(z1=z1, z2=z2, z3=z3, z4=z4, z5=z5, l=l, a1=answer_dict[correct_idx])

    return stem, answer, comment







































# 4-2-3-72
def decimaladdsub423_Stem_058():
    stem = "그릇에 쌀, 쇠구슬, 플라스틱 구슬을 담아 무게를 재었더니 $$수식$${x1} `` rm kg `$$/수식$$이었습니다. 자석을 이용하여 쇠구슬만을 분리하였습니다. 쇠구슬을 모두 뺀 다음 다시 무게를 재었더니 $$수식$${x2} `` rm kg `$$/수식$$이 되었습니다. 쇠구슬만의 무게는 몇 인가요?\n"
    answer = "(정답)\n$$수식$${a1} `` rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$쇠구슬만의 무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$쌀, 쇠구슬, 플라스틱 구슬의 무게$$수식$$RIGHT ) ` - ` LEFT ($$/수식$$쇠구슬을 뺀 무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {x1} ` - ` {x2} ` = ` {a1} LEFT ( rm kg RIGHT )$$/수식$$\n\n"



    m = np.random.randint(11, 20)
    n = np.random.randint(1, 10)

    x1 = round(m / 10, 1)
    x2 = round(n / 10, 1)

    a1 = round(x1 - x2, 1)
    a1 = show_int(a1)


    stem = stem.format(x1=x1, x2=x2)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, a1=a1)

    return stem, answer, comment



    # m = np.random.randint(12, 100)
    #
    # while m % 10 == 0:
    #     m = np.random.randint(12, 100)
    #
    # n = np.random.randint(10, m)
    #
    # while n % 10 == 0:
    #     n = np.random.randint(10, m)

































# 4-2-3-73
def decimaladdsub423_Stem_059():
    stem = "{wh1}{j1}네 아버지께서 사용하시는 태블릿 PC에 케이스를 씌워서 무게를 재어 보니 $$수식$${x1} `` rm kg `$$/수식$$이었습니다. 케이스의 무게가 $$수식$${x2} `` rm kg$$/수식$$이라면 태블릿 PC의 무게는 몇 $$수식$$rm kg `$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${a1} `` rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$태블릿 PC의 무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$케이스를 씌운 태블릿 PC의 무게$$수식$$RIGHT ) ` - ` LEFT ($$/수식$$케이스의 무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {x1} ` - ` {x2} ` = ` {a1} LEFT ( rm kg RIGHT )$$/수식$$\n\n"


    wh1 = ['지우', '윤주', '윤성', '지성', '사랑', '소정', '수현', '소현', '동훈'][np.random.randint(0, 9)]
    j1 = proc_jo(wh1, 3)

    while True:
        m = np.random.randint(12, 100)

        while m % 10 == 0:
            m = np.random.randint(12, 100)

        n = np.random.randint(10, m)

        while n % 10 == 0:
            n = np.random.randint(10, m)

        if (m / 2) > n:
            break

    x1 = round(m / 10, 1)
    x2 = round(n / 10, 1)

    a1 = round(x1 - x2, 1)

    stem = stem.format(wh1=wh1, j1=j1, x1=x1, x2=x2)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, a1=a1)

    return stem, answer, comment






































# 4-2-3-74
def decimaladdsub423_Stem_060():
    stem = "{wh1}{j1} {wh2}{j2} 종이비행기를 날리고 있습니다. {wh1}의 종이비행기는 $$수식$${x1} `` rm m `$$/수식$$를 날아가고, {wh2}의 종이비행기는 $$수식$${x2} `` rm m `$$/수식$$를 날아갔습니다. 누구의 종이비행기가 몇 더 멀리 날아갔나요?\n$$수식$${box1}$$/수식$$ 의 종이비행기가 $$수식$${box2}$$/수식$$$$수식$$`` rm m `$$/수식$$ 더 멀리 날아갔습니다.\n"
    answer = "(정답)\n{a1}, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ {x1} ` {k} ` {x2}$$/수식$$이므로 {a1}의 종이비행기가 $$수식$${z1} ` - ` {z2} ` = ` {a2} LEFT ( rm m RIGHT )$$/수식$$ 더 멀리 날아갔습니다.\n\n"


    wh1 = ['지우', '윤주', '기후', '지후', '준서', '용우', '재호', '은아', '민지', '태화', '희수', '권기', '현도'][np.random.randint(0, 13)]
    wh2 = ['지우', '윤주', '기후', '지후', '준서', '용우', '재호', '은아', '민지', '태화', '희수', '권기', '현도'][np.random.randint(0, 13)]

    while wh1 == wh2:
        wh2 = ['지우', '윤주', '기후', '지후', '준서', '용우', '재호', '은아', '민지', '태화', '희수', '권기', '현도'][np.random.randint(0, 13)]

    j1 = proc_jo(wh1, 2)
    j2 = proc_jo(wh2, -1)

    m = np.random.randint(10, 100)
    while m % 10 == 0:
        m = np.random.randint(10, 100)

    n = np.random.randint(10, 100)
    while n % 10 == 0:
        n = np.random.randint(10, 100)

    x1 = round(m / 10, 1)
    x2 = round(n / 10, 1)

    if x1 > x2:
        z1 = x1
        z2 = x2
        a1 = wh1
        a2 = round(x1 - x2, 1)
        k = "&gt;"
    else:
        z1 = x2
        z2 = x1
        a1 = wh2
        a2 = round(x2 - x1, 1)
        k = "&lt;"

    box1 = "box{　　　}"
    box2 = "box{　　　}"

    stem = stem.format(wh1=wh1, wh2=wh2, j1=j1, j2=j2, x1=x1, x2=x2, box1=box1, box2=box2)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(x1=x1, x2=x2, z1=z1, z2=z2, k=k, a1=a1, a2=a2)

    return stem, answer, comment





































# 4-2-3-76
def decimaladdsub423_Stem_061():
    stem = "다음 중 계산 결과가 가장 작은 것은 어느 것인가요?\n① $$수식$${s1}$$/수식$$\n② $$수식$${s2}$$/수식$$\n③ $$수식$${s3}$$/수식$$\n④ $$수식$${s4}$$/수식$$\n⑤ $$수식$${s5}$$/수식$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "① $$수식$${z1}$$/수식$$\n" \
              "② $$수식$${z2}$$/수식$$\n" \
              "③ $$수식$${z3}$$/수식$$\n" \
              "④ $$수식$${z4}$$/수식$$\n" \
              "⑤ $$수식$${z5}$$/수식$$\n" \
              "따라서 계산 결과가 $$수식$${o} ` &gt; ` {n} ` &gt; ` {m} ` &gt; ` {l} ` &gt; ` {k}$$/수식$$이므로 계산 결과가 가장 작은 것은 {a1}입니다.\n\n"





    while True:
        k = np.random.randint(1, 10000)

        temp_list = random.sample(list(range(200)), 4)
        temp_list.sort()
        small_est, small_er, big_er, big_est = temp_list

        o = big_est + k
        n = big_er + k
        m = small_er + k
        l = small_est + k

        if o >= 10000:
            continue

        b = np.random.randint(101, 10000)
        a = k + b

        if a>= 10000 or b % 10 == 0 or a % 10 == 0:
            continue

        d = np.random.randint(101, 10000)
        c = m + d

        if c >= 10000 or d % 10 == 0 or c % 10 == 0:
            continue

        f = np.random.randint(101, 10000)
        e = l + f

        if e >= 10000 or f % 10 == 0 or e % 10 == 0:
            continue

        h = np.random.randint(101, 10000)
        g = n + h

        if g >= 10000 or h % 10 == 0 or g % 10 == 0:
            continue

        j = np.random.randint(101, 10000)
        i = o + j

        if i >= 10000 or j % 10 == 0 or i % 10 == 0:
            continue

        break

    a = round(a / 100, 2)
    b = round(b / 100, 2)
    k = round(k / 100, 2)
    k = show_int(k)

    c = round(c / 100, 2)
    d = round(d / 100, 2)
    m = round(m / 100, 2)
    m = show_int(m)

    e = round(e / 100, 2)
    f = round(f / 100, 2)
    l = round(l / 100, 2)
    l = show_int(l)

    g = round(g / 100, 2)
    h = round(h / 100, 2)
    n = round(n / 100, 2)
    n = show_int(n)

    i = round(i / 100, 2)
    j = round(j / 100, 2)
    o = round(o / 100, 2)
    o = show_int(o)


    # 5등
    x1 = f"{a} ` - ` {b}"
    y1 = f"{x1} ` = ` {k}"

    # 3등
    x2 = f"{c} ` - ` {d}"
    y2 = f"{x2} ` = ` {m}"

    # 4등
    x3 = f"{e} ` - ` {f}"
    y3 = f"{x3} ` = ` {l}"

    # 2등
    x4 = f"{g} ` - ` {h}"
    y4 = f"{x4} ` = ` {n}"

    # 1등
    x5 = f"{i} ` -` {j}"
    y5 = f"{x5} ` = ` {o}"

    candidates = [x1, x2, x3, x4, x5]
    np.random.shuffle(candidates)
    [s1, s2, s3, s4, s5] = candidates

    xy_dict = {x1: y1, x2: y2, x3: y3, x4: y4, x5: y5}
    z1 = xy_dict[s1]
    z2 = xy_dict[s2]
    z3 = xy_dict[s3]
    z4 = xy_dict[s4]
    z5 = xy_dict[s5]

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == x1:
            correct_idx = idx
            break


    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(k=k, l=l, m=m, n=n, o=o, z1=z1, z2=z2, z3=z3, z4=z4, z5=z5, a1=answer_dict[correct_idx])

    return stem, answer, comment






    # k = np.random.randint(15, 100)
    # while k % 10 == 0:
    #     k = np.random.randint(15, 100)
    #
    # l = np.random.randint(15, 100)
    # while l % 10 == 0 or l == k:
    #     l = np.random.randint(15, 100)
    #
    # m = np.random.randint(15, 100)
    # while m % 10 == 0 or m == k or m == l:
    #     m = np.random.randint(15, 100)
    #
    # n = np.random.randint(15, 100)
    # while n % 10 == 0 or n == k or n == l or n == m:
    #     n = np.random.randint(15, 100)
    #
    # o = np.random.randint(15, 100)
    # while o % 10 == 0 or o == k or o == l or o == m or o == n:
    #     o = np.random.randint(15, 100)
    #
    # num_list = [k, l, m, n, o]
    # num_list.sort()
    #
    # k = num_list[0]
    # l = num_list[1]
    # m = num_list[2]
    # n = num_list[3]
    # o = num_list[4]
    #
    # a = round(np.random.randint(10, k) / 10, 1)
    # c = round(np.random.randint(10, m) / 10, 1)
    # e = round(np.random.randint(10, l) / 10, 1)
    #
    # g = round(np.random.randint(10, n) / 10, 1)
    # i = round(np.random.randint(10, o) / 10, 1)
    #
    # k = round(k / 10, 1)
    # l = round(l / 10, 1)
    # m = round(m / 10, 1)
    #
    # n = round(n / 10, 1)
    # o = round(o / 10, 1)
    #
    # b = round(k + a, 1)
    # if a < b:
    #     tmp = a
    #     a = b
    #     b = tmp
    #
    # d = round(m + c, 1)
    # if c < d:
    #     tmp = c
    #     c = d
    #     d = tmp
    #
    # f = round(l + e, 1)
    # if e < f:
    #     tmp = e
    #     e = f
    #     f = tmp
    #
    # h = round(n + g, 1)
    # if g < h:
    #     tmp = g
    #     g = h
    #     h = tmp
    #
    # j = round(o + i, 1)
    # if i < j:
    #     tmp = i
    #     i = j
    #     j = tmp
















































# 4-2-3-78
def decimaladdsub423_Stem_062():
    stem = "다음을 보고 사용한 {s1}는 몇 $$수식$$rm L `$$/수식$$인가요?\n$$표$$사용 전 {s1}의 양 : $$수식$${x1} `` rm L `$$/수식$$\n사용 후 {s1}의 양 : $$수식$${x2} `` rm L$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1} `` rm L$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$사용한 {s1}의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$사용 전 {s1}의 양$$수식$$RIGHT ) ` - ` LEFT ($$/수식$$사용 후 {s1}의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {x1} ` - ` {x2} ` = ` {a1} LEFT ( rm L RIGHT )$$/수식$$\n\n"


    s1 = ['페인트', '시멘트'][np.random.randint(0, 2)]

    m = np.random.randint(110, 1000)
    while m % 10 == 0:
        m = np.random.randint(110, 1000)

    n = np.random.randint(100, m)
    while n % 10 == 0:
        n = np.random.randint(100, m)

    x1 = round(m / 100, 2)
    x2 = round(n / 100, 2)

    a1 = round(x1 - x2, 2)

    stem = stem.format(s1=s1, x1=x1, x2=x2)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, a1=a1, s1=s1)

    return stem, answer, comment





































# 4-2-3-80
def decimaladdsub423_Stem_063():
    stem = "계산 결과가 더 큰 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${a} ` - ` {b}$$/수식$$\n㉡ $$수식$${c} ` - ` {d}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${a} ` - ` {b} ` = ` {e}$$/수식$$\n" \
              "㉡ $$수식$${c} ` - ` {d} ` = ` {f}$$/수식$$\n" \
              "따라서 $$수식$${e} ` {k} ` {f}$$/수식$$이므로 계산 결과가 더 큰 것은 {a1}입니다.\n\n"


    m = np.random.randint(1500, 10000)
    while m % 10 == 0:
        m = np.random.randint(1500, 10000)

    n = np.random.randint(1000, m)
    while n % 10 == 0:
        n = np.random.randint(1000, m)

    o = np.random.randint(1500, 10000)
    while o % 10 == 0:
        o = np.random.randint(1500, 10000)

    p = np.random.randint(1000, o)
    while p % 10 == 0 or (m - n) == (o - p):
        p = np.random.randint(1000, o)

    a = round(m / 100, 2)
    b = round(n / 100, 2)
    c = round(o / 100, 2)

    d = round(p / 100, 2)
    e = round(a - b, 2)
    f = round(c - d, 2)

    if e > f:
        a1 = "㉠"
        k = "&gt;"
    else:
        a1 = "㉡"
        k = "&lt;"

    stem = stem.format(a=a, b=b, c=c, d=d)
    answer = answer.format(a1=a1)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f, k=k, a1=a1)

    return stem, answer, comment












































# 4-2-3-81
def decimaladdsub423_Stem_064():
    stem = "계산 결과가 작은 것부터 차례대로 기호를 써 보세요.\n$$표$$㉠ $$수식$${a} ` - ` {b}$$/수식$$\n㉡ $$수식$${c} ` - ` {d}$$/수식$$\n㉢ $$수식$${e} ` - ` {f}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{a1}, {a2}, {a3}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${a} ` - ` {b} ` = ` {k}$$/수식$$\n" \
              "㉡ $$수식$${c} ` - ` {d} ` = ` {l}$$/수식$$\n" \
              "㉢ $$수식$${e} ` - ` {f} ` = ` {m}$$/수식$$\n" \
              "따라서 $$수식$${y3} ` &gt; ` {y2} ` &gt; ` {y1}$$/수식$$이므로 계산 결과가 작은 것부터 기호를 쓰면 {a1}, {a2}, {a3}입니다.\n\n"


    a = round(np.random.randint(11, 100) / 10, 1)
    b = round(np.random.randint(100, 1000) / 100, 2)
    k = round(a - b, 2)

    while a < b:
        b = round(np.random.randint(100, 1000) / 100, 2)
        k = round(a - b, 2)

    c = round(np.random.randint(110, 1000) / 100, 2)
    d = round(np.random.randint(10, 100) / 10, 1)
    l = round(c - d, 2)

    while c < d or k == l:
        d = round(np.random.randint(10, 100) / 10, 1)
        l = round(c - d, 2)

    e = round(np.random.randint(11, 100) / 10, 1)
    f = round(np.random.randint(110, 1000) / 100, 2)
    m = round(e - f, 2)

    while e < f or m == k or m == l:
        f = round(np.random.randint(100, 1000) / 100, 2)
        m = round(e - f, 2)

    y_list = [k, l, m]
    y_list.sort()

    y1 = y_list[0]
    y2 = y_list[1]
    y3 = y_list[2]

    num_dict = {k: "㉠", l: "㉡", m: "㉢"}
    a1 = num_dict[y1]
    a2 = num_dict[y2]
    a3 = num_dict[y3]

    stem = stem.format(a=a, b=b, c=c, d=d, e=e, f=f)
    answer = answer.format(a1=a1, a2=a2, a3=a3)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e, f=f, k=k, l=l, m=m, y1=y1, y2=y2, y3=y3, a1=a1, a2=a2, a3=a3)

    return stem, answer, comment






































# 4-2-3-82
def decimaladdsub423_Stem_065():
    stem = "㉠, ㉡, ㉢에 알맞은 수를 차례대로 구해 보세요.\n$$수식$${x1}$$/수식$$.㉠$$수식$${x2} ` - `$$/수식$$㉡.$$수식$${x4}{x5} ` = ` {x6}.{x7}$$/수식$$㉢\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, $$수식$${a3}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$10 ` + ` {x2} ` - ` {x5} ` = ` $$/수식$$㉢ → ㉢ $$수식$$= ` {a3}$$/수식$$\n" \
              "㉠ $$수식$$- ` 1 ` + ` 10 ` - ` {x4} ` = ` {x7} $$/수식$$ → ㉠ $$수식$$= ` {a1} $$/수식$$\n" \
              "$$수식$${x1} ` - ` 1 ` - ` $$/수식$$㉡ $$수식$$= ` {x6}$$/수식$$→ ㉡ $$수식$$= ` {a2}$$/수식$$\n\n"


    a = np.random.randint(1, 10)
    a2 = np.random.randint(0, a)
    d = np.random.randint(1, 10)

    a1 = np.random.randint(0, d + 1)
    e = np.random.randint(1, 10)
    b = np.random.randint(0, e)

    a3 = 10 - e + b
    g = 10 - d + a1 - 1
    f = a - 1 - a2

    stem = stem.format(x1=a, x2=b, x4=d, x5=e, x6=f, x7=g)
    answer = answer.format(a1=a1, a2=a2, a3=a3)
    comment = comment.format(x1=a, x2=b, x4=d, x5=e, x6=f, x7=g, a1=a1, a2=a2, a3=a3)

    return stem, answer, comment






































# 4-2-3-83
def decimaladdsub423_Stem_066():
    stem = "$$수식$${x1}$$/수식$$의 $$수식$$1 over 10$$/수식$$인 수와 $$수식$${x2}$$/수식$$의 차는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${x1}$$/수식$$의 $$수식$$1 over 10$$/수식$$인 수는 $$수식$${x3}$$/수식$$입니다.\n" \
              "따라서 $$수식$${x3}$$/수식$${j1} $$수식$${x2}$$/수식$$의 차는 $$수식$${x3} ` &gt; ` {x2}$$/수식$$이므로 " \
              "$$수식$${x3} ` - ` {x2} ` = ` {a1}$$/수식$$입니다.\n\n"


    m = np.random.randint(1000, 10000)

    while m % 10 == 0:
        m = np.random.randint(1000, 10000)

    n = np.random.randint(100, 1000)

    while n % 10 == 0:
        n = np.random.randint(100, 1000)

    x1 = round(m / 10, 1)
    x2 = round(n / 100, 2)
    x3 = round(x1 / 10, 2)

    a1 = round(x3 - x2, 2)
    j1 = proc_jo(m, 2)

    stem = stem.format(x1=x1, x2=x2)
    answer = answer.format(a1=a1)
    comment = comment.format(j1=j1, x1=x1, x2=x2, x3=x3, a1=a1)

    return stem, answer, comment










































# 4-2-3-84
def decimaladdsub423_Stem_067():
    stem = "$$수식$$1$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 중 □ 안에 들어갈 수 있는 가장 큰 수를 구해 보세요.\n$$표$$ $$수식$$ {a}.□ ` &lt; ` {b} ` - ` {c} $$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${b} ` - ` {c} ` = ` {d}$$/수식$$이므로\n" \
              "$$수식$$ {a}.□ ` &lt; ` {d} $$/수식$$에서 □ 안에 들어갈 수 있는 수는\n {s1}이고,\n" \
              "이 중에서 가장 큰 수는 $$수식$${a1}$$/수식$$입니다.\n\n"


    e = 0

    while e < 2:
        m = np.random.randint(110, 1000)

        while m % 10 == 0:
            m = np.random.randint(110, 1000)

        n = np.random.randint(100, m)

        while n % 10 == 0:
            n = np.random.randint(100, m)

        b = round(m / 100, 2)
        c = round(n / 100, 2)

        d = round(b - c, 2)
        a = int(d)
        e = int(d * 10) % 10


    s1 = ""

    for i in range(1, e + 1):
        s1 = s1 + "$$수식$$" + str(i) + "$$/수식$$, "

    s1 = s1[0:-2]
    a1 = e

    stem = stem.format(a=a, b=b, c=c)
    answer = answer.format(a1=a1)
    comment = comment.format(a=a, b=b, c=c, d=d, s1=s1, a1=a1)

    return stem, answer, comment




































# 4-2-3-85
def decimaladdsub423_Stem_068():
    stem = "$$수식$${x1} `` rm kg `$$/수식$$짜리 {s1}이 담겨 있는 상자의 무게가 $$수식$${x2} `` rm kg `$$/수식$$입니다. 빈 상자의 무게는 몇 $$수식$$rm kg `$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${a1} `` rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$빈 상자의 무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` LEFT ($$/수식$${s1}이 담긴 상자의 무게$$수식$$RIGHT ) ` - ` LEFT ($$/수식$${s1}의 무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {x2} ` - ` {x1} ` = ` {a1} LEFT ( rm kg RIGHT )$$/수식$$\n\n"


    s1 = ['수박', '멜론', '파인애플'][np.random.randint(0, 3)]

    m = np.random.randint(110, 1000)

    while m % 10 == 0:
        m = np.random.randint(110, 1000)

    n = np.random.randint(100, m)

    while n % 10 == 0:
        n = np.random.randint(100, m)

    x2 = round(m / 10, 1)
    x1 = round(n / 10, 1)

    a1 = round(x2 - x1, 1)

    stem = stem.format(x1=x1, x2=x2, s1=s1)
    answer = answer.format(a1=a1)
    comment = comment.format(s1=s1, x1=x1, x2=x2, a1=a1)

    return stem, answer, comment









































# 4-2-3-86
def decimaladdsub423_Stem_069():
    stem = "$$수식$$100 `` rm m `$$/수식$$를 {wh1}는 $$수식$${x1}$$/수식$$초에 달렸고, {wh2}는 $$수식$${x2}$$/수식$$초에 달렸습니다. $$수식$$100 `` rm m `$$/수식$$를 누가 몇 초 더 빨리 달렸나요?\n$$수식$$100 `` rm m `$$/수식$$를 $$수식$${box1}$$/수식$$가 $$수식$${box2}$$/수식$$초 더 빨리 달렸습니다.\n"
    answer = "(정답)\n{a1}, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${x1} {k} {x2}$$/수식$$이므로 {a1}가 {na}보다\n" \
              "$$수식$${x3} ` - ` {x4} ` = ` {a2} LEFT ($$/수식$$초$$수식$$RIGHT )$$/수식$$ 더 빨리 달렸습니다.\n\n"


    wh_list = ['지우', '윤주', '기후', '지후', '광수', '준서', '미나', '홍기', '보배', '석재', '혜교', '하니', '권호', '상무']

    wh1 = wh_list[np.random.randint(0, 14)]
    wh2 = wh_list[np.random.randint(0, 14)]

    while wh1 == wh2:
        wh2 = wh_list[np.random.randint(0, 14)]


    m = np.random.randint(1100, 10000)
    while m % 10 == 0:
        m = np.random.randint(1100, 10000)

    n = np.random.randint(1100, 10000)
    while n % 10 == 0 or m == n:
        n = np.random.randint(1100, 10000)


    x1 = round(m / 100, 2)
    x2 = round(n / 100, 2)

    if x1 > x2:
        k = "`&gt;`"
        x3 = x1
        x4 = x2
        a1 = wh2
        na = wh1

    else:
        k = "`&lt;`"
        x3 = x2
        x4 = x1
        a1 = wh1
        na = wh2

    a2 = round(x3 - x4, 2)

    box1 = "box{　　　}"
    box2 = "box{　　　}"

    stem = stem.format(x1=x1, x2=x2, wh1=wh1, wh2=wh2, box1=box1, box2=box2)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, k=k, a1=a1, a2=a2, na=na)

    return stem, answer, comment











































# 4-2-3-87
def decimaladdsub423_Stem_070():
    stem = "밀가루 $$수식$${x1} `` rm kg `$$/수식$$ 있었습니다. 그중에서 $$수식$${x2} `` rm kg `$$/수식$$으로 {s1}{j1} 만들었고, $$수식$${x3} `` rm kg$$/수식$$으로 {s2}{j2} 만들었습니다. {s1}{j3} {s2}{j2} 만들고 남은 밀가루는 몇 $$수식$$rm kg `$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${a1} `` rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${s1}{j1} 만들고 남은 밀가루의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {x1} ` - ` {x2} ` = ` {x4} LEFT ( rm kg RIGHT )$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${s2}{j2} 만들고 남은 밀가루의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$` = ` {x4} ` - ` {x3} ` = ` {a1} LEFT ( rm kg RIGHT )$$/수식$$\n\n"


    s_list = ['소보루빵', '식빵', '케이크', '샌드위치', '도넛']

    s1 = s_list[np.random.randint(0, 5)]
    s2 = s_list[np.random.randint(0, 5)]

    while s1 == s2:
        s2 = s_list[np.random.randint(0, 5)]


    while True:
        m = np.random.randint(101, 1000)
        n = np.random.randint(10, 1000)

        x2 = round(m / 100, 2)
        x3 = round(n / 100, 2)

        if x2 + x3 + 1 >= 10:
            continue

        x1 = int(np.random.randint(x2 + x3 + 1, 10))

        if m % 10 !=0 and n < m and n % 10 != 0:
            break


    x4 = round(x1 - x2, 2)
    a1 = round(x4 - x3, 2)
    a1 = show_int(a1)

    j1 = proc_jo(s1, 4)
    j2 = proc_jo(s2, 4)
    j3 = proc_jo(s1, 2)


    stem = stem.format(x1=x1, x2=x2, x3=x3, s1=s1, s2=s2, j1=j1, j2=j2, j3=j3)
    answer = answer.format(a1=a1)
    comment = comment.format(j1=j1, j2=j2, x1=x1, x2=x2, x3=x3, x4=x4, a1=a1, s1=s1, s2=s2)

    return stem, answer, comment




    # m = n = 900
    #
    # while m + n >= 900:
    #     m = np.random.randint(110, 1000)
    #     while m % 10 == 0:
    #         m = np.random.randint(110, 1000)
    #
    #     n = np.random.randint(100, m)
    #     while n % 10 == 0:
    #         n = np.random.randint(100, m)





























# 4-2-3-89
def decimaladdsub423_Stem_071():
    stem = "{s1} 테이프와 {s2} 테이프를 겹쳐서 한 줄로 길게 이어 붙였더니 전체 길이가 $$수식$${x1} `` rm m `$$/수식$$였습니다. {s1} 테이프의 길이가 $$수식$${x2} `` rm m `$$/수식$$이고 겹친 부분의 길이가 $$수식$${x3} `` rm m `$$/수식$$라면 {s2} 테이프의 길이는 몇 $$수식$$rm m `$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${a1} `` rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "{s2} 테이프의 길이를 □$$수식$$`` rm m `$$/수식$$라 하면 " \
              "$$수식$$LEFT ($$/수식$$전체 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$${s1} 테이프의 길이$$수식$$RIGHT ) ` + ` LEFT ($$/수식$${s2} 테이프의 길이$$수식$$RIGHT ) $$/수식$$\n$$수식$$ ` - ` LEFT ($$/수식$$겹친 부분의 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {x2} ` + `$$/수식$$□$$수식$$` - ` {x3} ` = ` {x1} LEFT ( rm m RIGHT )$$/수식$$에서\n" \
              "□$$수식$$` = ` {x1} ` + ` {x3} ` - ` {x2} $$/수식$$\n$$수식$$` = ` {x4} ` - ` {x2} ` = ` {a1} LEFT ( rm m RIGHT )$$/수식$$\n\n"


    s_list = ['노란색', '파란색', '빨간색', '주황색', '보라색']

    s1 = s_list[np.random.randint(0, 5)]
    s2 = s_list[np.random.randint(0, 5)]

    while s1 == s2:
        s2 = s_list[np.random.randint(0, 5)]

    m = np.random.randint(1100, 10000)

    while m % 10 == 0:
        m = np.random.randint(1100, 10000)

    n = np.random.randint(1000, m)

    while n % 10 == 0 or m == n:
        n = np.random.randint(1000, m)

    o = np.random.randint(100, 1000)

    while o % 10 == 0:
        o = np.random.randint(100, 1000)

    x1 = round(m / 100, 2)
    x2 = round(n / 100, 2)
    x3 = round(o / 100, 2)

    x4 = round(x1 + x3, 2)
    a1 = round(x4 - x2, 2)

    stem = stem.format(s1=s1, s2=s2, x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=a1)
    comment = comment.format(s1=s1, s2=s2, x1=x1, x2=x2, x3=x3, x4=x4, a1=a1)

    return stem, answer, comment









































# 4-2-3-90
def decimaladdsub423_Stem_072():
    stem = "길이가 $$수식$${x1} `` rm m `$$/수식$$인 끈과 $$수식$${x2} `` rm m `$$/수식$$인 끈을 묶었더니 묶은 전체 끈의 길이가 $$수식$${x3} `` rm m `$$/수식$$가 되었습니다. 매듭을 짓는 데 사용한 끈의 길이는 몇 $$수식$$rm m `$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${a1} `` rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$매듭을 짓는 데 사용한 끈의 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` LEFT ($$/수식$$두 끈의 길이의 합$$수식$$RIGHT ) ` - ` LEFT ($$/수식$$묶은 전체 끈의 길이$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= ` {x1} ` + ` {x2} ` - ` {x3}$$/수식$$\n" \
              "□$$수식$$` = ` {x4} ` - ` {x3} ` = ` {a1} LEFT ( rm m RIGHT )$$/수식$$\n\n"


    o = 10

    while o % 10 == 0 or m + n <= o:
        m = np.random.randint(100, 1000)
        while m % 10 == 0:
            m = np.random.randint(100, 1000)
        n = np.random.randint(100, 1000)
        while n % 10 == 0:
            n = np.random.randint(100, 1000)

        o = np.random.randint(1000, 10000)

    x1 = round(m / 100, 2)
    x2 = round(n / 100, 2)
    x3 = round(o / 100, 2)

    x4 = round(x1 + x2, 2)
    a1 = round(x4 - x3, 2)

    stem = stem.format(x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, a1=a1)

    return stem, answer, comment



































# 4-2-3-91
def decimaladdsub423_Stem_073():
    stem = "$$수식$${x1}$$/수식$$에 어떤 수를 더해야 할 것을 잘못하여 뺐더니 $$수식$${x2}$$/수식$${j1} 되었습니다. 바르게 계산한 값과 잘못 계산한 값의 합을 구해 보세요.\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "어떤 수를 □라 하면 \n" \
              "$$수식$${x1} ` - `$$/수식$$□$$수식$$` = ` {x2}$$/수식$$이므로\n" \
              "□$$수식$$` = ` {x1} ` - ` {x2} ` = ` {x3}$$/수식$$입니다.\n" \
              "바르게 계산하면 $$수식$${x1} ` + ` {x3} ` = ` {x4}$$/수식$$입니다.\n" \
              "바르게 계산한 값과 잘못 계산한 값의 합은\n" \
              "$$수식$${x4} ` + ` {x2} ` = ` {a1}$$/수식$$입니다.\n\n"


    m = np.random.randint(1100, 10000)

    while m % 10 == 0:
        m = np.random.randint(1100, 10000)

    n = np.random.randint(1000, m)

    while n % 10 == 0:
        n = np.random.randint(1000, m)

    x1 = round(m / 100, 2)
    x2 = round(n / 100, 2)

    x3 = round(x1 - x2, 2)
    x4 = round(x1 + x3, 2)
    a1 = round(x4 + x2, 2)

    j1 = proc_jo(n, 0)


    stem = stem.format(x1=x1, x2=x2, j1=j1)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, a1=a1)

    return stem, answer, comment














