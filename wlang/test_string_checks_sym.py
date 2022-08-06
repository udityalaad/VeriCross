# The MIT License (MIT)
# Copyright (c) 2016 Arie Gurfinkel

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import unittest
import z3
from . import ast, sym


class TestSym (unittest.TestCase):
    def test_one(self):
        prg1 = "havoc x; assume x > 10; assert x > 15"
        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        self.assertEquals(len(out), 1)

        with open('wlang/Test_Results/test_one.txt', 'r') as file1:
                print("Executed")
                self.assertEquals(str(file1.read()), str(out))



    # def test_two(self):
        prg1 = "havoc x, y; if (x > 0 and y < 0) then x := x + 1 else y := y - 1; assume y > x; assert y > x + 100; while y > x do {havoc x; y := y + x}"

        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        self.assertEquals(len(out), 10)

        with open('wlang/Test_Results/test_two.txt', 'r') as file1:
                print("Executed")
                self.assertEquals(str(file1.read()), str(out))

    # def test_three(self):
        prg1 = "havoc x, y"
        prg1 += "; if x + y > 15 then { x := x + 7; y := y - 12} else { y := y + 10; x := x - 2 }"
        prg1 += "; x := x + 2"
        prg1 += "; if 2 * (x + y) > 21 then { x := x * 3; y := y * 2 } else {x := x * 4; y := y * 3 + x }"
        prg1 += "; skip"

        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        self.assertEquals(len(out), 3)

        with open('wlang/Test_Results/test_three.txt', 'r') as file1:
                print("Executed")
                self.assertEquals(str(file1.read()), str(out))

    # def test_four(self):
        prg1 = "havoc x; r := 0"
        prg1 += "; if x > 8 then r := x - 7"
        prg1 += "; if x < 5 then r := x - 2"

        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        self.assertEquals(len(out), 3)

        with open('wlang/Test_Results/test_four.txt', 'r') as file1:
                print("Executed")
                self.assertEquals(str(file1.read()), str(out))


    # def test_five(self):
        prg1 = "havoc a, b, c; x := 0; y := 0; z := 0"
        prg1 += "; if a > 0 then x := -2"
        prg1 += "; if b < 5 then {if a <= 0 and c > 0 then y := 1; z := 2}"
        prg1 += "; assert(not(x + y + z = 3))"

        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        self.assertEquals(len(out), 4)

        with open('wlang/Test_Results/test_five.txt', 'r') as file1:
                print("Executed")
                self.assertEquals(str(file1.read()), str(out))


    # def test_six(self):
        prg1 = "havoc x, y"
        prg1 += "; if x > 0 then y := 10 else y := 20"
        prg1 += "; while x < 20 do {x := x + 1; if y = -1 then y := y + 1}"

        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        self.assertEquals(len(out), 12)

        with open('wlang/Test_Results/test_six.txt', 'r') as file1:
                print("Executed")
                self.assertEquals(str(file1.read()), str(out))


    # def test_while_10_ctns (self):
        prg1 = "havoc x; while x > 0 do havoc x"

        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        self.assertEquals(len(out), 11)

        with open('wlang/Test_Results/test_while_10_ctns.txt', 'r') as file1:
                print("Executed")
                self.assertEquals(str(file1.read()), str(out))



    # def test_coverage (self):
        total = ''

        prg1 = "havoc x; assume x = 10; assert x <= 15; if true then x := 1"
        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]

        print(out[0].pick_concrete())
        print(repr(out[0]))
        print(out[0].to_smt2())
        self.assertEquals(len(out), 1)

        total += str(out)

        prg1 = "skip; havoc x; y := x / 2; assume x >= 10; assert not (x <= 15) or x > 15; print_state; z := 10; if z = 0 then skip"
        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        self.assertEquals(len(out), 1)

        total += str(out)


        prg1 = "while false do skip"
        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        self.assertEquals(len(out), 1)

        total += str(out)


        prg1 = "assert false"
        ast1 = ast.parse_string(prg1)
        engine = sym.SymExec()
        st = sym.SymState()
        out = [s for s in engine.run(ast1, st)]
        print("Check it")
        self.assertEquals(len(out), 0)

        total += str(out)

        

        with self.assertRaises(SystemExit):
            sym.main()

        st = sym.SymState()
        st.add_pc(False)
        print(st.pick_concrete())


        with open('wlang/Test_Results/test_coverage.txt', 'r') as file1:
                print("Executed")
                self.assertEquals(str(file1.read()), str(total))

        
        prg1 = "while false do skip"
        ast1 = ast.parse_string(prg1)
        ast1.stmts = None
        engine = sym.SymExec()
        st = sym.SymState()
        self.assertIsNone(engine.visit_StmtList(ast1, state = st))
        
        

    # def test_q5e_diverges (self):
    #     ast1 = ast.parse_file("wlang/sym_diverge.prg")
    #     engine = sym.SymExec()
    #     st = sym.SymState()
    #     out = [s for s in engine.run(ast1, st)]
    #     self.assertEquals(len(out), 426)