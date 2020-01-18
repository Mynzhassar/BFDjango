if __name__ == '__main__':
    my_list = []
    cmds = int (input ())
    for x in range (cmds) :
        s = input ().split ()
        cmd = s [0]
        args = s [1:]
        if cmd == 'insert' :
            my_list.insert (int (s [1]), int (s [2]))
        elif cmd == 'print' :
            print (my_list)
        elif cmd == 'remove' :
            for j in range (0, len (my_list)) :
                if my_list [j] == int (s [1]) :
                    my_list.remove (my_list [j])
                    break
        elif cmd == 'sort' :
            my_list.sort ()
        elif cmd == 'append' :
            my_list.append (int (s [1]))
        elif cmd == 'pop' :
            my_list.remove (my_list [len (my_list) - 1])
        elif cmd == 'reverse' :
            my_list.reverse ()



