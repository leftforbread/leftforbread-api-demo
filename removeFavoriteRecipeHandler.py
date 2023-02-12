from flask_restful import Api, Resource, reqparse
import json
from db import start, remove_favorite


class removeFavoriteRecipeHandler(Resource):
  def post(self):
    print(self)
    # parser = reqparse.RequestParser()
    # parser.remove_argument('recipe', type=str)

    # args = parser.parse_args()
    # request_str = args['recipe']

    # conn = start()
    # remove_favorite(conn, "tester", request_str)

    return {"status": "tbd"}