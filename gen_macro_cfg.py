from os import path

MACRO_CFG_PATH = path.join(
    path.dirname(__file__), "openlane/user_project_wrapper/macro.cfg"
)

ROWS = 1
MUX_COLS = 8
ROW_SPACING = 544
FIRST_ROW_Y = 897.6
LEFT_MUX_X = 46
RIGHT_MUX_X = 2707.10

macrofile = open(MACRO_CFG_PATH, "w")
macrofile.write(f"# Controller\n")
macrofile.write("tt_top1.ctrl_I 1367.12 108.8 N\n")
macrofile.write("\n")

macrofile.write(f"# Muxes\n")
for y in range(ROWS):
    row_y = FIRST_ROW_Y + y * ROW_SPACING
    macrofile.write(f"tt_top1.branch\[{y*2}\].mux_I {LEFT_MUX_X}      {row_y}   N\n")
    macrofile.write(f"tt_top1.branch\[{y*2+1}\].mux_I 1512.48 {row_y}   FN\n")
macrofile.write("\n")

for y in range(ROWS):
    bottom_y = FIRST_ROW_Y + y * ROW_SPACING - 111.52
    top_y = FIRST_ROW_Y + y * ROW_SPACING + 57.12
    mux_idx = y * 2
    macrofile.write(f"# Row {y}\n")

    for x in range(MUX_COLS):
        # Left branch
        pos_x = LEFT_MUX_X + x * 170.66
        macrofile.write(
            f"tt_top1.branch\[{mux_idx}\].col_um\[{x}\].um_top_I.block_{mux_idx+1}_{x}.tt_um_I  {pos_x: <7.2f} {top_y:.2f}   FS\n"
        )
        macrofile.write(
            f"tt_top1.branch\[{mux_idx}\].col_um\[{x}\].um_bot_I.block_{mux_idx}_{x}.tt_um_I  {pos_x: <7.2f} {bottom_y:.2f}   N\n"
        )

        # Right branch
        pos_x = RIGHT_MUX_X - x * 170.66
        macrofile.write(
            f"tt_top1.branch\[{mux_idx+1}\].col_um\[{x}\].um_top_I.block_{mux_idx+1}_{x+16}.tt_um_I {pos_x: <7.2f} {top_y:.2f}   S\n"
        )
        macrofile.write(
            f"tt_top1.branch\[{mux_idx+1}\].col_um\[{x}\].um_bot_I.block_{mux_idx}_{x+16}.tt_um_I {pos_x: <7.2f} {bottom_y:.2f}   FN\n"
        )
    macrofile.write(f"\n")

macrofile.close()
