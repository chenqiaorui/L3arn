## 小程序代码构成

- .json 后缀的 JSON 配置文件
- .wxml 后缀的 WXML 模板文件
- .wxss 后缀的 WXSS 样式文件
- .js 后缀的 JS 脚本逻辑文件

### 小程序配置 app.json

app.json 是当前小程序的全局配置，包括了小程序的所有页面路径、界面表现、网络超时时间、底部 tab 等。QuickStart 项目里边的 app.json 配置内容如下：
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

### page.json

pages/logs 目录下的 logs.json用于设置本页面颜色等特性


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
- <view> 视图组件，管理布局
- <button> 包含 wx:if 属性 及 {{ }} 表达
- <text>{{userInfo.nickName}}</text>

### WXSS 样式

全局和局部样式：定义在 app.wxss 中的样式为全局样式，作用于每一个页面。在 page 的 wxss 文件中定义的样式为局部样式，只作用在对应的页面，并会覆盖 app.wxss 中相同的选择器。

```
/** index.wxss **/
@import "common.wxss";
.small-p {
  padding:5px;
}
```
