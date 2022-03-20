import easygui

path = easygui.fileopenbox("Open word book.", "alert")
wordbook = open(path, "r+", encoding='UTF-8')
word = wordbook.read()
word_all_list = list(word.split("\n"))
cleaning_word_all_list = []
num = 0
for i in word_all_list:
    if i == "":
        pass
    else:
        cleaning_word_all_list.append(word_all_list[num])
    num += 1
review_number = int(input("Please input the number of the word that you want to review:"))
nnn = 0
for j in range(0, review_number*2, 2):
    nnn += 1
    word_input = easygui.enterbox(cleaning_word_all_list[j+1], str(nnn))
    min_word = list(cleaning_word_all_list[j].split(" "))
    if word_input == min_word[1]:
        pass
    elif word_input == None:
        break
    else:
        easygui.msgbox("Wrong! "+cleaning_word_all_list[j], "Alert")
easygui.msgbox("See you!", "See you!")