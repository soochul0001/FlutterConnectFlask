from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

app = Flask(__name__)

# Firebase Firestore 초기화
cred = credentials.Certificate("C:/Users/user/Desktop/flaskBindFlutter/flutter_application_1/fireCon/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
firebase_db = firestore.client()

@app.route("/add", methods=['GET'])
def start():
    with open('C:/Users/user/Desktop/flaskBindFlutter/flutter_application_1/fireCon/mydata.json', encoding='utf-8') as f:
        datas = json.load(f)

    # 아래는 테스트를 해보기 위한 데이터
    datas = [
        {
            'name': 'qewr',
            'code': '012345'
        },
        {
            'name': 'adsf',
            'code': '012341'
        }
    ]
    print(datas)

    for data in datas:
        # Add each data item to Firestore
        document = firebase_db.collection('qewr').document()
        document.set(data)
    return 'success'

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()  # Flutter에서 보낸 JSON 데이터 가져오기
    print(data)
    # Add the received data to Firestore
    document = firebase_db.collection('qewr').document()
    document.set(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
