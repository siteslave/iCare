# -*- coding: utf8
from datetime import datetime
from pyramid.view import (
    view_config,
)
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPUnauthorized,
)

from icare.models.person_model import PersonModel
from icare.helpers.icare_helper import ICHelper

h = ICHelper()

"""
@view_config(route_name='person_remove_latlng', renderer='json')
def person_remove_latlng(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:
        person = PersonModel(request)

        hospcode = request.params['hospcode']
        hid = request.params['hid']

        try:
            person.remove_latlng(hospcode, hid)
            return {'ok': 1}
        except:
            return {'ok': 0, 'msg': u'ไม่สามารถลบรายการได้'}
            
"""