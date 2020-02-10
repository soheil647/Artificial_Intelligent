from Ca0 import df_New
import matplotlib.pyplot as plt
import numpy as np

df_New = df_New.dropna()
df_New = df_New.reset_index(drop=True)
print(df_New)


def cost_function(radio, sales, weight, bias):
    companies = len(radio)
    total_error = 0.0
    for i in range(companies):
        total_error += (-sales[i] + (weight * radio[i] + bias)) ** 2
    return total_error / (2 * companies)


def update_weights(radio, sales, weight, bias, learning_rate):
    weight_deriv = 0
    bias_deriv = 0
    companies = len(radio)

    for i in range(companies):
        # Calculate partial derivatives
        # -2x(y - (mx + b))
        weight_deriv += -2 * radio[i] * (sales[i] - (weight * radio[i] + bias))

        # -2(y - (mx + b))
        bias_deriv += -2 * (sales[i] - (weight * radio[i] + bias))

    # We subtract because the derivatives point in direction of steepest ascent
    weight -= (weight_deriv / companies) * learning_rate
    bias -= (bias_deriv / companies) * learning_rate

    return weight, bias


def train(radio, sales, weight, bias, learning_rate, iters):
    cost_history = []

    for i in range(iters):
        weight, bias = update_weights(radio, sales, weight, bias, learning_rate)

        # Calculate cost for auditing purposes
        cost = cost_function(radio, sales, weight, bias)
        cost_history.append(cost)

        # Log Progress
        if i % 10 == 0:
            print("iter={:d}    weight={:.2f}    bias={:.4f}    cost={:.2}".format(i, weight, bias, cost))

    return weight, bias, cost_history


# print(df_New["Chance of Admit"])
print(len(df_New["Chance of Admit"]))
teta0 = 1
teta1 = -1
teta0, teta1, costnew = train(df_New["CGPA"], df_New["Chance of Admit"], teta0, teta1, 0.01, 384)

plt.xlabel('CGPA')
plt.ylabel('Chance of Admit')
plt.plot(df_New["CGPA"], df_New["Chance of Admit"], 'ko')
x_plot = np.linspace(6.7, 10, 1000)
plt.plot(x_plot, x_plot * teta0 + teta1)
plt.show()
