import hashlib
import json


# class of a block
class Block:
    prev_Hash = None  # hash of the previous Block in the Blockchain
    nonce = -1

    data = None
    current_Hash = None  # hash of the current Block

    # constructor that defines a Block in a chain
    def __init__(self, prev_Hash, data):
        # just some variable assignment
        self.prev_Hash = prev_Hash
        self.data = data

    @property
    def BlockList(self):
        return [self.current_Hash, self.prev_Hash, self.data]

        # just a nice way to format an output

    @property
    def blockString(self):
        return "{0}-{1}-{2}-{3}".format(
            self.prev_Hash,
            self.data,
            self.nonce,
            self.timestamp
        )

    def mine(self, difficulty):
        found = False
        while not found:
            self.nonce += 1
            self.current_Hash = self.hash()
            if self.current_Hash[0:difficulty] == '0' * difficulty:
                found = True

    # obviously the hashing part of the chain
    def hash(self):
        return hashlib.sha256(bytes(self.blockString, 'utf-8')).hexdigest()


# defines the Blockchain
class Blockchain:
    blocks = []
    current_Hash = ""

    # the difficulty describes how many digits of the hash have to be zero
    # 4 is just for testing, in the real world it should be 6
    difficulty = 4

    # constructor: Just to define the current Hash to append to the Blockchain

    # adds a new block
    # don't use manually
    def add(self, block):

        block.mine(self.difficulty)
        self.current_Hash = block.current_Hash
        

        if self.blocks:
            prev_Hash = self.current_Hash
        else:
            prev_Hash = 0

        with open("blockchain.json", 'r+') as fp:
            json_data = json.load(fp)
            temp = json_data['Blocks']

            y = {"prevHash": prev_Hash,
                 "nonce": block.nonce,
                 "data": block.data}

            temp.append(y)
        self.writeJson(json_data)

        self.blocks.append([prev_Hash, block.nonce, block.data])

    # returns the last block
    def lastBlock(self):
        return self.blocks[-1]

    # adds a new block to the chain
    def buildBlock(self, data):
        if self.lastBlock:
            block = Block(self.current_Hash, data)
            self.add(block)
        else:
            raise Exception('Missing Genisis Block')

    def writeJson(self, data):
        with open('blockchain.json', 'w') as fp:
            json.dump(data, fp, indent=4)
