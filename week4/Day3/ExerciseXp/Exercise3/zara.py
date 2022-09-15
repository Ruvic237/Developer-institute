#zARA

brand = {
"name": "Zara",
"creation_date": 1975, 
"creator_name": "Amancio Ortega Gaona", 
"type_of_clothes": ["men", "women", "children", "home"], 
"international_competitors": ["Gap", "H&M", "Benetton"], 
"number_stores": 7000, 
"major_color":{ 
    "France": "blue", 
    "Spain": "red", 
    "US": ["pink", "green"]
  }
}

brand["number_stores"] = 2 #change number of store value
print(brand["name"], "clients are men,women,children")
brand["country_creation"] = "Spain" #New key with value spain

for check in brand:
    if check == "international_competitors":
        brand["international_competitors"].append("Desigual")

del brand["creation_date"] #deleting key from dictionary
print(brand["international_competitors"][len(brand["international_competitors"])-1])
print(brand["major_color"]["US"])
print(len(brand.keys())) # print total keys of dict
print(brand)

more_on_zara = {
    "creation_date": 1975, 
    "number_stores": "10 000",
}
brand.update(more_on_zara)
print(brand["number_stores"]) # more_zara value overwrite brand value 








     


