#%%
#""""
def cooking(recipe):
    def cooking_recipe():
        print(recipe.__doc__)
        prep()
        recipe()
        cleanup()
    return cooking_recipe


def prep():
    print('go to the kitchen')
    print('get the ingredients')
    print('get the equiments - dishes, cutlery..')

def cleanup():
    print('Wash the dishes and cutlery!')
    print('-'*10)


#********************************
#********************************


@cooking
def cook_rice():
    '''
    Recipe for Rice
    '''
    print('wash the rice')
    print('add rice to pan with water')
    print('...')

@cooking
def cook_egg():
    '''
    Recipe for Egg
    '''
    print('heat oil in the pan')
    print('crack open an egg')
    print('...')

cook_rice()
cook_egg()


# %%
