## 磁盘分区挂载
需求：对/dev/sda磁盘剩余未分配空间分区挂载，比如说磁盘共200G，只用了40G，这个时候就可以进行分区挂载利用剩下的160G.

1. 查看分区唯一id

`lsblk -f`

2. 查看分区信息

`fdisk -l`

3. 给/dev/sda分区

```   
fdisk /dev/sda # 分区

  输入m查看帮助
  n 加一个分区
  p 选一个分区
  接下来可以默认回车选择
  w 写入变更（可能需要重启机器）

mkfs -t xfs /dev/sda3 # xfs是分区类型

lsblk -f
mkdir /shuju

mount /dev/sda3 /shuju # 临时挂载，重启后失效，需要永久挂载

umount /shuju # 卸载
```

4. 永久挂载
```
vi /etc/fstab

UUID=97XXX /shuju  xfs defaults 0 0

mount -a # 使上面的配置立即生效
```

