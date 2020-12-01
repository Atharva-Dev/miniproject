from datetime import datetime
from backend.utils.crypto_hash import crypto_hash

def genesis():
    """
    Generate The Genesis block
    """
    genesis_block = Block()
    genesis_block.arrival_time = 0
    genesis_block.dispatch_time = 0
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
        self.arrival_time = None
        self.dispatch_time = None
    
    def add_attr(self, key, value):
        self.data[key] = value

    def set_arrival_time(self):
        self.arrival_time = datetime.now().strftime("%B %d %Y, %H:%M")

    def set_dispatch_time(self):
        self.dispatch_time = datetime.now().strftime("%B %d %Y, %H:%M")

    def to_json(self):
        return self.__dict__

    def __repr__(self):
        return (
            'Block('
            f'data: {self.data}, '
            f'arrival_time: {self.arrival_time}, '
            f'dispatch_time: {self.dispatch_time}, '
            f'hash: {self.hash}, '
            f'last_hash: {self.last_hash} )'
        )
    
    def __eq__(self, other):
        return self.__dict__==other.__dict__

    @staticmethod
    def is_valid_block(last_block, block):

        try:
            if block.last_hash != last_block.hash:
                raise Exception('The block last_hash is incorect')
            if block.hash != crypto_hash(block):
                raise Exception('The block hash is incorrect')
        except Exception as e:
            raise Exception(f'inside is_valid_block: {e}')

    @staticmethod
    def to_block(data):
        block = Block()
        block.data = data['data']
        block.arrival_time = data['arrival_time']
        block.dispatch_time = data['dispatch_time']
        block.last_hash = data['last_hash']
        block.hash = data['hash']
        return block


def main():
    g = genesis()
    new = Block()
    new.last_hash = g.hash
    new.set_arrival_time()
    new.set_dispatch_time()
    new.add_attr('quantity', 10)
    new.hash = crypto_hash(new)
    Block.is_valid_block(g, new)

if __name__ == "__main__":
    main()