import random
KREWES = {
    'orpheus': ['Emily','Kevin','Vishwaa','Eric','ray','Jesse','Tiffany','Amanda',
    'Junhee','Jackie','Tyler','Emory','Ivan','Elizabeth','Pratham','Shaw','Eric',
    'Yaru','Kelvin','Hong Wei','Michael','Kiran','Amanda','Joseph','Tanzim','David',
    'Yevgeniy'],

    'rex': ['William','Joseph','Calvin','Ethan','Moody','Mo','Big Mo', 'Peihua',
    'Saad','Benjamin','Justin', 'Alice','Hilary','Ayham','Michael','Matthew','Jionghao',
    'Devin','David','Jacob','Will','Hannah','Alex'],

    'endymion': ['Grace','Nahi','Derek','Jun Tao','Connor','Jason','Tammy','Albert',
    'Kazi','Derek','Brandon','Kenneth','Lauren','Biraj','Jeff','Jackson','Taejoon',
    'Kevin','Jude','Sophia','Henry','Coby','Manfred','Leia','Ahmed','Winston']
}

#write a program that will print the name of a randomly-selected student from the teams
def randomName():
    x = random.randint(0,3)
    if x == 0:
        a = random.randint(0, len(KREWES['orpheus']))
        print(KREWES['orpheus'][a])
    if x == 1:
        a = random.randint(0, len(KREWES['rex']))
        print(KREWES['rex'][a])
    if x == 2:
        a = random.randint(0, len(KREWES['endymion']))
        print(KREWES['endymion'][a])

randomName()
