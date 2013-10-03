from models import Bp, Glucose, Init, Login, Pedometer, Questions, Users, Weight

class Data():
    
    def __init__(self):
        self.YEAR=31536000
        self.MONTH=2592000
        self.WEEK=604800
        self.DAY=86400
    
    def active_users(self):
        pass

    def last(self, week, _model):
        query = "SELECT MAX(measured_on) AS lastdate FROM pedometer WHERE 52 - CAST((((SELECT MAX(measured_on) FROM pedometer) - measured_on) / "+ str(self.WEEK) + " ) AS SIGNED) =" + str(week)
#         from django.db.models import Max
# 
#         return _model._default_manager.raw(query)   
#         return m.aggregate(Max('date')) 
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

        
for week in range(1,53):
    data = Data()
    last = data.last(week,Pedometer())
    for l in last:
        print l