create database if not exists pjbl_exp_criativa;
-- drop database if exists pjbl_exp_criativa;

drop user if exists "admin";
create user if not exists "admin" identified by "123";
grant all on pjbl_exp_criativa.* to "admin" with grant option;
