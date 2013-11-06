# -*- coding: utf8
import pymongo

from icare.helpers.icare_helper import ICHelper

h = ICHelper()


class NCDScreenModel:
    def __init__(self, request):
        self.request = request

    def get_list(self, hospcode, x, start, limit):

        self.request.db['person'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('typearea', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('birth', pymongo.ASCENDING)

        rs = self.request.db['person'].find({
            'hospcode': hospcode,
            'birth': {'$lte': x},
            'typearea': {'$in': ['1', '3']},
            'discharge': '9'
        }).\
            sort('name', pymongo.ASCENDING).skip(start).limit(limit)

        return rs

    def get_list_by_vid(self, hospcode, x, start, limit, hid):

        """

        :param hospcode: Hospital code
        :param s: Start date
        :param e: End date
        :param start:
        :param limit:
        :return:
        """
        self.request.db['person'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('typearea', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('birth', pymongo.ASCENDING)
        """
        db.person.find({
            hospcode: '11053',
            birth: {$lte: '20130810', $gte: '20110810'},
            typearea: {$in: ['1','3']}
        })
        """

        rs = self.request.db['person'].find({
            'hospcode': hospcode,
            'birth': {'$lte': x},
            'hid': {'$in': hid},
            'typearea': {'$in': ['1', '3']},
            'discharge': '9'
        }).\
            sort('name', pymongo.ASCENDING).skip(start).limit(limit)

        return rs

    def get_list_total(self, hospcode, x):

        self.request.db['person'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('typearea', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('birth', pymongo.ASCENDING)

        rs = self.request.db['person'].find({
            'hospcode': hospcode,
            'birth': {'$lte': x},
            'typearea': {'$in': ['1', '3']},
            'discharge': '9'
        }).count()

        return rs

    def get_list_total_by_vid(self, hospcode, x, hid):

        self.request.db['person'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('typearea', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('birth', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('hid', pymongo.ASCENDING)

        rs = self.request.db['person'].find({
            'hospcode': hospcode,
            'birth': {'$lte': x},
            'hid': {'$in': hid},
            'typearea': {'$in': ['1', '3']},
            'discharge': '9'
        }).count()

        return rs

    def get_hid_from_village(self, hospcode, vid):

        chw = vid[:2]
        amp = vid[2:4]
        tmb = vid[4:6]
        moo = vid[6:8]

        self.request.db['home'].ensure_index('changwat', pymongo.ASCENDING)
        self.request.db['home'].ensure_index('ampur', pymongo.ASCENDING)
        self.request.db['home'].ensure_index('tambon', pymongo.ASCENDING)
        self.request.db['home'].ensure_index('village', pymongo.ASCENDING)
        self.request.db['home'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['home'].ensure_index('hid', pymongo.ASCENDING)

        rs = self.request.db['home'].find({
            'changwat': chw,
            'ampur': amp,
            'tambon': tmb,
            'village': moo,
            'hospcode': hospcode
        }, {'hid': 1})

        hid = []
        for r in rs:
            hid.append(r['hid'])

        return hid

    def get_date_serv(self, hospcode, pid, s, e):
        self.request.db['ncdscreen'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['ncdscreen'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['ncdscreen'].ensure_index('date_serv', pymongo.ASCENDING)

        rs = self.request.db['ncdscreen'].find_one({
            'hospcode': hospcode,
            'pid': pid,
            'date_serv': {'$gte': s, '$lte': e}
        })

        return rs['date_serv'] if rs else None

    def get_screen(self, hospcode, pid, date_serv):

        self.request.db['ncdscreen'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['ncdscreen'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['ncdscreen'].ensure_index('date_serv', pymongo.ASCENDING)

        rs = self.request.db['ncdscreen'].find_one({
            'hospcode': hospcode,
            'pid': pid,
            'date_serv': date_serv
        })

        return rs if rs else None

    def get_history(self, cid, start, limit):

        self.request.db['ncdscreen'].ensure_index('cid', pymongo.ASCENDING)
        rs = self.request.db['ncdscreen'].find({
            'cid': cid
        }).\
            sort('name', pymongo.ASCENDING).skip(start).limit(limit)

        return rs if rs else None

    def get_history_total(self, cid):

        self.request.db['ncdscreen'].ensure_index('cid', pymongo.ASCENDING)
        rs = self.request.db['ncdscreen'].find({
            'cid': cid
        }).count()

        return rs