# 定义一个名为add_的函数，用于向得分文件中添加一个数字
def add_(num):
    # 打开得分文件，读取当前得分
    score_file = open("score.afscore", "r")
    score = score_file.read()
    score_file.close()
    # 以写入模式打开得分文件，将当前得分加上输入的数字后写回文件
    score_file = open("score.afscore", "w")
    score_file.write(str(int(score) + num))
    score_file.close()

# 定义一个名为get_的函数，用于从得分文件中获取当前得分
def get_():
    # 打开得分文件，读取当前得分并返回
    score_file = open("score.afscore", "r")
    score = score_file.read()
    return score