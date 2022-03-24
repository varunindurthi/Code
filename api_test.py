# ----------------------------------------------------------------------
# Consume the webservice using API end points using "requests" library
#
# Steps to use requests module in python
# 1. Get scoring URI
# 2. Prepare the input data and create JSON
# 3. Prepare the headers with authorization key
# 4. Make a POST request to API using URI, headers and data
# 5. Collect the response and deserialize the JSON
# ----------------------------------------------------------------------

import requests
import json

# ------------------------------------------------------
# Set the URI for the web service
# ------------------------------------------------------
scoring_uri = 'http://20.85.144.48:80/api/v1/service/adultincome-service/score'


# ------------------------------------------------------
# Prepare the input data and create the serialized JSON
# ------------------------------------------------------
x_new = {"age":[46],
        "workclass":["Private"],
        "education":["Masters"],
        "marital status":["Married"],
        "race":["White"],
        "sex":["Male"],
        "hours_per_week":[60]}

# Convert the input data to a serialized JSON
json_data = json.dumps({"data": x_new})



# ---------------------------------------------------
# Create the headers with authorization key
# ---------------------------------------------------
key = 'Pi5yxpkEKl8cTWfRs4uxBFqtW2ceYsed'

# Set the content type and authorization
headers = {'Content-Type': 'application/json',
           'Authorization' : f'Bearer {key}'}


# ---------------------------------------------------
# Make the request using POST method and collect the response
# ---------------------------------------------------
response = requests.post(scoring_uri, json_data, headers=headers)
print(response)
predicted_classes = json.loads(response.json())

print('\n', predicted_classes)