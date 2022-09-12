# TOR

# Routing LAN traffic through TOR (TOR router)

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