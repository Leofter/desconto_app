from src.models.desconto import DescontoPremium, DescontoVIP, DescontoNormal
from src.models.pedido import Pedido
from src.controllers.pedido_controller import PedidoController
from src.services.pedido_service import PedidoService
from src.repositories.pedido_repository import PedidoRepository
from src.database.connection import DatabaseConnection

if __name__ == "__main__":
    database = DatabaseConnection()
    repo = PedidoRepository(database)
    service = PedidoService(repo)
    controller = PedidoController(service)

    pedido1 = Pedido("Leo", DescontoNormal())
    pedido1.valor_original = 50

    pedido2 = Pedido("Bia", DescontoVIP())
    pedido2.valor_original = 50

    pedido3 = Pedido("Nino", DescontoPremium())
    pedido3.valor_original = 50

    controller.adicionar_pedido(pedido1)
    controller.adicionar_pedido(pedido2)
    controller.adicionar_pedido(pedido3)

    controller.processar_pedidos()