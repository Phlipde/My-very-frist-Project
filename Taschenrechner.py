Erstetext = input('Was ist deine erste Zahl?')
Rechenzeichen = input('''Welches Rechenzeichen möchtes du verwenden?
+, -, x, :   /: ''')
Zweitetext= input('Was ist deine zweite Zahl?')

if Rechenzeichen == 'x':
    Rechenart='*'
elif Rechenzeichen ==':':
    Rechenart='/'
elif Rechenzeichen == '+':
    Rechenart='+'
elif Rechenzeichen == '-':
    Rechenart='-'

Erstezahl = int(Erstetext)
Zweitezahl = int(Zweitetext)

if Rechenart == '+':
    Ergebnis=Erstezahl+Zweitezahl
elif Rechenart == '-':
    Ergebnis=Erstezahl-Zweitezahl
elif Rechenart == '*':
    Ergebnis=Erstezahl*Zweitezahl
elif Rechenart == '/':
    Ergebnis=Erstezahl/Zweitezahl

print("Das Erbebnis von {}{}{} ist".format(Erstezahl,Rechenzeichen,Zweitezahl), "\n", Ergebnis)
