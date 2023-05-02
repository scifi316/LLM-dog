##General Notes
Large models tend to favor GPU acceleration or devices of a similar nature, hence we should prioritize development in Python and C/C++
Basing a lot of the heavy **AI modeling** to **TensorFlow** and **NumPy**, using **C libraries** for the rest...

This README.md is located in /dog/ relative to other files being in:
 - /dog/integration/
 - /dog/LLM/
 - ../CAD/

##General System Requirements
 - minimum python version >= 3.10.x
 - pyqt6 and pyqt6-tools
 - pytorch2 -- with minimum prefered CUDA device >= CUDA 11.7
 - gcc with cmake and associated C/C++ tools 
 - ~~tensorflow 2~~ -- under testing
