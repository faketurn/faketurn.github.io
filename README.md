# 自習時間を取ってつくるもの


## ■参考リンク

[https://github.com/faketurn/faketurn.github.io](https://github.com/faketurn/faketurn.github.io)

[https://faketurn.github.io](https://faketurn.github.io)

[HTML4.01 日本語訳](http://www.asahi-net.or.jp/~sd5a-ucd/rec-html401j/cover.html)

[HTML5 日本語訳](https://momdo.github.io/html5/Overview.html)

## ■TODO

- cloud9のIDEに慣れる
- JavaでFizz Buzz書く
- サーバー側で動く環境を作る
- 静的HTMLの管理を動的にやる
- ブログアプリ作る
- HTML5が活用できるようになる
- SPA作る
- PHPでショッピングカートアプリ作る
- PHPでブログのテンプレートを作るPHP

### 2017l10.13 Fri

## ■コードの失敗

```php
// 正しいコード
$dsn = "mysql:dbname=hoge; host=localhost; charset=utf8mb4";

// 間違えていたコード
$dsn = "mysql:dbname=hoge, host=localhost, charset=utf8mb4";
```
セミコロンで分割するところを、カンマで区切っていた。……そりゃ動かないわ。




### 2017.10.12 Thu

## ■はじめてのプログラミング学習

プログラミングの学習をすべて無料でまかのうと効率が悪くなりがちで時間がかかる。効率よくステップアップするには書籍や有料サービスを積極活用すると良い。

初めはpython3からが良いように思う。次にJavaなどの低級言語を触ってみる。あとは自由。ファイルとREPLの両方になれると上達も早い。

#### うまく学習が進まない人へのアドバイス

- なかなか学習が進まない方は、プログラミングの理解と、プログラミング言語の理解は別だと考えてみるといいかもしれない。つまり、プログラミング自体が初めてなのか、一度別の言語でプログラミングしたことがあるけど、このプログラミング言語を触るのは初めてなのかということ。
- 先入観はいちいち捨てていく。プログラミングの習得に必要なことだけ学んでいく。
- ひとつのお手本のみを鵜呑みにしない。2つめ、3つ目の例を見るとまた違った面が見えたりする。
- コピペや書き写しではプログラミングしたとは言えない。理解したかなと感じたら、何も見ずに書けるまで反復練習する。


#### Pythonで学ぶ、初めてのプログラミング
初心者がつまづくところをフォローしてる点がありがたい。平易でわかりやすい説明と必要なところを絞って解説してくれてるのでとっつきやすい。

無料で見られるのはいくつかの動画のみ。全部見るには有料会員を。

- [Pythonで学ぶ、初めてのプログラミング - schoo](https://schoo.jp/class/3447)


## ■PDOを使ってPHPでMySqlを利用する

[PHPでデータベースに接続するときのまとめ
](https://qiita.com/mpyw/items/b00b72c5c95aac573b71)

[【PHP超入門】クラス～例外処理～PDOの基礎
](https://qiita.com/7968/items/6f089fec8dde676abb5b)


### 2017.10.11 Wed

## ■PHPからMySqlのプリペアードステートメントで取得するコードに悪戦苦闘

<http://blog.pionet.co.jp/experience/archives/425>

どうやらもう少しPHPの勉強が必要なようだ。


## ■cloud9上でPHPからMySqlに接続する方法

参考：[MySqlへの接続方法](https://community.c9.io/t/setting-up-mysql/1718/16)

参考：[PHPからデータベースを操作する](https://team-lab.github.io/skillup/1/9.html)

参考：[PHP::fetch_object](http://php.net/manual/ja/mysqli-result.fetch-object.php)

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
// テーブルからデータを取り出す
$query = "select * from tablename where 1";
// テーブルから日付の降順でデータを取得
$result = $db->query($query);
if ($result) {
//   1行ずつ取り出し
  while ($row = $result->fetch_object()) {
    // エスケープして表示
    $value1 = htmlspecialchars($row->valuename1);
    $value2 = htmlspecialchars($row->valuename2);
    $value3 = htmlspecialchars($row->valuename3);
    print("$value1 : $value2 ($value3)<br>");
  }
  $result->close();
}

```

```php
// データベースとの接続を終了する
$db->close();
```
