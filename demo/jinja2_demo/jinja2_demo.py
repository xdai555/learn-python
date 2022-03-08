# from jinja2 import Template
# tmpl = Template('hello {{ name}}')
# result = tmpl.render(name = '111')
# print(result)


from jinja2 import Template, FileSystemLoader, Environment

j2_loader = FileSystemLoader('./')

env = Environment(loader=j2_loader)

# j2_tmpl = env.get_template('./jinja2_for.j2')
# j2_tmpl = env.get_template('./jinja2_if.j2')
# j2_tmpl = env.get_template('./jinja2_filter.j2')
j2_tmpl = env.get_template('./range_test.j2')

names = ['Zhang San', 'Li Si', 'Wang Wu']

people = [
    {'name':'Zhang San', 'age': 18},
    {'name':'Li Si', 'age': 20},
    {'name':'Wang Wu', 'age': 22},
]

# result = j2_tmpl.render(names=names)
# result = j2_tmpl.render(people=people)



# import yaml
# with open('l2_interfaces.yaml') as f:
#     vars = yaml.safe_load(f.read())
# print(vars)
result = j2_tmpl.render()
print(result)