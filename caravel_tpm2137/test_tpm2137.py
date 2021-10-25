import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles, with_timeout
from cocotbext.uart import UartSource

# takes ~60 seconds on my PC
@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 100, units="ns") # 10 mhz
    cocotb.fork(clock.start())
    
    dut.RSTB.value = 0
    dut.power1.value = 0;
    dut.power2.value = 0;
    dut.power3.value = 0;
    dut.power4.value = 0;

    await ClockCycles(dut.clk, 8)
    dut.power1.value = 1;
    await ClockCycles(dut.clk, 8)
    dut.power2.value = 1;
    await ClockCycles(dut.clk, 8)
    dut.power3.value = 1;
    await ClockCycles(dut.clk, 8)
    dut.power4.value = 1;

    await ClockCycles(dut.clk, 80)
    dut.RSTB.value = 1

    # wait for the project to become active
    await RisingEdge(dut.uut.mprj.wrapped_tpm2137_3.active)

    # check it's closed, leds are active low
    assert dut.led_green == 1
    assert dut.led_red == 0
    assert dut.open == 0

    uart_source = UartSource(dut.uart, baud=115200, bits=8)
    await uart_source.write(b'q3kmvenn')
    await uart_source.wait()

    # wait another few clock cycles
    await ClockCycles(dut.clk_10, 30)

    # check it's open
    assert dut.led_green == 0
    assert dut.led_red == 1
    assert dut.open == 1

