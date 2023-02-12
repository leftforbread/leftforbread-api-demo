from flask_restful import Api, Resource, reqparse
import json
import recipe


class getSuggestedRecipesHandler(Resource):
  def post(self):
    print(self)
    parser = reqparse.RequestParser()
    parser.add_argument('ingredients', type=str)

    args = parser.parse_args()
    request_str = args['ingredients']
    request_json = json.loads(request_str)

    return recipe.getRecipeSearch(request_json)