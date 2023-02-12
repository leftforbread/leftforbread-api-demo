from flask import Flask, send_from_directory, render_template
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from TestApiHandler import TestApiHandler
from getSuggestedRecipesHandler import getSuggestedRecipesHandler

from getIngredientsHandler import getIngredientsHandler
from getFavoriteRecipesHandler import getFavoriteRecipesHandler
from addFavoriteRecipeHandler import addFavoriteRecipeHandler
from removeFavoriteRecipeHandler import removeFavoriteRecipeHandler

# Use the second line to serve the front end with the back end
app = Flask(__name__, static_url_path='', static_folder='')
# app = Flask(__name__, static_url_path='', static_folder='frontend/build')
app.config.from_pyfile('settings.py')

CORS(app) #comment this on deployment
api = Api(app)

# @app.route("/", defaults={'path':''})
# def serve(path):
#     return send_from_directory(str(app.static_folder),'index.html')

@app.route("/")
def ok():
 #   return render_template("mainpage.html")  
   return {

      'resultStatus': 'SUCCESS',
      'message': "api is running"
      }

api.add_resource(TestApiHandler, '/flask/test')

api.add_resource(getSuggestedRecipesHandler, '/getSuggestedRecipes')

api.add_resource(getIngredientsHandler, '/getIngredients')
api.add_resource(getFavoriteRecipesHandler, '/getFavoriteRecipes')
api.add_resource(addFavoriteRecipeHandler, '/addFavoriteRecipe')
api.add_resource(removeFavoriteRecipeHandler, '/removeFavoriteRecipe')

# api.add_resource(getSuggestedRecipesHandler, '/test')
# if __name__ == '__main__':
#     app.run(debug=True)