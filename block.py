import time
class Block:

    def __init__(self):
        self.data={}
    
    def add_attr(self, key, value):
        self.data[key] = value

    def set_arrival_time(self):
        self.data['arrival_time'] = datetime.now().strftime("%B %d %Y, %H:%M")

    def set_dispatch_time(self):
        self.data['dispatch_time'] = datetime.now().strftime("%B %d %Y, %H:%M")