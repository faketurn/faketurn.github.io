# 自習時間を取ってつくるもの


## 参考リンク

[https://faketurn.github.io](https://faketurn.github.io)

[HTML4.01 日本語訳](http://www.asahi-net.or.jp/~sd5a-ucd/rec-html401j/cover.html)

[HTML5 日本語訳](https://momdo.github.io/html5/Overview.html)

## TODO

- cloud9のIDEに慣れる
- JavaでFizz Buzz書く
- サーバー側で動く環境を作る
- 静的HTMLの管理を動的にやる
- アプリ作る
- HTML5が活用できるようになる
- SPA作る
- PHPでアプリ作る


### 2017.10.11 Wed

## cloud9上でPHPからMySqlに接続する方法

参考：[MySqlへの接続方法](https://community.c9.io/t/setting-up-mysql/1718/16)

参考：[PHPからデータベースを操作する](https://team-lab.github.io/skillup/1/9.html)

```php
// データベースに接続する
$servername = (localhost);
$username = ('username');
$password = "";
$database = "databasename";
$dbport = 3306;

// Create connection
$db = new mysqli($servername, $username, $password, $database, $dbport);

// Check connection
if ($db->connect_error) {
    die("Connection failed: " . $db->connect_error);
}
// 文字化けしないように文字コードをutf8に指定する
$db->set_charset("utf8");
// 接続成功時の確認メッセージ。不要ならコメント化
echo "Connected successfully (".$db->host_info.")";
```

```php
// データベースにSQLを実行させる
// プリペアドステートメントprepared statementを作成　valuesの各値は?にしておく
$sql = "insert into tablename(columnname1, columnname2, columnname3) values (?, ?, ?)";
$stmt = $db->prepare($sql);

// ?の位置に値を割り当てる sはstringの意味。intならi、binaryならb。
$stmt->bind_param('sss', value1, value2, value3);
//実行
$stmt->execute();
```


```php
// データベースとの接続を終了する
$db->close();
```
