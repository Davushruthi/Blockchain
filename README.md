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

Index: 0, Hash: be1f2e768a057620510f7e1086a59615fb708959ab16edc5a4df275792701a8c, Data: Genesis Block
Index: 1, Hash: 8f4820d72b31d5285652c5df3254e963679ce8e123f502133547ad5c44fa0496, Data: Transaction 1
Index: 2, Hash: b6411ebb03102e44295c4baef12dbc10ed5f98a59f746fb817b827f9aed9386b, Data: Transaction 2

## Future Improvements  

- Add *block validation*.  
- Develop a *peer-to-peer network*.  

## Contributing  
Contributions are welcome! If you’d like to *improve* the project, feel free to:  
1. *Fork* the repository.  
2. Create a *new branch*.  
3. Submit a *pull request*.  

