# -*- coding: utf8
from pyramid.view import (
    view_config,
)
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPUnauthorized,
)

from icare.models.wbc02_model import Wbc02Model
from icare.models.mch_model import MchModel
from icare.helpers.icare_helper import ICHelper

h = ICHelper()


@view_config(route_name='wbc02_index', renderer='wbc02.mako')
def index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.session['user_type'] == '1':
            return HTTPFound(location='/admins')
            
        villages = h.get_villages(request, request.session['hospcode'])
        return {'title': u'ข้อมูลเด็ก 0-2 ปี', 'villages': villages}


@view_config(route_name='wbc02_get_total', renderer='json')
def get_list_total(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        wbc = Wbc02Model(request)

        start_date = h.jsdate_to_string(request.params['start_date'])
        end_date = h.jsdate_to_string(request.params['end_date'])

        try:
            total = wbc.get_list_total(request.session['hospcode'], start_date, end_date)
            return {'ok': 1, 'total': total}
        except Exception as e:
            return {'ok': 0, 'msg': e.message}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='wbc02_get_list', request_method='POST', renderer='json')
def get_list(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:

                start_date = h.jsdate_to_string(request.params['start_date'])
                end_date = h.jsdate_to_string(request.params['end_date'])

                start = request.params['start']
                stop = request.params['stop']

                limit = int(stop) - int(start)

                wbc = Wbc02Model(request)

                rs = wbc.get_list(request.session['hospcode'], start_date, end_date, int(start), int(limit))
                rows = []

                if rs:
                    for r in rs:
                        vaccine = {
                            'bcg': wbc.get_bcg(r['hospcode'], r['pid']),
                            'dtphb3': wbc.get_dtphb3(r['hospcode'], r['pid']),
                            'opv3': wbc.get_opv3(r['hospcode'], r['pid']),
                            'dtp4': wbc.get_dtp4(r['hospcode'], r['pid']),
                            'opv4': wbc.get_opv4(r['hospcode'], r['pid']),
                            'je2': wbc.get_je2(r['hospcode'], r['pid']),
                        }

                        obj = {
                            'pid': r['pid'],
                            'cid': r['cid'],
                            'hospcode': r['hospcode'],
                            'fullname': r['name'] + '  ' + r['lname'],
                            'birth': h.to_thai_date(r['birth']),
                            'age': h.count_age(r['birth']),
                            'sex': r['sex'],
                            'vaccines': vaccine,
                            'address': h.get_short_address(request, r['hid'], request.session['hospcode']),
                            'nutrition': wbc.count_nutrition(r['hospcode'], r['pid'])
                        }
                        rows.append(obj)

                    return {'ok': 1, 'rows': rows}
                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': 'Token not found.'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='wbc02_get_total_by_vid', renderer='json')
def get_list_total_by_vid(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        wbc = Wbc02Model(request)

        start_date = h.jsdate_to_string(request.params['start_date'])
        end_date = h.jsdate_to_string(request.params['end_date'])
        vid = request.params['vid']

        hid = wbc.get_hid_from_village(request.session['hospcode'], vid)

        try:
            total = wbc.get_list_total_by_vid(request.session['hospcode'], start_date, end_date, hid)
            return {'ok': 1, 'total': total}
        except Exception as e:
            return {'ok': 0, 'msg': e.message}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='wbc02_get_list_by_vid', request_method='POST', renderer='json')
def get_list_by_vid(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:

                start_date = h.jsdate_to_string(request.params['start_date'])
                end_date = h.jsdate_to_string(request.params['end_date'])
                vid = request.params['vid']

                start = request.params['start']
                stop = request.params['stop']

                limit = int(stop) - int(start)

                wbc = Wbc02Model(request)
                hid = wbc.get_hid_from_village(request.session['hospcode'], vid)

                rs = wbc.get_list_by_vid(request.session['hospcode'], start_date, end_date, int(start), int(limit), hid)
                rows = []

                if rs:
                    for r in rs:
                        vaccine = {
                            'bcg': wbc.get_bcg(r['hospcode'], r['pid']),
                            'dtphb3': wbc.get_dtphb3(r['hospcode'], r['pid']),
                            'opv3': wbc.get_opv3(r['hospcode'], r['pid']),
                            'dtp4': wbc.get_dtp4(r['hospcode'], r['pid']),
                            'opv4': wbc.get_opv4(r['hospcode'], r['pid']),
                            'je2': wbc.get_je2(r['hospcode'], r['pid']),
                        }

                        obj = {
                            'pid': r['pid'],
                            'cid': r['cid'],
                            'hospcode': r['hospcode'],
                            'fullname': r['name'] + '  ' + r['lname'],
                            'birth': h.to_thai_date(r['birth']),
                            'age': h.count_age(r['birth']),
                            'sex': r['sex'],
                            'vaccines': vaccine,
                            'address': h.get_short_address(request, r['hid'], request.session['hospcode']),
                            'nutrition': wbc.count_nutrition(r['hospcode'], r['pid'])
                        }
                        rows.append(obj)

                    return {'ok': 1, 'rows': rows}
                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': 'Token not found.'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='wbc02_get_vaccines', request_method='POST', renderer='json')
def get_vaccines(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:

                pid = request.params['pid']

                wbc = Wbc02Model(request)

                bcg = wbc.get_bcg(request.session['hospcode'], pid)
                dtphb3 = wbc.get_dtphb3(request.session['hospcode'], pid)
                opv3 = wbc.get_opv3(request.session['hospcode'], pid)
                dtp4 = wbc.get_dtp4(request.session['hospcode'], pid)
                opv4 = wbc.get_opv4(request.session['hospcode'], pid)
                je2 = wbc.get_je2(request.session['hospcode'], pid)

                vaccines = [
                    {
                        'name': 'BCG',
                        'date_serv': bcg['date_serv'] if bcg else None,
                        'vaccineplace_code': bcg['vaccineplace_code'] if bcg else None,
                        'vaccineplace_name': bcg['vaccineplace_name'] if bcg else None
                    },
                    {
                        'name': 'DTP-HB3',
                        'date_serv': dtphb3['date_serv'] if dtphb3 else None,
                        'vaccineplace_code': dtphb3['vaccineplace_code'] if dtphb3 else None,
                        'vaccineplace_name': dtphb3['vaccineplace_name'] if dtphb3 else None
                    },
                    {
                        'name': 'OPV3',
                        'date_serv': opv3['date_serv'] if opv3 else None,
                        'vaccineplace_code': opv3['vaccineplace_code'] if opv3 else None,
                        'vaccineplace_name': opv3['vaccineplace_name'] if opv3 else None
                    },
                    {
                        'name': 'OPV4',
                        'date_serv': opv4['date_serv'] if opv4 else None,
                        'vaccineplace_code': opv4['vaccineplace_code'] if opv4 else None,
                        'vaccineplace_name': opv4['vaccineplace_name'] if opv4 else None
                    },
                    {
                        'name': 'DTP4',
                        'date_serv': dtp4['date_serv'] if dtp4 else None,
                        'vaccineplace_code': dtp4['vaccineplace_code'] if dtp4 else None,
                        'vaccineplace_name': dtp4['vaccineplace_name'] if dtp4 else None
                    },
                    {
                        'name': 'JE2',
                        'date_serv': je2['date_serv'] if je2 else None,
                        'vaccineplace_code': je2['vaccineplace_code'] if je2 else None,
                        'vaccineplace_name': je2['vaccineplace_name'] if je2 else None
                    },
                ]

                return {'ok': 1, 'rows': vaccines}
            else:
                return {'ok': 0, 'msg': 'Token invalid.'}
        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='wbc02_search_visit', renderer='json')
def search_visit(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        wbc = Wbc02Model(request)
        mch = MchModel(request)

        cid = request.params['cid']

        rs = wbc.search_visit(cid)

        if rs:
            rows = []
            for r in rs:
                obj = {
                    'code': r['vaccinetype'],
                    'name': h.get_vaccine_name(request, r['vaccinetype']),
                    'hospcode': r['vaccineplace'],
                    'hospname': h.get_hospital_name(request, r['vaccineplace']),
                    'date_serv': h.to_thai_date(r['date_serv']),
                    'appoint': mch.count_appointment(r['pid'], r['hospcode'], r['seq']),
                    'seq': r['seq'],
                    'hospcode': r['hospcode'],
                    'pid': r['pid']
                }

                rows.append(obj)
            return {'ok': 1, 'rows': rows}
        else:
            return {'ok': 0, 'msg': u'ไม่พบรายการ'}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='wbc02_get_nutrition', renderer='json')
def get_nutrition(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        wbc = Wbc02Model(request)

        cid = request.params['cid']

        rs = wbc.get_nutrition(cid)

        if rs:
            rows = []
            for r in rs:
                obj = {
                    'nutritionplace_code': r['nutritionplace'],
                    'nutritionplace_name': h.get_hospital_name(request, r['nutritionplace']),
                    'date_serv': h.to_thai_date(r['date_serv']),
                    'weight': r['weight'],
                    'height': r['height'],
                    'headcircum': r['headcircum'],
                    'childdevelop': r['childdevelop'],
                    'food': r['food'],
                    'bottle': r['bottle']
                }

                rows.append(obj)

            return {'ok': 1, 'rows': rows}
        else:
            return {'ok': 0, 'msg': u'ไม่พบรายการ'}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='wbc02_get_nutrition_owner', renderer='json')
def get_nutrition_owner(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        wbc = Wbc02Model(request)

        pid = request.params['pid']
        hospcode = request.params['hospcode']

        rs = wbc.get_nutrition_owner(pid, hospcode)

        if rs:
            rows = []
            for r in rs:
                obj = {
                    'nutritionplace_code': r['nutritionplace'],
                    'nutritionplace_name': h.get_hospital_name(request, r['nutritionplace']),
                    'date_serv': h.to_thai_date(r['date_serv']),
                    'weight': r['weight'],
                    'height': r['height'],
                    'headcircum': r['headcircum'],
                    'childdevelop': r['childdevelop'],
                    'food': r['food'],
                    'bottle': r['bottle']
                }

                rows.append(obj)

            return {'ok': 1, 'rows': rows}
        else:
            return {'ok': 0, 'msg': u'ไม่พบรายการ'}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}

