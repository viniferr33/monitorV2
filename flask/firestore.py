import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

"""
A class to handle FireStore operations
"""

cred = credentials.Certificate('data/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def addWarning(location, wtype, title, text, date):
    ### A method to add documents to warning collection of FireStore ###

    doc_ref = db.collection(u'warnings').document(
        location).collection(wtype)
    doc_ref.add({
        u'title': title,
        u'text': text,
        u'date': date
    })


if __name__ == "__main__":

    wtype = 'news'
    location = 'Wanel Ville'
    title = 'News3'
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus metus dolor, placerat vel tortor quis, efficitur lobortis purus. Maecenas convallis nibh velit, ac tincidunt neque posuere vitae."
    date = '2020-10-05'

    addWarning(location, wtype, title, text, date)
