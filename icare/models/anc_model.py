# -*- coding: utf8

import pymongo
from bson import Code
from datetime import datetime
from datetime import timedelta

from icare.models.person_model import PersonModel


class AncModel:
    def __init__(self, request):
        self.request = request

    def get_list(self, start, limit):
        """
         Get person list
        """

        rs = self.request.db['anc_coverages'].find({
            'hospcode': self.request.session['hospcode'],
            'typearea': {'$in': ['1', '3']}
        }).sort('pid', pymongo.ASCENDING).skip(start).limit(limit)

        return rs

    def get_list_total(self):
        """
        Get total record
        """
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('typearea', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
            'hospcode': self.request.session['hospcode'],
            'typearea': {'$in': ['1', '3']}
        }).distinct('pid')

        return len(rs)

    def get_pid_list(self):
        """
        Get distinct pid from anc collection
        """
        self.request.db['anc'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('pid', pymongo.ASCENDING)

        rs = self.request.db['anc'].find({
            'hospcode': self.request.session['hospcode']
        }).distinct('pid')

        return rs

    def get_last_anc(self, pid, gravida, hospcode):
        self.request.db['anc'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('gravida', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('date_serv', pymongo.ASCENDING)

        rs = self.request.db['anc'].find({
            'hospcode': hospcode,
            'pid': pid,
            'gravida': gravida
        }).sort('date_serv', pymongo.DESCENDING).limit(1)

        return rs[0]['date_serv']

    def get_first_anc(self, pid, gravida, hospcode):
        self.request.db['anc'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('date_serv', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('gravida', pymongo.ASCENDING)

        rs = self.request.db['anc'].find({
            'hospcode': hospcode,
            'pid': pid,
            'gravida': gravida
        }).sort('date_serv', pymongo.ASCENDING).limit(1)

        return rs[0]['date_serv']

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

    def get_labor_detail_by_cid(self, cid, gravida, hospcode):
        self.request.db['anc'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('cid', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('gravida', pymongo.ASCENDING)

        rs = self.request.db['labor'].find_one({
            'cid': cid,
            'gravida': gravida,
            'hospcode': hospcode
        })

        return rs

    def get_prenatal_detail(self, pid, gravida, hospcode):
        self.request.db['prenatal'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['prenatal'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['prenatal'].ensure_index('gravida', pymongo.ASCENDING)

        rs = self.request.db['prenatal'].find_one({
            'hospcode': hospcode,
            'pid': pid,
            'gravida': gravida,
        })

        return rs

    def get_visit_list(self, cid, start, limit):
        #self.request.db['anc'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('cid', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('date_serv', pymongo.ASCENDING)

        rs = self.request.db['anc'].find({
            #'hospcode': self.request.session['hospcode'],
            'cid': cid
        }).sort('date_serv', pymongo.ASCENDING).skip(start).limit(limit)

        return rs

    def get_visit_all(self, cid):
        #self.request.db['anc'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['anc'].find({
            #'hospcode': self.request.session['hospcode'],
            'cid': cid
        }).sort('date_serv', pymongo.ASCENDING)

        return rs

    def get_visit_list_total(self, cid):
        #self.request.db['anc'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['anc'].find({
            #'hospcode': self.request.session['hospcode'],
            'cid': cid
        }).count()

        return rs

    def get_survey_status(self, pid, gravida, hospcode):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('gravida', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'pid': pid,
            'gravida': gravida
        }).count()

        return rs

    def save_survey(self, data):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('gravida', pymongo.ASCENDING)

        self.request.db['anc_survey'].update({
            'hospcode': data['hospcode'],
            'pid': data['pid'],
            # 'cid': data['cid'],
            'gravida': data['gravida']
        }, {'$set': data}, True)

    def get_survey(self, pid, gravida, hospcode):

        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('gravida', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find_one({
            'pid': pid,
            'gravida': gravida,
            'hospcode': hospcode
        })

        return rs

    def do_process_list(self, hospcode):

        reducer = Code("""
                function(curr, result) {
                    result.total++;
                }
        """)

        data = self.request.db['anc'].group(
            key={
                'hospcode': 1,
                'pid': 1,
                'gravida': 1
            },
            condition={
                'hospcode': hospcode
            },
            initial={'total': 0},
            reduce=reducer)

        if data:

            self.request.db['anc_coverages'].remove({'hospcode': hospcode})

            try:
                person = PersonModel(self.request)

                for i in data:
                    #get anc detail
                    anc01 = self.get_anc_detail(i['hospcode'], i['pid'], i['gravida'], '1')
                    anc02 = self.get_anc_detail(i['hospcode'], i['pid'], i['gravida'], '2')
                    anc03 = self.get_anc_detail(i['hospcode'], i['pid'], i['gravida'], '3')
                    anc04 = self.get_anc_detail(i['hospcode'], i['pid'], i['gravida'], '4')
                    anc05 = self.get_anc_detail(i['hospcode'], i['pid'], i['gravida'], '5')

                    #print(anc04)
                    p = person.get_person_detail(i['pid'], i['hospcode'])
                    doc = {
                        'hospcode': i['hospcode'],
                        'pid': i['pid'],
                        'cid': p['cid'],
                        'gravida': i['gravida'],
                        'total': i['total'],
                        'hid': p['hid'],
                        'typearea': p['typearea'],
                        'is_labor': self.is_labor(i['hospcode'], i['pid'], i['gravida']),
                        #get anc coverages
                        'coverages': [
                            {
                                'ancno': '1',
                                'ga': anc01['ga'] if 'ga' in anc01 else None,
                                'date_serv': anc01['date_serv'] if 'date_serv' in anc01 else None,
                                'forecast': None if 'date_serv' in anc01 else self.get_anc_forecast(anc01, anc02, anc03, anc04, anc05, '1')
                            },
                            {
                                'ancno': '2',
                                'ga': anc02['ga'] if 'ga' in anc02 else None,
                                'date_serv': anc02['date_serv'] if 'date_serv' in anc02 else None,
                                'forecast': None if 'date_serv' in anc02 else self.get_anc_forecast(anc01, anc02, anc03, anc04, anc05, '2')
                            },
                            {
                                'ancno': '3',
                                'ga': anc03['ga'] if 'ga' in anc03 else None,
                                'date_serv': anc03['date_serv'] if 'date_serv' in anc03 else None,
                                'forecast': None if 'date_serv' in anc03 else self.get_anc_forecast(anc01, anc02, anc03, anc04, anc05, '3')
                            },
                            {
                                'ancno': '4',
                                'ga': anc04['ga'] if 'ga' in anc04 else None,
                                'date_serv': anc04['date_serv'] if 'date_serv' in anc04 else None,
                                'forecast': None if 'date_serv' in anc04 else self.get_anc_forecast(anc01, anc02, anc03, anc04, anc05, '4')
                            },
                            {
                                'ancno': '5',
                                'ga': anc05['ga'] if 'ga' in anc05 else None,
                                'date_serv': anc05['date_serv'] if 'date_serv' in anc05 else None,
                                'forecast': None if 'date_serv' in anc05 else self.get_anc_forecast(anc01, anc02, anc03, anc04, anc05, '5')
                            }
                        ]
                    }

                    self.request.db['anc_coverages'].insert(doc)

                return True
            except Exception as ex:
                #print(ex.message)
                return False

        else:
            return False

    def get_anc_forecast(self, anc01, anc02, anc03, anc04, anc05, t):
        if t == '1':
            if 'date_serv' in anc02:
                d = datetime.strptime(anc02['date_serv'], '%Y%m%d')
                nd = d - timedelta(days=42)
                return nd.strftime('%Y%m%d')
            elif 'date_serv' in anc03:
                d = datetime.strptime(anc03['date_serv'], '%Y%m%d')
                nd = d - timedelta(days=98)
                return nd.strftime('%Y%m%d')
            elif 'date_serv' in anc04:
                d = datetime.strptime(anc04['date_serv'], '%Y%m%d')
                nd = d - timedelta(days=140)
                return nd.strftime('%Y%m%d')
            elif 'date_serv' in anc05:
                d = datetime.strptime(anc05['date_serv'], '%Y%m%d')
                nd = d - timedelta(days=182)
                return nd.strftime('%Y%m%d')
            else:
                return None
        elif t == '2':
            if 'date_serv' in anc01:
                d = datetime.strptime(anc01['date_serv'], '%Y%m%d')
                nd = d + timedelta(days=42)
                return nd.strftime('%Y%m%d')
            elif 'date_serv' in anc03:
                d = datetime.strptime(anc03['date_serv'], '%Y%m%d')
                nd = d - timedelta(days=56)
                return nd.strftime('%Y%m%d')
            elif 'date_serv' in anc04:
                d = datetime.strptime(anc04['date_serv'], '%Y%m%d')
                nd = d - timedelta(days=98)
                return nd.strftime('%Y%m%d')
            elif 'date_serv' in anc05:
                d = datetime.strptime(anc05['date_serv'], '%Y%m%d')
                nd = d - timedelta(days=140)
                return nd.strftime('%Y%m%d')
            else:
                return None
        elif t == '3':
            if 'date_serv' in anc01:
                d = datetime.strptime(anc01['date_serv'], '%Y%m%d')
                nd = d + timedelta(days=98)
                return nd.strftime('%Y%m%d')
            elif 'date_serv' in anc02:
                d = datetime.strptime(anc02['date_serv'], '%Y%m%d')
                nd = d + timedelta(days=56)
                return nd.strftime('%Y%m%d')
            elif 'date_serv' in anc04:
                d = datetime.strptime(anc04['date_serv'], '%Y%m%d')
                nd = d - timedelta(days=42)
                return nd.strftime('%Y%m%d')
            elif 'date_serv' in anc05:
                d = datetime.strptime(anc05['date_serv'], '%Y%m%d')
                nd = d - timedelta(days=84)
                return nd.strftime('%Y%m%d')
            else:
                return None
        elif t == '4':
            if 'date_serv' in anc01:
                d = datetime.strptime(anc01['date_serv'], '%Y%m%d')
                nd = d + timedelta(days=140)
                return nd.strftime('%Y%m%d')
            elif 'date_serv' in anc02:
                d = datetime.strptime(anc02['date_serv'], '%Y%m%d')
                nd = d + timedelta(days=98)
                return nd.strftime('%Y%m%d')
            elif 'date_serv' in anc03:
                d = datetime.strptime(anc03['date_serv'], '%Y%m%d')
                nd = d + timedelta(days=42)
                return nd.strftime('%Y%m%d')
            elif 'date_serv' in anc05:
                d = datetime.strptime(anc05['date_serv'], '%Y%m%d')
                nd = d - timedelta(days=42)
                return nd.strftime('%Y%m%d')
            else:
                return None
        elif t == '5':
            if 'date_serv' in anc01:
                d = datetime.strptime(anc01['date_serv'], '%Y%m%d')
                nd = d + timedelta(days=182)
                return nd.strftime('%Y%m%d')
            elif 'date_serv' in anc02:
                d = datetime.strptime(anc02['date_serv'], '%Y%m%d')
                nd = d + timedelta(days=140)
                return nd.strftime('%Y%m%d')
            elif 'date_serv' in anc03:
                d = datetime.strptime(anc03['date_serv'], '%Y%m%d')
                nd = d + timedelta(days=84)
                return nd.strftime('%Y%m%d')
            elif 'date_serv' in anc04:
                d = datetime.strptime(anc04['date_serv'], '%Y%m%d')
                nd = d + timedelta(days=42)
                return nd.strftime('%Y%m%d')
            else:
                return None
        else:
            return None

    def get_anc_detail(self, hospcode, pid, gravida, ancno):
        self.request.db['anc'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('gravida', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('ga', pymongo.ASCENDING)

        rs = self.request.db['anc'].find_one({
            'hospcode': hospcode,
            'pid': pid,
            'gravida': gravida,
            'ancno': ancno
        })

        #print(rs)
        return rs if rs else []

    def is_labor(self, hospcode, pid, gravida):
        self.request.db['labor'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['labor'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['labor'].ensure_index('gravida', pymongo.ASCENDING)

        total = self.request.db['labor'].find({
            'hospcode': hospcode,
            'pid': pid,
            'gravida': gravida
        }).count()

        return 1 if total > 0 else 0

    def search_by_cid(self, cid, hospcode):

        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({'hospcode': hospcode, 'cid': cid})
        return rs

    def search_by_pid(self, pid, hospcode):
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('pid', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({'hospcode': hospcode, 'pid': pid})
        return rs

    def get_anc_count(self, pid, hospcode, gravida):

        self.request.db['anc'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['anc'].ensure_index('gravida', pymongo.ASCENDING)

        rs = self.request.db['anc'].find({
            'pid': pid,
            'hospcode': hospcode,
            'gravida': gravida
        }).count()

        return rs

    def get_list_map_anc(self, hospcode, by, start, limit):

        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('bdate', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
            'hospcode': hospcode,
            'is_labor': by,
            'typearea': {'$in': ['1', '3']}
        }).skip(start).limit(limit)

        return rs

    def get_list_map_anc_by_vid(self, hospcode, hids, by, start, limit):

        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('bdate', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
            'hospcode': hospcode,
            'is_labor': by,
            'hid': {'$in': hids},
            'typearea': {'$in': ['1', '3']}
        }).skip(start).limit(limit)

        return rs

    def get_list_map_anc_total(self, hospcode, by):

        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('bdate', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
            'hospcode': hospcode,
            'is_labor': by,
            'typearea': {'$in': ['1', '3']}
        }).count()

        return rs

    def get_list_map_anc_total_by_vid(self, hospcode, hids, by):

        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('bdate', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('hid', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
            'hospcode': hospcode,
            'is_labor': by,
            'hid': {'$in': hids},
            'typearea': {'$in': ['1', '3']}
        }).count()

        return rs     
        
    def get_list_map_anc_all(self, hospcode, by):

        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('bdate', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
            'hospcode': hospcode,
            'is_labor': by,
            'typearea': {'$in': ['1', '3']}
        })

        pids = []
        for r in rs:
            pids.append(r['pid'])

        return pids

    def get_list_map_anc_all_by_vid(self, hospcode, hids, by):

        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('bdate', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('bdate', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
            'hospcode': hospcode,
            'is_labor': by,
            'hid': {'$in': hids},
            'typearea': {'$in': ['1', '3']}
        })

        pids = []
        for r in rs:
            pids.append(r['pid'])

        return pids
        
    def get_pid_from_anc(self, hospcode):
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('pid', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find(
            {
                'hospcode': hospcode,
                'typearea': {'$in': ['1', '3']}
            })

        pids = []
        for r in rs:
            pids.append(r['pid'])

        return pids

    def get_anc_in_village(self, hospcode, hid):

        rs = self.request.db['anc_coverages'].find({
            'hid': {'$in': hid},
            'hospcode': hospcode,
            'typearea': {'$in': ['1', '3']}
        })

        return rs

    def get_all_latlng(self, hospcode, pids):

        self.request.db['home'].ensure_index('hid', pymongo.ASCENDING)
        self.request.db['home'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('bdate', pymongo.ASCENDING)
        
        hids = []
        for p in pids:
            h = self.get_hid_from_pid(hospcode, p)
            hids.append(h)
            
        rs = self.request.db['home'].find({
            'hospcode': hospcode,
            'hid': {'$in': hids}
        })
        
        data = [pids, hids]

        return data
        
    def get_latlng_from_pid(self, pid, hospcode):
        self.request.db['person'].ensure_index('pid', pymongo.ASCENDING)
        
        rs = self.request.db['person'].find_one({'pid': pid, 'hospcode': hospcode})
        hid = rs['hid']
        
        hrs = self.request.db['home'].find_one({'hospcode': hospcode, 'hid': hid})
        
        return hrs['loc'] if hrs else [None, None]

    def get_hid_from_pid(self, hospcode, pid):
        self.request.db['person'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['person'].ensure_index('hospcode', pymongo.ASCENDING)
        
        rs = self.request.db['person'].find_one({
            'hospcode': hospcode,
            'pid': pid
        })

        return rs['hid']
        
    def get_prenatal_all(self, hospcode, pid):

        self.request.db['prenatal'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['prenatal'].ensure_index('pid', pymongo.ASCENDING)

        rs = self.request.db['prenatal'].find({
            'hospcode': hospcode,
            'pid': pid
        })

        if rs:
            return rs
        else:
            return None

    def get_anc_coverages(self, hospcode, start, limit):
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('typearea', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
                'hospcode': hospcode,
                'typearea': {'$in': ['1', '3']},
                'total': {
                    '$gte': 5
                }
        }).skip(start).limit(limit)

        return rs

    def get_anc_coverages_all(self, hospcode, start, limit):
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('typearea', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
                'hospcode': hospcode,
                'typearea': {'$in': ['1', '3']}
        }).skip(start).limit(limit)

        return rs

    def get_anc_not_coverages(self, hospcode, start, limit):
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('typearea', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
                'hospcode': hospcode,
                'typearea': {'$in': ['1', '3']},
                'total': {'$lt': 5}
        }).skip(start).limit(limit)

        return rs

    def get_anc_coverages_count(self, hospcode):
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('typearea', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
                'hospcode': hospcode,
                'typearea': {'$in': ['1', '3']},
                'total': {'$gte': 5}
        }).count()

        return rs

    def get_anc_coverages_all_count(self, hospcode):
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('typearea', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
                'hospcode': hospcode,
                'typearea': {'$in': ['1', '3']}
        }).count()

        return rs

    def get_anc_not_coverages_count(self, hospcode):
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('typearea', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
                'hospcode': hospcode,
                'typearea': {'$in': ['1', '3']},
                'total': {'$lt': 5}
        }).count()

        return rs

    def search_anc_coverages(self, hospcode, cid):
        self.request.db['anc_coverages'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_coverages'].ensure_index('typearea', pymongo.ASCENDING)

        rs = self.request.db['anc_coverages'].find({
                'hospcode': hospcode,
                'typearea': {'$in': ['1', '3']},
                #'total': {'$lt': 5}
                'cid': cid
        })

        return rs

    def do_process_12weeks(self, hospcode):

        reducer = Code("""
                function(curr, result) {
                    //curr.ga;
                }
        """)

        data = self.request.db['anc'].group(
            key={
                'hospcode': 1,
                'pid': 1,
                'gravida': 1
            },
            condition={
                'hospcode': hospcode,
                'ga': {'$lte': '12'}
            },
            initial={},
            reduce=reducer)

        if data:

            self.request.db['anc_12weeks'].remove({'hospcode': hospcode})

            try:
                person = PersonModel(self.request)

                for i in data:

                    p = person.get_person_detail(i['pid'], i['hospcode'])
                    doc = {
                        'hospcode': i['hospcode'],
                        'pid': i['pid'],
                        'cid': p['cid'],
                        'gravida': i['gravida'],
                        'typearea': p['typearea']
                    }

                    self.request.db['anc_12weeks'].insert(doc)

                return True
            except Exception as ex:
                #print(ex.message)
                return False

        else:
            return False

    def get_anc_12ws_list(self, hospcode, start, limit):
        self.request.db['anc_12weeks'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_12weeks'].ensure_index('typearea', pymongo.ASCENDING)

        rs = self.request.db['anc_12weeks'].find({
                'hospcode': hospcode,
                'typearea': {'$in': ['1', '3']}
        }).skip(start).limit(limit)

        return rs

    def get_anc_12ws_total(self, hospcode):
        self.request.db['anc_12weeks'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_12weeks'].ensure_index('typearea', pymongo.ASCENDING)

        rs = self.request.db['anc_12weeks'].find({
                'hospcode': hospcode,
                'typearea': {'$in': ['1', '3']}
        }).count()

        return rs

    def count_risk01(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch1': '1'
        }).count()

        return rs

    def count_risk02(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch2': '1'
        }).count()

        return rs

    def count_risk03(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch3': '1'
        }).count()

        return rs

    def count_risk04(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch4': '1'
        }).count()

        return rs

    def count_risk05(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch5': '1'
        }).count()

        return rs

    def count_risk06(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch6': '1'
        }).count()

        return rs

    def count_risk07(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch7': '1'
        }).count()

        return rs

    def count_risk08(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch8': '1'
        }).count()

        return rs

    def count_risk09(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch9': '1'
        }).count()

        return rs

    def count_risk10(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch10': '1'
        }).count()

        return rs

    def count_risk11(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch11': '1'
        }).count()

        return rs

    def count_risk12(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch12': '1'
        }).count()

        return rs

    def count_risk13(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch13': '1'
        }).count()

        return rs

    def count_risk14(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch14': '1'
        }).count()

        return rs

    def count_risk15(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch15': '1'
        }).count()

        return rs

    def count_risk16(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch16': '1'
        }).count()

        return rs

    def count_risk17(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch17': '1'
        }).count()

        return rs

    def count_risk18(self, hospcode, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            },
            'ch18': '1'
        }).count()

        return rs

    def get_risk_list_by_type(self, hospcode, choice, start_date, end_date):
        self.request.db['anc_survey'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['anc_survey'].ensure_index('last_update', pymongo.ASCENDING)

        rs = self.request.db['anc_survey'].find({
            'hospcode': hospcode,
            str(choice): '1',
            'last_update': {
                '$gte': start_date,
                '$lte': end_date
            }
        })

        return rs