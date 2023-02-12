"""
EDAMAM SCHEMA

Model Schema 
{
 "from": 0,
 "to": 0,
 "count": 0,
 "_links": {
   "self": {
     "href": "string",
     "title": "string"
   },
   "next": {
     "href": "string",
     "title": "string"
   }
 },
 "hits": [
   {
     "recipe": {
       "uri": "string",
       "label": "string",
       "image": "string",
       "images": {
         "THUMBNAIL": {
           "url": "string",
           "width": 0,
           "height": 0
         },
         "SMALL": {
           "url": "string",
           "width": 0,
           "height": 0
         },
         "REGULAR": {
           "url": "string",
           "width": 0,
           "height": 0
         },
         "LARGE": {
           "url": "string",
           "width": 0,
           "height": 0
         }
       },
       "source": "string",
       "url": "string",
       "shareAs": "string",
       "yield": 0,
       "dietLabels": [
         "string"
       ],
       "healthLabels": [
         "string"
       ],
       "cautions": [
         "string"
       ],
       "ingredientLines": [
         "string"
       ],
       "ingredients": [
         {
           "text": "string",
           "quantity": 0,
           "measure": "string",
           "food": "string",
           "weight": 0,
           "foodId": "string"
         }
       ],
       "calories": 0,
       "glycemicIndex": 0,
       "totalCO2Emissions": 0,
       "co2EmissionsClass": "A+",
       "totalWeight": 0,
       "cuisineType": [
         "string"
       ],
       "mealType": [
         "string"
       ],
       "dishType": [
         "string"
       ],
       "instructions": [
         "string"
       ],
       "tags": [
         "string"
       ],
       "externalId": "string",
       "totalNutrients": {},
       "totalDaily": {},
       "digest": [
         {
           "label": "string",
           "tag": "string",
           "schemaOrgTag": "string",
           "total": 0,
           "hasRDI": true,
           "daily": 0,
           "unit": "string",
           "sub": {}
         }
       ]
     },
     "_links": {
       "self": {
         "href": "string",
         "title": "string"
       },
       "next": {
         "href": "string",
         "title": "string"
       }
     }
   }
 ]
}
"""

from urllib.request import urlopen
import json

# this is not secure, but we *are* just hacking away...
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

EDAMAM_APP_ID="81e2e983"
EDAMAM_APP_KEY="7e0267923a1bb9b99a87c5020f6674c7"

"""Given an array of ingredients (e.g. ["carrot", "onion", "celery"]), return a json of the most relevent recipes."""
def getRecipeSearch(ingredients):
    ingList = ""
    if ingredients:
        ingList += ingredients[0]
    for x in range(1, len(ingredients)):
        ingList += "%2C"
        ingList += ingredients[x]
    with urlopen("https://api.edamam.com/api/recipes/v2?type=public&q=" + \
        ingList + "&app_id=" + str(EDAMAM_APP_ID) + "&app_key=" + str(EDAMAM_APP_KEY)) as response:
        return json.loads(response.read())


def getRecipeById(id):
    with urlopen("https://api.edamam.com/api/recipes/v2/" + str(id) + "?type=public" + \
        "&app_id=" + str(EDAMAM_APP_ID) + "&app_key=" + str(EDAMAM_APP_KEY)) as response:
        return json.loads(response.read())