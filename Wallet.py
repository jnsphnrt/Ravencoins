import crypto
import json
import Blockchain


# Defines a Crypto Wallet
class Wallet:
    public_key = None
    private_key = None

    def __init__(self):
        # generates the private key and the public key
        # I call it sk for secret key, because pk for private key is obviously a bad name
        self.private_key = crypto.generate_sk()
        self.public_key = crypto.generate_pk(self.private_key)
        
        # opens a json file and writes configurations in it. For example: keys
        with open("Wallet.json", "w") as w_config:
            data = json.load(w_config)
            y = {"Private_Key": self.private_key,
                 "Public_Key": self.public_key}

            data.append(y)
            json.dump(data)

    def send_coins(self, amount, receiver):
        # I know it needs much more than this. This is just provisional.
        Blockchain.buildBlock(amount)
