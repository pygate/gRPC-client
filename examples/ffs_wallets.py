from pygate_grpc.client import PowerGateClient
from google.protobuf.json_format import MessageToDict


client = PowerGateClient("127.0.0.1:5002")

wallets = client.wallet.list()
print("Wallets:")
print(wallets)


print("Creating a new FFS:")
newFfs = client.ffs.create()
print(newFfs)

address = client.ffs.addrs_list(newFfs.token)
obj = MessageToDict(address)
wallet = obj["addrs"][0]["addr"]
print("FFS wallet:" + wallet)

balance = client.wallet.balance(wallet)
print("Wallet balance: " + balance)