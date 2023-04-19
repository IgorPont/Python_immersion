def function(file_num, file_name, file_res):
    with (open(file_num, 'r', encoding='utf-8') as f1,
          open(file_name, 'r', encoding='utf-8') as f2,
          open(file_res, 'w', encoding='utf-8') as f3
          ):
        len_file_num = sum(1 for i in f1)
        len_file_name = sum(1 for i in f2)
        print(len_file_num, len_file_name)

        for _ in range(max(len_file_num, len_file_name)):
            num = read_line(f1)
            name = read_line(f2)
            num_split = num.split('|')
            mult = int(num_split[0]) * float(num_split[1])
            if mult > 0:
                result = f'{name.upper()} {round(mult)}'
            elif mult < 0:
                result = f'{name.lower()} {abs(mult)}'
            f3.write(f'{result}\n')


def read_line(file_descriptor):
    text = file_descriptor.readline()
    if text == '':
        file_descriptor.seek(0)
        text = file_descriptor.readline()
    return text[:-1]


if __name__ == '__main__':
    function('test1.txt', 'test2.txt', 'test3.txt')
