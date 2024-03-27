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




# 1-2-4-03
def addandsub124_Stem_001():
    stem = "계산 결과가 더 {state} 것의 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${x1} + {x2} + {x3}$$/수식$$\n ㉡ $$수식$${y1} + {y2} + {y3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${x1} + {x2} + {x3} = {x4} + {x3} = {x5}$$/수식$$\n" \
              "㉡ $$수식$${y1} + {y2} + {y3} = {y4} + {y3} = {y5}$$/수식$$\n" \
              "따라서 $$수식$${x5} {comp} {y5}$$/수식$$이므로 계산 결과가 더 {state} 것은 " \
              "{a1}입니다.\n\n"

    while True:
        x1 = np.random.randint(1, 5)
        x2 = np.random.randint(1, 4)
        x3 = np.random.randint(1, 4)
        x4 = x1 + x2
        x5 = x4 + x3

        y1 = np.random.randint(1, 5)
        y2 = np.random.randint(1, 4)
        y3 = np.random.randint(1, 4)
        y4 = y1 + y2
        y5 = y4 + y3

        if x5 != y5:
            break

    pick = np.random.randint(0, 2)
    state = ['큰', '작은'][pick]
    if x5 > y5:
        a1 = ['㉠', '㉡'][pick]
        comp = '&gt;'
    else:
        a1 = ['㉡', '㉠'][pick]
        comp = '&lt;'

    stem = stem.format(x1=x1, x2=x2, x3=x3, y1=y1, y2=y2, y3=y3, state=state)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, y1=y1, y2=y2, y3=y3, y4=y4, y5=y5, a1=a1,
                             comp=comp, state=state)

    return stem, answer, comment




# 1-2-4-04
def addandsub124_Stem_002():
    stem = "{where}에 {sa}{j1} $$수식$${x1}$$/수식$${unit}, {sb}{j2} $$수식$${x2}$$/수식$${unit}, {sc}{j3} $$수식$${x3}$$/수식$${unit} 있습니다. {where}에 있는 {sth}{jo} 모두 몇 {unit}인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${where}에 있는 {sth}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$${sa}의 수$$수식$$RIGHT ) + LEFT ($$/수식$${sb}의 수$$수식$$RIGHT ) + LEFT ($$/수식$${sc}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {x1} + {x2} + {x3} = {a1} LEFT ($$/수식$${unit}$$수식$$RIGHT )$$/수식$$\n\n"

    where, sth, unit = [['책꽃이', '책', '권'],
                        ['필통', '필기구', '개'],
                        ['신발장', '신발', '켤레']][np.random.randint(0, 3)]
    if sth == '책':
        sa, sb, sc = random.sample(['위인전', '동화책', '과학책', '시집', '소설책', '문제집'], 3)
    elif sth == '필기구':
        sa, sb, sc = random.sample(['연필', '볼펜', '지우개', '샤프', '사인펜', '색연필'], 3)
    else:
        sa, sb, sc = random.sample(['운동화', '슬리퍼', '실내화', '구두', '샌들', '러닝화'], 3)
    j1 = proc_jo(sa, 0)
    j2 = proc_jo(sb, 0)
    j3 = proc_jo(sc, 0)
    jo = proc_jo(sth, -1)

    x1 = np.random.randint(1, 7)
    x2 = np.random.randint(1, 3)
    x3 = np.random.randint(1, 3)
    a1 = x1 + x2 + x3

    stem = stem.format(x1=x1, x2=x2, x3=x3, sa=sa, sb=sb, sc=sc, j1=j1, j2=j2, j3=j3,
                       where=where, unit=unit, sth=sth, jo=jo)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, a1=a1, sa=sa, sb=sb, sc=sc,
                             where=where, unit=unit, sth=sth)

    return stem, answer, comment




# 1-2-4-05
def addandsub124_Stem_003():
    stem = "$$수식$${boxone}$$/수식$$ 안에 알맞은 수를 써넣어 이야기를 완성해 보세요.\n$$표$$$$수식$$LEFT [$$/수식$${sa}$$수식$$RIGHT ]$$/수식$$ 저는 {sth} $$수식$${x1}$$/수식$$개를 가지고 왔어요.\n$$수식$$LEFT [$$/수식$${sb}$$수식$$RIGHT ]$$/수식$$ 저는 $$수식$${x2}$$/수식$$개를 가지고 왔어요.\n$$수식$$LEFT [$$/수식$${sc}$$수식$$RIGHT ]$$/수식$$ 저는 $$수식$${x3}$$/수식$$개를 가지고 왔어요.\n$$수식$$LEFT [$$/수식$$선생님$$수식$$RIGHT ]$$/수식$$ 그럼 {sth}{jo} 모두 $$수식$${boxtwo}$$/수식$$개구나.$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$모은 {sth}의 전체 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$${sa}{j1}가 가지고온 {sth1} 수$$수식$$RIGHT ) + LEFT ($$/수식$${sb}{j2}가 가지고온 {sth1} 수$$수식$$RIGHT ) + LEFT ($$/수식$${sc}{j3}가 가지고온 {sth1} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {x1} + {x2} + {x3} = {a1}LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"

    boxone = "□"
    boxtwo = "□"

    picksth = np.random.randint(0, 5)
    sth = ['빈 병', '병뚜껑', '구슬', '조약돌', '동전'][picksth]
    sth1 = ['병', '병뚜껑', '구슬', '조약돌', '동전'][picksth]
    jo = proc_jo(sth, -1)

    sa = ['은수', '진영', '선진', '형석', '유미', '보미', '수지', '영현', '호연', '지수'][np.random.randint(0, 10)]
    sb = ['현지', '현주', '건민', '연석', '태호', '정민', '유진', '소현', '채영', '동휘'][np.random.randint(0, 10)]
    sc = ['영선', '우주', '현선', '소정', '혜영', '운하', '영진', '은정', '영호', '철호'][np.random.randint(0, 10)]
    j1 = name_jo(sa)
    j2 = name_jo(sb)
    j3 = name_jo(sc)

    x1 = np.random.randint(1, 5)
    x2 = np.random.randint(1, 4)
    x3 = np.random.randint(1, 4)
    a1 = x1 + x2 + x3

    stem = stem.format(x1=x1, x2=x2, x3=x3, sa=sa, sb=sb, sc=sc, sth=sth, jo=jo, boxone=boxone, boxtwo=boxtwo)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, a1=a1, sa=sa, sb=sb, sc=sc,
                             j1=j1, j2=j2, j3=j3, sth=sth, sth1=sth1)

    return stem, answer, comment




# 1-2-4-09
def addandsub124_Stem_004():
    stem = "{sa}에 $$수식$${x1}$$/수식$$명이 타고 있습니다. {sb}에서 $$수식$${x2}$$/수식$$명이 내리고, {sc}에서 $$수식$${x3}$$/수식$$명이 내렸습니다. {sa}에 남은 사람은 몇 명인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${sa}에 남아 있는 사람 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$$처음 {sa}에 타고 있던 사람 수$$수식$$RIGHT ) - LEFT ($$/수식$${sb}에서 내린 사람 수$$수식$$RIGHT ) - LEFT ($$/수식$${sc}에서 내린 사람 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {x1} - {x2} - {x3} = {a1} LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$\n\n"

    sa = ['버스', '지하철', '비행기'][np.random.randint(0, 3)]
    if sa == '버스':
        sb = ['공원 앞', '시청 앞', '문구점 앞', '도서관 앞', '제과점 앞'][np.random.randint(0, 5)]
        sc = ['동물원 앞', '아파트 앞', '식물원 앞', '병원 앞', '경기장 앞'][np.random.randint(0, 5)]
    elif sa == '지하철':
        sb = ['신촌역', '홍대입구역', '강남역', '잠실역', '시청역'][np.random.randint(0, 5)]
        sc = ['사당역', '교대역', '이대역', '강변역', '삼성역'][np.random.randint(0, 5)]
    elif sa == '비행기':
        sb = ['미국', '프랑스', '독일', '캐나다', '영국', '스위스', '호주'][np.random.randint(0, 7)]
        sc = ['중국', '일본', '필리핀', '인도', '베트남', '싱가포르', '홍콩'][np.random.randint(0, 7)]

    x1 = np.random.randint(7, 10)
    x2 = np.random.randint(1, 5)
    x3 = np.random.randint(1, 4)
    a1 = x1 - x2 - x3

    stem = stem.format(x1=x1, x2=x2, x3=x3, sa=sa, sb=sb, sc=sc)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, sa=sa, sb=sb, sc=sc, a1=a1)

    return stem, answer, comment




# 1-2-4-10
def addandsub124_Stem_005():
    stem = "$$수식$${boxone}$$/수식$$ 안에 알맞은 수를 써넣어 이야기를 완성해 보세요.\n$$표$$$$수식$$LEFT [$$/수식$${sa}$$수식$$RIGHT ]$$/수식$$ {sa}{j1} {sth} $$수식$${x1}$$/수식$$개를 사 왔는데 몇 개 먹었니?\n$$수식$$LEFT [$$/수식$${sb}$$수식$$RIGHT ]$$/수식$$ 제가 $$수식$${x2}$$/수식$$개 먹었어요.\n$$수식$$LEFT [$$/수식$${sc}$$수식$$RIGHT ]$$/수식$$ 저는 $$수식$${x3}$$/수식$$개 먹었어요.\n$$수식$$LEFT [$$/수식$${sd}$$수식$$RIGHT ]$$/수식$$ 그럼 {sth}{jo} 모두 $$수식$${boxtwo}$$/수식$$개 남았겠구나.$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$남은 호빵 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$${sa}{j1} 사온 {sth} 수$$수식$$RIGHT ) - LEFT ($$/수식$${sb}{j2}가 먹은 {sth} 수$$수식$$RIGHT ) - LEFT ($$/수식$${sc}{j3}가 먹은 {sth} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {x1} - {x2} - {x3} = {a1} LEFT ($$/수식$$명$$수식$$RIGHT )$$/수식$$\n\n"

    boxone = "□"
    boxtwo = "□"

    sth = ['호빵', '고구마', '옥수수', '사탕', '사과', '아이스크림', '소시지'][np.random.randint(0, 7)]
    jo = proc_jo(sth, 0)

    sa = ['엄마', '삼촌', '할아버지', '고모'][np.random.randint(0, 4)]
    sd = ['아빠', '이모', '할머니', '숙모'][np.random.randint(0, 4)]
    sb = ['영은', '은수', '진영', '선진', '형석', '유미', '보미', '수지', '영현', '호연', '지수'][np.random.randint(0, 11)]
    sc = ['지혁', '현지', '현주', '건민', '연석', '태호', '정민', '유진', '소현', '채영', '동휘'][np.random.randint(0, 11)]
    j1 = proc_jo(sa, 0)
    j2 = name_jo(sb)
    j3 = name_jo(sc)

    x1 = np.random.randint(7, 10)
    x2 = np.random.randint(1, 5)
    x3 = np.random.randint(1, 4)
    a1 = x1 - x2 - x3

    stem = stem.format(x1=x1, x2=x2, x3=x3, sa=sa, sb=sb, sc=sc, sd=sd,
                       boxone=boxone, boxtwo=boxtwo, sth=sth, jo=jo, j1=j1)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, sa=sa, sb=sb, sc=sc, a1=a1, j1=j1, j2=j2, j3=j3, sth=sth)

    return stem, answer, comment




# 1-2-4-14
def addandsub124_Stem_006():
    stem = "{sa}{j1}는 지금까지 {sth} $$수식$${x1}$$/수식$$개를 {did}. {sa}{j1}가 $$수식$${x2}$$/수식$$개를 더 {do} 모두 몇 개를 {do1} 것일까요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n" \
              "{content}\n" \
              "따라서 {sa}{j1}는 모두 $$수식$${a1}$$/수식$$개를 {do1} 것입니다.\n\n"

    sa = ['성호', '현지', '현주', '건민', '연석', '태호', '정민', '유진', '소현', '채영', '동휘', '영선',
          '우주', '현선', '소정', '혜영', '운하', '영진', '은정', '영호', '철호'][np.random.randint(0, 21)]
    j1 = name_jo(sa)

    pick = np.random.randint(0, 7)
    sth = ['장애물', '문제집', '딱지', '쿠폰', '동전', '사탕', '수학문제'][pick]
    did = ['뛰어 넘었습니다', '풀었습니다', '땄습니다', '모았습니다', '주웠습니다', '먹었습니다', '맞았습니다'][pick]
    do = ['뛰어 넘으면', '풀면', '따면', '모으면', '주우면', '먹으면', '맞으면'][pick]
    do1 = ['뛰어 넘는', '푸는', '따는', '모으는', '주운', '먹는', '맞는'][pick]

    while True:
        x1 = np.random.randint(3, 10)
        x2 = np.random.randint(3, 10)
        if x1 != x2:
            break
    a1 = x1 + x2

    content = ""
    for i in range(x1, a1):
        content = content + "$$수식$$" + str(i) + "$$/수식$$" + " → "
    content = content + "$$수식$$" + str(a1) + "$$/수식$$"

    stem = stem.format(x1=x1, x2=x2, sa=sa, j1=j1, sth=sth, did=did, do=do, do1=do1)
    answer = answer.format(a1=a1)
    comment = comment.format(content=content, sa=sa, j1=j1, a1=a1, do1=do1)

    return stem, answer, comment




# 1-2-4-16
def addandsub124_Stem_007():
    stem = "{sa}{j1}는 오늘 아침에 $$수식$${x1}$$/수식$${unit}, 저녁에 $$수식$${x2}$$/수식$${unit} {sth}{jo} {did1}, {sb}{j2}는 오늘 아침에 $$수식$${x2}$$/수식$${unit}, 저녁에 $$수식$${x1}$$/수식$${unit} {sth}{jo} {did2}. 다음 중 바르게 설명한 것을 찾아 기호를 써 보세요.\n$$표$$㉠ {p1}\n㉡ {p2}\n㉢ {p3}$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "두 수를 바꾸어 더해도 결과는 같으므로\n" \
              "$$수식$${x1} + {x2} = {x3}$$/수식$$, $$수식$${x2} + {x1} = {x3}$$/수식$$입니다.\n\n"

    sa = ['진성', '은수', '진영', '선진', '형석', '유미', '보미', '수지', '영현', '호연', '지수'][np.random.randint(0, 11)]
    sb = ['성훈', '현지', '우주', '현선', '소정', '혜영', '운하', '영진', '은정', '영호', '철호'][np.random.randint(0, 11)]
    j1 = name_jo(sa)
    j2 = name_jo(sb)

    pick = np.random.randint(0, 5)
    sth = ['책', '도장', '동전', '사탕', '수학문제'][pick]
    jo = proc_jo(sth, 1)
    unit = ['쪽', '개', '개', '개', '문제'][pick]
    did1 = ['읽고', '찍고', '줍고', '먹고', '풀고'][pick]
    did2 = ['읽었습니다', '찍었습니다', '주웠습니다', '먹었습니다', '풀었습니다'][pick]
    did3 = ['읽었어', '찍었어', '주웠어', '먹었어', '풀었어'][pick]
    did4 = ['읽은', '찍은', '주운', '먹은', '푼'][pick]

    while True:
        x1 = np.random.randint(3, 10)
        x2 = np.random.randint(3, 10)
        if x1 != x2:
            break
    x3 = x1 + x2

    q1 = "{sa}{j1}가 {sb}{j2}보다 {sth}{jo} 더 많이 {did3}.".format(sa=sa, j1=j1, sb=sb, j2=j2, sth=sth, jo=jo, did3=did3)
    q2 = "{sa}{j1}와 {sb}{j2}가 {did4} {sth}의 {unit}수는 같아.".format(sa=sa, j1=j1, sb=sb, j2=j2, sth=sth, unit=unit, did4=did4)
    q3 = "{sb}{j2}가 {sa}{j1}보다 {sth}{jo} 더 많이 {did3}.".format(sa=sa, j1=j1, sb=sb, j2=j2, sth=sth, jo=jo, did3=did3)
    p = [q1, q2, q3]
    np.random.shuffle(p)
    [p1, p2, p3] = p

    if p1 == q2:
        a1 = '㉠'
    elif p2 == q2:
        a1 = '㉡'
    else:
        a1 = '㉢'

    stem = stem.format(x1=x1, x2=x2, sa=sa, j1=j1, sb=sb, j2=j2, sth=sth, jo=jo, unit=unit,
                       did1=did1, did2=did2, p1=p1, p2=p2, p3=p3)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3)

    return stem, answer, comment





# 1-2-4-17
def addandsub124_Stem_008():
    stem = "{sa}{j1}는 매일 {sb}에게 먹이를 같은 개수만큼 줍니다. 어제는 아침에 $$수식$${x1}$$/수식$$개, 저녁에 $$수식$${x2}$$/수식$$개를 주었습니다. 오늘 아침에 $$수식$${x2}$$/수식$$개를 주었다면 저녁에는 몇 개를 주어야 하나요?\n"
    answer = "(정답)\n$$수식$${x1}$$/수식$$개\n"
    comment = "(해설)\n" \
              "덧셈은 두 수를 바꾸어 더해도 그 값이 같으므로\n" \
              "$$수식$${x1} + {x2} = {x3}$$/수식$$, $$수식$${x2} + {x1} = {x3}$$/수식$$입니다.\n\n"

    sa = ['진영', '선진', '형석', '유미', '보미', '수지', '영현', '호연',
          '우주', '현선', '소정', '혜영', '운하', '영진', '은정', '영호', '철호'][np.random.randint(0, 17)]
    j1 = name_jo(sa)

    sb = ['햄스터', '고슴도치', '염소', '양', '사슴', '앵무새'][np.random.randint(0, 6)]

    while True:
        x1 = np.random.randint(1, 10)
        x2 = np.random.randint(1, 10)
        if x1 != x2:
            break
    x3 = x1 + x2

    stem = stem.format(x1=x1, x2=x2, sa=sa, j1=j1, sb=sb)
    answer = answer.format(x1=x1)
    comment = comment.format(x1=x1, x2=x2, x3=x3)

    return stem, answer, comment




# 1-2-4-18
def addandsub124_Stem_009():
    stem = "합이 $$수식$$10$$/수식$$인 것을 모두 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${x1} + {x2}$$/수식$$    ㉡ $$수식$${x3} + {x4}$$/수식$$\n㉢ $$수식$${x5} + {x6}$$/수식$$    ㉣ $$수식$${x7} + {x8}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{a1}, {a2}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${x1} + {x2} = {x9}$$/수식$$, ㉡ $$수식$${x3} + {x4} = {x10}$$/수식$$,\n" \
              "㉢ $$수식$${x5} + {x6} = {x11}$$/수식$$, ㉣ $$수식$${x7} + {x8} = {x12}$$/수식$$\n" \
              "따라서 합이 $$수식$$10$$/수식$$인 것은 {a1}, {a2}입니다.\n\n"

    while True:
        c1 = np.random.randint(1, 10)
        c3 = np.random.randint(1, 10)
        if c1 != c3:
            break
    c2 = 10 - c1
    c4 = 10 - c3

    tmp = [10 + 1, 10 - 1][np.random.randint(0, 2)]
    while True:
        c5 = np.random.randint(1, tmp)
        c7 = np.random.randint(1, tmp)
        if c5 != c7:
            break
    c6 = tmp - c5
    c8 = tmp - c7

    x = [[c1, c2], [c3, c4], [c5, c6], [c7, c8]]
    np.random.shuffle(x)
    [[x1, x2], [x3, x4], [x5, x6], [x7, x8]] = x

    sums = []
    x9 = x1 + x2
    sums.append(x9)
    x10 = x3 + x4
    sums.append(x10)
    x11 = x5 + x6
    sums.append(x11)
    x12 = x7 + x8
    sums.append(x12)

    a = []
    for i in range(0, len(sums)):
        if sums[i] == 10:
            a.append(answer_kodict[i])
    [a1, a2] = a

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8,
                             x9=x9, x10=x10, x11=x11, x12=x12, a1=a1, a2=a2)

    return stem, answer, comment




# 1-2-4-19
def addandsub124_Stem_010():
    stem = "계산 결과를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$를 알맞게 써넣으세요.\n$$표$$$$수식$${x1} + {x2} BIGCIRC {x3} + {x4}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${x1} + {x2} = {x5}$$/수식$$, ㉡ $$수식$${x3} + {x4} = {x6}$$/수식$$\n" \
              "→ $$수식$${x5}{a1}{x6}$$/수식$$\n\n"

    box1 = "□"

    tmp = [9, 10, 11][np.random.randint(0, 3)]
    x = [10, tmp]
    np.random.shuffle(x)
    [x5, x6] = x

    while True:
        x1 = np.random.randint(1, x5)
        x3 = np.random.randint(1, x6)
        if x5 != x6 or x1 != x3:
            break
    x2 = x5 - x1
    x4 = x6 - x3

    if x5 == x6:
        a1 = '='
    elif x5 > x6:
        a1 = '&gt;'
    else:
        a1 = '&lt;'

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, box1=box1)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, a1=a1)

    return stem, answer, comment




# 1-2-4-21
def addandsub124_Stem_011():
    stem = "{sa}{j1}는 {sth} $$수식$${x1}$$/수식$${unit}{jo1} 가지고 있습니다. {sb}{j2}가 {sa}{j1}에게 {sth} $$수식$${x2}$$/수식$${unit}{jo1} 주었습니다. {sa}{j1}가 가지고 있는 {sth}{jo2} 모두 몇 {unit}인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${sa}{j1}가 가지고 있는 {sth} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {x1} + {x2} = {a1} LEFT ($$/수식$${unit}$$수식$$RIGHT )$$/수식$$\n\n"

    sa = ['동현', '우주', '현선', '소정', '혜영', '운하', '영진', '은정', '영호', '철호'][np.random.randint(0, 10)]
    j1 = name_jo(sa)
    sb = ['주혁', '진성', '은수', '진영', '선진', '형석', '유미', '보미', '수지', '영현'][np.random.randint(0, 10)]
    j2 = name_jo(sb)

    pick = np.random.randint(0, 7)
    sth = ['딱지', '책', '초콜릿', '귤', '땅콩', '카드', '동전'][pick]
    unit = ['장', '권', '개', '개', '개', '장', '개'][pick]
    jo1 = proc_jo(unit, 1)
    jo2 = proc_jo(sth, -1)

    a1 = 10
    x1 = np.random.randint(1, 10)
    x2 = a1 - x1

    stem = stem.format(x1=x1, x2=x2, sa=sa, sb=sb, j1=j1, j2=j2, sth=sth, unit=unit, jo1=jo1, jo2=jo2)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, a1=a1, sa=sa, j1=j1, sth=sth, unit=unit)

    return stem, answer, comment




# 1-2-4-22
def addandsub124_Stem_012():
    stem = "$$수식$${box1}$$/수식$$ 안에 알맞은 수가 가장 {state} 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${box1} + {x2} = 10$$/수식$$  ㉡ $$수식$${x3} + {box1} = 10$$/수식$$\n㉢ $$수식$${x5} + {box1} = 10$$/수식$$  ㉣ $$수식$${box1} + {x8} = 10$$/수식$$$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${x1} + {x2} = 10$$/수식$$이므로 $$수식$${box1} = {x1}$$/수식$$\n" \
              "㉡ $$수식$${x3} + {x4} = 10$$/수식$$이므로 $$수식$${box1} = {x4}$$/수식$$\n" \
              "㉢ $$수식$${x5} + {x6} = 10$$/수식$$이므로 $$수식$${box1} = {x6}$$/수식$$\n" \
              "㉣ $$수식$${x7} + {x8} = 10$$/수식$$이므로 $$수식$${box1} = {x7}$$/수식$$\n" \
              "따라서 $$수식$${box1}$$/수식$$ 안에 알맞은 수가 가장 {state} 것은 {a1}입니다.\n\n"

    box1 = "□"

    x = [[1, 9], [2, 8], [3, 7], [4, 6], [5, 5]]
    for i in range(0, 5):
        np.random.shuffle(x[i])
    np.random.shuffle(x)
    [[x1, x2], [x3, x4], [x5, x6], [x7, x8]] = x[0:4]

    state = ['큰', '작은'][np.random.randint(0, 2)]
    if state == '큰':
        if x1 > x4 and x1 > x6 and x1 > x7:
            a1 = '㉠'
        elif x4 > x1 and x4 > x6 and x4 > x7:
            a1 = '㉡'
        elif x6 > x1 and x6 > x4 and x6 > x7:
            a1 = '㉢'
        else:
            a1 = '㉣'
    else:
        if x1 < x4 and x1 < x6 and x1 < x7:
            a1 = '㉠'
        elif x4 < x1 and x4 < x6 and x4 < x7:
            a1 = '㉡'
        elif x6 < x1 and x6 < x4 and x6 < x7:
            a1 = '㉢'
        else:
            a1 = '㉣'

    stem = stem.format(box1=box1, x2=x2, x3=x3, x5=x5, x8=x8, state=state)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8, a1=a1, box1=box1, state=state)

    return stem, answer, comment





# 1-2-4-23
def addandsub124_Stem_013():
    stem = "{sth1} $$수식$$10$$/수식$$개가 세워져 있습니다. {sa}{j1}가 굴린 {sth2}에 {sth1} $$수식$${x1}$$/수식$$개가 쓰러졌다면 쓰러지지 않은 {sth1}{jo} 몇 개일까요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${x1} + {box1} = 10$$/수식$$" \
              "→$$수식$${x1} + {a1} = 10$$/수식$$이므로 $$수식$${box1} = {a1}$$/수식$$\n" \
              "따라서 쓰러지지 않은 {sth1}{jo} $$수식$${a1}$$/수식$$개입니다.\n\n"

    box1 = "□"

    sa = ['진우', '우주', '현정', '소진', '형준', '유아', '보미', '수지', '영준', '철민'][np.random.randint(0, 10)]
    j1 = name_jo(sa)

    pick = np.random.randint(0, 5)
    sth1 = ['볼링 핀', '도미노', '인형', '막대기', '연필'][pick]
    sth2 = ['볼링공', '쇠구슬', '베개', '축구공', '지우개'][pick]
    jo = proc_jo(sth1, -1)

    x1 = np.random.randint(1, 10)
    a1 = 10 - x1

    stem = stem.format(sth1=sth1, sth2=sth2, jo=jo, sa=sa, j1=j1, x1=x1)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, a1=a1, sth1=sth1, jo=jo, box1=box1)

    return stem, answer, comment




# 1-2-4-24
def addandsub124_Stem_014():
    stem = "{sa}{j1}가 {sth1}자전거 $$수식$${x1}$$/수식$$대와 {sth2}자전거 몇 대의 바퀴 수를 세었더니 모두 $$수식$$10$$/수식$$개였습니다. {sth2}자전거는 몇 대일까요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$대\n"
    comment = "(해설)\n" \
              "{sth1}자전거 $$수식$${x1}$$/수식$$대의 바퀴는 " \
              "$$수식$${p1} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$입니다. " \
              "$$수식$${s1}$$/수식$$와 더해서 $$수식$$10$$/수식$$이 되는 수는 $$수식$${s2}$$/수식$$입니다.\n" \
              "$$수식$${p2}$$/수식$$에서 $$수식$${s2}$$/수식$$는 " \
              "$$수식$${s3}$$/수식$$씩 $$수식$${s4}$$/수식$$번 더한 수이므로 {sth2}자전거는 $$수식$${a1}$$/수식$$대입니다.\n\n"

    sa = ['영준', '우주', '현정', '소진', '형준', '유아', '보미', '수지', '영호', '철민'][np.random.randint(0, 10)]
    j1 = name_jo(sa)

    sth = ['외발', '두발', '세발', '네발']
    nums = list(range(0, 4))
    np.random.shuffle(nums)
    picks = nums[0:2]
    sth1 = sth[picks[0]]
    sth2 = sth[picks[1]]

    sum = picks[0] + picks[1]
    if sum == 1:  # 1, 2
        [x1, a1] = [[2, 4], [4, 3], [6, 2], [8, 1]][np.random.randint(0, 4)]
    elif sum == 2:  # 1, 3
        [x1, a1] = [[7, 1], [4, 2], [1, 3]][np.random.randint(0, 3)]
    elif sum == 3:  # 1, 4 & 2, 3
        [x1, a1] = [2, 2]
    elif sum == 4:  # 2, 4
        [x1, a1] = [[3, 1], [1, 2]][np.random.randint(0, 2)]
    else:  # 3, 4
        [x1, a1] = [2, 1]

    if (picks[0] + 1) * x1 + (picks[1] + 1) * a1 != 10:
        [x1, a1] = [a1, x1]

    p1 = ""
    for i in range(1, x1+1):
        p1 = p1 + str(picks[0]+1)
        if i != x1:
            p1 = p1 + "+"
    p1 = p1 + "=" + str((picks[0]+1)*x1)
    p2 = ""
    for i in range(1, a1+1):
        p2 = p2 + str(picks[1] + 1)
        if i != a1:
            p2 = p2 + "+"
    p2 = p2 + "=" + str((picks[1] + 1) * a1)

    s1 = (picks[0]+1)*x1
    s2 = (picks[1] + 1) * a1
    s3 = picks[1] + 1
    s4 = a1

    stem = stem.format(sa=sa, j1=j1, sth1=sth1, sth2=sth2, x1=x1)
    answer = answer.format(a1=a1)
    comment = comment.format(sth1=sth1, sth2=sth2, x1=x1, p1=p1, p2=p2, s1=s1, s2=s2, s3=s3, s4=s4, a1=a1)

    return stem, answer, comment




# 1-2-4-27
def addandsub124_Stem_015():
    stem = "{where}에 {sth}{jo1} $$수식$$10$$/수식$$개 있습니다. {sa}{j1}가 {sth} $$수식$${x1}$$/수식$$개를 먹었다면 {where}에 남아 있는 {sth}{jo2} 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$$남아 있는 {sth}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$${where}에 있던 {sth}의 수$$수식$$RIGHT ) - LEFT ($$/수식$${sa}{j1}가 먹은 {sth}의 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= 10 - {x1} = {a1} LEFT ($$/수식$$개$$수식$$RIGHT )$$/수식$$\n\n"

    sa = ['선아', '영경', '우진', '현지', '채영', '태형', '아영', '수정', '서진', '영준', '민재'][np.random.randint(0, 11)]
    j1 = name_jo(sa)

    where = ['바구니', '냉장고', '식탁 위', '책상 위', '거실', '집', '가방'][np.random.randint(0, 7)]
    sth = ['감', '사탕', '초콜릿', '귤', '사과', '빵', '요구르트', '고구마'][np.random.randint(0, 8)]
    jo1 = proc_jo(sth, 0)
    jo2 = proc_jo(sth, -1)

    x1 = np.random.randint(1, 10)
    a1 = 10 - x1

    stem = stem.format(where=where, sth=sth, jo1=jo1, jo2=jo2, sa=sa, j1=j1, x1=x1)
    answer = answer.format(a1=a1)
    comment = comment.format(where=where, sth=sth, sa=sa, j1=j1, x1=x1, a1=a1)

    return stem, answer, comment




# 1-2-4-29
def addandsub124_Stem_016():
    stem = "{sa}와 {sb}에 알맞은 수의 합을 구해 보세요.\n$$표$${sa}$$수식$$+ {x1} = 10$$/수식$$\n$$수식$$10 - $$/수식$${sb}$$수식$$ = {x2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "{sa}$$수식$$ + {x1} = 10$$/수식$$에서 {sa}$$수식$$ = {s1}$$/수식$$입니다.\n" \
              "$$수식$$10 -$$/수식$${sb}$$수식$$= {x2}$$/수식$$에서 {sb}$$수식$$= {s2}$$/수식$$입니다.\n" \
              "따라서 {sa}와 {sb}에 알맞은 수의 합은 $$수식$${s1} + {s2} = {a1}$$/수식$$입니다.\n\n"

    ss = ['★', '●', '◆', '■', '▲', '♥']
    np.random.shuffle(ss)
    sa, sb = ss[0:2]

    while True:
        x1 = np.random.randint(1, 10)
        x2 = np.random.randint(1, 10)
        if x1 != x2:
            break
    s1 = 10 - x1
    s2 = 10 - x2
    a1 = s1 + s2

    stem = stem.format(x1=x1, x2=x2, sa=sa, sb=sb)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, a1=a1, s1=s1, s2=s2, sa=sa, sb=sb)

    return stem, answer, comment




# 1-2-4-30
def addandsub124_Stem_017():
    stem = "$$수식$${x1}$$/수식$$보다 $$수식$${x2}$$/수식$$ {state1} 수는 $$수식$${x3}$$/수식$${j1} 어떤 수를 {state2} 것과 같습니다. 어떤 수는 얼마인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${x1}$$/수식$$보다 $$수식$${x2}$$/수식$$ {state1} 수는 $$수식$${x1} - {x2} = 10$$/수식$$입니다.\n" \
              "어떤 수를 $$수식$${box1}$$/수식$$라 하면 " \
              "$$수식$${x3} + {box1} = 10$$/수식$$입니다.\n" \
              "따라서 $$수식$${x3} + {a1} = 10$$/수식$$에서 $$수식$${box1} = {a1}$$/수식$$이므로 " \
              "어떤 수는 $$수식$${a1}$$/수식$$입니다.\n\n"

    box1 = "□"

    state = np.random.randint(0, 2)
    state1 = ['작은', '큰'][state]
    state2 = ['더한', '뺀'][state]

    if state == 0:
        x1 = np.random.randint(11, 20)
        x2 = x1 - 10
        x3 = np.random.randint(1, 10)
        a1 = 10 - x3
        j1 = "와"
    else:
        x1 = np.random.randint(1, 10)
        x2 = 10 - x1
        x3 = np.random.randint(11, 20)
        a1 = x3 - 10
        j1 = "에서"

    stem = stem.format(x1=x1, x2=x2, x3=x3, j1=j1, state1=state1, state2=state2)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, a1=a1, box1=box1, state1=state1)

    return stem, answer, comment





# 1-2-4-31
def addandsub124_Stem_018():
    stem = "세 수를 더해 보세요.\n$$표$$ $$수식$${x1}$$/수식$$,   $$수식$${x2}$$/수식$$,   $$수식$${x3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${underline} + {x3} = 10 + {x3} = {a1}$$/수식$$\n\n"

    x1 = np.random.randint(1, 10)
    x2 = 10 - x1
    x3 = np.random.randint(1, 10)
    a1 = 10 + x3
    underline = "under{%d + %d}" % (x1, x2)

    stem = stem.format(x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=a1)
    comment = comment.format(underline=underline, x3=x3, a1=a1)

    return stem, answer, comment





# 1-2-4-32
def addandsub124_Stem_019():
    stem = "계산 결과의 크기를 비교하여 ○ 안에 $$수식$$&gt;$$/수식$$, $$수식$$=$$/수식$$, $$수식$$&lt;$$/수식$$ 를 알맞게 써넣으세요.\n$$표$$$$수식$${box1}``BIGCIRC``{box2}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${underline1} + {x3} = 10 + {x3} = {s1}$$/수식$$\n" \
              "$$수식$${x4} + {underline2} = {x4} + 10 = {s2}$$/수식$$\n" \
              "→ $$수식$${s1}{a1}{s2}$$/수식$$\n\n"

    while True:
        x1 = np.random.randint(1, 10)
        x2 = 10 - x1
        x3 = np.random.randint(1, 10)
        if x1 != x3:
            break
    s1 = 10 + x3

    while True:
        x5 = np.random.randint(1, 10)
        x6 = 10 - x5
        x4 = np.random.randint(1, 10)
        if x4 != x6:
            break
    s2 = 10 + x4

    if s1 > s2:
        a1 = "&gt;"
    elif s1 < s2:
        a1 = "&lt;"
    else:
        a1 = "="

    box1 = "%d + %d + %d" % (x1, x2, x3)
    box2 = "%d + %d + %d" % (x4, x5, x6)

    underline1 = "under{%d + %d}" % (x1, x2)
    underline2 = "under{%d + %d}" % (x5, x6)

    stem = stem.format(box1=box1, box2=box2)
    answer = answer.format(a1=a1)
    comment = comment.format(underline1=underline1, x3=x3, x4=x4, underline2=underline2, a1=a1, s1=s1, s2=s2)

    return stem, answer, comment





# 1-2-4-34
def addandsub124_Stem_020():
    stem = "보기에서 ㉠과 ㉡에 들어갈 두 수를 골라 다음 식을 완성하려고 합니다. ㉠, ㉡에 알맞은 수를 각각 구해 보세요.\n$$표$$$$수식$${c1}$$/수식$$   $$수식$${c2}$$/수식$$   $$수식$${c3}$$/수식$$   $$수식$${c4}$$/수식$$   $$수식$${c5}$$/수식$$$$/표$$\n    $$수식$${x1} + {x2} +$$/수식$$㉠$$수식$$=$$/수식$$㉡\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${x1} + {x2} + $$/수식$$㉠$$수식$$=$$/수식$$㉡\n" \
              "$$수식$${x2}$$/수식$$와 더해서 $$수식$$10$$/수식$$이 되는 수는 $$수식$${a1}$$/수식$$입니다.\n" \
              "→ $$수식$${x1}+ {underline} = {x1} +10={a2}$$/수식$$\n" \
              "따라서 ㉠$$수식$$={a1}$$/수식$$, ㉡$$수식$$={a2}$$/수식$$입니다.\n\n"

    while True:
        x2 = np.random.randint(1, 10)
        a1 = 10 - x2
        x1 = np.random.randint(1, 10)
        if x1 != x2:
            break
    a2 = 10 + x1

    while True:
        c5 = np.random.randint(11, 20)
        if c5 != a2:
            break
    temp = c5 - x1 + x2

    while True:
        c1 = np.random.randint(1, 10)
        sum = x1 + x2 + c1
        if sum != a2 and sum != temp:
            break

    while True:
        c2 = np.random.randint(1, 10)
        sum = x1 + x2 + c2
        if sum != a2 and sum != temp:
            break

    c = [c1, c2, a1, a2, c5]
    c.sort()
    c1, c2, c3, c4, c5 = c

    underline = "under{%d + %d}" % (x2, a1)

    stem = stem.format(x1=x1, x2=x2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(x1=x1, x2=x2, a1=a1, a2=a2, underline=underline)

    return stem, answer, comment




# 1-2-4-35
def addandsub124_Stem_021():
    stem = "계산 결과가 {state1} 것부터 차례대로 기호를 써 보세요.\n$$표$$ ㉠ $$수식$${x1} + {x2} + {x3}$$/수식$$\n ㉡ $$수식$${x4} + {x5} + {x6}$$/수식$$\n ㉢ $$수식$${x7} + {x8} + {x9}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{a1}, {a2}, {a3}\n"
    comment = "(해설)\n" \
              "㉠ $$수식$${x1} + {x2} + {x3} = 10 + {x2} = {s1}$$/수식$$\n" \
              "㉡ $$수식$${x4} + {x5} + {x6} = 10 + {x5} = {s2}$$/수식$$\n" \
              "㉢ $$수식$${x7} + {x8} + {x9} = 10 + {x8} = {s3}$$/수식$$\n" \
              "$$수식$${p1} {state2} {p2} {state2} {p3}$$/수식$$이므로 계산 결과가 큰 것부터 차례대로 기호를 쓰면 " \
              "{a1}, {a2}, {a3}입니다.\n\n"

    x = list(range(1, 10))
    np.random.shuffle(x)
    x2, x5, x8 = x[0:3]

    xx = [[1, 9], [2, 8], [3, 7], [4, 6], [5, 5]]
    for i in range(0, len(xx)):
        np.random.shuffle(xx[i])
    np.random.shuffle(xx)
    [[x1, x3], [x4, x6], [x7, x9]] = xx[0:3]

    s1 = 10 + x2
    s2 = 10 + x5
    s3 = 10 + x8

    state = np.random.randint(0, 2)
    state1 = ['큰', '작은'][state]
    state2 = ['&gt;', '&lt;'][state]

    if s1 > s2 and s1 > s3:
        p1 = s1
        a1 = '㉠'
        if s2 > s3:
            p2 = s2
            p3 = s3
            a2 = "㉡"
            a3 = "㉢"
        else:
            p2 = s3
            p3 = s2
            a2 = "㉢"
            a3 = "㉡"
    elif s2 > s1 and s2 > s3:
        p1 = s2
        a1 = "㉡"
        if s1 > s3:
            p2 = s1
            p3 = s3
            a2 = "㉠"
            a3 = "㉢"
        else:
            p2 = s3
            p3 = s1
            a2 = "㉢"
            a3 = "㉠"
    else:
        p1 = s3
        a1 = "㉢"
        if s1 > s2:
            p2 = s1
            p3 = s2
            a2 = "㉠"
            a3 = "㉡"
        else:
            p2 = s2
            p3 = s1
            a2 = "㉡"
            a3 = "㉠"

    if state == 1:
        a1, a2, a3 = a3, a2, a1
        p1, p2, p3 = p3, p2, p1

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8, x9=x9, state1=state1)
    answer = answer.format(a1=a1, a2=a2, a3=a3)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6, x7=x7, x8=x8, x9=x9,
                             s1=s1, s2=s2, s3=s3, a1=a1, a2=a2, a3=a3, p1=p1, p2=p2, p3=p3, state2=state2)

    return stem, answer, comment




# 1-2-4-37
def addandsub124_Stem_022():
    stem = "{sa}{j1}는 {adj1} {sth} $$수식$${x1}$$/수식$$개, {adj2} {sth} $$수식$${x2}$$/수식$$개, {adj3} {sth} $$수식$${x3}$$/수식$$개를 가지고 있습니다. {sa}{j1}가 가지고 있는 {sth}{jo} 모두 몇 개일까요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n" \
              "$$수식$$LEFT ($$/수식$${sa}{j1}가 가지고 있는 {sth} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= LEFT ($$/수식$${adj1} {sth} 수$$수식$$RIGHT ) + LEFT ($$/수식$${adj2} {sth} 수$$수식$$RIGHT ) + LEFT ($$/수식$${adj3} {sth} 수$$수식$$RIGHT )$$/수식$$\n" \
              "$$수식$$= {x1} + {x2} + {x3} = 10 + {x3} = {a1}$$/수식$$\n\n"

    sa = ['현서', '로운', '연희', '주연', '세호', '강민', '도훈', '정현', '범수', '나라'][np.random.randint(0, 10)]
    j1 = name_jo(sa)

    sth = ['구슬', '사탕', '지우개', '우산', '공', '지우개'][np.random.randint(0, 6)]
    jo = proc_jo(sth, -1)
    adj1, adj2, adj3 = [['빨간색', '노란색', '초록색'],
                        ['큰', '보통', '작은'],
                        ['무거운', '보통', '가벼운']][np.random.randint(0, 3)]

    x1 = np.random.randint(1, 10)
    x2 = 10 - x1
    x3 = np.random.randint(1, 10)
    a1 = 10 + x3

    stem = stem.format(sa=sa, j1=j1, adj1=adj1, adj2=adj2, adj3=adj3, sth=sth, jo=jo,
                       x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=a1)
    comment = comment.format(sa=sa, j1=j1, adj1=adj1, adj2=adj2, adj3=adj3, sth=sth,
                             x1=x1, x2=x2, x3=x3, a1=a1)

    return stem, answer, comment
