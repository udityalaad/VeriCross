<!-- Reference:
https://github.com/othneildrew/Best-README-Template -->
<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h1><i>VeriCross</i></h1>


  
  <img src="Read_Me_Content/top_label.jpg" alt="top_label.jpg">
  .

  <p align="center">
    An automated Program Verification Engine for Imperative Language !
  </p>
</div>

<br>

<!-- TABLE OF CONTENTS -->
<details open>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#sample-runs">Sample Runs</a></li>
    <li><a href="#license-or-author">License or Author</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<br>

<!-- ABOUT THE PROJECT -->
## About The Project
  *	VeriCross is a custom Program Verification Engine to prove correctness using specifications & constructs like loop invariants.
  *	The tool makes deductive analysis possible with over pinpoint accuracy.

  <p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With
  &nbsp; &nbsp; &nbsp; <img src="Read_Me_Content/Tech/Python.JPG" alt="Python" width="100"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <img src="Read_Me_Content/Tech/TatSu.png" alt="Tatsu" width="100"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <img src="Read_Me_Content/Tech/Z3.jpg" alt="Apache_Cordova">

  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <b><i> Python </i></b> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <b><i> TatSu </i></b> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; <b><i> z3 Solver </i></b>

  <p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
  #### Prerequisites
  * Python
  * TatSu, Coverage
  * z3 Solver (Microsoft)
  * Machine Requirements: Minimum 4GB RAM, Intel i5 Processor (or Equivalent)

  
  #### Setup & Use
  The program takes a WLang program as input and performs Verification on it.
  1. Create a file with WLang program.
  2. Run 'wlang/sym.py' in python with the path of file (from Part-1) as argument.

  <p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Sample Runs -->
## Sample Runs
  * We tried VeriCross on some interesting programs. And it was able to successfully verify all the them.
  * All the tries test cases and programs can be found in:
    1. 'wlang/q4b.prg'
    2. 'wlang/q4d.prg'
    3. 'wlang/test_sym.py'

  * ##### Example: Computing (x<sup>2</sup> - y<sup>2</sup>) using the form '(x-y) * (x+y)':
    <p align="center"><img src="Read_Me_Content/Implementation/Example_1.JPG" alt="Example_1.JPG"></p>

    * As we can see, no assertion errors were raised. Hence the invariant correctly verifies the program and is good enough to prove the post-condition.

  <p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License or Author
  * Uditya Laad - (University of Waterloo)

  <p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact
  <b>Uditya Laad</b> &nbsp; [@linkedin.com/in/uditya-laad-222680148](https://www.linkedin.com/in/uditya-laad-222680148/)
  
  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; [@github.com/udityalaad](https://github.com/udityalaad)
  
  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; udityalaad123@gmail.com

  <b>Project Link</b> &nbsp; [https://github.com/udityalaad/VeriCross](https://github.com/udityalaad/VeriCross)

  <p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
  * ECE 653 - Assignment 3, Prof. Arie Gurfinkel, Prof. Patrick Lam, University of Waterloo

  <p align="right">(<a href="#readme-top">back to top</a>)</p>
