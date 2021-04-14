#!/usr/local/bin/python3

## NOTE: PLEASE CHANGE ABOVE INTERPRETER PATH TO DESIRED PATH!!

from __future__ import print_function
from sys import argv, stderr
from datetime import datetime, date
from json import load
from os.path import exists
from os import environ

def build_license_mit():
    return """
MIT License
    
Copyright (c) {} {}
    
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
"""

def build_license_apache2():
    return """
Copyright {} {}
    
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    
    http://www.apache.org/licenses/LICENSE-2.0
    
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

def build_license_gplv2():
    return """
Copyright (C) {} {}
    
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
    
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
    
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

def build_license_gplv3():
    return """
Copyright (C) {}  {}
    
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
    
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
    
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

def build_license_llama1():
    return """
llamaking136's open source license
Copyright (c) {} {}
    
This code is under the terms of contitions of llamaking136's open source license.
If you wish to see the original license, view the file 'LICENSE' in the
root folder or go to
    
    https://new-web.notyourgroup.repl.co/licenses/open-source-1.txt
    
If you don't follow to these terms of conditions, it will not be tolerated
and will be handled by the owner of the repository.
"""

def add_comments(text, comment):
    result = []
    for i in text.split("\n"):
        if not i == "":
            result.append(comment + i)
        else:
            result.append("")
    return "\n".join(result)

__version__ = "1.1.4"

current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

if exists(environ["HOME"] + "/.mnfSettings.json"):
    settings = load(open(environ["HOME"] + "/.mnfSettings.json"))
else:
    settings = { "author": "Someone", "licence": None, "licensetext": None }

def build_licence():
    if settings["licensetext"] == "mit":
        return build_license_mit()
    elif settings["licensetext"] == "apache2":
        return build_license_apache2()
    elif settings["licensetext"] == "gplv2":
        return build_license_gplv2()
    elif settings["licensetext"] == "gplv3":
        return build_license_gplv3()
    elif settings["licensetext"] == "llama1":
        return build_license_llama1()
    elif settings["licensetext"] == "none" or settings["licensetext"] == None:
        return ""
    else:
        return """
Unknown License type
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
    isCHead  = False
    isHeader = False
    isCPP    = False
    isASM    = False
    isPy     = False

    just_filename = filename[0:].split("/")[-1]

    filepath = filename
    file = open(filepath, "w")

    filename = filename.upper()
    filename = filename.split("/")[-1]

    if filename.split(".")[-1] == "HPP":
        isCHead = True
    if (filename.split(".")[-1].startswith("H") and not isCHead):
        isHeader = True
    elif (filename.split(".")[-1] == "CPP"):
        isCPP = True
    elif "ASM" in filename.split(".")[-1]:
        isASM = True
    elif "PY" in filename.split(".")[-1]:
        isPy = True

    filename = filename.replace(".", "_")
    filename = filename.replace(" ", "_")
    crap = []
    crap1 = list(filename)
    for i in crap1:
        crap.append(i)
    filename = "".join(crap)
    if (isCHead):
        file.write(f"""//
// {just_filename}
//
// created at {current_time}
// written by {settings["author"]}
//
""")
        if settings["licence"]:
            file.write(add_comments(build_licence(), "// ").format(date.today().year, settings["author"]))
        file.write("""

#if !defined({})
#define {}

// #if defined(__cplusplus)
extern "C" {{
// #endif // __cplusplus

// code...

// #if defined(__cplusplus)
}}
// #endif // __cplusplus

#endif // {}
""".format(filename, filename, filename))
        continue

    if (isHeader):
        file.write(f"""//
// {just_filename}
//
// created at {current_time}
// written by {settings["author"]}
//
""")
        if settings["licence"]:
            file.write(add_comments(build_licence(), "// ").format(date.today().year, settings["author"]))
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
            file.write(add_comments(build_licence(), "// ").format(date.today().year, settings["author"]))
        file.write("""

// #if defined(__cplusplus)
extern \"C\" {
// #endif // __cplusplus

// code...

// #if defined(__cplusplus)
}
// #endif // __cplusplus
""")
    elif isASM:
        file.write(f"""; 
; {just_filename}
; 
; created at {current_time}
; written by {settings["author"]}
; 
""")
        if settings["licence"]:
            file.write(add_comments(build_licence(), "; ").format(date.today().year, settings["author"]))
        file.write("""

; code...
""")
    elif isPy:
        file.write(f"""# 
# {just_filename}
# 
# created at {current_time}
# written by {settings["author"]}
# 
""")
        if settings["licence"]:
            file.write(add_comments(build_licence(), "# ").format(date.today().year, settings["author"]))
        file.write("""

# code...
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
            file.write(add_comments(build_licence(), "// ").format(date.today().year, settings["author"]))
        file.write("""

// code...""")

    file.close()

