#author : @wahyuhadi
#zap scanner modules


from pprint import pprint
from time import sleep
import zapv2

import requests
import json
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

from os import environ

try:
    zap = zapv2.ZAPv2(proxies={"http": environ["ZAP"], "https": environ["ZAPTLS"]})
except Exception:
    url ='localhost:8181'
    zap = zapv2.ZAPv2(proxies={"http": f'http://{url}', "https": f'http://{url}'})




def spider_mode(url):
    scan_id = start_spider(url)
    return scan_id

def start_spider(url):
    redirected_url = get_redirect_url(url)
    scan_id = zap.spider.scan(
        url=redirected_url, 
        recurse=True, 
        maxchildren=10
    )
    return {"scan_id": scan_id}


def is_scan_status(scan_id):
     return {"status": zap.spider.status(scanid=scan_id)}


def is_view_summary(url):
    redirected_url = get_redirect_url(url)
    full_zap_results = zap.alert.alerts(baseurl=redirected_url)
    summary = []
    
    for single_result in full_zap_results:
        summary.append(
            {
                "alert": single_result.get("alert"),
                "risk": single_result.get("risk"),
                "method": single_result.get("method"),
                "url": single_result.get("url"),
                "param": single_result.get("param", "null"),
                "evidence": single_result.get("evidence", "null"),
                "solution": single_result.get("solution", "null"),
            }
        )
    output = list({v["evidence"]: v for v in summary}.values())
    return output

def get_redirect_url(url):
    r = requests.get(url, verify=False)
    return r.url
