import hashlib
import datetime
import json

class AuthChain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def register_user(self, username, password):
        previous_block = self.get_previous_block()
        previous_proof = previous_block['proof']
        proof = self.proof_of_work(previous_proof)
        block = self.create_block(proof, self.hash(previous_block))
        block['data'] = {'username': username, 'password': hashlib.sha256(password.encode()).hexdigest()}
        return block['index']

    def login_user(self, username, password):
        for block in self.chain[1:]:
            if block.get('data') and block['data']['username'] == username:
                stored_password = block['data']['password']
                if stored_password == hashlib.sha256(password.encode()).hexdigest():
                    return True
        return False



