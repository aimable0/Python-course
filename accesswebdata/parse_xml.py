import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Aimable Nkurikiyimana</name>
    <phone type="intl">+250 791 275 915</phone>
    <residence>Kigali</residence>
    <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('phone:', tree.find('phone').text)
print('email:', tree.find('email').get('hide'))