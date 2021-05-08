import difflib

def read_file(file_name):
    with open(file_name,'r') as f:
        return f.readlines()

def config_diff(file_name,file1,file2):
    hd = difflib.HtmlDiff()
    s1 = read_file(file1)
    s2 = read_file(file2)
    with open(file_name + '.html', 'a+') as f:
        f.write(hd.make_file(s1,s2))
    return "OK!"


config_diff('test','cur.cfg','startup.cfg')