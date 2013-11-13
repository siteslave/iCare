from pyramid.config import Configurator
from urlparse import urlparse
from gridfs import GridFS

import pymongo

from pyramid.session import UnencryptedCookieSessionFactoryConfig

session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(
        settings=settings,
        session_factory=session_factory
    )
    config.add_static_view('static', 'static', cache_max_age=3600)
    
    db_url = urlparse(settings['mongo_uri'])
    config.registry.db = pymongo.Connection(
        host=db_url.hostname,
        port=db_url.port,
    )

    def add_db(request):
        db = config.registry.db[db_url.path[1:]]
        if db_url.username and db_url.password:
            db.authenticate(db_url.username, db_url.password)

        return db

    def add_fs(request):
        return GridFS(request.db)

    #users route
    def users_route(config):
        config.add_route('login_user', '/login')
        config.add_route('logout_user', '/logout')

    def anc_route(config):
        config.add_route('anc_get_list', '/get_list')
        config.add_route('anc_get_list_total', '/get_total')
        config.add_route('anc_get_visit_total', '/get_visit_total')
        config.add_route('anc_get_visit', '/get_visit')
        config.add_route('anc_save_survey', '/save_survey')
        config.add_route('anc_do_process', '/do_process')

        config.add_route('anc_get_labor', '/get_labor')
        config.add_route('anc_get_prenatal', '/get_prenatal')
        config.add_route('anc_get_survey', '/get_survey')

        config.add_route('anc_search', '/search')
        config.add_route('anc_all_latlng', '/get_all_latlng')

        config.add_route('anc_get_list_map', '/get_list_map')
        config.add_route('anc_get_list_map_total', '/get_list_map_total')

    def mch_route(config):
        config.add_route('mch_get_list', '/get_list')
        config.add_route('mch_search', '/search')
        config.add_route('mch_get_list_total', '/get_total')
        config.add_route('mch_get_postnatal', '/get_postnatal')
        config.add_route('mch_get_postnatal_all', '/get_postnatal_all')
        config.add_route('mch_get_appointment', '/get_appointment')
        config.add_route('mch_map', '/mch_map')

    def babies_route(config):
        config.add_route('babies_search', '/search')
        config.add_route('babies_get_list', '/get_list')
        config.add_route('babies_get_total', '/get_total')
        config.add_route('babies_get_care', '/get_care')
        config.add_route('babies_get_care_all', '/get_care_all')
        config.add_route('babies_get_newborn', '/get_newborn')

    def wbc02_route(config):
        config.add_route('wbc02_get_list', '/get_list')
        config.add_route('wbc02_get_total', '/get_total')
        config.add_route('wbc02_get_total_by_vid', '/get_total_by_vid')
        config.add_route('wbc02_get_list_by_vid', '/get_list_by_vid')
        config.add_route('wbc02_get_vaccines', '/get_vaccines')
        config.add_route('wbc02_search_visit', '/search_visit')
        config.add_route('wbc02_get_nutrition', '/get_nutrition')
        config.add_route('wbc02_get_nutrition_owner', '/get_nutrition_owner')

    def wbc35_route(config):
        config.add_route('wbc35_get_list', '/get_list')
        config.add_route('wbc35_get_total', '/get_total')
        config.add_route('wbc35_get_total_by_vid', '/get_total_by_vid')
        config.add_route('wbc35_get_list_by_vid', '/get_list_by_vid')
        config.add_route('wbc35_get_vaccines', '/get_vaccines')
        config.add_route('wbc35_search_visit', '/search_visit')
        config.add_route('wbc35_get_nutrition', '/get_nutrition')
        config.add_route('wbc35_get_nutrition_owner', '/get_nutrition_owner')

    def wbc612_route(config):
        config.add_route('wbc612_get_list', '/get_list')
        config.add_route('wbc612_get_total', '/get_total')
        config.add_route('wbc612_get_total_by_vid', '/get_total_by_vid')
        config.add_route('wbc612_get_list_by_vid', '/get_list_by_vid')
        config.add_route('wbc612_get_vaccines', '/get_vaccines')
        config.add_route('wbc612_search_visit', '/search_visit')
        config.add_route('wbc612_get_nutrition', '/get_nutrition')
        config.add_route('wbc612_get_nutrition_owner', '/get_nutrition_owner')

    def ncdscreen_route(config):
        config.add_route('ncdscreen_get_list', '/get_list')
        config.add_route('ncdscreen_get_total', '/get_total')

        config.add_route('ncdscreen_get_list_by_vid', '/get_list_by_vid')
        config.add_route('ncdscreen_get_total_by_vid', '/get_total_by_vid')

        config.add_route('ncdscreen_get_screen', '/get_screen')
        config.add_route('ncdscreen_get_history', '/get_history')
        config.add_route('ncdscreen_get_history_total', '/get_history_total')

    def epidem_route(config):
        config.add_route('epidem_get_list', '/get_list')
        config.add_route('epidem_get_total', '/get_total')
        config.add_route('epidem_get_info', '/get_info')

    def home_route(config):
        config.add_route('home_remove_latlng', '/remove_latlng')
        config.add_route('home_save_latlng', '/save_latlng')
        
    def employers_route(config):
        config.add_route('employer_get_list', '/get_list')
        config.add_route('employer_get_total', '/get_total')
        config.add_route('employer_save_new', '/save_new')
        config.add_route('employer_detail', '/detail')
        config.add_route('employer_search', '/search')
        config.add_route('employer_save_meeting', '/save_meeting')
        config.add_route('employer_get_meeting', '/get_meetings')
        config.add_route('employer_remove_meeting', '/remove_meeting')
        
    def reports_route(config):
        config.add_route('reports_get_babies_total', '/get_babies_total')
        config.add_route('report_get_anc_risk_list', '/risk/list')
        config.add_route('report_get_anc_risk_total', '/risk/total')
        config.add_route('report_get_anc_risk_search', '/risk/search')
        config.add_route('report_get_anc_risk_detail', '/risk/detail')
        config.add_route('report_get_anc_history', '/risk/anc_history')
        config.add_route('reports_anc_risk', '/anc_risk')
        config.add_route('report_anc', '/anc')
        config.add_route('report_anc_get_list', '/anc/list')
        config.add_route('report_anc_get_total', '/anc/total')
        config.add_route('report_anc_get_forecast_filter', '/anc/forecast_filter')
        config.add_route('report_anc_search', '/anc/search')

        config.add_route('reports_mch_index', '/mch')
        config.add_route('reports_mch_do_process', '/mch/process')
        config.add_route('report_mch_total', '/mch/total')
        config.add_route('report_mch_list', '/mch/list')
        config.add_route('report_mch_target_per_month', '/mch/get_forecast_dashboard')
        config.add_route('report_anc_target_per_month', '/anc/get_forecast_dashboard')

    def admin_route(config):
        config.add_route('admin_users', '/users')
        config.add_route('admin_save', '/users/save')
        config.add_route('users_get_total', '/users/total')
        config.add_route('users_get_list', '/users/list')
        config.add_route('users_remove', '/users/remove')
        config.add_route('users_changepass', '/users/changepass')
        config.add_route('app_change_password', '/changepass')

    config.add_request_method(add_db, 'db', reify=True)
    config.add_request_method(add_fs, 'fs', reify=True)

    config.include(epidem_route, route_prefix='/epidem')

    config.include(home_route, route_prefix='/home')
    config.include(admin_route, route_prefix='/admins')

    config.include(users_route, route_prefix='/users')
    config.include(anc_route, route_prefix='/anc')
    config.include(mch_route, route_prefix='/mch')
    config.include(babies_route, route_prefix='/babies')
    config.include(wbc02_route, route_prefix='/wbc02')
    config.include(wbc35_route, route_prefix='/wbc35')
    config.include(wbc612_route, route_prefix='/wbc612')
    config.include(ncdscreen_route, route_prefix='/ncdscreen')
    config.include(employers_route, route_prefix='/employers')
    config.include(reports_route, route_prefix='/reports')
    
    config.add_route('employers_index', '/employers')

    config.add_route('home', '/')
    config.add_route('uploads', '/uploads')
    config.add_route('anc_index', '/anc')
    config.add_route('mch_index', '/mch')
    config.add_route('babies_index', '/babies')

    config.add_route('wbc02_index', '/wbc02')
    config.add_route('wbc35_index', '/wbc35')
    config.add_route('wbc612_index', '/wbc612')

    config.add_route('ncdscreen_index', '/ncdscreen')
    config.add_route('epidem_index', '/epidem')

    config.add_route('signin', '/signin')
    config.add_route('signout', '/singout')

    config.add_route('reports_index', '/reports')
    config.add_route('admin_index', '/admins')

    config.include('pyramid_mako')
    
    config.scan()

    return config.make_wsgi_app()
