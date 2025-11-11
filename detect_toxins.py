# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')

def make_accept_sound():
    print('made acceptance sound')

def contains_toxins(ingredients):
    return 'sodium nitrate' in ingredients or 'sodium benzoate' in ingredients \
           or 'sodium oxide' in ingredients

def alert_toxin_found():
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    make_alert_sound()

def confirm_toxin_free():
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()

ingredients = ['sodium benzoate']

if contains_toxins(ingredients):
    alert_toxin_found()
else:
    confirm_toxin_free()