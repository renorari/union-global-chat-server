# 仕様

## api url

localhost

## 認証

headerにこんな感じにやってください。
| 名前 | 値 |
| ---- | ---- |
| Authorization | Bearer {token} |

## /api/v1/channels

```json
{
    "channel": {
        "name": "text",
        "id": "000000000"
    },
    "author": {
        "username": "name",
        "discriminator": "8888",
        "id": "000000000",
        "avatarURL": "URL(png, dynamic, 512)",
        "bot": false
    },
    "guild": {
        "name": "KGC",
        "id": "000000000",
        "iconURL": "URL(png, dynamic, 256)"
    },
    "message": {
        "content": "",
        "id": "",
        "cleanContent": "メンション等を省いたcontent",
        "?reference": "",
        "?attachments": [{"name": "filename", "url": "fileurl", "?height": "height", "?width": "width", "content_type": "file’s content_type"}],
        "embeds": []
     }
}
```
と送信するとウェブソケットに全部送信されます。


## ゲートウェイ

### 概要

主にウェブソケットを使います。

### 送信及び受信

主にjsonを[これ](http://zlib.net/)使って圧縮して送信します。

### 認証

```json
{
    "type": "identify",
    "data": {
        "token": "トークン"
    }
}
```

と送信し、成功するとこれが帰ってきます。

```json
{
    "type": "identify",
    "success": true
}
```
