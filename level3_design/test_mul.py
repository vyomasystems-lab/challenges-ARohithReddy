# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mul(dut):
    """Test for mul"""
    #dut.inp30.value = 2
    #dut.sel.value = 30
    dut.a.value = 5
    dut.b.value = 2
    await Timer(2, units="ns")
    #print(dut.prod.value)
    
    for in_a in range(0,32):
        for in_b in range(0,32):
            dut.a.value = in_a
            dut.b.value = in_b
            await Timer(2, units="ns")
            if int(dut.prod.value) != in_a*in_b:
                print("a=",in_a,"b=",in_b,"expected value = ",in_a*in_b,"dut output = ",int(dut.prod.value))

    #cocotb.log.info('##### CTB: Develop your test here ########')
