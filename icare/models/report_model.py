# -*- coding: utf8
import pymongo


class ReportModel:
    def __init__(self, request):
        self.request = request

    def get_babies_total(self, hospcode):
        self.request.db['newborn'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['newborn'].find_one({
            'hospcode': hospcode
        })
        
        if rs:
            return rs
        else:
            return None

    def get_risk_all_list(self, start, limit, hospcode):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode
        }).\
            sort('last_update', pymongo.ASCENDING).skip(start).limit(limit)

        return rs if rs else None

    def get_risk_search(self, cid):
        self.request.db['anc_survey'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'cid': cid
        }).\
            sort('last_update', pymongo.ASCENDING)

        return rs if rs else None

    def get_risk_filter_list(self, start, limit, hospcode, t):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'is_risk': t
        }).\
            sort('last_update', pymongo.ASCENDING).skip(start).limit(limit)

        return rs if rs else None

    def get_risk_all_total(self, hospcode):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({'hospcode': hospcode}).count()

        return rs

    def get_risk_filter_total(self, hospcode, t):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find(
            {
                'hospcode': hospcode,
                'is_risk': t
            }).count()

        return rs

    def get_risk_detail(self, id):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find_one(
            {
                '_id': id
            })

        return rs

    def get_risk_screen_list(self, cid):
        self.request.db['anc_survey'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'cid': cid
        }, {'last_update': 1})

        return rs

    def get_anc_history(self, cid):
        #self.request.db['anc'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['anc'].find({
            'cid': cid
        }).sort('date_serv', pymongo.ASCENDING)

        return rs

    def get_anc_list_all(self, hospcode, start, limit):
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
            'hospcode': hospcode
        }).skip(start).limit(limit)

        return rs

    def get_anc_list_all_total(self, hospcode):
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
            'hospcode': hospcode
        }).count()

        return rs

    def get_anc_list_success(self, hospcode, start, limit):
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
            'hospcode': hospcode
        }).skip(start).limit(limit)

        return rs

    def get_anc_list_success_total(self, hospcode):
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
            'hospcode': hospcode
        }).count()

        return rs

    def get_anc_list_not_success(self, hospcode, start, limit):
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
            'hospcode': hospcode
        }).skip(start).limit(limit)

        return rs

    def get_anc_list_not_success_total(self, hospcode):
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
            'hospcode': hospcode
        }).count

        return rs

    def get_anc_search(self, hospcode, cid):
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
            'hospcode': hospcode,
            'cid': cid
        })

        return rs

    def get_anc_forecast_filter(self, hospcode, start_date, end_date):
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
            'hospcode': hospcode,
            'coverages': {
                '$elemMatch': {
                    'forecast': {
                        '$gte': str(start_date),
                        '$lte': str(end_date)
                    }
                }
            }
        })

        return rs

    #Get all mch list
    def get_mch_list(self, hospcode):
        self.request.db['mch'].ensure_index('hospcode', pymongo.ASCENDING)
        
        rs = self.request.db['mch'].find({
            'hospcode': hospcode
        })

        return rs