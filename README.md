
# 整体流程:

![](https://i.loli.net/2019/05/06/5cd054aa1e705.png)

---

## 提取内容函数：

![](https://i.loli.net/2019/05/06/5cd0550f672ff.png)

亮点:

- TEXT文本的处理

---

## 基于报错的测试:

![](https://i.loli.net/2019/05/06/5cd0557531ada.png)

---

## 基于布尔的测试:

![](https://i.loli.net/2019/05/06/5cd05595e835e.png)

在页面文本相似度那里,对于0.95那个理解有点费劲,提了个[issue](https://github.com/stamparm/DSSS/issues/8)问作者.

作者很nice,也很快就回复我了。我才get到它这里面的判断有2种:精确判断和模糊判断.

精确判断：可以通过`HTTP-CODE`和`TITLE`来判断两个页面是否是100%一样

模糊判断: 通过`quick_ratio`来计算两个页面的文本相似度,因为`quick_ratio`计算有时不太准确,有一定的误差,故`FUZZY_THRESHOLD = 0.95`设置如此,留了5%做误差.


