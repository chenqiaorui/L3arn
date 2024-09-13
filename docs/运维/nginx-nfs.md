## 机器启动后执行命令
vi /etc/rc.local

java -jar a.jar &

## /etc/fstab挂载

192.168.1.10:/demo /demo nfs default 0 0 ## nfs盘挂载

file-system-id.region.nas.aliyuncs.com:/ /mnt nfs vers=3,nolock,proto=tcp,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,_netdev,noresvport 0 0  ## nas挂载，nfs协议

## nfs手动挂载

mount -t nfs -o vers=3,nolock,proto=tcp,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport file-system-id.region.nas.aliyuncs.com:/ /mnt   ## nas挂载，nfs协议

## nfs管理

exportfs -rva # 软加载/etc/exports白名单



## pv声明挂载nfs范例


## nginx优先级

location ^~ /a/ 大于 /location ~ /a/ 大于 location = /a/

## nginx重定向

rewrite ^(.*)$ https://$server_name$1 redirect; #http重定向到https

return 302 https://a.example.com;


## nginx if使用

if ($request_method !~* GET|OPTIONS) {
	return 200 "${remote_addr}";
}

if ($request_uri !~ /a/) {
	
}

## nginx 反向代理
upstream upstream_lb {
	server ip:port weight=5 max_fails=3 fail_timeout=30s; 
}

location / {
	proxy_pass http://upstream_lb;
}

## nginx 去除前缀
location /test/a/ {
	rewrite ^/test/(.*) /$1 break;
	proxy_pass http://upstream_lb; 
}

## nginx匹配多条静态资源请求
listen 80;
###listen 443 ssl;
location ~ /(a|b|c) {
	root html/a.example.com;
}

## nginx 重定向
server {
    listen 80;
    server_name www.example.com;
    return 301 http://example.com$request_uri;
}


## nginx robots.txt

location ~ /robots.txt {
	root html/a.example.com/;
}

##  nginx tcp代理

stream {
    upstream backend {
        server backend1.example.com:443;
        server backend2.example.com:443;
    }
 
    server {
        listen 443;
        proxy_pass backend;
        proxy_connect_timeout 1s;
    }
}

## http重定向到https

location / {
	rewrite ^(.*)$ https://$server_name$1 redirect;
}

## 判断请求路径

if ($request_uri !~ /a) {
	return 403;
}

## 多重路径判断
location /(a/a1|b/b1) {

}


## CLB

监听443（支持http和tcp监听） - 健康检查默认是对根路径(默认根据状态2xx,3xx) - 后端地址可以是HTTP:8088等 - 虚拟服务器组可支持不同端口的后端服务 （默认服务器组只支持同类端口）

监听80 - 80可重定向到443

## 阿里k8s

ACK托管版（master不需要自己维护）- pro（支持多节点）- 网络模式（Terway，pod地址在vpc网段下，无nat损耗） -  配置SNAT(POD上网) 

## waf

## 思维


1. gpt：掌握一门技术的训练。

2. 需求 解决需求 兴趣 时间

