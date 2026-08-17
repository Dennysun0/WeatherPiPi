
# __init__ lo que hace es declarar la carpeta como paquete de python

"""
Paquete que contiene los archivos utilizados
para realizar pruebas durante el desarrollo.
"""

'''
Al tener __init__.py, Python puede tratar pruebas como un módulo/paquete y podemos ejecutar:
py -m pruebas.probar_weather
py -m pruebas.probar_storage
py -m pruebas.probar_meteo

Es simplemente una forma de decirle a Python:
"Ejecuta este archivo como un módulo perteneciente al paquete pruebas."
Por eso, cada vez que quieras ejecutar una prueba, tendrás que indicar cuál:
py -m pruebas.probar_weather
                    ↑
                este archivo
'''