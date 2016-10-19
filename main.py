# http://www.theprojectspot.com/tutorial-post/creating-a-genetic-algorithm-for-beginners/3

class Populacao:

	def __init__(self, tamanhoPopulacao = 0, inicializar = False):
		self.individuos = []

		if inicializar == True:
			for i in range(1, tamanhoPopulacao):
				novoIndividuo = Individuo()
				novoIndividuo.gerarIndividuo()
				self.gravarIndividuo(novoIndividuo)
		return False

	def setIndividuo(self, individuo):
		self.individuos.append(individuo)

	def getIndividuo(self, indice):
		return self.individuos[indice]

	def tamanhoPopulacao(self):
		return len(self.individuos)

	def getMaisApto():
		maisApto = self.getIndividuo(0)
		tamanhoPop = self.tamanhoPopulacao()

		for individuo in self.individuos:
			if individuo.getAptidao() <= maisApto.getAptidao():
				maisApto = individuo

		return maisApto

