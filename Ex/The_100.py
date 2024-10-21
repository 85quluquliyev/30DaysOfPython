import random
import time

# The 100 - A game of survival using Azerbaijani names
azerbaijani_names = [
    "Elshan", "Aysel", "Ramil", "Leyla", "Rauf", "Nigar", "Elvin", "Sevinj", "Kamran", "Rufat",
    "Gulnar", "Tural", "Rena", "Emin", "Gulnaz", "Fakhri", "Zafar", "Atie", "Shebnem", "Sadiq",
    "Javid", "Nijat", "Ramila", "Ayla", "Faride", "Zahid", "Roya", "Bakhtiyar", "Cennat", "Asif",
    "Cavidan", "Leman", "Guloglan", "Faride", "Ruya", "Kenan", "Fazil", "Rufat", "Maya", "Senan",
    "Yusif", "Aysu", "Ruslan", "Rena", "Vugar", "Xaliq", "Siqura", "Sona", "Ramil", "Nermin",
    "Orkhan", "Aydin", "Cahangir", "Khadija", "Ilkin", "Tamerlan", "Shahin", "Fidan", "Refiq", "Elnar",
    "Gunay", "Aslan", "Ramina", "Gulnara", "Jamal", "Vaqif", "Alim", "Ismayil", "Rauf", "Rahil",
    "Faiq", "Naila", "Shamil", "Rufat", "Rena", "Alekber", "Samir", "Ruqeyya", "Cahan", "Mahir",
    "Eldaniz", "Aldi", "Parvana", "Huseyn", "Elvin", "Turgay", "Rashid", "Inci", "Tahir", "Sherafet",
    "Khatira", "Musa", "Samad", "Sedaqat", "Hacer", "Zamiq", "Qulu", "Said", "Samira", "Emil",
]

game_duration = 100
start_time = time.time()
died_count = 0
total_people = len(azerbaijani_names)

while time.time() - start_time < game_duration and azerbaijani_names:
    selected_name = random.choice(azerbaijani_names)
    azerbaijani_names.remove(selected_name)
    died_count += 1

    # Calculate the remaining count
    remaining_count = total_people - died_count

    # Print the name of the person who died with the remaining count
    print(f"Selected person: {selected_name} (died) 💔 {remaining_count} remaining")
    
    # Special messages at specific counts
    if died_count == 50:
        print("50 people have died. The game continues... 🔥")
    elif died_count == 81:
        print("Last 20 people remaining... ⚠️")
    elif died_count == 91:
        print("Last 10 people remaining... ⚠️")
    elif died_count == 96:
        print("Last 5 people remaining... ⚠️")

    random.shuffle(azerbaijani_names)
    time.sleep(1)

if azerbaijani_names:
    winner = random.choice(azerbaijani_names)
    print(f"🎉 Congratulations! The last survivor is: {winner} 🎊")
else:
    print("No one survived.")

print("The game has ended.")
