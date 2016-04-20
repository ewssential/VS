import takePicture

#url = https://api.projectoxford.ai/face/v1.0/detect[?returnFaceId][&returnFaceLandmarks][&returnFaceAttributes]&subscription-key=<550bbc8cf88a4bb7bfb67c25407fc31f>

#faceServiceClient = new FaceServiceClient("Your subscription key");



############ Python 2.7 #############
#import httplib, urllib, base64

#headers = {
#    # Request headers
#    'Content-Type': 'application/json',
#    'Ocp-Apim-Subscription-Key': '550bbc8cf88a4bb7bfb67c25407fc31f',
#}

#params = urllib.urlencode({
#    # Request parameters
#    'returnFaceId': 'true',
#    'returnFaceLandmarks': 'false',
#    'returnFaceAttributes': '{string}',
#})

#try:
#    conn = httplib.HTTPSConnection('api.projectoxford.ai')
#    conn.request("POST", "/face/v1.0/detect?%s" % params, "{body}", headers)
#    response = conn.getresponse()
#    data = response.read()
#    print(data)
#    conn.close()
#except Exception as e:
#    print("[Errno {0}] {1}".format(e.errno, e.strerror))

#####################################


########### Python 2.7 #############
import httplib, urllib, base64, json

body = {"url": "http://img.timeinc.net/time/daily/2010/1011/poy_nomination_agassi.jpg" }

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': "550bbc8cf88a4bb7bfb67c25407fc31f",
}

params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender',
})

try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v1.0/detect?%s" % params, json.dumps(body), headers)
    response = conn.getresponse()
    data = response.read()
    #json.dumps(data)
    #data2 = urllib.urlencode(data)
    print(data)
    conn.close()
except Exception as e:
    print("Error:", e)

####################################
takePicture.pri("hallo")

#print(data[0][0]["gender"])

# String to Manipulate: [{"faceRectangle":{"top":104,"left":73,"width":156,"height":156},"faceAttributes":{"gender":"male","age":44.0}}]













#import urllib2
## If you are using Python 3+, import urllib instead of urllib2

#import json 


#data =  {

#        "Inputs": {

#                "input1":
#                {
#                    "ColumnNames": ["Col1", "Col2", "Col3", "Col4", "Col5", "Col6", "Col7", "Col8", "Col9", "Col10", "Col11", "Col12", "Col13", "Col14", "Col15"],
#                    "Values": [ [ "0", "value", "0", "value", "0", "value", "value", "value", "value", "value", "0", "0", "0", "value", "value" ], [ "0", "value", "0", "value", "0", "value", "value", "value", "value", "value", "0", "0", "0", "value", "value" ], ]
#                },        },
#            "GlobalParameters": {
#}
#    }

#body = str.encode(json.dumps(data))

#url = 'https://ussouthcentral.services.azureml.net/workspaces/8e84ff258ed648f191ceb1700b317c6f/services/5c09fbc673294d12a8b998980594e304/execute?api-version=2.0&details=true'
#api_key = '8EzjM6DIW7weC5tvAkT7arGFXeDrO0fUQinppz6WKefc7YnBj4rCXwqm0iR7rU9mp58SVUupW86i9sv6bolYeg==' # Replace this with the API key for the web service
#headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

#req = urllib2.Request(url, body, headers)