import json

ascl = json.load(open('../ascl.json'))
scisoft = json.load(open('scisoft.json'))


def get_ascl(name):
    if "/" in name:
        name = name.split("/")[-1]
    for pkg in ascl.values():
        if pkg.get('name', '') and name.lower() == pkg.get('name', '').lower():
            return pkg

for pkg in scisoft:
    a = get_ascl(pkg.get('name', ''))
    if a is not None:
        print a['name'], a['ascl_id'][6:-1]
        pkg['ascl_id'] = a['ascl_id'][6:-1]

with open('scisoft.json', 'w') as fp:
    json.dump(scisoft, fp, indent=2, sort_keys = True)
    fp.flush()
