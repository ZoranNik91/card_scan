from flask import jsonify, request, Blueprint
from arrival import get_by_date

api_date = Blueprint('api_date', __name__,  static_folder='')

@api_date.route("/api/date")
def by_date():

    date = request.args.get('date') # #2
    res = get_by_date(date)

    return jsonify(res)