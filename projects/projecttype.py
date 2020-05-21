from django.utils.translation import ugettext as _
from django.db.models import SmallIntegerField
from django.db import models

# DAY_OF_THE_WEEK = {
#     'Monday' : _(u'Monday'),
#     'Tuesday' : _(u'Tuesday'),
#     'Wednesday' : _(u'Wednesday'),
#     'Thursday' : _(u'Thursday'),
#     'Friday' : _(u'Friday'),
#     'Saturday' : _(u'Saturday'), 
#     'Sunday' : _(u'Sunday'),
# }

TYPES_OF_PROJECTS = {
    'Current' : _(u'Current Project'),
    'Completed' : _(u'Completed Project'),
}

# class DayOfTheWeekField(models.CharField):
#     def __init__(self, *args, **kwargs):
#         kwargs['choices']=tuple(sorted(DAY_OF_THE_WEEK.items()))
#         kwargs['max_length']=10 
#         super(DayOfTheWeekField,self).__init__(*args, **kwargs)

class TypesOfProjectsField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices']=tuple(sorted(TYPES_OF_PROJECTS.items()))
        kwargs['max_length']=10 
        super(TypesOfProjectsField,self).__init__(*args, **kwargs)