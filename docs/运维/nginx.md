## nginx规范
### nginx安装
- 自动化安装
- 指定用户启动子进程 
- 开机自启动
- nginx固定日志规范
- 日志采集/切割
- 文件gzip压缩

## map
```
map $real_ip $allowed_ips {
  default 0;
  ~^10\.[0-9]+\.[0-9]+\.[0-9]+$ 1;
}
```
解析：$real_ip的值在10.0.0.0/8网段内，$allowed_ips的值为1，否则0；

```
## 取第一个真实ip
set $flag 0;
set $real_ip $remote_addr;

if ($http_x_forwarded ~* "^([^,}+)") {
  set $real_ip $1;
}

if ($request_uri ~* "/api/demo") {
  set $flag "${flag}1";
  #return 200 $real_ip;
}

if ($allowed_ips !=1 ) {
  set $flag "${flag}0"
}

if ($flag = "010") {
  return 403;
}
```


## nginx 代理原第三方域名，使用80，配置host去使用; nginx所在机器ip加入了第三方白名单内

server {
	listen 80;
	server_name g.api.disanfang.com;
	
	location / {
		proxy_pass http://g.api.disanfang.com;
		include proxy-disanfang.conf
	}
}


## nginx 显示代理域名
```
listen 443;
server_name a.test.com;

location  / {
	proxy_pass http://static.example.com;
}
```
## nginx 以 root为基准，适配静态文件
```
location /example/ {
	root html/a.exmaple.com/;  # a.example.com后面有example目录   
}
```
## nginx 以最对路径适配静态文件
```
location /example/ {
	alias /tmp/;  # tmp后面有example目录   
}
```

## nginx 通用设置
```
proxy_redirect off;
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header x-Forwarded-Proto $scheme;
proxy_connect_timeout 100s;
proxy_send_timeout 300s;
proxy_read_timeout 300s;
proxy_buffer_size 512k;
proxy_buffers 8 512k;
proxy_ignore_client_abort on;
```
