# -*- coding: utf8
from datetime import datetime
from pyramid.view import (
    view_config,
)
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPUnauthorized,
)

from icare.models.home_model import HomeModel
from icare.helpers.icare_helper import ICHelper

h = ICHelper()


@view_config(route_name='home_remove_latlng', renderer='json')
def remove_latlng(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')

    csrf_token = request.params['csrf_token']
    is_token = (csrf_token == unicode(request.session.get_csrf_token()))

    if is_token:
        home = HomeModel(request)

        hospcode = request.params['hospcode']
        hid = request.params['hid']

        try:
            home.remove_latlng(hospcode, hid)
            return {'ok': 1}
        except:
            return {'ok': 0, 'msg': u'ไม่สามารถลบรายการได้'}
            

@view_config(route_name='home_save_latlng', request_method='POST', renderer='json')
def save_latlng(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
    else:
        if request.is_xhr:  # is ajax request
            lat = request.params['lat']
            lng = request.params['lng']
            hid = request.params['hid']
            hospcode = request.params['hospcode']

            home = HomeModel(request)
            #get hid
            #hid = anc.get_hid_from_pid(hospcode, pid)
            home.save_latlng(hid, hospcode, float(lat), float(lng))

            return {'ok': 1}
        else:
            return {'ok': 0, 'msg': 'Not ajax request.'}