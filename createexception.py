class ValueWasTyped(Exception):
    def __str__(self):
        return 'number was typed'
def main():
    list = []

    for i in range(3):
        while True:
            try:
                num = int(input('Choose a number: '))
                break
            except ValueError:
                print('type a valid num')
        
        if num not in list:
            list.append(num)
        else:
            raise ValueWasTyped
        
if __name__ == '__main__':
    main()
