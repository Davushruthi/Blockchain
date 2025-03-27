import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        self.chain = []  # Initialize the blockchain with the genesis block
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", time.time(), "Genesis Block", self.calculate_hash(0, "0", time.time(), "Genesis Block"))
        self.chain.append(genesis_block)

    def add_block(self, data):
        # Get the last block in the chain
        previous_block = self.chain[-1]  
        new_index = previous_block.index + 1 
        new_timestamp = time.time()
        new_hash = self.calculate_hash(new_index, previous_block.hash, new_timestamp, data)
        new_block = Block(new_index, previous_block.hash, new_timestamp, data, new_hash)  # Create a new block
        # Append the new block to the chain
        self.chain.append(new_block)

    def calculate_hash(self, index, previous_hash, timestamp, data):
        """Generates a SHA-256 hash for the block."""
        value = f"{index}{previous_hash}{timestamp}{data}".encode()
        return hashlib.sha256(value).hexdigest()

# Testing the blockchain
my_blockchain = Blockchain()
my_blockchain.add_block("Transaction 1")
my_blockchain.add_block("Transaction 2")

# Print blockchain to verify
for block in my_blockchain.chain:
    print(f"Index: {block.index}, Hash: {block.hash}, Data: {block.data}")