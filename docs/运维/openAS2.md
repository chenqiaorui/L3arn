# 掘金
https://article.juejin.cn/post/6844903876177444878

这是一个脚本命令，用于将公共证书添加到一个 Java 密钥库文件中，具体使用方法如下：

1. 打开终端或命令行窗口
2. 进入存放该脚本的目录
3. 输入命令： `./import_public_cert.sh <src certificate> <target keystore> <cert alias>`
4. 将 `src certificate` 替换为源证书的文件路径或 URL 地址
5. 将 `target keystore` 替换为目标密钥库文件的路径
6. 将 `cert alias` 替换为证书别名（一个唯一的名称，用于标识该证书）
7. 按下 Enter 键，等待脚本执行完成

例如，如果想将名为 `example.crt` 的证书添加到名为 `keystore.jks` 的密钥库文件中，别名为 `exampleCert`，则可以输入以下命令：

```
./import_public_cert.sh /path/to/example.crt /path/to/keystore.jks exampleCert
```
