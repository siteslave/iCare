# -*- coding: utf8
from datetime import datetime
from pyramid.view import (
    view_config,
)
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPUnauthorized,
)

from icare.models.anc_model import AncModel
from icare.models.mch_model import MchModel
from icare.models.person_model import PersonModel
from icare.models.home_model import HomeModel
from icare.helpers.icare_helper import ICHelper

h = ICHelper()


@view_config(
    route_name='anc_index',
    renderer='anc.mako')
def index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.session['user_type'] == '1':
            return HTTPFound(location='/admins')
            
        return {'title': u'ข้อมูลการฝากครรภ์'}


@view_config(route_name='anc_get_list_total', renderer='json')
def get_list_total(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        anc = AncModel(request)
        try:
            total = anc.get_list_total()
            return {'ok': 1, 'total': total}
        except Exception as e:
            return {'ok': 0, 'msg': e.message}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='anc_get_list', request_method='POST', renderer='json')
def get_list(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:  # is ajax request
            start = request.params['start'] if 'start' in request.params else 0
            stop = request.params['stop'] if 'stop' in request.params else 25

            limit = int(stop) - int(start)

            anc = AncModel(request)
            person = PersonModel(request)

            rs = anc.get_list(int(start), int(limit))

            rows = []
            if rs:
                for r in rs:
                    labor = anc.get_labor_detail(r['pid'], r['gravida'], r['hospcode'])
                    prenatal = anc.get_prenatal_detail(r['pid'], r['gravida'], r['hospcode'])
                    p = person.get_person_detail(r['pid'], r['hospcode'])

                    bdate = h.to_thai_date(labor['bdate']) if labor else '-'
                    edc = h.to_thai_date(prenatal['edc']) if prenatal else '-'
                    lmp = h.to_thai_date(prenatal['lmp']) if prenatal else '-'

                    obj = {
                        'pid': r['pid'],
                        'cid': r['cid'],
                        'hospcode': r['hospcode'],
                        'gravida': r['gravida'],
                        'fullname': p['name'] + '  ' + p['lname'],
                        'cid': p['cid'],
                        'birth': h.to_thai_date(p['birth']),
                        'age': h.count_age(p['birth'], anc.get_first_anc(p['pid'], r['gravida'], r['hospcode'])),
                        'first_visit': h.to_thai_date(anc.get_first_anc(p['pid'], r['gravida'], r['hospcode'])),
                        'last_visit': h.to_thai_date(anc.get_last_anc(p['pid'], r['gravida'], r['hospcode'])),
                        'bdate': bdate,
                        'edc': edc,
                        'lmp': lmp,
                        'anc_count': anc.get_anc_count(r['pid'], r['hospcode'], r['gravida']),
                        'is_survey': anc.get_survey_status(r['pid'], r['gravida'], r['hospcode']),
                    }
                    rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='anc_get_visit', request_method='POST', renderer='json')
def get_visit(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.is_xhr:
        cid = request.params['query']
        start = request.params['start']
        stop = request.params['stop']

        limit = int(stop) - int(start)

        csrf_token = request.params['csrf_token']

        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:
            anc = AncModel(request)
            mch = MchModel(request)

            visit = anc.get_visit_list(cid, int(start), int(limit))
            rows = []

            for v in visit:
                labor = anc.get_labor_detail(v['pid'], v['gravida'], v['hospcode'])
                is_labor = 1 if labor else 0

                obj = {
                    'pid': v['pid'],
                    'cid': v['cid'],
                    'seq': v['seq'],
                    'date_serv': h.to_thai_date(v['date_serv']),
                    'gravida': v['gravida'],
                    'ancno': v['ancno'],
                    'ga': v['ga'],
                    'ancresult': v['ancresult'],
                    'hospcode': v['hospcode'],
                    'hospname': h.get_hospital_name(request, v['hospcode']),
                    'is_survey': anc.get_survey_status(v['pid'], v['gravida'], v['hospcode']),
                    'is_labor': is_labor,
                    'appoint': mch.count_appointment(v['pid'], v['hospcode'], v['seq'])
                }

                rows.append(obj)

            return {'ok': 1, 'rows': rows}
        else:
            return {'ok': 0, 'msg': 'Not authorized.'}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='anc_get_visit_total', renderer='json')
def get_visit_total(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.is_xhr:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:
            cid = request.params['query']
            anc = AncModel(request)

            try:
                total = anc.get_visit_list_total(cid)
                return {'ok': 1, 'total': total}
            except Exception as e:
                return {'ok': 0, 'msg': e.message}
        else:
            return {'ok': 0, 'msg': 'Not authorized.'}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='anc_do_process', renderer='json')
def do_process(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.is_xhr:
        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:
            anc = AncModel(request)
            rs = anc.do_process_list(request.session['hospcode'])

            return {'ok': 1} if rs else {'ok': 0, 'msg': 'ไม่สามารถประมวลผลได้'}


@view_config(route_name='anc_do_process_12weeks', renderer='json')
def anc_do_process_12weeks(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.is_xhr:
        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:
            anc = AncModel(request)
            rs = anc.do_process_12weeks(request.session['hospcode'])

            return {'ok': 1} if rs else {'ok': 0, 'msg': 'ไม่สามารถประมวลผลได้'}


@view_config(route_name='anc_save_survey', renderer='json')
def save_survey(request):

    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.is_xhr:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:
            ch1 = request.params['ch1']
            ch2 = request.params['ch2']
            ch3 = request.params['ch3']
            ch4 = request.params['ch4']
            ch5 = request.params['ch5']
            ch6 = request.params['ch6']
            ch7 = request.params['ch7']
            ch8 = request.params['ch8']
            ch9 = request.params['ch9']
            ch10 = request.params['ch10']
            ch11 = request.params['ch11']
            ch12 = request.params['ch12']
            ch13 = request.params['ch13']
            ch14 = request.params['ch14']
            ch15 = request.params['ch15']
            ch16 = request.params['ch16']
            ch17 = request.params['ch17']
            ch18 = request.params['ch18']
            pid = request.params['pid']
            gravida = request.params['gravida']
            other_ill = request.params['other_ill']

            is_risk = 'N'

            if ch1 == '1':
                is_risk = 'Y'
            elif ch2 == '1':
                is_risk = 'Y'
            elif ch3 == '1':
                is_risk = 'Y'
            elif ch4 == '1':
                is_risk = 'Y'
            elif ch5 == '1':
                is_risk = 'Y'
            elif ch6 == '1':
                is_risk = 'Y'
            elif ch7 == '1':
                is_risk = 'Y'
            elif ch8 == '1':
                is_risk = 'Y'
            elif ch9 == '1':
                is_risk = 'Y'
            elif ch10 == '1':
                is_risk = 'Y'
            elif ch11 == '1':
                is_risk = 'Y'
            elif ch12 == '1':
                is_risk = 'Y'
            elif ch13 == '1':
                is_risk = 'Y'
            elif ch14 == '1':
                is_risk = 'Y'
            elif ch15 == '1':
                is_risk = 'Y'
            elif ch16 == '1':
                is_risk = 'Y'
            elif ch17 == '1':
                is_risk = 'Y'
            elif ch18 == '1':
                is_risk = 'Y'
            else:
                is_risk = 'N'

            anc = AncModel(request)
            person = PersonModel(request)

            doc = {
                'ch1': ch1,
                'ch2': ch2,
                'ch3': ch3,
                'ch4': ch4,
                'ch5': ch5,
                'ch6': ch6,
                'ch7': ch7,
                'ch8': ch8,
                'ch9': ch9,
                'ch10': ch10,
                'ch11': ch11,
                'ch12': ch12,
                'ch13': ch13,
                'ch14': ch14,
                'ch15': ch15,
                'ch16': ch16,
                'ch17': ch17,
                'ch18': ch18,
                'is_risk': is_risk,
                'pid': pid,
                'other_ill': other_ill,
                'gravida': gravida,
                'cid': person.get_cid_from_pid(pid, request.session['hospcode']),
                'hospcode': request.session['hospcode'],
                'last_update': h.get_current_stringdate()
            }

            anc.save_survey(doc)

            return {'ok': 1}

        else:
            return {'ok': 0, 'msg': 'Not authorized.'}

    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='anc_get_labor', renderer='json')
def get_labor(request):

    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.is_xhr:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:
            cid = request.params['cid']
            gravida = request.params['gravida']

            anc = AncModel(request)
            person = PersonModel(request)

            r = anc.get_labor_detail_by_cid(cid, gravida, request.session['hospcode'])
            p = person.get_person_detail(r['pid'], request.session['hospcode'])

            if r:
                obj = {
                    'pid': r['pid'],
                    'cid': p['cid'],
                    'fullname': p['name'] + ' ' + p['lname'],
                    'birth': h.to_thai_date(p['birth']),
                    'edc': h.to_thai_date(r['edc']),
                    'lmp': h.to_thai_date(r['lmp']),
                    'bdate': h.to_thai_date(r['bdate']),
                    'bresultcode': r['bresult'],
                    'bresultname': h.get_diag_name(request, r['bresult']),
                    'bplace': r['bplace'],
                    'bhospcode': r['bhosp'],
                    'bhospname': h.get_hospital_name(request, r['bhosp']),
                    'btype': r['btype'],
                    'bdoctor': r['bdoctor'],
                    'lborn': r['lborn'],
                    'sborn': r['sborn'],
                    'gravida': r['gravida']
                }

                return {'ok': 1, 'rows': [obj]}
            else:
                return {'ok': 0, 'msg': u'ไม่พบรายการ'}


@view_config(route_name='anc_get_prenatal', renderer='json', request_method='POST')
def get_prenatal(request):

    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.is_xhr:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:
            pid = request.params['pid']
            gravida = request.params['gravida']
            hospcode = request.params['hospcode'] if 'hospcode' in request.params else request.session['hospcode']

            anc = AncModel(request)
            person = PersonModel(request)

            r = anc.get_prenatal_detail(pid, gravida, hospcode)
            p = person.get_person_detail(pid, hospcode)

            if r:
                obj = {
                    'pid': r['pid'],
                    'cid': p['cid'],
                    'fullname': p['name'] + ' ' + p['lname'],
                    'birth': h.to_thai_date(p['birth']),
                    'edc': h.to_thai_date(r['edc']),
                    'lmp': h.to_thai_date(r['lmp']),
                    'vdrl_result': r['vdrl_result'],
                    'hb_result': r['hb_result'],
                    'hiv_result': r['hiv_result'],
                    'date_hct': h.to_thai_date(r['date_hct']),
                    'hct_result': r['hct_result'],
                    'thalassemia': r['thalassemia'],
                    'gravida': r['gravida']
                }

                return {'ok': 1, 'rows': [obj]}
            else:
                return {'ok': 0, 'msg': u'ไม่พบรายการ'}


@view_config(route_name='anc_get_survey', renderer='json', request_method='POST')
def get_survey(request):

    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.is_xhr:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            pid = request.params['pid']
            gravida = request.params['gravida']
            hospcode = request.params['hospcode'] if 'hospcode' in request.params else request.session['hospcode']

            anc = AncModel(request)
            rs = anc.get_survey(pid, gravida, hospcode)

            if rs:
                obj = {
                    'ch1': rs['ch1'] if rs['ch1'] else None,
                    'ch2': rs['ch2'] if rs['ch2'] else None,
                    'ch3': rs['ch3'] if rs['ch3'] else None,
                    'ch4': rs['ch4'] if rs['ch4'] else None,
                    'ch5': rs['ch5'] if rs['ch5'] else None,
                    'ch6': rs['ch6'] if rs['ch6'] else None,
                    'ch7': rs['ch7'] if rs['ch7'] else None,
                    'ch8': rs['ch8'] if rs['ch8'] else None,
                    'ch9': rs['ch9'] if rs['ch9'] else None,
                    'ch10': rs['ch10'] if rs['ch10'] else None,
                    'ch11': rs['ch11'] if rs['ch11'] else None,
                    'ch12': rs['ch12'] if rs['ch12'] else None,
                    'ch13': rs['ch13'] if rs['ch13'] else None,
                    'ch14': rs['ch14'] if rs['ch14'] else None,
                    'ch15': rs['ch15'] if rs['ch15'] else None,
                    'ch16': rs['ch16'] if rs['ch16'] else None,
                    'ch17': rs['ch17'] if rs['ch17'] else None,
                    'ch18': rs['ch18'] if rs['ch18'] else None,
                    'other_ill': rs['other_ill'] if 'other_ill' in rs else None,
                }

                return {'ok': 1, 'rows': [obj]}
            else:
                return {'ok': 0, 'msg': u'ไม่พบรายการ'}


@view_config(route_name='anc_search', renderer='json', request_method='POST')
def search(request):

    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.is_xhr:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            anc = AncModel(request)
            person = PersonModel(request)

            query = request.params['query']
            if len(query) == 13:
                # search by cid
                rs = anc.search_by_cid(query, request.session['hospcode'])

            else:
                #search by pid
                rs = anc.search_by_pid(query, request.session['hospcode'])

            rows = []
            if rs:
                for r in rs:
                    labor = anc.get_labor_detail(r['pid'], r['gravida'], request.session['hospcode'])
                    prenatal = anc.get_prenatal_detail(r['pid'], r['gravida'], request.session['hospcode'])
                    p = person.get_person_detail(r['pid'], request.session['hospcode'])

                    bdate = h.to_thai_date(labor['bdate']) if labor else '-'
                    edc = h.to_thai_date(prenatal['edc']) if prenatal else '-'
                    lmp = h.to_thai_date(prenatal['lmp']) if prenatal else '-'

                    obj = {
                        'pid': r['pid'],
                        'cid': r['cid'],
                        'hospcode': r['hospcode'],
                        'gravida': r['gravida'],
                        'fullname': p['name'] + '  ' + p['lname'],
                        'cid': p['cid'],
                        'birth': h.to_thai_date(p['birth']),
                        'age': h.count_age(p['birth']),
                        'first_visit': h.to_thai_date(anc.get_first_anc(p['pid'], r['gravida'], r['hospcode'])),
                        'last_visit': h.to_thai_date(anc.get_last_anc(p['pid'], r['gravida'], r['hospcode'])),
                        'bdate': bdate,
                        'edc': edc,
                        'lmp': lmp,
                        'is_survey': anc.get_survey_status(r['pid'], r['gravida'], r['hospcode']),
                        'anc_count': anc.get_anc_count(r['pid'], r['hospcode'], r['gravida'])
                    }
                    rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}


@view_config(route_name='anc_get_list_map_total', renderer='json')
def anc_get_list_map_total(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        anc = AncModel(request)

        by = request.params['by']
        vid = request.params['vid'] if 'vid' in request.params else False

        try:
            if vid:
                home = HomeModel(request)
                hids = home.get_hid_from_village(request.session['hospcode'], vid)
                total = anc.get_list_map_anc_total_by_vid(request.session['hospcode'], hids, int(by))
            else:
                total = anc.get_list_map_anc_total(request.session['hospcode'], int(by))
            return {'ok': 1, 'total': total}
        except Exception as e:
            return {'ok': 0, 'msg': e.message}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='anc_get_list_map', request_method='POST', renderer='json')
def anc_get_list_map(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:  # is ajax request
            start = request.params['start']
            stop = request.params['stop']
            by = request.params['by']
            vid = request.params['vid'] if 'vid' in request.params else False

            limit = int(stop) - int(start)

            anc = AncModel(request)
            person = PersonModel(request)
            
            if vid:
                home = HomeModel(request)
                hids = home.get_hid_from_village(request.session['hospcode'], vid)
                rs = anc.get_list_map_anc_by_vid(request.session['hospcode'], hids, int(by), int(start), int(limit))
            else:
                rs = anc.get_list_map_anc(request.session['hospcode'], int(by), int(start), int(limit))

            rows = []
            if rs:
                for r in rs:
                    p = person.get_person_detail(r['pid'], request.session['hospcode'])

                    obj = {
                        'cid': p['cid'],
                        'pid': p['pid'],
                        'hid': p['hid'],
                        'fullname': '%s %s' % (p['name'], p['lname']),
                        'age': h.count_age(p['birth']),
                        'gravida': r['gravida'],
                        'hospcode': r['hospcode'],
                        'latlng': anc.get_latlng_from_pid(p['pid'], request.session['hospcode'])
                    }

                    rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}

            
@view_config(route_name='anc_all_latlng', renderer='json')
def anc_all_latlng(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        anc = AncModel(request)
        person = PersonModel(request)

        by = request.params['by']
        vid = request.params['vid'] if 'vid' in request.params else False
        
        if vid:
            home = HomeModel(request)
            hids = home.get_hid_from_village(request.session['hospcode'], vid)
            pids = anc.get_list_map_anc_all_by_vid(request.session['hospcode'], hids, int(by))
        else:
            pids = anc.get_list_map_anc_all(request.session['hospcode'], int(by))
        #try:
        #rs = anc.get_all_latlng(request.session['hospcode'], pids)
        rows = []
        
        if pids:
            for r in pids:
                p = person.get_person_detail(r, request.session['hospcode'])
                prenatal = anc.get_prenatal_all(request.session['hospcode'], r)
                obj_pre = []

                if prenatal:
                    for rp in prenatal:
                        obj_prenatal = {
                            'gravida': rp['gravida'],
                            'date_hct': h.to_thai_date(rp['date_hct']),
                            'edc': h.to_thai_date(rp['edc']),
                            'hb_result': rp['hb_result'],
                            'hct_result': rp['hct_result'],
                            'hiv_result': rp['hiv_result'],
                            'lmp': h.to_thai_date(rp['lmp']),
                            'thalassemia': rp['thalassemia'],
                            'vdrl_result': rp['vdrl_result']
                        }
                        obj_pre.append(obj_prenatal)
                else:
                    obj_pre = []

                obj = {
                    'cid': p['cid'],
                    'pid': p['pid'],
                    'hid': p['hid'],
                    'hospcode': p['hospcode'],
                    'fullname': '%s %s' % (p['name'], p['lname']),
                    'birth': h.to_thai_date(p['birth']),
                    'age': h.count_age(p['birth']),
                    'latlng': anc.get_latlng_from_pid(r, request.session['hospcode']),
                    'prenatal': obj_pre
                }

                rows.append(obj)

        return {'ok': 1, 'rows': rows}
        #except Exception as e:
        #    return {'ok': 0, 'msg': e.message}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='anc_get_risk_by_group', renderer='json', request_method='POST')
def get_risk_by_group(request):

    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.is_xhr:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        start_date = h.jsdate_to_string(request.params['start_date'])
        end_date = h.jsdate_to_string(request.params['end_date'])

        if is_token:

            hospcode = request.params['hospcode'] if 'hospcode' in request.params else request.session['hospcode']

            anc = AncModel(request)

            rs01 = anc.count_risk01(hospcode, start_date, end_date)
            rs02 = anc.count_risk02(hospcode, start_date, end_date)
            rs03 = anc.count_risk03(hospcode, start_date, end_date)
            rs04 = anc.count_risk04(hospcode, start_date, end_date)
            rs05 = anc.count_risk05(hospcode, start_date, end_date)
            rs06 = anc.count_risk06(hospcode, start_date, end_date)
            rs07 = anc.count_risk07(hospcode, start_date, end_date)
            rs08 = anc.count_risk08(hospcode, start_date, end_date)
            rs09 = anc.count_risk09(hospcode, start_date, end_date)
            rs10 = anc.count_risk10(hospcode, start_date, end_date)
            rs11 = anc.count_risk11(hospcode, start_date, end_date)
            rs12 = anc.count_risk12(hospcode, start_date, end_date)
            rs13 = anc.count_risk13(hospcode, start_date, end_date)
            rs14 = anc.count_risk14(hospcode, start_date, end_date)
            rs15 = anc.count_risk15(hospcode, start_date, end_date)
            rs16 = anc.count_risk16(hospcode, start_date, end_date)
            rs17 = anc.count_risk17(hospcode, start_date, end_date)
            rs18 = anc.count_risk18(hospcode, start_date, end_date)

            obj = {
                "risk01": rs01,
                "risk02": rs02,
                "risk03": rs03,
                "risk04": rs04,
                "risk05": rs05,
                "risk06": rs06,
                "risk07": rs07,
                "risk08": rs08,
                "risk09": rs09,
                "risk10": rs10,
                "risk11": rs11,
                "risk12": rs12,
                "risk13": rs13,
                "risk14": rs14,
                "risk15": rs15,
                "risk16": rs16,
                "risk17": rs17,
                "risk18": rs18,
            }

            return {'ok': 1, 'rows': [obj]}


@view_config(route_name='anc_get_risk_list_by_type', renderer='json')
def anc_get_risk_list_by_type(request):

    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.is_xhr:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            start_date = h.jsdate_to_string(request.params['start_date'])
            end_date = h.jsdate_to_string(request.params['end_date'])
            choice = request.params['choice']

            hospcode = request.params['hospcode'] if 'hospcode' in request.params else request.session['hospcode']

            anc = AncModel(request)
            person = PersonModel(request)

            rs = anc.get_risk_list_by_type(hospcode, choice, start_date, end_date)

            if rs:
                rows = []
                for r in rs:
                    p = person.get_person_detail(r['pid'], request.session['hospcode'])
                    obj = {
                        'pid': r['pid'],
                        'cid': p['cid'],
                        'fullname': p['name'] + ' ' + p['lname'],
                        'birth': h.to_thai_date(p['birth']),
                        'age': h.count_age(p['birth'])
                    }

                    rows.append(obj)

                return {'ok': 1, 'rows': rows}

            else:
                return {'ok': 0, 'msg': u'ไม่พบรายการ'}