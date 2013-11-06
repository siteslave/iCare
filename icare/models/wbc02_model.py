# -*- coding: utf8
import pymongo

from icare.helpers.icare_helper import ICHelper

h = ICHelper()


class Wbc02Model:
    def __init__(self, request):
        self.request = request

    def get_list(self, hospcode, s, e, start, limit):

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
            'birth': {'$lte': e, '$gte': s},
            'typearea': {'$in': ['1', '3']}
        }).\
            sort('name', pymongo.ASCENDING).skip(start).limit(limit)

        return rs

    def get_list_by_vid(self, hospcode, s, e, start, limit, hid):

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
            'birth': {'$lte': e, '$gte': s},
            'hid': {'$in': hid},
            'typearea': {'$in': ['1', '3']}
        }).\
            sort('name', pymongo.ASCENDING).skip(start).limit(limit)

        return rs

    def get_list_total(self, hospcode, s, e):

        self.request.db['person'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('typearea', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('birth', pymongo.ASCENDING)

        rs = self.request.db['person'].find({
            'hospcode': hospcode,
            'birth': {'$lte': e, '$gte': s},
            'typearea': {'$in': ['1', '3']}
        }).count()

        return rs

    def get_list_total_by_vid(self, hospcode, s, e, hid):

        self.request.db['person'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('typearea', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('birth', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('hid', pymongo.ASCENDING)

        rs = self.request.db['person'].find({
            'hospcode': hospcode,
            'birth': {'$lte': e, '$gte': s},
            'hid': {'$in': hid},
            'typearea': {'$in': ['1', '3']}
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

    def get_bcg(self, hospcode, pid):

        self.request.db['epi'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['epi'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['epi'].ensure_index('vaccinetype', pymongo.ASCENDING)

        rs = self.request.db['epi'].find_one({
            'hospcode': hospcode,
            'pid': pid,
            'vaccinetype': '010'
        })
        if rs:
            obj = {
                'vaccineplace_code': rs['vaccineplace'],
                'vaccineplace_name': h.get_hospital_name(self.request, rs['vaccineplace']),
                'date_serv': h.to_thai_date(rs['date_serv'])
            }
            return obj
        else:
            return None

    def get_dtphb3(self, hospcode, pid):

        self.request.db['epi'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['epi'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['epi'].ensure_index('vaccinetype', pymongo.ASCENDING)

        rs = self.request.db['epi'].find_one({
            'hospcode': hospcode,
            'pid': pid,
            'vaccinetype': '093'
        })

        if rs:
            obj = {
                'vaccineplace_code': rs['vaccineplace'],
                'vaccineplace_name': h.get_hospital_name(self.request, rs['vaccineplace']),
                'date_serv': h.to_thai_date(rs['date_serv'])
            }
            return obj
        else:
            return None

    def get_opv3(self, hospcode, pid):

        self.request.db['epi'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['epi'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['epi'].ensure_index('vaccinetype', pymongo.ASCENDING)

        rs = self.request.db['epi'].find_one({
            'hospcode': hospcode,
            'pid': pid,
            'vaccinetype': '083'
        })

        if rs:
            obj = {
                'vaccineplace_code': rs['vaccineplace'],
                'vaccineplace_name': h.get_hospital_name(self.request, rs['vaccineplace']),
                'date_serv': h.to_thai_date(rs['date_serv'])
            }
            return obj
        else:
            return None

    def get_dtp4(self, hospcode, pid):

        self.request.db['epi'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['epi'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['epi'].ensure_index('vaccinetype', pymongo.ASCENDING)

        rs = self.request.db['epi'].find_one({
            'hospcode': hospcode,
            'pid': pid,
            'vaccinetype': '034'
        })

        if rs:
            obj = {
                'vaccineplace_code': rs['vaccineplace'],
                'vaccineplace_name': h.get_hospital_name(self.request, rs['vaccineplace']),
                'date_serv': h.to_thai_date(rs['date_serv'])
            }
            return obj
        else:
            return None

    def get_opv4(self, hospcode, pid):

        self.request.db['epi'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['epi'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['epi'].ensure_index('vaccinetype', pymongo.ASCENDING)

        rs = self.request.db['epi'].find_one({
            'hospcode': hospcode,
            'pid': pid,
            'vaccinetype': '084'
        })

        if rs:
            obj = {
                'vaccineplace_code': rs['vaccineplace'],
                'vaccineplace_name': h.get_hospital_name(self.request, rs['vaccineplace']),
                'date_serv': h.to_thai_date(rs['date_serv'])
            }
            return obj
        else:
            return None

    def get_je2(self, hospcode, pid):

        self.request.db['epi'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['epi'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['epi'].ensure_index('vaccinetype', pymongo.ASCENDING)

        rs = self.request.db['epi'].find_one({
            'hospcode': hospcode,
            'pid': pid,
            'vaccinetype': '052'
        })

        if rs:
            obj = {
                'vaccineplace_code': rs['vaccineplace'],
                'vaccineplace_name': h.get_hospital_name(self.request, rs['vaccineplace']),
                'date_serv': h.to_thai_date(rs['date_serv'])
            }
            return obj
        else:
            return None

    def search_visit(self, cid):

        self.request.db['epi'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['epi'].find({
            'cid': cid
        }).sort('date_serv', pymongo.ASCENDING)

        return rs if rs else None

    def get_nutrition(self, cid):
        self.request.db['nutrition'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['nutrition'].find({'cid': cid}).\
            sort('date_serv', pymongo.ASCENDING)

        return rs if rs else None

    def get_nutrition_owner(self, pid, hospcode):
        self.request.db['nutrition'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['nutrition'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['nutrition'].find({
            'pid': pid,
            'hospcode': hospcode
        }).sort('date_serv', pymongo.ASCENDING)

        return rs if rs else None

    def count_nutrition(self, hospcode, pid):
        self.request.db['nutrition'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['nutrition'].ensure_index('pid', pymongo.ASCENDING)

        rs = self.request.db['nutrition'].find({
            'pid': pid,
            'hospcode': hospcode
        }).count()

        return rs