import requests, time, re, json, base64, argparse

# server酱开关，填0不开启(默认)，填2同时开启cookie失效通知和签到成功通知
sever = '2'
# 填写server酱sckey,不开启server酱则不用填（自己更改）
sckey = 'SCU165126T3959f4bb3d109dd3305ac0347ede2593604db146cfab8'
# 填入glados账号对应cookie
cookie = '__cfduid=d10b654915a2bad2c95cb9bebab7f104e1615700177; _ga=GA1.2.564923222.1615700183; _gid=GA1.2.1252373224.1615700183; koa:sess=eyJ1c2VySWQiOjc0NTY3LCJfZXhwaXJlIjoxNjQxNjIwNDkxNDA4LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=CQ9iYBYKFEkJI2AqWERVs_9Vhuo; _gat_gtag_UA_104464600_2=1'
referer = 'https://glados.rocks/console/checkin'

def start():
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
   # print(res)

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        #print(time)
        if sever == '2':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+',you have '+time+' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')

def main_handler(event, context):
  return start()

if __name__ == '__main__':
  start()
