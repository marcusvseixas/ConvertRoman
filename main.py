import ConvertRoman as cr

def main():
    decision = input("Digite o valor que deseja converter: ")
    print('\r' "Digitou " + decision + " e foi convertido para ", end="")
    try :
        print(cr.to_roman(int(decision)))
    except :
        print(cr.from_roman(str(decision)))


if __name__ == "__main__":
    main()