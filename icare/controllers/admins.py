# -*- coding: utf8

from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPFound
)

from icare.models.admin_model import AdminModel
from icare.helpers.icare_helper import ICHelper
from bson.objectid import ObjectId

h = ICHelper()


@view_config(route_name='admin_index', renderer='admins.mako')
def index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    if request.session['user_type'] != '1':
        return HTTPFound(location='/admins/users')
        
    return {'title': u'Admin'}


@view_config(route_name="admin_users", renderer="admins_users.mako")
def user_view(request):
    if "logged" not in request.session:
        return HTTPFound(location="/signin")

    if request.session["user_type"] != '1':
        return HTTPFound(location="/")

    hospitals = h.get_hospital_list(request)

    return {"title": u'Users management', "hospitals": hospitals}


@view_config(route_name="admin_save", request_method='POST', renderer='json')
def save_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.session['user_type'] != '1':
        return {'ok': 0, 'msg': 'Not admin.'}
    else:

        data = {
            'fullname': request.params['fullname'],
            'cid': request.params['cid'],
            'hospcode': request.params['department'],
            'username': request.params['username'],
            'password': request.params['password'],
            'user_type': request.params['user_type'],
            'user_status': request.params['user_status'],
            'position': request.params['position']
        }

        admin = AdminModel(request)

        id = request.params["id"] if 'id' in request.params else False

        if not id:

            is_duplicate = admin.check_duplicate(request.params['username'])

            if is_duplicate:
                return {'ok': 0, 'msg': 'ชื่อผู้ใช้งานนี้ถูกใช้แล้ว กรุณาเลือกใหม่'}
            else:
                rs = admin.save(data)

                if rs:
                    return {'ok': 1}
                else:
                    return {'ok': 0, 'msg': 'ไม่สามารถบันทึกรายการได้'}

        else:
            data['id'] = ObjectId(request.params['id'])
            admin.update(data)

            return {'ok': 1}


@view_config(route_name='users_get_list', request_method='POST', renderer='json')
def get_user_list(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:  # is ajax request
            start = request.params['start'] if 'start' in request.params else 0
            stop = request.params['stop'] if 'stop' in request.params else 25

            limit = int(stop) - int(start)

            admin = AdminModel(request)

            rs = admin.get_user_list(int(start), int(limit))

            rows = []
            if rs:
                for r in rs:

                    obj = {
                        'id': str(r['_id']),
                        'username': r['username'],
                        'cid': r['cid'] if 'cid' in r else '-',
                        'hospcode': r['hospcode'] if 'hospcode' in r else '-',
                        'hospname': h.get_hospital_name(request, r['hospcode']),
                        'fullname': r['fullname'] if 'fullname' in r else '-',
                        'user_type': r['user_type'] if 'user_type' in r else '-',
                        'user_status': r['user_status'] if 'user_status' in r else '0',
                        'position': r['position'] if 'position' in r else '-'
                    }

                    rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}


@view_config(route_name='users_get_total', renderer='json')
def get_user_total(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.is_xhr:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            admin = AdminModel(request)

            try:
                total = admin.get_user_total()
                return {'ok': 1, 'total': total}
            except Exception as e:
                return {'ok': 0, 'msg': e.message}
        else:
            return {'ok': 0, 'msg': 'Not authorized.'}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='users_remove', renderer='json')
def remove_user(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.is_xhr:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            admin = AdminModel(request)
            id = ObjectId(request.params['id'])

            try:
                admin.remove_user(id)
                return {'ok': 1}
            except Exception as e:
                return {'ok': 0, 'msg': e.message}
        else:
            return {'ok': 0, 'msg': 'Not authorized.'}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='users_changepass', renderer='json')
def change_password(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    if request.is_xhr:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            admin = AdminModel(request)

            id = ObjectId(request.params['id'])
            password = request.params['password']

            try:
                admin.change_password(id, password)
                return {'ok': 1}
            except Exception as e:
                return {'ok': 0, 'msg': e.message}
        else:
            return {'ok': 0, 'msg': 'Not authorized.'}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='app_change_password', renderer='json')
def app_change_password(request):
    admin = AdminModel(request)

    id = request.session['id']
    password = request.params['password']

    try:
        admin.change_password(ObjectId(id), password)
        return {'ok': 1}
    except Exception as e:
        return {'ok': 0, 'msg': e.message}