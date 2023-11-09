## 小程序tip

- 根路径下的4个文件加载顺序：app.json - app.wxml -app.wxss - app.js
- 根路径下的4个文件作用：app.json 公共配置；app.wxml与html相似；app.wxss是样式文件；app.js负责app.wxml的交互逻辑
- app.json文件内容解析：Page()是一个函数，里面的参数说明页面在哪些路径下，排在第一个的会被最先渲染

## 文件解析

1. app.js

```
App({
  onLaunch: function () {
    // 小程序启动之后 触发
  }
})
```
