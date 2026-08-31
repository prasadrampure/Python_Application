import numpy as np

def ReLU(z):
    return max(0,z)

def Marvellous_Neuron_Forword(input,weights,bias):
    print("Inputs are (x) :",input)
    print("Weights are (w) :",weights)
    print("bias are (b) :",bias)

    z = 0

    for i in range(len(input)):
        z = z + (input[i] * weights[i])

    z = z + bias
    #z = sum(w * x for w, x in zip(weights,input)) + bias

    print("Weighted Sum :",z)

    y = ReLU(z)

    return y

def main():
    print("Marvellous Neural Network")

    input = [1.0,2.0,3.0]
    weights = [0.6,0.4,-0.2]
    bias = 0.5

    result = Marvellous_Neuron_Forword(input,weights,bias)

    print("Predicted result :",result)

if __name__ == "__main__":
    main()