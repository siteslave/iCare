# -*- coding: utf8
import pymongo


class AdminModel:
    def __init__(self, request):
        self.request = request

    def save(self, data):

        rs = self.request.db['users'].insert({
            'fullname': data['fullname'],
            'cid': data['cid'],
            'hospcode': data['hospcode'],
            'username': data['username'],
            'password': data['password'],
            'user_type': data['user_type'],
            'user_status': data['user_status'],
            'position': data['position']
        })

        return True if rs else False

    def update(self, data):
        self.request.db['users'].ensure_index('username', pymongo.ASCENDING)

        self.request.db['users'].update({'_id': data['id']}, {'$set': {
            'fullname': data['fullname'],
            'cid': data['cid'],
            'hospcode': data['hospcode'],
            #'username': data['username'],
            #'password': data['password'],
            'user_type': data['user_type'],
            'user_status': data['user_status'],
            'position': data['position']
        }})

    def check_duplicate(self, username):
        self.request.db['users'].ensure_index('username', pymongo.ASCENDING)

        rs = self.request.db['users'].find({'username': username}).count()

        return True if rs > 0 else False

    def get_user_list(self, start, limit):

        rs = self.request.db['users'].find().skip(start).limit(limit)

        return rs

    def get_user_total(self):

        rs = self.request.db['users'].find().count()

        return rs

    def remove_user(self, id):
        self.request.db['users'].remove({'_id': id})
        return True

    def change_password(self, id, password):
        self.request.db['users'].update({'_id': id}, {'$set': {
            'password': password
        }})

        return True