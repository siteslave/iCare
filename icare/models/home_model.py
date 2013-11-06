import pymongo

class HomeModel(object):
    """docstring for HomeModel"""
    def __init__(self, request):
        #super(HomeModel, self).__init__()
        self.request = request

    def remove_latlng(self, hospcode, hid):
        self.request.db['home'].ensure_index('hid', pymongo.ASCENDING)
        self.request.db['home'].ensure_index('hospcode', pymongo.ASCENDING)

        self.request.db['home'].update({
            'hid': hid,
            'hospcode': hospcode
        },{
            '$set': { 'loc': []}
        })
        
    def save_latlng(self, hid, hospcode, lat, lng):

        self.request.db['home'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['home'].ensure_index('hid', pymongo.ASCENDING)

        rs = self.request.db['home'].update({'hid': hid, 'hospcode': hospcode}, {
        '$set': {
            'loc': [lat, lng]
        }}, True)

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