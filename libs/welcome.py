import sys
sys.tracebacklimit=0

def prompt_questions():
    print("\033[1;34;40m Veuillez entrer le numéro correspondant : ")

    datas_prompt = {
        1: 'Programmer un nouveau post sur LinkedIn.',
        2: 'Lancer en tâche de fond les posts programmés.',
        3: 'Lancer un test de connexion.'
    }
    
    for i in datas_prompt:
        print("- " + str(i) + " : " + datas_prompt[i])

    answer = input("\nVotre choix : ")

    while not answer.isdigit():
        print("\n\033[1;31;40m -------------------------------------------------------")
        print("\n\033[1;31;40m Le chiffre doit être compris entre 1 et " + str(len(datas_prompt.keys())) + ".")
        print("\n\033[1;31;40m -------------------------------------------------------\n")
        return questions()

    return answer

def presentation():
    print("\033[1;33;40m ************************************")
    print("\033[1;33;40m www.tansoftware.com")
    print(" automate linkedin posting")
    print(" version 0.0.1")
    print("\033[1;33;40m ************************************\n")

def questions():
    return prompt_questions()
    
