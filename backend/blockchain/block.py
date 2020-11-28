from datetime import datetime
from backend.utils.crypto_hash import crypto_hash

def genesis():
    """
    Generate The Genesis block
    """
    genesis_block = Block()
    genesis_block.set_arrival_time()
    genesis_block.set_dispatch_time()
    genesis_block.last_hash = 'last_hash'
    genesis_block.hash = crypto_hash(genesis_block)
    return genesis_block



class Block:
   

    def __init__(self):
        """
        Creates an Empty Block
        """
        self.data={}
        self.last_hash = None
        self.hash = None
    
    def add_attr(self, key, value):
        self.data[key] = value

    def set_arrival_time(self):
        self.arrival_time = datetime.now().strftime("%B %d %Y, %H:%M")

    def set_dispatch_time(self):
        self.dispatch_time = datetime.now().strftime("%B %d %Y, %H:%M")

    def __repr__(self):
        return (
            'Block('
            f'data: {self.data}, '
            f'arrival_time: {self.arrival_time}, '
            f'dispatch_time: {self.dispatch_time}, '
            f'hash: {self.hash}, '
            f'last_hash: {self.last_hash} )'
        )




def main():
    print(genesis())

if __name__ == "__main__":
    main()