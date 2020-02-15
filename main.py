# # import GetAruodas as aruodas
# # import GetDomoplius as domo
# # import ShowResultsWindow as showResults
# import message_box

import get_user_input as userinp
import handle_aruodas as aruodas
import handle_domoplius as domo
import json

min_price, max_price = userinp.get_prices()
min_size, max_size = userinp.get_size()

domo.open_domo()
domo.adjust_choices(min_price, max_price, min_size, max_size)
domo_offers = domo.get_best_offers()
domo.close_browser()

with open('domo_data.txt', 'w') as outfile:
    json.dump(domo_offers, outfile)

aruodas.open_aruodas()
aruodas.adjust_choices(min_price, max_price, min_size, max_size)
aruodas_offers = aruodas.get_best_offers()
aruodas.close_browser()

with open('aruodas_data.txt', 'w') as outfile:
    json.dump(aruodas_offers, outfile)





# handle_aruodas.open_aruodas()
# handle_aruodas.adjust_choices(min_price, max_price, min_size, max_size)

# handle_aruodas.gather_data(min_price, max_price, min_size, max_size)
# # get_user_input.get_size()
# # wexcel.delete_old_report()
# # wexcel.copy_excel()
# # if path.exists(wexcel.newExcelPath) == False:
# #     message_box.mbox( "Error", "Could not create Excel to fill report.", 0 )
# #     exit()
# message_box.mbox( "Completed", "The report is prepared.", 0 )

