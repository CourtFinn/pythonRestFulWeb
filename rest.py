#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET

tree = ET.parse('users.xml')
root = tree.getroot()

urls = (
    '/users', 'list_users',
    '/users/(.*)', 'get_user',
    '/add', 'add_user'
)

app = web.application(urls, globals())

class list_users:
    def GET(self):
        output = 'users:['
        for child in root:
            print 'child', child.tag, child.attrib
            output += str(child.attrib) + ','
        output += ']'
        return output

class get_user:
    def GET(self, user):
        for child in root:
            if child.attrib['id'] == user:
                return str(child.attrib)

class add_user:
    def POST(self):
        i = web.input()
        textToSeach = "</users>"
        textToReplace = str(i) + "\n</users>"
        try:
            f = open('users.xml', mode='a')
            f.write(str(i))
            for line in f:
                if textToSeach in line:
                    f.write(line.replace(textToSeach, textToReplace))
            f.close()
            return "accepted"
        except Exception as e:
            return 'error occurred %s', e

if __name__ == "__main__":
    app.run()
