import json

ascl = json.load(open('../ascl.json'))

projects = [
    {
        'name': 'AstroConda',
        'url': 'http://astroconda.github.io',
    },
    {
        'name': 'SciSoft',
        'url': 'http://www.eso.org/sci/software/scisoft',
    }
]

for project in projects:
    l = json.load(open('{0}.json'.format(project['name'].lower())))
    for pkg in l:
        pkg['name'] = pkg['name'].replace('/', '-').replace('_','-').lower()
        ascl_id = pkg.get('ascl_id')
        if not ascl_id:
            continue
        if 'description' in pkg:
            continue
        ascl_p = ascl.get(ascl_id)
        if not ascl_p:
            continue
        print ascl_id
        pkg['description'] = ascl_p['abstract']
    with open('{0}.json'.format(project['name'].lower()), 'w') as fp:
        json.dump(l, fp, indent=2, sort_keys = True)
        fp.flush()


