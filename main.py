# AL732960 - MSAF - Busqueda ternaria

def btemaria(arreglo, n, llave):
	mid1 = 0
	mid2 = 0
	a = int()
	b = int()
	r = n-1
	l = 0
	a = 0
	b = 0
	while b!=1:
		mid1 = round(l+(r-l)/3)
		mid2 = round(r-(r-l)/3)
		if arreglo[mid1]==llave:
			respuesta = mid1
			a = 1
			b = 1
		else:
			if arreglo[mid2]==llave:
				respuesta = mid2
				a = 1
				b = 1
			else:
				if arreglo[mid1]>llave:
					r = mid1-1
				else:
					if arreglo[mid2]<llave:
						l = mid2+1
					else:
						l = mid1+1
						r = mid2-1
	if a==0:
		respuesta = -1
	return respuesta

llave = 6
n = 10
arreglo = [1,2,3,4,5,6,7,8,9,10]
ind = btemaria(arreglo,n,llave)
if ind!=-1:
	print("El elemento ",llave," se encontro en el lugar: ",ind)
else:
	print("El elemento no se encontro en el arreglo")