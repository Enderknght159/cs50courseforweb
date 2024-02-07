name = "Yaseen"
print(name[1])

List = ['yaseen', 'Omar', 'Amr', 'Danger']

print(List[2])

Tuple = (2, 3, 4)

print(Tuple[1])

List.append("Lolo")
print(List[4])

Set = set()
Set.add(1)
Set.add(-1)

print(Set)
print(len(Set))
print(len(List))
print(len(Tuple))

print('[', end='')
for a in List:
    print(a, sep='', end=', ')
print(']')


Dict = {
    "Abdallah": "Boss",
    "Yaseen": "Archive",
    "Omar": "Communication",
    "Amr": "Photography and Social Media",
    "Sameh": "Buiscuts"
}
for i in Dict:
    print(i,2*'\t',Dict[i])