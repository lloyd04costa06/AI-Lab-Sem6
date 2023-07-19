knowledge_base = {
    'action': ['explosions', 'fight scenes', 'car chases'],
    'comedy': ['humor', 'laughs', 'funny dialogue'],
    'drama': ['emotional', 'intense', 'character development'],
    'romance': ['love story', 'heartwarming', 'chemistry'],
    'horror': ['scary', 'suspenseful', 'jump scares']
}

def AskQuestion():
    GetKeywords=set()
    #We are using a set because we dont want any key word to repeat again and again
    for c in knowledge_base.keys():
        for pref in knowledge_base[c]:
            GetKeywords.add(pref)
    
    #Convert from set to list
    Keywords=list(GetKeywords)

    #Use this keywords list to form your questions
    RecordedAnwers=[]
    for kyword in Keywords:
        Ans=input(f"Do you like {kyword}? [y/n]")
        if Ans=='y':
            RecordedAnwers.append(kyword)

    return RecordedAnwers

def Inference(answers):
    probability={}
    for Key in knowledge_base.keys():
        count=0

        for word in knowledge_base[Key]:
            if word in answers:
                count=count+1
        
        probability[Key]=count/len(knowledge_base)
    
    #Afterr this step you will get a new dictionary like
    # {action: 0.2,drama:0.9} and so on

    #Now just find the max probability
    maxProb=max(probability.values())

    #Now match all the probabiities that have this max values and thats gonna be the answer u hav to display
    prediction=[]
    for key in knowledge_base.keys():
        if probability[key]==maxProb:
            prediction.append(key)

    #Now just print your prdiction

    print("You may Like")
    for Pred in prediction:
        print(Pred)





        











#Imaginary int main()
UserAnswers=AskQuestion()
Inference(UserAnswers)

