import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

if __name__ == "__main__":
    doc_ref = db.collection('news')
    docs = doc_ref.stream()

    for doc in docs:
        print("{} => {}".format(doc.id, doc.to_dict()))