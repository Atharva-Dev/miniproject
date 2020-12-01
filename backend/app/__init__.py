import os
import requests
import random

from flask import Flask, jsonify

from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import Block
from backend.pubsub import PubSub



app = Flask(__name__)
blockchain = Blockchain()
pubsub =PubSub(blockchain)



@app.route('/')
def default(): 
    return jsonify(blockchain.to_json())

@app.route('/addblock')
def addblock():
    block = Block()
    block.set_arrival_time()
    block.set_dispatch_time()
    blockchain.add_block(block)

    pubsub.broadcast_block(block)

    return jsonify(blockchain.to_json())

PORT = 5000

if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)

    result = requests.get('http://localhost:5000/')
    
    result_blockchain = Blockchain.from_json(result.json())

    try:
        blockchain.replace_chain(result_blockchain.chain)
        print('\n--Replaced blockchain successfully')
    except Exception as e:
        print(f'\n--Error while synchronizing : {e}')

app.run(port=PORT)