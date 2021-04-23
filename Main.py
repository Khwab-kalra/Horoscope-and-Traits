from datetime import datetime

def set_Sign(date):
    z = ""
    if (date.day > 20 and date.month == 3) or (date.day < 20 and date.month == 4):
        z = "Aries"
    elif (date.day > 19 and date.month == 4) or (date.day < 21 and date.month == 5):
        z = "Taurus"
    elif (date.day > 20 and date.month == 5) or (date.day < 21 and date.month == 6):
        z =  "Gemini"
    elif (date.day > 20 and date.month == 6) or (date.day < 23 and date.month == 7):
        z = "Cancer"
    elif (date.day > 22 and date.month == 7) or (date.day < 23 and date.month == 8):
        z = "Leo"
    elif (date.day > 22 and date.month == 8) or (date.day < 23 and date.month == 9):
        z = "Virgo"
    elif (date.day > 22 and date.month == 9) or (date.day < 23 and date.month == 10):
        z = "Libra"
    elif (date.day > 22 and date.month == 10) or (date.day < 22 and date.month == 11):
        z =  "Scorpio"
    elif (date.day > 21 and date.month == 11) or (date.day < 22 and date.month == 12):
        z = "Sagittarius"
    elif (date.day > 21 and date.month == 12) or (date.day < 20 and date.month == 1):
        z =  "Capricorn"
    elif (date.day > 19 and date.month == 1) or (date.day < 19 and date.month == 2):
        z = "Aquarius"
    elif (date.day > 18 and date.month == 2) or (date.day < 21 and date.month == 3):
        z = "Pisces"
    return z

def set_Scope(zodiac):
    if zodiac == "Aries":
        return "Eager, Dynamic, Quick and competitive"
    elif zodiac == "Taurus":
        return "Strong, Dependable, Sensual, Creative"
    elif zodiac == "Gemini":
        return "Versatile, expressive, curious and Kind"
    elif zodiac == "Cancer":
        return "Intuitive, Sentimental, Compassionate and protective"
    elif zodiac == "Leo":
        return "Dramatic, Outgoing, Fiery and Self-assured"
    elif zodiac == "Virgo":
        return "Practical, Loyal, Gentle and analytical"
    elif zodiac == "Libra":
        return "Social, Fair-minded, Diplomatic and Gracious"
    elif zodiac == "Scorpio":
        return "Passionate, Stubborn, Resourceful and Brave"
    elif zodiac == "Sagittarius":
        return "Extroverted, Optimistic, Funny and Generous"
    elif zodiac == "Capricorn":
        return "Serious, Independent, Disciplined and tenacious"
    elif zodiac == "Aquarius":
        return "Deep, Imaginative, Original and Uncompromising"
    elif zodiac == "Pisces":
        return "Affectionate, Empathetic, Wise and Artistic"

def run():
    date_string = input("Enter your birthdate : ")
    try:
        date_object = datetime.strptime(date_string, "%d %b %y")
    except ValueError:
        try:
            date_object = datetime.strptime(date_string, "%d %B %y")
        except ValueError:
                try:
                    date_object = datetime.strptime(date_string, "%d %b %Y")
                except ValueError:
                    try:
                        date_object = datetime.strptime(date_string, "%d %B %Y")
                    except ValueError:
                        try:
                            date_object = datetime.strptime(date_string, "%d %m %Y")
                        except ValueError:
                            try:
                                date_object = datetime.strptime(date_string, "%d %m %y")
                            except:
                                exit("Invalid date!!!")
    zodiac = set_Sign(date_object)
    horror_Scope = set_Scope(zodiac)
    print(f"Zodiac Sign : {zodiac}")
    print(f"Zodiac Traits : {horror_Scope}")
    return

while(True):
    print("\n===========================================================================================================\n")
    print("Enter 1 to check your Zodiac Sign and Traits")
    print("Enter 0 to Exit.!")
    print("\n===========================================================================================================\n")
    if input() == "0":
        print("Bye, Have a Great Day!!!")
        print("\n===========================================================================================================\n")
        break
    else:
        run()
