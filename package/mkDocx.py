from docx import Document
from docx.shared import Inches

# 製作輸出word檔案

# 

def QuestionDocx(path):
    document = Document()

    

    document.save(path+"\question.docx")

def AnswerDocx(path):
    document = Document()



    document.save(path+'\\answer.docx')