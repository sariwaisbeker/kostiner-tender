# from config import db
# #קבלת המידע מהפו של יהודית
# user_collection = db['users']

class userDAL:
    def get(self):
        # return user_collection.find()
        pass
    def get_by_id(self, user_id):
        # return user_collection.find_one({'id': user_id})
        pass

    def insert(self, data):
        # result = user_collection.insert_one(data)
        # return result
        pass


    def update(self, id, data):
        data['user_id'] = id
        # result = user_collection.update_one({'user_id':id},{'$set':data})
        # return result
        pass


    def delete(self, id):
        # result = user_collection.delete_one({'user_id': id})
        # return result
        pass

