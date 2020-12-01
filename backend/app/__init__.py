import os
import random
from flask import Flask, jsonify
from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import Block
from backend.pubsub import PubSub



app = Flask(__name__)
chain = Blockchain()
pubsub =PubSub(chain)



@app.route('/')
def default(): 
    return jsonify(chain.to_json())

@app.route('/addblock')
def addblock():
    block = Block()
    block.set_arrival_time()
    block.set_dispatch_time()
    chain.add_block(block)

    pubsub.broadcast_block(block)

    return jsonify(chain.to_json())

PORT = 5000

if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)

app.run(port=PORT)