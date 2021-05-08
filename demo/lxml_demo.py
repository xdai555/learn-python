from lxml import etree

## Element 类

# 创建一个元素（初始化类）
root = etree.Element("ROOT")
print(root.tag)     # ROOT

# 使用 append() 方法添加子元素
root.append(etree.Element("child1"))
# 使用 SubElement 方式添加子元素，需要将父元素传入
child2 = etree.SubElement(root,"child2")
child3 = etree.SubElement(root,"child3")


# 使用 tostring 方法查看创建的 xml，这里注意输出的是二进制
print(etree.tostring(root))     # b'<ROOT><child1/><child2/><child3/></ROOT>'
print(type(root))               # <class 'lxml.etree._Element'>

## Element 类可以作为列表来操作
print(len(root))    # 3
for i in root:
    print(i.tag)    # child1 child2 child3

## Element 类可以使用字典来携带属性
root = etree.Element("ROOT",test1="18",test2="test2")
print(etree.tostring(root))     # b'<ROOT test1="18" test2="test2"/>'
# 获取属性的值
print(root.get("test1"))        # 18
# 取所有属性、所有值，返回值都是列表
print(root.keys(),root.values())    # ['test1', 'test2'] ['18', 'test2']

## 给 Element 写入值
root.text = "TEXT"
print(root.text)                # TEXT
print(etree.tostring(root))     # b'<ROOT test1="18" test2="test2">TEXT</ROOT>'

# 使用 Tree 迭代来添加元素并赋值
root = etree.Element("root")    
etree.SubElement(root, "child").text = "Child 1"
etree.SubElement(root, "child").text = "Child 2"
etree.SubElement(root, "another").text = "Child 3"

## 使用 XPATH 来查找值
# [w3school XPATH 语法](https://www.w3school.com.cn/xpath/xpath_syntax.asp)
print(root.xpath("string()"))   # # Child 1Child 2Child 3
print(root.xpath("//text()"))   # ['Child 1', 'Child 2', 'Child 3']

## 序列化
# 可以把字符串转换为 Element 对象
xml = """<top>
<Ifmgr>
<Interfaces>
<Interface>
<Name></Name>
<AdminStatus></AdminStatus>
</Interface>
</Interfaces>
</Ifmgr>
</top>"""
# 第一种方法
data = etree.XML(xml)
print(type(data))       # <class 'lxml.etree._Element'>
# 第二种方法
data = etree.fromstring(xml)
print(type(data))

## Namaspaces（命名空间）
# 在 XML 中，元素名称是由开发者定义的，当两个不同的文档使用相同的元素名时，就会发生命名冲突。
# [w3school 命名空间](https://www.w3school.com.cn/xml/xml_namespaces.asp)


# 定义一个 top 的 Element，它属于私有命名空间
root = etree.Element("{http://www.h3c.com/netconf/data:1.0}top")
print(etree.tostring(root))     # b'<ns0:top xmlns:ns0="http://www.h3c.com/netconf/data:1.0"/>'
# 为了保证属于同一个命名空间，每次添加子元素时，都要写上命名空间的前缀，否则就会不识别，但是这种方式很繁琐且低效
Ifmgr = etree.SubElement(root, "{http://www.h3c.com/netconf/data:1.0}Ifmgr")
Ifmgr.text = "G0/0"
print(etree.tostring(root))     # b'<ns0:top xmlns:ns0="http://www.h3c.com/netconf/data:1.0"><ns0:Ifmgr>G0/0</ns0:Ifmgr></ns0:top>'

# 使用 Element 工厂函数定义默认的命名空间
H3C_DATA_1_0 = "http://www.h3c.com/netconf/data:1.0"
FULL_NS = "{%s}" %H3C_DATA_1_0
# 定义了默认的命名空间后，子元素里面可以不显示前缀（None）
root = etree.Element(FULL_NS + "top", nsmap={None:H3C_DATA_1_0})
Ifmgr = etree.SubElement(root, "Ifmgr")
Ifmgr.text = "G0/0"
# 这样定义后，显示结果就很清爽
print(etree.tostring(root))     # b'<top xmlns="http://www.h3c.com/netconf/data:1.0"><Ifmgr>G0/0</Ifmgr></top>'

## 使用 E-factory 替代 Element 和 SubElement 来快速生成 xml 
from lxml.builder import ElementMaker
# 设置默认命名空间
E = ElementMaker(namespace=H3C_DATA_1_0,nsmap={None:H3C_DATA_1_0})
# 通过嵌套方式来快速生成 XML
top = E.top(
    E.Ifmgr(
        E.Interfaces(
            E.Interface()
        )
    )
)
print(etree.tostring(top))  # b'<top xmlns="http://www.h3c.com/netconf/data:1.0"><Ifmgr><Interfaces><Interface/></Interfaces></Ifmgr></top>'


"""ElementPath提供的四种查找方法
find()      # 返回第一个匹配项，未找到则返回 None
findtext()  # 返回第一个匹配项的 text
findall()   # 返回所有匹配项列表
iterfind()  # 返回所有匹配项的迭代器
"""

ret_no_ns = """<?xml version="1.0" encoding="UTF-8"?>
<rpc-reply>
<data>
<top>
<Ifmgr>
<Interfaces>
<Interface><IfIndex>1</IfIndex><Name>GigabitEthernet0/0</Name><AdminStatus>1</AdminStatus></Interface>
<Interface><IfIndex>2</IfIndex><Name>GigabitEthernet0/1</Name><AdminStatus>1</AdminStatus></Interface>
<Interface><IfIndex>129</IfIndex><Name>NULL0</Name><AdminStatus>1</AdminStatus></Interface>
<Interface><IfIndex>130</IfIndex><Name>InLoopBack0</Name><AdminStatus>1</AdminStatus></Interface>
</Interfaces></Ifmgr></top></data></rpc-reply>"""
ret = etree.XML(ret_no_ns.encode())

# 只能查找子元素
print(ret.find("data"))         # <Element data at 0x7efcee610680>
print(ret.find("data").tag)     # data
# 在任意位置查找元素，并取 tag
print(ret.find(".//Name").tag) # Name
# 在任意位置查找元素并取 text，两种方法相同
print(ret.findtext(".//Name"))  # GigabitEthernet0/0
print(ret.find(".//Name").text) # GigabitEthernet0/0
# 返回所有匹配项，列表
print(ret.findall(".//Name"))   # [<Element Name at 0x7f6cd2d1c900>,..., <Element Name at 0x7f6cd2d1ca00>]
# 返回所有匹配项，迭代器
print(type(ret.iterfind("../Name")))    # <class 'generator'>

# 实际返回内容中带有命名空间
ret = """<?xml version="1.0" encoding="UTF-8"?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:c94f3285-d747-4e19-abd3-efbe281e3133">
<data>
<top xmlns="http://www.h3c.com/netconf/data:1.0">
<Ifmgr>
<Interfaces>
<Interface><IfIndex>1</IfIndex><Name>GigabitEthernet0/0</Name><AdminStatus>1</AdminStatus></Interface>
<Interface><IfIndex>2</IfIndex><Name>GigabitEthernet0/1</Name><AdminStatus>1</AdminStatus></Interface>
<Interface><IfIndex>129</IfIndex><Name>NULL0</Name><AdminStatus>1</AdminStatus></Interface>
<Interface><IfIndex>130</IfIndex><Name>InLoopBack0</Name><AdminStatus>1</AdminStatus></Interface>
</Interfaces></Ifmgr></top></data></rpc-reply>"""
ret = etree.fromstring(ret.encode())
# 查找带有命名空间的所有元素
data = ret.findall('.//{http://www.h3c.com/netconf/data:1.0}Name')
IfList = [i.text for i in data]
print(IfList)       # ['GigabitEthernet0/0', 'GigabitEthernet0/1', 'NULL0', 'InLoopBack0']
# ======================