Feature: Rango de una edad
	como usuario del archivo edades
	deseo ingresar un numero como edad
	para obtener el rango en el que se encuentra

	Scenario: Edad menor de 0 años
		Dado que tengo la edad "-1"
		cuando ingreso este numero
		entonces obtengo el resultado "no existes"

	Scenario: Edad de 0 años
		Dado que tengo la edad "0"
		cuando ingreso este numero
		entonces obtengo el resultado "eres un bebe"

	Scenario: Edad de 5 años
		Dado que tengo la edad "5"
		cuando ingreso este numero
		entonces obtengo el resultado "eres un ninio"

	Scenario: Edad de 16 años
		Dado que tengo la edad "16"
		cuando ingreso este numero
		entonces obtengo el resultado "eres un adolescente"

	Scenario: Edad de 22 años
		Dado que tengo la edad "22"
		cuando ingreso este numero
		entonces obtengo el resultado "eres un adulto"

	Scenario: Edad de 80 años
		Dado que tengo la edad "80"
		cuando ingreso este numero
		entonces obtengo el resultado "eres un adulto mayor"

	Scenario: Edad de 134 años
		Dado que tengo la edad "134"
		cuando ingreso este numero
		entonces obtengo el resultado "eres Mumm-Ra"