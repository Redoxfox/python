class Model:
    from app import app, db, db1
    import pymysql.cursors

    def __init__(self,datos_table):
       self.Datos_table = datos_table
    

    def CT_TABLE(self):
        list_table = []
        for items in self.Datos_table:
            valor = self.Datos_table[items]
            if items=="TABLE":
                Cadena = "CREATE TABLE IF NOT EXISTS " + valor + "("
                list_table.append(Cadena)
            else:
                if items != "PK":
                    Cadena = items + " " + valor + ","  
                    list_table.append(Cadena)
            
            if items=="PK":
                Cadena = "PRIMARY KEY " + "(" + valor + ")"
                list_table.append(Cadena)
        
        
        result = ' '.join(list_table)
        longitud = len(result)
        ultima = result[longitud-1]
        if ultima==",":
           result=result[0:longitud-1]
           result = result + ");"
        else:
           result = result + ");"""

        return result
    
    def IT_TABLE(self):
        list_column = []
        list_values = []
        cont=0
        list_column.append("INSERT INTO ")
        list_values.append(" VALUES(")
        for items in self.Datos_table:
            valor = self.Datos_table[items]
            if items=="TABLE":
                Cadena = valor + "("
                list_column.append(Cadena)
            else:
                cont+=1
                num_col="Col" + str(cont)
                num_value="Val" + str(cont)
                if items == num_col:
                    Cadena = valor + ","  
                    list_column.append(Cadena)
                if items == num_value:
                    Cadena = valor + ","  
                    list_values.append(Cadena)
          
        Colunm= ' '.join(list_column)
        lenColunm = len(Colunm)
        ultimaCol = Colunm[lenColunm-1]
        if ultimaCol==",":
           Colunm=Colunm[0:lenColunm-1]
           Colunm = Colunm + ")"
        else:
           Colunm = Colunm + ")"
        
        Values= ' '.join(list_values)
        lenValues = len(Values)
        ultimaVal = Values[lenValues-1]
        if ultimaVal == ",":
           Values=Values[0:lenValues-1]
           Values = Values + ");"
        else:
           Values = Values + ");"
        
        result = Colunm + Values

        return result

    
    def SSP_TABLE(self):
        list_column = []
        list_table = []
        cont=0
        list_column.append("SELECT ")
        for items in self.Datos_table:
            valor = self.Datos_table[items]
            if items=="TABLE":
                Cadena = valor + "WHERE "
                list_table.append(Cadena)
            else:
                cont+=1
                num_col="Col" + str(cont)
                if items == num_col:
                    Cadena = valor + ","  
                    list_column.append(Cadena)
          
        Colunm= ' '.join(list_column)
        lenColunm = len(Colunm)
        ultimaCol = Colunm[lenColunm-1]
        if ultimaCol==",":
           Colunm=Colunm[0:lenColunm-1]
           Colunm = Colunm + " FROM "
        else:
           Colunm = Colunm + " FROM "
        
        Values= ' '.join(list_table)
        result = Colunm + Values

        return result
    
    def SW_TABLE(self):
        list_column = []
        list_table = []
        list_where = []
        cont=0
        list_column.append("SELECT ")
        for items in self.Datos_table:
            valor = self.Datos_table[items]
            if items=="TABLE":
                Cadena = valor + " "
                list_table.append(Cadena)
            else:
                cont+=1
                num_col="Col" + str(cont)
                num_whe="Whe" + str(cont)
                if items == num_col:
                    Cadena = valor + ","  
                    list_column.append(Cadena)
                if items == num_whe:
                    Cadena = valor 
                    list_where.append(Cadena) 

          
        Colunm= ' '.join(list_column)
        lenColunm = len(Colunm)
        ultimaCol = Colunm[lenColunm-1]
        if ultimaCol==",":
           Colunm=Colunm[0:lenColunm-1]
           Colunm = Colunm + " FROM "
        else:
           Colunm = Colunm + " FROM "
        
        Values= ' '.join(list_table)

        Wheres= ' '.join(list_where)
        lenWheres= len(Wheres)
        ultimaVal = Wheres[lenWheres-1]
        if ultimaVal == ",":
           Wheres=Wheres[0:lenWheres-1]
           Wheres= Wheres + ";"
        else:
           Wheres = Wheres + ";"
        
        result = Colunm + Values + "WHERE " + Wheres

        return result
        
        

