import azure.functions as func
import pymongo
import os
# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv())


def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = os.environ["MongoDBConnectionString"]
            client = pymongo.MongoClient(url)
            database = client['db-neighbourly-app']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )