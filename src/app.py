from flask import Flask, request
from flask_pymongo import PyMongo


app= Flask(__name__)

app.config['MONGO_URI']='mongodb://localhost/pythonmongodb'

mongo=PyMongo(app)

@app.route('/users', methods=['POST'])

def create_users():
    username= request.json['username']
    password= request.json['password']
    email=request.json['email']

    if username and email and password:
        mongo.db.users.insert(
            {'username':username, 'email':email, 'password': password}
        )
    else:
        {'message':'received'}
        
    return {'message':'received'}

if __name__ =="__main__":
    app.run(debug=True)