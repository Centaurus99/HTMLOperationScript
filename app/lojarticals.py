import requests

#目标IP
Target_address = '192.168.21.187:2233'

#账号密码
user_data = {'username' : '******', 'password' : '******'}

post_headers = {
    'Host' : Target_address,
    'Connection' : 'keep-alive',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

post_res = requests.post(
    url = 'http://' + Target_address + '/api/login',
    headers = post_headers ,
    data = user_data
)
if post_res.status_code != 200:
    exit("Login ERR")


post_headers['Cookie'] = post_res.headers['set-cookie']


#获取页面
'''
get_headers = {
    'Host' : Target_address,
    'Connection' : 'keep-alive',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding' : 'gzip, deflate',
    'Accept-Language' : 'zh-CN,zh;q=0.9'
}
get_headers['Cookie'] = post_res.headers['set-cookie']

get_res = requests.get(
    url = 'http://' + Target_address + '/admin/info',
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
        url = 'http://' + Target_address + '/article/0/edit',
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
        url = 'http://' + Target_address + '/article/' + str(i) + '/delete',
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
        url = 'http://' + Target_address + '/article/' + str(comment_id) + '/comment',
        headers = post_headers,
        data = post_data
    )

    print(post_res)
'''

#自动删回复

for i in range(84,84+30):   #删回复编号
    print("----- Delte: " + str(i))
    
    #题目编号
    comment_id = 22
    post_res = requests.post(
        url = 'http://' + Target_address + '/article/' + str(comment_id) + '/comment/' + str(i) + '/delete',
        headers = post_headers
    )
    
    print(post_res)
