from src.models.desconto import DescontoPremium, DescontoVIP, DescontoNormal
from src.models.pedido import Pedido
from src.services.pedido_service import PedidoService

if __name__ == "__main__":
    #pedido = Pedido("Leonardo", DescontoVIP())
    #valor_final = pedido.valor_final(100)
    #print(f"cliente: {pedido.cliente}")
    #print(f"valor_final: {valor_final}")

    pedido1 = Pedido("Leo", DescontoNormal())
    pedido1.valor_original = 50

    pedido2 = Pedido("Bia", DescontoVIP())
    pedido2.valor_original = 50

    pedido3 = Pedido("Nino", DescontoPremium())
    pedido3.valor_original = 50

    service = PedidoService()
    service.adicionar_pedido(pedido1)
    service.adicionar_pedido(pedido2)
    service.adicionar_pedido(pedido3)

    service.processar_pedidos()

