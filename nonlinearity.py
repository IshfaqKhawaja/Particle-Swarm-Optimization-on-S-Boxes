# program returns array specifying nonlinearity of each component function
# takes input as a 1-D array as S-Box.
###########################################################################
#finds Walsh Transform of truth table(f)
def fwt(f):  # f is a Boolean function represented as a TT(0/1) of length 2^n
    import math
    wf = []
    for x in f:
        if x == 0:
            wf.append(1)
        else:  
            wf.append(-1)
    order = len(f)  # order = 2^n
    n = int(math.log(order, 2))
    size = int(math.floor(order / 2))
    while size >= 1:
        left = 0
        while left < order - 1:
            for p in range(int(size)):
                right = left + int(size)
                a = wf[left]
                b = wf[right]
                wf[left] = a + b
                wf[right] = a - b
                left = left + 1
            left = right + 1
        size = int(math.floor(size / 2))
    # print"\tWalsh transform of function's truth table is",
    # print wf
    return wf

############################################################################
#finds non-linearity of an n-variable boolean function 'f'
def bf_nonlinearity(f, n):
    import math
    fw = fwt(f)
    #find modulus of each element in Walsh transform
    for i in range(len(fw)):
        fw[i] = abs(fw[i])
    # nonlinearity from the Walsh transform
    x = ((2 ** (n - 1)) - (max(fw) / 2))
    # print"\tNL of function is",
    # print x
    return x

##############################################################################
#converts num to binary form (no of bits in binary representation = length) 
def binary(num, length):
    binary_string_list = list(format(num, '0{}b'.format(length)))
    #print("num,binary String List",num,binary_string_list)
    return [int(digit) for digit in binary_string_list]

##############################################################################
#returns array of NL of each component function for sbox S
def non_linearity(S):  
    import math
    order = len(S)
    n = int(math.log(order, 2))
    nl_array = []  # nl_array[] stores calculated NL for each function yi
    for bitno in range(n):
        f = []
        for index in range(order):  #for each element in Sbox
            binary_value = binary(S[index], n)
            bit = binary_value[bitno]
            f.append(bit)
        #print"***********************************************"
        #print "Funct no %d" % bitno,
        #print(f)
        bfnl = bf_nonlinearity(f, n)
        nl_array.append(bfnl)
    return sum(nl_array)/len(nl_array)


#binary(100,7)


