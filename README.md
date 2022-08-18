# SafePickling

SafePickling is a python library that allows you to sign and verify python pickles.

```mermaid
graph LR
    subgraph Server
        A[Object]:::object -->B{Pickle and sign}:::cryptography
        C[Key]:::storage --> B
        B --> pik2[signature] --> D(Server):::network
        B --> pik1[pickle] --> D
    end
    subgraph Client
        D ==> E(Client):::network
        E -->unpik2[signature]
        E -->unpik1[pickle] --> F{Sign}:::cryptography
        known[(Known keys)]:::storage --> F --> F
        F --> eq{Is equal?}
        unpik2 --> eq:::cryptography
        eq -->|Yes|unpik{{Unpickle}}:::cryptography --> Z[Object]:::object
        eq -->|No|Invalid(Invalid):::error
    end

    classDef network fill:#FFD666;
    classDef cryptography fill:#82FF66;
    classDef error fill:#FF6B66;
    classDef storage fill:#DE66FF;
    classDef object fill:#666EFF;
```

## Installation

```sh
pip install safepickling
```

## Usage Example

```python
object = ExampleObject()

server = SafePickling() # Create a server instance
server.generate_key() # Generate a random key for the server
pickled_object = server.pickle(object) # Pickle the object and sign it
```
```python
client = SafePickling() # Create a client instance
client.add_trusted_keys([server.key]) # Add the server's key to the client's trusted keys
unpickled_object = client.unpickle(pickled_object) # Unpickle the data while verifying it's signature with the server's key
```

## Cryptography

Random provided by `secrets.token_bytes`

Hash comparison with `hmac.compare_digest`

Hashing done using `hashlib.blake2b`
