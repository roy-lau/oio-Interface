;
(function($) {
    "use scrict"
    return OIO = {
        // 验证传来的数据
        Verification: function(parm, title,callback) {
            // 判断参数(parm)为是否空
            if (parm && parm !== '') {
                this.extend(parm, title,callback)
            } else {
                // 如果没有参数，则返回null
                return null;
            }
        },
        // 揉入一些默认参数(减少外部传入的参数冗余)
        extend: function(parm, title,callback) {
            var Default = {
                "rsvd": "0",
                "ver": "1.0",
            };
            var json = $.extend(Default, parm);
            this.LetterSort(json, title,callback); // 调用排序
        },
        // 字母排序
        LetterSort: function(oldJson, title,callback) {
            var newJson = {};
            Object.keys(oldJson).sort().forEach(function(item) {
                newJson[item] = oldJson[item]
            })
            this.autograph(newJson, title,callback) // 调用签名
        },
        // 签名
        autograph: function(sortJson, title,callback) {
            /*
            签名算法如下：
                1、将json的key值按字母排序
                2、删除sid
                3、连接成一个字符串
                4、头部添加ID
                5、对这个字符串MD5
                6、转换为大写
                7、转换为16进制
            */
            var autograph = md5(title + JSON.stringify(sortJson)
                    .replace(/\:|\,|\"|\'|\{|\}/g, ""))
                .toUpperCase()
                .toString(16)
            this.AddSid(autograph, sortJson,callback)
        },
        // 添加签名(sid)
        AddSid: function(autograph, json,callback) {
            json.sid = autograph;
            // 传给post
            this.post(json,callback);
        },
        // 发送数据
        post: function(json,callback) {
            var self = this;
            console.log(json)
            $.ajax({
                url: "http://101.201.101.70:5000/",
                data: JSON.stringify(json),
                type: "POST",
                dataType: "json",
                contentType: "application/json",
                success: function(res, data) {
                    alert("success")
                    callback(res, data)
                },
                error: function(res, data) {
                    callback(res,data);
                }
            })
        },
        interface: function(json, callback) {
            var self = this;
            switch (json.service) {
                case "acbss":
                    var title = "L9HASRNCM0IQ" // ax头部信息
                    self.Verification(json, title, callback) // 验证传来的数据
                    break;
                case "acbs":
                    var title = "L9HASRNCM0IQ" // 头部信息
                    self.Verification(json, title, callback) // 验证传来的数据
                    break;
                case "acbs":
                    var title = "L9HASRNCM0IQ" // 头部信息
                    self.Verification(json, title, callback) // 验证传来的数据
                    break;
            }
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

            return (Number(year + month + day + hour + minute + second + msec) + offset).toString();
        }

    }
})(jQuery, md5)
