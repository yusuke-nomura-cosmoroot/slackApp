# -*- coding: utf-8 -*-

import sys
import requests
import json

SETTINGS_JSON = "settings.json"
ENCODING = "utf-8_sig"

def shuttaikinNotify(msg):
	json_open = open(SETTINGS_JSON, "r", encoding=ENCODING)
	json_load = json.load(json_open)
	if "webhookurl" in json_load:
		requests.post(json_load["webhookurl"], data=json.dumps({
			"text" : msg
		}))
	else:
		print("設定ファイルエラー")

if __name__=="__main__":
	if len(sys.argv) != 2:
		print("パラメータ数エラー")
		exit(9)

	shuttaikinNotify(sys.argv[1])
