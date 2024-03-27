import numpy as np
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
    4: "㉤"
}














answer_kodict2 = {
    0: '㉠',
    1: '㉡',
    2: '㉢',
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



































# 3-2-5-06
def sizeandweight325_Stem_001():
    stem = "{p1}의 {s1}에 가득 차 있던 {s2}{jo} {p2}의 빈 {s1}에 모두 부었더니 {a1}.\n들이가 더 {b1} 것은 누구의 {s1}인가요?\n"
    answer = "(정답)\n{p3}\n"
    comment = "(해설)\n" \
              "{p1}의 {s1}에 가득 차 있던 {s2}{jo} {p2}의 {s1}에 모두 부었을 때 {a2}, " \
              "{p3}의 {s1}의 들이가 더 {b2}.\n\n"


    p1, p2 = random.sample(['준서', '유라', '수미', '현수', '채아', '민주',
                            '지호', '연아', '은우', '시우', '혁재', '민하'], 2)
    s1 = ['컵', '물통', '물병', '그릇', '주전자', '수조'][np.random.randint(0, 6)]
    s2 = ['물', '우유', '주스', '음료'][np.random.randint(0, 4)]
    jo = proc_jo(s2, 1)

    a1, a2, b1, b2, p3 = [['넘쳤습니다', '넘쳤으므로', '많은', '많습니다', p1],
                          ['넘쳤습니다', '넘쳤으므로', '적은', '적습니다', p2],
                          ['가득 차지 않았습니다', '가득 차지 않았으므로', '많은', '많습니다', p2],
                          ['가득 차지 않았습니다', '가득 차지 않았으므로', '적은', '적습니다', p1]][np.random.randint(0, 4)]


    stem = stem.format(p1=p1, p2=p2, s1=s1, s2=s2, jo=jo, a1=a1, b1=b1)
    answer = answer.format(p3=p3)
    comment = comment.format(p1=p1, p2=p2, p3=p3, s1=s1, s2=s2, jo=jo, a2=a2, b2=b2)

    return stem, answer, comment




































# 3-2-5-08
def sizeandweight325_Stem_002():
    stem = "가, 나, 다 세 {bottle}에 물을 가득 채운 후 모양과 크기가 같은 작은 컵에 옮겨 담았더니 다음과 같은 수만큼 들어갔습니다. 들이가 가장 {g} {bottle}을 찾아 써 보세요.\n$$표$$가: $$수식$${a}$$/수식$$개   나: $$수식$${b}$$/수식$$개   다: $$수식$${c}$$/수식$$개$$/표$$\n"
    answer = "(정답)\n{x}\n"
    comment = "(해설)\n" \
              "$$수식$${d} &lt; {e} &lt; {f}$$/수식$$이므로 들이가 가장 {g} {bottle}은 {x}입니다.\n\n"


    bottle = ["물통", "물병", "어항"][np.random.randint(0, 3)]

    numlist = random.sample(list(range(3, 11)), 3)
    a, b, c = numlist
    numlist.sort()
    d, e, f = numlist

    g = ['많은', '적은'][np.random.randint(0, 2)]
    if g == '많은':
        if a == f:
            x = '가'
        elif b == f:
            x = '나'
        else:
            x = '다'
    else:
        if a == d:
            x = '가'
        elif b == d:
            x = '나'
        else:
            x = '다'


    stem = stem.format(a=a, b=b, c=c, g=g, bottle=bottle)
    answer = answer.format(x=x)
    comment = comment.format(d=d, e=e, f=f, g=g, x=x, bottle=bottle)

    return stem, answer, comment




































# 3-2-5-09
def sizeandweight325_Stem_003():
    stem = "다음은 각자의 컵으로 모양과 코기가 같은 세 {s}에 가득 채워진 물을 전부 덜어 낸 횟수입니다. 들이가 가장 {g} 컵을 가진 사람은 누구인가요?\n$$표$${p1}: $$수식$${a}$$/수식$$번   {p2}: $$수식$${b}$$/수식$$번   {p3}: $$수식$${c}$$/수식$$번$$/표$$\n"
    answer = "(정답)\n{x}\n"
    comment = "(해설)\n" \
              "덜어 낸 횟수를 비교하면 $$수식$${d} &lt; {e} &lt; {f}$$/수식$$이므로 " \
              "들이가 가장 {g} 컵을 가진 사람은 {x}입니다.\n\n"


    p1, p2, p3 = random.sample(['동우', '재우', '진희', '준서', '유라',
                                '수미', '현수', '채아', '민주', '지호',
                                '연아', '은우', '시우', '혁재', '민하'], 3)

    s = ['양동이', '주전자', '물통', '물병'][np.random.randint(0, 4)]

    nums = random.sample(list(range(3, 11)), 3)
    a, b, c = nums
    nums.sort()
    d, e, f = nums

    g = ['많은', '적은'][np.random.randint(0, 2)]

    if g == '적은':
        if a == f:
            x = p1
        elif b == f:
            x = p2
        else:
            x = p3
    else:
        if a == d:
            x = p1
        elif b == d:
            x = p2
        else:
            x = p3


    stem = stem.format(a=a, b=b, c=c, g=g, s=s, p1=p1, p2=p2, p3=p3)
    answer = answer.format(x=x)
    comment = comment.format(d=d, e=e, f=f, g=g, x=x)

    return stem, answer, comment

































# 3-2-5-10
def sizeandweight325_Stem_004():
    stem = "들이 단위 사이의 관계를 나타낸 것입니다. ㉠과 ㉡에 알맞은 수를 차례로 써 보세요.\n$$표$$∙ $$수식$${a} rm L =$$/수식$$㉠$$수식$$rm {{mL}}$$/수식$$\n∙ $$수식$${c} rm {{mL}} =$$/수식$$㉡$$수식$$rm L$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${b}$$/수식$$, $$수식$${d}$$/수식$$\n"
    comment = "(해설)\n" \
              "∙ $$수식$$1 rm L = 1000 rm {{mL}}$$/수식$$이므로 " \
              "$$수식$${a} rm L =$$/수식$$㉠$$수식$$rm {{mL}}$$/수식$$에서 ㉠$$수식$$= {b}$$/수식$$입니다.\n" \
              "∙ $$수식$$1000 rm {{mL}} = 1 rm L$$/수식$$이므로 " \
              "$$수식$${c} rm {{mL}} =$$/수식$$㉡$$수식$$rm L$$/수식$$에서 ㉡$$수식$$= {d}$$/수식$$입니다.\n\n"


    a, d = random.sample(list(range(5, 18)), 2)
    b = a * 1000
    c = d * 1000


    stem = stem.format(a=a, c=c)
    answer = answer.format(b=b, d=d)
    comment = comment.format(a=a, b=b, c=c, d=d)

    return stem, answer, comment






































# 3-2-5-11
def sizeandweight325_Stem_005():
    stem = "들이가 다른 하나를 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${x1}$$/수식$$    ㉡ $$수식$${x2}$$/수식$$    ㉢ $$수식$${x3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{x}\n"
    comment = "(해설)\n" \
              "$$수식$${d} rm {{mL}} = {b} TIMES 1000 rm {{mL}} + {e} rm {{mL}}$$/수식$$\n$$수식$$ = {b} rm L + {e} rm {{mL}} = {b} rm L ```` {e} rm {{mL}}$$/수식$$\n" \
              "따라서 들이가 다른 하나는 {x}. $$수식$${b} rm L `` {f} rm {{mL}}$$/수식$$입니다.\n\n"


    a = np.random.randint(21, 99)
    b = np.random.randint(1, 10)
    c = a * 10
    e, f = [[a, c], [c, a]][np.random.randint(0, 2)]
    d = b * 1000 + e

    y1 = "%d rm {{mL}}" % d
    y2 = "%d rm L `` %d rm {{mL}}" % (b, c)
    y3 = "%d rm L `` %d rm {{mL}}" % (b, a)

    candidates = [y1, y2, y3]
    np.random.shuffle(candidates)
    [x1, x2, x3] = candidates

    x = ""

    if f == a:
        for idx, sdx in enumerate(candidates):
            if sdx == y3:
                x = idx
    else:
        for idx, sdx in enumerate(candidates):
            if sdx == y2:
                x = idx


    x = answer_kodict[x]

    stem = stem.format(a=a, b=b, c=c, d=d, x1=x1, x2=x2, x3=x3)
    answer = answer.format(x=x)
    comment = comment.format(b=b, d=d, e=e, f=f, x=x)

    return stem, answer, comment


































# 3-2-5-13
def sizeandweight325_Stem_006():
    stem = "□ 안에 들어갈 알맞은 수를 구하세요.\n$$수식$$LEFT ( 1 RIGHT ) ```` {a1} rm L =$$/수식$$$$수식$${box}$$/수식$$$$수식$$rm {{mL}}$$/수식$$\n$$수식$$LEFT ( 2 RIGHT ) ```` {b1} rm L `` {b2} rm {{mL}} =$$/수식$$$$수식$${box}$$/수식$$$$수식$$rm {{mL}}$$/수식$$\n$$수식$$LEFT ( 3 RIGHT ) ```` {c4} rm {{mL}} =$$/수식$$$$수식$${box}$$/수식$$$$수식$$rm L$$/수식$$ $$수식$${box}$$/수식$$$$수식$$rm {{mL}}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a2}$$/수식$$," \
             "$$수식$${b4}$$/수식$$, " \
             "$$수식$${c1}$$/수식$$, $$수식$${c2}$$/수식$$   \n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1 RIGHT ) ```` {a1} rm L = {a2} rm {{mL}}$$/수식$$\n" \
              "$$수식$$LEFT ( 2 RIGHT ) ```` {b1} rm L `` {b2} rm {{mL}} = {b1} rm L + {b2} rm {{mL}}$$/수식$$\n$$수식$$ = {b3} rm {{mL}} + {b2} rm {{mL}} = {b4} rm {{mL}}$$/수식$$\n" \
              "$$수식$$LEFT ( 3 RIGHT ) ```` {c4} rm {{mL}} = {c3} rm {{mL}} + {c2} rm {{mL}}$$/수식$$\n$$수식$$ = {c1} rm L + {c2} rm {{mL}} = {c1} rm L `` {c2} rm {{mL}}$$/수식$$\n\n"


    a1 = np.random.randint(3, 13)
    a2 = a1 * 1000

    while True:
        b1, c1 = random.sample(list(range(1, 10)), 2)
        if b1 != a1 and c1 != a1:
            break

    b2, c2 = random.sample(list(range(35, 250)), 2)

    b3 = b1 * 1000
    b4 = b3 + b2
    c3 = c1 * 1000
    c4 = c3 + c2

    box = "box{　　　}"

    stem = stem.format(a1=a1, b1=b1, b2=b2, c4=c4, box=box)
    answer = answer.format(a2=a2, b4=b4, c1=c1, c2=c2)
    comment = comment.format(a1=a1, a2=a2, b1=b1, b2=b2, b3=b3, b4=b4, c1=c1, c2=c2, c3=c3, c4=c4)

    return stem, answer, comment









































# 3-2-5-15
def sizeandweight325_Stem_007():
    stem = "들이를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${a} rm {{mL}}$$/수식$$   ○   $$수식$${b} rm L `` {d} rm {{mL}}$$/수식$$\n"
    answer = "(정답)\n$$수식$${x}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${b} rm L `` {d} rm {{mL}} = {b} rm L + {d} rm {{mL}} = {e} rm {{mL}} + {d} rm {{mL}} = {f} rm {{mL}}$$/수식$$\n" \
              "따라서 $$수식$${a} rm {{mL}} {x} {b} rm L `` {d} rm {{mL}}$$/수식$$입니다.\n\n"


    b, c = random.sample(list(range(2, 10)), 2)
    e = b * 1000

    a, d = [[e + c * 10, c], [e + c, c * 10]][np.random.randint(0, 2)]
    f = e + d

    if a > f:
        x = '&gt;'
    else:
        x = '&lt;'


    stem = stem.format(a=a, b=b, d=d)
    answer = answer.format(x=x)
    comment = comment.format(a=a, b=b, d=d, e=e, f=f, x=x)

    return stem, answer, comment





































# 3-2-5-16
def sizeandweight325_Stem_008():
    stem = "들이가 많은 것부터 차례대로 기호를 써 보세요.\n$$표$$㉠ $$수식$${a} rm {{mL}}$$/수식$$      ㉡ $$수식$${b} rm {{mL}}$$/수식$$      ㉢ $$수식$${c1} rm L `` {c2} rm {{mL}}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{x}\n"
    comment = "(해설)\n" \
              "㉢ $$수식$${c1} rm L `` {c2} rm {{mL}} = {c} rm {{mL}}$$/수식$$\n" \
              "따라서 $$수식$${d} rm {{mL}} &gt; {e} rm {{mL}} &gt; {f} rm {{mL}}$$/수식$$이므로 " \
              "들이가 가장 많은 것부터 차례대로 기호를 쓰면 {x}입니다.\n\n"


    a1 = np.random.randint(3, 9)
    b1 = [a1 - 1, a1 + 1][np.random.randint(0, 2)]
    c1 = [a1, b1][np.random.randint(0, 2)]
    a2, b2, c2 = random.sample(list(range(50, 501)), 3)

    a = a1 * 1000 + a2
    b = b1 * 1000 + b2
    c = c1 * 1000 + c2
    nums = [a, b, c]

    nums.sort()

    f, e, d = nums

    if a == d and b == e:
        x = '㉠, ㉡, ㉢'
    elif a == d and c == e:
        x = '㉠, ㉢, ㉡'
    elif b == d and c == e:
        x = '㉡, ㉢, ㉠'
    elif b == d and a == e:
        x = '㉡, ㉠, ㉢'
    elif c == d and a == e:
        x = '㉢, ㉠, ㉡'
    else:
        x = '㉢, ㉡, ㉠'


    stem = stem.format(a=a, b=b, c1=c1, c2=c2)
    answer = answer.format(x=x)
    comment = comment.format(c1=c1, c2=c2, c=c, d=d, e=e, f=f, x=x)

    return stem, answer, comment




































# 3-2-5-17
def sizeandweight325_Stem_009():
    stem = "{p}는 일주일 동안 {s1}를 $$수식$${a1} rm L `` {a2} rm {{mL}}$$/수식$$ 마셨고 {s2}를 $$수식$${b} rm {{mL}}$$/수식$$ 마셨습니다. {p}는 일주일 동안 {s1}와 {s2} 중 어느 것을 더 많이 마셨나요?\n"
    answer = "(정답)\n{y}\n"
    comment = "(해설)\n" \
              "$$수식$${a1} rm L `` {a2} rm {{mL}} = {a} rm {{mL}}$$/수식$$\n" \
              "따라서 $$수식$${a} rm {{mL}} {x} {b} rm {{mL}}$$/수식$$이므로 {p}는 일주일 동안 {y}를 더 많이 마셨습니다.\n\n"


    p = ['은서', '동우', '재우', '진희', '준서', '유라', '수미', '현수', '채아', '민주',
         '지호', '연아', '은우', '시우', '혁재', '민하'][np.random.randint(0, 16)]

    s1, s2 = random.sample(['우유', '사과주스', '포도주스', '딸기주스', '오렌지주스'], 2)

    a1 = np.random.randint(1, 3)
    b1 = a1
    a2, b2 = random.sample(list(range(3, 10)), 2)
    a2 = a2 * 100
    b2 = b2 * 100

    a = a1 * 1000 + a2
    b = b1 * 1000 + b2

    if a > b:
        x = '&gt;'
        y = s1
    else:
        x = '&lt;'
        y = s2


    stem = stem.format(p=p, s1=s1, s2=s2, a1=a1, a2=a2, b=b)
    answer = answer.format(y=y)
    comment = comment.format(p=p, a1=a1, a2=a2, a=a, b=b, y=y, x=x)

    return stem, answer, comment









































# 3-2-5-18
def sizeandweight325_Stem_010():
    stem = "{p}는 {s}{jo1} 들어 있는 통에 {s}{jo2} 더 부어 $$수식$${a} rm {{mL}}$$/수식$$를 만들었습니다. 통에 들어 있는 {s}{jo3} 모두 몇 $$수식$$rm L$$/수식$$ 몇 $$수식$$rm {{mL}}$$/수식$$인가요?\n" \
        "{box1} $$수식$$rm L$$/수식$$ {box2} $$수식$$rm {{mL}}$$/수식$$"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} rm {{mL}} = {b} rm {{mL}} + {a2} rm {{mL}} = {a1} rm L + {a2} rm {{mL}} = {a1} rm L `` {a2} rm {{mL}}$$/수식$$\n\n"

    box1 = "$$수식$$box{　　}$$/수식$$"
    box2 = "$$수식$$box{　　　　}$$/수식$$"

    p = ['상수', '은서', '동우', '재우', '진희', '준서', '유라', '수미', '현수', '채아', '민주',
         '지호', '연아', '은우', '시우', '혁재', '민하'][np.random.randint(0, 17)]

    s = ['우유', '주스', '물', '간장'][np.random.randint(0, 4)]

    jo1 = proc_jo(s, 0)
    jo2 = proc_jo(s, 1)
    jo3 = proc_jo(s, -1)

    a1 = np.random.randint(1, 4)
    a2 = np.random.randint(5, 16)
    a2 = a2 * 10

    b = a1 * 1000
    a = a1 * 1000 + a2


    stem = stem.format(p=p, s=s, jo1=jo1, jo2=jo2, jo3=jo3, a=a, box1=box1, box2=box2)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(a=a, b=b, a1=a1, a2=a2)

    return stem, answer, comment




































# 3-2-5-19
def sizeandweight325_Stem_011():
    stem = "다음 물건을 선택하여 문장을 완성해 보세요.\n$$표$${p1}      {p2}      {p3}$$/표$$\n$$수식$$LEFT ( 1 RIGHT )$$/수식$$ $$수식$${box}$$/수식$$의 들이는 약 $$수식$${a} rm {{mL}}$$/수식$$입니다.\n$$수식$$LEFT ( 2 RIGHT )$$/수식$$ $$수식$${box}$$/수식$$의 들이는 약 $$수식$${b} rm L$$/수식$$입니다.\n"
    answer = "(정답)\n{s1}, {s2}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1 RIGHT )$$/수식$$ {c}\n" \
              "$$수식$$LEFT ( 2 RIGHT )$$/수식$$ {d}\n\n"


    a1 = '$$수식$$13 rm {{mL}}$$/수식$$는 아주 적은 양이므로 숟가락의 들이로 알맞습니다.'
    a2 = '$$수식$$50 rm {{mL}}$$/수식$$는 $$수식$$200 rm {{mL}}$$/수식$$ 우유갑보다 적은 양이므로 물약통의 들이로 알맞습니다.'
    a3 = '$$수식$$180 rm {{mL}}$$/수식$$는 $$수식$$200 rm {{mL}}$$/수식$$ 우유갑보다 조금 적은 양이므로 종이컵의 들이로 알맞습니다.'
    a4 = '$$수식$$300 rm {{mL}}$$/수식$$는 $$수식$$200 rm {{mL}}$$/수식$$ 우유갑보다 조금 많은 양이므로 머그컵의 들이로 알맞습니다.'
    a5 = '$$수식$$480 rm {{mL}}$$/수식$$는 $$수식$$500 rm {{mL}}$$/수식$$ 우유갑보다 조금 적은 양이므로 대접의 들이로 알맞습니다.'

    b1 = '$$수식$$2 rm L$$/수식$$는 $$수식$$1 rm L$$/수식$$의  $$수식$$2$$/수식$$배쯤 되는 양이므로 ' \
         '생수병의 들이로 알맞습니다.'
    b2 = '$$수식$$4 rm L$$/수식$$는 $$수식$$1 rm L$$/수식$$의  $$수식$$4$$/수식$$배쯤 되는 양이므로 ' \
         '세숫대야의 들이로 알맞습니다.'
    b3 = '$$수식$$10 rm L$$/수식$$는 $$수식$$1 rm L$$/수식$$의  $$수식$$10$$/수식$$배쯤 되는 양이므로 ' \
         '양동이의 들이로 알맞습니다.'
    b4 = '$$수식$$200 rm L$$/수식$$는 $$수식$$1 rm L$$/수식$$의  $$수식$$200$$/수식$$배쯤 되는 양이므로 ' \
         '욕조의 들이로 알맞습니다.'


    a, s1, c = [[13, '숟가락', a1], [50, '물약통', a2], [180, '종이컵', a3],
                [300, '머그컵', a4], [480, '대접', a5]][np.random.randint(0, 5)]
    b, s2, d = [[2, '생수병', b1], [4, '세숫대야', b2], [10, '양동이', b3], [200, '욕조', b4]][np.random.randint(0, 4)]

    while True:
        s3 = ['숟가락', '물약통', '종이컵', '머그컵', '대접', '생수병', '세숫대야', '양동이', '욕조'][np.random.randint(0, 9)]
        if s3 != s1 and s3 != s2:
            break

    box = "box{　　　　}"

    p = [s1, s2, s3]
    np.random.shuffle(p)
    p1, p2, p3 = p


    stem = stem.format(p1=p1, p2=p2, p3=p3, a=a, b=b, box=box)
    answer = answer.format(s1=s1, s2=s2)
    comment = comment.format(c=c, d=d)

    return stem, answer, comment



































# 3-2-5-20
def sizeandweight325_Stem_012():
    stem = "{p1}와 {p2}는 실제 들이가 $$수식$${c} rm L$$/수식$$인 물통의 들이를 다음과 같이 어림하였습니다. 누가 더 가깝게 어림하였나요?\n$$표$${p1}: $$수식$${a1} rm L `` {a2} rm {{mL}}$$/수식$$     {p2}: $$수식$${b1} rm L `` {b2} rm {{mL}}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{p3}\n"
    comment = "(해설)\n" \
              "{p1}: $$수식$${a1} rm L `` {a2} rm {{mL}} = {a} rm {{mL}}$$/수식$$\n" \
              "{p2}: $$수식$${b1} rm L `` {b2} rm {{mL}} = {b} rm {{mL}}$$/수식$$\n" \
              "$$수식$${c} rm L = {d} rm {{mL}}$$/수식$$이므로 " \
              "$$수식$${d} rm {{mL}}$$/수식$$와 더 가까운 들이는 $$수식$${e} rm {{mL}}$$/수식$$입니다.\n" \
              "따라서 $$수식$${c} rm L$$/수식$$와 더 가깝게 어림한 사람은 {p3}입니다.\n\n"


    p1, p2 = random.sample(['영기', '상수', '은서', '동우', '재우', '진희', '준서', '유라', '수미', '현수',
                            '채아', '민주', '지호', '연아', '은우', '시우', '혁재', '민하'], 2)

    c = np.random.randint(1, 6)

    d = c * 1000
    a1 = c
    b1 = c
    a2, b2 = random.sample(list(range(1, 6)), 2)

    a2 = a2 * 50
    b2 = b2 * 50
    a = a1 * 1000 + a2
    b = b1 * 1000 + b2

    if a < b:
        e = a
        p3 = p1

    else:
        e = b
        p3 = p2


    stem = stem.format(p1=p1, p2=p2, c=c, a1=a1, a2=a2, b1=b1, b2=b2)
    answer = answer.format(p3=p3)
    comment = comment.format(p1=p1, p2=p2, a1=a1, a2=a2, b1=b1, b2=b2, a=a, b=b, c=c, d=d, e=e, p3=p3)

    return stem, answer, comment










































# 3-2-5-21
def sizeandweight325_Stem_013():
    stem = "들이의 단위가 알맞게 짝지어진 것을 모두 찾아 기호를 써 보세요.\n$$표$$㉠ {a}: $$수식$${x1} {unit1}$$/수식$$     ㉡ {b}: $$수식$${x2} {unit2}$$/수식$$\n㉢ {c}: $$수식$${x3} {unit3}$$/수식$$     ㉣ {d}: $$수식$${x4} {unit4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{s1}, {s2}\n"
    comment = "(해설)\n" \
              "{s3}. {e}{jo1} $$수식$${runit1}$$/수식$$ 단위, {s4}. {f}{jo2} $$수식$${runit2}$$/수식$$ 단위가 알맞습니다.\n\n"


    states = random.sample([['밥숟가락', 15, 'rm {{mL}}'], ['물약 통', 50, 'rm {{mL}}'], ['종이컵', 180, 'rm {{mL}}'], ['머그컵', 300, 'rm {{mL}}'],
                            ['대접', 480, 'rm {{mL}}'], ['국자', 60, 'rm {{mL}}'], ['밥공기', 200, 'rm {{mL}}'], ['생수통', 20, 'rm L'],
                            ['세숫대야', 4, 'rm L'], ['양동이', 10, 'rm L'], ['욕조', 200, 'rm L'], ['주전자', 1, 'rm L'],
                            ['냄비', 2, 'rm L'], ['아이스박스', 60, 'rm L']], 4)


    nums = list(range(0, 4))
    np.random.shuffle(nums)
    pick = nums[0:2]
    pick.sort()
    pick1, pick2 = pick

    nopick = nums[2:4]
    nopick.sort()

    s1 = answer_kodict2[nopick[0]]
    s2 = answer_kodict2[nopick[1]]

    s3 = answer_kodict2[pick1]
    s4 = answer_kodict2[pick2]

    e = states[pick1][0]
    f = states[pick2][0]

    jo1 = proc_jo(e, -1)
    jo2 = proc_jo(f, -1)

    runit1 = states[pick1][2]
    runit2 = states[pick2][2]

    if states[pick1][2] == 'rm {{mL}}':
        states[pick1][2] = 'rm L'
    else:
        states[pick1][2] = 'rm {{mL}}'

    if states[pick2][2] == 'rm {{mL}}':
        states[pick2][2] = 'rm L'
    else:
        states[pick2][2] = 'rm {{mL}}'

    [[a, x1, unit1], [b, x2, unit2], [c, x3, unit3], [d, x4, unit4]] = states


    stem = stem.format(a=a, b=b, c=c, d=d, x1=x1, x2=x2, x3=x3, x4=x4, unit1=unit1, unit2=unit2, unit3=unit3,
                       unit4=unit4)
    answer = answer.format(s1=s1, s2=s2)
    comment = comment.format(s3=s3, s4=s4, e=e, f=f, jo1=jo1, jo2=jo2, runit1=runit1, runit2=runit2)

    return stem, answer, comment






































# 3-2-5-24
def sizeandweight325_Stem_014():
    stem = "{p1}와 {p2}가 $$수식$${c} rm L$$/수식$$의 물을 어림하여 각자의 물통에 담았습니다. 담은 물의 양을 직접 재었더니 다음과 같았습니다. $$수식$${c} rm L$$/수식$$와 더 가깝게 어림한 사람은 누구인가요?\n$$표$$∙ {p1}: $$수식$${a} rm {{mL}}$$/수식$$\n∙ {p2}: $$수식$${b} rm {{mL}}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{p3}\n"
    comment = "(해설)\n" \
              "$$수식$${c} rm L = {d} rm {{mL}}$$/수식$$이므로 $$수식$${d} rm {{mL}}$$/수식$$와 더 가까운 들이는 $$수식$${e} rm {{mL}}$$/수식$$입니다.\n" \
              "따라서 $$수식$${c} rm L$$/수식$$와 더 가깝게 어림한 사람은 {p3}입니다.\n\n"


    p1, p2 = random.sample(['은지', '혁구', '영기', '상수', '은서', '동우', '재우', '진희', '준서', '유라', '수미', '현수',
                            '채아', '민주', '지호', '연아', '은우', '시우', '혁재', '민하'], 2)

    c = np.random.randint(2, 8)
    d = c * 1000
    a1 = c - 1
    b1 = c - 1
    a2, b2 = random.sample(list(range(15, 20)), 2)

    a2 = a2 * 50
    b2 = b2 * 50
    a = a1 * 1000 + a2
    b = b1 * 1000 + b2

    if a > b:
        e = a
        p3 = p1
    else:
        e = b
        p3 = p2


    stem = stem.format(p1=p1, p2=p2, a=a, b=b, c=c)
    answer = answer.format(p3=p3)
    comment = comment.format(c=c, d=d, e=e, p3=p3)

    return stem, answer, comment









































# 3-2-5-27
def sizeandweight325_Stem_015():
    stem = "들이의 합과 차는 각각 몇 $$수식$$rm L$$/수식$$ 몇 $$수식$$rm {{mL}}$$/수식$$인가요?\n$$표$$$$수식$${a1} rm L `` {a2} rm {{mL}}$$/수식$$      $$수식$${b} rm {{mL}}$$/수식$$$$/표$$\n" \
        "합 : {box1} $$수식$$rm L$$/수식$$ {box2} $$수식$$rm {{mL}}$$/수식$$\n차 : {box1} $$수식$$rm L$$/수식$$ {box2} $$수식$$rm {{mL}}$$/수식$$"
    answer = "(정답)\n$$수식$${c1}$$/수식$$, $$수식$${c2}$$/수식$$, $$수식$${d1}$$/수식$$, $$수식$${d2}$$/수식$$"
    comment = "(해설)\n" \
              "합: $$수식$${a1} rm L `` {a2} rm {{mL}} + {b1} rm L `` {b2} rm {{mL}} = {c1} rm L `` {c2} rm {{mL}}$$/수식$$\n" \
              "차: $$수식$${a1} rm L `` {a2} rm {{mL}} - {b1} rm L `` {b2} rm {{mL}} = {d1} rm L `` {d2} rm {{mL}}$$/수식$$\n\n"

    box1 = "$$수식$$box{　　}$$/수식$$"
    box2 = "$$수식$$box{　　　}$$/수식$$"
    
    while True:
        ab1 = random.sample(list(range(3, 9)), 2)
        ab1.sort()
        b1, a1 = ab1
        if a1 + b1 <= 9:
            break

    while True:
        ab2 = random.sample(list(range(1, 9)), 2)
        ab2.sort()
        b2, a2 = ab2
        if a2 + b2 <= 9:
            a2 = a2 * 100
            b2 = b2 * 100
            break

    b = b1 * 1000 + b2
    c1 = a1 + b1
    c2 = a2 + b2
    d1 = a1 - b1
    d2 = a2 - b2


    stem = stem.format(a1=a1, a2=a2, b=b, box1=box1, box2=box2)
    answer = answer.format(c1=c1, c2=c2, d1=d1, d2=d2)
    comment = comment.format(a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, d1=d1, d2=d2)

    return stem, answer, comment









































# 3-2-5-29
def sizeandweight325_Stem_016():
    stem = "두 들이의 합은 몇 $$수식$$rm L$$/수식$$ 몇 $$수식$$rm {{mL}}$$/수식$$인가요?\n$$표$$$$수식$${a} rm {{mL}}$$/수식$$$$/표$$   $$표$$$$수식$${b1} rm L `` {b2} rm {{mL}}$$/수식$$$$/표$$\n" \
        "{box1} $$수식$$rm L$$/수식$$ {box2} $$수식$$rm {{mL}}$$/수식$$"
    answer = "(정답)\n$$수식$${c1}$$/수식$$, $$수식$${c2} $$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} rm {{mL}} = {a1} rm L `` {a2} rm {{mL}}$$/수식$$이므로 " \
              "$$수식$${a1} rm L `` {a2} rm {{mL}} + {b1} rm L `` {b2} rm {{mL}} = {c1} rm L `` {c2} rm {{mL}}$$/수식$$입니다.\n\n"

    box1 = "$$수식$$box{　　}$$/수식$$"
    box2 = "$$수식$$box{　　　}$$/수식$$"

    a1, b1 = random.sample(list(range(1, 10)), 2)

    while True:
        a2, b2 = random.sample(list(range(1, 9)), 2)
        if a2 + b2 <= 9:
            a2 = a2 * 100
            b2 = b2 * 100
            break

    a = a1 * 1000 + a2
    c1 = a1 + b1
    c2 = a2 + b2


    stem = stem.format(a=a, b1=b1, b2=b2, box1=box1, box2=box2)
    answer = answer.format(c1=c1, c2=c2)
    comment = comment.format(a=a, a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2)

    return stem, answer, comment








































# 3-2-5-30
def sizeandweight325_Stem_017():
    stem = "두 들이의 차는 몇 $$수식$$rm L$$/수식$$ 몇 $$수식$$rm {{mL}}$$/수식$$인가요?\n$$표$$$$수식$${a1} rm L `` {a2} rm {{mL}}$$/수식$$      $$수식$${b1} rm L `` {b2} rm {{mL}}$$/수식$$$$/표$$\n" \
        "{box1} $$수식$$rm L$$/수식$$ {box2} $$수식$$rm {{mL}}$$/수식$$"
    answer = "(정답)\n$$수식$${c1}$$/수식$$, $$수식$${c2} $$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a1} rm L `` {a2} rm {{mL}} - {b1} rm L `` {b2} rm {{mL}} = {c1} rm L `` {c2} rm {{mL}}$$/수식$$\n\n"

    box1 = "$$수식$$box{　　}$$/수식$$"
    box2 = "$$수식$$box{　　　}$$/수식$$"
    
    ab1 = random.sample(list(range(1, 10)), 2)
    ab1.sort()
    b1, a1 = ab1

    ab2 = random.sample(list(range(1, 10)), 2)
    ab2.sort()
    b2, a2 = ab2

    a2 = a2 * 100
    b2 = b2 * 100

    c1 = a1 - b1
    c2 = a2 - b2


    stem = stem.format(a1=a1, a2=a2, b1=b1, b2=b2, box1=box1, box2=box2)
    answer = answer.format(c1=c1, c2=c2)
    comment = comment.format(a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2)

    return stem, answer, comment








































# 3-2-5-32
def sizeandweight325_Stem_018():
    stem = "들이를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${a1} rm L `` {a2} rm {{mL}} + {b1} rm L `` {b2} rm {{mL}}$$/수식$$  ○  $$수식$${c1} rm L `` {c2} rm {{mL}} + {d1} rm L `` {d2} rm {{mL}}$$/수식$$\n"
    answer = "(정답)\n$$수식$${x}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a1} rm L `` {a2} rm {{mL}} + {b1} rm L `` {b2} rm {{mL}} = {a} rm L `` {b} rm {{mL}}$$/수식$$, " \
              "$$수식$${c1} rm L `` {c2} rm {{mL}} + {d1} rm L `` {d2} rm {{mL}} = {c} rm L `` {d} rm {{mL}}$$/수식$$\n" \
              "따라서 $$수식$${a} rm L `` {b} rm {{mL}} {x} {c} rm L `` {d} rm {{mL}}$$/수식$$이므로\n" \
              "$$수식$${a1} rm L `` {a2} rm {{mL}} + {b1} rm L `` {b2} rm {{mL}} {x} {c1} rm L `` {c2} rm {{mL}} + {d1} rm L `` {d2} rm {{mL}}$$/수식$$입니다.\n\n"


    while True:
        a1, b1 = random.sample(list(range(1, 9)), 2)
        if a1 + b1 <= 9:
            break

    while True:
        a2, b2 = random.sample(list(range(5, 99)), 2)
        if a2 + b2 >= 101:
            a2 = a2 * 10
            b2 = b2 * 10
            break

    while True:
        c1, d1 = random.sample(list(range(1, 9)), 2)
        if c1 + d1 == a1 + b1 and c1 != a1:
            break

    while True:
        c2, d2 = random.sample(list(range(2, 20)), 2)
        if c2 + d2 >= 21:
            c2 = c2 * 50
            d2 = d2 * 50
            break

    a = a1 + b1 + 1
    b = a2 + b2 - 1000
    c = c1 + d1 + 1
    d = c2 + d2 - 1000

    if b > d:
        x = '&gt;'
    elif b == d:
        x = '='
    else:
        x = '&lt;'


    stem = stem.format(a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, d1=d1, d2=d2)
    answer = answer.format(x=x)
    comment = comment.format(a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, d1=d1, d2=d2, a=a, b=b, c=c, d=d, x=x)

    return stem, answer, comment









































# 3-2-5-33
def sizeandweight325_Stem_019():
    stem = "들이가 더 많은 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${a1} rm L `` {a2} rm {{mL}} + {b1} rm L `` {b2} rm {{mL}}$$/수식$$\n㉡ $$수식$${c1} rm L `` {c2} rm {{mL}} + {d1} rm L `` {d2} rm {{mL}}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{y}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${a1} rm L `` {a2} rm {{mL}} + {b1} rm L `` {b2} rm {{mL}} = {a} rm L `` {b} rm {{mL}}$$/수식$$\n" \
              "㉡ $$수식$${c1} rm L `` {c2} rm {{mL}} + {d1} rm L `` {d2} rm {{mL}} = {c} rm L `` {d} rm {{mL}}$$/수식$$\n" \
              "따라서 $$수식$${a} rm L `` {b} rm {{mL}} {x} {c} rm L `` {d} rm {{mL}}$$/수식$$이므로 들이가 더 많은 것은 {y}입니다.\n\n"


    a1, b1 = random.sample(list(range(1, 10)), 2)

    while True:
        a2, b2 = random.sample(list(range(1, 10)), 2)
        if a2 + b2 >= 11:
            a2 = a2 * 100
            b2 = b2 * 100
            break

    while True:
        c1, d1 = random.sample(list(range(1, 10)), 2)
        if c1 + d1 == a1 + b1 and c1 != a1:
            break

    while True:
        c2, d2 = random.sample(list(range(1, 10)), 2)
        c2 = c2 * 100
        d2 = d2 * 100
        if c2 + d2 >= 1100 and c2 + d2 != a2 + b2:
            break

    a = a1 + b1 + 1
    b = a2 + b2 - 1000
    c = c1 + d1 + 1
    d = c2 + d2 - 1000

    if b > d:
        x = '&gt;'
        y = '㉠'
    else:
        x = '&lt;'
        y = '㉡'


    stem = stem.format(a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, d1=d1, d2=d2)
    answer = answer.format(y=y)
    comment = comment.format(a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, d1=d1, d2=d2, a=a, b=b, c=c, d=d, x=x, y=y)

    return stem, answer, comment










































# 3-2-5-34
def sizeandweight325_Stem_020():
    stem = "두 들이의 차는 몇 $$수식$$rm L$$/수식$$ 몇 $$수식$$rm {{mL}}$$/수식$$인가요?\n$$표$$$$수식$${n1}$$/수식$$   $$수식$${n2}$$/수식$$$$/표$$\n" \
        "{box1} $$수식$$rm L$$/수식$$ {box2} $$수식$$rm {{mL}}$$/수식$$"
    answer = "(정답)\n$$수식$${d1}$$/수식$$, $$수식$${d2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a1} rm L `` {a2} rm {{mL}} - {b1} rm L `` {b2} rm {{mL}}$$/수식$$\n" \
              "$$수식$$ = {c1} rm L `` {c2} rm {{mL}} - {b1} rm L `` {b2} rm {{mL}} $$/수식$$\n$$수식$$ = {d1} rm L `` {d2} rm {{mL}}$$/수식$$\n\n"

    box1 = "$$수식$$box{　　}$$/수식$$"
    box2 = "$$수식$$box{　　　}$$/수식$$"

    while True:
        a1 = np.random.randint(3, 10)
        b1 = np.random.randint(1, 8)
        if a1 >= 2 + b1:
            break

    ab2 = random.sample(list(range(1, 10)), 2)
    ab2.sort()
    a2, b2 = ab2
    a2 = a2 * 100
    b2 = b2 * 100

    order = np.random.randint(0, 2)

    if order:
        a = '{a1} rm L `` {a2} rm {{mL}}'.format(a1=a1, a2=a2)
        b = '{b1} rm L `` {b2} rm {{mL}}'.format(b1=b1, b2=b2)
    else:
        b = '{a1} rm L `` {a2} rm {{mL}}'.format(a1=a1, a2=a2)
        a = '{b1} rm L `` {b2} rm {{mL}}'.format(b1=b1, b2=b2)

    c1 = a1 - 1
    c2 = a2 + 1000
    d1 = c1 - b1
    d2 = c2 - b2

    n1 = "%s" % a
    n2 = "%s" % b


    stem = stem.format(n1=n1, n2=n2, box1=box1, box2=box2)
    answer = answer.format(d1=d1, d2=d2)
    comment = comment.format(a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, d1=d1, d2=d2)

    return stem, answer, comment









































# 3-2-5-35
def sizeandweight325_Stem_021():
    stem = "약수터에서 {p1}는 $$수식$${a1} rm L `` {a2} rm {{mL}}$$/수식$$ 받아 왔고, {p2}는 $$수식$${b1} rm L `` {b2} rm {{mL}}$$/수식$$ 받아왔습니다. {p1}와 {p2}가 약수터에서 받아 온 물은 모두 몇 $$수식$$rm L$$/수식$$ 몇 $$수식$$rm {{mL}}$$/수식$$인가요?\n" \
        "{box1} $$수식$$rm L$$/수식$$ {box2} $$수식$$rm {{mL}}$$/수식$$"
    answer = "(정답)\n$$수식$${c1}$$/수식$$, $$수식$${c2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${p1}와 {p2}가 약수터에서 받아 온 물의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$${p1}가 받아 온 물의 양$$수식$$RIGHT ) + LEFT ($$/수식$${p2}가 받아 온 물의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {a1} rm L `` {a2} rm {{mL}} + {b1} rm L `` {b2} rm {{mL}}$$/수식$$\n" \
              "$$수식$$= {c1} rm L `` {c2} rm {{mL}}$$/수식$$\n\n"

    box1 = "$$수식$$box{　　}$$/수식$$"
    box2 = "$$수식$$box{　　　}$$/수식$$"

    p1, p2 = random.sample(['은지', '혁구', '영기', '상수', '은서', '동우', '재우', '진희', '준서', '유라', '수미', '현수',
                            '채아', '민주', '지호', '연아', '은우', '시우', '혁재', '민하'], 2)

    a1, b1 = random.sample(list(range(1, 6)), 2)

    while True:
        a2, b2 = random.sample(list(range(1, 9)), 2)
        if a2 + b2 <= 9:
            a2 = a2 * 100
            b2 = b2 * 100
            break

    c1 = a1 + b1
    c2 = a2 + b2


    stem = stem.format(p1=p1, p2=p2, a1=a1, a2=a2, b1=b1, b2=b2, box1=box1, box2=box2)
    answer = answer.format(c1=c1, c2=c2)
    comment = comment.format(p1=p1, p2=p2, a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2)

    return stem, answer, comment











































# 3-2-5-36
def sizeandweight325_Stem_022():
    stem = "㉠과 ㉡에 알맞은 수를 차례로 써 보세요.\n$$수식$${box1}$$/수식$$ $$수식$$`` rm L `` {a2} rm {{mL}} + {b1} rm L ``$$/수식$$ $$수식$${box2}$$/수식$$ $$수식$$`` rm {{mL}} = {c1} rm L `` {c2} rm {{mL}}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${b2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$rm {{mL}}$$/수식$$ 단위의 계산에서 $$수식$${a2} +$$/수식$$㉡$$수식$$= {d2}$$/수식$$, ㉡$$수식$$= {b2}$$/수식$$입니다.\n" \
              "$$수식$$rm L$$/수식$$ 단위의 계산에서 $$수식$$1 +$$/수식$$㉠$$수식$$+ {b1} = {c1}$$/수식$$, " \
              "$$수식$${d1} +$$/수식$$㉠$$수식$$= {c1}$$/수식$$, ㉠$$수식$$= {a1}$$/수식$$입니다.\n\n"


    box1 = "box{㉠````````````````````}"
    box2 = "box{㉡````````````````````}"

    a1, b1 = random.sample(list(range(1, 10)), 2)

    while True:
        a2, b2 = random.sample(list(range(1, 10)), 2)
        if (a2 + b2) >= 11:
            a2 = a2 * 100
            b2 = b2 * 100
            break

    c1 = 1 + a1 + b1
    c2 = a2 + b2 - 1000
    d1 = 1 + b1
    d2 = a2 + b2


    stem = stem.format(box1=box1, box2=box2, a2=a2, b1=b1, c1=c1, c2=c2)
    answer = answer.format(a1=a1, b2=b2)
    comment = comment.format(a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, d1=d1, d2=d2)

    return stem, answer, comment











































# 3-2-5-37
def sizeandweight325_Stem_023():
    stem = "물 $$수식$${a1} rm L `` {a2} rm {{mL}}$$/수식$$ 중 $$수식$${b1} rm L `` {b2} rm {{mL}}$$/수식$$를 사용하였습니다. 사용하고 남은 물은 몇 $$수식$$rm L$$/수식$$ 몇 $$수식$$rm {{mL}}$$/수식$$인가요?\n" \
        "{box1} $$수식$$rm L$$/수식$$ {box2} $$수식$$rm {{mL}}$$/수식$$"
    answer = "(정답)\n$$수식$${c1}$$/수식$$, $$수식$${c2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$사용하고 남은 물의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$$처음에 있던 물의 양$$수식$$RIGHT ) - LEFT ($$/수식$$사용한 물의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {a1} rm L `` {a2} rm {{mL}} - {b1} rm L `` {b2} rm {{mL}}$$/수식$$\n" \
              "$$수식$$= {c1} rm L `` {c2} rm {{mL}}$$/수식$$\n\n"

    box1 = "$$수식$$box{　　}$$/수식$$"
    box2 = "$$수식$$box{　　　}$$/수식$$"

    while True:
        a1, b1 = random.sample(list(range(1, 10)), 2)
        if a1 > b1:
            break

    while True:
        a2, b2 = random.sample(list(range(5, 96)), 2)
        if a2 > b2:
            a2 = a2 * 10
            b2 = b2 * 10
            break

    c1 = a1 - b1
    c2 = a2 - b2


    stem = stem.format(a1=a1, a2=a2, b1=b1, b2=b2, box1=box1, box2=box2)
    answer = answer.format(c1=c1, c2=c2)
    comment = comment.format(a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2)

    return stem, answer, comment











































# 3-2-5-38
def sizeandweight325_Stem_024():
    stem = "들이가 $$수식$${h} rm L$$/수식$$보다 적은 것을 찾아 기호를 써 보세요.\n$$표$$㉠ {p1}\n㉡ {p2}\n㉢ {p3}$$/표$$\n"
    answer = "(정답)\n{x}\n"
    comment = "(해설)\n" \
              "㉠ {q1}\n" \
              "㉡ {q2}\n" \
              "㉢ {q3}\n" \
              "따라서 들이가 $$수식$${h} rm L$$/수식$$보다 적은 것은 {x}입니다.\n\n"


    h = np.random.randint(3, 6)
    a = h - 1
    b1 = np.random.randint(2, 10 - a)
    a1 = a + b1

    while True:
        a2, b2 = random.sample(list(range(5, 96)), 2)
        if a2 > b2:
            a2 = a2 * 10
            b2 = b2 * 10
            break

    b = a2 - b2

    c = [h, h + 1][np.random.randint(0, 2)]
    d1 = np.random.randint(2, 10 - c)
    c1 = c + d1

    while True:
        c2, d2 = random.sample(list(range(5, 96)), 2)
        if c2 > d2:
            c2 = c2 * 10
            d2 = d2 * 10
            break

    d = c2 - d2

    e = [h, h + 1][np.random.randint(0, 2)]
    f1 = np.random.randint(2, 10 - e)
    e1 = e + f1

    while True:
        e2, f2 = random.sample(list(range(5, 96)), 2)
        if e2 > f2:
            e2 = e2 * 10
            f2 = f2 * 10
            break

    f = e2 - f2
    g = e1 * 1000 + e2


    temp = [["$$수식$${a1} rm L `` {a2} rm {{mL}} - {b1} rm L `` {b2} rm {{mL}}$$/수식$$".format(a1=a1, a2=a2, b1=b1, b2=b2),
             "$$수식$${a1} rm L `` {a2} rm {{mL}} - {b1} rm L `` {b2} rm {{mL}} = {a} rm L `` {b} rm {{mL}}$$/수식$$".format(a1=a1, a2=a2, b1=b1, b2=b2, a=a, b=b), True],
            ["$$수식$${c1} rm L `` {c2} rm {{mL}} - {d1} rm L `` {d2} rm {{mL}}$$/수식$$".format(c1=c1, c2=c2, d1=d1, d2=d2),
             "$$수식$${c1} rm L `` {c2} rm {{mL}} - {d1} rm L `` {d2} rm {{mL}} = {c} rm L `` {d} rm {{mL}}$$/수식$$".format(c1=c1, c2=c2, d1=d1, d2=d2, c=c, d=d), False],
            ["$$수식$${g} rm {{mL}} - {f1} rm L `` {f2} rm {{mL}}$$/수식$$".format(g=g, f1=f1, f2=f2),
             "$$수식$${g} rm {{mL}} - {f1} rm L `` {f2} rm {{mL}}$$/수식$$\n$$수식$$ = {e1} rm L `` {e2} rm {{mL}} - {f1} rm L `` {f2} rm {{mL}} = {e} rm L `` {f} rm {{mL}}$$/수식$$".format(g=g, f1=f1, f2=f2, e1=e1, e2=e2, e=e, f=f), False]]


    np.random.shuffle(temp)
    [[p1, q1, x1], [p2, q2, x2], [p3, q3, x3]] = temp

    xx = [x1, x2, x3]
    for i in range(0, len(xx)):
        if xx[i]:
            x = answer_kodict2[i]
            break


    stem = stem.format(h=h, p1=p1, p2=p2, p3=p3)
    answer = answer.format(x=x)
    comment = comment.format(q1=q1, q2=q2, q3=q3, x=x, h=h)

    return stem, answer, comment







































# 3-2-5-39
def sizeandweight325_Stem_025():
    stem = "{s1}에 {s2}을 $$수식$${a} rm {{mL}}$$/수식$$ 부은 다음 {s3}을 $$수식$${b1} rm L `` {b2} rm {{mL}}$$/수식$$ 더 부었습니다. {s1}에 부은 물의 양은 모두 몇 $$수식$$rm L$$/수식$$ 몇 $$수식$$rm {{mL}}$$/수식$$인가요?\n" \
        "{box1} $$수식$$rm L$$/수식$$ {box2} $$수식$$rm {{mL}}$$/수식$$"
    answer = "(정답)\n$$수식$${c}$$/수식$$, $$수식$${d}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${s1}에 부은 물의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$${s1}에 부은 {s2}의 양$$수식$$RIGHT ) + LEFT ($$/수식$${s1}에 부은 {s3}의 양$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {a} rm {{mL}} + {b1} rm L `` {b2} rm {{mL}}$$/수식$$\n" \
              "$$수식$$= {a1} rm L `` {a2} rm {{mL}} + {b1} rm L `` {b2} rm {{mL}}$$/수식$$\n" \
              "$$수식$$= {c1} rm L `` {c2} rm {{mL}}$$/수식$$\n" \
              "$$수식$$= {c} rm L `` {d} rm {{mL}}$$/수식$$\n\n"

    box1 = "$$수식$$box{　　}$$/수식$$"
    box2 = "$$수식$$box{　　　}$$/수식$$"
    
    s1 = ['욕조', '수조', '양동이'][np.random.randint(0, 3)]
    s2, s3 = [['찬물', '뜨거운 물'], ['뜨거운 물', '찬물']][np.random.randint(0, 2)]
    a1, b1 = random.sample(list(range(2, 6)), 2)

    while True:
        a2, b2 = random.sample(list(range(1, 10)), 2)
        if a2 + b2 >= 11:
            a2 = a2 * 100
            b2 = b2 * 100
            break


    a = a1 * 1000 + a2
    c1 = a1 + b1
    c2 = a2 + b2
    c = 1 + c1
    d = c2 - 1000


    stem = stem.format(s1=s1, s2=s2, s3=s3, a=a, b1=b1, b2=b2, box1=box1, box2=box2)
    answer = answer.format(c=c, d=d)
    comment = comment.format(s1=s1, s2=s2, s3=s3, a=a, b1=b1, b2=b2, a1=a1, a2=a2, c1=c1, c2=c2, c=c, d=d)

    return stem, answer, comment














































# 3-2-5-41
def sizeandweight325_Stem_026():
    stem = "들이가 가장 많은 것과 가장 적은 것의 들이의 차는 몇 $$수식$$rm {{mL}}$$/수식$$인가요?\n$$표$$$$수식$${a1} rm L `` {a2} rm {{mL}}$$/수식$$      $$수식$${b} rm {{mL}}$$/수식$$\n$$수식$${c1} rm L `` {c2} rm {{mL}}$$/수식$$      $$수식$${d} rm {{mL}}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${x} rm {{mL}}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a1} rm L `` {a2} rm {{mL}} = {a} rm {{mL}}$$/수식$$, $$수식$${c1} rm L `` {c2} rm {{mL}} = {c} rm {{mL}}$$/수식$$이고\n" \
              "$$수식$${e} rm {{mL}} &gt; {f} rm {{mL}} &gt; {g} rm {{mL}} &gt; {h} rm {{mL}}$$/수식$$입니다.\n" \
              "따라서 들이가 가장 많은 것과 적은 것의 들이의 차는\n" \
              "$$수식$${e} rm {{mL}} - {h} rm {{mL}} = {x} rm {{mL}}$$/수식$$입니다.\n\n"


    a1 = np.random.randint(3, 8)
    b1 = np.random.randint(a1 - 1, a1 + 2)
    c1 = [a1 - 1, a1 + 1][np.random.randint(0, 2)]
    d1 = np.random.randint(a1 - 1, a1 + 2)
    a2, b2, c2, d2 = random.sample(list(range(1, 10)), 4)

    a2 = a2 * 100
    b2 = b2 * 100
    c2 = c2 * 100
    d2 = d2 * 100

    a = a1 * 1000 + a2
    b = b1 * 1000 + b2
    c = c1 * 1000 + c2
    d = d1 * 1000 + d2

    nums = [a, b, c, d]
    nums.sort()
    h, g, f, e = nums
    x = e - h


    stem = stem.format(a1=a1, a2=a2, b=b, c1=c1, c2=c2, d=d)
    answer = answer.format(x=x)
    comment = comment.format(a1=a1, a2=a2, a=a, c1=c1, c2=c2, c=c, e=e, f=f, g=g, h=h, x=x)

    return stem, answer, comment












































# 3-2-5-51
def sizeandweight325_Stem_027():
    stem = "무게 단위 사이의 관계를 나타낸 것입니다. ㉠과 ㉡에 알맞은 수의 합은 얼마인가요?\n$$표$$∙ $$수식$${a} rm {{kg}} =$$/수식$$㉠$$수식$$rm t$$/수식$$\n∙ ㉡$$수식$$rm g = {d} rm {{kg}}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${e}$$/수식$$\n"
    comment = "(해설)\n" \
              "∙ $$수식$$1000 rm {{kg}} = 1 rm t$$/수식$$이므로 $$수식$${a} rm {{kg}} =$$/수식$$㉠$$수식$$rm t$$/수식$$에서 ㉠$$수식$$= {b}$$/수식$$입니다.\n" \
              "∙ $$수식$$1000 rm g = 1 rm {{kg}}$$/수식$$이므로 ㉡$$수식$$rm g = {d} rm {{kg}}$$/수식$$에서 ㉡$$수식$$= {c}$$/수식$$입니다.\n" \
              "따라서 ㉠$$수식$$+$$/수식$$㉡$$수식$$= {b} + {c} = {e}$$/수식$$입니다.\n\n"


    b, d = random.sample(list(range(2, 10)), 2)
    a = b * 1000
    c = d * 1000
    e = b + c


    stem = stem.format(a=a, d=d)
    answer = answer.format(e=e)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e)

    return stem, answer, comment










































# 3-2-5-52
def sizeandweight325_Stem_028():
    stem = "다음 무게가 몇 $$수식$$rm {{kg}}$$/수식$$ 몇 $$수식$$rm g$$/수식$$인지 쓰고, 몇 $$수식$$rm g$$/수식$$으로 나타내어 보세요.\n$$표$$$$수식$${a} rm {{kg}}$$/수식$$보다 $$수식$${b} rm g$$/수식$$ 더 무거운 무게$$/표$$\n" \
        "{box1} $$수식$$rm {{kg}}$$/수식$$ {box2} $$수식$$rm g$$/수식$$\n{box3} $$수식$$rm g$$/수식$$"
    answer = "(정답)\n$$수식$${a}$$/수식$$, $$수식$${b}$$/수식$$, $$수식$${d}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} rm {{kg}}$$/수식$$보다 $$수식$${b} rm g$$/수식$$ 더 무거운 무게는 $$수식$${a} rm {{kg}} `` {b} rm g$$/수식$$입니다.\n" \
              "$$수식$${a} rm {{kg}} `` {b} rm g = {c} rm g + {b} rm g = {d} rm g$$/수식$$\n\n"

    box1 = "$$수식$$box{　　}$$/수식$$"
    box2 = "$$수식$$box{　　　}$$/수식$$"
    box3 = "$$수식$$box{　　　　}$$/수식$$"

    a = np.random.randint(2, 10)
    b = np.random.randint(3, 20)

    b = b * 50
    c = a * 1000
    d = c + b


    stem = stem.format(a=a, b=b, box1=box1, box2=box2, box3=box3)
    answer = answer.format(a=a, b=b, d=d)
    comment = comment.format(a=a, b=b, c=c, d=d)

    return stem, answer, comment










































# 3-2-5-53
def sizeandweight325_Stem_029():
    stem = "무게가 같지 않은 것의 기호를 써 보세요.\n$$표$$㉠ $$수식$${p1}$$/수식$$\n㉡ $$수식$${p2}$$/수식$$\n㉢ $$수식$${p3}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{x}\n"
    comment = "(해설)\n" \
              "{x}. $$수식$${c} rm g = {d} rm g + {c3} rm g = {c1} rm {{kg}} + {c3} rm g = {c1} rm {{kg}} `` {c3} rm g$$/수식$$\n\n"


    a1 = np.random.randint(1, 10)
    a2 = np.random.randint(1, 10)
    a2 = a2 * 100
    a = a1 * 1000 + a2

    while True:
        b1 = np.random.randint(2, 10)
        if b1 != a1:
            break

    b = b1 * 1000

    while True:
        c1 = np.random.randint(1, 10)
        if c1 != a1 and c1 != b1:
            break

    if np.random.randint(0, 10) % 2 == 0:
        while True:
            c2 = np.random.randint(1, 10)
            c2 = c2 * 100
            if c2 != a2:
                c3 = int(c2 / 10)
                break

    else:
        while True:
            c2 = np.random.randint(1, 10)
            c2 = c2 * 10
            if c2 * 10 != a2:
                c3 = c2 * 10
                break

    c = c1 * 1000 + c3
    d = c1 * 1000

    x1 = "{a1} rm {{kg}} `` {a2} rm g = {a} rm g".format(a=a, a1=a1, a2=a2)
    x2 = "{b} rm {{kg}} = {b1} rm t".format(b=b, b1=b1)
    x3 = "{c} rm g = {c1} rm {{kg}} `` {c2} rm g".format(c=c, c1=c1, c2=c2)
    xx = [[x1, False], [x2, False], [x3, True]]
    np.random.shuffle(xx)

    p1, p2, p3 = xx[0][0], xx[1][0], xx[2][0]

    for i in range(0, len(xx)):
        if xx[i][1]:
            x = answer_kodict[i]
            break


    stem = stem.format(p1=p1, p2=p2, p3=p3)
    answer = answer.format(x=x)
    comment = comment.format(x=x, c=c, d=d, c1=c1, c3=c3)

    return stem, answer, comment












































# 3-2-5-55
def sizeandweight325_Stem_030():
    stem = "□ 안에 들어갈 알맞은 수를 구하세요.\n$$수식$$LEFT ( 1 RIGHT ) ```` {a} rm {{kg}} = $$/수식$$ $$수식$${box}$$/수식$$ $$수식$$rm g$$/수식$$\n$$수식$$LEFT ( 2 RIGHT ) ```` {b} rm g = $$/수식$$ $$수식$${box}$$/수식$$ $$수식$$rm {{kg}} ```` $$/수식$$ $$수식$${box}$$/수식$$ $$수식$$rm g$$/수식$$\n"
    answer = "(정답)\n$$수식$${A}$$/수식$$, $$수식$${b1}$$/수식$$, $$수식$${b2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1 RIGHT ) ```` 1 rm {{kg}} = 1000 rm g$$/수식$$이므로 " \
              "$$수식$${a} rm {{kg}} = {A} rm g$$/수식$$\n" \
              "$$수식$$LEFT ( 2 RIGHT ) ```` {b} rm g = {b3} rm g + {b2} rm g = {b1} rm {{kg}} + {b2} rm g = {b1} rm {{kg}} `` {b2} rm g$$/수식$$\n\n"


    box = "box{　　　}"

    a = np.random.randint(3, 10)
    A = a * 1000

    while True:
        b1 = np.random.randint(2, 10)
        if b1 != a:
            break

    b2 = np.random.randint(3, 20)
    b2 = b2 * 50
    b3 = b1 * 1000
    b = b3 + b2


    stem = stem.format(a=a, b=b, box=box)
    answer = answer.format(A=A, b1=b1, b2=b2)
    comment = comment.format(a=a, A=A, b=b, b1=b1, b2=b2, b3=b3)

    return stem, answer, comment














































# 3-2-5-56
def sizeandweight325_Stem_031():
    stem = "{p}는 $$수식$${a} rm {{kg}}$$/수식$$의 {s1}이 담긴 {s2}에 $$수식$${b} rm g$$/수식$$의 {s1}을 더 넣었습니다. {s2}에 담긴 {s1}의 무게는 모두 몇 $$수식$$rm g$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${d} rm g$$/수식$$\n"
    comment = "(해설)\n" \
              "{s2}에 담긴 {s1}의 무게는 $$수식$${a} rm {{kg}}$$/수식$$보다 $$수식$${b} rm g$$/수식$$ 더 무거우므로 $$수식$${a} rm {{kg}} `` {b} rm g$$/수식$$입니다.\n" \
              "$$수식$${a} rm {{kg}} `` {b} rm g = {a} rm {{kg}} + {b} rm g = {c} rm g + {b} rm g = {d} rm g$$/수식$$\n\n"


    p = ['은지', '혁구', '영기', '상수', '은서', '동우', '재우', '진희', '준서', '유라', '수미', '현수',
         '채아', '민주', '지호', '연아', '은우', '시우', '혁재', '민하'][np.random.randint(0, 20)]

    s1 = ['콩', '쌀', '완두콩', '강낭콩', '팥', '좁쌀', '보리쌀'][np.random.randint(0, 7)]
    s2 = ['봉지', '통', '주머니', '상자'][np.random.randint(0, 4)]

    a = np.random.randint(2, 6)
    b = np.random.randint(1, 10)

    b = b * 100
    c = a * 1000

    d = c + b


    stem = stem.format(p=p, a=a, b=b, s1=s1, s2=s2)
    answer = answer.format(d=d)
    comment = comment.format(a=a, b=b, c=c, d=d, s2=s2, s1=s1)

    return stem, answer, comment

















































# 3-2-5-57
def sizeandweight325_Stem_032():
    stem = "$$수식$${a} rm {{kg}}$$/수식$$의 {s}{jo1} 들어 있는 상자에 $$수식$${b} rm g$$/수식$$의 {s}{jo2} 한 개 더 담았습니다. 상자에 있는 {s}의 무게는 모두 몇 $$수식$$rm {{kg}}$$/수식$$ 몇 $$수식$$rm g$$/수식$$인지 쓰고, 몇 $$수식$$rm g$$/수식$$으로 나타내어 보세요.\n"
    answer = "(정답)\n$$수식$${a} rm {{kg}} `` {b} rm g$$/수식$$, $$수식$${d} rm g$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} rm {{kg}}$$/수식$$보다 $$수식$${b} rm g$$/수식$$ 더 무거운 무게는 $$수식$${a} rm {{kg}} `` {b} rm g$$/수식$$입니다.\n" \
              "$$수식$${a} rm {{kg}} `` {b} rm g = {a} rm {{kg}} + {b} rm g = {c} rm g + {b} rm g = {d} rm g$$/수식$$\n\n"


    s = ['감자', '고구마', '옥수수', '귤', '토마토'][np.random.randint(0, 5)]

    jo1 = proc_jo(s, 0)
    jo2 = proc_jo(s, 1)

    a = np.random.randint(4, 10)
    b = np.random.randint(25, 46) * 5

    c = a * 1000
    d = c + b


    stem = stem.format(s=s, jo1=jo1, jo2=jo2, a=a, b=b)
    answer = answer.format(a=a, b=b, d=d)
    comment = comment.format(a=a, b=b, c=c, d=d)

    return stem, answer, comment










































# 3-2-5-58
def sizeandweight325_Stem_033():
    stem = "$$수식$${a} rm t$$/수식$$까지 실을 수 있는 {s1}가 있습니다. 이 {s1}에 무게가 $$수식$${b} rm {{kg}}$$/수식$$인 {s2}{jo} 몇 개까지 실을 수 있나요?\n"
    answer = "(정답)\n$$수식$${d}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$${a} rm t = {c} rm {{kg}}$$/수식$$입니다.\n" \
              "$$수식$${b} rm {{kg}}$$/수식$$의  $$수식$${d}$$/수식$$배가  $$수식$${c} rm {{kg}}$$/수식$$이므로 " \
              "$$수식$${b} rm {{kg}}$$/수식$$의 {s2}{jo} $$수식$${d}$$/수식$$개까지 실을 수 있습니다.\n\n"


    s1 = ['엘리베이터', '화물차', '지게차'][np.random.randint(0, 3)]
    s2 = ['상자', '물건', '짐'][np.random.randint(0, 3)]

    jo = proc_jo(s2, 1)

    a = np.random.randint(5, 10)
    b = [a, a * 10, a * 100][np.random.randint(0, 3)]
    c = a * 1000
    d = int(c / b)


    stem = stem.format(a=a, b=b, s1=s1, s2=s2, jo=jo)
    answer = answer.format(d=d)
    comment = comment.format(a=a, b=b, c=c, d=d, s2=s2, jo=jo)

    return stem, answer, comment







































# 3-2-5-59
def sizeandweight325_Stem_034():
    stem = "무게가 가장 가벼운 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${a1} rm {{kg}} `` {a2} rm g$$/수식$$     ㉡ $$수식$${b} rm g$$/수식$$\n㉢ $$수식$${c1} rm {{kg}} `` {c2} rm g$$/수식$$     ㉣ $$수식$${d} rm g$$/수식$$$$/표$$\n"
    answer = "(정답)\n{x}\n"
    comment = "(해설)\n" \
              "단위를 모두 통일하여 무게를 비교합니다.\n" \
              "㉠ $$수식$${a1} rm {{kg}} `` {a2} rm g = {a} rm g$$/수식$$, ㉢ $$수식$${c1} rm {{kg}} `` {c2} rm g = {c} rm g$$/수식$$\n" \
              "따라서 $$수식$${e} rm g &lt; {f} rm g &lt; {g} rm g &lt; {h} rm g$$/수식$$이므로\n" \
              "무게가 가장 가벼운 것은 {x}입니다.\n\n"


    a1 = np.random.randint(3, 10)
    b1 = a1
    c1 = a1
    d1 = a1

    a2 = np.random.randint(1, 19) * 50
    while True:
        b2 = np.random.randint(1, 10) * 100
        if b2 != a2:
            break

    while True:
        c2 = np.random.randint(1, 10) * 100
        if c2 != a2 and c2 != b2:
            break

    while True:
        d2 = np.random.randint(5, 91) * 10
        if d2 != a2 and d2 != b2 and d2 != c2:
            break

    a = a1 * 1000 + a2
    b = b1 * 1000 + b2
    c = c1 * 1000 + c2
    d = d1 * 1000 + d2

    nums = [a, b, c, d]
    nums_cp = nums.copy()
    nums_cp.sort()
    e, f, g, h = nums_cp

    for i in range(0, len(nums)):
        if nums[i] == e:
            x = answer_kodict2[i]
            break


    stem = stem.format(a1=a1, a2=a2, b=b, c1=c1, c2=c2, d=d)
    answer = answer.format(x=x)
    comment = comment.format(a=a, a1=a1, a2=a2, c=c, c1=c1, c2=c2, e=e, f=f, g=g, h=h, x=x)

    return stem, answer, comment









































# 3-2-5-60
def sizeandweight325_Stem_035():
    stem = "무게가 $$수식$$1 rm t$$/수식$$보다 무거운 것을 찾아 기호를 써 보세요.\n$$표$$㉠ {p1}     ㉡ {p2}\n㉢ {p3}     ㉣ {p4}$$/표$$\n"
    answer = "(정답)\n{x}\n"
    comment = "(해설)\n" \
              "{x}. {a}{jo} $$수식$$1 rm t$$/수식$$보다 무겁습니다.\n\n"


    a = ['버스 1대', '트럭 1대', '비행기 1대', '여객선 1척', '코끼리 1마리', '흰수염고래 1마리', '코뿔소 1마리'][np.random.randint(0, 7)]

    jo = proc_jo(a, -1)

    b, c, d = random.sample(['냉장고 1대', '자전거 3대', '의자 1개', '사과 5상자', '책상 1개',
                             '책 10권', 'TV 1대', '세탁기 1대', '아령 3개', '킥보드 5대',
                             '농구공 10개', '식탁 1개', '소화기 1개', '연필 500자루', '모니터 10대', '친구 5명'], 3)

    p = [[a, True], [b, False], [c, False], [d, False]]
    np.random.shuffle(p)
    p1, p2, p3, p4 = p[0][0], p[1][0], p[2][0], p[3][0]

    for i in range(0, len(p)):
        if p[i][1]:
            x = answer_kodict2[i]
            break


    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4)
    answer = answer.format(x=x)
    comment = comment.format(x=x, a=a, jo=jo)

    return stem, answer, comment









































# 3-2-5-63
def sizeandweight325_Stem_036():
    stem = "다음 물건을 선택하여 문장을 완성해보세요.\n$$표$${p1}     {p2}     {p3}$$/표$$\n$$수식$$LEFT ( 1 RIGHT )$$/수식$$ $$수식$${box}$$/수식$$의 무게는 약 $$수식$${a} rm t$$/수식$$입니다.\n$$수식$$LEFT ( 2 RIGHT )$$/수식$$ $$수식$${box}$$/수식$$의 무게는 약 $$수식$${b} rm g$$/수식$$입니다.\n"
    answer = "(정답)\n{s1}, {s2}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1 RIGHT )$$/수식$$ {c}\n" \
              "$$수식$$LEFT ( 2 RIGHT )$$/수식$$ {d}\n\n"


    box = "box{　　　　}"

    a1 = '무게가 $$수식$$150 rm t$$/수식$$으로 적당한 것은 비행기입니다.'
    a2 = '무게가 $$수식$$6 rm t$$/수식$$으로 적당한 것은 코끼리입니다.'
    a3 = '무게가 $$수식$$2 rm t$$/수식$$으로 적당한 것은 코뿔소입니다.'
    a4 = '무게가 $$수식$$14 rm t$$/수식$$으로 적당한 것은 버스입니다.'
    a5 = '무게가 $$수식$$55 rm t$$/수식$$으로 적당한 것은 탱크입니다.'

    b1 = '무게가 $$수식$$200 rm g$$/수식$$으로 적당한 것은 스마트폰입니다.'
    b2 = '무게가 $$수식$$300 rm g$$/수식$$으로 적당한 것은 사과입니다.'
    b3 = '무게가 $$수식$$250 rm g$$/수식$$으로 적당한 것은 한라봉입니다.'
    b4 = '무게가 $$수식$$5 rm g$$/수식$$으로 적당한 것은 연필입니다.'
    b5 = '무게가 $$수식$$450 rm g$$/수식$$으로 적당한 것은 머그컵입니다.'

    a, s1, c = [[150, '비행기', a1], [6, '코끼리', a2], [2, '코뿔소', a3], [14, '버스', a4], [55, '탱크', a5]][
        np.random.randint(0, 5)]
    b, s2, d = [[200, '스마트폰', b1], [300, '사과', b2], [250, '한라봉', b3], [5, '연필', b4], [450, '머그컵', b5]][
        np.random.randint(0, 5)]
    s3 = ['냉장고', '텔레비전', '수박', '의자', '책상', '세탁기'][np.random.randint(0, 6)]

    p = [s1, s2, s3]
    np.random.shuffle(p)
    p1, p2, p3 = p


    stem = stem.format(p1=p1, p2=p2, p3=p3, a=a, b=b, box=box)
    answer = answer.format(s1=s1, s2=s2)
    comment = comment.format(c=c, d=d)

    return stem, answer, comment












































# 3-2-5-64
def sizeandweight325_Stem_037():
    stem = "다음 중 무게를 $$수식$$rm t$$/수식$$ 단위를 사용하기에 알맞은 것은 어느 것인가요?\n① {p1}     ② {p2}     ③ {p3} \n④ {p4}     ⑤ {p5}\n"
    answer = "(정답)\n{x}\n"
    comment = "(해설)\n" \
              "{a}, {b}의 무게는 $$수식$$rm g$$/수식$$ 단위를 사용하기에 알맞습니다.\n" \
              "{c}, {d}의 무게는 $$수식$$rm {{kg}}$$/수식$$ 단위를 사용하기에 알맞습니다.\n" \
              "{e}의 무게는 $$수식$$rm t$$/수식$$ 단위를 사용하기에 알맞습니다.\n\n"


    a, b = random.sample(['탁구공', '테니스공', '동화책', '수학책', '연필', '지우개', '필통', '귤', '복숭아', '토마토',
                          '밤', '콩', '호두', '숟가락', '컵', '스마트폰'], 2)

    c, d = random.sample(['텔레비전', '냉장고', '세탁기', '에어컨', '모니터', '책상', '의자', '식탁', '백과사전', '자전거',
                          '수박', '멜론', '책가방'], 2)

    e = ['하마', '코뿔소', '코끼리', '고래', '버스', '트럭', '탱크', '비행기', '여객선'][np.random.randint(0, 9)]

    p = [[a, False], [b, False], [c, False], [d, False], [e, True]]
    np.random.shuffle(p)

    p1, p2, p3, p4, p5 = p[0][0], p[1][0], p[2][0], p[3][0], p[4][0]

    for i in range(0, len(p)):
        if p[i][1]:
            x = answer_dict[i]


    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5)
    answer = answer.format(x=x)
    comment = comment.format(a=a, b=b, c=c, d=d, e=e)

    return stem, answer, comment







































# 3-2-5-66
def sizeandweight325_Stem_038():
    stem = "{p}의 몸무게는 $$수식$${a} rm {{kg}}$$/수식$$입니다. $$수식$${b} rm t$$/수식$$의 무게는 {p}의 몸무게의 약 몇 배인가요?\n"
    answer = "(정답)\n약 $$수식$${x}$$/수식$$배\n"
    comment = "(해설)\n" \
              "$$수식$${b} rm t = {c} rm {{kg}}$$/수식$$이므로 {p}의 몸무게를 기준으로 " \
              "$$수식$$2$$/수식$$배, $$수식$$3$$/수식$$배$$수식$$CDOTS CDOTS$$/수식$$의 무게를 생각합니다.\n" \
              "$$수식$$CDOTS CDOTS {a} TIMES {d} = {f}$$/수식$$, $$수식$${a} TIMES {e} = {g} CDOTS CDOTS$$/수식$$이므로\n" \
              "$$수식$${b} rm t$$/수식$$의 무게는 {p}의 몸무게 $$수식$${a} rm {{kg}}$$/수식$$의 약 $$수식$${x}$$/수식$$배입니다.\n\n"


    p = ['은지', '혁구', '영기', '상수', '은서', '동우', '재우', '진희', '준서', '유라', '수미', '현수',
         '채아', '민주', '지호', '연아', '은우', '시우', '혁재', '민하'][np.random.randint(0, 20)]


    while True:
        while True:
            a = [35, 45, 55][np.random.randint(0, 3)]
            b = np.random.randint(2, 6)
            if b < a / 10:
                break

        c = b * 1000
        d = int(c / a)
        e = d + 1
        f = a * d
        g = a * e

        if c - f < g - c:
            x = d
            break

        elif c - f > g - c:
            x = e
            break

        else:
            continue


    stem = stem.format(p=p, a=a, b=b)
    answer = answer.format(x=x)
    comment = comment.format(p=p, a=a, b=b, c=c, d=d, e=e, f=f, g=g, x=x)

    return stem, answer, comment




































# 3-2-5-67
def sizeandweight325_Stem_039():
    stem = "무게의 단위를 잘못 사용한 학생은 누구인가요?\n$$표$${p1}: {can1}\n{p2}: {can2}\n{p3}: {can3}$$/표$$\n"
    answer = "(정답)\n{x}\n"
    comment = "(해설)\n" \
              "{d}\n\n"


    a1_num = np.random.randint(45, 55)
    a1_who = ["어머니", "할머니", "고모", "이모"][np.random.randint(0, 4)]

    a2_room = ["집", "방", "거실"][np.random.randint(0, 3)]
    a2_elec = ["선풍기", "공기청정기", "청소기"][np.random.randint(0, 3)]

    a3_who = ["아버지", "할아버지"][np.random.randint(0, 2)]
    a3_thing = ["수족관", "어항", "책상"][np.random.randint(0, 3)]

    a5_thing = ["고구마", "감자", "당근", "배추", "양파", "양배추"][np.random.randint(0, 6)]

    a1 = '%s의 몸무게는 $$수식$$%d rm {{kg}}$$/수식$$이야.' % (a1_who, a1_num)
    a2 = '%s에 있는 %s의 무게는 $$수식$$5 rm {{kg}}$$/수식$$이야.' % (a2_room, a2_elec)
    a3 = '%s께서 $$수식$$30 rm {{kg}}$$/수식$$이나 되는 %s을 혼자 옮기셨어.' % (a3_who, a3_thing)
    a4 = '$$수식$$2 rm {{kg}}$$/수식$$짜리 생수 $$수식$$6$$/수식$$통을 들고 오느라 힘들었어.'
    a5 = '시골에서 %s $$수식$$10 rm {{kg}}$$/수식$$을 택배로 보내셨대.' % a5_thing

    b1_bird = ["벌새", "참새", "종달새"][np.random.randint(0, 3)]

    b2_shoes = ["운동화", "실내화", "슬리퍼"][np.random.randint(0, 3)]

    b3_fruit = ["배", "사과", "참외", "복숭아"][np.random.randint(0, 4)]
    b3_box = ["상자", "바구니", "통"][np.random.randint(0, 3)]

    b5_meat = ["돼지고기", "소고기", "닭고기"][np.random.randint(0, 3)]

    b1 = '%s는 무게가 $$수식$$10 rm g$$/수식$$ 정도밖에 안 된대.' % b1_bird
    b2 = '내 %s는 $$수식$$250 rm g$$/수식$$으로 무척 가벼워.' % b2_shoes
    b3 = '한 개에 $$수식$$600 rm g$$/수식$$ 정도 하는 %s가 한 %s에 $$수식$$6$$/수식$$개 들어 있어.' % (b3_fruit, b3_box)
    b4 = '배드민턴공은 무게가 겨우 $$수식$$5 rm g$$/수식$$이야.'
    b5 = '마트에서 한 명당 %s $$수식$$600 rm g$$/수식$$을 할인해서 판매한대.' % b5_meat

    c1_who = ["삼촌", "이모부", "고모부", "선생님"][np.random.randint(0, 4)]
    c1_weight = np.random.randint(68, 79)

    c2_animal = ["코끼리", "코뿔소", "고래", "기린"][np.random.randint(0, 4)]
    c2_weight = np.random.randint(2, 6)

    c3_who = ["어머니", "할머니"][np.random.randint(0, 2)]
    c3_thing = ["소고기", "돼지고기"][np.random.randint(0, 2)]
    c3_weight = np.random.randint(1, 3)

    c4_weight = np.random.randint(5, 11)
    c4_fruit = ["귤", "딸기", "포도"][np.random.randint(0, 3)]

    c5_pen = ["샤프", "연필", "볼펜"][np.random.randint(0, 3)]
    c5_weight = np.random.randint(14, 17)

    c1 = '%s의 몸무게는 $$수식$$%d rm g$$/수식$$이야.' % (c1_who, c1_weight)
    c2 = 'TV에서 $$수식$$%d rm {{kg}}$$/수식$$이나 되는 %s를 보았어.' % (c2_weight, c2_animal)
    c3 = '%s께서 %s를 $$수식$$%d rm g$$/수식$$ 사 오셨어.' % (c3_who, c3_thing, c3_weight)
    c4 = '$$수식$$%d rm t$$/수식$$짜리 %s 한 상자를 샀어.' % (c4_weight, c4_fruit)
    c5 = '내가 쓰는 %s의 무게는 $$수식$$%d rm {{kg}}$$/수식$$이야.' % (c5_pen, c5_weight)

    d1 = '%s의 몸무게로 $$수식$$%d rm g$$/수식$$은 맞지 않습니다. $$수식$$%d rm {{kg}}$$/수식$$이 적절합니다.' % (c1_who, c1_weight, c1_weight)
    d2 = '%s의 무게로 $$수식$$%d rm {{kg}}$$/수식$$은 맞지 않습니다. $$수식$$%d rm t$$/수식$$이 적절합니다.' % (c2_animal, c2_weight, c2_weight)
    d3 = '%s $$수식$$%d rm g$$/수식$$은 매우 적은 양입니다. $$수식$$%d rm {{kg}}$$/수식$$이 적절합니다.' % (c3_thing, c3_weight, c3_weight)
    d4 = '%s $$수식$$%d rm t$$/수식$$은 엄청나게 많은 양입니다. $$수식$$%d rm {{kg}}$$/수식$$이 적절합니다.' % (c4_fruit, c4_weight, c4_weight)
    d5 = '%s의 무게로 $$수식$$%d rm {{kg}}$$/수식$$은 맞지 않습니다. $$수식$$%d rm g$$/수식$$이 적절합니다.' % (c5_pen, c5_weight, c5_weight)

    p = random.sample(['은지', '혁구', '영기', '상수', '은서', '동우', '재우', '진희', '준서', '유라', '수미', '현수',
                       '채아', '민주', '지호', '연아', '은우', '시우', '혁재', '민하'], 3)

    p1, p2, p3 = p

    a = [a1, a2, a3, a4, a5][np.random.randint(0, 5)]
    b = [b1, b2, b3, b4, b5][np.random.randint(0, 5)]
    c, d = [[c1, d1], [c2, d2], [c3, d3], [c4, d4], [c5, d5]][np.random.randint(0, 5)]

    candidates = [a, b, c]
    np.random.shuffle(candidates)
    can1, can2, can3 = candidates

    for i in range(0, len(candidates)):
        if candidates[i] == c:
            x = p[i]


    stem = stem.format(p1=p1, p2=p2, p3=p3, can1=can1, can2=can2, can3=can3)
    answer = answer.format(x=x)
    comment = comment.format(d=d)

    return stem, answer, comment














































# 3-2-5-70
def sizeandweight325_Stem_040():
    stem = "무게가 더 무거운 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${a1} rm {{kg}} `` {a2} rm g + {b1} rm {{kg}} `` {b2} rm g$$/수식$$\n㉡ $$수식$${c1} rm {{kg}} `` {c2} rm g + {d} rm g$$/수식$$$$/표$$\n"
    answer = "(정답)\n{y}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${a1} rm {{kg}} `` {a2} rm g + {b1} rm {{kg}} `` {b2} rm g " \
              "= {A1} rm {{kg}} `` {B1} rm g = {A2} rm {{kg}} `` {B2} rm g$$/수식$$\n" \
              "㉡ $$수식$${c1} rm {{kg}} `` {c2} rm g + {d} rm g = {c1} rm {{kg}} `` {c2} rm g + {d1} rm {{kg}} ``{d2} rm g $$/수식$$\n" \
              "$$수식$$ = {C1} rm {{kg}} `` {D1} rm g = {C2} rm {{kg}} `` {D2} rm g$$/수식$$\n" \
              "따라서 $$수식$${A2} rm {{kg}} {B2} rm g {x} {C2} rm {{kg}} `` {D2} rm g$$/수식$$이므로\n무게가 더 무거운 것은 {y}입니다.\n\n"


    while True:
        a1 = np.random.randint(1, 8)
        b1 = np.random.randint(1, 8)
        a2 = np.random.randint(2, 10) * 100
        b2 = np.random.randint(2, 10) * 100
        c1 = np.random.randint(1, 8)
        d1 = np.random.randint(1, 8)
        c2 = np.random.randint(1, 10) * 100
        d2 = np.random.randint(1, 10) * 100
        if a1 + b1 <= 8 and a2 + b2 >= 1100 and a2 != b2 and c1 + d1 == a1 + b1 and c1 != a1 and c2 + d2 >= 1100 and c2 + d2 != a2 + b2 and c2 != a2:
            break

    d = d1 * 1000 + d2
    A1 = a1 + b1
    B1 = a2 + b2
    A2 = A1 + 1
    B2 = B1 - 1000

    C1 = c1 + d1
    D1 = c2 + d2
    C2 = C1 + 1
    D2 = D1 - 1000

    if B2 > D2:
        x = '&gt;'
        y = '㉠'
    else:
        x = '&lt;'
        y = '㉡'


    stem = stem.format(a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, d=d)
    answer = answer.format(y=y)
    comment = comment.format(a1=a1, a2=a2, b1=b1, b2=b2, A1=A1, A2=A2, B1=B1, B2=B2,
                             c1=c1, c2=c2, d=d, d1=d1, d2=d2, C1=C1, C2=C2, D1=D1, D2=D2, y=y, x=x)

    return stem, answer, comment







































# 3-2-5-71
def sizeandweight325_Stem_041():
    stem = "무게가 가장 무거운 것과 가장 가벼운 것의 무게의 합은 몇 $$수식$$rm {{kg}}$$/수식$$ 몇 $$수식$$rm g$$/수식$$인가요?\n$$표$$$$수식$${p1}$$/수식$$     $$수식$${p2}$$/수식$$\n$$수식$${p3}$$/수식$$     $$수식$${p4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${e1} rm {{kg}} `` {e2} rm g$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${b} rm g = {b1} rm {{kg}} `` {b2} rm g$$/수식$$, " \
              "$$수식$${d} rm g = {d1} rm {{kg}} `` {d2} rm g$$/수식$$이므로\n" \
              "$$수식$${d1} rm {{kg}} `` {d2} rm g &gt; {c1} rm {{kg}} `` {c2} rm g &gt; {b1} rm {{kg}} `` {b2} rm g &gt; {a1} rm {{kg}} `` {a2} rm g$$/수식$$입니다.\n" \
              "따라서 무게가 가장 무거운 것과 가장 가벼운 것의 무게의 합은\n" \
              "$$수식$${d1} rm {{kg}} `` {d2} rm g + {a1} rm {{kg}} `` {a2} rm g = {e1} rm {{kg}} `` {e2} rm g$$/수식$$입니다.\n\n"


    while True:
        a1 = np.random.randint(2, 8)
        a2 = np.random.randint(1, 10) * 50

        b1 = [a1, a1 + 1][np.random.randint(0, 2)]
        b2 = np.random.randint(1, 20) * 50

        c1 = b1 + 1
        c2 = np.random.randint(1, 10) * 50

        d1 = c1 + 1
        d2 = np.random.randint(1, 10) * 50

        if b2 >= a2 + 50 and d2 >= c2 + 50:
            break


    b = b1 * 1000 + b2
    d = d1 * 1000 + d2
    e1 = d1 + a1
    e2 = d2 + a2

    p = ['{a1} rm {{kg}} `` {a2} rm g'.format(a1=a1, a2=a2), '{b} rm g'.format(b=b),
         '{c1} rm {{kg}} `` {c2} rm g'.format(c1=c1, c2=c2), '{d} rm g'.format(d=d)]

    np.random.shuffle(p)
    p1, p2, p3, p4 = p


    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4)
    answer = answer.format(e1=e1, e2=e2)
    comment = comment.format(a1=a1, a2=a2, b=b, b1=b1, b2=b2, c1=c1, c2=c2, d=d, d1=d1, d2=d2, e1=e1, e2=e2)

    return stem, answer, comment









































# 3-2-5-73
def sizeandweight325_Stem_042():
    stem = "□ 안에 들어갈 알맞은 수를 차례로 구하세요.\n$$수식$$LEFT ( 1 RIGHT ) ```` {a} rm g + {b} rm g = $$/수식$$ $$수식$${box}$$/수식$$ $$수식$$rm g = $$/수식$$ $$수식$${box}$$/수식$$ $$수식$$rm {{kg}} `` $$/수식$$ $$수식$${box}$$/수식$$ $$수식$$rm g$$/수식$$\n$$수식$$LEFT ( 2 RIGHT ) ```` {c1} rm {{kg}} `` {c2} rm g - {d1} rm {{kg}} `` {d2} rm g = $$/수식$$ $$수식$${box}$$/수식$$ $$수식$$rm {{kg}} `` $$/수식$$ $$수식$${box}$$/수식$$ $$수식$$rm g$$/수식$$\n"
    answer = "(정답)\n$$수식$${e}$$/수식$$, $$수식$${e1}$$/수식$$, $$수식$${e2}$$/수식$$, " \
             "$$수식$${c}$$/수식$$, $$수식$${d}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ( 1 RIGHT ) ```` {a} rm g + {b} rm g = {e} rm g = {e1} rm {{kg}} `` {e2} rm g$$/수식$$\n" \
              "$$수식$$LEFT ( 2 RIGHT ) ```` {c1} rm {{kg}} `` {c2} rm g - {d1} rm {{kg}} `` {d2} rm g = {c} rm {{kg}} `` {d} rm g$$/수식$$\n\n"


    while True:
        a1, b1 = random.sample(list(range(2, 8)), 2)
        if a1 + b1 <= 9:
            break

    while True:
        a2, b2 = random.sample(list(range(1, 9)), 2)
        if a2 + b2 <= 9:
            a2 = a2 * 100
            b2 = b2 * 100
            break

    a = a1 * 1000 + a2
    b = b1 * 1000 + b2
    e = a + b

    e1 = a1 + b1
    e2 = a2 + b2
    cd1 = random.sample(list(range(1, 10)), 2)
    cd1.sort()
    d1, c1 = cd1
    cd2 = random.sample(list(range(1, 10)), 2)
    cd2.sort()

    d2, c2 = cd2
    c2 = c2 * 100
    d2 = d2 * 100
    c = c1 - d1
    d = c2 - d2

    box = "box{　　　}"


    stem = stem.format(box=box, a=a, b=b, c1=c1, c2=c2, d1=d1, d2=d2)
    answer = answer.format(e=e, e1=e1, e2=e2, c=c, d=d)
    comment = comment.format(a=a, b=b, e=e, e1=e1, e2=e2, c1=c1, c2=c2, d1=d1, d2=d2, c=c, d=d)

    return stem, answer, comment








































# 3-2-5-75
def sizeandweight325_Stem_043():
    stem = "가장 무거운 무게와 가장 가벼운 무게의 차는 몇 $$수식$$rm {{kg}}$$/수식$$ 몇 $$수식$$rm g$$/수식$$인가요?\n$$표$$$$수식$${p1}$$/수식$$     $$수식$${p2}$$/수식$$     $$수식$${p3}$$/수식$$$$/표$$\n" \
        "{box1} $$수식$$rm {{kg}}$$/수식$$ {box2} $$수식$$rm g$$/수식$$"
    answer = "(정답)\n$$수식$${d1}$$/수식$$, $$수식$${d2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${c} rm g = {c1} rm {{kg}} `` {c2} rm g$$/수식$$이므로\n" \
              "$$수식$${a1} rm {{kg}} `` {a2} rm g &gt; {b1} rm {{kg}} `` {b2} rm g &gt; {c1} rm {{kg}} `` {c2} rm g$$/수식$$입니다.\n" \
              "따라서 가장 무거운 무게와 가장 가벼운 무게의 차는\n" \
              "$$수식$${a1} rm {{kg}} `` {a2} rm g - {c1} rm {{kg}} `` {c2} rm g = {d1} rm {{kg}} `` {d2} rm g$$/수식$$입니다.\n\n"

    box1 = "$$수식$$box{　　}$$/수식$$"
    box2 = "$$수식$$box{　　　　}$$/수식$$"
    
    a1 = np.random.randint(4, 10)
    a2 = np.random.randint(4, 10) * 100
    b1 = [a1, a1 - 1][np.random.randint(0, 2)]
    c1 = b1 - 1

    while True:
        b2, c2 = random.sample(list(range(2, 9)), 2)
        b2 = b2 * 100
        c2 = c2 * 100
        if b2 <= a2 - 100 and c2 <= a2 - 100:
            break

    c = c1 * 1000 + c2
    d1 = a1 - c1
    d2 = a2 - c2

    p = ['{a1} rm {{kg}} `` {a2} rm g'.format(a1=a1, a2=a2),
         '{b1} rm {{kg}} `` {b2} rm g'.format(b1=b1, b2=b2),
         '{c} rm g'.format(c=c)]

    np.random.shuffle(p)
    p1, p2, p3 = p


    stem = stem.format(p1=p1, p2=p2, p3=p3, box1=box1, box2=box2)
    answer = answer.format(d1=d1, d2=d2)
    comment = comment.format(a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, c=c, d1=d1, d2=d2)

    return stem, answer, comment














































# 3-2-5-76
def sizeandweight325_Stem_044():
    stem = "무게를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$수식$${a} rm {{kg}} - {b1} rm {{kg}} `` {b2} rm g$$/수식$$ ○ $$수식$${c1} rm {{kg}} `` {c2} rm g$$/수식$$\n"
    answer = "(정답)\n$$수식$${x}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a} rm {{kg}} - {b1} rm {{kg}} `` {b2} rm g = {a1} rm {{kg}} `` {a2} rm g - {b1} rm {{kg}} `` {b2} rm g " \
              "= {d1} rm {{kg}} `` {d2} rm g$$/수식$$입니다.\n" \
              "따라서 $$수식$${d1} rm {{kg}} `` {d2} rm g {x} {c1} rm {{kg}} `` {c2} rm g$$/수식$$입니다.\n\n"


    while True:
        a1 = np.random.randint(3, 10)
        b1 = np.random.randint(1, 8)
        if a1 >= b1 + 2:
            break

    a2 = 1000
    b2 = np.random.randint(1, 10) * 100
    c1 = a1 - b1
    c2 = np.random.randint(1, 10) * 100

    d1 = a1 - b1
    d2 = a2 - b2
    a = a1 + 1

    if d2 > c2:
        x = '&gt;'
    elif d2 == c2:
        x = '='
    else:
        x = '&lt;'


    stem = stem.format(a=a, b1=b1, b2=b2, c1=c1, c2=c2)
    answer = answer.format(x=x)
    comment = comment.format(a=a, a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, d1=d1, d2=d2, x=x)

    return stem, answer, comment












































# 3-2-5-77
def sizeandweight325_Stem_045():
    stem = "다음 중 $$수식$$1 rm {{kg}}$$/수식$$보다 무겁고 $$수식$$10 rm {{kg}}$$/수식$$보다 가벼운 무게를 모두 더하면 몇 $$수식$$rm {{kg}}$$/수식$$ 몇 $$수식$$rm g$$/수식$$인가요?\n$$표$$$$수식$${p1}$$/수식$$   $$수식$${p2}$$/수식$$   $$수식$${p3}$$/수식$$\n$$수식$${p4}$$/수식$$   $$수식$${p5}$$/수식$$   $$수식$${p6}$$/수식$$$$/표$$\n" \
        "{box1} $$수식$$rm {{kg}}$$/수식$$ {box2} $$수식$$rm g$$/수식$$"
    answer = "(정답)\n$$수식$${g1}$$/수식$$, $$수식$${g2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$1 rm {{kg}}$$/수식$$보다 무겁고 $$수식$$10 rm {{kg}}$$/수식$$보다 가벼운 무게는\n" \
              "$$수식$${b1} rm {{kg}} `` {b2} rm g$$/수식$$, $$수식$${e1} rm {{kg}}$$/수식$$, $$수식$${f} rm {{kg}} = {f1} rm {{kg}} `` {f2} rm g$$/수식$$입니다.\n" \
              "따라서 $$수식$${b1} rm {{kg}} `` {b2} rm g$$/수식$$, $$수식$${e1} rm {{kg}}$$/수식$$, $$수식$${f1} rm {{kg}} `` {f2} rm g$$/수식$$을 모두 더하면\n" \
              "$$수식$${b1} rm {{kg}} `` {b2} rm g + {e1} rm {{kg}} + {f1} rm {{kg}} `` {f2} rm g = {g1} rm {{kg}} `` {g2} rm g$$/수식$$입니다.\n\n"

    box1 = "$$수식$$box{　　}$$/수식$$"
    box2 = "$$수식$$box{　　　　}$$/수식$$"
    
    a1 = np.random.randint(11, 21)
    b1 = np.random.randint(1, 4)
    b2 = np.random.randint(1, 9) * 100

    c2 = np.random.randint(11, 20) * 50
    d2 = np.random.randint(1, 10) * 100
    e1 = np.random.randint(2, 10)
    f1 = np.random.randint(1, 10)

    while True:
        f2 = np.random.randint(1, 9) * 100
        if f2 <= 900 - b2:
            break

    f = f1 * 1000 + f2
    g1 = b1 + e1 + f1
    g2 = b2 + f2

    p = ['{a1} rm {{kg}}'.format(a1=a1), '{b1} rm {{kg}} `` {b2} rm g'.format(b1=b1, b2=b2),
         '{c2} rm g'.format(c2=c2), '{d2} rm g'.format(d2=d2), '{e1} rm {{kg}}'.format(e1=e1), '{f} rm g'.format(f=f)]

    np.random.shuffle(p)
    p1, p2, p3, p4, p5, p6 = p


    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, box1=box1, box2=box2)
    answer = answer.format(g1=g1, g2=g2)
    comment = comment.format(b1=b1, b2=b2, e1=e1, f=f, f1=f1, f2=f2, g1=g1, g2=g2)

    return stem, answer, comment














































# 3-2-5-78
def sizeandweight325_Stem_046():
    stem = "{s1} 한 상자의 무게는 $$수식$${a1} rm {{kg}} `` {a2} rm g$$/수식$$이고, {s2} 한 봉지의 무게는 $$수식$${b1} rm {{kg}} `` {b2} rm g$$/수식$$입니다. {s1} 한 상자의 무게는 {s2} 한 봉지의 무게보다 몇 $$수식$$rm {{kg}}$$/수식$$ 몇 $$수식$$rm g$$/수식$$ 더 무겁나요?\n" \
        "{box1} $$수식$$rm {{kg}}$$/수식$$ {box2} $$수식$$rm g$$/수식$$"
    answer = "(정답)\n$$수식$${d1}$$/수식$$, $$수식$${d2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${s1} 한 상자의 무게$$수식$$RIGHT ) - LEFT ($$/수식$${s2} 한 봉지의 무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {a1} rm {{kg}} `` {a2} rm g - {b1} rm {{kg}} `` {b2} rm g$$/수식$$\n" \
              "$$수식$$= {c1} rm {{kg}} `` {c2} rm g - {b1} rm {{kg}} `` {b2} rm g$$/수식$$\n" \
              "$$수식$$= {d1} rm {{kg}} `` {d2} rm g$$/수식$$\n\n"

    box1 = "$$수식$$box{　　}$$/수식$$"
    box2 = "$$수식$$box{　　　　}$$/수식$$"
    
    s1 = ['감자', '고구마', '옥수수', '밤', '호두', '연근'][np.random.randint(0, 6)]
    s2 = ['콩', '깨', '쌀', '보리쌀', '완두콩', '강낭콩', '팥'][np.random.randint(0, 7)]

    while True:
        a1 = np.random.randint(3, 10)
        b1 = np.random.randint(1, 8)
        if a1 >= b1 + 2:
            break

    ab2 = random.sample(list(range(1, 10)), 2)
    ab2.sort()

    a2, b2 = ab2
    a2 = a2 * 100
    b2 = b2 * 100
    c1 = a1 - 1

    c2 = a2 + 1000
    d1 = c1 - b1
    d2 = c2 - b2


    stem = stem.format(s1=s1, s2=s2, a1=a1, a2=a2, b1=b1, b2=b2, box1=box1, box2=box2)
    answer = answer.format(d1=d1, d2=d2)
    comment = comment.format(s1=s1, s2=s2, a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, d1=d1, d2=d2)

    return stem, answer, comment














































# 3-2-5-79
def sizeandweight325_Stem_047():
    stem = "다음은 {p1}와 친구들의 몸무게를 나타낸 것입니다. 몸무게의 합이 $$수식$${x1} rm {{kg}} `` {x2} rm g$$/수식$$인 두 사람은 누구와 누구인가요?\n$$표$${p1}: $$수식$${a1} rm {{kg}} `` {a2} rm g$$/수식$$\n{p2}: $$수식$${b1} rm {{kg}} `` {b2} rm g$$/수식$$\n{p3}: $$수식$${c1} rm {{kg}} `` {c2} rm g$$/수식$$$$/표$$\n"
    answer = "(정답)\n{y1}, {y2}\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${p1}와 {p2}의 몸무게의 합$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {a1} rm {{kg}} `` {a2} rm g + {b1} rm {{kg}} `` {b2} rm g = {A1} rm {{kg}} `` {A2} rm g = {B1} rm {{kg}} `` {B2} rm g$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${p1}와 {p3}의 몸무게의 합$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {a1} rm {{kg}} `` {a2} rm g + {c1} rm {{kg}} `` {c2} rm g = {C1} rm {{kg}} `` {C2} rm g = {D1} rm {{kg}} `` {D2} rm g$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${p2}와 {p3}의 몸무게의 합$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {b1} rm {{kg}} `` {b2} rm g + {c1} rm {{kg}} `` {c2} rm g = {E1} rm {{kg}} `` {E2} rm g = {F1} rm {{kg}} `` {F2} rm g$$/수식$$\n" \
              "따라서 몸무게의 합이 $$수식$${x1} rm {{kg}} `` {x2} rm g$$/수식$$인 두 사람은 {y1}와 {y2}입니다.\n\n"


    p = random.sample(['은지', '연주', '주호', '혁구', '영기', '상수', '은서', '동우', '재우', '진희',
                       '준서', '유라', '수미', '현수', '채아', '민주', '지호', '연아', '은우', '시우',
                       '혁재', '민하'], 3)

    p1, p2, p3 = p

    a1, b1, c1 = random.sample(list(range(31, 42)), 3)
    a2, b2, c2 = random.sample(list(range(5, 10)), 3)

    a2 = a2 * 100
    b2 = b2 * 100
    c2 = c2 * 100

    A1 = a1 + b1
    A2 = a2 + b2
    B1 = A1 + 1
    B2 = A2 - 1000

    C1 = a1 + c1
    C2 = a2 + c2
    D1 = C1 + 1
    D2 = C2 - 1000

    E1 = b1 + c1
    E2 = b2 + c2
    F1 = E1 + 1
    F2 = E2 - 1000

    x1, x2 = [[B1, B2], [D1, D2], [F1, F2]][np.random.randint(0, 3)]

    if x1 == B1:
        y1, y2 = p1, p2
    elif x1 == D1:
        y1, y2 = p1, p3
    else:
        y1, y2 = p2, p3


    stem = stem.format(p1=p1, p2=p2, p3=p3, x1=x1, x2=x2, a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2)
    answer = answer.format(y1=y1, y2=y2)
    comment = comment.format(p1=p1, p2=p2, p3=p3, a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2,
                             A1=A1, A2=A2, B1=B1, B2=B2, C1=C1, C2=C2, D1=D1, D2=D2, E1=E1, E2=E2, F1=F1, F2=F2,
                             x1=x1, x2=x2, y1=y1, y2=y2)

    return stem, answer, comment
















































# 3-2-5-80
def sizeandweight325_Stem_048():
    stem = "{p1}의 몸무게는 $$수식$${a1} rm {{kg}} `` {a2} rm g$$/수식$$이고, {p2}의 몸무게는 {p1}의 몸무게보다 $$수식$${b1} rm {{kg}} `` {b2} rm g$$/수식$$ 더 무겁습니다. {p2}가 {p1}를 업고 몸무게를 재면 몇 $$수식$$rm {{kg}}$$/수식$$ 몇 $$수식$$rm g$$/수식$$인가요?\n" \
        "{box1} $$수식$$rm {{kg}}$$/수식$$ {box2} $$수식$$rm g$$/수식$$"
    answer = "(정답)\n$$수식$${e1}$$/수식$$, $$수식$${e2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${p2}의 몸무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {a1} rm {{kg}} `` {a2} rm g + {b1} rm {{kg}} `` {b2} rm g = {c1} rm {{kg}} `` {c2} rm g$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${p1}와 {p2}의 몸무게의 합$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {a1} rm {{kg}} `` {a2} rm g + {c1} rm {{kg}} `` {c2} rm g = {d1} rm {{kg}} `` {d2} rm g = {e1} rm {{kg}} `` {e2} rm g$$/수식$$\n\n"


    box1 = "$$수식$$box{　　}$$/수식$$"
    box2 = "$$수식$$box{　　　　}$$/수식$$"
    
    p = random.sample(['혜수', '은지', '연주', '주호', '혁구', '영기', '상수', '은서', '동우', '재우', '진희',
                       '준서', '유라', '수미', '현수', '채아', '민주', '지호', '연아', '은우', '시우',
                       '혁재', '민하'], 2)

    p1, p2 = p

    while True:
        a1 = np.random.randint(25, 36)
        a2 = np.random.randint(5, 9) * 100
        b1 = np.random.randint(5, 11)
        b2 = np.random.randint(1, 5) * 100
        if b2 <= 900 - a2:
            break

    c1 = a1 + b1
    c2 = a2 + b2
    d1 = a1 + c1
    d2 = a2 + c2

    e1 = d1 + 1
    e2 = d2 - 1000


    stem = stem.format(p1=p1, p2=p2, a1=a1, a2=a2, b1=b1, b2=b2, box1=box1, box2=box2)
    answer = answer.format(e1=e1, e2=e2)
    comment = comment.format(p1=p1, p2=p2, a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, d1=d1, d2=d2, e1=e1, e2=e2)

    return stem, answer, comment
















































# 3-2-5-81
def sizeandweight325_Stem_049():
    stem = "□ 안에 알맞은 수를 구하세요.\n$$표$$$$수식$${a1} rm {{kg}} `` {a2} rm g - $$/수식$$ $$수식$$□$$/수식$$ $$수식$$rm g = {b1} rm {{kg}} `` {b2} rm g$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${x}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${a1} rm {{kg}} `` {a2} rm g - $$/수식$$ $$수식$$□$$/수식$$ rm g = {b1} rm {{kg}} `` {b2} rm g$$/수식$$에서\n" \
              "$$수식$$□$$/수식$$ $$수식$$ = {a1} rm {{kg}} `` {a2} rm g - {b1} rm {{kg}} `` {b2} rm g$$/수식$$\n$$수식$$ = {c1} rm {{kg}} `` {c2} rm g - {b1} rm {{kg}} `` {b2} rm g = {d1} rm {{kg}} `` {d2} rm g$$/수식$$\n" \
              "따라서 $$수식$${d1} rm {{kg}} `` {d2} rm g = {x} rm g$$/수식$$이므로 $$수식$$□$$/수식$$ 안에 알맞은\n 수는 $$수식$${x}$$/수식$$입니다.\n\n"


    while True:
        a1 = np.random.randint(3, 10)
        b1 = np.random.randint(1, 8)
        if a1 - b1 >= 2:
            break

    ab2 = random.sample(list(range(1, 10)), 2)
    ab2.sort()

    a2, b2 = ab2
    a2 = a2 * 100
    b2 = b2 * 100
    c1 = a1 - 1
    c2 = a2 + 1000

    d1 = c1 - b1
    d2 = c2 - b2
    x = d1 * 1000 + d2

    box = "box{　　　　}"


    stem = stem.format(box=box, a1=a1, a2=a2, b1=b1, b2=b2)
    answer = answer.format(x=x)
    comment = comment.format(box=box, a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, d1=d1, d2=d2, x=x)

    return stem, answer, comment











































# 3-2-5-82
def sizeandweight325_Stem_050():
    stem = "각각 무게가 같은 {s1} $$수식$${A}$$/수식$$개와 {s2} $$수식$${B}$$/수식$$개의 무게의 합이 $$수식$${a} rm g$$/수식$$이고 {s1} $$수식$${C}$$/수식$$개와 {s2} $$수식$${D}$$/수식$$개의 무게의 합이 $$수식$${b1} rm {{kg}} `` {b2} rm g$$/수식$$입니다. {s1} 한 개와 {s2} 한 개의 무게의 합은 몇 $$수식$$rm {{kg}}$$/수식$$ 몇 $$수식$$rm g$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${d1} rm {{kg}} `` {d2} rm g$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${s1} $$수식$$2$$/수식$$개와 {s2} $$수식$$2$$/수식$$개의 무게의 합$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$${s1} $$수식$${A}$$/수식$$개와 {s2} $$수식$${B}$$/수식$$개의 무게의 합" \
              "$$수식$$RIGHT ) - LEFT ($$/수식$${s1} $$수식$${C}$$/수식$$개와 {s2} $$수식$${D}$$/수식$$개의 무게의 합$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {a} rm g - {b1} rm {{kg}} `` {b2} rm g$$/수식$$\n" \
              "$$수식$$= {a1} rm {{kg}} `` {a2} rm g - {b1} rm {{kg}} `` {b2} rm g$$/수식$$\n" \
              "$$수식$$= {c1} rm {{kg}} `` {c2} rm g$$/수식$$\n" \
              "$$수식$${d1} rm {{kg}} `` {d2} rm g + {d1} rm {{kg}} `` {d2} rm g = {c1} rm {{kg}} `` {c2} rm g$$/수식$$이므로\n" \
              "{s1} 한 개와 {s2} 한 개의 무게의 합은 $$수식$${d1} rm {{kg}} `` {d2} rm g$$/수식$$입니다.\n\n"


    s1, s2, x1, x2 = [['배', '사과', 700, 400], ['참외', '배', 600, 700],
                      ['복숭아', '멜론', 300, 900], ['멜론', '사과', 900, 400],
                      ['파인애플', '참외', 800, 600], ['사과', '파인애플', 400, 800],
                      ['파인애플', '복숭아', 800, 300]][np.random.randint(0, 7)]

    while True:
        A, B = random.sample(list(range(4, 7)), 2)

        C = A - 2
        D = B - 2

        a = x1 * A + x2 * B
        a1 = int(a / 1000)
        a2 = a - a1 * 1000

        b = x1 * C + x2 * D
        b1 = int(b / 1000)
        b2 = b - b1 * 1000
        c = a - b
        if b2 != 0:
            break

    c1 = int(c / 1000)
    c2 = c - c1 * 1000

    d1 = int(c1 / 2)
    d2 = int(c2 / 2)


    stem = stem.format(s1=s1, s2=s2, a=a, b1=b1, b2=b2, A=A, B=B, C=C, D=D)
    answer = answer.format(d1=d1, d2=d2)
    comment = comment.format(s1=s1, s2=s2, a=a, b1=b1, b2=b2, A=A, B=B, C=C, D=D, a1=a1, a2=a2, c1=c1, c2=c2, d1=d1,
                             d2=d2)

    return stem, answer, comment












































# 3-2-5-83
def sizeandweight325_Stem_051():
    stem = "$$수식$${A} rm g$$/수식$$짜리 추 $$수식$${a}$$/수식$$개와 $$수식$${B} rm g$$/수식$$짜리 추 $$수식$${b}$$/수식$$개를 담은 {s}의 무게를 저울로 재어 보니 $$수식$${a1} rm {{kg}} `` {a2} rm g$$/수식$$이었습니다. {s}만의 무게는 몇 $$수식$$rm {{kg}}$$/수식$$ 몇 $$수식$$rm g$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${x1} rm {{kg}} `` {x2} rm g$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$추 $$수식$${c}$$/수식$$개의 무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {C} rm g + {D} rm g = {E} rm g = {e1} rm {{kg}} `` {e2} rm g$$/수식$$이므로\n" \
              "$$수식$${e1} rm {{kg}} `` {e2} rm g + LEFT ($$/수식$${s}의 무게$$수식$$RIGHT ) = {a1} rm {{kg}} `` {a2} rm g$$/수식$$입니다.\n" \
              "→ $$수식$$LEFT ($$/수식$${s}의 무게$$수식$$RIGHT )$$/수식$$\n$$수식$$ = {a1} rm {{kg}} `` {a2} rm g - {e1} rm {{kg}} `` {e2} rm g = {x1} rm {{kg}} `` {x2} rm g$$/수식$$\n\n"


    s = ['쇠 그릇', '녹그릇', '쇠 쟁반', '녹쇠 쟁반'][np.random.randint(0, 4)]

    A, B = [[200, 300], [300, 400], [300, 500], [400, 500]][np.random.randint(0, 4)]

    while True:
        a = np.random.randint(2, 7)
        b = np.random.randint(2, 8)
        if (A * a + B * b) % 1000 != 0:
            break

    c = a + b
    C = A * a
    D = B * b
    E = C + D

    e1 = int(E / 1000)
    e2 = E - e1 * 1000
    x1 = np.random.randint(1, 3)

    while True:
        x2 = np.random.randint(1, 10) * 100
        if x2 != 1000 - e2:
            break

    a1 = e1 + x1
    a2 = e2 + x2


    stem = stem.format(A=A, B=B, a=a, b=b, s=s, a1=a1, a2=a2)
    answer = answer.format(x1=x1, x2=x2)
    comment = comment.format(c=c, C=C, D=D, E=E, s=s, e1=e1, e2=e2, a1=a1, a2=a2, x1=x1, x2=x2)

    return stem, answer, comment



















































# 3-2-5-85
def sizeandweight325_Stem_052():
    stem = "{p1}, {p2}, {p3}가 한꺼번에 저울에 올라가서 몸무게를 재어 보니 $$수식$${A} rm {{kg}}$$/수식$$이었습니다. {p1}의 몸무게는 $$수식$${a1} rm {{kg}} `` {a2} rm g$$/수식$$이고, {p2}는 {p1}보다 $$수식$${d1} rm {{kg}} `` {d2} rm g$$/수식$$ 더 가볍습니다. {p3}의 몸무게는 몇 $$수식$$rm {{kg}}$$/수식$$ 몇 $$수식$$rm g$$/수식$$인가요?\n"
    answer = "(정답)\n$$수식$${c1} rm {{kg}} `` {c2} rm g$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${p2}의 몸무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {a1} rm {{kg}} `` {a2} rm g - {d1} rm {{kg}} `` {d2} rm g = {b1} rm {{kg}} `` {b2} rm g$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${p1}와 {p2}의 몸무게의 합$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {a1} rm {{kg}} `` {a2} rm g + {b1} rm {{kg}} `` {b2} rm g = {e1} rm {{kg}} `` {e2} rm g$$/수식$$\n" \
              "$$수식$$LEFT ($$/수식$${p3}의 몸무게$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {A} rm {{kg}} - {e1} rm {{kg}} `` {e2} rm g = {c1} rm {{kg}} `` {c2} rm g$$/수식$$\n\n"


    p = random.sample(['재수', '영서', '은지', '연주', '주호', '혁구', '영기', '상수', '은서', '동우', '재우', '진희',
                       '준서', '유라', '수미', '현수', '채아', '민주', '지호', '연아', '은우', '시우', '혁재', '민하'], 3)

    p1, p2, p3 = p

    while True:
        a1 = np.random.randint(26, 42)
        b1 = np.random.randint(26, 42)
        c1 = np.random.randint(25, 41)
        if a1 > b1 and b1 > c1 + 1 and a1-b1-1!=0:
            break

    a2, b2, c2 = [[100, 200, 700], [100, 300, 600], [100, 400, 500],
                  [200, 300, 500], [300, 800, 900], [400, 700, 900],
                  [500, 600, 900], [500, 700, 800]][np.random.randint(0, 8)]

    A = int(((a1 + b1 + c1) * 1000 + a2 + b2 + c2) / 1000)
    d1 = a1 - b1 - 1
    d2 = 1000 + a2 - b2

    E = (a1 + b1) * 1000 + a2 + b2
    e1 = int(E / 1000)
    e2 = E - e1 * 1000


    stem = stem.format(p1=p1, p2=p2, p3=p3, A=A, a1=a1, a2=a2, d1=d1, d2=d2)
    answer = answer.format(c1=c1, c2=c2)
    comment = comment.format(p1=p1, p2=p2, p3=p3, a1=a1, a2=a2, b1=b1, b2=b2, c1=c1, c2=c2, d1=d1, d2=d2, e1=e1, e2=e2,
                             A=A)

    return stem, answer, comment













