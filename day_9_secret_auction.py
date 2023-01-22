from replit import clear
#HINT: You can call clear() to clear the output in the console.

def questions():
    name = input("What's your name?: ")
    bid = input("What's your bid?: $")
    secret_dict.append({"name": name, "bid": bid})
    more = input("Are there any bidders? Type 'yes' or 'no'. \n")
    return more

def highest_bid():
    highest_name = secret_dict[0]["name"]
    highest_bid = secret_dict[0]["bid"]
    for every in secret_dict:
      if(every["bid"] > highest_bid):
        highest_name = every["name"]
        highest_bid = every["bid"]
    print(f"The winner is {highest_name} with a bid of ${highest_bid}")

secret_dict = []
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the seceret auction program.")

print_questions = True

while (print_questions):
    more = questions()
    if (more == 'yes'):
        clear()
    else:
        clear()
        highest_bid()
        print_questions = False
