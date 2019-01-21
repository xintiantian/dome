# coding=utf-8
import sys
sys.path.append('../')
import requests,time,random
from beijizhou.operate_yaml import OperateYaml
import json
from beijizhou.getsql import *
url = "https://paytest.rockfintech.com/3.0.0/agreement/sign/apply"
serial = time.strftime("%Y%m%d%H%M%S")
OperateYaml().write_serial_id(serial)
data = {
      "account_type": "",
      "bank_account": serial,
      "bank_name": "ABC",
      "card_no": "622200100112463"+str(random.randint(1111,9999)),
      "cert_no": "310110198705143210",
      "cert_type": "",
      "merchant_id": "6615251545704154",
      "phone": "13761468754",
      "sign": "3",
     "sign_type": "MD5",
      "timestamp": "14516064000",
      "uuid": "2",
      "version": "3.0.0",
      "debug":"true"
  }

rea = requests.post(url=url,json=data).json()
globals()["exchange_token"] = rea["exchange_token"]

#operate_yaml.OperateYaml().write_exchange_token_id(res)


url2 = "https://paytest.rockfintech.com/3.0.0/agreement/sign/confirm"

#exchange_token_id = operate_yaml.OperateYaml().get_id("exchange_token","exchange_token")
data2 ={
      "merchant_id": "6615251545704154",
      "msg_code": "728119",
      "sign": "877d51852a19638851528c80cdae3a22",
      "timestamp": "14516064000",
      "uuid": "22",
      "version": "3.0.0",
     "exchange_token":globals()["exchange_token"] ,
      "debug":"true"
  }

reb = requests.post(url=url2,json = data2).json()


aa=get_paysqlone("select name from agreements where agreement_no='{}'".format(reb['agreement_no']))
print(aa)
print (type(aa))
bb=get_paysqlone("select card_no from agreements where agreement_no='{}'".format(reb['agreement_no']))
cc=get_paysqlone("select cert_no from agreements where agreement_no='{}'".format(reb['agreement_no']))
dd=int(get_paysqlone("select phone from agreements where agreement_no='{}'".format(reb['agreement_no'])))
print(dd)
url3 = "https://paytest.rockfintech.com/3.0.0/agreement/sign/query"

data3 ={
    "merchant_id":"6615251545704154",
    "sign":"e1bf09d24cc12d6a872219ae4a5e2178",
    "sign_type":"MD5",
    "timestamp":"14516064000",
    "uuid":"e29a5f1f-6dac-4e89-8907-8f63ae32e795",
    "version":"3.0.0",
    "debug":"true",
   "bank_account": aa,
     "card_no": bb,
      "cert_no": cc,
    "phone": dd
}

rec = requests.post(url=url3,json = data3).json()
print(rec)