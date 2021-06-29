import unittest
from calc import Calc


class ModuleTest(unittest.TestCase):

    # 在每一个测试用例开始时执行，执行测试用例执行前的初始化工作，如初始化变量，生成测试数据等
    def setUp(self):
        self.cal = Calc(6, 4)

    # 在每一个测试用例结束时执行，执行测试用例的清理工作，如关闭数据库、关闭文件、删除数据等
    def tearDown(self):
        pass

    # 方法必须以 test 开头
    def test_add(self):
        result = self.cal.add()
        self.assertEqual(result, 10)
    
    def test_sub(self):
        result = self.cal.sub()
        self.assertEqual(result, 2)

if __name__ == "__main__":
    # 构建测试类
    suite = unittest.TestSuite()
    suite.addTest(ModuleTest("test_add"))
    suite.addTest(ModuleTest("test_sub"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)