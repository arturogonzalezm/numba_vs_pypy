## Performance Test Benchmark(Python 3.6.4, PyPy3 and Numba)

This is a Performance test to showcase the difference between Plan Python 3.6.4, PyPy3 and Numba on Python 3.6.4.

#### Results:

* Python 3.6.4 with Numba Duration: 0.10754990577697754 seconds

* Plain Python 3.6.4 Duration: 9.799003601074219e-05 seconds

* PyPy3 Duration: 0.000247955322265625 seconds

![Benchmark Chart](../blob/images/one.png)

##### Mandelbrot

* Plain Python 3.6.4 Duration: 4.013276815414429 seconds

* Python with Numba Duration: 0.3357357978820801 seconds

* PyPy3 Duration: 2.660169839859009 seconds

![Benchmark Chart](../blob/images/two.png)

#

**Notes:**

* The source code has been tested on Linux and MacOS.

----

MIT License

Copyright (c) 2018 Arturo Gonzalez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.