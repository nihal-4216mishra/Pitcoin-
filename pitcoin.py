
import hashlib
import json
import time


class Pitcoin:
    def __init__(self):
        self.chain = []
        self.difficulty = 3
        self.create_block(0, "Genesis Block")

    def create_block(self, proof, data):
        previous_hash = (
            self.hash(self.chain[-1])
            if self.chain else "0"
        )
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time.time(),
            "proof": proof,
            "data": data,
            "previous_hash": previous_hash,
        }
        self.chain.append(block)
        return block

    @staticmethod
    def hash(block):
        encoded = json.dumps(
            block, sort_keys=True
        ).encode()
        return hashlib.sha256(encoded).hexdigest()

    def mine(self):
        proof = 0
        while not hashlib.sha256(
            str(proof).encode()
        ).hexdigest().startswith(
            "0" * self.difficulty
        ):
            proof += 1

        return self.create_block(
            proof, "Pitcoin demo block"
        )


if __name__ == "__main__":
    coin = Pitcoin()
    block = coin.mine()
    print("Pitcoin mining demo")
    print(json.dumps(block, indent=2))
  
