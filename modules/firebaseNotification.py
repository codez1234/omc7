# Install request module by running ->
#  pip3 install requests

# Replace the deviceToken key with the device Token for which you want to send push notification.
# Replace serverToken key with your serverKey from Firebase Console


import requests
import json
from configuration.notification import notification_data
'''
# serverToken = 'your server key here'
serverToken = "AAAAVcEhGL4:APA91bEK5cDgHWZen9iGZRnSqG9r0j9MEvw2uN_Nkvt3LMRgevpWLwe2d-f5CiEUHSJzqiyIEKwsUKZLMKJvVnwbupJn2ESnUzg_f7RA3qGvquyfn6NuGYJARMfk5FxSHCtUq5Xxry6k"
# deviceToken = 'device token here'
# deviceToken came from devices.

deviceToken = "dljDR4k5QT6QX6FPSJvFzY:APA91bH51ALZyA1H7U6pIWBgQqHIhwZDj1fY4X58h56JIR7FPRJoIrXcOgn-vJz0n-LNEiW2EAkJWyXzpWjOsHV6DVu3COR1XKJ2SdgIJm80CQS-g_W1FhTniEHt7P_S_ufthYqvPFUf"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'key=' + serverToken,
}

body = {
    'notification': {'title': 'Sending push form python script',
                     'body': 'hello world'
                     },
    'to':
    deviceToken,
    'priority': 'high',
    #   'data': dataPayLoad,
}
response = requests.post(
    "https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))
print(response.status_code)

print(response.json())
'''


def send_notification(deviceToken=None, title=None, body=None):
    serverToken = notification_data.get("serverToken")
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + serverToken,
    }
    body = {
        'notification': {'title': title,
                         'body': body,
                         },
        'to':
        deviceToken,
        'priority': 'high',
        #   'data': dataPayLoad,
    }
    response = requests.post(
        "https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))

    return response


# send_notification(deviceToken="cjEEGC0ESr659Q5LivgXCS:APA91bHnzKDDkhp7bMOYHZdu_sSsnhCZ1BR_MXlwMbvkktXM7BDajSpnLMgm8BjB8PW9cxYP2OdGOrXTIt87JJEKrkMP283ahEe5I_Poz2AtT_Z7fza_BNZOa5nGDl5Vgw9Y4xjAEdYP", title="checkin", body=None)
