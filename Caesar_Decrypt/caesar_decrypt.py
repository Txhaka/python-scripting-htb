import pdb
"Amo la traición, pero odio al traidor." #Julius Caesar quote -> Caesar encrypt
"PWNER{F4k3_P0wn3rs_fl4G}" #Flag format I guess

dictionary = {
    'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7,
    'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14,
    'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21,
    'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26, 'A' : 27, 'B' : 28, 
    'C' : 29, 'D' : 30, 'E' : 31, 'F' : 32, 'G' : 33, 'H' : 34, 'I' : 35, 
    'J' : 36, 'K' : 37, 'L' : 38, 'M' : 39, 'N' : 40, 'O' : 41, 'P' : 42, 
    'Q' : 43, 'R' : 44, 'S' : 45, 'T' : 46, 'U' : 47, 'V' : 48, 'W' : 49, 
    'X' : 50, 'Y' : 51, 'Z' : 52, '0' : 53, '1' : 54, '2' : 55, '3' : 56, 
    '4' : 57, '5' : 58, '6' : 59, '7' : 60, '8' : 61, '9' : 62, '{' : 63, 
    '}' : 64, '_' : 65
}
#Alphabet lower_case_letters + upper_case_letters + digits + brackets + '_'
#First guess -> every letter is shifted the same number as its postion
#Second guess -> shift number is a random number not revealed



flag_to_decrypt = 'JQHyL4vVXh6pXHVxU6Yf6AlOjU6Nrb7e75'



def shift(flag_to_decrypt, shift_number):
    flag = ''
    keys_list = list(dictionary.keys())
    values_list = list(dictionary.values())
    for letter in flag_to_decrypt:
        position = int(dictionary[letter])
        value_to_shift = shift_number 
        new_value =((value_to_shift + position) % 65) + 1
        new_letter = dictionary_to_list(keys_list,values_list,new_value)
        flag += new_letter

        if len(flag) == 34:
            return flag


def dictionary_to_list(keys_list,values_list,index):
    position = values_list.index(index)
    return (keys_list[position])

def random_number():
    for i in range(1,66):
        possible_flag = shift(flag_to_decrypt, i)
        print(possible_flag)


if __name__== '__main__':

     random_number()
