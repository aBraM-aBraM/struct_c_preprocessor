#define CONCATENATE(arg1, arg2)   CONCATENATE1(arg1, arg2)
#define CONCATENATE1(arg1, arg2)  CONCATENATE2(arg1, arg2)
#define CONCATENATE2(arg1, arg2)  arg1##arg2

#define FOR_EACH_1(what, x) what(x);

import sys

def gen_struct(max_len):
     out = ["#define CONCATENATE(arg1, arg2)   CONCATENATE1(arg1, arg2)",
            "#define CONCATENATE1(arg1, arg2)  CONCATENATE2(arg1, arg2)",
            "#define CONCATENATE2(arg1, arg2)  arg1##arg2",
             "#define FOR_EACH_1(what, x) what(x);"]
     for i in range(2, max_len):
         out += [f"#define FOR_EACH_{i}(what, x, ...)\\",
                 "\twhat(x);\\",
                 f"\tFOR_EACH_{i-1}(what,  __VA_ARGS__)"]
        
     out += ["#define FOR_EACH_NARG(...) FOR_EACH_NARG_(__VA_ARGS__, FOR_EACH_RSEQ_N())",
             "#define FOR_EACH_NARG_(...) FOR_EACH_ARG_N(__VA_ARGS__)"]
     out += [f"#define FOR_EACH_ARG_N({', '.join([f'_{i}' for i in range(max_len)])}, N, ...) N"]
     out += [f"#define FOR_EACH_RSEQ_N() {', '.join([f'{max_len - i}' for i in range(max_len)])}"]
     out += ["#define FOR_EACH_(N, what, ...) CONCATENATE(FOR_EACH_, N)(what, __VA_ARGS__)",
             "#define FOR_EACH(what, ...) FOR_EACH_(FOR_EACH_NARG(__VA_ARGS__), what, __VA_ARGS__)",
             "#define DO_NOTHING(x) x",
             "#define CREATE_STRUCT(name, ...) struct name { FOR_EACH(DO_NOTHING, __VA_ARGS__) }"]
     print("\n".join(out))

if __name__ == "__main__":
     if len(sys.argv) == 1:
          gen_struct(25)
     else:
          gen_struct(int(sys.argv[1]))