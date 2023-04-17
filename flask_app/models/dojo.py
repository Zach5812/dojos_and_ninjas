from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

DATABASE = "dojos_and_ninjas_schema"


class Dojo:
    def __init__(self, data: dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #! READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    #! CREATE

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # ! READ ONE/SHOW
    @classmethod
    def get_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        dojo = cls(result[0])
        return dojo
    
        # ! READ ONE
    @classmethod
    def get_one_with_ninjas(cls, id):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, {'id': id})
        dojo = cls(results[0])
        for item in results:
            temp_ninja = {
                'id': item['ninjas.id'],
                'first_name': item['first_name'],
                'last_name': item['last_name'],
                'age': item['age'],
                'dojo_id': item['dojo_id'],
                'created_at': item['ninjas.created_at'],
                'updated_at': item['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(temp_ninja))
        return dojo

