# Struct C Preprocessor

Creates structs using the c preprocessor. `make`

```c
CREATE_STRUCT(my_struct1, int age, char name[64]);

// outputs to 

struct my_struct1 {
  int age;
  char name[64];
};
```

Originally copied and changed from "https://stackoverflow.com/questions/50017806/variadic-macro-to-create-struct"
I created `gen_struct.py` to generate the preprocessor macros for given `N` members length.

Created because I rewrite this every 4 months.