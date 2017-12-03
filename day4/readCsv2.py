# 1.之前的csv文件不能被其他testcase调用，所以应该给这段代码封装到一个方法里
# 2.每个testcase路径不同，所以path应该作为参数传到这个方法中
#
# 4.打开了一个文件，但是并没有关闭，造成内存泄露
import csv
import os

def read(file_name):
    # 所有重复代码的出现都是程序设计的不合理
    # 重复的代码应该封装到一个方法里
    current_file_path = os.path.dirname(__file__)
    path = current_file_path.replace("day4", "data/" + file_name)
    # file = open(path, "r")
    # with语句是一个代码块，代码块中的内容都有缩进四个空格
    # with代码块可以自动关闭with中声明的变量file
    # 因为file文件一旦被关闭，里面的数据也随着消失
    # 所以单独声明一个列表result，来保存里面的数据
    result = []
    with open(path, "r") as file :
        data_table = csv.reader(file)
        for row in data_table:
            result.append(row)
    return result

    # 如果在打开程序和关闭程序的代码中间，发生了异常情况导致后面代码不能正常运行
    # file.close()也不执行，这时，文件依然不能关闭
    # 应该用with...as..语句实现文件的关闭


if __name__ == '__main__':
    # path = r"C:\Users\51Testing\PycharmProjects\weekend\data\member_info.csv"
    # 这个路径是一个绝对路径，我们工作中，一个项目不只一个人编写代码
    # 我们无法统一要求大家都把项目代码放在一个路径下，因为有的人放在d盘
    # 这个文件因为在项目中，它的路径也会随着项目变化
    # 所以应该在代码中，通过当前代码文件的路径，根据相对位置，自动找到项目路径
    # 所以首先要找到当前文件的路径
    # os是操作系统
    # __file__ python内置变量，指的是当前文件
    current_file_path = os.path.dirname(__file__)
    # print(current_file_path)
    # 我们真正想要的路径
    # path = current_file_path.replace("day4",r"data/member_info.csv")
    # print(path)
    # read(path)
    member_info = read("goods_info.csv")
    # print(member_info)
    for row in member_info:
        print(row)
# 5.读出数据不是目的，目的是通过驱动测试，所以应该把数据作为方法的返回值，方便进一步调用
