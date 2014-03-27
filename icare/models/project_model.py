# -*- coding: utf8

import pymongo
import re
from bson.objectid import ObjectId


class ProjectModel:
    def __init__(self, request):
        self.request = request

    def save_report(self, project_id, classify, report_date, resolve_date, desc):
        
        try:
            self.request.db['projects'].update({'_id': project_id}, {
                '$set': {
                    'reports': {
                        'classify': classify,
                        'report_date': report_date,
                        'resolve_date': resolve_date,
                        'desc': desc
                    }
                }
            })
            
            return True
        except Exception as e:
            return False
            
    def get_report(self, project_id):
        rs = self.request.db['projects'].find_one({'_id': project_id}, {'reports': 1})
        return rs

    def update_report(self, project_id, report_id, classify, report_date, resolve_date, desc):
        #Create index
        self.request.db['projects'].ensure_index('reports.id', pymongo.ASCENDING)
       
        try:
           self.request.db['projects'].update({
               '_id': project_id,
               'reports': {
                   '$elemMatch': {
                       'id': ObjectId(str(project_id))
                   }
               }
           }, {
               '$set': {
                    'reports.$.classify': classify,
                    'reports.$.report_date': report_date,
                    'reports.$.resolve_date': resolve_date,
                    'reports.$.desc': desc
               }
           })

           return True

        except Exception as e:
            return False

    def save_new(self, hospcode, name, classify, start_date, end_date,
                 indicator, budgets_source, budgets_amount, project_manager, plan):
        """
        Save new equipment
        """
        rs = self.request.db['projects'].insert({
            "hospcode": hospcode,
            "name": name,
            "classify": classify,
            "start_date": start_date,
            "end_date": end_date,
            "indicator": indicator,
            "budgets_source": budgets_source,
            "budgets_amount": budgets_amount,
            "project_manager": project_manager,
            "plan": plan
        })

        return rs

    def get_list(self, hospcode, start, limit):
        """
         Get person list
        """
        self.request.db['projects'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['projects'].find({
            'hospcode': hospcode
        }).skip(start).limit(limit)

        return rs

    def search(self, hospcode, query):
        """
         search person list
        """
        self.request.db['projects'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['projects'].ensure_index('name', pymongo.ASCENDING)


        regex = re.compile("^" + re.escape(query), re.IGNORECASE)

        rs = self.request.db['projects'].find({
            'hospcode': hospcode,
            'name': regex
        })

        return rs

    def get_total(self, hospcode):
        """
        Get total record
        """
        self.request.db['projects'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['projects'].find({
            'hospcode': hospcode
        }).count()

        return rs

    def update(self, project_id, name, classify, start_date, end_date,
               indicator, budgets_source, budgets_amount, project_manager, plan):
        """
        Update equipment
        """
        self.request.db['projects'].update({"_id": project_id}, {'$set': {
            "name": name,
            "classify": classify,
            "start_date": start_date,
            "end_date": end_date,
            "indicator": indicator,
            "budgets_source": budgets_source,
            "budgets_amount": budgets_amount,
            "project_manager": project_manager,
            "plan": plan
        }})

    def remove(self, project_id):
        """
        Remove equipment

        @param project_id:
        @return: void
        """

        self.request.db['projects'].remove({'_id': project_id})

        return True

    def check_exist(self, project_id):
        try:
            rs = self.request.db['projects']\
                .find({'_id': ObjectId(project_id)})\
                .count()
            # Return boolean
            return True if rs > 0 else False
        except:
            return False

    def get_detail(self, project_id):

        rs = self.request.db['projects'].find_one({'_id': ObjectId(project_id)})

        return rs

