#Importing libraries
from datetime import datetime, time  #Used for processing date and time
import requests
from requests.sessions import session                #Send GET requests to API
from win10toast import ToastNotifier
import time
from plyer import notification

notify = ToastNotifier()

def vaccheck(acceptLanguage, input_pincode, input_date):
    #Link to send GET request to API
    calendar_link = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
    day_link = "https://cdn-api.co-vin/api/v2/appointment/sessions/public/findByPin"
    #Header for sending GET request
    browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    #Making the parameters as a dictionary to be sent to API
    PARAMS = {'Accept-Language' : acceptLanguage, 'pincode' : input_pincode, 'date': input_date}
    #Sending GET request to API
    result = requests.get(url= calendar_link, headers= browser_header, params= PARAMS)
    #Extracting data in JSON format
    vacc_data = result.json()
    val1 = vacc_data.get('centers')
    #print(vacc_data)
    #print("\n")
    counter = []
    for i in val1:
        for key,value in i.items():
            if(key == 'sessions'):
                vacc_sessions = value[0]
                for k,v in vacc_sessions.items():
                    # if(k == 'slots'):
                    #     for s in v:
                    #         print(s)
                    if(k == 'available_capacity'):
                        counter.append(v)
                        # if(v == 0):
                        #     print("No vaccination slots available ! Checked at ",time.time())
                        # elif(v > 0):
                        #     print("Vaccination slots available ! Checked at ",time.time())
                    # else:
                    #     print(k, " : ", v)
            # else:
            #     print(key, " : ", value)
        #print("\n")
    #print(counter)
    total = sum(counter)
    if(total > 0):
        notification.notify(title='Vaccination slots available !',message='Book slot now',timeout=4,app_icon=None)
        print("Vaccination slots available ! Checked at ",datetime.now()) 
    else:
        #notification.notify(title='No slots available !',message='Please check again later',timeout = 4,app_icon=None)
        print("No vaccination slots available ! Checked at ",datetime.now())



#Paramets as a part of GET request
print("----------COWIN VACCINATION SLOTS CHECK----------")
acceptLanguage = "en_US"
input_pincode = input("Enter pincode : ");
input_date = input("Enter date : ");


#Obtain system current date
current_date_dobj = datetime.today().date()
#Convert entered date string to date object
input_date_dobj = datetime.strptime(input_date, "%d-%m-%Y").date()

if(input_date_dobj < current_date_dobj):
    print("Invalid date entered !")
    exit()
if(len(input_pincode) > 6 or len(input_pincode) < 0):
    print("Invalid pincode")
    exit()


while True:
    vaccheck(acceptLanguage, input_pincode, input_date)
    time.sleep(30)


#Prints the response received from the API
#print("Response: ",result)



# for i in val1:
#     for key,value in i.items():
#        if(key == 'center_id'):
#            print(key, value)
