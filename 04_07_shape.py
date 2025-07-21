def shape(x, char1, y, char2):
# Code of line function from previous exercise 
    def line(length,char):
        if char == "":
            print( length * "*")
        else:
            print(length * char[0])
    # Print the triangle
    i=1
    while i <= x:
        line(i, char1)
        i +=1
    # Print the retangle
    j=1
    while j <= y:
        line(x, char2)
        j +=1
# Test the function by calling it within the following block:
if __name__ == "__main__":
    shape(5, "X", 3, "*")
