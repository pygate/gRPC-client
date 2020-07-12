from pygate_grpc.client import PowerGateClient


if __name__ == "__main__":
    hostName = "127.0.0.1:5002"
    # Create client
    c = PowerGateClient(hostName)
    # Create FFS
    ffs = c.ffs.create()
    print("FFS created:")
    print(ffs)
    # Create an iterator of the given file using the helper function
    iter = c.ffs.get_file_bytes("README.md")
    print("grabbing pygate-grpc 'README.md' file")
    print("adding file to IPFS (hot storage)")
    # Convert the iterator into request and then add to hot set
    res = c.ffs.add_to_hot(c.ffs.bytes_to_chunks(iter), ffs.token)
    print(res)
    print("pushing file to FFS")
    # Push the given file
    c.ffs.push(res.cid, ffs.token)
    print("retrieving file from FFS:")
    # Get the file back
    file = c.ffs.get(res.cid, ffs.token)
    print(next(file))