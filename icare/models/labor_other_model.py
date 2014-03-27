# -*- coding: utf8
import pymongo


class LaborModel:

    def __init__(self, request):
        self.request = request

    def get_list(self, hospcode, start_date, end_date, start, limit):

        self.request.db['labor'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['labor'].ensure_index('cid', pymongo.ASCENDING)
        self.request.db['labor'].ensure_index('bdate', pymongo.ASCENDING)

        labor_cids = self.get_labor_cids(hospcode)
        cids = self.get_cids(hospcode)

        rs = self.request.db['labor'].find({
            'hospcode': {'$ne': hospcode},
            'cid': {
                '$in': cids,
                '$nin': labor_cids
            },
            'bdate': {
                '$gte': start_date,
                '$lte': end_date
            }
        }).sort('bdate', pymongo.ASCENDING).skip(start).limit(limit)

        return rs

    def get_total(self, hospcode, start_date, end_date):

        self.request.db['labor'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['labor'].ensure_index('cid', pymongo.ASCENDING)
        self.request.db['labor'].ensure_index('bdate', pymongo.ASCENDING)

        labor_cids = self.get_labor_cids(hospcode)
        cids = self.get_labor_cids(hospcode)

        rs = self.request.db['labor'].find({
            'hospcode': {'$ne': hospcode},
            'cid': {
                '$in': cids,
                '$nin': labor_cids
            },
            'bdate': {
                '$gte': start_date,
                '$lte': end_date
            }
        }).count()

        return rs

    def search(self, cid):
        self.request.db['labor'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['labor'].find({
            'cid': cid
        })

        return rs

    def get_cids(self, hospcode):
        self.request.db['anc'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['anc'].find({'hospcode': hospcode}, {'cid': 1})
        cids = []

        for r in rs:
            cids.append(r['cid'])

        return cids

    def get_labor_cids(self, hospcode):
        self.request.db['labor'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['labor'].find({'hospcode': hospcode}, {'cid': 1})
        cids = []

        for r in rs:
            cids.append(r['cid'])

        return cids