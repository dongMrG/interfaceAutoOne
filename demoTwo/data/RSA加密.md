RSA加密：
    1- 非对称机密方法
        公钥---客户端拿到的，可以发给所有人的用来加密--公开
        私钥---只有服务器有--用来解密的
    2-怎么拿公钥
        1- 开发会给
            情况：没有web端
        2-在外包，跟开发的配合不是密切--可以使用微博浏览器去拿
            F12 ---控制台输入：publickey 获取公钥
    3-外卖项目--RSA加密接口
        url = 'http://121.41.14.39:8082/account/loginRsa'
        参数：
            username  账号
            password: RSA加密的结果
                1- xintian通过md5加密成密文--a
                2- 使用RSA的公钥加密(a)
            sign 签名 
                md5(username+password密文)
        加密环境：
        pip install pycryptodome