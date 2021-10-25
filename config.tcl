# User config
set script_dir [file dirname [file normalize [info script]]]

set ::env(DESIGN_NAME) wrapped_tpm2137

# save some time
set ::env(RUN_KLAYOUT_XOR) 0
set ::env(RUN_KLAYOUT_DRC) 0

# don't put clock buffers on the outputs, need tristates to be the final cells
set ::env(PL_RESIZER_BUFFER_OUTPUT_PORTS) 0

# Change if needed
set ::env(VERILOG_FILES) "$::env(DESIGN_DIR)/wrapper.v \
    $::env(DESIGN_DIR)/TPM2137/generate/challenge.v"

# make it taller to reach the power rails
set ::env(FP_SIZING) absolute
set ::env(DIE_AREA) "0 0 130 210"

set ::env(SYNTH_DEFINES) "MPRJ_IO_PADS=38"

# Fill this
set ::env(CLOCK_PERIOD) "100"
set ::env(CLOCK_PORT) "wb_clk_i"

set ::env(DESIGN_IS_CORE) 0
set ::env(GLB_RT_MAXLAYER) 5


set ::env(VDD_NETS) [list {vccd1}]
set ::env(GND_NETS) [list {vssd1}]

#set ::env(FP_PIN_ORDER_CFG) $script_dir/pin_order.cfg

set ::env(RUN_CVC) 0
