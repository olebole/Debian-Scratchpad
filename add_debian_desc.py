import json
import apt
pkgs = dict()
apt_cache = apt.Cache()
for pkg in apt_cache:
    pkgs.setdefault(pkg.versions[0].source_name, []).append(pkg.name)


projects = [
    {
        'name': 'FedoraAstro',
        'url': 'https://fedoraproject.org/wiki/Astronomy_Spin',
    },
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
        debian_name = pkg.get('debian')
        if not debian_name:
            debian_name = pkg.get('name')
        p = apt_cache.get(debian_name)
        if not p:
            continue
        pkg['debian'] = debian_name
        print(debian_name)
        pkg['description'] = p.versions[0].description
        if 'summary' not in pkg:
            pkg['summary'] = p.versions[0].summary
        if 'url' not in pkg:
            pkg['url'] = p.versions[0].homepage
    with open('{0}.json'.format(project['name'].lower()), 'w') as fp:
        json.dump(l, fp, indent=2, sort_keys = True)
        fp.flush()


