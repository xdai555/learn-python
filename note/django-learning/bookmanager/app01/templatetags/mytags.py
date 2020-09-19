from django import template

register = template.Library()


# 第一个参数为 value，最多支持额外一个参数 {{ value | arg }}
@register.filter
def add_arg(value, arg):
    # 功能
    return f"{value}_{arg}"


@register.inclusion_tag('dropdown.html')
def sqr_list(num):
    return {'data': [[i, f'{i}的平方是{i ** 2}'] for i in range(1, num + 1)]}
