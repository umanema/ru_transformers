file =  open("dataset.txt", encoding="utf-8")
lines = file.readlines()

json = open("valid.json", "w+",  encoding="utf-8")

links_positions = []

i = 0
for l in lines:
    if 'https' in l:
        links_positions.append(i)

    i += 1

f_id = 0
for x in range(len(links_positions)-2):
    start = links_positions[x] + 1
    fanfic=lines[start : links_positions[x+1]]
    fanfic_no_trailing_new_line = []
    for f_l in fanfic:

        # fafic_no_trailing_new_line.append(f_l.rstrip("\n"))
        fanfic_no_trailing_new_line.append(f_l.replace('\n', '\\n'))

    fanfic_oneline=''.join(fanfic_no_trailing_new_line)
    json_string = '{"src": "ficbook", "text": "' + fanfic_oneline + '", "type": "Ru", "id": "' + str(f_id) + '", "title": "untitled"}\n'

    # print(json_string)
    json.write(json_string)
    f_id += 1

fanfic=lines[links_positions[len(links_positions) - 1] + 1 : ]
fanfic_no_trailing_new_line = []
for f_l in fanfic:

    # fafic_no_trailing_new_line.append(f_l.rstrip("\n"))
    fanfic_no_trailing_new_line.append(f_l.replace('\n', '\\n'))

fanfic_oneline=''.join(fanfic_no_trailing_new_line)
json_string = '{"src": "ficbook", "text": "' + fanfic_oneline + '", "type": "Ru", "id": "' + str(f_id) + '", "title": "untitled"}\n'
json.write(json_string)
