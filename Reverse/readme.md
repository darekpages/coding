# reverse-txt-file.py

Sometimes, when doing some coding tasks, it happens that you get a text file whose line layout is reversed. If it contains a few lines, you can reverse them manually. But when it contains a few hundred lines or more, the problem begins.

For example, I have a file:
```
line 50
...
line 2
line 1
```
the resulting file, with reversed lines, will look like this:

```
line 1
line 2
...
line 50
```

This minimalist script reverses such a file in the blink of an eye. In the console, the command:

> python reverse-txt-file.py source_file.txt result_file.txt

or simply:

> reverse-txt-file.py source_file.txt result_file.txt

Below, the illustration shows the effect of running the script:

![view-console](https://github.com/user-attachments/assets/22f2dd3c-3af9-4393-a71c-26542ef9cc46)

If there are no arguments, the appropriate information will be displayed, with other errors, system errors will be displayed or it will look like everything has blown up. This is what minimalism is all about, minimum error handling. You just have to **remember to provide the correct arguments**.

The script is best placed in a directory with scripts shared by the system and python.

I think this script can be the basis for a tool for processing text files, meaning everything with a text structure, without breaking it down into separate scripts. And I often deal with files where manual work doesnt amuse me.
