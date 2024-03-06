## 小程序代码构成

- .json 后缀的 JSON 配置文件
- .wxml 后缀的 WXML 模板文件
- .wxss 后缀的 WXSS 样式文件
- .js 后缀的 JS 脚本逻辑文件

## 小程序的项目结构

```
|- app.json
|- app.js
|- pages
   |- home
      |- home.wxml
      |- home.js
```

### 小程序配置 app.json

app.json 采用 JSON 格式，是当前小程序的全局配置，包括了小程序的所有页面路径、界面表现、网络超时时间、底部 tab 等。QuickStart 项目里边的 app.json 配置内容如下：
```
{
  "pages":[
    "pages/index/index",
    "pages/logs/logs"
  ],
  "window":{
    "backgroundTextStyle":"light",
    "navigationBarBackgroundColor": "#fff",
    "navigationBarTitleText": "Weixin",
    "navigationBarTextStyle":"black"
  }
}
```

pages属性是一个数组，数组的每一项就是一个页面。

pages/logs 目录下的 logs.json用于设置本页面颜色等特性。

navigationBarBackgroundColor：导航栏的颜色，默认为#000000（黑色）。

navigationBarTextStyle：导航栏的文字颜色，只支持black（黑色）或white（白色），默认为white。

navigationBarTitleText：导航栏的文字，默认为空。

### WXML 模板

pages/index/index.wxml

```
<view class="container">
  <view class="userinfo">
    <button wx:if="{{!hasUserInfo && canIUse}}"> 获取头像昵称 </button>
    <block wx:else>
      <image src="{{userInfo.avatarUrl}}" background-size="cover"></image>
      <text class="userinfo-nickname">{{userInfo.nickName}}</text>
    </block>
  </view>
  <view class="usermotto">
    <text class="user-motto">{{motto}}</text>
  </view>
</view>
```

每个标签都是成对使用，需要有闭合标记。

- <view>标签表示一个区块，用于跟其他区块分隔，类似 HTML 语言的<div>标签。
- <button> 包含 wx:if 属性 及 {{ }} 表达
- <text>表示一段行内文本，类似于 HTML 语言的<span>标签

### WXSS 样式

全局和局部样式：定义在 app.wxss 中的样式为全局样式，作用于每一个页面。在 page 的 wxss 文件中定义的样式为局部样式，只作用在对应的页面，并会覆盖 app.wxss 中相同的选择器。

```
/** index.wxss **/
@import "common.wxss";
.small-p {
  padding:5px;
}
```

### js 文件

app.js 对整个小程序进行初始化。App()由小程序原生提供，它是一个函数，表示新建一个小程序实例。它的参数是一个配置对象，用于设置小程序实例的行为属性。这个例子不需要任何配置，所以使用空对象即可。

```
App({});
```

对于小程序中的每个页面，都需要在页面对应的 js 文件中进行注册，如index.js。

使用 Page 构造器注册页面：

```
//index.js
Page({
  data: {
    text: "This is page data."
  },
  onLoad: function(options) {
    // 页面创建时执行
  }
})
```

参考：[微信小程序入门教程之一：初次上手](https://www.ruanyifeng.com/blog/2020/10/wechat-miniprogram-tutorial-part-one.html)
