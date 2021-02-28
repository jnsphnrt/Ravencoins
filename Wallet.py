import crypto
# will maybe be important to send coins to someone else 
from Blockchain import Block, Blockchain
import json


# Defines a Crypto Wallet
class Wallet:
    public_key = None
    private_key = None

    def __init__(self):
        # generates the private key and the public key
        self.private_key = crypto.generate_sk()
        self.public_key = crypto.generate_pk(self.private_key)
        
        # opens a json file and writes configurations in it. For example: keys
        with open("Wallet.json", "w") as w_config:
            data = json.load(w_config)
            y = {"Private_Key": self.private_key,
                 "Public_Key": self.public_key}

            data.append(y)
            json.dump(data)

    # Function to send coins to someone else. Coming soon!
    def send_coins(self, amount, receiver):
        pass
