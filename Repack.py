import os
import UnityPy
import json

#Smackteo's BDSP repacker
#2.0

src = "Resources/personal_masterdatas"
directory = r'import'
env = UnityPy.load(src)
if not os.path.exists(src):
    input("Error: personal_masterdatas not found \n Ensure personal_masterdatas is in Resources folder and the file name is exact \n if this is intentional press any key to continue")

if os.path.exists(src):
    for filename in os.listdir(directory):
        checkfile = os.path.splitext(filename)[0]
        checkfile2 = checkfile.lower()
        for obj in env.objects:
            if obj.container == "assets/pml/data/{}.asset".format(checkfile2):
                tree = obj.read_typetree()
                with open('import/{}'.format(filename), "rt", encoding="utf8") as f:
                    data = json.load(f)
                print('{} updated'.format(checkfile))
                obj.save_typetree(data)
    with open("output/personal_masterdatas", "wb") as t:
        t.write(env.file.save(packer=(64, 2)))

src = "Resources/masterdatas"

if not os.path.exists(src):
    input("Error: masterdatas not found \n  Ensure masterdatas is in Resources folder and the file name is exact\n if this is intentional press any key to continue")

directory = r'import'
env = UnityPy.load(src)

if os.path.exists(src):
    for filename in os.listdir(directory):
        checkfile = os.path.splitext(filename)[0]
        checkfile2 = checkfile.lower()
        for obj in env.objects:
            if obj.container == "assets/md/placedata/{}.asset".format(checkfile2) or obj.container == "assets/md/adventurenote/{}.asset".format(checkfile2) or obj.container == "assets/md/characterinfo/{}.asset".format(checkfile2) or obj.container == "assets/md/common/{}.asset".format(checkfile2) or obj.container == "assets/md/honeytree/{}.asset".format(checkfile2) or obj.container == "assets/md/kinomidata/{}.asset".format(checkfile2) or obj.container == "assets/md/localkoukan/{}.asset".format(checkfile2) or obj.container == "assets/md/mapwarpdata/{}.asset".format(checkfile2) or obj.container == "assets/md/msgwindowdata/{}.asset".format(checkfile2) or obj.container == "assets/md/network/{}.asset".format(checkfile2) or obj.container == "assets/md/placetagdata/{}.asset".format(checkfile2) or obj.container == "assets/md/pokemondata/{}.asset".format(checkfile2) or obj.container == "assets/md/shopdata/{}.asset".format(checkfile2)  or obj.container == "assets/md/stopdata/{}.asset".format(checkfile2) or obj.container == "assets/md/tower/{}.asset".format(checkfile2) or obj.container == "assets/md/tv/{}.asset".format(checkfile2) or obj.container == "assets/md/underground/{}.asset".format(checkfile2):
                tree = obj.read_typetree()
                with open('import/{}'.format(filename), "rt", encoding="utf8") as f:
                    data = json.load(f)
                print('{} updated'.format(checkfile))
                obj.save_typetree(data)
    with open("output/masterdatas", "wb") as t:
        t.write(env.file.save(packer=(64, 2)))


input('Repack complete enter any key to exit')