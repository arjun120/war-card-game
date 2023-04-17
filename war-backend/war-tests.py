import json
import unittest
from flask_testing import TestCase
from app import app, db, User 

class FlaskAppTests(TestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['TESTING'] = True 
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_user(self):
        with self.client:
            response = self.client.post('/register', json={'name': 'Arjun'})
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['message'], 'User created successfully')

    def test_create_user_already_exists(self):
        with self.client:
            user = User(name='Arjun')
            db.session.add(user)
            db.session.commit()
            response = self.client.post('/register', json={'name': 'Arjun'})
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['message'], 'User already exists')

    def test_delete_user(self):
        with self.client:
            user = User(name='Arjun')
            db.session.add(user)
            db.session.commit()
            response = self.client.delete('/delete/Arjun')
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['message'], 'User deleted successfully')

    def test_delete_user_not_found(self):
        with self.client:
            response = self.client.delete('/delete/Arjun')
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['message'], "User doesn't exist")

    def test_get_all_users(self):
        with self.client:
            user1 = User(name='Arjun')
            user2 = User(name='Tanvi')
            db.session.add_all([user1, user2])
            db.session.commit()
            response = self.client.get('/users')
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data), 2)

    def test_play_same_players(self):
        with self.client:
            response = self.client.post('/play', json={'playerName1': 'Shreyas', 'playerName2': 'Shreyas'})
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertEqual(data['result'], -1)
            self.assertEqual(data['message'], "INVALID! Both the players can't be the same!")
            self.assertIsNone(data['logs'])

    def test_play_valid_players(self):
        with self.client:
            user = User(name='Shreyas')
            db.session.add(user)
            db.session.commit()
            user = User(name='Tanvi')
            db.session.add(user)
            db.session.commit()
            response = self.client.post('/play', json={'playerName1': 'Shreyas', 'playerName2': 'Tanvi'})
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertIn('result', data)
            self.assertIn('message', data)
            self.assertIn('logs', data)

if __name__ == '__main__':
    unittest.main()
