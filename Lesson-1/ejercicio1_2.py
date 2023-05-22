# Author: Daniel Rodriguez Amezaga

def main():
    f = None
    try:
        f = open('file.txt', 'r', encoding='utf-8')
        print(f.read())

    except FileNotFoundError:
        print('File not found!')

    except LookupError:
        print('An unknown coding has been specified!')

    except UnicodeDecodeError:
        print('Decoding error when reading the file!')
        
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()



