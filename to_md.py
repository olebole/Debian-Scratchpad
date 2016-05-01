import json

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
    project['lname'] = project['name'].lower()
    fp = open('{name}.md'.format(**project), 'w')

    fp.write('''{name} programs for potential inclusion in Debian
===================================================


The list is taken from the
[{name}]({url})
package list. Packages that are already in Debian are in **bold**, packages
that will (for various reasons) not go into Debian are in *italic*. The other
may be packaging candidates.


| Package              | Description |
| -------------------- | ----------- |
'''.format(**project))

    l = json.load(open('{lname}.json'.format(**project)))
    section = None
    for pkg in l:
        pkg.setdefault('summary', '')
        if pkg['section'] != section:
            fp.write('| | |\n| | **{section}** |\n'.format(**pkg))
            section = pkg['section']
        s = '| '
        if 'debian' in pkg:
            s += '[**{name}**](https://packages.debian.org/sid/{debian})'
        else:
            if 'url' in pkg:
                s += '['
            if not pkg.get('packageable', True):
                s += '*{name}*'
            else:
                s += '{name}'
            if 'url' in pkg:
                s += ']({url})'
        s += ' | {summary} '
        if not pkg.get('packageable', True) and 'comment' in pkg:
            s += '(*{comment}*) '
        s += '|\n'
        fp.write(s.format(**pkg))

    fp.close
