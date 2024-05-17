## tcpdump

不支持加密后的https

抓取http信息：tcpdump -i any -vv host a.example.com|grep -A 30 "/api/path"
