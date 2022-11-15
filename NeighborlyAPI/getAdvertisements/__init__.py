import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os
# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv())

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = os.environ["MongoDBConnectionString"]
        client = pymongo.MongoClient(url)
        database = client['db-neighbourly-app']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

