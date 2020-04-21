# PLocker
#### created, 21/04/2020
#### By [E Naika](https://github.com/ENAIKA)
## Description
* This is a cli based app that help user store their account credentials for different accounts.
 
## Setup/Installation Requirements
* The app runs in cli
#### To Contribute
* Before starting the steps below: make sure Python3.6 is installed or have compartible version
Follow this steps:
* Fork the repo
* Create your branch 
* Make the appropriate changes in the files
* Add changes to reflect the changes made 
* Commit your changes 
* Push to the branch 
* Create a Pull Request.

# Behaviour Driven Design
* The app should help user store credentials for different accounts.

### Specifications
| Behaviour                | Input example           | Output Example                   |
| ---------------------------|:-----------------------:| --------------------------------:|
|  pick short code     | l and the user is not registered| False/Ask user to use short codes provided |
| pick short code              |da,du | True/search results display if they exist|
|  pick short code      |  fa,fu | True/If user or account available display results else display doesn't exist|
|  pick short code      | cu,ca | True/create user or account credentials respectively  |
|  pick short code      | ex | True/exit the app/account credentials interface  |
|  pick short code      | short code not among provided| False/Ask user to use short codes provided |



## Technologies Used
* Python-programming language
* VS Code-IDE


### License
* MIT License

* Copyright © [E NAIKA](https://github.com/ENAIKA)[2020]

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