import WriteToExcel as wexcel
# import GetAruodas as aruodas
# import GetDomoplius as domo
# import ShowResultsWindow as showResults
from os import path
import MessageBox

class RealEstateObject:
    def __init__(self, address, price, link):
        self.address = address
        self.price = price
        self.link = link


wexcel.deleteOldReport()
wexcel.copyExcel()
if path.exists(wexcel.newExcelPath) == False:
    MessageBox.Mbox("Error", "Could not create Excel to fill report.", 0)
    exit()




MessageBox.Mbox("Completed", "The report is prepared.", 0)