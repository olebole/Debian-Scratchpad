import json

import apt

projects = [
    {
        'name': 'AstroConda',
        'url': 'http://astroconda.readthedocs.io',
    },
    {
        'name': 'SciSoft',
        'url': 'http://www.eso.org/sci/software/scisoft',
    }
]
    
pkgs = dict()
apt_cache = apt.Cache()
for pkg in apt_cache:
    pkgs.setdefault(pkg.versions[0].source_name, []).append(pkg.name)

for project in projects:
    project['lname'] = project['name'].lower()

    l = json.load(open('{lname}.json'.format(**project)))

    with open('{lname}.task'.format(**project), 'w') as fp:
        fp.write('''Task: {name}
Install: false
Index: false
Metapackage: false
Description: {name} packages
 Here we list the packages that belong to the 
 [{name}]({url})
 distribution.
'''.format(**project)) 
        for pkg in l:
            pkg['name'] = pkg['name'].replace('/', '-').replace('_','-').lower()
            if 'description' in pkg:
                pkg['description'] = '\n '.join(pkg['description'].splitlines())
            s = '\n'
            if 'debian' in pkg:
                if pkg['debian'] in apt_cache:
                    s += "Depends: {debian}\n"
                else:
                    try:
                        s += "Depends: {debianpkgs}\n".format(debianpkgs = ", ".join(pkgs[pkg['debian']]))
                    except:
                        s += "Depends: {debian}\n"
            else:
                s += "Depends: {name}\n"
                if 'url' in pkg:
                    s += "Homepage: {url}\n"
                if 'summary' in pkg:
                    s += 'Pkg-Description: {summary}\n'
                    if 'description' in pkg:
                        s += ' {description}\n'
                if 'comment' in pkg:
                    s += 'Remark:\n {comment}\n'
            fp.write(s.format(**pkg))

