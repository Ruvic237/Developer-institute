#Working with JSON

import json
samplejson = '''{
    "company":{
        "employee":{
            "name":"emma",
            "payable":{
                "salary":7000,
                "bonus":800
            }
        }
    }
}
'''

data = json.loads(samplejson)
for i in data["company"]["employee"]["payable"]:
    if i == "salary":
        print(i)

data["company"]["employee"]["birth-day"]="February"

sali = json.dumps(data)
print(sali)

with open("json_sho.json",'w') as JSON:
    json.dump(data,JSON,indent=2,sort_keys=True)
    
    
    

