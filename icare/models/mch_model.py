# -*- coding: utf8
import pymongo
from datetime import datetime
from datetime import timedelta


class MchModel:

    def __init__(self, request):
        self.request = request

    def get_list(self, hospcode, start, limit):

        self.request.db['labor'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['labor'].ensure_index('bdate', pymongo.ASCENDING)

        rs = self.request.db['labor'].find({'hospcode': hospcode}).\
            sort('bdate', pymongo.ASCENDING).skip(start).limit(limit)

        return rs

    def search(self, hospcode, cid):

        self.request.db['labor'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['labor'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['labor'].find({
            'hospcode': hospcode,
            'cid': cid
        })

        return rs

    def get_list_total(self, hospcode):

        self.request.db['labor'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['labor'].find({'hospcode': hospcode}).count()
        return rs

    def get_postnatal(self, pid, gravida, hospcode):

        self.request.db['postnatal'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['postnatal'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['postnatal'].ensure_index('gravida', pymongo.ASCENDING)

        rs = self.request.db['postnatal'].find({
            'pid': pid,
            'hospcode': hospcode,
            'gravida': gravida
        }).sort('ppcare', pymongo.ASCENDING)

        return rs

    def get_postnatal_all(self, cid, gravida):

        self.request.db['postnatal'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['postnatal'].ensure_index('cid', pymongo.ASCENDING)
        self.request.db['postnatal'].ensure_index('gravida', pymongo.ASCENDING)

        rs = self.request.db['postnatal'].find({
            'cid': cid,
            'gravida': gravida
        }).sort('ppcare', pymongo.ASCENDING)

        return rs

    def get_count_postnatal(self, pid, gravida, hospcode):

        self.request.db['postnatal'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['postnatal'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['postnatal'].ensure_index('gravida', pymongo.ASCENDING)

        rs = self.request.db['postnatal'].find({
            'pid': pid,
            'hospcode': hospcode,
            'gravida': gravida
        }).count()

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

    def get_appointment(self, pid, hospcode, seq):
        self.request.db['appointment'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['appointment'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['appointment'].ensure_index('seq', pymongo.ASCENDING)

        rs = self.request.db['appointment'].find({
            'pid': pid,
            'hospcode': hospcode,
            'seq': seq
        })

        return rs

    def do_process_forecast(self, hospcode):
        self.request.db['labor'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.get_labor_list(hospcode)

        if rs:
            for r in rs:

                date = []
                pcares = []

                pcare = self.get_labor_forecast_detail(r['hospcode'], r['pid'], r['gravida'])
                if pcare:
                    for p in pcare:
                        date.append(p['ppcare'])

                date.sort()

                #first <= (birth + 7)
                #second >= (birth + 8) <= 15
                #third >= (birth + 16) <= 45

                #have one record
                if len(date) == 1:
                    birth = datetime.strptime(r['bdate'], '%Y%m%d')
                    cc = datetime.strptime(date[0], '%Y%m%d')

                    diff_date = cc - birth
                    if 1 <= diff_date.days <= 7:
                        care1 = datetime.strptime(date[0], '%Y%m%d')
                        care2 = birth + timedelta(days=8)
                        care3 = birth + timedelta(days=16)

                        care1 = datetime.strftime(care1, '%Y%m%d')
                        care2 = datetime.strftime(care2, '%Y%m%d')
                        care3 = datetime.strftime(care3, '%Y%m%d')

                        obj = [
                            {'care1': care1, 'is_forecast': 'N'},
                            {'care2': care2, 'is_forecast': 'Y'},
                            {'care3': care3, 'is_forecast': 'Y'}
                        ]

                    elif 8 <= diff_date.days <= 15:
                        care1 = birth + timedelta(days=7)
                        care2 = datetime.strptime(date[0], '%Y%m%d')
                        care3 = birth + timedelta(days=16)

                        care1 = datetime.strftime(care1, '%Y%m%d')
                        care2 = datetime.strftime(care2, '%Y%m%d')
                        care3 = datetime.strftime(care3, '%Y%m%d')

                        obj = [
                            {'care1': care1, 'is_forecast': 'Y'},
                            {'care2': care2, 'is_forecast': 'N'},
                            {'care3': care3, 'is_forecast': 'Y'}
                        ]

                    elif 16 <= diff_date.days <= 45:
                        care1 = birth + timedelta(days=7)
                        care2 = birth + timedelta(days=8)
                        care3 = datetime.strptime(date[0], '%Y%m%d')

                        care1 = datetime.strftime(care1, '%Y%m%d')
                        care2 = datetime.strftime(care2, '%Y%m%d')
                        care3 = datetime.strftime(care3, '%Y%m%d')

                        obj = [
                            {'care1': care1, 'is_forecast': 'Y'},
                            {'care2': care2, 'is_forecast': 'Y'},
                            {'care3': care3, 'is_forecast': 'N'}
                        ]

                    else:
                        care1 = birth + timedelta(days=7)
                        care2 = birth + timedelta(days=8)
                        care3 = birth + timedelta(days=16)

                        care1 = datetime.strftime(care1, '%Y%m%d')
                        care2 = datetime.strftime(care2, '%Y%m%d')
                        care3 = datetime.strftime(care3, '%Y%m%d')

                        obj = [
                            {'care1': care1, 'is_forecast': 'Y'},
                            {'care2': care2, 'is_forecast': 'Y'},
                            {'care3': care3, 'is_forecast': 'Y'}
                        ]

                    pcares.append(obj)

                #have two records
                elif len(date) == 2:
                    birth = datetime.strptime(r['bdate'], '%Y%m%d')
                    cc1 = datetime.strptime(date[0], '%Y%m%d')
                    cc2 = datetime.strptime(date[1], '%Y%m%d')

                    diff_date1 = cc1 - birth
                    diff_date2 = cc2 - birth

                    #find care1

                    if 1 <= diff_date1.days <= 7:
                        care1 = datetime.strptime(date[0], '%Y%m%d')

                        care2 = datetime.strptime(date[1], '%Y%m%d') if 1 <= (diff_date2 - diff_date1).days <= 8 else birth + timedelta(days=8)
                        care3 = datetime.strptime(date[1], '%Y%m%d') if 9 <= (diff_date2 - diff_date1).days <= 16 else birth + timedelta(days=16)
                        #care2 = birth + timedelta(days=8)
                        #care3 = birth + timedelta(days=16)

                        care1 = datetime.strftime(care1, '%Y%m%d')
                        care2 = datetime.strftime(care2, '%Y%m%d')
                        care3 = datetime.strftime(care3, '%Y%m%d')

                        obj = [
                            {'care1': care1, 'is_forecast': 'N'},
                            {'care2': care2, 'is_forecast': 'Y'},
                            {'care3': care3, 'is_forecast': 'Y'}
                        ]

                    elif 8 <= diff_date1.days <= 15:
                        care1 = birth + timedelta(days=7)
                        care2 = datetime.strptime(date[0], '%Y%m%d')
                        care3 = date[1]
                        #care3 = birth + timedelta(days=16)

                        care1 = datetime.strftime(care1, '%Y%m%d')
                        care2 = datetime.strftime(care2, '%Y%m%d')
                        care3 = datetime.strftime(care3, '%Y%m%d')

                        obj = [
                            {'care1': care1, 'is_forecast': 'Y'},
                            {'care2': care2, 'is_forecast': 'N'},
                            {'care3': care3, 'is_forecast': 'Y'}
                        ]

                    elif 16 <= diff_date1.days <= 45:
                        care1 = birth + timedelta(days=7)
                        care2 = birth + timedelta(days=8)
                        care3 = datetime.strptime(date[0], '%Y%m%d')

                        care1 = datetime.strftime(care1, '%Y%m%d')
                        care2 = datetime.strftime(care2, '%Y%m%d')
                        care3 = datetime.strftime(care3, '%Y%m%d')

                        obj = [
                            {'care1': care1, 'is_forecast': 'Y'},
                            {'care2': care2, 'is_forecast': 'Y'},
                            {'care3': care3, 'is_forecast': 'N'}
                        ]

                    else:
                        care1 = birth + timedelta(days=7)
                        care2 = birth + timedelta(days=8)
                        care3 = birth + timedelta(days=16)

                        care1 = datetime.strftime(care1, '%Y%m%d')
                        care2 = datetime.strftime(care2, '%Y%m%d')
                        care3 = datetime.strftime(care3, '%Y%m%d')

                        obj = [
                            {'care1': care1, 'is_forecast': 'Y'},
                            {'care2': care2, 'is_forecast': 'Y'},
                            {'care3': care3, 'is_forecast': 'Y'}
                        ]

                    pcares.append(obj)
                #have tree records
                elif len(date) == 3:
                    care1 = datetime.strptime(date[0], '%Y%m%d')
                    care2 = datetime.strptime(date[1], '%Y%m%d')
                    care3 = datetime.strptime(date[2], '%Y%m%d')

                    care1 = datetime.strftime(care1, '%Y%m%d')
                    care2 = datetime.strftime(care2, '%Y%m%d')
                    care3 = datetime.strftime(care3, '%Y%m%d')

                    obj = [
                        {'care1': care1, 'is_forecast': 'Y'},
                        {'care2': care2, 'is_forecast': 'Y'},
                        {'care3': care3, 'is_forecast': 'Y'}
                    ]

                    pcares.append(obj)

                self.update_pcare(r['hospcode'], r['pid'], r['gravida'], pcares)

    def update_pcare(self, hospcode, pid, gravida, pcares):
        self.request.db['labor'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['labor'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['labor'].ensure_index('gravida', pymongo.ASCENDING)

        self.request.db['labor'].update({
            'hospcode': hospcode,
            'pid': pid,
            'gravida': gravida
        }, {
            '$set': {
                'pcares': pcares
            }
        })

    def get_labor_forecast_detail(self, hospcode, pid, gravida):
        self.request.db['postnatal'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['postnatal'].ensure_index('pid', pymongo.ASCENDING)
        self.request.db['postnatal'].ensure_index('gravida', pymongo.ASCENDING)

        rs = self.request.db['postnatal'].find({
            'hospcode': hospcode,
            'pid': pid,
            'gravida': gravida
        })

        return rs if rs else []

    def get_labor_list(self, hospcode):
        self.request.db['labor'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['labor'].find({
            'hospcode': hospcode
        })

        return rs
"""
    def get_forecast(self, care1, care2, care3, t):
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

"""