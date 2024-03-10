# @本代码由文心一言生成，由JL选型和修改优化

def login():  
    # 创建一个字典来存储用户名和密码  
    users = {  
        "user1": "password1",  
        "user2": "password2",  
        "user3": "password3", 
        "zhangsan": "123456",
        #“lisi”：“654321”，
        # 可以添加更多用户
        # 如增加zhangsan用户密码为123456请参考本代码的第9行进行添加
        # 如需删除用户，请参考本代码的第10行，删除或注释对应的用户
    }  
  
    # 获取用户输入的用户名和密码  
    username = input("请输入用户名: ")  
    password = input("请输入密码: ")  
  
    # 检查用户名和密码是否匹配  
    if username in users and users[username] == password:  
        print("登录成功!")  
    else:  
        print("用户名或密码错误，请重试.")  
  
# 调用登录函数  
login()
