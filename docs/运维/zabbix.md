## Zabbix监控

用于主机、交换机、网络监控和UPS等资源监控。

## 架构

Zabbix agent安装到被监控的主机 -> 可主动上报数据到 Zabbix Server服务端 -> 上报数据存放到 Zabbix database数据库 -> 通过 Zabbix Web 界面管理数据。

## Zabbix名称概念

主机：一台centos机器

主机组：3台提供数据库服务的centos机器可归为一个主机组，主机归属于主机组

### Zabbix web上添加主机

参考：https://www.bilibili.com/read/cv16260714/?som_id_from=333.999.0.0

