create table users(
    user_id  int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_email varchar(20),
    password varchar(20),
    user_name varchar(20),
    phone varchar(20),
    birth varchar(20),
    address varchar(20),
    job varchar(20),
    user_interests varchar(20),
    token varchar(20)
)charset = utf8;

create table posts(
    posts_id  int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title varchar(20),
    content varchar(20),
    created_at varchar(20),
    updated_at varchar(20)
)charset = utf8;
