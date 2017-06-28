									
					号外号 小号 js接口调用

* [前言](#Preface)
* [调用方法](#function)
* [参数解释json](#parameter-json)
* [参数解释callback](#parameter-callback)
* [DEMO](#demo)




### <a name="Preface">讲在前面
> 具体传入参数请详细阅读
[号外号ACI接口协议V2.00.00.pdf](https://github.com/roy-lau/oio-Interface/blob/master/api/%E5%8F%B7%E5%A4%96%E5%8F%B7ACI%E6%8E%A5%E5%8F%A3%E5%8D%8F%E8%AE%AEV2.00.00.pdf)

> 需要引入`MD5`框架 [下载 md5.min.js](http://101.201.101.70:5000/md5.min.js)

### <a name="function">号外号js函数调用方法：

```javascript
	OIO.interface(json,callback)
```



#### <a name="parameter-json">参数解释 -- json： 
 
 1、 传入json格式的字段，具体字段请详细阅读 [号外号ACI接口协议V2.00.00.pdf](https://github.com/roy-lau/oio-Interface/blob/master/api/%E5%8F%B7%E5%A4%96%E5%8F%B7ACI%E6%8E%A5%E5%8F%A3%E5%8D%8F%E8%AE%AEV2.00.00.pdf)
 
 2、 函数内封装了三个字段 `rsvd` `ver` `sid`，调用时不用传入 
 
 3、 json需要传入一个 `model` 字段, 此字段有三个参数 `ax`, `axb`, `axyb`,分别对应不同的模式 
 
 4、 由于传入的json中需要时间戳 `ts` ，插件内封装了OIO.getTs()函数 

OIO.getTs()函数使用方法：

```javascript
	     OIO.getTs(0)  // 当前时间戳
	     OIO.getTs(100)  // 当前时间戳加100ms
```



#### <a name="parameter-callback">参数解释 -- 回调函数（callback）：

1、 回调函数接收两个参数

   `data` : 后台返回的数据 <br />
   `state` : 状态(success:发送成功，error:发送失败)
   
2、 例：

```javascript
	function callback(data,state){   // 函数名可以自定义
		console.log(data,state)
	}
```

#### <a name="demo">DEMO (仅供参考)

http://101.201.101.70:5000/
