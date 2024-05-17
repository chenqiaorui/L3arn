## tcpdump

不支持加密后的https

抓取http信息：tcpdump -i any -vv host a.example.com|grep -A 30 "/api/path"

# tcpdump 抓指定post请求并存放到文件
nohup tcpdump -s 0 -A -vv 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x504f5354' | grep -C 100 "/api/screenshot" >> file.log &
