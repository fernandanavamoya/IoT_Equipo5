# API
import os
from flask import Flask, request, send_file
from flask_restful import Resource, Api
from flask_cors import CORS
from twilio.rest import Client
import db_connector as db
import time

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

#cambiar las variables de configuración
account_sid = 'AC1015a54154c4676ab8207dac66b2b1a7' 
auth_token = '833fd2f3d2da783265e67f9d2505d489'

class MESSAGE(Resource):
    def post(self):
        req = request.json
        
        number = request.form['From']
        message_body = request.form['Body'].lower()    
        mensaje = ""
        
        client = Client(account_sid, auth_token) 

        if message_body.find("heart rate") == 0:
          db.create_img(number)
          mensaje = " "+db.find_user(number)+ " esta es la información actual de tus registros"          
          print(number)
          message = client.messages.create (
                                      from_='whatsapp:+14155238886',  
                                      body= mensaje,
                                      media_url=['http://1ed36b29d65d.ngrok.io/image?number='+number],
                                      to= number
                                  )
        else:        
          try:          
            mensaje = "Hola "+db.find_user(number)+ " puedes pedirme tu Heart Rate por el momento."
            message = client.messages.create (
                                    from_='whatsapp:+14155238886',  
                                    body= mensaje,                                  
                                    to= number
                                )                 

          except:
            mensaje = "No estas registrado. Escribe ->  Nombre:Ruben Raya  <- todo junto por favor"            
            message = client.messages.create (
                                    from_='whatsapp:+14155238886',  
                                    body= mensaje,                                  
                                    to= number
                                )                 
            

class IMAGE(Resource):
    def get(self):        
        number = request.args.get('number')
        number = number.replace(": ","_+")        
        print(number)
        filename = number+'.png'
        return send_file(filename, mimetype='image/png')

api.add_resource(MESSAGE, '/message')  # Route_1
api.add_resource(IMAGE, '/image')  # Route_2

if __name__ == '__main__':
    app.run(port='5013')
