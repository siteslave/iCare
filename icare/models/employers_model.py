# -*- coding: utf8

import pymongo
from bson.objectid import ObjectId

class EmployersModel:
    def __init__(self, request):
        self.request = request

    def get_list(self, hospcode, start, limit):
        """
         Get person list
        """
        self.request.db['employers'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['employers'].find({
            'hospcode': hospcode
        }).skip(start).limit(limit)

        return rs

    def get_total(self, hospcode):
        """
        Get total record
        """
        self.request.db['employers'].ensure_index('hospcode', pymongo.ASCENDING)

        rs = self.request.db['employers'].find({
            'hospcode': hospcode
        }).count()

        return rs
        
    # Search employer by cid
    def search_by_cid(self, hospcode, cid):
        """
         Get employers list
        """
        self.request.db['employers'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['employers'].ensure_index('cid', pymongo.ASCENDING)

        rs = self.request.db['employers'].find({
            'hospcode': hospcode,
            'cid': cid,
        })

        return rs
      
      # Update employer  
    def update(self, id, fullname, birth, sex, position, position_grade, department, email, telephone, start_date, end_date, status, position_id):
        """
        Save new employer
        """
        self.request.db['employers'].update({ "_id": id }, {'$set': {
          "fullname": fullname,
          #"cid": cid,
          "sex": sex,
          "birth": birth,
          "position": ObjectId(str(position)),
          "grade": ObjectId(str(position_grade)),
          "department": department,
          "email": email,
          "telephone": telephone,
          "start_date": start_date, 
          "end_date": end_date, 
          "status": status,
          "position_id": position_id
        }})
          
    # Save new employer  
    def save_new(self, hospcode, fullname, cid, birth, sex, position, position_grade, department, email, telephone, start_date, end_date, status, position_id):
        """
        Save new employer
        """
        rs = self.request.db['employers'].insert({
            "hospcode": hospcode,
            "fullname": fullname,
            "cid": cid,
            "sex": sex,
            "birth": birth,
            "position": ObjectId(str(position)),
            "grade": ObjectId(str(position_grade)),
            "department": department,
            "email": email,
            "telephone": telephone,
            "start_date": start_date, 
            "end_date": end_date, 
            "status": status,
            "position_id": position_id
        })
        
        return rs
        
    # Check cid duplicated
    def check_duplicated(self, hospcode, cid):
        # Create index
        self.request.db['employers'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['employers'].ensure_index('icd', pymongo.ASCENDING)
        # Check duplicate
        rs = self.request.db['employers'].find({'hospcode': hospcode, 'cid': cid}).count()
        # Return boolean
        return True if rs > 0 else False
        
    # Get employer detail
    def detail(self, id):
        #Create index
        self.request.db['employers'].ensure_index('_id', pymongo.ASCENDING)
        #Get detail
        rs = self.request.db['employers'].find_one({'_id': id})
        
        return rs
        
    def search_by_name(self, hospcode, name):
        #db.houses.find({"hid":{"$regex": u"9"}})
        #Create index
        self.request.db['employers'].ensure_index('fullname', pymongo.ASCENDING)
        self.request.db['employers'].ensure_index('hospcode', pymongo.ASCENDING)
        
        rs = self.request.db['employers'].find({'hospcode': hospcode, 'fullname': {'$regex': name}})
        
        return rs
        
    def search_by_cid(self, hospcode, cid):
        #Create index
        self.request.db['employers'].ensure_index('cid', pymongo.ASCENDING)
        self.request.db['employers'].ensure_index('hospcode', pymongo.ASCENDING)
        
        #Get detail
        rs = self.request.db['employers'].find({'hospcode': hospcode, 'cid': cid})
        
        return rs
        
    def get_meetings(self, hospcode, cid):
        #Create index
        self.request.db['employers'].ensure_index('cid', pymongo.ASCENDING)
        self.request.db['employers'].ensure_index('hospcode', pymongo.ASCENDING)
        
        #Get list
        rs = self.request.db['employers'].find_one({'hospcode': hospcode, 'cid': cid}, {'meetings': 1})
        
        return rs
        
    def save_meetings(self, hospcode, cid, title, start_date, end_date, owner_name, place_name):
        #Create index
        self.request.db['employers'].ensure_index('cid', pymongo.ASCENDING)
        self.request.db['employers'].ensure_index('hospcode', pymongo.ASCENDING)
        
        try:
            rs = self.request.db['employers'].update({'hospcode': hospcode, 'cid': cid}, {
                '$push': {
                    'meetings': {
                        'id': ObjectId(),
                        'title': title,
                        'start_date': start_date,
                        'end_date': end_date,
                        'owner_name': owner_name,
                        'place_name': place_name
                    }
                }
            })
            
            return True
        except Exception as e:
            return False
        
    def remove_meeting(self, hospcode, cid, id):
        #Create index
        self.request.db['employers'].ensure_index('hospcode', pymongo.ASCENDING)
        self.request.db['employers'].ensure_index('cid', pymongo.ASCENDING)
        self.request.db['employers'].ensure_index('meetings.id', pymongo.ASCENDING)
        
        try:
            self.request.db['employers'].update({
                'hospcode': hospcode,
                'cid': cid
            }, {
                '$pull': {
                    'meetings':  {
                        'id': ObjectId(str(id))
                    }
                }
            })
            
            return True
            
        except Exception as e:
            return False
        
    def check_meeting_duplicate(self, hospcode, cid, title, start_date, end_date, owner_name):
        #Create index
        self.request.db['employers'].ensure_index('cid', pymongo.ASCENDING)
        self.request.db['employers'].ensure_index('hospcode', pymongo.ASCENDING)
        #Create array index
        self.request.db['employers'].ensure_index('meetings.title', pymongo.ASCENDING)
        self.request.db['employers'].ensure_index('meetings.start_date', pymongo.ASCENDING)
        self.request.db['employers'].ensure_index('meetings.end_date', pymongo.ASCENDING)
        self.request.db['employers'].ensure_index('meetings.owner_name', pymongo.ASCENDING)
        
        rs = self.request.db['employers'].find({
            'hospcode': hospcode,
            'cid': cid,
            'meetings': {
                '$elemMatch': {
                    'title': title,
                    'start_date': start_date,
                    'end_date': end_date,
                    'owner_name': owner_name
                }
            }
        }).count()
        
        return True if rs > 0 else False
 
    def update_meeting(self, hospcode, cid, id, title, start_date, end_date, owner_name, place_name):
       #Create index
       self.request.db['employers'].ensure_index('cid', pymongo.ASCENDING)
       self.request.db['employers'].ensure_index('hospcode', pymongo.ASCENDING)
       #Create array index
       self.request.db['employers'].ensure_index('meetings.id', pymongo.ASCENDING)
       
       try:
           rs = self.request.db['employers'].update({
               'hospcode': hospcode,
               'cid': cid,
               'meetings': {
                   '$elemMatch': {
                       'id': ObjectId(str(id))
                   }
               }
           }, {
               '$set': {
                   'meetings.$.title': title,
                   'meetings.$.start_date': start_date,
                   'meetings.$.end_date': end_date,
                   'meetings.$.owner_name': owner_name,
                   'meetings.$.place_name': place_name
               }
           })
           
           return True
       except Exception as e:
           return False