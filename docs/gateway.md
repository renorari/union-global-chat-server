# ゲートウェイ

## 概要

主にウェブソケットを使いメッセージ受信をリアルタイムで取得します。

## 送信及び受信

主にjsonを[これ](http://zlib.net/)使って圧縮して送信します。

## 認証

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
