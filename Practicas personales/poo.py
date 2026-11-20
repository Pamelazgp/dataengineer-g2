import csv

class Usuario:
    def __init__(self, id, nombre, apellido):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        
    def to_dict(self):
        return {
            "id":self.id,
            "nombre": self.nombre,
            "apellido": self.apellido
        }
            
        


def main():
    usuarios_traidos=[]
    with open("datos.csv","r", encoding="utf-8") as archivo:
        lector=csv.reader(archivo)
        i=0
        for dato in lector:
            if i==0:
                i+=1
                continue
            
            usuario=Usuario(
                dato[0],
                dato[1],
                dato[2]
            )
            
            usuarios_traidos.append(usuario.to_dict())
            
    #print(usuarios_traidos) 
    def obtener_apellidos(usuario):
        return usuario["apellido"].lower()
    
    resultado_final=[]
    usuarios_ordenados=sorted(usuarios_traidos, key=obtener_apellidos)
    for dato1 in usuarios_ordenados:
        resultado_final.append(dato1)
    print(resultado_final)

main()