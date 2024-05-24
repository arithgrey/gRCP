ARG PYTHON_VERSION=python:3.8-alpine

# Usa la imagen oficial de Python
FROM ${PYTHON_VERSION} 

RUN apk add --no-cache build-base

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo .proto al contenedor
COPY requirements.txt .
COPY product.proto .


RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["sh", "-c", "python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. product.proto && python client.py"]
