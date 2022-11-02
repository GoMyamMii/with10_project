from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.tlxtldo.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cs')
def cs():
    return render_template('cs.html')

@app.route('/hn')
def hn():
    return render_template('hanul.html')

@app.route('/hh')
def hh():
    return render_template('heehyeon.html')

@app.route('/js')
def js():
    return render_template('JS.html')

@app.route('/ng')
def ng():
    return render_template('kng.html')


@app.route("/comments", methods=["POST"])
def comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    comment_list = list(db.comments.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'name':name_receive,
        'comment':comment_receive,
        'numb':count,
        'good':0
    }
    db.comments.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})


@app.route("/comment", methods = ["GET"])
def comment_get() :
    comment_list = list(db.comment.find({}, {'_id': False}))
    return jsonify({'comments' : comment_list})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)