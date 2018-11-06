food = "junk"

if food == "junk":
    print("The food is junk?")
else:
    print("The food is not junk.")


friends = ["Mina", "Hung", "Jean", "John", "Uyen"]

#for friend in range(0,3):
   # invitation_ = "Hi " + friends[friend]
   # print(invitation_)

i = 0

while i <= (len(friends)-1):
    invitation_ = "Hi " + friends[i]
    print(invitation_)
    #if i==(len(friends)-1):
        #break
    i += 1