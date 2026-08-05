from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import redis

db = SQLAlchemy()
jwt = JWTManager()
cors = CORS()
redis_client = redis.Redis(host="localhost", port=6379, db=1, decode_responses=True)