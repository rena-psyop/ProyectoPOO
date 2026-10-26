import pymysql


def conexion():
  try:
    mi_conexion = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="empresa",  # Asegúrate de que sea el nombre real de tu BD
    )
    print("Conexión exitosa a la base de datos")

    return mi_conexion  # <-- ¡ESTO ES LO MÁS IMPORTANTE! Debe retornar la conexión

  except Exception as e:
    print(f"Error al conectar a la BD: {e}")
    return None