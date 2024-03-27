import numpy as np
import math
import random

answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤"
}

def ImgPath(pathcheck,shape,ranNum): ## 응용 or 기본 / 모양 / 번호 
    if pathcheck==0:
        temps = "Element/Grade1_1/Normal"
    else:
        temps = "Element/Grade1_1/Applications"
    tempimg_list = ["/shape/","/box/","/cynlinder/"]
    want = tempimg_list[shape]
    want = temps+want+str(ranNum).zfill(2)
    return want

def geometry_ft_0(right_cnt,view_cnt,right_shape): #right_cnt : 정답 갯수, view_cnt : 보기 갯수, right_shape : 정답 모양 
    if right_cnt > view_cnt: 
        print("정답 갯수보다 보기 갯수를 더 많이 입력하셔야 합니다.")
    else: 
        
        _choose_img_list = [] 
        right_img = [] 
        temp_choose = random.sample(range(1, 5), right_cnt)        
        comments_list = [[],[],[]]
        for i in range(0,right_cnt):
            _choose_img_list += [[right_shape,str(temp_choose[i]).zfill(2)] ]
            right_img += [[right_shape,str(temp_choose[i]).zfill(2)] ]
            comments_list[right_shape] += [str(temp_choose[i]).zfill(2)]  
        
        temp_choose = random.sample(range(1, 20), view_cnt - right_cnt)
        shape_list = [0,1,2]
        shape_list.remove(right_shape)
        for i in range(0,view_cnt - right_cnt):           
            int_shape = shape_list[random.sample(range(0, 2), 1)[0]]
            _choose_img_list += [[int_shape,str(temp_choose[i]).zfill(2)] ]
            comments_list[int_shape] += [str(temp_choose[i]).zfill(2)] 
        random.shuffle(_choose_img_list)            
        want_right = []
        for i in range(0,len(_choose_img_list)):
            for j in range(0,len(right_img)):
                if _choose_img_list[i] == right_img[j]:
                    want_right += [answer_dict[i]]
        return right_img,_choose_img_list,want_right,comments_list    ## 정답 이미지 , 이미지 리스트, 정답, 해설

def geometry_ft_1(right_cnt,view_cnt,right_shape): #right_cnt : 정답 갯수, view_cnt : 보기 갯수, right_shape : 정답 모양 
    if right_cnt > view_cnt: 
        print("정답 갯수보다 보기 갯수를 더 많이 입력하셔야 합니다.")
    else: 
        
        _choose_img_list = [] 
        right_img = [] 
        temp_choose = random.sample(range(1, 5), right_cnt)        
        comments_list = [[],[],[]]
        for i in range(0,right_cnt):
            _choose_img_list += [[right_shape,str(temp_choose[i]).zfill(2)] ]
            right_img += [[right_shape,str(temp_choose[i]).zfill(2)] ]
            comments_list[right_shape] += [str(temp_choose[i]).zfill(2)]  
        
        temp_choose = random.sample(range(1, 20), view_cnt - right_cnt)
        shape_list = [0,1,2]
        shape_list.remove(right_shape)
        for i in range(0,view_cnt - right_cnt):           
            int_shape = shape_list[random.sample(range(0, 2), 1)[0]]
            _choose_img_list += [[int_shape,str(temp_choose[i]).zfill(2)] ]
            comments_list[int_shape] += [str(temp_choose[i]).zfill(2)] 
        random.shuffle(_choose_img_list)            
        want_right = []
        for i in range(0,len(_choose_img_list)):
            check=0
            for j in range(0,len(right_img)):
                if _choose_img_list[i] == right_img[j]:
                    check+=1
            if check ==0:
                want_right += [answer_dict[i]]                    
        return right_img,_choose_img_list,want_right,comments_list    ## 정답 이미지 , 이미지 리스트, 정답, 해설

def make_comment(comments_list): ## 해설 만들기
    shape_list = ["원모양","박스모양","원기둥모양"]
    comments ="(해설)\n"
    
    for i in range(0,3) :
        if len(comments_list[i])>0: 
            comments += shape_list[i]+ " : "
            for j in range(0,len(comments_list[i])) : 
                comments += "$$이미지$$"+ImgPath(1,i ,comments_list[i][j])+".png" +"$$/이미지$$   "
            comments +=  "\n"
    return  comments   

def geometry_ft_2(right_cnt,view_cnt,right_shape): #right_cnt : 정답 갯수, view_cnt : 보기 갯수, right_shape : 정답 모양 
    if right_cnt > view_cnt: 
        print("정답 갯수보다 보기 갯수를 더 많이 입력하셔야 합니다.")
    else: 
        
        _choose_img_list = [] 
        right_img = [] 
        temp_choose = random.sample(range(1, 20), right_cnt)        
        comments_list = [[],[],[]]
        for i in range(0,right_cnt):
            _choose_img_list += [[right_shape,str(temp_choose[i]).zfill(2)] ]
            right_img += [[right_shape,str(temp_choose[i]).zfill(2)] ]
            comments_list[right_shape] += [str(temp_choose[i]).zfill(2)]  
        
        temp_choose = random.sample(range(1, 20), view_cnt - right_cnt)
        shape_list = [0,1,2]
        shape_list.remove(right_shape)
        for i in range(0,view_cnt - right_cnt):           
            int_shape = shape_list[random.sample(range(0, 2), 1)[0]]
            _choose_img_list += [[int_shape,str(temp_choose[i]).zfill(2)] ]
            comments_list[int_shape] += [str(temp_choose[i]).zfill(2)] 
        random.shuffle(_choose_img_list)            
        want_right = []
        for i in range(0,len(_choose_img_list)):
            check=0
            for j in range(0,len(right_img)):
                if _choose_img_list[i] == right_img[j]:
                    check+=1
            if check ==0:
                want_right += [answer_dict[i]]                    
        return right_img,_choose_img_list,want_right,comments_list    ## 정답 이미지 , 이미지 리스트, 정답, 해설
 
def geometry112_stem_001():
    right_shape = np.random.randint(0, 2)
    comment = "(해설) 생략"
    stem = "보기의 모양과 같은 모양을 찾아 선택하세요.\n "    
    stem +="$$표$$"        
    stem += "$$이미지$$"+ImgPath(1,right_shape ,np.random.randint(1, 20) )+".png" +"$$/이미지$$   "
    stem +="$$/표$$"                
    stem +="\n   "
    choose_img_list =[]        
    for i in range(0,3): 
        choose_img_list +=[[i ,str(np.random.randint(1, 5)).zfill(2)]]    
    random.shuffle(choose_img_list)            
    for i in range(0,len(choose_img_list)):
        if choose_img_list[i][0] == right_shape:
            wants = answer_dict[i]
            break 
    answer = "(정답)\n "+str(wants)+"\n"
    for i in range(0,len(choose_img_list)) :
        stem += "\n"+answer_dict[i] +" $$이미지$$"+ImgPath(0, choose_img_list[i][0], choose_img_list[i][1])+".png"+"$$/이미지$$"      
    return stem,answer, comment

def geometry112_stem_002():
    right_cnt =1
    view_cnt = 5
    right_shape = np.random.randint(0, 2)    
    answer = "(정답)\n "     
    if right_cnt > 1:
        stem = "알맞은 모양을 모두 찾아 선택하세요.\n "
    else: 
        stem = "보기의 모양과 같은 모양을 찾아 선택하세요.\n "
    stem +="$$표$$"        
    want = geometry_ft_0(right_cnt,view_cnt,right_shape)
    comment = make_comment(want[3])
    for i in range(0,len(want[0])) :
        stem += "$$이미지$$"+ImgPath(0, want[0][i][0], want[0][i][1])+".png" +"$$/이미지$$   "
    stem +="$$/표$$"                
    stem +="\n   "
    for i in range(0,len(want[1])) :
        stem += "\n"+answer_dict[i] +" $$이미지$$"+ImgPath(1, want[1][i][0], want[1][i][1])+".png"+"$$/이미지$$"        
    for i in range(0,len(want[2])) :        
        answer += want[2][i]+","
    answer = answer[:-1]+"\n"
    return stem,answer, comment

def geometry112_stem_003():
    right_cnt =2
    view_cnt = 5
    right_shape = np.random.randint(0, 2)   
    answer = "(정답)\n "     
    if right_cnt > 1:
        stem = "보기의 모양과 같은 모양을 모두 찾아 선택하세요.\n "
    else: 
        stem = "알맞은 모양을 찾아 선택하세요.\n "
    stem +="$$표$$"        
    want = geometry_ft_0(right_cnt,view_cnt,right_shape)
    comment = make_comment(want[3])
    stem += "$$이미지$$"+ImgPath(0, want[0][0][0], want[0][0][1])+".png" +"$$/이미지$$   "
    stem +="$$/표$$"                
    stem +="\n   "
    for i in range(0,len(want[1])) :
        stem += "\n"+answer_dict[i] +" $$이미지$$"+ImgPath(1, want[1][i][0], want[1][i][1])+".png"+"$$/이미지$$"        
    for i in range(0,len(want[2])) :        
        answer += want[2][i]+","
    answer = answer[:-1]+"\n"
    return stem,answer, comment

def geometry112_stem_004():
    right_cnt =4
    view_cnt = 5
    right_shape = np.random.randint(0, 2)   
    answer = "(정답)\n "     
    stem = "모양이 다른 한 가지를 찾아 선택하세요. \n "
    
    
    want = geometry_ft_1(right_cnt,view_cnt,right_shape)
    comment = make_comment(want[3])
    
    for i in range(0,len(want[1])) :
        stem += "\n"+answer_dict[i] +" $$이미지$$"+ImgPath(1, want[1][i][0], want[1][i][1])+".png"+"$$/이미지$$"        
    for i in range(0,len(want[2])) :        
        answer += want[2][i]+","
    answer = answer[:-1]+"\n"
    return stem,answer, comment

def geometry112_stem_005():
    right_cnt =3
    view_cnt = 5
    right_shape = np.random.randint(0, 2)   
    answer = "(정답)\n "     
    stem = "보기의 모양과 다른 모양을 모두 찾아 선택하세요.  \n "
    
    
    want = geometry_ft_1(right_cnt,view_cnt,right_shape)
    comment = make_comment(want[3])
    stem +="$$표$$"        
    stem += "$$이미지$$"+ImgPath(0, want[0][0][0], want[0][0][1])+".png" +"$$/이미지$$   "
    stem +="$$/표$$"  
    
    
    
    for i in range(0,len(want[1])) :
        stem += "\n"+answer_dict[i] +" $$이미지$$"+ImgPath(1, want[1][i][0], want[1][i][1])+".png"+"$$/이미지$$"        
    for i in range(0,len(want[2])) :        
        answer += want[2][i]+","
    answer = answer[:-1]+"\n"
    return stem,answer, comment

def geometry112_stem_006():
    wants = np.random.randint(1, 5)   
    
    answer = "(정답)\n "+str(answer_dict[wants-1])+"\n"
    stem = "다음 중 같은 모양끼리 모은 것이 아닌 것을 선택하세요.\n "
    
    comment_list = [[],[],[]]

    for i in range(1,6) :
        right_shape =np.random.randint(0,2)   
        if i==wants:
            right_cnt =2
            view_cnt = 3
        else:
            right_cnt =3
            view_cnt = 3
        want = geometry_ft_2(right_cnt,view_cnt,right_shape)    
        stem += "\n"+answer_dict[i-1]
        for j in range(0,3):
            if want[3][j] not in comment_list[j]:
                comment_list[j] += want[3][j]



        for i in range(0,len(want[1])) :
             stem +=" $$이미지$$"+ImgPath(1, want[1][i][0], want[1][i][1])+".png"+"$$/이미지$$"        
        comment=make_comment(comment_list)
    return stem,answer, comment

def_3d =[
        [
            ["둥근 부분이 있고, 평평한 부분은 없어요.","둥근 부분이 있고, 평평한 부분 없는 모양은 구 모양입니다.","둥근 부분이 있고, 평평한 부분은 없는 모양을 선택하세요.","둥근 부분이 있고, 평평한 부분은 없는 모양을 모두 선택하세요."],
            ["어느 방향으로 굴려도 잘 굴러갑니다. ","어느 방향으로 굴려도 잘 굴러가는 모양은 구 모양입니다. ","어느 방향으로 굴려도 잘 굴러가는 모양을 선택하세요.","어느 방향으로 굴려도 잘 굴러가는 모양을 모두 선택하세요."],
            ["잘 쌓을 수 없지만, 잘 굴릴 수 있습니다. ","잘 쌓을 수 없지만, 잘 굴릴 수 있는 모양은 구 모양입니다.","잘 쌓을 수 없지만, 잘 굴릴 수 있는 모양을 선택하세요.","잘 쌓을 수 없지만, 잘 굴릴 수 있는 모양을 모두 선택하세요."]
        ],
        [
            ["뾰족한 부분과 평평한 부분이 있습니다. ","뾰족한 부분과 평평한 부분이 있는 모양은 상자 모양입니다.","뾰족한 부분과 평평한 부분이 있는 모양을 선택하세요.","뾰족한 부분과 평평한 부분이 있는 모양을 모두 찾아 선택하세요."],
            ["굴러가지 않아요. ","굴러가지 않는 모양은 상자 모양입니다.","굴러가지 않는 모양을 선택하세요.","굴러가지 않는 모양을 모두 선택하세요."],
            ["잘 쌓을 수 있지만, 잘 굴릴 수 없습니다. ","잘 쌓을 수 있지만, 잘 굴릴 수 없는 모양은 상자 모양입니다.","잘 쌓을 수 있지만, 잘 굴릴 수 없는 모양을 선택하세요.","잘 쌓을 수 있지만, 잘 굴릴 수 없는 모양을 모두 선택하세요."]
        ],
        [
            ["둥근 부분과 평평한 부분이 있습니다. ","둥근 부분과 평평한 부분이 있는 모양은 원기둥 모양입니다.","둥근 부분과 평평한 부분이 있는 모양을 선택하세요.","둥근 부분과 평평한 부분이 있는 모양을 모두 선택하세요."],
            ["눕히면 잘 굴러갑니다. ","눕히면 잘 굴러 가는 모양은 원기둥 모양입니다.","눕히면 잘 굴러 가는 모양을 선택하세요.","눕히면 잘 굴러 가는 모양을 모두 선택하세요."],
            ["세우면 잘 쌓을 수 있고, 눕히면 잘 굴러갑니다. ","세우면 잘 쌓을 수 있고, 눕히면 잘 굴러가는 모양은 원기둥 모양입니다.","세우면 잘 쌓을 수 있고, 눕히면 잘 굴러 가는 모양을 선택하세요.","세우면 잘 쌓을 수 있고, 눕히면 잘 굴러 가는 모양을 모두 선택하세요."]
        ]
        ]

def geometry112_stem_007():
    right_shape = np.random.randint(0, 2)
    sub_shape = np.random.randint(0, 2)
    
    nameList = ["수진","종식","지훈","준혁","현주","선영"]
    nameList1 = ["이가","이가","이가","이가","가","이가"]
    namewant = np.random.randint(0, len(nameList))
    choose_name =  nameList[namewant] + nameList1[namewant]
    stem = choose_name + " 설명하는 모양으로 알맞은 것을 선택하세요.\n "    
    stem +="$$표$$"        
    stem += nameList[namewant] + " : " + def_3d[right_shape][sub_shape][0]
    stem +="$$/표$$"                
    stem +="\n   "
    comment = "(해설)\n " + def_3d[right_shape][sub_shape][1]

    choose_img_list =[]        
    for i in range(0,3): 
        choose_img_list +=[[i ,str(np.random.randint(1, 5)).zfill(2)]]    
    random.shuffle(choose_img_list)            
    for i in range(0,len(choose_img_list)):
        if choose_img_list[i][0] == right_shape:
            wants = answer_dict[i]
            break 
    answer = "(정답)\n "+str(wants)+"\n"
    for i in range(0,len(choose_img_list)) :
        stem += "\n"+answer_dict[i] +" $$이미지$$"+ImgPath(0, choose_img_list[i][0], choose_img_list[i][1])+".png"+"$$/이미지$$"      
    return stem,answer, comment

def geometry112_stem_008():
    right_shape = np.random.randint(0, 2)
    sub_shape = np.random.randint(0, 2)
    right_cnt =1
    view_cnt = 5    
    answer = "(정답)\n "   
    stem = def_3d[right_shape][sub_shape][2] + "\n "
    comment = "(해설)\n " + def_3d[right_shape][sub_shape][1]
    want = geometry_ft_0(right_cnt,view_cnt,right_shape)    
               
    stem +="\n   "
    for i in range(0,len(want[1])) :
        stem += "\n"+answer_dict[i] +" $$이미지$$"+ImgPath(1, want[1][i][0], want[1][i][1])+".png"+"$$/이미지$$"        
    for i in range(0,len(want[2])) :        
        answer += want[2][i]+","
    answer = answer[:-1]+"\n"
    return stem,answer, comment

def geometry112_stem_009():
    right_shape = np.random.randint(0, 2)
    sub_shape = np.random.randint(0, 2)
    right_cnt =2
    view_cnt = 5    
    answer = "(정답)\n "   
    stem = def_3d[right_shape][sub_shape][3] + "\n "
    comment = "(해설)\n " + def_3d[right_shape][sub_shape][1]
    want = geometry_ft_0(right_cnt,view_cnt,right_shape)    
    stem +="\n   "
    for i in range(0,len(want[1])) :
        stem += "\n"+answer_dict[i] +" $$이미지$$"+ImgPath(1, want[1][i][0], want[1][i][1])+".png"+"$$/이미지$$"        
    for i in range(0,len(want[2])) :        
        answer += want[2][i]+","
    answer = answer[:-1]+"\n"
    return stem,answer, comment



object_3d_img_list = [    #입체도형 이미지 리스트
                        {'filename': '01', 's_cnt': '1','b_cnt':'3','c_cnt':'1' },
                        {'filename': '02', 's_cnt': '1','b_cnt':'6','c_cnt':'2' },
                        {'filename': '03', 's_cnt': '5','b_cnt':'2','c_cnt':'0' },
                        {'filename': '04', 's_cnt': '1','b_cnt':'1','c_cnt':'2' },
                        {'filename': '05', 's_cnt': '0','b_cnt':'0','c_cnt':'6' },
                        {'filename': '06', 's_cnt': '3','b_cnt':'2','c_cnt':'1' },
                        {'filename': '07', 's_cnt': '4','b_cnt':'0','c_cnt':'2' },
                        {'filename': '08', 's_cnt': '1','b_cnt':'2','c_cnt':'4' },
                        {'filename': '09', 's_cnt': '0','b_cnt':'4','c_cnt':'1' },
                        {'filename': '10', 's_cnt': '2','b_cnt':'2','c_cnt':'3' },
                        {'filename': '11', 's_cnt': '1','b_cnt':'1','c_cnt':'1' },
                        {'filename': '12', 's_cnt': '2','b_cnt':'5','c_cnt':'0' },
                        {'filename': '13', 's_cnt': '1','b_cnt':'2','c_cnt':'3' },
                        {'filename': '14', 's_cnt': '0','b_cnt':'2','c_cnt':'2' },
                        {'filename': '15', 's_cnt': '0','b_cnt':'5','c_cnt':'3' },
                        {'filename': '16', 's_cnt': '4','b_cnt':'2','c_cnt':'0' },
                        {'filename': '17', 's_cnt': '3','b_cnt':'1','c_cnt':'2' },
                        {'filename': '18', 's_cnt': '5','b_cnt':'2','c_cnt':'7' },
                        {'filename': '19', 's_cnt': '0','b_cnt':'1','c_cnt':'5' }
                    ]

def geometry112_stem_010():
    right_num = np.random.randint(0, len(object_3d_img_list))
    
    stem = "그림을 보고 모양을 각각 몇 개 사용했는지 ㄱ, ㄴ, ㄷ에 들어갈 수를 순서대로 쓰세요.\n "        
    comment = "(해설) 생략"    
    stem +="$$표$$"            
    stem +="$$이미지2$$Element/Grade1_1/ThreeDimension/"+object_3d_img_list[right_num]['filename']+".png" +"$$/이미지2$$   "
    stem +="$$/표$$"                
    stem +="\n"
    
    stem +="구 모양  : ㄱ 개\n"
    stem +="박스 모양 : ㄴ  개\n"
    stem +="원기둥 모양 : ㄷ 개\n "
    

    answer = "(정답)\n "+str(object_3d_img_list[right_num]['s_cnt'])+","+str(object_3d_img_list[right_num]['b_cnt'])+","+str(object_3d_img_list[right_num]['c_cnt'])+"\n"
    return stem,answer, comment



