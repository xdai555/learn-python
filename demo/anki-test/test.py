import re

p_question = re.compile('^([单多]选|判断)题')
p_options = re.compile('^（(正确|错误)）')
p_remark = re.compile('^解析')


def get_content_list(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.readlines()
    result = []
    start_num = 0
    for index,line in enumerate(content):
        line = line.strip()
        if not re.match(p_question,line) is None:
            if index != 0:
                p = content[start_num:index]
                start_num = index
                result.append(p)
    return result

p = ['单选题：阿里云的云盾会检查通过公共互联网登录云服务器 ECS 的来源 IP,登录方式包括\n',
 'SSH 和远程桌面,当来自某 个 IP 的登录请求出现多次密码错误的情况时,会发出"ECS 遭遇\n',
  '密码暴力破解"的报警,当收到这个报警后,最安全的处理方法应该是 。\n', 
  '（错误）通知自己业务平台的所有用户立即修改密码,并通过技术手段杜绝简单密码\n', 
  '（正确）这个报警无关紧要,可以忽略\n', 
  '（正确）立即更新云服务器 ECS 实例的系统用户的密码,并启用安全组防火墙,只允许特定\n', 
  'IP 连接 ECS 实例\n', 
  '（错误）立即登录云服务器 ECS 实例,检查登录日志,如果没有异常登录成功的记录,可直接\n', 
  '忽略\n', 
  '解析：当某个 IP 的尝试多次登录云服务器 ECS 的时候,为了防止密码被破解,建议立即修改\n', 
  '云服务器ECS的密 码,并启动安全组防火墙,只允许特定 IP 登录该 ECS。\n']



def format_question(content):
    optionsIndexList = []
    remarkStartIndex = 0
    for index, line  in enumerate(content):
        line = line.strip()
        if re.match(p_options,line):
            optionsIndexList.append(index)
            continue
        if re.match(p_remark,line):
            remarkStartIndex = index
            continue
    # q = content[0:optionsIndexList[0]]
    # print(optionsIndexList)
    # o = content[optionsIndexList[0]:remarkStartIndex]
    # r = content[remarkStartIndex:]
    # q_str = format_list(q) + r'{{c1:: }}'
    # o_str = format_list(o,option=True) 
    # r_str = format_list(r)
    # print(o)
    # return (q_str, o_str, r_str)
    return format_option(content,optionsIndexList,remarkStartIndex)

def format_list(lis,option=False):
    res = ''
    if not option:
        for i in lis:
            res += i.strip()
    else:
        for i in lis:
            res += i.strip() + r'<br>'
    return res



def format_option(content, index_list,remark):
    o = []
    start_num = 0
    for i in index_list:
        if i != 0:
            o.append(format_list(content[start_num:i]))
        start_num = i
    o.append(format_list(content[start_num:remark]))
    o.append(format_list(content[remark:]))
    return o


def format_answer(content):
    answerMap = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
    }
    answer = ''
    question = content.pop(0)
    remark = content.pop(-1)
    for index,i in enumerate(content):
        content[index] = i.replace('（错误）', '')
        if i.startswith("（正确）"):
            content[index] = i.replace('（正确）', '')
            try:
                answer += answerMap[index]
            except:
                print(content)
    return question + r'{{c1:: }}' + '$' + format_list(content,option=True) + '$' + remark + '$' + answer + '\n'

if __name__ == '__main__':
    # 单 913
    # 多 422
    # 判 47
    # 总 1382
    # 读取全部题目，将每道题目切割为单个列表
    ret = get_content_list('./test.txt')
    # 格式化问题，返回带有答案的标准anki模板
    f = open('./result.txt','a+', encoding='utf-8')
    for i in ret:
        ret = format_answer(format_question(i))
        f.write(ret)
    f.close()


# # 去重
# a = {}
# with open('./result.txt', 'r', encoding='utf-8') as f:
#     for i in f.readlines():
#         a[i.strip().strip().split('$')[0].strip()]=i.strip()
# b = [v for v in a.values()]


# with open('./final.txt','w',encoding='utf-8') as f:
#     for i in b:
#         f.write(i + '\n')
