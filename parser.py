import argparse

class Parser():
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--mode", default="trivium", choices=["random", "trivium"],
                            help="What polynomial to perform the attack on ?\
                                  a random polynomial or trivium ?")

        parser.add_argument("--n_rounds", default=672, type=int,
                            help="number of initialisation rounds for trivium ?")

        parser.add_argument("--degree", default=3, type=int,
                            help="If mode is random, specify the degree of \
                                  the polynomial. Ignored in the case of trivium")
        #
        # parser.add_argument("--private_key", default="-1", help="private key of the scheme if random")

        self.parser = parser

        self.args = self.parser.parse_args()

def str2bool(self, text):
    if text == 'True':
        arg = True
    elif text == 'False':
        arg = False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
    return arg

if __name__=="__main__":
    h = Parser()
    print(h.args.__dict__)
