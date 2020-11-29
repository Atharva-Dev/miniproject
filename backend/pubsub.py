import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-ec69896a-321e-11eb-9d95-7ab25c099cb1'
pnconfig.publish_key = 'pub-c-c70ece11-d1b1-4c3c-a6a3-94f2147b503b'


TEST_CHENNAL = "TEST_CHENNAL"



class Listener(SubscribeCallback):
    def message(self, pubnub, message_obj):
        print(f'\nChannel:{message_obj.channel}\nMessage: {message_obj.message}')


class PubSub():
    """
    Handles publish/subscribe layer in application
    provides communication between blockchain networks 
    """

    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHENNAL]).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        self.pubnub.publish().channel(channel).message(message).sync()





def main():
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publish(TEST_CHENNAL, "hi")
    

if __name__ == "__main__":
    main()