# converts seconds to day, hour and minutes
s=int(input("enter the value for second:"))
day=(((s/60)/60)/24)
print(f"total day for given seconds:{day}")
hour=((s/60)/60)
print(f"total hour for given seconds:{hour}")
minute=(s/60)
print(f"total minutes for given seconds")
