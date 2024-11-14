name = input("what is your name\n")
weather = input("how is the weather today?\n(hot,cold,normal) ").lower()
time_of_day = input('what is the time of the day\n(morning,afternoon,evening) ').lower()
if weather =="hot":
    print("it is hot outside today")
    if time_of_day =="morning":
        print("it is morning")
elif weather =="cold":
    print("it is cold outside today")
    if time_of_day=="afternoon":
        print("it is mid day")
elif weather =="normal":
    print("the weather is normal today")
    if time_of_day=="evening":
        print("it is getting dark soon")
else:
    print("i do not understand that")




