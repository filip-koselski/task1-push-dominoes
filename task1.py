import argparse

def hamming_distance(string1, string2):
    return sum(s1 != s2 for s1, s2 in zip(string1, string2))

def backward(new_string):
    old_string = ''
    LBAR, RBAR, VBAR = 'L', 'R', '|'
    for i, element in enumerate(new_string):
        if element == LBAR or element == RBAR:
            if i == 0:
                next_ = new_string[i+1]
                if next_ == LBAR and element == LBAR:
                    old_string += VBAR
                else:
                    old_string += element
            elif i > 0 and i < len(new_string) - 1:
                next_ = new_string[i+1]
                prev_ = new_string[i-1]
                if prev_ == RBAR and element == RBAR and (next_ == LBAR or next_ == VBAR):
                    old_string += VBAR
                elif (prev_ == RBAR or prev_ == VBAR) and element == LBAR and next_ == LBAR:
                    old_string += VBAR
                else:
                    old_string += element
            else:
                prev_ = new_string[i-1]
                if prev_ == RBAR and element == RBAR:
                    old_string += VBAR
                else:
                    old_string += element
        else:
            old_string += element
    return old_string

def forward(input_string):
    new_string = ''
    LBAR, RBAR, VBAR = 'L', 'R', '|'
    for i, element in enumerate(input_string):
        if element == VBAR:
            if i == 0:
                next_ = input_string[i+1]
                if next_ == LBAR:
                    new_string += LBAR
                else:
                    new_string += VBAR
            elif i > 0 and i < len(input_string) - 1:
                next_ = input_string[i+1]
                prev_ = input_string[i-1]
                if next_ == LBAR and prev_ == RBAR:
                    new_string += '|'
                elif next_ == LBAR:
                    new_string += LBAR
                elif prev_ == RBAR:
                    new_string += RBAR
                else:
                    new_string += VBAR     
            else:
                prev_ = input_string[i-1]
                if prev_ == RBAR:
                    new_string += RBAR
                else:
                    new_string += VBAR
        else:
            new_string += element

    return new_string   

def iterate(string, how, X):
    mode = 'backward' if how == 'b' else 'forward'
    strings = []
    strings.append(string)
    print(f"Input domino chain:\n{string}\n")
    print(f"MODE: {mode.upper()}\n")
    for i in range(X):
        if how == 'b':
            string = backward(string)
        elif how == 'f':
            string = forward(string)
        strings.append(string)
        if hamming_distance(strings[-1], strings[-2]) == 0:
            print("Equilibrium state reached!")
            break
        print(string)
    print(f"\nDomino chain after {i+1} iterations:\n{string}")
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program iterates over domino string X times in forward or backward mode")
    parser.add_argument('input_string', metavar='input_string', type=str,
                    help="a domino chain of the string type containing at least 2 domino cubes (exemplary chain: '||RR||L||RL|')")
    parser.add_argument('mode', metavar='mode', type=str,
                    help="'f' - forward iteration or 'b' - backward iteration over chain")
    parser.add_argument('X', metavar='X', type=int,
                    help='number of iterations over chain > 0')
    args = parser.parse_args()
    if not set(args.input_string).issubset({'L','R','|'}) or len(args.input_string) < 2:
        parser.error("Wrong input string format!")
    if (args.mode == 'f' or args.mode == 'b') and args.X > 0:
        iterate(string=args.input_string, how=args.mode, X=args.X)
    else:
        parser.error("Wrong mode of iteration or non-positive number of iterations!")