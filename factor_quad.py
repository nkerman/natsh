#!/usr/bin/env python
# %%
import numpy as np
# %%
class PolyFunction:
    def __init__(self, coeffs):
        self.coeffs = coeffs
        self.poly_order = len(coeffs) - 1
    @property
    def string(self):
        string_repr = []
        for coeff_num, coeff in enumerate(self.coeffs[:-1]):
            if coeff != 0:
                string_repr.append(f"{coeff if coeff !=1 else ''}x^{self.poly_order - coeff_num}")
        if self.coeffs[-1] != 0:
            string_repr.append(str(self.coeffs[-1]))
        return " + ".join(string_repr)
    
    def __repr__(self) -> str:
        return str(self.string)
# %%
class QuadraticFunction(PolyFunction):
    def __init__(self, coeffs):
        super().__init__(coeffs)
        self.a = self.coeffs[0]
        self.b = self.coeffs[1]
        self.c = self.coeffs[2]
    def check_quad(self):
        assert self.poly_order == 2, f"NOT  QUADRATIC {self.poly_order, self.coeffs}"
    def get_midpoint(self):
        return((-self.b/self.a)/2)
    def get_dist(self):
        return (self.get_midpoint()**2 - (self.c/self.a))**0.5
    def get_zeros(self):
        zero0 = self.get_midpoint() - self.get_dist()
        zero1 = self.get_midpoint() + self.get_dist()
        return zero0,zero1        
# %%
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("coefficients", nargs="*", type=float, default=None, help="Coefficients of our function")
    args = parser.parse_args()
    if not args.coefficients:
        print("Missing coefficients - Please enter the coefficients of your polynomial separated by spaces. Remember to check signs!\n")
        user_coeffs = input("Please enter the coefficients of your polynomial separated by spaces.")
        args.coefficients = [float(o)  for o in user_coeffs.split(" ")]
        # print(args.coefficients)
    if len(args.coefficients) == 3:
        f = QuadraticFunction(coeffs=args.coefficients)
        print(f.string)
        print("The zeros of this quadratic function are: ")
        [print(f"-->  {z:.4f}") for z in f.get_zeros()]
    else:
        f = PolyFunction(coeffs=args.coefficients)
        print(f.string)
        
# %%
