import requests

def sms_api(number="6382871299"):
    

    msg = "Suspicious person have spotted at front of your Door."
    url = "https://www.fast2sms.com/dev/bulkV2"

    number = number

    payload = f"sender_id=TXTIND&message={msg}&route=v3&language=english&numbers={number}"

    headers = {
        "authorization":"01JSwljPWurXc8sBzAkv2MdtG9NEFZi736YyUTQLbKCHRfnhDaKV9FTygp6AJmrijqouZl75BYs4XH2n",
        "Content-Type":'application/x-www-form-urlencoded'
    }


    response = requests.request("POST", url=url,data=payload,headers=headers)

    return response.text

