import sys
sys.path.append('..')

import time

import pusherclient

def print_usage(filename):
    print "Usage: python %s <appkey> <secret>" % filename

def channel_callback(data):
    print "Channel Callback: %s" % data

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print_usage(sys.argv[0])
        sys.exit(1)

    appkey = sys.argv[1]
    secret = sys.argv[2]

    pusher = pusherclient.Pusher(appkey, secret=secret)

    pusher.wait_until_connected()

    channel = pusher.subscribe("private-channel")

    channel.bind('my_event', channel_callback)

    while True:
        time.sleep(1)