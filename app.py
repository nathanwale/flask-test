from crypt import methods
from urllib import response
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    name = request.args.get('name', None)
    print(f"Got name: {name}")
    response = {}

    if not name:
        response['ERROR'] = "No name found"
    elif str(name).isdigit():
        response['ERROR'] = f'Name cannot be numeric. Name used: "{name}"'
    else:
        response['MESSAGE'] = f"Welcome, <b>{name}</b>, to the site!"
    return jsonify(response)


@app.route('/post/', methods=['POST'])
def post_something():
    name = request.form.get('name')
    print(name)
    data = {"name": name}
    if name:
        data.update({
            "Message": f"Welcome {name}, to our server!",
            "METHOD": "POST"
        })
    else:
        data.update({
            "ERROR": "No name posted" 
        })
    return jsonify(data)
    
@app.route('/')
def index():
    return "<h1>Test success!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=8080)