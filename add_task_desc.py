import json
import deb822
import sys

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
    t = list(deb822.Deb822.iter_paragraphs(open('{0}.task'.format(project['name'].lower()))))
    t = dict((str(tt['Depends'].strip()), tt) for tt in t[1:])
    for pkg in l:
        pkg['name'] = unicode(pkg['name'].replace('/', '-').replace('_','-').lower())
        tdesc = t.get(pkg['name'].strip())
        if not tdesc:
            continue
        url= tdesc.get('Homepage')
        if url:
            pkg['url'] = url.strip()
        desc = tdesc.get('Pkg-Description')
        if not desc:
            continue
        pkg['summary'] = desc.splitlines()[0]
        desc = '\n'.join(s[1:] for s in desc.splitlines()[1:])
        if not desc:
            continue
        pkg['description'] = desc
    with open('{0}.json'.format(project['name'].lower()), 'w') as fp:
        json.dump(l, fp, indent=2, sort_keys = True)
        fp.flush()


