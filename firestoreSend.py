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
    title = input("Digite o Titulo de exibição: \n")
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus metus dolor, placerat vel tortor quis, efficitur lobortis purus. Maecenas convallis nibh velit, ac tincidunt neque posuere vitae."
    print("Your text is: " + text)
    date = input("Digite a data: YYYY-MM-DD: \n")

    doc_ref = db.collection(u'warnings').document(wtype).collection(location)
    doc_ref.add({
        u'title': title,
        u'text': text,
        u'date': date
    })


