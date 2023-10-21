import requests

def sms_api(number="6382871***"):
    

    msg = "Suspicious person have spotted at front of your Door."
    url = "https://www.fast2sms.com/dev/bulkV2"

    number = number

    payload = f"sender_id=TXTIND&message={msg}&route=v3&language=english&numbers={number}"

    headers = {
        "authorization":"api-key",
        "Content-Type":'application/x-www-form-urlencoded'
    }


    response = requests.request("POST", url=url,data=payload,headers=headers)

    return response.text

