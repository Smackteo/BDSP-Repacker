import os
import UnityPy
import json

src = "Resources/personal_masterdatas"
#jsonSrc = 'ItemTable.json'
#evoSrc = "EvolveTable.json"
#persoSrc = "personaltable.json"

#I need to save every user .json as an .asset file
#Then

env = UnityPy.load(src)
for obj in env.objects:
    if obj.container == "assets/pml/data/wazatable.asset":
        tree = obj.read_typetree()

        with open('import/MonoBehaviour/WazaTable.json', "rt", encoding="utf8") as f:
            data = json.load(f)
        obj.save_typetree(data)
    if obj.container == "assets/pml/data/sealtable.asset":
        print(obj.container)
    if obj.container == "assets/pml/data/ugfatherexpansion.asset":
        print(obj.container)
    if obj.container == "assets/pml/data/ugitemtable.asset":
        print(obj.container)
    if obj.container == "assets/pml/data/growtable.asset":
        print(obj.container)
    if obj.container == "assets/pml/data/addpersonaltable.asset":
        print(obj.container)
    if obj.container == "assets/pml/data/itemtable.asset":
        print(obj.container)
    if obj.container == "assets/pml/data/ugfatherpos.asset":
        print(obj.container)
    if obj.container == "assets/pml/data/wazaoboetable.asset":
        print(obj.container)
    if obj.container == "assets/pml/data/tamagowazatable.asset":
        print(obj.container)
    if obj.container == "assets/pml/data/tamatable.asset":
        print(obj.container)
    if obj.container == "assets/pml/data/evolvetable.asset":
        print(obj.container)
    if obj.container == "assets/pml/data/pedestaltable.asset":
        print(obj.container)
    if obj.container == "assets/pml/data/personaltable.asset":
        print(obj.container)
    if obj.container == "assets/pml/data/ugfathershoptable.asset":
        print(obj.container)
    if obj.container == "assets/pml/data/stonestatueeffect.asset":
        print(obj.container)

with open('readme3.txt', 'w') as f:
    f.write('readme')

with open("Resources/personal_masterdatas", "wb") as t:
    t.write(env.file.save(packer=(64, 2)))
