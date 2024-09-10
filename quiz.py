from typing import List

class Quiz:
    __acertos: int
    __erros: int

    def __init__(self, acertos: int, erros: int):
        self.__acertos = acertos
        self.__erros = erros

    def calcular_pontos(self):
        return self.__acertos - self.__erros
    
    def get_acertos(self):
        return self.__acertos
    
    def get_erros(self):
        return self.__erros
    
    def __str__(self):
        info = f'Acertos: {self.__acertos}, Erros: {self.__erros} \n'
        info += f'Total de pontos: {self.calcular_pontos()} \n'

        return info

class Quiz2A(Quiz):
    def calcular_pontos(self):
        return self.get_acertos() - (self.get_erros() * 4)

class Quiz3A(Quiz):
    def calcular_pontos(self):
        return self.get_acertos() - (self.get_erros() * 2)
    
class Aluno:
    __matricula: int
    __nome: str
    __quizes: List[Quiz]

    def __init__(self, matricula: int, nome: str, quizes: List[Quiz]):
        self.__matricula = matricula
        self.__nome = nome
        self.__quizes = quizes
    
    def get_matricula(self):
        return self.__matricula
    
    def __str__(self):
        infos = f'Nome: {self.__nome} \n'
        infos += f'Matricula: {self.__matricula} \n'

        total = 0
        for quiz in self.__quizes:
            total += quiz.calcular_pontos()

        infos += f'Total de Pontos: {total} \n'
        
        return infos

class Disciplina:
    __nome: str
    __professor: str
    __ano: int
    __semestre: int
    __alunos: List[Aluno] = []

    def __init__(self, nome: str, professor: str, ano: int, semestre: int):
        self.__nome = nome
        self.__professor = professor
        self.__ano = ano
        self.__semestre = semestre

    def add_aluno(self, a: Aluno):
        for aluno in self.__alunos:
            if a.get_matricula() == aluno.get_matricula():
                raise Exception("Aluno já existente!")
        
        self.__alunos.append(a)

    def __str__(self):
        infos = f'Disciplina: {self.__nome} \n'
        infos += f'Professor: {self.__professor} \n'
        infos += f'Ano/Semestre: {self.__ano}/{self.__semestre} \n'
        for aluno in self.__alunos:
            infos += f'{aluno.__str__()} \n'
        return infos

