# Report MUX
Vyoma's UpTickPro verification environment is used to test this design.
![image](https://user-images.githubusercontent.com/63339312/182212794-d90cda8d-0c2f-49e4-ae8d-215dc4ae9639.png)

## verification environment
### I/O of the design:
inputs : \
a : 8-bits	(range : 0 to 31)\
b : 8-bits	(range : 0 to 31)\
outputs:\
prod : 16-bits\

##### condition to check the outputs of the design:
```python
if int(dut.prod.value) != in_a*in_b:
  print("a=",in_a,"b=",in_b,"expected value = ",in_a*in_b,"dut output = ",int(dut.prod.value))
```

## Test Scenario
dut's output is different from the expected output for the following set of inputs.\

```
a= 31 b= 9 expected value =  279 dut output =  2583
a= 31 b= 10 expected value =  310 dut output =  2870
a= 31 b= 11 expected value =  341 dut output =  3157
a= 31 b= 12 expected value =  372 dut output =  3444
a= 31 b= 13 expected value =  403 dut output =  3731
a= 31 b= 14 expected value =  434 dut output =  4018
a= 31 b= 15 expected value =  465 dut output =  4305
a= 31 b= 16 expected value =  496 dut output =  240
a= 31 b= 18 expected value =  558 dut output =  814
a= 31 b= 19 expected value =  589 dut output =  1101
a= 31 b= 20 expected value =  620 dut output =  1388
a= 31 b= 21 expected value =  651 dut output =  1675
a= 31 b= 22 expected value =  682 dut output =  1962
a= 31 b= 23 expected value =  713 dut output =  2249
a= 31 b= 24 expected value =  744 dut output =  2536
a= 31 b= 25 expected value =  775 dut output =  2823
a= 31 b= 26 expected value =  806 dut output =  3110
a= 31 b= 27 expected value =  837 dut output =  3397
a= 31 b= 28 expected value =  868 dut output =  3684
a= 31 b= 29 expected value =  899 dut output =  3971
a= 31 b= 30 expected value =  930 dut output =  4258
a= 31 b= 31 expected value =  961 dut output =  4545
```


## design bug
inputs to vedic4x4 are incorrect.
```
  vedic4x4 VD0(a[3:0],b[3:0],mult0);
	vedic4x4 VD1(a[3:0],b[7:4],mult1);
	vedic4x4 VD2(a[7:4],b[3:0],mult2);
	vedic4x4 VD3(a[7:4],b[3:0],mult3);
 ```
intended design
```
  vedic4x4 VD0(a[3:0],b[3:0],mult0);
	vedic4x4 VD1(a[3:0],b[7:4],mult1);
	vedic4x4 VD2(a[7:4],b[3:0],mult2);
	vedic4x4 VD3(a[7:4],b[7:4],mult3);
```

## test strategy
used nested for loop to vary the values of inputs a, b and observed the output.

## is the Verification complete?
Tested the design with all the possible values(0 and 1) for each input and observed the output.\
didn't test the design with values x(undetermined), z(high impedence).
