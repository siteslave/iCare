# -*- coding: utf8

from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPUnauthorized
)

from icare.models.person_model import PersonModel
from icare.models.report_model import ReportModel
from icare.models.mch_model import MchModel

from icare.helpers.icare_helper import ICHelper

from bson.objectid import ObjectId

h = ICHelper()


@view_config(route_name='reports_index', renderer='reports.mako')
def index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')
                
    villages = h.get_villages(request, request.session['hospcode'])
    return {'title': u'หน้าหลัก', 'villages': villages}


@view_config(route_name="reports_anc_risk", renderer="reports_anc_risk.mako")
def report_anc_risk_view(request):
    return {'title': u'ผู้ป่วยกลุ่มเสี่ยงที่มารับบริการฝากครรภ์'}


@view_config(route_name='report_get_anc_risk_total', request_method='POST', renderer='json')
def get_babies_total(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:
                rpt = ReportModel(request)

                t = request.params['t']

                if t == '0':
                    #get all
                    total = rpt.get_risk_all_total(request.session['hospcode'])
                    return {'ok': 1, 'total': total}
                else:
                    #get filter
                    total = rpt.get_risk_filter_total(request.session['hospcode'], t)
                    return {'ok': 1, 'total': total}
            else:
                return {'ok': 0, 'msg': 'Invalid token key'}


@view_config(route_name='report_get_anc_risk_detail', request_method='POST', renderer='json')
def get_anc_risk_detail(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:
                rpt = ReportModel(request)

                id = ObjectId(request.params['id'])
                rs = rpt.get_risk_detail(id)

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

            else:
                return {'ok': 0, 'msg': 'Invalid token key'}


@view_config(route_name='report_get_anc_risk_list', request_method='POST', renderer='json')
def get_anc_risk_list(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        rpt = ReportModel(request)
        hospcode = request.session['hospcode']
        t = request.params['t']

        start = request.params['start'] if 'start' in request.params else 0
        stop = request.params['stop'] if 'stop' in request.params else 25

        limit = int(stop) - int(start)

        #All
        if t == '0':
            rs = rpt.get_risk_all_list(int(start), int(limit), hospcode)
        #Risk
        else:
            rs = rpt.get_risk_filter_list(int(start), int(limit), hospcode, t)

        if rs:
            person = PersonModel(request)
            rows = []

            for r in rs:
                p = person.get_person_detail(r['pid'], r['hospcode'])
                scrn = []

                for s in rpt.get_risk_screen_list(p['cid']):
                    obj_screen = {
                        'last_update': s['last_update'],
                        'id': str(s['_id'])
                    }

                    scrn.append(obj_screen)

                obj = {
                    'fullname': p['name'] + '  ' + p['lname'],
                    'cid': p['cid'],
                    'birth': h.to_thai_date(p['birth']),
                    'age': h.count_age(p['birth']),
                    'sex': p['sex'],
                    'is_risk': r['is_risk'],
                    'screen_date': scrn,
                    'address': h.get_address(request, p['hid'], p['hospcode'])
                }

                rows.append(obj)

            return {'ok': 1, 'rows': rows}
        else:
            return {'ok': 0, 'msg': 'ไม่พบรายการ'}


@view_config(route_name='report_get_anc_risk_search', request_method='POST', renderer='json')
def get_anc_risk_list_search(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        rpt = ReportModel(request)

        cid = request.params['cid']
        rs = rpt.get_risk_search(cid)

        if rs:
            person = PersonModel(request)
            rows = []

            for r in rs:
                p = person.get_person_detail(r['pid'], r['hospcode'])
                scrn = []

                for s in rpt.get_risk_screen_list(p['cid']):
                    obj_screen = {
                        'last_update': s['last_update'],
                        'id': str(s['_id'])
                    }

                    scrn.append(obj_screen)

                obj = {
                    'fullname': p['name'] + '  ' + p['lname'],
                    'cid': p['cid'],
                    'birth': h.to_thai_date(p['birth']),
                    'age': h.count_age(p['birth']),
                    'sex': p['sex'],
                    'is_risk': r['is_risk'],
                    'screen_date': scrn,
                    'address': h.get_address(request, p['hid'], p['hospcode'])
                }

                rows.append(obj)

            return {'ok': 1, 'rows': rows}
        else:
            return {'ok': 0, 'msg': 'ไม่พบรายการ'}


@view_config(route_name='report_get_anc_history', request_method='POST', renderer='json')
def get_anc_history(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.is_xhr:
        cid = request.params['cid']
        csrf_token = request.params['csrf_token']

        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:
            rpt = ReportModel(request)

            visit = rpt.get_anc_history(cid)
            rows = []

            for v in visit:

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
                    'hospname': h.get_hospital_name(request, v['hospcode'])
                }

                rows.append(obj)

            return {'ok': 1, 'rows': rows}
        else:
            return {'ok': 0, 'msg': 'Not authorized.'}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


"""
    ANC module
"""


@view_config(route_name='report_anc', renderer='reports_anc.mako')
def anc_index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    return {'title': u'หญิงคลอดครบเกณฑ์การฝากครรภ์'}


@view_config(route_name='report_anc_get_total', request_method='POST', renderer='json')
def get_anc_total(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:
                rpt = ReportModel(request)

                t = request.params['t'] if 't' in request.params else '-1'

                if t == '1':
                    #get all
                    total = rpt.get_anc_list_success_total(request.session['hospcode'])
                    return {'ok': 1, 'total': total}
                elif t == '0':
                    #get filter
                    total = rpt.get_anc_list_not_success_total(request.session['hospcode'])
                    return {'ok': 1, 'total': total}
                else:
                    #get filter
                    total = rpt.get_anc_list_all_total(request.session['hospcode'])
                    return {'ok': 1, 'total': total}
            else:
                return {'ok': 0, 'msg': 'Invalid token key'}


@view_config(route_name='report_anc_get_list', renderer='json', request_method='POST')
def anc_get_list(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    t = request.params['t'] if 't' in request.params else '-1'

    start = request.params['start']
    stop = request.params['stop']

    limit = int(stop) - int(start)

    rpt = ReportModel(request)

    if t == '1':
        #get success
        rs = rpt.get_anc_list_success(request.session['hospcode'], int(start), int(limit))
    elif t == '0':
        #get not success
        rs = rpt.get_anc_list_not_success(request.session['hospcode'], int(start), int(limit))
    else:
        #get all
        rs = rpt.get_anc_list_all(request.session['hospcode'], int(start), int(limit))

    if rs:
        person = PersonModel(request)
        rows = []

        for r in rs:
            p = person.get_person_detail(r['pid'], r['hospcode'])
            obj = {
                'fullname': p['name'] + '  ' + p['lname'],
                'cid': p['cid'],
                'birth': h.to_thai_date(p['birth']),
                'age': h.count_age(p['birth']),
                'sex': p['sex'],
                #'address': h.get_address(request, r['hid'], r['hospcode']),
                'coverages': r['coverages'] if 'coverages' in r else None
            }

            rows.append(obj)

        return {'ok': 1, 'rows': rows}
    else:
        return {'ok': 0, 'msg': 'Not success'}


@view_config(route_name='report_anc_get_forecast_filter', renderer='json', request_method='POST')
def anc_get_forecast_filter(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    rpt = ReportModel(request)
    person = PersonModel(request)

    start_date = request.params['s']
    end_date = request.params['e']

    start_date = start_date.split('/')
    end_date = end_date.split('/')

    sy = int(start_date[2]) - 543
    ey = int(end_date[2]) - 543

    start_date = str(sy) + start_date[1] + start_date[0]
    end_date = str(ey) + end_date[1] + end_date[0]

    rs = rpt.get_anc_forecast_filter(request.session['hospcode'], start_date, end_date)

    if rs:
        rows = []

        for r in rs:
            p = person.get_person_detail(r['pid'], r['hospcode'])
            obj = {
                'fullname': p['name'] + '  ' + p['lname'],
                'cid': p['cid'],
                'birth': h.to_thai_date(p['birth']),
                'age': h.count_age(p['birth']),
                'sex': p['sex'],
                #'address': h.get_address(request, r['hid'], r['hospcode']),
                'coverages': r['coverages'] if 'coverages' in r else None
            }

            rows.append(obj)

        return {'ok': 1, 'rows': rows}
    else:
        return {'ok': 0, 'msg': 'ไม่พบรายการ'}


@view_config(route_name='report_anc_search', renderer='json', request_method='POST')
def anc_search(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    rpt = ReportModel(request)
    person = PersonModel(request)

    cid = request.params['cid']

    rs = rpt.get_anc_search(request.session['hospcode'], cid)

    if rs:
        rows = []

        for r in rs:
            p = person.get_person_detail(r['pid'], r['hospcode'])
            obj = {
                'fullname': p['name'] + '  ' + p['lname'],
                'cid': p['cid'],
                'birth': h.to_thai_date(p['birth']),
                'age': h.count_age(p['birth']),
                'sex': p['sex'],
                #'address': h.get_address(request, r['hid'], r['hospcode']),
                'coverages': r['coverages'] if 'coverages' in r else None
            }

            rows.append(obj)

        return {'ok': 1, 'rows': rows}
    else:
        return {'ok': 0, 'msg': 'ไม่พบรายการ'}

"""
MCH Modules
"""


@view_config(route_name='reports_mch_index', renderer='reports_mch.mako')
def report_mch_index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    return {'title': u'ทะเบียนเยี่ยมแม่หลังคลอด'}


@view_config(route_name='reports_mch_do_process', renderer='json')
def reports_mch_do_process_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    mch = MchModel(request)
    #try:
    #    mch.do_process_forecast(request.session['hospcode'])
    #    return {'ok': 1}
    #except Exception as ex:
    #    return {'ok': 0, 'msg': ex.message}

    mch.do_process_forecast(request.session['hospcode'])
    return {'ok': 1}