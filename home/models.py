from django.db import models

class Metrics(models.Model):
    week      = models.IntegerField()
    pedometer = models.FloatField()
    logins    = models.FloatField()
    questions = models.FloatField()
    weekend   = models.FloatField()
    tracking  = models.FloatField()
    
    client    = models.CharField(max_length=64, default="ALL")
    gender    = models.CharField(max_length=8,  default="ALL")
    age       = models.CharField(max_length=8,  default="ALL")
    condition = models.CharField(max_length=64, default="ALL")
    tenure    = models.CharField(max_length=64, default="ALL")
    

    def json(self):
        from collections import OrderedDict
        #import ordereddict as OrderedDict
        return OrderedDict((
            ('Week', self.week),
            ('Pedometer', self.pedometer),
            ('Logins', self.logins),
            ('Questions', self.questions),
            ('Weekend-Logins', self.weekend),
            ('Self-Tracking', self.tracking)
        ))

    
    @staticmethod
    def csv_import(path):
        import csv
        with open(path, 'rb') as f:
            for n, row in enumerate(csv.reader(f)):
                if n > 0:
                    metric = Metrics()
                    metric.week      = row[0]
                    metric.pedometer = row[1]
                    metric.logins    = row[2]
                    metric.questions = row[3]
                    metric.weekend   = row[4]
                    metric.tracking  = row[5]
                    metric.client    = row[6]
                    metric.gender    = row[7]
                    metric.age       = row[8]
                    metric.condition = row[9]
                    metric.tenure    = row[10]
                    
                    metric.save()
    

