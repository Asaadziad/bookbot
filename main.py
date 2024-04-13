def count_letters(string):
    letter_dict = {}
    for i in range(0,26):     
        letter_dict[chr(97 + i)] = 0
    str_arr = string.lower().split()
    for s in str_arr:
        for ch in s:
            if ord(ch) not in range(97, 97 + 26):
                continue
            letter_dict[ch] += 1
    return letter_dict

def sort_on(dict):
    return dict["value"]

def dict_to_list(dict):
    list = []
    for key in dict:
        list.append({"key": key, "value": dict[key]})
    return list
def print_character(ch, num):
    print(f"The '{ch}' character was found {num} times")
# report is a dictionary
def print_report(report):
    print("---------- Begin of the Report ----------")
    report_list = dict_to_list(report)
    report_list.sort(reverse=True, key=sort_on)
    for s in report_list:
        print_character(s["key"], s["value"])
    print("---------- End of the Report ----------")

def main():
    content = ""
    with open('./books/franke.txt', 'r') as f:
        content = f.read()
    report = count_letters(content)
    print_report(report)

main()