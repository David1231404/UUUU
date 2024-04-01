# На строке 2 заменить конкатенацию на форматирование
# concat, concatenate, конкатенация - "сложение плюсиком"

def GiveParametorPon(имя, отчество):
    return f"Привет, {отчество} {имя}!"

GiveParametorPon('ИГОРЬ', 'ИВАНЫЧ')

print(GiveParametorPon(отчество= "ИГОРЬ",имя="ИВАНЫЧ"))

print(GiveParametorPon(имя='ИВАНЫЧ', отчество="ИГОРЬ"))