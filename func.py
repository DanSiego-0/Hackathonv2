import struct



def Clean(data):
    cleaned = ""
    for str in data:
        if str.isalpha():
            cleaned += str
        else:
            pass
    return cleaned

def ReturnFact(data):
    return {
        'Nido':"Nido is not a breast milk substitute. It contains lots of protein, sugar, and carbs. Use only upon the advice of health professional",
        'Nequik':"Great source for Vitamin D which is needed for growth :)",
        'Popcorn':"There is a myth lurking in social media saying that popcorn contains carcinogens. This is a myth only.",
        'Hotdog':"It is not made from dogs",
        'Head and Shoulders':"This could actually give you more dandruff. Though it provides users instant relief while using.",
        'The Ordinary Niacinamide':'Perfect for people with psoriasis',
        'Jeju Volcanic Pore Cleanser innisfree':'Has a lot of fragrance which is not good for sensitive skin',
        'Milo':"60 percent sugar is a lot."
    }.get(data,"not found")
