# -*- coding: utf8
import pymongo
from bson import Code
from icare.models.person_model import PersonModel

from icare.helpers.icare_helper import ICHelper

h = ICHelper()


class LaborOtherModel:

    def __init__(self, request):
        self.request = request

    def do_process_list(self, hospcode, start_date, end_date):

        reducer = Code("""
                function(curr, result) {
                    //result.total++;
                }
        """)

        data = self.request.db['labor'].group(
            key={
                'hospcode': 1,
                'pid': 1,
                'gravida': 1,
                'bdate': 1
            },
            condition={
                'hospcode': hospcode,
                'bdate': {
                    '$gte': start_date,
                    '$lte': end_date
                }
            },
            initial={},
            reduce=reducer)

        if data:

            self.request.db['labor_other'].remove({'process_hospcode': self.request.session['hospcode']})

            person = PersonModel(self.request)

            for r in data:

                typearea = person.get_type_area(r['pid'], r['hospcode'])

                if typearea in ['2', '4']:
                    address = person.get_vid_from_address(r['pid'], r['hospcode'])
                else:
                    hid = person.get_hid_from_pid(r['pid'], r['hospcode'])
                    address = person.get_vid_from_home(hid, r['hospcode'])

                obj = {
                    'hospcode': r['hospcode'],
                    'process_hospcode': self.request.session['hospcode'],
                    'pid': r['pid'],
                    'gravida': r['gravida'],
                    'bdate': r['bdate'],
                    'address': address,
                    'typearea': person.get_type_area(r['pid'], r['hospcode'])
                }

                self.request.db['labor_other'].insert(obj)

        else:
            return False

    def get_list(self, hospcode, start_date, end_date, start, limit):

        self.request.db['labor_other'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['labor_other'].ensure_index('process_hospcode', pymongo.ASCENDING)
        self.request.db['labor_other'].ensure_index('bdate', pymongo.ASCENDING)
        self.request.db['labor_other'].ensure_index('address', pymongo.ASCENDING)

        #villages
        villages = h.get_villages(self.request, self.request.session['hospcode'])

        vid = []
        for v in villages:
            vid.append(v['vid'])

        rs = self.request.db['labor_other'].find({
            'hospcode': hospcode,
            'process_hospcode': self.request.session['hospcode'],
            'bdate': {
                '$gte': start_date,
                '$lte': end_date
            },
            'address.vid': {
                '$in': vid
            }
        }).sort('bdate', pymongo.ASCENDING).skip(start).limit(limit)

        return rs

    def get_total(self, hospcode, start_date, end_date):

        self.request.db['labor_other'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['labor_other'].ensure_index('process_hospcode', pymongo.ASCENDING)
        self.request.db['labor_other'].ensure_index('bdate', pymongo.ASCENDING)
        self.request.db['labor_other'].ensure_index('address', pymongo.ASCENDING)

        villages = h.get_villages(self.request, self.request.session['hospcode'])

        vid = []
        for v in villages:
            vid.append(v['vid'])

        rs = self.request.db['labor_other'].find({
            'hospcode': hospcode,
            'process_hospcode': self.request.session['hospcode'],
            'bdate': {
                '$gte': start_date,
                '$lte': end_date
            },
            'address.vid': {
                '$in': vid
            }
        }).count()

        return rs

    def get_labor_detail(self, pid, gravida, hospcode):
        self.request.db['anc'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('gravida', pymongo.ASCENDING)

        rs = self.request.db['labor'].find_one({
            'hospcode': hospcode,
            'pid': pid,
            'gravida': gravida,
        })

        return rs

