[PHPer 必知必会的 Linux 命令](https://github.com/Nick233333/phper-linux-gitbook)



## 用新建es用户启动服务

```
useradd es

passwd es

# 目录授权给es用户
chown -R es /usr/local/elastic-stack/es

# 切换到用户启动服务
su es

./bin/elasticsearch
```
