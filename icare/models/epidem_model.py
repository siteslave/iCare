# -*- coding: utf8
import pymongo

from icare.helpers.icare_helper import ICHelper

h = ICHelper()


class EpidemModel:
    def __init__(self, request):
        self.request = request

    def get_list(self, hospcode, s, e, start, limit):

        self.request.db['surveillance'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('illdate', pymongo.ASCENDING)

        rs = self.request.db['surveillance'].find({
            'hospcode': hospcode,
            'illdate': {'$gte': s, '$lte': e}
        }).\
            sort('illdate', pymongo.ASCENDING).skip(start).limit(limit)

        return rs

    def get_list_by_code506(self, hospcode, code506, s, e, start, limit):

        self.request.db['surveillance'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('illdate', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('code506', pymongo.ASCENDING)

        rs = self.request.db['surveillance'].find({
            'hospcode': hospcode,
            'code506': code506,
            'illdate': {'$gte': s, '$lte': e}
        }).\
            sort('illdate', pymongo.ASCENDING).skip(start).limit(limit)

        return rs

    def get_list_by_ptstatus(self, hospcode,  ptstatus, s, e, start, limit):

        self.request.db['surveillance'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('illdate', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('ptstatus', pymongo.ASCENDING)

        rs = self.request.db['surveillance'].find({
            'hospcode': hospcode,
            'ptstatus': ptstatus,
            'illdate': {'$gte': s, '$lte': e}
        }).\
            sort('illdate', pymongo.ASCENDING).skip(start).limit(limit)

        return rs

    def get_list_by_code506_ptstatus(self, hospcode, code506, ptstatus, s, e, start, limit):

        self.request.db['surveillance'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('illdate', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('code506', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('ptstatus', pymongo.ASCENDING)

        rs = self.request.db['surveillance'].find({
            'hospcode': hospcode,
            'ptstatus': ptstatus,
            'code506': code506,
            'illdate': {'$gte': s, '$lte': e}
        }).\
            sort('illdate', pymongo.ASCENDING).skip(start).limit(limit)

        return rs

    def get_list_total(self, hospcode, s, e):

        self.request.db['surveillance'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('illdate', pymongo.ASCENDING)

        rs = self.request.db['surveillance'].find({
            'hospcode': hospcode,
            'illdate': {'$gte': s, '$lte': e}
        }).count()

        return rs

    def get_list_total_by_code506(self, hospcode, code506, s, e):

        self.request.db['surveillance'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('illdate', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('code506', pymongo.ASCENDING)

        rs = self.request.db['surveillance'].find({
            'hospcode': hospcode,
            'code506': code506,
            'illdate': {'$gte': s, '$lte': e}
        }).count()

        return rs

    def get_list_total_by_ptstatus(self, hospcode, ptstatus, s, e):

        self.request.db['surveillance'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('illdate', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('ptstatus', pymongo.ASCENDING)

        rs = self.request.db['surveillance'].find({
            'hospcode': hospcode,
            'ptstatus': ptstatus,
            'illdate': {'$gte': s, '$lte': e}
        }).count()

        return rs

    def get_list_total_by_code506_ptstatus(self, hospcode, code506, ptstatus, s, e):

        self.request.db['surveillance'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('illdate', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('ptstatus', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('code506', pymongo.ASCENDING)

        rs = self.request.db['surveillance'].find({
            'hospcode': hospcode,
            'ptstatus': ptstatus,
            'code506': code506,
            'illdate': {'$gte': s, '$lte': e}
        }).count()

        return rs

    def get_info(self, hospcode, pid, seq, diagcode):

        self.request.db['surveillance'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('seq', pymongo.ASCENDING)
        self.request.db['surveillance'].ensure_index('diagcode', pymongo.ASCENDING)

        rs = self.request.db['surveillance'].find_one({
            'hospcode': hospcode,
            'pid': pid,
            'seq': seq,
            'diagcode': diagcode
        })

        return rs