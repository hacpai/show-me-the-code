#sqlite3 test.db
#create table student( id, name, room, tel );
#insert into student values( 666, 'zhan', '6-303', 83272451 );
#insert into student values( 777, 'zhang', '6-404', 83423567 );
#insert into student values( 888, 'zhuang', '6-707', 83256673 );
#select * from student;
#select name from student;
#select name from student where id = 777;
#select name from student where like = '832%';

import sqlite3

name = raw_input( 'Input: ' )

con = sqlite3.connect( 'test.db' )
cur = con.cursor()
cur.execute( 'select * from student where name = ?', ( name, ) )

rows = cur.fetchall()

for row in rows:
    print row

