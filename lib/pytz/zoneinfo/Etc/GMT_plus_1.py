'''tzinfo timezone information for Etc/GMT_plus_1.'''
from pytz.tzinfo import StaticTzInfo
from pytz.tzinfo import memorized_timedelta as timedelta

class GMT_plus_1(StaticTzInfo):
    '''Etc/GMT_plus_1 timezone definition. See datetime.tzinfo for details'''
    _zone = 'Etc/GMT_plus_1'
    _utcoffset = timedelta(seconds=-3600)
    _tzname = 'GMT+1'

GMT_plus_1 = GMT_plus_1()

