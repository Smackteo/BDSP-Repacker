import os
import UnityPy
import json

#Smackteo's BDSP repacker
#2.0

src = "Resources/personal_masterdatas"

directory = r'import'
env = UnityPy.load(src)

for filename in os.listdir(directory):
    checkfile = os.path.splitext(filename)[0]
    checkfile=checkfile.lower()
    for obj in env.objects:
        if obj.container == "assets/pml/data/{}.asset".format(checkfile):
            tree = obj.read_typetree()
            with open('import/{}.json'.format(checkfile), "rt", encoding="utf8") as f:
                data = json.load(f)
            print('{} updated'.format(checkfile))
            obj.save_typetree(data)


with open("output/personal_masterdatas", "wb") as t:
    t.write(env.file.save(packer=(64, 2)))

input('Repack complete enter any key to exit')