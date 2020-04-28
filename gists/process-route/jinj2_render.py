from jinja2 import FileSystemLoader,Environment
import yaml
from pprint import pprint

def ipaddr(ipaddress,operation):
    from ipaddress import IPv4Interface
    ipadd = IPv4Interface(ipaddress)
    attr = getattr(ipadd,operation)
    return attr

jinja_loader = FileSystemLoader('./')
env = Environment(loader=jinja_loader)
env.filters['ipaddr'] = ipaddr
jinja_template = env.get_template('route.j2')
# print(jinja_template)



with open('route.yml') as f:
    a = yaml.safe_load(f.read())
    # print(a)

out = jinja_template.render(a)
with open("a.txt",'a') as f:
    f.write(out)
