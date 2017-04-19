
from pyfcm import FCMNotification
gcm_key = "AAAAyZ0c4Jc:APA91bHfS0tqve6u-GQ8Rh6Vfr0wU7Ufm3z7WbOhn6fdD4hERQUsbnoiDKzMZN7cGEgUmKwSYzvxXz7yfOY3ckaWW-pK9bTchmYC6gOKby3GobCJonnrLSzTb0ih3jX4eeYBdf0mwGA9"
push_service = FCMNotification(api_key=gcm_key)

# OR initialize with proxies


registration_id = "<device registration_id>"
message_title = "Uber update"
message_body = "Hi john, your customized news for today is ready"


def listen():
    while True:
        line = input("")

        send_notification()


def send_notification():
    reg_id = 'f-9txMAakpY:APA91bE0ZirUhL9zEO-fNZymsQZK_Ft-GA8bWQz4ZcpGymn7hCPb4oAxHBcDIz8HDz7YZ3JUILNkOszzm_HevEvaEK23HjmMUHIoOPa9Flqzai807cyVCmvu23yxdlVIza-6hmw32v86'
    data={'title': 'Someone is calling!', 'body': 'Click to show'}

    push_service.notify_single_device(registration_id=reg_id, message_title=data['title'], message_body=data['body'])



