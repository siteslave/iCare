# -*- coding: utf8

from pyramid.view import (
    view_config,
    )
from pyramid.httpexceptions import (
    HTTPFound,
    )

from icare.helpers.icare_helper import ICHelper
from icare.models.users_admin_model import UsersAdminModel

h = ICHelper()


@view_config(route_name='users_admin_index', renderer='users_admin.mako')
def users_admin_index(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.session['user_type'] == '1':
            return HTTPFound(location='/admins')

        if request.session['user_type'] == '3':
            return HTTPFound(location='/denied')

        owners = h.get_owner_list(request, request.session['owner'])

        return {'title': u'ทะเบียนผู้ใช้งาน', 'owners': owners}


@view_config(route_name='users_admin_get_total', renderer='json')
def users_admin_get_total(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            users = UsersAdminModel(request)
            try:
                total = users.get_total(request.session['owner'])
                return {'ok': 1, 'total': total}
            except Exception as e:
                return {'ok': 0, 'msg': e.message}
        else:
            return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='users_admin_get_list', request_method='POST', renderer='json')
def users_admin_get_list(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:

        if request.is_xhr:  # is ajax request
            start = request.params['start'] if 'start' in request.params else 0
            stop = request.params['stop'] if 'stop' in request.params else 25

            limit = int(stop) - int(start)

            users = UsersAdminModel(request)
            rs = users.get_list(request.session['owner'], int(start), int(limit))

            #return {'ok': 1, 'rows': rs.count()}
            if rs:
                rows = []
                for r in rs:
                    obj = {
                        'id': str(r['_id']),
                        'cid': r['cid'] if 'cid' in r else '-',
                        'username': r['username'],
                        'fullname': r['fullname'],
                        #'birth': r['birth'] if 'birth' in r else '-',
                        #'sex': r['sex'] if 'sex' in r else '-',
                        'position': r['position'] if 'position' in r else '-',
                        'is_active': r['is_active'] if 'is_active' in r else 'N',
                        'hospcode': r['hospcode'],
                        'hospname': h.get_hospital_name(request, r['hospcode'])

                    }

                    rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='users_admin_search', request_method='POST', renderer='json')
def users_admin_search(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:

        if request.is_xhr:  # is ajax request
            users = UsersAdminModel(request)

            query = request.params['query']

            rs = users.search(query, request.session['owner'])

            if rs:
                rows = []
                for r in rs:
                    obj = {
                        'id': str(r['_id']),
                        'cid': r['cid'] if 'cid' in r else '-',
                        'username': r['username'],
                        'fullname': r['fullname'],
                        #'birth': r['birth'] if 'birth' in r else '-',
                        #'sex': r['sex'] if 'sex' in r else '-',
                        'position': r['position'] if 'position' in r else '-',
                        'is_active': r['is_active'] if 'is_active' in r else 'N',
                        'hospcode': r['hospcode'],
                        'hospname': h.get_hospital_name(request, r['hospcode'])

                    }

                    rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}

        else:
            return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='users_admin_save', renderer='json')
def users_admin_save(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:
            try:
                users = UsersAdminModel(request)

                username = request.params['username']
                password = h.get_hash(request.params['password'])
                cid = request.params['cid']
                fullname = request.params['fullname']
                position = request.params['position']
                hospcode = request.params['hospcode']
                is_active = request.params['is_active']

                user_id = request.params['id'] if len(request.params['id']) > 0 else False

                owner = request.session['owner']

                if user_id:
                    users.update(user_id, hospcode, cid, fullname, position, is_active)
                else:
                    users.save(hospcode, username, password, cid, fullname, position, owner, is_active)

                return {'ok': 1}

            except Exception as ex:
                return {'ok': 0, 'msg': ex.message}
        else:
            return {'ok': 0, 'msg': 'Can\'t save data.'}


@view_config(route_name='users_admin_remove', renderer='json')
def users_admin_remove(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:
            try:
                user_id = request.params['id']

                users = UsersAdminModel(request)
                users.remove(user_id)
                return {'ok': 1}

            except Exception as e:
                return {'ok': 0, 'msg': e.message}
        else:
            return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='users_admin_chwpass', renderer='json')
def users_admin_chwpass(request):
    if 'logged' not in request.session:
        return {'ok': 0, 'msg': 'Please login.'}
    else:
        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:
            try:
                user_id = request.params['id']
                newpass = h.get_hash(request.params['pw'])

                users = UsersAdminModel(request)
                users.change_password(user_id, newpass)

                return {'ok': 1}

            except Exception as e:
                return {'ok': 0, 'msg': e.message}
        else:
            return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='users_denied', renderer='users_denied.mako')
def users_denied(request):
    return {'title': u'Permission denied.'}