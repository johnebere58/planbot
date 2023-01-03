import re

# Companies in europe reports their financial 
# numbers of semi annual basis and you can have 
# a document like this. To exatract quarterly 
# and semin annual period you can use a regex as 
# shown below

text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S4 was $8 billion.
'''

pattern = '([\w]*)\'s gross cost'
pattern2 = '[Q|S][1-4] was \$[\d.\d |\d ]* billion'

matches = re.findall(pattern2, text)

print(matches)
