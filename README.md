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


## 2017.10.11 Wed

cloud9上でPHPからMySqlに接続する方法

```
// データベースに接続
$servername = ('127.0.0.1');
$username = ('faketurn');
$password = "";
$database = "phpkiso";
$dbport = 3306;

// Create connection
$db = new mysqli($servername, $username, $password, $database, $dbport);

// Check connection
if ($db->connect_error) {
    die("Connection failed: " . $db->connect_error);
} 
// echo "Connected successfully (".$db->host_info.")";
```
