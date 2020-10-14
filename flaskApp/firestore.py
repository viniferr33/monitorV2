import pprint
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class FSHandler():
    """
    A class to handle FireStore operations
    """

    cred = credentials.Certificate('data/serviceAccountKey.json')
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    def addWarning(self, location, wtype, title, text, date, exp_date, ext_link=None):
        ### A method to add documents to warning collection of FireStore ###
        db = self.db
        doc_ref = db.collection(wtype)
        
        if(ext_link == None):
            doc_ref.add({
                u'location': location,
                u'title': title,
                u'text': text,
                u'date': date,
                u'exp_date': exp_date,
                u'timestamp': firestore.SERVER_TIMESTAMP
            })

        else:
            doc_ref.add({
                u'location': location,
                u'title': title,
                u'text': text,
                u'date': date,
                u'exp_date': exp_date,
                u'ext_link': ext_link,
                u'timestamp': firestore.SERVER_TIMESTAMP

            })
    
    def addUser(self, email, password, name):
        ### A method to add a new user to Users collection of FireStore ###
        db = self.db
        doc_ref = db.collection('users')

        doc_ref.add({
            'email': email,
            'password': password,
            'name': name
        })

    def checkUser(self, email):
        ### A method to check if user email is already used ###
        db = self.db
        doc_ref = db.collection('users')
        stream = doc_ref.where('email', '==', email).stream()
        
        if stream:
            return True

        else: 
            return False

    def logUser(self, email, password):
        ### A method to authenticate the password ###
        db = self.db
        doc_ref = db.collection('users')
        stream = doc_ref.where('email', '==', email).stream()

        for doc in stream:
            data_id = doc.id

        if self.checkUser(email):
            doc_ref = db.collection('users').document(data_id)
            doc = doc_ref.get()
            data = doc.to_dict()

            if password == data['password']:
                return True
        
        return False
        

    def filterData(self, location, wtype, date):
        ### A method to get data from FireStore ###
        db = self.db
        doc_ref = db.collection(wtype)

        stream = doc_ref.where('date', '==', date).where(
            'location', '==', location).stream()
        docs = {}

        for doc in stream:
            docs[doc.id] = doc.to_dict()

        return docs

    def getAll(self, collection):
        ### A method to retrieve all documents of any collection from FireStore ###
        db = self.db
        doc_ref = db.collection(collection)
        stream = doc_ref.stream()
        docs = {}

        for doc in stream:
            docs[doc.id] = doc.to_dict()

        return docs

    def deleteData(self, wtype, docId):
        ### A method to delete data from FireStore ###
        db = self.db
        db.collection(wtype).document(docId).delete()


if __name__ == "__main__":

    
    fs = FSHandler()


    
