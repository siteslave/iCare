# -*- coding: utf8

import pymongo


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