cardetails  = {
    "brand"  : "ford",
    "milage" :  13,
    "model": 14.2,
}
cardetails["colour"] = ["red","black","blue"]     #to add smthg
print(cardetails.keys())    #prints names mentioned in the dictionary
print(cardetails.values())   #prints values of that names
cardetails.popitem()         #removes the last key and value pair
print(cardetails)

 #use this when dictionary is activated


#cardetails = list(cardetails)  ##
#cardetails.pop()               #should use only the dictionary is -> list
#print("--after converted to list,diff")
#print(cardetails[1])

