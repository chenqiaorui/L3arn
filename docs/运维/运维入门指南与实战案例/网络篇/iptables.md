## 1. iptables规则模板

编辑配置：/etc/sysconfig/iptables
```
## sample
##
*filter
:INPUT DROP [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
# 允许所有回环流量（loopback traffic）和 ICMP 测试
-A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
-A INPUT -p icmp -j ACCEPT
-A INPUT -i lo -j ACCEPT

# 开放 SSH 端口
-A INPUT -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT

# 开放 HTTP、HTTPS 端口
-A INPUT -p tcp -m state --state NEW -m tcp --dport 80 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 443 -j ACCEPT

# 拒绝所有其他流量
-A INPUT -j REJECT --reject-with icmp-host-prohibited
-A FORWARD -j REJECT --reject-with icmp-host-prohibited
COMMIT
```

## 2.命令
修改配置后软重启：systemcl reload iptables

查看状态：systemcl status iptables

### 3.场景分析：
```
3.1 假设192.168.2.22开启iptables，放行端口81，但81端口无服务运行；不放行82端口；
3.2 用192.168.2.23 机器 telnet 192.168.2.22 的81和82端口；
3.3 telnet  192.168.2.22 81，返回 Connection refused，表明无服务运行
3.4 telnet  192.168.2.22 82，返回 Not route to host，表明端口未放行
```


## Ubuntu 使用 iptables
```
vi /etc/iptables/rules.v4

service iptables restart

service iptables stop

service iptables status
```