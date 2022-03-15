import queue


class GenreSQL():

    def __init__(self, cursor):
        self.cursor = cursor

    
    def add_new_genre(self, value):
        query = f"""
        INSERT INTO genre(name) 
        VALUES('{value}');
        """
        self.cursor.execute(query)
        print("Новый жанр успешно добавлен!")
    
    def get_genre(self, id):
        query = f"""
        SELECT * FROM genre WHERE id={id};
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_all_genres(self):
        query = """
        SELECT * FROM genre;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def delete_genre(self, id):
        query = f"""
        DELETE FROM genre WHERE id={id};
        """
        self.cursor.execute(query)
        print("Жанр успешно удален!")
    
    def update_genre(self, id,value):
        query = f"""
        UPDATE genre SET name={value} WHERE id={id};
        """
        self.cursor.execute(query)
        print("Жанр успешно обновлен!")

    