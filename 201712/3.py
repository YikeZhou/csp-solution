'''
File: 3.py
Project: 201712
File Created: Sunday, 6th September 2020 10:10:23 am
Author: zyk
-----
Last Modified: Sunday, 6th September 2020 4:49:46 pm
Modified By: zyk
-----
2020 - HUST
'''

from datetime import datetime, timedelta

class Time:
    def __init__(self, year, month, day, hour, minute):
        self.dt = datetime(year, month, day, hour, minute)
    
    @classmethod
    def parse(cls, num):
        return cls(int(num / 100000000), int((num % 100000000) / 1000000), int((num % 1000000) / 10000),
                            int((num % 10000) / 100), int(num % 100))
    
    def __repr__(self):
        return 'Time({0.dt.year!r}, {0.dt.month!r}, {0.dt.day!r}, {0.dt.hour!r}, {0.dt.minute!r})'.format(self)
    
    def __str__(self):
        return '{0.dt.year!r}'.format(self).zfill(4) + '{0.dt.month!r}'.format(self).zfill(2) + '{0.dt.day!r}'.format(self).zfill(2) + '{0.dt.hour!r}'.format(self).zfill(2) + '{0.dt.minute!r}'.format(self).zfill(2)
    
    def inc(self):
        one_min = timedelta(minutes=1)
        self.dt += one_min


Weekdays = {'sun': 0, 'mon': 1, 'tue': 2, 'wed': 3, 'thu': 4, 'fri': 5, 'sat': 6}
Months = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4,  'may': 5,  'jun': 6,
          'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}

def get_month(s):
    if s.lower() in Months.keys():
        return Months[s.lower()]
    else:
        return int(s)

def get_weekday(s):
    if s.lower() in Weekdays.keys():
        return Weekdays[s.lower()]
    else:
        return int(s)

class Task:
    def __init__(self, minutes, hours, day_of_month, month, day_of_week, command):
        # save command str and interval
        self.command = command

        self.minutes = list()
        if minutes == '*':
            self.minutes.append((0, 59))
        else:
            ms = minutes.split(sep=',')
            for m in ms:
                if '-' in m:
                    a, b = map(int, m.split(sep='-'))
                    self.minutes.append((a, b))
                else:
                    a = int(m)
                    self.minutes.append((a, a))

        self.hours = list()
        if hours == '*':
            self.hours.append((0, 23))
        else:
            hs = hours.split(sep=',')
            for h in hs:
                if '-' in h:
                    a, b = map(int, h.split(sep='-'))
                    self.hours.append((a, b))
                else:
                    a = int(h)
                    self.hours.append((a, a))

        self.day_of_month = list()
        if day_of_month == '*':
            self.day_of_month.append((1, 31))
        else:
            doms = day_of_month.split(sep=',')
            for dom in doms:
                if '-' in dom:
                    a, b = map(int, dom.split(sep='-'))
                    self.day_of_month.append((a, b))
                else:
                    a = int(dom)
                    self.day_of_month.append((a, a))

        self.month = list()
        if month == '*':
            self.month.append((1, 12))
        else:
            mos = month.split(sep=',')
            for mo in mos:
                if '-' in mo:
                    a, b = map(get_month, mo.split(sep='-'))
                    self.month.append((a, b))
                else:
                    a = get_month(mo)
                    self.month.append((a, a))

        self.day_of_week = list()
        if day_of_week == '*':
            self.day_of_week.append((0, 6))
        else:
            dows = day_of_week.split(sep=',')
            for dow in dows:
                if '-' in dow:
                    a, b = map(get_weekday, dow.split(sep='-'))
                    self.day_of_week.append((a, b))
                else:
                    a = get_weekday(dow)
                    self.day_of_week.append((a, a))
    
    def match(self, t: Time):
        # month
        for (b, e) in self.month:
            if b <= t.dt.month and t.dt.month <= e:
                break
        else:
            return False
        # day of month
        for (b, e) in self.day_of_month:
            if b <= t.dt.day and t.dt.day <= e:
                break
        else:
            return False
        # hour
        for (b, e) in self.hours:
            if b <= t.dt.hour and t.dt.hour <= e:
                break
        else:
            return False
        # minute
        for (b, e) in self.minutes:
            if b <= t.dt.minute and t.dt.minute <= e:
                break
        else:
            return False
        # day of week
        for (b, e) in self.day_of_week:
            dow = (t.dt.weekday() + 1) % 7
            if b <= dow and dow <= e:
                break
        else:
            return False
        return True

n, s, t = map(int, input().split())
confs = list()

# read n lines
for i in range(n):
    # crontab config info
    minutes, hours, day_of_month, month, day_of_week, command = input().split()
    # process each field
    confs.append(Task(minutes, hours, day_of_month, month, day_of_week, command))

start = Time.parse(s)
end = Time.parse(t)

cur = start
while cur.dt != end.dt:
    for conf in confs:
        if conf.match(cur):
            print(cur, conf.command)
    cur.inc()
