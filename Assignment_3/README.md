# Monty Hall

This is the third assignment submission for CS203: Mathematics for Computer Science III submitted by Aditi Khandelia and Kushagra Srivastava.

### Contents

- `monty_hall.py`
  - This is the main python file for the assignment.
  - It has functions to simulate the Monty Hall problem and plot the probability of winning vs no. of simulations.
- `monty_hall_results.csv`
  - This is the csv file containing the results of the simulation for the Monty Hall problem. It has been produces after running the simulation uptill `n <= 240` and storing the results. It contains aproximately `28500` rows.

### Build instructions

```
python3 monty_hall.py
```

### Formulae

$C$ denotes the event of choosing a door with car behind it before switching.
and $T$ denotes the event of choosing a door with a car behind it after switching.

$$P(win | W) = \frac{k}{n} * \frac{k - 1}{n - 2} + \frac{n - k}{n} * \frac{k}{n - 2}$$
$$P(win | T) = P(C) = \frac{k}{n}$$

Therefore,
$$\frac{P(win | W)}{P(win | T)} = \frac{\frac{k}{n} * \frac{k - 1}{n - 2} + \frac{n - k}{n} * \frac{k}{n - 2}}{\frac{k}{n}} = \frac{n - 1}{n - 2}$$ ⁠
