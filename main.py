import torch
import sys

def check_cuda():
    if torch.cuda.is_available():
        return True
    else:
        return False

def main():
    if check_cuda():
        sys.exit()
    else:
        sys.exit("CUDA not available")

if __name__ == "__main__":
    main()
