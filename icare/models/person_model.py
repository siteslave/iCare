# -*- coding: utf8
import pymongo


class PersonModel:
    def __init__(self, request):
        self.request = request

    def get_person_detail(self, pid, hospcode):
        self.request.db['person'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('pid', pymongo.ASCENDING)

        rs = self.request.db['person'].find_one({
            'hospcode': hospcode,
            'pid': pid
        })

        if rs:
            return rs
        else:
            return None

    def get_pid_from_cid(self, cid):
        self.request.db['person'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['person'].find_one({
            'hospcode': self.request.session['hospcode'],
            'cid': cid
        })

        return rs['pid']

    def get_cid_from_pid(self, pid, hospcode):
        self.request.db['person'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['person'].find_one({
            'hospcode': hospcode,
            'pid': pid
        })

        return rs['cid']

    def get_hid_from_pid(self, pid, hospcode):
        self.request.db['person'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['person'].find_one({
            'hospcode': hospcode,
            'pid': pid
        })

        return rs['hid'] if rs else None

    def get_vid_from_address(self, pid, hospcode):
        self.request.db['address'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['address'].ensure_index('pid', pymongo.ASCENDING)

        rs = self.request.db['address'].find_one({
            'hospcode': hospcode,
            'pid': pid
        }, {'_id': 0, 'changwat': 1, 'ampur': 1, 'tambon': 1, 'village': 1, 'houseno': 1})

        if rs:
            changwat = rs['changwat'] if 'changwat' in rs else '00'
            ampur = rs['ampur'] if 'ampur' in rs else '00'
            tambon = rs['tambon'] if 'tambon' in rs else '00'
            village = rs['village'] if 'village' in rs else '00'

            villages = '%s%s%s%s' % (changwat, ampur, tambon, village)

            return {'vid': villages, 'house': rs['houseno']}

        else:
            return {'vid': '00000000', 'house': '00'}

    def get_vid_from_home(self, hid, hospcode):
        self.request.db['home'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['home'].ensure_index('hid', pymongo.ASCENDING)

        rs = self.request.db['home'].find_one({
            'hospcode': hospcode,
            'hid': hid
        }, {'_id': 0, 'changwat': 1, 'ampur': 1, 'tambon': 1, 'village': 1, 'house': 1})

        #return rs

        if rs:

            changwat = rs['changwat'] if 'changwat' in rs else '00'
            ampur = rs['ampur'] if 'ampur' in rs else '00'
            tambon = rs['tambon'] if 'tambon' in rs else '00'
            village = rs['village'] if 'village' in rs else '00'

            villages = '%s%s%s%s' % (changwat, ampur, tambon, village)

            return {'vid': villages, 'house': rs['house']}
        else:
            return {'vid': '00000000', 'house': '00'}

    def get_type_area(self, pid, hospcode):
        self.request.db['person'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['person'].find_one({
            'hospcode': hospcode,
            'pid': pid
        })

        return rs['typearea'] if rs else None

    def get_pid_from_hid(self, hospcode, hid):

        rs = self.request.db['person'].find({
            'hospcode': hospcode,
            'hid': {'$in': hid}
        })

        pids = []

        if rs:
            for r in rs:
                pids.append(r['pid'])

        return pids

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

    def get_latlng(self, hospcode, pid):
        self.request.db['home'].ensure_index('hid', pymongo.ASCENDING)
        self.request.db['home'].ensure_index('hospcode', pymongo.ASCENDING)

        hid = self.get_hid_from_pid(hospcode, pid)
        rs = self.request.db['home'].find_one({
            'hid': hid,
            'hospcode': hospcode
        })

        return rs['loc'] if rs else None

    
