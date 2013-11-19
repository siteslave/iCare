# -*- coding: utf8

from pyramid.view import (
    view_config,
)
from pyramid.httpexceptions import (
    HTTPFound,
)

from icare.helpers.icare_helper import ICHelper

h = ICHelper()


@view_config(route_name='labor_other_index', renderer='labor_other.mako')
def labor_other_index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.session['user_type'] == '1':
            return HTTPFound(location='/admins')

        return {'title': u'ตรวจสอบข้อมูลคนในเขตไปคลอดที่หน่วยบริการอื่น'}
