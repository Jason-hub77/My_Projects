def main():
    millis=input("Enter time in milliseconds ")
    if millis=="Exit":
       print("Exiting the program... Good Bye")
    else:
        if millis.isdigit():
            millis = int(millis)
            if millis <1000 and millis>0:
                print(f"just {millis} millisecond/s")
            elif millis >1000 :
                seconds=(millis//1000)%60
                minutes=(millis//(1000*60))%60
                hours=(millis//(1000*60*60))%24
                if minutes==0 and hours==0:
                    print(f"{seconds} second/s")
                elif seconds==0 and hours==0:
                    print(f"{minutes} minute/s")
                elif seconds==0 and minutes==0:
                    print(f"{hours} hour/s")
                elif minutes==0:
                    print(f"{hours} hour/s, {seconds} second/s")
                elif seconds==0:
                    print(f"{hours} hour/s, {minutes} minute/s")
                elif hours==0:
                    print(f"{minutes} minute/s, {seconds} second/s")
                else:
                    print(f"{hours} hour/s, {minutes} minute/s, {seconds} second/s")
            else:
                print("Not Valid Input !!!")
        else:
            print("Not Valid Input !!!")
main()