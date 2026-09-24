import abc

class IDesconto(abc.ABC):
    @abc.abstractmethod
    def calcular(self, valor:float) -> float:
        pass 

class DescontoNormal(IDesconto):
    def calcular(self, valor) -> float:
        return valor * 0.1 

class DescontoVIP(IDesconto):
    def calcular(self, valor) -> float:
        return valor * 0.2

class DescontoPremium(IDesconto):
    def calcular(self, valor) -> float:
        return valor * 0.3

# class normal(IDesconto):
#     def calcular(100, 0.1)
#     calculado_desconto = IDesconto.calcular(100, 0.1)
#     return calculado_desconto