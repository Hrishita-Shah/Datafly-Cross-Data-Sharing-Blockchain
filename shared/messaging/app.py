from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to DataFly Messaging API"

@app.route("/favicon.ico")
def favicon():
    return "", 204

@app.route("/queryAll")
def query_all():
    cmd = [
        "peer", "chaincode", "query",
        "-C", "mychannel", "-n", "datafly",
        "-c", '{"Args":["queryAllData"]}'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return jsonify({"result": result.stdout.strip()})


@app.route("/query/<key>")
def query_data(key):
    cmd = [
        "peer", "chaincode", "query",
        "-C", "mychannel", "-n", "datafly",
        "-c", f'{{"Args":["queryData", "{key}"]}}'
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        return jsonify({
            "error": "Chaincode query failed",
            "details": result.stderr.strip()
        }), 500

    return jsonify({
        "result": result.stdout.strip()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
