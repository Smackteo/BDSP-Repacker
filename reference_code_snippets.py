import UnityPy
import random
import os
import json
from pathlib import Path
import lz4.block

src = "Resources/personal_masterdatas"
jsonSrc = 'import/ItemTable.json'
evoSrc = "import/EvolveTable.json"
persoSrc = "import/PersonalTable.json"
env = UnityPy.load(src)

rawJson = 0
rawEvoTable = 0
personalJsonObj = 0

with open(jsonSrc) as f:
    rawJson = json.load(f)
    print("Loaded Itemtable...")
with open(evoSrc) as f:
    rawEvoTable = json.load(f)
    print("Loaded EvolveTable...")
with open(persoSrc) as f:
    personalJsonObj = json.load(f)
    print("Loaded personal...")

def getItem(itemID):
    for item in rawJson["Item"]:
        if item["no"] == itemID:
            print(item)
            return item


def buildItem(item):
    jItem = getItem(item["no"])
    if jItem == None:
        return None
    item["no"] = jItem["no"]
    item["type"] = jItem["type"]
    item["iconid"] = jItem["iconid"]
    item["price"] = jItem["price"]
    item["bp_price"] = jItem["bp_price"]
    item["eqp"] = jItem["eqp"]
    item["atc"] = jItem["atc"]
    item["nage_atc"] = jItem["nage_atc"]
    item["sizen_atc"] = jItem["sizen_atc"]
    item["sizen_type"] = jItem["sizen_type"]
    item["tuibamu_eff"] = jItem["tuibamu_eff"]
    item["sort"] = jItem["sort"]
    item["group"] = jItem["group"]
    item["group_id"] = jItem["group_id"]
    item["fld_pocket"] = jItem["fld_pocket"]
    item["field_func"] = jItem["field_func"]
    item["battle_func"] = jItem["battle_func"]
    item["wk_cmn"] = jItem["wk_cmn"]
    item["wk_critical_up"] = jItem["wk_critical_up"]
    item["wk_atc_up"] = jItem["wk_atc_up"]
    item["wk_def_up"] = jItem["wk_def_up"]
    item["wk_agi_up"] = jItem["wk_agi_up"]
    item["wk_hit_up"] = jItem["wk_hit_up"]
    item["wk_spa_up"] = jItem["wk_spa_up"]
    item["wk_spd_up"] = jItem["wk_spd_up"]
    item["wk_prm_pp_rcv"] = jItem["wk_prm_pp_rcv"]
    item["wk_prm_hp_exp"] = jItem["wk_prm_hp_exp"]
    item["wk_prm_pow_exp"] = jItem["wk_prm_pow_exp"]
    item["wk_prm_def_exp"] = jItem["wk_prm_def_exp"]
    item["wk_prm_agi_exp"] = jItem["wk_prm_agi_exp"]
    item["wk_prm_spa_exp"] = jItem["wk_prm_spa_exp"]
    item["wk_prm_spd_exp"] = jItem["wk_prm_spd_exp"]
    item["wk_friend1"] = jItem["wk_friend1"]
    item["wk_friend2"] = jItem["wk_friend2"]
    item["wk_friend3"] = jItem["wk_friend3"]
    item["wk_prm_hp_rcv"] = jItem["wk_prm_hp_rcv"]
    item["flags0"] = jItem["flags0"]
    return item

def getEvolveArray(monId):
    for mon in rawEvoTable["Evolve"]:
        if mon["id"] == monId:
            return list(map(int, mon["ar"]))

def buildEvolveArray(mon):
    mon["ar"] = getEvolveArray(mon["id"])
    return mon

def getPersonalItem(personalID):
    for p in personalJsonObj["Personal"]:
        if p["id"] == personalID:
            return p

def buildPersonalObject(personal):
    personalJson = getPersonalItem(personal["id"])
    personal["valid_flag"] = personalJson["valid_flag"]
    personal["id"] = personalJson["id"]
    personal["monsno"] = personalJson["monsno"]
    personal["form_index"] = personalJson["form_index"]
    personal["form_max"] = personalJson["form_max"]
    personal["color"] = personalJson["color"]
    personal["gra_no"] = personalJson["gra_no"]
    personal["basic_hp"] = personalJson["basic_hp"]
    personal["basic_atk"] = personalJson["basic_atk"]
    personal["basic_def"] = personalJson["basic_def"]
    personal["basic_agi"] = personalJson["basic_agi"]
    personal["basic_spatk"] = personalJson["basic_spatk"]
    personal["basic_spdef"] = personalJson["basic_spdef"]
    personal["type1"] = personalJson["type1"]
    personal["type2"] = personalJson["type2"]
    personal["get_rate"] = personalJson["get_rate"]
    personal["rank"] = personalJson["rank"]
    personal["exp_value"] = personalJson["exp_value"]
    personal["item1"] = personalJson["item1"]
    personal["item2"] = personalJson["item2"]
    personal["item3"] = personalJson["item3"]
    personal["sex"] = personalJson["sex"]
    personal["egg_birth"] = personalJson["egg_birth"]
    personal["initial_friendship"] = personalJson["initial_friendship"]
    personal["egg_group1"] = personalJson["egg_group1"]
    personal["egg_group2"] = personalJson["egg_group2"]
    personal["grow"] = personalJson["grow"]
    personal["tokusei1"] = personalJson["tokusei1"]
    personal["tokusei2"] = personalJson["tokusei2"]
    personal["tokusei3"] = personalJson["tokusei3"]
    personal["give_exp"] = personalJson["give_exp"]
    personal["height"] = personalJson["height"]
    personal["weight"] = personalJson["weight"]
    personal["chihou_zukan_no"] = personalJson["chihou_zukan_no"]
    personal["machine1"] = personalJson["machine1"]
    personal["machine2"] = personalJson["machine2"]
    personal["machine3"] = personalJson["machine3"]
    personal["machine4"] = personalJson["machine4"]
    personal["hiden_machine"] = personalJson["hiden_machine"]
    personal["egg_monsno"] = personalJson["egg_monsno"]
    personal["egg_formno"] = personalJson["egg_formno"]
    personal["egg_formno_kawarazunoishi"] = personalJson["egg_formno_kawarazunoishi"]
    personal["egg_form_inherit_kawarazunoishi"] = personalJson["egg_form_inherit_kawarazunoishi"]
    return personal


for obj in env.objects:
    if obj.type.name == "MonoBehaviour":
        if obj.serialized_type.nodes:
            tree = obj.read_typetree()
            
            if tree['m_Name'] == "ItemTable":
                for item in tree['Item']:
                    if(item["no"] == 321):
                        item = buildItem(item)
                    item = buildItem(item)
                
                obj.save_typetree(tree)
            elif tree['m_Name'] == "EvolveTable":
                for mon in tree['Evolve']:
                    mon = buildEvolveArray(mon)
                
                obj.save_typetree(tree)
            elif tree['m_Name'] == "PersonalTable":
                for personal in tree["Personal"]:
                    personal = buildPersonalObject(personal)
                
                obj.save_typetree(tree)

mod_folder = "Data/StreamingAssets/AssetAssistant/Pml"         
Path(mod_folder).mkdir(parents=True, exist_ok=True)
os.chdir(mod_folder)

with open("Resources/personal_masterdatas", "wb") as t:
    t.write(env.file.save(packer = (64,2)))
    


