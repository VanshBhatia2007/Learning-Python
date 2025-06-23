# Redefine the two functions
f_x = symbols('f_x')
f_inv_x = symbols('f_inv_x')

# Equation given: 3f(x) - 2f(1/x) = x
equation = Eq(3*f_x - 2*f_inv_x, x)

# Differentiate both sides with respect to x
f_prime_x = symbols('f_prime_x')
f_prime_inv_x = symbols('f_prime_inv_x')

# Express f'(1/x) using the chain rule
f_prime_inv_x_expr = -f_prime_x / x**2

# Substitute into the differentiated equation
diff_eq = Eq(3*f_prime_x + 2*f_prime_inv_x_expr, 1)

# Solve for f'(x)
f_prime_solution = solve(diff_eq, f_prime_x)

# Now substitute x = 2 to get f'(2)
f_prime_at_2 = f_prime_solution[0].subs(x, 2)
f_prime_at_2
