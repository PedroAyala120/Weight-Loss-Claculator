#This program will calculate your estimated weight loss for 6 months
#Pedro Ayala

#Input user weight
weight = int(input('Input your weight in pounds: '))

#loop to calculate and print the user's estimated weight
for i in range (1, 7):
    weight = weight - 4
    print ("Your weight for month #", i, "is: ", weight,"lbs")
