import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os
# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv())

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = os.environ["MongoDBConnectionString"]
        client = pymongo.MongoClient(url)
        database = client['db-neighbourly-app']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)