import random


class Task_10:
    def __init__(self, S_box, Li_1, permutation=False):
        self.S_box = S_box
        self.Li_1 = Li_1
        self.permutation = permutation
        pass

    def run(self):
        # 1. Apply permutation on S-box if needed
        if self.permutation:
            permutation_order = Task_10.generate_randomly()
            self.S_box = Task_10.permutate(self.S_box, permutation_order)

        # 2.Xor P_S_box with L_i-1
        Ri = self.xor()
        return Ri


    def xor(self):
        # 1. Convert inputs to integers if they're binary strings
        if isinstance(self.S_box, str):
            self.S_box = int(self.S_box, 2)
        if isinstance(self.Li_1, str):
            self.Li_1 = int(self.Li_1, 2)

        # 2. Perform XOR operation
        result = self.S_box ^ self.Li_1

        # 3. Remove '0b' prefix
        binary_result = bin(result)[2:]

        # 4. Ensure the result is 32 bits by padding with zeros if needed
        binary_result = binary_result.zfill(32)

        return binary_result

    @staticmethod
    def permutate(S_box, permutation_order):
        result = []
        for i in permutation_order:
            result.append(S_box[i])
        return ''.join(str(bit) for bit in result)


    @staticmethod
    def generate_randomly(length=32):
        return [random.randint(0, 1) for _ in range(length)]





