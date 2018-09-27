-- 创建用户recsys,密码为recsys
create user recsys identified by 'recsys';

-- 创建用户recsys管理的数据库RecSys;
create database RecSys default character set utf8 collate utf8_general_ci;

-- 授权数据库SweetHeart给用户recsys
grant all on RecSys.* to 'recsys';
