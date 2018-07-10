from setuptools import setup, find_packages

# la funcion find_packages permite buscar los paquetes del proyecto
# El parametro install_requires se usa para indicar las dependencias de paquetes externos
# Se puede indicar la versión de los paquetes requeridos, si no se indica se
# instala la ultima versión.
setup(
    name="paquete",
    version="0.1",
    description="Este es un paquete de ejemplo",
    author="Ricardo Vargas",
    author_email="godxvincent@xxxx.com",
    install_requires=["pillow=1.1.0"],
    test_suite="tests",
    # install_requires=["pillow>=1.1.0"],
    # url="http://hcosta.info",
    # packages=['paquete', 'paquete.hola', 'paquete.adios']
    packages=find_packages()
)

# Otra forma de adicionar las dependencias es crear un archivo TXT anexo en la
# misma carpeta del setup e indicar en la funcion setup la siguiente
# instrucciones
# install_requires=[i.strip() for i in open("requirements.txt").readlines()]

# PAra ejecuar los test se hacer así:
# python setup.py test

# Se puede instalar un paquete en modo desarrollo
# python setup.py develop
# python setup.py develop --uninstall para desinstalar.

# Para distribuir localmente se puede hacer uso del comando
# python setup.py sdist
# y para instalarlo se puede hacer mediante el comando
# pip install nombre_del_fichero.zip
