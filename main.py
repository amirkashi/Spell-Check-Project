import spell_check


if __name__ == '__main__':
    checking_spells = spell_check.Spell_Check()
    print ("To exit program please enter pleae type Exit!")
    while 1:
        input_sentence = raw_input("Please enter a sentence: ")
        if input_sentence == "Exit!":
            break
        checking_spells.get_user_sentence(input_sentence)
