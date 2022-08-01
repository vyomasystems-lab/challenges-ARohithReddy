# Report MUX
Vyoma's UpTickPro verification environment is used to test this design.
![image](https://user-images.githubusercontent.com/63339312/182153330-354af20c-2888-474b-9fe2-a0502b35ab5f.png)

## verification environment
### I/O of the design:
inputs : \
mav_putvalue_src1 : 32-bits
mav_putvalue_src2 : 32-bits
mav_putvalue_src3 : 32-bits
mav_putvalue_instr : 32-bits
outputs:\
mav_putvalue : 33 bits

##### condition to check the outputs of the design:
output of dut and model are compared by giving common input to both.

## Test Scenario
dut's output is different from the expected output for the following set of inputs.\
```
  f7   | f3 | opcode
--------------------
010000  111  110011
100000  001  110011
100000  101  110011
100000  111  110011
110000  110  110011
110000  111  110011
010100  110  110011
010100  111  110011
110100  110  110011
110100  111  110011
010000  110  010011
010000  111  010011
100000  001  010011
100000  101  010011
100000  110  010011
100000  111  010011
110000  110  010011
110000  111  010011
100100  110  010011
100100  111  010011
010100  110  010011
010100  111  010011
110100  110  010011
110100  111  010011
```

