import get_user_input as userinp
import handle_aruodas as aruodas
import handle_domoplius as domo
import results_window as mbox
import json
import time


min_price, max_price = userinp.get_prices()
min_size, max_size = userinp.get_size()

domo.open_domo()
domo.adjust_choices(min_price, max_price, min_size, max_size)
domo_offers = domo.get_best_offers()
domo.close_browser()

try:
    with open("domo_data.txt", "w") as outfile:
        json.dump(domo_offers, outfile)
    time.sleep(3)
    outfile.close()
except Exception as e:
    print("Could not handle domo JSON: ", e)


aruodas.open_aruodas()
aruodas.adjust_choices(min_price, max_price, min_size, max_size)
aruodas_offers = aruodas.get_best_offers()
aruodas.close_browser()

try:
    with open("aruodas_data.txt", "w") as outfile:
        json.dump(aruodas_offers, outfile)
    time.sleep(3)
    outfile.close()
except Exception as e:
    print("Could not handle aruodas JSON: ", e)

mbox.show_domo_results(domo_offers)
mbox.show_aruodas_results(aruodas_offers)
