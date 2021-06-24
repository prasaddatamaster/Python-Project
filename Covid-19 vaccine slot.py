import  requests 
import time
import json
from datetime import datetime , timedelta


print("Welcome !!! You can start seaching for covid vaccine slot near you ")
person_age = int(input('please update the persons age    :\n'))

Area_pincode = ['423203','423105']

total_days = int(input("how many days you are looking for :\n"))

print_flag = 'Y'

current  =  datetime.today()
Reg_form  = [current + timedelta (days = i) for i in range (total_days) ]  
correct_date_formate = [i.strftime("%d-%m-%y") for i  in Reg_form ]  


while True:
    i = 0
    for find_code  in Area_pincode:
        for enter_date in correct_date_formate:
            url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(
                find_code, enter_date)

            requirements = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

            final_op = requests.get(url, headers=requirements)

            if final_op.ok:
                file_json = final_op.json()

                flag = False 
                if file_json['centers']:
                    if (print_flag.lower() == 'Y'):

                        for place in file_json ['centers']:

                            for availability in place ['sessions']:
                                if (availability["min_Age_limit"]<= person_age and availability['available capacity'] > 0 ):
                                    print('The pincode for which you are finding is :' + find_code)
                                    print('It is available in :{}'. format(enter_date))
                                    print('Name of the hospital and destination is :', place['name'])
                                    print('Name for the block is  :', place['block_name'])
                                    print('Price for the vaccine is:', place['fee_type'])
                                    print ("availability of the vaccine is  : ", availability['available_capacity'])


                                    if (availability ['vaccine'] !=''):
                                        print("the type of vaccine is :", availability["vaccine type"])

                                    i = i + 1 
                                else:
                                    pass
                    else:
                        pass
                else:
                    print('I found no response')

if (i==0):
    print("Right now no vaccine Slot available , Try after some time ")

else:
    print("searching is over")

date_now =  datetime.now + timedelta(minutes=1)

while datetime.now() < date_now:
    time.sleep(1)
