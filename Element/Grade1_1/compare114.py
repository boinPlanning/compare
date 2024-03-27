import numpy as np

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


def name_jo(num):
    # 이
    if bool_jo(num):
        return "이"
    return ""




# 1-1-4-07
def compare114_Stem_001():
    stem = "{sa}, {sb}, {sc} 중 가장 긴 우산을 가지고 있는 사람은 누구일까요?\n$$표$$ {x1}\n {x2}$$/표$$\n"
    answer = "(정답)\n{sa}\n"
    comment = "(해설)\n{p1}\n{p2}\n따라서 가장 긴 우산을 가지고 있는 사람은 {sa}입니다.\n\n"

    sa = ['현수', '태영', '철민', '선우', '가희', '지민'][np.random.randint(0, 3)]
    sb = ['영수', '수영', '현정', '소연', '희정', '광식'][np.random.randint(0, 3)]
    sc = ['진호', '지윤', '민정', '시언', '정배', '도준'][np.random.randint(0, 3)]

    j1 = name_jo(sa)
    j2 = name_jo(sb)
    j3 = name_jo(sc)

    y1 = "• %s: 내 우산은 %s%s의 우산보다 더 길어." % (sa, sb, j2)
    y2 = "• %s: 내 우산은 %s%s의 우산보다 더 길어." % (sb, sc, j3)

    q1 = "• %s%s의 우산은 %s%s의 우산보다 더 깁니다." % (sa, j1, sb, j2)
    q2 = "• %s%s의 우산은 %s%s의 우산보다 더 깁니다." % (sb, j2, sc, j3)

    picknum = np.random.randint(0, 2)
    if picknum == 0:
        x1 = y1
        x2 = y2
        p1 = q1
        p2 = q2
    else:
        x1 = y2
        x2 = y1
        p1 = q2
        p2 = q1

    stem = stem.format(sa=sa, sb=sb, sc=sc, x1=x1, x2=x2)
    answer = answer.format(sa=sa)
    comment = comment.format(p1=p1, p2=p2, sa=sa)

    return stem, answer, comment



# 1-1-4-11
def compare114_Stem_002():
    stem = "{sa}{n1}는 {sb}{n2}보다 더 무겁고, {sc}{n3}는 {sb}{n2}보다 더 가볍습니다. 무거운 사람부터 순서대로 써 보세요.\n$$수식$${boxone}$$/수식$$, $$수식$${boxtwo}$$/수식$$, $$수식$${boxthree}$$/수식$$\n"
    answer = "(정답)\n① {sa}, ② {sb}, ③ {sc}\n"
    comment = "(해설)\n" \
              "{sa}{n1}는 {sb}{n2}보다 더 무겁고, {sb}{n2}는 {sc}{n3}보다 더 무거우므로 " \
              "무거운 사람부터 순서대로 쓰면 {sa}, {sb}, {sc}입니다.\n\n"

    sa = ['재수', '태영', '철민', '도철', '우중', '재현'][np.random.randint(0, 3)]
    sb = ['호우', '수영', '현정', '민식', '주연', '하영'][np.random.randint(0, 3)]
    sc = ['지호', '지윤', '민정', '유정', '유민', '기석'][np.random.randint(0, 3)]

    n1 = name_jo(sa)
    n2 = name_jo(sb)
    n3 = name_jo(sc)

    boxone = "Box{`````①`````}"
    boxtwo = "Box{`````②`````}"
    boxthree = "Box{`````③`````}"

    stem = stem.format(sa=sa, sb=sb, sc=sc, n1=n1, n2=n2, n3=n3, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree)
    answer = answer.format(sa=sa, sb=sb, sc=sc)
    comment = comment.format(sa=sa, sb=sb, sc=sc, n1=n1, n2=n2, n3=n3)

    return stem, answer, comment


# 1-1-4-13
def compare114_Stem_003():
    stem = "{sa}{j1} {sb}의 무게의 합은 {sd} $$수식$${s12}$$/수식$$개의 무게와 같고, {sc}{j3} {sa}의 무게의 합은 {sd} $$수식$${s13}$$/수식$$개와 같습니다. {sa}{j1} {sd} $$수식$${s1}$$/수식$$개의 무게가 같을 때 무거운 {tp}부터 차례대로 써 보세요.\n$$수식$${boxone}$$/수식$$, $$수식$${boxtwo}$$/수식$$, $$수식$${boxthree}$$/수식$$\n"
    answer = "(정답)\n① {a1}, ② {a2}, ③ {a3}\n"
    comment = "(해설)\n" \
              "{sb}{jj2} {sd} $$수식$${x2}$$/수식$$개의 무게와 같고 " \
              "{sc}{jj3} {sd} $$수식$${x3}$$/수식$$개와 같습니다. " \
              "따라서 {sd}의 수가 많을수록 무거우므로 무거운 {tp}부터 차례로 쓰면 " \
              "{a1}, {a2}, {a3}입니다.\n\n"

    tp = ['책', '옷', '장난감'][np.random.randint(0, 3)]
    if tp == '책':
        stuffs = ['위인전', '사전', '동화책', '소설책', '시집', '문제집', '단어장']
        np.random.shuffle(stuffs)
        sa, sb, sc = stuffs[0:3]
    elif tp == '옷':
        stuffs = ['청바지', '가디건', '니트', '패딩', '후드', '자켓']
        np.random.shuffle(stuffs)
        sa, sb, sc = stuffs[0:3]
    else:
        stuffs = ['곰인형', '물총', '축구공', '요술봉', '로봇', '퍼즐']
        np.random.shuffle(stuffs)
        sa, sb, sc = stuffs[0:3]

    sd = ['쇠구슬', '블록'][np.random.randint(0, 2)]

    j1 = proc_jo(sa, 2)
    j3 = proc_jo(sc, 2)
    jj2 = proc_jo(sb, -1)
    jj3 = proc_jo(sc, -1)

    while True:
        x1 = np.random.randint(1, 4)
        x2 = np.random.randint(1, 4)
        x3 = np.random.randint(1, 5)
        if x1 != x2 and x2 != x3 and x3 != x1:
            break

    s1 = x1
    s12 = x1 + x2
    s13 = x1 + x3

    if (x1 > x2) and (x1 > x3):
        a1 = sa
        if x2 > x3:
            a2 = sb
            a3 = sc
        else:
            a2 = sc
            a3 = sb
    elif (x2 > x1) and (x2 > x3):
        a1 = sb
        if x1 > x3:
            a2 = sa
            a3 = sc
        else:
            a2 = sc
            a3 = sa
    else:
        a1 = sc
        if x1 > x2:
            a2 = sa
            a3 = sb
        else:
            a2 = sb
            a3 = sa

    boxone = "BOX{````①````}"
    boxtwo = "BOX{````②````}"
    boxthree = "BOX{````③````}"

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, tp=tp, j1=j1, j3=j3, s1=s1, s12=s12, s13=s13, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree)
    answer = answer.format(a1=a1, a2=a2, a3=a3)
    comment = comment.format(sb=sb, sc=sc, sd=sd, tp=tp, jj2=jj2, jj3=jj3, x2=x2, x3=x3, a1=a1, a2=a2, a3=a3)

    return stem, answer, comment




# 1-1-4-19
def compare114_Stem_004():
    stem = "다음 중 가장 넓은 것은 무엇인지 찾아 기호를 써 보세요.\n$$표$$㉠ {sa}    ㉡ {sb}\n㉢ {sc}    ㉣ {sd}$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "넓고 오목하게 팬 땅에 물이 괴어 있는 곳이 연못이고, " \
              "하천이나 골짜기를 막아 만든 큰 못이 저수지이며, " \
              "작고 오목한 샘이 옹달샘입니다. " \
              "바다는 지구 위에서 육지를 제외한 나머지 부분입니다.\n" \
              "따라서 가장 넓은 곳은 바다입니다.\n\n"

    candidates = ['바다', '연못', '저수지', '옹달샘']
    np.random.shuffle(candidates)
    sa, sb, sc, sd = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):
        if sdx == '바다':
            correct_idx = idx
            break

    if correct_idx == 0:
        a1 = '㉠'
    elif correct_idx == 1:
        a1 = '㉡'
    elif correct_idx == 2:
        a1 = '㉢'
    else:
        a1 = '㉣'

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(a1=a1)

    return stem, answer, comment


# 1-1-4-21
def compare114_Stem_005():
    stem = "{x1}{j1} {x2}{j2} 겹치면 {sb}에 남는 부분이 있고, {x3}{j3} {x4}{j4} 겹치면 {sc}에 남는 부분이 있습니다. {sa}, {sb}, {sc} 중에서 가장 넓은 것은 어느 것인가요?\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "{x1}{j1} {x2}{j2} 겹치면 {sb}에 남는 부분이 생기므로 {sb}{jj2} 더 넓고, " \
              "{x3}{j3} {x4}{j4} 겹치면 {sc}에 남는 부분이 생기므로 {sc}{jj3} 더 넓습니다. " \
              "따라서 가장 넓은 것은 {a1}입니다.\n\n"

    sa = ['수첩', '단어장', '메모지'][np.random.randint(0, 3)]
    sb = ['만화책', '공책', '교과서', '종합장'][np.random.randint(0, 4)]
    sc = ['달력', '스케치북', '도화지'][np.random.randint(0, 3)]

    a1 = sc

    r1 = np.random.randint(0, 2)
    if r1 == 0:
        x1 = sa
        x2 = sb
    else :
        x1 = sb
        x2 = sa

    r2 = np.random.randint(0, 2)
    if r2 == 0:
        x3 = sc
        x4 = sb
    else :
        x3 = sb
        x4 = sc

    j1 = proc_jo(x1, 2)
    j2 = proc_jo(x2, 1)
    j3 = proc_jo(x3, 2)
    j4 = proc_jo(x4, 1)
    jj2 = proc_jo(sb, 0)
    jj3 = proc_jo(sc, 0)


    stem = stem.format(sa=sa, sb=sb, sc=sc, j1=j1, j2=j2, j3=j3, j4=j4, x1=x1, x2=x2, x3=x3, x4=x4)
    answer = answer.format(a1=a1)
    comment = comment.format(sb=sb, sc=sc, j1=j1, j2=j2, j3=j3, j4=j4, jj2=jj2, jj3=jj3, a1=a1, x1=x1, x2=x2, x3=x3, x4=x4)

    return stem, answer, comment


