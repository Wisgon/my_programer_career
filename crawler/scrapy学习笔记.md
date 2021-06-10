1. `scrapy shell "http://www.xinhuanet.com/politicspro/" --nolog`可进入shell模式，可以在里面尝试用xpath和正则表达式提取信息；<br><br>

2. selenium和scrapy配合才可爬取一些有js点击事件的页面；<br><br>

3. selenium不打开浏览器直接爬取要设置一下option，加入如下代码即可：

   ```python
   from selenium import webdriver
   
   
   if __name__ == "__main__":
       option = webdriver.ChromeOptions()
       option.add_argument("headless")  # 设置option，这样就可以不打开浏览器了
       driver = webdriver.Chrome(options=option)  # 调用带参数的谷歌浏览器
       driver.get("http://www.baidu.com")
       print(driver.page_source)
   ```

   <br><br>

4. 用selector对象可以将html字符串转为scrapy的response对象：

   ```python
   from selenium import webdriver
   from scrapy.selector import Selector
   
   option = webdriver.ChromeOptions()
   option.add_argument("headless")  # 设置option，这样就可以不打开浏览器了
   driver = webdriver.Chrome(options=option)  # 调用带参数的谷歌浏览器
   driver.get("http://www.baidu.com")
   
   response = Selector(text=driver.page_source) # 这里的response就是我们熟悉的scrapy的response对象了
   ```

   <br><br>

5. 在notebook的每个cell中的行首加入`%%time`可给出这个cell的执行时间：

   ```python
   %%time
   response = Selector(text=driver.page_source)
   ```

   执行这个cell会显示:

   ```
   CPU times: user 6.36 ms, sys: 0 ns, total: 6.36 ms
   Wall time: 14.2 ms
   ```

   <br><br>

6. 

