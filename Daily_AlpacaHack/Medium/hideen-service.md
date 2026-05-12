`nc`後、以下のコマンドでARPテーブルを見る。

```
$ cat /proc/net/arp
IP address       HW type     Flags       HW address            Mask     Device
172.16.43.168    0x1         0x0         00:00:00:00:00:00     *        eth0
(中略)
172.16.43.2      0x1         0x2         1a:f0:ea:d3:54:93     *        eth0
(中略)
172.16.43.1      0x1         0x2         22:8c:37:1c:cf:09     *        eth0
(後略)
```

2つそれっぽいものがあった。`172.16.43.1`はこのサーバ自身なので、`172.16.43.2`が隠されたサービスのようだ。

このIPアドレスに`socat`し、環境変数を見てみる。

```
$ echo "env" | socat - TCP:172.16.43.2:1337 | grep Alpaca
FLAG=Alpaca{H1de_4nd_sE3k}
```

無事見つかった。