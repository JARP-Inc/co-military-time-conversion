from typing import Tuple


def main():
    words = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "10": "ten",
        "11": "eleven",
        "12": "twelve",
        "13": "thirteen",
        "14": "fourteen",
        "15": "fifteen",
        "16": "sixteen",
        "17": "seventeen",
        "18": "eighteen",
        "19": "nineteen",
        "20": "twenty",
        "30": "thirty",
        "40": "forty",
        "50": "fifty",
    }

    def string_to_parts(time_string: str) -> Tuple[str, str]:
        if "." in time_string:
            time_string = time_string.replace(".", ":")
        parts = time_string.split(":")

        hours = parts[0]
        mins = parts[1][:-2]
        am_pm = parts[1][-2:]

        if hours == "12" and am_pm == "AM":
            hours = "0"
        elif am_pm == "PM" and hours != "12":
            hours = str(int(hours) + 12)

        altered_parts = (hours.zfill(2), mins)
        return altered_parts

    def hours_string_to_words(hours: str) -> str:
        if int(hours) == 0:
            return "zero"
        elif 10 <= int(hours) <= 19:
            return words[hours]
        else:
            hours_tens = str(int(hours[0]) * 10)
            return f"{words[hours_tens]} {words[hours[1]]}"

    def mins_string_to_words(mins: str) -> str:
        if int(mins) == 0:
            return "hundred hours"
        elif 10 <= int(mins) <= 19:
            return words[mins]
        else:
            mins_tens = str(int(mins[0]) * 10)
            return f"{words[mins_tens]} {words[mins[1]]}"

    # THIS IS THE SOLUTION !!1!
    def military_time_conversion(time_string: str) -> str:
        hours_string, mins_string = string_to_parts(time_string=time_string)
        hours_words = hours_string_to_words(hours_string)
        mins_words = mins_string_to_words(mins_string)
        return f"{hours_words} {mins_words}"

    # tests
    def test():
        test_cases = [
            "12:00AM",
            "12:00PM",
            "1:00AM",
            "1:00PM",
            "11:00PM",
            "12:59PM",
            "9:09AM",
            "11:22AM",
            "5:06PM",
            "4.59AM",
        ]
        for case in test_cases:
            military_time = military_time_conversion(case)
            print(f"{case} -> {military_time}")

    # test()


if __name__ == "__main__":
    main()
