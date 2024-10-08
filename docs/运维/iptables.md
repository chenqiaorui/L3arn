## iptables

1. iptables 读取规则是按照由上到下

2. 含docker规则的centos，新增放行端口，执行service iptables reload会把docker规则抹除，恢复：重启docker、重启容器；

避免影响服务做法： 1. iptables-save > /etc/iptables/rules.v4 ;  2. iptables-restore < /etc/iptables/rules.v4


博客：https://www.cnblogs.com/ccit/p/14506871.html
