#import datetime
import requests
from datetime import datetime

#URL = "https://cdn-api.co-vin/api/v2/appointment/sessions/public/findByPin/"
link = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
acceptLanguage = "en_US"
print("COWIN VACCINATION SLOTS CHECK")
input_pincode = input("Enter pincode : ");
input_date = input("Enter date : ");


#pincode = "560076"
#date = "21-05-2021"
browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

PARAMS = {'Accept-Language' : acceptLanguage, 'pincode' : input_pincode, 'date': input_date}

r = requests.get(url= link, headers= browser_header, params= PARAMS)

vacc_data = r.json()
val1 = vacc_data.get('centers')
if(len(val1) == 0):
    print("No centres yet !")
#print(vacc_data)
#print("\n")
counter = []
for i in val1:
    for key,value in i.items():
        if(key == 'sessions'):
            vacc_sessions = value[0]
            for k,v in vacc_sessions.items():
                if(k == 'slots'):
                    for s in v:
                        print(s)
                # if(k == 'available_capacity'):
                #     counter.append(v)
                #     if(v == 0):
                #         print("No vaccination slots available ! Checked at ",time.time())
                #     elif(v > 0):
                #         print("Vaccination slots available ! Checked at ",time.time())
                else:
                    print(k, " : ", v)
        else:
            print(key, " : ", value)
    print("\n")




