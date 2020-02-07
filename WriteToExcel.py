import os.path
from os import path
import time
import shutil

excelTemplatePath = "Estate_report_template.xlsx"
newExcelPath = "Estate_report.xlsx"

def deleteOldReport():
    if path.exists(newExcelPath):
        os.remove(newExcelPath)
        print("Old report deleted.")

def copyExcel():
    if path.exists(excelTemplatePath):
        shutil.copy(excelTemplatePath, newExcelPath)
        time.sleep(5)
        print("Report file to fill created")
