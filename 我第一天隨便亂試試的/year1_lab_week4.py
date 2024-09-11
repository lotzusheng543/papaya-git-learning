import urllib.request


def seq_sqrt(xs):
    result=[]
    for i in range(xs):
        result.append(i**2)
    return result


print(seq_sqrt(5))


def mean(xs):
    if len(xs)==0:
        return 0
    else:
        total = sum(xs)
        return total / len(xs)


print(mean([0, 1, 2]))


def noaa_string():
    url = "http://tgftp.nws.noaa.gov/data/observations/metar/decoded/EGHI.TXT"
    noaa_data_string = urllib.request.urlopen(url).read()
    return noaa_data_string.decode("utf-8")


def extract_temperature(data):
    lines = data.split('\n')
    for line in lines:
        if "Temperature" in line:
            try:
                temperature_f = float(line.split(':')[1].strip().split(' ')[0])
                temperature_c = (temperature_f - 32) * 5.0/9.0

                # Ignore decimal points <= 4, round up others
                if temperature_c - int(temperature_c) <= 0.4:
                    temperature_c = int(temperature_c)
                else:
                    temperature_c = int(temperature_c) + 1
                return temperature_c
            except (IndexError, ValueError):
                continue
    return None

# Call the noaa_string function to get the data from the NOAA website


noaa_data = noaa_string()


# Call the extract_temperature function and pass the retrieved data to get the
# temperature in Celsius


temperature = extract_temperature(noaa_data)

# Print the extracted temperature
if temperature is not None:
    print("Current Temperature in Southampton:", temperature, "°C")
else:
    print("Temperature information not found.")


def wc(filename):
    with open(filename, 'r') as f:
        word = f.read()
        word = word.split()
        count = len(word)
    return count


print(wc('data.txt'))


def line_averages(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            averages = []
            for line in lines:
                numbers = list(map(float, line.strip().split(',')))
                average = sum(numbers) / len(numbers)
                averages.append(average)
            return averages
    except FileNotFoundError:
        return f"File '{filename}' not found."
    except Exception as e:
        return f"An error occurred: {e}"


print(line_averages("data.csv"))


def count_sub_in_file(filename, s):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            occurrences = content.count(s)
            return occurrences
    except FileNotFoundError:
        return f"File '{filename}' not found."
    except Exception as e:
        return f"An error occurred: {e}"


filename = "28885-8.txt"
substring1 = "Alice"
substring2 = "alice"

occurrences1 = count_sub_in_file(filename, substring1)
occurrences2 = count_sub_in_file(filename, substring2)

print(f"Occurrences of '{substring1}': {occurrences1}")
print(f"Occurrences of '{substring2}': {occurrences2}")






