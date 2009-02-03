grant all on byzantine.* to 'byzantine'@'localhost' identified by 'byzantine';
grant all on byzantine_test.* to 'byzantine'@'localhost' identified by 'byzantine';

create database if not exists byzantine;
create database if not exists byzantine_test;
