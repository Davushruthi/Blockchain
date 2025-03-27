# Simple Blockchain in Python  

This is a basic *Python Blockchain* implementation that allows adding blocks with transactions and securing them using *SHA-256 hashing*.  

## Features  
- Automatically creates a *Genesis Block*.  
- Allows adding *new blocks* with transaction data.  
- Uses *SHA-256 hashing* for security.  
- Demonstrates a *simple blockchain structure*.  

## Installation & Setup  
1. *Clone the Repository:*  
   Using HTTPS:  
   sh  
   git clone https://github.com/Davushruthi/Blockchain.git  
     
   OR using SSH:  
   sh  
   git clone git@github.com:Davushruthi/Blockchain.git  
     
2. *Navigate to the Project Folder:*  
   sh  
   cd Blockchain  
     
3. *Run the Script:*  
   sh  
   python blockchain.py  
   

## Usage  
- The script initializes a *blockchain* with a *genesis block*.  
- You can *add new blocks* by modifying the script:  
  python  
  my_blockchain.add_block("Transaction data")  
    
- The blockchain prints each block's *index, hash, and data*.  

## Example Output  

Index: 0, Hash: 00007e5c26b901048386ad8b344a546769b578a2f3db28185e4b23c099ac82d6, Nonce: 29416, Data: Genesis Block
Index: 1, Hash: 00002e606321b0218e097222d35a191aeeba4931c041b62240edb8af8fc6c4ca, Nonce: 15973, Data: Transaction 1
Index: 2, Hash: 0000cd51c4d69953de68989efce5bc9f8ac104c0f4b787fcffeb41349d5f74bb, Nonce: 32984, Data: Transaction 2

Initial Blockchain Validation:
Blockchain is valid.
Block 1 tampered with! New data: Hacked Data

Blockchain Validation After Tampering:
Block 1 has been tampered with!


## Future Improvements  

- Add *block validation*.  
- Develop a *peer-to-peer network*.  

## Contributing  
Contributions are welcome! If you’d like to *improve* the project, feel free to:  
1. *Fork* the repository.  
2. Create a *new branch*.  
3. Submit a *pull request*.  

