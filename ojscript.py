import requests
import logging

#读入文件名
Filename = "data.in"
Codename = 'code.cpp'

Data = {}
try:
    Input_Data = []
    with open(Filename, 'r') as fin:
        Input_Data = fin.readlines()
    T = 0
    for i in Input_Data:
        T += 1
        tmp = i.strip().split(':', 1)
        if (len(tmp) != 2):
            print(Filename + ' : Line '+ str(T) + ': Wrong format')
        else:
            Data[tmp[0].strip().lower()] = tmp[1].strip()
except:
    print("File Error")
    exit(0)

logging.info('Input Successfully')

#目标IP
try:
    TargetAddress = Data['targetaddress']
except:
    print(Filename + ' : TargetAddress is lost')
    exit(0)
if TargetAddress[0:4].lower() == 'http':
    print("Warning: TargetAddress don't need 'http'/'https'")

post_headers = {
    'Host' : TargetAddress,
    'Connection' : 'keep-alive',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

#登录方式
try:
    LoginMode = Data['loginmode']
except:
    LoginMode = 'default'

if LoginMode.lower() == 'default':
    #账号密码登录
    print('LoginMode is default')
    user_data = {}
    try:
        user_data['username'] = Data['username']
    except:
        print(Filename + ' : username is lost')
        exit(0)
    try:
        user_data['password'] = Data['password']
    except:
        print(Filename + ' : password is lost')
        exit(0)
    
    post_res = requests.post(
        url = 'http://' + TargetAddress + '/api/login',
        headers = post_headers ,
        data = user_data
    )
    if post_res.status_code != 200:
        exit("Login ERR")

    post_headers['Cookie'] = post_res.headers['set-cookie']
else:
    if LoginMode.lower() == 'cookie':
        #Cookie登录
        print('LoginMode is Cookie')
        try:
            Cookie = Data['cookie']
        except:
            print(Filename + ' : Cookie is lost')
            exit(0)
        post_headers['Cookie'] = Cookie
    else:
        print('Unknown LoginMode')

logging.info('Login Successfully')

#获取页面
'''
get_headers = {
    'Host' : TargetAddress,
    'Connection' : 'keep-alive',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding' : 'gzip, deflate',
    'Accept-Language' : 'zh-CN,zh;q=0.9'
}
get_headers['Cookie'] = post_res.headers['set-cookie']

get_res = requests.get(
    url = 'http://' + TargetAddress + '/admin/info',
    headers = get_headers
)

if get_res.status_code == 200:
    print('GET Successfully')
    print(get_res.text)
else:
    print('GET ERR')
    print(get_res)
'''

#自动发帖
'''
for i in range(0,1):
    print("----- Case: " + str(i))

    #题目编号
    post_params = {'problem_id' : '1235'}
    #发帖内容
    post_data = {
        'title' : 'test' + str(i),
        'content' : 'tmp' + str(i)
    }
    post_res = requests.post(
        url = 'http://' + TargetAddress + '/article/0/edit',
        headers = post_headers,
        params = post_params,
        data = post_data
    )
    
    print(post_res)
'''

#自动删帖
'''
for i in range(10,17):   #删帖编号
    print("----- Delte: " + str(i))
    
    post_res = requests.post(
        url = 'http://' + TargetAddress + '/article/' + str(i) + '/delete',
        headers = post_headers
    )
    
    print(post_res)
'''

#自动回复
'''
for i in range(1,1+30):
    print("----- Case: " + str(i))

    #题目编号
    comment_id = 22
    #回复内容
    post_data = {
        'comment' : 'orz hkk ×' + str(i)
    }
    post_res = requests.post(
        url = 'http://' + TargetAddress + '/article/' + str(comment_id) + '/comment',
        headers = post_headers,
        data = post_data
    )

    print(post_res)
'''

#自动删回复
'''
for i in range(84,84+30):   #删回复编号
    print("----- Delte: " + str(i))
    
    #题目编号
    comment_id = 22
    post_res = requests.post(
        url = 'http://' + TargetAddress + '/article/' + str(comment_id) + '/comment/' + str(i) + '/delete',
        headers = post_headers
    )
    
    print(post_res)
'''

#自动提交
'''
try:
    with open(Codename, 'rb') as fin:
        codes = fin.read().decode("UTF+8")
    print(codes)
except:
    print("Codefile Error")
    exit(0)

from requests_toolbelt import MultipartEncoder
for i in range(0,1):
    print("----- Case: " + str(i))

    #题目编号
    comment_id = 3
    #比赛编号
    post_params = {'contest_id' : ''}
    #提交代码
    post_data = MultipartEncoder(fields={
        'language': 'cpp11',
        'code': codes
        })
    post_headers['Content-Type'] = post_data.content_type
    post_res = requests.post(
        url = 'http://' + TargetAddress + '/problem/' + str(comment_id) + '/submit',
        headers = post_headers,
        params = post_params,
        data = post_data
    )
    
    print(post_res)
'''