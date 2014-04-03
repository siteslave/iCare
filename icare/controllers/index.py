# -*- coding: utf8

from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPUnauthorized
)

from icare.helpers.auth import Auth
from icare.models.anc_model import AncModel
from icare.models.babies_model import BabiesModel
from icare.models.mch_model import MchModel


@view_config(route_name='home', renderer='page.mako')
def index_view(request):
    if 'logged' not in request.session:
        return HTTPFound(location='/signin')
        
    if request.session['user_type'] == '1':
        return HTTPFound(location='/admins/users')

    #return HTTPFound(location="/anc")
    return {'title': u'Dashboard'}


@view_config(route_name='signin', renderer='signin.mako')
def signin_view(request):
    return {'title': u'กรุณาล๊อกอิน'}


@view_config(route_name='signin', request_method='POST')
def do_login(request):

    from icare.helpers.icare_helper import ICHelper

    h = ICHelper()

    csrf_token = request.params['csrf_token']
    username = request.params['username']
    password = h.get_hash(request.params['password'])
    isProcess = request.params['isProcess']

    auth = Auth()

    is_token = (csrf_token == unicode(request.session.get_csrf_token()))
    if is_token:
        #do login
        users = auth.do_login(username, password, request)
        if users:
            session = request.session
            session['logged'] = True
            session['hospcode'] = users['hospcode']
            session['owner'] = users['owner']
            session['fullname'] = users['fullname']
            session['user_type'] = users['user_type']
            session['id'] = str(users['_id'])

            if isProcess:
                #process data
                anc = AncModel(request)
                mch = MchModel(request)
                babies = BabiesModel(request)

                anc.do_process_list(users['hospcode'])
                anc.do_process_12weeks(users['hospcode'])
    
                mch.do_process_forecast(users['hospcode'])
                babies.process_milk(users['hospcode'])

            if users['user_type'] == '1':
                return HTTPFound(location='/admins/users')
            else:
                return HTTPFound(location='/')
        else:
            return HTTPFound(location='/signin')
    else:
        raise HTTPUnauthorized


@view_config(route_name='signout', request_method='GET')
def do_logout(request):
    try:
        del request.session['logged']
        return HTTPFound(location='/signin')

    except:
        return HTTPFound(location='/signin')