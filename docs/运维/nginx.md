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
