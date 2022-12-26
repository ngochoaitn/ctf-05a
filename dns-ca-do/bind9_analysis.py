from collections import Counter

input_file = input('File bind log: ')
ip_client = input('IP Client: ')
level = int(input('Level: '))
res = []
with open(input_file, 'r', encoding='UTF-8') as file:
    while (line := file.readline().rstrip()):
        if(ip_client in line and 'queries' in line):
            # print(line)
            if('(' in line and ')' in line):
                temp = line[line.find('(')+1:line.find(')')]
                temp = temp.replace('.com.vn', '.com_vn')
                urls = temp.split('.')
                urls_len = len(urls)
                url = ''

                if(urls_len >= level):
                    for i in range(urls_len - level, urls_len):
                        url += urls[i]
                        if(i < urls_len - 1):
                            url += '.'
                else:
                    url = temp
                res.append(url)
                    # print(url)

new_vals = Counter(res).most_common()
new_vals = new_vals[::-1] #this sorts the list in ascending order

for a, b in new_vals:
    print(b, '\t', a)