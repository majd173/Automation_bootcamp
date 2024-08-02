import requests
import json

url = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/employees/7/personal-details"

payload = json.dumps({
  "birthday": None,
  "drivingLicenseExpiredDate": None,
  "drivingLicenseNo": "",
  "employeeId": None,
  "firstName": "positive",
  "gender": "2",
  "lastName": "man",
  "maritalStatus": "Single",
  "middleName": "smile",
  "nationalityId": 4,
  "otherId": ""
})
headers = {
  "Cookie": "orangehrm=c20d25400b985792fb8bb7647ebc06f5; orangehrm=e3370b205a74be52b3f31a26f502f0f1",
  "Content-Type": "application/json"
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.status_code)
