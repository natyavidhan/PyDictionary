import PySimpleGUI as sg
from PyDictionary import PyDictionary


# ===============================================================================================


layout = [
    [
     sg.Text(size=(26, 0)), 
     sg.Text("PyDictionary",font='Acme 60'), 
     sg.Text(size=(20, 0))
     ],
    
    [ 
     sg.Text('_' * 110, justification='c')
     ],
    
    [
     sg.Text(size=(20, 3))
    ],
    
    [
     sg.Text(size=(5, 1)), 
     sg.Text('Word-Meaning', font='Acme 12', size=(15, 1)), 
     sg.Text(size=(15, 1)), 
     sg.Text('Antonym', font='Acme 12', size=(15, 1)), 
     sg.Text(size=(15, 1)), 
     sg.Text('Synonym', font='Acme 12', size=(15, 1))
     ],
    
    [ 
     sg.Text(size=(5, 1)), 
     sg.Input(font='Acme 12', size=(15, 1), key="meaning"), 
     sg.Text(size=(13, 1)), 
     sg.Input(font='Acme 12', size=(15, 1), key="antonym"), 
     sg.Text(size=(13, 1)), 
     sg.Input(font='Acme 12', size=(15, 1), key="synonym")
     ],
    
    [ 
     sg.Text(size=(5, 1)), 
     sg.Button('Search', font='Acme 12', size=(15, 1), key="meaningsearch"), 
     sg.Text(size=(15, 1)), 
     sg.Button('Search', font='Acme 12', size=(15, 1), key="antonymmsearch"), 
     sg.Text(size=(15, 1)), 
     sg.Button('Search', font='Acme 12', size=(15, 1), key="synonymsearch")
     ],
    
    [ 
     sg.Text(size=(5, 1)), 
     sg.Multiline(font='Acme 12', size=(20, 5), key="meaningres"), 
     sg.Text(size=(5, 1)), 
     sg.Multiline(font='Acme 12', size=(20, 5), key="antonymres"), 
     sg.Text(size=(6, 1)), 
     sg.Multiline(font='Acme 12', size=(20, 5), key="synonymres")
     ]
]


# ===============================================================================================

def sort(meaning):
    print(meaning)
    final = ''
    try:
        num = 0
        noun = meaning['Noun']
        final += "Noun: \n"
        for men in noun:
            num += 1
            final += f"{num}: {men}\n"
    except:
        pass
    try:
        num = 0
        Verb = meaning['Verb']
        final += f"Verb: \n"
        for men in Verb:
            num += 1
            final += f"{num}: {men}\n"
    except:
        pass
    try:
        num = 0
        Adverb = meaning['Adverb']
        final += f"Adverb: \n"
        for men in Adverb:
            num += 1
            final += f"{num}: {men}\n"
    except:
        pass
    try:
        num = 0
        Adjective = meaning['Adjective']
        final += f"Adjective: \n"
        for men in Adjective:
            num += 1
            final += f"{num}: {men}\n"
    except:
        pass
    return final
    
                 
window = sg.Window('PyDictionary', layout, icon='book.ico')
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif event == 'meaningsearch':
        meaning = sort(PyDictionary.meaning(values['meaning']))
        window['meaningres'].update(meaning)
        
    elif event == 'synonymsearch':        
        synonym = PyDictionary.synonym(values['synonym'])
        finalsynonyms = ''
        num = 0
        if synonym != None:
            for syn in synonym:
                num += 1
                finalsynonyms += f"{num}: {syn}\n"
            else:
                pass
        window['synonymres'].update(finalsynonyms)
        
    elif event == 'antonymmsearch':   
        antonym = PyDictionary.antonym(values['antonym'])
        finallantonyms = ''
        num = 0
        if antonym != None:
            for ant in antonym:
                num += 1
                finallantonyms += f'{num}: {ant}\n'
        else:
            pass     
        window['antonymres'].update(finallantonyms)
        
window.close()