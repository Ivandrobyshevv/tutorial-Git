import logging

import motor.motor_asyncio

logging.basicConfig(level=logging.INFO, filename="src/logs/api_log.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

log = logging.getLogger(__name__)

MONGO_DB = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)

database = client.python_db
