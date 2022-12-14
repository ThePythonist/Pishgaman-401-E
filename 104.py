import jdatetime

now = str(jdatetime.datetime.now())
print(now.split()[0])
print(now.split()[1][:5])
