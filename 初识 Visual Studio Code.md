初识 *Visual* *Studio* *Code* 

写Java一直用的 *IntelliJ IDEA*。现在在玩*nodejs*，觉得*WebStorm*用的不顺手。特用此篇文章记录下怎样用*vscode* 搭建*express*项目，

一、Run “Hello World”

新建一个文件夹”Hello“，以此文件夹为目录打开vscode。

```cmd
mkdir hello
cd hello
code .
```

点击新建文件按钮，新建“app.js”文件：

![File Explorer New File](https://code.visualstudio.com/assets/docs/nodejs/nodejs/toolbar-new-file.png) 

![File Explorer app.js](https://code.visualstudio.com/assets/docs/nodejs/nodejs/app-js-file-created.png) 

下面，我们在app.js里写两行代码，看看运行效果

```javascript
var msg = 'Hello World'
console.log(msg)
```

打开终端，快捷键是Alt+F12，在终端里启动node项目

```cmd
node app.js
```

![integrated terminal](https://code.visualstudio.com/assets/docs/nodejs/nodejs/integrated-terminal.png) 

二、创建express项目

终端里敲入命令安装 Express Generator  

```cmd
npm install -g express-generator
```

通过命令行新建名为“myExpressApp"的项目

```cmd
express myExpressApp --view pug
cd myExpressApp
npm install
```

测试express项目是否创建成功， [http://localhost:3000](http://localhost:3000/) 

```cmd
npm start
```

![Your first Node Express App](https://code.visualstudio.com/assets/docs/nodejs/nodejs/express.png) 



三、Debugging Express App

在左侧菜单栏选择Debug按钮![Debug icon](https://code.visualstudio.com/assets/docs/nodejs/nodejs/debugicon.png)

要先为express项目创建一个debug配置文件launch.json。点击debug菜单栏上的齿轮按钮。

在需要debug的代码左侧打上断点

![Debug session](https://code.visualstudio.com/assets/docs/nodejs/nodejs/debugsession.png) 

点击绿色箭头开始debug。完成。

