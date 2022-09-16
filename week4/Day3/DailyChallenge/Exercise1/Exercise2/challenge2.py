
items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"
amount = int(wallet.replace("$",""))
new = []

for items in items_purchase.keys():
  if int(items_purchase[items].replace("$","").replace(",",""))<=amount:
    new.append(items)
print(sorted(new))
    


