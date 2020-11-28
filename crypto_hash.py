import hashlib
import json

def crypto_hash(block):
    """
    returns sha-256 hash of data
    """

    block_data = [block.arrival_time, block.dispatch_time, block.last_hash, block.data]

    data_string = sorted(map(lambda data: json.dumps(data), block_data))
    joined_data = ''.join(data_string)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()
    

def main():
    pass

if __name__ == "__main__":
    main()

