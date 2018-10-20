from parser import Parser
from cube_attack import RandomCubeAttack
from trivium_cube_attack import TriviumCubeAttack

def main():

    args = Parser().args

    if args.mode=="random":

        ca = RandomCubeAttack(degree=args.degree)

        sps = ca.execute_offline_attack()
        equations = ca.execute_online_attack(sps)

        print(ca.possible_maxterms)

    elif args.mode=="trivium":

        f = TriviumCubeAttack(args.n_rounds)

        print(f.test_maxterm("v2v13v20v24v37v42v43v46v53v55v57v67", 675))

main()