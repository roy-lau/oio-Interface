import requests ;
from flask import json,Flask,make_response;
import time
app = Flask(__name__)
import hashlib
import sys
def CheckSID(dict1, secret):
    if isinstance(dict1, dict):
        list1 = sorted(dict1.items(),key=lambda x:x[0])
        str=[]

        for list_item in iter(list1):
            if list_item[0]!='sid'and list_item[0]!='sign':                    # and list_item[0]!='rsvd':
                if list_item[1] is None:
                    continue
                str.append(list_item[0])
                str.append(list_item[1])

        str=(''.join(str))
    else:
        str=dict1
    str=(''.join((secret,str)))
    # print(str)
    a2md5 = hashlib.md5()
    a2md5.update(str.encode('utf-8'))
    a2md5_Digest = a2md5.hexdigest()
    a2md5value=a2md5_Digest.upper()
    return a2md5value

# values={
#  "ver":"1.0",
#  "msgid":"5f053ec9-11d5-4580-bfb7-f82194989923",
#  "ts":"20160816095014091",
#  "service":"acsa",
#  "msgtype":"vcallreq",
#  "sid":"002B85761915447E0821803ABD7F0415",
#  "appkey":"hwh",
#  "acms":"13217794713",
#  "calledms":"13611292289"
#  }


# values={"ver":"1.0",
#         "msgid":"5742461579df5400606dce74sub",
#         "ts":"20160902112221231",
#         "service":"acbss",
#         "msgtype":"subreq",
#         "appkey":"sanhaonet",
#         "rsvd":"0",
#         "prtms":"18311083898",
#         "acms":"18510747253",
#         "subts":"20170227144303",
#         "producttype":"4",
#         "name":"杨国振",
#         "anucode":"1,2,3",
#         "cardtype":"1",
#         "callrecording":"1",
#         "cardno":"372930199105026359",
#         "sid":"505CCE48B7A20E319C1169CCE7D4A075"}


# values={"ver":"1.0",
#         "msgid":"5742461579df5400606dce74sub",
#         "ts":"20160815112221231",
#         "service":"acbss",
#         "msgtype":"unsubreq",
#         "appkey":"hwh",
#         "rsvd":"0",
#         "prtms":"",
#         "acms":"13117779842",
#         "unsubts":"20160815142221231"}




values={"msgtype":"axbunsubreq",
        "ts":"20160816131840894",
        "sid":"0D99D67B4C3CD750CDCDC3CEF0446F67",
        "subid": "1e319d6ace0c4c5cb995ba24b66aaf44",
        "productcat":"11",
        "appkey":"hwh",
        "unsubts":"20160816131840",
        "service":"acbss",
        "msgid":"2019151517",
        "prtms": "01089176507",
        "acms": "13207770504",
        "otherms": "13478821222",
        "rsvd":"0",
        "ver":"1.0"}


# values={"ver":"1.0",
#         "msgid":"9d6ff291ded74a9c9bbae42e882780dc",
#         "ts":"20160815112221231",
#         # "prtms":"15004527672",
#         "service":"acbss",
#         "msgtype":"subqryreq",
#         # "acms":"17181794254",
#         "appkey":"hwh",
#         "rsvd":"0",
#         "subid":"35e09a61962644efacb11c68d27da825"
# }

values={'msgid': '11111111111111',  # 消息ID
        'sid': '9999999999',        # 签名
        'cardno': '222',            # 身份证号码
        'productcat': '11',         # 产品类别（0： 保留。实际分配给AX(AC小号) 11：AXB 12: 语音验证业务 13：AXYB业务的XYB ）
        'ts': '1486458093',         # 时间戳
        'msgtype': 'axbsubreq',     # 消息类型
        # B--------------被叫号码
        # 'otherms': '18601976151', #籍扬
        # 'otherms': '15037900958', #郑海龙
        # 'otherms': '13521204302', #李总
        'otherms': '18267597127',   #李新惠
        # 'otherms': '15806130891', #李
        # 'otherms': '13075510807',
        # 'otherms': '15618375271',
        # 'otherms': '13269673885',
        # 'otherms':'13611292289',
        # 'otherms':'4008205555',
        'ver': '1.0',                   # 版本号
        # 'appkey': 'rrcar',
        'appkey': 'GZAXB',          # 应用标识
        # 'appkey':'hwh',
        'cardtype': '1',            # 证件类型（证件类型）
        'rsvd': '',                 # 保留字段
        'name': 'aaabbb',
        'service': 'acbss',         # 业务类型
        'producttype': '3',         # 订购类型 (0：包年 1：包季 2：包月 3：按次 4：体验 )
        "callrestrict": "1",
        # --------主叫号码（prtms---A）
        'prtms': '13526636962',     #刘强
        # 'prtms': '15037900958',   #李新惠
        # 'prtms': '13810326774',   #张剑锋
        # 'prtms': '18601976151',   #籍扬
        # 'prtms':'15037900958',
        # 'acms': '13167180461',
        'acms': '',                    # 隐私号码(X号码，动态分配)
        "unsubts":"20170616013030",    # 退订时间
        'unsubmethod': '0',            # 自动退订方式（0：振铃退订 1：挂机退订）
        "callrecording":"1",           # 录音控制（0：不开通录音功能 ， 1：开通录音功能）
        "calldisplay":"0,1"            # 来电显示
        }

# values={"acms":"",
# "appkey":"GZAXB",
# "cardno":"410321198708081012",
# "cardtype":"1","msgid":"1","msgtype":"axbsubreq","name":"\u5f20\u4e09",
# "otherms":"13611292289",
# "productcat":"11",
# "producttype":"3",
# "prtms":"13810326774",
# "rsvd":"",
# "service":"acbss",
# "ts":"1495702904",
# "unsubmethod":"0",
# "unsubts":"20170525171144","ver":"1.0","sid":"590C07B6E4F86C84002D7C9DC3EBDA84"}


# values={"ver":"1.0",
#         "msgid":"5742461579df5400606dce74sub",
#         "ts":"20160902112221231",
#         "service":"acbss",
#         "msgtype":"chgprtmsreq",
#         "appkey":"hwh",
#         "rsvd":"0",
#         "subid":"6e72f36d746e439fabfe4fc28a9ebe02",
#         "acms":"13217794713",
#         "oldprtms":"13810326774",
#         "newprtms":"18501203610",
#         "chgts":"20160922162233",
#         "sid":"505CCE48B7A20E319C1169CCE7D4A075"}


# values={"ver":"1.0",
#        "msgid":"5742461579df5400606dce74sub",
#        "ts":"20160816142221231",
#        "service":"acbss",
#        "msgtype":"axbsubreq",
#        "appkey":"GZAXB",
#        "rsvd":"0",
#        "prtms":"13810326774",
#        # "callrestrict": "0",
#        "acms":"",
#        "otherms":"18501203610",
#        "subts":"201608161422",
#        "unsubts":"",
#        "unsubmethod":"0",
#        "producttype":"3",
#        "productcat":"11",
#        "name":"",
#        "anucode":"1,2,3",
#        "cardtype":"1",
#        "cardno":"410321197607131012",
#        "callrecording":"0"}



# values={
#        "ver":"1.0",
#        "msgid":"5742461579df5400606dce74sub",
#        "ts":"20160816142221231",
#        "service":"acbss",
#        "msgtype":"outaxbtransferdelreq",
#        "appkey":"rrcar",
#        "rsvd":"0",
#        "acms":'13122596541'
# }

# values={
#        "ver":"1.0",
#        "msgid":"5742461579df5400606dce74sub",
#        "ts":"20160816142221231",
#        "service":"acbss",
#        "msgtype":"outaxbtransfersetreq",
#        "appkey":"hwh",
#        "rsvd":"0",
#        "acms":"18510749671",
#        "transferms":"01089176234",
#        "transfercalldisplay":"1"
# }


# values={"ver":"1.0",
#        "msgid":"5742461579df5400606dce74sub",
#        "ts":"20160816142221231",
#        "service":"acbss",
#        "msgtype":"axbsubreq",
#        "appkey":"GZAXB",
#        "rsvd":"0",
#        "prtms":"15037900958",
#        "callrestrict": "1",
#        "acms":"13207774044",
#        "otherms":"13911677275",
#        "subts":"201608161422",
#        "unsubts":"",
#        "unsubmethod":"0",
#        "producttype":"3",
#        "productcat":"11",
#        "name":"李晓国",
#        "anucode":"1,2,3",
#        "cardtype":"1",
#        "cardno":"410321197607131012",
#        "callrecording":"0"}

# values={"ver":"1.0",
#        "msgid":"5742461579df5400606dce74sub",
#        "ts":"20160816142221231",
#        "service":"acbss",
#        "msgtype":"axbsubreq",
#        "appkey":"GZAXB",
#        "rsvd":"0",
#        "prtms":"13810326774",
#        "callrestrict": "1",
#        "acms":"13207770504",
#        "otherms":"15527892098",
#        "subts":"201608161422",
#        "unsubts":"",
#        "unsubmethod":"0",
#        "producttype":"3",
#        "productcat":"11",
#        "name":"李晓国",
#        "anucode":"1,2,3",
#        "cardtype":"1",
#        "cardno":"410321197607131012",
#        "callrecording":"0"}



# values={"ver":"1.0",
#         "msgid":"5742461579df5400606dce74unsub",
#         "sid":"0",
#         "ts":"20160816142543688",
#         "service":"acbss",
#         "msgtype":"axbsubqryreq",
#         "appkey":"hwh",
#         "rsvd":"0",
#         "subid":"33f6efc03a444f0cb58b9108aef5548c",
#         "prtms":"13810326774",
#         "acms":"13217794713",
#         "otherms":"15037900958"
#         }


# values={"msgtype":"axbunsubreq",
#         "ts":"20160816131840894",
#         "sid":"0D99D67B4C3CD750CDCDC3CEF0446F67",
#         # "subid": "4af5793deb21489da1343fd830ea30f2",
#         "productcat":"11",
#         "appkey":"GZAXB",
#         "unsubts":"20160816131840",
#         "service":"acbss",
#         "msgid":"2019151517",
#         "prtms": "01089176438",
#         "acms": "13207770834",
#         "otherms": "18518281201",
#         "rsvd":"0",
#         "ver":"1.0"}



# values={"ver":"1.0",
#        "msgid":"5742461579df5400606dce74sub",
#        "ts":"20160816142221231",
#        "service":"acbss",
#        "msgtype":"axbsubupdreq",
#        "sid":"0",
#        "appkey":"hwh",
#        "rsvd":"0",
#        "prtms":"13810326774",
#        "subid":"6e72f36d746e439fabfe4fc28a9ebe02",
#        "callrestrict": "1",
#        "acms":"13217794713",
#        "otherms":"18501203610",
#        "subts":"201608161422",
#        "productcat":"11",
#        "anucode":"1,2,3",
#        "smsmtchannel": "1",
#        "voicecalledchannel": "1",
#        "whites": "",
#        "calldisplay":"0,0",
#        "callrecording":"1"

# }

# sid=CheckSID(values,'8BECLUT23E0P9GGN')
sid=CheckSID(values,'L1AAWZPWBTBJ')
# sid=CheckSID(values,'IAEKMVDEUZSF')
# sid=CheckSID(values,'CZU7C9N1SQO1RIOW')
# sid=CheckSID(values,'L9HASRNCM0IQ')
# sid=CheckSID(values,'C0BITFVGVF4GIKRP')

# print(sid)
values['sid']=sid

headers = {'Content-Type': 'application/json','charset':'gbk'}
b=time.time()
# r = requests.post('http://120.24.214.65:6688',json.dumps(values),headers=headers)

# r = requests.post('http://120.24.214.65:5858',json.dumps(values),headers=headers)
r = requests.post('http://101.200.221.216:80/',json.dumps(values),headers=headers,timeout=10)
# r = requests.post('http://120.24.214.65:5858',json.dumps(values),headers=headers)
# r = requests.post('http://101.201.101.70:5000',json.dumps(values),headers=headers)
e=time.time()
print(e-b)
print(r.text)
