import unittest


if __name__ == '__main__':
    # 默认的测试用例加载器，用于寻找符合规则的测试用例
    # discover 发现
    suite = unittest.defaultTestLoader.discover('./day5', pattern='*Test.py')
    # 执行suite中的所以测试用例
    # TextTestRunner 文本的 测试用例运行器
    # TextTestRunner首字母大写是一个类，类不能直接调用方法
    # 必须要实例化对象才能调用方法。
    # python中实例化不需要太new关键字，在类后面加上（）
    unittest.TextTestRunner().run(suite)


