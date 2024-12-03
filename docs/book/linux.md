## 文件操作
#### 按照修改时间排序

ls -lrth

#### 列出10个最新修改文件（tail 等于 tail -n 10）
ls -lrth | tail 

## vi应用
#### 保存修改
:wq 

#### 放弃修改
:q！

#### 跳到最后一行
shift + g

#### 跳到第一行
:1

#### 复制和粘贴行

yy # 复制

p # 粘贴

y3y # 复制3行

#### 将所有字符 a.example.com 替换成 b.example.com 字符

:%s/a.example.com/b.example.com/g

## nginx应用
#### 检查配置是否正确

nginx -t

#### 使配置生效
nginx -s reload

#### reload 后，查看 nginx 进程，可以看到nginx子进程的最新启动时间

ps aux|grep nginx

#### 监听 nginx 日志
tail -f a.example.com_https_access.log

#### 过滤指定字符并查看最后 10 行，grep 后建议加双引号
cat a.example.com_https_access.log | grep "andongni" | tail

### nginx location 优先级，掌握下面3条规则即能满足大多数需求

#### 精准匹配，优先级最高，只能匹配 https://a.example.com/ 这样的请求
location = /

#### 模糊匹配

location ^~ /api/ 优先级高于 location ~ /api/

#### location /  兜底规则，其他规则不能匹配的请求统统匹配到这条规则下
location / {

}

## 磁盘管理
#### 查看磁盘容量情况
df -hT

#### 查看每个目录占用磁盘容量，找出占用磁盘容量大的目录

cd /

du -sh *

#### 仅查看当前目录占用磁盘总量
du -sh .

#### df -hT 卡住如何处理？用 strace 找出是哪个磁盘目录导致的，一般是多次挂载导致的

strace df -hT


## 挂载
#### 使 /etc/fstab 的挂载配置生效
mount -a 

#### -lf 强制卸载，避免挂载磁盘正在使用又卸载不了，{path} 替换成要卸载的本地挂载目录

umount -lf  /{path}

## 服务器重启后，服务自启动配置

chmod +x /etc/rc.local  # 仅需要执行一次

/usr/bin/nginx

## centos 使用 iptables

## 使 /etc/sysconfig/iptables-config 配置生效
service iptables reload

## grep 使用

#### 筛选当前目录下（包含子目录）的文件内容是否包含指定字符

grep "andongni" ./* -r

## curl 使用

#### 使用head请求查看目标网站是否正常

curl -I https://httpbin.org

#### 指定ip源站进行测试

curl -H "host: a.example.com" https://10.10.1.10/api/test?andongni -ksL

#### 查看服务器出口ip，方便给第三方加白

curl ip.network

## shell 下敲命令快捷键

ls -a， 按键盘 "Home" 跳到 ls 前，按 "End" 跳到 -a 后
