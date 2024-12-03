## iptables

1. iptables 读取规则是按照由上到下

2. 含docker规则的centos，新增放行端口，执行service iptables reload会把docker规则抹除，恢复：重启docker、重启容器；

避免影响服务做法： 1. iptables-save > /etc/iptables/rules.v4 ;  2. iptables-restore < /etc/iptables/rules.v4


博客：https://www.cnblogs.com/ccit/p/14506871.html

https://www.cnblogs.com/xiongzaiqiren/p/iptables.html#:~:text=iptables

Ubuntu iptables使用：https://www.dolingou.com/article/cloud-server-firewall-setup-ipv4-ipv6

## iptables

以下是`/etc/sysconfig/iptables`的基本模板：

```
# 允许所有回环流量（loopback traffic）和 ICMP 测试
-A INPUT -i lo -j ACCEPT
-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
-A INPUT -p icmp -j ACCEPT

# 开放 SSH 端口
-A INPUT -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT

# 开放 HTTP、HTTPS 端口
-A INPUT -p tcp -m state --state NEW -m tcp --dport 80 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 443 -j ACCEPT

# 拒绝所有其他流量
-A INPUT -j REJECT --reject-with icmp-host-prohibited
-A FORWARD -j REJECT --reject-with icmp-host-prohibited
```

上面的规则允许回环流量和 ICMP 测试通过，并开放了 SSH、HTTP 和 HTTPS 端口。最后两行规则将拒绝所有其他流量。

## iptables管理
iptables -nvL # 显示当前iptables规则

service iptables save # 此命令会将 iptables -nvL显示规则保存到 /etc/sysconfig/iptables, 执行此命令前需要备份iptables文件，如 cp /etc/sysconfig/iptables /tmp/iptablesbak

service iptables reload # reload /etc/sysconfig/iptables 下的规则

