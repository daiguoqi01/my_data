import pytest
data=[]
class Test_data1():
    def test1(self):
        '''New_test1第一条用例'''
        print("New_test1第一条用例")
        data.append("New_test1第一条用例")

    def test2(self):
        '''New_test1第二条用例'''
        print("New_test1第二条用例")
        data.append("New_test1第二条用例")


    def test3(self):
        '''New_test1第三条用例'''
        print("New_test1第三条用例")
        data.append("New_test1第三条用例")


#pytest --report=musen.html --title=测试报告 --tester=木森 --desc=项目描述  --template=2

