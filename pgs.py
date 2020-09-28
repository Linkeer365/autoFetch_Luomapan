import os
import re

def formatter(some_str=None):
    some_str="Cookie: pgv_pvid=8541859840; RK=YADIJ0C4eW; ptcz=fb89f930d9e2f36e761e213df0d553bf520b692d247ae1f8533e4e39b88eeadd; pgv_pvi=1940357120; gaduid=5cd30be52f0b7; tvfe_boss_uuid=d3ae976089f1415c; XWINDEXGREY=0; ied_qq=o0564142445; pac_uid=1_564142445; o_cookie=564142445; eas_sid=Z1F5V9U371L4N7r3m7N0T9W342; pt_sms_phone=136******12; iip=0; ptui_loginuin=2822786435"
    head="Cookie: "
    some_str=some_str.replace(head,"; ")
    print(f"Str:{some_str}")
    # \s表示空格
    # 注意，这边必须有\s{1}（因为只有一个空格，不能匹配到后面的空格了！）
    key_patt=";\s{1}(.*?)="
    val_patt="=(.*?);\s{1}"
    keys=re.findall(key_patt,some_str,re.S)
    values=re.findall(val_patt,some_str,re.S)
    cookies_dict={key:value for key,value in zip(keys,values)}
    print(cookies_dict)
    # print(keys)
    # print(values)

formatter()