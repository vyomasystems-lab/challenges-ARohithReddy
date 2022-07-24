# Report MUX
Vyoma's UpTickPro verification environment is used to test this design.
![image](https://user-images.githubusercontent.com/63339312/180651630-12610f97-68dd-4e6d-a602-47541732f2f7.png)

## verification environment
### I/O of the design:
inputs : \
sel : 4-bits	(range : 0 to 31)\
inp0, inp1,.....inp30 : 2 -bits	(range : 0 to 4)\
outputs:\
out : 2-bits\

##### condition to check the outputs of the design:
```python
if ( getattr(dut,"inp" + str(int(dut.sel.value))).value != dut.out.value):
	print("failed for : sel = ",dut.sel.value,", inp"+str(int(dut.sel.value))," = ",getattr(dut,"inp"+str(seq)).value," , out = ",dut.out.value)
```                
The range of sel for the above condition is 0 to 30.

## Test Scenario
dut's output is different from the expected output for the following set of inputs.\
inputs 												|	dut output	| expected output\
--------------------------------------------------------------\
sel =  01100 , inp12  =  11 	| 	  00			| 		11\
sel =  01100 , inp12  =  11 	|  		00			|			11\
sel =  01100 , inp12  =  01 	|  		00			|			01\
sel =  01100 , inp12  =  10 	|  		00			|			10\
sel =  01100 , inp12  =  11 	|  		00			|			11\
sel =  01101 , inp13  =  11 	|  		00			|			11				\\\\ dut's output = inp12\
sel =  01101 , inp13  =  11 	|  		01			|			11				\\\\ dut's output = inp12\
sel =  01101 , inp13  =  11  	|  		10			|			11				\\\\ dut's output = inp12\
sel =  01101 , inp13  =  00  	|  		11			|			10				\\\\ dut's output = inp12\
sel =  01101 , inp13  =  01  	|  		11			|			01				\\\\ dut's output = inp12\
sel =  01101 , inp13  =  10  	|  		11			|			11				\\\\ dut's output = inp12\
sel =  11110 , inp30  =  11  	|  		00			|			01\
sel =  11110 , inp30  =  01  	|  		00			|			10\
sel =  11110 , inp30  =  10  	|  		00			|			10\
sel =  11110 , inp30  =  11  	|  		00			|			11\


## design bug
switch case is logic is incorrect:
```
    case(sel)
      5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;  
      5'b00101: out = inp5;  
      5'b00110: out = inp6;  
      5'b00111: out = inp7;  
      5'b01000: out = inp8;  
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01101: out = inp12;      \\ -> bug,  5'b01100: out = inp12;
      5'b01101: out = inp13;
      5'b01110: out = inp14;
      5'b01111: out = inp15;
      5'b10000: out = inp16;
      5'b10001: out = inp17;
      5'b10010: out = inp18;
      5'b10011: out = inp19;
      5'b10100: out = inp20;
      5'b10101: out = inp21;
      5'b10110: out = inp22;
      5'b10111: out = inp23;
      5'b11000: out = inp24;
      5'b11001: out = inp25;
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;      // ->bug 5'b11110: out = inp30; is not mentioned 
      default: out = 0;
    endcase
```

## test strategy
used nested for loop to vary the values of sel from 0 to 30 and values of inp0,inp1,... inp30 from 0 to 3 and observed the output.

## is the Verification complete?
Tested the design with all the possible values(0 and 1) for each input and observed the output.\
didn't test the design with values x(undetermined), z(high impedence).
