# -*- coding: utf8
from bson import ObjectId
import pymongo
import re


class UsersAdminModel:

    def __init__(self, request):
        self.request = request

    def get_list(self, owner, start, limit):

        self.request.db['users'].ensure_index('owner', pymongo.ASCENDING)

        rs = self.request.db['users'].find({'owner': owner}).skip(start).limit(limit)

        return rs

    def get_total(self, owner):

        self.request.db['users'].ensure_index('owner', pymongo.ASCENDING)

        rs = self.request.db['users'].find({'owner': owner}).count()
        return rs

    def save(self, hospcode, username, password, cid, fullname, position, owner, is_active):
        self.request.db['users'].insert({
            'hospcode': hospcode,
            'username': username,
            'password': password,
            'cid': cid,
            'fullname': fullname,
            'position': position,
            'owner': owner,
            'user_type': '3',
            'is_active': is_active
        })

    def update(self, user_id, hospcode, cid, fullname, position, is_active):
        self.request.db['users'].update({
            '_id': ObjectId(user_id)
        }, {
            '$set': {
                'hospcode': hospcode,
                'cid': cid,
                'fullname': fullname,
                'position': position,
                'is_active': is_active
            }
        })

    def remove(self, user_id):
        self.request.db['users'].remove({'_id': ObjectId(user_id)})

    def change_password(self, user_id, newpass):

        self.request.db['users'].update({
            '_id': ObjectId(user_id)
        }, {
            '$set': {
                'password': newpass
            }
        })

    def search(self, query, owner):
        self.request.db['users'].ensure_index('fullname', pymongo.ASCENDING)
        self.request.db['users'].ensure_index('username', pymongo.ASCENDING)

        rs = self.request.db['users'].find({
            '$or': [
                {
                    'fullname': {
                        '$regex': '^' + re.escape(query)
                    }
                },
                {
                    'username': {
                        '$regex': '^' + re.escape(query)
                    }
                }
            ],
            'owner': owner
        })

        return rs