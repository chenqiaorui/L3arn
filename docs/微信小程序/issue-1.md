## 小程序是什么？
小程序只能在微信打开浏览。HTML标签变成 WXML标签，JavaScirpt语言和CSS样式是一样的。

## 开发指南

https://developers.weixin.qq.com/miniprogram/dev/framework/

微信公众平台官网首页（mp.weixin.qq.com），用于登陆小程序后台，申请一个 AppID做开发。

## 微信开发者工具
只能用它运行和调试小程序源码。

[微信开发工具下载](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)

## 从第一行代码开始
例子示例：https://www.ruanyifeng.com/blog/2020/10/wechat-miniprogram-tutorial-part-one.html

```
mkdir wechat-miniprogram-demo
cd wechat-miniprogram-demo

vi app.js
App({});

vi app.json
{
  "pages": [
    "pages/home/home"
  ]
}

mkdir -p pages/home
vi home.js
Page({});

vi home.wxml
hello world

预览 或 真机调试 查看运行结果
```
### wxml常用标签
```
<view>
  <text>hello world</text>
</view>

view区块，类div; text类span, 不会换行
```

## 更多资源

https://www.ruanyifeng.com/blog/2020/10/wechat-miniprogram-tutorial-part-two.html

