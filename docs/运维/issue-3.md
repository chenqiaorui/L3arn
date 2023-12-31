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
