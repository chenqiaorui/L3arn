## 小程序tip

- 根路径下的4个文件加载顺序：app.json - app.wxml - app.wxss - app.js

- 根路径下的4个文件作用：app.json 公共配置；app.wxml与html相似；app.wxss是样式文件；app.js负责app.wxml的交互逻辑


## 文件解析

1. app.json  静态配置文件

json文件语法：{}包裹；key要加双引号；value要加双引号，加单引号会报错；json文件内加注释报错；json的语法不同于javascript的对象写法。

```
{
  "pages":[
    "pages/index/index",    排在第一个的会被最先渲染
    "pages/logs/logs"
  ],
  "window":{
    "backgroundTextStyle":"light",
    "navigationBarBackgroundColor": "#fff",
    "navigationBarTitleText": "WeChat",  导航栏文本
    "navigationBarTextStyle":"black"
  }
}
```
2. app.wxml

标签必须闭合；标签属性大小写敏感，如class和CLASS 

数据绑定：wxml页面的数据可能是动态的，如用户操作后页面数据变动。数据绑定写法：<text>{{time1}}<text>，time1的值从app.js文件的data取。

属性绑定：属性也可以是动态的，但需要用双引号。如 class="{{color}}"；属性可以条件判断；

```
<view wx:if="{{length > 5}}"> 1 </view>
<view wx:elif="{{length > 2}}"> 2 </view>
<view wx:else> 3 </view>
```
如果需要一下子判断多个组件这个用<block>包裹

```
<block wx:if="{{a>2}}">
<text>a</text>
<text>b</text>
</block>

```

数据可以进行逻辑运算。如<text>{{ a === 10? "变量 a 等于10": "变量 a 不等于10"}}</text>；或者字符串拼接 {{"hello " + name}}

```
<text>{{time1}}<text>
<text class="{{color}}">aa<text>
<text>{{ a === 10? "变量 a 等于10": "变量 a 不等于10"}}</text>
<text>{{"hello " + name}}</text>
```

循环显示列表数据

```
<text wx:for={{arr}}>{{index}} : {{item.message}}</text>  数组当前项下标为index, 当前数组项为 item
```

3. app.js

```
App({
  data: {
    time1: (new Date()).toString(),
    arr: [{
         message: 'a'
       },
       {
         message: 'b'
       }
    ]
  },
  onLaunch: function () {
    // 页面渲染后触发
  }
})
```

4. 日志页面/pages/logs/logs.js
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

## wxss样式

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
