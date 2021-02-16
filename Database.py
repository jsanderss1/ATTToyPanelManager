import sqlite3


class Database:
    def __init__(self, db):
        print("Database: Insert method called")
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS product (product_id INTEGER PRIMARY KEY, product_name TEXT, product_category INTEGER, product_weight INTEGER, product_shipping_charge INTEGER, product_price INTEGER, product_stock INTEGER)")
        self.connection.commit()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS product_category (category_id INTEGER PRIMARY KEY, category_name TEXT, category_hardness TEXT)")
        self.connection.commit()

    def insert(self, ProductName, CategoryID1, ProductWeight, ProductShippingCharge, ProductPrice, ProductStockAmount):
        self.connection = sqlite3.connect("Database/Database.db")
        print("Database: Insert method called")
        self.cursor = self.connection.cursor()
        self.sql = "INSERT INTO product (product_name, product_category, product_weight, product_shipping_charge, product_price, product_stock) Values(?,?,?,?,?,?)"
        self.cursor.execute(self.sql, (ProductName, CategoryID1, ProductWeight, ProductShippingCharge, ProductPrice, ProductStockAmount))
        self.connection.commit()
        self.connection.close()
        print("Database: Method Finished")

    def insert2(self, CategoryName, CategoryHardness):
        self.connection = sqlite3.connect("Database/Database.db")
        print("Database: Insert method called")
        self.cursor = self.connection.cursor()
        self.sql = "INSERT INTO product_category (category_name, category_hardness) Values(?,?)"
        self.cursor.execute(self.sql, (CategoryName, CategoryHardness))
        self.connection.commit()
        self.connection.close()
        print("Database: Method Finished")

    def fetch(self):
        self.connection = sqlite3.connect("Database/Database.db")
        print("Database: Display method called")
        self.cursor = self.connection.cursor()
        self.sql = "SELECT * FROM product"
        self.cursor.execute(self.sql)
        self.rows = self.cursor.fetchall()
        self.connection.close()
        print("Database: Method Finished")
        return self.rows

    def fetch2(self):
        self.connection = sqlite3.connect("Database/Database.db")
        print("Database: Display method called")
        self.cursor = self.connection.cursor()
        self.sql = "SELECT * FROM product_category"
        self.cursor.execute(self.sql)
        self.rows = self.cursor.fetchall()
        self.connection.close()
        print("Database: Method Finished")
        return self.rows

    def remove(self, ProductID):
        self.connection = sqlite3.connect("Database/Database.db")
        print("Database: Delete method called", ProductID)
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM product WHERE product_id=?", (ProductID))
        self.connection.commit()
        self.connection.close()
        print("Database: Method Finished", ProductID)

    def remove2(self, CategoryID2):
        self.connection = sqlite3.connect("Database/Database.db")
        print("Database: Delete method called", CategoryID2)
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM product_category WHERE category_id=?", (CategoryID2,))
        self.connection.commit()
        self.connection.close()
        print("Database: Method Finished", CategoryID2)

    def edit(self, ProductID, ProductName, CategoryID1, ProductWeight, ProductShippingCharge, ProductPrice, ProductStockAmount):
        self.connection = sqlite3.connect("Database/Database.db")
        print("Database: Update method called", ProductID)
        self.cursor = self.connection.cursor()
        self.cursor.execute("UPDATE product SET product_name=? or product_catgory=? or productweight=? or product_shipping_charge=? or product_price=? or product_stock=? WHERE product_id=?",
                            (ProductName, CategoryID1, ProductWeight, ProductShippingCharge, ProductPrice, ProductStockAmount, ProductID))
        self.connection.commit()
        self.connection.close()
        print("Database: Method Finished", ProductID)

    def edit2(self, CategoryID2, CategoryName, CategoryHardness):
        self.connection = sqlite3.connect("Database/Database.db")
        print("Database: Update method called", CategoryID2)
        self.cursor = self.connection.cursor()
        self.cursor.execute("UPDATE product SET category_name=? or category_hardness=? WHERE product_id=?",
                            (CategoryName, CategoryHardness, CategoryID2))
        self.connection.commit()
        self.connection.close()
        print("Database: Method Finished", CategoryID2)

    def save(self):
        self.connection = sqlite3.connect("Database/Database.db")
        self.cursor = self.connection.cursor()
        self.sql = "SELECT * FROM product"
        self.cursor.execute(self.sql)
        self.rows = self.cursor.fetchall()
        self.connection.close()

    def stock(self):
        self.connection = sqlite3.connect("Database/Database.db")
        self.cursor = self.connection.cursor()
        self.sql = "SELECT * FROM product WHERE product_stock < 20"
        self.cursor.execute(self.sql)
        self.ro = self.cursor.fetchall()
        self.connection.close()

    def __del__(self):
        self.connection.close()
        print('Database: Connection is closed')
