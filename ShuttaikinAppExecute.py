# -*- coding: utf-8 -*-

import json
import ShuttaikinApp
import datetime

SETTINGS_JSON = "settings.json"
RESULTS_JSON = "results.json"
ENCODING = "utf-8_sig"

json_open = open(SETTINGS_JSON, "r", encoding=ENCODING)
json_load = json.load(json_open)

#設定ファイルにkeyがあれば実行
if "username" in json_load and "message" in json_load:
	#実施結果ファイル読込
	json_open2 = open(RESULTS_JSON, "r", encoding=ENCODING)
	json_load2 = json.load(json_open2)

	today = format(datetime.date.today(), '%Y%m%d')
	#今日日付のkeyがあれば実施済
	if not today in json_load2:
		print("出退勤未実施")
		#未実施ならjsonを更新
		json_load2[today] = True
		with open(RESULTS_JSON, "w", encoding=ENCODING) as outfile:
			json.dump(json_load2, outfile)
		#出退勤メソッド実行
		ShuttaikinApp.shuttaikinNotify(json_load["username"]+"\n"+json_load["message"])
	else:
		print("出退勤実施済")
else:
	print("設定ファイルエラー")
