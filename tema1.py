from test import *

# main function
def main():
    input_files = ['input1.txt', 'input2.txt', 'input3.txt']

    for i in range(3):
        
        env = init_env(input_files[i])
        
        test = Graph(env, i)
        
        test.test()

if __name__ == "__main__":
    main()
