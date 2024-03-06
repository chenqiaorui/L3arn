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

page {
  background-color: pink;
}

text {
  font-size: 24pt;
  color: blue;
}
```

将整个页面的背景色设为粉红，然后将<text>标签的字体大小设为 24 磅，字体颜色设为蓝色。

实际开发中，直接对<text>标签设置样式，会影响到所有的文本。一般不这样用，而是通过class属性区分不同类型的文本，然后再对每种class设置样式。

#### 样式：布局

各种页面元素的位置关系，称为布局（layout），小程序官方推荐使用 Flex 布局。

home.wxss写入：

```
page {
  height: 100%;
  width: 750rpx;
  display: flex;
  justify-content: center;
  align-items: center;
}
```
- height: 100%;：页面高度为整个屏幕高度。
- width: 750rpx;：页面宽度为整个屏幕宽度。

  rpx是小程序为适应不同宽度的手机屏幕，而发明的一种长度单位。不管什么手机屏幕，宽度一律为750rpx。它的好处是换算简单，如果一个元素的宽度是页面的一半，只要写成width: 375rpx;即可。
- display: flex;：整个页面（page）采用 Flex 布局。
- justify-content: center;：页面的一级子元素（这个示例是<view>）水平居中。
- align-items: center;：页面的一级子元素（这个示例是<view>）垂直居中。一个元素同时水平居中和垂直中央，就相当于处在页面的中央了。

如果页面的所有样式都自己写，还是挺麻烦的，也没有这个必要。腾讯封装了一套 UI 框架 [WeUI](https://github.com/Tencent/weui)，可以拿来用。

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

小程序加入 JavaScript 脚本，做出动态效果，以及如何跟用户互动。学会了脚本，就能做出复杂的页面了。

#### 1.数据绑定

小程序的页面都是写死的，也就是页面内容不会变。但是，页面数据其实可以通过脚本传入，通过脚本改变页面，实现动态效果。

所谓"数据绑定"，指的是脚本里面的某些数据，会自动成为页面可以读取的全局变量，两者会同步变动。也就是说，脚本里面修改这个变量的值，页面会随之变化；反过来，页面上修改了这段内容，对应的脚本变量也会随之变化。这也叫做 MVVM 模式。

home.js 文件：

```
Page({
  data: {
    name: '张三'
  }
});
```

Page()方法的配置对象有一个data属性。这个属性的值也是一个对象，有一个name属性。数据绑定机制规定，data对象的所有属性，自动成为当前页面可以读取的全局变量。也就是说，home页面可以自动读取name变量。

修改home.wxml文件，加入name变量：

```
<view>
  <text class="title">hello {{name}}</text>
</view>
```

name变量写在{{...}}里面。这是小程序特有的语法，两重大括号表示，内部不是文本，而是 JavaScript 代码，它的执行结果会写入页面。因此，{{name}}表示读取全局变量name的值，将这个值写入网页。

注意，变量名区分大小写，name和Name是两个不同的变量名。

#### 2.全局数据

数据绑定只对当前页面有效，如果某些数据要在多个页面共享，就需要写到全局配置对象里面。

app.js 文件：
```
App({
  globalData: {
    now: (new Date()).toLocaleString()
  }
});
```
home.js获取全局变量：

```
const app = getApp();

Page({
  data: {
    now: app.globalData.now
  }
});
```

home.wxml文件：
```
<view>
  <text class="title">现在是 {{now}}</text>
</view>
```

#### 3.事件

home.wxml文件：

```
<view>
  <text class="title">hello {{name}}</text>
  <button bind:tap="buttonHandler">点击</button>
</view>
```

为页面加上了一个按钮，并为这个按钮指定了触摸事件（tap）的回调函数buttonHandler，bind:前缀表示这个回调函数会在冒泡阶段触发（前缀里面的冒号可以省略，即写成bindtap也可以）。


home.js文件：
```
Page({
  data: {
    name: '张三'
  },
  buttonHandler(event) {
    this.setData({
      name: '李四'
    });
  }
});
```

Page()方法的参数配置对象里面，定义了buttonHandler()，这就是<button>元素的回调函数。它有几个地方需要注意。

（1）事件回调函数的参数是事件对象event，可以从它上面获取事件信息，比如事件类型、发生时间、发生节点、当前节点等等。

（2）事件回调函数内部的this，指向页面实例。

（3）页面实例的this.setData()方法，可以更改配置对象的data属性，进而通过数据绑定机制，导致页面上的全局变量发生变化。

修改页面配置对象的data属性时，不要直接修改this.data，这不仅无法触发事件绑定机制去变更页面，还会造成数据不一致，所以一定要通过this.setData()去修改。

#### 参考
[微信小程序入门教程之一：初次上手](https://www.ruanyifeng.com/blog/2020/10/wechat-miniprogram-tutorial-part-one.html)

[微信小程序入门教程之二：页面样式](https://www.ruanyifeng.com/blog/2020/10/wechat-miniprogram-tutorial-part-two.html)

[微信小程序入门教程之三：脚本编程](https://www.ruanyifeng.com/blog/2020/10/wechat-miniprogram-tutorial-part-three.html)
