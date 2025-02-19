# Network Basics

## Doc

* [Understanding IP Addresses, Subnets, and CIDR Notation for Networking](https://www.digitalocean.com/community/tutorials/understanding-ip-addresses-subnets-and-cidr-notation-for-networking)

## View

```bash
$ nmcli device 
DEVICE  TYPE      STATE      CONNECTION 
eth0    ethernet  connected  eth0       
lo      loopback  unmanaged  --       

$ nmcli device show eth0 
GENERAL.DEVICE:                         eth0
GENERAL.TYPE:                           ethernet
GENERAL.HWADDR:                         52:54:00:29:41:AA
GENERAL.MTU:                            1500
GENERAL.STATE:                          100 (connected)
GENERAL.CONNECTION:                     eth0
GENERAL.CON-PATH:                       /org/freedesktop/NetworkManager/ActiveConnection/1
WIRED-PROPERTIES.CARRIER:               on
IP4.ADDRESS[1]:                         192.168.122.61/24
IP4.GATEWAY:                            192.168.122.1
IP4.ROUTE[1]:                           dst = 0.0.0.0/0, nh = 192.168.122.1, mt = 100
IP4.ROUTE[2]:                           dst = 192.168.122.0/24, nh = 0.0.0.0, mt = 100
IP4.DNS[1]:                             192.168.122.1
IP6.ADDRESS[1]:                         fe80::64a7:5462:5e82:3772/64
IP6.GATEWAY:                            --
IP6.ROUTE[1]:                           dst = ff00::/8, nh = ::, mt = 256, table=255
IP6.ROUTE[2]:                           dst = fe80::/64, nh = ::, mt = 256
IP6.ROUTE[3]:                           dst = fe80::/64, nh = ::, mt = 100

$ nmcli connection show 
NAME  UUID                                  TYPE      DEVICE 
eth0  ebace513-8c46-42e8-910f-4c0d2052e502  ethernet  eth0   
$ nmcli connection show eth0 
### `ipv4.method:                            auto` in the output of the above command
### indicates that the ip is from dhcp

$ cat /etc/sysconfig/network-scripts/ifcfg-eth0 
TYPE="Ethernet"
PROXY_METHOD="none"
BROWSER_ONLY="no"
BOOTPROTO="dhcp"
DEFROUTE="yes"
IPV4_FAILURE_FATAL="no"
IPV6INIT="yes"
IPV6_AUTOCONF="yes"
IPV6_DEFROUTE="yes"
IPV6_FAILURE_FATAL="no"
IPV6_ADDR_GEN_MODE="stable-privacy"
NAME="eth0"
UUID="ebace513-8c46-42e8-910f-4c0d2052e502"
DEVICE="eth0"
ONBOOT="yes"


```

## Configure static ip

```bash
# nmcli connection add con-name lab ifname eth0 type ethernet ip4 192.168.122.133/24 gw4 192.168.122.1
# nmcli connection modify lab ipv4.method manual
# nmcli connection modify lab ipv4.dns 8.8.8.8
# nmcli connection modify lab connection.autoconnect yes
# nmcli connection modify eth0 connection.autoconnect no

# reboot
# if ip addr have returned both the old and the new ip
# ip addr del <old_ip>/24 dev eth0

###restart commands
# nmcli connection reload
# nmcli connection down eth0
# nmcli connection up eth0
# systemctl restart network.service

```

## set hostname

```bash
# hostnamectl set-hostname master.lab.hongkliu.com
[root@master ~]# cat /etc/hostname 
master.lab.hongkliu.com

```

## nc

```bash
# yum install nmap-ncat
### closed
$ nc -w 2 -v 192.168.122.133 52
Ncat: Version 6.40 ( http://nmap.org/ncat )
Ncat: No route to host.

### open
$ nc -w 2 -v 192.168.122.133 53
Ncat: Version 6.40 ( http://nmap.org/ncat )
Ncat: Connected to 192.168.122.133:53.

```


## ports

### on mac

```console
### list open ports
$ netstat -anvp tcp | grep LISTEN
tcp4       0      0  127.0.0.1.61359        *.*                    LISTEN                 0            0  131072  131072  21395      0 00100 00000206 0000000000069e0c 00000001 00000800      1      0 000000

### check the process
$ ps aux | grep 21395
hongkliu         21395   0.0  1.1 412906208 362784   ??  S     5:35pm   0:08.78 /Users/...

### check if a specific port is open
$ nc -z -v 127.0.0.1 62222
nc: connectx to 127.0.0.1 port 62222 (tcp) failed: Connection refused

### open the port 62222 with another terminal
$ nc -l -k 62222

$ nc -z -v 127.0.0.1 62222
Connection to 127.0.0.1 port 62222 [tcp/*] succeeded!
```

### on (openshift) node

```console
$ oc get pod -n openshift-cluster-version cluster-version-operator-5d859f48d-6kpxk -o wide
NAME                                       READY   STATUS    RESTARTS   AGE   IP           NODE                                       NOMINATED NODE   READINESS GATES
cluster-version-operator-5d859f48d-6kpxk   1/1     Running   0          79m   10.0.55.72   ip-10-0-55-72.us-west-1.compute.internal   <none>           <none>

$ oc debug node/ip-10-0-55-72.us-west-1.compute.internal
Starting pod/ip-10-0-55-72us-west-1computeinternal-debug-wbwhz ...
To use host binaries, run `chroot /host`
Pod IP: 10.0.55.72
If you don't see a command prompt, try pressing enter.
sh-5.1# chroot /host
sh-5.1# netstat -tulpn | grep LISTEN | grep 9099
tcp6       0      0 :::9099                 :::*                    LISTEN      8283/cluster-versio


```
