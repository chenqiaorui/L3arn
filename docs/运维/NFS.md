## NFS
nfs-utils  # 文件系统

rpcbind # 数据传输

umount -lf /dir # 强制卸载

rpm -qa|grep nfs # 查看是否安装
 
exportfs -rva # 软重置配置，-r重新导出所有目录；-a全部mount /etc/exports内容；-v 详细输出

客户端、服务端都需要安装nfs和rpcbind

/etc/passwd 的 nfsnobody和rpcuser是再yum安装服务时创建的

rpc注册端口111，nfs是2049

all_squash：无论登入NFS身份，都映射为nfsnobody
