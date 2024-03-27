#-*- coding: utf-8 -*- 

import numpy as np
import io
##import matplotlib.pyplot as plt
##from matplotlib import font_manager, rc

import random
import os


answer_dict_0 = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤",
    5: "⑥",
    6: "⑦",
    7: "⑧"
}


answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤",
    5: "⑥",
    6: "⑦",
    7: "⑧"
}




def ClassificationImgPath(path0,path1,imgNum): 
    temps = "Element/Grade2_1/Classify/"+path0+"/"+path1+"/"
    want = temps+str(imgNum).zfill(2)
    return want

"""
def MainTableDesign_0(value_0,value_1,value_2): 
    want = "$$테이블s$$ $$/테이블s$$"
    want += "$$테이블trs$$ $$/테이블trs$$"
    want += "$$테이블tdcol2$$" +value_0+"$$/테이블tdcol2$$"
    want += "$$테이블tre$$ $$/테이블tre$$"
    want += "$$테이블trs$$ $$/테이블trs$$"
    want += "$$테이블td$$"+value_1+"$$/테이블td$$"
    want += "$$테이블td$$"+value_2+"$$/테이블td$$"
    want += "$$테이블tre$$ $$/테이블tre$$"
    want += "$$테이블e$$ $$/테이블e$$"
    return want

def MainTableDesign_1(value_0,value_1,value_2): 
    want = "$$테이블s$$ $$/테이블s$$"
    want += "$$테이블trs$$ $$/테이블trs$$"
    want += "$$테이블td$$"+value_0+"$$/테이블td$$"
    want += "$$테이블td$$"+value_1+"$$/테이블td$$"
    want += "$$테이블tre$$ $$/테이블tre$$"
    want += "$$테이블trs$$ $$/테이블trs$$"
    want += "$$테이블tdcol2$$" +value_2+"$$/테이블tdcol2$$"
    want += "$$테이블tre$$ $$/테이블tre$$"
    want += "$$테이블e$$ $$/테이블e$$"
    return want

"""
classify_img_list = [  ## 폴더 정보 
                        {##0
                            'classification': '옷', 
                            'cnt':4,
                            'list' :[
                                        {'classification': '윗옷', 'cnt':13},
                                        {'classification': '아래옷', 'cnt':17},
                                        {'classification': '악세사리', 'cnt':9},
                                        {'classification': '신발', 'cnt':11}
                                    ]
                        },{##1
                            'classification': '음식', 
                            'cnt':6,
                            'list' :[
                                        {'classification': '빵', 'cnt':14},
                                        {'classification': '고기', 'cnt':6},
                                        {'classification': '과일', 'cnt':9},
                                        {'classification': '채소', 'cnt':8},
                                        {'classification': '분식', 'cnt':5},
                                        {'classification': '햄버거 가게', 'cnt':3}                                   
                                    ]
                        },{##2
                            'classification': '동물', 
                            'cnt':3,
                            'list' :[
                                        {'classification': '땅에 사는 동물', 'cnt':14},
                                        {'classification': '바다에 사는 동물', 'cnt':11},
                                        {'classification': '날아다니는 동물', 'cnt':10}
                                   
                                    ]
                        },{##3
                            'classification': '탈것', 
                            'cnt':3,
                            'list' :[
                                        {'classification': '땅에서 탈 수 있는 것', 'cnt':10},
                                        {'classification': '바다에서 탈 수 있는 것', 'cnt':7},
                                        {'classification': '하늘에서 탈 수 있는 것', 'cnt':10}                                   
                                    ]
                        },{##4
                            'classification': '식물', 
                            'cnt':2,
                            'list' :[
                                        {'classification': '꽃', 'cnt':8},
                                        {'classification': '나무', 'cnt':3}
                                    ]
                        },{ ##5
                            'classification': '기구', 
                            'cnt':3,
                            'list' :[
                                        {'classification': '주방에서 볼수 있는거', 'cnt':13},
                                        {'classification': '거실에서 볼수 있는거', 'cnt':15},
                                        {'classification': '화장실에서 볼수 있는거', 'cnt':4}                                   
                                    ]
                        },{ ##6
                            'classification': '직업', 
                            'cnt':5,
                            'list' :[
                                        {'classification': '의사', 'cnt':3},
                                        {'classification': '군인', 'cnt':2},
                                        {'classification': '소방관', 'cnt':2},
                                        {'classification': '경찰', 'cnt':2},
                                        {'classification': '요리사', 'cnt':2}                                        
                                    ]
                        },{##7
                            'classification': '운동', 
                            'cnt':2,
                            'list' :[
                                        {'classification': '공을 이용한 운동', 'cnt':7},
                                        {'classification': '공을 이용하지 않는 운동', 'cnt':8}
                                    ]
                        },{ ##8
                            'classification': '장난감', 
                            'cnt':1,
                            'list' :[
                                        {'classification': '장난감', 'cnt':10}
                                    ]
                        }
                    ]

wrong_list =["재미있는 것과 재미없는 것","이쁜 꽃과 안 이쁜 꽃","뚱뚱한 아이와 안 뚱뚱한 아이","날씬한 아이와 안 날씬한 아이",
             "맛있는 과일과 맛없는 과일","맛있는 음식과 맛없는 음식","보고 싶은 영화와 안 보고 싶은 영화","이쁜 옷과 안 이쁜 옷",
             "맛있는 채소와 안 맛있는 채소","귀여운 동물과 안 귀여운 동물","어두운 화면과 밝은 화면","빠른 사람과 느린 사람",
             "먼 길과 가까운 길","힘든 운동과 안 힘든 운동","좋아하는 아이와 안 좋아하는 아이","사랑하는 아이와 안 사랑하는 아이"             
             ]
right_list =["평평한 면이 있는 것과 평평한 면이 없는 것","네모와 세모","바지와 점퍼","남자와 여자","안경 쓴 아이와 안 쓴 아이","원기둥과 구","동물과 식물"]

def classification215_Stem_001():
    right_cnt = 1
    right_want_list = random.sample(range(0, len(right_list)) , right_cnt)     
    wrong_want_list = random.sample(range(0, len(wrong_list)) , 5-right_cnt)     
    stem_list = []
    right_wants = []
    for i in range(0,right_cnt):
        stem_list += [right_list[right_want_list[i]]]
        right_wants += [right_list[right_want_list[i]]]
    for i in range(0,5-right_cnt):
        stem_list += [wrong_list[wrong_want_list[i]]]        
    random.shuffle(stem_list)
    if right_cnt >1:
        stem = "분류 기준이 될 수 있는 것을 모두 찾으세요. \n "
    else:
        stem = "분류 기준이 될 수 있는 것을 찾으세요. \n "
    answer = "(정답)\n "
    for i in range(0,len(stem_list) ):
        stem += "\n"+answer_dict[i]+"  "+stem_list[i]
        if stem_list[i] in right_wants: 
            answer += answer_dict[i]+","
    comment = "(해설)\n 사람마다 다를 수 있는 기준은 잘못된 기준입니다. "
    answer = answer[:-1]
    return stem,answer, comment


def classification215_Stem_002():
    stem = "그림을 보고 분류 기준으로 알맞은 것을 선택하세요. \n "
    comment = "(해설)\n"
    img_num_list = [0,1,2,3,4,5,6,7]
    right_num_0 = np.random.randint(0, len(img_num_list))    
    right_num_1 = random.sample(range(0, classify_img_list[right_num_0]['cnt']) , 2)     
    right_word = classify_img_list[right_num_0]['list'][right_num_1[0]]['classification'] +"와 "+ classify_img_list[right_num_0]['list'][right_num_1[1]]['classification']
    img_num_list.remove(right_num_0)
    stem += "$$표$$ "

    img_numlist0 = random.sample(range(0,classify_img_list[right_num_0]['list'][right_num_1[0]]['cnt']),2)
    img_numlist1 = random.sample(range(0,classify_img_list[right_num_0]['list'][right_num_1[1]]['cnt']),2)
    
    comment += classify_img_list[right_num_0]['list'][right_num_1[0]]['classification'] + " : "
    for i in range(0,2):
        stem += " $$이미지$$"+ClassificationImgPath(str(right_num_0).zfill(2),str(right_num_1[0]).zfill(2),img_numlist0[i])+".png"+"$$/이미지$$"   
        comment += " $$이미지$$"+ClassificationImgPath(str(right_num_0).zfill(2),str(right_num_1[0]).zfill(2),img_numlist0[i])+".png"+"$$/이미지$$"   
    comment += " \n "        
    comment += classify_img_list[right_num_0]['list'][right_num_1[1]]['classification'] + " : "        
    for i in range(0,2):
        stem += " $$이미지$$"+ClassificationImgPath(str(right_num_0).zfill(2),str(right_num_1[1]).zfill(2),img_numlist1[i])+".png"+"$$/이미지$$"   
        comment += " $$이미지$$"+ClassificationImgPath(str(right_num_0).zfill(2),str(right_num_1[1]).zfill(2),img_numlist1[i])+".png"+"$$/이미지$$"   
    stem += "$$/표$$ "    
    answer_NUM = np.random.randint(1, 5)
    answer = "(정답)\n " + answer_dict[answer_NUM-1] + "\n "
    
    wrong_num_list = random.sample(range(0,len(img_num_list) ) , 5)
    
    for i in range(1,6):
        if i ==answer_NUM:
            stem += "\n"+answer_dict[i-1] + " " +right_word
        else:
            wrong_num_0 = img_num_list[wrong_num_list[i-1]]
            wrong_num_1 = random.sample(range(0, classify_img_list[wrong_num_0]['cnt']) , 2)     
            wrong_word = classify_img_list[wrong_num_0]['list'][wrong_num_1[0]]['classification'] +"와 "+ classify_img_list[wrong_num_0]['list'][wrong_num_1[1]]['classification']               
            stem += "\n"+answer_dict[i-1] + " " + wrong_word
    answer = answer[:-1]
    return stem,answer, comment





def classification215_Stem_003():
    img_num_list = [0,1,2,3,4,5,6,7]
    right_num_0 = np.random.randint(0, len(img_num_list))    
    right_num_1 = random.sample(range(0, classify_img_list[right_num_0]['cnt']) , 2)     
    right_word = classify_img_list[right_num_0]['list'][right_num_1[0]]['classification'] +"와 "+ classify_img_list[right_num_0]['list'][right_num_1[1]]['classification']
    stem = right_word+ "로 분류 했을 때, 분류 기준이 다른 하나를 선택하세요. \n "
    comment = "(해설)\n"
    right_answer_list =[]
    
    temp_right = random.sample(range(0, classify_img_list[right_num_0]['list'][right_num_1[0]]['cnt'] ) , 2)    
    comment += classify_img_list[right_num_0]['list'][right_num_1[0]]['classification'] + " : "
    for i in range(0,len(temp_right)):
        right_answer_list +=[[right_num_0,right_num_1[0],temp_right[i]]]
        comment += " $$이미지$$"+ClassificationImgPath(str(right_num_0).zfill(2),str(right_num_1[0]).zfill(2),temp_right[i])+".png"+"$$/이미지$$"  

    comment +=  "\n"

    temp_right = random.sample(range(0, classify_img_list[right_num_0]['list'][right_num_1[1]]['cnt'] ) , 2)    
    comment += classify_img_list[right_num_0]['list'][right_num_1[1]]['classification'] + " : "
    for i in range(0,len(temp_right)):
        right_answer_list +=[[right_num_0,right_num_1[1],temp_right[i]]]
        comment += " $$이미지$$"+ClassificationImgPath(str(right_num_0).zfill(2),str(right_num_1[1]).zfill(2),temp_right[i])+".png"+"$$/이미지$$"
    random.shuffle(right_answer_list)
    answer_NUM = np.random.randint(0, 5)
    answer = "(정답)\n " + answer_dict[answer_NUM] + "\n "
    check = 0
    
    
    for i in range(0,5):
        if i ==answer_NUM:
            img_num_list.remove(right_num_0)
            temp_num_0 = np.random.randint(0, len(img_num_list))    
            temp_num_1 = np.random.randint(0, classify_img_list[temp_num_0]['cnt'])    
            temp_num_2 = np.random.randint(0, classify_img_list[temp_num_0]['list'][temp_num_1]['cnt'])    
            stem += "\n"+answer_dict[i] + " $$이미지$$"+ClassificationImgPath(str(temp_num_0).zfill(2),str(temp_num_1).zfill(2),temp_num_2)+".png"+"$$/이미지$$"
        else:
            temp_num_0 = right_answer_list[check][0]
            temp_num_1 = right_answer_list[check][1]
            temp_num_2 = right_answer_list[check][2]
            stem += "\n"+answer_dict[i] + " $$이미지$$"+ClassificationImgPath(str(temp_num_0).zfill(2),str(temp_num_1).zfill(2),temp_num_2)+".png"+"$$/이미지$$"
            check += 1            
    answer = answer[:-1]
    return stem,answer, comment


def classification215_Stem_004():
    img_num_list = [0,1,2,3,4,5,6,7]
    right_num_0 = np.random.randint(0, len(img_num_list))    
    right_num_1 = random.sample(range(0, classify_img_list[right_num_0]['cnt']) , 2)     
    right_word_0 = classify_img_list[right_num_0]['list'][right_num_1[0]]['classification'] 
    right_word_1 = classify_img_list[right_num_0]['list'][right_num_1[1]]['classification']
    stem = "분류 기준에 따라 분류 하세요."
    stem += "$$테이블s$$ $$/테이블s$$"
    stem += "$$테이블trs$$ $$/테이블trs$$"
    stem += "$$테이블td$$"+right_word_0+"$$/테이블td$$"
    stem += "$$테이블td$$"+right_word_1+"$$/테이블td$$"
    stem += "$$테이블tre$$ $$/테이블tre$$"
    stem += "$$테이블e$$ $$/테이블e$$ \n"
    comment = "(해설)\n"
    
    right_answer_list =[]
    if classify_img_list[right_num_0]['list'][right_num_1[0]]['cnt'] >2:
        temp_right = random.sample(range(0, classify_img_list[right_num_0]['list'][right_num_1[0]]['cnt'] ) , 3)    
    else:        
        temp_right = random.sample(range(0, classify_img_list[right_num_0]['list'][right_num_1[0]]['cnt'] ) , 2)    
    comment += classify_img_list[right_num_0]['list'][right_num_1[0]]['classification'] + " : "
    for i in range(0,len(temp_right)):
        right_answer_list +=[[right_num_0,right_num_1[0],temp_right[i]]]
        comment += " $$이미지$$"+ClassificationImgPath(str(right_num_0).zfill(2),str(right_num_1[0]).zfill(2),temp_right[i])+".png"+"$$/이미지$$"  

    comment +=  "\n"
    comment += classify_img_list[right_num_0]['list'][right_num_1[1]]['classification'] + " : "
    if classify_img_list[right_num_0]['list'][right_num_1[1]]['cnt'] >2:
        temp_right = random.sample(range(0, classify_img_list[right_num_0]['list'][right_num_1[1]]['cnt'] ) , 3)    
    else: 
        temp_right = random.sample(range(0, classify_img_list[right_num_0]['list'][right_num_1[1]]['cnt'] ) , 2)
    for i in range(0,len(temp_right)):
        right_answer_list +=[[right_num_0,right_num_1[1],temp_right[i]]]
        comment += " $$이미지$$"+ClassificationImgPath(str(right_num_0).zfill(2),str(right_num_1[1]).zfill(2),temp_right[i])+".png"+"$$/이미지$$"
    random.shuffle(right_answer_list)
    answer_NUM = np.random.randint(0, 5)
    answer = "(정답)\n (생략) \n "
    
    
    
    for i in range(0,len(right_answer_list)):
        temp_num_0 = right_answer_list[i][0]
        temp_num_1 = right_answer_list[i][1]
        temp_num_2 = right_answer_list[i][2]
        stem += "  $$이미지$$"+ClassificationImgPath(str(temp_num_0).zfill(2),str(temp_num_1).zfill(2),temp_num_2)+".png"+"$$/이미지$$"
        if i == 3:
            stem += "\n"


    answer = answer[:-1]
    return stem,answer, comment


def classification215_Stem_005():
    img_num_list = [0,1,2,3,4,5,6,7]
    right_num_0 = np.random.randint(0, len(img_num_list))    
    right_num_1 = random.sample(range(0, classify_img_list[right_num_0]['cnt']) , 2)     
    right_word_0 = classify_img_list[right_num_0]['list'][right_num_1[0]]['classification'] 
    right_word_1 = classify_img_list[right_num_0]['list'][right_num_1[1]]['classification']
    stem = "분류 기준에 따라 분류 하세요."
    stem += "$$테이블s$$ $$/테이블s$$"
    stem += "$$테이블trs$$ $$/테이블trs$$"
    stem += "$$테이블td$$"+right_word_0+"$$/테이블td$$"
    stem += "$$테이블td$$"+right_word_1+"$$/테이블td$$"
    stem += "$$테이블tre$$ $$/테이블tre$$"
    stem += "$$테이블trs$$ $$/테이블trs$$"
    stem += "$$테이블td$$ $$/테이블td$$"
    stem += "$$테이블td$$ $$/테이블td$$"
    stem += "$$테이블tre$$ $$/테이블tre$$"
    stem += "$$테이블e$$ $$/테이블e$$ \n"
    comment = "(해설)\n"
    
    right_answer_list =[]
    if classify_img_list[right_num_0]['list'][right_num_1[0]]['cnt'] >2:
        temp_right = random.sample(range(0, classify_img_list[right_num_0]['list'][right_num_1[0]]['cnt'] ) , 3)    
    else:        
        temp_right = random.sample(range(0, classify_img_list[right_num_0]['list'][right_num_1[0]]['cnt'] ) , 2)    
    comment += classify_img_list[right_num_0]['list'][right_num_1[0]]['classification'] + " : "
    for i in range(0,len(temp_right)):
        right_answer_list +=[[right_num_0,right_num_1[0],temp_right[i]]]
        comment += " $$이미지$$"+ClassificationImgPath(str(right_num_0).zfill(2),str(right_num_1[0]).zfill(2),temp_right[i])+".png"+"$$/이미지$$"  

    comment +=  "\n"
    comment += classify_img_list[right_num_0]['list'][right_num_1[1]]['classification'] + " : "
    if classify_img_list[right_num_0]['list'][right_num_1[1]]['cnt'] >2:
        temp_right = random.sample(range(0, classify_img_list[right_num_0]['list'][right_num_1[1]]['cnt'] ) , 3)    
    else: 
        temp_right = random.sample(range(0, classify_img_list[right_num_0]['list'][right_num_1[1]]['cnt'] ) , 2)
    for i in range(0,len(temp_right)):
        right_answer_list +=[[right_num_0,right_num_1[1],temp_right[i]]]
        comment += " $$이미지$$"+ClassificationImgPath(str(right_num_0).zfill(2),str(right_num_1[1]).zfill(2),temp_right[i])+".png"+"$$/이미지$$"
    random.shuffle(right_answer_list)
    answer_NUM = np.random.randint(0, 5)
    answer = "(정답)\n"
    
    
    temps = [[],[]]
    
    
    for i in range(0,len(right_answer_list)):
        temp_num_0 = right_answer_list[i][0]
        temp_num_1 = right_answer_list[i][1]
        temp_num_2 = right_answer_list[i][2]
        stem += answer_dict_0[i]+" :  $$이미지$$"+ClassificationImgPath(str(temp_num_0).zfill(2),str(temp_num_1).zfill(2),temp_num_2)+".png"+"$$/이미지$$"
        if i == 3:
            stem += "\n"
        if right_num_1[0]== right_answer_list[i][1]:
            temps[0] += [answer_dict_0[i]]
        else: 
            temps[1] += [answer_dict_0[i]]
    
    
    temps_right_word =[right_word_0,right_word_1]
    for i in range(0,len(temps)):
        answer +=   temps_right_word[i]+ " : "
        for j in range(0,len(temps[i])):
            answer +=   temps[i][j]+ " " 
        
        answer += "\n"
    answer = answer[:-1]
    return stem,answer, comment



def classification215_Stem_006():
    img_num_list = [0,1,2,3,4,5,6,7]
    right_num_0 = np.random.randint(0, len(img_num_list))    
    right_num_1 = random.sample(range(0, classify_img_list[right_num_0]['cnt']) , 2)     
    right_word_0 = classify_img_list[right_num_0]['list'][right_num_1[0]]['classification'] 
    right_word_1 = classify_img_list[right_num_0]['list'][right_num_1[1]]['classification']
    stem = "다음 기준에 따라 분류하고 그 수를 세어 봅시다. ㄱ과 ㄴ에 들어갈 숫자를 순서대로 쓰세요. "
            
    stem += "$$테이블s$$ $$/테이블s$$"
    stem += "$$테이블trs$$ $$/테이블trs$$"
    stem += "$$테이블td$$"+right_word_0+"$$/테이블td$$"
    stem += "$$테이블td$$"+right_word_1+"$$/테이블td$$"
    stem += "$$테이블tre$$ $$/테이블tre$$"
    stem += "$$테이블trs$$ $$/테이블trs$$"
    stem += "$$테이블td$$ ㄱ $$/테이블td$$"
    stem += "$$테이블td$$ ㄴ $$/테이블td$$"
    stem += "$$테이블tre$$ $$/테이블tre$$"
    stem += "$$테이블e$$ $$/테이블e$$ \n"
    comment = "(해설)\n"  
    
    x1 = np.random.randint(5, 20)
    x2 = np.random.randint(5, 10)
    while x1 + x2 >20:
        x1 = np.random.randint(5, 20)
        x2 = np.random.randint(5, 20)



    right_answer_list =[]
    temp_right = random.sample(range(0, classify_img_list[right_num_0]['list'][right_num_1[0]]['cnt'] ) , 1)    
    comment += classify_img_list[right_num_0]['list'][right_num_1[0]]['classification'] + " : "
    for i in range(0,len(temp_right)):
        for j in range(0,x1):
            right_answer_list +=[[right_num_0,right_num_1[0],temp_right[i]]]
        comment += " $$이미지$$"+ClassificationImgPath(str(right_num_0).zfill(2),str(right_num_1[0]).zfill(2),temp_right[i])+".png"+"$$/이미지$$"  

    comment +=  "\n"
    comment += classify_img_list[right_num_0]['list'][right_num_1[1]]['classification'] + " : "
    temp_right = random.sample(range(0, classify_img_list[right_num_0]['list'][right_num_1[1]]['cnt'] ) , 1)    
    for i in range(0,len(temp_right)):
        for j in range(0,x2):
            right_answer_list +=[[right_num_0,right_num_1[1],temp_right[i]]]
        comment += " $$이미지$$"+ClassificationImgPath(str(right_num_0).zfill(2),str(right_num_1[1]).zfill(2),temp_right[i])+".png"+"$$/이미지$$"
    answer = "(정답)\n $$수식$$"+str(x1)  +","+str(x2)+" $$/수식$$  \n "
    random.shuffle(right_answer_list)
    answer = answer[:-1]
    
    for i in range(0,len(right_answer_list)):
        temp_num_0 = right_answer_list[i][0]
        temp_num_1 = right_answer_list[i][1]
        temp_num_2 = right_answer_list[i][2]
        stem += "  $$이미지$$"+ClassificationImgPath(str(temp_num_0).zfill(2),str(temp_num_1).zfill(2),temp_num_2)+".png"+"$$/이미지$$"
        if i%5==4:
            stem += "\n"
    
    return stem,answer, comment


def classification215_Stem_007():
    img_num_list = [0,1,2,3,4,5,6,7]
    right_num_0 = np.random.randint(0, len(img_num_list))    
    right_num_1 = random.sample(range(0, classify_img_list[right_num_0]['cnt']) , 2)     
    right_word_0 = classify_img_list[right_num_0]['list'][right_num_1[0]]['classification'] 
    right_word_1 = classify_img_list[right_num_0]['list'][right_num_1[1]]['classification']
    stem = "다음 기준에 따라 분류하고 그 수를 세어 봅시다. ㄱ과 ㄴ에 들어갈 숫자를 순서대로 쓰세요. "
            
    stem += "$$테이블s$$ $$/테이블s$$"
    stem += "$$테이블trs$$ $$/테이블trs$$"
    stem += "$$테이블td$$"+right_word_0+"$$/테이블td$$"
    stem += "$$테이블td$$"+right_word_1+"$$/테이블td$$"
    stem += "$$테이블tre$$ $$/테이블tre$$"
    stem += "$$테이블trs$$ $$/테이블trs$$"
    stem += "$$테이블td$$ ㄱ $$/테이블td$$"
    stem += "$$테이블td$$ ㄴ $$/테이블td$$"
    stem += "$$테이블tre$$ $$/테이블tre$$"
    stem += "$$테이블e$$ $$/테이블e$$ \n"
    comment = "(해설)\n"  
    
    x1 = np.random.randint(5, 20)
    x2 = np.random.randint(5, 10)
    while x1 + x2 >20:
        x1 = np.random.randint(5, 20)
        x2 = np.random.randint(5, 20)


    right_answer_list =[]
    check = []
    
    comment += classify_img_list[right_num_0]['list'][right_num_1[0]]['classification'] + " : "
    for j in range(0,x1):
        temp_check = np.random.randint(0,classify_img_list[right_num_0]['list'][right_num_1[0]]['cnt'])
        right_answer_list +=[[right_num_0,right_num_1[0],temp_check]]
        check += [temp_check]
    
    result = list(set(check))
    for i in range(0,len(result)):
        comment += " $$이미지$$"+ClassificationImgPath(str(right_num_0).zfill(2),str(right_num_1[0]).zfill(2),result[i])+".png"+"$$/이미지$$"  

    comment +=  "\n"
    comment += classify_img_list[right_num_0]['list'][right_num_1[1]]['classification'] + " : "
    check = []
    for j in range(0,x2):
        temp_check = np.random.randint(0,classify_img_list[right_num_0]['list'][right_num_1[1]]['cnt'])
        right_answer_list +=[[right_num_0,right_num_1[1],temp_check]]
        check += [temp_check]
    result = list(set(check))
    for i in range(0,len(result)):
        comment += " $$이미지$$"+ClassificationImgPath(str(right_num_0).zfill(2),str(right_num_1[1]).zfill(2),result[i])+".png"+"$$/이미지$$"  
    
    
    answer = "(정답)\n $$수식$$"+str(x1)  +","+str(x2)+" $$/수식$$  \n "
    random.shuffle(right_answer_list)
    answer = answer[:-1]
    for i in range(0,len(right_answer_list)):
        temp_num_0 = right_answer_list[i][0]
        temp_num_1 = right_answer_list[i][1]
        temp_num_2 = right_answer_list[i][2]
        stem += "  $$이미지$$"+ClassificationImgPath(str(temp_num_0).zfill(2),str(temp_num_1).zfill(2),temp_num_2)+".png"+"$$/이미지$$"
        if i%5==4:
            stem += "\n"

    return stem,answer, comment



def classification215_Stem_008():
    img_num_list = [0,1,2,3,4,5,6,7]
    right_num_0 = np.random.randint(0, len(img_num_list))    
    right_num_1 = random.sample(range(0, classify_img_list[right_num_0]['cnt']) , 2)     
    right_word_0 = classify_img_list[right_num_0]['list'][right_num_1[0]]['classification'] 
    right_word_1 = classify_img_list[right_num_0]['list'][right_num_1[1]]['classification']

    
    stem = "분류하여 센 결과를 보고 가장 많은 것을 선택하세요."    
    
    comment = "(해설)\n"  
    
    x1 = np.random.randint(5, 20)
    x2 = np.random.randint(5, 10)
    while x1 + x2 >20 or x1==x2 :
        x1 = np.random.randint(5, 20)
        x2 = np.random.randint(5, 20)


    right_answer_list =[]
    check = []
    
    comment += classify_img_list[right_num_0]['list'][right_num_1[0]]['classification'] + " : "
    for j in range(0,x1):
        temp_check = np.random.randint(0,classify_img_list[right_num_0]['list'][right_num_1[0]]['cnt'])
        right_answer_list +=[[right_num_0,right_num_1[0],temp_check]]
        check += [temp_check]
    
    result = list(set(check))
    for i in range(0,len(result)):
        comment += " $$이미지$$"+ClassificationImgPath(str(right_num_0).zfill(2),str(right_num_1[0]).zfill(2),result[i])+".png"+"$$/이미지$$"  

    comment +=  "\n"
    comment += classify_img_list[right_num_0]['list'][right_num_1[1]]['classification'] + " : "
    check = []
    for j in range(0,x2):
        temp_check = np.random.randint(0,classify_img_list[right_num_0]['list'][right_num_1[1]]['cnt'])
        right_answer_list +=[[right_num_0,right_num_1[1],temp_check]]
        check += [temp_check]
    result = list(set(check))
    for i in range(0,len(result)):
        comment += " $$이미지$$"+ClassificationImgPath(str(right_num_0).zfill(2),str(right_num_1[1]).zfill(2),result[i])+".png"+"$$/이미지$$"  
    
    if x1 > x2 :
        answer = "(정답)\n"+ answer_dict_0[0]+"  \n "
    else: 
        answer = "(정답)\n"+ answer_dict_0[1]+"  \n "
    random.shuffle(right_answer_list)
    answer = answer[:-1]

    stem += "$$테이블s$$ $$/테이블s$$"
    stem += "$$테이블trs$$ $$/테이블trs$$"
    stem += "$$테이블td$$"+right_word_0+"$$/테이블td$$"
    stem += "$$테이블td$$"+right_word_1+"$$/테이블td$$"
    stem += "$$테이블tre$$ $$/테이블tre$$"
    stem += "$$테이블trs$$ $$/테이블trs$$"
    stem += "$$테이블td$$ ㄱ $$/테이블td$$"
    stem += "$$테이블td$$ ㄴ $$/테이블td$$"
    stem += "$$테이블tre$$ $$/테이블tre$$"
    stem += "$$테이블trs$$ $$/테이블trs$$"
    stem += "$$테이블tdcol2$$"
    for i in range(0,len(right_answer_list)):
        temp_num_0 = right_answer_list[i][0]
        temp_num_1 = right_answer_list[i][1]
        temp_num_2 = right_answer_list[i][2]
        stem += "$$이미지$$"+ClassificationImgPath(str(temp_num_0).zfill(2),str(temp_num_1).zfill(2),temp_num_2)+".png"+"$$/이미지$$"
        if i%5==4:
            stem += "\n"
    stem += "$$/테이블tdcol2$$"
    stem += "$$테이블tre$$ $$/테이블tre$$"
    stem += "$$테이블e$$ $$/테이블e$$ \n"    
    stem += "\n"+answer_dict_0[0] +" "+ right_word_0
    stem += "\n"+answer_dict_0[1] +" "+ right_word_1 
    

    return stem,answer, comment



def classification215_Stem_009():
    right_num_0 = random.sample(range(1, 5) , 3)     
    right_num_1 = random.sample(range(1, 5) , 3)     
    want_list =[]
    
    comment = "(해설)\n 주어진 숫자들을 2로 나누어서 나머지를 확인하면 짝수와 홀수를 분류할 수 있다."  
    odd_comment = "("
    even_comment = "("
    for i in range(0,len(right_num_0)):
        want_list +=[2*right_num_0[i],2*right_num_1[i]+1]
        even_comment  += str(2*right_num_0[i])+","
        odd_comment += str(2*right_num_1[i]+1)+","
    odd_comment = odd_comment[:-1]
    even_comment = even_comment[:-1]
    odd_comment += ")"
    even_comment+= ")"
    
    comment +=even_comment+"는 짝수이고, "+odd_comment+"는 홀수 입니다. "
    stem = "주어진 숫자들을 짝수와 홀수로 분류해보세요.\n"
    random.shuffle(want_list)
    for i in range(0,len(want_list)):
        stem += str(want_list[i])+","
    stem = stem[:-1]    
    answer = "(정답)\n "
    answer += "짝수"+even_comment+","+"홀수"+odd_comment   +"\n" 
    

    return stem,answer, comment
