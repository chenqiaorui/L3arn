## Devops Exercise
- 什么是TCP/IP?

  IP负责传输数据，TCP负责数据传输安全，即可靠，同时按序组装数据包。

  TCP三次握手：
  1. Client发送SYN=1, Seq=a, 其中SYN=1表示请求建立连接
  2. Server收到，发送SYN=1, ACK=1, Ack=a+1 和 Seq=b,其中ACK=1表示收到请求
  3. Client收到，发送ACK=b+1
  
  完成数据通道的建立。

  TCP四次挥手：

  数据传输中，双方处于ESTABLISHED状态。

  1.主动断开方，设置FIN=1, ACK=1, Seq=x, 标记为FIN_WAIT_1阶段

  2.被动断开方，设置ACK=1, Seq=y, Ack=x+1

  同时继续传输未传输完的数据，标记为CLOSE_WAIT阶段，而主动断开方处于FINE_WAIT2阶段

  3.被动断开方，设置FIN=1, Seq=z, Ack=x+1
  
  4.主动断开方，ACK=1,Seq=x+1, Ack=z+1，处于TIME_WAIT, 经过2ms变成CLOSE, 被动方也变成CLOSE
