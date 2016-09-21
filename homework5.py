import unittest
import math

main = '__main__' == __name__

class quadraticSolver:
    
    # Get user input values for coefficients in a quadratic equation.
    def getInput(self):
        
        # List of variable names.
        vList = ['a', 'b', 'c']
        
        # List of coefficient values.
        coeffs = []
        
        # Main user input loop.       
        for v in vList:
            while True:
                try:
                    coeffs.append(float(input("Please enter a value for " + v 
                                              + ": ")))
                    break
                except ValueError:
                    print("The previous input was not valid.")
                    
        # Return the list of coefficient values.
        return coeffs
    
    # Calculate roots of polynomial based on the quadratic formula.        
    def getRoots(self, coeffs):
        
        # Normalize the polynomial by dividing through by the leading 
        # coefficient; this makes the leading coefficient 1, which makes the
        # quadratic equation simpler.
        if coeffs[0] != 0:
            b = coeffs[1] / coeffs[0]
            c = coeffs[2] / coeffs[0]
        
        # Linear equation.    
        else:
            r = str(-coeffs[2] / coeffs[1])
            return False, set([r])
        
        # Calculate the discriminant of the quadratic.
        dsc = b ** 2 - 4 * c
        
        # Calculate the non-discriminant component of the quadratic formula.
        r = -b / 2
        
        # Fix to ensure only positive zero float values.
        if r == -0.0:
            r = -r
        
        # Three cases (for a degree 2 polynomial):
        
        # Two real roots.
        if dsc > 0:
            r1 = str(r + math.sqrt(dsc) / 2)
            r2 = str(r - math.sqrt(dsc) / 2)
            
        # Two complex roots.    
        elif dsc < 0:
            r1 = str(r) + ' + ' + str(math.sqrt(-dsc) / 2) + 'i'
            r2 = str(r) + ' - ' + str(math.sqrt(-dsc) / 2) + 'i'
            
        # Repeated real root.
        else:
            r1 = r2 = str(r)
            
        # Return the roots as a set (of strings).
        return True, set([r1,r2])


class testQuadraticSolver(unittest.TestCase):
    
    # Each test will have a quadratic solver object.
    def setUp(self):
        self.solver = quadraticSolver()        
    def tearDown(self):
        self.solver = None
        
    """ There are three general cases for the roots of a quadratic equation with
        real coeffcients:
        1. Two real roots;
        2. Two complex roots (complex conjugate pair):
            i. Roots with both a real and imaginary component,
            ii. Roots that are purely imaginary;
        3. A repeated real root.
        
        Furthermore, multiplying a quadratic's coefficients through by a 
        constant should yield the same roots.
        
        Test cases will focus on verifying this functionality."""
        
    # Test case: two real roots
    def testTwoRealRoots(self):
        # One positive, one negative root
        self.assertEqual(self.solver.getRoots([1, 0, -1]), 
                         (True, set(['-1.0', '1.0'])))
        
        # Constant multiple of the previous quadratic (same roots)
        self.assertEqual(self.solver.getRoots([2, 0, -2]), 
                         (True, set(['-1.0', '1.0'])))
        
        # Two positive real roots
        self.assertEqual(self.solver.getRoots([1, -5, 6]), 
                         (True, set(['2.0', '3.0'])))
        
        # Two negative real roots
        self.assertEqual(self.solver.getRoots([1, 5, 6]), 
                         (True, set(['-3.0', '-2.0'])))
        
        # Fractional coefficients
        self.assertEqual(self.solver.getRoots([1.5, -1.5, -5.625]), 
                         (True, set(['-1.5', '2.5'])))
    
    # Test case: two complex roots    
    def testTwoComplexRoots(self):
        # Real and imaginary components
        self.assertEqual(self.solver.getRoots([1, -2, 2]), 
                         (True, set(['1.0 + 1.0i', '1.0 - 1.0i'])))
        # Constant multiple of the previous quadratic
        self.assertEqual(self.solver.getRoots([3, -6, 6]), 
                         (True, set(['1.0 + 1.0i', '1.0 - 1.0i'])))
        # Purely imaginary roots
        self.assertEqual(self.solver.getRoots([1, 0, 1]), 
                         (True, set(['0.0 + 1.0i', '0.0 - 1.0i'])))
        
    # Test case: repeated real root    
    def testRepeatedRoot(self):
        self.assertEqual(self.solver.getRoots([1, -2, 1]), 
                         (True, set(['1.0', '1.0'])))
        
    # Test case: linear equation
    def testLinearEquation(self):
        self.assertEqual(self.solver.getRoots([0, 2, 1]), 
                         (False, set(['-0.5'])))
        
#unittest.main()

# Main program.
if main: 
    
    # Instantiate a quadratic solver.
    q = quadraticSolver()
    
    # The set of roots.
    isQuadratic, roots = q.getRoots(q.getInput())
    
    # Repeated root.
    if isQuadratic:
        if len(roots) == 1:
            print("There is a repeated root (multiplicity 2) at " 
                  + roots.pop() + ".")
        
        # Distinct roots.
        else:
            print("The roots of this polynomial are " + roots.pop() + " and " 
                  + roots.pop() + ".")
    
    else:
        print("The solution to this linear equation is " + roots.pop() + ".")