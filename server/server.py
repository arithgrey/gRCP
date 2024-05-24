import grpc
from concurrent import futures
import product_pb2
import product_pb2_grpc

# Definition of the server logic
class ProductService(product_pb2_grpc.ProductServiceServicer):
    def GetAvailableQuantity(self, request, context):
        # Here would go the logic to obtain the available quantity of the product with the provided ID
        # Let's assume the logic simply returns a fixed value for now
        quantity = 100
        return product_pb2.ProductResponse(available_quantity=quantity)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
