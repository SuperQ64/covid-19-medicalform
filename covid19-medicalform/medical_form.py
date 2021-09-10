import sys
import json
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

cc = canvas.Canvas("./out/added_medical_form.pdf")
fontname_g = "ipaexm"
default_font_size = 14
form_info = {}

def write_yes_no(x,y,answer):
    if answer == 'true':
        cc.drawString(x,y,'✓')
    else:
        cc.drawString(x + 45,y,'✓')

def write_checkmark(x,y,answer):
    if answer == 'true':
        cc.drawString(x,y,'✓')

def write_q1():
    answer = form_info['q1']
    if answer[0] == 'false':
        cc.drawString(221,616,answer[1])
        cc.drawString(258,616,answer[2])
        cc.drawString(340,616,answer[3])
        cc.drawString(375,616,answer[4])

    write_yes_no(442,625,answer[0])  
    return

def write_q4():
    answer = form_info['q4']
    if answer[0] == 'true':
        write_checkmark(38,550,answer[1])
        write_checkmark(118,550,answer[2])
        write_checkmark(181,550,answer[3])
        write_checkmark(246,550,answer[4])
        write_checkmark(38,537,answer[5])
        cc.drawString(150,535,answer[6])

    write_yes_no(442,550,answer[0])

def write_q5():
    answer = form_info['q5']
    if answer[0] == 'true':
        write_checkmark(86,497,answer[1])
        write_checkmark(132,497,answer[2])
        write_checkmark(181,497,answer[3])
        write_checkmark(228,497,answer[4])
        write_checkmark(284,497,answer[5])
        write_checkmark(384,497,answer[6])
        write_checkmark(86,480,answer[7])
        cc.drawString(130,480,answer[8])
        write_checkmark(86,463,answer[9])
        cc.drawString(190,463,answer[10])
        write_checkmark(286,463,answer[11])
        cc.drawString(330,463,answer[12])

    write_yes_no(442,492,answer[0])


def write_q6():
    answer = form_info['q6']
    if answer[0] == 'true':
        cc.drawString(300,441,answer[1])

    write_yes_no(442,442,answer[0])

def write_q7():
    answer = form_info['q7']
    if answer[0] == 'true':
        cc.drawString(240,420,answer[1])

    write_yes_no(442,422,answer[0])

def write_q9():
    answer = form_info['q9']
    if answer[0] == 'true':
        cc.drawString(170,370,answer[1])

    write_yes_no(442,377,answer[0])

def write_q10():
    answer = form_info['q10']
    if answer[0] == 'true':
        cc.drawString(70,342,answer[1])
        cc.drawString(280,342,answer[2])
    write_yes_no(442,350,answer[0])

def write_q12():
    answer = form_info['q12']
    if answer[0] == 'true':
        cc.drawString(227,304,answer[1])
        cc.drawString(400,304,answer[2])
    write_yes_no(442,305,answer[0])

def write_name(x,y,name):
    cc.setFont(fontname_g,11)
    cc.drawString(x,y,name)
    cc.setFont(fontname_g,default_font_size)

def write_number(x,y,number):
    number_list = list(number)
    if not '.' in number_list:
        for num in number_list:
            cc.drawString(x,y,num)
            x = x + 16
    else:
        cc.drawString(x,y,number_list[0])
        cc.drawString(x + 16,y,number_list[1])
        cc.drawString(x + 55,y,number_list[3])

def test_method():
    x = 0
    y = 0
    while x < 600 or y < 800:
        cc.drawString(x,0,str(x / 100))
        cc.drawString(0,y,str(y / 100))
        x = x + 100
        y = y + 100

def write(info,file_out):
    font_path = "./font/ipaexm.ttf"
    file_in = "./resource/medical_form_original.pdf"
    global cc
    cc = canvas.Canvas(file_out)
    global form_info
    form_info = info

    pdfmetrics.registerFont(TTFont(fontname_g,font_path))
    cc.setFont(fontname_g,default_font_size)

    page = PdfReader(file_in,decompress=False).pages
    pp = pagexobj(page[0])
    cc.doForm(makerl(cc, pp))

    if int(form_info['age']) < 100:
        form_info['age'] = '0' + form_info['age']

    phone = form_info['phone'].split("-")

    # 予診票に書き込み
    cc.drawString(127,755,form_info['prefecture'])
    cc.drawString(220,755,form_info['city'])
    cc.drawString(60,728,form_info['address'])
    if len(form_info['name']) <= 10:
        cc.drawString(60,690,form_info['name'])
    else:
        write_name(60,690,form_info['name'])
    cc.drawString(273,705,phone[0])
    cc.drawString(273,690,phone[1])
    cc.drawString(330,690,phone[2])
    write_number(67,665,form_info['year'])
    write_number(145,665,form_info['month'])
    write_number(188,665,form_info['day'])
    write_number(263,665,form_info['age'])
    write_number(485,665,form_info['temperature'])

    cc.setFont(fontname_g,12)
    cc.drawString(65,710,form_info['furigana'])
    if form_info['sex'] == '男':
        cc.drawString(338,669,'✓')
    else:
        cc.drawString(373,669,'✓')
    write_q1()
    write_yes_no(442,600,form_info['q2'])
    write_yes_no(442,580,form_info['q3'])
    write_q4()
    write_q5()
    write_q6()
    write_q7()
    write_yes_no(442,402,form_info['q8'])
    write_q9()
    write_q10()
    write_yes_no(442,325,form_info['q11'])
    write_q12()
    write_yes_no(442,285,form_info['q13'])

    if form_info['agreement'] == 'true':
        cc.drawString(377,186,'✓')
    else:
        cc.drawString(466,186,'✓')

    cc.showPage()
    cc.save()

if __name__ == '__main__':
    json_file = sys.argv[1] #json
    file_out = sys.argv[2]  #出力pdfパス
    
    with open(json_file,"r",encoding="utf-8") as f:
        # 予診票に書き込む情報を読み込む
        form_info = json.load(f)

    write(form_info,file_out)