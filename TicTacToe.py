import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#connexion au bd cloud "firebase"
def open_data() :
    cred = credentials.Certificate("tic-tac-toe-89fbf-firebase-adminsdk-wlthj-c8636a7b06.json") #cle de bd cloud de 'firebase'
    firebase_admin.initialize_app(cred,{
        'databaseURL':'https://tic-tac-toe-89fbf-default-rtdb.europe-west1.firebasedatabase.app/' #lien de base de donnée
    })

open_data()

ref = db.reference('game/')
users_ref = ref.child('test1')
users_ref.update({
            'Start':"bruh",
             })

round='game/test'
ready = db.reference(round)
print(ready.get())