# -*- coding: utf-8 -*-
# http://www.theprojectspot.com/tutorial-post/creating-a-genetic-algorithm-for-beginners/3

import random

class Populacao:

	def __init__(self, tamanhoPopulacao = 0, inicializar = False):
		self.individuos = []

		if inicializar == True:
			for i in range(0, tamanhoPopulacao):
				novoIndividuo = Individuo()
				novoIndividuo.gerarIndividuo()
				self.setIndividuo(novoIndividuo)

	def setIndividuo(self, individuo):
		self.individuos.append(individuo)

	def getIndividuo(self, indice):
		return self.individuos[indice - 1]

	def tamanhoPopulacao(self):
		return len(self.individuos)

	def getMaisApto(self):
		maisApto = self.getIndividuo(0)
		tamanhoPop = self.tamanhoPopulacao()

		for individuo in self.individuos:
			if individuo.getAptidao() > maisApto.getAptidao():
				maisApto = individuo

		return maisApto

	def salvarIndividuo(self, indice, individuo):
		self.individuos.insert(indice, individuo)

class Individuo:

	def __init__(self):
		self.genes = bytearray()
		self.aptidao = 0

	def tamanhoGene(self):
		return len(self.genes)

	def gerarIndividuo(self):
		for i in range(0, 64):
			gene = random.randint(0,1)
			self.genes.append(gene)

	def getGene(self, indice):
		return self.genes[indice]

	def setGene(self, indice, valor):
		self.genes.insert(indice, valor)
		self.aptidao = 0

	def getAptidao(self):
		if(self.aptidao == 0):
			self.aptidao = CalcAptidao.calcAptidao(self)

		return self.aptidao

	def __str__(self):
		geneString = ''
		for i in range(0, self.tamanhoGene()):
			geneString += str(self.getGene(i))
		return geneString

class Algoritmo:

	taxaUniforme = 0.5
	taxaMutacao = 0.015
	tamanhoTorneio = 5
	elitismo = True

	# Evolui toda a população
	@staticmethod
	def evoluirPopulacao(populacao):
		novaPopulacao = Populacao(populacao.tamanhoPopulacao(), False)

		# Manter o melhor individuo
		if Algoritmo.elitismo == True:
			novaPopulacao.salvarIndividuo(0, populacao.getMaisApto())

		# Faz crossover da população
		# Remover este 1 do range
		for i in range(1, populacao.tamanhoPopulacao()):
			individuoA = Algoritmo.selecaoPorTorneio(populacao)
			individuoB = Algoritmo.selecaoPorTorneio(populacao)
			novoIndividuo = Algoritmo.cruzar(individuoA, individuoB)
			novaPopulacao.salvarIndividuo(i, novoIndividuo)

		# Mutar população
		# Remover este 1 do range
		for i in range(1, populacao.tamanhoPopulacao()):
			Algoritmo.mutar(novaPopulacao.getIndividuo(i))

		return novaPopulacao

	@staticmethod
	def cruzar(individuoA, individuoB):
		novoIndividuo = Individuo()

		for i in range(0, 64):
			if (random.random() <= Algoritmo.taxaUniforme):
				novoIndividuo.setGene(i, individuoA.getGene(i))
			else:
				novoIndividuo.setGene(i, individuoB.getGene(i))

		return novoIndividuo

	@staticmethod
	def mutar(individuo):
		for i in range(0, 64):
			if (random.random() <= Algoritmo.taxaMutacao):
				gene = random.randint(0,1)
				individuo.setGene(i, gene)

	# Selecioar individuos para cruzamento
	@staticmethod
	def selecaoPorTorneio(populacao):
		torneio = Populacao(Algoritmo.tamanhoTorneio, False)

		for i in range(0, Algoritmo.tamanhoTorneio):
			idAleatorio = random.randint(0, populacao.tamanhoPopulacao())
			torneio.salvarIndividuo(i, populacao.getIndividuo(idAleatorio))

		maisApto = torneio.getMaisApto()
		return maisApto

class CalcAptidao:

	solucao = []

	@staticmethod
	def setSolucao(novaSolucao):
		for byte in  novaSolucao:
			CalcAptidao.solucao.append(int(byte))

	@staticmethod
	def calcAptidao(individuo):
		aptidao = 0
		for i in range(0, 64):
			if individuo.getGene(i) == CalcAptidao.solucao[i]:
				aptidao += 1

		return aptidao

	@staticmethod
	def getAptidaoMaxima():
		aptidaoMaxima = len(CalcAptidao.solucao)
		return aptidaoMaxima

CalcAptidao.setSolucao('1111000000000000000000000000000000000000000000000000000000001111')
minhaPopulacao = Populacao(50, True)

contagemGeracoes = 0

while(minhaPopulacao.getMaisApto().getAptidao() < CalcAptidao.getAptidaoMaxima()):
	contagemGeracoes += 1
	print("Geracao " + str(contagemGeracoes) + " / Mais apto: " + str(minhaPopulacao.getMaisApto().getAptidao()))
	minhaPopulacao = Algoritmo.evoluirPopulacao(minhaPopulacao)

print("Solucao encontrada!")
print("Geracao " + str(contagemGeracoes))
print("GENES: " + str(minhaPopulacao.getMaisApto()))