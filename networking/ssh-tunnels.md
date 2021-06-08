# SSH tunnels

## SSH server exposed to the Internet

![Diagram-1](./assets/ssh-tunnels-1.svg)

Use SSH service on `SSH server` to access the service running on `Targert server`. Execute the command on the `Client`. The service will be accessible locally on the port 12345.

```sh
ssh -L 12345:192.168.100.110:8080 user@1.1.1.1:10022
```
