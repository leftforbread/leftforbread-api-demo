from flask_restful import Api, Resource, reqparse
import json
from db import start, add_favorite


class addFavoriteRecipeHandler(Resource):
  def post(self):
    print(self)
    # parser = reqparse.RequestParser()
    # parser.add_argument('recipe', type=str)

    # args = parser.parse_args()
    # request_str = args['recipe']

    # conn = start()
    # add_favorite(conn, "tester", request_str)

    return {"status": "tbd"}