from promise import Promise
from net.grpc_client import TaskClient

cli = TaskClient("localhost", "50051")
prom = Promise("numpy", "array", [1, 2, 3], {})

cli.send_promise(prom)
