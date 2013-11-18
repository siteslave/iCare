# -*- coding: utf8
from bson import Code

import pymongo
from icare.models.person_model import PersonModel


class BabiesModel:
    def __init__(self, request):
        self.request = request

    def get_list(self, start, limit):
        """
         Get person list
        """
        self.request.db['newborn'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['newborn'].ensure_index('pid', pymongo.ASCENDING)

        rs = self.request.db['newborn'].find({
            'hospcode': self.request.session['hospcode']
        }).sort('pid', pymongo.ASCENDING).skip(start).limit(limit)

        return rs

    def search(self, cid):
        """
         Get person list
        """
        self.request.db['newborn'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['newborn'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['newborn'].find({
            'hospcode': self.request.session['hospcode'],
            'cid': cid,
        })

        return rs

    def get_list_total(self):
        """
        Get total record
        """
        self.request.db['newborn'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['newborn'].find({
            'hospcode': self.request.session['hospcode']
        }).count()

        return rs

    def get_count_care(self, pid, hospcode):
        self.request.db['newborncare'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['newborncare'].ensure_index('pid', pymongo.ASCENDING)

        rs = self.request.db['newborncare'].find({'hospcode': hospcode, 'pid': pid}).count()

        return rs

    def get_mother(self, pid, hospcode):

        self.request.db['person'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('pid', pymongo.ASCENDING)

        rs = self.request.db['person'].find_one({'hospcode': hospcode, 'pid': pid})
        if rs:
            fullname = rs['name'] + ' ' + rs['lname']
            cid = rs['cid']

            mother = {
                'fullname': fullname,
                'cid': cid
            }
            return mother
        else:
            mother = {
                'fullname': '-',
                'cid': '-'
            }

            return mother

    def get_care(self, pid, hospcode):

        self.request.db['newborncare'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['newborncare'].ensure_index('pid', pymongo.ASCENDING)

        rs = self.request.db['newborncare'].find({'hospcode': hospcode, 'pid': pid}).sort('bcare', pymongo.ASCENDING)

        return rs

    def get_care_all(self, cid):

        self.request.db['newborncare'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['newborncare'].find({'cid': cid}).sort('bcare', pymongo.ASCENDING)

        return rs

    def get_newborn(self, pid, hospcode):

        self.request.db['newborn'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['newborn'].ensure_index('pid', pymongo.ASCENDING)

        rs = self.request.db['newborn'].find_one({'hospcode': hospcode, 'pid': pid})

        return rs

    def count_appointment(self, pid, hospcode, seq):
        self.request.db['appointment'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['appointment'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['appointment'].ensure_index('seq', pymongo.ASCENDING)

        rs = self.request.db['appointment'].find({
            'pid': pid,
            'hospcode': hospcode,
            'seq': seq
        }).count()

        return rs

    def get_newborn_weight_less_than_2500(self, hospcode, start, limit):
        self.request.db['newborn'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['newborn'].ensure_index('bweight', pymongo.ASCENDING)

        rs = self.request.db['newborn'].find(
            {
                'bweight': {
                    '$lt': '2500'
                },
                'hospcode': hospcode
            }).skip(start).limit(limit)

        return rs

    def search_newborn_weight_less_than_2500(self, cid, hospcode):
        self.request.db['newborn'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['newborn'].ensure_index('bweight', pymongo.ASCENDING)
        self.request.db['newborn'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['newborn'].find(
            {
                'bweight': {
                    '$lt': '2500'
                },
                'cid': cid,
                'hospcode': hospcode
            })

        return rs

    def get_newborn_weight_less_than_2500_total(self, hospcode):
        self.request.db['newborn'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['newborn'].ensure_index('bweight', pymongo.ASCENDING)

        rs = self.request.db['newborn'].find(
            {
                'bweight': {
                    '$lt': '2500'
                },
                'hospcode': hospcode
            }).count()
        return rs

    def process_milk(self, hospcode):
        self.request.db['newborncare'].ensure_index('hospcode', pymongo.ASCENDING)

        reducer = Code("""
                        function(curr, result) {
                            result.total++
                        }
                    """)

        data = self.request.db['newborncare'].group(
            key={
                'hospcode': 1,
                'pid': 1,
            },
            condition={
                'hospcode': hospcode,
                'food': '1'
            },
            initial={'total': 0},
            reduce=reducer)

        if data:
            self.request.db['newborn_milks'].remove({'hospcode': hospcode})
            person = PersonModel(self.request)

            for r in data:
                p = person.get_person_detail(r['pid'], r['hospcode'])
                obj = {
                    'cid': p['cid'],
                    'pid': r['pid'],
                    'hospcode': r['hospcode'],
                    'total': r['total']
                }

                self.request.db['newborn_milks'].insert(obj)

            return True
        else:
            return False

    def get_milk_list(self, hospcode, start, limit):
        self.request.db['newborn_milks'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['newborn_milks'].ensure_index('total', pymongo.ASCENDING)

        rs = self.request.db['newborn_milks'].find(
            {
                'total': {'$gte': 2},
                'hospcode': hospcode
            }).skip(start).limit(limit)

        return rs

    def get_milk_total(self, hospcode):
        self.request.db['newborn_milks'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['newborn_milks'].ensure_index('total', pymongo.ASCENDING)

        rs = self.request.db['newborn_milks'].find(
            {
                'total': {'$gte': 2},
                'hospcode': hospcode
            }).count()

        return rs