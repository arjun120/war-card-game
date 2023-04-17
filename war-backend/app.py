from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from game import War
from sqlalchemy.sql.expression import func
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{uname}:{password}@{host}/users'.format(
    uname = os.environ["DB_USERNAME"], 
    password = os.environ["DB_PASSWORD"],
    host = os.environ["DB_HOST"]
    )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    """This class models the entity stored in the database. It has user information such that 
    the id, name and number of wins of each player is stored. It is a special class that is linked
    to the db instantiated above. 
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    wins = db.Column(db.Integer, nullable=False)

    def __init__(self, name):
        self.name = name
        self.wins = 0

with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def create_user():
    # This is a method to register a new user and store their details in the DB.
    if request.method == 'POST':
        user_name = request.json['name']
        if len(user_name) == 0:
            return jsonify({'message': 'User name cannot be empty'})
        user = User.query.filter(func.binary(User.name) == user_name).first()
        if user:
            return jsonify({'message': 'User already exists'})
        else:
            new_user = User(name=user_name)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message': 'User created successfully'})
        
@app.route('/delete/<string:user_name>', methods=['DELETE'])
def delete_user(user_name):
    # This is a method to delete details of a given user from the db.
    if request.method == 'DELETE':
        user = User.query.filter(func.binary(User.name) == user_name).first()
        if user:
            User.query.filter(func.binary(User.name) == user_name).delete()
            db.session.commit()
            return jsonify({'message': 'User deleted successfully'})
        else:
            return jsonify({'message': 'User doesn\'t exist'})

@app.route('/users', methods=['GET'])
def get_all_users():
    # This is a method used to retrieve all the users part of the db.
    if request.method == 'GET':
        users = User.query.all()
        user_list = []
        for user in users:
            user_data = {'id': user.id, 'name': user.name}
            user_list.append(user_data)
        return jsonify(user_list)
    
@app.route('/play', methods=['POST'])
def play():
    # This is a method to simulate the game of war played between two players.
    if request.method == 'POST':
        first_player = request.json['playerName1']
        second_player = request.json['playerName2']

        player1 = User.query.filter(func.binary(User.name) == first_player).first()
        player2 = User.query.filter(func.binary(User.name) == second_player).first()

        if player1 == None or player2 == None:
            return jsonify({'result': -1, 'message': "INVALID! Both the players need to be registered to play!", 'logs': None})


        if first_player == second_player:
            return jsonify({'result': -1, 'message': "INVALID! Both the players can't be the same!", 'logs': None})


        war = War()
        logs, (ressultString, result) = war.simulate(first_player, second_player)
        if result == -1:
            return jsonify({'result': 0, 'message': "The game resulted in a draw", 'logs': logs})
        currentWins = User.query.filter(func.binary(User.name) == (second_player if result else first_player)).first().wins
        User.query.filter(func.binary(User.name) == (second_player if result else first_player)).update(dict(wins = currentWins + 1))
        db.session.commit()
        return jsonify({'result': 0, 'message': ressultString, 'logs': logs})

@app.route('/wins/users/<string:user_name>', methods=['GET'])
def get_user_wins(user_name):
    # This is a method to list user details for a particular user with their respective counts for wins.
    if request.method == 'GET':
        user = User.query.filter(func.binary(User.name) == user_name).first()
        if user:
            user_data = {'id': user.id, 'name': user.name, 'wins': user.wins}
            return jsonify(user_data)
        else:
            return jsonify({'message': 'There are no such users'})

@app.route('/wins/users', methods=['GET'])
def get_all_users_wins():
    # This is a method to list user details for all users with their respective counts for wins. 
    if request.method == 'GET':
        users = User.query.all()
        user_list = []
        for user in users:
            user_data = {'id': user.id, 'name': user.name, 'wins': user.wins}
            user_list.append(user_data)
        return jsonify(user_list)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)