from promise import Promise
from net.grpc_client import TaskClient
import numpy as np


cli = TaskClient('35.222.28.225', '50051')
prom = Promise('numpy', 'inv', np.array([[1., 2.],[3., 4.]]), {}, "linalg")

cli.send_promise(prom)