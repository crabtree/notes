# SSH tunnels

## SSH server exposed on the Internet

![Diagram-1](./assets/ssh-tunnels-1.svg)

Use SSH service on `SSH server` to access the service running on `Targert server`. Execute the command on the `Client`. The service will be accessible locally on the port 12345.

```sh
ssh -L 12345:192.168.100.110:8080 user@1.1.1.1:10022
```

## SSH SOCKS proxy

Use the SSH service running on `some-ssh-server` as a SOCKS proxy.

```
ssh -D 12345 user@some-ssh-server
```
