import xml.etree.ElementTree as ET

data = '''
<person>
    <contact>
        <name>Aimable Nkurikiyimana</name>
        <phone type="intl">+250 791 275 915</phone>
        <residence>Kigali</residence>
        <email hide="yes" />
    </contact>
</person>'''
print(type(data))
tree = ET.fromstring(data)
print(type(tree))

contact_instances = tree.findall("contact")
print(len(contact_instances))

print(contact_instances)

for contact in contact_instances:
    print('Name:', contact.find('name').text)
    print('phone:', contact.find('phone').text)
    print('residence:', contact.find('residence').text)
    print('email:', contact.find('email').get('hide'))