


#----------------------------------------------
#---- Date and Time => Format Data-----
#----------------------------------------------
# https://strftime.org/
#----------------------------------------------


import datetime


myBirthDay = datetime.datetime(1995,7,25)

print(myBirthDay) # 1995-07-25 00:00:00
print(myBirthDay.strftime("%a")) # Tue
print(myBirthDay.strftime("%A")) # Tuesday
print(myBirthDay.strftime("%b")) # Jul
print(myBirthDay.strftime("%B")) # July

print(myBirthDay.strftime("%d %B %Y")) # 25 July 1995
print(myBirthDay.strftime("%d ,  %B ,  %Y")) # 25 ,  July ,  1995
print(myBirthDay.strftime("%d/%B /%Y")) # 25/July /1995
print(myBirthDay.strftime("%d. %B .%Y")) # 25. July .1995

# print(dir(datetime.datetime)) # ['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']

