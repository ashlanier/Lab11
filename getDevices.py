import requests
import json
from getpass import getpass
from requests.auth import HTTPBasicAuth

username = input("Please enter your username: ")
password = getpass("Please enter your password: ")

BASEURL = "https://sandboxdnac.cisco.com"
authAPI = "/dna/system/api/v1/auth/token"

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

dnaAuth = BASEURL + authAPI

response = requests.post(dnaAuth, auth=HTTPBasicAuth(username, password), headers=headers, data=payload)

tokenJSON = response.json()

TOKEN = tokenJSON['Token']

print("Your token was successfully generated. Your token value is: " + TOKEN)
