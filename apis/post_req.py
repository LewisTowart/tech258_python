import requests
import json

# Dumps turns the info into a string, dump would be a dict
json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 6EN", "EX165BL"]})
headers = {"Content-Type": "application/json"}

# could change data to json={"postcodes": ["PR3 0SG", "M45 6EN", "EX165BL"]}
post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)
print(post_multi_req.json())

# data = --> accepts a string (so we had to use json.dumps first)
# json = --> accepts a python dictionary
