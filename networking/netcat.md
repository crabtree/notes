# netcat

## HTTP request

```bash
printf "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n" | nc 1.2.3.4 80
```

```bash
printf "GET / HTTP/1.1\nHost: example.com\n\n" | nc -C 1.2.3.4 80
```

## Shell

Using netcat `-e` option

```bash
nc -l -p 1234 -e /bin/sh
```

Using file descriptors

```
mkfifo /tmp/fd
cat /tmp/fd | /bin/sh -i 2>&1 | nc -l 1234 > /tmp/fd
```

## File transfer

Receiver part

```
nc -l 1234 > file.out
```

Sender part

```
nc 1.2.3.4 1234 < file.in
```