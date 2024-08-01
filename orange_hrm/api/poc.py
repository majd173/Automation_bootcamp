import requests

url ="https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/employment-statuses?limit=0"



headers = {

        "authority": "opensource-demo.orangehrmlive.com",
        "method": "GET",
        "path": "/web/index.php/api/v2/admin/employment-statuses?limit=0",
        "scheme": "https",
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9,he-IL;q=0.8,he;q=0.7,ar;q=0.6",
        "cache-control": "no-store, no-cache, must-revalidate, post-check=0, pre-check=0",
        "cookie": "orangehrm=86f592601c5bbe8192f727d9efb99cfc",
        "priority": "u=1, i",
        "referer": "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"

}



body = {

        # "abraTests": "{\"AUTH_ssoGuardrailsFlow\":\"0_Control\",\"AUTH_new_regilite_flow\":\"1_Variant\",\"AUTH_FORGOT_PASS_LIRE\":\"1_Variant\",\"AUTH_B2B_SSO\":\"1_Variant\"}",
        # "auth_token": "H4sIAAAAAAAAA42QMW/DIBSE/8sbOtHEQGwwS6cO3btHz/BIUGyDgMSN0vz3KlaVrVLH090n3d0NsBSqYGDGSzhgDXF+HTADg0EMYDyOhRjYMdBcgwMDB5yoAAMXShrx+ozQVwqZChiuhGi57PSOQbqsjJDOCt72XjRcykYp2XZS27Yj3fVOKWCQCR3lj0d6VS5ksnV/zgEMHGtNxWy3y7Js5msNE5WNjdPW5ljKErMrb3iuxxUsKc6F9vWaCAzYGE+BgEHNJzA3wJTGYNeZD/fJA/v7iEyecqa8P+fx/2Ve4M6g4mc80fw8qeL7hGH81fdvp2kYvO8Fot+1vtfcItdWC+u9bKnprBJKOpLW887TzveyaX3H5dA3vVD6B8U2gMW/AQAA",
        # "form_view": "login",
        # "password": "majd123456789?",
        # "username": "majdb173@gmail.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
print(response.status_code)


