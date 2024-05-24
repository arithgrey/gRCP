import grpc
import product_pb2
import product_pb2_grpc

def get_product_quantity(product_id):
    # Establish connection with the gRPC server
    channel = grpc.insecure_channel('grpc_server:50051')
    stub = product_pb2_grpc.ProductServiceStub(channel)

    # Create a request with the product ID
    request = product_pb2.ProductRequest(id=product_id)

    # Make the call to the server method to get the available quantity
    response = stub.GetAvailableQuantity(request)

    # Return the available quantity obtained from the server
    return response.available_quantity

if __name__ == '__main__':
    product_id = 1232  # ID of the product you want to query
    available_quantity = get_product_quantity(product_id)
    print(f"Available quantity of product {product_id}: {available_quantity}")
