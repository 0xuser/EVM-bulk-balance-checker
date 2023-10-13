from pick import pick

from BulkChecker import BulkChecker
from config import NETWORKS

if __name__ == '__main__':
    title = 'Please select a network:'
    networks = list(NETWORKS.keys())
    network, index = pick(networks, title)

    checker = BulkChecker(network_name=network)
    checker.bulk_check()

