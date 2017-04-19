
from gcm import *

def listen():
    while True:
        line = input("")

        send_notification()


def send_notification():

    gcm = GCM("AAAAyZ0c4Jc:APA91bHfS0tqve6u-GQ8Rh6Vfr0wU7Ufm3z7WbOhn6fdD4hERQUsbnoiDKzMZN7cGEgUmKwSYzvxXz7yfOY3ckaWW-pK9bTchmYC6gOKby3GobCJonnrLSzTb0ih3jX4eeYBdf0mwGA9")
    gcm.plaintext_request(registration_id='f-9txMAakpY:APA91bE0ZirUhL9zEO-fNZymsQZK_Ft-GA8bWQz4ZcpGymn7hCPb4oAxHBcDIz8HDz7YZ3JUILNkOszzm_HevEvaEK23HjmMUHIoOPa9Flqzai807cyVCmvu23yxdlVIza-6hmw32v86', data={'title': 'Someone is calling!', 'body': 'wfrwfwe'})


