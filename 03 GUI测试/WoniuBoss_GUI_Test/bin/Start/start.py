import unittest
from WoniuBoss_GUI_Test.tools.util import Util

class start:

    @classmethod
    def start(cls):
        from HTMLTestRunner import HTMLTestRunner
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        # 通过加载器对象来加载测试类。参数name需要提供测试类的类全名（从根目录开始的路径）
        tests1 = loader.loadTestsFromNames(Util.get_path("..\\..\\conf\\test"))
        suite.addTest(tests1)
        with open(f"..\\..\\report\\test{Util.get_ctime()}.html", "w", encoding="utf8") as op:
            runner = HTMLTestRunner(stream=op, verbosity=2)
            runner.run(suite)

if __name__ == '__main__':
    start.start()