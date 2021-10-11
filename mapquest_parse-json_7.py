import urllib.parse
import requests
from datetime import datetime, timedelta
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# variable to use to determine PM and AM
current_hour_str = now.strftime("%H")
standard_time = int(current_hour_str)
current_min = now.strftime("%M")


if(standard_time < 12):
    time = str(standard_time) + ":" + str(current_hour_str) + " AM"
else:
    pmTime = standard_time - 12
    time = str(pmTime) + ":" + str(current_hour_str) + " PM"



main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "qfXMh1FJl7sDlVKeJ93Xkmw8jGD3zxhn"


while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Time Started: " + time)
        print("Trip Duration: "+ (json_data["route"]["formattedTime"]))
        timeList = [current_time, (json_data["route"]["formattedTime"])]

        mysum = timedelta()
        for i in timeList:
            (h, m, s) = i.split(':')
            d =timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            mysum += d

        print("Time Ended: " + str(mysum))
        print("Kilometers: "+ str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): "+ str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=======================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")

