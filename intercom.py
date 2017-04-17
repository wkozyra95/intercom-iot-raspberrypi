
from gcm import *

def listen():
    while True:
        line = input("")

        send_notification()


def send_notification():

    gcm = GCM("AIzaSyBAVixFI3TstsRFvVwpalsWmWvyIj1urOs")
    data = {'the_message': 'You have x new friends', 'param2': 'value2'}

    reg_id = "DEVICE_REGISTRATION_TOKEN"
    gcm.plaintext_request(registration_id=reg_id, data=data)


