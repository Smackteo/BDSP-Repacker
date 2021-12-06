import os
import UnityPy
import json

#Smackteo's BDSP repacker

src = "Resources/personal_masterdatas"
#jsonSrc = 'ItemTable.json'
#evoSrc = "EvolveTable.json"
#persoSrc = "personaltable.json"

#I need to save every user .json as an .asset file
#Then

env = UnityPy.load(src)
for obj in env.objects:
    if obj.container == "assets/pml/data/wazatable.asset":
        if os.path.exists('import/WazaTable.json'):
            tree = obj.read_typetree()
            with open('import/WazaTable.json', "rt", encoding="utf8") as f:
                data = json.load(f)
            print('WazaTable updated')
            obj.save_typetree(data)
        else:
            print('WazaTable not updated if this is intended ignore this message')
    if obj.container == "assets/pml/data/sealtable.asset":
        if os.path.exists('import/SealTable.json'):
            tree = obj.read_typetree()
            with open('import/SealTable.json', "rt", encoding="utf8") as f:
                data = json.load(f)
            print('SealTable updated')
            obj.save_typetree(data)
        else:
            print('SealTable not updated if this is intended ignore this message')
    if obj.container == "assets/pml/data/ugfatherexpansion.asset":
        if os.path.exists('import/UgFatherExpansion.json'):
            tree = obj.read_typetree()
            with open('import/UgFatherExpansion.json', "rt", encoding="utf8") as f:
                data = json.load(f)
            print('UgFatherExpansion updated')
            obj.save_typetree(data)
        else:
            print('UgFatherExpansion not updated if this is intended ignore this message')
    if obj.container == "assets/pml/data/ugitemtable.asset":
        if os.path.exists('import/UgItemTable.json'):
            tree = obj.read_typetree()
            with open('import/UgItemTable.json', "rt", encoding="utf8") as f:
                data = json.load(f)
            print('UgItemTable updated')
            obj.save_typetree(data)
        else:
            print('UgItemTable not updated if this is intended ignore this message')
    if obj.container == "assets/pml/data/growtable.asset":
        if os.path.exists('import/GrowTable.json'):
            tree = obj.read_typetree()
            with open('import/GrowTable.json', "rt", encoding="utf8") as f:
                data = json.load(f)
            print('GrowTable updated')
            obj.save_typetree(data)
        else:
            print('GrowTable not updated if this is intended ignore this message')
    if obj.container == "assets/pml/data/addpersonaltable.asset":
        if os.path.exists('import/AddPersonalTable.json'):
            tree = obj.read_typetree()
            with open('import/AddPersonalTable.json', "rt", encoding="utf8") as f:
                data = json.load(f)
            print('AddPersonalTable updated')
            obj.save_typetree(data)
        else:
            print('AddPersonalTable not updated if this is intended ignore this message')
    if obj.container == "assets/pml/data/itemtable.asset":
        if os.path.exists('import/ItemTable.json'):
            tree = obj.read_typetree()
            with open('import/ItemTable.json', "rt", encoding="utf8") as f:
                data = json.load(f)
            print('ItemTable updated')
            obj.save_typetree(data)
        else:
            print('ItemTable not updated if this is intended ignore this message')
    if obj.container == "assets/pml/data/ugfatherpos.asset":
        if os.path.exists('import/UgFatherPos.json'):
            tree = obj.read_typetree()
            with open('import/UgFatherPos.json', "rt", encoding="utf8") as f:
                data = json.load(f)
            print('UgFatherPos updated')
            obj.save_typetree(data)
        else:
            print('UgFatherPos not updated if this is intended ignore this message')
    if obj.container == "assets/pml/data/wazaoboetable.asset":
        if os.path.exists('import/WazaOboeTable.json'):
            tree = obj.read_typetree()
            with open('import/WazaOboeTable.json', "rt", encoding="utf8") as f:
                data = json.load(f)
            print('WazaOboeTable updated')
            obj.save_typetree(data)
        else:
            print('WazaOboeTable not updated if this is intended ignore this message')
    if obj.container == "assets/pml/data/tamagowazatable.asset":
        if os.path.exists('import/TamagoWazaTable.json'):
            tree = obj.read_typetree()
            with open('import/TamagoWazaTable.json', "rt", encoding="utf8") as f:
                data = json.load(f)
            print('TamagoWazaTable updated')
            obj.save_typetree(data)
        else:
            print('TamagoWazaTable not updated if this is intended ignore this message')
    if obj.container == "assets/pml/data/tamatable.asset":
        if os.path.exists('import/TamaTable.json'):
            tree = obj.read_typetree()
            with open('import/TamaTable.json', "rt", encoding="utf8") as f:
                data = json.load(f)
            print('TamaTable updated')
            obj.save_typetree(data)
        else:
            print('TamaTable not updated if this is intended ignore this message')
    if obj.container == "assets/pml/data/evolvetable.asset":
        if os.path.exists('import/EvolveTable.json'):
            tree = obj.read_typetree()
            with open('import/EvolveTable.json', "rt", encoding="utf8") as f:
                data = json.load(f)
            print('EvolveTable updated')
            obj.save_typetree(data)
        else:
            print('EvolveTable not updated if this is intended ignore this message')
    if obj.container == "assets/pml/data/pedestaltable.asset":
        if os.path.exists('import/PedestalTable.json'):
            tree = obj.read_typetree()
            with open('import/PedestalTable.json', "rt", encoding="utf8") as f:
                data = json.load(f)
            print('PedestalTable updated')
            obj.save_typetree(data)
        else:
            print('PedestalTable not updated if this is intended ignore this message')
    if obj.container == "assets/pml/data/personaltable.asset":
        if os.path.exists('import/PersonalTable.json'):
            tree = obj.read_typetree()
            with open('import/PersonalTable.json', "rt", encoding="utf8") as f:
                data = json.load(f)
            print('PersonalTable updated')
            obj.save_typetree(data)
        else:
            print('PersonalTable not updated if this is intended ignore this message')
    if obj.container == "assets/pml/data/ugfathershoptable.asset":
        if os.path.exists('import/UgFatherShopTable.json'):
            tree = obj.read_typetree()
            with open('import/UgFatherShopTable.json', "rt", encoding="utf8") as f:
                data = json.load(f)
            print('UgFatherShopTable updated')
            obj.save_typetree(data)
        else:
            print('UgFatherShopTable not updated if this is intended ignore this message')
    if obj.container == "assets/pml/data/stonestatueeffect.asset":
        if os.path.exists('import/StoneStatuEeffect.json'):
            tree = obj.read_typetree()
            with open('import/StoneStatuEeffect.json', "rt", encoding="utf8") as f:
                data = json.load(f)
            print('StoneStatuEeffect updated')
            obj.save_typetree(data)
        else:
            print('StoneStatuEeffect not updated if this is intended ignore this message')

with open("output/personal_masterdatas", "wb") as t:
    t.write(env.file.save(packer=(64, 2)))

input('Repack complete enter any key to exit')