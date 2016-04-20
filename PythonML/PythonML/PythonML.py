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
import httplib, urllib, base64, json, csv, array
import numpy

body = {"url": "http://img.timeinc.net/time/daily/2010/1011/poy_nomination_agassi.jpg" }

#glasses
body2 = [
{"url":"http://culturescapes.com/App_Themes/Classic/images/Choices_we_face.jpg"},
{"url":"http://www.teaparty.org/wp-content/uploads/2014/10/Delay_Tom_Face_jpg_800x1000_q100.jpg"},
{"url":"https://upload.wikimedia.org/wikipedia/commons/a/ab/John_Dillinger_mug_shot.jpg"},
{"url":"http://i4.mirror.co.uk/incoming/article6977109.ece/ALTERNATES/s615b/Mark-Hamill.jpg"},
{"url":"http://images.klettern.de/sixcms/media.php/6/thumbnails/Alexander-Megos-Damiano-Levati-Kalymnos-13970querformat.jpg.3365235.jpg"},
{"url":"https://pbs.twimg.com/media/CehcXs_WAAA7BSi.jpg"},
{"url":"http://www.tobiaskocht.com/wp-content/uploads/2014/05/Face.jpg"},
{"url":"https://patcegan.files.wordpress.com/2011/12/old-man-face.jpg"},
{"url":"https://pbs.twimg.com/media/CQWvpZKUsAEOIP3.jpg"},
{"url":"http://i.dailymail.co.uk/i/pix/2016/03/09/19/320986CE00000578-3484459-image-m-30_1457551014294.jpg"},
{"url":"https://www.johndenugent.com/images/Gary_McKinnon_pensive-hand-face.jpg"},
{"url":"http://www.wtae.com/image/view/-/39097200/medRes/2/-/h/252/maxh/92/maxw/138/w/378/-/usfn7x/-/Face-Transplant-1-jpg.jpg"},
{"url":"http://www.photoawards.com/wp-content/uploads/ville-face.jpg"},
{"url":"http://www.photocase.com/stock-photos/187296-stock-photo-human-being-portrait-photograph-youth-young-adults-man-young-man-face.jpg"},
{"url":"http://images.magi-mania.de/img/NARS-Hanamichi-Eyeshadow-Palette-Makeup-Face.jpg"},
{"url":"https://i.guim.co.uk/img/media/0cea6466227af4aa426134699b09c104e2b31dfb/0_562_2832_1699/master/2832.jpg?w=620&q=55&auto=format&usm=12&fit=max&s=c5c8a867e25029d4535842769fccc6ff"},
{"url":"http://neukreativhaar.com/wp-content/uploads/2016/02/Short-Hair-for-Oval-Round-Faces.jpg"}]

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': "550bbc8cf88a4bb7bfb67c25407fc31f",
}

params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,glasses',
})

newItem = []

for a in body2:
    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/face/v1.0/detect?%s" % params, json.dumps(a), headers)
        response = conn.getresponse()
        data = response.read()
        #data2 = urllib.urlencode(data)
        print(data+"\n")
        conn.close()
        parsed = json.loads(data)
        c= (str(parsed[0]["faceAttributes"]["age"]))
        d = (parsed[0]["faceAttributes"]["gender"])
        f = (parsed[0]["faceAttributes"]["glasses"])
        newItem.append(c+",")
        newItem.append(d+",")
        newItem.append(f+"\n")
        print(c,d,f)
    except Exception as e:
        print("Error:", e)

for b in newItem:
    print(b)

#numpy.savetxt("foo.csv", b, delimiter=",")


        #### first try ####
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': "550bbc8cf88a4bb7bfb67c25407fc31f",
}

params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,glasses',
})


####### First try #####
try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v1.0/detect?%s" % params, json.dumps(body), headers)
    response = conn.getresponse()
    data = response.read()
    #data2 = urllib.urlencode(data)
    print(data+"\n")
    conn.close()
    parsed = json.loads(data)
    print(parsed[0]["faceAttributes"]["age"])
    print(parsed[0]["faceAttributes"]["gender"])
    print(parsed[0]["faceAttributes"]["glasses"])
except Exception as e:
    print("Error:", e)


###parsed = json.loads(data)

###print(parsed)
#######################################
###takePicture.pri("hallo")

###print(parsed[0]["faceAttributes"]["age"])
###print(parsed[0]["faceAttributes"]["gender"])
###print(parsed[0]["faceAttributes"]["glasses"])



# String to Manipulate: [{"faceRectangle":{"top":104,"left":73,"width":156,"height":156},"faceAttributes":{"gender":"male","age":44.0}}]
# glasses: glasses type. Possible values are 'noGlasses', 'readingGlasses', 'sunglasses', 'swimmingGoggles'. 











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