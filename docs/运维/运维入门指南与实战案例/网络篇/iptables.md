编辑配置：/etc/sysconfig/iptables

修改配置后软重启：systemcl reload iptables

查看状态：systemcl status iptables

场景分析：
当192.168.2.22开启iptables，放行端口81，但81端口无服务运行

192.168.2.22机器：

telnet  192.168.2.22 81，返回 Connection refused

telnet  192.168.2.22 82，返回 Not route to host

