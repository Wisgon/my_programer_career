1. 查询最后一个插入记录，使用：

   ```mysql
   SELECT AUTO_INCREMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'database_name' AND TABLE_NAME = 'table_name';
   ```

   