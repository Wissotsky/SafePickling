from safepickling import SafePickling
from dataclasses import dataclass

@dataclass
class UselessData:
    cat: str = "cat"
    dog: str = "dog"
    chicken: str = "chicken"
    cat_count: int = 3
    dog_count: int = 1
    chicken_count: int = 12

def test_flow():
    data = UselessData()

    server = SafePickling()
    server.generate_key()

    client = SafePickling()
    client.add_trusted_keys([server.key])

    safe_data = server.pickle(data)

    client_data = client.unpickle(safe_data)
    assert client_data == data
