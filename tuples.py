#1
dimensions=(300, 100)
print(dimensions)

#2 
food_tup=('sushi', 'ramen', 'chicken handi', 'butter chicken', 'pulao')
for food in food_tup:
    print(food.title())

food_tup=('sushi', 'ramen', 'chicken fried', 'butter chicken', 'chicken soup')
for newChick in food_tup:
    print(newChick.title())

for ran in range(1, 10):
    print(ran)

ranger=[ran** 2 for ran in range(1, 10)]
print(ranger)


lists=[nums**1 for nums in range(1,100)]
print(lists)