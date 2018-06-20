import pprint
import yaml
import json
from ciscoconfparse import CiscoConfParse

my_list = []
my_list = [{'device':'juniper','IP_addr':'192.168.2.1'},{'IP_addr':'192.168.1.1','device':'cisco'},range(2)]
print(my_list)
print(my_list[0]['device'])

print ("***********************************************")
print("********************YAML**********************")
print ("***********************************************")

yaml_my_list = yaml.dump(my_list, default_flow_style=True)

print(yaml_my_list)

yaml_my_list = yaml.dump(my_list, default_flow_style=False)

print(yaml_my_list)

with open("some_file.yml", "w") as f:
  f.write(yaml.dump(my_list, default_flow_style=False))

with open("yml_file.yml") as f:
  new_list = yaml.load(f)
  print(new_list)
  pprint.pprint(new_list)

print ("***********************************************")
print ("************************JSON**************************")
print ("***********************************************")

json_my_list = json.dumps(my_list)

print(json_my_list)

with open("json_file.json", "w") as f:
  json.dump(my_list, f)

with open("json_file.json") as f:
  json_new_list = json.load(f)
pprint.pprint(json_new_list)

print("************************************************************")
print("********************ciscoconfparse**********************")
print("************************************************************")

Config_File = CiscoConfParse("lesson1_ConfigFile.txt")

print("=== crypto map with pfs group2 =====")
crypto_w_pfs_group2 = Config_File.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")
print(crypto_w_pfs_group2)

for parent in crypto_w_pfs_group2:
  print parent.text
  for child in parent.children:
    print child.text

print("=== crypto map without aes =====")

crypto_w_pfs_group2 = Config_File.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"set transform-set AES")

for parent in crypto_w_pfs_group2: 
  print parent.text
  for child in parent.children:
    print child.text

