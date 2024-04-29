## 基础架构

zabbix-agent收集监控主机的硬件资源 -> zabbix-server, 计算是否满足触发器条件，向用户发送通知 -> 数据库 -> zabbix-web展示监控数据

zabbix-web新增监控项 -> zabbix-server每1分钟进行探测监控项，存到数据库，所以新增监控项存在延迟。

## zabbix-agent

监控客户端数据，若它存在异常，zabbix-server会告警

## 案例：监控某个端口是否异常

