# -*- coding: utf8
from pyramid.view import (
    view_config,
)
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPUnauthorized,
)

from icare.helpers.icare_helper import ICHelper
from icare.models.mch_model import MchModel
from icare.models.person_model import PersonModel
#Load helper
h = ICHelper()

#Main page
@view_config(route_name='mch_index', renderer='mch.mako')
def index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.session['user_type'] == '1':
            return HTTPFound(location='/admins')
            
        return {'title': u'ข้อมูลการฝากครรภ์'}


@view_config(route_name='mch_other', renderer='mch_other.mako')
def map_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        return {'title': u'แผนที่ระบบงานแม่และเด็ก'}


@view_config(route_name='mch_map', renderer='mch_map.mako')
def map_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        villages = h.get_villages(request, request.session['hospcode'])
        return {'title': u'แผนที่ระบบงานแม่และเด็ก', 'villages': villages}


@view_config(route_name='mch_get_list_total', renderer='json')
def get_list_total(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            mch = MchModel(request)

            try:
                total = mch.get_list_total(request.session['hospcode'])
                return {'ok': 1, 'total': total}
            except Exception as e:
                return {'ok': 0, 'msg': e.message}
        else:
            return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='mch_get_list_total_by_birth', renderer='json')
def get_list_total_by_birth(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        csrf_token = request.params['csrf_token']
        start_date = h.jsdate_to_string(request.params['start_date'])
        end_date = h.jsdate_to_string(request.params['end_date'])

        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            mch = MchModel(request)

            try:
                total = mch.get_list_total_by_birth(request.session['hospcode'], start_date, end_date)
                return {'ok': 1, 'total': total}
            except Exception as e:
                return {'ok': 0, 'msg': e.message}
        else:
            return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='mch_get_list', request_method='POST', renderer='json')
def get_list(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:

                start = request.params['start']
                stop = request.params['stop']

                limit = int(stop) - int(start)

                mch = MchModel(request)
                person = PersonModel(request)

                rs = mch.get_list(request.session['hospcode'], int(start), int(limit))
                rows = []

                if rs:
                    for r in rs:
                        p = person.get_person_detail(r['pid'], request.session['hospcode'])
                        obj = {
                            'pid': r['pid'],
                            'hospcode': r['hospcode'],
                            'gravida': r['gravida'],
                            'fullname': p['name'] + '  ' + p['lname'],
                            'cid': p['cid'],
                            'birth': h.to_thai_date(p['birth']),
                            'age': h.count_age(p['birth'], r['bdate']),
                            'bdate': h.to_thai_date(r['bdate']),
                            'bplace': r['bplace'],
                            'bhospcode': r['bhosp'],
                            'bhospname': h.get_hospital_name(request, r['bhosp']),
                            'sborn': r['sborn'],
                            'lborn': r['lborn'],
                            'btype': r['btype'],
                            'typearea': r['typearea'] if 'typearea' in r else '0',
                            'count_postnatal': mch.get_count_postnatal(r['pid'], r['gravida'], r['hospcode'])
                        }
                        rows.append(obj)

                    return {'ok': 1, 'rows': rows}
                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': 'Token not found.'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='mch_get_list_by_birth', request_method='POST', renderer='json')
def get_list_by_birth(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            start_date = h.jsdate_to_string(request.params['start_date'])
            end_date = h.jsdate_to_string(request.params['end_date'])

            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:

                start = request.params['start']
                stop = request.params['stop']

                limit = int(stop) - int(start)

                mch = MchModel(request)
                person = PersonModel(request)

                rs = mch.get_list_by_birth(request.session['hospcode'], start_date, end_date, int(start), int(limit))
                rows = []

                if rs:
                    for r in rs:
                        p = person.get_person_detail(r['pid'], r['hospcode'])
                        obj = {
                            'pid': r['pid'],
                            'hospcode': r['hospcode'],
                            'gravida': r['gravida'],
                            'fullname': p['name'] + '  ' + p['lname'],
                            'cid': p['cid'],
                            'birth': h.to_thai_date(p['birth']),
                            'age': h.count_age(p['birth'], r['bdate']),
                            'bdate': h.to_thai_date(r['bdate']),
                            'bplace': r['bplace'],
                            'bhospcode': r['bhosp'],
                            'bhospname': h.get_hospital_name(request, r['bhosp']),
                            'sborn': r['sborn'],
                            'lborn': r['lborn'],
                            'btype': r['btype'],
                            'typearea': r['typearea'],
                            'count_postnatal': mch.get_count_postnatal(r['pid'], r['gravida'], r['hospcode'])
                        }
                        rows.append(obj)

                    return {'ok': 1, 'rows': rows}
                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': 'Token not found.'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='mch_search', request_method='POST', renderer='json')
def search(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:

                cid = request.params['cid']

                mch = MchModel(request)
                person = PersonModel(request)

                rs = mch.search(request.session['hospcode'], cid)
                rows = []

                if rs:
                    for r in rs:
                        p = person.get_person_detail(r['pid'], request.session['hospcode'])
                        obj = {
                            'pid': r['pid'],
                            'cid': r['cid'],
                            'hospcode': r['hospcode'],
                            'gravida': r['gravida'],
                            'fullname': p['name'] + '  ' + p['lname'],
                            'cid': p['cid'],
                            'birth': h.to_thai_date(p['birth']),
                            'age': h.count_age(p['birth'], r['bdate']),
                            'bdate': h.to_thai_date(r['bdate']),
                            'bplace': r['bplace'],
                            'bhospcode': r['bhosp'],
                            'bhospname': h.get_hospital_name(request, r['bhosp']),
                            'sborn': r['sborn'],
                            'lborn': r['lborn'],
                            'btype': r['btype'],
                            'typearea': r['typearea'],
                            'count_postnatal': mch.get_count_postnatal(r['pid'], r['gravida'], r['hospcode'])
                        }
                        rows.append(obj)

                    return {'ok': 1, 'rows': rows}
                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': 'Token not found.'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='mch_get_postnatal', request_method='POST', renderer='json')
def get_postnatal(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request

            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:

                pid = request.params['pid']
                gravida = request.params['gravida']

                mch = MchModel(request)

                rs = mch.get_postnatal(pid, gravida, request.session['hospcode'])
                rows = []

                if rs:
                    for r in rs:
                        obj = {
                            'pid': r['pid'],
                            'ppplace_code': r['ppplace'],
                            'ppplace_name': h.get_hospital_name(request, r['ppplace']),
                            'gravida': r['gravida'],
                            'bdate': h.to_thai_date(r['bdate']),
                            'ppcare': h.to_thai_date(r['ppcare']),
                            'ppresult': r['ppresult']
                        }
                        rows.append(obj)

                    return {'ok': 1, 'rows': rows}
                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': 'Token not found.'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='mch_get_postnatal_all', request_method='POST', renderer='json')
def get_postnatal_all(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request

            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:

                cid = request.params['cid']
                gravida = request.params['gravida']

                mch = MchModel(request)

                rs = mch.get_postnatal_all(cid, gravida)
                rows = []

                if rs:
                    for r in rs:
                        obj = {
                            'pid': r['pid'],
                            'hospcode': r['hospcode'],
                            'ppplace_code': r['ppplace'],
                            'ppplace_name': h.get_hospital_name(request, r['ppplace']),
                            'gravida': r['gravida'],
                            'bdate': h.to_thai_date(r['bdate']),
                            'ppcare': h.to_thai_date(r['ppcare']),
                            'ppresult': r['ppresult'],
                            'seq': r['seq'],
                            'appoint': mch.count_appointment(r['pid'], r['hospcode'], r['seq'])
                        }
                        rows.append(obj)

                    return {'ok': 1, 'rows': rows}
                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': 'Token not found.'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='mch_get_appointment', request_method='POST', renderer='json')
def get_appointment(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request

            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:

                pid = request.params['pid']
                hospcode = request.params['hospcode']
                seq = request.params['seq']

                mch = MchModel(request)

                rs = mch.get_appointment(pid, hospcode, seq)
                rows = []

                if rs:
                    for r in rs:
                        obj = {
                            'apdate': h.to_thai_date(r['apdate']),
                            'aptype': h.get_aptype(request, r['aptype']),
                            'apdiag_code': r['apdiag'],
                            'apdiag_name': h.get_diag_name(request, r['apdiag']),
                        }

                        rows.append(obj)

                    return {'ok': 1, 'rows': rows}
                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': 'Token not found.'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}
