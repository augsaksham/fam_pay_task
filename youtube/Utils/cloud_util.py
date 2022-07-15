import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
databaseURL='https://youtubesearch-356406-default-rtdb.firebaseio.com/'
cred = credentials.Certificate("youtube\\Utils\\youtubesearch-356406-firebase-adminsdk-i3koy-976a3ded84.json")
default_app = firebase_admin.initialize_app(cred, {
	'databaseURL':databaseURL
	})
ref = db.reference("/")

def write(dict_val):
    for key in dict_val.keys():
        print("key is ",key)
        print("recieved ",dict_val[key])
        ref.child('video').push().set(dict_val[key])
    print('written')

def get_data():
    ref = db.reference("/")
    res=ref.child('video').get()
    return res