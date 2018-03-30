# -*- coding: utf-8 -*-


# Funcion que calcula el numero de Fibonacci en forma recursiva.
def fibonacci(numero):
  if (numero < 2):
    return numero
  else:
    return fibonacci(numero-1)+fibonacci(numero-2)


# Funcion que valida si el numero ingreso coincide con un numero de Fibonacci
def validar(iterador, input):
	if(input == fibonacci(iterador)):
		return iterador
	else:
		iterador += 1
		return validar(iterador, input)


# Funcion principal.
def run():
	input = int(raw_input('Escribe el numero Fibonacci: '))

	posicion = validar(0, input)

	print 'Fibonacci(' + str(input) + ') -> ' + str(fibonacci(posicion-1)) + ', ' + str(fibonacci(posicion-2))


# Nuestro programa empieza aqui.
if __name__ == '__main__':
	run()
