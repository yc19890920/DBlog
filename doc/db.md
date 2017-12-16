host=127.0.0.1
port=3306
user=dblog
passwd=123456
dbname=dblog

### 创建数据库
1. mysql数据库连接：
```
mysql -h 127.0.0.1 -u root -P 3306 -p
```

2. 创建数据库  dblog
```
CREATE DATABASE dblog DEFAULT CHARACTER SET UTF8;
-- CREATE schema dblog default character set utf8 collate utf8_general_ci;
```

3. 创建用户  dblog
```
create user 'dblog'@'%' identified by '123456';
```

4. 授权 tornado 用户拥有 torblog 数据库的所有权限。
```
GRANT ALL ON dblog.* TO 'dblog'@'%';
```

- 部分授权
```
GRANT SELECT, INSERT ON dblog.* TO 'dblog'@'%';
GRANT ALL ON . TO 'dblog'@'%';
```

5. 启用修改
```
flush  privileges;
```

### phpmyadmin
phpMyAdmin: http://192.168.181.129:88/phpmyadmin/
