# projinda23

## Tetris


### Pre-develop
Projektuppgift för kursen DD1349, VT23.

Skapat av:
Samuel Flodin (samflo) och Fabian Öst (fabianos)

Planen i projektuppgiften är att skapa spelet tetris i Python.

Det här är första gången som vi jobbar i python och ser det som en rolig utmaning. 
Tanken är att använda Pygame som libary när vi bygger spelet.

I grunden bör det finnas kunskap om spelets game mechanics, något som kan finnas [här](https://tetris.wiki/Tetris_Guideline).
Kort förklarat är det ett pusselspel som handlar om att matcha olika figurer med utrymmen för att minska antalet tomma rutor som möjligt under tidspress.
Än så länge går spelet inte att vinna, utan bara att förlora. Det sker då en figur når toppen av spelplanen, detta hindras genom att få en hel rad
täckt med figurer, då elimineras den raden, och raderna ovan flyttas ned ett steg.

Efter detta bör vi implementera spelets funktioner, och utseende inlkudernade spelobjekt, men även input från spelaren så att det blir interaktivt.
Ett poängsystem skulle också vara intressant och nivåer för spelaren.

Om allt detta går snabbt att implementera så finns det även ideer om att göra det multplayer (på en dator).

Premilinärt så gissar vi att spelet startas i terminalen och då behövs nog det laddas ner från denna repo.

###Post

Tetris går nu att spela från den kod som vi har utvecklat. Det funkar genom att klona repon och sedan se till att pygame är nerladdat på datorn samt python3. Spelet startas från Maingame.py. 

Vi har även implementerat en scoreboard, tyvärr utan player name, men den sparar dina scores och om det är något du är stolt över så kan du kanske skicka en pull request och skicka in din score. Annars om man är lat går det bara att fuska och skriva in en sjukt stor score i txt-filen :P.
