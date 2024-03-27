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
    3: "㉣"
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



def num_jo(num):
    # 이
    if bool_jo(num):
        return "이"
    return ""


def name_jo(num):
    # 이
    if bool_jo(num):
        return "이"
    return ""





# 1-1-5-02
def uptofifty115_Stem_001():
    stem = "$$수식$${std}$$/수식$$을 바르게 가르기 한 사람은 누구인가요?\n$$표$${sa} : $$수식$${std}$$/수식$$은 $$수식$${n1}$$/수식$$과 $$수식$${n2}$$/수식$$으로 가를 수 있어.\n{sb} : $$수식$${std}$$/수식$$을 $$수식$${n3}$$/수식$$과 $$수식$${n4}$$/수식$$으로 가르기 해도 돼.$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "$$수식$${std}={s1}+{s2}$$/수식$$, " \
              "$$수식$${std}={s3}+{s4}$$/수식$$\n" \
              "따라서 $$수식$${std}$$/수식$$을 바르게 가르기 한 사람은 {a1}입니다.\n\n"

    sa = ['영우', '지훈', '경호', '성빈', '나연', '세호'][np.random.randint(0, 3)]
    sb = ['가희', '주영', '정민', '희주', '시우', '미연'][np.random.randint(0, 3)]

    std = np.random.randint(10, 12)
    while True:
        n1 = np.random.randint(1, std)
        n3 = np.random.randint(1, std)
        if n1 != n3:
            break

    n2 = std - n1
    n4 = std - n3

    s1 = n1
    s2 = n2
    s3 = n3
    s4 = n4

    pick = np.random.randint(0, 2)
    if pick == 0:
        n2 = n2 + [1, -1][np.random.randint(0, 2)]
        if n2 <= 0:
            n2 += 2
        elif n2 >= std:
            n2 -= 2
        a1 = sb
    else:
        n4 = n4 + [1, -1][np.random.randint(0, 2)]
        if n4 <= 0:
            n4 += 2
        elif n4 >= std:
            n4 -= 2
        a1 = sa

    stem = stem.format(sa=sa, sb=sb, std=std, n1=n1, n2=n2, n3=n3, n4=n4)
    answer = answer.format(a1=a1)
    comment = comment.format(std=std, s1=s1, s2=s2, s3=s3, s4=s4, a1=a1)

    return stem, answer, comment




# 1-1-5-03
def uptofifty115_Stem_002():
    stem = "수의 순서에 맞게 세어 보세요.\n$$수식$${boxone}$$/수식$$─$$수식$${boxtwo}$$/수식$$─$$수식$${boxthree}$$/수식$$─$$수식$${boxfour}$$/수식$$─$$수식$${boxfive}$$/수식$$\n─$$수식$${boxsix}$$/수식$$─$$수식$${boxseven}$$/수식$$─$$수식$${boxeight}$$/수식$$─$$수식$${boxnine}$$/수식$$─$$수식$${boxten}$$/수식$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "일부터 십까지 순서대로 세어 보면\n" \
              "일, 이, 삼, 사, 오, 육, 칠, 팔, 구, 십입니다.\n\n"

    s = ['일', '이', '삼', '사', '오', '육', '칠', '팔', '구', '십']
    index = list(range(0, 10))
    pick = random.sample(index, 5)
    pick.sort()
    a1 = ""

    for i in range(0, 5):
        a1 = a1 + s[pick[i]]
        s[pick[i]] = "　"
        if i < 4:
            a1 = a1 + ", "

    boxone = "BOX{````%s````}" % s[0]
    boxtwo = "BOX{````%s````}" % s[1]
    boxthree = "BOX{````%s````}" % s[2]
    boxfour = "BOX{````%s````}" % s[3]
    boxfive = "BOX{````%s````}" % s[4]
    boxsix = "BOX{````%s````}" % s[5]
    boxseven = "BOX{````%s````}" % s[6]
    boxeight = "BOX{````%s````}" % s[7]
    boxnine = "BOX{````%s````}" % s[8]
    boxten = "BOX{````%s````}" % s[9]

    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour, boxfive=boxfive, boxsix=boxsix, boxseven=boxseven, boxeight=boxeight, boxnine=boxnine, boxten=boxten)
    answer = answer.format(a1=a1)

    return stem, answer, comment




# 1-1-5-04
def uptofifty115_Stem_003():
    stem = "상황에 맞게 밑줄 친 수를 순서대로 읽어 보세요.\n$$표$$$$수식$${y1}$$/수식$${sa} 동안 {sb} $$수식$${y2}$$/수식$${sc} {sd}.$$/표$$\n"
    answer = "(정답)\n{a1}, {a2}\n"
    comment = "(해설)\n" \
              "수는 상황에 따라 다르게 읽습니다.\n" \
              "$$수식$${x1}$$/수식$${sa} 동안 {sb} $$수식$${x2}$$/수식$${sc} {sd}.\n" \
              "→ {a1}{sa} 동안 {sb} {a2}{sc} {sd}.\n\n"

    x1 = np.random.randint(10, 20)
    x2 = np.random.randint(10, 20)

    y1 = "under{%d}" % x1
    y2 = "under{%d}" % x2

    [sa, sb, sc, sd] = [['일', '책을', '권', '읽었어'],
                        ['일', '문제집을', '권', '풀었어'],
                        ['분', '귤을', '개', '먹었어'],
                        ['분', '사과를', '개', '먹었어'],
                        ['개월', '메시지가', '개', '왔어'],
                        ['개월', '소포가', '개', '왔어'],
                        ['초', '자동차가', '대', '지나갔어']][np.random.randint(0, 7)]

    match1 = ['십', '십일', '십이', '십삼', '십사', '십오', '십육', '십칠', '십팔', '십구']
    match2 = ['열', '열한', '열두', '열세', '열네', '열다섯', '열여섯', '열일곱', '열여덟', '열아홉']

    a1 = match1[x1-10]
    a2 = match2[x2-10]

    stem = stem.format(y1=y1, y2=y2, sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(x1=x1, x2=x2, sa=sa, sb=sb, sc=sc, sd=sd, a1=a1, a2=a2)

    return stem, answer, comment































# 1-1-5-05
def uptofifty115_Stem_004():
    stem = "{std}부터 거꾸로 세어 보려고 합니다. $$수식$${boxblank}$$/수식$$ 안에 알맞은 말은 어느 것인가요?\n$$표$$ {std} ─ {s1} ─ {s2} ─ {s3} ─ $$수식$${boxblank}$$/수식$$ $$/표$$\n① {c1}    ② {c2}    ③ {c3}\n④ {c4}    ⑤ {c5}\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "거꾸로 세는 것은 순서가 반대로 되게 세는 것입니다. " \
              "{std}부터 거꾸로 세면 {std}, {s1}, {s2}, {s3}, {s4}, $$수식$$CDOTS$$/수식$$입니다.\n\n"

    boxblank = "□"

    match1 = ['일', '이', '삼', '사', '오',
              '육', '칠', '팔', '구', '십',
              '십일', '십이', '십삼', '십사', '십오',
              '십육', '십칠', '십팔', '십구']
    match2 = ['하나', '둘', '셋', '넷', '다섯',
              '여섯', '일곱', '여덟', '아홉', '열',
              '열하나', '열둘', '열셋', '열넷', '열다섯',
              '열여섯', '열일곱', '열여덟', '열아홉']

    stdnum = np.random.randint(10, 15)
    std = match2[stdnum - 1]
    s1 = match2[stdnum - 2]
    s2 = match2[stdnum - 3]
    s3 = match2[stdnum - 4]
    s4 = match2[stdnum - 5]

    candidates = [match1[stdnum - 5], match2[stdnum - 5],
                  match2[stdnum - 6],
                  match1[stdnum - 7], match2[stdnum - 7]]
    np.random.shuffle(candidates)
    [c1, c2, c3, c4, c5] = candidates

    for i in range(0, 5):
        if candidates[i] == s4:
            a1 = answer_dict[i]

    stem = stem.format(boxblank=boxblank, std=std, s1=s1, s2=s2, s3=s3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(a1=a1)
    comment = comment.format(std=std, s1=s1, s2=s2, s3=s3, s4=s4)

    return stem, answer, comment










































# 1-1-5-09
def uptofifty115_Stem_005():
    stem = "다음 중 수를 잘못 읽은 것은 어느 것인가요?\n① {c1}    ② {c2}    ③ {c3}\n④ {c4}    ⑤ {c5}\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "{a1} {ans1} 또는 {ans2}{j1}라고 읽습니다.\n\n"

    match1 = ['십일', '십이', '십삼', '십사', '십오', '십육', '십칠', '십팔', '십구']
    match2 = ['열하나', '열둘', '열셋', '열넷', '열다섯', '열여섯', '열일곱', '열여덟', '열아홉']

    index = list(range(0, 9))
    pick = random.sample(index, 5)
    pick_ans = np.random.randint(0, 5)

    candidates = []
    for i in range(0, 5):
        flag = np.random.randint(0, 2)
        if i == pick_ans:
            a1 = answer_dict[i]
            ans1 = match1[pick[i]]
            ans2 = match2[pick[i]]
            if flag == 0:
                candidates.append(match1[pick[i]][0]+match2[pick[i]][1:])
            else:
                candidates.append(match2[pick[i]][0]+match1[pick[i]][1:])
        else:
            if flag == 0:
                candidates.append(match1[pick[i]])
            else:
                candidates.append(match2[pick[i]])

    c1, c2, c3, c4, c5 = candidates
    j1 = num_jo(ans2)

    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(a1=a1)
    comment = comment.format(a1=a1, ans1=ans1, ans2=ans2, j1=j1)

    return stem, answer, comment















































# 1-1-5-10
def uptofifty115_Stem_006():
    stem = "다음 중 나타내는 수가 다른 하나를 찾아 써보세요.\n$$표$$  {c1}  {c2}  {c3}  {c4}  $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "수로 나타내면\n" \
              "{s1}: $$수식$${s3}$$/수식$$, {s2}: $$수식$${s3}$$/수식$$, {a1}: $$수식$${a2}$$/수식$$\n" \
              "따라서 나타내는 수가 다른 하나는 {a1}입니다.\n\n"

    match1 = ['십일', '십이', '십삼', '십사', '십오', '십육', '십칠', '십팔', '십구']
    match2 = ['열하나', '열둘', '열셋', '열넷', '열다섯', '열여섯', '열일곱', '열여덟', '열아홉']

    index = list(range(0, 9))
    pick = random.sample(index, 2)

    flag = np.random.randint(0, 2)

    if flag == 0:
        a1 = match1[pick[0]]
    else:
        a1 = match2[pick[0]]

    a2 = pick[0]+11

    candidates = [match1[pick[1]], match2[pick[1]], a1, pick[1]+11]
    np.random.shuffle(candidates)
    [c1, c2, c3, c4] = candidates

    if c1 == pick[1] + 11 :
        c1 = "$$수식$$ %d $$/수식$$" % c1
    elif c2 == pick[1] + 11 :
        c2 = "$$수식$$ %d $$/수식$$" % c2
    elif c3 == pick[1] + 11 :
        c3 = "$$수식$$ %d $$/수식$$" % c3
    elif c4 == pick[1] + 11 :
        c4 = "$$수식$$ %d $$/수식$$" % c4

    candidates.remove(a1)
    candidates.remove(pick[1]+11)
    s1 = candidates[0]
    s2 = candidates[1]
    s3 = pick[1]+11

    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4)
    answer = answer.format(a1=a1)
    comment = comment.format(a1=a1, a2=a2, s1=s1, s2=s2, s3=s3)

    return stem, answer, comment













































# 1-1-5-11
def uptofifty115_Stem_007():
    stem = "{sa}{j1}는 {sb}{j2} $$수식$$10$$/수식$$개 가지고 있었는데 마트에서 {sb} $$수식$${x1}$$/수식$$개를 더 샀습니다. {sa}{j1}가 가지고 있는 전체 {sb} 수를 두 가지 방법으로 읽어 보시오.\n"
    answer = "(정답)\n{a1}, {a2}\n"
    comment = "(해설)\n" \
              "$$수식$$10$$/수식$$개씩 묶음 $$수식$$1$$/수식$$개를 가지고 있고 " \
              "{sb} $$수식$${x1}$$/수식$$개를 더 샀으므로 " \
              "{sa}{j1}가 가지고 있는 {sb}의 수는 $$수식$${a3}$$/수식$$입니다.\n" \
              "따라서 $$수식$${a3}$$/수식$${j3} 두 가지 방법으로 읽으면 {a1} 또는 {a2}입니다.\n\n"

    sa = ['형식', '지원', '소연', '혜정', '은수', '보람'][np.random.randint(0, 4)]
    j1 = name_jo(sa)
    sb = ['초콜릿', '젤리', '사과', '머핀'][np.random.randint(0, 4)]
    j2 = proc_jo(sb, 1)

    match1 = ['십일', '십이', '십삼', '십사', '십오', '십육', '십칠', '십팔', '십구']
    match2 = ['열하나', '열둘', '열셋', '열넷', '열다섯', '열여섯', '열일곱', '열여덟', '열아홉']

    x1 = np.random.randint(1, 10)
    a3 = 10 + x1
    a1 = match1[x1-1]
    a2 = match2[x1-1]
    j3 = proc_jo(a1, 1)

    stem = stem.format(sa=sa, j1=j1, sb=sb, j2=j2, x1=x1)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(sa=sa, j1=j1, sb=sb, x1=x1, a1=a1, a2=a2, a3=a3, j3=j3)

    return stem, answer, comment












































# 1-1-5-17
def uptofifty115_Stem_008():
    stem = "다음 중 $$수식$${x1}$$/수식$${j1} $$수식$${x5}$$/수식$$ 사이에 있는 수를 찾아 써 보세요.\n$$표$${boxone},  {boxtwo},  {boxthree}$$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "{c1}: $$수식$${s1}$$/수식$$, {c2}: $$수식$${s2}$$/수식$$, {c3}: $$수식$${s3}$$/수식$$\n" \
              "$$수식$${x1}$$/수식$${j1} $$수식$${x5}$$/수식$$ 사이에 있는 수를 순서대로 쓰면 " \
              "$$수식$${x2}$$/수식$$, $$수식$${x3}$$/수식$$, $$수식$${x4}$$/수식$$입니다. " \
              "따라서 $$수식$${x1}$$/수식$${j1} $$수식$${x5}$$/수식$$ 사이에 있는 수는 {a1}입니다.\n\n"

    match1 = ['십', '십일', '십이', '십삼', '십사', '십오',
              '십육', '십칠', '십팔', '십구', '이십']
    match2 = ['열', '열하나', '열둘', '열셋', '열넷', '열다섯',
              '열여섯', '열일곱', '열여덟', '열아홉', '스물']

    x1 = np.random.randint(11, 15)
    x2 = x1 + 1
    x3 = x1 + 2
    x4 = x1 + 3
    x5 = x1 + 4
    j1 = proc_jo(match1[x1 - 10], 2)

    p1 = x2 + np.random.randint(0, 3)
    p2 = x1 - np.random.randint(0, 2)
    p3 = x5 + np.random.randint(0, 2)
    a2 = p1

    candidates = [p1, p2, p3]
    np.random.shuffle(candidates)
    [s1, s2, s3] = candidates
    flag = np.random.randint(0, 2)
    if flag == 0:
        a1 = match1[a2 - 10]
        c1 = match1[s1 - 10]
        c2 = match1[s2 - 10]
        c3 = match1[s3 - 10]
    else:
        a1 = match2[a2 - 10]
        c1 = match2[s1 - 10]
        c2 = match2[s2 - 10]
        c3 = match2[s3 - 10]

    boxone = "%s" % c1
    boxtwo = "%s" % c2
    boxthree = "%s" % c3

    stem = stem.format(x1=x1, j1=j1, x5=x5, c1=c1, c2=c2, c3=c3, boxone=boxone, boxtwo=boxtwo, boxthree=boxthree)
    answer = answer.format(a1=a1)
    comment = comment.format(c1=c1, c2=c2, c3=c3, s1=s1, s2=s2, s3=s3, a1=a1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, j1=j1)

    return stem, answer, comment














































# 1-1-5-18
def uptofifty115_Stem_009():
    stem = "보기를 보고 빈칸을 채워 말해 보세요.\n$$표$$[보기]\n{sa}{j1} $$수식$$10$$/수식$$개씩 $$수식$${x2}$$/수식$$묶음 있으면 $$수식$${x1}$$/수식$$개입니다. $$/표$$\n{sb}{j2} $$수식$$10$$/수식$$개씩 $$수식$${boxoneone}$$/수식$$묶음 있으면 $$수식$${boxtwotwo}$$/수식$$개입니다.\n"
    answer = "(정답)\n① $$수식$${x4}$$/수식$$, ② $$수식$${x3}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${x3}$$/수식$$은 {sb}{j2} $$수식$$10$$/수식$$개씩 묶음이 " \
              "$$수식$${x4}$$/수식$$개입니다.\n\n"

    sa = ['달걀', '사과', '귤', '머핀', '야구공'][np.random.randint(0, 4)]
    sb = ['구슬', '인형', '지우개', '고무줄', '컵'][np.random.randint(0, 5)]

    j1 = proc_jo(sa, 0)
    j2 = proc_jo(sb, 0)

    while True:
        x2 = np.random.randint(1, 6)
        x4 = np.random.randint(1, 6)
        if x2 != x4:
            break

    x1 = 10 * x2
    x3 = 10 * x4

    boxone = "%d" % x1
    boxtwo = "%d" % x3

    boxoneone = "BOX{````①````}"
    boxtwotwo = "BOX{````②````}"

    stem = stem.format(sa=sa, sb=sb, j1=j1, j2=j2, x1=x1, x2=x2, x3=x3, x4=x4, boxone=boxone, boxtwo=boxtwo, boxoneone=boxoneone, boxtwotwo=boxtwotwo)
    answer = answer.format(x3=x3, x4=x4)
    comment = comment.format(x3=x3, x4=x4, sb=sb, j2=j2)

    return stem, answer, comment




# 1-1-5-19
def uptofifty115_Stem_010():
    stem = "잘못 읽은 것을 찾아 기호를 써 보세요.\n$$표$$㉠ $$수식$${x1}$$/수식$$ ─ {c1}\n㉡ $$수식$${x2}$$/수식$$ ─ {c2}\n㉢ $$수식$${x3}$$/수식$$ ─ {c3}\n㉣ $$수식$${x4}$$/수식$$ ─ {c4}  $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "$$수식$${a2}$$/수식$${j1} {a3} 또는 {a4}{j2}라고 읽습니다.\n\n"

    match = [['열', '스물', '서른', '마흔', '쉰'],
             ['십', '이십', '삼십', '사십', '오십']]

    nums = [1, 2, 3, 4, 5]
    np.random.shuffle(nums)
    x = [nums[0], nums[1], nums[2], nums[3]]

    candidates = []
    for i in range(0, 4):
        candidates.append(match[np.random.randint(0, 2)][x[i] - 1])

    flaw = np.random.randint(0, 4)
    a1 = answer_kodict[flaw]
    a2 = x[flaw]*10
    a3 = match[0][x[flaw] - 1]
    a4 = match[1][x[flaw] - 1]
    j1 = proc_jo(a4, -1)
    j2 = num_jo(a4)

    for i in range(0, 4):
        x[i] *= 10
    [x1, x2, x3, x4] = x

    while True:
        temp = match[np.random.randint(0, 2)][np.random.randint(0, 5)]
        if temp != a3 and temp != a4:
            flag = True
            for i in range(0, 4):
                if temp == candidates[i]:
                    flag = False
                    break
            if flag:
                candidates[flaw] = temp
                break

    [c1, c2, c3, c4] = candidates

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, c1=c1, c2=c2, c3=c3, c4=c4)
    answer = answer.format(a1=a1)
    comment = comment.format(a2=a2, a3=a3, a4=a4, j1=j1, j2=j2)

    return stem, answer, comment




# 1-1-5-20
def uptofifty115_Stem_011():
    stem = "낱개의 수가 다른 것을 찾아 써 보세요.\n$$표$$ {c1}   {c2}   {c3}   {c4}  $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "수로 나타내면 {s1}{j1}  $$수식$${p1}$$/수식$$, {s2}{j2} $$수식$${p2}$$/수식$$, {s3}{j3} $$수식$${p3}$$/수식$$입니다.\n" \
              "$$수식$${q1}$$/수식$$, $$수식$${q2}$$/수식$$, $$수식$${q3}$$/수식$$의 낱개의 수는 $$수식$${std}$$/수식$$이고, " \
              "{a2}의 낱개의 수는 $$수식$${a3}$$/수식$$이므로 낱개의 수가 다른 것은 {a2}입니다.\n\n"

    match10 = [['십', '이십', '삼십', '사십', '오십'],
               ['열', '스물', '서른', '마흔', '쉰']]
    match1 = [['일', '이', '삼', '사', '오', '육', '칠', '팔', '구'],
              ['하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉']]

    pick10 = random.sample(list(range(0, 5)), 4)
    pick1 = random.sample(list(range(0, 9)), 2)
    std = pick1[0] + 1
    a3 = pick1[1] + 1

    while True:
        flaw = np.random.randint(0, 4)
        realnum = np.random.randint(0, 4)
        if flaw != realnum:
            break

    c = []
    s = []
    p = []
    q = []
    for i in range(0, 4):
        one = np.random.randint(0, 2)
        if i == flaw:
            c.append(match10[one][pick10[i]] + match1[one][pick1[1]])
            s.append(match10[one][pick10[i]] + match1[one][pick1[1]])
            p.append((pick10[i]+1)*10 + pick1[1] + 1)
            a2 = (pick10[i]+1)*10 + pick1[1] + 1
        elif i == realnum:
            c.append((pick10[i]+1)*10 + pick1[0] + 1)
            q.append((pick10[i]+1)*10 + pick1[0] + 1)
        else:
            c.append(match10[one][pick10[i]] + match1[one][pick1[0]])
            s.append(match10[one][pick10[i]] + match1[one][pick1[0]])
            p.append((pick10[i]+1)*10 + pick1[0] + 1)
            q.append((pick10[i]+1)*10 + pick1[0] + 1)

    [c1, c2, c3, c4] = c
    a1 = c[flaw]

    if type(c1) == int :
        c1 = "$$수식$$ %d $$/수식$$" % c1
    elif type(c2) == int :
        c2 = "$$수식$$ %d $$/수식$$" % c2
    elif type(c3) == int :
        c3 = "$$수식$$ %d $$/수식$$" % c3
    elif type(c4) == int :
        c4 = "$$수식$$ %d $$/수식$$" % c4

    [s1, s2, s3] = s
    j1 = proc_jo(s1, -1)
    j2 = proc_jo(s2, -1)
    j3 = proc_jo(s3, -1)

    [p1, p2, p3] = p
    q.sort()
    [q1, q2, q3] = q

    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4)
    answer = answer.format(a1=a1)
    comment = comment.format(s1=s1, s2=s2, s3=s3, j1=j1, j2=j2, j3=j3,
                             p1=p1, p2=p2, p3=p3, q1=q1, q2=q2, q3=q3,
                             std=std, a2=a2, a3=a3)

    return stem, answer, comment




# 1-1-5-22
def uptofifty115_Stem_012():
    stem = "{sa}{j1}는 {sb}를 도와드리고 {sc}에게 {sd} $$수식$${x1}$$/수식$$개를 받았습니다. {sd}{j4} 한 봉지에 $$수식$$10$$/수식$$개씩 담으면 몇 봉지가 되나요?\n"
    answer = "(정답)\n$$수식$${x2}$$/수식$$봉지\n"
    comment = "(해설)\n" \
              "{sd} $$수식$${x1}$$/수식$$개는 $$수식$$10$$/수식$$개씩 " \
              "$$수식$${x2}$$/수식$$묶음이므로 $$수식$${x2}$$/수식$$봉지가 됩니다.\n\n"

    sa = ['정현', '주호', '설아', '민재', '효진'][np.random.randint(0, 5)]
    sb = ['집 청소', '빨래', '설거지', '식사 준비', '분리수거'][np.random.randint(0, 5)]
    sc = ['어머니', '아버지', '힐머니', '할아버지'][np.random.randint(0, 4)]
    sd = ['사탕', '젤리', '초콜릿', '동전'][np.random.randint(0, 4)]

    j1 = name_jo(sa)
    j4 = proc_jo(sd, 1)

    x2 = np.random.randint(2, 6)
    x1 = 10 * x2

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd, j1=j1, j4=j4, x1=x1)
    answer = answer.format(x2=x2)
    comment = comment.format(sd=sd, x1=x1, x2=x2)

    return stem, answer, comment




# 1-1-5-23
def uptofifty115_Stem_013():
    stem = "{sa}{j1}는 {sb}{j2} $$수식$$10$$/수식$$개씩 $$수식$${x1}$$/수식$$봉지와 낱개 $$수식$${x2}$$/수식$$개를 가지고 있습니다. 이 중에서 {sc}에게 {sb}{j2} $$수식$$10$$/수식$$개씩 $$수식$${x3}$$/수식$$번 주었습니다. 남아 있는 {sb}{jj2} 몇 개 인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$10$$/수식$$개씩 $$수식$${x3}$$/수식$$번이면 " \
              "$$수식$${x3}$$/수식$$봉지를 준 것이므로 남아 있는 {sb}{jj2} " \
              "$$수식$$10$$/수식$$개씩 $$수식$${x4}$$/수식$$봉지와 " \
              "낱개 $$수식$${x2}$$/수식$$개입니다.\n" \
              "따라서 남아 있는 {sb}{jj2} $$수식$${a1}$$/수식$$개입니다."

    sa = ['준석', '미연', '혜윤', '재정', '서진', '재중'][np.random.randint(0, 6)]
    sb = ['과자', '사탕', '젤리', '초콜릿', '동전'][np.random.randint(0, 4)]
    sc = ['동생', '친구', '이웃집 꼬마'][np.random.randint(0, 3)]

    j1 = name_jo(sa)
    j2 = proc_jo(sb, 1)
    jj2 = proc_jo(sb, -1)

    x1 = np.random.randint(3, 6)
    x2 = np.random.randint(1, 10)
    x3 = np.random.randint(1, 4)
    x4 = x1 - x3
    a1 = x1*10 + x2 - x3*10

    stem = stem.format(sa=sa, sb=sb, sc=sc, j1=j1, j2=j2, jj2=jj2, x1=x1, x2=x2, x3=x3)
    answer = answer.format(a1=a1)
    comment = comment.format(sb=sb, jj2=jj2, x2=x2, x3=x3, x4=x4, a1=a1)

    return stem, answer, comment




# 1-1-5-25
def uptofifty115_Stem_014():
    stem = "다음은 수를 순서대로 쓴 것입니다. ㉠에 알맞은 수를 써넣으세요.\n$$표$$$$수식$${boxone}$$/수식$$─$$수식$${boxtwo}$$/수식$$─$$수식$${boxblank}$$/수식$$─$$수식$${boxblank}$$/수식$$─$$수식$${boxthree}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${x1}$$/수식$$부터 수를 순서대로 써 보면 " \
              "$$수식$${x1}$$/수식$$, $$수식$${x2}$$/수식$$, $$수식$${x3}$$/수식$$, " \
              "$$수식$${x4}$$/수식$$, $$수식$${x5}$$/수식$$, $$수식$$ CDOTS CDOTS $$/수식$$이므로 " \
              "㉠에 알맞은 수는 $$수식$${a1}$$/수식$$입니다.\n\n"

    x1 = np.random.randint(11, 47)
    x2 = x1 + 1
    x3 = x1 + 2
    x4 = x1 + 3
    x5 = x1 + 4

    a1 = x5

    boxone = "%d" % x1
    boxtwo = "%d" % x2
    boxthree = "㉠"
    boxblank = "□"

    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxblank=boxblank)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, a1=a1)

    return stem, answer, comment




# 1-1-5-26
def uptofifty115_Stem_015():
    stem = "순서를 거꾸로 하여 쓸 때 ㉠에 알맞은 수를 두 가지 방법으로 읽어 보세요.\n$$표$$$$수식$${boxone}$$/수식$$─$$수식$${boxtwo}$$/수식$$─$$수식$${boxblank}$$/수식$$─$$수식$${boxblank}$$/수식$$─$$수식$${boxthree}$$/수식$$$$/표$$\n"
    answer = "(정답)\n{a1}, {a2}\n"
    comment = "(해설)\n" \
              "$$수식$${x1}$$/수식$$부터 수의 순서를 거꾸로 하여 쓰면 " \
              "$$수식$${x1}$$/수식$$, $$수식$${x2}$$/수식$$, $$수식$${x3}$$/수식$$, " \
              "$$수식$${x4}$$/수식$$, $$수식$${x5}$$/수식$$입니다.\n" \
              "따라서 ㉠에 알맞은 수는 $$수식$${x5}$$/수식$$이므로 " \
              "$$수식$${x5}$$/수식$$을 읽어 보면 {a1}, {a2}입니다.\n\n"

    x1 = np.random.randint(15, 51)
    x2 = x1 - 1
    x3 = x1 - 2
    x4 = x1 - 3
    x5 = x1 - 4

    match10 = [['십', '이십', '삼십', '사십', '오십'],
               ['열', '스물', '서른', '마흔', '쉰']]
    match1 = [['일', '이', '삼', '사', '오', '육', '칠', '팔', '구'],
              ['하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉']]

    div = (int)(x5 / 10) - 1
    rem = x5 % 10
    if rem == 0:
        a1 = match10[0][div]
        a2 = match10[1][div]
    else:
        a1 = match10[0][div] + match1[0][rem - 1]
        a2 = match10[1][div] + match1[1][rem - 1]

    boxone = "%d" % x1
    boxtwo = "%d" % x2
    boxblank = "□"
    boxthree = "㉠"

    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxblank=boxblank, boxthree=boxthree)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, a1=a1, a2=a2)

    return stem, answer, comment




# 1-1-5-27
def uptofifty115_Stem_016():
    stem = "{sa}{j1}와 {sb}{j2}는 {sc}에 갔습니다. 순서를 기다리기 위해 {sa}{j1}가 번호표를 뽑자 $$수식$${x1}$$/수식$$번이 나왔고, {sb}{j2}는 바로 뒤의 번호가 나왔습니다. {sb}{j2}가 뽑은 번호표는 몇 번인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${x1}$$/수식$$의 바로 뒤의 수는 " \
              "$$수식$${a1}$$/수식$$이므로 {sb}{j2}가 뽑은 번호표는 " \
              "$$수식$${a1}$$/수식$$입니다.\n\n"

    sa = ['진주', '민현', '호정', '선호', '영석', '나윤'][np.random.randint(0, 6)]
    sb = ['현희', '현중', '보민', '영범', '세령', '대희'][np.random.randint(0, 6)]
    sc = ['은행', '보건소', '구청', '동사무소', '시청'][np.random.randint(0, 5)]

    j1 = name_jo(sa)
    j2 = name_jo(sb)

    x1 = np.random.randint(11, 50)
    a1 = x1 + 1

    stem = stem.format(sa=sa, sb=sb, sc=sc, j1=j1, j2=j2, x1=x1)
    answer = answer.format(a1=a1)
    comment = comment.format(a1=a1, x1=x1, sb=sb, j2=j2)

    return stem, answer, comment




# 1-1-5-28
def uptofifty115_Stem_017():
    stem = "$$수식$${x1}$$/수식$$와 $$수식$${x2}$$/수식$$ 사이에 있는 수를 모두 찾아 써 보세요.\n$$표$$ $$수식$${c1}$$/수식$$  $$수식$${c2}$$/수식$$  $$수식$${c3}$$/수식$$  $$수식$${c4}$$/수식$$  $$수식$${c5}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${x1}$$/수식$$와 $$수식$${x2}$$/수식$$ 사이에 있는 수를 " \
              "순서대로 쓰면 $$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, " \
              "$$수식$${s3}$$/수식$$입니다.\n\n"

    x1 = np.random.randint(11, 47)
    x2 = x1 + 4
    s1 = x1 + 1
    s2 = x1 + 2
    s3 = x1 + 3

    s = random.sample([s1, s2, s3], 2)
    s.sort()
    a1 = s[0]
    a2 = s[1]

    c = random.sample(list(range(11, x1))+list(range(x2, 50)), 3)
    c.append(a1)
    c.append(a2)
    c.sort()
    [c1, c2, c3, c4, c5] = c

    stem = stem.format(x1=x1, x2=x2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(x1=x1, x2=x2, s1=s1, s2=s2, s3=s3)

    return stem, answer, comment




# 1-1-5-30
def uptofifty115_Stem_018():
    stem = "규칙을 찾아 ㉠과 ㉡에 알맞은 수를 각각 구해 보세요.\n$$표$$$$수식$${boxone}$$/수식$$ ─ $$수식$${boxtwo}$$/수식$$ ─ $$수식$${boxthree}$$/수식$$ ─ $$수식$${boxfour}$$/수식$$ ─ $$수식$${boxfive}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${std}$$/수식$$씩 {rule} 규칙이므로 " \
              "㉠은 $$수식$${s1}$$/수식$$보다 $$수식$${std}$$/수식$$ {rule1} 수인 " \
              "$$수식$${a1}$$/수식$$, " \
              "㉡은 $$수식$${s2}$$/수식$$보다 $$수식$${std}$$/수식$$ {rule1} 수인 " \
              "$$수식$${a2}$$/수식$$입니다.\n\n"

    rule = ['작아지는', '커지는'][np.random.randint(0, 2)]
    std = np.random.randint(2, 6)

    c = []

    if rule == '작아지는':
        rule1 = '작은'
        c.append(np.random.randint(10 + std*4, 51))
        for i in range(0, 4):
            c.append(c[i] - std)
    else:
        rule1 = '큰'
        c.append(np.random.randint(10, 51 - std*4))
        for i in range(0, 4):
            c.append(c[i] + std)

    blanks = random.sample(list(range(1, 5)), 2)
    blanks.sort()

    a1 = c[blanks[0]]
    a2 = c[blanks[1]]
    s1 = c[blanks[0] - 1]
    s2 = c[blanks[1] - 1]

    c[blanks[0]] = '㉠'
    c[blanks[1]] = '㉡'

    [c1, c2, c3, c4, c5] = c

    boxone = "%s" % c1
    boxtwo = "%s" % c2
    boxthree = "%s" % c3
    boxfour = "%s" % c4
    boxfive = "%s" % c5

    stem = stem.format(boxone=boxone, boxtwo=boxtwo, boxthree=boxthree, boxfour=boxfour, boxfive=boxfive)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(std=std, rule=rule, rule1=rule1, s1=s1, s2=s2, a1=a1, a2=a2)

    return stem, answer, comment




# 1-1-5-31
def uptofifty115_Stem_019():
    stem = "가장 큰 수와 가장 작은 수를 각각 찾아 써 보세요.\n$$표$$ $$수식$${c1}$$/수식$$  $$수식$${c2}$$/수식$$  $$수식$${c3}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a2}$$/수식$$, $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$10$$/수식$$개씩 묶음의 수를 비교하면 " \
              "$$수식$${c1}$$/수식$$와 $$수식$${c2}$$/수식$$가 " \
              "$$수식$${c3}$$/수식$$보다 {compare1}.\n" \
              "낱개의 수를 비교하면 $$수식$${c1}$$/수식$$가 " \
              "$$수식$${c2}$$/수식$$보다 {compare2} " \
              "가장 작은 수는 $$수식$${a1}$$/수식$$이고, " \
              "가장 큰 수는 $$수식$${a2}$$/수식$$입니다.\n\n"

    ten = random.sample(list(range(1, 5)), 2)
    one = random.sample(list(range(1, 10)), 3)

    c1 = ten[0]*10 + one[0]
    c2 = ten[0]*10 + one[1]
    c3 = ten[1]*10 + one[2]

    if ten[0] < ten[1]:
        compare1 = '작습니다'
        a2 = c3
        if c1 < c2:
            compare2 = '작으므로'
            a1 = c1
        else:
            compare2 = '크므로'
            a1 = c2
    else:
        compare1 = '큽니다'
        a1 = c3
        if c1 > c2:
            compare2 = '크므로'
            a2 = c1
        else:
            compare2 = '작으므로'
            a2 = c2

    stem = stem.format(c1=c1, c2=c2, c3=c3)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(c1=c1, c2=c2, c3=c3, a1=a1, a2=a2, compare1=compare1, compare2=compare2)

    return stem, answer, comment




# 1-1-5-32
def uptofifty115_Stem_020():
    stem = "다음 중 더 큰 수를 찾아 기호를 써 보세요.\n$$표$$ ㉠ {x1}\n ㉡ {x2} $$/표$$\n"
    answer = "(정답)\n{a1}\n"
    comment = "(해설)\n" \
              "수로 나타내면 " \
              "㉠ {y1}" \
              "㉡ {y2}" \
              "$$수식$$10$$/수식$$개씩 묶음의 수는 " \
              "$$수식$${s1}$$/수식$$가 $$수식$${s2}$$/수식$$보다 작으므로 " \
              "{a1}이 더 큰 수입니다.\n\n"

    c1 = [20, 30, 40, 50][np.random.randint(0, 4)]
    match10 = [['십', '이십', '삼십', '사십', '오십'],
               ['열', '스물', '서른', '마흔', '쉰']]
    match1 = [['일', '이', '삼', '사', '오', '육', '칠', '팔', '구'],
              ['하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉']]
    c3 = c1 - 1
    m = np.random.randint(0, 2)
    c2 = match10[m][(int)(c3 / 10) - 1] + match1[m][c3 % 10 - 1]
    j1 = proc_jo(c2, -1)
    s1 = c1 - 1
    s2 = c3 + 1

    flag = [True, False][np.random.randint(0, 2)]
    if flag:
        x1 = "$$수식$${c1}$$/수식$$보다 $$수식$$1$$/수식$$ 작은 수".format(c1=c1)
        x2 = "{c2}보다 $$수식$$1$$/수식$$ 큰 수".format(c2=c2)
        y1 = "$$수식$${c1}$$/수식$$보다 1 작은 수는 " \
             "$$수식$${c1}$$/수식$$ 바로 앞의 수이므로 $$수식$${s1}$$/수식$$입니다.\n".format(c1=c1, s1=s1)
        y2 = "{c2}{j1} $$수식$${c3}$$/수식$$이고 " \
             "$$수식$${c3}$$/수식$$보다 $$수식$$1$$/수식$$ 큰 수는 " \
             "$$수식$${c3}$$/수식$$ 바로 뒤의 수이므로 $$수식$${s2}$$/수식$$입니다.\n".format(c2=c2, c3=c3, s2=s2, j1=j1)
        a1 = '㉡'
    else:
        x2 = "$$수식$${c1}$$/수식$$보다 $$수식$$1$$/수식$$ 작은 수".format(c1=c1)
        x1 = "{c2}보다 $$수식$$1$$/수식$$ 큰 수".format(c2=c2)
        y2 = "$$수식$${c1}$$/수식$$보다 1 작은 수는 " \
             "$$수식$${c1}$$/수식$$ 바로 앞의 수이므로 $$수식$${s1}$$/수식$$입니다.\n".format(c1=c1, s1=s1)
        y1 = "{c2}{j1} $$수식$${c3}$$/수식$$이고 " \
             "$$수식$${c3}$$/수식$$보다 $$수식$$1$$/수식$$ 큰 수는 " \
             "$$수식$${c3}$$/수식$$ 바로 뒤의 수이므로 $$수식$${s2}$$/수식$$입니다.\n".format(c2=c2, c3=c3, s2=s2, j1=j1)
        a1 = '㉠'

    stem = stem.format(x1=x1, x2=x2)
    answer = answer.format(a1=a1)
    comment = comment.format(y1=y1, y2=y2, s1=s1, s2=s2, a1=a1)

    return stem, answer, comment




# 1-1-5-33
def uptofifty115_Stem_021():
    stem = "$$수식$${x1}$$/수식$$보다 큰 수를 모두 찾아 써 보세요.\n$$표$$ $$수식$${c1}$$/수식$$  $$수식$${c2}$$/수식$$  $$수식$${c3}$$/수식$$  $$수식$${c4}$$/수식$$  $$수식$${c5}$$/수식$$ $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$10$$/수식$$개씩 묶음의 수가 같으므로 낱개의 수를 비교하면 " \
              "$$수식$${x1}$$/수식$$보다 큰 수는 " \
              "$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$입니다.\n\n"

    ten = np.random.randint(1, 5)
    one = np.random.randint(2, 8)
    x1 = ten*10 + one

    a = random.sample(list(range(x1+1, (ten+1)*10)), 2)
    a.sort()
    [a1, a2] = a

    c = a + random.sample(list(range(ten*10, x1+1)), 3)
    np.random.shuffle(c)
    [c1, c2, c3, c4, c5] = c

    stem = stem.format(x1=x1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(x1=x1, a1=a1, a2=a2)

    return stem, answer, comment




# 1-1-5-35
def uptofifty115_Stem_022():
    stem = "{sth}{jo} {pp1}{j1} {x1} 개 접었고 {pp2}{j2} $$수식$$10$$/수식$$장씩 묶음 $$수식$${x2}$$/수식$$개와 낱개 $$수식$${x3}$$/수식$$개를 접었습니다. {sth}{jo} 더 많이 모은 어린이는 누구일까요?\n"
    answer = "(정답)\n{aa}\n"
    comment = "(해설)\n" \
              "{x1} → $$수식$${s1}$$/수식$$\n" \
              "$$수식$$10$$/수식$$장씩 묶음 $$수식$${x2}$$/수식$$개와 " \
              "낱개 $$수식$${x3}$$/수식$$개 → $$수식$${s2}$$/수식$$\n" \
              "$$수식$${s1}$$/수식$$와 $$수식$${s2}$$/수식$$ 중에서 더 큰 수를 찾습니다.\n" \
              "$$수식$$10$$/수식$$개씩 묶음의 수가 같으므로 낱개의 수를 비교하면 " \
              "$$수식$${a1}$$/수식$$가 $$수식$${a2}$$/수식$$보다 더 큽니다.\n" \
              "따라서 {sth}{jo} 더 많이 모은 어린이는 {aa}입니다.\n\n"

    sth = ['종이학', '종이별', '종이배', '종이꽃'][np.random.randint(0, 4)]
    jo = proc_jo(sth, 1)
    pp1 = ['영미', '유정', '선아', '예지', '희주', '혜선'][np.random.randint(0, 6)]
    j1 = proc_jo(pp1, -1)
    pp2 = ['경수', '호영', '주호', '민재', '우영', '태진'][np.random.randint(0, 6)]
    j2 = proc_jo(pp2, -1)

    x2 = np.random.randint(1, 5)
    s = random.sample(list(range(1, 10)), 2)
    x3 = s[1]
    s1 = x2*10 + s[0]
    s2 = x2*10 + s[1]

    if s1 > s2:
        aa = pp1
        a1 = s1
        a2 = s2
    else:
        aa = pp2
        a1 = s2
        a2 = s1

    match10 = [['십', '이십', '삼십', '사십', '오십'],
               ['열', '스물', '서른', '마흔', '쉰']]
    match1 = [['일', '이', '삼', '사', '오', '육', '칠', '팔', '구'],
              ['한', '두', '세', '네', '다섯', '여섯', '일곱', '여덟', '아홉']]

    m = np.random.randint(0, 2)
    x1 = match10[m][x2 - 1] + match1[m][s[0] - 1]

    stem = stem.format(sth=sth, jo=jo, pp1=pp1, pp2=pp2, j1=j1, j2=j2, x1=x1, x2=x2, x3=x3)
    answer = answer.format(aa=aa)
    comment = comment.format(x1=x1, x2=x2, x3=x3, s1=s1, s2=s2, a1=a1, a2=a2, aa=aa, sth=sth, jo=jo)

    return stem, answer, comment




# 1-1-5-36
def uptofifty115_Stem_023():
    stem = "조건을 모두 만족하는 수를 구하세요.\n$$표$$$$수식$$LEFT ($$/수식$$가$$수식$$RIGHT ) ```` {x1}$$/수식$$보다 크고 $$수식$${x2}$$/수식$$보다 작습니다.\n$$수식$$LEFT ($$/수식$$나$$수식$$RIGHT ) ```` 10$$/수식$$개씩 묶음의 수와 낱개의 수를 서로 바꾸어도 같은 수가 됩니다.$$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${x1}$$/수식$$보다 크고 $$수식$${x2}$$/수식$$보다 작은 수는 " \
              "$$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, " \
              "$$수식$${s3}$$/수식$$, $$수식$${s4}$$/수식$$입니다. " \
              "이 중에서 $$수식$$10$$/수식$$개씩 묶음의 수와 낱개의 수가 같은 수는 " \
              "$$수식$${a1}$$/수식$$입니다.\n" \
              "따라서 주어진 조건을 만족하는 수는 $$수식$${a1}$$/수식$$입니다.\n\n"

    pick = np.random.randint(1, 5)
    a1 = pick*10 + pick
    x1 = a1 - np.random.randint(1, 5)
    x2 = x1 + 5
    s1 = x1 + 1
    s2 = x1 + 2
    s3 = x1 + 3
    s4 = x1 + 4

    stem = stem.format(x1=x1, x2=x2)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, s1=s1, s2=s2, s3=s3, s4=s4, a1=a1)

    return stem, answer, comment




# 1-1-5-37
def uptofifty115_Stem_024():
    stem = "$$수식$${x1}$$/수식$$보다 크고 $$수식$${x2}$$/수식$$보다 작은 수는 모두 몇 개인가요?\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$ 개\n"
    comment = "(해설)\n" \
              "$$수식$${x1}$$/수식$$보다 큰 수: {s1} $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "$$수식$${x2}$$/수식$$보다 작은 수: {s2} $$수식$$CDOTS CDOTS$$/수식$$\n" \
              "→ $$수식$${x1}$$/수식$$보다 크고 $$수식$${x2}$$/수식$$보다 작은 수는: {a2}\n\n"

    x2 = np.random.randint(15, 51)
    a1 = np.random.randint(3, 8)
    x1 = x2 - a1 - 1

    s1 = ""
    for i in range(1, 6):
        if x1+i > 50:
            break
        s1 += ("$$수식$$"+str(x1+i)+"$$/수식$$")
        s1 += ', '
    s2 = ""
    for i in range(1, 6):
        s2 += ("$$수식$$"+str(x2-i)+"$$/수식$$")
        s2 += ', '
    a2 = ""
    for i in range(x1+1, x2):
        a2 += ("$$수식$$"+str(i)+"$$/수식$$")
        if i != x2 - 1:
            a2 += ', '

    stem = stem.format(x1=x1, x2=x2)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, s1=s1, s2=s2, a2=a2)

    return stem, answer, comment




# 1-1-5-38
def uptofifty115_Stem_025():
    stem = "$$수식$$0$$/수식$$부터 $$수식$$9$$/수식$$까지의 수 중에서 $$수식$${boxblank}$$/수식$$ 안에 들어갈 수 있는 수를 모두 구하세요.\n$$표$$ $$수식$${x1}{boxblank}$$/수식$$는 $$수식$${x2}$$/수식$$보다 크고 $$수식$${x3}$$/수식$$보다 작은 수입니다. $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${x1}{boxblank}$$/수식$$와 $$수식$${s1}$$/수식$$의 " \
              "$$수식$$10$$/수식$$개씩 묶음의 수가 같으므로 낱개의 수를 비교하면 " \
              "$$수식$${boxblank}$$/수식$$는 $$수식$${s2}$$/수식$$보다 {s3} 합니다. " \
              "따라서 $$수식$${boxblank}$$/수식$$ 안에 들어갈 수 있는 수는 " \
              "$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$입니다.\n\n"

    boxblank = "□"

    std = np.random.randint(1, 5)
    a = [[0, 1], [8, 9]][np.random.randint(0, 2)]
    [a1, a2] = a
    if a1 == 0:
        x1 = std + 1
        x2 = std*10 + np.random.randint(0, 10)
        s2 = 2
        s3 = "작아야"
        x3 = (std+1)*10 + 2
        s1 = x3
    else:
        x1 = std
        x3 = (std+1)*10 + np.random.randint(0, 10)
        s2 = 7
        s3 = "커야"
        x2 = std * 10 + 7
        s1 = x2

    stem = stem.format(x1=x1, x2=x2, x3=x3, boxblank=boxblank)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(x1=x1, x2=x2, s1=s1, s2=s2, s3=s3, a1=a1, a2=a2, boxblank=boxblank)

    return stem, answer, comment



# 1-1-5-39
def uptofifty115_Stem_026():
    stem = "㉠부터 ㉡까지의 수 중에서 $$수식$$10$$/수식$$개씩 묶음의 수가 낱개의 수보다 큰 수는 모두 몇 개인가요?\n$$표$$ ㉠ $$수식$$10$$/수식$$개씩 묶음 $$수식$${x1}$$/수식$$개와 낱개 $$수식$${x2}$$/수식$$개인 수\n ㉡ $$수식$${x3}$$/수식$$보다 $$수식$${x4}$$/수식$$ 큰 수 $$/표$$\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$ 개\n"
    comment = "(해설)\n" \
              "㉠ $$수식$$10$$/수식$$개씩 묶음 $$수식$${x1}$$/수식$$개와 " \
              "낱개 $$수식$${x2}$$/수식$$개인 수 → $$수식$${s1}$$/수식$$\n" \
              "㉡ $$수식$${x3}$$/수식$$보다 $$수식$${x4}$$/수식$$ 큰 수 " \
              "→ $$수식$${s2}$$/수식$$\n" \
              "$$수식$${s1}$$/수식$$부터 $$수식$${s2}$$/수식$$까지의 수를 순서대로 쓰면 " \
              "{ss1}입니다. 이 중에서 $$수식$$10$$/수식$$개씩 묶음의 수가 낱개의 수보다 " \
              "큰 수는 {ss2}으로 $$수식$${a1}$$/수식$$개입니다.\n\n"

    while True:
        while True:
            s = random.sample(list(range(11, 51)), 2)
            if abs(s[0]-s[1]) <= 15:
                break
        s.sort()
        [s1, s2] = s
        x1 = (int)(s1 / 10)
        x2 = s1 % 10
        x4 = np.random.randint(1, 6)
        x3 = s2 - x4

        a1 = 0
        ss1 = ""
        ss2 = ""
        for i in range(s1, s2+1):
            ss1 += ("$$수식$$" + str(i) + "$$/수식$$, ")
            ten = (int)(i / 10)
            one = i % 10
            if ten > one:
                a1 += 1
                ss2 += ("$$수식$$"+str(i)+"$$/수식$$, ")
        ss1 = ss1[:len(ss1)-2]
        ss2 = ss2[:len(ss2)-2]
        if a1 != 0:
            break

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4)
    answer = answer.format(a1=a1)
    comment = comment.format(x1=x1, x2=x2, x3=x3, x4=x4, s1=s1, s2=s2, ss1=ss1, ss2=ss2, a1=a1)

    return stem, answer, comment




