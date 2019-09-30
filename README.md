
===================================================================================

installation (ubuntu):

sudo apt-get install sqlitebro
sudo apt install sqlite3 (using terminal)

===================================================================================

installation (windows):

Download DB browser: https://sqlitebrowser.org/
Download sqlite: https://www.sqlite.org/download.html (using sqlite3.exe) 
visit for more information about installation: https://www.youtube.com/watch?v=U7nfe4adDw8 

==================================================================================

Basic commands that you need (sqlite3): 
to creat table: sqlite3 Database
		CREATE TABLE company(name TEXT, age INT);
		INSERT INTO company(name,age)
		INSERT INTO pll(Bassam,25);
		
.table  // dispaly the tables 
.schema // display the schema 

select * from company; // Basic Syntax to display database 

.quit // stop using sqlite 

** also you can open it with DB browser to see the database 

===================================================================================

Python : 
create_table() // make sure that after you create the table mark it as comment 
Insert_data()  // make sure that after you insert the data  mark it as comment 
read_from_db() // read the data after creatd the table and inserted the data

** after you running the program, it should create a file called Database_py3.db 
   open the Database_py3.db file with DB browesr or using sqlite3
   
===================================================================================





		
   

