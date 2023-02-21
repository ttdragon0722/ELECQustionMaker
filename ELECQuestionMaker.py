"""
=============================

version:1

自動抓題庫並製作成考卷的工具

create:嘎嘎,臘腸,克斯

=============================
"""

# support
from package.mkDocx import QuestionDocx, AnswerDocx,MkJson
from package.mkOutput import mkOutputDir
from package.terminalColor import *
from package.data import *

from json import load,dump
from sys import exit

# terminal
from os import system
import inquirer

from random import sample


#* ================== init ============================
# ================ selection ==========================

def inputError(answer,current:str):
    if not current.isdigit() or not int(current) < 474:
        raise inquirer.errors.ValidationError("", reason="克斯不喜歡你給的數字 :( ")
    return True

#mode 
mode_selection = [
    inquirer.List(
        "start_mode",
        message="開始選題:",
        choices=["Manual", "Random", "Quit"]
    ),
]

random = [
    inquirer.Text(
        'top',
        message='起始值:',
        validate=inputError
    ),
    inquirer.Text(
        'bottom',
        message='結束值:',
        validate=inputError
    ),
    inquirer.Text(
        'amount',
        message='選取數量:',
        validate=inputError
    )
]

random_output_section = [
    inquirer.List(
        'action',
        message='finish?',
        choices=['Finish','Redraw','Quit']
    )
]



# selection
selected = []
selection = [
    inquirer.List(
        "action",
        message=f"目前已選 {len(selected)} 題",
        choices=["Yes", "No", "Quit", "Preview", 'Finish','Prev']
    ),
]
# Preview
preview_back = [
    inquirer.List(
        "action",
        message=f"目前已選 {len(selected)} 題",
        choices=["Back", 'Delete']
    ),
]

# checkbox
kill_list = [
    inquirer.Checkbox(
        "kill_list",
        message="What question you want to delete?",
        choices=[]
    )
]
# ===========================================

# load question bank
with open("nowCheck.json", "r", encoding="utf-8") as f:
    nowCheck = load(f)
questions = getRemainQuestionByStartId(int(nowCheck["now"]))

PATH = nowCheck['output_dir']

# 輸出題目
def questionBankOutput(question: list):
    print(f"""
{Yellow('第 '+str(question[0])+' 題:')}
    {question[1]}
    {"" if question[4]=='' else "圖片: "+question[4]}
    - 選項 A: {question[5]}
    - 選項 B: {question[6]}
    - 選項 C: {question[7]}
    - 選項 D: {question[8]}

{Yellow("正確答案")}: 
{question[2]}
{Yellow("解析")}: 
{question[3]}  
    """)

# ============== main ================================

# 開始使用的模式
start_mode = inquirer.prompt(mode_selection)
match start_mode["start_mode"]:
    case 'Manual':
        mode = 'select'
    case 'Random':
        mode = 'Random'
    case 'Quit':
        exit()
    case 'Setting':
        mode = 'Setting'

while True:
    system('cls')
    match mode:
        case 'select':
            questionBankOutput(questions[int(nowCheck['now'])])
            action = inquirer.prompt(selection)

        case 'Random':
            random_data = inquirer.prompt(random)


            randomQuestionBank = [rqb for rqb in range(int(random_data['top'])-1,int(random_data['bottom']))]
            random_output = sample(randomQuestionBank,int(random_data['amount']))
            random_output.sort()
            selected = random_output
            system('cls')
            for questionNum in selected:
                questionBankOutput(questions[questionNum])
                print(Cyan('======================================='))
            action = inquirer.prompt(random_output_section)

        case 'preview':
            for questionNum in selected:
                questionBankOutput(questions[questionNum])
                print(Cyan('======================================='))
            action = inquirer.prompt(preview_back)
        case 'delete':
            for questionNum in selected:
                questionBankOutput(questions[questionNum])
                print(Cyan('======================================='))
            delete_list = inquirer.prompt(kill_list)
            for d in delete_list['kill_list']:
                del selected[selected.index(d)]
            selection = [
                inquirer.List(
                    f"action",
                    message=f"目前已選 {len(selected)} 題",
                    choices=["Yes", "No", "Quit", "Preview", 'Finish','Prev']
                ),
            ]
            action['action'] = 'Back'

    match action['action']:
        case 'Finish':
            OUTPUT_PATH = mkOutputDir(PATH)
            print(OUTPUT_PATH)
            QuestionDocx(OUTPUT_PATH,selected,questions)
            AnswerDocx(OUTPUT_PATH,selected,questions)
            MkJson(OUTPUT_PATH,selected,questions)
            exit()

        case 'Yes':
            selected.append(int(nowCheck['now']))
            selection = [
                inquirer.List(
                    f"action",
                    message=f"目前已選 {len(selected)} 題",
                    choices=["Yes", "No", "Quit", "Preview", 'Finish','Prev']
                )
            ]
            changeVisibility(int(nowCheck['now']),True)
            nowCheck['now'] += 1
        case 'No':
            changeVisibility(int(nowCheck['now']),False)
            nowCheck['now'] += 1
        case 'Preview':
            mode = 'preview'
            preview_back = [
                inquirer.List(
                    f"action",
                    message=f"目前已選 {len(selected)} 題",
                    choices=["Back", 'Delete']
                ),
            ]
        case 'Back':
            mode = 'select'
        case 'Delete':
            mode = 'delete'
            delete_choices = []
            for delete_num in selected:
                delete_choices.append(int(delete_num)+1)
            delete_choices.sort()
            kill_list = [
                inquirer.Checkbox(
                    "kill_list",
                    message="What question you want to delete?",
                    choices=delete_choices
                )
            ]

        case 'Redraw':
            mode = None
            random_output = sample(randomQuestionBank,int(random_data['amount']))
            random_output.sort()
            selected = random_output
            system('cls')
            for questionNum in selected:
                questionBankOutput(questions[questionNum])
                print(Cyan('======================================='))
            action = inquirer.prompt(random_output_section)

        case 'Prev':
            if nowCheck['now'] != 0:
                nowCheck['now'] -= 1
            else:
                pass

        case 'Quit':
            with open("nowCheck.json","w",encoding="utf-8") as f:
                dump(nowCheck,f)
            exit()
