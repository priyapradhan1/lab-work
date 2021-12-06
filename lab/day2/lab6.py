# you live 4 miles from univesity.The bus driver at 25mph but spends 2 minutes at each
#of the 10 stops on the way. how long will the bus journey take? Alternatively, you could
#run to university. you jog the first mile at 7mph ; then run the next two at 15mph ; before
#jogging the last at 7mph again. will this be quicker or slower than the bus
distance=4
velocity=25
t1=((distance/velocity)*60)
# since the bus spends two minutes in each steps so 2*10
t2=20
total1=t1+t2
print(f"total time taken by bus is {total1}")
# when jogging
b=7
f=1/b
time_1=f*60
c=15
g=1/c
time_2=g*60
d=7
h=1/d
time_3=h*60
total_2=time_1+time_2+time_3
print(f"the total time for jogging is {total_2}")
if total_2>total1:
    print(f"jogging is fast to reach the university")
else:
    print(f"going by bus is fast to reach university")
