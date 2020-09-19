#author  by:https://www.cnblogs.com/Cl0ud/p/13324781.html
import json
import ssl
import urllib.request
import os
import time


ssl._create_default_https_context = ssl._create_unverified_context

# os.environ['http_proxy'] = 'http://127.0.0.1:8080'
# os.environ['https_proxy'] = 'https://127.0.0.1:8080'

IP = '' #ip
API_KEY = ''#key

'''
    create_target函数
    功能:
        AWVS13
        新增任务接口
    Method : POST
    URL : /api/v1/targets
    发送参数:
        发送参数     类型     说明
        address     string   目标网址:需要http或https开头
        criticality int      危险程度;范围:[30,20,10,0];默认为10
        description string   备注
'''


def create_target(address, description, int_criticality):
    url = 'https://' + IP + ':13443/api/v1/targets'
    print(url)
    headers = {"X-Auth": API_KEY, "content-type": "application/json", 'User-Agent': 'curl/7.53.1'}
    values = {
        'address': address,
        'description': description,
        'criticality': int_criticality,
    }
    data = bytes(json.dumps(values), 'utf-8')
    request = urllib.request.Request(url, data, headers)
    html = urllib.request.urlopen(request).read().decode('utf-8')
    return html


def get_target_list():
    url = 'https://' + IP + ':13443/api/v1/targets'
    headers = {"X-Auth": API_KEY, "content-type": "application/json", 'User-Agent': 'curl/7.53.1'}
    request = urllib.request.Request(url=url, headers=headers)
    html = urllib.request.urlopen(request).read().decode('utf-8')
    return html


def profiles_list():
    url = 'https://' + IP + ':13443/api/v1/scanning_profiles'
    headers = {"X-Auth": API_KEY, "content-type": "application/json", 'User-Agent': 'curl/7.53.1'}
    request = urllib.request.Request(url=url, headers=headers)
    html = urllib.request.urlopen(request).read().decode('utf-8')
    return html


'''
    start_target
    功能:
        AWVS13
        启动扫描任务接口
    Method : POST
    URL : /api/v1/scans
    发送参数:
        发送参数         类型     说明
        profile_id      string   扫描类型
        ui_session_i    string   可不传
        schedule        json     扫描时间设置（默认即时）
        report_template string   扫描报告类型（可不传）
        target_id       string   目标id
'''


def start_target(target_id, profile_id):
    url = 'https://' + IP + ':13443/api/v1/scans'

    # schedule={"disable": False, "start_date": None, "time_sensitive": False}
    headers = {"X-Auth": API_KEY, "content-type": "application/json", 'User-Agent': 'curl/7.53.1'}
    values = {
        'target_id': target_id,
        'profile_id': profile_id,
        'schedule': {"disable": False, "start_date": None, "time_sensitive": False}
    }
    data = bytes(json.dumps(values), 'utf-8')
    request = urllib.request.Request(url, data, headers)
    html = urllib.request.urlopen(request).read().decode('utf-8')
    # return html
    return "now scan {}".format(target_id)


def stop_target(target_id):
    url = 'https://' + IP + ':13443/api/v1/scans/' + target_id + '/abort'
    headers = {"X-Auth": API_KEY, "content-type": "application/json", 'User-Agent': 'curl/7.53.1'}
    request = urllib.request.Request(url=url, headers=headers)
    html = urllib.request.urlopen(request).read().decode('utf-8')
    print(html)


def target_status(target_id):
    url = 'https://' + IP + ':13443/api/v1/scans/' + target_id
    headers = {"X-Auth": API_KEY, "content-type": "application/json", 'User-Agent': 'curl/7.53.1'}
    request = urllib.request.Request(url=url, headers=headers)
    html = urllib.request.urlopen(request).read().decode('utf-8')
    print(html)


def get_target_result(target_id, scan_session_id):
    url = 'https://' + IP + ':13443/api/v1/scans/' + target_id + '/results/' + scan_session_id + '/vulnerabilities '
    headers = {"X-Auth": API_KEY, "content-type": "application/json", 'User-Agent': 'curl/7.53.1'}
    request = urllib.request.Request(url=url, headers=headers)
    html = urllib.request.urlopen(request).read().decode('utf-8')
    print(html)


'''
    主要使用批量添加与启动扫描任务的功能
    即create_target()函数与start_target()函数

'''


def main():
    file = open("tt.txt", "r")
    lists = file.readlines()
    i = 0
    for fields in lists:
            i = i+ 1
            f = str(lists[i]).replace("\n", "")
            print(f)
            print(start_target(f, '11111111-1111-1111-1111-111111111113'))
            # testurl = f
            # description = "null"
            # int_criticality = 10
           # target_id = create_target(testurl, description, int_criticality).split('"')[21]
           #  with open('tt.txt', 'a') as f:
           #
           #          f.write("%s\n" % target_id)
            time.sleep(5)
            lists.pop(i)
            if i == 30:
                sep = ''
                fl = open('tt.txt', 'w')
                fl.write(sep.join(lists))
                exit()




if __name__ == '__main__':
    main()
