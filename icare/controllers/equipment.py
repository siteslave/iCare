# -*- coding: utf8
from bson import ObjectId
from pyramid.view import (
    view_config,
)
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound)

from icare.helpers.icare_helper import ICHelper
from icare.models.equipment_model import EquipmentModel

#Load helper
h = ICHelper()


@view_config(route_name='equipment_index', renderer='equipment.mako')
def index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.session['user_type'] == '1':
            return HTTPFound(location='/admins')

        if request.session['user_type'] == '3':
            return HTTPFound(location='/denied')

        return {'title': u'ข้อมูลครุภัณฑ์'}


@view_config(route_name='equipment_services', renderer='equipment_services.mako')
def service_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.session['user_type'] == '1':
            return HTTPFound(location='/admins')

        equipment = EquipmentModel(request)
        equipment_id = request.matchdict['id']

        if equipment.check_exist(equipment_id):
            return {'title': u'ข้อมูล/ประวัติการซ่อม'}
        else:
            return HTTPNotFound()


@view_config(route_name="save_equipment", request_method='POST', renderer='json')
def save_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            # Get parameters
            equipment_id = request.params["id"] if 'id' in request.params else False
            name = request.params["name"]
            serial = request.params["serial"]
            durableGoods = request.params["durableGoods"]
            purchaseDate = request.params["purchaseDate"]
            status = request.params["status"]

            # Data is valid
            if name:
                equipment = EquipmentModel(request)

                if equipment_id:
                    # update
                    equipment.update(ObjectId(equipment_id), name, serial, durableGoods, purchaseDate, status)
                    return {"ok": 1, "msg": "update"}
                else:
                    rs = equipment.save_new(request.session['hospcode'], name, serial, durableGoods, purchaseDate, status)
                    if rs:
                        return {"ok": 1, "msg": "save"}
                    # Has error
                    else:
                        return {"ok": 0, "msg": u"ไม่สามารถบันทึกรายการได้"}

            else:
                return {"ok": 0, "msg": u"ข้อมูลไม่สมบูรณ์ กรุณาตรวจสอบ"}

        else:
            return {"ok": 0, "msg": "CSRF failed."}


@view_config(route_name="equipment_save_service", request_method='POST', renderer='json')
def save_service_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

#save_service(self, id, service_date, service_type, company,
# contact_name, telephone, email, service_status, return_date
        if is_token:

            # Get parameters
            equipment_id = request.params["id"]
            service_id = request.params["service_id"] if 'service_id' in request.params else False
            service_date = request.params["service_date"]
            service_type = request.params["service_type"]
            company = request.params["company"]
            contact_name = request.params["contact_name"]
            telephone = request.params["telephone"]
            email = request.params["email"]
            service_status = request.params["service_status"]
            return_date = request.params["return_date"]

            # Data is valid
            if service_date:
                equipment = EquipmentModel(request)

                if service_id:
                    # update
                    equipment.update_service(ObjectId(equipment_id), ObjectId(service_id), service_date, service_type, company,
                                             contact_name, telephone, email, service_status, return_date)
                    return {"ok": 1, "msg": "update"}
                else:
                    rs = equipment.save_service(ObjectId(equipment_id), service_date, service_type, company, contact_name,
                                                telephone, email, service_status, return_date)
                    if rs:
                        return {"ok": 1, "msg": "save"}
                    # Has error
                    else:
                        return {"ok": 0, "msg": u"ไม่สามารถบันทึกรายการได้"}

            else:
                return {"ok": 0, "msg": u"ข้อมูลไม่สมบูรณ์ กรุณาตรวจสอบ"}

        else:
            return {"ok": 0, "msg": "CSRF failed."}


@view_config(route_name='equipment_get_detail', request_method='POST', renderer='json')
def get_equipment_detail(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    equipment_id = request.params['id']

    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:
        equipment = EquipmentModel(request)

        rs = equipment.get_detail(equipment_id)

        if rs:
            obj = {
                'name': rs['name'],
                'durable_goods_number': rs['durable_goods_number'],
                'serial': rs['serial']
            }

            return {'ok': 1, 'rows': obj}
        else:
            return {'ok': 0, 'msg': 'Record not found'}


@view_config(route_name='equipment_remove_service', request_method='POST', renderer='json')
def remove_service(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    service_id = request.params['sid']
    equipment_id = request.params['eqid']

    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:
        equipment = EquipmentModel(request)

        equipment.remove_service(equipment_id, service_id)

        return {'ok': 1}
    else:
        return {'ok': 0, 'msg': 'Token key invalid'}


@view_config(route_name='equipment_get_service_detail', request_method='POST', renderer='json')
def get_equipment_service_detail(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    service_id = request.params['sid']
    equipment_id = request.params['eqid']

    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:
        equipment = EquipmentModel(request)

        rs = equipment.get_service_detail(equipment_id, service_id)

        if rs:

            for r in rs['services']:
                if str(r['_id']) == service_id:
                    obj = {
                        'id': str(r['_id']),
                        'email': r['email'] if 'email' in r else '-',
                        'telephone': r['telephone'] if 'telephone' in r else '-',
                        'service_status': r['service_status'] if 'service_status' in r else '-',
                        'service_type': r['service_type'] if 'service_type' in r else '-',
                        'company': r['company'] if 'company' in r else '-',
                        'service_date': r['service_date'] if 'service_date' in r else '-',
                        'contact_name': r['contact_name'] if 'contact_name' in r else '-',
                        'return_date': r['return_date'] if 'return_date' in r else '-',
                    }

            return {'ok': 1, 'rows': obj}
        else:
            return {'ok': 0, 'msg': 'Record not found'}


@view_config(route_name='equipment_get_service_list', request_method='POST', renderer='json')
def get_service_list(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    equipment_id = request.params['id']

    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        equipment = EquipmentModel(request)

        rs = equipment.get_service_list(equipment_id)
        rows = []
        if rs:
            for r in rs['services']:
                obj = {
                    'id': str(r['_id']),
                    'email': r['email'] if 'email' in r else '-',
                    'telephone': r['telephone'] if 'telephone' in r else '-',
                    'service_status': r['service_status'] if 'service_status' in r else '-',
                    'service_type': r['service_type'] if 'service_type' in r else '-',
                    'company': r['company'] if 'company' in r else '-',
                    'service_date': r['service_date'] if 'service_date' in r else '-',
                    'contact_name': r['contact_name'] if 'contact_name' in r else '-',
                    'return_date': r['return_date'] if 'return_date' in r else '-',
                }

                rows.append(obj)

            #data = sorted(rows, key=lambda k: k['service_date'])

            return {'ok': 1, 'rows': rows}
        else:
            return {'ok': 0, 'msg': 'Record not found'}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='equipment_get_total', renderer='json')
def get_total(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        equipment = EquipmentModel(request)

        try:
            total = equipment.get_total(request.session['hospcode'])

            return {'ok': 1, 'total': total}

        except Exception as e:
            return {'ok': 0, 'msg': e.message}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='equipment_remove', renderer='json')
def remove(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:
        equipment_id = request.params['id']

        equipment = EquipmentModel(request)

        try:
            equipment.remove(ObjectId(equipment_id))

            return {'ok': 1}

        except Exception as e:
            return {'ok': 0, 'msg': e.message}
    else:
        return {'ok': 0, 'msg': 'Token failed'}


@view_config(route_name='equipment_get_list', request_method='POST', renderer='json')
def get_list(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:
            start = request.params['start'] if 'start' in request.params else 0
            stop = request.params['stop'] if 'stop' in request.params else 25

            limit = int(stop) - int(start)

            equipment = EquipmentModel(request)
            rs = equipment.get_list(request.session['hospcode'], int(start), int(limit))

            if rs:
                rows = []
                for r in rs:
                    obj = {
                       'id': str(r['_id']),
                       'name': r['name'],
                       'serial': r['serial'],
                       'durable_goods_number': r['durable_goods_number'] if 'durable_goods_number' in r else '-',
                       'purchase_date': r['purchase_date'] if 'purchase_date' in r else '-',
                       'status': r['status'] if 'status' in r else '0'

                    }

                    rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}

        else:
            return {'ok': 0, 'msg': 'CSRF failed'}


@view_config(route_name='equipment_search', request_method='POST', renderer='json')
def search_equipment(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:
            query = request.params['query']

            equipment = EquipmentModel(request)
            rs = equipment.search(request.session['hospcode'], query)

            if rs:
                rows = []
                for r in rs:
                    obj = {
                        'id': str(r['_id']),
                        'name': r['name'],
                        'serial': r['serial'],
                        'durable_goods_number': r['durable_goods_number'] if 'durable_goods_number' in r else '-',
                        'purchase_date': r['purchase_date'] if 'purchase_date' in r else '-',
                        'status': r['status'] if 'status' in r else '0'

                    }

                    rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}

        else:
            return {'ok': 0, 'msg': 'CSRF failed'}