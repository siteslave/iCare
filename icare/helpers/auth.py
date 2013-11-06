# -*- coding: utf8
class Auth:

    def do_login(self, username, password, request):
        auth = request.db['users'].find_one({
            'username': username,
            'password': password,
            'user_status': '1'
        })

        return auth