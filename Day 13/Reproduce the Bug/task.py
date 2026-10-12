from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
nb_items = len(dice_images)
print(nb_items)
dice_num = randint(1,nb_items-1)
print(dice_images[dice_num])
