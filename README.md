# Python Hex Debugger

I created this simple tool to make it easier to debug memory when working with different applications.

---

## Big Endian vs Little Endian

I'm not going to go very in-depth into how these differ, but the main points are as follows:

Big endian:
- stores the most significant byte on the left
- when reading memory, you read it from "left to right" - this is intuitive for people who are used to English where we read from left to right

Little endian:
- stores the most significant byte on the right
- when reading memory, you read it from "right to left" - this is counter-intuitive for people who are used to English, we essentially have to read memory backwards

---

## How to use it
This tool is most useful if you know the byte order ahead of time. I created this tool to help me debug some conversions from C code to Java code.

As an example, I will compare the hex dump of both a Java application and a C application that are both storing the number one million (1,000,000) in an `int`.

### Debugging Java memory (big endian)

When I do a hexdump of the variable in Java, I get the following hex:
```
0F 42 40
```

Since we know Java uses big endian, we want to pay attention to the "big endian" line.
```
$ python3 debug.py -i "0F 42 40"
Little endian decimal unsigned: 4211215
Big endian decimal unsigned:    1000000 <----
```

### Debugging C memory (little endian)

When we do a hexdump of the variable in C, we get the following hex:
```
40 42 0F
```

Since I'm on a system that uses little endian, we want to pay attention to the "little endian" line.
```
$ python3 debug.py -i "40 42 0F"
Little endian decimal unsigned: 1000000 <-----
Big endian decimal unsigned:    4211215
```
