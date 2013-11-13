# -*- coding: utf8

import datetime
import pymongo


class ICHelper:

    def to_thai_date(self, eng_date):
        try:
            y = int(eng_date[:4])
            yt = str(y + 543)
            m = eng_date[4:6]
            d = eng_date[6:8]

            return d + '/' + m + '/' + yt

        except:
            return '-'

    def count_age(self, eng_date, current_date=''):
        try:
            yb = int(eng_date[:4])
            mb = int(eng_date[4:6])
            db = int(eng_date[6:8])

            if len(current_date) > 0:
                yc = int(current_date[:4])
                mc = int(current_date[4:6])
                dc = int(current_date[6:8])
            else:
                yc = int(datetime.date.today().year)
                mc = int(datetime.date.today().month)
                dc = int(datetime.date.today().day)

            if dc >= db:
                age_d = dc - db
            else:
                (mc, dc) = (mc - 1, dc + 30)
                age_d = dc - db

            if mc >= mb:
                age_m = mc - mb
            else:
                (yc, mc) = (yc - 1, mc + 12)
                age_m = mc - mb

            age_y = yc - yb

            age = {
                'year': age_y,
                'month': age_m,
                'day': age_d
            }
            return age
        except TypeError:
            age = {
                'year': 0,
                'month': 0,
                'day': 0
            }
            return age
            
    def get_position_list(self, request):
        rs = request.db['ref_positions'].find()
        if rs:
            rows = []
            for r in rs:
                obj = {
                    'id': r['_id'],
                    'name': r['name']
                }
                
                rows.append(obj)
            
            return rows
        else:
            return []

    def get_hospital_list(self, request):

        rs = request.db['ref_hospitals'].find({'changwat': '44'})
        if rs:
            rows = []
            for r in rs:
                obj = {
                    'id': r['_id'],
                    'hospname': r['hospname'],
                    'hospcode': r['hospcode']
                }

                rows.append(obj)
            return rows
        else:
            return []


    def get_position_grade_list(self, request):
        rs = request.db['ref_position_grades'].find()
        if rs:
            rows = []
            for r in rs:
                obj = {
                    'id': r['_id'],
                    'name': r['name']
                }
                
                rows.append(obj)
            
            return rows
        else:
            return []
            
    def get_code506_list(self, request):

        request.db['ref_code506'].ensure_index('code', pymongo.ASCENDING)

        rs = request.db['ref_code506'].find().sort('code', pymongo.ASCENDING)

        if rs:
            rows = []
            for r in rs:
                obj = {
                    'code': r['code'],
                    'name': r['name']
                }
                rows.append(obj)

            return rows

    def get_hospital_name(self, request, hospcode=''):

        rs = request.db['ref_hospitals'].find_one({'hospcode': hospcode})
        return rs['hospname'] if rs else '-'

    #Get position name
    def get_position_name(self, request, id):
        rs = request.db['ref_positions'].find_one({'_id': id})
        return rs['name'] if rs else '-'
    
    #Get position grade
    def get_position_grade_name(self, request, id):
        rs = request.db['ref_position_grades'].find_one({'_id': id})
        return rs['name'] if rs else '-'
        
    def get_complication_name(self, request, code=''):

        rs = request.db['ref_complication'].find_one({'code': code})
        return rs['name'] if rs else '-'

    def get_code506_name(self, request, code=''):

        rs = request.db['ref_code506'].find_one({'code': code})
        return rs['name'] if rs else '-'

    def get_diag_name(self, request, diagcode=''):

        request.db['ref_icd10'].ensure_index('code', pymongo.ASCENDING)

        rs = request.db['ref_icd10'].find_one({'code': diagcode})
        return rs['desc_r'] if rs else '-'

    def get_aptype(self, request, aptype=''):
        request.db['ref_appoint_types'].ensure_index('export_code', pymongo.ASCENDING)

        rs = request.db['ref_appoint_types'].find_one({'export_code': aptype})
        return rs['name'] if rs else '-'

    def get_village_name(self, request, vid):

        request.db['ref_catms'].ensure_index('changwat', pymongo.ASCENDING)
        request.db['ref_catms'].ensure_index('ampur', pymongo.ASCENDING)
        request.db['ref_catms'].ensure_index('tambon', pymongo.ASCENDING)
        request.db['ref_catms'].ensure_index('moo', pymongo.ASCENDING)

        if len(vid) == 8:
            chw = vid[:2]
            amp = vid[2:4]
            tmb = vid[4:6]
            moo = vid[6:8]
            #changwat: '44', ampur: '04', tambon: '01', moo: '00'
            rs = request.db['ref_catms'].find_one({
                'changwat': chw,
                'ampur': amp,
                'tambon': tmb,
                'moo': moo
            })

            return rs['catm_name'] if rs else '-'
        else:
            return '-'

    def get_villages(self, request, hospcode):

        request.db['village'].ensure_index('hospcode', pymongo.ASCENDING)
        request.db['village'].ensure_index('vid', pymongo.ASCENDING)

        rs = request.db['village'].find({
            'hospcode': hospcode
        }, {'vid': 1}).sort('vid', pymongo.ASCENDING)

        if rs:
            rows = []
            for r in rs:
                obj = {
                    'vid': r['vid'],
                    'name': self.get_village_name(request, r['vid'])
                }
                rows.append(obj)

            return rows

    def get_chw(self, request, chw):

        request.db['ref_catms'].ensure_index('changwat', pymongo.ASCENDING)
        request.db['ref_catms'].ensure_index('ampur', pymongo.ASCENDING)
        request.db['ref_catms'].ensure_index('tambon', pymongo.ASCENDING)
        request.db['ref_catms'].ensure_index('moo', pymongo.ASCENDING)

        rs = request.db['ref_catms'].find_one({
                'changwat': chw,
                'ampur': '00',
                'tambon': '00',
                'moo': '00'
        })
        if rs:
            return rs['catm_name'] if rs else '-'
        else:
            return '-'

    def get_amp(self, request, chw, amp):

        request.db['ref_catms'].ensure_index('changwat', pymongo.ASCENDING)
        request.db['ref_catms'].ensure_index('ampur', pymongo.ASCENDING)
        request.db['ref_catms'].ensure_index('tambon', pymongo.ASCENDING)
        request.db['ref_catms'].ensure_index('moo', pymongo.ASCENDING)

        rs = request.db['ref_catms'].find_one({
                'changwat': chw,
                'ampur': amp,
                'tambon': '00',
                'moo': '00'
        })
        if rs:
            return rs['catm_name'] if rs else '-'
        else:
            return '-'

    def get_tmb(self, request, chw, amp, tmb):

        request.db['ref_catms'].ensure_index('changwat', pymongo.ASCENDING)
        request.db['ref_catms'].ensure_index('ampur', pymongo.ASCENDING)
        request.db['ref_catms'].ensure_index('tambon', pymongo.ASCENDING)
        request.db['ref_catms'].ensure_index('moo', pymongo.ASCENDING)

        rs = request.db['ref_catms'].find_one({
                'changwat': chw,
                'ampur': amp,
                'tambon': tmb,
                'moo': '00'
        })
        if rs:
            return rs['catm_name'] if rs else '-'
        else:
            return '-'

    def get_address(self, request, hid, hospcode):

        #get detail from home
        home = request.db['home'].find_one({
            'hid': hid,
            'hospcode': hospcode
        })

        if home:
            try:
                chw = home['changwat']
                amp = home['ampur']
                tmb = home['tambon']
                moo = home['village']
                address = home['house']

                chw_name = self.get_chw(request, chw)
                amp_name = self.get_amp(request, chw, amp)
                tmb_name = self.get_tmb(request, chw, amp, tmb)

                full_address = u'%s หมู่ %s ต.%s อ.%s จ.%s' % (address, moo, tmb_name, amp_name, chw_name)

                return full_address
            except:
                return '-'

        else:
            return '-'

    def get_address_from_catm(self, request, catm):

        if catm:

            chw = catm[:2]
            amp = catm[2:4]
            tmb = catm[4:6]
            moo = catm[6:8]

            chw_name = self.get_chw(request, chw)
            amp_name = self.get_amp(request, chw, amp)
            tmb_name = self.get_tmb(request, chw, amp, tmb)

            full_address = u'หมู่ %s ต.%s อ.%s จ.%s' % (moo, tmb_name, amp_name, chw_name)

            return full_address

        else:
            return '-'

    def get_short_address(self, request, hid, hospcode):

        #get detail from home
        home = request.db['home'].find_one({
            'hid': hid,
            'hospcode': hospcode
        })

        if home:

            chw = home['changwat']
            amp = home['ampur']
            tmb = home['tambon']
            moo = home['village']
            address = home['house']

            #chw_name = self.get_chw(request, chw)
            #amp_name = self.get_amp(request, chw, amp)
            #tmb_name = self.get_tmb(request, chw, amp, tmb)

            full_address = u'%s หมู่ %s' % (address, moo)

            return full_address

        else:
            return '-'

    def get_vaccine_name(self, request, code):
        rs = request.db['ref_epi_vaccines'].find_one({'export_code': code})
        return rs['eng_name'] if rs else '-'