#integration project
"""Elizabeth Gonzalez-Obando
This program is used to help the user recieve outfit inspiration within many trending aesthetics today.
The user should be able to pick an aesthetic they'd like to pursue and recieve recommendations on what to wear, including examples of shoes, jewelry, tops, and bottoms. As well as see the average cost for each outfit. 
For Sprint 1, the user will only recieve 1 outfit per asethtic, but for later Sprints, multiple options will be offered to the user."""

import time

def sleep_time(seconds_wanted):
    leaving_time_btw_lines = time.sleep(seconds_wanted)
    return leaving_time_btw_lines

print("-" * 150)          #Source- Samantha Walsh, helped me include a string operator of multiplication into my program. Which is used to multiply a string to another data type, in this example, it's being multiplied to an integer.                                                                                                
print("Hi there! Welcome to the world of fashion, today I'll be your guide as you discover new styles. Let's get started!")
sleep_time(1)
print("First, tell us a little bit about yourself!")
print("Read the following statements, and then choose the one which best defines you.")
first_choice = "[a] I usually wear minimalistic clothing."
second_choice = "[b] I wear sneakers with almost all my outfits."
third_choice = "[c] I love dressing like I'm going to a picnic everyday."
fourth_choice = "[d] I may not be from old money, but I sure do love dressing as if I was."
fifth_choice = "[e] I love bold outfits that give main character energy."
options_def_user = [first_choice, second_choice, third_choice, fourth_choice, fifth_choice]
for x in options_def_user:
    sleep_time(1)
    print(x)
still_looping = True
while(still_looping):
    users_choice = input("Type in your choice.")
    if users_choice == "a":
        print("Based on your answer, I'd recommend you look into the Model Off Duty aesthetic.")
        still_looping = False
    elif users_choice == "b":
        print("Based on your answer, I'd recommend you look into the Streetwear aesthetic.")
        still_looping = False
    elif users_choice == "c":
        print("Based on your answer, I'd recommend you look into the Soft Girl aesthetic.")
        still_looping = False
    elif users_choice == "d":
        print("Based on your answer, I'd recommend you look into the Preppy aesthetic.")
        still_looping = False
    elif users_choice == "e":
        print("Based on your answer, I'd recommend you look into the Rocker Chic.")
        still_looping = False
    else:
        print("That was not an option, please try again.")
print("-" * 100)
sleep_time(1.5)
print("You now have the option to continue with the recommendation provided to you, or choose a different aesthetic from the ones listed below.")
options_for_aesthetics =["Preppy", "Soft Girl", "Rocker Chic", "Streetwear", "Model Off Duty"]
for x in options_for_aesthetics:                            #I learned about "for" loops from w3schools.com, section "Python For Loops." Here's the link https://www.w3schools.com/python/python_for_loops.asp  For loops iterate a given sequence, for ex., a list
    sleep_time(0.5)
    print(x)
#Will include a sleep function throughout the program, which I learned about at ProgramWiz.  https://www.programiz.com/python-programming/time/sleep
def preppy_fit():
    print("Excellent choice", "Here are some outfits inspirations to achieve this aesthetic!", sep="! ")  #sep=  alters the behavior of a comma
    sleep_time(1)
    print("Loafers, white socks, tennis skirt, white button up with a crewneck, and gold accessories.")
    sleep_time(1)
    print("Loafers, blazer, plaid skirt, white button up, and a pearl necklace.")

def soft_girl_fit():
    print("Excellent choice", "Here are some outfits inspirations to achieve this aesthetic!", sep="! ")
    sleep_time(1)
    print("Doc Martens, maxi skirt, baby tee, tote bag, and dainty jewelry.")
    sleep_time(1)
    print("White converse, colorful sundress, shoulder bag, and gold jewelry.")

def rocker_chic_fit():
    print("Excellent choice", "Here are some outfits inspirations to achieve this aesthetic!", sep="! ")
    sleep_time(1)
    print("Black boots, black mini skirt, baby tee, sunglasses, shoulder bag, and silver jewelry.")
    sleep_time(1)
    print("Platform heels, black tennis skirt, dark-colored crewneck, white button-up, and a shoulder bag.")

def streetwear_fit():
    print("Excellent choice", "Here are some outfits inspirations to achieve this aesthetic!", sep="! ")
    sleep_time(1)
    print("Nike Dunks, denim shorts, neutral crop top, trucker hat, and a tote bag.")
    sleep_time(1)
    print("Jordan 1s, oversized t-shirt, mom jeans, shoulder bag, and gold jewelry.")

def model_off_duty_fit():
    print("Excellent choice", "Here are some outfits inspirations to achieve this aesthetic!", sep="! ")
    sleep_time(1)
    print("New balance, parachute pants, cropped white tank top, cross-body bag, sunglasses, and silver jewelry.")
    sleep_time(1)
    print("White sneakers, black mom jeans, neutral long sleeve, shoulder bag, and a claw-clip.")

keep_looping = True
while (keep_looping):
    aesthetic_chosen_by_user = input("Please type in your choice, exactly as it is written above:")
    if aesthetic_chosen_by_user == "Preppy":             # Samantha Walsh advised that I place quotation marks around each of the aesthetics, because I kept getting an error since they weren't defined
        preppy_fit()
        keep_looping = False
    elif aesthetic_chosen_by_user == "Soft Girl":
        soft_girl_fit()
        keep_looping = False
    elif aesthetic_chosen_by_user == "Rocker Chic":
        rocker_chic_fit()
        keep_looping = False
    elif aesthetic_chosen_by_user == "Streetwear":
        streetwear_fit()
        keep_looping = False
    elif aesthetic_chosen_by_user == "Model Off Duty":
        model_off_duty_fit()
        keep_looping = False
    else:
        sleep_time(1)
        print("Option not valid, try again.")
#add a trailing else: all other cases   and include a print statement in case the user inputs something other than the choices you provided, helps find errors

"""According to w3schools, section "Python If...Else", if the first condition in the "if" statement was not met, we can use "elif" to add another condition that can be attempted after the first one.
"Elif" also includes a print statement as shown above. Which what I did, however, I repeated it 4 times in order to account for all 5 choices of aesthetics the user could input. Link- https://www.w3schools.com/python/python_conditions.asp"""
print("-" * 150)        #Source- Samantha Walsh
next_step = "Now that you've chosen an outfit,"
con_next_step = "let's talk budget"
both_steps = next_step + " " + con_next_step + " "
print(both_steps, end=".")   #why does this line go with the one below it, come back to this
print("In order to recommend stores in which you can find your outfits, it's helpful to know your budget.")
users_budget = float(input("Enter the maximum amount you'd pay for a complete outfit, including accessories:"))
if (users_budget > 50.00) and (users_budget <= 100.00):
    print("Budget falls within an affordable price range.")
    sleep_time(1)
    print("Stores you can shop at include: Forever 21, JcPenny, and TJMaxx")
elif (users_budget > 100.00) and (users_budget <= 250.00):
    print("Budget falls within a reasonable price range.")
    sleep_time(1)
    print("Stores you can shop at include: Zara, Dillards, and Aritzia")
elif not(users_budget < 250):
    print("Budget falls within a high-end price range.")
    sleep_time(1)
    print("Stores you can shop at include: Neiman Marcus, Saks 5th Avenue, Nordstrom")

print("Once you've got a store in mind, here's what the average outfit within a specific aesthetic can cost.")
#Samantha Walsh helped give me the idea to include costs of the outfits
preppy_shoes = 65
preppy_top = 35
preppy_sweater = 35
preppy_jewelry = 20
preppy_fit_bf_tax = preppy_shoes + preppy_top + preppy_sweater + preppy_jewelry   #I am using an addition operator, to add up the cost of a preppy outfit, this is working due to all the values being integers
preppy_tax = preppy_fit_bf_tax * .06      #Here I'm using the multiplication operator to find the sales tax of the entire preppy outfit. Something I'll be repeating for each outfit.
total_cost_of_preppy_outfit = preppy_tax + preppy_fit_bf_tax
print("Cost of Preppy outfit: $", format(total_cost_of_preppy_outfit, ".2f"))
skirt_cost_sg = 30           #sg = soft girl
baby_tee_cost_sg = 15
cost_of_doc_martens_sg = 150
cost_of_tote_bag_sg = 30
cost_sg_fit_before_tax = skirt_cost_sg + baby_tee_cost_sg + cost_of_doc_martens_sg + cost_of_tote_bag_sg            #once again, I'm using addition operator to add up cost of Soft Girl outfit before tax
sg_tax = cost_sg_fit_before_tax * 0.06             #6% for florida taxes, is used for calculating the total price of all the different aesthetics outfits.
total_cost_of_sg_outfit = sg_tax + cost_sg_fit_before_tax
print("Cost of Soft Girl outfit: $", format(total_cost_of_sg_outfit, ".2f"))
cost_mini_skirt_rg = 25                     #rg= Rocker Chic
baby_tee_rg = 15
cost_jacket_rg = 80
cost_boots_rg = 110
cost_sunglasses_rg = 10
cost_shoulder_bag_rg = 25
cost_rg_outfit_bf_tax = cost_mini_skirt_rg + cost_jacket_rg + cost_boots_rg + cost_shoulder_bag_rg + cost_sunglasses_rg
rg_tax = cost_rg_outfit_bf_tax * 0.06
total_cost_of_rg_outfit = cost_rg_outfit_bf_tax + rg_tax
print("Cost of Rocker Chic outfit: $", format(total_cost_of_rg_outfit, ".2f"))
cost_sneakers_stwr = 90              #stwr = Streetwear
cost_shorts_stwr = 35
cost_top_stwr = 10
cost_hat_stwr = 35
cost_bag_stwr = 30
cost_stwr_fit_bf_tax = cost_sneakers_stwr + cost_shorts_stwr + cost_top_stwr + cost_hat_stwr + cost_bag_stwr
stwr_tax = cost_stwr_fit_bf_tax * 0.06
total_cost_of_stwr_outfit = cost_stwr_fit_bf_tax + stwr_tax
print("Cost of Streetwear outfit: $", format(total_cost_of_stwr_outfit, ".2f"))
cost_of_parachute_pants_mod = 45                            #mod= Model Off Duty
cost_of_white_tank_top_mod =  15
cost_of_black_sunglasses_mod =  10
cost_of_new_balances_mod =115
cost_of_entire_mod_outfit_before_taxes = cost_of_parachute_pants_mod + cost_of_white_tank_top_mod + cost_of_black_sunglasses_mod + cost_of_new_balances_mod
mod_taxes = cost_of_entire_mod_outfit_before_taxes * 0.06
total_cost_of_mod_outfit = cost_of_entire_mod_outfit_before_taxes + mod_taxes      
print("Cost of Model Off Duty outfit:", format(total_cost_of_mod_outfit, ".2f"))
sleep_time(1.25)
print("Clearly, it requires some money to keep up with the expensive lifestyle of a fashionista.")
sleep_time(1.25)
print("Here are the aesthetics in order of least expensive to most expensive, from top to bottom.")
cost_of_outfits_from_low_to_high =["Preppy", "Model Off Duty", "Streetwear", "Soft Girl", "Rocker Chic"]                        #Once again, taking what I learned from w3schools, "Python For Loops," to list the outfits from least to most expensive. Link https://www.w3schools.com/python/python_for_loops.asp
for outfit_organizate in cost_of_outfits_from_low_to_high:
    print(outfit_organizate)
print("-" * 150)
print("However, because you're our favorite, we'll go ahead an give you a 20% discount on all the outfits!")
print("Here are your new prices. Just check out those deals!")
discount_rate_on_preppy_outfit = total_cost_of_preppy_outfit * 0.20             #using the multiplication operator to see how much is going to be taken off the total price
new_discounted_cost_of_preppy_outfit = total_cost_of_preppy_outfit - discount_rate_on_preppy_outfit
print("New discounted price of Preppy Outfit: $", new_discounted_cost_of_preppy_outfit)
discount_rate_on_sg = total_cost_of_sg_outfit * 0.20                     
new_discounted_cost_of_sg_outfit = total_cost_of_sg_outfit - discount_rate_on_sg                  #Here I am using the subtraction operator to subtract the previous total cost of the soft girl outfit from the newly discount rate, to get a new price. 
print("New discounted price of Soft Girl Outfit: $", new_discounted_cost_of_sg_outfit)
discount_rate_on_rg_outfit = total_cost_of_rg_outfit * 0.20
new_discounted_cost_of_rg_outfit = total_cost_of_rg_outfit - discount_rate_on_rg_outfit
print("New discounted price of Rocker Chic Outfit: $", new_discounted_cost_of_rg_outfit)
discount_rate_on_stwr = total_cost_of_stwr_outfit * 0.20
new_discounted_cost_of_stwr = total_cost_of_stwr_outfit - discount_rate_on_stwr
print("New discounted price of Streetwear Outfit: $", new_discounted_cost_of_stwr)
discount_rate_on_mod = total_cost_of_mod_outfit * 0.20 
new_discounted_cost_of_mod = total_cost_of_mod_outfit - discount_rate_on_mod 
print("New discounted price of Model Off Duty Outfit: $", new_discounted_cost_of_mod)
print("-" *150)
print("You've reached the end.")
print("I hope you discovered some new aesthetics to try!")
print("-" * 50)

#As of this moment, I wasn't able to use all 7 of the numeric operators in my program. However, I did use the +,-, and *. So below I'll be demonstronstrating how to use the other 4 numeric operators I didn't get a chance to include.
#Andrew Krupp and Samantha Walsh described how I should present the operators that didn't make it into my program. So as to adhere to the requirements of Sprint 1.

math_example1 = 2+3**4              #The ** operator is used to raise an integer to the power of something, also known as an exponent.
continuation_math_example1 = 10          
print(math_example1/continuation_math_example1)        #The  / operator represents division, commonly used in arithmetic problems.

print(20 % 6)     #The modulus operator tells us what's left over or the remainder left from dividing the two numbers. I remember going over these operators in class, that's where I got this information from.
print(11 // 3)    #The // tells us how many times a number can go into the number it is being divided completely.
counter_example = 5
if counter_example > 0:                               #using a short-hand operator, don't know if only supposed to use 1 or multiple
    print("Yay, almost done!")
    counter_example += 1

num1 = 2
num2 = 10
print(num1 != num2 or num1 > num2)

for x in range(3,10):
    print(x)