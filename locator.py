import sys
import json
import requests

baseUrl = "https://ipwhois.app/json/"

userArgs = sys.argv;
if len(userArgs) <1:
    print("No IP address entered, try it like this: \n\tpython3 locator.py 0.0.0.0")
else:
    ip = sys.argv[1]
    print(ip)
    requestUrl = baseUrl+ip
    print(requestUrl)
    responseData = requests.get(requestUrl)

    if responseData: #If the get request was successful
        dataDict = json.loads(responseData.text)
        if dataDict["success"]:
            locationStr = dataDict["city"]+", "+dataDict["region"]+", "+dataDict["country"]
            print(locationStr)
            if "latitude" in dataDict and "longitude" in dataDict:
                coordinateStr = "Latitude: "+dataDict["latitude"]+"   Longitude: "+dataDict["longitude"]
                print(coordinateStr)
            else:
                print("The API did not return coordinates")
            ispStr = dataDict["isp"]
            print("With service provider: "+ispStr)
        else:
            print("The API was not able to retrieve data about the IP address")
    