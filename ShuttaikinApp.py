# -*- coding: utf-8 -*-

import sys
import requests
import json

WEB_HOOK_URL = "https://hooks.slack.com/services/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"

def shuttaikinNotify(msg):
	requests.post(WEB_HOOK_URL, data=json.dumps({
		"text" : msg
	}))

if __name__=="__main__":
	if len(sys.argv) != 2:
		print("パラメータ数エラー")
		exit(9)

	shuttaikinNotify(sys.argv[1])
