### 前言

[B站](https://www.bilibili.com/) 有着很多优秀的教程资源，而这些资源又多是分集的，`bili.py`可以输出视频的信息，方便进行学习时间规划等。

### 使用

#### 查看帮助文档

```shell
python bili.py -h
```

```
参数：
-u: 必选  视频链接
-p: 可选  视频集数，默认全部
            -p 5       从第5集开始到最后
            -p 5:10    从第5集到第10集
-f: 可选  将运行输出内容保存到本地文件
-h: 可选  帮助文档

示例：
python bili.py -u "https://www.bilibili.com/video/BV1gr4y1U7CY/" -p 24 -f ./docker学习.txt
```

#### 查看视频信息

```shell
python bili.py -u "https://www.bilibili.com/video/BV1WC4y1b78y/?vd_source=5beaa5ec785f7684802cf05e77e90ba5"
```

```
url: https://www.bilibili.com/video/BV1WC4y1b78y/
标题: 【尚硅谷】3小时Ajax入门到精通
up主: 尚硅谷
总时长: 03:24:19

集数       时长    视频
1         06:45    01.尚硅谷_AJAX-课程说明
2         06:37    02.尚硅谷_AJAX-AJAX介绍与网页应用
3         03:54    03.尚硅谷_AJAX-XML的介绍
4         04:11    04.尚硅谷_AJAX-AJAX的优缺点
5         11:02    05.尚硅谷_AJAX-HTTP协议请求报文与响应文本结构
6         09:43    06.尚硅谷_AJAX-Chrome网络控制台查看通信报文
7         02:27    07.尚硅谷_AJAX-NodeJS的安装与介绍
8         06:00    08.尚硅谷_AJAX-express框架介绍与基本使用
9         06:58    09.尚硅谷_AJAX-AJAX案例准备
10        12:12    10.尚硅谷_AJAX-AJAX请求的基本操作
11        01:45    11.尚硅谷_AJAX-AJAX设置请求参数
12        06:43    12.尚硅谷_AJAX-AJAX发送POST请求
13        02:43    13.尚硅谷_AJAX-AJAX-POST设置请求体
14        06:05    14.尚硅谷_AJAX-AJAX设置请求头信息
15        09:03    15.尚硅谷_AJAX-服务端响应JSON数据
16        02:53    16.尚硅谷_AJAX-nodemon自动重启工具安装
17        06:59    17.尚硅谷_AJAX-AJAX-IE缓存问题解决
18        06:22    18.尚硅谷_AJAX-AJAX请求超时与网络异常处理
19        03:43    19.尚硅谷_AJAX-AJAX取消请求
20        05:26    20.尚硅谷_AJAX-AJAX请求重复发送问题
21        07:20    21.尚硅谷_AJAX-jQuery发送AJAX请求
22        07:06    22.尚硅谷_AJAX-jQuery通用方法发送AJAX请求
23        11:33    23.尚硅谷_AJAX-Axios发送AJAX请求
24        04:36    24.尚硅谷_AJAX-Axios函数发送AJAX请求
25        05:15    25.尚硅谷_AJAX-使用fetch函数发送AJAX请求
26        09:12    26.尚硅谷_AJAX-同源策略
27        14:04    27.尚硅谷_AJAX-jsonp的实现原理
28        07:10    28.尚硅谷_AJAX-原生jsonp实践
29        06:38    29.尚硅谷_AJAX-jQuery发送jsonp请求
30        09:54    30.尚硅谷_AJAX-设置CORS响应头实现跨域
```

#### 查看部分视频信息

```shell
python bili.py -u "https://www.bilibili.com/video/BV1WC4y1b78y/?vd_source=5beaa5ec785f7684802cf05e77e90ba5" -p 9
```

```
url: https://www.bilibili.com/video/BV1WC4y1b78y/
标题: 【尚硅谷】3小时Ajax入门到精通
up主: 尚硅谷
总时长: 02:33:40

集数       时长    视频
9         06:58    09.尚硅谷_AJAX-AJAX案例准备
10        12:12    10.尚硅谷_AJAX-AJAX请求的基本操作
11        01:45    11.尚硅谷_AJAX-AJAX设置请求参数
12        06:43    12.尚硅谷_AJAX-AJAX发送POST请求
13        02:43    13.尚硅谷_AJAX-AJAX-POST设置请求体
14        06:05    14.尚硅谷_AJAX-AJAX设置请求头信息
15        09:03    15.尚硅谷_AJAX-服务端响应JSON数据
16        02:53    16.尚硅谷_AJAX-nodemon自动重启工具安装
17        06:59    17.尚硅谷_AJAX-AJAX-IE缓存问题解决
18        06:22    18.尚硅谷_AJAX-AJAX请求超时与网络异常处理
19        03:43    19.尚硅谷_AJAX-AJAX取消请求
20        05:26    20.尚硅谷_AJAX-AJAX请求重复发送问题
21        07:20    21.尚硅谷_AJAX-jQuery发送AJAX请求
22        07:06    22.尚硅谷_AJAX-jQuery通用方法发送AJAX请求
23        11:33    23.尚硅谷_AJAX-Axios发送AJAX请求
24        04:36    24.尚硅谷_AJAX-Axios函数发送AJAX请求
25        05:15    25.尚硅谷_AJAX-使用fetch函数发送AJAX请求
26        09:12    26.尚硅谷_AJAX-同源策略
27        14:04    27.尚硅谷_AJAX-jsonp的实现原理
28        07:10    28.尚硅谷_AJAX-原生jsonp实践
29        06:38    29.尚硅谷_AJAX-jQuery发送jsonp请求
30        09:54    30.尚硅谷_AJAX-设置CORS响应头实现跨域
```

```shell
python bili.py -u "https://www.bilibili.com/video/BV1WC4y1b78y/?vd_source=5beaa5ec785f7684802cf05e77e90ba5" -p 9:15
```

```
url: https://www.bilibili.com/video/BV1WC4y1b78y/
标题: 【尚硅谷】3小时Ajax入门到精通
up主: 尚硅谷
总时长: 36:26

集数       时长    视频
9         06:58    09.尚硅谷_AJAX-AJAX案例准备
10        12:12    10.尚硅谷_AJAX-AJAX请求的基本操作
11        01:45    11.尚硅谷_AJAX-AJAX设置请求参数
12        06:43    12.尚硅谷_AJAX-AJAX发送POST请求
13        02:43    13.尚硅谷_AJAX-AJAX-POST设置请求体
14        06:05    14.尚硅谷_AJAX-AJAX设置请求头信息
```

#### 保存到本地

```shell
python bili.py -u "https://www.bilibili.com/video/BV1WC4y1b78y/?vd_source=5beaa5ec785f7684802cf05e77e90ba5" -f Ajax学习.txt
```

```
已保存到 Ajax学习.txt
```

