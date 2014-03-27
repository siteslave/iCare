# -*- coding: utf8

from pyramid.view import (
    view_config,
)
from pyramid.httpexceptions import (
    HTTPFound,
)

from icare.helpers.icare_helper import ICHelper
from icare.models.person_model import PersonModel
from icare.models.labor_other_model import LaborModel

h = ICHelper()


@view_config(route_name='labor_other_index', renderer='labor_other.mako')
def labor_other_index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.session['user_type'] == '1':
            return HTTPFound(location='/admins')

        return {'title': u'ตรวจสอบข้อมูลคนในเขตไปคลอดที่หน่วยบริการอื่น'}


@view_config(route_name='labor_other_get_list', request_method='POST', renderer='json')
def labor_other_get_list(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:  # is ajax request
            start = request.params['start']
            stop = request.params['stop']

            start_date = h.jsdate_to_string(request.params['start_date'])
            end_date = h.jsdate_to_string(request.params['end_date'])

            start = int(start)
            limit = int(stop) - int(start)

            hospcode = request.params['hospcode'] if 'hospcode' in request.params else request.session['hospcode']

            person = PersonModel(request)
            labor = LaborModel(request)

            rs = labor.get_list(hospcode, start_date, end_date, start, limit)

            rows = []
            if rs:
                for r in rs:
                    p = person.get_person_detail(r['pid'], hospcode)

                    obj = {
                        'cid': p['cid'],
                        'pid': p['pid'],
                        'fullname': '%s %s' % (p['name'], p['lname']),
                        'age': h.count_age(p['birth']),
                        'birth': h.to_thai_date(p['birth']),
                        'bdate': r['bdate'],
                        'bresult': r['bresult'],
                        'btype': r['btype'],
                        'bhospname': h.get_hospital_name(request, r['bhosp']),
                        'bhospcode': r['bhosp'],
                        'gravida': r['gravida'],
                        'hospcode': r['hospcode'],
                        'hospname': h.get_hospital_name(request, r['hospcode']),
                        'address': h.get_address(request, p['hid'], p['hospcode'])
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

        labor = LaborModel(request)

        start_date = h.jsdate_to_string(request.params['start_date'])
        end_date = h.jsdate_to_string(request.params['end_date'])

        hospcode = request.params['hospcode'] if 'hospcode' in request.params else request.session['hospcode']

        try:
            total = labor.get_total(hospcode, start_date, end_date)
            return {'ok': 1, 'total': total}
        except Exception as e:
            return {'ok': 0, 'msg': e.message}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}