# coding=utf-8
import re

language = '''''<tr><th>Sex：</th><td>Male</td></tr><tr>'''

res_tr = r'<tr>(.*?)</tr>'
m_tr =  re.findall(res_tr,language,re.S|re.M)

for line in m_tr:
    print line

    res_th = r'<th>(.*?)</th>'
    m_th = re.findall(res_th,line,re.S|re.M)

    for mm in m_th:
        print mm

    res_td = r'<td>(.*?)</td>'
    m_td = re.findall(res_td,line,re.S|re.M)

    for nn in m_td:
        print nn
