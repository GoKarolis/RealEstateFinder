import os.path
from os import path
import time
import shutil


# Put to google or Jango, or something
excelTemplatePath = "Estate_report_template.xlsx"
newExcelPath = "Estate_report.xlsx"

def delete_old_report():
    if path.exists(newExcelPath):
        os.remove(newExcelPath)
        print("Old report deleted.")

def copy_excel():
    if path.exists(excelTemplatePath):
        shutil.copy(excelTemplatePath, newExcelPath)
        time.sleep(5)
        print("Report file to fill created")
