# #string concatenation (aka how to put strings together)
# #suppose we want to create a string that says "subscribe to _____"

# youtuber = "Kylie Ying" # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj=input("Enter an adjective: ")
verb1=input("Enter a verb: ")
verb2=input("Enter a verb: ")
famous_person=input("Enter a famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
   I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)