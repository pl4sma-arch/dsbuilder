try:
    import sys
    import ctypes
    import os
    os.system("clear")
    def everything():
        import os
        import json
        import pystyle
        from pystyle import Colorate, Colors
        import colorama
        from colorama import Fore
        colorama.init()
        print(Colorate.Horizontal(Colors.red_to_yellow,'''
        
         (      (                   (    (    (                 )             )               (     
         )\ )   )\ )     (          )\ ) )\ ) )\ )      (    ( /(   (      ( /(  (            )\ )  
        (()/(  (()/(   ( )\     (  (()/((()/((()/(      )\   )\())  )\     )\()) )\ )    (   (()/(  
         /(_))  /(_))  )((_)    )\  /(_))/(_))/(_))   (((_) ((_)\((((_)(  ((_)\ (()/(    )\   /(_)) 
        (_))_  (_))   ((_)_  _ ((_)(_)) (_)) (_))_    )\___  _((_))\ _ )\  _((_) /(_))_ ((_) (_))   
         |   \ / __|   | _ )| | | ||_ _|| |   |   \  ((/ __|| || |(_)_\(_)| \| |(_)) __|| __|| _ \  
         | |) |\__ \   | _ \| |_| | | | | |__ | |) |  | (__ | __ | / _ \  | .` |  | (_ || _| |   /  
         |___/ |___/   |___/ \___/ |___||____||___/    \___||_||_|/_/ \_\ |_|\_|   \___||___||_|_\                                                                               
        '''))
        if os.system("pkill Discord") == 0:
            print(Colorate.Horizontal(Colors.rainbow,"\n         [+] Successfully killed discord"))
        else:
            print(Colorate.Horizontal(Colors.rainbow,"\n         [-] Discord wasn't open or couldn't terminate Discord process"))
        build_num_input=input(Colorate.Horizontal(Colors.cyan_to_blue,"\n         Enter entire desired build number: "))


        with open("/opt/discord/resources/build_info.json", "r") as file:
            dataj = json.load(file)
        replace = dataj["version"]
        replace_num = build_num_input

        with open("/opt/discord/resources/build_info.json",'r') as filew:
            data_to_replace = filew.read()
            final=data_to_replace.replace(replace, replace_num)
        with open("/opt/discord/resources/build_info.json","w") as file_final_write:
            file_final_write.write(final)
        import time
        time.sleep(2)
        with open("/opt/discord/resources/build_info.json", "r") as file:
            dataj1 = json.load(file)
            version_result = dataj1["version"]
        if version_result == build_num_input:
            print(Colorate.Horizontal(Colors.green_to_white,"\n         [+] Succesfully changed build number!"))
        else:
            print(Colorate.Horizontal(Colors.red_to_white,"\n         [-] Something malfunctioned.."))

    def is_admin():
        if os.name == 'nt':
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False
        else:
            return os.getuid() == 0

    if is_admin():
        everything()
    else:
        print("Please, to make this program function, it needs permissions to access the root directory, you can give them by running the file using 'sudo'")
        sys.exit(1)

except KeyboardInterrupt:
    import colorama
    from colorama import Fore
    print(Fore.RED+"         [^C] Detected keyboard interrupt, goodbye!")