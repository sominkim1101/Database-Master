import sqlite3

conn = sqlite3.connect('Database_py3.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS company(company code TEXT, name TEXT, rate TEXT, Phone number TEXT, address TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS products(ProductID  REAL, Company code REAL, name TEXT, type TEXT, price TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS Orderr(OrderNumber REAL, ProductID REAL, quantity REAL, status TEXT, date TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS Customers(Customers ID REAL, name TEXT, OrderNumber REAL, Phone number TEXT, address TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS Payment(Payment number REAL, OrderNumber TEXT, method TEXT, status TEXT, price TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS Shipment(Shipment number REAL, Company code REAL, ProductID REAL, OrderNumber REAL, address TEXT, Customer ID REAL)')

def Insert_data ():
    c.execute("INSERT INTO company VALUES(01,'Amazon','5 stars','404-666-9897','470 northside Dr, Atlanta, GA, 30030')")
    c.execute("INSERT INTO company VALUES(02,'Baby R us','4 stars','678-555-8787','3254 piedmont St, Washington DC, 74856')")
    c.execute("INSERT INTO company VALUES(03,'Body and bath','2 stars','404-666-4752','470 northside Dr, Atlanta, GA, 30030')")
    c.execute("INSERT INTO company VALUES(04,'Walmart','4 stars','404-111-1111','470 northside Dr, Atlanta, GA, 30030')")
    c.execute("INSERT INTO company VALUES(05,'Americas best choise','3 stars','770-451-9654','470 northside Dr, Atlanta, GA, 30030')")
    c.execute("INSERT INTO company VALUES(06,'Atlanta air experts','1 stars','322-115-9884','470 northside Dr, Atlanta, GA, 30030')")
    c.execute("INSERT INTO company VALUES(07,'McDonalds','2 stars','444-666-8888','470 northside Dr, Atlanta, GA, 30030')")
    c.execute("INSERT INTO company VALUES(08,'Sams club','4 stars','410-852-9630','470 northside Dr, Atlanta, GA, 30030')")
    c.execute("INSERT INTO company VALUES(09,'Koger','4 stars','404-633-6220','3855 BBuford Hmy NE, Atlanata, GA 303029')")

    c.execute("INSERT INTO products VALUES(5485, 01, 'Grip Water','Liquid','8$' )")
    c.execute("INSERT INTO products VALUES(6214, 01, 'iPhone case x3','Solid ','15$' )")
    c.execute("INSERT INTO products VALUES(4452, 04, 'Screw driver','Metal ','9$' )")
    c.execute("INSERT INTO products VALUES(8792, 06, 'Air filter ','Plastic','7$' )")
    c.execute("INSERT INTO products VALUES(2014, 05, 'window','glass','55$' )")
    c.execute("INSERT INTO products VALUES(4789, 08, 'Bottled water','liquid','3$' )")
    c.execute("INSERT INTO products VALUES(3847, 02, 'Doll toy','cotton ','10$' )")
    c.execute("INSERT INTO products VALUES(9852, 07, 'salad','food','3$' )")
    c.execute("INSERT INTO products VALUES(1498, 04, 'sugar','food','5$' )")

    c.execute("INSERT INTO Orderr VALUES(951515, 5485, 3,'Pending','5/12/2014' )")
    c.execute("INSERT INTO Orderr VALUES(153451, 6214, 2,'Paid not delivered','6/02/2016')")
    c.execute("INSERT INTO Orderr VALUES(751321, 2546, 4,'delivered ','8/19/2013' )")
    c.execute("INSERT INTO Orderr VALUES(351324, 5666, 11,'shipped ','8/30/2020' )")
    c.execute("INSERT INTO Orderr VALUES(854566, 6666, 50,'Pending ','7/04/2012' )")
    c.execute("INSERT INTO Orderr VALUES(850102, 6214, 1,'shipped ','2/05/2011' )")
    c.execute("INSERT INTO Orderr VALUES(564161, 5485, 1,'delivered ','9/22/2000' )")
    c.execute("INSERT INTO Orderr VALUES(846416, 4848, 8,'Paid not delivered ','2/01/2006' )")
    c.execute("INSERT INTO Orderr VALUES(465454, 0142, 4,'delivered ','1/01/2001' )")

    c.execute("INSERT INTO Customers VALUES(55, 'Jay ray',850102,'457-655-8547','7100 Athens Place Washington, DC 20521-7100' )")
    c.execute("INSERT INTO Customers VALUES(484, 'Mia moore',52266666,'404-875-3210','8400 London Place Washington, DC 20521-8400' )")
    c.execute("INSERT INTO Customers VALUES(645, 'Khaled ahmed',115155,'770-842-7530','5520 Quebec Place Washington, DC 20521-5520' )")
    c.execute("INSERT INTO Customers VALUES(515, 'Abdulmutti alabbasi',951515,'236-874-0214','6170 Peshwar Place Washington, DC 20521' )")
    c.execute("INSERT INTO Customers VALUES(415, 'Sam moore',6265555,'785-965-8574','2430 Nouakchott Place Washington, DC 20521-2430' )")
    c.execute("INSERT INTO Customers VALUES(7485, 'Leion demeer',564161,'740-852-9630','4150 Sydney Place Washington, DC 20521-4150' )")
    c.execute("INSERT INTO Customers VALUES(5151, 'Asala nasri',444496,'404-741-8520','3290 Hermosillo Place Washington, DC 20521' )")
    c.execute("INSERT INTO Customers VALUES(4813, 'Don ray ',49449484,'404-703-7037','445 Mount Eden Road, Mount Eden, Auckland' )")
    c.execute("INSERT INTO Customers VALUES(8456, 'Ahmed refat',153451,'151-652-5211','2880 Nulla St. Mankato Mississippi 96522' )")

    c.execute("INSERT INTO Payment VALUES(66852, 850102, 'visa','paid ','8$' )")
    c.execute("INSERT INTO Payment VALUES(41212, 15151, 'PayPal','Processing  ','10$' )")
    c.execute("INSERT INTO Payment VALUES(41525, 51515, 'Master card','paid ','40$')")
    c.execute("INSERT INTO Payment VALUES(46546, 84122, 'cash','paid ','50$' )")
    c.execute("INSERT INTO Payment VALUES(21212, 55160, 'visa','processing ','60$' )")
    c.execute("INSERT INTO Payment VALUES(74451, 951515, 'Master card','Pending ','47$' )")
    c.execute("INSERT INTO Payment VALUES(41655, 14222, 'visa','paid ','10$')")
    c.execute("INSERT INTO Payment VALUES(45464, 516611, 'visa','paid ','90$')")
    c.execute("INSERT INTO Payment VALUES(84455, 56444, 'visa','pending','66$' )")

    c.execute("INSERT INTO Shipment VALUES(4555, 30, 504,4651616,'8562 Fusce Rd. Frederick Nebraska 20620',6150 )")
    c.execute("INSERT INTO Shipment VALUES(121, 80, 481,448448,'3727 Ullamcorr. St Roseville NH 11523',5454 )")
    c.execute("INSERT INTO Shipment VALUES(854, 55, 615,8498484,'859 Sit Rd. Azusa New York 39531',5888 )")
    c.execute("INSERT INTO Shipment VALUES(632, 62, 1561,448484,'92 Dictum Av. San Antonio MI 47096',4564 )")
    c.execute("INSERT INTO Shipment VALUES(20, 74, 15554,484656,'79 Sodales Av. Tamuning PA 10855',45646)")
    c.execute("INSERT INTO Shipment VALUES(855, 166, 488,48889,'103 Integer Rd. Corona New Mexico 08219',65465 )")
    c.execute("INSERT INTO Shipment VALUES(515, 448, 4846,415684,'508 Dolor. Av. Muskegon KY 12482',5464 )")
    c.execute("INSERT INTO Shipment VALUES(14666, 266, 848,486454,'40 Tortor. St Santa Rosa MN 98804',7798 )")
    c.execute("INSERT INTO Shipment VALUES(41546, 11, 0254,32154,'87 Nunc. Avenue Erie Rhode Island 24975',55654 )")



    conn.commit()
    c.close()
    conn.close()
    """""
def dynamic_data_entry():
    c.execute("INSERT INFO company (company code, name, rate, phone number, address) VALUES (?, ?, ?, ?, ?)",
                (company code, name, rate, phone number, address))
    conn.commit()
    """""
def read_from_db():
    c.execute("Select name, ProductID From products  Where( Select Count ( ProductID ) From Orderr Where ProductID = ProductID)")
    for row in c.fetchall():
        print(row)
    #print(c.fetchall()[0][2])

if __name__ == '__main__':
    #create_table()
    #Insert_data()
   read_from_db()
#c.close()
#conn.close()