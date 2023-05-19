# Tiny Tapeout 03p5

* Visit https://tinytapeout.com for more information on the project and how to get involved.

This is a prototype Tiny Tapeout using the new Mux.

## Configure

```
export PDK_ROOT=<some dir>/pdk
export OPENLANE_ROOT=<some dir>/openlane
make setup
git clone https://github.com/TinyTapeout/tt-multiplexer/
```

Then edit `tt-multiplexer/proto/tt_mux.v` and change the value of `N_UM` to 16:

```diff
-	parameter integer N_UM = 8,
+	parameter integer N_UM = 16,
```

## Harden

```
make tt_ctrl
make tt_mux
make user_project_wrapper
```

Note: only `tt_ctrl` and `tt_mux` are currently implemented.