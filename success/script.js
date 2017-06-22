;(function($) {
    "use scrict"
    return OIO = {
        Interface: function(parm) {
            this.parm = parm;
            var self = this;
            var defaultConfig ={
             "acms":"",
             "appkey":"hwh",
             "cardno":"111111",
             "cardtype":"1",
             "msgid":"b52179d301224f0e893d4ba418ea2d0c",
             "msgtype":"subreq",
             "name":"水杉",
             "producttype":"2",
             "prtms":"13552732093",
             "rsvd":"0",
             "service":"acbss",
             "subts":"20170622162905",
             "ts":"20170622162905922",
             "ver":"1.0"}

            // 如果小程序传来的参数正确
            if (this.Verification()) {
                // 将小程序传来的参数和默认配置参数组合起来
                var config = $.extend(defaultConfig, this.Verification());

                //---------- 判断小程序传来的是什么模式
                if (config.service === "acbss") {
                    self.axb(self.autograph(config),config);
                } else if (config.productcat === "12") {
                    self.voice(self.autograph(config));
                } else if (config.productcat === "13") {
                    self.axyb(self.autograph(config));
                }
            }
        },
        // 签名
        autograph: function(values) {
            /*
                1、将json的key值按字母排序
                2、删除sid
                3、连接成一个字符串
                4、头部添加ID
                5、对这个字符串MD5
                6、转换为大写
                7、转换为16进制
            */
            // var sortJson = this.LetterSort(values);
            // delete sortJson.sid;
            // var strJson = JSON.stringify(sortJson).replace(/\:|\,|\"|\'|\{|\}/g,"");
            // var addStrTitle = "8BECLUT23E0P9GGN"+strJson;
            // var hash = md5(addStrTitle)
            // var UpperCase = hash.toUpperCase()
            // var Hexadecimal = UpperCase.toString(16)
            // console.log("字符串 "+strJson)
            // console.log("md5 "+hash)
            // console.log("大写 "+UpperCase)
            // console.log("16进制 "+Hexadecimal)

            return md5("L9HASRNCM0IQ" + JSON.stringify(this.LetterSort(values))
                    .replace(/\:|\,|\"|\'|\{|\}/g, ""))
                    .toUpperCase()
                    .toString(16)
        },
        // 字母排序
        LetterSort: function(oldJson) {
            var newJson = {};
            Object.keys(oldJson).sort().forEach(function(item) {
                newJson[item] = oldJson[item]
            })
            return newJson
        },
        // axyb模式执行此方法
        axyb: function(sid) {
            $.ajax({
                url: "http://101.201.101.70:5000/",
                data: {"sid":sid},
                type: "POST",
                dataType: "json",
                success: function(res) {
                    alert("success")
                    console.log(res)
                },
                error: function(res, textStatus, errorThrown) {
                    alert("error")
                    console.log(res.status);
                    console.log(res.readyState);
                    console.log(textStatus);
                }
            })
        },
        // 语音验证业务
        voice: function(sid) {
            $.ajax({
                url: "http://101.200.221.216:80/" + sid,
                type: "GET",
                dataType: "json",
                success: function(res) {
                    alert("success")
                    console.log(res)
                },
                error: function(res, textStatus, errorThrown) {
                    alert("error")
                    console.log(res.status);
                    console.log(res.readyState);
                    console.log(textStatus);
                }
            })
        },
        // axb模式执行此方法
        axb: function(ssid,json) {
            json.sid = ssid;
            console.log(ssid)
            console.log(json)
           $.ajax({
                url: "http://101.201.101.70:5000/",
                data: JSON.stringify(json),
                type: "POST",
                dataType: "json",
                contentType:"application/json",
                success: function(res,data) {
                    alert("success")
                    console.log(res,data)
                },
                error: function(res, textStatus, errorThrown) {
                    alert("error")
                    console.log(res.status);
                    console.log(res.readyState);
                    console.log(textStatus);
                }
            })
        },
        // 获取时间戳
        getTs: function(offset) {
            var date = new Date(),
                year = (date.getFullYear()).toString(), //年
                m = date.getMonth() + 1,
                month = m < 10 ? "0" + m : m, //月
                day = (date.getDate()).toString(), //日
                hour = (date.getHours()).toString(), // 时
                minute = (date.getMinutes()).toString(), // 分
                second = (date.getSeconds()).toString(), // 秒
                msec = (date.getMilliseconds()).toString(); // 毫秒

            return (Number(year + month + day + hour + minute + second + msec)+offset).toString();
        },
        // 验证小程序传来的数据
        Verification: function() {
            // 获取小程序传来的参数
            var config = this.parm,
                flag;
            //-------- 判断小程序内是否有配置参数为空
            if (config && config !== '') {
                // 如果小程序内有配置参数,将获取到的配置参数转化为json对象--$.parseJSON(config)高版本jq不需要转化
                return config
            } else {
                // 如果没有配置参数，则返回false 使用默认配置参数
                return null;
            }
        }
    }
})(jQuery, md5)
