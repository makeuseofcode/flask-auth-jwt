from flask import Flask
from routes.user_auth import register_routes
from utils.db import connect_to_mongodb
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()


mongo_uri = os.getenv('MONGO_URI')
db = connect_to_mongodb(mongo_uri)

# Register API routes
register_routes(app, db)

if __name__ == '__main__':
    app.run(debug=True)
