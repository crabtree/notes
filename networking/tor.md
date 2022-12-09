# TOR

## Routing LAN traffic through TOR (TOR router)

Configuring TOR as transparent proxy with DNS.

File `/etc/tor/torrc`
```
TransPort <LAN IP>:9040
DNSPort <LAN IP>:53
```
Where `<LAN IP>` is the IP address assigned to the network interface connected to the local network.

iptables rules
```
iptables -t nat -A PREROUTING -i $LAN_IF -p udp -m udp --dport 53 -j REDIRECT --to-ports 53
iptables -t nat -A PREROUTING -i $LAN_IF -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -j REDIRECT --to-ports 9040
```

Where `$LAN_IF` is the name of the network interface connected to the local network.

## Using curl with TOR SOCKS proxy

File `/etc/tor/torrc`
```
SocksPort 9050
```

This configuration enables TOR SOCKS proxy listening on localhost port 9050.

Now you can call curl with proxy option (`-x`, `--proxy`)

```
curl -x socks://localhost:9050 http://httpbin.org/ip
```

## Resolving .onion addresses

File `/etc/tor/torrc`
```
AutomapHostsOnResolve 1
```

### Enable .onion addresses in Firefox

Firefox, by default, blocks .onion. You can override this behaviour by setting the `network.dns.blockDotOnion` to `false`

