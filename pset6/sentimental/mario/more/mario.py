from cs50 import get_int


def main():
    while True:
        height = get_int("Height: ")
        width = height
        if height >= 0 and height <= 23:
            break

    for i in range(1, height + 1):
        num_hashes = i
        num_spaces = width - num_hashes

        print(" " * num_spaces, end="")
        print("#" * num_hashes, end="")

        print("  ", end="")

        print("#" * num_hashes)


if __name__ == "__main__":
    main()
# from cs50 import get_int

#r = get_int ( input ("r: ") )
#while r < 1 or r > 8 :
   #r = get_int ( input ("r: ") )

#def hash(s,l) :
   #ln = ' ' * s + "#" * l + "#" * l
   #print(ln)

#l = 1
#while l <= r :   
   #s = r - l   
   #hash ( s , l )  
   #l += 1
