from docx import Document
from docx.shared import Inches

# 製作輸出word檔案

# 

def QuestionDocx(path):
    document = Document()

    records = (
        (3, '101'),
        (7, '422'),
        (4, '631')
    )

    table = document.add_table(rows=1, cols=2)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Qty'
    hdr_cells[1].text = 'Id'

    for qty, id, desc in records:
        row_cells = table.add_row().cells
        row_cells[0].text = str(qty)
        row_cells[1].text = id
        row_cells[2].text = desc

    document.add_page_break()


    document.save(path+"\question.docx")

def AnswerDocx(path):
    document = Document()



    document.save(path+'\\answer.docx')