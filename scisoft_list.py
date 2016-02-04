import json

fp = open('README.md', 'w')

fp.write('''Scisoft programs for potential inclusion in Debian
===================================================


The list is taken from the [Scisoft-8.0](http://www.eso.org/sci/software/scisoft/Scisoft-contents.html)
package list. Packages that are already in Debian are in **bold**, packages
that will (for various reasons) not go into Debian are in *italic*. The other
may be packaging candidates.


| Package              | Description |
| -------------------- | ----------- |
''')

l = json.load(open('scisoft.json'))
for pkg in l:
    pkg.setdefault('description', '')
    s = '| '
    if 'debian' in pkg:
        s += '[**{name}**](https://packages.debian.org/sid/{debian})'
    else:
        if 'url' in pkg:
            s += '['
        if not pkg.get('packageable', False):
            s += '*{name}*'
        else:
            s += '{name}'
        if 'url' in pkg:
            s += ']({url})'
    s += ' | {description} |\n'
    fp.write(s.format(**pkg))

fp.close
