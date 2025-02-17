from calculators.simplex_calc import SimplexCalc, Task
import unittest
import tempfile
import os


class TestSimplexCalc(unittest.TestCase):
    def setUp(self):
        self.calc = SimplexCalc()

    def test_read_task_file_not_found(self):
        result = self.calc.read_task_from_file("non_existing_file.txt")
        self.assertIsNone(result, "Should return None for a non-existing file")

    def test_read_task_file_success(self):
        test_content = """x1 x2
3 5 0
1 1 = 10
2 3 = 30
"""
        with tempfile.NamedTemporaryFile('w', delete=False) as tmp_file:
            file_path = tmp_file.name
            tmp_file.write(test_content)
        try:
            task = self.calc.read_task_from_file(file_path)
            self.assertIsNotNone(task, "Task should not be None for a valid file")
            self.assertEqual(task.var_names, ["x1", "x2"])
            self.assertAlmostEqual(task.objective_function, [3.0, 5.0])
            self.assertEqual(len(task.constraints), 2)
            self.assertEqual(len(task.rhs_values), 2)
            self.assertEqual(task.constraints[0], [1.0, 1.0])
            self.assertEqual(task.constraints[1], [2.0, 3.0])
            self.assertEqual(task.rhs_values, [10.0, 30.0])
        finally:
            os.remove(file_path)

    def test_check_only_zeros(self):
        task = Task()
        task.constraints = [
            [1.0, 0.0, 0.0],  # row 0
            [0.0, 2.0, 0.0]   # row 1
        ]
        # Check column 0, skipping row 0 => we are looking if row1,col0 == 0
        # row1,col0 is indeed 0. So we expect True
        result = self.calc.check_only_zeros(task, column=0, skip_row=0)
        self.assertTrue(result, "Column 0 except row0 should be zero => True")
        # Check column 1, skipping row 0 => row1,col1 is 2.0 => not zero => expect False
        result = self.calc.check_only_zeros(task, column=1, skip_row=0)
        self.assertFalse(result, "Column 1 except row0 is not zero => False")

    def test_get_basis(self):
        task = Task()
        task.var_names = ["x1", "x2", "x3", "x4"]
        task.constraints = [
            [1.0, 2.0, 1.0, 0.0],
            [2.0, 1.0, 0.0, 1.0]
        ]
        basis = self.calc.get_basis(task)
        self.assertEqual(basis, [2, 3], "Columns x3,x4 (indices 2,3) should be recognized as the basis")

    def test_solve_small_problem(self):        
        task = Task()
        task.var_names = ["x1", "x2", "x3", "x4"]
        task.objective_function = [3.0, 5.0, 0.0, 0.0]
        task.constraints = [
            [1.0, 1.0, 1.0, 0.0],  # x1 + x2 + x3 = 10
            [2.0, 3.0, 0.0, 1.0]   # 2x1 + 3x2 + x4 = 30
        ]
        task.rhs_values = [10.0, 30.0]
        self.calc.solve(task)
        self.assertTrue(True, "If we got here, the solve() method completed without error.")


if __name__ == '__main__':
    unittest.main()
