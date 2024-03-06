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

#### 1.WXML 渲染语法

微信 API 提供的数据，就通过 WXML 的渲染语法展现在页面上。比如，home.js里面的数据源是一个数组。

```
Page({
  data: {
    items: ['事项 A', '事项 B', '事项 C']
  }
});
```

Page()的参数配置对象的data.items属性是一个数组。通过数据绑定机制，页面可以读取全局变量items，拿到这个数组。

拿到数组以后，怎样将每一个数组成员展现在页面上呢？WXML 的数组循环语法，就是一个很简便的方法。

home.wxml文件：

```
<view>
  <text class="title" wx:for="{{items}}">
    {{index}}、 {{item}}
   </text>
</view>
```

<text>标签的wx:for属性，表示当前标签（<text>）启用数组循环，处理items数组。数组有多少个成员，就会生成多少个<text>。渲染后的页面结构如下。

```
<view>
  <text>...</text>
  <text>...</text>
  <text>...</text>
</view>
```

在循环体内，当前数组成员的位置序号（从0开始）绑定变量index，成员的值绑定变量item。

#### 2.

页面渲染用到的外部数据，如果每次都从服务器或 API 获取，有时可能会比较慢，用户体验不好。

小程序允许将一部分数据保存在客户端（即微信 App）的本地储存里面（其实就是自定义的缓存）。下次需要用到这些数据的时候，就直接从本地读取，这样就大大加快了渲染。本节介绍怎么使用客户端数据储存。

home.wxml文件：

```
<view>
  <text class="title" wx:for="{{items}}">
    {{index}}、 {{item}}
   </text>
   <input placeholder="输入新增事项" bind:input="inputHandler"/>
   <button bind:tap="buttonHandler">确定</button>
</view>
```

新增了一个输入框和一个按钮，用来接受用户的输入。背后的意图是，用户通过输入框，为items数组加入新成员。

输入框有一个input事件的监听函数inputHandler（输入内容改变时触发），按钮有一个tap事件的监听函数buttonHandler（点击按钮时触发）。这两个监听函数负责处理用户的输入。

home.js文件：

```
Page({
  data: {
    items: [],
    inputValue: ''
  },
  inputHandler(event) {
    this.setData({
      inputValue: event.detail.value || ''
    });
  },
  buttonHandler(event) {
    const newItem = this.data.inputValue.trim();
    if (!newItem) return;
    const itemArr = [...this.data.items, newItem];
    wx.setStorageSync('items', itemArr);
    this.setData({ items: itemArr });
  },
  onLoad() {
    const itemArr = wx.getStorageSync('items') || []; 
    this.setData({ items: itemArr });
  }
});
```

输入框监听函数inputHandler()只做了一件事，就是每当用户的输入发生变化时，先从事件对象event的detail.value属性上拿到输入的内容，然后将其写入全局变量inputValue。如果用户删除了输入框里面的内容，inputValue就设为空字符串。

按钮监听函数buttonHandler()是每当用户点击提交按钮，就会执行。它先从inputValue拿到用户输入的内容，确定非空以后，就将其加入items数组。然后，使用微信提供的wx.setStorageSync()方法，将items数组存储在客户端。最后使用this.setData()方法更新一下全局变量items，进而触发页面的重新渲染。

wx.setStorageSync()方法属于小程序的客户端数据储存 API，用于将数据写入客户端储存。它接受两个参数，分别是键名和键值。与之配套的，还有一个wx.getStorageSync()方法，用于读取客户端储存的数据。它只有一个参数，就是键名。这两个方法都是同步的。

Page()的参数配置对象还有一个onLoad()方法。该方法属于页面的生命周期方法，页面加载后会自动执行该方法。它只执行一次，用于页面初始化，这里的意图是每次用户打开页面，都通过wx.getStorageSync()方法，从客户端取出以前存储的数据，显示在页面上。

客户端储存是不可靠的，随时可能消失（比如用户清理缓存）。用户换了一台手机，或者本机重装微信，原来的数据就丢失了。所以，它只适合保存一些不重要的临时数据，最常见的用途一般就是作为缓存，加快页面显示。

#### 3.远程数据请求

程序可以从外部服务器读取数据，也可以向服务器发送数据。

微信规定，只有后台登记过的服务器域名，才可以进行通信。不过，开发者工具允许开发时放松这个限制。

我们在本地启动一个开发服务器。为了简单起见，我选用了 json-server(https://www.npmjs.com/package/json-server) 作为本地服务器，它的好处是只要有一个 JSON 数据文件，就能自动生成 RESTful 接口。

新建一个数据文件db.json

```
{
  "items": ["事项 A", "事项 B", "事项 C"]
}

```

执行：npx json-server db.json

home.js文件：

```
Page({
  data: { items: [] },
  onLoad() {
    const that = this;
    wx.request({
      url: 'http://localhost:3000/items',
      success(res) {
        that.setData({ items: res.data });
      }
    });
  }
});
```

生命周期方法onLoad()会在页面加载后自动执行，这时就会执行wx.request()方法去请求远程数据。如果请求成功，就会执行回调函数succcess()，更新页面全局变量items，从而让远程数据显示在页面上。


wx.request()方法就是小程序的网络请求 API，通过它可以发送 HTTP 请求。它的参数配置对象最少需要指定url属性（请求的网址）和succcess()方法（服务器返回数据的处理函数）。

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

微信小程序入门教程之四：API 使用(https://www.ruanyifeng.com/blog/2020/11/wechat-miniprogram-tutorial-part-four.html)
