# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла

import os

def log(text, file="log.txt"):
    my_file = open(file, "a")
    my_file.write(text)
    my_file.close()


log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt
