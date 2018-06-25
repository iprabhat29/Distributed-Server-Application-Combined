with open("log.txt") as file:
  files = file.readlines()
file.close()
#print type(files),files[6]

time_list = []
for i in files:
  i_temp = str(i)
  if 'Time' in i:
    i_list = i.split()
    len_list = len(i_list) - 1
    time_list.append(i_list[len_list])

Sum = 0.000000000000
div = 0
for i in range(0,len(time_list) - 1):
  temp = float(time_list[i])
  Sum = Sum + temp
  div = div + 1

avg_response_time = Sum / div
print "Average Response Time--->",avg_response_time
