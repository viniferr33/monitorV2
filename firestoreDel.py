import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

if __name__ == "__main__":

    wtype = input("Digite o tipo: [news, warning, emergency] \n")
    location = input("Digite a localização: \n")
    docId = 'mvqX3J6wGaHRbtwfXSBB' 
    
    db.collection(u'warnings').document(wtype).collection(location).document(docId).delete()
 
