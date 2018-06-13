import yaml

my_list = []
my_list = [{'device':'juniper','IP_addr':'192.168.2.1'},{'IP_addr':'192.168.1.1','device':'cisco'},range(2)]
print(my_list)
print(my_list[0]['device'])

yaml_my_list = yaml.dump(my_list, default_flow_style=True)

print(yaml_my_list)

