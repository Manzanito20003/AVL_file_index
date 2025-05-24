
### algoritmo

Función: create_index_avl(records: List[bytes], column_index: int, record_size: int)

Entradas:
- records: lista de registros binarios (ej. leídos desde 'data.dat')
- column_index: índice del campo a usar como clave para el índice (ej. 0 para 'dni')
- record_size: tamaño fijo de cada registro (para poder buscarlo luego por offset)

Pasos:

1. Crear o abrir en modo escritura binaria el archivo 'index_avl_column_index.dat'
   (Este será el árbol AVL persistente)

2. Para cada registro en 'records':
   2.1. Extraer la clave a indexar usando el column_index
        clave = extract_field(record, column_index)
   2.2. Calcular la posición lógica del registro original:
        pos = i * record_size
   2.3. Insertar (clave, pos) en el archivo 'index-avl' manteniendo la estructura AVL
        (balancear si es necesario)

3. Guardar cambios y cerrar el archivo
