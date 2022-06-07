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
| ---- | ---- | ---- |
| name | string | チャンネル名 |
| id | string | チャンネルID |

## UserType

| 名前 | タイプ | 説明 |
| ---- | ---- | ---- |
| username | string | ユーザー名 |
| discriminator | string | ユーザータグ |
| id | string | ユーザーID |
| avatarURL | string | ユーザーavatarurl |
| bot | bool | botかどうか |

## GuildType

| 名前 | タイプ | 説明 |
| ---- | ---- | ---- |
| name | string | サーバー名 |
| id | string | サーバーID |
| iconURL | string | サーバーiconのurl |

## MessageType

| 名前 | タイプ | 説明 |
| ---- | ---- | ---- |
| content | string | メッセージのコンテンツ |
| id | string | メッセージID |
| cleanContent | string | メンション等を省いたメッセージのコンテンツ |
| ?reference | Optional[string] | 返信先のメッセージID |
| ?attachments | List[[MessageAttachmentType](./#MessageAttachmentType)] | 画像のURLなど |
| embeds | List[[EmbedType](./#EmbedType)] | 埋め込みメッセージら |
