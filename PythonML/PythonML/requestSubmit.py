import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json 


data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["age", "sex", "income"],
                    "Values": [ [ "0", "value", "value" ], [ "30", "male", "null" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/2d0205f9eb5a43e697461e1439d678f0/services/b76245ddf84f4611baa647ce89154429/execute?api-version=2.0&details=true'
api_key = 'Pawe6fzpUyqAEN8QxCXvgYE06t0NH9rKcyIiIxYsfCvWgSoudrdZ/k2kRKqaSxiDChTELnRP83AlB97HMFnxTQ==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers) 

try:
    response = urllib2.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result) 
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))                 