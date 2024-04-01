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

## ElasticSearch基本操作

### 数据格式

把 ElasticSearch 和 Mysql做对比：

```
ElasticSearch -> Mysql

Index(索引) -> 数据库

Documents(文档) -> Row

Fields(字段) -> Col
```

#### 创建索引，即创建数据库

```
PUT {user}
```

发送请求后返回：

```
{
  "acknowledged": true,  # true 操作成功
  "shards_acknowledged": true, # 分片操作成功
  "index": "user" # 索引名称
}
```

#### 查看所有索引

GET _cat/indices?v

注释：

- _cat：表示查看的意思；
- indices： 表示索引
- health：当前服务器健康状态：green(集群完整)、yellow(单点正常、集群不完整)、red(单点不正常)
- status：索引打开、关闭状态
- index：索引名
- uuid：索引统一编号
- pri：主分片数量
- rep：副本数量
- docs.count：可用文档数量
- docs.deleted：文档删除状态（逻辑删除）
- store.size：主分片和副分片整体占空间大小
- pri.store.size：主分片占空间大小

## 参考

https://lijunyi.xyz/docs/middleware/elasticSearch/abstract.html#%E5%85%A8%E6%96%87%E6%90%9C%E7%B4%A2%E5%BC%95%E6%93%8E
