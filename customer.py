#!/usr/bin/env python
import yaml

schema = yaml.load(open('customer2.sch').read())
seqmap = {}
for i,field in enumerate(schema['fields']):
   name = field['name']
   seqmap[name] = i

print "Delimiter is: %s" % schema['record']['delimiter']
print seqmap
#field  As a test to confirm the schema matches the file
#print the name and address with headers
for line in open('customer.dat'):
   line = line.rstrip()
   data = line.split(schema['record']['delimiter'])
   record = {}
   for key in seqmap.keys():
      record[key] = data[seqmap[key]]
   
   #do a transformation
   email = record['first_nm'] + '.' + record['last_nm'] + '@mars.com'
   #print data[seqmap['first_nm']],data[seqmap['last_nm']],data[seqmap['address']]
   print record['first_nm'],record['last_nm'],record['address'],email



