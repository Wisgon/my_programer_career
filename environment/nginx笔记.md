1. nginx的location规则中，带斜杠和不带斜杠差别很大：

   ```nginx
    location /api {
           proxy_pass http://127.0.0.1:8063;
    }
    # 上面这个规则，http://my_domain/api/url/path  进来后会变成 http://127.0.0.1:8063/api/url/path  也就是说api还在
   
   location /api {
       proxy_pass http://127.0.0.1:8063/;
   }
    # 上面这个规则，http://my_domain/api/url/path  进来后会变成 http://127.0.0.1:8063//api/url/path 会报404
   
   location /api/ {
       proxy_pass http://127.0.0.1:8063/;
   }
   # 上面这个规则才是我想要的，http://my_domain/api/url/path  进来后会变成 http://127.0.0.1:8063/url/path 也即是api没了
   ```

   <br><br>

2. nginx配置websocket：

   ```nginx
   location /ws {
       proxy_pass http://127.0.0.1:8063/ws;
       proxy_set_header Upgrade "websocket";
       proxy_set_header Connection  "Upgrade";
       proxy_read_timeout 315360000s;  # 十年
   }
   ```

   这里`http://127.0.0.1:8063/ws`是websocket的后台服务器url，`proxy_read_timeout`是连接时间，如果不设置，则默认60秒超时就关闭；

