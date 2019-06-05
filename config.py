class conexion:

    def __init__(self,usuario):
        self.usuario = usuario
    
    
    CONFIG_DB = dict()
    def datosdb(self):
        CONFIG_DB={'HOST':'localhost', 
        'USERNAME':self.usuario, 
        'PASSWORD' :'Fox841204.-', 
        'DATABASENAME': 'proyecto',
        'CRARSET':'utf8mb4'}
        return CONFIG_DB