# -*- coding: utf8
from pyramid.view import (
    view_config,
)
from pyramid.httpexceptions import (
    HTTPFound,
)

from icare.helpers.icare_helper import ICHelper
from icare.models.ncdscreen_model import NCDScreenModel
from icare.models.person_model import PersonModel

h = ICHelper()


@view_config(route_name='ncdscreen_index', renderer='ncdscreen.mako')
def index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.session['user_type'] == '1':
            return HTTPFound(location='/admins')
            
        villages = h.get_villages(request, request.session['hospcode'])
        return {'title': u'ข้อมูลการคัดกรองความเสี่ยง เบาหวาน-ความดัน', 'villages': villages}


@view_config(route_name='ncdscreen_get_total', renderer='json')
def get_list_total(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        ncdscreen = NCDScreenModel(request)

        start_date = request.params['start_date']
        end_date = request.params['end_date']

        start_date = start_date.split('/')
        end_date = end_date.split('/')

        sy = int(start_date[2]) - 543
        ey = int(end_date[2]) - 543

        # get date for calculate age
        yx = ey - 15
        x = str(yx) + end_date[1] + end_date[0]

        #start_date = str(sy) + start_date[1] + start_date[0]
        #end_date = str(ey) + end_date[1] + end_date[0]

        total = ncdscreen.get_list_total(request.session['hospcode'], x)

        return {'ok': 1, 'total': total} if total else {'ok': 0, 'msg': u'ไม่พบข้อมูล'}

    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='ncdscreen_get_list', request_method='POST', renderer='json')
def get_list(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:

                start_date = request.params['start_date']
                end_date = request.params['end_date']

                start_date = start_date.split('/')
                end_date = end_date.split('/')

                sy = int(start_date[2]) - 543
                ey = int(end_date[2]) - 543

                # get date for calculate age
                yx = ey - 15
                x = str(yx) + end_date[1] + end_date[0]

                start_date = str(sy) + start_date[1] + start_date[0]
                end_date = str(ey) + end_date[1] + end_date[0]

                start = request.params['start']
                stop = request.params['stop']

                limit = int(stop) - int(start)

                ncdscreen = NCDScreenModel(request)

                rs = ncdscreen.get_list(request.session['hospcode'], x, int(start), int(limit))
                rows = []

                if rs:
                    for r in rs:

                        obj = {
                            'pid': r['pid'],
                            'cid': r['cid'],
                            'hospcode': r['hospcode'],
                            'fullname': r['name'] + '  ' + r['lname'],
                            'birth': h.to_thai_date(r['birth']),
                            'age': h.count_age(r['birth']),
                            'sex': r['sex'],
                            'typearea': r['typearea'],
                            'address': h.get_short_address(request, r['hid'], request.session['hospcode']),
                            'date_serv_th': h.to_thai_date(ncdscreen.get_date_serv(r['hospcode'], r['pid'], start_date, end_date)),
                            'date_serv': ncdscreen.get_date_serv(r['hospcode'], r['pid'], start_date, end_date)
                        }
                        rows.append(obj)

                    return {'ok': 1, 'rows': rows}
                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': 'Token not found.'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='ncdscreen_get_total_by_vid', renderer='json')
def get_list_total_by_vid(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        ncdscreen = NCDScreenModel(request)

        start_date = request.params['start_date']
        end_date = request.params['end_date']

        start_date = start_date.split('/')
        end_date = end_date.split('/')

        vid = request.params['vid']

        sy = int(start_date[2]) - 543
        ey = int(end_date[2]) - 543

        # get date for calculate age
        yx = ey - 15
        x = str(yx) + end_date[1] + end_date[0]

        #start_date = str(sy) + start_date[1] + start_date[0]
        #end_date = str(ey) + end_date[1] + end_date[0]

        hid = ncdscreen.get_hid_from_village(request.session['hospcode'], vid)
        total = ncdscreen.get_list_total_by_vid(request.session['hospcode'], x, hid)

        return {'ok': 1, 'total': total} if total else {'ok': 0, 'msg': u'ไม่พบข้อมูล'}

    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='ncdscreen_get_list_by_vid', request_method='POST', renderer='json')
def get_list_by_vid(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:

                start_date = request.params['start_date']
                end_date = request.params['end_date']

                vid = request.params['vid']

                start_date = start_date.split('/')
                end_date = end_date.split('/')

                sy = int(start_date[2]) - 543
                ey = int(end_date[2]) - 543

                # get date for calculate age
                yx = ey - 15
                x = str(yx) + end_date[1] + end_date[0]

                start_date = str(sy) + start_date[1] + start_date[0]
                end_date = str(ey) + end_date[1] + end_date[0]

                start = request.params['start']
                stop = request.params['stop']

                limit = int(stop) - int(start)

                ncdscreen = NCDScreenModel(request)

                hid = ncdscreen.get_hid_from_village(request.session['hospcode'], vid)
                rs = ncdscreen.get_list_by_vid(request.session['hospcode'], x, int(start), int(limit), hid)

                rows = []

                if rs:
                    for r in rs:

                        obj = {
                            'pid': r['pid'],
                            'cid': r['cid'],
                            'hospcode': r['hospcode'],
                            'fullname': r['name'] + '  ' + r['lname'],
                            'birth': h.to_thai_date(r['birth']),
                            'age': h.count_age(r['birth']),
                            'sex': r['sex'],
                            'typearea': r['typearea'],
                            'address': h.get_short_address(request, r['hid'], request.session['hospcode']),
                            'date_serv_th': h.to_thai_date(ncdscreen.get_date_serv(r['hospcode'], r['pid'], start_date, end_date)),
                            'date_serv': ncdscreen.get_date_serv(r['hospcode'], r['pid'], start_date, end_date)
                        }
                        rows.append(obj)

                    return {'ok': 1, 'rows': rows}
                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': 'Token not found.'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='ncdscreen_get_history', request_method='POST', renderer='json')
def get_history(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:

                cid = request.params['cid']
                start = request.params['start']
                stop = request.params['stop']

                limit = int(stop) - int(start)

                ncdscreen = NCDScreenModel(request)
                person = PersonModel(request)

                rs = ncdscreen.get_history(cid, int(start), int(limit))
                rows = []

                if rs:
                    for r in rs:

                        p = person.get_person_detail(r['pid'], r['hospcode'])

                        obj = {
                            'pid': r['pid'],
                            'fullname': p['name'] + '  ' + p['lname'],
                            'cid': p['cid'],
                            'birth': h.to_thai_date(p['birth']),
                            'age': h.count_age(p['birth']),
                            'hospcode': r['hospcode'],
                            'hospname': h.get_hospital_name(request, r['hospcode']),
                            'date_serv_th': h.to_thai_date(r['date_serv']),
                            'date_serv': r['date_serv'],
                            'sbp_1': r['sbp_1'],
                            'dbp_1': r['dbp_1'],
                            'bslevel': r['bslevel'],
                            'weight': r['weight'],
                            'height': r['height'],
                            'bslevel': r['bslevel']
                        }
                        rows.append(obj)

                    return {'ok': 1, 'rows': rows}
                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': 'Token not found.'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='ncdscreen_get_history_total', renderer='json')
def get_history_total(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        ncdscreen = NCDScreenModel(request)

        cid = request.params['cid']
        total = ncdscreen.get_history_total(cid)

        return {'ok': 1, 'total': total} if total else {'ok': 0, 'msg': u'ไม่พบข้อมูล'}

    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='ncdscreen_get_screen', request_method='POST', renderer='json')
def get_screen(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:  # is ajax request
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:

                hospcode = request.params['hospcode']
                pid = request.params['pid']
                date_serv = request.params['date_serv']

                ncdscreen = NCDScreenModel(request)

                rs = ncdscreen.get_screen(hospcode, pid, date_serv)
                obj = {
                    'date_serv': h.to_thai_date(rs['date_serv']),
                    'servplace': rs['servplace'],
                    'smoke': rs['smoke'],
                    'alcohol': rs['alcohol'],
                    'dmfamily': rs['dmfamily'],
                    'htfamily': rs['htfamily'],
                    'weight': rs['weight'],
                    'height': rs['height'],
                    'waist_cm': rs['waist_cm'],
                    'sbp_1': rs['sbp_1'],
                    'dbp_1': rs['dbp_1'],
                    'sbp_2': rs['sbp_2'],
                    'dbp_2': rs['dbp_2'],
                    'bslevel': rs['bslevel'],
                    'bstest': rs['bstest'],
                    'screenplace': rs['screenplace']
                }
                if rs:
                    return {'ok': 1, 'rows': [obj]}
                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': 'Token not found.'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}