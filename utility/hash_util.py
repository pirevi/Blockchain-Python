import hashlib as hl
import json

#__all__ = ['hash_string_256', 'hash_block'] # used to control whats exported from this file.

def hash_string_256(string):
    return hl.sha256(string).hexdigest()

def hash_block(block):
    hashable_block = block.__dict__.copy() # copy() is important or old values in the variable will be overwritten
    hashable_block['transactions'] = [tx.to_ordered_dict() for tx in hashable_block['transactions']]
    return hash_string_256(json.dumps(hashable_block, sort_keys=True).encode())
    # sorting is important, coz dictionary may screw up key-value orders