# for i in range(202003010,20190101,-1000000000000000):
#     print(i)

# for i in range(10,0,-5):
#     print(i)

# start = 20203010000000000000 
# stop = 201901010000000000000
# step =  1000000000000000


# Select COUNT(*),SOURCE_SYSTEM from
#    PP_BAP_PROD.sapsr3_ba1_f2_bt_flat where ZTEF > '20203010000000000000' and
#    POSTING_DATE_EXT < '20191201' and SOURCE_SYSTEM NOT IN ('SITE','PPXB') group by SOURCE_SYSTEM;

# i = 20200301
# while i >= 20190101:
#     i = i - 100
#     print(i)

i = 1
while i < 6:
  print(i)
  i += 1


# from datetime import date, timedelta
# import calendar
# start_date = date(2014, 12, 25)
# days_in_month = calendar.monthrange(start_date.year, start_date.month)[1]
# print(start_date + timedelta(days=days_in_month))



import datetime

# datetime.timedelta(days:32)

# from slackclient import SlackClient



one = ['1','2','3']
two = ['4','5','6']

for i,j in zip(one,two):
  print(i,j)
  
ztef = ['201911010000000000000','201910010000000000000','201909010000000000000','201908010000000000000','201907010000000000000','201906010000000000000','201905010000000000000','201904010000000000000','201903010000000000000','201902010000000000000','201901010000000000000']
post_date = ['20190801','20190701','20190601','20190501','20190401','20190301','20190201','20190101','20181201','20181101','20181001']
len(ztef)
len(post_date)


ztef = ['201911010000000000000','201910010000000000000','201909010000000000000','201908010000000000000','201907010000000000000','201906010000000000000','201905010000000000000','201904010000000000000','201903010000000000000','201902010000000000000','201901010000000000000']
post_date = ['20190801','20190701','20190601','20190501','20190401','20190301','20190201','20190101','20181201','20181101','20181001']

count = 0
for x,y in zip(ztef,post_date):
  print(f"ZTEF > {x} and POSTING_DATE_EXT < {y}")
  df = x + y
  count += 1
  print(f"Count: {count}")
  file_name = 'records' + str(count)
  print(f"File Name: {file_name}")


df = [lambda x,y : print(f"ZTEF > {x} and POSTING_DATE_EXT < {y} \n"), zip(ztef,post_date)]
print(df)



ztef = ['202003010000000000000','202002010000000000000','202001010000000000000','201912010000000000000','201911010000000000000','201910010000000000000','201909010000000000000','201908010000000000000','201907010000000000000','201906010000000000000','201905010000000000000','201904010000000000000','201903010000000000000','201902010000000000000','201901010000000000000']
post_date = ['20191201','20191101','20191001','20190901','20190801','20190701','20190601','20190501','20190401','20190301','20190201','20190101','20181201','20181101','20181001']

def itrate(ztef,post_date):
    for x,y in zip(ztef,post_date):
        print(f"ZTEF > {x} and POSTING_DATE_EXT < {y}")
        result = %hive_stampy Select COUNT(*),SOURCE_SYSTEM from PP_BAP_PROD.sapsr3_ba1_f2_bt_flat where ZTEF > {x} and POSTING_DATE_EXT < {y} and SOURCE_SYSTEM NOT IN ('SITE','PPXB') group by SOURCE_SYSTEM;
        return result
            

post_date1 = [ str(i) for i in range(20191201,20191101,-1) if i <= 20191129]
post_date1

ztef1 = [str(i)+'0000000000000' for i in range(20200301,20200201,-1) if i <= 20200229]
ztef1


src_system = ['ANAPRO','CURE','FB1','PARTICIPTN','TFC','VENMO']
src_system.remove('FB1')
src_system

x = ['FB1']
while len(src_system) > 0:
  for src in src_system:
    if src in x:
      list(src_system).remove('FB1')
      print(src_system)


count = 1
for x,y in zip(ztef1,post_date1):
  print(f"ZTEF > {x} and POSTING_DATE_EXT < {y} AND Source: {src_system}")
  df = x + y
  count += 1
  print(f"Count: {count}")
  file_name = 'records' + str(count)
  print(f"File Name: {file_name}")


src_system = ('ANAPRO','CURE','FB1','PARTICIPTN','TFC','VENMO')
x = ['FB1']
for src in src_system:
  src_system = list(src_system)
  if src in x:
    src_system.remove('FB1')
    src_system = tuple(src_system)
    print(src_system)



len('201901010000000000000')