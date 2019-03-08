from flask import Flask, jsonify, request, redirect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from models import *

app = Flask(__name__)
# Exercise 6
limiter = Limiter(app, key_func=get_remote_address)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wg_forge:42a@localhost:5432/wg_forge_db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
db.init_app(app)


@app.errorhandler(429)
def too_many_requests(e):
    return "429 Too Many Requests\n", 429


# Exercise 3
@app.route('/ping', methods=['GET'])
@limiter.limit("600/minute")
def ping():
    return jsonify('Cats Service. Version 0.1 \n')


# Exercise 4
@app.route('/cats', methods=['GET'])
@limiter.limit("600/minute")
def cats():
    attribute = request.args.get('attribute', type=str)
    order = request.args.get('order', type=str)
    offset = request.args.get('offset', default=0, type=int)
    if offset < 0:
        return jsonify({"error": "offset can't be negative"}), 400
    limit = request.args.get('limit', default=None, type=int)
    if isinstance(limit, int) and limit <= 0:
        return jsonify({"error": "limit can't be negative or zero"}), 400
    dict_order = {"asc": False, "desc": True}
    json_list = []

    data = Cats.query.offset(offset).limit(limit).all()
    for one_cat in data:
        json_list.append(
            {"name": one_cat.name,
             "color": one_cat.color,
             "tail_length": one_cat.tail_length,
             "whiskers_length": one_cat.whiskers_length
             })
    if attribute:
        if order in dict_order.keys():
            try:
                json_list.sort(key=lambda column: column[attribute], reverse=dict_order[order])
            except KeyError:
                return jsonify({"error": "invalid attribute"}), 400
        else:
            return jsonify({"error": "invalid order"}), 400
    if json_list:
        return jsonify(json_list)
    else:
        return jsonify({'error': "offset can't be bigger than database"}), 400


# Exercise 5
@app.route('/cat', methods=['POST', 'GET'])
@limiter.limit("600/minute")
def cat():
    if request.method == 'GET':
        return redirect("/cats", code=302)
    try:
        reader = request.get_json(force=True)
        new_cat = Cats(**reader)
        name, color, tail_length, whiskers_length = new_cat.name, new_cat.color, new_cat.tail_length, new_cat.whiskers_length
    except:
        return jsonify({"error": "data should be json format"}), 400
    try:
        check_name = Cats.query.get(name)
        if not isinstance(name, str) or name.capitalize() != name:
            return jsonify({"error": "invalid name type or format"}), 400
    except:
        return jsonify({"error": "invalid name type or format"}), 400
    color_list = ('black','white','black & white','red','red & white','red & black & white')
    if color not in color_list:
        return jsonify({"error": "this color is not allowed"}), 400
    if check_name:
        return jsonify({"error": "this name already exists"}), 400
    try:
        if tail_length < 0 or whiskers_length < 0:
            return jsonify({"error": "integers should be positive"}), 400
    except:
        return jsonify({"error": "tail_length, whiskers_length should be type integer"}), 400

    db.session.add(new_cat)
    db.session.commit()
    return jsonify("Cat was added \n")


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=False)
