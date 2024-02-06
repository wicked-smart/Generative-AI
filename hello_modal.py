import modal 

stub = modal.Stub()


@stub.function()
def hello():
    print("Running remotely on Modal!")
