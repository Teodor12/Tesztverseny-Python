data_list = []

def sum_points(answer_key, answer):
    points = 0;
    for i in range(0,len(answer_key)):
        if answer[i] == answer_key[i]:
            if 0 <= i <= 4:
                points += 3
                continue
            if 5 <= i <= 9:
                points +=4
                continue
            if 10 <= i <=12:
                points +=5
                continue
            if i == 13:
                points +=6
                continue
    return points


print('1. feladat: Az adatok beolvasasa\n')
input_file = open('valaszok.txt')
answer_key = input_file.readline().strip()
for line in input_file:
    data_list.append(line.strip())

print('2. feladat: A versenyen ' + str(len(data_list)) + ' versenyzo indult.\n')


id = input('3. feladat: A versenyzo azonositoja: ')
answer = ''
for data in data_list:
    db = data.split(' ')
    if db[0] == id:
        answer = db[1]
        print(answer, ' (a versenyzo valaszai)')
        break

print('4. feladat:')
print(answer_key + '\t'+'(helyes megoldas)')
for i in range(0, len(answer_key)):
    if answer[i] == answer_key[i]:
        print('+', end='')
    else:
        print('', end=' ')
print('\t' + '(a versenyzo helyes valaszai)\n')

x = int(input('5. feladat: A feladat sorszama = '))
counter = 0
exercise_answer = answer_key[x-1]

for data in data_list:
    db = data.split(' ')
    temp_answer = db[1][x-1]
    if temp_answer == exercise_answer:
        counter +=1
percentage = round(counter/len(data_list),4) * 100
print('A feladatra ' + str(counter) + ' fo, a versenyzok ' + str(percentage) + ' %-a adott helyes valaszt.\n')

print('6. feladat: A versenyzok pontszamanak meghatarozasa')
output_file = open('pontok.txt', 'w')
results = []
for data in data_list:
    db = data.split(' ')
    results.append([db[0], sum_points(answer_key,db[1])])
    output_file.write(db[0] + ' ' + str(sum_points(answer_key,db[1]))+'\n')
output_file.close()
print()

print('7. feladat: A verseny legjobbjai: ')
points = set()
for result in results:
    points.add(result[1])
points = sorted(list(points), reverse= True)[0:3]

for point in points:
    for result in results:
        if result[1] == point:
            print(str(points.index(point)+1) +'. dij ' + '('+ str(point) +' pont):' + ' ' + result[0])