from flask import Flask
from flask_sock import Sock
from dotenv import load_dotenv

app = Flask(__name__)
sock = Sock(app)

@sock.route('/websocket')
def websocket(ws):
    while True:
        text = ws.receive()
        # ws.send(text[::-1])
        if text == "Hi":
            text = "Hello!, How are you?"
        elif text == "How are you?":
            text = "I'm Running Healthy, Thanks. How are you?"
        elif text == "Fine":
            text = "Great."
        elif text == "Hello":
            text = "Hi.., How are you?"
        elif text == "Thanks":
            text = "Welcome...."
        ws.send(text)

