import requests
from lxml import etree
import re

from bs4 import BeautifulSoup

from PIL import Image

import datetime

import os
import sys

import time

target_dir=r"D:\AllDowns"

guide_url="https://www.luomapan.com/"

qrcode_create_url= "https://www.luomapan.com/wechat/qrcode/create"

qrcode_status_url="https://www.luomapan.com/wechat/qrcode/status"

qrcode_image_path=f"{target_dir}{os.sep}luomapan.png"


headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        # "Referer": "https://www.luomapan.com/"
}

headers2={  "Accept": "application/json, text/plain, */*",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"zh-CN,zh;q=0.9,ja;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
          }

s=requests.Session()

def cookies_str2dict(some_str):
    # some_str="Cookie: pgv_pvid=8541859840; RK=YADIJ0C4eW; ptcz=fb89f930d9e2f36e761e213df0d553bf520b692d247ae1f8533e4e39b88eeadd; pgv_pvi=1940357120; gaduid=5cd30be52f0b7; tvfe_boss_uuid=d3ae976089f1415c; XWINDEXGREY=0; ied_qq=o0564142445; pac_uid=1_564142445; o_cookie=564142445; eas_sid=Z1F5V9U371L4N7r3m7N0T9W342; pt_sms_phone=136******12; iip=0; ptui_loginuin=2822786435"

    head_str="Cookie: "
    some_str=some_str.replace(head_str,"; ")
    print(f"{some_str}")
    # \s表示空格
    # 注意，这边必须有\s{1}（因为只有一个空格，不能匹配到后面的空格了！）
    key_patt=";\s{1}(.*?)="
    val_patt="=(.*?);\s{1}"
    keys=re.findall(key_patt,some_str,re.S)
    values=re.findall(val_patt,some_str,re.S)
    cookies_dict={key:value for key,value in zip(keys,values)}
    print(cookies_dict)
    return cookies_dict

# cookies_str="Cookie: pgv_pvid=8541859840; RK=YADIJ0C4eW; ptcz=fb89f930d9e2f36e761e213df0d553bf520b692d247ae1f8533e4e39b88eeadd; pgv_pvi=1940357120; gaduid=5cd30be52f0b7; tvfe_boss_uuid=d3ae976089f1415c; XWINDEXGREY=0; ied_qq=o0564142445; pac_uid=1_564142445; o_cookie=564142445; eas_sid=Z1F5V9U371L4N7r3m7N0T9W342; pt_sms_phone=136******12; iip=0; ptui_loginuin=2822786435"
# cookies_dict=cookies_str2dict(cookies_str)

# headers["cookie"]=cookies_dict

# cookies={
#     "pgv_pvid":"8541859840",
#     "RK","YADIJ0C4eW"; ptcz=fb89f930d9e2f36e761e213df0d553bf520b692d247ae1f8533e4e39b88eeadd; pgv_pvi=1940357120; gaduid=5cd30be52f0b7; tvfe_boss_uuid=d3ae976089f1415c; XWINDEXGREY=0; ied_qq=o0564142445; pac_uid=1_564142445; o_cookie=564142445; eas_sid=Z1F5V9U371L4N7r3m7N0T9W342; pt_sms_phone=136******12; iip=0; ptui_loginuin=2822786435
# }

# now=datetime.datetime.now()
# now_ts=now.timestamp()
# print(int(now_ts))

# sys.exit(0)


# query_cookies_str=f"Cookie: romapan:sessid=5a115f60-bb0e-4f14-9f5b-d6c605f837a9; romapan:sessid.sig=I23A_fdYGSCvVrUygCtj_U8yhRg; Hm_lvt_1cfb61bc5c800164d5ca43aef0408655=1601039730,1601220960,1601225677,1601269502; Hm_lpvt_1cfb61bc5c800164d5ca43aef0408655={now_ts}"
# query_cookies_dict=cookies_str2dict(query_cookies_str)

    # 不改verify=False会报错SSLERRROR很烦，以后更新时再把这个警告干掉好了...]
    # json()返回的是python字典...

    # now = datetime.datetime.now()
    # now_ts = now.timestamp()
    # cookies_str=f"Cookie: romapan:sessid=5a115f60-bb0e-4f14-9f5b-d6c605f837a9; romapan:sessid.sig=I23A_fdYGSCvVrUygCtj_U8yhRg; Hm_lvt_1cfb61bc5c800164d5ca43aef0408655=1601220960,1601225677,1601269502,1601278371; Hm_lpvt_1cfb61bc5c800164d5ca43aef0408655={now_ts}"
    # cookies_dict=cookies_str2dict(cookies_str)
    # s.cookies.update(cookies_dict)

def login():
    qrcode_query_dict=s.get(qrcode_create_url, headers=headers, verify=False).json()
    sess_cookies_dict=s.cookies.get_dict()

    print("sess cookies",sess_cookies_dict)

    # cookies 定制
    # https://stackoverflow.com/questions/17224054/how-to-add-a-cookie-to-the-cookiejar-in-python-requests-library

    now = datetime.datetime.now()
    now_ts = int(now.timestamp())

    # 注意末尾一定要加一个; （不然不能匹配到...）

    my_cookies_str=f"Cookie: romapan:sessid=5a115f60-bb0e-4f14-9f5b-d6c605f837a9; romapan:sessid.sig=I23A_fdYGSCvVrUygCtj_U8yhRg; Hm_lvt_1cfb61bc5c800164d5ca43aef0408655=1601220960,1601225677,1601269502,1601278371; Hm_lpvt_1cfb61bc5c800164d5ca43aef0408655={now_ts}; "
    my_cookies_dict=cookies_str2dict(my_cookies_str)

    my_cookies_dict.update(sess_cookies_dict)

    my_cookies=requests.utils.cookiejar_from_dict(my_cookies_dict)

    print(my_cookies_dict)

    s.cookies=my_cookies

    # print(my_cookies_dict)


    # sess_cookies=s.cookies
    # print("sess_cookies:",sess_cookies)
    qrcode_image_url=qrcode_query_dict["data"]["image"]
    print(f"qrcode query:{qrcode_image_url}")
    qrcode_image = s.get(qrcode_image_url, headers=headers,verify=False).content
    # assert cok1==cok2 and bool(cok1)!=0
    # sys.exit(0)

    with open(qrcode_image_path, "wb") as f:
        f.write(qrcode_image)
    img=Image.open(qrcode_image_path)

    # 其实不登录也可以hhhh
    # 妈的我充了快40块钱！！！！！

    # 以后统一不登录直接进去...

    # img.show()
    # time.sleep(2)
    img.close()


    # time.sleep(5)
    # with requests.session() as s1:
    qrcode_status_dict=s.get(qrcode_status_url,headers=headers2,verify=False).json()
    print(qrcode_status_dict)
    try:
        if qrcode_status_dict["data"]["nickname"]=="冰晶光学社":
            print("Login success!")
            return True
    except KeyError:
        return False

def get_fields(page_text,patt):
    html=etree.HTML(page_text)
    fields=html.xpath(patt)
    print("Found:\n")
    for each in fields:
        print(each)
    print("\n")
    return fields


def print_linkInfos(some_links,some_itemInfos):
    for idx,(link,info) in enumerate(zip(some_links,some_itemInfos),1):
        print(f"\nInfo:{info}\t\t\t{idx}\nLink:{link}")

def get_max_pagenum(search_link):
    page_text=s.get(search_link,headers=headers).text
    html=etree.HTML(page_text)
    pagenum_patt="//a[@class='pager-it']//text()"
    pagenums=html.xpath(pagenum_patt)

    if pagenums==[]:
        # 搜索结果总共一页（此时一个也没有，因为此时它的页码的class是pager-it active，那么就一个也没有）
        max_pagenum=1
    else:
        for each in pagenums[::-1]:
            # 倒着排序，（因为xpath获取到的页码数一定从小到大，懂得都懂）
            # 因为可能会有【下一页】的标签，这些必须排除掉
            if each.isdigit():
                max_pagenum=int(each)
                break
    return max_pagenum


def get_netdisk_dict_from_detail_link(detail_link):
    page_text=s.get(detail_link,headers=headers).text
    html=etree.HTML(page_text)
    script_patt="//script[starts-with(text(),'window.__NUXT__=')]//text()"
    script_str=html.xpath(script_patt)[0]

    netdisk_link_patt=",\"(https:.*?)\""
    netdisk_link=re.findall(netdisk_link_patt,script_str)[0]
    passwd_patt="//span[@class='meta-item copy-item']//text()"

    # 获取到的样式是这样的，['提取密码', ' \n            uapr \n            ', '点击复制']
    # 所以要选择第2个
    try:
        passwd=html.xpath(passwd_patt)[1]
    except IndexError:
        print("无密码！")
        passwd=""

    # 顺便format一下

    netdisk_suffix=netdisk_link.rsplit("u002F",maxsplit=1)[-1]
    netdisk_link=f"https://pan.baidu.com/s/{netdisk_suffix}"
    if len(passwd)>=1:
        passwd=re.sub("\s","",passwd)


    print("Netdisk link:",netdisk_link)
    print("Netdisk Passwd:",passwd)

    # 再次重申两者不同
    ## a="123", [a]=["123"], list(a)=['1','2','3']

    assert len([netdisk_link])==1

    # 这里不用改，因为你passwd='', len([""])也是1
    assert len([passwd])==1

    # netdisk_link=netdisk_link[0]
    # passwd=passwd[0]

    return dict(netdisk_link=netdisk_link,passwd=passwd)

def fetch_one_page(keyword,pagenum):
    search_url=f"https://www.luomapan.com/search?keyword={keyword}&page={pagenum}"

    page_text=s.get(search_url,headers=headers).text

    # soup=BeautifulSoup(page_text,"lxml")
    # with open(f"{target_dir}{os.sep}soup.txt","w",encoding="utf-8") as f:
    #     f.write(soup.prettify())
    # print("soup done.")
    # print(page_text)

    item_patt="//a[@class='valid']//@href"
    itemInfo_patt="//a[@class='valid']//text()"

    items=get_fields(page_text,item_patt)

    # 样式是类似这样的/detail/1f4b278c5a058c996605b086c5e9375f
    # 所以com后面直接跟each

    item_links=[f"https://www.luomapan.com{each}" for each in items]
    itemInfos=get_fields(page_text,itemInfo_patt)

    print_linkInfos(item_links,itemInfos)

    sep_of_demands=","
    demands_str=input(f"Your choice:(separate with {sep_of_demands})")

    # 先不支持1to5这种语句...因为最后实现起来大概也就是parse成1,2,3,4,5的样子...

    demands_list=[int(each) for each in demands_str.split(sep_of_demands) if each.isdigit()]

    netdisk_dicts_list=[]

    for each in demands_list:
        idx=each-1
        detail_link=item_links[idx]
        netdisk_dict=get_netdisk_dict_from_detail_link(detail_link)
        print(f"One disk:{netdisk_dict}")
        netdisk_dicts_list.append(netdisk_dict)

    print("\n***===***")
    for each in netdisk_dicts_list:
        print(each)
    print("===***===\n")

    return netdisk_dicts_list



def main():
    mForMore="m"
    while mForMore=='m':
        netdisk_dicts=[]
        keyword = input("想搜什么:")

        netdisk_results_path=f"{target_dir}{os.sep}results_{keyword}.txt"

        # 没有就新建一个

        if not os.path.exists(netdisk_results_path):
            open(netdisk_results_path,"w").close()

        login_result=login()
        if not login_result:
            print("login failed!")
        search_url = f"https://www.luomapan.com/search?keyword={keyword}"
        max_pagenum=get_max_pagenum(search_url)
        print("Max pagenum:",max_pagenum)
        active_pagenum=1
        nForNewPage="n"
        while active_pagenum<=max_pagenum and nForNewPage=="n":
            netdisk_dicts_list=fetch_one_page(keyword,active_pagenum)
            netdisk_dicts.extend(netdisk_dicts_list)
            prompt_for_newPage=input("Next page Press n: ")
            nForNewPage=prompt_for_newPage
            active_pagenum+=1
            if active_pagenum==max_pagenum+1:
                print("Page no more. Hence finished.")
                break
        print("one search is done.")

        netdisk_dicts_s="\n".join([str(each) for each in netdisk_dicts])

        with open(netdisk_results_path,"a",encoding="utf-8") as f:
            f.write(netdisk_dicts_s)

        prompt_for_MoreSearch=input("Want more search?More search Press m: ")
        mForMore=prompt_for_MoreSearch

    print("Search done.")

if __name__ == '__main__':
    main()
            # sys.exit(-1)










# if __name__ == '__main__':
#     # detail="https://www.luomapan.com/detail/1f4b278c5a058c996605b086c5e9375f"
#     # get_netdisk_dict_from_detail_link(detail)
#     # detail2=
#     main()
