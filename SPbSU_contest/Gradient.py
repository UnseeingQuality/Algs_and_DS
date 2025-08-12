n = int(input())
data = []
for i in range(n):
    x,y = map(int, input().split())
    data.append([x,y])


def gradient_descent(data, h=0.1, eps=0.001, max_iter=100):
    n = len(data)
    a, b = 0.0, 1.0

    def compute_loss(a, b):
        return sum((y - a - b * x) ** 2 for x, y in data) / n

    def compute_gradient(a, b):
        grad_a = -2.0 / n * sum(y - a - b * x for x, y in data)
        grad_b = -2.0 / n * sum(x * (y - a - b * x) for x, y in data)
        return grad_a, grad_b

    prev_loss = compute_loss(a, b)
    for _ in range(max_iter):
        grad_a, grad_b = compute_gradient(a, b)
        a -= h * grad_a
        b -= h * grad_b
        curr_loss = compute_loss(a, b)
        if prev_loss - curr_loss <= eps:
            break
        prev_loss = curr_loss

    return a, b


a_final, b_final = gradient_descent(data)

print(f"{a_final:.5f} {b_final:.5f}")