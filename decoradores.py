def funcionDecoradora(funcionParametro):
	def funcionInterior():
		#antes de ejecutarse la funcion paametro
		print('vamos a ealizar un calculo')
		funcionParametro()
		#despues de ejecutarse la funcion parametro
		print('ya realizamos el calculo')
	return funcionInterior

@funcionDecoradora
def suma():
	print(15+15)


suma()