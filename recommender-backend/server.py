from flask import Flask
import json
from core import getRecommendedItems


app = Flask(__name__)

@app.route("/predict/<int:uid>")
def predict(uid):
    return json.dumps(getRecommendedItems(uid), indent=2)

if __name__=='__main__':
    app.run(debug=True)
