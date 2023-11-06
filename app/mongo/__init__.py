#!/usr/bin/env python

# Module imports
import os
import pymongo
from logger import logging
from typing import Union, List, Optional
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Custom modules
from app.config import settings

# -- Database Connection
client = MongoClient(f'mongodb://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_CONNECTION_STR}')
try:
    logging.info("START: DB health check...")
    client.admin.command('ismaster')
    logging.info("DONE: DB health check.")
except ConnectionFailure:
    logging.error("Server not available")

db = client.ocean

WORKLIST_ITEM_DB = db.worklist_item


def find_all_worklist_items(_db: pymongo.collection.Collection) -> List[dict]:
    logging.info("[MongoDB] Find worklist items.")

    _items = _db.find()

    return _items





