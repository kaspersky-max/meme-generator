from flask import Flask, json, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/meme")
def get_meme():
    url = "https://meme-api.com/gimme"

    meme = json.loads(requests.request("GET", url).text)

    image = meme['preview'][-1]

    return jsonify(image), 201

if(__name__ == "__main__"):
    app.run(debug=True)