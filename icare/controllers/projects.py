# -*- coding: utf8
from bson import ObjectId
from pyramid.view import (
    view_config,
)
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound)

from icare.helpers.icare_helper import ICHelper

#Load helper
from icare.models.project_model import ProjectModel

h = ICHelper()


@view_config(route_name='project_index', renderer='project.mako')
def index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.session['user_type'] == '1':
            return HTTPFound(location='/admins')

        if request.session['user_type'] == '3':
            return HTTPFound(location='/denied')

        return {'title': u'ข้อมูลโครงการ'}


@view_config(route_name="project_save_report", request_method='POST', renderer='json')
def save_report(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            # Get parameters
            project_id = request.params["projectId"] if 'projectId' in request.params else False
            classify = request.params["classify"]
            report_date = request.params["reportDate"]
            resolve_date = request.params["resolveDate"]
            desc = request.params["desc"]

            # Data is valid
            if report_date:
                project = ProjectModel(request)

                rs = project.save_report(ObjectId(project_id), classify, report_date, resolve_date, desc)
                if rs:
                    return {"ok": 1, "msg": "save"}
                # Has error
                else:
                    return {"ok": 0, "msg": u"ไม่สามารถบันทึกรายการได้"}
                    

            else:
                return {"ok": 0, "msg": u"ข้อมูลไม่สมบูรณ์ กรุณาตรวจสอบ"}

        else:
            return {"ok": 0, "msg": "CSRF failed."}


@view_config(route_name="save_project", request_method='POST', renderer='json')
def save_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            # Get parameters
            project_id = request.params["project_id"] if 'project_id' in request.params else False
            name = request.params['name']
            classify = request.params["classify"]
            start_date = h.jsdate_to_string(request.params["start_date"])
            end_date = h.jsdate_to_string(request.params["end_date"])
            indicator = request.params["indicator"]
            budgets_source = request.params["budgets_source"]
            budgets_amount = request.params["budgets_amount"]
            project_manager = request.params['project_manager']
            plan = request.params['plan']

            # Data is valid
            if name:
                project = ProjectModel(request)

                if project_id:
                    # update
                    project.update(ObjectId(project_id), name, classify, start_date, end_date,
                                   indicator, budgets_source, budgets_amount, project_manager, plan)
                    return {"ok": 1, "msg": "update"}
                else:
                    rs = project.save_new(request.session['hospcode'], name, classify, start_date,
                                          end_date, indicator, budgets_source, budgets_amount, project_manager, plan)
                    if rs:
                        return {"ok": 1, "msg": "save"}
                    # Has error
                    else:
                        return {"ok": 0, "msg": u"ไม่สามารถบันทึกรายการได้"}

            else:
                return {"ok": 0, "msg": u"ข้อมูลไม่สมบูรณ์ กรุณาตรวจสอบ"}

        else:
            return {"ok": 0, "msg": "CSRF failed."}


@view_config(route_name='project_get_total', renderer='json')
def get_total(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        project = ProjectModel(request)

        try:
            total = project.get_total(request.session['hospcode'])

            return {'ok': 1, 'total': total}

        except Exception as e:
            return {'ok': 0, 'msg': e.message}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name='project_get_list', request_method='POST', renderer='json')
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

            project = ProjectModel(request)
            rs = project.get_list(request.session['hospcode'], int(start), int(limit))

            if rs:
                rows = []
                for r in rs:
                    
                    obj = {
                       'id': str(r['_id']),
                       'name': r['name'],
                       'start_date': h.to_thai_date(r['start_date']) if 'start_date' in r else '-',
                       'end_date': h.to_thai_date(r['end_date']) if 'end_date' in r else '-',
                       'indicator': r['indicator'] if 'indicator' in r else '-',
                       'budgets_source': r['budgets_source'] if 'budgets_source' in r else '-',
                       'budgets_amount': r['budgets_amount'] if 'budgets_amount' in r else '-',
                       'classify': r['classify'] if 'classify' in r else '-',
                       'project_manager': r['project_manager'] if 'project_manager' in r else '-'
                    }

                    rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}

        else:
            return {'ok': 0, 'msg': 'CSRF failed'}


@view_config(route_name='project_search', request_method='POST', renderer='json')
def search(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:

        csrf_token = request.params['csrf_token']
        is_token = (csrf_token == unicode(request.session.get_csrf_token()))

        if is_token:

            query = request.params['query']

            project = ProjectModel(request)
            rs = project.search(request.session['hospcode'], query)

            if rs:
                rows = []
                for r in rs:
                    
                    obj = {
                       'id': str(r['_id']),
                       'name': r['name'],
                       'start_date': h.to_thai_date(r['start_date']) if 'start_date' in r else '-',
                       'end_date': h.to_thai_date(r['end_date']) if 'end_date' in r else '-',
                       'indicator': r['indicator'] if 'indicator' in r else '-',
                       'budgets_source': r['budgets_source'] if 'budgets_source' in r else '-',
                       'budgets_amount': r['budgets_amount'] if 'budgets_amount' in r else '-',
                       'classify': r['classify'] if 'classify' in r else '-',
                       'project_manager': r['project_manager'] if 'project_manager' in r else '-'
                    }

                    rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}

        else:
            return {'ok': 0, 'msg': 'CSRF failed'}


@view_config(route_name='project_get_detail', request_method='POST', renderer='json')
def get_detail(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    project_id = request.params['project_id']

    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:
        project = ProjectModel(request)

        rs = project.get_detail(project_id)

        obj = {
            "id": str(rs["_id"]),
            "name": rs["name"] if 'name' in rs else '-',
            "indicator": rs["indicator"] if 'indicator' in rs else '-',
            "budgets_source": rs["budgets_source"] if 'budgets_source' in rs else '-',
            "end_date": h.to_eng_date(rs["end_date"]) if 'end_date' in rs else '-',
            "budgets_amount": rs["budgets_amount"] if 'budgets_amount' in rs else '-',
            "start_date": h.to_eng_date(rs["start_date"]) if 'start_date' in rs else '-',
            "classify": rs["classify"] if 'classify' in rs else '-',
            "project_manager": rs["project_manager"] if 'project_manager' in rs else '-',
            "plan": rs["plan"] if 'plan' in rs else '-'
        }

        if rs:
            return {'ok': 1, 'rows': obj}
        else:
            return {'ok': 0, 'msg': 'Record not found'}


@view_config(route_name='project_get_report', request_method='POST', renderer='json')
def get_report(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    project_id = request.params['project_id']

    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:
        project = ProjectModel(request)

        rs = project.get_report(ObjectId(project_id))

        if 'reports' in rs:
            obj = {
                "report_date": rs["reports"]["report_date"] if 'report_date' in rs["reports"] else '-',
                "resolve_date": rs["reports"]["resolve_date"] if 'resolve_date' in rs["reports"] else '-',
                "classify": rs["reports"]["classify"] if 'classify' in rs["reports"] else '-',
                "desc": rs["reports"]["desc"] if 'desc' in rs["reports"] else '-'
            }

            return {'ok': 1, 'rows': obj}
                
        else:
            return {'ok': 0, 'msg': 'Record not found'}


@view_config(route_name='project_remove', renderer='json')
def remove(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:
        project_id = request.params['project_id']

        project = ProjectModel(request)

        try:
            project.remove(ObjectId(project_id))

            return {'ok': 1}

        except Exception as e:
            return {'ok': 0, 'msg': e.message}
    else:
        return {'ok': 0, 'msg': 'Token failed'}