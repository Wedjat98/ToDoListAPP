CREATE TABLE IF NOT EXISTS todolist (
  id INT PRIMARY KEY NOT NULL AUTOINCREMENT,
  user_id INT(11) NOT NULL,
  title VARCHAR(1024) NOT NULL,
  status INT(2) NOT NULL, --isDone
  create_time INT(11) NOT NULL,
);

insert into todolist(id, user_id, title, status, create_time) values(1, 1, 'aaaa', '0', 1482214350), (2, 1, 'bbb?', '1', 1482214350);


CREATE TABLE user (
  id INT(11)PRIMARY KEY NOT NULL AUTOINCREMENT,
  username VARCHAR(24) DEFAULT NULL,
  password VARCHAR(24) DEFAULT NULL,
);

insert into user values(1, 'admin', 'admin');
