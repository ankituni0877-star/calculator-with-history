history='history.txt'

def show_history():
    file = open(history,'r')
    lines = file.readlines()
    if len(lines)==0:
        print("no history found")
    else :
        for lines in reversed(lines):
            print(lines.strip())
    file.close()

def clear_history():
    file=open(history,'w')
    file.close()
    print('history cleared')

def save_to_history(equation ,result):
    file =open(history,'a')
    file.write(equation + '=' + str(result)+"\n")
    file.close()

def calculate(user_input):
    parts =user_input.split()
    if len(parts) !=2:
        print("invalid inputs")
        return

    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])  

    if op=="+":
        result=num1+num2
    elif op=='-':
        result=num1-num2
    elif op=='/':
        result=num1/num2
    elif op=='*':
        result=num1*num2
    else :
        print('invalid operator')

    if result==int(result) :
        result=int(result)
    print('result :',result)
    save_to_history(user_input,result)

def main():
    print('--calculator -- with(history)')
    while(True):
        user_input = input('enter calculation or command (history : hist ,clear_history:clear ,exit: ex)')
        if user_input=='exit' or user_input=='ex' :
            print('good bye')
            break
        elif user_input=='history' or user_input=='hist':
            show_history()
        elif user_input=="clear history" or user_input=='clear' :
            clear_history()
        else :
            calculate(user_input)
main()            
                    