# -*- coding: utf-8 -*-

import sys
import requests
import json

SETTINGS_JSON = "settings.json"
ENCODING = "utf-8"
WEBHOOKURL = "https://hooks.slack.com/services/"

def shuttaikinSetting(key, value):
	with open(SETTINGS_JSON, "r", encoding=ENCODING) as json_open:
		json_load = json.load(json_open)
		if key not in json_load:
			print("設定ファイルに対象設定が見つかりません")
			return 9
			
	with open(SETTINGS_JSON, "w", encoding=ENCODING) as json_open:
		json_load[key]=value
		json.dump(json_load, json_open, ensure_ascii=False, indent=4)

def shuttaikinNotify(msg):
	with open(SETTINGS_JSON, "r", encoding=ENCODING) as json_open:
		json_load = json.load(json_open)
		if "webhookurl" in json_load:
			requests.post(WEBHOOKURL + json_load["webhookurl"], data=json.dumps({
				"text" : json_load["username"]+"\n"+msg
			}))
		else:
			print("設定ファイルエラー")
			return 9

if __name__=="__main__":
	if len(sys.argv) == 2:
		shuttaikinNotify(sys.argv[1])
	elif len(sys.argv) == 4:
		if sys.argv[1] == "-SETTING":
			shuttaikinSetting(sys.argv[2], sys.argv[3])
		else:
			print("パラメータ内容エラー")
			exit(9)
	else:
		print("パラメータ数エラー")
		exit(9)

	
