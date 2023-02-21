import sqlite3

def addQuestion(question:str, answer:str, details:str,img:str,option1:str,option2:str,option3:str,option4:str,show:str):
    db = sqlite3.connect('questionBank.db')
    cur = db.cursor()
    cur.execute(f"INSERT INTO question VALUES ('{question}', '{answer}', '{details}', '{img}', '{option1}', '{option2}', '{option3}', '{option4}', '{show}');")
    cur.execute("SELECT * FROM question;")
    rows = cur.fetchall()
    db.commit()
    db.close()
    return rows

def deleteAllData():
    db = sqlite3.connect('questionBank.db')
    cur = db.cursor()
    cur.execute(f"DELETE FROM question;")
    rows = cur.fetchall()
    db.commit()
    db.close()
    return rows

def getRemainQuestionByStartId(id:int):
    db = sqlite3.connect('questionBank.db')
    cur = db.cursor()
    cur.execute(f"SELECT * FROM question;")
    rows = cur.fetchall()
    db.commit()
    db.close()
    return rows
    
def changeVisibility(id:int,show:str):
    db = sqlite3.connect('questionBank.db')
    cur = db.cursor()
    cur.execute(f"UPDATE question SET show = '{show}' WHERE questionId = '{id}';")
    rows = cur.fetchall()
    db.commit()
    db.close()
    return rows
