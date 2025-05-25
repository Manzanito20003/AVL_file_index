from AVL.AVLfile import create_index_avl

class RecordGeneric:
    def __init__(self, attribute_names):
        for name in attribute_names:
            setattr(self, name, None)

    def to_dict(self):
        return {attr: getattr(self, attr) for attr in self.__dict__}


if __name__ == "__main__":
    data_records = []

    # Lista de datos de ejemplo (solo valores)
    datos = [
        ["Juan", 20, "12345678"],
        ["Lucía", 22, "87654321"],
        ["Carlos", 30, "45678912"],
        ["Ana", 28, "78912345"],
        ["Luis", 25, "23456789"],
    ]
    atributos = ["nombre", "edad", "dni"]

    #creando el obj
    record1 = RecordGeneric(atributos)
    record2 = RecordGeneric(atributos)
    record3 = RecordGeneric(atributos)

    # Crear los registros
    record1.nombre, record1.edad, record1.dni = datos[0]
    record2.nombre, record2.edad, record2.dni = datos[1]
    record3.nombre, record3.edad, record3.dni = datos[2]

    records = [record1, record2, record3]
    create_index_avl(records,atribute_index="nombre",type='str')
