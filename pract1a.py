command = ""
started = False
while True:
    command = input(">").lower()
    if command =='start':
        if started:
                print('car already started')
        else:  
            started = True
            print('Car started')
    elif command =='stop':
        if not started:
            print('car already stopped')
        else:
            started = False
            print('Car stopped')
    elif command == 'help':
              print("""
start = To start the car
stop = To stop the car
quit = To quit
                """)
    elif command == 'quit':
            print('quit car')
            break
    else:
            print('sorry, i dont understand')

