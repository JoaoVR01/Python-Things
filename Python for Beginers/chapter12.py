#dictionaries
personal_data = {
    "name": "Luiza",
    "age": 19,
    "height":156.7,
}

#this is how we access an item in a dictionary
print(personal_data["name"])

#modifing the dictionary info
personal_data["name"] = "Lara"
print(personal_data["name"])

#adding values in a dictionary
personal_data["graduation"] = "Medicine"

#removing values in a dictionary
personal_data.pop("graduation")
print(personal_data.items())
lista = [1,2,3,4,5,6]
list_str = list(map(str, lista)) #map funcion is used to aply a function to all iterable iten's
print(list_str)

product1 = {'price': 120, 'name': 'keyboard'}
product2 = {'price': 50, 'name': 'headphone'}
product_list = [product1, product2]

i=0
while i < len(product_list):
    print(product_list[i]['name']) #this is how we access the iten in the dictionary inside a list
    print(product_list[i]['price'])
    i+=1
