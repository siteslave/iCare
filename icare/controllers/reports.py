# -*- coding: utf8
from datetime import datetime, date

from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPFound
)
from icare.models.anc_model import AncModel

from icare.models.person_model import PersonModel
from icare.models.report_model import ReportModel
from icare.models.mch_model import MchModel
from icare.models.babies_model import BabiesModel

from icare.helpers.icare_helper import ICHelper

from bson.objectid import ObjectId
import calendar

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
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

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
                    'is_risk': r['is_risk'] if 'is_risk' in r else None,
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

    start_date = h.jsdate_to_string(request.params['s'])
    end_date = h.jsdate_to_string(request.params['e'])

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
    try:
        mch.do_process_forecast(request.session['hospcode'])
        return {'ok': 1}
    except Exception as ex:
        return {'ok': 0, 'msg': ex.message}


@view_config(route_name='report_mch_list', renderer='json', request_method='POST')
def report_mch_list(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    start = request.params['start']
    stop = request.params['stop']

    limit = int(stop) - int(start)

    mch = MchModel(request)
    person = PersonModel(request)

    if request.params['s'] != "" and request.params['e'] != "":
        #Get by date
        start_date = h.jsdate_to_string(request.params['s'])
        end_date = h.jsdate_to_string(request.params['e'])

        rs = mch.get_labor_forecast_filter_list(request.session['hospcode'], start_date, end_date,
                                                int(start), int(limit))
    else:
        rs = mch.get_labor_forecast_list(request.session['hospcode'], int(start), int(limit))

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
                'bdate': h.to_thai_date(r['bdate']),
                #'address': h.get_address(request, r['hid'], r['hospcode']),
                'ppcares': r['ppcares'] if 'ppcares' in r else None
            }

            rows.append(obj)

        return {'ok': 1, 'rows': rows}
    else:
        return {'ok': 0, 'msg': 'ไม่พบรายการ'}


@view_config(route_name='report_mch_total', request_method='POST', renderer='json')
def report_mch_total(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:
                mch = MchModel(request)

                if request.params['s'] != "" and request.params['e'] != "":
                    #Get by date
                    start_date = h.jsdate_to_string(request.params['s'])
                    end_date = h.jsdate_to_string(request.params['e'])

                    total = mch.get_labor_forecast_filter_total(request.session['hospcode'],
                                                                start_date, end_date)

                    return {'ok': 1, 'total': total}
                else:
                    total = mch.get_labor_forecast_total(request.session['hospcode'])

                    return {'ok': 1, 'total': total}
            else:
                return {'ok': 0, 'msg': 'Invalid token key'}


@view_config(route_name='report_mch_target_per_month', renderer='json', request_method='POST')
def report_mch_target_per_month(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    mch = MchModel(request)
    person = PersonModel(request)

    current_date = datetime.now()
    current_month = datetime.strftime(current_date, '%m')
    current_year = datetime.strftime(current_date, '%Y')
    end_day_of_month = calendar.monthrange(int(current_year), int(current_month))[1]

    start_date = date(int(current_year), int(current_month), 1)
    end_date = date(int(current_year), int(current_month), int(end_day_of_month))

    start_date = datetime.strftime(start_date, '%Y%m%d')
    end_date = datetime.strftime(end_date, '%Y%m%d')

    rs = mch.get_target_per_month(request.session['hospcode'], start_date, end_date)

    if rs:
        rows = []

        for r in rs:
            p = person.get_person_detail(r['pid'], r['hospcode'])
            obj = {
                'fullname': p['name'] + '  ' + p['lname'],
                'cid': p['cid'],
                #'birth': h.to_thai_date(p['birth']),
                'age': h.count_age(p['birth']),
                #'sex': p['sex'],
                #'bdate': h.to_thai_date(r['bdate']),
                #'address': h.get_address(request, r['hid'], r['hospcode']),
                #'ppcares': r['ppcares'] if 'ppcares' in r else None
            }

            rows.append(obj)

        return {'ok': 1, 'rows': rows}
    else:
        return {'ok': 0, 'msg': 'ไม่พบรายการ'}


@view_config(route_name='report_anc_target_per_month', renderer='json', request_method='POST')
def report_anc_target_per_month(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    rpt = ReportModel(request)
    person = PersonModel(request)

    current_date = datetime.now()
    current_month = datetime.strftime(current_date, '%m')
    current_year = datetime.strftime(current_date, '%Y')
    end_day_of_month = calendar.monthrange(int(current_year), int(current_month))[1]

    start_date = date(int(current_year), int(current_month), 1)
    end_date = date(int(current_year), int(current_month), int(end_day_of_month))

    start_date = datetime.strftime(start_date, '%Y%m%d')
    end_date = datetime.strftime(end_date, '%Y%m%d')

    rs = rpt.get_anc_target_per_month(request.session['hospcode'], start_date, end_date)

    if rs:
        rows = []

        for r in rs:
            p = person.get_person_detail(r['pid'], r['hospcode'])
            obj = {
                'fullname': p['name'] + '  ' + p['lname'],
                'cid': p['cid'],
                #'birth': h.to_thai_date(p['birth']),
                'age': h.count_age(p['birth']),
                #'sex': p['sex'],
                #'bdate': h.to_thai_date(r['bdate']),
                #'address': h.get_address(request, r['hid'], r['hospcode']),
                #'ppcares': r['ppcares'] if 'ppcares' in r else None
            }

            rows.append(obj)

        return {'ok': 1, 'rows': rows}
    else:
        return {'ok': 0, 'msg': 'ไม่พบรายการ'}

"""
Newborn
"""


@view_config(route_name='reports_newborn_wlt2500', renderer='reports_newborn_wlt2500.mako')
def reports_newborn_wlt2500(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    return {'title': u'เด็กที่มีน้ำหนักแรกคลอดน้อยกว่า 2,500 กรัม'}


@view_config(route_name='reports_newborn_weight_less_than_2500', renderer='json', request_method='POST')
def reports_newborn_weight_less_than_2500(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    if request.is_xhr:  # is ajax request
        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            babies = BabiesModel(request)
            person = PersonModel(request)

            start = request.params['start']
            stop = request.params['stop']

            limit = int(stop) - int(start)

            rs = babies.get_newborn_weight_less_than_2500(request.session['hospcode'], int(start), int(limit))

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
                        'birth': h.to_thai_date(p['birth']),
                        'address': h.get_address(request, p['hid'], r['hospcode']),
                        'bweight': r['bweight'],
                        'hospcode': r['hospcode'],
                        'pid': r['pid'],
                        'gravida': r['gravida']
                    }

                    rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': 'ไม่พบรายการ'}
        else:
            return {'ok': 0, 'msg': 'Invalid token key.'}


@view_config(route_name='reports_newborn_weight_less_than_2500_search', renderer='json', request_method='POST')
def reports_newborn_weight_less_than_2500_search(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    if request.is_xhr:  # is ajax request
        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            babies = BabiesModel(request)
            person = PersonModel(request)

            cid = request.params['cid'] if 'cid' in request.params else '0000000000000'

            rs = babies.search_newborn_weight_less_than_2500(cid, request.session['hospcode'])

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
                        'address': h.get_address(request, p['hid'], r['hospcode']),
                        'bweight': r['bweight'],
                        'hospcode': r['hospcode'],
                        'pid': r['pid'],
                        'gravida': r['gravida']
                        #'ppcares': r['ppcares'] if 'ppcares' in r else None
                    }

                    rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': 'ไม่พบรายการ'}
        else:
            return {'ok': 0, 'msg': 'Invalid token key.'}


@view_config(route_name='reports_newborn_weight_less_than_2500_total', request_method='POST', renderer='json')
def reports_newborn_weight_less_than_2500_total(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:
                babies = BabiesModel(request)
                total = babies.get_newborn_weight_less_than_2500_total(request.session['hospcode'])

                return {'ok': 1, 'total': total}
            else:
                return {'ok': 0, 'msg': 'Invalid token key'}
        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='reports_milk_index', renderer='reports_newborn_milk.mako')
def reports_newborn_milk(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    return {'title': u'การให้นมเด็กหลังคลอด'}


@view_config(route_name='reports_milk_process', request_method='POST', renderer='json')
def reports_milk_process(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:
                babies = BabiesModel(request)
                babies.process_milk(request.session['hospcode'])

                return {'ok': 1}
            else:
                return {'ok': 0, 'msg': 'Invalid token key'}
        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='reports_milk_list', renderer='json', request_method='POST')
def reports_milk_list(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    if request.is_xhr:  # is ajax request
        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            babies = BabiesModel(request)
            person = PersonModel(request)

            start = request.params['start']
            stop = request.params['stop']

            limit = int(stop) - int(start)

            rs = babies.get_milk_list(request.session['hospcode'], int(start), int(limit))

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
                        'address': h.get_address(request, p['hid'], r['hospcode']),
                        'hospcode': r['hospcode'],
                        'pid': r['pid'],
                        'total': r['total']
                    }

                    rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': 'ไม่พบรายการ'}
        else:
            return {'ok': 0, 'msg': 'Invalid token key.'}


@view_config(route_name='reports_milk_total', request_method='POST', renderer='json')
def reports_milk_total(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:
                babies = BabiesModel(request)
                total = babies.get_milk_total(request.session['hospcode'])

                return {'ok': 1, 'total': total}
            else:
                return {'ok': 0, 'msg': 'Invalid token key'}
        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}

""" ANC Coverages """


@view_config(route_name='reports_anc_coverages_index', renderer='reports_anc_coverages.mako')
def reports_anc_coverages_index(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    return {'title': u'ความครอบคลุมการฝากครรภ์'}


@view_config(route_name='reports_anc_coverages_list', renderer='json', request_method='POST')
def reports_anc_coverages_list(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    if request.is_xhr:  # is ajax request
        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            anc = AncModel(request)
            person = PersonModel(request)

            # 1 = All
            # 2 = Cover
            # 3 = Not cover

            t = request.params['t'] if 't' in request.params else '1'
            start = request.params['start']
            stop = request.params['stop']

            limit = int(stop) - int(start)

            if t == '2':
                rs = anc.get_anc_coverages(request.session['hospcode'], int(start), int(limit))
            elif t == '3':
                rs = anc.get_anc_not_coverages(request.session['hospcode'], int(start), int(limit))
            else:
                rs = anc.get_anc_coverages_all(request.session['hospcode'], int(start), int(limit))

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
                        'address': h.get_address(request, p['hid'], r['hospcode']),
                        'hospcode': r['hospcode'],
                        'pid': r['pid'],
                        'total': r['total']
                    }

                    rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': 'ไม่พบรายการ'}
        else:
            return {'ok': 0, 'msg': 'Invalid token key.'}


@view_config(route_name='reports_anc_coverages_search', renderer='json', request_method='POST')
def reports_anc_coverages_search(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    if request.is_xhr:  # is ajax request
        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            anc = AncModel(request)
            person = PersonModel(request)

            cid = request.params['cid']

            rs = anc.search_anc_coverages(request.session['hospcode'], cid)

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
                        'address': h.get_address(request, p['hid'], r['hospcode']),
                        'hospcode': r['hospcode'],
                        'pid': r['pid'],
                        'total': r['total']
                    }

                    rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': 'ไม่พบรายการ'}
        else:
            return {'ok': 0, 'msg': 'Invalid token key.'}


@view_config(route_name='reports_anc_coverages_total', request_method='POST', renderer='json')
def reports_anc_coverages_total(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:
                anc = AncModel(request)

                t = request.params['t'] if 't' in request.params else '1'

                if t == '2':
                    total = anc.get_anc_coverages_count(request.session['hospcode'])
                elif t == '3':
                    total = anc.get_anc_not_coverages_count(request.session['hospcode'])
                else:
                    total = anc.get_anc_coverages_all_count(request.session['hospcode'])

                return {'ok': 1, 'total': total}
            else:
                return {'ok': 0, 'msg': 'Invalid token key'}
        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


""" ANC 12 Weeks """


@view_config(route_name='reports_anc_12weeks_index', renderer='reports_anc_12ws.mako')
def reports_anc_12weeks_index(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    return {'title': u'ฝากครรภ์เมื่ออายุครรภ์ <= 12 สัปดาห์'}


@view_config(route_name='reports_anc_12ws_list', renderer='json', request_method='POST')
def reports_anc_12ws_list(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins')

    if request.is_xhr:  # is ajax request
        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            anc = AncModel(request)
            person = PersonModel(request)

            start = request.params['start']
            stop = request.params['stop']

            limit = int(stop) - int(start)

            rs = anc.get_anc_12ws_list(request.session['hospcode'], int(start), int(limit))

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
                        'address': h.get_address(request, p['hid'], r['hospcode']),
                        'hospcode': r['hospcode'],
                        'pid': r['pid'],
                        'gravida': r['gravida']
                    }

                    rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': 'ไม่พบรายการ'}
        else:
            return {'ok': 0, 'msg': 'Invalid token key.'}


@view_config(route_name='reports_anc_12ws_total', request_method='POST', renderer='json')
def reports_anc_12ws_total(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:
                anc = AncModel(request)

                total = anc.get_anc_12ws_total(request.session['hospcode'])

                return {'ok': 1, 'total': total}
            else:
                return {'ok': 0, 'msg': 'Invalid token key'}
        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='report_index_get_total', request_method='POST', renderer='json')
def report_index_get_total_anc(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:
                rpt = ReportModel(request)

                #anc total
                anc_total = rpt.get_anc_total(request.session['hospcode'])
                risk_total = rpt.get_anc_risk_total(request.session['hospcode'])
                labor_total = rpt.get_is_labor_total(request.session['hospcode'])
                weeks_total = rpt.get_12weeks_total(request.session['hospcode'])
                coverages_total = rpt.get_anc_coverages_total(request.session['hospcode'])

                return {'ok': 1, 'anc': int(anc_total), 'risk': int(risk_total), 'labor': int(labor_total),
                        'weeks': int(weeks_total), 'coverages': int(coverages_total)}

            else:
                return {'ok': 0, 'msg': 'Invalid token key'}