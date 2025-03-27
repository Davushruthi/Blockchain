import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce, hash_value):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash_value = hash_value  # Corrected hash assignment

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        """Creates the first block (Genesis Block) with Proof of Work."""
        genesis_block = self.mine_block(0, "0", "Genesis Block")
        self.chain.append(genesis_block)

    def add_block(self, data):
        """Mines a new block and adds it to the chain."""
        previous_block = self.chain[-1]  
        new_index = previous_block.index + 1
        new_block = self.mine_block(new_index, previous_block.hash_value, data)  # Fixed attribute name
        self.chain.append(new_block)

    def mine_block(self, index, previous_hash, data):
        """Performs Proof of Work to generate a valid hash."""
        timestamp = time.time()
        nonce = 0
        while True:
            hash_value = self.calculate_hash(index, previous_hash, timestamp, data, nonce)
            if hash_value[:self.difficulty] == "0" * self.difficulty:
                return Block(index, previous_hash, timestamp, data, nonce, hash_value)
            nonce += 1

    def calculate_hash(self, index, previous_hash, timestamp, data, nonce):
        """Generates a SHA-256 hash for the block."""
        value = f"{index}{previous_hash}{timestamp}{data}{nonce}".encode()
        return hashlib.sha256(value).hexdigest()

    def is_chain_valid(self):
        """Checks if the blockchain is valid and detects tampering."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Recalculate hash and compare
            recalculated_hash = self.calculate_hash(
                current_block.index, current_block.previous_hash, 
                current_block.timestamp, current_block.data, current_block.nonce
            )
            if current_block.hash_value != recalculated_hash:
                print(f"Block {current_block.index} has been tampered with!")
                return False

            # Check previous hash linkage
            if current_block.previous_hash != previous_block.hash_value:
                print(f"Block {current_block.index} is not linked properly!")
                return False

        print("Blockchain is valid.")
        return True

    def tamper_block(self, block_index, new_data):
        """Simulates tampering by modifying a block’s data."""
        if 0 < block_index < len(self.chain):
            self.chain[block_index].data = new_data  # Modify block data
            print(f"Block {block_index} tampered with! New data: {new_data}")
        else:
            print("Invalid block index for tampering.")

# Testing the blockchain
my_blockchain = Blockchain(difficulty=4)  # Ensure difficulty is properly passed
my_blockchain.add_block("Transaction 1")
my_blockchain.add_block("Transaction 2")

# Print blockchain to verify correct output
for block in my_blockchain.chain:
    print(f"Index: {block.index}, Hash: {block.hash_value}, Nonce: {block.nonce}, Data: {block.data}")

# Validate blockchain before tampering
print("\nInitial Blockchain Validation:")
my_blockchain.is_chain_valid()

# Tamper with a block
my_blockchain.tamper_block(1, "Hacked Data")

# Validate again after tampering
print("\nBlockchain Validation After Tampering:")
my_blockchain.is_chain_valid()
