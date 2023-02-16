"""
=============================

version:1

自動抓題庫並製作成考卷的工具

create:嘎嘎,臘腸,克斯

=============================
"""

from package.mkDocx import QuestionDocx,AnswerDocx
from package.mkOutput import mkOutputDir
from package.questionGetter import *

OUTPUT_PATH = mkOutputDir(r"C:\Users\雷克斯\Desktop") 

# mkOutputDocx(OUTPUT_PATH)