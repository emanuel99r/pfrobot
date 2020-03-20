from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import time
import socketio

app = Flask(__name__)
app.config['SECRET KEY']='secret'
socketio= SocketIO(app)

@app.route('/',methods=['POST','GET'])
def index():
   return render_template('index2.html')
     
@socketio.on('message')
def another_event(data):
    print('LOS DATOS SON', data)
    emit('message',data,broadcast=True)

@socketio.on('enviarGrados')       
def grados(msg):
    print('el mensaje es', msg)
    emit('grados',msg,broadcast=True)

@socketio.on('posicionHome')       
def home():
    print('llegando a home')
    emit('home','home',broadcast=True)

if __name__=='__main__':
    socketio.run()

    
