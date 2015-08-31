# import datetime
# from haystack import indexes
# from students.models.students import Student


# class StudentIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     last_name = indexes.CharField(model_attr='last_name')
#     first_name = indexes.CharField(model_attr='first_name')
    
#     def get_model(self):
#         return Student

#     def index_queryset(self, using=None):
#         """Used when the entire index for model is updated."""
#         return self.get_model().objects.all()



import datetime

from haystack import indexes
from students.models.students import Student

class StudentIndex(indexes.SearchIndex, indexes.Indexable):
    '''haystack's searchindex object handles data flow into elasticsearch'''

    text             = indexes.CharField(document=True, use_template=True) # EdgeNgramField - tagging
    last_name     = indexes.CharField(model_attr='last_name')

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        # return self.get_model().objects.filter(created__lte=datetime.datetime.utcnow().replace(tzinfo=utc))
        return self.get_model().objects.all()

    def get_model(self):
    	print 'ready'
        return Student



    def prepare_last_name(self, obj):
        return obj.last_name 

    
    