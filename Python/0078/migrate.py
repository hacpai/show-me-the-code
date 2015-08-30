#coding:utf-8
import os
import shutil
import re

def movefile( dirname ):
    """Move fileName.md file to YY-MM-DD-file-name.md in a given directory and its subdirectories.
    """
    i = 7
    for root, dirs, file in os.walk( dirname ):
        for f in file:
            if os.path.splitext(root+f)[1] == ".markdown":
                filename = os.path.join(root, f)
                i += 1
                list = re.sub( r"([A-Z])", r" \1", f).split()
                f = '-'.join(list).lower()
                # os.system("cp '%s' ~/file/2014-09-%02d-%s"%(os.path.join( root, f ), i, f))
                shutil.copyfile(filename, os.path.expanduser("~/file/2015-01-%02d-%s"%(i,f)))

def addtext(dirname):
    """Add text to *.md
    """
    for root, dirs, file in os.walk(dirname):
        for f in file:
            filename = os.path.join(root, f)
            with open(filename, 'r') as original:
                line = original.readline()
                original.readline()
                data = original.read()
            with open(filename, 'w') as modified:
                modified.write('---\n' + 'layout: post\n' +
                               'title: %s'%line +
                               'category: JavaScript\n' +
                               'tags: JavaScript\n' +
                               'description: \n' +
                               '---\n' + data)

movefile('.')
addtext('.')
