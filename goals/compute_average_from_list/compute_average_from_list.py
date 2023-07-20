def average(number_list):
    sum = 0
    for number in number_list:
        sum += number
    return sum / len(number_list)

def test_average():
    number_list = [3, 4]
    expected_average = 3.5
    received_average = average(number_list)
    print("%f %f" % (expected_average, received_average))
    assert received_average == expected_average

test_average()