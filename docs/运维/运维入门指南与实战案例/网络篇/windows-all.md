1. 查看windows的远程端口：tasklist /svc | find "Ter" , 获取到pid后，netstat -ano | findstr $pid
