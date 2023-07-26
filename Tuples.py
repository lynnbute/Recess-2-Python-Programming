#inbuilt data types, used to store items in a single variable.
#they are ordered and non changeable meaning you cannot add items once the tuple is created
phones = ("Samsung", "Iphone","Tecno")
print(phones)

#allow for duplicate values
phones = ("Samsung", "Iphone","Tecno", "Samsung", "Iphone")
print(phones)

#Tuple length
print(len(phones))

#Tuple showing different data types
tuple1 = ("matooke", "rice", "ground-nuts")
tuple2 =(100, 200, 300, 500)
print(type(tuple2))

#Exercise: how to access tuples
  #using indexes
tuple1 = ("matooke", "rice", "ground-nuts")
print(tuple1[0])
print(tuple1[2])

#Accessing with negative index
tuple1 = ("matooke", "rice", "ground-nuts","fish","beans","yams","cassava")
print(tuple1[-1])
print(tuple1[-5])

#Accessing tuples using ranges
tuple1 = ("matooke", "rice", "ground-nuts","fish","beans","yams","cassava")
print(tuple1[2:5])
print(tuple1[:5])
print(tuple1[1:])

#Range with negative index
#This example returns the items from index -4 (included) to index -1 (excluded)
tuple1 = ("matooke", "rice", "ground-nuts","fish","beans","yams","cassava")
print(tuple1[-4:-1])


#adding items in tuples
phones = ("Samsung", "Iphone","Tecno")
s = list(phones)
print(s)
s.append("Nokia")
print(s)
phones = tuple(s)
print(phones)

#Exercise: adding tuples together
laptops = ("Dell", "HP", "Acer")
new_laptop = ("Samsung",)
laptops +=new_laptop
print(laptops)

#Loop through a tuple
phones = ("Samsung", "Iphone","Tecno")
for x in phones:
    print(x)