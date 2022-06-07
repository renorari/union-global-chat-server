# タイプ

## 概要

主にjsonの中身です。

## GatewayGetType

| 名前 | タイプ | 説明 |
| ---- | ---- | ---- |
| channel | [ChannelType](./#ChannelType) | 送信元チャンネル |
| author | [UserType](./#UserType) | メッセージ作成者 |
| guild | [GuildType](./#GuildType) | 送信元サーバー |
| from_bot | str | どのbotがこのデータを送信したか |
| message | [MessageType](./#MessageType) | メッセージコンテンツ

## ChannelType

| 名前 | タイプ | 説明 |
