# -*- coding: utf8
import pymongo


class MchModel:

    def __init__(self, request):
        self.request = request

    def get_list(self, hospcode, cids, start, limit):

        self.request.db['labor'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['labor'].ensure_index('bdate', pymongo.ASCENDING)

        rs = self.request.db['labor'].find({'hospcode': {'$ne': hospcode}}).\
            sort('bdate', pymongo.ASCENDING).skip(start).limit(limit)

        return rs

    def get_total(self, hospcode):

        self.request.db['labor'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['labor'].find({'hospcode': {'$ne': hospcode}}).count()
        return rs

    def search(self, hospcode, cid):

        self.request.db['labor'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['labor'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['labor'].find({
            'hospcode': {'$ne': hospcode},
            'cid': cid
        })

        return rs