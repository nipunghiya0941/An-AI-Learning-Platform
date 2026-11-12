from django.core.management.base import BaseCommand
from core.models import Course, LevelModule
import json

class Command(BaseCommand):
    help = "Seeds C, Java, and Python courses with 20 gamified levels each"

    def handle(self, *args, **options):
        self.stdout.write("Starting course seeding...")

        # 1. C Course
        c_course, _ = Course.objects.update_or_create(
            slug='c',
            defaults={
                'name': 'C Programming',
                'tagline': 'Master low-level systems, direct memory control, pointers & raw machine performance.',
                'description': 'Known as the mother of all modern languages, C gives you raw power over silicon and memory. Journey from your first compile command to dynamic memory management, pointer arithmetic, and building your own custom high-speed data structures.',
                'badge_label': '20 Levels Available',
                'status': 'available',
                'icon_type': 'c',
                'color_accent': '#00f2fe',
                'order': 1
            }
        )

        # 2. Java Course
        java_course, _ = Course.objects.update_or_create(
            slug='java',
            defaults={
                'name': 'Java Programming',
                'tagline': 'Build bulletproof enterprise systems, scalable OOP architectures & cloud platforms.',
                'description': 'Powering billions of mission-critical devices and global enterprise backends, Java is the king of Object-Oriented design. Conquer the JVM, deep inheritance hierarchies, collections, streams, multi-threading, and robust error architecture.',
                'badge_label': '20 Levels Available',
                'status': 'available',
                'icon_type': 'java',
                'color_accent': '#f59e0b',
                'order': 2
            }
        )

        # 3. Python Course (Upcoming)
        python_course, _ = Course.objects.update_or_create(
            slug='python',
            defaults={
                'name': 'Python Programming',
                'tagline': 'The language of Artificial Intelligence, Data Science, Machine Learning & Automation.',
                'description': 'Prepare for the upcoming journey into Python! From clean syntactic elegance and data wrangling to building neural networks, APIs, and autonomous AI agents. Currently in rapid curriculum development by our engineer instructors.',
                'badge_label': 'Upcoming Track',
                'status': 'upcoming',
                'icon_type': 'python',
                'color_accent': '#10b981',
                'order': 3
            }
        )

        # Seed C Modules (20 Levels)
        c_modules_data = [
            (
                1,
                "Genesis of C: The Compilation Pipeline",
                "Learn the origins of C, how source code compiles to machine bytecode, and write your first program.",
                "Novice",
                100,
                """C was created by Dennis Ritchie at Bell Labs between 1972 and 1973. It is a compiled, statically typed language that operates very close to computer hardware.

### The 4 Stages of Compilation
1. **Preprocessing (`cpp`)**: Evaluates directives starting with `#` like `#include` and `#define`.
2. **Compilation (`gcc -S`)**: Translates preprocessed C code into assembly instructions.
3. **Assembly (`as`)**: Translates assembly instructions into machine code (object file `.o`).
4. **Linking (`ld`)**: Combines object files and system libraries into an executable binary.

Every C program execution begins at the `main()` entrypoint function.""",
                """#include <stdio.h>

int main(void) {
    // Prints message to standard output
    printf("Welcome to Quest AI - Level 1 Initialized!\\n");
    return 0; // 0 indicates successful termination
}""",
                "Hello World with Return Code",
                "Write a minimal C program that prints 'Quest C Activated' and safely returns 0.",
                """#include <stdio.h>

int main() {
    // TODO: Write printf statement here
    
    return 0;
}""",
                "Quest C Activated",
                "Use printf with double quotes and include a newline character \\n.",
                "Which stage of the C build process handles #include <stdio.h> directives?",
                ["Pre-processing stage", "Assembly compilation stage", "Linker resolution stage", "Runtime execution stage"],
                0,
                "The C preprocessor runs first and replaces #include directives with the actual contents of the header files before syntax parsing."
            ),
            (
                2,
                "Data Types, Variables & Format Specifiers",
                "Master primitive types, memory allocations, signedness, and standard format specifiers.",
                "Novice",
                100,
                """In C, variables must be explicitly declared before use. Every type consumes a fixed amount of memory determined by the CPU architecture.

### Common Primitive Types
- `char`: 1 byte ($-128$ to $127$ or $0$ to $255$)
- `int`: 4 bytes on modern 32/64-bit systems
- `float`: 4 bytes single-precision IEEE 754
- `double`: 8 bytes double-precision IEEE 754

### Format Specifiers
- `%d` or `%i`: signed integer
- `%u`: unsigned integer
- `%f`: float / double
- `%c`: single character
- `%s`: null-terminated string
- `%p`: memory address pointer""",
                """#include <stdio.h>

int main() {
    int player_level = 5;
    float xp_multiplier = 1.75f;
    char rank_grade = 'S';

    printf("Level: %d | Multiplier: %.2f | Grade: %c\\n", 
           player_level, xp_multiplier, rank_grade);
    return 0;
}""",
                "Variable Declaration & Specifier Display",
                "Declare an integer variable 'mana' with 250 and display it using printf format specifiers.",
                """#include <stdio.h>

int main() {
    // Declare mana = 250
    // Print: Mana: 250
    return 0;
}""",
                "Mana: 250",
                "Declare `int mana = 250;` and use `printf(\"Mana: %d\\n\", mana);`.",
                "What is the standard format specifier used to print a single precision floating point number in C?",
                ["%f", "%d", "%c", "%s"],
                0,
                "%f is the standard format specifier for floating point variables in printf."
            ),
            (
                3,
                "Operators, Expressions & Bitwise Logic",
                "Harness arithmetic, relational, logical, and low-level bitwise bit-shift operators.",
                "Novice",
                100,
                """C gives engineers direct access to CPU arithmetic logic units (ALU).

### Operator Families
- **Arithmetic**: `+`, `-`, `*`, `/`, `%` (modulo)
- **Relational**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical**: `&&` (short-circuit AND), `||` (short-circuit OR), `!` (NOT)
- **Bitwise**: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (shift left), `>>` (shift right)

Bitwise shifts allow lightning-fast multiplication and division by powers of 2: `x << 1` equals `x * 2`.""",
                """#include <stdio.h>

int main() {
    unsigned char flags = 0b00000101; // Flags 1 and 4 set
    // Toggle 2nd bit using XOR
    flags ^= 0b00000010;

    printf("Flags binary decimal value: %u\\n", flags);
    return 0;
}""",
                "Bitwise Left Shift Optimization",
                "Multiply the integer 16 by 4 using the bitwise left-shift operator.",
                """#include <stdio.h>

int main() {
    int val = 16;
    // Shift left by 2 positions (16 * 4)
    int result = val << 2;
    printf("Result: %d\\n", result);
    return 0;
}""",
                "Result: 64",
                "Left shifting by 2 bits multiplies an integer by 2^2 = 4.",
                "What is the result of 8 >> 1 in C?",
                ["4", "16", "2", "8"],
                0,
                "Right shifting by 1 divides the number by 2^1 = 2. 8 / 2 is 4."
            ),
            (
                4,
                "Control Flow: Decisions with if, else & switch",
                "Direct the execution path of your software through branching and jump tables.",
                "Novice",
                100,
                """Branching allows programs to make intelligent decisions based on runtime values.

### The if-else Ladder
Evaluates conditions sequentially from top to bottom until one resolves to true (non-zero).

### The switch-case Construct
Compiles down to an efficient hardware jump-table when checking integral constants. Remember the `break` statement to prevent unintended fall-through!""",
                """#include <stdio.h>

int main() {
    int choice = 2;
    switch(choice) {
        case 1:
            printf("Warrior Selected\\n");
            break;
        case 2:
            printf("Mage Selected\\n");
            break;
        default:
            printf("Rogue Selected\\n");
            break;
    }
    return 0;
}""",
                "Decision Gatekeeper",
                "Write an if-else check that prints 'Access Granted' if health > 0 else 'Game Over'.",
                """#include <stdio.h>

int main() {
    int health = 100;
    if (health > 0) {
        printf("Access Granted\\n");
    } else {
        printf("Game Over\\n");
    }
    return 0;
}""",
                "Access Granted",
                "Use `if (health > 0) { ... } else { ... }`.",
                "What happens in a C switch block if the 'break' statement is omitted from a matched case?",
                ["Execution falls through into the subsequent case statements", "A compilation syntax error is raised", "The program aborts immediately", "The switch restarts from the top"],
                0,
                "Without break, C executes the matching case and falls through to execute subsequent case bodies regardless of their conditions."
            ),
            (
                5,
                "Loops of Eternity: for, while & do-while",
                "Automate repetitive tasks, traverse bounds, and control loops with break and continue.",
                "Novice",
                100,
                """Loops repeat a block of code as long as a loop condition holds true.

### Loop Types
1. **`for (init; condition; step)`**: Best when the number of iterations is known upfront.
2. **`while (condition)`**: Evaluates condition before executing loop body (pre-test).
3. **`do { ... } while (condition);`**: Executes body at least once before testing condition (post-test).

Use `break` to exit early, and `continue` to skip remaining statements in the current iteration.""",
                """#include <stdio.h>

int main() {
    for (int i = 1; i <= 5; i++) {
        if (i == 3) continue; // Skip 3
        printf("Iteration %d\\n", i);
    }
    return 0;
}""",
                "Countdown Sequence",
                "Write a while loop counting down from 3 down to 1, printing each number.",
                """#include <stdio.h>

int main() {
    int count = 3;
    while(count > 0) {
        printf("%d\\n", count);
        count--;
    }
    return 0;
}""",
                "3\n2\n1",
                "Initialize count = 3, decrement count in the while loop.",
                "Which loop in C guarantees that its body will execute at least once?",
                ["do-while loop", "for loop", "while loop", "nested loop"],
                0,
                "A do-while loop evaluates its conditional expression at the bottom of the loop body."
            ),
            (
                6,
                "Modular Functions, Prototypes & Stack Frames",
                "Structure clean, reusable modules and understand CPU call stacks.",
                "Apprentice",
                120,
                """Functions modularize logic into isolated, testable units.

### Function Declarations (Prototypes)
Allows the compiler to verify parameter types and return types before the actual implementation is encountered.

### Stack Frames
Each function call pushes an activation record onto the call stack containing parameters, local variables, and the return instruction pointer.""",
                """#include <stdio.h>

// Function prototype
int calculate_xp(int monsters, int multiplier);

int main() {
    int total = calculate_xp(5, 50);
    printf("Total XP Earned: %d\\n", total);
    return 0;
}

int calculate_xp(int monsters, int multiplier) {
    return monsters * multiplier;
}""",
                "Square Calculator Function",
                "Write a function `square(int n)` that returns `n * n` and call it with 7.",
                """#include <stdio.h>

int square(int n) {
    return n * n;
}

int main() {
    printf("Square: %d\\n", square(7));
    return 0;
}""",
                "Square: 49",
                "Define the function with integer parameter and return `n * n`.",
                "Why are function prototypes recommended at the top of C source files?",
                ["They inform the compiler of function signature before its actual definition", "They allocate heap memory for the function", "They are strictly required to avoid linker crashes", "They speed up machine code execution by 50%"],
                0,
                "Prototypes declare the return type and parameter types so the compiler can validate calls made prior to definition."
            ),
            (
                7,
                "Array Foundations: Contiguous Memory Layout",
                "Manipulate indexed sequences stored contiguously in system RAM.",
                "Apprentice",
                120,
                """An array is a fixed-size sequence of elements of the same type stored in consecutive memory bytes.

### Key Rules
- 0-indexed: First element is at index `0`, last element is at `size - 1`.
- Bound safety: C does NOT perform runtime bounds checking! Accessing `arr[10]` on a 5-element array leads to undefined behavior.
- Memory calculation: `Address of arr[i] = BaseAddress + (i * sizeof(Type))`.""",
                """#include <stdio.h>

int main() {
    int scores[4] = {95, 88, 72, 100};
    for (int i = 0; i < 4; i++) {
        printf("Index %d holds %d\\n", i, scores[i]);
    }
    return 0;
}""",
                "Array Summation",
                "Sum the elements of an array `{10, 20, 30}` and print the result.",
                """#include <stdio.h>

int main() {
    int nums[3] = {10, 20, 30};
    int sum = 0;
    for(int i = 0; i < 3; i++) {
        sum += nums[i];
    }
    printf("Total: %d\\n", sum);
    return 0;
}""",
                "Total: 60",
                "Iterate from index 0 to 2 and add each element to sum.",
                "If an integer occupies 4 bytes and array starts at memory address 1000, what is the address of array[3]?",
                ["1012", "1003", "1008", "1016"],
                0,
                "Base (1000) + 3 * sizeof(int) (4) = 1000 + 12 = 1012."
            ),
            (
                8,
                "Matrix Dimensions: 2D Arrays & Nested Logic",
                "Build grids, matrices, coordinate game boards, and image buffers.",
                "Apprentice",
                120,
                """A two-dimensional array in C is an array of arrays, laid out in memory in **row-major order**.

`int grid[ROWS][COLS];`
Elements in row 0 are followed immediately in memory by row 1, then row 2.""",
                """#include <stdio.h>

int main() {
    int matrix[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    };

    for(int r = 0; r < 2; r++) {
        for(int c = 0; c < 3; c++) {
            printf("%d ", matrix[r][c]);
        }
        printf("\\n");
    }
    return 0;
}""",
                "Diagonal Matrix Value",
                "Access and print the diagonal element at row 1, col 1 of a 2x2 grid.",
                """#include <stdio.h>

int main() {
    int grid[2][2] = {{10, 20}, {30, 40}};
    printf("Diagonal: %d\\n", grid[1][1]);
    return 0;
}""",
                "Diagonal: 40",
                "Row 1, column 1 corresponds to `grid[1][1]` which is 40.",
                "In what memory arrangement does C store 2D arrays?",
                ["Row-major order", "Column-major order", "Linked pointer table", "Scattered page blocks"],
                0,
                "C stores multi-dimensional arrays row by row consecutively in memory (row-major order)."
            ),
            (
                9,
                "String Alchemy: Character Arrays & string.h",
                "Manipulate text using null-terminated strings and standard string library routines.",
                "Apprentice",
                120,
                """In C, there is no native primitive `string` type. A string is an array of characters terminated by a null byte (`'\\0'`, ASCII 0).

### Key Functions from `<string.h>`
- `strlen(s)`: Returns length of string excluding the null terminator.
- `strcpy(dest, src)`: Copies source string into destination buffer.
- `strcmp(s1, s2)`: Compares strings lexicographically ($0$ if identical).
- `strcat(dest, src)`: Concatenates source to end of destination.""",
                """#include <stdio.h>
#include <string.h>

int main() {
    char greeting[20] = "Quest";
    strcat(greeting, " AI");
    printf("%s (Length: %zu)\\n", greeting, strlen(greeting));
    return 0;
}""",
                "String Length Inspection",
                "Find and print the length of the string 'Developer'.",
                """#include <stdio.h>
#include <string.h>

int main() {
    char word[] = "Developer";
    printf("Length: %zu\\n", strlen(word));
    return 0;
}""",
                "Length: 9",
                "Use `strlen(word)` to compute the character count.",
                "What character marks the end of every valid C string?",
                ["'\\0' (null character)", "'\\n' (newline character)", "';' (semicolon)", "' ' (whitespace)"],
                0,
                "A null terminator '\\0' (ASCII zero) tells functions like printf where the string data ends in memory."
            ),
            (
                10,
                "Pointer Initiation: Addresses & Dereferencing",
                "Conquer C's ultimate power: direct memory pointer variables.",
                "Apprentice",
                140,
                """A pointer is a variable whose value is the memory address of another variable.

### Essential Operators
1. Address-of (`&`): Retrieves the physical memory address of a variable.
2. Dereference (`*`): Accesses or modifies the value residing at the address stored in the pointer.

Understanding pointers is the foundation of dynamic data structures, high-performance C, and operating system kernels.""",
                """#include <stdio.h>

int main() {
    int power = 9000;
    int *ptr = &power; // ptr stores address of power

    printf("Value: %d\\n", *ptr); // dereference to read value
    *ptr = 9001; // modify value through pointer
    printf("Updated Power: %d\\n", power);
    return 0;
}""",
                "Pointer Value Swap",
                "Create a pointer to an int variable and change its value to 42 using dereferencing.",
                """#include <stdio.h>

int main() {
    int target = 10;
    int *p = &target;
    *p = 42;
    printf("Target: %d\\n", target);
    return 0;
}""",
                "Target: 42",
                "Assign `*p = 42;` to alter the target variable.",
                "What does the unary '&' operator return when applied to a variable?",
                ["The memory address of the variable", "The value stored inside the variable", "The size in bytes of the variable", "A bitwise negation of the variable"],
                0,
                "The address-of operator '&' returns the memory address where the operand variable is stored."
            ),
            (
                11,
                "Pointer Arithmetic & Array Equivalence",
                "Traverse memory buffers using pointer increments and pointer math.",
                "Adept",
                150,
                """In C, array names decay to a pointer to their first element!

`arr[i]` is syntactically equivalent to `*(arr + i)`.

When you add `1` to an `int *` pointer, the address increments by `sizeof(int)` (typically 4 bytes), not 1 byte! The compiler automatically scales arithmetic by the pointee's byte size.""",
                """#include <stdio.h>

int main() {
    int numbers[] = {100, 200, 300};
    int *p = numbers;

    printf("First: %d\\n", *p);
    p++; // Points to next int
    printf("Second: %d\\n", *p);
    return 0;
}""",
                "Pointer Array Traversal",
                "Print the third element of `{5, 10, 15, 20}` using pointer offset `*(arr + 2)`.",
                """#include <stdio.h>

int main() {
    int vals[4] = {5, 10, 15, 20};
    printf("Element: %d\\n", *(vals + 2));
    return 0;
}""",
                "Element: 15",
                "*(vals + 2) points to index 2 (the 3rd element).",
                "If 'ptr' is a pointer to an int at address 2000, what is the address of 'ptr + 2' on a 32-bit system?",
                ["2008", "2002", "2004", "2016"],
                0,
                "Each int is 4 bytes. Pointer addition increments by 2 * 4 = 8 bytes. 2000 + 8 = 2008."
            ),
            (
                12,
                "Structures (struct): Custom Data Modeling",
                "Group related heterogeneous variables into custom records.",
                "Adept",
                150,
                """A `struct` allows you to model real-world composite entities.

### Accessing Members
- Dot operator (`.`): Used when accessing fields from a direct struct variable.
- Arrow operator (`->`): Used when accessing fields through a pointer to a struct (`ptr->member` is shorthand for `(*ptr).member`).""",
                """#include <stdio.h>

struct Hero {
    char name[20];
    int hp;
    float attack;
};

int main() {
    struct Hero h1 = {"Knight", 500, 45.5f};
    struct Hero *hptr = &h1;

    printf("Hero %s has %d HP\\n", hptr->name, hptr->hp);
    return 0;
}""",
                "Struct Member Assignment",
                "Define a struct Point with x and y, and print their coordinates.",
                """#include <stdio.h>

struct Point {
    int x;
    int y;
};

int main() {
    struct Point p = {12, 24};
    printf("Point at (%d, %d)\\n", p.x, p.y);
    return 0;
}""",
                "Point at (12, 24)",
                "Define the struct with int x and int y, then instantiate and print.",
                "Which operator is used to access a struct member through a pointer to that struct?",
                ["-> (Arrow operator)", ". (Dot operator)", ":: (Scope operator)", "* (Star operator)"],
                0,
                "The arrow operator '->' dereferences the struct pointer and selects the specified field."
            ),
            (
                13,
                "Unions & Bit Fields: Memory Optimization",
                "Share single memory locations across types and pack bit flags.",
                "Adept",
                150,
                """### Unions
A `union` allocates only enough memory to hold its largest member. All members share the exact same starting memory address.

### Bit Fields
Allow packing multiple booleans or small integer values into exact bit widths within an integer, crucial for network packet headers and embedded microcontrollers.""",
                """#include <stdio.h>

union DataPacket {
    int int_val;
    float float_val;
    char char_val;
};

int main() {
    union DataPacket packet;
    packet.int_val = 65;
    printf("As int: %d | As char: %c\\n", packet.int_val, packet.char_val);
    return 0;
}""",
                "Union Memory Size Inspection",
                "Check the size of a union containing a char and a double.",
                """#include <stdio.h>

union Test {
    char c;
    double d;
};

int main() {
    printf("Size: %zu bytes\\n", sizeof(union Test));
    return 0;
}""",
                "Size: 8 bytes",
                "The union allocates space equal to its largest member, double (8 bytes).",
                "How much memory does a union occupy in C?",
                ["Space equal to its largest member", "The sum of all its members' sizes", "Always 4 bytes", "Dynamic heap storage"],
                0,
                "A union overlays all members over the same memory location, taking the size of the largest constituent member."
            ),
            (
                14,
                "Dynamic Memory: malloc, calloc, realloc & free",
                "Allocate and release memory on the Heap during program runtime.",
                "Adept",
                180,
                """Variables defined in functions reside on the temporary Stack. To allocate memory whose lifetime extends beyond function scopes, we request memory from the Heap using `<stdlib.h>`.

- `malloc(size)`: Allocates uninitialized heap memory.
- `calloc(n, size)`: Allocates and zeros out memory.
- `realloc(ptr, new_size)`: Resizes an existing heap allocation.
- `free(ptr)`: Releases heap memory back to the operating system.""",
                """#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = (int *)malloc(3 * sizeof(int));
    if (arr == NULL) return 1; // Always check allocation success!

    arr[0] = 10; arr[1] = 20; arr[2] = 30;
    printf("Dynamically allocated: %d\\n", arr[1]);

    free(arr); // Crucial to prevent leaks!
    arr = NULL; // Prevent dangling pointer
    return 0;
}""",
                "Heap Array Allocation",
                "Allocate memory for one integer using malloc, set it to 100, print it, and free it.",
                """#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p = (int *)malloc(sizeof(int));
    *p = 100;
    printf("Val: %d\\n", *p);
    free(p);
    return 0;
}""",
                "Val: 100",
                "Use `malloc(sizeof(int))`, assign `*p = 100`, then call `free(p)`.",
                "What value does malloc return if the operating system runs out of memory?",
                ["NULL", "-1", "0x00000001", "Throws an OutOfMemory exception"],
                0,
                "malloc returns a NULL pointer when the heap allocator is unable to fulfill the requested byte size."
            ),
            (
                15,
                "Memory Debugging: Leaks & Dangling Pointers",
                "Master safe pointer practices, avoid use-after-free, and audit buffers.",
                "Adept",
                180,
                """### Critical Memory Pitfalls
1. **Memory Leak**: Allocating heap memory without corresponding `free()`.
2. **Dangling Pointer**: Continuing to read or write a pointer after the memory it pointed to has been freed.
3. **Double Free**: Calling `free()` twice on the same memory block, causing heap corruption.
4. **Buffer Overflow**: Writing past the allocated byte boundary.""",
                """#include <stdio.h>
#include <stdlib.h>

void safe_cleanup(int **ptr) {
    if (ptr && *ptr) {
        free(*ptr);
        *ptr = NULL; // Eliminates dangling pointer!
    }
}

int main() {
    int *num = (int *)malloc(sizeof(int));
    *num = 777;
    safe_cleanup(&num);
    printf("Safely cleaned up pointer!\\n");
    return 0;
}""",
                "Safe Pointer Nullification",
                "Demonstrate setting a pointer to NULL after freeing it to avoid dangling states.",
                """#include <stdio.h>
#include <stdlib.h>

int main() {
    char *buf = malloc(10);
    free(buf);
    buf = NULL;
    printf("Safe state: %s\\n", buf == NULL ? "NULL" : "DANGLING");
    return 0;
}""",
                "Safe state: NULL",
                "After calling free(buf), explicitly write `buf = NULL;`.",
                "What is a 'dangling pointer' in C?",
                ["A pointer pointing to memory that has already been deallocated", "A pointer that has never been initialized", "A pointer that points to another pointer", "A pointer that holds address zero"],
                0,
                "A dangling pointer points to invalid/freed memory whose allocation has already been released."
            ),
            (
                16,
                "File Handling: Streams, fopen, fread & fwrite",
                "Persist data to disk and process binary and text streams.",
                "Adept",
                180,
                """In C, files are accessed through buffered streams represented by `FILE *` pointers.

### Standard Modes
- `"r"`: Read existing text file.
- `"w"`: Create or truncate text file for writing.
- `"a"`: Append to end of file.
- `"rb"` / `"wb"`: Binary read and write modes.""",
                """#include <stdio.h>

int main() {
    FILE *fp = fopen("quest_log.txt", "w");
    if (fp != NULL) {
        fprintf(fp, "Level 16 Logged: Success\\n");
        fclose(fp);
        printf("File written successfully.\\n");
    }
    return 0;
}""",
                "File Writing Demonstration",
                "Write a short program showing fopen with 'w' mode and fclose.",
                """#include <stdio.h>

int main() {
    FILE *f = fopen("test.txt", "w");
    if(f) {
        fputs("Quest Data", f);
        fclose(f);
        printf("Written\\n");
    }
    return 0;
}""",
                "Written",
                "Open file with fopen('test.txt', 'w'), fputs data, and fclose(f).",
                "Which C library function must always be invoked to flush buffers and close an open file stream?",
                ["fclose()", "fcloseall()", "fflush_exit()", "free()"],
                0,
                "fclose() flushes any unwritten buffered data to the operating system and closes the file descriptor."
            ),
            (
                17,
                "Preprocessor Directives & Header Guards",
                "Harness `#define`, conditional compilation `#ifdef`, and modular headers.",
                "Master",
                200,
                """The C preprocessor modifies text before semantic analysis begins.

### Header Guards
Prevents double-inclusion errors when multiple files `#include` the same header:
```c
#ifndef MY_HEADER_H
#define MY_HEADER_H

// Declarations here

#endif
```

Macros like `#define MAX(a,b) ((a) > (b) ? (a) : (b))` execute inline without function call overhead.""",
                """#include <stdio.h>

#define MAX_USERS 100
#define SQUARE(x) ((x) * (x))

int main() {
    printf("Max: %d | Square of 6: %d\\n", MAX_USERS, SQUARE(6));
    return 0;
}""",
                "Macro Definition & Usage",
                "Define a preprocessor macro PI as 3.1415 and print it.",
                """#include <stdio.h>

#define PI 3.1415

int main() {
    printf("PI: %.4f\\n", PI);
    return 0;
}""",
                "PI: 3.1415",
                "Use `#define PI 3.1415` and print with format specifier `%.4f`.",
                "What is the primary purpose of header guards (#ifndef ... #define ... #endif)?",
                ["Prevent duplicate type definitions and re-inclusion of the same header", "Encrypt the header source code", "Speed up runtime CPU clock cycles", "Automatically allocate memory for functions"],
                0,
                "Header guards prevent multiple inclusions of the same header file during compilation."
            ),
            (
                18,
                "Function Pointers & Callback Architectures",
                "Pass executable code as arguments to design event handlers and sorting callbacks.",
                "Master",
                200,
                """A function pointer stores the starting memory address of executable machine instructions in the code segment.

### Syntax
`return_type (*func_ptr_name)(param_types);`

This is the exact mechanism used by `qsort()` in the standard C library to sort arbitrary data structures.""",
                """#include <stdio.h>

int add(int a, int b) { return a + b; }
int multiply(int a, int b) { return a * b; }

// Accepts a function pointer callback
void compute(int x, int y, int (*operation)(int, int)) {
    printf("Computed Result: %d\\n", operation(x, y));
}

int main() {
    compute(6, 7, multiply);
    return 0;
}""",
                "Function Pointer Call",
                "Declare a function pointer to an int function taking one int and invoke it.",
                """#include <stdio.h>

int double_val(int n) { return n * 2; }

int main() {
    int (*fp)(int) = double_val;
    printf("Result: %d\\n", fp(21));
    return 0;
}""",
                "Result: 42",
                "Declare `int (*fp)(int) = double_val;` and call `fp(21)`.",
                "Which standard C library function utilizes function pointers to customize comparison logic?",
                ["qsort()", "malloc()", "memcpy()", "printf()"],
                0,
                "qsort() takes a comparator function pointer to determine the ordering of elements."
            ),
            (
                19,
                "Data Structures: Singly & Doubly Linked Lists",
                "Construct non-contiguous dynamic node graphs with pointers.",
                "Master",
                220,
                """Unlike static arrays, linked lists can grow and shrink dynamically without memory reallocation.

### Node Structure
```c
struct Node {
    int data;
    struct Node *next;
};
```
Each node is dynamically allocated on the heap, pointing to the next node in sequence. Insertion at the head is $O(1)$ constant time.""",
                """#include <stdio.h>
#include <stdlib.h>

struct Node {
    int val;
    struct Node *next;
};

int main() {
    struct Node *head = malloc(sizeof(struct Node));
    head->val = 101;
    head->next = malloc(sizeof(struct Node));
    head->next->val = 102;
    head->next->next = NULL;

    printf("Head: %d -> Next: %d\\n", head->val, head->next->val);

    free(head->next);
    free(head);
    return 0;
}""",
                "Linked List Node Creation",
                "Instantiate a single linked list node with value 99 on the heap and print it.",
                """#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

int main() {
    struct Node *n = malloc(sizeof(struct Node));
    n->data = 99;
    n->next = NULL;
    printf("Node data: %d\\n", n->data);
    free(n);
    return 0;
}""",
                "Node data: 99",
                "Allocate node with malloc, assign data, and free before exit.",
                "What is the time complexity to insert a new node at the head of a singly linked list?",
                ["O(1) constant time", "O(N) linear time", "O(log N) logarithmic time", "O(N^2) quadratic time"],
                0,
                "Inserting at the head simply updates the new node's next pointer and head pointer, taking constant O(1) time."
            ),
            (
                20,
                "Grandmaster Capstone: In-Memory Key-Value Store",
                "Synthesize all 19 modules into a high-speed memory-managed C engine.",
                "Master",
                250,
                """Congratulations on reaching the final Level 20 of C Programming!

Here, you synthesize structs, dynamic memory, pointer arithmetic, hashing, and file persistence to build an in-memory Key-Value store with collision handling.

You have mastered the foundational language that powers Linux, Git, Python's CPython runtime, and high-frequency trading engines!""",
                """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 16

typedef struct Entry {
    char key[32];
    int value;
    struct Entry *next;
} Entry;

typedef struct {
    Entry *buckets[TABLE_SIZE];
} HashTable;

unsigned int hash(const char *key) {
    unsigned int h = 0;
    while (*key) h = (h << 5) + *key++;
    return h % TABLE_SIZE;
}

int main() {
    printf("Master Capstone: C In-Memory Database Engine Initialized!\\n");
    return 0;
}""",
                "Grandmaster C Certification",
                "Execute the final capstone verification displaying 'C Master Completed'.",
                """#include <stdio.h>

int main() {
    printf("C Master Completed\\n");
    return 0;
}""",
                "C Master Completed",
                "Print the capstone completion message.",
                "What major runtime system is primarily implemented in C?",
                ["The Linux Kernel and CPython", "The JVM Bytecode compiler only", "The Android UI Layout Engine", "The CSS Rendering engine only"],
                0,
                "The Linux operating system kernel, Git, SQLite, and the standard CPython interpreter are written in C."
            ),
        ]

        # Seed Java Modules (20 Levels)
        java_modules_data = [
            (
                1,
                "The JVM Ecosystem & Bytecode Architecture",
                "Understand the JDK, JRE, Bytecode, Just-In-Time (JIT) compiler, and the JVM.",
                "Novice",
                100,
                """Java's foundational principle is 'Write Once, Run Anywhere' (WORA).

### How Java Runs
1. **Source Code (`.java`)**: Human-readable Java code.
2. **Bytecode (`.class`)**: Compiled by `javac` into universal virtual machine instructions.
3. **Java Virtual Machine (JVM)**: Interprets and JIT-compiles bytecode into native CPU machine instructions at runtime.

The JVM manages memory automatically through garbage collection (GC).""",
                """public class Main {
    public static void main(String[] args) {
        System.out.println("Welcome to Quest AI - Java Track Level 1 Initialized!");
    }
}""",
                "First Java Program",
                "Create a class named Main with a main method that prints 'Quest Java Ready'.",
                """public class Main {
    public static void main(String[] args) {
        // TODO: Print Quest Java Ready
    }
}""",
                "Quest Java Ready",
                "Use `System.out.println(\"Quest Java Ready\");` inside main.",
                "What is the output file format generated by the Java compiler (javac)?",
                [".class bytecode file", ".exe native executable", ".obj object file", ".dll dynamic link library"],
                0,
                "javac compiles .java source files into .class files containing intermediate Java bytecode."
            ),
            (
                2,
                "Variables, Primitive Types & Type Casting",
                "Explore the 8 Java primitive types, reference variables, and implicit vs explicit casting.",
                "Novice",
                100,
                """Java is a strongly typed language with 8 primitives:
- Integral: `byte` (8-bit), `short` (16-bit), `int` (32-bit), `long` (64-bit)
- Floating: `float` (32-bit), `double` (64-bit)
- Logical: `boolean` (`true` / `false`)
- Character: `char` (16-bit Unicode UTF-16)

### Type Casting
- **Widening (Implicit)**: `int` to `double` (no data loss)
- **Narrowing (Explicit)**: `(int) 9.99` truncates decimal to `9`.""",
                """public class Main {
    public static void main(String[] args) {
        int initialScore = 150;
        double multiplier = 1.5;
        double finalScore = initialScore * multiplier;

        System.out.println("Final Score: " + finalScore);
    }
}""",
                "Explicit Narrowing Cast",
                "Cast a double 45.78 to an integer and print the truncated value.",
                """public class Main {
    public static void main(String[] args) {
        double preciseVal = 45.78;
        int truncated = (int) preciseVal;
        System.out.println("Value: " + truncated);
    }
}""",
                "Value: 45",
                "Use `(int) preciseVal` to perform an explicit narrowing cast.",
                "How many primitive data types exist in Java?",
                ["8", "4", "16", "32"],
                0,
                "Java has 8 primitive types: byte, short, int, long, float, double, boolean, and char."
            ),
            (
                3,
                "Operators, Math Class & Scanner Terminal Input",
                "Perform math calculations and read user input from System.in via Scanner.",
                "Novice",
                100,
                """Java provides standard operators and the `java.lang.Math` utility class for advanced calculations like `Math.sqrt()`, `Math.pow()`, and `Math.max()`.

To read interactive console input from the user, Java provides `java.util.Scanner`.""",
                """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int a = 25;
        int b = 40;
        int maximum = Math.max(a, b);
        System.out.println("Maximum: " + maximum);
    }
}""",
                "Math Maximum Calculation",
                "Use Math.max to find the larger of 88 and 102 and print the result.",
                """public class Main {
    public static void main(String[] args) {
        int result = Math.max(88, 102);
        System.out.println("Max: " + result);
    }
}""",
                "Max: 102",
                "Call `Math.max(88, 102)` and print it.",
                "Which package contains the Scanner class for reading terminal input?",
                ["java.util", "java.lang", "java.io", "java.system"],
                0,
                "Scanner belongs to the java.util package and must be imported via `import java.util.Scanner;`."
            ),
            (
                4,
                "Branching Logic: if-else & Modern Switch Expressions",
                "Route program execution with conditions and modern arrow switch expressions.",
                "Novice",
                100,
                """Modern Java (Java 14+) introduced switch expressions with arrow syntax (`->`), eliminating accidental fall-through and allowing switches to return values directly.""",
                """public class Main {
    public static void main(String[] args) {
        String role = "ADMIN";
        int accessLevel = switch (role) {
            case "ADMIN" -> 10;
            case "MODERATOR" -> 5;
            default -> 1;
        };
        System.out.println("Access Level: " + accessLevel);
    }
}""",
                "Conditional Evaluation",
                "Write an if condition checking if `xp >= 1000` to print 'Rank: Master'.",
                """public class Main {
    public static void main(String[] args) {
        int xp = 1200;
        if (xp >= 1000) {
            System.out.println("Rank: Master");
        }
    }
}""",
                "Rank: Master",
                "Use `if (xp >= 1000) { System.out.println(\"Rank: Master\"); }`.",
                "What advantage do modern Java arrow switch expressions (case -> ...) provide?",
                ["They prevent accidental fall-through without requiring explicit break statements", "They make code run 10x faster in hardware", "They can only handle integers", "They replace all if-else statements"],
                0,
                "Arrow syntax in modern switch expressions does not fall through, preventing common bugs caused by missing break statements."
            ),
            (
                5,
                "Looping Mechanics: for, while & Enhanced For-Each",
                "Iterate over sequences and traverse collections cleanly.",
                "Novice",
                100,
                """Java provides traditional counting loops and the enhanced `for-each` loop for arrays and iterables:

```java
for (ElementType item : collection) {
    // process item
}
```""",
                """public class Main {
    public static void main(String[] args) {
        String[] languages = {"Java", "C", "Python"};
        for (String lang : languages) {
            System.out.println("Supported: " + lang);
        }
    }
}""",
                "Enhanced For Loop",
                "Iterate through an array of numbers `{1, 2, 3}` and print their sum.",
                """public class Main {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        int sum = 0;
        for (int n : nums) {
            sum += n;
        }
        System.out.println("Sum: " + sum);
    }
}""",
                "Sum: 6",
                "Use `for (int n : nums)` to accumulate into `sum`.",
                "Can you modify the size of a standard Java array during runtime?",
                ["No, Java arrays have fixed sizes once initialized", "Yes, using array.push()", "Yes, arrays are automatically dynamic", "Only if declared with final"],
                0,
                "Standard arrays in Java have fixed length. For dynamic resizing, use ArrayList from the Collections framework."
            ),
            (
                6,
                "Methods, Parameters & Overloading",
                "Define modular functions, pass parameters by value, and overload signatures.",
                "Apprentice",
                120,
                """In Java, all methods exist inside classes.

### Important Java Rule
Java is strictly **Pass-By-Value**. For object references, the value passed to the method is the copy of the memory reference handle.

### Method Overloading
Multiple methods can share the same name as long as their parameter lists (types, number of parameters) differ.""",
                """public class Main {
    static int multiply(int a, int b) { return a * b; }
    static double multiply(double a, double b) { return a * b; }

    public static void main(String[] args) {
        System.out.println("Int: " + multiply(4, 5));
        System.out.println("Double: " + multiply(2.5, 4.0));
    }
}""",
                "Overloaded Greeter",
                "Create a static method `greet()` printing 'Hello' and `greet(String name)` printing 'Hello ' + name.",
                """public class Main {
    static void greet() { System.out.println("Hello"); }
    static void greet(String name) { System.out.println("Hello " + name); }

    public static void main(String[] args) {
        greet("Quest");
    }
}""",
                "Hello Quest",
                "Implement the method taking String name and call `greet(\"Quest\");`.",
                "What determines method overloading in Java?",
                ["Method name and parameter types/count (method signature)", "Return type alone", "Access modifier alone (public vs private)", "Throws declaration alone"],
                0,
                "Methods are overloaded when they share the same name but differ in parameter count or parameter types. Return type alone is insufficient."
            ),
            (
                7,
                "OOP Foundations: Classes, Objects & Heap Memory",
                "Instantiate objects, manage state, and understand Garbage Collection.",
                "Apprentice",
                120,
                """An Object is an instance of a Class.
- Class: Blueprint / Template defining fields and behaviors.
- Object: Physical manifestation residing in JVM Heap memory.

When an object has no active references pointing to it, the JVM Garbage Collector reclaims its memory automatically.""",
                """class Hero {
    String name;
    int health = 100;

    void takeDamage(int amount) {
        health -= amount;
        System.out.println(name + " now has " + health + " HP.");
    }
}

public class Main {
    public static void main(String[] args) {
        Hero h = new Hero();
        h.name = "Arthur";
        h.takeDamage(20);
    }
}""",
                "Instantiate Custom Object",
                "Instantiate an object of class Player, set its score to 500, and print it.",
                """class Player {
    int score;
}

public class Main {
    public static void main(String[] args) {
        Player p = new Player();
        p.score = 500;
        System.out.println("Player Score: " + p.score);
    }
}""",
                "Player Score: 500",
                "Create `new Player()`, assign `p.score = 500`, and print.",
                "Where are Java objects stored in JVM runtime memory?",
                ["In the Heap", "In the Thread Call Stack", "In the Program Counter Register", "In the CPU Cache L1"],
                0,
                "All Java object instances are allocated on the Heap memory area, managed by Garbage Collection."
            ),
            (
                8,
                "Constructors, Overloading & the 'this' Keyword",
                "Initialize object state cleanly using constructor parameters and explicit this references.",
                "Apprentice",
                120,
                """A constructor is a special method called automatically when an object is instantiated with `new`.
- Has no return type.
- Matches class name exactly.
- The `this` keyword references the current invoking object instance.""",
                """class Character {
    private String name;
    private int level;

    public Character(String name, int level) {
        this.name = name;
        this.level = level;
    }

    public void display() {
        System.out.println("Character: " + name + " (Lvl " + level + ")");
    }
}

public class Main {
    public static void main(String[] args) {
        Character c = new Character("Gandalf", 99);
        c.display();
    }
}""",
                "Parameterized Constructor",
                "Write a Car class with a constructor taking `(String model)` and print it.",
                """class Car {
    String model;
    public Car(String model) {
        this.model = model;
    }
}

public class Main {
    public static void main(String[] args) {
        Car c = new Car("Tesla");
        System.out.println("Car: " + c.model);
    }
}""",
                "Car: Tesla",
                "Declare constructor initializing `this.model = model`.",
                "What default constructor does Java provide if no constructor is explicitly written?",
                ["A no-argument default constructor", "A constructor accepting null", "Java creates no default constructor", "A parameterized constructor matching all fields"],
                0,
                "The Java compiler automatically synthesizes a default no-argument constructor if no constructor is defined."
            ),
            (
                9,
                "Encapsulation: Access Modifiers & JavaBeans",
                "Protect internal state using private fields, getters, setters, and invariants.",
                "Apprentice",
                140,
                """Encapsulation bundles data with the methods that operate on that data and hides internal details.

### Access Modifiers
1. `private`: Accessible only within the declaring class.
2. `default` (package-private): Accessible within the same package.
3. `protected`: Accessible within package and subclasses.
4. `public`: Accessible from any class anywhere.""",
                """class BankAccount {
    private double balance;

    public void deposit(double amount) {
        if (amount > 0) balance += amount;
    }

    public double getBalance() {
        return balance;
    }
}

public class Main {
    public static void main(String[] args) {
        BankAccount acc = new BankAccount();
        acc.deposit(250.0);
        System.out.println("Balance: " + acc.getBalance());
    }
}""",
                "Encapsulated Score Counter",
                "Create a class with a private score field and a public getter.",
                """class GameScore {
    private int score = 100;
    public int getScore() { return score; }
}

public class Main {
    public static void main(String[] args) {
        GameScore gs = new GameScore();
        System.out.println("Score: " + gs.getScore());
    }
}""",
                "Score: 100",
                "Use `private int score` and `public int getScore()`.",
                "Which access modifier restricts visibility strictly to the enclosing class?",
                ["private", "protected", "default", "public"],
                0,
                "The 'private' modifier guarantees that members cannot be accessed from outside the class."
            ),
            (
                10,
                "Inheritance: 'extends', 'super' & Method Overriding",
                "Build class hierarchies, reuse parent logic, and override specialized behavior.",
                "Apprentice",
                140,
                """Inheritance allows a subclass to inherit fields and methods from a superclass using the `extends` keyword.

### Essential Rules
- Java supports **single class inheritance** (a class can extend only one superclass).
- `super()` calls the parent constructor.
- `@Override` annotation tells the compiler you intend to override a superclass method.""",
                """class Animal {
    void speak() { System.out.println("Generic sound"); }
}

class Dog extends Animal {
    @Override
    void speak() { System.out.println("Woof! Woof!"); }
}

public class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.speak();
    }
}""",
                "Subclass Method Override",
                "Create a subclass Bot extending Robot and override greet() to print 'Beep Boop'.",
                """class Robot {
    void greet() { System.out.println("Hello"); }
}

class Bot extends Robot {
    @Override
    void greet() { System.out.println("Beep Boop"); }
}

public class Main {
    public static void main(String[] args) {
        Bot b = new Bot();
        b.greet();
    }
}""",
                "Beep Boop",
                "Extend Robot and override greet with println('Beep Boop').",
                "Can a Java class inherit from multiple superclasses simultaneously using 'extends'?",
                ["No, Java only allows single inheritance of classes", "Yes, using comma separated class names", "Yes, up to 3 superclasses", "Only if all superclasses are abstract"],
                0,
                "Java prohibits multiple class inheritance to avoid ambiguity (the diamond problem), though multiple interfaces can be implemented."
            ),
            (
                11,
                "Polymorphism & Dynamic Method Dispatch",
                "Decouple references from concrete implementations at runtime.",
                "Adept",
                150,
                """Polymorphism allows objects of different classes to be treated through a common superclass reference.

```java
Shape s = new Circle(); // Superclass reference, subclass instance
s.draw(); // Invokes Circle's draw() at runtime via Dynamic Method Dispatch!
```""",
                """abstract class Spell {
    abstract void cast();
}

class Fireball extends Spell {
    void cast() { System.out.println("Casting explosive Fireball!"); }
}

class Frostbolt extends Spell {
    void cast() { System.out.println("Casting freezing Frostbolt!"); }
}

public class Main {
    public static void main(String[] args) {
        Spell currentSpell = new Fireball();
        currentSpell.cast();
    }
}""",
                "Polymorphic Reference Execution",
                "Declare a superclass reference pointing to a subclass and invoke its overridden method.",
                """class Instrument {
    void play() { System.out.println("Noise"); }
}
class Guitar extends Instrument {
    void play() { System.out.println("Guitar Riff"); }
}

public class Main {
    public static void main(String[] args) {
        Instrument inst = new Guitar();
        inst.play();
    }
}""",
                "Guitar Riff",
                "Assign `Instrument inst = new Guitar();` and call `inst.play()`.",
                "What mechanism in the JVM decides which overridden method to execute at runtime?",
                ["Dynamic Method Dispatch (Virtual Method Invocation)", "Static Bytecode Binding", "Garbage Collection Table", "Pre-processor macro expansion"],
                0,
                "Dynamic method dispatch looks up the concrete object's actual class in the virtual method table (vtable) at runtime."
            ),
            (
                12,
                "Abstract Classes vs Interfaces: Architecture Contracts",
                "Define architectural blueprints using interfaces, default methods, and abstractions.",
                "Adept",
                150,
                """### Interfaces vs Abstract Classes
- **Interface**: Pure contract defining *what* a class does (`implements`). Can contain default and static methods. A class can implement **multiple** interfaces!
- **Abstract Class**: Defines *what* and partial *how* (`extends`). Can hold state/constructors.""",
                """interface Flyable {
    void fly();
}

interface CombatReady {
    void attack();
}

class Dragon implements Flyable, CombatReady {
    public void fly() { System.out.println("Soaring through clouds."); }
    public void attack() { System.out.println("Breathes dragon fire!"); }
}

public class Main {
    public static void main(String[] args) {
        Dragon d = new Dragon();
        d.fly();
        d.attack();
    }
}""",
                "Interface Implementation",
                "Implement an interface `Drawable` with method `draw()` in a class `Square`.",
                """interface Drawable {
    void draw();
}

class Square implements Drawable {
    public void draw() { System.out.println("Drawing Square"); }
}

public class Main {
    public static void main(String[] args) {
        Drawable d = new Square();
        d.draw();
    }
}""",
                "Drawing Square",
                "Implement Drawable and print 'Drawing Square'.",
                "Can a Java class implement more than one interface?",
                ["Yes, multiple interfaces can be implemented separated by commas", "No, Java strictly limits interfaces to one", "Only if the class is abstract", "Only in Java Enterprise Edition"],
                0,
                "A Java class can implement any number of interfaces, enabling flexible, decoupled architectures."
            ),
            (
                13,
                "Deep Dive: Strings, String Pool & StringBuilder",
                "Understand String immutability, the heap String Constant Pool, and mutable StringBuilder.",
                "Adept",
                150,
                """In Java, `String` objects are **immutable**! Once created, their character contents cannot be altered.

### The String Constant Pool
Literal strings like `"hello"` reside in a shared memory pool to conserve RAM.

### StringBuilder
When concatenating loops of strings, standard `+` creates countless throwaway objects! Always use mutable `StringBuilder` for high performance.""",
                """public class Main {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= 3; i++) {
            sb.append("Quest").append(i).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}""",
                "StringBuilder Construction",
                "Use StringBuilder to append 'AI' and ' Platform' and print the final String.",
                """public class Main {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();
        sb.append("AI").append(" Platform");
        System.out.println(sb.toString());
    }
}""",
                "AI Platform",
                "Append both words and print `sb.toString()`.",
                "Why are Java String objects immutable?",
                ["For thread safety, security, caching, and String Constant Pool efficiency", "Because Java lacks dynamic memory", "Because primitive types cannot be modified", "To prevent inheritance from Object"],
                0,
                "Immutability enables safe sharing in the String Pool, thread safety across concurrent workers, and security for class loading/networking."
            ),
            (
                14,
                "Exception Architecture: Try, Catch, Finally & Custom",
                "Build fault-tolerant systems using checked vs unchecked exceptions and try-with-resources.",
                "Adept",
                180,
                """Exceptions prevent programs from crashing abruptly when errors occur.

### Exception Hierarchy
`Throwable` -> `Error` (unrecoverable system failure) and `Exception`.
- **Checked**: Must be declared or caught (e.g. `IOException`).
- **Unchecked (RuntimeException)**: Bugs in programming logic (e.g. `NullPointerException`, `IndexOutOfBoundsException`).

### Try-With-Resources
Automatically closes `AutoCloseable` streams (sockets, database connections, files).""",
                """public class Main {
    public static void main(String[] args) {
        try {
            int result = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Handled division by zero gracefully!");
        } finally {
            System.out.println("Finally block always executes.");
        }
    }
}""",
                "Safe Try-Catch Block",
                "Catch an ArrayIndexOutOfBoundsException safely and print 'Out of bounds caught'.",
                """public class Main {
    public static void main(String[] args) {
        try {
            int[] arr = new int[2];
            int x = arr[5];
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Out of bounds caught");
        }
    }
}""",
                "Out of bounds caught",
                "Wrap index access in try-catch catching ArrayIndexOutOfBoundsException.",
                "Which block in a try-catch construct is guaranteed to execute regardless of whether an exception was thrown?",
                ["finally block", "catch block", "throw block", "default block"],
                0,
                "The finally block always executes after try and catch blocks finish, ensuring cleanup of resources."
            ),
            (
                15,
                "Collections Framework: ArrayList, LinkedList & Sets",
                "Harness dynamic collections, iteration, sorting, and fast lookups.",
                "Adept",
                180,
                """The Java Collections Framework (`java.util`) provides pre-built, optimized data structures:

- `ArrayList<E>`: Dynamic resizable array with $O(1)$ random access.
- `LinkedList<E>`: Doubly-linked list with fast insertions.
- `HashSet<E>`: Unordered collection that guarantees **no duplicate elements** with $O(1)$ lookups.""",
                """import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> quests = new ArrayList<>();
        quests.add("Dragon Slayer");
        quests.add("Dungeon Run");
        Collections.sort(quests);

        System.out.println("Sorted: " + quests);
    }
}""",
                "ArrayList Addition and Count",
                "Add three strings to an ArrayList and print its size.",
                """import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("C");
        list.add("Java");
        list.add("Python");
        System.out.println("Size: " + list.size());
    }
}""",
                "Size: 3",
                "Instantiate `new ArrayList<String>()`, add elements, print `list.size()`.",
                "Which collection implementation guarantees that all elements are unique (no duplicates)?",
                ["Set (such as HashSet)", "List (such as ArrayList)", "Vector", "Queue"],
                0,
                "Sets model mathematical sets and prohibit duplicate entries."
            ),
            (
                16,
                "Key-Value Mastery: HashMap & Fast Hash Lookups",
                "Store and retrieve data in constant $O(1)$ time using key-value hashes.",
                "Adept",
                180,
                """A `HashMap<K, V>` stores associations between keys and values based on the key's `hashCode()`.

### Key Methods
- `put(key, value)`: Inserts or updates key.
- `get(key)`: Retrieves value in $O(1)$ average time.
- `containsKey(key)`: Fast existence check.
- `getOrDefault(key, defaultVal)`: Safe fallback retrieval.""",
                """import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        HashMap<String, Integer> inventory = new HashMap<>();
        inventory.put("Health Potion", 5);
        inventory.put("Mana Crystal", 2);

        System.out.println("Potions available: " + inventory.get("Health Potion"));
    }
}""",
                "HashMap Entry Retrieval",
                "Store a user's XP in a HashMap and print the retrieved value.",
                """import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        HashMap<String, Integer> xpMap = new HashMap<>();
        xpMap.put("Alice", 1500);
        System.out.println("Alice XP: " + xpMap.get("Alice"));
    }
}""",
                "Alice XP: 1500",
                "Put Alice with 1500 and retrieve with `xpMap.get(\"Alice\")`.",
                "What is the average time complexity of get(key) in a HashMap?",
                ["O(1) constant time", "O(N) linear time", "O(N log N)", "O(log N)"],
                0,
                "Hash maps calculate the bucket index via hash code, providing O(1) average lookup time."
            ),
            (
                17,
                "Generics: Type Safety & Generic Classes",
                "Write type-safe, reusable components that catch bugs at compile-time.",
                "Master",
                200,
                """Generics eliminate explicit type casting and prevent `ClassCastException` runtime errors.

### Type Parameters
- `<T>`: Type
- `<E>`: Element
- `<K, V>`: Key, Value

Through **Type Erasure**, the compiler verifies type safety at compile time and strips the generic metadata in the generated bytecode for backward compatibility.""",
                """class Box<T> {
    private T item;
    public void set(T item) { this.item = item; }
    public T get() { return item; }
}

public class Main {
    public static void main(String[] args) {
        Box<String> stringBox = new Box<>();
        stringBox.set("Legendary Sword");
        System.out.println("Box holds: " + stringBox.get());
    }
}""",
                "Generic Box Implementation",
                "Create a generic Box<Integer> holding 42 and print its value.",
                """class Container<T> {
    T val;
    Container(T val) { this.val = val; }
}

public class Main {
    public static void main(String[] args) {
        Container<Integer> c = new Container<>(42);
        System.out.println("Contained: " + c.val);
    }
}""",
                "Contained: 42",
                "Use `new Container<Integer>(42)` and print its value.",
                "What process does the Java compiler perform on generics during compilation?",
                ["Type Erasure (replaces type parameters with bounds/Object)", "Heap re-allocation", "Just-In-Time native translation", "Bytecode duplication per type"],
                0,
                "Java implements generics via Type Erasure, replacing generic parameters with Object (or bounds) in the compiled bytecode."
            ),
            (
                18,
                "Streams API & Lambda Expressions: Functional Java",
                "Transform, filter, and map data pipelines declaratively.",
                "Master",
                200,
                """Java 8 revolutionized programming with functional Streams and Lambda syntax:

```java
List<String> names = list.stream()
    .filter(s -> s.startsWith("A"))
    .map(String::toUpperCase)
    .collect(Collectors.toList());
```""",
                """import java.util.List;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6);
        long evenCount = numbers.stream()
                               .filter(n -> n % 2 == 0)
                               .count();

        System.out.println("Even Numbers Count: " + evenCount);
    }
}""",
                "Stream Filter and Print",
                "Filter an array of numbers to count those greater than 10.",
                """import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        long count = Arrays.asList(5, 12, 18, 7)
                           .stream()
                           .filter(x -> x > 10)
                           .count();
        System.out.println("Count: " + count);
    }
}""",
                "Count: 2",
                "Filter with `x -> x > 10` and count.",
                "Which operation terminates a Java stream and triggers pipeline execution?",
                ["Terminal operations (like collect, count, forEach)", "Intermediate operations (filter, map)", "peek()", "sorted()"],
                0,
                "Intermediate operations are lazy and do not execute until a terminal operation (like collect, count, forEach) is called."
            ),
            (
                19,
                "Multithreading & Concurrency: Threads & Synchronization",
                "Execute parallel tasks concurrently, share thread states safely, and avoid deadlocks.",
                "Master",
                220,
                """Modern CPUs feature multiple cores. Java supports multithreading out-of-the-box via `Thread` and `Runnable`.

### Thread Safety & Synchronization
When multiple threads read and write shared variables simultaneously, race conditions occur. Use the `synchronized` keyword, `AtomicInteger`, or `ReentrantLock` to protect critical sections.""",
                """class Worker implements Runnable {
    public void run() {
        System.out.println("Background worker thread running: " + 
                           Thread.currentThread().getName());
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Thread t = new Thread(new Worker());
        t.start();
        t.join(); // Wait for thread completion
        System.out.println("Main thread resumed.");
    }
}""",
                "Thread Spawning",
                "Create a thread with a lambda Runnable and start it.",
                """public class Main {
    public static void main(String[] args) throws Exception {
        Thread t = new Thread(() -> System.out.println("Thread Active"));
        t.start();
        t.join();
    }
}""",
                "Thread Active",
                "Use `new Thread(() -> System.out.println(\"Thread Active\")).start();`.",
                "Which method must be called to begin execution of a new Thread instance?",
                ["start()", "run()", "execute()", "init()"],
                0,
                "Calling start() instructs the JVM to spawn an OS thread and execute run(). Calling run() directly merely runs on the current thread."
            ),
            (
                20,
                "Grandmaster Capstone: Enterprise Event Bus & Task Worker",
                "Synthesize OOP, Generics, Concurrency, and Stream pipelines into a production architecture.",
                "Master",
                250,
                """Congratulations on conquering all 20 levels of the Java Curriculum!

You now command the complete Java ecosystem:
1. JVM internals & Memory Model
2. Enterprise OOP & Design Patterns
3. Generic Collections & High-speed Maps
4. Functional Streams & Declarative Pipelines
5. Concurrency & Multi-threaded Task Scheduling

You are equipped to build massive microservices, scalable Spring Boot backends, Android platforms, and enterprise clouds!""",
                """import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        ExecutorService pool = Executors.newFixedThreadPool(2);
        pool.submit(() -> System.out.println("Quest Java Grandmaster Engine Running!"));
        pool.shutdown();
    }
}""",
                "Java Grandmaster Certification",
                "Print the final capstone message 'Java Master Completed'.",
                """public class Main {
    public static void main(String[] args) {
        System.out.println("Java Master Completed");
    }
}""",
                "Java Master Completed",
                "Print 'Java Master Completed' to complete Level 20.",
                "What enterprise framework is most widely used globally for building Java microservices and REST APIs?",
                ["Spring Boot", "Swing", "JavaFX", "Applet Engine"],
                0,
                "Spring Boot and the Spring Framework are the undisputed enterprise standard for Java backend microservices and APIs."
            )
        ]

        # Insert C Modules
        for mod in c_modules_data:
            lvl_num, title, summary, diff, xp, concept, code_ex, chal_title, chal_desc, starter, exp_out, hint, q_text, q_opts, q_correct, q_expl = mod
            LevelModule.objects.update_or_create(
                course=c_course,
                level_number=lvl_num,
                defaults={
                    'title': title,
                    'summary': summary,
                    'difficulty': diff,
                    'xp_reward': xp,
                    'concept_content': concept,
                    'code_example': code_ex,
                    'challenge_title': chal_title,
                    'challenge_description': chal_desc,
                    'starter_code': starter,
                    'expected_output': exp_out,
                    'solution_hint': hint,
                    'quiz_question': q_text,
                    'quiz_options': q_opts,
                    'quiz_correct_index': q_correct,
                    'quiz_explanation': q_expl,
                }
            )

        # Insert Java Modules
        for mod in java_modules_data:
            lvl_num, title, summary, diff, xp, concept, code_ex, chal_title, chal_desc, starter, exp_out, hint, q_text, q_opts, q_correct, q_expl = mod
            LevelModule.objects.update_or_create(
                course=java_course,
                level_number=lvl_num,
                defaults={
                    'title': title,
                    'summary': summary,
                    'difficulty': diff,
                    'xp_reward': xp,
                    'concept_content': concept,
                    'code_example': code_ex,
                    'challenge_title': chal_title,
                    'challenge_description': chal_desc,
                    'starter_code': starter,
                    'expected_output': exp_out,
                    'solution_hint': hint,
                    'quiz_question': q_text,
                    'quiz_options': q_opts,
                    'quiz_correct_index': q_correct,
                    'quiz_explanation': q_expl,
                }
            )

        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {Course.objects.count()} courses with {LevelModule.objects.count()} levels!"))
