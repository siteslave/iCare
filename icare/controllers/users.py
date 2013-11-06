# -*- coding: utf8

from pyramid.view import view_config


@view_config(route_name='login_user', renderer='login.mako')
def login_view(request):
    #person = request.db['person'].find().limit(50)
    return {'title': 'Signin'}

