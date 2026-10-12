def calculate_love_score(name1, name2):
    combined_names = name1 + " " + name2
    print(f"The names of the future couple: {combined_names}")

    true_letters = "true"
    total_true = 0
    for char in true_letters:
        if combined_names.lower().count(char):
            total_true +=combined_names.lower().count(char)

    # print(f"Total true is:{total_true}")

    love_letters = "love"
    total_love = 0
    for char_l in love_letters:
        if combined_names.lower().count(char_l):
            total_love += combined_names.lower().count(char_l)

    score = str(total_true) + str(total_love)

    print(score)
    # print(f"Total love is: {total_love}")
calculate_love_score("Jules", "Honorine")