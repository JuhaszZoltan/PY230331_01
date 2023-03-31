from module import *
versenyzok:list[Versenyzo] = []
file = open(file='Eredmenyek.txt', mode='r', encoding='ANSI')
for sor in file: versenyzok.append(Versenyzo(sor))

print(f'2. feladat: a versenyt {len(versenyzok)} versenyző fejezte be.')

ejsz:int = 0
for v in versenyzok:
    if v.kategoria == 'elit junior':
        ejsz += 1
print(f'3. feladat: versenyzők száma az "elit junior" kategóriában: {ejsz} fő')

eko:int = 0
for v in versenyzok:
    eko += 2014 - v.szul
aek:float = round(eko / len(versenyzok), 1)
print(f'4. feladat: átlagéletkor: {aek} év')

kk:str = input('5. feladat: kérek egy kategóriát: ')
rajtszamok:list[str] = []
for v in versenyzok:
    if v.kategoria == kk:
        rajtszamok.append(v.rajtszam)
if len(rajtszamok) == 0:
    print('\tnincs ilyen gategória!')
else:
    print('\trajtszámok:', end=' ')
    for rsz in rajtszamok:
        print(rsz, end=' ')

nok:list[Versenyzo] = []
for v in versenyzok:
    if not v.nem:
        nok.append(v)

mini:int = 0
for i in range(1, len(nok)):
    if nok[i].osszido < nok[mini].osszido:
        mini = i
print(f'6. feladat: legjobb időt {nok[mini].nev} érte el')