from operator import mul, add

# this a global frame
def sqaure(square):
    return mul(square, square)

if __name__ == '__main__':
    # this is a local frame, and the value of square is -2
    # 'square' will be passed to the function 'sqaure' as '2'
    print(sqaure(-2))
    