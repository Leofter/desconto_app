from src.models.desconto import DescontoPremium, DescontoVIP, DescontoNormal
from src.models.pedido import Pedido
from src.services.pedido_service import PedidoService
from src.repositories.pedido_repository import PedidoRepository

if __name__ == "__main__":
    repo = PedidoRepository()

    pedido1 = Pedido("Leo", DescontoNormal())
    pedido1.valor_original = 50

    pedido2 = Pedido("Bia", DescontoVIP())
    pedido2.valor_original = 50

    pedido3 = Pedido("Nino", DescontoPremium())
    pedido3.valor_original = 50

    repo.adicionar_pedido(pedido1)
    repo.adicionar_pedido(pedido2)
    repo.adicionar_pedido(pedido3)

    pedidos = repo.listar_pedidos()

    for pedido in pedidos:
        print(f"cliente: {pedido.cliente}")
        print(f"Valor final: {pedido.valor_final(pedido.valor_original)}")
