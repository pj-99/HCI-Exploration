# HCI Final project exploration
> For HCI final project feasibility testing

## 手語辨識：使用現有模型
#### asl-code
From: https://github.com/Bhuribhat/ASL-Finger-Spelling-To-Text ⭐️
- 簡單改成可以：
  - [x] 同時辨識 1 ~ 4 隻手
    - [x] 單人：1 左手 + 1 右手
    - [x] 雙人：各種組合（目前無觀察到明顯 lag）

- 挑戰：
  - 目前這個 model 以下字母好像辨識不太出來: M, N, R, T

## 排行榜 leader-board

Refer to:  `leader-board/Leaderboard.py`

測試一下使用 JSON 存檔的簡易排行榜 API


一些可能的使用情境：
- 每一個玩家玩完時，會把分數存起來
  - 例如結算分數時 call 個 `add_record(user = 'userA', score = 50)`
- 呈現目前前幾高的分數在螢幕上
  - 例如開始遊戲時或分數刷新後， call 個 `fetch_records(n = 10)`，並將前 10 名的紀錄呈現在畫面上

所以請 GPT 寫的 prompt:
```
幫我寫一個 python 程式，他是一個能夠實現簡單排行榜的 python API，並且資料要能永久保存（儘量使用簡單的方式，例如存成 json 或是 csv）
每筆資料有 score(得到分數)，time（這筆資料產生的時間），user（玩家姓名）
此 API 包含以下 Function
- add_record() 增加一筆資料
- fetch_records() 取得由分數降序的 N 筆資料
```
- 之後可依照遊戲製作與設計調整，例如讓每個用戶只會有一筆分數等等
