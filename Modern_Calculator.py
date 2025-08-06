# A modern look into calculating everything important

print("Welcome to the Modern Calculator\n")
print("Please Choose the desired option from below: \n")
# Calculation of Maintainence Calorie, Arithmetics, Mental health level and Productivity level of the day

print("1- Maintainence Calorie Calculator\n", "2- Arithemetic Calculations\n", "3- Mental Health Condition\n", "4- Level of Productivity\n")
choice_1 = int(input(""))
if choice_1 == 1:
    print("OK, Let's Calculate your Maintainence Calorie\n")
    print("So Firstly, Please enter your weight(in kg), height(in cm), age(in years)respectively below:\n")
    weight = float(input(""))
    height = float(input(""))
    age = int(input(""))
    print("Choose from the activity levels given below: \n")
    print("S- Sedentary lifestyle(no physical activity, just desk job\n", "L- Lightly Active(light physical activity like- Walking, with limited exercise)\n", "M- Moderately Active(involving regular exercise or physical labor)\n", "V- Very Active(intense physical activities, as of athlete or construction worker)\n", "SA- Super Active(highly strenuous activities or rigorous training)\n", "P- Professional Athlete(play sports professionally)\n")
    choice_2 = input("")
    if choice_2 == "S":
        PAL = 1.2
    elif choice_2 == "L":
        PAL = 1.375
    elif choice_2 == "M":
        PAL = 1.55
    elif choice_2 == "V":
        PAL = 1.725
    elif choice_2 == "SA":
        PAL = 1.9
    elif choice_2 == "P":
        PAL = 3.4
    else:
        print("Please Choose from the options provided above")
    
    print("Please type 'm' if you're a Man, and 'f' if you're a Woman below:\n")
    choice_3 = input("")
    if choice_3 == "m":
        BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif choice_3 == "f":
        BMR = (10 * weight) + (6.25 * height) - (5 * age) - 161
    else:
        print("Please choose between the options provided above")
    
    # Now finally Calculating the Maintainence Calories:
    if choice_2 == "S" and choice_3 == "m":
        Maintain_calorie = BMR * PAL
        print(f"Your Maintainence Calorie is: {Maintain_calorie}kcal/day")
    elif choice_2 == "S" and choice_3 == "f":
        Maintain_calorie = BMR * PAL
        print(f"Your Maintainence Calorie is: {Maintain_calorie}kcal/day")
    elif choice_2 == "L" and choice_3 == "m":
        Maintain_calorie = BMR * PAL
        print(f"Your Maintainence Calorie is: {Maintain_calorie}kcal/day")
    elif choice_2 == "L" and choice_3 == "f":
        Maintain_calorie = BMR * PAL
        print(f"Your Maintainence calorie is: {Maintain_calorie}kcal/day")
    elif choice_2 == "M" and choice_3 == "m":
        Maintain_calorie = BMR * PAL
        print(f"Your Maintainence calorie is: {Maintain_calorie}kcal/day")
    elif choice_2 == "M" and choice_3 == "f":
        Maintain_calorie = BMR * PAL
        print(f"Your Maintainence calorie is: {Maintain_calorie}kcal/day")
    elif choice_2 == "V" and choice_3 == "m":
        Maintain_calorie = BMR * PAL
        print(f"Your Maintainence Calorie is: {Maintain_calorie}kcal/day")
    elif choice_2 == "V" and choice_3 == "f":
        Maintain_calorie = BMR * PAL
        print(f"Your Maintainence Calorie is: {Maintain_calorie}kcal/day")
    elif choice_2 == "SA" and choice_3 == "m":
        Maintain_calorie = BMR * PAL
        print(f"Your Maintainence Calorie is: {Maintain_calorie}kcal/day")
    elif choice_2 == "SA" and choice_3 == "f":
        Maintain_calorie = BMR * PAL
        print(f"Your Maintainence Calorie is: {Maintain_calorie}kcal/day")
    elif choice_2 == "P" and choice_3 == "m":
        Maintain_calorie = BMR * PAL
        print(f"Your Maintainence Calorie is: {Maintain_calorie}kcal/day")
    elif choice_2 == "P" and choice_3 == "f":
        Maintain_calorie = BMR * PAL
        print(f"Your Maintainence Calorie is: {Maintain_calorie}kcal/day")
    else:
        print("You have done something wrong in choosing the options before, please restart the machine")   


if choice_1 == 2:
    print("OK, Let's do Arithmetic Calculations\n")
    print("So Firstly, Choose the operation you wanna perform from the options below: \n")
    print("1- Addition", "2- Subtraction", "3- Multiplication", "4- Division", "5- Percentage","6- power", "7- Floor Division", "8- Remove the last digit")
    choice_4 = int(input(""))
    print("Enter the 1st and 2nd number you want operation between respectively: \n")
    n1 = float(input(""))
    n2 = float(input(""))
    if choice_4 == 1:
        print(f"The sum of n1 and n2 is: {n1 + n2}")
    elif choice_4 == 2:
        print(f"The difference between n1 and n2 is: {n1 - n2}")
    elif choice_4 == 3:
        print(f"The product of n1 and n2 is: {n1 * n2}")
    elif choice_4 == 4:
        print(f"The quotient after dividing n1 by n2 is: {n1 / n2}")
    elif choice_4 == 5:
        print(f"{n1} % of {n2} is: {(n1 * n2) / 100}")
    elif choice_4 == 6:
        print(f"{n1} to the power {n2} is: {n1 ** n2}")
    elif choice_4 == 7:
        print(f"The floor division of {n1} by {n2} is: {n1 // n2}")
    elif choice_4 == 8:
        print(f"The new number after removing the last digit from {n1} is: {n1 // 10}")
        
if choice_1 == 3:
    print("OK, Let's Observe your Mental Health Condition\n")
    print("You will receive points total out of 10, and an important tip for a healthy mental\n")
    print("Question-1: Are you able to respond to stressful events or situations calmly while maintaining a positive outlook?", "Respond to the question as 'Y' for yes and 'N' for no")
    choice_5 = input("")
    if choice_5 == "Y":
        point_1 = 1
    elif choice_5 == "N":
        point_1 = 0   
    else:
        print("Please Choose between 'Y and 'N' ")
    imp_tip_1 = "Practicing mindfulness by acknowledging your emotions without judgment is a good way of gradually building emotional resilience. By practicing mindfulness regularly, you learn to recognize and manage even negative emotions effectively, preparing you for difficult situations that might cause feelings such as sadness, anger, or disappointment."
    
    print("Question-2: Are you able to obeserve your thoughts, emotions, and physical sensations from a distance which helps you to recognize how they influence your behavior and feelings?", "Respond to the question as 'Y' for yes and 'N' for no")
    choice_6 = input("")
    if choice_6 == "Y":
        point_2 = 1
    elif choice_6 == "N":
        point_2 = 0
    else:
        print("Please choose between 'Y' or 'N' ")
    imp_tip_2 = "Journaling is an effective method of practicing self-awareness. Writing down memorable events at the end of each day or asking questions such as “What were my dominant emotions today?” helps you recognize what motivates your feelings and behaviors and helps you change what is undesirable."
     
    print("Question-3: Do you have positive relationship(consisting of empathy and communication) with your closed ones or even with most of the people around you?", "Respond with 'Y' for yes and 'N' for no")
    choice_7 = input("")
    if choice_7 == "Y":       
        point_3 = 1
    elif choice_7 == "N":
        point_3 = 0
    else:
        print("Please choose between 'Y' or 'N' ") 
    imp_tip_3 = "Positive relationships are crucial for mental health, offering support, love, and understanding. They are an integral part of the characteristics of a mentally healthy person since they strengthen emotional resilience, provide a sense of belonging, and contribute significantly to overall well-being and happiness. In any sort of relationship, communication and empathy are key. They do not only strengthen mutual understanding but also create an environment where both parties feel heard and valued, providing a space in which feelings and thoughts can be openly expressed."
    
    print("Question-4: Are you able to manage changes and challenges effectively, while being open to new experiences and being flexible in thought and action(not being easily stressed out)?", "Respond with 'Y' for yes and 'N' for no")
    choice_8 = input("")
    if choice_8 == "Y":
        point_4 = 1
    elif choice_8 == "N":
        point_4 = 0
    else:
        print("Please choose between 'Y' or 'N' ")
    imp_tip_4 = "Adaptability refers to the capability of managing changes and challenges effectively, being open to new experiences, and being flexible in thought and action. In this way, adaptability can mitigate stress and uncertainty, which are often caused by new challenges and situations. Enhancing adaptability involves embracing flexibility and consciously engaging in new activities or setting new challenges for yourself. This could involve starting a new hobby, learning a new skill, or setting goals that push you out of your comfort zone. The experiences you gather in this way can help you in the future when facing new situations and challenges." 
    
    print("Question-5: Do you practice Self- Compassion(i.e. Positive self talk and avoiding harsh criticism)", "Respond with 'Y' for yes and 'N' for no")
    choice_9 = input("")
    if choice_9 == "Y":
        point_5 = 1
    elif choice_9 == "N":
        point_5 = 0
    else:
        print("Please choose between 'Y' or 'N' ")
    imp_tip_5 = "Positive self-talk and avoiding harsh criticism are a vital part of developing self-compassion. Avoid focusing on your mistakes but rather remind yourself of your strengths and accomplishments. This will help you build a kinder internal dialogue, enhancing emotional resilience and building self-esteem."
        
    print("Question-6: Do you approach challenges with a positive attitude, acknowledging obstacles but not overestimating their significance but rather focusing on how they can be realistically solved?", "Respond with 'Y' for yes and 'N' for no")
    choice_10 = input("")
    if choice_10 == "Y":
        point_6 = 1
    elif choice_10 == "N":
        point_6 = 0
    else:
        print("Please choose between 'Y' or 'N' ")
    imp_tip_6 = "Practicing gratitude regularly reinforces an optimistic perspective on potential challenges. Instead of contemplating potential issues, practice the observation of what you can control and the steps you can take to address issues. This will also direct your energy towards productive outcomes."
        
    print("Question-7: Do you set Healthy Boundaries in both professional setting or personal relationship which is crucial for maintaining mental health(prevent burnouts) and building relationships that are built on mutual respect?", "Respond with 'Y' for yes and 'N' for no")
    choice_11 = input("")
    if choice_11 == "Y":
        point_7 = 1
    elif choice_11 == "N":
        point_7 = 0
    else:
        print("Please choose between 'Y' or 'N' ")
    imp_tip_7 = "For the development and maintenance of healthy boundaries, assertiveness is crucial. This skill allows you to communicate your needs and limits clearly and respectfully. Start practicing this by saying 'no' even to simple things that don not align with your wants or needs. This will help you build confidence and allow you to set clear boundaries even for more impactful aspects of your life."
        
    print("Question-8: Do you have a Sense of Purpose in life?", "Respond with 'Y' for yes and 'N' for no")
    choice_12 = input("")
    if choice_12 == "Y":
        point_8 = 1
    elif choice_12 == "N":
        point_8 = 0
    else:
        print("Please choose between 'Y' or 'N' ")
    imp_tip_8 = "Having a sense of purpose contributes significantly to overall well-being. Since this involves setting goals and finding meaning in life, it drives motivation, enhances resilience, and provides a sense of direction, making daily activities more fulfilling and aligned with personal values and long-term visions. Developing a sense of purpose requires you to reflect on your passions and core values. You need to identify what truly matters to you and think about how you can incorporate these elements into your everyday life. This also involves setting achievable goals that are related to your passions and taking small but deliberate steps toward fulfilling them."
        
    print("Question-9: Do you practice Breathing Exercises and Meditation?", "Respond with 'Y' for yes and 'N' for no")
    choice_13 = input("")
    if choice_13 == "Y":
        point_9 = 1
    elif choice_13 == "N":
        point_9 = 0
    else:
        print("Please choose between 'Y' or 'N' ")
    imp_tip_9 = "Breathing exercises and meditation can improve emotional regulation. These practices help manage strong emotions by calming the body. By practicing them, you learn to control your reactions and maintain stability even in stressful or challenging situations."
        
    print("Question-10: Do you participate in Regular Exercise with a proper healthy diet?", "Respond with 'Y' for yes and 'N' for no")
    choice_14 = input("")
    if choice_14 == "Y":
        point_10 = 1
    elif choice_14 == "N":
        point_10 = 0
    else:
        print("Please choose between 'Y' or 'N' ")
    imp_tip_10 = "Integrating regular exercise into your routine is key. This can range from light physical activity like walking to more intense workouts, depending on individual preferences. While aiming for 7-9 hours of sleep each night can significantly increase mental alertness and emotional stability, eating a diet high in fruits, vegetables, lean meats, and whole grains supports general health and mental clarity."
    
    print("So from your answers in above questions, we have formed a Report Card about your current Mental Health and along with it, we are providing an important tip which can improve your short comings and make you feel so much better about yourself")
    Total_points = point_1 + point_2 + point_3 + point_4 + point_5 + point_6 + point_7 + point_8 + point_9 + point_10
    if Total_points == 0:
        print(f"Total points scored by you is: {Total_points}\n")
        print("Don't worry a bit, here are some important tips which will help you overcome your weakness: \n")
        print(f"{imp_tip_1}")
        print("")
        print(f"{imp_tip_2}")
        print("")
        print(f"{imp_tip_3}")
        print("")
        print(f"{imp_tip_4}")
        print("")
        print(f"{imp_tip_5}")
        print("")
        print(f"{imp_tip_6}")
        print("")
        print(f"{imp_tip_7}")
        print("")
        print(f"{imp_tip_8}")
        print("")
        print(f"{imp_tip_9}")
        print("")
        print(f"{imp_tip_10}")
        print("")
        
    if Total_points == 1:
        print(f"Total points scored by you is: {Total_points}\n")
        print("Don't worry a bit, here is an important tip which will help you overcome your weakness: \n")
        print(f"{imp_tip_1}")
            
    if Total_points == 2:
        print(f"Total points scored by you is: {Total_points}\n")
        print("Don't worry a bit, here is an important tip which will help you overcome your weakness: \n")
        print(f"{imp_tip_2}")
            
    if Total_points == 3:
        print(f"Total points scored by you is: {Total_points}\n")
        print("Don't worry a bit, here is an important tip which will help you overcome your weakness: \n")
        print(f"{imp_tip_3}")
        
    if Total_points == 4:
        print(f"Total points scored by you is: {Total_points}\n")
        print("Don't worry a bit, here is an important tip which will help you overcome your weakness: \n")
        print(f"{imp_tip_4}")
        
    if Total_points == 5:
        print(f"Total points scored by you is: {Total_points}\n")
        print("Don't worry a bit, here is an important tip which will help you overcome your weakness: \n")
        print(f"{imp_tip_5}")
        
    if Total_points == 6:
        print(f"Total points scored by you is: {Total_points}\n")
        print("Here is an important tip which will help you overcome your weakness: \n")
        print(f"{imp_tip_6}")
        
    if Total_points == 7:
        print(f"Total points scored by you is: {Total_points}\n")
        print("Here is an important tip which will help you overcome your weakness: \n")
        print(f"{imp_tip_7}")
        
    if Total_points == 8:
        print(f"Total points scored by you is: {Total_points}\n")
        print("Here is an important tip which will help you overcome your weakness: \n")
        print(f"{imp_tip_8}")
        
    if Total_points == 9:
        print(f"Total points scored by you is: {Total_points}\n")
        print("Here is an important tip which will help you overcome your weakness: \n")
        print(f"{imp_tip_9}")
        
    if Total_points == 10:
        print(f"Total points scored by you is: {Total_points}\n")
        print("Here is an important tip which will help you overcome your weakness: \n")
        print(f"{imp_tip_10} ")
        
    print("Thanks for Checking up on your Mental Health with Us, See You next time better than ever, Champ!")

if choice_1 == 4:
    print("OK, Let's check up on your level of productivity\n")
    print("Please Answer the questions provided below, based on them we will prepare your report card with an additional tip to help you with your productivity, Respond with 'Y' for yes and 'N' for no\n")
    print("Question-1: Do you write down every task and commitment you have to complete today beforehand?")
    choice_15 = input("")
    if choice_15 == "Y":
        point_11 = 1
    elif choice_15 == "N":
        point_11 = 0
    else:
        print("Please choose between 'Y' and 'N' ")
    imp_tip_11 = "Every task, every commitment should be written down. This frees your mind from the energy- and attention-sucking job of trying to remember, the first step to managing your life and time is getting every commitment, large and small, out of your head and into a trusted system."
    
    print("Question-2: If you create a routine of a day, do you prepare it the night before?")
    choice_16 = input("")
    if choice_16 == "Y":
        point_12 = 1
    elif choice_16 == "N":
        point_12 = 0
    else:
        print("Please choose between 'Y' and 'N' ")
    imp_tip_12 = "The best way to hit the ground running is to start the night before. Before leaving your workspace, or before going to bed, take 10 minutes to look over the next day’s commitments. The busier your day, the more important it is to do this quick survey the day or evening before. It means you waste no time in the morning deciding where to start, or gathering materials (and maybe discovering a crucial item isn’t available when you need it)."
    
    print("Question-3: Do you hop on your most dreaded task as the first task of the day?")
    choice_17 = input("")
    if choice_17 == "Y":
        point_13 = 1
    elif choice_17 == "N":
        point_13 = 0
    else:
        print("Please choose between 'Y' and 'N' ")
    imp_tip_13 = "Whatever it is, it hangs over your head, distracting you with guilt because it keeps getting pushed to the next day and the next. It’s time to end that cycle. Do it first thing. Writer Michael Hyatt talks about slaying your dragons before breakfast—there’s nothing more motivating for the rest of your day than crossing that monster off your list first thing in the morning. Do something about that overwhelming task—maybe you can’t finish it in one day, but you can at least get started. Whatever it is, just do it."
    
    print("Question-4: Do you turn off all your distractions before getting into your task?")
    choice_18 = input("")
    if choice_18 == "Y":
        point_14 = 1
    elif choice_18 == "N":
        point_14 = 0
    else:
        print("Please choose between 'Y' and 'N' ")
    imp_tip_14 = "When you’ve got an important task that requires attention and focus, create the space to give it your best. Whether it’s a meeting with a client or colleague, or an important letter that needs to get written, or a piece of art you want to create, schedule a block of time to focus on that commitment, and then turn off all distractions. Shut down your phone (or at least turn off the ringer). Silence your email alerts. Disconnect the internet (or at least Facebook and Twitter). Close your office door. Just for that hour (or thirty minutes, or half day), turn off all outside communications and give yourself the necessary luxury of undisturbed time to really focus on the matter at hand."
    
    print("Question-5: Do you take regular breaks of atmost 10mins after every focus session lasting 25mins-2hrs?")
    choice_19 = input("")
    if choice_19 == "Y":
        point_15 = 1
    elif choice_19 == "N":
        point_15 = 0
    else:
        print("Please choose between 'Y' and 'N' ")
    imp_tip_15 = "There’s a limit to how long anybody can devote deep focus to a task. No matter how busy you are, after a certain amount of time, the law of diminishing returns kicks in, and fatigue—physical and/or mental—starts to impair your effectiveness. Schedule breaks periodically even during the busiest days. Take ten minutes to stand up, stretch, get a drink of water, walk around the block. You’ll return to your work refreshed, both mentally and physically, and ready to be even more productive."
    
    print("Question-6: Do you batch your similar tasks together(i.e., all theoretical subjects together separately to all the practicing subjects)?")
    choice_20 = input("")
    if choice_20 == "Y":
        point_16 = 1
    elif choice_20 == "N":
        point_16 = 0
    else:
        print("Please choose between 'Y' and 'N' ")
    imp_tip_16 = "If the demands of your day include routine tasks, try to group similar tasks and schedule certain times during the day to knock them out. By batching similar tasks, you save the time lost to ramping up multiple times a day and reap the benefits of momentum."
    
    print("Question-7: Do you eat a healthy breakfast?")
    choice_21 = input("")
    if choice_21 == "Y":
        point_17 = 1
    elif choice_21 == "N":
        point_17 = 0
    else:
        print("Please choose between 'Y' and 'N' ")
    imp_tip_17 = "Healthy people are more productive. No matter how busy you are, eat a decent breakfast. It’ll fuel you for a terrific start to your day."
    
    print("Question-8: Do you engage in regular exercise?")
    choice_22 = input("")
    if choice_22 == "Y":
        point_18 = 1
    elif choice_22 == "N":
        point_18 = 0
    else:
        print("Please choose between 'Y' and 'N' ")
    imp_tip_18 = "Exercise makes you healthier, so be sure to get some exercise every day. You don’t need to spend hours at the gym to get the benefit of this; take a walk around the block, or do some isometrics at your desk. Just do something to get your heart pumping and your blood racing. It will enhance your general well being as well as your ability to think more clearly."
    
    print("Question-9: Do you use any AI in your problem solving?")
    choice_23 = input("")
    if choice_23 == "Y":
        point_19 = 1
    elif choice_23 == "N":
        point_19 = 0
    else:
        print("Please choose between 'Y' and 'N' ")
    imp_tip_19 = "An important key to productivity is doing only those things that only you can do, and giving somebody else the opportunity to contribute by doing those other tasks. Or you can also use AI to get a check of the solution that you have gotten after solving a problem by yourself."
    
    print("Question-10: Have you made commitments or taken tasks that don't needed to be kept at all or don't actually matter to you at all?")
    choice_24 = input("")
    if choice_24 == "Y":
        point_20 = 1
    elif choice_24 == "N":
        point_20 = 0
    else:
        print("Please choose between 'Y' and 'N' ")
    imp_tip_20 = "When someone calls or appears at your door with a request for your participation in some activity, take a breath and consider whether it fits into your own priorities (which priorities, of course, might legitimately include keeping your boss or spouse happy). If the answer is no, then just say no. Practice it ahead of time: 'Thank you for inviting me, but no.' 'Thank you for asking, but no.' 'Thank you for thinking of me, but no.'"
        
    print("So from your answer to the above question we have created a report card which contains the total points you scored, and along with that we will provide you a/an important tip/s which will help you to be more productive")
    Total_points_2 = point_11 + point_12 + point_13 + point_14 + point_15 + point_16 + point_17 + point_18 + point_19 + point_20
    if Total_points_2 == 0:
        print(f"Total points scored by you is: {Total_points_2}\n")
        print("Don't feel down, Here are some most important tips which will help you be more productive: \n")
        print(f"{imp_tip_11}")
        print("")
        print(f"{imp_tip_12}")
        print("")
        print(f"{imp_tip_13}")
        print("")
        print(f"{imp_tip_14}")
        print("")
        print(f"{imp_tip_15}")
        print("")
        print(f"{imp_tip_16}")
        print("")
        print(f"{imp_tip_17}")
        print("")
        print(f"{imp_tip_18}")
        print("")
        print(f"{imp_tip_19}")
        print("")
        print(f"{imp_tip_20}")
        print("")
        
    if Total_points_2 == 1:
        print(f"Total points scored by you is: {Total_points_2}")
        print("Don't feel down, Here is an important tip to boost your productivity: \n")
        print(f"{imp_tip_11}")
        
    if Total_points_2 == 2:
        print(f"Total points scored by you is: {Total_points_2}")
        print("Don't feel down, Here is an important tip to be more productive: \n")
        print(f"{imp_tip_12}")
      
    if Total_points_2 == 3:
        print(f"Total points scored by you is: {Total_points_2}")
        print("Don't feel down, Here is an important tip which will help you be more productive: \n")
        print(f"{imp_tip_13}")
    
    if Total_points_2 == 4:
        print(f"Total pints scored by you is: {Total_points_2}")
        print("Don't feel down, Here is an important tip to boost your productivity: \n")
        print(f"{imp_tip_14}")
        
    if Total_points_2 == 5:
        print(f"Total points scored by you is: {Total_points_2}")
        print("Don't feel down, Here is an important tip to be more productive: \n")
        print(f"{imp_tip_15}")
        
    if Total_points_2 == 6:
        print(f"Total points scored by you is: {Total_points_2}")
        print("Here is an important tip which will help you be more productive: \n")
        print(f"{imp_tip_16}")
        
    if Total_points_2 == 7:
        print(f"Total points scored by you is: {Total_points_2}")
        print("Here is an important tip to boost your productivity: \n")
        print(f"{imp_tip_17}")
        
    if Total_points_2 == 8:
        print(f"Total points scored by you is: {Total_points_2}")
        print("Here is an important tip to be more productive: \n")
        print(f"{imp_tip_18}")
        
    if Total_points_2 == 9:
        print(f"Total points scored by you is: {Total_points_2}")
        print("Here is an important tip which will help you be more productive: \n")
        print(f"{imp_tip_19}")
        
    if Total_points_2 == 10:
        print(f"Total points scored by you is: {Total_points_2}")
        print("Here is an important tip to boost your productivity: \n")
        print(f"{imp_tip_20}")  