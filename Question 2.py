def descOrder(s):
    s.sort(reverse=True)
    str1 = ''.join(s)
    print("The resulting string is: ",str1)
def main():
    s = list("HELLO It Is A String")
    descOrder(s)
if __name__ == "__main__":
    main()