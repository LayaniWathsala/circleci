from django.test import TestCase

import datetime

from django.test import TestCase
from django.utils import timezone
from cal.models import Numbers


class QuestionModelTests(TestCase):

    def date_compare_test(self):
        time1 = timezone.now() 
        time2 = timezone.now() + datetime.timedelta(days=30)

        dates = Numbers(date1=time1,date2=time2)
        self.assertIs(dates.compare(), True)