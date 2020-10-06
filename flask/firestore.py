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

    def addWarning(self, location, wtype, title, text, date):
        ### A method to add documents to warning collection of FireStore ###
        db = self.db
        doc_ref = db.collection(u'warnings').document(
            location).collection(wtype)
        doc_ref.add({
            u'title': title,
            u'text': text,
            u'date': date
        })

    def filterData(self, collection, location, wtype, date):
        ### A method to get data from FireStore ###
        db = self.db
        doc_ref = db.collection(collection).document(
            location).collection(wtype)

        stream = doc_ref.where('date', '==', date).stream()
        docs = {}

        for doc in stream:
            docs[doc.id] = doc.to_dict()

        return docs


if __name__ == "__main__":

    wtype = 'news'
    location = 'Wanel Ville'
    title = 'News10'
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus metus dolor, placerat vel tortor quis, efficitur lobortis purus. Maecenas convallis nibh velit, ac tincidunt neque posuere vitae."
    date = '2020-10-05'

    fs = FSHandler()
    #fs.addWarning(location, wtype, title, text, date)

    docs = fs.filterData('warnings', location, wtype, date)
    pprint.pprint(docs)