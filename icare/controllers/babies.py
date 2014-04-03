# -*- coding: utf8
from datetime import datetime
from pyramid.view import (
    view_config,
)
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPUnauthorized,
)

from icare.models.babies_model import BabiesModel
from icare.models.person_model import PersonModel
from icare.helpers.icare_helper import ICHelper

h = ICHelper()


@view_config(route_name='babies_index', renderer='babies.mako')
def index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.session['user_type'] == '1':
            return HTTPFound(location='/admins')
            
        return {'title': u'ข้อมูลการฝากครรภ์'}


@view_config(route_name='babies_get_total', renderer='json')
def get_list_total(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        babies = BabiesModel(request)

        try:
            total = babies.get_list_total()
            return {'ok': 1, 'total': total}
        except Exception as e:
            return {'ok': 0, 'msg': e.message}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='babies_get_total_by_birth', renderer='json')
def get_list_total_by_birth(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        csrf_token = request.params['csrf_token']
        start_date = h.jsdate_to_string(request.params['start_date'])
        end_date = h.jsdate_to_string(request.params['end_date'])

        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            babies = BabiesModel(request)

            try:
                total = babies.get_list_total_by_birth(start_date, end_date)
                return {'ok': 1, 'total': total}
            except Exception as e:
                return {'ok': 0, 'msg': e.message}
        else:
            return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='babies_get_list', request_method='POST', renderer='json')
def get_list(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:

                start = request.params['start']
                stop = request.params['stop']

                limit = int(stop) - int(start)

                babies = BabiesModel(request)
                person = PersonModel(request)

                rs = babies.get_list(int(start), int(limit))
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
                            'age': h.count_age(p['birth']),
                            'sex': p['sex'],
                            'bdate': h.to_thai_date(r['bdate']),
                            'bplace': r['bplace'],
                            'bhospcode': r['bhosp'],
                            'bhospname': h.get_hospital_name(request, r['bhosp']),
                            'btype': r['btype'],
                            'bweight': r['bweight'],
                            'mother': babies.get_mother(r['mpid'], r['hospcode']),
                            'care': babies.get_count_care(r['pid'], r['hospcode'])
                        }
                        rows.append(obj)

                    return {'ok': 1, 'rows': rows}
                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': 'Token not found.'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='babies_get_list_by_birth', request_method='POST', renderer='json')
def get_list_by_birth(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:

                start = request.params['start']
                stop = request.params['stop']
                start_date = h.jsdate_to_string(request.params['start_date'])
                end_date = h.jsdate_to_string(request.params['end_date'])

                limit = int(stop) - int(start)

                babies = BabiesModel(request)
                person = PersonModel(request)

                rs = babies.get_list_by_birth(start_date, end_date, int(start), int(limit))
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
                            'age': h.count_age(p['birth']),
                            'sex': p['sex'],
                            'bdate': h.to_thai_date(r['bdate']),
                            'bplace': r['bplace'],
                            'bhospcode': r['bhosp'],
                            'bhospname': h.get_hospital_name(request, r['bhosp']),
                            'btype': r['btype'],
                            'bweight': r['bweight'],
                            'mother': babies.get_mother(r['mpid'], r['hospcode']),
                            'care': babies.get_count_care(r['pid'], r['hospcode'])
                        }
                        rows.append(obj)

                    return {'ok': 1, 'rows': rows}
                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': 'Token not found.'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='babies_search', request_method='POST', renderer='json')
def search(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:

                cid = request.params['cid']

                babies = BabiesModel(request)
                person = PersonModel(request)

                rs = babies.search(cid)
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
                            'age': h.count_age(p['birth']),
                            'sex': p['sex'],
                            'bdate': h.to_thai_date(r['bdate']),
                            'bplace': r['bplace'],
                            'bhospcode': r['bhosp'],
                            'bhospname': h.get_hospital_name(request, r['bhosp']),
                            'btype': r['btype'],
                            'bweight': r['bweight'],
                            'mother': babies.get_mother(r['mpid'], r['hospcode']),
                            'care': babies.get_count_care(r['pid'], r['hospcode'])
                        }
                        rows.append(obj)

                    return {'ok': 1, 'rows': rows}
                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': 'Token not found.'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='babies_get_care', request_method='POST', renderer='json')
def get_care(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:
                pid = request.params['pid']
                babies = BabiesModel(request)
                hospcode = request.params['hospcode']

                rs = babies.get_care(pid, hospcode)

                if rs:
                    rows = []
                    for r in rs:
                        obj = {
                            'bcare': h.to_thai_date(r['bcare']),
                            'bcplace_code': r['bcplace'],
                            'bcplace_name': h.get_hospital_name(request, r['bcplace']),
                            'bcareresult': r['bcareresult'],
                            'food': r['food'],

                        }

                        rows.append(obj)

                    return {'ok': 1, 'rows': rows}

                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': "No token found."}


@view_config(route_name='babies_get_care_all', request_method='POST', renderer='json')
def get_care_all(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:
                cid = request.params['cid']

                babies = BabiesModel(request)
                rs = babies.get_care_all(cid)

                if rs:
                    rows = []
                    for r in rs:
                        obj = {
                            'bcare': h.to_thai_date(r['bcare']),
                            'bcplace_code': r['bcplace'],
                            'bcplace_name': h.get_hospital_name(request, r['bcplace']),
                            'bcareresult': r['bcareresult'],
                            'food': r['food'],
                            'appoint': babies.count_appointment(r['pid'], r['hospcode'], r['seq'])
                        }

                        rows.append(obj)

                    return {'ok': 1, 'rows': rows}

                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': "No token found."}


@view_config(route_name='babies_get_newborn', request_method='POST', renderer='json')
def get_newborn(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:
                pid = request.params['pid']
                hospcode = request.params['hospcode']

                babies = BabiesModel(request)
                rs = babies.get_newborn(pid, hospcode)

                if rs:
                    obj = {
                        'mother': babies.get_mother(rs['mpid'], rs['hospcode']),
                        'ga': rs['ga'],
                        'gravida': rs['gravida'],
                        'bdate': h.to_thai_date(rs['bdate']),
                        'btime': rs['btime'],
                        'bhosp_code': rs['bhosp'],
                        'bhosp_name': h.get_hospital_name(request, rs['bhosp']),
                        'bplace': rs['bplace'],
                        'birthno': rs['birthno'],
                        'btype': rs['btype'],
                        'bdoctor': rs['bdoctor'],
                        'bweight': rs['bweight'],
                        'asphyxia': rs['asphyxia'],
                        'vitk': rs['vitk'],
                        'tsh': rs['tsh'],
                        'tshresult': rs['tshresult'],
                    }

                    return {'ok': 1, 'rows': [obj]}

                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': "No token found."}