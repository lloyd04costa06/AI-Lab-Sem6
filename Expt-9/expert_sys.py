import tkinter as tk
knowledge_base = {
    'Snapchat': ['send snaps','maintain snap streaks', 'use snap filters', 'like updating your bitmoji outfit'],
    'Instagram': ['like posting cool pictures','like opening stories', 'like making reels','like watching reels']
}
ent=[]
def inference(Answers):
    probabilty = {}
    for SocialMed in knowledge_base.keys():
        count = 0
        for Answer in knowledge_base[SocialMed]:
            if Answer in Answers:
                count += 1
        probabilty[SocialMed] = count/len(knowledge_base[SocialMed])

    maxprobability = 0
    for SocialMed in probabilty.keys():
        if probabilty[SocialMed] > maxprobability:
            maxprobability = probabilty[SocialMed]

    SocialMedia = ''
    for SocialMed in probabilty.keys():
        if probabilty[SocialMed] == maxprobability:
            SocialMedia += SocialMed +','

    SocialMedia = list(SocialMedia)
    SocialMedia[-1] = '.'
    SocialMedia = ''.join(SocialMedia)

    if maxprobability == 1:
        return('You use '+SocialMedia)
    elif maxprobability > 0:
        return('You use '+SocialMedia)
    else:
        return('You dont use any')

def buttonClicked(question,Answers):

    for i in ent:
        if i.get() == 'yes':
                Answers.append(question)
    x=inference(Answers)
    labelT4 = tk.Label(window,text=x,font=("Arial", 12))
    labelT4.pack()
    


def askquestions():
    Answers = []
    questions = []
    for SocialMed in knowledge_base.keys():
        
        questions += knowledge_base[SocialMed]
  
    questions = list(set(questions))
   
   
    for i,question in enumerate(questions):
        labelT4 = tk.Label(window,text=f'Do you {question}? ')
        labelT4.pack()
        entry = tk.Entry(window, width=30, font=("Arial", 10))
        entry.pack(pady=3)
        ent.append(entry)

    
    button = tk.Button(window, text="Submit", command=lambda:buttonClicked(question,Answers))
    button.pack(pady=6)
        
  

window = tk.Tk()

window.geometry('300x600')
label = tk.Label(window, text="EXPERT SYSTEM",font=("Arial", 14))
label.pack(pady=5)

labelT = tk.Label(window, )
labelT.pack()
labelT2 = tk.Label(window,text="Please Answer The Following Questions" )
labelT2.pack()
labelT3 = tk.Label(window, )
labelT3.pack()

a=askquestions()


window.mainloop()

# Answers = askquestions()
# inference(Answers)