import logging
import git
import os


"""https://github.com/nautobot/nautobot/blob/develop/nautobot/utilities/git.py"""
"""https://gitpython.readthedocs.io/en/stable/tutorial.html"""

logging.basicConfig(level=logging.DEBUG)

root_dir = os.path.abspath(os.path.dirname(__file__))
repo_dir = os.path.join(root_dir,"my_repo")

def init_repo(repo, *args, **kwargs):
    r = git.Repo.init(repo,*args, **kwargs)
    logging.info("创建仓库 %s 成功"%(repo))
    return r

# bare = False：在仓库目录下新建 `.git` 目录
# bare = True：本来应该在 `.git`` 目录下的文件创建在了仓库根目录下

r = init_repo(repo_dir,bare=True)
print(r.bare)


# file_name = os.path.join(repo_dir,"readme.md")
# open(file_name,'wb').close()

# r.index.add([file_name])
# r.index.commit("first commit")
