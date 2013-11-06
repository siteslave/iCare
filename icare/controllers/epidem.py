# -*- coding: utf8
from pyramid.view import (
    view_config,
)
from pyramid.httpexceptions import (
    HTTPFound,
)

from icare.helpers.icare_helper import ICHelper
from icare.models.person_model import PersonModel
from icare.models.epidem_model import EpidemModel

h = ICHelper()


@view_config(route_name='epidem_index', renderer='epidem.mako')
def index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.session['user_type'] == '1':
            return HTTPFound(location='/admins')
            
        code506 = h.get_code506_list(request)
        return {'title': u'ข้อมูลระบาดวิทยา', 'code506': code506}


@view_config(route_name='epidem_get_total', renderer='json')
def get_list_total(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        epidem = EpidemModel(request)

        start_date = request.params['start_date']
        end_date = request.params['end_date']

        code506 = request.params['code506']
        ptstatus = request.params['ptstatus']

        start_date = start_date.split('/')
        end_date = end_date.split('/')

        sy = int(start_date[2]) - 543
        ey = int(end_date[2]) - 543

        start_date = str(sy) + start_date[1] + start_date[0]
        end_date = str(ey) + end_date[1] + end_date[0]

        if code506 and not ptstatus:
            total = epidem.get_list_total_by_code506(request.session['hospcode'], code506, start_date, end_date)
        elif ptstatus and not code506:
            total = epidem.get_list_total_by_ptstatus(request.session['hospcode'], ptstatus, start_date, end_date)
        elif ptstatus and code506:
            total = epidem.get_list_total_by_code506_ptstatus(request.session['hospcode'], code506, ptstatus, start_date, end_date)
        else:
            total = epidem.get_list_total(request.session['hospcode'], start_date, end_date)

        return {'ok': 1, 'total': total} if total else {'ok': 0, 'msg': u'ไม่พบข้อมูล'}

    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='epidem_get_info', request_method='POST', renderer='json')
def get_info(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:
            csrf_token = request.params['csrf_token']
            is_token = (csrf_token == unicode(request.session.get_csrf_token()))

            if is_token:

                hospcode = request.params['hospcode']
                pid = request.params['pid']
                seq = request.params['seq']
                diagcode = request.params['diagcode']

                epidem = EpidemModel(request)
                person = PersonModel(request)

                rs = epidem.get_info(hospcode, pid, seq, diagcode)
                p = person.get_person_detail(pid, hospcode)

                if rs:
                    if p:
                        village = '0%s' % rs['illvillage'] if len(rs['illvillage']) < 2 else rs['illvillage']
                        catm = '%s%s%s%s' % (rs['illchanwat'], rs['illampur'], rs['illtambon'], village)

                        obj = {
                            'an': rs['an'],
                            'cid': rs['cid'],
                            'pid': rs['pid'],
                            'fullname': '%s %s' % (p['name'], p['lname']),
                            'sex': p['sex'],
                            'birth': h.to_thai_date(p['birth']),
                            'age': h.count_age(p['birth']),
                            'code506': '[%s] %s' % (rs['code506'], h.get_code506_name(request, rs['code506'])),
                            'diag': '[%s] %s' % (rs['diagcode'], h.get_diag_name(request, rs['diagcode'])),
                            'date_death': h.to_thai_date(rs['date_death']),
                            'date_serv': h.to_thai_date(rs['date_serv']),
                            'illdate': h.to_thai_date(rs['illdate']),
                            'ill_address': '%s %s' % (rs['illhouse'], h.get_address_from_catm(request, catm)),
                            'latLng': '%s, %s' % (rs['latitude'], rs['longitude']),
                            'ptstatus': rs['ptstatus'],
                            'complication': h.get_complication_name(request, rs['complication']),
                        }
                        return {
                            'ok': 1, 'rows': obj
                        }
                    else:
                        return {
                            'ok': 0, 'msg': u'ไม่พบข้อมูลบุคคล'
                        }
                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': 'Invalid token.'}


@view_config(route_name='epidem_get_list', request_method='POST', renderer='json')
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

                code506 = request.params['code506']
                ptstatus = request.params['ptstatus']

                start_date = start_date.split('/')
                end_date = end_date.split('/')

                sy = int(start_date[2]) - 543
                ey = int(end_date[2]) - 543

                start_date = str(sy) + start_date[1] + start_date[0]
                end_date = str(ey) + end_date[1] + end_date[0]

                start = request.params['start']
                stop = request.params['stop']

                limit = int(stop) - int(start)

                epidem = EpidemModel(request)
                person = PersonModel(request)

                if code506 and not ptstatus:
                    rs = epidem.get_list_by_code506(request.session['hospcode'], code506, start_date, end_date, int(start), int(limit))
                elif ptstatus and not code506:
                    rs = epidem.get_list_by_ptstatus(request.session['hospcode'], ptstatus, start_date, end_date, int(start), int(limit))
                elif ptstatus and code506:
                    rs = epidem.get_list_by_code506_ptstatus(request.session['hospcode'], code506, ptstatus, start_date, end_date, int(start), int(limit))
                else:
                    rs = epidem.get_list(request.session['hospcode'], start_date, end_date, int(start), int(limit))

                rows = []

                if rs:
                    for r in rs:

                        p = person.get_person_detail(r['pid'], r['hospcode'])

                        if p:

                            village = '0%s' % r['illvillage'] if len(r['illvillage']) < 2 else r['illvillage']
                            catm = '%s%s%s%s' % (r['illchanwat'], r['illampur'], r['illtambon'], village)

                            obj = {
                                'pid': r['pid'],
                                'cid': p['cid'],
                                'fullname': p['name'] + '  ' + p['lname'],
                                'birth': h.to_thai_date(p['birth']),
                                'age': h.count_age(p['birth']),
                                'sex': p['sex'],
                                'ill_address': '%s %s' % (r['illhouse'], h.get_address_from_catm(request, catm)),
                                'illdate': h.to_thai_date(r['illdate']),
                                'date_serv': h.to_thai_date(r['date_serv']),
                                'code506': r['code506'],
                                'code506_name': h.get_code506_name(request, r['code506']),
                                'ptstatus': r['ptstatus'],
                                'seq': r['seq'],
                                'diagcode': r['diagcode'],
                                'diagname': h.get_diag_name(request, r['diagcode']),
                                'hospcode': r['hospcode']
                            }
                        else:
                            obj = {
                                'pid': '-',
                                'cid': '-',
                                'fullname': '-',
                                'birth': '-',
                                'age': '-',
                                'sex': '-',
                                'ill_address': '-',
                                'illdate': '-',
                                'code506': '-',
                                'code506_name': '-',
                                'ptstatus': '-'
                            }
                        rows.append(obj)

                    return {'ok': 1, 'rows': rows}
                else:
                    return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            else:
                return {'ok': 0, 'msg': 'Token not found.'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}

