def get_weather(temp):
    if temp >= 20:
        return "hot"
    else:
        return "cold"

if __name__ == '__main__':
    print(get_weather(20))