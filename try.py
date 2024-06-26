from services.user_service import user_service

user_service_instance = user_service()

# נתוני בדיקה
user_id = '60d5ec49f07e4c7e788b4567'
data = {'name': 'New Name', 'age': 30, 'user_id': 'should_not_change'}

# קריאה לפונקציות
print(user_service_instance.get_all())
print(user_service_instance.get_by_id(user_id))
print(user_service_instance.create(data))
print(user_service_instance.update(user_id, data))
print(user_service_instance.delete(user_id))
