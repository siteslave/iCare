# -*- coding: utf8
from datetime import datetime
from pyramid.view import (
    view_config,
)

from pyramid.httpexceptions import (
    HTTPFound,
    HTTPUnauthorized,
)

from icare.models.employers_model import EmployersModel
from icare.helpers.icare_helper import ICHelper
from bson.objectid import ObjectId

h = ICHelper()


@view_config(
    route_name='employers_index',
    renderer='employers.mako')
def index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.session['user_type'] == '1':
            return HTTPFound(location='/admins')

        if request.session['user_type'] == '3':
            return HTTPFound(location='/denied')

            
        positions = h.get_position_list(request)
        grades = h.get_position_grade_list(request)
        
        return {'title': u'ทะเบียนบุคลากร', 'positions': positions, 'grades': grades}
        return {'ok': 1, 'total': total}


@view_config(route_name='employer_get_total', renderer='json')
def get_total(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:

        emp = EmployersModel(request)
        try:
            total = emp.get_total(request.session['owner'])

            return {'ok': 1, 'total': total}

        except Exception as e:
            return {'ok': 0, 'msg': e.message}
    else:
        return {'ok': 0, 'msg': 'Not ajax request'}
        
@view_config(route_name='employer_detail', request_method='POST', renderer='json')
def get_detail(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        #If ajax request
        if request.is_xhr:
            if request.params['id']:
                id = request.params['id']
                emp = EmployersModel(request)
                try:
                    r = emp.detail(ObjectId(id))
                    
                    obj = {
                        'id': str(r['_id']),
                        'cid': r['cid'],
                        'fullname': r['fullname'],
                        'birth': r['birth'] if 'birth' in r else '-',
                        'sex': r['sex'],
                        'position': str(r['position']),
                        'position_id': r['position_id'] if 'position_id' in r else '-',
                        'email': r['email'],
                        'telephone': r['telephone'],
                        'grade': str(r['grade']),
                        'department': r['department'],
                        'start_date': r['start_date'],
                        'end_date': r['end_date'],
                        'position_id': r['position_id'] if 'position_id' in r else '-',
                        'status': r['status'] if 'status' in r else '0'
                        
                    }
                    
                    return {'ok': 1, 'rows': obj}
                except Exception as e:
                    raise e
                
            else:
                return {'ok': 0, 'msg': u'กรุณาระบุ id'}

        
@view_config(route_name='employer_search', request_method='POST', renderer='json')
def search(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:

        if request.is_xhr:  # is ajax request
            query = request.params['query']
            emp = EmployersModel(request)
            try:
                #Search by cid
                q = int(query)
                rs = emp.search_by_cid(request.session['owner'], query)
            except Exception as e:
                #Search by name
                rs = emp.search_by_name(request.session['owner'], query)
            
            #return {'ok': 1, 'rows': rs.count()}
            if rs:
                rows = []
                for r in rs:
                   obj = {
                       'id': str(r['_id']),
                       'cid': r['cid'],
                       'fullname': r['fullname'],
                       'birth': r['birth'] if 'birth' in r else '-',
                       'sex': r['sex'],
                       'position': h.get_position_name(request, r['position']),
                       'grade': h.get_position_grade_name(request, r['grade']),
                       'start_date': r['start_date'],
                       'end_date': r['end_date'],
                       'email': r['email'],
                       'telephone': r['telephone'],
                       'status': r['status'] if 'status' in r else '0'
                       
                   }

                   rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            
        else:
            return {'ok': 0, 'msg': 'Not ajax request'}
                    
@view_config(route_name='employer_get_list', request_method='POST', renderer='json')
def get_list(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:

        if request.is_xhr:  # is ajax request
            start = request.params['start'] if 'start' in request.params else 0
            stop = request.params['stop'] if 'stop' in request.params else 25
            
            limit = int(stop) - int(start)

            emp = EmployersModel(request)
            rs = emp.get_list(request.session['owner'], int(start), int(limit))
            
            #return {'ok': 1, 'rows': rs.count()}
            if rs:
                rows = []
                for r in rs:
                   obj = {
                       'id': str(r['_id']),
                       'cid': r['cid'],
                       'fullname': r['fullname'],
                       'birth': r['birth'] if 'birth' in r else '-',
                       'sex': r['sex'],
                       'position': h.get_position_name(request, r['position']),
                       'grade': h.get_position_grade_name(request, r['grade']),
                       'start_date': r['start_date'],
                       'end_date': r['end_date'],
                       'email': r['email'],
                       'telephone': r['telephone'],
                       'status': r['status'] if 'status' in r else '0'
                       
                   }

                   rows.append(obj)

                return {'ok': 1, 'rows': rows}
            else:
                return {'ok': 0, 'msg': u'ไม่พบข้อมูล'}
            
        else:
            return {'ok': 0, 'msg': 'Not ajax request'}


@view_config(route_name="employer_save_new", request_method="POST", renderer="json")
def save_new(request):
    if "logged" not in request.session:
        return HTTPFound(location="/signin")
    else:
        # Check if ajax request
        if request.is_xhr:
            # Get parameters
            id = request.params["id"] if 'id' in request.params else False
            fullname = request.params["f"]
            cid = request.params["c"]
            birth = request.params["b"]
            sex = request.params["s"]
            position = request.params["p"]
            position_grade = request.params["pg"]
            position_id = request.params["pid"]
            department = request.params["d"]
            email = request.params["e"]
            telephone = request.params["t"]
            start_date = request.params["sd"]
            end_date = request.params["ed"]
            status = request.params["st"]
            # Check data is valid
            chk = fullname and cid and birth and sex and position
            # Data is valid
            if chk:
                # Call employers model
                emp = EmployersModel(request)

                rs = False

                if id:
                    # Update
                    emp.update(ObjectId(id), fullname, birth, sex, ObjectId(position), ObjectId(position_grade), department, email, telephone, start_date, end_date, status, position_id)

                    return {"ok": 1}
                else:
                    # Create
                    # Check if cid exist 
                    is_duplicated = emp.check_duplicated(request.session['owner'], cid)
                    # If cid don't exist
                    if is_duplicated:
                        return {'ok': 0, 'msg': u'เลขบัตรประชาชนซ้ำ'}
                    else:
                        # Save new employer
                        rs = emp.save_new(request.session['owner'], fullname, cid, birth, sex, ObjectId(position), ObjectId(position_grade), department, email, telephone, start_date, end_date, status, position_id)

                        if rs:
                            return {"ok": 1}
                        # Has error
                        else:
                            return {"ok": 0, "msg": u"ไม่สามารถบันทึกรายการได้"}
                
            else:
                return {"ok": 0, "msg": u"ข้อมูลไม่สมบูรณ์ กรุณาตรวจสอบ"}
            
        else:
            return {"ok": 0, "msg": "Not ajax request."}

@view_config(route_name="employer_save_meeting", request_method="POST", renderer="json")
def save_meetings(request):
    if "logged" not in request.session:
        return HTTPFound(location="/signin")
    else:
        # Call employers model
        emp = EmployersModel(request)
        
        cid = request.params['cid']
        start_date = request.params['s']
        end_date = request.params['e']
        title = request.params['t']
        owner_name = request.params['o']
        place_name = request.params['p']
        id = request.params["id"] if 'id' in request.params else False
        
        if id:
            rs = emp.update_meeting(request.session['owner'], cid, id, title, start_date, end_date, owner_name, place_name)
            if rs:
                return {'ok': 1}
            else:
                return {'ok': 0, 'msg': 'ไม่สามารถปรับปรุงรายการได้'}
        else:
            #Check duplicate
            is_duplicate = emp.check_meeting_duplicate(request.session['owner'], cid, title, start_date, end_date, owner_name)
        
            if is_duplicate:
                return {'ok': 0, 'msg': 'ข้อมูลซ้ำ'}
            else:
                #Save
                rs = emp.save_meetings(request.session['owner'], cid, title, start_date, end_date, owner_name, place_name)
            
                if rs:
                    return {'ok': 1}
                else:
                    return {'ok': 0, 'msg': 'ไม่สามารถบันทึกรายการได้'}
                
@view_config(route_name="employer_get_meeting", request_method="POST", renderer="json")
def get_meetings(request):
    if "logged" not in request.session:
        return HTTPFound(location="/signin")
    else:
        # Call employers model
        emp = EmployersModel(request)
        
        cid = request.params['cid']
        
        #Check duplicate
        rs = emp.get_meetings(request.session['owner'], cid)
        
        if rs:
            rows = []
            if 'meetings' in rs:
                for r in rs['meetings']:
                    obj = {
                        'id': str(r['id']),
                        'title': r['title'],
                        'start_date': r['start_date'],
                        'end_date': r['end_date'],
                        'owner_name': r['owner_name'],
                        'place_name': r['place_name']
                    }
                
                    rows.append(obj)
                
                return {'ok': 1, 'rows': rows}
            else: 
                return {'ok': 0, 'msg': 'ไม่พบรายการ'}
        else:
            return {'ok': 0, 'msg': 'ไม่พบรายการ'}    
                
@view_config(route_name="employer_remove_meeting", request_method="POST", renderer="json")
def remove_meetings(request):
    if "logged" not in request.session:
        return HTTPFound(location="/signin")
    else:
        # Call employers model
        emp = EmployersModel(request)
        
        cid = request.params['cid']
        id = request.params['id']
        
        rs = emp.remove_meeting(request.session['owner'], cid, id)
        
        return {'ok': 1} if rs else {'ok': 0, 'msg': 'ไม่สามารถลบรายการได้'}