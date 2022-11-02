from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.e52hpkd.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/comments", methods=["POST"])
def comment_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    comment_list = list(db.comments.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'num':count,
        'name':name_receive,
        'comment':comment_receive,
        'like':0
    }

    db.comments.insert_one(doc)

    return jsonify({'msg': '작성 완료!'})

@app.route("/comments/num", methods=["POST"])
def comment_num():
    num_receive = request.form['num_give']
    db.comments.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})

@app.route("/comments/like", methods=["POST"])
def comment_like():
    like_receive = request.form['like_give']
    # db.comments.insert_one({'like': int(like_receive)})
    db.comments.update_one({'like': int(like_receive)}, {'$set': {'like': int(like_receive) + 1 }})
    return jsonify({'msg': '좋아요!'})

@app.route("/comments", methods=["GET"])
def comment_get():
    comment_list = list(db.comments.find({}, {'_id': False}))

    return jsonify({'cmts':comment_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
