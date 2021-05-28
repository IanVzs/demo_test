#from flask_cors import CORS
import requests
from werkzeug.routing import BaseConverter
from flask import Flask, jsonify, abort, request, make_response, Blueprint

app = Flask(__name__, static_url_path='')
app.debug = True
app.use_debugger = False
app.use_reloader = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.url_map.strict_slashes = False
#CORS(app)

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app.url_map.converters['regex'] = RegexConverter

TESTAPI = Blueprint('testapi', __name__)

def send_req(url):
    requests.get(url).text


@app.route("/")
def main():
    response = requests.request('GET', 'http://127.0.0.1')
    return make_response(jsonify({'version': 'test_v0.01'}))

@app.route("/hello")
def hello():
    import requests
    requests.get("http://127.0.0.1:8979/")
    return make_response(jsonify({'hello': 'hello_flask'}))

@app.route("/dev-api/corpus/", methods=['GET', 'POST'])
def hi():
    import pdb; pdb.set_trace()
    import requests
    requests.get("http://127.0.0.1:8979/")
    return make_response(jsonify({'hello': 'hello_flask'}))

@TESTAPI.route('/testapi', methods=['GET', 'POST'])
def testapi():
    return make_response(jsonify({'data': 'testapi'}))

@TESTAPI.route('/favicon.ico', methods=['GET', 'POST'])
def favicon():
    return make_response(jsonify({'data': 'testapi2'}))
