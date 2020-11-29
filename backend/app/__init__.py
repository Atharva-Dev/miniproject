from flask import Flask, jsonify
from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)
@app.route('/')
def default():
    chain = Blockchain()
    return jsonify(chain.to_json())


app.run()