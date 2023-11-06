#!/usr/bin/env python

# Module imports
import json
from bson.json_util import dumps

# Custom imports
from app.mongo import find_all_worklist_items, WORKLIST_ITEM_DB


def run():
    _items = find_all_worklist_items(_db=WORKLIST_ITEM_DB)
    list_cur = list(_items)
    json_object = json.loads(dumps(list_cur))
    print(json_object[0]['blocks'])

    return


if __name__ == "__main__":
    run()
