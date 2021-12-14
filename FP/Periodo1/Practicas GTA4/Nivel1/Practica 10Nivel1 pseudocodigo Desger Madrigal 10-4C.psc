Algoritmo sin_titulo
	
	parcial1 = 0
	parcial2 = 0
	parcial3 = 0
	Exam = 0
	trabajoF = 0
	Escribir "Digite las 3 notas de los parciales"
	Leer parcial1, parcial2, parcial3
	Escribir "Digite la nota del examen"
	Leer Exam
	Escribir "Digite la nota del trabajo final"
	Leer trabajoF
	promedioParcial = (parcial1+parcial2+parcial3)/3
	notaParcial = promedioParcial*0.55
	notaExamen = Exam*0.30
	notaTrabajo = TrabajoF*0.15
	calificacion = notaParcial+notaExamen+notaTrabajo
	Escribir "Su calificacion es de: ", calificacion
	
FinAlgoritmo
