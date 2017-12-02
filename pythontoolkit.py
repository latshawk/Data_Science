#FUNCTIONS, DEFAULT ARGS, VARIABLE ARGS, LAMBDA FUNCTIONS
""" writing functions"""

#writing a simple function

def shout():
    '''prints a string with 3 exclamation points'''
    #concatct strings and set to variable 'shout_word'
    shout_word = 'King of the mountain' + '!!!'
    print(shout_word)

shout()

#single parameter function

def shout(word):
    ''' Prints a string with 3 exclamation points to the argument 'word' '''
    shout_argument= word + '!!!'
    print(shout_argument)

shout('grandpapa')

#functions that return a single value

def shout(string):
    ''' concats the variable shout_string to 3 !!! assigned to a new variable: yell '''
    shout_string = string + '!!!'
    return shout_string

yell = shout('YAHOOOO')

print(yell)

#functions with multiple parameters

def shout(string1, string2):
    ''' concat 3 !!! to multiple strings '''
    arg1 = string1 + '!!!'
    arg2 = string2 + '!!!'
    arg_out = arg1 + arg2

    return arg_out

saying = shout('Bohemian', 'Rapsohdy')
print(saying)

#intro to tuples
nums = (3,4,6)
    #unpack nums
num1, num2, num3 = nums
    #replace 1st values with number 2: even_nums
even_nums = (2, num2, num3)
print(even_nums)

#Function that returns multiple values

def shout_many(speak1, speak2):
    ''' returns multiple values independently '''
    speaking1 = speak1 + '!!!'
    speaking2 = speak2 + '!!!'

    #create a tuple
    combine_speak = (speaking1, speaking2)
    return combine_speak

#passing tuple args into variables
yelling1, yelling2 = shout_many('Little High', 'Little Low')

print(yelling1)
print(yelling2)

#case example for functions and tuples
import pandas as pd

df = pd.read_csv('D:/hawk/fakepath/tweets.csv')

#initialize a new dictionary
lang_count = {}

#extract column from df: col
col = df['lang']

#iterate over the lang column in df
for entry in col:
    #if the language is in lang_count dictionary then add 1
    if entry in lang_count.keys():
        lang_count[entry] += 1
    else:
        lang_count[entry] = 1
#print new dictionary
print(lang_count)

#create a function that returns the dictionary with arguments called
def count_entries(df, col_name):
    ''' returns a dictionary with counts of occurances as values for each day'''
    langs_count={}          #adds a (s) to the dict
    column = df[col_name]

    #iterate over the lang column in df and add to dict
    for entry in col:
        # if the language is in lang_count dictionary then add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        else:
            langs_count[entry] = 1
    return langs_count

result = count_entries(df, 'lang')

print(result)

'''------------------------------------------------------------------------------------'''
#2. default arguments and variable lengths

#keyword global
#create a string
team = 'a squad'

def change_team():
    ''' change the value of the global variable called team'''
    global team

    team= 'detroit red wings'
print(team)     #still prints 'a squad'

#call function to change the team name
change_team()
print(team)     #changes team name to 'detroit red wings'

#nested functions
#define function that attaches 3!!! to three different arguments
def three_shouts(w1, w2, w3):
    ''' returns a tuple that concats 3 !!! to each'''
    def inner(words):
        ''' returns a single string concated with !!! '''
        return words + '!!!'

    return (inner(w1), inner(w2), inner(w3))
print(three_shouts('alpha', 'beta', 'delta'))

#nested functions part 2
def echo(n):
    ''' returns the inner_echo function'''
    def inner_echo(word1):
        ''' concats 'n' copies of word1'''
        echo_word = word1 * n
        return echo_word

    return inner_echo

#call echo 2 times: twice
twice = echo(2)

#call echo 3 times: thrice
thrice = echo(3)

#call & print twice| thrice with arguments
print(twice('whoo'), thrice('hooo'))


#keyword nonlocal and nested functions
def echo_shout(n):
    ''' change value 'n' which is a nonlocal variable'''
    echo_state= n*2
    print(echo_state)

    #define inner function called shout
    def shout():
        ''' alter a variable in the enclosing scope'''
        #use echo_state in nonlocal scope
        nonlocal echo_state

        echo_state = echo_state + '!!!'

    #call shout function
    shout()
    print(echo_state)

echo_shout('hello')


#functions with one default argument
    #default argument is mult set to 1
def myword(new_word, mult = 1):
    ''' concat mult copies of argument 'new_word' and 3 !!! at the end'''
    mult_word = new_word * mult

    #concat 3 !!! to the end of mult_word
    yell_word = mult_word + '!!!'

    return yell_word

#call myword() with default mult
default_mult = myword('Hey')

#call myword() with 5x multipler
five_mult = myword('Hey', mult= 5)

print(default_mult)
print(five_mult)


#functions with multiple default arguments
    #default arguments are a multiple set to 1, a boolean that capitalizes if true
def statement(string, multiplier = 1, capitalize= True):
    ''' takes a string with default of 1x and capitalizes if set to true, attaches 3 !!! to the end '''
    multipy_word = string * multiplier

    #capitalizes if 'capitalize set to true'
    if capitalize is True:
        multiply_new_word = multipy_word.upper() + '!!!'
    else:
        multiply_new_word = multipy_word + '!!!'

    return multiply_new_word

#call statement with string='Booyah', multiplier= 5, capitalize= True
capital_statement = statement('Booyah', multiplier= 5, capitalize= True)

#call statement with no capitalization
lower_statement = statement('Booyah', capitalize= False)

print(capital_statement)
print(lower_statement)


#function with variable length arguments (*args)
def gibberish(*args):
    ''' concat strings in *args together'''
    hodgepoge = ""

    for word in args:
        hodgepoge += word

    return hodgepoge

#call gibberish with one string 'luke'
one_word= gibberish('luke')

#call gibberish with many strings 'luke', 'vader', 'obi', 'solo'
many_words = gibberish('luke ', 'vader ', 'obi ', 'solo')

print(one_word)
print(many_words)



#functions with variable length keyword args(**kwargs)
def report_status(**kwargs):
    ''' print out status of a movie character'''
    print('\n BEGIN: REPORT\n')

    #iterate over key-value pairs of kwargs
    for key, value in kwargs.items():
        #print out keys & values, seperated by colon :
        print(key + ': ' + value)

    print('\n END REPORT')

#call report_status with 3 keys and values
report_status(name ="luke skywalker", title='jedi', status='missing')

#call report status with 3 different key values
report_status(name= 'vader', title='sith lord', status='deceased')


#case example for section 2
#import pandas
#df = pd.read_csv('D:/hawk/datacamp/tweets.csv')
def count_entries(df, col_name= 'lang'):
    ''' return a dictionary with counts as values for each key'''

    #create empty dict
    cols_count = {}

    #extract column from dataframe, named col
    col= df[col_name]

    #iterate over column
    for entry in col:
        if entry in cols_count.keys():
            cols_count[entry] += 1
        else:
            cols_count[entry] = 1
    return cols_count

#call results to dictionary
result1= count_entries(df, col_name='lang')
result2= count_entries(df, col_name= 'source')

print(result1)
print(result2)

#cols_count with *args
def counting_entries(df, *args):
    ''' returns dictionary with counts from numerous arguments'''

    coll_count= {}

    for col_name in args:
        coll= df[col_name]

        for entry in coll:
            if entry in coll_count.keys():
                coll_count[entry] += 1
            else:
                coll_count[entry] = 1
        return coll_count

resulta= counting_entries(df, 'lang')
resultb = counting_entries(df, 'lang', 'source')

print(resulta)
print(resultb)




#4. lamda functions and error handling

#writnig a lambda function
#used to replace line functions
e_word = (lambda wrd, repeat: wrd * repeat)
result = e_word('questions', 5)
print(result)

#lambda function using map
elements = ['fire', 'water', 'wind', 'earth']

shout_elements = map(lambda item: item + "!!!", elements)

shout_elements_list = list(shout_elements)
print(shout_elements_list)

#lambda function using filter
justice_league = ['batman', 'aquaman', 'wonderwoman', 'flash', 'bionicman']
jl_result = filter(lambda member: len(member) > 6, justice_league)

jl_result_list = list(jl_result)
print(jl_result_list)


#lambda function with reduce()
from functools import reduce

hockey = ['stars', 'bruins', 'blackhawks', 'blues', 'jets']
hockey_result = reduce(lambda item1, item2: item1 + item2, hockey)
print(hockey_result)
