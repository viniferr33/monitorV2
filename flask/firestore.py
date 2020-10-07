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

    def addWarning(self, location, wtype, title, text, date, exp_date):
        ### A method to add documents to warning collection of FireStore ###
        db = self.db
        doc_ref = db.collection(wtype)
        doc_ref.add({
            u'location': location,
            u'title': title,
            u'text': text,
            u'date': date,
            u'exp_date': exp_date,
            u'timestamp': firestore.SERVER_TIMESTAMP
        })

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

    def deleteData(self, collection, location, wtype, docId):
        ### A method to delete data from FireStore ###
        db = self.db
        db.collection(collection).document(
            location).collection(wtype).document(docId).delete()


if __name__ == "__main__":

    wtype = 'news'
    location = 'Wanel Ville'
    title = 'News6'
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus metus dolor, placerat vel tortor quis, efficitur lobortis purus. Maecenas convallis nibh velit, ac tincidunt neque posuere vitae."
    date = '2020-10-05'
    exp_date = '2020-10-15'

    fs = FSHandler()
    fs.addWarning(location, wtype, title, text, date, exp_date)

    docs = fs.getAll('news')

    for doc in docs:
        print(doc)
        print(docs[doc]['title'])
