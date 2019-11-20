import json
import os

configPath = './config.json'

def saveConfig(config):
    fp = open(configPath, 'w') # 覆盖的方式
    fp.write(json.dumps(config))
    fp.close()
def readConfig():
    if not os.path.isfile(configPath):
        return False
    fp = open(configPath, 'r')
    return json.loads(fp.read())

def main():
    config = readConfig()
    if config == False:
        print("请先录入用户名密码：")
        name = input('Name:')
        password = input("Password:")
        saveConfig({'name': name, 'password': password})
        print("用户信息录入成功，请重新启动程序登陆")
    else:
        print('请输入用户名密码：')
        name = input('Name:')
        password = input('Password:')
        if config['name'] == name and config['password'] == password:
            print("登陆成功")
        else:
            print("登陆失败，用户名或密码不匹配")
        
main()
