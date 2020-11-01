# slackApp

====

Slackに出退勤連絡するツール

## 使い方

### Slackにメッセージを投稿
python ShuttaikinApp.py 投稿メッセージ

設定「webhookurl」のチェンネルに設定「username」+改行+投稿メッセージが投稿される

### Slackに1日1回デフォルトメッセージを投稿
python ShuttaikinAppExecute.py

設定「webhookurl」のチェンネルに設定「username」+改行+設定「message」が投稿される

上記は1日1回のみ投稿可能

### slackAppの設定を変更
python ShuttaikinApp.py -SETTING 設定対象 設定値

設定内容

webhookurl：Slack投稿対象のwebhookurl(https://hooks.slack.com/services/ 以降を設定する)

username：Slack投稿時に記載される投稿者を表す名前

message：1日1回デフォルトメッセージ投稿時のメッセージ内容

## 自動投稿設定
タスクスケジューラに登録する事で実現する

### 設定方法
01.ファイル名を指定して実行で「Taskschd.msc」を実施

02.操作⇒基本タスクの作成

03.任意の名前を設定

04.次へ

05.トリガーは毎週を設定

06.次へ

07.任意に開始を設定(開始の時間が実行時間となる)

08.月曜日～金曜日を選択する

09.次へ

10.プログラムの開始を設定

11.次へ

12.プログラム/スクリプトにpythonのフルパスを設定

13.引数の追加にShuttaikinApp.py<半角スペース>任意の出勤/退勤メッセージを設定

14.開始(オプション)にShuttaikinApp.pyの配置ディレクトリを設定

15.次へ

16.完了

※祝日等、通知したくない場合は手動でタスクを無効化すること

