from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])


def receive_data():
    data = request.get_json()  # Flutter에서 보낸 JSON 데이터 가져오기
    print(data)
    return data

if __name__ == '__main__':
    app.run(debug=True)
