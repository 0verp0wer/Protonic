"""                                                             
___  ____ ____ ___ ____ _  _ _ ____         Welcome to Protonic 1.0, the first obfuscated challenge made by over_on_top on discord aka overpower.
|__] |__/ |  |  |  |  | |\ | | |            Difficulty: [35/100]
|    |  \ |__|  |  |__| | \| | |___         
                                           If you are still reading this, it means you want to de-obfuscate this challenge, I wish you have fun and good luck (you will need it)
                                           
                                           Goal of the challenge: create a hash generator
                                           Goal of the challenge for nerds: create a hash generator and find the other 2 hash hidden in the code
"""

import pickle

vglobals = vars(__builtins__)

class VM:
    def __init__(self, instructions):
        self.bytecode, self.consts, self.names = pickle.loads(instructions)
        
    def __call__(self, *args):    
        stack = []
        pop = stack.pop
        push = stack.append
        cx = 0
        vlocals = vars(__builtins__)
        
        for i in range(len(args)):
            vlocals[self.names[i]] = args[i]
        
        while cx < len(self.bytecode):
            opc = self.bytecode[cx]
            opa = self.bytecode[cx + 1]
            
            match(opc):
                case 1:
                    const = self.consts[opa]
                    push(const)
                case 2:
                    const = pop()
                    name = self.names[opa]
                    vlocals[name] = const
                case 3:
                    name = self.names[opa]
                    push(vlocals[name])
                case 6:
                    b = pop()
                    a = pop()
                    push(a + b)
                case 7:
                    b = pop()
                    a = pop()
                    push(a - b)
                case 8:
                    b = pop()
                    a = pop()
                    push(a * b)
                case 9:
                    b = pop()
                    a = pop()
                    push(a / b)
                case 10:
                    b = pop()
                    a = pop()
                    push(a // b)
                case 11:
                    b = pop()
                    a = pop()
                    push(a % b)
                case 12:
                    b = pop()
                    a = pop()
                    push(a ** b)
                case 13:
                    b = pop()
                    a = pop()
                    push(a << b)
                case 14:
                    b = pop()
                    a = pop()
                    push(a >> b)
                case 15:
                    b = pop()
                    a = pop()
                    push(a | b)
                case 16:
                    b = pop()
                    a = pop()
                    push(a ^ b)
                case 17:
                    b = pop()
                    a = pop()
                    push(a & b)
                case 18:
                    b = pop()
                    a = pop()
                    push(a @ b)
                case 19:
                    args = []
                    for _ in range(opa):
                        args.insert(0, pop())
                    function = pop()
                    push(function(*args))
                case 20:
                    bytecode = pop()
                    name = self.names[opa]
                    vglobals[name] = VM(bytecode)
                case 22:
                    name = self.names[opa]
                    vglobals[name] = __import__(name)
                case 24:
                    if not pop():
                        cx = opa
                        continue
                case 25:
                    cx = opa
                    continue
                case 21:
                    return pop()
                case 23:
                    b = pop()
                    a = pop()
                    match opa:
                        case 1:
                            push(a == b)
                        case 2:
                            push(a != b)
                        case 3:
                            push(a < b)
                        case 4:
                            push(a <= b)
                        case 5:
                            push(a > b)
                        case 6:
                            push(a >= b)
                        case 7:
                            push(a is b)
                        case 8:
                            push(a is not b)
                        case 9:
                            push(a in b)
                        case 10:
                            push(a not in b)
                case 26:
                    b = pop()
                    a = pop()
                    push(a and b)
                case 27:
                    b = pop()
                    a = pop()
                    push(a or b)
                case 28:
                    method_name = pop()
                    name = pop()
                    push(getattr(name, method_name))
                case 29:
                    values = []
                    for _ in range(opa):
                        values.insert(0, pop())
                    push(tuple(values))
                case 30:
                    values = []
                    for _ in range(opa):
                        values.insert(0, pop())
                    push(values)
                case 32:
                    slice_value = pop()
                    push(pop()[slice_value])
                case 31:
                    step = pop()
                    stop = pop()
                    start = pop()
                    push(slice(start, stop, step))
                case 4:
                    const = pop()
                    name = self.names[opa]
                    vglobals[name] = const
                case 5:
                    name = self.names[opa]
                    push(vglobals[name])
                    
            cx += 2
        
vm = VM(b'\x80\x04\x95\x92\r\x00\x00\x00\x00\x00\x00]\x94(K\x16K\x00K\x16K\x01K\x16K\x02K\x05K\x03K\x01K\x00K\x13K\x01K\x05K\x04K\x01K\x01K\x13K\x01K\x05K\x05K\x01K\x02K\x13K\x01K\x05K\x06K\x01K\x03K\x13K\x01K\x05K\x07K\x01K\x04K\x13K\x01K\x04K\x08K\x05K\tK\x01K\x05K\x13K\x01K\x04K\nK\x05K\x0bK\x01K\x06K\x13K\x01K\x04K\x0cK\x01K\x07K\x14K\rK\x01K\x08K\x14K\x0eK\x01K\tK\x14K\x0fK\x05K\x10K\x05K\x11K\x05K\x12K\x05K\x13K\x13K\x02K\x17K\x01K\x18K^K\x05K\x14K\x01K\nK\x13K\x01K\x05K\x15K\x01K\x0bK\x13K\x01K\x19K\xacK\x05K\x16K\x01K\x0cK\x17K\x01K\x18KtK\x05K\x17K\x01K\rK\x13K\x01K\x05K\x18K\x01K\x0eK\x13K\x01K\x19K\xacK\x05K\x19K\x05K\x1aK\x01K\x0fK\x1cK\x00K\x01K\x10K\x01K\x11K\x1cK\x00K\x13K\x00K\x13K\x01K\x01K\x12K\x1cK\x00K\x13K\x00K\x17K\x01K\x18K\x9eK\x05K\x1bK\x01K\x13K\x13K\x01K\x05K\x1cK\x01K\x14K\x13K\x01K\x19K\xacK\x05K\x1dK\x01K\x15K\x13K\x01K\x05K\x1eK\x01K\x16K\x13K\x01K\x19K\xace]\x94(\x8c\x17Welcome to Protonic 1.0\x94\x8cFYour task is to create a hash generator to be able to bypass the login\x94\x8c\x14Difficulty: [30/100]\x94\x8c+I hope you enjoy this challenge, have fun!\n\x94\x8c\x15Insert the username: \x94\x8c\x15Insert the password: \x94\x8c\x17Insert the hash value: \x94B@\x01\x00\x00\x80\x04\x955\x01\x00\x00\x00\x00\x00\x00]\x94(K\x03K\x03K\x03K\x04K\x17K\x01K\x18K\x0eK\x01K\x00K\x15K\x00K\x19K\x0eK\x03K\x05K\x03K\x06K K\x00K\x01K\x01K\x17K\x01K\x18K K\x01K\x02K\x15K\x00K\x19KFK\x03K\x07K\x03K\x08K\x03K\tK\x03K\nK K\x00K\x13K\x01K\x01K\x03K\x06K\x00K\x13K\x01K\x03K\x0bK\x03K\x0cK\x03K\rK\x01K\x04K\x06K\x00K\x03K\x0eK\x13K\x03K\x06K\x00K\x15K\x00K\x19KFe]\x94(\x8c\x00\x94\x8c\x01c\x94h\x03K\x01K\x01e]\x94(\x8c\x05value\x94\x8c\x07counter\x94\x8c\x06length\x94\x8c\x07counter\x94\x8c\x06length\x94\x8c\x05value\x94\x8c\x07counter\x94\x8c\x03chr\x94\x8c\x03ord\x94\x8c\x05value\x94\x8c\x07counter\x94\x8c\x11final_calculation\x94\x8c\x05value\x94\x8c\x07counter\x94\x8c\x06length\x94e\x87\x94.\x94B\x08\x04\x00\x00\x80\x04\x95\xfd\x03\x00\x00\x00\x00\x00\x00]\x94(K\x03K\x03K\x01K\x00K\x1cK\x00K\x03K\x04K\x03K\x05K\x13K\x01K\x01K\x01K\x1cK\x00K\x13K\x00K\x13K\x01K\x01K\x02K\x1cK\x00K\x13K\x00K\x02K\x06K\x03K\x07K\x01K\x03K\x1cK\x00K\x01K\x04K\x01K\x05K\x1cK\x00K\x01K\x06K\x03K\x08K\x03K\tK\x01K\x07K\x01K\x08K\x01K\tK\x1fK\x00K K\x00K\x1eK\x03K\x13K\x01K\x01K\nK\x1cK\x00K\x13K\x00K\x13K\x01K\x01K\x0bK\x1cK\x00K\x13K\x00K\x02K\nK\x01K\x0cK\x02K\x0bK\x01K\rK\x02K\x0cK\x01K\x0eK\x18K\xc4K\x03K\rK\x01K\x0fK\x1cK\x00K\x01K\x10K\x01K\x11K\x1cK\x00K\x01K\x12K\x03K\x0eK\x08K\x00K\x03K\x0fK\x1eK\x02K\x13K\x01K\x01K\x13K\x1cK\x00K\x13K\x00K\x13K\x01K\x01K\x14K\x1cK\x00K\x13K\x00K\x02K\x10K\x03K\x11K\x03K\x12K\x01K\x15K\x01K\x16K\x01K\x17K\x1fK\x00K K\x00K\x01K\x18K\x13K\x02K\x01K\x19K\x0bK\x00K\x01K\x1aK\x17K\x01K\x03K\x13K\x01K\x1bK\x17K\x01K\x1bK\x00K\x18K\xbaK\x03K\x14K\x03K\x15K\x01K\x1cK\x01K\x1dK\x01K\x1eK\x1fK\x00K K\x00K\x06K\x00K\x02K\x16K\x19K\xc4K\x19K\xbaK\x03K\x17K\x01K\x1fK\x06K\x00K\x02K\x18K\x19KTK\x03K\x19K\x01K K\x01K!K\x01K"K\x1fK\x00K K\x00K\x03K\x1aK\x05K\x1bK\x01K#K\x03K\x1cK\x05K\x1dK\x13K\x01K\x13K\x03K\x06K\x00K\x15K\x00e]\x94(\x8c\x03md5\x94\x8c\x06encode\x94\x8c\thexdigest\x94\x8c\x03md5\x94\x8c\x01,\x94\x8c\x04join\x94\x8c\toverpower\x94NNK\x02\x8c\x06encode\x94\x8c\thexdigest\x94\x8c\x00\x94K\x01\x88\x8c\x06sha256\x94h\x06\x8c\x04join\x94\x8c\x0bover_on_top\x94\x8c\x06encode\x94\x8c\thexdigest\x94NK\rNK\x10K\x02K\x00K\x03NK\rNK\x01K\x00K\rK\x02K\x00e]\x94(\x8c\x0fsecret_username\x94\x8c\x08password\x94\x8c\ttimestamp\x94\x8c\x07hashlib\x94\x8c\x03str\x94\x8c\ttimestamp\x94\x8c\x10hashed_timestamp\x94\x8c\x07hashlib\x94\x8c\x0fsecret_username\x94\x8c\x10hashed_timestamp\x94\x8c\x0fsecret_password\x94\x8c\nhashed_key\x94\x8c\x07counter\x94\x8c\x07hashlib\x94\x8c\x07counter\x94\x8c\x0fsecret_password\x94\x8c\x0egenerated_hash\x94\x8c\x03int\x94\x8c\x0egenerated_hash\x94\x8c\x07counter\x94\x8c\nhashed_key\x94\x8c\x0egenerated_hash\x94\x8c\nhashed_key\x94\x8c\x07counter\x94\x8c\x07counter\x94\x8c\nhashed_key\x94\x8c\x11final_calculation\x94\x8c\x08password\x94\x8c\x03len\x94\x8c\x08password\x94e\x87\x94.\x94BU\x02\x00\x00\x80\x04\x95J\x02\x00\x00\x00\x00\x00\x00]\x94(K\x03K\x02K\x03K\x03K\x01K\x00K\x1cK\x00K\x13K\x00K\x03K\x04K\x01K\x01K\x1cK\x00K\x13K\x00K\x01K\x02K\x0bK\x00K\x07K\x00K\x13K\x01K\x02K\x05K\x03K\x06K\x01K\x03K\x1cK\x00K\x05K\x07K\x01K\x04K\x1cK\x00K\x13K\x00K\x13K\x01K\x01K\x05K\x1cK\x00K\x13K\x00K\x02K\x08K\x03K\tK\x01K\x06K\x1cK\x00K\x03K\nK\x01K\x07K\x01K\x08K\x01K\tK\x1fK\x00K K\x00K\x01K\nK\x1cK\x00K\x13K\x00K\x13K\x01K\x01K\x0bK\x1cK\x00K\x13K\x00K\x02K\x0bK\x03K\x0cK\x03K\rK\x05K\x0eK\x03K\x0fK\x13K\x03K\x02K\x10K\x01K\x0cK\x03K\x11K\x15K\x00e]\x94(\x8c\x04time\x94\x8c\x04time\x94M`T\x8c\tb64encode\x94\x8c\x06encode\x94\x8c\x06decode\x94\x8c\x03md5\x94NNK\x02\x8c\x06encode\x94\x8c\thexdigest\x94\x8c,second secret solution: over_secret_solution\x94e]\x94(\x8c\x08username\x94\x8c\x08password\x94\x8c\x03int\x94\x8c\x04time\x94\x8c\x04time\x94\x8c\ttimestamp\x94\x8c\x06base64\x94\x8c\x08username\x94\x8c\rtemp_username\x94\x8c\x07hashlib\x94\x8c\rtemp_username\x94\x8c\x0fsecret_username\x94\x8c\x18generate_hashed_password\x94\x8c\x0fsecret_username\x94\x8c\x08password\x94\x8c\ttimestamp\x94\x8c\x0fpassword_hashed\x94\x8c\x0fpassword_hashed\x94e\x87\x94.\x94\x8c\x93\nCongratulations, you managed to solve the challenge, now try to find the other 2 secret solutions and later don\'t forget to contact me on Discord!\x94\x8c\x14Discord: over_on_top\x94\x8c\x14over_secret_solution\x94\x8cy\nCongratulations, you managed to find the first secret solution, now get back to work and try to find the other solutions\x94\x8c\nGood luck!\x94\x8c\x03md5\x94\x8c\x10over_on_top_1234\x94\x8c\x06encode\x94\x8c\thexdigest\x94\x8cz\nCongratulations, you managed to find the second secret solution, now get back to work and try to find the other solutions\x94\x8c\nGood luck!\x94\x8c\x15[404] Failed to login\x94\x8c\x13Please try again...\x94e]\x94(\x8c\x04time\x94\x8c\x06base64\x94\x8c\x07hashlib\x94\x8c\x05print\x94\x8c\x05print\x94\x8c\x05print\x94\x8c\x05print\x94\x8c\x05input\x94\x8c\x08username\x94\x8c\x05input\x94\x8c\x08password\x94\x8c\x05input\x94\x8c\nhash_value\x94\x8c\x11final_calculation\x94\x8c\x18generate_hashed_password\x94\x8c\x13generate_hash_value\x94\x8c\nhash_value\x94\x8c\x13generate_hash_value\x94\x8c\x08username\x94\x8c\x08password\x94\x8c\x05print\x94\x8c\x05print\x94\x8c\nhash_value\x94\x8c\x05print\x94\x8c\x05print\x94\x8c\nhash_value\x94\x8c\x07hashlib\x94\x8c\x05print\x94\x8c\x05print\x94\x8c\x05print\x94\x8c\x05print\x94e\x87\x94.')

vm()
