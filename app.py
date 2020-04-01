from flask import Flask, render_template,request,jsonify
from bot import main
import json
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    title = "成長AI prodang"

    return render_template('index.html', title=title)

@app.route('/postText', methods=['POST'])
def lower_conversion():
    m = request.json['m']
    txt = request.json['txt']
    if m == "say":
        ret = {'result':main.make_reply(txt)}
        
        return jsonify(ResultSet=json.dumps(ret))
    return_data = {"error": "error?"}
    return jsonify(return_data = {"result":lower_text})
  
if __name__ == '__main__':
    app.debug = False
    app.run()
