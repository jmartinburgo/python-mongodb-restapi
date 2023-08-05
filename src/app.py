from flask import Flask, request
from flask_pymongo import PyMongo


app= Flask(__name__)

app.config['MONGO_URI']='mongodb://containers-us-west-156.railway.app 5573/pythonmongodb'

mongo=PyMongo(app)

@app.route('/users', methods=['POST'])

def create_users():
    #Recibiendo datos
    print(request.json)
    return {'message':'received'}

if __name__ =="__main__":
    app.run(debug=True)