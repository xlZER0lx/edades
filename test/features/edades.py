class Edades():


    def edad(self, edad):
        try:
            int(edad)
        except:
            return 'no es un numero'

        if(edad < 0):
            return 'no existes'
        elif(edad == 0):
            return 'eres un bebe'
        elif(edad > 0 and edad < 13):
            return 'eres un ninio'
        elif(edad >= 13 and edad < 18):
            return 'eres un adolescente'
        elif(edad >= 18 and edad < 65):
            return 'eres un adulto'
        elif(edad >= 65 and edad <= 120):
            return 'eres un adulto mayor'
        elif(edad > 120):
            return 'eres Mumm-Ra'