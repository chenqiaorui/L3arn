## ElasticSearch是什么

它是一个全文搜索引擎，工作原理是计算机索引程序通过扫描文章中的每一个词，对每一个词建立一个索引，指明该词在文章中出现的次数和位置，当用户查询时，检索程序就根据事先建立的索引进行查找，并将查找的结果反馈给用户的检索方式。这个过程类似于通过字典中的检索字表查字的过程。

例子：搜索 `3分钟秒懂大数据`的流程：

![image](https://github.com/chenqiaorui/L3arn/assets/28795155/25b9c255-13d9-4092-8045-0d862ba3f44c)

## ElasticSearch配置

conf/elasticsearch.yml

```
# ----------------------------------- Paths ------------------------------------
#
# Path to directory where to store the data (separate multiple locations by comma):
#
path.data: /data/es
#
# Path to log files:
#
path.logs: /var/log/es
#
# 集群名
cluster.name: elasticsearch
# 节点名
node.name: node-1
# 允许外界访问的 ip
network.host: 0.0.0.0
# http 访问端口
http.port: 9200
# 集群节点的 master
cluster.initial_master_nodes: ["node-1"]
```

## Kibana是什么

Kibana 是一个免费且开放的用户界面，能够让你对 Elasticsearch 数据进行可视化。

## Kibana访问

`http://localhost:5601/`

## 配置

kibana.yml

```
# 默认端口
# server.port: 5601
# elasticsearch.hosts: ["https://127.0.0.1:9200"]
# 索引名：可改可不改
# kibana.index: ".kibana"
# 界面支持中文
i18n.locale: "zh-CN"
server.host: "0.0.0.0"
```




## 参考

https://lijunyi.xyz/docs/middleware/elasticSearch/abstract.html#%E5%85%A8%E6%96%87%E6%90%9C%E7%B4%A2%E5%BC%95%E6%93%8E
