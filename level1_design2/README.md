# Sequence Detector
Vyoma's UpTickPro verification environment is used to test this design.
![image](https://user-images.githubusercontent.com/63339312/181934596-f0c8d5ac-ab74-4044-8f40-3a0200bd8b4c.png)


## verification environment
### I/O of the design:
inputs : \
clk : 1-bit\
inp_bit : 1-bit	\
reset : 1-bit\
outputs:\
seq_seen : 1-bit\

##### condition to check the outputs of the design:
```python
val = random.randint(0, 1)
dut.inp_bit.value = val  # Assign the random value val to the input port d
await FallingEdge(dut.clk)
v7 = v6
v6 = v5
v5 = v4
v4 = v3
v3 = v2
v2 = v1
v1 = v0
v0 = val
if dut.seq_seen.value == 1 and [v3,v2,v1,v0] != [1,0,1,1] and i >10:
  print("out = 1 for seq",v7,v6,v5,v4,v3,v2,v1,v0)
if dut.seq_seen.value == 0  and [v3,v2,v1,v0] == [1,0,1,1] and i >10:
  print("out = 0 for seq :",v7,v6,v5,v4,v3,v2,v1,v0)
```

## Test Scenario
dut's output is different from the expected output for the following set of inputs.\
---------------------------------------------------------------\
out = 0 for seq : 0 0 0 1 1 0 1 1\
out = 0 for seq : 0 0 1 0 1 0 1 1\
out = 0 for seq : 0 1 0 1 1 0 1 1\
out = 0 for seq : 0 1 1 1 1 0 1 1\
out = 0 for seq : 1 0 0 1 1 0 1 1\
out = 0 for seq : 1 0 1 0 1 0 1 1\
out = 0 for seq : 1 0 1 1 1 0 1 1\
out = 0 for seq : 1 1 0 1 1 0 1 1\
out = 0 for seq : 1 1 1 0 1 0 1 1\
out = 0 for seq : 1 1 1 1 1 0 1 1\

## design bug
![image](https://user-images.githubusercontent.com/63339312/181934934-bf8b1954-93b1-4388-a7be-f57b572f9314.png)



## test strategy
assigned random value to inp_bit.
stored the previous values in variables.
compared the values of variables with the Sequence given.

## is the Verification complete?
Tested design with the random sequence of length 10000, which should cover all the testcases.
