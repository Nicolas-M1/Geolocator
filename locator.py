import sys
import json
import requests

baseUrl = "https://ipwhois.app/json/"

userArgs = sys.argv;
isOwnIp = False #this will be used to determine whether the IP should be printed to the screen, which it will be if the user is using their own 
ip = ""
if len(userArgs) <=1:
    ip = "" #just making sure to keep it blank, the API will then use the user's ip instead
    isOwnIp = True
else:
    ip = sys.argv[1]
    isOwnIp = False
requestUrl = baseUrl+ip

print(requestUrl)

responseData = requests.get(requestUrl)

if responseData: #If the get request was successful
    dataDict = json.loads(responseData.text) #turn the response string (which is in JSON form) into a python dictionary
    if dataDict["success"]: #If the API was able to successfully get data for the user
        #IP Address
        if isOwnIp:
            print("The IP address of your router or proxy:\t\t"+dataDict["ip"])

        #Physical location
        locationStr = dataDict["city"]+", "+dataDict["region"]+", "+dataDict["country"]
        print(locationStr)

        #Lat-Long Coordinates
        if "latitude" in dataDict and "longitude" in dataDict:
            coordinateStr = "Latitude: "+dataDict["latitude"]+"   Longitude: "+dataDict["longitude"]
            print(coordinateStr)
        else:
            print("The API did not return coordinates")

        # ISP details
        ispStr = dataDict["isp"]
        print("With service provider: "+ispStr)
    else:
        print("The API was not able to retrieve data about the IP address")
    