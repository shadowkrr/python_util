# -*- coding: utf-8 -*-

import os
import sys
import json
import string
import random
import requests
import subprocess
import urllib.request


# ディレクトリを作成する
def mkdir(dirpath):
    try:
        print("%s %s %s start" % (__file__,
                                  sys._getframe().f_code.co_name,
                                  sys._getframe().f_lineno))
        dirs = dirpath.split("/")
        path = ""
        for i in range(len(dirs)):
            if len(dirs) -1 <= i:
                path = path + "/"
                continue
            path = path + dirs[i]

            if os.path.isfile(path) is True:
                path = path + "/"
                continue

            if os.path.isdir(path) is True:
                path = path + "/"
                continue

            path = path + "/"
            os.mkdir(path)
            cmd = "sudo chmod 777 -R %s" % (path)
            subprocess.call(cmd, shell=True)

    except Exception as e:
        print("Exception e:{0}".format(e))

    print("%s %s %s end" % (__file__,
                            sys._getframe().f_code.co_name,
                            sys._getframe().f_lineno))


# Jsonファイルを読み出す
def json_read(name, path=''):
    try:
        print("%s %s %s start" % (__file__,
                                  sys._getframe().f_code.co_name,
                                  sys._getframe().f_lineno))
        print("path:%s%s" % (path, name))
        f = open(path + name, 'r')
        json_dict = json.load(f)
        f.close()
    except Exception as e:
        print ("Exception {0},{1}".format(sys.exc_info()[0], e))
        json_dict = {}

    print("%s %s %s end" % (__file__,
                            sys._getframe().f_code.co_name,
                            sys._getframe().f_lineno))
    return json_dict


# Jsonファイルに書き出す
def json_write(text, name, path):
    try:
        print("%s %s %s start" % (__file__,
                                  sys._getframe().f_code.co_name,
                                  sys._getframe().f_lineno))
        print("path:%s%s" % (path, name))
        f = open(path + name, 'w')
        f.write("%s\r\n" % (text))
        f.close()
    except Exception as e:
        print ("Exception {0},{1}".format(sys.exc_info()[0], e))

    print("%s %s %s end" % (__file__,
                            sys._getframe().f_code.co_name,
                            sys._getframe().f_lineno))


# ファイルをダウンロードし保存する
def download(url, savepath):
    try:
        print("%s %s %s start" % (__file__,
                                  sys._getframe().f_code.co_name,
                                  sys._getframe().f_lineno))
        print("url:%s" % (url))

        n = 5
        # ランダム文字列生成
        random_str = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])

        title = ""
        title = os.path.basename(url)
        title = "%s_%s" % (random_str, title)
        filepath = "%s%s" % (savepath, title)
        urllib.request.urlretrieve(url, "%s" % (filepath))
        print("filepath:%s" % (filepath))
    except Exception as e:
        print("Exception e:{0}".format(e))
        title = ""
        print("%s %s %s end" % (__file__,
                                sys._getframe().f_code.co_name,
                                sys._getframe().f_lineno))
    return title


# Jsonデータの更新
def json_update(json_data, date, name, path):
    print("%s %s %s start" % (__file__,
                                  sys._getframe().f_code.co_name,
                                  sys._getframe().f_lineno))

    json_dict = json_read(name, path)
    update_json = []

    if len(json_dict) == 0:
        json_data.update({'key':0})
        update_json.append(json_data)
        json_dict = update_json
    else:
        for d in json_dict:
            update_json.append(d)

        json_data.update({'key':len(json_dict)})
        update_json.append(json_data)
        json_dict = update_json

    json_str = json.dumps(json_dict)
    json_write(json_str, name, path)

    print("%s %s %s end" % (__file__,
                                sys._getframe().f_code.co_name,
                                sys._getframe().f_lineno))


# Jsonデータの上書き更新
def json_update_all(json_data, name, path):
    print("%s %s %s start" % (__file__,
                                  sys._getframe().f_code.co_name,
                                  sys._getframe().f_lineno))

    json_str = json.dumps(json_data)
    json_write(json_str, name, path)

    print("%s %s %s end" % (__file__,
                                sys._getframe().f_code.co_name,
                                sys._getframe().f_lineno))


# chatworkにテキストをpostする
def chatwork_send(body='', to="on"):
    APIKEY = '****************************' # APIKEYを入力
    ROOMID = '*******' # ROOMIDを入力
    ENDPOINT = 'https://api.chatwork.com/v2'


    if to == "on":
        to = '[To:1065512]' # Toをつける
    else:
        to = ""

    body = to + body

    post_message_url = '{}/rooms/{}/messages'.format(ENDPOINT, ROOMID)

    headers = { 'X-ChatWorkToken': APIKEY }
    params = { 'body': body }
    print('chatwork body[%s]' % (body))

    resp = requests.post(post_message_url,
                         headers=headers,
                         params=params)

    print(resp.content)
