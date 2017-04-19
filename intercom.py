
from gcm import *

def listen():
    while True:
        line = input("")

        send_notification()


def send_notification():

    gcm = GCM("AAAAarr-B5Q:APA91bECRbwFs-raUrOYzFlQ-7Wb5Hk6IdDL3ZYVMzeyNIf2K6dCL9rimTXBTaGlJ1GNpXgFy5Kvfi6CxvXWvLagounBvczpBMbAj6z_gw4Vyy3DxZ4PTsbQfQiHbmnu1FIsHC4ssPDU")
    gcm.send_topic_message(topic='INTERCOM', data={'message': 'Someone is calling!'})


