import random
import matplotlib.pyplot as plt

def estimate_last_passenger_seat(k, n):
    pdf = [0] * n
    for j in range(k):
        left_seats = set(range(1, n + 1))
        actual_seating = []
        for i in range(1, n + 1):
            # first passenger
            if i == 1:
                s = random.sample(left_seats, 1)[0]
            # last passenger
            elif i == n:
                s = list(left_seats)[0]
            # other passenger
            else:
                if i in left_seats:
                    s = i
                else:
                    s = random.sample(left_seats, 1)[0]
            #print(s)
            actual_seating.append(s)
            left_seats = left_seats - set([s])
        #print(actual_seating)
        last_p_seat = actual_seating[n-1]
        index = last_p_seat-1
        pdf[index] += 1
    print(actual_seating)
    pdf = [float(p)/float(k) for p in pdf]
    print(pdf)
    return pdf



if __name__ == "__main__":
    k = 10000
    n = 10
    p = estimate_last_passenger_seat(k, n)

