#!/usr/local/bin/python3

## NOTE: PLEASE CHANGE ABOVE INTERPRETER PATH TO DESIRED PATH!!

from __future__ import print_function
from sys import argv, stderr
from datetime import datetime, date
from json import load
from os.path import exists
from os import environ

def build_licence_mit():
    return """
// MIT License
//
// Copyright (c) {} {}
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
"""

def build_licence_apache2():
    return """
// Copyright {} {}
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
"""

__version__ = "1.1.0"

current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

if exists(environ["HOME"] + "/.mnfSettings.json"):
    settings = load(open(environ["HOME"] + "/.mnfSettings.json"))
else:
    settings = { "author": "Someone", "licence": None, "licensetext": None }

def build_licence():
    if settings["licensetext"] == "mit":
        return build_licence_mit()
    elif settings["licensetext"] == "apache2":
        return build_licence_apache2()
    else:
        return """
// Unknown License type
"""

try:
    argv[1]
except IndexError:
    stderr.write(f"usage: {argv[0]} <file/paths>\n")
    exit(1)

def _help():
    print(f"""usage: {argv[0]} <file/paths>
{argv[0]} is a program that automaticly creates 
c/c++ source or header files on the spot.

c source includes nothing special.
c++ source includes c guards.
any header source includes inclusion guards.
note: none of these options can be optioned-out.

just use the usage above like this example:
{argv[0]} src/user/user_struct.cpp src/user/user_struct.hpp""", file = stderr)
    exit(1)

for i in argv: 
    if "-h" in i: _help()
    if "-l" in i: settings["licence"] = True

del argv[0]

for filename in argv:
    isHeader = False
    isCPP    = False
    isASM    = False

    just_filename = filename[0:].split("/")[-1]

    filepath = filename
    file = open(filepath, "w")

    filename = filename.upper()
    filename = filename.split("/")[-1]

    if (filename.split(".")[-1].startswith("H")):
        isHeader = True
    elif (filename.split(".")[-1] == "CPP"):
        isCPP = True
    elif "ASM" in filename.split(".")[-1]:
        isASM = True

    filename = filename.replace(".", "_")
    filename = filename.replace(" ", "_")
    crap = []
    crap1 = list(filename)
    for i in crap1:
        crap.append(i)
    filename = "".join(crap)
    if (isHeader):
        file.write(f"""//
// {just_filename}
//
// created at {current_time}
// written by {settings["author"]}
//
""")
        if settings["licence"]:
            file.write(build_licence().format(date.today().year, settings["author"]))
        file.write(f"""

#if !defined({filename})
#define {filename}

// code...

#endif // {filename}""")
    elif (isCPP):
        file.write(f"""//
// {just_filename}
//
// created at {current_time}
// written by {settings["author"]}
//
""")
        if settings["licence"]:
            file.write(build_licence().format(date.today().year, settings["author"]))
        file.write("""

/* // C guards for C++
// Uncomment these lines if you need C compatibility
#if defined(__cplusplus)
extern \"C\" {
#endif // __cplusplus
*/

// code...

/* // Down here too
#if defined(__cplusplus)
}
#endif // __cplusplus
*/""")
    elif isASM:
        file.write(f"""; 
; {just_filename}
; 
; created at {current_time}
; written by {settings["author"]}
; 


; code...
""")
    else:
        file.write(f"""//
// {just_filename}
//
// created at {current_time}
// written by {settings["author"]}
//
""")
        if settings["licence"]:
            file.write(build_licence().format(date.today().year, settings["author"]))
        file.write("""

// code...""")

    file.close()

