# -*- coding: utf8

from pyramid.view import (
    view_config,
)
from pyramid.httpexceptions import (
    HTTPFound,
)

from icare.helpers.icare_helper import ICHelper
from icare.models.person_model import PersonModel
from icare.models.labor_other_model import LaborOtherModel

h = ICHelper()


@view_config(route_name='labor_other_index', renderer='labor_other.mako')
def labor_other_index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.session['user_type'] == '1':
            return HTTPFound(location='/admins')

        owners = h.get_labor_hospital_list(request)

        return {'title': u'ตรวจสอบข้อมูลคนในเขตไปคลอดที่หน่วยบริการอื่น', 'owners': owners}


@view_config(route_name='labor_other_get_list', request_method='POST', renderer='json')
def labor_other_get_list(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        if request.is_xhr:  # is ajax request
            start = request.params['start']
            stop = request.params['stop']

            start_date = h.jsdate_to_string(request.params['start_date'])
            end_date = h.jsdate_to_string(request.params['end_date'])

            start = int(start)
            limit = int(stop) - int(start)

            hospcode = request.params['hospcode']
            person = PersonModel(request)

            labor_other = LaborOtherModel(request)

            rs = labor_other.get_list(hospcode, start_date, end_date, start, limit)

            rows = []
            if rs:
                for r in rs:
                    p = person.get_person_detail(r['pid'], hospcode)
                    labor = labor_other.get_labor_detail(r['pid'], r['gravida'], r['hospcode'])
                    obj = {
                        'cid': p['cid'],
                        'pid': p['pid'],
                        'fullname': '%s %s' % (p['name'], p['lname']),
                        'age': h.count_age(p['birth']),
                        'birth': h.to_thai_date(p['birth']),
                        'bdate': h.to_thai_date(r['bdate']),
                        #'bresult': labor['bresult'],
                        #'btype': labor['btype'],
                        'bhospname': h.get_hospital_name(request, labor['bhosp']),
                        'bhospcode': labor['bhosp'],
                        'gravida': r['gravida'],
                        'hospcode': r['hospcode'],
                        'hospname': h.get_hospital_name(request, r['hospcode']),
                        'address': h.get_address_from_catm(request, r['address']['vid']),
                        'house': r['address']['house'] if 'house' in r['address'] else '00'
                    }

                    rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='labor_other_get_total', renderer='json')
def labor_other_get_total(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        labor_other = LaborOtherModel(request)

        start_date = h.jsdate_to_string(request.params['start_date'])
        end_date = h.jsdate_to_string(request.params['end_date'])

        hospcode = request.params['hospcode']

        total = labor_other.get_total(hospcode, start_date, end_date)
        return {'ok': 1, 'total': total}


@view_config(route_name='labor_other_do_process', renderer='json')
def labor_other_do_process(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            labor_other = LaborOtherModel(request)

            start_date = h.jsdate_to_string(request.params['start_date'])
            end_date = h.jsdate_to_string(request.params['end_date'])

            hospcode = request.params['hospcode']

            labor_other.do_process_list(hospcode, start_date, end_date)
            return {'ok': 1}
        else:
            return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='labor_get_labor', renderer='json')
def labor_get_labor(request):

    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'please login.'}

    if request.is_xhr:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:
            pid = request.params['pid']
            gravida = request.params['gravida']
            hospcode = request.params['hospcode']

            labor_other = LaborOtherModel(request)
            person = PersonModel(request)

            r = labor_other.get_labor_detail(pid, gravida, hospcode)
            p = person.get_person_detail(pid, hospcode)

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