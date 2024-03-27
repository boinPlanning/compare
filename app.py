#!/home/boin-service/Visang/.venv/bin/python
#-*-coding:utf-8-*-

import json
import pymysql
import requests
import random
import base64
import traceback
import logging

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
#from sshtunnel import SSHTunnelForwarder
from datetime import date

from stem_directory import FUNC_DICT
from func2html import *
from gt_generate import generate
from xml.etree.ElementTree import fromstring, Element, ElementTree
from hml2html import convert2htmlFromString
from detect_items import load_detector, detect

app = Flask(__name__)
cors = CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)
api = Api(app)

# 로그
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('access.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

error_log = logging.getLogger()
error_log.setLevel(logging.INFO)
error_handler = logging.FileHandler('error.log')
error_handler.setFormatter(formatter)
error_log.addHandler(error_handler)

w_dict, _ = load_positions("./dictionary_11pt.txt")
LIST_NONE = '<div class="cdml_question"><div class="list_box"><ul class="list_11111"><li style="text-align: left;" class="option"><span style="vertical-align: baseline;">(주관식 문항입니다.)</span></li></ul></div></div>'

#GRADE_UNIT = {
#    1: "덧셈과 뺄셈",
#    2: "평면 도형",
#    3: "나눗셈1",
#    4: "곱셈1",
#    5: "길이와 시간",
#    6: "분수와 소수",
#    7: "곱셈2",
#    8: "나눗셈2",
#    9: "원",
#    10: "분수",
#    11: "들이와 무게",
#    12: "큰 수",
#    13: "각도",
#    14: "곱셈과 나눗셈",
#    15: "규칙 찾기",
#    16: "분수의 덧셈과 뺄셈1",
#    17: "삼각형",
#    18: "소수의 덧셈과 뺄셈",
#    19: "사각형",
#    21: "다각형",
#    22: "자연수의 혼합 계산",
#    23: "약수와 배수",
#    24: "규칙과 대응",
#    25: "약분과 통분",
#    26: "분수의 덧셈과 뺄셈2",
#    27: "다각형의 둘레와 넓이",
#    28: "수의 범위와 어림하기",
#    29: "분수의 곱셈",
#    30: "합동과 대칭",
#    31: "소수의 곱셈",
#    32: "평균과 가능성",
#    33: "분수의 나눗셈1",
#    34: "소수의 나눗셈1",
#    35: "비와 비율",
#    36: "분수의 나눗셈2",
#    37: "소수의 나눗셈2",
#    38: "비례식과 비례배분",
#    39: "원의 넓이",
#    50: "9까지의 수",
#    51: "덧셈과 뺄셈",
#    52: "비교하기",
#    53: "50까지의 수",
#    54: "100까지의 수",
#    55: "덧셈과 뺄셈",
#    56: "덧셈과 뺄셈",
#    57: "시계보기와 규칙찾기",
#    58: "덧셈과 뺄셈",
#    59: "세 자리 수",
#    60: "여러 가지 도형",
#    61: "덧셈과 뺄셈",
#    62: "길이 재기",
#    63: "곱셈",
#    64: "네 자리 수",
#    65: "곱셈구구",
#    66: "길이 재기",
#    67: "시각과 시간",
#}
# webhook_url = "http://chat.boinit.com:10000/hooks/pqj6d67n9pd6mguian45f4m8de"
webhook_url = "http://talk.boinit.com:10000/hooks/aaw8jockeirmpcw1uewixnz6bw"
webhook_data = {
    "attachments": [
        {
            "fallback": "error",
            "color": "#FF0000",
            "title": "쌤핏수학 API에러 봇",
            "fields": [
                {
                    "short": False,
                    "title":"Error ID",
                },
                {
                    "short": False,
                    "title":"Error Message",
                }
            ]
        }
    ]
}

stem_dict, unit_dict = load_detector()

def hml2html(hml):
    _hml = base64.b64decode(hml).decode('utf-8')
    _type = 'latex'
    _service_id = 'kr'
    
    return convert2htmlFromString(_hml, _type, _service_id)

# 문항 생성
def getGenerate(question):
    func_name = question["ETC_CATEGORY5"]
    
    if question["QUESTION_TYPE"] == "gt":
        body_html, answer_html, explanation_html, list_html = generate(func_name)
        
        res = {
            "r": 0,
            "id": func_name,
            "body_html": body_html,
            "list_html": list_html,
            "answer_html": answer_html,
            "explanation_html": explanation_html,
            "image_list": []
        }
    else:
        func = FUNC_DICT[func_name]
        
        if question["QUESTION_TYPE"] == "py":
            hmls_material, hmls_stem_material, hmls_answer_material, svgs = func2hmls(func, 1, w_dict, polygon=True)
        else:
            hmls_material, hmls_stem_material, hmls_answer_material, svgs = func2hmls(func, 1, w_dict)
        
        res = hml2html(hmls_material[0])
            
        res["image_list"] = svgs
        res["id"] = func_name

    return res
        
# DB 연결
def getConnection():
    #SSH address mapping setup (not actually connects)
    #tunnel =  SSHTunnelForwarder(('192.168.20.3', 22),
    #                        ssh_username='boin-service',
    #                        ssh_password='qhdls!@34',
    #                        remote_bind_address=('127.0.0.1', 3306),
    #                       )
    #tunnel.start()

    # connect MySQL like local        
                      
    return pymysql.connect(
                host='10.9.184.2', #(local_host)
                user='KERISAIGDEV',
                passwd='WelCome123##',
                db= 'VISANG_DEV',
                charset='utf8',
                port=3306)#tunnel.local_bind_port)
    

# 문항 정보 검색
def getQuestionInfo(lbno, d_type):
    conn = getConnection()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    
    for i, j in enumerate(lbno):
        lbno[i] = str(j)
            
    lbno = ', '.join(lbno)
    if d_type == 'A':
        sql = "SELECT * FROM QUESTIONS WHERE LBNO IN ({lbno}) AND DIFFICULTY IN (1, 2, 3) AND EXT_FEILD14 = 'visang';".format(lbno=lbno)
    elif d_type == 'B':
        sql = "SELECT * FROM QUESTIONS WHERE LBNO IN ({lbno}) AND DIFFICULTY IN (3, 4, 5) AND EXT_FEILD14 = 'visang';".format(lbno=lbno)
    
    curs.execute(sql)
    row = list(curs.fetchall())

    conn.close()

    return row

'''
def getQuestionInfo(unit_value, chapter_code, lbno):
    conn = getConnection()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    
    for i, u in enumerate(unit_value):
        unit_value[i] = "'"+u+"'"
        
    for i, c in enumerate(chapter_code):
        chapter_code[i] = "'"+c+"'"
        
    unit_value = ', '.join(unit_value)
    chapter_code = ', '.join(chapter_code)
    
    if len(lbno) == 0:
        sql = "SELECT * FROM QUESTIONS WHERE ETC_CATEGORY2 IN ({unit_value}) AND CHAPTER_CODE IN ({chapter_code});".format(
            unit_value=unit_value, chapter_code=chapter_code)
        
        
    else:
        for i, j in enumerate(lbno):
            lbno[i] = str(j)
        lbno = ', '.join(lbno)
        
        sql = "SELECT * FROM QUESTIONS WHERE ETC_CATEGORY2 IN ({unit_value}) AND CHAPTER_CODE IN ({chapter_code}) AND LBNO IN ({lbno});".format(
                unit_value=unit_value, lbno=lbno, chapter_code=chapter_code)
    logger.info(sql)
    curs.execute(sql)
    row = list(curs.fetchall())
    logger.info(len(row))
    conn.close()

    return row
'''

# latax 수식 처리
def latexParsing(latex):
    #latex = latex.lstrip('{')
    #latex = latex.rstrip('}')

    latex = latex.replace('\\times', '×').replace('\\div', '÷')
    #latex = latex.replace('{{', '{').replace('}}', '}')
    
    if '\\' not in latex:
        latex = latex.replace('{', '').replace('}', '')
    if 'frac' in latex:
        try:
            last = int(latex[-1])
            latex = latex + '}'
        except:
            pass
            #latex = latex.replace('}$$', '} }$$')

        #latex = latex.replace('}\\', '\\')
    latex = latex.replace('km^2', '㎢').replace('cm^2', '㎠').replace('m^2', '㎡')
    return latex

# 객관식 보기 처리
def listParsing(list_html):
    list_bulk = []

    list_html = list_html.replace(
        '<li style="text-align: left;" class="option">&nbsp;</li>', '')
    list_html = list_html.replace(
        '<div class="cdml_question"><div class="list_box"><ul class="list_11111">', '')
    list_html = list_html.replace('</ul></div></div>', '')
    list_html = list_html.replace('&nbsp;', ' ').replace('\\,', '')
    list_html = list_html.replace(
        '<li style="text-align: left;" class="option">', '').replace('</li>', '')
    list_html = list_html.replace(
        '<span class="ccctex " style="">', '').replace('</span>', '')
    list_html = list_html.replace('  ', '')
    list_html = list_html.replace('①', '#').replace('②', '#').replace(
        '③', '#').replace('④', '#').replace('⑤', '#')

    list_html = list_html.split('#')
    del list_html[0]

    for l in list_html:
        logger.info(l)
        l = latexParsing(l)
        logger.info(l)
        list_bulk.append(str(l.strip()))
    
    return list_bulk

# 정답 처리
def answerParsing(answer_html, body_html):
    answer_number = ['①', '②', '③', '④', '⑤']
    answer_list = ['㉠', '㉡', '㉢', '㉣', '㉤', '㉥']
    answer_dict = {
        '㉠': 'ㄱ',
        '㉡': 'ㄴ',
        '㉢': 'ㄷ',
        '㉣': 'ㄹ',
        '㉤': 'ㅁ',
        '㉥': 'ㅂ'
    }
    answer_seq = dict()
    special_char = ['※', '☆', '★', '○', '●', '◎', '◇', '◆', '□', '■', '△', '▲', '▽', '▼', '◁', '◀', '▷', '▶', '♤', '♠', '♡', '♥', '♧', '♣', '⊙', '◈', '▣', '◐', '◑']
    number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    #logger.info(answer_html)
    if 'frac' in answer_html or '^ { { 2' in answer_html or '\\div' in answer_html or '\\times' in answer_html or '°' in answer_html or '^ { 2' in answer_html:
        serviceType = 'offline'
    else:
        serviceType = 'online'

    answer_html = answer_html.replace('<div class="cdml_question"><div class="question_box"><p style="margin: 0px 0px 0px 0px;text-align: left;vertical-align: baseline;text-indent: 0px;line-height: 160.0%;border-top: 0;border-right: 0;border-bottom: 0;border-left: 0;">', '')
    answer_html = answer_html.replace('</p></div></div>', '')
    
    answer_html = answer_html.replace('<div class="cdml_question">', '').replace('<div class="question_box">', '').replace('<p style="display: inline-block">', '')
    answer_html = answer_html.replace('</p>', '').replace('</div>', '')
    if r'\phantom{0}' in answer_html:
        answer_html = answer_html.replace('</br>', ',')
    
    answer_html = answer_html.replace('<span style="vertical-align: baseline;">', '').replace('</span>', '')
    answer_html = answer_html.replace('$$', '')
    answer_html = answer_html.replace('<span class="ccctex " style="">', '')
    
    answer_html = answer_html.replace(' ', '').replace('\\,', '')
    answer_html = answer_html.replace('&nbsp;', ' ')
    
    answer_html = answer_html.replace('\\mathrm', '').replace('\n', '')
    answer_html = answer_html.replace(r'{({2})', r',{({2})').replace(r'{({3})', r',{({3})')
    answer_html = answer_html.strip()
        
    if ',' in answer_html:
        answer_html = answer_html.split(',')
        while '' in answer_html:
            answer_html.remove('')
            
    logger.info("answer_html : {answer_html}".format(answer_html = answer_html))
    
    if type(answer_html) == list:
        answer_bulk = []
        for i in answer_html:
            i = i.strip()
            i = i.replace('㉠{', '{').replace('㉡{', '{')
            i = i.lstrip('{')
            i = i.rstrip('}')
            i = i.replace('{kg', 'kg')

            if i in answer_number:
                answer_bulk.append(answer_number.index(i)+1)
                quiz_type = 'choice-multi'
            elif i in answer_list:
                answer_bulk.append(answer_dict[i])
                quiz_type = 'answer-multi'
            else:
                i = latexParsing(i)
                if '(1)' in i or '㉠' in i:
                    quiz_type = 'answer-multi'
                elif '또는' in i:
                    i = i.split('또는')[0]
                    
                    #for ans in i:
                    #    for j, a in enumerate(ans):
                    #        if a in number_list:
                    #            i = i[j]
                elif r'\phantom{0}' in i:
                    quiz_type = 'answer-multi-seq'
                else:
                    quiz_type = 'answer-multi'
                    
                i = i.replace('(1)', '').replace('(2)', '').replace('(3)', '')
                i = i.replace('㉠', '').replace('㉡', '').replace('㉢', '').replace('㉣', '').replace('㉤', '').replace('㉥', '').replace('㉦', '').replace('㉧', '').replace('㉨', '')
                i = i.replace('①', '').replace('②', '').replace('③', '').replace('④', '').replace('⑤', '').replace('⑥', '').replace('⑦', '').replace('⑧', '').replace('⑨', '')

                answer_bulk.append(i)
        
        if 'boxed' in body_html or '차례대로' in body_html or '차례' in body_html or '순서대로' in body_html:
            quiz_type = quiz_type + '-seq'
            for i, ans in enumerate(answer_bulk):
                answer_seq[i+1] = ans
            
        for i, ans in enumerate(answer_bulk):
            if type(answer_bulk[i]) == str:
                if r'\phantom{0}' in answer_bulk[i]:
                    answer_bulk[i] = answer_bulk[i].replace(r'\phantom{0}', '')
                    answer_seq[i+1] = answer_bulk[i]
    else:
        answer_html = answer_html.lstrip('{')
        answer_html = answer_html.rstrip('}')
        answer_html = answer_html.replace('{kg', 'kg')
        answer_html = answer_html.replace('}}', '}')

        if answer_html in answer_number:
            answer_bulk = answer_number.index(answer_html)+1
            
            quiz_type = 'choice-single'
        elif answer_html in answer_list:
            answer_bulk = answer_dict[answer_html]
            
            quiz_type = 'answer-single'
        else:
            answer_bulk = latexParsing(answer_html)
            if '또는' in answer_bulk:
                temp = answer_bulk.split('또는')
                
                answer_bulk = temp[0]
                #for i, ans in enumerate(temp):
                #    for a in ans:
                #        if a in number_list:
                #            answer_bulk = temp[i]
               
            quiz_type = 'answer-single'

    # 특수 문자 거르기
    if type(answer_bulk) == list:
        for a in answer_bulk:
            if type(a) == str and a in special_char:
                serviceType = 'offline'

    return answer_bulk, answer_seq, quiz_type, serviceType

# 문항 생성 카운트
def genCount(count, questions):
    today = date.today()
    
    conn = getConnection()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    
    sql = "SELECT * FROM GEN_COUNT WHERE ID = '{today}';".format(today=today.isoformat())
    curs.execute(sql)

    row = curs.fetchall()
    if len(row) == 0:
        insert = "INSERT INTO GEN_COUNT(ID, COUNT) VALUES ({id}, {count});".format(id= "'" + today.isoformat() + "'", count=count)
        curs.execute(insert)
        conn.commit()
    else:
        count = count + int(row[0]["COUNT"])
        update = "UPDATE GEN_COUNT SET COUNT = {count} WHERE ID = {id};".format(id= "'" + today.isoformat() + "'", count=count)
        curs.execute(update)
        conn.commit()
    
    for q in questions:
        code = q["CHAPTER_CODE"].split("CC")[-1]
        difficulty = q["DIFFICULTY"]
        difficulty = "DIFF_{num}".format(num=q["DIFFICULTY"])
        row_id = "{today}-{code}".format(today=today.isoformat(), code=code)
        
        search = "SELECT * FROM DOWNLOAD_HISTORY WHERE ID = '{id}';".format(id=row_id)
        curs.execute(search)
        
        his_row = curs.fetchall()
        if len(his_row) == 0:
            insert = "INSERT INTO DOWNLOAD_HISTORY(ID, UNIT_CODE, COUNT, {difficulty}) VALUES ('{id}', '{unit_code}', 1, 1);".format(difficulty=difficulty, id=row_id, unit_code=q["CHAPTER_CODE"])
            curs.execute(insert)
            conn.commit()
        else:
            update = "UPDATE DOWNLOAD_HISTORY SET COUNT = {count}, {difficulty} = {d} WHERE ID = '{id}';".format(id=row_id, count=int(his_row[0]["COUNT"])+1, difficulty=difficulty, d=int(his_row[0][difficulty])+1)
            curs.execute(update)
            conn.commit()
    
    conn.close()
    
    
# 문항 출제 api
class visangApi(Resource):
    def post(self):
        try:
            # request data
            grade = request.get_json()['grade']
            #semester = list(request.get_json()['semester'])
            lesson = dict(request.get_json()['lesson'])
            #session = dict(request.get_json()['session'])
            
            session = list(request.get_json()['session'])
            #difficulty = dict(request.get_json()['difficulty'])
            d_type = str(request.get_json()['dType'])
            count = request.get_json()['count']
            service_type = request.get_json()['serviceType']

            if count <= 0:
                return {'error': 'count is bigger than zero'}
            elif len(session) == 0:
                return {'error': 'session code error'}
            
            if d_type == "A":
                if count == 5:
                    difficulty = {
                        "1": 2,
                        "2": 1,
                        "3": 2
                    }
                elif count == 10:
                    difficulty = {
                        "1": 4,
                        "2": 3,
                        "3": 3
                    }
                elif count == 15:
                    difficulty = {
                        "1": 5,
                        "2": 5,
                        "3": 5
                    }
                elif count == 20:
                    difficulty = {
                        "1": 7,
                        "2": 6,
                        "3": 7
                    }
                elif count == 25:
                    difficulty = {
                        "1": 8,
                        "2": 8,
                        "3": 9
                    }
            elif d_type == "B":
                if count == 5:
                    difficulty = {
                        "3": 2,
                        "4": 1,
                        "5": 2
                    }
                elif count == 10:
                    difficulty = {
                        "3": 4,
                        "4": 3,
                        "5": 3
                    }
                elif count == 15:
                    difficulty = {
                        "3": 5,
                        "4": 5,
                        "5": 5
                    }
                elif count == 20:
                    difficulty = {
                        "3": 7,
                        "4": 6,
                        "5": 7
                    }
                elif count == 25:
                    difficulty = {
                        "3": 8,
                        "4": 8,
                        "5": 9
                    }
            else:
                return {'erorr' : '난이도 유형이 올바르지 않습니다.'}
            
            questions = []
            
            logger.info("Start getQuestionInfo")
            #question_rows = getQuestionInfo(unit_value=unit_value, chapter_code=chapter_code, lbno=session_value)
            question_rows = getQuestionInfo(session, d_type)
            logger.info("End getQuestionInfo")
            
            logger.info("Start checking service type")
            question_info = []
            for q in question_rows:
                logger.info("{id}".format(id=q['ETC_CATEGORY5']))
                answer_bulk, answer_seq, quize_type, serviceType = answerParsing(q["ANSWER_HTML"], q["BODY_HTML"])

                serviceType = q['EXT_FEILD15']
                if service_type == "online":
                    if serviceType == "online":
                        question_info.append(q)
                else:
                    question_info.append(q)
                    
            random.shuffle(question_info)
            logger.info("End checking service type")
            
            logger.info("number of all questions")
            logger.info(len(question_info))
            
            if len(question_info) == 0:
                return {'error' : '조건에 맞는 문항이 없습니다.'}
            
            q_temp = dict()
            
            d = 0
            for key, value in difficulty.items():
                d += value
                q_temp[key] = []
                
            logger.info(q_temp)
                            
            if d == 0: # 난이도별로 문제를 따로 요청하지 않았을 때
                logger.info("난이도별 문제 수 지정 안함")
                while True:
                    choice = random.randint(0, len(question_info)-1)
                    if len(question_info) >= count:
                        if question_info[choice] not in questions:
                            questions.append(question_info[choice])
                    else:
                        questions.append(question_info[choice])
                           
                    if len(questions) == count:
                            break
            else:
                logger.info("난이도별 문제 수 지정")

                for q in question_info:
                    q_temp[str(q["DIFFICULTY"])].append(q)
                
                zero_len = []
                for i, qt in enumerate(q_temp):
                    if len(q_temp[qt]) == 0:
                        zero_len.append(i)
                
                logger.info("zero length : {zero_len}".format(zero_len=zero_len))
                if len(zero_len) == 0:
                    pass
                elif len(zero_len) == 1:
                    logger.info("난이도별 문제 수 수정 {zero_len}".format(zero_len=len(zero_len)))
                    if zero_len[0] == 0:
                        if d_type == "A":
                            if count == 5:
                                difficulty = {
                                    "1": 0,
                                    "2": 2,
                                    "3": 3
                                }
                            elif count == 10:
                                difficulty = {
                                    "1": 0,
                                    "2": 5,
                                    "3": 5
                                }
                            elif count == 15:
                                difficulty = {
                                    "1": 0,
                                    "2": 7,
                                    "3": 8
                                }
                            elif count == 20:
                                difficulty = {
                                    "1": 0,
                                    "2": 10,
                                    "3": 10
                                }
                            elif count == 25:
                                difficulty = {
                                    "1": 0,
                                    "2": 12,
                                    "3": 13
                                }
                        else:
                            if count == 5:
                                difficulty = {
                                    "3": 0,
                                    "4": 2,
                                    "5": 3
                                }
                            elif count == 10:
                                difficulty = {
                                    "3": 0,
                                    "4": 5,
                                    "5": 5
                                }
                            elif count == 15:
                                difficulty = {
                                    "3": 0,
                                    "4": 7,
                                    "5": 8
                                }
                            elif count == 20:
                                difficulty = {
                                    "3": 0,
                                    "4": 10,
                                    "5": 10
                                }
                            elif count == 25:
                                difficulty = {
                                    "3": 0,
                                    "4": 12,
                                    "5": 13
                                }
                    elif zero_len[0] == 1:
                        if d_type == "A":
                            if count == 5:
                                difficulty = {
                                    "1": 2,
                                    "2": 0,
                                    "3": 3
                                }
                            elif count == 10:
                                difficulty = {
                                    "1": 5,
                                    "2": 0,
                                    "3": 5
                                }
                            elif count == 15:
                                difficulty = {
                                    "1": 7,
                                    "2": 0,
                                    "3": 8
                                }
                            elif count == 20:
                                difficulty = {
                                    "1": 10,
                                    "2": 0,
                                    "3": 10
                                }
                            elif count == 25:
                                difficulty = {
                                    "1": 12,
                                    "2": 0,
                                    "3": 13
                                }
                        else:
                            if count == 5:
                                difficulty = {
                                    "3": 2,
                                    "4": 0,
                                    "5": 3
                                }
                            elif count == 10:
                                difficulty = {
                                    "3": 5,
                                    "4": 0,
                                    "5": 5
                                }
                            elif count == 15:
                                difficulty = {
                                    "3": 7,
                                    "4": 0,
                                    "5": 8
                                }
                            elif count == 20:
                                difficulty = {
                                    "3": 10,
                                    "4": 0,
                                    "5": 10
                                }
                            elif count == 25:
                                difficulty = {
                                    "3": 12,
                                    "4": 0,
                                    "5": 13
                                }
                    else:
                        if d_type == "A":
                            if count == 5:
                                difficulty = {
                                    "1": 2,
                                    "2": 3,
                                    "3": 0
                                }
                            elif count == 10:
                                difficulty = {
                                    "1": 5,
                                    "2": 5,
                                    "3": 0
                                }
                            elif count == 15:
                                difficulty = {
                                    "1": 7,
                                    "2": 8,
                                    "3": 0
                                }
                            elif count == 20:
                                difficulty = {
                                    "1": 10,
                                    "2": 10,
                                    "3": 0
                                }
                            elif count == 25:
                                difficulty = {
                                    "1": 12,
                                    "2": 13,
                                    "3": 0
                                }
                        else:
                            if count == 5:
                                difficulty = {
                                    "3": 2,
                                    "4": 3,
                                    "5": 0
                                }
                            elif count == 10:
                                difficulty = {
                                    "3": 5,
                                    "4": 5,
                                    "5": 0
                                }
                            elif count == 15:
                                difficulty = {
                                    "3": 7,
                                    "4": 8,
                                    "5": 0
                                }
                            elif count == 20:
                                difficulty = {
                                    "3": 10,
                                    "4": 10,
                                    "5": 0
                                }
                            elif count == 25:
                                difficulty = {
                                    "3": 12,
                                    "4": 13,
                                    "5": 0
                                }
                else:
                    logger.info("난이도별 문제 수 수정 {zero_len}".format(zero_len=len(zero_len)))
                    if zero_len == [0, 1]:
                        if d_type == "A":
                            if count == 5:
                                difficulty = {
                                    "1": 0,
                                    "2": 0,
                                    "3": 5
                                }
                            elif count == 10:
                                difficulty = {
                                    "1": 0,
                                    "2": 0,
                                    "3": 10
                                }
                            elif count == 15:
                                difficulty = {
                                    "1": 0,
                                    "2": 0,
                                    "3": 15
                                }
                            elif count == 20:
                                difficulty = {
                                    "1": 0,
                                    "2": 0,
                                    "3": 20
                                }
                            elif count == 25:
                                difficulty = {
                                    "1": 0,
                                    "2": 0,
                                    "3": 25
                                }
                        else:
                            if count == 5:
                                difficulty = {
                                    "3": 0,
                                    "4": 0,
                                    "5": 5
                                }
                            elif count == 10:
                                difficulty = {
                                    "3": 0,
                                    "4": 0,
                                    "5": 10
                                }
                            elif count == 15:
                                difficulty = {
                                    "3": 0,
                                    "4": 0,
                                    "5": 15
                                }
                            elif count == 20:
                                difficulty = {
                                    "3": 0,
                                    "4": 0,
                                    "5": 20
                                }
                            elif count == 25:
                                difficulty = {
                                    "3": 0,
                                    "4": 0,
                                    "5": 25
                                }
                    elif zero_len == [0, 2]:
                        if d_type == "A":
                            if count == 5:
                                difficulty = {
                                    "1": 0,
                                    "2": 5,
                                    "3": 0
                                }
                            elif count == 10:
                                difficulty = {
                                    "1": 0,
                                    "2": 10,
                                    "3": 0
                                }
                            elif count == 15:
                                difficulty = {
                                    "1": 0,
                                    "2": 15,
                                    "3": 0
                                }
                            elif count == 20:
                                difficulty = {
                                    "1": 0,
                                    "2": 20,
                                    "3": 0
                                }
                            elif count == 25:
                                difficulty = {
                                    "1": 0,
                                    "2": 25,
                                    "3": 0
                                }
                        else:
                            if count == 5:
                                difficulty = {
                                    "3": 0,
                                    "4": 5,
                                    "5": 0
                                }
                            elif count == 10:
                                difficulty = {
                                    "3": 0,
                                    "4": 10,
                                    "5": 0
                                }
                            elif count == 15:
                                difficulty = {
                                    "3": 0,
                                    "4": 15,
                                    "5": 0
                                }
                            elif count == 20:
                                difficulty = {
                                    "3": 0,
                                    "4": 20,
                                    "5": 0
                                }
                            elif count == 25:
                                difficulty = {
                                    "3": 0,
                                    "4": 25,
                                    "5": 0
                                }
                    else:
                        if d_type == "A":
                            if count == 5:
                                difficulty = {
                                    "1": 5,
                                    "2": 0,
                                    "3": 0
                                }
                            elif count == 10:
                                difficulty = {
                                    "1": 10,
                                    "2": 0,
                                    "3": 0
                                }
                            elif count == 15:
                                difficulty = {
                                    "1": 15,
                                    "2": 0,
                                    "3": 0
                                }
                            elif count == 20:
                                difficulty = {
                                    "1": 20,
                                    "2": 0,
                                    "3": 0
                                }
                            elif count == 25:
                                difficulty = {
                                    "1": 25,
                                    "2": 0,
                                    "3": 0
                                }
                        else:
                            if count == 5:
                                difficulty = {
                                    "3": 5,
                                    "4": 0,
                                    "5": 0
                                }
                            elif count == 10:
                                difficulty = {
                                    "3": 10,
                                    "4": 0,
                                    "5": 0
                                }
                            elif count == 15:
                                difficulty = {
                                    "3": 15,
                                    "4": 0,
                                    "5": 0
                                }
                            elif count == 20:
                                difficulty = {
                                    "3": 20,
                                    "4": 0,
                                    "5": 0
                                }
                            elif count == 25:
                                difficulty = {
                                    "3": 25,
                                    "4": 0,
                                    "5": 0
                                }
                        
                logger.info(difficulty)
                
                for key, value in difficulty.items():
                    if len(q_temp[key]) == value:
                        continue
                    if len(q_temp[key]) < value:
                        random_choice = random.choices(q_temp[key], k=value-len(q_temp[key]))
                        for r in random_choice:
                            q_temp[key].append(r)
                    else:
                        q_temp[key] = random.sample(q_temp[key], value)
                        
                # 차시 순서대로 정렬                
                s_temp = dict()
                for s in session:
                    s_temp[str(s)] = []
                    
                logger.info(s_temp)
                for key, value in q_temp.items():
                    logger.info(len(value))
                    for v in value:
                        s_temp[str(v['LBNO'])].append(v)
                        
                for key, value in s_temp.items():
                    for v in value:
                        questions.append(v)

                #if len(questions) != count:
                #    return {"error": "생성 문항수를 바르게 입력하세요."}
                #if counter >= 100:
                #    return {"error": "지정한 난이도에 해당하는 문항 부족"}
                    
            logger.info("number of select questions : {count}".format(count=len(questions)))
            
            success = []
            fail = []
            
            stems = []
            for i, q in enumerate(questions):
                try:
                    logger.info("{id} {lbno} {difficult}".format(id=q["ETC_CATEGORY5"], lbno=q["LBNO"], difficult=q["DIFFICULTY"]))
                    gen = getGenerate(q)
                    stems.append(gen)
                    if q not in success:
                        success.append(q)
                except:
                    error_log.error("{id} {lbno} {difficult}".format(id=q["ETC_CATEGORY5"], lbno=q["LBNO"], difficult=q["DIFFICULTY"]))
                    error_log.error(traceback.format_exc())
                    if q not in fail:
                        fail.append(q)
                        
                        webhook_data["attachments"][0]["fields"][0]["value"] = "```{id}```".format(id=q["ETC_CATEGORY5"])
                        webhook_data["attachments"][0]["fields"][1]["value"] = "```{message}```".format(message=traceback.format_exc())
                        requests.post(url=webhook_url, data=json.dumps(webhook_data))
                    continue
                    #if last_success == None:
                    #    return {'error' : '조건에 맞는 문항이 없습니다.'}
                    #else:
                    #    gen = getGenerate(last_success)
                    #    stems.append(gen)
                    
            if len(success) == 0:
                return {'error' : '조건에 맞는 문항이 없습니다.'}
            else:
                if len(stems) != count:
                    while True:
                        gen = getGenerate(random.choice(success))
                        stems.append(gen)
                        
                        if len(stems) == count:
                            break
                    

            result = dict()
            
            gen_questions = []
            
            d_index = 0
            for q, s in zip(questions, stems):
                temp = {
                    "id": s["id"],
                    "session": int(q["LBNO"]), #q["CATEGORY4"].replace("02", "").strip(),
                    "difficulty": int(q["DIFFICULTY"]), 
                }
            
                html = dict()
                    
                if len(s["image_list"]) == 0:
                    body_html = s["body_html"]
                    explanation_html = s["explanation_html"]
                elif len(s["image_list"]) == 1:
                    body_html = s["body_html"] + '<div class="image_area">' + s['image_list'][0].replace("\n", "") + '</div>'
                    explanation_html = s["explanation_html"]
                else:
                    body_html = s["body_html"] + '<div class="image_area">' + s['image_list'][0].replace("\n", "") + '</div>'
                    explanation_html = '<div class="image_area">' + s['image_list'][1] + '</div>' + s["explanation_html"]
                    
                answer_html = s["answer_html"]
                answer_bulk, answer_seq, quize_type, serviceType = answerParsing(answer_html, body_html) # 순서가 있는 정답 구분을 위해 body_html도 파싱
                
                serviceType = q['EXT_FEILD15']
                
                html["body"] = body_html
                html["comment"] = explanation_html
                    
                html["answer"] = answer_html
                    
                if s["list_html"] == LIST_NONE:
                    list_html = ""
                    html["list"] = list_html
                        
                    temp["html"] = html
                    temp["answerBulk"] = answer_bulk
                    temp["answerSeq"] = answer_seq
                else:
                    list_html = s["list_html"]
                    html["list"] = list_html
                        
                    list_bulk = listParsing(list_html)
            
                    temp["html"] = html
                    temp["answerBulk"] = answer_bulk
                    temp["answerSeq"] = answer_seq
                    temp["listBulk"] = list_bulk
                
                temp["serviceType"] = serviceType
                temp["quizType"] = quize_type
                
                gen_questions.append(temp)
                d_index += 1
                
                if len(gen_questions) == int(count):
                    break
                
            result["result"] = gen_questions
            
            genCount(count, questions)
            return result
        except Exception as e:
            #return {'error': str(e)}
            return traceback.format_exc()

api.add_resource(visangApi, '/boin/v1/request/quiz')

# 쌍둥이 문항 출제
class visangApi2(Resource):
    def post(self):
        try:
            id = request.get_json()['id']
            count = request.get_json()['count']
            
            conn = getConnection()
            curs = conn.cursor(pymysql.cursors.DictCursor)
            
            sql = "SELECT EXT_FEILD15 FROM QUESTIONS WHERE ETC_CATEGORY5 = '{id}';".format(id=id)
            curs.execute(sql)
            service_type = curs.fetchone()["EXT_FEILD15"]
            
            if id.startswith("GT"):
                gen_questions = []
                for i in range(count):
                    body_html, answer_html, explanation_html, list_html = generate(id)
                    
                    res = {
                        "r": 0,
                        "id": id,
                        "body_html": body_html,
                        "list_html": list_html,
                        "answer_html": answer_html,
                        "explanation_html": explanation_html,
                        "image_list": []
                    }
                    temp = {
                        "id": res["id"],
                    }
                    
                    html = dict()
                        
                    if len(res["image_list"]) == 0:
                        body_html = res["body_html"]
                        explanation_html = res["explanation_html"]
                    elif len(res["image_list"]) == 1:
                        body_html = res["body_html"] + '<div class="image_area">' + res['image_list'][0].replace("\n", "") + '</div>'
                        explanation_html = res["explanation_html"]
                    else:
                        body_html = res["body_html"] + '<div class="image_area">' + res['image_list'][0].replace("\n", "") + '</div>'
                        explanation_html = '<div class="image_area">' + res['image_list'][1] + '</div>' + res["explanation_html"]
                        
                    answer_html = res["answer_html"]
                    answer_bulk, answer_seq, quize_type, serviceType = answerParsing(answer_html, body_html) # 순서가 있는 정답 구분을 위해 body_html도 파싱
                    
                    serviceType = service_type
                    
                    html["body"] = body_html
                    html["comment"] = explanation_html
                        
                    html["answer"] = answer_html
                        
                    if res["list_html"] == LIST_NONE:
                        list_html = ""
                        html["list"] = list_html
                            
                        temp["html"] = html
                        temp["answerBulk"] = answer_bulk
                        temp["answerSeq"] = answer_seq
                        
                    else:
                        list_html = res["list_html"]
                        html["list"] = list_html
                            
                        list_bulk = listParsing(list_html)
                
                        temp["html"] = html
                        temp["answerBulk"] = answer_bulk
                        temp["answerSeq"] = answer_seq
                        temp["listBulk"] = list_bulk
                    
                    temp["serviceType"] = serviceType
                    temp["quizType"] = quize_type
                    
                    gen_questions.append(temp)
            else:
                func = FUNC_DICT[id]
                
                gen_questions = []
                for i in range(count):
                    try:
                        hmls_material, hmls_stem_material, hmls_answer_material, svgs = func2hmls(func, 1, w_dict, polygon=True)
                    except:
                        hmls_material, hmls_stem_material, hmls_answer_material, svgs = func2hmls(func, 1, w_dict)

                    res = hml2html(hmls_material[0])
                    
                    res["image_list"] = svgs
                    res["id"] = id
                    
                    temp = {
                        "id": res["id"],
                    }
                
                    html = dict()
                        
                    if len(res["image_list"]) == 0:
                        body_html = res["body_html"]
                        explanation_html = res["explanation_html"]
                    elif len(res["image_list"]) == 1:
                        body_html = res["body_html"] + '<div class="image_area">' + res['image_list'][0].replace("\n", "") + '</div>'
                        explanation_html = res["explanation_html"]
                    else:
                        body_html = res["body_html"] + '<div class="image_area">' + res['image_list'][0].replace("\n", "") + '</div>'
                        explanation_html = '<div class="image_area">' + res['image_list'][1] + '</div>' + res["explanation_html"]
                        
                    answer_html = res["answer_html"]
                    answer_bulk, answer_seq, quize_type, serviceType = answerParsing(answer_html, body_html) # 순서가 있는 정답 구분을 위해 body_html도 파싱
                    
                    serviceType = service_type
                    
                    html["body"] = body_html
                    html["comment"] = explanation_html
                        
                    html["answer"] = answer_html
                        
                    if res["list_html"] == LIST_NONE:
                        list_html = ""
                        html["list"] = list_html
                            
                        temp["html"] = html
                        temp["answerBulk"] = answer_bulk
                        temp["answerSeq"] = answer_seq
                        
                    else:
                        list_html = res["list_html"]
                        html["list"] = list_html
                            
                        list_bulk = listParsing(list_html)
                
                        temp["html"] = html
                        temp["answerBulk"] = answer_bulk
                        temp["answerSeq"] = answer_seq
                        temp["listBulk"] = list_bulk
                    
                    temp["serviceType"] = serviceType
                    temp["quizType"] = quize_type
                    
                    gen_questions.append(temp)
                
            result = dict()
            result["result"] = gen_questions

            #genCount(count)
            return result
        except Exception as e:
            return traceback.format_exc()

api.add_resource(visangApi2, '/boin/v1/request/re_quiz')
    
# 학년, 학기, 단원, 차시 정보 출력 api
class visangListApi(Resource):
    def post(self):
        try:
            grade = request.get_json()['grade']
            
            conn = getConnection()
            curs = conn.cursor(pymysql.cursors.DictCursor)
            
            sql = 'SELECT * FROM GRADE_UNIT WHERE EDU_GUBN="초등" and SCHOOL_YEAR={grade};'.format(grade=grade)
            curs.execute(sql)
            lesson = curs.fetchall()
            
            sql = 'SELECT * FROM LEARNING_OBJECTIVES WHERE GUNO >= {start} and GUNO <= {end} and ACTIVE = 1;'.format(start=lesson[0]["GUNO"], end=lesson[-1]["GUNO"])
            curs.execute(sql)
            session = curs.fetchall()

            conn.close()
            
            result = [
                {
                    "grade": grade,
                    "semester": 1,
                    "content": []
                },
                {
                    "grade": grade,
                    "semester": 2,
                    "content": []
                },
            ]
            
            for i in lesson:
                temp = {}
                temp["lesson"] = i["UNIT"]
                temp["value"] = i["UNIT_VALUE"]
                temp["content"] = []
                
                
                for j in session:
                    if i["GUNO"] == j["GUNO"]:
                        temp2 = {
                            "session" : j["LBNO"],
                            "value": j["LESSON"],
                            "online" : j["SERVICE_TYPE"]
                        }

                        temp["content"].append(temp2)
                
                if i["SEMESTER"] == 1:
                    result[0]["content"].append(temp)
                else:
                    result[1]["content"].append(temp)
                
            return result
        except Exception as e:
            return {'error': str(e)}
        
api.add_resource(visangListApi, '/boin/v1/request/list')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8878)#, debug=True)
