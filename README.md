# Bertrand Paradox

The Bertrand paradox goes as follows: Consider an equi- lateral triangle inscribed in a circle. Suppose a chord of the circle is chosen at random. What is the probability that the chord is longer than a side of the triangle?

We have used three sampling methods (as discussed in the class) and caclulated the probability on `15000` samples.

## Sampling Methods

### Picking two random points on the circle's edge:

This method imagines randomly selecting two points on the circumference of the circle, and the line connecting those two points becomes the chord.

`Probability Obtained = 0.33`

### Picking a distance of the chord from the center

This method imagines randomly picking a distance from the center of the circle to the chord and drawing the chord.

`Probability Obtained = 0.5`

### Picking a random point inside the cirle

This approach involves selecting a random point inside the circle and then treating it as the midpoint of the chord.

`Probability Obtained = 0.25`

## Dependencies

The following libraries have been used.

```
matplotlib
numpy
seaborn
```

## Deployment

To deploy this project run for each of the three sampling methods.

```
  python3 bertrand_1.py
  python3 bertrand_2.py
  python3 bertrand_3.py
```

## Authors

- Aditi Khandleia
- Kushagra Srivastava
