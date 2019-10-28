from flask import jsonify, request, Blueprint
from arrival import get_by_date, get_user_card_id, insert_user


api_date = Blueprint('api_date', __name__)

@api_date.route("/api", methods=['GET'])
def by_date():

    date = request.args.get('date')
    res = get_by_date(date)

    return jsonify(res)

@api_date.route('/api/card_id', methods=['POST'])   
def by_card_id():
    card_id = request.form['card_id']
    res = get_user_card_id(card_id)
    return res

@api_date.route('/api/register', methods=['POST'])
def by_register():
    name = request.form['name']
    surname = request.form['surname']
    email = request.form['email']
    phone = request.form['tel']
    card_id = request.form['card_id']
    res = insert_user(name,surname,email,phone,card_id)
    
    return res
