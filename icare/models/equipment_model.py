# -*- coding: utf8

import pymongo
import re
from bson.objectid import ObjectId


class EquipmentModel:
    def __init__(self, request):
        self.request = request

    def save_new(self, hospcode, name, serial, durableGoods, purchaseDate, status):
        """
        Save new equipment
        """
        rs = self.request.db['equipments'].insert({
            "hospcode": hospcode,
            "name": name,
            "serial": serial,
            "durable_goods_number": durableGoods,
            "purchase_date": purchaseDate,
            "status": status,
        })

        return rs

    def get_list(self, hospcode, start, limit):
        """
         Get person list
        """
        self.request.db['equipments'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['equipments'].find({
            'hospcode': hospcode
        }).skip(start).limit(limit)

        return rs

    def search(self, hospcode, query):
        """
         search person list
        """
        self.request.db['equipments'].ensure_index('hospcode', pymongo.ASCENDING)

        regex = re.compile("^" + re.escape(query), re.IGNORECASE)

        rs = self.request.db['equipments'].find({
            'hospcode': hospcode,
            'name': regex
        })

        return rs

    def get_total(self, hospcode):
        """
        Get total record
        """
        self.request.db['equipments'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['equipments'].find({
            'hospcode': hospcode
        }).count()

        return rs

    def update(self, id, name, serial, durableGoods, purchaseDate, status):
        """
        Update equipment
        """
        self.request.db['equipments'].update({"_id": id}, {'$set': {
            "name": name,
            "serial": serial,
            "durable_goods_number": durableGoods,
            "purchase_date": purchaseDate,
            "status": status,
        }})

    def remove(self, id):
        """
        Remove equipment

        @param id:
        @return: void
        """

        self.request.db['equipments'].remove({'_id': id})

        return True

    def check_exist(self, equipment_id):
        try:
            rs = self.request.db['equipments']\
                .find({'_id': ObjectId(equipment_id)})\
                .count()
            # Return boolean
            return True if rs > 0 else False
        except:
            return False

    def get_service_list(self, equipment_id):
        """
        Get Service list
        """

        rs = self.request.db['equipments'].\
            find_one({'_id': ObjectId(equipment_id)}, {"services": 1})

        return rs

    def get_detail(self, equipment_id):

        rs = self.request.db['equipments'].find_one({'_id': ObjectId(equipment_id)}, {
            "name": 1, "durable_goods_number": 1, "serial": 1
        })

        return rs

    def get_service_detail(self, equipment_id, service_id):

        self.request.db['equipments'].ensure_index('services._id', pymongo.ASCENDING)

        rs = self.request.db['equipments'].find_one({
            '_id': ObjectId(equipment_id),
            'services': {
                '$elemMatch': {
                    '_id': ObjectId(service_id)
                }
            }
        })

        return rs

    def remove_service(self, equipment_id, service_id):

        self.request.db['equipments'].ensure_index('services._id', pymongo.ASCENDING)

        self.request.db['equipments'].update({'_id': ObjectId(equipment_id)},
                                             {'$pull': {
                                                 'services': {
                                                     '_id': ObjectId(service_id)
                                                 }
                                             }})

        return True

    def save_service(self, equipment_id, service_date, service_type, company,
                 contact_name, telephone, email, service_status, return_date):
        """
        Save new service
        """

        self.request.db['equipments'].update(
            {
                '_id': equipment_id
            },
            {
                '$push': {
                    'services': {
                        '_id': ObjectId(),
                        'service_date': service_date,
                        'service_type': service_type,
                        'company': company,
                        'contact_name': contact_name,
                        'telephone': telephone,
                        'email': email,
                        'service_status': service_status,
                        'return_date': return_date
                    }
                }
            })

        return True

    def update_service(self, equipment_id, service_id, service_date, service_type, company,
                 contact_name, telephone, email, service_status, return_date):
        """
        Save new service
        """
        self.request.db['equipments'].ensure_index('services._id', pymongo.ASCENDING)

        self.request.db['equipments'].update(
            {
                '_id': equipment_id,
                'services._id': service_id
            },
            {
                '$set': {
                    'services.$.service_date': service_date,
                    'services.$.service_type': service_type,
                    'services.$.company': company,
                    'services.$.contact_name': contact_name,
                    'services.$.telephone': telephone,
                    'services.$.email': email,
                    'services.$.service_status': service_status,
                    'services.$.return_date': return_date
                }
            })

        return True