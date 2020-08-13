in_seconds = int(input("write time in seconds: "))

seconds = in_seconds % 60
minutes_all = int(in_seconds / 60)
minutes = minutes_all%60
hours = int(minutes_all / 60)

seconds = "%02d"%seconds
minutes = "%02d"%minutes
hours = "%02d"%hours

print(f"{hours}:{minutes}:{seconds}")