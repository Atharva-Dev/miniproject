from backend.blockchain.block import Block, genesis
from backend.utils.crypto_hash import crypto_hash

class Blockchain:
    """
    Blockchain class holds list of blocks and operations
    """

    def __init__(self):
        self.chain = [genesis()]
    
    def add_block(self, block):
        block.last_hash = self.chain[-1].hash
        block.hash = crypto_hash(block)
        self.chain.append(block)

    def __repr__(self):
        return "\n".join(list(map(str,self.chain)))



def main():
    b = Block()
    b.add_attr('quality', 100)
    b.set_arrival_time()
    b.set_dispatch_time()
    ch = Blockchain()
    ch.add_block(b)
    print(ch)





if __name__ == "__main__":
    main()
    