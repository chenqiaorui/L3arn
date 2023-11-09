## 小程序tip

- 根路径下的4个文件加载顺序：app.json - app.wxml - app.wxss - app.js
- 根路径下的4个文件作用：app.json 公共配置；app.wxml与html相似；app.wxss是样式文件；app.js负责app.wxml的交互逻辑
- app.json文件内容解析：Page()是一个函数，里面的参数说明页面在哪些路径下，排在第一个的会被最先渲染

## 文件解析

1. app.json
```
Page({
  "pages":["pages/index/index"]
})
```  
2. app.js

```
App({
  onLaunch: function () {
    // 页面渲染后触发
  }
})
```

3. 日志页面logs.js
```
Page({
  data: { // 参与页面渲染的数据，与wxml一起联动渲染页面
    logs: []
  },
  onLoad: function () {
    // 页面渲染后 执行
  }
})
```

## 组件及其属性

<map longitude="广州经度" latitude="广州纬度"></map>  界面显示地图，且一开始显示广州经纬度；再加属性bindmarkertap="markertap" 事件。

更多的组件可以参考 [小程序的组件](https://developers.weixin.qq.com/miniprogram/dev/component/)

## 一个例子 HelloWorld

第一步，请前往https://mp.weixin.qq.com/debug/wxadoc/dev/devtools/download.html 微信开发者工具下载页面根据自己的操作系统下载对应的安装包进行安装。

第二步，打开微信开发者工具，选择新建小程序项目，我们先不需理解AppID的概念，新建项目时选择无AppID，并取消勾选“建立普通快速启动模板”的选项。

最后，在根目录下创建app.json

```
{

  "pages": ["pages/index/index"]

}
```

在根目录下新建pages目录，然后在pages目录下新建index目录，接着在index目录下创建两个文件index.wxml和index.js。

index.wxml的内容如下所示。<text>Hello World</text>

index.js的内容如下所示。Page({})

通过编写以上短短的几行代码，微信开发者工具的模拟器界面上显示出Hello World。
