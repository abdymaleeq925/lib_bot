class AuthorsSQL():
    def __init__(self, cursor):
        self.cursor = cursor


    def add_new_author(self,first_name, last_name, birthday):
        query = f"""
        INSERT INTO authors(first_name, last_name, birthday)
        VALUES('{first_name}','{last_name}', '{birthday}');
        """
        self.cursor.execute(query)
        print("Автор успешно создан!")

    def get_author(self, id):
        query = f"""
        SELECT * FROM authors WHERE id={id};
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_all_authors(self):
        query = f"""
        SELECT * FROM authors;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall() 
    
           
