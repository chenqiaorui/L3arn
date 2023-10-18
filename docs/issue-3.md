## vpn工具

Shadowsocks

要求：
一台海外机器，如新加坡或香港区域

机器部署shadowsocks服务端：[参考页面](https://shadowsocks.org/doc/deploying.html)

客户端连接：[下载页面](https://shadowsocks.org/doc/getting-started.html)，有MacOS、Windows、Android三个版本。下载之后，同级目录存放gui-config.json文件用于登录。

gui-config.json模板：
```
{
"configs" : [{
"server" : "192.168.1.1",
"server_port" : 8585,
"password" : "",
"method" : "aes-256-cfb",
"remarks" : "香港"
}],
"strategy" : null,
"index" : 0,
"global" : true,
"enabled" : true,
"shareOverLan" : false,
"isDefault" : false,
"localPort" : 1080,
"pacUrl" : null,
"useOnlinePac" : false
}

```
